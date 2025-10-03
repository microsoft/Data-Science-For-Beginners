<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:34:45+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "hi"
}
-->
# समस्या निवारण गाइड

यह गाइड आपको Data Science for Beginners पाठ्यक्रम के दौरान आने वाली सामान्य समस्याओं के समाधान प्रदान करता है।

## सामग्री सूची

- [Python और Jupyter समस्याएँ](../..)
- [पैकेज और निर्भरता समस्याएँ](../..)
- [Jupyter Notebook समस्याएँ](../..)
- [क्विज़ एप्लिकेशन समस्याएँ](../..)
- [Git और GitHub समस्याएँ](../..)
- [Docsify दस्तावेज़ समस्याएँ](../..)
- [डेटा और फ़ाइल समस्याएँ](../..)
- [प्रदर्शन समस्याएँ](../..)
- [अतिरिक्त सहायता प्राप्त करना](../..)

## Python और Jupyter समस्याएँ

### Python नहीं मिला या गलत संस्करण

**समस्या:** `python: command not found` या गलत Python संस्करण

**समाधान:**

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

**Windows समाधान:**
1. [python.org](https://www.python.org/) से Python को पुनः इंस्टॉल करें।
2. इंस्टॉलेशन के दौरान "Add Python to PATH" विकल्प चुनें।
3. अपना टर्मिनल/कमांड प्रॉम्प्ट पुनः प्रारंभ करें।

### वर्चुअल एनवायरनमेंट सक्रिय करने में समस्या

**समस्या:** वर्चुअल एनवायरनमेंट सक्रिय नहीं हो रहा है।

**समाधान:**

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

**सक्रियता की पुष्टि करें:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter Kernel समस्याएँ

**समस्या:** "Kernel not found" या "Kernel keeps dying"

**समाधान:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**समस्या:** Jupyter में गलत Python संस्करण

**समाधान:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## पैकेज और निर्भरता समस्याएँ

### आयात त्रुटियाँ

**समस्या:** `ModuleNotFoundError: No module named 'pandas'` (या अन्य पैकेज)

**समाधान:**

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

### Pip इंस्टॉलेशन विफलता

**समस्या:** `pip install` अनुमति त्रुटियों के साथ विफल हो रहा है।

**समाधान:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**समस्या:** `pip install` SSL प्रमाणपत्र त्रुटियों के साथ विफल हो रहा है।

**समाधान:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### पैकेज संस्करण संघर्ष

**समस्या:** असंगत पैकेज संस्करण

**समाधान:**

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

## Jupyter Notebook समस्याएँ

### Jupyter प्रारंभ नहीं हो रहा है

**समस्या:** `jupyter notebook` कमांड नहीं मिला

**समाधान:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook लोड या सेव नहीं हो रहा है

**समस्या:** "Notebook failed to load" या सेव त्रुटियाँ

**समाधान:**

1. फ़ाइल अनुमतियों की जाँच करें।
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. फ़ाइल भ्रष्टाचार की जाँच करें।
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Jupyter कैश साफ़ करें।
```bash
jupyter notebook --clear-cache
```

### सेल निष्पादित नहीं हो रहा है

**समस्या:** सेल "In [*]" पर अटका हुआ है या बहुत समय ले रहा है।

**समाधान:**

1. **कर्नेल को बाधित करें:** "Interrupt" बटन पर क्लिक करें या `I, I` दबाएँ।
2. **कर्नेल पुनः प्रारंभ करें:** Kernel मेनू → Restart।
3. **कोड में अनंत लूप की जाँच करें।**
4. **आउटपुट साफ़ करें:** Cell → All Output → Clear।

### प्लॉट प्रदर्शित नहीं हो रहे हैं

**समस्या:** `matplotlib` प्लॉट नोटबुक में नहीं दिख रहे हैं।

**समाधान:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**इंटरैक्टिव प्लॉट के लिए वैकल्पिक:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## क्विज़ एप्लिकेशन समस्याएँ

### npm install विफल हो रहा है

**समस्या:** `npm install` के दौरान त्रुटियाँ

**समाधान:**

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

### क्विज़ ऐप प्रारंभ नहीं हो रहा है

**समस्या:** `npm run serve` विफल हो रहा है

**समाधान:**

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

### पोर्ट पहले से उपयोग में है

**समस्या:** "Port 8080 is already in use"

**समाधान:**

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

### क्विज़ लोड नहीं हो रहा है या खाली पेज दिखा रहा है

**समस्या:** क्विज़ ऐप लोड हो रहा है लेकिन खाली पेज दिखा रहा है।

**समाधान:**

1. ब्राउज़र कंसोल में त्रुटियों की जाँच करें (F12 दबाएँ)।
2. ब्राउज़र कैश और कुकीज़ साफ़ करें।
3. अलग ब्राउज़र आज़माएँ।
4. सुनिश्चित करें कि JavaScript सक्षम है।
5. विज्ञापन ब्लॉकर के हस्तक्षेप की जाँच करें।

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git और GitHub समस्याएँ

### Git मान्यता प्राप्त नहीं हो रहा है

**समस्या:** `git: command not found`

**समाधान:**

**Windows:**
- [git-scm.com](https://git-scm.com/) से Git इंस्टॉल करें।
- इंस्टॉलेशन के बाद टर्मिनल पुनः प्रारंभ करें।

**macOS:**

> **नोट:** यदि आपके पास Homebrew इंस्टॉल नहीं है, तो [https://brew.sh/](https://brew.sh/) पर दिए गए निर्देशों का पालन करें।
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

### Clone विफल हो रहा है

**समस्या:** `git clone` प्रमाणीकरण त्रुटियों के साथ विफल हो रहा है।

**समाधान:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### अनुमति अस्वीकृत (publickey)

**समस्या:** SSH कुंजी प्रमाणीकरण विफल हो रहा है।

**समाधान:**

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

## Docsify दस्तावेज़ समस्याएँ

### Docsify कमांड नहीं मिला

**समस्या:** `docsify: command not found`

**समाधान:**

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

### दस्तावेज़ लोड नहीं हो रहा है

**समस्या:** Docsify सर्व कर रहा है लेकिन सामग्री लोड नहीं हो रही है।

**समाधान:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### चित्र प्रदर्शित नहीं हो रहे हैं

**समस्या:** चित्र टूटे हुए लिंक आइकन दिखा रहे हैं।

**समाधान:**

1. सुनिश्चित करें कि चित्र पथ सापेक्ष हैं।
2. सुनिश्चित करें कि चित्र फ़ाइलें रिपॉजिटरी में मौजूद हैं।
3. ब्राउज़र कैश साफ़ करें।
4. फ़ाइल एक्सटेंशन का मिलान करें (कुछ सिस्टम पर केस-सेंसिटिव)।

## डेटा और फ़ाइल समस्याएँ

### फ़ाइल नहीं मिली त्रुटियाँ

**समस्या:** `FileNotFoundError` डेटा लोड करते समय

**समाधान:**

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

### CSV पढ़ने में त्रुटियाँ

**समस्या:** CSV फ़ाइलें पढ़ने में त्रुटियाँ

**समाधान:**

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

### बड़े डेटा सेट के साथ मेमोरी त्रुटियाँ

**समस्या:** `MemoryError` बड़े फ़ाइलें लोड करते समय

**समाधान:**

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

## प्रदर्शन समस्याएँ

### नोटबुक प्रदर्शन धीमा

**समस्या:** नोटबुक बहुत धीमी चल रही है।

**समाधान:**

1. **कर्नेल पुनः प्रारंभ करें और आउटपुट साफ़ करें।**
   - Kernel → Restart & Clear Output।

2. **अनावश्यक नोटबुक बंद करें।**

3. **कोड को अनुकूलित करें:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **बड़े डेटा सेट का नमूना लें:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### ब्राउज़र क्रैश हो रहा है

**समस्या:** ब्राउज़र क्रैश हो रहा है या अनुत्तरदायी हो रहा है।

**समाधान:**

1. अनावश्यक टैब बंद करें।
2. ब्राउज़र कैश साफ़ करें।
3. ब्राउज़र मेमोरी बढ़ाएँ (Chrome: `chrome://settings/system`)।
4. JupyterLab का उपयोग करें:
```bash
pip install jupyterlab
jupyter lab
```

## अतिरिक्त सहायता प्राप्त करना

### सहायता मांगने से पहले

1. इस समस्या निवारण गाइड की जाँच करें।
2. [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) पर खोजें।
3. [INSTALLATION.md](INSTALLATION.md) और [USAGE.md](USAGE.md) की समीक्षा करें।
4. त्रुटि संदेश को ऑनलाइन खोजने का प्रयास करें।

### सहायता कैसे मांगें

जब कोई समस्या बनाएं या सहायता मांगें, तो निम्नलिखित शामिल करें:

1. **ऑपरेटिंग सिस्टम**: Windows, macOS, या Linux (कौन सा वितरण)
2. **Python संस्करण**: `python --version` चलाएँ।
3. **त्रुटि संदेश**: पूरा त्रुटि संदेश कॉपी करें।
4. **पुनरुत्पादन के चरण**: त्रुटि होने से पहले आपने क्या किया।
5. **आपने क्या प्रयास किया है**: पहले से किए गए समाधान।

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

### सामुदायिक संसाधन

- **GitHub Issues**: [समस्या बनाएं](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [हमारे समुदाय से जुड़ें](https://aka.ms/ds4beginners/discord)
- **चर्चाएँ**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Q&A फ़ोरम](https://docs.microsoft.com/answers/)

### संबंधित दस्तावेज़

- [INSTALLATION.md](INSTALLATION.md) - सेटअप निर्देश
- [USAGE.md](USAGE.md) - पाठ्यक्रम का उपयोग कैसे करें
- [CONTRIBUTING.md](CONTRIBUTING.md) - योगदान कैसे करें
- [README.md](README.md) - प्रोजेक्ट का अवलोकन

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।