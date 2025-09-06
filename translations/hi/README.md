<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5443b88ba402d2ec7b000e4de6cecb8",
  "translation_date": "2025-08-30T08:58:36+00:00",
  "source_file": "README.md",
  "language_code": "hi"
}
-->
# शुरुआती लोगों के लिए डेटा साइंस - एक पाठ्यक्रम

Azure Cloud Advocates ने Microsoft में 10 सप्ताह का, 20 पाठों वाला पाठ्यक्रम तैयार किया है, जो पूरी तरह से डेटा साइंस पर आधारित है। हर पाठ में प्री-लेसन और पोस्ट-लेसन क्विज़, पाठ को पूरा करने के लिए लिखित निर्देश, समाधान और एक असाइनमेंट शामिल है। हमारा प्रोजेक्ट-आधारित शिक्षण दृष्टिकोण आपको सीखने के साथ-साथ निर्माण करने का मौका देता है, जो नई स्किल्स को लंबे समय तक याद रखने का एक सिद्ध तरीका है।

**हमारे लेखकों को हार्दिक धन्यवाद:** [जैस्मिन ग्रीनअवे](https://www.twitter.com/paladique), [दिमित्री सॉश्निकोव](http://soshnikov.com), [नित्या नरसिम्हन](https://twitter.com/nitya), [जालेन मैक्गी](https://twitter.com/JalenMcG), [जेन लूपर](https://twitter.com/jenlooper), [मॉड लेवी](https://twitter.com/maudstweets), [टिफ़नी सॉटर](https://twitter.com/TiffanySouterre), [क्रिस्टोफर हैरिसन](https://www.twitter.com/geektrainer)।

**🙏 विशेष धन्यवाद 🙏 हमारे [Microsoft Student Ambassador](https://studentambassadors.microsoft.com/) लेखकों, समीक्षकों और सामग्री योगदानकर्ताओं को,** विशेष रूप से आर्यन अरोड़ा, [आदित्य गर्ग](https://github.com/AdityaGarg00), [अलोंद्रा सांचेज़](https://www.linkedin.com/in/alondra-sanchez-molina/), [अंकिता सिंह](https://www.linkedin.com/in/ankitasingh007), [अनुपम मिश्रा](https://www.linkedin.com/in/anupam--mishra/), [अर्पिता दास](https://www.linkedin.com/in/arpitadas01/), छैल बिहारी दुबे, [डिब्री न्सोफोर](https://www.linkedin.com/in/dibrinsofor), [दिशिता भसीन](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [मज्द साफी](https://www.linkedin.com/in/majd-s/), [मैक्स ब्लम](https://www.linkedin.com/in/max-blum-6036a1186/), [मिगुएल कोरेआ](https://www.linkedin.com/in/miguelmque/), [मोहम्मा इफ्तेखेर (इफ्तु) इब्ने जलाल](https://twitter.com/iftu119), [नवरिन तबस्सुम](https://www.linkedin.com/in/nawrin-tabassum), [रेमंड वांगसा पुत्रा](https://www.linkedin.com/in/raymond-wp/), [रोहित यादव](https://www.linkedin.com/in/rty2423), समृद्धि शर्मा, [सान्या सिन्हा](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200), [शीना नरूला](https://www.linkedin.com/in/sheena-narua-n/), [तौकीर अहमद](https://www.linkedin.com/in/tauqeerahmad5201/), योगेंद्रसिंह पवार, [विदुषी गुप्ता](https://www.linkedin.com/in/vidushi-gupta07/), [जसलीन सोनधी](https://www.linkedin.com/in/jasleen-sondhi/)।

|![@sketchthedocs द्वारा स्केच नोट https://sketchthedocs.dev](../../translated_images/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.hi.png)|
|:---:|
| शुरुआती लोगों के लिए डेटा साइंस - _[@nitya](https://twitter.com/nitya) द्वारा स्केच नोट_ |

### 🌐 बहुभाषी समर्थन

#### GitHub Action के माध्यम से समर्थित (स्वचालित और हमेशा अद्यतन)

[फ्रेंच](../fr/README.md) | [स्पेनिश](../es/README.md) | [जर्मन](../de/README.md) | [रूसी](../ru/README.md) | [अरबी](../ar/README.md) | [फारसी (फारसी)](../fa/README.md) | [उर्दू](../ur/README.md) | [चीनी (सरलीकृत)](../zh/README.md) | [चीनी (पारंपरिक, मकाऊ)](../mo/README.md) | [चीनी (पारंपरिक, हांगकांग)](../hk/README.md) | [चीनी (पारंपरिक, ताइवान)](../tw/README.md) | [जापानी](../ja/README.md) | [कोरियाई](../ko/README.md) | [हिंदी](./README.md) | [बंगाली](../bn/README.md) | [मराठी](../mr/README.md) | [नेपाली](../ne/README.md) | [पंजाबी (गुरमुखी)](../pa/README.md) | [पुर्तगाली (पुर्तगाल)](../pt/README.md) | [पुर्तगाली (ब्राज़ील)](../br/README.md) | [इतालवी](../it/README.md) | [पोलिश](../pl/README.md) | [तुर्की](../tr/README.md) | [ग्रीक](../el/README.md) | [थाई](../th/README.md) | [स्वीडिश](../sv/README.md) | [डेनिश](../da/README.md) | [नॉर्वेजियन](../no/README.md) | [फिनिश](../fi/README.md) | [डच](../nl/README.md) | [हिब्रू](../he/README.md) | [वियतनामी](../vi/README.md) | [इंडोनेशियाई](../id/README.md) | [मलय](../ms/README.md) | [टैगालोग (फिलिपिनो)](../tl/README.md) | [स्वाहिली](../sw/README.md) | [हंगेरियन](../hu/README.md) | [चेक](../cs/README.md) | [स्लोवाक](../sk/README.md) | [रोमानियाई](../ro/README.md) | [बुल्गारियाई](../bg/README.md) | [सर्बियाई (सिरिलिक)](../sr/README.md) | [क्रोएशियाई](../hr/README.md) | [स्लोवेनियाई](../sl/README.md) | [यूक्रेनी](../uk/README.md) | [बर्मी (म्यांमार)](../my/README.md)

**यदि आप अतिरिक्त अनुवाद चाहते हैं, तो समर्थित भाषाओं की सूची [यहां](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) देखें।**

#### हमारे समुदाय से जुड़ें 
[![Azure AI Discord](https://dcbadge.limes.pink/api/server/kzRShWzttr)](https://discord.gg/kzRShWzttr)

# क्या आप एक छात्र हैं?

निम्नलिखित संसाधनों से शुरुआत करें:

- [स्टूडेंट हब पेज](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) इस पेज पर आपको शुरुआती संसाधन, स्टूडेंट पैक्स और यहां तक कि मुफ्त प्रमाणपत्र वाउचर प्राप्त करने के तरीके मिलेंगे। यह एक ऐसा पेज है जिसे आप बुकमार्क करना चाहेंगे और समय-समय पर जांचना चाहेंगे क्योंकि हम कम से कम मासिक रूप से सामग्री बदलते रहते हैं।
- [Microsoft Learn Student Ambassadors](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) एक वैश्विक छात्र एंबेसडर समुदाय में शामिल हों, यह Microsoft में आपका प्रवेश द्वार हो सकता है।

# शुरुआत कैसे करें

> **शिक्षकों के लिए**: हमने इस पाठ्यक्रम का उपयोग करने के लिए [कुछ सुझाव शामिल किए हैं](for-teachers.md)। हमें आपके फीडबैक की आवश्यकता है [हमारे चर्चा मंच में](https://github.com/microsoft/Data-Science-For-Beginners/discussions)!

> **[छात्रों](https://aka.ms/student-page)**: इस पाठ्यक्रम का उपयोग अपने दम पर करने के लिए, पूरे रिपॉजिटरी को फोर्क करें और अपने दम पर अभ्यास पूरा करें, एक प्री-लेक्चर क्विज़ से शुरुआत करें। फिर लेक्चर पढ़ें और बाकी गतिविधियों को पूरा करें। पाठों को समझकर प्रोजेक्ट बनाने का प्रयास करें, समाधान कोड की नकल करने के बजाय; हालांकि, वह कोड प्रत्येक प्रोजेक्ट-उन्मुख पाठ के /solutions फ़ोल्डरों में उपलब्ध है। एक और विचार यह हो सकता है कि दोस्तों के साथ एक अध्ययन समूह बनाएं और सामग्री को एक साथ पढ़ें। आगे की पढ़ाई के लिए, हम [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum) की सिफारिश करते हैं।

## टीम से मिलें

[![प्रोमो वीडियो](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "प्रोमो वीडियो")

**Gif द्वारा** [मोहित जैसल](https://www.linkedin.com/in/mohitjaisal)

> 🎥 ऊपर दी गई छवि पर क्लिक करें इस प्रोजेक्ट और इसे बनाने वाले लोगों के बारे में वीडियो देखने के लिए!

## शिक्षण दृष्टिकोण

हमने इस पाठ्यक्रम को बनाते समय दो शिक्षण सिद्धांतों को अपनाया है: यह सुनिश्चित करना कि यह प्रोजेक्ट-आधारित है और इसमें बार-बार क्विज़ शामिल हैं। इस श्रृंखला के अंत तक, छात्र डेटा साइंस के बुनियादी सिद्धांतों को सीख लेंगे, जिनमें नैतिक अवधारणाएं, डेटा तैयारी, डेटा के साथ काम करने के विभिन्न तरीके, डेटा विज़ुअलाइज़ेशन, डेटा विश्लेषण, डेटा साइंस के वास्तविक जीवन के उपयोग के मामले और अधिक शामिल हैं।

इसके अलावा, कक्षा से पहले एक लो-स्टेक्स क्विज़ छात्र को विषय सीखने के लिए प्रेरित करता है, जबकि कक्षा के बाद का दूसरा क्विज़ आगे की अवधारणाओं को बनाए रखने में मदद करता है। यह पाठ्यक्रम लचीला और मजेदार बनाया गया है और इसे पूरे या आंशिक रूप से लिया जा सकता है। प्रोजेक्ट छोटे से शुरू होते हैं और 10 सप्ताह के चक्र के अंत तक धीरे-धीरे जटिल हो जाते हैं।
हमारे [Code of Conduct](CODE_OF_CONDUCT.md), [Contributing](CONTRIBUTING.md), [Translation](TRANSLATIONS.md) दिशानिर्देश देखें। हम आपके रचनात्मक सुझावों का स्वागत करते हैं!
## प्रत्येक पाठ में शामिल हैं:

- वैकल्पिक स्केच नोट
- वैकल्पिक पूरक वीडियो
- पाठ से पहले वार्मअप क्विज़
- लिखित पाठ
- प्रोजेक्ट-आधारित पाठों के लिए, प्रोजेक्ट बनाने के चरण-दर-चरण निर्देश
- ज्ञान जांच
- एक चुनौती
- पूरक पढ़ाई
- असाइनमेंट
- [पाठ के बाद क्विज़](https://ff-quizzes.netlify.app/en/)

> **क्विज़ के बारे में एक नोट**: सभी क्विज़ `Quiz-App` फ़ोल्डर में संग्रहीत हैं, कुल 40 क्विज़, प्रत्येक में तीन प्रश्न। ये पाठों के भीतर से लिंक किए गए हैं, लेकिन क्विज़ ऐप को स्थानीय रूप से चलाया जा सकता है या Azure पर डिप्लॉय किया जा सकता है; `quiz-app` फ़ोल्डर में दिए गए निर्देशों का पालन करें। इन्हें धीरे-धीरे स्थानीयकृत किया जा रहा है।

## पाठ

|![ Sketchnote by @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Roadmap.4905d6567dff47532b9bfb8e0b8980fc6b0b1292eebb24181c1a9753b33bc0f5.hi.png)|
|:---:|
| डेटा साइंस फॉर बिगिनर्स: रोडमैप - _स्केच नोट [@nitya](https://twitter.com/nitya) द्वारा_ |

| पाठ संख्या | विषय | पाठ समूह | सीखने के उद्देश्य | लिंक किया गया पाठ | लेखक |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | डेटा साइंस को परिभाषित करना | [परिचय](1-Introduction/README.md) | डेटा साइंस के पीछे के बुनियादी अवधारणाओं को समझें और यह कृत्रिम बुद्धिमत्ता, मशीन लर्निंग, और बिग डेटा से कैसे संबंधित है। | [पाठ](1-Introduction/01-defining-data-science/README.md) [वीडियो](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | डेटा साइंस नैतिकता | [परिचय](1-Introduction/README.md) | डेटा नैतिकता की अवधारणाएं, चुनौतियां और फ्रेमवर्क। | [पाठ](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | डेटा को परिभाषित करना | [परिचय](1-Introduction/README.md) | डेटा को कैसे वर्गीकृत किया जाता है और इसके सामान्य स्रोत। | [पाठ](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | सांख्यिकी और संभावना का परिचय | [परिचय](1-Introduction/README.md) | डेटा को समझने के लिए संभावना और सांख्यिकी की गणितीय तकनीकें। | [पाठ](1-Introduction/04-stats-and-probability/README.md) [वीडियो](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | संबंधपरक डेटा के साथ काम करना | [डेटा के साथ काम करना](2-Working-With-Data/README.md) | संबंधपरक डेटा का परिचय और SQL (जिसे "सी-क्वेल" कहा जाता है) के साथ संबंधपरक डेटा का अन्वेषण और विश्लेषण करने की मूल बातें। | [पाठ](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | NoSQL डेटा के साथ काम करना | [डेटा के साथ काम करना](2-Working-With-Data/README.md) | गैर-संबंधपरक डेटा का परिचय, इसके विभिन्न प्रकार और डॉक्यूमेंट डेटाबेस का अन्वेषण और विश्लेषण करने की मूल बातें। | [पाठ](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | Python के साथ काम करना | [डेटा के साथ काम करना](2-Working-With-Data/README.md) | Pandas जैसी लाइब्रेरी के साथ डेटा अन्वेषण के लिए Python का उपयोग करने की मूल बातें। Python प्रोग्रामिंग की बुनियादी समझ की सिफारिश की जाती है। | [पाठ](2-Working-With-Data/07-python/README.md) [वीडियो](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | डेटा तैयारी | [डेटा के साथ काम करना](2-Working-With-Data/README.md) | डेटा को साफ करने और बदलने के लिए तकनीकों पर चर्चा, ताकि गायब, गलत, या अधूरी जानकारी की चुनौतियों को संभाला जा सके। | [पाठ](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | मात्राओं का विज़ुअलाइज़ेशन | [डेटा विज़ुअलाइज़ेशन](3-Data-Visualization/README.md) | Matplotlib का उपयोग करके पक्षी डेटा 🦆 को विज़ुअलाइज़ करना सीखें। | [पाठ](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | डेटा वितरण का विज़ुअलाइज़ेशन | [डेटा विज़ुअलाइज़ेशन](3-Data-Visualization/README.md) | अंतराल के भीतर अवलोकन और रुझानों को विज़ुअलाइज़ करना। | [पाठ](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | अनुपात का विज़ुअलाइज़ेशन | [डेटा विज़ुअलाइज़ेशन](3-Data-Visualization/README.md) | अलग-अलग और समूहित प्रतिशत को विज़ुअलाइज़ करना। | [पाठ](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | संबंधों का विज़ुअलाइज़ेशन | [डेटा विज़ुअलाइज़ेशन](3-Data-Visualization/README.md) | डेटा सेट और उनके वेरिएबल्स के बीच कनेक्शन और सहसंबंध को विज़ुअलाइज़ करना। | [पाठ](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | सार्थक विज़ुअलाइज़ेशन | [डेटा विज़ुअलाइज़ेशन](3-Data-Visualization/README.md) | प्रभावी समस्या समाधान और अंतर्दृष्टि के लिए आपके विज़ुअलाइज़ेशन को मूल्यवान बनाने के लिए तकनीक और मार्गदर्शन। | [पाठ](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | डेटा साइंस जीवनचक्र का परिचय | [जीवनचक्र](4-Data-Science-Lifecycle/README.md) | डेटा साइंस जीवनचक्र और डेटा को प्राप्त करने और निकालने के पहले चरण का परिचय। | [पाठ](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | विश्लेषण करना | [जीवनचक्र](4-Data-Science-Lifecycle/README.md) | डेटा साइंस जीवनचक्र का यह चरण डेटा का विश्लेषण करने की तकनीकों पर केंद्रित है। | [पाठ](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | संचार | [जीवनचक्र](4-Data-Science-Lifecycle/README.md) | डेटा साइंस जीवनचक्र का यह चरण डेटा से अंतर्दृष्टि को इस तरह प्रस्तुत करने पर केंद्रित है कि निर्णय लेने वालों के लिए इसे समझना आसान हो। | [पाठ](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | क्लाउड में डेटा साइंस | [क्लाउड डेटा](5-Data-Science-In-Cloud/README.md) | क्लाउड में डेटा साइंस और इसके लाभों का परिचय। | [पाठ](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) और [Maud](https://twitter.com/maudstweets) |
| 18 | क्लाउड में डेटा साइंस | [क्लाउड डेटा](5-Data-Science-In-Cloud/README.md) | लो कोड टूल्स का उपयोग करके मॉडल को प्रशिक्षित करना। |[पाठ](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) और [Maud](https://twitter.com/maudstweets) |
| 19 | क्लाउड में डेटा साइंस | [क्लाउड डेटा](5-Data-Science-In-Cloud/README.md) | Azure Machine Learning Studio के साथ मॉडल को डिप्लॉय करना। | [पाठ](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) और [Maud](https://twitter.com/maudstweets) |
| 20 | वास्तविक दुनिया में डेटा साइंस | [वाइल्ड में](6-Data-Science-In-Wild/README.md) | वास्तविक दुनिया में डेटा साइंस संचालित परियोजनाएं। | [पाठ](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

Codespace में इस सैंपल को खोलने के लिए इन चरणों का पालन करें:
1. Code ड्रॉप-डाउन मेनू पर क्लिक करें और Open with Codespaces विकल्प चुनें।
2. पैन के नीचे + New codespace चुनें।
अधिक जानकारी के लिए, [GitHub दस्तावेज़](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace) देखें।

## VSCode Remote - Containers
अपने स्थानीय मशीन और VSCode का उपयोग करके इस रिपॉजिटरी को कंटेनर में खोलने के लिए इन चरणों का पालन करें:

1. यदि यह पहली बार है जब आप डेवलपमेंट कंटेनर का उपयोग कर रहे हैं, तो कृपया सुनिश्चित करें कि आपका सिस्टम प्री-रिक्वायरमेंट्स को पूरा करता है (जैसे कि Docker इंस्टॉल हो) [शुरुआती दस्तावेज़](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started) में।

इस रिपॉजिटरी का उपयोग करने के लिए, आप या तो रिपॉजिटरी को एक अलग Docker वॉल्यूम में खोल सकते हैं:

**नोट**: अंदर से, यह Remote-Containers: **Clone Repository in Container Volume...** कमांड का उपयोग करेगा ताकि स्रोत कोड को स्थानीय फाइल सिस्टम के बजाय Docker वॉल्यूम में क्लोन किया जा सके। [Volumes](https://docs.docker.com/storage/volumes/) कंटेनर डेटा को बनाए रखने के लिए पसंदीदा तंत्र हैं।

या रिपॉजिटरी के स्थानीय रूप से क्लोन किए गए या डाउनलोड किए गए संस्करण को खोलें:

- इस रिपॉजिटरी को अपने स्थानीय फाइल सिस्टम पर क्लोन करें।
- F1 दबाएं और **Remote-Containers: Open Folder in Container...** कमांड चुनें।
- इस फ़ोल्डर की क्लोन की गई कॉपी चुनें, कंटेनर के शुरू होने की प्रतीक्षा करें, और चीजों को आज़माएं।

## ऑफलाइन एक्सेस

आप इस दस्तावेज़ को ऑफलाइन [Docsify](https://docsify.js.org/#/) का उपयोग करके चला सकते हैं। इस रिपॉजिटरी को फोर्क करें, [Docsify इंस्टॉल करें](https://docsify.js.org/#/quickstart) अपने स्थानीय मशीन पर, फिर इस रिपॉजिटरी के रूट फ़ोल्डर में `docsify serve` टाइप करें। वेबसाइट आपके localhost पर पोर्ट 3000 पर सर्व की जाएगी: `localhost:3000`।

> नोट, नोटबुक्स Docsify के माध्यम से रेंडर नहीं किए जाएंगे, इसलिए जब आपको नोटबुक चलाने की आवश्यकता हो, तो इसे अलग से VS Code में Python कर्नेल चलाकर करें।

## अन्य पाठ्यक्रम

हमारी टीम अन्य पाठ्यक्रम भी तैयार करती है! देखें:

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

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।