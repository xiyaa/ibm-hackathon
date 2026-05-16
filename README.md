# DevPilot 🚀

**AI-Powered Developer Onboarding Assistant**

[![IBM watsonx.ai](https://img.shields.io/badge/Powered%20by-IBM%20watsonx.ai-0f62fe?style=for-the-badge)](https://www.ibm.com/watsonx)
[![React](https://img.shields.io/badge/Built%20with-React-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge)](https://fastapi.tiangolo.com)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=for-the-badge)](https://render.com)

> Built for **IBM Hackathon 2026** - Showcasing IBM watsonx.ai Granite Models

---

## 🎯 Overview

**DevPilot** streamlines developer onboarding by automatically analyzing GitHub repositories and generating comprehensive onboarding guides using **IBM watsonx.ai Granite models**. Get new developers up to speed in minutes, not days!

### Key Features

- 🧠 **AI-Powered Analysis** - Uses IBM watsonx.ai Granite for intelligent code understanding
- 📖 **Auto-Generated Guides** - Comprehensive onboarding documentation in minutes
- 💬 **Interactive Chat** - Ask questions about the codebase with context-aware AI responses
- 📊 **Visual Diagrams** - Mermaid diagrams for architecture visualization
- 🎨 **Modern UI** - Material-UI (MUI) components with responsive design
- ⚡ **Fast & Efficient** - Intelligent caching and optimized performance
- 🚀 **Production Ready** - Deployed on Render with CI/CD

---

## 🚀 Quick Start

### 🌐 Try the Live Demo

**No installation required!** Visit the deployed application:

👉 **[https://ibm-hackathon-frontend.onrender.com](https://ibm-hackathon-frontend.onrender.com)**

Simply enter a GitHub repository URL and start exploring!

---

### 💻 Local Development Setup

#### Prerequisites
- Python 3.9+
- Node.js 18+
- Git
- IBM watsonx.ai API credentials

### Local Development Setup

#### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ibm-hackathon.git
cd ibm-hackathon
```

#### 2. Backend Setup
```bash
cd backend
pip install -r requirements.txt

# Create .env file with your credentials
cat > .env << EOF
WATSONX_API_KEY=your_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-3-8b-instruct
REPO_CLONE_DIR=/tmp/repos
CACHE_TTL_DAYS=7
EOF

# Start the backend
python api.py
# Or with uvicorn: uvicorn api:app --reload --host 127.0.0.1 --port 8000
```

#### 3. Frontend Setup
```bash
cd frontend
npm install

# Create .env file
cat > .env << EOF
VITE_API_URL=http://localhost:8000
VITE_APP_NAME=DevPilot
EOF

# Start the development server
npm run dev
```

#### 4. Access the Application

**Local Development:**
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

**Production (Render):**
- **Frontend**: https://ibm-hackathon-frontend.onrender.com
- **Backend API**: https://ibm-hackathon-backend.onrender.com
- **API Docs**: https://ibm-hackathon-backend.onrender.com/docs

---

## 📚 Documentation

- **[Frontend README](frontend/README.md)** - React frontend documentation
- **[Backend README](backend/README.md)** - Backend API documentation
- **[Architecture Guide](bob_sessions/bob_plans/AGENTS.md)** - Technical architecture and development plan
- **[Render Deployment](bob_sessions/bob_plans/RENDER_DEPLOYMENT.md)** - Production deployment guide

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│           React Frontend (Port 5173/Render)              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ Repository   │  │  Onboarding  │  │     Chat     │  │
│  │    Input     │  │    Guide     │  │  Interface   │  │
│  │              │  │  - Overview  │  │  - Messages  │  │
│  │ - URL        │  │  - Tech      │  │  - Code Ref  │  │
│  │ - Branch     │  │  - Setup     │  │  - History   │  │
│  │ - Analyze    │  │  - Files     │  │              │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                           │
                           │ Axios HTTP Client
                           │ REST API Calls
                           ▼
┌─────────────────────────────────────────────────────────┐
│           FastAPI Backend (Port 8000/Render)             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Analyzer   │  │  Repo Mgr    │  │  watsonx.ai  │  │
│  │  - Code      │  │  - Clone     │  │   Client     │  │
│  │  - Metrics   │  │  - Files     │  │  - Granite   │  │
│  │  - Structure │  │  - Tree      │  │  - Chat      │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                           │
                           │ IBM watsonx.ai SDK
                           ▼
┌─────────────────────────────────────────────────────────┐
│              IBM watsonx.ai Granite Models               │
│         ibm/granite-3-8b-instruct (Code & Chat)            │
└─────────────────────────────────────────────────────────┘
```

---

## 🛠️ Technology Stack

### Frontend
- **React 18** - Modern UI library
- **Vite** - Fast build tool and dev server
- **Material-UI (MUI)** - Component library
- **Axios** - HTTP client
- **react-markdown** - Markdown rendering
- **react-syntax-highlighter** - Code highlighting
- **Mermaid** - Diagram generation

### Backend
- **FastAPI** - High-performance async API framework
- **Python 3.9+** - Core programming language
- **GitPython** - Repository cloning and management
- **Pygments** - Syntax highlighting and language detection
- **Radon** - Code complexity metrics

### AI/ML
- **IBM watsonx.ai** - AI platform
- **Granite 13B Chat v2** - Code analysis and conversational AI

### Deployment
- **Render** - Cloud hosting platform
- **GitHub Actions** - CI/CD (future)

---

## 📁 Project Structure

```
ibm-hackathon/
├── README.md                    # This file
├── render.yaml                  # Render deployment config
├── .gitignore                   # Git ignore rules
│
├── frontend/                    # React frontend
│   ├── src/
│   │   ├── components/         # React components
│   │   │   ├── RepositoryInput.jsx
│   │   │   ├── OnboardingGuide.jsx
│   │   │   ├── ChatInterface.jsx
│   │   │   ├── CodeReference.jsx
│   │   │   ├── LoadingSpinner.jsx
│   │   │   └── MermaidDiagram.jsx
│   │   ├── context/
│   │   │   └── AppContext.jsx  # Global state
│   │   ├── services/
│   │   │   └── api.js          # API client
│   │   ├── App.jsx             # Main component
│   │   ├── main.jsx            # Entry point
│   │   └── index.css           # Global styles
│   ├── index.html              # HTML template
│   ├── vite.config.js          # Vite config
│   ├── package.json            # Dependencies
│   └── README.md               # Frontend docs
│
├── backend/                     # FastAPI backend
│   ├── api.py                  # Main API application
│   ├── analyzer.py             # Code analysis logic
│   ├── watsonx_client.py       # IBM watsonx.ai integration
│   ├── repo_manager.py         # Git operations
│   ├── models.py               # Pydantic models
│   ├── config.py               # Configuration
│   ├── utils.py                # Utility functions
│   ├── requirements.txt        # Backend dependencies
│   ├── runtime.txt             # Python version
│   └── README.md               # Backend docs
│
└── bob_sessions/                # Development documentation
    └── bob_plans/
        ├── AGENTS.md           # Architecture guide
        └── RENDER_DEPLOYMENT.md # Deployment guide
```

---

## 🎬 Demo Workflow

### 1. Enter Repository URL
Enter any public GitHub repository URL:
```
https://github.com/tiangolo/fastapi
```
- Optionally specify a branch (default: main)
- Check "Force Refresh" to bypass cache

### 2. Watch Analysis Progress
Real-time progress indicators show:
- ⏳ Cloning repository from GitHub
- 🔍 Analyzing code structure and metrics
- 🧠 Generating AI insights with IBM watsonx.ai Granite
- ✅ Analysis complete!

### 3. Explore Onboarding Guide
AI-generated comprehensive guide includes:
- **📋 Project Overview** - Purpose, description, and goals
- **🛠️ Technology Stack** - Languages, frameworks, and tools
- **🏗️ Architecture** - Design patterns, structure, and diagrams
- **⚙️ Setup Instructions** - Step-by-step getting started guide
- **📁 Key Files** - Important files with code snippets
- **📦 Dependencies** - Required packages and versions
- **🔧 Configuration** - Environment setup and configs

### 4. Interactive Chat
Ask questions about the codebase:
- "How does authentication work?"
- "What's the main entry point?"
- "Explain the database schema"
- Get code references in responses
- Context-aware AI powered by Granite

---

## ⚙️ Configuration

### Environment Variables

**Backend (`backend/.env`):**
```bash
# IBM watsonx.ai Configuration (Required)
WATSONX_API_KEY=your_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-3-8b-instruct

# Application Settings
REPO_CLONE_DIR=/tmp/repos
MAX_REPO_SIZE_MB=500
CACHE_TTL_DAYS=7
API_HOST=0.0.0.0
API_PORT=8000
LOG_LEVEL=INFO

# CORS (for production)
CORS_ORIGINS=https://your-frontend.onrender.com,http://localhost:5173
```

**Frontend (`frontend/.env`):**
```bash
VITE_API_URL=http://localhost:8000
VITE_APP_NAME=DevPilot
```

### Getting IBM watsonx.ai Credentials

1. Sign up for [IBM Cloud](https://cloud.ibm.com/)
2. Create a watsonx.ai project
3. Generate an API key from IBM Cloud IAM
4. Copy your project ID from watsonx.ai

---

## 🎨 UI/UX Features

### Material-UI Design
- **Modern Interface** - Clean, professional design
- **Responsive Layout** - Works on desktop and mobile
- **Dark Mode Ready** - Easy theme customization
- **Accessibility** - WCAG compliant components

### Interactive Elements
- Expandable sections with smooth animations
- Syntax-highlighted code snippets (Prism.js)
- Real-time loading indicators
- Toast notifications for feedback
- Markdown rendering with GFM support
- Mermaid diagram visualization
- Code reference cards with file paths

---

## 🧪 Example Repositories to Try

**Small Projects (< 1 minute):**
- `https://github.com/pallets/flask`
- `https://github.com/psf/requests`
- `https://github.com/kennethreitz/requests`

**Medium Projects (1-2 minutes):**
- `https://github.com/tiangolo/fastapi` ⭐ **Recommended**
- `https://github.com/django/django`
- `https://github.com/streamlit/streamlit`

**Large Projects (2-5 minutes):**
- `https://github.com/facebook/react`
- `https://github.com/microsoft/vscode`
- `https://github.com/nodejs/node`

---

## 🔧 Troubleshooting

### Backend Not Starting
```bash
# Check Python version
python --version  # Should be 3.9+

# Reinstall dependencies
cd backend
pip install --upgrade pip
pip install -r requirements.txt

# Check for port conflicts
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows
```

### Frontend Build Errors
```bash
# Clear cache and reinstall
cd frontend
rm -rf node_modules package-lock.json dist
npm install
npm run build
```

### CORS Errors
Ensure backend `.env` has correct CORS_ORIGINS:
```bash
CORS_ORIGINS=http://localhost:5173,https://your-frontend.onrender.com
```

### watsonx.ai API Errors
- Verify API key is valid and not expired
- Check project ID is correct
- Ensure you have access to Granite models
- Check IBM Cloud service status

### Repository Clone Failures
- Ensure repository is public
- Check GitHub URL format: `https://github.com/owner/repo`
- Verify network connectivity
- Check disk space in REPO_CLONE_DIR

---

## 🚀 Deployment

### Render (Current)

The application is configured for deployment on Render using `render.yaml`:

**Backend:**
- Python web service
- Auto-deploys from main branch
- Environment variables set in Render dashboard

**Frontend:**
- Static site
- Built with Vite
- Served from `dist/` directory

See [RENDER_DEPLOYMENT.md](bob_sessions/bob_plans/RENDER_DEPLOYMENT.md) for detailed instructions.

### Manual Deployment

**Backend (any Python host):**
```bash
cd backend
pip install -r requirements.txt
uvicorn api:app --host 0.0.0.0 --port $PORT
```

**Frontend (any static host):**
```bash
cd frontend
npm install
npm run build
# Serve the dist/ directory
```

### Docker (Future)
```dockerfile
# Coming soon: Docker Compose setup
# - Backend container
# - Frontend container
# - Nginx reverse proxy
```

---

## 🎯 Use Cases

### For Developers
- Quickly understand new codebases
- Get up to speed on team projects
- Learn from open-source repositories
- Explore unfamiliar technologies

### For Teams
- Streamline onboarding process
- Reduce time-to-productivity
- Create consistent documentation
- Share knowledge effectively

### For Educators
- Teach software architecture
- Analyze example projects
- Demonstrate best practices
- Compare different approaches

---

## 🏆 Hackathon Highlights

### Innovation
- ✅ Novel application of IBM watsonx.ai Granite models
- ✅ Solves real developer pain point
- ✅ Production-ready architecture
- ✅ Scalable and extensible

### Technical Excellence
- ✅ Clean, maintainable code
- ✅ Comprehensive error handling
- ✅ Professional UI/UX
- ✅ Complete documentation

### IBM Integration
- ✅ IBM watsonx.ai Granite models
- ✅ IBM Carbon Design System
- ✅ Ready for IBM Cloud deployment
- ✅ Showcases platform capabilities

---

## 📈 Future Enhancements

### Phase 1 (Immediate)
- [x] React frontend with Material-UI
- [x] FastAPI backend with watsonx.ai
- [x] Repository analysis and chat
- [x] Render deployment
- [ ] User authentication
- [ ] Analysis history/bookmarks
- [ ] Export guides to PDF/Markdown

### Phase 2 (Short-term)
- [ ] Multi-repository comparison
- [ ] Advanced code metrics dashboard
- [ ] Security vulnerability scanning
- [ ] Team collaboration features
- [ ] Custom analysis templates
- [ ] GitHub App integration

### Phase 3 (Long-term)
- [ ] IDE extensions (VSCode, IntelliJ)
- [ ] CLI tool for CI/CD integration
- [ ] Private repository support
- [ ] Enterprise SSO
- [ ] API rate limiting and quotas
- [ ] Analytics and usage tracking

---

## 🤝 Contributing

This project was built for the IBM Hackathon 2026. For improvements:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

[Specify your license here - e.g., MIT, Apache 2.0]

---

## 🙏 Acknowledgments

- **IBM watsonx.ai** for providing the powerful Granite models
- **Material-UI** for the excellent React component library
- **FastAPI** for the high-performance backend framework
- **Vite** for the blazing-fast build tool
- **Render** for the seamless deployment platform
- **Open Source Community** for inspiration and tools

---

## 📞 Contact & Resources

**Project Links:**
- GitHub Repository: [Your repo URL]
- Live Demo: [Your Render URL]
- API Documentation: [Your backend URL]/docs

**IBM Resources:**
- [IBM watsonx.ai Documentation](https://www.ibm.com/docs/en/watsonx-as-a-service)
- [Granite Models](https://www.ibm.com/products/watsonx-ai/foundation-models)
- [IBM Cloud](https://cloud.ibm.com/)

**Support:**
- Create a GitHub issue for bugs
- Check documentation for common questions
- Contact: [Your contact information]

---

**Built with ❤️ for IBM Hackathon 2026**

*Powered by IBM watsonx.ai Granite Models*

---

## 📊 Quick Stats

- **Lines of Code**: ~2,500+
- **Components**: 20+
- **Technologies**: 15+
- **Development Time**: Hackathon sprint
- **AI Model**: ibm/granite-3-8b-instruct
- **Frontend**: React 18 + Vite + Material-UI
- **Backend**: FastAPI + Python 3.9+
- **Deployment**: Render (Production-ready)

---

**Ready to revolutionize developer onboarding? Get started now! 🚀**