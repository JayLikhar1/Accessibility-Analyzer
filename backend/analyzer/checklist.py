"""
Checklist Generator
Converts analysis results into WCAG checklist format
"""

from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


class ChecklistGenerator:
    """Generate accessibility checklist from analysis results"""
    
    WCAG_MAPPING = {
        "images": {
            "check": "Images have alt text",
            "wcag": "1.1.1",
            "description": "All images must have descriptive alt text or be marked as decorative"
        },
        "forms": {
            "check": "Forms have labels",
            "wcag": "1.3.1, 3.3.2",
            "description": "All form inputs must have associated labels"
        },
        "headings": {
            "check": "Headings are structured",
            "wcag": "1.3.1",
            "description": "Headings must follow proper hierarchy (h1 -> h2 -> h3, etc.)"
        },
        "links": {
            "check": "Links are descriptive",
            "wcag": "2.4.4",
            "description": "Link text should be descriptive and not vague"
        },
        "color_contrast": {
            "check": "Color contrast passes WCAG",
            "wcag": "1.4.3",
            "description": "Text must meet minimum contrast ratios"
        },
        "lang_attribute": {
            "check": "Page has lang attribute",
            "wcag": "3.1.1",
            "description": "HTML element must have lang attribute"
        },
        "buttons": {
            "check": "Buttons are accessible",
            "wcag": "4.1.2",
            "description": "Buttons must have accessible names"
        },
        "aria_labels": {
            "check": "ARIA labels are properly used",
            "wcag": "4.1.2",
            "description": "ARIA attributes must be used correctly"
        }
    }
    
    def generate(self, rule_results: Dict[str, Any], ml_results: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Generate checklist from analysis results
        
        Returns:
            List of checklist items
        """
        checklist = []
        
        for check_key, check_info in self.WCAG_MAPPING.items():
            if check_key not in rule_results:
                continue
            
            result = rule_results[check_key]
            total = result.get("total", 0)
            failed = result.get("failed", 0)
            passed = result.get("passed", 0)
            
            # Determine status
            if total == 0:
                status = "pass"  # No elements to check
            elif failed == 0:
                status = "pass"
            else:
                status = "fail"
            
            # Determine severity
            severity = self._determine_severity(check_key, failed)
            
            # Generate fix suggestion
            fix = self._generate_fix(check_key, result, ml_results)
            
            checklist_item = {
                "check": check_info["check"],
                "wcag": check_info["wcag"],
                "description": check_info["description"],
                "status": status,
                "severity": severity,
                "total": total,
                "passed": passed,
                "failed": failed,
                "count": failed,
                "fix": fix
            }
            
            checklist.append(checklist_item)
        
        return checklist
    
    def _determine_severity(self, check_key: str, failed_count: int) -> str:
        """Determine severity based on check type and failure count"""
        # High severity checks
        high_severity_checks = ["images", "forms", "lang_attribute"]
        if check_key in high_severity_checks:
            return "High"
        
        # Medium severity checks
        medium_severity_checks = ["headings", "buttons", "aria_labels"]
        if check_key in medium_severity_checks:
            return "Medium"
        
        # Low severity checks (often need manual review)
        return "Low"
    
    def _generate_fix(self, check_key: str, result: Dict[str, Any], ml_results: Dict[str, Any]) -> str:
        """Generate fix suggestion based on check type"""
        issues = result.get("issues", [])
        
        if not issues:
            return "No issues found"
        
        # Get first issue as example
        first_issue = issues[0] if issues else {}
        fix_suggestion = first_issue.get("fix", "Review and fix accessibility issues")
        
        # Enhance with ML insights
        if check_key == "images" and "alt_text_quality" in ml_results:
            quality = ml_results["alt_text_quality"].get("average_score", 0)
            if quality < 50:
                fix_suggestion += ". Consider improving alt text descriptiveness."
        
        if check_key == "links" and "link_text_quality" in ml_results:
            vague_count = ml_results["link_text_quality"].get("vague_links", 0)
            if vague_count > 0:
                fix_suggestion += f" Replace {vague_count} vague link texts with descriptive alternatives."
        
        return fix_suggestion
