<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:36:32+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "ne"
}
-->
# समस्या समाधान मार्गदर्शिका

यो मार्गदर्शिकाले Data Science for Beginners पाठ्यक्रमसँग काम गर्दा सामना गर्न सकिने सामान्य समस्याहरूको समाधान प्रदान गर्दछ।

## सामग्री सूची

- [Python र Jupyter समस्याहरू](../..)
- [प्याकेज र निर्भरता समस्याहरू](../..)
- [Jupyter Notebook समस्याहरू](../..)
- [क्विज एप्लिकेशन समस्याहरू](../..)
- [Git र GitHub समस्याहरू](../..)
- [Docsify डकुमेन्टेशन समस्याहरू](../..)
- [डाटा र फाइल समस्याहरू](../..)
- [प्रदर्शन समस्याहरू](../..)
- [थप सहयोग प्राप्त गर्ने](../..)

## Python र Jupyter समस्याहरू

### Python फेला परेन वा गलत संस्करण

**समस्या:** `python: command not found` वा गलत Python संस्करण

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
1. [python.org](https://www.python.org/) बाट Python पुन: स्थापना गर्नुहोस्।
2. स्थापना गर्दा "Add Python to PATH" चेक गर्नुहोस्।
3. आफ्नो टर्मिनल/कमाण्ड प्रम्प्ट पुन: सुरु गर्नुहोस्।

### भर्चुअल वातावरण सक्रियता समस्याहरू

**समस्या:** भर्चुअल वातावरण सक्रिय हुँदैन

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

**सक्रियता पुष्टि गर्नुहोस्:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter कर्नेल समस्याहरू

**समस्या:** "कर्नेल फेला परेन" वा "कर्नेल बारम्बार मर्छ"

**समाधान:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**समस्या:** Jupyter मा गलत Python संस्करण

**समाधान:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## प्याकेज र निर्भरता समस्याहरू

### आयात त्रुटिहरू

**समस्या:** `ModuleNotFoundError: No module named 'pandas'` (वा अन्य प्याकेजहरू)

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

### Pip स्थापना असफलता

**समस्या:** `pip install` अनुमति त्रुटिहरूको साथ असफल हुन्छ

**समाधान:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**समस्या:** `pip install` SSL प्रमाणपत्र त्रुटिहरूको साथ असफल हुन्छ

**समाधान:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### प्याकेज संस्करण द्वन्द्व

**समस्या:** असंगत प्याकेज संस्करणहरू

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

## Jupyter Notebook समस्याहरू

### Jupyter सुरु हुँदैन

**समस्या:** `jupyter notebook` कमाण्ड फेला परेन

**समाधान:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### नोटबुक लोड हुँदैन वा बचत हुँदैन

**समस्या:** "Notebook failed to load" वा बचत त्रुटिहरू

**समाधान:**

1. फाइल अनुमति जाँच गर्नुहोस्।
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. फाइल क्षति जाँच गर्नुहोस्।
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Jupyter क्यास सफा गर्नुहोस्।
```bash
jupyter notebook --clear-cache
```

### सेल कार्यान्वयन हुँदैन

**समस्या:** सेल "In [*]" मा अड्किएको छ वा धेरै समय लाग्छ।

**समाधान:**

1. **कर्नेल रोक्नुहोस्:** "Interrupt" बटन क्लिक गर्नुहोस् वा `I, I` थिच्नुहोस्।
2. **कर्नेल पुन: सुरु गर्नुहोस्:** कर्नेल मेनु → Restart
3. **कोडमा अनन्त लूपहरू जाँच गर्नुहोस्।**
4. **आउटपुट सफा गर्नुहोस्:** Cell → All Output → Clear

### प्लटहरू देखिँदैनन्

**समस्या:** `matplotlib` प्लटहरू नोटबुकमा देखिँदैनन्।

**समाधान:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**इन्टरएक्टिभ प्लटहरूको लागि विकल्प:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## क्विज एप्लिकेशन समस्याहरू

### npm install असफल

**समस्या:** `npm install` को क्रममा त्रुटिहरू

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

### क्विज एप सुरु हुँदैन

**समस्या:** `npm run serve` असफल

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

### पोर्ट पहिले नै प्रयोगमा छ

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

### क्विज लोड हुँदैन वा खाली पृष्ठ देखिन्छ

**समस्या:** क्विज एप लोड हुन्छ तर खाली पृष्ठ देखाउँछ।

**समाधान:**

1. ब्राउजर कन्सोलमा त्रुटिहरू जाँच गर्नुहोस् (F12)
2. ब्राउजर क्यास र कुकीहरू सफा गर्नुहोस्।
3. अर्को ब्राउजर प्रयास गर्नुहोस्।
4. सुनिश्चित गर्नुहोस् कि JavaScript सक्षम छ।
5. विज्ञापन ब्लकरहरू हस्तक्षेप गरिरहेको छ कि जाँच गर्नुहोस्।

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git र GitHub समस्याहरू

### Git मान्यता प्राप्त छैन

**समस्या:** `git: command not found`

**समाधान:**

**Windows:**
- [git-scm.com](https://git-scm.com/) बाट Git स्थापना गर्नुहोस्।
- स्थापना पछि टर्मिनल पुन: सुरु गर्नुहोस्।

**macOS:**

> **नोट:** यदि तपाईंले Homebrew स्थापना गर्नुभएको छैन भने, [https://brew.sh/](https://brew.sh/) मा निर्देशनहरू पालना गरेर पहिले स्थापना गर्नुहोस्।
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

### Clone असफल

**समस्या:** `git clone` प्रमाणीकरण त्रुटिहरूको साथ असफल

**समाधान:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### अनुमति अस्वीकृत (publickey)

**समस्या:** SSH key प्रमाणीकरण असफल

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

## Docsify डकुमेन्टेशन समस्याहरू

### Docsify कमाण्ड फेला परेन

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

### डकुमेन्टेशन लोड हुँदैन

**समस्या:** Docsify सेवा दिन्छ तर सामग्री लोड हुँदैन।

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

### छविहरू देखिँदैनन्

**समस्या:** छविहरूमा टुटेको लिंक आइकन देखिन्छ।

**समाधान:**

1. छवि पथहरू सापेक्ष छन् कि जाँच गर्नुहोस्।
2. सुनिश्चित गर्नुहोस् कि छवि फाइलहरू रिपोजिटरीमा छन्।
3. ब्राउजर क्यास सफा गर्नुहोस्।
4. फाइल एक्सटेन्सनहरू मिल्छन् कि जाँच गर्नुहोस् (केही प्रणालीहरूमा केस-संवेदी)।

## डाटा र फाइल समस्याहरू

### फाइल फेला परेन त्रुटिहरू

**समस्या:** `FileNotFoundError` डाटा लोड गर्दा

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

### CSV पढ्ने त्रुटिहरू

**समस्या:** CSV फाइलहरू पढ्दा त्रुटिहरू

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

### ठूला डाटासेटहरूमा मेमोरी त्रुटिहरू

**समस्या:** ठूला फाइलहरू लोड गर्दा `MemoryError`

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

## प्रदर्शन समस्याहरू

### नोटबुक प्रदर्शन सुस्त

**समस्या:** नोटबुकहरू धेरै सुस्त चल्छन्।

**समाधान:**

1. **कर्नेल पुन: सुरु गर्नुहोस् र आउटपुट सफा गर्नुहोस्।**
   - Kernel → Restart & Clear Output

2. **प्रयोग नगरिएका नोटबुकहरू बन्द गर्नुहोस्।**

3. **कोड अनुकूलन गर्नुहोस्:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **ठूला डाटासेटहरू नमूना गर्नुहोस्:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### ब्राउजर क्र्यास

**समस्या:** ब्राउजर क्र्यास हुन्छ वा अनुत्तरदायी हुन्छ।

**समाधान:**

1. प्रयोग नगरिएका ट्याबहरू बन्द गर्नुहोस्।
2. ब्राउजर क्यास सफा गर्नुहोस्।
3. ब्राउजर मेमोरी बढाउनुहोस् (Chrome: `chrome://settings/system`)
4. JupyterLab प्रयोग गर्नुहोस्:
```bash
pip install jupyterlab
jupyter lab
```

## थप सहयोग प्राप्त गर्ने

### सहयोग माग्नु अघि

1. यो समस्या समाधान मार्गदर्शिका जाँच गर्नुहोस्।
2. [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) खोज्नुहोस्।
3. [INSTALLATION.md](INSTALLATION.md) र [USAGE.md](USAGE.md) समीक्षा गर्नुहोस्।
4. अनलाइन त्रुटि सन्देश खोज्ने प्रयास गर्नुहोस्।

### सहयोग कसरी माग्ने

इस्यु सिर्जना गर्दा वा सहयोग माग्दा, निम्न समावेश गर्नुहोस्:

1. **अपरेटिङ सिस्टम**: Windows, macOS, वा Linux (कुन वितरण)
2. **Python संस्करण**: `python --version` चलाउनुहोस्।
3. **त्रुटि सन्देश**: पूर्ण त्रुटि सन्देश प्रतिलिपि गर्नुहोस्।
4. **पुन: उत्पादन गर्ने चरणहरू**: त्रुटि हुनु अघि तपाईंले के गर्नुभयो।
5. **तपाईंले प्रयास गर्नुभएको समाधानहरू**: तपाईंले पहिले नै प्रयास गरिसकेको समाधानहरू।

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

### समुदाय स्रोतहरू

- **GitHub Issues**: [इस्यु सिर्जना गर्नुहोस्](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [हाम्रो समुदायमा सामेल हुनुहोस्](https://aka.ms/ds4beginners/discord)
- **Discussions**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Q&A Forums](https://docs.microsoft.com/answers/)

### सम्बन्धित डकुमेन्टेशन

- [INSTALLATION.md](INSTALLATION.md) - सेटअप निर्देशनहरू
- [USAGE.md](USAGE.md) - पाठ्यक्रम कसरी प्रयोग गर्ने
- [CONTRIBUTING.md](CONTRIBUTING.md) - योगदान कसरी गर्ने
- [README.md](README.md) - परियोजना अवलोकन

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी यथार्थताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। मूल दस्तावेज़ यसको मातृभाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुनेछैनौं।