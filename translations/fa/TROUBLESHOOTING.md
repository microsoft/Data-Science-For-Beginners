<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:30:55+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "fa"
}
-->
# راهنمای رفع مشکلات

این راهنما راه‌حل‌هایی برای مشکلات رایج که ممکن است هنگام کار با دوره آموزشی «علم داده برای مبتدیان» با آن مواجه شوید ارائه می‌دهد.

## فهرست مطالب

- [مشکلات پایتون و Jupyter](../..)
- [مشکلات بسته‌ها و وابستگی‌ها](../..)
- [مشکلات Jupyter Notebook](../..)
- [مشکلات برنامه آزمون](../..)
- [مشکلات Git و GitHub](../..)
- [مشکلات مستندات Docsify](../..)
- [مشکلات داده‌ها و فایل‌ها](../..)
- [مشکلات عملکرد](../..)
- [دریافت کمک بیشتر](../..)

## مشکلات پایتون و Jupyter

### پایتون پیدا نمی‌شود یا نسخه اشتباه است

**مشکل:** `python: command not found` یا نسخه اشتباه پایتون

**راه‌حل:**

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

**راه‌حل برای ویندوز:**
1. پایتون را از [python.org](https://www.python.org/) دوباره نصب کنید.
2. هنگام نصب، گزینه "Add Python to PATH" را انتخاب کنید.
3. ترمینال/خط فرمان خود را مجدداً راه‌اندازی کنید.

### مشکلات فعال‌سازی محیط مجازی

**مشکل:** محیط مجازی فعال نمی‌شود

**راه‌حل:**

**ویندوز:**
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

**تأیید فعال‌سازی:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### مشکلات کرنل Jupyter

**مشکل:** "Kernel پیدا نشد" یا "Kernel مدام از کار می‌افتد"

**راه‌حل:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**مشکل:** نسخه اشتباه پایتون در Jupyter

**راه‌حل:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## مشکلات بسته‌ها و وابستگی‌ها

### خطاهای Import

**مشکل:** `ModuleNotFoundError: No module named 'pandas'` (یا سایر بسته‌ها)

**راه‌حل:**

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

### شکست نصب Pip

**مشکل:** `pip install` با خطاهای دسترسی شکست می‌خورد

**راه‌حل:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**مشکل:** `pip install` با خطاهای گواهی SSL شکست می‌خورد

**راه‌حل:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### تضاد نسخه‌های بسته‌ها

**مشکل:** نسخه‌های ناسازگار بسته‌ها

**راه‌حل:**

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

## مشکلات Jupyter Notebook

### Jupyter اجرا نمی‌شود

**مشکل:** دستور `jupyter notebook` پیدا نمی‌شود

**راه‌حل:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook بارگیری یا ذخیره نمی‌شود

**مشکل:** "Notebook بارگیری نشد" یا خطاهای ذخیره‌سازی

**راه‌حل:**

1. بررسی مجوزهای فایل
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. بررسی خرابی فایل
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. پاک کردن کش Jupyter
```bash
jupyter notebook --clear-cache
```

### سلول اجرا نمی‌شود

**مشکل:** سلول روی "In [*]" گیر کرده یا زمان زیادی می‌برد

**راه‌حل:**

1. **کرنل را متوقف کنید:** دکمه "Interrupt" را کلیک کنید یا `I, I` را فشار دهید.
2. **کرنل را مجدداً راه‌اندازی کنید:** منوی Kernel → Restart
3. **بررسی حلقه‌های بی‌نهایت** در کد خود
4. **پاک کردن خروجی:** Cell → All Output → Clear

### نمودارها نمایش داده نمی‌شوند

**مشکل:** نمودارهای `matplotlib` در Notebook نمایش داده نمی‌شوند

**راه‌حل:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**جایگزین برای نمودارهای تعاملی:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## مشکلات برنامه آزمون

### شکست npm install

**مشکل:** خطاها هنگام `npm install`

**راه‌حل:**

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

### برنامه آزمون اجرا نمی‌شود

**مشکل:** `npm run serve` شکست می‌خورد

**راه‌حل:**

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

### پورت قبلاً استفاده شده است

**مشکل:** "Port 8080 قبلاً استفاده شده است"

**راه‌حل:**

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

### آزمون بارگیری نمی‌شود یا صفحه خالی است

**مشکل:** برنامه آزمون بارگیری می‌شود اما صفحه خالی نمایش می‌دهد

**راه‌حل:**

1. کنسول مرورگر را برای خطاها بررسی کنید (F12)
2. کش و کوکی‌های مرورگر را پاک کنید
3. مرورگر دیگری را امتحان کنید
4. مطمئن شوید جاوااسکریپت فعال است
5. بررسی کنید آیا افزونه‌های مسدودکننده تبلیغات مشکل ایجاد می‌کنند

```bash
# Rebuild the app
npm run build
npm run serve
```

## مشکلات Git و GitHub

### Git شناسایی نمی‌شود

**مشکل:** `git: command not found`

**راه‌حل:**

**ویندوز:**
- Git را از [git-scm.com](https://git-scm.com/) نصب کنید.
- پس از نصب، ترمینال را مجدداً راه‌اندازی کنید.

**macOS:**

> **توجه:** اگر Homebrew نصب نشده است، دستورالعمل‌های [https://brew.sh/](https://brew.sh/) را برای نصب آن دنبال کنید.
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

### شکست Clone

**مشکل:** `git clone` با خطاهای احراز هویت شکست می‌خورد

**راه‌حل:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### دسترسی رد شد (publickey)

**مشکل:** احراز هویت کلید SSH شکست می‌خورد

**راه‌حل:**

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

## مشکلات مستندات Docsify

### دستور Docsify پیدا نمی‌شود

**مشکل:** `docsify: command not found`

**راه‌حل:**

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

### مستندات بارگیری نمی‌شود

**مشکل:** Docsify اجرا می‌شود اما محتوا بارگیری نمی‌شود

**راه‌حل:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### تصاویر نمایش داده نمی‌شوند

**مشکل:** تصاویر آیکون لینک شکسته نمایش می‌دهند

**راه‌حل:**

1. بررسی کنید مسیر تصاویر نسبی باشد.
2. مطمئن شوید فایل‌های تصاویر در مخزن وجود دارند.
3. کش مرورگر را پاک کنید.
4. بررسی کنید پسوند فایل‌ها مطابقت داشته باشد (حساس به حروف بزرگ و کوچک در برخی سیستم‌ها).

## مشکلات داده‌ها و فایل‌ها

### خطاهای فایل پیدا نشد

**مشکل:** `FileNotFoundError` هنگام بارگیری داده‌ها

**راه‌حل:**

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

### خطاهای خواندن CSV

**مشکل:** خطاها هنگام خواندن فایل‌های CSV

**راه‌حل:**

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

### خطاهای حافظه با مجموعه داده‌های بزرگ

**مشکل:** `MemoryError` هنگام بارگیری فایل‌های بزرگ

**راه‌حل:**

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

## مشکلات عملکرد

### عملکرد کند Notebook

**مشکل:** Notebook‌ها بسیار کند اجرا می‌شوند

**راه‌حل:**

1. **کرنل را مجدداً راه‌اندازی کنید و خروجی را پاک کنید**
   - Kernel → Restart & Clear Output

2. **Notebook‌های استفاده نشده را ببندید**

3. **کد را بهینه کنید:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **نمونه‌گیری از مجموعه داده‌های بزرگ:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### کرش مرورگر

**مشکل:** مرورگر کرش می‌کند یا پاسخ نمی‌دهد

**راه‌حل:**

1. تب‌های استفاده نشده را ببندید.
2. کش مرورگر را پاک کنید.
3. حافظه مرورگر را افزایش دهید (Chrome: `chrome://settings/system`)
4. به جای آن از JupyterLab استفاده کنید:
```bash
pip install jupyterlab
jupyter lab
```

## دریافت کمک بیشتر

### قبل از درخواست کمک

1. این راهنمای رفع مشکلات را بررسی کنید.
2. در [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) جستجو کنید.
3. [INSTALLATION.md](INSTALLATION.md) و [USAGE.md](USAGE.md) را مرور کنید.
4. پیام خطا را به صورت آنلاین جستجو کنید.

### نحوه درخواست کمک

هنگام ایجاد یک Issue یا درخواست کمک، موارد زیر را شامل کنید:

1. **سیستم عامل:** ویندوز، macOS یا لینوکس (کدام توزیع)
2. **نسخه پایتون:** دستور `python --version` را اجرا کنید.
3. **پیام خطا:** پیام خطا را به طور کامل کپی کنید.
4. **مراحل بازتولید:** کاری که قبل از وقوع خطا انجام دادید.
5. **آنچه امتحان کرده‌اید:** راه‌حل‌هایی که قبلاً امتحان کرده‌اید.

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

### منابع جامعه

- **GitHub Issues:** [ایجاد یک Issue](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord:** [به جامعه ما بپیوندید](https://aka.ms/ds4beginners/discord)
- **Discussions:** [بحث‌های GitHub](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn:** [فروم‌های پرسش و پاسخ](https://docs.microsoft.com/answers/)

### مستندات مرتبط

- [INSTALLATION.md](INSTALLATION.md) - دستورالعمل‌های راه‌اندازی
- [USAGE.md](USAGE.md) - نحوه استفاده از دوره آموزشی
- [CONTRIBUTING.md](CONTRIBUTING.md) - نحوه مشارکت
- [README.md](README.md) - نمای کلی پروژه

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده کنید. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.