# 🔧 Fix Python Version in Render - Alternative Methods

## Problem
Render dashboard doesn't show Python version dropdown option.

## Solutions

### Method 1: Use render.yaml (RECOMMENDED - Already Created)

The `render.yaml` file has been created/updated in your `backend` folder. This is the most reliable way to set Python version.

**What to do:**
1. Make sure `backend/render.yaml` exists ✅ (already done)
2. Push to GitHub:
   ```powershell
   cd "c:\Users\jay likhar\OneDrive\Desktop\Accessibility Analyzer"
   git add backend/render.yaml
   git commit -m "Add render.yaml to specify Python 3.11.9"
   git push origin main
   ```
3. In Render dashboard:
   - Go to your service
   - Settings → **"Apply render.yaml"** or **"Sync from render.yaml"**
   - Or delete and recreate service - it will auto-detect render.yaml

### Method 2: Use runtime.txt (Already Created)

The `runtime.txt` file should work, but Render might not always read it.

**Verify:**
1. Make sure `backend/runtime.txt` contains: `python-3.11.9`
2. File should be in the `backend` folder (where Render's Root Directory points)
3. Push to GitHub if not already pushed

### Method 3: Delete and Recreate Service

If render.yaml doesn't work:

1. **Delete current service** in Render dashboard
2. **Create new service** with these exact settings:
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
3. Render should detect `runtime.txt` or `render.yaml` automatically

### Method 4: Use Environment Variable

1. Go to Render dashboard → Your service
2. Settings → **Environment**
3. Add new environment variable:
   - **Key**: `PYTHON_VERSION`
   - **Value**: `3.11.9`
4. Save and redeploy

### Method 5: Check Buildpack Settings

Some Render services use buildpacks:

1. Go to Settings → **Build & Deploy**
2. Look for **"Buildpack"** or **"Runtime"** section
3. If you see buildpack options, select Python buildpack
4. There might be a Python version option there

## Verify Python Version

After deployment, check logs:

1. Go to Render dashboard → Your service → **Logs**
2. Look for: `Python 3.11.9` or `Python 3.11.x` in build logs
3. If you see `Python 3.13`, the version wasn't set correctly

## Current Files

✅ `backend/runtime.txt` - Contains: `python-3.11.9`
✅ `backend/render.yaml` - Specifies Python 3.11.9
✅ `backend/requirements.txt` - Updated to pydantic 2.9.0 (works with both 3.11 and 3.13)

## Recommended Action

1. **Push render.yaml to GitHub** (if not already pushed)
2. **Delete and recreate** the Render service - it will auto-detect render.yaml
3. Or manually apply render.yaml in Render dashboard

The render.yaml method is the most reliable way to ensure Python 3.11 is used.
