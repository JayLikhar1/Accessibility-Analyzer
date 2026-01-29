"""
FastAPI Backend for Accessibility Analyzer
Main API endpoint for analyzing website accessibility
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging
import os
from urllib.parse import urlparse

from analyzer.scraper import WebScraper
from analyzer.rules import RuleBasedAnalyzer
from analyzer.ml_analyzer import MLAnalyzer
from analyzer.checklist import ChecklistGenerator
from analyzer.scorer import ScoringEngine

# --------------------------------------------------
# Logging
# --------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --------------------------------------------------
# FastAPI app
# --------------------------------------------------
app = FastAPI(
    title="Accessibility Analyzer API",
    description="AI-powered WCAG accessibility analysis for websites",
    version="1.0.0"
)

# --------------------------------------------------
# CORS
# --------------------------------------------------
cors_origins = os.getenv("CORS_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if cors_origins == ["*"] else [o.strip() for o in cors_origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Models
# --------------------------------------------------
class AnalyzeRequest(BaseModel):
    url: str   # ✅ relaxed from HttpUrl


class AnalyzeResponse(BaseModel):
    url: str
    overall_score: int
    summary: dict
    checklist: list
    issues: list
    metadata: dict

# --------------------------------------------------
# Routes
# --------------------------------------------------
@app.get("/")
async def root():
    return {"message": "Accessibility Analyzer API", "version": "1.0.0"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze_website(request: AnalyzeRequest):
    try:
        # ------------------------------------------
        # URL NORMALIZATION & VALIDATION (IMPORTANT)
        # ------------------------------------------
        url_str = request.url.strip()

        if not url_str:
            raise HTTPException(status_code=400, detail="URL cannot be empty")

        if not url_str.startswith(("http://", "https://")):
            url_str = "https://" + url_str

        parsed = urlparse(url_str)
        if not parsed.netloc:
            raise HTTPException(status_code=400, detail="Invalid URL format")

        logger.info(f"Analyzing URL: {url_str}")

        # ------------------------------------------
        # Step 1: Scrape website
        # ------------------------------------------
        scraper = WebScraper()
        html_content, metadata = scraper.scrape(url_str)

        if not html_content:
            raise HTTPException(
                status_code=400,
                detail="Failed to fetch website content. Website may block bots or require JavaScript."
            )

        # ------------------------------------------
        # Step 2: Rule-based analysis
        # ------------------------------------------
        rule_analyzer = RuleBasedAnalyzer()
        rule_results = rule_analyzer.analyze(html_content, url_str)

        # ------------------------------------------
        # Step 3: ML/NLP analysis
        # ------------------------------------------
        ml_analyzer = MLAnalyzer()
        ml_results = ml_analyzer.analyze(html_content, rule_results)

        # ------------------------------------------
        # Step 4: Checklist
        # ------------------------------------------
        checklist_gen = ChecklistGenerator()
        checklist = checklist_gen.generate(rule_results, ml_results)

        # ------------------------------------------
        # Step 5: Scoring
        # ------------------------------------------
        scorer = ScoringEngine()
        score_data = scorer.calculate(checklist)

        # ------------------------------------------
        # Step 6: Compile issues
        # ------------------------------------------
        issues = [
            {
                "check": item["check"],
                "wcag": item["wcag"],
                "severity": item["severity"],
                "fix": item["fix"],
                "count": item.get("count", 0)
            }
            for item in checklist
            if item["status"] == "fail"
        ]

        severity_order = {"High": 0, "Medium": 1, "Low": 2}
        issues.sort(key=lambda x: severity_order.get(x["severity"], 3))

        response = AnalyzeResponse(
            url=url_str,
            overall_score=score_data["overall_score"],
            summary={
                "total_checks": len(checklist),
                "passed": score_data["passed"],
                "failed": score_data["failed"],
                "high_issues": score_data["high_issues"],
                "medium_issues": score_data["medium_issues"],
                "low_issues": score_data["low_issues"]
            },
            checklist=checklist,
            issues=issues,
            metadata={
                "title": metadata.get("title", "Unknown"),
                "timestamp": metadata.get("timestamp"),
                "html_size": len(html_content)
            }
        )

        logger.info(f"Analysis complete. Score: {score_data['overall_score']}")
        return response

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Unexpected error", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Internal server error during accessibility analysis"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
