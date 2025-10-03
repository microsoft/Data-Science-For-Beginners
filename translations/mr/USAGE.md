<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T14:58:45+00:00",
  "source_file": "USAGE.md",
  "language_code": "mr"
}
-->
# वापर मार्गदर्शक

ही मार्गदर्शिका डेटा सायन्स फॉर बिगिनर्स अभ्यासक्रमाचा वापर करण्यासाठी उदाहरणे आणि सामान्य कार्यप्रवाह प्रदान करते.

## विषय सूची

- [हा अभ्यासक्रम कसा वापरायचा](../..)
- [पाठांसोबत काम करणे](../..)
- [ज्युपिटर नोटबुक्ससोबत काम करणे](../..)
- [क्विझ अ‍ॅप्लिकेशन वापरणे](../..)
- [सामान्य कार्यप्रवाह](../..)
- [स्वत: शिकणाऱ्यांसाठी टिप्स](../..)
- [शिक्षकांसाठी टिप्स](../..)

## हा अभ्यासक्रम कसा वापरायचा

हा अभ्यासक्रम लवचिक आहे आणि विविध प्रकारे वापरला जाऊ शकतो:

- **स्वत: शिकणे**: स्वत:च्या गतीने स्वतंत्रपणे पाठ पूर्ण करा
- **वर्गात शिकवणे**: संरचित अभ्यासक्रम म्हणून मार्गदर्शित शिकवणीसह वापरा
- **अभ्यास गट**: सहकाऱ्यांसोबत सहयोगात्मकपणे शिकणे
- **कार्यशाळा स्वरूप**: तीव्र अल्पकालीन शिकवणी सत्रे

## पाठांसोबत काम करणे

प्रत्येक पाठ शिकण्याची क्षमता वाढवण्यासाठी सुसंगत संरचनेचे अनुसरण करतो:

### पाठ संरचना

1. **पाठपूर्व क्विझ**: तुमचे विद्यमान ज्ञान तपासा
2. **स्केच नोट** (ऐच्छिक): मुख्य संकल्पनांचा व्हिज्युअल सारांश
3. **व्हिडिओ** (ऐच्छिक): पूरक व्हिडिओ सामग्री
4. **लिखित पाठ**: मुख्य संकल्पना आणि स्पष्टीकरणे
5. **ज्युपिटर नोटबुक**: हाताळण्यायोग्य कोडिंग सराव
6. **असाइनमेंट**: तुम्ही शिकलेले सराव करा
7. **पाठोत्तर क्विझ**: तुमचे ज्ञान मजबूत करा

### पाठासाठी उदाहरण कार्यप्रवाह

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

## ज्युपिटर नोटबुक्ससोबत काम करणे

### ज्युपिटर सुरू करणे

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### नोटबुक सेल्स चालवणे

1. **सेल चालवा**: `Shift + Enter` दाबा किंवा "Run" बटणावर क्लिक करा
2. **सर्व सेल्स चालवा**: मेनूमधून "Cell" → "Run All" निवडा
3. **कर्नल रीस्टार्ट करा**: समस्या आल्यास "Kernel" → "Restart" निवडा

### उदाहरण: नोटबुकमध्ये डेटा सोबत काम करणे

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

### तुमचे काम जतन करणे

- ज्युपिटर वेळोवेळी स्वयंचलितपणे जतन करते
- मॅन्युअली जतन करा: `Ctrl + S` (किंवा macOS वर `Cmd + S`) दाबा
- तुमची प्रगती `.ipynb` फाईलमध्ये जतन केली जाते

## क्विझ अ‍ॅप्लिकेशन वापरणे

### स्थानिक स्तरावर क्विझ अ‍ॅप चालवणे

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### क्विझ घेणे

1. पाठपूर्व क्विझ प्रत्येक पाठाच्या शीर्षस्थानी लिंक केलेले असते
2. पाठोत्तर क्विझ प्रत्येक पाठाच्या तळाशी लिंक केलेले असते
3. प्रत्येक क्विझमध्ये 3 प्रश्न असतात
4. क्विझ शिकवणी मजबूत करण्यासाठी डिझाइन केलेले आहेत, संपूर्णपणे चाचणी घेण्यासाठी नाही

### क्विझ क्रमांक

- क्विझ 0-39 क्रमांकित आहेत (एकूण 40 क्विझ)
- प्रत्येक पाठामध्ये सामान्यतः एक पाठपूर्व आणि एक पाठोत्तर क्विझ असते
- क्विझ URL मध्ये क्विझ क्रमांक समाविष्ट असतो: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## सामान्य कार्यप्रवाह

### कार्यप्रवाह 1: पूर्ण नवशिक्या मार्ग

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

### कार्यप्रवाह 2: विशिष्ट विषय शिकणे

जर तुम्हाला विशिष्ट विषयात रस असेल:

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

### कार्यप्रवाह 3: प्रकल्प-आधारित शिकणे

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### कार्यप्रवाह 4: क्लाउड-आधारित डेटा सायन्स

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## स्वत: शिकणाऱ्यांसाठी टिप्स

### व्यवस्थित रहा

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### नियमित सराव करा

- दररोज किंवा दर आठवड्याला समर्पित वेळ ठेवा
- दर आठवड्याला किमान एक पाठ पूर्ण करा
- मागील पाठ वेळोवेळी पुनरावलोकन करा

### समुदायाशी संवाद साधा

- [Discord समुदाय](https://aka.ms/ds4beginners/discord) मध्ये सामील व्हा
- Discord मधील #Data-Science-for-Beginners चॅनेलमध्ये सहभागी व्हा [Discord Discussions](https://aka.ms/ds4beginners/discord)
- तुमची प्रगती शेअर करा आणि प्रश्न विचारा

### स्वत:चे प्रकल्प तयार करा

पाठ पूर्ण केल्यानंतर, वैयक्तिक प्रकल्पांमध्ये संकल्पना लागू करा:

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

## शिक्षकांसाठी टिप्स

### वर्ग सेटअप

1. तपशीलवार मार्गदर्शनासाठी [for-teachers.md](for-teachers.md) पुनरावलोकन करा
2. सामायिक वातावरण सेट करा (GitHub Classroom किंवा Codespaces)
3. संवाद चॅनेल स्थापन करा (Discord, Slack, किंवा Teams)

### पाठ नियोजन

**सुचवलेला 10-आठवड्यांचा वेळापत्रक:**

- **आठवडा 1-2**: परिचय (पाठ 1-4)
- **आठवडा 3-4**: डेटा सोबत काम करणे (पाठ 5-8)
- **आठवडा 5-6**: डेटा व्हिज्युअलायझेशन (पाठ 9-13)
- **आठवडा 7-8**: डेटा सायन्स जीवनचक्र (पाठ 14-16)
- **आठवडा 9**: क्लाउड डेटा सायन्स (पाठ 17-19)
- **आठवडा 10**: वास्तविक-जगातील अनुप्रयोग आणि अंतिम प्रकल्प (पाठ 20)

### ऑफलाइन प्रवेशासाठी Docsify चालवणे

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### असाइनमेंट ग्रेडिंग

- विद्यार्थ्यांच्या नोटबुक्स पुनरावलोकन करा आणि पूर्ण केलेल्या सराव तपासा
- क्विझ स्कोर्सद्वारे समज तपासा
- डेटा सायन्स जीवनचक्र तत्त्वांचा वापर करून अंतिम प्रकल्पांचे मूल्यांकन करा

### असाइनमेंट तयार करणे

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

## ऑफलाइन काम करणे

### संसाधने डाउनलोड करा

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### स्थानिक स्तरावर दस्तऐवज चालवा

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### स्थानिक स्तरावर क्विझ अ‍ॅप चालवा

```bash
cd quiz-app
npm run serve
```

## अनुवादित सामग्रीमध्ये प्रवेश करणे

40+ भाषांमध्ये अनुवाद उपलब्ध आहेत:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

प्रत्येक अनुवाद इंग्रजी आवृत्तीप्रमाणेच संरचना राखतो.

## अतिरिक्त संसाधने

### शिकणे सुरू ठेवा

- [Microsoft Learn](https://docs.microsoft.com/learn/) - अतिरिक्त शिकवणी मार्ग
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - विद्यार्थ्यांसाठी संसाधने
- [Azure AI Foundry](https://aka.ms/foundry/forum) - समुदाय मंच

### संबंधित अभ्यासक्रम

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## मदत मिळवणे

- सामान्य समस्यांसाठी [TROUBLESHOOTING.md](TROUBLESHOOTING.md) तपासा
- [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) शोधा
- आमच्या [Discord](https://aka.ms/ds4beginners/discord) मध्ये सामील व्हा
- समस्या नोंदवण्यासाठी किंवा योगदान देण्यासाठी [CONTRIBUTING.md](CONTRIBUTING.md) पुनरावलोकन करा

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरे त्रुटी किंवा अचूकतेच्या अभावाने युक्त असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.