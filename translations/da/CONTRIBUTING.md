<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T14:08:06+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "da"
}
-->
# Bidrag til Data Science for Beginners

Tak for din interesse i at bidrage til Data Science for Beginners-kurset! Vi værdsætter bidrag fra fællesskabet.

## Indholdsfortegnelse

- [Adfærdskodeks](../..)
- [Hvordan kan jeg bidrage?](../..)
- [Kom godt i gang](../..)
- [Retningslinjer for bidrag](../..)
- [Pull Request-processen](../..)
- [Stilretningslinjer](../..)
- [Bidragsyderlicensaftale](../..)

## Adfærdskodeks

Dette projekt har vedtaget [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). 
For mere information, se [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) 
eller kontakt [opencode@microsoft.com](mailto:opencode@microsoft.com) med yderligere spørgsmål eller kommentarer.

## Hvordan kan jeg bidrage?

### Rapportering af fejl

Før du opretter fejlrapporter, skal du tjekke de eksisterende issues for at undgå dubletter. Når du opretter en fejlrapport, skal du inkludere så mange detaljer som muligt:

- **Brug en klar og beskrivende titel**
- **Beskriv de præcise trin for at genskabe problemet**
- **Giv specifikke eksempler** (kodeudsnit, skærmbilleder)
- **Beskriv den observerede adfærd og hvad du forventede**
- **Inkluder detaljer om din arbejdsmiljø** (OS, Python-version, browser)

### Foreslå forbedringer

Forslag til forbedringer er velkomne! Når du foreslår forbedringer:

- **Brug en klar og beskrivende titel**
- **Giv en detaljeret beskrivelse af den foreslåede forbedring**
- **Forklar, hvorfor denne forbedring ville være nyttig**
- **List eventuelle lignende funktioner i andre projekter, hvis relevant**

### Bidrag til dokumentation

Forbedringer af dokumentationen er altid værdsat:

- **Ret stavefejl og grammatiske fejl**
- **Forbedr forklaringers klarhed**
- **Tilføj manglende dokumentation**
- **Opdater forældet information**
- **Tilføj eksempler eller brugsscenarier**

### Bidrag med kode

Vi byder kodebidrag velkommen, herunder:

- **Nye lektioner eller øvelser**
- **Fejlrettelser**
- **Forbedringer af eksisterende notebooks**
- **Nye datasæt eller eksempler**
- **Forbedringer af quiz-applikationen**

## Kom godt i gang

### Forudsætninger

Før du bidrager, skal du sikre dig, at du har:

1. En GitHub-konto
2. Git installeret på dit system
3. Python 3.7+ og Jupyter installeret
4. Node.js og npm (til bidrag til quiz-appen)
5. Kendskab til kursusstrukturen

Se [INSTALLATION.md](INSTALLATION.md) for detaljerede installationsinstruktioner.

### Fork og klon

1. **Fork repository** på GitHub
2. **Klon din fork** lokalt:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
3. **Tilføj upstream remote**:
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```

### Opret en branch

Opret en ny branch til dit arbejde:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Branch-navnekonventioner:
- `feature/` - Nye funktioner eller lektioner
- `fix/` - Fejlrettelser
- `docs/` - Dokumentationsændringer
- `refactor/` - Kodeomstrukturering

## Retningslinjer for bidrag

### For lektionsindhold

Når du bidrager med lektioner eller ændrer eksisterende:

1. **Følg den eksisterende struktur**:
   - README.md med lektionsindhold
   - Jupyter-notebook med øvelser
   - Opgave (hvis relevant)
   - Link til før- og efterquizzer

2. **Inkluder disse elementer**:
   - Klare læringsmål
   - Trinvise forklaringer
   - Kodeeksempler med kommentarer
   - Øvelser til praksis
   - Links til yderligere ressourcer

3. **Sikre tilgængelighed**:
   - Brug klart og enkelt sprog
   - Tilføj alt-tekst til billeder
   - Inkluder kodekommentarer
   - Tag hensyn til forskellige læringsstile

### For Jupyter-notebooks

1. **Ryd alle outputs** før du committer:
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```

2. **Inkluder markdown-celler** med forklaringer

3. **Brug konsekvent formatering**:
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```

4. **Test din notebook** fuldstændigt før indsendelse

### For Python-kode

Følg [PEP 8](https://www.python.org/dev/peps/pep-0008/) stilretningslinjer:

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

### For quiz-app-bidrag

Når du ændrer quiz-applikationen:

1. **Test lokalt**:
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```

2. **Kør linter**:
   ```bash
   npm run lint
   ```

3. **Byg succesfuldt**:
   ```bash
   npm run build
   ```

4. **Følg Vue.js stilguide** og eksisterende mønstre

### For oversættelser

Når du tilføjer eller opdaterer oversættelser:

1. Følg strukturen i `translations/`-mappen
2. Brug sprogets kode som mappenavn (f.eks. `fr` for fransk)
3. Bevar samme filstruktur som den engelske version
4. Opdater quiz-links til at inkludere sprogparameter: `?loc=fr`
5. Test alle links og formatering

## Pull Request-processen

### Før indsendelse

1. **Opdater din branch** med de nyeste ændringer:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Test dine ændringer**:
   - Kør alle ændrede notebooks
   - Test quiz-appen, hvis den er ændret
   - Verificer, at alle links fungerer
   - Tjek for stave- og grammatikfejl

3. **Commit dine ændringer**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   Skriv klare commit-beskeder:
   - Brug nutid ("Tilføj funktion" ikke "Tilføjede funktion")
   - Brug imperativ ("Flyt cursor til..." ikke "Flytter cursor til...")
   - Begræns første linje til 72 tegn
   - Referer til issues og pull requests, når det er relevant

4. **Push til din fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

### Opret Pull Request

1. Gå til [repository](https://github.com/microsoft/Data-Science-For-Beginners)
2. Klik på "Pull requests" → "New pull request"
3. Klik på "compare across forks"
4. Vælg din fork og branch
5. Klik på "Create pull request"

### PR-titelformat

Brug klare, beskrivende titler efter dette format:

```
[Component] Brief description
```

Eksempler:
- `[Lektion 7] Ret Python-notebook importfejl`
- `[Quiz App] Tilføj tysk oversættelse`
- `[Docs] Opdater README med nye forudsætninger`
- `[Fix] Ret datasti i visualiseringslektion`

### PR-beskrivelse

Inkluder i din PR-beskrivelse:

- **Hvad**: Hvilke ændringer har du lavet?
- **Hvorfor**: Hvorfor er disse ændringer nødvendige?
- **Hvordan**: Hvordan har du implementeret ændringerne?
- **Test**: Hvordan har du testet ændringerne?
- **Skærmbilleder**: Inkluder skærmbilleder for visuelle ændringer
- **Relaterede issues**: Link til relaterede issues (f.eks. "Fixes #123")

### Review-processen

1. **Automatiske checks** vil køre på din PR
2. **Maintainers vil gennemgå** dit bidrag
3. **Imødekom feedback** ved at lave yderligere commits
4. Når det er godkendt, vil en **maintainer merge** din PR

### Efter din PR er merged

1. Slet din branch:
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```

2. Opdater din fork:
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

## Stilretningslinjer

### Markdown

- Brug konsekvente overskriftsniveauer
- Inkluder blanke linjer mellem sektioner
- Brug kodeblokke med sprogangivelser:
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
- Tilføj alt-tekst til billeder: `![Alt tekst](../../translated_images/da/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.png)`
- Hold linjelængder rimelige (omkring 80-100 tegn)

### Python

- Følg PEP 8 stilguide
- Brug meningsfulde variabelnavne
- Tilføj docstrings til funktioner
- Inkluder type hints, hvor det er passende:
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```

### JavaScript/Vue.js

- Følg Vue.js 2 stilguide
- Brug den medfølgende ESLint-konfiguration
- Skriv modulære, genanvendelige komponenter
- Tilføj kommentarer til kompleks logik

### Filorganisering

- Hold relaterede filer samlet
- Brug beskrivende filnavne
- Følg den eksisterende mappestruktur
- Commit ikke unødvendige filer (.DS_Store, .pyc, node_modules, etc.)

## Bidragsyderlicensaftale

Dette projekt byder bidrag og forslag velkommen. De fleste bidrag kræver, at du 
accepterer en Bidragsyderlicensaftale (CLA), der erklærer, at du har retten til, 
og faktisk giver os rettighederne til at bruge dit bidrag. For detaljer, besøg 
https://cla.microsoft.com.

Når du indsender en pull request, vil en CLA-bot automatisk afgøre, om du skal 
give en CLA og dekorere PR'en passende (f.eks. label, kommentar). Følg blot 
instruktionerne fra botten. Du skal kun gøre dette én gang på tværs af alle repositories, der bruger vores CLA.

## Spørgsmål?

- Tjek vores [Discord-kanal #data-science-for-beginners](https://aka.ms/ds4beginners/discord)
- Deltag i vores [Discord-fællesskab](https://aka.ms/ds4beginners/discord)
- Gennemgå eksisterende [issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) og [pull requests](https://github.com/microsoft/Data-Science-For-Beginners/pulls)

## Tak!

Dine bidrag gør dette kursus bedre for alle. Tak fordi du tager dig tid til at bidrage!

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.