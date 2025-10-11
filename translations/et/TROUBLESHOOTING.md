<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-11T15:15:34+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "et"
}
-->
# Tõrkeotsingu juhend

See juhend pakub lahendusi levinud probleemidele, millega võite kokku puutuda Data Science for Beginners õppekava kasutamisel.

## Sisukord

- [Python ja Jupyter probleemid](../..)
- [Pakettide ja sõltuvuste probleemid](../..)
- [Jupyter Notebooki probleemid](../..)
- [Viktoriinirakenduse probleemid](../..)
- [Git ja GitHubi probleemid](../..)
- [Docsify dokumentatsiooni probleemid](../..)
- [Andmete ja failide probleemid](../..)
- [Jõudlusprobleemid](../..)
- [Lisaküsimuste korral abi saamine](../..)

## Python ja Jupyter probleemid

### Python puudub või vale versioon

**Probleem:** `python: command not found` või vale Python versioon

**Lahendus:**

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

**Windowsi lahendus:**
1. Installige Python uuesti [python.org](https://www.python.org/) lehelt
2. Installimise ajal märkige "Add Python to PATH"
3. Taaskäivitage terminal/käsurida

### Virtuaalse keskkonna aktiveerimise probleemid

**Probleem:** Virtuaalset keskkonda ei saa aktiveerida

**Lahendus:**

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

**Aktiveerimise kontroll:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter kerneli probleemid

**Probleem:** "Kernel not found" või "Kernel keeps dying"

**Lahendus:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Probleem:** Vale Python versioon Jupyteri keskkonnas

**Lahendus:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Pakettide ja sõltuvuste probleemid

### Importimisvead

**Probleem:** `ModuleNotFoundError: No module named 'pandas'` (või muud paketid)

**Lahendus:**

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

### Pip installimise vead

**Probleem:** `pip install` ebaõnnestub õiguste probleemide tõttu

**Lahendus:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Probleem:** `pip install` ebaõnnestub SSL sertifikaadi vigade tõttu

**Lahendus:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Pakettide versioonide konfliktid

**Probleem:** Ühildumatud pakettide versioonid

**Lahendus:**

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

## Jupyter Notebooki probleemid

### Jupyter ei käivitu

**Probleem:** `jupyter notebook` käsk ei tööta

**Lahendus:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook ei lae ega salvesta

**Probleem:** "Notebook failed to load" või salvestamise vead

**Lahendus:**

1. Kontrollige failide õigusi
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Kontrollige failide rikutust
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Tühjendage Jupyteri vahemälu
```bash
jupyter notebook --clear-cache
```

### Lahter ei täitu

**Probleem:** Lahter jääb "In [*]" olekusse või täitmine võtab kaua aega

**Lahendus:**

1. **Katkestage kernel**: Klõpsake "Interrupt" nuppu või vajutage `I, I`
2. **Taaskäivitage kernel**: Kernel menüü → Restart
3. **Kontrollige koodis lõputuid tsükleid**
4. **Tühjendage väljund**: Cell → All Output → Clear

### Graafikud ei kuvata

**Probleem:** `matplotlib` graafikud ei ilmu notebookis

**Lahendus:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternatiiv interaktiivsete graafikute jaoks:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Viktoriinirakenduse probleemid

### npm install ebaõnnestub

**Probleem:** Veateated `npm install` käivitamisel

**Lahendus:**

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

### Viktoriinirakendus ei käivitu

**Probleem:** `npm run serve` ebaõnnestub

**Lahendus:**

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

### Port on juba kasutusel

**Probleem:** "Port 8080 is already in use"

**Lahendus:**

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

### Viktoriin ei lae või näitab tühja lehte

**Probleem:** Viktoriinirakendus laeb, kuid kuvab tühja lehe

**Lahendus:**

1. Kontrollige brauseri konsooli vigade osas (F12)
2. Tühjendage brauseri vahemälu ja küpsised
3. Proovige teist brauserit
4. Veenduge, et JavaScript on lubatud
5. Kontrollige, kas reklaamiblokeerijad segavad

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git ja GitHubi probleemid

### Git ei ole tuvastatud

**Probleem:** `git: command not found`

**Lahendus:**

**Windows:**
- Installige Git [git-scm.com](https://git-scm.com/) lehelt
- Taaskäivitage terminal pärast installimist

**macOS:**

> **Märkus:** Kui Homebrew pole installitud, järgige juhiseid [https://brew.sh/](https://brew.sh/) lehel, et see esmalt paigaldada.
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

### Kloonimine ebaõnnestub

**Probleem:** `git clone` ebaõnnestub autentimisvigade tõttu

**Lahendus:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Luba keelatud (publickey)

**Probleem:** SSH võtme autentimine ebaõnnestub

**Lahendus:**

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

## Docsify dokumentatsiooni probleemid

### Docsify käsk ei tööta

**Probleem:** `docsify: command not found`

**Lahendus:**

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

### Dokumentatsioon ei lae

**Probleem:** Docsify server töötab, kuid sisu ei lae

**Lahendus:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Pildid ei kuvata

**Probleem:** Pildid näitavad katkise lingi ikooni

**Lahendus:**

1. Kontrollige, et pilditeed oleksid suhtelised
2. Veenduge, et pildifailid eksisteerivad repositooriumis
3. Tühjendage brauseri vahemälu
4. Kontrollige, et faililaiendid vastavad (mõnel süsteemil tõstutundlik)

## Andmete ja failide probleemid

### Faili ei leitud vead

**Probleem:** `FileNotFoundError` andmete laadimisel

**Lahendus:**

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

### CSV lugemise vead

**Probleem:** Veateated CSV failide lugemisel

**Lahendus:**

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

### Mäluvead suurte andmekogumitega

**Probleem:** `MemoryError` suurte failide laadimisel

**Lahendus:**

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

## Jõudlusprobleemid

### Notebooki aeglane jõudlus

**Probleem:** Notebookid töötavad väga aeglaselt

**Lahendus:**

1. **Taaskäivitage kernel ja tühjendage väljund**
   - Kernel → Restart & Clear Output

2. **Sulgege kasutamata notebookid**

3. **Optimeerige koodi:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Proovige suuri andmekogumeid osaliselt:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Brauseri kokkujooksmine

**Probleem:** Brauser jookseb kokku või muutub reageerimatuks

**Lahendus:**

1. Sulgege kasutamata vahelehed
2. Tühjendage brauseri vahemälu
3. Suurendage brauseri mälu (Chrome: `chrome://settings/system`)
4. Kasutage JupyterLabi:
```bash
pip install jupyterlab
jupyter lab
```

## Lisaküsimuste korral abi saamine

### Enne abi küsimist

1. Kontrollige seda tõrkeotsingu juhendit
2. Otsige [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) lehelt
3. Vaadake üle [INSTALLATION.md](INSTALLATION.md) ja [USAGE.md](USAGE.md)
4. Proovige otsida veateadet internetist

### Kuidas abi küsida

Kui loote probleemi või palute abi, lisage:

1. **Operatsioonisüsteem**: Windows, macOS või Linux (milline distributsioon)
2. **Python versioon**: Käivitage `python --version`
3. **Veateade**: Kopeerige täielik veateade
4. **Sammud vea kordamiseks**: Mida tegite enne vea ilmnemist
5. **Mida olete proovinud**: Lahendused, mida olete juba katsetanud

**Näide:**
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

### Kogukonna ressursid

- **GitHub Issues**: [Loo probleem](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Liitu meie kogukonnaga](https://aka.ms/ds4beginners/discord)
- **Arutelud**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Küsimuste ja vastuste foorumid](https://docs.microsoft.com/answers/)

### Seotud dokumentatsioon

- [INSTALLATION.md](INSTALLATION.md) - Paigaldusjuhised
- [USAGE.md](USAGE.md) - Kuidas õppekava kasutada
- [CONTRIBUTING.md](CONTRIBUTING.md) - Kuidas panustada
- [README.md](README.md) - Projekti ülevaade

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.