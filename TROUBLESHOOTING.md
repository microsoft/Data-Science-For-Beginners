# Troubleshooting Guide

This guide provides solutions to common issues you might encounter while working with the Data Science for Beginners curriculum.

## Table of Contents

- [Python and Jupyter Issues](#python-and-jupyter-issues)
- [Package and Dependency Issues](#package-and-dependency-issues)
- [Jupyter Notebook Issues](#jupyter-notebook-issues)
- [Quiz Application Issues](#quiz-application-issues)
- [Git and GitHub Issues](#git-and-github-issues)
- [Docsify Documentation Issues](#docsify-documentation-issues)
- [Data and File Issues](#data-and-file-issues)
- [Performance Issues](#performance-issues)
- [Getting Additional Help](#getting-additional-help)

## Python and Jupyter Issues

### Python Not Found or Wrong Version

**Problem:** `python: command not found` or wrong Python version

**Solution:**

```bash
# Check Python version
python --version
python3 --version

# If Python 3 is installed as 'python3', create an alias
# On macOS/Linux, add to ~/.bashrc or ~/.zshrc:
alias python=python3
alias pip=pip3

# Or use python3 explicitly
python3 -m pip install jupyter
```

**Windows Solution:**
1. Reinstall Python from [python.org](https://www.python.org/)
2. During installation, check "Add Python to PATH"
3. Restart your terminal/command prompt

### Virtual Environment Activation Issues

**Problem:** Virtual environment won't activate

**Solution:**

**Windows:**
```bash
# If you get execution policy error
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
venv\Scripts\activate
```

**macOS/Linux:**
```bash
# Ensure the activate script is executable
chmod +x venv/bin/activate

# Then activate
source venv/bin/activate
```

**Verify activation:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter Kernel Issues

**Problem:** "Kernel not found" or "Kernel keeps dying"

**Solution:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Problem:** Wrong Python version in Jupyter

**Solution:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Package and Dependency Issues

### Import Errors

**Problem:** `ModuleNotFoundError: No module named 'pandas'` (or other packages)

**Solution:**

```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install missing package
pip install pandas

# Install all common packages
pip install jupyter pandas numpy matplotlib seaborn scikit-learn

# Verify installation
python -c "import pandas; print(pandas.__version__)"
```

### Pip Installation Failures

**Problem:** `pip install` fails with permission errors

**Solution:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Problem:** `pip install` fails with SSL certificate errors

**Solution:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Package Version Conflicts

**Problem:** Incompatible package versions

**Solution:**

```bash
# Create fresh virtual environment
python -m venv venv-new
source venv-new/bin/activate  # or venv-new\Scripts\activate on Windows

# Install packages with specific versions if needed
pip install pandas==1.3.0
pip install numpy==1.21.0

# Or let pip resolve dependencies
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

## Jupyter Notebook Issues

### Jupyter Won't Start

**Problem:** `jupyter notebook` command not found

**Solution:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook Won't Load or Save

**Problem:** "Notebook failed to load" or save errors

**Solution:**

1. Check file permissions
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Check for file corruption
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Clear Jupyter cache
```bash
jupyter notebook --clear-cache
```

### Cell Won't Execute

**Problem:** Cell stuck on "In [*]" or takes forever

**Solution:**

1. **Interrupt the kernel**: Click "Interrupt" button or press `I, I`
2. **Restart kernel**: Kernel menu → Restart
3. **Check for infinite loops** in your code
4. **Clear output**: Cell → All Output → Clear

### Plots Not Displaying

**Problem:** `matplotlib` plots don't show in notebook

**Solution:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternative for interactive plots:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Quiz Application Issues

### npm install Fails

**Problem:** Errors during `npm install`

**Solution:**

```bash
# Clear npm cache
npm cache clean --force

# Remove node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Reinstall
npm install

# If still failing, try with legacy peer deps
npm install --legacy-peer-deps
```

### Quiz App Won't Start

**Problem:** `npm run serve` fails

**Solution:**

```bash
# Check Node.js version
node --version  # Should be 12.x or higher

# Reinstall dependencies
cd quiz-app
rm -rf node_modules package-lock.json
npm install

# Try different port
npm run serve -- --port 8081
```

### Port Already in Use

**Problem:** "Port 8080 is already in use"

**Solution:**

```bash
# Find and kill process on port 8080
# macOS/Linux:
lsof -ti:8080 | xargs kill -9

# Windows:
netstat -ano | findstr :8080
taskkill /PID <PID> /F

# Or use a different port
npm run serve -- --port 8081
```

### Quiz Not Loading or Blank Page

**Problem:** Quiz app loads but shows blank page

**Solution:**

1. Check browser console for errors (F12)
2. Clear browser cache and cookies
3. Try a different browser
4. Ensure JavaScript is enabled
5. Check for ad blockers interfering

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git and GitHub Issues

### Git Not Recognized

**Problem:** `git: command not found`

**Solution:**

**Windows:**
- Install Git from [git-scm.com](https://git-scm.com/)
- Restart terminal after installation

**macOS:**

> **Note:** If you do not have Homebrew installed, follow the instructions at [https://brew.sh/](https://brew.sh/) to install it first.
```bash
# Install via Homebrew
brew install git

# Or install Xcode Command Line Tools
xcode-select --install
```

**Linux:**
```bash
sudo apt-get install git  # Debian/Ubuntu
sudo dnf install git      # Fedora
```

### Clone Fails

**Problem:** `git clone` fails with authentication errors

**Solution:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Permission Denied (publickey)

**Problem:** SSH key authentication fails

**Solution:**

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add key to ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Add public key to GitHub
# Copy key: cat ~/.ssh/id_ed25519.pub
# Add at: https://github.com/settings/keys
```

## Docsify Documentation Issues

### Docsify Command Not Found

**Problem:** `docsify: command not found`

**Solution:**

```bash
# Install globally
npm install -g docsify-cli

# If permission error on macOS/Linux
sudo npm install -g docsify-cli

# Verify installation
docsify --version

# If still not found, add npm global path
# Find npm global path
npm config get prefix

# Add to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH="$PATH:/usr/local/bin"
```

### Documentation Not Loading

**Problem:** Docsify serves but content doesn't load

**Solution:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Images Not Displaying

**Problem:** Images show broken link icon

**Solution:**

1. Check image paths are relative
2. Ensure image files exist in the repository
3. Clear browser cache
4. Verify file extensions match (case-sensitive on some systems)

## Data and File Issues

### File Not Found Errors

**Problem:** `FileNotFoundError` when loading data

**Solution:**

```python
import os

# Check current working directory
print(os.getcwd())

# Use absolute path
data_path = os.path.join(os.getcwd(), 'data', 'filename.csv')
df = pd.read_csv(data_path)

# Or use relative path from notebook location
df = pd.read_csv('../data/filename.csv')

# Verify file exists
print(os.path.exists('data/filename.csv'))
```

### CSV Reading Errors

**Problem:** Errors reading CSV files

**Solution:**

```python
import pandas as pd

# Try different encodings
df = pd.read_csv('file.csv', encoding='utf-8')
# or
df = pd.read_csv('file.csv', encoding='latin-1')
# or
df = pd.read_csv('file.csv', encoding='ISO-8859-1')

# Handle missing values
df = pd.read_csv('file.csv', na_values=['NA', 'N/A', ''])

# Specify delimiter if not comma
df = pd.read_csv('file.csv', delimiter=';')
```

### Memory Errors with Large Datasets

**Problem:** `MemoryError` when loading large files

**Solution:**

```python
# Read in chunks
chunk_size = 10000
chunks = []
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # Process chunk
    chunks.append(chunk)
df = pd.concat(chunks)

# Or read specific columns only
df = pd.read_csv('file.csv', usecols=['col1', 'col2'])

# Use more efficient data types
df = pd.read_csv('file.csv', dtype={'column_name': 'int32'})
```

## Performance Issues

### Slow Notebook Performance

**Problem:** Notebooks run very slowly

**Solution:**

1. **Restart kernel and clear output**
   - Kernel → Restart & Clear Output

2. **Close unused notebooks**

3. **Optimize code:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Sample large datasets:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Browser Crashes

**Problem:** Browser crashes or becomes unresponsive

**Solution:**

1. Close unused tabs
2. Clear browser cache
3. Increase browser memory (Chrome: `chrome://settings/system`)
4. Use JupyterLab instead:
```bash
pip install jupyterlab
jupyter lab
```

## Getting Additional Help

### Before Asking for Help

1. Check this troubleshooting guide
2. Search [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Review [INSTALLATION.md](INSTALLATION.md) and [USAGE.md](USAGE.md)
4. Try searching the error message online

### How to Ask for Help

When creating an issue or asking for help, include:

1. **Operating System**: Windows, macOS, or Linux (which distribution)
2. **Python Version**: Run `python --version`
3. **Error Message**: Copy the complete error message
4. **Steps to Reproduce**: What you did before the error occurred
5. **What You've Tried**: Solutions you've already attempted

**Example:**
```
**Operating System:** macOS 12.0
**Python Version:** 3.9.7
**Error Message:** ModuleNotFoundError: No module named 'pandas'
**Steps to Reproduce:**
1. Activated virtual environment
2. Started Jupyter notebook
3. Tried to import pandas

**What I've Tried:**
- Ran pip install pandas
- Restarted Jupyter
```

### Community Resources

- **GitHub Issues**: [Create an issue](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Join our community](https://aka.ms/ds4beginners/discord)
- **Discussions**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Q&A Forums](https://docs.microsoft.com/answers/)

### Related Documentation

- [INSTALLATION.md](INSTALLATION.md) - Setup instructions
- [USAGE.md](USAGE.md) - How to use the curriculum
- [CONTRIBUTING.md](CONTRIBUTING.md) - How to contribute
- [README.md](README.md) - Project overview
