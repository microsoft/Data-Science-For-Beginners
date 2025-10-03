<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:10:43+00:00",
  "source_file": "USAGE.md",
  "language_code": "hr"
}
-->
# Vodič za korištenje

Ovaj vodič pruža primjere i uobičajene radne procese za korištenje kurikuluma "Data Science for Beginners".

## Sadržaj

- [Kako koristiti ovaj kurikulum](../..)
- [Rad s lekcijama](../..)
- [Rad s Jupyter Notebookovima](../..)
- [Korištenje aplikacije za kviz](../..)
- [Uobičajeni radni procesi](../..)
- [Savjeti za samostalne učenike](../..)
- [Savjeti za nastavnike](../..)

## Kako koristiti ovaj kurikulum

Ovaj kurikulum je dizajniran da bude fleksibilan i može se koristiti na više načina:

- **Samostalno učenje**: Radite kroz lekcije neovisno, vlastitim tempom
- **Nastava u učionici**: Koristite ga kao strukturirani tečaj uz vođenu nastavu
- **Studijske grupe**: Učite surađujući s kolegama
- **Radionice**: Intenzivne kratkoročne sesije učenja

## Rad s lekcijama

Svaka lekcija slijedi dosljednu strukturu kako bi se maksimiziralo učenje:

### Struktura lekcije

1. **Kviz prije lekcije**: Testirajte svoje postojeće znanje
2. **Sketchnote** (Opcionalno): Vizualni sažetak ključnih pojmova
3. **Video** (Opcionalno): Dodatni video sadržaj
4. **Pisani materijal**: Osnovni pojmovi i objašnjenja
5. **Jupyter Notebook**: Praktične vježbe kodiranja
6. **Zadatak**: Vježbajte ono što ste naučili
7. **Kviz nakon lekcije**: Učvrstite svoje razumijevanje

### Primjer radnog procesa za lekciju

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

## Rad s Jupyter Notebookovima

### Pokretanje Jupytera

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Pokretanje ćelija u Notebooku

1. **Izvršite ćeliju**: Pritisnite `Shift + Enter` ili kliknite gumb "Run"
2. **Izvršite sve ćelije**: Odaberite "Cell" → "Run All" iz izbornika
3. **Ponovno pokrenite kernel**: Odaberite "Kernel" → "Restart" ako naiđete na probleme

### Primjer: Rad s podacima u Notebooku

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

### Spremanje vašeg rada

- Jupyter automatski sprema periodično
- Ručno spremanje: Pritisnite `Ctrl + S` (ili `Cmd + S` na macOS-u)
- Vaš napredak se sprema u `.ipynb` datoteku

## Korištenje aplikacije za kviz

### Pokretanje aplikacije za kviz lokalno

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Polaganje kvizova

1. Kvizovi prije lekcije nalaze se na vrhu svake lekcije
2. Kvizovi nakon lekcije nalaze se na dnu svake lekcije
3. Svaki kviz ima 3 pitanja
4. Kvizovi su osmišljeni da učvrste učenje, a ne da iscrpno testiraju

### Numeracija kvizova

- Kvizovi su numerirani od 0-39 (ukupno 40 kvizova)
- Svaka lekcija obično ima kviz prije i nakon lekcije
- URL-ovi kvizova uključuju broj kviza: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Uobičajeni radni procesi

### Radni proces 1: Put za potpune početnike

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

### Radni proces 2: Učenje specifičnih tema

Ako vas zanima određena tema:

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

### Radni proces 3: Učenje temeljeno na projektima

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Radni proces 4: Data Science u oblaku

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Savjeti za samostalne učenike

### Ostanite organizirani

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Redovito vježbajte

- Odvojite posvećeno vrijeme svaki dan ili tjedan
- Završite barem jednu lekciju tjedno
- Povremeno pregledajte prethodne lekcije

### Sudjelujte u zajednici

- Pridružite se [Discord zajednici](https://aka.ms/ds4beginners/discord)
- Sudjelujte u kanalu #Data-Science-for-Beginners na Discordu [Discord Discussions](https://aka.ms/ds4beginners/discord)
- Podijelite svoj napredak i postavljajte pitanja

### Izradite vlastite projekte

Nakon završetka lekcija, primijenite pojmove na osobne projekte:

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

## Savjeti za nastavnike

### Postavljanje učionice

1. Pregledajte [for-teachers.md](for-teachers.md) za detaljne upute
2. Postavite zajedničko okruženje (GitHub Classroom ili Codespaces)
3. Uspostavite komunikacijski kanal (Discord, Slack ili Teams)

### Planiranje lekcija

**Predloženi raspored za 10 tjedana:**

- **Tjedan 1-2**: Uvod (Lekcije 1-4)
- **Tjedan 3-4**: Rad s podacima (Lekcije 5-8)
- **Tjedan 5-6**: Vizualizacija podataka (Lekcije 9-13)
- **Tjedan 7-8**: Životni ciklus Data Science-a (Lekcije 14-16)
- **Tjedan 9**: Data Science u oblaku (Lekcije 17-19)
- **Tjedan 10**: Primjene u stvarnom svijetu i završni projekti (Lekcija 20)

### Pokretanje Docsify-a za offline pristup

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Ocjenjivanje zadataka

- Pregledajte studentske notebookove za dovršene vježbe
- Provjerite razumijevanje kroz rezultate kvizova
- Procijenite završne projekte koristeći principe životnog ciklusa Data Science-a

### Izrada zadataka

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

## Rad offline

### Preuzimanje resursa

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Pokretanje dokumentacije lokalno

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Pokretanje aplikacije za kviz lokalno

```bash
cd quiz-app
npm run serve
```

## Pristup prevedenom sadržaju

Prijevodi su dostupni na više od 40 jezika:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Svaki prijevod zadržava istu strukturu kao i engleska verzija.

## Dodatni resursi

### Nastavite učiti

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Dodatni putovi učenja
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Resursi za studente
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Forum zajednice

### Povezani kurikulumi

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## Dobivanje pomoći

- Provjerite [TROUBLESHOOTING.md](TROUBLESHOOTING.md) za uobičajene probleme
- Pretražite [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Pridružite se našem [Discordu](https://aka.ms/ds4beginners/discord)
- Pregledajte [CONTRIBUTING.md](CONTRIBUTING.md) za prijavu problema ili doprinos

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.