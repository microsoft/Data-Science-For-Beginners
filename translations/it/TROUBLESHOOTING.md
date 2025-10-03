<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:38:14+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "it"
}
-->
# Guida alla Risoluzione dei Problemi

Questa guida fornisce soluzioni ai problemi comuni che potresti incontrare mentre lavori con il curriculum "Data Science for Beginners".

## Indice

- [Problemi con Python e Jupyter](../..)
- [Problemi con Pacchetti e Dipendenze](../..)
- [Problemi con Jupyter Notebook](../..)
- [Problemi con l'Applicazione Quiz](../..)
- [Problemi con Git e GitHub](../..)
- [Problemi con la Documentazione Docsify](../..)
- [Problemi con Dati e File](../..)
- [Problemi di Prestazioni](../..)
- [Ottenere Ulteriore Aiuto](../..)

## Problemi con Python e Jupyter

### Python Non Trovato o Versione Errata

**Problema:** `python: command not found` o versione errata di Python

**Soluzione:**

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

**Soluzione per Windows:**
1. Reinstalla Python da [python.org](https://www.python.org/)
2. Durante l'installazione, seleziona "Add Python to PATH"
3. Riavvia il terminale/prompt dei comandi

### Problemi di Attivazione dell'Ambiente Virtuale

**Problema:** L'ambiente virtuale non si attiva

**Soluzione:**

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

**Verifica dell'attivazione:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Problemi con il Kernel di Jupyter

**Problema:** "Kernel non trovato" o "Kernel continua a morire"

**Soluzione:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Problema:** Versione errata di Python in Jupyter

**Soluzione:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Problemi con Pacchetti e Dipendenze

### Errori di Importazione

**Problema:** `ModuleNotFoundError: No module named 'pandas'` (o altri pacchetti)

**Soluzione:**

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

### Fallimenti nell'Installazione con Pip

**Problema:** `pip install` fallisce con errori di permessi

**Soluzione:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Problema:** `pip install` fallisce con errori di certificato SSL

**Soluzione:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Conflitti di Versione dei Pacchetti

**Problema:** Versioni incompatibili dei pacchetti

**Soluzione:**

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

## Problemi con Jupyter Notebook

### Jupyter Non Si Avvia

**Problema:** Comando `jupyter notebook` non trovato

**Soluzione:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook Non Si Carica o Non Si Salva

**Problema:** "Notebook non caricato" o errori di salvataggio

**Soluzione:**

1. Controlla i permessi dei file
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Controlla la corruzione dei file
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Cancella la cache di Jupyter
```bash
jupyter notebook --clear-cache
```

### Celle Non Eseguono

**Problema:** La cella rimane bloccata su "In [*]" o impiega troppo tempo

**Soluzione:**

1. **Interrompi il kernel**: Clicca sul pulsante "Interrupt" o premi `I, I`
2. **Riavvia il kernel**: Menu Kernel → Restart
3. **Controlla cicli infiniti** nel tuo codice
4. **Cancella output**: Cell → All Output → Clear

### Grafici Non Visualizzati

**Problema:** I grafici di `matplotlib` non vengono mostrati nel notebook

**Soluzione:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternativa per grafici interattivi:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Problemi con l'Applicazione Quiz

### npm install Fallisce

**Problema:** Errori durante `npm install`

**Soluzione:**

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

### L'Applicazione Quiz Non Si Avvia

**Problema:** `npm run serve` fallisce

**Soluzione:**

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

### Porta Già in Uso

**Problema:** "Porta 8080 già in uso"

**Soluzione:**

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

### Quiz Non Carica o Pagina Bianca

**Problema:** L'app quiz si carica ma mostra una pagina bianca

**Soluzione:**

1. Controlla gli errori nella console del browser (F12)
2. Cancella cache e cookie del browser
3. Prova un browser diverso
4. Assicurati che JavaScript sia abilitato
5. Controlla se i blocchi pubblicitari interferiscono

```bash
# Rebuild the app
npm run build
npm run serve
```

## Problemi con Git e GitHub

### Git Non Riconosciuto

**Problema:** `git: command not found`

**Soluzione:**

**Windows:**
- Installa Git da [git-scm.com](https://git-scm.com/)
- Riavvia il terminale dopo l'installazione

**macOS:**

> **Nota:** Se non hai Homebrew installato, segui le istruzioni su [https://brew.sh/](https://brew.sh/) per installarlo prima.
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

### Clone Fallisce

**Problema:** `git clone` fallisce con errori di autenticazione

**Soluzione:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Permesso Negato (publickey)

**Problema:** Autenticazione con chiave SSH fallisce

**Soluzione:**

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

## Problemi con la Documentazione Docsify

### Comando Docsify Non Trovato

**Problema:** `docsify: command not found`

**Soluzione:**

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

### Documentazione Non Carica

**Problema:** Docsify si avvia ma il contenuto non si carica

**Soluzione:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Immagini Non Visualizzate

**Problema:** Le immagini mostrano l'icona di link rotto

**Soluzione:**

1. Controlla che i percorsi delle immagini siano relativi
2. Assicurati che i file immagine esistano nel repository
3. Cancella la cache del browser
4. Verifica che le estensioni dei file corrispondano (case-sensitive su alcuni sistemi)

## Problemi con Dati e File

### Errori di File Non Trovato

**Problema:** `FileNotFoundError` durante il caricamento dei dati

**Soluzione:**

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

### Errori di Lettura CSV

**Problema:** Errori durante la lettura di file CSV

**Soluzione:**

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

### Errori di Memoria con Dataset Grandi

**Problema:** `MemoryError` durante il caricamento di file grandi

**Soluzione:**

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

## Problemi di Prestazioni

### Prestazioni Lente del Notebook

**Problema:** I notebook funzionano molto lentamente

**Soluzione:**

1. **Riavvia il kernel e cancella l'output**
   - Kernel → Restart & Clear Output

2. **Chiudi i notebook non utilizzati**

3. **Ottimizza il codice:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Campiona dataset grandi:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Crash del Browser

**Problema:** Il browser si blocca o diventa non responsivo

**Soluzione:**

1. Chiudi le schede non utilizzate
2. Cancella la cache del browser
3. Aumenta la memoria del browser (Chrome: `chrome://settings/system`)
4. Usa JupyterLab invece:
```bash
pip install jupyterlab
jupyter lab
```

## Ottenere Ulteriore Aiuto

### Prima di Chiedere Aiuto

1. Controlla questa guida alla risoluzione dei problemi
2. Cerca su [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Consulta [INSTALLATION.md](INSTALLATION.md) e [USAGE.md](USAGE.md)
4. Prova a cercare il messaggio di errore online

### Come Chiedere Aiuto

Quando crei un problema o chiedi aiuto, includi:

1. **Sistema Operativo**: Windows, macOS o Linux (quale distribuzione)
2. **Versione di Python**: Esegui `python --version`
3. **Messaggio di Errore**: Copia il messaggio di errore completo
4. **Passaggi per Riprodurre**: Cosa hai fatto prima che si verificasse l'errore
5. **Cosa Hai Provato**: Soluzioni che hai già tentato

**Esempio:**
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

### Risorse della Comunità

- **GitHub Issues**: [Crea un problema](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Unisciti alla nostra comunità](https://aka.ms/ds4beginners/discord)
- **Discussioni**: [Discussioni su GitHub](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Forum di Q&A](https://docs.microsoft.com/answers/)

### Documentazione Correlata

- [INSTALLATION.md](INSTALLATION.md) - Istruzioni per l'installazione
- [USAGE.md](USAGE.md) - Come utilizzare il curriculum
- [CONTRIBUTING.md](CONTRIBUTING.md) - Come contribuire
- [README.md](README.md) - Panoramica del progetto

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.