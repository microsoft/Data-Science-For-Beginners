<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:39:38+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "el"
}
-->
# Οδηγός Αντιμετώπισης Προβλημάτων

Αυτός ο οδηγός παρέχει λύσεις σε κοινά προβλήματα που μπορεί να αντιμετωπίσετε κατά την εργασία σας με το πρόγραμμα σπουδών "Data Science for Beginners".

## Πίνακας Περιεχομένων

- [Προβλήματα με Python και Jupyter](../..)
- [Προβλήματα με Πακέτα και Εξαρτήσεις](../..)
- [Προβλήματα με Jupyter Notebook](../..)
- [Προβλήματα με την Εφαρμογή Quiz](../..)
- [Προβλήματα με Git και GitHub](../..)
- [Προβλήματα με την Τεκμηρίωση Docsify](../..)
- [Προβλήματα με Δεδομένα και Αρχεία](../..)
- [Προβλήματα Απόδοσης](../..)
- [Πώς να Ζητήσετε Επιπλέον Βοήθεια](../..)

## Προβλήματα με Python και Jupyter

### Python Δεν Βρέθηκε ή Λάθος Έκδοση

**Πρόβλημα:** `python: command not found` ή λάθος έκδοση Python

**Λύση:**

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

**Λύση για Windows:**
1. Εγκαταστήστε ξανά την Python από [python.org](https://www.python.org/)
2. Κατά την εγκατάσταση, επιλέξτε "Add Python to PATH"
3. Επανεκκινήστε το τερματικό/προτροπή εντολών

### Προβλήματα Ενεργοποίησης Εικονικού Περιβάλλοντος

**Πρόβλημα:** Το εικονικό περιβάλλον δεν ενεργοποιείται

**Λύση:**

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

**Επαλήθευση ενεργοποίησης:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Προβλήματα Kernel στο Jupyter

**Πρόβλημα:** "Kernel not found" ή "Kernel keeps dying"

**Λύση:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Πρόβλημα:** Λάθος έκδοση Python στο Jupyter

**Λύση:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Προβλήματα με Πακέτα και Εξαρτήσεις

### Σφάλματα Εισαγωγής

**Πρόβλημα:** `ModuleNotFoundError: No module named 'pandas'` (ή άλλα πακέτα)

**Λύση:**

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

### Αποτυχίες Εγκατάστασης με Pip

**Πρόβλημα:** `pip install` αποτυγχάνει με σφάλματα δικαιωμάτων

**Λύση:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Πρόβλημα:** `pip install` αποτυγχάνει με σφάλματα πιστοποιητικών SSL

**Λύση:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Συγκρούσεις Εκδόσεων Πακέτων

**Πρόβλημα:** Μη συμβατές εκδόσεις πακέτων

**Λύση:**

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

## Προβλήματα με Jupyter Notebook

### Το Jupyter Δεν Ξεκινά

**Πρόβλημα:** Η εντολή `jupyter notebook` δεν βρέθηκε

**Λύση:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Το Notebook Δεν Φορτώνει ή Δεν Αποθηκεύεται

**Πρόβλημα:** "Notebook failed to load" ή σφάλματα αποθήκευσης

**Λύση:**

1. Ελέγξτε τα δικαιώματα αρχείων
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Ελέγξτε για καταστροφή αρχείων
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Καθαρίστε την προσωρινή μνήμη του Jupyter
```bash
jupyter notebook --clear-cache
```

### Το Κελί Δεν Εκτελείται

**Πρόβλημα:** Το κελί μένει κολλημένο στο "In [*]" ή παίρνει πολύ χρόνο

**Λύση:**

1. **Διακόψτε τον kernel**: Πατήστε το κουμπί "Interrupt" ή πατήστε `I, I`
2. **Επανεκκινήστε τον kernel**: Μενού Kernel → Restart
3. **Ελέγξτε για άπειρους βρόχους** στον κώδικά σας
4. **Καθαρίστε την έξοδο**: Cell → All Output → Clear

### Τα Γραφήματα Δεν Εμφανίζονται

**Πρόβλημα:** Τα γραφήματα `matplotlib` δεν εμφανίζονται στο notebook

**Λύση:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Εναλλακτική για διαδραστικά γραφήματα:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Προβλήματα με την Εφαρμογή Quiz

### Αποτυχία npm install

**Πρόβλημα:** Σφάλματα κατά την εκτέλεση του `npm install`

**Λύση:**

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

### Η Εφαρμογή Quiz Δεν Ξεκινά

**Πρόβλημα:** Το `npm run serve` αποτυγχάνει

**Λύση:**

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

### Η Θύρα Είναι Ήδη Χρησιμοποιούμενη

**Πρόβλημα:** "Port 8080 is already in use"

**Λύση:**

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

### Το Quiz Δεν Φορτώνει ή Εμφανίζεται Κενή Σελίδα

**Πρόβλημα:** Η εφαρμογή Quiz φορτώνει αλλά εμφανίζει κενή σελίδα

**Λύση:**

1. Ελέγξτε την κονσόλα του προγράμματος περιήγησης για σφάλματα (F12)
2. Καθαρίστε την προσωρινή μνήμη και τα cookies του προγράμματος περιήγησης
3. Δοκιμάστε διαφορετικό πρόγραμμα περιήγησης
4. Βεβαιωθείτε ότι η JavaScript είναι ενεργοποιημένη
5. Ελέγξτε αν οι αποκλειστές διαφημίσεων προκαλούν παρεμβολές

```bash
# Rebuild the app
npm run build
npm run serve
```

## Προβλήματα με Git και GitHub

### Το Git Δεν Αναγνωρίζεται

**Πρόβλημα:** `git: command not found`

**Λύση:**

**Windows:**
- Εγκαταστήστε το Git από [git-scm.com](https://git-scm.com/)
- Επανεκκινήστε το τερματικό μετά την εγκατάσταση

**macOS:**

> **Σημείωση:** Αν δεν έχετε εγκαταστήσει το Homebrew, ακολουθήστε τις οδηγίες στο [https://brew.sh/](https://brew.sh/) για να το εγκαταστήσετε πρώτα.
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

### Αποτυχία Κλωνοποίησης

**Πρόβλημα:** Το `git clone` αποτυγχάνει με σφάλματα πιστοποίησης

**Λύση:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Άρνηση Δικαιωμάτων (publickey)

**Πρόβλημα:** Η πιστοποίηση με SSH key αποτυγχάνει

**Λύση:**

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

## Προβλήματα με την Τεκμηρίωση Docsify

### Η Εντολή Docsify Δεν Βρέθηκε

**Πρόβλημα:** `docsify: command not found`

**Λύση:**

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

### Η Τεκμηρίωση Δεν Φορτώνει

**Πρόβλημα:** Το Docsify εξυπηρετεί αλλά το περιεχόμενο δεν φορτώνει

**Λύση:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Οι Εικόνες Δεν Εμφανίζονται

**Πρόβλημα:** Οι εικόνες εμφανίζουν εικονίδιο σπασμένου συνδέσμου

**Λύση:**

1. Ελέγξτε αν οι διαδρομές εικόνων είναι σχετικές
2. Βεβαιωθείτε ότι τα αρχεία εικόνων υπάρχουν στο αποθετήριο
3. Καθαρίστε την προσωρινή μνήμη του προγράμματος περιήγησης
4. Επαληθεύστε ότι οι επεκτάσεις αρχείων ταιριάζουν (ευαίσθητο σε πεζά/κεφαλαία σε ορισμένα συστήματα)

## Προβλήματα με Δεδομένα και Αρχεία

### Σφάλματα "File Not Found"

**Πρόβλημα:** `FileNotFoundError` κατά τη φόρτωση δεδομένων

**Λύση:**

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

### Σφάλματα Ανάγνωσης CSV

**Πρόβλημα:** Σφάλματα κατά την ανάγνωση αρχείων CSV

**Λύση:**

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

### Σφάλματα Μνήμης με Μεγάλα Σύνολα Δεδομένων

**Πρόβλημα:** `MemoryError` κατά τη φόρτωση μεγάλων αρχείων

**Λύση:**

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

## Προβλήματα Απόδοσης

### Αργή Απόδοση Notebook

**Πρόβλημα:** Τα notebooks εκτελούνται πολύ αργά

**Λύση:**

1. **Επανεκκινήστε τον kernel και καθαρίστε την έξοδο**
   - Kernel → Restart & Clear Output

2. **Κλείστε αχρησιμοποίητα notebooks**

3. **Βελτιστοποιήστε τον κώδικα:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Δειγματοληψία μεγάλων συνόλων δεδομένων:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Κατάρρευση Προγράμματος Περιήγησης

**Πρόβλημα:** Το πρόγραμμα περιήγησης καταρρέει ή γίνεται μη ανταποκρίσιμο

**Λύση:**

1. Κλείστε αχρησιμοποίητες καρτέλες
2. Καθαρίστε την προσωρινή μνήμη του προγράμματος περιήγησης
3. Αυξήστε τη μνήμη του προγράμματος περιήγησης (Chrome: `chrome://settings/system`)
4. Χρησιμοποιήστε το JupyterLab αντί:
```bash
pip install jupyterlab
jupyter lab
```

## Πώς να Ζητήσετε Επιπλέον Βοήθεια

### Πριν Ζητήσετε Βοήθεια

1. Ελέγξτε αυτόν τον οδηγό αντιμετώπισης προβλημάτων
2. Αναζητήστε στα [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Εξετάστε τα [INSTALLATION.md](INSTALLATION.md) και [USAGE.md](USAGE.md)
4. Δοκιμάστε να αναζητήσετε το μήνυμα σφάλματος στο διαδίκτυο

### Πώς να Ζητήσετε Βοήθεια

Όταν δημιουργείτε ένα ζήτημα ή ζητάτε βοήθεια, συμπεριλάβετε:

1. **Λειτουργικό Σύστημα**: Windows, macOS ή Linux (ποια διανομή)
2. **Έκδοση Python**: Εκτελέστε `python --version`
3. **Μήνυμα Σφάλματος**: Αντιγράψτε το πλήρες μήνυμα σφάλματος
4. **Βήματα Αναπαραγωγής**: Τι κάνατε πριν εμφανιστεί το σφάλμα
5. **Τι Έχετε Δοκιμάσει**: Λύσεις που έχετε ήδη επιχειρήσει

**Παράδειγμα:**
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

### Πόροι Κοινότητας

- **GitHub Issues**: [Δημιουργήστε ένα ζήτημα](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Εγγραφείτε στην κοινότητά μας](https://aka.ms/ds4beginners/discord)
- **Συζητήσεις**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Φόρουμ Ερωτήσεων & Απαντήσεων](https://docs.microsoft.com/answers/)

### Σχετική Τεκμηρίωση

- [INSTALLATION.md](INSTALLATION.md) - Οδηγίες εγκατάστασης
- [USAGE.md](USAGE.md) - Πώς να χρησιμοποιήσετε το πρόγραμμα σπουδών
- [CONTRIBUTING.md](CONTRIBUTING.md) - Πώς να συνεισφέρετε
- [README.md](README.md) - Επισκόπηση του έργου

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.