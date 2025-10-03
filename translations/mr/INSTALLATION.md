<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:18:10+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "mr"
}
-->
# स्थापना मार्गदर्शक

हा मार्गदर्शक तुम्हाला Data Science for Beginners अभ्यासक्रमासाठी तुमचे वातावरण सेट अप करण्यात मदत करेल.

## विषय सूची

- [पूर्वतयारी](../..)
- [जलद प्रारंभ पर्याय](../..)
- [स्थानिक स्थापना](../..)
- [तुमची स्थापना सत्यापित करा](../..)

## पूर्वतयारी

सुरुवात करण्यापूर्वी, तुम्हाला खालील गोष्टींची आवश्यकता आहे:

- कमांड लाइन/टर्मिनलची मूलभूत ओळख
- GitHub खाते (फ्री)
- प्रारंभिक सेटअपसाठी स्थिर इंटरनेट कनेक्शन

## जलद प्रारंभ पर्याय

### पर्याय 1: GitHub Codespaces (नवशिक्यांसाठी शिफारस केलेले)

सुरुवात करण्याचा सर्वात सोपा मार्ग म्हणजे GitHub Codespaces, जे तुमच्या ब्राउझरमध्ये संपूर्ण विकास वातावरण प्रदान करते.

1. [रेपॉझिटरी](https://github.com/microsoft/Data-Science-For-Beginners) वर जा
2. **Code** ड्रॉपडाउन मेनूवर क्लिक करा
3. **Codespaces** टॅब निवडा
4. **Create codespace on main** वर क्लिक करा
5. वातावरण प्रारंभ होईपर्यंत प्रतीक्षा करा (2-3 मिनिटे)

तुमचे वातावरण आता सर्व आवश्यक गोष्टींसह तयार आहे!

### पर्याय 2: स्थानिक विकास

तुमच्या स्वतःच्या संगणकावर काम करण्यासाठी, खाली दिलेल्या तपशीलवार सूचनांचे अनुसरण करा.

## स्थानिक स्थापना

### चरण 1: Git स्थापित करा

रेपॉझिटरी क्लोन करण्यासाठी आणि तुमचे बदल ट्रॅक करण्यासाठी Git आवश्यक आहे.

**Windows:**
- [git-scm.com](https://git-scm.com/download/win) वरून डाउनलोड करा
- डिफॉल्ट सेटिंग्ससह इंस्टॉलर चालवा

**macOS:**
- Homebrew वापरून इंस्टॉल करा: `brew install git`
- किंवा [git-scm.com](https://git-scm.com/download/mac) वरून डाउनलोड करा

**Linux:**
```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

### चरण 2: रेपॉझिटरी क्लोन करा

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### चरण 3: Python आणि Jupyter स्थापित करा

डेटा सायन्स धड्यांसाठी Python 3.7 किंवा त्याहून अधिक आवृत्ती आवश्यक आहे.

**Windows:**
1. [python.org](https://www.python.org/downloads/) वरून Python डाउनलोड करा
2. इंस्टॉलेशन दरम्यान, "Add Python to PATH" निवडा
3. इंस्टॉलेशन सत्यापित करा:
```bash
python --version
```

**macOS:**
```bash
# Using Homebrew
brew install python3

# Verify installation
python3 --version
```

**Linux:**
```bash
# Most Linux distributions come with Python pre-installed
python3 --version

# If not installed:
# Debian/Ubuntu
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

### चरण 4: Python वातावरण सेट अप करा

निर्भरता वेगळ्या ठेवण्यासाठी व्हर्च्युअल वातावरण वापरण्याची शिफारस केली जाते.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### चरण 5: Python पॅकेजेस स्थापित करा

आवश्यक डेटा सायन्स लायब्ररी इंस्टॉल करा:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### चरण 6: Node.js आणि npm स्थापित करा (क्विझ अॅपसाठी)

क्विझ अॅप्लिकेशनसाठी Node.js आणि npm आवश्यक आहे.

**Windows/macOS:**
- [nodejs.org](https://nodejs.org/) वरून डाउनलोड करा (LTS आवृत्ती शिफारस केली जाते)
- इंस्टॉलर चालवा

**Linux:**
```bash
# Debian/Ubuntu
# WARNING: Piping scripts from the internet directly into bash can be a security risk.
# It is recommended to review the script before running it:
#   curl -fsSL https://deb.nodesource.com/setup_lts.x -o setup_lts.x
#   less setup_lts.x
# Then run:
#   sudo -E bash setup_lts.x
#
# Alternatively, you can use the one-liner below at your own risk:
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# Fedora
sudo dnf install nodejs

# Verify installation
node --version
npm --version
```

### चरण 7: क्विझ अॅप निर्भरता स्थापित करा

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### चरण 8: Docsify स्थापित करा (ऐच्छिक)

डॉक्युमेंटेशनसाठी ऑफलाइन प्रवेशासाठी:

```bash
npm install -g docsify-cli
```

## तुमची स्थापना सत्यापित करा

### Python आणि Jupyter चाचणी करा

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

तुमच्या ब्राउझरमध्ये Jupyter इंटरफेस उघडला पाहिजे. तुम्ही आता कोणत्याही धड्याच्या `.ipynb` फाइलमध्ये नेव्हिगेट करू शकता.

### क्विझ अॅप्लिकेशन चाचणी करा

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

क्विझ अॅप `http://localhost:8080` (किंवा 8080 व्यस्त असल्यास दुसऱ्या पोर्टवर) उपलब्ध असावा.

### डॉक्युमेंटेशन सर्व्हर चाचणी करा

```bash
# From the root directory of the repository
docsify serve
```

डॉक्युमेंटेशन `http://localhost:3000` वर उपलब्ध असावे.

## VS Code Dev Containers वापरणे

जर तुमच्याकडे Docker इंस्टॉल असेल, तर तुम्ही VS Code Dev Containers वापरू शकता:

1. [Docker Desktop](https://www.docker.com/products/docker-desktop) इंस्टॉल करा
2. [Visual Studio Code](https://code.visualstudio.com/) इंस्टॉल करा
3. [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) इंस्टॉल करा
4. रेपॉझिटरी VS Code मध्ये उघडा
5. `F1` दाबा आणि "Remote-Containers: Reopen in Container" निवडा
6. कंटेनर तयार होईपर्यंत प्रतीक्षा करा (फक्त पहिल्यांदा)

## पुढील पायऱ्या

- अभ्यासक्रमाचा आढावा घेण्यासाठी [README.md](README.md) एक्सप्लोर करा
- सामान्य कार्यप्रवाह आणि उदाहरणांसाठी [USAGE.md](USAGE.md) वाचा
- समस्या आल्यास [TROUBLESHOOTING.md](TROUBLESHOOTING.md) तपासा
- योगदान देण्याची इच्छा असल्यास [CONTRIBUTING.md](CONTRIBUTING.md) वाचा

## मदत मिळवणे

जर तुम्हाला समस्या आल्या तर:

1. [TROUBLESHOOTING.md](TROUBLESHOOTING.md) मार्गदर्शक तपासा
2. विद्यमान [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) शोधा
3. आमच्या [Discord community](https://aka.ms/ds4beginners/discord) मध्ये सामील व्हा
4. तुमच्या समस्येबद्दल तपशीलवार माहिती देऊन नवीन इश्यू तयार करा

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून निर्माण झालेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.