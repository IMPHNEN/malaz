# Malaz Usage Guide 📚

Panduan lengkap penggunaan Malaz AI Coding Agent untuk berbagai skenario development.

## 📖 Table of Contents

1. [Getting Started](#getting-started)
2. [Basic Commands](#basic-commands)
3. [Advanced Usage](#advanced-usage)
4. [Tool-Specific Examples](#tool-specific-examples)
5. [Best Practices](#best-practices)
6. [Integration Examples](#integration-examples)
7. [Troubleshooting](#troubleshooting)

## Getting Started

### First Run

```bash
# Setup environment
cp .env.example .env
# Edit .env dengan OpenAI API key Anda

# Install dependencies
pip install -r requirements.txt

# Run Malaz
python malaz_cli.py
```

### Basic Interaction

```bash
# Interactive mode
python malaz_cli.py

# Direct command
python malaz_cli.py "create a simple Python script that calculates fibonacci numbers"

# Help
python malaz_cli.py --help
```

## Basic Commands

### Interactive Mode Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/help` | Show help | `/help` |
| `/tools` | List available tools | `/tools` |
| `/context` | Show project context | `/context` |
| `/history` | Show conversation history | `/history` |
| `/reset` | Reset session memory | `/reset` |
| `/state` | Show project state | `/state` |
| `/exit` | Exit program | `/exit` |

### Special Commands

| Command | Description | Example |
|---------|-------------|---------|
| `!review <file>` | Code review | `!review app.py` |
| `!debug <trace>` | Debug error | `!debug "TypeError at line 42"` |
| `!commit [msg]` | Git commit | `!commit "Add new feature"` |

## Advanced Usage

### 1. Project Development Workflow

```bash
# Start interactive session
python malaz_cli.py

# Create new project
malaz> scaffold a Flask web application with authentication

# Analyze project structure  
malaz> /context

# Add new features
malaz> add user registration functionality with email validation

# Review code
malaz> !review app.py

# Run tests
malaz> create unit tests for the user registration module

# Commit changes
malaz> !commit "Add user registration with email validation"
```

### 2. Code Analysis and Debugging

```bash
# Analyze entire project
python malaz_cli.py "analyze the code structure and find potential issues"

# Specific file analysis
python malaz_cli.py "analyze security vulnerabilities in auth.py"

# Debug specific error
python malaz_cli.py "!debug 'AttributeError: NoneType object has no attribute split'"

# Code quality review
python malaz_cli.py "!review models/user.py"
```

### 3. Batch Operations

```bash
# Multiple file operations
python malaz_cli.py "create unit tests for all modules in the utils directory"

# Refactoring
python malaz_cli.py "refactor the database connection code to use connection pooling"

# Documentation
python malaz_cli.py "generate comprehensive documentation for all API endpoints"
```

## Tool-Specific Examples

### 1. create_file Tool

```bash
# Create simple Python script
malaz> create a Python script that fetches weather data from an API

# Create configuration file
malaz> create a config.yaml file with database settings

# Create test file
malaz> create unit tests for the authentication module
```

### 2. modify_file Tool

```bash
# Add new function
malaz> add a function to calculate user age in utils.py

# Fix bug
malaz> fix the division by zero error in calculator.py line 45

# Optimize code
malaz> optimize the database query in get_users function
```

### 3. run_shell Tool

```bash
# Install packages
malaz> install pytest and pytest-cov packages

# Run tests
malaz> run all unit tests and show coverage report

# Git operations
malaz> initialize git repository and add all files
```

### 4. search_code Tool

```bash
# Find patterns
malaz> search for all TODO comments in the codebase

# Find security issues
malaz> search for SQL injection vulnerabilities

# Find deprecated functions
malaz> search for usage of deprecated functions
```

### 5. analyze_code Tool

```bash
# Project analysis
malaz> analyze the project structure and dependencies

# Performance analysis
malaz> analyze performance bottlenecks in the main module

# Complexity analysis
malaz> analyze code complexity and suggest improvements
```

### 6. scaffold_project Tool

```bash
# Create Flask app
malaz> scaffold a Flask web application

# Create CLI tool
malaz> scaffold a command-line tool project

# Create data analysis project
malaz> scaffold a Jupyter-based data analysis project
```

## Best Practices

### 1. Effective Prompting

**Good:**
```
"Create a REST API for user management with the following endpoints:
- GET /users (list all users)
- POST /users (create new user)
- PUT /users/{id} (update user)
- DELETE /users/{id} (delete user)
Include input validation and error handling."
```

**Avoid:**
```
"make api"
```

### 2. Project Context

Malaz bekerja lebih baik dengan konteks yang jelas:

```bash
# Set project context first
malaz> /context

# Then make specific requests
malaz> add pagination to the user list endpoint
```

### 3. Iterative Development

```bash
# Step 1: Create basic structure
malaz> create a basic Flask application structure

# Step 2: Add features incrementally  
malaz> add user authentication to the Flask app

# Step 3: Add tests
malaz> create unit tests for the authentication module

# Step 4: Review and improve
malaz> !review auth.py
```

### 4. Session Memory Usage

```bash
# Malaz remembers context within session
malaz> create a User model with SQLAlchemy
malaz> now add validation methods to the User model
malaz> create a migration for the User table
```

### 5. File Organization

```bash
# Be specific about file locations
malaz> create a user service in services/user_service.py
malaz> add the database configuration to config/database.py
```

## Integration Examples

### 1. Web Development

```bash
# Full stack development
python malaz_cli.py

malaz> create a Flask web application with:
- User authentication (login/register)
- Dashboard with user profile
- SQLAlchemy database integration
- Bootstrap frontend
- API endpoints

malaz> add email verification for user registration

malaz> create unit tests for all authentication functions

malaz> !review app.py
```

### 2. Data Science Project

```bash
malaz> scaffold a data analysis project with Jupyter notebooks

malaz> create a data preprocessing script that:
- Loads CSV data
- Handles missing values
- Performs feature engineering
- Saves cleaned data

malaz> create visualizations for data exploration

malaz> implement machine learning model for prediction
```

### 3. CLI Tool Development

```bash
malaz> scaffold a command-line tool project

malaz> create a CLI tool that:
- Accepts file input
- Processes data with multiple options
- Outputs results in JSON/CSV format
- Has proper argument parsing and help

malaz> add configuration file support

malaz> create comprehensive documentation
```

### 4. API Development

```bash
malaz> create a RESTful API with FastAPI that includes:
- User authentication with JWT
- CRUD operations for multiple resources
- Database integration with async SQLAlchemy
- API documentation with Swagger
- Rate limiting and security headers

malaz> add comprehensive error handling

malaz> create integration tests for all endpoints
```

## Advanced Features

### 1. Custom Templates

```python
# Add to core/scaffold.py
"my_custom_template": {
    "description": "My custom project template",
    "structure": {
        "src/": None,
        "src/main.py": "# Main application file\nprint('Hello World')",
        "tests/": None,
        "tests/test_main.py": "# Test file\nimport unittest",
        "requirements.txt": "# Dependencies\n",
        "README.md": "# My Project\n"
    }
}
```

### 2. Environment-Specific Configuration

```bash
# Development
MALAZ_MODEL=gpt-4o-mini
MALAZ_DEBUG=1

# Production
MALAZ_MODEL=gpt-4o
MALAZ_DEBUG=0
```

### 3. Security Best Practices

```bash
# Always validate file paths
malaz> create a secure file upload handler with path validation

# Check for vulnerabilities
malaz> analyze the codebase for security vulnerabilities

# Implement security headers
malaz> add security headers to the Flask application
```

## Troubleshooting

### Common Issues and Solutions

#### 1. OpenAI API Errors

**Problem:** `AuthenticationError: Invalid API key`
```bash
# Solution: Check .env file
cat .env
# Ensure OPENAI_API_KEY is correct
```

**Problem:** `RateLimitError: Rate limit exceeded`
```bash
# Solution: Wait or upgrade OpenAI plan
# Use cheaper model temporarily
MALAZ_MODEL=gpt-3.5-turbo
```

#### 2. Tool Execution Errors

**Problem:** `SecurityException: Path validation failed`
```bash
# Solution: Check file paths are within project directory
# Avoid using absolute paths or parent directory references
```

**Problem:** `Tool Error: File not found`
```bash
# Solution: Verify file exists and check permissions
ls -la filename.py
```

#### 3. Memory Issues

**Problem:** Session memory becomes too large
```bash
# Solution: Reset session memory
malaz> /reset
```

#### 4. Model Response Issues

**Problem:** Incomplete or cut-off responses
```bash
# Solution: Break complex requests into smaller parts
# Instead of: "create a complete web application"
# Use: "create a basic Flask app structure"
# Then: "add user authentication"
# Then: "add database integration"
```

### Debug Mode

Enable debug mode untuk detailed logging:

```bash
export MALAZ_DEBUG=1
python malaz_cli.py
```

### Performance Tips

1. **Use specific models for tasks:**
   - `gpt-4o-mini` untuk tasks sederhana
   - `gpt-4o` untuk complex reasoning

2. **Break large tasks:**
   ```bash
   # Instead of creating everything at once
   malaz> create basic Flask structure
   malaz> add authentication module  
   malaz> add database models
   ```

3. **Use project context:**
   ```bash
   malaz> /context  # Show current context
   malaz> /state    # Show project state
   ```

## Tips and Tricks

### 1. Efficient Development

```bash
# Create development workflow
malaz> create a development workflow script that:
- Sets up virtual environment
- Installs dependencies
- Runs tests
- Starts development server
```

### 2. Code Quality

```bash
# Regular code review
malaz> !review *.py

# Check for improvements
malaz> analyze code quality and suggest improvements
```

### 3. Documentation

```bash
# Generate documentation
malaz> generate API documentation for all endpoints

# Create README
malaz> create a comprehensive README for this project
```

### 4. Testing

```bash
# Comprehensive testing
malaz> create unit tests with 90% coverage for all modules

# Integration testing
malaz> create integration tests for the API endpoints
```

---

Untuk pertanyaan lebih lanjut atau bantuan, gunakan command `/help` dalam interactive mode atau buat issue di repository. 