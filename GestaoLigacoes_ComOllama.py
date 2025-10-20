"""
Versão do sistema com controle automático do Ollama
"""
import os
import sys

# Ativar controle automático do Ollama
os.environ['AUTO_OLLAMA'] = 'true'

# Importar e executar o app principal
if __name__ == '__main__':
    from app import app
    
    print("🤖 Iniciando Sistema com Controle Automático do Ollama...")
    print("📱 Acesse: http://localhost:5000")
    print("⚙️ Configurações: http://localhost:5000/configuracoes")
    print("\n💡 O servidor Ollama será iniciado/parado automaticamente!")
    print("   Para parar: Feche esta janela ou pressione Ctrl+C")
    print()
    
    try:
        app.run(debug=False, port=5000)
    except KeyboardInterrupt:
        print("\n👋 Sistema encerrado!")
        sys.exit(0)
