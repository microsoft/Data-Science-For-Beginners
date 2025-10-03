<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:31:26+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "ur"
}
-->
# خرابیوں کو دور کرنے کی رہنما

یہ رہنما ڈیٹا سائنس فار بیگنرز نصاب کے دوران پیش آنے والے عام مسائل کے حل فراہم کرتی ہے۔

## مواد کی فہرست

- [پائتھون اور جیوپیٹر کے مسائل](../..)
- [پیکیج اور انحصار کے مسائل](../..)
- [جیوپیٹر نوٹ بک کے مسائل](../..)
- [کوئز ایپلیکیشن کے مسائل](../..)
- [گٹ اور گٹ ہب کے مسائل](../..)
- [ڈاکسیفائی دستاویزات کے مسائل](../..)
- [ڈیٹا اور فائل کے مسائل](../..)
- [کارکردگی کے مسائل](../..)
- [اضافی مدد حاصل کرنا](../..)

## پائتھون اور جیوپیٹر کے مسائل

### پائتھون نہیں ملا یا غلط ورژن

**مسئلہ:** `python: command not found` یا غلط پائتھون ورژن

**حل:**

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

**ونڈوز حل:**
1. [python.org](https://www.python.org/) سے پائتھون دوبارہ انسٹال کریں۔
2. انسٹالیشن کے دوران "Add Python to PATH" کو چیک کریں۔
3. اپنا ٹرمینل/کمانڈ پرامپٹ دوبارہ شروع کریں۔

### ورچوئل ماحول کو فعال کرنے کے مسائل

**مسئلہ:** ورچوئل ماحول فعال نہیں ہو رہا

**حل:**

**ونڈوز:**
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

**فعالیت کی تصدیق کریں:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### جیوپیٹر کرنل کے مسائل

**مسئلہ:** "Kernel not found" یا "Kernel keeps dying"

**حل:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**مسئلہ:** جیوپیٹر میں غلط پائتھون ورژن

**حل:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## پیکیج اور انحصار کے مسائل

### درآمد کی غلطیاں

**مسئلہ:** `ModuleNotFoundError: No module named 'pandas'` (یا دیگر پیکیجز)

**حل:**

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

### پِپ انسٹالیشن کی ناکامیاں

**مسئلہ:** `pip install` اجازت کی غلطیوں کے ساتھ ناکام ہو رہا ہے

**حل:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**مسئلہ:** `pip install` SSL سرٹیفکیٹ کی غلطیوں کے ساتھ ناکام ہو رہا ہے

**حل:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### پیکیج ورژن کے تضادات

**مسئلہ:** غیر مطابقت پذیر پیکیج ورژن

**حل:**

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

## جیوپیٹر نوٹ بک کے مسائل

### جیوپیٹر شروع نہیں ہو رہا

**مسئلہ:** `jupyter notebook` کمانڈ نہیں ملا

**حل:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### نوٹ بک لوڈ یا محفوظ نہیں ہو رہی

**مسئلہ:** "Notebook failed to load" یا محفوظ کرنے کی غلطیاں

**حل:**

1. فائل کی اجازتیں چیک کریں
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. فائل کے خراب ہونے کی جانچ کریں
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. جیوپیٹر کیش صاف کریں
```bash
jupyter notebook --clear-cache
```

### سیل عمل نہیں کر رہا

**مسئلہ:** سیل "In [*]" پر پھنس گیا یا بہت زیادہ وقت لے رہا ہے

**حل:**

1. **کرنل کو روکا جائے**: "Interrupt" بٹن پر کلک کریں یا `I, I` دبائیں۔
2. **کرنل کو دوبارہ شروع کریں**: Kernel مینو → Restart
3. **اپنے کوڈ میں لامتناہی لوپس کی جانچ کریں**
4. **آؤٹ پٹ صاف کریں**: Cell → All Output → Clear

### گراف ظاہر نہیں ہو رہے

**مسئلہ:** `matplotlib` گراف نوٹ بک میں ظاہر نہیں ہو رہے

**حل:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**متبادل برائے انٹرایکٹو گراف:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## کوئز ایپلیکیشن کے مسائل

### npm install ناکام ہو رہا ہے

**مسئلہ:** `npm install` کے دوران غلطیاں

**حل:**

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

### کوئز ایپ شروع نہیں ہو رہی

**مسئلہ:** `npm run serve` ناکام ہو رہا ہے

**حل:**

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

### پورٹ پہلے سے استعمال میں ہے

**مسئلہ:** "Port 8080 is already in use"

**حل:**

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

### کوئز لوڈ نہیں ہو رہا یا خالی صفحہ

**مسئلہ:** کوئز ایپ لوڈ ہو رہی ہے لیکن خالی صفحہ دکھا رہی ہے

**حل:**

1. براؤزر کنسول میں غلطیوں کی جانچ کریں (F12)
2. براؤزر کیش اور کوکیز صاف کریں
3. مختلف براؤزر آزمائیں
4. یقینی بنائیں کہ جاوا اسکرپٹ فعال ہے
5. ایڈ بلاکرز کی مداخلت چیک کریں

```bash
# Rebuild the app
npm run build
npm run serve
```

## گٹ اور گٹ ہب کے مسائل

### گٹ تسلیم نہیں ہو رہا

**مسئلہ:** `git: command not found`

**حل:**

**ونڈوز:**
- [git-scm.com](https://git-scm.com/) سے گٹ انسٹال کریں۔
- انسٹالیشن کے بعد ٹرمینل دوبارہ شروع کریں۔

**macOS:**

> **نوٹ:** اگر آپ کے پاس ہوم بریو انسٹال نہیں ہے، تو پہلے [https://brew.sh/](https://brew.sh/) پر دی گئی ہدایات پر عمل کریں۔
```bash
# Install via Homebrew
brew install git

# Or install Xcode Command Line Tools
xcode-select --install
```

**لینکس:**
```bash
sudo apt-get install git  # Debian/Ubuntu
sudo dnf install git      # Fedora
```

### کلون ناکام ہو رہا ہے

**مسئلہ:** `git clone` تصدیقی غلطیوں کے ساتھ ناکام ہو رہا ہے

**حل:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### اجازت مسترد (publickey)

**مسئلہ:** SSH کلید کی تصدیق ناکام ہو رہی ہے

**حل:**

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

## ڈاکسیفائی دستاویزات کے مسائل

### ڈاکسیفائی کمانڈ نہیں ملا

**مسئلہ:** `docsify: command not found`

**حل:**

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

### دستاویزات لوڈ نہیں ہو رہی

**مسئلہ:** ڈاکسیفائی سروس ہو رہی ہے لیکن مواد لوڈ نہیں ہو رہا

**حل:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### تصاویر ظاہر نہیں ہو رہی

**مسئلہ:** تصاویر ٹوٹے ہوئے لنک آئیکن دکھا رہی ہیں

**حل:**

1. چیک کریں کہ تصویر کے راستے نسبتی ہیں
2. یقینی بنائیں کہ تصویر کی فائلیں ریپوزٹری میں موجود ہیں
3. براؤزر کیش صاف کریں
4. فائل ایکسٹینشنز کی تصدیق کریں (کچھ سسٹمز پر کیس حساس)

## ڈیٹا اور فائل کے مسائل

### فائل نہیں ملی غلطیاں

**مسئلہ:** `FileNotFoundError` ڈیٹا لوڈ کرتے وقت

**حل:**

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

### CSV پڑھنے کی غلطیاں

**مسئلہ:** CSV فائلز پڑھتے وقت غلطیاں

**حل:**

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

### بڑے ڈیٹا سیٹس کے ساتھ میموری کی غلطیاں

**مسئلہ:** `MemoryError` بڑی فائلز لوڈ کرتے وقت

**حل:**

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

## کارکردگی کے مسائل

### نوٹ بک کی سست کارکردگی

**مسئلہ:** نوٹ بکس بہت سست چل رہی ہیں

**حل:**

1. **کرنل کو دوبارہ شروع کریں اور آؤٹ پٹ صاف کریں**
   - Kernel → Restart & Clear Output

2. **غیر استعمال شدہ نوٹ بکس بند کریں**

3. **کوڈ کو بہتر بنائیں:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **بڑے ڈیٹا سیٹس کو نمونہ بنائیں:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### براؤزر کریش ہو رہا ہے

**مسئلہ:** براؤزر کریش ہو رہا ہے یا غیر جوابی ہو رہا ہے

**حل:**

1. غیر استعمال شدہ ٹیبز بند کریں
2. براؤزر کیش صاف کریں
3. براؤزر میموری بڑھائیں (Chrome: `chrome://settings/system`)
4. جیوپیٹر لیب استعمال کریں:
```bash
pip install jupyterlab
jupyter lab
```

## اضافی مدد حاصل کرنا

### مدد مانگنے سے پہلے

1. اس خرابیوں کو دور کرنے کی رہنما چیک کریں
2. [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) تلاش کریں
3. [INSTALLATION.md](INSTALLATION.md) اور [USAGE.md](USAGE.md) کا جائزہ لیں
4. آن لائن غلطی کا پیغام تلاش کرنے کی کوشش کریں

### مدد مانگنے کا طریقہ

جب کوئی مسئلہ بنائیں یا مدد مانگیں، تو شامل کریں:

1. **آپریٹنگ سسٹم**: ونڈوز، macOS، یا لینکس (کون سا ڈسٹریبیوشن)
2. **پائتھون ورژن**: `python --version` چلائیں
3. **غلطی کا پیغام**: مکمل غلطی کا پیغام کاپی کریں
4. **دوبارہ پیدا کرنے کے اقدامات**: غلطی ہونے سے پہلے آپ نے کیا کیا
5. **آپ نے کیا کوشش کی**: وہ حل جو آپ نے پہلے ہی آزما لیے ہیں

**مثال:**
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

### کمیونٹی وسائل

- **GitHub Issues**: [مسئلہ بنائیں](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [ہماری کمیونٹی میں شامل ہوں](https://aka.ms/ds4beginners/discord)
- **Discussions**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Q&A فورمز](https://docs.microsoft.com/answers/)

### متعلقہ دستاویزات

- [INSTALLATION.md](INSTALLATION.md) - سیٹ اپ کی ہدایات
- [USAGE.md](USAGE.md) - نصاب استعمال کرنے کا طریقہ
- [CONTRIBUTING.md](CONTRIBUTING.md) - تعاون کرنے کا طریقہ
- [README.md](README.md) - پروجیکٹ کا جائزہ

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔