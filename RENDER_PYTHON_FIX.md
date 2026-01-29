# 🔧 Fix Python 3.13 Compatibility Issue

## Problem
Render is using Python 3.13, which has breaking changes with older pydantic versions. The error:
```
TypeError: ForwardRef._evaluate() missing 1 required keyword-only argument: 'recursive_guard'
```

## Solution Applied

1. ✅ Fixed `runtime.txt` encoding and set to Python 3.11.9
2. ✅ Updated `requirements.txt` to use pydantic 2.9.0+ (supports Python 3.13)
3. ✅ Updated FastAPI and uvicorn to latest compatible versions

## What You Need to Do

### Option 1: Set Python Version in Render Dashboard (RECOMMENDED)

1. Go to your Render dashboard
2. Click on your backend service
3. Go to **"Settings"** tab
4. Scroll to **"Environment"** section
5. Find **"Python Version"** dropdown
6. Select: **`Python 3.11`** (NOT 3.13)
7. Click **"Save Changes"**
8. Go to **"Manual Deploy"** → **"Deploy latest commit"**

### Option 2: Push Updated Files (Auto-Deploy)

The updated files are ready. Push to GitHub:

```powershell
cd "c:\Users\jay likhar\OneDrive\Desktop\Accessibility Analyzer"
git add backend/runtime.txt backend/requirements.txt
git commit -m "Fix Python 3.13 compatibility: Update pydantic and set Python 3.11"
git push origin main
```

Render will auto-deploy, but you still need to set Python version in dashboard.

### Option 3: Use Python 3.13 Compatible Versions

If you want to use Python 3.13, the updated `requirements.txt` now has pydantic 2.9.0 which supports it. But Python 3.11 is more stable.

## Verify Fix

After deployment:
1. Check Render logs - should show Python 3.11
2. Test: `https://YOUR-BACKEND-URL.onrender.com/health`
3. Should return: `{"status":"healthy"}`

## Important Notes

- **Python 3.11 is recommended** - more stable, better wheel support
- **runtime.txt** must be in `backend` folder (where Render looks)
- **Manual Python version setting** in Render dashboard is most reliable
- The updated pydantic 2.9.0 works with both Python 3.11 and 3.13
