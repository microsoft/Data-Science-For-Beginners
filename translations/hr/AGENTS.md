<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:42:38+00:00",
  "source_file": "AGENTS.md",
  "language_code": "hr"
}
-->
# AGENTS.md

## Pregled projekta

Data Science for Beginners je sveobuhvatan 10-tjedni, 20-lekcijski kurikulum koji su kreirali Microsoft Azure Cloud Advocates. Repozitorij je edukativni resurs koji podučava osnovne koncepte podatkovne znanosti kroz lekcije temeljene na projektima, uključujući Jupyter bilježnice, interaktivne kvizove i praktične zadatke.

**Ključne tehnologije:**
- **Jupyter bilježnice**: Glavni medij za učenje koristeći Python 3
- **Python biblioteke**: pandas, numpy, matplotlib za analizu podataka i vizualizaciju
- **Vue.js 2**: Aplikacija za kvizove (mapa quiz-app)
- **Docsify**: Generator dokumentacijskih stranica za offline pristup
- **Node.js/npm**: Upravljanje paketima za JavaScript komponente
- **Markdown**: Sav sadržaj lekcija i dokumentacija

**Arhitektura:**
- Edukativni repozitorij na više jezika s opsežnim prijevodima
- Strukturiran u module lekcija (1-Uvod do 6-Podatkovna-Znanost-U-Praksi)
- Svaka lekcija uključuje README, bilježnice, zadatke i kvizove
- Samostalna Vue.js aplikacija za kvizove za procjenu prije/poslije lekcije
- Podrška za GitHub Codespaces i VS Code razvojne kontejnere

## Postavljanje repozitorija

### Postavljanje repozitorija
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Postavljanje Python okruženja
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Postavljanje aplikacije za kvizove
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

### Docsify dokumentacijski server
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Postavljanje projekata za vizualizaciju
Za projekte vizualizacije poput meaningful-visualizations (lekcija 13):
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


## Radni tijek razvoja

### Rad s Jupyter bilježnicama
1. Pokrenite Jupyter u korijenu repozitorija: `jupyter notebook`
2. Navigirajte do željene mape lekcije
3. Otvorite `.ipynb` datoteke za rad na vježbama
4. Bilježnice su samostalne s objašnjenjima i kodnim ćelijama
5. Većina bilježnica koristi pandas, numpy i matplotlib - osigurajte da su instalirani

### Struktura lekcije
Svaka lekcija obično sadrži:
- `README.md` - Glavni sadržaj lekcije s teorijom i primjerima
- `notebook.ipynb` - Praktične vježbe u Jupyter bilježnici
- `assignment.ipynb` ili `assignment.md` - Praktični zadaci
- `solution/` mapa - Bilježnice s rješenjima i kod
- `images/` mapa - Vizualni materijali za podršku

### Razvoj aplikacije za kvizove
- Vue.js 2 aplikacija s hot-reload funkcijom tijekom razvoja
- Kvizovi se nalaze u `quiz-app/src/assets/translations/`
- Svaki jezik ima vlastitu mapu za prijevode (en, fr, es, itd.)
- Numeracija kvizova počinje od 0 i ide do 39 (ukupno 40 kvizova)

### Dodavanje prijevoda
- Prijevodi se nalaze u mapi `translations/` u korijenu repozitorija
- Svaki jezik ima potpunu strukturu lekcija preslikanu iz engleskog
- Automatski prijevod putem GitHub Actions (co-op-translator.yml)

## Upute za testiranje

### Testiranje aplikacije za kvizove
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Testiranje bilježnica
- Ne postoji automatizirani okvir za testiranje bilježnica
- Ručna validacija: Pokrenite sve ćelije redom kako biste osigurali da nema grešaka
- Provjerite dostupnost datoteka s podacima i generiranje izlaza
- Provjerite ispravnost prikaza vizualizacija

### Testiranje dokumentacije
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Provjere kvalitete koda
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Smjernice za stil koda

### Python (Jupyter bilježnice)
- Slijedite PEP 8 smjernice za stil Python koda
- Koristite jasne nazive varijabli koje objašnjavaju podatke koji se analiziraju
- Dodajte markdown ćelije s objašnjenjima prije kodnih ćelija
- Fokusirajte kodne ćelije na pojedinačne koncepte ili operacije
- Koristite pandas za manipulaciju podacima, matplotlib za vizualizaciju
- Uobičajeni uzorak uvoza:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Slijedite Vue.js 2 smjernice za stil i najbolje prakse
- ESLint konfiguracija u `quiz-app/package.json`
- Koristite Vue komponente u jednoj datoteci (.vue datoteke)
- Održavajte arhitekturu temeljenu na komponentama
- Pokrenite `npm run lint` prije predaje promjena

### Markdown dokumentacija
- Koristite jasnu hijerarhiju naslova (# ## ### itd.)
- Dodajte kodne blokove s oznakama jezika
- Dodajte alt tekst za slike
- Povežite se na povezane lekcije i resurse
- Održavajte razumne duljine linija radi čitljivosti

### Organizacija datoteka
- Sadržaj lekcija u numeriranim mapama (01-defining-data-science, itd.)
- Rješenja u namjenskim `solution/` podmapama
- Prijevodi preslikavaju englesku strukturu u mapi `translations/`
- Datoteke s podacima u `data/` ili mapama specifičnim za lekcije

## Izgradnja i implementacija

### Implementacija aplikacije za kvizove
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Implementacija Azure Static Web Apps
Aplikacija za kvizove može se implementirati na Azure Static Web Apps:
1. Kreirajte resurs Azure Static Web App
2. Povežite se s GitHub repozitorijem
3. Konfigurirajte postavke izgradnje:
   - Lokacija aplikacije: `quiz-app`
   - Lokacija izlaza: `dist`
4. GitHub Actions tijek rada automatski će implementirati promjene nakon guranja

### Dokumentacijska stranica
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Repozitorij uključuje konfiguraciju razvojnih kontejnera
- Codespaces automatski postavlja Python i Node.js okruženje
- Otvorite repozitorij u Codespace putem GitHub sučelja
- Sve ovisnosti se automatski instaliraju

## Smjernice za Pull Requestove

### Prije predaje
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Format naslova PR-a
- Koristite jasne, opisne naslove
- Format: `[Komponenta] Kratak opis`
- Primjeri:
  - `[Lekcija 7] Popravak greške uvoza u Python bilježnici`
  - `[Aplikacija za kvizove] Dodavanje njemačkog prijevoda`
  - `[Dokumentacija] Ažuriranje README s novim preduvjetima`

### Potrebne provjere
- Osigurajte da se sav kod izvršava bez grešaka
- Provjerite da se bilježnice potpuno izvršavaju
- Potvrdite da se Vue.js aplikacije uspješno izgrađuju
- Provjerite da veze u dokumentaciji rade
- Testirajte aplikaciju za kvizove ako je izmijenjena
- Provjerite da prijevodi održavaju dosljednu strukturu

### Smjernice za doprinos
- Slijedite postojeći stil koda i uzorke
- Dodajte objašnjavajuće komentare za složenu logiku
- Ažurirajte relevantnu dokumentaciju
- Testirajte promjene kroz različite module lekcija ako je primjenjivo
- Pregledajte datoteku CONTRIBUTING.md

## Dodatne napomene

### Uobičajene korištene biblioteke
- **pandas**: Manipulacija i analiza podataka
- **numpy**: Numeričko računanje
- **matplotlib**: Vizualizacija i crtanje podataka
- **seaborn**: Statistička vizualizacija podataka (neke lekcije)
- **scikit-learn**: Strojno učenje (napredne lekcije)

### Rad s datotekama podataka
- Datoteke podataka nalaze se u mapi `data/` ili mapama specifičnim za lekcije
- Većina bilježnica očekuje datoteke podataka u relativnim putanjama
- CSV datoteke su primarni format podataka
- Neke lekcije koriste JSON za primjere nerelacijskih podataka

### Podrška za više jezika
- 40+ prijevoda jezika putem automatiziranih GitHub Actions
- Tijek rada za prijevod u `.github/workflows/co-op-translator.yml`
- Prijevodi u mapi `translations/` s kodovima jezika
- Prijevodi kvizova u `quiz-app/src/assets/translations/`

### Opcije razvojnih okruženja
1. **Lokalni razvoj**: Instalirajte Python, Jupyter, Node.js lokalno
2. **GitHub Codespaces**: Cloud-based instant razvojno okruženje
3. **VS Code razvojni kontejneri**: Lokalni razvoj temeljen na kontejnerima
4. **Binder**: Pokrenite bilježnice u oblaku (ako je konfigurirano)

### Smjernice za sadržaj lekcija
- Svaka lekcija je samostalna, ali se nadovezuje na prethodne koncepte
- Kvizovi prije lekcije testiraju prethodno znanje
- Kvizovi nakon lekcije učvršćuju naučeno
- Zadaci pružaju praktičnu vježbu
- Sketchnotes pružaju vizualne sažetke

### Rješavanje uobičajenih problema

**Problemi s Jupyter kernelom:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Neuspjesi instalacije npm-a:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Greške uvoza u bilježnicama:**
- Provjerite jesu li sve potrebne biblioteke instalirane
- Provjerite kompatibilnost verzije Pythona (preporučuje se Python 3.7+)
- Osigurajte da je virtualno okruženje aktivirano

**Docsify se ne učitava:**
- Provjerite da poslužujete iz korijena repozitorija
- Provjerite da `index.html` postoji
- Osigurajte ispravan mrežni pristup (port 3000)

### Razmatranja performansi
- Veliki skupovi podataka mogu zahtijevati vrijeme za učitavanje u bilježnicama
- Prikaz vizualizacija može biti spor za složene grafikone
- Vue.js razvojni server omogućuje hot-reload za brzu iteraciju
- Produkcijske izgradnje su optimizirane i minimizirane

### Sigurnosne napomene
- Ne smiju se predavati osjetljivi podaci ili vjerodajnice
- Koristite varijable okruženja za API ključeve u lekcijama u oblaku
- Lekcije povezane s Azureom mogu zahtijevati vjerodajnice za Azure račun
- Održavajte ažuriranost ovisnosti radi sigurnosnih zakrpa

## Doprinos prijevodima
- Automatski prijevodi upravljani putem GitHub Actions
- Ručne korekcije dobrodošle za točnost prijevoda
- Slijedite postojeću strukturu mapa za prijevode
- Ažurirajte poveznice kvizova kako bi uključivale parametar jezika: `?loc=fr`
- Testirajte prevedene lekcije za ispravan prikaz

## Povezani resursi
- Glavni kurikulum: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Forum za raspravu: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Ostali Microsoft kurikulumi: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Održavanje projekta
- Redovita ažuriranja za održavanje aktualnosti sadržaja
- Doprinosi zajednice su dobrodošli
- Problemi se prate na GitHubu
- PR-ove pregledavaju održavatelji kurikuluma
- Mjesečni pregledi i ažuriranja sadržaja

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.