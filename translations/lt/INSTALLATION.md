<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:27:49+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "lt"
}
-->
# Diegimo vadovas

Šis vadovas padės jums paruošti aplinką darbui su pradedančiųjų duomenų mokslo mokymo programa.

## Turinys

- [Būtinos sąlygos](../..)
- [Greito starto parinktys](../..)
- [Vietinis diegimas](../..)
- [Patikrinkite diegimą](../..)

## Būtinos sąlygos

Prieš pradėdami, turėtumėte:

- Turėti pagrindines žinias apie komandų eilutę/terminalą
- Turėti GitHub paskyrą (nemokamą)
- Stabilų interneto ryšį pradiniam nustatymui

## Greito starto parinktys

### Parinktis 1: GitHub Codespaces (Rekomenduojama pradedantiesiems)

Lengviausias būdas pradėti yra naudoti GitHub Codespaces, kuris suteikia pilną kūrimo aplinką jūsų naršyklėje.

1. Eikite į [saugyklą](https://github.com/microsoft/Data-Science-For-Beginners)
2. Spustelėkite **Code** išskleidžiamąjį meniu
3. Pasirinkite **Codespaces** skirtuką
4. Spustelėkite **Create codespace on main**
5. Palaukite, kol aplinka bus inicializuota (2-3 minutės)

Jūsų aplinka paruošta su visomis iš anksto įdiegtomis priklausomybėmis!

### Parinktis 2: Vietinis kūrimas

Norėdami dirbti savo kompiuteryje, vadovaukitės išsamiais nurodymais žemiau.

## Vietinis diegimas

### 1 žingsnis: Įdiekite Git

Git reikalingas saugyklos klonavimui ir pakeitimų sekimui.

**Windows:**
- Atsisiųskite iš [git-scm.com](https://git-scm.com/download/win)
- Paleiskite diegimo programą su numatytaisiais nustatymais

**macOS:**
- Įdiekite per Homebrew: `brew install git`
- Arba atsisiųskite iš [git-scm.com](https://git-scm.com/download/mac)

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

### 2 žingsnis: Klonuokite saugyklą

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### 3 žingsnis: Įdiekite Python ir Jupyter

Duomenų mokslo pamokoms reikalinga Python 3.7 ar naujesnė versija.

**Windows:**
1. Atsisiųskite Python iš [python.org](https://www.python.org/downloads/)
2. Diegimo metu pažymėkite "Add Python to PATH"
3. Patikrinkite diegimą:
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

### 4 žingsnis: Sukurkite Python aplinką

Rekomenduojama naudoti virtualią aplinką, kad priklausomybės būtų izoliuotos.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 5 žingsnis: Įdiekite Python bibliotekas

Įdiekite reikalingas duomenų mokslo bibliotekas:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### 6 žingsnis: Įdiekite Node.js ir npm (skirta viktorinos programai)

Viktorinos programai reikalingi Node.js ir npm.

**Windows/macOS:**
- Atsisiųskite iš [nodejs.org](https://nodejs.org/) (rekomenduojama LTS versija)
- Paleiskite diegimo programą

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

### 7 žingsnis: Įdiekite viktorinos programos priklausomybes

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### 8 žingsnis: Įdiekite Docsify (nebūtina)

Norėdami turėti dokumentaciją neprisijungus:

```bash
npm install -g docsify-cli
```

## Patikrinkite diegimą

### Testuokite Python ir Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Jūsų naršyklė turėtų atsidaryti su Jupyter sąsaja. Dabar galite naršyti bet kurį pamokos `.ipynb` failą.

### Testuokite viktorinos programą

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Viktorinos programa turėtų būti pasiekiama adresu `http://localhost:8080` (arba kitu portu, jei 8080 užimtas).

### Testuokite dokumentacijos serverį

```bash
# From the root directory of the repository
docsify serve
```

Dokumentacija turėtų būti pasiekiama adresu `http://localhost:3000`.

## VS Code Dev Containers naudojimas

Jei turite įdiegtą Docker, galite naudoti VS Code Dev Containers:

1. Įdiekite [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Įdiekite [Visual Studio Code](https://code.visualstudio.com/)
3. Įdiekite [Remote - Containers plėtinį](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Atidarykite saugyklą VS Code
5. Paspauskite `F1` ir pasirinkite "Remote-Containers: Reopen in Container"
6. Palaukite, kol konteineris bus sukurtas (tik pirmą kartą)

## Tolimesni žingsniai

- Peržiūrėkite [README.md](README.md) norėdami susipažinti su mokymo programa
- Perskaitykite [USAGE.md](USAGE.md) apie dažniausiai naudojamus darbo procesus ir pavyzdžius
- Patikrinkite [TROUBLESHOOTING.md](TROUBLESHOOTING.md), jei susiduriate su problemomis
- Peržiūrėkite [CONTRIBUTING.md](CONTRIBUTING.md), jei norite prisidėti

## Pagalbos gavimas

Jei susiduriate su problemomis:

1. Patikrinkite [TROUBLESHOOTING.md](TROUBLESHOOTING.md) vadovą
2. Ieškokite esamų [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Prisijunkite prie mūsų [Discord bendruomenės](https://aka.ms/ds4beginners/discord)
4. Sukurkite naują problemą su išsamia informacija apie jūsų situaciją

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, atsiradusius dėl šio vertimo naudojimo.