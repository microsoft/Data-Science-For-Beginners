<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:18:30+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "ne"
}
-->
# स्थापना मार्गदर्शन

यो मार्गदर्शनले तपाईंलाई Data Science for Beginners पाठ्यक्रमसँग काम गर्नको लागि आफ्नो वातावरण सेटअप गर्न मद्दत गर्नेछ।

## सामग्री तालिका

- [पूर्वापेक्षाहरू](../..)
- [छिटो सुरु गर्ने विकल्पहरू](../..)
- [स्थानीय स्थापना](../..)
- [तपाईंको स्थापना प्रमाणित गर्नुहोस्](../..)

## पूर्वापेक्षाहरू

सुरु गर्नु अघि, तपाईंले निम्न कुराहरू जान्नुपर्छ:

- कमाण्ड लाइन/टर्मिनलसँग आधारभूत परिचय
- GitHub खाता (निःशुल्क)
- प्रारम्भिक सेटअपको लागि स्थिर इन्टरनेट जडान

## छिटो सुरु गर्ने विकल्पहरू

### विकल्प १: GitHub Codespaces (सुरुवातकर्ताहरूको लागि सिफारिस गरिएको)

सबैभन्दा सजिलो तरिका GitHub Codespaces प्रयोग गर्नु हो, जसले तपाईंको ब्राउजरमा पूर्ण विकास वातावरण प्रदान गर्दछ।

1. [रिपोजिटरी](https://github.com/microsoft/Data-Science-For-Beginners) मा जानुहोस्
2. **Code** ड्रपडाउन मेनुमा क्लिक गर्नुहोस्
3. **Codespaces** ट्याब चयन गर्नुहोस्
4. **Create codespace on main** मा क्लिक गर्नुहोस्
5. वातावरणलाई इनिसियलाइज गर्न २-३ मिनेट पर्खनुहोस्

अब तपाईंको वातावरण सबै निर्भरता पूर्व-स्थापितसँग तयार छ!

### विकल्प २: स्थानीय विकास

आफ्नै कम्प्युटरमा काम गर्नको लागि, तलका विस्तृत निर्देशनहरू पालना गर्नुहोस्।

## स्थानीय स्थापना

### चरण १: Git स्थापना गर्नुहोस्

रिपोजिटरी क्लोन गर्न र तपाईंको परिवर्तनहरू ट्र्याक गर्न Git आवश्यक छ।

**Windows:**
- [git-scm.com](https://git-scm.com/download/win) बाट डाउनलोड गर्नुहोस्
- डिफल्ट सेटिङ्सको साथ इन्स्टलर चलाउनुहोस्

**macOS:**
- Homebrew मार्फत स्थापना गर्नुहोस्: `brew install git`
- वा [git-scm.com](https://git-scm.com/download/mac) बाट डाउनलोड गर्नुहोस्

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

### चरण २: रिपोजिटरी क्लोन गर्नुहोस्

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### चरण ३: Python र Jupyter स्थापना गर्नुहोस्

Python 3.7 वा उच्च संस्करण डेटा विज्ञान पाठहरूको लागि आवश्यक छ।

**Windows:**
1. [python.org](https://www.python.org/downloads/) बाट Python डाउनलोड गर्नुहोस्
2. स्थापना गर्दा "Add Python to PATH" चेक गर्नुहोस्
3. स्थापना प्रमाणित गर्नुहोस्:
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

### चरण ४: Python वातावरण सेटअप गर्नुहोस्

निर्भरता अलग राख्नको लागि भर्चुअल वातावरण प्रयोग गर्न सिफारिस गरिन्छ।

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### चरण ५: Python प्याकेजहरू स्थापना गर्नुहोस्

आवश्यक डेटा विज्ञान पुस्तकालयहरू स्थापना गर्नुहोस्:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### चरण ६: Node.js र npm स्थापना गर्नुहोस् (Quiz App को लागि)

Quiz एप्लिकेसनको लागि Node.js र npm आवश्यक छ।

**Windows/macOS:**
- [nodejs.org](https://nodejs.org/) बाट डाउनलोड गर्नुहोस् (LTS संस्करण सिफारिस गरिएको)
- इन्स्टलर चलाउनुहोस्

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

### चरण ७: Quiz App निर्भरता स्थापना गर्नुहोस्

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### चरण ८: Docsify स्थापना गर्नुहोस् (वैकल्पिक)

डकुमेन्टेसनको अफलाइन पहुँचको लागि:

```bash
npm install -g docsify-cli
```

## तपाईंको स्थापना प्रमाणित गर्नुहोस्

### Python र Jupyter परीक्षण गर्नुहोस्

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

तपाईंको ब्राउजर Jupyter इन्टरफेससँग खुल्नुपर्छ। अब तपाईं कुनै पनि पाठको `.ipynb` फाइलमा जान सक्नुहुन्छ।

### Quiz एप्लिकेसन परीक्षण गर्नुहोस्

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Quiz एप्लिकेसन `http://localhost:8080` (वा यदि 8080 व्यस्त छ भने अर्को पोर्ट) मा उपलब्ध हुनुपर्छ।

### डकुमेन्टेसन सर्भर परीक्षण गर्नुहोस्

```bash
# From the root directory of the repository
docsify serve
```

डकुमेन्टेसन `http://localhost:3000` मा उपलब्ध हुनुपर्छ।

## VS Code Dev Containers प्रयोग गर्दै

यदि तपाईंले Docker स्थापना गर्नुभएको छ भने, तपाईं VS Code Dev Containers प्रयोग गर्न सक्नुहुन्छ:

1. [Docker Desktop](https://www.docker.com/products/docker-desktop) स्थापना गर्नुहोस्
2. [Visual Studio Code](https://code.visualstudio.com/) स्थापना गर्नुहोस्
3. [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) स्थापना गर्नुहोस्
4. रिपोजिटरीलाई VS Code मा खोल्नुहोस्
5. `F1` थिच्नुहोस् र "Remote-Containers: Reopen in Container" चयन गर्नुहोस्
6. कन्टेनर निर्माणको लागि पर्खनुहोस् (पहिलो पटक मात्र)

## अर्को चरणहरू

- पाठ्यक्रमको अवलोकनको लागि [README.md](README.md) अन्वेषण गर्नुहोस्
- सामान्य कार्यप्रवाह र उदाहरणहरूको लागि [USAGE.md](USAGE.md) पढ्नुहोस्
- यदि समस्या आउँछ भने [TROUBLESHOOTING.md](TROUBLESHOOTING.md) जाँच गर्नुहोस्
- योगदान गर्न चाहनुहुन्छ भने [CONTRIBUTING.md](CONTRIBUTING.md) समीक्षा गर्नुहोस्

## सहयोग प्राप्त गर्दै

यदि तपाईंले समस्या सामना गर्नुभयो भने:

1. [TROUBLESHOOTING.md](TROUBLESHOOTING.md) मार्गदर्शन जाँच गर्नुहोस्
2. विद्यमान [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) खोज्नुहोस्
3. हाम्रो [Discord समुदाय](https://aka.ms/ds4beginners/discord) मा सामेल हुनुहोस्
4. आफ्नो समस्याको विस्तृत जानकारीसहित नयाँ मुद्दा सिर्जना गर्नुहोस्

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी यथार्थताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।