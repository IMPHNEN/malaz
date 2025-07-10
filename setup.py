from setuptools import setup, find_packages

setup(
    name='malaz',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'openai',
        'python-dotenv',
        'rich',
        'pygments',
        'watchdog',
        'astunparse',
        'dotenv'
    ],
    entry_points={
        'console_scripts': [
            'malaz = malaz_cli:main'
        ]
    },
    python_requires='>=3.8',
    author='IMPHNEN',
    description='Malaz AI Coding Assistant CLI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/IMPHNEN/malaz',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)