<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T14:57:53+00:00",
  "source_file": "USAGE.md",
  "language_code": "hi"
}
-->
# उपयोग गाइड

यह गाइड शुरुआती डेटा साइंस पाठ्यक्रम का उपयोग करने के उदाहरण और सामान्य कार्यप्रवाह प्रदान करता है।

## सामग्री तालिका

- [इस पाठ्यक्रम का उपयोग कैसे करें](../..)
- [पाठों के साथ काम करना](../..)
- [जुपिटर नोटबुक्स के साथ काम करना](../..)
- [क्विज़ एप्लिकेशन का उपयोग करना](../..)
- [सामान्य कार्यप्रवाह](../..)
- [स्व-शिक्षार्थियों के लिए सुझाव](../..)
- [शिक्षकों के लिए सुझाव](../..)

## इस पाठ्यक्रम का उपयोग कैसे करें

यह पाठ्यक्रम लचीला है और इसे कई तरीकों से उपयोग किया जा सकता है:

- **स्व-गति से सीखना**: अपने समय और गति के अनुसार पाठों को स्वतंत्र रूप से पूरा करें
- **कक्षा शिक्षण**: संरचित पाठ्यक्रम के रूप में निर्देशित शिक्षण के साथ उपयोग करें
- **अध्ययन समूह**: साथियों के साथ सहयोगात्मक रूप से सीखें
- **कार्यशाला प्रारूप**: गहन अल्पकालिक सीखने के सत्र

## पाठों के साथ काम करना

प्रत्येक पाठ एक सुसंगत संरचना का अनुसरण करता है ताकि सीखने को अधिकतम किया जा सके:

### पाठ संरचना

1. **प्री-लेसन क्विज़**: अपने मौजूदा ज्ञान का परीक्षण करें
2. **स्केच नोट** (वैकल्पिक): मुख्य अवधारणाओं का दृश्य सारांश
3. **वीडियो** (वैकल्पिक): पूरक वीडियो सामग्री
4. **लिखित पाठ**: मुख्य अवधारणाएं और व्याख्याएं
5. **जुपिटर नोटबुक**: व्यावहारिक कोडिंग अभ्यास
6. **असाइनमेंट**: आपने जो सीखा है उसका अभ्यास करें
7. **पोस्ट-लेसन क्विज़**: अपनी समझ को मजबूत करें

### पाठ के लिए उदाहरण कार्यप्रवाह

```bash
# 1. Navigate to the lesson directory
cd 1-Introduction/01-defining-data-science

# 2. Read the README.md
# Open README.md in your browser or editor

# 3. Take the pre-lesson quiz
# Click the quiz link in the README

# 4. Open the Jupyter notebook (if available)
jupyter notebook

# 5. Complete the exercises in the notebook

# 6. Work on the assignment

# 7. Take the post-lesson quiz
```

## जुपिटर नोटबुक्स के साथ काम करना

### जुपिटर शुरू करना

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### नोटबुक सेल्स चलाना

1. **सेल चलाएं**: `Shift + Enter` दबाएं या "Run" बटन पर क्लिक करें
2. **सभी सेल्स चलाएं**: मेनू से "Cell" → "Run All" चुनें
3. **कर्नल रीस्टार्ट करें**: यदि आपको समस्याओं का सामना करना पड़े तो "Kernel" → "Restart" चुनें

### उदाहरण: नोटबुक में डेटा के साथ काम करना

```python
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load a dataset
df = pd.read_csv('data/sample.csv')

# Explore the data
df.head()
df.info()
df.describe()

# Create a visualization
plt.figure(figsize=(10, 6))
plt.plot(df['column_name'])
plt.title('Sample Visualization')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()
```

### अपना काम सहेजना

- जुपिटर समय-समय पर स्वचालित रूप से सहेजता है
- मैन्युअल रूप से सहेजें: `Ctrl + S` दबाएं (या macOS पर `Cmd + S`)
- आपकी प्रगति `.ipynb` फ़ाइल में सहेजी जाती है

## क्विज़ एप्लिकेशन का उपयोग करना

### स्थानीय रूप से क्विज़ ऐप चलाना

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### क्विज़ लेना

1. प्री-लेसन क्विज़ प्रत्येक पाठ के शीर्ष पर लिंक किए गए हैं
2. पोस्ट-लेसन क्विज़ प्रत्येक पाठ के नीचे लिंक किए गए हैं
3. प्रत्येक क्विज़ में 3 प्रश्न होते हैं
4. क्विज़ सीखने को मजबूत करने के लिए डिज़ाइन किए गए हैं, न कि व्यापक परीक्षण के लिए

### क्विज़ नंबरिंग

- क्विज़ 0-39 तक क्रमांकित हैं (कुल 40 क्विज़)
- प्रत्येक पाठ में आमतौर पर एक प्री और पोस्ट क्विज़ होता है
- क्विज़ URLs में क्विज़ नंबर शामिल होता है: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## सामान्य कार्यप्रवाह

### कार्यप्रवाह 1: पूर्ण शुरुआती पथ

```bash
# 1. Set up your environment (see INSTALLATION.md)

# 2. Start with Lesson 1
cd 1-Introduction/01-defining-data-science

# 3. For each lesson:
#    - Take pre-lesson quiz
#    - Read the lesson content
#    - Work through the notebook
#    - Complete the assignment
#    - Take post-lesson quiz

# 4. Progress through all 20 lessons sequentially
```

### कार्यप्रवाह 2: विषय-विशिष्ट सीखना

यदि आप किसी विशेष विषय में रुचि रखते हैं:

```bash
# Example: Focus on Data Visualization
cd 3-Data-Visualization

# Explore lessons 9-13:
# - Lesson 9: Visualizing Quantities
# - Lesson 10: Visualizing Distributions
# - Lesson 11: Visualizing Proportions
# - Lesson 12: Visualizing Relationships
# - Lesson 13: Meaningful Visualizations
```

### कार्यप्रवाह 3: प्रोजेक्ट-आधारित सीखना

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### कार्यप्रवाह 4: क्लाउड-आधारित डेटा साइंस

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## स्व-शिक्षार्थियों के लिए सुझाव

### संगठित रहें

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### नियमित रूप से अभ्यास करें

- हर दिन या सप्ताह में समर्पित समय निर्धारित करें
- कम से कम एक पाठ प्रति सप्ताह पूरा करें
- समय-समय पर पिछले पाठों की समीक्षा करें

### समुदाय के साथ जुड़ें

- [Discord समुदाय](https://aka.ms/ds4beginners/discord) में शामिल हों
- Discord में #Data-Science-for-Beginners चैनल में भाग लें [Discord Discussions](https://aka.ms/ds4beginners/discord)
- अपनी प्रगति साझा करें और प्रश्न पूछें

### अपने स्वयं के प्रोजेक्ट बनाएं

पाठों को पूरा करने के बाद, व्यक्तिगत प्रोजेक्ट्स पर अवधारणाओं को लागू करें:

```python
# Example: Analyze your own dataset
import pandas as pd

# Load your own data
my_data = pd.read_csv('my-project/data.csv')

# Apply techniques learned
# - Data cleaning (Lesson 8)
# - Exploratory data analysis (Lesson 7)
# - Visualization (Lessons 9-13)
# - Analysis (Lesson 15)
```

## शिक्षकों के लिए सुझाव

### कक्षा सेटअप

1. विस्तृत मार्गदर्शन के लिए [for-teachers.md](for-teachers.md) की समीक्षा करें
2. साझा वातावरण सेट करें (GitHub Classroom या Codespaces)
3. संचार चैनल स्थापित करें (Discord, Slack, या Teams)

### पाठ योजना

**सुझाई गई 10-सप्ताह की अनुसूची:**

- **सप्ताह 1-2**: परिचय (पाठ 1-4)
- **सप्ताह 3-4**: डेटा के साथ काम करना (पाठ 5-8)
- **सप्ताह 5-6**: डेटा विज़ुअलाइज़ेशन (पाठ 9-13)
- **सप्ताह 7-8**: डेटा साइंस जीवनचक्र (पाठ 14-16)
- **सप्ताह 9**: क्लाउड डेटा साइंस (पाठ 17-19)
- **सप्ताह 10**: वास्तविक दुनिया के अनुप्रयोग और अंतिम प्रोजेक्ट्स (पाठ 20)

### ऑफलाइन एक्सेस के लिए Docsify चलाना

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### असाइनमेंट ग्रेडिंग

- छात्र नोटबुक्स की समीक्षा करें कि अभ्यास पूरे किए गए हैं
- क्विज़ स्कोर के माध्यम से समझ की जांच करें
- डेटा साइंस जीवनचक्र सिद्धांतों का उपयोग करके अंतिम प्रोजेक्ट्स का मूल्यांकन करें

### असाइनमेंट बनाना

```python
# Example custom assignment template
"""
Assignment: [Topic]

Objective: [Learning goal]

Dataset: [Provide or have students find one]

Tasks:
1. Load and explore the dataset
2. Clean and prepare the data
3. Create at least 3 visualizations
4. Perform analysis
5. Communicate findings

Deliverables:
- Jupyter notebook with code and explanations
- Written summary of findings
"""
```

## ऑफलाइन काम करना

### संसाधन डाउनलोड करें

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### स्थानीय रूप से दस्तावेज़ चलाएं

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### स्थानीय रूप से क्विज़ ऐप चलाएं

```bash
cd quiz-app
npm run serve
```

## अनुवादित सामग्री तक पहुंच

40+ भाषाओं में अनुवाद उपलब्ध हैं:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

प्रत्येक अनुवाद अंग्रेजी संस्करण के समान संरचना बनाए रखता है।

## अतिरिक्त संसाधन

### सीखना जारी रखें

- [Microsoft Learn](https://docs.microsoft.com/learn/) - अतिरिक्त सीखने के पथ
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - छात्रों के लिए संसाधन
- [Azure AI Foundry](https://aka.ms/foundry/forum) - सामुदायिक मंच

### संबंधित पाठ्यक्रम

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## सहायता प्राप्त करना

- सामान्य समस्याओं के लिए [TROUBLESHOOTING.md](TROUBLESHOOTING.md) की जांच करें
- [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) खोजें
- हमारे [Discord](https://aka.ms/ds4beginners/discord) में शामिल हों
- समस्याओं की रिपोर्ट करने या योगदान करने के लिए [CONTRIBUTING.md](CONTRIBUTING.md) की समीक्षा करें

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।