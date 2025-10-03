<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:21:18+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "sv"
}
-->
# Installationsguide

Den här guiden hjälper dig att ställa in din miljö för att arbeta med Data Science for Beginners-kursen.

## Innehållsförteckning

- [Förutsättningar](../..)
- [Snabbstartsalternativ](../..)
- [Lokal installation](../..)
- [Verifiera din installation](../..)

## Förutsättningar

Innan du börjar bör du ha:

- Grundläggande kunskaper om kommandoraden/terminalen
- Ett GitHub-konto (gratis)
- Stabil internetanslutning för den första installationen

## Snabbstartsalternativ

### Alternativ 1: GitHub Codespaces (Rekommenderas för nybörjare)

Det enklaste sättet att komma igång är med GitHub Codespaces, som erbjuder en komplett utvecklingsmiljö direkt i din webbläsare.

1. Gå till [repositoryt](https://github.com/microsoft/Data-Science-For-Beginners)
2. Klicka på **Code**-menyn
3. Välj fliken **Codespaces**
4. Klicka på **Create codespace on main**
5. Vänta tills miljön har initierats (2-3 minuter)

Din miljö är nu redo med alla beroenden förinstallerade!

### Alternativ 2: Lokal utveckling

För att arbeta på din egen dator, följ de detaljerade instruktionerna nedan.

## Lokal installation

### Steg 1: Installera Git

Git krävs för att klona repositoryt och spåra dina ändringar.

**Windows:**
- Ladda ner från [git-scm.com](https://git-scm.com/download/win)
- Kör installationsprogrammet med standardinställningar

**macOS:**
- Installera via Homebrew: `brew install git`
- Eller ladda ner från [git-scm.com](https://git-scm.com/download/mac)

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

### Steg 2: Klona repositoryt

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Steg 3: Installera Python och Jupyter

Python 3.7 eller högre krävs för data science-lektionerna.

**Windows:**
1. Ladda ner Python från [python.org](https://www.python.org/downloads/)
2. Under installationen, kryssa i "Add Python to PATH"
3. Verifiera installationen:
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

### Steg 4: Ställ in Python-miljö

Det rekommenderas att använda en virtuell miljö för att hålla beroenden isolerade.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Steg 5: Installera Python-paket

Installera de nödvändiga data science-biblioteken:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Steg 6: Installera Node.js och npm (För quiz-appen)

Quiz-applikationen kräver Node.js och npm.

**Windows/macOS:**
- Ladda ner från [nodejs.org](https://nodejs.org/) (LTS-versionen rekommenderas)
- Kör installationsprogrammet

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

### Steg 7: Installera beroenden för quiz-appen

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Steg 8: Installera Docsify (Valfritt)

För offlineåtkomst till dokumentationen:

```bash
npm install -g docsify-cli
```

## Verifiera din installation

### Testa Python och Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Din webbläsare bör öppnas med Jupyter-gränssnittet. Du kan nu navigera till valfri lektions `.ipynb`-fil.

### Testa quiz-applikationen

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Quiz-appen bör vara tillgänglig på `http://localhost:8080` (eller en annan port om 8080 är upptagen).

### Testa dokumentationsservern

```bash
# From the root directory of the repository
docsify serve
```

Dokumentationen bör vara tillgänglig på `http://localhost:3000`.

## Använda VS Code Dev Containers

Om du har Docker installerat kan du använda VS Code Dev Containers:

1. Installera [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Installera [Visual Studio Code](https://code.visualstudio.com/)
3. Installera [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Öppna repositoryt i VS Code
5. Tryck på `F1` och välj "Remote-Containers: Reopen in Container"
6. Vänta tills containern byggs (endast första gången)

## Nästa steg

- Utforska [README.md](README.md) för en översikt av kursen
- Läs [USAGE.md](USAGE.md) för vanliga arbetsflöden och exempel
- Kontrollera [TROUBLESHOOTING.md](TROUBLESHOOTING.md) om du stöter på problem
- Granska [CONTRIBUTING.md](CONTRIBUTING.md) om du vill bidra

## Få hjälp

Om du stöter på problem:

1. Kontrollera [TROUBLESHOOTING.md](TROUBLESHOOTING.md)-guiden
2. Sök bland befintliga [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Gå med i vår [Discord-community](https://aka.ms/ds4beginners/discord)
4. Skapa ett nytt ärende med detaljerad information om ditt problem

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.