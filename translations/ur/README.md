<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7c31d1a22c746b1d0f0582d4f54702ba",
  "translation_date": "2025-12-24T22:48:42+00:00",
  "source_file": "README.md",
  "language_code": "ur"
}
-->
# ڈیٹا سائنس برائے مبتدی - ایک نصاب

[![GitHub Codespaces میں کھولیں](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=344191198)

[![GitHub لائسنس](https://img.shields.io/github/license/microsoft/Data-Science-For-Beginners.svg)](https://github.com/microsoft/Data-Science-For-Beginners/blob/master/LICENSE)
[![GitHub شراکت کنندگان](https://img.shields.io/github/contributors/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/graphs/contributors/)
[![GitHub مسائل](https://img.shields.io/github/issues/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/issues/)
[![GitHub پل-درخواستیں](https://img.shields.io/github/issues-pr/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/pulls/)
[![PRs خوش آمدید](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

Azure Cloud Advocates at Microsoft خوش ہیں کہ وہ ایک 10 ہفتوں، 20 اسباق پر مشتمل نصاب پیش کر رہے ہیں جو مکمل طور پر ڈیٹا سائنس کے بارے میں ہے۔ ہر سبق میں پیش سبق اور بعد از سبق کوئزز، سبق مکمل کرنے کے لیے تحریری ہدایات، ایک حل، اور ایک اسائنمنٹ شامل ہے۔ ہمارا پروجیکٹ پر مبنی تدریسی انداز آپ کو بنانے کے دوران سیکھنے کا موقع دیتا ہے، جو نئی مہارتوں کو 'ٹکنے' کے لیے ایک ثابت شدہ طریقہ ہے۔

**ہمارے مؤلفین کا دلی شکریہ:** [Jasmine Greenaway](https://www.twitter.com/paladique), [Dmitry Soshnikov](http://soshnikov.com), [Nitya Narasimhan](https://twitter.com/nitya), [Jalen McGee](https://twitter.com/JalenMcG), [Jen Looper](https://twitter.com/jenlooper), [Maud Levy](https://twitter.com/maudstweets), [Tiffany Souterre](https://twitter.com/TiffanySouterre), [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏 خصوصی شکریہ 🙏 ہمارے [Microsoft Student Ambassador](https://studentambassadors.microsoft.com/) مصنفین، جائزہ نگاروں اور مواد کے حصہ ڈالنے والوں کو،** خاص طور پر Aaryan Arora, [Aditya Garg](https://github.com/AdityaGarg00), [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/), [Ankita Singh](https://www.linkedin.com/in/ankitasingh007), [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/), [Arpita Das](https://www.linkedin.com/in/arpitadas01/), ChhailBihari Dubey, [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor), [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [Majd Safi](https://www.linkedin.com/in/majd-s/), [Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/), [Miguel Correa](https://www.linkedin.com/in/miguelmque/), [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119), [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum), [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/), [Rohit Yadav](https://www.linkedin.com/in/rty2423), Samridhi Sharma, [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200),
[Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/), [Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/), Yogendrasingh Pawar , [Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/), [Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![سکیچ نوٹ بذریعہ @sketchthedocs https://sketchthedocs.dev](../../translated_images/ur/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.png)|
|:---:|
| ڈیٹا سائنس برائے مبتدی - _سکیچ نوٹ بذریعہ [@nitya](https://twitter.com/nitya)_ |

### 🌐 متعدد زبانوں کی حمایت

#### GitHub Action کے ذریعے سپورٹ (خودکار اور ہمیشہ تازہ ترین)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[عربی](../ar/README.md) | [بنگالی](../bn/README.md) | [بلغاریائی](../bg/README.md) | [برمی (میانمار)](../my/README.md) | [چینی (سادہ)](../zh/README.md) | [چینی (روایتی، ہانگ کانگ)](../hk/README.md) | [چینی (روایتی، مکاو)](../mo/README.md) | [چینی (روایتی، تائیوان)](../tw/README.md) | [کروشیائی](../hr/README.md) | [چیک](../cs/README.md) | [ڈینش](../da/README.md) | [ڈچ](../nl/README.md) | [اسٹونین](../et/README.md) | [فنش](../fi/README.md) | [فرانسیسی](../fr/README.md) | [جرمن](../de/README.md) | [یونانی](../el/README.md) | [عبرانی](../he/README.md) | [ہندی](../hi/README.md) | [ہنگیرین](../hu/README.md) | [انڈونیشین](../id/README.md) | [اطالوی](../it/README.md) | [جاپانی](../ja/README.md) | [کنڑ](../kn/README.md) | [کوریائی](../ko/README.md) | [لتھوانین](../lt/README.md) | [مالے](../ms/README.md) | [مالایالم](../ml/README.md) | [مراٹھی](../mr/README.md) | [نیپالی](../ne/README.md) | [نائجیریا پیجن](../pcm/README.md) | [نارویجیئن](../no/README.md) | [فارسی (فارسی)](../fa/README.md) | [پولش](../pl/README.md) | [پرتگالی (برازیل)](../br/README.md) | [پرتگالی (پرتگال)](../pt/README.md) | [پنجابی (گرمکھی)](../pa/README.md) | [رومانیائی](../ro/README.md) | [روسی](../ru/README.md) | [سربیائی (سریلیک)](../sr/README.md) | [سلوواک](../sk/README.md) | [سلووینیائی](../sl/README.md) | [ہسپانوی](../es/README.md) | [سواحلی](../sw/README.md) | [سویڈش](../sv/README.md) | [ٹاگالوگ (فلپائنی)](../tl/README.md) | [تمل](../ta/README.md) | [تلگو](../te/README.md) | [تھائی](../th/README.md) | [ترکی](../tr/README.md) | [یوکرینیائی](../uk/README.md) | [اردو](./README.md) | [ویتنامی](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**اگر آپ مزید تراجم چاہتے ہیں تو سپورٹ شدہ زبانیں [یہاں](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) درج ہیں**

#### ہماری کمیونٹی میں شامل ہوں 
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

ہماری Discord پر "AI کے ساتھ سیکھیں" سیریز جاری ہے، مزید جاننے اور شامل ہونے کے لیے [Learn with AI Series](https://aka.ms/learnwithai/discord) پر آئیں از 18 - 30 ستمبر، 2025۔ آپ کو GitHub Copilot کو ڈیٹا سائنس کے لیے استعمال کرنے کے ٹپس اور ٹرکس ملیں گے۔

![AI کے ساتھ سیکھنے کی سیریز](../../translated_images/ur/1.2b28cdc6205e26fef6a21817fe5d83ae8b50fbd0a33e9fed0df05845da5b30b6.jpg)

# کیا آپ طالب علم ہیں؟

مندرجہ ذیل وسائل سے شروع کریں:

- [Student Hub صفحہ](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) اس صفحے میں آپ کو ابتدائی وسائل، اسٹوڈنٹ پیکس اور یہاں تک کہ مفت سرٹیفیکیٹ ووچر حاصل کرنے کے طریقے ملیں گے۔ یہ وہ صفحہ ہے جسے آپ نشان زد کرنا چاہیں گے اور وقتاً فوقتاً چیک کریں کیونکہ ہم کم از کم ماہانہ بنیاد پر مواد تبدیل کرتے ہیں۔
- [Microsoft Learn Student Ambassadors](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) عالمی سطح پر اسٹوڈنٹ ایمبیسیڈرز کی کمیونٹی میں شامل ہوں، یہ مائیکروسافٹ میں آپ کے داخلے کا راستہ ہو سکتا ہے۔

# شروع کریں

## 📚 دستاویزات

- **[Installation Guide](INSTALLATION.md)** - ابتدائیوں کے لیے قدم بہ قدم سیٹ اپ ہدایات
- **[Usage Guide](USAGE.md)** - مثالیں اور عام ورک فلو
- **[Troubleshooting](TROUBLESHOOTING.md)** - عام مسائل کے حل
- **[Contributing Guide](CONTRIBUTING.md)** - اس پروجیکٹ میں حصہ ڈالنے کا طریقہ
- **[For Teachers](for-teachers.md)** - تدریسی رہنمائی اور کلاس روم وسائل

## 👨‍🎓 طلباء کے لیے
> **بالکل نوآموز**: کیا آپ ڈیٹا سائنس میں نئے ہیں؟ ہمارے [ابتدائیوں کے لیے مثالیں](examples/README.md) سے شروع کریں! یہ سادہ، اچھی طرح کومنٹس والی مثالیں آپ کو مکمل نصاب میں داخل ہونے سے پہلے بنیادی باتیں سمجھنے میں مدد دیں گی۔
> **[طلباء](https://aka.ms/student-page)**: اس نصاب کو خود استعمال کرنے کے لیے، پورے ریپو کو فورک کریں اور خود مشقیں مکمل کریں، پری لیکچر کوئز سے شروع کریں۔ پھر لیکچر پڑھیں اور باقی سرگرمیاں مکمل کریں۔ کوشش کریں کہ حل کا کوڈ نقل کرنے کی بجائے اسباق کو سمجھ کر پروجیکٹس بنائیں؛ تاہم وہ کوڈ ہر پروجیکٹ-مرکوز سبق کے /solutions فولڈرز میں دستیاب ہے۔ ایک اور خیال یہ ہے کہ دوستوں کے ساتھ ایک اسٹڈی گروپ بنائیں اور مل کر مواد کا مطالعہ کریں۔ مزید مطالعے کے لیے، ہم [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum) کی سفارش کرتے ہیں۔

**فوری آغاز:**
1. اپنے ماحول کو سیٹ اپ کرنے کے لیے [Installation Guide](INSTALLATION.md) چیک کریں
2. نصاب کے ساتھ کام کرنے کا طریقہ سیکھنے کے لیے [Usage Guide](USAGE.md) کا جائزہ لیں
3. سبق 1 سے شروع کریں اور ترتیب وار آگے بڑھیں
4. معاونت کے لیے ہماری [Discord کمیونٹی](https://aka.ms/ds4beginners/discord) میں شامل ہوں

## 👩‍🏫 اساتذہ کے لیے

> **اساتذہ**: ہم نے اس نصاب کو استعمال کرنے کے متعلق [کچھ تجاویز شامل کی ہیں](for-teachers.md)۔ ہمیں آپ کی رائے [ہمارے مباحثہ فورم میں](https://github.com/microsoft/Data-Science-For-Beginners/discussions) پسند آئے گی!

## ٹیم سے ملیں

[![پرومو ویڈیو](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "پرومو ویڈیو")

**گِف بذریعہ** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)
> 🎥 اوپر والی تصویر پر پروجیکٹ اور اسے بنانے والے لوگوں کے بارے میں ویڈیو کے لیے کلک کریں!  

## تدریسی اصول

ہم نے اس نصاب کی تیاری کے دوران دو تدریسی اصول منتخب کیے ہیں: یہ یقینی بنانا کہ نصاب پروجیکٹ پر مبنی ہو اور اس میں بار بار کوئزز شامل ہوں۔ اس سلسلے کے اختتام تک، طلبہ نے ڈیٹا سائنس کے بنیادی اصول سیکھ لیے ہوں گے، جن میں اخلاقی تصورات، ڈیٹا کی تیاری، ڈیٹا کے ساتھ کام کرنے کے مختلف طریقے، ڈیٹا بصری نمائندگی، ڈیٹا تجزیہ، ڈیٹا سائنس کے حقیقی دنیا میں اطلاق اور مزید شامل ہیں۔

اس کے علاوہ، کلاس سے قبل ایک کم دباؤ والا کوئز طالب علم کے سیکھنے کے ارادے کو قائم کرتا ہے، جبکہ کلاس کے بعد ایک دوسرا کوئز مزید حفظِ معلومات کو یقینی بناتا ہے۔ یہ نصاب لچکدار اور دلچسپ بنانے کے لیے ڈیزائن کیا گیا تھا اور اسے مکمل یا جزوی طور پر لیا جا سکتا ہے۔ پروجیکٹس چھوٹے آغاز ہوتے ہیں اور 10 ہفتوں کے دورانیے کے اختتام تک بتدریج زیادہ پیچیدہ ہوتے جاتے ہیں۔

> ہمارا [ضابطۂ اخلاق](CODE_OF_CONDUCT.md)، [شراکت](CONTRIBUTING.md)،  [ترجمہ](TRANSLATIONS.md) گائیڈ لائنز دیکھیں۔ ہم آپ کی تعمیری رائے کا خیرمقدم کرتے ہیں!

## ہر سبق میں شامل ہے:

- اختیاری سکیچ نوٹ
- اختیاری ضمنی ویڈیو
- سبق سے قبل وارم اپ کوئز
- تحریری سبق
- پروجیکٹ پر مبنی اسباق کے لیے، پروجیکٹ بنانے کے مرحلہ وار رہنما
- علمی جانچ
- ایک چیلنج
- ضمنی مطالعہ
- اسائنمنٹ
- [سبق کے بعد کا کوئز](https://ff-quizzes.netlify.app/en/)

> **کوئزز کے بارے میں ایک نوٹ**: تمام کوئزز Quiz-App فولڈر میں محفوظ ہیں، کل 40 کوئزز ہیں جن میں سے ہر ایک تین سوالات پر مشتمل ہے۔ یہ اسباق کے اندر سے لنک کیے گئے ہیں، لیکن quiz app کو مقامی طور پر چلایا جا سکتا ہے یا Azure پر تعینات کیا جا سکتا ہے؛ `quiz-app` فولڈر میں ہدایات پر عمل کریں۔ انہیں بتدریج مختلف مقامی زبانوں میں ڈھالا جا رہا ہے۔

## 🎓 ابتدائی افراد کے لیے مثالیں

**ڈیٹا سائنس میں نئے ہیں؟** ہم نے خاص [examples directory](examples/README.md) تیار کیا ہے جس میں سادہ، اچھی طرح کمنٹس کے ساتھ کوڈ شامل ہے تاکہ آپ شروعات کر سکیں:

- 🌟 **Hello World** - آپ کا پہلا ڈیٹا سائنس پروگرام
- 📂 **Loading Data** - ڈیٹا سیٹس کو پڑھنے اور ان کی کھوج کرنے کا طریقہ سیکھیں
- 📊 **Simple Analysis** - اعداد و شمار کا حساب لگائیں اور پیٹرن تلاش کریں
- 📈 **Basic Visualization** - چارٹس اور گرافس بنائیں
- 🔬 **Real-World Project** - شروع سے آخر تک مکمل ورک فلو

ہر مثال میں ہر قدم کی وضاحت کرنے والی تفصیلی کمنٹس شامل ہیں، جو انہیں بالکل نو آموز افراد کے لیے بہترین بناتی ہیں!

👉 **[مثالوں سے شروع کریں](examples/README.md)** 👈

## اسباق


|![ اسکیچ نوٹ بذریعہ @sketchthedocs https://sketchthedocs.dev](../../translated_images/ur/00-Roadmap.4905d6567dff47532b9bfb8e0b8980fc6b0b1292eebb24181c1a9753b33bc0f5.png)|
|:---:|
| ڈیٹا سائنس برائے ابتدائی افراد: روڈ میپ - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |


| Lesson Number | Topic | Lesson Grouping | Learning Objectives | Linked Lesson | Author |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | ڈیٹا سائنس کی تعریف | [Introduction](1-Introduction/README.md) | ڈیٹا سائنس کے بنیادی تصورات سیکھیں اور یہ کہ یہ مصنوعی ذہانت، مشین لرننگ، اور بگ ڈیٹا سے کس طرح متعلق ہے۔ | [lesson](1-Introduction/01-defining-data-science/README.md) [video](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | ڈیٹا سائنس اخلاقیات | [Introduction](1-Introduction/README.md) | ڈیٹا اخلاقیات کے تصورات، چیلنجز اور فریم ورک۔ | [lesson](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | ڈیٹا کی تعریف | [Introduction](1-Introduction/README.md) | ڈیٹا کی درجہ بندی اور اس کے عام ذرائع۔ | [lesson](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | اعداد و شمار اور احتمال کا تعارف | [Introduction](1-Introduction/README.md) | ڈیٹا کو سمجھنے کے لیے احتمال اور اعداد و شمار کی ریاضیاتی تکنیکیں۔ | [lesson](1-Introduction/04-stats-and-probability/README.md) [video](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | رلیشنل ڈیٹا کے ساتھ کام کرنا | [Working With Data](2-Working-With-Data/README.md) | رلیشنل ڈیٹا کا تعارف اور Structured Query Language (SQL، جس کا تلفظ “see-quell” ہے) کے ذریعے رلیشنل ڈیٹا کو تلاش اور تجزیہ کرنے کی بنیادی باتیں۔ | [lesson](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | NoSQL ڈیٹا کے ساتھ کام کرنا | [Working With Data](2-Working-With-Data/README.md) | غیر رلیشنل ڈیٹا کا تعارف، اس کی مختلف اقسام اور ڈاکیومنٹ ڈیٹا بیسز کے بنیادی تلاش اور تجزیہ۔ | [lesson](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | Python کے ساتھ کام کرنا | [Working With Data](2-Working-With-Data/README.md) | Pandas جیسے لائبریریز کے ساتھ ڈیٹا کی کھوج کے لیے Python کے استعمال کی بنیادی باتیں۔ Python پروگرامنگ کی بنیادی سمجھ کی سفارش کی جاتی ہے۔ | [lesson](2-Working-With-Data/07-python/README.md) [video](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | ڈیٹا کی تیاری | [Working With Data](2-Working-With-Data/README.md) | ڈیٹا کو صاف اور تبدیل کرنے کی تکنیکیں تاکہ غائب، غلط، یا نامکمل ڈیٹا کے چیلنجز کو سنبھالا جا سکے۔ | [lesson](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | مقداروں کی بصری نمائندگی | [Data Visualization](3-Data-Visualization/README.md) | Matplotlib کا استعمال کر کے پرندوں کے ڈیٹا کی بصری نمائندگی سیکھیں 🦆 | [lesson](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | ڈیٹا کی تقسیمات کی بصری نمائندگی | [Data Visualization](3-Data-Visualization/README.md) | وقفہ کے اندر مشاہدات اور رجحانات کو بصری شکل دینا۔ | [lesson](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | تناسبات کی بصری نمائندگی | [Data Visualization](3-Data-Visualization/README.md) | غیر مسلسل اور گروپ شدہ فیصدات کی بصری نمائندگی۔ | [lesson](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | تعلقات کی بصری نمائندگی | [Data Visualization](3-Data-Visualization/README.md) | ڈیٹا کے سیٹ اور ان کے متغیرات کے درمیان روابط اور هم بستگی کی بصری نمائندگی۔ | [lesson](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | بامعنی بصری نمائندگیاں | [Data Visualization](3-Data-Visualization/README.md) | اپنی بصری نمائندگیوں کو مؤثر مسئلہ حل اور بصیرت کے لیے قیمتی بنانے کی تکنیکیں اور رہنمائی۔ | [lesson](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | ڈیٹا سائنس لائف سائیکل کا تعارف | [Lifecycle](4-Data-Science-Lifecycle/README.md) | ڈیٹا سائنس لائف سائیکل کا تعارف اور اس کے پہلے مرحلے یعنی ڈیٹا حاصل کرنے اور نکالنے کا تعارف۔ | [lesson](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | تجزیہ کرنا | [Lifecycle](4-Data-Science-Lifecycle/README.md) | ڈیٹا سائنس لائف سائیکل کا یہ مرحلہ ڈیٹا کا تجزیہ کرنے کی تکنیکوں پر توجہ دیتا ہے۔ | [lesson](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | ابلاغ | [Lifecycle](4-Data-Science-Lifecycle/README.md) | یہ مرحلہ ڈیٹا سے حاصل شدہ بصیرت کو ایسے انداز میں پیش کرنے پر مرکوز ہے جو فیصلہ سازوں کے لیے سمجھنا آسان بنائے۔ | [lesson](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | کلاؤڈ میں ڈیٹا سائنس | [Cloud Data](5-Data-Science-In-Cloud/README.md) | یہ سلسلہ کلاؤڈ میں ڈیٹا سائنس اور اس کے فوائد کا تعارف کراتا ہے۔ | [lesson](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 18 | کلاؤڈ میں ڈیٹا سائنس | [Cloud Data](5-Data-Science-In-Cloud/README.md) | Low Code ٹولز کا استعمال کرتے ہوئے ماڈلز کی ٹریننگ۔ |[lesson](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 19 | کلاؤڈ میں ڈیٹا سائنس | [Cloud Data](5-Data-Science-In-Cloud/README.md) | Azure Machine Learning Studio کے ساتھ ماڈلز کو ڈپلائے کرنا۔ | [lesson](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 20 | حقیقی دنیا میں ڈیٹا سائنس | [In the Wild](6-Data-Science-In-Wild/README.md) | حقیقی دنیا میں ڈیٹا سائنس سے چلنے والے پروجیکٹس۔ | [lesson](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

اس نمونے کو Codespace میں کھولنے کے لیے درج ذیل اقدامات پر عمل کریں:
1. Code ڈراپ ڈاؤن مینو پر کلک کریں اور Open with Codespaces آپشن منتخب کریں۔
2. پین کے نیچے + New codespace منتخب کریں۔
مزید معلومات کے لیے، [GitHub documentation](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace) دیکھیں۔

## VSCode Remote - Containers
اپنے مقامی مشین اور VSCode کا استعمال کرتے ہوئے اس ریپو کو کنٹینر میں کھولنے کے لیے درج ذیل اقدامات پر عمل کریں، اس کے لیے VS Code Remote - Containers ایکسٹینشن استعمال کریں:

1. اگر یہ آپ کا پہلی بار ڈیویلپمنٹ کنٹینر استعمال کرنا ہے، تو براہ کرم یقینی بنائیں کہ آپ کا سسٹم پری-ریکوئزٹس پورا کرتا ہے (مثلاً Docker نصب ہو) اس کے لیے [the getting started documentation](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started) دیکھیں۔

اس ریپوزٹری کو استعمال کرنے کے لیے، آپ یا تو ریپوزٹری کو ایک الگ شدہ Docker والیوم میں کھول سکتے ہیں:

**نوٹ**: اندرونی طور پر، یہ Remote-Containers: **Clone Repository in Container Volume...** کمانڈ استعمال کرے گا تاکہ سورس کوڈ کو مقامی فائل سسٹم کی بجائے Docker والیوم میں کلون کیا جائے۔ [Volumes](https://docs.docker.com/storage/volumes/) کنٹینر ڈیٹا کو برقرار رکھنے کے لیے ترجیحی طریقہ کار ہیں۔

یا ریپوزٹری کی مقامی کلون شدہ یا ڈاؤن لوڈ شدہ کاپی کھولیں:

- اس ریپوزٹری کو اپنے مقامی فائل سسٹم پر کلون کریں۔
- F1 دبائیں اور Remote-Containers: **Open Folder in Container...** کمانڈ منتخب کریں۔
- اس فولڈر کی کلون شدہ کاپی منتخب کریں، کنٹینر کے شروع ہونے تک انتظار کریں، اور پھر چیزیں آزمائیں۔

## آف لائن رسائی

آپ اس دستاویز کو آف لائن Docsify کے ذریعے چلا کر دیکھ سکتے ہیں۔ اس ریپو کو فورک کریں، اپنی مقامی مشین پر [Docsify انسٹال کریں](https://docsify.js.org/#/quickstart)، پھر اس ریپو کے روٹ فولڈر میں `docsify serve` ٹائپ کریں۔ ویب سائٹ آپ کے لوکل ہوسٹ پر پورٹ 3000 پر فراہم کی جائے گی: `localhost:3000`.

> نوٹ، نوٹ بکس Docsify کے ذریعے رینڈر نہیں ہوں گے، لہٰذا جب آپ کو نوٹ بک چلانی ہو تو وہ الگ طور پر VS Code میں Python کرنل کے ساتھ چلائیں۔

## دیگر نصاب

ہماری ٹیم دیگر نصاب بھی تیار کرتی ہے! دیکھیں:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j برائے مبتدی](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js برائے مبتدی](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![ابتدائیوں کے لیے AZD](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![ابتدائیوں کے لیے Edge AI](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![ابتدائیوں کے لیے MCP](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![ابتدائیوں کے لیے AI ایجنٹس](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### جنریٹو AI سیریز
[![ابتدائیوں کے لیے جنریٹو AI](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![جنریٹو AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![جنریٹو AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![جنریٹو AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### بنیادی سیکھنے
[![ابتدائیوں کے لیے مشین لرننگ](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![ابتدائیوں کے لیے ڈیٹا سائنس](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![ابتدائیوں کے لیے مصنوعی ذہانت](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![ابتدائیوں کے لیے سائبر سکیورٹی](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![ابتدائیوں کے لیے ویب ڈویلپمنٹ](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![ابتدائیوں کے لیے IoT](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![ابتدائیوں کے لیے XR ڈویلپمنٹ](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### کوپائلٹ سیریز
[![AI کے ساتھ جوڑی پروگرامنگ کے لیے کوپائلٹ](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET کے لیے کوپائلٹ](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![کوپائلٹ ایڈونچر](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## مدد حاصل کریں

**مسائل درپیش ہیں؟** عام مسائل کے حل کے لیے ہماری [مسائل حل کرنے کی رہنمائی](TROUBLESHOOTING.md) دیکھیں۔

اگر آپ پھنس جائیں یا AI ایپس بنانے کے بارے میں کوئی سوال ہو۔ MCP کے بارے میں گفتگو میں ساتھی سیکھنے والوں اور تجربہ کار ڈویلپرز میں شامل ہوں۔ یہ ایک معاون کمیونٹی ہے جہاں سوالات خوش آمدید ہیں اور علم کھل کر بانٹا جاتا ہے۔

[![مائیکروسافٹ فاؤنڈری ڈسکارڈ](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

اگر آپ کے پاس پراڈکٹ کا فیڈبیک یا بنانے کے دوران خامیاں ہوں تو ملاحظہ کریں:

[![مائیکروسافٹ فاؤنڈری ڈویلپر فورم](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
دسکلیمر:
اس دستاویز کا ترجمہ AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے کیا گیا ہے۔ ہم درستگی کے لیے کوشاں ہیں، تاہم براہِ کرم نوٹ کریں کہ خودکار تراجم میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی مادری زبان میں معتبر ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ذمہ دار نہیں ہوں گے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->