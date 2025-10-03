<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:15:36+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "ur"
}
-->
# انسٹالیشن گائیڈ

یہ گائیڈ آپ کو ڈیٹا سائنس فار بیگنرز نصاب کے ساتھ کام کرنے کے لیے اپنا ماحول ترتیب دینے میں مدد دے گی۔

## مواد کی فہرست

- [ضروریات](../..)
- [فوری آغاز کے اختیارات](../..)
- [مقامی انسٹالیشن](../..)
- [اپنی انسٹالیشن کی تصدیق کریں](../..)

## ضروریات

شروع کرنے سے پہلے، آپ کو درج ذیل چیزوں کی ضرورت ہوگی:

- کمانڈ لائن/ٹرمینل سے بنیادی واقفیت
- ایک GitHub اکاؤنٹ (مفت)
- ابتدائی سیٹ اپ کے لیے مستحکم انٹرنیٹ کنکشن

## فوری آغاز کے اختیارات

### آپشن 1: GitHub Codespaces (نوآموزوں کے لیے تجویز کردہ)

شروع کرنے کا سب سے آسان طریقہ GitHub Codespaces ہے، جو آپ کے براؤزر میں مکمل ترقیاتی ماحول فراہم کرتا ہے۔

1. [ریپوزٹری](https://github.com/microsoft/Data-Science-For-Beginners) پر جائیں
2. **Code** ڈراپ ڈاؤن مینو پر کلک کریں
3. **Codespaces** ٹیب منتخب کریں
4. **Create codespace on main** پر کلک کریں
5. ماحول کے ابتدائی ہونے کا انتظار کریں (2-3 منٹ)

آپ کا ماحول اب تمام ضروریات کے ساتھ تیار ہے!

### آپشن 2: مقامی ترقی

اپنے کمپیوٹر پر کام کرنے کے لیے، نیچے دی گئی تفصیلی ہدایات پر عمل کریں۔

## مقامی انسٹالیشن

### مرحلہ 1: Git انسٹال کریں

ریپوزٹری کلون کرنے اور اپنی تبدیلیوں کو ٹریک کرنے کے لیے Git ضروری ہے۔

**ونڈوز:**
- [git-scm.com](https://git-scm.com/download/win) سے ڈاؤنلوڈ کریں
- انسٹالر کو ڈیفالٹ سیٹنگز کے ساتھ چلائیں

**macOS:**
- Homebrew کے ذریعے انسٹال کریں: `brew install git`
- یا [git-scm.com](https://git-scm.com/download/mac) سے ڈاؤنلوڈ کریں

**لینکس:**
```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

### مرحلہ 2: ریپوزٹری کلون کریں

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### مرحلہ 3: Python اور Jupyter انسٹال کریں

ڈیٹا سائنس کے اسباق کے لیے Python 3.7 یا اس سے زیادہ ورژن ضروری ہے۔

**ونڈوز:**
1. [python.org](https://www.python.org/downloads/) سے Python ڈاؤنلوڈ کریں
2. انسٹالیشن کے دوران "Add Python to PATH" کو چیک کریں
3. انسٹالیشن کی تصدیق کریں:
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

**لینکس:**
```bash
# Most Linux distributions come with Python pre-installed
python3 --version

# If not installed:
# Debian/Ubuntu
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

### مرحلہ 4: Python ماحول ترتیب دیں

ضروریات کو الگ رکھنے کے لیے ورچوئل ماحول استعمال کرنے کی سفارش کی جاتی ہے۔

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### مرحلہ 5: Python پیکجز انسٹال کریں

ضروری ڈیٹا سائنس لائبریریاں انسٹال کریں:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### مرحلہ 6: Node.js اور npm انسٹال کریں (کوئز ایپ کے لیے)

کوئز ایپلیکیشن کے لیے Node.js اور npm ضروری ہیں۔

**ونڈوز/macOS:**
- [nodejs.org](https://nodejs.org/) سے ڈاؤنلوڈ کریں (LTS ورژن تجویز کردہ)
- انسٹالر چلائیں

**لینکس:**
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

### مرحلہ 7: کوئز ایپ کی ضروریات انسٹال کریں

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### مرحلہ 8: Docsify انسٹال کریں (اختیاری)

دستاویزات تک آف لائن رسائی کے لیے:

```bash
npm install -g docsify-cli
```

## اپنی انسٹالیشن کی تصدیق کریں

### Python اور Jupyter کا ٹیسٹ کریں

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

آپ کا براؤزر Jupyter انٹرفیس کے ساتھ کھلنا چاہیے۔ آپ اب کسی بھی سبق کی `.ipynb` فائل پر جا سکتے ہیں۔

### کوئز ایپلیکیشن کا ٹیسٹ کریں

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

کوئز ایپ `http://localhost:8080` پر دستیاب ہونی چاہیے (یا اگر 8080 مصروف ہو تو کسی اور پورٹ پر)۔

### دستاویزات سرور کا ٹیسٹ کریں

```bash
# From the root directory of the repository
docsify serve
```

دستاویزات `http://localhost:3000` پر دستیاب ہونی چاہیے۔

## VS Code Dev Containers کا استعمال

اگر آپ نے Docker انسٹال کیا ہے، تو آپ VS Code Dev Containers استعمال کر سکتے ہیں:

1. [Docker Desktop](https://www.docker.com/products/docker-desktop) انسٹال کریں
2. [Visual Studio Code](https://code.visualstudio.com/) انسٹال کریں
3. [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) انسٹال کریں
4. ریپوزٹری کو VS Code میں کھولیں
5. `F1` دبائیں اور "Remote-Containers: Reopen in Container" منتخب کریں
6. کنٹینر کے بننے کا انتظار کریں (صرف پہلی بار)

## اگلے مراحل

- نصاب کا جائزہ لینے کے لیے [README.md](README.md) کو دیکھیں
- عام ورک فلو اور مثالوں کے لیے [USAGE.md](USAGE.md) پڑھیں
- اگر آپ کو مسائل کا سامنا ہو تو [TROUBLESHOOTING.md](TROUBLESHOOTING.md) چیک کریں
- اگر آپ تعاون کرنا چاہتے ہیں تو [CONTRIBUTING.md](CONTRIBUTING.md) کا جائزہ لیں

## مدد حاصل کرنا

اگر آپ کو مسائل کا سامنا ہو:

1. [TROUBLESHOOTING.md](TROUBLESHOOTING.md) گائیڈ چیک کریں
2. موجودہ [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) تلاش کریں
3. ہمارے [Discord کمیونٹی](https://aka.ms/ds4beginners/discord) میں شامل ہوں
4. اپنی مسئلے کی تفصیلات کے ساتھ نیا مسئلہ بنائیں

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔