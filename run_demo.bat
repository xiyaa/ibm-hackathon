@echo off
REM DevOnboard AI - Quick Start Script for Windows
REM This script starts both the backend and Streamlit app

echo ========================================
echo   DevOnboard AI - IBM Hackathon Demo
echo   Powered by IBM watsonx.ai Granite
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/4] Checking backend setup...
if not exist "backend\.env" (
    echo WARNING: backend\.env not found
    echo Please copy backend\.env.example to backend\.env and configure it
    pause
    exit /b 1
)

echo [2/4] Checking Streamlit setup...
if not exist ".env" (
    echo Creating .env file...
    echo BACKEND_URL=http://localhost:8000 > .env
)

echo [3/4] Starting FastAPI backend...
start "DevOnboard Backend" cmd /k "cd backend && python api.py"
timeout /t 3 /nobreak >nul

echo [4/4] Starting Streamlit app...
echo.
echo ========================================
echo   Opening Streamlit in your browser...
echo   Backend: http://localhost:8000
echo   Frontend: http://localhost:8501
echo ========================================
echo.
echo Press Ctrl+C to stop the demo
echo.

python -m streamlit run streamlit_app.py

pause

@REM Made with Bob
