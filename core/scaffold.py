import os
import json

class ProjectScaffolder:
    TEMPLATES = {
        "flask_web_app": {
            "description": "Basic Flask web application",
            "structure": {
                "app.py": "from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return 'Hello, World!'\n\nif __name__ == '__main__':\n    app.run(debug=True)",
                "templates/": None,
                "static/": None,
                "requirements.txt": "flask\n"
            }
        },
        "cli_tool": {
            "description": "Python CLI tool with argument parsing",
            "structure": {
                "main.py": "import argparse\n\ndef main():\n    parser = argparse.ArgumentParser(description='My CLI Tool')\n    parser.add_argument('input', help='Input file')\n    args = parser.parse_args()\n    print(f'Processing {args.input}')\n\nif __name__ == '__main__':\n    main()",
                "setup.py": "from setuptools import setup\n\nsetup(\n    name='my-tool',\n    version='0.1.0',\n    py_modules=['main'],\n    install_requires=[],\n    entry_points={\n        'console_scripts': [\n            'mytool = main:main',\n        ],\n    },\n)",
            }
        },
        "data_analysis": {
            "description": "Jupyter-based data analysis project",
            "structure": {
                "notebooks/exploratory.ipynb": json.dumps({
                    "cells": [
                        {
                            "cell_type": "code",
                            "execution_count": None,
                            "metadata": {},
                            "outputs": [],
                            "source": [
                                "import pandas as pd\n",
                                "import numpy as np\n",
                                "import matplotlib.pyplot as plt\n\n",
                                "# Load your data here\n",
                                "# df = pd.read_csv('data.csv')"
                            ]
                        }
                    ],
                    "metadata": {
                        "kernelspec": {
                            "display_name": "Python 3",
                            "language": "python",
                            "name": "python3"
                        }
                    },
                    "nbformat": 4,
                    "nbformat_minor": 4
                }, indent=2),
                "data/": None,
                "requirements.txt": "pandas\nnumpy\nmatplotlib\njupyter\n"
            }
        }
    }

    @classmethod
    def list_templates(cls):
        return [
            {"name": name, "description": data["description"]}
            for name, data in cls.TEMPLATES.items()
        ]

    def create_project(self, template_name, project_path):
        if template_name not in self.TEMPLATES:
            return f"Template '{template_name}' not found"
        
        if os.path.exists(project_path):
            return f"Path already exists: {project_path}"
        
        os.makedirs(project_path, exist_ok=True)
        template = self.TEMPLATES[template_name]["structure"]
        
        for path, content in template.items():
            full_path = os.path.join(project_path, path)
            
            if path.endswith('/'):
                os.makedirs(full_path, exist_ok=True)
            else:
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                with open(full_path, 'w') as f:
                    f.write(content)
        
        return f"Project created at {project_path} using template '{template_name}'"