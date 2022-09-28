<div dir="rtl">
 
# علم داده برای مبتدیان - برنامه درسی


[![GitHub license](https://img.shields.io/github/license/microsoft/Data-Science-For-Beginners.svg)](https://github.com/microsoft/Data-Science-For-Beginners/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/Data-Science-For-Beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/Data-Science-For-Beginners/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/Data-Science-For-Beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/Data-Science-For-Beginners/network/)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/Data-Science-For-Beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/Data-Science-For-Beginners/stargazers/) 
 
طرفداران Azure Cloud در مایکروسافت مفتخر هستند که یک برنامه درسی 10 هفته ای و 20 درسی درباره علم داده ارائه دهند. هر درس شامل کوییزهای پیش از درس و پس از درس، دستورالعمل های کتبی برای تکمیل درس، راه حل و تکلیف است. آموزش پروژه محور ما به شما این امکان را می دهد در حین ساختن یاد بگیرید، راهی ثابت شده جهت "ماندگاری" مهارت های جدید.
 
**تشکر از صمیم قلب از نویسندگانمان:** [Jasmine Greenaway](https://www.twitter.com/paladique), [Dmitry Soshnikov](http://soshnikov.com), [Nitya Narasimhan](https://twitter.com/nitya), [Jalen McGee](https://twitter.com/JalenMcG), [Jen Looper](https://twitter.com/jenlooper), [Maud Levy](https://twitter.com/maudstweets), [Tiffany Souterre](https://twitter.com/TiffanySouterre), [Christopher Harrison](https://www.twitter.com/geektrainer).
 
**🙏 تشکر ویژه 🙏 از نویسندگان سفیر دانشجویی مایکروسافت، بازبینی کنندگان، و مشارکت کنندگان در محتوا،** به ویژه [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/), [Ankita Singh](https://www.linkedin.com/in/ankitasingh007), [Rohit Yadav](https://www.linkedin.com/in/rty2423), [Arpita Das](https://www.linkedin.com/in/arpitadas01/), [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119), [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [Miguel Correa](https://www.linkedin.com/in/miguelmque/), [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum), [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200), [Majd Safi](https://www.linkedin.com/in/majd-s/), [Sheena Narula](https://www.linkedin.com/in/sheena-narula-n/), [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/), [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor), [Aditya Garg](https://github.com/AdityaGarg00), [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/), Yogendrasingh Pawar, Max Blum, Samridhi Sharma, Tauqeer Ahmad, Aaryan Arora, ChhailBihari Dubey

 |![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../sketchnotes/00-Title.png)|
|:---:|
| علم داده برای مبتدیان - یادداشت بصری (sketchnote) از [@nitya](https://twitter.com/nitya)_ |


# شروع به کار

> **معلمان**، ما در مورد نحوه استفاده از این برنامه درسی [برخی از پیشنهادات را درج کرده ایم](../for-teachers.md).  بسیار خوشحال می شویم که بازخوردهای شما را در [انجمن بحث و گفت و گوی](https://github.com/microsoft/Data-Science-For-Beginners/discussions) خود داشته باشیم!

> **دانش آموزان**، اگر قصد دارید به تنهایی از این برنامه درسی استفاده کنید، کل مخزن را فورک کنید و تمرینات را خودتان به تنهایی انجام دهید. ابتدا با آزمون قبل از درس آغاز کنید، سپس درسنامه را خوانده و باقی فعالیت ها را تکمیل کنید. سعی کنید به جای کپی کردن کد راه حل، خودتان پروژه ها را با درک مفاهیم درسنامه ایجاد کنید. با این حال،کد راه حل در پوشه های /solutions داخل هر درس پروژه محور موجود می باشد. ایده دیگر تشکیل گروه مطالعه با دوستان است تا بتوانید مطالب را با هم مرور کنید، پیشنهاد ما [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum) می باشد.
 
<!--[![Promo video](../screenshot.png)]( "Promo video")

> 🎥 برای مشاهده ویدیویی در مورد این پروژه و افرادی که آن را ایجاد کرده اند، روی تصویر بالا کلیک کنید!-->
 

## آموزش

ما هنگام تدوین این برنامه درسی دو اصل آموزشی را انتخاب کرده ایم: اطمینان حاصل کنیم که پروژه محور است و شامل آزمونهای مکرر می باشد. دانش آموزان به محض تکمیل این سری آموزشی، اصول اولیه علم داده، شامل اصول اخلاقی، آماده سازی داده ها، روش های مختلف کار با داده ها، تصویرسازی داده ها، تجزیه و تحلیل داده ها، موارد استفاده از علم داده در دنیای واقعی و بسیاری مورد دیگر را فرا می گیرند.

علاوه بر این، یک کوییز با امتیاز کم قبل از کلاس، مقصود دانش آموز درجهت یادگیری یک موضوع را مشخص می کند، در حالی که کوییز دوم بعد از کلاس ماندگاری بیشتر مطالب را تضمین می کند. این برنامه درسی طوری طراحی شده است که انعطاف پذیر و سرگرم کننده باشد و می تواند به طور کامل یا جزئی مورد استفاده قرار گیرد. پروژه از کوچک شروع می شوند و تا پایان چرخه ۱۰ هفته ای همینطور پیچیده تر می شوند.

> دستورالعمل های ما را درباره [کد رفتار](../CODE_OF_CONDUCT.md), [مشارکت](../CONTRIBUTING.md),  [ترجمه](../TRANSLATIONS.md) ببینید. ما از بازخورد سازنده شما استقبال می کنیم!

 ## هر درس شامل:
 
- یادداشت های بصری (sketchnote) اختیاری
- فیلم های مکمل اختیاری
- کوییز های دست گرمی قبل از درس
- درسنامه مکتوب
- راهنمای گام به گام نحوه ساخت پروژه برای درس های مبتنی بر پروژه
- بررسی دانش
- یک چالش
- منابع خواندنی مکمل
- تمرین
- کوییز پس از درس

> **نکته ای در مورد آزمونها**: همه آزمون ها در [این برنامه](https://purple-hill-04aebfb03.1.azurestaticapps.net/) موجود هستند، برای در مجموع  ۴۰ کوییز که هرکدام شامل سه سوال می باشد. کوییزها از داخل درسنامه لینک داده شده اند اما برنامه کوییز را می توان به صورت محلی اجرا کرد. برای اینکار، دستورالعمل موجود در پوشه `quiz-app` را دنبال کنید. سوالات به تدریج در حال محلی سازی هستند.

## درسنامه


|![ یادداشت بصری (Sketchnote) از [(@sketchthedocs)](https://sketchthedocs.dev) ](../sketchnotes/00-Roadmap.png)|
|:---:|
| علم داده برای مبتدیان: نقشه راه - یادداشت بصری از [@nitya](https://twitter.com/nitya)_ |

 
| شماره درس | موضوع | گروه بندی درس | اهداف یادگیری | درس پیوند شده | نویسنده |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| ۱ | تعریف علم داده | [معرفی](../1-Introduction/README.md) | مفاهیم اساسی علم داده و نحوه ارتباط آن با هوش مصنوعی، یادگیری ماشین و کلان داده را بیاموزید. | [درسنامه](../1-Introduction/01-defining-data-science/README.md) [ویدیو](https://youtu.be/pqqsm5reGvs) | [Dmitry](http://soshnikov.com) |
| ۲ | اصول اخلاقی علم داده | [معرفی](../1-Introduction/README.md) | مفاهیم اخلاق داده ها، چالش ها و چارچوب ها. | [درسنامه](../1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| ۳ | تعریف داده | [معرفی](../1-Introduction/README.md) | نحوه دسته بندی داده ها و منابع رایج آن. | [درسنامه](../1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| ۴ | مقدمه ای بر آمار و احتمال | [معرفی](../1-Introduction/README.md) | تکنیک های ریاضی آمار و احتمال برای درک داده ها. | [درسنامه](../1-Introduction/04-stats-and-probability/README.md) [ویدیو](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| ۵ | کار با داده های رابطه ای | [کار با داده ها](../2-Working-With-Data/README.md) | مقدمه ای بر داده های رابطه ای و مبانی اکتشاف و تجزیه و تحلیل داده های رابطه ای با زبان پرس و جوی ساختار یافته ، که به SQL نیز معروف است (تلفظ کنید “see-quell”). | [درسنامه](../2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| ۶ | کار با داده های NoSQL | [کار با داده ها](../2-Working-With-Data/README.md) | مقدمه ای بر داده های غیر رابطه ای، انواع مختلف آن و مبانی کاوش و تجزیه و تحلیل پایگاه داده های اسناد(document databases). | [درسنامه](../2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| ۷ | کار با پایتون | [کار با داده ها](../2-Working-With-Data/README.md) | اصول استفاده از پایتون برای کاوش داده با کتابخانه هایی مانند Pandas. توصیه می شود مبانی برنامه نویسی پایتون را بلد باشید. | [درسنامه](../2-Working-With-Data/07-python/README.md) [ویدیو](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| ۸ | آماده سازی داده ها | [کار با داده ها](../2-Working-With-Data/README.md) | مباحث مربوط به تکنیک های داده ای برای پاکسازی و تبدیل داده ها به منظور رسیدگی به چالش های داده های مفقود شده، نادرست یا ناقص. | [درسنامه](../2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| ۹ | تصویرسازی مقادیر | [تصویرسازی داده ها](../3-Data-Visualization/README.md) | نحوه استفاده از Matplotlib برای تصویرسازی داده های پرندگان را می آموزید. 🦆 | [درسنامه](../3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| ۱۰ | تصویرسازی توزیع داده ها | [تصویرسازی داده ها](../3-Data-Visualization/README.md) | تصویرسازی مشاهدات و روندها در یک بازه زمانی. | [درسنامه](../3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| ۱۱ | تصویرسازی نسبت ها | [تصویرسازی داده ها](../3-Data-Visualization/README.md) | تصویرسازی درصدهای مجزا و گروهی. | [درسنامه](../3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| ۱۲ | تصویرسازی روابط | [تصویرسازی داده ها](../3-Data-Visualization/README.md) | تصویرسازی ارتباطات و همبستگی بین مجموعه داده ها و متغیرهای آنها. | [درسنامه](../3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| ۱۳ | تصویرسازی های معنی دار | [تصویرسازی داده ها](../3-Data-Visualization/README.md) | تکنیک ها و راهنمایی هایی برای تبدیل تصویرسازی های شما به خروجی های ارزشمندی جهت حل موثرتر مشکلات و بینش ها. | [درسنامه](../3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| ۱۴ | مقدمه ای بر چرخه حیات علم داده | [چرخه حیات](../4-Data-Science-Lifecycle/README.md) | مقدمه ای بر چرخه حیات علم داده و اولین گام آن برای دستیابی به داده ها و استخراج آن ها. | [درسنامه](../4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| ۱۵ | تجزیه و تحلیل | [چرخه حیات](../4-Data-Science-Lifecycle/README.md) | این مرحله از چرخه حیات علم داده بر تکنیک های تجزیه و تحلیل داده ها متمرکز است. | [درسنامه](../4-Data-Science-Lifecycle/15-Analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| ۱۶ | ارتباطات | [چرخه حیات](../4-Data-Science-Lifecycle/README.md) | این مرحله از چرخه حیات علم داده بر روی ارائه بینش از داده ها به نحوی که درک آنها را برای تصمیم گیرندگان آسان تر بکند، متمرکز است. | [درسنامه](../4-Data-Science-Lifecycle/16-Communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| ۱۷ | علم داده در فضای ابری | [داده های ابری](../5-Data-Science-In-Cloud/README.md) | این سری از درسنامه ها علم داده در فضای ابری و مزایای آن را معرفی می کند. | [درسنامه](../5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) و [Maud](https://twitter.com/maudstweets) |
| ۱۸ | علم داده در فضای ابری | [داده های ابری](../5-Data-Science-In-Cloud/README.md) | آموزش مدل ها با استفاده از ابزارهای کد کمتر(low code). |[درسنامه](../5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) و [Maud](https://twitter.com/maudstweets) |
| ۱۹ | علم داده در فضای  | [داده های ابری](../5-Data-Science-In-Cloud/README.md) | استقرار(Deploy) مدل ها با استفاده از استودیوی یادگیری ماشین آژور(Azure Machine Learning Studio). | [درسنامه](../5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) و [Maud](https://twitter.com/maudstweets) |
| ۲۰ | علم داده در طبیعت | [در طبیعت](../6-Data-Science-In-Wild/README.md) | پروژه های علم داده در دنیای واقعی. | [درسنامه](../6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |
## دسترسی آفلاین

شما می توانید این سند را به با استفاده از [Docsify](https://docsify.js.org/#/) به صورت آفلاین اجرا کنید. این مخزن را فورک کنید، [Docsify را روی دستگاه محلی خود نصب کنید](https://docsify.js.org/#/quickstart)، سپس در شاخه اصلی(root) این مخزن، بنویسید `docsify serve`. وب سایت در پورت 3000 روی localhost شما ارائه می شود: `localhost:3000`. 

> توجه داشته باشید، نوت بوک ها توسط Docsify ترجمه نمی شوند، بنابراین هنگامی که شما نیاز به اجرای یک نوت بوک دارید، این کار را به صورت جداگانه در VS Code با اجرای یک کرنل پایتون انجام دهید. 
## پی دی اف

یک پی دی اف شامل همه درسها را می توان [اینجا](https://microsoft.github.io/Data-Science-For-Beginners/pdf/readme.pdf) یافت.

## به کمک شما نیازمندیم!

اگر می خواهید تمام یا بخشی از برنامه درسی را ترجمه کنید، لطفاً ظبق راهنمای [ترجمه ها](../TRANSLATIONS.md)ی ما عمل کنید.

## سایر برنامه های درسی
تیم ما برنامه های درسی دیگری نیز تولید می کند! بدین منظور ببینید:

- [یادگیری ماشین برای مبتدیان](https://aka.ms/ml-beginners)
- [اینترنت اشیا برای مبتدیان](https://aka.ms/iot-beginners)
- [توسعه سایت برای مبتدیان](https://aka.ms/webdev-beginners)

</div>
