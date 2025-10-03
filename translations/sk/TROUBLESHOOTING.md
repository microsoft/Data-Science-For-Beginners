<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:46:35+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "sk"
}
-->
# Príručka na riešenie problémov

Táto príručka poskytuje riešenia bežných problémov, s ktorými sa môžete stretnúť pri práci s učebnými materiálmi Data Science for Beginners.

## Obsah

- [Problémy s Pythonom a Jupyterom](../..)
- [Problémy s balíkmi a závislosťami](../..)
- [Problémy s Jupyter Notebookom](../..)
- [Problémy s aplikáciou kvízu](../..)
- [Problémy s Gitom a GitHubom](../..)
- [Problémy s dokumentáciou Docsify](../..)
- [Problémy s dátami a súbormi](../..)
- [Problémy s výkonom](../..)
- [Získanie ďalšej pomoci](../..)

## Problémy s Pythonom a Jupyterom

### Python nie je nájdený alebo má nesprávnu verziu

**Problém:** `python: command not found` alebo nesprávna verzia Pythonu

**Riešenie:**

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

**Riešenie pre Windows:**
1. Preinštalujte Python z [python.org](https://www.python.org/)
2. Počas inštalácie zaškrtnite "Add Python to PATH"
3. Reštartujte terminál/command prompt

### Problémy s aktiváciou virtuálneho prostredia

**Problém:** Virtuálne prostredie sa neaktivuje

**Riešenie:**

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

**Overenie aktivácie:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Problémy s Jupyter kernelom

**Problém:** "Kernel not found" alebo "Kernel keeps dying"

**Riešenie:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Problém:** Nesprávna verzia Pythonu v Jupyteri

**Riešenie:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Problémy s balíkmi a závislosťami

### Chyby pri importe

**Problém:** `ModuleNotFoundError: No module named 'pandas'` (alebo iné balíky)

**Riešenie:**

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

### Zlyhanie inštalácie cez pip

**Problém:** `pip install` zlyhá s chybami povolení

**Riešenie:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Problém:** `pip install` zlyhá s chybami SSL certifikátov

**Riešenie:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Konflikty verzií balíkov

**Problém:** Nezlučiteľné verzie balíkov

**Riešenie:**

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

## Problémy s Jupyter Notebookom

### Jupyter sa nespustí

**Problém:** Príkaz `jupyter notebook` nie je nájdený

**Riešenie:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook sa nenačíta alebo neuloží

**Problém:** "Notebook failed to load" alebo chyby pri ukladaní

**Riešenie:**

1. Skontrolujte povolenia súborov
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Skontrolujte poškodenie súborov
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Vymažte cache Jupytera
```bash
jupyter notebook --clear-cache
```

### Bunky sa nevykonávajú

**Problém:** Bunky sú zaseknuté na "In [*]" alebo trvajú príliš dlho

**Riešenie:**

1. **Prerušte kernel**: Kliknite na tlačidlo "Interrupt" alebo stlačte `I, I`
2. **Reštartujte kernel**: Menu Kernel → Restart
3. **Skontrolujte nekonečné slučky** vo vašom kóde
4. **Vymažte výstup**: Cell → All Output → Clear

### Grafy sa nezobrazujú

**Problém:** Grafy z `matplotlib` sa nezobrazujú v notebooku

**Riešenie:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternatíva pre interaktívne grafy:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Problémy s aplikáciou kvízu

### Zlyhanie npm install

**Problém:** Chyby počas `npm install`

**Riešenie:**

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

### Aplikácia kvízu sa nespustí

**Problém:** `npm run serve` zlyhá

**Riešenie:**

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

### Port je už obsadený

**Problém:** "Port 8080 is already in use"

**Riešenie:**

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

### Kvíz sa nenačíta alebo prázdna stránka

**Problém:** Aplikácia kvízu sa načíta, ale zobrazuje prázdnu stránku

**Riešenie:**

1. Skontrolujte chyby v konzole prehliadača (F12)
2. Vymažte cache a cookies prehliadača
3. Skúste iný prehliadač
4. Uistite sa, že JavaScript je povolený
5. Skontrolujte, či adblockery nezasahujú

```bash
# Rebuild the app
npm run build
npm run serve
```

## Problémy s Gitom a GitHubom

### Git nie je rozpoznaný

**Problém:** `git: command not found`

**Riešenie:**

**Windows:**
- Nainštalujte Git z [git-scm.com](https://git-scm.com/)
- Po inštalácii reštartujte terminál

**macOS:**

> **Poznámka:** Ak nemáte nainštalovaný Homebrew, postupujte podľa pokynov na [https://brew.sh/](https://brew.sh/) na jeho inštaláciu.
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

### Zlyhanie klonovania

**Problém:** `git clone` zlyhá s chybami autentifikácie

**Riešenie:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Permission Denied (publickey)

**Problém:** Zlyhanie autentifikácie pomocou SSH kľúča

**Riešenie:**

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

## Problémy s dokumentáciou Docsify

### Príkaz Docsify nie je nájdený

**Problém:** `docsify: command not found`

**Riešenie:**

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

### Dokumentácia sa nenačíta

**Problém:** Docsify sa spustí, ale obsah sa nenačíta

**Riešenie:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Obrázky sa nezobrazujú

**Problém:** Obrázky zobrazujú ikonu zlomeného odkazu

**Riešenie:**

1. Skontrolujte, či sú cesty k obrázkom relatívne
2. Uistite sa, že súbory obrázkov existujú v repozitári
3. Vymažte cache prehliadača
4. Overte, či sa zhodujú prípony súborov (na niektorých systémoch sú citlivé na veľkosť písmen)

## Problémy s dátami a súbormi

### Chyby File Not Found

**Problém:** `FileNotFoundError` pri načítaní dát

**Riešenie:**

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

### Chyby pri čítaní CSV

**Problém:** Chyby pri čítaní CSV súborov

**Riešenie:**

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

### Chyby pamäte pri veľkých datasetoch

**Problém:** `MemoryError` pri načítaní veľkých súborov

**Riešenie:**

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

## Problémy s výkonom

### Pomalý výkon notebooku

**Problém:** Notebooky bežia veľmi pomaly

**Riešenie:**

1. **Reštartujte kernel a vymažte výstup**
   - Kernel → Restart & Clear Output

2. **Zatvorte nepoužívané notebooky**

3. **Optimalizujte kód:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Vzorkujte veľké datasety:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Zlyhanie prehliadača

**Problém:** Prehliadač zlyhá alebo sa stane nereagujúcim

**Riešenie:**

1. Zatvorte nepoužívané karty
2. Vymažte cache prehliadača
3. Zvýšte pamäť prehliadača (Chrome: `chrome://settings/system`)
4. Použite JupyterLab namiesto:
```bash
pip install jupyterlab
jupyter lab
```

## Získanie ďalšej pomoci

### Predtým, než požiadate o pomoc

1. Skontrolujte túto príručku na riešenie problémov
2. Vyhľadajte [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Prezrite si [INSTALLATION.md](INSTALLATION.md) a [USAGE.md](USAGE.md)
4. Skúste vyhľadať chybové hlásenie online

### Ako požiadať o pomoc

Pri vytváraní problému alebo žiadosti o pomoc uveďte:

1. **Operačný systém**: Windows, macOS alebo Linux (ktorá distribúcia)
2. **Verzia Pythonu**: Spustite `python --version`
3. **Chybové hlásenie**: Skopírujte celé chybové hlásenie
4. **Kroky na reprodukciu**: Čo ste urobili pred výskytom chyby
5. **Čo ste už vyskúšali**: Riešenia, ktoré ste už skúšali

**Príklad:**
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

### Komunitné zdroje

- **GitHub Issues**: [Vytvorte problém](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Pripojte sa ku komunite](https://aka.ms/ds4beginners/discord)
- **Diskusie**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Fóra otázok a odpovedí](https://docs.microsoft.com/answers/)

### Súvisiaca dokumentácia

- [INSTALLATION.md](INSTALLATION.md) - Pokyny na nastavenie
- [USAGE.md](USAGE.md) - Ako používať učebné materiály
- [CONTRIBUTING.md](CONTRIBUTING.md) - Ako prispievať
- [README.md](README.md) - Prehľad projektu

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.