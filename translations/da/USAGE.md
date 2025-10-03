<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:04:24+00:00",
  "source_file": "USAGE.md",
  "language_code": "da"
}
-->
# Brugsvejledning

Denne vejledning giver eksempler og almindelige arbejdsgange til brug af Data Science for Beginners-kurset.

## Indholdsfortegnelse

- [Sådan bruger du dette kursus](../..)
- [Arbejde med lektioner](../..)
- [Arbejde med Jupyter Notebooks](../..)
- [Brug af quiz-applikationen](../..)
- [Almindelige arbejdsgange](../..)
- [Tips til selvstuderende](../..)
- [Tips til undervisere](../..)

## Sådan bruger du dette kursus

Dette kursus er designet til at være fleksibelt og kan bruges på flere måder:

- **Selvstudium**: Gennemgå lektionerne uafhængigt i dit eget tempo
- **Klasseundervisning**: Brug som et struktureret kursus med vejledning
- **Studiegrupper**: Lær sammen med andre
- **Workshop-format**: Intensiv kortvarig læring

## Arbejde med lektioner

Hver lektion følger en konsekvent struktur for at maksimere læringen:

### Lektionens struktur

1. **Quiz før lektionen**: Test din eksisterende viden
2. **Sketchnote** (Valgfrit): Visuel opsummering af nøglebegreber
3. **Video** (Valgfrit): Supplerende videomateriale
4. **Skriftlig lektion**: Kernekoncepter og forklaringer
5. **Jupyter Notebook**: Praktiske kodningsøvelser
6. **Opgave**: Øv det, du har lært
7. **Quiz efter lektionen**: Styrk din forståelse

### Eksempel på arbejdsgang for en lektion

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

## Arbejde med Jupyter Notebooks

### Start Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Kør Notebook-celler

1. **Kør en celle**: Tryk `Shift + Enter` eller klik på "Run"-knappen
2. **Kør alle celler**: Vælg "Cell" → "Run All" i menuen
3. **Genstart kernel**: Vælg "Kernel" → "Restart", hvis du oplever problemer

### Eksempel: Arbejde med data i en Notebook

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

### Gem dit arbejde

- Jupyter gemmer automatisk med jævne mellemrum
- Gem manuelt: Tryk `Ctrl + S` (eller `Cmd + S` på macOS)
- Din fremgang gemmes i `.ipynb`-filen

## Brug af quiz-applikationen

### Kør quiz-applikationen lokalt

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Tag quizzes

1. Quiz før lektionen findes øverst i hver lektion
2. Quiz efter lektionen findes nederst i hver lektion
3. Hver quiz har 3 spørgsmål
4. Quizzes er designet til at styrke læringen, ikke til at teste udtømmende

### Nummerering af quizzes

- Quizzes er nummereret 0-39 (i alt 40 quizzes)
- Hver lektion har typisk en quiz før og efter
- Quiz-URL'er inkluderer quiznummeret: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Almindelige arbejdsgange

### Arbejdsgang 1: Begyndervej

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

### Arbejdsgang 2: Emnespecifik læring

Hvis du er interesseret i et specifikt emne:

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

### Arbejdsgang 3: Projektbaseret læring

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Arbejdsgang 4: Cloud-baseret data science

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Tips til selvstuderende

### Hold dig organiseret

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Øv regelmæssigt

- Sæt tid af hver dag eller uge
- Gennemfør mindst én lektion om ugen
- Gennemgå tidligere lektioner med jævne mellemrum

### Deltag i fællesskabet

- Bliv medlem af [Discord-fællesskabet](https://aka.ms/ds4beginners/discord)
- Deltag i #Data-Science-for-Beginners-kanalen på Discord [Discord Diskussioner](https://aka.ms/ds4beginners/discord)
- Del din fremgang og stil spørgsmål

### Byg dine egne projekter

Efter at have gennemført lektionerne, anvend koncepterne på personlige projekter:

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

## Tips til undervisere

### Opsætning af klasseværelse

1. Gennemgå [for-teachers.md](for-teachers.md) for detaljeret vejledning
2. Opsæt et delt miljø (GitHub Classroom eller Codespaces)
3. Etabler en kommunikationskanal (Discord, Slack eller Teams)

### Planlægning af lektioner

**Foreslået 10-ugers plan:**

- **Uge 1-2**: Introduktion (Lektioner 1-4)
- **Uge 3-4**: Arbejde med data (Lektioner 5-8)
- **Uge 5-6**: Datavisualisering (Lektioner 9-13)
- **Uge 7-8**: Data Science-livscyklus (Lektioner 14-16)
- **Uge 9**: Cloud Data Science (Lektioner 17-19)
- **Uge 10**: Virkelige anvendelser & afsluttende projekter (Lektion 20)

### Kør Docsify for offline adgang

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Bedømmelse af opgaver

- Gennemgå studerendes notebooks for færdige øvelser
- Tjek forståelse gennem quizresultater
- Evaluer afsluttende projekter ved hjælp af principperne for data science-livscyklus

### Oprettelse af opgaver

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

## Arbejde offline

### Download ressourcer

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Kør dokumentation lokalt

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Kør quiz-applikationen lokalt

```bash
cd quiz-app
npm run serve
```

## Adgang til oversat indhold

Oversættelser er tilgængelige på 40+ sprog:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Hver oversættelse har samme struktur som den engelske version.

## Yderligere ressourcer

### Fortsæt læringen

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Yderligere læringsforløb
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Ressourcer til studerende
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Fællesskabsforum

### Relaterede kurser

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## Få hjælp

- Tjek [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for almindelige problemer
- Søg i [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Deltag i vores [Discord](https://aka.ms/ds4beginners/discord)
- Gennemgå [CONTRIBUTING.md](CONTRIBUTING.md) for at rapportere problemer eller bidrage

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.