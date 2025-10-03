<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:25:03+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "sk"
}
-->
# Inštalačný návod

Tento návod vám pomôže nastaviť prostredie na prácu s učebnými materiálmi Data Science for Beginners.

## Obsah

- [Predpoklady](../..)
- [Rýchle možnosti začiatku](../..)
- [Lokálna inštalácia](../..)
- [Overenie inštalácie](../..)

## Predpoklady

Predtým, než začnete, mali by ste mať:

- Základné znalosti práce s príkazovým riadkom/terminálom
- GitHub účet (bezplatný)
- Stabilné internetové pripojenie na počiatočné nastavenie

## Rýchle možnosti začiatku

### Možnosť 1: GitHub Codespaces (Odporúčané pre začiatočníkov)

Najjednoduchší spôsob, ako začať, je GitHub Codespaces, ktorý poskytuje kompletné vývojové prostredie priamo vo vašom prehliadači.

1. Prejdite na [repozitár](https://github.com/microsoft/Data-Science-For-Beginners)
2. Kliknite na rozbaľovacie menu **Code**
3. Vyberte kartu **Codespaces**
4. Kliknite na **Create codespace on main**
5. Počkajte, kým sa prostredie inicializuje (2-3 minúty)

Vaše prostredie je teraz pripravené so všetkými predinštalovanými závislosťami!

### Možnosť 2: Lokálny vývoj

Ak chcete pracovať na vlastnom počítači, postupujte podľa podrobných pokynov nižšie.

## Lokálna inštalácia

### Krok 1: Inštalácia Git

Git je potrebný na klonovanie repozitára a sledovanie vašich zmien.

**Windows:**
- Stiahnite z [git-scm.com](https://git-scm.com/download/win)
- Spustite inštalátor s predvolenými nastaveniami

**macOS:**
- Nainštalujte cez Homebrew: `brew install git`
- Alebo stiahnite z [git-scm.com](https://git-scm.com/download/mac)

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

### Krok 2: Klonovanie repozitára

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Krok 3: Inštalácia Pythonu a Jupyter

Pre lekcie z oblasti dátovej vedy je potrebný Python 3.7 alebo novší.

**Windows:**
1. Stiahnite Python z [python.org](https://www.python.org/downloads/)
2. Počas inštalácie zaškrtnite "Add Python to PATH"
3. Overte inštaláciu:
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

### Krok 4: Nastavenie Python prostredia

Odporúča sa používať virtuálne prostredie na izoláciu závislostí.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Krok 5: Inštalácia Python balíkov

Nainštalujte požadované knižnice pre dátovú vedu:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Krok 6: Inštalácia Node.js a npm (Pre aplikáciu kvízu)

Aplikácia kvízu vyžaduje Node.js a npm.

**Windows/macOS:**
- Stiahnite z [nodejs.org](https://nodejs.org/) (odporúča sa verzia LTS)
- Spustite inštalátor

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

### Krok 7: Inštalácia závislostí aplikácie kvízu

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Krok 8: Inštalácia Docsify (Voliteľné)

Pre offline prístup k dokumentácii:

```bash
npm install -g docsify-cli
```

## Overenie inštalácie

### Test Pythonu a Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Váš prehliadač by sa mal otvoriť s rozhraním Jupyter. Teraz môžete prejsť na akýkoľvek súbor `.ipynb` z lekcií.

### Test aplikácie kvízu

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Aplikácia kvízu by mala byť dostupná na `http://localhost:8080` (alebo na inom porte, ak je 8080 obsadený).

### Test servera dokumentácie

```bash
# From the root directory of the repository
docsify serve
```

Dokumentácia by mala byť dostupná na `http://localhost:3000`.

## Používanie VS Code Dev Containers

Ak máte nainštalovaný Docker, môžete použiť VS Code Dev Containers:

1. Nainštalujte [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Nainštalujte [Visual Studio Code](https://code.visualstudio.com/)
3. Nainštalujte rozšírenie [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Otvorte repozitár vo VS Code
5. Stlačte `F1` a vyberte "Remote-Containers: Reopen in Container"
6. Počkajte, kým sa kontajner vytvorí (iba pri prvom spustení)

## Ďalšie kroky

- Preskúmajte [README.md](README.md) pre prehľad učebných materiálov
- Prečítajte si [USAGE.md](USAGE.md) pre bežné pracovné postupy a príklady
- Skontrolujte [TROUBLESHOOTING.md](TROUBLESHOOTING.md), ak narazíte na problémy
- Preštudujte [CONTRIBUTING.md](CONTRIBUTING.md), ak chcete prispieť

## Získanie pomoci

Ak narazíte na problémy:

1. Skontrolujte návod [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Vyhľadajte existujúce [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Pripojte sa k našej [Discord komunite](https://aka.ms/ds4beginners/discord)
4. Vytvorte nový issue s podrobnými informáciami o vašom probléme

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.