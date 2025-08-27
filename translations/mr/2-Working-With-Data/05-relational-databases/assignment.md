<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-27T16:44:17+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "mr"
}
-->
# विमानतळ डेटा प्रदर्शित करणे

तुम्हाला [SQLite](https://sqlite.org/index.html) वर आधारित एक [डेटाबेस](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) प्रदान करण्यात आला आहे, ज्यामध्ये विमानतळांची माहिती आहे. त्याची स्कीमा खाली दर्शविली आहे. तुम्ही [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) मधील [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) चा वापर करून विविध शहरांच्या विमानतळांची माहिती प्रदर्शित कराल.

## सूचना

असाइनमेंट सुरू करण्यासाठी, तुम्हाला काही पायऱ्या पार पाडाव्या लागतील. तुम्हाला काही साधने स्थापित करावी लागतील आणि नमुना डेटाबेस डाउनलोड करावा लागेल.

### तुमची प्रणाली सेटअप करा

डेटाबेसशी संवाद साधण्यासाठी तुम्ही Visual Studio Code आणि SQLite extension चा वापर करू शकता.

1. [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) वर जा आणि Visual Studio Code स्थापित करण्यासाठी दिलेल्या सूचनांचे पालन करा
1. [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) स्थापित करा, जसे की मार्केटप्लेस पृष्ठावर दिले आहे

### डेटाबेस डाउनलोड करा आणि उघडा

पुढे, तुम्ही डेटाबेस डाउनलोड करून उघडाल.

1. [GitHub वरून डेटाबेस फाइल](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) डाउनलोड करा आणि ती एका डिरेक्टरीमध्ये सेव्ह करा
1. Visual Studio Code उघडा
1. SQLite extension मध्ये डेटाबेस उघडण्यासाठी **Ctl-Shift-P** (किंवा Mac वर **Cmd-Shift-P**) निवडा आणि `SQLite: Open database` टाइप करा
1. **Choose database from file** निवडा आणि तुम्ही पूर्वी डाउनलोड केलेली **airports.db** फाइल उघडा
1. डेटाबेस उघडल्यानंतर (स्क्रीनवर कोणताही बदल दिसणार नाही), **Ctl-Shift-P** (किंवा Mac वर **Cmd-Shift-P**) निवडून आणि `SQLite: New query` टाइप करून एक नवीन क्वेरी विंडो तयार करा

एकदा उघडल्यानंतर, नवीन क्वेरी विंडो डेटाबेसवर SQL स्टेटमेंट्स चालवण्यासाठी वापरली जाऊ शकते. डेटाबेसवर क्वेरी चालवण्यासाठी तुम्ही **Ctl-Shift-Q** (किंवा Mac वर **Cmd-Shift-Q**) कमांड वापरू शकता.

> [!NOTE] SQLite extension बद्दल अधिक माहितीसाठी, तुम्ही [डॉक्युमेंटेशन](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) पाहू शकता

## डेटाबेस स्कीमा

डेटाबेसची स्कीमा म्हणजे त्याची टेबल डिझाइन आणि रचना. **airports** डेटाबेसमध्ये दोन टेबल्स आहेत, `cities`, ज्यामध्ये युनायटेड किंगडम आणि आयर्लंडमधील शहरांची यादी आहे, आणि `airports`, ज्यामध्ये सर्व विमानतळांची यादी आहे. काही शहरांमध्ये एकापेक्षा जास्त विमानतळ असू शकतात, म्हणून माहिती साठवण्यासाठी दोन टेबल्स तयार करण्यात आले आहेत. या सरावामध्ये तुम्ही विविध शहरांसाठी माहिती प्रदर्शित करण्यासाठी जोइन्सचा वापर कराल.

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

खालील माहिती परत करण्यासाठी क्वेरी तयार करा:

1. `Cities` टेबलमधील सर्व शहरांची नावे
1. `Cities` टेबलमधील आयर्लंडमधील सर्व शहरे
1. त्यांच्या शहर आणि देशासह सर्व विमानतळांची नावे
1. लंडन, युनायटेड किंगडममधील सर्व विमानतळ

## मूल्यांकन निकष

| उत्कृष्ट | समाधानकारक | सुधारणा आवश्यक |
| -------- | ----------- | --------------- |

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.