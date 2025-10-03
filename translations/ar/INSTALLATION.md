<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:14:41+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "ar"
}
-->
# دليل التثبيت

هذا الدليل سيساعدك في إعداد بيئتك للعمل مع منهج "علم البيانات للمبتدئين".

## جدول المحتويات

- [المتطلبات الأساسية](../..)
- [خيارات البدء السريع](../..)
- [التثبيت المحلي](../..)
- [التحقق من التثبيت](../..)

## المتطلبات الأساسية

قبل أن تبدأ، يجب أن تكون لديك:

- معرفة أساسية باستخدام سطر الأوامر/الطرفية
- حساب GitHub (مجاني)
- اتصال إنترنت مستقر للإعداد الأولي

## خيارات البدء السريع

### الخيار الأول: GitHub Codespaces (موصى به للمبتدئين)

أسهل طريقة للبدء هي باستخدام GitHub Codespaces، الذي يوفر بيئة تطوير كاملة في متصفحك.

1. انتقل إلى [المستودع](https://github.com/microsoft/Data-Science-For-Beginners)
2. انقر على قائمة **Code** المنسدلة
3. اختر علامة التبويب **Codespaces**
4. انقر على **Create codespace on main**
5. انتظر حتى يتم تهيئة البيئة (2-3 دقائق)

الآن أصبحت بيئتك جاهزة مع جميع التبعيات المثبتة مسبقًا!

### الخيار الثاني: التطوير المحلي

للعمل على جهاز الكمبيوتر الخاص بك، اتبع التعليمات التفصيلية أدناه.

## التثبيت المحلي

### الخطوة الأولى: تثبيت Git

Git مطلوب لاستنساخ المستودع وتتبع تغييراتك.

**Windows:**
- قم بالتنزيل من [git-scm.com](https://git-scm.com/download/win)
- قم بتشغيل المثبت بالإعدادات الافتراضية

**macOS:**
- قم بالتثبيت عبر Homebrew: `brew install git`
- أو قم بالتنزيل من [git-scm.com](https://git-scm.com/download/mac)

**Linux:**
```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

### الخطوة الثانية: استنساخ المستودع

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### الخطوة الثالثة: تثبيت Python وJupyter

Python 3.7 أو أعلى مطلوب لدروس علم البيانات.

**Windows:**
1. قم بتنزيل Python من [python.org](https://www.python.org/downloads/)
2. أثناء التثبيت، قم بتحديد خيار "Add Python to PATH"
3. تحقق من التثبيت:
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

**Linux:**
```bash
# Most Linux distributions come with Python pre-installed
python3 --version

# If not installed:
# Debian/Ubuntu
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

### الخطوة الرابعة: إعداد بيئة Python

يُوصى باستخدام بيئة افتراضية للحفاظ على التبعيات معزولة.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### الخطوة الخامسة: تثبيت مكتبات Python

قم بتثبيت مكتبات علم البيانات المطلوبة:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### الخطوة السادسة: تثبيت Node.js وnpm (لتطبيق الاختبارات)

تطبيق الاختبارات يتطلب Node.js وnpm.

**Windows/macOS:**
- قم بالتنزيل من [nodejs.org](https://nodejs.org/) (يُوصى بالإصدار LTS)
- قم بتشغيل المثبت

**Linux:**
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

### الخطوة السابعة: تثبيت تبعيات تطبيق الاختبارات

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### الخطوة الثامنة: تثبيت Docsify (اختياري)

للوصول إلى الوثائق دون اتصال:

```bash
npm install -g docsify-cli
```

## التحقق من التثبيت

### اختبار Python وJupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

يجب أن يفتح المتصفح بواجهة Jupyter. يمكنك الآن التنقل إلى أي ملف `.ipynb` من الدروس.

### اختبار تطبيق الاختبارات

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

يجب أن يكون تطبيق الاختبارات متاحًا على `http://localhost:8080` (أو منفذ آخر إذا كان 8080 مشغولًا).

### اختبار خادم الوثائق

```bash
# From the root directory of the repository
docsify serve
```

يجب أن تكون الوثائق متاحة على `http://localhost:3000`.

## استخدام حاويات التطوير في VS Code

إذا كان لديك Docker مثبتًا، يمكنك استخدام حاويات التطوير في VS Code:

1. قم بتثبيت [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. قم بتثبيت [Visual Studio Code](https://code.visualstudio.com/)
3. قم بتثبيت [الإضافة Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. افتح المستودع في VS Code
5. اضغط على `F1` واختر "Remote-Containers: Reopen in Container"
6. انتظر حتى يتم بناء الحاوية (فقط في المرة الأولى)

## الخطوات التالية

- استكشف [README.md](README.md) للحصول على نظرة عامة على المنهج
- اقرأ [USAGE.md](USAGE.md) للحصول على أمثلة وسير العمل الشائعة
- تحقق من [TROUBLESHOOTING.md](TROUBLESHOOTING.md) إذا واجهت مشاكل
- راجع [CONTRIBUTING.md](CONTRIBUTING.md) إذا كنت ترغب في المساهمة

## الحصول على المساعدة

إذا واجهت مشاكل:

1. تحقق من دليل [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. ابحث في [مشاكل GitHub الحالية](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. انضم إلى [مجتمع Discord الخاص بنا](https://aka.ms/ds4beginners/discord)
4. قم بإنشاء مشكلة جديدة مع معلومات مفصلة حول مشكلتك

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.