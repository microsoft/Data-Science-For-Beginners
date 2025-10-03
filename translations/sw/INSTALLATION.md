<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:24:04+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "sw"
}
-->
# Mwongozo wa Ufungaji

Mwongozo huu utakusaidia kuandaa mazingira yako ili kufanya kazi na mtaala wa Data Science kwa Kompyuta.

## Jedwali la Maudhui

- [Mahitaji ya Awali](../..)
- [Chaguo za Kuanza Haraka](../..)
- [Ufungaji wa Kwenye Kompyuta](../..)
- [Thibitisha Ufungaji Wako](../..)

## Mahitaji ya Awali

Kabla ya kuanza, unapaswa kuwa na:

- Uelewa wa msingi wa mstari wa amri/terminal
- Akaunti ya GitHub (bure)
- Muunganisho wa intaneti thabiti kwa usanidi wa awali

## Chaguo za Kuanza Haraka

### Chaguo 1: GitHub Codespaces (Inapendekezwa kwa Kompyuta)

Njia rahisi zaidi ya kuanza ni kutumia GitHub Codespaces, ambayo hutoa mazingira kamili ya maendeleo kwenye kivinjari chako.

1. Tembelea [repo](https://github.com/microsoft/Data-Science-For-Beginners)
2. Bonyeza menyu ya kushuka ya **Code**
3. Chagua kichupo cha **Codespaces**
4. Bonyeza **Create codespace on main**
5. Subiri mazingira yaanze (dakika 2-3)

Mazingira yako sasa yako tayari na utegemezi wote umewekwa!

### Chaguo 2: Maendeleo ya Kwenye Kompyuta

Kwa kufanya kazi kwenye kompyuta yako mwenyewe, fuata maelekezo ya kina hapa chini.

## Ufungaji wa Kwenye Kompyuta

### Hatua ya 1: Weka Git

Git inahitajika ili kunakili repo na kufuatilia mabadiliko yako.

**Windows:**
- Pakua kutoka [git-scm.com](https://git-scm.com/download/win)
- Endesha kisakinishi na mipangilio ya chaguo-msingi

**macOS:**
- Weka kupitia Homebrew: `brew install git`
- Au pakua kutoka [git-scm.com](https://git-scm.com/download/mac)

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

### Hatua ya 2: Nakili Repo

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Hatua ya 3: Weka Python na Jupyter

Python 3.7 au zaidi inahitajika kwa masomo ya data science.

**Windows:**
1. Pakua Python kutoka [python.org](https://www.python.org/downloads/)
2. Wakati wa usakinishaji, angalia "Add Python to PATH"
3. Thibitisha usakinishaji:
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

### Hatua ya 4: Sanidi Mazingira ya Python

Inapendekezwa kutumia mazingira ya kawaida ili kuweka utegemezi tofauti.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Hatua ya 5: Weka Maktaba za Python

Weka maktaba zinazohitajika za data science:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Hatua ya 6: Weka Node.js na npm (Kwa Programu ya Maswali)

Programu ya maswali inahitaji Node.js na npm.

**Windows/macOS:**
- Pakua kutoka [nodejs.org](https://nodejs.org/) (toleo la LTS linapendekezwa)
- Endesha kisakinishi

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

### Hatua ya 7: Weka Utegemezi wa Programu ya Maswali

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Hatua ya 8: Weka Docsify (Hiari)

Kwa ufikiaji wa nje ya mtandao wa nyaraka:

```bash
npm install -g docsify-cli
```

## Thibitisha Ufungaji Wako

### Jaribu Python na Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Kivinjari chako kinapaswa kufunguka na kiolesura cha Jupyter. Sasa unaweza kuvinjari faili yoyote ya `.ipynb` ya somo.

### Jaribu Programu ya Maswali

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Programu ya maswali inapaswa kupatikana kwenye `http://localhost:8080` (au bandari nyingine ikiwa 8080 imejaa).

### Jaribu Seva ya Nyaraka

```bash
# From the root directory of the repository
docsify serve
```

Nyaraka zinapaswa kupatikana kwenye `http://localhost:3000`.

## Kutumia Kontena za Maendeleo za VS Code

Ikiwa una Docker imewekwa, unaweza kutumia Kontena za Maendeleo za VS Code:

1. Weka [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Weka [Visual Studio Code](https://code.visualstudio.com/)
3. Weka kiendelezi cha [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Fungua repo kwenye VS Code
5. Bonyeza `F1` na uchague "Remote-Containers: Reopen in Container"
6. Subiri kontena lijengwe (mara ya kwanza tu)

## Hatua Zifuatazo

- Chunguza [README.md](README.md) kwa muhtasari wa mtaala
- Soma [USAGE.md](USAGE.md) kwa mifumo ya kazi ya kawaida na mifano
- Angalia [TROUBLESHOOTING.md](TROUBLESHOOTING.md) ikiwa unakutana na matatizo
- Kagua [CONTRIBUTING.md](CONTRIBUTING.md) ikiwa unataka kuchangia

## Kupata Msaada

Ikiwa unakutana na matatizo:

1. Angalia mwongozo wa [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Tafuta [Masuala ya GitHub](https://github.com/microsoft/Data-Science-For-Beginners/issues) yaliyopo
3. Jiunge na [Jamii ya Discord](https://aka.ms/ds4beginners/discord)
4. Unda suala jipya na maelezo ya kina kuhusu tatizo lako

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.