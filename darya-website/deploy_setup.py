#!/usr/bin/env python3
"""
Deployment setup script for Darya Bernard's website
This script helps prepare the website for deployment
"""

import os
import json
import secrets
import string

def generate_secret_key():
    """Generate a secure secret key"""
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(32))

def create_env_file():
    """Create a .env file with environment variables"""
    env_content = f"""# Darya Bernard Website Environment Variables
# Copy these to your deployment platform

SECRET_KEY={generate_secret_key()}
ADMIN_PASSWORD=darya_secure_admin_2025
PORT=8000
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("✅ Created .env file with environment variables")
    print("📝 Remember to set these in your deployment platform!")

def check_files():
    """Check if all required files exist"""
    required_files = [
        'app.py',
        'requirements.txt',
        'Procfile',
        'runtime.txt',
        'gunicorn.conf.py',
        'templates/',
        'static/',
        'website_data.json'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    else:
        print("✅ All required files present")
        return True

def update_requirements():
    """Ensure requirements.txt has all necessary packages"""
    with open('requirements.txt', 'r') as f:
        content = f.read()
    
    if 'gunicorn' not in content:
        with open('requirements.txt', 'a') as f:
            f.write('\ngunicorn==21.2.0\n')
        print("✅ Added gunicorn to requirements.txt")
    else:
        print("✅ requirements.txt is up to date")

def create_gitignore():
    """Create .gitignore file"""
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
env.bak/
venv.bak/

# Environment variables
.env
.env.local
.env.production

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Database
*.db
*.sqlite3

# Temporary files
*.tmp
*.temp
"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)
    
    print("✅ Created .gitignore file")

def main():
    print("🚀 Darya Bernard Website - Deployment Setup")
    print("=" * 50)
    
    # Check files
    if not check_files():
        print("\n❌ Please ensure all required files are present before deploying")
        return
    
    # Update requirements
    update_requirements()
    
    # Create .gitignore
    create_gitignore()
    
    # Create .env file
    create_env_file()
    
    print("\n🎉 Setup complete! Your website is ready for deployment.")
    print("\n📋 Next steps:")
    print("1. Choose a deployment platform (Railway, Render, or DigitalOcean)")
    print("2. Create a Git repository and push your code")
    print("3. Set up the deployment with the environment variables from .env")
    print("4. Deploy and share the URL with your sister!")
    print("\n📖 See DEPLOYMENT_GUIDE.md for detailed instructions")

if __name__ == "__main__":
    main()
