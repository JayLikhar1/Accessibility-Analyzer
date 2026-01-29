# Accessibility Analyzer

An AI-powered accessibility analysis tool that scans websites and generates actionable WCAG 2.1 compliance reports with checklist progress, issue severity, and clear fixes.

## 🎯 Problem Statement

Web accessibility is crucial for ensuring that websites are usable by everyone, including people with disabilities. However, many developers and organizations struggle to:
- Identify accessibility issues systematically
- Understand WCAG compliance requirements
- Prioritize fixes based on severity
- Get actionable recommendations

This tool addresses these challenges by providing automated, comprehensive accessibility analysis with ML-enhanced insights.

## 🌟 Why Accessibility Matters

- **Legal Compliance**: Many countries require WCAG compliance (ADA, Section 508, EN 301 549)
- **Inclusivity**: 15% of the world's population has some form of disability
- **Better UX**: Accessible sites are more usable for everyone
- **SEO Benefits**: Accessible sites rank better in search engines
- **Business Impact**: Larger audience reach and reduced legal risk

## 🏗️ Architecture

```
React Frontend (UI)
   ↓
FastAPI Backend
   ↓
HTML Scraper (Security: SSRF Protection)
   ↓
Rule-Based Analyzer (WCAG Checks)
   ↓
ML/NLP Analyzer (Quality Scoring)
   ↓
Scoring Engine
   ↓
JSON Accessibility Report
```

## ✨ Features

### Core Functionality
- **URL Analysis**: Enter any website URL and get comprehensive analysis
- **WCAG 2.1 Compliance**: Checks based on WCAG 2.1 guidelines
- **Checklist-Driven UI**: Clear, actionable checklist interface
- **Severity Classification**: Issues categorized as High, Medium, or Low
- **Fix Suggestions**: Specific recommendations for each issue
- **Overall Score**: 0-100 accessibility score

### WCAG Checks Implemented
- ✅ Missing alt text (WCAG 1.1.1)
- ✅ Poor alt text quality (ML-enhanced)
- ✅ Low color contrast (WCAG 1.4.3)
- ✅ Missing form labels (WCAG 1.3.1, 3.3.2)
- ✅ Improper heading hierarchy (WCAG 1.3.1)
- ✅ Empty/vague links (WCAG 2.4.4)
- ✅ Missing lang attribute (WCAG 3.1.1)
- ✅ Button accessibility issues (WCAG 4.1.2)

### ML/NLP Enhancements
- Alt-text quality scoring
- Vague link text detection
- Readability scoring (Flesch-like)
- Severity classification

## 🛠️ Tech Stack

### Frontend
- **React 18** - UI framework
- **Tailwind CSS** - Styling
- **React Router** - Navigation
- **Axios** - API client
- **Recharts** - Data visualization (optional)

### Backend
- **FastAPI** - Python web framework
- **BeautifulSoup4** - HTML parsing
- **Requests** - HTTP client
- **Scikit-learn/spaCy** - ML/NLP (lightweight implementations)

## 📁 Project Structure

```
accessibility-analyzer/
│
├── backend/
│   ├── main.py                 # FastAPI app
│   ├── analyzer/
│   │   ├── scraper.py         # Web scraping with SSRF protection
│   │   ├── rules.py           # WCAG rule-based checks
│   │   ├── ml_analyzer.py     # ML/NLP analysis
│   │   ├── checklist.py       # Checklist generator
│   │   ├── scorer.py          # Scoring engine
│   │   └── utils.py           # Utility functions
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── pages/             # Landing, Dashboard
│   │   ├── components/        # ScoreCard, Checklist, Table, etc.
│   │   ├── layout/            # Layout component
│   │   ├── services/          # API client
│   │   ├── styles/            # Tailwind CSS
│   │   └── App.jsx
│   ├── package.json
│   └── tailwind.config.js
│
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Node.js 18+
- npm or yarn

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the server:
```bash
python main.py
# Or: uvicorn main:app --reload
```

Backend will run on `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start development server:
```bash
npm run dev
```

Frontend will run on `http://localhost:3000`

### Environment Variables

Create `.env` file in frontend directory:
```
VITE_API_URL=http://localhost:8000
```

## 📊 UI/UX Design

### Design Principles
- **Calm & Minimal**: Clean, professional interface
- **Checklist-Driven**: Focus on actionable items
- **Accessible Colors**: WCAG-compliant color palette
- **Editorial Typography**: Clear, readable fonts
- **Enterprise SaaS Style**: Professional, trustworthy appearance

### Color System
- Background: `#F7F8FA`
- Card BG: `#FFFFFF`
- Border: `#E5E7EB`
- Text: `#111827`
- Muted Text: `#6B7280`
- High Severity: `#DC2626`
- Medium Severity: `#F59E0B`
- Low Severity: `#16A34A`
- Primary CTA: `#2563EB`

## 🔐 Security Features

- **SSRF Protection**: Blocks localhost and private IPs
- **Timeout Handling**: 15-second request timeout
- **Content Size Limits**: Maximum 10MB HTML
- **Input Validation**: URL validation and sanitization
- **Error Handling**: Graceful error messages

## 🧪 Testing

Test with various website types:
- Blog websites
- Government sites
- Portfolio sites
- E-commerce sites

## 📈 Scoring Algorithm

Overall Score Formula:
```
Score = 100
  - (High Issues × 5)
  - (Medium Issues × 3)
  - (Low Issues × 1)
```

Score is clamped between 0-100.

## 🚢 Deployment

### Frontend (Vercel)
1. Connect GitHub repository
2. Set build command: `npm run build`
3. Set output directory: `dist`
4. Add environment variable: `VITE_API_URL`

### Backend (Render/Railway)
1. Connect GitHub repository
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Add environment variables as needed

## 📝 API Documentation

### POST /analyze

**Request:**
```json
{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "url": "https://example.com",
  "overall_score": 75,
  "summary": {
    "total_checks": 8,
    "passed": 5,
    "failed": 3,
    "high_issues": 2,
    "medium_issues": 1,
    "low_issues": 0
  },
  "checklist": [...],
  "issues": [...],
  "metadata": {...}
}
```

## 🎨 UI Screenshots

### Landing Page
- Hero section with URL input
- Feature cards
- Clean, minimal design

### Dashboard
- Overall score card
- Summary cards (High/Medium/Low issues)
- Interactive checklist
- Issues table

## ⚠️ Limitations

1. **Color Contrast**: Full contrast checking requires CSS parsing (currently flags potential issues)
2. **JavaScript Content**: Cannot analyze dynamically rendered content
3. **Authentication**: Cannot access password-protected sites
4. **Rate Limiting**: No built-in rate limiting (add for production)
5. **ML Models**: Lightweight implementations (not production-grade ML)

## 🔮 Future Scope

- [ ] Full CSS parsing for accurate contrast checking
- [ ] JavaScript execution for dynamic content analysis
- [ ] PDF accessibility analysis
- [ ] Batch URL analysis
- [ ] Export reports (PDF, CSV)
- [ ] Historical tracking and trends
- [ ] Integration with CI/CD pipelines
- [ ] Advanced ML models for better accuracy
- [ ] Multi-language support
- [ ] Custom WCAG rule configuration

## 📄 License

MIT License

## 🤝 Contributing

Contributions welcome! Please read the contributing guidelines first.

## 📧 Support

For issues and questions, please open an issue on GitHub.

---

Built with ❤️ for a more accessible web.
