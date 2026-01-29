"""
ML/NLP Analyzer Module
Enhances accessibility analysis with ML-based quality scoring
"""

import re
from typing import Dict, Any, List
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)


class MLAnalyzer:
    """
    Lightweight ML/NLP analyzer for accessibility
    Uses TF-IDF-like features and simple classifiers
    """
    
    def __init__(self):
        # Vague link text patterns
        self.vague_patterns = [
            r"click\s+here",
            r"read\s+more",
            r"^here$",
            r"^link$",
            r"^more$",
            r"^>>+$",
            r"^learn\s+more$",
            r"^see\s+more$"
        ]
        
        # Poor alt text indicators
        self.poor_alt_indicators = [
            "image", "img", "photo", "picture", "pic", "graphic",
            "icon", "logo", "banner", "screenshot"
        ]
    
    def analyze(self, html_content: str, rule_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run ML-enhanced analysis
        
        Returns:
            Dictionary with ML analysis results
        """
        soup = BeautifulSoup(html_content, "html.parser")
        
        ml_results = {
            "alt_text_quality": self._analyze_alt_text_quality(soup, rule_results),
            "link_text_quality": self._analyze_link_text_quality(soup, rule_results),
            "readability": self._calculate_readability(soup),
            "severity_classification": self._classify_severity(rule_results)
        }
        
        return ml_results
    
    def _analyze_alt_text_quality(self, soup: BeautifulSoup, rule_results: Dict[str, Any]) -> Dict[str, Any]:
        """Score alt text quality using NLP heuristics"""
        images = soup.find_all("img")
        scores = []
        
        for img in images:
            alt = img.get("alt", "")
            
            if not alt or alt.strip() == "":
                scores.append(0)
                continue
            
            alt_lower = alt.lower().strip()
            score = 100
            
            # Deduct points for poor indicators
            if any(indicator in alt_lower for indicator in self.poor_alt_indicators):
                score -= 30
            
            # Deduct for very short text
            if len(alt) < 5:
                score -= 20
            elif len(alt) < 10:
                score -= 10
            
            # Deduct for generic patterns
            if re.match(r"^(image|img|photo|picture)\s*\d*$", alt_lower):
                score -= 40
            
            # Bonus for descriptive length
            if len(alt) > 20:
                score += 10
            
            scores.append(max(0, min(100, score)))
        
        avg_score = sum(scores) / len(scores) if scores else 0
        
        return {
            "average_score": round(avg_score, 1),
            "total_images": len(images),
            "scored_images": len(scores)
        }
    
    def _analyze_link_text_quality(self, soup: BeautifulSoup, rule_results: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze link text descriptiveness"""
        links = soup.find_all("a", href=True)
        vague_count = 0
        quality_scores = []
        
        for link in links:
            text = link.get_text(strip=True)
            aria_label = link.get("aria-label", "")
            
            if not text and not aria_label:
                vague_count += 1
                quality_scores.append(0)
                continue
            
            display_text = aria_label if aria_label else text
            display_lower = display_text.lower()
            
            # Check against vague patterns
            is_vague = any(re.search(pattern, display_lower) for pattern in self.vague_patterns)
            
            if is_vague:
                vague_count += 1
                quality_scores.append(30)
            elif len(display_text) < 3:
                quality_scores.append(40)
            else:
                # Score based on length and descriptiveness
                score = min(100, 50 + len(display_text) * 2)
                quality_scores.append(score)
        
        avg_quality = sum(quality_scores) / len(quality_scores) if quality_scores else 0
        
        return {
            "vague_links": vague_count,
            "average_quality": round(avg_quality, 1),
            "total_links": len(links)
        }
    
    def _calculate_readability(self, soup: BeautifulSoup) -> Dict[str, Any]:
        """
        Calculate basic readability score (simplified Flesch-like)
        """
        # Extract text content
        text_elements = soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "li"])
        text_content = " ".join([elem.get_text(strip=True) for elem in text_elements])
        
        if not text_content:
            return {
                "score": 0,
                "level": "Unknown",
                "word_count": 0
            }
        
        # Simple metrics
        words = text_content.split()
        sentences = re.split(r'[.!?]+', text_content)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        word_count = len(words)
        sentence_count = len(sentences)
        avg_sentence_length = word_count / sentence_count if sentence_count > 0 else 0
        
        # Simplified readability score
        # Lower avg sentence length = higher readability
        readability_score = max(0, min(100, 100 - (avg_sentence_length * 2)))
        
        # Determine level
        if readability_score >= 70:
            level = "Easy"
        elif readability_score >= 50:
            level = "Moderate"
        else:
            level = "Difficult"
        
        return {
            "score": round(readability_score, 1),
            "level": level,
            "word_count": word_count,
            "sentence_count": sentence_count,
            "avg_sentence_length": round(avg_sentence_length, 1)
        }
    
    def _classify_severity(self, rule_results: Dict[str, Any]) -> Dict[str, int]:
        """
        Classify issues by severity based on WCAG impact
        """
        severity_counts = {"High": 0, "Medium": 0, "Low": 0}
        
        # High severity: Missing alt text, missing form labels, missing lang
        high_checks = ["images", "forms", "lang_attribute"]
        for check in high_checks:
            if check in rule_results:
                failed = rule_results[check].get("failed", 0)
                severity_counts["High"] += failed
        
        # Medium severity: Heading hierarchy, button accessibility
        medium_checks = ["headings", "buttons"]
        for check in medium_checks:
            if check in rule_results:
                failed = rule_results[check].get("failed", 0)
                severity_counts["Medium"] += failed
        
        # Low severity: Link text, color contrast (often needs manual review)
        low_checks = ["links", "color_contrast"]
        for check in low_checks:
            if check in rule_results:
                failed = rule_results[check].get("failed", 0)
                severity_counts["Low"] += min(failed, 5)  # Cap low severity
        
        return severity_counts
