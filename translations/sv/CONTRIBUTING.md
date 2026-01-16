<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T14:06:35+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sv"
}
-->
# Bidra till Data Science för Nybörjare

Tack för ditt intresse av att bidra till Data Science för Nybörjare-kursen! Vi välkomnar bidrag från communityn.

## Innehållsförteckning

- [Uppförandekod](../..)
- [Hur kan jag bidra?](../..)
- [Komma igång](../..)
- [Riktlinjer för bidrag](../..)
- [Process för pull requests](../..)
- [Stilriktlinjer](../..)
- [Licensavtal för bidragsgivare](../..)

## Uppförandekod

Det här projektet har antagit [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
För mer information, se [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
eller kontakta [opencode@microsoft.com](mailto:opencode@microsoft.com) med ytterligare frågor eller kommentarer.

## Hur kan jag bidra?

### Rapportera buggar

Innan du skapar en buggrapport, kontrollera befintliga ärenden för att undvika dubbletter. När du skapar en buggrapport, inkludera så många detaljer som möjligt:

- **Använd en tydlig och beskrivande titel**
- **Beskriv de exakta stegen för att återskapa problemet**
- **Ge specifika exempel** (kodsnuttar, skärmdumpar)
- **Beskriv det beteende du observerade och vad du förväntade dig**
- **Inkludera detaljer om din miljö** (OS, Python-version, webbläsare)

### Föreslå förbättringar

Förslag på förbättringar är välkomna! När du föreslår förbättringar:

- **Använd en tydlig och beskrivande titel**
- **Ge en detaljerad beskrivning av den föreslagna förbättringen**
- **Förklara varför denna förbättring skulle vara användbar**
- **Lista eventuella liknande funktioner i andra projekt, om tillämpligt**

### Bidra till dokumentation

Förbättringar av dokumentationen uppskattas alltid:

- **Rätta stavfel och grammatiska fel**
- **Förbättra tydligheten i förklaringar**
- **Lägg till saknad dokumentation**
- **Uppdatera föråldrad information**
- **Lägg till exempel eller användningsfall**

### Bidra med kod

Vi välkomnar kodbidrag, inklusive:

- **Nya lektioner eller övningar**
- **Buggrättningar**
- **Förbättringar av befintliga notebooks**
- **Nya dataset eller exempel**
- **Förbättringar av quiz-applikationen**

## Komma igång

### Förutsättningar

Innan du bidrar, se till att du har:

1. Ett GitHub-konto
2. Git installerat på ditt system
3. Python 3.7+ och Jupyter installerat
4. Node.js och npm (för bidrag till quiz-appen)
5. Kunskap om kursens struktur

Se [INSTALLATION.md](INSTALLATION.md) för detaljerade installationsinstruktioner.

### Forka och klona

1. **Forka repot** på GitHub
2. **Klona din fork** lokalt:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
3. **Lägg till upstream remote**:
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```

### Skapa en gren

Skapa en ny gren för ditt arbete:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Grennamns-konventioner:
- `feature/` - Nya funktioner eller lektioner
- `fix/` - Buggrättningar
- `docs/` - Dokumentationsändringar
- `refactor/` - Kodomstrukturering

## Riktlinjer för bidrag

### För lektionsinnehåll

När du bidrar med lektioner eller ändrar befintliga:

1. **Följ den befintliga strukturen**:
   - README.md med lektionsinnehåll
   - Jupyter-notebook med övningar
   - Uppgift (om tillämpligt)
   - Länk till quiz före och efter lektionen

2. **Inkludera dessa element**:
   - Tydliga lärandemål
   - Steg-för-steg-förklaringar
   - Kodexempel med kommentarer
   - Övningar för träning
   - Länkar till ytterligare resurser

3. **Säkerställ tillgänglighet**:
   - Använd tydligt, enkelt språk
   - Ge alt-text för bilder
   - Inkludera kodkommentarer
   - Tänk på olika inlärningsstilar

### För Jupyter-notebooks

1. **Rensa alla outputs** innan du commitar:
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```

2. **Inkludera markdown-celler** med förklaringar

3. **Använd konsekvent formatering**:
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```

4. **Testa din notebook** helt innan du skickar in

### För Python-kod

Följ [PEP 8](https://www.python.org/dev/peps/pep-0008/) stilriktlinjer:

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

### För quiz-app-bidrag

När du ändrar quiz-applikationen:

1. **Testa lokalt**:
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```

2. **Kör linter**:
   ```bash
   npm run lint
   ```

3. **Bygg framgångsrikt**:
   ```bash
   npm run build
   ```

4. **Följ Vue.js stilguide** och befintliga mönster

### För översättningar

När du lägger till eller uppdaterar översättningar:

1. Följ strukturen i `translations/`-mappen
2. Använd språkkoden som mappnamn (t.ex. `fr` för franska)
3. Behåll samma filstruktur som den engelska versionen
4. Uppdatera quiz-länkar för att inkludera språkparameter: `?loc=fr`
5. Testa alla länkar och formatering

## Process för pull requests

### Innan du skickar in

1. **Uppdatera din gren** med de senaste ändringarna:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Testa dina ändringar**:
   - Kör alla modifierade notebooks
   - Testa quiz-appen om den ändrats
   - Kontrollera att alla länkar fungerar
   - Kontrollera stavning och grammatik

3. **Commit dina ändringar**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   Skriv tydliga commit-meddelanden:
   - Använd presens ("Lägg till funktion" inte "Lade till funktion")
   - Använd imperativ form ("Flytta markören till..." inte "Flyttar markören till...")
   - Begränsa första raden till 72 tecken
   - Referera till ärenden och pull requests när det är relevant

4. **Push till din fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

### Skapa pull request

1. Gå till [repot](https://github.com/microsoft/Data-Science-For-Beginners)
2. Klicka på "Pull requests" → "New pull request"
3. Klicka på "compare across forks"
4. Välj din fork och gren
5. Klicka på "Create pull request"

### Format för PR-titel

Använd tydliga, beskrivande titlar enligt detta format:

```
[Component] Brief description
```

Exempel:
- `[Lektion 7] Rätta importfel i Python-notebook`
- `[Quiz App] Lägg till tysk översättning`
- `[Docs] Uppdatera README med nya förutsättningar`
- `[Fix] Korrigera datapath i visualiseringslektionen`

### PR-beskrivning

Inkludera i din PR-beskrivning:

- **Vad**: Vilka ändringar har du gjort?
- **Varför**: Varför är dessa ändringar nödvändiga?
- **Hur**: Hur implementerade du ändringarna?
- **Testning**: Hur testade du ändringarna?
- **Skärmdumpar**: Inkludera skärmdumpar för visuella ändringar
- **Relaterade ärenden**: Länka till relaterade ärenden (t.ex. "Fixes #123")

### Granskningsprocess

1. **Automatiska kontroller** kommer att köras på din PR
2. **Maintainers kommer att granska** ditt bidrag
3. **Åtgärda feedback** genom att göra ytterligare commits
4. När det är godkänt, kommer en **maintainer att mergea** din PR

### Efter att din PR har mergeats

1. Ta bort din gren:
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```

2. Uppdatera din fork:
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

## Stilriktlinjer

### Markdown

- Använd konsekventa rubriknivåer
- Inkludera tomma rader mellan sektioner
- Använd kodblock med språkangivelser:
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
- Lägg till alt-text till bilder: `![Alt text](../../translated_images/sv/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.png)`
- Håll linjelängder rimliga (runt 80-100 tecken)

### Python

- Följ PEP 8 stilguide
- Använd meningsfulla variabelnamn
- Lägg till docstrings till funktioner
- Inkludera typanvisningar där det är lämpligt:
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```

### JavaScript/Vue.js

- Följ Vue.js 2 stilguide
- Använd den medföljande ESLint-konfigurationen
- Skriv modulära, återanvändbara komponenter
- Lägg till kommentarer för komplex logik

### Filorganisation

- Håll relaterade filer tillsammans
- Använd beskrivande filnamn
- Följ befintlig katalogstruktur
- Commita inte onödiga filer (.DS_Store, .pyc, node_modules, etc.)

## Licensavtal för bidragsgivare

Det här projektet välkomnar bidrag och förslag. De flesta bidrag kräver att du
godkänner ett Licensavtal för bidragsgivare (CLA) som deklarerar att du har rätt att,
och faktiskt gör, ge oss rättigheterna att använda ditt bidrag. För detaljer, besök
https://cla.microsoft.com.

När du skickar in en pull request, kommer en CLA-bot automatiskt att avgöra om du behöver
tillhandahålla en CLA och dekorera PR:n på lämpligt sätt (t.ex. etikett, kommentar). Följ bara
instruktionerna som tillhandahålls av boten. Du behöver bara göra detta en gång för alla repositories som använder vår CLA.

## Frågor?

- Kolla vår [Discord-kanal #data-science-for-beginners](https://aka.ms/ds4beginners/discord)
- Gå med i vår [Discord-community](https://aka.ms/ds4beginners/discord)
- Granska befintliga [ärenden](https://github.com/microsoft/Data-Science-For-Beginners/issues) och [pull requests](https://github.com/microsoft/Data-Science-For-Beginners/pulls)

## Tack!

Dina bidrag gör denna kurs bättre för alla. Tack för att du tar dig tid att bidra!

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.