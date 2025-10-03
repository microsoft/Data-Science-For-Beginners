<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:18:00+00:00",
  "source_file": "AGENTS.md",
  "language_code": "it"
}
-->
# AGENTS.md

## Panoramica del Progetto

Data Science for Beginners è un curriculum completo di 10 settimane e 20 lezioni creato dai Microsoft Azure Cloud Advocates. Il repository è una risorsa didattica che insegna i concetti fondamentali della data science attraverso lezioni basate su progetti, inclusi Jupyter notebook, quiz interattivi e compiti pratici.

**Tecnologie Chiave:**
- **Jupyter Notebooks**: Principale mezzo di apprendimento utilizzando Python 3
- **Librerie Python**: pandas, numpy, matplotlib per analisi e visualizzazione dei dati
- **Vue.js 2**: Applicazione per quiz (cartella quiz-app)
- **Docsify**: Generatore di siti di documentazione per accesso offline
- **Node.js/npm**: Gestione dei pacchetti per componenti JavaScript
- **Markdown**: Tutti i contenuti delle lezioni e la documentazione

**Architettura:**
- Repository educativo multilingue con ampie traduzioni
- Strutturato in moduli di lezione (1-Introduzione fino a 6-Data-Science-In-Wild)
- Ogni lezione include README, notebook, compiti e quiz
- Applicazione per quiz Vue.js autonoma per valutazioni pre/post lezione
- Supporto per GitHub Codespaces e contenitori di sviluppo VS Code

## Comandi di Configurazione

### Configurazione del Repository
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Configurazione dell'Ambiente Python
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Configurazione dell'Applicazione per Quiz
```bash
# Navigate to quiz app
cd quiz-app

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint and fix files
npm run lint
```

### Server di Documentazione Docsify
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Configurazione dei Progetti di Visualizzazione
Per progetti di visualizzazione come meaningful-visualizations (lezione 13):
```bash
# Navigate to starter or solution folder
cd 3-Data-Visualization/13-meaningful-visualizations/starter

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint files
npm run lint
```


## Flusso di Lavoro per lo Sviluppo

### Lavorare con i Jupyter Notebooks
1. Avvia Jupyter nella radice del repository: `jupyter notebook`
2. Naviga nella cartella della lezione desiderata
3. Apri i file `.ipynb` per lavorare sugli esercizi
4. I notebook sono autonomi con spiegazioni e celle di codice
5. La maggior parte dei notebook utilizza pandas, numpy e matplotlib - assicurati che siano installati

### Struttura delle Lezioni
Ogni lezione contiene tipicamente:
- `README.md` - Contenuto principale della lezione con teoria ed esempi
- `notebook.ipynb` - Esercizi pratici con Jupyter notebook
- `assignment.ipynb` o `assignment.md` - Compiti pratici
- Cartella `solution/` - Notebook e codice delle soluzioni
- Cartella `images/` - Materiali visivi di supporto

### Sviluppo dell'Applicazione per Quiz
- Applicazione Vue.js 2 con hot-reload durante lo sviluppo
- Quiz archiviati in `quiz-app/src/assets/translations/`
- Ogni lingua ha la propria cartella di traduzione (en, fr, es, ecc.)
- La numerazione dei quiz parte da 0 e arriva fino a 39 (40 quiz in totale)

### Aggiungere Traduzioni
- Le traduzioni vanno nella cartella `translations/` alla radice del repository
- Ogni lingua ha una struttura completa delle lezioni speculare a quella in inglese
- Traduzione automatizzata tramite GitHub Actions (co-op-translator.yml)

## Istruzioni per i Test

### Test dell'Applicazione per Quiz
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Test dei Notebook
- Non esiste un framework di test automatizzato per i notebook
- Validazione manuale: Esegui tutte le celle in sequenza per assicurarti che non ci siano errori
- Verifica che i file di dati siano accessibili e che gli output vengano generati correttamente
- Controlla che le visualizzazioni vengano renderizzate correttamente

### Test della Documentazione
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Controlli di Qualità del Codice
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Linee Guida per lo Stile del Codice

### Python (Jupyter Notebooks)
- Segui le linee guida di stile PEP 8 per il codice Python
- Usa nomi di variabili chiari che spieghino i dati analizzati
- Includi celle markdown con spiegazioni prima delle celle di codice
- Mantieni le celle di codice focalizzate su concetti o operazioni singole
- Usa pandas per la manipolazione dei dati, matplotlib per la visualizzazione
- Modello comune di importazione:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Segui la guida di stile Vue.js 2 e le migliori pratiche
- Configurazione ESLint in `quiz-app/package.json`
- Usa componenti Vue a file singolo (.vue files)
- Mantieni un'architettura basata sui componenti
- Esegui `npm run lint` prima di inviare modifiche

### Documentazione Markdown
- Usa una gerarchia chiara di intestazioni (# ## ### ecc.)
- Includi blocchi di codice con specificatori di linguaggio
- Aggiungi testo alternativo per le immagini
- Collega lezioni e risorse correlate
- Mantieni lunghezze di riga ragionevoli per la leggibilità

### Organizzazione dei File
- Contenuti delle lezioni in cartelle numerate (01-defining-data-science, ecc.)
- Soluzioni in sottocartelle dedicate `solution/`
- Le traduzioni rispecchiano la struttura inglese nella cartella `translations/`
- Mantieni i file di dati in `data/` o cartelle specifiche per le lezioni

## Build e Deployment

### Deployment dell'Applicazione per Quiz
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Deployment di Azure Static Web Apps
L'app quiz può essere distribuita su Azure Static Web Apps:
1. Crea una risorsa Azure Static Web App
2. Connetti al repository GitHub
3. Configura le impostazioni di build:
   - Posizione dell'app: `quiz-app`
   - Posizione dell'output: `dist`
4. Il workflow GitHub Actions distribuirà automaticamente al push

### Sito di Documentazione
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Il repository include configurazione del contenitore di sviluppo
- Codespaces configura automaticamente l'ambiente Python e Node.js
- Apri il repository in Codespace tramite l'interfaccia GitHub
- Tutte le dipendenze vengono installate automaticamente

## Linee Guida per le Pull Request

### Prima di Inviare
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Formato del Titolo della PR
- Usa titoli chiari e descrittivi
- Formato: `[Componente] Breve descrizione`
- Esempi:
  - `[Lezione 7] Correggi errore di importazione nel notebook Python`
  - `[Applicazione Quiz] Aggiungi traduzione in tedesco`
  - `[Documentazione] Aggiorna README con nuovi prerequisiti`

### Controlli Richiesti
- Assicurati che tutto il codice venga eseguito senza errori
- Verifica che i notebook vengano eseguiti completamente
- Conferma che le app Vue.js vengano compilate con successo
- Controlla che i link della documentazione funzionino
- Testa l'app quiz se modificata
- Verifica che le traduzioni mantengano una struttura coerente

### Linee Guida per il Contributo
- Segui lo stile e i modelli di codice esistenti
- Aggiungi commenti esplicativi per logiche complesse
- Aggiorna la documentazione pertinente
- Testa le modifiche su diversi moduli di lezione, se applicabile
- Consulta il file CONTRIBUTING.md

## Note Aggiuntive

### Librerie Comuni Utilizzate
- **pandas**: Manipolazione e analisi dei dati
- **numpy**: Calcolo numerico
- **matplotlib**: Visualizzazione e grafici dei dati
- **seaborn**: Visualizzazione statistica dei dati (alcune lezioni)
- **scikit-learn**: Machine learning (lezioni avanzate)

### Lavorare con i File di Dati
- File di dati situati nella cartella `data/` o nelle directory specifiche delle lezioni
- La maggior parte dei notebook si aspetta file di dati in percorsi relativi
- I file CSV sono il formato principale dei dati
- Alcune lezioni utilizzano JSON per esempi di dati non relazionali

### Supporto Multilingue
- Traduzioni in oltre 40 lingue tramite GitHub Actions automatizzati
- Workflow di traduzione in `.github/workflows/co-op-translator.yml`
- Traduzioni nella cartella `translations/` con codici lingua
- Traduzioni dei quiz in `quiz-app/src/assets/translations/`

### Opzioni per l'Ambiente di Sviluppo
1. **Sviluppo Locale**: Installa Python, Jupyter, Node.js localmente
2. **GitHub Codespaces**: Ambiente di sviluppo istantaneo basato su cloud
3. **Contenitori Dev di VS Code**: Sviluppo locale basato su contenitori
4. **Binder**: Avvia notebook nel cloud (se configurato)

### Linee Guida per i Contenuti delle Lezioni
- Ogni lezione è autonoma ma si basa su concetti precedenti
- I quiz pre-lezione testano le conoscenze pregresse
- I quiz post-lezione rafforzano l'apprendimento
- I compiti forniscono pratica pratica
- Gli sketchnotes offrono riassunti visivi

### Risoluzione dei Problemi Comuni

**Problemi con il Kernel di Jupyter:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Errori di Installazione npm:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Errori di Importazione nei Notebook:**
- Verifica che tutte le librerie richieste siano installate
- Controlla la compatibilità della versione di Python (consigliato Python 3.7+)
- Assicurati che l'ambiente virtuale sia attivato

**Docsify Non Carica:**
- Verifica che stai servendo dalla radice del repository
- Controlla che `index.html` esista
- Assicurati di avere accesso alla rete corretta (porta 3000)

### Considerazioni sulle Prestazioni
- I dataset di grandi dimensioni potrebbero richiedere tempo per il caricamento nei notebook
- Il rendering delle visualizzazioni può essere lento per grafici complessi
- Il server di sviluppo Vue.js abilita l'hot-reload per iterazioni rapide
- Le build di produzione sono ottimizzate e minificate

### Note sulla Sicurezza
- Non devono essere commessi dati sensibili o credenziali
- Usa variabili d'ambiente per eventuali chiavi API nelle lezioni cloud
- Le lezioni relative ad Azure potrebbero richiedere credenziali dell'account Azure
- Mantieni le dipendenze aggiornate per le patch di sicurezza

## Contribuire alle Traduzioni
- Le traduzioni automatizzate sono gestite tramite GitHub Actions
- Correzioni manuali sono benvenute per migliorare l'accuratezza delle traduzioni
- Segui la struttura esistente delle cartelle di traduzione
- Aggiorna i link dei quiz per includere il parametro della lingua: `?loc=fr`
- Testa le lezioni tradotte per verificarne il corretto rendering

## Risorse Correlate
- Curriculum principale: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Forum di discussione: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Altri curricula Microsoft: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Manutenzione del Progetto
- Aggiornamenti regolari per mantenere i contenuti attuali
- Contributi della comunità benvenuti
- Problemi tracciati su GitHub
- PR revisionate dai manutentori del curriculum
- Revisioni e aggiornamenti mensili dei contenuti

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.