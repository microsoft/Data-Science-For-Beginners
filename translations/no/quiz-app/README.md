<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-26T22:19:44+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "no"
}
-->
# Quizer

Disse quizene er forhånds- og etterforelesningsquizer for data science-læreplanen på https://aka.ms/datascience-beginners

## Legge til et oversatt quizsett

Legg til en quizoversettelse ved å lage tilsvarende quizstrukturer i `assets/translations`-mappene. De originale quizene finnes i `assets/translations/en`. Quizene er delt inn i flere grupperinger. Sørg for å justere nummereringen med riktig quizseksjon. Det er totalt 40 quizer i denne læreplanen, med nummereringen som starter på 0.

Etter at du har redigert oversettelsene, rediger `index.js`-filen i oversettelsesmappen for å importere alle filene i henhold til konvensjonene i `en`.

Rediger `index.js`-filen i `assets/translations` for å importere de nye oversatte filene.

Deretter redigerer du nedtrekksmenyen i `App.vue` i denne appen for å legge til språket ditt. Match den lokaliserte forkortelsen med mappenavnet for språket ditt.

Til slutt, rediger alle quizlenkene i de oversatte leksjonene, hvis de finnes, for å inkludere denne lokaliseringen som en spørringsparameter: `?loc=fr` for eksempel.

## Prosjektoppsett

```
npm install
```

### Kompilerer og oppdaterer for utvikling

```
npm run serve
```

### Kompilerer og minimerer for produksjon

```
npm run build
```

### Linter og fikser filer

```
npm run lint
```

### Tilpass konfigurasjon

Se [Konfigurasjonsreferanse](https://cli.vuejs.org/config/).

Kreditering: Takk til den originale versjonen av denne quiz-appen: https://github.com/arpan45/simple-quiz-vue

## Distribuere til Azure

Her er en steg-for-steg guide for å komme i gang:

1. Fork en GitHub-repositorium  
Sørg for at koden til din statiske webapp ligger i din GitHub-repositorium. Fork denne repositoriumen.

2. Opprett en Azure Static Web App  
- Opprett en [Azure-konto](http://azure.microsoft.com)  
- Gå til [Azure-portalen](https://portal.azure.com)  
- Klikk på "Create a resource" og søk etter "Static Web App".  
- Klikk "Create".  

3. Konfigurer den statiske webappen  
- Grunnleggende:  
  - Abonnement: Velg ditt Azure-abonnement.  
  - Ressursgruppe: Opprett en ny ressursgruppe eller bruk en eksisterende.  
  - Navn: Gi et navn til din statiske webapp.  
  - Region: Velg regionen nærmest brukerne dine.  

- #### Distribusjonsdetaljer:  
  - Kilde: Velg "GitHub".  
  - GitHub-konto: Autoriser Azure til å få tilgang til din GitHub-konto.  
  - Organisasjon: Velg din GitHub-organisasjon.  
  - Repositorium: Velg repositoriet som inneholder din statiske webapp.  
  - Gren: Velg grenen du vil distribuere fra.  

- #### Byggdetaljer:  
  - Byggeforhåndsinnstillinger: Velg rammeverket appen din er bygget med (f.eks. React, Angular, Vue, osv.).  
  - App-plassering: Angi mappen som inneholder appkoden din (f.eks. / hvis den er i roten).  
  - API-plassering: Hvis du har en API, angi dens plassering (valgfritt).  
  - Utdata-plassering: Angi mappen der byggeutdataene genereres (f.eks. build eller dist).  

4. Gjennomgå og opprett  
Gjennomgå innstillingene dine og klikk "Create". Azure vil sette opp de nødvendige ressursene og opprette en GitHub Actions-arbeidsflyt i repositoriet ditt.

5. GitHub Actions-arbeidsflyt  
Azure vil automatisk opprette en GitHub Actions-arbeidsflytfil i repositoriet ditt (.github/workflows/azure-static-web-apps-<name>.yml). Denne arbeidsflyten vil håndtere bygge- og distribusjonsprosessen.

6. Overvåk distribusjonen  
Gå til "Actions"-fanen i ditt GitHub-repositorium.  
Du bør se en arbeidsflyt som kjører. Denne arbeidsflyten vil bygge og distribuere din statiske webapp til Azure.  
Når arbeidsflyten er fullført, vil appen din være live på den oppgitte Azure-URL-en.

### Eksempel på arbeidsflytfil

Her er et eksempel på hvordan GitHub Actions-arbeidsflytfilen kan se ut:  
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

### Ekstra ressurser  
- [Azure Static Web Apps Dokumentasjon](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions Dokumentasjon](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.