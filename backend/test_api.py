"""
Simple test script to verify the API is working
Run this after starting the backend server
"""

import requests
import json

API_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    print("Testing health endpoint...")
    try:
        response = requests.get(f"{API_URL}/health")
        print(f"✓ Health check: {response.json()}")
        return True
    except Exception as e:
        print(f"✗ Health check failed: {e}")
        return False

def test_analyze():
    """Test analyze endpoint with example.com"""
    print("\nTesting analyze endpoint...")
    try:
        response = requests.post(
            f"{API_URL}/analyze",
            json={"url": "https://example.com"},
            timeout=30
        )
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Analysis successful!")
            print(f"  URL: {data['url']}")
            print(f"  Score: {data['overall_score']}")
            print(f"  Checks: {data['summary']['total_checks']}")
            print(f"  Passed: {data['summary']['passed']}")
            print(f"  Failed: {data['summary']['failed']}")
            return True
        else:
            print(f"✗ Analysis failed: {response.status_code}")
            print(f"  Response: {response.text}")
            return False
    except Exception as e:
        print(f"✗ Analysis failed: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("Accessibility Analyzer API Test")
    print("=" * 50)
    
    health_ok = test_health()
    if health_ok:
        test_analyze()
    else:
        print("\n⚠ Backend server may not be running.")
        print("Start it with: python main.py")
