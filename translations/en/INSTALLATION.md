<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:13:27+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "en"
}
-->
# Installation Guide

This guide will help you set up your environment to work with the Data Science for Beginners curriculum.

## Table of Contents

- [Prerequisites](../..)
- [Quick Start Options](../..)
- [Local Installation](../..)
- [Verify Your Installation](../..)

## Prerequisites

Before starting, you should have:

- Basic knowledge of command line/terminal usage
- A GitHub account (free)
- A stable internet connection for the initial setup

## Quick Start Options

### Option 1: GitHub Codespaces (Recommended for Beginners)

The simplest way to get started is by using GitHub Codespaces, which provides a complete development environment directly in your browser.

1. Go to the [repository](https://github.com/microsoft/Data-Science-For-Beginners)
2. Click the **Code** dropdown menu
3. Select the **Codespaces** tab
4. Click **Create codespace on main**
5. Wait for the environment to initialize (2-3 minutes)

Your environment is now ready with all dependencies pre-installed!

### Option 2: Local Development

If you prefer working on your own computer, follow the detailed instructions below.

## Local Installation

### Step 1: Install Git

Git is required to clone the repository and manage your changes.

**Windows:**
- Download from [git-scm.com](https://git-scm.com/download/win)
- Run the installer with default settings

**macOS:**
- Install via Homebrew: `brew install git`
- Or download from [git-scm.com](https://git-scm.com/download/mac)

**Linux:**
```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

### Step 2: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Step 3: Install Python and Jupyter

Python 3.7 or higher is required for the data science lessons.

**Windows:**
1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, check "Add Python to PATH"
3. Verify installation:
```bash
python --version
```

**macOS:**
```bash
# Using Homebrew
brew install python3

# Verify installation
python3 --version
```

**Linux:**
```bash
# Most Linux distributions come with Python pre-installed
python3 --version

# If not installed:
# Debian/Ubuntu
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

### Step 4: Set Up Python Environment

It is recommended to use a virtual environment to keep dependencies isolated.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 5: Install Python Packages

Install the required data science libraries:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Step 6: Install Node.js and npm (For Quiz App)

The quiz application requires Node.js and npm.

**Windows/macOS:**
- Download from [nodejs.org](https://nodejs.org/) (LTS version recommended)
- Run the installer

**Linux:**
```bash
# Debian/Ubuntu
# WARNING: Piping scripts from the internet directly into bash can be a security risk.
# It is recommended to review the script before running it:
#   curl -fsSL https://deb.nodesource.com/setup_lts.x -o setup_lts.x
#   less setup_lts.x
# Then run:
#   sudo -E bash setup_lts.x
#
# Alternatively, you can use the one-liner below at your own risk:
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# Fedora
sudo dnf install nodejs

# Verify installation
node --version
npm --version
```

### Step 7: Install Quiz App Dependencies

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Step 8: Install Docsify (Optional)

For offline access to documentation:

```bash
npm install -g docsify-cli
```

## Verify Your Installation

### Test Python and Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Your browser should open with the Jupyter interface. You can now navigate to any lesson's `.ipynb` file.

### Test Quiz Application

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

The quiz app should be accessible at `http://localhost:8080` (or another port if 8080 is already in use).

### Test Documentation Server

```bash
# From the root directory of the repository
docsify serve
```

The documentation should be accessible at `http://localhost:3000`.

## Using VS Code Dev Containers

If you have Docker installed, you can use VS Code Dev Containers:

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Install [Visual Studio Code](https://code.visualstudio.com/)
3. Install the [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Open the repository in VS Code
5. Press `F1` and select "Remote-Containers: Reopen in Container"
6. Wait for the container to build (only required the first time)

## Next Steps

- Explore the [README.md](README.md) for an overview of the curriculum
- Read [USAGE.md](USAGE.md) for common workflows and examples
- Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md) if you encounter issues
- Review [CONTRIBUTING.md](CONTRIBUTING.md) if you want to contribute

## Getting Help

If you run into issues:

1. Check the [TROUBLESHOOTING.md](TROUBLESHOOTING.md) guide
2. Search existing [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Join our [Discord community](https://aka.ms/ds4beginners/discord)
4. Create a new issue with detailed information about your problem

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.