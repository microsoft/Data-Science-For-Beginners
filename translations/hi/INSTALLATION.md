<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:17:38+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "hi"
}
-->
# इंस्टॉलेशन गाइड

यह गाइड आपको Data Science for Beginners पाठ्यक्रम के साथ काम करने के लिए अपना वातावरण सेट करने में मदद करेगा।

## सामग्री सूची

- [पूर्व आवश्यकताएँ](../..)
- [त्वरित प्रारंभ विकल्प](../..)
- [स्थानीय इंस्टॉलेशन](../..)
- [अपनी इंस्टॉलेशन सत्यापित करें](../..)

## पूर्व आवश्यकताएँ

शुरू करने से पहले, आपके पास होना चाहिए:

- कमांड लाइन/टर्मिनल की बुनियादी जानकारी
- एक GitHub खाता (मुफ्त)
- प्रारंभिक सेटअप के लिए स्थिर इंटरनेट कनेक्शन

## त्वरित प्रारंभ विकल्प

### विकल्प 1: GitHub Codespaces (शुरुआती लोगों के लिए अनुशंसित)

शुरू करने का सबसे आसान तरीका GitHub Codespaces है, जो आपके ब्राउज़र में एक पूर्ण विकास वातावरण प्रदान करता है।

1. [रिपॉजिटरी](https://github.com/microsoft/Data-Science-For-Beginners) पर जाएं
2. **Code** ड्रॉपडाउन मेनू पर क्लिक करें
3. **Codespaces** टैब चुनें
4. **Create codespace on main** पर क्लिक करें
5. वातावरण को प्रारंभ करने के लिए प्रतीक्षा करें (2-3 मिनट)

आपका वातावरण अब सभी आवश्यकताओं के साथ तैयार है!

### विकल्प 2: स्थानीय विकास

अपने कंप्यूटर पर काम करने के लिए नीचे दिए गए विस्तृत निर्देशों का पालन करें।

## स्थानीय इंस्टॉलेशन

### चरण 1: Git इंस्टॉल करें

रिपॉजिटरी को क्लोन करने और अपने परिवर्तनों को ट्रैक करने के लिए Git आवश्यक है।

**Windows:**
- [git-scm.com](https://git-scm.com/download/win) से डाउनलोड करें
- डिफ़ॉल्ट सेटिंग्स के साथ इंस्टॉलर चलाएं

**macOS:**
- Homebrew के माध्यम से इंस्टॉल करें: `brew install git`
- या [git-scm.com](https://git-scm.com/download/mac) से डाउनलोड करें

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

### चरण 2: रिपॉजिटरी क्लोन करें

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### चरण 3: Python और Jupyter इंस्टॉल करें

डेटा साइंस पाठों के लिए Python 3.7 या उच्च संस्करण आवश्यक है।

**Windows:**
1. [python.org](https://www.python.org/downloads/) से Python डाउनलोड करें
2. इंस्टॉलेशन के दौरान "Add Python to PATH" विकल्प चुनें
3. इंस्टॉलेशन सत्यापित करें:
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

### चरण 4: Python वातावरण सेट करें

निर्भरता को अलग रखने के लिए वर्चुअल वातावरण का उपयोग करने की सिफारिश की जाती है।

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### चरण 5: Python पैकेज इंस्टॉल करें

आवश्यक डेटा साइंस लाइब्रेरी इंस्टॉल करें:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### चरण 6: Node.js और npm इंस्टॉल करें (क्विज़ ऐप के लिए)

क्विज़ एप्लिकेशन के लिए Node.js और npm आवश्यक हैं।

**Windows/macOS:**
- [nodejs.org](https://nodejs.org/) से डाउनलोड करें (LTS संस्करण अनुशंसित)
- इंस्टॉलर चलाएं

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

### चरण 7: क्विज़ ऐप निर्भरता इंस्टॉल करें

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### चरण 8: Docsify इंस्टॉल करें (वैकल्पिक)

दस्तावेज़ों तक ऑफलाइन पहुंच के लिए:

```bash
npm install -g docsify-cli
```

## अपनी इंस्टॉलेशन सत्यापित करें

### Python और Jupyter का परीक्षण करें

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

आपका ब्राउज़र Jupyter इंटरफ़ेस के साथ खुलना चाहिए। अब आप किसी भी पाठ के `.ipynb` फ़ाइल पर जा सकते हैं।

### क्विज़ एप्लिकेशन का परीक्षण करें

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

क्विज़ ऐप `http://localhost:8080` (या यदि 8080 व्यस्त है तो किसी अन्य पोर्ट) पर उपलब्ध होना चाहिए।

### दस्तावेज़ सर्वर का परीक्षण करें

```bash
# From the root directory of the repository
docsify serve
```

दस्तावेज़ `http://localhost:3000` पर उपलब्ध होना चाहिए।

## VS Code Dev Containers का उपयोग करना

यदि आपने Docker इंस्टॉल किया है, तो आप VS Code Dev Containers का उपयोग कर सकते हैं:

1. [Docker Desktop](https://www.docker.com/products/docker-desktop) इंस्टॉल करें
2. [Visual Studio Code](https://code.visualstudio.com/) इंस्टॉल करें
3. [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) इंस्टॉल करें
4. रिपॉजिटरी को VS Code में खोलें
5. `F1` दबाएं और "Remote-Containers: Reopen in Container" चुनें
6. कंटेनर को बनाने के लिए प्रतीक्षा करें (केवल पहली बार)

## अगले कदम

- पाठ्यक्रम का अवलोकन करने के लिए [README.md](README.md) देखें
- सामान्य वर्कफ़्लो और उदाहरणों के लिए [USAGE.md](USAGE.md) पढ़ें
- यदि आपको समस्याओं का सामना करना पड़ता है तो [TROUBLESHOOTING.md](TROUBLESHOOTING.md) देखें
- यदि आप योगदान करना चाहते हैं तो [CONTRIBUTING.md](CONTRIBUTING.md) की समीक्षा करें

## सहायता प्राप्त करना

यदि आपको समस्याओं का सामना करना पड़ता है:

1. [TROUBLESHOOTING.md](TROUBLESHOOTING.md) गाइड देखें
2. मौजूदा [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) खोजें
3. हमारे [Discord समुदाय](https://aka.ms/ds4beginners/discord) में शामिल हों
4. अपनी समस्या के बारे में विस्तृत जानकारी के साथ एक नया मुद्दा बनाएं

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।