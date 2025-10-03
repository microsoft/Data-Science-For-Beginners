<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:13:02+00:00",
  "source_file": "USAGE.md",
  "language_code": "lt"
}
-->
# Naudojimo vadovas

Šis vadovas pateikia pavyzdžius ir dažniausiai naudojamus darbo procesus, susijusius su „Duomenų mokslas pradedantiesiems“ mokymo programa.

## Turinys

- [Kaip naudotis šia mokymo programa](../..)
- [Darbas su pamokomis](../..)
- [Darbas su Jupyter Notebook](../..)
- [Naudojimasis viktorinos programa](../..)
- [Dažniausiai naudojami darbo procesai](../..)
- [Patarimai savarankiškai besimokantiems](../..)
- [Patarimai mokytojams](../..)

## Kaip naudotis šia mokymo programa

Ši mokymo programa yra lanksti ir gali būti naudojama įvairiais būdais:

- **Savarankiškas mokymasis**: Pamokas atlikite savarankiškai savo tempu
- **Pamokos klasėje**: Naudokite kaip struktūruotą kursą su mokytojo vadovavimu
- **Studijų grupės**: Mokykitės bendradarbiaudami su kolegomis
- **Seminarų formatas**: Intensyvios trumpalaikės mokymosi sesijos

## Darbas su pamokomis

Kiekviena pamoka turi nuoseklią struktūrą, kad mokymasis būtų efektyvus:

### Pamokos struktūra

1. **Prieš pamoką viktorina**: Patikrinkite savo esamas žinias
2. **Sketchnote** (Pasirinktinai): Vizualinė pagrindinių sąvokų santrauka
3. **Vaizdo įrašas** (Pasirinktinai): Papildomas vaizdo turinys
4. **Rašytinė pamoka**: Pagrindinės sąvokos ir paaiškinimai
5. **Jupyter Notebook**: Praktiniai kodavimo pratimai
6. **Užduotis**: Praktikuokite tai, ką išmokote
7. **Po pamokos viktorina**: Sustiprinkite savo supratimą

### Pamokos darbo proceso pavyzdys

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

## Darbas su Jupyter Notebook

### Jupyter paleidimas

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Notebook langelių vykdymas

1. **Vykdyti langelį**: Paspauskite `Shift + Enter` arba spustelėkite mygtuką „Run“
2. **Vykdyti visus langelius**: Pasirinkite „Cell“ → „Run All“ iš meniu
3. **Perkrauti branduolį**: Pasirinkite „Kernel“ → „Restart“, jei kyla problemų

### Pavyzdys: Darbas su duomenimis Notebook

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

### Darbo išsaugojimas

- Jupyter periodiškai automatiškai išsaugo
- Rankinis išsaugojimas: Paspauskite `Ctrl + S` (arba `Cmd + S` macOS)
- Jūsų pažanga išsaugoma `.ipynb` faile

## Naudojimasis viktorinos programa

### Viktorinos programos paleidimas vietoje

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Viktorinos atlikimas

1. Prieš pamoką viktorinos yra pateiktos pamokos pradžioje
2. Po pamokos viktorinos yra pateiktos pamokos pabaigoje
3. Kiekviena viktorina turi 3 klausimus
4. Viktorinos skirtos mokymosi stiprinimui, o ne išsamiam testavimui

### Viktorinos numeracija

- Viktorinos numeruojamos nuo 0 iki 39 (iš viso 40 viktorinų)
- Kiekviena pamoka paprastai turi prieš ir po pamokos viktoriną
- Viktorinos URL apima viktorinos numerį: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Dažniausiai naudojami darbo procesai

### Darbo procesas 1: Pradedančiųjų kelias

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

### Darbo procesas 2: Mokymasis pagal temą

Jei jus domina konkreti tema:

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

### Darbo procesas 3: Mokymasis pagal projektą

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Darbo procesas 4: Duomenų mokslas debesyje

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Patarimai savarankiškai besimokantiems

### Organizuokite savo mokymąsi

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Praktikuokite reguliariai

- Skirkite tam skirtą laiką kiekvieną dieną ar savaitę
- Atlikite bent vieną pamoką per savaitę
- Periodiškai peržiūrėkite ankstesnes pamokas

### Dalyvaukite bendruomenėje

- Prisijunkite prie [Discord bendruomenės](https://aka.ms/ds4beginners/discord)
- Dalyvaukite #Data-Science-for-Beginners kanale Discord [Discord diskusijos](https://aka.ms/ds4beginners/discord)
- Dalinkitės savo pažanga ir užduokite klausimus

### Kurkite savo projektus

Baigę pamokas, pritaikykite sąvokas asmeniniams projektams:

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

## Patarimai mokytojams

### Klasės paruošimas

1. Peržiūrėkite [for-teachers.md](for-teachers.md) išsamiems nurodymams
2. Sukurkite bendrą aplinką (GitHub Classroom arba Codespaces)
3. Nustatykite komunikacijos kanalą (Discord, Slack arba Teams)

### Pamokų planavimas

**Siūlomas 10 savaičių tvarkaraštis:**

- **1-2 savaitė**: Įvadas (Pamokos 1-4)
- **3-4 savaitė**: Darbas su duomenimis (Pamokos 5-8)
- **5-6 savaitė**: Duomenų vizualizacija (Pamokos 9-13)
- **7-8 savaitė**: Duomenų mokslo gyvavimo ciklas (Pamokos 14-16)
- **9 savaitė**: Duomenų mokslas debesyje (Pamokos 17-19)
- **10 savaitė**: Realūs pritaikymai ir baigiamieji projektai (Pamoka 20)

### Docsify paleidimas neprisijungus

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Užduočių vertinimas

- Peržiūrėkite studentų Notebook užbaigtus pratimus
- Patikrinkite supratimą pagal viktorinos rezultatus
- Įvertinkite baigiamuosius projektus pagal duomenų mokslo gyvavimo ciklo principus

### Užduočių kūrimas

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

## Darbas neprisijungus

### Atsisiųskite išteklius

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Dokumentacijos paleidimas vietoje

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Viktorinos programos paleidimas vietoje

```bash
cd quiz-app
npm run serve
```

## Prieiga prie išversto turinio

Vertimai yra prieinami daugiau nei 40 kalbų:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Kiekvienas vertimas išlaiko tokią pačią struktūrą kaip ir angliška versija.

## Papildomi ištekliai

### Tęskite mokymąsi

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Papildomi mokymosi keliai
- [Studentų centras](https://docs.microsoft.com/learn/student-hub) - Ištekliai studentams
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Bendruomenės forumas

### Susijusios mokymo programos

- [Dirbtinis intelektas pradedantiesiems](https://aka.ms/ai-beginners)
- [Mašininis mokymasis pradedantiesiems](https://aka.ms/ml-beginners)
- [Web kūrimas pradedantiesiems](https://aka.ms/webdev-beginners)
- [Generatyvus dirbtinis intelektas pradedantiesiems](https://aka.ms/genai-beginners)

## Pagalbos gavimas

- Peržiūrėkite [TROUBLESHOOTING.md](TROUBLESHOOTING.md) dėl dažniausiai pasitaikančių problemų
- Ieškokite [GitHub klausimų](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Prisijunkite prie mūsų [Discord](https://aka.ms/ds4beginners/discord)
- Peržiūrėkite [CONTRIBUTING.md](CONTRIBUTING.md), kad praneštumėte apie problemas ar prisidėtumėte

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.