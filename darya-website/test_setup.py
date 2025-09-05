#!/usr/bin/env python3
"""
Test script to verify the Darya Bernard website setup
"""

import os
import sys
import json

def test_directories():
    """Test if all required directories exist"""
    required_dirs = [
        'templates',
        'static',
        'static/videos',
        'static/photos/people',
        'static/photos/places',
        'static/photos/sports'
    ]
    
    print("Testing directory structure...")
    for directory in required_dirs:
        if os.path.exists(directory):
            print(f"✅ {directory}/ exists")
        else:
            print(f"❌ {directory}/ missing")
            return False
    return True

def test_templates():
    """Test if all required templates exist"""
    required_templates = [
        'templates/base.html',
        'templates/index.html',
        'templates/art.html',
        'templates/corporate.html',
        'templates/social.html',
        'templates/people.html',
        'templates/places.html',
        'templates/sports.html',
        'templates/admin.html',
        'templates/admin_login.html'
    ]
    
    print("\nTesting template files...")
    for template in required_templates:
        if os.path.exists(template):
            print(f"✅ {template} exists")
        else:
            print(f"❌ {template} missing")
            return False
    return True

def test_app_file():
    """Test if the main app file exists and is valid"""
    print("\nTesting app.py...")
    if os.path.exists('app.py'):
        print("✅ app.py exists")
        try:
            with open('app.py', 'r') as f:
                content = f.read()
                if 'Flask' in content and 'app = Flask' in content:
                    print("✅ app.py appears to be a valid Flask app")
                    return True
                else:
                    print("❌ app.py doesn't appear to be a valid Flask app")
                    return False
        except Exception as e:
            print(f"❌ Error reading app.py: {e}")
            return False
    else:
        print("❌ app.py missing")
        return False

def test_requirements():
    """Test if requirements.txt exists"""
    print("\nTesting requirements.txt...")
    if os.path.exists('requirements.txt'):
        print("✅ requirements.txt exists")
        try:
            with open('requirements.txt', 'r') as f:
                content = f.read()
                if 'Flask' in content:
                    print("✅ Flask is listed in requirements")
                    return True
                else:
                    print("❌ Flask not found in requirements")
                    return False
        except Exception as e:
            print(f"❌ Error reading requirements.txt: {e}")
            return False
    else:
        print("❌ requirements.txt missing")
        return False

def main():
    """Run all tests"""
    print("Darya Bernard Website - Setup Test")
    print("=" * 40)
    
    tests = [
        test_directories,
        test_templates,
        test_app_file,
        test_requirements
    ]
    
    all_passed = True
    for test in tests:
        if not test():
            all_passed = False
    
    print("\n" + "=" * 40)
    if all_passed:
        print("🎉 All tests passed! The website is ready to run.")
        print("\nTo start the website:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Run the app: python app.py")
        print("3. Visit: http://localhost:5000")
        print("4. Admin panel: http://localhost:5000/admin")
    else:
        print("❌ Some tests failed. Please check the issues above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
