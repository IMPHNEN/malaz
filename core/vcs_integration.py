import os
import subprocess
from utils.security import sanitize_command

class VCSIntegration:
    def __init__(self, project_path):
        self.project_path = project_path
        self.vcs_type = self.detect_vcs()
    
    def detect_vcs(self):
        if os.path.exists(os.path.join(self.project_path, '.git')):
            return 'git'
        elif os.path.exists(os.path.join(self.project_path, '.hg')):
            return 'mercurial'
        elif os.path.exists(os.path.join(self.project_path, '.svn')):
            return 'svn'
        return None
    
    def commit_changes(self, message):
        if not self.vcs_type:
            return "No version control system detected"
        
        try:
            if self.vcs_type == 'git':
                commands = [
                    "git add .",
                    f"git commit -m '{message}'"
                ]
                output = ""
                for cmd in commands:
                    sanitized = sanitize_command(cmd)
                    result = subprocess.run(
                        sanitized,
                        shell=True,
                        cwd=self.project_path,
                        capture_output=True,
                        text=True
                    )
                    output += f"$ {cmd}\n{result.stdout}\n"
                    if result.returncode != 0:
                        output += f"Error: {result.stderr}"
                        return output
                return output
            # Add support for other VCS here
        except Exception as e:
            return f"VCS operation failed: {str(e)}"
    
    def get_status(self):
        if not self.vcs_type:
            return "No version control system detected"
        
        try:
            if self.vcs_type == 'git':
                result = subprocess.run(
                    "git status",
                    shell=True,
                    cwd=self.project_path,
                    capture_output=True,
                    text=True
                )
                return result.stdout
            # Add support for other VCS here
        except Exception as e:
            return f"VCS status failed: {str(e)}"
    
    def get_diff(self):
        if not self.vcs_type:
            return "No version control system detected"
        
        try:
            if self.vcs_type == 'git':
                result = subprocess.run(
                    "git diff",
                    shell=True,
                    cwd=self.project_path,
                    capture_output=True,
                    text=True
                )
                return result.stdout
            # Add support for other VCS here
        except Exception as e:
            return f"VCS diff failed: {str(e)}"