<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:07:51+00:00",
  "source_file": "USAGE.md",
  "language_code": "sw"
}
-->
# Mwongozo wa Matumizi

Mwongozo huu unatoa mifano na mchakato wa kawaida wa kutumia mtaala wa Data Science kwa Kompyuta.

## Jedwali la Maudhui

- [Jinsi ya Kutumia Mtaala Huu](../..)
- [Kufanya Kazi na Masomo](../..)
- [Kufanya Kazi na Jupyter Notebooks](../..)
- [Kutumia Programu ya Maswali](../..)
- [Michakato ya Kawaida](../..)
- [Vidokezo kwa Wanaojifunza Wenyewe](../..)
- [Vidokezo kwa Walimu](../..)

## Jinsi ya Kutumia Mtaala Huu

Mtaala huu umeundwa kuwa rahisi na unaweza kutumika kwa njia mbalimbali:

- **Kujifunza kwa kasi yako mwenyewe**: Pitia masomo kwa kujitegemea kwa kasi yako
- **Mafunzo darasani**: Tumia kama kozi iliyopangwa na mwongozo wa mwalimu
- **Makundi ya kujifunza**: Jifunze kwa kushirikiana na wenzako
- **Muundo wa warsha**: Vipindi vya kujifunza vya muda mfupi na makini

## Kufanya Kazi na Masomo

Kila somo linafuata muundo thabiti ili kuongeza ufanisi wa kujifunza:

### Muundo wa Somo

1. **Maswali ya awali ya somo**: Jaribu ujuzi wako wa awali
2. **Sketchnote** (Hiari): Muhtasari wa kuona wa dhana kuu
3. **Video** (Hiari): Maudhui ya ziada ya video
4. **Somo la maandishi**: Dhana kuu na maelezo
5. **Jupyter Notebook**: Mazoezi ya vitendo ya kuandika programu
6. **Kazi ya nyumbani**: Fanya mazoezi ya kile ulichojifunza
7. **Maswali ya baada ya somo**: Imarisha uelewa wako

### Mfano wa Mchakato wa Somo

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

## Kufanya Kazi na Jupyter Notebooks

### Kuanza Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Kuendesha Seliseli za Notebook

1. **Tekeleza seli**: Bonyeza `Shift + Enter` au bofya kitufe cha "Run"
2. **Tekeleza seli zote**: Chagua "Cell" → "Run All" kutoka kwenye menyu
3. **Anzisha upya kernel**: Chagua "Kernel" → "Restart" ikiwa unakutana na matatizo

### Mfano: Kufanya Kazi na Data katika Notebook

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

### Kuhifadhi Kazi Yako

- Jupyter hujihifadhi mara kwa mara
- Hifadhi kwa mkono: Bonyeza `Ctrl + S` (au `Cmd + S` kwenye macOS)
- Maendeleo yako yanahifadhiwa katika faili ya `.ipynb`

## Kutumia Programu ya Maswali

### Kuendesha Programu ya Maswali Laini

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Kujibu Maswali

1. Maswali ya awali ya somo yanapatikana juu ya kila somo
2. Maswali ya baada ya somo yanapatikana chini ya kila somo
3. Kila jaribio lina maswali 3
4. Maswali yameundwa kuimarisha kujifunza, si kupima kwa kina

### Uorodheshaji wa Maswali

- Maswali yameorodheshwa 0-39 (maswali 40 kwa jumla)
- Kila somo kwa kawaida lina maswali ya awali na ya baada ya somo
- URL za maswali zinajumuisha namba ya jaribio: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Michakato ya Kawaida

### Mchakato 1: Njia ya Kompyuta Kabisa

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

### Mchakato 2: Kujifunza Mada Mahususi

Ikiwa unavutiwa na mada fulani:

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

### Mchakato 3: Kujifunza kwa Mradi

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Mchakato 4: Data Science kwa Mtandao

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Vidokezo kwa Wanaojifunza Wenyewe

### Kuwa na Mpangilio

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Fanya Mazoezi Mara kwa Mara

- Tengeneza muda maalum kila siku au wiki
- Kamilisha angalau somo moja kwa wiki
- Pitia masomo ya awali mara kwa mara

### Shirikiana na Jamii

- Jiunge na [Jamii ya Discord](https://aka.ms/ds4beginners/discord)
- Shiriki katika #Data-Science-for-Beginners Channel kwenye Discord [Majadiliano ya Discord](https://aka.ms/ds4beginners/discord)
- Shiriki maendeleo yako na uliza maswali

### Unda Miradi Yako Mwenyewe

Baada ya kukamilisha masomo, tumia dhana kwa miradi ya kibinafsi:

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

## Vidokezo kwa Walimu

### Kuandaa Darasa

1. Pitia [for-teachers.md](for-teachers.md) kwa mwongozo wa kina
2. Unda mazingira ya kushirikiana (GitHub Classroom au Codespaces)
3. Weka njia ya mawasiliano (Discord, Slack, au Teams)

### Kupanga Masomo

**Ratiba Inayopendekezwa ya Wiki 10:**

- **Wiki 1-2**: Utangulizi (Masomo 1-4)
- **Wiki 3-4**: Kufanya Kazi na Data (Masomo 5-8)
- **Wiki 5-6**: Uonyeshaji wa Data (Masomo 9-13)
- **Wiki 7-8**: Mzunguko wa Maisha wa Data Science (Masomo 14-16)
- **Wiki 9**: Data Science kwa Mtandao (Masomo 17-19)
- **Wiki 10**: Matumizi Halisi & Miradi ya Mwisho (Somo 20)

### Kuendesha Docsify kwa Ufikiaji Nje ya Mtandao

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Kuweka Alama za Kazi za Nyumbani

- Pitia notebooks za wanafunzi kwa mazoezi yaliyokamilika
- Angalia uelewa kupitia alama za maswali
- Tathmini miradi ya mwisho kwa kutumia kanuni za mzunguko wa maisha wa data science

### Kuunda Kazi za Nyumbani

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

## Kufanya Kazi Nje ya Mtandao

### Pakua Rasilimali

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Endesha Nyaraka Laini

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Endesha Programu ya Maswali Laini

```bash
cd quiz-app
npm run serve
```

## Kupata Maudhui Yaliyotafsiriwa

Tafsiri zinapatikana kwa lugha zaidi ya 40:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Kila tafsiri inafuata muundo sawa na toleo la Kiingereza.

## Rasilimali za Ziada

### Endelea Kujifunza

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Njia za kujifunza za ziada
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Rasilimali kwa wanafunzi
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Jukwaa la jamii

### Mitaala Inayohusiana

- [AI kwa Kompyuta](https://aka.ms/ai-beginners)
- [ML kwa Kompyuta](https://aka.ms/ml-beginners)
- [Web Dev kwa Kompyuta](https://aka.ms/webdev-beginners)
- [Generative AI kwa Kompyuta](https://aka.ms/genai-beginners)

## Kupata Msaada

- Angalia [TROUBLESHOOTING.md](TROUBLESHOOTING.md) kwa matatizo ya kawaida
- Tafuta [Masuala ya GitHub](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Jiunge na [Discord](https://aka.ms/ds4beginners/discord)
- Pitia [CONTRIBUTING.md](CONTRIBUTING.md) kuripoti matatizo au kuchangia

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya kibinadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.