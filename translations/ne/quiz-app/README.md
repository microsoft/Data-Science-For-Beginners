<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-27T17:54:45+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "ne"
}
-->
# क्विजहरू

यी क्विजहरू डेटा साइन्स पाठ्यक्रमको लागि प्रि- र पोस्ट-लेक्चर क्विजहरू हुन्, जुन https://aka.ms/datascience-beginners मा उपलब्ध छ।  
## अनुवादित क्विज सेट थप्ने

क्विज अनुवाद थप्न `assets/translations` फोल्डरमा मिल्दो क्विज संरचना सिर्जना गर्नुहोस्। मूल क्विजहरू `assets/translations/en` मा छन्। क्विजहरू विभिन्न समूहहरूमा विभाजित छन्। सही क्विज सेक्सनसँग नम्बरिङ मिलाउन सुनिश्चित गर्नुहोस्। यो पाठ्यक्रममा कुल ४० क्विजहरू छन्, जसको गणना ० बाट सुरु हुन्छ।

अनुवादहरू सम्पादन गरेपछि, अनुवाद फोल्डरको `index.js` फाइल सम्पादन गर्नुहोस् र `en` मा भएका नियमहरू पालना गर्दै सबै फाइलहरू आयात गर्नुहोस्।

`assets/translations` मा रहेको `index.js` फाइल सम्पादन गरेर नयाँ अनुवादित फाइलहरू आयात गर्नुहोस्।

त्यसपछि, यस एपको `App.vue` मा ड्रपडाउन सम्पादन गरेर आफ्नो भाषा थप्नुहोस्। स्थानीयकृत संक्षेप नामलाई तपाईंको भाषाको फोल्डर नामसँग मिलाउनुहोस्।

अन्ततः, अनुवादित पाठहरूमा भएका सबै क्विज लिंकहरू सम्पादन गर्नुहोस्, यदि तिनीहरू छन् भने, यस स्थानीयकरणलाई क्वेरी प्यारामिटरको रूपमा समावेश गर्न: उदाहरणका लागि `?loc=fr`।

## प्रोजेक्ट सेटअप

```
npm install
```

### विकासको लागि कम्पाइल र हॉट-रिलोड

```
npm run serve
```

### उत्पादनको लागि कम्पाइल र मिनिफाइ

```
npm run build
```

### फाइलहरू लिन्ट र फिक्स गर्नुहोस्

```
npm run lint
```

### कन्फिगरेसन अनुकूलन गर्नुहोस्

[Configuration Reference](https://cli.vuejs.org/config/) हेर्नुहोस्।

क्रेडिट: यो क्विज एपको मूल संस्करणलाई धन्यवाद: https://github.com/arpan45/simple-quiz-vue

## Azure मा डिप्लोय गर्नुहोस्

यहाँ सुरु गर्नका लागि चरण-दर-चरण मार्गदर्शन छ:

1. GitHub रिपोजिटरी फोर्क गर्नुहोस्  
तपाईंको स्टाटिक वेब एप कोड GitHub रिपोजिटरीमा सुनिश्चित गर्नुहोस्। यो रिपोजिटरी फोर्क गर्नुहोस्।

2. Azure स्टाटिक वेब एप सिर्जना गर्नुहोस्  
- [Azure खाता](http://azure.microsoft.com) सिर्जना गर्नुहोस्।  
- [Azure पोर्टल](https://portal.azure.com) मा जानुहोस्।  
- “Create a resource” मा क्लिक गर्नुहोस् र “Static Web App” खोज्नुहोस्।  
- “Create” मा क्लिक गर्नुहोस्।  

3. स्टाटिक वेब एप कन्फिगर गर्नुहोस्  
- आधारभूत:  
  - Subscription: तपाईंको Azure सब्सक्रिप्शन चयन गर्नुहोस्।  
  - Resource Group: नयाँ रिसोर्स ग्रुप सिर्जना गर्नुहोस् वा विद्यमान प्रयोग गर्नुहोस्।  
  - Name: तपाईंको स्टाटिक वेब एपको नाम प्रदान गर्नुहोस्।  
  - Region: तपाईंको प्रयोगकर्ताहरू नजिकको क्षेत्र चयन गर्नुहोस्।  

- #### डिप्लोयमेन्ट विवरण:  
  - Source: “GitHub” चयन गर्नुहोस्।  
  - GitHub Account: Azure लाई तपाईंको GitHub खाता पहुँच गर्न अनुमति दिनुहोस्।  
  - Organization: तपाईंको GitHub संगठन चयन गर्नुहोस्।  
  - Repository: तपाईंको स्टाटिक वेब एप समावेश भएको रिपोजिटरी चयन गर्नुहोस्।  
  - Branch: तपाईं डिप्लोय गर्न चाहनुभएको ब्रान्च चयन गर्नुहोस्।  

- #### बिल्ड विवरण:  
  - Build Presets: तपाईंको एप निर्माण गरिएको फ्रेमवर्क चयन गर्नुहोस् (जस्तै React, Angular, Vue, आदि)।  
  - App Location: तपाईंको एप कोड समावेश भएको फोल्डर निर्दिष्ट गर्नुहोस् (जस्तै, / यदि यो रूटमा छ)।  
  - API Location: यदि तपाईंको API छ भने, यसको स्थान निर्दिष्ट गर्नुहोस् (वैकल्पिक)।  
  - Output Location: बिल्ड आउटपुट उत्पन्न हुने फोल्डर निर्दिष्ट गर्नुहोस् (जस्तै, build वा dist)।  

4. समीक्षा र सिर्जना गर्नुहोस्  
तपाईंको सेटिङहरू समीक्षा गर्नुहोस् र “Create” मा क्लिक गर्नुहोस्। Azure आवश्यक स्रोतहरू सेटअप गर्नेछ र तपाईंको रिपोजिटरीमा GitHub Actions वर्कफ्लो सिर्जना गर्नेछ।  

5. GitHub Actions वर्कफ्लो  
Azure स्वचालित रूपमा तपाईंको रिपोजिटरीमा GitHub Actions वर्कफ्लो फाइल (.github/workflows/azure-static-web-apps-<name>.yml) सिर्जना गर्नेछ। यो वर्कफ्लो बिल्ड र डिप्लोयमेन्ट प्रक्रिया ह्यान्डल गर्नेछ।  

6. डिप्लोयमेन्ट अनुगमन गर्नुहोस्  
तपाईंको GitHub रिपोजिटरीको “Actions” ट्याबमा जानुहोस्।  
तपाईंले वर्कफ्लो चलिरहेको देख्नुहुनेछ। यो वर्कफ्लो तपाईंको स्टाटिक वेब एप Azure मा निर्माण र डिप्लोय गर्नेछ।  
वर्कफ्लो पूरा भएपछि, तपाईंको एप प्रदान गरिएको Azure URL मा लाइभ हुनेछ।  

### उदाहरण वर्कफ्लो फाइल

यहाँ GitHub Actions वर्कफ्लो फाइलको उदाहरण छ:  
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

### थप स्रोतहरू  
- [Azure Static Web Apps Documentation](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions Documentation](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटि वा अशुद्धता हुन सक्छ। यसको मूल भाषा मा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।