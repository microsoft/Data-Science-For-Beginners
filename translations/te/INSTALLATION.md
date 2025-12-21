<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-12-19T13:10:17+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "te"
}
-->
# ఇన్‌స్టాలేషన్ గైడ్

ఈ గైడ్ మీకు Data Science for Beginners పాఠ్యాంశంతో పని చేయడానికి మీ వాతావరణాన్ని సెట్ చేయడంలో సహాయపడుతుంది.

## విషయ సూచిక

- [ముందస్తు అవసరాలు](../..)
- [త్వరిత ప్రారంభ ఎంపికలు](../..)
- [స్థానిక ఇన్‌స్టాలేషన్](../..)
- [మీ ఇన్‌స్టాలేషన్‌ను ధృవీకరించండి](../..)

## ముందస్తు అవసరాలు

మీరు ప్రారంభించడానికి ముందు, మీ వద్ద ఉండాలి:

- కమాండ్ లైన్/టెర్మినల్‌తో ప్రాథమిక పరిచయం
- GitHub ఖాతా (ఉచితం)
- ప్రారంభ సెటప్ కోసం స్థిరమైన ఇంటర్నెట్ కనెక్షన్

## త్వరిత ప్రారంభ ఎంపికలు

### ఎంపిక 1: GitHub Codespaces (ఆరంభకులకు సిఫార్సు)

GitHub Codespaces తో ప్రారంభించడం అత్యంత సులభం, ఇది మీ బ్రౌజర్‌లో పూర్తి అభివృద్ధి వాతావరణాన్ని అందిస్తుంది.

1. [repository](https://github.com/microsoft/Data-Science-For-Beginners) కి వెళ్లండి
2. **Code** డ్రాప్‌డౌన్ మెనూను క్లిక్ చేయండి
3. **Codespaces** ట్యాబ్‌ను ఎంచుకోండి
4. **Create codespace on main** క్లిక్ చేయండి
5. వాతావరణం ప్రారంభం కావడానికి వేచి ఉండండి (2-3 నిమిషాలు)

మీ వాతావరణం ఇప్పుడు అన్ని డిపెండెన్సీలతో ముందుగా ఇన్‌స్టాల్ చేయబడింది!

### ఎంపిక 2: స్థానిక అభివృద్ధి

మీ స్వంత కంప్యూటర్‌లో పని చేయడానికి, క్రింది వివరమైన సూచనలను అనుసరించండి.

## స్థానిక ఇన్‌స్టాలేషన్

### దశ 1: Git ఇన్‌స్టాల్ చేయండి

Git రిపాజిటరీని క్లోన్ చేయడానికి మరియు మీ మార్పులను ట్రాక్ చేయడానికి అవసరం.

**Windows:**
- [git-scm.com](https://git-scm.com/download/win) నుండి డౌన్లోడ్ చేసుకోండి
- డిఫాల్ట్ సెట్టింగ్స్‌తో ఇన్‌స్టాలర్‌ను రన్ చేయండి

**macOS:**
- Homebrew ద్వారా ఇన్‌స్టాల్ చేయండి: `brew install git`
- లేదా [git-scm.com](https://git-scm.com/download/mac) నుండి డౌన్లోడ్ చేసుకోండి

**Linux:**
```bash
# డెబియన్/ఉబుంటు
sudo apt-get update
sudo apt-get install git

# ఫెడోరా
sudo dnf install git

# ఆర్చ్
sudo pacman -S git
```

### దశ 2: రిపాజిటరీని క్లోన్ చేయండి

```bash
# రిపోజిటరీని క్లోన్ చేయండి
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# డైరెక్టరీకి నావిగేట్ చేయండి
cd Data-Science-For-Beginners
```

### దశ 3: Python మరియు Jupyter ఇన్‌స్టాల్ చేయండి

Python 3.7 లేదా అంతకంటే పై వెర్షన్ డేటా సైన్స్ పాఠాల కోసం అవసరం.

**Windows:**
1. [python.org](https://www.python.org/downloads/) నుండి Python డౌన్లోడ్ చేసుకోండి
2. ఇన్‌స్టాలేషన్ సమయంలో, "Add Python to PATH" ను గుర్తించండి
3. ఇన్‌స్టాలేషన్‌ను ధృవీకరించండి:
```bash
python --version
```

**macOS:**
```bash
# హోంబ్రూ ఉపయోగించడం
brew install python3

# ఇన్‌స్టాలేషన్‌ను ధృవీకరించండి
python3 --version
```

**Linux:**
```bash
# ఎక్కువ Linux పంపిణీలు Python ముందుగా ఇన్‌స్టాల్ చేయబడినవిగా వస్తాయి
python3 --version

# ఇన్‌స్టాల్ చేయబడకపోతే:
# Debian/Ubuntu
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

### దశ 4: Python వాతావరణాన్ని సెట్ చేయండి

డిపెండెన్సీలను వేరుగా ఉంచడానికి వర్చువల్ వాతావరణం ఉపయోగించడం సిఫార్సు చేయబడింది.

```bash
# ఒక వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించండి
python -m venv venv

# వర్చువల్ ఎన్విరాన్‌మెంట్‌ను యాక్టివేట్ చేయండి
# విండోస్‌లో:
venv\Scripts\activate

# మాక్‌ఓఎస్/లినక్స్‌లో:
source venv/bin/activate
```

### దశ 5: Python ప్యాకేజీలను ఇన్‌స్టాల్ చేయండి

అవసరమైన డేటా సైన్స్ లైబ్రరీలను ఇన్‌స్టాల్ చేయండి:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### దశ 6: Node.js మరియు npm ఇన్‌స్టాల్ చేయండి (Quiz App కోసం)

క్విజ్ అప్లికేషన్‌కు Node.js మరియు npm అవసరం.

**Windows/macOS:**
- [nodejs.org](https://nodejs.org/) నుండి డౌన్లోడ్ చేసుకోండి (LTS వెర్షన్ సిఫార్సు)
- ఇన్‌స్టాలర్‌ను రన్ చేయండి

**Linux:**
```bash
# డెబియన్/ఉబుంటు
# హెచ్చరిక: ఇంటర్నెట్ నుండి స్క్రిప్టులను నేరుగా బాష్‌లో పైప్ చేయడం భద్రతా ప్రమాదం కావచ్చు.
# స్క్రిప్ట్‌ను నడపడానికి ముందు సమీక్షించడం సిఫార్సు చేయబడింది:
#   curl -fsSL https://deb.nodesource.com/setup_lts.x -o setup_lts.x
#   less setup_lts.x
# ఆపై నడపండి:
#   sudo -E bash setup_lts.x
#
# ప్రత్యామ్నాయంగా, మీ స్వంత ప్రమాదంలో క్రింది ఒక లైనర్‌ను ఉపయోగించవచ్చు:
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# ఫెడోరా
sudo dnf install nodejs

# ఇన్‌స్టాలేషన్‌ను ధృవీకరించండి
node --version
npm --version
```

### దశ 7: Quiz App డిపెండెన్సీలను ఇన్‌స్టాల్ చేయండి

```bash
# క్విజ్ యాప్ డైరెక్టరీకి నావిగేట్ చేయండి
cd quiz-app

# డిపెండెన్సీలను ఇన్‌స్టాల్ చేయండి
npm install

# రూట్ డైరెక్టరీకి తిరిగి వెళ్లండి
cd ..
```

### దశ 8: Docsify ఇన్‌స్టాల్ చేయండి (ఐచ్ఛికం)

డాక్యుమెంటేషన్‌ను ఆఫ్‌లైన్ యాక్సెస్ కోసం:

```bash
npm install -g docsify-cli
```

## మీ ఇన్‌స్టాలేషన్‌ను ధృవీకరించండి

### Python మరియు Jupyter ను పరీక్షించండి

```bash
# మీ వర్చువల్ ఎన్విరాన్‌మెంట్ ఇప్పటికే యాక్టివేట్ కాకపోతే యాక్టివేట్ చేయండి
# విండోస్‌లో:
venv\Scripts\activate
# మాక్‌ఓఎస్/లినక్స్‌లో:
source venv/bin/activate

# జూపిటర్ నోట్‌బుక్ ప్రారంభించండి
jupyter notebook
```

మీ బ్రౌజర్ Jupyter ఇంటర్‌ఫేస్‌తో తెరవాలి. మీరు ఇప్పుడు ఏ పాఠం `.ipynb` ఫైల్‌కు వెళ్లవచ్చు.

### Quiz అప్లికేషన్‌ను పరీక్షించండి

```bash
# క్విజ్ యాప్‌కు నావిగేట్ చేయండి
cd quiz-app

# అభివృద్ధి సర్వర్‌ను ప్రారంభించండి
npm run serve
```

క్విజ్ యాప్ `http://localhost:8080` (లేదా 8080 బిజీ అయితే మరొక పోర్ట్) వద్ద అందుబాటులో ఉండాలి.

### డాక్యుమెంటేషన్ సర్వర్‌ను పరీక్షించండి

```bash
# రిపాజిటరీ యొక్క రూట్ డైరెక్టరీ నుండి
docsify serve
```

డాక్యుమెంటేషన్ `http://localhost:3000` వద్ద అందుబాటులో ఉండాలి.

## VS Code Dev Containers ఉపయోగించడం

మీ వద్ద Docker ఇన్‌స్టాల్ ఉంటే, మీరు VS Code Dev Containers ఉపయోగించవచ్చు:

1. [Docker Desktop](https://www.docker.com/products/docker-desktop) ఇన్‌స్టాల్ చేయండి
2. [Visual Studio Code](https://code.visualstudio.com/) ఇన్‌స్టాల్ చేయండి
3. [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) ఇన్‌స్టాల్ చేయండి
4. రిపాజిటరీని VS Code లో ఓపెన్ చేయండి
5. `F1` నొక్కి "Remote-Containers: Reopen in Container" ఎంచుకోండి
6. కంటైనర్ నిర్మాణం కోసం వేచి ఉండండి (మొదటి సారి మాత్రమే)

## తదుపరి దశలు

- పాఠ్యాంశం అవలోకనం కోసం [README.md](README.md) ను అన్వేషించండి
- సాధారణ వర్క్‌ఫ్లోలు మరియు ఉదాహరణల కోసం [USAGE.md](USAGE.md) చదవండి
- సమస్యలు ఎదురైతే [TROUBLESHOOTING.md](TROUBLESHOOTING.md) ను తనిఖీ చేయండి
- మీరు సహకరించాలనుకుంటే [CONTRIBUTING.md](CONTRIBUTING.md) ను సమీక్షించండి

## సహాయం పొందడం

మీరు సమస్యలను ఎదుర్కొంటే:

1. [TROUBLESHOOTING.md](TROUBLESHOOTING.md) గైడ్‌ను తనిఖీ చేయండి
2. ఉన్న [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) ను శోధించండి
3. మా [Discord community](https://aka.ms/ds4beginners/discord) లో చేరండి
4. మీ సమస్య గురించి వివరాలతో కొత్త ఇష్యూ సృష్టించండి

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->