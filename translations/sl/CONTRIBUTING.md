<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T14:43:35+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sl"
}
-->
# Prispevanje k Data Science za začetnike

Hvala za vaše zanimanje za prispevanje k učnemu načrtu Data Science za začetnike! Veseli smo prispevkov iz skupnosti.

## Kazalo vsebine

- [Kodeks ravnanja](../..)
- [Kako lahko prispevam?](../..)
- [Začetek](../..)
- [Smernice za prispevanje](../..)
- [Postopek za Pull Request](../..)
- [Slogovne smernice](../..)
- [Dogovor o licenciranju prispevkov](../..)

## Kodeks ravnanja

Ta projekt je sprejel [Microsoftov kodeks ravnanja za odprto kodo](https://opensource.microsoft.com/codeofconduct/).
Za več informacij si oglejte [pogosta vprašanja o kodeksu ravnanja](https://opensource.microsoft.com/codeofconduct/faq/)
ali se obrnite na [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna vprašanja ali komentarje.

## Kako lahko prispevam?

### Poročanje o napakah

Preden ustvarite poročilo o napaki, preverite obstoječe težave, da se izognete podvajanju. Ko ustvarjate poročilo o napaki, vključite čim več podrobnosti:

- **Uporabite jasen in opisni naslov**
- **Opišite natančne korake za reprodukcijo težave**
- **Predložite konkretne primere** (odlomki kode, posnetki zaslona)
- **Opišite vedenje, ki ste ga opazili, in kaj ste pričakovali**
- **Vključite podrobnosti o vašem okolju** (OS, različica Pythona, brskalnik)

### Predlaganje izboljšav

Predlogi za izboljšave so dobrodošli! Pri predlaganju izboljšav:

- **Uporabite jasen in opisni naslov**
- **Predložite podroben opis predlagane izboljšave**
- **Razložite, zakaj bi bila ta izboljšava koristna**
- **Navedite podobne funkcije v drugih projektih, če je primerno**

### Prispevanje k dokumentaciji

Izboljšave dokumentacije so vedno cenjene:

- **Popravite tipkarske in slovnične napake**
- **Izboljšajte jasnost razlag**
- **Dodajte manjkajočo dokumentacijo**
- **Posodobite zastarele informacije**
- **Dodajte primere ali primere uporabe**

### Prispevanje kode

Veseli smo prispevkov kode, vključno z:

- **Novimi lekcijami ali vajami**
- **Popravki napak**
- **Izboljšavami obstoječih zvezkov**
- **Novimi podatkovnimi nabori ali primeri**
- **Izboljšavami aplikacije za kvize**

## Začetek

### Predpogoji

Pred prispevanjem se prepričajte, da imate:

1. GitHub račun
2. Git nameščen na vašem sistemu
3. Python 3.7+ in Jupyter nameščen
4. Node.js in npm (za prispevke k aplikaciji za kvize)
5. Poznavanje strukture učnega načrta

Oglejte si [INSTALLATION.md](INSTALLATION.md) za podrobna navodila za nastavitev.

### Fork in kloniranje

1. **Forkajte repozitorij** na GitHubu
2. **Klonirajte svoj fork** lokalno:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
3. **Dodajte upstream remote**:
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```

### Ustvarite vejo

Ustvarite novo vejo za svoje delo:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Konvencije poimenovanja vej:
- `feature/` - Nove funkcije ali lekcije
- `fix/` - Popravki napak
- `docs/` - Spremembe dokumentacije
- `refactor/` - Prestrukturiranje kode

## Smernice za prispevanje

### Za vsebino lekcij

Pri prispevanju lekcij ali spreminjanju obstoječih:

1. **Sledite obstoječi strukturi**:
   - README.md z vsebino lekcije
   - Jupyter zvezek z vajami
   - Naloga (če je primerno)
   - Povezava na predkviz in postkviz

2. **Vključite te elemente**:
   - Jasni učni cilji
   - Razlage korak za korakom
   - Primeri kode s komentarji
   - Vaje za prakso
   - Povezave do dodatnih virov

3. **Zagotovite dostopnost**:
   - Uporabite jasno, preprosto jezikovno izražanje
   - Dodajte alt besedilo za slike
   - Vključite komentarje v kodo
   - Upoštevajte različne stile učenja

### Za Jupyter zvezke

1. **Počistite vse izhode** pred oddajo:
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```

2. **Vključite markdown celice** z razlagami

3. **Uporabite dosledno oblikovanje**:
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```

4. **Popolnoma preizkusite svoj zvezek** pred oddajo

### Za Python kodo

Sledite smernicam sloga [PEP 8](https://www.python.org/dev/peps/pep-0008/):

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

### Za prispevke k aplikaciji za kvize

Pri spreminjanju aplikacije za kvize:

1. **Preizkusite lokalno**:
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```

2. **Zaženite linter**:
   ```bash
   npm run lint
   ```

3. **Uspešno zgradite**:
   ```bash
   npm run build
   ```

4. **Sledite smernicam sloga Vue.js** in obstoječim vzorcem

### Za prevode

Pri dodajanju ali posodabljanju prevodov:

1. Sledite strukturi v mapi `translations/`
2. Uporabite kodo jezika kot ime mape (npr. `fr` za francoščino)
3. Ohranite enako strukturo datotek kot angleška različica
4. Posodobite povezave kvizov, da vključujejo parameter jezika: `?loc=fr`
5. Preizkusite vse povezave in oblikovanje

## Postopek za Pull Request

### Pred oddajo

1. **Posodobite svojo vejo** z najnovejšimi spremembami:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Preizkusite svoje spremembe**:
   - Zaženite vse spremenjene zvezke
   - Preizkusite aplikacijo za kvize, če je bila spremenjena
   - Preverite, ali vse povezave delujejo
   - Preverite črkovanje in slovnične napake

3. **Zavežite svoje spremembe**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   Pišite jasna sporočila o zavezah:
   - Uporabite sedanjik ("Dodaj funkcijo" ne "Dodana funkcija")
   - Uporabite imperativni način ("Premakni kazalec na..." ne "Premakne kazalec na...")
   - Omejite prvo vrstico na 72 znakov
   - Navedite težave in pull requeste, kjer je to primerno

4. **Potisnite na svoj fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

### Ustvarjanje Pull Requesta

1. Pojdite na [repozitorij](https://github.com/microsoft/Data-Science-For-Beginners)
2. Kliknite "Pull requests" → "New pull request"
3. Kliknite "compare across forks"
4. Izberite svoj fork in vejo
5. Kliknite "Create pull request"

### Format naslova PR

Uporabite jasne, opisne naslove po tem formatu:

```
[Component] Brief description
```

Primeri:
- `[Lekcija 7] Popravi napako pri uvozu Python zvezka`
- `[Aplikacija za kvize] Dodaj nemški prevod`
- `[Dokumentacija] Posodobi README z novimi predpogoji`
- `[Popravek] Popravi pot podatkov v lekciji o vizualizaciji`

### Opis PR

Vključite v opis PR:

- **Kaj**: Katere spremembe ste naredili?
- **Zakaj**: Zakaj so te spremembe potrebne?
- **Kako**: Kako ste izvedli spremembe?
- **Testiranje**: Kako ste preizkusili spremembe?
- **Posnetki zaslona**: Vključite posnetke zaslona za vizualne spremembe
- **Povezane težave**: Povezava na povezane težave (npr. "Fixes #123")

### Postopek pregleda

1. **Avtomatizirani pregledi** bodo izvedeni na vašem PR
2. **Vzdrževalci bodo pregledali** vaš prispevek
3. **Odpravite povratne informacije** z dodatnimi zavezami
4. Ko bo odobreno, bo **vzdrževalec združil** vaš PR

### Po združitvi vašega PR

1. Izbrišite svojo vejo:
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```

2. Posodobite svoj fork:
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

## Slogovne smernice

### Markdown

- Uporabite dosledne ravni naslovov
- Vključite prazne vrstice med odseki
- Uporabite blok kode z določenimi jeziki:
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
- Dodajte alt besedilo slikam: `![Alt besedilo](../../translated_images/sl/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.png)`
- Ohranjajte dolžino vrstic razumno (približno 80-100 znakov)

### Python

- Sledite smernicam sloga PEP 8
- Uporabite smiselna imena spremenljivk
- Dodajte docstrings funkcijam
- Vključite namige tipov, kjer je primerno:
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```

### JavaScript/Vue.js

- Sledite smernicam sloga Vue.js 2
- Uporabite konfiguracijo ESLint, ki je na voljo
- Pišite modularne, ponovno uporabne komponente
- Dodajte komentarje za kompleksno logiko

### Organizacija datotek

- Hranite povezane datoteke skupaj
- Uporabite opisna imena datotek
- Sledite obstoječi strukturi imenikov
- Ne zavezujte nepotrebnih datotek (.DS_Store, .pyc, node_modules itd.)

## Dogovor o licenciranju prispevkov

Ta projekt pozdravlja prispevke in predloge. Večina prispevkov zahteva, da se strinjate z Dogovorom o licenciranju prispevkov (CLA), ki potrjuje, da imate pravico in dejansko podeljujete pravice za uporabo vašega prispevka. Za podrobnosti obiščite https://cla.microsoft.com.

Ko oddate pull request, bo CLA-bot samodejno določil, ali morate predložiti CLA in ustrezno označil PR (npr. oznaka, komentar). Preprosto sledite navodilom, ki jih zagotovi bot. To boste morali storiti le enkrat za vse repozitorije, ki uporabljajo naš CLA.

## Vprašanja?

- Preverite naš [Discord kanal #data-science-for-beginners](https://aka.ms/ds4beginners/discord)
- Pridružite se naši [Discord skupnosti](https://aka.ms/ds4beginners/discord)
- Preglejte obstoječe [težave](https://github.com/microsoft/Data-Science-For-Beginners/issues) in [pull requeste](https://github.com/microsoft/Data-Science-For-Beginners/pulls)

## Hvala!

Vaši prispevki izboljšujejo ta učni načrt za vse. Hvala, ker ste si vzeli čas za prispevanje!

---

**Izjava o omejitvi odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.