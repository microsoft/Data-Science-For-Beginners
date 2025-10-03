<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:11:12+00:00",
  "source_file": "AGENTS.md",
  "language_code": "hi"
}
-->
# AGENTS.md

## परियोजना का अवलोकन

बिगिनर्स के लिए डेटा साइंस एक व्यापक 10-सप्ताह, 20-पाठ का पाठ्यक्रम है जिसे Microsoft Azure Cloud Advocates द्वारा बनाया गया है। यह रिपॉजिटरी एक शिक्षण संसाधन है जो प्रोजेक्ट-आधारित पाठों के माध्यम से डेटा साइंस की बुनियादी अवधारणाओं को सिखाता है, जिसमें Jupyter नोटबुक, इंटरएक्टिव क्विज़ और प्रैक्टिकल असाइनमेंट शामिल हैं।

**मुख्य तकनीकें:**
- **Jupyter नोटबुक**: Python 3 का उपयोग करके प्राथमिक शिक्षण माध्यम
- **Python लाइब्रेरीज़**: डेटा विश्लेषण और विज़ुअलाइज़ेशन के लिए pandas, numpy, matplotlib
- **Vue.js 2**: क्विज़ एप्लिकेशन (quiz-app फ़ोल्डर)
- **Docsify**: ऑफलाइन एक्सेस के लिए डॉक्यूमेंटेशन साइट जनरेटर
- **Node.js/npm**: जावास्क्रिप्ट घटकों के लिए पैकेज प्रबंधन
- **Markdown**: सभी पाठ सामग्री और डॉक्यूमेंटेशन

**आर्किटेक्चर:**
- बहु-भाषा शैक्षिक रिपॉजिटरी जिसमें व्यापक अनुवाद शामिल हैं
- पाठ मॉड्यूल में संरचित (1-Introduction से 6-Data-Science-In-Wild तक)
- प्रत्येक पाठ में README, नोटबुक, असाइनमेंट और क्विज़ शामिल हैं
- प्री/पोस्ट-पाठ आकलन के लिए स्वतंत्र Vue.js क्विज़ एप्लिकेशन
- GitHub Codespaces और VS Code dev कंटेनर समर्थन

## सेटअप कमांड्स

### रिपॉजिटरी सेटअप
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Python एनवायरनमेंट सेटअप
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### क्विज़ एप्लिकेशन सेटअप
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

### Docsify डॉक्यूमेंटेशन सर्वर
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### विज़ुअलाइज़ेशन प्रोजेक्ट्स सेटअप
जैसे meaningful-visualizations (पाठ 13) के लिए:
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


## विकास कार्यप्रवाह

### Jupyter नोटबुक के साथ काम करना
1. रिपॉजिटरी रूट में Jupyter शुरू करें: `jupyter notebook`
2. इच्छित पाठ फ़ोल्डर पर जाएं
3. `.ipynb` फ़ाइलें खोलें और अभ्यास करें
4. नोटबुक्स में स्पष्टीकरण और कोड सेल्स होते हैं
5. अधिकांश नोटबुक्स pandas, numpy, और matplotlib का उपयोग करते हैं - सुनिश्चित करें कि ये इंस्टॉल हैं

### पाठ संरचना
प्रत्येक पाठ में आमतौर पर शामिल होता है:
- `README.md` - मुख्य पाठ सामग्री जिसमें सिद्धांत और उदाहरण होते हैं
- `notebook.ipynb` - प्रैक्टिकल Jupyter नोटबुक अभ्यास
- `assignment.ipynb` या `assignment.md` - अभ्यास असाइनमेंट
- `solution/` फ़ोल्डर - समाधान नोटबुक्स और कोड
- `images/` फ़ोल्डर - सहायक दृश्य सामग्री

### क्विज़ एप्लिकेशन विकास
- Vue.js 2 एप्लिकेशन जिसमें विकास के दौरान हॉट-रिलोड होता है
- क्विज़ `quiz-app/src/assets/translations/` में संग्रहीत हैं
- प्रत्येक भाषा का अपना अनुवाद फ़ोल्डर होता है (en, fr, es, आदि)
- क्विज़ की संख्या 0 से शुरू होती है और 39 तक जाती है (कुल 40 क्विज़)

### अनुवाद जोड़ना
- अनुवाद `translations/` फ़ोल्डर में रिपॉजिटरी रूट पर जाते हैं
- प्रत्येक भाषा का पाठ संरचना अंग्रेजी से मेल खाती है
- GitHub Actions के माध्यम से स्वचालित अनुवाद (co-op-translator.yml)

## परीक्षण निर्देश

### क्विज़ एप्लिकेशन परीक्षण
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### नोटबुक परीक्षण
- नोटबुक्स के लिए कोई स्वचालित परीक्षण फ्रेमवर्क मौजूद नहीं है
- मैन्युअल सत्यापन: सभी सेल्स को क्रम में चलाएं ताकि कोई त्रुटि न हो
- सुनिश्चित करें कि डेटा फ़ाइलें सुलभ हैं और आउटपुट सही ढंग से उत्पन्न होते हैं
- जांचें कि विज़ुअलाइज़ेशन सही ढंग से रेंडर होते हैं

### डॉक्यूमेंटेशन परीक्षण
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### कोड गुणवत्ता जांच
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## कोड शैली दिशानिर्देश

### Python (Jupyter नोटबुक्स)
- Python कोड के लिए PEP 8 शैली दिशानिर्देशों का पालन करें
- स्पष्ट वेरिएबल नामों का उपयोग करें जो विश्लेषण किए जा रहे डेटा को समझाएं
- कोड सेल्स से पहले स्पष्टीकरण के साथ Markdown सेल्स शामिल करें
- कोड सेल्स को एकल अवधारणाओं या संचालन पर केंद्रित रखें
- डेटा हेरफेर के लिए pandas और विज़ुअलाइज़ेशन के लिए matplotlib का उपयोग करें
- सामान्य आयात पैटर्न:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Vue.js 2 शैली गाइड और सर्वोत्तम प्रथाओं का पालन करें
- ESLint कॉन्फ़िगरेशन `quiz-app/package.json` में
- Vue सिंगल-फाइल घटकों (.vue फ़ाइलें) का उपयोग करें
- घटक-आधारित आर्किटेक्चर बनाए रखें
- परिवर्तन करने से पहले `npm run lint` चलाएं

### Markdown डॉक्यूमेंटेशन
- स्पष्ट शीर्षक पदानुक्रम (# ## ### आदि) का उपयोग करें
- भाषा निर्दिष्ट करने वाले कोड ब्लॉक शामिल करें
- छवियों के लिए alt टेक्स्ट जोड़ें
- संबंधित पाठ और संसाधनों के लिंक जोड़ें
- पठनीयता के लिए लाइन लंबाई उचित रखें

### फ़ाइल संगठन
- पाठ सामग्री क्रमांकित फ़ोल्डरों में (01-defining-data-science, आदि)
- समाधान समर्पित `solution/` उपफ़ोल्डरों में
- अनुवाद अंग्रेजी संरचना को `translations/` फ़ोल्डर में दर्शाते हैं
- डेटा फ़ाइलें `data/` या पाठ-विशिष्ट फ़ोल्डरों में रखें

## निर्माण और परिनियोजन

### क्विज़ एप्लिकेशन परिनियोजन
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Azure Static Web Apps परिनियोजन
क्विज़-ऐप को Azure Static Web Apps पर परिनियोजित किया जा सकता है:
1. Azure Static Web App संसाधन बनाएं
2. GitHub रिपॉजिटरी से कनेक्ट करें
3. निर्माण सेटिंग्स कॉन्फ़िगर करें:
   - ऐप स्थान: `quiz-app`
   - आउटपुट स्थान: `dist`
4. GitHub Actions वर्कफ़्लो पुश पर स्वचालित रूप से परिनियोजित करेगा

### डॉक्यूमेंटेशन साइट
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- रिपॉजिटरी में dev कंटेनर कॉन्फ़िगरेशन शामिल है
- Codespaces स्वचालित रूप से Python और Node.js एनवायरनमेंट सेट करता है
- GitHub UI के माध्यम से रिपॉजिटरी को Codespace में खोलें
- सभी निर्भरताएं स्वचालित रूप से इंस्टॉल होती हैं

## पुल अनुरोध दिशानिर्देश

### सबमिट करने से पहले
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### PR शीर्षक प्रारूप
- स्पष्ट, वर्णनात्मक शीर्षक का उपयोग करें
- प्रारूप: `[घटक] संक्षिप्त विवरण`
- उदाहरण:
  - `[Lesson 7] Python नोटबुक आयात त्रुटि ठीक करें`
  - `[Quiz App] जर्मन अनुवाद जोड़ें`
  - `[Docs] README को नए आवश्यकताओं के साथ अपडेट करें`

### आवश्यक जांच
- सुनिश्चित करें कि सभी कोड त्रुटियों के बिना चलते हैं
- सत्यापित करें कि नोटबुक्स पूरी तरह से निष्पादित होते हैं
- पुष्टि करें कि Vue.js ऐप्स सफलतापूर्वक बनते हैं
- जांचें कि डॉक्यूमेंटेशन लिंक काम करते हैं
- यदि संशोधित किया गया हो तो क्विज़ एप्लिकेशन का परीक्षण करें
- सुनिश्चित करें कि अनुवाद संरचना सुसंगत बनाए रखते हैं

### योगदान दिशानिर्देश
- मौजूदा कोड शैली और पैटर्न का पालन करें
- जटिल तर्क के लिए व्याख्यात्मक टिप्पणियां जोड़ें
- संबंधित डॉक्यूमेंटेशन अपडेट करें
- यदि लागू हो तो विभिन्न पाठ मॉड्यूल में परिवर्तनों का परीक्षण करें
- CONTRIBUTING.md फ़ाइल की समीक्षा करें

## अतिरिक्त नोट्स

### सामान्य उपयोग की जाने वाली लाइब्रेरीज़
- **pandas**: डेटा हेरफेर और विश्लेषण
- **numpy**: संख्यात्मक गणना
- **matplotlib**: डेटा विज़ुअलाइज़ेशन और प्लॉटिंग
- **seaborn**: सांख्यिकीय डेटा विज़ुअलाइज़ेशन (कुछ पाठ)
- **scikit-learn**: मशीन लर्निंग (उन्नत पाठ)

### डेटा फ़ाइलों के साथ काम करना
- डेटा फ़ाइलें `data/` फ़ोल्डर या पाठ-विशिष्ट निर्देशिकाओं में स्थित हैं
- अधिकांश नोटबुक्स अपेक्षा करते हैं कि डेटा फ़ाइलें सापेक्ष पथों में हों
- CSV फ़ाइलें प्राथमिक डेटा प्रारूप हैं
- कुछ पाठ गैर-संबंधपरक डेटा उदाहरणों के लिए JSON का उपयोग करते हैं

### बहुभाषी समर्थन
- स्वचालित GitHub Actions के माध्यम से 40+ भाषा अनुवाद
- अनुवाद वर्कफ़्लो `.github/workflows/co-op-translator.yml` में
- अनुवाद `translations/` फ़ोल्डर में भाषा कोड के साथ
- क्विज़ अनुवाद `quiz-app/src/assets/translations/` में

### विकास पर्यावरण विकल्प
1. **स्थानीय विकास**: Python, Jupyter, Node.js को स्थानीय रूप से इंस्टॉल करें
2. **GitHub Codespaces**: क्लाउड-आधारित त्वरित विकास पर्यावरण
3. **VS Code Dev Containers**: स्थानीय कंटेनर-आधारित विकास
4. **Binder**: क्लाउड में नोटबुक्स लॉन्च करें (यदि कॉन्फ़िगर किया गया हो)

### पाठ सामग्री दिशानिर्देश
- प्रत्येक पाठ स्वतंत्र है लेकिन पिछले अवधारणाओं पर आधारित है
- प्री-पाठ क्विज़ पूर्व ज्ञान का परीक्षण करते हैं
- पोस्ट-पाठ क्विज़ सीखने को सुदृढ़ करते हैं
- असाइनमेंट व्यावहारिक अभ्यास प्रदान करते हैं
- स्केच नोट्स दृश्य सारांश प्रदान करते हैं

### सामान्य समस्याओं का निवारण

**Jupyter कर्नेल समस्याएं:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**npm इंस्टॉल विफलताएं:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**नोटबुक्स में आयात त्रुटियां:**
- सुनिश्चित करें कि सभी आवश्यक लाइब्रेरीज़ इंस्टॉल हैं
- Python संस्करण संगतता की जांच करें (Python 3.7+ अनुशंसित)
- सुनिश्चित करें कि वर्चुअल एनवायरनमेंट सक्रिय है

**Docsify लोड नहीं हो रहा:**
- सुनिश्चित करें कि आप रिपॉजिटरी रूट से सर्व कर रहे हैं
- जांचें कि `index.html` मौजूद है
- उचित नेटवर्क एक्सेस सुनिश्चित करें (पोर्ट 3000)

### प्रदर्शन विचार
- बड़े डेटा सेट्स को नोटबुक्स में लोड करने में समय लग सकता है
- जटिल प्लॉट्स के लिए विज़ुअलाइज़ेशन रेंडरिंग धीमी हो सकती है
- Vue.js dev सर्वर त्वरित पुनरावृत्ति के लिए हॉट-रिलोड सक्षम करता है
- प्रोडक्शन बिल्ड्स अनुकूलित और मिनिफाइड होते हैं

### सुरक्षा नोट्स
- कोई संवेदनशील डेटा या क्रेडेंशियल्स कमिट नहीं किए जाने चाहिए
- क्लाउड पाठों में किसी भी API कुंजी के लिए एनवायरनमेंट वेरिएबल्स का उपयोग करें
- Azure-संबंधित पाठों में Azure खाता क्रेडेंशियल्स की आवश्यकता हो सकती है
- सुरक्षा पैच के लिए निर्भरताओं को अपडेट रखें

## अनुवाद में योगदान
- स्वचालित अनुवाद GitHub Actions के माध्यम से प्रबंधित
- अनुवाद सटीकता के लिए मैन्युअल सुधार स्वागत योग्य हैं
- मौजूदा अनुवाद फ़ोल्डर संरचना का पालन करें
- क्विज़ लिंक को भाषा पैरामीटर के साथ अपडेट करें: `?loc=fr`
- अनुवादित पाठों को सही ढंग से रेंडर करने के लिए परीक्षण करें

## संबंधित संसाधन
- मुख्य पाठ्यक्रम: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- छात्र हब: https://docs.microsoft.com/learn/student-hub
- चर्चा मंच: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- अन्य Microsoft पाठ्यक्रम: ML for Beginners, AI for Beginners, Web Dev for Beginners

## परियोजना रखरखाव
- सामग्री को अद्यतन रखने के लिए नियमित अपडेट
- समुदाय योगदान स्वागत योग्य
- GitHub पर मुद्दों को ट्रैक किया गया
- पाठ्यक्रम रखरखावकर्ताओं द्वारा PR की समीक्षा
- मासिक सामग्री समीक्षा और अपडेट

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।