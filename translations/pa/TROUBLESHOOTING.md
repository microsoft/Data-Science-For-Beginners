<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:36:52+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "pa"
}
-->
# ਸਮੱਸਿਆ ਹੱਲ ਗਾਈਡ

ਇਹ ਗਾਈਡ ਤੁਹਾਨੂੰ Data Science for Beginners ਕੋਰਸ ਦੇ ਦੌਰਾਨ ਆਉਣ ਵਾਲੀਆਂ ਆਮ ਸਮੱਸਿਆਵਾਂ ਦੇ ਹੱਲ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ।

## ਸੂਚੀ

- [Python ਅਤੇ Jupyter ਸਮੱਸਿਆਵਾਂ](../..)
- [ਪੈਕੇਜ ਅਤੇ Dependency ਸਮੱਸਿਆਵਾਂ](../..)
- [Jupyter Notebook ਸਮੱਸਿਆਵਾਂ](../..)
- [Quiz ਐਪਲੀਕੇਸ਼ਨ ਸਮੱਸਿਆਵਾਂ](../..)
- [Git ਅਤੇ GitHub ਸਮੱਸਿਆਵਾਂ](../..)
- [Docsify ਦਸਤਾਵੇਜ਼ ਸਮੱਸਿਆਵਾਂ](../..)
- [ਡਾਟਾ ਅਤੇ ਫਾਈਲ ਸਮੱਸਿਆਵਾਂ](../..)
- [ਪ੍ਰਦਰਸ਼ਨ ਸਮੱਸਿਆਵਾਂ](../..)
- [ਵਧੇਰੇ ਮਦਦ ਪ੍ਰਾਪਤ ਕਰਨਾ](../..)

## Python ਅਤੇ Jupyter ਸਮੱਸਿਆਵਾਂ

### Python ਨਾ ਮਿਲਣਾ ਜਾਂ ਗਲਤ ਵਰਜਨ

**ਸਮੱਸਿਆ:** `python: command not found` ਜਾਂ ਗਲਤ Python ਵਰਜਨ

**ਹੱਲ:**

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

**Windows ਹੱਲ:**
1. [python.org](https://www.python.org/) ਤੋਂ Python ਨੂੰ ਮੁੜ ਇੰਸਟਾਲ ਕਰੋ।
2. ਇੰਸਟਾਲੇਸ਼ਨ ਦੌਰਾਨ, "Add Python to PATH" ਚੈੱਕ ਕਰੋ।
3. ਆਪਣਾ ਟਰਮੀਨਲ/ਕਮਾਂਡ ਪ੍ਰਾਂਪਟ ਰੀਸਟਾਰਟ ਕਰੋ।

### Virtual Environment Activation ਸਮੱਸਿਆਵਾਂ

**ਸਮੱਸਿਆ:** Virtual environment ਐਕਟੀਵੇਟ ਨਹੀਂ ਹੋ ਰਿਹਾ

**ਹੱਲ:**

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

**ਐਕਟੀਵੇਸ਼ਨ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter Kernel ਸਮੱਸਿਆਵਾਂ

**ਸਮੱਸਿਆ:** "Kernel not found" ਜਾਂ "Kernel keeps dying"

**ਹੱਲ:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**ਸਮੱਸਿਆ:** Jupyter ਵਿੱਚ ਗਲਤ Python ਵਰਜਨ

**ਹੱਲ:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## ਪੈਕੇਜ ਅਤੇ Dependency ਸਮੱਸਿਆਵਾਂ

### Import Errors

**ਸਮੱਸਿਆ:** `ModuleNotFoundError: No module named 'pandas'` (ਜਾਂ ਹੋਰ ਪੈਕੇਜ)

**ਹੱਲ:**

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

**ਸਮੱਸਿਆ:** `pip install` permission errors ਨਾਲ ਫੇਲ੍ਹ ਹੋ ਜਾਂਦਾ ਹੈ

**ਹੱਲ:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**ਸਮੱਸਿਆ:** `pip install` SSL certificate errors ਨਾਲ ਫੇਲ੍ਹ ਹੋ ਜਾਂਦਾ ਹੈ

**ਹੱਲ:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### ਪੈਕੇਜ ਵਰਜਨ ਸੰਘਰਸ਼

**ਸਮੱਸਿਆ:** ਅਣਕੁਲ ਪੈਕੇਜ ਵਰਜਨ

**ਹੱਲ:**

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

## Jupyter Notebook ਸਮੱਸਿਆਵਾਂ

### Jupyter ਸ਼ੁਰੂ ਨਹੀਂ ਹੁੰਦਾ

**ਸਮੱਸਿਆ:** `jupyter notebook` ਕਮਾਂਡ ਨਹੀਂ ਮਿਲੀ

**ਹੱਲ:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook ਲੋਡ ਜਾਂ ਸੇਵ ਨਹੀਂ ਹੁੰਦਾ

**ਸਮੱਸਿਆ:** "Notebook failed to load" ਜਾਂ ਸੇਵ ਕਰਨ ਵਿੱਚ ਗਲਤੀਆਂ

**ਹੱਲ:**

1. ਫਾਈਲ permissions ਚੈੱਕ ਕਰੋ
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. ਫਾਈਲ ਕਰਪਸ਼ਨ ਚੈੱਕ ਕਰੋ
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Jupyter cache ਕਲੀਅਰ ਕਰੋ
```bash
jupyter notebook --clear-cache
```

### Cell ਚਲਦਾ ਨਹੀਂ

**ਸਮੱਸਿਆ:** Cell "In [*]" 'ਤੇ ਅਟਕ ਜਾਂਦਾ ਹੈ ਜਾਂ ਬਹੁਤ ਸਮਾਂ ਲੈਂਦਾ ਹੈ

**ਹੱਲ:**

1. **Kernel interrupt ਕਰੋ**: "Interrupt" ਬਟਨ 'ਤੇ ਕਲਿੱਕ ਕਰੋ ਜਾਂ `I, I` ਦਬਾਓ।
2. **Kernel ਰੀਸਟਾਰਟ ਕਰੋ**: Kernel menu → Restart
3. **Infinite loops** ਲਈ ਆਪਣੇ ਕੋਡ ਦੀ ਜਾਂਚ ਕਰੋ।
4. **Output ਕਲੀਅਰ ਕਰੋ**: Cell → All Output → Clear

### Plots ਦਿਖਾਈ ਨਹੀਂ ਦੇ ਰਹੇ

**ਸਮੱਸਿਆ:** `matplotlib` ਦੇ plots notebook ਵਿੱਚ ਨਹੀਂ ਦਿਖ ਰਹੇ

**ਹੱਲ:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**ਇੰਟਰੈਕਟਿਵ plots ਲਈ ਵਿਕਲਪ:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Quiz ਐਪਲੀਕੇਸ਼ਨ ਸਮੱਸਿਆਵਾਂ

### npm install ਫੇਲ੍ਹ

**ਸਮੱਸਿਆ:** `npm install` ਦੌਰਾਨ errors

**ਹੱਲ:**

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

### Quiz ਐਪ ਸ਼ੁਰੂ ਨਹੀਂ ਹੁੰਦੀ

**ਸਮੱਸਿਆ:** `npm run serve` ਫੇਲ੍ਹ

**ਹੱਲ:**

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

### Port ਪਹਿਲਾਂ ਹੀ ਵਰਤੋਂ ਵਿੱਚ ਹੈ

**ਸਮੱਸਿਆ:** "Port 8080 is already in use"

**ਹੱਲ:**

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

### Quiz ਲੋਡ ਨਹੀਂ ਹੋ ਰਿਹਾ ਜਾਂ ਖਾਲੀ ਪੇਜ

**ਸਮੱਸਿਆ:** Quiz ਐਪ ਲੋਡ ਹੁੰਦੀ ਹੈ ਪਰ ਖਾਲੀ ਪੇਜ ਦਿਖਾਉਂਦੀ ਹੈ

**ਹੱਲ:**

1. ਬ੍ਰਾਊਜ਼ਰ console ਵਿੱਚ errors ਚੈੱਕ ਕਰੋ (F12)
2. ਬ੍ਰਾਊਜ਼ਰ cache ਅਤੇ cookies ਕਲੀਅਰ ਕਰੋ
3. ਵੱਖਰੇ ਬ੍ਰਾਊਜ਼ਰ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ
4. ਯਕੀਨੀ ਬਣਾਓ ਕਿ JavaScript ਐਨੇਬਲ ਹੈ
5. Ad blockers ਦੀ ਜਾਂਚ ਕਰੋ ਜੋ ਰੁਕਾਵਟ ਪੈਦਾ ਕਰ ਰਹੇ ਹੋਣ

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git ਅਤੇ GitHub ਸਮੱਸਿਆਵਾਂ

### Git ਪਛਾਣਿਆ ਨਹੀਂ ਗਿਆ

**ਸਮੱਸਿਆ:** `git: command not found`

**ਹੱਲ:**

**Windows:**
- [git-scm.com](https://git-scm.com/) ਤੋਂ Git ਇੰਸਟਾਲ ਕਰੋ।
- ਇੰਸਟਾਲੇਸ਼ਨ ਤੋਂ ਬਾਅਦ ਟਰਮੀਨਲ ਰੀਸਟਾਰਟ ਕਰੋ।

**macOS:**

> **ਨੋਟ:** ਜੇਕਰ ਤੁਹਾਡੇ ਕੋਲ Homebrew ਇੰਸਟਾਲ ਨਹੀਂ ਹੈ, ਤਾਂ ਪਹਿਲਾਂ [https://brew.sh/](https://brew.sh/) 'ਤੇ ਦਿੱਤੀਆਂ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ।
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

### Clone ਫੇਲ੍ਹ

**ਸਮੱਸਿਆ:** `git clone` authentication errors ਨਾਲ ਫੇਲ੍ਹ

**ਹੱਲ:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Permission Denied (publickey)

**ਸਮੱਸਿਆ:** SSH key authentication ਫੇਲ੍ਹ

**ਹੱਲ:**

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

## Docsify ਦਸਤਾਵੇਜ਼ ਸਮੱਸਿਆਵਾਂ

### Docsify ਕਮਾਂਡ ਨਹੀਂ ਮਿਲੀ

**ਸਮੱਸਿਆ:** `docsify: command not found`

**ਹੱਲ:**

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

### ਦਸਤਾਵੇਜ਼ ਲੋਡ ਨਹੀਂ ਹੋ ਰਿਹਾ

**ਸਮੱਸਿਆ:** Docsify serve ਕਰਦਾ ਹੈ ਪਰ ਸਮੱਗਰੀ ਲੋਡ ਨਹੀਂ ਹੁੰਦੀ

**ਹੱਲ:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### ਚਿੱਤਰ ਦਿਖਾਈ ਨਹੀਂ ਦੇ ਰਹੇ

**ਸਮੱਸਿਆ:** ਚਿੱਤਰ ਟੁੱਟੇ ਹੋਏ ਲਿੰਕ ਆਈਕਨ ਦਿਖਾਉਂਦੇ ਹਨ

**ਹੱਲ:**

1. ਚਿੱਤਰ ਦੇ paths ਨੂੰ ਚੈੱਕ ਕਰੋ ਕਿ ਉਹ ਸਹੀ ਹਨ।
2. ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਚਿੱਤਰ ਫਾਈਲਾਂ repository ਵਿੱਚ ਮੌਜੂਦ ਹਨ।
3. ਬ੍ਰਾਊਜ਼ਰ cache ਕਲੀਅਰ ਕਰੋ।
4. ਫਾਈਲ extensions ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ (ਕੁਝ ਸਿਸਟਮਾਂ 'ਤੇ case-sensitive).

## ਡਾਟਾ ਅਤੇ ਫਾਈਲ ਸਮੱਸਿਆਵਾਂ

### File Not Found Errors

**ਸਮੱਸਿਆ:** `FileNotFoundError` ਡਾਟਾ ਲੋਡ ਕਰਦੇ ਸਮੇਂ

**ਹੱਲ:**

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

### CSV ਪੜ੍ਹਨ ਦੀਆਂ ਗਲਤੀਆਂ

**ਸਮੱਸਿਆ:** CSV ਫਾਈਲਾਂ ਪੜ੍ਹਨ ਵਿੱਚ ਗਲਤੀਆਂ

**ਹੱਲ:**

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

### ਵੱਡੇ ਡਾਟਾਸੈਟ ਨਾਲ Memory Errors

**ਸਮੱਸਿਆ:** `MemoryError` ਵੱਡੀਆਂ ਫਾਈਲਾਂ ਲੋਡ ਕਰਦੇ ਸਮੇਂ

**ਹੱਲ:**

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

## ਪ੍ਰਦਰਸ਼ਨ ਸਮੱਸਿਆਵਾਂ

### Notebook ਦੀ ਧੀਮੀ ਪ੍ਰਦਰਸ਼ਨ

**ਸਮੱਸਿਆ:** Notebook ਬਹੁਤ ਧੀਮੀ ਚੱਲਦੀ ਹੈ

**ਹੱਲ:**

1. **Kernel ਰੀਸਟਾਰਟ ਕਰੋ ਅਤੇ output ਕਲੀਅਰ ਕਰੋ**
   - Kernel → Restart & Clear Output

2. **ਅਣਵਰਤ Notebook ਬੰਦ ਕਰੋ**

3. **ਕੋਡ ਨੂੰ optimize ਕਰੋ:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **ਵੱਡੇ ਡਾਟਾਸੈਟ ਨੂੰ sample ਕਰੋ:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### ਬ੍ਰਾਊਜ਼ਰ Crash

**ਸਮੱਸਿਆ:** ਬ੍ਰਾਊਜ਼ਰ crash ਜਾਂ ਅਣਜਵਾਬ ਹੋ ਜਾਂਦਾ ਹੈ

**ਹੱਲ:**

1. ਅਣਵਰਤ tabs ਬੰਦ ਕਰੋ।
2. ਬ੍ਰਾਊਜ਼ਰ cache ਕਲੀਅਰ ਕਰੋ।
3. ਬ੍ਰਾਊਜ਼ਰ memory ਵਧਾਓ (Chrome: `chrome://settings/system`)
4. JupyterLab ਦੀ ਵਰਤੋਂ ਕਰੋ:
```bash
pip install jupyterlab
jupyter lab
```

## ਵਧੇਰੇ ਮਦਦ ਪ੍ਰਾਪਤ ਕਰਨਾ

### ਮਦਦ ਮੰਗਣ ਤੋਂ ਪਹਿਲਾਂ

1. ਇਸ troubleshooting ਗਾਈਡ ਦੀ ਜਾਂਚ ਕਰੋ।
2. [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) ਵਿੱਚ ਖੋਜ ਕਰੋ।
3. [INSTALLATION.md](INSTALLATION.md) ਅਤੇ [USAGE.md](USAGE.md) ਦੀ ਸਮੀਖਾ ਕਰੋ।
4. Error message ਨੂੰ ਆਨਲਾਈਨ ਖੋਜਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ।

### ਮਦਦ ਮੰਗਣ ਦਾ ਤਰੀਕਾ

Issue ਬਣਾਉਣ ਜਾਂ ਮਦਦ ਮੰਗਣ ਸਮੇਂ, ਇਹ ਸ਼ਾਮਲ ਕਰੋ:

1. **Operating System**: Windows, macOS, ਜਾਂ Linux (ਕਿਹੜਾ distribution)
2. **Python Version**: `python --version` ਚਲਾਓ।
3. **Error Message**: ਪੂਰਾ error message ਕਾਪੀ ਕਰੋ।
4. **Steps to Reproduce**: Error ਤੋਂ ਪਹਿਲਾਂ ਕੀ ਕੀਤਾ।
5. **What You've Tried**: ਜੋ ਹੱਲ ਤੁਸੀਂ ਪਹਿਲਾਂ ਹੀ ਅਜ਼ਮਾਏ ਹਨ।

**ਉਦਾਹਰਨ:**
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

- **GitHub Issues**: [Issue ਬਣਾਓ](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [ਸਾਡੇ community ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ](https://aka.ms/ds4beginners/discord)
- **Discussions**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Q&A Forums](https://docs.microsoft.com/answers/)

### ਸੰਬੰਧਿਤ ਦਸਤਾਵੇਜ਼

- [INSTALLATION.md](INSTALLATION.md) - ਸੈਟਅੱਪ ਹਦਾਇਤਾਂ
- [USAGE.md](USAGE.md) - ਕੋਰਸ ਦੀ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰਨੀ ਹੈ
- [CONTRIBUTING.md](CONTRIBUTING.md) - ਯੋਗਦਾਨ ਦੇਣ ਦਾ ਤਰੀਕਾ
- [README.md](README.md) - ਪ੍ਰੋਜੈਕਟ ਦਾ ਜਾਇਜ਼ਾ

---

**ਅਸਵੀਕਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਣੀਕਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਮੂਲ ਰੂਪ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।