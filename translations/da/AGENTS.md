<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:25:00+00:00",
  "source_file": "AGENTS.md",
  "language_code": "da"
}
-->
# AGENTS.md

## Projektoversigt

Data Science for Beginners er et omfattende 10-ugers, 20-lektions pensum skabt af Microsoft Azure Cloud Advocates. Repositoriet er en læringsressource, der underviser i grundlæggende data science-koncepter gennem projektbaserede lektioner, herunder Jupyter-notebooks, interaktive quizzer og praktiske opgaver.

**Nøgleteknologier:**
- **Jupyter Notebooks**: Primært læringsmedium ved brug af Python 3
- **Python-biblioteker**: pandas, numpy, matplotlib til dataanalyse og visualisering
- **Vue.js 2**: Quiz-applikation (quiz-app-mappe)
- **Docsify**: Dokumentationsgenerator til offline adgang
- **Node.js/npm**: Pakkehåndtering til JavaScript-komponenter
- **Markdown**: Alt lektionsindhold og dokumentation

**Arkitektur:**
- Flersproget uddannelsesrepository med omfattende oversættelser
- Struktureret i lektionsmoduler (1-Introduction til 6-Data-Science-In-Wild)
- Hver lektion inkluderer README, notebooks, opgaver og quizzer
- Selvstændig Vue.js quiz-applikation til før/efter-lektionsvurderinger
- GitHub Codespaces og VS Code dev-containere understøttes

## Opsætningskommandoer

### Repository-opsætning
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Opsætning af Python-miljø
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Opsætning af quiz-applikation
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

### Opsætning af visualiseringsprojekter
For visualiseringsprojekter som meaningful-visualizations (lektion 13):
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


## Udviklingsarbejdsgang

### Arbejde med Jupyter-notebooks
1. Start Jupyter i repositoryets rod: `jupyter notebook`
2. Naviger til den ønskede lektionsmappe
3. Åbn `.ipynb`-filer for at arbejde med øvelserne
4. Notebooks er selvstændige med forklaringer og kodeceller
5. De fleste notebooks bruger pandas, numpy og matplotlib - sørg for, at disse er installeret

### Lektionsstruktur
Hver lektion indeholder typisk:
- `README.md` - Hovedindhold med teori og eksempler
- `notebook.ipynb` - Praktiske Jupyter-notebook-øvelser
- `assignment.ipynb` eller `assignment.md` - Øvelsesopgaver
- `solution/`-mappe - Løsningsnotebooks og kode
- `images/`-mappe - Understøttende visuelle materialer

### Udvikling af quiz-applikation
- Vue.js 2-applikation med hot-reload under udvikling
- Quizzer gemmes i `quiz-app/src/assets/translations/`
- Hvert sprog har sin egen oversættelsesmappe (en, fr, es osv.)
- Quiznummerering starter ved 0 og går op til 39 (i alt 40 quizzer)

### Tilføjelse af oversættelser
- Oversættelser placeres i `translations/`-mappen i repositoryets rod
- Hvert sprog har en komplet lektionsstruktur, der spejler engelsk
- Automatiseret oversættelse via GitHub Actions (co-op-translator.yml)

## Testinstruktioner

### Test af quiz-applikation
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Test af notebooks
- Der findes ikke noget automatiseret testframework til notebooks
- Manuel validering: Kør alle celler i rækkefølge for at sikre, at der ikke er fejl
- Verificer, at datafiler er tilgængelige, og at output genereres korrekt
- Kontroller, at visualiseringer gengives korrekt

### Test af dokumentation
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Kvalitetskontrol af kode
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Retningslinjer for kodestil

### Python (Jupyter-notebooks)
- Følg PEP 8-stilretningslinjer for Python-kode
- Brug klare variabelnavne, der forklarer de analyserede data
- Inkluder markdown-celler med forklaringer før kodeceller
- Hold kodeceller fokuseret på enkeltstående koncepter eller operationer
- Brug pandas til datamanipulation, matplotlib til visualisering
- Almindeligt importmønster:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Følg Vue.js 2-stilguide og bedste praksis
- ESLint-konfiguration i `quiz-app/package.json`
- Brug Vue single-file-komponenter (.vue-filer)
- Bevar komponentbaseret arkitektur
- Kør `npm run lint` før ændringer committes

### Markdown-dokumentation
- Brug en klar overskriftsstruktur (# ## ### osv.)
- Inkluder kodeblokke med sprogangivelser
- Tilføj alt-tekst til billeder
- Link til relaterede lektioner og ressourcer
- Hold linjelængder rimelige for læsbarhed

### Filorganisering
- Lektionsindhold i nummererede mapper (01-defining-data-science osv.)
- Løsninger i dedikerede `solution/`-undermapper
- Oversættelser spejler engelsk struktur i `translations/`-mappen
- Opbevar datafiler i `data/` eller lektionsspecifikke mapper

## Bygning og udrulning

### Udrulning af quiz-applikation
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Udrulning til Azure Static Web Apps
Quiz-applikationen kan udrulles til Azure Static Web Apps:
1. Opret en Azure Static Web App-ressource
2. Forbind til GitHub-repositoriet
3. Konfigurer build-indstillinger:
   - App-placering: `quiz-app`
   - Output-placering: `dist`
4. GitHub Actions workflow udruller automatisk ved push

### Dokumentationsside
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Repositoriet inkluderer dev-container-konfiguration
- Codespaces opsætter automatisk Python- og Node.js-miljø
- Åbn repositoriet i Codespace via GitHub UI
- Alle afhængigheder installeres automatisk

## Retningslinjer for pull requests

### Før indsendelse
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### PR-titelformat
- Brug klare, beskrivende titler
- Format: `[Komponent] Kort beskrivelse`
- Eksempler:
  - `[Lektion 7] Ret Python-notebook-importfejl`
  - `[Quiz App] Tilføj tysk oversættelse`
  - `[Docs] Opdater README med nye forudsætninger`

### Påkrævede kontroller
- Sørg for, at al kode kører uden fejl
- Verificer, at notebooks udføres fuldstændigt
- Bekræft, at Vue.js-applikationer bygger korrekt
- Kontroller, at dokumentationslinks fungerer
- Test quiz-applikationen, hvis den er ændret
- Verificer, at oversættelser bevarer en ensartet struktur

### Retningslinjer for bidrag
- Følg eksisterende kodestil og mønstre
- Tilføj forklarende kommentarer til kompleks logik
- Opdater relevant dokumentation
- Test ændringer på tværs af forskellige lektionsmoduler, hvis det er relevant
- Gennemgå CONTRIBUTING.md-filen

## Yderligere noter

### Almindeligt anvendte biblioteker
- **pandas**: Datamanipulation og analyse
- **numpy**: Numerisk beregning
- **matplotlib**: Datavisualisering og diagrammer
- **seaborn**: Statistisk datavisualisering (nogle lektioner)
- **scikit-learn**: Maskinlæring (avancerede lektioner)

### Arbejde med datafiler
- Datafiler findes i `data/`-mappen eller lektionsspecifikke mapper
- De fleste notebooks forventer datafiler i relative stier
- CSV-filer er det primære dataformat
- Nogle lektioner bruger JSON til eksempler på ikke-relationelle data

### Flersproget understøttelse
- 40+ sprogoversættelser via automatiserede GitHub Actions
- Oversættelsesworkflow i `.github/workflows/co-op-translator.yml`
- Oversættelser i `translations/`-mappen med sprogkoder
- Quiz-oversættelser i `quiz-app/src/assets/translations/`

### Udviklingsmiljømuligheder
1. **Lokal udvikling**: Installer Python, Jupyter, Node.js lokalt
2. **GitHub Codespaces**: Cloud-baseret øjeblikkeligt udviklingsmiljø
3. **VS Code Dev-containere**: Lokalt containerbaseret udvikling
4. **Binder**: Start notebooks i skyen (hvis konfigureret)

### Retningslinjer for lektionsindhold
- Hver lektion er selvstændig, men bygger på tidligere koncepter
- Quizzer før lektionen tester forudgående viden
- Quizzer efter lektionen styrker læringen
- Opgaver giver praktisk erfaring
- Sketchnotes giver visuelle opsummeringer

### Fejlfinding af almindelige problemer

**Problemer med Jupyter-kernel:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**npm-installationsfejl:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Importfejl i notebooks:**
- Verificer, at alle nødvendige biblioteker er installeret
- Kontroller Python-versionens kompatibilitet (Python 3.7+ anbefales)
- Sørg for, at det virtuelle miljø er aktiveret

**Docsify indlæses ikke:**
- Verificer, at du serverer fra repositoryets rod
- Kontroller, at `index.html` findes
- Sørg for korrekt netværksadgang (port 3000)

### Ydelseshensyn
- Store datasæt kan tage tid at indlæse i notebooks
- Visualiseringer kan være langsomme at gengive for komplekse diagrammer
- Vue.js dev-server muliggør hot-reload for hurtig iteration
- Produktionsbuilds er optimerede og minimerede

### Sikkerhedsnoter
- Ingen følsomme data eller legitimationsoplysninger bør committes
- Brug miljøvariabler til eventuelle API-nøgler i cloud-lektioner
- Azure-relaterede lektioner kan kræve Azure-kontooplysninger
- Hold afhængigheder opdaterede for sikkerhedsrettelser

## Bidrag til oversættelser
- Automatiserede oversættelser håndteres via GitHub Actions
- Manuelle rettelser er velkomne for at sikre oversættelseskvalitet
- Følg eksisterende oversættelsesmappe-struktur
- Opdater quiz-links til at inkludere sprogparameter: `?loc=fr`
- Test oversatte lektioner for korrekt gengivelse

## Relaterede ressourcer
- Hovedpensum: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Diskussionsforum: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Andre Microsoft-pensum: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Projektvedligeholdelse
- Regelmæssige opdateringer for at holde indholdet aktuelt
- Bidrag fra fællesskabet er velkomne
- Issues spores på GitHub
- PR'er gennemgås af pensumvedligeholdere
- Månedlige indholdsrevisioner og opdateringer

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.