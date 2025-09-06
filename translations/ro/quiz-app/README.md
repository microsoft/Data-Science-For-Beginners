<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-26T16:19:53+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "ro"
}
-->
# Chestionare

Aceste chestionare sunt chestionarele de dinaintea și de după lecții pentru curriculumul de știința datelor de la https://aka.ms/datascience-beginners

## Adăugarea unui set de chestionare traduse

Adaugă o traducere a unui chestionar creând structuri de chestionare corespunzătoare în folderele `assets/translations`. Chestionarele canonice se află în `assets/translations/en`. Chestionarele sunt împărțite în mai multe grupuri. Asigură-te că numerotarea este aliniată cu secțiunea corectă a chestionarului. În acest curriculum sunt în total 40 de chestionare, numerotarea începând de la 0.

După ce editezi traducerile, editează fișierul `index.js` din folderul de traduceri pentru a importa toate fișierele, urmând convențiile din `en`.

Editează fișierul `index.js` din `assets/translations` pentru a importa noile fișiere traduse.

Apoi, editează meniul dropdown din `App.vue` din această aplicație pentru a adăuga limba ta. Potrivește abrevierea localizată cu numele folderului pentru limba ta.

În cele din urmă, editează toate linkurile chestionarelor din lecțiile traduse, dacă există, pentru a include această localizare ca parametru de interogare: `?loc=fr`, de exemplu.

## Configurarea proiectului

```
npm install
```

### Compilează și reîncarcă automat pentru dezvoltare

```
npm run serve
```

### Compilează și minimizează pentru producție

```
npm run build
```

### Verifică și repară fișierele

```
npm run lint
```

### Personalizează configurația

Vezi [Referința de Configurare](https://cli.vuejs.org/config/).

Credite: Mulțumiri versiunii originale a acestei aplicații de chestionare: https://github.com/arpan45/simple-quiz-vue

## Publicarea pe Azure

Iată un ghid pas cu pas pentru a te ajuta să începi:

1. Clonează un Repository GitHub  
Asigură-te că codul aplicației tale web statice se află în repository-ul tău GitHub. Clonează acest repository.

2. Creează o aplicație web statică pe Azure  
- Creează un [cont Azure](http://azure.microsoft.com)  
- Accesează [portalul Azure](https://portal.azure.com)  
- Dă clic pe „Create a resource” și caută „Static Web App”.  
- Dă clic pe „Create”.  

3. Configurează aplicația web statică  
- **Bazele**:  
  - Subscription: Selectează abonamentul tău Azure.  
  - Resource Group: Creează un nou grup de resurse sau folosește unul existent.  
  - Name: Oferă un nume aplicației tale web statice.  
  - Region: Alege regiunea cea mai apropiată de utilizatorii tăi.  

- **Detalii despre implementare**:  
  - Source: Selectează „GitHub”.  
  - GitHub Account: Autorizează Azure să acceseze contul tău GitHub.  
  - Organization: Selectează organizația ta GitHub.  
  - Repository: Alege repository-ul care conține aplicația ta web statică.  
  - Branch: Selectează ramura din care vrei să implementezi.  

- **Detalii despre build**:  
  - Build Presets: Alege framework-ul cu care este construită aplicația ta (de exemplu, React, Angular, Vue etc.).  
  - App Location: Specifică folderul care conține codul aplicației tale (de exemplu, / dacă este în rădăcină).  
  - API Location: Dacă ai un API, specifică locația acestuia (opțional).  
  - Output Location: Specifică folderul unde este generat output-ul build-ului (de exemplu, build sau dist).  

4. Revizuiește și creează  
Revizuiește setările și dă clic pe „Create”. Azure va configura resursele necesare și va crea un workflow GitHub Actions în repository-ul tău.  

5. Workflow GitHub Actions  
Azure va crea automat un fișier workflow GitHub Actions în repository-ul tău (.github/workflows/azure-static-web-apps-<name>.yml). Acest workflow va gestiona procesul de build și implementare.  

6. Monitorizează implementarea  
Accesează tab-ul „Actions” din repository-ul tău GitHub.  
Ar trebui să vezi un workflow în desfășurare. Acest workflow va construi și implementa aplicația ta web statică pe Azure.  
După ce workflow-ul se finalizează, aplicația ta va fi live pe URL-ul furnizat de Azure.  

### Exemplu de fișier Workflow

Iată un exemplu de cum ar putea arăta fișierul workflow GitHub Actions:  
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

### Resurse suplimentare  
- [Documentația Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [Documentația GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.