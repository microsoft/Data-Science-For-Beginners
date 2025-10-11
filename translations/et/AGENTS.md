<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-11T15:10:42+00:00",
  "source_file": "AGENTS.md",
  "language_code": "et"
}
-->
# AGENTS.md

## Projekti Ülevaade

Andmeteadus algajatele on Microsoft Azure Cloud Advocates'i loodud põhjalik 10-nädalane, 20-õppetunniga õppekava. Repositoorium on õppevahend, mis õpetab projektipõhiste tundide kaudu andmeteaduse põhikontseptsioone, sealhulgas Jupyteri märkmikke, interaktiivseid teste ja praktilisi ülesandeid.

**Peamised tehnoloogiad:**
- **Jupyteri märkmikud**: Peamine õppevahend, kasutades Python 3
- **Python'i teegid**: pandas, numpy, matplotlib andmete analüüsimiseks ja visualiseerimiseks
- **Vue.js 2**: Testirakendus (quiz-app kaust)
- **Docsify**: Dokumentatsiooni saidi generaator võrguühenduseta kasutamiseks
- **Node.js/npm**: JavaScripti komponentide paketihaldus
- **Markdown**: Kõik õppetundide sisu ja dokumentatsioon

**Arhitektuur:**
- Mitmekeelne õppe repositoorium ulatuslike tõlgetega
- Struktureeritud õppetundide mooduliteks (1-Sissejuhatus kuni 6-Andmeteadus-praktikas)
- Iga õppetund sisaldab README-d, märkmikke, ülesandeid ja teste
- Iseseisev Vue.js testirakendus enne/pärast õppetundi hindamiseks
- GitHub Codespaces ja VS Code arenduskonteinerite tugi

## Seadistamise käsud

### Repositooriumi seadistamine
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Python'i keskkonna seadistamine
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Testirakenduse seadistamine
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

### Docsify dokumentatsiooni server
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Visualiseerimisprojektide seadistamine
Näiteks visualiseerimisprojektide jaoks nagu meaningful-visualizations (õppetund 13):
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


## Arenduse töövoog

### Töötamine Jupyteri märkmikega
1. Käivita Jupyter repositooriumi juurikas: `jupyter notebook`
2. Liigu soovitud õppetunni kausta
3. Ava `.ipynb` failid, et harjutusi läbi töötada
4. Märkmikud on iseseisvad, sisaldades selgitusi ja koodirakke
5. Enamik märkmikke kasutab pandas, numpy ja matplotlib - veendu, et need on paigaldatud

### Õppetunni struktuur
Iga õppetund sisaldab tavaliselt:
- `README.md` - Peamine õppetunni sisu teooria ja näidetega
- `notebook.ipynb` - Praktilised Jupyteri märkmiku harjutused
- `assignment.ipynb` või `assignment.md` - Praktilised ülesanded
- `solution/` kaust - Lahenduste märkmikud ja kood
- `images/` kaust - Toetavad visuaalsed materjalid

### Testirakenduse arendus
- Vue.js 2 rakendus kuumlaadimisega arenduse ajal
- Testid salvestatud `quiz-app/src/assets/translations/` kaustas
- Iga keel omab oma tõlkekausta (en, fr, es jne)
- Testide numeratsioon algab 0-st ja ulatub 39-ni (kokku 40 testi)

### Tõlgete lisamine
- Tõlked asuvad repositooriumi juurikas `translations/` kaustas
- Iga keel peegeldab ingliskeelset õppetunni struktuuri
- Automaatne tõlkimine GitHub Actions'i kaudu (co-op-translator.yml)

## Testimise juhised

### Testirakenduse testimine
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Märkmike testimine
- Märkmike jaoks puudub automaatne testiraamistik
- Käsitsi valideerimine: Käivita kõik rakud järjest, et veenduda, et vigu pole
- Kontrolli, et andmefailid oleksid kättesaadavad ja väljundid korrektselt genereeritud
- Veendu, et visualisatsioonid kuvatakse õigesti

### Dokumentatsiooni testimine
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Koodi kvaliteedi kontroll
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Koodistiili juhised

### Python (Jupyteri märkmikud)
- Järgi PEP 8 stiilijuhiseid Python'i koodis
- Kasuta selgeid muutujanimesid, mis selgitavad analüüsitavaid andmeid
- Lisa markdown-rakud selgitustega enne koodirakke
- Hoia koodirakud keskendunud ühele kontseptsioonile või operatsioonile
- Kasuta pandas andmete manipuleerimiseks, matplotlib visualiseerimiseks
- Tavaline importimise muster:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Järgi Vue.js 2 stiilijuhiseid ja parimaid praktikaid
- ESLint konfiguratsioon `quiz-app/package.json` failis
- Kasuta Vue ühefaililisi komponente (.vue failid)
- Säilita komponentidel põhinev arhitektuur
- Käivita `npm run lint` enne muudatuste salvestamist

### Markdown dokumentatsioon
- Kasuta selget pealkirjade hierarhiat (# ## ### jne)
- Lisa koodiplokid keele määratlustega
- Lisa piltidele alt-tekst
- Linki seotud õppetundide ja ressurssidega
- Hoia rea pikkused mõistlikud loetavuse jaoks

### Failide organiseerimine
- Õppetunni sisu nummerdatud kaustades (01-defining-data-science jne)
- Lahendused eraldi `solution/` alamkaustades
- Tõlked peegeldavad ingliskeelset struktuuri `translations/` kaustas
- Andmefailid asuvad `data/` või õppetunnispetsiifilistes kaustades

## Ehitamine ja juurutamine

### Testirakenduse juurutamine
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Azure Static Web Apps juurutamine
Testirakendust saab juurutada Azure Static Web Apps'i:
1. Loo Azure Static Web App ressurss
2. Ühenda GitHubi repositooriumiga
3. Konfigureeri ehituse seaded:
   - Rakenduse asukoht: `quiz-app`
   - Väljundi asukoht: `dist`
4. GitHub Actions töövoog juurutab automaatselt muudatuste korral

### Dokumentatsiooni sait
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Repositoorium sisaldab arenduskonteineri konfiguratsiooni
- Codespaces seadistab automaatselt Python'i ja Node.js keskkonna
- Ava repositoorium Codespaces'is GitHubi UI kaudu
- Kõik sõltuvused paigaldatakse automaatselt

## Pull Request'i juhised

### Enne esitamist
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### PR-i pealkirja formaat
- Kasuta selgeid, kirjeldavaid pealkirju
- Formaat: `[Komponent] Lühike kirjeldus`
- Näited:
  - `[Õppetund 7] Paranda Python'i märkmiku importimise viga`
  - `[Testirakendus] Lisa saksa keele tõlge`
  - `[Dokumentatsioon] Uuenda README uute eeldustega`

### Nõutavad kontrollid
- Veendu, et kogu kood töötab vigadeta
- Kontrolli, et märkmikud täituvad täielikult
- Kinnita, et Vue.js rakendused ehituvad edukalt
- Kontrolli, et dokumentatsiooni lingid töötavad
- Testi testirakendust, kui see on muudetud
- Veendu, et tõlked säilitavad ühtlase struktuuri

### Panustamise juhised
- Järgi olemasolevat koodistiili ja mustreid
- Lisa selgitavad kommentaarid keeruka loogika jaoks
- Uuenda asjakohast dokumentatsiooni
- Testi muudatusi erinevates õppetundide moodulites, kui see on asjakohane
- Vaata üle CONTRIBUTING.md fail

## Täiendavad märkused

### Kasutatavad teegid
- **pandas**: Andmete manipuleerimine ja analüüs
- **numpy**: Numbriline arvutus
- **matplotlib**: Andmete visualiseerimine ja graafikute loomine
- **seaborn**: Statistiline andmete visualiseerimine (mõned õppetunnid)
- **scikit-learn**: Masinõpe (edasijõudnud õppetunnid)

### Töötamine andmefailidega
- Andmefailid asuvad `data/` kaustas või õppetunnispetsiifilistes kataloogides
- Enamik märkmikke eeldab andmefailide olemasolu suhtelistes radades
- CSV-failid on peamine andmeformaat
- Mõned õppetunnid kasutavad JSON-i relatsiooniväliste andmete näideteks

### Mitmekeelne tugi
- 40+ keele tõlked automaatse GitHub Actions'i kaudu
- Tõlkimise töövoog `.github/workflows/co-op-translator.yml` failis
- Tõlked `translations/` kaustas keelekoodidega
- Testide tõlked `quiz-app/src/assets/translations/` kaustas

### Arenduskeskkonna valikud
1. **Kohalik arendus**: Paigalda Python, Jupyter, Node.js kohalikult
2. **GitHub Codespaces**: Pilvepõhine kohene arenduskeskkond
3. **VS Code arenduskonteinerid**: Kohalik konteineripõhine arendus
4. **Binder**: Käivita märkmikud pilves (kui konfigureeritud)

### Õppetunni sisu juhised
- Iga õppetund on iseseisev, kuid tugineb eelnevatele kontseptsioonidele
- Eeltestid kontrollivad eelnevaid teadmisi
- Järgnevad testid tugevdavad õpitut
- Ülesanded pakuvad praktilist harjutamist
- Sketšid pakuvad visuaalseid kokkuvõtteid

### Tavaliste probleemide lahendamine

**Jupyteri tuuma probleemid:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**npm paigaldamise vead:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Importimise vead märkmikes:**
- Kontrolli, et kõik vajalikud teegid on paigaldatud
- Kontrolli Python'i versiooni ühilduvust (soovitatav Python 3.7+)
- Veendu, et virtuaalne keskkond on aktiveeritud

**Docsify ei laadi:**
- Kontrolli, et server töötab repositooriumi juurikas
- Kontrolli, et `index.html` eksisteerib
- Veendu, et võrgule ligipääs on korrektne (port 3000)

### Jõudluse kaalutlused
- Suurte andmekogumite laadimine märkmikes võib võtta aega
- Visualisatsioonide renderdamine võib olla aeglane keerukate graafikute puhul
- Vue.js arenduse server võimaldab kiiret iteratsiooni kuumlaadimisega
- Tootmise ehitused on optimeeritud ja minimeeritud

### Turvanõuded
- Ärge lisage tundlikke andmeid või mandaate
- Kasutage keskkonnamuutujaid API võtmete jaoks pilveõppetundides
- Azure'iga seotud õppetunnid võivad nõuda Azure'i konto mandaate
- Hoidke sõltuvused ajakohased turvaparanduste jaoks

## Panustamine tõlgetesse
- Automaatne tõlkimine hallatud GitHub Actions'i kaudu
- Käsitsi parandused on teretulnud tõlke täpsuse tagamiseks
- Järgi olemasolevat tõlkekaustade struktuuri
- Uuenda testide linke, et lisada keele parameeter: `?loc=fr`
- Testi tõlgitud õppetunde, et veenduda nende korrektsetes kuvamistes

## Seotud ressursid
- Peamine õppekava: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Õpilaste keskus: https://docs.microsoft.com/learn/student-hub
- Arutelufoorum: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Teised Microsofti õppekavad: ML algajatele, AI algajatele, Veebiarendus algajatele

## Projekti hooldus
- Regulaarne uuendamine, et hoida sisu ajakohasena
- Kogukonna panused on teretulnud
- Probleemid jälgitakse GitHubis
- PR-id vaadatakse üle õppekava hooldajate poolt
- Igakuine sisu ülevaatus ja uuendused

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.