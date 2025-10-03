<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:36:41+00:00",
  "source_file": "AGENTS.md",
  "language_code": "cs"
}
-->
# AGENTS.md

## Přehled projektu

Data Science for Beginners je komplexní desetitýdenní kurz s 20 lekcemi vytvořený týmem Microsoft Azure Cloud Advocates. Tento repozitář slouží jako vzdělávací zdroj, který učí základní koncepty datové vědy prostřednictvím projektově orientovaných lekcí, včetně Jupyter notebooků, interaktivních kvízů a praktických úkolů.

**Klíčové technologie:**
- **Jupyter Notebooks**: Hlavní výukové médium využívající Python 3
- **Python knihovny**: pandas, numpy, matplotlib pro analýzu a vizualizaci dat
- **Vue.js 2**: Aplikace pro kvízy (složka quiz-app)
- **Docsify**: Generátor dokumentačních stránek pro offline přístup
- **Node.js/npm**: Správa balíčků pro JavaScript komponenty
- **Markdown**: Veškerý obsah lekcí a dokumentace

**Architektura:**
- Vzdělávací repozitář s podporou více jazyků a rozsáhlými překlady
- Strukturováno do modulů lekcí (1-Introduction až 6-Data-Science-In-Wild)
- Každá lekce obsahuje README, notebooky, úkoly a kvízy
- Samostatná aplikace Vue.js pro hodnocení před a po lekci
- Podpora GitHub Codespaces a vývojových kontejnerů VS Code

## Příkazy pro nastavení

### Nastavení repozitáře
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Nastavení Python prostředí
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Nastavení aplikace pro kvízy
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

### Dokumentační server Docsify
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Nastavení projektů pro vizualizaci
Pro projekty vizualizace, jako je meaningful-visualizations (lekce 13):
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


## Pracovní postup vývoje

### Práce s Jupyter notebooky
1. Spusťte Jupyter v kořenovém adresáři repozitáře: `jupyter notebook`
2. Přejděte do složky požadované lekce
3. Otevřete soubory `.ipynb` a pracujte na cvičeních
4. Notebooky jsou samostatné, obsahují vysvětlení a buňky s kódem
5. Většina notebooků používá pandas, numpy a matplotlib - ujistěte se, že jsou nainstalovány

### Struktura lekce
Každá lekce obvykle obsahuje:
- `README.md` - Hlavní obsah lekce s teorií a příklady
- `notebook.ipynb` - Praktická cvičení v Jupyter notebooku
- `assignment.ipynb` nebo `assignment.md` - Praktické úkoly
- Složku `solution/` - Notebooky a kód s řešeními
- Složku `images/` - Podpůrné vizuální materiály

### Vývoj aplikace pro kvízy
- Aplikace Vue.js 2 s podporou hot-reload během vývoje
- Kvízy jsou uloženy ve složce `quiz-app/src/assets/translations/`
- Každý jazyk má vlastní složku s překlady (en, fr, es atd.)
- Číslování kvízů začíná od 0 a končí na 39 (celkem 40 kvízů)

### Přidávání překladů
- Překlady se ukládají do složky `translations/` v kořenovém adresáři repozitáře
- Každý jazyk má kompletní strukturu lekcí zrcadlenou z angličtiny
- Automatizované překlady prostřednictvím GitHub Actions (co-op-translator.yml)

## Pokyny k testování

### Testování aplikace pro kvízy
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Testování notebooků
- Pro notebooky neexistuje žádný automatizovaný testovací rámec
- Ruční ověření: Spusťte všechny buňky v pořadí a ověřte, že nedochází k chybám
- Ověřte, že jsou přístupné datové soubory a že výstupy jsou správně generovány
- Zkontrolujte, zda se vizualizace správně vykreslují

### Testování dokumentace
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


## Pokyny ke stylu kódu

### Python (Jupyter notebooky)
- Dodržujte pokyny ke stylu PEP 8 pro Python kód
- Používejte jasné názvy proměnných, které vysvětlují analyzovaná data
- Přidávejte buňky Markdown s vysvětlením před buňkami s kódem
- Udržujte buňky s kódem zaměřené na jednotlivé koncepty nebo operace
- Používejte pandas pro manipulaci s daty, matplotlib pro vizualizaci
- Běžný vzor importu:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Dodržujte pokyny ke stylu Vue.js 2 a osvědčené postupy
- Konfigurace ESLint ve `quiz-app/package.json`
- Používejte Vue komponenty s jedním souborem (.vue soubory)
- Udržujte architekturu založenou na komponentách
- Spusťte `npm run lint` před odesláním změn

### Dokumentace v Markdownu
- Používejte jasnou hierarchii nadpisů (# ## ### atd.)
- Přidávejte bloky kódu s určením jazyka
- Přidávejte alternativní texty k obrázkům
- Odkazujte na související lekce a zdroje
- Udržujte rozumnou délku řádků pro čitelnost

### Organizace souborů
- Obsah lekcí ve složkách s čísly (01-defining-data-science atd.)
- Řešení ve vyhrazených podsložkách `solution/`
- Překlady zrcadlí anglickou strukturu ve složce `translations/`
- Datové soubory uchovávejte ve složce `data/` nebo ve složkách specifických pro lekce

## Sestavení a nasazení

### Nasazení aplikace pro kvízy
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Nasazení Azure Static Web Apps
Aplikace quiz-app může být nasazena na Azure Static Web Apps:
1. Vytvořte prostředek Azure Static Web App
2. Připojte se k repozitáři na GitHubu
3. Nakonfigurujte nastavení sestavení:
   - Umístění aplikace: `quiz-app`
   - Umístění výstupu: `dist`
4. GitHub Actions workflow automaticky nasadí při push

### Dokumentační web
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Repozitář obsahuje konfiguraci vývojového kontejneru
- Codespaces automaticky nastaví prostředí pro Python a Node.js
- Otevřete repozitář v Codespace prostřednictvím GitHub UI
- Všechny závislosti se nainstalují automaticky

## Pokyny pro pull requesty

### Před odesláním
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Formát názvu PR
- Používejte jasné, popisné názvy
- Formát: `[Komponenta] Stručný popis`
- Příklady:
  - `[Lekce 7] Oprava chyby importu v Python notebooku`
  - `[Aplikace pro kvízy] Přidání německého překladu`
  - `[Dokumentace] Aktualizace README s novými předpoklady`

### Požadované kontroly
- Ujistěte se, že veškerý kód běží bez chyb
- Ověřte, že notebooky se kompletně spustí
- Zkontrolujte, že aplikace Vue.js se úspěšně sestaví
- Ověřte, že odkazy v dokumentaci fungují
- Otestujte aplikaci pro kvízy, pokud byla upravena
- Ověřte, že překlady zachovávají konzistentní strukturu

### Pokyny pro přispívání
- Dodržujte stávající styl kódu a vzory
- Přidávejte vysvětlující komentáře ke složitější logice
- Aktualizujte příslušnou dokumentaci
- Testujte změny napříč různými moduly lekcí, pokud je to relevantní
- Prostudujte si soubor CONTRIBUTING.md

## Další poznámky

### Běžně používané knihovny
- **pandas**: Manipulace a analýza dat
- **numpy**: Numerické výpočty
- **matplotlib**: Vizualizace a vykreslování dat
- **seaborn**: Statistická vizualizace dat (některé lekce)
- **scikit-learn**: Strojové učení (pokročilé lekce)

### Práce s datovými soubory
- Datové soubory jsou umístěny ve složce `data/` nebo ve složkách specifických pro lekce
- Většina notebooků očekává datové soubory v relativních cestách
- Hlavním formátem dat jsou soubory CSV
- Některé lekce používají JSON pro příklady nerelačních dat

### Podpora více jazyků
- Přes 40 jazykových překladů prostřednictvím automatizovaných GitHub Actions
- Workflow překladu ve `.github/workflows/co-op-translator.yml`
- Překlady ve složce `translations/` s jazykovými kódy
- Překlady kvízů ve složce `quiz-app/src/assets/translations/`

### Možnosti vývojového prostředí
1. **Lokální vývoj**: Nainstalujte Python, Jupyter, Node.js lokálně
2. **GitHub Codespaces**: Cloudové okamžité vývojové prostředí
3. **VS Code Dev Containers**: Lokální vývoj založený na kontejnerech
4. **Binder**: Spuštění notebooků v cloudu (pokud je nakonfigurováno)

### Pokyny k obsahu lekcí
- Každá lekce je samostatná, ale staví na předchozích konceptech
- Kvízy před lekcí testují předchozí znalosti
- Kvízy po lekci posilují učení
- Úkoly poskytují praktické procvičení
- Sketchnotes poskytují vizuální shrnutí

### Řešení běžných problémů

**Problémy s jádrem Jupyter:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Chyby při instalaci npm:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Chyby importu v notebookách:**
- Ověřte, že jsou nainstalovány všechny požadované knihovny
- Zkontrolujte kompatibilitu verze Pythonu (doporučeno Python 3.7+)
- Ujistěte se, že je aktivováno virtuální prostředí

**Docsify se nenačítá:**
- Ověřte, že spouštíte ze základního adresáře repozitáře
- Zkontrolujte, zda existuje `index.html`
- Ujistěte se, že máte správný přístup k síti (port 3000)

### Úvahy o výkonu
- Velké datové sady mohou trvat déle na načtení v notebookách
- Vykreslování vizualizací může být pomalé u složitých grafů
- Vývojový server Vue.js umožňuje rychlé iterace díky hot-reload
- Produkční sestavení jsou optimalizována a minimalizována

### Bezpečnostní poznámky
- Do repozitáře by neměla být ukládána citlivá data nebo přihlašovací údaje
- Používejte proměnné prostředí pro jakékoli API klíče v cloudových lekcích
- Lekce související s Azure mohou vyžadovat přihlašovací údaje k účtu Azure
- Udržujte závislosti aktuální kvůli bezpečnostním opravám

## Přispívání k překladům
- Automatizované překlady jsou spravovány prostřednictvím GitHub Actions
- Manuální opravy jsou vítány pro zajištění přesnosti překladů
- Dodržujte stávající strukturu složek pro překlady
- Aktualizujte odkazy na kvízy tak, aby zahrnovaly parametr jazyka: `?loc=fr`
- Testujte přeložené lekce, zda se správně zobrazují

## Související zdroje
- Hlavní kurikulum: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Diskusní fórum: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Další kurikula od Microsoftu: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Údržba projektu
- Pravidelné aktualizace pro udržení aktuálnosti obsahu
- Příspěvky komunity jsou vítány
- Problémy jsou sledovány na GitHubu
- PR jsou kontrolovány správci kurikula
- Měsíční revize a aktualizace obsahu

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme zodpovědní za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.