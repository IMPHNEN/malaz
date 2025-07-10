import os
import json
import ast

def detect_dependencies(project_path):
    """Detect project dependencies based on files"""
    dependencies = []
    
    # Python
    if os.path.exists(os.path.join(project_path, 'requirements.txt')):
        dependencies.append("Python")
    
    # Node.js
    if os.path.exists(os.path.join(project_path, 'package.json')):
        dependencies.append("Node.js")
    
    # Go
    if os.path.exists(os.path.join(project_path, 'go.mod')):
        dependencies.append("Go")
    
    # Rust
    if os.path.exists(os.path.join(project_path, 'Cargo.toml')):
        dependencies.append("Rust")
    
    return dependencies

def load_project_structure(project_path):
    """Generate detailed project structure with file contents summary"""
    structure = {
        "path": project_path,
        "directories": [],
        "files": [],
        "dependencies": detect_dependencies(project_path)
    }

    for root, dirs, files in os.walk(project_path):
        # Skip hidden directories# Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        for dir_name in dirs:
            structure["dependencies"].append(os.path.relpath(os.path.join(root, dir_name), project_path))
        
        for file_name in files:
            file_path = os.path.join(root, file_name)
            rel_path = os.path.relpath(file_path, project_path)

            file_info = {
                "path": rel_path,
                "size": os.path.getsize(file_path),
                "type": "file"
            }

            # Add language-specific metadata
            if file_name.endswith('.py'):
                file_info["type"] = "python"
                file_info["summary"] = get_python_file_summary(file_path)
            elif file_name.endswith('.js'):
                file_info["type"] = "javascript"
            elif file_name.endswith('.json'):
                file_info["type"] = "json"
            elif file_name == 'package.json':
                file_info["type"] = "package.json"
                file_info["dependencies"] = get_package_dependencies(file_path)
            elif file_name == 'requirements.txt':
                file_info["type"] = "python-dependencies"

            structure["files"].append(file_info)

    return structure

def format_context(structure, max_files=20):
    """Format project context for AI prompt"""
    context = f"Project: {structure['path']}\n"

    if structure['dependencies']:
        context += f"Dependencies: {', '.join(structure['dependencies'])}\n"

    context += "\nDirectory Structure:\n"
    context += "\n".join(f"- {d}" for d in structure['directories'][:max_files])
    

    context += "\n\nImportant Files:\n"
    for file in structure['files'][:max_files]:
        context += f"- {file['path']}"
        if file.get('summary'):
            context += f" ({file['summary']})"
        context += "\n"
    
    return context

def get_python_file_summary(file_path):
    """Extract summary from Python file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('class '):
                    return f"Class: {line.split()[1].split(':')[0]}"
                elif line.startswith('def '):
                    return f"Function: {line.split()[1].split('(')[0]}"
            return "No classes/functions found"
    except Exception as e:
        return f"Error reading file: {str(e)}"
    
def get_package_dependencies(file_path):
    """Extract dependencies from package.json"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            package = json.load(f)
            deps = list(package.get('dependencies', {}).keys())
            deps += list(package.get('devDependencies', {}).keys())
            return deps[:5]  # Return first 5 dependencies
    except Exception as e:
        return [f"Error: {str(e)}"]
