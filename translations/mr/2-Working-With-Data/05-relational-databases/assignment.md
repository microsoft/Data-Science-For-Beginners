<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:54:16+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "mr"
}
-->
# विमानतळ डेटा प्रदर्शित करणे

तुम्हाला [SQLite](https://sqlite.org/index.html) वर आधारित एक [डेटाबेस](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) प्रदान करण्यात आला आहे ज्यामध्ये विमानतळांची माहिती आहे. खाली स्कीमा दर्शवले आहे. तुम्ही [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) मधील [SQLite विस्तार](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) वापरून विविध शहरांच्या विमानतळांची माहिती प्रदर्शित कराल.

## सूचना

असाइनमेंट सुरू करण्यासाठी, तुम्हाला काही चरण पूर्ण करावे लागतील. तुम्हाला काही साधने स्थापित करावी लागतील आणि नमुना डेटाबेस डाउनलोड करावा लागेल.

### तुमची प्रणाली सेट करा

डेटाबेसशी संवाद साधण्यासाठी तुम्ही Visual Studio Code आणि SQLite विस्तार वापरू शकता.

1. [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) वर जा आणि Visual Studio Code स्थापित करण्याच्या सूचनांचे अनुसरण करा
1. [SQLite विस्तार](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) स्थापित करा, ज्यासाठी मार्केटप्लेस पृष्ठावरील सूचनांचे अनुसरण करा

### डेटाबेस डाउनलोड करा आणि उघडा

पुढे, तुम्ही डेटाबेस डाउनलोड करून उघडाल.

1. [GitHub वरून डेटाबेस फाइल डाउनलोड करा](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) आणि ती एका निर्देशिकेत सेव्ह करा
1. Visual Studio Code उघडा
1. SQLite विस्तारामध्ये डेटाबेस उघडण्यासाठी **Ctl-Shift-P** (किंवा Mac वर **Cmd-Shift-P**) निवडा आणि `SQLite: Open database` टाइप करा
1. **Choose database from file** निवडा आणि तुम्ही पूर्वी डाउनलोड केलेली **airports.db** फाइल उघडा
1. डेटाबेस उघडल्यानंतर (स्क्रीनवर कोणताही अपडेट दिसणार नाही), नवीन क्वेरी विंडो तयार करण्यासाठी **Ctl-Shift-P** (किंवा Mac वर **Cmd-Shift-P**) निवडा आणि `SQLite: New query` टाइप करा

एकदा उघडल्यानंतर, नवीन क्वेरी विंडो डेटाबेसवर SQL स्टेटमेंट्स चालवण्यासाठी वापरली जाऊ शकते. तुम्ही **Ctl-Shift-Q** (किंवा Mac वर **Cmd-Shift-Q**) कमांड वापरून डेटाबेसवर क्वेरी चालवू शकता.

> [!NOTE] 
> SQLite विस्ताराबद्दल अधिक माहितीसाठी, तुम्ही [प्रलेखन](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) सल्ला घेऊ शकता.

## डेटाबेस स्कीमा

डेटाबेसची स्कीमा म्हणजे त्याची टेबल डिझाइन आणि रचना. **airports** डेटाबेसमध्ये दोन टेबल्स आहेत, `cities`, ज्यामध्ये युनायटेड किंगडम आणि आयर्लंडमधील शहरांची यादी आहे, आणि `airports`, ज्यामध्ये सर्व विमानतळांची यादी आहे. काही शहरांमध्ये एकापेक्षा जास्त विमानतळ असू शकतात, म्हणून माहिती साठवण्यासाठी दोन टेबल्स तयार करण्यात आले. या व्यायामामध्ये तुम्ही वेगवेगळ्या शहरांसाठी माहिती प्रदर्शित करण्यासाठी जॉइन्स वापराल.

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

| उत्कृष्ट | पुरेसे | सुधारणा आवश्यक |
| --------- | -------- | ----------------- |

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून निर्माण झालेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.