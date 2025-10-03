<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:38:40+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "pl"
}
-->
# Przewodnik rozwiązywania problemów

Ten przewodnik zawiera rozwiązania typowych problemów, które możesz napotkać podczas pracy z programem nauczania "Data Science for Beginners".

## Spis treści

- [Problemy z Pythonem i Jupyter](../..)
- [Problemy z pakietami i zależnościami](../..)
- [Problemy z Jupyter Notebook](../..)
- [Problemy z aplikacją quizową](../..)
- [Problemy z Git i GitHub](../..)
- [Problemy z dokumentacją Docsify](../..)
- [Problemy z danymi i plikami](../..)
- [Problemy z wydajnością](../..)
- [Uzyskiwanie dodatkowej pomocy](../..)

## Problemy z Pythonem i Jupyter

### Python nie znaleziony lub niewłaściwa wersja

**Problem:** `python: command not found` lub niewłaściwa wersja Pythona

**Rozwiązanie:**

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

**Rozwiązanie dla Windows:**
1. Zainstaluj ponownie Pythona z [python.org](https://www.python.org/)
2. Podczas instalacji zaznacz opcję "Add Python to PATH"
3. Uruchom ponownie terminal/wiersz poleceń

### Problemy z aktywacją wirtualnego środowiska

**Problem:** Wirtualne środowisko nie chce się aktywować

**Rozwiązanie:**

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

**Sprawdź aktywację:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Problemy z Jupyter Kernel

**Problem:** "Kernel not found" lub "Kernel keeps dying"

**Rozwiązanie:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Problem:** Niewłaściwa wersja Pythona w Jupyter

**Rozwiązanie:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Problemy z pakietami i zależnościami

### Błędy importu

**Problem:** `ModuleNotFoundError: No module named 'pandas'` (lub inne pakiety)

**Rozwiązanie:**

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

### Problemy z instalacją pip

**Problem:** `pip install` kończy się błędami uprawnień

**Rozwiązanie:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Problem:** `pip install` kończy się błędami certyfikatu SSL

**Rozwiązanie:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Konflikty wersji pakietów

**Problem:** Niekompatybilne wersje pakietów

**Rozwiązanie:**

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

## Problemy z Jupyter Notebook

### Jupyter nie chce się uruchomić

**Problem:** Komenda `jupyter notebook` nie została znaleziona

**Rozwiązanie:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook nie chce się załadować lub zapisać

**Problem:** "Notebook failed to load" lub błędy zapisu

**Rozwiązanie:**

1. Sprawdź uprawnienia do plików
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Sprawdź, czy plik nie jest uszkodzony
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Wyczyść pamięć podręczną Jupyter
```bash
jupyter notebook --clear-cache
```

### Komórka nie chce się wykonać

**Problem:** Komórka utknęła na "In [*]" lub wykonuje się bardzo długo

**Rozwiązanie:**

1. **Przerwij kernel**: Kliknij przycisk "Interrupt" lub naciśnij `I, I`
2. **Zrestartuj kernel**: Menu Kernel → Restart
3. **Sprawdź, czy w kodzie nie ma pętli nieskończonych**
4. **Wyczyść wyniki**: Cell → All Output → Clear

### Wykresy nie wyświetlają się

**Problem:** Wykresy `matplotlib` nie pojawiają się w notebooku

**Rozwiązanie:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Alternatywa dla interaktywnych wykresów:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Problemy z aplikacją quizową

### npm install kończy się błędami

**Problem:** Błędy podczas `npm install`

**Rozwiązanie:**

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

### Aplikacja quizowa nie chce się uruchomić

**Problem:** `npm run serve` kończy się błędami

**Rozwiązanie:**

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

### Port już zajęty

**Problem:** "Port 8080 is already in use"

**Rozwiązanie:**

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

### Quiz nie ładuje się lub pokazuje pustą stronę

**Problem:** Aplikacja quizowa ładuje się, ale pokazuje pustą stronę

**Rozwiązanie:**

1. Sprawdź błędy w konsoli przeglądarki (F12)
2. Wyczyść pamięć podręczną i ciasteczka przeglądarki
3. Spróbuj użyć innej przeglądarki
4. Upewnij się, że JavaScript jest włączony
5. Sprawdź, czy blokery reklam nie przeszkadzają

```bash
# Rebuild the app
npm run build
npm run serve
```

## Problemy z Git i GitHub

### Git nie rozpoznany

**Problem:** `git: command not found`

**Rozwiązanie:**

**Windows:**
- Zainstaluj Git z [git-scm.com](https://git-scm.com/)
- Uruchom ponownie terminal po instalacji

**macOS:**

> **Uwaga:** Jeśli nie masz zainstalowanego Homebrew, postępuj zgodnie z instrukcjami na [https://brew.sh/](https://brew.sh/), aby go zainstalować.
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

### Clone kończy się błędami

**Problem:** `git clone` kończy się błędami uwierzytelnienia

**Rozwiązanie:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Permission Denied (publickey)

**Problem:** Błąd uwierzytelnienia klucza SSH

**Rozwiązanie:**

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

## Problemy z dokumentacją Docsify

### Komenda Docsify nie została znaleziona

**Problem:** `docsify: command not found`

**Rozwiązanie:**

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

### Dokumentacja nie ładuje się

**Problem:** Docsify działa, ale treść się nie ładuje

**Rozwiązanie:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Obrazy nie wyświetlają się

**Problem:** Obrazy pokazują ikonę uszkodzonego linku

**Rozwiązanie:**

1. Sprawdź, czy ścieżki do obrazów są względne
2. Upewnij się, że pliki obrazów istnieją w repozytorium
3. Wyczyść pamięć podręczną przeglądarki
4. Sprawdź, czy rozszerzenia plików są zgodne (wrażliwe na wielkość liter w niektórych systemach)

## Problemy z danymi i plikami

### Błędy "File Not Found"

**Problem:** `FileNotFoundError` podczas ładowania danych

**Rozwiązanie:**

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

### Błędy podczas odczytu CSV

**Problem:** Błędy podczas odczytu plików CSV

**Rozwiązanie:**

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

### Błędy pamięci przy dużych zbiorach danych

**Problem:** `MemoryError` podczas ładowania dużych plików

**Rozwiązanie:**

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

## Problemy z wydajnością

### Wolne działanie notebooków

**Problem:** Notebooki działają bardzo wolno

**Rozwiązanie:**

1. **Zrestartuj kernel i wyczyść wyniki**
   - Kernel → Restart & Clear Output

2. **Zamknij nieużywane notebooki**

3. **Optymalizuj kod:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Próbkuj duże zbiory danych:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Zawieszanie się przeglądarki

**Problem:** Przeglądarka zawiesza się lub staje się nieodpowiedzialna

**Rozwiązanie:**

1. Zamknij nieużywane karty
2. Wyczyść pamięć podręczną przeglądarki
3. Zwiększ pamięć przeglądarki (Chrome: `chrome://settings/system`)
4. Użyj JupyterLab zamiast:
```bash
pip install jupyterlab
jupyter lab
```

## Uzyskiwanie dodatkowej pomocy

### Zanim poprosisz o pomoc

1. Sprawdź ten przewodnik rozwiązywania problemów
2. Przeszukaj [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Przejrzyj [INSTALLATION.md](INSTALLATION.md) i [USAGE.md](USAGE.md)
4. Spróbuj wyszukać komunikat błędu w internecie

### Jak poprosić o pomoc

Tworząc zgłoszenie lub prosząc o pomoc, podaj:

1. **System operacyjny**: Windows, macOS lub Linux (jaka dystrybucja)
2. **Wersja Pythona**: Uruchom `python --version`
3. **Komunikat błędu**: Skopiuj pełny komunikat błędu
4. **Kroki do odtworzenia**: Co zrobiłeś przed wystąpieniem błędu
5. **Co już próbowałeś**: Rozwiązania, które już wypróbowałeś

**Przykład:**
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

### Zasoby społecznościowe

- **GitHub Issues**: [Utwórz zgłoszenie](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Dołącz do naszej społeczności](https://aka.ms/ds4beginners/discord)
- **Dyskusje**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Fora Q&A](https://docs.microsoft.com/answers/)

### Powiązana dokumentacja

- [INSTALLATION.md](INSTALLATION.md) - Instrukcje instalacji
- [USAGE.md](USAGE.md) - Jak korzystać z programu nauczania
- [CONTRIBUTING.md](CONTRIBUTING.md) - Jak wnosić wkład
- [README.md](README.md) - Przegląd projektu

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.