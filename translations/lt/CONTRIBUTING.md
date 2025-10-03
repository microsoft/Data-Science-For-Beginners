<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T14:49:29+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "lt"
}
-->
# Prisidėjimas prie „Data Science for Beginners“

Ačiū, kad domitės prisidėjimu prie „Data Science for Beginners“ mokymo programos! Mes džiaugiamės bendruomenės indėliu.

## Turinys

- [Elgesio kodeksas](../..)
- [Kaip galiu prisidėti?](../..)
- [Pradžia](../..)
- [Prisidėjimo gairės](../..)
- [„Pull Request“ procesas](../..)
- [Stiliaus gairės](../..)
- [Autoriaus licencijos sutartis](../..)

## Elgesio kodeksas

Šis projektas laikosi [Microsoft atvirojo kodo elgesio kodekso](https://opensource.microsoft.com/codeofconduct/).  
Daugiau informacijos rasite [Elgesio kodekso DUK](https://opensource.microsoft.com/codeofconduct/faq/)  
arba susisiekite el. paštu [opencode@microsoft.com](mailto:opencode@microsoft.com), jei turite papildomų klausimų ar komentarų.

## Kaip galiu prisidėti?

### Klaidų pranešimas

Prieš kurdami klaidų pranešimus, patikrinkite esamus klausimus, kad išvengtumėte pasikartojimų. Kurdamas klaidų pranešimą, pateikite kuo daugiau detalių:

- **Naudokite aiškų ir aprašomąjį pavadinimą**
- **Aprašykite tikslius veiksmus, kaip atkurti problemą**
- **Pateikite konkrečius pavyzdžius** (kodo fragmentus, ekrano nuotraukas)
- **Aprašykite stebėtą elgesį ir tai, ko tikėjotės**
- **Įtraukite savo aplinkos detales** (OS, Python versija, naršyklė)

### Pasiūlymų teikimas

Pasiūlymai dėl patobulinimų visada laukiami! Teikdami pasiūlymus:

- **Naudokite aiškų ir aprašomąjį pavadinimą**
- **Pateikite išsamų pasiūlymo aprašymą**
- **Paaiškinkite, kodėl šis patobulinimas būtų naudingas**
- **Nurodykite panašias funkcijas kituose projektuose, jei taikoma**

### Prisidėjimas prie dokumentacijos

Dokumentacijos patobulinimai visada vertinami:

- **Taisykite rašybos ir gramatikos klaidas**
- **Gerinkite paaiškinimų aiškumą**
- **Pridėkite trūkstamą dokumentaciją**
- **Atnaujinkite pasenusią informaciją**
- **Pridėkite pavyzdžių ar naudojimo atvejų**

### Kodo prisidėjimas

Mes laukiame kodo indėlio, įskaitant:

- **Naujas pamokas ar pratimus**
- **Klaidų taisymus**
- **Esamų užrašų patobulinimus**
- **Naujus duomenų rinkinius ar pavyzdžius**
- **Klausimų programėlės patobulinimus**

## Pradžia

### Būtinos sąlygos

Prieš prisidedant, įsitikinkite, kad turite:

1. GitHub paskyrą
2. Git įdiegtą jūsų sistemoje
3. Python 3.7+ ir Jupyter įdiegtą
4. Node.js ir npm (klausimų programėlės indėliui)
5. Susipažinimą su mokymo programos struktūra

Žr. [INSTALLATION.md](INSTALLATION.md) išsamias diegimo instrukcijas.

### Fork ir Clone

1. **Fork** projektą GitHub
2. **Clone** savo fork lokaliai:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
3. **Pridėkite upstream nuotolinį**:
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```

### Sukurkite šaką

Sukurkite naują šaką savo darbui:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Šakų pavadinimų konvencijos:
- `feature/` - Naujos funkcijos ar pamokos
- `fix/` - Klaidų taisymai
- `docs/` - Dokumentacijos pakeitimai
- `refactor/` - Kodo pertvarkymas

## Prisidėjimo gairės

### Pamokų turiniui

Prisidedant pamokomis ar keičiant esamas:

1. **Laikykitės esamos struktūros**:
   - README.md su pamokos turiniu
   - Jupyter užrašų knygelė su pratimais
   - Užduotis (jei taikoma)
   - Nuoroda į prieš ir po klausimus

2. **Įtraukite šiuos elementus**:
   - Aiškius mokymosi tikslus
   - Žingsnis po žingsnio paaiškinimus
   - Kodo pavyzdžius su komentarais
   - Pratimus praktikai
   - Nuorodas į papildomus išteklius

3. **Užtikrinkite prieinamumą**:
   - Naudokite aiškią, paprastą kalbą
   - Pateikite alternatyvų tekstą vaizdams
   - Įtraukite kodo komentarus
   - Atsižvelkite į skirtingus mokymosi stilius

### Jupyter užrašų knygelėms

1. **Išvalykite visus išvesties duomenis** prieš įsipareigojimą:
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```

2. **Įtraukite markdown langelius** su paaiškinimais

3. **Naudokite nuoseklų formatavimą**:
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```

4. **Išbandykite savo užrašų knygelę** visiškai prieš pateikimą

### Python kodui

Laikykitės [PEP 8](https://www.python.org/dev/peps/pep-0008/) stiliaus gairių:

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

### Klausimų programėlės indėliui

Keičiant klausimų programėlę:

1. **Išbandykite lokaliai**:
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```

2. **Paleiskite linterį**:
   ```bash
   npm run lint
   ```

3. **Sėkmingai sukurkite**:
   ```bash
   npm run build
   ```

4. **Laikykitės Vue.js stiliaus gairių** ir esamų šablonų

### Vertimams

Pridedant ar atnaujinant vertimus:

1. Laikykitės struktūros aplanke `translations/`
2. Naudokite kalbos kodą kaip aplanko pavadinimą (pvz., `fr` prancūzų kalbai)
3. Išlaikykite tą pačią failų struktūrą kaip anglų versijoje
4. Atnaujinkite klausimų nuorodas, kad įtrauktumėte kalbos parametrą: `?loc=fr`
5. Išbandykite visas nuorodas ir formatavimą

## „Pull Request“ procesas

### Prieš pateikimą

1. **Atnaujinkite savo šaką** su naujausiais pakeitimais:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Išbandykite savo pakeitimus**:
   - Paleiskite visus pakeistus užrašus
   - Išbandykite klausimų programėlę, jei ji buvo pakeista
   - Patikrinkite, ar visos nuorodos veikia
   - Patikrinkite rašybos ir gramatikos klaidas

3. **Įsipareigokite savo pakeitimus**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   Rašykite aiškius įsipareigojimų pranešimus:
   - Naudokite esamą laiką („Pridėti funkciją“, o ne „Pridėta funkcija“)
   - Naudokite imperatyvų toną („Perkelti žymeklį į...“, o ne „Perkelia žymeklį į...“)
   - Pirmą eilutę apribokite iki 72 simbolių
   - Nurodykite klausimus ir „pull request“, jei taikoma

4. **Įkelkite į savo fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

### „Pull Request“ kūrimas

1. Eikite į [projektą](https://github.com/microsoft/Data-Science-For-Beginners)
2. Spustelėkite „Pull requests“ → „New pull request“
3. Spustelėkite „compare across forks“
4. Pasirinkite savo fork ir šaką
5. Spustelėkite „Create pull request“

### PR pavadinimo formatas

Naudokite aiškius, aprašomuosius pavadinimus pagal šį formatą:

```
[Component] Brief description
```

Pavyzdžiai:
- `[Pamoka 7] Taisyti Python užrašų knygelės importavimo klaidą`
- `[Klausimų programėlė] Pridėti vokiečių kalbos vertimą`
- `[Dokumentai] Atnaujinti README su naujomis būtinosiomis sąlygomis`
- `[Taisyti] Ištaisyti duomenų kelią vizualizacijos pamokoje`

### PR aprašymas

Įtraukite į savo PR aprašymą:

- **Kas**: Kokius pakeitimus atlikote?
- **Kodėl**: Kodėl šie pakeitimai būtini?
- **Kaip**: Kaip įgyvendinote pakeitimus?
- **Testavimas**: Kaip išbandėte pakeitimus?
- **Ekrano nuotraukos**: Įtraukite ekrano nuotraukas vizualiems pakeitimams
- **Susiję klausimai**: Nuoroda į susijusius klausimus (pvz., „Fixes #123“)

### Peržiūros procesas

1. **Automatiniai patikrinimai** bus vykdomi jūsų PR
2. **Prižiūrėtojai peržiūrės** jūsų indėlį
3. **Atsakykite į atsiliepimus**, atlikdami papildomus įsipareigojimus
4. Kai bus patvirtinta, **prižiūrėtojas sujungs** jūsų PR

### Po PR sujungimo

1. Ištrinkite savo šaką:
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```

2. Atnaujinkite savo fork:
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

## Stiliaus gairės

### Markdown

- Naudokite nuoseklius antraščių lygius
- Įtraukite tuščias eilutes tarp skyrių
- Naudokite kodo blokus su kalbos specifikatoriais:
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
- Pridėkite alternatyvų tekstą vaizdams: `![Alt text](../../translated_images/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.lt.png)`
- Išlaikykite pagrįstą eilutės ilgį (apie 80–100 simbolių)

### Python

- Laikykitės PEP 8 stiliaus gairių
- Naudokite prasmingus kintamųjų pavadinimus
- Pridėkite docstring funkcijoms
- Įtraukite tipų užuominas, kur tinkama:
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```

### JavaScript/Vue.js

- Laikykitės Vue.js 2 stiliaus gairių
- Naudokite pateiktą ESLint konfigūraciją
- Rašykite modulius, pakartotinai naudojamus komponentus
- Pridėkite komentarus sudėtingai logikai

### Failų organizavimas

- Laikykite susijusius failus kartu
- Naudokite aprašomuosius failų pavadinimus
- Laikykitės esamos katalogų struktūros
- Neįsipareigokite nereikalingų failų (.DS_Store, .pyc, node_modules ir kt.)

## Autoriaus licencijos sutartis

Šis projektas priima indėlius ir pasiūlymus. Dauguma indėlių reikalauja, kad jūs  
sutiktumėte su Autoriaus licencijos sutartimi (CLA), patvirtinančia, kad turite teisę  
ir iš tikrųjų suteikiate mums teisę naudoti jūsų indėlį. Daugiau informacijos rasite  
https://cla.microsoft.com.

Kai pateiksite „pull request“, CLA-bot automatiškai nustatys, ar jums reikia  
pateikti CLA, ir atitinkamai pažymės PR (pvz., etikete, komentaru). Tiesiog vykdykite  
bot pateiktas instrukcijas. Tai reikės padaryti tik vieną kartą visiems projektams, naudojantiems mūsų CLA.

## Klausimai?

- Patikrinkite mūsų [Discord kanalo #data-science-for-beginners](https://aka.ms/ds4beginners/discord)
- Prisijunkite prie mūsų [Discord bendruomenės](https://aka.ms/ds4beginners/discord)
- Peržiūrėkite esamus [klausimus](https://github.com/microsoft/Data-Science-For-Beginners/issues) ir [pull requests](https://github.com/microsoft/Data-Science-For-Beginners/pulls)

## Ačiū!

Jūsų indėlis daro šią mokymo programą geresnę visiems. Ačiū, kad skiriate laiko prisidėti!

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.