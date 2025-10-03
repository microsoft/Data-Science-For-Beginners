<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:26:12+00:00",
  "source_file": "AGENTS.md",
  "language_code": "no"
}
-->
# AGENTS.md

## Prosjektoversikt

Data Science for Beginners er et omfattende 10-ukers, 20-leksjons pensum opprettet av Microsoft Azure Cloud Advocates. Repositoriet er en læringsressurs som lærer grunnleggende konsepter innen data science gjennom prosjektbaserte leksjoner, inkludert Jupyter-notebooks, interaktive quizer og praktiske oppgaver.

**Nøkkelteknologier:**
- **Jupyter Notebooks**: Primært læringsmedium med Python 3
- **Python-biblioteker**: pandas, numpy, matplotlib for dataanalyse og visualisering
- **Vue.js 2**: Quiz-applikasjon (quiz-app-mappe)
- **Docsify**: Dokumentasjonsgenerator for offline tilgang
- **Node.js/npm**: Pakkehåndtering for JavaScript-komponenter
- **Markdown**: Alt leksjonsinnhold og dokumentasjon

**Arkitektur:**
- Flerspråklig utdanningsrepository med omfattende oversettelser
- Strukturert i leksjonsmoduler (1-Introduksjon til 6-Data-Science-In-Wild)
- Hver leksjon inkluderer README, notebooks, oppgaver og quizer
- Selvstendig Vue.js quiz-applikasjon for vurderinger før/etter leksjoner
- Støtte for GitHub Codespaces og VS Code utviklingscontainere

## Oppsettskommandoer

### Repository-oppsett
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Python-miljøoppsett
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Oppsett av quiz-applikasjon
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

### Docsify dokumentasjonsserver
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Oppsett av visualiseringsprosjekter
For visualiseringsprosjekter som meaningful-visualizations (leksjon 13):
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


## Utviklingsarbeidsflyt

### Arbeide med Jupyter Notebooks
1. Start Jupyter i repository-roten: `jupyter notebook`
2. Naviger til ønsket leksjonsmappe
3. Åpne `.ipynb`-filer for å jobbe gjennom øvelser
4. Notebooks er selvstendige med forklaringer og kodeceller
5. De fleste notebooks bruker pandas, numpy og matplotlib - sørg for at disse er installert

### Leksjonsstruktur
Hver leksjon inneholder typisk:
- `README.md` - Hovedinnhold med teori og eksempler
- `notebook.ipynb` - Praktiske Jupyter-notebook-øvelser
- `assignment.ipynb` eller `assignment.md` - Praktiske oppgaver
- `solution/`-mappe - Løsningsnotebooks og kode
- `images/`-mappe - Støttende visuelle materialer

### Utvikling av quiz-applikasjon
- Vue.js 2-applikasjon med hot-reload under utvikling
- Quizer lagret i `quiz-app/src/assets/translations/`
- Hvert språk har sin egen oversettelsesmappe (en, fr, es, etc.)
- Quiznummerering starter på 0 og går opp til 39 (40 quizer totalt)

### Legge til oversettelser
- Oversettelser legges i `translations/`-mappen i repository-roten
- Hvert språk har komplett leksjonsstruktur speilet fra engelsk
- Automatisk oversettelse via GitHub Actions (co-op-translator.yml)

## Testinstruksjoner

### Testing av quiz-applikasjon
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Testing av notebooks
- Ingen automatisert testrammeverk finnes for notebooks
- Manuell validering: Kjør alle celler i rekkefølge for å sikre ingen feil
- Verifiser at datafiler er tilgjengelige og at utdata genereres korrekt
- Sjekk at visualiseringer vises riktig

### Testing av dokumentasjon
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Kvalitetssjekk av kode
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Retningslinjer for kodestil

### Python (Jupyter Notebooks)
- Følg PEP 8-stilretningslinjer for Python-kode
- Bruk klare variabelnavn som forklarer dataene som analyseres
- Inkluder markdown-celler med forklaringer før kodeceller
- Hold kodeceller fokusert på enkeltkonsepter eller operasjoner
- Bruk pandas for datamanipulering, matplotlib for visualisering
- Vanlig importmønster:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Følg Vue.js 2-stilguide og beste praksis
- ESLint-konfigurasjon i `quiz-app/package.json`
- Bruk Vue single-file-komponenter (.vue-filer)
- Oppretthold komponentbasert arkitektur
- Kjør `npm run lint` før du sender inn endringer

### Markdown-dokumentasjon
- Bruk klar overskriftsstruktur (# ## ### osv.)
- Inkluder kodeblokker med språkspesifikasjoner
- Legg til alt-tekst for bilder
- Lenke til relaterte leksjoner og ressurser
- Hold linjelengder rimelige for lesbarhet

### Filorganisering
- Leksjonsinnhold i nummererte mapper (01-defining-data-science, etc.)
- Løsninger i dedikerte `solution/`-undermapper
- Oversettelser speiler engelsk struktur i `translations/`-mappen
- Hold datafiler i `data/` eller leksjonsspesifikke mapper

## Bygging og distribusjon

### Distribusjon av quiz-applikasjon
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Distribusjon av Azure Static Web Apps
Quiz-applikasjonen kan distribueres til Azure Static Web Apps:
1. Opprett Azure Static Web App-ressurs
2. Koble til GitHub-repository
3. Konfigurer bygginnstillinger:
   - Applikasjonsplassering: `quiz-app`
   - Utdata-plassering: `dist`
4. GitHub Actions-arbeidsflyt vil automatisk distribuere ved push

### Dokumentasjonsnettsted
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Repository inkluderer utviklingscontainer-konfigurasjon
- Codespaces setter automatisk opp Python- og Node.js-miljø
- Åpne repository i Codespace via GitHub UI
- Alle avhengigheter installeres automatisk

## Retningslinjer for pull requests

### Før innsending
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Format for PR-titler
- Bruk klare, beskrivende titler
- Format: `[Komponent] Kort beskrivelse`
- Eksempler:
  - `[Leksjon 7] Fiks Python-notebook importfeil`
  - `[Quiz App] Legg til tysk oversettelse`
  - `[Docs] Oppdater README med nye forutsetninger`

### Nødvendige sjekker
- Sørg for at all kode kjører uten feil
- Verifiser at notebooks kjører fullstendig
- Bekreft at Vue.js-applikasjoner bygges vellykket
- Sjekk at dokumentasjonslenker fungerer
- Test quiz-applikasjonen hvis den er endret
- Verifiser at oversettelser opprettholder konsistent struktur

### Retningslinjer for bidrag
- Følg eksisterende kodestil og mønstre
- Legg til forklarende kommentarer for kompleks logikk
- Oppdater relevant dokumentasjon
- Test endringer på tvers av ulike leksjonsmoduler hvis aktuelt
- Se gjennom CONTRIBUTING.md-filen

## Tilleggsnotater

### Vanlige biblioteker brukt
- **pandas**: Datamanipulering og analyse
- **numpy**: Numerisk databehandling
- **matplotlib**: Datavisualisering og plotting
- **seaborn**: Statistisk datavisualisering (noen leksjoner)
- **scikit-learn**: Maskinlæring (avanserte leksjoner)

### Arbeide med datafiler
- Datafiler plassert i `data/`-mappen eller leksjonsspesifikke kataloger
- De fleste notebooks forventer datafiler i relative stier
- CSV-filer er primært dataformat
- Noen leksjoner bruker JSON for eksempler på ikke-relasjonelle data

### Flerspråklig støtte
- 40+ språkoversettelser via automatiserte GitHub Actions
- Oversettelsesarbeidsflyt i `.github/workflows/co-op-translator.yml`
- Oversettelser i `translations/`-mappen med språkkoder
- Quiz-oversettelser i `quiz-app/src/assets/translations/`

### Utviklingsmiljøalternativer
1. **Lokal utvikling**: Installer Python, Jupyter, Node.js lokalt
2. **GitHub Codespaces**: Skybasert øyeblikkelig utviklingsmiljø
3. **VS Code Dev Containers**: Lokalt containerbasert utvikling
4. **Binder**: Start notebooks i skyen (hvis konfigurert)

### Retningslinjer for leksjonsinnhold
- Hver leksjon er selvstendig, men bygger på tidligere konsepter
- Quizer før leksjonen tester forkunnskaper
- Quizer etter leksjonen forsterker læring
- Oppgaver gir praktisk trening
- Sketchnotes gir visuelle oppsummeringer

### Feilsøking av vanlige problemer

**Jupyter-kjerneproblemer:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**npm-installasjonsfeil:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Importfeil i notebooks:**
- Verifiser at alle nødvendige biblioteker er installert
- Sjekk Python-versjonskompatibilitet (Python 3.7+ anbefalt)
- Sørg for at virtuelt miljø er aktivert

**Docsify laster ikke:**
- Verifiser at du serverer fra repository-roten
- Sjekk at `index.html` eksisterer
- Sørg for riktig nettverkstilgang (port 3000)

### Ytelseshensyn
- Store datasett kan ta tid å laste i notebooks
- Visualiseringsrendering kan være treg for komplekse grafer
- Vue.js utviklingsserver muliggjør hot-reload for rask iterasjon
- Produksjonsbygg er optimalisert og minifisert

### Sikkerhetsnotater
- Ingen sensitiv data eller legitimasjon skal legges inn
- Bruk miljøvariabler for eventuelle API-nøkler i sky-leksjoner
- Azure-relaterte leksjoner kan kreve Azure-kontolegitimasjon
- Hold avhengigheter oppdatert for sikkerhetsoppdateringer

## Bidra til oversettelser
- Automatiserte oversettelser administrert via GitHub Actions
- Manuelle korrigeringer ønskes velkommen for oversettelsesnøyaktighet
- Følg eksisterende oversettelsesmappe-struktur
- Oppdater quiz-lenker for å inkludere språkparameter: `?loc=fr`
- Test oversatte leksjoner for riktig visning

## Relaterte ressurser
- Hovedpensum: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Diskusjonsforum: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Andre Microsoft-pensum: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Prosjektvedlikehold
- Regelmessige oppdateringer for å holde innholdet aktuelt
- Bidrag fra fellesskapet ønskes velkommen
- Problemer spores på GitHub
- PR-er gjennomgås av pensumansvarlige
- Månedlige innholdsrevisjoner og oppdateringer

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.