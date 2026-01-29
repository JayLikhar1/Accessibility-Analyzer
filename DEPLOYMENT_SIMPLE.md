# 🚀 Simple Deployment Guide

Deploy your Accessibility Analyzer in 15 minutes! Follow these steps:

---

## Step 1: Put Your Code on GitHub (5 minutes)

1. **Go to github.com** and sign in
2. Click **"+"** → **"New repository"**
3. Name it: `accessibility-analyzer`
4. Click **"Create repository"**
5. **Upload your code:**
   - Download [GitHub Desktop](https://desktop.github.com/)
   - Open GitHub Desktop → **File** → **Add Local Repository**
   - Select your project folder
   - Click **"Publish repository"**

✅ **Done!** Your code is now on GitHub.

---

## Step 2: Deploy Backend on Render (5 minutes)

1. **Go to render.com** and sign up (use GitHub login)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. **Settings:**
   - Name: `accessibility-backend`
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Click **"Create Web Service"**
6. **Wait 5 minutes** - copy the URL when done (looks like: `https://xxx.onrender.com`)

✅ **Done!** Backend is live.

---

## Step 3: Deploy Frontend on Vercel (5 minutes)

1. **Go to vercel.com** and sign up (use GitHub login)
2. Click **"Add New..."** → **"Project"**
3. Select your repository
4. **Settings:**
   - Root Directory: `frontend`
   - Framework: Vite (auto-detected)
5. **Add Environment Variable:**
   - Name: `VITE_API_URL`
   - Value: Your Render URL from Step 2
6. Click **"Deploy"**
7. **Wait 2 minutes** - you'll get a URL (looks like: `https://xxx.vercel.app`)

✅ **Done!** Your website is live!

---

## Step 4: Test It!

1. Open your Vercel URL
2. Enter `https://example.com`
3. Click **"Analyze"**
4. If you see results, **everything works!** 🎉

---

## ⚠️ Common Issues

**"Can't connect to backend"**
- Check `VITE_API_URL` in Vercel matches your Render URL exactly
- Make sure Render service is running (not sleeping)

**"Backend is sleeping"**
- Render free tier sleeps after 15 minutes
- First request takes 30-60 seconds to wake up
- This is normal on free tier

**"CORS error"**
- The code already allows all origins, so this shouldn't happen
- If it does, check backend logs in Render

---

## 🎯 That's It!

Your Accessibility Analyzer is now live on the internet!

**Your URLs:**
- Frontend: `https://your-app.vercel.app`
- Backend: `https://your-backend.onrender.com`

Share your frontend URL with anyone! 🌐
