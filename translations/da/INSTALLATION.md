<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:21:35+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "da"
}
-->
# Installationsvejledning

Denne vejledning hjælper dig med at opsætte dit miljø til at arbejde med Data Science for Beginners-kurset.

## Indholdsfortegnelse

- [Forudsætninger](../..)
- [Hurtige Startmuligheder](../..)
- [Lokal Installation](../..)
- [Bekræft Din Installation](../..)

## Forudsætninger

Før du begynder, bør du have:

- Grundlæggende kendskab til kommandolinjen/terminalen
- En GitHub-konto (gratis)
- Stabil internetforbindelse til den første opsætning

## Hurtige Startmuligheder

### Mulighed 1: GitHub Codespaces (Anbefales til begyndere)

Den nemmeste måde at komme i gang på er med GitHub Codespaces, som giver et komplet udviklingsmiljø direkte i din browser.

1. Gå til [repositoryet](https://github.com/microsoft/Data-Science-For-Beginners)
2. Klik på **Code**-dropdown-menuen
3. Vælg fanen **Codespaces**
4. Klik på **Create codespace on main**
5. Vent på, at miljøet initialiseres (2-3 minutter)

Dit miljø er nu klar med alle nødvendige afhængigheder forudinstalleret!

### Mulighed 2: Lokal Udvikling

Hvis du vil arbejde på din egen computer, skal du følge de detaljerede instruktioner nedenfor.

## Lokal Installation

### Trin 1: Installer Git

Git er nødvendigt for at klone repositoryet og spore dine ændringer.

**Windows:**
- Download fra [git-scm.com](https://git-scm.com/download/win)
- Kør installationsprogrammet med standardindstillinger

**macOS:**
- Installer via Homebrew: `brew install git`
- Eller download fra [git-scm.com](https://git-scm.com/download/mac)

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

### Trin 2: Klon Repositoryet

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Trin 3: Installer Python og Jupyter

Python 3.7 eller nyere er påkrævet til data science-lektionerne.

**Windows:**
1. Download Python fra [python.org](https://www.python.org/downloads/)
2. Under installationen, marker "Add Python to PATH"
3. Bekræft installationen:
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

### Trin 4: Opsæt Python-miljø

Det anbefales at bruge et virtuelt miljø for at holde afhængigheder isolerede.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Trin 5: Installer Python-pakker

Installer de nødvendige data science-biblioteker:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Trin 6: Installer Node.js og npm (Til Quiz App)

Quiz-applikationen kræver Node.js og npm.

**Windows/macOS:**
- Download fra [nodejs.org](https://nodejs.org/) (LTS-version anbefales)
- Kør installationsprogrammet

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

### Trin 7: Installer Quiz App-afhængigheder

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Trin 8: Installer Docsify (Valgfrit)

For offline adgang til dokumentation:

```bash
npm install -g docsify-cli
```

## Bekræft Din Installation

### Test Python og Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Din browser bør åbne med Jupyter-grænsefladen. Du kan nu navigere til enhver lektions `.ipynb`-fil.

### Test Quiz-applikationen

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Quiz-applikationen bør være tilgængelig på `http://localhost:8080` (eller en anden port, hvis 8080 er optaget).

### Test Dokumentationsserveren

```bash
# From the root directory of the repository
docsify serve
```

Dokumentationen bør være tilgængelig på `http://localhost:3000`.

## Brug af VS Code Dev Containers

Hvis du har Docker installeret, kan du bruge VS Code Dev Containers:

1. Installer [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Installer [Visual Studio Code](https://code.visualstudio.com/)
3. Installer [Remote - Containers-udvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Åbn repositoryet i VS Code
5. Tryk `F1` og vælg "Remote-Containers: Reopen in Container"
6. Vent på, at containeren bygges (kun første gang)

## Næste Skridt

- Udforsk [README.md](README.md) for et overblik over kurset
- Læs [USAGE.md](USAGE.md) for almindelige arbejdsgange og eksempler
- Tjek [TROUBLESHOOTING.md](TROUBLESHOOTING.md), hvis du støder på problemer
- Gennemgå [CONTRIBUTING.md](CONTRIBUTING.md), hvis du vil bidrage

## Få Hjælp

Hvis du støder på problemer:

1. Tjek [TROUBLESHOOTING.md](TROUBLESHOOTING.md)-guiden
2. Søg efter eksisterende [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Deltag i vores [Discord-community](https://aka.ms/ds4beginners/discord)
4. Opret en ny issue med detaljeret information om dit problem

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.