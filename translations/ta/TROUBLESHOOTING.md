<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-11T15:15:08+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "ta"
}
-->
# பிரச்சினைகளை தீர்க்கும் வழிகாட்டி

இந்த வழிகாட்டி, Data Science for Beginners பாடத்திட்டத்துடன் வேலை செய்யும்போது நீங்கள் சந்திக்கக்கூடிய பொதுவான பிரச்சினைகளுக்கு தீர்வுகளை வழங்குகிறது.

## உள்ளடக்க அட்டவணை

- [Python மற்றும் Jupyter பிரச்சினைகள்](../..)
- [பேக்கேஜ் மற்றும் சார்பு பிரச்சினைகள்](../..)
- [Jupyter Notebook பிரச்சினைகள்](../..)
- [வினாடி வினா பயன்பாட்டு பிரச்சினைகள்](../..)
- [Git மற்றும் GitHub பிரச்சினைகள்](../..)
- [Docsify ஆவண பிரச்சினைகள்](../..)
- [தரவு மற்றும் கோப்பு பிரச்சினைகள்](../..)
- [செயல்திறன் பிரச்சினைகள்](../..)
- [கூடுதல் உதவி பெறுதல்](../..)

## Python மற்றும் Jupyter பிரச்சினைகள்

### Python கிடைக்கவில்லை அல்லது தவறான பதிப்பு

**பிரச்சினை:** `python: command not found` அல்லது Python பதிப்பு தவறாக உள்ளது

**தீர்வு:**

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

**Windows தீர்வு:**
1. [python.org](https://www.python.org/) இல் இருந்து Python ஐ மீண்டும் நிறுவவும்
2. நிறுவும் போது "Add Python to PATH" என்பதை தேர்வு செய்யவும்
3. உங்கள் டெர்மினல்/கமாண்டு ப்ராம்ப்ட்டை மீண்டும் தொடங்கவும்

### மெய்நிகர் சூழல் செயல்படுத்தல் பிரச்சினைகள்

**பிரச்சினை:** மெய்நிகர் சூழல் செயல்படவில்லை

**தீர்வு:**

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

**செயல்படுத்தல் சரிபார்க்கவும்:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter Kernel பிரச்சினைகள்

**பிரச்சினை:** "Kernel not found" அல்லது "Kernel keeps dying"

**தீர்வு:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**பிரச்சினை:** Jupyter இல் Python பதிப்பு தவறாக உள்ளது

**தீர்வு:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## பேக்கேஜ் மற்றும் சார்பு பிரச்சினைகள்

### இறக்குமதி பிழைகள்

**பிரச்சினை:** `ModuleNotFoundError: No module named 'pandas'` (அல்லது பிற பேக்கேஜ்கள்)

**தீர்வு:**

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

### Pip நிறுவல் தோல்விகள்

**பிரச்சினை:** `pip install` அனுமதி பிழைகளுடன் தோல்வியடைகிறது

**தீர்வு:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**பிரச்சினை:** `pip install` SSL சான்றிதழ் பிழைகளுடன் தோல்வியடைகிறது

**தீர்வு:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### பேக்கேஜ் பதிப்பு முரண்பாடுகள்

**பிரச்சினை:** பொருந்தாத பேக்கேஜ் பதிப்புகள்

**தீர்வு:**

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

## Jupyter Notebook பிரச்சினைகள்

### Jupyter தொடங்கவில்லை

**பிரச்சினை:** `jupyter notebook` கமாண்டு கிடைக்கவில்லை

**தீர்வு:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook ஏற்றப்படவில்லை அல்லது சேமிக்கப்படவில்லை

**பிரச்சினை:** "Notebook failed to load" அல்லது சேமிப்பு பிழைகள்

**தீர்வு:**

1. கோப்பு அனுமதிகளை சரிபார்க்கவும்
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. கோப்பு சேதத்தை சரிபார்க்கவும்
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Jupyter கேஷை அழிக்கவும்
```bash
jupyter notebook --clear-cache
```

### செல் செயல்படவில்லை

**பிரச்சினை:** "In [*]" இல் செல் சிக்கியுள்ளது அல்லது மிகவும் நீண்ட நேரம் எடுக்கிறது

**தீர்வு:**

1. **Kernel ஐ தடை செய்யவும்:** "Interrupt" பொத்தானை கிளிக் செய்யவும் அல்லது `I, I` அழுத்தவும்
2. **Kernel ஐ மீண்டும் தொடங்கவும்:** Kernel மெனு → Restart
3. **உங்கள் குறியீட்டில் முடிவில்லாத மடல்களை** சரிபார்க்கவும்
4. **வெளியீட்டை அழிக்கவும்:** Cell → All Output → Clear

### வரைபடங்கள் காட்டப்படவில்லை

**பிரச்சினை:** `matplotlib` வரைபடங்கள் Notebook இல் காட்டப்படவில்லை

**தீர்வு:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**இயங்கும் வரைபடங்களுக்கு மாற்று:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## வினாடி வினா பயன்பாட்டு பிரச்சினைகள்

### npm install தோல்வியடைகிறது

**பிரச்சினை:** `npm install` போது பிழைகள்

**தீர்வு:**

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

### வினாடி வினா பயன்பாடு தொடங்கவில்லை

**பிரச்சினை:** `npm run serve` தோல்வியடைகிறது

**தீர்வு:**

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

### போர்ட் ஏற்கனவே பயன்படுத்தப்படுகிறது

**பிரச்சினை:** "Port 8080 is already in use"

**தீர்வு:**

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

### வினாடி வினா ஏற்றப்படவில்லை அல்லது வெற்று பக்கம்

**பிரச்சினை:** வினாடி வினா பயன்பாடு ஏற்றுகிறது ஆனால் வெற்று பக்கம் காட்டுகிறது

**தீர்வு:**

1. உலாவி கன்சோலில் பிழைகளை சரிபார்க்கவும் (F12)
2. உலாவி கேஷ் மற்றும் குக்கீகளை அழிக்கவும்
3. வேறு உலாவியை முயற்சிக்கவும்
4. JavaScript இயங்குகிறது என்பதை உறுதிப்படுத்தவும்
5. விளம்பர தடுப்பிகள் தடை செய்யும் என்பதை சரிபார்க்கவும்

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git மற்றும் GitHub பிரச்சினைகள்

### Git அடையாளம் காணப்படவில்லை

**பிரச்சினை:** `git: command not found`

**தீர்வு:**

**Windows:**
- [git-scm.com](https://git-scm.com/) இல் இருந்து Git ஐ நிறுவவும்
- நிறுவலுக்குப் பிறகு டெர்மினலை மீண்டும் தொடங்கவும்

**macOS:**

> **குறிப்பு:** Homebrew நிறுவப்படவில்லை என்றால், முதலில் [https://brew.sh/](https://brew.sh/) இல் உள்ள வழிகாட்டுதல்களைப் பின்பற்றி அதை நிறுவவும்.
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

### Clone தோல்வியடைகிறது

**பிரச்சினை:** `git clone` அங்கீகார பிழைகளுடன் தோல்வியடைகிறது

**தீர்வு:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### அனுமதி மறுக்கப்பட்டது (publickey)

**பிரச்சினை:** SSH கீ அங்கீகாரம் தோல்வியடைகிறது

**தீர்வு:**

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

## Docsify ஆவண பிரச்சினைகள்

### Docsify கமாண்டு கிடைக்கவில்லை

**பிரச்சினை:** `docsify: command not found`

**தீர்வு:**

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

### ஆவணங்கள் ஏற்றப்படவில்லை

**பிரச்சினை:** Docsify சேவை செய்கிறது ஆனால் உள்ளடக்கம் ஏற்றப்படவில்லை

**தீர்வு:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### படங்கள் காட்டப்படவில்லை

**பிரச்சினை:** படங்கள் உடைந்த இணைச்சொற்கள் ஐகானை காட்டுகிறது

**தீர்வு:**

1. பட பாதைகள் தொடர்புடையவை என்பதை சரிபார்க்கவும்
2. பட கோப்புகள் களஞ்சியத்தில் உள்ளன என்பதை உறுதிப்படுத்தவும்
3. உலாவி கேஷை அழிக்கவும்
4. கோப்பு நீட்டிப்புகள் பொருந்துகின்றன என்பதை உறுதிப்படுத்தவும் (சில அமைப்புகளில் கேஸ்-சென்சிடிவ்)

## தரவு மற்றும் கோப்பு பிரச்சினைகள்

### கோப்பு கிடைக்கவில்லை பிழைகள்

**பிரச்சினை:** `FileNotFoundError` தரவை ஏற்றும்போது

**தீர்வு:**

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

### CSV வாசிப்பு பிழைகள்

**பிரச்சினை:** CSV கோப்புகளை வாசிக்கும் போது பிழைகள்

**தீர்வு:**

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

### பெரிய தரவுத்தொகுப்புகளுடன் நினைவக பிழைகள்

**பிரச்சினை:** `MemoryError` பெரிய கோப்புகளை ஏற்றும்போது

**தீர்வு:**

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

## செயல்திறன் பிரச்சினைகள்

### Notebook செயல்திறன் மந்தமாக உள்ளது

**பிரச்சினை:** Notebook கள் மிகவும் மந்தமாக இயங்குகிறது

**தீர்வு:**

1. **Kernel ஐ மீண்டும் தொடங்கவும் மற்றும் வெளியீட்டை அழிக்கவும்**
   - Kernel → Restart & Clear Output

2. **பயன்படுத்தப்படாத Notebook களை மூடவும்**

3. **குறியீட்டை மேம்படுத்தவும்:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **பெரிய தரவுத்தொகுப்புகளை மாதிரி எடுக்கவும்:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### உலாவி சிக்கல்கள்

**பிரச்சினை:** உலாவி சிக்கலாகிறது அல்லது பதிலளிக்கவில்லை

**தீர்வு:**

1. பயன்படுத்தப்படாத தாவல்கள் மூடவும்
2. உலாவி கேஷை அழிக்கவும்
3. உலாவி நினைவகத்தை அதிகரிக்கவும் (Chrome: `chrome://settings/system`)
4. JupyterLab ஐ பயன்படுத்தவும்:
```bash
pip install jupyterlab
jupyter lab
```

## கூடுதல் உதவி பெறுதல்

### உதவி கேட்பதற்கு முன்

1. இந்த பிரச்சினைகளை தீர்க்கும் வழிகாட்டியை சரிபார்க்கவும்
2. [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) தேடவும்
3. [INSTALLATION.md](INSTALLATION.md) மற்றும் [USAGE.md](USAGE.md) ஐ மதிப்பாய்வு செய்யவும்
4. பிழை செய்தியை ஆன்லைனில் தேட முயற்சிக்கவும்

### உதவி கேட்பது எப்படி

ஒரு பிரச்சினையை உருவாக்கும்போது அல்லது உதவி கேட்கும்போது, பின்வருவனவற்றை சேர்க்கவும்:

1. **இயங்கும் அமைப்பு:** Windows, macOS, அல்லது Linux (எந்த விநியோகம்)
2. **Python பதிப்பு:** `python --version` ஐ இயக்கவும்
3. **பிழை செய்தி:** முழுமையான பிழை செய்தியை நகலெடுக்கவும்
4. **மீண்டும் உருவாக்கும் படிகள்:** பிழை ஏற்படும் முன் நீங்கள் செய்தது
5. **நீங்கள் முயற்சித்தது:** நீங்கள் ஏற்கனவே முயற்சித்த தீர்வுகள்

**உதாரணம்:**
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

### சமூக வளங்கள்

- **GitHub Issues:** [ஒரு பிரச்சினையை உருவாக்கவும்](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord:** [எங்கள் சமூகத்தில் சேரவும்](https://aka.ms/ds4beginners/discord)
- **Discussions:** [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn:** [Q&A Forums](https://docs.microsoft.com/answers/)

### தொடர்புடைய ஆவணங்கள்

- [INSTALLATION.md](INSTALLATION.md) - அமைப்பு வழிகாட்டுதல்
- [USAGE.md](USAGE.md) - பாடத்திட்டத்தை எப்படி பயன்படுத்துவது
- [CONTRIBUTING.md](CONTRIBUTING.md) - பங்களிக்க எப்படி
- [README.md](README.md) - திட்டத்தின் மேற்பார்வை

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாகக் கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.