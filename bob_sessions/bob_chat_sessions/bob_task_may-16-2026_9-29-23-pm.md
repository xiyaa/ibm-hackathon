**User:**

<task>
con el proyecto que tenemos, give me:
Short Description: A concise summary (up to 255 characters) capturing the essence of your project.
Long Description: Detailed write-up (at least 100 words) highlighting the problem, your solution, target audience, and any unique features/benefits.
Technology & Category Tags: Select tags that best categorize your project, aiding judges and participants in understanding its primary focus.
</task>
<environment_details>
# VSCode Visible Files
requirements.txt

# VSCode Open Tabs
streamlit_app.py,.gitignore,.streamlit/config.toml,STREAMLIT_README.md,backend/models.py,backend/analyzer.py,frontend/src/components/MermaidDiagram.jsx,frontend/src/components/OnboardingGuide.jsx,backend/watsonx_client.py,frontend/index.html,frontend/src/App.jsx,backend/api.py,README.md,frontend/package.json,requirements.txt,run_demo.bat,run_demo.sh,DEMO_GUIDE.md

# Current Time
Current time in ISO 8601 UTC format: 2026-05-16T19:29:01.448Z
User time zone: Europe/Madrid, UTC+2:00

# Current Cost
$0.00

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>


# Current Workspace Directory (d:/Docs/master_eit/EIT_exit_KTH/ibm-hackathon) Files
.gitignore
AGENTS.md
BUGFIX_REPORT.md
DEPLOYMENT.md
README.md
RENDER_DEPLOYMENT.md
render.yaml
.vscode/
backend/
backend/__init__.py
backend/.bobignore
backend/analyzer.py
backend/api.py
backend/config.py
backend/desktop.ini
backend/models.py
backend/README.md
backend/repo_manager.py
backend/requirements.txt
backend/runtime.txt
backend/utils.py
backend/watsonx_client.py
frontend/
frontend/.gitignore
frontend/index.html
frontend/package-lock.json
frontend/package.json
frontend/README.md
frontend/vite.config.js
frontend/src/
frontend/src/App.jsx
frontend/src/index.css
frontend/src/main.jsx
frontend/src/components/
frontend/src/components/ChatInterface.jsx
frontend/src/components/CodeReference.jsx
frontend/src/components/LoadingSpinner.jsx
frontend/src/components/MermaidDiagram.jsx
frontend/src/components/OnboardingGuide.jsx
frontend/src/components/RepositoryInput.jsx
frontend/src/context/
frontend/src/context/AppContext.jsx
frontend/src/services/
frontend/src/services/api.js
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

I'll analyze the project to provide you with the requested descriptions and tags.

<read_file>
<args>
<file>
<path>README.md</path>
</file>
<file>
<path>AGENTS.md</path>
</file>
<file>
<path>backend/api.py</path>
</file>
<file>
<path>frontend/src/App.jsx</path>
</file>
</args>
</read_file>

---

**User:**

[read_file for 4 files] Result:
<files>
<file><path>README.md</path>
<content lines="1-424">
  1 | # DevPilot 🚀
  2 | 
  3 | **AI-Powered Developer Onboarding Assistant**
  4 | 
  5 | [![IBM watsonx.ai](https://img.shields.io/badge/Powered%20by-IBM%20watsonx.ai-0f62fe?style=for-the-badge)](https://www.ibm.com/watsonx)
  6 | [![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?style=for-the-badge)](https://streamlit.io)
  7 | [![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge)](https://fastapi.tiangolo.com)
  8 | 
  9 | > Built for **IBM Hackathon 2026** - Showcasing IBM watsonx.ai Granite Models
 10 | 
 11 | ---
 12 | 
 13 | ## 🎯 Overview
 14 | 
 15 | **DevPilot** streamlines developer onboarding by automatically analyzing GitHub repositories and generating comprehensive onboarding guides using **IBM watsonx.ai Granite models**. Get new developers up to speed in minutes, not days!
 16 | 
 17 | ### Key Features
 18 | 
 19 | - 🧠 **AI-Powered Analysis** - Uses IBM watsonx.ai Granite for intelligent code understanding
 20 | - 📖 **Auto-Generated Guides** - Comprehensive onboarding documentation in minutes
 21 | - 💬 **Interactive Chat** - Ask questions about the codebase and get context-aware answers
 22 | - 🗂️ **File Tree Browser** - Explore repository structure with language detection
 23 | - 🎨 **Professional UI** - IBM Carbon Design System inspired dark theme
 24 | - ⚡ **Fast & Efficient** - Intelligent caching for repeated analyses
 25 | 
 26 | ---
 27 | 
 28 | ## 🚀 Quick Start
 29 | 
 30 | ### Option 1: One-Click Demo (Recommended)
 31 | 
 32 | **Windows:**
 33 | ```bash
 34 | run_demo.bat
 35 | ```
 36 | 
 37 | **macOS/Linux:**
 38 | ```bash
 39 | chmod +x run_demo.sh
 40 | ./run_demo.sh
 41 | ```
 42 | 
 43 | ### Option 2: Manual Setup
 44 | 
 45 | #### 1. Backend Setup
 46 | 
 47 | ```bash
 48 | cd backend
 49 | pip install -r requirements.txt
 50 | cp .env.example .env
 51 | # Edit .env with your IBM watsonx.ai credentials
 52 | python api.py
 53 | ```
 54 | 
 55 | #### 2. Streamlit App Setup
 56 | 
 57 | ```bash
 58 | pip install -r requirements-streamlit.txt
 59 | cp .env.example .env
 60 | streamlit run streamlit_app.py
 61 | ```
 62 | 
 63 | ### 3. Access the App
 64 | 
 65 | - **Streamlit UI**: http://localhost:8501
 66 | - **Backend API**: http://localhost:8000
 67 | - **API Docs**: http://localhost:8000/docs
 68 | 
 69 | ---
 70 | 
 71 | ## 📚 Documentation
 72 | 
 73 | - **[Streamlit Demo Guide](STREAMLIT_README.md)** - Complete setup and usage instructions
 74 | - **[Demo Script](DEMO_GUIDE.md)** - Hackathon presentation guide
 75 | - **[Architecture Guide](AGENTS.md)** - Technical architecture and development plan
 76 | - **[Backend README](backend/README.md)** - Backend API documentation
 77 | 
 78 | ---
 79 | 
 80 | ## 🏗️ Architecture
 81 | 
 82 | ```
 83 | ┌─────────────────────────────────────────────────────────┐
 84 | │              Streamlit Frontend (Port 8501)              │
 85 | │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
 86 | │  │   Sidebar    │  │  Main View   │  │  Chat Panel  │  │
 87 | │  │ - URL Input  │  │ - Guide      │  │ - Messages   │  │
 88 | │  │ - File Tree  │  │ - Sections   │  │ - Input      │  │
 89 | │  └──────────────┘  └──────────────┘  └──────────────┘  │
 90 | └─────────────────────────────────────────────────────────┘
 91 |                            │
 92 |                            │ REST API
 93 |                            ▼
 94 | ┌─────────────────────────────────────────────────────────┐
 95 | │              FastAPI Backend (Port 8000)                 │
 96 | │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
 97 | │  │   Analyzer   │  │  Repo Mgr    │  │  watsonx.ai  │  │
 98 | │  │              │  │              │  │   Client     │  │
 99 | │  └──────────────┘  └──────────────┘  └──────────────┘  │
100 | └─────────────────────────────────────────────────────────┘
101 |                            │
102 |                            │ API Calls
103 |                            ▼
104 | ┌─────────────────────────────────────────────────────────┐
105 | │              IBM watsonx.ai Granite Models               │
106 | │                  (Code Analysis & Chat)                  │
107 | └─────────────────────────────────────────────────────────┘
108 | ```
109 | 
110 | ---
111 | 
112 | ## 🛠️ Technology Stack
113 | 
114 | ### Frontend
115 | - **Streamlit** - Interactive web application framework
116 | - **Python 3.9+** - Core programming language
117 | - **IBM Carbon Design** - UI/UX design system
118 | 
119 | ### Backend
120 | - **FastAPI** - High-performance async API framework
121 | - **GitPython** - Repository cloning and management
122 | - **Pygments** - Syntax highlighting and language detection
123 | 
124 | ### AI/ML
125 | - **IBM watsonx.ai** - AI platform
126 | - **Granite Models** - Code analysis and chat (ibm/granite-13b-chat-v2)
127 | 
128 | ### Future Enhancements
129 | - **IBM Cloudant** - Persistent caching (currently in-memory)
130 | - **IBM Cloud Code Engine** - Production deployment
131 | 
132 | ---
133 | 
134 | ## 📁 Project Structure
135 | 
136 | ```
137 | ibm-hackathon/
138 | ├── streamlit_app.py              # Main Streamlit application
139 | ├── requirements-streamlit.txt    # Streamlit dependencies
140 | ├── .streamlit/
141 | │   └── config.toml              # Streamlit configuration
142 | ├── .env.example                 # Environment template
143 | ├── run_demo.bat                 # Windows quick start
144 | ├── run_demo.sh                  # Unix quick start
145 | ├── STREAMLIT_README.md          # Streamlit documentation
146 | ├── DEMO_GUIDE.md               # Hackathon demo guide
147 | ├── AGENTS.md                   # Architecture documentation
148 | └── backend/                     # FastAPI backend
149 |     ├── api.py                  # Main API application
150 |     ├── analyzer.py             # Code analysis logic
151 |     ├── watsonx_client.py       # IBM watsonx.ai integration
152 |     ├── repo_manager.py         # Git operations
153 |     ├── models.py               # Pydantic models
154 |     ├── config.py               # Configuration
155 |     ├── utils.py                # Utility functions
156 |     └── requirements.txt        # Backend dependencies
157 | ```
158 | 
159 | ---
160 | 
161 | ## 🎬 Demo Workflow
162 | 
163 | ### 1. Enter Repository URL
164 | Enter any public GitHub repository URL in the sidebar:
165 | ```
166 | https://github.com/tiangolo/fastapi
167 | ```
168 | 
169 | ### 2. Watch Analysis Progress
170 | Real-time progress indicators show:
171 | - ⏳ Cloning repository from GitHub
172 | - 🔍 Analyzing code structure
173 | - 🧠 Generating AI insights with IBM watsonx.ai Granite
174 | - ✅ Analysis complete!
175 | 
176 | ### 3. Explore Onboarding Guide
177 | AI-generated guide includes:
178 | - **Project Overview** - Purpose and description
179 | - **Technology Stack** - Languages and frameworks
180 | - **Architecture Insights** - Design patterns and structure
181 | - **Setup Instructions** - How to get started
182 | - **Key Files** - Important files with snippets
183 | 
184 | ### 4. Browse File Tree
185 | - View complete repository structure
186 | - Files tagged with programming language
187 | - Hierarchical organization
188 | 
189 | ### 5. Ask Questions
190 | Interactive chat interface for:
191 | - Feature explanations
192 | - Code references
193 | - Architecture questions
194 | - Setup guidance
195 | 
196 | ---
197 | 
198 | ## ⚙️ Configuration
199 | 
200 | ### Required Environment Variables
201 | 
202 | **Backend (`backend/.env`):**
203 | ```bash
204 | # IBM watsonx.ai Configuration
205 | WATSONX_API_KEY=your_api_key_here
206 | WATSONX_PROJECT_ID=your_project_id_here
207 | WATSONX_URL=https://us-south.ml.cloud.ibm.com
208 | WATSONX_MODEL_ID=ibm/granite-13b-chat-v2
209 | 
210 | # Application Settings
211 | REPO_CLONE_DIR=/tmp/repos
212 | CACHE_TTL_DAYS=7
213 | API_PORT=8000
214 | ```
215 | 
216 | **Streamlit (`.env`):**
217 | ```bash
218 | BACKEND_URL=http://localhost:8000
219 | ```
220 | 
221 | ---
222 | 
223 | ## 🎨 UI/UX Features
224 | 
225 | ### IBM Carbon Design System
226 | - **Dark Theme** - Professional developer-focused design
227 | - **Color Palette**:
228 |   - Background: `#161616` (Gray 100)
229 |   - Surface: `#262626` (Gray 90)
230 |   - Primary: `#0f62fe` (Blue 60)
231 |   - Text: `#f4f4f4` (Gray 10)
232 | 
233 | ### Interactive Elements
234 | - Collapsible sections for better organization
235 | - Syntax-highlighted code snippets
236 | - Animated progress indicators
237 | - Responsive layout
238 | - Smooth transitions
239 | 
240 | ---
241 | 
242 | ## 🧪 Example Repositories to Try
243 | 
244 | **Fast Analysis (< 1 minute):**
245 | - Flask: `https://github.com/pallets/flask`
246 | - Requests: `https://github.com/psf/requests`
247 | 
248 | **Medium (1-2 minutes):**
249 | - FastAPI: `https://github.com/tiangolo/fastapi` ⭐ **Recommended**
250 | - Django: `https://github.com/django/django`
251 | 
252 | **Large (2-3 minutes):**
253 | - React: `https://github.com/facebook/react`
254 | - VS Code: `https://github.com/microsoft/vscode`
255 | 
256 | ---
257 | 
258 | ## 🔧 Troubleshooting
259 | 
260 | ### Backend Connection Error
261 | ```bash
262 | # Check if backend is running
263 | curl http://localhost:8000/health
264 | 
265 | # Restart backend
266 | cd backend && python api.py
267 | ```
268 | 
269 | ### Import Errors
270 | ```bash
271 | # Install dependencies
272 | pip install -r requirements-streamlit.txt
273 | pip install -r backend/requirements.txt
274 | ```
275 | 
276 | ### Invalid GitHub URL
277 | Ensure URL format is:
278 | - ✅ `https://github.com/owner/repo`
279 | - ❌ `github.com/owner/repo` (missing https://)
280 | - ❌ `https://github.com/owner/repo.git` (remove .git)
281 | 
282 | ---
283 | 
284 | ## 🚀 Deployment
285 | 
286 | ### Local Development
287 | 1. Start backend: `python backend/api.py`
288 | 2. Start Streamlit: `streamlit run streamlit_app.py`
289 | 
290 | ### IBM Cloud (Future)
291 | - Deploy FastAPI to IBM Cloud Code Engine
292 | - Deploy Streamlit to IBM Cloud Code Engine
293 | - Configure IBM Cloudant for persistent caching
294 | - Set up watsonx.ai service binding
295 | 
296 | ---
297 | 
298 | ## 🎯 Use Cases
299 | 
300 | ### For Developers
301 | - Quickly understand new codebases
302 | - Get up to speed on team projects
303 | - Learn from open-source repositories
304 | - Explore unfamiliar technologies
305 | 
306 | ### For Teams
307 | - Streamline onboarding process
308 | - Reduce time-to-productivity
309 | - Create consistent documentation
310 | - Share knowledge effectively
311 | 
312 | ### For Educators
313 | - Teach software architecture
314 | - Analyze example projects
315 | - Demonstrate best practices
316 | - Compare different approaches
317 | 
318 | ---
319 | 
320 | ## 🏆 Hackathon Highlights
321 | 
322 | ### Innovation
323 | - ✅ Novel application of IBM watsonx.ai Granite models
324 | - ✅ Solves real developer pain point
325 | - ✅ Production-ready architecture
326 | - ✅ Scalable and extensible
327 | 
328 | ### Technical Excellence
329 | - ✅ Clean, maintainable code
330 | - ✅ Comprehensive error handling
331 | - ✅ Professional UI/UX
332 | - ✅ Complete documentation
333 | 
334 | ### IBM Integration
335 | - ✅ IBM watsonx.ai Granite models
336 | - ✅ IBM Carbon Design System
337 | - ✅ Ready for IBM Cloud deployment
338 | - ✅ Showcases platform capabilities
339 | 
340 | ---
341 | 
342 | ## 📈 Future Enhancements
343 | 
344 | ### Phase 1 (Post-Hackathon)
345 | - [ ] IBM Cloudant integration for persistent caching
346 | - [ ] Multi-repository comparison
347 | - [ ] Advanced code metrics
348 | - [ ] Security vulnerability scanning
349 | 
350 | ### Phase 2
351 | - [ ] Team collaboration features
352 | - [ ] Shared annotations and notes
353 | - [ ] Knowledge base building
354 | - [ ] Custom analysis templates
355 | 
356 | ### Phase 3
357 | - [ ] IDE extensions (VSCode, IntelliJ)
358 | - [ ] CLI tool
359 | - [ ] API for third-party integrations
360 | - [ ] Enterprise features
361 | 
362 | ---
363 | 
364 | ## 🤝 Contributing
365 | 
366 | This project was built for the IBM Hackathon 2026. For improvements:
367 | 
368 | 1. Fork the repository
369 | 2. Create a feature branch
370 | 3. Make your changes
371 | 4. Submit a pull request
372 | 
373 | ---
374 | 
375 | ## 📄 License
376 | 
377 | [Specify your license here - e.g., MIT, Apache 2.0]
378 | 
379 | ---
380 | 
381 | ## 🙏 Acknowledgments
382 | 
383 | - **IBM watsonx.ai** for providing the Granite models
384 | - **IBM Carbon Design System** for design inspiration
385 | - **Streamlit** for the amazing framework
386 | - **FastAPI** for the robust backend
387 | - **Open Source Community** for inspiration
388 | 
389 | ---
390 | 
391 | ## 📞 Contact
392 | 
393 | For questions or feedback:
394 | - Create a GitHub issue
395 | - Contact: [Your contact information]
396 | - IBM watsonx.ai docs: https://www.ibm.com/docs/en/watsonx-as-a-service
397 | 
398 | ---
399 | 
400 | ## 🎉 Demo Video
401 | 
402 | [Link to demo video if available]
403 | 
404 | ---
405 | 
406 | **Built with ❤️ for IBM Hackathon 2026**
407 | 
408 | *Powered by IBM watsonx.ai Granite Models*
409 | 
410 | ---
411 | 
412 | ## 📊 Quick Stats
413 | 
414 | - **Lines of Code**: ~1,500+
415 | - **Files Created**: 15+
416 | - **Technologies**: 10+
417 | - **Development Time**: Hackathon sprint
418 | - **AI Model**: IBM Granite 13B Chat v2
419 | - **UI Framework**: Streamlit + IBM Carbon Design
420 | - **Backend**: FastAPI + Python 3.9+
421 | 
422 | ---
423 | 
424 | **Ready to revolutionize developer onboarding? Get started now! 🚀**
</content>
</file>
<file><path>AGENTS.md</path>
<content lines="1-744">
  1 | # DevOnboard AI - Architecture & Development Guide
  2 | 
  3 | ## 🎯 Project Overview
  4 | 
  5 | **DevOnboard AI** is an intelligent developer onboarding assistant that streamlines the process of understanding new codebases. It clones GitHub repositories, performs deep analysis using IBM watsonx.ai Granite models, and provides an interactive chat interface where developers can explore and learn about the codebase through natural language conversations.
  6 | 
  7 | ### Key Features
  8 | - 🔄 Automated GitHub repository cloning and analysis
  9 | - 🧠 AI-powered codebase understanding using watsonx.ai Granite models
 10 | - 💬 Context-aware chat interface with file-specific references
 11 | - 📊 Comprehensive onboarding guide generation
 12 | - 💾 Intelligent caching with IBM Cloudant
 13 | - 🚀 IBM Cloud-ready architecture with local development support
 14 | 
 15 | ---
 16 | 
 17 | ## 🏗️ System Architecture
 18 | 
 19 | ### High-Level Architecture
 20 | 
 21 | ```mermaid
 22 | graph TB
 23 |     User[Developer User] --> Frontend[React Frontend]
 24 |     Frontend --> API[FastAPI Backend]
 25 |     API --> RepoCloner[Repository Cloner]
 26 |     API --> Analyzer[Code Analyzer]
 27 |     API --> WatsonX[watsonx.ai Client]
 28 |     API --> Cache[Cloudant Cache]
 29 |     
 30 |     RepoCloner --> LocalRepo[Local Repository]
 31 |     Analyzer --> LocalRepo
 32 |     Analyzer --> WatsonX
 33 |     WatsonX --> Granite[Granite Model]
 34 |     
 35 |     Cache --> AnalysisCache[Analysis Results]
 36 |     Cache --> ChatCache[Chat History]
 37 |     
 38 |     style Frontend fill:#61dafb
 39 |     style API fill:#009688
 40 |     style WatsonX fill:#0f62fe
 41 |     style Cache fill:#1192e8
 42 |     style Granite fill:#8a3ffc
 43 | ```
 44 | 
 45 | ### Component Interaction Flow
 46 | 
 47 | ```mermaid
 48 | sequenceDiagram
 49 |     participant User
 50 |     participant Frontend
 51 |     participant API
 52 |     participant RepoCloner
 53 |     participant Analyzer
 54 |     participant WatsonX
 55 |     participant Cloudant
 56 |     
 57 |     User->>Frontend: Enter GitHub URL
 58 |     Frontend->>API: POST /api/analyze
 59 |     API->>Cloudant: Check cache
 60 |     
 61 |     alt Cache Hit
 62 |         Cloudant-->>API: Return cached analysis
 63 |         API-->>Frontend: Analysis results
 64 |     else Cache Miss
 65 |         API->>RepoCloner: Clone repository
 66 |         RepoCloner-->>API: Repository path
 67 |         API->>Analyzer: Analyze codebase
 68 |         Analyzer->>WatsonX: Generate insights
 69 |         WatsonX-->>Analyzer: AI analysis
 70 |         Analyzer-->>API: Analysis results
 71 |         API->>Cloudant: Cache results
 72 |         API-->>Frontend: Analysis results
 73 |     end
 74 |     
 75 |     Frontend-->>User: Display onboarding guide
 76 |     
 77 |     User->>Frontend: Ask question
 78 |     Frontend->>API: POST /api/chat
 79 |     API->>Cloudant: Get session context
 80 |     API->>WatsonX: Generate response
 81 |     WatsonX-->>API: AI response
 82 |     API->>Cloudant: Update chat history
 83 |     API-->>Frontend: Chat response
 84 |     Frontend-->>User: Display answer
 85 | ```
 86 | 
 87 | ---
 88 | 
 89 | ## 🛠️ Technology Stack
 90 | 
 91 | ### Backend
 92 | - **Framework**: FastAPI 0.104+
 93 |   - High-performance async API framework
 94 |   - Automatic OpenAPI documentation
 95 |   - Built-in validation with Pydantic
 96 |   
 97 | - **AI/ML**: IBM watsonx.ai
 98 |   - Model: Granite (ibm/granite-13b-chat-v2 or similar)
 99 |   - Purpose: Code analysis, documentation generation, Q&A
100 |   
101 | - **Database**: IBM Cloudant
102 |   - NoSQL document database
103 |   - Caching layer for analysis results
104 |   - Session and chat history storage
105 |   
106 | - **Repository Management**: GitPython
107 |   - Clone and manage Git repositories
108 |   - Extract repository metadata
109 | 
110 | - **Code Analysis**: 
111 |   - `tree-sitter` - Syntax tree parsing
112 |   - `radon` - Code complexity metrics
113 |   - `pygments` - Syntax highlighting and language detection
114 | 
115 | ### Frontend
116 | - **Framework**: React 18+
117 |   - Component-based UI architecture
118 |   - Hooks for state management
119 |   
120 | - **UI Library**: Material-UI (MUI) or Tailwind CSS
121 |   - Modern, responsive design
122 |   - Pre-built components
123 |   
124 | - **State Management**: React Context API / Zustand
125 |   - Global state for chat history
126 |   - Session management
127 |   
128 | - **HTTP Client**: Axios
129 |   - API communication
130 |   - Request/response interceptors
131 | 
132 | - **Markdown Rendering**: react-markdown
133 |   - Display formatted onboarding guides
134 |   - Code syntax highlighting
135 | 
136 | ### Development & Deployment
137 | - **Local Development**: 
138 |   - Docker Compose for service orchestration
139 |   - Hot reload for both frontend and backend
140 |   
141 | - **IBM Cloud Ready**:
142 |   - Cloud Foundry or Code Engine deployment
143 |   - Cloudant as managed service
144 |   - watsonx.ai API integration
145 | 
146 | ---
147 | 
148 | ## 📁 Project Structure
149 | 
150 | ```
151 | ibm-hackathon/
152 | ├── backend/
153 | │   ├── __init__.py
154 | │   ├── api.py                    # FastAPI application & routes
155 | │   ├── analyzer.py               # Code analysis logic
156 | │   ├── watsonx_client.py         # watsonx.ai integration
157 | │   ├── cloudant_client.py        # Cloudant database operations
158 | │   ├── repo_manager.py           # Git repository operations
159 | │   ├── models.py                 # Pydantic models
160 | │   ├── config.py                 # Configuration management
161 | │   ├── utils.py                  # Utility functions
162 | │   ├── requirements.txt          # Python dependencies
163 | │   ├── .env.example              # Environment variables template
164 | │   └── tests/
165 | │       ├── test_api.py
166 | │       ├── test_analyzer.py
167 | │       └── test_watsonx.py
168 | │
169 | ├── frontend/
170 | │   ├── public/
171 | │   │   ├── index.html
172 | │   │   └── favicon.ico
173 | │   ├── src/
174 | │   │   ├── components/
175 | │   │   │   ├── RepositoryInput.jsx    # GitHub URL input
176 | │   │   │   ├── OnboardingGuide.jsx    # Display analysis results
177 | │   │   │   ├── ChatInterface.jsx      # Chat UI
178 | │   │   │   ├── CodeReference.jsx      # File/code snippets
179 | │   │   │   └── LoadingSpinner.jsx     # Loading states
180 | │   │   ├── services/
181 | │   │   │   └── api.js                 # API client
182 | │   │   ├── context/
183 | │   │   │   └── AppContext.jsx         # Global state
184 | │   │   ├── hooks/
185 | │   │   │   ├── useAnalysis.js
186 | │   │   │   └── useChat.js
187 | │   │   ├── utils/
188 | │   │   │   └── helpers.js
189 | │   │   ├── App.jsx                    # Main application
190 | │   │   ├── index.jsx                  # Entry point
191 | │   │   └── styles/
192 | │   │       └── main.css
193 | │   ├── package.json
194 | │   └── vite.config.js / webpack.config.js
195 | │
196 | ├── docker-compose.yml            # Local development setup
197 | ├── Dockerfile.backend            # Backend container
198 | ├── Dockerfile.frontend           # Frontend container
199 | ├── .gitignore
200 | ├── README.md                     # Project overview
201 | ├── AGENTS.md                     # This file
202 | └── docs/
203 |     ├── API.md                    # API documentation
204 |     ├── DEPLOYMENT.md             # Deployment guide
205 |     └── DEVELOPMENT.md            # Development setup
206 | ```
207 | 
208 | ---
209 | 
210 | ## 🔌 API Endpoints
211 | 
212 | ### Repository Analysis
213 | 
214 | #### `POST /api/analyze`
215 | Analyze a GitHub repository and generate onboarding guide.
216 | 
217 | **Request Body:**
218 | ```json
219 | {
220 |   "repo_url": "https://github.com/username/repository",
221 |   "branch": "main",
222 |   "force_refresh": false
223 | }
224 | ```
225 | 
226 | **Response:**
227 | ```json
228 | {
229 |   "session_id": "uuid-v4",
230 |   "repository": {
231 |     "name": "repository",
232 |     "owner": "username",
233 |     "url": "https://github.com/username/repository",
234 |     "branch": "main",
235 |     "last_commit": "abc123"
236 |   },
237 |   "analysis": {
238 |     "overview": "Project description...",
239 |     "tech_stack": ["Python", "FastAPI", "React"],
240 |     "file_structure": {...},
241 |     "key_files": [...],
242 |     "dependencies": {...},
243 |     "setup_instructions": "...",
244 |     "architecture_insights": "..."
245 |   },
246 |   "cached": false,
247 |   "analyzed_at": "2026-05-16T09:00:00Z"
248 | }
249 | ```
250 | 
251 | ### Chat Interface
252 | 
253 | #### `POST /api/chat`
254 | Send a message and get AI-powered response about the codebase.
255 | 
256 | **Request Body:**
257 | ```json
258 | {
259 |   "session_id": "uuid-v4",
260 |   "message": "How does authentication work in this project?",
261 |   "context": {
262 |     "file_path": "backend/auth.py",
263 |     "line_range": [10, 50]
264 |   }
265 | }
266 | ```
267 | 
268 | **Response:**
269 | ```json
270 | {
271 |   "response": "Authentication in this project uses JWT tokens...",
272 |   "references": [
273 |     {
274 |       "file": "backend/auth.py",
275 |       "lines": [15, 30],
276 |       "snippet": "def authenticate_user(...)..."
277 |     }
278 |   ],
279 |   "timestamp": "2026-05-16T09:05:00Z"
280 | }
281 | ```
282 | 
283 | #### `GET /api/chat/history/{session_id}`
284 | Retrieve chat history for a session.
285 | 
286 | **Response:**
287 | ```json
288 | {
289 |   "session_id": "uuid-v4",
290 |   "messages": [
291 |     {
292 |       "role": "user",
293 |       "content": "How does authentication work?",
294 |       "timestamp": "2026-05-16T09:05:00Z"
295 |     },
296 |     {
297 |       "role": "assistant",
298 |       "content": "Authentication uses JWT tokens...",
299 |       "references": [...],
300 |       "timestamp": "2026-05-16T09:05:02Z"
301 |     }
302 |   ]
303 | }
304 | ```
305 | 
306 | ### File Operations
307 | 
308 | #### `GET /api/files/{session_id}`
309 | Get file tree for analyzed repository.
310 | 
311 | #### `GET /api/files/{session_id}/content`
312 | Get content of a specific file.
313 | 
314 | **Query Parameters:**
315 | - `path`: File path relative to repository root
316 | 
317 | ---
318 | 
319 | ## 💾 Data Models
320 | 
321 | ### Cloudant Collections
322 | 
323 | #### `repository_analysis`
324 | Stores cached analysis results.
325 | 
326 | ```json
327 | {
328 |   "_id": "repo_hash_branch",
329 |   "type": "analysis",
330 |   "repo_url": "https://github.com/username/repository",
331 |   "branch": "main",
332 |   "analysis": {...},
333 |   "created_at": "2026-05-16T09:00:00Z",
334 |   "expires_at": "2026-05-23T09:00:00Z"
335 | }
336 | ```
337 | 
338 | #### `chat_sessions`
339 | Stores chat history per session.
340 | 
341 | ```json
342 | {
343 |   "_id": "session_uuid",
344 |   "type": "chat_session",
345 |   "repo_url": "https://github.com/username/repository",
346 |   "messages": [...],
347 |   "created_at": "2026-05-16T09:00:00Z",
348 |   "last_activity": "2026-05-16T09:15:00Z"
349 | }
350 | ```
351 | 
352 | ---
353 | 
354 | ## 🧠 AI Integration Details
355 | 
356 | ### watsonx.ai Configuration
357 | 
358 | **Model Selection:**
359 | - Primary: `ibm/granite-3-8b-instruct` (general purpose instruction model)
360 | - Alternative: `ibm/granite-8b-code-instruct` (specialized for code analysis)
361 | - Alternative: `meta-llama/llama-3-3-70b-instruct` (larger model for complex tasks)
362 | 
363 | **Prompt Templates:**
364 | 
365 | #### Repository Analysis Prompt
366 | ```
367 | You are an expert software architect analyzing a codebase for developer onboarding.
368 | 
369 | Repository: {repo_name}
370 | Files analyzed: {file_count}
371 | Primary languages: {languages}
372 | 
373 | File structure:
374 | {file_tree}
375 | 
376 | Key files content:
377 | {key_files_content}
378 | 
379 | Dependencies:
380 | {dependencies}
381 | 
382 | Generate a comprehensive onboarding guide including:
383 | 1. Project overview and purpose
384 | 2. Technology stack explanation
385 | 3. Architecture overview
386 | 4. Setup instructions
387 | 5. Key components and their interactions
388 | 6. Development workflow
389 | 7. Important files and their purposes
390 | 
391 | Format the response in markdown.
392 | ```
393 | 
394 | #### Chat Prompt
395 | ```
396 | You are a helpful AI assistant helping a developer understand a codebase.
397 | 
398 | Repository context:
399 | {repository_overview}
400 | 
401 | Current file context (if provided):
402 | {file_context}
403 | 
404 | Chat history:
405 | {chat_history}
406 | 
407 | User question: {user_message}
408 | 
409 | Provide a clear, concise answer. If referencing specific code, include file paths and line numbers.
410 | ```
411 | 
412 | ### Inference Parameters
413 | ```python
414 | {
415 |     "model_id": "ibm/granite-3-8b-instruct",
416 |     "parameters": {
417 |         "max_new_tokens": 2048,
418 |         "temperature": 0.7,
419 |         "top_p": 0.9,
420 |         "top_k": 50,
421 |         "repetition_penalty": 1.1
422 |     }
423 | }
424 | ```
425 | 
426 | ### Available Models in watsonx.ai
427 | The following models are supported in the current environment:
428 | - **Granite Models**: `ibm/granite-3-8b-instruct`, `ibm/granite-8b-code-instruct`, `ibm/granite-3-1-8b-base`
429 | - **Llama Models**: `meta-llama/llama-3-3-70b-instruct`, `meta-llama/llama-3-1-8b`
430 | - **Mistral Models**: `mistral-large-2512`, `mistralai/mistral-small-3-1-24b-instruct-2503`
431 | 
432 | ---
433 | 
434 | ## 🔧 Configuration
435 | 
436 | ### Environment Variables
437 | 
438 | **Backend (`.env`):**
439 | ```bash
440 | # watsonx.ai Configuration
441 | WATSONX_API_KEY=your_api_key_here
442 | WATSONX_PROJECT_ID=your_project_id
443 | WATSONX_URL=https://us-south.ml.cloud.ibm.com
444 | 
445 | # Cloudant Configuration
446 | CLOUDANT_URL=https://your-instance.cloudantnosqldb.appdomain.cloud
447 | CLOUDANT_API_KEY=your_cloudant_api_key
448 | CLOUDANT_DATABASE=devonboard_cache
449 | 
450 | # Application Settings
451 | REPO_CLONE_DIR=/tmp/repos
452 | MAX_REPO_SIZE_MB=500
453 | CACHE_TTL_DAYS=7
454 | SESSION_TIMEOUT_HOURS=24
455 | 
456 | # API Settings
457 | API_HOST=0.0.0.0
458 | API_PORT=8000
459 | CORS_ORIGINS=http://localhost:3000,http://localhost:5173
460 | 
461 | # Logging
462 | LOG_LEVEL=INFO
463 | ```
464 | 
465 | **Frontend (`.env`):**
466 | ```bash
467 | VITE_API_URL=http://localhost:8000
468 | VITE_APP_NAME=DevOnboard AI
469 | ```
470 | 
471 | ---
472 | 
473 | ## 🚀 Development Plan
474 | 
475 | ### Phase 1: Backend Foundation (Days 1-2)
476 | 1. **Setup FastAPI Application**
477 |    - Initialize FastAPI project structure
478 |    - Configure CORS and middleware
479 |    - Setup logging and error handling
480 |    - Create Pydantic models for requests/responses
481 | 
482 | 2. **Implement watsonx.ai Client**
483 |    - Create [`watsonx_client.py`](backend/watsonx_client.py)
484 |    - Implement authentication
485 |    - Create prompt templates
486 |    - Add retry logic and error handling
487 | 
488 | 3. **Implement Cloudant Client**
489 |    - Create [`cloudant_client.py`](backend/cloudant_client.py)
490 |    - Setup database connection
491 |    - Implement CRUD operations
492 |    - Add caching logic with TTL
493 | 
494 | ### Phase 2: Repository Analysis (Days 2-3)
495 | 1. **Repository Manager**
496 |    - Create [`repo_manager.py`](backend/repo_manager.py)
497 |    - Implement Git cloning with GitPython
498 |    - Add repository validation
499 |    - Handle cleanup of temporary files
500 | 
501 | 2. **Code Analyzer**
502 |    - Create [`analyzer.py`](backend/analyzer.py)
503 |    - Implement file tree generation
504 |    - Add language detection
505 |    - Extract dependencies from package files
506 |    - Identify key files (README, main entry points)
507 |    - Calculate code metrics
508 | 
509 | 3. **Analysis Pipeline**
510 |    - Integrate analyzer with watsonx.ai
511 |    - Generate comprehensive onboarding guide
512 |    - Cache results in Cloudant
513 |    - Return structured analysis
514 | 
515 | ### Phase 3: Chat Functionality (Days 3-4)
516 | 1. **Chat Endpoint**
517 |    - Implement `/api/chat` endpoint
518 |    - Session management
519 |    - Context-aware prompting
520 |    - File reference extraction
521 | 
522 | 2. **Chat History**
523 |    - Store conversations in Cloudant
524 |    - Retrieve session history
525 |    - Implement context window management
526 | 
527 | ### Phase 4: Frontend Development (Days 4-5)
528 | 1. **React Application Setup**
529 |    - Initialize React project with Vite
530 |    - Setup routing
531 |    - Configure API client
532 |    - Create global state management
533 | 
534 | 2. **Core Components**
535 |    - [`RepositoryInput.jsx`](frontend/src/components/RepositoryInput.jsx) - URL input form
536 |    - [`OnboardingGuide.jsx`](frontend/src/components/OnboardingGuide.jsx) - Display analysis
537 |    - [`ChatInterface.jsx`](frontend/src/components/ChatInterface.jsx) - Chat UI
538 |    - [`CodeReference.jsx`](frontend/src/components/CodeReference.jsx) - Code snippets
539 | 
540 | 3. **Integration**
541 |    - Connect frontend to backend APIs
542 |    - Implement loading states
543 |    - Add error handling
544 |    - Style with UI library
545 | 
546 | ### Phase 5: Testing & Polish (Days 5-6)
547 | 1. **Backend Testing**
548 |    - Unit tests for core functions
549 |    - Integration tests for API endpoints
550 |    - Mock watsonx.ai and Cloudant
551 | 
552 | 2. **Frontend Testing**
553 |    - Component tests
554 |    - Integration tests
555 |    - E2E testing with Playwright/Cypress
556 | 
557 | 3. **Documentation**
558 |    - API documentation
559 |    - Setup instructions
560 |    - Deployment guide
561 | 
562 | ### Phase 6: Deployment Preparation (Day 6)
563 | 1. **Local Development**
564 |    - Create Docker Compose setup
565 |    - Test full stack locally
566 | 
567 | 2. **IBM Cloud Configuration**
568 |    - Prepare Cloud Foundry manifest
569 |    - Configure Cloudant service binding
570 |    - Setup environment variables
571 |    - Create deployment scripts
572 | 
573 | ---
574 | 
575 | ## 🎨 User Experience Flow
576 | 
577 | ### 1. Repository Analysis
578 | ```mermaid
579 | graph LR
580 |     A[Enter GitHub URL] --> B[Validate URL]
581 |     B --> C{Cached?}
582 |     C -->|Yes| D[Load from Cache]
583 |     C -->|No| E[Clone Repository]
584 |     E --> F[Analyze Code]
585 |     F --> G[Generate Guide]
586 |     G --> H[Cache Results]
587 |     D --> I[Display Guide]
588 |     H --> I
589 |     I --> J[Enable Chat]
590 | ```
591 | 
592 | ### 2. Chat Interaction
593 | ```mermaid
594 | graph LR
595 |     A[User Question] --> B[Load Context]
596 |     B --> C[Generate Prompt]
597 |     C --> D[Call watsonx.ai]
598 |     D --> E[Parse Response]
599 |     E --> F[Extract References]
600 |     F --> G[Display Answer]
601 |     G --> H[Update History]
602 |     H --> I[Cache Session]
603 | ```
604 | 
605 | ---
606 | 
607 | ## 🔒 Security Considerations
608 | 
609 | 1. **API Key Management**
610 |    - Store credentials in environment variables
611 |    - Never commit `.env` files
612 |    - Use IBM Cloud secrets management in production
613 | 
614 | 2. **Repository Access**
615 |    - Validate GitHub URLs
616 |    - Limit repository size
617 |    - Sanitize file paths
618 |    - Implement rate limiting
619 | 
620 | 3. **Data Privacy**
621 |    - Don't store sensitive code permanently
622 |    - Implement session expiration
623 |    - Clear temporary repositories
624 |    - GDPR compliance for chat history
625 | 
626 | 4. **Input Validation**
627 |    - Validate all user inputs
628 |    - Sanitize file paths
629 |    - Prevent code injection
630 |    - Rate limit API calls
631 | 
632 | ---
633 | 
634 | ## 📊 Performance Optimization
635 | 
636 | 1. **Caching Strategy**
637 |    - Cache analysis results for 7 days
638 |    - Invalidate on repository updates
639 |    - Use Cloudant indexes for fast lookups
640 | 
641 | 2. **Repository Analysis**
642 |    - Limit file size for analysis
643 |    - Skip binary files
644 |    - Parallel file processing
645 |    - Incremental analysis for large repos
646 | 
647 | 3. **AI Inference**
648 |    - Batch similar requests
649 |    - Implement request queuing
650 |    - Use streaming responses for chat
651 |    - Cache common questions
652 | 
653 | 4. **Frontend**
654 |    - Lazy load components
655 |    - Virtualize long lists
656 |    - Debounce user inputs
657 |    - Optimize bundle size
658 | 
659 | ---
660 | 
661 | ## 🧪 Testing Strategy
662 | 
663 | ### Backend Tests
664 | ```python
665 | # tests/test_analyzer.py
666 | def test_analyze_repository():
667 |     """Test repository analysis pipeline"""
668 |     pass
669 | 
670 | def test_cache_hit():
671 |     """Test Cloudant cache retrieval"""
672 |     pass
673 | 
674 | def test_watsonx_integration():
675 |     """Test watsonx.ai API calls"""
676 |     pass
677 | ```
678 | 
679 | ### Frontend Tests
680 | ```javascript
681 | // tests/ChatInterface.test.jsx
682 | describe('ChatInterface', () => {
683 |   it('sends message and displays response', () => {
684 |     // Test implementation
685 |   });
686 | });
687 | ```
688 | 
689 | ---
690 | 
691 | ## 📈 Future Enhancements
692 | 
693 | 1. **Multi-Repository Support**
694 |    - Compare multiple repositories
695 |    - Cross-repository search
696 |    - Dependency graph visualization
697 | 
698 | 2. **Advanced Analysis**
699 |    - Security vulnerability scanning
700 |    - Code quality metrics
701 |    - Performance bottleneck detection
702 |    - Architecture diagram generation
703 | 
704 | 3. **Collaboration Features**
705 |    - Team onboarding sessions
706 |    - Shared annotations
707 |    - Knowledge base building
708 | 
709 | 4. **IDE Integration**
710 |    - VSCode extension
711 |    - IntelliJ plugin
712 |    - CLI tool
713 | 
714 | ---
715 | 
716 | ## 🤝 Contributing
717 | 
718 | This project is built for the IBM Hackathon. For development:
719 | 
720 | 1. Clone the repository
721 | 2. Follow setup instructions in [`DEVELOPMENT.md`](docs/DEVELOPMENT.md)
722 | 3. Create feature branches
723 | 4. Submit pull requests with clear descriptions
724 | 
725 | ---
726 | 
727 | ## 📝 License
728 | 
729 | [Specify license - e.g., MIT, Apache 2.0]
730 | 
731 | ---
732 | 
733 | ## 🆘 Support
734 | 
735 | For issues or questions:
736 | - Create GitHub issues
737 | - Contact: [Your contact information]
738 | - IBM watsonx.ai documentation: https://www.ibm.com/docs/en/watsonx-as-a-service
739 | 
740 | ---
741 | 
742 | **Last Updated**: 2026-05-16
743 | **Version**: 1.0.0
744 | **Status**: In Development
</content>
</file>
<file><path>backend/api.py</path>
<content lines="1-466">
  1 | """
  2 | FastAPI application for DevOnboard AI backend.
  3 | Provides REST API endpoints for repository analysis and chat functionality.
  4 | """
  5 | 
  6 | from fastapi import FastAPI, HTTPException, Query
  7 | from fastapi.middleware.cors import CORSMiddleware
  8 | from typing import Dict, List, Optional
  9 | from datetime import datetime
 10 | import asyncio
 11 | 
 12 | from models import (
 13 |     AnalyzeRequest, AnalyzeResponse, ChatRequest, ChatResponse,
 14 |     ChatHistoryResponse, ChatMessage, FileTreeResponse,
 15 |     FileContentRequest, FileContentResponse, ErrorResponse,
 16 |     CodeReference, CachedAnalysis, ChatSession
 17 | )
 18 | from analyzer import CodebaseAnalyzer
 19 | from watsonx_client import WatsonXClient
 20 | from config import settings
 21 | from utils import (
 22 |     get_logger, generate_session_id, hash_repo_url,
 23 |     calculate_expiry_time, is_expired, extract_code_snippet,
 24 |     sanitize_path
 25 | )
 26 | 
 27 | logger = get_logger(__name__)
 28 | 
 29 | # Initialize FastAPI app
 30 | app = FastAPI(
 31 |     title="DevPilot API",
 32 |     description="AI-powered code analysis and developer onboarding",
 33 |     version="1.0.0"
 34 | )
 35 | 
 36 | # Configure CORS
 37 | app.add_middleware(
 38 |     CORSMiddleware,
 39 |     allow_origins=settings.get_cors_origins_list(),
 40 |     allow_credentials=True,
 41 |     allow_methods=["*"],
 42 |     allow_headers=["*"],
 43 | )
 44 | 
 45 | # Initialize components
 46 | analyzer = CodebaseAnalyzer()
 47 | watsonx_client = WatsonXClient()
 48 | 
 49 | # In-memory cache (temporary, will be replaced with Cloudant)
 50 | analysis_cache: Dict[str, CachedAnalysis] = {}
 51 | chat_sessions: Dict[str, ChatSession] = {}
 52 | repo_paths: Dict[str, str] = {}  # session_id -> repo_path mapping
 53 | session_to_cache_key: Dict[str, str] = {}  # session_id -> cache_key mapping for recovery
 54 | 
 55 | 
 56 | @app.on_event("startup")
 57 | async def startup_event():
 58 |     """Initialize application on startup."""
 59 |     logger.info("Starting DevPilot API")
 60 |     settings.ensure_repo_dir_exists()
 61 | 
 62 | 
 63 | @app.on_event("shutdown")
 64 | async def shutdown_event():
 65 |     """Cleanup on shutdown."""
 66 |     logger.info("Shutting down DevPilot API")
 67 | 
 68 | 
 69 | @app.get("/")
 70 | async def root():
 71 |     """Root endpoint."""
 72 |     return {
 73 |         "name": "DevPilot API",
 74 |         "version": "1.0.0",
 75 |         "status": "running"
 76 |     }
 77 | 
 78 | 
 79 | @app.get("/health")
 80 | async def health_check():
 81 |     """Health check endpoint."""
 82 |     return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}
 83 | 
 84 | 
 85 | @app.post("/api/analyze", response_model=AnalyzeResponse)
 86 | async def analyze_repository(request: AnalyzeRequest):
 87 |     """
 88 |     Analyze a GitHub repository and generate onboarding guide.
 89 |     
 90 |     Args:
 91 |         request: Analysis request with repo URL and options
 92 |         
 93 |     Returns:
 94 |         Complete analysis results
 95 |     """
 96 |     try:
 97 |         repo_url = str(request.repo_url)
 98 |         branch = request.branch
 99 |         force_refresh = request.force_refresh
100 |         
101 |         logger.info(f"Received analysis request for {repo_url} (branch: {branch})")
102 |         
103 |         # Check cache unless force refresh
104 |         cache_key = hash_repo_url(repo_url, branch)
105 |         
106 |         if not force_refresh and cache_key in analysis_cache:
107 |             cached = analysis_cache[cache_key]
108 |             
109 |             # Check if cache is still valid
110 |             if not is_expired(cached.expires_at):
111 |                 logger.info(f"Returning cached analysis for {repo_url}")
112 |                 
113 |                 # Create new session for cached result
114 |                 session_id = generate_session_id()
115 |                 
116 |                 # Store repo path and cache key for this session
117 |                 repo_paths[session_id] = settings.get_repo_path(cache_key)
118 |                 session_to_cache_key[session_id] = cache_key
119 |                 
120 |                 # Initialize chat session if not exists
121 |                 if session_id not in chat_sessions:
122 |                     chat_sessions[session_id] = ChatSession(
123 |                         session_id=session_id,
124 |                         repo_url=repo_url,
125 |                         messages=[],
126 |                         created_at=datetime.utcnow(),
127 |                         last_activity=datetime.utcnow()
128 |                     )
129 |                 
130 |                 return AnalyzeResponse(
131 |                     session_id=session_id,
132 |                     repository=cached.repository,
133 |                     analysis=cached.analysis,
134 |                     cached=True,
135 |                     analyzed_at=cached.created_at
136 |                 )
137 |         
138 |         # Perform analysis
139 |         result = await analyzer.analyze_repository(repo_url, branch)
140 |         
141 |         # Cache the result
142 |         analysis_cache[cache_key] = CachedAnalysis(
143 |             repo_url=repo_url,
144 |             branch=branch,
145 |             analysis=result.analysis,
146 |             repository=result.repository,
147 |             created_at=result.analyzed_at,
148 |             expires_at=calculate_expiry_time(settings.cache_ttl_days)
149 |         )
150 |         
151 |         # Store repo path and cache key for this session
152 |         repo_paths[result.session_id] = settings.get_repo_path(cache_key)
153 |         session_to_cache_key[result.session_id] = cache_key
154 |         
155 |         # Initialize chat session
156 |         chat_sessions[result.session_id] = ChatSession(
157 |             session_id=result.session_id,
158 |             repo_url=repo_url,
159 |             messages=[],
160 |             created_at=datetime.utcnow(),
161 |             last_activity=datetime.utcnow()
162 |         )
163 |         
164 |         logger.info(f"Analysis complete for {repo_url}, session: {result.session_id}")
165 |         return result
166 |         
167 |     except ValueError as e:
168 |         logger.error(f"Validation error: {str(e)}")
169 |         raise HTTPException(status_code=400, detail=str(e))
170 |     except Exception as e:
171 |         logger.error(f"Error analyzing repository: {str(e)}")
172 |         raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")
173 | 
174 | 
175 | @app.post("/api/chat", response_model=ChatResponse)
176 | async def chat(request: ChatRequest):
177 |     """
178 |     Send a message and get AI-powered response about the codebase.
179 |     
180 |     Args:
181 |         request: Chat request with session ID and message
182 |         
183 |     Returns:
184 |         AI-generated response with code references
185 |     """
186 |     try:
187 |         session_id = request.session_id
188 |         user_message = request.message
189 |         
190 |         # Validate session - try to recover if not found
191 |         if session_id not in chat_sessions:
192 |             logger.warning(f"Session not found in chat_sessions: {session_id}")
193 |             
194 |             # Try to recover session from cache
195 |             if session_id in session_to_cache_key:
196 |                 cache_key = session_to_cache_key[session_id]
197 |                 if cache_key in analysis_cache:
198 |                     cached = analysis_cache[cache_key]
199 |                     logger.info(f"Recovering session {session_id} from cache")
200 |                     
201 |                     # Recreate chat session
202 |                     chat_sessions[session_id] = ChatSession(
203 |                         session_id=session_id,
204 |                         repo_url=cached.repo_url,
205 |                         messages=[],
206 |                         created_at=datetime.utcnow(),
207 |                         last_activity=datetime.utcnow()
208 |                     )
209 |                     
210 |                     # Ensure repo_path is set
211 |                     if session_id not in repo_paths:
212 |                         repo_paths[session_id] = settings.get_repo_path(cache_key)
213 |                 else:
214 |                     logger.error(f"Cache key {cache_key} not found in analysis_cache")
215 |                     raise HTTPException(
216 |                         status_code=404,
217 |                         detail=f"Session expired or not found. Please analyze the repository again. Session ID: {session_id}"
218 |                     )
219 |             else:
220 |                 logger.error(f"Session {session_id} not found in session_to_cache_key")
221 |                 logger.debug(f"Available sessions: {list(chat_sessions.keys())}")
222 |                 logger.debug(f"Total sessions in memory: {len(chat_sessions)}")
223 |                 raise HTTPException(
224 |                     status_code=404,
225 |                     detail=f"Session not found. Please analyze a repository first to create a session. Session ID: {session_id}"
226 |                 )
227 |         
228 |         session = chat_sessions[session_id]
229 |         
230 |         # Get repository context - try to find the cached analysis
231 |         # First, try to find the cache key by iterating through cache
232 |         cached = None
233 |         cache_key = None
234 |         for key, value in analysis_cache.items():
235 |             if value.repo_url == session.repo_url:
236 |                 cached = value
237 |                 cache_key = key
238 |                 break
239 |         
240 |         if not cached:
241 |             logger.error(f"Repository analysis not found for session {session_id}")
242 |             logger.debug(f"Session repo_url: {session.repo_url}")
243 |             logger.debug(f"Available cache keys: {list(analysis_cache.keys())}")
244 |             raise HTTPException(status_code=404, detail="Repository analysis not found")
245 |         repository_overview = cached.analysis.overview[:2000]  # Limit context size
246 |         
247 |         # Build file context if provided
248 |         file_context = None
249 |         if request.context:
250 |             repo_path = repo_paths.get(session_id)
251 |             if repo_path:
252 |                 try:
253 |                     file_path = sanitize_path(request.context.file_path)
254 |                     content, language, lines = analyzer.get_file_content(repo_path, file_path)
255 |                     
256 |                     # Extract specific line range if provided
257 |                     if request.context.line_range and len(request.context.line_range) == 2:
258 |                         start, end = request.context.line_range
259 |                         snippet = extract_code_snippet(content, start, end)
260 |                         file_context = f"File: {file_path}\nLines {start}-{end}:\n```{language or ''}\n{snippet}\n```"
261 |                     else:
262 |                         # Use first 50 lines as context
263 |                         snippet = extract_code_snippet(content, 1, 50)
264 |                         file_context = f"File: {file_path}\n```{language or ''}\n{snippet}\n```"
265 |                 except Exception as e:
266 |                     logger.warning(f"Could not load file context: {str(e)}")
267 |         
268 |         # Prepare chat history
269 |         chat_history = [
270 |             {"role": msg.role, "content": msg.content}
271 |             for msg in session.messages[-5:]  # Last 5 messages
272 |         ]
273 |         
274 |         # Generate response
275 |         logger.info(f"Generating chat response for session {session_id}")
276 |         response_text = watsonx_client.generate_chat_response(
277 |             repository_overview=repository_overview,
278 |             file_context=file_context,
279 |             chat_history=chat_history,
280 |             user_message=user_message
281 |         )
282 |         
283 |         # Extract code references from response (simplified)
284 |         references = []
285 |         # TODO: Implement proper code reference extraction
286 |         
287 |         # Create response
288 |         timestamp = datetime.utcnow()
289 |         response = ChatResponse(
290 |             response=response_text,
291 |             references=references,
292 |             timestamp=timestamp
293 |         )
294 |         
295 |         # Update chat history
296 |         session.messages.append(ChatMessage(
297 |             role="user",
298 |             content=user_message,
299 |             references=None,
300 |             timestamp=timestamp
301 |         ))
302 |         session.messages.append(ChatMessage(
303 |             role="assistant",
304 |             content=response_text,
305 |             references=references if references else None,
306 |             timestamp=timestamp
307 |         ))
308 |         session.last_activity = timestamp
309 |         
310 |         logger.info(f"Chat response generated for session {session_id}")
311 |         return response
312 |         
313 |     except HTTPException:
314 |         raise
315 |     except Exception as e:
316 |         logger.error(f"Error generating chat response: {str(e)}")
317 |         raise HTTPException(status_code=500, detail=f"Chat failed: {str(e)}")
318 | 
319 | 
320 | @app.get("/api/chat/history/{session_id}", response_model=ChatHistoryResponse)
321 | async def get_chat_history(session_id: str):
322 |     """
323 |     Retrieve chat history for a session.
324 |     
325 |     Args:
326 |         session_id: Session identifier
327 |         
328 |     Returns:
329 |         Chat message history
330 |     """
331 |     if session_id not in chat_sessions:
332 |         raise HTTPException(status_code=404, detail="Session not found")
333 |     
334 |     session = chat_sessions[session_id]
335 |     
336 |     return ChatHistoryResponse(
337 |         session_id=session_id,
338 |         messages=session.messages
339 |     )
340 | 
341 | 
342 | @app.get("/api/files/{session_id}", response_model=FileTreeResponse)
343 | async def get_file_tree(session_id: str):
344 |     """
345 |     Get file tree for analyzed repository.
346 |     
347 |     Args:
348 |         session_id: Session identifier
349 |         
350 |     Returns:
351 |         Repository file tree
352 |     """
353 |     # Validate session - try to recover if not found
354 |     if session_id not in chat_sessions:
355 |         logger.warning(f"Session not found in chat_sessions: {session_id}")
356 |         
357 |         # Try to recover session from cache
358 |         if session_id in session_to_cache_key:
359 |             cache_key = session_to_cache_key[session_id]
360 |             if cache_key in analysis_cache:
361 |                 cached = analysis_cache[cache_key]
362 |                 logger.info(f"Recovering session {session_id} from cache for file tree")
363 |                 
364 |                 # Recreate chat session
365 |                 chat_sessions[session_id] = ChatSession(
366 |                     session_id=session_id,
367 |                     repo_url=cached.repo_url,
368 |                     messages=[],
369 |                     created_at=datetime.utcnow(),
370 |                     last_activity=datetime.utcnow()
371 |                 )
372 |                 
373 |                 # Ensure repo_path is set
374 |                 if session_id not in repo_paths:
375 |                     repo_paths[session_id] = settings.get_repo_path(cache_key)
376 |             else:
377 |                 logger.error(f"Cache key {cache_key} not found in analysis_cache")
378 |                 raise HTTPException(
379 |                     status_code=404,
380 |                     detail=f"Session expired or not found. Please analyze the repository again. Session ID: {session_id}"
381 |                 )
382 |         else:
383 |             logger.error(f"Session {session_id} not found in session_to_cache_key")
384 |             logger.debug(f"Available sessions: {list(chat_sessions.keys())}")
385 |             logger.debug(f"Total sessions in memory: {len(chat_sessions)}")
386 |             raise HTTPException(
387 |                 status_code=404,
388 |                 detail=f"Session not found. Please analyze a repository first to create a session. Session ID: {session_id}"
389 |             )
390 |     
391 |     session = chat_sessions[session_id]
392 |     
393 |     # Find the cached analysis for this repository
394 |     cached = None
395 |     for key, value in analysis_cache.items():
396 |         if value.repo_url == session.repo_url:
397 |             cached = value
398 |             break
399 |     
400 |     if not cached:
401 |         raise HTTPException(status_code=404, detail="Repository analysis not found")
402 |     
403 |     return FileTreeResponse(
404 |         session_id=session_id,
405 |         file_tree=cached.analysis.file_structure
406 |     )
407 | 
408 | 
409 | @app.get("/api/files/{session_id}/content", response_model=FileContentResponse)
410 | async def get_file_content(
411 |     session_id: str,
412 |     path: str = Query(..., description="File path relative to repository root")
413 | ):
414 |     """
415 |     Get content of a specific file.
416 |     
417 |     Args:
418 |         session_id: Session identifier
419 |         path: File path
420 |         
421 |     Returns:
422 |         File content and metadata
423 |     """
424 |     if session_id not in repo_paths:
425 |         logger.error(f"Session not found in repo_paths: {session_id}")
426 |         logger.debug(f"Available repo_paths: {list(repo_paths.keys())}")
427 |         raise HTTPException(
428 |             status_code=404,
429 |             detail=f"Session not found. Please analyze a repository first to create a session. Session ID: {session_id}"
430 |         )
431 |     
432 |     repo_path = repo_paths[session_id]
433 |     safe_path = sanitize_path(path)
434 |     
435 |     try:
436 |         content, language, lines = analyzer.get_file_content(repo_path, safe_path)
437 |         
438 |         return FileContentResponse(
439 |             path=safe_path,
440 |             content=content,
441 |             language=language,
442 |             lines=lines
443 |         )
444 |     except FileNotFoundError:
445 |         raise HTTPException(status_code=404, detail=f"File not found: {path}")
446 |     except Exception as e:
447 |         logger.error(f"Error reading file: {str(e)}")
448 |         raise HTTPException(status_code=500, detail=f"Failed to read file: {str(e)}")
449 | 
450 | 
451 | if __name__ == "__main__":
452 |     import uvicorn
453 |     import multiprocessing
454 |     
455 |     # Fix for Windows multiprocessing issue
456 |     multiprocessing.freeze_support()
457 |     
458 |     uvicorn.run(
459 |         app,  # Pass app object directly instead of string to avoid reimport issues
460 |         host=settings.api_host,
461 |         port=settings.api_port,
462 |         reload=False,  # Disable reload on Windows to prevent multiprocessing issues
463 |         log_level=settings.log_level.lower()
464 |     )
465 | 
466 | # Made with Bob
</content>
</file>
<file><path>frontend/src/App.jsx</path>
<content lines="1-370">
  1 | /**
  2 |  * Main application component with modern, beautiful design
  3 |  */
  4 | 
  5 | import React from 'react';
  6 | import {
  7 |   Container,
  8 |   Box,
  9 |   Typography,
 10 |   AppBar,
 11 |   Toolbar,
 12 |   Alert,
 13 |   CssBaseline,
 14 |   ThemeProvider,
 15 |   createTheme,
 16 |   Paper,
 17 |   Chip,
 18 |   Stack,
 19 |   Button,
 20 |   IconButton,
 21 |   Tooltip,
 22 | } from '@mui/material';
 23 | import {
 24 |   Code as CodeIcon,
 25 |   AutoAwesome as AIIcon,
 26 |   GitHub as GitHubIcon,
 27 |   Speed as SpeedIcon,
 28 |   Home as HomeIcon,
 29 |   Refresh as RefreshIcon,
 30 | } from '@mui/icons-material';
 31 | import { AppProvider, useApp } from './context/AppContext';
 32 | import RepositoryInput from './components/RepositoryInput';
 33 | import OnboardingGuide from './components/OnboardingGuide';
 34 | import ChatInterface from './components/ChatInterface';
 35 | import LoadingSpinner from './components/LoadingSpinner';
 36 | 
 37 | // Create beautiful Material-UI theme
 38 | const theme = createTheme({
 39 |   palette: {
 40 |     mode: 'light',
 41 |     primary: {
 42 |       main: '#667eea',
 43 |       light: '#8b9cff',
 44 |       dark: '#4c63d2',
 45 |     },
 46 |     secondary: {
 47 |       main: '#764ba2',
 48 |       light: '#9d6cc9',
 49 |       dark: '#5a3a7d',
 50 |     },
 51 |     background: {
 52 |       default: '#f8f9ff',
 53 |       paper: '#ffffff',
 54 |     },
 55 |     text: {
 56 |       primary: '#2d3748',
 57 |       secondary: '#718096',
 58 |     },
 59 |   },
 60 |   typography: {
 61 |     fontFamily: '"Inter", "Roboto", "Helvetica", "Arial", sans-serif',
 62 |     h1: {
 63 |       fontWeight: 800,
 64 |       letterSpacing: '-0.02em',
 65 |     },
 66 |     h3: {
 67 |       fontWeight: 700,
 68 |       letterSpacing: '-0.01em',
 69 |     },
 70 |     h6: {
 71 |       fontWeight: 600,
 72 |     },
 73 |   },
 74 |   shape: {
 75 |     borderRadius: 16,
 76 |   },
 77 |   components: {
 78 |     MuiButton: {
 79 |       styleOverrides: {
 80 |         root: {
 81 |           textTransform: 'none',
 82 |           fontWeight: 600,
 83 |           borderRadius: 12,
 84 |           padding: '10px 24px',
 85 |         },
 86 |       },
 87 |     },
 88 |     MuiPaper: {
 89 |       styleOverrides: {
 90 |         root: {
 91 |           backgroundImage: 'none',
 92 |         },
 93 |       },
 94 |     },
 95 |   },
 96 | });
 97 | 
 98 | const AppContent = () => {
 99 |   const { isAnalyzing, analysisError, sessionId, cancelAnalysis, clearAnalysis } = useApp();
100 | 
101 |   const handleNewAnalysis = () => {
102 |     clearAnalysis();
103 |   };
104 | 
105 |   return (
106 |     <Box sx={{ 
107 |       minHeight: '100vh',
108 |       background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
109 |       position: 'relative',
110 |       overflow: 'hidden',
111 |     }}>
112 |       {/* Animated background elements */}
113 |       <Box sx={{
114 |         position: 'absolute',
115 |         top: 0,
116 |         left: 0,
117 |         right: 0,
118 |         bottom: 0,
119 |         opacity: 0.1,
120 |         background: 'radial-gradient(circle at 20% 50%, rgba(255,255,255,0.3) 0%, transparent 50%), radial-gradient(circle at 80% 80%, rgba(255,255,255,0.3) 0%, transparent 50%)',
121 |         pointerEvents: 'none',
122 |       }} />
123 | 
124 |       {/* App Bar with glass effect */}
125 |       <AppBar 
126 |         position="static" 
127 |         elevation={0}
128 |         sx={{
129 |           background: 'rgba(255, 255, 255, 0.1)',
130 |           backdropFilter: 'blur(10px)',
131 |           borderBottom: '1px solid rgba(255, 255, 255, 0.2)',
132 |         }}
133 |       >
134 |         <Toolbar sx={{ py: 1 }}>
135 |           <Box sx={{
136 |             display: 'flex',
137 |             alignItems: 'center',
138 |             gap: 1,
139 |             background: 'rgba(255, 255, 255, 0.2)',
140 |             px: 2,
141 |             py: 0.5,
142 |             borderRadius: 3,
143 |           }}>
144 |             <CodeIcon sx={{ fontSize: 28 }} />
145 |             <Typography variant="h6" component="div" sx={{ fontWeight: 700 }}>
146 |               DevPilot
147 |             </Typography>
148 |           </Box>
149 |           <Box sx={{ flexGrow: 1 }} />
150 |           
151 |           {/* New Analysis Button - only show when there's a session */}
152 |           {sessionId && !isAnalyzing && (
153 |             <Tooltip title="Go to Home">
154 |               <Button
155 |                 variant="contained"
156 |                 startIcon={<RefreshIcon />}
157 |                 onClick={handleNewAnalysis}
158 |                 sx={{
159 |                   mr: 2,
160 |                   background: 'rgba(255, 255, 255, 0.25)',
161 |                   color: 'white',
162 |                   fontWeight: 600,
163 |                   backdropFilter: 'blur(10px)',
164 |                   border: '1px solid rgba(255, 255, 255, 0.3)',
165 |                   '&:hover': {
166 |                     background: 'rgba(255, 255, 255, 0.35)',
167 |                     transform: 'translateY(-2px)',
168 |                     boxShadow: '0 4px 20px rgba(0,0,0,0.2)',
169 |                   },
170 |                   transition: 'all 0.3s ease',
171 |                 }}
172 |               >
173 |                 Home
174 |               </Button>
175 |             </Tooltip>
176 |           )}
177 |           
178 |           <Chip
179 |             icon={<AIIcon />}
180 |             label="Powered by IBM watsonx.ai"
181 |             sx={{
182 |               background: 'rgba(255, 255, 255, 0.2)',
183 |               color: 'white',
184 |               fontWeight: 600,
185 |               '& .MuiChip-icon': { color: 'white' },
186 |             }}
187 |           />
188 |         </Toolbar>
189 |       </AppBar>
190 | 
191 |       {/* Main Content */}
192 |       <Container maxWidth="lg" sx={{ py: 6, position: 'relative', zIndex: 1 }}>
193 |         {/* Hero Section */}
194 |         {!sessionId && !isAnalyzing && (
195 |           <Box sx={{ textAlign: 'center', mb: 6, animation: 'fadeIn 0.8s ease-out' }}>
196 |             <Box sx={{ mb: 3 }}>
197 |               <Typography 
198 |                 variant="h1" 
199 |                 component="h1" 
200 |                 sx={{ 
201 |                   fontSize: { xs: '2.5rem', md: '4rem' },
202 |                   color: 'white',
203 |                   mb: 2,
204 |                   textShadow: '0 2px 20px rgba(0,0,0,0.2)',
205 |                 }}
206 |               >
207 |                 Intelligent Developer
208 |                 <br />
209 |                 <span className="gradient-text" style={{ 
210 |                   background: 'linear-gradient(135deg, #fff 0%, #f0f0ff 100%)',
211 |                   WebkitBackgroundClip: 'text',
212 |                   WebkitTextFillColor: 'transparent',
213 |                 }}>
214 |                   Onboarding
215 |                 </span>
216 |               </Typography>
217 |               <Typography 
218 |                 variant="h5" 
219 |                 sx={{ 
220 |                   color: 'rgba(255, 255, 255, 0.9)',
221 |                   mb: 4,
222 |                   fontWeight: 400,
223 |                   maxWidth: '700px',
224 |                   mx: 'auto',
225 |                 }}
226 |               >
227 |                 Analyze any GitHub repository and get AI-powered insights in minutes
228 |               </Typography>
229 |             </Box>
230 | 
231 |             {/* Feature Cards */}
232 |             <Stack 
233 |               direction={{ xs: 'column', md: 'row' }} 
234 |               spacing={3} 
235 |               sx={{ mb: 5, justifyContent: 'center' }}
236 |             >
237 |               {[
238 |                 { icon: <GitHubIcon />, title: 'GitHub Integration', desc: 'Clone any public repository' },
239 |                 { icon: <AIIcon />, title: 'AI Analysis', desc: 'Powered by Granite models' },
240 |                 { icon: <SpeedIcon />, title: 'Fast Results', desc: 'Get insights in 1-2 minutes' },
241 |               ].map((feature, index) => (
242 |                 <Paper
243 |                   key={index}
244 |                   elevation={0}
245 |                   className="glass hover-lift"
246 |                   sx={{
247 |                     p: 3,
248 |                     textAlign: 'center',
249 |                     minWidth: { xs: '100%', md: '200px' },
250 |                     animation: `slideIn 0.6s ease-out ${index * 0.1}s both`,
251 |                   }}
252 |                 >
253 |                   <Box sx={{ 
254 |                     color: 'primary.main', 
255 |                     mb: 1,
256 |                     '& svg': { fontSize: 40 },
257 |                   }}>
258 |                     {feature.icon}
259 |                   </Box>
260 |                   <Typography variant="h6" gutterBottom sx={{ fontWeight: 700 }}>
261 |                     {feature.title}
262 |                   </Typography>
263 |                   <Typography variant="body2" color="text.secondary">
264 |                     {feature.desc}
265 |                   </Typography>
266 |                 </Paper>
267 |               ))}
268 |             </Stack>
269 |           </Box>
270 |         )}
271 | 
272 |         {/* Repository Input Card */}
273 |         <Paper 
274 |           elevation={0}
275 |           className="glass"
276 |           sx={{ 
277 |             p: 4, 
278 |             mb: 4,
279 |             animation: 'fadeIn 0.6s ease-out',
280 |           }}
281 |         >
282 |           <RepositoryInput />
283 |         </Paper>
284 | 
285 |         {/* Analysis Error */}
286 |         {analysisError && (
287 |           <Alert 
288 |             severity="error" 
289 |             sx={{ 
290 |               mb: 3,
291 |               borderRadius: 3,
292 |               animation: 'slideIn 0.4s ease-out',
293 |             }}
294 |           >
295 |             {analysisError}
296 |           </Alert>
297 |         )}
298 | 
299 |         {/* Loading State */}
300 |         {isAnalyzing && (
301 |           <Paper 
302 |             elevation={0}
303 |             className="glass"
304 |             sx={{ 
305 |               p: 6, 
306 |               textAlign: 'center',
307 |               animation: 'fadeIn 0.4s ease-out',
308 |             }}
309 |           >
310 |             <LoadingSpinner
311 |               message="Analyzing repository... This may take 1-2 minutes."
312 |               size={60}
313 |               onCancel={cancelAnalysis}
314 |             />
315 |           </Paper>
316 |         )}
317 | 
318 |         {/* Results Section */}
319 |         {!isAnalyzing && sessionId && (
320 |           <Box sx={{ animation: 'fadeIn 0.6s ease-out' }}>
321 |             <OnboardingGuide />
322 |             <Box sx={{ mt: 4 }}>
323 |               <ChatInterface />
324 |             </Box>
325 |           </Box>
326 |         )}
327 | 
328 |         {/* Footer */}
329 |         {!sessionId && !isAnalyzing && (
330 |           <Box sx={{ textAlign: 'center', mt: 8, py: 4 }}>
331 |             <Typography 
332 |               variant="body1" 
333 |               sx={{ 
334 |                 color: 'rgba(255, 255, 255, 0.9)',
335 |                 mb: 2,
336 |                 fontWeight: 500,
337 |               }}
338 |             >
339 |               🚀 Enter a GitHub repository URL above to get started
340 |             </Typography>
341 |             <Typography 
342 |               variant="caption" 
343 |               sx={{ 
344 |                 color: 'rgba(255, 255, 255, 0.7)',
345 |                 display: 'block',
346 |               }}
347 |             >
348 |               Built for IBM Hackathon • Powered by watsonx.ai Granite Models
349 |             </Typography>
350 |           </Box>
351 |         )}
352 |       </Container>
353 |     </Box>
354 |   );
355 | };
356 | 
357 | function App() {
358 |   return (
359 |     <ThemeProvider theme={theme}>
360 |       <CssBaseline />
361 |       <AppProvider>
362 |         <AppContent />
363 |       </AppProvider>
364 |     </ThemeProvider>
365 |   );
366 | }
367 | 
368 | export default App;
369 | 
370 | // Made with Bob
</content>
</file>
</files>
<environment_details>
# VSCode Visible Files
requirements.txt

# VSCode Open Tabs
streamlit_app.py,.gitignore,.streamlit/config.toml,STREAMLIT_README.md,backend/models.py,backend/analyzer.py,frontend/src/components/MermaidDiagram.jsx,frontend/src/components/OnboardingGuide.jsx,backend/watsonx_client.py,frontend/index.html,frontend/src/App.jsx,backend/api.py,README.md,frontend/package.json,requirements.txt,run_demo.bat,run_demo.sh,DEMO_GUIDE.md

# Current Time
Current time in ISO 8601 UTC format: 2026-05-16T19:29:09.402Z
User time zone: Europe/Madrid, UTC+2:00

# Current Cost
$0.02

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

Based on my analysis of the project, here are the requested descriptions and tags:

<attempt_completion>
<result>
## Short Description (255 characters max)
AI-powered developer onboarding assistant that analyzes GitHub repositories using IBM watsonx.ai Granite models, generating comprehensive guides and providing interactive chat for faster codebase understanding.

## Long Description (100+ words)
**DevPilot** revolutionizes developer onboarding by leveraging IBM watsonx.ai Granite models to automatically analyze GitHub repositories and generate comprehensive onboarding documentation. 

**The Problem:** New developers spend days or weeks understanding unfamiliar codebases, slowing productivity and increasing onboarding costs.

**Our Solution:** DevPilot clones any public GitHub repository, performs deep AI-powered analysis, and generates structured onboarding guides covering project overview, technology stack, architecture insights, setup instructions, and key files. An interactive chat interface powered by Granite models allows developers to ask questions and get context-aware answers with code references.

**Target Audience:** Software development teams, open-source contributors, educators, and individual developers exploring new projects.

**Unique Features:**
- 🧠 IBM watsonx.ai Granite model integration for intelligent code understanding
- 📖 Auto-generated comprehensive onboarding guides in minutes
- 💬 Context-aware chat with file-specific references
- 🎨 Beautiful UI with IBM Carbon Design inspiration
- ⚡ Smart caching for repeated analyses
- 🚀 Production-ready architecture with FastAPI backend and React frontend

**Benefits:** Reduces onboarding time from days to minutes, ensures consistent documentation, improves knowledge sharing, and accelerates developer productivity.

## Technology & Category Tags

**Primary Categories:**
- Artificial Intelligence / Machine Learning
- Developer Tools
- Code Analysis
- Documentation Generation

**Technology Tags:**
- IBM watsonx.ai
- IBM Granite Models
- FastAPI
- React
- Python
- JavaScript
- Natural Language Processing
- Code Intelligence
- GitHub Integration
- Streamlit
- Material-UI
- REST API

**Use Case Tags:**
- Developer Onboarding
- Code Understanding
- Knowledge Management
- Team Productivity
- Open Source
- Education
- Software Architecture
- Documentation Automation

**IBM-Specific Tags:**
- IBM Cloud Ready
- IBM Carbon Design
- watsonx.ai Integration
- Granite Code Models
- IBM Hackathon 2026
</result>
</attempt_completion>

