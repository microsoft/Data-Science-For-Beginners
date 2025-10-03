<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:46:40+00:00",
  "source_file": "AGENTS.md",
  "language_code": "lt"
}
-->
# AGENTS.md

## Projekto apžvalga

„Data Science for Beginners“ yra išsamus 10 savaičių, 20 pamokų mokymo planas, sukurtas „Microsoft Azure Cloud Advocates“. Šis saugykla yra mokymosi šaltinis, kuris moko pagrindinių duomenų mokslo koncepcijų per projektines pamokas, įskaitant Jupyter užrašų knygeles, interaktyvius testus ir praktines užduotis.

**Pagrindinės technologijos:**
- **Jupyter užrašų knygelės**: Pagrindinė mokymosi priemonė naudojant Python 3
- **Python bibliotekos**: pandas, numpy, matplotlib duomenų analizei ir vizualizacijai
- **Vue.js 2**: Testų programa (quiz-app aplankas)
- **Docsify**: Dokumentacijos svetainės generatorius neprisijungus
- **Node.js/npm**: Paketų valdymas JavaScript komponentams
- **Markdown**: Visas pamokų turinys ir dokumentacija

**Architektūra:**
- Daugiakalbė mokomoji saugykla su plačiomis vertimais
- Struktūrizuota į pamokų modulius (nuo 1-Introduction iki 6-Data-Science-In-Wild)
- Kiekviena pamoka apima README, užrašų knygeles, užduotis ir testus
- Savarankiška Vue.js testų programa prieš/pamokos vertinimui
- GitHub Codespaces ir VS Code dev konteinerių palaikymas

## Nustatymo komandos

### Saugyklos nustatymas
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Python aplinkos nustatymas
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Testų programos nustatymas
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

### Docsify dokumentacijos serveris
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Vizualizacijos projektų nustatymas
Vizualizacijos projektams, pvz., meaningful-visualizations (13 pamoka):
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


## Vystymo darbo eiga

### Darbas su Jupyter užrašų knygelėmis
1. Paleiskite Jupyter saugyklos šaknyje: `jupyter notebook`
2. Naršykite į norimą pamokos aplanką
3. Atidarykite `.ipynb` failus, kad atliktumėte pratimus
4. Užrašų knygelės yra savarankiškos su paaiškinimais ir kodų langeliais
5. Dauguma užrašų knygelių naudoja pandas, numpy ir matplotlib - įsitikinkite, kad jos įdiegtos

### Pamokos struktūra
Kiekviena pamoka paprastai apima:
- `README.md` - Pagrindinis pamokos turinys su teorija ir pavyzdžiais
- `notebook.ipynb` - Praktiniai Jupyter užrašų knygelės pratimai
- `assignment.ipynb` arba `assignment.md` - Praktinės užduotys
- `solution/` aplankas - Sprendimų užrašų knygelės ir kodas
- `images/` aplankas - Palaikomos vizualinės medžiagos

### Testų programos kūrimas
- Vue.js 2 programa su karštu perkrovimu vystymo metu
- Testai saugomi `quiz-app/src/assets/translations/`
- Kiekviena kalba turi savo vertimų aplanką (en, fr, es ir kt.)
- Testų numeracija prasideda nuo 0 ir tęsiasi iki 39 (iš viso 40 testų)

### Vertimų pridėjimas
- Vertimai dedami į `translations/` aplanką saugyklos šaknyje
- Kiekviena kalba turi pilną pamokų struktūrą, atspindinčią anglų kalbą
- Automatinis vertimas per GitHub Actions (co-op-translator.yml)

## Testavimo instrukcijos

### Testų programos testavimas
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Užrašų knygelių testavimas
- Automatinės testavimo sistemos užrašų knygelėms nėra
- Rankinis patikrinimas: Paleiskite visus langelius iš eilės, kad įsitikintumėte, jog nėra klaidų
- Patikrinkite, ar duomenų failai yra pasiekiami ir ar rezultatai generuojami teisingai
- Įsitikinkite, kad vizualizacijos tinkamai rodomos

### Dokumentacijos testavimas
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Kodo kokybės patikrinimai
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Kodo stiliaus gairės

### Python (Jupyter užrašų knygelės)
- Laikykitės PEP 8 stiliaus gairių Python kodui
- Naudokite aiškius kintamųjų pavadinimus, kurie paaiškina analizuojamus duomenis
- Prieš kodų langelius įtraukite markdown langelius su paaiškinimais
- Kodų langelius laikykite sutelktus į vieną koncepciją ar operaciją
- Naudokite pandas duomenų manipuliacijai, matplotlib vizualizacijai
- Įprastas importavimo modelis:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Laikykitės Vue.js 2 stiliaus gairių ir geriausių praktikų
- ESLint konfigūracija `quiz-app/package.json`
- Naudokite Vue vieno failo komponentus (.vue failai)
- Išlaikykite komponentų pagrįstą architektūrą
- Prieš įsipareigojimus paleiskite `npm run lint`

### Markdown dokumentacija
- Naudokite aiškią antraščių hierarchiją (# ## ### ir kt.)
- Įtraukite kodų blokus su kalbos specifikatoriais
- Pridėkite alternatyvų tekstą vaizdams
- Nuorodos į susijusias pamokas ir išteklius
- Išlaikykite tinkamą eilučių ilgį, kad būtų lengviau skaityti

### Failų organizavimas
- Pamokų turinys numeruotuose aplankuose (01-defining-data-science ir kt.)
- Sprendimai dedami į atskirus `solution/` aplankus
- Vertimai atspindi anglų struktūrą `translations/` aplanke
- Duomenų failai laikomi `data/` arba pamokai skirtuose aplankuose

## Kūrimas ir diegimas

### Testų programos diegimas
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Azure Static Web Apps diegimas
Testų programa gali būti diegiama į Azure Static Web Apps:
1. Sukurkite Azure Static Web App resursą
2. Prisijunkite prie GitHub saugyklos
3. Konfigūruokite kūrimo nustatymus:
   - Programos vieta: `quiz-app`
   - Išvesties vieta: `dist`
4. GitHub Actions darbo eiga automatiškai diegs po pakeitimų

### Dokumentacijos svetainė
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Saugykla apima dev konteinerio konfigūraciją
- Codespaces automatiškai nustato Python ir Node.js aplinką
- Atidarykite saugyklą Codespace per GitHub UI
- Visos priklausomybės įdiegiamos automatiškai

## Pull Request gairės

### Prieš pateikimą
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### PR pavadinimo formatas
- Naudokite aiškius, aprašomuosius pavadinimus
- Formatavimas: `[Komponentas] Trumpas aprašymas`
- Pavyzdžiai:
  - `[Pamoka 7] Ištaisykite Python užrašų knygelės importavimo klaidą`
  - `[Testų programa] Pridėkite vokiečių kalbos vertimą`
  - `[Dokumentai] Atnaujinkite README su naujais reikalavimais`

### Reikalingi patikrinimai
- Įsitikinkite, kad visas kodas veikia be klaidų
- Patikrinkite, ar užrašų knygelės vykdomos visiškai
- Patvirtinkite, kad Vue.js programos sėkmingai kuriamos
- Patikrinkite, ar dokumentacijos nuorodos veikia
- Testuokite testų programą, jei ji buvo pakeista
- Patikrinkite, ar vertimai išlaiko nuoseklią struktūrą

### Prisidėjimo gairės
- Laikykitės esamo kodo stiliaus ir modelių
- Pridėkite paaiškinamuosius komentarus sudėtingai logikai
- Atnaujinkite susijusią dokumentaciją
- Testuokite pakeitimus skirtinguose pamokų moduliuose, jei taikoma
- Peržiūrėkite CONTRIBUTING.md failą

## Papildomos pastabos

### Naudojamos bibliotekos
- **pandas**: Duomenų manipuliacija ir analizė
- **numpy**: Skaitmeninis skaičiavimas
- **matplotlib**: Duomenų vizualizacija ir grafikai
- **seaborn**: Statistinė duomenų vizualizacija (kai kurios pamokos)
- **scikit-learn**: Mašininis mokymasis (pažangios pamokos)

### Darbas su duomenų failais
- Duomenų failai yra `data/` aplanke arba pamokai skirtuose kataloguose
- Dauguma užrašų knygelių tikisi duomenų failų santykiniais keliais
- CSV failai yra pagrindinis duomenų formatas
- Kai kurios pamokos naudoja JSON nestruktūrizuotų duomenų pavyzdžiams

### Daugiakalbė parama
- 40+ kalbų vertimai per automatizuotus GitHub Actions
- Vertimo darbo eiga `.github/workflows/co-op-translator.yml`
- Vertimai `translations/` aplanke su kalbos kodais
- Testų vertimai `quiz-app/src/assets/translations/`

### Vystymo aplinkos pasirinkimai
1. **Vietinis vystymas**: Įdiekite Python, Jupyter, Node.js vietoje
2. **GitHub Codespaces**: Debesų pagrindu veikianti momentinė vystymo aplinka
3. **VS Code Dev Containers**: Vietinė konteinerių pagrindu veikianti aplinka
4. **Binder**: Paleiskite užrašų knygeles debesyje (jei sukonfigūruota)

### Pamokų turinio gairės
- Kiekviena pamoka yra savarankiška, bet remiasi ankstesnėmis koncepcijomis
- Prieš pamoką testai tikrina ankstesnes žinias
- Po pamokos testai stiprina mokymąsi
- Užduotys suteikia praktinę patirtį
- Sketchnotes pateikia vizualines santraukas

### Dažniausiai pasitaikančių problemų sprendimas

**Jupyter branduolio problemos:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**npm diegimo klaidos:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Importavimo klaidos užrašų knygelėse:**
- Patikrinkite, ar visos reikalingos bibliotekos yra įdiegtos
- Patikrinkite Python versijos suderinamumą (rekomenduojama Python 3.7+)
- Įsitikinkite, kad virtuali aplinka yra aktyvuota

**Docsify neveikia:**
- Patikrinkite, ar serveris paleistas iš saugyklos šaknies
- Patikrinkite, ar egzistuoja `index.html`
- Įsitikinkite tinkamu tinklo prieinamumu (3000 prievadas)

### Našumo apsvarstymai
- Dideli duomenų rinkiniai gali užtrukti, kol bus įkelti užrašų knygelėse
- Vizualizacijos generavimas gali būti lėtas sudėtingiems grafams
- Vue.js vystymo serveris leidžia greitą iteraciją su karštu perkrovimu
- Produkcijos kūrimai yra optimizuoti ir minimizuoti

### Saugumo pastabos
- Jokių jautrių duomenų ar kredencialų neturėtų būti įsipareigojama
- Naudokite aplinkos kintamuosius bet kokiems API raktams debesų pamokose
- Pamokos, susijusios su Azure, gali reikalauti Azure paskyros kredencialų
- Laikykite priklausomybes atnaujintas dėl saugumo pataisų

## Prisidėjimas prie vertimų
- Automatiniai vertimai valdomi per GitHub Actions
- Rankiniai pataisymai laukiami dėl vertimo tikslumo
- Laikykitės esamos vertimų aplankų struktūros
- Atnaujinkite testų nuorodas, kad įtrauktumėte kalbos parametrą: `?loc=fr`
- Testuokite išverstus pamokas, kad įsitikintumėte tinkamu rodymu

## Susiję ištekliai
- Pagrindinis mokymo planas: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Studentų centras: https://docs.microsoft.com/learn/student-hub
- Diskusijų forumas: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Kiti Microsoft mokymo planai: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Projekto priežiūra
- Reguliarūs atnaujinimai, kad turinys būtų aktualus
- Bendruomenės indėlis laukiami
- Problemos stebimos GitHub
- PR peržiūrimi mokymo plano prižiūrėtojų
- Mėnesiniai turinio peržiūros ir atnaujinimai

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingą interpretaciją, atsiradusią dėl šio vertimo naudojimo.