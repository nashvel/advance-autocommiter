# Auto-Committer GUI - How to Use

## 🎯 Quick Start

### Option 1: Run GUI with Python
```bash
python auto_committer_gui.py
```

### Option 2: Use Standalone Executable
1. Copy `dist/AutoCommitter-GUI.exe` to your project folder
2. Double-click `AutoCommitter-GUI.exe`

## ⚠️ Important for Executable Users

**The executable must be run from your Git project directory!**

### Correct Setup:
1. Copy `AutoCommitter-GUI.exe` to: `c:\Users\user\OneDrive\Desktop\Projects\github-scipt\auto-commiter\`
2. Run it from there

### Why?
The executable needs to find:
- `.git` folder (for Git operations)
- `changes.txt` file (to modify)

## 🎮 Using the GUI

1. **Select Commits**: Choose 10, 20, 30, or enter custom number
2. **Click "Start Commits"**: Begin the auto-commit process
3. **Watch Progress**: Real-time progress bar and logs
4. **Stop Anytime**: Click "Stop" to halt the process

## ✅ Startup Check

When the GUI starts, it will show:
- ✅ Git repository found
- ✅ changes.txt file found
- Working directory path

If you see ❌ errors, make sure you're running from the correct directory!

## 🔧 Building New Executable

If you modify the code:
```bash
python build_exe.py
```
Or double-click `build_exe.bat`
