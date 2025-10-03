<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:07:29+00:00",
  "source_file": "USAGE.md",
  "language_code": "tl"
}
-->
# Gabay sa Paggamit

Ang gabay na ito ay nagbibigay ng mga halimbawa at karaniwang daloy ng trabaho para sa paggamit ng kurikulum ng Data Science for Beginners.

## Talaan ng Nilalaman

- [Paano Gamitin ang Kurikulum na Ito](../..)
- [Paggawa sa mga Aralin](../..)
- [Paggamit ng Jupyter Notebooks](../..)
- [Paggamit ng Quiz Application](../..)
- [Karaniwang Daloy ng Trabaho](../..)
- [Mga Tip para sa mga Nag-aaral Mag-isa](../..)
- [Mga Tip para sa mga Guro](../..)

## Paano Gamitin ang Kurikulum na Ito

Ang kurikulum na ito ay idinisenyo upang maging flexible at maaaring gamitin sa iba't ibang paraan:

- **Pag-aaral sa sariling bilis**: Magtrabaho sa mga aralin nang mag-isa sa iyong sariling bilis
- **Instruksyon sa silid-aralan**: Gamitin bilang isang nakabalangkas na kurso na may gabay na pagtuturo
- **Mga grupo ng pag-aaral**: Matutong sama-sama kasama ang mga kapwa mag-aaral
- **Format ng workshop**: Masinsinang panandaliang sesyon ng pag-aaral

## Paggawa sa mga Aralin

Ang bawat aralin ay sumusunod sa isang pare-parehong istruktura upang mapakinabangan ang pag-aaral:

### Istruktura ng Aralin

1. **Pre-lesson Quiz**: Subukan ang iyong kasalukuyang kaalaman
2. **Sketchnote** (Opsyonal): Visual na buod ng mga pangunahing konsepto
3. **Video** (Opsyonal): Karagdagang video na nilalaman
4. **Nakatalang Aralin**: Mga pangunahing konsepto at paliwanag
5. **Jupyter Notebook**: Mga hands-on na coding exercise
6. **Assignment**: Sanayin ang natutunan
7. **Post-lesson Quiz**: Palakasin ang iyong pag-unawa

### Halimbawa ng Daloy ng Trabaho para sa Isang Aralin

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

## Paggamit ng Jupyter Notebooks

### Pagsisimula ng Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Pagpapatakbo ng Notebook Cells

1. **Patakbuhin ang isang cell**: Pindutin ang `Shift + Enter` o i-click ang "Run" na button
2. **Patakbuhin ang lahat ng cell**: Piliin ang "Cell" → "Run All" mula sa menu
3. **I-restart ang kernel**: Piliin ang "Kernel" → "Restart" kung may mga isyu

### Halimbawa: Paggawa sa Data sa isang Notebook

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

### Pag-save ng Iyong Trabaho

- Ang Jupyter ay awtomatikong nagsa-save nang pana-panahon
- Manu-manong mag-save: Pindutin ang `Ctrl + S` (o `Cmd + S` sa macOS)
- Ang iyong progreso ay naka-save sa `.ipynb` na file

## Paggamit ng Quiz Application

### Pagpapatakbo ng Quiz App Lokal

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Pagsagot sa mga Quiz

1. Ang mga pre-lesson quiz ay naka-link sa itaas ng bawat aralin
2. Ang mga post-lesson quiz ay naka-link sa ibaba ng bawat aralin
3. Ang bawat quiz ay may 3 tanong
4. Ang mga quiz ay idinisenyo upang palakasin ang pag-aaral, hindi upang lubos na subukan

### Pagbilang ng Quiz

- Ang mga quiz ay binibilang mula 0-39 (kabuuang 40 quiz)
- Ang bawat aralin ay karaniwang may pre at post quiz
- Ang mga URL ng quiz ay may kasamang numero ng quiz: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Karaniwang Daloy ng Trabaho

### Daloy ng Trabaho 1: Landas para sa Ganap na Baguhan

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

### Daloy ng Trabaho 2: Pag-aaral ng Tiyak na Paksa

Kung interesado ka sa isang partikular na paksa:

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

### Daloy ng Trabaho 3: Pag-aaral Batay sa Proyekto

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Daloy ng Trabaho 4: Data Science na Batay sa Cloud

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Mga Tip para sa mga Nag-aaral Mag-isa

### Maging Organisado

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Magpraktis nang Regular

- Maglaan ng nakatakdang oras araw-araw o lingguhan
- Kumpletuhin ang hindi bababa sa isang aralin bawat linggo
- Balikan ang mga nakaraang aralin paminsan-minsan

### Makilahok sa Komunidad

- Sumali sa [Discord community](https://aka.ms/ds4beginners/discord)
- Makilahok sa #Data-Science-for-Beginners Channel sa Discord [Discord Discussions](https://aka.ms/ds4beginners/discord)
- Ibahagi ang iyong progreso at magtanong

### Gumawa ng Sariling Proyekto

Pagkatapos kumpletuhin ang mga aralin, i-apply ang mga konsepto sa personal na proyekto:

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

## Mga Tip para sa mga Guro

### Paghahanda ng Silid-Aralan

1. Suriin ang [for-teachers.md](for-teachers.md) para sa detalyadong gabay
2. Mag-set up ng shared environment (GitHub Classroom o Codespaces)
3. Magtatag ng communication channel (Discord, Slack, o Teams)

### Pagpaplano ng Aralin

**Iminungkahing 10-Linggong Iskedyul:**

- **Linggo 1-2**: Panimula (Mga Aralin 1-4)
- **Linggo 3-4**: Paggawa sa Data (Mga Aralin 5-8)
- **Linggo 5-6**: Data Visualization (Mga Aralin 9-13)
- **Linggo 7-8**: Data Science Lifecycle (Mga Aralin 14-16)
- **Linggo 9**: Cloud Data Science (Mga Aralin 17-19)
- **Linggo 10**: Mga Aplikasyon sa Tunay na Mundo at Panghuling Proyekto (Aralin 20)

### Pagpapatakbo ng Docsify para sa Offline Access

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Pag-grado ng Assignment

- Suriin ang mga notebook ng mag-aaral para sa mga natapos na exercise
- Tingnan ang pag-unawa sa pamamagitan ng mga score sa quiz
- Suriin ang mga panghuling proyekto gamit ang mga prinsipyo ng data science lifecycle

### Paglikha ng Assignment

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

## Paggawa Offline

### Pag-download ng Mga Resource

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Pagpapatakbo ng Dokumentasyon Lokal

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Pagpapatakbo ng Quiz App Lokal

```bash
cd quiz-app
npm run serve
```

## Pag-access sa Isinaling Nilalaman

Ang mga salin ay available sa mahigit 40 na wika:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Ang bawat salin ay nagpapanatili ng parehong istruktura tulad ng bersyong Ingles.

## Karagdagang Mga Resource

### Magpatuloy sa Pag-aaral

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Karagdagang mga landas sa pag-aaral
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Mga resource para sa mga mag-aaral
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Community forum

### Kaugnay na Kurikulum

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## Pagkuha ng Tulong

- Suriin ang [TROUBLESHOOTING.md](TROUBLESHOOTING.md) para sa mga karaniwang isyu
- Maghanap sa [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Sumali sa aming [Discord](https://aka.ms/ds4beginners/discord)
- Suriin ang [CONTRIBUTING.md](CONTRIBUTING.md) upang mag-ulat ng mga isyu o mag-ambag

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.