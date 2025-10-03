<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:45:32+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "hu"
}
-->
# Hibakeresési útmutató

Ez az útmutató megoldásokat kínál a Data Science for Beginners tananyag használata során felmerülő gyakori problémákra.

## Tartalomjegyzék

- [Python és Jupyter problémák](../..)
- [Csomag- és függőségi problémák](../..)
- [Jupyter Notebook problémák](../..)
- [Kvíz alkalmazás problémák](../..)
- [Git és GitHub problémák](../..)
- [Docsify dokumentáció problémák](../..)
- [Adat- és fájlproblémák](../..)
- [Teljesítményproblémák](../..)
- [További segítség kérése](../..)

## Python és Jupyter problémák

### Python nem található vagy rossz verzió

**Probléma:** `python: command not found` vagy rossz Python verzió

**Megoldás:**

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

**Windows megoldás:**
1. Telepítse újra a Pythont a [python.org](https://www.python.org/) weboldalról
2. A telepítés során jelölje be az "Add Python to PATH" opciót
3. Indítsa újra a terminált/parancssort

### Virtuális környezet aktiválási problémák

**Probléma:** A virtuális környezet nem aktiválódik

**Megoldás:**

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

**Aktiválás ellenőrzése:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter kernel problémák

**Probléma:** "Kernel nem található" vagy "Kernel folyamatosan leáll"

**Megoldás:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Probléma:** Rossz Python verzió a Jupyterben

**Megoldás:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Csomag- és függőségi problémák

### Importálási hibák

**Probléma:** `ModuleNotFoundError: No module named 'pandas'` (vagy más csomagok)

**Megoldás:**

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

### Pip telepítési hibák

**Probléma:** `pip install` engedélyezési hibákkal leáll

**Megoldás:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Probléma:** `pip install` SSL tanúsítvány hibákkal leáll

**Megoldás:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Csomag verzióütközések

**Probléma:** Összeférhetetlen csomagverziók

**Megoldás:**

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

## Jupyter Notebook problémák

### Jupyter nem indul

**Probléma:** `jupyter notebook` parancs nem található

**Megoldás:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook nem töltődik be vagy nem menthető

**Probléma:** "Notebook nem sikerült betölteni" vagy mentési hibák

**Megoldás:**

1. Ellenőrizze a fájlengedélyeket
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Ellenőrizze a fájl sérülését
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Törölje a Jupyter gyorsítótárát
```bash
jupyter notebook --clear-cache
```

### Cellák nem futnak

**Probléma:** Cellák "In [*]" állapotban ragadnak vagy túl sokáig tartanak

**Megoldás:**

1. **Megszakítsa a kernelt**: Kattintson az "Interrupt" gombra vagy nyomja meg `I, I`
2. **Indítsa újra a kernelt**: Kernel menü → Restart
3. **Ellenőrizze a végtelen ciklusokat** a kódjában
4. **Törölje a kimenetet**: Cell → All Output → Clear

### Diagramok nem jelennek meg

**Probléma:** `matplotlib` diagramok nem jelennek meg a notebookban

**Megoldás:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternatíva interaktív diagramokhoz:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Kvíz alkalmazás problémák

### npm install hibák

**Probléma:** Hibák az `npm install` során

**Megoldás:**

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

### Kvíz alkalmazás nem indul

**Probléma:** `npm run serve` leáll

**Megoldás:**

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

### Port már használatban

**Probléma:** "Port 8080 már használatban van"

**Megoldás:**

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

### Kvíz nem töltődik be vagy üres oldal

**Probléma:** A kvíz alkalmazás betöltődik, de üres oldalt mutat

**Megoldás:**

1. Ellenőrizze a böngésző konzolt hibákért (F12)
2. Törölje a böngésző gyorsítótárát és sütiket
3. Próbáljon ki egy másik böngészőt
4. Győződjön meg róla, hogy a JavaScript engedélyezve van
5. Ellenőrizze, hogy az adblockerek nem zavarják-e

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git és GitHub problémák

### Git nem ismerhető fel

**Probléma:** `git: command not found`

**Megoldás:**

**Windows:**
- Telepítse a Gitet a [git-scm.com](https://git-scm.com/) weboldalról
- Indítsa újra a terminált a telepítés után

**macOS:**

> **Megjegyzés:** Ha nincs telepítve a Homebrew, kövesse az utasításokat a [https://brew.sh/](https://brew.sh/) oldalon a telepítéshez.
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

### Klónozás sikertelen

**Probléma:** `git clone` hitelesítési hibákkal leáll

**Megoldás:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Hozzáférés megtagadva (publickey)

**Probléma:** SSH kulcs hitelesítés sikertelen

**Megoldás:**

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

## Docsify dokumentáció problémák

### Docsify parancs nem található

**Probléma:** `docsify: command not found`

**Megoldás:**

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

### Dokumentáció nem töltődik be

**Probléma:** Docsify elindul, de a tartalom nem töltődik be

**Megoldás:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Képek nem jelennek meg

**Probléma:** Képek törött link ikont mutatnak

**Megoldás:**

1. Ellenőrizze, hogy a képek elérési útjai relatívak-e
2. Győződjön meg róla, hogy a képfájlok léteznek a repóban
3. Törölje a böngésző gyorsítótárát
4. Ellenőrizze, hogy a fájlkiterjesztések egyeznek-e (érzékeny lehet a kis- és nagybetűkre bizonyos rendszereken)

## Adat- és fájlproblémák

### Fájl nem található hibák

**Probléma:** `FileNotFoundError` adat betöltésekor

**Megoldás:**

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

### CSV olvasási hibák

**Probléma:** Hibák CSV fájlok olvasásakor

**Megoldás:**

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

### Memóriahibák nagy adathalmazokkal

**Probléma:** `MemoryError` nagy fájlok betöltésekor

**Megoldás:**

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

## Teljesítményproblémák

### Lassú notebook teljesítmény

**Probléma:** Notebookok nagyon lassan futnak

**Megoldás:**

1. **Indítsa újra a kernelt és törölje a kimenetet**
   - Kernel → Restart & Clear Output

2. **Zárja be a nem használt notebookokat**

3. **Optimalizálja a kódot:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Mintavételezzen nagy adathalmazokat:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Böngésző összeomlik

**Probléma:** Böngésző összeomlik vagy nem válaszol

**Megoldás:**

1. Zárja be a nem használt lapokat
2. Törölje a böngésző gyorsítótárát
3. Növelje a böngésző memóriáját (Chrome: `chrome://settings/system`)
4. Használja a JupyterLabot helyette:
```bash
pip install jupyterlab
jupyter lab
```

## További segítség kérése

### Mielőtt segítséget kérne

1. Ellenőrizze ezt a hibakeresési útmutatót
2. Keressen a [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) között
3. Nézze át az [INSTALLATION.md](INSTALLATION.md) és [USAGE.md](USAGE.md) fájlokat
4. Próbálja meg online keresni a hibaüzenetet

### Hogyan kérjen segítséget

Amikor hibát jelent vagy segítséget kér, adja meg:

1. **Operációs rendszer**: Windows, macOS vagy Linux (melyik disztribúció)
2. **Python verzió**: Futtassa a `python --version` parancsot
3. **Hibaüzenet**: Másolja be a teljes hibaüzenetet
4. **Reprodukálási lépések**: Mit tett a hiba előtt
5. **Mit próbált már**: Az eddig kipróbált megoldások

**Példa:**
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

### Közösségi források

- **GitHub Issues**: [Hozzon létre egy hibajelentést](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Csatlakozzon a közösségünkhöz](https://aka.ms/ds4beginners/discord)
- **Discussions**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Q&A Fórumok](https://docs.microsoft.com/answers/)

### Kapcsolódó dokumentáció

- [INSTALLATION.md](INSTALLATION.md) - Telepítési útmutató
- [USAGE.md](USAGE.md) - A tananyag használata
- [CONTRIBUTING.md](CONTRIBUTING.md) - Hogyan járulhat hozzá
- [README.md](README.md) - Projekt áttekintése

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.