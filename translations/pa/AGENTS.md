<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:14:40+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pa"
}
-->
# AGENTS.md

## ਪ੍ਰੋਜੈਕਟ ਝਲਕ

ਬਿਗਿਨਰਜ਼ ਲਈ ਡਾਟਾ ਸਾਇੰਸ ਮਾਈਕਰੋਸਾਫਟ ਐਜ਼ਯੂਰ ਕਲਾਉਡ ਐਡਵੋਕੇਟਸ ਦੁਆਰਾ ਬਣਾਈ ਗਈ 10 ਹਫ਼ਤਿਆਂ ਦੀ, 20 ਪਾਠਾਂ ਦੀ ਵਿਸਤ੍ਰਿਤ ਪਾਠਕ੍ਰਮ ਹੈ। ਇਹ ਰਿਪੋਜ਼ਟਰੀ ਇੱਕ ਸਿੱਖਣ ਦਾ ਸਰੋਤ ਹੈ ਜੋ ਪ੍ਰੋਜੈਕਟ-ਅਧਾਰਿਤ ਪਾਠਾਂ ਰਾਹੀਂ ਮੂਲ ਡਾਟਾ ਸਾਇੰਸ ਧਾਰਨਾਵਾਂ ਸਿਖਾਉਂਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ Jupyter ਨੋਟਬੁੱਕ, ਇੰਟਰਐਕਟਿਵ ਕਵਿਜ਼, ਅਤੇ ਹੱਥ-ਅਨੁਭਵ ਅਸਾਈਨਮੈਂਟ ਸ਼ਾਮਲ ਹਨ।

**ਮੁੱਖ ਤਕਨਾਲੋਜੀਆਂ:**
- **Jupyter ਨੋਟਬੁੱਕ**: Python 3 ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮੁੱਖ ਸਿੱਖਣ ਮਾਧਿਅਮ
- **Python ਲਾਇਬ੍ਰੇਰੀਆਂ**: pandas, numpy, matplotlib ਡਾਟਾ ਵਿਸ਼ਲੇਸ਼ਣ ਅਤੇ ਵਿਜ਼ੁਅਲਾਈਜ਼ੇਸ਼ਨ ਲਈ
- **Vue.js 2**: ਕਵਿਜ਼ ਐਪਲੀਕੇਸ਼ਨ (quiz-app ਫੋਲਡਰ)
- **Docsify**: ਆਫਲਾਈਨ ਪਹੁੰਚ ਲਈ ਦਸਤਾਵੇਜ਼ ਸਾਈਟ ਜਨਰੇਟਰ
- **Node.js/npm**: ਜਾਵਾਸਕ੍ਰਿਪਟ ਕੰਪੋਨੈਂਟਸ ਲਈ ਪੈਕੇਜ ਮੈਨੇਜਮੈਂਟ
- **Markdown**: ਸਾਰੇ ਪਾਠ ਸਮੱਗਰੀ ਅਤੇ ਦਸਤਾਵੇਜ਼

**ਆਰਕੀਟੈਕਚਰ:**
- ਬਹੁ-ਭਾਸ਼ਾਈ ਸਿੱਖਣ ਰਿਪੋਜ਼ਟਰੀ ਜਿਸ ਵਿੱਚ ਵਿਸਤ੍ਰਿਤ ਅਨੁਵਾਦ ਹਨ
- ਪਾਠ ਮੋਡੀਊਲਾਂ ਵਿੱਚ ਸੰਰਚਿਤ (1-Introduction ਤੋਂ 6-Data-Science-In-Wild)
- ਹਰ ਪਾਠ ਵਿੱਚ README, ਨੋਟਬੁੱਕ, ਅਸਾਈਨਮੈਂਟ ਅਤੇ ਕਵਿਜ਼ ਸ਼ਾਮਲ ਹਨ
- ਪਾਠ ਤੋਂ ਪਹਿਲਾਂ/ਬਾਅਦ ਦੇ ਮੁਲਾਂਕਣ ਲਈ ਸਵਤੰਤਰ Vue.js ਕਵਿਜ਼ ਐਪਲੀਕੇਸ਼ਨ
- GitHub Codespaces ਅਤੇ VS Code dev ਕੰਟੇਨਰ ਸਹਾਇਤਾ

## ਸੈਟਅੱਪ ਕਮਾਂਡ

### ਰਿਪੋਜ਼ਟਰੀ ਸੈਟਅੱਪ
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Python ਵਾਤਾਵਰਣ ਸੈਟਅੱਪ
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### ਕਵਿਜ਼ ਐਪਲੀਕੇਸ਼ਨ ਸੈਟਅੱਪ
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

### Docsify ਦਸਤਾਵੇਜ਼ ਸਰਵਰ
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### ਵਿਜ਼ੁਅਲਾਈਜ਼ੇਸ਼ਨ ਪ੍ਰੋਜੈਕਟ ਸੈਟਅੱਪ
ਜਿਵੇਂ ਕਿ meaningful-visualizations (lesson 13) ਲਈ:
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


## ਵਿਕਾਸ ਵਰਕਫਲੋ

### Jupyter ਨੋਟਬੁੱਕ ਨਾਲ ਕੰਮ ਕਰਨਾ
1. ਰਿਪੋਜ਼ਟਰੀ ਰੂਟ ਵਿੱਚ Jupyter ਸ਼ੁਰੂ ਕਰੋ: `jupyter notebook`
2. ਚਾਹੀਦੇ ਪਾਠ ਫੋਲਡਰ ਵਿੱਚ ਜਾਓ
3. `.ipynb` ਫਾਈਲਾਂ ਖੋਲ੍ਹੋ ਅਤੇ ਅਭਿਆਸ ਕਰੋ
4. ਨੋਟਬੁੱਕ ਵਿੱਚ ਵਿਆਖਿਆਵਾਂ ਅਤੇ ਕੋਡ ਸੈੱਲਾਂ ਸ਼ਾਮਲ ਹਨ
5. ਜ਼ਿਆਦਾਤਰ ਨੋਟਬੁੱਕ pandas, numpy, ਅਤੇ matplotlib ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ - ਇਹਨਾਂ ਨੂੰ ਇੰਸਟਾਲ ਕਰਨਾ ਯਕੀਨੀ ਬਣਾਓ

### ਪਾਠਾਂ ਦੀ ਸੰਰਚਨਾ
ਹਰ ਪਾਠ ਵਿੱਚ ਆਮ ਤੌਰ 'ਤੇ ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ:
- `README.md` - ਮੁੱਖ ਪਾਠ ਸਮੱਗਰੀ ਸਿਧਾਂਤ ਅਤੇ ਉਦਾਹਰਣਾਂ ਨਾਲ
- `notebook.ipynb` - Jupyter ਨੋਟਬੁੱਕ ਅਭਿਆਸ
- `assignment.ipynb` ਜਾਂ `assignment.md` - ਅਸਾਈਨਮੈਂਟ
- `solution/` ਫੋਲਡਰ - ਹੱਲ ਨੋਟਬੁੱਕ ਅਤੇ ਕੋਡ
- `images/` ਫੋਲਡਰ - ਸਹਾਇਕ ਵਿਜ਼ੁਅਲ ਸਮੱਗਰੀ

### ਕਵਿਜ਼ ਐਪਲੀਕੇਸ਼ਨ ਵਿਕਾਸ
- Vue.js 2 ਐਪਲੀਕੇਸ਼ਨ ਵਿਕਾਸ ਦੌਰਾਨ ਹੌਟ-ਰੀਲੋਡ ਨਾਲ
- ਕਵਿਜ਼ `quiz-app/src/assets/translations/` ਵਿੱਚ ਸਟੋਰ ਕੀਤੇ ਗਏ ਹਨ
- ਹਰ ਭਾਸ਼ਾ ਦਾ ਆਪਣਾ ਅਨੁਵਾਦ ਫੋਲਡਰ ਹੈ (en, fr, es, ਆਦਿ)
- ਕਵਿਜ਼ ਨੰਬਰ 0 ਤੋਂ ਸ਼ੁਰੂ ਹੁੰਦੇ ਹਨ ਅਤੇ 39 ਤੱਕ ਜਾਂਦੇ ਹਨ (ਕੁੱਲ 40 ਕਵਿਜ਼)

### ਅਨੁਵਾਦ ਸ਼ਾਮਲ ਕਰਨਾ
- ਅਨੁਵਾਦ `translations/` ਫੋਲਡਰ ਵਿੱਚ ਰਿਪੋਜ਼ਟਰੀ ਰੂਟ 'ਤੇ ਜਾਂਦੇ ਹਨ
- ਹਰ ਭਾਸ਼ਾ ਦਾ ਅੰਗਰੇਜ਼ੀ ਤੋਂ ਮਿਰਰ ਕੀਤਾ ਪਾਠਕ੍ਰਮ ਹੈ
- GitHub Actions ਰਾਹੀਂ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ (co-op-translator.yml)

## ਟੈਸਟਿੰਗ ਨਿਰਦੇਸ਼

### ਕਵਿਜ਼ ਐਪਲੀਕੇਸ਼ਨ ਟੈਸਟਿੰਗ
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### ਨੋਟਬੁੱਕ ਟੈਸਟਿੰਗ
- ਨੋਟਬੁੱਕ ਲਈ ਕੋਈ ਆਟੋਮੈਟਿਕ ਟੈਸਟ ਫਰੇਮਵਰਕ ਨਹੀਂ ਹੈ
- ਮੈਨੂਅਲ ਵੈਰੀਫਿਕੇਸ਼ਨ: ਸਾਰੇ ਸੈੱਲ ਲਗਾਤਾਰ ਚਲਾਓ ਅਤੇ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਕੋਈ ਗਲਤੀ ਨਹੀਂ ਹੈ
- ਡਾਟਾ ਫਾਈਲਾਂ ਪਹੁੰਚਯੋਗ ਹਨ ਅਤੇ ਆਉਟਪੁੱਟ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਜਨਰੇਟ ਹੁੰਦੀ ਹੈ
- ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਵਿਜ਼ੁਅਲਾਈਜ਼ੇਸ਼ਨ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਰੈਂਡਰ ਹੁੰਦੇ ਹਨ

### ਦਸਤਾਵੇਜ਼ ਟੈਸਟਿੰਗ
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### ਕੋਡ ਗੁਣਵੱਤਾ ਚੈੱਕ
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## ਕੋਡ ਸਟਾਈਲ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼

### Python (Jupyter ਨੋਟਬੁੱਕ)
- Python ਕੋਡ ਲਈ PEP 8 ਸਟਾਈਲ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼ਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ
- ਸਪਸ਼ਟ ਵੈਰੀਏਬਲ ਨਾਮ ਵਰਤੋ ਜੋ ਡਾਟਾ ਨੂੰ ਵਿਆਖਿਆ ਕਰਦੇ ਹਨ
- ਕੋਡ ਸੈੱਲਾਂ ਤੋਂ ਪਹਿਲਾਂ ਵਿਆਖਿਆਵਾਂ ਵਾਲੇ ਮਾਰਕਡਾਊਨ ਸੈੱਲ ਸ਼ਾਮਲ ਕਰੋ
- ਕੋਡ ਸੈੱਲਾਂ ਨੂੰ ਇੱਕਲੇ ਧਾਰਨਾ ਜਾਂ ਕਾਰਵਾਈ 'ਤੇ ਕੇਂਦਰਿਤ ਰੱਖੋ
- pandas ਡਾਟਾ ਮੈਨਿਪੂਲੇਸ਼ਨ ਲਈ, matplotlib ਵਿਜ਼ੁਅਲਾਈਜ਼ੇਸ਼ਨ ਲਈ ਵਰਤੋ
- ਆਮ ਇੰਪੋਰਟ ਪੈਟਰਨ:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Vue.js 2 ਸਟਾਈਲ ਗਾਈਡ ਅਤੇ ਬਿਹਤਰ ਅਭਿਆਸਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ
- ESLint ਕਨਫਿਗਰੇਸ਼ਨ `quiz-app/package.json` ਵਿੱਚ
- Vue ਸਿੰਗਲ-ਫਾਈਲ ਕੰਪੋਨੈਂਟ (.vue ਫਾਈਲਾਂ) ਵਰਤੋ
- ਕੰਪੋਨੈਂਟ-ਅਧਾਰਿਤ ਆਰਕੀਟੈਕਚਰ ਨੂੰ ਬਣਾਓ
- ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ `npm run lint` ਚਲਾਓ

### Markdown ਦਸਤਾਵੇਜ਼
- ਸਪਸ਼ਟ ਹੈਡਿੰਗ ਹਾਇਰਾਰਕੀ (# ## ### ਆਦਿ) ਵਰਤੋ
- ਭਾਸ਼ਾ ਨਿਰਧਾਰਕਾਂ ਨਾਲ ਕੋਡ ਬਲਾਕ ਸ਼ਾਮਲ ਕਰੋ
- ਚਿੱਤਰਾਂ ਲਈ alt ਟੈਕਸਟ ਸ਼ਾਮਲ ਕਰੋ
- ਸੰਬੰਧਿਤ ਪਾਠਾਂ ਅਤੇ ਸਰੋਤਾਂ ਨਾਲ ਲਿੰਕ ਕਰੋ
- ਪੜ੍ਹਨਯੋਗਤਾ ਲਈ ਲਾਈਨ ਦੀ ਲੰਬਾਈ ਵਾਜਬ ਰੱਖੋ

### ਫਾਈਲ ਸੰਰਚਨਾ
- ਪਾਠ ਸਮੱਗਰੀ ਗਿਣਤੀ ਫੋਲਡਰਾਂ ਵਿੱਚ (01-defining-data-science, ਆਦਿ)
- ਹੱਲਾਂ ਸਮਰਪਿਤ `solution/` ਸਬਫੋਲਡਰਾਂ ਵਿੱਚ
- ਅਨੁਵਾਦ `translations/` ਫੋਲਡਰ ਵਿੱਚ ਅੰਗਰੇਜ਼ੀ ਸੰਰਚਨਾ ਨੂੰ ਮਿਰਰ ਕਰਦੇ ਹਨ
- ਡਾਟਾ ਫਾਈਲਾਂ `data/` ਜਾਂ ਪਾਠ-ਵਿਸ਼ੇਸ਼ ਫੋਲਡਰਾਂ ਵਿੱਚ ਰੱਖੋ

## ਬਿਲਡ ਅਤੇ ਡਿਪਲੌਇਮੈਂਟ

### ਕਵਿਜ਼ ਐਪਲੀਕੇਸ਼ਨ ਡਿਪਲੌਇਮੈਂਟ
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Azure Static Web Apps ਡਿਪਲੌਇਮੈਂਟ
ਕਵਿਜ਼-ਐਪ ਨੂੰ Azure Static Web Apps 'ਤੇ ਡਿਪਲੌਇ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ:
1. Azure Static Web App ਸਰੋਤ ਬਣਾਓ
2. GitHub ਰਿਪੋਜ਼ਟਰੀ ਨਾਲ ਕਨੈਕਟ ਕਰੋ
3. ਬਿਲਡ ਸੈਟਿੰਗਾਂ ਕਨਫਿਗਰ ਕਰੋ:
   - ਐਪ ਸਥਾਨ: `quiz-app`
   - ਆਉਟਪੁੱਟ ਸਥਾਨ: `dist`
4. GitHub Actions ਵਰਕਫਲੋ ਪੁਸ਼ 'ਤੇ ਆਟੋ-ਡਿਪਲੌਇ ਕਰੇਗਾ

### ਦਸਤਾਵੇਜ਼ ਸਾਈਟ
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ dev ਕੰਟੇਨਰ ਕਨਫਿਗਰੇਸ਼ਨ ਸ਼ਾਮਲ ਹੈ
- Codespaces ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ Python ਅਤੇ Node.js ਵਾਤਾਵਰਣ ਸੈਟਅੱਪ ਕਰਦਾ ਹੈ
- GitHub UI ਰਾਹੀਂ ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ Codespace ਵਿੱਚ ਖੋਲ੍ਹੋ
- ਸਾਰੇ ਡਿਪੈਂਡੈਂਸੀਜ਼ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਇੰਸਟਾਲ ਹੁੰਦੀਆਂ ਹਨ

## ਪੁਲ ਰਿਕਵੈਸਟ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼

### ਸਬਮਿਟ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### PR ਟਾਈਟਲ ਫਾਰਮੈਟ
- ਸਪਸ਼ਟ, ਵਰਣਨਾਤਮਕ ਟਾਈਟਲ ਵਰਤੋ
- ਫਾਰਮੈਟ: `[Component] Brief description`
- ਉਦਾਹਰਣ:
  - `[Lesson 7] Fix Python notebook import error`
  - `[Quiz App] Add German translation`
  - `[Docs] Update README with new prerequisites`

### ਲਾਜ਼ਮੀ ਚੈੱਕ
- ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਾਰਾ ਕੋਡ ਗਲਤੀ ਤੋਂ ਬਿਨਾਂ ਚਲਦਾ ਹੈ
- ਨੋਟਬੁੱਕ ਪੂਰੀ ਤਰ੍ਹਾਂ ਚਲਾਉਣ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ
- Vue.js ਐਪਸ ਸਫਲਤਾਪੂਰਵਕ ਬਣਾਉਣ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ
- ਦਸਤਾਵੇਜ਼ ਲਿੰਕਾਂ ਦੀ ਜਾਂਚ ਕਰੋ
- ਜੇਕਰ ਸੋਧ ਕੀਤੀ ਗਈ ਹੈ ਤਾਂ ਕਵਿਜ਼ ਐਪਲੀਕੇਸ਼ਨ ਟੈਸਟ ਕਰੋ
- ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਅਨੁਵਾਦ ਸੰਰਚਨਾ ਸਥਿਰ ਹੈ

### ਯੋਗਦਾਨ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼
- ਮੌਜੂਦਾ ਕੋਡ ਸਟਾਈਲ ਅਤੇ ਪੈਟਰਨ ਦੀ ਪਾਲਣਾ ਕਰੋ
- ਜਟਿਲ ਲਾਜ਼ਿਕ ਲਈ ਵਿਆਖਿਆਵਾਂ ਵਾਲੇ ਟਿੱਪਣੀਆਂ ਸ਼ਾਮਲ ਕਰੋ
- ਸੰਬੰਧਿਤ ਦਸਤਾਵੇਜ਼ ਅਪਡੇਟ ਕਰੋ
- ਜੇਕਰ ਲਾਗੂ ਹੋਵੇ ਤਾਂ ਵੱਖ-ਵੱਖ ਪਾਠ ਮੋਡੀਊਲਾਂ 'ਤੇ ਬਦਲਾਵਾਂ ਟੈਸਟ ਕਰੋ
- CONTRIBUTING.md ਫਾਈਲ ਦੀ ਸਮੀਖਿਆ ਕਰੋ

## ਵਾਧੂ ਨੋਟਸ

### ਆਮ ਲਾਇਬ੍ਰੇਰੀਆਂ ਦੀ ਵਰਤੋਂ
- **pandas**: ਡਾਟਾ ਮੈਨਿਪੂਲੇਸ਼ਨ ਅਤੇ ਵਿਸ਼ਲੇਸ਼ਣ
- **numpy**: ਗਣਿਤੀ ਗਣਨਾ
- **matplotlib**: ਡਾਟਾ ਵਿਜ਼ੁਅਲਾਈਜ਼ੇਸ਼ਨ ਅਤੇ ਪਲਾਟਿੰਗ
- **seaborn**: ਸਾਂਖਿਕ ਡਾਟਾ ਵਿਜ਼ੁਅਲਾਈਜ਼ੇਸ਼ਨ (ਕੁਝ ਪਾਠਾਂ ਵਿੱਚ)
- **scikit-learn**: ਮਸ਼ੀਨ ਲਰਨਿੰਗ (ਉੱਚ ਪੱਧਰ ਦੇ ਪਾਠ)

### ਡਾਟਾ ਫਾਈਲਾਂ ਨਾਲ ਕੰਮ ਕਰਨਾ
- ਡਾਟਾ ਫਾਈਲਾਂ `data/` ਫੋਲਡਰ ਜਾਂ ਪਾਠ-ਵਿਸ਼ੇਸ਼ ਡਾਇਰੈਕਟਰੀਜ਼ ਵਿੱਚ ਸਥਿਤ ਹਨ
- ਜ਼ਿਆਦਾਤਰ ਨੋਟਬੁੱਕ ਡਾਟਾ ਫਾਈਲਾਂ ਨੂੰ ਰਿਲੇਟਿਵ ਪਾਥ ਵਿੱਚ ਉਮੀਦ ਕਰਦੇ ਹਨ
- CSV ਫਾਈਲਾਂ ਮੁੱਖ ਡਾਟਾ ਫਾਰਮੈਟ ਹਨ
- ਕੁਝ ਪਾਠ JSON ਨੂੰ ਗੈਰ-ਸੰਬੰਧਿਤ ਡਾਟਾ ਉਦਾਹਰਣਾਂ ਲਈ ਵਰਤਦੇ ਹਨ

### ਬਹੁਭਾਸ਼ਾਈ ਸਹਾਇਤਾ
- 40+ ਭਾਸ਼ਾ ਅਨੁਵਾਦ GitHub Actions ਰਾਹੀਂ ਆਟੋਮੈਟਿਕ
- ਅਨੁਵਾਦ ਵਰਕਫਲੋ `.github/workflows/co-op-translator.yml` ਵਿੱਚ
- ਅਨੁਵਾਦ `translations/` ਫੋਲਡਰ ਵਿੱਚ ਭਾਸ਼ਾ ਕੋਡਾਂ ਨਾਲ
- ਕਵਿਜ਼ ਅਨੁਵਾਦ `quiz-app/src/assets/translations/` ਵਿੱਚ

### ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਵਿਕਲਪ
1. **ਸਥਾਨਕ ਵਿਕਾਸ**: ਸਥਾਨਕ ਤੌਰ 'ਤੇ Python, Jupyter, Node.js ਇੰਸਟਾਲ ਕਰੋ
2. **GitHub Codespaces**: ਕਲਾਉਡ-ਅਧਾਰਿਤ ਤੁਰੰਤ ਵਿਕਾਸ ਵਾਤਾਵਰਣ
3. **VS Code Dev Containers**: ਸਥਾਨਕ ਕੰਟੇਨਰ-ਅਧਾਰਿਤ ਵਿਕਾਸ
4. **Binder**: ਕਲਾਉਡ ਵਿੱਚ ਨੋਟਬੁੱਕ ਲਾਂਚ ਕਰੋ (ਜੇਕਰ ਕਨਫਿਗਰ ਕੀਤਾ ਗਿਆ)

### ਪਾਠ ਸਮੱਗਰੀ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼
- ਹਰ ਪਾਠ ਸਵਤੰਤਰ ਹੈ ਪਰ ਪਿਛਲੇ ਧਾਰਨਾਵਾਂ 'ਤੇ ਬਣਦਾ ਹੈ
- ਪਾਠ ਤੋਂ ਪਹਿਲਾਂ ਕਵਿਜ਼ ਪਿਛਲੇ ਗਿਆਨ ਦੀ ਜਾਂਚ ਕਰਦੇ ਹਨ
- ਪਾਠ ਤੋਂ ਬਾਅਦ ਕਵਿਜ਼ ਸਿੱਖਣ ਨੂੰ ਮਜ਼ਬੂਤ ਕਰਦੇ ਹਨ
- ਅਸਾਈਨਮੈਂਟ ਹੱਥ-ਅਨੁਭਵ ਅਭਿਆਸ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ
- ਸਕੈਚਨੋਟਸ ਵਿਜ਼ੁਅਲ ਸੰਖੇਪ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ

### ਆਮ ਸਮੱਸਿਆਵਾਂ ਦਾ ਨਿਪਟਾਰਾ

**Jupyter Kernel ਸਮੱਸਿਆਵਾਂ:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**npm ਇੰਸਟਾਲ ਫੇਲ੍ਹ:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**ਨੋਟਬੁੱਕ ਵਿੱਚ ਇੰਪੋਰਟ ਗਲਤੀਆਂ:**
- ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਾਰੀਆਂ ਲੋੜੀਂਦੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਸਟਾਲ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ
- Python ਵਰਜਨ ਅਨੁਕੂਲਤਾ ਦੀ ਜਾਂਚ ਕਰੋ (Python 3.7+ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਗਈ ਹੈ)
- ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਐਕਟੀਵੇਟ ਹੈ

**Docsify ਲੋਡ ਨਹੀਂ ਹੋ ਰਿਹਾ:**
- ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ ਰਿਪੋਜ਼ਟਰੀ ਰੂਟ ਤੋਂ ਸਰਵ ਕਰ ਰਹੇ ਹੋ
- ਜਾਂਚ ਕਰੋ ਕਿ `index.html` ਮੌਜੂਦ ਹੈ
- ਸਹੀ ਨੈਟਵਰਕ ਪਹੁੰਚ (ਪੋਰਟ 3000) ਯਕੀਨੀ ਬਣਾਓ

### ਪ੍ਰਦਰਸ਼ਨ ਵਿਚਾਰ
- ਵੱਡੇ ਡਾਟਾਸੈਟ ਨੋਟਬੁੱਕ ਵਿੱਚ ਲੋਡ ਕਰਨ ਵਿੱਚ ਸਮਾਂ ਲੈ ਸਕਦੇ ਹਨ
- ਜਟਿਲ ਪਲਾਟਾਂ ਲਈ ਵਿਜ਼ੁਅਲਾਈਜ਼ੇਸ਼ਨ ਰੈਂਡਰਿੰਗ ਹੌਲੀ ਹੋ ਸਕਦੀ ਹੈ
- Vue.js dev ਸਰਵਰ ਤੇਜ਼ ਦੁਹਰਾਈ ਲਈ ਹੌਟ-ਰੀਲੋਡ ਸਹਾਇਤਾ ਦਿੰਦਾ ਹੈ
- ਪ੍ਰੋਡਕਸ਼ਨ ਬਿਲਡਸ ਅਨੁਕੂਲਿਤ ਅਤੇ ਮਿਨੀਫਾਈਡ ਹੁੰਦੇ ਹਨ

### ਸੁਰੱਖਿਆ ਨੋਟਸ
- ਕੋਈ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟਾ ਜਾਂ ਪ੍ਰਮਾਣ ਪੱਤਰ ਕਮਿਟ ਨਹੀਂ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ
- ਕਲਾਉਡ ਪਾਠਾਂ ਵਿੱਚ ਕੋਈ ਵੀ API ਕੁੰਜੀਆਂ ਲਈ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਵਰਤੋ
- Azure-ਸੰਬੰਧਿਤ ਪਾਠਾਂ ਨੂੰ Azure ਖਾਤੇ ਦੇ ਪ੍ਰਮਾਣ ਪੱਤਰਾਂ ਦੀ ਲੋੜ ਹੋ ਸਕਦੀ ਹੈ
- ਸੁਰੱਖਿਆ ਪੈਚਾਂ ਲਈ ਡਿਪੈਂਡੈਂਸੀਜ਼ ਨੂੰ ਅਪਡੇਟ ਰੱਖੋ

## ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਯੋਗਦਾਨ
- GitHub Actions ਰਾਹੀਂ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਪ੍ਰਬੰਧਿਤ
- ਅਨੁਵਾਦ ਸਹੀਤਾ ਲਈ ਮੈਨੂਅਲ ਸੁਧਾਰਾਂ ਦਾ ਸਵਾਗਤ ਹੈ
- ਮੌਜੂਦਾ ਅਨੁਵਾਦ ਫੋਲਡਰ ਸੰਰਚਨਾ ਦੀ ਪਾਲਣਾ ਕਰੋ
- ਕਵਿਜ਼ ਲਿੰਕਾਂ ਨੂੰ ਭਾਸ਼ਾ ਪੈਰਾਮੀਟਰ ਸ਼ਾਮਲ ਕਰਨ ਲਈ ਅਪਡੇਟ

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।