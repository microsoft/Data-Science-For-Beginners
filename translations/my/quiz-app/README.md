<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-30T19:50:53+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "my"
}
-->
# မေးခွန်းများ

ဒီမေးခွန်းများကတော့ https://aka.ms/datascience-beginners မှာရှိတဲ့ ဒေတာသိပ္ပံ သင်ရိုးညွှန်းတန်းအတွက် သင်ခန်းစာမတိုင်မီနှင့်ပြီးလျှင် မေးခွန်းများဖြစ်ပါတယ်။
## ဘာသာပြန်ထားသော မေးခွန်းအစုတစ်ခု ထည့်သွင်းခြင်း

ဘာသာပြန်ထားသော မေးခွန်းများကို `assets/translations` ဖိုလ်ဒါထဲမှာ မူရင်းမေးခွန်းဖွဲ့စည်းမှုနဲ့ကိုက်ညီအောင် ဖန်တီးပြီး ထည့်သွင်းပါ။ မူရင်းမေးခွန်းများကို `assets/translations/en` မှာတွေ့နိုင်ပါတယ်။ မေးခွန်းများကို အုပ်စုအလိုက် ခွဲထားပါတယ်။ မေးခွန်းအပိုင်းနဲ့အမှတ်စဉ်ကိုမှန်ကန်အောင် သေချာစွာလိုက်နာပါ။ ဒီသင်ရိုးညွှန်းတန်းမှာ စုစုပေါင်း ၄၀ မေးခွန်းရှိပြီး၊ အမှတ်စဉ် ၀ မှစတင်ပါတယ်။

ဘာသာပြန်ထားသော မေးခွန်းများကို ပြင်ဆင်ပြီးနောက်၊ `en` မှာရှိတဲ့ စံနည်းများအတိုင်း translation ဖိုလ်ဒါထဲက `index.js` ဖိုင်ကို ပြင်ဆင်ပြီး ဖိုင်အားလုံးကို import လုပ်ပါ။

ထို့နောက်၊ `assets/translations` ထဲက `index.js` ဖိုင်ကို ပြင်ဆင်ပြီး ဘာသာပြန်ထားသော ဖိုင်အသစ်များကို import လုပ်ပါ။

ပြီးရင် ဒီ app ရဲ့ `App.vue` ထဲမှာ dropdown ကို ပြင်ဆင်ပြီး သင့်ဘာသာစကားကို ထည့်သွင်းပါ။ ဘာသာပြန်ထားသော အတိုကောက်ကို သင့်ဘာသာစကားဖိုလ်ဒါနာမည်နဲ့ ကိုက်ညီအောင်လုပ်ပါ။

နောက်ဆုံးမှာ ဘာသာပြန်ထားသော သင်ခန်းစာများထဲက မေးခွန်းလင့်ခ်အားလုံးကို ပြင်ဆင်ပြီး localization ကို query parameter အနေနဲ့ ထည့်သွင်းပါ။ ဥပမာ - `?loc=fr`။

## ပရောဂျက် စတင်ခြင်း

```
npm install
```

### ဖွံ့ဖြိုးရေးအတွက် Compile နှင့် Hot-reload

```
npm run serve
```

### ထုတ်လုပ်မှုအတွက် Compile နှင့် Minify

```
npm run build
```

### ဖိုင်များကို Lint နှင့် ပြင်ဆင်ခြင်း

```
npm run lint
```

### ဖွဲ့စည်းမှုကို Customize လုပ်ခြင်း

[Configuration Reference](https://cli.vuejs.org/config/) ကိုကြည့်ပါ။

Credit: ဒီမေးခွန်း app ရဲ့ မူရင်းဗားရှင်းအတွက် ကျေးဇူးတင်ပါတယ် - https://github.com/arpan45/simple-quiz-vue

## Azure သို့ Deploy လုပ်ခြင်း

ဒီလမ်းညွှန်ချက်တွေက သင့်ကို စတင်ရန် ကူညီပေးပါမယ် -

1. GitHub Repository ကို Fork လုပ်ပါ  
သင့် Static Web App Code ကို GitHub Repository ထဲမှာထားပါ။ ဒီ Repository ကို Fork လုပ်ပါ။

2. Azure Static Web App တစ်ခု ဖန်တီးပါ  
- [Azure account](http://azure.microsoft.com) တစ်ခု ဖန်တီးပါ  
- [Azure portal](https://portal.azure.com) သို့ သွားပါ  
- “Create a resource” ကိုနှိပ်ပြီး “Static Web App” ကို ရှာပါ။  
- “Create” ကိုနှိပ်ပါ။

3. Static Web App ကို Configure လုပ်ပါ  
- #### Basics:  
  - Subscription: သင့် Azure subscription ကိုရွေးပါ။  
  - Resource Group: အသစ်တစ်ခုဖန်တီးပါ၊ သို့မဟုတ် ရှိပြီးသားတစ်ခုကို အသုံးပြုပါ။  
  - Name: သင့် Static Web App အတွက် နာမည်တစ်ခုပေးပါ။  
  - Region: သင့်အသုံးပြုသူများနဲ့အနီးဆုံးဒေသကိုရွေးပါ။  

- #### Deployment Details:  
  - Source: “GitHub” ကိုရွေးပါ။  
  - GitHub Account: Azure ကို သင့် GitHub Account ကို အသုံးပြုခွင့်ပေးပါ။  
  - Organization: သင့် GitHub Organization ကိုရွေးပါ။  
  - Repository: သင့် Static Web App ကိုပါဝင်တဲ့ Repository ကိုရွေးပါ။  
  - Branch: Deploy လုပ်ချင်တဲ့ Branch ကိုရွေးပါ။  

- #### Build Details:  
  - Build Presets: သင့် App ဖွဲ့စည်းထားတဲ့ Framework ကိုရွေးပါ (ဥပမာ - React, Angular, Vue, စသည်တို့)။  
  - App Location: သင့် App Code ရှိတဲ့ ဖိုလ်ဒါကို သတ်မှတ်ပါ (ဥပမာ - / သို့မဟုတ် root မှာရှိရင် /)။  
  - API Location: API ရှိရင်၊ API ရဲ့ တည်နေရာကို သတ်မှတ်ပါ (optional)။  
  - Output Location: Build Output ဖိုင်တွေ ထွက်ရှိမယ့် ဖိုလ်ဒါကို သတ်မှတ်ပါ (ဥပမာ - build သို့မဟုတ် dist)။  

4. Review နှင့် Create  
သင့်အချက်အလက်များကို ပြန်လည်စစ်ဆေးပြီး “Create” ကိုနှိပ်ပါ။ Azure က လိုအပ်တဲ့ အရင်းအမြစ်တွေကို ဖန်တီးပြီး GitHub Actions Workflow တစ်ခုကို သင့် Repository ထဲမှာ ဖန်တီးပါမယ်။

5. GitHub Actions Workflow  
Azure က GitHub Actions Workflow ဖိုင်တစ်ခုကို သင့် Repository ထဲမှာ အလိုအလျောက် ဖန်တီးပါမယ် (.github/workflows/azure-static-web-apps-<name>.yml)။ ဒီ Workflow က Build နှင့် Deployment လုပ်ငန်းစဉ်ကို စီမံဆောင်ရွက်ပါမယ်။

6. Deployment ကို စောင့်ကြည့်ပါ  
GitHub Repository ရဲ့ “Actions” Tab သို့ သွားပါ။  
Workflow တစ်ခု လုပ်ဆောင်နေတယ်ဆိုတာ တွေ့ရပါမယ်။ ဒီ Workflow က သင့် Static Web App ကို Azure သို့ Build နှင့် Deploy လုပ်ပါမယ်။  
Workflow ပြီးဆုံးသွားတဲ့အခါ၊ သင့် App ကို Azure URL မှာ Live ဖြစ်နေပါမယ်။

### ဥပမာ Workflow ဖိုင်

GitHub Actions Workflow ဖိုင်က ဒီလိုပုံစံရှိနိုင်ပါတယ် -  
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

### ထပ်မံသိရှိရန် အရင်းအမြစ်များ  
- [Azure Static Web Apps Documentation](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions Documentation](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

---

**ဝက်ဘ်ဆိုက်မှတ်ချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်ကြောင်း သတိပြုပါ။ မူလဘာသာဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတည်သော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားများ သို့မဟုတ် အဓိပ္ပာယ်မှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။