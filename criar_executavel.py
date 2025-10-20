"""
Script para criar executável do Sistema de Gestão de Ligações
"""
import os
import sys
import subprocess

def criar_executavel():
    print("=" * 60)
    print("🏗️  CRIADOR DE EXECUTÁVEL - Sistema de Gestão de Ligações")
    print("=" * 60)
    print()
    
    # Verificar se PyInstaller está instalado
    try:
        import PyInstaller
        print("✅ PyInstaller encontrado")
    except ImportError:
        print("❌ PyInstaller não encontrado. Instalando...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstaller instalado com sucesso!")
    
    print()
    print("📦 Criando executável...")
    print("   Isso pode levar alguns minutos...")
    print()
    
    # Comando para criar o executável
    cmd = [
        'pyinstaller',
        '--name=GestaoLigacoes',
        '--onefile',
        '--windowed',
        '--add-data=templates;templates',
        '--add-data=ollama_manager.py;.',
        '--icon=NONE',
        '--hidden-import=flask',
        '--hidden-import=requests',
        '--hidden-import=json',
        '--hidden-import=base64',
        '--hidden-import=subprocess',
        '--hidden-import=threading',
        '--hidden-import=time',
        '--hidden-import=signal',
        '--hidden-import=atexit',
        '--hidden-import=ollama_manager',
        'app.py'
    ]
    
    try:
        # Executar PyInstaller
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        print()
        print("=" * 60)
        print("✅ EXECUTÁVEL CRIADO COM SUCESSO!")
        print("=" * 60)
        print()
        print("📁 Localização: dist/GestaoLigacoes.exe")
        print()
        print("📝 Instruções:")
        print("   1. Vá até a pasta 'dist'")
        print("   2. Execute 'GestaoLigacoes.exe'")
        print("   3. O sistema abrirá automaticamente no navegador")
        print()
        print("💡 Dica: Você pode criar um atalho no Desktop para")
        print("   facilitar o acesso!")
        print()
        print("⚠️  Lembre-se:")
        print("   - Para usar Ollama: tenha-o instalado e rodando")
        print("   - Para usar Gemini: configure sua API Key no sistema")
        print()
        
    except subprocess.CalledProcessError as e:
        print()
        print("❌ ERRO ao criar executável!")
        print()
        print("Detalhes:", e.stderr)
        print()
        print("💡 Tente instalar novamente o PyInstaller:")
        print("   pip install --upgrade pyinstaller")
        return False
    
    return True

if __name__ == '__main__':
    print()
    criar_executavel()
    print()
    input("Pressione ENTER para sair...")

