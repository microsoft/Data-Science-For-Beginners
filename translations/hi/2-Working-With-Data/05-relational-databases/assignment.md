<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:53:55+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "hi"
}
-->
# हवाई अड्डे का डेटा प्रदर्शित करना

आपको [SQLite](https://sqlite.org/index.html) पर आधारित एक [डेटाबेस](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) प्रदान किया गया है, जिसमें हवाई अड्डों की जानकारी है। नीचे स्कीमा प्रदर्शित किया गया है। आप [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) में [SQLite एक्सटेंशन](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) का उपयोग करके विभिन्न शहरों के हवाई अड्डों की जानकारी प्रदर्शित करेंगे।

## निर्देश

असाइनमेंट शुरू करने के लिए, आपको कुछ चरणों का पालन करना होगा। आपको कुछ टूल्स इंस्टॉल करने और सैंपल डेटाबेस डाउनलोड करने की आवश्यकता होगी।

### अपने सिस्टम को सेटअप करें

डेटाबेस के साथ इंटरैक्ट करने के लिए आप Visual Studio Code और SQLite एक्सटेंशन का उपयोग कर सकते हैं।

1. [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) पर जाएं और Visual Studio Code इंस्टॉल करने के निर्देशों का पालन करें।
1. [SQLite एक्सटेंशन](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) को मार्केटप्लेस पेज पर दिए गए निर्देशों के अनुसार इंस्टॉल करें।

### डेटाबेस डाउनलोड करें और खोलें

अब आप डेटाबेस डाउनलोड करेंगे और उसे खोलेंगे।

1. [GitHub से डेटाबेस फाइल डाउनलोड करें](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) और इसे किसी डायरेक्टरी में सेव करें।
1. Visual Studio Code खोलें।
1. SQLite एक्सटेंशन में डेटाबेस खोलने के लिए **Ctl-Shift-P** (या Mac पर **Cmd-Shift-P**) दबाएं और `SQLite: Open database` टाइप करें।
1. **Choose database from file** चुनें और पहले डाउनलोड की गई **airports.db** फाइल खोलें।
1. डेटाबेस खोलने के बाद (स्क्रीन पर कोई अपडेट नहीं दिखेगा), एक नया क्वेरी विंडो बनाने के लिए **Ctl-Shift-P** (या Mac पर **Cmd-Shift-P**) दबाएं और `SQLite: New query` टाइप करें।

एक बार खुलने के बाद, नया क्वेरी विंडो डेटाबेस पर SQL स्टेटमेंट्स चलाने के लिए उपयोग किया जा सकता है। आप **Ctl-Shift-Q** (या Mac पर **Cmd-Shift-Q**) कमांड का उपयोग करके डेटाबेस पर क्वेरी चला सकते हैं।

> [!NOTE] 
> SQLite एक्सटेंशन के बारे में अधिक जानकारी के लिए आप [डॉक्यूमेंटेशन](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) देख सकते हैं।

## डेटाबेस स्कीमा

डेटाबेस का स्कीमा उसकी टेबल डिज़ाइन और संरचना है। **airports** डेटाबेस में दो टेबल हैं, `cities`, जिसमें यूनाइटेड किंगडम और आयरलैंड के शहरों की सूची है, और `airports`, जिसमें सभी हवाई अड्डों की सूची है। क्योंकि कुछ शहरों में कई हवाई अड्डे हो सकते हैं, जानकारी को स्टोर करने के लिए दो टेबल बनाई गई हैं। इस अभ्यास में आप जोइन का उपयोग करके विभिन्न शहरों की जानकारी प्रदर्शित करेंगे।

| Cities           |
| ---------------- |
| id (PK, integer) |
| city (text)      |
| country (text)   |

| Airports                         |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK to id in **Cities**) |

## असाइनमेंट

निम्नलिखित जानकारी लौटाने के लिए क्वेरी बनाएं:

1. `Cities` टेबल में सभी शहरों के नाम।
1. `Cities` टेबल में आयरलैंड के सभी शहर।
1. सभी हवाई अड्डों के नाम उनके शहर और देश के साथ।
1. लंदन, यूनाइटेड किंगडम के सभी हवाई अड्डे।

## मूल्यांकन मानदंड

| उत्कृष्ट | पर्याप्त | सुधार की आवश्यकता |

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।