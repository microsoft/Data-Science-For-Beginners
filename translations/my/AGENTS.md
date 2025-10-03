<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:44:36+00:00",
  "source_file": "AGENTS.md",
  "language_code": "my"
}
-->
# AGENTS.md

## ပရောဂျက်အကျဉ်းချုပ်

Data Science for Beginners သည် Microsoft Azure Cloud Advocates မှဖန်တီးထားသော ၁၀ ပတ်၊ ၂၀ သင်ခန်းစာများပါဝင်သော အကျယ်အဝန်းရှိသင်ရိုးတစ်ခုဖြစ်သည်။ ဤ repository သည် Jupyter notebooks, interactive quizzes, နှင့် လက်တွေ့လုပ်ငန်းများပါဝင်သော project-based သင်ခန်းစာများမှတဆင့် အခြေခံ data science အယူအဆများကို သင်ကြားပေးသော သင်ယူရေးအရင်းအမြစ်တစ်ခုဖြစ်သည်။

**အဓိကနည်းပညာများ:**
- **Jupyter Notebooks**: Python 3 ကိုအသုံးပြုသော အဓိကသင်ယူရေးအကောင်အထည်
- **Python Libraries**: pandas, numpy, matplotlib ကို data analysis နှင့် visualization အတွက်အသုံးပြု
- **Vue.js 2**: Quiz application (quiz-app folder)
- **Docsify**: Offline access အတွက် documentation site generator
- **Node.js/npm**: JavaScript components အတွက် package management
- **Markdown**: သင်ခန်းစာအကြောင်းအရာနှင့် documentation အားလုံး

**Architecture:**
- ဘာသာစကားများစွာပါဝင်သော သင်ကြားရေး repository
- သင်ခန်းစာ module များ (1-Introduction မှ 6-Data-Science-In-Wild အထိ) အဖြစ်ဖွဲ့စည်းထား
- သင်ခန်းစာတစ်ခုစီတွင် README, notebooks, assignments, နှင့် quizzes ပါဝင်သည်
- သင်ခန်းစာမတိုင်မီ/ပြီးနောက် စမ်းသပ်မှုများအတွက် standalone Vue.js quiz application
- GitHub Codespaces နှင့် VS Code dev containers အထောက်အပံ့

## Setup Commands

### Repository Setup
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Python Environment Setup
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Quiz Application Setup
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

### Visualization Projects Setup
meaningful-visualizations (lesson 13) ကဲ့သို့သော visualization projects အတွက်:
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


## Development Workflow

### Jupyter Notebooks နှင့်အလုပ်လုပ်ခြင်း
1. Repository root တွင် Jupyter ကိုစတင်ပါ: `jupyter notebook`
2. လိုအပ်သော သင်ခန်းစာ folder သို့သွားပါ
3. `.ipynb` ဖိုင်များကိုဖွင့်ပြီး လေ့ကျင့်မှုများကိုလုပ်ဆောင်ပါ
4. Notebooks တွင် ရှင်းလင်းချက်များနှင့် code cells ပါဝင်ပြီး အပြည့်အစုံဖြစ်သည်
5. notebooks များအများစုသည် pandas, numpy, နှင့် matplotlib ကိုအသုံးပြုသည် - ဤ library များကို install လုပ်ထားရန်သေချာပါ

### သင်ခန်းစာဖွဲ့စည်းမှု
သင်ခန်းစာတစ်ခုစီတွင် အများအားဖြင့်:
- `README.md` - သင်ခန်းစာအကြောင်းအရာအဓိကနှင့် သီအိုရီ၊ ဥပမာများ
- `notebook.ipynb` - လက်တွေ့ Jupyter notebook လေ့ကျင့်မှုများ
- `assignment.ipynb` သို့မဟုတ် `assignment.md` - လေ့ကျင့်မှုအလုပ်များ
- `solution/` folder - ဖြေရှင်းချက် notebooks နှင့် code
- `images/` folder - အထောက်အကူပြု visual materials

### Quiz Application Development
- Vue.js 2 application သည် hot-reload ဖြင့် development အတွင်းအလုပ်လုပ်သည်
- Quizzes များကို `quiz-app/src/assets/translations/` တွင်သိမ်းဆည်းထားသည်
- ဘာသာစကားတစ်ခုစီတွင် translation folder (en, fr, es, စသည်) ရှိသည်
- Quiz အရေအတွက်သည် 0 မှစတင်ပြီး 39 အထိရှိသည် (စုစုပေါင်း 40 quizzes)

### Translations ထည့်သွင်းခြင်း
- Translations များကို repository root တွင် `translations/` folder တွင်ထား
- ဘာသာစကားတစ်ခုစီသည် အင်္ဂလိပ်ဘာသာစကားမှ mirrored lesson structure ရှိသည်
- GitHub Actions (co-op-translator.yml) မှတဆင့် automated translation

## Testing Instructions

### Quiz Application Testing
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Notebook Testing
- notebooks အတွက် automated test framework မရှိပါ
- Manual validation: Cell အားလုံးကို အစဉ်လိုက် run လုပ်ပြီး error မရှိကြောင်းသေချာပါ
- Data files များရရှိနိုင်မှုနှင့် output များ generate ဖြစ်ကြောင်းစစ်ဆေးပါ
- Visualizations များမှန်ကန်စွာ render ဖြစ်ကြောင်းစစ်ဆေးပါ

### Documentation Testing
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Code Quality Checks
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Code Style Guidelines

### Python (Jupyter Notebooks)
- Python code အတွက် PEP 8 style guidelines ကိုလိုက်နာပါ
- အချက်အလက်ကိုရှင်းလင်းစွာဖော်ပြသော variable names ကိုအသုံးပြုပါ
- Markdown cells တွင် code cells မတိုင်မီ ရှင်းလင်းချက်များထည့်ပါ
- Code cells များကို concept တစ်ခုစီ သို့မဟုတ် operation တစ်ခုစီအတွက် အာရုံစိုက်ပါ
- Data manipulation အတွက် pandas, visualization အတွက် matplotlib ကိုအသုံးပြုပါ
- Import pattern အများအားဖြင့်:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Vue.js 2 style guide နှင့် best practices ကိုလိုက်နာပါ
- `quiz-app/package.json` တွင် ESLint configuration ရှိသည်
- Vue single-file components (.vue files) ကိုအသုံးပြုပါ
- Component-based architecture ကိုထိန်းသိမ်းပါ
- Commit မလုပ်မီ `npm run lint` ကို run လုပ်ပါ

### Markdown Documentation
- ရှင်းလင်းသော headings hierarchy (# ## ### စသည်) ကိုအသုံးပြုပါ
- Language specifiers ပါသော code blocks ထည့်ပါ
- Images အတွက် alt text ထည့်ပါ
- သက်ဆိုင်သော သင်ခန်းစာများနှင့် အရင်းအမြစ်များ link လုပ်ပါ
- ဖတ်ရှုရလွယ်ကူစေရန် line lengths ကိုသင့်တင့်စွာထားပါ

### File Organization
- သင်ခန်းစာအကြောင်းအရာကို အမှတ်ပေးထားသော folders (01-defining-data-science စသည်) တွင်ထား
- Solutions များကို `solution/` subfolders တွင်ထား
- Translations များကို `translations/` folder တွင် အင်္ဂလိပ် structure ကို mirror လုပ်ထား
- Data files များကို `data/` သို့မဟုတ် သင်ခန်းစာ-specific folders တွင်ထား

## Build and Deployment

### Quiz Application Deployment
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Azure Static Web Apps Deployment
Quiz-app ကို Azure Static Web Apps တွင် deploy လုပ်နိုင်သည်:
1. Azure Static Web App resource တစ်ခုဖန်တီးပါ
2. GitHub repository ကိုချိတ်ဆက်ပါ
3. Build settings ကို configure လုပ်ပါ:
   - App location: `quiz-app`
   - Output location: `dist`
4. GitHub Actions workflow သည် push လုပ်သောအခါ auto-deploy လုပ်မည်

### Documentation Site
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Repository တွင် dev container configuration ပါဝင်သည်
- Codespaces သည် Python နှင့် Node.js environment ကို auto-setup လုပ်သည်
- GitHub UI မှတဆင့် repository ကို Codespace တွင်ဖွင့်ပါ
- Dependencies အားလုံးကို auto-install လုပ်သည်

## Pull Request Guidelines

### Submit မလုပ်မီ
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### PR Title Format
- ရှင်းလင်းသော၊ ဖော်ပြချက်ပေးသော title များကိုအသုံးပြုပါ
- Format: `[Component] Brief description`
- ဥပမာများ:
  - `[Lesson 7] Fix Python notebook import error`
  - `[Quiz App] Add German translation`
  - `[Docs] Update README with new prerequisites`

### Required Checks
- Code အားလုံး error မရှိကြောင်းသေချာပါ
- Notebooks အားလုံးကို အပြည့်အစုံ run လုပ်ပါ
- Vue.js apps များကို build လုပ်ပြီးအောင်မြင်ကြောင်းစစ်ဆေးပါ
- Documentation links အားလုံးအလုပ်လုပ်ကြောင်းစစ်ဆေးပါ
- Quiz application ကိုပြောင်းလဲထားပါက စမ်းသပ်ပါ
- Translations များ structure တူညီမှုရှိကြောင်းအတည်ပြုပါ

### Contribution Guidelines
- ရှိပြီးသား code style နှင့် patterns ကိုလိုက်နာပါ
- ရှုပ်ထွေးသော logic အတွက် ရှင်းလင်းချက် comment များထည့်ပါ
- သက်ဆိုင်သော documentation ကို update လုပ်ပါ
- သင်ခန်းစာ module များအနှံ့ စမ်းသပ်ပါ (သက်ဆိုင်ပါက)
- CONTRIBUTING.md ဖိုင်ကိုကြည့်ပါ

## အပိုအချက်အလက်များ

### Common Libraries Used
- **pandas**: Data manipulation နှင့် analysis
- **numpy**: Numerical computing
- **matplotlib**: Data visualization နှင့် plotting
- **seaborn**: Statistical data visualization (သင်ခန်းစာအချို့)
- **scikit-learn**: Machine learning (အဆင့်မြင့်သင်ခန်းစာများ)

### Data Files နှင့်အလုပ်လုပ်ခြင်း
- Data files များကို `data/` folder သို့မဟုတ် သင်ခန်းစာ-specific directories တွင်ထား
- Notebooks များအများစုသည် relative paths တွင် data files များကိုမျှော်လင့်သည်
- CSV files သည် primary data format ဖြစ်သည်
- Non-relational data ဥပမာများအတွက် JSON ကိုသုံးသော သင်ခန်းစာအချို့ရှိသည်

### Multilingual Support
- Automated GitHub Actions မှတဆင့် 40+ ဘာသာစကား translation များ
- Translation workflow ကို `.github/workflows/co-op-translator.yml` တွင်ထား
- Translations များကို `translations/` folder တွင် language codes ဖြင့်ထား
- Quiz translations များကို `quiz-app/src/assets/translations/` တွင်ထား

### Development Environment Options
1. **Local Development**: Python, Jupyter, Node.js ကို locally install လုပ်ပါ
2. **GitHub Codespaces**: Cloud-based instant development environment
3. **VS Code Dev Containers**: Local container-based development
4. **Binder**: Cloud တွင် notebooks များကို launch လုပ်ပါ (configure လုပ်ထားပါက)

### Lesson Content Guidelines
- သင်ခန်းစာတစ်ခုစီသည် standalone ဖြစ်ပြီး အရင် concept များကိုအခြေခံထားသည်
- Pre-lesson quizzes သည် အရင်အတန်းအကြောင်းအရာကိုစမ်းသပ်သည်
- Post-lesson quizzes သည် သင်ယူမှုကို reinforcement လုပ်သည်
- Assignments များသည် လက်တွေ့လေ့ကျင့်မှုများပေးသည်
- Sketchnotes များသည် visual summaries ပေးသည်

### Troubleshooting Common Issues

**Jupyter Kernel Issues:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**npm Install Failures:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Import Errors in Notebooks:**
- လိုအပ်သော library များအားလုံး install လုပ်ထားကြောင်းစစ်ဆေးပါ
- Python version compatibility ကိုစစ်ဆေးပါ (Python 3.7+ recommend)
- Virtual environment ကို activate လုပ်ထားကြောင်းသေချာပါ

**Docsify Not Loading:**
- Repository root မှ serve လုပ်နေကြောင်းစစ်ဆေးပါ
- `index.html` ရှိကြောင်းစစ်ဆေးပါ
- သင့် network access (port 3000) မှန်ကန်ကြောင်းစစ်ဆေးပါ

### Performance Considerations
- အကြီးမားသော datasets များသည် notebooks တွင် load လုပ်ရန်အချိန်ယူနိုင်သည်
- Visualization rendering သည် ရှုပ်ထွေးသော plots များအတွက်နှေးနိုင်သည်
- Vue.js dev server သည် hot-reload ကို enable လုပ်သည်
- Production builds များသည် optimized နှင့် minified ဖြစ်သည်

### Security Notes
- Sensitive data သို့မဟုတ် credentials များကို commit မလုပ်ပါနှင့်
- Cloud lessons များတွင် API keys အတွက် environment variables ကိုအသုံးပြုပါ
- Azure သက်ဆိုင်သော သင်ခန်းစာများတွင် Azure account credentials လိုအပ်နိုင်သည်
- Security patches အတွက် dependencies များကို update လုပ်ထားပါ

## Contributing to Translations
- Automated translations များကို GitHub Actions မှစီမံခန့်ခွဲထားသည်
- Translation accuracy အတွက် manual corrections များကိုကြိုဆိုပါသည်
- ရှိပြီးသား translation folder structure ကိုလိုက်နာပါ
- Quiz links များကို language parameter ပါအောင် update လုပ်ပါ: `?loc=fr`
- Translated lessons များကို rendering မှန်ကန်ကြောင်းစမ်းသပ်ပါ

## Related Resources
- Main curriculum: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Discussion Forum: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Other Microsoft curricula: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Project Maintenance
- အကြောင်းအရာကို current ဖြစ်အောင် regular updates လုပ်ပါ
- Community contributions များကိုကြိုဆိုပါသည်
- GitHub တွင် issues များကို tracking လုပ်ပါ
- PRs များကို curriculum maintainers မှ review လုပ်ပါ
- Content များကို လစဉ် review နှင့် update လုပ်ပါ

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွဲအချော်များ သို့မဟုတ် အနားယူမှုမှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။