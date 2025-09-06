<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e92c33ea498915a13c9aec162616db18",
  "translation_date": "2025-08-28T11:29:57+00:00",
  "source_file": "quiz-app/README.md",
  "language_code": "it"
}
-->
# Quiz

Questi quiz sono i quiz pre- e post-lezione per il curriculum di data science disponibile su https://aka.ms/datascience-beginners

## Aggiungere un set di quiz tradotto

Aggiungi una traduzione dei quiz creando strutture di quiz corrispondenti nelle cartelle `assets/translations`. I quiz canonici si trovano in `assets/translations/en`. I quiz sono suddivisi in diversi gruppi. Assicurati di allineare la numerazione con la sezione corretta del quiz. In totale, ci sono 40 quiz in questo curriculum, con il conteggio che inizia da 0.

Dopo aver modificato le traduzioni, modifica il file index.js nella cartella delle traduzioni per importare tutti i file seguendo le convenzioni di `en`.

Modifica il file `index.js` in `assets/translations` per importare i nuovi file tradotti.

Successivamente, modifica il menu a tendina in `App.vue` in questa app per aggiungere la tua lingua. Abbina l'abbreviazione localizzata al nome della cartella per la tua lingua.

Infine, modifica tutti i link ai quiz nelle lezioni tradotte, se esistono, per includere questa localizzazione come parametro di query: `?loc=fr`, ad esempio.

## Configurazione del progetto

```
npm install
```

### Compilazione e aggiornamento automatico per lo sviluppo

```
npm run serve
```

### Compilazione e minimizzazione per la produzione

```
npm run build
```

### Analisi e correzione dei file

```
npm run lint
```

### Personalizzare la configurazione

Consulta [Configuration Reference](https://cli.vuejs.org/config/).

Crediti: Grazie alla versione originale di questa app per quiz: https://github.com/arpan45/simple-quiz-vue

## Distribuzione su Azure

Ecco una guida passo-passo per aiutarti a iniziare:

1. Fork del repository GitHub  
Assicurati che il codice della tua app web statica sia nel tuo repository GitHub. Fai un fork di questo repository.

2. Creare un'app web statica su Azure  
- Crea un [account Azure](http://azure.microsoft.com)  
- Vai al [portale di Azure](https://portal.azure.com)  
- Clicca su “Crea una risorsa” e cerca “App Web Statica”.  
- Clicca su “Crea”.

3. Configurare l'app web statica  
- **Informazioni di base**:  
  - **Sottoscrizione**: Seleziona la tua sottoscrizione Azure.  
  - **Gruppo di risorse**: Crea un nuovo gruppo di risorse o utilizza uno esistente.  
  - **Nome**: Fornisci un nome per la tua app web statica.  
  - **Regione**: Scegli la regione più vicina ai tuoi utenti.  

- **Dettagli di distribuzione**:  
  - **Origine**: Seleziona “GitHub”.  
  - **Account GitHub**: Autorizza Azure ad accedere al tuo account GitHub.  
  - **Organizzazione**: Seleziona la tua organizzazione GitHub.  
  - **Repository**: Scegli il repository contenente la tua app web statica.  
  - **Branch**: Seleziona il branch da cui vuoi distribuire.  

- **Dettagli di build**:  
  - **Preset di build**: Scegli il framework con cui è costruita la tua app (ad esempio, React, Angular, Vue, ecc.).  
  - **Posizione dell'app**: Specifica la cartella contenente il codice della tua app (ad esempio, / se si trova nella radice).  
  - **Posizione API**: Se hai un'API, specifica la sua posizione (opzionale).  
  - **Posizione output**: Specifica la cartella in cui viene generato l'output della build (ad esempio, build o dist).  

4. Revisione e creazione  
Rivedi le impostazioni e clicca su “Crea”. Azure configurerà le risorse necessarie e creerà un workflow GitHub Actions nel tuo repository.

5. Workflow GitHub Actions  
Azure creerà automaticamente un file workflow GitHub Actions nel tuo repository (.github/workflows/azure-static-web-apps-<name>.yml). Questo workflow gestirà il processo di build e distribuzione.

6. Monitorare la distribuzione  
Vai alla scheda “Actions” nel tuo repository GitHub.  
Dovresti vedere un workflow in esecuzione. Questo workflow costruirà e distribuirà la tua app web statica su Azure.  
Una volta completato il workflow, la tua app sarà online all'URL fornito da Azure.

### Esempio di file workflow

Ecco un esempio di come potrebbe apparire il file workflow GitHub Actions:  
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

### Risorse aggiuntive  
- [Documentazione Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [Documentazione GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.