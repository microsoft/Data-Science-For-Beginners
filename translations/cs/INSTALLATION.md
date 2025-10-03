<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:24:46+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "cs"
}
-->
# Průvodce instalací

Tento průvodce vám pomůže nastavit prostředí pro práci s učebními materiály Data Science for Beginners.

## Obsah

- [Předpoklady](../..)
- [Možnosti rychlého startu](../..)
- [Lokální instalace](../..)
- [Ověření instalace](../..)

## Předpoklady

Než začnete, měli byste mít:

- Základní znalosti práce s příkazovým řádkem/terminálem
- Účet na GitHubu (zdarma)
- Stabilní internetové připojení pro počáteční nastavení

## Možnosti rychlého startu

### Možnost 1: GitHub Codespaces (doporučeno pro začátečníky)

Nejjednodušší způsob, jak začít, je GitHub Codespaces, který poskytuje kompletní vývojové prostředí přímo ve vašem prohlížeči.

1. Přejděte na [repozitář](https://github.com/microsoft/Data-Science-For-Beginners)
2. Klikněte na rozbalovací nabídku **Code**
3. Vyberte záložku **Codespaces**
4. Klikněte na **Create codespace on main**
5. Počkejte, až se prostředí inicializuje (2-3 minuty)

Vaše prostředí je nyní připraveno se všemi předinstalovanými závislostmi!

### Možnost 2: Lokální vývoj

Pokud chcete pracovat na svém vlastním počítači, postupujte podle podrobných pokynů níže.

## Lokální instalace

### Krok 1: Instalace Git

Git je nutný pro klonování repozitáře a sledování vašich změn.

**Windows:**
- Stáhněte z [git-scm.com](https://git-scm.com/download/win)
- Spusťte instalátor s výchozím nastavením

**macOS:**
- Nainstalujte pomocí Homebrew: `brew install git`
- Nebo stáhněte z [git-scm.com](https://git-scm.com/download/mac)

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

### Krok 2: Klonování repozitáře

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Krok 3: Instalace Pythonu a Jupyteru

Pro lekce datové vědy je vyžadován Python 3.7 nebo vyšší.

**Windows:**
1. Stáhněte Python z [python.org](https://www.python.org/downloads/)
2. Během instalace zaškrtněte "Add Python to PATH"
3. Ověřte instalaci:
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

### Krok 4: Nastavení Python prostředí

Doporučuje se použít virtuální prostředí pro izolaci závislostí.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Krok 5: Instalace Python balíčků

Nainstalujte požadované knihovny pro datovou vědu:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Krok 6: Instalace Node.js a npm (pro aplikaci kvízu)

Aplikace kvízu vyžaduje Node.js a npm.

**Windows/macOS:**
- Stáhněte z [nodejs.org](https://nodejs.org/) (doporučena verze LTS)
- Spusťte instalátor

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

### Krok 7: Instalace závislostí aplikace kvízu

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Krok 8: Instalace Docsify (volitelné)

Pro offline přístup k dokumentaci:

```bash
npm install -g docsify-cli
```

## Ověření instalace

### Test Pythonu a Jupyteru

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Váš prohlížeč by se měl otevřít s rozhraním Jupyter. Nyní můžete přejít k jakémukoli souboru `.ipynb` v lekcích.

### Test aplikace kvízu

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Aplikace kvízu by měla být dostupná na `http://localhost:8080` (nebo na jiném portu, pokud je 8080 obsazen).

### Test serveru dokumentace

```bash
# From the root directory of the repository
docsify serve
```

Dokumentace by měla být dostupná na `http://localhost:3000`.

## Použití Dev Containers ve VS Code

Pokud máte nainstalovaný Docker, můžete použít Dev Containers ve VS Code:

1. Nainstalujte [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Nainstalujte [Visual Studio Code](https://code.visualstudio.com/)
3. Nainstalujte rozšíření [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Otevřete repozitář ve VS Code
5. Stiskněte `F1` a vyberte "Remote-Containers: Reopen in Container"
6. Počkejte, až se kontejner vytvoří (pouze při prvním spuštění)

## Další kroky

- Prozkoumejte [README.md](README.md) pro přehled učebních materiálů
- Přečtěte si [USAGE.md](USAGE.md) pro běžné pracovní postupy a příklady
- Zkontrolujte [TROUBLESHOOTING.md](TROUBLESHOOTING.md), pokud narazíte na problémy
- Projděte [CONTRIBUTING.md](CONTRIBUTING.md), pokud chcete přispět

## Získání pomoci

Pokud narazíte na problémy:

1. Zkontrolujte průvodce [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Vyhledejte existující [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Připojte se k naší [Discord komunitě](https://aka.ms/ds4beginners/discord)
4. Vytvořte nový issue s podrobnými informacemi o vašem problému

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.