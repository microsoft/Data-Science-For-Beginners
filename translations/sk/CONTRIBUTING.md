<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T14:33:05+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sk"
}
-->
# Prispievanie do Data Science for Beginners

Ďakujeme za váš záujem prispieť do učebných osnov Data Science for Beginners! Radi privítame príspevky od komunity.

## Obsah

- [Kódex správania](../..)
- [Ako môžem prispieť?](../..)
- [Začíname](../..)
- [Pokyny pre prispievanie](../..)
- [Proces Pull Request](../..)
- [Štýlové pokyny](../..)
- [Dohoda o licencii prispievateľa](../..)

## Kódex správania

Tento projekt prijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Viac informácií nájdete v [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
alebo kontaktujte [opencode@microsoft.com](mailto:opencode@microsoft.com) s ďalšími otázkami alebo pripomienkami.

## Ako môžem prispieť?

### Nahlasovanie chýb

Pred vytvorením hlásenia o chybe si prosím skontrolujte existujúce problémy, aby ste sa vyhli duplicite. Pri vytváraní hlásenia o chybe uveďte čo najviac podrobností:

- **Použite jasný a popisný názov**
- **Popíšte presné kroky na reprodukciu problému**
- **Poskytnite konkrétne príklady** (úryvky kódu, snímky obrazovky)
- **Popíšte pozorované správanie a očakávané výsledky**
- **Uveďte podrobnosti o vašom prostredí** (OS, verzia Pythonu, prehliadač)

### Navrhovanie vylepšení

Návrhy na vylepšenia sú vítané! Pri navrhovaní vylepšení:

- **Použite jasný a popisný názov**
- **Poskytnite podrobný popis navrhovaného vylepšenia**
- **Vysvetlite, prečo by toto vylepšenie bolo užitočné**
- **Uveďte podobné funkcie v iných projektoch, ak je to relevantné**

### Prispievanie do dokumentácie

Vylepšenia dokumentácie sú vždy ocenené:

- **Opravte preklepy a gramatické chyby**
- **Zlepšite jasnosť vysvetlení**
- **Doplňte chýbajúcu dokumentáciu**
- **Aktualizujte zastarané informácie**
- **Pridajte príklady alebo prípady použitia**

### Prispievanie kódu

Radi privítame príspevky kódu vrátane:

- **Nových lekcií alebo cvičení**
- **Opráv chýb**
- **Vylepšení existujúcich notebookov**
- **Nových datasetov alebo príkladov**
- **Vylepšení aplikácie kvízu**

## Začíname

### Predpoklady

Pred prispievaním sa uistite, že máte:

1. Účet na GitHub
2. Nainštalovaný Git na vašom systéme
3. Python 3.7+ a Jupyter nainštalovaný
4. Node.js a npm (pre príspevky do aplikácie kvízu)
5. Znalosť štruktúry učebných osnov

Pozrite si [INSTALLATION.md](INSTALLATION.md) pre podrobné pokyny na nastavenie.

### Fork a klonovanie

1. **Forknite repozitár** na GitHub
2. **Klonujte svoj fork** lokálne:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
3. **Pridajte upstream remote**:
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```

### Vytvorenie vetvy

Vytvorte novú vetvu pre svoju prácu:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Konvencie pre názvy vetiev:
- `feature/` - Nové funkcie alebo lekcie
- `fix/` - Opravy chýb
- `docs/` - Zmeny v dokumentácii
- `refactor/` - Refaktoring kódu

## Pokyny pre prispievanie

### Pre obsah lekcií

Pri prispievaní lekcií alebo úpravách existujúcich:

1. **Dodržiavajte existujúcu štruktúru**:
   - README.md s obsahom lekcie
   - Jupyter notebook s cvičeniami
   - Zadanie (ak je relevantné)
   - Odkaz na pred a po kvízy

2. **Zahrňte tieto prvky**:
   - Jasné vzdelávacie ciele
   - Krok za krokom vysvetlenia
   - Príklady kódu s komentármi
   - Cvičenia na precvičenie
   - Odkazy na ďalšie zdroje

3. **Zabezpečte prístupnosť**:
   - Používajte jasný, jednoduchý jazyk
   - Poskytnite alt text pre obrázky
   - Zahrňte komentáre ku kódu
   - Zohľadnite rôzne štýly učenia

### Pre Jupyter notebooky

1. **Vymažte všetky výstupy** pred commitom:
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```

2. **Zahrňte markdown bunky** s vysvetleniami

3. **Používajte konzistentné formátovanie**:
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```

4. **Otestujte svoj notebook** úplne pred odoslaním

### Pre Python kód

Dodržiavajte [PEP 8](https://www.python.org/dev/peps/pep-0008/) štýlové pokyny:

```python
# Good practices
import pandas as pd

def calculate_mean(data):
    """Calculate the mean of a dataset.
    
    Args:
        data (list): List of numerical values
        
    Returns:
        float: Mean of the dataset
    """
    return sum(data) / len(data)
```

### Pre príspevky do aplikácie kvízu

Pri úpravách aplikácie kvízu:

1. **Testujte lokálne**:
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```

2. **Spustite linter**:
   ```bash
   npm run lint
   ```

3. **Úspešne buildnite**:
   ```bash
   npm run build
   ```

4. **Dodržiavajte Vue.js štýlové pokyny** a existujúce vzory

### Pre preklady

Pri pridávaní alebo aktualizácii prekladov:

1. Dodržiavajte štruktúru v priečinku `translations/`
2. Použite kód jazyka ako názov priečinka (napr. `fr` pre francúzštinu)
3. Zachovajte rovnakú štruktúru súborov ako anglická verzia
4. Aktualizujte odkazy na kvízy, aby obsahovali parameter jazyka: `?loc=fr`
5. Otestujte všetky odkazy a formátovanie

## Proces Pull Request

### Pred odoslaním

1. **Aktualizujte svoju vetvu** s najnovšími zmenami:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Otestujte svoje zmeny**:
   - Spustite všetky upravené notebooky
   - Otestujte aplikáciu kvízu, ak bola upravená
   - Overte funkčnosť všetkých odkazov
   - Skontrolujte pravopisné a gramatické chyby

3. **Commitnite svoje zmeny**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   Píšte jasné commit správy:
   - Používajte prítomný čas ("Pridať funkciu" namiesto "Pridaná funkcia")
   - Používajte imperatívnu náladu ("Presunúť kurzor na..." namiesto "Presúva kurzor na...")
   - Obmedzte prvý riadok na 72 znakov
   - Odkazujte na problémy a pull requesty, ak je to relevantné

4. **Pushnite na svoj fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

### Vytvorenie Pull Request

1. Prejdite na [repozitár](https://github.com/microsoft/Data-Science-For-Beginners)
2. Kliknite na "Pull requests" → "New pull request"
3. Kliknite na "compare across forks"
4. Vyberte svoj fork a vetvu
5. Kliknite na "Create pull request"

### Formát názvu PR

Používajte jasné, popisné názvy podľa tohto formátu:

```
[Component] Brief description
```

Príklady:
- `[Lekcia 7] Oprava chyby importu v Python notebooku`
- `[Aplikácia kvízu] Pridanie nemeckého prekladu`
- `[Dokumentácia] Aktualizácia README s novými predpokladmi`
- `[Oprava] Korekcia cesty k dátam v lekcii vizualizácie`

### Popis PR

Zahrňte do popisu PR:

- **Čo**: Aké zmeny ste vykonali?
- **Prečo**: Prečo sú tieto zmeny potrebné?
- **Ako**: Ako ste implementovali zmeny?
- **Testovanie**: Ako ste testovali zmeny?
- **Snímky obrazovky**: Zahrňte snímky obrazovky pre vizuálne zmeny
- **Súvisiace problémy**: Odkaz na súvisiace problémy (napr. "Fixes #123")

### Proces kontroly

1. **Automatické kontroly** sa spustia na vašom PR
2. **Správcovia skontrolujú** váš príspevok
3. **Riešte spätnú väzbu** vykonaním ďalších commitov
4. Po schválení **správca zlúči** váš PR

### Po zlúčení vášho PR

1. Vymažte svoju vetvu:
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```

2. Aktualizujte svoj fork:
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

## Štýlové pokyny

### Markdown

- Používajte konzistentné úrovne nadpisov
- Zahrňte prázdne riadky medzi sekciami
- Používajte bloky kódu so špecifikáciou jazyka:
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
- Pridajte alt text k obrázkom: `![Alt text](../../translated_images/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.sk.png)`
- Udržujte rozumnú dĺžku riadkov (okolo 80-100 znakov)

### Python

- Dodržiavajte PEP 8 štýlové pokyny
- Používajte zmysluplné názvy premenných
- Pridajte docstringy k funkciám
- Zahrňte typové anotácie, kde je to vhodné:
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```

### JavaScript/Vue.js

- Dodržiavajte Vue.js 2 štýlové pokyny
- Používajte poskytnutú konfiguráciu ESLint
- Píšte modulárne, znovupoužiteľné komponenty
- Pridajte komentáre pre zložitú logiku

### Organizácia súborov

- Uchovávajte súvisiace súbory spolu
- Používajte popisné názvy súborov
- Dodržiavajte existujúcu štruktúru adresárov
- Necommitujte nepotrebné súbory (.DS_Store, .pyc, node_modules, atď.)

## Dohoda o licencii prispievateľa

Tento projekt víta príspevky a návrhy. Väčšina príspevkov vyžaduje, aby ste
súhlasili s Dohodou o licencii prispievateľa (CLA), ktorá deklaruje, že máte právo
a skutočne udeľujete práva na používanie vášho príspevku. Podrobnosti nájdete na
https://cla.microsoft.com.

Keď odošlete pull request, CLA-bot automaticky určí, či potrebujete
poskytnúť CLA a označí PR vhodne (napr. štítok, komentár). Jednoducho postupujte podľa
pokynov poskytnutých botom. Toto budete musieť urobiť iba raz vo všetkých repozitároch používajúcich našu CLA.

## Otázky?

- Skontrolujte náš [Discord kanál #data-science-for-beginners](https://aka.ms/ds4beginners/discord)
- Pripojte sa k našej [Discord komunite](https://aka.ms/ds4beginners/discord)
- Prezrite si existujúce [problémy](https://github.com/microsoft/Data-Science-For-Beginners/issues) a [pull requesty](https://github.com/microsoft/Data-Science-For-Beginners/pulls)

## Ďakujeme!

Vaše príspevky zlepšujú tieto učebné osnovy pre všetkých. Ďakujeme, že ste si našli čas na prispievanie!

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.