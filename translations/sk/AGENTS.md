<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:38:05+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sk"
}
-->
# AGENTS.md

## Prehľad projektu

Data Science for Beginners je komplexný 10-týždňový, 20-lekciový kurz vytvorený tímom Microsoft Azure Cloud Advocates. Tento repozitár je vzdelávací zdroj, ktorý učí základné koncepty dátovej vedy prostredníctvom lekcií založených na projektoch, vrátane Jupyter notebookov, interaktívnych kvízov a praktických úloh.

**Kľúčové technológie:**
- **Jupyter Notebooks**: Hlavné médium na učenie pomocou Pythonu 3
- **Python knižnice**: pandas, numpy, matplotlib na analýzu a vizualizáciu dát
- **Vue.js 2**: Aplikácia na kvízy (priečinok quiz-app)
- **Docsify**: Generátor dokumentačných stránok pre offline prístup
- **Node.js/npm**: Správa balíkov pre JavaScript komponenty
- **Markdown**: Všetok obsah lekcií a dokumentácia

**Architektúra:**
- Vzdelávací repozitár s podporou viacerých jazykov a rozsiahlymi prekladmi
- Štruktúrovaný do modulov lekcií (1-Úvod až 6-Dátová veda v praxi)
- Každá lekcia obsahuje README, notebooky, úlohy a kvízy
- Samostatná aplikácia Vue.js na hodnotenie pred/po lekciách
- Podpora GitHub Codespaces a VS Code dev kontajnerov

## Príkazy na nastavenie

### Nastavenie repozitára
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Nastavenie Python prostredia
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Nastavenie aplikácie na kvízy
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

### Docsify dokumentačný server
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Nastavenie projektov na vizualizáciu
Pre projekty na vizualizáciu, ako napríklad meaningful-visualizations (lekcia 13):
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


## Pracovný postup vývoja

### Práca s Jupyter notebookmi
1. Spustite Jupyter v koreňovom adresári repozitára: `jupyter notebook`
2. Prejdite do požadovaného priečinka lekcie
3. Otvorte súbory `.ipynb` na prácu s cvičeniami
4. Notebooky sú samostatné, obsahujú vysvetlenia a bunky s kódom
5. Väčšina notebookov používa pandas, numpy a matplotlib - uistite sa, že sú nainštalované

### Štruktúra lekcií
Každá lekcia zvyčajne obsahuje:
- `README.md` - Hlavný obsah lekcie s teóriou a príkladmi
- `notebook.ipynb` - Praktické cvičenia v Jupyter notebooku
- `assignment.ipynb` alebo `assignment.md` - Úlohy na precvičenie
- Priečinok `solution/` - Notebooky a kód s riešeniami
- Priečinok `images/` - Podporné vizuálne materiály

### Vývoj aplikácie na kvízy
- Aplikácia Vue.js 2 s hot-reload počas vývoja
- Kvízy sú uložené v `quiz-app/src/assets/translations/`
- Každý jazyk má vlastný priečinok s prekladmi (en, fr, es, atď.)
- Číslovanie kvízov začína od 0 a pokračuje až do 39 (celkovo 40 kvízov)

### Pridávanie prekladov
- Preklady sa ukladajú do priečinka `translations/` v koreňovom adresári repozitára
- Každý jazyk má kompletnú štruktúru lekcií zrkadlenú z angličtiny
- Automatizované preklady prostredníctvom GitHub Actions (co-op-translator.yml)

## Pokyny na testovanie

### Testovanie aplikácie na kvízy
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Testovanie notebookov
- Pre notebooky neexistuje automatizovaný testovací rámec
- Manuálna validácia: Spustite všetky bunky postupne, aby ste sa uistili, že neobsahujú chyby
- Overte dostupnosť dátových súborov a správnosť generovaných výstupov
- Skontrolujte, či sa vizualizácie správne zobrazujú

### Testovanie dokumentácie
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Kontroly kvality kódu
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Pokyny pre štýl kódu

### Python (Jupyter notebooky)
- Dodržiavajte štýlové pokyny PEP 8 pre Python kód
- Používajte jasné názvy premenných, ktoré vysvetľujú analyzované dáta
- Pred bunkami s kódom pridávajte bunky s vysvetleniami v Markdown
- Udržujte bunky s kódom zamerané na jednotlivé koncepty alebo operácie
- Používajte pandas na manipuláciu s dátami, matplotlib na vizualizáciu
- Bežný importovací vzor:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Dodržiavajte štýlové pokyny Vue.js 2 a osvedčené postupy
- Konfigurácia ESLint v `quiz-app/package.json`
- Používajte Vue komponenty s jedným súborom (.vue súbory)
- Zachovávajte architektúru založenú na komponentoch
- Pred odoslaním zmien spustite `npm run lint`

### Dokumentácia v Markdown
- Používajte jasnú hierarchiu nadpisov (# ## ### atď.)
- Zahrňte bloky kódu so špecifikáciou jazyka
- Pridávajte alt text pre obrázky
- Odkazujte na súvisiace lekcie a zdroje
- Udržujte rozumnú dĺžku riadkov pre čitateľnosť

### Organizácia súborov
- Obsah lekcií v očíslovaných priečinkoch (01-defining-data-science, atď.)
- Riešenia v samostatných podpriečinkoch `solution/`
- Preklady zrkadlia anglickú štruktúru v priečinku `translations/`
- Dátové súbory uchovávajte v priečinku `data/` alebo v priečinkoch špecifických pre lekcie

## Build a nasadenie

### Nasadenie aplikácie na kvízy
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Nasadenie Azure Static Web Apps
Aplikáciu quiz-app je možné nasadiť na Azure Static Web Apps:
1. Vytvorte zdroj Azure Static Web App
2. Pripojte sa k GitHub repozitáru
3. Konfigurujte nastavenia buildu:
   - Umiestnenie aplikácie: `quiz-app`
   - Umiestnenie výstupu: `dist`
4. GitHub Actions workflow automaticky nasadí pri pushi

### Dokumentačná stránka
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Repozitár obsahuje konfiguráciu dev kontajnera
- Codespaces automaticky nastaví Python a Node.js prostredie
- Otvorte repozitár v Codespace cez GitHub UI
- Všetky závislosti sa nainštalujú automaticky

## Pokyny pre pull requesty

### Pred odoslaním
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Formát názvu PR
- Používajte jasné, popisné názvy
- Formát: `[Komponent] Stručný popis`
- Príklady:
  - `[Lekcia 7] Oprava chyby importu v Python notebooku`
  - `[Aplikácia na kvízy] Pridanie nemeckého prekladu`
  - `[Dokumentácia] Aktualizácia README s novými predpokladmi`

### Požadované kontroly
- Uistite sa, že všetok kód beží bez chýb
- Overte, že notebooky sa vykonávajú úplne
- Skontrolujte, či aplikácie Vue.js úspešne buildujú
- Overte funkčnosť odkazov v dokumentácii
- Otestujte aplikáciu na kvízy, ak bola upravená
- Overte, že preklady zachovávajú konzistentnú štruktúru

### Pokyny pre prispievanie
- Dodržiavajte existujúci štýl kódu a vzory
- Pridávajte vysvetľujúce komentáre k zložitej logike
- Aktualizujte relevantnú dokumentáciu
- Testujte zmeny naprieč rôznymi modulmi lekcií, ak je to vhodné
- Preštudujte si súbor CONTRIBUTING.md

## Ďalšie poznámky

### Bežne používané knižnice
- **pandas**: Manipulácia a analýza dát
- **numpy**: Numerické výpočty
- **matplotlib**: Vizualizácia a grafy
- **seaborn**: Štatistická vizualizácia dát (niektoré lekcie)
- **scikit-learn**: Strojové učenie (pokročilé lekcie)

### Práca s dátovými súbormi
- Dátové súbory sa nachádzajú v priečinku `data/` alebo v priečinkoch špecifických pre lekcie
- Väčšina notebookov očakáva dátové súbory v relatívnych cestách
- Primárnym formátom dát sú CSV súbory
- Niektoré lekcie používajú JSON pre príklady nerelačných dát

### Podpora viacerých jazykov
- Viac ako 40 jazykových prekladov prostredníctvom automatizovaných GitHub Actions
- Workflow pre preklady v `.github/workflows/co-op-translator.yml`
- Preklady v priečinku `translations/` s jazykovými kódmi
- Preklady kvízov v `quiz-app/src/assets/translations/`

### Možnosti vývojového prostredia
1. **Lokálny vývoj**: Nainštalujte Python, Jupyter, Node.js lokálne
2. **GitHub Codespaces**: Cloudové okamžité vývojové prostredie
3. **VS Code Dev kontajnery**: Lokálny vývoj založený na kontajneroch
4. **Binder**: Spustenie notebookov v cloude (ak je nakonfigurované)

### Pokyny pre obsah lekcií
- Každá lekcia je samostatná, ale stavia na predchádzajúcich konceptoch
- Kvízy pred lekciou testujú predchádzajúce znalosti
- Kvízy po lekcii posilňujú učenie
- Úlohy poskytujú praktické precvičenie
- Sketchnotes poskytujú vizuálne zhrnutia

### Riešenie bežných problémov

**Problémy s Jupyter kernelom:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Zlyhania npm inštalácie:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Chyby importu v notebookoch:**
- Overte, že všetky požadované knižnice sú nainštalované
- Skontrolujte kompatibilitu verzie Pythonu (odporúčaný Python 3.7+)
- Uistite sa, že virtuálne prostredie je aktivované

**Docsify sa nenačítava:**
- Overte, že server spúšťate z koreňového adresára repozitára
- Skontrolujte, či existuje súbor `index.html`
- Uistite sa, že máte správny sieťový prístup (port 3000)

### Úvahy o výkone
- Veľké dátové súbory môžu trvať dlhšie na načítanie v notebookoch
- Vizualizácie môžu byť pomalé pri zložitých grafoch
- Dev server Vue.js umožňuje hot-reload pre rýchlu iteráciu
- Produkčné buildy sú optimalizované a minifikované

### Poznámky k bezpečnosti
- Do repozitára by nemali byť nahrávané citlivé údaje alebo poverenia
- Používajte environmentálne premenné pre akékoľvek API kľúče v cloudových lekciách
- Lekcie súvisiace s Azure môžu vyžadovať poverenia k Azure účtu
- Udržujte závislosti aktualizované kvôli bezpečnostným opravám

## Prispievanie k prekladom
- Automatizované preklady sú spravované prostredníctvom GitHub Actions
- Manuálne opravy sú vítané pre presnosť prekladov
- Dodržiavajte existujúcu štruktúru priečinkov pre preklady
- Aktualizujte odkazy na kvízy, aby obsahovali jazykový parameter: `?loc=fr`
- Testujte preložené lekcie na správne zobrazenie

## Súvisiace zdroje
- Hlavný kurz: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Študentské centrum: https://docs.microsoft.com/learn/student-hub
- Diskusné fórum: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Ďalšie Microsoft kurzy: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Údržba projektu
- Pravidelné aktualizácie na udržanie aktuálneho obsahu
- Príspevky od komunity sú vítané
- Problémy sú sledované na GitHube
- PR sú kontrolované správcami kurzu
- Mesačné kontroly obsahu a aktualizácie

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.