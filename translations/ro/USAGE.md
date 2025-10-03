<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:09:27+00:00",
  "source_file": "USAGE.md",
  "language_code": "ro"
}
-->
# Ghid de Utilizare

Acest ghid oferă exemple și fluxuri de lucru comune pentru utilizarea curriculumului „Data Science for Beginners”.

## Cuprins

- [Cum să folosești acest curriculum](../..)
- [Lucrul cu lecțiile](../..)
- [Lucrul cu Jupyter Notebooks](../..)
- [Utilizarea aplicației de quiz](../..)
- [Fluxuri de lucru comune](../..)
- [Sfaturi pentru auto-învățare](../..)
- [Sfaturi pentru profesori](../..)

## Cum să folosești acest curriculum

Acest curriculum este conceput să fie flexibil și poate fi utilizat în mai multe moduri:

- **Învățare în ritm propriu**: Parcurge lecțiile independent, în ritmul tău
- **Predare în clasă**: Folosește-l ca un curs structurat cu instruire ghidată
- **Grupuri de studiu**: Învață colaborativ cu colegii
- **Format de workshop**: Sesiuni intensive de învățare pe termen scurt

## Lucrul cu lecțiile

Fiecare lecție urmează o structură consistentă pentru a maximiza învățarea:

### Structura lecției

1. **Quiz înainte de lecție**: Testează-ți cunoștințele existente
2. **Sketchnote** (Opțional): Rezumat vizual al conceptelor cheie
3. **Video** (Opțional): Conținut video suplimentar
4. **Lecție scrisă**: Concepte de bază și explicații
5. **Jupyter Notebook**: Exerciții practice de codare
6. **Temă**: Exersează ceea ce ai învățat
7. **Quiz după lecție**: Consolidează-ți înțelegerea

### Exemplu de flux de lucru pentru o lecție

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

## Lucrul cu Jupyter Notebooks

### Pornirea Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Rularea celulelor din notebook

1. **Execută o celulă**: Apasă `Shift + Enter` sau fă clic pe butonul „Run”
2. **Execută toate celulele**: Selectează „Cell” → „Run All” din meniu
3. **Restart kernel**: Selectează „Kernel” → „Restart” dacă întâmpini probleme

### Exemplu: Lucrul cu date într-un notebook

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

### Salvarea muncii tale

- Jupyter salvează automat periodic
- Salvează manual: Apasă `Ctrl + S` (sau `Cmd + S` pe macOS)
- Progresul tău este salvat în fișierul `.ipynb`

## Utilizarea aplicației de quiz

### Rularea aplicației de quiz local

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Completarea quiz-urilor

1. Quiz-urile înainte de lecție sunt legate la începutul fiecărei lecții
2. Quiz-urile după lecție sunt legate la sfârșitul fiecărei lecții
3. Fiecare quiz are 3 întrebări
4. Quiz-urile sunt concepute pentru a consolida învățarea, nu pentru a testa exhaustiv

### Numerotarea quiz-urilor

- Quiz-urile sunt numerotate de la 0 la 39 (40 de quiz-uri în total)
- Fiecare lecție are, de obicei, un quiz înainte și unul după
- URL-urile quiz-urilor includ numărul quiz-ului: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Fluxuri de lucru comune

### Flux de lucru 1: Parcurs pentru începători complet

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

### Flux de lucru 2: Învățare specifică unui subiect

Dacă ești interesat de un subiect specific:

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

### Flux de lucru 3: Învățare bazată pe proiecte

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Flux de lucru 4: Data Science bazată pe cloud

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Sfaturi pentru auto-învățare

### Fii organizat

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Exersează regulat

- Alocă timp dedicat în fiecare zi sau săptămână
- Completează cel puțin o lecție pe săptămână
- Revizuiește periodic lecțiile anterioare

### Implică-te în comunitate

- Alătură-te [comunității Discord](https://aka.ms/ds4beginners/discord)
- Participă în canalul #Data-Science-for-Beginners pe Discord [Discuții Discord](https://aka.ms/ds4beginners/discord)
- Împărtășește progresul tău și pune întrebări

### Construiește propriile proiecte

După ce ai finalizat lecțiile, aplică conceptele în proiecte personale:

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

## Sfaturi pentru profesori

### Configurarea clasei

1. Revizuiește [for-teachers.md](for-teachers.md) pentru îndrumări detaliate
2. Configurează un mediu comun (GitHub Classroom sau Codespaces)
3. Stabilește un canal de comunicare (Discord, Slack sau Teams)

### Planificarea lecțiilor

**Program sugerat de 10 săptămâni:**

- **Săptămâna 1-2**: Introducere (Lecțiile 1-4)
- **Săptămâna 3-4**: Lucrul cu date (Lecțiile 5-8)
- **Săptămâna 5-6**: Vizualizarea datelor (Lecțiile 9-13)
- **Săptămâna 7-8**: Ciclu de viață în Data Science (Lecțiile 14-16)
- **Săptămâna 9**: Data Science în cloud (Lecțiile 17-19)
- **Săptămâna 10**: Aplicații reale și proiecte finale (Lecția 20)

### Rularea Docsify pentru acces offline

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Evaluarea temelor

- Revizuiește notebook-urile studenților pentru exerciții completate
- Verifică înțelegerea prin scorurile quiz-urilor
- Evaluează proiectele finale folosind principiile ciclului de viață în Data Science

### Crearea temelor

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

## Lucrul offline

### Descărcarea resurselor

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Rularea documentației local

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Rularea aplicației de quiz local

```bash
cd quiz-app
npm run serve
```

## Accesarea conținutului tradus

Traducerile sunt disponibile în peste 40 de limbi:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Fiecare traducere păstrează aceeași structură ca versiunea în engleză.

## Resurse suplimentare

### Continuă să înveți

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Alte trasee de învățare
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Resurse pentru studenți
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Forum comunitar

### Curricula conexe

- [AI pentru Începători](https://aka.ms/ai-beginners)
- [ML pentru Începători](https://aka.ms/ml-beginners)
- [Web Dev pentru Începători](https://aka.ms/webdev-beginners)
- [Generative AI pentru Începători](https://aka.ms/genai-beginners)

## Obținerea ajutorului

- Verifică [TROUBLESHOOTING.md](TROUBLESHOOTING.md) pentru probleme comune
- Caută [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Alătură-te [Discord](https://aka.ms/ds4beginners/discord)
- Revizuiește [CONTRIBUTING.md](CONTRIBUTING.md) pentru a raporta probleme sau a contribui

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.