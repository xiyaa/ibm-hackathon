# DevOnboard AI - Frontend

React frontend for the DevOnboard AI developer onboarding assistant.

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ and npm
- Backend API running on http://localhost:8000

### Installation

```bash
cd frontend
npm install
```

### Development

```bash
npm run dev
```

The app will be available at http://localhost:5173

### Build for Production

```bash
npm run build
```

The build output will be in the `dist/` directory.

## 📁 Project Structure

```
frontend/
├── src/
│   ├── components/          # React components
│   │   ├── RepositoryInput.jsx
│   │   ├── OnboardingGuide.jsx
│   │   ├── ChatInterface.jsx
│   │   ├── CodeReference.jsx
│   │   └── LoadingSpinner.jsx
│   ├── context/            # Global state management
│   │   └── AppContext.jsx
│   ├── services/           # API client
│   │   └── api.js
│   ├── App.jsx             # Main app component
│   ├── main.jsx            # Entry point
│   └── index.css           # Global styles
├── public/                 # Static assets
├── index.html             # HTML template
├── vite.config.js         # Vite configuration
└── package.json           # Dependencies
```

## 🎨 Features

### Repository Analysis
- Enter any GitHub repository URL
- Specify branch (default: main)
- Force refresh option to bypass cache
- Real-time analysis progress

### Onboarding Guide
- AI-generated project overview
- Technology stack identification
- Setup instructions
- Architecture insights
- Key files with code snippets
- Dependency information

### Interactive Chat
- Context-aware AI assistant
- Ask questions about the codebase
- Code references in responses
- Markdown formatting with syntax highlighting
- Chat history per session

## 🛠️ Technologies

- **React 18** - UI framework
- **Material-UI (MUI)** - Component library
- **Vite** - Build tool
- **Axios** - HTTP client
- **react-markdown** - Markdown rendering
- **react-syntax-highlighter** - Code syntax highlighting

## 🔧 Configuration

### Environment Variables

Create a `.env` file:

```env
VITE_API_URL=http://localhost:8000
VITE_APP_NAME=DevOnboard AI
```

### API Proxy

The Vite dev server is configured to proxy `/api` requests to the backend:

```javascript
// vite.config.js
server: {
  proxy: {
    '/api': {
      target: 'http://localhost:8000',
      changeOrigin: true,
    }
  }
}
```

## 📝 Usage

1. **Start the backend** (see backend/README.md)
2. **Start the frontend**: `npm run dev`
3. **Open browser**: http://localhost:5173
4. **Enter a GitHub URL** and click "Analyze Repository"
5. **Wait for analysis** (1-2 minutes)
6. **Explore the onboarding guide** and chat with the AI

## 🎯 Component Overview

### RepositoryInput
- GitHub URL input with validation
- Branch selection
- Force refresh checkbox
- Analysis trigger

### OnboardingGuide
- Displays analysis results
- Expandable sections for different aspects
- Markdown rendering with code highlighting
- Tech stack chips
- Key files accordion

### ChatInterface
- Message input with send button
- Chat history display
- User and AI message bubbles
- Code references in responses
- Auto-scroll to latest message

### CodeReference
- File path display
- Line number indicators
- Syntax-highlighted code snippets
- Language detection

### LoadingSpinner
- Animated loading indicator
- Customizable message and size

## 🐛 Troubleshooting

### Cannot connect to backend
- Ensure backend is running on http://localhost:8000
- Check CORS settings in backend
- Verify `.env` file has correct `VITE_API_URL`

### Build errors
```bash
rm -rf node_modules package-lock.json
npm install
```

### Vite port already in use
```bash
npm run dev -- --port 5174
```

## 📚 Learn More

- [React Documentation](https://react.dev/)
- [Material-UI](https://mui.com/)
- [Vite](https://vitejs.dev/)
- [AGENTS.md](../AGENTS.md) - Full architecture documentation