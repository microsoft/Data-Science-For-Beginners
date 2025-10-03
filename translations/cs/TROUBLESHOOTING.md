<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:46:04+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "cs"
}
-->
# Průvodce řešením problémů

Tento průvodce poskytuje řešení běžných problémů, na které můžete narazit při práci s kurikulem Data Science for Beginners.

## Obsah

- [Problémy s Pythonem a Jupyterem](../..)
- [Problémy s balíčky a závislostmi](../..)
- [Problémy s Jupyter Notebookem](../..)
- [Problémy s aplikací kvízu](../..)
- [Problémy s Gitem a GitHubem](../..)
- [Problémy s dokumentací Docsify](../..)
- [Problémy s daty a soubory](../..)
- [Problémy s výkonem](../..)
- [Získání další pomoci](../..)

## Problémy s Pythonem a Jupyterem

### Python nenalezen nebo špatná verze

**Problém:** `python: command not found` nebo špatná verze Pythonu

**Řešení:**

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

**Řešení pro Windows:**
1. Znovu nainstalujte Python z [python.org](https://www.python.org/)
2. Během instalace zaškrtněte "Add Python to PATH"
3. Restartujte terminál/příkazový řádek

### Problémy s aktivací virtuálního prostředí

**Problém:** Virtuální prostředí se nedaří aktivovat

**Řešení:**

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

**Ověření aktivace:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Problémy s Jupyter kernelem

**Problém:** "Kernel nenalezen" nebo "Kernel stále selhává"

**Řešení:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Problém:** Špatná verze Pythonu v Jupyteru

**Řešení:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Problémy s balíčky a závislostmi

### Chyby při importu

**Problém:** `ModuleNotFoundError: No module named 'pandas'` (nebo jiné balíčky)

**Řešení:**

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

### Selhání instalace pomocí pip

**Problém:** `pip install` selhává s chybami oprávnění

**Řešení:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Problém:** `pip install` selhává s chybami SSL certifikátu

**Řešení:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Konflikty verzí balíčků

**Problém:** Nekompatibilní verze balíčků

**Řešení:**

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

## Problémy s Jupyter Notebookem

### Jupyter se nespustí

**Problém:** Příkaz `jupyter notebook` nenalezen

**Řešení:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook se nenačítá nebo neukládá

**Problém:** "Notebook se nepodařilo načíst" nebo chyby při ukládání

**Řešení:**

1. Zkontrolujte oprávnění k souborům
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Zkontrolujte, zda není soubor poškozen
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Vymažte cache Jupyteru
```bash
jupyter notebook --clear-cache
```

### Buňka se nespustí

**Problém:** Buňka zůstává na "In [*]" nebo trvá příliš dlouho

**Řešení:**

1. **Přerušení kernelu**: Klikněte na tlačítko "Interrupt" nebo stiskněte `I, I`
2. **Restart kernelu**: Menu Kernel → Restart
3. **Zkontrolujte nekonečné smyčky** ve vašem kódu
4. **Vymažte výstup**: Cell → All Output → Clear

### Grafy se nezobrazují

**Problém:** Grafy z `matplotlib` se nezobrazují v notebooku

**Řešení:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternativa pro interaktivní grafy:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Problémy s aplikací kvízu

### Selhání npm install

**Problém:** Chyby během `npm install`

**Řešení:**

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

### Aplikace kvízu se nespustí

**Problém:** `npm run serve` selhává

**Řešení:**

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

### Port již používán

**Problém:** "Port 8080 je již používán"

**Řešení:**

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

### Kvíz se nenačítá nebo prázdná stránka

**Problém:** Aplikace kvízu se načte, ale zobrazí prázdnou stránku

**Řešení:**

1. Zkontrolujte chyby v konzoli prohlížeče (F12)
2. Vymažte cache a cookies prohlížeče
3. Vyzkoušejte jiný prohlížeč
4. Ujistěte se, že je povolen JavaScript
5. Zkontrolujte, zda neblokují reklamy

```bash
# Rebuild the app
npm run build
npm run serve
```

## Problémy s Gitem a GitHubem

### Git není rozpoznán

**Problém:** `git: command not found`

**Řešení:**

**Windows:**
- Nainstalujte Git z [git-scm.com](https://git-scm.com/)
- Po instalaci restartujte terminál

**macOS:**

> **Poznámka:** Pokud nemáte nainstalovaný Homebrew, postupujte podle pokynů na [https://brew.sh/](https://brew.sh/) pro jeho instalaci.
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

### Selhání klonování

**Problém:** `git clone` selhává s chybami autentizace

**Řešení:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Permission Denied (publickey)

**Problém:** Selhání autentizace pomocí SSH klíče

**Řešení:**

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

## Problémy s dokumentací Docsify

### Příkaz Docsify nenalezen

**Problém:** `docsify: command not found`

**Řešení:**

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

### Dokumentace se nenačítá

**Problém:** Docsify běží, ale obsah se nenačítá

**Řešení:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Obrázky se nezobrazují

**Problém:** Obrázky zobrazují ikonu rozbitého odkazu

**Řešení:**

1. Zkontrolujte, zda jsou cesty k obrázkům relativní
2. Ujistěte se, že soubory obrázků existují v repozitáři
3. Vymažte cache prohlížeče
4. Ověřte, zda přípony souborů odpovídají (na některých systémech záleží na velikosti písmen)

## Problémy s daty a soubory

### Chyby nenalezeného souboru

**Problém:** `FileNotFoundError` při načítání dat

**Řešení:**

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

### Chyby při čtení CSV

**Problém:** Chyby při čtení CSV souborů

**Řešení:**

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

### Chyby paměti u velkých datových sad

**Problém:** `MemoryError` při načítání velkých souborů

**Řešení:**

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

## Problémy s výkonem

### Pomalejší výkon notebooku

**Problém:** Notebooky běží velmi pomalu

**Řešení:**

1. **Restartujte kernel a vymažte výstup**
   - Kernel → Restart & Clear Output

2. **Zavřete nepoužívané notebooky**

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

4. **Pracujte s výběrem z velkých datových sad:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Pád prohlížeče

**Problém:** Prohlížeč padá nebo se stává nereagujícím

**Řešení:**

1. Zavřete nepoužívané záložky
2. Vymažte cache prohlížeče
3. Zvyšte paměť prohlížeče (Chrome: `chrome://settings/system`)
4. Použijte JupyterLab místo:
```bash
pip install jupyterlab
jupyter lab
```

## Získání další pomoci

### Před žádostí o pomoc

1. Zkontrolujte tento průvodce řešením problémů
2. Vyhledejte [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Projděte si [INSTALLATION.md](INSTALLATION.md) a [USAGE.md](USAGE.md)
4. Zkuste vyhledat chybovou zprávu online

### Jak požádat o pomoc

Při vytváření issue nebo žádosti o pomoc uveďte:

1. **Operační systém**: Windows, macOS nebo Linux (která distribuce)
2. **Verze Pythonu**: Spusťte `python --version`
3. **Chybová zpráva**: Zkopírujte kompletní chybovou zprávu
4. **Kroky k reprodukci**: Co jste udělali před výskytem chyby
5. **Co jste již zkusili**: Řešení, která jste již vyzkoušeli

**Příklad:**
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

### Komunitní zdroje

- **GitHub Issues**: [Vytvořit issue](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Připojte se ke komunitě](https://aka.ms/ds4beginners/discord)
- **Diskuze**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Fóra Q&A](https://docs.microsoft.com/answers/)

### Související dokumentace

- [INSTALLATION.md](INSTALLATION.md) - Pokyny k nastavení
- [USAGE.md](USAGE.md) - Jak používat kurikulum
- [CONTRIBUTING.md](CONTRIBUTING.md) - Jak přispívat
- [README.md](README.md) - Přehled projektu

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.