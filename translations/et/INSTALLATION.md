<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-11T15:14:44+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "et"
}
-->
# Paigaldusjuhend

See juhend aitab teil seadistada oma keskkonda, et töötada algajatele mõeldud andmeteaduse õppekavaga.

## Sisukord

- [Eeltingimused](../..)
- [Kiire alustamise valikud](../..)
- [Kohalik paigaldus](../..)
- [Paigalduse kontrollimine](../..)

## Eeltingimused

Enne alustamist peaks teil olema:

- Põhiline tuttavus käsurea/terminaliga
- GitHubi konto (tasuta)
- Stabiilne internetiühendus esialgseks seadistamiseks

## Kiire alustamise valikud

### Valik 1: GitHub Codespaces (soovitatav algajatele)

Lihtsaim viis alustamiseks on GitHub Codespaces, mis pakub täielikku arenduskeskkonda otse teie brauseris.

1. Minge [repositooriumisse](https://github.com/microsoft/Data-Science-For-Beginners)
2. Klõpsake **Code** rippmenüüd
3. Valige **Codespaces** vahekaart
4. Klõpsake **Create codespace on main**
5. Oodake, kuni keskkond initsialiseeritakse (2-3 minutit)

Teie keskkond on nüüd valmis koos kõigi eelinstallitud sõltuvustega!

### Valik 2: Kohalik arendus

Kui soovite töötada oma arvutis, järgige allolevaid üksikasjalikke juhiseid.

## Kohalik paigaldus

### Samm 1: Paigaldage Git

Git on vajalik repositooriumi kloonimiseks ja muudatuste jälgimiseks.

**Windows:**
- Laadige alla [git-scm.com](https://git-scm.com/download/win)
- Käivitage paigaldaja vaikeseadetega

**macOS:**
- Paigaldage Homebrew abil: `brew install git`
- Või laadige alla [git-scm.com](https://git-scm.com/download/mac)

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

### Samm 2: Kloonige repositoorium

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Samm 3: Paigaldage Python ja Jupyter

Andmeteaduse tundide jaoks on vajalik Python 3.7 või uuem.

**Windows:**
1. Laadige Python alla [python.org](https://www.python.org/downloads/)
2. Paigaldamise ajal märkige "Add Python to PATH"
3. Kontrollige paigaldust:
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

### Samm 4: Seadistage Pythoni keskkond

Soovitatav on kasutada virtuaalset keskkonda, et hoida sõltuvused eraldatud.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Samm 5: Paigaldage Pythoni paketid

Paigaldage vajalikud andmeteaduse teegid:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Samm 6: Paigaldage Node.js ja npm (viktoriinirakenduse jaoks)

Viktoriinirakendus vajab Node.js-i ja npm-i.

**Windows/macOS:**
- Laadige alla [nodejs.org](https://nodejs.org/) (soovitatav LTS versioon)
- Käivitage paigaldaja

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

### Samm 7: Paigaldage viktoriinirakenduse sõltuvused

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Samm 8: Paigaldage Docsify (valikuline)

Dokumentatsiooni võrguühenduseta kasutamiseks:

```bash
npm install -g docsify-cli
```

## Paigalduse kontrollimine

### Testige Pythonit ja Jupyterit

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Teie brauser peaks avanema Jupyteri liidesega. Nüüd saate liikuda mis tahes tunni `.ipynb` failini.

### Testige viktoriinirakendust

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Viktoriinirakendus peaks olema saadaval aadressil `http://localhost:8080` (või mõnel muul pordil, kui 8080 on hõivatud).

### Testige dokumentatsiooniserverit

```bash
# From the root directory of the repository
docsify serve
```

Dokumentatsioon peaks olema saadaval aadressil `http://localhost:3000`.

## VS Code Dev Containers kasutamine

Kui teil on Docker paigaldatud, saate kasutada VS Code Dev Containers:

1. Paigaldage [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Paigaldage [Visual Studio Code](https://code.visualstudio.com/)
3. Paigaldage [Remote - Containers laiendus](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Avage repositoorium VS Code'is
5. Vajutage `F1` ja valige "Remote-Containers: Reopen in Container"
6. Oodake, kuni konteiner ehitatakse (ainult esimesel korral)

## Järgmised sammud

- Uurige [README.md](README.md), et saada ülevaade õppekavast
- Lugege [USAGE.md](USAGE.md), et tutvuda tavapäraste töövoogude ja näidetega
- Kontrollige [TROUBLESHOOTING.md](TROUBLESHOOTING.md), kui teil tekib probleeme
- Vaadake [CONTRIBUTING.md](CONTRIBUTING.md), kui soovite panustada

## Abi saamine

Kui teil tekib probleeme:

1. Kontrollige [TROUBLESHOOTING.md](TROUBLESHOOTING.md) juhendit
2. Otsige olemasolevaid [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Liituge meie [Discordi kogukonnaga](https://aka.ms/ds4beginners/discord)
4. Looge uus probleem koos üksikasjaliku teabega oma probleemi kohta

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokumenti selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.