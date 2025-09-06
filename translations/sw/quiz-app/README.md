<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-26T16:17:50+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "sw"
}
-->
# Maswali ya Quiz

Maswali haya ya quiz ni ya kabla na baada ya mihadhara katika mtaala wa sayansi ya data kwenye https://aka.ms/datascience-beginners

## Kuongeza seti ya quiz iliyotafsiriwa

Ongeza tafsiri ya quiz kwa kuunda miundo inayolingana ya quiz katika folda za `assets/translations`. Quiz za msingi ziko kwenye `assets/translations/en`. Quiz zimegawanywa katika makundi kadhaa. Hakikisha unalinganisha namba na sehemu sahihi ya quiz. Kuna jumla ya quiz 40 katika mtaala huu, na hesabu inaanza na 0.

Baada ya kuhariri tafsiri, hariri faili ya `index.js` katika folda ya tafsiri ili kuingiza faili zote kufuatia kanuni za `en`.

Hariri faili ya `index.js` katika `assets/translations` ili kuingiza faili mpya zilizotafsiriwa.

Kisha, hariri menyu kunjuzi katika `App.vue` kwenye programu hii ili kuongeza lugha yako. Linganisha kifupi cha lugha na jina la folda ya lugha yako.

Hatimaye, hariri viungo vyote vya quiz katika masomo yaliyotafsiriwa, ikiwa vipo, ili kujumuisha utafsiri huu kama parameter ya swali: `?loc=fr` kwa mfano.

## Usanidi wa Mradi

```
npm install
```

### Inakompilesha na kupakia upya kwa maendeleo

```
npm run serve
```

### Inakompilesha na kupunguza kwa uzalishaji

```
npm run build
```

### Inakagua na kurekebisha faili

```
npm run lint
```

### Kubadilisha usanidi

Tazama [Marejeleo ya Usanidi](https://cli.vuejs.org/config/).

Shukrani: Asante kwa toleo la awali la programu hii ya quiz: https://github.com/arpan45/simple-quiz-vue

## Kuweka kwenye Azure

Hapa kuna mwongozo wa hatua kwa hatua wa kukusaidia kuanza:

1. Nakili Hifadhi ya GitHub
Hakikisha msimbo wa programu yako ya wavuti ya tuli uko kwenye hifadhi yako ya GitHub. Nakili hifadhi hii.

2. Unda Azure Static Web App
- Unda [akaunti ya Azure](http://azure.microsoft.com)
- Nenda kwenye [Azure portal](https://portal.azure.com) 
- Bonyeza “Create a resource” na tafuta “Static Web App”.
- Bonyeza “Create”.

3. Sanidi Static Web App
- Msingi: Subscription: Chagua usajili wako wa Azure.
- Resource Group: Unda kikundi kipya cha rasilimali au tumia kilichopo.
- Name: Toa jina kwa programu yako ya wavuti ya tuli.
- Region: Chagua eneo lililo karibu zaidi na watumiaji wako.

- #### Maelezo ya Uwekaji:
- Source: Chagua “GitHub”.
- GitHub Account: Ruhusu Azure kufikia akaunti yako ya GitHub.
- Organization: Chagua shirika lako la GitHub.
- Repository: Chagua hifadhi inayojumuisha programu yako ya wavuti ya tuli.
- Branch: Chagua tawi unalotaka kuweka kutoka.

- #### Maelezo ya Ujenzi:
- Build Presets: Chagua mfumo ambao programu yako imejengwa (mfano, React, Angular, Vue, n.k.).
- App Location: Eleza folda inayojumuisha msimbo wa programu yako (mfano, / ikiwa iko kwenye mzizi).
- API Location: Ikiwa una API, eleza eneo lake (hiari).
- Output Location: Eleza folda ambapo matokeo ya ujenzi yanazalishwa (mfano, build au dist).

4. Kagua na Unda
Kagua mipangilio yako na bonyeza “Create”. Azure itaweka rasilimali zinazohitajika na kuunda faili ya GitHub Actions workflow kwenye hifadhi yako.

5. GitHub Actions Workflow
Azure itaunda faili ya GitHub Actions workflow kiotomatiki kwenye hifadhi yako (.github/workflows/azure-static-web-apps-<name>.yml). Workflow hii itashughulikia mchakato wa ujenzi na uwekaji.

6. Fuatilia Uwekaji
Nenda kwenye kichupo cha “Actions” katika hifadhi yako ya GitHub.
Unapaswa kuona workflow ikifanya kazi. Workflow hii itajenga na kuweka programu yako ya wavuti ya tuli kwenye Azure.
Mara workflow itakapokamilika, programu yako itakuwa hai kwenye URL iliyotolewa na Azure.

### Mfano wa Faili ya Workflow

Hapa kuna mfano wa jinsi faili ya GitHub Actions workflow inaweza kuonekana:
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

### Rasilimali za Ziada
- [Nyaraka za Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [Nyaraka za GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa maelewano mabaya au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.