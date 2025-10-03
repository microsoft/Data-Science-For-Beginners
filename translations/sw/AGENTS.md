<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:34:03+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sw"
}
-->
# AGENTS.md

## Muhtasari wa Mradi

Data Science for Beginners ni mtaala wa kina wa wiki 10, masomo 20 ulioundwa na Microsoft Azure Cloud Advocates. Hifadhi hii ni rasilimali ya kujifunza inayofundisha dhana za msingi za sayansi ya data kupitia masomo yanayotegemea miradi, ikijumuisha Jupyter notebooks, maswali ya maingiliano, na mazoezi ya vitendo.

**Teknolojia Muhimu:**
- **Jupyter Notebooks**: Njia kuu ya kujifunza kwa kutumia Python 3
- **Maktaba za Python**: pandas, numpy, matplotlib kwa uchambuzi wa data na uonyeshaji
- **Vue.js 2**: Programu ya maswali (folda ya quiz-app)
- **Docsify**: Jenereta ya tovuti ya nyaraka kwa ufikiaji wa nje ya mtandao
- **Node.js/npm**: Usimamizi wa vifurushi kwa vipengele vya JavaScript
- **Markdown**: Yote yaliyomo kwenye masomo na nyaraka

**Muundo:**
- Hifadhi ya elimu ya lugha nyingi yenye tafsiri nyingi
- Imeundwa katika moduli za masomo (1-Introduction hadi 6-Data-Science-In-Wild)
- Kila somo linajumuisha README, notebooks, mazoezi, na maswali
- Programu ya maswali ya Vue.js inayojitegemea kwa tathmini kabla/baada ya somo
- Msaada wa GitHub Codespaces na kontena za maendeleo za VS Code

## Amri za Usanidi

### Usanidi wa Hifadhi
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Usanidi wa Mazingira ya Python
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Usanidi wa Programu ya Maswali
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

### Seva ya Nyaraka ya Docsify
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Usanidi wa Miradi ya Uonyeshaji
Kwa miradi ya uonyeshaji kama meaningful-visualizations (somo la 13):
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


## Mtiririko wa Maendeleo

### Kufanya Kazi na Jupyter Notebooks
1. Anzisha Jupyter katika mzizi wa hifadhi: `jupyter notebook`
2. Tembelea folda ya somo unalotaka
3. Fungua faili za `.ipynb` ili kufanya mazoezi
4. Notebooks ni za kujitegemea zikiwa na maelezo na seli za msimbo
5. Notebooks nyingi zinatumia pandas, numpy, na matplotlib - hakikisha zimesakinishwa

### Muundo wa Somo
Kila somo kwa kawaida lina:
- `README.md` - Yaliyomo kuu ya somo na nadharia na mifano
- `notebook.ipynb` - Mazoezi ya vitendo ya Jupyter notebook
- `assignment.ipynb` au `assignment.md` - Mazoezi ya mazoezi
- Folda ya `solution/` - Notebooks za suluhisho na msimbo
- Folda ya `images/` - Vifaa vya kuonyesha vinavyosaidia

### Maendeleo ya Programu ya Maswali
- Programu ya Vue.js 2 yenye upakiaji wa haraka wakati wa maendeleo
- Maswali yamehifadhiwa katika `quiz-app/src/assets/translations/`
- Kila lugha ina folda yake ya tafsiri (en, fr, es, nk.)
- Nambari ya maswali inaanza 0 na inaendelea hadi 39 (maswali 40 kwa jumla)

### Kuongeza Tafsiri
- Tafsiri zinawekwa katika folda ya `translations/` kwenye mzizi wa hifadhi
- Kila lugha ina muundo kamili wa somo unaolingana na Kiingereza
- Tafsiri za kiotomatiki kupitia GitHub Actions (co-op-translator.yml)

## Maelekezo ya Kupima

### Upimaji wa Programu ya Maswali
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Upimaji wa Notebooks
- Hakuna mfumo wa upimaji wa kiotomatiki kwa notebooks
- Uthibitishaji wa mwongozo: Endesha seli zote kwa mpangilio ili kuhakikisha hakuna makosa
- Hakikisha faili za data zinapatikana na matokeo yanazalishwa kwa usahihi
- Angalia kwamba uonyeshaji unachorwa vizuri

### Upimaji wa Nyaraka
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Ukaguzi wa Ubora wa Msimbo
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Miongozo ya Mtindo wa Msimbo

### Python (Jupyter Notebooks)
- Fuata miongozo ya mtindo wa PEP 8 kwa msimbo wa Python
- Tumia majina ya kutofautisha yanayoelezea data inayochambuliwa
- Jumuisha seli za markdown zenye maelezo kabla ya seli za msimbo
- Weka seli za msimbo zikilenga dhana moja au operesheni moja
- Tumia pandas kwa uendeshaji wa data, matplotlib kwa uonyeshaji
- Muundo wa kawaida wa uingizaji:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Fuata mwongozo wa mtindo wa Vue.js 2 na mazoea bora
- Usanidi wa ESLint katika `quiz-app/package.json`
- Tumia vipengele vya faili moja vya Vue (.vue files)
- Dumisha muundo wa vipengele
- Endesha `npm run lint` kabla ya kuwasilisha mabadiliko

### Nyaraka za Markdown
- Tumia uongozi wa wazi wa vichwa (# ## ### nk.)
- Jumuisha vizuizi vya msimbo na viainishi vya lugha
- Ongeza maandishi mbadala kwa picha
- Unganisha masomo na rasilimali zinazohusiana
- Weka urefu wa mistari kuwa wa kusomeka

### Mpangilio wa Faili
- Yaliyomo ya somo katika folda zenye nambari (01-defining-data-science, nk.)
- Suluhisho katika folda ndogo ya `solution/`
- Tafsiri zinaakisi muundo wa Kiingereza katika folda ya `translations/`
- Weka faili za data katika `data/` au folda maalum za somo

## Ujenzi na Uwekaji

### Uwekaji wa Programu ya Maswali
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Uwekaji wa Azure Static Web Apps
Programu ya quiz-app inaweza kuwekwa kwenye Azure Static Web Apps:
1. Unda rasilimali ya Azure Static Web App
2. Unganisha na hifadhi ya GitHub
3. Sanidi mipangilio ya ujenzi:
   - Eneo la programu: `quiz-app`
   - Eneo la matokeo: `dist`
4. Mtiririko wa kazi wa GitHub Actions utaweka kiotomatiki unapofanya push

### Tovuti ya Nyaraka
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Hifadhi inajumuisha usanidi wa kontena la maendeleo
- Codespaces huweka kiotomatiki mazingira ya Python na Node.js
- Fungua hifadhi katika Codespace kupitia UI ya GitHub
- Vifurushi vyote vinasakinishwa kiotomatiki

## Miongozo ya Maombi ya Kuvuta (Pull Request)

### Kabla ya Kuwasilisha
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Muundo wa Kichwa cha PR
- Tumia vichwa vya wazi, vya kuelezea
- Muundo: `[Sehemu] Maelezo mafupi`
- Mifano:
  - `[Somo la 7] Rekebisha hitilafu ya uingizaji wa notebook ya Python`
  - `[Programu ya Maswali] Ongeza tafsiri ya Kijerumani`
  - `[Nyaraka] Sasisha README na mahitaji mapya`

### Ukaguzi Unaohitajika
- Hakikisha msimbo wote unafanya kazi bila makosa
- Thibitisha notebooks zinaendeshwa kikamilifu
- Hakikisha programu za Vue.js zinajengwa kwa mafanikio
- Angalia kwamba viungo vya nyaraka vinafanya kazi
- Jaribu programu ya maswali ikiwa imebadilishwa
- Thibitisha tafsiri zinadumisha muundo thabiti

### Miongozo ya Mchango
- Fuata mtindo wa msimbo uliopo na mifumo
- Ongeza maoni ya kuelezea kwa mantiki ngumu
- Sasisha nyaraka husika
- Jaribu mabadiliko katika moduli tofauti za somo ikiwa inafaa
- Soma faili ya CONTRIBUTING.md

## Vidokezo vya Ziada

### Maktaba za Kawaida Zinazotumika
- **pandas**: Uendeshaji na uchambuzi wa data
- **numpy**: Uhesabu wa namba
- **matplotlib**: Uonyeshaji wa data na uchoraji
- **seaborn**: Uonyeshaji wa data wa takwimu (masomo fulani)
- **scikit-learn**: Kujifunza kwa mashine (masomo ya juu)

### Kufanya Kazi na Faili za Data
- Faili za data ziko katika folda ya `data/` au folda maalum za somo
- Notebooks nyingi zinatarajia faili za data katika njia za jamaa
- Faili za CSV ni muundo wa msingi wa data
- Masomo fulani yanatumia JSON kwa mifano ya data isiyo ya uhusiano

### Msaada wa Lugha Nyingi
- Tafsiri 40+ za lugha kupitia GitHub Actions za kiotomatiki
- Mtiririko wa tafsiri katika `.github/workflows/co-op-translator.yml`
- Tafsiri katika folda ya `translations/` yenye misimbo ya lugha
- Tafsiri za maswali katika `quiz-app/src/assets/translations/`

### Chaguo za Mazingira ya Maendeleo
1. **Maendeleo ya Ndani**: Sakinisha Python, Jupyter, Node.js ndani
2. **GitHub Codespaces**: Mazingira ya maendeleo ya papo hapo ya wingu
3. **VS Code Dev Containers**: Maendeleo ya ndani kwa kutumia kontena
4. **Binder**: Fungua notebooks katika wingu (ikiwa imewekwa)

### Miongozo ya Yaliyomo ya Somo
- Kila somo ni la kujitegemea lakini linajenga dhana za awali
- Maswali ya kabla ya somo yanapima maarifa ya awali
- Maswali ya baada ya somo yanasisitiza kujifunza
- Mazoezi yanatoa mazoezi ya vitendo
- Sketchnotes zinatoa muhtasari wa kuona

### Kutatua Masuala ya Kawaida

**Masuala ya Kernel ya Jupyter:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Hitilafu za Usakinishaji wa npm:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Hitilafu za Uingizaji katika Notebooks:**
- Thibitisha maktaba zote zinazohitajika zimesakinishwa
- Angalia utangamano wa toleo la Python (Python 3.7+ inapendekezwa)
- Hakikisha mazingira ya kawaida yamewezeshwa

**Docsify Haipakii:**
- Thibitisha unahudumia kutoka mzizi wa hifadhi
- Angalia kwamba `index.html` ipo
- Hakikisha ufikiaji sahihi wa mtandao (bandari 3000)

### Mazingatio ya Utendaji
- Seti kubwa za data zinaweza kuchukua muda kupakia katika notebooks
- Uchoraji wa uonyeshaji unaweza kuwa polepole kwa michoro ngumu
- Seva ya maendeleo ya Vue.js inawezesha upakiaji wa haraka kwa kurudia haraka
- Ujenzi wa uzalishaji umeboreshwa na umepunguzwa

### Vidokezo vya Usalama
- Hakuna data nyeti au hati za siri zinapaswa kuwasilishwa
- Tumia vigezo vya mazingira kwa funguo zozote za API katika masomo ya wingu
- Masomo yanayohusiana na Azure yanaweza kuhitaji hati za akaunti ya Azure
- Weka maktaba zikiwa zimesasishwa kwa viraka vya usalama

## Kuchangia Tafsiri
- Tafsiri za kiotomatiki zinasimamiwa kupitia GitHub Actions
- Marekebisho ya mwongozo yanakaribishwa kwa usahihi wa tafsiri
- Fuata muundo wa folda ya tafsiri uliopo
- Sasisha viungo vya maswali ili kujumuisha parameter ya lugha: `?loc=fr`
- Jaribu masomo yaliyotafsiriwa ili kuhakikisha yanachapishwa vizuri

## Rasilimali Zinazohusiana
- Mtaala kuu: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Jukwaa la Majadiliano: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Mitaala mingine ya Microsoft: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Matengenezo ya Mradi
- Sasisho za mara kwa mara ili kuweka yaliyomo kuwa ya sasa
- Michango ya jamii inakaribishwa
- Masuala yanafuatiliwa kwenye GitHub
- PRs zinakaguliwa na waangalizi wa mtaala
- Mapitio na sasisho za yaliyomo kila mwezi

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.