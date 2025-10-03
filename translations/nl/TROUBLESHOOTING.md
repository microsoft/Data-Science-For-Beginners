<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:42:39+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "nl"
}
-->
# Probleemoplossingsgids

Deze gids biedt oplossingen voor veelvoorkomende problemen die je kunt tegenkomen bij het werken met het curriculum Data Science voor Beginners.

## Inhoudsopgave

- [Python- en Jupyter-problemen](../..)
- [Pakket- en afhankelijkheidsproblemen](../..)
- [Jupyter Notebook-problemen](../..)
- [Quizapplicatieproblemen](../..)
- [Git- en GitHub-problemen](../..)
- [Docsify documentatieproblemen](../..)
- [Data- en bestandsproblemen](../..)
- [Prestatieproblemen](../..)
- [Extra hulp krijgen](../..)

## Python- en Jupyter-problemen

### Python niet gevonden of verkeerde versie

**Probleem:** `python: command not found` of verkeerde Python-versie

**Oplossing:**

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

**Oplossing voor Windows:**
1. Installeer Python opnieuw via [python.org](https://www.python.org/)
2. Vink tijdens de installatie "Add Python to PATH" aan
3. Herstart je terminal/command prompt

### Problemen met activering van virtuele omgeving

**Probleem:** Virtuele omgeving wordt niet geactiveerd

**Oplossing:**

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

**Controleer activering:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter Kernel-problemen

**Probleem:** "Kernel not found" of "Kernel blijft crashen"

**Oplossing:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Probleem:** Verkeerde Python-versie in Jupyter

**Oplossing:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Pakket- en afhankelijkheidsproblemen

### Importfouten

**Probleem:** `ModuleNotFoundError: No module named 'pandas'` (of andere pakketten)

**Oplossing:**

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

### Pip-installatiefouten

**Probleem:** `pip install` faalt met permissiefouten

**Oplossing:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Probleem:** `pip install` faalt met SSL-certificaatfouten

**Oplossing:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Pakketversieconflicten

**Probleem:** Onverenigbare pakketversies

**Oplossing:**

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

## Jupyter Notebook-problemen

### Jupyter start niet

**Probleem:** `jupyter notebook` command niet gevonden

**Oplossing:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook laadt niet of slaat niet op

**Probleem:** "Notebook failed to load" of opslagfouten

**Oplossing:**

1. Controleer bestandsrechten
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Controleer op corrupte bestanden
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Wis Jupyter-cache
```bash
jupyter notebook --clear-cache
```

### Cel voert niet uit

**Probleem:** Cel blijft hangen op "In [*]" of duurt erg lang

**Oplossing:**

1. **Onderbreek de kernel**: Klik op de knop "Interrupt" of druk op `I, I`
2. **Herstart kernel**: Kernel-menu → Restart
3. **Controleer op oneindige loops** in je code
4. **Wis uitvoer**: Cel → Alle uitvoer → Wissen

### Grafieken worden niet weergegeven

**Probleem:** `matplotlib`-grafieken worden niet weergegeven in notebook

**Oplossing:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternatief voor interactieve grafieken:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Quizapplicatieproblemen

### npm install faalt

**Probleem:** Fouten tijdens `npm install`

**Oplossing:**

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

### Quizapp start niet

**Probleem:** `npm run serve` faalt

**Oplossing:**

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

### Poort al in gebruik

**Probleem:** "Port 8080 is already in use"

**Oplossing:**

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

### Quiz laadt niet of lege pagina

**Probleem:** Quizapp laadt maar toont een lege pagina

**Oplossing:**

1. Controleer browserconsole op fouten (F12)
2. Wis browsercache en cookies
3. Probeer een andere browser
4. Zorg dat JavaScript is ingeschakeld
5. Controleer of adblockers interfereren

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git- en GitHub-problemen

### Git niet herkend

**Probleem:** `git: command not found`

**Oplossing:**

**Windows:**
- Installeer Git via [git-scm.com](https://git-scm.com/)
- Herstart terminal na installatie

**macOS:**

> **Let op:** Als je Homebrew niet hebt geïnstalleerd, volg de instructies op [https://brew.sh/](https://brew.sh/) om het eerst te installeren.
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

### Clone faalt

**Probleem:** `git clone` faalt met authenticatiefouten

**Oplossing:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Toegang geweigerd (publickey)

**Probleem:** SSH-sleutel authenticatie faalt

**Oplossing:**

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

## Docsify documentatieproblemen

### Docsify command niet gevonden

**Probleem:** `docsify: command not found`

**Oplossing:**

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

### Documentatie laadt niet

**Probleem:** Docsify wordt geserveerd maar inhoud laadt niet

**Oplossing:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Afbeeldingen worden niet weergegeven

**Probleem:** Afbeeldingen tonen een gebroken link-icoon

**Oplossing:**

1. Controleer of afbeeldingspaden relatief zijn
2. Zorg dat afbeeldingsbestanden bestaan in de repository
3. Wis browsercache
4. Controleer of bestandsextensies overeenkomen (hoofdlettergevoelig op sommige systemen)

## Data- en bestandsproblemen

### Bestand niet gevonden fouten

**Probleem:** `FileNotFoundError` bij het laden van data

**Oplossing:**

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

### CSV-leesfouten

**Probleem:** Fouten bij het lezen van CSV-bestanden

**Oplossing:**

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

### Geheugenfouten bij grote datasets

**Probleem:** `MemoryError` bij het laden van grote bestanden

**Oplossing:**

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

## Prestatieproblemen

### Trage notebookprestaties

**Probleem:** Notebooks werken erg traag

**Oplossing:**

1. **Herstart kernel en wis uitvoer**
   - Kernel → Restart & Clear Output

2. **Sluit ongebruikte notebooks**

3. **Optimaliseer code:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Neem steekproeven van grote datasets:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Browser crasht

**Probleem:** Browser crasht of reageert niet meer

**Oplossing:**

1. Sluit ongebruikte tabbladen
2. Wis browsercache
3. Verhoog browsergeheugen (Chrome: `chrome://settings/system`)
4. Gebruik JupyterLab in plaats van:
```bash
pip install jupyterlab
jupyter lab
```

## Extra hulp krijgen

### Voordat je om hulp vraagt

1. Controleer deze probleemoplossingsgids
2. Zoek in [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Bekijk [INSTALLATION.md](INSTALLATION.md) en [USAGE.md](USAGE.md)
4. Zoek de foutmelding online

### Hoe om hulp te vragen

Wanneer je een issue aanmaakt of om hulp vraagt, vermeld:

1. **Besturingssysteem**: Windows, macOS of Linux (welke distributie)
2. **Python-versie**: Voer `python --version` uit
3. **Foutmelding**: Kopieer de volledige foutmelding
4. **Stappen om te reproduceren**: Wat je deed voordat de fout optrad
5. **Wat je al hebt geprobeerd**: Oplossingen die je al hebt geprobeerd

**Voorbeeld:**
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

### Communitybronnen

- **GitHub Issues**: [Maak een issue aan](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Word lid van onze community](https://aka.ms/ds4beginners/discord)
- **Discussies**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Q&A Forums](https://docs.microsoft.com/answers/)

### Gerelateerde documentatie

- [INSTALLATION.md](INSTALLATION.md) - Installatie-instructies
- [USAGE.md](USAGE.md) - Hoe het curriculum te gebruiken
- [CONTRIBUTING.md](CONTRIBUTING.md) - Hoe bij te dragen
- [README.md](README.md) - Projectoverzicht

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.