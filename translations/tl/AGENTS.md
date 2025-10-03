<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:32:55+00:00",
  "source_file": "AGENTS.md",
  "language_code": "tl"
}
-->
# AGENTS.md

## Pangkalahatang-ideya ng Proyekto

Ang Data Science for Beginners ay isang komprehensibong kurikulum na tumatagal ng 10 linggo at may 20 aralin, na ginawa ng Microsoft Azure Cloud Advocates. Ang repositoryo ay isang mapagkukunan ng pag-aaral na nagtuturo ng mga pangunahing konsepto ng data science sa pamamagitan ng mga aralin na nakabatay sa proyekto, kabilang ang mga Jupyter notebook, interactive na pagsusulit, at mga praktikal na gawain.

**Pangunahing Teknolohiya:**
- **Jupyter Notebooks**: Pangunahing medium ng pag-aaral gamit ang Python 3
- **Python Libraries**: pandas, numpy, matplotlib para sa pagsusuri at visualisasyon ng data
- **Vue.js 2**: Aplikasyon ng pagsusulit (quiz-app folder)
- **Docsify**: Tagabuo ng site ng dokumentasyon para sa offline na access
- **Node.js/npm**: Pamamahala ng package para sa mga JavaScript na bahagi
- **Markdown**: Lahat ng nilalaman ng aralin at dokumentasyon

**Arkitektura:**
- Repositoryo na pang-edukasyon na multi-wika na may malawak na mga pagsasalin
- Nakabalangkas sa mga module ng aralin (1-Introduction hanggang 6-Data-Science-In-Wild)
- Ang bawat aralin ay may kasamang README, mga notebook, mga gawain, at mga pagsusulit
- Standalone Vue.js na aplikasyon ng pagsusulit para sa pre/post-lesson assessments
- Suporta para sa GitHub Codespaces at VS Code dev containers

## Mga Utos sa Setup

### Setup ng Repositoryo
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Setup ng Python Environment
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Setup ng Aplikasyon ng Pagsusulit
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

### Docsify Documentation Server
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Setup ng Mga Proyekto ng Visualisasyon
Para sa mga proyekto ng visualisasyon tulad ng meaningful-visualizations (lesson 13):
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


## Workflow ng Pag-develop

### Paggamit ng Jupyter Notebooks
1. Simulan ang Jupyter sa root ng repositoryo: `jupyter notebook`
2. Mag-navigate sa nais na folder ng aralin
3. Buksan ang mga `.ipynb` file upang magtrabaho sa mga ehersisyo
4. Ang mga notebook ay self-contained na may mga paliwanag at code cells
5. Karamihan sa mga notebook ay gumagamit ng pandas, numpy, at matplotlib - tiyaking naka-install ang mga ito

### Estruktura ng Aralin
Ang bawat aralin ay karaniwang naglalaman ng:
- `README.md` - Pangunahing nilalaman ng aralin na may teorya at mga halimbawa
- `notebook.ipynb` - Mga praktikal na ehersisyo sa Jupyter notebook
- `assignment.ipynb` o `assignment.md` - Mga gawain para sa pagsasanay
- `solution/` folder - Mga notebook ng solusyon at code
- `images/` folder - Mga sumusuportang visual na materyales

### Pag-develop ng Aplikasyon ng Pagsusulit
- Aplikasyon ng Vue.js 2 na may hot-reload sa panahon ng pag-develop
- Ang mga pagsusulit ay naka-imbak sa `quiz-app/src/assets/translations/`
- Ang bawat wika ay may sariling folder ng pagsasalin (en, fr, es, atbp.)
- Ang pagbilang ng pagsusulit ay nagsisimula sa 0 at umaabot hanggang 39 (40 pagsusulit sa kabuuan)

### Pagdaragdag ng Mga Pagsasalin
- Ang mga pagsasalin ay inilalagay sa `translations/` folder sa root ng repositoryo
- Ang bawat wika ay may kumpletong estruktura ng aralin na ginaya mula sa Ingles
- Automated na pagsasalin sa pamamagitan ng GitHub Actions (co-op-translator.yml)

## Mga Tagubilin sa Pagsubok

### Pagsubok ng Aplikasyon ng Pagsusulit
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Pagsubok ng Notebook
- Walang automated na test framework para sa mga notebook
- Manu-manong pag-validate: Patakbuhin ang lahat ng cells nang sunod-sunod upang tiyakin na walang error
- Siguraduhing naa-access ang mga data file at tama ang mga output
- Tiyakin na maayos ang pag-render ng mga visualisasyon

### Pagsubok ng Dokumentasyon
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Mga Pag-check ng Kalidad ng Code
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Mga Alituntunin sa Estilo ng Code

### Python (Jupyter Notebooks)
- Sundin ang PEP 8 na mga alituntunin sa estilo para sa Python code
- Gumamit ng malinaw na pangalan ng variable na nagpapaliwanag sa data na sinusuri
- Maglagay ng markdown cells na may mga paliwanag bago ang mga code cells
- Panatilihing nakatuon ang mga code cells sa iisang konsepto o operasyon
- Gumamit ng pandas para sa manipulasyon ng data, matplotlib para sa visualisasyon
- Karaniwang pattern ng import:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Sundin ang Vue.js 2 na gabay sa estilo at pinakamahusay na mga kasanayan
- ESLint configuration sa `quiz-app/package.json`
- Gumamit ng Vue single-file components (.vue files)
- Panatilihin ang arkitektura na nakabatay sa mga bahagi
- Patakbuhin ang `npm run lint` bago mag-commit ng mga pagbabago

### Markdown Documentation
- Gumamit ng malinaw na hierarchy ng mga heading (# ## ### atbp.)
- Maglagay ng mga code block na may mga specifier ng wika
- Magdagdag ng alt text para sa mga imahe
- Mag-link sa mga kaugnay na aralin at mapagkukunan
- Panatilihing maayos ang haba ng linya para sa readability

### Organisasyon ng File
- Nilalaman ng aralin sa mga folder na may numero (01-defining-data-science, atbp.)
- Mga solusyon sa dedikadong `solution/` subfolders
- Ang mga pagsasalin ay ginagaya ang estruktura ng Ingles sa `translations/` folder
- Panatilihin ang mga data file sa `data/` o mga folder na partikular sa aralin

## Build at Deployment

### Deployment ng Aplikasyon ng Pagsusulit
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Deployment ng Azure Static Web Apps
Ang quiz-app ay maaaring i-deploy sa Azure Static Web Apps:
1. Gumawa ng Azure Static Web App resource
2. Ikonekta sa GitHub repository
3. I-configure ang mga setting ng build:
   - Lokasyon ng app: `quiz-app`
   - Lokasyon ng output: `dist`
4. Ang workflow ng GitHub Actions ay awtomatikong mag-deploy kapag may push

### Site ng Dokumentasyon
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Ang repositoryo ay may kasamang dev container configuration
- Ang Codespaces ay awtomatikong nagse-set up ng Python at Node.js environment
- Buksan ang repositoryo sa Codespace sa pamamagitan ng GitHub UI
- Ang lahat ng dependencies ay awtomatikong naka-install

## Mga Alituntunin sa Pull Request

### Bago Mag-submit
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Format ng PR Title
- Gumamit ng malinaw, deskriptibong mga pamagat
- Format: `[Component] Maikling paglalarawan`
- Mga Halimbawa:
  - `[Lesson 7] Ayusin ang Python notebook import error`
  - `[Quiz App] Magdagdag ng German translation`
  - `[Docs] I-update ang README na may bagong prerequisites`

### Mga Kinakailangang Pag-check
- Siguraduhing tumatakbo ang lahat ng code nang walang error
- Tiyakin na ang mga notebook ay ganap na na-eexecute
- Kumpirmahin na matagumpay ang pag-build ng Vue.js apps
- Suriin na gumagana ang mga link ng dokumentasyon
- Subukan ang aplikasyon ng pagsusulit kung binago
- Siguraduhin na ang mga pagsasalin ay may pare-parehong estruktura

### Mga Alituntunin sa Kontribusyon
- Sundin ang umiiral na estilo ng code at mga pattern
- Magdagdag ng mga paliwanag na komento para sa kumplikadong lohika
- I-update ang kaugnay na dokumentasyon
- Subukan ang mga pagbabago sa iba't ibang module ng aralin kung naaangkop
- Suriin ang CONTRIBUTING.md file

## Karagdagang Tala

### Karaniwang Ginagamit na Mga Library
- **pandas**: Manipulasyon at pagsusuri ng data
- **numpy**: Numerical computing
- **matplotlib**: Visualisasyon at pag-plot ng data
- **seaborn**: Statistical data visualization (ilang aralin)
- **scikit-learn**: Machine learning (mga advanced na aralin)

### Paggamit ng Mga Data File
- Ang mga data file ay matatagpuan sa `data/` folder o mga direktoryo na partikular sa aralin
- Karamihan sa mga notebook ay inaasahan ang mga data file sa mga relative na path
- Ang mga CSV file ang pangunahing format ng data
- Ang ilang aralin ay gumagamit ng JSON para sa mga halimbawa ng non-relational na data

### Suporta sa Multi-Wika
- 40+ na pagsasalin ng wika sa pamamagitan ng automated na GitHub Actions
- Workflow ng pagsasalin sa `.github/workflows/co-op-translator.yml`
- Ang mga pagsasalin ay nasa `translations/` folder na may mga code ng wika
- Ang mga pagsasalin ng pagsusulit ay nasa `quiz-app/src/assets/translations/`

### Mga Opsyon sa Development Environment
1. **Local Development**: Mag-install ng Python, Jupyter, Node.js nang lokal
2. **GitHub Codespaces**: Cloud-based na instant development environment
3. **VS Code Dev Containers**: Lokal na container-based na development
4. **Binder**: I-launch ang mga notebook sa cloud (kung naka-configure)

### Mga Alituntunin sa Nilalaman ng Aralin
- Ang bawat aralin ay standalone ngunit bumubuo sa mga naunang konsepto
- Ang mga pre-lesson quiz ay sumusubok sa naunang kaalaman
- Ang mga post-lesson quiz ay nagpapatibay ng pagkatuto
- Ang mga gawain ay nagbibigay ng praktikal na pagsasanay
- Ang mga sketchnotes ay nagbibigay ng visual na buod

### Pag-troubleshoot ng Karaniwang Mga Isyu

**Mga Isyu sa Jupyter Kernel:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Mga Pagkabigo sa npm Install:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Mga Error sa Import sa Notebook:**
- Siguraduhing naka-install ang lahat ng kinakailangang library
- Suriin ang compatibility ng bersyon ng Python (inirerekomenda ang Python 3.7+)
- Tiyakin na naka-activate ang virtual environment

**Hindi Naglo-load ang Docsify:**
- Siguraduhing nagseserbisyo mula sa root ng repositoryo
- Suriin na umiiral ang `index.html`
- Tiyakin ang tamang network access (port 3000)

### Mga Pagsasaalang-alang sa Performance
- Ang malalaking dataset ay maaaring tumagal ng oras upang mag-load sa mga notebook
- Ang pag-render ng visualisasyon ay maaaring mabagal para sa mga kumplikadong plot
- Ang Vue.js dev server ay nagbibigay-daan sa hot-reload para sa mabilis na iterasyon
- Ang mga production build ay na-optimize at minified

### Mga Tala sa Seguridad
- Walang sensitibong data o mga kredensyal ang dapat i-commit
- Gumamit ng environment variables para sa anumang API keys sa mga cloud lessons
- Ang mga aralin na may kaugnayan sa Azure ay maaaring mangailangan ng mga kredensyal ng Azure account
- Panatilihing updated ang mga dependencies para sa mga security patch

## Pag-aambag sa Mga Pagsasalin
- Ang mga automated na pagsasalin ay pinamamahalaan sa pamamagitan ng GitHub Actions
- Malugod na tinatanggap ang mga manu-manong pagwawasto para sa katumpakan ng pagsasalin
- Sundin ang umiiral na estruktura ng folder ng pagsasalin
- I-update ang mga link ng pagsusulit upang isama ang parameter ng wika: `?loc=fr`
- Subukan ang mga isinaling aralin para sa tamang pag-render

## Kaugnay na Mga Mapagkukunan
- Pangunahing kurikulum: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Discussion Forum: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Iba pang kurikulum ng Microsoft: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Pagpapanatili ng Proyekto
- Regular na pag-update upang mapanatiling kasalukuyan ang nilalaman
- Malugod na tinatanggap ang mga kontribusyon ng komunidad
- Ang mga isyu ay sinusubaybayan sa GitHub
- Ang mga PR ay sinusuri ng mga tagapangalaga ng kurikulum
- Buwanang pagsusuri at pag-update ng nilalaman

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.