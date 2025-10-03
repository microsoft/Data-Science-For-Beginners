<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:43:35+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sl"
}
-->
# AGENTS.md

## Pregled projekta

Data Science for Beginners je obsežen 10-tedenski, 20-lekcijski učni načrt, ki ga je ustvarila ekipa Microsoft Azure Cloud Advocates. Repozitorij je učni vir, ki poučuje osnovne koncepte podatkovne znanosti skozi lekcije, ki temeljijo na projektih, vključno z Jupyter zvezki, interaktivnimi kvizi in praktičnimi nalogami.

**Ključne tehnologije:**
- **Jupyter zvezki**: Glavno učno sredstvo z uporabo Python 3
- **Python knjižnice**: pandas, numpy, matplotlib za analizo podatkov in vizualizacijo
- **Vue.js 2**: Aplikacija za kvize (mapa quiz-app)
- **Docsify**: Generator dokumentacijskih strani za dostop brez povezave
- **Node.js/npm**: Upravljanje paketov za JavaScript komponente
- **Markdown**: Vsa vsebina lekcij in dokumentacija

**Arhitektura:**
- Večjezični izobraževalni repozitorij z obsežnimi prevodi
- Strukturiran v module lekcij (1-Uvod do 6-Podatkovna znanost v praksi)
- Vsaka lekcija vključuje README, zvezke, naloge in kvize
- Samostojna aplikacija za kvize Vue.js za ocenjevanje pred/po lekciji
- Podpora za GitHub Codespaces in VS Code razvojne vsebnike

## Ukazi za nastavitev

### Nastavitev repozitorija
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Nastavitev Python okolja
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Nastavitev aplikacije za kvize
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

### Docsify strežnik za dokumentacijo
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Nastavitev projektov za vizualizacijo
Za projekte vizualizacije, kot je meaningful-visualizations (lekcija 13):
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


## Razvojni potek dela

### Delo z Jupyter zvezki
1. Zaženite Jupyter v korenu repozitorija: `jupyter notebook`
2. Pomaknite se do želene mape lekcije
3. Odprite `.ipynb` datoteke za delo z vajami
4. Zvezki so samostojni z razlagami in kodnimi celicami
5. Večina zvezkov uporablja pandas, numpy in matplotlib - preverite, da so nameščeni

### Struktura lekcije
Vsaka lekcija običajno vsebuje:
- `README.md` - Glavna vsebina lekcije s teorijo in primeri
- `notebook.ipynb` - Praktične vaje v Jupyter zvezku
- `assignment.ipynb` ali `assignment.md` - Praktične naloge
- `solution/` mapa - Zvezki z rešitvami in koda
- `images/` mapa - Podporni vizualni materiali

### Razvoj aplikacije za kvize
- Aplikacija Vue.js 2 z možnostjo hitrega osveževanja med razvojem
- Kvizi so shranjeni v `quiz-app/src/assets/translations/`
- Vsak jezik ima svojo mapo za prevode (en, fr, es itd.)
- Številčenje kvizov se začne pri 0 in gre do 39 (skupaj 40 kvizov)

### Dodajanje prevodov
- Prevodi se nahajajo v mapi `translations/` v korenu repozitorija
- Vsak jezik ima popolno strukturo lekcij, ki zrcali angleško
- Avtomatizirani prevodi prek GitHub Actions (co-op-translator.yml)

## Navodila za testiranje

### Testiranje aplikacije za kvize
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Testiranje zvezkov
- Za zvezke ne obstaja avtomatiziran testni okvir
- Ročna validacija: Zaženite vse celice zaporedoma, da preverite, da ni napak
- Preverite dostopnost datotek s podatki in pravilno generiranje izhodov
- Preverite, da se vizualizacije pravilno prikažejo

### Testiranje dokumentacije
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Preverjanje kakovosti kode
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Smernice za slog kode

### Python (Jupyter zvezki)
- Upoštevajte smernice sloga PEP 8 za Python kodo
- Uporabljajte jasna imena spremenljivk, ki pojasnjujejo analizirane podatke
- Dodajte markdown celice z razlagami pred kodnimi celicami
- Kodne celice naj se osredotočajo na posamezne koncepte ali operacije
- Uporabljajte pandas za manipulacijo podatkov, matplotlib za vizualizacijo
- Pogost vzorec uvoza:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Upoštevajte smernice sloga Vue.js 2 in najboljše prakse
- ESLint konfiguracija v `quiz-app/package.json`
- Uporabljajte Vue datoteke z enim komponentom (.vue datoteke)
- Ohranjajte arhitekturo, ki temelji na komponentah
- Pred oddajo sprememb zaženite `npm run lint`

### Markdown dokumentacija
- Uporabljajte jasno hierarhijo naslovov (# ## ### itd.)
- Dodajte kodne bloke z določenimi jeziki
- Dodajte alt besedilo za slike
- Povezujte na sorodne lekcije in vire
- Ohranjajte razumne dolžine vrstic za berljivost

### Organizacija datotek
- Vsebina lekcij v oštevilčenih mapah (01-defining-data-science itd.)
- Rešitve v namenskih podmapah `solution/`
- Prevodi zrcalijo angleško strukturo v mapi `translations/`
- Datoteke s podatki v mapi `data/` ali specifičnih mapah lekcij

## Gradnja in uvajanje

### Uvajanje aplikacije za kvize
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Uvajanje Azure Static Web Apps
Aplikacijo za kvize lahko uvedete v Azure Static Web Apps:
1. Ustvarite vir Azure Static Web App
2. Povežite se z GitHub repozitorijem
3. Konfigurirajte nastavitve gradnje:
   - Lokacija aplikacije: `quiz-app`
   - Lokacija izhoda: `dist`
4. GitHub Actions delovni tok bo samodejno uvedel ob potisku

### Spletno mesto dokumentacije
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Repozitorij vključuje konfiguracijo razvojnega vsebnika
- Codespaces samodejno nastavi Python in Node.js okolje
- Odprite repozitorij v Codespace prek GitHub UI
- Vse odvisnosti se samodejno namestijo

## Smernice za zahteve za združitev

### Pred oddajo
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Format naslova PR
- Uporabljajte jasne, opisne naslove
- Format: `[Komponenta] Kratek opis`
- Primeri:
  - `[Lekcija 7] Popravi napako pri uvozu Python zvezka`
  - `[Aplikacija za kvize] Dodaj nemški prevod`
  - `[Dokumentacija] Posodobi README z novimi predpogoji`

### Zahtevani pregledi
- Preverite, da vsa koda deluje brez napak
- Preverite, da se zvezki popolnoma izvedejo
- Potrdite, da se aplikacije Vue.js uspešno gradijo
- Preverite, da povezave v dokumentaciji delujejo
- Testirajte aplikacijo za kvize, če je bila spremenjena
- Preverite, da prevodi ohranjajo dosledno strukturo

### Smernice za prispevanje
- Upoštevajte obstoječi slog kode in vzorce
- Dodajte razlagalne komentarje za kompleksno logiko
- Posodobite ustrezno dokumentacijo
- Testirajte spremembe v različnih modulih lekcij, če je primerno
- Preglejte datoteko CONTRIBUTING.md

## Dodatne opombe

### Pogosto uporabljene knjižnice
- **pandas**: Manipulacija in analiza podatkov
- **numpy**: Numerično računanje
- **matplotlib**: Vizualizacija in risanje podatkov
- **seaborn**: Statistična vizualizacija podatkov (nekatere lekcije)
- **scikit-learn**: Strojno učenje (napredne lekcije)

### Delo z datotekami s podatki
- Datoteke s podatki se nahajajo v mapi `data/` ali specifičnih mapah lekcij
- Večina zvezkov pričakuje datoteke s podatki v relativnih poteh
- CSV datoteke so primarni format podatkov
- Nekatere lekcije uporabljajo JSON za primere nerelacijskih podatkov

### Večjezična podpora
- 40+ jezikovnih prevodov prek avtomatiziranih GitHub Actions
- Delovni tok prevodov v `.github/workflows/co-op-translator.yml`
- Prevodi v mapi `translations/` z jezikovnimi kodami
- Prevodi kvizov v `quiz-app/src/assets/translations/`

### Možnosti razvojnega okolja
1. **Lokalni razvoj**: Namestite Python, Jupyter, Node.js lokalno
2. **GitHub Codespaces**: Oblakovno takojšnje razvojno okolje
3. **VS Code razvojni vsebniki**: Lokalni razvoj na osnovi vsebnikov
4. **Binder**: Zaženite zvezke v oblaku (če je konfigurirano)

### Smernice za vsebino lekcij
- Vsaka lekcija je samostojna, vendar gradi na prejšnjih konceptih
- Kvizi pred lekcijo preverjajo predhodno znanje
- Kvizi po lekciji krepijo učenje
- Naloge omogočajo praktično vadbo
- Sketchnotes zagotavljajo vizualne povzetke

### Reševanje pogostih težav

**Težave z Jupyter jedrom:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Napake pri namestitvi npm:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Napake pri uvozu v zvezkih:**
- Preverite, da so nameščene vse zahtevane knjižnice
- Preverite združljivost različice Python (priporočeno Python 3.7+)
- Prepričajte se, da je virtualno okolje aktivirano

**Docsify se ne nalaga:**
- Preverite, da strežnik deluje iz korena repozitorija
- Preverite, da obstaja `index.html`
- Preverite pravilno omrežno povezavo (port 3000)

### Premisleki o zmogljivosti
- Veliki nabori podatkov lahko trajajo dlje časa za nalaganje v zvezkih
- Prikaz vizualizacij je lahko počasen za kompleksne grafe
- Vue.js razvojni strežnik omogoča hitro osveževanje za hitro iteracijo
- Proizvodne gradnje so optimizirane in minimizirane

### Opombe o varnosti
- Nobeni občutljivi podatki ali poverilnice ne smejo biti vključeni
- Uporabljajte okoljske spremenljivke za vse API ključe v lekcijah v oblaku
- Lekcije, povezane z Azure, lahko zahtevajo poverilnice za Azure račun
- Posodabljajte odvisnosti za varnostne popravke

## Prispevanje k prevodom
- Avtomatizirani prevodi upravljani prek GitHub Actions
- Ročne popravke so dobrodošle za natančnost prevodov
- Upoštevajte obstoječo strukturo map za prevode
- Posodobite povezave kvizov, da vključujejo jezikovni parameter: `?loc=fr`
- Testirajte prevedene lekcije za pravilno prikazovanje

## Sorodni viri
- Glavni učni načrt: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Forum za razprave: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Drugi Microsoft učni načrti: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Vzdrževanje projekta
- Redne posodobitve za ohranjanje aktualnosti vsebine
- Prispevki skupnosti so dobrodošli
- Težave se spremljajo na GitHubu
- PR-ji pregledani s strani vzdrževalcev učnega načrta
- Mesečni pregledi in posodobitve vsebine

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.