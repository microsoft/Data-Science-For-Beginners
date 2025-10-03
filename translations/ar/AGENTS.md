<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:02:42+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ar"
}
-->
# AGENTS.md

## نظرة عامة على المشروع

"علم البيانات للمبتدئين" هو منهج شامل لمدة 10 أسابيع و20 درسًا تم إنشاؤه بواسطة Microsoft Azure Cloud Advocates. المستودع هو مورد تعليمي يشرح مفاهيم علم البيانات الأساسية من خلال دروس قائمة على المشاريع، بما في ذلك دفاتر Jupyter، اختبارات تفاعلية، وتكليفات عملية.

**التقنيات الرئيسية:**
- **دفاتر Jupyter**: الوسيلة التعليمية الأساسية باستخدام Python 3
- **مكتبات Python**: pandas، numpy، matplotlib لتحليل البيانات وتصويرها
- **Vue.js 2**: تطبيق الاختبارات (مجلد quiz-app)
- **Docsify**: مولد مواقع التوثيق للوصول دون اتصال
- **Node.js/npm**: إدارة الحزم لمكونات JavaScript
- **Markdown**: جميع محتويات الدروس والتوثيق

**الهيكلية:**
- مستودع تعليمي متعدد اللغات مع ترجمات واسعة النطاق
- مُنظم في وحدات دروس (من 1-Introduction إلى 6-Data-Science-In-Wild)
- كل درس يتضمن README، دفاتر، تكليفات، واختبارات
- تطبيق اختبارات مستقل باستخدام Vue.js لتقييم ما قبل/ما بعد الدرس
- دعم GitHub Codespaces وحاويات التطوير في VS Code

## أوامر الإعداد

### إعداد المستودع
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### إعداد بيئة Python
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### إعداد تطبيق الاختبارات
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

### خادم توثيق Docsify
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### إعداد مشاريع التصوير
بالنسبة لمشاريع التصوير مثل meaningful-visualizations (الدرس 13):
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


## سير العمل التطويري

### العمل مع دفاتر Jupyter
1. تشغيل Jupyter في جذر المستودع: `jupyter notebook`
2. الانتقال إلى مجلد الدرس المطلوب
3. فتح ملفات `.ipynb` للعمل على التمارين
4. الدفاتر مكتفية ذاتيًا مع شروحات وخلايا أكواد
5. معظم الدفاتر تستخدم pandas، numpy، وmatplotlib - تأكد من تثبيتها

### هيكلية الدرس
كل درس يحتوي عادةً على:
- `README.md` - محتوى الدرس الرئيسي مع النظرية والأمثلة
- `notebook.ipynb` - تمارين عملية باستخدام دفاتر Jupyter
- `assignment.ipynb` أو `assignment.md` - تكليفات عملية
- مجلد `solution/` - دفاتر الحلول والأكواد
- مجلد `images/` - مواد بصرية داعمة

### تطوير تطبيق الاختبارات
- تطبيق Vue.js 2 مع إعادة تحميل فوري أثناء التطوير
- الاختبارات مخزنة في `quiz-app/src/assets/translations/`
- لكل لغة مجلد ترجمة خاص بها (en، fr، es، إلخ)
- ترقيم الاختبارات يبدأ من 0 ويصل إلى 39 (40 اختبارًا إجمالاً)

### إضافة الترجمات
- الترجمات تُضاف في مجلد `translations/` في جذر المستودع
- لكل لغة هيكلية دروس كاملة مشابهة للإنجليزية
- ترجمة تلقائية عبر GitHub Actions (co-op-translator.yml)

## تعليمات الاختبار

### اختبار تطبيق الاختبارات
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### اختبار الدفاتر
- لا يوجد إطار اختبار تلقائي للدفاتر
- التحقق اليدوي: تشغيل جميع الخلايا بالتسلسل للتأكد من عدم وجود أخطاء
- التحقق من الوصول إلى ملفات البيانات وتوليد المخرجات بشكل صحيح
- التأكد من عرض التصورات بشكل صحيح

### اختبار التوثيق
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### فحوصات جودة الأكواد
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## إرشادات نمط الأكواد

### Python (دفاتر Jupyter)
- اتباع إرشادات نمط PEP 8 لأكواد Python
- استخدام أسماء متغيرات واضحة تشرح البيانات التي يتم تحليلها
- تضمين خلايا Markdown مع شروحات قبل خلايا الأكواد
- التركيز على مفاهيم أو عمليات محددة في خلايا الأكواد
- استخدام pandas لمعالجة البيانات، matplotlib للتصور
- نمط الاستيراد الشائع:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- اتباع دليل نمط Vue.js 2 وأفضل الممارسات
- تكوين ESLint في `quiz-app/package.json`
- استخدام مكونات Vue ذات الملف الواحد (.vue files)
- الحفاظ على هيكلية قائمة على المكونات
- تشغيل `npm run lint` قبل تقديم التغييرات

### توثيق Markdown
- استخدام تسلسل واضح للعناوين (# ## ### إلخ)
- تضمين كتل الأكواد مع محددات اللغة
- إضافة نصوص بديلة للصور
- الربط بالدروس والموارد ذات الصلة
- الحفاظ على طول السطور معقولًا لسهولة القراءة

### تنظيم الملفات
- محتوى الدروس في مجلدات مرقمة (01-defining-data-science، إلخ)
- الحلول في مجلدات فرعية مخصصة `solution/`
- الترجمات تعكس الهيكلية الإنجليزية في مجلد `translations/`
- الاحتفاظ بملفات البيانات في `data/` أو مجلدات خاصة بالدروس

## البناء والنشر

### نشر تطبيق الاختبارات
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### نشر تطبيقات Azure Static Web
يمكن نشر quiz-app على Azure Static Web Apps:
1. إنشاء مورد Azure Static Web App
2. الاتصال بمستودع GitHub
3. تكوين إعدادات البناء:
   - موقع التطبيق: `quiz-app`
   - موقع الإخراج: `dist`
4. سير عمل GitHub Actions سيقوم بالنشر تلقائيًا عند الدفع

### موقع التوثيق
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- المستودع يتضمن تكوين حاوية التطوير
- Codespaces يقوم تلقائيًا بإعداد بيئة Python وNode.js
- فتح المستودع في Codespace عبر واجهة GitHub
- تثبيت جميع التبعيات تلقائيًا

## إرشادات طلبات السحب

### قبل التقديم
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### تنسيق عنوان طلب السحب
- استخدام عناوين واضحة وواصفة
- التنسيق: `[المكون] وصف مختصر`
- أمثلة:
  - `[Lesson 7] إصلاح خطأ استيراد في دفتر Python`
  - `[Quiz App] إضافة ترجمة ألمانية`
  - `[Docs] تحديث README بمتطلبات جديدة`

### الفحوصات المطلوبة
- التأكد من تشغيل جميع الأكواد دون أخطاء
- التحقق من تنفيذ الدفاتر بالكامل
- التأكد من بناء تطبيقات Vue.js بنجاح
- التحقق من عمل روابط التوثيق
- اختبار تطبيق الاختبارات إذا تم تعديله
- التحقق من الحفاظ على هيكلية الترجمات

### إرشادات المساهمة
- اتباع نمط الأكواد والأنماط الموجودة
- إضافة تعليقات تفسيرية للمنطق المعقد
- تحديث التوثيق ذي الصلة
- اختبار التغييرات عبر وحدات الدروس المختلفة إذا كان ذلك ممكنًا
- مراجعة ملف CONTRIBUTING.md

## ملاحظات إضافية

### المكتبات الشائعة الاستخدام
- **pandas**: معالجة وتحليل البيانات
- **numpy**: الحوسبة العددية
- **matplotlib**: التصور ورسم البيانات
- **seaborn**: التصور الإحصائي للبيانات (بعض الدروس)
- **scikit-learn**: التعلم الآلي (الدروس المتقدمة)

### العمل مع ملفات البيانات
- ملفات البيانات موجودة في مجلد `data/` أو مجلدات خاصة بالدروس
- معظم الدفاتر تتوقع ملفات البيانات في مسارات نسبية
- ملفات CSV هي تنسيق البيانات الأساسي
- بعض الدروس تستخدم JSON لأمثلة البيانات غير العلائقية

### دعم متعدد اللغات
- أكثر من 40 ترجمة لغوية عبر GitHub Actions تلقائيًا
- سير عمل الترجمة في `.github/workflows/co-op-translator.yml`
- الترجمات في مجلد `translations/` مع رموز اللغات
- ترجمات الاختبارات في `quiz-app/src/assets/translations/`

### خيارات بيئة التطوير
1. **التطوير المحلي**: تثبيت Python، Jupyter، Node.js محليًا
2. **GitHub Codespaces**: بيئة تطوير سحابية فورية
3. **VS Code Dev Containers**: تطوير محلي قائم على الحاويات
4. **Binder**: تشغيل الدفاتر في السحابة (إذا تم تكوينه)

### إرشادات محتوى الدروس
- كل درس مكتفٍ ذاتيًا ولكنه يبني على المفاهيم السابقة
- اختبارات ما قبل الدرس تختبر المعرفة السابقة
- اختبارات ما بعد الدرس تعزز التعلم
- التكليفات توفر ممارسة عملية
- الرسومات التخطيطية تقدم ملخصات بصرية

### استكشاف المشكلات الشائعة

**مشكلات Kernel في Jupyter:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**فشل تثبيت npm:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**أخطاء الاستيراد في الدفاتر:**
- التحقق من تثبيت جميع المكتبات المطلوبة
- التحقق من توافق إصدار Python (يوصى بـ Python 3.7+)
- التأكد من تنشيط البيئة الافتراضية

**Docsify لا يعمل:**
- التحقق من أنك تقدم الخدمة من جذر المستودع
- التحقق من وجود `index.html`
- التأكد من الوصول الصحيح للشبكة (المنفذ 3000)

### اعتبارات الأداء
- قد تستغرق مجموعات البيانات الكبيرة وقتًا للتحميل في الدفاتر
- عرض التصورات قد يكون بطيئًا للرسومات المعقدة
- خادم التطوير في Vue.js يتيح إعادة تحميل فوري للتكرار السريع
- بناء الإنتاج يتم تحسينه وتصغيره

### ملاحظات الأمان
- لا يجب تقديم أي بيانات حساسة أو بيانات اعتماد
- استخدام متغيرات البيئة لأي مفاتيح API في دروس السحابة
- قد تتطلب دروس Azure بيانات اعتماد حساب Azure
- الحفاظ على تحديث التبعيات لتصحيحات الأمان

## المساهمة في الترجمات
- الترجمات التلقائية تُدار عبر GitHub Actions
- التصحيحات اليدوية مرحب بها لتحسين دقة الترجمة
- اتباع هيكلية مجلدات الترجمة الموجودة
- تحديث روابط الاختبارات لتضمين معلمة اللغة: `?loc=fr`
- اختبار الدروس المترجمة للتأكد من عرضها بشكل صحيح

## الموارد ذات الصلة
- المنهج الرئيسي: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- مركز الطلاب: https://docs.microsoft.com/learn/student-hub
- منتدى المناقشة: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- مناهج Microsoft الأخرى: ML للمبتدئين، AI للمبتدئين، تطوير الويب للمبتدئين

## صيانة المشروع
- تحديثات منتظمة للحفاظ على المحتوى محدثًا
- مساهمات المجتمع مرحب بها
- تتبع المشكلات على GitHub
- مراجعة طلبات السحب بواسطة مشرفي المنهج
- مراجعات وتحديثات شهرية للمحتوى

---

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الموثوق. للحصول على معلومات حساسة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.