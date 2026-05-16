# DevPilot 🚀

**AI-Powered Developer Onboarding Assistant**

[![IBM watsonx.ai](https://img.shields.io/badge/Powered%20by-IBM%20watsonx.ai-0f62fe?style=for-the-badge)](https://www.ibm.com/watsonx)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?style=for-the-badge)](https://streamlit.io)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge)](https://fastapi.tiangolo.com)

> Built for **IBM Hackathon 2026** - Showcasing IBM watsonx.ai Granite Models

---

## 🎯 Overview

**DevPilot** streamlines developer onboarding by automatically analyzing GitHub repositories and generating comprehensive onboarding guides using **IBM watsonx.ai Granite models**. Get new developers up to speed in minutes, not days!

### Key Features

- 🧠 **AI-Powered Analysis** - Uses IBM watsonx.ai Granite for intelligent code understanding
- 📖 **Auto-Generated Guides** - Comprehensive onboarding documentation in minutes
- 💬 **Interactive Chat** - Ask questions about the codebase and get context-aware answers
- 🗂️ **File Tree Browser** - Explore repository structure with language detection
- 🎨 **Professional UI** - IBM Carbon Design System inspired dark theme
- ⚡ **Fast & Efficient** - Intelligent caching for repeated analyses

---

## 🚀 Quick Start

### Option 1: One-Click Demo (Recommended)

**Windows:**
```bash
run_demo.bat
```

**macOS/Linux:**
```bash
chmod +x run_demo.sh
./run_demo.sh
```

### Option 2: Manual Setup

#### 1. Backend Setup

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your IBM watsonx.ai credentials
python api.py
```

#### 2. Streamlit App Setup

```bash
pip install -r requirements-streamlit.txt
cp .env.example .env
streamlit run streamlit_app.py
```

### 3. Access the App

- **Streamlit UI**: http://localhost:8501
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

---

## 📚 Documentation

- **[Streamlit Demo Guide](STREAMLIT_README.md)** - Complete setup and usage instructions
- **[Demo Script](DEMO_GUIDE.md)** - Hackathon presentation guide
- **[Architecture Guide](AGENTS.md)** - Technical architecture and development plan
- **[Backend README](backend/README.md)** - Backend API documentation

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│              Streamlit Frontend (Port 8501)              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Sidebar    │  │  Main View   │  │  Chat Panel  │  │
│  │ - URL Input  │  │ - Guide      │  │ - Messages   │  │
│  │ - File Tree  │  │ - Sections   │  │ - Input      │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                           │
                           │ REST API
                           ▼
┌─────────────────────────────────────────────────────────┐
│              FastAPI Backend (Port 8000)                 │
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

## 🛠️ Technology Stack

### Frontend
- **Streamlit** - Interactive web application framework
- **Python 3.9+** - Core programming language
- **IBM Carbon Design** - UI/UX design system

### Backend
- **FastAPI** - High-performance async API framework
- **GitPython** - Repository cloning and management
- **Pygments** - Syntax highlighting and language detection

### AI/ML
- **IBM watsonx.ai** - AI platform
- **Granite Models** - Code analysis and chat (ibm/granite-13b-chat-v2)

### Future Enhancements
- **IBM Cloudant** - Persistent caching (currently in-memory)
- **IBM Cloud Code Engine** - Production deployment

---

## 📁 Project Structure

```
ibm-hackathon/
├── streamlit_app.py              # Main Streamlit application
├── requirements-streamlit.txt    # Streamlit dependencies
├── .streamlit/
│   └── config.toml              # Streamlit configuration
├── .env.example                 # Environment template
├── run_demo.bat                 # Windows quick start
├── run_demo.sh                  # Unix quick start
├── STREAMLIT_README.md          # Streamlit documentation
├── DEMO_GUIDE.md               # Hackathon demo guide
├── AGENTS.md                   # Architecture documentation
└── backend/                     # FastAPI backend
    ├── api.py                  # Main API application
    ├── analyzer.py             # Code analysis logic
    ├── watsonx_client.py       # IBM watsonx.ai integration
    ├── repo_manager.py         # Git operations
    ├── models.py               # Pydantic models
    ├── config.py               # Configuration
    ├── utils.py                # Utility functions
    └── requirements.txt        # Backend dependencies
```

---

## 🎬 Demo Workflow

### 1. Enter Repository URL
Enter any public GitHub repository URL in the sidebar:
```
https://github.com/tiangolo/fastapi
```

### 2. Watch Analysis Progress
Real-time progress indicators show:
- ⏳ Cloning repository from GitHub
- 🔍 Analyzing code structure
- 🧠 Generating AI insights with IBM watsonx.ai Granite
- ✅ Analysis complete!

### 3. Explore Onboarding Guide
AI-generated guide includes:
- **Project Overview** - Purpose and description
- **Technology Stack** - Languages and frameworks
- **Architecture Insights** - Design patterns and structure
- **Setup Instructions** - How to get started
- **Key Files** - Important files with snippets

### 4. Browse File Tree
- View complete repository structure
- Files tagged with programming language
- Hierarchical organization

### 5. Ask Questions
Interactive chat interface for:
- Feature explanations
- Code references
- Architecture questions
- Setup guidance

---

## ⚙️ Configuration

### Required Environment Variables

**Backend (`backend/.env`):**
```bash
# IBM watsonx.ai Configuration
WATSONX_API_KEY=your_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-13b-chat-v2

# Application Settings
REPO_CLONE_DIR=/tmp/repos
CACHE_TTL_DAYS=7
API_PORT=8000
```

**Streamlit (`.env`):**
```bash
BACKEND_URL=http://localhost:8000
```

---

## 🎨 UI/UX Features

### IBM Carbon Design System
- **Dark Theme** - Professional developer-focused design
- **Color Palette**:
  - Background: `#161616` (Gray 100)
  - Surface: `#262626` (Gray 90)
  - Primary: `#0f62fe` (Blue 60)
  - Text: `#f4f4f4` (Gray 10)

### Interactive Elements
- Collapsible sections for better organization
- Syntax-highlighted code snippets
- Animated progress indicators
- Responsive layout
- Smooth transitions

---

## 🧪 Example Repositories to Try

**Fast Analysis (< 1 minute):**
- Flask: `https://github.com/pallets/flask`
- Requests: `https://github.com/psf/requests`

**Medium (1-2 minutes):**
- FastAPI: `https://github.com/tiangolo/fastapi` ⭐ **Recommended**
- Django: `https://github.com/django/django`

**Large (2-3 minutes):**
- React: `https://github.com/facebook/react`
- VS Code: `https://github.com/microsoft/vscode`

---

## 🔧 Troubleshooting

### Backend Connection Error
```bash
# Check if backend is running
curl http://localhost:8000/health

# Restart backend
cd backend && python api.py
```

### Import Errors
```bash
# Install dependencies
pip install -r requirements-streamlit.txt
pip install -r backend/requirements.txt
```

### Invalid GitHub URL
Ensure URL format is:
- ✅ `https://github.com/owner/repo`
- ❌ `github.com/owner/repo` (missing https://)
- ❌ `https://github.com/owner/repo.git` (remove .git)

---

## 🚀 Deployment

### Local Development
1. Start backend: `python backend/api.py`
2. Start Streamlit: `streamlit run streamlit_app.py`

### IBM Cloud (Future)
- Deploy FastAPI to IBM Cloud Code Engine
- Deploy Streamlit to IBM Cloud Code Engine
- Configure IBM Cloudant for persistent caching
- Set up watsonx.ai service binding

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

### Phase 1 (Post-Hackathon)
- [ ] IBM Cloudant integration for persistent caching
- [ ] Multi-repository comparison
- [ ] Advanced code metrics
- [ ] Security vulnerability scanning

### Phase 2
- [ ] Team collaboration features
- [ ] Shared annotations and notes
- [ ] Knowledge base building
- [ ] Custom analysis templates

### Phase 3
- [ ] IDE extensions (VSCode, IntelliJ)
- [ ] CLI tool
- [ ] API for third-party integrations
- [ ] Enterprise features

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

- **IBM watsonx.ai** for providing the Granite models
- **IBM Carbon Design System** for design inspiration
- **Streamlit** for the amazing framework
- **FastAPI** for the robust backend
- **Open Source Community** for inspiration

---

## 📞 Contact

For questions or feedback:
- Create a GitHub issue
- Contact: [Your contact information]
- IBM watsonx.ai docs: https://www.ibm.com/docs/en/watsonx-as-a-service

---

## 🎉 Demo Video

[Link to demo video if available]

---

**Built with ❤️ for IBM Hackathon 2026**

*Powered by IBM watsonx.ai Granite Models*

---

## 📊 Quick Stats

- **Lines of Code**: ~1,500+
- **Files Created**: 15+
- **Technologies**: 10+
- **Development Time**: Hackathon sprint
- **AI Model**: IBM Granite 13B Chat v2
- **UI Framework**: Streamlit + IBM Carbon Design
- **Backend**: FastAPI + Python 3.9+

---

**Ready to revolutionize developer onboarding? Get started now! 🚀**