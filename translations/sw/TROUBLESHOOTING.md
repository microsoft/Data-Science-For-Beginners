<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:45:04+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "sw"
}
-->
# Mwongozo wa Kutatua Matatizo

Mwongozo huu unatoa suluhisho kwa matatizo ya kawaida unayoweza kukutana nayo unapotumia mtaala wa Data Science for Beginners.

## Jedwali la Maudhui

- [Matatizo ya Python na Jupyter](../..)
- [Matatizo ya Pakiti na Utegemezi](../..)
- [Matatizo ya Jupyter Notebook](../..)
- [Matatizo ya Programu ya Maswali](../..)
- [Matatizo ya Git na GitHub](../..)
- [Matatizo ya Nyaraka za Docsify](../..)
- [Matatizo ya Data na Faili](../..)
- [Matatizo ya Utendaji](../..)
- [Kupata Msaada Zaidi](../..)

## Matatizo ya Python na Jupyter

### Python Haipatikani au Toleo Lisilo Sahihi

**Tatizo:** `python: command not found` au toleo lisilo sahihi la Python

**Suluhisho:**

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

**Suluhisho la Windows:**
1. Sakinisha tena Python kutoka [python.org](https://www.python.org/)
2. Wakati wa usakinishaji, hakikisha umechagua "Add Python to PATH"
3. Anzisha upya terminal/command prompt yako

### Matatizo ya Kuamsha Mazingira ya Virtual

**Tatizo:** Mazingira ya virtual hayataamsha

**Suluhisho:**

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

**Thibitisha uamsho:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Matatizo ya Kernel ya Jupyter

**Tatizo:** "Kernel not found" au "Kernel keeps dying"

**Suluhisho:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Tatizo:** Toleo lisilo sahihi la Python kwenye Jupyter

**Suluhisho:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Matatizo ya Pakiti na Utegemezi

### Makosa ya Uingizaji

**Tatizo:** `ModuleNotFoundError: No module named 'pandas'` (au pakiti nyingine)

**Suluhisho:**

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

### Kushindwa kwa Usakinishaji wa Pip

**Tatizo:** `pip install` inashindwa na makosa ya ruhusa

**Suluhisho:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Tatizo:** `pip install` inashindwa na makosa ya cheti cha SSL

**Suluhisho:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Migongano ya Toleo la Pakiti

**Tatizo:** Matoleo yasiyolingana ya pakiti

**Suluhisho:**

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

## Matatizo ya Jupyter Notebook

### Jupyter Haianzi

**Tatizo:** Amri `jupyter notebook` haipatikani

**Suluhisho:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook Haifunguki au Haisave

**Tatizo:** "Notebook failed to load" au makosa ya kuhifadhi

**Suluhisho:**

1. Angalia ruhusa za faili
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Angalia uharibifu wa faili
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Futa cache ya Jupyter
```bash
jupyter notebook --clear-cache
```

### Seli Haisogei

**Tatizo:** Seli imekwama kwenye "In [*]" au inachukua muda mrefu

**Suluhisho:**

1. **Katiza kernel**: Bonyeza kitufe cha "Interrupt" au bonyeza `I, I`
2. **Anzisha upya kernel**: Menyu ya Kernel → Restart
3. **Angalia loops zisizo na mwisho** kwenye msimbo wako
4. **Futa matokeo**: Cell → All Output → Clear

### Michoro Haionyeshi

**Tatizo:** Michoro ya `matplotlib` haionekani kwenye notebook

**Suluhisho:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Njia mbadala kwa michoro ya maingiliano:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Matatizo ya Programu ya Maswali

### npm install Inashindwa

**Tatizo:** Makosa wakati wa `npm install`

**Suluhisho:**

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

### Programu ya Maswali Haianzi

**Tatizo:** `npm run serve` inashindwa

**Suluhisho:**

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

### Bandari Tayari Inatumika

**Tatizo:** "Port 8080 is already in use"

**Suluhisho:**

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

### Maswali Hayapaki au Ukurasa Mweupe

**Tatizo:** Programu ya maswali inapakia lakini inaonyesha ukurasa mweupe

**Suluhisho:**

1. Angalia makosa kwenye console ya kivinjari (F12)
2. Futa cache na cookies za kivinjari
3. Jaribu kivinjari tofauti
4. Hakikisha JavaScript imewezeshwa
5. Angalia kama vizuizi vya matangazo vinazuia

```bash
# Rebuild the app
npm run build
npm run serve
```

## Matatizo ya Git na GitHub

### Git Haijatambulika

**Tatizo:** `git: command not found`

**Suluhisho:**

**Windows:**
- Sakinisha Git kutoka [git-scm.com](https://git-scm.com/)
- Anzisha upya terminal baada ya usakinishaji

**macOS:**

> **Kumbuka:** Ikiwa huna Homebrew iliyosakinishwa, fuata maelekezo kwenye [https://brew.sh/](https://brew.sh/) ili kuisakinisha kwanza.
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

### Clone Inashindwa

**Tatizo:** `git clone` inashindwa na makosa ya uthibitisho

**Suluhisho:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Ruhusa Imekataliwa (publickey)

**Tatizo:** Uthibitisho wa SSH key unashindwa

**Suluhisho:**

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

## Matatizo ya Nyaraka za Docsify

### Amri ya Docsify Haipatikani

**Tatizo:** `docsify: command not found`

**Suluhisho:**

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

### Nyaraka Hazipaki

**Tatizo:** Docsify inahudumu lakini maudhui hayapaki

**Suluhisho:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Picha Hazionekani

**Tatizo:** Picha zinaonyesha ikoni ya kiungo kilichovunjika

**Suluhisho:**

1. Hakikisha njia za picha ni za jamaa
2. Hakikisha faili za picha zipo kwenye hifadhi
3. Futa cache ya kivinjari
4. Thibitisha viendelezi vya faili vinavyolingana (case-sensitive kwenye mifumo mingine)

## Matatizo ya Data na Faili

### Makosa ya Faili Haipatikani

**Tatizo:** `FileNotFoundError` wakati wa kupakia data

**Suluhisho:**

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

### Makosa ya Kusoma CSV

**Tatizo:** Makosa ya kusoma faili za CSV

**Suluhisho:**

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

### Makosa ya Kumbukumbu na Dataset Kubwa

**Tatizo:** `MemoryError` wakati wa kupakia faili kubwa

**Suluhisho:**

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

## Matatizo ya Utendaji

### Utendaji wa Notebook Polepole

**Tatizo:** Notebook zinafanya kazi polepole sana

**Suluhisho:**

1. **Anzisha upya kernel na futa matokeo**
   - Kernel → Restart & Clear Output

2. **Funga notebook zisizotumika**

3. **Boresha msimbo:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Sampuli dataset kubwa:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Kivinjari Kinakwama

**Tatizo:** Kivinjari kinakwama au hakijibu

**Suluhisho:**

1. Funga tabo zisizotumika
2. Futa cache ya kivinjari
3. Ongeza kumbukumbu ya kivinjari (Chrome: `chrome://settings/system`)
4. Tumia JupyterLab badala yake:
```bash
pip install jupyterlab
jupyter lab
```

## Kupata Msaada Zaidi

### Kabla ya Kuomba Msaada

1. Angalia mwongozo huu wa kutatua matatizo
2. Tafuta [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Soma [INSTALLATION.md](INSTALLATION.md) na [USAGE.md](USAGE.md)
4. Jaribu kutafuta ujumbe wa kosa mtandaoni

### Jinsi ya Kuomba Msaada

Unapounda suala au kuomba msaada, jumuisha:

1. **Mfumo wa Uendeshaji**: Windows, macOS, au Linux (usambazaji gani)
2. **Toleo la Python**: Endesha `python --version`
3. **Ujumbe wa Kosa**: Nakili ujumbe kamili wa kosa
4. **Hatua za Kuzalisha Tatizo**: Ulichofanya kabla ya kosa kutokea
5. **Ulichojaribu**: Suluhisho ulizojaribu tayari

**Mfano:**
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

### Rasilimali za Jamii

- **GitHub Issues**: [Unda suala](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Jiunge na jamii yetu](https://aka.ms/ds4beginners/discord)
- **Majadiliano**: [Majadiliano ya GitHub](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Mabaraza ya Maswali na Majibu](https://docs.microsoft.com/answers/)

### Nyaraka Zinazohusiana

- [INSTALLATION.md](INSTALLATION.md) - Maelekezo ya usakinishaji
- [USAGE.md](USAGE.md) - Jinsi ya kutumia mtaala
- [CONTRIBUTING.md](CONTRIBUTING.md) - Jinsi ya kuchangia
- [README.md](README.md) - Muhtasari wa mradi

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.