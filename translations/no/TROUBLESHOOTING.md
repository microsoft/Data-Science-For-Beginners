<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:41:43+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "no"
}
-->
# Feilsøkingsguide

Denne guiden gir løsninger på vanlige problemer du kan støte på når du jobber med Data Science for Beginners-kurset.

## Innholdsfortegnelse

- [Python- og Jupyter-problemer](../..)
- [Pakke- og avhengighetsproblemer](../..)
- [Jupyter Notebook-problemer](../..)
- [Quiz-applikasjonsproblemer](../..)
- [Git- og GitHub-problemer](../..)
- [Docsify-dokumentasjonsproblemer](../..)
- [Data- og filproblemer](../..)
- [Ytelsesproblemer](../..)
- [Få ekstra hjelp](../..)

## Python- og Jupyter-problemer

### Python ikke funnet eller feil versjon

**Problem:** `python: command not found` eller feil Python-versjon

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

**Løsning for Windows:**
1. Installer Python på nytt fra [python.org](https://www.python.org/)
2. Under installasjonen, huk av for "Add Python to PATH"
3. Start terminalen/kommandoprompten på nytt

### Problemer med aktivering av virtuelt miljø

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

**Bekreft aktivering:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter-kjerneproblemer

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

**Problem:** Feil Python-versjon i Jupyter

**Løsning:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Pakke- og avhengighetsproblemer

### Importfeil

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

### Feil ved pip-installasjon

**Problem:** `pip install` feiler med tillatelsesfeil

**Løsning:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Problem:** `pip install` feiler med SSL-sertifikatfeil

**Løsning:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Konflikter mellom pakkeversjoner

**Problem:** Uforenlige pakkeversjoner

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

**Problem:** `jupyter notebook`-kommandoen ikke funnet

**Løsning:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook laster ikke eller lagrer ikke

**Problem:** "Notebook failed to load" eller lagringsfeil

**Løsning:**

1. Sjekk filrettigheter
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Sjekk for filkorrupsjon
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Tøm Jupyter-cache
```bash
jupyter notebook --clear-cache
```

### Celle kjører ikke

**Problem:** Celle sitter fast på "In [*]" eller tar evigheter

**Løsning:**

1. **Avbryt kjernen**: Klikk på "Interrupt"-knappen eller trykk `I, I`
2. **Start kjernen på nytt**: Kernel-meny → Restart
3. **Sjekk for uendelige løkker** i koden din
4. **Tøm utdata**: Cell → All Output → Clear

### Diagrammer vises ikke

**Problem:** `matplotlib`-diagrammer vises ikke i notebook

**Løsning:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternativ for interaktive diagrammer:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Quiz-applikasjonsproblemer

### npm install feiler

**Problem:** Feil under `npm install`

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

**Problem:** `npm run serve` feiler

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

### Port allerede i bruk

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

### Quiz laster ikke eller viser blank side

**Problem:** Quiz-appen laster, men viser blank side

**Løsning:**

1. Sjekk nettleserkonsollen for feil (F12)
2. Tøm nettleserens cache og informasjonskapsler
3. Prøv en annen nettleser
4. Sørg for at JavaScript er aktivert
5. Sjekk om annonseblokkerere forstyrrer

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git- og GitHub-problemer

### Git ikke gjenkjent

**Problem:** `git: command not found`

**Løsning:**

**Windows:**
- Installer Git fra [git-scm.com](https://git-scm.com/)
- Start terminalen på nytt etter installasjonen

**macOS:**

> **Merk:** Hvis du ikke har Homebrew installert, følg instruksjonene på [https://brew.sh/](https://brew.sh/) for å installere det først.
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

### Kloning feiler

**Problem:** `git clone` feiler med autentiseringsfeil

**Løsning:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Tillatelse nektet (publickey)

**Problem:** SSH-nøkkelautentisering feiler

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

## Docsify-dokumentasjonsproblemer

### Docsify-kommando ikke funnet

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

### Dokumentasjon laster ikke

**Problem:** Docsify serverer, men innholdet laster ikke

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

### Bilder vises ikke

**Problem:** Bilder viser ødelagt lenkeikon

**Løsning:**

1. Sjekk at bildefilbanene er relative
2. Sørg for at bildefilene finnes i depotet
3. Tøm nettleserens cache
4. Verifiser at filendelsene stemmer (skift-sensitivt på noen systemer)

## Data- og filproblemer

### Fil ikke funnet-feil

**Problem:** `FileNotFoundError` ved lasting av data

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

### Feil ved lesing av CSV

**Problem:** Feil ved lesing av CSV-filer

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

### Minnefeil med store datasett

**Problem:** `MemoryError` ved lasting av store filer

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

## Ytelsesproblemer

### Langsom ytelse i notebook

**Problem:** Notebook kjører veldig sakte

**Løsning:**

1. **Start kjernen på nytt og tøm utdata**
   - Kernel → Restart & Clear Output

2. **Lukk ubrukte notebooks**

3. **Optimaliser kode:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Bruk utvalg av store datasett:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Nettleser krasjer

**Problem:** Nettleseren krasjer eller blir uresponsiv

**Løsning:**

1. Lukk ubrukte faner
2. Tøm nettleserens cache
3. Øk nettleserens minne (Chrome: `chrome://settings/system`)
4. Bruk JupyterLab i stedet:
```bash
pip install jupyterlab
jupyter lab
```

## Få ekstra hjelp

### Før du ber om hjelp

1. Sjekk denne feilsøkingsguiden
2. Søk i [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Gå gjennom [INSTALLATION.md](INSTALLATION.md) og [USAGE.md](USAGE.md)
4. Prøv å søke etter feilmeldingen på nettet

### Hvordan be om hjelp

Når du oppretter en sak eller ber om hjelp, inkluder:

1. **Operativsystem**: Windows, macOS eller Linux (hvilken distribusjon)
2. **Python-versjon**: Kjør `python --version`
3. **Feilmelding**: Kopier hele feilmeldingen
4. **Steg for å gjenskape**: Hva du gjorde før feilen oppstod
5. **Hva du har prøvd**: Løsninger du allerede har forsøkt

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

### Fellesskapsressurser

- **GitHub Issues**: [Opprett en sak](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Bli med i fellesskapet vårt](https://aka.ms/ds4beginners/discord)
- **Diskusjoner**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Q&A-forum](https://docs.microsoft.com/answers/)

### Relatert dokumentasjon

- [INSTALLATION.md](INSTALLATION.md) - Installasjonsinstruksjoner
- [USAGE.md](USAGE.md) - Hvordan bruke kurset
- [CONTRIBUTING.md](CONTRIBUTING.md) - Hvordan bidra
- [README.md](README.md) - Prosjektoversikt

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.