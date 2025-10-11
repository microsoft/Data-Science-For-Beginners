<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-11T15:14:27+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "ta"
}
-->
# நிறுவல் வழிகாட்டி

இந்த வழிகாட்டி, Data Science for Beginners பாடத்திட்டத்துடன் வேலை செய்ய உங்கள் சூழலை அமைக்க உதவுகிறது.

## உள்ளடக்க அட்டவணை

- [முன் தேவைகள்](../..)
- [விரைவான தொடக்க விருப்பங்கள்](../..)
- [உள்ளூர் நிறுவல்](../..)
- [உங்கள் நிறுவலை சரிபார்க்கவும்](../..)

## முன் தேவைகள்

தொடங்குவதற்கு முன், உங்களிடம் இருக்க வேண்டும்:

- கட்டளைகள் வரிசை/டெர்மினல் பற்றிய அடிப்படை அறிவு
- GitHub கணக்கு (இலவசம்)
- ஆரம்ப அமைப்புக்கான நிலையான இணைய இணைப்பு

## விரைவான தொடக்க விருப்பங்கள்

### விருப்பம் 1: GitHub Codespaces (தொடக்கத்திற்கான பரிந்துரை)

தொடங்க எளிதான வழி GitHub Codespaces ஆகும், இது உங்களின் உலாவியில் முழுமையான மேம்பாட்டு சூழலை வழங்குகிறது.

1. [களஞ்சியத்திற்கு](https://github.com/microsoft/Data-Science-For-Beginners) செல்லவும்
2. **Code** மெனுவை கிளிக் செய்யவும்
3. **Codespaces** தாவலைத் தேர்ந்தெடுக்கவும்
4. **Create codespace on main** ஐ கிளிக் செய்யவும்
5. சூழல் ஆரம்பிக்க 2-3 நிமிடங்கள் காத்திருக்கவும்

உங்கள் சூழல் அனைத்து சார்புகளை முன்கூட்டியே நிறுவிய நிலையில் தயாராக உள்ளது!

### விருப்பம் 2: உள்ளூர் மேம்பாடு

உங்கள் சொந்த கணினியில் வேலை செய்ய, கீழே உள்ள விரிவான வழிமுறைகளை பின்பற்றவும்.

## உள்ளூர் நிறுவல்

### படி 1: Git ஐ நிறுவவும்

களஞ்சியத்தை கிளோன் செய்யவும், உங்கள் மாற்றங்களை கண்காணிக்கவும் Git தேவை.

**Windows:**
- [git-scm.com](https://git-scm.com/download/win) இல் இருந்து பதிவிறக்கவும்
- இயல்புநிலை அமைப்புகளுடன் நிறுவல் இயக்கவும்

**macOS:**
- Homebrew மூலம் நிறுவவும்: `brew install git`
- அல்லது [git-scm.com](https://git-scm.com/download/mac) இல் இருந்து பதிவிறக்கவும்

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

### படி 2: களஞ்சியத்தை கிளோன் செய்யவும்

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### படி 3: Python மற்றும் Jupyter ஐ நிறுவவும்

Python 3.7 அல்லது அதற்கு மேல் தரவியல் அறிவியல் பாடங்களுக்கு தேவை.

**Windows:**
1. [python.org](https://www.python.org/downloads/) இல் இருந்து Python ஐ பதிவிறக்கவும்
2. நிறுவலின் போது "Add Python to PATH" ஐ தேர்ந்தெடுக்கவும்
3. நிறுவலை சரிபார்க்கவும்:
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

### படி 4: Python சூழலை அமைக்கவும்

சார்புகளை தனித்துவமாக வைத்திருக்க ஒரு மெய்நிகர் சூழலை பயன்படுத்த பரிந்துரைக்கப்படுகிறது.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### படி 5: Python தொகுப்புகளை நிறுவவும்

தேவையான தரவியல் அறிவியல் நூலகங்களை நிறுவவும்:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### படி 6: Node.js மற்றும் npm ஐ நிறுவவும் (வினாடி வினா பயன்பாட்டிற்காக)

வினாடி வினா பயன்பாட்டிற்கு Node.js மற்றும் npm தேவை.

**Windows/macOS:**
- [nodejs.org](https://nodejs.org/) (LTS பதிப்பு பரிந்துரைக்கப்படுகிறது) இல் இருந்து பதிவிறக்கவும்
- நிறுவல் இயக்கவும்

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

### படி 7: வினாடி வினா பயன்பாட்டு சார்புகளை நிறுவவும்

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### படி 8: Docsify ஐ நிறுவவும் (விருப்பம்)

ஆஃப்லைன் ஆவண அணுகலுக்காக:

```bash
npm install -g docsify-cli
```

## உங்கள் நிறுவலை சரிபார்க்கவும்

### Python மற்றும் Jupyter ஐ சோதிக்கவும்

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

உங்கள் உலாவி Jupyter இடைமுகத்துடன் திறக்க வேண்டும். நீங்கள் எந்த பாடத்தின் `.ipynb` கோப்பிற்கும் செல்லலாம்.

### வினாடி வினா பயன்பாட்டை சோதிக்கவும்

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

வினாடி வினா பயன்பாடு `http://localhost:8080` (அல்லது 8080 பிஸியாக இருந்தால் மற்றொரு போர்ட்) இல் கிடைக்க வேண்டும்.

### ஆவண சேவையகத்தை சோதிக்கவும்

```bash
# From the root directory of the repository
docsify serve
```

ஆவணங்கள் `http://localhost:3000` இல் கிடைக்க வேண்டும்.

## VS Code Dev Containers ஐ பயன்படுத்துதல்

உங்களிடம் Docker நிறுவப்பட்டிருந்தால், நீங்கள் VS Code Dev Containers ஐ பயன்படுத்தலாம்:

1. [Docker Desktop](https://www.docker.com/products/docker-desktop) ஐ நிறுவவும்
2. [Visual Studio Code](https://code.visualstudio.com/) ஐ நிறுவவும்
3. [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) ஐ நிறுவவும்
4. களஞ்சியத்தை VS Code இல் திறக்கவும்
5. `F1` ஐ அழுத்தி "Remote-Containers: Reopen in Container" ஐ தேர்ந்தெடுக்கவும்
6. கெண்டைனர் உருவாக்க (முதல் முறை மட்டும்) காத்திருக்கவும்

## அடுத்த படிகள்

- பாடத்திட்டத்தின் மேற்பார்வைக்காக [README.md](README.md) ஐ ஆராயவும்
- பொதுவான வேலைகள் மற்றும் உதாரணங்களுக்காக [USAGE.md](USAGE.md) ஐ படிக்கவும்
- பிரச்சினைகள் ஏற்பட்டால் [TROUBLESHOOTING.md](TROUBLESHOOTING.md) ஐ சரிபார்க்கவும்
- பங்களிக்க விரும்பினால் [CONTRIBUTING.md](CONTRIBUTING.md) ஐ மதிப்பீடு செய்யவும்

## உதவி பெறுதல்

பிரச்சினைகள் ஏற்பட்டால்:

1. [TROUBLESHOOTING.md](TROUBLESHOOTING.md) வழிகாட்டியை சரிபார்க்கவும்
2. உள்ள [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) ஐ தேடவும்
3. எங்கள் [Discord community](https://aka.ms/ds4beginners/discord) இல் சேரவும்
4. உங்கள் பிரச்சினை பற்றிய விரிவான தகவலுடன் புதிய பிரச்சினையை உருவாக்கவும்

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.