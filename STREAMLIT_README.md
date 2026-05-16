# DevOnboard AI - Streamlit Demo App

🚀 **AI-Powered Developer Onboarding Assistant**

An interactive Streamlit demo application that showcases DevOnboard AI's capabilities using **IBM watsonx.ai Granite models** for intelligent code analysis and developer onboarding.

![IBM watsonx.ai](https://img.shields.io/badge/Powered%20by-IBM%20watsonx.ai-0f62fe?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?style=for-the-badge)

---

## 🎯 Features

- **🧠 AI-Powered Analysis**: Leverages IBM watsonx.ai Granite models for deep code understanding
- **📖 Comprehensive Onboarding Guides**: Auto-generated documentation for any GitHub repository
- **🗂️ Interactive File Tree**: Browse repository structure with language detection
- **💬 Context-Aware Chat**: Ask questions about the codebase and get intelligent responses
- **🎨 IBM Carbon Design**: Professional dark theme inspired by IBM's design system
- **⚡ Fast & Efficient**: Intelligent caching for quick repeated analyses

---

## 📋 Prerequisites

Before running the Streamlit demo app, ensure you have:

1. **Python 3.9+** installed
2. **FastAPI Backend** running (see backend setup below)
3. **IBM watsonx.ai credentials** (API key and Project ID)
4. **Git** installed on your system

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd ibm-hackathon
```

### 2. Set Up Backend (FastAPI)

First, ensure the backend is running:

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install backend dependencies
pip install -r requirements.txt

# Create .env file with your credentials
cp .env.example .env
# Edit .env and add your IBM watsonx.ai credentials

# Start the FastAPI backend
python api.py
```

The backend should now be running at `http://localhost:8000`

### 3. Set Up Streamlit App

In a new terminal:

```bash
# From project root
cd ibm-hackathon

# Create virtual environment (or use the same one)
python -m venv venv-streamlit

# Activate virtual environment
# On Windows:
venv-streamlit\Scripts\activate
# On macOS/Linux:
source venv-streamlit/bin/activate

# Install Streamlit dependencies
pip install -r requirements-streamlit.txt

# Create .env file for Streamlit
echo "BACKEND_URL=http://localhost:8000" > .env

# Run the Streamlit app
streamlit run streamlit_app.py
```

The Streamlit app will open automatically in your browser at `http://localhost:8501`

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```bash
# Backend API URL
BACKEND_URL=http://localhost:8000

# Optional: Custom port for Streamlit
# STREAMLIT_PORT=8501
```

### Backend Configuration

Ensure your `backend/.env` file contains:

```bash
# IBM watsonx.ai Configuration
WATSONX_API_KEY=your_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-13b-chat-v2

# Application Settings
REPO_CLONE_DIR=/tmp/repos
MAX_REPO_SIZE_MB=500
CACHE_TTL_DAYS=7

# API Settings
API_HOST=0.0.0.0
API_PORT=8000
CORS_ORIGINS=http://localhost:3000,http://localhost:5173,http://localhost:8501

# Logging
LOG_LEVEL=INFO
```

---

## 🎨 Using the Demo App

### Step 1: Enter Repository URL

1. In the sidebar, enter a GitHub repository URL
   - Example: `https://github.com/tiangolo/fastapi`
2. Optionally change the branch (default: `main`)
3. Click **"🔍 Analyze Repository"**

### Step 2: Watch the Analysis

The app will show real-time progress:
- ⏳ Cloning repository from GitHub
- 🔍 Analyzing code structure
- 🧠 Generating AI insights with IBM watsonx.ai Granite
- ✅ Analysis complete!

### Step 3: Explore the Onboarding Guide

The AI-generated guide includes:
- **📖 Project Overview**: High-level description and purpose
- **🛠️ Technology Stack**: Languages and frameworks used
- **🏗️ Architecture Insights**: Design patterns and structure
- **📦 Setup Instructions**: How to get started
- **📁 Key Files**: Important files with code snippets

### Step 4: Browse the File Tree

- View the complete repository structure in the sidebar
- Files are tagged with their programming language
- Organized hierarchically with folders and files

### Step 5: Ask Questions

Use the chat interface to:
- Ask about specific features: *"How does authentication work?"*
- Request explanations: *"Explain the database schema"*
- Get code references: *"Where is the API defined?"*
- Understand architecture: *"What design patterns are used?"*

---

## 🎬 Demo Script (for Hackathon Presentation)

### 5-Minute Demo Flow

**1. Introduction (30 seconds)**
- "DevOnboard AI helps developers quickly understand new codebases"
- "Powered by IBM watsonx.ai Granite models"

**2. Repository Analysis (2 minutes)**
- Enter a popular repo URL (e.g., FastAPI, React, Flask)
- Show real-time analysis progress
- Highlight the AI-generated onboarding guide
- Demonstrate collapsible sections

**3. File Tree Navigation (1 minute)**
- Browse the repository structure
- Show language detection
- Explain the organization

**4. Interactive Chat (1.5 minutes)**
- Ask 2-3 questions about the codebase
- Show how AI provides context-aware answers
- Highlight code references in responses

**5. Closing (30 seconds)**
- Emphasize IBM watsonx.ai integration
- Mention caching for efficiency
- Show IBM Carbon Design System styling

### Suggested Demo Repositories

**Small & Fast** (< 1 minute analysis):
- `https://github.com/pallets/flask`
- `https://github.com/psf/requests`

**Medium** (1-2 minutes):
- `https://github.com/tiangolo/fastapi`
- `https://github.com/django/django`

**Large** (2-3 minutes):
- `https://github.com/facebook/react`
- `https://github.com/microsoft/vscode`

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   Streamlit Frontend                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Sidebar    │  │  Main View   │  │  Chat Panel  │  │
│  │ - URL Input  │  │ - Guide      │  │ - Messages   │  │
│  │ - File Tree  │  │ - Sections   │  │ - Input      │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                           │
                           │ HTTP/REST API
                           ▼
┌─────────────────────────────────────────────────────────┐
│                    FastAPI Backend                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Analyzer   │  │  Repo Mgr    │  │  watsonx.ai  │  │
│  │              │  │              │  │   Client     │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                           │
                           │ API Calls
                           ▼
┌─────────────────────────────────────────────────────────┐
│              IBM watsonx.ai Granite Models               │
│                  (Code Analysis & Chat)                  │
└─────────────────────────────────────────────────────────┘
```

---

## 🎨 UI/UX Design

### IBM Carbon Design System

The app uses IBM's Carbon Design System colors:

- **Background**: `#161616` (Gray 100)
- **Surface**: `#262626` (Gray 90)
- **Primary**: `#0f62fe` (Blue 60)
- **Text**: `#f4f4f4` (Gray 10)
- **Accent**: `#8a3ffc` (Purple 60)

### Key Design Elements

- **Dark Theme**: Professional, easy on the eyes
- **Clear Typography**: IBM Plex Sans font family
- **Consistent Spacing**: Carbon grid system
- **Interactive Elements**: Hover states and transitions
- **Progress Indicators**: Animated loading states
- **Code Highlighting**: Syntax-aware display

---

## 🔧 Troubleshooting

### Backend Not Running

**Error**: `❌ Error analyzing repository: Connection refused`

**Solution**:
```bash
# Check if backend is running
curl http://localhost:8000/health

# If not, start the backend
cd backend
python api.py
```

### Invalid GitHub URL

**Error**: `❌ Invalid GitHub URL format`

**Solution**: Ensure URL format is:
- ✅ `https://github.com/owner/repo`
- ❌ `github.com/owner/repo` (missing https://)
- ❌ `https://github.com/owner/repo.git` (remove .git)

### Analysis Timeout

**Error**: Analysis takes too long or times out

**Solution**:
- Try a smaller repository first
- Check your internet connection
- Verify watsonx.ai credentials are correct
- Increase `API_TIMEOUT` in `streamlit_app.py`

### Import Errors

**Error**: `ModuleNotFoundError: No module named 'streamlit'`

**Solution**:
```bash
# Ensure virtual environment is activated
# Install dependencies
pip install -r requirements-streamlit.txt
```

---

## 📊 Performance Tips

1. **Use Caching**: Analysis results are cached for 7 days
2. **Start Small**: Test with smaller repositories first
3. **Check Backend Logs**: Monitor `backend/api.py` output
4. **Network Speed**: Faster internet = faster cloning
5. **Force Refresh**: Use checkbox to bypass cache if needed

---

## 🚀 Deployment Options

### Local Development
- Backend: `python backend/api.py`
- Frontend: `streamlit run streamlit_app.py`

### IBM Cloud Code Engine
1. Deploy FastAPI backend as a service
2. Deploy Streamlit app as a separate service
3. Configure environment variables
4. Set up watsonx.ai credentials

### Docker (Future Enhancement)
```bash
# Build and run with Docker Compose
docker-compose up
```

---

## 📝 API Endpoints Used

The Streamlit app interacts with these backend endpoints:

- `POST /api/analyze` - Analyze repository
- `POST /api/chat` - Send chat message
- `GET /api/files/{session_id}` - Get file tree
- `GET /api/files/{session_id}/content` - Get file content
- `GET /health` - Health check

---

## 🤝 Contributing

This is a hackathon demo project. For improvements:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

[Specify your license here]

---

## 🙏 Acknowledgments

- **IBM watsonx.ai** for providing the Granite models
- **Streamlit** for the amazing framework
- **IBM Carbon Design System** for design inspiration
- **FastAPI** for the robust backend framework

---

## 📞 Support

For issues or questions:
- Create a GitHub issue
- Contact: [Your contact information]
- IBM watsonx.ai docs: https://www.ibm.com/docs/en/watsonx-as-a-service

---

**Built with ❤️ for IBM Hackathon 2026**

*Powered by IBM watsonx.ai Granite Models*