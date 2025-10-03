<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:50:28+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "lt"
}
-->
# Trikčių šalinimo vadovas

Šis vadovas pateikia sprendimus dažniausiai pasitaikančioms problemoms, su kuriomis galite susidurti dirbdami su „Data Science for Beginners“ mokymo programa.

## Turinys

- [Python ir Jupyter problemos](../..)
- [Paketų ir priklausomybių problemos](../..)
- [Jupyter Notebook problemos](../..)
- [Klausimynų programos problemos](../..)
- [Git ir GitHub problemos](../..)
- [Docsify dokumentacijos problemos](../..)
- [Duomenų ir failų problemos](../..)
- [Našumo problemos](../..)
- [Papildomos pagalbos gavimas](../..)

## Python ir Jupyter problemos

### Python nerastas arba neteisinga versija

**Problema:** `python: command not found` arba neteisinga Python versija

**Sprendimas:**

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

**Sprendimas Windows:**
1. Iš naujo įdiekite Python iš [python.org](https://www.python.org/)
2. Diegimo metu pažymėkite „Add Python to PATH“
3. Perkraukite terminalą/komandinę eilutę

### Virtualios aplinkos aktyvavimo problemos

**Problema:** Virtuali aplinka neaktyvuojama

**Sprendimas:**

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

**Patikrinkite aktyvavimą:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter branduolio problemos

**Problema:** „Kernel not found“ arba „Kernel keeps dying“

**Sprendimas:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Problema:** Netinkama Python versija Jupyter

**Sprendimas:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Paketų ir priklausomybių problemos

### Importavimo klaidos

**Problema:** `ModuleNotFoundError: No module named 'pandas'` (arba kiti paketai)

**Sprendimas:**

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

### Pip diegimo klaidos

**Problema:** `pip install` nepavyksta dėl leidimų klaidų

**Sprendimas:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Problema:** `pip install` nepavyksta dėl SSL sertifikato klaidų

**Sprendimas:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Paketų versijų konfliktai

**Problema:** Nesuderinamos paketų versijos

**Sprendimas:**

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

## Jupyter Notebook problemos

### Jupyter neįsijungia

**Problema:** `jupyter notebook` komanda nerasta

**Sprendimas:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Užrašų knygelė neįkeliama arba neišsaugoma

**Problema:** „Notebook failed to load“ arba išsaugojimo klaidos

**Sprendimas:**

1. Patikrinkite failų leidimus
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Patikrinkite, ar failas nėra sugadintas
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Išvalykite Jupyter talpyklą
```bash
jupyter notebook --clear-cache
```

### Ląstelė neįvykdoma

**Problema:** Ląstelė užstringa „In [*]“ arba vykdymas trunka labai ilgai

**Sprendimas:**

1. **Nutraukite branduolį**: Spustelėkite „Interrupt“ mygtuką arba paspauskite `I, I`
2. **Perkraukite branduolį**: Kernel meniu → Restart
3. **Patikrinkite, ar nėra begalinių ciklų** jūsų kode
4. **Išvalykite išvestį**: Cell → All Output → Clear

### Grafikai nerodomi

**Problema:** `matplotlib` grafikai nerodomi užrašų knygelėje

**Sprendimas:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternatyva interaktyviems grafikams:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Klausimynų programos problemos

### npm install nepavyksta

**Problema:** Klaidos vykdant `npm install`

**Sprendimas:**

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

### Klausimynų programa neįsijungia

**Problema:** `npm run serve` nepavyksta

**Sprendimas:**

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

### Uostas jau naudojamas

**Problema:** „Port 8080 is already in use“

**Sprendimas:**

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

### Klausimynas neįkeliamas arba tuščias puslapis

**Problema:** Klausimynų programa įsijungia, bet rodo tuščią puslapį

**Sprendimas:**

1. Patikrinkite naršyklės konsolę dėl klaidų (F12)
2. Išvalykite naršyklės talpyklą ir slapukus
3. Išbandykite kitą naršyklę
4. Įsitikinkite, kad JavaScript įjungtas
5. Patikrinkite, ar reklamos blokatoriai netrukdo

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git ir GitHub problemos

### Git nerastas

**Problema:** `git: command not found`

**Sprendimas:**

**Windows:**
- Įdiekite Git iš [git-scm.com](https://git-scm.com/)
- Po diegimo perkraukite terminalą

**macOS:**

> **Pastaba:** Jei neturite Homebrew, sekite instrukcijas [https://brew.sh/](https://brew.sh/) norėdami jį įdiegti.
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

### Klonavimas nepavyksta

**Problema:** `git clone` nepavyksta dėl autentifikacijos klaidų

**Sprendimas:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Leidimas atmestas (publickey)

**Problema:** SSH raktų autentifikacija nepavyksta

**Sprendimas:**

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

## Docsify dokumentacijos problemos

### Docsify komanda nerasta

**Problema:** `docsify: command not found`

**Sprendimas:**

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

### Dokumentacija neįkeliama

**Problema:** Docsify veikia, bet turinys neįkeliamas

**Sprendimas:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Vaizdai nerodomi

**Problema:** Vaizdai rodo sugadinto nuorodos ikoną

**Sprendimas:**

1. Patikrinkite, ar vaizdų keliai yra santykiniai
2. Įsitikinkite, kad vaizdų failai egzistuoja saugykloje
3. Išvalykite naršyklės talpyklą
4. Patikrinkite, ar failų plėtiniai atitinka (kai kuriose sistemose skiriama didžiosios ir mažosios raidės)

## Duomenų ir failų problemos

### Failas nerastas

**Problema:** `FileNotFoundError` kraunant duomenis

**Sprendimas:**

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

### CSV skaitymo klaidos

**Problema:** Klaidos skaitant CSV failus

**Sprendimas:**

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

### Atminties klaidos su dideliais duomenų rinkiniais

**Problema:** `MemoryError` kraunant didelius failus

**Sprendimas:**

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

## Našumo problemos

### Lėtas užrašų knygelės veikimas

**Problema:** Užrašų knygelės veikia labai lėtai

**Sprendimas:**

1. **Perkraukite branduolį ir išvalykite išvestį**
   - Kernel → Restart & Clear Output

2. **Uždarykite nenaudojamas užrašų knygeles**

3. **Optimizuokite kodą:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Pavyzdys su dideliais duomenų rinkiniais:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Naršyklė užstringa

**Problema:** Naršyklė užstringa arba tampa neatsakinga

**Sprendimas:**

1. Uždarykite nenaudojamus skirtukus
2. Išvalykite naršyklės talpyklą
3. Padidinkite naršyklės atmintį (Chrome: `chrome://settings/system`)
4. Naudokite JupyterLab vietoje:
```bash
pip install jupyterlab
jupyter lab
```

## Papildomos pagalbos gavimas

### Prieš prašant pagalbos

1. Peržiūrėkite šį trikčių šalinimo vadovą
2. Ieškokite [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Peržiūrėkite [INSTALLATION.md](INSTALLATION.md) ir [USAGE.md](USAGE.md)
4. Pabandykite ieškoti klaidos pranešimo internete

### Kaip prašyti pagalbos

Kuriant problemą arba prašant pagalbos, įtraukite:

1. **Operacinė sistema**: Windows, macOS arba Linux (kuri distribucija)
2. **Python versija**: Vykdykite `python --version`
3. **Klaidos pranešimas**: Nukopijuokite visą klaidos pranešimą
4. **Veiksmai, kurie sukėlė klaidą**: Ką darėte prieš atsirandant klaidai
5. **Ką jau bandėte**: Sprendimus, kuriuos jau išbandėte

**Pavyzdys:**
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

### Bendruomenės ištekliai

- **GitHub Issues**: [Sukurti problemą](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Prisijunkite prie mūsų bendruomenės](https://aka.ms/ds4beginners/discord)
- **Diskusijos**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Q&A forumai](https://docs.microsoft.com/answers/)

### Susijusi dokumentacija

- [INSTALLATION.md](INSTALLATION.md) - Diegimo instrukcijos
- [USAGE.md](USAGE.md) - Kaip naudoti mokymo programą
- [CONTRIBUTING.md](CONTRIBUTING.md) - Kaip prisidėti
- [README.md](README.md) - Projekto apžvalga

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.