<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:42:07+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "fi"
}
-->
# Vianmääritysopas

Tämä opas tarjoaa ratkaisuja yleisiin ongelmiin, joita saatat kohdata työskennellessäsi Data Science for Beginners -opetussuunnitelman parissa.

## Sisällysluettelo

- [Python- ja Jupyter-ongelmat](../..)
- [Paketit ja riippuvuudet](../..)
- [Jupyter Notebook -ongelmat](../..)
- [Tietovisa-sovelluksen ongelmat](../..)
- [Git- ja GitHub-ongelmat](../..)
- [Docsify-dokumentaatio-ongelmat](../..)
- [Data- ja tiedosto-ongelmat](../..)
- [Suorituskykyongelmat](../..)
- [Lisäavun saaminen](../..)

## Python- ja Jupyter-ongelmat

### Pythonia ei löydy tai väärä versio

**Ongelma:** `python: command not found` tai väärä Python-versio

**Ratkaisu:**

```bash
# Check Python version
python --version
python3 --version

# If Python 3 is installed as 'python3', create an alias
# On macOS/Linux, add to ~/.bashrc or ~/.zshrc:
alias python=python3
alias pip=pip3

# Or use python3 explicitly
python3 -m pip install jupyter
```

**Windows-ratkaisu:**
1. Asenna Python uudelleen [python.org](https://www.python.org/) -sivustolta
2. Asennuksen aikana valitse "Add Python to PATH"
3. Käynnistä terminaali/komentokehote uudelleen

### Virtuaaliympäristön aktivointiongelmat

**Ongelma:** Virtuaaliympäristö ei aktivoidu

**Ratkaisu:**

**Windows:**
```bash
# If you get execution policy error
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
venv\Scripts\activate
```

**macOS/Linux:**
```bash
# Ensure the activate script is executable
chmod +x venv/bin/activate

# Then activate
source venv/bin/activate
```

**Varmista aktivointi:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter-ytimen ongelmat

**Ongelma:** "Kernel not found" tai "Kernel keeps dying"

**Ratkaisu:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Ongelma:** Väärä Python-versio Jupyterissä

**Ratkaisu:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Paketit ja riippuvuudet

### Tuontivirheet

**Ongelma:** `ModuleNotFoundError: No module named 'pandas'` (tai muita paketteja)

**Ratkaisu:**

```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install missing package
pip install pandas

# Install all common packages
pip install jupyter pandas numpy matplotlib seaborn scikit-learn

# Verify installation
python -c "import pandas; print(pandas.__version__)"
```

### Pip-asennusvirheet

**Ongelma:** `pip install` epäonnistuu käyttöoikeusvirheiden vuoksi

**Ratkaisu:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Ongelma:** `pip install` epäonnistuu SSL-varmennevirheiden vuoksi

**Ratkaisu:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Pakettiversioiden ristiriidat

**Ongelma:** Yhteensopimattomat pakettiversiot

**Ratkaisu:**

```bash
# Create fresh virtual environment
python -m venv venv-new
source venv-new/bin/activate  # or venv-new\Scripts\activate on Windows

# Install packages with specific versions if needed
pip install pandas==1.3.0
pip install numpy==1.21.0

# Or let pip resolve dependencies
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

## Jupyter Notebook -ongelmat

### Jupyter ei käynnisty

**Ongelma:** `jupyter notebook` -komentoa ei löydy

**Ratkaisu:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook ei lataudu tai tallennu

**Ongelma:** "Notebook failed to load" tai tallennusvirheet

**Ratkaisu:**

1. Tarkista tiedoston käyttöoikeudet
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Tarkista tiedoston korruptio
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Tyhjennä Jupyterin välimuisti
```bash
jupyter notebook --clear-cache
```

### Solu ei suoriteta

**Ongelma:** Solu jumissa tilassa "In [*]" tai kestää ikuisuuden

**Ratkaisu:**

1. **Keskeytä ydin**: Klikkaa "Interrupt"-painiketta tai paina `I, I`
2. **Käynnistä ydin uudelleen**: Kernel-valikko → Restart
3. **Tarkista koodin äärettömät silmukat**
4. **Tyhjennä tulosteet**: Cell → All Output → Clear

### Kuviot eivät näy

**Ongelma:** `matplotlib`-kuviot eivät näy notebookissa

**Ratkaisu:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Vaihtoehto interaktiivisille kuvioille:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Tietovisa-sovelluksen ongelmat

### npm install epäonnistuu

**Ongelma:** Virheitä `npm install` -komennon aikana

**Ratkaisu:**

```bash
# Clear npm cache
npm cache clean --force

# Remove node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Reinstall
npm install

# If still failing, try with legacy peer deps
npm install --legacy-peer-deps
```

### Tietovisa-sovellus ei käynnisty

**Ongelma:** `npm run serve` epäonnistuu

**Ratkaisu:**

```bash
# Check Node.js version
node --version  # Should be 12.x or higher

# Reinstall dependencies
cd quiz-app
rm -rf node_modules package-lock.json
npm install

# Try different port
npm run serve -- --port 8081
```

### Portti jo käytössä

**Ongelma:** "Port 8080 is already in use"

**Ratkaisu:**

```bash
# Find and kill process on port 8080
# macOS/Linux:
lsof -ti:8080 | xargs kill -9

# Windows:
netstat -ano | findstr :8080
taskkill /PID <PID> /F

# Or use a different port
npm run serve -- --port 8081
```

### Tietovisa ei lataudu tai näyttää tyhjän sivun

**Ongelma:** Tietovisa-sovellus latautuu mutta näyttää tyhjän sivun

**Ratkaisu:**

1. Tarkista selaimen konsoli virheiden varalta (F12)
2. Tyhjennä selaimen välimuisti ja evästeet
3. Kokeile toista selainta
4. Varmista, että JavaScript on käytössä
5. Tarkista, häiritsevätkö mainosten estäjät

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git- ja GitHub-ongelmat

### Git ei tunnisteta

**Ongelma:** `git: command not found`

**Ratkaisu:**

**Windows:**
- Asenna Git [git-scm.com](https://git-scm.com/) -sivustolta
- Käynnistä terminaali uudelleen asennuksen jälkeen

**macOS:**

> **Huom:** Jos sinulla ei ole Homebrew'ta asennettuna, seuraa ohjeita [https://brew.sh/](https://brew.sh/) -sivustolla sen asentamiseksi.
```bash
# Install via Homebrew
brew install git

# Or install Xcode Command Line Tools
xcode-select --install
```

**Linux:**
```bash
sudo apt-get install git  # Debian/Ubuntu
sudo dnf install git      # Fedora
```

### Kloonaus epäonnistuu

**Ongelma:** `git clone` epäonnistuu todennusvirheiden vuoksi

**Ratkaisu:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Käyttö estetty (publickey)

**Ongelma:** SSH-avaimen todennus epäonnistuu

**Ratkaisu:**

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add key to ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Add public key to GitHub
# Copy key: cat ~/.ssh/id_ed25519.pub
# Add at: https://github.com/settings/keys
```

## Docsify-dokumentaatio-ongelmat

### Docsify-komentoa ei löydy

**Ongelma:** `docsify: command not found`

**Ratkaisu:**

```bash
# Install globally
npm install -g docsify-cli

# If permission error on macOS/Linux
sudo npm install -g docsify-cli

# Verify installation
docsify --version

# If still not found, add npm global path
# Find npm global path
npm config get prefix

# Add to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH="$PATH:/usr/local/bin"
```

### Dokumentaatio ei lataudu

**Ongelma:** Docsify toimii, mutta sisältö ei lataudu

**Ratkaisu:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Kuvat eivät näy

**Ongelma:** Kuvat näyttävät rikkinäisen linkin kuvakkeen

**Ratkaisu:**

1. Tarkista, että kuvapolut ovat suhteellisia
2. Varmista, että kuvatiedostot ovat olemassa repositoriossa
3. Tyhjennä selaimen välimuisti
4. Varmista, että tiedostopäätteet täsmäävät (kirjainkokoherkkä joillakin järjestelmillä)

## Data- ja tiedosto-ongelmat

### Tiedostoa ei löydy -virheet

**Ongelma:** `FileNotFoundError` datan lataamisen yhteydessä

**Ratkaisu:**

```python
import os

# Check current working directory
print(os.getcwd())

# Use absolute path
data_path = os.path.join(os.getcwd(), 'data', 'filename.csv')
df = pd.read_csv(data_path)

# Or use relative path from notebook location
df = pd.read_csv('../data/filename.csv')

# Verify file exists
print(os.path.exists('data/filename.csv'))
```

### CSV-lukemisvirheet

**Ongelma:** Virheitä CSV-tiedostojen lukemisessa

**Ratkaisu:**

```python
import pandas as pd

# Try different encodings
df = pd.read_csv('file.csv', encoding='utf-8')
# or
df = pd.read_csv('file.csv', encoding='latin-1')
# or
df = pd.read_csv('file.csv', encoding='ISO-8859-1')

# Handle missing values
df = pd.read_csv('file.csv', na_values=['NA', 'N/A', ''])

# Specify delimiter if not comma
df = pd.read_csv('file.csv', delimiter=';')
```

### Muistivirheet suurten tietoaineistojen kanssa

**Ongelma:** `MemoryError` suurten tiedostojen lataamisen yhteydessä

**Ratkaisu:**

```python
# Read in chunks
chunk_size = 10000
chunks = []
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # Process chunk
    chunks.append(chunk)
df = pd.concat(chunks)

# Or read specific columns only
df = pd.read_csv('file.csv', usecols=['col1', 'col2'])

# Use more efficient data types
df = pd.read_csv('file.csv', dtype={'column_name': 'int32'})
```

## Suorituskykyongelmat

### Notebookin hidas suorituskyky

**Ongelma:** Notebookit toimivat erittäin hitaasti

**Ratkaisu:**

1. **Käynnistä ydin uudelleen ja tyhjennä tulosteet**
   - Kernel → Restart & Clear Output

2. **Sulje käyttämättömät notebookit**

3. **Optimoi koodi:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Ota näytteitä suurista tietoaineistoista:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Selaimen kaatuminen

**Ongelma:** Selain kaatuu tai muuttuu vastaamattomaksi

**Ratkaisu:**

1. Sulje käyttämättömät välilehdet
2. Tyhjennä selaimen välimuisti
3. Lisää selaimen muistia (Chrome: `chrome://settings/system`)
4. Käytä JupyterLabia:
```bash
pip install jupyterlab
jupyter lab
```

## Lisäavun saaminen

### Ennen avun pyytämistä

1. Tarkista tämä vianmääritysopas
2. Etsi [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) -sivustolta
3. Lue [INSTALLATION.md](INSTALLATION.md) ja [USAGE.md](USAGE.md)
4. Kokeile etsiä virheilmoitusta verkosta

### Kuinka pyytää apua

Kun luot ongelmaraportin tai pyydät apua, sisällytä:

1. **Käyttöjärjestelmä**: Windows, macOS tai Linux (mikä jakelu)
2. **Python-versio**: Suorita `python --version`
3. **Virheilmoitus**: Kopioi täydellinen virheilmoitus
4. **Toistettavat vaiheet**: Mitä teit ennen virheen ilmenemistä
5. **Mitä olet kokeillut**: Ratkaisut, joita olet jo yrittänyt

**Esimerkki:**
```
**Operating System:** macOS 12.0
**Python Version:** 3.9.7
**Error Message:** ModuleNotFoundError: No module named 'pandas'
**Steps to Reproduce:**
1. Activated virtual environment
2. Started Jupyter notebook
3. Tried to import pandas

**What I've Tried:**
- Ran pip install pandas
- Restarted Jupyter
```

### Yhteisön resurssit

- **GitHub Issues**: [Luo ongelmaraportti](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Liity yhteisöömme](https://aka.ms/ds4beginners/discord)
- **Keskustelut**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Q&A-foorumit](https://docs.microsoft.com/answers/)

### Liittyvä dokumentaatio

- [INSTALLATION.md](INSTALLATION.md) - Asennusohjeet
- [USAGE.md](USAGE.md) - Opetussuunnitelman käyttöohjeet
- [CONTRIBUTING.md](CONTRIBUTING.md) - Kuinka osallistua
- [README.md](README.md) - Projektin yleiskatsaus

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.