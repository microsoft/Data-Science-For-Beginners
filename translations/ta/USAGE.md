<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-11T15:11:11+00:00",
  "source_file": "USAGE.md",
  "language_code": "ta"
}
-->
# பயன்பாட்டு வழிகாட்டி

இந்த வழிகாட்டி, Data Science for Beginners பாடத்திட்டத்தை பயன்படுத்துவதற்கான உதாரணங்கள் மற்றும் பொதுவான பணிச்சூழல்களை வழங்குகிறது.

## உள்ளடக்க அட்டவணை

- [இந்த பாடத்திட்டத்தை எப்படி பயன்படுத்துவது](../..)
- [பாடங்களைப் பயன்படுத்துவது](../..)
- [Jupyter Notebooks உடன் வேலை செய்வது](../..)
- [வினாடி வினா பயன்பாட்டை பயன்படுத்துவது](../..)
- [பொதுவான பணிச்சூழல்கள்](../..)
- [சுயமாக கற்றுக்கொள்வதற்கான குறிப்புகள்](../..)
- [ஆசிரியர்களுக்கான குறிப்புகள்](../..)

## இந்த பாடத்திட்டத்தை எப்படி பயன்படுத்துவது

இந்த பாடத்திட்டம் பல்வேறு முறைகளில் பயன்படுத்துவதற்காக வடிவமைக்கப்பட்டுள்ளது:

- **சுயமாக கற்றல்**: உங்கள் சொந்த வேகத்தில் தனியாக பாடங்களை முடிக்கவும்
- **வகுப்பு கற்பித்தல்**: வழிகாட்டப்பட்ட கற்பித்தலுடன் அமைந்த பாடமாக பயன்படுத்தவும்
- **கற்கும் குழுக்கள்**: சக மாணவர்களுடன் இணைந்து கற்றுக்கொள்ளவும்
- **வார்ப்பெழு வடிவம்**: குறுகிய காலத்தில் தீவிரமாக கற்றல் அமர்வுகள்

## பாடங்களைப் பயன்படுத்துவது

ஒவ்வொரு பாடமும் கற்றலை அதிகரிக்க ஒரே மாதிரியான அமைப்பை பின்பற்றுகிறது:

### பாட அமைப்பு

1. **பாடத்திற்கு முன் வினாடி வினா**: உங்கள் தற்போதைய அறிவை சோதிக்கவும்
2. **Sketchnote** (விருப்பம்): முக்கிய கருத்துக்களின் காட்சிப்பட வடிவம்
3. **வீடியோ** (விருப்பம்): கூடுதல் வீடியோ உள்ளடக்கம்
4. **எழுத்து பாடம்**: முக்கிய கருத்துகள் மற்றும் விளக்கங்கள்
5. **Jupyter Notebook**: கையால் எழுதும் குறியீட்டு பயிற்சிகள்
6. **பணி**: நீங்கள் கற்றதைப் பயிற்சி செய்யவும்
7. **பாடத்திற்கு பின் வினாடி வினா**: உங்கள் புரிதலை உறுதிப்படுத்தவும்

### ஒரு பாடத்திற்கான உதாரண பணிச்சூழல்

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

## Jupyter Notebooks உடன் வேலை செய்வது

### Jupyter தொடங்குவது

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Notebook Cells இயக்குவது

1. **ஒரு செல்களை இயக்கவும்**: `Shift + Enter` அழுத்தவும் அல்லது "Run" பொத்தானை கிளிக் செய்யவும்
2. **அனைத்து செல்களை இயக்கவும்**: "Cell" → "Run All" என்பதை மெனுவில் தேர்ந்தெடுக்கவும்
3. **கேர்னலை மீண்டும் தொடங்கவும்**: "Kernel" → "Restart" என்பதை தேர்ந்தெடுக்கவும், நீங்கள் சிக்கல்களை சந்தித்தால்

### உதாரணம்: Notebook-இல் தரவுடன் வேலை செய்வது

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

### உங்கள் பணியைச் சேமிக்கவும்

- Jupyter தானாகவே காலகாலமாக சேமிக்கிறது
- கையால் சேமிக்க: `Ctrl + S` (macOS-ல் `Cmd + S`) அழுத்தவும்
- உங்கள் முன்னேற்றம் `.ipynb` கோப்பில் சேமிக்கப்படுகிறது

## வினாடி வினா பயன்பாட்டை பயன்படுத்துவது

### வினாடி வினா பயன்பாட்டை உள்ளூரில் இயக்குவது

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### வினாடி வினாக்களை எடுப்பது

1. பாடத்திற்கு முன் வினாடி வினாக்கள் ஒவ்வொரு பாடத்தின் மேல் இணைக்கப்பட்டுள்ளன
2. பாடத்திற்கு பின் வினாடி வினாக்கள் ஒவ்வொரு பாடத்தின் கீழ் இணைக்கப்பட்டுள்ளன
3. ஒவ்வொரு வினாடி வினாவிலும் 3 கேள்விகள் உள்ளன
4. வினாடி வினாக்கள் கற்றலை உறுதிப்படுத்த வடிவமைக்கப்பட்டவை, முழுமையாக சோதிக்க அல்ல

### வினாடி வினா எண் அமைப்பு

- வினாடி வினாக்கள் 0-39 (மொத்தம் 40) என எண்களிடப்பட்டுள்ளன
- ஒவ்வொரு பாடத்திலும் பொதுவாக ஒரு முன் மற்றும் பின் வினாடி வினா இருக்கும்
- வினாடி வினா URLs வினாடி வினா எண்ணை உள்ளடக்கியது: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## பொதுவான பணிச்சூழல்கள்

### பணிச்சூழல் 1: முழுமையான தொடக்க பாதை

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

### பணிச்சூழல் 2: குறிப்பிட்ட தலைப்புக்கான கற்றல்

நீங்கள் ஒரு குறிப்பிட்ட தலைப்பில் ஆர்வமாக இருந்தால்:

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

### பணிச்சூழல் 3: திட்ட அடிப்படையிலான கற்றல்

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### பணிச்சூழல் 4: மேக அடிப்படையிலான தரவியல்

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## சுயமாக கற்றுக்கொள்வதற்கான குறிப்புகள்

### ஒழுங்காக இருக்கவும்

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### தொடர்ந்து பயிற்சி செய்யவும்

- ஒவ்வொரு நாளும் அல்லது வாரமும் ஒதுக்கப்பட்ட நேரத்தை அமைக்கவும்
- வாரத்திற்கு குறைந்தது ஒரு பாடத்தை முடிக்கவும்
- முந்தைய பாடங்களை காலகாலமாக மீண்டும் பார்வையிடவும்

### சமூகத்துடன் ஈடுபடவும்

- [Discord சமூகத்தில்](https://aka.ms/ds4beginners/discord) சேரவும்
- Discord-இல் #Data-Science-for-Beginners சேனலில் கலந்துரையாடல்களில் பங்கேற்கவும் [Discord Discussions](https://aka.ms/ds4beginners/discord)
- உங்கள் முன்னேற்றத்தை பகிர்ந்து கேள்விகளை கேட்கவும்

### உங்கள் சொந்த திட்டங்களை உருவாக்கவும்

பாடங்களை முடித்த பிறகு, தனிப்பட்ட திட்டங்களில் கருத்துக்களைப் பயன்படுத்தவும்:

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

## ஆசிரியர்களுக்கான குறிப்புகள்

### வகுப்பு அமைப்பு

1. [for-teachers.md](for-teachers.md) ஐப் பார்வையிடவும், விரிவான வழிகாட்டுதலுக்காக
2. பகிரப்பட்ட சூழலை அமைக்கவும் (GitHub Classroom அல்லது Codespaces)
3. தொடர்பு சேனலை நிறுவவும் (Discord, Slack, அல்லது Teams)

### பாட திட்டமிடல்

**பரிந்துரைக்கப்பட்ட 10-வார அட்டவணை:**

- **வாரம் 1-2**: அறிமுகம் (பாடங்கள் 1-4)
- **வாரம் 3-4**: தரவுடன் வேலை செய்வது (பாடங்கள் 5-8)
- **வாரம் 5-6**: தரவின் காட்சிப்படுத்தல் (பாடங்கள் 9-13)
- **வாரம் 7-8**: தரவியல் வாழ்க்கைச் சுழற்சி (பாடங்கள் 14-16)
- **வாரம் 9**: மேக தரவியல் (பாடங்கள் 17-19)
- **வாரம் 10**: உண்மையான பயன்பாடுகள் & இறுதி திட்டங்கள் (பாடம் 20)

### Docsify ஐ ஆஃப்லைனில் அணுக இயக்குவது

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### பணிகளை மதிப்பீடு செய்வது

- மாணவர்களின் Notebook-களை முடிக்கப்பட்ட பயிற்சிகளுக்காக மதிப்பீடு செய்யவும்
- வினாடி வினா மதிப்பெண்கள் மூலம் புரிதலைச் சரிபார்க்கவும்
- தரவியல் வாழ்க்கைச் சுழற்சி கோட்பாடுகளைப் பயன்படுத்தி இறுதி திட்டங்களை மதிப்பீடு செய்யவும்

### பணிகளை உருவாக்குவது

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

## ஆஃப்லைனில் வேலை செய்வது

### வளங்களைப் பதிவிறக்கவும்

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### உள்ளூரில் ஆவணங்களை இயக்கவும்

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### உள்ளூரில் வினாடி வினா பயன்பாட்டை இயக்கவும்

```bash
cd quiz-app
npm run serve
```

## மொழிபெயர்க்கப்பட்ட உள்ளடக்கத்தை அணுகுவது

மொழிபெயர்ப்புகள் 40+ மொழிகளில் கிடைக்கின்றன:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

ஒவ்வொரு மொழிபெயர்ப்பும் ஆங்கில பதிப்பின் ஒரே அமைப்பை பராமரிக்கிறது.

## கூடுதல் வளங்கள்

### கற்றலை தொடரவும்

- [Microsoft Learn](https://docs.microsoft.com/learn/) - கூடுதல் கற்றல் பாதைகள்
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - மாணவர்களுக்கான வளங்கள்
- [Azure AI Foundry](https://aka.ms/foundry/forum) - சமூக மன்றம்

### தொடர்புடைய பாடத்திட்டங்கள்

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## உதவி பெறுவது

- பொதுவான சிக்கல்களுக்கு [TROUBLESHOOTING.md](TROUBLESHOOTING.md) ஐச் சரிபார்க்கவும்
- [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) ஐத் தேடவும்
- எங்கள் [Discord](https://aka.ms/ds4beginners/discord) சமூகத்தில் சேரவும்
- சிக்கல்களைப் புகாரளிக்க அல்லது பங்களிக்க [CONTRIBUTING.md](CONTRIBUTING.md) ஐப் பார்வையிடவும்

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.