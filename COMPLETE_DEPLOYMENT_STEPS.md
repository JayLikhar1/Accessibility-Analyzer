# 🚀 Complete Deployment Guide - Step by Step

This guide covers everything: GitHub → Backend → Frontend

---

## 📦 PART 1: GitHub Setup (Put Your Code Online)

### Step 1: Create GitHub Account
1. Go to **https://github.com**
2. Click **"Sign up"** (top right)
3. Enter your email, password, username
4. Verify your email
5. ✅ **Done!** You now have a GitHub account

### Step 2: Create New Repository
1. After logging in, click the **"+"** button (top right)
2. Click **"New repository"**
3. Fill in:
   - **Repository name**: `accessibility-analyzer`
   - **Description**: `AI-powered accessibility analyzer for websites` (optional)
   - **Visibility**: Choose **Public** (or Private if you prefer)
   - **⚠️ IMPORTANT**: Do NOT check "Add a README file" (we already have files)
   - **⚠️ IMPORTANT**: Do NOT add .gitignore or license (we already have them)
4. Click **"Create repository"**
5. ✅ **Done!** Repository created

### Step 3: Upload Your Code to GitHub

**Method A: Using GitHub Desktop (EASIEST - Recommended)**

1. **Download GitHub Desktop:**
   - Go to **https://desktop.github.com/**
   - Click **"Download for Windows"**
   - Install the downloaded file

2. **Sign in to GitHub Desktop:**
   - Open GitHub Desktop
   - Click **"Sign in to GitHub.com"**
   - Authorize GitHub Desktop

3. **Add Your Project:**
   - Click **"File"** → **"Add Local Repository"**
   - Click **"Choose..."**
   - Navigate to: `C:\Users\jay likhar\OneDrive\Desktop\Accessibility Analyzer`
   - Click **"Add repository"**

4. **Publish to GitHub:**
   - You'll see your files listed
   - At the bottom, type: `Initial commit` in the summary box
   - Click **"Commit to main"**
   - Click **"Publish repository"**
   - Make sure repository name is: `accessibility-analyzer`
   - Make sure it's set to your GitHub account
   - Click **"Publish repository"**

5. ✅ **Done!** Your code is now on GitHub!

**Method B: Using Command Line (Alternative)**

1. Open **PowerShell** in your project folder:
   - Press `Windows + R`
   - Type: `powershell`
   - Press Enter
   - Type: `cd "C:\Users\jay likhar\OneDrive\Desktop\Accessibility Analyzer"`
   - Press Enter

2. **Run these commands one by one:**

```powershell
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/accessibility-analyzer.git
git push -u origin main
```

⚠️ **Replace `YOUR_USERNAME`** with your actual GitHub username!

3. ✅ **Done!** Your code is now on GitHub!

### Step 4: Verify Upload
1. Go to **https://github.com/YOUR_USERNAME/accessibility-analyzer**
2. You should see all your files (backend, frontend, README, etc.)
3. ✅ **Perfect!** Move to Part 2

---

## 🔧 PART 2: Backend Deployment (Render)

### Step 5: Create Render Account
1. Go to **https://render.com**
2. Click **"Get Started for Free"** (top right)
3. Click **"Sign up with GitHub"** (easiest way)
4. Authorize Render to access your GitHub
5. ✅ **Done!** You're logged into Render

### Step 6: Create Web Service
1. In Render dashboard, click **"New +"** button (top right)
2. Click **"Web Service"**
3. You'll see "Connect a repository" - if not connected:
   - Click **"Connect GitHub"**
   - Authorize Render
   - Find and select: **`accessibility-analyzer`**
   - Click **"Connect"**

### Step 7: Configure Backend Settings

Fill in these exact settings:

**Basic Settings:**
- **Name**: `accessibility-analyzer-backend` (or any name you like)
- **Region**: Choose closest to you (e.g., `Oregon (US West)` or `Frankfurt (EU Central)`)
- **Branch**: `main` (should be selected automatically)
- **Root Directory**: `backend` ⚠️ **IMPORTANT: Type this exactly**
- **Runtime**: `Python 3` (should be auto-detected)

**Build & Deploy:**
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

**Advanced Settings (Optional - Skip for now):**
- You can leave everything else as default

### Step 8: Deploy Backend
1. Scroll down and click **"Create Web Service"** (blue button)
2. ⏳ **Wait 5-10 minutes** - Render is:
   - Installing Python
   - Installing your packages
   - Starting your server
3. You'll see logs scrolling - this is normal!
4. When you see: `Application is live` ✅
5. **Copy your URL** - it looks like: `https://accessibility-analyzer-backend.onrender.com`
6. ⚠️ **SAVE THIS URL** - you'll need it for frontend!

### Step 9: Test Backend
1. Open a new browser tab
2. Go to: `https://YOUR-BACKEND-URL.onrender.com/health`
   (Replace `YOUR-BACKEND-URL` with your actual URL)
3. You should see: `{"status":"healthy"}`
4. ✅ **Backend is working!**

### Step 10: Test Backend API
1. Go to: `https://YOUR-BACKEND-URL.onrender.com`
2. You should see: `{"message":"Accessibility Analyzer API","version":"1.0.0"}`
3. ✅ **Perfect!** Backend is ready!

---

## 🎨 PART 3: Frontend Deployment (Vercel)

### Step 11: Create Vercel Account
1. Go to **https://vercel.com**
2. Click **"Sign Up"** (top right)
3. Click **"Continue with GitHub"** (easiest way)
4. Authorize Vercel to access your GitHub
5. ✅ **Done!** You're logged into Vercel

### Step 12: Import Project
1. In Vercel dashboard, click **"Add New..."** button (top right)
2. Click **"Project"**
3. You'll see your repositories - find **`accessibility-analyzer`**
4. Click **"Import"** next to it

### Step 13: Configure Frontend Settings

**Project Settings:**
- **Project Name**: `accessibility-analyzer` (or any name)
- **Framework Preset**: Should auto-detect as **"Vite"** ✅
- **Root Directory**: Click **"Edit"** → Change to: `frontend` ⚠️ **IMPORTANT**
- **Build Command**: `npm run build` (should be automatic)
- **Output Directory**: `dist` (should be automatic)
- **Install Command**: `npm install` (should be automatic)

**Environment Variables:**
1. Scroll down to **"Environment Variables"** section
2. Click **"Add New"**
3. Fill in:
   - **Key**: `VITE_API_URL`
   - **Value**: Your backend URL from Step 8 (e.g., `https://accessibility-analyzer-backend.onrender.com`)
   - ⚠️ **IMPORTANT**: No trailing slash, no `/health`, just the base URL
4. Click **"Save"**

### Step 14: Deploy Frontend
1. Scroll down and click **"Deploy"** button (bottom right)
2. ⏳ **Wait 2-3 minutes** - Vercel is:
   - Installing Node.js packages
   - Building your React app
   - Deploying to CDN
3. When you see: `Ready` ✅
4. **Copy your URL** - it looks like: `https://accessibility-analyzer.vercel.app`
5. ⚠️ **SAVE THIS URL** - this is your live website!

### Step 15: Test Frontend
1. Open your Vercel URL in browser
2. You should see the **"Accessibility Analyzer"** landing page
3. Enter a test URL: `https://example.com`
4. Click **"Analyze"**
5. ⏳ Wait for analysis (may take 30-60 seconds first time if Render is sleeping)
6. You should see the dashboard with scores!
7. ✅ **Everything works!** 🎉

---

## ✅ FINAL CHECKLIST

Make sure you have:

- [ ] ✅ Code uploaded to GitHub
- [ ] ✅ Backend deployed on Render
- [ ] ✅ Backend URL tested (`/health` endpoint works)
- [ ] ✅ Frontend deployed on Vercel
- [ ] ✅ Environment variable `VITE_API_URL` set correctly
- [ ] ✅ Frontend can analyze websites

---

## 🔧 TROUBLESHOOTING

### Issue: "Backend not connecting"

**Check:**
1. Go to Vercel → Your Project → Settings → Environment Variables
2. Make sure `VITE_API_URL` matches your Render URL exactly
3. No `http://` or trailing `/` - just: `https://xxx.onrender.com`
4. Click **"Redeploy"** after changing environment variables

### Issue: "Backend is sleeping"

**What happens:**
- Render free tier sleeps after 15 minutes of no activity
- First request takes 30-60 seconds (waking up)
- This is **normal** on free tier

**Solution:**
- Just wait - it will wake up
- Or upgrade to paid plan for always-on

### Issue: "CORS error"

**Check:**
- The code already allows all origins
- If still getting errors, check Render logs
- Make sure backend is actually running

### Issue: "Build failed"

**Backend (Render):**
- Check logs in Render dashboard
- Make sure `requirements.txt` exists in `backend` folder
- Verify Python version is correct

**Frontend (Vercel):**
- Check logs in Vercel dashboard
- Make sure `package.json` exists in `frontend` folder
- Verify Root Directory is set to `frontend`

### Issue: "404 Not Found"

**Backend:**
- Make sure Root Directory is: `backend`
- Check Start Command is correct

**Frontend:**
- Make sure Root Directory is: `frontend`
- Check Build Command and Output Directory

---

## 📝 IMPORTANT NOTES

1. **Free Tiers:**
   - Render: Free tier sleeps after inactivity (normal)
   - Vercel: Always-on, unlimited (great!)

2. **URLs Change:**
   - If you delete and recreate services, URLs change
   - Update `VITE_API_URL` in Vercel if backend URL changes

3. **Auto-Deploy:**
   - Both platforms auto-deploy when you push to GitHub
   - Just commit and push, and they'll update automatically!

4. **Environment Variables:**
   - Changes require redeploy
   - In Vercel: Settings → Environment Variables → Save → Redeploy

---

## 🎉 CONGRATULATIONS!

Your Accessibility Analyzer is now live on the internet!

**Your URLs:**
- 🌐 **Frontend (Live Website)**: `https://your-app.vercel.app`
- 🔧 **Backend API**: `https://your-backend.onrender.com`

**Share your frontend URL with anyone!** They can now analyze websites for accessibility! 🚀

---

## 📞 Need Help?

- Check logs in Render/Vercel dashboards
- Look for error messages in red
- Common issues are listed above
- Make sure all settings match exactly as written

**You've got this!** 🎯
