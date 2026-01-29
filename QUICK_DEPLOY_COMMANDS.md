# ⚡ Quick Deploy Commands - Copy & Paste

Fast reference for deploying your Accessibility Analyzer

---

## 🚀 ONE-TIME SETUP

### 1. Push Code to GitHub (Already Done ✅)

```powershell
cd "c:\Users\jay likhar\OneDrive\Desktop\Accessibility Analyzer"
git push origin main
```

---

## 🔧 BACKEND: Render Deployment

### Web UI Method (Easiest - No Commands)

1. Go to: **https://render.com**
2. Sign up with GitHub
3. Click: **"New +"** → **"Web Service"**
4. Connect: `accessibility-analyzer` repository
5. Settings:
   ```
   Root Directory: backend
   Build Command: pip install -r requirements.txt
   Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
6. Click: **"Create Web Service"**
7. Wait 5-10 minutes
8. Copy URL: `https://xxx.onrender.com`

### Test Backend

```powershell
# Open in browser or use curl:
curl https://YOUR-BACKEND-URL.onrender.com/health
```

---

## 🎨 FRONTEND: Vercel Deployment

### Method 1: Web UI (Easiest)

1. Go to: **https://vercel.com**
2. Sign up with GitHub
3. Click: **"Add New..."** → **"Project"**
4. Import: `accessibility-analyzer`
5. Settings:
   ```
   Root Directory: frontend
   ```
6. Environment Variable:
   ```
   Key: VITE_API_URL
   Value: https://YOUR-BACKEND-URL.onrender.com
   ```
7. Click: **"Deploy"**
8. Wait 2-3 minutes
9. Copy URL: `https://xxx.vercel.app`

### Method 2: CLI Commands

```powershell
# Install Vercel CLI (one time)
npm install -g vercel

# Navigate to frontend
cd "c:\Users\jay likhar\OneDrive\Desktop\Accessibility Analyzer\frontend"

# Login (first time only)
vercel login

# Deploy
vercel --prod

# Add environment variable
vercel env add VITE_API_URL production
# When prompted, enter: https://YOUR-BACKEND-URL.onrender.com
```

---

## 🔄 UPDATE CODE (After Changes)

```powershell
# Navigate to project
cd "c:\Users\jay likhar\OneDrive\Desktop\Accessibility Analyzer"

# Add changes
git add .

# Commit
git commit -m "Your update description"

# Push (triggers auto-deploy on both platforms)
git push origin main
```

**That's it!** Both Render and Vercel will automatically deploy your changes.

---

## ✅ VERIFY DEPLOYMENT

### Backend (Render)

```powershell
# Test health
curl https://YOUR-BACKEND-URL.onrender.com/health

# Should return: {"status":"healthy"}
```

### Frontend (Vercel)

1. Open: `https://YOUR-APP.vercel.app`
2. Enter test URL: `https://example.com`
3. Click: **"Analyze"**
4. Should show results! ✅

---

## 🔧 TROUBLESHOOTING

### Backend Not Working?

```powershell
# Check Render logs in dashboard
# Common issues:
# - Wrong Root Directory (should be: backend)
# - Wrong Start Command (should be: uvicorn main:app --host 0.0.0.0 --port $PORT)
```

### Frontend Can't Connect?

```powershell
# Check environment variable in Vercel
vercel env ls

# Update if wrong:
vercel env rm VITE_API_URL production
vercel env add VITE_API_URL production
# Enter correct backend URL
```

### View Logs

**Render:**
- Dashboard → Service → "Logs" tab

**Vercel:**
```powershell
vercel logs
```

---

## 📋 CHECKLIST

- [ ] Code on GitHub
- [ ] Backend deployed on Render
- [ ] Backend URL copied
- [ ] Frontend deployed on Vercel
- [ ] `VITE_API_URL` set correctly
- [ ] Both tested and working

---

## 🎉 DONE!

Your app is live! Share your Vercel URL: `https://xxx.vercel.app`
