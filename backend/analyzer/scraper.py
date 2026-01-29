"""
Web Scraper Module
Safely fetches and parses HTML content from URLs
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import ipaddress
import re
from datetime import datetime
from typing import Tuple, Optional
import logging

logger = logging.getLogger(__name__)


class WebScraper:
    """Safely scrape websites with SSRF protection and timeout handling"""
    
    MAX_CONTENT_SIZE = 10 * 1024 * 1024  # 10MB
    TIMEOUT = 15  # seconds
    MAX_REDIRECTS = 5
    
    # Blocked IP ranges
    BLOCKED_IPS = [
        ipaddress.ip_network("127.0.0.0/8"),      # localhost
        ipaddress.ip_network("10.0.0.0/8"),      # private
        ipaddress.ip_network("172.16.0.0/12"),   # private
        ipaddress.ip_network("192.168.0.0/16"),  # private
        ipaddress.ip_network("169.254.0.0/16"),  # link-local
    ]
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 AccessibilityAnalyzer/1.0"
        })
    
    def _is_blocked_url(self, url: str) -> bool:
        """Check if URL should be blocked (SSRF protection)"""
        try:
            parsed = urlparse(url)
            hostname = parsed.hostname
            
            if not hostname:
                return True
            
            # Block localhost variants
            if hostname in ["localhost", "127.0.0.1", "0.0.0.0"]:
                return True
            
            # Try to resolve IP
            try:
                import socket
                ip = socket.gethostbyname(hostname)
                ip_obj = ipaddress.ip_address(ip)
                
                # Check against blocked ranges
                for blocked_net in self.BLOCKED_IPS:
                    if ip_obj in blocked_net:
                        return True
            except:
                pass
            
            # Block file:// and other dangerous schemes
            if parsed.scheme not in ["http", "https"]:
                return True
            
            return False
            
        except Exception as e:
            logger.warning(f"URL validation error: {e}")
            return True
    
    def scrape(self, url: str) -> Tuple[Optional[str], dict]:
        """
        Scrape website and return HTML content with metadata
        
        Returns:
            Tuple of (html_content, metadata)
        """
        metadata = {
            "timestamp": datetime.utcnow().isoformat(),
            "title": None,
            "url": url
        }
        
        try:
            # Validate URL
            if self._is_blocked_url(url):
                raise ValueError("URL is blocked for security reasons (localhost/private IP)")
            
            # Fetch content
            logger.info(f"Fetching: {url}")
            response = self.session.get(
                url,
                timeout=self.TIMEOUT,
                allow_redirects=True,
                stream=True
            )
            response.raise_for_status()
            
            # Check content size
            content_length = response.headers.get("Content-Length")
            if content_length and int(content_length) > self.MAX_CONTENT_SIZE:
                raise ValueError(f"Content too large: {content_length} bytes")
            
            # Read content with size limit
            content = b""
            for chunk in response.iter_content(chunk_size=8192):
                content += chunk
                if len(content) > self.MAX_CONTENT_SIZE:
                    raise ValueError("Content exceeds maximum size")
            
            html_content = content.decode("utf-8", errors="ignore")
            
            # Parse with BeautifulSoup
            soup = BeautifulSoup(html_content, "html.parser")
            
            # Extract metadata
            title_tag = soup.find("title")
            if title_tag:
                metadata["title"] = title_tag.get_text(strip=True)
            
            # Return cleaned HTML
            return str(soup), metadata
            
        except requests.exceptions.Timeout:
            logger.error(f"Timeout fetching {url}")
            raise ValueError("Request timed out. The website may be slow or unreachable.")
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error: {e}")
            raise ValueError(f"Failed to fetch website: {str(e)}")
        except Exception as e:
            logger.error(f"Scraping error: {e}")
            raise ValueError(f"Error scraping website: {str(e)}")
