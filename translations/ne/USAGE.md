<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T14:59:07+00:00",
  "source_file": "USAGE.md",
  "language_code": "ne"
}
-->
# प्रयोग मार्गदर्शन

यो मार्गदर्शनले Data Science for Beginners पाठ्यक्रम प्रयोग गर्नका लागि उदाहरणहरू र सामान्य कार्यप्रवाहहरू प्रदान गर्दछ।

## सामग्री तालिका

- [यो पाठ्यक्रम कसरी प्रयोग गर्ने](../..)
- [पाठहरूसँग काम गर्ने](../..)
- [Jupyter Notebooksसँग काम गर्ने](../..)
- [क्विज एप्लिकेसन प्रयोग गर्ने](../..)
- [सामान्य कार्यप्रवाहहरू](../..)
- [आफैँ सिक्नेहरूका लागि सुझावहरू](../..)
- [शिक्षकहरूका लागि सुझावहरू](../..)

## यो पाठ्यक्रम कसरी प्रयोग गर्ने

यो पाठ्यक्रम लचिलो रूपमा डिजाइन गरिएको छ र विभिन्न तरिकामा प्रयोग गर्न सकिन्छ:

- **आफैँ सिक्ने**: पाठहरू स्वतन्त्र रूपमा आफ्नो गति अनुसार पूरा गर्नुहोस्।
- **कक्षा शिक्षण**: संरचित पाठ्यक्रमको रूपमा निर्देशित शिक्षणको साथ प्रयोग गर्नुहोस्।
- **अध्ययन समूहहरू**: सहकर्मीहरूसँग मिलेर सिक्नुहोस्।
- **कार्यशाला ढाँचा**: छोटो अवधिको गहन सिकाइ सत्रहरू।

## पाठहरूसँग काम गर्ने

प्रत्येक पाठले सिकाइलाई अधिकतम बनाउनको लागि एक सुसंगत संरचना अनुसरण गर्दछ:

### पाठ संरचना

1. **पाठ अघि क्विज**: तपाईंको हालको ज्ञान परीक्षण गर्नुहोस्।
2. **स्केच नोट** (वैकल्पिक): मुख्य अवधारणाहरूको दृश्य सारांश।
3. **भिडियो** (वैकल्पिक): पूरक भिडियो सामग्री।
4. **लेखिएको पाठ**: मुख्य अवधारणाहरू र व्याख्याहरू।
5. **Jupyter Notebook**: कोडिङ अभ्यासहरू।
6. **असाइनमेन्ट**: तपाईंले सिकेको अभ्यास गर्नुहोस्।
7. **पाठ पछि क्विज**: तपाईंको बुझाइलाई सुदृढ गर्नुहोस्।

### पाठको लागि उदाहरण कार्यप्रवाह

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

## Jupyter Notebooksसँग काम गर्ने

### Jupyter सुरु गर्ने

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Notebook सेलहरू चलाउने

1. **सेल चलाउनुहोस्**: `Shift + Enter` थिच्नुहोस् वा "Run" बटन क्लिक गर्नुहोस्।
2. **सबै सेलहरू चलाउनुहोस्**: मेनुबाट "Cell" → "Run All" चयन गर्नुहोस्।
3. **कर्नेल पुनः सुरु गर्नुहोस्**: समस्या आएमा "Kernel" → "Restart" चयन गर्नुहोस्।

### उदाहरण: Notebook मा डाटासँग काम गर्ने

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

### तपाईंको काम बचत गर्ने

- Jupyter समय-समयमा स्वतः बचत गर्छ।
- म्यानुअली बचत गर्नुहोस्: `Ctrl + S` (वा macOS मा `Cmd + S`) थिच्नुहोस्।
- तपाईंको प्रगति `.ipynb` फाइलमा बचत हुन्छ।

## क्विज एप्लिकेसन प्रयोग गर्ने

### स्थानीय रूपमा क्विज एप चलाउने

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### क्विजहरू लिने

1. पाठ अघि क्विजहरू प्रत्येक पाठको माथि लिंक गरिएको हुन्छ।
2. पाठ पछि क्विजहरू प्रत्येक पाठको तल लिंक गरिएको हुन्छ।
3. प्रत्येक क्विजमा 3 प्रश्नहरू हुन्छन्।
4. क्विजहरू सिकाइलाई सुदृढ गर्न डिजाइन गरिएको हो, व्यापक परीक्षण गर्न होइन।

### क्विज नम्बरिङ

- क्विजहरू 0-39 नम्बर गरिएको छ (कुल 40 क्विजहरू)।
- प्रत्येक पाठमा सामान्यतया एक पाठ अघि र एक पाठ पछि क्विज हुन्छ।
- क्विज URL मा क्विज नम्बर समावेश छ: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## सामान्य कार्यप्रवाहहरू

### कार्यप्रवाह 1: पूर्ण प्रारम्भिक मार्ग

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

### कार्यप्रवाह 2: विषय-विशिष्ट सिकाइ

यदि तपाईंलाई कुनै विशेष विषयमा रुचि छ भने:

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

### कार्यप्रवाह 3: परियोजना-आधारित सिकाइ

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### कार्यप्रवाह 4: क्लाउड-आधारित डाटा साइन्स

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## आफैँ सिक्नेहरूका लागि सुझावहरू

### व्यवस्थित रहनुहोस्

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### नियमित अभ्यास गर्नुहोस्

- प्रत्येक दिन वा हप्तामा समर्पित समय छुट्याउनुहोस्।
- हरेक हप्ता कम्तीमा एक पाठ पूरा गर्नुहोस्।
- अघिल्लो पाठहरू समय-समयमा पुनरावलोकन गर्नुहोस्।

### समुदायसँग संलग्न हुनुहोस्

- [Discord समुदाय](https://aka.ms/ds4beginners/discord) मा सामेल हुनुहोस्।
- Discord मा #Data-Science-for-Beginners च्यानलमा भाग लिनुहोस् [Discord Discussions](https://aka.ms/ds4beginners/discord)।
- तपाईंको प्रगति साझा गर्नुहोस् र प्रश्नहरू सोध्नुहोस्।

### आफ्नै परियोजनाहरू निर्माण गर्नुहोस्

पाठहरू पूरा गरेपछि, व्यक्तिगत परियोजनाहरूमा अवधारणाहरू लागू गर्नुहोस्:

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

## शिक्षकहरूका लागि सुझावहरू

### कक्षा सेटअप

1. विस्तृत मार्गदर्शनको लागि [for-teachers.md](for-teachers.md) समीक्षा गर्नुहोस्।
2. साझा वातावरण सेटअप गर्नुहोस् (GitHub Classroom वा Codespaces)।
3. सञ्चार च्यानल स्थापना गर्नुहोस् (Discord, Slack, वा Teams)।

### पाठ योजना

**सुझाव गरिएको 10-हप्ताको तालिका:**

- **हप्ता 1-2**: परिचय (पाठ 1-4)
- **हप्ता 3-4**: डाटासँग काम गर्ने (पाठ 5-8)
- **हप्ता 5-6**: डाटा दृश्यात्मकता (पाठ 9-13)
- **हप्ता 7-8**: डाटा साइन्स जीवनचक्र (पाठ 14-16)
- **हप्ता 9**: क्लाउड डाटा साइन्स (पाठ 17-19)
- **हप्ता 10**: वास्तविक-विश्व अनुप्रयोगहरू र अन्तिम परियोजनाहरू (पाठ 20)

### Docsify चलाएर अफलाइन पहुँच

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### असाइनमेन्ट ग्रेडिङ

- विद्यार्थीका Notebook हरूमा पूरा गरिएका अभ्यासहरू समीक्षा गर्नुहोस्।
- क्विज स्कोरहरू मार्फत बुझाइ जाँच गर्नुहोस्।
- डाटा साइन्स जीवनचक्र सिद्धान्तहरू प्रयोग गरेर अन्तिम परियोजनाहरू मूल्याङ्कन गर्नुहोस्।

### असाइनमेन्ट सिर्जना गर्ने

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

## अफलाइन काम गर्ने

### स्रोतहरू डाउनलोड गर्नुहोस्

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### स्थानीय रूपमा डकुमेन्टेसन चलाउनुहोस्

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### स्थानीय रूपमा क्विज एप चलाउनुहोस्

```bash
cd quiz-app
npm run serve
```

## अनुवादित सामग्री पहुँच गर्ने

अनुवादहरू 40+ भाषाहरूमा उपलब्ध छन्:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

प्रत्येक अनुवादले अंग्रेजी संस्करणको समान संरचना कायम राख्छ।

## अतिरिक्त स्रोतहरू

### सिकाइ जारी राख्नुहोस्

- [Microsoft Learn](https://docs.microsoft.com/learn/) - थप सिकाइ मार्गहरू।
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - विद्यार्थीहरूका लागि स्रोतहरू।
- [Azure AI Foundry](https://aka.ms/foundry/forum) - समुदाय फोरम।

### सम्बन्धित पाठ्यक्रमहरू

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## सहयोग प्राप्त गर्ने

- सामान्य समस्याहरूका लागि [TROUBLESHOOTING.md](TROUBLESHOOTING.md) जाँच गर्नुहोस्।
- [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) खोज्नुहोस्।
- हाम्रो [Discord](https://aka.ms/ds4beginners/discord) मा सामेल हुनुहोस्।
- समस्या रिपोर्ट गर्न वा योगदान गर्न [CONTRIBUTING.md](CONTRIBUTING.md) समीक्षा गर्नुहोस्।

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी यथासम्भव शुद्धताको प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। यसको मूल भाषामा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्त्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुने छैनौं।