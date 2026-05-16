
"""
DevOnboard AI - Streamlit Demo Application
AI-powered developer onboarding assistant using IBM watsonx.ai Granite models.
"""

import streamlit as st
import requests
import json
import time
from typing import Dict, List, Optional, Any
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
API_TIMEOUT = 300  # 5 minutes for analysis

# Page configuration
st.set_page_config(
    page_title="DevOnboard AI - IBM watsonx.ai",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for IBM-inspired dark theme
def apply_custom_css():
    """Apply IBM Carbon Design System inspired dark theme."""
    st.markdown("""
    <style>
    /* IBM Carbon Design System Colors */
    :root {
        --ibm-gray-100: #161616;
        --ibm-gray-90: #262626;
        --ibm-gray-80: #393939;
        --ibm-gray-70: #525252;
        --ibm-gray-10: #f4f4f4;
        --ibm-blue-60: #0f62fe;
        --ibm-blue-70: #0043ce;
        --ibm-purple-60: #8a3ffc;
        --ibm-green-50: #24a148;
    }
    
    /* Main background */
    .stApp {
        background-color: var(--ibm-gray-100);
        color: var(--ibm-gray-10);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: var(--ibm-gray-90);
        border-right: 1px solid var(--ibm-gray-80);
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: var(--ibm-gray-10) !important;
        font-family: 'IBM Plex Sans', sans-serif;
    }
    
    h1 {
        border-bottom: 2px solid var(--ibm-blue-60);
        padding-bottom: 0.5rem;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: var(--ibm-blue-60);
        color: white;
        border: none;
        border-radius: 0;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: background-color 0.2s;
    }
    
    .stButton > button:hover {
        background-color: var(--ibm-blue-70);
    }
    
    /* Input fields */
    .stTextInput > div > div > input {
        background-color: var(--ibm-gray-90);
        color: var(--ibm-gray-10);
        border: 1px solid var(--ibm-gray-70);
        border-radius: 0;
    }
    
    /* Expanders */
    .streamlit-expanderHeader {
        background-color: var(--ibm-gray-90);
        color: var(--ibm-gray-10);
        border-radius: 0;
    }
    
    /* Code blocks */
    .stCodeBlock {
        background-color: var(--ibm-gray-90);
        border: 1px solid var(--ibm-gray-80);
        border-radius: 0;
    }
    
    /* Success/Info/Warning boxes */
    .stSuccess {
        background-color: rgba(36, 161, 72, 0.1);
        border-left: 4px solid var(--ibm-green-50);
    }
    
    .stInfo {
        background-color: rgba(15, 98, 254, 0.1);
        border-left: 4px solid var(--ibm-blue-60);
    }
    
    /* Chat messages */
    .chat-message {
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 4px;
        background-color: var(--ibm-gray-90);
        border-left: 3px solid var(--ibm-blue-60);
    }
    
    .user-message {
        border-left-color: var(--ibm-purple-60);
    }
    
    /* File tree styling */
    .file-tree-item {
        padding: 0.25rem 0.5rem;
        cursor: pointer;
        transition: background-color 0.2s;
    }
    
    .file-tree-item:hover {
        background-color: var(--ibm-gray-80);
    }
    
    /* Progress indicators */
    .progress-step {
        padding: 0.5rem;
        margin: 0.25rem 0;
        background-color: var(--ibm-gray-90);
        border-left: 3px solid var(--ibm-blue-60);
    }
    
    .progress-step.active {
        border-left-color: var(--ibm-green-50);
        animation: pulse 1.5s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    /* Markdown content */
    .markdown-content {
        background-color: var(--ibm-gray-90);
        padding: 1.5rem;
        border-radius: 4px;
        border: 1px solid var(--ibm-gray-80);
    }
    
    /* Links */
    a {
        color: var(--ibm-blue-60);
        text-decoration: none;
    }
    
    a:hover {
        color: var(--ibm-blue-70);
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)


def initialize_session_state():
    """Initialize Streamlit session state variables."""
    if 'session_id' not in st.session_state:
        st.session_state.session_id = None
    if 'repo_url' not in st.session_state:
        st.session_state.repo_url = ""
    if 'analysis_result' not in st.session_state:
        st.session_state.analysis_result = None
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'file_tree' not in st.session_state:
        st.session_state.file_tree = None
    if 'selected_file' not in st.session_state:
        st.session_state.selected_file = None
    if 'analyzing' not in st.session_state:
        st.session_state.analyzing = False


def validate_github_url(url: str) -> bool:
    """Validate GitHub repository URL format."""
    import re
    pattern = r'^https?://github\.com/[\w-]+/[\w.-]+/?$'
    return bool(re.match(pattern, url.rstrip('/')))


def analyze_repository(repo_url: str, branch: str = "main", force_refresh: bool = False) -> Optional[Dict]:
    """
    Call backend API to analyze repository.
    
    Args:
        repo_url: GitHub repository URL
        branch: Branch to analyze
        force_refresh: Force re-analysis
        
    Returns:
        Analysis result or None on error
    """
    try:
        response = requests.post(
            f"{BACKEND_URL}/api/analyze",
            json={
                "repo_url": repo_url,
                "branch": branch,
                "force_refresh": force_refresh
            },
            timeout=API_TIMEOUT
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error analyzing repository: {str(e)}")
        return None


def send_chat_message(session_id: str, message: str, context: Optional[Dict] = None) -> Optional[Dict]:
    """
    Send chat message to backend API.
    
    Args:
        session_id: Session identifier
        message: User message
        context: Optional file context
        
    Returns:
        Chat response or None on error
    """
    try:
        payload = {
            "session_id": session_id,
            "message": message
        }
        if context:
            payload["context"] = context
            
        response = requests.post(
            f"{BACKEND_URL}/api/chat",
            json=payload,
            timeout=60
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error sending message: {str(e)}")
        return None


def get_file_tree(session_id: str) -> Optional[Dict]:
    """Get file tree for analyzed repository."""
    try:
        response = requests.get(
            f"{BACKEND_URL}/api/files/{session_id}",
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error fetching file tree: {str(e)}")
        return None


def render_file_tree(node: Dict, indent: int = 0):
    """Recursively render file tree structure."""
    icon = "📁" if node["type"] == "directory" else "📄"
    name = node["name"]
    
    # Add language badge for files
    language_badge = ""
    if node["type"] == "file" and node.get("language"):
        language_badge = f" `{node['language']}`"
    
    # Render node
    st.markdown(f"{'&nbsp;' * (indent * 4)}{icon} **{name}**{language_badge}")
    
    # Render children
    if node.get("children"):
        for child in node["children"]:
            render_file_tree(child, indent + 1)


def render_sidebar():
    """Render sidebar with input and file tree."""
    with st.sidebar:
        # Header with branding
        st.markdown("# 🚀 DevOnboard AI")
        st.markdown("*Powered by IBM watsonx.ai Granite*")
        st.markdown("---")
        
        # GitHub URL input
        st.markdown("### 📦 Repository Analysis")
        repo_url = st.text_input(
            "GitHub Repository URL",
            value=st.session_state.repo_url,
            placeholder="https://github.com/owner/repo",
            help="Enter a public GitHub repository URL"
        )
        
        col1, col2 = st.columns([2, 1])
        with col1:
            branch = st.text_input("Branch", value="main", help="Branch to analyze")
        with col2:
            force_refresh = st.checkbox("Force", help="Force re-analysis")
        
        analyze_button = st.button("🔍 Analyze Repository", use_container_width=True)
        
        # Handle analysis
        if analyze_button:
            if not repo_url:
                st.error("❌ Please enter a repository URL")
            elif not validate_github_url(repo_url):
                st.error("❌ Invalid GitHub URL format")
            else:
                st.session_state.repo_url = repo_url
                st.session_state.analyzing = True
                st.rerun()
        
        # Show file tree if available
        if st.session_state.file_tree:
            st.markdown("---")
            st.markdown("### 📁 Repository Structure")
            with st.expander("File Tree", expanded=True):
                render_file_tree(st.session_state.file_tree)
        
        # Footer
        st.markdown("---")
        st.markdown("""
        <div style='text-align: center; font-size: 0.8rem; color: #8d8d8d;'>
        Built for IBM Hackathon 2026<br>
        Using IBM watsonx.ai Granite Models
        </div>
        """, unsafe_allow_html=True)


def render_analysis_progress():
    """Render analysis progress indicator."""
    st.markdown("### ⏳ Analyzing Repository...")
    
    progress_steps = [
        ("⏳", "Cloning repository", "Fetching from GitHub..."),
        ("🔍", "Analyzing code structure", "Building file tree and identifying key files..."),
        ("🧠", "Generating AI insights", "Powered by IBM watsonx.ai Granite..."),
        ("✅", "Analysis complete", "Ready to explore!")
    ]
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i, (icon, title, description) in enumerate(progress_steps):
        progress = (i + 1) / len(progress_steps)
        progress_bar.progress(progress)
        status_text.markdown(f"""
        <div class='progress-step active'>
        {icon} <strong>{title}</strong><br>
        <small>{description}</small>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.5)  # Simulate progress
    
    # Perform actual analysis
    result = analyze_repository(
        st.session_state.repo_url,
        branch="main",
        force_refresh=False
    )
    
    if result:
        st.session_state.session_id = result["session_id"]
        st.session_state.analysis_result = result
        
        # Fetch file tree
        file_tree_response = get_file_tree(result["session_id"])
        if file_tree_response:
            st.session_state.file_tree = file_tree_response["file_tree"]
        
        st.session_state.analyzing = False
        st.success("✅ Analysis complete!")
        time.sleep(1)
        st.rerun()
    else:
        st.session_state.analyzing = False
        st.error("❌ Analysis failed. Please try again.")


def render_onboarding_guide():
    """Render the AI-generated onboarding guide."""
    if not st.session_state.analysis_result:
        return
    
    result = st.session_state.analysis_result
    analysis = result["analysis"]
    repo_info = result["repository"]
    
    # Header
    st.markdown(f"# 📖 {repo_info['name']}")
    st.markdown(f"**Owner:** {repo_info['owner']} | **Branch:** {repo_info['branch']}")
    
    if result.get("cached"):
        st.info("ℹ️ Showing cached analysis results")
    
    st.markdown("---")
    
    # Overview
    with st.expander("📖 Project Overview", expanded=True):
        st.markdown(f"<div class='markdown-content'>{analysis['overview']}</div>", unsafe_allow_html=True)
    
    # Tech Stack
    with st.expander("🛠️ Technology Stack", expanded=True):
        cols = st.columns(4)
        for i, tech in enumerate(analysis['tech_stack']):
            with cols[i % 4]:
                st.markdown(f"- `{tech}`")
    
    # Architecture Insights
    with st.expander("🏗️ Architecture Insights", expanded=False):
        st.markdown(f"<div class='markdown-content'>{analysis['architecture_insights']}</div>", unsafe_allow_html=True)
    
    # Setup Instructions
    with st.expander("📦 Setup Instructions", expanded=False):
        st.markdown(f"<div class='markdown-content'>{analysis['setup_instructions']}</div>", unsafe_allow_html=True)
    
    # Key Files
    with st.expander("📁 Key Files", expanded=False):
        for key_file in analysis['key_files']:
            st.markdown(f"**{key_file['path']}** ({key_file['type']})")
            if key_file.get('snippet'):
                st.code(key_file['snippet'][:500], language=key_file.get('language', ''))
            st.markdown("---")


def render_chat_interface():
    """Render chat interface for Q&A."""
    if not st.session_state.session_id:
        return
    
    st.markdown("---")
    st.markdown("## 💬 Ask Questions About the Codebase")
    
    # Chat history
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.chat_history:
            role = msg["role"]
            content = msg["content"]
            
            if role == "user":
                st.markdown(f"""
                <div class='chat-message user-message'>
                <strong>You:</strong><br>{content}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class='chat-message'>
                <strong>AI Assistant:</strong><br>{content}
                </div>
                """, unsafe_allow_html=True)
    
    # Chat input
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_area(
            "Your question",
            placeholder="e.g., How does authentication work in this project?",
            height=100
        )
        submit_button = st.form_submit_button("Send 💬")
        
        if submit_button and user_input:
            # Add user message to history
            st.session_state.chat_history.append({
                "role": "user",
                "content": user_input
            })
            
            # Get AI response
            response = send_chat_message(st.session_state.session_id, user_input)
            
            if response:
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": response["response"]
                })
            
            st.rerun()


def main():
    """Main application entry point."""
    # Apply styling
    apply_custom_css()
    
    # Initialize session state
    initialize_session_state()
    
    # Render sidebar
    render_sidebar()
    
    # Main content area
    if st.session_state.analyzing:
        render_analysis_progress()
    elif st.session_state.analysis_result:
        # Show onboarding guide and chat
        render_onboarding_guide()
        render_chat_interface()
    else:
        # Welcome screen
        st.markdown("# 🚀 Welcome to DevOnboard AI")
        st.markdown("""
        ### AI-Powered Developer Onboarding Assistant
        
        DevOnboard AI helps developers quickly understand new codebases using 
        **IBM watsonx.ai Granite models** for intelligent code analysis.
        
        #### How it works:
        1. 📦 Enter a GitHub repository URL in the sidebar
        2. 🔍 Click "Analyze Repository" to start the analysis
        3. 📖 Explore the AI-generated onboarding guide
        4. 💬 Ask questions about the codebase in the chat interface
        
        #### Features:
        - 🧠 AI-powered code analysis using IBM watsonx.ai Granite
        - 📊 Comprehensive onboarding guides
        - 🗂️ Interactive file tree browser
        - 💬 Context-aware Q&A chat interface
        - ⚡ Fast analysis with intelligent caching
        
        ---
        
        **Get started by entering a GitHub repository URL in the sidebar!**
        """)
        
        # Example repositories
        st.markdown("### 📚 Try these example repositories:")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("FastAPI", use_container_width=True):
                st.session_state.repo_url = "https://github.com/tiangolo/fastapi"
                st.rerun()
        
        with col2:
            if st.button("React", use_container_width=True):
                st.session_state.repo_url = "https://github.com/facebook/react"
                st.rerun()
        
        with col3:
            if st.button("Flask", use_container_width=True):
                st.session_state.repo_url = "https://github.com/pallets/flask"
                st.rerun()


if __name__ == "__main__":
    main()