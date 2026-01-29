"""
Rule-Based Accessibility Analyzer
Implements WCAG 2.1 compliance checks
"""

from bs4 import BeautifulSoup
from typing import List, Dict, Any
import re
import logging

logger = logging.getLogger(__name__)


class RuleBasedAnalyzer:
    """Rule-based WCAG accessibility checker"""
    
    def __init__(self):
        self.min_contrast_ratio_aa = 4.5  # WCAG AA for normal text
        self.min_contrast_ratio_large_aa = 3.0  # WCAG AA for large text
    
    def analyze(self, html_content: str, url: str) -> Dict[str, Any]:
        """
        Run all accessibility checks
        
        Returns:
            Dictionary with check results
        """
        soup = BeautifulSoup(html_content, "html.parser")
        
        results = {
            "images": self._check_images(soup),
            "forms": self._check_forms(soup),
            "headings": self._check_headings(soup),
            "links": self._check_links(soup),
            "color_contrast": self._check_color_contrast(soup),
            "lang_attribute": self._check_lang_attribute(soup),
            "buttons": self._check_buttons(soup),
            "aria_labels": self._check_aria_labels(soup),
        }
        
        return results
    
    def _check_images(self, soup: BeautifulSoup) -> Dict[str, Any]:
        """Check WCAG 1.1.1: Images must have alt text"""
        images = soup.find_all("img")
        issues = []
        passed = 0
        
        for img in images:
            alt = img.get("alt")
            aria_hidden = img.get("aria-hidden", "").lower() == "true"
            role = img.get("role", "").lower()
            
            # Decorative images (aria-hidden or role=presentation) are OK without alt
            if aria_hidden or role == "presentation":
                passed += 1
                continue
            
            # Missing alt text
            if alt is None:
                issues.append({
                    "element": str(img)[:100],
                    "issue": "Missing alt attribute",
                    "fix": "Add alt='description' attribute to img tag"
                })
            # Empty alt text (should be descriptive or decorative)
            elif alt.strip() == "":
                issues.append({
                    "element": str(img)[:100],
                    "issue": "Empty alt text",
                    "fix": "Add descriptive alt text or set alt='' if decorative"
                })
            # Poor alt text (too short, generic)
            elif len(alt.strip()) < 3 or alt.lower() in ["image", "img", "photo", "picture"]:
                issues.append({
                    "element": str(img)[:100],
                    "issue": "Poor alt text quality",
                    "fix": f"Replace '{alt}' with descriptive alt text"
                })
            else:
                passed += 1
        
        return {
            "total": len(images),
            "passed": passed,
            "failed": len(issues),
            "issues": issues
        }
    
    def _check_forms(self, soup: BeautifulSoup) -> Dict[str, Any]:
        """Check WCAG 1.3.1, 3.3.2: Forms must have labels"""
        inputs = soup.find_all(["input", "textarea", "select"])
        issues = []
        passed = 0
        
        for inp in inputs:
            input_type = inp.get("type", "").lower()
            
            # Skip hidden inputs
            if input_type == "hidden":
                continue
            
            # Skip submit/reset buttons
            if input_type in ["submit", "reset", "button"]:
                continue
            
            # Check for label
            has_label = False
            
            # Check for id and associated label
            input_id = inp.get("id")
            if input_id:
                label = soup.find("label", {"for": input_id})
                if label:
                    has_label = True
            
            # Check for aria-label
            if inp.get("aria-label"):
                has_label = True
            
            # Check for aria-labelledby
            if inp.get("aria-labelledby"):
                has_label = True
            
            # Check if wrapped in label
            if inp.find_parent("label"):
                has_label = True
            
            if not has_label:
                issues.append({
                    "element": str(inp)[:100],
                    "issue": "Form input missing label",
                    "fix": "Add <label> element or aria-label attribute"
                })
            else:
                passed += 1
        
        return {
            "total": len(inputs),
            "passed": passed,
            "failed": len(issues),
            "issues": issues
        }
    
    def _check_headings(self, soup: BeautifulSoup) -> Dict[str, Any]:
        """Check WCAG 1.3.1: Proper heading hierarchy"""
        headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
        issues = []
        passed = 0
        last_level = 0
        
        # Check for h1
        h1_count = len(soup.find_all("h1"))
        if h1_count == 0:
            issues.append({
                "element": "Page structure",
                "issue": "Missing h1 heading",
                "fix": "Add at least one h1 heading to describe page content"
            })
        elif h1_count > 1:
            issues.append({
                "element": "Page structure",
                "issue": "Multiple h1 headings",
                "fix": "Use only one h1 per page for main content"
            })
        
        # Check hierarchy
        for heading in headings:
            level = int(heading.name[1])
            
            # Skip if first heading
            if last_level == 0:
                last_level = level
                passed += 1
                continue
            
            # Check for skipped levels (e.g., h1 -> h3)
            if level > last_level + 1:
                issues.append({
                    "element": str(heading)[:100],
                    "issue": f"Heading hierarchy skipped (h{last_level} -> h{level})",
                    "fix": f"Use h{last_level + 1} instead of h{level}"
                })
            else:
                passed += 1
            
            last_level = level
        
        return {
            "total": len(headings),
            "passed": passed,
            "failed": len(issues),
            "issues": issues
        }
    
    def _check_links(self, soup: BeautifulSoup) -> Dict[str, Any]:
        """Check WCAG 2.4.4: Link text should be descriptive"""
        links = soup.find_all("a", href=True)
        issues = []
        passed = 0
        
        vague_texts = ["click here", "read more", "here", "link", "more", ">>", ">>>"]
        
        for link in links:
            text = link.get_text(strip=True).lower()
            aria_label = link.get("aria-label", "").lower()
            
            # Skip if has aria-label
            if aria_label:
                passed += 1
                continue
            
            # Check for empty or vague text
            if not text or text in vague_texts:
                issues.append({
                    "element": str(link)[:100],
                    "issue": f"Vague or empty link text: '{text}'",
                    "fix": "Use descriptive link text or add aria-label"
                })
            # Check for image-only links without alt
            elif link.find("img") and not link.find("img").get("alt"):
                issues.append({
                    "element": str(link)[:100],
                    "issue": "Image link missing alt text",
                    "fix": "Add alt text to image or descriptive link text"
                })
            else:
                passed += 1
        
        return {
            "total": len(links),
            "passed": passed,
            "failed": len(issues),
            "issues": issues
        }
    
    def _check_color_contrast(self, soup: BeautifulSoup) -> Dict[str, Any]:
        """Check WCAG 1.4.3: Color contrast (basic check)"""
        # This is a simplified check - full contrast requires CSS parsing
        # We'll flag potential issues based on inline styles
        elements_with_color = soup.find_all(style=re.compile(r"color|background"))
        issues = []
        passed = 0
        
        # Note: Full contrast checking requires CSS parsing and color calculation
        # This is a placeholder that flags elements with inline color styles
        for elem in elements_with_color:
            style = elem.get("style", "")
            if "color:" in style.lower() or "background" in style.lower():
                # Flag for manual review (we can't calculate contrast without CSS)
                issues.append({
                    "element": str(elem)[:100],
                    "issue": "Inline color styles detected",
                    "fix": "Ensure text meets WCAG AA contrast ratio (4.5:1 for normal text)"
                })
        
        # Also check for low contrast indicators
        text_elements = soup.find_all(["p", "span", "div", "a", "li"])
        for elem in text_elements[:50]:  # Sample first 50
            classes = elem.get("class", [])
            class_str = " ".join(classes).lower()
            
            # Common low-contrast class names
            if any(word in class_str for word in ["light", "muted", "gray", "grey", "fade"]):
                issues.append({
                    "element": str(elem)[:100],
                    "issue": "Potential low contrast (class-based)",
                    "fix": "Verify text meets WCAG AA contrast ratio"
                })
        
        passed = max(0, len(text_elements) - len(issues))
        
        return {
            "total": len(elements_with_color) + len(text_elements[:50]),
            "passed": passed,
            "failed": len(issues),
            "issues": issues[:10]  # Limit issues
        }
    
    def _check_lang_attribute(self, soup: BeautifulSoup) -> Dict[str, Any]:
        """Check WCAG 3.1.1: Language attribute"""
        html_tag = soup.find("html")
        issues = []
        
        if not html_tag or not html_tag.get("lang"):
            issues.append({
                "element": "<html> tag",
                "issue": "Missing lang attribute",
                "fix": "Add lang='en' (or appropriate language) to <html> tag"
            })
        
        return {
            "total": 1,
            "passed": 1 if not issues else 0,
            "failed": len(issues),
            "issues": issues
        }
    
    def _check_buttons(self, soup: BeautifulSoup) -> Dict[str, Any]:
        """Check WCAG 4.1.2: Button accessibility"""
        buttons = soup.find_all(["button", "input"], type=["button", "submit"])
        issues = []
        passed = 0
        
        for btn in buttons:
            # Check for accessible name
            has_name = False
            
            if btn.get_text(strip=True):
                has_name = True
            if btn.get("aria-label"):
                has_name = True
            if btn.get("aria-labelledby"):
                has_name = True
            if btn.get("title"):
                has_name = True
            
            # Image buttons need alt
            img = btn.find("img")
            if img and not img.get("alt"):
                issues.append({
                    "element": str(btn)[:100],
                    "issue": "Button with image missing alt text",
                    "fix": "Add alt text to image or aria-label to button"
                })
            elif not has_name:
                issues.append({
                    "element": str(btn)[:100],
                    "issue": "Button missing accessible name",
                    "fix": "Add text content, aria-label, or aria-labelledby"
                })
            else:
                passed += 1
        
        return {
            "total": len(buttons),
            "passed": passed,
            "failed": len(issues),
            "issues": issues
        }
    
    def _check_aria_labels(self, soup: BeautifulSoup) -> Dict[str, Any]:
        """Check for proper ARIA usage"""
        # Check for aria-hidden without proper handling
        aria_hidden = soup.find_all(attrs={"aria-hidden": "true"})
        issues = []
        
        # Check for interactive elements that are aria-hidden
        for elem in aria_hidden:
            if elem.name in ["a", "button", "input", "select", "textarea"]:
                issues.append({
                    "element": str(elem)[:100],
                    "issue": "Interactive element with aria-hidden='true'",
                    "fix": "Remove aria-hidden or make element non-interactive"
                })
        
        return {
            "total": len(aria_hidden),
            "passed": len(aria_hidden) - len(issues),
            "failed": len(issues),
            "issues": issues
        }
