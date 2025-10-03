<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T14:12:19+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "fi"
}
-->
# Osallistuminen Data Science for Beginners -projektiin

Kiitos kiinnostuksestasi osallistua Data Science for Beginners -opetussuunnitelmaan! Otamme mielellämme vastaan yhteisön panoksia.

## Sisällysluettelo

- [Toimintaohjeet](../..)
- [Kuinka voin osallistua?](../..)
- [Aloittaminen](../..)
- [Osallistumisohjeet](../..)
- [Pull Request -prosessi](../..)
- [Tyyliohjeet](../..)
- [Osallistujan lisenssisopimus](../..)

## Toimintaohjeet

Tämä projekti on omaksunut [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Lisätietoja saat [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) -sivulta
tai ottamalla yhteyttä [opencode@microsoft.com](mailto:opencode@microsoft.com), jos sinulla on kysymyksiä tai kommentteja.

## Kuinka voin osallistua?

### Virheiden raportointi

Ennen kuin luot virheraportin, tarkista olemassa olevat ongelmat välttääksesi päällekkäisyyksiä. Kun luot virheraportin, sisällytä mahdollisimman paljon yksityiskohtia:

- **Käytä selkeää ja kuvaavaa otsikkoa**
- **Kuvaile tarkat vaiheet ongelman toistamiseksi**
- **Anna konkreettisia esimerkkejä** (koodinpätkiä, kuvakaappauksia)
- **Kuvaile havaittua käyttäytymistä ja odotuksiasi**
- **Sisällytä ympäristötiedot** (käyttöjärjestelmä, Python-versio, selain)

### Parannusehdotusten tekeminen

Parannusehdotukset ovat tervetulleita! Kun ehdotat parannuksia:

- **Käytä selkeää ja kuvaavaa otsikkoa**
- **Anna yksityiskohtainen kuvaus ehdotetusta parannuksesta**
- **Selitä, miksi tämä parannus olisi hyödyllinen**
- **Listaa vastaavia ominaisuuksia muissa projekteissa, jos sovellettavissa**

### Dokumentaation parantaminen

Dokumentaation parannukset ovat aina arvostettuja:

- **Korjaa kirjoitus- ja kielioppivirheet**
- **Paranna selitysten selkeyttä**
- **Lisää puuttuvaa dokumentaatiota**
- **Päivitä vanhentunutta tietoa**
- **Lisää esimerkkejä tai käyttötapauksia**

### Koodin kontribuointi

Otamme mielellämme vastaan koodipanoksia, kuten:

- **Uusia oppitunteja tai harjoituksia**
- **Virheiden korjauksia**
- **Parannuksia olemassa oleviin muistikirjoihin**
- **Uusia tietoaineistoja tai esimerkkejä**
- **Visailusovelluksen parannuksia**

## Aloittaminen

### Esivaatimukset

Ennen osallistumista varmista, että sinulla on:

1. GitHub-tili
2. Git asennettuna järjestelmääsi
3. Python 3.7+ ja Jupyter asennettuna
4. Node.js ja npm (visailusovelluksen kontribuutioita varten)
5. Tuntemus opetussuunnitelman rakenteesta

Katso [INSTALLATION.md](INSTALLATION.md) yksityiskohtaisia asennusohjeita varten.

### Haaroita ja kloonaa

1. **Haaroita arkisto** GitHubissa
2. **Kloonaa haarasi** paikallisesti:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
3. **Lisää upstream-remote**:
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```

### Luo haara

Luo uusi haara työllesi:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Haaran nimeämiskäytännöt:
- `feature/` - Uudet ominaisuudet tai oppitunnit
- `fix/` - Virheiden korjaukset
- `docs/` - Dokumentaatiomuutokset
- `refactor/` - Koodin uudelleenjärjestely

## Osallistumisohjeet

### Oppituntisisällön osalta

Kun osallistut oppitunteihin tai muokkaat olemassa olevia:

1. **Noudata olemassa olevaa rakennetta**:
   - README.md oppituntisisällön kanssa
   - Jupyter-muistikirja harjoituksilla
   - Tehtävä (jos sovellettavissa)
   - Linkki ennen ja jälkeen visailuihin

2. **Sisällytä nämä elementit**:
   - Selkeät oppimistavoitteet
   - Vaiheittaiset selitykset
   - Koodiesimerkit kommentteineen
   - Harjoituksia harjoittelua varten
   - Linkkejä lisäresursseihin

3. **Varmista saavutettavuus**:
   - Käytä selkeää, yksinkertaista kieltä
   - Lisää alt-tekstiä kuviin
   - Sisällytä koodikommentteja
   - Huomioi erilaiset oppimistyylit

### Jupyter-muistikirjojen osalta

1. **Tyhjennä kaikki tulosteet** ennen sitoutumista:
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```

2. **Sisällytä markdown-solut** selityksillä

3. **Käytä johdonmukaista muotoilua**:
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```

4. **Testaa muistikirjasi** kokonaan ennen lähettämistä

### Python-koodin osalta

Noudata [PEP 8](https://www.python.org/dev/peps/pep-0008/) -tyyliohjeita:

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

### Visailusovelluksen kontribuutioiden osalta

Kun muokkaat visailusovellusta:

1. **Testaa paikallisesti**:
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```

2. **Aja linter**:
   ```bash
   npm run lint
   ```

3. **Rakenna onnistuneesti**:
   ```bash
   npm run build
   ```

4. **Noudata Vue.js-tyyliohjeita** ja olemassa olevia malleja

### Käännösten osalta

Kun lisäät tai päivität käännöksiä:

1. Noudata rakennetta `translations/`-kansiossa
2. Käytä kielikoodia kansion nimenä (esim. `fi` suomelle)
3. Säilytä sama tiedostorakenne kuin englanninkielisessä versiossa
4. Päivitä visailulinkit sisältämään kieliparametri: `?loc=fi`
5. Testaa kaikki linkit ja muotoilu

## Pull Request -prosessi

### Ennen lähettämistä

1. **Päivitä haarasi** uusimmilla muutoksilla:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Testaa muutoksesi**:
   - Aja kaikki muokatut muistikirjat
   - Testaa visailusovellus, jos sitä on muokattu
   - Varmista, että kaikki linkit toimivat
   - Tarkista oikeinkirjoitus- ja kielioppivirheet

3. **Sitouta muutoksesi**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   Kirjoita selkeät commit-viestit:
   - Käytä preesensmuotoa ("Lisää ominaisuus" ei "Lisätty ominaisuus")
   - Käytä imperatiivimuotoa ("Siirrä kursori..." ei "Siirtää kursoria...")
   - Rajoita ensimmäinen rivi 72 merkkiin
   - Viittaa ongelmiin ja pull requesteihin, kun se on olennaista

4. **Puske haarasi**:
   ```bash
   git push origin feature/your-feature-name
   ```

### Pull Requestin luominen

1. Siirry [arkistoon](https://github.com/microsoft/Data-Science-For-Beginners)
2. Klikkaa "Pull requests" → "New pull request"
3. Klikkaa "compare across forks"
4. Valitse haarasi ja haara
5. Klikkaa "Create pull request"

### PR-otsikon muoto

Käytä selkeitä, kuvaavia otsikoita seuraavan mallin mukaisesti:

```
[Component] Brief description
```

Esimerkkejä:
- `[Lesson 7] Korjaa Python-muistikirjan tuontivirhe`
- `[Quiz App] Lisää saksankielinen käännös`
- `[Docs] Päivitä README uusilla esivaatimuksilla`
- `[Fix] Korjaa datan polku visualisointitehtävässä`

### PR-kuvaus

Sisällytä PR-kuvaukseesi:

- **Mitä**: Mitä muutoksia teit?
- **Miksi**: Miksi nämä muutokset ovat tarpeellisia?
- **Miten**: Kuinka toteutit muutokset?
- **Testaus**: Kuinka testasit muutokset?
- **Kuvakaappaukset**: Sisällytä kuvakaappauksia visuaalisista muutoksista
- **Liittyvät ongelmat**: Linkitä liittyviin ongelmiin (esim. "Fixes #123")

### Tarkistusprosessi

1. **Automaattiset tarkistukset** suoritetaan PR:ssäsi
2. **Ylläpitäjät tarkistavat** kontribuutiosi
3. **Vastaa palautteeseen** tekemällä lisäsitoutumisia
4. Kun PR hyväksytään, **ylläpitäjä yhdistää** sen

### PR:n yhdistämisen jälkeen

1. Poista haarasi:
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```

2. Päivitä haarasi:
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

## Tyyliohjeet

### Markdown

- Käytä johdonmukaisia otsikkotasoja
- Sisällytä tyhjiä rivejä osioiden väliin
- Käytä koodilohkoja kielimäärityksillä:
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
- Lisää alt-tekstiä kuviin: `![Alt-teksti](../../translated_images/kuva.a2a8c9070e65ff3c7c6a6dc945dcd333c7807f900cd4709e93198d0022bd0d3d.fi.png)`
- Pidä rivien pituudet kohtuullisina (noin 80-100 merkkiä)

### Python

- Noudata PEP 8 -tyyliohjeita
- Käytä merkityksellisiä muuttujanimiä
- Lisää docstringit funktioihin
- Sisällytä tyyppivihjeet tarvittaessa:
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```

### JavaScript/Vue.js

- Noudata Vue.js 2 -tyyliohjeita
- Käytä annettua ESLint-konfiguraatiota
- Kirjoita modulaarisia, uudelleenkäytettäviä komponentteja
- Lisää kommentteja monimutkaiselle logiikalle

### Tiedostojen organisointi

- Pidä liittyvät tiedostot yhdessä
- Käytä kuvaavia tiedostonimiä
- Noudata olemassa olevaa hakemistorakennetta
- Älä sitouta tarpeettomia tiedostoja (.DS_Store, .pyc, node_modules, jne.)

## Osallistujan lisenssisopimus

Tämä projekti toivottaa tervetulleeksi kontribuutiot ja ehdotukset. Useimmat kontribuutiot vaativat, että hyväksyt Contributor License Agreement (CLA) -sopimuksen, jossa vakuutat, että sinulla on oikeus antaa meille oikeudet käyttää kontribuutiotasi. Lisätietoja saat osoitteesta https://cla.microsoft.com.

Kun lähetät pull requestin, CLA-bot määrittää automaattisesti, tarvitsetko CLA:n ja merkitsee PR:n asianmukaisesti (esim. etiketti, kommentti). Seuraa yksinkertaisesti botin antamia ohjeita. Sinun tarvitsee tehdä tämä vain kerran kaikissa arkistoissa, jotka käyttävät CLA:ta.

## Kysymyksiä?

- Tarkista [Discord-kanavamme #data-science-for-beginners](https://aka.ms/ds4beginners/discord)
- Liity [Discord-yhteisöömme](https://aka.ms/ds4beginners/discord)
- Tarkista olemassa olevat [ongelmat](https://github.com/microsoft/Data-Science-For-Beginners/issues) ja [pull requestit](https://github.com/microsoft/Data-Science-For-Beginners/pulls)

## Kiitos!

Panoksesi tekee tästä opetussuunnitelmasta paremman kaikille. Kiitos, että käytät aikaa osallistumiseen!

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.