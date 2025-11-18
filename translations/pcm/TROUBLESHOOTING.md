<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-11-18T18:16:38+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "pcm"
}
-->
# Troubleshooting Guide

Dis guide dey show solution to common wahala wey fit happen wen you dey use Data Science for Beginners curriculum.

## Table of Contents

- [Python and Jupyter Wahala](../..)
- [Package and Dependency Wahala](../..)
- [Jupyter Notebook Wahala](../..)
- [Quiz Application Wahala](../..)
- [Git and GitHub Wahala](../..)
- [Docsify Documentation Wahala](../..)
- [Data and File Wahala](../..)
- [Performance Wahala](../..)
- [How to Get Extra Help](../..)

## Python and Jupyter Wahala

### Python No Dey or Wrong Version

**Wahala:** `python: command not found` or wrong Python version

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
1. Install Python again from [python.org](https://www.python.org/)
2. Wen you dey install am, tick "Add Python to PATH"
3. Restart your terminal/command prompt

### Virtual Environment No Gree Activate

**Wahala:** Virtual environment no gree activate

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

**Check say e activate:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter Kernel Wahala

**Wahala:** "Kernel no dey" or "Kernel dey die anyhow"

**Solution:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Wahala:** Wrong Python version for Jupyter

**Solution:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Package and Dependency Wahala

### Import Errors

**Wahala:** `ModuleNotFoundError: No module named 'pandas'` (or other packages)

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

### Pip Installation Wahala

**Wahala:** `pip install` dey fail with permission wahala

**Solution:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Wahala:** `pip install` dey fail with SSL certificate wahala

**Solution:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Package Version Wahala

**Wahala:** Package versions no dey compatible

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

## Jupyter Notebook Wahala

### Jupyter No Gree Start

**Wahala:** `jupyter notebook` command no dey

**Solution:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook No Gree Load or Save

**Wahala:** "Notebook no fit load" or save dey fail

**Solution:**

1. Check file permissions
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Check say file no spoil
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Clear Jupyter cache
```bash
jupyter notebook --clear-cache
```

### Cell No Gree Run

**Wahala:** Cell dey stuck for "In [*]" or e dey take forever

**Solution:**

1. **Interrupt kernel**: Click "Interrupt" button or press `I, I`
2. **Restart kernel**: Kernel menu → Restart
3. **Check say no be infinite loop dey your code**
4. **Clear output**: Cell → All Output → Clear

### Plots No Dey Show

**Wahala:** `matplotlib` plots no dey show for notebook

**Solution:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Another way for interactive plots:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Quiz Application Wahala

### npm install Dey Fail

**Wahala:** Errors dey happen wen you run `npm install`

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

### Quiz App No Gree Start

**Wahala:** `npm run serve` dey fail

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

### Port Don Already Dey Use

**Wahala:** "Port 8080 don already dey use"

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

### Quiz No Dey Load or Blank Page

**Wahala:** Quiz app dey load but na blank page e dey show

**Solution:**

1. Check browser console for errors (F12)
2. Clear browser cache and cookies
3. Try another browser
4. Make sure say JavaScript dey enabled
5. Check say ad blockers no dey disturb

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git and GitHub Wahala

### Git No Dey Recognize

**Wahala:** `git: command not found`

**Solution:**

**Windows:**
- Install Git from [git-scm.com](https://git-scm.com/)
- Restart terminal after installation

**macOS:**

> **Note:** If Homebrew no dey your system, follow the instructions for [https://brew.sh/](https://brew.sh/) to install am first.
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

### Clone Dey Fail

**Wahala:** `git clone` dey fail with authentication wahala

**Solution:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Permission Denied (publickey)

**Wahala:** SSH key authentication dey fail

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

## Docsify Documentation Wahala

### Docsify Command No Dey

**Wahala:** `docsify: command not found`

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

### Documentation No Dey Load

**Wahala:** Docsify dey serve but content no dey load

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

### Images No Dey Show

**Wahala:** Images dey show broken link icon

**Solution:**

1. Check say image paths dey correct
2. Make sure say image files dey inside the repository
3. Clear browser cache
4. Confirm say file extensions dey match (case-sensitive for some systems)

## Data and File Wahala

### File No Dey Errors

**Wahala:** `FileNotFoundError` wen you dey load data

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

### CSV Reading Wahala

**Wahala:** Errors dey happen wen you dey read CSV files

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

### Memory Wahala with Big Datasets

**Wahala:** `MemoryError` wen you dey load big files

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

## Performance Wahala

### Notebook Dey Slow

**Wahala:** Notebooks dey run very slow

**Solution:**

1. **Restart kernel and clear output**
   - Kernel → Restart & Clear Output

2. **Close notebooks wey you no dey use**

3. **Make your code better:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Use sample for big datasets:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Browser Dey Crash

**Wahala:** Browser dey crash or e no dey respond

**Solution:**

1. Close tabs wey you no dey use
2. Clear browser cache
3. Add browser memory (Chrome: `chrome://settings/system`)
4. Use JupyterLab instead:
```bash
pip install jupyterlab
jupyter lab
```

## How to Get Extra Help

### Before You Ask for Help

1. Check dis troubleshooting guide
2. Search [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Read [INSTALLATION.md](INSTALLATION.md) and [USAGE.md](USAGE.md)
4. Search the error message online

### How to Ask for Help

Wen you dey create issue or dey ask for help, include:

1. **Operating System**: Windows, macOS, or Linux (which distribution)
2. **Python Version**: Run `python --version`
3. **Error Message**: Copy the full error message
4. **Steps to Reproduce**: Wetin you do before the wahala happen
5. **Wetin You Don Try**: Solutions wey you don already try

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) take translate am. Even though we dey try make sure say e correct, abeg sabi say automatic translation fit get mistake or no dey accurate well. Di original dokyument for im native language na di main correct source. For important information, e go beta make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->