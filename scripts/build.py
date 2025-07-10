#!/usr/bin/env python3
"""
Build script for creating Malaz executable packages
"""
import os
import sys
import shutil
import subprocess
import platform
import zipfile
import tarfile
from datetime import datetime
import argparse

def get_version():
    """Get version from git or use fallback"""
    try:
        # Try to get version from git
        result = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], 
                              capture_output=True, text=True, check=True)
        git_hash = result.stdout.strip()
        
        date_str = datetime.now().strftime('%Y.%m.%d')
        return f"{date_str}-{git_hash}"
    except:
        return "1.0.0-local"

def clean_build():
    """Clean previous build artifacts"""
    dirs_to_clean = ['build', 'dist', '__pycache__']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"Cleaned {dir_name}/")

def create_version_file(version):
    """Create version file"""
    with open('core/version.py', 'w') as f:
        f.write(f'__version__ = "{version}"\n')
    print(f"Created version file with version: {version}")

def build_executable():
    """Build executable using PyInstaller"""
    system = platform.system().lower()
    executable_name = 'malaz.exe' if system == 'windows' else 'malaz'
    
    cmd = [
        'pyinstaller',
        '--onefile',
        '--name', executable_name.replace('.exe', ''),
        '--add-data', f'core{os.pathsep}core',
        '--add-data', f'utils{os.pathsep}utils',
        '--add-data', f'.env.example{os.pathsep}.',
        '--hidden-import', 'openai',
        '--hidden-import', 'tiktoken',
        '--hidden-import', 'rich',
        '--hidden-import', 'dotenv',
        '--hidden-import', 'httpx',
        'malaz_cli.py'
    ]
    
    print(f"Building executable for {system}...")
    print(f"Running: {' '.join(cmd)}")
    
    try:
        subprocess.run(cmd, check=True)
        print("✅ Executable built successfully!")
        return executable_name
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        sys.exit(1)

def create_package(version, executable_name):
    """Create distribution package"""
    system = platform.system().lower()
    package_name = f"malaz-{system}-{version}"
    
    # Create package directory
    package_dir = os.path.join('dist', package_name)
    os.makedirs(package_dir, exist_ok=True)
    
    # Copy executable
    shutil.copy2(os.path.join('dist', executable_name), package_dir)
    
    # Copy additional files
    files_to_copy = ['.env.example', 'README.md']
    for file_name in files_to_copy:
        if os.path.exists(file_name):
            shutil.copy2(file_name, package_dir)
    
    # Copy docs directory
    if os.path.exists('docs'):
        shutil.copytree('docs', os.path.join(package_dir, 'docs'))
    
    # Create installation script
    create_install_script(package_dir, system, executable_name)
    
    # Create archive
    archive_path = create_archive(package_dir, system)
    
    print(f"✅ Package created: {archive_path}")
    return archive_path

def create_install_script(package_dir, system, executable_name):
    """Create installation script for the package"""
    if system == 'windows':
        install_script = '''@echo off
echo Installing Malaz AI Coding Agent...

set "INSTALL_DIR=%USERPROFILE%\\AppData\\Local\\Programs\\Malaz"
mkdir "%INSTALL_DIR%" 2>nul

copy malaz.exe "%INSTALL_DIR%\\"

echo Adding to PATH...
setx PATH "%PATH%;%INSTALL_DIR%"

echo Installation complete!
echo Please restart your command prompt or PowerShell
echo Then you can use: malaz --help
'''
        with open(os.path.join(package_dir, 'install.bat'), 'w') as f:
            f.write(install_script)
    else:
        install_script = '''#!/bin/bash
set -e

echo "Installing Malaz AI Coding Agent..."

# Create installation directory
INSTALL_DIR="$HOME/.local/bin"
mkdir -p "$INSTALL_DIR"

# Copy executable
cp malaz "$INSTALL_DIR/"
chmod +x "$INSTALL_DIR/malaz"

# Add to PATH if not already there
if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc 2>/dev/null || true
fi

echo "Installation complete!"
echo "Please restart your terminal or run: source ~/.bashrc"
echo "Then you can use: malaz --help"
'''
        install_path = os.path.join(package_dir, 'install.sh')
        with open(install_path, 'w') as f:
            f.write(install_script)
        os.chmod(install_path, 0o755)

def create_archive(package_dir, system):
    """Create compressed archive"""
    if system == 'windows':
        archive_path = f"{package_dir}.zip"
        with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(package_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, os.path.dirname(package_dir))
                    zipf.write(file_path, arcname)
    else:
        archive_path = f"{package_dir}.tar.gz"
        with tarfile.open(archive_path, 'w:gz') as tar:
            tar.add(package_dir, arcname=os.path.basename(package_dir))
    
    return archive_path

def main():
    parser = argparse.ArgumentParser(description='Build Malaz executable package')
    parser.add_argument('--clean', action='store_true', help='Clean build artifacts before building')
    parser.add_argument('--version', type=str, help='Override version number')
    args = parser.parse_args()
    
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    os.chdir(project_dir)
    
    print("🚀 Building Malaz AI Coding Agent...")
    print(f"Platform: {platform.system()} {platform.machine()}")
    
    if args.clean:
        clean_build()
    
    # Get version
    version = args.version or get_version()
    create_version_file(version)
    
    # Check dependencies
    try:
        import pyinstaller
    except ImportError:
        print("❌ PyInstaller not found. Installing...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'pyinstaller'], check=True)
    
    # Build executable
    executable_name = build_executable()
    
    # Create package
    archive_path = create_package(version, executable_name)
    
    print("\n✅ Build completed successfully!")
    print(f"📦 Package: {archive_path}")
    print(f"🔧 Version: {version}")
    print(f"💻 Platform: {platform.system()}")

if __name__ == '__main__':
    main() 