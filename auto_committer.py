#!/usr/bin/env python3
"""
Auto-Committer Script
Modifies itself 100 times and commits each change to GitHub.
Runs automatically at 6 AM daily.
"""

import os
import sys
import time
import random
import subprocess
from datetime import datetime
import schedule

class AutoCommitter:
    def __init__(self):
        self.script_path = os.path.abspath(__file__)
        self.commit_count = 0
        self.max_commits = 100
        
    def modify_self(self):
        """Modify this script file by adding a comment with timestamp"""
        try:
            with open(self.script_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add a timestamp comment at the end
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            random_num = random.randint(1000, 9999)
            new_comment = f"\n# Auto-generated comment {self.commit_count + 1}: {timestamp} - Random: {random_num}"
            
            # Append the comment
            modified_content = content + new_comment
            
            with open(self.script_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
                
            print(f"✅ Modified script (change #{self.commit_count + 1})")
            return True
            
        except Exception as e:
            print(f"❌ Error modifying script: {e}")
            return False
    
    def git_commit_and_push(self):
        """Commit and push changes to GitHub"""
        try:
            # Get current directory
            repo_dir = os.path.dirname(self.script_path)
            
            # Add changes
            subprocess.run(['git', 'add', '.'], cwd=repo_dir, check=True)
            
            # Commit with message
            commit_msg = f"Auto-commit #{self.commit_count + 1} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            subprocess.run(['git', 'commit', '-m', commit_msg], cwd=repo_dir, check=True)
            
            # Push to GitHub
            subprocess.run(['git', 'push'], cwd=repo_dir, check=True)
            
            print(f"✅ Committed and pushed change #{self.commit_count + 1}")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Git error: {e}")
            return False
        except Exception as e:
            print(f"❌ Error in git operations: {e}")
            return False
    
    def run_commit_cycle(self):
        """Run the complete cycle of 100 modifications and commits"""
        print(f"🚀 Starting auto-commit cycle at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"📁 Working on: {self.script_path}")
        
        success_count = 0
        
        for i in range(self.max_commits):
            self.commit_count = i
            
            print(f"\n--- Processing change {i + 1}/{self.max_commits} ---")
            
            # Modify the script
            if self.modify_self():
                # Wait a moment to ensure file system updates
                time.sleep(1)
                
                # Commit and push
                if self.git_commit_and_push():
                    success_count += 1
                    print(f"✅ Successfully completed change {i + 1}")
                else:
                    print(f"❌ Failed to commit change {i + 1}")
            else:
                print(f"❌ Failed to modify script for change {i + 1}")
            
            # Small delay between operations
            time.sleep(2)
        
        print(f"\n🎉 Completed! Successfully processed {success_count}/{self.max_commits} changes")
        print(f"⏰ Finished at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    def setup_scheduler(self):
        """Set up the scheduler to run at 6 AM daily"""
        schedule.every().day.at("06:00").do(self.run_commit_cycle)
        
        print("📅 Scheduler set up to run at 6:00 AM daily")
        print("⏰ Waiting for next scheduled run...")
        print("Press Ctrl+C to stop the scheduler")
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            print("\n👋 Scheduler stopped by user")

def main():
    """Main function"""
    committer = AutoCommitter()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--run-now":
            # Run immediately for testing
            committer.run_commit_cycle()
        elif sys.argv[1] == "--schedule":
            # Run with scheduler
            committer.setup_scheduler()
        else:
            print("Usage:")
            print("  python auto_committer.py --run-now    # Run immediately")
            print("  python auto_committer.py --schedule   # Run with daily scheduler")
    else:
        print("🤖 Auto-Committer Script")
        print("This script modifies itself 100 times and commits each change to GitHub.")
        print("\nUsage:")
        print("  python auto_committer.py --run-now    # Run immediately")
        print("  python auto_committer.py --schedule   # Run with daily scheduler at 6 AM")

if __name__ == "__main__":
    main()

# Auto-generated comment 1: 2025-07-29 09:11:39 - Random: 9717
# Auto-generated comment 2: 2025-07-29 09:11:42 - Random: 3737
# Auto-generated comment 3: 2025-07-29 09:11:46 - Random: 4167
# Auto-generated comment 4: 2025-07-29 09:11:49 - Random: 1658
# Auto-generated comment 5: 2025-07-29 09:11:52 - Random: 4991
# Auto-generated comment 6: 2025-07-29 09:11:55 - Random: 4556
# Auto-generated comment 7: 2025-07-29 09:11:58 - Random: 3986
# Auto-generated comment 8: 2025-07-29 09:12:02 - Random: 9340
# Auto-generated comment 9: 2025-07-29 09:12:05 - Random: 8216
# Auto-generated comment 10: 2025-07-29 09:12:08 - Random: 3785
# Auto-generated comment 11: 2025-07-29 09:12:11 - Random: 9924
# Auto-generated comment 12: 2025-07-29 09:12:14 - Random: 9557
# Auto-generated comment 13: 2025-07-29 09:12:17 - Random: 5643
# Auto-generated comment 14: 2025-07-29 09:12:21 - Random: 3282
# Auto-generated comment 15: 2025-07-29 09:12:24 - Random: 8815
# Auto-generated comment 16: 2025-07-29 09:12:27 - Random: 1933
# Auto-generated comment 17: 2025-07-29 09:12:30 - Random: 7693
# Auto-generated comment 18: 2025-07-29 09:12:33 - Random: 6069
# Auto-generated comment 19: 2025-07-29 09:12:37 - Random: 3517
# Auto-generated comment 20: 2025-07-29 09:12:40 - Random: 8555
# Auto-generated comment 21: 2025-07-29 09:12:43 - Random: 1003
# Auto-generated comment 22: 2025-07-29 09:12:46 - Random: 3681
# Auto-generated comment 23: 2025-07-29 09:12:49 - Random: 4836
# Auto-generated comment 24: 2025-07-29 09:12:53 - Random: 7921
# Auto-generated comment 25: 2025-07-29 09:12:56 - Random: 2581