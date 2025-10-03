<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:21:48+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "no"
}
-->
# Installasjonsveiledning

Denne veiledningen hjelper deg med å sette opp miljøet ditt for å jobbe med Data Science for Beginners-kurset.

## Innholdsfortegnelse

- [Forutsetninger](../..)
- [Hurtigstartalternativer](../..)
- [Lokal installasjon](../..)
- [Verifiser installasjonen din](../..)

## Forutsetninger

Før du begynner, bør du ha:

- Grunnleggende kjennskap til kommandolinje/terminal
- En GitHub-konto (gratis)
- Stabil internettforbindelse for den første oppsettet

## Hurtigstartalternativer

### Alternativ 1: GitHub Codespaces (Anbefalt for nybegynnere)

Den enkleste måten å komme i gang på er med GitHub Codespaces, som gir et komplett utviklingsmiljø i nettleseren din.

1. Gå til [repositoryet](https://github.com/microsoft/Data-Science-For-Beginners)
2. Klikk på **Code**-menyen
3. Velg fanen **Codespaces**
4. Klikk på **Create codespace on main**
5. Vent til miljøet initialiseres (2-3 minutter)

Miljøet ditt er nå klart med alle avhengigheter forhåndsinstallert!

### Alternativ 2: Lokal utvikling

For å jobbe på din egen datamaskin, følg de detaljerte instruksjonene nedenfor.

## Lokal installasjon

### Trinn 1: Installer Git

Git er nødvendig for å klone repositoryet og spore endringene dine.

**Windows:**
- Last ned fra [git-scm.com](https://git-scm.com/download/win)
- Kjør installasjonsprogrammet med standardinnstillinger

**macOS:**
- Installer via Homebrew: `brew install git`
- Eller last ned fra [git-scm.com](https://git-scm.com/download/mac)

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

### Trinn 2: Klon repositoryet

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Trinn 3: Installer Python og Jupyter

Python 3.7 eller nyere er nødvendig for data science-leksjonene.

**Windows:**
1. Last ned Python fra [python.org](https://www.python.org/downloads/)
2. Under installasjonen, kryss av for "Add Python to PATH"
3. Verifiser installasjonen:
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

### Trinn 4: Sett opp Python-miljø

Det anbefales å bruke et virtuelt miljø for å holde avhengigheter isolert.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Trinn 5: Installer Python-pakker

Installer de nødvendige data science-bibliotekene:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Trinn 6: Installer Node.js og npm (For Quiz App)

Quiz-applikasjonen krever Node.js og npm.

**Windows/macOS:**
- Last ned fra [nodejs.org](https://nodejs.org/) (LTS-versjon anbefales)
- Kjør installasjonsprogrammet

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

### Trinn 7: Installer Quiz App-avhengigheter

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Trinn 8: Installer Docsify (Valgfritt)

For offline tilgang til dokumentasjon:

```bash
npm install -g docsify-cli
```

## Verifiser installasjonen din

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

Nettleseren din skal åpne med Jupyter-grensesnittet. Du kan nå navigere til en leksjons `.ipynb`-fil.

### Test Quiz-applikasjonen

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Quiz-applikasjonen skal være tilgjengelig på `http://localhost:8080` (eller en annen port hvis 8080 er opptatt).

### Test dokumentasjonsserveren

```bash
# From the root directory of the repository
docsify serve
```

Dokumentasjonen skal være tilgjengelig på `http://localhost:3000`.

## Bruke VS Code Dev Containers

Hvis du har Docker installert, kan du bruke VS Code Dev Containers:

1. Installer [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Installer [Visual Studio Code](https://code.visualstudio.com/)
3. Installer [Remote - Containers-utvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Åpne repositoryet i VS Code
5. Trykk `F1` og velg "Remote-Containers: Reopen in Container"
6. Vent til containeren bygges (kun første gang)

## Neste steg

- Utforsk [README.md](README.md) for en oversikt over kurset
- Les [USAGE.md](USAGE.md) for vanlige arbeidsflyter og eksempler
- Sjekk [TROUBLESHOOTING.md](TROUBLESHOOTING.md) hvis du støter på problemer
- Gå gjennom [CONTRIBUTING.md](CONTRIBUTING.md) hvis du vil bidra

## Få hjelp

Hvis du støter på problemer:

1. Sjekk [TROUBLESHOOTING.md](TROUBLESHOOTING.md)-veiledningen
2. Søk etter eksisterende [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Bli med i vår [Discord-community](https://aka.ms/ds4beginners/discord)
4. Opprett en ny issue med detaljert informasjon om problemet ditt

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.