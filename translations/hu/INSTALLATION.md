<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:24:22+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "hu"
}
-->
# Telepítési útmutató

Ez az útmutató segít beállítani a környezetet a Data Science for Beginners tananyag használatához.

## Tartalomjegyzék

- [Előfeltételek](../..)
- [Gyors kezdési lehetőségek](../..)
- [Helyi telepítés](../..)
- [Telepítés ellenőrzése](../..)

## Előfeltételek

Mielőtt elkezdené, szüksége lesz:

- Alapvető ismeretekre a parancssor/terminál használatában
- Egy GitHub fiókra (ingyenes)
- Stabil internetkapcsolatra a kezdeti beállításhoz

## Gyors kezdési lehetőségek

### Opció 1: GitHub Codespaces (Ajánlott kezdőknek)

A legegyszerűbb módja a kezdésnek a GitHub Codespaces használata, amely teljes fejlesztési környezetet biztosít a böngészőben.

1. Nyissa meg a [repository-t](https://github.com/microsoft/Data-Science-For-Beginners)
2. Kattintson a **Code** legördülő menüre
3. Válassza ki a **Codespaces** fület
4. Kattintson a **Create codespace on main** gombra
5. Várja meg, amíg a környezet inicializálódik (2-3 perc)

A környezete most készen áll, minden szükséges függőség előre telepítve van!

### Opció 2: Helyi fejlesztés

Ha saját számítógépen szeretne dolgozni, kövesse az alábbi részletes utasításokat.

## Helyi telepítés

### 1. lépés: Git telepítése

A Git szükséges a repository klónozásához és a változások nyomon követéséhez.

**Windows:**
- Töltse le innen: [git-scm.com](https://git-scm.com/download/win)
- Futtassa az telepítőt alapértelmezett beállításokkal

**macOS:**
- Telepítse Homebrew segítségével: `brew install git`
- Vagy töltse le innen: [git-scm.com](https://git-scm.com/download/mac)

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

### 2. lépés: Repository klónozása

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### 3. lépés: Python és Jupyter telepítése

A data science leckékhez Python 3.7 vagy újabb verzió szükséges.

**Windows:**
1. Töltse le a Pythont innen: [python.org](https://www.python.org/downloads/)
2. A telepítés során jelölje be az "Add Python to PATH" opciót
3. Ellenőrizze a telepítést:
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

### 4. lépés: Python környezet beállítása

Ajánlott virtuális környezetet használni a függőségek elkülönítéséhez.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 5. lépés: Python csomagok telepítése

Telepítse a szükséges data science könyvtárakat:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### 6. lépés: Node.js és npm telepítése (Kvíz alkalmazáshoz)

A kvíz alkalmazás Node.js-t és npm-et igényel.

**Windows/macOS:**
- Töltse le innen: [nodejs.org](https://nodejs.org/) (Ajánlott LTS verzió)
- Futtassa a telepítőt

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

### 7. lépés: Kvíz alkalmazás függőségeinek telepítése

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### 8. lépés: Docsify telepítése (Opcionális)

Offline dokumentáció eléréséhez:

```bash
npm install -g docsify-cli
```

## Telepítés ellenőrzése

### Python és Jupyter tesztelése

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

A böngészőnek meg kell nyílnia a Jupyter felülettel. Most navigálhat bármelyik lecke `.ipynb` fájljához.

### Kvíz alkalmazás tesztelése

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

A kvíz alkalmazásnak elérhetőnek kell lennie a `http://localhost:8080` címen (vagy más porton, ha a 8080 foglalt).

### Dokumentációs szerver tesztelése

```bash
# From the root directory of the repository
docsify serve
```

A dokumentációnak elérhetőnek kell lennie a `http://localhost:3000` címen.

## VS Code Dev Containers használata

Ha telepítve van a Docker, használhatja a VS Code Dev Containers funkciót:

1. Telepítse a [Docker Desktop](https://www.docker.com/products/docker-desktop) alkalmazást
2. Telepítse a [Visual Studio Code](https://code.visualstudio.com/) programot
3. Telepítse a [Remote - Containers kiegészítőt](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Nyissa meg a repository-t a VS Code-ban
5. Nyomja meg az `F1` gombot, és válassza a "Remote-Containers: Reopen in Container" opciót
6. Várja meg, amíg a konténer felépül (csak első alkalommal)

## Következő lépések

- Fedezze fel a [README.md](README.md) fájlt a tananyag áttekintéséhez
- Olvassa el a [USAGE.md](USAGE.md) fájlt a gyakori munkafolyamatok és példák megismeréséhez
- Nézze meg a [TROUBLESHOOTING.md](TROUBLESHOOTING.md) fájlt, ha problémákba ütközik
- Tekintse át a [CONTRIBUTING.md](CONTRIBUTING.md) fájlt, ha hozzájárulni szeretne

## Segítség kérése

Ha problémákba ütközik:

1. Nézze meg a [TROUBLESHOOTING.md](TROUBLESHOOTING.md) útmutatót
2. Keressen meglévő [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) között
3. Csatlakozzon a [Discord közösségünkhöz](https://aka.ms/ds4beginners/discord)
4. Hozzon létre egy új hibajelentést részletes információkkal a problémáról

---

**Felelősség kizárása**:  
Ezt a dokumentumot az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével fordították le. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.