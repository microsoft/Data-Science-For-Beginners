<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "33d252f7491b696d85df7f680e7e7b90",
  "translation_date": "2026-01-16T09:17:01+00:00",
  "source_file": "README.md",
  "language_code": "fa"
}
-->
# علم داده برای مبتدیان - یک برنامه درسی

[![باز کردن در GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=344191198)

[![مجوز GitHub](https://img.shields.io/github/license/microsoft/Data-Science-For-Beginners.svg)](https://github.com/microsoft/Data-Science-For-Beginners/blob/master/LICENSE)
[![همکاران GitHub](https://img.shields.io/github/contributors/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/graphs/contributors/)
[![مسائل GitHub](https://img.shields.io/github/issues/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/issues/)
[![درخواست‌های کشش GitHub](https://img.shields.io/github/issues-pr/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/pulls/)
[![درخواست‌های کشش خوش آمدید](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![ناظرین GitHub](https://img.shields.io/github/watchers/microsoft/Data-Science-For-Beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/Data-Science-For-Beginners/watchers/)
[![شاخه‌ها GitHub](https://img.shields.io/github/forks/microsoft/Data-Science-For-Beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/Data-Science-For-Beginners/network/)
[![ستاره‌ها GitHub](https://img.shields.io/github/stars/microsoft/Data-Science-For-Beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/Data-Science-For-Beginners/stargazers/)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![انجمن توسعه‌دهندگان Microsoft Foundry](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

مدافعان ابر آزور در مایکروسافت مفتخرند که یک برنامه درسی ۱۰ هفته‌ای و شامل ۲۰ درس درباره علم داده ارائه دهند. هر درس شامل آزمون‌های قبل و بعد از درس، دستورالعمل‌های مکتوب برای انجام درس، یک راه‌حل و یک تکلیف است. روش آموزشی ما مبتنی بر پروژه به شما امکان می‌دهد همزمان با ساخت پروژه‌ها یاد بگیرید؛ روشی اثبات‌شده برای تثبیت مهارت‌های جدید.

**از نویسندگان عزیزمان صمیمانه تشکر می‌کنیم:** [Jasmine Greenaway](https://www.twitter.com/paladique)، [Dmitry Soshnikov](http://soshnikov.com)، [Nitya Narasimhan](https://twitter.com/nitya)، [Jalen McGee](https://twitter.com/JalenMcG)، [Jen Looper](https://twitter.com/jenlooper)، [Maud Levy](https://twitter.com/maudstweets)، [Tiffany Souterre](https://twitter.com/TiffanySouterre)، [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏 تشکر ویژه 🙏 از نویسندگان، بازبینان و مشارکت‌کنندگان محتوا از [سفیران دانشجویی مایکروسافت](https://studentambassadors.microsoft.com/)،** به ویژه آریان آرورا، [Aditya Garg](https://github.com/AdityaGarg00)، [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/)، [Ankita Singh](https://www.linkedin.com/in/ankitasingh007)، [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/)، [Arpita Das](https://www.linkedin.com/in/arpitadas01/)، ChhailBihari Dubey، [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor)، [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb)، [Majd Safi](https://www.linkedin.com/in/majd-s/)، [Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/)، [Miguel Correa](https://www.linkedin.com/in/miguelmque/)، [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119)، [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum)، [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/)، [Rohit Yadav](https://www.linkedin.com/in/rty2423)، Samridhi Sharma، [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200)،
[Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/)، [Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/)، Yogendrasingh Pawar، [Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/)، [Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![تصویر یادداشت دستی ساخته شده توسط @sketchthedocs https://sketchthedocs.dev](../../../../translated_images/fa/00-Title.8af36cd35da1ac55.webp)|
|:---:|
| علم داده برای مبتدیان - _یادداشت دستی توسط [@nitya](https://twitter.com/nitya)_ |

### 🌐 پشتیبانی چندزبانه

#### پشتیبانی شده توسط GitHub Action (خودکار و همیشه به‌روز)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](./README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ترجیح می‌دهید محلی کلون کنید؟**

> این مخزن شامل بیش از ۵۰ ترجمه زبان است که اندازه دانلود را به طور قابل توجهی افزایش می‌دهد. برای کلون کردن بدون ترجمه‌ها، از sparse checkout استفاده کنید:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Data-Science-For-Beginners.git
> cd Data-Science-For-Beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> این به شما همه چیز را می‌دهد تا دوره را کامل کنید با سرعت دانلود بسیار سریع‌تر.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**اگر مایلید زبان‌های ترجمه بیشتری پشتیبانی شوند، فهرست آن‌ها در [اینجا](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) موجود است**

#### به جامعه ما بپیوندید
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

ما یک سری آموزش Discord با موضوع یادگیری با هوش مصنوعی داریم، برای کسب اطلاعات بیشتر و پیوستن به ما به [سری آموزش با هوش مصنوعی](https://aka.ms/learnwithai/discord) از ۱۸ تا ۳۰ سپتامبر ۲۰۲۵ مراجعه کنید. نکات و ترفندهایی برای استفاده از GitHub Copilot در علم داده دریافت خواهید کرد.

![سری آموزش با هوش مصنوعی](../../../../translated_images/fa/1.2b28cdc6205e26fe.webp)

# آیا دانشجو هستید؟

برای شروع از منابع زیر استفاده کنید:

- [صفحه مرکز دانشجویی](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) در این صفحه منابع مبتدی، بسته‌های دانشجویی و حتی روش‌هایی برای دریافت کوپن رایگان گواهینامه را خواهید یافت. این صفحه‌ای است که می‌خواهید در نشانه‌گذاری خود داشته باشید و هر از چندگاهی بررسی کنید زیرا حداقل ماهانه محتوا را به‌روزرسانی می‌کنیم.
- [سفیران دانشجویی مایکروسافت](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) به یک جامعه جهانی از سفیران دانشجویی بپیوندید؛ این می‌تواند راه ورود شما به مایکروسافت باشد.

# شروع به کار

## 📚 مستندات

- **[راهنمای نصب](INSTALLATION.md)** - دستورالعمل‌های گام به گام برای راه‌اندازی برای مبتدیان
- **[راهنمای استفاده](USAGE.md)** - مثال‌ها و جریان‌های کاری رایج
- **[عیب‌یابی](TROUBLESHOOTING.md)** - راه‌حل‌های مشکلات رایج
- **[راهنمای مشارکت](CONTRIBUTING.md)** - چگونه در این پروژه مشارکت کنید
- **[برای معلمان](for-teachers.md)** - راهنمای تدریس و منابع کلاسی

## 👨‍🎓 برای دانشجویان
> **کاملاً مبتدی:** تازه با علم داده آشنا شده‌اید؟ با [مثال‌های دوستانه برای مبتدیان](examples/README.md) ما شروع کنید! این مثال‌های ساده و دارای توضیح به شما کمک می‌کند مبانی را درک کنید قبل از اینکه به کل برنامه درسی بپردازید.
> **[دانشجویان](https://aka.ms/student-page):** برای استفاده از این برنامه درسی به تنهایی، کل مخزن را فورک کنید و تمرین‌ها را به ترتیب انجام دهید، با یک آزمون قبل از درس شروع کنید. سپس درس را بخوانید و بقیه فعالیت‌ها را انجام دهید. تلاش کنید پروژه‌ها را با درک درس‌ها بسازید نه صرفاً کپی کردن کد راه‌حل؛ هرچند کد راه‌حل در پوشه /solutions در هر درس مبتنی بر پروژه موجود است. ایده دیگر تشکیل گروه مطالعه با دوستان و طی کردن محتوا با هم است. برای مطالعه بیشتر، [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum) را توصیه می‌کنیم.

**شروع سریع:**
1. برای راه‌اندازی محیط خود، [راهنمای نصب](INSTALLATION.md) را بررسی کنید
2. برای یادگیری نحوه کار با برنامه درسی، [راهنمای استفاده](USAGE.md) را مرور کنید
3. با درس ۱ شروع کرده و به ترتیب ادامه دهید
4. برای پشتیبانی به [جامعه Discord ما](https://aka.ms/ds4beginners/discord) بپیوندید

## 👩‍🏫 برای معلمان

> **معلمان:** ما [برخی پیشنهادها](for-teachers.md) را درباره چگونگی استفاده از این برنامه درسی ارائه داده‌ایم. مشتاقانه منتظر بازخورد شما در [انجمن بحث ما](https://github.com/microsoft/Data-Science-For-Beginners/discussions) هستیم!

## تیم را ملاقات کنید
[![ویدئوی تبلیغاتی](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "ویدئوی تبلیغاتی")

**گیف توسط** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)

> 🎥 برای مشاهده ویدئویی درباره پروژه و افرادی که آن را ایجاد کرده‌اند، روی تصویر بالا کلیک کنید!

## روش آموزشی

در ساخت این برنامه درسی دو اصل آموزشی را انتخاب کرده‌ایم: اطمینان از اینکه مبتنی بر پروژه باشد و شامل آزمون‌های مکرر باشد. تا پایان این مجموعه، دانش‌آموزان اصول پایه‌ای علم داده را خواهند آموخت، از جمله مفاهیم اخلاقی، آماده‌سازی داده‌ها، روش‌های مختلف کار با داده، تجسم داده، تحلیل داده، موارد کاربرد واقعی علم داده و موارد بیشتر.

علاوه بر این، یک آزمون کم‌ریسک قبل از کلاس قصد دانش‌آموز برای یادگیری یک موضوع را تنظیم می‌کند، در حالی که پس از کلاس آزمون دوم به حفظ بهتر مطالب کمک می‌کند. این برنامه درسی برای انعطاف‌پذیری و سرگرمی طراحی شده است و می‌توان آن را به‌صورت کامل یا جزئی گذراند. پروژه‌ها از ساده شروع شده و تا پایان دوره ۱۰ هفته‌ای پیچیده‌تر می‌شوند.

> راهنمای [قوانین رفتار](CODE_OF_CONDUCT.md)، [مشارکت](CONTRIBUTING.md)، [ترجمه](TRANSLATIONS.md) ما را بیابید. ما از بازخورد سازنده شما استقبال می‌کنیم!

## هر درس شامل موارد زیر است:

- یادداشت اسکیچ اختیاری
- ویدئوی تکمیلی اختیاری
- آزمون گرم‌کردن قبل از درس
- درس مکتوب
- در دروس مبتنی بر پروژه، راهنمای مرحله به مرحله برای ساخت پروژه
- بررسی دانش
- یک چالش
- مطالعات تکمیلی
- تمرین
- [آزمون پس از درس](https://ff-quizzes.netlify.app/en/)

> **یک نکته درباره آزمون‌ها**: همه آزمون‌ها در پوشه Quiz-App قرار دارند، مجموعاً ۴۰ آزمون با سه سوال هر کدام. این آزمون‌ها در داخل دروس لینک شده‌اند، اما می‌توان برنامه آزمون را به صورت محلی اجرا کرد یا در Azure مستقر نمود؛ دستورالعمل‌ها در پوشه `quiz-app` موجود است. این آزمون‌ها به تدریج بومی‌سازی می‌شوند.

## 🎓 مثال‌های مناسب مبتدیان

**تازه‌کار در علم داده؟** ما یک [دایرکتوری مثال‌ها](examples/README.md) ویژه با کدهای ساده و خوب توضیح داده شده ایجاد کرده‌ایم تا به شما کمک کند شروع کنید:

- 🌟 **سلام دنیا** - اولین برنامه علم داده شما
- 📂 **بارگذاری داده‌ها** - یادگیری خواندن و بررسی مجموعه داده‌ها
- 📊 **تحلیل ساده** - محاسبه آمار و یافتن الگوها
- 📈 **تجسم پایه‌ای** - ساخت نمودارها و گراف‌ها
- 🔬 **پروژه واقعی** - جریان کاری کامل از ابتدا تا پایان

هر مثال شامل توضیحات دقیق برای هر مرحله است، که آن را برای مبتدیان مطلق ایده‌آل می‌کند!

👉 **[شروع با مثال‌ها](examples/README.md)** 👈

## دروس


|![ یادداشت اسکیچ توسط @sketchthedocs https://sketchthedocs.dev](../../../../translated_images/fa/00-Roadmap.4905d6567dff4753.webp)|
|:---:|
| علم داده برای مبتدیان: نقشه راه - _یادداشت اسکیچ توسط [@nitya](https://twitter.com/nitya)_ |


| شماره درس | موضوع | گروه درس | اهداف یادگیری | درس مرتبط | نویسنده |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| ۰۱ | تعریف علم داده | [مقدمه](1-Introduction/README.md) | آشنایی با مفاهیم پایه علم داده و ارتباط آن با هوش مصنوعی، یادگیری ماشین و داده‌های بزرگ. | [درس](1-Introduction/01-defining-data-science/README.md) [ویدئو](https://youtu.be/beZ7Mb_oz9I) | [دیمیترای](http://soshnikov.com) |
| ۰۲ | اخلاق علم داده | [مقدمه](1-Introduction/README.md) | مفاهیم، چالش‌ها و چارچوب‌های اخلاق داده. | [درس](1-Introduction/02-ethics/README.md) | [نیتیا](https://twitter.com/nitya) |
| ۰۳ | تعریف داده | [مقدمه](1-Introduction/README.md) | چگونه داده‌ها دسته‌بندی می‌شوند و منابع رایج آن‌ها. | [درس](1-Introduction/03-defining-data/README.md) | [جاسمین](https://www.twitter.com/paladique) |
| ۰۴ | مقدمه‌ای بر آمار و احتمال | [مقدمه](1-Introduction/README.md) | تکنیک‌های ریاضی احتمال و آمار برای درک داده‌ها. | [درس](1-Introduction/04-stats-and-probability/README.md) [ویدئو](https://youtu.be/Z5Zy85g4Yjw) | [دیمیترای](http://soshnikov.com) |
| ۰۵ | کار با داده‌های رابطه‌ای | [کار با داده](2-Working-With-Data/README.md) | مقدمه‌ای بر داده‌های رابطه‌ای و اصول کاوش و تحلیل این داده‌ها با زبان ساخت‌یافته پرس‌وجو، معروف به SQL ("سی‌کوئل"). | [درس](2-Working-With-Data/05-relational-databases/README.md) | [کریستوفر](https://www.twitter.com/geektrainer) | | |
| ۰۶ | کار با داده‌های NoSQL | [کار با داده](2-Working-With-Data/README.md) | مقدمه‌ای بر داده‌های غیررابطه‌ای، انواع مختلف آن و مبانی کاوش و تحلیل پایگاه داده‌های اسنادی. | [درس](2-Working-With-Data/06-non-relational/README.md) | [جاسمین](https://twitter.com/paladique)|
| ۰۷ | کار با پایتون | [کار با داده](2-Working-With-Data/README.md) | اصول استفاده از پایتون برای کاوش داده‌ها با کتابخانه‌هایی مانند Pandas. آشنایی پایه با برنامه‌نویسی پایتون توصیه می‌شود. | [درس](2-Working-With-Data/07-python/README.md) [ویدئو](https://youtu.be/dZjWOGbsN4Y) | [دیمیترای](http://soshnikov.com) |
| ۰۸ | آماده‌سازی داده‌ها | [کار با داده](2-Working-With-Data/README.md) | موضوعات مربوط به تکنیک‌های پاک‌سازی و تبدیل داده برای مواجهه با چالش‌های داده‌های ناقص، نادرست یا کمبود اطلاعات. | [درس](2-Working-With-Data/08-data-preparation/README.md) | [جاسمین](https://www.twitter.com/paladique) |
| ۰۹ | تجسم مقادیر | [تجسم داده](3-Data-Visualization/README.md) | یادگیری استفاده از Matplotlib برای تجسم داده‌های پرندگان 🦆 | [درس](3-Data-Visualization/09-visualization-quantities/README.md) | [جن](https://twitter.com/jenlooper) |
| ۱۰ | تجسم توزیع داده‌ها | [تجسم داده](3-Data-Visualization/README.md) | تجسم مشاهدات و روندها در بازه‌ای مشخص. | [درس](3-Data-Visualization/10-visualization-distributions/README.md) | [جن](https://twitter.com/jenlooper) |
| ۱۱ | تجسم نسبت‌ها | [تجسم داده](3-Data-Visualization/README.md) | تجسم درصدهای گسسته و گروه‌بندی شده. | [درس](3-Data-Visualization/11-visualization-proportions/README.md) | [جن](https://twitter.com/jenlooper) |
| ۱۲ | تجسم روابط | [تجسم داده](3-Data-Visualization/README.md) | تجسم ارتباطات و همبستگی‌ها بین مجموعه‌های داده و متغیرهای آن‌ها. | [درس](3-Data-Visualization/12-visualization-relationships/README.md) | [جن](https://twitter.com/jenlooper) |
| ۱۳ | تجسم‌های معنادار | [تجسم داده](3-Data-Visualization/README.md) | تکنیک‌ها و راهنمایی برای ارزشمند کردن تجسم‌ها جهت حل مؤثر مسائل و کسب بینش‌ها. | [درس](3-Data-Visualization/13-meaningful-visualizations/README.md) | [جن](https://twitter.com/jenlooper) |
| ۱۴ | مقدمه‌ای بر چرخه زندگی علم داده | [چرخه زندگی](4-Data-Science-Lifecycle/README.md) | معرفی چرخه زندگی علم داده و اولین گام آن یعنی کسب و استخراج داده. | [درس](4-Data-Science-Lifecycle/14-Introduction/README.md) | [جاسمین](https://twitter.com/paladique) |
| ۱۵ | تحلیل | [چرخه زندگی](4-Data-Science-Lifecycle/README.md) | این مرحله از چرخه زندگی علم داده بر تکنیک‌های تحلیل داده متمرکز است. | [درس](4-Data-Science-Lifecycle/15-analyzing/README.md) | [جاسمین](https://twitter.com/paladique) | | |
| ۱۶ | ارتباطات | [چرخه زندگی](4-Data-Science-Lifecycle/README.md) | این مرحله از چرخه زندگی علم داده بر ارائه بینش‌های داده به طریقی که تصمیم‌گیرندگان به راحتی بفهمند، متمرکز است. | [درس](4-Data-Science-Lifecycle/16-communication/README.md) | [جالن](https://twitter.com/JalenMcG) | | |
| ۱۷ | علم داده در فضای ابری | [داده ابری](5-Data-Science-In-Cloud/README.md) | این مجموعه درس‌ها علم داده در فضای ابری و مزایای آن را معرفی می‌کند. | [درس](5-Data-Science-In-Cloud/17-Introduction/README.md) | [تیفانی](https://twitter.com/TiffanySouterre) و [ماود](https://twitter.com/maudstweets) |
| ۱۸ | علم داده در فضای ابری | [داده ابری](5-Data-Science-In-Cloud/README.md) | آموزش مدل‌ها با استفاده از ابزارهای کد پایین. |[درس](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [تیفانی](https://twitter.com/TiffanySouterre) و [ماود](https://twitter.com/maudstweets) |
| ۱۹ | علم داده در فضای ابری | [داده ابری](5-Data-Science-In-Cloud/README.md) | استقرار مدل‌ها با استفاده از Azure Machine Learning Studio. | [درس](5-Data-Science-In-Cloud/19-Azure/README.md)| [تیفانی](https://twitter.com/TiffanySouterre) و [ماود](https://twitter.com/maudstweets) |
| ۲۰ | علم داده در دنیای واقعی | [در دنیای واقعی](6-Data-Science-In-Wild/README.md) | پروژه‌های مبتنی بر علم داده در دنیای واقعی. | [درس](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [نیتیا](https://twitter.com/nitya) |

## گیت‌هاب کدسپیس

برای باز کردن این نمونه در یک Codespace مراحل زیر را دنبال کنید:
۱. منوی کشویی Code را کلیک کنید و گزینه Open with Codespaces را انتخاب کنید.
۲. در پایین پنل گزینه + New codespace را انتخاب کنید.
برای اطلاعات بیشتر، مستندات [GitHub](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace) را بررسی کنید.

## VSCode Remote - Containers
برای باز کردن این مخزن در یک کانتینر با استفاده از دستگاه محلی و VSCode با افزونه VS Code Remote - Containers مراحل زیر را دنبال کنید:

۱. اگر برای اولین بار است که از یک کانتینر توسعه استفاده می‌کنید، لطفاً اطمینان حاصل کنید که سیستم شما پیش‌نیازها را دارد (مثلاً Docker نصب شده باشد) در [مستندات شروع](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started).

برای استفاده از این مخزن، می‌توانید مخزن را در یک volume ایزوله Docker باز کنید:

**توجه**: در پشت صحنه، این از فرمان Remote-Containers: **Clone Repository in Container Volume...** استفاده می‌کند تا کد منبع را در یک volume داکر کپی کند نه در سیستم فایل محلی. [Volumeها](https://docs.docker.com/storage/volumes/) مکانیزم ترجیحی برای حفظ داده‌های کانتینر هستند.

یا نسخه‌ای که به‌صورت محلی کلون یا دانلود شده است را باز کنید:

- این مخزن را در سیستم فایل محلی خود کلون کنید.
- کلید F1 را فشار دهید و فرمان **Remote-Containers: Open Folder in Container...** را انتخاب کنید.
- نسخه کلون شده این پوشه را انتخاب کنید، منتظر شروع کانتینر بمانید و همه چیز را امتحان کنید.

## دسترسی آفلاین

می‌توانید این مستندات را به صورت آفلاین با استفاده از [Docsify](https://docsify.js.org/#/) اجرا کنید. این مخزن را فورک کنید، [Docsify را نصب کنید](https://docsify.js.org/#/quickstart) در رایانه محلی خود، سپس در پوشه ریشه این مخزن تایپ کنید `docsify serve`. وب‌سایت بر روی پورت ۳۰۰۰ در localhost شما سرو خواهد شد: `localhost:3000`.

> توجه، دفترچه‌ها از طریق Docsify رندر نمی‌شوند، بنابراین هر زمان نیاز به اجرای یک دفترچه یادداشت داشتید، آن را جداگانه در VS Code با اجرای هسته Python انجام دهید.

## برنامه‌های درسی دیگر

تیم ما برنامه‌های درسی دیگری تولید می‌کند! نگاهی بیندازید به:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j برای مبتدیان](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js برای مبتدیان](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD برای مبتدیان](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI برای مبتدیان](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP برای مبتدیان](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents برای مبتدیان](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### سری هوش مصنوعی مولد
[![هوش مصنوعی مولد برای مبتدیان](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![هوش مصنوعی مولد (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![هوش مصنوعی مولد (جاوا)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![هوش مصنوعی مولد (جاوااسکریپت)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### یادگیری پایه
[![یادگیری ماشین برای مبتدیان](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![علم داده برای مبتدیان](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![هوش مصنوعی برای مبتدیان](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![امنیت سایبری برای مبتدیان](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![توسعه وب برای مبتدیان](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![اینترنت اشیاء برای مبتدیان](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![توسعه XR برای مبتدیان](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### سری کاپیلوت
[![کاپیلوت برای برنامه‌نویسی جفتی هوش مصنوعی](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![کاپیلوت برای C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![ماجراجویی کاپیلوت](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## دریافت کمک

**با مشکلات مواجه شده‌اید؟** راهنمای [عیب‌یابی](TROUBLESHOOTING.md) را برای راه‌حل مشکلات رایج بررسی کنید.

اگر گیر کردید یا سوالی درباره ساخت برنامه‌های هوش مصنوعی دارید، به همراه سایر یادگیرندگان و توسعه‌دهندگان با تجربه در بحث‌های مربوط به MCP شرکت کنید. این یک جامعه حمایتی است که سوالات در آن استقبال می‌شود و دانش به طور آزاد به اشتراک گذاشته می‌شود.

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

اگر بازخورد درباره محصول دارید یا هنگام ساخت با خطا مواجه شدید، به آدرس زیر مراجعه کنید:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است دارای خطاها یا نواقص باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا برداشت نادرستی ناشی از استفاده از این ترجمه نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->