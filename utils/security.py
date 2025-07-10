import os

def validate_path(project_path, target_path):
    """Ensure target path is within project boundaries"""
    project_path = os.path.abspath(project_path)
    target_path = os.path.abspath(target_path)
    
    # Check if target path is within project
    if os.path.commonpath([project_path]) != os.path.commonpath([project_path, target_path]):
        raise SecurityException(f"Attempt to access path outside project: {target_path}")
    
    return target_path

def sanitize_command(command):
    """Basic command sanitization"""
    forbidden = ['rm ', 'del ', 'format ', 'shutdown', 'reboot', 'chmod', 'chown', 'dd', 'mv ', '>', '|']
    for word in forbidden:
        if word in command:
            raise SecurityException(f"Forbidden command detected: {word}")
    return command

class SecurityException(Exception):
    pass