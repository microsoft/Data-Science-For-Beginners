<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:03:39+00:00",
  "source_file": "AGENTS.md",
  "language_code": "fa"
}
-->
# AGENTS.md

## نمای کلی پروژه

داده‌کاوی برای مبتدیان یک برنامه آموزشی جامع ۱۰ هفته‌ای و ۲۰ درس است که توسط مدافعان ابری Microsoft Azure ایجاد شده است. این مخزن یک منبع آموزشی است که مفاهیم پایه‌ای داده‌کاوی را از طریق درس‌های مبتنی بر پروژه، شامل دفترچه‌های Jupyter، آزمون‌های تعاملی و تکالیف عملی آموزش می‌دهد.

**فناوری‌های کلیدی:**
- **دفترچه‌های Jupyter**: رسانه اصلی یادگیری با استفاده از Python 3
- **کتابخانه‌های پایتون**: pandas، numpy، matplotlib برای تحلیل داده‌ها و مصورسازی
- **Vue.js 2**: برنامه آزمون (پوشه quiz-app)
- **Docsify**: تولیدکننده سایت مستندات برای دسترسی آفلاین
- **Node.js/npm**: مدیریت بسته برای اجزای جاوااسکریپت
- **Markdown**: تمام محتوای درس‌ها و مستندات

**معماری:**
- مخزن آموزشی چندزبانه با ترجمه‌های گسترده
- ساختار یافته در ماژول‌های درس (۱-مقدمه تا ۶-داده‌کاوی در دنیای واقعی)
- هر درس شامل README، دفترچه‌ها، تکالیف و آزمون‌ها است
- برنامه آزمون مستقل Vue.js برای ارزیابی‌های قبل/بعد از درس
- پشتیبانی از GitHub Codespaces و کانتینرهای توسعه VS Code

## دستورات راه‌اندازی

### راه‌اندازی مخزن
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### راه‌اندازی محیط پایتون
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### راه‌اندازی برنامه آزمون
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

### سرور مستندات Docsify
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### راه‌اندازی پروژه‌های مصورسازی
برای پروژه‌های مصورسازی مانند meaningful-visualizations (درس ۱۳):
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


## جریان کاری توسعه

### کار با دفترچه‌های Jupyter
1. Jupyter را در ریشه مخزن شروع کنید: `jupyter notebook`
2. به پوشه درس مورد نظر بروید
3. فایل‌های `.ipynb` را باز کنید تا تمرین‌ها را انجام دهید
4. دفترچه‌ها خودکفا هستند و شامل توضیحات و سلول‌های کد می‌باشند
5. بیشتر دفترچه‌ها از pandas، numpy و matplotlib استفاده می‌کنند - مطمئن شوید که این‌ها نصب شده‌اند

### ساختار درس‌ها
هر درس معمولاً شامل موارد زیر است:
- `README.md` - محتوای اصلی درس با تئوری و مثال‌ها
- `notebook.ipynb` - تمرین‌های عملی دفترچه Jupyter
- `assignment.ipynb` یا `assignment.md` - تکالیف تمرینی
- پوشه `solution/` - دفترچه‌ها و کدهای حل تمرین
- پوشه `images/` - مواد بصری پشتیبان

### توسعه برنامه آزمون
- برنامه Vue.js 2 با قابلیت بارگذاری مجدد در زمان توسعه
- آزمون‌ها در `quiz-app/src/assets/translations/` ذخیره می‌شوند
- هر زبان پوشه ترجمه مخصوص به خود را دارد (en، fr، es و غیره)
- شماره‌گذاری آزمون‌ها از ۰ شروع شده و تا ۳۹ ادامه دارد (۴۰ آزمون در کل)

### افزودن ترجمه‌ها
- ترجمه‌ها در پوشه `translations/` در ریشه مخزن قرار می‌گیرند
- ساختار کامل درس‌ها از انگلیسی در هر زبان منعکس می‌شود
- ترجمه خودکار از طریق GitHub Actions (co-op-translator.yml)

## دستورالعمل‌های تست

### تست برنامه آزمون
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### تست دفترچه‌ها
- هیچ چارچوب تست خودکاری برای دفترچه‌ها وجود ندارد
- اعتبارسنجی دستی: تمام سلول‌ها را به ترتیب اجرا کنید تا مطمئن شوید خطایی وجود ندارد
- بررسی کنید که فایل‌های داده قابل دسترسی هستند و خروجی‌ها به درستی تولید می‌شوند
- مطمئن شوید که مصورسازی‌ها به درستی نمایش داده می‌شوند

### تست مستندات
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### بررسی کیفیت کد
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## دستورالعمل‌های سبک کدنویسی

### پایتون (دفترچه‌های Jupyter)
- از دستورالعمل‌های سبک PEP 8 برای کد پایتون پیروی کنید
- از نام‌های متغیر واضحی استفاده کنید که داده‌های تحلیل شده را توضیح دهند
- سلول‌های Markdown با توضیحات قبل از سلول‌های کد قرار دهید
- سلول‌های کد را بر روی مفاهیم یا عملیات‌های واحد متمرکز کنید
- از pandas برای دستکاری داده‌ها و matplotlib برای مصورسازی استفاده کنید
- الگوی وارد کردن معمول:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### جاوااسکریپت/Vue.js
- از دستورالعمل‌های سبک Vue.js 2 و بهترین شیوه‌ها پیروی کنید
- پیکربندی ESLint در `quiz-app/package.json`
- از اجزای تک‌فایلی Vue (.vue files) استفاده کنید
- معماری مبتنی بر اجزا را حفظ کنید
- قبل از ثبت تغییرات، `npm run lint` را اجرا کنید

### مستندات Markdown
- از سلسله‌مراتب واضح عناوین (# ## ### و غیره) استفاده کنید
- بلوک‌های کد با مشخص‌کننده زبان اضافه کنید
- متن جایگزین برای تصاویر اضافه کنید
- به درس‌ها و منابع مرتبط لینک دهید
- طول خطوط را برای خوانایی مناسب نگه دارید

### سازماندهی فایل‌ها
- محتوای درس‌ها در پوشه‌های شماره‌گذاری شده (01-defining-data-science و غیره)
- حل تمرین‌ها در زیرپوشه‌های اختصاصی `solution/`
- ترجمه‌ها ساختار انگلیسی را در پوشه `translations/` منعکس می‌کنند
- فایل‌های داده در `data/` یا پوشه‌های مخصوص درس نگهداری می‌شوند

## ساخت و استقرار

### استقرار برنامه آزمون
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### استقرار برنامه‌های وب ایستا Azure
برنامه آزمون می‌تواند در Azure Static Web Apps مستقر شود:
1. ایجاد منبع Azure Static Web App
2. اتصال به مخزن GitHub
3. تنظیمات ساخت را پیکربندی کنید:
   - مکان برنامه: `quiz-app`
   - مکان خروجی: `dist`
4. جریان کاری GitHub Actions به صورت خودکار با هر push مستقر می‌شود

### سایت مستندات
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- مخزن شامل پیکربندی کانتینر توسعه است
- Codespaces به صورت خودکار محیط Python و Node.js را تنظیم می‌کند
- مخزن را از طریق رابط کاربری GitHub در Codespace باز کنید
- تمام وابستگی‌ها به صورت خودکار نصب می‌شوند

## دستورالعمل‌های درخواست کشش (Pull Request)

### قبل از ارسال
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### قالب عنوان PR
- از عناوین واضح و توصیفی استفاده کنید
- قالب: `[Component] توضیح مختصر`
- مثال‌ها:
  - `[Lesson 7] رفع خطای وارد کردن دفترچه پایتون`
  - `[Quiz App] افزودن ترجمه آلمانی`
  - `[Docs] به‌روزرسانی README با پیش‌نیازهای جدید`

### بررسی‌های مورد نیاز
- مطمئن شوید که تمام کد بدون خطا اجرا می‌شود
- دفترچه‌ها را به طور کامل اجرا کنید
- اطمینان حاصل کنید که برنامه‌های Vue.js به درستی ساخته می‌شوند
- بررسی کنید که لینک‌های مستندات کار می‌کنند
- برنامه آزمون را در صورت تغییر تست کنید
- مطمئن شوید که ترجمه‌ها ساختار سازگار را حفظ می‌کنند

### دستورالعمل‌های مشارکت
- از سبک و الگوهای کدنویسی موجود پیروی کنید
- برای منطق پیچیده توضیحات اضافه کنید
- مستندات مرتبط را به‌روزرسانی کنید
- تغییرات را در ماژول‌های مختلف درس در صورت لزوم تست کنید
- فایل CONTRIBUTING.md را مرور کنید

## یادداشت‌های اضافی

### کتابخانه‌های رایج مورد استفاده
- **pandas**: دستکاری و تحلیل داده‌ها
- **numpy**: محاسبات عددی
- **matplotlib**: مصورسازی و نمودار داده‌ها
- **seaborn**: مصورسازی داده‌های آماری (برخی درس‌ها)
- **scikit-learn**: یادگیری ماشین (درس‌های پیشرفته)

### کار با فایل‌های داده
- فایل‌های داده در پوشه `data/` یا دایرکتوری‌های مخصوص درس قرار دارند
- بیشتر دفترچه‌ها فایل‌های داده را در مسیرهای نسبی انتظار دارند
- فایل‌های CSV فرمت اصلی داده هستند
- برخی درس‌ها از JSON برای مثال‌های داده غیررابطه‌ای استفاده می‌کنند

### پشتیبانی چندزبانه
- بیش از ۴۰ ترجمه زبان از طریق GitHub Actions خودکار
- جریان کاری ترجمه در `.github/workflows/co-op-translator.yml`
- ترجمه‌ها در پوشه `translations/` با کدهای زبان قرار دارند
- ترجمه‌های آزمون در `quiz-app/src/assets/translations/`

### گزینه‌های محیط توسعه
1. **توسعه محلی**: نصب Python، Jupyter، Node.js به صورت محلی
2. **GitHub Codespaces**: محیط توسعه ابری فوری
3. **کانتینرهای توسعه VS Code**: توسعه مبتنی بر کانتینر محلی
4. **Binder**: اجرای دفترچه‌ها در ابر (در صورت پیکربندی)

### دستورالعمل‌های محتوای درس
- هر درس مستقل است اما بر مفاهیم قبلی بنا می‌شود
- آزمون‌های قبل از درس دانش قبلی را ارزیابی می‌کنند
- آزمون‌های بعد از درس یادگیری را تقویت می‌کنند
- تکالیف تمرین عملی ارائه می‌دهند
- Sketchnotes خلاصه‌های بصری ارائه می‌دهند

### رفع مشکلات رایج

**مشکلات کرنل Jupyter:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**خطاهای نصب npm:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**خطاهای وارد کردن در دفترچه‌ها:**
- مطمئن شوید که تمام کتابخانه‌های مورد نیاز نصب شده‌اند
- سازگاری نسخه پایتون را بررسی کنید (پایتون ۳.۷+ توصیه می‌شود)
- مطمئن شوید که محیط مجازی فعال است

**Docsify بارگذاری نمی‌شود:**
- مطمئن شوید که از ریشه مخزن سرویس‌دهی می‌کنید
- بررسی کنید که `index.html` وجود دارد
- دسترسی شبکه مناسب را تضمین کنید (پورت ۳۰۰۰)

### ملاحظات عملکرد
- مجموعه داده‌های بزرگ ممکن است زمان بارگذاری در دفترچه‌ها طول بکشد
- نمایش مصورسازی‌ها ممکن است برای نمودارهای پیچیده کند باشد
- سرور توسعه Vue.js امکان بارگذاری مجدد سریع را فراهم می‌کند
- ساخت‌های تولید بهینه‌سازی و کوچک‌سازی شده‌اند

### یادداشت‌های امنیتی
- هیچ داده حساس یا اطلاعات کاربری نباید ثبت شود
- از متغیرهای محیطی برای هر کلید API در درس‌های ابری استفاده کنید
- درس‌های مرتبط با Azure ممکن است به اطلاعات حساب Azure نیاز داشته باشند
- وابستگی‌ها را برای وصله‌های امنیتی به‌روز نگه دارید

## مشارکت در ترجمه‌ها
- ترجمه‌های خودکار از طریق GitHub Actions مدیریت می‌شوند
- اصلاحات دستی برای دقت ترجمه استقبال می‌شود
- ساختار پوشه ترجمه موجود را دنبال کنید
- لینک‌های آزمون را به پارامتر زبان اضافه کنید: `?loc=fr`
- درس‌های ترجمه شده را برای نمایش صحیح تست کنید

## منابع مرتبط
- برنامه اصلی: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- مرکز دانش‌آموزی: https://docs.microsoft.com/learn/student-hub
- انجمن بحث: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- سایر برنامه‌های آموزشی Microsoft: ML برای مبتدیان، AI برای مبتدیان، توسعه وب برای مبتدیان

## نگهداری پروژه
- به‌روزرسانی‌های منظم برای حفظ محتوای به‌روز
- مشارکت‌های جامعه استقبال می‌شود
- مشکلات در GitHub پیگیری می‌شوند
- PRها توسط نگهدارندگان برنامه بررسی می‌شوند
- بررسی‌ها و به‌روزرسانی‌های ماهانه محتوا

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.