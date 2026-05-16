# DevOnboard AI - Deployment Guide

This guide covers multiple deployment options to get a public URL for your application.

## 🚀 Quick Deployment Options

### Option 1: IBM Cloud (Recommended for Hackathon)
### Option 2: Vercel (Frontend) + Railway/Render (Backend)
### Option 3: Docker + Any Cloud Provider

---

## Option 1: IBM Cloud Deployment

### Prerequisites
- IBM Cloud account
- IBM Cloud CLI installed
- watsonx.ai project with API key
- (Optional) Cloudant service instance

### Step 1: Install IBM Cloud CLI

```bash
# macOS
curl -fsSL https://clis.cloud.ibm.com/install/osx | sh

# Windows
# Download from: https://github.com/IBM-Cloud/ibm-cloud-cli-release/releases/

# Linux
curl -fsSL https://clis.cloud.ibm.com/install/linux | sh
```

### Step 2: Login to IBM Cloud

```bash
ibmcloud login
ibmcloud target --cf
```

### Step 3: Create Services (Optional)

```bash
# Create Cloudant instance
ibmcloud resource service-instance-create devonboard-cloudant \
  cloudantnosqldb lite us-south

# Create service key
ibmcloud resource service-key-create devonboard-cloudant-key \
  Manager --instance-name devonboard-cloudant
```

### Step 4: Set Environment Variables

```bash
# Set environment variables for Cloud Foundry
ibmcloud cf set-env devonboard-ai-backend WATSONX_API_KEY "your_api_key"
ibmcloud cf set-env devonboard-ai-backend WATSONX_PROJECT_ID "your_project_id"
ibmcloud cf set-env devonboard-ai-backend WATSONX_URL "https://us-south.ml.cloud.ibm.com"
```

### Step 5: Deploy Backend

```bash
# From project root
ibmcloud cf push devonboard-ai-backend -f manifest.yml
```

Your backend will be available at:
`https://devonboard-ai-backend.mybluemix.net`

### Step 6: Deploy Frontend

Update `frontend/.env` with your backend URL:
```env
VITE_API_URL=https://devonboard-ai-backend.mybluemix.net
```

Build and deploy:
```bash
cd frontend
npm run build

# Deploy static files to IBM Cloud Object Storage or Cloud Foundry
ibmcloud cf push devonboard-ai-frontend -p dist
```

---

## Option 2: Vercel + Railway (Easiest)

### Backend on Railway

1. **Go to [Railway.app](https://railway.app)**
2. **Click "New Project" → "Deploy from GitHub"**
3. **Select your repository**
4. **Configure**:
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn api:app --host 0.0.0.0 --port $PORT`
5. **Add Environment Variables**:
   ```
   WATSONX_API_KEY=your_key
   WATSONX_PROJECT_ID=your_project_id
   WATSONX_URL=https://us-south.ml.cloud.ibm.com
   REPO_CLONE_DIR=/tmp/repos
   ```
6. **Deploy** - You'll get a URL like: `https://your-app.railway.app`

### Frontend on Vercel

1. **Go to [Vercel.com](https://vercel.com)**
2. **Click "New Project" → Import from Git**
3. **Select your repository**
4. **Configure**:
   - Framework Preset: Vite
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `dist`
5. **Add Environment Variable**:
   ```
   VITE_API_URL=https://your-app.railway.app
   ```
6. **Deploy** - You'll get a URL like: `https://your-app.vercel.app`

---

## Option 3: Render (All-in-One)

### Backend on Render

1. **Go to [Render.com](https://render.com)**
2. **New → Web Service**
3. **Connect your repository**
4. **Configure**:
   - Name: `devonboard-ai-backend`
   - Root Directory: `backend`
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn api:app --host 0.0.0.0 --port $PORT`
5. **Add Environment Variables** (same as Railway)
6. **Create Web Service**

### Frontend on Render

1. **New → Static Site**
2. **Connect your repository**
3. **Configure**:
   - Name: `devonboard-ai-frontend`
   - Root Directory: `frontend`
   - Build Command: `npm install && npm run build`
   - Publish Directory: `dist`
4. **Add Environment Variable**:
   ```
   VITE_API_URL=https://devonboard-ai-backend.onrender.com
   ```
5. **Create Static Site**

---

## Option 4: Docker Deployment

### Build Docker Images

```bash
# Backend
docker build -t devonboard-backend -f Dockerfile.backend .

# Frontend
docker build -t devonboard-frontend -f Dockerfile.frontend .
```

### Deploy to Any Cloud

- **AWS ECS/Fargate**
- **Google Cloud Run**
- **Azure Container Instances**
- **DigitalOcean App Platform**

---

## 🔧 Configuration for Production

### Backend Environment Variables

```bash
WATSONX_API_KEY=your_api_key
WATSONX_PROJECT_ID=your_project_id
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-13b-chat-v2

# Optional Cloudant
CLOUDANT_URL=https://your-instance.cloudantnosqldb.appdomain.cloud
CLOUDANT_API_KEY=your_cloudant_key
CLOUDANT_DATABASE=devonboard_cache

# Application
REPO_CLONE_DIR=/tmp/repos
MAX_REPO_SIZE_MB=500
CACHE_TTL_DAYS=7
API_HOST=0.0.0.0
API_PORT=8000
CORS_ORIGINS=https://your-frontend-url.com
LOG_LEVEL=INFO
```

### Frontend Environment Variables

```bash
VITE_API_URL=https://your-backend-url.com
VITE_APP_NAME=DevOnboard AI
```

---

## 🎯 Recommended for Hackathon Demo

**Fastest Option**: Railway (Backend) + Vercel (Frontend)

**Why?**
- ✅ Free tier available
- ✅ Automatic HTTPS
- ✅ Deploy in 5 minutes
- ✅ No credit card required
- ✅ GitHub integration
- ✅ Automatic deployments on push

**Steps**:
1. Push code to GitHub
2. Deploy backend to Railway (5 min)
3. Deploy frontend to Vercel (3 min)
4. Share public URLs in demo

**Your Public URLs**:
- Frontend: `https://devonboard-ai.vercel.app`
- Backend: `https://devonboard-ai.railway.app`
- API Docs: `https://devonboard-ai.railway.app/docs`

---

## 🐛 Troubleshooting

### CORS Errors
Update `CORS_ORIGINS` in backend to include your frontend URL:
```bash
CORS_ORIGINS=https://your-frontend.vercel.app,http://localhost:5173
```

### Build Failures
- Check Node.js version (use 18+)
- Check Python version (use 3.11+)
- Verify all dependencies in package.json/requirements.txt

### API Connection Issues
- Verify `VITE_API_URL` in frontend matches backend URL
- Check backend logs for errors
- Test backend health endpoint: `https://your-backend/health`

### Repository Cloning Issues
- Ensure `REPO_CLONE_DIR` has write permissions
- For Railway/Render, use `/tmp/repos`
- Check repository size limits

---

## 📊 Monitoring

### Check Backend Health
```bash
curl https://your-backend-url.com/health
```

### View Logs
- **Railway**: Dashboard → Logs tab
- **Vercel**: Dashboard → Deployments → View Logs
- **Render**: Dashboard → Logs tab
- **IBM Cloud**: `ibmcloud cf logs devonboard-ai-backend`

---

## 🔒 Security Checklist

- [ ] Environment variables set (not in code)
- [ ] CORS configured for production domains
- [ ] API keys secured
- [ ] HTTPS enabled (automatic on most platforms)
- [ ] Rate limiting configured
- [ ] Input validation enabled

---

## 📈 Scaling

### If You Get Traffic

1. **Backend**: Increase instances/memory
2. **Add Cloudant**: Replace in-memory cache
3. **Add CDN**: For frontend static assets
4. **Add Redis**: For session management
5. **Load Balancer**: For multiple backend instances

---

## 💰 Cost Estimates

### Free Tier (Hackathon Demo)
- Railway: 500 hours/month free
- Vercel: Unlimited deployments
- Render: 750 hours/month free
- **Total**: $0/month

### Production (After Hackathon)
- Railway: ~$5-10/month
- Vercel: Free for personal projects
- IBM Cloud: Pay-as-you-go
- **Total**: ~$5-20/month

---

## 🎬 Quick Deploy Script

Save as `deploy.sh`:

```bash
#!/bin/bash

echo "🚀 Deploying DevOnboard AI..."

# Build frontend
cd frontend
npm install
npm run build
echo "✅ Frontend built"

# Deploy to Vercel
vercel --prod
echo "✅ Frontend deployed"

# Deploy backend to Railway
cd ../backend
railway up
echo "✅ Backend deployed"

echo "🎉 Deployment complete!"
echo "Frontend: Check Vercel dashboard"
echo "Backend: Check Railway dashboard"
```

---

**Need Help?** Check the platform-specific documentation:
- [Railway Docs](https://docs.railway.app/)
- [Vercel Docs](https://vercel.com/docs)
- [Render Docs](https://render.com/docs)
- [IBM Cloud Docs](https://cloud.ibm.com/docs)