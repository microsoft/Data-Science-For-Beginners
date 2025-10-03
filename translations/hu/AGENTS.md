<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:35:23+00:00",
  "source_file": "AGENTS.md",
  "language_code": "hu"
}
-->
# AGENTS.md

## Projekt áttekintése

A Data Science for Beginners egy átfogó, 10 hetes, 20 leckéből álló tananyag, amelyet a Microsoft Azure Cloud Advocates készített. A repozitórium egy tanulási erőforrás, amely projektalapú leckéken keresztül tanítja az adatkutatás alapvető fogalmait, beleértve a Jupyter notebookokat, interaktív kvízeket és gyakorlati feladatokat.

**Kulcstechnológiák:**
- **Jupyter Notebookok**: Elsődleges tanulási eszköz Python 3 használatával
- **Python könyvtárak**: pandas, numpy, matplotlib az adatelemzéshez és vizualizációhoz
- **Vue.js 2**: Kvíz alkalmazás (quiz-app mappa)
- **Docsify**: Dokumentációs oldal generátor offline hozzáféréshez
- **Node.js/npm**: JavaScript komponensek csomagkezelése
- **Markdown**: Minden lecke tartalma és dokumentáció

**Architektúra:**
- Többnyelvű oktatási repozitórium kiterjedt fordításokkal
- Leckemodulokra strukturálva (1-Bevezetés-től 6-Adattudomány-a-gyakorlatban-ig)
- Minden lecke tartalmaz README-t, notebookokat, feladatokat és kvízeket
- Önálló Vue.js kvíz alkalmazás elő-/utólecke értékelésekhez
- GitHub Codespaces és VS Code fejlesztői konténerek támogatása

## Beállítási parancsok

### Repozitórium beállítása
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Python környezet beállítása
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Kvíz alkalmazás beállítása
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

### Docsify dokumentációs szerver
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Vizualizációs projektek beállítása
Olyan vizualizációs projektekhez, mint a meaningful-visualizations (13. lecke):
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


## Fejlesztési munkafolyamat

### Jupyter Notebookok használata
1. Indítsa el a Jupyter-t a repozitórium gyökerében: `jupyter notebook`
2. Navigáljon a kívánt lecke mappájába
3. Nyissa meg a `.ipynb` fájlokat a gyakorlatok elvégzéséhez
4. A notebookok önállóak, magyarázatokat és kódcellákat tartalmaznak
5. A legtöbb notebook pandas, numpy és matplotlib használatát igényli - győződjön meg róla, hogy ezek telepítve vannak

### Lecke struktúra
Minden lecke általában tartalmaz:
- `README.md` - Fő lecke tartalom elmélettel és példákkal
- `notebook.ipynb` - Gyakorlati Jupyter notebook gyakorlatok
- `assignment.ipynb` vagy `assignment.md` - Gyakorlati feladatok
- `solution/` mappa - Megoldási notebookok és kód
- `images/` mappa - Támogató vizuális anyagok

### Kvíz alkalmazás fejlesztése
- Vue.js 2 alkalmazás hot-reload funkcióval fejlesztés közben
- Kvízek tárolása a `quiz-app/src/assets/translations/` mappában
- Minden nyelvnek saját fordítási mappája van (en, fr, es stb.)
- A kvízek számozása 0-tól kezdődik és 39-ig tart (összesen 40 kvíz)

### Fordítások hozzáadása
- Fordítások a repozitórium gyökerében lévő `translations/` mappába kerülnek
- Minden nyelv teljes lecke struktúrája tükrözi az angolt
- Automatikus fordítás GitHub Actions segítségével (co-op-translator.yml)

## Tesztelési utasítások

### Kvíz alkalmazás tesztelése
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Notebook tesztelése
- Nincs automatizált tesztkeretrendszer a notebookokhoz
- Manuális ellenőrzés: Futtassa az összes cellát sorrendben, hogy megbizonyosodjon róla, nincs hiba
- Ellenőrizze, hogy az adatfájlok elérhetők-e, és az eredmények helyesen generálódnak-e
- Győződjön meg róla, hogy a vizualizációk megfelelően jelennek meg

### Dokumentáció tesztelése
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Kódminőség ellenőrzések
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Kódstílus irányelvek

### Python (Jupyter Notebookok)
- Kövesse a PEP 8 stílusirányelveket Python kódhoz
- Használjon egyértelmű változóneveket, amelyek magyarázzák az elemzett adatokat
- Tartalmazzon markdown cellákat magyarázatokkal a kódcellák előtt
- Tartsa a kódcellákat egyetlen fogalomra vagy műveletre fókuszálva
- Használja a pandas-t adatmanipulációhoz, matplotlib-et vizualizációhoz
- Gyakori import minta:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Kövesse a Vue.js 2 stílusirányelveket és legjobb gyakorlatokat
- ESLint konfiguráció a `quiz-app/package.json` fájlban
- Használjon Vue egyfájlú komponenseket (.vue fájlok)
- Tartsa meg a komponens-alapú architektúrát
- Futtassa az `npm run lint` parancsot a változtatások elkötelezése előtt

### Markdown dokumentáció
- Használjon egyértelmű címsor hierarchiát (# ## ### stb.)
- Tartalmazzon kódrészleteket nyelvi specifikációval
- Adjon meg alternatív szöveget a képekhez
- Linkeljen kapcsolódó leckékre és erőforrásokra
- Tartsa a sorhosszúságot olvasható szinten

### Fájlok szervezése
- Lecke tartalom számozott mappákban (01-defining-data-science stb.)
- Megoldások dedikált `solution/` almappákban
- Fordítások tükrözik az angol struktúrát a `translations/` mappában
- Adatfájlok a `data/` vagy lecke-specifikus mappákban

## Építés és telepítés

### Kvíz alkalmazás telepítése
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Azure Static Web Apps telepítés
A quiz-app telepíthető Azure Static Web Apps-re:
1. Hozzon létre Azure Static Web App erőforrást
2. Csatlakoztassa a GitHub repozitóriumhoz
3. Konfigurálja az építési beállításokat:
   - Alkalmazás helye: `quiz-app`
   - Kimeneti hely: `dist`
4. A GitHub Actions munkafolyamat automatikusan telepíti a push után

### Dokumentációs oldal
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- A repozitórium tartalmaz fejlesztői konténer konfigurációt
- A Codespaces automatikusan beállítja a Python és Node.js környezetet
- Nyissa meg a repozitóriumot Codespace-ben a GitHub UI segítségével
- Minden függőség automatikusan települ

## Pull Request irányelvek

### Beküldés előtt
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### PR cím formátuma
- Használjon egyértelmű, leíró címeket
- Formátum: `[Komponens] Rövid leírás`
- Példák:
  - `[7. lecke] Python notebook import hiba javítása`
  - `[Kvíz alkalmazás] Német fordítás hozzáadása`
  - `[Dokumentáció] README frissítése új előfeltételekkel`

### Szükséges ellenőrzések
- Győződjön meg róla, hogy minden kód hiba nélkül fut
- Ellenőrizze, hogy a notebookok teljesen végrehajtódnak
- Győződjön meg róla, hogy a Vue.js alkalmazások sikeresen épülnek
- Ellenőrizze, hogy a dokumentációs linkek működnek
- Tesztelje a kvíz alkalmazást, ha módosítva lett
- Ellenőrizze, hogy a fordítások következetes struktúrát tartanak

### Hozzájárulási irányelvek
- Kövesse a meglévő kódstílust és mintákat
- Adjon magyarázó megjegyzéseket a bonyolult logikához
- Frissítse a releváns dokumentációt
- Tesztelje a változtatásokat különböző leckemodulokon, ha alkalmazható
- Tekintse át a CONTRIBUTING.md fájlt

## További megjegyzések

### Gyakran használt könyvtárak
- **pandas**: Adatmanipuláció és elemzés
- **numpy**: Numerikus számítások
- **matplotlib**: Adatvizualizáció és grafikonok
- **seaborn**: Statisztikai adatvizualizáció (néhány lecke)
- **scikit-learn**: Gépi tanulás (haladó leckék)

### Adatfájlok kezelése
- Adatfájlok a `data/` mappában vagy lecke-specifikus könyvtárakban találhatók
- A legtöbb notebook relatív útvonalakon várja az adatfájlokat
- A CSV fájlok az elsődleges adatformátum
- Néhány lecke JSON-t használ nem relációs adatpéldákhoz

### Többnyelvű támogatás
- 40+ nyelvi fordítás automatikus GitHub Actions segítségével
- Fordítási munkafolyamat a `.github/workflows/co-op-translator.yml` fájlban
- Fordítások a `translations/` mappában nyelvi kódokkal
- Kvíz fordítások a `quiz-app/src/assets/translations/` mappában

### Fejlesztési környezet opciók
1. **Helyi fejlesztés**: Telepítse a Python-t, Jupyter-t, Node.js-t helyben
2. **GitHub Codespaces**: Felhőalapú azonnali fejlesztési környezet
3. **VS Code Dev Containers**: Helyi konténer-alapú fejlesztés
4. **Binder**: Notebookok indítása felhőben (ha konfigurálva van)

### Lecke tartalom irányelvek
- Minden lecke önálló, de az előző fogalmakra épít
- Előlecke kvízek tesztelik az előzetes tudást
- Utólecke kvízek megerősítik a tanultakat
- Feladatok gyakorlati tapasztalatot nyújtanak
- Sketchnotes vizuális összefoglalókat biztosítanak

### Gyakori problémák elhárítása

**Jupyter kernel problémák:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**npm telepítési hibák:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Import hibák notebookokban:**
- Ellenőrizze, hogy minden szükséges könyvtár telepítve van-e
- Ellenőrizze a Python verzió kompatibilitását (Python 3.7+ ajánlott)
- Győződjön meg róla, hogy a virtuális környezet aktiválva van

**Docsify nem töltődik be:**
- Ellenőrizze, hogy a repozitórium gyökeréből szolgáltat-e
- Ellenőrizze, hogy létezik-e `index.html`
- Győződjön meg róla, hogy megfelelő hálózati hozzáférés van (3000-es port)

### Teljesítmény szempontok
- Nagy adathalmazok betöltése időt vehet igénybe a notebookokban
- Vizualizációk megjelenítése lassú lehet összetett grafikonok esetén
- A Vue.js fejlesztői szerver hot-reload funkciót biztosít gyors iterációhoz
- A produkciós build-ek optimalizáltak és minifikáltak

### Biztonsági megjegyzések
- Ne kötelezzen el érzékeny adatokat vagy hitelesítő adatokat
- Használjon környezeti változókat bármilyen API kulcshoz felhőleckékben
- Azure-hoz kapcsolódó leckékhez Azure fiók hitelesítő adatok szükségesek lehetnek
- Tartsa a függőségeket naprakészen a biztonsági javítások érdekében

## Hozzájárulás fordításokhoz
- Automatikus fordítások kezelése GitHub Actions segítségével
- Kézi korrekciók szívesen látottak a fordítás pontossága érdekében
- Kövesse a meglévő fordítási mappa struktúrát
- Frissítse a kvíz linkeket, hogy tartalmazzák a nyelvi paramétert: `?loc=fr`
- Tesztelje a fordított leckéket a megfelelő megjelenítés érdekében

## Kapcsolódó erőforrások
- Fő tananyag: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Vita fórum: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Egyéb Microsoft tananyagok: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Projekt karbantartás
- Rendszeres frissítések a tartalom naprakészen tartásához
- Közösségi hozzájárulások szívesen látottak
- Problémák nyomon követése GitHub-on
- PR-eket a tananyag karbantartói felülvizsgálják
- Havi tartalomellenőrzések és frissítések

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.