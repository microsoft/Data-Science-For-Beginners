<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:22:04+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "fi"
}
-->
# Asennusopas

Tämä opas auttaa sinua ympäristön asennuksessa, jotta voit työskennellä Data Science for Beginners -opetussuunnitelman parissa.

## Sisällysluettelo

- [Edellytykset](../..)
- [Pikakäynnistysvaihtoehdot](../..)
- [Paikallinen asennus](../..)
- [Asennuksen tarkistaminen](../..)

## Edellytykset

Ennen kuin aloitat, sinulla tulisi olla:

- Perustiedot komentorivistä/terminaalista
- GitHub-tili (ilmainen)
- Vakaa internetyhteys alkuasennusta varten

## Pikakäynnistysvaihtoehdot

### Vaihtoehto 1: GitHub Codespaces (suositeltu aloittelijoille)

Helpoin tapa aloittaa on GitHub Codespaces, joka tarjoaa täydellisen kehitysympäristön suoraan selaimessasi.

1. Siirry [repositoryyn](https://github.com/microsoft/Data-Science-For-Beginners)
2. Klikkaa **Code**-pudotusvalikkoa
3. Valitse **Codespaces**-välilehti
4. Klikkaa **Create codespace on main**
5. Odota ympäristön alustamista (2-3 minuuttia)

Ympäristösi on nyt valmis, ja kaikki riippuvuudet on esiasennettu!

### Vaihtoehto 2: Paikallinen kehitys

Jos haluat työskennellä omalla tietokoneellasi, seuraa alla olevia yksityiskohtaisia ohjeita.

## Paikallinen asennus

### Vaihe 1: Asenna Git

Git vaaditaan repositoryn kloonaamiseen ja muutosten seuraamiseen.

**Windows:**
- Lataa [git-scm.com](https://git-scm.com/download/win)
- Suorita asennus oletusasetuksilla

**macOS:**
- Asenna Homebrew'n kautta: `brew install git`
- Tai lataa [git-scm.com](https://git-scm.com/download/mac)

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

### Vaihe 2: Kloonaa repository

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Vaihe 3: Asenna Python ja Jupyter

Python 3.7 tai uudempi vaaditaan data science -oppitunteihin.

**Windows:**
1. Lataa Python [python.org](https://www.python.org/downloads/)
2. Asennuksen aikana valitse "Add Python to PATH"
3. Vahvista asennus:
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

### Vaihe 4: Määritä Python-ympäristö

Suosittelemme käyttämään virtuaalista ympäristöä riippuvuuksien eristämiseksi.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Vaihe 5: Asenna Python-kirjastot

Asenna tarvittavat data science -kirjastot:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Vaihe 6: Asenna Node.js ja npm (Quiz-sovellusta varten)

Quiz-sovellus vaatii Node.js:n ja npm:n.

**Windows/macOS:**
- Lataa [nodejs.org](https://nodejs.org/) (suositellaan LTS-versiota)
- Suorita asennusohjelma

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

### Vaihe 7: Asenna Quiz-sovelluksen riippuvuudet

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Vaihe 8: Asenna Docsify (valinnainen)

Dokumentaation offline-käyttöä varten:

```bash
npm install -g docsify-cli
```

## Asennuksen tarkistaminen

### Testaa Python ja Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Selaimesi pitäisi avautua Jupyter-käyttöliittymällä. Voit nyt navigoida minkä tahansa oppitunnin `.ipynb`-tiedostoon.

### Testaa Quiz-sovellus

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Quiz-sovelluksen pitäisi olla saatavilla osoitteessa `http://localhost:8080` (tai toisessa portissa, jos 8080 on varattu).

### Testaa dokumentaatiopalvelin

```bash
# From the root directory of the repository
docsify serve
```

Dokumentaation pitäisi olla saatavilla osoitteessa `http://localhost:3000`.

## VS Code Dev Containers -käyttö

Jos sinulla on Docker asennettuna, voit käyttää VS Code Dev Containers -ominaisuutta:

1. Asenna [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Asenna [Visual Studio Code](https://code.visualstudio.com/)
3. Asenna [Remote - Containers -laajennus](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Avaa repository VS Codessa
5. Paina `F1` ja valitse "Remote-Containers: Reopen in Container"
6. Odota säiliön rakentamista (vain ensimmäisellä kerralla)

## Seuraavat askeleet

- Tutustu [README.md](README.md)-tiedostoon saadaksesi yleiskuvan opetussuunnitelmasta
- Lue [USAGE.md](USAGE.md) yleisiä työnkulkuja ja esimerkkejä varten
- Tarkista [TROUBLESHOOTING.md](TROUBLESHOOTING.md), jos kohtaat ongelmia
- Katso [CONTRIBUTING.md](CONTRIBUTING.md), jos haluat osallistua

## Avun saaminen

Jos kohtaat ongelmia:

1. Tarkista [TROUBLESHOOTING.md](TROUBLESHOOTING.md) -opas
2. Etsi olemassa olevia [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Liity [Discord-yhteisöömme](https://aka.ms/ds4beginners/discord)
4. Luo uusi issue, jossa kerrot yksityiskohtaisesti ongelmastasi

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.