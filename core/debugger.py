import os
import re
import ast
from core.tool_manager import ToolManager

class CodeDebugger:
    def __init__(self, project_path):
        self.project_path = project_path
        self.tool_manager = ToolManager(project_path)
    
    def analyze_exception(self, exception_trace):
        """Analyze exception trace and suggest fixes"""
        # Extract relevant info from traceback
        file_match = re.search(r'File "(.*?)", line (\d+)', exception_trace)
        if not file_match:
            return "Could not parse exception details"
        
        file_path = file_match.group(1)
        line_number = int(file_match.group(2))
        
        # Get problematic code
        with open(file_path, 'r') as f:
            lines = f.readlines()
            problem_line = lines[line_number - 1].strip()
        
        # Basic error pattern matching
        suggestions = []
        if "NoneType" in exception_trace and "has no attribute" in exception_trace:
            attribute = re.search(r"has no attribute '(\w+)'", exception_trace).group(1)
            suggestions.append(f"Check if variable is None before accessing attribute '{attribute}'")
        
        if "IndexError" in exception_trace:
            suggestions.append("Check list length before accessing index")
        
        if "KeyError" in exception_trace:
            key = re.search(r"KeyError: '(\w+)'", exception_trace)
            if key:
                suggestions.append(f"Check if key '{key.group(1)}' exists in dictionary")
        
        # Construct response
        response = f"Exception in {file_path}, line {line_number}:\n"
        response += f"Code: {problem_line}\n\n"
        response += "Possible fixes:\n"
        response += "\n".join(f"- {s}" for s in suggestions) if suggestions else "- No specific suggestions"
        
        return response
    
    def static_analysis(self, file_path):
        """Perform static code analysis"""
        full_path = os.path.join(self.project_path, file_path)
        if not os.path.exists(full_path):
            return f"File not found: {file_path}"
        
        issues = []
        try:
            with open(full_path, 'r') as f:
                tree = ast.parse(f.read())
            
            # Walk through AST to find potential issues
            for node in ast.walk(tree):
                # Check for undefined variables
                if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                    # This is a simplified check - real implementation would track scope
                    pass
                
                # Check for unused imports
                if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                    for alias in node.names:
                        if alias.asname:
                            name = alias.asname
                        else:
                            name = alias.name.split('.')[0]
                        
                        # Check if name is used
                        used = any(isinstance(n, ast.Name) and n.id == name 
                                  for n in ast.walk(tree))
                        
                        if not used:
                            issues.append(f"Unused import: {name}")
            
            # Add more checks as needed
            
        except Exception as e:
            return f"Analysis failed: {str(e)}"
        
        if issues:
            return "Potential issues found:\n" + "\n".join(f"- {issue}" for issue in issues)
        return "No issues found in static analysis"