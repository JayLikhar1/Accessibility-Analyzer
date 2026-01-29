"""
Scoring Engine
Calculates overall accessibility score and metrics
"""

from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


class ScoringEngine:
    """Calculate accessibility scores"""
    
    def __init__(self):
        # Penalty weights
        self.HIGH_PENALTY = 5
        self.MEDIUM_PENALTY = 3
        self.LOW_PENALTY = 1
    
    def calculate(self, checklist: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculate overall score and metrics
        
        Returns:
            Dictionary with score data
        """
        total_checks = len(checklist)
        passed = sum(1 for item in checklist if item["status"] == "pass")
        failed = total_checks - passed
        
        # Count issues by severity (total failed elements)
        high_issues = sum(item.get("failed", 0) for item in checklist if item["severity"] == "High")
        medium_issues = sum(item.get("failed", 0) for item in checklist if item["severity"] == "Medium")
        low_issues = sum(item.get("failed", 0) for item in checklist if item["severity"] == "Low")
        
        # Base score: Start with percentage of checklist items that passed
        # This is the primary metric - each WCAG check is pass/fail
        base_score = (passed / total_checks * 100) if total_checks > 0 else 100
        
        logger.info(f"Scoring: {passed}/{total_checks} checks passed, base_score={base_score}")
        logger.info(f"Issue counts - High: {high_issues}, Medium: {medium_issues}, Low: {low_issues}")
        
        # Apply penalty based on issue density
        # Count total elements checked across all categories
        total_elements = sum(item.get("total", 0) for item in checklist)
        
        logger.info(f"Total elements checked: {total_elements}")
        
        if total_elements > 0:
            # Calculate failure rates
            total_failed_elements = high_issues + medium_issues + low_issues
            failure_rate = total_failed_elements / total_elements
            
            logger.info(f"Failure rate: {failure_rate:.2%} ({total_failed_elements}/{total_elements})")
            
            # Apply severity-weighted penalties based on failure rate
            # Penalties are proportional to failure rate, not absolute counts
            high_penalty_rate = high_issues / total_elements
            medium_penalty_rate = medium_issues / total_elements
            low_penalty_rate = low_issues / total_elements
            
            # Scale penalties (more forgiving)
            high_penalty = high_penalty_rate * 0.25  # Max 25% penalty
            medium_penalty = medium_penalty_rate * 0.12  # Max 12% penalty
            low_penalty = low_penalty_rate * 0.05  # Max 5% penalty
            
            total_penalty = min(high_penalty + medium_penalty + low_penalty, 0.35)  # Cap at 35%
            
            logger.info(f"Penalties - High: {high_penalty:.2%}, Medium: {medium_penalty:.2%}, Low: {low_penalty:.2%}, Total: {total_penalty:.2%}")
            
            # Apply penalty to base score
            overall_score = base_score * (1 - total_penalty)
        else:
            # No elements found (e.g., very simple page), use base score
            logger.info("No elements found, using base score")
            overall_score = base_score
        
        # Ensure score reflects passed checks (minimum floor)
        # If most checks pass, score should be reasonable even with some issues
        if passed > 0:
            min_score = (passed / total_checks) * 60  # At least 60% of passed ratio
            overall_score = max(overall_score, min_score)
        
        # Final clamp to 0-100
        overall_score = max(0, min(100, overall_score))
        
        logger.info(f"Final score: {overall_score}")
        
        # Calculate percentage
        pass_percentage = (passed / total_checks * 100) if total_checks > 0 else 0
        
        return {
            "overall_score": round(overall_score),
            "pass_percentage": round(pass_percentage, 1),
            "total_checks": total_checks,
            "passed": passed,
            "failed": failed,
            "high_issues": high_issues,
            "medium_issues": medium_issues,
            "low_issues": low_issues
        }
