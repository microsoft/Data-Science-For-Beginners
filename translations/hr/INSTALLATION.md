<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:26:19+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "hr"
}
-->
# Vodič za instalaciju

Ovaj vodič pomoći će vam da postavite svoje okruženje za rad s kurikulumom "Data Science for Beginners".

## Sadržaj

- [Preduvjeti](../..)
- [Opcije brzog početka](../..)
- [Lokalna instalacija](../..)
- [Provjera instalacije](../..)

## Preduvjeti

Prije nego što započnete, trebali biste imati:

- Osnovno poznavanje naredbenog retka/terminala
- GitHub račun (besplatan)
- Stabilnu internetsku vezu za početnu postavku

## Opcije brzog početka

### Opcija 1: GitHub Codespaces (Preporučeno za početnike)

Najlakši način za početak je korištenje GitHub Codespaces, koji pruža potpuno razvojno okruženje u vašem pregledniku.

1. Idite na [repozitorij](https://github.com/microsoft/Data-Science-For-Beginners)
2. Kliknite na padajući izbornik **Code**
3. Odaberite karticu **Codespaces**
4. Kliknite **Create codespace on main**
5. Pričekajte da se okruženje inicijalizira (2-3 minute)

Vaše okruženje sada je spremno sa svim unaprijed instaliranim ovisnostima!

### Opcija 2: Lokalni razvoj

Za rad na vlastitom računalu slijedite detaljne upute u nastavku.

## Lokalna instalacija

### Korak 1: Instalirajte Git

Git je potreban za kloniranje repozitorija i praćenje vaših promjena.

**Windows:**
- Preuzmite s [git-scm.com](https://git-scm.com/download/win)
- Pokrenite instalacijski program s zadanim postavkama

**macOS:**
- Instalirajte putem Homebrew-a: `brew install git`
- Ili preuzmite s [git-scm.com](https://git-scm.com/download/mac)

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

### Korak 3: Instalirajte Python i Jupyter

Python 3.7 ili noviji potreban je za lekcije o znanosti o podacima.

**Windows:**
1. Preuzmite Python s [python.org](https://www.python.org/downloads/)
2. Tijekom instalacije označite "Add Python to PATH"
3. Provjerite instalaciju:
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

### Korak 4: Postavite Python okruženje

Preporučuje se korištenje virtualnog okruženja za izolaciju ovisnosti.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Korak 5: Instalirajte Python pakete

Instalirajte potrebne biblioteke za znanost o podacima:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Korak 6: Instalirajte Node.js i npm (za aplikaciju kviza)

Aplikacija kviza zahtijeva Node.js i npm.

**Windows/macOS:**
- Preuzmite s [nodejs.org](https://nodejs.org/) (preporučuje se LTS verzija)
- Pokrenite instalacijski program

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

### Korak 7: Instalirajte ovisnosti aplikacije kviza

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Korak 8: Instalirajte Docsify (Opcionalno)

Za offline pristup dokumentaciji:

```bash
npm install -g docsify-cli
```

## Provjera instalacije

### Testirajte Python i Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Vaš preglednik trebao bi se otvoriti s Jupyter sučeljem. Sada možete navigirati do bilo koje `.ipynb` datoteke lekcije.

### Testirajte aplikaciju kviza

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Aplikacija kviza trebala bi biti dostupna na `http://localhost:8080` (ili na drugom portu ako je 8080 zauzet).

### Testirajte poslužitelj dokumentacije

```bash
# From the root directory of the repository
docsify serve
```

Dokumentacija bi trebala biti dostupna na `http://localhost:3000`.

## Korištenje VS Code Dev Containers

Ako imate instaliran Docker, možete koristiti VS Code Dev Containers:

1. Instalirajte [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Instalirajte [Visual Studio Code](https://code.visualstudio.com/)
3. Instalirajte ekstenziju [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Otvorite repozitorij u VS Code-u
5. Pritisnite `F1` i odaberite "Remote-Containers: Reopen in Container"
6. Pričekajte da se kontejner izgradi (samo prvi put)

## Sljedeći koraci

- Istražite [README.md](README.md) za pregled kurikuluma
- Pročitajte [USAGE.md](USAGE.md) za uobičajene radne procese i primjere
- Provjerite [TROUBLESHOOTING.md](TROUBLESHOOTING.md) ako naiđete na probleme
- Pregledajte [CONTRIBUTING.md](CONTRIBUTING.md) ako želite doprinijeti

## Dobivanje pomoći

Ako naiđete na probleme:

1. Provjerite vodič [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Pretražite postojeće [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Pridružite se našoj [Discord zajednici](https://aka.ms/ds4beginners/discord)
4. Kreirajte novi problem s detaljnim informacijama o vašem problemu

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.