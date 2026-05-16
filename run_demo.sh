#!/bin/bash
# DevOnboard AI - Quick Start Script for Unix/Linux/macOS
# This script starts both the backend and Streamlit app

echo "========================================"
echo "  DevOnboard AI - IBM Hackathon Demo"
echo "  Powered by IBM watsonx.ai Granite"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.9+ from https://www.python.org/"
    exit 1
fi

echo "[1/4] Checking backend setup..."
if [ ! -f "backend/.env" ]; then
    echo "WARNING: backend/.env not found"
    echo "Please copy backend/.env.example to backend/.env and configure it"
    exit 1
fi

echo "[2/4] Checking Streamlit setup..."
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    echo "BACKEND_URL=http://localhost:8000" > .env
fi

echo "[3/4] Starting FastAPI backend..."
cd backend
python3 api.py &
BACKEND_PID=$!
cd ..
sleep 3

echo "[4/4] Starting Streamlit app..."
echo ""
echo "========================================"
echo "  Opening Streamlit in your browser..."
echo "  Backend: http://localhost:8000"
echo "  Frontend: http://localhost:8501"
echo "========================================"
echo ""
echo "Press Ctrl+C to stop the demo"
echo ""

# Trap Ctrl+C to kill both processes
trap "kill $BACKEND_PID; exit" INT

streamlit run streamlit_app.py

# Cleanup
kill $BACKEND_PID

# Made with Bob
