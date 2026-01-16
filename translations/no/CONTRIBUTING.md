<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T14:10:41+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "no"
}
-->
# Bidra til Data Science for Beginners

Takk for din interesse for å bidra til Data Science for Beginners-kurset! Vi ønsker bidrag fra fellesskapet velkommen.

## Innholdsfortegnelse

- [Regler for oppførsel](../..)
- [Hvordan kan jeg bidra?](../..)
- [Kom i gang](../..)
- [Retningslinjer for bidrag](../..)
- [Prosess for pull requests](../..)
- [Stilretningslinjer](../..)
- [Bidragsyterlisensavtale](../..)

## Regler for oppførsel

Dette prosjektet har vedtatt [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
For mer informasjon, se [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)  
eller kontakt [opencode@microsoft.com](mailto:opencode@microsoft.com) med eventuelle spørsmål eller kommentarer.

## Hvordan kan jeg bidra?

### Rapportere feil

Før du oppretter feilrapporter, sjekk eksisterende saker for å unngå duplikater. Når du lager en feilrapport, inkluder så mange detaljer som mulig:

- **Bruk en klar og beskrivende tittel**
- **Beskriv de nøyaktige trinnene for å gjenskape problemet**
- **Gi spesifikke eksempler** (kodebiter, skjermbilder)
- **Beskriv oppførselen du observerte og hva du forventet**
- **Inkluder detaljer om miljøet ditt** (OS, Python-versjon, nettleser)

### Foreslå forbedringer

Forslag til forbedringer er velkomne! Når du foreslår forbedringer:

- **Bruk en klar og beskrivende tittel**
- **Gi en detaljert beskrivelse av den foreslåtte forbedringen**
- **Forklar hvorfor denne forbedringen vil være nyttig**
- **List opp lignende funksjoner i andre prosjekter, hvis aktuelt**

### Bidra til dokumentasjon

Forbedringer av dokumentasjonen er alltid verdsatt:

- **Rett opp skrivefeil og grammatiske feil**
- **Forbedre klarheten i forklaringer**
- **Legg til manglende dokumentasjon**
- **Oppdater utdatert informasjon**
- **Legg til eksempler eller brukstilfeller**

### Bidra med kode

Vi ønsker kodebidrag velkommen, inkludert:

- **Nye leksjoner eller øvelser**
- **Feilrettinger**
- **Forbedringer av eksisterende notatbøker**
- **Nye datasett eller eksempler**
- **Forbedringer av quiz-applikasjonen**

## Kom i gang

### Forutsetninger

Før du bidrar, sørg for at du har:

1. En GitHub-konto
2. Git installert på systemet ditt
3. Python 3.7+ og Jupyter installert
4. Node.js og npm (for bidrag til quiz-appen)
5. Kjennskap til kursstrukturen

Se [INSTALLATION.md](INSTALLATION.md) for detaljerte installasjonsinstruksjoner.

### Fork og klon

1. **Fork repository** på GitHub  
2. **Klon din fork** lokalt:  
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
  
3. **Legg til upstream remote**:  
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```
  

### Opprett en gren

Opprett en ny gren for arbeidet ditt:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```
  
Navnekonvensjoner for grener:  
- `feature/` - Nye funksjoner eller leksjoner  
- `fix/` - Feilrettinger  
- `docs/` - Dokumentasjonsendringer  
- `refactor/` - Omstrukturering av kode  

## Retningslinjer for bidrag

### For leksjonsinnhold

Når du bidrar med leksjoner eller endrer eksisterende:

1. **Følg den eksisterende strukturen**:  
   - README.md med leksjonsinnhold  
   - Jupyter-notatbok med øvelser  
   - Oppgave (hvis aktuelt)  
   - Lenke til quiz før og etter leksjonen  

2. **Inkluder disse elementene**:  
   - Klare læringsmål  
   - Trinnvise forklaringer  
   - Kodeeksempler med kommentarer  
   - Øvelser for praksis  
   - Lenker til ekstra ressurser  

3. **Sørg for tilgjengelighet**:  
   - Bruk klart, enkelt språk  
   - Gi alt-tekst for bilder  
   - Inkluder kodekommentarer  
   - Ta hensyn til ulike læringsstiler  

### For Jupyter-notatbøker

1. **Tøm alle utdata** før du committer:  
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```
  
2. **Inkluder markdown-celler** med forklaringer  

3. **Bruk konsekvent formatering**:  
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```
  
4. **Test notatboken** fullstendig før innsending  

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
  

### For bidrag til quiz-appen

Når du endrer quiz-applikasjonen:

1. **Test lokalt**:  
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```
  
2. **Kjør linter**:  
   ```bash
   npm run lint
   ```
  
3. **Bygg vellykket**:  
   ```bash
   npm run build
   ```
  
4. **Følg Vue.js stilguide** og eksisterende mønstre  

### For oversettelser

Når du legger til eller oppdaterer oversettelser:

1. Følg strukturen i `translations/`-mappen  
2. Bruk språkkoden som mappenavn (f.eks. `fr` for fransk)  
3. Oppretthold samme filstruktur som den engelske versjonen  
4. Oppdater quiz-lenker for å inkludere språkparameter: `?loc=fr`  
5. Test alle lenker og formatering  

## Prosess for pull requests

### Før innsending

1. **Oppdater grenen din** med de nyeste endringene:  
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```
  
2. **Test endringene dine**:  
   - Kjør alle endrede notatbøker  
   - Test quiz-appen hvis den er endret  
   - Verifiser at alle lenker fungerer  
   - Sjekk for skrivefeil og grammatiske feil  

3. **Commit endringene dine**:  
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
  
   Skriv klare commit-meldinger:  
   - Bruk nåtid ("Legg til funksjon" ikke "La til funksjon")  
   - Bruk imperativ form ("Flytt markøren til..." ikke "Flytter markøren til...")  
   - Begrens første linje til 72 tegn  
   - Referer til saker og pull requests når relevant  

4. **Push til din fork**:  
   ```bash
   git push origin feature/your-feature-name
   ```
  

### Opprette pull request

1. Gå til [repository](https://github.com/microsoft/Data-Science-For-Beginners)  
2. Klikk "Pull requests" → "New pull request"  
3. Klikk "compare across forks"  
4. Velg din fork og gren  
5. Klikk "Create pull request"  

### Format for PR-tittel

Bruk klare, beskrivende titler med følgende format:

```
[Component] Brief description
```
  
Eksempler:  
- `[Lesson 7] Rett Python-notatbok importfeil`  
- `[Quiz App] Legg til tysk oversettelse`  
- `[Docs] Oppdater README med nye forutsetninger`  
- `[Fix] Korriger datapath i visualiseringsleksjon`  

### PR-beskrivelse

Inkluder i PR-beskrivelsen:

- **Hva**: Hvilke endringer har du gjort?  
- **Hvorfor**: Hvorfor er disse endringene nødvendige?  
- **Hvordan**: Hvordan implementerte du endringene?  
- **Testing**: Hvordan testet du endringene?  
- **Skjermbilder**: Inkluder skjermbilder for visuelle endringer  
- **Relaterte saker**: Lenke til relaterte saker (f.eks. "Fixes #123")  

### Gjennomgangsprosess

1. **Automatiske sjekker** vil kjøre på din PR  
2. **Vedlikeholdere vil gjennomgå** bidraget ditt  
3. **Svar på tilbakemeldinger** ved å gjøre ytterligere commits  
4. Når godkjent, vil en **vedlikeholder merge** din PR  

### Etter at PR-en din er merget

1. Slett grenen din:  
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```
  
2. Oppdater din fork:  
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```
  

## Stilretningslinjer

### Markdown

- Bruk konsekvente overskriftsnivåer  
- Inkluder tomme linjer mellom seksjoner  
- Bruk kodeblokker med språkspesifikasjoner:  
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
  
- Legg til alt-tekst til bilder: `![Alt-tekst](../../translated_images/no/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.png)`  
- Hold linjelengder rimelige (rundt 80-100 tegn)  

### Python

- Følg PEP 8 stilguide  
- Bruk meningsfulle variabelnavn  
- Legg til docstrings til funksjoner  
- Inkluder type hints der det er passende:  
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```
  

### JavaScript/Vue.js

- Følg Vue.js 2 stilguide  
- Bruk den medfølgende ESLint-konfigurasjonen  
- Skriv modulære, gjenbrukbare komponenter  
- Legg til kommentarer for kompleks logikk  

### Filorganisering

- Hold relaterte filer samlet  
- Bruk beskrivende filnavn  
- Følg eksisterende katalogstruktur  
- Ikke commit unødvendige filer (.DS_Store, .pyc, node_modules, etc.)  

## Bidragsyterlisensavtale

Dette prosjektet ønsker bidrag og forslag velkommen. De fleste bidrag krever at du  
godtar en Bidragsyterlisensavtale (CLA) som erklærer at du har rett til,  
og faktisk gir oss rettighetene til å bruke ditt bidrag. For detaljer, besøk  
https://cla.microsoft.com.

Når du sender inn en pull request, vil en CLA-bot automatisk avgjøre om du trenger  
å gi en CLA og dekorere PR-en deretter (f.eks. etikett, kommentar). Følg bare  
instruksjonene gitt av boten. Du trenger bare å gjøre dette én gang på tvers av alle repositories som bruker vår CLA.

## Spørsmål?

- Sjekk vår [Discord-kanal #data-science-for-beginners](https://aka.ms/ds4beginners/discord)  
- Bli med i vårt [Discord-fellesskap](https://aka.ms/ds4beginners/discord)  
- Gå gjennom eksisterende [saker](https://github.com/microsoft/Data-Science-For-Beginners/issues) og [pull requests](https://github.com/microsoft/Data-Science-For-Beginners/pulls)  

## Takk!

Dine bidrag gjør dette kurset bedre for alle. Takk for at du tar deg tid til å bidra!

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.