<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:04:09+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ur"
}
-->
# اے جی ای این ٹی ایس۔ایم ڈی

## پروجیکٹ کا جائزہ

ڈیٹا سائنس فار بیگنرز مائیکروسافٹ ایزور کلاؤڈ ایڈووکیٹس کے ذریعہ تخلیق کردہ ایک جامع 10 ہفتوں، 20 اسباق پر مشتمل نصاب ہے۔ یہ ریپوزیٹری ایک تعلیمی وسیلہ ہے جو پروجیکٹ پر مبنی اسباق کے ذریعے بنیادی ڈیٹا سائنس کے تصورات سکھاتا ہے، جس میں جیوپیٹر نوٹ بکس، انٹرایکٹو کوئزز، اور عملی اسائنمنٹس شامل ہیں۔

**اہم ٹیکنالوجیز:**
- **جیوپیٹر نوٹ بکس**: Python 3 کے ساتھ بنیادی تعلیمی ذریعہ
- **پائتھن لائبریریاں**: pandas، numpy، matplotlib ڈیٹا تجزیہ اور بصریات کے لیے
- **Vue.js 2**: کوئز ایپلیکیشن (quiz-app فولڈر)
- **Docsify**: آف لائن رسائی کے لیے دستاویزات سائٹ جنریٹر
- **Node.js/npm**: جاوا اسکرپٹ اجزاء کے لیے پیکیج مینجمنٹ
- **مارک ڈاؤن**: تمام اسباق کا مواد اور دستاویزات

**آرکیٹیکچر:**
- کثیر زبانوں پر مشتمل تعلیمی ریپوزیٹری جس میں وسیع ترجمے شامل ہیں
- اسباق کے ماڈیولز میں منظم (1-Introduction سے 6-Data-Science-In-Wild تک)
- ہر سبق میں README، نوٹ بکس، اسائنمنٹس، اور کوئزز شامل ہیں
- پری/پوسٹ سبق کے جائزے کے لیے اسٹینڈ الون Vue.js کوئز ایپلیکیشن
- GitHub Codespaces اور VS Code ڈیولپمنٹ کنٹینرز کی حمایت

## سیٹ اپ کمانڈز

### ریپوزیٹری سیٹ اپ
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### پائتھن ماحول سیٹ اپ
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### کوئز ایپلیکیشن سیٹ اپ
```bash
# Navigate to quiz app
cd quiz-app

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint and fix files
npm run lint
```

### Docsify دستاویزات سرور
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### بصری منصوبوں کا سیٹ اپ
معنی خیز بصریات جیسے منصوبوں کے لیے (سبق 13):
```bash
# Navigate to starter or solution folder
cd 3-Data-Visualization/13-meaningful-visualizations/starter

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint files
npm run lint
```

## ترقیاتی ورک فلو

### جیوپیٹر نوٹ بکس کے ساتھ کام کرنا
1. ریپوزیٹری روٹ میں جیوپیٹر شروع کریں: `jupyter notebook`
2. مطلوبہ سبق فولڈر پر جائیں
3. `.ipynb` فائلز کھولیں اور مشقیں کریں
4. نوٹ بکس وضاحتوں اور کوڈ سیلز کے ساتھ خود مختار ہیں
5. زیادہ تر نوٹ بکس pandas، numpy، اور matplotlib استعمال کرتے ہیں - یقینی بنائیں کہ یہ انسٹال ہیں

### سبق کی ساخت
ہر سبق عام طور پر شامل ہوتا ہے:
- `README.md` - مرکزی سبق کا مواد نظریہ اور مثالوں کے ساتھ
- `notebook.ipynb` - عملی جیوپیٹر نوٹ بک مشقیں
- `assignment.ipynb` یا `assignment.md` - عملی اسائنمنٹس
- `solution/` فولڈر - حل نوٹ بکس اور کوڈ
- `images/` فولڈر - معاون بصری مواد

### کوئز ایپلیکیشن کی ترقی
- Vue.js 2 ایپلیکیشن ترقی کے دوران ہاٹ ری لوڈ کے ساتھ
- کوئزز `quiz-app/src/assets/translations/` میں محفوظ ہیں
- ہر زبان کا اپنا ترجمہ فولڈر ہے (en، fr، es، وغیرہ)
- کوئز نمبرنگ 0 سے شروع ہوتی ہے اور 39 تک جاتی ہے (کل 40 کوئزز)

### ترجمے شامل کرنا
- ترجمے ریپوزیٹری روٹ میں `translations/` فولڈر میں جاتے ہیں
- ہر زبان کا مکمل سبق ڈھانچہ انگریزی سے آئینہ دار ہوتا ہے
- GitHub Actions کے ذریعے خودکار ترجمہ (co-op-translator.yml)

## ٹیسٹنگ ہدایات

### کوئز ایپلیکیشن ٹیسٹنگ
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### نوٹ بک ٹیسٹنگ
- نوٹ بکس کے لیے کوئی خودکار ٹیسٹ فریم ورک موجود نہیں ہے
- دستی توثیق: تمام سیلز کو ترتیب میں چلائیں تاکہ کوئی غلطی نہ ہو
- ڈیٹا فائلز کی رسائی اور آؤٹ پٹس کی درستگی کی تصدیق کریں
- بصریات کی درست رینڈرنگ کو چیک کریں

### دستاویزات ٹیسٹنگ
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### کوڈ کوالٹی چیکس
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```

## کوڈ اسٹائل گائیڈ لائنز

### پائتھن (جیوپیٹر نوٹ بکس)
- پائتھن کوڈ کے لیے PEP 8 اسٹائل گائیڈ لائنز پر عمل کریں
- واضح متغیر نام استعمال کریں جو تجزیہ کیے جانے والے ڈیٹا کی وضاحت کریں
- کوڈ سیلز سے پہلے وضاحتوں کے ساتھ مارک ڈاؤن سیلز شامل کریں
- کوڈ سیلز کو ایک ہی تصور یا آپریشن پر مرکوز رکھیں
- ڈیٹا ہیرا پھیری کے لیے pandas، بصریات کے لیے matplotlib استعمال کریں
- عام درآمد کا نمونہ:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```

### جاوا اسکرپٹ/Vue.js
- Vue.js 2 اسٹائل گائیڈ اور بہترین طریقوں پر عمل کریں
- ESLint کنفیگریشن `quiz-app/package.json` میں
- Vue سنگل فائل اجزاء (.vue فائلز) استعمال کریں
- جزو پر مبنی آرکیٹیکچر برقرار رکھیں
- تبدیلیاں کرنے سے پہلے `npm run lint` چلائیں

### مارک ڈاؤن دستاویزات
- واضح سرخیوں کی درجہ بندی استعمال کریں (# ## ### وغیرہ)
- زبان کے وضاحت کنندہ کے ساتھ کوڈ بلاکس شامل کریں
- تصاویر کے لیے alt متن شامل کریں
- متعلقہ اسباق اور وسائل کے لنکس شامل کریں
- پڑھنے کے لیے لائن کی لمبائی مناسب رکھیں

### فائل تنظیم
- سبق کا مواد نمبر والے فولڈرز میں (01-defining-data-science، وغیرہ)
- حل مخصوص `solution/` سب فولڈرز میں
- ترجمے انگریزی ڈھانچے کو `translations/` فولڈر میں آئینہ دار کرتے ہیں
- ڈیٹا فائلز کو `data/` یا سبق مخصوص فولڈرز میں رکھیں

## تعمیر اور تعیناتی

### کوئز ایپلیکیشن تعیناتی
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Azure Static Web Apps تعیناتی
کوئز ایپ کو Azure Static Web Apps پر تعینات کیا جا سکتا ہے:
1. Azure Static Web App ریسورس بنائیں
2. GitHub ریپوزیٹری سے جڑیں
3. تعمیر کی ترتیبات کو ترتیب دیں:
   - ایپ مقام: `quiz-app`
   - آؤٹ پٹ مقام: `dist`
4. GitHub Actions ورک فلو پش پر خودکار تعیناتی کرے گا

### دستاویزات سائٹ
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- ریپوزیٹری میں ڈیولپمنٹ کنٹینر کنفیگریشن شامل ہے
- Codespaces خود بخود پائتھن اور Node.js ماحول سیٹ اپ کرتا ہے
- GitHub UI کے ذریعے ریپوزیٹری کو Codespace میں کھولیں
- تمام انحصار خود بخود انسٹال ہو جاتے ہیں

## پل ریکویسٹ گائیڈ لائنز

### جمع کرانے سے پہلے
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### پی آر عنوان کی شکل
- واضح، وضاحتی عنوانات استعمال کریں
- فارمیٹ: `[Component] مختصر وضاحت`
- مثالیں:
  - `[Lesson 7] Python نوٹ بک درآمد کی غلطی کو درست کریں`
  - `[Quiz App] جرمن ترجمہ شامل کریں`
  - `[Docs] نئی ضروریات کے ساتھ README کو اپ ڈیٹ کریں`

### مطلوبہ چیکس
- یقینی بنائیں کہ تمام کوڈ بغیر کسی غلطی کے چلتا ہے
- تصدیق کریں کہ نوٹ بکس مکمل طور پر عمل کرتے ہیں
- تصدیق کریں کہ Vue.js ایپس کامیابی سے تعمیر ہوتی ہیں
- چیک کریں کہ دستاویزات کے لنکس کام کرتے ہیں
- اگر ترمیم کی گئی ہو تو کوئز ایپلیکیشن کی جانچ کریں
- تصدیق کریں کہ ترجمے مستقل ڈھانچے کو برقرار رکھتے ہیں

### ترجمہ میں تعاون
- موجودہ کوڈ اسٹائل اور پیٹرنز پر عمل کریں
- پیچیدہ منطق کے لیے وضاحتی تبصرے شامل کریں
- متعلقہ دستاویزات کو اپ ڈیٹ کریں
- اگر قابل اطلاق ہو تو مختلف سبق ماڈیولز میں تبدیلیوں کی جانچ کریں
- CONTRIBUTING.md فائل کا جائزہ لیں

## اضافی نوٹس

### عام استعمال شدہ لائبریریاں
- **pandas**: ڈیٹا ہیرا پھیری اور تجزیہ
- **numpy**: عددی کمپیوٹنگ
- **matplotlib**: ڈیٹا بصریات اور پلاٹنگ
- **seaborn**: شماریاتی ڈیٹا بصریات (کچھ اسباق)
- **scikit-learn**: مشین لرننگ (اعلی درجے کے اسباق)

### ڈیٹا فائلز کے ساتھ کام کرنا
- ڈیٹا فائلز `data/` فولڈر یا سبق مخصوص ڈائریکٹریز میں واقع ہیں
- زیادہ تر نوٹ بکس ڈیٹا فائلز کو رشتہ دار راستوں میں توقع کرتے ہیں
- CSV فائلز بنیادی ڈیٹا فارمیٹ ہیں
- کچھ اسباق غیر رشتہ دار ڈیٹا مثالوں کے لیے JSON استعمال کرتے ہیں

### کثیر لسانی حمایت
- 40+ زبانوں کے ترجمے خودکار GitHub Actions کے ذریعے
- ترجمہ ورک فلو `.github/workflows/co-op-translator.yml` میں
- ترجمے `translations/` فولڈر میں زبان کے کوڈز کے ساتھ
- کوئز ترجمے `quiz-app/src/assets/translations/` میں

### ترقیاتی ماحول کے اختیارات
1. **مقامی ترقی**: Python، Jupyter، Node.js مقامی طور پر انسٹال کریں
2. **GitHub Codespaces**: کلاؤڈ پر مبنی فوری ترقیاتی ماحول
3. **VS Code Dev Containers**: مقامی کنٹینر پر مبنی ترقی
4. **Binder**: کلاؤڈ میں نوٹ بکس لانچ کریں (اگر کنفیگر کیا گیا ہو)

### سبق مواد کی گائیڈ لائنز
- ہر سبق خود مختار ہے لیکن پچھلے تصورات پر مبنی ہے
- سبق سے پہلے کے کوئزز پہلے علم کی جانچ کرتے ہیں
- سبق کے بعد کے کوئزز سیکھنے کو مضبوط کرتے ہیں
- اسائنمنٹس عملی مشق فراہم کرتے ہیں
- اسکیچ نوٹس بصری خلاصے فراہم کرتے ہیں

### عام مسائل کا حل

**جیوپیٹر کرنل کے مسائل:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**npm انسٹال کی ناکامی:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**نوٹ بکس میں درآمد کی غلطیاں:**
- تصدیق کریں کہ تمام مطلوبہ لائبریریاں انسٹال ہیں
- پائتھن ورژن کی مطابقت چیک کریں (Python 3.7+ تجویز کردہ)
- یقینی بنائیں کہ ورچوئل ماحول فعال ہے

**Docsify لوڈ نہیں ہو رہا:**
- تصدیق کریں کہ آپ ریپوزیٹری روٹ سے سرور کر رہے ہیں
- چیک کریں کہ `index.html` موجود ہے
- مناسب نیٹ ورک رسائی کو یقینی بنائیں (پورٹ 3000)

### کارکردگی کے تحفظات
- بڑے ڈیٹا سیٹس نوٹ بکس میں لوڈ ہونے میں وقت لے سکتے ہیں
- پیچیدہ پلاٹس کے لیے بصریات کی رینڈرنگ سست ہو سکتی ہے
- Vue.js ڈیولپمنٹ سرور فوری تکرار کے لیے ہاٹ ری لوڈ فعال کرتا ہے
- پروڈکشن بلڈز کو بہتر اور کم کیا جاتا ہے

### سیکیورٹی نوٹس
- کوئی حساس ڈیٹا یا اسناد کمیٹ نہیں کی جانی چاہیے
- کلاؤڈ اسباق میں کسی بھی API کیز کے لیے ماحول متغیرات استعمال کریں
- Azure سے متعلق اسباق کو Azure اکاؤنٹ کی اسناد کی ضرورت ہو سکتی ہے
- سیکیورٹی پیچز کے لیے انحصار کو اپ ڈیٹ رکھیں

## ترجموں میں تعاون
- خودکار ترجمے GitHub Actions کے ذریعے منظم کیے گئے
- ترجمے کی درستگی کے لیے دستی اصلاحات کا خیر مقدم ہے
- موجودہ ترجمہ فولڈر ڈھانچے پر عمل کریں
- کوئز لنکس کو زبان کے پیرامیٹر کے ساتھ اپ ڈیٹ کریں: `?loc=fr`
- ترجمہ شدہ اسباق کی درست رینڈرنگ کے لیے جانچ کریں

## متعلقہ وسائل
- مرکزی نصاب: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- اسٹوڈنٹ ہب: https://docs.microsoft.com/learn/student-hub
- بحث فورم: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- دیگر Microsoft نصاب: ML for Beginners، AI for Beginners، Web Dev for Beginners

## پروجیکٹ کی دیکھ بھال
- مواد کو موجودہ رکھنے کے لیے باقاعدہ اپ ڈیٹس
- کمیونٹی تعاون کا خیر مقدم ہے
- مسائل GitHub پر ٹریک کیے گئے
- پی آرز نصاب کے منتظمین کے ذریعے جائزہ لیا گیا
- ماہانہ مواد کے جائزے اور اپ ڈیٹس

---

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا خامیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔