<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:47:08+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "ro"
}
-->
# Ghid de depanare

Acest ghid oferă soluții pentru problemele comune pe care le puteți întâmpina în timp ce lucrați cu curriculumul Data Science for Beginners.

## Cuprins

- [Probleme Python și Jupyter](../..)
- [Probleme cu pachete și dependențe](../..)
- [Probleme cu Jupyter Notebook](../..)
- [Probleme cu aplicația de quiz](../..)
- [Probleme Git și GitHub](../..)
- [Probleme cu documentația Docsify](../..)
- [Probleme cu datele și fișierele](../..)
- [Probleme de performanță](../..)
- [Obținerea ajutorului suplimentar](../..)

## Probleme Python și Jupyter

### Python nu este găsit sau versiunea este greșită

**Problemă:** `python: command not found` sau versiunea Python este greșită

**Soluție:**

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

**Soluție pentru Windows:**
1. Reinstalați Python de pe [python.org](https://www.python.org/)
2. În timpul instalării, bifați "Add Python to PATH"
3. Reporniți terminalul/command prompt-ul

### Probleme de activare a mediului virtual

**Problemă:** Mediul virtual nu se activează

**Soluție:**

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

**Verificați activarea:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Probleme cu kernel-ul Jupyter

**Problemă:** "Kernel not found" sau "Kernel keeps dying"

**Soluție:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Problemă:** Versiunea Python greșită în Jupyter

**Soluție:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Probleme cu pachete și dependențe

### Erori de import

**Problemă:** `ModuleNotFoundError: No module named 'pandas'` (sau alte pachete)

**Soluție:**

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

### Probleme la instalarea cu pip

**Problemă:** `pip install` eșuează cu erori de permisiune

**Soluție:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Problemă:** `pip install` eșuează cu erori de certificat SSL

**Soluție:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Conflicte de versiuni ale pachetelor

**Problemă:** Versiuni incompatibile ale pachetelor

**Soluție:**

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

## Probleme cu Jupyter Notebook

### Jupyter nu pornește

**Problemă:** Comanda `jupyter notebook` nu este găsită

**Soluție:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook-ul nu se încarcă sau nu se salvează

**Problemă:** "Notebook failed to load" sau erori la salvare

**Soluție:**

1. Verificați permisiunile fișierului
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Verificați dacă fișierul este corupt
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Goliți cache-ul Jupyter
```bash
jupyter notebook --clear-cache
```

### Celula nu se execută

**Problemă:** Celula rămâne blocată pe "In [*]" sau durează foarte mult

**Soluție:**

1. **Opriți kernel-ul**: Apăsați butonul "Interrupt" sau tastați `I, I`
2. **Reporniți kernel-ul**: Meniu Kernel → Restart
3. **Verificați buclele infinite** din codul dvs.
4. **Ștergeți output-ul**: Cell → All Output → Clear

### Graficele nu se afișează

**Problemă:** Graficele `matplotlib` nu apar în notebook

**Soluție:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternativă pentru grafice interactive:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Probleme cu aplicația de quiz

### npm install eșuează

**Problemă:** Erori în timpul `npm install`

**Soluție:**

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

### Aplicația de quiz nu pornește

**Problemă:** `npm run serve` eșuează

**Soluție:**

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

### Portul este deja utilizat

**Problemă:** "Port 8080 is already in use"

**Soluție:**

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

### Quiz-ul nu se încarcă sau apare o pagină goală

**Problemă:** Aplicația de quiz se încarcă, dar afișează o pagină goală

**Soluție:**

1. Verificați erorile din consola browserului (F12)
2. Goliți cache-ul și cookie-urile browserului
3. Încercați un alt browser
4. Asigurați-vă că JavaScript este activat
5. Verificați dacă extensiile de blocare a reclamelor interferează

```bash
# Rebuild the app
npm run build
npm run serve
```

## Probleme Git și GitHub

### Git nu este recunoscut

**Problemă:** `git: command not found`

**Soluție:**

**Windows:**
- Instalați Git de pe [git-scm.com](https://git-scm.com/)
- Reporniți terminalul după instalare

**macOS:**

> **Notă:** Dacă nu aveți Homebrew instalat, urmați instrucțiunile de la [https://brew.sh/](https://brew.sh/) pentru a-l instala mai întâi.
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

### Clone eșuează

**Problemă:** `git clone` eșuează cu erori de autentificare

**Soluție:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Permisiune refuzată (publickey)

**Problemă:** Autentificarea cu cheia SSH eșuează

**Soluție:**

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

## Probleme cu documentația Docsify

### Comanda Docsify nu este găsită

**Problemă:** `docsify: command not found`

**Soluție:**

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

### Documentația nu se încarcă

**Problemă:** Docsify servește, dar conținutul nu se încarcă

**Soluție:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Imaginile nu se afișează

**Problemă:** Imaginile afișează pictograma de link rupt

**Soluție:**

1. Verificați dacă căile imaginilor sunt relative
2. Asigurați-vă că fișierele imagine există în depozit
3. Goliți cache-ul browserului
4. Verificați dacă extensiile fișierelor se potrivesc (sensibile la majuscule pe unele sisteme)

## Probleme cu datele și fișierele

### Erori de fișier negăsit

**Problemă:** `FileNotFoundError` la încărcarea datelor

**Soluție:**

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

### Erori la citirea fișierelor CSV

**Problemă:** Erori la citirea fișierelor CSV

**Soluție:**

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

### Erori de memorie cu seturi de date mari

**Problemă:** `MemoryError` la încărcarea fișierelor mari

**Soluție:**

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

## Probleme de performanță

### Performanță lentă a notebook-ului

**Problemă:** Notebook-urile rulează foarte lent

**Soluție:**

1. **Reporniți kernel-ul și ștergeți output-ul**
   - Kernel → Restart & Clear Output

2. **Închideți notebook-urile neutilizate**

3. **Optimizați codul:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Eșantionați seturile de date mari:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Browserul se blochează

**Problemă:** Browserul se blochează sau devine nefuncțional

**Soluție:**

1. Închideți filele neutilizate
2. Goliți cache-ul browserului
3. Creșteți memoria browserului (Chrome: `chrome://settings/system`)
4. Utilizați JupyterLab în loc:
```bash
pip install jupyterlab
jupyter lab
```

## Obținerea ajutorului suplimentar

### Înainte de a cere ajutor

1. Consultați acest ghid de depanare
2. Căutați în [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Revizuiți [INSTALLATION.md](INSTALLATION.md) și [USAGE.md](USAGE.md)
4. Încercați să căutați mesajul de eroare online

### Cum să cereți ajutor

Când creați o problemă sau cereți ajutor, includeți:

1. **Sistem de operare**: Windows, macOS sau Linux (ce distribuție)
2. **Versiunea Python**: Rulați `python --version`
3. **Mesajul de eroare**: Copiați mesajul complet de eroare
4. **Pașii pentru reproducere**: Ce ați făcut înainte de apariția erorii
5. **Ce ați încercat**: Soluțiile pe care le-ați încercat deja

**Exemplu:**
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

### Resurse comunitare

- **GitHub Issues**: [Creați o problemă](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Alăturați-vă comunității noastre](https://aka.ms/ds4beginners/discord)
- **Discuții**: [Discuții pe GitHub](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Forumuri de întrebări și răspunsuri](https://docs.microsoft.com/answers/)

### Documentație asociată

- [INSTALLATION.md](INSTALLATION.md) - Instrucțiuni de configurare
- [USAGE.md](USAGE.md) - Cum să utilizați curriculumul
- [CONTRIBUTING.md](CONTRIBUTING.md) - Cum să contribuiți
- [README.md](README.md) - Prezentare generală a proiectului

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.