<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-28T15:57:48+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "nl"
}
-->
# Quizzen

Deze quizzen zijn de quizzen vóór en na de lessen in het data science-curriculum op https://aka.ms/datascience-beginners

## Een vertaalde quizset toevoegen

Voeg een vertaling van een quiz toe door bijpassende quizstructuren te maken in de map `assets/translations`. De originele quizzen staan in `assets/translations/en`. De quizzen zijn onderverdeeld in verschillende groepen. Zorg ervoor dat de nummering overeenkomt met de juiste quizsectie. In totaal zijn er 40 quizzen in dit curriculum, waarbij de telling begint bij 0.

Na het bewerken van de vertalingen, bewerk het bestand `index.js` in de vertaalmap om alle bestanden te importeren volgens de conventies in `en`.

Bewerk het bestand `index.js` in `assets/translations` om de nieuw vertaalde bestanden te importeren.

Bewerk vervolgens het dropdownmenu in `App.vue` in deze app om jouw taal toe te voegen. Zorg ervoor dat de lokale afkorting overeenkomt met de mapnaam van jouw taal.

Ten slotte, bewerk alle quizlinks in de vertaalde lessen, indien aanwezig, om deze lokalisatie toe te voegen als queryparameter: `?loc=fr` bijvoorbeeld.

## Projectinstellingen

```
npm install
```

### Compileert en herlaadt automatisch voor ontwikkeling

```
npm run serve
```

### Compileert en minimaliseert voor productie

```
npm run build
```

### Controleert en herstelt bestanden

```
npm run lint
```

### Configuratie aanpassen

Zie [Configuratiereferentie](https://cli.vuejs.org/config/).

Credits: Dank aan de originele versie van deze quiz-app: https://github.com/arpan45/simple-quiz-vue

## Deployen naar Azure

Hier is een stapsgewijze handleiding om je op weg te helpen:

1. Fork een GitHub-repository  
Zorg ervoor dat je statische webapp-code in je GitHub-repository staat. Fork deze repository.

2. Maak een Azure Static Web App  
- Maak een [Azure-account](http://azure.microsoft.com) aan.  
- Ga naar het [Azure-portaal](https://portal.azure.com).  
- Klik op "Create a resource" en zoek naar "Static Web App".  
- Klik op "Create".  

3. Configureer de Static Web App  
- **Basisinstellingen:**  
  - Abonnement: Selecteer je Azure-abonnement.  
  - Resourcegroep: Maak een nieuwe resourcegroep aan of gebruik een bestaande.  
  - Naam: Geef een naam op voor je statische webapp.  
  - Regio: Kies de regio die het dichtst bij je gebruikers ligt.  

- **Details voor implementatie:**  
  - Bron: Selecteer "GitHub".  
  - GitHub-account: Autoriseer Azure om toegang te krijgen tot je GitHub-account.  
  - Organisatie: Selecteer je GitHub-organisatie.  
  - Repository: Kies de repository die je statische webapp bevat.  
  - Branch: Selecteer de branch waarvan je wilt implementeren.  

- **Details voor build:**  
  - Build-presets: Kies het framework waarmee je app is gebouwd (bijv. React, Angular, Vue, etc.).  
  - App-locatie: Geef de map op die je app-code bevat (bijv. / als het in de root staat).  
  - API-locatie: Als je een API hebt, geef de locatie op (optioneel).  
  - Outputlocatie: Geef de map op waar de build-output wordt gegenereerd (bijv. build of dist).  

4. Controleer en maak aan  
Controleer je instellingen en klik op "Create". Azure zal de benodigde resources instellen en een GitHub Actions-workflow in je repository aanmaken.

5. GitHub Actions-workflow  
Azure maakt automatisch een GitHub Actions-workflowbestand aan in je repository (.github/workflows/azure-static-web-apps-<naam>.yml). Deze workflow zal het build- en implementatieproces afhandelen.

6. Monitor de implementatie  
Ga naar het tabblad "Actions" in je GitHub-repository.  
Je zou een workflow moeten zien draaien. Deze workflow zal je statische webapp bouwen en implementeren naar Azure.  
Zodra de workflow voltooid is, is je app live op de opgegeven Azure-URL.

### Voorbeeld van een workflowbestand

Hier is een voorbeeld van hoe het GitHub Actions-workflowbestand eruit zou kunnen zien:  
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

### Aanvullende bronnen
- [Azure Static Web Apps Documentatie](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions Documentatie](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.