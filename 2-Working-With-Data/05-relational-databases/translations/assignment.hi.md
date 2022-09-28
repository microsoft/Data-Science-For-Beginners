# हवाईअड्डा डेटा प्रदर्शित करना

आपको एक [डेटाबेस](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) प्रदान किया जायेगा। बनाया गया है [SQLite](https://sqlite.org/index.html) पर जिसमें हवाई अड्डों के बारे में जानकारी होती है। स्कीमा नीचे प्रदर्शित किया गया है। आप [विजुअल स्टूडियो कोड](https://code.visualstudio.com/) में [SQLite एक्सटेंशन](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) का इस्तेमाल करेंगे। Visualstudio.com?WT.mc_id=academic-77958-bethanycheum) विभिन्न शहरों के हवाई अड्डों के बारे में जानकारी प्रदर्शित करने के लिए।

## निर्देश

असाइनमेंट के साथ आरंभ करने के लिए, आपको कुछ चरणों का पालन करना होगा। आपको कुछ टूलींग स्थापित करने और नमूना डेटाबेस डाउनलोड करने की आवश्यकता होगी।

### अपना सिस्टम सेटअप करें

आप डेटाबेस के साथ इंटरैक्ट करने के लिए विजुअल स्टूडियो कोड और SQLite एक्सटेंशन का उपयोग कर सकते हैं।

1. [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) पर नेविगेट करें और विजुअल स्टूडियो कोड इंस्टॉल करने के लिए निर्देशों का पालन करें
1. मार्केटप्लेस पेज पर दिए निर्देशों के अनुसार [SQLite एक्सटेंशन](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) एक्सटेंशन इंस्टॉल करें

### डेटाबेस डाउनलोड करें और खोलें

इसके बाद आप एक ओपन डेटाबेस डाउनलोड करेंगे।

1. [GitHub से डेटाबेस फ़ाइल](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) डाउनलोड करें और इसे एक निर्देशिका में सहेजें
1. विजुअल स्टूडियो कोड खोलें
1. SQLite एक्सटेंशन में डेटाबेस को **Ctl-Shift-P** (या मैक पर **Cmd-Shift-P**) चुनकर और `SQLite: Open database` टाइप करके खोलें।
1. **फ़ाइल से डेटाबेस चुनें** चुनें और **airports.db** फ़ाइल खोलें जिसे आपने पहले डाउनलोड किया था
1. डेटाबेस खोलने के बाद (आप स्क्रीन पर अपडेट नहीं देखेंगे), **Ctl-Shift-P** (या मैक पर **Cmd-Shift-P**) का चयन करके एक नई क्वेरी विंडो बनाएं। और `SQLite: new query` टाइप करना

एक बार खुलने के बाद, नई क्वेरी विंडो का उपयोग डेटाबेस के विरुद्ध SQL कथन चलाने के लिए किया जा सकता है। डेटाबेस के विरुद्ध क्वेरी चलाने के लिए आप **Ctl-Shift-Q** (या मैक पर **Cmd-Shift-Q**) कमांड का उपयोग कर सकते हैं।

> [!नोट] SQLite एक्सटेंशन के बारे में अधिक जानकारी के लिए, आप [दस्तावेज़ीकरण](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) से परामर्श कर सकते हैं।

## डेटाबेस स्कीमा

एक डेटाबेस की स्कीमा इसकी टेबल डिजाइन और संरचना है। **airports** डेटाबेस दो तालिकाओं के रूप में, `cities`, जिसमें यूनाइटेड किंगडम और आयरलैंड के शहरों की सूची है, और `airports`, जिसमें सभी हवाई अड्डों की सूची है। क्योंकि कुछ शहरों में कई हवाई अड्डे हो सकते हैं, जानकारी संग्रहीत करने के लिए दो टेबल बनाए गए थे। इस अभ्यास में आप विभिन्न शहरों की जानकारी प्रदर्शित करने के लिए जॉइन का उपयोग करेंगे।

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

## कार्यभार

निम्नलिखित जानकारी वापस करने के लिए प्रश्न बनाएं:

1. `Cities` तालिका में सभी शहर के नाम
1. आयरलैंड के सभी शहर `Cities` तालिका . में
1. सभी हवाई अड्डों के नाम उनके शहर और देश के साथ
1. लंदन, यूनाइटेड किंगडम में सभी हवाई अड्डे

## रूब्रिक

| अनुकरणीय  |   पर्याप्त   |   सुधार की जरूरत  |
| --------- | -------- | ----------------- |
