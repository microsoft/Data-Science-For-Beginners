<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-27T17:54:23+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "mr"
}
-->
# क्विझेस

ही क्विझेस डेटा सायन्स अभ्यासक्रमासाठीच्या व्याख्यानांपूर्वी आणि नंतर घेण्यात येणाऱ्या क्विझेस आहेत. अधिक माहितीसाठी https://aka.ms/datascience-beginners येथे भेट द्या.

## अनुवादित क्विझ सेट जोडणे

क्विझचा अनुवाद `assets/translations` फोल्डरमध्ये योग्य रचना तयार करून जोडा. मूळ क्विझेस `assets/translations/en` मध्ये आहेत. क्विझेस वेगवेगळ्या गटांमध्ये विभागल्या आहेत. योग्य क्विझ विभागाशी क्रमांक जुळवून ठेवा. या अभ्यासक्रमात एकूण 40 क्विझेस आहेत, ज्यांची क्रमांकवारी 0 पासून सुरू होते.

अनुवाद संपादित केल्यानंतर, `en` मधील पद्धतींचे अनुसरण करून, अनुवाद फोल्डरमधील `index.js` फाइलमध्ये सर्व फाइल्स आयात करा.

`assets/translations` मधील `index.js` फाइल संपादित करून नवीन अनुवादित फाइल्स आयात करा.

यानंतर, या अॅपमधील `App.vue` मधील ड्रॉपडाउन संपादित करून तुमची भाषा जोडा. तुमच्या भाषेसाठी फोल्डर नावाशी स्थानिक संक्षेप जुळवा.

शेवटी, अनुवादित धड्यांमधील सर्व क्विझ लिंक्स संपादित करा, जर त्या अस्तित्वात असतील, आणि त्यामध्ये स्थानिकीकरण क्वेरी पॅरामीटर समाविष्ट करा: उदाहरणार्थ `?loc=fr`.

## प्रकल्प सेटअप

```
npm install
```

### विकासासाठी संकलन आणि हॉट-रिलोड

```
npm run serve
```

### उत्पादनासाठी संकलन आणि मिनिफिकेशन

```
npm run build
```

### फाइल्स तपासा आणि दुरुस्त्या करा

```
npm run lint
```

### कॉन्फिगरेशन सानुकूलित करा

[कॉन्फिगरेशन संदर्भ](https://cli.vuejs.org/config/) पहा.

क्रेडिट्स: या क्विझ अॅपच्या मूळ आवृत्तीसाठी धन्यवाद: https://github.com/arpan45/simple-quiz-vue

## Azure वर डिप्लॉय करणे

येथे सुरुवात करण्यासाठी चरण-दर-चरण मार्गदर्शिका दिली आहे:

1. GitHub रेपॉझिटरी फोर्क करा  
तुमच्या GitHub रेपॉझिटरीमध्ये तुमच्या स्थिर वेब अॅपचा कोड ठेवा. ही रेपॉझिटरी फोर्क करा.

2. Azure Static Web App तयार करा  
- [Azure खाते](http://azure.microsoft.com) तयार करा  
- [Azure पोर्टल](https://portal.azure.com) वर जा  
- “Create a resource” वर क्लिक करा आणि “Static Web App” शोधा.  
- “Create” वर क्लिक करा.  

3. Static Web App कॉन्फिगर करा  
- #### बेसिक्स:  
  - Subscription: तुमची Azure सबस्क्रिप्शन निवडा.  
  - Resource Group: नवीन रिसोर्स ग्रुप तयार करा किंवा विद्यमान वापरा.  
  - Name: तुमच्या स्थिर वेब अॅपसाठी नाव द्या.  
  - Region: तुमच्या वापरकर्त्यांच्या जवळचा प्रदेश निवडा.  

- #### डिप्लॉयमेंट तपशील:  
  - Source: “GitHub” निवडा.  
  - GitHub Account: Azure ला तुमच्या GitHub खात्याचा प्रवेश अधिकृत करा.  
  - Organization: तुमची GitHub संस्था निवडा.  
  - Repository: तुमच्या स्थिर वेब अॅपचा समावेश असलेली रेपॉझिटरी निवडा.  
  - Branch: ज्या शाखेतून तुम्हाला डिप्लॉय करायचे आहे ती निवडा.  

- #### बिल्ड तपशील:  
  - Build Presets: तुमचे अॅप ज्या फ्रेमवर्कसह तयार केले आहे ते निवडा (उदा. React, Angular, Vue, इ.).  
  - App Location: तुमच्या अॅप कोडचा समावेश असलेला फोल्डर निर्दिष्ट करा (उदा. / जर तो रूटमध्ये असेल).  
  - API Location: जर तुमच्याकडे API असेल, तर त्याचे स्थान निर्दिष्ट करा (पर्यायी).  
  - Output Location: बिल्ड आउटपुट जिथे तयार होते तो फोल्डर निर्दिष्ट करा (उदा. build किंवा dist).  

4. पुनरावलोकन आणि तयार करा  
तुमच्या सेटिंग्ज पुनरावलोकन करा आणि “Create” वर क्लिक करा. Azure आवश्यक संसाधने सेटअप करेल आणि तुमच्या रेपॉझिटरीमध्ये GitHub Actions वर्कफ्लो तयार करेल.  

5. GitHub Actions वर्कफ्लो  
Azure तुमच्या रेपॉझिटरीमध्ये स्वयंचलितपणे GitHub Actions वर्कफ्लो फाइल तयार करेल (.github/workflows/azure-static-web-apps-<name>.yml). हा वर्कफ्लो बिल्ड आणि डिप्लॉयमेंट प्रक्रिया हाताळेल.  

6. डिप्लॉयमेंट मॉनिटर करा  
तुमच्या GitHub रेपॉझिटरीमधील “Actions” टॅबवर जा.  
तुम्हाला वर्कफ्लो चालू असल्याचे दिसेल. हा वर्कफ्लो तुमचा स्थिर वेब अॅप Azure वर बिल्ड आणि डिप्लॉय करेल.  
वर्कफ्लो पूर्ण झाल्यावर, तुमचे अॅप दिलेल्या Azure URL वर लाइव्ह असेल.  

### वर्कफ्लो फाइलचे उदाहरण

GitHub Actions वर्कफ्लो फाइल कशी दिसू शकते याचे उदाहरण येथे आहे:  
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

### अतिरिक्त संसाधने  
- [Azure Static Web Apps दस्तऐवज](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions दस्तऐवज](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.