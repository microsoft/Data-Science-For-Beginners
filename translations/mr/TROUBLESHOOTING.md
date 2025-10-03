<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:35:58+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "mr"
}
-->
# समस्या निराकरण मार्गदर्शक

ही मार्गदर्शिका डेटा सायन्स फॉर बिगिनर्स अभ्यासक्रमाशी संबंधित सामान्य समस्यांचे निराकरण प्रदान करते.

## विषय सूची

- [Python आणि Jupyter समस्या](../..)
- [पॅकेज आणि अवलंबित्व समस्या](../..)
- [Jupyter Notebook समस्या](../..)
- [क्विझ अॅप्लिकेशन समस्या](../..)
- [Git आणि GitHub समस्या](../..)
- [Docsify दस्तऐवजीकरण समस्या](../..)
- [डेटा आणि फाइल समस्या](../..)
- [कामगिरी समस्या](../..)
- [अतिरिक्त मदत मिळवणे](../..)

## Python आणि Jupyter समस्या

### Python सापडत नाही किंवा चुकीचा आवृत्ती

**समस्या:** `python: command not found` किंवा चुकीची Python आवृत्ती

**निराकरण:**

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

**Windows निराकरण:**
1. [python.org](https://www.python.org/) वरून Python पुन्हा स्थापित करा
2. स्थापना दरम्यान, "Add Python to PATH" निवडा
3. तुमचा टर्मिनल/कमांड प्रॉम्प्ट पुन्हा सुरू करा

### व्हर्च्युअल एन्व्हायर्नमेंट सक्रिय करण्याच्या समस्या

**समस्या:** व्हर्च्युअल एन्व्हायर्नमेंट सक्रिय होत नाही

**निराकरण:**

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

**सक्रियता सत्यापित करा:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter कर्नल समस्या

**समस्या:** "Kernel not found" किंवा "Kernel keeps dying"

**निराकरण:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**समस्या:** Jupyter मध्ये चुकीची Python आवृत्ती

**निराकरण:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## पॅकेज आणि अवलंबित्व समस्या

### आयात त्रुटी

**समस्या:** `ModuleNotFoundError: No module named 'pandas'` (किंवा इतर पॅकेजेस)

**निराकरण:**

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

### Pip स्थापना अयशस्वी

**समस्या:** `pip install` परवानगी त्रुटींसह अयशस्वी

**निराकरण:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**समस्या:** `pip install` SSL प्रमाणपत्र त्रुटींसह अयशस्वी

**निराकरण:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### पॅकेज आवृत्ती संघर्ष

**समस्या:** असुसंगत पॅकेज आवृत्त्या

**निराकरण:**

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

## Jupyter Notebook समस्या

### Jupyter सुरू होत नाही

**समस्या:** `jupyter notebook` कमांड सापडत नाही

**निराकरण:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### नोटबुक लोड होत नाही किंवा सेव्ह होत नाही

**समस्या:** "Notebook failed to load" किंवा सेव्ह त्रुटी

**निराकरण:**

1. फाइल परवानग्या तपासा
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. फाइल भ्रष्टाचार तपासा
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Jupyter कॅशे साफ करा
```bash
jupyter notebook --clear-cache
```

### सेल कार्यान्वित होत नाही

**समस्या:** सेल "In [*]" वर अडकले आहे किंवा खूप वेळ घेत आहे

**निराकरण:**

1. **कर्नल थांबवा:** "Interrupt" बटण क्लिक करा किंवा `I, I` दाबा
2. **कर्नल पुन्हा सुरू करा:** कर्नल मेनू → Restart
3. **कोडमधील अमर्यादित लूप्स तपासा**
4. **आउटपुट साफ करा:** Cell → All Output → Clear

### प्लॉट्स दिसत नाहीत

**समस्या:** `matplotlib` प्लॉट्स नोटबुकमध्ये दिसत नाहीत

**निराकरण:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**परस्परसंवादी प्लॉट्ससाठी पर्याय:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## क्विझ अॅप्लिकेशन समस्या

### npm install अयशस्वी

**समस्या:** `npm install` दरम्यान त्रुटी

**निराकरण:**

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

### क्विझ अॅप सुरू होत नाही

**समस्या:** `npm run serve` अयशस्वी

**निराकरण:**

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

### पोर्ट आधीच वापरात आहे

**समस्या:** "Port 8080 is already in use"

**निराकरण:**

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

### क्विझ लोड होत नाही किंवा रिकामी पृष्ठ

**समस्या:** क्विझ अॅप लोड होते पण रिकामी पृष्ठ दाखवते

**निराकरण:**

1. ब्राउझर कन्सोलमध्ये त्रुटी तपासा (F12)
2. ब्राउझर कॅशे आणि कुकीज साफ करा
3. वेगळा ब्राउझर वापरून पहा
4. JavaScript सक्षम असल्याची खात्री करा
5. अॅड ब्लॉकर्स हस्तक्षेप करत असल्यास तपासा

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git आणि GitHub समस्या

### Git ओळखले जात नाही

**समस्या:** `git: command not found`

**निराकरण:**

**Windows:**
- [git-scm.com](https://git-scm.com/) वरून Git स्थापित करा
- स्थापना नंतर टर्मिनल पुन्हा सुरू करा

**macOS:**

> **टीप:** जर तुमच्याकडे Homebrew स्थापित नसेल, तर [https://brew.sh/](https://brew.sh/) येथे दिलेल्या सूचनांचे अनुसरण करा.
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

### Clone अयशस्वी

**समस्या:** `git clone` प्रमाणीकरण त्रुटींसह अयशस्वी

**निराकरण:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### परवानगी नाकारली (publickey)

**समस्या:** SSH की प्रमाणीकरण अयशस्वी

**निराकरण:**

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

## Docsify दस्तऐवजीकरण समस्या

### Docsify कमांड सापडत नाही

**समस्या:** `docsify: command not found`

**निराकरण:**

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

### दस्तऐवज लोड होत नाही

**समस्या:** Docsify सर्व्ह करतो पण सामग्री लोड होत नाही

**निराकरण:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### प्रतिमा दिसत नाहीत

**समस्या:** प्रतिमा तुटलेल्या लिंक आयकॉन दाखवतात

**निराकरण:**

1. प्रतिमा पथ सापेक्ष आहेत याची खात्री करा
2. प्रतिमा फाइल्स रेपॉझिटरीमध्ये अस्तित्वात आहेत याची खात्री करा
3. ब्राउझर कॅशे साफ करा
4. फाइल एक्स्टेंशन्स जुळत असल्याची खात्री करा (काही सिस्टमवर केस-संवेदनशील)

## डेटा आणि फाइल समस्या

### फाइल सापडत नाही त्रुटी

**समस्या:** डेटा लोड करताना `FileNotFoundError`

**निराकरण:**

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

### CSV वाचन त्रुटी

**समस्या:** CSV फाइल्स वाचताना त्रुटी

**निराकरण:**

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

### मोठ्या डेटासेट्ससह मेमरी त्रुटी

**समस्या:** मोठ्या फाइल्स लोड करताना `MemoryError`

**निराकरण:**

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

## कामगिरी समस्या

### नोटबुकची कामगिरी मंद आहे

**समस्या:** नोटबुक खूप मंद चालते

**निराकरण:**

1. **कर्नल पुन्हा सुरू करा आणि आउटपुट साफ करा**
   - Kernel → Restart & Clear Output

2. **न वापरलेली नोटबुक्स बंद करा**

3. **कोड ऑप्टिमाइझ करा:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **मोठ्या डेटासेट्सचे नमुने घ्या:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### ब्राउझर क्रॅश होते

**समस्या:** ब्राउझर क्रॅश होते किंवा प्रतिसाद देत नाही

**निराकरण:**

1. न वापरलेले टॅब्स बंद करा
2. ब्राउझर कॅशे साफ करा
3. ब्राउझर मेमरी वाढवा (Chrome: `chrome://settings/system`)
4. JupyterLab वापरा:
```bash
pip install jupyterlab
jupyter lab
```

## अतिरिक्त मदत मिळवणे

### मदत मागण्यापूर्वी

1. ही समस्या निराकरण मार्गदर्शिका तपासा
2. [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) शोधा
3. [INSTALLATION.md](INSTALLATION.md) आणि [USAGE.md](USAGE.md) पुनरावलोकन करा
4. त्रुटी संदेश ऑनलाइन शोधण्याचा प्रयत्न करा

### मदत कशी मागावी

जर तुम्ही समस्या तयार करत असाल किंवा मदत मागत असाल, तर खालील माहिती समाविष्ट करा:

1. **ऑपरेटिंग सिस्टम**: Windows, macOS, किंवा Linux (कोणते वितरण)
2. **Python आवृत्ती**: `python --version` चालवा
3. **त्रुटी संदेश**: संपूर्ण त्रुटी संदेश कॉपी करा
4. **पुनरुत्पादनाचे चरण**: त्रुटी होण्यापूर्वी तुम्ही काय केले
5. **तुम्ही काय प्रयत्न केले आहे**: तुम्ही आधीच प्रयत्न केलेली निराकरणे

**उदाहरण:**
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

### समुदाय संसाधने

- **GitHub Issues**: [समस्या तयार करा](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [आमच्या समुदायात सामील व्हा](https://aka.ms/ds4beginners/discord)
- **चर्चा**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Q&A फोरम्स](https://docs.microsoft.com/answers/)

### संबंधित दस्तऐवजीकरण

- [INSTALLATION.md](INSTALLATION.md) - सेटअप सूचना
- [USAGE.md](USAGE.md) - अभ्यासक्रम कसा वापरायचा
- [CONTRIBUTING.md](CONTRIBUTING.md) - योगदान कसे करावे
- [README.md](README.md) - प्रकल्पाचा आढावा

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.