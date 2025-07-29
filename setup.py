#!/usr/bin/env python3
"""
Setup script for Auto-Committer
Initializes git repository and installs dependencies
"""

import os
import subprocess
import sys

def run_command(command, cwd=None):
    """Run a command and return success status"""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, check=True, 
                              capture_output=True, text=True)
        print(f"✅ {command}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {command}")
        print(f"Error: {e.stderr}")
        return False

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("🚀 Setting up Auto-Committer...")
    
    # Install dependencies
    print("\n📦 Installing dependencies...")
    if not run_command("pip install -r requirements.txt", cwd=script_dir):
        print("Failed to install dependencies")
        return False
    
    # Initialize git repository if not exists
    print("\n🔧 Setting up Git repository...")
    if not os.path.exists(os.path.join(script_dir, '.git')):
        if not run_command("git init", cwd=script_dir):
            return False
        
        # Add initial files
        if not run_command("git add .", cwd=script_dir):
            return False
        
        if not run_command('git commit -m "Initial commit - Auto-Committer setup"', cwd=script_dir):
            return False
        
        print("\n🔗 To connect to GitHub:")
        print("1. Create a new repository on GitHub")
        print("2. Run: git remote add origin <your-github-repo-url>")
        print("3. Run: git branch -M main")
        print("4. Run: git push -u origin main")
    else:
        print("Git repository already exists")
    
    print("\n✅ Setup complete!")
    print("\nUsage:")
    print("  python auto_committer.py --run-now    # Test run immediately")
    print("  python auto_committer.py --schedule   # Run with daily scheduler at 6 AM")

if __name__ == "__main__":
    main()
