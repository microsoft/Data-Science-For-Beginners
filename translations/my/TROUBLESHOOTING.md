<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:49:27+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "my"
}
-->
# ပြဿနာဖြေရှင်းလမ်းညွှန်

ဒီလမ်းညွှန်မှာ Data Science for Beginners သင်ခန်းစာကို အသုံးပြုရာမှာ ကြုံတွေ့နိုင်တဲ့ ပုံမှန်ပြဿနာများအတွက် ဖြေရှင်းနည်းများကို ပေးထားပါတယ်။

## အကြောင်းအရာများ

- [Python နှင့် Jupyter ပြဿနာများ](../..)
- [Package နှင့် Dependency ပြဿနာများ](../..)
- [Jupyter Notebook ပြဿနာများ](../..)
- [Quiz Application ပြဿနာများ](../..)
- [Git နှင့် GitHub ပြဿနာများ](../..)
- [Docsify Documentation ပြဿနာများ](../..)
- [Data နှင့် File ပြဿနာများ](../..)
- [Performance ပြဿနာများ](../..)
- [အပိုဆောင်းအကူအညီရယူခြင်း](../..)

## Python နှင့် Jupyter ပြဿနာများ

### Python မတွေ့ရှိခြင်း သို့မဟုတ် မမှန်သော Version

**ပြဿနာ:** `python: command not found` သို့မဟုတ် မမှန်သော Python version

**ဖြေရှင်းနည်း:**

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

**Windows ဖြေရှင်းနည်း:**
1. [python.org](https://www.python.org/) မှ Python ကို ပြန်လည်ထည့်သွင်းပါ
2. ထည့်သွင်းစဉ် "Add Python to PATH" ကို အမှန်ခြစ်ပါ
3. Terminal/Command Prompt ကို ပြန်လည်စတင်ပါ

### Virtual Environment Activation ပြဿနာများ

**ပြဿနာ:** Virtual environment ကို activate မရခြင်း

**ဖြေရှင်းနည်း:**

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

**Activation ကို အတည်ပြုပါ:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Jupyter Kernel ပြဿနာများ

**ပြဿနာ:** "Kernel not found" သို့မဟုတ် "Kernel keeps dying"

**ဖြေရှင်းနည်း:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**ပြဿနာ:** Jupyter မှာ Python version မမှန်ခြင်း

**ဖြေရှင်းနည်း:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Package နှင့် Dependency ပြဿနာများ

### Import Errors

**ပြဿနာ:** `ModuleNotFoundError: No module named 'pandas'` (သို့မဟုတ် အခြား package များ)

**ဖြေရှင်းနည်း:**

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

### Pip Installation Failures

**ပြဿနာ:** `pip install` မှာ permission error ဖြစ်ခြင်း

**ဖြေရှင်းနည်း:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**ပြဿနာ:** `pip install` မှာ SSL certificate error ဖြစ်ခြင်း

**ဖြေရှင်းနည်း:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Package Version Conflicts

**ပြဿနာ:** Package version မကိုက်ညီခြင်း

**ဖြေရှင်းနည်း:**

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

## Jupyter Notebook ပြဿနာများ

### Jupyter မစတင်နိုင်ခြင်း

**ပြဿနာ:** `jupyter notebook` command မတွေ့ရှိခြင်း

**ဖြေရှင်းနည်း:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook မတင်နိုင်ခြင်း သို့မဟုတ် မသိမ်းနိုင်ခြင်း

**ပြဿနာ:** "Notebook failed to load" သို့မဟုတ် save error ဖြစ်ခြင်း

**ဖြေရှင်းနည်း:**

1. File permission ကို စစ်ဆေးပါ
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. File ပျက်စီးမှုကို စစ်ဆေးပါ
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Jupyter cache ကို ရှင်းလင်းပါ
```bash
jupyter notebook --clear-cache
```

### Cell မအလုပ်လုပ်နိုင်ခြင်း

**ပြဿနာ:** Cell "In [*]" မှာ ရပ်နေခြင်း သို့မဟုတ် အချိန်ကြာနေခြင်း

**ဖြေရှင်းနည်း:**

1. **Kernel ကို ချိတ်ဆက်ဖြတ်ပါ**: "Interrupt" ခလုတ်ကို နှိပ်ပါ သို့မဟုတ် `I, I` ကို နှိပ်ပါ
2. **Kernel ကို ပြန်စတင်ပါ**: Kernel menu → Restart
3. **Infinite loop များ** ကို စစ်ဆေးပါ
4. **Output ကို ရှင်းလင်းပါ**: Cell → All Output → Clear

### Plots မပေါ်ခြင်း

**ပြဿနာ:** `matplotlib` plots မပေါ်ခြင်း

**ဖြေရှင်းနည်း:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Interactive plots အတွက် အခြားနည်းလမ်း:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Quiz Application ပြဿနာများ

### npm install မအောင်မြင်ခြင်း

**ပြဿနာ:** `npm install` မှာ error ဖြစ်ခြင်း

**ဖြေရှင်းနည်း:**

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

### Quiz App မစတင်နိုင်ခြင်း

**ပြဿနာ:** `npm run serve` မအောင်မြင်ခြင်း

**ဖြေရှင်းနည်း:**

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

### Port Already in Use

**ပြဿနာ:** "Port 8080 is already in use"

**ဖြေရှင်းနည်း:**

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

### Quiz မတင်နိုင်ခြင်း သို့မဟုတ် Blank Page

**ပြဿနာ:** Quiz app တင်နိုင်သော်လည်း Blank Page ပေါ်နေခြင်း

**ဖြေရှင်းနည်း:**

1. Browser console မှာ error ကို စစ်ဆေးပါ (F12)
2. Browser cache နှင့် cookies ကို ရှင်းလင်းပါ
3. အခြား browser ကို စမ်းသုံးပါ
4. JavaScript ကို enable လုပ်ထားပါ
5. Ad blocker များက အတားအဆီးဖြစ်နေမရှိကြောင်း စစ်ဆေးပါ

```bash
# Rebuild the app
npm run build
npm run serve
```

## Git နှင့် GitHub ပြဿနာများ

### Git မမှတ်မိခြင်း

**ပြဿနာ:** `git: command not found`

**ဖြေရှင်းနည်း:**

**Windows:**
- [git-scm.com](https://git-scm.com/) မှ Git ကို ထည့်သွင်းပါ
- Installation ပြီးလျှင် terminal ကို ပြန်လည်စတင်ပါ

**macOS:**

> **မှတ်ချက်:** Homebrew မရှိပါက [https://brew.sh/](https://brew.sh/) မှာ လမ်းညွှန်ချက်များကို လိုက်နာပြီး Install လုပ်ပါ။
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

### Clone မအောင်မြင်ခြင်း

**ပြဿနာ:** `git clone` မှာ authentication error ဖြစ်ခြင်း

**ဖြေရှင်းနည်း:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Permission Denied (publickey)

**ပြဿနာ:** SSH key authentication မအောင်မြင်ခြင်း

**ဖြေရှင်းနည်း:**

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

## Docsify Documentation ပြဿနာများ

### Docsify Command မတွေ့ရှိခြင်း

**ပြဿနာ:** `docsify: command not found`

**ဖြေရှင်းနည်း:**

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

### Documentation မတင်နိုင်ခြင်း

**ပြဿနာ:** Docsify serve သော်လည်း content မပေါ်ခြင်း

**ဖြေရှင်းနည်း:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Images မပေါ်ခြင်း

**ပြဿနာ:** Images မှာ broken link icon ပေါ်နေခြင်း

**ဖြေရှင်းနည်း:**

1. Image path များကို relative ဖြစ်ကြောင်း စစ်ဆေးပါ
2. Image file များ repository ထဲမှာ ရှိကြောင်း အတည်ပြုပါ
3. Browser cache ကို ရှင်းလင်းပါ
4. File extension များကို စစ်ဆေးပါ (အချို့ system များမှာ case-sensitive ဖြစ်သည်)

## Data နှင့် File ပြဿနာများ

### File မတွေ့ရှိခြင်း

**ပြဿနာ:** `FileNotFoundError` data ကို load လုပ်စဉ် ဖြစ်ခြင်း

**ဖြေရှင်းနည်း:**

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

### CSV Reading Errors

**ပြဿနာ:** CSV file မဖတ်နိုင်ခြင်း

**ဖြေရှင်းနည်း:**

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

### Memory Errors with Large Datasets

**ပြဿနာ:** `MemoryError` ใหญ่သော file များကို load လုပ်စဉ် ဖြစ်ခြင်း

**ဖြေရှင်းနည်း:**

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

## Performance ပြဿနာများ

### Notebook အလုပ်လုပ်နှေးခြင်း

**ပြဿနာ:** Notebook များ အလုပ်လုပ်နှေးခြင်း

**ဖြေရှင်းနည်း:**

1. **Kernel ကို ပြန်စတင်ပြီး output ကို ရှင်းလင်းပါ**
   - Kernel → Restart & Clear Output

2. **အသုံးမပြုသော notebook များကို ပိတ်ပါ**

3. **Code ကို အဆင့်မြှင့်ပါ:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **ใหญသော dataset များကို sample လုပ်ပါ:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Browser Crash ဖြစ်ခြင်း

**ပြဿနာ:** Browser crash ဖြစ်ခြင်း သို့မဟုတ် မတုံ့ပြန်ခြင်း

**ဖြေရှင်းနည်း:**

1. အသုံးမပြုသော tab များကို ပိတ်ပါ
2. Browser cache ကို ရှင်းလင်းပါ
3. Browser memory ကို တိုးမြှင့်ပါ (Chrome: `chrome://settings/system`)
4. JupyterLab ကို အသုံးပြုပါ:
```bash
pip install jupyterlab
jupyter lab
```

## အပိုဆောင်းအကူအညီရယူခြင်း

### အကူအညီတောင်းရန်မတိုင်မီ

1. ဒီ troubleshooting လမ်းညွှန်ကို စစ်ဆေးပါ
2. [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) ကို ရှာဖွေပါ
3. [INSTALLATION.md](INSTALLATION.md) နှင့် [USAGE.md](USAGE.md) ကို ပြန်လည်သုံးသပ်ပါ
4. Error message ကို အွန်လိုင်းတွင် ရှာဖွေကြည့်ပါ

### အကူအညီတောင်းရန် နည်းလမ်း

Issue တစ်ခုဖန်တီးသို့မဟုတ် အကူအညီတောင်းစဉ် အောက်ပါအချက်များကို ထည့်သွင်းပါ:

1. **Operating System**: Windows, macOS, သို့မဟုတ် Linux (distribution ဘယ်ဟာလဲ)
2. **Python Version**: `python --version` ကို run လုပ်ပါ
3. **Error Message**: Error message အပြည့်အစုံကို ကူးယူပါ
4. **Steps to Reproduce**: Error ဖြစ်မတိုင်မီ ဘာလုပ်ခဲ့လဲ
5. **What You've Tried**: အရင်စမ်းသုံးခဲ့တဲ့ ဖြေရှင်းနည်းများ

**ဥပမာ:**
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

### Community Resources

- **GitHub Issues**: [Issue တစ်ခုဖန်တီးပါ](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Community ကို Join လုပ်ပါ](https://aka.ms/ds4beginners/discord)
- **Discussions**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Q&A Forums](https://docs.microsoft.com/answers/)

### ဆက်စပ် Documentation

- [INSTALLATION.md](INSTALLATION.md) - Setup လမ်းညွှန်ချက်များ
- [USAGE.md](USAGE.md) - သင်ခန်းစာကို ဘယ်လိုအသုံးပြုမလဲ
- [CONTRIBUTING.md](CONTRIBUTING.md) - အထောက်အကူပြုရန် လမ်းညွှန်ချက်
- [README.md](README.md) - Project အကျဉ်းချုပ်

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။