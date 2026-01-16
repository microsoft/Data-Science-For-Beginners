<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-11T15:08:22+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "et"
}
-->
# Panustamine algajate andmeteaduse projekti

Täname, et olete huvitatud panustamisest algajate andmeteaduse õppekavasse! Me tervitame kogukonna panuseid.

## Sisukord

- [Käitumisjuhend](../..)
- [Kuidas saan panustada?](../..)
- [Alustamine](../..)
- [Panustamise juhised](../..)
- [Pull Request'i protsess](../..)
- [Stiilijuhised](../..)
- [Panustaja litsentsileping](../..)

## Käitumisjuhend

See projekt järgib [Microsofti avatud lähtekoodi käitumisjuhendit](https://opensource.microsoft.com/codeofconduct/).  
Lisateabe saamiseks vaadake [käitumisjuhendi KKK-d](https://opensource.microsoft.com/codeofconduct/faq/)  
või võtke ühendust [opencode@microsoft.com](mailto:opencode@microsoft.com), kui teil on lisaküsimusi või kommentaare.

## Kuidas saan panustada?

### Vigade raporteerimine

Enne vigade raportite loomist kontrollige olemasolevaid probleeme, et vältida duplikaate. Kui loote veateate, lisage võimalikult palju üksikasju:

- **Kasutage selget ja kirjeldavat pealkirja**
- **Kirjeldage täpseid samme probleemi taastamiseks**
- **Esitage konkreetseid näiteid** (koodilõigud, ekraanipildid)
- **Kirjeldage täheldatud käitumist ja oodatud tulemust**
- **Lisage oma keskkonna üksikasjad** (OS, Python versioon, brauser)

### Paranduste ettepanekud

Paranduste ettepanekud on teretulnud! Paranduste ettepanekute tegemisel:

- **Kasutage selget ja kirjeldavat pealkirja**
- **Esitage üksikasjalik kirjeldus soovitatud parandusest**
- **Selgitage, miks see parandus oleks kasulik**
- **Loetlege sarnased funktsioonid teistes projektides, kui see on asjakohane**

### Dokumentatsiooni panustamine

Dokumentatsiooni täiustused on alati hinnatud:

- **Parandage kirjavigu ja grammatikavigu**
- **Selgitage keerulisi teemasid selgemalt**
- **Lisage puuduvaid dokumente**
- **Uuendage vananenud teavet**
- **Lisage näiteid või kasutusjuhtumeid**

### Koodi panustamine

Me tervitame koodipanuseid, sealhulgas:

- **Uued õppetunnid või harjutused**
- **Vigade parandused**
- **Olemasolevate märkmike täiustused**
- **Uued andmekogumid või näited**
- **Viktoriinirakenduse täiustused**

## Alustamine

### Eeltingimused

Enne panustamist veenduge, et teil on:

1. GitHubi konto
2. Git installitud teie süsteemis
3. Python 3.7+ ja Jupyter installitud
4. Node.js ja npm (viktoriinirakenduse panuste jaoks)
5. Tutvumine õppekava struktuuriga

Vaadake [INSTALLATION.md](INSTALLATION.md) üksikasjalike seadistusjuhiste jaoks.

### Forkimine ja kloonimine

1. **Forkige repositoorium** GitHubis  
2. **Kloonige oma fork** lokaalselt:  
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
  
3. **Lisage upstream remote**:  
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```
  

### Haru loomine

Looge oma töö jaoks uus haru:  
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```
  
Haru nimetamise konventsioonid:  
- `feature/` - Uued funktsioonid või õppetunnid  
- `fix/` - Vigade parandused  
- `docs/` - Dokumentatsiooni muudatused  
- `refactor/` - Koodi refaktoreerimine  

## Panustamise juhised

### Õppetundide sisu jaoks

Õppetundide loomisel või olemasolevate muutmisel:

1. **Järgige olemasolevat struktuuri**:  
   - README.md õppetunni sisuga  
   - Jupyteri märkmik harjutustega  
   - Ülesanne (kui kohaldatav)  
   - Lingid eel- ja järelviktoriinidele  

2. **Lisage järgmised elemendid**:  
   - Selged õpieesmärgid  
   - Samm-sammult selgitused  
   - Koodinäited kommentaaridega  
   - Harjutused praktiseerimiseks  
   - Lingid täiendavatele ressurssidele  

3. **Tagage ligipääsetavus**:  
   - Kasutage selget ja lihtsat keelt  
   - Lisage piltidele alt-tekst  
   - Lisage koodikommentaarid  
   - Arvestage erinevate õppimisstiilidega  

### Jupyteri märkmike jaoks

1. **Tühjendage kõik väljundid** enne commit'i:  
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```
  
2. **Lisage markdown-rakud** selgitustega  

3. **Kasutage ühtlast vormindust**:  
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```
  
4. **Testige oma märkmikku** täielikult enne esitamist  

### Python-koodi jaoks

Järgige [PEP 8](https://www.python.org/dev/peps/pep-0008/) stiilijuhiseid:  
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
  

### Viktoriinirakenduse panuste jaoks

Viktoriinirakenduse muutmisel:

1. **Testige lokaalselt**:  
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```
  
2. **Käivitage linter**:  
   ```bash
   npm run lint
   ```
  
3. **Ehitage edukalt**:  
   ```bash
   npm run build
   ```
  
4. **Järgige Vue.js stiilijuhendit** ja olemasolevaid mustreid  

### Tõlgete jaoks

Tõlgete lisamisel või uuendamisel:

1. Järgige struktuuri kaustas `translations/`  
2. Kasutage keelekoodi kausta nimena (nt `fr` prantsuse keele jaoks)  
3. Säilitage sama failistruktuur nagu ingliskeelses versioonis  
4. Uuendage viktoriinilinke, et lisada keeleparameeter: `?loc=fr`  
5. Testige kõiki linke ja vormindust  

## Pull Request'i protsess

### Enne esitamist

1. **Uuendage oma haru** viimaste muudatustega:  
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```
  
2. **Testige oma muudatusi**:  
   - Käivitage kõik muudetud märkmikud  
   - Testige viktoriinirakendust, kui seda muudeti  
   - Kontrollige, kas kõik lingid töötavad  
   - Kontrollige õigekirja ja grammatikavigu  

3. **Commitige oma muudatused**:  
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
  
   Kirjutage selged commit-sõnumid:  
   - Kasutage olevikuvormi ("Lisa funktsioon" mitte "Lisatud funktsioon")  
   - Kasutage käskivat vormi ("Liiguta kursor..." mitte "Liigutab kursorit...")  
   - Piirake esimene rida 72 tähemärgiga  
   - Viidake probleemidele ja pull request'idele, kui asjakohane  

4. **Pushige oma fork'i**:  
   ```bash
   git push origin feature/your-feature-name
   ```
  

### Pull Request'i loomine

1. Minge [repositooriumisse](https://github.com/microsoft/Data-Science-For-Beginners)  
2. Klõpsake "Pull requests" → "New pull request"  
3. Klõpsake "compare across forks"  
4. Valige oma fork ja haru  
5. Klõpsake "Create pull request"  

### PR-i pealkirja formaat

Kasutage selgeid ja kirjeldavaid pealkirju, järgides seda formaati:  
```
[Component] Brief description
```
  
Näited:  
- `[Lesson 7] Paranda Python märkmiku importimisviga`  
- `[Quiz App] Lisa saksa keele tõlge`  
- `[Docs] Uuenda README uute eeltingimustega`  
- `[Fix] Paranda andmete tee visualiseerimise õppetunnis`  

### PR-i kirjeldus

Lisage oma PR-i kirjeldusse:

- **Mis**: Milliseid muudatusi te tegite?  
- **Miks**: Miks need muudatused on vajalikud?  
- **Kuidas**: Kuidas te muudatused rakendasite?  
- **Testimine**: Kuidas te muudatusi testisite?  
- **Ekraanipildid**: Lisage ekraanipildid visuaalsete muudatuste jaoks  
- **Seotud probleemid**: Linkige seotud probleemid (nt "Fixes #123")  

### Ülevaatusprotsess

1. **Automaatkontrollid** käivitatakse teie PR-il  
2. **Hooldajad vaatavad üle** teie panuse  
3. **Tegelege tagasisidega**, tehes täiendavaid commit'e  
4. Kui heaks kiidetud, **hooldaja ühendab** teie PR-i  

### Pärast PR-i ühendamist

1. Kustutage oma haru:  
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```
  
2. Uuendage oma fork:  
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```
  

## Stiilijuhised

### Markdown

- Kasutage ühtlaseid pealkirjatasemeid  
- Lisage tühjad read sektsioonide vahele  
- Kasutage koodiblokke koos keele määratlustega:  
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
  
- Lisage piltidele alt-tekst: `![Alt tekst](../../translated_images/et/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.png)`  
- Hoidke rea pikkused mõistlikud (umbes 80-100 tähemärki)  

### Python

- Järgige PEP 8 stiilijuhendit  
- Kasutage tähenduslikke muutujanimesid  
- Lisage funktsioonidele docstring'id  
- Lisage tüübiviited, kui see on asjakohane:  
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```
  

### JavaScript/Vue.js

- Järgige Vue.js 2 stiilijuhendit  
- Kasutage pakutud ESLint konfiguratsiooni  
- Kirjutage modulaarseid, korduvkasutatavaid komponente  
- Lisage kommentaare keeruka loogika jaoks  

### Failide organiseerimine

- Hoidke seotud failid koos  
- Kasutage kirjeldavaid failinimesid  
- Järgige olemasolevat kataloogistruktuuri  
- Ärge commitige mittevajalikke faile (.DS_Store, .pyc, node_modules jne)  

## Panustaja litsentsileping

See projekt tervitab panuseid ja ettepanekuid. Enamik panuseid nõuab, et te nõustuksite  
panustaja litsentsilepinguga (CLA), mis kinnitab, et teil on õigus ja tegelikult annate meile õigused teie panuse kasutamiseks. Üksikasjade saamiseks külastage  
https://cla.microsoft.com.

Kui esitate pull request'i, määrab CLA-bot automaatselt, kas peate  
esitama CLA ja märgistab PR-i vastavalt (nt silt, kommentaar). Järgige lihtsalt  
boti antud juhiseid. Seda peate tegema ainult üks kord kõigi meie CLA-d kasutavate repositooriumide puhul.

## Küsimused?

- Kontrollige meie [Discordi kanalit #data-science-for-beginners](https://aka.ms/ds4beginners/discord)  
- Liituge meie [Discordi kogukonnaga](https://aka.ms/ds4beginners/discord)  
- Vaadake olemasolevaid [probleeme](https://github.com/microsoft/Data-Science-For-Beginners/issues) ja [pull request'e](https://github.com/microsoft/Data-Science-For-Beginners/pulls)  

## Aitäh!

Teie panused muudavad selle õppekava kõigile paremaks. Täname, et võtate aega panustamiseks!

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.