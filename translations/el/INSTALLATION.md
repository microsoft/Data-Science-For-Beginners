<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:20:45+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "el"
}
-->
# Οδηγός Εγκατάστασης

Αυτός ο οδηγός θα σας βοηθήσει να ρυθμίσετε το περιβάλλον σας για να εργαστείτε με το πρόγραμμα σπουδών "Data Science for Beginners".

## Περιεχόμενα

- [Προαπαιτούμενα](../..)
- [Γρήγορες Επιλογές Έναρξης](../..)
- [Τοπική Εγκατάσταση](../..)
- [Επαλήθευση Εγκατάστασης](../..)

## Προαπαιτούμενα

Πριν ξεκινήσετε, θα πρέπει να έχετε:

- Βασική εξοικείωση με τη γραμμή εντολών/τερματικό
- Λογαριασμό GitHub (δωρεάν)
- Σταθερή σύνδεση στο διαδίκτυο για την αρχική ρύθμιση

## Γρήγορες Επιλογές Έναρξης

### Επιλογή 1: GitHub Codespaces (Συνιστάται για Αρχάριους)

Ο πιο εύκολος τρόπος για να ξεκινήσετε είναι με το GitHub Codespaces, το οποίο παρέχει ένα πλήρες περιβάλλον ανάπτυξης στον περιηγητή σας.

1. Μεταβείτε στο [αποθετήριο](https://github.com/microsoft/Data-Science-For-Beginners)
2. Κάντε κλικ στο μενού **Code**
3. Επιλέξτε την καρτέλα **Codespaces**
4. Κάντε κλικ στο **Create codespace on main**
5. Περιμένετε να ολοκληρωθεί η αρχικοποίηση του περιβάλλοντος (2-3 λεπτά)

Το περιβάλλον σας είναι τώρα έτοιμο με όλες τις εξαρτήσεις προεγκατεστημένες!

### Επιλογή 2: Τοπική Ανάπτυξη

Για εργασία στον δικό σας υπολογιστή, ακολουθήστε τις λεπτομερείς οδηγίες παρακάτω.

## Τοπική Εγκατάσταση

### Βήμα 1: Εγκατάσταση Git

Το Git απαιτείται για την κλωνοποίηση του αποθετηρίου και την παρακολούθηση των αλλαγών σας.

**Windows:**
- Κατεβάστε από [git-scm.com](https://git-scm.com/download/win)
- Εκτελέστε τον εγκαταστάτη με τις προεπιλεγμένες ρυθμίσεις

**macOS:**
- Εγκαταστήστε μέσω Homebrew: `brew install git`
- Ή κατεβάστε από [git-scm.com](https://git-scm.com/download/mac)

**Linux:**
```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

### Βήμα 2: Κλωνοποίηση του Αποθετηρίου

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Βήμα 3: Εγκατάσταση Python και Jupyter

Απαιτείται Python 3.7 ή νεότερη έκδοση για τα μαθήματα επιστήμης δεδομένων.

**Windows:**
1. Κατεβάστε την Python από [python.org](https://www.python.org/downloads/)
2. Κατά την εγκατάσταση, επιλέξτε "Add Python to PATH"
3. Επαληθεύστε την εγκατάσταση:
```bash
python --version
```

**macOS:**
```bash
# Using Homebrew
brew install python3

# Verify installation
python3 --version
```

**Linux:**
```bash
# Most Linux distributions come with Python pre-installed
python3 --version

# If not installed:
# Debian/Ubuntu
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

### Βήμα 4: Ρύθμιση Περιβάλλοντος Python

Συνιστάται η χρήση εικονικού περιβάλλοντος για την απομόνωση των εξαρτήσεων.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Βήμα 5: Εγκατάσταση Πακέτων Python

Εγκαταστήστε τις απαραίτητες βιβλιοθήκες επιστήμης δεδομένων:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Βήμα 6: Εγκατάσταση Node.js και npm (Για την Εφαρμογή Κουίζ)

Η εφαρμογή κουίζ απαιτεί Node.js και npm.

**Windows/macOS:**
- Κατεβάστε από [nodejs.org](https://nodejs.org/) (Συνιστάται η έκδοση LTS)
- Εκτελέστε τον εγκαταστάτη

**Linux:**
```bash
# Debian/Ubuntu
# WARNING: Piping scripts from the internet directly into bash can be a security risk.
# It is recommended to review the script before running it:
#   curl -fsSL https://deb.nodesource.com/setup_lts.x -o setup_lts.x
#   less setup_lts.x
# Then run:
#   sudo -E bash setup_lts.x
#
# Alternatively, you can use the one-liner below at your own risk:
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# Fedora
sudo dnf install nodejs

# Verify installation
node --version
npm --version
```

### Βήμα 7: Εγκατάσταση Εξαρτήσεων Εφαρμογής Κουίζ

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Βήμα 8: Εγκατάσταση Docsify (Προαιρετικό)

Για πρόσβαση στην τεκμηρίωση εκτός σύνδεσης:

```bash
npm install -g docsify-cli
```

## Επαλήθευση Εγκατάστασης

### Δοκιμή Python και Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Ο περιηγητής σας θα πρέπει να ανοίξει με τη διεπαφή Jupyter. Μπορείτε τώρα να πλοηγηθείτε σε οποιοδήποτε αρχείο `.ipynb` του μαθήματος.

### Δοκιμή Εφαρμογής Κουίζ

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Η εφαρμογή κουίζ θα πρέπει να είναι διαθέσιμη στη διεύθυνση `http://localhost:8080` (ή σε άλλη θύρα αν η 8080 είναι απασχολημένη).

### Δοκιμή Διακομιστή Τεκμηρίωσης

```bash
# From the root directory of the repository
docsify serve
```

Η τεκμηρίωση θα πρέπει να είναι διαθέσιμη στη διεύθυνση `http://localhost:3000`.

## Χρήση Dev Containers στο VS Code

Αν έχετε εγκατεστημένο το Docker, μπορείτε να χρησιμοποιήσετε Dev Containers στο VS Code:

1. Εγκαταστήστε το [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Εγκαταστήστε το [Visual Studio Code](https://code.visualstudio.com/)
3. Εγκαταστήστε την επέκταση [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Ανοίξτε το αποθετήριο στο VS Code
5. Πατήστε `F1` και επιλέξτε "Remote-Containers: Reopen in Container"
6. Περιμένετε να δημιουργηθεί το container (μόνο την πρώτη φορά)

## Επόμενα Βήματα

- Εξερευνήστε το [README.md](README.md) για μια επισκόπηση του προγράμματος σπουδών
- Διαβάστε το [USAGE.md](USAGE.md) για συνήθεις ροές εργασίας και παραδείγματα
- Ελέγξτε το [TROUBLESHOOTING.md](TROUBLESHOOTING.md) αν αντιμετωπίσετε προβλήματα
- Ανατρέξτε στο [CONTRIBUTING.md](CONTRIBUTING.md) αν θέλετε να συνεισφέρετε

## Λήψη Βοήθειας

Αν αντιμετωπίσετε προβλήματα:

1. Ελέγξτε τον οδηγό [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Αναζητήστε υπάρχοντα [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Εγγραφείτε στην [κοινότητα Discord](https://aka.ms/ds4beginners/discord)
4. Δημιουργήστε ένα νέο issue με λεπτομερείς πληροφορίες για το πρόβλημά σας

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.