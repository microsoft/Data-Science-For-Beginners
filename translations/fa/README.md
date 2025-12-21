<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "210052dafe5b5d956c427824e2c96686",
  "translation_date": "2025-12-19T10:32:28+00:00",
  "source_file": "README.md",
  "language_code": "fa"
}
-->
# علوم داده برای مبتدیان - یک برنامه درسی

[![باز کردن در GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=344191198)

[![مجوز GitHub](https://img.shields.io/github/license/microsoft/Data-Science-For-Beginners.svg)](https://github.com/microsoft/Data-Science-For-Beginners/blob/master/LICENSE)
[![مشارکت‌کنندگان GitHub](https://img.shields.io/github/contributors/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/graphs/contributors/)
[![مسائل GitHub](https://img.shields.io/github/issues/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/issues/)
[![درخواست‌های کشش GitHub](https://img.shields.io/github/issues-pr/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/pulls/)
[![خوش آمدید به PRها](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![ناظرین GitHub](https://img.shields.io/github/watchers/microsoft/Data-Science-For-Beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/Data-Science-For-Beginners/watchers/)
[![شاخه‌های GitHub](https://img.shields.io/github/forks/microsoft/Data-Science-For-Beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/Data-Science-For-Beginners/network/)
[![ستاره‌های GitHub](https://img.shields.io/github/stars/microsoft/Data-Science-For-Beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/Data-Science-For-Beginners/stargazers/)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

مدافعان ابر آزور در مایکروسافت خوشحالند که یک برنامه درسی ۱۰ هفته‌ای با ۲۰ درس درباره علوم داده ارائه دهند. هر درس شامل آزمون‌های قبل و بعد از درس، دستورالعمل‌های مکتوب برای تکمیل درس، یک راه‌حل و یک تمرین است. روش آموزش مبتنی بر پروژه ما به شما اجازه می‌دهد در حین ساختن یاد بگیرید، روشی اثبات شده برای تثبیت مهارت‌های جدید.

**تشکر صمیمانه از نویسندگان ما:** [Jasmine Greenaway](https://www.twitter.com/paladique)، [Dmitry Soshnikov](http://soshnikov.com)، [Nitya Narasimhan](https://twitter.com/nitya)، [Jalen McGee](https://twitter.com/JalenMcG)، [Jen Looper](https://twitter.com/jenlooper)، [Maud Levy](https://twitter.com/maudstweets)، [Tiffany Souterre](https://twitter.com/TiffanySouterre)، [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏 تشکر ویژه 🙏 از نویسندگان، بازبینان و مشارکت‌کنندگان محتوا از [سفیران دانشجویی مایکروسافت](https://studentambassadors.microsoft.com/)،** به ویژه آریان آرورا، [Aditya Garg](https://github.com/AdityaGarg00)، [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/)، [Ankita Singh](https://www.linkedin.com/in/ankitasingh007)، [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/)، [Arpita Das](https://www.linkedin.com/in/arpitadas01/)، ChhailBihari Dubey، [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor)، [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb)، [Majd Safi](https://www.linkedin.com/in/majd-s/)، [Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/)، [Miguel Correa](https://www.linkedin.com/in/miguelmque/)، [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119)، [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum)، [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/)، [Rohit Yadav](https://www.linkedin.com/in/rty2423)، Samridhi Sharma، [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200)،
[Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/)، [Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/)، Yogendrasingh Pawar ، [Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/)، [Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![یادداشت تصویری توسط @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.fa.png)|
|:---:|
| علوم داده برای مبتدیان - _یادداشت تصویری توسط [@nitya](https://twitter.com/nitya)_ |

### 🌐 پشتیبانی چندزبانه

#### پشتیبانی شده از طریق GitHub Action (خودکار و همیشه به‌روز)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](./README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**اگر مایلید زبان‌های ترجمه بیشتری پشتیبانی شوند، فهرست آن‌ها را [اینجا](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) ببینید**

#### به جامعه ما بپیوندید
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

ما یک سری یادگیری با هوش مصنوعی در دیسکورد داریم، بیشتر بدانید و به ما بپیوندید در [سری یادگیری با هوش مصنوعی](https://aka.ms/learnwithai/discord) از ۱۸ تا ۳۰ سپتامبر ۲۰۲۵. نکات و ترفندهای استفاده از GitHub Copilot برای علوم داده را دریافت خواهید کرد.

![سری یادگیری با هوش مصنوعی](../../translated_images/1.2b28cdc6205e26fef6a21817fe5d83ae8b50fbd0a33e9fed0df05845da5b30b6.fa.jpg)

# آیا دانشجو هستید؟

با منابع زیر شروع کنید:

- [صفحه مرکز دانشجویی](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) در این صفحه منابع مبتدی، بسته‌های دانشجویی و حتی راه‌هایی برای دریافت کوپن رایگان گواهی را خواهید یافت. این صفحه‌ای است که می‌خواهید نشانک بزنید و هر از گاهی بررسی کنید چون حداقل ماهی یکبار محتوا را تغییر می‌دهیم.
- [سفیران دانشجویی مایکروسافت](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) به یک جامعه جهانی از سفیران دانشجویی بپیوندید، این می‌تواند راه شما به مایکروسافت باشد.

# شروع به کار

## 📚 مستندات

- **[راهنمای نصب](INSTALLATION.md)** - دستورالعمل‌های گام به گام برای مبتدیان
- **[راهنمای استفاده](USAGE.md)** - مثال‌ها و جریان‌های کاری رایج
- **[رفع اشکال](TROUBLESHOOTING.md)** - راه‌حل‌های مشکلات رایج
- **[راهنمای مشارکت](CONTRIBUTING.md)** - چگونه به این پروژه کمک کنیم
- **[برای معلمان](for-teachers.md)** - راهنمای تدریس و منابع کلاسی

## 👨‍🎓 برای دانشجویان
> **کاملاً مبتدی:** تازه وارد علوم داده هستید؟ با [مثال‌های مناسب مبتدیان](examples/README.md) ما شروع کنید! این مثال‌های ساده و با توضیحات خوب به شما کمک می‌کنند قبل از ورود به برنامه درسی کامل، اصول را درک کنید.
> **[دانشجویان](https://aka.ms/student-page):** برای استفاده از این برنامه درسی به صورت مستقل، کل مخزن را فورک کنید و تمرین‌ها را خودتان انجام دهید، با یک آزمون پیش‌درس شروع کنید. سپس درس را بخوانید و بقیه فعالیت‌ها را کامل کنید. سعی کنید پروژه‌ها را با درک درس‌ها بسازید نه کپی کردن کد راه‌حل؛ البته آن کد در پوشه /solutions در هر درس پروژه‌محور موجود است. ایده دیگر تشکیل گروه مطالعه با دوستان و مرور محتوا با هم است. برای مطالعه بیشتر، ما [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum) را توصیه می‌کنیم.

**شروع سریع:**
1. راهنمای [نصب](INSTALLATION.md) را برای راه‌اندازی محیط خود بررسی کنید
2. راهنمای [استفاده](USAGE.md) را برای یادگیری نحوه کار با برنامه درسی مرور کنید
3. با درس ۱ شروع کنید و به ترتیب پیش بروید
4. برای پشتیبانی به [جامعه دیسکورد ما](https://aka.ms/ds4beginners/discord) بپیوندید

## 👩‍🏫 برای معلمان

> **معلمان:** ما [چند پیشنهاد](for-teachers.md) درباره نحوه استفاده از این برنامه درسی ارائه داده‌ایم. خوشحال می‌شویم بازخورد شما را [در انجمن بحث ما](https://github.com/microsoft/Data-Science-For-Beginners/discussions) دریافت کنیم!

## تیم را ملاقات کنید

[![ویدئوی تبلیغاتی](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "ویدئوی تبلیغاتی")

**گیف توسط** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)
> 🎥 برای مشاهده ویدیو درباره پروژه و افرادی که آن را ساخته‌اند، روی تصویر بالا کلیک کنید!

## آموزش

ما در ساخت این برنامه درسی دو اصل آموزشی را انتخاب کرده‌ایم: اطمینان از پروژه‌محور بودن آن و گنجاندن آزمون‌های مکرر. تا پایان این سری، دانش‌آموزان اصول پایه‌ای علم داده را خواهند آموخت، از جمله مفاهیم اخلاقی، آماده‌سازی داده‌ها، روش‌های مختلف کار با داده‌ها، مصورسازی داده‌ها، تحلیل داده‌ها، کاربردهای واقعی علم داده و موارد بیشتر.

علاوه بر این، یک آزمون کم‌فشار قبل از کلاس، نیت دانش‌آموز را برای یادگیری یک موضوع تنظیم می‌کند، در حالی که آزمون دوم پس از کلاس، حفظ بیشتر مطالب را تضمین می‌کند. این برنامه درسی به گونه‌ای طراحی شده است که انعطاف‌پذیر و سرگرم‌کننده باشد و می‌توان آن را به طور کامل یا بخشی از آن را گذراند. پروژه‌ها از کوچک شروع شده و تا پایان چرخه ۱۰ هفته‌ای به تدریج پیچیده‌تر می‌شوند.

> دستورالعمل‌های [کد رفتار](CODE_OF_CONDUCT.md)، [مشارکت](CONTRIBUTING.md)، [ترجمه](TRANSLATIONS.md) ما را بیابید. ما از بازخورد سازنده شما استقبال می‌کنیم!

## هر درس شامل موارد زیر است:

- یادداشت تصویری اختیاری
- ویدیوی مکمل اختیاری
- آزمون گرم‌کننده قبل از درس
- درس مکتوب
- برای درس‌های پروژه‌محور، راهنمای گام‌به‌گام ساخت پروژه
- بررسی دانش
- یک چالش
- مطالعه مکمل
- تمرین
- [آزمون پس از درس](https://ff-quizzes.netlify.app/en/)

> **یادداشتی درباره آزمون‌ها**: همه آزمون‌ها در پوشه Quiz-App قرار دارند، شامل ۴۰ آزمون با سه سوال هر کدام. این آزمون‌ها از داخل درس‌ها لینک شده‌اند، اما اپلیکیشن آزمون می‌تواند به صورت محلی اجرا یا در Azure مستقر شود؛ دستورالعمل‌ها در پوشه `quiz-app` موجود است. این آزمون‌ها به تدریج بومی‌سازی می‌شوند.

## 🎓 مثال‌های مناسب مبتدیان

**جدید در علم داده؟** ما یک [دایرکتوری مثال‌ها](examples/README.md) ویژه با کد ساده و کامنت‌گذاری شده ایجاد کرده‌ایم تا به شما در شروع کمک کند:

- 🌟 **سلام دنیا** - اولین برنامه علم داده شما
- 📂 **بارگذاری داده‌ها** - یادگیری خواندن و کاوش مجموعه داده‌ها
- 📊 **تحلیل ساده** - محاسبه آمار و یافتن الگوها
- 📈 **مصورسازی پایه** - ایجاد نمودارها و گراف‌ها
- 🔬 **پروژه واقعی** - جریان کاری کامل از ابتدا تا پایان

هر مثال شامل توضیحات دقیق در مورد هر مرحله است، که آن را برای مبتدیان مطلق ایده‌آل می‌کند!

👉 **[شروع با مثال‌ها](examples/README.md)** 👈

## دروس


|![ یادداشت تصویری توسط @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Roadmap.4905d6567dff47532b9bfb8e0b8980fc6b0b1292eebb24181c1a9753b33bc0f5.fa.png)|
|:---:|
| علم داده برای مبتدیان: نقشه راه - _یادداشت تصویری توسط [@nitya](https://twitter.com/nitya)_ |


| شماره درس | موضوع | گروه درس | اهداف یادگیری | درس مرتبط | نویسنده |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| ۰۱ | تعریف علم داده | [مقدمه](1-Introduction/README.md) | یادگیری مفاهیم پایه علم داده و ارتباط آن با هوش مصنوعی، یادگیری ماشین و داده‌های بزرگ. | [درس](1-Introduction/01-defining-data-science/README.md) [ویدیو](https://youtu.be/beZ7Mb_oz9I) | [دیمیتری](http://soshnikov.com) |
| ۰۲ | اخلاق علم داده | [مقدمه](1-Introduction/README.md) | مفاهیم، چالش‌ها و چارچوب‌های اخلاق داده. | [درس](1-Introduction/02-ethics/README.md) | [نیتیا](https://twitter.com/nitya) |
| ۰۳ | تعریف داده | [مقدمه](1-Introduction/README.md) | چگونگی طبقه‌بندی داده‌ها و منابع رایج آن‌ها. | [درس](1-Introduction/03-defining-data/README.md) | [جاسمین](https://www.twitter.com/paladique) |
| ۰۴ | مقدمه‌ای بر آمار و احتمال | [مقدمه](1-Introduction/README.md) | تکنیک‌های ریاضی احتمال و آمار برای درک داده‌ها. | [درس](1-Introduction/04-stats-and-probability/README.md) [ویدیو](https://youtu.be/Z5Zy85g4Yjw) | [دیمیتری](http://soshnikov.com) |
| ۰۵ | کار با داده‌های رابطه‌ای | [کار با داده](2-Working-With-Data/README.md) | مقدمه‌ای بر داده‌های رابطه‌ای و اصول کاوش و تحلیل داده‌های رابطه‌ای با زبان پرس‌وجوی ساختاریافته، معروف به SQL (تلفظ: سی‌کول). | [درس](2-Working-With-Data/05-relational-databases/README.md) | [کریستوفر](https://www.twitter.com/geektrainer) | | |
| ۰۶ | کار با داده‌های NoSQL | [کار با داده](2-Working-With-Data/README.md) | مقدمه‌ای بر داده‌های غیررابطه‌ای، انواع مختلف آن و اصول کاوش و تحلیل پایگاه‌های داده سندی. | [درس](2-Working-With-Data/06-non-relational/README.md) | [جاسمین](https://twitter.com/paladique)|
| ۰۷ | کار با پایتون | [کار با داده](2-Working-With-Data/README.md) | اصول استفاده از پایتون برای کاوش داده‌ها با کتابخانه‌هایی مانند Pandas. درک پایه‌ای برنامه‌نویسی پایتون توصیه می‌شود. | [درس](2-Working-With-Data/07-python/README.md) [ویدیو](https://youtu.be/dZjWOGbsN4Y) | [دیمیتری](http://soshnikov.com) |
| ۰۸ | آماده‌سازی داده | [کار با داده](2-Working-With-Data/README.md) | موضوعاتی درباره تکنیک‌های پاک‌سازی و تبدیل داده‌ها برای مقابله با چالش‌های داده‌های گمشده، نادرست یا ناقص. | [درس](2-Working-With-Data/08-data-preparation/README.md) | [جاسمین](https://www.twitter.com/paladique) |
| ۰۹ | مصورسازی مقادیر | [مصورسازی داده](3-Data-Visualization/README.md) | یادگیری استفاده از Matplotlib برای مصورسازی داده‌های پرندگان 🦆 | [درس](3-Data-Visualization/09-visualization-quantities/README.md) | [جن](https://twitter.com/jenlooper) |
| ۱۰ | مصورسازی توزیع داده‌ها | [مصورسازی داده](3-Data-Visualization/README.md) | مصورسازی مشاهدات و روندها در یک بازه زمانی. | [درس](3-Data-Visualization/10-visualization-distributions/README.md) | [جن](https://twitter.com/jenlooper) |
| ۱۱ | مصورسازی نسبت‌ها | [مصورسازی داده](3-Data-Visualization/README.md) | مصورسازی درصدهای گسسته و گروه‌بندی شده. | [درس](3-Data-Visualization/11-visualization-proportions/README.md) | [جن](https://twitter.com/jenlooper) |
| ۱۲ | مصورسازی روابط | [مصورسازی داده](3-Data-Visualization/README.md) | مصورسازی ارتباطات و همبستگی‌ها بین مجموعه داده‌ها و متغیرهای آن‌ها. | [درس](3-Data-Visualization/12-visualization-relationships/README.md) | [جن](https://twitter.com/jenlooper) |
| ۱۳ | مصورسازی‌های معنادار | [مصورسازی داده](3-Data-Visualization/README.md) | تکنیک‌ها و راهنمایی برای ارزشمند کردن مصورسازی‌ها برای حل موثر مشکلات و کسب بینش. | [درس](3-Data-Visualization/13-meaningful-visualizations/README.md) | [جن](https://twitter.com/jenlooper) |
| ۱۴ | مقدمه‌ای بر چرخه عمر علم داده | [چرخه عمر](4-Data-Science-Lifecycle/README.md) | مقدمه‌ای بر چرخه عمر علم داده و اولین مرحله آن یعنی کسب و استخراج داده‌ها. | [درس](4-Data-Science-Lifecycle/14-Introduction/README.md) | [جاسمین](https://twitter.com/paladique) |
| ۱۵ | تحلیل | [چرخه عمر](4-Data-Science-Lifecycle/README.md) | این مرحله از چرخه عمر علم داده بر تکنیک‌های تحلیل داده تمرکز دارد. | [درس](4-Data-Science-Lifecycle/15-analyzing/README.md) | [جاسمین](https://twitter.com/paladique) | | |
| ۱۶ | ارتباطات | [چرخه عمر](4-Data-Science-Lifecycle/README.md) | این مرحله از چرخه عمر علم داده بر ارائه بینش‌های داده به گونه‌ای که تصمیم‌گیرندگان راحت‌تر درک کنند، تمرکز دارد. | [درس](4-Data-Science-Lifecycle/16-communication/README.md) | [جالن](https://twitter.com/JalenMcG) | | |
| ۱۷ | علم داده در فضای ابری | [داده ابری](5-Data-Science-In-Cloud/README.md) | این سری دروس، علم داده در فضای ابری و مزایای آن را معرفی می‌کند. | [درس](5-Data-Science-In-Cloud/17-Introduction/README.md) | [تیفانی](https://twitter.com/TiffanySouterre) و [مود](https://twitter.com/maudstweets) |
| ۱۸ | علم داده در فضای ابری | [داده ابری](5-Data-Science-In-Cloud/README.md) | آموزش مدل‌ها با استفاده از ابزارهای کم‌کد. |[درس](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [تیفانی](https://twitter.com/TiffanySouterre) و [مود](https://twitter.com/maudstweets) |
| ۱۹ | علم داده در فضای ابری | [داده ابری](5-Data-Science-In-Cloud/README.md) | استقرار مدل‌ها با Azure Machine Learning Studio. | [درس](5-Data-Science-In-Cloud/19-Azure/README.md)| [تیفانی](https://twitter.com/TiffanySouterre) و [مود](https://twitter.com/maudstweets) |
| ۲۰ | علم داده در دنیای واقعی | [در دنیای واقعی](6-Data-Science-In-Wild/README.md) | پروژه‌های مبتنی بر علم داده در دنیای واقعی. | [درس](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [نیتیا](https://twitter.com/nitya) |

## GitHub Codespaces

برای باز کردن این نمونه در Codespace مراحل زیر را دنبال کنید:
۱. منوی کشویی Code را کلیک کرده و گزینه Open with Codespaces را انتخاب کنید.
۲. در پایین پنل، + New codespace را انتخاب کنید.
برای اطلاعات بیشتر، مستندات [GitHub](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace) را بررسی کنید.

## VSCode Remote - Containers
برای باز کردن این مخزن در یک کانتینر با استفاده از ماشین محلی و VSCode با استفاده از افزونه VS Code Remote - Containers مراحل زیر را دنبال کنید:

۱. اگر برای اولین بار است که از کانتینر توسعه استفاده می‌کنید، لطفاً اطمینان حاصل کنید که سیستم شما پیش‌نیازها (مانند نصب Docker) را دارد، در [مستندات شروع به کار](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started) آمده است.

برای استفاده از این مخزن، می‌توانید مخزن را در یک حجم جداگانه Docker باز کنید:

**توجه**: در پس‌زمینه، این از فرمان Remote-Containers: **Clone Repository in Container Volume...** برای کلون کردن کد منبع در یک حجم Docker به جای سیستم فایل محلی استفاده می‌کند. [حجم‌ها](https://docs.docker.com/storage/volumes/) مکانیزم ترجیحی برای حفظ داده‌های کانتینر هستند.

یا نسخه‌ای از مخزن که به صورت محلی کلون یا دانلود شده است را باز کنید:

- این مخزن را در سیستم فایل محلی خود کلون کنید.
- کلید F1 را فشار دهید و فرمان **Remote-Containers: Open Folder in Container...** را انتخاب کنید.
- نسخه کلون شده این پوشه را انتخاب کنید، منتظر بمانید تا کانتینر شروع شود و سپس کارها را امتحان کنید.

## دسترسی آفلاین

می‌توانید این مستندات را به صورت آفلاین با استفاده از [Docsify](https://docsify.js.org/#/) اجرا کنید. این مخزن را فورک کنید، [Docsify را نصب کنید](https://docsify.js.org/#/quickstart) روی ماشین محلی خود، سپس در پوشه ریشه این مخزن، دستور `docsify serve` را تایپ کنید. وب‌سایت روی پورت ۳۰۰۰ در لوکال‌هاست شما سرو خواهد شد: `localhost:3000`.

> توجه داشته باشید، دفترچه‌های یادداشت (notebooks) توسط Docsify رندر نمی‌شوند، بنابراین وقتی نیاز به اجرای دفترچه یادداشت دارید، آن را جداگانه در VS Code با کرنل پایتون اجرا کنید.

## برنامه‌های درسی دیگر

تیم ما برنامه‌های درسی دیگری نیز تولید می‌کند! بررسی کنید:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j برای مبتدیان](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js برای مبتدیان](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### سری هوش مصنوعی مولد
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### یادگیری پایه
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### سری کوپایلوت
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## دریافت کمک

**با مشکلی مواجه شده‌اید؟** راهنمای [عیب‌یابی](TROUBLESHOOTING.md) ما را برای راه‌حل مشکلات رایج بررسی کنید.

اگر گیر کردید یا سوالی درباره ساخت برنامه‌های هوش مصنوعی دارید، به جمع یادگیرندگان و توسعه‌دهندگان باتجربه در بحث‌های مربوط به MCP بپیوندید. این یک جامعه حمایتی است که سوالات در آن خوش‌آمد گفته می‌شود و دانش به‌صورت آزادانه به اشتراک گذاشته می‌شود.

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

اگر بازخورد محصول یا خطاهایی هنگام ساخت دارید، به اینجا مراجعه کنید:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->