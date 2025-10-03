<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:44:40+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "tl"
}
-->
# Gabay sa Pag-aayos ng Problema

Ang gabay na ito ay nagbibigay ng mga solusyon sa mga karaniwang isyu na maaaring maranasan habang ginagamit ang kurikulum ng Data Science for Beginners.

## Talaan ng Nilalaman

- [Mga Isyu sa Python at Jupyter](../..)
- [Mga Isyu sa Package at Dependency](../..)
- [Mga Isyu sa Jupyter Notebook](../..)
- [Mga Isyu sa Quiz Application](../..)
- [Mga Isyu sa Git at GitHub](../..)
- [Mga Isyu sa Docsify Documentation](../..)
- [Mga Isyu sa Data at File](../..)
- [Mga Isyu sa Performance](../..)
- [Pagkuha ng Karagdagang Tulong](../..)

## Mga Isyu sa Python at Jupyter

### Hindi Natagpuan ang Python o Mali ang Bersyon

**Problema:** `python: command not found` o maling bersyon ng Python

**Solusyon:**

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

**Solusyon para sa Windows:**
1. I-reinstall ang Python mula sa [python.org](https://www.python.org/)
2. Sa panahon ng pag-install, i-check ang "Add Python to PATH"
3. I-restart ang iyong terminal/command prompt

### Mga Isyu sa Pag-activate ng Virtual Environment

**Problema:** Hindi ma-activate ang virtual environment

**Solusyon:**

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

**I-verify ang activation:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Mga Isyu sa Kernel ng Jupyter

**Problema:** "Kernel not found" o "Kernel keeps dying"

**Solusyon:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Problema:** Maling bersyon ng Python sa Jupyter

**Solusyon:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Mga Isyu sa Package at Dependency

### Mga Error sa Import

**Problema:** `ModuleNotFoundError: No module named 'pandas'` (o iba pang mga package)

**Solusyon:**

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

### Mga Pagkabigo sa Pag-install ng Pip

**Problema:** Nabigo ang `pip install` dahil sa mga error sa permiso

**Solusyon:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Problema:** Nabigo ang `pip install` dahil sa mga SSL certificate errors

**Solusyon:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Mga Konflikto sa Bersyon ng Package

**Problema:** Hindi magkatugma ang mga bersyon ng package

**Solusyon:**

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

## Mga Isyu sa Jupyter Notebook

### Hindi Nag-i-start ang Jupyter

**Problema:** `jupyter notebook` command not found

**Solusyon:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Hindi Naglo-load o Nagsa-save ang Notebook

**Problema:** "Notebook failed to load" o mga error sa pag-save

**Solusyon:**

1. Suriin ang mga permiso ng file
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Suriin kung may corruption sa file
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. I-clear ang cache ng Jupyter
```bash
jupyter notebook --clear-cache
```

### Hindi Nag-e-execute ang Cell

**Problema:** Cell stuck sa "In [*]" o sobrang tagal

**Solusyon:**

1. **I-interrupt ang kernel**: I-click ang "Interrupt" button o pindutin ang `I, I`
2. **I-restart ang kernel**: Kernel menu → Restart
3. **Suriin kung may infinite loops** sa iyong code
4. **I-clear ang output**: Cell → All Output → Clear

### Hindi Nagpapakita ang Plots

**Problema:** Hindi nagpapakita ang `matplotlib` plots sa notebook

**Solusyon:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternatibo para sa interactive plots:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Mga Isyu sa Quiz Application

### Nabigo ang npm install

**Problema:** Mga error sa panahon ng `npm install`

**Solusyon:**

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

### Hindi Nag-i-start ang Quiz App

**Problema:** Nabigo ang `npm run serve`

**Solusyon:**

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

### Port na Ginagamit Na

**Problema:** "Port 8080 is already in use"

**Solusyon:**

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

### Hindi Naglo-load o Blangkong Pahina ang Quiz

**Problema:** Naglo-load ang quiz app pero blangkong pahina ang ipinapakita

**Solusyon:**

1. Suriin ang console ng browser para sa mga error (F12)
2. I-clear ang cache at cookies ng browser
3. Subukan ang ibang browser
4. Siguraduhing naka-enable ang JavaScript
5. Suriin kung may ad blockers na nakakaabala

```bash
# Rebuild the app
npm run build
npm run serve
```

## Mga Isyu sa Git at GitHub

### Hindi Nakikilala ang Git

**Problema:** `git: command not found`

**Solusyon:**

**Windows:**
- I-install ang Git mula sa [git-scm.com](https://git-scm.com/)
- I-restart ang terminal pagkatapos ng pag-install

**macOS:**

> **Tandaan:** Kung wala kang Homebrew, sundin ang mga tagubilin sa [https://brew.sh/](https://brew.sh/) para i-install ito.
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

### Nabigo ang Clone

**Problema:** Nabigo ang `git clone` dahil sa mga authentication errors

**Solusyon:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Permission Denied (publickey)

**Problema:** Nabigo ang SSH key authentication

**Solusyon:**

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

## Mga Isyu sa Docsify Documentation

### Hindi Nakikilala ang Docsify Command

**Problema:** `docsify: command not found`

**Solusyon:**

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

### Hindi Naglo-load ang Dokumentasyon

**Problema:** Nagsa-serve ang Docsify pero hindi naglo-load ang content

**Solusyon:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Hindi Nagpapakita ang Mga Imahe

**Problema:** Nagpapakita ng broken link icon ang mga imahe

**Solusyon:**

1. Suriin kung relative ang mga path ng imahe
2. Siguraduhing umiiral ang mga file ng imahe sa repository
3. I-clear ang cache ng browser
4. I-verify kung tugma ang mga file extension (case-sensitive sa ilang sistema)

## Mga Isyu sa Data at File

### Mga Error sa File Not Found

**Problema:** `FileNotFoundError` kapag naglo-load ng data

**Solusyon:**

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

### Mga Error sa Pagbasa ng CSV

**Problema:** Mga error sa pagbasa ng mga CSV file

**Solusyon:**

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

### Mga Error sa Memorya sa Malalaking Dataset

**Problema:** `MemoryError` kapag naglo-load ng malalaking file

**Solusyon:**

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

## Mga Isyu sa Performance

### Mabagal na Performance ng Notebook

**Problema:** Mabagal ang takbo ng mga notebook

**Solusyon:**

1. **I-restart ang kernel at i-clear ang output**
   - Kernel → Restart & Clear Output

2. **Isara ang mga hindi ginagamit na notebook**

3. **I-optimize ang code:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Sample ang malalaking dataset:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Pag-crash ng Browser

**Problema:** Nagka-crash o hindi tumutugon ang browser

**Solusyon:**

1. Isara ang mga hindi ginagamit na tab
2. I-clear ang cache ng browser
3. Dagdagan ang memorya ng browser (Chrome: `chrome://settings/system`)
4. Gumamit ng JupyterLab:
```bash
pip install jupyterlab
jupyter lab
```

## Pagkuha ng Karagdagang Tulong

### Bago Humingi ng Tulong

1. Suriin ang gabay na ito sa pag-aayos ng problema
2. Maghanap sa [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Basahin ang [INSTALLATION.md](INSTALLATION.md) at [USAGE.md](USAGE.md)
4. Subukang hanapin ang error message online

### Paano Humingi ng Tulong

Kapag gumagawa ng isyu o humihingi ng tulong, isama ang:

1. **Operating System**: Windows, macOS, o Linux (alin na distribution)
2. **Python Version**: Patakbuhin ang `python --version`
3. **Error Message**: Kopyahin ang kumpletong error message
4. **Mga Hakbang para Ulitin**: Ano ang ginawa mo bago nangyari ang error
5. **Mga Sinubukan Mo Na**: Mga solusyon na sinubukan mo na

**Halimbawa:**
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

### Mga Resource ng Komunidad

- **GitHub Issues**: [Gumawa ng isyu](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Sumali sa aming komunidad](https://aka.ms/ds4beginners/discord)
- **Discussions**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Q&A Forums](https://docs.microsoft.com/answers/)

### Kaugnay na Dokumentasyon

- [INSTALLATION.md](INSTALLATION.md) - Mga tagubilin sa setup
- [USAGE.md](USAGE.md) - Paano gamitin ang kurikulum
- [CONTRIBUTING.md](CONTRIBUTING.md) - Paano mag-ambag
- [README.md](README.md) - Pangkalahatang-ideya ng proyekto

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.