<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5443b88ba402d2ec7b000e4de6cecb8",
  "translation_date": "2025-08-29T07:57:01+00:00",
  "source_file": "README.md",
  "language_code": "bn"
}
-->
# শিক্ষার্থীদের জন্য ডেটা সায়েন্স - একটি পাঠক্রম

Azure Cloud Advocates at Microsoft একটি ১০-সপ্তাহের, ২০-লেসনের পাঠক্রম নিয়ে এসেছে যা সম্পূর্ণ ডেটা সায়েন্স নিয়ে। প্রতিটি লেসনে রয়েছে প্রাক-লেসন এবং পরবর্তী লেসনের কুইজ, লেসন সম্পন্ন করার জন্য লিখিত নির্দেশনা, একটি সমাধান এবং একটি অ্যাসাইনমেন্ট। আমাদের প্রকল্প-ভিত্তিক পদ্ধতি আপনাকে শেখার সময় তৈরি করতে সাহায্য করে, যা নতুন দক্ষতা অর্জনের একটি প্রমাণিত উপায়।

**আমাদের লেখকদের প্রতি আন্তরিক ধন্যবাদ:** [জেসমিন গ্রিনওয়ে](https://www.twitter.com/paladique), [দিমিত্রি সশনিকভ](http://soshnikov.com), [নিত্যা নারাসিমহান](https://twitter.com/nitya), [জালেন ম্যাকগি](https://twitter.com/JalenMcG), [জেন লুপার](https://twitter.com/jenlooper), [মড লেভি](https://twitter.com/maudstweets), [টিফানি সুটের](https://twitter.com/TiffanySouterre), [ক্রিস্টোফার হ্যারিসন](https://www.twitter.com/geektrainer)।

**🙏 বিশেষ ধন্যবাদ 🙏 আমাদের [Microsoft Student Ambassador](https://studentambassadors.microsoft.com/) লেখক, রিভিউয়ার এবং কন্টেন্ট কন্ট্রিবিউটরদের প্রতি,** বিশেষত আরিয়ান অরোরা, [আদিত্য গার্গ](https://github.com/AdityaGarg00), [আলন্দ্রা সানচেজ](https://www.linkedin.com/in/alondra-sanchez-molina/), [অঙ্কিতা সিং](https://www.linkedin.com/in/ankitasingh007), [অনুপম মিশ্র](https://www.linkedin.com/in/anupam--mishra/), [অর্পিতা দাস](https://www.linkedin.com/in/arpitadas01/), ছাইলবিহারী দুবে, [ডিব্রি এনসোফর](https://www.linkedin.com/in/dibrinsofor), [দিশিতা ভাসিন](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [মাজদ সাফি](https://www.linkedin.com/in/majd-s/), [ম্যাক্স ব্লুম](https://www.linkedin.com/in/max-blum-6036a1186/), [মিগুয়েল কোরিয়া](https://www.linkedin.com/in/miguelmque/), [মোহাম্মদ ইফতেখার (ইফটু) ইবনে জালাল](https://twitter.com/iftu119), [নওরিন তাবাসসুম](https://www.linkedin.com/in/nawrin-tabassum), [রেমন্ড ওয়াংসা পুত্র](https://www.linkedin.com/in/raymond-wp/), [রোহিত যাদব](https://www.linkedin.com/in/rty2423), সমৃদ্ধি শর্মা, [সানিয়া সিনহা](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200), [শীনা নারুলা](https://www.linkedin.com/in/sheena-narua-n/), [তৌকির আহমদ](https://www.linkedin.com/in/tauqeerahmad5201/), যোগেন্দ্রসিং পাওয়ার, [বিদুষী গুপ্তা](https://www.linkedin.com/in/vidushi-gupta07/), [জাসলিন সোধি](https://www.linkedin.com/in/jasleen-sondhi/)।

|![@sketchthedocs দ্বারা স্কেচনোট https://sketchthedocs.dev](../../translated_images/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.bn.png)|
|:---:|
| শিক্ষার্থীদের জন্য ডেটা সায়েন্স - _[@nitya](https://twitter.com/nitya) দ্বারা স্কেচনোট_ |

### 🌐 বহু-ভাষার সমর্থন

#### GitHub Action এর মাধ্যমে সমর্থিত (স্বয়ংক্রিয় এবং সর্বদা আপডেটেড)

[ফরাসি](../fr/README.md) | [স্প্যানিশ](../es/README.md) | [জার্মান](../de/README.md) | [রাশিয়ান](../ru/README.md) | [আরবি](../ar/README.md) | [ফার্সি](../fa/README.md) | [উর্দু](../ur/README.md) | [চীনা (সরলীকৃত)](../zh/README.md) | [চীনা (প্রথাগত, ম্যাকাও)](../mo/README.md) | [চীনা (প্রথাগত, হংকং)](../hk/README.md) | [চীনা (প্রথাগত, তাইওয়ান)](../tw/README.md) | [জাপানি](../ja/README.md) | [কোরিয়ান](../ko/README.md) | [হিন্দি](../hi/README.md) | [বাংলা](./README.md) | [মারাঠি](../mr/README.md) | [নেপালি](../ne/README.md) | [পাঞ্জাবি (গুরুমুখী)](../pa/README.md) | [পর্তুগিজ (পর্তুগাল)](../pt/README.md) | [পর্তুগিজ (ব্রাজিল)](../br/README.md) | [ইতালিয়ান](../it/README.md) | [পোলিশ](../pl/README.md) | [তুর্কি](../tr/README.md) | [গ্রিক](../el/README.md) | [থাই](../th/README.md) | [সুইডিশ](../sv/README.md) | [ড্যানিশ](../da/README.md) | [নরওয়েজিয়ান](../no/README.md) | [ফিনিশ](../fi/README.md) | [ডাচ](../nl/README.md) | [হিব্রু](../he/README.md) | [ভিয়েতনামি](../vi/README.md) | [ইন্দোনেশিয়ান](../id/README.md) | [মালয়](../ms/README.md) | [তাগালগ (ফিলিপিনো)](../tl/README.md) | [সোয়াহিলি](../sw/README.md) | [হাঙ্গেরিয়ান](../hu/README.md) | [চেক](../cs/README.md) | [স্লোভাক](../sk/README.md) | [রোমানিয়ান](../ro/README.md) | [বুলগেরিয়ান](../bg/README.md) | [সার্বিয়ান (সিরিলিক)](../sr/README.md) | [ক্রোয়েশিয়ান](../hr/README.md) | [স্লোভেনিয়ান](../sl/README.md) | [ইউক্রেনিয়ান](../uk/README.md) | [বার্মিজ (মিয়ানমার)](../my/README.md)

**যদি আপনি অতিরিক্ত অনুবাদ চান, সমর্থিত ভাষাগুলোর তালিকা [এখানে](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) পাওয়া যাবে।**

#### আমাদের কমিউনিটিতে যোগ দিন 
[![Azure AI Discord](https://dcbadge.limes.pink/api/server/kzRShWzttr)](https://discord.gg/kzRShWzttr)

# আপনি কি একজন শিক্ষার্থী?

নিম্নলিখিত রিসোর্স দিয়ে শুরু করুন:

- [স্টুডেন্ট হাব পেজ](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) এই পেজে আপনি পাবেন শিক্ষার্থীদের জন্য রিসোর্স, স্টুডেন্ট প্যাক এবং এমনকি বিনামূল্যে সার্টিফিকেট ভাউচার পাওয়ার উপায়। এটি একটি পেজ যা আপনি বুকমার্ক করতে এবং সময়ে সময়ে চেক করতে চাইবেন কারণ আমরা অন্তত মাসিক ভিত্তিতে কন্টেন্ট পরিবর্তন করি।
- [Microsoft Learn Student Ambassadors](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) একটি গ্লোবাল স্টুডেন্ট অ্যাম্বাসেডর কমিউনিটিতে যোগ দিন, এটি হতে পারে মাইক্রোসফটে প্রবেশের আপনার পথ।

# শুরু করা যাক

> **শিক্ষকগণ**: আমরা [কিছু পরামর্শ অন্তর্ভুক্ত করেছি](for-teachers.md) কীভাবে এই পাঠক্রম ব্যবহার করবেন। আমাদের [আলোচনা ফোরামে](https://github.com/microsoft/Data-Science-For-Beginners/discussions) আপনার মতামত জানাতে ভালো লাগবে!

> **[শিক্ষার্থীরা](https://aka.ms/student-page)**: এই পাঠক্রমটি নিজের জন্য ব্যবহার করতে, পুরো রিপোজিটরি ফর্ক করুন এবং নিজের মতো করে এক্সারসাইজগুলো সম্পন্ন করুন, প্রাক-লেকচার কুইজ দিয়ে শুরু করুন। তারপর লেকচার পড়ুন এবং বাকি কার্যক্রম সম্পন্ন করুন। লেসনগুলো বুঝে প্রজেক্ট তৈরি করার চেষ্টা করুন, সমাধান কোড কপি না করে; তবে, সেই কোড /solutions ফোল্ডারে পাওয়া যাবে প্রতিটি প্রজেক্ট-ভিত্তিক লেসনে। আরেকটি ধারণা হতে পারে বন্ধুদের সাথে একটি স্টাডি গ্রুপ তৈরি করা এবং একসাথে কন্টেন্টটি পড়া। আরও পড়াশোনার জন্য, আমরা [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum) সুপারিশ করি।

## টিমের সাথে পরিচিত হন

[![প্রোমো ভিডিও](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "প্রোমো ভিডিও")

**Gif তৈরি করেছেন** [মোহিত জয়সল](https://www.linkedin.com/in/mohitjaisal)

> 🎥 উপরের ছবিতে ক্লিক করুন প্রজেক্ট এবং এটি তৈরি করা ব্যক্তিদের সম্পর্কে একটি ভিডিও দেখার জন্য!

## শিক্ষাদান পদ্ধতি

আমরা এই পাঠক্রম তৈরি করার সময় দুটি শিক্ষাদান নীতি বেছে নিয়েছি: এটি প্রকল্প-ভিত্তিক নিশ্চিত করা এবং এতে ঘন ঘন কুইজ অন্তর্ভুক্ত করা। এই সিরিজের শেষে, শিক্ষার্থীরা ডেটা সায়েন্সের মৌলিক নীতিগুলো শিখবে, যার মধ্যে রয়েছে নৈতিক ধারণা, ডেটা প্রস্তুতি, ডেটার সাথে কাজ করার বিভিন্ন উপায়, ডেটা ভিজ্যুয়ালাইজেশন, ডেটা বিশ্লেষণ, ডেটা সায়েন্সের বাস্তব জীবনের ব্যবহারিক কেস এবং আরও অনেক কিছু।

এছাড়াও, একটি ক্লাসের আগে একটি কম ঝুঁকির কুইজ শিক্ষার্থীর মনোযোগ একটি বিষয় শেখার দিকে নিয়ে যায়, যখন ক্লাসের পরে একটি দ্বিতীয় কুইজ আরও ধারণ নিশ্চিত করে। এই পাঠক্রমটি নমনীয় এবং মজাদার করার জন্য ডিজাইন করা হয়েছে এবং এটি পুরোপুরি বা আংশিকভাবে নেওয়া যেতে পারে। প্রকল্পগুলো ছোট থেকে শুরু হয় এবং ১০ সপ্তাহের চক্রের শেষে ক্রমশ জটিল হয়ে ওঠে।
আমাদের [আচরণবিধি](CODE_OF_CONDUCT.md), [অবদান](CONTRIBUTING.md), [অনুবাদ](TRANSLATIONS.md) নির্দেশিকা দেখুন। আমরা আপনার গঠনমূলক প্রতিক্রিয়া স্বাগত জানাই!
## প্রতিটি পাঠ অন্তর্ভুক্ত করে:

- ঐচ্ছিক স্কেচনোট
- ঐচ্ছিক সম্পূরক ভিডিও
- পাঠের আগে উষ্ণতা পরীক্ষা
- লিখিত পাঠ
- প্রকল্প-ভিত্তিক পাঠের জন্য, প্রকল্প তৈরি করার ধাপে ধাপে নির্দেশিকা
- জ্ঞান যাচাই
- একটি চ্যালেঞ্জ
- সম্পূরক পাঠ্য
- অ্যাসাইনমেন্ট
- [পাঠ-পরবর্তী কুইজ](https://ff-quizzes.netlify.app/en/)

> **কুইজ সম্পর্কে একটি নোট**: সমস্ত কুইজ `Quiz-App` ফোল্ডারে অন্তর্ভুক্ত, যেখানে মোট ৪০টি কুইজ রয়েছে, প্রতিটিতে তিনটি প্রশ্ন। এগুলো পাঠের মধ্যে থেকে লিঙ্ক করা হয়েছে, তবে কুইজ অ্যাপটি স্থানীয়ভাবে চালানো বা Azure-এ ডিপ্লয় করা যেতে পারে; `quiz-app` ফোল্ডারের নির্দেশনা অনুসরণ করুন। এগুলো ধীরে ধীরে স্থানীয় ভাষায় অনুবাদ করা হচ্ছে।

## পাঠসমূহ

|![ @sketchthedocs দ্বারা স্কেচনোট https://sketchthedocs.dev](../../translated_images/00-Roadmap.4905d6567dff47532b9bfb8e0b8980fc6b0b1292eebb24181c1a9753b33bc0f5.bn.png)|
|:---:|
| ডেটা সায়েন্স ফর বিগিনার্স: রোডম্যাপ - _[@nitya](https://twitter.com/nitya) দ্বারা স্কেচনোট_ |

| পাঠ নম্বর | বিষয় | পাঠের বিভাগ | শেখার উদ্দেশ্য | লিঙ্ককৃত পাঠ | লেখক |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | ডেটা সায়েন্স সংজ্ঞায়িত করা | [ভূমিকা](1-Introduction/README.md) | ডেটা সায়েন্সের মৌলিক ধারণাগুলি এবং এটি কীভাবে কৃত্রিম বুদ্ধিমত্তা, মেশিন লার্নিং এবং বিগ ডেটার সাথে সম্পর্কিত তা শিখুন। | [পাঠ](1-Introduction/01-defining-data-science/README.md) [ভিডিও](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | ডেটা সায়েন্স নৈতিকতা | [ভূমিকা](1-Introduction/README.md) | ডেটা নৈতিকতার ধারণা, চ্যালেঞ্জ এবং কাঠামো। | [পাঠ](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | ডেটা সংজ্ঞায়িত করা | [ভূমিকা](1-Introduction/README.md) | ডেটা কীভাবে শ্রেণীবদ্ধ হয় এবং এর সাধারণ উৎস। | [পাঠ](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | পরিসংখ্যান ও সম্ভাবনার পরিচিতি | [ভূমিকা](1-Introduction/README.md) | ডেটা বোঝার জন্য সম্ভাবনা এবং পরিসংখ্যানের গাণিতিক কৌশল। | [পাঠ](1-Introduction/04-stats-and-probability/README.md) [ভিডিও](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | সম্পর্কিত ডেটার সাথে কাজ করা | [ডেটার সাথে কাজ করা](2-Working-With-Data/README.md) | সম্পর্কিত ডেটার পরিচিতি এবং SQL (যাকে "see-quell" বলা হয়) নামে পরিচিত স্ট্রাকচার্ড কোয়েরি ল্যাঙ্গুয়েজ ব্যবহার করে সম্পর্কিত ডেটা অন্বেষণ এবং বিশ্লেষণের মৌলিক বিষয়। | [পাঠ](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | NoSQL ডেটার সাথে কাজ করা | [ডেটার সাথে কাজ করা](2-Working-With-Data/README.md) | অ-সম্পর্কিত ডেটার পরিচিতি, এর বিভিন্ন প্রকার এবং ডকুমেন্ট ডেটাবেস অন্বেষণ এবং বিশ্লেষণের মৌলিক বিষয়। | [পাঠ](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | পাইথনের সাথে কাজ করা | [ডেটার সাথে কাজ করা](2-Working-With-Data/README.md) | Pandas-এর মতো লাইব্রেরি ব্যবহার করে ডেটা অন্বেষণের জন্য পাইথন ব্যবহার করার মৌলিক বিষয়। পাইথন প্রোগ্রামিংয়ের প্রাথমিক ধারণা সুপারিশ করা হয়। | [পাঠ](2-Working-With-Data/07-python/README.md) [ভিডিও](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | ডেটা প্রস্তুতি | [ডেটার সাথে কাজ করা](2-Working-With-Data/README.md) | ডেটা পরিষ্কার এবং রূপান্তর করার কৌশলগুলি, যেমন অনুপস্থিত, ভুল বা অসম্পূর্ণ ডেটা পরিচালনা। | [পাঠ](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | পরিমাণের ভিজ্যুয়ালাইজেশন | [ডেটা ভিজ্যুয়ালাইজেশন](3-Data-Visualization/README.md) | Matplotlib ব্যবহার করে পাখির ডেটা 🦆 ভিজ্যুয়ালাইজ করতে শিখুন। | [পাঠ](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | ডেটার বিতরণ ভিজ্যুয়ালাইজেশন | [ডেটা ভিজ্যুয়ালাইজেশন](3-Data-Visualization/README.md) | একটি অন্তরালের পর্যবেক্ষণ এবং প্রবণতা ভিজ্যুয়ালাইজ করা। | [পাঠ](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | অনুপাতের ভিজ্যুয়ালাইজেশন | [ডেটা ভিজ্যুয়ালাইজেশন](3-Data-Visualization/README.md) | পৃথক এবং গোষ্ঠীভুক্ত শতাংশের ভিজ্যুয়ালাইজেশন। | [পাঠ](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | সম্পর্কের ভিজ্যুয়ালাইজেশন | [ডেটা ভিজ্যুয়ালাইজেশন](3-Data-Visualization/README.md) | ডেটার সেট এবং এর ভেরিয়েবলগুলির মধ্যে সংযোগ এবং সম্পর্কের ভিজ্যুয়ালাইজেশন। | [পাঠ](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | অর্থপূর্ণ ভিজ্যুয়ালাইজেশন | [ডেটা ভিজ্যুয়ালাইজেশন](3-Data-Visualization/README.md) | কার্যকর সমস্যা সমাধান এবং অন্তর্দৃষ্টির জন্য আপনার ভিজ্যুয়ালাইজেশনকে মূল্যবান করার কৌশল এবং নির্দেশিকা। | [পাঠ](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | ডেটা সায়েন্স লাইফসাইকেলের পরিচিতি | [লাইফসাইকেল](4-Data-Science-Lifecycle/README.md) | ডেটা সায়েন্স লাইফসাইকেলের পরিচিতি এবং ডেটা সংগ্রহ ও নিষ্কাশনের প্রথম ধাপ। | [পাঠ](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | বিশ্লেষণ | [লাইফসাইকেল](4-Data-Science-Lifecycle/README.md) | ডেটা বিশ্লেষণের কৌশলগুলির উপর ভিত্তি করে ডেটা সায়েন্স লাইফসাইকেলের এই ধাপ। | [পাঠ](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | যোগাযোগ | [লাইফসাইকেল](4-Data-Science-Lifecycle/README.md) | ডেটা থেকে অন্তর্দৃষ্টি উপস্থাপন করার কৌশল, যা সিদ্ধান্ত গ্রহণকারীদের জন্য বোঝা সহজ করে। | [পাঠ](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | ক্লাউডে ডেটা সায়েন্স | [ক্লাউড ডেটা](5-Data-Science-In-Cloud/README.md) | ক্লাউডে ডেটা সায়েন্স এবং এর সুবিধাগুলির পরিচিতি। | [পাঠ](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) এবং [Maud](https://twitter.com/maudstweets) |
| 18 | ক্লাউডে ডেটা সায়েন্স | [ক্লাউড ডেটা](5-Data-Science-In-Cloud/README.md) | লো কোড টুল ব্যবহার করে মডেল প্রশিক্ষণ। |[পাঠ](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) এবং [Maud](https://twitter.com/maudstweets) |
| 19 | ক্লাউডে ডেটা সায়েন্স | [ক্লাউড ডেটা](5-Data-Science-In-Cloud/README.md) | Azure Machine Learning Studio ব্যবহার করে মডেল ডিপ্লয় করা। | [পাঠ](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) এবং [Maud](https://twitter.com/maudstweets) |
| 20 | বাস্তব জীবনে ডেটা সায়েন্স | [ইন দ্য ওয়াইল্ড](6-Data-Science-In-Wild/README.md) | বাস্তব জীবনের ডেটা সায়েন্স চালিত প্রকল্প। | [পাঠ](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

Codespace-এ এই নমুনা খুলতে নিম্নলিখিত ধাপগুলি অনুসরণ করুন:
1. Code ড্রপ-ডাউন মেনুতে ক্লিক করুন এবং Open with Codespaces অপশনটি নির্বাচন করুন।
2. প্যানেলের নিচে + New codespace নির্বাচন করুন।
আরও তথ্যের জন্য, [GitHub ডকুমেন্টেশন](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace) দেখুন।

## VSCode Remote - Containers
আপনার স্থানীয় মেশিন এবং VSCode ব্যবহার করে এই রিপোজিটরি একটি কন্টেইনারে খুলতে নিম্নলিখিত ধাপগুলি অনুসরণ করুন:

1. যদি এটি আপনার প্রথমবার ডেভেলপমেন্ট কন্টেইনার ব্যবহার হয়, তাহলে নিশ্চিত করুন যে আপনার সিস্টেম প্রয়োজনীয়তা পূরণ করে (যেমন Docker ইনস্টল করা আছে) [শুরু করার ডকুমেন্টেশন](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started) এ।

এই রিপোজিটরি ব্যবহার করতে, আপনি হয় রিপোজিটরিটি একটি বিচ্ছিন্ন Docker ভলিউমে খুলতে পারেন:

**নোট**: ভিতরে, এটি Remote-Containers: **Clone Repository in Container Volume...** কমান্ড ব্যবহার করবে, যা স্থানীয় ফাইল সিস্টেমের পরিবর্তে Docker ভলিউমে সোর্স কোড ক্লোন করবে। [Volumes](https://docs.docker.com/storage/volumes/) ডেটা সংরক্ষণের জন্য পছন্দনীয় পদ্ধতি।

অথবা স্থানীয়ভাবে ক্লোন করা বা ডাউনলোড করা সংস্করণ খুলুন:

- এই রিপোজিটরিটি আপনার স্থানীয় ফাইল সিস্টেমে ক্লোন করুন।
- F1 চাপুন এবং **Remote-Containers: Open Folder in Container...** কমান্ড নির্বাচন করুন।
- এই ফোল্ডারের ক্লোন করা কপি নির্বাচন করুন, কন্টেইনারটি শুরু হওয়ার জন্য অপেক্ষা করুন এবং পরীক্ষা করুন।

## অফলাইন অ্যাক্সেস

আপনি [Docsify](https://docsify.js.org/#/) ব্যবহার করে এই ডকুমেন্টেশন অফলাইনে চালাতে পারেন। এই রিপোজিটরি ফর্ক করুন, [Docsify ইনস্টল করুন](https://docsify.js.org/#/quickstart) আপনার স্থানীয় মেশিনে, তারপর এই রিপোজিটরির মূল ফোল্ডারে `docsify serve` টাইপ করুন। ওয়েবসাইটটি আপনার লোকালহোস্টে পোর্ট 3000-এ পরিবেশন করা হবে: `localhost:3000`।

> নোট, নোটবুকগুলি Docsify-এর মাধ্যমে রেন্ডার করা হবে না, তাই যখন আপনাকে একটি নোটবুক চালাতে হবে, তখন এটি আলাদাভাবে VS Code-এ একটি পাইথন কার্নেল চালিয়ে করুন।

## অন্যান্য পাঠ্যক্রম

আমাদের দল অন্যান্য পাঠ্যক্রম তৈরি করে! দেখুন:

- [Generative AI for Beginners](https://aka.ms/genai-beginners)
- [Generative AI for Beginners .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI with JavaScript](https://github.com/microsoft/generative-ai-with-javascript)
- [Generative AI with Java](https://aka.ms/genaijava)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101) 
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [XR Development for Beginners](https://github.com/microsoft/xr-development-for-beginners)
- [Mastering GitHub Copilot for Paired Programming](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)
- [Mastering GitHub Copilot for C#/.NET Developers](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers)
- [Choose Your Own Copilot Adventure](https://github.com/microsoft/CopilotAdventures)

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিক অনুবাদের চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। নথিটির মূল ভাষায় লেখা সংস্করণটিকেই প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ ব্যবহার করার পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।