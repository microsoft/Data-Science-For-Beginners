<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:13:42+00:00",
  "source_file": "AGENTS.md",
  "language_code": "mr"
}
-->
# AGENTS.md

## प्रकल्पाचा आढावा

डेटा सायन्स फॉर बिगिनर्स हा मायक्रोसॉफ्ट Azure क्लाउड अॅडव्होकेट्सद्वारे तयार केलेला 10 आठवड्यांचा, 20 धड्यांचा व्यापक अभ्यासक्रम आहे. हे रिपॉझिटरी प्रकल्प-आधारित धड्यांद्वारे मूलभूत डेटा सायन्स संकल्पना शिकवणारे शिक्षण संसाधन आहे, ज्यामध्ये Jupyter नोटबुक्स, परस्पर क्विझ आणि प्रॅक्टिकल असाइनमेंट्स समाविष्ट आहेत.

**मुख्य तंत्रज्ञान:**
- **Jupyter नोटबुक्स**: Python 3 वापरून प्राथमिक शिक्षण माध्यम
- **Python लायब्ररी**: pandas, numpy, matplotlib डेटा विश्लेषण आणि व्हिज्युअलायझेशनसाठी
- **Vue.js 2**: क्विझ अॅप्लिकेशन (quiz-app फोल्डर)
- **Docsify**: ऑफलाइन प्रवेशासाठी दस्तऐवज साइट जनरेटर
- **Node.js/npm**: JavaScript घटकांसाठी पॅकेज व्यवस्थापन
- **Markdown**: सर्व धड्यांची सामग्री आणि दस्तऐवज

**आर्किटेक्चर:**
- बहुभाषिक शैक्षणिक रिपॉझिटरी विस्तृत अनुवादांसह
- धड्यांच्या मॉड्यूल्समध्ये संरचित (1-Introduction ते 6-Data-Science-In-Wild)
- प्रत्येक धड्यात README, नोटबुक्स, असाइनमेंट्स आणि क्विझ समाविष्ट आहेत
- स्वतंत्र Vue.js क्विझ अॅप्लिकेशन प्री/पोस्ट-धडा मूल्यांकनासाठी
- GitHub Codespaces आणि VS Code dev कंटेनर समर्थन

## सेटअप कमांड्स

### रिपॉझिटरी सेटअप
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Python वातावरण सेटअप
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### क्विझ अॅप्लिकेशन सेटअप
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

### Docsify दस्तऐवज सर्व्हर
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### व्हिज्युअलायझेशन प्रकल्प सेटअप
अर्थपूर्ण व्हिज्युअलायझेशनसारख्या प्रकल्पांसाठी (धडा 13):
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

### Jupyter नोटबुक्ससह काम करणे
1. रिपॉझिटरी रूटमध्ये Jupyter सुरू करा: `jupyter notebook`
2. इच्छित धड्याच्या फोल्डरमध्ये जा
3. `.ipynb` फाइल्स उघडा आणि सराव करा
4. नोटबुक्स स्पष्टीकरण आणि कोड सेल्ससह स्वयंपूर्ण आहेत
5. बहुतेक नोटबुक्स pandas, numpy, आणि matplotlib वापरतात - यांची स्थापना सुनिश्चित करा

### धड्यांची रचना
प्रत्येक धड्यात सामान्यतः समाविष्ट असते:
- `README.md` - मुख्य धड्याची सामग्री, सिद्धांत आणि उदाहरणांसह
- `notebook.ipynb` - प्रॅक्टिकल Jupyter नोटबुक सराव
- `assignment.ipynb` किंवा `assignment.md` - सराव असाइनमेंट्स
- `solution/` फोल्डर - सोल्यूशन नोटबुक्स आणि कोड
- `images/` फोल्डर - सहाय्यक व्हिज्युअल सामग्री

### क्विझ अॅप्लिकेशन विकास
- Vue.js 2 अॅप्लिकेशन विकासादरम्यान हॉट-रिलोडसह
- क्विझेस `quiz-app/src/assets/translations/` मध्ये संग्रहित
- प्रत्येक भाषेसाठी स्वतंत्र अनुवाद फोल्डर (en, fr, es, इ.)
- क्विझ क्रमांक 0 पासून सुरू होतो आणि 39 पर्यंत जातो (एकूण 40 क्विझ)

### अनुवाद जोडणे
- अनुवाद `translations/` फोल्डरमध्ये रिपॉझिटरी रूटवर जातात
- प्रत्येक भाषेचा इंग्रजीसारखा पूर्ण धड्यांचा आराखडा असतो
- GitHub Actions द्वारे स्वयंचलित अनुवाद (co-op-translator.yml)

## चाचणी सूचना

### क्विझ अॅप्लिकेशन चाचणी
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### नोटबुक चाचणी
- नोटबुक्ससाठी कोणतेही स्वयंचलित चाचणी फ्रेमवर्क अस्तित्वात नाही
- मॅन्युअल सत्यापन: सर्व सेल्स क्रमाने चालवा आणि त्रुटी नसल्याची खात्री करा
- डेटा फाइल्स प्रवेशयोग्य आहेत आणि आउटपुट योग्यरित्या तयार होतात याची खात्री करा
- व्हिज्युअलायझेशन योग्यरित्या रेंडर होतात याची तपासणी करा

### दस्तऐवज चाचणी
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### कोड गुणवत्ता तपासणी
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## कोड शैली मार्गदर्शक तत्त्वे

### Python (Jupyter नोटबुक्स)
- Python कोडसाठी PEP 8 शैली मार्गदर्शकांचे अनुसरण करा
- विश्लेषित डेटा स्पष्ट करणारी व्हेरिएबल नावे वापरा
- कोड सेल्सच्या आधी स्पष्टीकरणांसह Markdown सेल्स समाविष्ट करा
- कोड सेल्स एका संकल्पनेवर किंवा ऑपरेशनवर केंद्रित ठेवा
- डेटा मॅनिप्युलेशनसाठी pandas, व्हिज्युअलायझेशनसाठी matplotlib वापरा
- सामान्य आयात पॅटर्न:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Vue.js 2 शैली मार्गदर्शक आणि सर्वोत्तम पद्धतींचे अनुसरण करा
- `quiz-app/package.json` मध्ये ESLint कॉन्फिगरेशन
- Vue सिंगल-फाइल घटक (.vue फाइल्स) वापरा
- घटक-आधारित आर्किटेक्चर राखा
- बदल करण्यापूर्वी `npm run lint` चालवा

### Markdown दस्तऐवज
- स्पष्ट शीर्षकांची श्रेणी (# ## ### इ.) वापरा
- भाषा निर्दिष्ट करणाऱ्या कोड ब्लॉक्स समाविष्ट करा
- प्रतिमांसाठी alt टेक्स्ट जोडा
- संबंधित धडे आणि संसाधनांशी लिंक करा
- वाचनीयतेसाठी ओळींची लांबी योग्य ठेवा

### फाइल्सचे आयोजन
- क्रमांकित फोल्डर्समध्ये धड्यांची सामग्री (01-defining-data-science, इ.)
- `solution/` उपफोल्डर्समध्ये सोल्यूशन्स
- `translations/` फोल्डरमध्ये इंग्रजी संरचनेचे प्रतिबिंब
- डेटा फाइल्स `data/` किंवा धड्यांसाठी विशिष्ट फोल्डर्समध्ये ठेवा

## बिल्ड आणि डिप्लॉयमेंट

### क्विझ अॅप्लिकेशन डिप्लॉयमेंट
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Azure Static Web Apps डिप्लॉयमेंट
क्विझ-अॅप Azure Static Web Apps वर डिप्लॉय केले जाऊ शकते:
1. Azure Static Web App संसाधन तयार करा
2. GitHub रिपॉझिटरीशी कनेक्ट करा
3. बिल्ड सेटिंग्ज कॉन्फिगर करा:
   - अॅप स्थान: `quiz-app`
   - आउटपुट स्थान: `dist`
4. GitHub Actions वर्कफ्लो पुश केल्यावर स्वयंचलितपणे डिप्लॉय होईल

### दस्तऐवज साइट
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- रिपॉझिटरीमध्ये dev कंटेनर कॉन्फिगरेशन समाविष्ट आहे
- Codespaces स्वयंचलितपणे Python आणि Node.js वातावरण सेट करते
- GitHub UI द्वारे रिपॉझिटरी Codespace मध्ये उघडा
- सर्व आवश्यक गोष्टी स्वयंचलितपणे स्थापित होतात

## पुल रिक्वेस्ट मार्गदर्शक तत्त्वे

### सबमिट करण्यापूर्वी
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### PR शीर्षक स्वरूप
- स्पष्ट, वर्णनात्मक शीर्षके वापरा
- स्वरूप: `[घटक] संक्षिप्त वर्णन`
- उदाहरणे:
  - `[Lesson 7] Python नोटबुक आयात त्रुटी दुरुस्त करा`
  - `[Quiz App] जर्मन अनुवाद जोडा`
  - `[Docs] नवीन पूर्वापेक्षांसह README अपडेट करा`

### आवश्यक तपासण्या
- सर्व कोड त्रुटीशिवाय चालतो याची खात्री करा
- नोटबुक्स पूर्णपणे चालवतात याची पुष्टी करा
- Vue.js अॅप्स यशस्वीरित्या बिल्ड होतात याची खात्री करा
- दस्तऐवज दुवे कार्यरत आहेत याची तपासणी करा
- क्विझ अॅप्लिकेशन बदलल्यास चाचणी करा
- अनुवाद संरचना सुसंगत ठेवतात याची पुष्टी करा

### योगदान मार्गदर्शक तत्त्वे
- विद्यमान कोड शैली आणि नमुन्यांचे अनुसरण करा
- जटिल लॉजिकसाठी स्पष्टीकरणात्मक टिप्पण्या जोडा
- संबंधित दस्तऐवज अपडेट करा
- बदल लागू असल्यास विविध धड्यांमध्ये चाचणी करा
- CONTRIBUTING.md फाइल पुनरावलोकन करा

## अतिरिक्त टिप्पण्या

### सामान्यतः वापरल्या जाणाऱ्या लायब्ररी
- **pandas**: डेटा मॅनिप्युलेशन आणि विश्लेषण
- **numpy**: संख्यात्मक संगणन
- **matplotlib**: डेटा व्हिज्युअलायझेशन आणि प्लॉटिंग
- **seaborn**: सांख्यिकीय डेटा व्हिज्युअलायझेशन (काही धडे)
- **scikit-learn**: मशीन लर्निंग (प्रगत धडे)

### डेटा फाइल्ससह काम करणे
- डेटा फाइल्स `data/` फोल्डर किंवा धड्यासाठी विशिष्ट निर्देशिकांमध्ये स्थित आहेत
- बहुतेक नोटबुक्स डेटा फाइल्स सापेक्ष पथांमध्ये अपेक्षित करतात
- CSV फाइल्स प्राथमिक डेटा स्वरूप आहेत
- काही धडे नॉन-रिलेशनल डेटा उदाहरणांसाठी JSON वापरतात

### बहुभाषिक समर्थन
- स्वयंचलित GitHub Actions द्वारे 40+ भाषांमध्ये अनुवाद
- `.github/workflows/co-op-translator.yml` मध्ये अनुवाद कार्यप्रवाह
- `translations/` फोल्डरमध्ये भाषा कोडसह अनुवाद
- क्विझ अनुवाद `quiz-app/src/assets/translations/` मध्ये

### विकास वातावरण पर्याय
1. **स्थानिक विकास**: स्थानिकरित्या Python, Jupyter, Node.js स्थापित करा
2. **GitHub Codespaces**: क्लाउड-आधारित त्वरित विकास वातावरण
3. **VS Code Dev Containers**: स्थानिक कंटेनर-आधारित विकास
4. **Binder**: क्लाउडमध्ये नोटबुक्स लॉन्च करा (कॉन्फिगर केल्यास)

### धड्यांची सामग्री मार्गदर्शक तत्त्वे
- प्रत्येक धडा स्वतंत्र आहे परंतु मागील संकल्पनांवर आधारित आहे
- प्री-धडा क्विझेस पूर्व ज्ञानाची चाचणी करतात
- पोस्ट-धडा क्विझेस शिकवलेले बळकट करतात
- असाइनमेंट्स प्रॅक्टिकल सराव प्रदान करतात
- स्केच नोट्स व्हिज्युअल सारांश प्रदान करतात

### सामान्य समस्या सोडवणे

**Jupyter कर्नल समस्या:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**npm इंस्टॉल अपयश:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**नोटबुक्समध्ये आयात त्रुटी:**
- आवश्यक सर्व लायब्ररी स्थापित आहेत याची पुष्टी करा
- Python आवृत्ती सुसंगतता तपासा (Python 3.7+ शिफारस केलेले)
- व्हर्च्युअल वातावरण सक्रिय आहे याची खात्री करा

**Docsify लोड होत नाही:**
- रिपॉझिटरी रूटवरून सर्व्ह करत आहात याची पुष्टी करा
- `index.html` अस्तित्वात आहे याची खात्री करा
- योग्य नेटवर्क प्रवेश सुनिश्चित करा (पोर्ट 3000)

### कार्यक्षमता विचार
- मोठ्या डेटासेट्स नोटबुक्समध्ये लोड होण्यासाठी वेळ घेऊ शकतात
- जटिल प्लॉट्ससाठी व्हिज्युअलायझेशन रेंडरिंग मंद असू शकते
- Vue.js dev सर्व्हर जलद पुनरावृत्तीसाठी हॉट-रिलोड सक्षम करते
- उत्पादन बिल्ड्स ऑप्टिमाइझ आणि मिनिफाईड आहेत

### सुरक्षा टिप्पण्या
- संवेदनशील डेटा किंवा क्रेडेन्शियल्स कमिट करू नका
- क्लाउड धड्यांमध्ये कोणत्याही API कीसाठी पर्यावरणीय व्हेरिएबल्स वापरा
- Azure संबंधित धड्यांसाठी Azure खाते क्रेडेन्शियल्स आवश्यक असू शकतात
- सुरक्षा पॅचसाठी अवलंबित्व अद्यतनित ठेवा

## अनुवादांमध्ये योगदान
- GitHub Actions द्वारे व्यवस्थापित स्वयंचलित अनुवाद
- अनुवाद अचूकतेसाठी मॅन्युअल सुधारणा स्वागतार्ह
- विद्यमान अनुवाद फोल्डर संरचनेचे अनुसरण करा
- क्विझ दुवे भाषेचा पॅरामीटर समाविष्ट करण्यासाठी अपडेट करा: `?loc=fr`
- योग्य रेंडरिंगसाठी अनुवादित धडे चाचणी करा

## संबंधित संसाधने
- मुख्य अभ्यासक्रम: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- विद्यार्थी हब: https://docs.microsoft.com/learn/student-hub
- चर्चा मंच: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- इतर Microsoft अभ्यासक्रम: ML for Beginners, AI for Beginners, Web Dev for Beginners

## प्रकल्प देखभाल
- सामग्री अद्ययावत ठेवण्यासाठी नियमित अद्यतने
- समुदाय योगदान स्वागतार्ह
- GitHub वर समस्यांचे ट्रॅकिंग
- अभ्यासक्रम देखरेख करणाऱ्यांद्वारे PR पुनरावलोकन
- मासिक सामग्री पुनरावलोकन आणि अद्यतने

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.