"""
Script Python para iniciar o Sistema de Gestão de Ligações
Abre automaticamente o navegador
"""
import subprocess
import webbrowser
import time
import sys
import os
from threading import Timer

def abrir_navegador():
    """Abre o navegador após 2 segundos"""
    time.sleep(2)
    webbrowser.open('http://localhost:5000')

def main():
    print("=" * 60)
    print("📞 Sistema de Gestão de Ligações com IA")
    print("=" * 60)
    print()
    print("🚀 Iniciando o servidor...")
    print()
    print("📱 O sistema será aberto automaticamente no navegador")
    print("   URL: http://localhost:5000")
    print()
    print("💡 Para parar: Pressione Ctrl+C nesta janela")
    print()
    print("=" * 60)
    print()
    
    # Iniciar timer para abrir o navegador
    timer = Timer(2.0, abrir_navegador)
    timer.daemon = True
    timer.start()
    
    # Verificar se está na pasta correta
    if not os.path.exists('app.py'):
        print("❌ ERRO: app.py não encontrado!")
        print("   Execute este script da pasta do projeto.")
        input("Pressione ENTER para sair...")
        sys.exit(1)
    
    # Verificar dependências
    try:
        import flask
        import requests
    except ImportError:
        print("📦 Instalando dependências necessárias...")
        print()
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print()
        print("✅ Dependências instaladas!")
        print()
    
    # Iniciar o aplicativo Flask
    try:
        subprocess.run([sys.executable, 'app.py'])
    except KeyboardInterrupt:
        print()
        print("=" * 60)
        print("👋 Sistema encerrado. Até logo!")
        print("=" * 60)
        sys.exit(0)

if __name__ == '__main__':
    main()

