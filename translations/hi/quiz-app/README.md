<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-24T22:13:19+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "hi"
}
-->
# क्विज़

ये क्विज़ डेटा साइंस पाठ्यक्रम के लिए प्री- और पोस्ट-लेक्चर क्विज़ हैं, जो https://aka.ms/datascience-beginners पर उपलब्ध है।  
## अनुवादित क्विज़ सेट जोड़ना

क्विज़ का अनुवाद जोड़ने के लिए, `assets/translations` फोल्डर में समान क्विज़ संरचनाएँ बनाएं। मूल क्विज़ `assets/translations/en` में हैं। क्विज़ को कई समूहों में विभाजित किया गया है। सुनिश्चित करें कि सही क्विज़ सेक्शन के साथ नंबरिंग मेल खाती हो। इस पाठ्यक्रम में कुल 40 क्विज़ हैं, जिनकी गिनती 0 से शुरू होती है।

अनुवाद संपादित करने के बाद, अनुवाद फोल्डर में `index.js` फ़ाइल को संपादित करें और सभी फाइलों को `en` में दिए गए नियमों के अनुसार इम्पोर्ट करें।

`assets/translations` में `index.js` फ़ाइल को संपादित करें और नई अनुवादित फाइलों को इम्पोर्ट करें।

फिर, इस ऐप में `App.vue` में ड्रॉपडाउन को संपादित करें और अपनी भाषा जोड़ें। स्थानीयकृत संक्षिप्त नाम को आपकी भाषा के फोल्डर नाम से मिलाएं।

अंत में, अनुवादित पाठों में सभी क्विज़ लिंक को संपादित करें, यदि वे मौजूद हैं, ताकि इस स्थानीयकरण को एक क्वेरी पैरामीटर के रूप में शामिल किया जा सके: उदाहरण के लिए `?loc=fr`।  

## प्रोजेक्ट सेटअप

```
npm install
```

### विकास के लिए कंपाइल और हॉट-रिलोड

```
npm run serve
```

### प्रोडक्शन के लिए कंपाइल और मिनिफाई

```
npm run build
```

### फाइलों को लिंट और फिक्स करें

```
npm run lint
```

### कॉन्फ़िगरेशन को कस्टमाइज़ करें

[Configuration Reference](https://cli.vuejs.org/config/) देखें।

श्रेय: इस क्विज़ ऐप के मूल संस्करण के लिए धन्यवाद: https://github.com/arpan45/simple-quiz-vue  

## Azure पर डिप्लॉय करना

यहां एक चरण-दर-चरण गाइड है जो आपको शुरुआत करने में मदद करेगा:

1. GitHub रिपॉजिटरी को फोर्क करें  
सुनिश्चित करें कि आपका स्टैटिक वेब ऐप कोड आपके GitHub रिपॉजिटरी में है। इस रिपॉजिटरी को फोर्क करें।  

2. एक Azure Static Web App बनाएं  
- एक [Azure खाता](http://azure.microsoft.com) बनाएं।  
- [Azure पोर्टल](https://portal.azure.com) पर जाएं।  
- “Create a resource” पर क्लिक करें और “Static Web App” खोजें।  
- “Create” पर क्लिक करें।  

3. Static Web App को कॉन्फ़िगर करें  
- #### बेसिक्स:  
  - Subscription: अपनी Azure सब्सक्रिप्शन चुनें।  
  - Resource Group: एक नया रिसोर्स ग्रुप बनाएं या मौजूदा का उपयोग करें।  
  - Name: अपने स्टैटिक वेब ऐप के लिए एक नाम दें।  
  - Region: अपने उपयोगकर्ताओं के सबसे नजदीकी क्षेत्र को चुनें।  

- #### डिप्लॉयमेंट डिटेल्स:  
  - Source: “GitHub” चुनें।  
  - GitHub Account: Azure को आपके GitHub अकाउंट तक पहुंचने की अनुमति दें।  
  - Organization: अपना GitHub संगठन चुनें।  
  - Repository: वह रिपॉजिटरी चुनें जिसमें आपका स्टैटिक वेब ऐप है।  
  - Branch: वह ब्रांच चुनें जिससे आप डिप्लॉय करना चाहते हैं।  

- #### बिल्ड डिटेल्स:  
  - Build Presets: वह फ्रेमवर्क चुनें जिससे आपका ऐप बना है (जैसे React, Angular, Vue, आदि)।  
  - App Location: वह फोल्डर निर्दिष्ट करें जिसमें आपका ऐप कोड है (जैसे, / यदि यह रूट में है)।  
  - API Location: यदि आपके पास API है, तो उसका स्थान निर्दिष्ट करें (वैकल्पिक)।  
  - Output Location: वह फोल्डर निर्दिष्ट करें जहां बिल्ड आउटपुट उत्पन्न होता है (जैसे, build या dist)।  

4. रिव्यू और क्रिएट  
अपनी सेटिंग्स की समीक्षा करें और “Create” पर क्लिक करें। Azure आवश्यक संसाधनों को सेटअप करेगा और आपके रिपॉजिटरी में एक GitHub Actions वर्कफ़्लो बनाएगा।  

5. GitHub Actions वर्कफ़्लो  
Azure स्वचालित रूप से आपके रिपॉजिटरी में एक GitHub Actions वर्कफ़्लो फ़ाइल बनाएगा (.github/workflows/azure-static-web-apps-<name>.yml)। यह वर्कफ़्लो बिल्ड और डिप्लॉयमेंट प्रक्रिया को संभालेगा।  

6. डिप्लॉयमेंट की निगरानी करें  
अपने GitHub रिपॉजिटरी में “Actions” टैब पर जाएं।  
आपको एक वर्कफ़्लो चलते हुए दिखेगा। यह वर्कफ़्लो आपके स्टैटिक वेब ऐप को Azure पर बिल्ड और डिप्लॉय करेगा।  
जैसे ही वर्कफ़्लो पूरा होता है, आपका ऐप प्रदान किए गए Azure URL पर लाइव हो जाएगा।  

### उदाहरण वर्कफ़्लो फ़ाइल

यहां GitHub Actions वर्कफ़्लो फ़ाइल का एक उदाहरण है:  
name: Azure Static Web Apps CI/CD  
```
on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened, closed]
    branches:
      - main

jobs:
  build_and_deploy_job:
    runs-on: ubuntu-latest
    name: Build and Deploy Job
    steps:
      - uses: actions/checkout@v2
      - name: Build And Deploy
        id: builddeploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN }}
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          action: "upload"
          app_location: "quiz-app" # App source code path
          api_location: ""API source code path optional
          output_location: "dist" #Built app content directory - optional
```  

### अतिरिक्त संसाधन  
- [Azure Static Web Apps Documentation](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions Documentation](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।