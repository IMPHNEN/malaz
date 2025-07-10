import ast
import difflib

class CodeReviewer:
    def __init__(self):
        self.best_practices = [
            "Use meaningful variable names",
            "Keep functions small and focused",
            "Add docstrings for public functions",
            "Avoid global variables",
            "Handle exceptions appropriately",
            "Follow PEP 8 style guide"
        ]
    
    def review_file(self, file_path):
        """Perform code review on a single file"""
        try:
            with open(file_path, 'r') as f:
                code = f.read()
            
            return self.review_code(code, file_path)
        except Exception as e:
            return f"Review failed: {str(e)}"
    
    def review_code(self, code, file_name="code.py"):
        """Perform code review on code string"""
        try:
            # Parse AST
            tree = ast.parse(code)
            
            # Initialize findings
            findings = []
            
            # Check for best practices
            # 1. Check function length
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    if len(node.body) > 30:
                        findings.append({
                            "line": node.lineno,
                            "message": f"Function '{node.name}' is too long ({len(node.body)} lines). Consider refactoring.",
                            "severity": "medium"
                        })
            
            # 2. Check for docstrings
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
                    if not (node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Str)):
                        findings.append({
                            "line": node.lineno if hasattr(node, 'lineno') else 1,
                            "message": f"Missing docstring for {type(node).__name__.lower()}",
                            "severity": "low"
                        })
            
            # 3. Check variable naming conventions
            for node in ast.walk(tree):
                if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                    if not node.id.replace('_', '').isalnum():
                        findings.append({
                            "line": node.lineno,
                            "message": f"Invalid variable name: '{node.id}' should only contain letters, numbers, and underscores",
                            "severity": "high"
                        })
            
            # Format findings
            if findings:
                report = f"Code Review for {file_name}:\n"
                for finding in findings:
                    report += f"\nLine {finding['line']} ({finding['severity']}): {finding['message']}"
                return report
            return "No issues found. Code follows best practices."
        
        except SyntaxError as e:
            return f"Syntax error: {e.msg} at line {e.lineno}"
    
    def suggest_improvement(self, old_code, suggestion):
        """Generate diff for code improvement"""
        old_lines = old_code.splitlines(keepends=True)
        new_lines = suggestion.splitlines(keepends=True)
        
        diff = difflib.unified_diff(
            old_lines,
            new_lines,
            fromfile='original',
            tofile='suggested',
            lineterm=''
        )
        return '\n'.join(diff)