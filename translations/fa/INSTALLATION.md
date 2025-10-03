<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:15:16+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "fa"
}
-->
# راهنمای نصب

این راهنما به شما کمک می‌کند محیط خود را برای کار با دوره آموزشی «علم داده برای مبتدیان» آماده کنید.

## فهرست مطالب

- [پیش‌نیازها](../..)
- [گزینه‌های شروع سریع](../..)
- [نصب محلی](../..)
- [تأیید نصب](../..)

## پیش‌نیازها

قبل از شروع، باید موارد زیر را داشته باشید:

- آشنایی اولیه با خط فرمان/ترمینال
- یک حساب کاربری GitHub (رایگان)
- اتصال اینترنت پایدار برای تنظیم اولیه

## گزینه‌های شروع سریع

### گزینه ۱: GitHub Codespaces (توصیه‌شده برای مبتدیان)

ساده‌ترین راه برای شروع، استفاده از GitHub Codespaces است که یک محیط توسعه کامل را در مرورگر شما فراهم می‌کند.

1. به [مخزن](https://github.com/microsoft/Data-Science-For-Beginners) بروید  
2. روی منوی کشویی **Code** کلیک کنید  
3. تب **Codespaces** را انتخاب کنید  
4. روی **Create codespace on main** کلیک کنید  
5. منتظر بمانید تا محیط راه‌اندازی شود (۲-۳ دقیقه)  

اکنون محیط شما با تمام وابستگی‌های پیش‌نصب شده آماده است!

### گزینه ۲: توسعه محلی

برای کار بر روی کامپیوتر خود، دستورالعمل‌های زیر را دنبال کنید.

## نصب محلی

### مرحله ۱: نصب Git

Git برای کلون کردن مخزن و پیگیری تغییرات شما لازم است.

**ویندوز:**
- از [git-scm.com](https://git-scm.com/download/win) دانلود کنید  
- نصب‌کننده را با تنظیمات پیش‌فرض اجرا کنید  

**macOS:**
- از طریق Homebrew نصب کنید: `brew install git`  
- یا از [git-scm.com](https://git-scm.com/download/mac) دانلود کنید  

**لینوکس:**
```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

### مرحله ۲: کلون کردن مخزن

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### مرحله ۳: نصب Python و Jupyter

Python نسخه ۳.۷ یا بالاتر برای درس‌های علم داده مورد نیاز است.

**ویندوز:**
1. Python را از [python.org](https://www.python.org/downloads/) دانلود کنید  
2. در طول نصب، گزینه "Add Python to PATH" را انتخاب کنید  
3. نصب را تأیید کنید:  
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

**لینوکس:**
```bash
# Most Linux distributions come with Python pre-installed
python3 --version

# If not installed:
# Debian/Ubuntu
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

### مرحله ۴: تنظیم محیط Python

توصیه می‌شود از یک محیط مجازی برای جداسازی وابستگی‌ها استفاده کنید.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### مرحله ۵: نصب بسته‌های Python

کتابخانه‌های لازم برای علم داده را نصب کنید:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### مرحله ۶: نصب Node.js و npm (برای اپلیکیشن آزمون)

اپلیکیشن آزمون نیاز به Node.js و npm دارد.

**ویندوز/macOS:**
- از [nodejs.org](https://nodejs.org/) دانلود کنید (نسخه LTS توصیه می‌شود)  
- نصب‌کننده را اجرا کنید  

**لینوکس:**
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

### مرحله ۷: نصب وابستگی‌های اپلیکیشن آزمون

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### مرحله ۸: نصب Docsify (اختیاری)

برای دسترسی آفلاین به مستندات:

```bash
npm install -g docsify-cli
```

## تأیید نصب

### تست Python و Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

مرورگر شما باید با رابط Jupyter باز شود. اکنون می‌توانید به فایل‌های `.ipynb` هر درس دسترسی پیدا کنید.

### تست اپلیکیشن آزمون

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

اپلیکیشن آزمون باید در `http://localhost:8080` (یا یک پورت دیگر اگر 8080 مشغول باشد) در دسترس باشد.

### تست سرور مستندات

```bash
# From the root directory of the repository
docsify serve
```

مستندات باید در `http://localhost:3000` در دسترس باشد.

## استفاده از Dev Containers در VS Code

اگر Docker نصب شده باشد، می‌توانید از Dev Containers در VS Code استفاده کنید:

1. [Docker Desktop](https://www.docker.com/products/docker-desktop) را نصب کنید  
2. [Visual Studio Code](https://code.visualstudio.com/) را نصب کنید  
3. افزونه [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) را نصب کنید  
4. مخزن را در VS Code باز کنید  
5. کلید `F1` را فشار دهید و گزینه "Remote-Containers: Reopen in Container" را انتخاب کنید  
6. منتظر بمانید تا کانتینر ساخته شود (فقط بار اول)  

## مراحل بعدی

- [README.md](README.md) را برای یک نمای کلی از دوره مطالعه کنید  
- [USAGE.md](USAGE.md) را برای گردش‌های کاری و مثال‌های رایج بخوانید  
- اگر با مشکلی مواجه شدید، [TROUBLESHOOTING.md](TROUBLESHOOTING.md) را بررسی کنید  
- اگر می‌خواهید مشارکت کنید، [CONTRIBUTING.md](CONTRIBUTING.md) را مرور کنید  

## دریافت کمک

اگر با مشکلی مواجه شدید:

1. راهنمای [TROUBLESHOOTING.md](TROUBLESHOOTING.md) را بررسی کنید  
2. در [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) موجود جستجو کنید  
3. به جامعه [Discord](https://aka.ms/ds4beginners/discord) ما بپیوندید  
4. یک مشکل جدید با اطلاعات دقیق درباره مشکل خود ایجاد کنید  

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه انسانی حرفه‌ای استفاده کنید. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.