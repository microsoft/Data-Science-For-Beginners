<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T14:13:43+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "nl"
}
-->
# Bijdragen aan Data Science voor Beginners

Bedankt voor je interesse om bij te dragen aan het curriculum Data Science voor Beginners! We verwelkomen bijdragen van de gemeenschap.

## Inhoudsopgave

- [Gedragscode](../..)
- [Hoe kan ik bijdragen?](../..)
- [Aan de slag](../..)
- [Richtlijnen voor bijdragen](../..)
- [Pull Request-proces](../..)
- [Stijlrichtlijnen](../..)
- [Contributor License Agreement](../..)

## Gedragscode

Dit project hanteert de [Microsoft Open Source Gedragscode](https://opensource.microsoft.com/codeofconduct/).  
Voor meer informatie, zie de [FAQ over de gedragscode](https://opensource.microsoft.com/codeofconduct/faq/)  
of neem contact op via [opencode@microsoft.com](mailto:opencode@microsoft.com) voor aanvullende vragen of opmerkingen.

## Hoe kan ik bijdragen?

### Bugs rapporteren

Voordat je een bugrapport aanmaakt, controleer eerst de bestaande issues om duplicaten te voorkomen. Wanneer je een bugrapport aanmaakt, geef zoveel mogelijk details:

- **Gebruik een duidelijke en beschrijvende titel**
- **Beschrijf de exacte stappen om het probleem te reproduceren**
- **Geef specifieke voorbeelden** (codefragmenten, screenshots)
- **Beschrijf het waargenomen gedrag en wat je verwachtte**
- **Geef details over je omgeving** (OS, Python-versie, browser)

### Verbeteringen voorstellen

Suggesties voor verbeteringen zijn altijd welkom! Bij het voorstellen van verbeteringen:

- **Gebruik een duidelijke en beschrijvende titel**
- **Geef een gedetailleerde beschrijving van de voorgestelde verbetering**
- **Leg uit waarom deze verbetering nuttig zou zijn**
- **Noem vergelijkbare functies in andere projecten, indien van toepassing**

### Bijdragen aan documentatie

Verbeteringen aan de documentatie worden altijd gewaardeerd:

- **Corrigeer typfouten en grammaticale fouten**
- **Verbeter de duidelijkheid van uitleg**
- **Voeg ontbrekende documentatie toe**
- **Werk verouderde informatie bij**
- **Voeg voorbeelden of gebruiksscenario's toe**

### Code bijdragen

We verwelkomen codebijdragen, waaronder:

- **Nieuwe lessen of oefeningen**
- **Bugfixes**
- **Verbeteringen aan bestaande notebooks**
- **Nieuwe datasets of voorbeelden**
- **Verbeteringen aan de quizapplicatie**

## Aan de slag

### Vereisten

Voordat je bijdraagt, zorg ervoor dat je het volgende hebt:

1. Een GitHub-account  
2. Git geïnstalleerd op je systeem  
3. Python 3.7+ en Jupyter geïnstalleerd  
4. Node.js en npm (voor bijdragen aan de quizapplicatie)  
5. Bekendheid met de structuur van het curriculum  

Zie [INSTALLATION.md](INSTALLATION.md) voor gedetailleerde installatie-instructies.

### Fork en Clone

1. **Fork de repository** op GitHub  
2. **Clone je fork** lokaal:  
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
  
3. **Voeg upstream remote toe**:  
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```
  

### Maak een branch

Maak een nieuwe branch voor je werk:  
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```
  
Branch naamconventies:  
- `feature/` - Nieuwe functies of lessen  
- `fix/` - Bugfixes  
- `docs/` - Documentatiewijzigingen  
- `refactor/` - Codeherstructurering  

## Richtlijnen voor bijdragen

### Voor lesinhoud

Bij het bijdragen van lessen of het wijzigen van bestaande lessen:

1. **Volg de bestaande structuur**:  
   - README.md met lesinhoud  
   - Jupyter-notebook met oefeningen  
   - Opdracht (indien van toepassing)  
   - Link naar pre- en postquizzen  

2. **Voeg deze elementen toe**:  
   - Duidelijke leerdoelen  
   - Stapsgewijze uitleg  
   - Codevoorbeelden met opmerkingen  
   - Oefeningen om te oefenen  
   - Links naar aanvullende bronnen  

3. **Zorg voor toegankelijkheid**:  
   - Gebruik duidelijke, eenvoudige taal  
   - Voeg alt-tekst toe aan afbeeldingen  
   - Voeg codeopmerkingen toe  
   - Houd rekening met verschillende leerstijlen  

### Voor Jupyter-notebooks

1. **Wis alle uitvoer** voordat je commit:  
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```
  
2. **Voeg markdown-cellen toe** met uitleg  

3. **Gebruik consistente opmaak**:  
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```
  
4. **Test je notebook** volledig voordat je deze indient  

### Voor Python-code

Volg de [PEP 8](https://www.python.org/dev/peps/pep-0008/) stijlrichtlijnen:  
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
  

### Voor bijdragen aan de quizapplicatie

Bij het wijzigen van de quizapplicatie:

1. **Test lokaal**:  
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```
  
2. **Voer linter uit**:  
   ```bash
   npm run lint
   ```
  
3. **Bouw succesvol**:  
   ```bash
   npm run build
   ```
  
4. **Volg de Vue.js stijlrichtlijnen** en bestaande patronen  

### Voor vertalingen

Bij het toevoegen of bijwerken van vertalingen:

1. Volg de structuur in de map `translations/`  
2. Gebruik de taalcode als mapnaam (bijv. `fr` voor Frans)  
3. Behoud dezelfde bestandsstructuur als de Engelse versie  
4. Werk quizlinks bij om de taalparameter op te nemen: `?loc=fr`  
5. Test alle links en opmaak  

## Pull Request-proces

### Voordat je indient

1. **Werk je branch bij** met de laatste wijzigingen:  
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```
  
2. **Test je wijzigingen**:  
   - Voer alle gewijzigde notebooks uit  
   - Test de quizapplicatie indien gewijzigd  
   - Controleer of alle links werken  
   - Controleer op spelling- en grammaticafouten  

3. **Commit je wijzigingen**:  
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
  
   Schrijf duidelijke commitberichten:  
   - Gebruik de tegenwoordige tijd ("Voeg functie toe" in plaats van "Functie toegevoegd")  
   - Gebruik de gebiedende wijs ("Verplaats cursor naar..." in plaats van "Verplaatst cursor naar...")  
   - Beperk de eerste regel tot 72 tekens  
   - Verwijs naar issues en pull requests indien relevant  

4. **Push naar je fork**:  
   ```bash
   git push origin feature/your-feature-name
   ```
  

### Een Pull Request aanmaken

1. Ga naar de [repository](https://github.com/microsoft/Data-Science-For-Beginners)  
2. Klik op "Pull requests" → "New pull request"  
3. Klik op "compare across forks"  
4. Selecteer je fork en branch  
5. Klik op "Create pull request"  

### PR Titel Formaat

Gebruik duidelijke, beschrijvende titels volgens dit formaat:  
```
[Component] Brief description
```
  
Voorbeelden:  
- `[Les 7] Fix Python-notebook importfout`  
- `[Quiz App] Voeg Duitse vertaling toe`  
- `[Docs] Update README met nieuwe vereisten`  
- `[Fix] Corrigeer datapad in visualisatieles`  

### PR Beschrijving

Neem in je PR-beschrijving op:

- **Wat**: Welke wijzigingen heb je aangebracht?  
- **Waarom**: Waarom zijn deze wijzigingen nodig?  
- **Hoe**: Hoe heb je de wijzigingen geïmplementeerd?  
- **Testen**: Hoe heb je de wijzigingen getest?  
- **Screenshots**: Voeg screenshots toe voor visuele wijzigingen  
- **Gerelateerde issues**: Link naar gerelateerde issues (bijv. "Fixes #123")  

### Reviewproces

1. **Automatische controles** worden uitgevoerd op je PR  
2. **Maintainers zullen je bijdrage beoordelen**  
3. **Verwerk feedback** door aanvullende commits te maken  
4. Zodra goedgekeurd, zal een **maintainer je PR mergen**  

### Nadat je PR is gemerged

1. Verwijder je branch:  
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```
  
2. Werk je fork bij:  
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```
  

## Stijlrichtlijnen

### Markdown

- Gebruik consistente kopniveaus  
- Voeg lege regels toe tussen secties  
- Gebruik codeblokken met taalspecificaties:  
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
  
- Voeg alt-tekst toe aan afbeeldingen: `![Alt-tekst](../../translated_images/nl/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.png)`  
- Houd de regellengte redelijk (ongeveer 80-100 tekens)  

### Python

- Volg de PEP 8 stijlrichtlijnen  
- Gebruik betekenisvolle variabelenamen  
- Voeg docstrings toe aan functies  
- Voeg type hints toe waar nodig:  
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```
  

### JavaScript/Vue.js

- Volg de Vue.js 2 stijlrichtlijnen  
- Gebruik de meegeleverde ESLint-configuratie  
- Schrijf modulaire, herbruikbare componenten  
- Voeg opmerkingen toe voor complexe logica  

### Bestandsorganisatie

- Houd gerelateerde bestanden bij elkaar  
- Gebruik beschrijvende bestandsnamen  
- Volg de bestaande mapstructuur  
- Commit geen onnodige bestanden (.DS_Store, .pyc, node_modules, etc.)  

## Contributor License Agreement

Dit project verwelkomt bijdragen en suggesties. De meeste bijdragen vereisen dat je akkoord gaat met een Contributor License Agreement (CLA) waarin je verklaart dat je het recht hebt om, en daadwerkelijk doet, ons de rechten te geven om je bijdrage te gebruiken. Voor details, bezoek  
https://cla.microsoft.com.

Wanneer je een pull request indient, zal een CLA-bot automatisch bepalen of je een CLA moet indienen en de PR dienovereenkomstig voorzien van een label of opmerking. Volg gewoon de instructies van de bot. Je hoeft dit slechts één keer te doen voor alle repositories die onze CLA gebruiken.

## Vragen?

- Bekijk ons [Discord-kanaal #data-science-for-beginners](https://aka.ms/ds4beginners/discord)  
- Word lid van onze [Discord-community](https://aka.ms/ds4beginners/discord)  
- Bekijk bestaande [issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) en [pull requests](https://github.com/microsoft/Data-Science-For-Beginners/pulls)  

## Bedankt!

Jouw bijdragen maken dit curriculum beter voor iedereen. Bedankt dat je de tijd neemt om bij te dragen!

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.