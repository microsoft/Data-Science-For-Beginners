<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:27:05+00:00",
  "source_file": "AGENTS.md",
  "language_code": "fi"
}
-->
# AGENTS.md

## Projektin yleiskatsaus

Data Science for Beginners on Microsoft Azure Cloud Advocatesin luoma kattava 10 viikon, 20 oppitunnin opetusohjelma. Tämä repositorio on oppimisresurssi, joka opettaa perustavanlaatuisia datatieteen käsitteitä projektipohjaisten oppituntien avulla, mukaan lukien Jupyter-muistikirjat, interaktiiviset visailut ja käytännön tehtävät.

**Keskeiset teknologiat:**
- **Jupyter-muistikirjat**: Pääasiallinen oppimisväline Python 3:lla
- **Python-kirjastot**: pandas, numpy, matplotlib datan analysointiin ja visualisointiin
- **Vue.js 2**: Visailusovellus (quiz-app-kansio)
- **Docsify**: Dokumentaation sivustogeneraattori offline-käyttöön
- **Node.js/npm**: JavaScript-komponenttien pakettien hallinta
- **Markdown**: Kaikki oppituntien sisältö ja dokumentaatio

**Arkkitehtuuri:**
- Monikielinen opetusrepositorio laajoilla käännöksillä
- Jäsennelty oppituntimoduuleihin (1-Introduction - 6-Data-Science-In-Wild)
- Jokainen oppitunti sisältää README:n, muistikirjat, tehtävät ja visailut
- Erillinen Vue.js-visailusovellus oppituntien arviointiin ennen ja jälkeen
- GitHub Codespaces ja VS Code -kehityskonttien tuki

## Asennuskomennot

### Repositorion asennus
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Python-ympäristön asennus
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Visailusovelluksen asennus
```bash
# Navigate to quiz app
cd quiz-app

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint and fix files
npm run lint
```

### Docsify-dokumentaatiopalvelin
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Visualisointiprojektien asennus
Visualisointiprojekteille, kuten meaningful-visualizations (oppitunti 13):
```bash
# Navigate to starter or solution folder
cd 3-Data-Visualization/13-meaningful-visualizations/starter

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint files
npm run lint
```


## Kehitystyön kulku

### Työskentely Jupyter-muistikirjojen kanssa
1. Käynnistä Jupyter repositorion juurihakemistossa: `jupyter notebook`
2. Siirry haluttuun oppituntikansioon
3. Avaa `.ipynb`-tiedostot harjoitusten tekemistä varten
4. Muistikirjat ovat itsenäisiä ja sisältävät selityksiä sekä koodisoluja
5. Useimmat muistikirjat käyttävät pandas-, numpy- ja matplotlib-kirjastoja - varmista, että ne on asennettu

### Oppituntien rakenne
Jokainen oppitunti sisältää yleensä:
- `README.md` - Pääsisältö teoriaa ja esimerkkejä varten
- `notebook.ipynb` - Käytännön Jupyter-muistikirjaharjoituksia
- `assignment.ipynb` tai `assignment.md` - Harjoitustehtäviä
- `solution/`-kansio - Ratkaisumuistikirjat ja koodi
- `images/`-kansio - Tukimateriaalit

### Visailusovelluksen kehitys
- Vue.js 2 -sovellus, jossa on hot-reload kehityksen aikana
- Visailut tallennetaan `quiz-app/src/assets/translations/`-kansioon
- Jokaisella kielellä on oma käännöskansio (en, fr, es jne.)
- Visailujen numerointi alkaa 0:sta ja jatkuu 39:ään (yhteensä 40 visailua)

### Käännösten lisääminen
- Käännökset sijoitetaan `translations/`-kansioon repositorion juurihakemistossa
- Jokaisella kielellä on täydellinen oppituntirakenne, joka peilaa englanninkielistä
- Automaattinen käännös GitHub Actionsin kautta (co-op-translator.yml)

## Testausohjeet

### Visailusovelluksen testaus
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Muistikirjojen testaus
- Muistikirjoille ei ole olemassa automaattista testauskehystä
- Manuaalinen validointi: Suorita kaikki solut järjestyksessä varmistaaksesi, ettei virheitä esiinny
- Varmista, että datatiedostot ovat saatavilla ja tulokset luodaan oikein
- Tarkista, että visualisoinnit renderöityvät oikein

### Dokumentaation testaus
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Koodin laadun tarkistukset
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Koodityyliohjeet

### Python (Jupyter-muistikirjat)
- Noudata PEP 8 -tyyliohjeita Python-koodissa
- Käytä selkeitä muuttujanimiä, jotka kuvaavat analysoitavaa dataa
- Sisällytä markdown-solut selityksillä ennen koodisoluja
- Pidä koodisolut keskittyneinä yksittäisiin käsitteisiin tai operaatioihin
- Käytä pandas-kirjastoa datan käsittelyyn ja matplotlib-kirjastoa visualisointiin
- Yleinen tuontimalli:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Noudata Vue.js 2 -tyyliopasta ja parhaita käytäntöjä
- ESLint-konfiguraatio `quiz-app/package.json`-tiedostossa
- Käytä Vue-yksittäistiedostokomponentteja (.vue-tiedostot)
- Säilytä komponenttipohjainen arkkitehtuuri
- Suorita `npm run lint` ennen muutosten lähettämistä

### Markdown-dokumentaatio
- Käytä selkeää otsikkohierarkiaa (# ## ### jne.)
- Sisällytä koodilohkot kielimäärityksillä
- Lisää kuville alt-teksti
- Linkitä liittyviin oppitunteihin ja resursseihin
- Pidä rivin pituudet kohtuullisina luettavuuden vuoksi

### Tiedostojen organisointi
- Oppituntisisältö numeroiduissa kansioissa (01-defining-data-science jne.)
- Ratkaisut omissa `solution/`-alikansioissaan
- Käännökset peilaavat englanninkielistä rakennetta `translations/`-kansiossa
- Datatiedostot `data/`-kansiossa tai oppituntikohtaisissa kansioissa

## Rakentaminen ja käyttöönotto

### Visailusovelluksen käyttöönotto
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Azure Static Web Apps -käyttöönotto
Visailusovellus voidaan ottaa käyttöön Azure Static Web Appsissa:
1. Luo Azure Static Web App -resurssi
2. Yhdistä GitHub-repositorioon
3. Määritä rakennusasetukset:
   - Sovelluksen sijainti: `quiz-app`
   - Tulosteen sijainti: `dist`
4. GitHub Actions -työnkulku ottaa käyttöön automaattisesti pushin yhteydessä

### Dokumentaatiosivusto
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Repositorio sisältää kehityskonttien konfiguraation
- Codespaces asentaa automaattisesti Python- ja Node.js-ympäristön
- Avaa repositorio Codespacessa GitHubin käyttöliittymän kautta
- Kaikki riippuvuudet asennetaan automaattisesti

## Pull Request -ohjeet

### Ennen lähettämistä
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### PR-otsikon muoto
- Käytä selkeitä, kuvaavia otsikoita
- Muoto: `[Komponentti] Lyhyt kuvaus`
- Esimerkkejä:
  - `[Oppitunti 7] Korjaa Python-muistikirjan tuontivirhe`
  - `[Visailusovellus] Lisää saksankielinen käännös`
  - `[Dokumentaatio] Päivitä README uusilla vaatimuksilla`

### Vaaditut tarkistukset
- Varmista, että kaikki koodi toimii ilman virheitä
- Tarkista, että muistikirjat suorittavat kokonaan
- Varmista, että Vue.js-sovellukset rakentuvat onnistuneesti
- Tarkista, että dokumentaatiolinkit toimivat
- Testaa visailusovellus, jos sitä on muokattu
- Varmista, että käännökset säilyttävät yhtenäisen rakenteen

### Osallistumisohjeet
- Noudata olemassa olevia koodityylejä ja -malleja
- Lisää selittäviä kommentteja monimutkaiselle logiikalle
- Päivitä asiaankuuluva dokumentaatio
- Testaa muutokset eri oppituntimoduuleissa, jos sovellettavissa
- Lue CONTRIBUTING.md-tiedosto

## Lisähuomautuksia

### Yleisesti käytetyt kirjastot
- **pandas**: Datan käsittely ja analysointi
- **numpy**: Laskennallinen matematiikka
- **matplotlib**: Datan visualisointi ja kaavioiden luonti
- **seaborn**: Tilastollinen datan visualisointi (joissakin oppitunneissa)
- **scikit-learn**: Koneoppiminen (edistyneet oppitunnit)

### Työskentely datatiedostojen kanssa
- Datatiedostot sijaitsevat `data/`-kansiossa tai oppituntikohtaisissa hakemistoissa
- Useimmat muistikirjat odottavat datatiedostoja suhteellisissa poluissa
- CSV-tiedostot ovat ensisijainen datamuoto
- Joissakin oppitunneissa käytetään JSON-tiedostoja ei-relationaalisen datan esimerkkeinä

### Monikielinen tuki
- Yli 40 kielen käännökset automaattisesti GitHub Actionsin kautta
- Käännöstyönkulku `.github/workflows/co-op-translator.yml`-tiedostossa
- Käännökset `translations/`-kansiossa kielikoodeilla
- Visailukäännökset `quiz-app/src/assets/translations/`-kansiossa

### Kehitysympäristön vaihtoehdot
1. **Paikallinen kehitys**: Asenna Python, Jupyter, Node.js paikallisesti
2. **GitHub Codespaces**: Pilvipohjainen välitön kehitysympäristö
3. **VS Code Dev Containers**: Paikallinen konttipohjainen kehitys
4. **Binder**: Käynnistä muistikirjat pilvessä (jos konfiguroitu)

### Oppituntisisällön ohjeet
- Jokainen oppitunti on itsenäinen, mutta rakentuu aiempien käsitteiden päälle
- Ennakkovisailut testaavat aiempaa tietämystä
- Jälkivisailut vahvistavat oppimista
- Tehtävät tarjoavat käytännön harjoitusta
- Sketchnotes tarjoaa visuaalisia yhteenvetoja

### Yleiset ongelmatilanteet

**Jupyter-ytimen ongelmat:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**npm-asennuksen epäonnistumiset:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Tuontivirheet muistikirjoissa:**
- Varmista, että kaikki tarvittavat kirjastot on asennettu
- Tarkista Python-version yhteensopivuus (suositus: Python 3.7+)
- Varmista, että virtuaaliympäristö on aktivoitu

**Docsify ei lataudu:**
- Varmista, että palvelin toimii repositorion juurihakemistosta
- Tarkista, että `index.html`-tiedosto on olemassa
- Varmista oikea verkkoyhteys (portti 3000)

### Suorituskykyhuomautukset
- Suuret datatiedostot voivat kestää aikaa latautua muistikirjoissa
- Visualisointien renderöinti voi olla hidasta monimutkaisille kaavioille
- Vue.js-kehityspalvelin mahdollistaa nopean iteroinnin hot-reloadin avulla
- Tuotantoversiot ovat optimoituja ja pienennettyjä

### Tietoturvahuomautukset
- Älä tallenna arkaluontoisia tietoja tai tunnuksia
- Käytä ympäristömuuttujia pilvioppituntien API-avaimille
- Azureen liittyvät oppitunnit saattavat vaatia Azure-tilin tunnuksia
- Pidä riippuvuudet ajan tasalla tietoturvapäivitysten varalta

## Osallistuminen käännöksiin
- Automaattiset käännökset hallinnoidaan GitHub Actionsin kautta
- Manuaaliset korjaukset ovat tervetulleita käännösten tarkkuuden parantamiseksi
- Noudata olemassa olevaa käännöskansiota
- Päivitä visailulinkit sisältämään kieliparametri: `?loc=fr`
- Testaa käännetyt oppitunnit varmistaaksesi oikean renderöinnin

## Liittyvät resurssit
- Pääopetusohjelma: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Keskustelufoorumi: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Muut Microsoftin opetusohjelmat: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Projektin ylläpito
- Säännölliset päivitykset sisällön ajantasaisena pitämiseksi
- Yhteisön panokset ovat tervetulleita
- Ongelmia seurataan GitHubissa
- PR:t tarkistetaan opetusohjelman ylläpitäjien toimesta
- Kuukausittaiset sisällön tarkistukset ja päivitykset

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.