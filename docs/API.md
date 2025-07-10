# Malaz API Reference 🔧

Dokumentasi lengkap untuk semua tools, commands, dan API yang tersedia di Malaz AI Coding Agent.

## 📋 Table of Contents

1. [Core Classes](#core-classes)
2. [Built-in Tools](#built-in-tools)
3. [CLI Commands](#cli-commands)
4. [Configuration](#configuration)
5. [Error Handling](#error-handling)
6. [Extension API](#extension-api)

## Core Classes

### CodingAgent

Main AI agent class yang mengelola interaksi dengan OpenAI API dan tool execution.

```python
class CodingAgent:
    def __init__(self, project_path=None)
    def process_request(self, user_input: str, memory: SessionMemory)
    def handle_code_review(self, command)
    def handle_debug_command(self, command)
    def handle_commit_command(self, command)
```

**Parameters:**
- `project_path` (str, optional): Path ke project directory. Default: current working directory

**Methods:**
- `process_request()`: Process user input dan execute tools jika diperlukan
- `handle_code_review()`: Handle code review commands (`!review`)
- `handle_debug_command()`: Handle debugging commands (`!debug`)
- `handle_commit_command()`: Handle Git commit commands (`!commit`)

### ToolManager

Mengelola semua built-in tools dan execution.

```python
class ToolManager:
    def __init__(self, project_path)
    def get_tool_definitions(self)
    def list_tools(self)
    def execute_tool(self, tool_name, arguments)
```

**Methods:**
- `get_tool_definitions()`: Return tool definitions untuk OpenAI API
- `list_tools()`: Return list available tools
- `execute_tool()`: Execute specific tool dengan arguments

### SessionMemory

Mengelola conversation history dan context.

```python
class SessionMemory:
    def __init__(self, max_history=50)
    def add_interaction(self, user_input, assistant_response)
    def get_context(self, max_length=2000)
    def reset(self)
```

## Built-in Tools

### 1. create_file

Create file baru dengan content yang ditentukan.

**Parameters:**
```json
{
  "file_path": "string (required)",
  "content": "string (required)"
}
```

**Example:**
```bash
malaz> create a Python script that calculates prime numbers
```

**Returns:** Success message atau error

### 2. modify_file

Modify existing file menggunakan diff patches.

**Parameters:**
```json
{
  "file_path": "string (required)",
  "patches": [
    {
      "old_line": "string",
      "new_line": "string"
    }
  ]
}
```

**Example:**
```bash
malaz> fix the bug in line 42 of calculator.py
```

**Returns:** Number of changes applied

### 3. run_shell

Execute shell command dalam project directory.

**Parameters:**
```json
{
  "command": "string (required)"
}
```

**Security:** Command dibatasi dalam project directory

**Example:**
```bash
malaz> install pytest package
malaz> run unit tests
```

**Returns:** Command output dan exit code

### 4. search_code

Search pattern dalam codebase menggunakan regex.

**Parameters:**
```json
{
  "pattern": "string (required)"
}
```

**Supported File Types:**
- `.py` (Python)
- `.js`, `.ts` (JavaScript/TypeScript)
- `.java` (Java)
- `.go` (Go)
- `.rs` (Rust)
- `.c`, `.cpp`, `.h` (C/C++)

**Example:**
```bash
malaz> search for all TODO comments
malaz> find functions that use deprecated APIs
```

**Returns:** Matches dengan file path dan line number

### 5. analyze_code

Analyze code structure dan dependencies.

**Parameters:**
```json
{
  "file_path": "string (optional)"
}
```

**Analysis Results:**
- Dependencies list
- Classes found
- Functions found
- Import statements

**Example:**
```bash
malaz> analyze the entire project structure
malaz> analyze security.py file
```

**Returns:** JSON analysis report

### 6. scaffold_project

Create project baru dari template.

**Parameters:**
```json
{
  "template": "string (required)",
  "project_path": "string (required)"
}
```

**Available Templates:**
- `flask_web_app`: Basic Flask web application
- `cli_tool`: Python CLI tool dengan argument parsing
- `data_analysis`: Jupyter-based data analysis project

**Example:**
```bash
malaz> scaffold a Flask web application in ./my-web-app
malaz> create a CLI tool project
```

**Returns:** Success message dan created files list

### 7. code_review

Perform code review pada file.

**Parameters:**
```json
{
  "file_path": "string (required)"
}
```

**Review Aspects:**
- Code quality
- Security issues
- Performance concerns
- Best practices
- Documentation

**Example:**
```bash
malaz> !review app.py
malaz> review the authentication module
```

**Returns:** Detailed review report

### 8. auto_debug

Analyze dan debug error trace.

**Parameters:**
```json
{
  "error_trace": "string (required)"
}
```

**Debug Capabilities:**
- Exception analysis
- Root cause identification
- Fix suggestions
- Related code inspection

**Example:**
```bash
malaz> !debug "TypeError: unsupported operand type(s)"
malaz> debug the connection timeout error
```

**Returns:** Debug analysis dan suggested solutions

### 9. vcs_commit

Commit changes ke version control.

**Parameters:**
```json
{
  "message": "string (optional)"
}
```

**Default Message:** "Auto-commit by Malaz"

**Example:**
```bash
malaz> !commit "Add user authentication feature"
malaz> commit the current changes
```

**Returns:** Git commit result

## CLI Commands

### Interactive Mode Commands

#### `/help`
Show help dan available commands.

**Usage:** `/help`

**Returns:** Command list dengan descriptions

#### `/tools`
List semua available tools.

**Usage:** `/tools`

**Returns:** Tool list dengan descriptions

#### `/context`
Show current project context.

**Usage:** `/context`

**Returns:** Project structure dan context information

#### `/history`
Show conversation history.

**Usage:** `/history`

**Returns:** Previous interactions dalam session

#### `/reset`
Reset session memory.

**Usage:** `/reset`

**Effect:** Clear conversation history

#### `/state`
Show current project state.

**Usage:** `/state`

**Returns:** Project path, context, dan configuration

#### `/exit`
Exit dari interactive mode.

**Usage:** `/exit`

**Effect:** Terminate session

### Special Commands

#### `!review <file>`
Quick code review.

**Usage:** `!review filename.py`

**Returns:** Code review analysis

#### `!debug <trace>`
Quick debug assistance.

**Usage:** `!debug "error message"`

**Returns:** Debug analysis

#### `!commit [message]`
Quick Git commit.

**Usage:** 
- `!commit` (default message)
- `!commit "Custom message"`

**Returns:** Commit result

## Configuration

### Environment Variables

```bash
# Required
OPENAI_API_KEY=your_api_key_here

# Optional
MALAZ_MODEL=gpt-4o-mini        # Default: gpt-4o-mini
MALAZ_DEBUG=1                  # Enable debug mode
```

### Supported Models

| Model | Use Case | Cost |
|-------|----------|------|
| `gpt-4o-mini` | General tasks, cost-effective | Low |
| `gpt-4o` | Complex reasoning | Medium |
| `gpt-4-turbo` | High performance tasks | High |
| `gpt-3.5-turbo` | Simple tasks | Very Low |

### Project Configuration

Malaz reads project structure dan creates context automatically:

```python
# Project structure example
{
    "files": ["app.py", "models.py", "utils.py"],
    "directories": ["templates/", "static/", "tests/"],
    "languages": ["python"],
    "frameworks": ["flask"]
}
```

## Error Handling

### Common Error Types

#### SecurityException
File path validation failed.

```python
raise SecurityException("Path outside project directory")
```

**Causes:**
- Absolute paths
- Parent directory access (`../`)
- Symbolic links outside project

#### ToolError
Tool execution failed.

```python
return f"Tool Error: {str(e)}"
```

**Common Causes:**
- File not found
- Permission denied
- Invalid arguments

#### OpenAI API Errors

**AuthenticationError:**
```bash
Error: Invalid API key
```

**RateLimitError:**
```bash
Error: Rate limit exceeded
```

**ModelError:**
```bash
Error: Model not found
```

### Error Response Format

```json
{
  "error": "error_type",
  "message": "Human readable message",
  "details": "Technical details",
  "suggestion": "How to fix"
}
```

## Extension API

### Adding Custom Tools

1. **Define tool function:**

```python
def custom_tool(self, param1, param2):
    """Custom tool implementation"""
    try:
        # Implementation
        result = do_something(param1, param2)
        return f"Success: {result}"
    except Exception as e:
        return f"Error: {str(e)}"
```

2. **Add tool definition:**

```python
{
    "type": "function",
    "function": {
        "name": "custom_tool",
        "description": "Description of what the tool does",
        "parameters": {
            "type": "object",
            "properties": {
                "param1": {"type": "string"},
                "param2": {"type": "integer"}
            },
            "required": ["param1"]
        }
    }
}
```

3. **Add to executor:**

```python
elif tool_name == "custom_tool":
    return self.custom_tool(**arguments)
```

### Adding Project Templates

Edit `core/scaffold.py`:

```python
"my_template": {
    "description": "Template description",
    "structure": {
        "file.py": "file content",
        "directory/": None,
        "directory/subfile.py": "sub file content"
    }
}
```

### Custom Memory Processors

Extend `SessionMemory`:

```python
class CustomMemory(SessionMemory):
    def add_interaction(self, user_input, response):
        # Custom processing
        processed_input = self.process_input(user_input)
        super().add_interaction(processed_input, response)
    
    def process_input(self, input_text):
        # Custom input processing
        return processed_input
```

### Event Hooks

```python
class CustomAgent(CodingAgent):
    def process_request(self, user_input, memory):
        # Pre-processing hook
        self.on_request_start(user_input)
        
        # Main processing
        response = super().process_request(user_input, memory)
        
        # Post-processing hook
        self.on_request_end(response)
        
        return response
```

## Performance Considerations

### Tool Execution Timeout

```python
# Shell commands timeout after 30 seconds
subprocess.run(command, timeout=30)
```

### Memory Management

```python
# Session memory limited to 50 interactions
SessionMemory(max_history=50)

# Context limited to 2000 characters
memory.get_context(max_length=2000)
```

### Rate Limiting

- OpenAI API rate limits apply
- Use appropriate model untuk task complexity
- Break large tasks into smaller operations

---

**Note:** Dokumentasi ini untuk Malaz v1.0. Untuk versi terbaru, check repository updates. 