<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7c31d1a22c746b1d0f0582d4f54702ba",
  "translation_date": "2025-12-24T23:07:38+00:00",
  "source_file": "README.md",
  "language_code": "hi"
}
-->
# डेटा साइंस शुरुआती के लिए - एक पाठ्यक्रम

[![GitHub Codespaces में खोलें](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=344191198)

[![GitHub लाइसेंस](https://img.shields.io/github/license/microsoft/Data-Science-For-Beginners.svg)](https://github.com/microsoft/Data-Science-For-Beginners/blob/master/LICENSE)
[![GitHub योगदानकर्ता](https://img.shields.io/github/contributors/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/graphs/contributors/)
[![GitHub मुद्दे](https://img.shields.io/github/issues/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/issues/)
[![GitHub पुल-रिक्वेस्ट](https://img.shields.io/github/issues-pr/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/pulls/)
[![PRs स्वागत](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub वॉचर्स](https://img.shields.io/github/watchers/microsoft/Data-Science-For-Beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/Data-Science-For-Beginners/watchers/)
[![GitHub फोर्क्स](https://img.shields.io/github/forks/microsoft/Data-Science-For-Beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/Data-Science-For-Beginners/network/)
[![GitHub स्टार्स](https://img.shields.io/github/stars/microsoft/Data-Science-For-Beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/Data-Science-For-Beginners/stargazers/)


[![Microsoft Foundry डिस्कॉर्ड](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Microsoft Foundry डेवलपर फ़ोरम](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

Microsoft में Azure Cloud Advocates प्रसन्न हैं कि हम डेटा साइंस के बारे में 10 सप्ताह, 20-लेसन का पाठ्यक्रम पेश कर रहे हैं। प्रत्येक पाठ में प्री-लेसन और पोस्ट-लेसन क्विज़, पाठ को पूरा करने के लिखित निर्देश, एक समाधान, और एक असाइनमेंट शामिल है। हमारी प्रोजेक्ट-आधारित शिक्षण पद्धति आपको बनाते समय सीखने की अनुमति देती है, जो नई क्षमतियों को 'टिकाने' का एक सिद्ध तरीका है।

**हमारे लेखकों को हार्दिक धन्यवाद:** [Jasmine Greenaway](https://www.twitter.com/paladique), [Dmitry Soshnikov](http://soshnikov.com), [Nitya Narasimhan](https://twitter.com/nitya), [Jalen McGee](https://twitter.com/JalenMcG), [Jen Looper](https://twitter.com/jenlooper), [Maud Levy](https://twitter.com/maudstweets), [Tiffany Souterre](https://twitter.com/TiffanySouterre), [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏 विशेष धन्यवाद 🙏 हमारे [Microsoft Student Ambassador](https://studentambassadors.microsoft.com/) लेखकों, समीक्षकों और सामग्री योगदानकर्ताओं को,** प्रमुख रूप से Aaryan Arora, [Aditya Garg](https://github.com/AdityaGarg00), [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/), [Ankita Singh](https://www.linkedin.com/in/ankitasingh007), [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/), [Arpita Das](https://www.linkedin.com/in/arpitadas01/), ChhailBihari Dubey, [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor), [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [Majd Safi](https://www.linkedin.com/in/majd-s/), [Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/), [Miguel Correa](https://www.linkedin.com/in/miguelmque/), [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119), [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum), [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/), [Rohit Yadav](https://www.linkedin.com/in/rty2423), Samridhi Sharma, [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200),
[Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/), [Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/), Yogendrasingh Pawar , [Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/), [Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![स्केचनोट द्वारा @sketchthedocs https://sketchthedocs.dev](../../translated_images/hi/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.png)|
|:---:|
| डेटा साइंस शुरुआती के लिए - _स्केचनोट द्वारा [@nitya](https://twitter.com/nitya)_ |

### 🌐 बहु-भाषा समर्थन

#### GitHub Action के जरिए समर्थित (स्वचालित और हमेशा अपडेट)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[अरबी](../ar/README.md) | [बंगाली](../bn/README.md) | [बुल्गारियाई](../bg/README.md) | [बर्मी (म्यांमार)](../my/README.md) | [चीनी (सरलीकृत)](../zh/README.md) | [चीनी (पारंपरिक, हांगकांग)](../hk/README.md) | [चीनी (पारंपरिक, मकाऊ)](../mo/README.md) | [चीनी (पारंपरिक, ताइवान)](../tw/README.md) | [क्रोएशियाई](../hr/README.md) | [चेक](../cs/README.md) | [डेनिश](../da/README.md) | [डच](../nl/README.md) | [एस्टोनियाई](../et/README.md) | [फिनिश](../fi/README.md) | [फ्रेंच](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हिब्रू](../he/README.md) | [हिंदी](./README.md) | [हंगेरियन](../hu/README.md) | [इंडोनेशियाई](../id/README.md) | [इटालियन](../it/README.md) | [जापानी](../ja/README.md) | [कन्नड़](../kn/README.md) | [कोरियाई](../ko/README.md) | [लिथुआनियाई](../lt/README.md) | [मलय](../ms/README.md) | [मलयालम](../ml/README.md) | [मराठी](../mr/README.md) | [नेपाली](../ne/README.md) | [नाइजीरियाई पिजिन](../pcm/README.md) | [नॉर्वेजियन](../no/README.md) | [फारसी (फ़ारसी)](../fa/README.md) | [पोलिश](../pl/README.md) | [पुर्तगाली (ब्राजील)](../br/README.md) | [पुर्तगाली (पुर्तगाल)](../pt/README.md) | [पंजाबी (गुरुमुखी)](../pa/README.md) | [रोमानियाई](../ro/README.md) | [रूसी](../ru/README.md) | [सर्बियाई (सिरिलिक)](../sr/README.md) | [स्लोवाक](../sk/README.md) | [स्लोवेनियाई](../sl/README.md) | [स्पेनिश](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्वीडिश](../sv/README.md) | [तागालोग (फिलिपिनो)](../tl/README.md) | [तमिल](../ta/README.md) | [तेलुगु](../te/README.md) | [थाई](../th/README.md) | [तुर्की](../tr/README.md) | [यूक्रेनी](../uk/README.md) | [उर्दू](../ur/README.md) | [वियतनामी](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**यदि आप अतिरिक्त अनुवाद चाहते हैं तो समर्थित भाषाएँ [यहाँ](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) सूचीबद्ध हैं**

#### हमारे समुदाय में शामिल हों 
[![Microsoft Foundry डिस्कॉर्ड](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

हमारे पास एक Discord पर "AI के साथ सीखें" सीरीज़ चल रही है, और अधिक जानने और जुड़ने के लिए [Learn with AI Series](https://aka.ms/learnwithai/discord) पर हमारे साथ शामिल हों, 18 - 30 सितंबर, 2025 से। आपको Data Science के लिए GitHub Copilot का उपयोग करने के टिप्स और ट्रिक्स मिलेंगे।

![AI के साथ सीखने की श्रृंखला](../../translated_images/hi/1.2b28cdc6205e26fef6a21817fe5d83ae8b50fbd0a33e9fed0df05845da5b30b6.jpg)

# क्या आप छात्र हैं?

निम्नलिखित संसाधनों के साथ शुरू करें:

- [छात्र हब पेज](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) इस पेज पर, आप शुरुआती संसाधन, छात्र पैक और यहाँ तक कि मुफ्त सर्टिफिकेट वाउचर पाने के तरीके भी पाएंगे। यह एक पेज है जिसे आप बुकमार्क करना चाहेंगे और समय-समय पर चेक करते रहना चाहिए क्योंकि हम कम से कम मासिक आधार पर सामग्री बदलते रहते हैं।
- [Microsoft Learn छात्र एम्बेसडर](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) वैश्विक छात्र एम्बेसडर समुदाय में शामिल हों, यह आपके लिए Microsoft में जाने का एक रास्ता हो सकता है।

# आरंभ करें

## 📚 प्रलेखन

- **[इंस्टॉलेशन गाइड](INSTALLATION.md)** - शुरुआती के लिए कदम-दर-कदम सेटअप निर्देश
- **[उपयोग गाइड](USAGE.md)** - उदाहरण और सामान्य कार्यप्रवाह
- **[समस्या निवारण](TROUBLESHOOTING.md)** - सामान्य समस्याओं के समाधान
- **[योगदान कैसे करें गाइड](CONTRIBUTING.md)** - इस परियोजना में कैसे योगदान दें
- **[शिक्षकों के लिए](for-teachers.md)** - पढ़ाने के मार्गदर्शन और कक्षा संसाधन

## 👨‍🎓 छात्रों के लिए
> **पूरी तरह शुरुआती**: डेटा साइंस में नए हैं? हमारे [शुरुआती-अनुकूल उदाहरणों](examples/README.md) से शुरू करें! ये सरल, अच्छी तरह टिप्पणीकृत उदाहरण आपको पूरे पाठ्यक्रम में जाने से पहले मूल बातें समझने में मदद करेंगे।
> **[छात्र](https://aka.ms/student-page)**: इस पाठ्यक्रम का स्वतंत्र रूप से उपयोग करने के लिए, पूरे रिपो को fork करें और व्यायाम स्वयं पूरा करें, प्री-लेक्चर क्विज़ से शुरू करते हुए। फिर लेक्चर पढ़ें और शेष गतिविधियाँ पूरी करें। समाधान कोड की नकल करने के बजाय पाठों को समझकर परियोजनाएँ बनाने का प्रयास करें; हालांकि, उस कोड को प्रत्येक प्रोजेक्ट-उन्मुख पाठ में /solutions फ़ोल्डरों में उपलब्ध किया गया है। एक और विचार यह होगा कि दोस्तों के साथ एक अध्ययन समूह बनाएं और सामग्री को साथ में देखें। आगे अध्ययन के लिए, हम [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum) की सिफारिश करते हैं।

**त्वरित शुरुआत:**
1. अपनी परिवेश सेटअप करने के लिए [इंस्टॉलेशन गाइड](INSTALLATION.md) देखें
2. पाठ्यक्रम के साथ काम करने के तरीके जानने के लिए [उपयोग गाइड](USAGE.md) की समीक्षा करें
3. पाठ 1 से शुरू करें और क्रमशः आगे बढ़ें
4. सहायता के लिए हमारे [Discord समुदाय](https://aka.ms/ds4beginners/discord) में शामिल हों

## 👩‍🏫 शिक्षकों के लिए

> **शिक्षकगण**: हमने इस पाठ्यक्रम का उपयोग करने के तरीके पर [कुछ सुझाव शामिल किए हैं](for-teachers.md)। हम आपके सुझावों को हमारे [चर्चा मंच](https://github.com/microsoft/Data-Science-For-Beginners/discussions) में सुनना चाहेंगे!

## टीम से मिलें

[![प्रमो वीडियो](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "प्रमो वीडियो")

**गिफ़ द्वारा** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)
> 🎥 ऊपर की छवि पर क्लिक करके परियोजना  इसे बनाने वाले लोगों के बारे में वीडियो देखें!

## शिक्षाशास्त्र

हमने इस पाठ्यक्रम का निर्माण करते समय दो शिक्षण सिद्धांत चुने हैं: यह सुनिश्चित करना कि यह परियोजना-आधारित हो और इसमें बार-बार क्विज़ शामिल हों। इस श्रृंखला के अंत तक, छात्र डेटा साइंस के बुनियादी सिद्धांत सीख लेंगे, जिनमें नैतिक अवधारणाएँ, डेटा तैयारी, डेटा के साथ काम करने के विभिन्न तरीके, डेटा विज़ुअलाइज़ेशन, डेटा विश्लेषण, डेटा साइंस के वास्तविक-विश्व उपयोग के मामले, और भी बहुत कुछ शामिल हैं।

इसके अलावा, क्लास से पहले एक लो-स्टेक्स क्विज़ छात्र के विषय सीखने के इरादे को सेट करता है, जबकि क्लास के बाद दूसरा क्विज़ आगे की जानकारी को सुनिश्चित करता है। यह पाठ्यक्रम लचीला और मज़ेदार बनाने के लिए डिज़ाइन किया गया था और इसे पूरा या आंशिक रूप से लिया जा सकता है। परियोजनाएँ छोटी से शुरू होती हैं और 10 सप्ताह के चक्र के अंत तक क्रमिक रूप से अधिक जटिल हो जाती हैं।

> Find our [आचार संहिता](CODE_OF_CONDUCT.md), [योगदान](CONTRIBUTING.md),  [अनुवाद](TRANSLATIONS.md) guidelines. We welcome your constructive feedback!

## प्रत्येक पाठ में शामिल है:

- वैकल्पिक sketchnote
- वैकल्पिक सहायक वीडियो
- पाठ से पहले वार्मअप क्विज़
- लिखित पाठ
- परियोजना-आधारित पाठों के लिए, परियोजना बनाने के चरण-दर-चरण मार्गदर्शिका
- ज्ञान जांच
- एक चुनौती
- सहायक पढ़ाई
- असाइनमेंट
- [पाठ के बाद क्विज़](https://ff-quizzes.netlify.app/en/)

> **क्विज़ के बारे में एक नोट**: सभी क्विज़ Quiz-App फ़ोल्डर में रखे गए हैं, कुल 40 क्विज़ हैं जिनमें से हर एक में तीन प्रश्न हैं। इन्हें पाठों के भीतर लिंक किया गया है, लेकिन क्विज़ ऐप को स्थानीय रूप से चलाया जा सकता है या Azure पर तैनात किया जा सकता है; `quiz-app` फ़ोल्डर में दिए निर्देशों का पालन करें। इन्हें धीरे-धीरे स्थानीयकृत किया जा रहा है।

## 🎓 शुरुआती-अनुकूल उदाहरण

**डेटा साइंस में नए हैं?** हमने एक विशेष [उदाहरण निर्देशिका](examples/README.md) बनाई है जिसमें सरल, अच्छी तरह टिप्पणी किया गया कोड है ताकि आप शुरू कर सकें:

- 🌟 **Hello World** - आपका पहला डेटा साइंस प्रोग्राम
- 📂 **Loading Data** - डेटासेट पढ़ना और अन्वेषण करना सीखें
- 📊 **Simple Analysis** - सांख्यिकी की गणना करें और पैटर्न खोजें
- 📈 **Basic Visualization** - चार्ट और ग्राफ़ बनाएं
- 🔬 **Real-World Project** - शुरुआत से अंत तक पूर्ण वर्कफ़्लो

प्रत्येक उदाहरण में हर चरण को समझाने वाली विस्तृत टिप्पणियाँ शामिल हैं, जो इसे बिल्कुल शुरुआती लोगों के लिए उपयुक्त बनाती हैं!

👉 **[उदाहरणों से शुरू करें](examples/README.md)** 👈

## Lessons


|![ स्केचनोट द्वारा @sketchthedocs https://sketchthedocs.dev](../../translated_images/hi/00-Roadmap.4905d6567dff47532b9bfb8e0b8980fc6b0b1292eebb24181c1a9753b33bc0f5.png)|
|:---:|
| डेटा साइंस शुरुआती के लिए: रोडमैप - _स्केचनोट द्वारा [@nitya](https://twitter.com/nitya)_ |


| Lesson Number | Topic | Lesson Grouping | Learning Objectives | Linked Lesson | Author |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | डेटा साइंस की परिभाषा | [परिचय](1-Introduction/README.md) | डेटा साइंस के मूल सिद्धांत सीखें और यह कृत्रिम बुद्धिमत्ता, मशीन लर्निंग, और बिग डेटा से कैसे जुड़ा हुआ है। | [पाठ](1-Introduction/01-defining-data-science/README.md) [वीडियो](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | डेटा साइंस नैतिकता | [परिचय](1-Introduction/README.md) | डेटा एथिक्स के सिद्धांत, चुनौतियाँ और ढाँचे। | [पाठ](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | डेटा की परिभाषा | [परिचय](1-Introduction/README.md) | डेटा कैसे वर्गीकृत किया जाता है और इसके सामान्य स्रोत क्या हैं। | [पाठ](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | सांख्यिकी और प्रायिकता का परिचय | [परिचय](1-Introduction/README.md) | डेटा को समझने के लिए प्रायिकता और सांख्यिकी की गणितीय तकनीकें। | [पाठ](1-Introduction/04-stats-and-probability/README.md) [वीडियो](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | रिलेशनल डेटा के साथ काम करना | [डेटा के साथ काम करना](2-Working-With-Data/README.md) | रिलेशनल डेटा का परिचय और Structured Query Language (SQL) के साथ रिलेशनल डेटा का अन्वेषण और विश्लेषण करने की बुनियादी बातें (उच्चारण “see-quell”)। | [पाठ](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | NoSQL डेटा के साथ काम करना | [डेटा के साथ काम करना](2-Working-With-Data/README.md) | नॉन-रिलेशनल डेटा, इसके विभिन्न प्रकार और दस्तावेज़ डेटाबेस की खोज और विश्लेषण करने की बुनियादी बातें। | [पाठ](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | Python के साथ काम करना | [डेटा के साथ काम करना](2-Working-With-Data/README.md) | Pandas जैसी लाइब्रेरीज़ के साथ डेटा अन्वेषण के लिए Python का उपयोग करने के मूल। Python प्रोग्रामिंग की बुनियादी समझ की सिफारिश की जाती है। | [पाठ](2-Working-With-Data/07-python/README.md) [वीडियो](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | डेटा तैयारी | [डेटा के साथ काम करना](2-Working-With-Data/README.md) | गायब, गलत, या अपूर्ण डेटा की चुनौतियों से निपटने के लिए डेटा को साफ़ करने और रूपांतरित करने की डेटा तकनीकों पर विषय। | [पाठ](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | मात्राओं का दृश्यांकन | [डेटा विज़ुअलाइज़ेशन](3-Data-Visualization/README.md) | Matplotlib का उपयोग करके पक्षियों के डेटा को कैसे विज़ुअलाइज़ करें सीखें 🦆 | [पाठ](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | डेटा के वितरणों का दृश्यांकन | [डेटा विज़ुअलाइज़ेशन](3-Data-Visualization/README.md) | किसी अंतराल के भीतर अवलोकनों और रुझानों का दृश्यांकन। | [पाठ](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | अनुपातों का दृश्यांकन | [डेटा विज़ुअलाइज़ेशन](3-Data-Visualization/README.md) | विविक्त और समूहित प्रतिशत का दृश्यांकन। | [पाठ](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | संबंधों का दृश्यांकन | [डेटा विज़ुअलाइज़ेशन](3-Data-Visualization/README.md) | डेटा सेट और उनके वेरिएबल्स के बीच संबंधों और सहसंबंधों का दृश्यांकन। | [पाठ](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | अर्थपूर्ण विज़ुअलाइज़ेशन | [डेटा विज़ुअलाइज़ेशन](3-Data-Visualization/README.md) | प्रभावी समस्या-समाधान और अंतर्दृष्टि के लिए अपनी विज़ुअलाइज़ेशन को मूल्यवान बनाने की तकनीकें और मार्गदर्शन। | [पाठ](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | डेटा साइंस जीवनचक्र का परिचय | [जीवनचक्र](4-Data-Science-Lifecycle/README.md) | डेटा साइंस जीवनचक्र का परिचय और डेटा प्राप्त करने व निकालने का पहला कदम। | [पाठ](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | विश्लेषण | [जीवनचक्र](4-Data-Science-Lifecycle/README.md) | डेटा का विश्लेषण करने की तकनीकों पर यह डेटा साइंस जीवनचक्र का चरण केंद्रित है। | [पाठ](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | संचार | [जीवनचक्र](4-Data-Science-Lifecycle/README.md) | यह चरण डेटा से मिली अंतर्दृष्टियों को इस तरह प्रस्तुत करने पर केंद्रित है कि निर्णय-निर्माताओं के लिए उन्हें समझना आसान हो। | [पाठ](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | क्लाउड में डेटा साइंस | [क्लाउड डेटा](5-Data-Science-In-Cloud/README.md) | इस श्रृंखला के पाठ क्लाउड में डेटा साइंस और इसके लाभों का परिचय देते हैं। | [पाठ](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 18 | क्लाउड में डेटा साइंस | [क्लाउड डेटा](5-Data-Science-In-Cloud/README.md) | Low Code टूल्स का उपयोग करके मॉडल्स को प्रशिक्षित करना। |[पाठ](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 19 | क्लाउड में डेटा साइंस | [क्लाउड डेटा](5-Data-Science-In-Cloud/README.md) | Azure Machine Learning Studio का उपयोग करके मॉडल्स को तैनात करना। | [पाठ](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 20 | वास्तविक दुनिया में डेटा साइंस | [In the Wild](6-Data-Science-In-Wild/README.md) | वास्तविक दुनिया में डेटा साइंस प्रेरित परियोजनाएँ। | [पाठ](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

इन चरणों का पालन करके इस नमूने को एक Codespace में खोलें:
1. Code ड्रॉप-डाउन मेनू पर क्लिक करें और Open with Codespaces विकल्प चुनें।
2. पैन के नीचे + New codespace चुनें।
For more info, check out the [GitHub दस्तावेज़](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace-for-a-repository).

## VSCode Remote - Containers
Follow these steps to open this repo in a container using your local machine and VSCode using  the VS Code Remote - Containers extension:

1. If this is your first time using a development container, please ensure your system meets the pre-reqs (i.e. have Docker installed) in [शुरूआत करने के दस्तावेज़](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started).

To use this repository, you can either open the repository in an isolated Docker volume:

**Note**: Under the hood, this will use the Remote-Containers: **Clone Repository in Container Volume...** command to clone the source code in a Docker volume instead of the local filesystem. [Volumes](https://docs.docker.com/storage/volumes/) are the preferred mechanism for persisting container data.

Or open a locally cloned or downloaded version of the repository:

- Clone this repository to your local filesystem.
- Press F1 and select the **Remote-Containers: Open Folder in Container...** command.
- Select the cloned copy of this folder, wait for the container to start, and try things out.

## Offline access

You can run this documentation offline by using [Docsify](https://docsify.js.org/#/). Fork this repo, [install Docsify](https://docsify.js.org/#/quickstart) on your local machine,  then in the root folder of this repo, type `docsify serve`. The website will be served on port 3000 on your localhost: `localhost:3000`.

> Note, notebooks will not be rendered via Docsify, so when you need to run a notebook, do that separately in VS Code running a Python kernel.

## अन्य पाठ्यक्रम

Our team produces other curricula! Check out:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j - शुरुआती के लिए](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js - शुरुआती के लिए](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD शुरुआती के लिए](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI शुरुआती के लिए](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP शुरुआती के लिए](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents शुरुआती के लिए](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### जनरेटिव AI श्रृंखला
[![जनरेटिव AI शुरुआती के लिए](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![जनरेटिव AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![जनरेटिव AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![जनरेटिव AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### मुख्य शिक्षा
[![ML शुरुआती के लिए](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![डेटा साइंस शुरुआती के लिए](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI शुरुआती के लिए](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![साइबर सुरक्षा शुरुआती के लिए](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![वेब विकास शुरुआती के लिए](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT शुरुआती के लिए](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR विकास शुरुआती के लिए](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot श्रृंखला
[![Copilot AI-पेयर्ड प्रोग्रामिंग के लिए](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET के लिए](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot एडवेंचर](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## सहायता प्राप्त करें

**क्या आप समस्याओं का सामना कर रहे हैं?** सामान्य समस्याओं के समाधान के लिए हमारी [समस्या निवारण मार्गदर्शिका](TROUBLESHOOTING.md) देखें।

यदि आप अटक जाते हैं या AI ऐप्स बनाने के बारे में कोई प्रश्न है तो साथी शिक्षार्थियों और अनुभवी डेवलपर्स के साथ MCP पर चर्चा में शामिल हों। यह एक सहायक समुदाय है जहाँ प्रश्न स्वागत हैं और ज्ञान स्वतंत्र रूप से साझा किया जाता है।

[![Microsoft Foundry डिस्कॉर्ड](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

यदि आपके पास उत्पाद संबंधी प्रतिक्रिया या निर्माण के दौरान त्रुटियाँ हैं, तो जाएँ:

[![Microsoft Foundry डेवलपर फोरम](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा Co-op Translator (https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। हालाँकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या असमानताएँ हो सकती हैं। मूल दस्तावेज़ उसकी मूल भाषा में अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->