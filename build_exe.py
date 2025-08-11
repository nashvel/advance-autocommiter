#!/usr/bin/env python3
"""
Build script to create executable from the GUI version
"""

import os
import subprocess
import sys

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    try:
        import PyInstaller
        print("PyInstaller is already installed")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller==6.3.0"])

def build_executable():
    """Build the executable using PyInstaller"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    gui_script = os.path.join(script_dir, "auto_committer_gui.py")
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",  # Create a single executable file
        "--windowed",  # Hide console window (GUI app)
        "--name", "AutoCommitter-GUI",  # Name of the executable
        "--icon", "NONE",  # No icon for now
        "--distpath", os.path.join(script_dir, "dist"),  # Output directory
        "--workpath", os.path.join(script_dir, "build"),  # Build directory
        "--specpath", script_dir,  # Spec file location
        gui_script
    ]
    
    print(f"Building executable from {gui_script}...")
    print(f"Command: {' '.join(cmd)}")
    
    try:
        subprocess.check_call(cmd, cwd=script_dir)
        print("\n✅ Executable built successfully!")
        print(f"📁 Location: {os.path.join(script_dir, 'dist', 'AutoCommitter-GUI.exe')}")
        print("\nYou can now run the executable without Python installed!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False
    
    return True

def main():
    """Main function"""
    print("=== Auto-Committer Executable Builder ===\n")
    
    # Install PyInstaller
    install_pyinstaller()
    
    # Build executable
    build_executable()

if __name__ == "__main__":
    main()
