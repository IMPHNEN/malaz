# Malaz - AI Coding Agent 🤖

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-green.svg)](https://openai.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/IMPHNEN/malaz/workflows/Continuous%20Integration/badge.svg)](https://github.com/IMPHNEN/malaz/actions)
[![Release](https://github.com/IMPHNEN/malaz/workflows/Build%20and%20Release/badge.svg)](https://github.com/IMPHNEN/malaz/actions)

Malaz adalah AI coding assistant yang powerful, dirancang untuk membantu developer dalam berbagai tugas pengembangan software termasuk code generation, debugging, refactoring, dan project management.

## ✨ Features

- 🔧 **Tool Integration**: Built-in tools untuk file management, code analysis, dan shell execution
- 🧠 **Smart Code Analysis**: Analisis struktur code dan dependencies secara otomatis
- 🛠️ **Project Scaffolding**: Template untuk berbagai jenis project (Flask, CLI, Data Analysis)
- 🔍 **Code Search**: Pencarian pattern dalam codebase menggunakan regex
- 📝 **Code Review**: Review code otomatis dengan saran improvement
- 🐛 **Auto Debug**: Analisis error trace dan saran solusi
- 🔄 **Version Control**: Integrasi dengan Git untuk commit otomatis
- 💬 **Interactive Mode**: CLI interaktif dengan session memory
- 🔐 **Security**: Built-in security validation untuk operasi file

## 📦 Installation

### Download Pre-built Binaries (Recommended)

Download the latest release untuk platform Anda:

- **Windows**: [malaz-windows-latest.zip](https://github.com/IMPHNEN/malaz/releases/latest)
- **Linux**: [malaz-linux-latest.tar.gz](https://github.com/IMPHNEN/malaz/releases/latest)
- **macOS**: [malaz-macos-latest.tar.gz](https://github.com/IMPHNEN/malaz/releases/latest)

#### Installation Steps:

**Windows:**
1. Download `malaz-windows-*.zip`
2. Extract archive
3. Run `install.bat` as Administrator
4. Restart Command Prompt/PowerShell
5. Use: `malaz --help`

**Linux/macOS:**
1. Download file `.tar.gz` yang sesuai
2. Extract: `tar -xzf malaz-*.tar.gz`
3. Run: `./install.sh`
4. Restart terminal atau run: `source ~/.bashrc`
5. Use: `malaz --help`

### Development Installation

Untuk development atau jika ingin build dari source:

1. **Clone repository:**
```bash
git clone <repository-url>
cd malaz
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Setup environment:**
```bash
cp .env.example .env
# Edit .env dan masukkan OpenAI API key Anda
```

4. **Run Malaz:**
```bash
# Interactive mode
python malaz_cli.py

# Direct command
python malaz_cli.py "create a simple Python calculator"

# Show help
python malaz_cli.py --help
```

### Build dari Source

Untuk build executable sendiri:

```bash
# Install build dependencies
pip install pyinstaller

# Build untuk platform saat ini
python scripts/build.py

# Build dengan clean
python scripts/build.py --clean

# Build dengan version custom
python scripts/build.py --version "1.0.0-custom"
```

## 📖 Usage

### Interactive Mode

Jalankan Malaz dalam mode interaktif:

```bash
python malaz_cli.py
```

Mode interaktif menyediakan:
- Session memory untuk konteks percakapan
- Built-in commands dengan prefix `/`
- Special commands dengan prefix `!`

### Direct Command Mode

Eksekusi command langsung:

```bash
python malaz_cli.py "analyze the code structure of this project"
python malaz_cli.py "create a Flask web app with user authentication"
python malaz_cli.py "debug this error: AttributeError in line 45"
```

### Built-in Commands

| Command | Description |
|---------|-------------|
| `/help` | Tampilkan bantuan |
| `/tools` | List available tools |
| `/context` | Show project context |
| `/history` | Show conversation history |
| `/reset` | Reset session memory |
| `/state` | Show current project state |
| `/exit` | Keluar dari program |

### Special Commands

| Command | Description |
|---------|-------------|
| `!review <file>` | Review code file |
| `!debug <trace>` | Debug error trace |
| `!commit [message]` | Commit changes to Git |

## 📚 Documentation

Untuk panduan lengkap dan referensi API, kunjungi [Malaz Documentation](docs/README.md):

- **📖 [Usage Guide](docs/USAGE.md)** - Panduan lengkap dengan contoh-contoh praktis
- **🔧 [API Reference](docs/API.md)** - Dokumentasi lengkap tools dan commands
- **🚀 [Getting Started](docs/README.md)** - Quick links dan overview

## 🛠️ Available Tools

Malaz dilengkapi dengan 9 built-in tools:

1. **create_file** - Create file baru dengan content
2. **modify_file** - Modify file menggunakan diff patches
3. **run_shell** - Execute shell command
4. **search_code** - Search pattern dalam codebase
5. **analyze_code** - Analisis struktur code dan dependencies
6. **scaffold_project** - Create project dari template
7. **code_review** - Perform code review
8. **auto_debug** - Analisis error trace
9. **vcs_commit** - Commit changes ke version control

## 📁 Project Structure

```
malaz/
├── core/
│   ├── agent.py           # Main AI agent class
│   ├── tool_manager.py    # Tool management system
│   ├── memory.py          # Session memory management
│   ├── scaffold.py        # Project scaffolding
│   ├── debugger.py        # Auto debugging system
│   └── vcs_integration.py # Version control integration
├── utils/
│   ├── file_utils.py      # File operations utilities
│   ├── security.py        # Security validation
│   └── review_assistant.py # Code review assistant
├── malaz_cli.py           # Main CLI interface
├── requirements.txt       # Python dependencies
├── .env                   # Environment configuration
└── README.md             # Documentation
```

## ⚙️ Configuration

Edit file `.env` untuk konfigurasi:

```env
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional
MALAZ_MODEL=gpt-4o-mini  # Default model to use
```

### Supported Models

- `gpt-4o-mini` (default, cost-effective)
- `gpt-4o`
- `gpt-4-turbo`
- `gpt-3.5-turbo`

## 📋 Examples

### 1. Create New Project

```bash
python malaz_cli.py "create a Flask web application with user authentication and database integration"
```

### 2. Code Analysis

```bash
python malaz_cli.py "analyze the security vulnerabilities in my authentication module"
```

### 3. Debug Assistance

```bash
python malaz_cli.py "!debug 'TypeError: unsupported operand type(s) for +: 'int' and 'str' at line 42'"
```

### 4. Code Review

```bash
python malaz_cli.py "!review app.py"
```

### 5. Interactive Development

```bash
python malaz_cli.py
malaz> create a REST API for user management
malaz> add input validation to the endpoints
malaz> write unit tests for the API
malaz> /exit
```

## 🔧 Development

### CI/CD Pipeline

Project ini menggunakan GitHub Actions untuk automated testing dan releases:

- **Continuous Integration**: Test otomatis pada Python 3.8-3.11 di Windows, Linux, dan macOS
- **Security Scanning**: Automated security checks dengan bandit dan safety
- **Code Quality**: Linting dengan flake8, formatting dengan black, type checking dengan mypy
- **Automated Releases**: Build dan release otomatis untuk semua platform saat merge ke branch `release`

### Release Process

1. **Development**: Work pada branch `feature/*` atau `develop`
2. **Testing**: CI pipeline akan run test otomatis
3. **Release**: Merge ke branch `release` akan trigger:
   - Build executable untuk Windows, Linux, macOS
   - Create GitHub release dengan versioning otomatis
   - Upload binaries sebagai release assets

### Branch Strategy

- `main`: Stable production code
- `develop`: Development integration branch
- `feature/*`: Feature development branches
- `release`: Release trigger branch

### Adding Custom Tools

Extend `ToolManager` class di `core/tool_manager.py`:

```python
def your_custom_tool(self, param1, param2):
    """Your custom tool implementation"""
    # Implementation here
    return "Tool result"
```

Update tool definitions dalam `_get_builtin_tools()` method.

### Adding Project Templates

Edit `core/scaffold.py` untuk menambah template baru:

```python
"your_template": {
    "description": "Your template description",
    "structure": {
        "file1.py": "file content",
        "folder/": None,
        # ... more files
    }
}
```

## 🚦 Troubleshooting

### Common Issues

1. **OpenAI API Error**
   - Pastikan API key valid di `.env`
   - Check quota/billing di OpenAI dashboard

2. **Tool Execution Failed**
   - Verify file permissions
   - Check security validation dalam `utils/security.py`

3. **Module Import Error**
   - Pastikan semua dependencies terinstall
   - Run `pip install -r requirements.txt`

4. **Executable Issues**
   - Download ulang dari [releases page](https://github.com/IMPHNEN/malaz/releases)
   - Pastikan executable memiliki permission yang benar
   - Check antivirus software yang mungkin block executable

### Debug Mode

Enable verbose logging:

```bash
export MALAZ_DEBUG=1
python malaz_cli.py
```

Atau untuk pre-built executable:
```bash
export MALAZ_DEBUG=1
malaz
```

## 🏗️ Build Status

| Platform | Status | Latest Release |
|----------|--------|----------------|
| Windows  | [![Windows](https://github.com/IMPHNEN/malaz/workflows/Build%20and%20Release/badge.svg?branch=release)](https://github.com/IMPHNEN/malaz/actions) | [Download](https://github.com/IMPHNEN/malaz/releases/latest) |
| Linux    | [![Linux](https://github.com/IMPHNEN/malaz/workflows/Build%20and%20Release/badge.svg?branch=release)](https://github.com/IMPHNEN/malaz/actions) | [Download](https://github.com/IMPHNEN/malaz/releases/latest) |
| macOS    | [![macOS](https://github.com/IMPHNEN/malaz/workflows/Build%20and%20Release/badge.svg?branch=release)](https://github.com/IMPHNEN/malaz/actions) | [Download](https://github.com/IMPHNEN/malaz/releases/latest) |

## 🤝 Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI untuk GPT API
- Rich library untuk beautiful CLI output
- Python community untuk ecosystem yang luar biasa

## 📞 Support

Jika ada pertanyaan atau issue:

1. Check [troubleshooting section](#-troubleshooting)
2. Search existing issues
3. Create new issue dengan detail lengkap
4. Join komunitas developer untuk diskusi

---

**Happy Coding with Malaz! 🚀** 