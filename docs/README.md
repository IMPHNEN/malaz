# Malaz Documentation 📚

Selamat datang di dokumentasi lengkap Malaz AI Coding Agent!

## 📋 Dokumentasi

### 🚀 [Getting Started](../README.md)
Panduan instalasi dan quick start untuk memulai menggunakan Malaz.

### 📖 [Usage Guide](USAGE.md)
Panduan lengkap penggunaan Malaz dengan contoh-contoh praktis untuk berbagai skenario development.

### 🔧 [API Reference](API.md)
Dokumentasi lengkap semua tools, commands, dan API yang tersedia di Malaz.

## 🎯 Quick Links

### Untuk Pemula
- [Installation Guide](../README.md#-quick-start)
- [First Steps](USAGE.md#getting-started)
- [Basic Commands](USAGE.md#basic-commands)

### Untuk Developer
- [Tool-Specific Examples](USAGE.md#tool-specific-examples)
- [Best Practices](USAGE.md#best-practices)
- [Extension API](API.md#extension-api)

### Troubleshooting
- [Common Issues](USAGE.md#troubleshooting)
- [Error Handling](API.md#error-handling)
- [Performance Tips](USAGE.md#performance-tips)

## 📋 Table of Contents

### Core Features
1. **Interactive Mode** - CLI interaktif dengan session memory
2. **Direct Commands** - Eksekusi command langsung
3. **Built-in Tools** - 9 tools terintegrasi untuk development
4. **Project Scaffolding** - Template untuk berbagai jenis project
5. **Code Analysis** - Analisis struktur code dan dependencies
6. **Code Review** - Review otomatis dengan saran improvement
7. **Auto Debug** - Analisis error trace dan solusi
8. **Version Control** - Integrasi Git untuk commit otomatis

### Available Tools
1. `create_file` - Create file baru
2. `modify_file` - Modify existing file
3. `run_shell` - Execute shell commands
4. `search_code` - Search patterns dalam codebase
5. `analyze_code` - Analyze code structure
6. `scaffold_project` - Create project dari template
7. `code_review` - Perform code review
8. `auto_debug` - Debug error traces
9. `vcs_commit` - Git commit integration

### Project Templates
- **Flask Web App** - Basic web application dengan authentication
- **CLI Tool** - Command-line tool dengan argument parsing
- **Data Analysis** - Jupyter-based data science project

## 🎉 Quick Examples

### Create New Project
```bash
python malaz_cli.py "create a Flask web application with user authentication"
```

### Code Review
```bash
python malaz_cli.py "!review app.py"
```

### Debug Assistance
```bash
python malaz_cli.py "!debug 'TypeError at line 42'"
```

### Interactive Development
```bash
python malaz_cli.py
malaz> create a REST API for user management
malaz> add input validation to all endpoints
malaz> create unit tests with 90% coverage
malaz> /exit
```

## 🛠️ Configuration

### Environment Setup
```bash
# Copy example config
cp .env.example .env

# Edit dengan API key Anda
# OPENAI_API_KEY=your_key_here
```

### Model Selection
- `gpt-4o-mini` - Cost-effective, recommended untuk general tasks
- `gpt-4o` - High performance untuk complex reasoning
- `gpt-4-turbo` - Premium performance
- `gpt-3.5-turbo` - Budget option untuk simple tasks

## 🔄 Workflow Examples

### Web Development
```bash
malaz> scaffold a Flask web application
malaz> add user authentication with JWT
malaz> create database models for users and posts
malaz> add API endpoints with validation
malaz> create unit tests for all modules
malaz> !review app.py
malaz> !commit "Complete web application with auth"
```

### Data Science
```bash
malaz> scaffold a data analysis project
malaz> create data preprocessing pipeline
malaz> add exploratory data analysis notebook
malaz> implement machine learning model
malaz> create visualization dashboard
```

### CLI Tool Development
```bash
malaz> scaffold a command-line tool
malaz> add argument parsing with click
malaz> implement core functionality
malaz> add configuration file support
malaz> create comprehensive tests
```

## 📞 Support & Contributing

### Getting Help
1. Check [troubleshooting guide](USAGE.md#troubleshooting)
2. Review [API documentation](API.md)
3. Use `/help` command dalam interactive mode
4. Create issue di repository untuk bug reports

### Contributing
1. Fork repository
2. Create feature branch
3. Add documentation untuk new features
4. Submit pull request

### Community
- Join developer discussions
- Share your projects
- Contribute templates dan tools
- Help improve documentation

---

**Happy Coding dengan Malaz! 🚀**

Untuk pertanyaan atau bantuan, silakan buat issue di repository atau gunakan command `/help` dalam interactive mode. 