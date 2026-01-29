# 🚀 Render & Vercel Deployment Commands & Steps

Complete guide for deploying backend (Render) and frontend (Vercel)

---

## 📦 PART 1: RENDER (Backend Deployment)

### Step 1: Install Render CLI (Optional - Can use Web UI instead)

```powershell
# Install Render CLI (optional - web UI is easier)
npm install -g render-cli

# Login to Render
render login
```

**⚠️ Note:** You can skip CLI and use the web interface (recommended for beginners)

### Step 2: Create Render Account & Service (Web UI - Recommended)

**No commands needed - just follow these steps:**

1. **Go to:** https://render.com
2. **Sign up** with GitHub
3. **Click:** "New +" → "Web Service"
4. **Connect** your GitHub repository: `accessibility-analyzer`
5. **Configure settings:**

```
Name: accessibility-analyzer-backend
Region: Oregon (US West) or closest to you
Branch: main
Root Directory: backend
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
```

6. **Click:** "Create Web Service"
7. **Wait 5-10 minutes** for deployment
8. **Copy your URL** when done (e.g., `https://xxx.onrender.com`)

### Step 3: Test Backend

```powershell
# Test health endpoint
curl https://YOUR-BACKEND-URL.onrender.com/health

# Or open in browser:
# https://YOUR-BACKEND-URL.onrender.com/health
```

**Expected response:** `{"status":"healthy"}`

---

## 🎨 PART 2: VERCEL (Frontend Deployment)

### Option A: Using Vercel CLI (Command Line)

#### Step 1: Install Vercel CLI

```powershell
# Install Vercel CLI globally
npm install -g vercel

# Login to Vercel
vercel login
```

#### Step 2: Navigate to Frontend Directory

```powershell
cd "c:\Users\jay likhar\OneDrive\Desktop\Accessibility Analyzer\frontend"
```

#### Step 3: Deploy to Vercel

```powershell
# First deployment (will ask questions)
vercel

# Follow prompts:
# - Set up and deploy? Yes
# - Which scope? Your account
# - Link to existing project? No (first time)
# - Project name? accessibility-analyzer (or press Enter)
# - Directory? ./ (current directory)
# - Override settings? No

# Set environment variable
vercel env add VITE_API_URL

# When prompted, enter your Render backend URL:
# https://YOUR-BACKEND-URL.onrender.com

# Deploy to production
vercel --prod
```

#### Step 4: Update Environment Variable (if needed)

```powershell
# Add/update environment variable
vercel env add VITE_API_URL production

# Or edit existing
vercel env ls
vercel env rm VITE_API_URL production
vercel env add VITE_API_URL production
```

### Option B: Using Vercel Web UI (Recommended - Easier)

**No commands needed - just follow these steps:**

1. **Go to:** https://vercel.com
2. **Sign up** with GitHub
3. **Click:** "Add New..." → "Project"
4. **Import** repository: `accessibility-analyzer`
5. **Configure settings:**

```
Framework Preset: Vite (auto-detected)
Root Directory: frontend
Build Command: npm run build (auto)
Output Directory: dist (auto)
Install Command: npm install (auto)
```

6. **Add Environment Variable:**
   - Click "Environment Variables"
   - Add new:
     - **Key:** `VITE_API_URL`
     - **Value:** `https://YOUR-BACKEND-URL.onrender.com`
     - **Environment:** Production, Preview, Development (select all)

7. **Click:** "Deploy"
8. **Wait 2-3 minutes**
9. **Copy your URL** when done (e.g., `https://xxx.vercel.app`)

---

## 🔄 UPDATE DEPLOYMENTS (After Code Changes)

### Render (Backend) - Auto Deploys

```powershell
# Just push to GitHub - Render auto-deploys!
cd "c:\Users\jay likhar\OneDrive\Desktop\Accessibility Analyzer"
git add .
git commit -m "Your commit message"
git push origin main

# Render will automatically detect and deploy
```

### Vercel (Frontend) - Auto Deploys

```powershell
# Just push to GitHub - Vercel auto-deploys!
cd "c:\Users\jay likhar\OneDrive\Desktop\Accessibility Analyzer"
git add .
git commit -m "Your commit message"
git push origin main

# Vercel will automatically detect and deploy
```

**Or using Vercel CLI:**

```powershell
cd "c:\Users\jay likhar\OneDrive\Desktop\Accessibility Analyzer\frontend"
vercel --prod
```

---

## 📋 QUICK REFERENCE COMMANDS

### Git Commands (Push Updates)

```powershell
# Navigate to project
cd "c:\Users\jay likhar\OneDrive\Desktop\Accessibility Analyzer"

# Check status
git status

# Add all changes
git add .

# Commit changes
git commit -m "Update: description of changes"

# Push to GitHub (triggers auto-deploy)
git push origin main
```

### Vercel CLI Commands

```powershell
# Login
vercel login

# Deploy
vercel

# Deploy to production
vercel --prod

# List projects
vercel ls

# View project info
vercel inspect

# View logs
vercel logs

# Remove deployment
vercel remove

# Environment variables
vercel env add VARIABLE_NAME
vercel env ls
vercel env rm VARIABLE_NAME
```

### Render CLI Commands (if using CLI)

```powershell
# Login
render login

# List services
render services list

# View logs
render logs

# View service info
render service show SERVICE_ID
```

---

## 🔧 TROUBLESHOOTING COMMANDS

### Check Backend Status

```powershell
# Test backend health
curl https://YOUR-BACKEND-URL.onrender.com/health

# Test API root
curl https://YOUR-BACKEND-URL.onrender.com/

# Test analyze endpoint (with PowerShell)
Invoke-RestMethod -Uri "https://YOUR-BACKEND-URL.onrender.com/health" -Method Get
```

### Check Frontend Build Locally

```powershell
cd "c:\Users\jay likhar\OneDrive\Desktop\Accessibility Analyzer\frontend"
npm install
npm run build

# Check if build succeeds
# If errors, fix them before deploying
```

### View Deployment Logs

**Render:**
- Go to Render dashboard → Your service → "Logs" tab

**Vercel:**
```powershell
vercel logs
# Or check dashboard → Your project → "Deployments" → Click deployment → "Build Logs"
```

---

## ✅ DEPLOYMENT CHECKLIST

### Before Deploying:

- [ ] Code pushed to GitHub
- [ ] Backend `requirements.txt` exists
- [ ] Frontend `package.json` exists
- [ ] Environment variables ready

### Render (Backend):

- [ ] Account created
- [ ] Repository connected
- [ ] Root Directory: `backend`
- [ ] Build Command: `pip install -r requirements.txt`
- [ ] Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- [ ] Service deployed successfully
- [ ] Health endpoint tested: `/health`

### Vercel (Frontend):

- [ ] Account created
- [ ] Repository connected
- [ ] Root Directory: `frontend`
- [ ] Environment Variable `VITE_API_URL` set
- [ ] Backend URL correct (no trailing slash)
- [ ] Frontend deployed successfully
- [ ] Website tested and working

---

## 🎯 COMPLETE DEPLOYMENT WORKFLOW

### First Time Setup:

```powershell
# 1. Push code to GitHub (already done)
cd "c:\Users\jay likhar\OneDrive\Desktop\Accessibility Analyzer"
git push origin main

# 2. Deploy Backend on Render (use web UI - easier)
# Go to render.com and follow steps above

# 3. Deploy Frontend on Vercel
cd frontend
vercel login
vercel --prod

# 4. Set environment variable
vercel env add VITE_API_URL production
# Enter: https://YOUR-BACKEND-URL.onrender.com
```

### Regular Updates:

```powershell
# Just push to GitHub - both auto-deploy!
cd "c:\Users\jay likhar\OneDrive\Desktop\Accessibility Analyzer"
git add .
git commit -m "Your update message"
git push origin main

# Render and Vercel will automatically deploy updates
```

---

## 📝 IMPORTANT NOTES

1. **Auto-Deploy:** Both Render and Vercel auto-deploy when you push to GitHub
2. **Environment Variables:** Must be set in Vercel dashboard or via CLI
3. **Backend URL:** Update `VITE_API_URL` if backend URL changes
4. **Free Tiers:**
   - Render: Sleeps after 15 min inactivity (wakes on first request)
   - Vercel: Always-on, unlimited deployments

---

## 🎉 YOU'RE READY!

Follow the steps above and your Accessibility Analyzer will be live! 🚀

**Need help?** Check the logs in Render/Vercel dashboards for errors.
