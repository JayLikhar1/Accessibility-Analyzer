# 🚀 Deployment Guide - Step by Step

This guide will help you deploy your Accessibility Analyzer to the internet so anyone can use it.

## 📋 What You Need

- A GitHub account (free)
- A Vercel account (free) - for frontend
- A Render account (free) - for backend
- Your code ready to push

---

## Part 1: Prepare Your Code for GitHub

### Step 1: Create a GitHub Repository

1. Go to [github.com](https://github.com) and sign in
2. Click the **"+"** button in the top right
3. Click **"New repository"**
4. Name it: `accessibility-analyzer`
5. Make it **Public** (or Private if you prefer)
6. **Don't** check "Initialize with README" (we already have files)
7. Click **"Create repository"**

### Step 2: Upload Your Code to GitHub

**Option A: Using GitHub Desktop (Easiest)**

1. Download [GitHub Desktop](https://desktop.github.com/)
2. Install and sign in
3. Click **"File" → "Add Local Repository"**
4. Browse to your project folder: `C:\Users\jay likhar\OneDrive\Desktop\Accessibility Analyzer`
5. Click **"Publish repository"**
6. Make sure it's set to your GitHub account
7. Click **"Publish repository"**

**Option B: Using Command Line**

1. Open PowerShell in your project folder
2. Run these commands one by one:

```powershell
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/accessibility-analyzer.git
git push -u origin main
```

(Replace `YOUR_USERNAME` with your GitHub username)

---

## Part 2: Deploy Backend (Render)

### Step 3: Create Render Account

1. Go to [render.com](https://render.com)
2. Click **"Get Started for Free"**
3. Sign up with your GitHub account (easiest way)

### Step 4: Create Backend Service

1. In Render dashboard, click **"New +"** button
2. Click **"Web Service"**
3. Click **"Connect GitHub"** if not connected
4. Find and select your `accessibility-analyzer` repository
5. Click **"Connect"**

### Step 5: Configure Backend Settings

Fill in these settings:

- **Name**: `accessibility-analyzer-backend` (or any name you like)
- **Region**: Choose closest to you (e.g., `Oregon (US West)`)
- **Branch**: `main`
- **Root Directory**: `backend`
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Step 6: Deploy Backend

1. Scroll down and click **"Create Web Service"**
2. Wait 5-10 minutes for deployment (you'll see logs)
3. Once done, you'll see a URL like: `https://accessibility-analyzer-backend.onrender.com`
4. **Copy this URL** - you'll need it for frontend!

### Step 7: Test Backend

1. Open the URL in your browser
2. Add `/health` at the end: `https://your-backend-url.onrender.com/health`
3. You should see: `{"status":"healthy"}`
4. If yes, backend is working! ✅

---

## Part 3: Deploy Frontend (Vercel)

### Step 8: Create Vercel Account

1. Go to [vercel.com](https://vercel.com)
2. Click **"Sign Up"**
3. Sign up with your GitHub account (easiest way)

### Step 9: Import Your Project

1. In Vercel dashboard, click **"Add New..."**
2. Click **"Project"**
3. Find your `accessibility-analyzer` repository
4. Click **"Import"**

### Step 10: Configure Frontend Settings

1. **Framework Preset**: Select `Vite`
2. **Root Directory**: Click **"Edit"** and change to `frontend`
3. **Build Command**: `npm run build` (should be automatic)
4. **Output Directory**: `dist` (should be automatic)

### Step 11: Add Environment Variable

1. Scroll down to **"Environment Variables"**
2. Click **"Add New"**
3. **Name**: `VITE_API_URL`
4. **Value**: Your backend URL from Step 6 (e.g., `https://accessibility-analyzer-backend.onrender.com`)
5. Click **"Save"**

### Step 12: Deploy Frontend

1. Scroll down and click **"Deploy"**
2. Wait 2-3 minutes for deployment
3. Once done, you'll see a URL like: `https://accessibility-analyzer.vercel.app`
4. **This is your live website!** 🎉

---

## Part 4: Test Everything

### Step 13: Test Your Live Website

1. Open your Vercel URL in browser
2. Enter a website URL (e.g., `https://example.com`)
3. Click **"Analyze"**
4. Wait for results
5. If you see the dashboard with scores, **everything works!** ✅

### Step 14: Fix CORS (If Needed)

If you get errors, you need to update backend CORS settings:

1. Go back to Render dashboard
2. Find your backend service
3. Go to **"Environment"** tab
4. Add new variable:
   - **Name**: `CORS_ORIGINS`
   - **Value**: Your Vercel URL (e.g., `https://accessibility-analyzer.vercel.app`)
5. Click **"Save Changes"**
6. Update `backend/main.py`:

```python
# Replace this line in main.py:
allow_origins=["http://localhost:3000", "http://localhost:5173"],

# With this (add your Vercel URL):
allow_origins=[
    "http://localhost:3000", 
    "http://localhost:5173",
    "https://accessibility-analyzer.vercel.app"  # Your Vercel URL
],
```

7. Commit and push to GitHub
8. Render will auto-deploy the update

---

## 🎯 Quick Checklist

- [ ] Code pushed to GitHub
- [ ] Backend deployed on Render
- [ ] Backend URL tested and working
- [ ] Frontend deployed on Vercel
- [ ] Environment variable `VITE_API_URL` set in Vercel
- [ ] Live website tested and working

---

## 🔧 Troubleshooting

### Backend won't start?
- Check Render logs (click on your service → "Logs" tab)
- Make sure `requirements.txt` has all packages
- Verify start command is correct

### Frontend can't connect to backend?
- Check `VITE_API_URL` is set correctly in Vercel
- Make sure backend URL doesn't have `/health` or anything extra
- Check CORS settings in backend

### Getting 404 errors?
- Make sure Root Directory is set correctly
- Backend: `backend`
- Frontend: `frontend`

### Backend goes to sleep?
- Render free tier sleeps after 15 minutes of inactivity
- First request after sleep takes 30-60 seconds (it's waking up)
- Consider upgrading to paid plan for always-on

---

## 📝 Notes

- **Free tiers are limited**: Render free tier sleeps, Vercel is always-on
- **Backend URL changes**: If you delete and recreate, URL changes
- **Update frontend**: If backend URL changes, update `VITE_API_URL` in Vercel
- **Auto-deploy**: Both platforms auto-deploy when you push to GitHub

---

## 🎉 You're Done!

Your Accessibility Analyzer is now live on the internet! Share your Vercel URL with anyone.

**Need help?** Check the logs in Render/Vercel dashboards - they show what's happening.
