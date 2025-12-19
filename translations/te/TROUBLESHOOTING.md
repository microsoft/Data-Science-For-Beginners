<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-12-19T12:52:41+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "te"
}
-->
# సమస్య పరిష్కరణ గైడ్

ఈ గైడ్ Data Science for Beginners పాఠ్యాంశంతో పని చేస్తూ మీరు ఎదుర్కొనే సాధారణ సమస్యలకు పరిష్కారాలను అందిస్తుంది.

## విషయ సూచిక

- [Python మరియు Jupyter సమస్యలు](../..)
- [ప్యాకేజ్ మరియు ఆధారిత సమస్యలు](../..)
- [Jupyter నోట్‌బుక్ సమస్యలు](../..)
- [క్విజ్ అప్లికేషన్ సమస్యలు](../..)
- [Git మరియు GitHub సమస్యలు](../..)
- [Docsify డాక్యుమెంటేషన్ సమస్యలు](../..)
- [డేటా మరియు ఫైల్ సమస్యలు](../..)
- [పనితీరు సమస్యలు](../..)
- [అదనపు సహాయం పొందడం](../..)

## Python మరియు Jupyter సమస్యలు

### Python కనుగొనబడలేదు లేదా తప్పు వెర్షన్

**సమస్య:** `python: command not found` లేదా తప్పు Python వెర్షన్

**పరిష్కారం:**

```bash
# పైథాన్ వెర్షన్‌ను తనిఖీ చేయండి
python --version
python3 --version

# పైథాన్ 3 'python3' గా ఇన్‌స్టాల్ అయితే, అలియాస్ సృష్టించండి
# macOS/Linux లో, ~/.bashrc లేదా ~/.zshrc లో జోడించండి:
alias python=python3
alias pip=pip3

# లేదా python3 ను స్పష్టంగా ఉపయోగించండి
python3 -m pip install jupyter
```

**Windows పరిష్కారం:**
1. [python.org](https://www.python.org/) నుండి Python ను మళ్లీ ఇన్‌స్టాల్ చేయండి
2. ఇన్‌స్టాలేషన్ సమయంలో, "Add Python to PATH" ను ఎంచుకోండి
3. మీ టెర్మినల్/కమాండ్ ప్రాంప్ట్‌ను రీస్టార్ట్ చేయండి

### వర్చువల్ ఎన్విరాన్‌మెంట్ యాక్టివేషన్ సమస్యలు

**సమస్య:** వర్చువల్ ఎన్విరాన్‌మెంట్ యాక్టివేట్ అవ్వడం లేదు

**పరిష్కారం:**

**Windows:**
```bash
# మీరు ఎగ్జిక్యూషన్ పాలసీ లోపం పొందితే
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# అప్పుడు యాక్టివేట్ చేయండి
venv\Scripts\activate
```

**macOS/Linux:**
```bash
# యాక్టివేట్ స్క్రిప్ట్ అమలు చేయదగినదిగా ఉండాలి
chmod +x venv/bin/activate

# ఆపై యాక్టివేట్ చేయండి
source venv/bin/activate
```

**యాక్టివేషన్ నిర్ధారించుకోండి:**
```bash
# మీ ప్రాంప్ట్ (venv) చూపించాలి
# Python స్థానం తనిఖీ చేయండి
which python  # venv ను సూచించాలి
```

### Jupyter కర్నెల్ సమస్యలు

**సమస్య:** "Kernel not found" లేదా "Kernel keeps dying"

**పరిష్కారం:**

```bash
# కర్నెల్‌ను మళ్లీ ఇన్‌స్టాల్ చేయండి
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# లేదా డిఫాల్ట్ కర్నెల్‌ను ఉపయోగించండి
python -m ipykernel install --user

# జూపిటర్‌ను రీస్టార్ట్ చేయండి
jupyter notebook
```

**సమస్య:** Jupyterలో తప్పు Python వెర్షన్

**పరిష్కారం:**
```bash
# మీ వర్చువల్ ఎన్విరాన్‌మెంట్‌లో Jupyter ను ఇన్‌స్టాల్ చేయండి
source venv/bin/activate  # ముందుగా యాక్టివేట్ చేయండి
pip install jupyter ipykernel

# కర్నెల్‌ను రిజిస్టర్ చేయండి
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# Jupyter లో, Kernel -> Change kernel -> Python (venv) ను ఎంచుకోండి
```

## ప్యాకేజ్ మరియు ఆధారిత సమస్యలు

### ఇంపోర్ట్ లోపాలు

**సమస్య:** `ModuleNotFoundError: No module named 'pandas'` (లేదా ఇతర ప్యాకేజీలు)

**పరిష్కారం:**

```bash
# వర్చువల్ ఎన్విరాన్‌మెంట్ సక్రియమై ఉందో లేదో నిర్ధారించుకోండి
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# లేని ప్యాకేజీని ఇన్‌స్టాల్ చేయండి
pip install pandas

# అన్ని సాధారణ ప్యాకేజీలను ఇన్‌స్టాల్ చేయండి
pip install jupyter pandas numpy matplotlib seaborn scikit-learn

# ఇన్‌స్టాలేషన్‌ను ధృవీకరించండి
python -c "import pandas; print(pandas.__version__)"
```

### Pip ఇన్‌స్టాలేషన్ విఫలమవడం

**సమస్య:** `pip install` అనుమతి లోపాలతో విఫలమవుతుంది

**పరిష్కారం:**

```bash
# --user ఫ్లాగ్ ఉపయోగించండి
pip install --user package-name

# లేదా వర్చువల్ ఎన్విరాన్‌మెంట్ ఉపయోగించండి (సిఫార్సు చేయబడింది)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**సమస్య:** `pip install` SSL సర్టిఫికేట్ లోపాలతో విఫలమవుతుంది

**పరిష్కారం:**

```bash
# ముందుగా పిప్‌ను నవీకరించండి
python -m pip install --upgrade pip

# నమ్మకమైన హోస్ట్‌తో ఇన్‌స్టాల్ చేయడానికి ప్రయత్నించండి (తాత్కాలిక పరిష్కారం)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### ప్యాకేజ్ వెర్షన్ విరుద్ధతలు

**సమస్య:** అనుకూలం కాని ప్యాకేజ్ వెర్షన్లు

**పరిష్కారం:**

```bash
# కొత్త వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించండి
python -m venv venv-new
source venv-new/bin/activate  # లేదా Windows లో venv-new\Scripts\activate

# అవసరమైతే నిర్దిష్ట సంస్కరణలతో ప్యాకేజీలను ఇన్‌స్టాల్ చేయండి
pip install pandas==1.3.0
pip install numpy==1.21.0

# లేదా pip కు ఆధారాలను పరిష్కరించనివ్వండి
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

## Jupyter నోట్‌బుక్ సమస్యలు

### Jupyter ప్రారంభం కావడం లేదు

**సమస్య:** `jupyter notebook` కమాండ్ కనుగొనబడలేదు

**పరిష్కారం:**

```bash
# జూపిటర్‌ను ఇన్‌స్టాల్ చేయండి
pip install jupyter

# లేదా python -m ఉపయోగించండి
python -m jupyter notebook

# అవసరమైతే PATH లో చేర్చండి (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### నోట్‌బుక్ లోడ్ లేదా సేవ్ అవ్వడం లేదు

**సమస్య:** "Notebook failed to load" లేదా సేవ్ లోపాలు

**పరిష్కారం:**

1. ఫైల్ అనుమతులను తనిఖీ చేయండి
```bash
# మీరు రాయడానికి అనుమతులు ఉన్నాయో నిర్ధారించుకోండి
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # అవసరమైతే
```

2. ఫైల్ కరప్షన్ కోసం తనిఖీ చేయండి
```bash
# JSON నిర్మాణాన్ని తనిఖీ చేయడానికి టెక్స్ట్ ఎడిటర్‌లో తెరవడానికి ప్రయత్నించండి
# దెబ్బతిన్నట్లయితే కంటెంట్‌ను కొత్త నోట్‌బుక్‌కు కాపీ చేయండి
```

3. Jupyter క్యాషే క్లియర్ చేయండి
```bash
jupyter notebook --clear-cache
```

### సెల్ అమలు కావడం లేదు

**సమస్య:** సెల్ "In [*]" వద్ద అడ్డుకుంటోంది లేదా చాలా సమయం తీసుకుంటోంది

**పరిష్కారం:**

1. **కర్నెల్‌ను అంతరాయం చేయండి**: "Interrupt" బటన్ క్లిక్ చేయండి లేదా `I, I` నొక్కండి
2. **కర్నెల్‌ను రీస్టార్ట్ చేయండి**: Kernel మెనూ → Restart
3. మీ కోడ్‌లో **అనంత లూప్‌లు** ఉన్నాయా చూడండి
4. **ఫలితాన్ని క్లియర్ చేయండి**: సెల్ → All Output → Clear

### ప్లాట్లు ప్రదర్శించబడడం లేదు

**సమస్య:** `matplotlib` ప్లాట్లు నోట్‌బుక్‌లో చూపించబడడం లేదు

**పరిష్కారం:**

```python
# నోట్‌బుక్ టాప్‌లో మేజిక్ కమాండ్‌ను జోడించండి
%matplotlib inline

import matplotlib.pyplot as plt

# ప్లాట్ సృష్టించండి
plt.plot([1, 2, 3, 4])
plt.show()  # show() ను పిలవడం నిర్ధారించుకోండి
```

**ఇంటరాక్టివ్ ప్లాట్లకు ప్రత్యామ్నాయం:**
```python
%matplotlib notebook
# లేదా
%matplotlib widget
```

## క్విజ్ అప్లికేషన్ సమస్యలు

### npm install విఫలమవుతుంది

**సమస్య:** `npm install` సమయంలో లోపాలు

**పరిష్కారం:**

```bash
# npm క్యాషేను క్లియర్ చేయండి
npm cache clean --force

# node_modules మరియు package-lock.json ను తొలగించండి
rm -rf node_modules package-lock.json

# మళ్లీ ఇన్‌స్టాల్ చేయండి
npm install

# ఇంకా విఫలమైతే, legacy peer deps తో ప్రయత్నించండి
npm install --legacy-peer-deps
```

### Quiz App ప్రారంభం కావడం లేదు

**సమస్య:** `npm run serve` విఫలమవుతుంది

**పరిష్కారం:**

```bash
# Node.js వెర్షన్‌ను తనిఖీ చేయండి
node --version  # 12.x లేదా అంతకంటే ఎక్కువ ఉండాలి

# డిపెండెన్సీలను మళ్లీ ఇన్‌స్టాల్ చేయండి
cd quiz-app
rm -rf node_modules package-lock.json
npm install

# వేరే పోర్ట్ ప్రయత్నించండి
npm run serve -- --port 8081
```

### పోర్ట్ ఇప్పటికే ఉపయోగంలో ఉంది

**సమస్య:** "Port 8080 is already in use"

**పరిష్కారం:**

```bash
# పోర్ట్ 8080 పై ప్రాసెస్‌ను కనుగొని ముగించండి
# macOS/Linux:
lsof -ti:8080 | xargs kill -9

# Windows:
netstat -ano | findstr :8080
taskkill /PID <PID> /F

# లేదా వేరే పోర్ట్ ఉపయోగించండి
npm run serve -- --port 8081
```

### Quiz లోడ్ అవ్వడం లేదా ఖాళీ పేజీ

**సమస్య:** Quiz యాప్ లోడ్ అవుతుంది కానీ ఖాళీ పేజీ చూపిస్తుంది

**పరిష్కారం:**

1. బ్రౌజర్ కన్సోల్ లో లోపాలు తనిఖీ చేయండి (F12)
2. బ్రౌజర్ క్యాషే మరియు కుకీలను క్లియర్ చేయండి
3. వేరే బ్రౌజర్ ప్రయత్నించండి
4. జావాస్క్రిప్ట్ ఎనేబుల్ ఉందని నిర్ధారించుకోండి
5. అడ్బ్లాకర్లు జోక్యం చేస్తున్నాయా చూడండి

```bash
# యాప్‌ను మళ్లీ నిర్మించండి
npm run build
npm run serve
```

## Git మరియు GitHub సమస్యలు

### Git గుర్తించబడడం లేదు

**సమస్య:** `git: command not found`

**పరిష్కారం:**

**Windows:**
- [git-scm.com](https://git-scm.com/) నుండి Git ఇన్‌స్టాల్ చేయండి
- ఇన్‌స్టాలేషన్ తర్వాత టెర్మినల్‌ను రీస్టార్ట్ చేయండి

**macOS:**

> **గమనిక:** మీరు Homebrew ఇన్‌స్టాల్ చేయకపోతే, ముందుగా [https://brew.sh/](https://brew.sh/) వద్ద సూచనలను అనుసరించండి.
```bash
# హోంబ్రూ ద్వారా ఇన్‌స్టాల్ చేయండి
brew install git

# లేదా Xcode కమాండ్ లైన్ టూల్స్ ఇన్‌స్టాల్ చేయండి
xcode-select --install
```

**Linux:**
```bash
sudo apt-get install git  # డెబియన్/ఉబుంటు
sudo dnf install git      # ఫెడోరా
```

### క్లోన్ విఫలమవుతుంది

**సమస్య:** `git clone` ధృవీకరణ లోపాలతో విఫలమవుతుంది

**పరిష్కారం:**

```bash
# HTTPS URL ఉపయోగించండి
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# మీరు GitHub లో 2FA సక్రియం చేసుకున్నట్లయితే, Personal Access Token ఉపయోగించండి
# టోకెన్ సృష్టించండి: https://github.com/settings/tokens
# అడిగినప్పుడు పాస్వర్డ్ గా టోకెన్ ఉపయోగించండి
```

### అనుమతి నిరాకరించబడింది (publickey)

**సమస్య:** SSH కీ ధృవీకరణ విఫలమవుతుంది

**పరిష్కారం:**

```bash
# SSH కీని సృష్టించండి
ssh-keygen -t ed25519 -C "your_email@example.com"

# కీని ssh-agent కు జోడించండి
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# పబ్లిక్ కీని GitHub కు జోడించండి
# కీని కాపీ చేయండి: cat ~/.ssh/id_ed25519.pub
# ఇక్కడ జోడించండి: https://github.com/settings/keys
```

## Docsify డాక్యుమెంటేషన్ సమస్యలు

### Docsify కమాండ్ కనుగొనబడలేదు

**సమస్య:** `docsify: command not found`

**పరిష్కారం:**

```bash
# గ్లోబల్‌గా ఇన్‌స్టాల్ చేయండి
npm install -g docsify-cli

# macOS/Linuxలో అనుమతి లోపం ఉంటే
sudo npm install -g docsify-cli

# ఇన్‌స్టాలేషన్‌ను ధృవీకరించండి
docsify --version

# ఇంకా కనబడకపోతే, npm గ్లోబల్ పాత్‌ను జోడించండి
# npm గ్లోబల్ పాత్‌ను కనుగొనండి
npm config get prefix

# PATHలో జోడించండి (~/.bashrc లేదా ~/.zshrcలో జోడించండి)
export PATH="$PATH:/usr/local/bin"
```

### డాక్యుమెంటేషన్ లోడ్ అవ్వడం లేదు

**సమస్య:** Docsify సర్వ్ చేస్తోంది కానీ కంటెంట్ లోడ్ అవ్వడం లేదు

**పరిష్కారం:**

```bash
# మీరు రిపాజిటరీ రూట్‌లో ఉన్నారని నిర్ధారించుకోండి
cd Data-Science-For-Beginners

# index.html కోసం తనిఖీ చేయండి
ls index.html

# నిర్దిష్ట పోర్ట్‌తో సర్వ్ చేయండి
docsify serve --port 3000

# బ్రౌజర్ కన్సోల్‌లో లోపాలను తనిఖీ చేయండి (F12)
```

### చిత్రాలు ప్రదర్శించబడడం లేదు

**సమస్య:** చిత్రాలు బ్రోకెన్ లింక్ ఐకాన్ చూపిస్తున్నాయి

**పరిష్కారం:**

1. చిత్రం మార్గాలు రిలేటివ్‌గా ఉన్నాయా తనిఖీ చేయండి
2. చిత్రం ఫైళ్లు రిపోజిటరీలో ఉన్నాయా నిర్ధారించుకోండి
3. బ్రౌజర్ క్యాషే క్లియర్ చేయండి
4. ఫైల్ ఎక్స్‌టెన్షన్లు సరిపోతున్నాయా తనిఖీ చేయండి (కొన్ని సిస్టమ్స్‌లో కేస్-సెన్సిటివ్)

## డేటా మరియు ఫైల్ సమస్యలు

### ఫైల్ కనుగొనబడలేదు లోపాలు

**సమస్య:** డేటా లోడ్ చేస్తున్నప్పుడు `FileNotFoundError`

**పరిష్కారం:**

```python
import os

# ప్రస్తుత పని డైరెక్టరీని తనిఖీ చేయండి
print(os.getcwd())

# సంపూర్ణ మార్గాన్ని ఉపయోగించండి
data_path = os.path.join(os.getcwd(), 'data', 'filename.csv')
df = pd.read_csv(data_path)

# లేదా నోట్‌బుక్ స్థానం నుండి సంబంధిత మార్గాన్ని ఉపయోగించండి
df = pd.read_csv('../data/filename.csv')

# ఫైల్ ఉన్నదో లేదో నిర్ధారించండి
print(os.path.exists('data/filename.csv'))
```

### CSV చదవడంలో లోపాలు

**సమస్య:** CSV ఫైళ్లు చదవడంలో లోపాలు

**పరిష్కారం:**

```python
import pandas as pd

# వేరే ఎన్‌కోడింగ్స్ ప్రయత్నించండి
df = pd.read_csv('file.csv', encoding='utf-8')
# లేదా
df = pd.read_csv('file.csv', encoding='latin-1')
# లేదా
df = pd.read_csv('file.csv', encoding='ISO-8859-1')

# లేని విలువలను నిర్వహించండి
df = pd.read_csv('file.csv', na_values=['NA', 'N/A', ''])

# కామా కాకపోతే డెలిమిటర్‌ను పేర్కొనండి
df = pd.read_csv('file.csv', delimiter=';')
```

### పెద్ద డేటాసెట్‌లతో మెమరీ లోపాలు

**సమస్య:** పెద్ద ఫైళ్లు లోడ్ చేస్తున్నప్పుడు `MemoryError`

**పరిష్కారం:**

```python
# భాగాలుగా చదవండి
chunk_size = 10000
chunks = []
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # భాగాన్ని ప్రాసెస్ చేయండి
    chunks.append(chunk)
df = pd.concat(chunks)

# లేదా నిర్దిష్ట కాలమ్స్ మాత్రమే చదవండి
df = pd.read_csv('file.csv', usecols=['col1', 'col2'])

# మరింత సమర్థవంతమైన డేటా రకాలను ఉపయోగించండి
df = pd.read_csv('file.csv', dtype={'column_name': 'int32'})
```

## పనితీరు సమస్యలు

### నోట్‌బుక్ పనితీరు మందగించడం

**సమస్య:** నోట్‌బుక్స్ చాలా మందగిస్తాయి

**పరిష్కారం:**

1. **కర్నెల్‌ను రీస్టార్ట్ చేసి అవుట్‌పుట్ క్లియర్ చేయండి**
   - Kernel → Restart & Clear Output

2. **వినియోగంలో లేని నోట్‌బుక్స్ మూసివేయండి**

3. **కోడ్‌ను ఆప్టిమైజ్ చేయండి:**
```python
# లూపుల బదులు వెక్టరైజ్డ్ ఆపరేషన్లు ఉపయోగించండి
# చెడు:
result = []
for x in data:
    result.append(x * 2)

# మంచి:
result = data * 2  # NumPy/Pandas వెక్టరైజేషన్
```

4. **పెద్ద డేటాసెట్‌ల నుండి నమూనాలు తీసుకోండి:**
```python
# అభివృద్ధి సమయంలో నమూనాతో పని చేయండి
df_sample = df.sample(n=1000)  # లేదా df.head(1000)
```

### బ్రౌజర్ క్రాష్‌లు

**సమస్య:** బ్రౌజర్ క్రాష్ అవుతుంది లేదా స్పందించదు

**పరిష్కారం:**

1. వినియోగంలో లేని ట్యాబ్స్ మూసివేయండి
2. బ్రౌజర్ క్యాషే క్లియర్ చేయండి
3. బ్రౌజర్ మెమరీ పెంచండి (Chrome: `chrome://settings/system`)
4. JupyterLab ఉపయోగించండి:
```bash
pip install jupyterlab
jupyter lab
```

## అదనపు సహాయం పొందడం

### సహాయం కోరేముందు

1. ఈ సమస్య పరిష్కరణ గైడ్‌ను తనిఖీ చేయండి
2. [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) లో శోధించండి
3. [INSTALLATION.md](INSTALLATION.md) మరియు [USAGE.md](USAGE.md) ను సమీక్షించండి
4. లోప సందేశాన్ని ఆన్‌లైన్‌లో శోధించండి

### సహాయం ఎలా కోరాలి

సమస్యను సృష్టించేటప్పుడు లేదా సహాయం కోరేటప్పుడు, ఈ వివరాలను చేర్చండి:

1. **ఆపరేటింగ్ సిస్టమ్**: Windows, macOS, లేదా Linux (ఏ డిస్ట్రిబ్యూషన్)
2. **Python వెర్షన్**: `python --version` ను రన్ చేయండి
3. **లోప సందేశం**: పూర్తి లోప సందేశాన్ని కాపీ చేయండి
4. **పునరుత్పత్తి దశలు**: లోపం సంభవించే ముందు మీరు చేసిన దశలు
5. **మీ ప్రయత్నాలు**: మీరు ఇప్పటికే ప్రయత్నించిన పరిష్కారాలు

**ఉదాహరణ:**
```
**Operating System:** macOS 12.0
**Python Version:** 3.9.7
**Error Message:** ModuleNotFoundError: No module named 'pandas'
**Steps to Reproduce:**
1. Activated virtual environment
2. Started Jupyter notebook
3. Tried to import pandas

**What I've Tried:**
- Ran pip install pandas
- Restarted Jupyter
```

### కమ్యూనిటీ వనరులు

- **GitHub Issues**: [Create an issue](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Join our community](https://aka.ms/ds4beginners/discord)
- **Discussions**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Q&A Forums](https://docs.microsoft.com/answers/)

### సంబంధిత డాక్యుమెంటేషన్

- [INSTALLATION.md](INSTALLATION.md) - సెటప్ సూచనలు
- [USAGE.md](USAGE.md) - పాఠ్యాంశం ఎలా ఉపయోగించాలి
- [CONTRIBUTING.md](CONTRIBUTING.md) - ఎలా సహకరించాలి
- [README.md](README.md) - ప్రాజెక్ట్ అవలోకనం

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->