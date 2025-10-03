<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:23:43+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "tl"
}
-->
# Gabay sa Pag-install

Ang gabay na ito ay tutulong sa iyo na i-set up ang iyong environment para magamit ang kurikulum ng Data Science for Beginners.

## Talaan ng Nilalaman

- [Mga Kinakailangan](../..)
- [Mga Mabilisang Opsyon sa Pagsisimula](../..)
- [Lokal na Pag-install](../..)
- [I-verify ang Iyong Pag-install](../..)

## Mga Kinakailangan

Bago ka magsimula, dapat ay mayroon ka ng:

- Pangunahing kaalaman sa command line/terminal
- Isang GitHub account (libre)
- Matatag na koneksyon sa internet para sa paunang setup

## Mga Mabilisang Opsyon sa Pagsisimula

### Opsyon 1: GitHub Codespaces (Inirerekomenda para sa mga Baguhan)

Ang pinakamadaling paraan para magsimula ay sa GitHub Codespaces, na nagbibigay ng kumpletong development environment sa iyong browser.

1. Pumunta sa [repository](https://github.com/microsoft/Data-Science-For-Beginners)
2. I-click ang dropdown menu na **Code**
3. Piliin ang tab na **Codespaces**
4. I-click ang **Create codespace on main**
5. Maghintay para ma-initialize ang environment (2-3 minuto)

Handa na ang iyong environment na may lahat ng pre-installed na dependencies!

### Opsyon 2: Lokal na Pag-develop

Para magtrabaho sa iyong sariling computer, sundin ang detalyadong mga tagubilin sa ibaba.

## Lokal na Pag-install

### Hakbang 1: I-install ang Git

Kinakailangan ang Git para i-clone ang repository at subaybayan ang iyong mga pagbabago.

**Windows:**
- I-download mula sa [git-scm.com](https://git-scm.com/download/win)
- Patakbuhin ang installer gamit ang default na mga setting

**macOS:**
- I-install gamit ang Homebrew: `brew install git`
- O i-download mula sa [git-scm.com](https://git-scm.com/download/mac)

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

### Hakbang 2: I-clone ang Repository

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Hakbang 3: I-install ang Python at Jupyter

Kinakailangan ang Python 3.7 o mas mataas para sa mga aralin sa data science.

**Windows:**
1. I-download ang Python mula sa [python.org](https://www.python.org/downloads/)
2. Sa panahon ng pag-install, i-check ang "Add Python to PATH"
3. I-verify ang pag-install:
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

### Hakbang 4: I-set Up ang Python Environment

Inirerekomenda na gumamit ng virtual environment para panatilihing hiwalay ang mga dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Hakbang 5: I-install ang Python Packages

I-install ang kinakailangang mga library para sa data science:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Hakbang 6: I-install ang Node.js at npm (Para sa Quiz App)

Kinakailangan ng quiz application ang Node.js at npm.

**Windows/macOS:**
- I-download mula sa [nodejs.org](https://nodejs.org/) (LTS version ang inirerekomenda)
- Patakbuhin ang installer

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

### Hakbang 7: I-install ang Quiz App Dependencies

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Hakbang 8: I-install ang Docsify (Opsyonal)

Para sa offline na access sa dokumentasyon:

```bash
npm install -g docsify-cli
```

## I-verify ang Iyong Pag-install

### Subukan ang Python at Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Dapat magbukas ang iyong browser na may Jupyter interface. Maaari mo nang i-navigate ang anumang `.ipynb` file ng aralin.

### Subukan ang Quiz Application

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Dapat maging available ang quiz app sa `http://localhost:8080` (o ibang port kung busy ang 8080).

### Subukan ang Documentation Server

```bash
# From the root directory of the repository
docsify serve
```

Dapat maging available ang dokumentasyon sa `http://localhost:3000`.

## Paggamit ng VS Code Dev Containers

Kung mayroon kang naka-install na Docker, maaari mong gamitin ang VS Code Dev Containers:

1. I-install ang [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. I-install ang [Visual Studio Code](https://code.visualstudio.com/)
3. I-install ang [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Buksan ang repository sa VS Code
5. Pindutin ang `F1` at piliin ang "Remote-Containers: Reopen in Container"
6. Maghintay para ma-build ang container (sa unang pagkakataon lamang)

## Mga Susunod na Hakbang

- I-explore ang [README.md](README.md) para sa pangkalahatang ideya ng kurikulum
- Basahin ang [USAGE.md](USAGE.md) para sa mga karaniwang workflow at halimbawa
- Tingnan ang [TROUBLESHOOTING.md](TROUBLESHOOTING.md) kung makakaranas ng mga problema
- Suriin ang [CONTRIBUTING.md](CONTRIBUTING.md) kung nais mong mag-ambag

## Pagkuha ng Tulong

Kung makakaranas ng mga problema:

1. Tingnan ang gabay na [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Maghanap ng mga umiiral na [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Sumali sa aming [Discord community](https://aka.ms/ds4beginners/discord)
4. Gumawa ng bagong issue na may detalyadong impormasyon tungkol sa iyong problema

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.