<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:41:16+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "da"
}
-->
# Fejlfindingsguide

Denne guide giver løsninger på almindelige problemer, du kan støde på, mens du arbejder med Data Science for Beginners-kurset.

## Indholdsfortegnelse

- [Python og Jupyter-problemer](../..)
- [Pakke- og afhængighedsproblemer](../..)
- [Jupyter Notebook-problemer](../..)
- [Quiz-applikationsproblemer](../..)
- [Git og GitHub-problemer](../..)
- [Docsify-dokumentationsproblemer](../..)
- [Data- og filproblemer](../..)
- [Ydelsesproblemer](../..)
- [Få yderligere hjælp](../..)

## Python og Jupyter-problemer

### Python ikke fundet eller forkert version

**Problem:** `python: command not found` eller forkert Python-version

**Løsning:**

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

**Løsning til Windows:**
1. Geninstaller Python fra [python.org](https://www.python.org/)
2. Under installationen, marker "Add Python to PATH"
3. Genstart din terminal/kommandoprompt

### Problemer med aktivering af virtuel miljø

**Problem:** Virtuelt miljø aktiveres ikke

**Løsning:**

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

**Bekræft aktivering:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter Kernel-problemer

**Problem:** "Kernel not found" eller "Kernel keeps dying"

**Løsning:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Problem:** Forkert Python-version i Jupyter

**Løsning:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Pakke- og afhængighedsproblemer

### Importfejl

**Problem:** `ModuleNotFoundError: No module named 'pandas'` (eller andre pakker)

**Løsning:**

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

### Fejl ved pip-installation

**Problem:** `pip install` fejler med tilladelsesfejl

**Løsning:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Problem:** `pip install` fejler med SSL-certifikatfejl

**Løsning:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Konflikter mellem pakkeversioner

**Problem:** Uforenelige pakkeversioner

**Løsning:**

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

## Jupyter Notebook-problemer

### Jupyter starter ikke

**Problem:** `jupyter notebook` kommando ikke fundet

**Løsning:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook kan ikke indlæses eller gemmes

**Problem:** "Notebook failed to load" eller gemmefejl

**Løsning:**

1. Tjek filtilladelser
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Tjek for filkorruption
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Ryd Jupyter-cache
```bash
jupyter notebook --clear-cache
```

### Celle udføres ikke

**Problem:** Celle sidder fast på "In [*]" eller tager evigheder

**Løsning:**

1. **Afbryd kernen**: Klik på "Interrupt"-knappen eller tryk `I, I`
2. **Genstart kernen**: Kernel-menu → Restart
3. **Tjek for uendelige loops** i din kode
4. **Ryd output**: Cell → All Output → Clear

### Diagrammer vises ikke

**Problem:** `matplotlib` diagrammer vises ikke i notebook

**Løsning:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternativ til interaktive diagrammer:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Quiz-applikationsproblemer

### npm install fejler

**Problem:** Fejl under `npm install`

**Løsning:**

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

### Quiz-app starter ikke

**Problem:** `npm run serve` fejler

**Løsning:**

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

### Port allerede i brug

**Problem:** "Port 8080 is already in use"

**Løsning:**

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

### Quiz indlæses ikke eller viser tom side

**Problem:** Quiz-app indlæses, men viser tom side

**Løsning:**

1. Tjek browserkonsollen for fejl (F12)
2. Ryd browserens cache og cookies
3. Prøv en anden browser
4. Sørg for, at JavaScript er aktiveret
5. Tjek for adblockere, der kan forstyrre

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git og GitHub-problemer

### Git ikke genkendt

**Problem:** `git: command not found`

**Løsning:**

**Windows:**
- Installer Git fra [git-scm.com](https://git-scm.com/)
- Genstart terminalen efter installation

**macOS:**

> **Bemærk:** Hvis du ikke har Homebrew installeret, følg instruktionerne på [https://brew.sh/](https://brew.sh/) for at installere det først.
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

### Clone fejler

**Problem:** `git clone` fejler med autentificeringsfejl

**Løsning:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Tilladelse nægtet (publickey)

**Problem:** SSH-nøgleautentificering fejler

**Løsning:**

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

## Docsify-dokumentationsproblemer

### Docsify-kommando ikke fundet

**Problem:** `docsify: command not found`

**Løsning:**

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

### Dokumentation indlæses ikke

**Problem:** Docsify serverer, men indholdet indlæses ikke

**Løsning:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Billeder vises ikke

**Problem:** Billeder viser ikon for brudt link

**Løsning:**

1. Tjek, at billedstier er relative
2. Sørg for, at billedfiler findes i repository
3. Ryd browserens cache
4. Bekræft, at filendelser matcher (case-sensitive på nogle systemer)

## Data- og filproblemer

### Fil ikke fundet fejl

**Problem:** `FileNotFoundError` ved indlæsning af data

**Løsning:**

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

### Fejl ved læsning af CSV

**Problem:** Fejl ved læsning af CSV-filer

**Løsning:**

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

### Hukommelsesfejl med store datasæt

**Problem:** `MemoryError` ved indlæsning af store filer

**Løsning:**

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

## Ydelsesproblemer

### Langsom notebook-ydelse

**Problem:** Notebooks kører meget langsomt

**Løsning:**

1. **Genstart kernen og ryd output**
   - Kernel → Restart & Clear Output

2. **Luk ubrugte notebooks**

3. **Optimer kode:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Udtag store datasæt:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Browser går ned

**Problem:** Browser går ned eller bliver uresponsiv

**Løsning:**

1. Luk ubrugte faner
2. Ryd browserens cache
3. Øg browserens hukommelse (Chrome: `chrome://settings/system`)
4. Brug JupyterLab i stedet:
```bash
pip install jupyterlab
jupyter lab
```

## Få yderligere hjælp

### Før du beder om hjælp

1. Tjek denne fejlfindingsguide
2. Søg på [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Gennemgå [INSTALLATION.md](INSTALLATION.md) og [USAGE.md](USAGE.md)
4. Prøv at søge fejlmeddelelsen online

### Sådan beder du om hjælp

Når du opretter en issue eller beder om hjælp, inkluder:

1. **Operativsystem**: Windows, macOS eller Linux (hvilken distribution)
2. **Python-version**: Kør `python --version`
3. **Fejlmeddelelse**: Kopiér den komplette fejlmeddelelse
4. **Trin til reproduktion**: Hvad du gjorde, før fejlen opstod
5. **Hvad du har prøvet**: Løsninger, du allerede har forsøgt

**Eksempel:**
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

### Fællesskabsressourcer

- **GitHub Issues**: [Opret en issue](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Deltag i vores fællesskab](https://aka.ms/ds4beginners/discord)
- **Diskussioner**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Q&A-fora](https://docs.microsoft.com/answers/)

### Relateret dokumentation

- [INSTALLATION.md](INSTALLATION.md) - Installationsinstruktioner
- [USAGE.md](USAGE.md) - Sådan bruges kurset
- [CONTRIBUTING.md](CONTRIBUTING.md) - Sådan bidrager du
- [README.md](README.md) - Projektoversigt

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.