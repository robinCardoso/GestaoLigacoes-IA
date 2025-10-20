"""
Gerenciador automático do servidor Ollama
Inicia e para o servidor automaticamente com o executável
"""
import subprocess
import time
import os
import sys
import signal
import atexit

class OllamaManager:
    def __init__(self):
        self.ollama_process = None
        self.auto_start = True
        
    def start_ollama(self):
        """Inicia o servidor Ollama"""
        try:
            # Verificar se já está rodando
            if self.is_ollama_running():
                print("✅ Ollama já está rodando")
                return True
            
            print("🚀 Iniciando servidor Ollama...")
            
            # Iniciar o processo
            if os.name == 'nt':  # Windows
                self.ollama_process = subprocess.Popen(
                    ['ollama', 'serve'],
                    creationflags=subprocess.CREATE_NEW_CONSOLE,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
            else:  # Linux/Mac
                self.ollama_process = subprocess.Popen(
                    ['ollama', 'serve'],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
            
            # Aguardar inicialização
            time.sleep(3)
            
            if self.is_ollama_running():
                print("✅ Servidor Ollama iniciado com sucesso!")
                return True
            else:
                print("❌ Falha ao iniciar servidor Ollama")
                return False
                
        except FileNotFoundError:
            print("❌ Ollama não encontrado. Instale em: https://ollama.ai/download")
            return False
        except Exception as e:
            print(f"❌ Erro ao iniciar Ollama: {e}")
            return False
    
    def stop_ollama(self):
        """Para o servidor Ollama"""
        try:
            print("⏹️ Parando servidor Ollama...")
            
            if self.ollama_process:
                self.ollama_process.terminate()
                self.ollama_process.wait(timeout=5)
                self.ollama_process = None
            
            # Tentar parar outros processos Ollama
            if os.name == 'nt':  # Windows
                subprocess.run(['taskkill', '/f', '/im', 'ollama.exe'], 
                             capture_output=True)
            else:  # Linux/Mac
                subprocess.run(['pkill', '-f', 'ollama serve'], 
                             capture_output=True)
            
            time.sleep(2)
            print("✅ Servidor Ollama parado")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao parar Ollama: {e}")
            return False
    
    def is_ollama_running(self):
        """Verifica se o Ollama está rodando"""
        try:
            import requests
            response = requests.get('http://localhost:11434/api/tags', timeout=2)
            return response.status_code == 200
        except:
            return False
    
    def cleanup(self):
        """Limpeza ao sair"""
        if self.auto_start and self.ollama_process:
            self.stop_ollama()

# Instância global
ollama_manager = OllamaManager()

def setup_ollama_auto_control():
    """Configura controle automático do Ollama"""
    # Registrar função de limpeza
    atexit.register(ollama_manager.cleanup)
    
    # Configurar handler para Ctrl+C
    def signal_handler(signum, frame):
        print("\n🛑 Encerrando sistema...")
        ollama_manager.cleanup()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Iniciar Ollama automaticamente
    if ollama_manager.auto_start:
        ollama_manager.start_ollama()

if __name__ == '__main__':
    # Teste do gerenciador
    setup_ollama_auto_control()
    
    print("🤖 Gerenciador Ollama ativo!")
    print("Pressione Ctrl+C para parar...")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Encerrando...")
