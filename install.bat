@echo off
echo 🔬 LocalResearcherAI - Installation Script (Windows)
echo ==================================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.12+
    exit /b 1
)

echo ✅ Python detected
echo.

REM Check Ollama
ollama --version >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Ollama is not installed
    echo.
    echo Download Ollama from: https://ollama.ai
    echo.
    set /p continue="Continue without Ollama? (y/n): "
    if /i not "%continue%"=="y" exit /b 1
) else (
    echo ✅ Ollama detected
)

echo.
echo 📦 Setting up virtual environment...

REM Create venv
if not exist "venv" (
    python -m venv venv
    echo ✅ Virtual environment created
) else (
    echo ✅ Virtual environment exists
)

REM Activate and install
call venv\Scripts\activate.bat

echo.
echo 📦 Installing dependencies...
python -m pip install --upgrade pip
pip install -e .

echo.
echo 📄 Setting up configuration...
if not exist ".env" (
    copy .env.example .env
    echo ✅ Created .env file
) else (
    echo ✅ .env file exists
)

echo.
echo ✅ Installation complete!
echo.
echo Next steps:
echo   1. Activate virtual environment:
echo      venv\Scripts\activate.bat
echo.
echo   2. Test installation:
echo      localresearcher version
echo.
echo   3. Run example:
echo      localresearcher ask "What are AI trends?" --files examples/sample.md
echo.
echo For more info, see: docs\QUICKSTART.md

pause