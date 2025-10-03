<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:26:36+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "sl"
}
-->
# Vodnik za namestitev

Ta vodnik vam bo pomagal nastaviti okolje za delo s kurikulumom "Data Science for Beginners".

## Kazalo

- [Predpogoji](../..)
- [Hitre možnosti za začetek](../..)
- [Lokalna namestitev](../..)
- [Preverite svojo namestitev](../..)

## Predpogoji

Preden začnete, morate imeti:

- Osnovno poznavanje ukazne vrstice/terminala
- GitHub račun (brezplačen)
- Stabilno internetno povezavo za začetno nastavitev

## Hitre možnosti za začetek

### Možnost 1: GitHub Codespaces (Priporočeno za začetnike)

Najlažji način za začetek je z GitHub Codespaces, ki omogoča popolno razvojno okolje v vašem brskalniku.

1. Obiščite [repozitorij](https://github.com/microsoft/Data-Science-For-Beginners)
2. Kliknite spustni meni **Code**
3. Izberite zavihek **Codespaces**
4. Kliknite **Create codespace on main**
5. Počakajte, da se okolje inicializira (2-3 minute)

Vaše okolje je zdaj pripravljeno z vsemi predhodno nameščenimi odvisnostmi!

### Možnost 2: Lokalni razvoj

Če želite delati na svojem računalniku, sledite podrobnim navodilom spodaj.

## Lokalna namestitev

### Korak 1: Namestite Git

Git je potreben za kloniranje repozitorija in sledenje vašim spremembam.

**Windows:**
- Prenesite z [git-scm.com](https://git-scm.com/download/win)
- Zaženite namestitveni program z privzetimi nastavitvami

**macOS:**
- Namestite prek Homebrew: `brew install git`
- Ali prenesite z [git-scm.com](https://git-scm.com/download/mac)

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

### Korak 2: Klonirajte repozitorij

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Korak 3: Namestite Python in Jupyter

Za lekcije o podatkovni znanosti je potreben Python 3.7 ali novejši.

**Windows:**
1. Prenesite Python z [python.org](https://www.python.org/downloads/)
2. Med namestitvijo označite "Add Python to PATH"
3. Preverite namestitev:
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

### Korak 4: Nastavite Python okolje

Priporočljivo je uporabljati virtualno okolje za izolacijo odvisnosti.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Korak 5: Namestite Python pakete

Namestite potrebne knjižnice za podatkovno znanost:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Korak 6: Namestite Node.js in npm (Za aplikacijo kvizov)

Aplikacija za kvize zahteva Node.js in npm.

**Windows/macOS:**
- Prenesite z [nodejs.org](https://nodejs.org/) (priporočena LTS različica)
- Zaženite namestitveni program

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

### Korak 7: Namestite odvisnosti aplikacije kvizov

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Korak 8: Namestite Docsify (Neobvezno)

Za dostop do dokumentacije brez povezave:

```bash
npm install -g docsify-cli
```

## Preverite svojo namestitev

### Testirajte Python in Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Vaš brskalnik bi se moral odpreti z vmesnikom Jupyter. Zdaj lahko dostopate do katere koli lekcije `.ipynb` datoteke.

### Testirajte aplikacijo kvizov

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Aplikacija za kvize bi morala biti dostopna na `http://localhost:8080` (ali drugem portu, če je 8080 zaseden).

### Testirajte strežnik dokumentacije

```bash
# From the root directory of the repository
docsify serve
```

Dokumentacija bi morala biti dostopna na `http://localhost:3000`.

## Uporaba VS Code Dev Containers

Če imate nameščen Docker, lahko uporabite VS Code Dev Containers:

1. Namestite [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Namestite [Visual Studio Code](https://code.visualstudio.com/)
3. Namestite razširitev [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Odprite repozitorij v VS Code
5. Pritisnite `F1` in izberite "Remote-Containers: Reopen in Container"
6. Počakajte, da se kontejner zgradi (samo prvič)

## Naslednji koraki

- Raziščite [README.md](README.md) za pregled kurikuluma
- Preberite [USAGE.md](USAGE.md) za pogoste delovne tokove in primere
- Preverite [TROUBLESHOOTING.md](TROUBLESHOOTING.md), če naletite na težave
- Preglejte [CONTRIBUTING.md](CONTRIBUTING.md), če želite prispevati

## Pomoč

Če naletite na težave:

1. Preverite vodnik [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Poiščite obstoječe [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Pridružite se naši [Discord skupnosti](https://aka.ms/ds4beginners/discord)
4. Ustvarite novo težavo z natančnimi informacijami o vašem problemu

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.