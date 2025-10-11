<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-10-11T15:16:34+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "et"
}
-->
# Viktoriinid

Need viktoriinid on andmeteaduse õppekava eel- ja järelloengute viktoriinid aadressil https://aka.ms/datascience-beginners

## Tõlgitud viktoriinikomplekti lisamine

Lisa viktoriini tõlge, luues vastavad viktoriinistruktuurid kaustadesse `assets/translations`. Originaalviktoriinid asuvad kaustas `assets/translations/en`. Viktoriinid on jagatud mitmeks grupiks. Veendu, et nummerdamine vastaks õigele viktoriini sektsioonile. Selles õppekavas on kokku 40 viktoriini, alustades numbrist 0.

Pärast tõlgete redigeerimist muuda tõlke kaustas `index.js` faili, et importida kõik failid vastavalt `en` konventsioonidele.

Muuda faili `index.js` kaustas `assets/translations`, et importida uued tõlgitud failid.

Seejärel muuda selle rakenduse failis `App.vue` rippmenüüd, et lisada oma keel. Sobita lokaliseeritud lühend oma keele kausta nimega.

Lõpuks muuda kõik tõlgitud õppetundides olevad viktoriinilingid, kui need eksisteerivad, et lisada lokaliseerimine päringuparameetrina: näiteks `?loc=fr`.

## Projekti seadistamine

```
npm install
```

### Kompileerib ja uuesti laadib arenduseks

```
npm run serve
```

### Kompileerib ja minimeerib tootmiseks

```
npm run build
```

### Kontrollib ja parandab faile

```
npm run lint
```

### Kohanda konfiguratsiooni

Vaata [Konfiguratsiooni viidet](https://cli.vuejs.org/config/).

Tunnustus: Tänud selle viktoriinirakenduse algversiooni eest: https://github.com/arpan45/simple-quiz-vue

## Azure'i juurutamine

Siin on samm-sammuline juhend, mis aitab sul alustada:

1. Forki GitHubi repositoorium
Veendu, et sinu staatilise veebirakenduse kood on sinu GitHubi repositooriumis. Forki see repositoorium.

2. Loo Azure'i staatiline veebirakendus
- Loo [Azure'i konto](http://azure.microsoft.com)
- Mine [Azure'i portaali](https://portal.azure.com) 
- Klõpsa “Loo ressurss” ja otsi “Static Web App”.
- Klõpsa “Loo”.

3. Konfigureeri staatiline veebirakendus
- Põhiandmed: Tellimus: Vali oma Azure'i tellimus.
- Ressursigrupp: Loo uus ressursigrupp või kasuta olemasolevat.
- Nimi: Anna oma staatilisele veebirakendusele nimi.
- Piirkond: Vali piirkond, mis on sinu kasutajatele kõige lähemal.

- #### Juurutamise üksikasjad:
- Allikas: Vali “GitHub”.
- GitHubi konto: Autoriseeri Azure, et pääseda sinu GitHubi kontole.
- Organisatsioon: Vali oma GitHubi organisatsioon.
- Repositoorium: Vali repositoorium, mis sisaldab sinu staatilist veebirakendust.
- Haru: Vali haru, millest soovid juurutada.

- #### Ehituse üksikasjad:
- Ehituse eelseadistused: Vali raamistik, millele sinu rakendus on ehitatud (nt React, Angular, Vue jne).
- Rakenduse asukoht: Määra kaust, mis sisaldab sinu rakenduse koodi (nt / kui see on juurkaustas).
- API asukoht: Kui sul on API, määra selle asukoht (valikuline).
- Väljundi asukoht: Määra kaust, kuhu ehituse väljund genereeritakse (nt build või dist).

4. Vaata üle ja loo
Vaata oma seaded üle ja klõpsa “Loo”. Azure seadistab vajalikud ressursid ja loob GitHub Actions töövoo sinu repositooriumis.

5. GitHub Actions töövoog
Azure loob automaatselt GitHub Actions töövoo faili sinu repositooriumis (.github/workflows/azure-static-web-apps-<nimi>.yml). See töövoog haldab ehituse ja juurutamise protsessi.

6. Jälgi juurutamist
Mine oma GitHubi repositooriumi vahekaardile “Actions”.
Sa peaksid nägema töövoogu, mis töötab. See töövoog ehitab ja juurutab sinu staatilise veebirakenduse Azure'i.
Kui töövoog on lõpule jõudnud, on sinu rakendus saadaval antud Azure'i URL-il.

### Näide töövoo failist

Siin on näide, milline GitHub Actions töövoo fail võib välja näha:
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

### Täiendavad ressursid
- [Azure'i staatiliste veebirakenduste dokumentatsioon](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [GitHub Actions dokumentatsioon](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.