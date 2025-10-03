<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:22:21+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "nl"
}
-->
# Installatiegids

Deze gids helpt je om je omgeving in te stellen voor het werken met het curriculum Data Science voor Beginners.

## Inhoudsopgave

- [Vereisten](../..)
- [Snelle Startopties](../..)
- [Lokale Installatie](../..)
- [Controleer je Installatie](../..)

## Vereisten

Voordat je begint, zorg ervoor dat je:

- Basiskennis hebt van de command line/terminal
- Een GitHub-account hebt (gratis)
- Een stabiele internetverbinding hebt voor de initiële setup

## Snelle Startopties

### Optie 1: GitHub Codespaces (Aanbevolen voor Beginners)

De eenvoudigste manier om te beginnen is met GitHub Codespaces, dat een complete ontwikkelomgeving in je browser biedt.

1. Ga naar de [repository](https://github.com/microsoft/Data-Science-For-Beginners)
2. Klik op het **Code** dropdownmenu
3. Selecteer het tabblad **Codespaces**
4. Klik op **Create codespace on main**
5. Wacht tot de omgeving is geïnitialiseerd (2-3 minuten)

Je omgeving is nu klaar met alle vereiste afhankelijkheden vooraf geïnstalleerd!

### Optie 2: Lokale Ontwikkeling

Voor werken op je eigen computer, volg de gedetailleerde instructies hieronder.

## Lokale Installatie

### Stap 1: Installeer Git

Git is nodig om de repository te klonen en je wijzigingen bij te houden.

**Windows:**
- Download van [git-scm.com](https://git-scm.com/download/win)
- Voer de installer uit met de standaardinstellingen

**macOS:**
- Installeer via Homebrew: `brew install git`
- Of download van [git-scm.com](https://git-scm.com/download/mac)

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

### Stap 2: Clone de Repository

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Stap 3: Installeer Python en Jupyter

Python 3.7 of hoger is vereist voor de data science-lessen.

**Windows:**
1. Download Python van [python.org](https://www.python.org/downloads/)
2. Vink tijdens de installatie "Add Python to PATH" aan
3. Controleer de installatie:
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

### Stap 4: Stel Python-omgeving in

Het wordt aanbevolen om een virtuele omgeving te gebruiken om afhankelijkheden geïsoleerd te houden.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Stap 5: Installeer Python-pakketten

Installeer de benodigde data science-bibliotheken:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Stap 6: Installeer Node.js en npm (Voor Quiz App)

De quizapplicatie vereist Node.js en npm.

**Windows/macOS:**
- Download van [nodejs.org](https://nodejs.org/) (LTS-versie aanbevolen)
- Voer de installer uit

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

### Stap 7: Installeer Quiz App-afhankelijkheden

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Stap 8: Installeer Docsify (Optioneel)

Voor offline toegang tot documentatie:

```bash
npm install -g docsify-cli
```

## Controleer je Installatie

### Test Python en Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Je browser zou moeten openen met de Jupyter-interface. Je kunt nu navigeren naar een `.ipynb`-bestand van een les.

### Test Quiz Applicatie

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

De quizapplicatie zou beschikbaar moeten zijn op `http://localhost:8080` (of een andere poort als 8080 bezet is).

### Test Documentatieserver

```bash
# From the root directory of the repository
docsify serve
```

De documentatie zou beschikbaar moeten zijn op `http://localhost:3000`.

## Gebruik van VS Code Dev Containers

Als je Docker hebt geïnstalleerd, kun je VS Code Dev Containers gebruiken:

1. Installeer [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Installeer [Visual Studio Code](https://code.visualstudio.com/)
3. Installeer de [Remote - Containers extensie](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Open de repository in VS Code
5. Druk op `F1` en selecteer "Remote-Containers: Reopen in Container"
6. Wacht tot de container is gebouwd (alleen de eerste keer)

## Volgende Stappen

- Verken de [README.md](README.md) voor een overzicht van het curriculum
- Lees [USAGE.md](USAGE.md) voor veelvoorkomende workflows en voorbeelden
- Bekijk [TROUBLESHOOTING.md](TROUBLESHOOTING.md) als je problemen tegenkomt
- Bekijk [CONTRIBUTING.md](CONTRIBUTING.md) als je wilt bijdragen

## Hulp krijgen

Als je problemen ondervindt:

1. Bekijk de [TROUBLESHOOTING.md](TROUBLESHOOTING.md) gids
2. Zoek in bestaande [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Word lid van onze [Discord-community](https://aka.ms/ds4beginners/discord)
4. Maak een nieuw issue aan met gedetailleerde informatie over je probleem

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.