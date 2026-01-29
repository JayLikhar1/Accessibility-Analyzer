# 🔧 Fix Render Build Error

## Problem
Render is failing to build because `pydantic-core` requires Rust compilation, and Render's environment has issues with it.

## Solution Applied

1. ✅ Updated `requirements.txt` to use newer versions with better wheel support
2. ✅ Created `runtime.txt` to specify Python 3.11 (better wheel support than 3.13)

## What You Need to Do

### Option 1: Update Render Settings (Recommended)

1. Go to your Render dashboard
2. Click on your backend service
3. Go to **"Settings"** tab
4. Scroll to **"Environment"** section
5. Find **"Python Version"** or **"Runtime"**
6. Set it to: **`python-3.11`** or **`3.11`**
7. Click **"Save Changes"**
8. Click **"Manual Deploy"** → **"Deploy latest commit"**

### Option 2: Use runtime.txt (Already Created)

The `runtime.txt` file has been created in your `backend` folder. Render should automatically detect it.

1. Make sure `runtime.txt` is in your `backend` folder ✅ (already done)
2. Push the changes to GitHub:
   ```powershell
   cd "c:\Users\jay likhar\OneDrive\Desktop\Accessibility Analyzer"
   git add .
   git commit -m "Fix Render build: Update Python version and dependencies"
   git push origin main
   ```
3. Render will automatically redeploy

### Option 3: Alternative Requirements (If Still Failing)

If the build still fails, try this alternative `requirements.txt`:

```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.3
requests==2.31.0
beautifulsoup4==4.12.2
lxml==4.9.3
python-multipart==0.0.6
```

## Verify Fix

After deployment, check:
1. Render logs show successful build
2. Test: `https://YOUR-BACKEND-URL.onrender.com/health`
3. Should return: `{"status":"healthy"}`

## Common Issues

**Still getting Rust errors?**
- Make sure Python version is set to 3.11 in Render settings
- Check that `runtime.txt` is in the `backend` folder
- Try the alternative requirements.txt above

**Build succeeds but app doesn't start?**
- Check Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Check Root Directory: `backend`
- Check logs in Render dashboard
