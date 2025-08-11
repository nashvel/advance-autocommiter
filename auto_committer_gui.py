#!/usr/bin/env python3
"""
Auto-Committer GUI
A GUI version of the auto-committer script with selectable commit counts.
"""

import os
import sys
import time
import random
import subprocess
import threading
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class AutoCommitterCore:
    """Core logic for the auto-committer, separated from GUI"""
    
    def __init__(self, progress_callback=None, log_callback=None):
        self.script_path = os.path.abspath(__file__)
        self.target_file = os.path.join(os.path.dirname(self.script_path), 'changes.txt')
        self.commit_count = 0
        self.max_commits = 100
        self.progress_callback = progress_callback
        self.log_callback = log_callback
        self.is_running = False
        
    def log(self, message):
        """Log a message"""
        print(message)
        if self.log_callback:
            self.log_callback(message)
    
    def update_progress(self, current, total):
        """Update progress"""
        if self.progress_callback:
            self.progress_callback(current, total)
    
    def modify_target_file(self):
        """Modify the changes.txt file by adding a timestamp line"""
        try:
            # Read existing content
            if os.path.exists(self.target_file):
                with open(self.target_file, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
            else:
                content = "change me multiple times."
            
            # Add a timestamp line
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            random_num = random.randint(1000, 9999)
            new_line = f"Change #{self.commit_count + 1}: {timestamp} - Random: {random_num}"
            
            # Append the new line
            modified_content = content + "\n" + new_line
            
            with open(self.target_file, 'w', encoding='utf-8') as f:
                f.write(modified_content)
                
            self.log(f"Modified changes.txt (change #{self.commit_count + 1})")
            return True
            
        except Exception as e:
            self.log(f"Error modifying changes.txt: {e}")
            return False
    
    def commit_and_push(self):
        """Commit changes and push to GitHub"""
        try:
            # Add changes to git
            result = subprocess.run(['git', 'add', '.'], 
                                  capture_output=True, text=True, cwd=os.path.dirname(self.script_path))
            if result.returncode != 0:
                self.log(f"Git add failed: {result.stderr}")
                return False
            
            # Commit changes
            commit_message = f"Auto-commit #{self.commit_count + 1}: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            result = subprocess.run(['git', 'commit', '-m', commit_message], 
                                  capture_output=True, text=True, cwd=os.path.dirname(self.script_path))
            if result.returncode != 0:
                self.log(f"Git commit failed: {result.stderr}")
                return False
            
            # Push to GitHub
            result = subprocess.run(['git', 'push'], 
                                  capture_output=True, text=True, cwd=os.path.dirname(self.script_path))
            if result.returncode != 0:
                self.log(f"Git push failed: {result.stderr}")
                return False
            
            self.log(f"Successfully committed and pushed change #{self.commit_count + 1}")
            return True
            
        except Exception as e:
            self.log(f"Error in commit_and_push: {e}")
            return False
    
    def run_commits(self, num_commits):
        """Run the specified number of commits"""
        self.max_commits = num_commits
        self.commit_count = 0
        self.is_running = True
        
        self.log(f"Starting auto-commit process for {num_commits} commits...")
        
        for i in range(num_commits):
            if not self.is_running:  # Allow stopping
                self.log("Process stopped by user")
                break
                
            self.log(f"\n--- Commit {i + 1}/{num_commits} ---")
            
            # Modify the target file
            if not self.modify_target_file():
                self.log("Failed to modify file, stopping...")
                break
            
            # Commit and push
            if not self.commit_and_push():
                self.log("Failed to commit/push, stopping...")
                break
            
            self.commit_count += 1
            self.update_progress(self.commit_count, num_commits)
            
            # Wait a bit between commits (optional)
            if i < num_commits - 1:  # Don't wait after the last commit
                self.log("Waiting 2 seconds before next commit...")
                time.sleep(2)
        
        self.is_running = False
        if self.commit_count == num_commits:
            self.log(f"\n✅ Successfully completed all {num_commits} commits!")
        else:
            self.log(f"\n⚠️ Completed {self.commit_count}/{num_commits} commits")
    
    def stop(self):
        """Stop the commit process"""
        self.is_running = False


class AutoCommitterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto-Committer GUI")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Initialize core
        self.core = AutoCommitterCore(
            progress_callback=self.update_progress,
            log_callback=self.log_message
        )
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Auto-Committer", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Commit count selection
        ttk.Label(main_frame, text="Select number of commits:").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        # Radio buttons for preset values
        self.commit_var = tk.StringVar(value="10")
        
        radio_frame = ttk.Frame(main_frame)
        radio_frame.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Radiobutton(radio_frame, text="10", variable=self.commit_var, value="10").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(radio_frame, text="20", variable=self.commit_var, value="20").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(radio_frame, text="30", variable=self.commit_var, value="30").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(radio_frame, text="Custom", variable=self.commit_var, value="custom").pack(side=tk.LEFT, padx=5)
        
        # Custom input
        ttk.Label(main_frame, text="Custom amount:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.custom_entry = ttk.Entry(main_frame, width=10)
        self.custom_entry.grid(row=2, column=1, sticky=tk.W, pady=5)
        self.custom_entry.insert(0, "50")
        
        # Control buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=2, sticky=tk.E, pady=5)
        
        self.start_button = ttk.Button(button_frame, text="Start Commits", command=self.start_commits)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.stop_button = ttk.Button(button_frame, text="Stop", command=self.stop_commits, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        
        # Progress bar
        ttk.Label(main_frame, text="Progress:").grid(row=3, column=0, sticky=(tk.W, tk.N), pady=(20, 5))
        self.progress = ttk.Progressbar(main_frame, mode='determinate')
        self.progress.grid(row=3, column=1, columnspan=2, sticky=(tk.W, tk.E, tk.N), pady=(20, 5))
        
        # Progress label
        self.progress_label = ttk.Label(main_frame, text="Ready to start")
        self.progress_label.grid(row=4, column=1, columnspan=2, sticky=(tk.W, tk.N))
        
        # Log area
        ttk.Label(main_frame, text="Log:").grid(row=5, column=0, sticky=(tk.W, tk.N), pady=(20, 5))
        
        self.log_text = scrolledtext.ScrolledText(main_frame, height=15, width=70)
        self.log_text.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        # Configure text area to expand
        main_frame.rowconfigure(6, weight=1)
        
    def get_commit_count(self):
        """Get the selected commit count"""
        if self.commit_var.get() == "custom":
            try:
                return int(self.custom_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number for custom commits")
                return None
        else:
            return int(self.commit_var.get())
    
    def start_commits(self):
        """Start the commit process"""
        commit_count = self.get_commit_count()
        if commit_count is None:
            return
        
        if commit_count <= 0:
            messagebox.showerror("Error", "Number of commits must be greater than 0")
            return
        
        # Update UI state
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.progress['value'] = 0
        self.progress['maximum'] = commit_count
        self.log_text.delete(1.0, tk.END)
        
        # Start in a separate thread to avoid blocking the GUI
        self.commit_thread = threading.Thread(target=self.core.run_commits, args=(commit_count,))
        self.commit_thread.daemon = True
        self.commit_thread.start()
    
    def stop_commits(self):
        """Stop the commit process"""
        self.core.stop()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.log_message("Stopping process...")
    
    def update_progress(self, current, total):
        """Update the progress bar"""
        self.root.after(0, lambda: self._update_progress_ui(current, total))
    
    def _update_progress_ui(self, current, total):
        """Update progress bar in main thread"""
        self.progress['value'] = current
        self.progress_label.config(text=f"{current}/{total} commits completed")
        
        if current >= total:
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
    
    def log_message(self, message):
        """Add a message to the log"""
        self.root.after(0, lambda: self._log_message_ui(message))
    
    def _log_message_ui(self, message):
        """Add message to log in main thread"""
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)


def main():
    """Main function"""
    root = tk.Tk()
    app = AutoCommitterGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
