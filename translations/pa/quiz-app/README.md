<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-27T17:55:03+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "pa"
}
-->
# ਕਵਿਜ਼

ਇਹ ਕਵਿਜ਼ ਡਾਟਾ ਸਾਇੰਸ ਕਰੀਕੁਲਮ ਲਈ ਲੈਕਚਰ ਤੋਂ ਪਹਿਲਾਂ ਅਤੇ ਬਾਅਦ ਦੇ ਕਵਿਜ਼ ਹਨ ਜੋ https://aka.ms/datascience-beginners 'ਤੇ ਉਪਲਬਧ ਹਨ।  
## ਅਨੁਵਾਦਿਤ ਕਵਿਜ਼ ਸੈੱਟ ਸ਼ਾਮਲ ਕਰਨਾ

ਕਵਿਜ਼ ਦਾ ਅਨੁਵਾਦ ਸ਼ਾਮਲ ਕਰਨ ਲਈ `assets/translations` ਫੋਲਡਰ ਵਿੱਚ ਮਿਲਦੇ ਜੁਲਦੇ ਕਵਿਜ਼ ਸਟ੍ਰਕਚਰ ਬਣਾਓ। ਮੂਲ ਕਵਿਜ਼ `assets/translations/en` ਵਿੱਚ ਹਨ। ਕਵਿਜ਼ ਕਈ ਸਮੂਹਾਂ ਵਿੱਚ ਵੰਡੇ ਹੋਏ ਹਨ। ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਹੀ ਕਵਿਜ਼ ਸੈਕਸ਼ਨ ਨਾਲ ਗਿਣਤੀ ਨੂੰ ਸਿੰਕ ਕਰੋ। ਇਸ ਕਰੀਕੁਲਮ ਵਿੱਚ ਕੁੱਲ 40 ਕਵਿਜ਼ ਹਨ, ਅਤੇ ਗਿਣਤੀ 0 ਤੋਂ ਸ਼ੁਰੂ ਹੁੰਦੀ ਹੈ।

ਅਨੁਵਾਦਾਂ ਨੂੰ ਸੰਪਾਦਿਤ ਕਰਨ ਤੋਂ ਬਾਅਦ, translation ਫੋਲਡਰ ਵਿੱਚ `index.js` ਫਾਇਲ ਨੂੰ ਸੰਪਾਦਿਤ ਕਰੋ ਤਾਂ ਜੋ ਸਾਰੇ ਫਾਇਲਾਂ ਨੂੰ `en` ਵਿੱਚ ਦਿੱਤੇ ਗਏ ਰੀਤ-ਰਿਵਾਜਾਂ ਦੇ ਅਨੁਸਾਰ ਇੰਪੋਰਟ ਕੀਤਾ ਜਾ ਸਕੇ।

`assets/translations` ਵਿੱਚ `index.js` ਫਾਇਲ ਨੂੰ ਸੰਪਾਦਿਤ ਕਰੋ ਤਾਂ ਜੋ ਨਵੇਂ ਅਨੁਵਾਦਿਤ ਫਾਇਲਾਂ ਨੂੰ ਇੰਪੋਰਟ ਕੀਤਾ ਜਾ ਸਕੇ।

ਫਿਰ, ਇਸ ਐਪ ਵਿੱਚ `App.vue` ਵਿੱਚ ਡ੍ਰਾਪਡਾਊਨ ਨੂੰ ਸੰਪਾਦਿਤ ਕਰੋ ਤਾਂ ਜੋ ਤੁਹਾਡੀ ਭਾਸ਼ਾ ਸ਼ਾਮਲ ਕੀਤੀ ਜਾ ਸਕੇ। ਅਨੁਵਾਦਿਤ ਸੰਖੇਪ ਰੂਪ ਨੂੰ ਤੁਹਾਡੀ ਭਾਸ਼ਾ ਦੇ ਫੋਲਡਰ ਨਾਮ ਨਾਲ ਮਿਲਾਓ।

ਅੰਤ ਵਿੱਚ, ਅਨੁਵਾਦਿਤ ਪਾਠਾਂ ਵਿੱਚ ਸਾਰੇ ਕਵਿਜ਼ ਲਿੰਕਾਂ ਨੂੰ ਸੰਪਾਦਿਤ ਕਰੋ, ਜੇ ਉਹ ਮੌਜੂਦ ਹਨ, ਤਾਂ ਜੋ ਇਸ ਅਨੁਵਾਦ ਨੂੰ ਇੱਕ ਕਵੈਰੀ ਪੈਰਾਮੀਟਰ ਦੇ ਰੂਪ ਵਿੱਚ ਸ਼ਾਮਲ ਕੀਤਾ ਜਾ ਸਕੇ: `?loc=fr` ਉਦਾਹਰਨ ਲਈ।  

## ਪ੍ਰੋਜੈਕਟ ਸੈਟਅੱਪ

```
npm install
```

### ਵਿਕਾਸ ਲਈ ਕੰਪਾਇਲ ਅਤੇ ਹੌਟ-ਰੀਲੋਡ

```
npm run serve
```

### ਪ੍ਰੋਡਕਸ਼ਨ ਲਈ ਕੰਪਾਇਲ ਅਤੇ ਮਿਨੀਫਾਈ

```
npm run build
```

### ਫਾਇਲਾਂ ਨੂੰ ਲਿੰਟ ਅਤੇ ਫਿਕਸ ਕਰਦਾ ਹੈ

```
npm run lint
```

### ਕਨਫਿਗਰੇਸ਼ਨ ਨੂੰ ਕਸਟਮਾਈਜ਼ ਕਰੋ

[Configuration Reference](https://cli.vuejs.org/config/) ਵੇਖੋ।

ਸ਼੍ਰੇਯ: ਇਸ ਕਵਿਜ਼ ਐਪ ਦੇ ਮੂਲ ਸੰਸਕਰਣ ਲਈ ਧੰਨਵਾਦ: https://github.com/arpan45/simple-quiz-vue  

## Azure 'ਤੇ ਡਿਪਲੌਇ ਕਰਨਾ

ਇੱਥੇ ਇੱਕ ਕਦਮ-ਦਰ-ਕਦਮ ਗਾਈਡ ਹੈ ਜੋ ਤੁਹਾਨੂੰ ਸ਼ੁਰੂਆਤ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰੇਗੀ:

1. GitHub ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਫੋਰਕ ਕਰੋ  
ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡਾ ਸਟੈਟਿਕ ਵੈੱਬ ਐਪ ਕੋਡ ਤੁਹਾਡੇ GitHub ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ ਹੈ। ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਫੋਰਕ ਕਰੋ।

2. ਇੱਕ Azure ਸਟੈਟਿਕ ਵੈੱਬ ਐਪ ਬਣਾਓ  
- ਇੱਕ [Azure ਖਾਤਾ](http://azure.microsoft.com) ਬਣਾਓ  
- [Azure ਪੋਰਟਲ](https://portal.azure.com) 'ਤੇ ਜਾਓ  
- “Create a resource” 'ਤੇ ਕਲਿਕ ਕਰੋ ਅਤੇ “Static Web App” ਦੀ ਖੋਜ ਕਰੋ।  
- “Create” 'ਤੇ ਕਲਿਕ ਕਰੋ।  

3. ਸਟੈਟਿਕ ਵੈੱਬ ਐਪ ਨੂੰ ਕਨਫਿਗਰ ਕਰੋ  
- ਬੇਸਿਕਸ:  
  - Subscription: ਆਪਣੀ Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਚੁਣੋ।  
  - Resource Group: ਇੱਕ ਨਵਾਂ ਰਿਸੋਰਸ ਗਰੁੱਪ ਬਣਾਓ ਜਾਂ ਮੌਜੂਦਾ ਵਰਤੋ।  
  - Name: ਆਪਣੇ ਸਟੈਟਿਕ ਵੈੱਬ ਐਪ ਲਈ ਇੱਕ ਨਾਮ ਦਿਓ।  
  - Region: ਆਪਣੇ ਯੂਜ਼ਰਾਂ ਦੇ ਸਭ ਤੋਂ ਨੇੜੇ ਖੇਤਰ ਦੀ ਚੋਣ ਕਰੋ।  

- #### ਡਿਪਲੌਇਮੈਂਟ ਵੇਰਵੇ:  
  - Source: “GitHub” ਚੁਣੋ।  
  - GitHub Account: Azure ਨੂੰ ਤੁਹਾਡੇ GitHub ਖਾਤੇ ਤੱਕ ਪਹੁੰਚ ਦੀ ਅਨੁਮਤੀ ਦਿਓ।  
  - Organization: ਆਪਣੀ GitHub ਸੰਸਥਾ ਚੁਣੋ।  
  - Repository: ਉਹ ਰਿਪੋਜ਼ਟਰੀ ਚੁਣੋ ਜਿਸ ਵਿੱਚ ਤੁਹਾਡਾ ਸਟੈਟਿਕ ਵੈੱਬ ਐਪ ਹੈ।  
  - Branch: ਉਹ ਬ੍ਰਾਂਚ ਚੁਣੋ ਜਿਸ ਤੋਂ ਤੁਸੀਂ ਡਿਪਲੌਇ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ।  

- #### ਬਿਲਡ ਵੇਰਵੇ:  
  - Build Presets: ਉਹ ਫਰੇਮਵਰਕ ਚੁਣੋ ਜਿਸ ਨਾਲ ਤੁਹਾਡਾ ਐਪ ਬਣਾਇਆ ਗਿਆ ਹੈ (ਜਿਵੇਂ React, Angular, Vue, ਆਦਿ)।  
  - App Location: ਉਹ ਫੋਲਡਰ ਦਰਸਾਓ ਜਿਸ ਵਿੱਚ ਤੁਹਾਡਾ ਐਪ ਕੋਡ ਹੈ (ਜਿਵੇਂ / ਜੇਕਰ ਇਹ ਰੂਟ ਵਿੱਚ ਹੈ)।  
  - API Location: ਜੇ ਤੁਹਾਡੇ ਕੋਲ API ਹੈ, ਤਾਂ ਇਸ ਦਾ ਸਥਾਨ ਦਰਸਾਓ (ਵਿਕਲਪਿਕ)।  
  - Output Location: ਉਹ ਫੋਲਡਰ ਦਰਸਾਓ ਜਿੱਥੇ ਬਿਲਡ ਆਉਟਪੁੱਟ ਤਿਆਰ ਹੁੰਦੀ ਹੈ (ਜਿਵੇਂ build ਜਾਂ dist)।  

4. ਸਮੀਖਿਆ ਕਰੋ ਅਤੇ ਬਣਾਓ  
ਆਪਣੀਆਂ ਸੈਟਿੰਗਾਂ ਦੀ ਸਮੀਖਿਆ ਕਰੋ ਅਤੇ “Create” 'ਤੇ ਕਲਿਕ ਕਰੋ। Azure ਜ਼ਰੂਰੀ ਰਿਸੋਰਸ ਸੈਟਅੱਪ ਕਰੇਗਾ ਅਤੇ ਤੁਹਾਡੇ ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ ਇੱਕ GitHub Actions ਵਰਕਫਲੋ ਬਣਾਏਗਾ।  

5. GitHub Actions ਵਰਕਫਲੋ  
Azure ਤੁਹਾਡੇ ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਇੱਕ GitHub Actions ਵਰਕਫਲੋ ਫਾਇਲ ਬਣਾਏਗਾ (.github/workflows/azure-static-web-apps-<name>.yml)। ਇਹ ਵਰਕਫਲੋ ਬਿਲਡ ਅਤੇ ਡਿਪਲੌਇਮੈਂਟ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਸੰਭਾਲੇਗਾ।  

6. ਡਿਪਲੌਇਮੈਂਟ ਦੀ ਨਿਗਰਾਨੀ ਕਰੋ  
ਤੁਹਾਡੇ GitHub ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ “Actions” ਟੈਬ 'ਤੇ ਜਾਓ।  
ਤੁਹਾਨੂੰ ਇੱਕ ਵਰਕਫਲੋ ਚੱਲਦਾ ਹੋਇਆ ਦਿਖਾਈ ਦੇਣਾ ਚਾਹੀਦਾ ਹੈ। ਇਹ ਵਰਕਫਲੋ ਤੁਹਾਡੇ ਸਟੈਟਿਕ ਵੈੱਬ ਐਪ ਨੂੰ Azure 'ਤੇ ਬਿਲਡ ਅਤੇ ਡਿਪਲੌਇ ਕਰੇਗਾ।  
ਜਦੋਂ ਵਰਕਫਲੋ ਪੂਰਾ ਹੋ ਜਾਵੇ, ਤੁਹਾਡਾ ਐਪ ਦਿੱਤੇ ਗਏ Azure URL 'ਤੇ ਲਾਈਵ ਹੋਵੇਗਾ।  

### ਉਦਾਹਰਨ ਵਰਕਫਲੋ ਫਾਇਲ

ਇੱਥੇ GitHub Actions ਵਰਕਫਲੋ ਫਾਇਲ ਦਾ ਇੱਕ ਉਦਾਹਰਨ ਦਿੱਤਾ ਗਿਆ ਹੈ:  
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

### ਵਾਧੂ ਸਰੋਤ  
- [Azure Static Web Apps Documentation](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions Documentation](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

---

**ਅਸਵੀਕਾਰਨਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਣੀਕਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼, ਜੋ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੈ, ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।