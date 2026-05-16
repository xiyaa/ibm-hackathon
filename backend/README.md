# DevOnboard AI Backend

## Quick Start

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Edit `.env` and add your IBM watsonx.ai credentials:

```env
WATSONX_API_KEY=your_api_key_here
WATSONX_PROJECT_ID=your_project_id
WATSONX_URL=https://us-south.ml.cloud.ibm.com
```

### 3. Run the Backend

**Option 1: Using Python directly**
```bash
python api.py
```

**Option 2: Using uvicorn (recommended)**
```bash
uvicorn api:app --reload --host 127.0.0.1 --port 8000
```

### 4. Access the API

- **API Documentation (Swagger UI)**: http://localhost:8000/docs
- **Alternative Documentation (ReDoc)**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## API Endpoints

### Repository Analysis
- `POST /api/analyze` - Analyze a GitHub repository
  ```json
  {
    "repo_url": "https://github.com/username/repo",
    "branch": "main",
    "force_refresh": false
  }
  ```

### Chat
- `POST /api/chat` - Ask questions about the codebase
- `GET /api/chat/history/{session_id}` - Get chat history

### Files
- `GET /api/files/{session_id}` - Get repository file tree
- `GET /api/files/{session_id}/content?path=file.py` - Get file content

## Troubleshooting

### Cannot access http://0.0.0.0:8000

Use `http://localhost:8000` or `http://127.0.0.1:8000` instead. The `0.0.0.0` address is for binding the server to all network interfaces, but you access it via localhost.

### Import Errors

Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### watsonx.ai Errors

Verify your credentials in the `.env` file:
- `WATSONX_API_KEY` - Your IBM Cloud API key
- `WATSONX_PROJECT_ID` - Your watsonx.ai project ID
- `WATSONX_URL` - The watsonx.ai endpoint URL

### Repository Clone Errors

The backend clones repositories to `/tmp/repos` by default. On Windows, you may want to change this in `.env`:
```env
REPO_CLONE_DIR=C:/temp/repos
```

## Development

### Running with Auto-reload

```bash
uvicorn api:app --reload --host 127.0.0.1 --port 8000
```

The `--reload` flag enables auto-reload on code changes.

### Testing Endpoints

Use the interactive API documentation at http://localhost:8000/docs to test endpoints directly in your browser.

### Logs

The application logs to stdout. Set log level in `.env`:
```env
LOG_LEVEL=INFO  # or DEBUG, WARNING, ERROR
```

## Architecture

See [AGENTS.md](../AGENTS.md) for complete architecture documentation.