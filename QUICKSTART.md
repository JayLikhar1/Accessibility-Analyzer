# Quick Start Guide

Get the Accessibility Analyzer up and running in minutes!

## Prerequisites

- Python 3.9 or higher
- Node.js 18 or higher
- npm or yarn

## Step-by-Step Setup

### 1. Backend Setup

Open a terminal and navigate to the backend directory:

```bash
cd backend
```

Create and activate a virtual environment:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Start the backend server:

```bash
python main.py
```

The backend API will be running on `http://localhost:8000`

You can verify it's working by visiting `http://localhost:8000/health` in your browser.

### 2. Frontend Setup

Open a **new terminal** and navigate to the frontend directory:

```bash
cd frontend
```

Install Node.js dependencies:

```bash
npm install
```

Create a `.env` file (copy from `.env.example`):

**Windows:**
```bash
copy .env.example .env
```

**macOS/Linux:**
```bash
cp .env.example .env
```

Start the development server:

```bash
npm run dev
```

The frontend will be running on `http://localhost:3000`

### 3. Test the Application

1. Open your browser and go to `http://localhost:3000`
2. Enter a website URL (e.g., `https://example.com`)
3. Click "Analyze"
4. View the accessibility report!

## Troubleshooting

### Backend Issues

**Port 8000 already in use:**
- Change the port in `backend/main.py`: `uvicorn.run(app, host="0.0.0.0", port=8001)`
- Update `frontend/.env` to match: `VITE_API_URL=http://localhost:8001`

**Module not found errors:**
- Make sure your virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

### Frontend Issues

**Port 3000 already in use:**
- Vite will automatically use the next available port (3001, 3002, etc.)
- Or specify a port: `npm run dev -- --port 3001`

**API connection errors:**
- Verify backend is running on port 8000
- Check `frontend/.env` has correct `VITE_API_URL`
- Check browser console for CORS errors

**Build errors:**
- Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`
- Clear npm cache: `npm cache clean --force`

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Test with different websites to see various accessibility issues
- Customize the UI colors in `frontend/tailwind.config.js`
- Add more WCAG checks in `backend/analyzer/rules.py`

## Production Deployment

See the [README.md](README.md) for deployment instructions to Vercel (frontend) and Render/Railway (backend).
