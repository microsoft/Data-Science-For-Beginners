<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:35:19+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "bn"
}
-->
# সমস্যার সমাধানের গাইড

এই গাইডটি ডেটা সায়েন্স ফর বিগিনার্স কারিকুলাম নিয়ে কাজ করার সময় সাধারণ সমস্যাগুলোর সমাধান প্রদান করে।

## বিষয়বস্তুর তালিকা

- [Python এবং Jupyter সংক্রান্ত সমস্যা](../..)
- [প্যাকেজ এবং নির্ভরতা সংক্রান্ত সমস্যা](../..)
- [Jupyter Notebook সংক্রান্ত সমস্যা](../..)
- [কুইজ অ্যাপ্লিকেশন সংক্রান্ত সমস্যা](../..)
- [Git এবং GitHub সংক্রান্ত সমস্যা](../..)
- [Docsify ডকুমেন্টেশন সংক্রান্ত সমস্যা](../..)
- [ডেটা এবং ফাইল সংক্রান্ত সমস্যা](../..)
- [পারফরম্যান্স সংক্রান্ত সমস্যা](../..)
- [অতিরিক্ত সাহায্য পাওয়া](../..)

## Python এবং Jupyter সংক্রান্ত সমস্যা

### Python পাওয়া যাচ্ছে না বা ভুল ভার্সন

**সমস্যা:** `python: command not found` বা ভুল Python ভার্সন

**সমাধান:**

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

**Windows সমাধান:**
1. [python.org](https://www.python.org/) থেকে Python পুনরায় ইনস্টল করুন
2. ইনস্টলেশনের সময় "Add Python to PATH" চেক করুন
3. আপনার টার্মিনাল/কমান্ড প্রম্পট পুনরায় চালু করুন

### ভার্চুয়াল এনভায়রনমেন্ট সক্রিয় করার সমস্যা

**সমস্যা:** ভার্চুয়াল এনভায়রনমেন্ট সক্রিয় হচ্ছে না

**সমাধান:**

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

**সক্রিয়তা যাচাই করুন:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter Kernel সংক্রান্ত সমস্যা

**সমস্যা:** "Kernel not found" বা "Kernel keeps dying"

**সমাধান:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**সমস্যা:** Jupyter-এ ভুল Python ভার্সন

**সমাধান:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## প্যাকেজ এবং নির্ভরতা সংক্রান্ত সমস্যা

### Import Errors

**সমস্যা:** `ModuleNotFoundError: No module named 'pandas'` (বা অন্যান্য প্যাকেজ)

**সমাধান:**

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

### Pip ইনস্টলেশন ব্যর্থতা

**সমস্যা:** `pip install` অনুমতি সংক্রান্ত ত্রুটির কারণে ব্যর্থ

**সমাধান:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**সমস্যা:** `pip install` SSL সার্টিফিকেট ত্রুটির কারণে ব্যর্থ

**সমাধান:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### প্যাকেজ ভার্সন দ্বন্দ্ব

**সমস্যা:** অসামঞ্জস্যপূর্ণ প্যাকেজ ভার্সন

**সমাধান:**

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

## Jupyter Notebook সংক্রান্ত সমস্যা

### Jupyter চালু হচ্ছে না

**সমস্যা:** `jupyter notebook` কমান্ড পাওয়া যাচ্ছে না

**সমাধান:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook লোড বা সেভ হচ্ছে না

**সমস্যা:** "Notebook failed to load" বা সেভ ত্রুটি

**সমাধান:**

1. ফাইল অনুমতি যাচাই করুন
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. ফাইল ক্ষতিগ্রস্ত কিনা যাচাই করুন
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Jupyter ক্যাশ পরিষ্কার করুন
```bash
jupyter notebook --clear-cache
```

### সেল কার্যকর হচ্ছে না

**সমস্যা:** সেল "In [*]" এ আটকে আছে বা অনেক সময় নিচ্ছে

**সমাধান:**

1. **কর্নেল থামান:** "Interrupt" বোতাম ক্লিক করুন বা `I, I` চাপুন
2. **কর্নেল পুনরায় চালু করুন:** Kernel মেনু → Restart
3. **আপনার কোডে অসীম লুপ আছে কিনা যাচাই করুন**
4. **আউটপুট পরিষ্কার করুন:** Cell → All Output → Clear

### প্লট প্রদর্শিত হচ্ছে না

**সমস্যা:** `matplotlib` প্লট নোটবুকে প্রদর্শিত হচ্ছে না

**সমাধান:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**ইন্টারঅ্যাকটিভ প্লটের জন্য বিকল্প:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## কুইজ অ্যাপ্লিকেশন সংক্রান্ত সমস্যা

### npm install ব্যর্থ

**সমস্যা:** `npm install` চলাকালীন ত্রুটি

**সমাধান:**

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

### কুইজ অ্যাপ চালু হচ্ছে না

**সমস্যা:** `npm run serve` ব্যর্থ

**সমাধান:**

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

### পোর্ট ইতিমধ্যে ব্যবহৃত হচ্ছে

**সমস্যা:** "Port 8080 is already in use"

**সমাধান:**

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

### কুইজ লোড হচ্ছে না বা খালি পৃষ্ঠা

**সমস্যা:** কুইজ অ্যাপ লোড হচ্ছে কিন্তু খালি পৃষ্ঠা দেখাচ্ছে

**সমাধান:**

1. ব্রাউজার কনসোলে ত্রুটি চেক করুন (F12)
2. ব্রাউজারের ক্যাশ এবং কুকিজ পরিষ্কার করুন
3. অন্য ব্রাউজার চেষ্টা করুন
4. নিশ্চিত করুন যে জাভাস্ক্রিপ্ট সক্রিয় আছে
5. বিজ্ঞাপন ব্লকার সমস্যা সৃষ্টি করছে কিনা যাচাই করুন

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git এবং GitHub সংক্রান্ত সমস্যা

### Git স্বীকৃত হচ্ছে না

**সমস্যা:** `git: command not found`

**সমাধান:**

**Windows:**
- [git-scm.com](https://git-scm.com/) থেকে Git ইনস্টল করুন
- ইনস্টলেশনের পরে টার্মিনাল পুনরায় চালু করুন

**macOS:**

> **নোট:** যদি আপনার Homebrew ইনস্টল না থাকে, তাহলে [https://brew.sh/](https://brew.sh/) এ নির্দেশনা অনুসরণ করে প্রথমে এটি ইনস্টল করুন।
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

### ক্লোন ব্যর্থ

**সমস্যা:** `git clone` প্রমাণীকরণ ত্রুটির কারণে ব্যর্থ

**সমাধান:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### অনুমতি অস্বীকৃত (publickey)

**সমস্যা:** SSH কী প্রমাণীকরণ ব্যর্থ

**সমাধান:**

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

## Docsify ডকুমেন্টেশন সংক্রান্ত সমস্যা

### Docsify কমান্ড পাওয়া যাচ্ছে না

**সমস্যা:** `docsify: command not found`

**সমাধান:**

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

### ডকুমেন্টেশন লোড হচ্ছে না

**সমস্যা:** Docsify চালু হচ্ছে কিন্তু কন্টেন্ট লোড হচ্ছে না

**সমাধান:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### ছবি প্রদর্শিত হচ্ছে না

**সমস্যা:** ছবির স্থানে ভাঙা লিঙ্ক আইকন দেখাচ্ছে

**সমাধান:**

1. নিশ্চিত করুন যে ছবির পথগুলো আপেক্ষিক
2. নিশ্চিত করুন যে ছবির ফাইলগুলো রিপোজিটরিতে আছে
3. ব্রাউজারের ক্যাশ পরিষ্কার করুন
4. ফাইল এক্সটেনশনগুলো মিলে যাচ্ছে কিনা যাচাই করুন (কিছু সিস্টেমে কেস-সেনসিটিভ)

## ডেটা এবং ফাইল সংক্রান্ত সমস্যা

### ফাইল পাওয়া যাচ্ছে না ত্রুটি

**সমস্যা:** `FileNotFoundError` ডেটা লোড করার সময়

**সমাধান:**

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

### CSV পড়ার ত্রুটি

**সমস্যা:** CSV ফাইল পড়ার সময় ত্রুটি

**সমাধান:**

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

### বড় ডেটাসেটের কারণে মেমোরি ত্রুটি

**সমস্যা:** বড় ফাইল লোড করার সময় `MemoryError`

**সমাধান:**

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

## পারফরম্যান্স সংক্রান্ত সমস্যা

### নোটবুকের ধীর পারফরম্যান্স

**সমস্যা:** নোটবুক খুব ধীরে চলছে

**সমাধান:**

1. **কর্নেল পুনরায় চালু করুন এবং আউটপুট পরিষ্কার করুন**
   - Kernel → Restart & Clear Output

2. **অপ্রয়োজনীয় নোটবুক বন্ধ করুন**

3. **কোড অপ্টিমাইজ করুন:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **বড় ডেটাসেটের নমুনা নিন:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### ব্রাউজার ক্র্যাশ

**সমস্যা:** ব্রাউজার ক্র্যাশ করছে বা অপ্রতিক্রিয়াশীল হয়ে যাচ্ছে

**সমাধান:**

1. অপ্রয়োজনীয় ট্যাব বন্ধ করুন
2. ব্রাউজারের ক্যাশ পরিষ্কার করুন
3. ব্রাউজারের মেমোরি বাড়ান (Chrome: `chrome://settings/system`)
4. JupyterLab ব্যবহার করুন:
```bash
pip install jupyterlab
jupyter lab
```

## অতিরিক্ত সাহায্য পাওয়া

### সাহায্য চাওয়ার আগে

1. এই সমস্যার সমাধানের গাইডটি চেক করুন
2. [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) অনুসন্ধান করুন
3. [INSTALLATION.md](INSTALLATION.md) এবং [USAGE.md](USAGE.md) পর্যালোচনা করুন
4. ত্রুটির বার্তা অনলাইনে অনুসন্ধান করুন

### সাহায্য চাওয়ার পদ্ধতি

ইস্যু তৈরি করার সময় বা সাহায্য চাওয়ার সময় অন্তর্ভুক্ত করুন:

1. **অপারেটিং সিস্টেম**: Windows, macOS, বা Linux (যে ডিস্ট্রিবিউশন)
2. **Python ভার্সন**: `python --version` চালান
3. **ত্রুটির বার্তা**: সম্পূর্ণ ত্রুটির বার্তা কপি করুন
4. **পুনরুত্পাদনের ধাপ**: ত্রুটি ঘটার আগে আপনি কী করেছিলেন
5. **আপনার চেষ্টা করা সমাধান**: আপনি ইতিমধ্যে যে সমাধানগুলো চেষ্টা করেছেন

**উদাহরণ:**
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

### কমিউনিটি রিসোর্স

- **GitHub Issues**: [ইস্যু তৈরি করুন](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [আমাদের কমিউনিটিতে যোগ দিন](https://aka.ms/ds4beginners/discord)
- **Discussions**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [প্রশ্নোত্তর ফোরাম](https://docs.microsoft.com/answers/)

### সম্পর্কিত ডকুমেন্টেশন

- [INSTALLATION.md](INSTALLATION.md) - সেটআপ নির্দেশনা
- [USAGE.md](USAGE.md) - কারিকুলাম ব্যবহারের পদ্ধতি
- [CONTRIBUTING.md](CONTRIBUTING.md) - অবদান রাখার পদ্ধতি
- [README.md](README.md) - প্রকল্পের সংক্ষিপ্ত বিবরণ

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।