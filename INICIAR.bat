@echo off
chcp 65001 > nul
cls
echo ╔════════════════════════════════════════════════════╗
echo ║  📞 Sistema de Gestão de Ligações com IA          ║
echo ╚════════════════════════════════════════════════════╝
echo.
echo 🚀 Iniciando o sistema...
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERRO: Python não encontrado!
    echo.
    echo Por favor, instale o Python em: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

REM Verificar se as dependências estão instaladas
echo 📦 Verificando dependências...
python -c "import flask" >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo 📥 Instalando dependências necessárias...
    echo.
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo.
        echo ❌ Erro ao instalar dependências!
        pause
        exit /b 1
    )
)

echo.
echo ✅ Tudo pronto!
echo.
echo ═══════════════════════════════════════════════════
echo   O sistema será aberto automaticamente no seu
echo   navegador em: http://localhost:5000
echo ═══════════════════════════════════════════════════
echo.
echo 💡 Para parar o sistema: Feche esta janela ou
echo    pressione Ctrl+C
echo.
echo ═══════════════════════════════════════════════════
echo.

REM Aguardar 2 segundos e abrir o navegador
timeout /t 2 /nobreak >nul
start http://localhost:5000

REM Iniciar o aplicativo
echo.
echo 🤖 Iniciando com controle automático do Ollama...
set AUTO_OLLAMA=true
python app.py

pause

