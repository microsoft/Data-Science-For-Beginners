<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-27T16:44:37+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "ne"
}
-->
# विमानस्थलको डेटा देखाउने

तपाईंलाई [SQLite](https://sqlite.org/index.html) मा आधारित [डाटाबेस](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) प्रदान गरिएको छ जसमा विमानस्थलहरूको जानकारी समावेश छ। स्किमालाई तल देखाइएको छ। तपाईं [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) मा [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) प्रयोग गरेर विभिन्न शहरहरूको विमानस्थलहरूको जानकारी देखाउनुहुनेछ।

## निर्देशनहरू

यस असाइनमेन्ट सुरु गर्नका लागि, तपाईंले केही चरणहरू पूरा गर्नुपर्नेछ। तपाईंले केही उपकरणहरू स्थापना गर्नुपर्नेछ र नमूना डाटाबेस डाउनलोड गर्नुपर्नेछ।

### आफ्नो प्रणाली सेटअप गर्नुहोस्

तपाईं Visual Studio Code र SQLite extension प्रयोग गरेर डाटाबेससँग अन्तरक्रिया गर्न सक्नुहुन्छ।

1. [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) मा जानुहोस् र Visual Studio Code स्थापना गर्नका लागि निर्देशनहरू पालना गर्नुहोस्।
1. [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) स्थापना गर्नुहोस् जसरी Marketplace पृष्ठमा निर्देशन दिइएको छ।

### डाटाबेस डाउनलोड र खोल्नुहोस्

अब तपाईंले डाटाबेस डाउनलोड र खोल्नु पर्नेछ।

1. [GitHub बाट डाटाबेस फाइल](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) डाउनलोड गर्नुहोस् र यसलाई कुनै डाइरेक्टरीमा सुरक्षित गर्नुहोस्।
1. Visual Studio Code खोल्नुहोस्।
1. SQLite extension मा डाटाबेस खोल्नका लागि **Ctl-Shift-P** (वा Mac मा **Cmd-Shift-P**) चयन गर्नुहोस् र `SQLite: Open database` टाइप गर्नुहोस्।
1. **Choose database from file** चयन गर्नुहोस् र पहिले डाउनलोड गरिएको **airports.db** फाइल खोल्नुहोस्।
1. डाटाबेस खोलिसकेपछि (स्क्रिनमा कुनै अपडेट देखिने छैन), नयाँ क्वेरी विन्डो सिर्जना गर्नका लागि **Ctl-Shift-P** (वा Mac मा **Cmd-Shift-P**) चयन गर्नुहोस् र `SQLite: New query` टाइप गर्नुहोस्।

एकपटक खोलिसकेपछि, नयाँ क्वेरी विन्डो डाटाबेसमा SQL स्टेटमेन्टहरू चलाउन प्रयोग गर्न सकिन्छ। तपाईं **Ctl-Shift-Q** (वा Mac मा **Cmd-Shift-Q**) कमाण्ड प्रयोग गरेर डाटाबेसमा क्वेरीहरू चलाउन सक्नुहुन्छ।

> [!NOTE] SQLite extension को बारेमा थप जानकारीका लागि, तपाईं [डकुमेन्टेशन](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) परामर्श गर्न सक्नुहुन्छ।

## डाटाबेस स्किमा

डाटाबेसको स्किमा यसको टेबल डिजाइन र संरचना हो। **airports** डाटाबेसमा दुई टेबलहरू छन्, `cities`, जसमा संयुक्त अधिराज्य र आयरल्याण्डका शहरहरूको सूची छ, र `airports`, जसमा सबै विमानस्थलहरूको सूची छ। किनभने केही शहरहरूमा धेरै विमानस्थलहरू हुन सक्छन्, दुई टेबलहरू जानकारी भण्डारण गर्नका लागि सिर्जना गरिएको थियो। यस अभ्यासमा तपाईंले विभिन्न शहरहरूको जानकारी देखाउनका लागि जोइनहरू प्रयोग गर्नुहुनेछ।

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

## असाइनमेन्ट

निम्न जानकारी फिर्ता गर्नका लागि क्वेरीहरू सिर्जना गर्नुहोस्:

1. `Cities` टेबलमा सबै शहरका नामहरू।
1. `Cities` टेबलमा आयरल्याण्डका सबै शहरहरू।
1. सबै विमानस्थलका नामहरू तिनका शहर र देशसँग।
1. लन्डन, संयुक्त अधिराज्यका सबै विमानस्थलहरू।

## मूल्यांकन मापदण्ड

| उत्कृष्ट | पर्याप्त | सुधार आवश्यक |

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी यथासम्भव शुद्धताको प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। यसको मूल भाषामा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुने छैनौं।