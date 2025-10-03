<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:25:21+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "ro"
}
-->
# Ghid de Instalare

Acest ghid te va ajuta să configurezi mediul pentru a lucra cu curriculumul Data Science pentru Începători.

## Cuprins

- [Prerechizite](../..)
- [Opțiuni de Start Rapid](../..)
- [Instalare Locală](../..)
- [Verificarea Instalării](../..)

## Prerechizite

Înainte de a începe, ar trebui să ai:

- Familiaritate de bază cu linia de comandă/terminalul
- Un cont GitHub (gratuit)
- Conexiune stabilă la internet pentru configurarea inițială

## Opțiuni de Start Rapid

### Opțiunea 1: GitHub Codespaces (Recomandat pentru Începători)

Cea mai simplă modalitate de a începe este cu GitHub Codespaces, care oferă un mediu complet de dezvoltare direct în browser.

1. Accesează [repository-ul](https://github.com/microsoft/Data-Science-For-Beginners)
2. Dă clic pe meniul dropdown **Code**
3. Selectează fila **Codespaces**
4. Dă clic pe **Create codespace on main**
5. Așteaptă ca mediul să se inițializeze (2-3 minute)

Mediul tău este acum pregătit cu toate dependențele preinstalate!

### Opțiunea 2: Dezvoltare Locală

Pentru a lucra pe propriul computer, urmează instrucțiunile detaliate de mai jos.

## Instalare Locală

### Pasul 1: Instalează Git

Git este necesar pentru a clona repository-ul și a urmări modificările tale.

**Windows:**
- Descarcă de la [git-scm.com](https://git-scm.com/download/win)
- Rulează instalatorul cu setările implicite

**macOS:**
- Instalează prin Homebrew: `brew install git`
- Sau descarcă de la [git-scm.com](https://git-scm.com/download/mac)

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

### Pasul 2: Clonează Repository-ul

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Pasul 3: Instalează Python și Jupyter

Python 3.7 sau o versiune mai nouă este necesar pentru lecțiile de știința datelor.

**Windows:**
1. Descarcă Python de la [python.org](https://www.python.org/downloads/)
2. În timpul instalării, bifează "Add Python to PATH"
3. Verifică instalarea:
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

### Pasul 4: Configurează Mediul Python

Se recomandă utilizarea unui mediu virtual pentru a menține dependențele izolate.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Pasul 5: Instalează Pachetele Python

Instalează bibliotecile necesare pentru știința datelor:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Pasul 6: Instalează Node.js și npm (Pentru Aplicația de Quiz)

Aplicația de quiz necesită Node.js și npm.

**Windows/macOS:**
- Descarcă de la [nodejs.org](https://nodejs.org/) (se recomandă versiunea LTS)
- Rulează instalatorul

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

### Pasul 7: Instalează Dependențele Aplicației de Quiz

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Pasul 8: Instalează Docsify (Opțional)

Pentru acces offline la documentație:

```bash
npm install -g docsify-cli
```

## Verificarea Instalării

### Testează Python și Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Browserul tău ar trebui să se deschidă cu interfața Jupyter. Acum poți naviga la orice fișier `.ipynb` din lecții.

### Testează Aplicația de Quiz

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Aplicația de quiz ar trebui să fie disponibilă la `http://localhost:8080` (sau un alt port dacă 8080 este ocupat).

### Testează Serverul de Documentație

```bash
# From the root directory of the repository
docsify serve
```

Documentația ar trebui să fie disponibilă la `http://localhost:3000`.

## Utilizarea Containerelor Dev din VS Code

Dacă ai Docker instalat, poți utiliza Containerele Dev din VS Code:

1. Instalează [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Instalează [Visual Studio Code](https://code.visualstudio.com/)
3. Instalează extensia [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Deschide repository-ul în VS Code
5. Apasă `F1` și selectează "Remote-Containers: Reopen in Container"
6. Așteaptă ca containerul să se construiască (doar prima dată)

## Următorii Pași

- Explorează [README.md](README.md) pentru o privire de ansamblu asupra curriculumului
- Citește [USAGE.md](USAGE.md) pentru fluxuri de lucru și exemple comune
- Verifică [TROUBLESHOOTING.md](TROUBLESHOOTING.md) dacă întâmpini probleme
- Consultă [CONTRIBUTING.md](CONTRIBUTING.md) dacă vrei să contribui

## Obținerea Ajutorului

Dacă întâmpini probleme:

1. Consultă ghidul [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Caută probleme existente în [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Alătură-te comunității noastre pe [Discord](https://aka.ms/ds4beginners/discord)
4. Creează o nouă problemă cu informații detaliate despre problema ta

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.