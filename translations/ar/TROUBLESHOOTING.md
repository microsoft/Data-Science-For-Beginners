<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:30:25+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "ar"
}
-->
# دليل استكشاف الأخطاء وإصلاحها

يوفر هذا الدليل حلولًا للمشكلات الشائعة التي قد تواجهها أثناء العمل مع منهج "علم البيانات للمبتدئين".

## جدول المحتويات

- [مشكلات Python وJupyter](../..)
- [مشكلات الحزم والاعتماديات](../..)
- [مشكلات Jupyter Notebook](../..)
- [مشكلات تطبيق الاختبارات](../..)
- [مشكلات Git وGitHub](../..)
- [مشكلات توثيق Docsify](../..)
- [مشكلات البيانات والملفات](../..)
- [مشكلات الأداء](../..)
- [الحصول على مساعدة إضافية](../..)

## مشكلات Python وJupyter

### Python غير موجود أو إصدار خاطئ

**المشكلة:** `python: command not found` أو إصدار Python غير صحيح

**الحل:**

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

**الحل لنظام Windows:**
1. أعد تثبيت Python من [python.org](https://www.python.org/)
2. أثناء التثبيت، تأكد من تحديد خيار "Add Python to PATH"
3. أعد تشغيل الطرفية/موجه الأوامر

### مشكلات تفعيل البيئة الافتراضية

**المشكلة:** البيئة الافتراضية لا تعمل

**الحل:**

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

**التحقق من التفعيل:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### مشكلات Kernel في Jupyter

**المشكلة:** "Kernel غير موجود" أو "Kernel يستمر في التوقف"

**الحل:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**المشكلة:** إصدار Python غير صحيح في Jupyter

**الحل:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## مشكلات الحزم والاعتماديات

### أخطاء الاستيراد

**المشكلة:** `ModuleNotFoundError: No module named 'pandas'` (أو حزم أخرى)

**الحل:**

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

### فشل تثبيت pip

**المشكلة:** `pip install` يفشل بسبب أخطاء في الأذونات

**الحل:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**المشكلة:** `pip install` يفشل بسبب أخطاء شهادة SSL

**الحل:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### تعارض إصدارات الحزم

**المشكلة:** إصدارات الحزم غير متوافقة

**الحل:**

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

## مشكلات Jupyter Notebook

### Jupyter لا يعمل

**المشكلة:** الأمر `jupyter notebook` غير موجود

**الحل:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### دفتر الملاحظات لا يتم تحميله أو حفظه

**المشكلة:** "Notebook فشل في التحميل" أو أخطاء الحفظ

**الحل:**

1. تحقق من أذونات الملفات
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. تحقق من تلف الملفات
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. قم بمسح ذاكرة التخزين المؤقت لـ Jupyter
```bash
jupyter notebook --clear-cache
```

### الخلايا لا تعمل

**المشكلة:** الخلية عالقة على "In [*]" أو تستغرق وقتًا طويلًا

**الحل:**

1. **إيقاف Kernel:** انقر على زر "Interrupt" أو اضغط `I, I`
2. **إعادة تشغيل Kernel:** قائمة Kernel → إعادة تشغيل
3. **تحقق من الحلقات اللانهائية** في الكود الخاص بك
4. **مسح الإخراج:** قائمة Cell → All Output → Clear

### الرسوم البيانية لا تظهر

**المشكلة:** الرسوم البيانية باستخدام `matplotlib` لا تظهر في دفتر الملاحظات

**الحل:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**بديل للرسوم البيانية التفاعلية:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## مشكلات تطبيق الاختبارات

### فشل npm install

**المشكلة:** أخطاء أثناء تنفيذ `npm install`

**الحل:**

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

### تطبيق الاختبارات لا يعمل

**المشكلة:** `npm run serve` يفشل

**الحل:**

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

### المنفذ مستخدم بالفعل

**المشكلة:** "Port 8080 is already in use"

**الحل:**

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

### الاختبار لا يتم تحميله أو تظهر صفحة فارغة

**المشكلة:** تطبيق الاختبارات يتم تحميله ولكن تظهر صفحة فارغة

**الحل:**

1. تحقق من أخطاء وحدة التحكم في المتصفح (F12)
2. قم بمسح ذاكرة التخزين المؤقت وملفات تعريف الارتباط للمتصفح
3. جرب متصفحًا مختلفًا
4. تأكد من تمكين JavaScript
5. تحقق من وجود أدوات حظر الإعلانات التي قد تتداخل

```bash
# Rebuild the app
npm run build
npm run serve
```

## مشكلات Git وGitHub

### Git غير معترف به

**المشكلة:** `git: command not found`

**الحل:**

**Windows:**
- قم بتثبيت Git من [git-scm.com](https://git-scm.com/)
- أعد تشغيل الطرفية بعد التثبيت

**macOS:**

> **ملاحظة:** إذا لم يكن لديك Homebrew مثبتًا، اتبع التعليمات على [https://brew.sh/](https://brew.sh/) لتثبيته أولاً.
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

### فشل الاستنساخ

**المشكلة:** `git clone` يفشل بسبب أخطاء المصادقة

**الحل:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### رفض الإذن (publickey)

**المشكلة:** فشل مصادقة مفتاح SSH

**الحل:**

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

## مشكلات توثيق Docsify

### أمر Docsify غير موجود

**المشكلة:** `docsify: command not found`

**الحل:**

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

### التوثيق لا يتم تحميله

**المشكلة:** Docsify يعمل ولكن المحتوى لا يتم تحميله

**الحل:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### الصور لا تظهر

**المشكلة:** الصور تظهر كرمز رابط مكسور

**الحل:**

1. تحقق من أن مسارات الصور نسبية
2. تأكد من وجود ملفات الصور في المستودع
3. قم بمسح ذاكرة التخزين المؤقت للمتصفح
4. تحقق من تطابق امتدادات الملفات (حساسة لحالة الأحرف في بعض الأنظمة)

## مشكلات البيانات والملفات

### أخطاء عدم العثور على الملف

**المشكلة:** `FileNotFoundError` عند تحميل البيانات

**الحل:**

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

### أخطاء قراءة CSV

**المشكلة:** أخطاء عند قراءة ملفات CSV

**الحل:**

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

### أخطاء الذاكرة مع مجموعات البيانات الكبيرة

**المشكلة:** `MemoryError` عند تحميل ملفات كبيرة

**الحل:**

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

## مشكلات الأداء

### أداء دفتر الملاحظات بطيء

**المشكلة:** دفاتر الملاحظات تعمل ببطء شديد

**الحل:**

1. **إعادة تشغيل Kernel ومسح الإخراج**
   - Kernel → Restart & Clear Output

2. **إغلاق دفاتر الملاحظات غير المستخدمة**

3. **تحسين الكود:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **أخذ عينات من مجموعات البيانات الكبيرة:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### تعطل المتصفح

**المشكلة:** المتصفح يتعطل أو يصبح غير مستجيب

**الحل:**

1. أغلق علامات التبويب غير المستخدمة
2. قم بمسح ذاكرة التخزين المؤقت للمتصفح
3. زيادة ذاكرة المتصفح (Chrome: `chrome://settings/system`)
4. استخدم JupyterLab بدلاً من ذلك:
```bash
pip install jupyterlab
jupyter lab
```

## الحصول على مساعدة إضافية

### قبل طلب المساعدة

1. تحقق من هذا الدليل لاستكشاف الأخطاء وإصلاحها
2. ابحث في [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. راجع [INSTALLATION.md](INSTALLATION.md) و[USAGE.md](USAGE.md)
4. حاول البحث عن رسالة الخطأ عبر الإنترنت

### كيفية طلب المساعدة

عند إنشاء مشكلة أو طلب المساعدة، قم بتضمين:

1. **نظام التشغيل**: Windows، macOS، أو Linux (أي توزيع)
2. **إصدار Python**: قم بتشغيل `python --version`
3. **رسالة الخطأ**: انسخ رسالة الخطأ كاملة
4. **خطوات إعادة الإنتاج**: ما الذي قمت به قبل حدوث الخطأ
5. **ما الذي جربته بالفعل**: الحلول التي حاولت تطبيقها

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

### موارد المجتمع

- **GitHub Issues**: [إنشاء مشكلة](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [انضم إلى مجتمعنا](https://aka.ms/ds4beginners/discord)
- **Discussions**: [مناقشات GitHub](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [منتديات الأسئلة والأجوبة](https://docs.microsoft.com/answers/)

### الوثائق ذات الصلة

- [INSTALLATION.md](INSTALLATION.md) - تعليمات الإعداد
- [USAGE.md](USAGE.md) - كيفية استخدام المنهج
- [CONTRIBUTING.md](CONTRIBUTING.md) - كيفية المساهمة
- [README.md](README.md) - نظرة عامة على المشروع

---

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.