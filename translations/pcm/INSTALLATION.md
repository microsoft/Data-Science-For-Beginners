<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-11-18T18:15:45+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "pcm"
}
-->
# Installation Guide

Dis guide go help you set up your environment to work with di Data Science for Beginners curriculum.

## Table of Contents

- [Prerequisites](../..)
- [Quick Start Options](../..)
- [Local Installation](../..)
- [Verify Your Installation](../..)

## Prerequisites

Before you start, you go need:

- Small sabi of command line/terminal
- GitHub account (free)
- Good internet connection for di first setup

## Quick Start Options

### Option 1: GitHub Codespaces (We recommend am for Beginners)

Di easiest way to start na with GitHub Codespaces, e go give you complete development environment inside your browser.

1. Go di [repository](https://github.com/microsoft/Data-Science-For-Beginners)
2. Click di **Code** dropdown menu
3. Select di **Codespaces** tab
4. Click **Create codespace on main**
5. Wait make di environment initialize (2-3 minutes)

Your environment don ready with all di dependencies wey dem don pre-install!

### Option 2: Local Development

If you wan work for your own computer, follow di detailed instructions wey dey below.

## Local Installation

### Step 1: Install Git

You go need Git to clone di repository and track your changes.

**Windows:**
- Download am from [git-scm.com](https://git-scm.com/download/win)
- Run di installer with di default settings

**macOS:**
- Install am with Homebrew: `brew install git`
- Or download am from [git-scm.com](https://git-scm.com/download/mac)

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

### Step 2: Clone di Repository

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Step 3: Install Python and Jupyter

You go need Python 3.7 or higher for di data science lessons.

**Windows:**
1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, check "Add Python to PATH"
3. Verify di installation:
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

E good make you use virtual environment to keep di dependencies separate.

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

Install di data science libraries wey you need:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Step 6: Install Node.js and npm (For Quiz App)

Di quiz app need Node.js and npm.

**Windows/macOS:**
- Download am from [nodejs.org](https://nodejs.org/) (LTS version we recommend)
- Run di installer

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

For offline access to di documentation:

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

Your browser go open with di Jupyter interface. You fit now navigate go any lesson `.ipynb` file.

### Test Quiz Application

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Di quiz app go dey available for `http://localhost:8080` (or another port if 8080 dey busy).

### Test Documentation Server

```bash
# From the root directory of the repository
docsify serve
```

Di documentation go dey available for `http://localhost:3000`.

## Using VS Code Dev Containers

If you get Docker installed, you fit use VS Code Dev Containers:

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Install [Visual Studio Code](https://code.visualstudio.com/)
3. Install di [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Open di repository for VS Code
5. Press `F1` and select "Remote-Containers: Reopen in Container"
6. Wait make di container build (first time only)

## Next Steps

- Check di [README.md](README.md) for overview of di curriculum
- Read [USAGE.md](USAGE.md) for common workflows and examples
- Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md) if you get issues
- Review [CONTRIBUTING.md](CONTRIBUTING.md) if you wan contribute

## Getting Help

If you get issues:

1. Check di [TROUBLESHOOTING.md](TROUBLESHOOTING.md) guide
2. Search di existing [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Join our [Discord community](https://aka.ms/ds4beginners/discord)
4. Create new issue with detailed information about your problem

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) take translate am. Even though we dey try make e accurate, abeg sabi say automated translations fit get mistake or no correct well. Di original document for di native language na di main correct source. For important information, e good make una use professional human translation. We no go dey responsible for any misunderstanding or wrong interpretation wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->