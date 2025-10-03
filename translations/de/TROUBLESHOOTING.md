<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:29:25+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "de"
}
-->
# Fehlerbehebungsleitfaden

Dieser Leitfaden bietet Lösungen für häufige Probleme, die beim Arbeiten mit dem Data Science for Beginners-Lehrplan auftreten können.

## Inhaltsverzeichnis

- [Python- und Jupyter-Probleme](../..)
- [Paket- und Abhängigkeitsprobleme](../..)
- [Jupyter-Notebook-Probleme](../..)
- [Quiz-Anwendungsprobleme](../..)
- [Git- und GitHub-Probleme](../..)
- [Docsify-Dokumentationsprobleme](../..)
- [Daten- und Datei-Probleme](../..)
- [Leistungsprobleme](../..)
- [Weitere Hilfe erhalten](../..)

## Python- und Jupyter-Probleme

### Python nicht gefunden oder falsche Version

**Problem:** `python: command not found` oder falsche Python-Version

**Lösung:**

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

**Lösung für Windows:**
1. Installieren Sie Python neu von [python.org](https://www.python.org/)
2. Aktivieren Sie während der Installation die Option "Add Python to PATH"
3. Starten Sie Ihr Terminal/den Kommandozeilen-Prompt neu

### Probleme mit der Aktivierung der virtuellen Umgebung

**Problem:** Virtuelle Umgebung lässt sich nicht aktivieren

**Lösung:**

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

**Aktivierung überprüfen:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter-Kernel-Probleme

**Problem:** "Kernel nicht gefunden" oder "Kernel stürzt ab"

**Lösung:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Problem:** Falsche Python-Version in Jupyter

**Lösung:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Paket- und Abhängigkeitsprobleme

### Importfehler

**Problem:** `ModuleNotFoundError: No module named 'pandas'` (oder andere Pakete)

**Lösung:**

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

### Fehler bei der Pip-Installation

**Problem:** `pip install` schlägt mit Berechtigungsfehlern fehl

**Lösung:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Problem:** `pip install` schlägt mit SSL-Zertifikatsfehlern fehl

**Lösung:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Konflikte bei Paketversionen

**Problem:** Inkompatible Paketversionen

**Lösung:**

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

## Jupyter-Notebook-Probleme

### Jupyter startet nicht

**Problem:** `jupyter notebook`-Befehl nicht gefunden

**Lösung:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook lädt oder speichert nicht

**Problem:** "Notebook konnte nicht geladen werden" oder Speicherfehler

**Lösung:**

1. Überprüfen Sie die Dateiberechtigungen
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Überprüfen Sie auf Dateibeschädigungen
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Löschen Sie den Jupyter-Cache
```bash
jupyter notebook --clear-cache
```

### Zelle wird nicht ausgeführt

**Problem:** Zelle bleibt bei "In [*]" hängen oder benötigt ewig

**Lösung:**

1. **Kernel unterbrechen**: Klicken Sie auf die Schaltfläche "Interrupt" oder drücken Sie `I, I`
2. **Kernel neu starten**: Menü "Kernel" → Neustart
3. **Überprüfen Sie auf Endlosschleifen** in Ihrem Code
4. **Ausgabe löschen**: Zelle → Alle Ausgaben → Löschen

### Diagramme werden nicht angezeigt

**Problem:** `matplotlib`-Diagramme werden im Notebook nicht angezeigt

**Lösung:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternative für interaktive Diagramme:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Quiz-Anwendungsprobleme

### npm install schlägt fehl

**Problem:** Fehler während `npm install`

**Lösung:**

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

### Quiz-App startet nicht

**Problem:** `npm run serve` schlägt fehl

**Lösung:**

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

### Port bereits in Verwendung

**Problem:** "Port 8080 ist bereits in Verwendung"

**Lösung:**

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

### Quiz lädt nicht oder zeigt eine leere Seite

**Problem:** Quiz-App lädt, zeigt aber eine leere Seite

**Lösung:**

1. Überprüfen Sie die Browser-Konsole auf Fehler (F12)
2. Löschen Sie den Browser-Cache und die Cookies
3. Probieren Sie einen anderen Browser aus
4. Stellen Sie sicher, dass JavaScript aktiviert ist
5. Überprüfen Sie, ob Werbeblocker stören

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git- und GitHub-Probleme

### Git wird nicht erkannt

**Problem:** `git: command not found`

**Lösung:**

**Windows:**
- Installieren Sie Git von [git-scm.com](https://git-scm.com/)
- Starten Sie das Terminal nach der Installation neu

**macOS:**

> **Hinweis:** Wenn Sie Homebrew nicht installiert haben, folgen Sie den Anweisungen unter [https://brew.sh/](https://brew.sh/), um es zuerst zu installieren.
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

### Klonen schlägt fehl

**Problem:** `git clone` schlägt mit Authentifizierungsfehlern fehl

**Lösung:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Berechtigung verweigert (publickey)

**Problem:** SSH-Schlüssel-Authentifizierung schlägt fehl

**Lösung:**

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

## Docsify-Dokumentationsprobleme

### Docsify-Befehl nicht gefunden

**Problem:** `docsify: command not found`

**Lösung:**

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

### Dokumentation lädt nicht

**Problem:** Docsify wird bereitgestellt, aber Inhalte laden nicht

**Lösung:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Bilder werden nicht angezeigt

**Problem:** Bilder zeigen ein Symbol für defekte Links

**Lösung:**

1. Überprüfen Sie, ob die Bildpfade relativ sind
2. Stellen Sie sicher, dass die Bilddateien im Repository vorhanden sind
3. Löschen Sie den Browser-Cache
4. Überprüfen Sie, ob die Dateierweiterungen übereinstimmen (auf manchen Systemen case-sensitiv)

## Daten- und Datei-Probleme

### Datei nicht gefunden Fehler

**Problem:** `FileNotFoundError` beim Laden von Daten

**Lösung:**

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

### Fehler beim Lesen von CSV-Dateien

**Problem:** Fehler beim Lesen von CSV-Dateien

**Lösung:**

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

### Speicherfehler bei großen Datensätzen

**Problem:** `MemoryError` beim Laden großer Dateien

**Lösung:**

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

## Leistungsprobleme

### Langsame Notebook-Leistung

**Problem:** Notebooks laufen sehr langsam

**Lösung:**

1. **Kernel neu starten und Ausgabe löschen**
   - Kernel → Neustart & Ausgabe löschen

2. **Nicht verwendete Notebooks schließen**

3. **Code optimieren:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Große Datensätze stichprobenartig verwenden:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Browser-Abstürze

**Problem:** Browser stürzt ab oder reagiert nicht mehr

**Lösung:**

1. Schließen Sie nicht verwendete Tabs
2. Löschen Sie den Browser-Cache
3. Erhöhen Sie den Browser-Speicher (Chrome: `chrome://settings/system`)
4. Verwenden Sie stattdessen JupyterLab:
```bash
pip install jupyterlab
jupyter lab
```

## Weitere Hilfe erhalten

### Bevor Sie um Hilfe bitten

1. Überprüfen Sie diesen Fehlerbehebungsleitfaden
2. Suchen Sie in [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Lesen Sie [INSTALLATION.md](INSTALLATION.md) und [USAGE.md](USAGE.md)
4. Suchen Sie die Fehlermeldung online

### Wie man um Hilfe bittet

Wenn Sie ein Problem erstellen oder um Hilfe bitten, geben Sie Folgendes an:

1. **Betriebssystem**: Windows, macOS oder Linux (welche Distribution)
2. **Python-Version**: Führen Sie `python --version` aus
3. **Fehlermeldung**: Kopieren Sie die vollständige Fehlermeldung
4. **Schritte zur Reproduktion**: Was Sie getan haben, bevor der Fehler auftrat
5. **Was Sie bereits versucht haben**: Lösungen, die Sie bereits ausprobiert haben

**Beispiel:**
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

### Community-Ressourcen

- **GitHub Issues**: [Problem erstellen](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Treten Sie unserer Community bei](https://aka.ms/ds4beginners/discord)
- **Diskussionen**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Q&A-Foren](https://docs.microsoft.com/answers/)

### Verwandte Dokumentation

- [INSTALLATION.md](INSTALLATION.md) - Installationsanweisungen
- [USAGE.md](USAGE.md) - Anleitung zur Nutzung des Lehrplans
- [CONTRIBUTING.md](CONTRIBUTING.md) - Wie man beiträgt
- [README.md](README.md) - Projektübersicht

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.