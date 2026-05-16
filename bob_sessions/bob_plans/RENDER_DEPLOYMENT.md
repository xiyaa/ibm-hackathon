# 🚀 Deploy DevPilot to Render - Step by Step

Complete guide to deploy your application to Render and get public URLs.

## 📋 Prerequisites

- GitHub account with your code pushed
- Render account (free) - Sign up at [render.com](https://render.com)
- IBM watsonx.ai API key and Project ID

## 🌿 Branch Configuration

**Yes! You can deploy from any branch, not just `main`.**

When configuring your service in Render, you can specify which branch to deploy from:

### For Backend:
- In the **"Branch"** field (Step 2 of backend configuration), enter your branch name
- Example: `develop`, `staging`, `feature/new-ui`, etc.

### For Frontend:
- In the **"Branch"** field (Step 2 of frontend configuration), enter the same or different branch
- You can deploy frontend and backend from different branches if needed

### Automatic Deployments:
- Render will automatically redeploy when you push to the selected branch
- To change branches later: Dashboard → Service → Settings → Branch

### Example Workflow:
```bash
# Create and push to a test branch
git checkout -b test-deployment
git add .
git commit -m "Test deployment"
git push origin test-deployment

# Then in Render, set Branch to: test-deployment
```

---

## 🎯 Quick Deploy (10 Minutes)

### Step 1: Push Code to GitHub

```bash
# If not already done
git add .
git commit -m "Ready for Render deployment"
git push origin main
```

### Step 2: Sign Up for Render

1. Go to **[render.com](https://render.com)**
2. Click **"Get Started"**
3. Sign up with **GitHub** (recommended)
4. Authorize Render to access your repositories


## ⚠️ Important: Python Version & Dependencies

**Before deploying, ensure these files exist in your `backend/` folder:**

### 1. `backend/runtime.txt` (REQUIRED)
This file forces Render to use Python 3.11 (stable version with pre-built wheels):
```
python-3.11.0
```

**Why this is needed:**
- Render defaults to Python 3.14 (too new)
- Python 3.14 doesn't have pre-built wheels for many packages
- This causes Rust compilation errors with Pydantic
- Python 3.11 has all necessary pre-built wheels

### 2. `backend/requirements.txt` (UPDATED)
Uses Pydantic v1 to avoid Rust compilation:
```python
fastapi==0.103.0
uvicorn[standard]==0.23.2
pydantic==1.10.13  # v1 - pure Python, no Rust needed
ibm-watsonx-ai==0.2.6
GitPython==3.1.40
pygments==2.16.1
radon==6.0.1
# ... other dependencies
```

**Why Pydantic v1:**
- Pydantic v2 requires Rust compilation
- Render's free tier has read-only filesystem
- Can't compile Rust extensions
- Pydantic v1 is pure Python and works perfectly

### 3. Verify Files Exist
```bash
# Check if files exist
ls backend/runtime.txt
ls backend/requirements.txt

# If missing, create them:
echo "python-3.11.0" > backend/runtime.txt
```

---

---

## 🔧 Deploy Backend (5 minutes)

### 1. Create New Web Service

1. From Render Dashboard, click **"New +"** → **"Web Service"**
2. Click **"Connect a repository"**
3. Find and select your **`ibm-hackathon`** repository
4. Click **"Connect"**

### 2. Configure Backend Service

Fill in the following settings:

**Basic Settings:**
- **Name**: `devonboard-ai-backend`
- **Region**: Oregon (US West) or closest to you
- **Branch**: `main`
- **Root Directory**: `backend`
- **Runtime**: `Python 3`

**Build & Deploy:**
- **Build Command**: 
  ```bash
  pip install -r requirements.txt
  ```
- **Start Command**: 
  ```bash
  uvicorn api:app --host 0.0.0.0 --port $PORT
  ```

**Instance Type:**
- Select **"Free"** plan

### 3. Add Environment Variables

Click **"Advanced"** → **"Add Environment Variable"**

Add these variables one by one:

```
WATSONX_API_KEY = your_actual_api_key_here
WATSONX_PROJECT_ID = your_actual_project_id_here
WATSONX_URL = https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID = ibm/granite-3-8b-instruct
REPO_CLONE_DIR = /tmp/repos
MAX_REPO_SIZE_MB = 500
CACHE_TTL_DAYS = 7
API_HOST = 0.0.0.0
API_PORT = 10000
LOG_LEVEL = INFO
CORS_ORIGINS = https://devonboard-ai-frontend.onrender.com,http://localhost:5173
```

**Important**: Replace `your_actual_api_key_here` and `your_actual_project_id_here` with your real credentials!

### 4. Create Web Service

1. Click **"Create Web Service"**
2. Wait 3-5 minutes for deployment
3. Your backend will be live at: `https://devonboard-ai-backend.onrender.com`

### 5. Test Backend

Once deployed, test it:
```bash
curl https://devonboard-ai-backend.onrender.com/health
```

You should see:
```json
{"status": "healthy", "timestamp": "..."}
```

---

## 🎨 Deploy Frontend (5 minutes)

### 1. Create New Static Site

1. From Render Dashboard, click **"New +"** → **"Static Site"**
2. Select your **`ibm-hackathon`** repository
3. Click **"Connect"**

### 2. Configure Frontend Service

Fill in the following settings:

**Basic Settings:**
- **Name**: `devonboard-ai-frontend`
- **Branch**: `main`
- **Root Directory**: `frontend`

**Build Settings:**
- **Build Command**: 
  ```bash
  npm install && npm run build
  ```
- **Publish Directory**: 
  ```
  dist
  ```

### 3. Add Environment Variables

Click **"Advanced"** → **"Add Environment Variable"**

Add these variables:

```
VITE_API_URL = https://devonboard-ai-backend.onrender.com
VITE_APP_NAME = DevPilot
```

**Important**: Use your actual backend URL from Step 1!

### 4. Create Static Site

1. Click **"Create Static Site"**
2. Wait 2-3 minutes for deployment
3. Your frontend will be live at: `https://devonboard-ai-frontend.onrender.com`

---

## 🎉 Your Public URLs

After deployment, you'll have:

- **Frontend Application**: `https://devonboard-ai-frontend.onrender.com`
- **Backend API**: `https://devonboard-ai-backend.onrender.com`
- **API Documentation**: `https://devonboard-ai-backend.onrender.com/docs`
- **Health Check**: `https://devonboard-ai-backend.onrender.com/health`

---

## ✅ Verify Deployment

### Test Frontend
1. Open `https://devonboard-ai-frontend.onrender.com`
2. You should see the DevPilot interface
3. Try entering a GitHub URL (e.g., `https://github.com/tiangolo/typer`)

### Test Backend
```bash
# Health check
curl https://devonboard-ai-backend.onrender.com/health

# API docs
open https://devonboard-ai-backend.onrender.com/docs
```

---

## 🔄 Update CORS Settings

After frontend is deployed, update backend CORS:

1. Go to backend service in Render Dashboard
2. Click **"Environment"**
3. Update `CORS_ORIGINS` to include your actual frontend URL:
   ```
   CORS_ORIGINS = https://devonboard-ai-frontend.onrender.com,http://localhost:5173
   ```
4. Click **"Save Changes"**
5. Service will automatically redeploy


### Pydantic Compilation Error (Rust/maturin)

**Issue**: Build fails with error about Rust compilation or `pydantic-core`
```
error: failed to create directory `/usr/local/cargo/registry/cache/...`
Caused by: Read-only file system (os error 30)
💥 maturin failed
```

**Solution**:
1. **Create `backend/runtime.txt`** with content:
   ```
   python-3.11.0
   ```
2. **Update `backend/requirements.txt`** to use Pydantic v1:
   ```
   pydantic==1.10.13
   ```
3. **Update `backend/config.py`** to use Pydantic v1 syntax:
   ```python
   from pydantic import BaseSettings  # Not from pydantic_settings
   
   class Settings(BaseSettings):
       # ... your settings ...
       
       class Config:  # Not model_config
           env_file = ".env"
           case_sensitive = False
   ```
4. **Commit and push changes**:
   ```bash
   git add backend/runtime.txt backend/requirements.txt backend/config.py
   git commit -m "Fix Render deployment - Python 3.11 + Pydantic v1"
   git push
   ```
5. **Redeploy** - Build should now succeed

**Why this happens:**
- Render uses Python 3.14 by default (too new)
- Pydantic v2 requires Rust compilation
- Render's free tier has read-only filesystem
- Can't compile Rust extensions
- Solution: Use Python 3.11 + Pydantic v1 (pure Python)

---

## 🐛 Troubleshooting

### Backend Build Fails

**Issue**: Dependencies not installing

**Solution**:
1. Check `backend/requirements.txt` exists
2. Verify Python version (should be 3.11+)
3. Check build logs in Render Dashboard

### Frontend Build Fails

**Issue**: npm install errors

**Solution**:
1. Check `frontend/package.json` exists
2. Verify Node version (should be 18+)
3. Try locally: `cd frontend && npm install && npm run build`

### CORS Errors

**Issue**: Frontend can't connect to backend

**Solution**:
1. Verify `VITE_API_URL` in frontend matches backend URL
2. Update `CORS_ORIGINS` in backend to include frontend URL
3. Check both services are deployed and running

### API Connection Timeout

**Issue**: Requests taking too long

**Solution**:
1. Free tier services sleep after 15 min of inactivity
2. First request after sleep takes 30-60 seconds
3. Consider upgrading to paid tier for always-on service

### Repository Clone Fails

**Issue**: Can't clone GitHub repos

**Solution**:
1. Check `REPO_CLONE_DIR=/tmp/repos` is set
2. Verify repository URL is valid
3. Check repository size (limit: 500MB)

---

## 📊 Monitor Your Application

### View Logs

**Backend Logs**:
1. Go to backend service in Dashboard
2. Click **"Logs"** tab
3. See real-time logs

**Frontend Logs**:
1. Go to frontend service in Dashboard
2. Click **"Logs"** tab
3. See build and deploy logs

### Check Metrics

1. Click **"Metrics"** tab
2. View:
   - Request count
   - Response times
   - Memory usage
   - CPU usage

---

## 🔄 Automatic Deployments

Render automatically deploys when you push to GitHub:

```bash
# Make changes
git add .
git commit -m "Update feature"
git push origin main

# Render automatically:
# 1. Detects push
# 2. Rebuilds services
# 3. Deploys new version
```

---

## 💰 Free Tier Limits

**What's Included (Free)**:
- ✅ 750 hours/month per service
- ✅ Automatic HTTPS
- ✅ Custom domains
- ✅ Automatic deployments
- ✅ Build minutes included

**Limitations**:
- ⚠️ Services sleep after 15 min inactivity
- ⚠️ 512 MB RAM
- ⚠️ Shared CPU
- ⚠️ 100 GB bandwidth/month

**For Production**: Upgrade to paid tier ($7/month) for:
- Always-on services
- More RAM and CPU
- Priority support

---

## 🎯 Alternative: One-Click Deploy

### Using render.yaml (Blueprint)

I've included a `render.yaml` file in your project. To use it:

1. Go to [render.com/dashboard](https://render.com/dashboard)
2. Click **"New +"** → **"Blueprint"**
3. Connect your repository
4. Render will automatically:
   - Create both services
   - Configure settings
   - Deploy everything

**Note**: You'll still need to add your watsonx.ai credentials manually.

---

## 📝 Post-Deployment Checklist

- [ ] Backend deployed and accessible
- [ ] Frontend deployed and accessible
- [ ] Health endpoint returns 200
- [ ] API docs accessible at `/docs`
- [ ] CORS configured correctly
- [ ] Environment variables set
- [ ] Test repository analysis works
- [ ] Test chat functionality works
- [ ] Share public URLs with team

---

## 🎬 Demo Your Application

**Your Public URLs**:
- Frontend: `https://devonboard-ai-frontend.onrender.com`
- Backend: `https://devonboard-ai-backend.onrender.com`

**Demo Script**:
1. Open frontend URL
2. Enter a GitHub repository (e.g., `https://github.com/tiangolo/typer`)
3. Wait for analysis (1-2 minutes)
4. Show AI-generated onboarding guide
5. Demonstrate chat functionality
6. Highlight code references and syntax highlighting

---

## 🆘 Need Help?

- **Render Docs**: [render.com/docs](https://render.com/docs)
- **Render Community**: [community.render.com](https://community.render.com)
- **Check Logs**: Dashboard → Service → Logs tab
- **Status Page**: [status.render.com](https://status.render.com)

---

## 🚀 Next Steps

1. **Test thoroughly** with different repositories
2. **Share URLs** with your team
3. **Prepare demo** for hackathon
4. **Monitor logs** for any issues
5. **Consider upgrading** if you need always-on service

---

**Congratulations! Your DevPilot is now live! 🎉**

Share your public URL and showcase your AI-powered developer onboarding assistant!