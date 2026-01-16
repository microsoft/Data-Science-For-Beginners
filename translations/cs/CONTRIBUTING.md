<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T14:31:12+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "cs"
}
-->
# Přispívání do Data Science pro začátečníky

Děkujeme za váš zájem o přispění do kurikula Data Science pro začátečníky! Uvítáme příspěvky od komunity.

## Obsah

- [Kodex chování](../..)
- [Jak mohu přispět?](../..)
- [Začínáme](../..)
- [Pokyny pro přispívání](../..)
- [Proces pull requestu](../..)
- [Pokyny pro styl](../..)
- [Dohoda o licenci přispěvatele](../..)

## Kodex chování

Tento projekt přijal [Kodex chování Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/).
Pro více informací si přečtěte [FAQ ke kodexu chování](https://opensource.microsoft.com/codeofconduct/faq/)
nebo kontaktujte [opencode@microsoft.com](mailto:opencode@microsoft.com) s dalšími dotazy nebo připomínkami.

## Jak mohu přispět?

### Hlášení chyb

Než vytvoříte hlášení o chybě, zkontrolujte existující problémy, abyste se vyhnuli duplicitám. Při vytváření hlášení o chybě uveďte co nejvíce podrobností:

- **Použijte jasný a popisný název**
- **Popište přesné kroky k reprodukci problému**
- **Uveďte konkrétní příklady** (ukázky kódu, snímky obrazovky)
- **Popište chování, které jste pozorovali, a co jste očekávali**
- **Uveďte podrobnosti o vašem prostředí** (OS, verze Pythonu, prohlížeč)

### Návrhy na vylepšení

Návrhy na vylepšení jsou vítány! Při navrhování vylepšení:

- **Použijte jasný a popisný název**
- **Poskytněte podrobný popis navrhovaného vylepšení**
- **Vysvětlete, proč by toto vylepšení bylo užitečné**
- **Uveďte podobné funkce v jiných projektech, pokud je to relevantní**

### Přispívání do dokumentace

Vylepšení dokumentace jsou vždy oceněna:

- **Opravte překlepy a gramatické chyby**
- **Zlepšete srozumitelnost vysvětlení**
- **Doplňte chybějící dokumentaci**
- **Aktualizujte zastaralé informace**
- **Přidejte příklady nebo případy použití**

### Přispívání kódem

Uvítáme příspěvky kódu, včetně:

- **Nových lekcí nebo cvičení**
- **Oprav chyb**
- **Vylepšení stávajících notebooků**
- **Nových datových sad nebo příkladů**
- **Vylepšení aplikace pro kvízy**

## Začínáme

### Předpoklady

Než začnete přispívat, ujistěte se, že máte:

1. Účet na GitHubu
2. Git nainstalovaný na vašem systému
3. Python 3.7+ a Jupyter nainstalovaný
4. Node.js a npm (pro příspěvky do aplikace pro kvízy)
5. Znalost struktury kurikula

Podrobné pokyny k nastavení najdete v [INSTALLATION.md](INSTALLATION.md).

### Fork a klonování

1. **Forkněte repozitář** na GitHubu
2. **Klonujte svůj fork** lokálně:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
3. **Přidejte upstream remote**:
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```

### Vytvoření větve

Vytvořte novou větev pro svou práci:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Konvence pojmenování větví:
- `feature/` - Nové funkce nebo lekce
- `fix/` - Opravy chyb
- `docs/` - Změny v dokumentaci
- `refactor/` - Refaktorizace kódu

## Pokyny pro přispívání

### Pro obsah lekcí

Při přispívání lekcí nebo úpravách stávajících:

1. **Dodržujte stávající strukturu**:
   - README.md s obsahem lekce
   - Jupyter notebook s cvičeními
   - Zadání (pokud je relevantní)
   - Odkaz na před a po kvízy

2. **Zahrňte tyto prvky**:
   - Jasné vzdělávací cíle
   - Postupné vysvětlení
   - Ukázky kódu s komentáři
   - Cvičení pro procvičení
   - Odkazy na další zdroje

3. **Zajistěte přístupnost**:
   - Používejte jasný, jednoduchý jazyk
   - Poskytněte alt text pro obrázky
   - Zahrňte komentáře ke kódu
   - Zvažte různé styly učení

### Pro Jupyter notebooky

1. **Vymažte všechny výstupy** před commitováním:
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```

2. **Zahrňte markdown buňky** s vysvětlením

3. **Používejte konzistentní formátování**:
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```

4. **Otestujte svůj notebook** kompletně před odesláním

### Pro Python kód

Dodržujte pokyny stylu [PEP 8](https://www.python.org/dev/peps/pep-0008/):

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

### Pro příspěvky do aplikace pro kvízy

Při úpravách aplikace pro kvízy:

1. **Testujte lokálně**:
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```

2. **Spusťte linter**:
   ```bash
   npm run lint
   ```

3. **Úspěšně sestavte**:
   ```bash
   npm run build
   ```

4. **Dodržujte stylový průvodce Vue.js** a stávající vzory

### Pro překlady

Při přidávání nebo aktualizaci překladů:

1. Dodržujte strukturu ve složce `translations/`
2. Použijte kód jazyka jako název složky (např. `fr` pro francouzštinu)
3. Zachovejte stejnou strukturu souborů jako anglická verze
4. Aktualizujte odkazy na kvízy, aby obsahovaly parametr jazyka: `?loc=fr`
5. Otestujte všechny odkazy a formátování

## Proces pull requestu

### Před odesláním

1. **Aktualizujte svou větev** s nejnovějšími změnami:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Otestujte své změny**:
   - Spusťte všechny upravené notebooky
   - Otestujte aplikaci pro kvízy, pokud byla upravena
   - Ověřte funkčnost všech odkazů
   - Zkontrolujte pravopisné a gramatické chyby

3. **Commitujte své změny**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   Pište jasné zprávy commitů:
   - Používejte přítomný čas ("Přidat funkci" místo "Přidána funkce")
   - Používejte imperativní způsob ("Přesuň kurzor na..." místo "Přesouvá kurzor na...")
   - Omezte první řádek na 72 znaků
   - Odkazujte na problémy a pull requesty, pokud je to relevantní

4. **Pushněte na svůj fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

### Vytvoření pull requestu

1. Přejděte na [repozitář](https://github.com/microsoft/Data-Science-For-Beginners)
2. Klikněte na "Pull requests" → "New pull request"
3. Klikněte na "compare across forks"
4. Vyberte svůj fork a větev
5. Klikněte na "Create pull request"

### Formát názvu PR

Používejte jasné, popisné názvy podle tohoto formátu:

```
[Component] Brief description
```

Příklady:
- `[Lekce 7] Oprava chyby importu v Python notebooku`
- `[Aplikace pro kvízy] Přidání německého překladu`
- `[Dokumentace] Aktualizace README s novými předpoklady`
- `[Oprava] Oprava cesty k datům v lekci vizualizace`

### Popis PR

Do popisu PR zahrňte:

- **Co**: Jaké změny jste provedli?
- **Proč**: Proč jsou tyto změny nutné?
- **Jak**: Jak jste změny implementovali?
- **Testování**: Jak jste změny otestovali?
- **Snímky obrazovky**: Přidejte snímky obrazovky pro vizuální změny
- **Související problémy**: Odkaz na související problémy (např. "Fixes #123")

### Proces recenze

1. **Automatické kontroly** budou spuštěny na vašem PR
2. **Správci zkontrolují** váš příspěvek
3. **Zpracujte zpětnou vazbu** vytvořením dalších commitů
4. Po schválení **správce sloučí** váš PR

### Po sloučení vašeho PR

1. Smažte svou větev:
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```

2. Aktualizujte svůj fork:
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

## Pokyny pro styl

### Markdown

- Používejte konzistentní úrovně nadpisů
- Vkládejte prázdné řádky mezi sekce
- Používejte bloky kódu s určením jazyka:
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
- Přidávejte alt text k obrázkům: `![Alt text](../../translated_images/cs/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.png)`
- Udržujte rozumnou délku řádků (kolem 80-100 znaků)

### Python

- Dodržujte stylový průvodce PEP 8
- Používejte smysluplné názvy proměnných
- Přidávejte docstringy k funkcím
- Zahrňte typové anotace, kde je to vhodné:
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```

### JavaScript/Vue.js

- Dodržujte stylový průvodce Vue.js 2
- Používejte poskytnutou konfiguraci ESLint
- Pište modulární, znovupoužitelné komponenty
- Přidávejte komentáře ke složité logice

### Organizace souborů

- Uchovávejte související soubory pohromadě
- Používejte popisné názvy souborů
- Dodržujte stávající strukturu adresářů
- Necommitujte zbytečné soubory (.DS_Store, .pyc, node_modules, atd.)

## Dohoda o licenci přispěvatele

Tento projekt vítá příspěvky a návrhy. Většina příspěvků vyžaduje, abyste
souhlasili s Dohodou o licenci přispěvatele (CLA), která deklaruje, že máte právo
a skutečně udělujete práva k použití vašeho příspěvku. Podrobnosti najdete na
https://cla.microsoft.com.

Když odešlete pull request, CLA-bot automaticky určí, zda je potřeba
poskytnout CLA, a příslušně označí PR (např. štítek, komentář). Jednoduše postupujte podle
pokynů poskytnutých botem. Toto budete muset udělat pouze jednou napříč všemi repozitáři, které používají naši CLA.

## Dotazy?

- Zkontrolujte náš [Discord kanál #data-science-for-beginners](https://aka.ms/ds4beginners/discord)
- Připojte se k naší [Discord komunitě](https://aka.ms/ds4beginners/discord)
- Projděte existující [problémy](https://github.com/microsoft/Data-Science-For-Beginners/issues) a [pull requesty](https://github.com/microsoft/Data-Science-For-Beginners/pulls)

## Děkujeme!

Vaše příspěvky zlepšují toto kurikulum pro všechny. Děkujeme, že jste si našli čas na přispění!

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.