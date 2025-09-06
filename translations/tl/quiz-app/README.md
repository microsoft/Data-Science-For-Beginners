<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-28T02:48:16+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "tl"
}
-->
# Mga Pagsusulit

Ang mga pagsusulit na ito ay ang pre- at post-lecture quizzes para sa kurikulum ng data science sa https://aka.ms/datascience-beginners

## Pagdaragdag ng Isinaling Set ng Pagsusulit

Magdagdag ng salin ng pagsusulit sa pamamagitan ng paggawa ng mga katugmang istruktura ng pagsusulit sa mga folder na `assets/translations`. Ang mga orihinal na pagsusulit ay nasa `assets/translations/en`. Ang mga pagsusulit ay hinati sa ilang mga grupo. Siguraduhing i-align ang pagnunumero sa tamang seksyon ng pagsusulit. May kabuuang 40 pagsusulit sa kurikulum na ito, na nagsisimula sa bilang na 0.

Pagkatapos i-edit ang mga salin, i-edit ang file na `index.js` sa folder ng salin upang i-import ang lahat ng mga file ayon sa mga convention sa `en`.

I-edit ang file na `index.js` sa `assets/translations` upang i-import ang mga bagong isinaling file.

Pagkatapos, i-edit ang dropdown sa `App.vue` sa app na ito upang idagdag ang iyong wika. Itugma ang lokal na abbreviation sa pangalan ng folder para sa iyong wika.

Sa wakas, i-edit ang lahat ng mga link ng pagsusulit sa mga isinaling aralin, kung mayroon, upang isama ang lokal na parameter bilang query: `?loc=fr` halimbawa.

## Setup ng Proyekto

```
npm install
```

### Nagko-compile at nagre-reload para sa development

```
npm run serve
```

### Nagko-compile at nagmi-minify para sa production

```
npm run build
```

### Nagli-lint at nag-aayos ng mga file

```
npm run lint
```

### I-customize ang configuration

Tingnan ang [Configuration Reference](https://cli.vuejs.org/config/).

Mga Kredito: Salamat sa orihinal na bersyon ng app na ito ng pagsusulit: https://github.com/arpan45/simple-quiz-vue

## Pag-deploy sa Azure

Narito ang isang step-by-step na gabay upang matulungan kang magsimula:

1. I-fork ang isang GitHub Repository  
Siguraduhing ang iyong static web app code ay nasa iyong GitHub repository. I-fork ang repository na ito.

2. Gumawa ng Azure Static Web App  
- Gumawa ng [Azure account](http://azure.microsoft.com)  
- Pumunta sa [Azure portal](https://portal.azure.com)  
- I-click ang “Create a resource” at hanapin ang “Static Web App”.  
- I-click ang “Create”.

3. I-configure ang Static Web App  
- **Basics**:  
  - Subscription: Piliin ang iyong Azure subscription.  
  - Resource Group: Gumawa ng bagong resource group o gumamit ng umiiral na.  
  - Name: Magbigay ng pangalan para sa iyong static web app.  
  - Region: Piliin ang rehiyon na pinakamalapit sa iyong mga user.  

- **Deployment Details**:  
  - Source: Piliin ang “GitHub”.  
  - GitHub Account: I-authorize ang Azure na ma-access ang iyong GitHub account.  
  - Organization: Piliin ang iyong GitHub organization.  
  - Repository: Piliin ang repository na naglalaman ng iyong static web app.  
  - Branch: Piliin ang branch na nais mong i-deploy.  

- **Build Details**:  
  - Build Presets: Piliin ang framework na ginamit sa paggawa ng iyong app (hal., React, Angular, Vue, atbp.).  
  - App Location: Tukuyin ang folder na naglalaman ng iyong app code (hal., / kung nasa root ito).  
  - API Location: Kung mayroon kang API, tukuyin ang lokasyon nito (opsyonal).  
  - Output Location: Tukuyin ang folder kung saan nabubuo ang build output (hal., build o dist).  

4. I-review at I-create  
I-review ang iyong mga setting at i-click ang “Create”. Ang Azure ay magse-set up ng mga kinakailangang resources at gagawa ng GitHub Actions workflow sa iyong repository.

5. GitHub Actions Workflow  
Ang Azure ay awtomatikong gagawa ng GitHub Actions workflow file sa iyong repository (.github/workflows/azure-static-web-apps-<name>.yml). Ang workflow na ito ang hahawak sa proseso ng build at deployment.

6. I-monitor ang Deployment  
Pumunta sa tab na “Actions” sa iyong GitHub repository.  
Makikita mo ang isang workflow na tumatakbo. Ang workflow na ito ang magbi-build at magde-deploy ng iyong static web app sa Azure.  
Kapag natapos ang workflow, magiging live na ang iyong app sa ibinigay na Azure URL.

### Halimbawa ng Workflow File

Narito ang halimbawa ng GitHub Actions workflow file:  
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

### Karagdagang Mga Mapagkukunan  
- [Azure Static Web Apps Documentation](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions Documentation](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.