import os
import subprocess
import re
import ast
import json
from utils.security import validate_path, SecurityException
from core.scaffold import ProjectScaffolder

class ToolManager:
    def __init__(self, project_path):
        self.project_path = project_path
        self.scaffolder = ProjectScaffolder()
        self.tools = self._get_builtin_tools()

    def _get_builtin_tools(self):
        """Get all builtin tools"""
        return [
            {
                "type": "function",
                "function": {
                    "name": "create_file",
                    "description": "Create a new file with specified content",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "file_path": {"type": "string"},
                            "content": {"type": "string"}
                        },
                        "required": ["file_path", "content"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "modify_file",
                    "description": "Modify existing file using diff patches",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "file_path": {"type": "string"},
                            "patches": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "old_line": {"type": "string"},
                                        "new_line": {"type": "string"}
                                    }
                                }
                            }
                        },
                        "required": ["file_path", "patches"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "run_shell",
                    "description": "Execute shell command in project directory",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "command": {"type": "string"}
                        },
                        "required": ["command"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "search_code",
                    "description": "Search codebase for pattern",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "pattern": {"type": "string"}
                        },
                        "required": ["pattern"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "analyze_code",
                    "description": "Analyze code structure and dependencies",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "file_path": {"type": "string"}
                        }
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "scaffold_project",
                    "description": "Create a new project from template",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "template": {
                                "type": "string",
                                "enum": list(self.scaffolder.TEMPLATES.keys())
                            },
                            "project_path": {"type": "string"}
                        },
                        "required": ["template", "project_path"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "code_review",
                    "description": "Perform code review on a file",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "file_path": {"type": "string"}
                        },
                        "required": ["file_path"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "auto_debug",
                    "description": "Analyze and debug error trace",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "error_trace": {"type": "string"}
                        },
                        "required": ["error_trace"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "vcs_commit",
                    "description": "Commit changes to version control",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "message": {"type": "string"}
                        }
                    }
                }
            }
        ]
    
    def get_tool_definitions(self):
        """Get all tool definitions"""
        return self.tools
    
    def list_tools(self):
        """List all available tools"""
        return [{
            "name": tool["function"]["name"],
            "description": tool["function"]["description"]
        } for tool in self.tools]

    def execute_tool(self, tool_name, arguments):
        """Execute a tool with given name and arguments"""
        try:
            if tool_name == "create_file":
                return self.create_file(**arguments)
            elif tool_name == "modify_file":
                return self.modify_file(**arguments)
            elif tool_name == "run_shell":
                return self.run_shell(**arguments)
            elif tool_name == "search_code":
                return self.search_code(**arguments)
            elif tool_name == "analyze_code":
                return self.analyze_code(**arguments)
            elif tool_name == "scaffold_project":
                return self.scaffold_project(**arguments)
            elif tool_name == "code_review":
                return self.code_review(**arguments)
            elif tool_name == "auto_debug":
                return self.auto_debug(**arguments)
            elif tool_name == "vcs_commit":
                return self.vcs_commit(**arguments)
            else:
                return f"Error: Unknown tool {tool_name}"
        except SecurityException as e:
            return f"Security Error: {str(e)}"
        except Exception as e:
            return f"Tool Error: {str(e)}"
    
    def _resolve_path(self, file_path):
        """Resolve file path relative to project with security check"""
        full_path = os.path.join(self.project_path, file_path)
        return validate_path(self.project_path, full_path)
    
    def create_file(self, file_path, content):
        """Create a new file with specified content"""
        full_path = self._resolve_path(file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"File created: {file_path}"
    
    def modify_file(self, file_path, patches):
        """Modify existing file using diff patches"""
        full_path = self._resolve_path(file_path)
        
        if not os.path.exists(full_path):
            return f"Error: File not found - {file_path}"
        
        with open(full_path, 'r', encoding='utf-8') as f:
            original_lines = f.readlines()
        
        new_lines = original_lines.copy()
        
        # Apply patches
        changes = 0
        for patch in patches:
            try:
                old_line = patch['old_line'] + '\n'
                new_line = patch['new_line'] + '\n'
                
                if old_line in new_lines:
                    index = new_lines.index(old_line)
                    new_lines[index] = new_line
                    changes += 1
            except Exception:
                continue
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        
        return f"File modified: {file_path} ({changes}/{len(patches)} changes applied)"
    
    def run_shell(self, command):
        """Execute shell command in project directory"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                cwd=self.project_path,
                capture_output=True,
                text=True,
                timeout=30
            )
            output = f"Command: {command}\nExit code: {result.returncode}\n"
            if result.stdout:
                output += f"Stdout:\n{result.stdout}\n"
            if result.stderr:
                output += f"Stderr:\n{result.stderr}"
            return output
        except Exception as e:
            return f"Command execution failed: {str(e)}"
        
    def search_code(self, pattern):
        """Search codebase for pattern"""
        results = []
        regex = re.compile(pattern)
        
        for root, _, files in os.walk(self.project_path):
            for file in files:
                if file.endswith(('.py', '.js', '.ts', '.java', '.go', '.rs', '.c', '.cpp', '.h')):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            for i, line in enumerate(f, 1):
                                if regex.search(line):
                                    rel_path = os.path.relpath(file_path, self.project_path)
                                    results.append(f"{rel_path}:{i}: {line.strip()}")
                    except Exception:
                        continue
        
        return "\n".join(results) if results else "No matches found"

    def analyze_code(self, file_path=None):
        """Analyze code structure and dependencies"""
        analysis = {
            "dependencies": [],
            "classes": [],
            "functions": [],
            "imports": []
        }
        
        if file_path:
            full_path = self._resolve_path(file_path)
            if not os.path.exists(full_path):
                return f"Error: File not found - {file_path}"
            
            files = [full_path]
        else:
            files = [
                os.path.join(root, file)
                for root, _, files in os.walk(self.project_path)
                for file in files if file.endswith('.py')
            ]
        
        for file in files:
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    tree = ast.parse(f.read())
                
                rel_path = os.path.relpath(file, self.project_path)
                
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            analysis["imports"].append(f"{rel_path}: import {alias.name}")
                    elif isinstance(node, ast.ImportFrom):
                        module = node.module if node.module else ""
                        analysis["imports"].append(f"{rel_path}: from {module} import {', '.join(a.name for a in node.names)}")
                    elif isinstance(node, ast.ClassDef):
                        analysis["classes"].append(f"{rel_path}: class {node.name}")
                    elif isinstance(node, ast.FunctionDef):
                        analysis["functions"].append(f"{rel_path}: function {node.name}")
            
            except Exception as e:
                print(f"Error analyzing {file}: {e}")
                continue
        
        return json.dumps(analysis, indent=2)
    
    def scaffold_project(self, template, project_path):
        """Create a new project from template"""
        return self.scaffolder.create_project(template, project_path)
    
    def code_review(self, file_path):
        """Perform code review on a file"""
        full_path = os.path.join(self.project_path, file_path)
        return self.reviewer.review_file(full_path)
    
    def auto_debug(self, error_trace):
        """Analyze and debug error trace"""
        return self.debugger.analyze_exception(error_trace)
    
    def vcs_commit(self, message="Auto-commit by Malaz"):
        """Commit changes to version control"""
        return self.vcs.commit_changes(message)