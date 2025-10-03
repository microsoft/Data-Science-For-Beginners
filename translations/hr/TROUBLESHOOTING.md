<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:48:31+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "hr"
}
-->
# Vodič za rješavanje problema

Ovaj vodič pruža rješenja za uobičajene probleme na koje možete naići dok radite s kurikulumom "Data Science for Beginners".

## Sadržaj

- [Problemi s Pythonom i Jupyterom](../..)
- [Problemi s paketima i ovisnostima](../..)
- [Problemi s Jupyter Notebookom](../..)
- [Problemi s aplikacijom za kviz](../..)
- [Problemi s Gitom i GitHubom](../..)
- [Problemi s dokumentacijom Docsify](../..)
- [Problemi s podacima i datotekama](../..)
- [Problemi s performansama](../..)
- [Dobivanje dodatne pomoći](../..)

## Problemi s Pythonom i Jupyterom

### Python nije pronađen ili je pogrešna verzija

**Problem:** `python: command not found` ili pogrešna verzija Pythona

**Rješenje:**

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

**Rješenje za Windows:**
1. Ponovno instalirajte Python s [python.org](https://www.python.org/)
2. Tijekom instalacije označite opciju "Add Python to PATH"
3. Ponovno pokrenite terminal/command prompt

### Problemi s aktivacijom virtualnog okruženja

**Problem:** Virtualno okruženje se ne aktivira

**Rješenje:**

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

**Provjera aktivacije:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Problemi s Jupyter kernelom

**Problem:** "Kernel nije pronađen" ili "Kernel stalno prestaje raditi"

**Rješenje:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Problem:** Pogrešna verzija Pythona u Jupyteru

**Rješenje:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Problemi s paketima i ovisnostima

### Pogreške pri uvozu

**Problem:** `ModuleNotFoundError: No module named 'pandas'` (ili drugi paketi)

**Rješenje:**

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

### Neuspjeh instalacije putem pipa

**Problem:** `pip install` ne uspijeva zbog problema s dozvolama

**Rješenje:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Problem:** `pip install` ne uspijeva zbog SSL certifikata

**Rješenje:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Sukobi verzija paketa

**Problem:** Nepodudarne verzije paketa

**Rješenje:**

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

## Problemi s Jupyter Notebookom

### Jupyter se ne pokreće

**Problem:** `jupyter notebook` naredba nije pronađena

**Rješenje:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook se ne učitava ili ne sprema

**Problem:** "Notebook nije uspio učitati" ili pogreške pri spremanju

**Rješenje:**

1. Provjerite dozvole za datoteke
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Provjerite je li datoteka oštećena
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Očistite Jupyter cache
```bash
jupyter notebook --clear-cache
```

### Ćelija se ne izvršava

**Problem:** Ćelija je zaglavljena na "In [*]" ili traje predugo

**Rješenje:**

1. **Prekinite kernel**: Kliknite na gumb "Interrupt" ili pritisnite `I, I`
2. **Ponovno pokrenite kernel**: Izbornik Kernel → Restart
3. **Provjerite ima li beskonačnih petlji** u vašem kodu
4. **Očistite izlaz**: Cell → All Output → Clear

### Grafovi se ne prikazuju

**Problem:** `matplotlib` grafovi se ne prikazuju u notebooku

**Rješenje:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternativa za interaktivne grafove:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Problemi s aplikacijom za kviz

### Neuspjeh `npm install`

**Problem:** Pogreške tijekom `npm install`

**Rješenje:**

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

### Aplikacija za kviz se ne pokreće

**Problem:** `npm run serve` ne uspijeva

**Rješenje:**

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

### Port je već zauzet

**Problem:** "Port 8080 je već zauzet"

**Rješenje:**

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

### Kviz se ne učitava ili prikazuje praznu stranicu

**Problem:** Aplikacija za kviz se učitava, ali prikazuje praznu stranicu

**Rješenje:**

1. Provjerite konzolu preglednika za pogreške (F12)
2. Očistite cache i kolačiće preglednika
3. Pokušajte s drugim preglednikom
4. Provjerite je li JavaScript omogućen
5. Provjerite ometaju li blokatori oglasa

```bash
# Rebuild the app
npm run build
npm run serve
```

## Problemi s Gitom i GitHubom

### Git nije prepoznat

**Problem:** `git: command not found`

**Rješenje:**

**Windows:**
- Instalirajte Git s [git-scm.com](https://git-scm.com/)
- Ponovno pokrenite terminal nakon instalacije

**macOS:**

> **Napomena:** Ako nemate instaliran Homebrew, slijedite upute na [https://brew.sh/](https://brew.sh/) za instalaciju.
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

### Neuspjeh kloniranja

**Problem:** `git clone` ne uspijeva zbog problema s autentifikacijom

**Rješenje:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Dozvola odbijena (publickey)

**Problem:** Autentifikacija putem SSH ključa ne uspijeva

**Rješenje:**

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

## Problemi s dokumentacijom Docsify

### Naredba Docsify nije pronađena

**Problem:** `docsify: command not found`

**Rješenje:**

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

### Dokumentacija se ne učitava

**Problem:** Docsify se pokreće, ali sadržaj se ne učitava

**Rješenje:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Slike se ne prikazuju

**Problem:** Slike prikazuju ikonu slomljene veze

**Rješenje:**

1. Provjerite jesu li putanje slika relativne
2. Provjerite postoje li datoteke slika u repozitoriju
3. Očistite cache preglednika
4. Provjerite odgovaraju li ekstenzije datoteka (osjetljivo na velika/mala slova na nekim sustavima)

## Problemi s podacima i datotekama

### Pogreške "Datoteka nije pronađena"

**Problem:** `FileNotFoundError` prilikom učitavanja podataka

**Rješenje:**

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

### Pogreške pri čitanju CSV datoteka

**Problem:** Pogreške pri čitanju CSV datoteka

**Rješenje:**

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

### Problemi s memorijom kod velikih skupova podataka

**Problem:** `MemoryError` prilikom učitavanja velikih datoteka

**Rješenje:**

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

## Problemi s performansama

### Sporo izvođenje notebooka

**Problem:** Notebooki se izvode vrlo sporo

**Rješenje:**

1. **Ponovno pokrenite kernel i očistite izlaz**
   - Kernel → Restart & Clear Output

2. **Zatvorite nepotrebne notebooke**

3. **Optimizirajte kod:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Uzmite uzorak velikih skupova podataka:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Preglednik se ruši

**Problem:** Preglednik se ruši ili postaje neodgovarajući

**Rješenje:**

1. Zatvorite nepotrebne kartice
2. Očistite cache preglednika
3. Povećajte memoriju preglednika (Chrome: `chrome://settings/system`)
4. Koristite JupyterLab umjesto toga:
```bash
pip install jupyterlab
jupyter lab
```

## Dobivanje dodatne pomoći

### Prije traženja pomoći

1. Provjerite ovaj vodič za rješavanje problema
2. Pretražite [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Pregledajte [INSTALLATION.md](INSTALLATION.md) i [USAGE.md](USAGE.md)
4. Pokušajte pretražiti poruku o pogrešci na internetu

### Kako zatražiti pomoć

Kada kreirate problem ili tražite pomoć, uključite:

1. **Operativni sustav**: Windows, macOS ili Linux (koja distribucija)
2. **Verzija Pythona**: Pokrenite `python --version`
3. **Poruka o pogrešci**: Kopirajte kompletnu poruku o pogrešci
4. **Koraci za reprodukciju**: Što ste radili prije nego što se dogodila pogreška
5. **Što ste već pokušali**: Rješenja koja ste već isprobali

**Primjer:**
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

### Resursi zajednice

- **GitHub Issues**: [Kreirajte problem](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Pridružite se našoj zajednici](https://aka.ms/ds4beginners/discord)
- **Diskusije**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Q&A Forumi](https://docs.microsoft.com/answers/)

### Povezana dokumentacija

- [INSTALLATION.md](INSTALLATION.md) - Upute za postavljanje
- [USAGE.md](USAGE.md) - Kako koristiti kurikulum
- [CONTRIBUTING.md](CONTRIBUTING.md) - Kako doprinijeti
- [README.md](README.md) - Pregled projekta

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.