<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:48:59+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "sl"
}
-->
# Vodnik za odpravljanje težav

Ta vodnik ponuja rešitve za pogoste težave, s katerimi se lahko srečate med delom s kurikulumom "Data Science for Beginners".

## Kazalo

- [Težave s Pythonom in Jupyterjem](../..)
- [Težave s paketi in odvisnostmi](../..)
- [Težave z Jupyter Notebookom](../..)
- [Težave z aplikacijo za kvize](../..)
- [Težave z Gitom in GitHubom](../..)
- [Težave z dokumentacijo Docsify](../..)
- [Težave s podatki in datotekami](../..)
- [Težave z zmogljivostjo](../..)
- [Dodatna pomoč](../..)

## Težave s Pythonom in Jupyterjem

### Python ni najden ali napačna različica

**Težava:** `python: command not found` ali napačna različica Pythona

**Rešitev:**

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

**Rešitev za Windows:**
1. Ponovno namestite Python s [python.org](https://www.python.org/)
2. Med namestitvijo označite "Add Python to PATH"
3. Znova zaženite terminal/ukazno vrstico

### Težave z aktivacijo virtualnega okolja

**Težava:** Virtualno okolje se ne aktivira

**Rešitev:**

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

**Preverite aktivacijo:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Težave z jedrom Jupyterja

**Težava:** "Jedro ni najdeno" ali "Jedro se nenehno ustavlja"

**Rešitev:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Težava:** Napačna različica Pythona v Jupyterju

**Rešitev:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Težave s paketi in odvisnostmi

### Napake pri uvozu

**Težava:** `ModuleNotFoundError: No module named 'pandas'` (ali drugi paketi)

**Rešitev:**

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

### Napake pri namestitvi s pip

**Težava:** `pip install` ne uspe zaradi težav z dovoljenji

**Rešitev:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Težava:** `pip install` ne uspe zaradi težav s SSL certifikatom

**Rešitev:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Konflikti med različicami paketov

**Težava:** Nepovezljive različice paketov

**Rešitev:**

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

## Težave z Jupyter Notebookom

### Jupyter se ne zažene

**Težava:** Ukaz `jupyter notebook` ni najden

**Rešitev:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Zvezek se ne naloži ali shrani

**Težava:** "Zvezek ni uspel naložiti" ali napake pri shranjevanju

**Rešitev:**

1. Preverite dovoljenja za datoteke
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Preverite, ali je datoteka poškodovana
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Počistite predpomnilnik Jupyterja
```bash
jupyter notebook --clear-cache
```

### Celica se ne izvrši

**Težava:** Celica ostane na "In [*]" ali traja predolgo

**Rešitev:**

1. **Prekinite jedro:** Kliknite gumb "Interrupt" ali pritisnite `I, I`
2. **Znova zaženite jedro:** Meni Kernel → Restart
3. **Preverite, ali je v kodi neskončna zanka**
4. **Počistite izhod:** Cell → All Output → Clear

### Grafi se ne prikazujejo

**Težava:** Grafi `matplotlib` se ne prikažejo v zvezku

**Rešitev:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternativa za interaktivne grafe:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Težave z aplikacijo za kvize

### Napake pri `npm install`

**Težava:** Napake med `npm install`

**Rešitev:**

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

### Aplikacija za kvize se ne zažene

**Težava:** `npm run serve` ne uspe

**Rešitev:**

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

### Vrata so že v uporabi

**Težava:** "Port 8080 is already in use"

**Rešitev:**

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

### Kviz se ne naloži ali prikaže prazno stran

**Težava:** Aplikacija za kvize se naloži, vendar prikaže prazno stran

**Rešitev:**

1. Preverite napake v konzoli brskalnika (F12)
2. Počistite predpomnilnik in piškotke brskalnika
3. Poskusite z drugim brskalnikom
4. Prepričajte se, da je JavaScript omogočen
5. Preverite, ali adblockerji motijo delovanje

```bash
# Rebuild the app
npm run build
npm run serve
```

## Težave z Gitom in GitHubom

### Git ni prepoznan

**Težava:** `git: command not found`

**Rešitev:**

**Windows:**
- Namestite Git s [git-scm.com](https://git-scm.com/)
- Po namestitvi znova zaženite terminal

**macOS:**

> **Opomba:** Če Homebrew ni nameščen, sledite navodilom na [https://brew.sh/](https://brew.sh/) za namestitev.
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

### Napake pri kloniranju

**Težava:** `git clone` ne uspe zaradi težav z avtentikacijo

**Rešitev:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Dovoljenje zavrnjeno (publickey)

**Težava:** Avtentikacija z SSH ključem ne uspe

**Rešitev:**

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

## Težave z dokumentacijo Docsify

### Ukaz Docsify ni najden

**Težava:** `docsify: command not found`

**Rešitev:**

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

### Dokumentacija se ne naloži

**Težava:** Docsify se zažene, vendar vsebina ni naložena

**Rešitev:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Slike se ne prikazujejo

**Težava:** Slike prikazujejo ikono zlomljene povezave

**Rešitev:**

1. Preverite, ali so poti do slik relativne
2. Prepričajte se, da slike obstajajo v repozitoriju
3. Počistite predpomnilnik brskalnika
4. Preverite, ali se končnice datotek ujemajo (občutljivo na velike/male črke na nekaterih sistemih)

## Težave s podatki in datotekami

### Napake "Datoteka ni najdena"

**Težava:** `FileNotFoundError` pri nalaganju podatkov

**Rešitev:**

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

### Napake pri branju CSV datotek

**Težava:** Napake pri branju CSV datotek

**Rešitev:**

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

### Napake pomnilnika pri velikih podatkovnih nizih

**Težava:** `MemoryError` pri nalaganju velikih datotek

**Rešitev:**

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

## Težave z zmogljivostjo

### Počasno delovanje zvezkov

**Težava:** Zvezki delujejo zelo počasi

**Rešitev:**

1. **Znova zaženite jedro in počistite izhod**
   - Kernel → Restart & Clear Output

2. **Zaprite neuporabljene zvezke**

3. **Optimizirajte kodo:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Vzorec velikih podatkovnih nizov:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Zrušitve brskalnika

**Težava:** Brskalnik se zruši ali postane neodziven

**Rešitev:**

1. Zaprite neuporabljene zavihke
2. Počistite predpomnilnik brskalnika
3. Povečajte pomnilnik brskalnika (Chrome: `chrome://settings/system`)
4. Uporabite JupyterLab namesto:
```bash
pip install jupyterlab
jupyter lab
```

## Dodatna pomoč

### Preden zaprosite za pomoč

1. Preverite ta vodnik za odpravljanje težav
2. Poiščite [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Preglejte [INSTALLATION.md](INSTALLATION.md) in [USAGE.md](USAGE.md)
4. Poskusite poiskati sporočilo o napaki na spletu

### Kako zaprositi za pomoč

Ko ustvarjate težavo ali zaprosite za pomoč, vključite:

1. **Operacijski sistem**: Windows, macOS ali Linux (katero distribucijo)
2. **Različica Pythona**: Zaženite `python --version`
3. **Sporočilo o napaki**: Kopirajte celotno sporočilo o napaki
4. **Koraki za reprodukcijo**: Kaj ste naredili pred pojavom napake
5. **Kaj ste že poskusili**: Rešitve, ki ste jih že preizkusili

**Primer:**
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

### Viri skupnosti

- **GitHub Issues**: [Ustvarite težavo](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Pridružite se naši skupnosti](https://aka.ms/ds4beginners/discord)
- **Razprave**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Forumi za vprašanja in odgovore](https://docs.microsoft.com/answers/)

### Povezana dokumentacija

- [INSTALLATION.md](INSTALLATION.md) - Navodila za nastavitev
- [USAGE.md](USAGE.md) - Kako uporabljati kurikulum
- [CONTRIBUTING.md](CONTRIBUTING.md) - Kako prispevati
- [README.md](README.md) - Pregled projekta

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.