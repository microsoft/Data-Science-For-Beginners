<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:24:03+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sv"
}
-->
# AGENTS.md

## Projektöversikt

Data Science for Beginners är en omfattande 10-veckors, 20-lektions läroplan skapad av Microsoft Azure Cloud Advocates. Repositoriet är en lärresurs som lär ut grundläggande datavetenskapliga koncept genom projektbaserade lektioner, inklusive Jupyter-notebooks, interaktiva quiz och praktiska uppgifter.

**Nyckelteknologier:**
- **Jupyter Notebooks**: Primärt läromedel med Python 3
- **Python-bibliotek**: pandas, numpy, matplotlib för dataanalys och visualisering
- **Vue.js 2**: Quiz-applikation (quiz-app-mapp)
- **Docsify**: Dokumentationsgenerator för offlineåtkomst
- **Node.js/npm**: Paketadministration för JavaScript-komponenter
- **Markdown**: Allt lektionsinnehåll och dokumentation

**Arkitektur:**
- Flerspråkigt utbildningsrepository med omfattande översättningar
- Strukturerat i lektionsmoduler (1-Introduction till 6-Data-Science-In-Wild)
- Varje lektion innehåller README, notebooks, uppgifter och quiz
- Fristående Vue.js quiz-applikation för bedömningar före/efter lektion
- Stöd för GitHub Codespaces och VS Code utvecklingscontainrar

## Installationskommandon

### Repository-installation
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Python-miljöinstallation
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Quiz-applikationsinstallation
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

### Docsify-dokumentationsserver
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Installation av visualiseringsprojekt
För visualiseringsprojekt som meaningful-visualizations (lektion 13):
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


## Utvecklingsarbetsflöde

### Arbeta med Jupyter Notebooks
1. Starta Jupyter i repositoryns rot: `jupyter notebook`
2. Navigera till önskad lektionsmapp
3. Öppna `.ipynb`-filer för att arbeta igenom övningar
4. Notebooks är självständiga med förklaringar och kodceller
5. De flesta notebooks använder pandas, numpy och matplotlib - se till att dessa är installerade

### Lektionsstruktur
Varje lektion innehåller vanligtvis:
- `README.md` - Huvudinnehåll med teori och exempel
- `notebook.ipynb` - Praktiska Jupyter-notebook-övningar
- `assignment.ipynb` eller `assignment.md` - Praktiska uppgifter
- `solution/`-mapp - Lösningsnotebooks och kod
- `images/`-mapp - Stödjande visuellt material

### Utveckling av quiz-applikation
- Vue.js 2-applikation med hot-reload under utveckling
- Quiz lagras i `quiz-app/src/assets/translations/`
- Varje språk har sin egen översättningsmapp (en, fr, es, etc.)
- Quiznumrering börjar på 0 och går upp till 39 (totalt 40 quiz)

### Lägga till översättningar
- Översättningar placeras i `translations/`-mappen i repositoryns rot
- Varje språk har en komplett lektionsstruktur speglad från engelska
- Automatiserad översättning via GitHub Actions (co-op-translator.yml)

## Testinstruktioner

### Testning av quiz-applikation
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Testning av notebooks
- Inget automatiserat testverktyg finns för notebooks
- Manuell validering: Kör alla celler i ordning för att säkerställa att inga fel uppstår
- Kontrollera att datafiler är åtkomliga och att utdata genereras korrekt
- Kontrollera att visualiseringar renderas korrekt

### Testning av dokumentation
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Kontroll av kodkvalitet
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Kodstilsguider

### Python (Jupyter Notebooks)
- Följ PEP 8-stilguider för Python-kod
- Använd tydliga variabelnamn som förklarar den analyserade datan
- Inkludera markdown-celler med förklaringar före kodceller
- Håll kodceller fokuserade på enskilda koncept eller operationer
- Använd pandas för datamanipulation, matplotlib för visualisering
- Vanligt importmönster:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Följ Vue.js 2-stilguide och bästa praxis
- ESLint-konfiguration i `quiz-app/package.json`
- Använd Vue single-file-komponenter (.vue-filer)
- Bibehåll komponentbaserad arkitektur
- Kör `npm run lint` innan du skickar ändringar

### Markdown-dokumentation
- Använd tydlig rubrikhierarki (# ## ### etc.)
- Inkludera kodblock med språkangivelser
- Lägg till alt-text för bilder
- Länka till relaterade lektioner och resurser
- Håll radlängder rimliga för läsbarhet

### Filorganisation
- Lektionsinnehåll i numrerade mappar (01-defining-data-science, etc.)
- Lösningar i dedikerade `solution/`-undermappar
- Översättningar speglar engelsk struktur i `translations/`-mappen
- Håll datafiler i `data/` eller lektionsspecifika mappar

## Bygg och distribution

### Distribution av quiz-applikation
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Distribution av Azure Static Web Apps
Quiz-applikationen kan distribueras till Azure Static Web Apps:
1. Skapa en Azure Static Web App-resurs
2. Anslut till GitHub-repository
3. Konfigurera bygginställningar:
   - Applikationsplats: `quiz-app`
   - Utdata-plats: `dist`
4. GitHub Actions-arbetsflöde distribuerar automatiskt vid push

### Dokumentationssida
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Repository innehåller utvecklingscontainerkonfiguration
- Codespaces ställer automatiskt in Python- och Node.js-miljö
- Öppna repository i Codespace via GitHub UI
- Alla beroenden installeras automatiskt

## Riktlinjer för pull requests

### Innan du skickar in
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Format för PR-titlar
- Använd tydliga, beskrivande titlar
- Format: `[Komponent] Kort beskrivning`
- Exempel:
  - `[Lektion 7] Åtgärda importfel i Python-notebook`
  - `[Quiz App] Lägg till tysk översättning`
  - `[Docs] Uppdatera README med nya förutsättningar`

### Obligatoriska kontroller
- Säkerställ att all kod körs utan fel
- Verifiera att notebooks exekveras helt
- Bekräfta att Vue.js-appar byggs framgångsrikt
- Kontrollera att dokumentationslänkar fungerar
- Testa quiz-applikationen om den har ändrats
- Verifiera att översättningar bibehåller konsekvent struktur

### Riktlinjer för bidrag
- Följ befintlig kodstil och mönster
- Lägg till förklarande kommentarer för komplex logik
- Uppdatera relevant dokumentation
- Testa ändringar över olika lektionsmoduler om tillämpligt
- Granska CONTRIBUTING.md-filen

## Ytterligare anteckningar

### Vanliga bibliotek som används
- **pandas**: Datamanipulation och analys
- **numpy**: Numerisk beräkning
- **matplotlib**: Datavisualisering och diagram
- **seaborn**: Statistisk datavisualisering (vissa lektioner)
- **scikit-learn**: Maskininlärning (avancerade lektioner)

### Arbeta med datafiler
- Datafiler finns i `data/`-mappen eller lektionsspecifika kataloger
- De flesta notebooks förväntar sig datafiler i relativa sökvägar
- CSV-filer är det primära dataformatet
- Vissa lektioner använder JSON för exempel på icke-relationell data

### Flerspråkigt stöd
- 40+ språköversättningar via automatiserade GitHub Actions
- Översättningsarbetsflöde i `.github/workflows/co-op-translator.yml`
- Översättningar i `translations/`-mappen med språkkoder
- Quiz-översättningar i `quiz-app/src/assets/translations/`

### Alternativ för utvecklingsmiljö
1. **Lokal utveckling**: Installera Python, Jupyter, Node.js lokalt
2. **GitHub Codespaces**: Molnbaserad omedelbar utvecklingsmiljö
3. **VS Code Dev Containers**: Lokal containerbaserad utveckling
4. **Binder**: Starta notebooks i molnet (om konfigurerat)

### Riktlinjer för lektionsinnehåll
- Varje lektion är fristående men bygger på tidigare koncept
- Quiz före lektionen testar förkunskaper
- Quiz efter lektionen förstärker lärandet
- Uppgifter ger praktisk övning
- Sketchnotes ger visuella sammanfattningar

### Felsökning av vanliga problem

**Problem med Jupyter-kärnan:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Fel vid npm-installation:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Importfel i notebooks:**
- Kontrollera att alla nödvändiga bibliotek är installerade
- Kontrollera Python-versionens kompatibilitet (Python 3.7+ rekommenderas)
- Säkerställ att den virtuella miljön är aktiverad

**Docsify laddas inte:**
- Kontrollera att du serverar från repositoryns rot
- Kontrollera att `index.html` finns
- Säkerställ korrekt nätverksåtkomst (port 3000)

### Prestandahänsyn
- Stora dataset kan ta tid att ladda i notebooks
- Visualiseringsrendering kan vara långsam för komplexa diagram
- Vue.js utvecklingsserver möjliggör hot-reload för snabb iteration
- Produktionsbyggen är optimerade och minifierade

### Säkerhetsanteckningar
- Ingen känslig data eller autentiseringsuppgifter bör skickas in
- Använd miljövariabler för API-nycklar i molnlektioner
- Azure-relaterade lektioner kan kräva Azure-kontouppgifter
- Håll beroenden uppdaterade för säkerhetsfixar

## Bidra till översättningar
- Automatiserade översättningar hanteras via GitHub Actions
- Manuella korrigeringar välkomnas för översättningsnoggrannhet
- Följ befintlig översättningsmappstruktur
- Uppdatera quiz-länkar för att inkludera språkparameter: `?loc=fr`
- Testa översatta lektioner för korrekt rendering

## Relaterade resurser
- Huvudläroplan: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Diskussionsforum: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Andra Microsoft-läroplaner: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Projektunderhåll
- Regelbundna uppdateringar för att hålla innehållet aktuellt
- Gemenskapsbidrag välkomnas
- Problem spåras på GitHub
- PRs granskas av läroplansansvariga
- Månatliga innehållsgranskningar och uppdateringar

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.