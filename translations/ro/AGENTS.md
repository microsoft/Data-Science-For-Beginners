<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:39:12+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ro"
}
-->
# AGENTS.md

## Prezentare Generală a Proiectului

Data Science for Beginners este un curriculum cuprinzător de 10 săptămâni și 20 de lecții, creat de Microsoft Azure Cloud Advocates. Repozitoriul este o resursă educațională care predă concepte fundamentale de știința datelor prin lecții bazate pe proiecte, incluzând notebook-uri Jupyter, chestionare interactive și teme practice.

**Tehnologii Cheie:**
- **Jupyter Notebooks**: Principalul mediu de învățare utilizând Python 3
- **Biblioteci Python**: pandas, numpy, matplotlib pentru analiză și vizualizare de date
- **Vue.js 2**: Aplicație de chestionare (folderul quiz-app)
- **Docsify**: Generator de site-uri de documentație pentru acces offline
- **Node.js/npm**: Gestionarea pachetelor pentru componente JavaScript
- **Markdown**: Tot conținutul lecțiilor și documentația

**Arhitectură:**
- Repozitoriu educațional multilingv cu traduceri extinse
- Structurat în module de lecții (1-Introducere până la 6-Știința-Datelor-În-Lumea-Reală)
- Fiecare lecție include README, notebook-uri, teme și chestionare
- Aplicație de chestionare Vue.js independentă pentru evaluări pre/post-lecție
- Suport pentru GitHub Codespaces și containere de dezvoltare VS Code

## Comenzi de Configurare

### Configurarea Repozitoriului
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Configurarea Mediului Python
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Configurarea Aplicației de Chestionare
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

### Serverul de Documentație Docsify
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Configurarea Proiectelor de Vizualizare
Pentru proiecte de vizualizare precum meaningful-visualizations (lecția 13):
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


## Flux de Lucru în Dezvoltare

### Lucrul cu Jupyter Notebooks
1. Porniți Jupyter din rădăcina repo-ului: `jupyter notebook`
2. Navigați la folderul lecției dorite
3. Deschideți fișierele `.ipynb` pentru a lucra la exerciții
4. Notebook-urile sunt autonome, cu explicații și celule de cod
5. Majoritatea notebook-urilor folosesc pandas, numpy și matplotlib - asigurați-vă că acestea sunt instalate

### Structura Lecțiilor
Fiecare lecție conține, de obicei:
- `README.md` - Conținutul principal al lecției cu teorie și exemple
- `notebook.ipynb` - Exerciții practice în Jupyter notebook
- `assignment.ipynb` sau `assignment.md` - Teme practice
- Folderul `solution/` - Notebook-uri și coduri de soluții
- Folderul `images/` - Materiale vizuale suport

### Dezvoltarea Aplicației de Chestionare
- Aplicație Vue.js 2 cu reîncărcare automată în timpul dezvoltării
- Chestionarele sunt stocate în `quiz-app/src/assets/translations/`
- Fiecare limbă are propriul folder de traduceri (en, fr, es etc.)
- Numerotarea chestionarelor începe de la 0 și ajunge până la 39 (40 chestionare în total)

### Adăugarea Traducerilor
- Traducerile se află în folderul `translations/` din rădăcina repo-ului
- Fiecare limbă are o structură completă a lecțiilor, oglindită din engleză
- Traducere automată prin GitHub Actions (co-op-translator.yml)

## Instrucțiuni de Testare

### Testarea Aplicației de Chestionare
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Testarea Notebook-urilor
- Nu există un cadru de testare automat pentru notebook-uri
- Validare manuală: Rulați toate celulele în ordine pentru a vă asigura că nu există erori
- Verificați accesibilitatea fișierelor de date și generarea corectă a rezultatelor
- Asigurați-vă că vizualizările se redau corect

### Testarea Documentației
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Verificări de Calitate a Codului
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Ghiduri de Stil pentru Cod

### Python (Jupyter Notebooks)
- Respectați ghidurile de stil PEP 8 pentru codul Python
- Folosiți nume de variabile clare care explică datele analizate
- Includeți celule markdown cu explicații înainte de celulele de cod
- Păstrați celulele de cod concentrate pe concepte sau operațiuni unice
- Utilizați pandas pentru manipularea datelor, matplotlib pentru vizualizare
- Model comun de import:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Respectați ghidul de stil Vue.js 2 și cele mai bune practici
- Configurația ESLint în `quiz-app/package.json`
- Utilizați componente Vue single-file (.vue)
- Mențineți o arhitectură bazată pe componente
- Rulați `npm run lint` înainte de a trimite modificări

### Documentație Markdown
- Utilizați o ierarhie clară a titlurilor (# ## ### etc.)
- Includeți blocuri de cod cu specificatori de limbă
- Adăugați text alternativ pentru imagini
- Link către lecții și resurse conexe
- Păstrați lungimea liniilor rezonabilă pentru lizibilitate

### Organizarea Fișierelor
- Conținutul lecțiilor în foldere numerotate (01-defining-data-science etc.)
- Soluțiile în subfoldere dedicate `solution/`
- Traducerile oglindesc structura engleză în folderul `translations/`
- Păstrați fișierele de date în `data/` sau foldere specifice lecțiilor

## Construire și Implementare

### Implementarea Aplicației de Chestionare
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Implementarea Azure Static Web Apps
Aplicația quiz-app poate fi implementată pe Azure Static Web Apps:
1. Creați o resursă Azure Static Web App
2. Conectați-vă la repo-ul GitHub
3. Configurați setările de construire:
   - Locația aplicației: `quiz-app`
   - Locația output-ului: `dist`
4. Workflow-ul GitHub Actions va implementa automat la fiecare push

### Site-ul de Documentație
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Repozitoriul include configurația containerului de dezvoltare
- Codespaces configurează automat mediul Python și Node.js
- Deschideți repo-ul în Codespace prin UI-ul GitHub
- Toate dependențele se instalează automat

## Ghiduri pentru Pull Request-uri

### Înainte de Trimitere
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Formatul Titlului PR
- Utilizați titluri clare și descriptive
- Format: `[Componentă] Descriere scurtă`
- Exemple:
  - `[Lecția 7] Rezolvă eroarea de import în notebook-ul Python`
  - `[Aplicația de Chestionare] Adaugă traducerea în germană`
  - `[Documentație] Actualizează README cu noi cerințe preliminare`

### Verificări Necesare
- Asigurați-vă că tot codul rulează fără erori
- Verificați execuția completă a notebook-urilor
- Confirmați construirea cu succes a aplicațiilor Vue.js
- Verificați funcționarea link-urilor din documentație
- Testați aplicația de chestionare dacă a fost modificată
- Verificați că traducerile mențin o structură consistentă

### Ghiduri de Contribuție
- Respectați stilul și modelele de cod existente
- Adăugați comentarii explicative pentru logica complexă
- Actualizați documentația relevantă
- Testați modificările în diferite module de lecții, dacă este cazul
- Consultați fișierul CONTRIBUTING.md

## Note Suplimentare

### Biblioteci Comune Utilizate
- **pandas**: Manipularea și analiza datelor
- **numpy**: Calcul numeric
- **matplotlib**: Vizualizare și graficare de date
- **seaborn**: Vizualizare statistică a datelor (unele lecții)
- **scikit-learn**: Învățare automată (lecții avansate)

### Lucrul cu Fișiere de Date
- Fișierele de date se află în folderul `data/` sau în directoare specifice lecțiilor
- Majoritatea notebook-urilor se așteaptă ca fișierele de date să fie în căi relative
- Fișierele CSV sunt formatul principal de date
- Unele lecții folosesc JSON pentru exemple de date nerelaționale

### Suport Multilingv
- Peste 40 de traduceri lingvistice prin GitHub Actions automate
- Workflow-ul de traducere în `.github/workflows/co-op-translator.yml`
- Traducerile în folderul `translations/` cu coduri de limbă
- Traducerile chestionarelor în `quiz-app/src/assets/translations/`

### Opțiuni de Mediu de Dezvoltare
1. **Dezvoltare Locală**: Instalați Python, Jupyter, Node.js local
2. **GitHub Codespaces**: Mediu de dezvoltare instant în cloud
3. **Containere Dev VS Code**: Dezvoltare locală bazată pe containere
4. **Binder**: Lansați notebook-uri în cloud (dacă este configurat)

### Ghiduri pentru Conținutul Lecțiilor
- Fiecare lecție este autonomă, dar se bazează pe conceptele anterioare
- Chestionarele pre-lecție testează cunoștințele anterioare
- Chestionarele post-lecție consolidează învățarea
- Temele oferă practică hands-on
- Sketchnotes oferă rezumate vizuale

### Rezolvarea Problemelor Comune

**Probleme cu Kernel-ul Jupyter:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Eșecuri la Instalarea npm:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Erori de Import în Notebook-uri:**
- Verificați instalarea tuturor bibliotecilor necesare
- Verificați compatibilitatea versiunii Python (recomandat Python 3.7+)
- Asigurați-vă că mediul virtual este activat

**Docsify Nu Se Încarcă:**
- Verificați că serviți din rădăcina repo-ului
- Asigurați-vă că `index.html` există
- Verificați accesul corect la rețea (portul 3000)

### Considerații de Performanță
- Seturile mari de date pot necesita timp pentru încărcare în notebook-uri
- Redarea vizualizărilor poate fi lentă pentru grafice complexe
- Serverul de dezvoltare Vue.js permite reîncărcare rapidă pentru iterații rapide
- Build-urile de producție sunt optimizate și minificate

### Note de Securitate
- Nu trebuie să se comită date sensibile sau credențiale
- Utilizați variabile de mediu pentru orice chei API în lecțiile cloud
- Lecțiile legate de Azure pot necesita credențiale de cont Azure
- Mențineți dependențele actualizate pentru patch-uri de securitate

## Contribuția la Traduceri
- Traducerile automate sunt gestionate prin GitHub Actions
- Corecțiile manuale sunt binevenite pentru acuratețea traducerilor
- Respectați structura folderului de traduceri existentă
- Actualizați link-urile chestionarelor pentru a include parametrul de limbă: `?loc=fr`
- Testați lecțiile traduse pentru redarea corectă

## Resurse Conexe
- Curriculum principal: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Forum de Discuții: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Alte curriculum-uri Microsoft: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Întreținerea Proiectului
- Actualizări regulate pentru a menține conținutul actual
- Contribuțiile comunității sunt binevenite
- Problemele sunt urmărite pe GitHub
- PR-urile sunt revizuite de către mentenorii curriculum-ului
- Revizuiri și actualizări lunare ale conținutului

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.