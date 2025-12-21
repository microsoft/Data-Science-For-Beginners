<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "278a30661fe9f10afd81dea999adc63a",
  "translation_date": "2025-12-21T10:29:35+00:00",
  "source_file": "README.md",
  "language_code": "ur"
}
-->
‏# ڈیٹا سائنس برائے مبتدی - ایک نصاب

[![GitHub Codespaces میں کھولیں](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=344191198)

[![GitHub لائسنس](https://img.shields.io/github/license/microsoft/Data-Science-For-Beginners.svg)](https://github.com/microsoft/Data-Science-For-Beginners/blob/master/LICENSE)
[![GitHub شراکت کنندگان](https://img.shields.io/github/contributors/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/graphs/contributors/)
[![GitHub ایشوز](https://img.shields.io/github/issues/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/issues/)
[![GitHub پل-ریکویسٹس](https://img.shields.io/github/issues-pr/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/pulls/)
[![PRs خوش آمدید](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

Microsoft میں Azure Cloud Advocates خوش ہیں کہ وہ ڈیٹا سائنس کے بارے میں 10 ہفتوں، 20 اسباق پر مشتمل نصاب پیش کر رہے ہیں۔ ہر سبق میں پری-سبق اور پوسٹ-سبق کوئزز، سبق مکمل کرنے کے لیے تحریری ہدایات، ایک حل، اور ایک اسائنمنٹ شامل ہے۔ ہمارا پروجیکٹ پر مبنی اندازِ تدریس آپ کو بنانے کے دوران سیکھنے میں مدد دیتا ہے، جو نئی مہارتوں کو قائم کرنے کا ثابت شدہ طریقہ ہے۔

**ہمارے مصنفین کا دلی شکریہ:** [Jasmine Greenaway](https://www.twitter.com/paladique), [Dmitry Soshnikov](http://soshnikov.com), [Nitya Narasimhan](https://twitter.com/nitya), [Jalen McGee](https://twitter.com/JalenMcG), [Jen Looper](https://twitter.com/jenlooper), [Maud Levy](https://twitter.com/maudstweets), [Tiffany Souterre](https://twitter.com/TiffanySouterre), [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏 خاص شکریہ 🙏 ہمارے [Microsoft Student Ambassador](https://studentambassadors.microsoft.com/) مصنفین، نظر ثانی کرنے والوں اور مواد میں حصہ ڈالنے والوں کو،** خصوصاً Aaryan Arora, [Aditya Garg](https://github.com/AdityaGarg00), [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/), [Ankita Singh](https://www.linkedin.com/in/ankitasingh007), [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/), [Arpita Das](https://www.linkedin.com/in/arpitadas01/), ChhailBihari Dubey, [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor), [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [Majd Safi](https://www.linkedin.com/in/majd-s/), [Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/), [Miguel Correa](https://www.linkedin.com/in/miguelmque/), [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119), [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum), [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/), [Rohit Yadav](https://www.linkedin.com/in/rty2423), Samridhi Sharma, [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200),
[Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/), [Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/), Yogendrasingh Pawar , [Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/), [Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![اسکیچنوٹ بذریعہ @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.ur.png)|
|:---:|
| ڈیٹا سائنس برائے مبتدی - _اسکیچنوٹ از [@nitya](https://twitter.com/nitya)_ |

### 🌐 متعدد زبانوں کی حمایت

#### GitHub Action کے ذریعے معاونت (خودکار اور ہمیشہ تازہ ترین)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](./README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**اگر آپ مزید ترجمہ شدہ زبانوں کی حمایت چاہتے ہیں تو وہ یہاں فہرست شدہ ہیں:** [یہاں](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)

#### ہماری کمیونٹی میں شامل ہوں 
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

ہماری Discord پر Learn with AI سیریز جاری ہے، مزید جاننے اور شامل ہونے کے لیے ہمیں [Learn with AI سیریز](https://aka.ms/learnwithai/discord) پر جوائن کریں، جو 18 - 30 ستمبر، 2025 کو ہوگی۔ آپ کو GitHub Copilot کو ڈیٹا سائنس کے لیے استعمال کرنے کے ٹپس اور ٹرکس ملیں گے۔

![Learn with AI سیریز](../../translated_images/1.2b28cdc6205e26fef6a21817fe5d83ae8b50fbd0a33e9fed0df05845da5b30b6.ur.jpg)

# کیا آپ طالب علم ہیں؟

مندرجہ ذیل وسائل سے شروع کریں:

- [Student Hub page](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) اس صفحے میں آپ کو ابتدائی وسائل، Student پیکس اور یہاں تک کہ مفت سرٹیفکیٹ ووچر حاصل کرنے کے طریقے ملیں گے۔ یہ ایک صفحہ ہے جسے آپ کو بک مارک کرنا چاہیے اور وقتاً فوقتاً دیکھنا چاہیے کیونکہ ہم مواد کو کم از کم ماہانہ بنیاد پر تبدیل کرتے رہتے ہیں۔
- [Microsoft Learn Student Ambassadors](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) ایک عالمی طلباء سفیروں کی کمیونٹی میں شامل ہوں، یہ آپ کا مائیکروسافٹ میں داخل ہونے کا راستہ ہو سکتا ہے۔

# شروع کریں

## 📚 دستاویزات

- **[انسٹالیشن گائیڈ](INSTALLATION.md)** - شروع کرنے والوں کے لیے مرحلہ وار سیٹ اپ ہدایات
- **[استعمال گائیڈ](USAGE.md)** - مثالیں اور عام ورک فلو
- **[مسائل کا حل](TROUBLESHOOTING.md)** - عام مسائل کے حل
- **[شراکت کا رہنما](CONTRIBUTING.md)** - اس پروجیکٹ میں حصہ لینے کا طریقہ
- **[اساتذہ کے لیے](for-teachers.md)** - تدریسی رہنمائی اور کلاس روم کے وسائل

## 👨‍🎓 طلباء کے لیے
> **بالکل ابتدائی**: کیا آپ ڈیٹا سائنس میں نئے ہیں؟ ہمارے [ابتدائی دوستانہ مثالیں](examples/README.md) سے شروعات کریں! یہ سادہ، اچھی طرح تشریحات والی مثالیں آپ کو پورے نصاب میں غوطہ لگانے سے پہلے بنیادیں سمجھنے میں مدد دیں گی۔
> **[طلباء](https://aka.ms/student-page)**: اس نصاب کو خود استعمال کرنے کے لیے، پورا ریپو فورک کریں اور مشقیں خود مکمل کریں، پری-لیکچر کوئز سے شروع کریں۔ پھر لیکچر پڑھیں اور باقی سرگرمیاں مکمل کریں۔ کوشش کریں کہ حل کے کوڈ کی نقل کرنے کے بجائے اسباق کو سمجھ کر پروجیکٹس بنائیں؛ تاہم، وہ کوڈ ہر پروجیکٹ پر مبنی سبق کے /solutions فولڈرز میں دستیاب ہے۔ ایک اور خیال یہ ہے کہ دوستوں کے ساتھ ایک مطالعہ گروپ بنائیں اور مواد کو ایک ساتھ دیکھیں۔ مزید مطالعے کے لیے، ہم [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum) کی سفارش کرتے ہیں۔

**فوری آغاز:**
1. اپنے ماحول کو ترتیب دینے کے لیے [انسٹالیشن گائیڈ](INSTALLATION.md) چیک کریں
2. نصاب کے ساتھ کام کرنے کا طریقہ سیکھنے کے لیے [استعمال گائیڈ](USAGE.md) کا جائزہ لیں
3. سبق 1 سے شروع کریں اور ترتیب وار کام کریں
4. مدد کے لیے ہماری [Discord کمیونٹی](https://aka.ms/ds4beginners/discord) میں شامل ہوں

## 👩‍🏫 اساتذہ کے لیے

> **اساتذہ**: ہم نے اس نصاب کو استعمال کرنے کے کچھ مشورے [شامل کیے ہیں](for-teachers.md). ہمیں آپ کی آراء [ہمارے بحثی فورم](https://github.com/microsoft/Data-Science-For-Beginners/discussions) میں جان کر خوشی ہوگی!

## ٹیم سے ملیں

[![پرومو ویڈیو](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "پرومو ویڈیو")

**گیف بذریعہ** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)
> 🎥 اوپر موجود تصویر پر کلک کریں تاکہ اس پراجیکٹ اور اسے بنانے والوں کے بارے میں ویڈیو دیکھ سکیں!

## تدریسی اصول

ہم نے اس نصاب کو تیار کرتے وقت دو تدریسی اصول منتخب کیے ہیں: یہ کہ یہ پراجیکٹ پر مبنی ہو اور اس میں بار بار کوئزز شامل ہوں۔ اس سلسلے کے اختتام تک، طلباء ڈیٹا سائنس کے بنیادی اصول سیکھ لیں گے، جن میں اخلاقی تصورات، ڈیٹا کی تیاری، ڈیٹا کے ساتھ کام کرنے کے مختلف طریقے، ڈیٹا کی بصری نمائندگی، ڈیٹا کا تجزیہ، ڈیٹا سائنس کے حقیقی دنیا کے استعمالات، وغیرہ شامل ہیں۔

مزید برآں، کلاس سے پہلے ایک ہلکا پھلکا کوئز طلباء کے سیکھنے کے ارادے کو ترتیب دیتا ہے، جبکہ کلاس کے بعد دوسرا کوئز مزید حفظانِ ذہن کو یقینی بناتا ہے۔ یہ نصاب لچکدار اور خوشگوار ہونے کے لیے ڈیزائن کیا گیا ہے اور پورا یا جزوی طور پر لیا جا سکتا ہے۔ پراجیکٹس چھوٹے سے شروع ہوتے ہیں اور 10 ہفتوں کے چکر کے اختتام تک بتدریج پیچیدہ ہوتے جاتے ہیں۔

> ہمارے [ہمارا ضابطہ اخلاق](CODE_OF_CONDUCT.md), [Contributing](CONTRIBUTING.md),  [Translation](TRANSLATIONS.md) رہنما خطوط دیکھیں۔ ہم آپ کی تعمیری رائے کا خیرمقدم کرتے ہیں!

## ہر سبق میں شامل ہیں:

- اختیاری اسکیچنوٹ
- اختیاری معاون ویڈیو
- سبق سے قبل وارم اپ کوئز
- متن پر مبنی سبق
- پراجیکٹ پر مبنی اسباق کے لیے، پراجیکٹ بنانے کے مرحلہ وار رہنما
- علمی جانچیں
- ایک چیلنج
- معاون مطالعہ
- اسائنمنٹ
- [سبق کے بعد کا کوئز](https://ff-quizzes.netlify.app/en/)

> **کوئزز کے بارے میں ایک نوٹس**: تمام کوئزز Quiz-App فولڈر میں موجود ہیں، مجموعی طور پر 40 کوئزز ہر ایک میں تین سوالات ہیں۔ یہ اسباق کے اندر سے جوڑے گئے ہیں، لیکن کوئز ایپ کو مقامی طور پر چلایا جا سکتا ہے یا Azure پر ڈیپلائے کیا جا سکتا ہے؛ ہدایات `quiz-app` فولڈر میں موجود ہدایات پر عمل کریں۔ انہیں بتدریج مقامی زبانوں میں منتقل کیا جا رہا ہے۔

## 🎓 مبتدیوں کے لیے مثالیں

**کیا آپ ڈیٹا سائنس میں نئے ہیں؟** ہم نے شروعات میں مدد کے لیے سادہ، اچھی طرح تبصرہ شدہ کوڈ کے ساتھ ایک خاص [مثالوں کی ڈائریکٹری](examples/README.md) بنائی ہے:

- 🌟 **ہیلو ورلڈ** - آپ کا پہلا ڈیٹا سائنس پروگرام
- 📂 **ڈیٹا لوڈ کرنا** - ڈیٹا سیٹس کو پڑھنا اور دریافت کرنا سیکھیں
- 📊 **سادہ تجزیہ** - شماریات نکالیں اور پیٹرن تلاش کریں
- 📈 **بنیادی بصری نمائندگی** - چارٹس اور گراف بنائیں
- 🔬 **حقیقی دنیا کا پراجیکٹ** - شروع سے اختتام تک مکمل ورک فلو

ہر مثال میں ہر قدم کی وضاحت کرنے والے تفصیلی تبصرے شامل ہیں، جو بالکل ابتدائی لوگوں کے لیے بہترین ہیں!

👉 **[مثالوں سے شروع کریں](examples/README.md)** 👈

## اسباق


|![ اسکیچنوٹ از @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Roadmap.4905d6567dff47532b9bfb8e0b8980fc6b0b1292eebb24181c1a9753b33bc0f5.ur.png)|
|:---:|
| ڈیٹا سائنس برائے مبتدیان: روڈ میپ - _اسکیچنوٹ از [@nitya](https://twitter.com/nitya)_ |


| سبق نمبر | موضوع | سبق کا گروپ | سیکھنے کے مقاصد | مربوط سبق | مصنف |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | ڈیٹا سائنس کی تعریف | [تعارف](1-Introduction/README.md) | ڈیٹا سائنس کے بنیادی تصورات اور یہ مصنوعی ذہانت، مشین لرننگ، اور بگ ڈیٹا سے کیسے متعلق ہے، سیکھیں۔ | [سبق](1-Introduction/01-defining-data-science/README.md) [ویڈیو](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | ڈیٹا سائنس اخلاقیات | [تعارف](1-Introduction/README.md) | ڈیٹا اخلاقیات کے تصورات، چیلنجز اور فریم ورکس۔ | [سبق](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | ڈیٹا کی تعریف | [تعارف](1-Introduction/README.md) | ڈیٹا کو کیسے درجہ بندی کیا جاتا ہے اور اس کے عام ذرائع کون سے ہیں۔ | [سبق](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | اعداد و شمار اور امکانیت کا تعارف | [تعارف](1-Introduction/README.md) | ڈیٹا کو سمجھنے کے لیے احتمال اور شماریات کی ریاضیاتی تکنیکیں۔ | [سبق](1-Introduction/04-stats-and-probability/README.md) [ویڈیو](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | تعلقاتی (ریلیشنل) ڈیٹا کے ساتھ کام کرنا | [ڈیٹا کے ساتھ کام کرنا](2-Working-With-Data/README.md) | تعلقاتی ڈیٹا کا تعارف اور Structured Query Language (SQL) کے ساتھ تعلقاتی ڈیٹا کو تلاش اور تجزیہ کرنے کی بنیادی باتیں۔ | [سبق](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | NoSQL ڈیٹا کے ساتھ کام کرنا | [ڈیٹا کے ساتھ کام کرنا](2-Working-With-Data/README.md) | غیر تعلقاتی ڈیٹا کا تعارف، اس کی مختلف اقسام اور ڈاکیومنٹ ڈیٹابیسز کو تلاش اور تجزیہ کرنے کی بنیادی باتیں۔ | [سبق](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | Python کے ساتھ کام کرنا | [ڈیٹا کے ساتھ کام کرنا](2-Working-With-Data/README.md) | Pandas جیسے لائبریریوں کے ساتھ ڈیٹا کی کھوج کے لیے Python کے استعمال کی بنیادیں۔ Python پروگرامنگ کی بنیادی سمجھ تجویز کی جاتی ہے۔ | [سبق](2-Working-With-Data/07-python/README.md) [ویڈیو](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | ڈیٹا کی تیاری | [ڈیٹا کے ساتھ کام کرنا](2-Working-With-Data/README.md) | غائب، غلط یا نامکمل ڈیٹا کے چیلنجز سے نمٹنے کے لیے ڈیٹا کو صاف اور تبدیل کرنے کی تکنیکوں کے موضوعات۔ | [سبق](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | مقداروں کی بصری نمائندگی | [ڈیٹا ویزولائزیشن](3-Data-Visualization/README.md) | Matplotlib کا استعمال کرتے ہوئے پرندوں کے ڈیٹا کو بصری شکل میں دکھانا سیکھیں 🦆 | [سبق](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | ڈیٹا کی تقسیمات کی بصری نمائندگی | [ڈیٹا ویزولائزیشن](3-Data-Visualization/README.md) | کسی وقفے کے اندر مشاہدات اور رجحانات کو بصری شکل دینا۔ | [سبق](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | تناسبات کی بصری نمائندگی | [ڈیٹا ویزولائزیشن](3-Data-Visualization/README.md) | منفرد اور گروہ بند شدہ فیصدات کو بصری شکل میں دکھانا۔ | [سبق](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | رشتوں کی بصری نمائندگی | [ڈیٹا ویزولائزیشن](3-Data-Visualization/README.md) | ڈیٹا سیٹس اور ان کے متغیرات کے درمیان روابط اور ہم آہنگیوں کو بصری شکل میں دکھانا۔ | [سبق](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | بامعنی بصری نمائندگیاں | [ڈیٹا ویزولائزیشن](3-Data-Visualization/README.md) | آپ کی بصری نمائندگی کو مؤثر مسئلہ حل اور بصیرت کے لیے قیمتی بنانے کی تکنیکیں اور رہنمائی۔ | [سبق](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | ڈیٹا سائنس لائف سائیکل کا تعارف | [لائف سائیکل](4-Data-Science-Lifecycle/README.md) | ڈیٹا سائنس لائف سائیکل کا تعارف اور اس کے پہلے قدم یعنی ڈیٹا حاصل کرنا اور نکالنا۔ | [سبق](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | تجزیہ کرنا | [لائف سائیکل](4-Data-Science-Lifecycle/README.md) | ڈیٹا سائنس لائف سائیکل کا یہ مرحلہ ڈیٹا کا تجزیہ کرنے کی تکنیکوں پر مرکوز ہے۔ | [سبق](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | مواصلات | [لائف سائیکل](4-Data-Science-Lifecycle/README.md) | ڈیٹا سائنس لائف سائیکل کا یہ مرحلہ ڈیٹا سے حاصل شدہ بصیرت کو اس انداز میں پیش کرنے پر مرکوز ہے کہ فیصلہ سازان اسے آسانی سے سمجھ سکیں۔ | [سبق](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | کلاؤڈ میں ڈیٹا سائنس | [کلاؤڈ ڈیٹا](5-Data-Science-In-Cloud/README.md) | اس سلسلے کے اسباق کلاؤڈ میں ڈیٹا سائنس اور اس کے فوائد کا تعارف کراتے ہیں۔ | [سبق](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 18 | کلاؤڈ میں ڈیٹا سائنس | [کلاؤڈ ڈیٹا](5-Data-Science-In-Cloud/README.md) | Low Code ٹولز کا استعمال کرتے ہوئے ماڈلز کی تربیت۔ |[سبق](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 19 | کلاؤڈ میں ڈیٹا سائنس | [کلاؤڈ ڈیٹا](5-Data-Science-In-Cloud/README.md) | Azure Machine Learning Studio کے ساتھ ماڈلز کی تعیناتی۔ | [سبق](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 20 | حقیقی دنیا میں ڈیٹا سائنس | [حقیقی دنیا میں](6-Data-Science-In-Wild/README.md) | حقیقی دنیا میں ڈیٹا سائنس پر مبنی پراجیکٹس۔ | [سبق](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

اس نمونے کو Codespace میں کھولنے کے لیے یہ اقدامات کریں:
1. Code ڈراپ ڈاؤن مینو پر کلک کریں اور Open with Codespaces آپشن منتخب کریں۔
2. پین کے نیچے + New codespace منتخب کریں۔
مزید معلومات کے لیے، [GitHub documentation](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace) دیکھیں۔

## VSCode Remote - Containers
اپنے مقامی مشین اور VSCode کے توسط سے اس ریپو کو کانٹینر میں کھولنے کے لیے VS Code Remote - Containers ایکسٹینشن استعمال کریں:

1. اگر آپ پہلی بار ڈویلپمنٹ کنٹینر استعمال کر رہے ہیں تو، براہِ کرم یقینی بنائیں کہ آپ کا سسٹم ابتدائی تقاضوں کو پورا کرتا ہے (مثلاً Docker انسٹال ہو)؛ اس کے لیے [the getting started documentation](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started) دیکھیں۔

اس ریپوزیٹری کو استعمال کرنے کے لیے، آپ یا تو ریپوزیٹری کو ایک علیحدہ Docker والیوم میں کھول سکتے ہیں:

**نوٹ**: اندرونی طور پر، یہ Remote-Containers: **Clone Repository in Container Volume...** کمانڈ استعمال کرے گا تاکہ سورس کوڈ کو مقامی فائل سسٹم کی بجائے ایک Docker والیوم میں کلون کیا جا سکے۔ [Volumes](https://docs.docker.com/storage/volumes/) کنٹینر ڈیٹا کو برقرار رکھنے کے لیے ترجیحی طریقہ ہیں۔

یا ریپوزیٹری کی مقامی کلون کی گئی یا ڈاؤن لوڈ شدہ کاپی کھولیں:

- اس ریپوزیٹری کو اپنے مقامی فائل سسٹم پر کلون کریں۔
- F1 دبائیں اور **Remote-Containers: Open Folder in Container...** کمانڈ منتخب کریں۔
- اس فولڈر کی کلون شدہ کاپی منتخب کریں، کنٹینر کے شروع ہونے کا انتظار کریں، اور چیزیں آزمائیں۔

## آف لائن رسائی

آپ [Docsify](https://docsify.js.org/#/) استعمال کرکے اس دستاویزات کو آف لائن چلا سکتے ہیں۔ اس ریپو کو فورک کریں، اپنی مقامی مشین پر [install Docsify](https://docsify.js.org/#/quickstart) کریں، پھر اس ریپو کے روٹ فولڈر میں ٹائپ کریں `docsify serve`۔ ویب سائٹ آپ کے localhost پر پورٹ 3000 پر سرور کی جائے گی: `localhost:3000`۔

> نوٹ، نوٹ بکس Docsify کے ذریعے رینڈر نہیں ہوں گے، لہٰذا جب آپ کو نوٹ بک چلانے کی ضرورت ہو تو اسے علیحدہ طور پر VS Code میں Python کرنل کے ساتھ کریں۔

## دیگر نصاب

ہماری ٹیم دیگر نصاب بھی تیار کرتی ہے! دیکھیں:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD مبتدیوں کے لیے](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI مبتدیوں کے لیے](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP مبتدیوں کے لیے](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI ایجنٹس مبتدیوں کے لیے](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### جنریٹو AI سیریز
[![جنریٹو AI مبتدیوں کے لیے](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![جنریٹو AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![جنریٹو AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![جنریٹو AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### بنیادی سیکھنے
[![ML مبتدیوں کے لیے](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![ڈیٹا سائنس مبتدیوں کے لیے](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![مصنوعی ذہانت مبتدیوں کے لیے](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![سائبر سیکیورٹی مبتدیوں کے لیے](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![ویب ڈویلپمنٹ مبتدیوں کے لیے](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT مبتدیوں کے لیے](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR ڈویلپمنٹ مبتدیوں کے لیے](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### کوپائلٹ سیریز
[![Copilot برائے مشترکہ AI پروگرامنگ](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot برائے C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot مہم](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## مدد حاصل کریں

**کیا آپ مسائل کا سامنا کر رہے ہیں؟** ہمارے [مسائل کے حل کی رہنمائی](TROUBLESHOOTING.md) میں عمومی مسائل کے حل دیکھیں۔

اگر آپ پھنس جائیں یا AI ایپس بنانے کے بارے میں کوئی سوال ہو۔ MCP کے بارے میں مباحثوں میں دوسرے سیکھنے والوں اور تجربہ کار ڈویلپرز کے ساتھ شامل ہوں۔ یہ ایک معاون کمیونٹی ہے جہاں سوالات خوش آمدید کہے جاتے ہیں اور علم بلا جھجھک بانٹا جاتا ہے۔

[![Microsoft Foundry ڈسکارڈ](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

اگر آپ کے پاس پروڈکٹ فیڈبیک یا تعمیر کے دوران غلطیاں ہوں تو ملاحظہ کریں:

[![Microsoft Foundry ڈویلپر فورم](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
دفعِ ذمہ داری:
اس دستاویز کا ترجمہ AI ترجمہ سروس Co-op Translator (https://github.com/Azure/co-op-translator) کے ذریعے کیا گیا ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہِ کرم نوٹ کریں کہ خودکار تراجم میں غلطیاں یا عدمِ درستی ہو سکتی ہیں۔ اصل دستاویز کو اس کی مادری زبان میں معتبر ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی مترجم کا ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہوں گے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->