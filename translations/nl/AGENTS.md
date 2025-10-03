<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:28:02+00:00",
  "source_file": "AGENTS.md",
  "language_code": "nl"
}
-->
# AGENTS.md

## Projectoverzicht

Data Science for Beginners is een uitgebreide 10-weekse, 20-lessen curriculum ontwikkeld door Microsoft Azure Cloud Advocates. De repository is een leerbron die fundamentele data science-concepten onderwijst via projectgebaseerde lessen, inclusief Jupyter-notebooks, interactieve quizzen en praktische opdrachten.

**Belangrijke technologieën:**
- **Jupyter Notebooks**: Primair leermedium met Python 3
- **Python-bibliotheken**: pandas, numpy, matplotlib voor data-analyse en visualisatie
- **Vue.js 2**: Quizapplicatie (quiz-app map)
- **Docsify**: Documentatiesitegenerator voor offline toegang
- **Node.js/npm**: Pakketbeheer voor JavaScript-componenten
- **Markdown**: Alle lesinhoud en documentatie

**Architectuur:**
- Meertalige educatieve repository met uitgebreide vertalingen
- Gestructureerd in lesmodules (1-Introduction tot 6-Data-Science-In-Wild)
- Elke les bevat README, notebooks, opdrachten en quizzen
- Zelfstandige Vue.js quizapplicatie voor pre/post-les beoordelingen
- Ondersteuning voor GitHub Codespaces en VS Code dev containers

## Setupcommando's

### Repository Setup
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Python-omgeving instellen
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Quizapplicatie instellen
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

### Docsify documentatieserver
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Visualisatieprojecten instellen
Voor visualisatieprojecten zoals meaningful-visualizations (les 13):
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


## Ontwikkelworkflow

### Werken met Jupyter Notebooks
1. Start Jupyter in de root van de repository: `jupyter notebook`
2. Navigeer naar de gewenste lesmap
3. Open `.ipynb` bestanden om oefeningen door te nemen
4. Notebooks zijn zelfstandig met uitleg en codecellen
5. De meeste notebooks gebruiken pandas, numpy en matplotlib - zorg ervoor dat deze geïnstalleerd zijn

### Lesstructuur
Elke les bevat doorgaans:
- `README.md` - Hoofdlesinhoud met theorie en voorbeelden
- `notebook.ipynb` - Praktische Jupyter-notebook oefeningen
- `assignment.ipynb` of `assignment.md` - Oefenopdrachten
- `solution/` map - Oplossingsnotebooks en code
- `images/` map - Ondersteunend visueel materiaal

### Ontwikkeling van de quizapplicatie
- Vue.js 2 applicatie met hot-reload tijdens ontwikkeling
- Quizzen opgeslagen in `quiz-app/src/assets/translations/`
- Elke taal heeft zijn eigen vertaalmap (en, fr, es, etc.)
- Quiznummering begint bij 0 en loopt op tot 39 (40 quizzen totaal)

### Vertalingen toevoegen
- Vertalingen gaan in de `translations/` map in de root van de repository
- Elke taal heeft een complete lesstructuur die de Engelse structuur weerspiegelt
- Geautomatiseerde vertaling via GitHub Actions (co-op-translator.yml)

## Testinstructies

### Testen van de quizapplicatie
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Testen van notebooks
- Er bestaat geen geautomatiseerd testframework voor notebooks
- Handmatige validatie: Voer alle cellen achter elkaar uit om te controleren op fouten
- Controleer of databestanden toegankelijk zijn en outputs correct worden gegenereerd
- Controleer of visualisaties correct worden weergegeven

### Testen van documentatie
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Controle van codekwaliteit
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Richtlijnen voor codestijl

### Python (Jupyter Notebooks)
- Volg PEP 8 stijlrichtlijnen voor Python-code
- Gebruik duidelijke variabelenamen die de geanalyseerde data beschrijven
- Voeg markdown-cellen toe met uitleg vóór codecellen
- Houd codecellen gericht op één concept of operatie
- Gebruik pandas voor datamanipulatie, matplotlib voor visualisatie
- Veelgebruikte importpatroon:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Volg Vue.js 2 stijlrichtlijnen en best practices
- ESLint-configuratie in `quiz-app/package.json`
- Gebruik Vue single-file componenten (.vue bestanden)
- Behoud componentgebaseerde architectuur
- Voer `npm run lint` uit voordat je wijzigingen commit

### Markdown-documentatie
- Gebruik een duidelijke koppenhiërarchie (# ## ### etc.)
- Voeg codeblokken toe met taalspecificaties
- Voeg alt-tekst toe voor afbeeldingen
- Link naar gerelateerde lessen en bronnen
- Houd regellengtes redelijk voor leesbaarheid

### Bestandsorganisatie
- Lesinhoud in genummerde mappen (01-defining-data-science, etc.)
- Oplossingen in toegewijde `solution/` submappen
- Vertalingen spiegelen de Engelse structuur in de `translations/` map
- Houd databestanden in `data/` of les-specifieke mappen

## Build en deployment

### Deployment van de quizapplicatie
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Azure Static Web Apps Deployment
De quiz-app kan worden gedeployed naar Azure Static Web Apps:
1. Maak een Azure Static Web App resource aan
2. Verbind met de GitHub-repository
3. Configureer buildinstellingen:
   - App-locatie: `quiz-app`
   - Output-locatie: `dist`
4. GitHub Actions workflow zal automatisch deployen bij een push

### Documentatiesite
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Repository bevat dev container configuratie
- Codespaces stelt automatisch Python- en Node.js-omgeving in
- Open repository in Codespace via GitHub UI
- Alle afhankelijkheden worden automatisch geïnstalleerd

## Richtlijnen voor pull requests

### Voor het indienen
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### PR-titel formaat
- Gebruik duidelijke, beschrijvende titels
- Formaat: `[Component] Korte beschrijving`
- Voorbeelden:
  - `[Les 7] Fix Python notebook importfout`
  - `[Quiz App] Voeg Duitse vertaling toe`
  - `[Docs] Update README met nieuwe vereisten`

### Vereiste controles
- Zorg ervoor dat alle code zonder fouten draait
- Controleer dat notebooks volledig worden uitgevoerd
- Bevestig dat Vue.js apps succesvol bouwen
- Controleer dat documentatielinks werken
- Test de quizapplicatie indien gewijzigd
- Controleer of vertalingen een consistente structuur behouden

### Richtlijnen voor bijdragen
- Volg bestaande codestijl en patronen
- Voeg verklarende opmerkingen toe voor complexe logica
- Update relevante documentatie
- Test wijzigingen in verschillende lesmodules indien van toepassing
- Bekijk het CONTRIBUTING.md bestand

## Aanvullende opmerkingen

### Veelgebruikte bibliotheken
- **pandas**: Datamanipulatie en analyse
- **numpy**: Numerieke berekeningen
- **matplotlib**: Datavisualisatie en grafieken
- **seaborn**: Statistische datavisualisatie (sommige lessen)
- **scikit-learn**: Machine learning (gevorderde lessen)

### Werken met databestanden
- Databestanden bevinden zich in de `data/` map of les-specifieke mappen
- De meeste notebooks verwachten databestanden in relatieve paden
- CSV-bestanden zijn het primaire dataformaat
- Sommige lessen gebruiken JSON voor voorbeelden van niet-relationele data

### Meertalige ondersteuning
- 40+ taalvertalingen via geautomatiseerde GitHub Actions
- Vertaalworkflow in `.github/workflows/co-op-translator.yml`
- Vertalingen in de `translations/` map met taalcodes
- Quizvertalingen in `quiz-app/src/assets/translations/`

### Opties voor ontwikkelomgeving
1. **Lokale ontwikkeling**: Installeer Python, Jupyter, Node.js lokaal
2. **GitHub Codespaces**: Cloudgebaseerde directe ontwikkelomgeving
3. **VS Code Dev Containers**: Lokale containergebaseerde ontwikkeling
4. **Binder**: Start notebooks in de cloud (indien geconfigureerd)

### Richtlijnen voor lesinhoud
- Elke les is zelfstandig maar bouwt voort op eerdere concepten
- Pre-les quizzen testen voorkennis
- Post-les quizzen versterken het geleerde
- Opdrachten bieden praktische oefening
- Sketchnotes bieden visuele samenvattingen

### Veelvoorkomende problemen oplossen

**Jupyter Kernel Problemen:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**npm Installatiefouten:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Importfouten in notebooks:**
- Controleer of alle vereiste bibliotheken zijn geïnstalleerd
- Controleer Python-versiecompatibiliteit (Python 3.7+ aanbevolen)
- Zorg ervoor dat de virtuele omgeving is geactiveerd

**Docsify Laadt Niet:**
- Controleer of je serveert vanuit de root van de repository
- Controleer of `index.html` bestaat
- Zorg voor juiste netwerktoegang (poort 3000)

### Prestatieoverwegingen
- Grote datasets kunnen tijd kosten om te laden in notebooks
- Rendering van visualisaties kan traag zijn voor complexe grafieken
- Vue.js dev server biedt hot-reload voor snelle iteratie
- Productiebouws zijn geoptimaliseerd en geminimaliseerd

### Veiligheidsopmerkingen
- Geen gevoelige data of inloggegevens mogen worden gecommit
- Gebruik omgevingsvariabelen voor API-sleutels in cloudlessen
- Azure-gerelateerde lessen kunnen Azure-accountgegevens vereisen
- Houd afhankelijkheden up-to-date voor beveiligingspatches

## Bijdragen aan vertalingen
- Geautomatiseerde vertalingen beheerd via GitHub Actions
- Handmatige correcties welkom voor vertaalnauwkeurigheid
- Volg bestaande structuur van vertaalmappen
- Update quizlinks om taalparameter toe te voegen: `?loc=fr`
- Test vertaalde lessen op correcte weergave

## Gerelateerde bronnen
- Hoofdcurriculum: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Discussieforum: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Andere Microsoft curricula: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Projectonderhoud
- Regelmatige updates om inhoud actueel te houden
- Bijdragen van de gemeenschap welkom
- Problemen worden bijgehouden op GitHub
- PR's worden beoordeeld door curriculumbeheerders
- Maandelijkse inhoudsbeoordelingen en updates

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.