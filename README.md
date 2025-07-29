# Auto-Committer Script

A Python script that automatically modifies itself 100 times, commits each change to GitHub, and runs on a daily schedule at 6 AM.

## Features

- 🔄 Self-modifying script that adds timestamped comments
- 📝 Automatic Git commits and pushes after each modification
- ⏰ Scheduled execution at 6 AM daily
- 🎯 Configurable number of commits (default: 100)
- 📊 Progress tracking and error handling

## Setup

1. **Install dependencies:**
   ```bash
   python setup.py
   ```

2. **Connect to GitHub repository:**
   ```bash
   git remote add origin https://github.com/nashvel/advance-autocommiter.git
   git branch -M main
   git push -u origin main
   ```

## Usage

### Run immediately (for testing):
```bash
python auto_committer.py --run-now
```

### Run with daily scheduler at 6 AM:
```bash
python auto_committer.py --schedule
```

## How it works

1. The script modifies itself by adding timestamped comments
2. After each modification, it commits the change to Git
3. Pushes the commit to GitHub
4. Repeats this process 100 times
5. Can run on schedule or immediately

## Requirements

- Python 3.6+
- Git configured with GitHub credentials
- `schedule` library (installed via requirements.txt)

## File Structure

```
auto-commiter/
├── auto_committer.py    # Main script
├── setup.py            # Setup and initialization
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Notes

- Ensure Git is configured with your GitHub credentials
- The script will create 100 commits, so use a dedicated repository
- Press Ctrl+C to stop the scheduler
- Each modification adds a unique timestamped comment to the script
# advance-autocommiter
