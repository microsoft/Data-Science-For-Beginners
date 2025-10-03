<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:11:09+00:00",
  "source_file": "USAGE.md",
  "language_code": "sl"
}
-->
# Vodnik za uporabo

Ta vodnik ponuja primere in običajne delovne tokove za uporabo učnega načrta "Data Science for Beginners".

## Kazalo vsebine

- [Kako uporabljati ta učni načrt](../..)
- [Delo z lekcijami](../..)
- [Delo z Jupyter Notebooks](../..)
- [Uporaba aplikacije za kvize](../..)
- [Običajni delovni tokovi](../..)
- [Nasveti za samostojne učence](../..)
- [Nasveti za učitelje](../..)

## Kako uporabljati ta učni načrt

Ta učni načrt je zasnovan tako, da je prilagodljiv in ga je mogoče uporabljati na več načinov:

- **Samostojno učenje**: Lekcije obdelujte neodvisno in v svojem tempu
- **Poučevanje v razredu**: Uporabite ga kot strukturiran tečaj z vodenim poučevanjem
- **Študijske skupine**: Učite se skupaj s kolegi
- **Delavnice**: Intenzivne kratkoročne učne seje

## Delo z lekcijami

Vsaka lekcija sledi dosledni strukturi za maksimalno učenje:

### Struktura lekcije

1. **Predhodni kviz**: Preverite svoje obstoječe znanje
2. **Sketchnote** (neobvezno): Vizualni povzetek ključnih konceptov
3. **Video** (neobvezno): Dopolnilna video vsebina
4. **Pisna lekcija**: Osnovni koncepti in razlage
5. **Jupyter Notebook**: Praktične vaje kodiranja
6. **Naloga**: Vadite, kar ste se naučili
7. **Zaključni kviz**: Okrepite svoje razumevanje

### Primer delovnega toka za lekcijo

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

## Delo z Jupyter Notebooks

### Zagon Jupyterja

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Zagon celic v Notebooku

1. **Izvedite celico**: Pritisnite `Shift + Enter` ali kliknite gumb "Run"
2. **Izvedite vse celice**: Izberite "Cell" → "Run All" v meniju
3. **Ponovni zagon jedra**: Izberite "Kernel" → "Restart", če naletite na težave

### Primer: Delo s podatki v Notebooku

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

### Shranjevanje vašega dela

- Jupyter samodejno shranjuje občasno
- Ročno shranjevanje: Pritisnite `Ctrl + S` (ali `Cmd + S` na macOS)
- Vaš napredek je shranjen v datoteki `.ipynb`

## Uporaba aplikacije za kvize

### Zagon aplikacije za kvize lokalno

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Reševanje kvizov

1. Predhodni kvizi so povezani na vrhu vsake lekcije
2. Zaključni kvizi so povezani na dnu vsake lekcije
3. Vsak kviz ima 3 vprašanja
4. Kvizi so zasnovani za krepitev učenja, ne za izčrpno testiranje

### Oštevilčenje kvizov

- Kvizi so oštevilčeni od 0 do 39 (skupaj 40 kvizov)
- Vsaka lekcija običajno vsebuje predhodni in zaključni kviz
- URL-ji kvizov vključujejo številko kviza: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Običajni delovni tokovi

### Delovni tok 1: Pot popolnega začetnika

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

### Delovni tok 2: Učenje specifičnih tem

Če vas zanima določena tema:

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

### Delovni tok 3: Učenje na podlagi projektov

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Delovni tok 4: Podatkovna znanost v oblaku

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Nasveti za samostojne učence

### Bodite organizirani

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Redno vadite

- Vsak dan ali teden si rezervirajte čas za učenje
- Dokončajte vsaj eno lekcijo na teden
- Občasno preglejte prejšnje lekcije

### Povežite se s skupnostjo

- Pridružite se [Discord skupnosti](https://aka.ms/ds4beginners/discord)
- Sodelujte v kanalu #Data-Science-for-Beginners na Discordu [Discord Discussions](https://aka.ms/ds4beginners/discord)
- Delite svoj napredek in postavljajte vprašanja

### Ustvarite svoje projekte

Po zaključku lekcij uporabite koncepte v osebnih projektih:

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

## Nasveti za učitelje

### Priprava učilnice

1. Preglejte [for-teachers.md](for-teachers.md) za podrobna navodila
2. Nastavite skupno okolje (GitHub Classroom ali Codespaces)
3. Ustanovite komunikacijski kanal (Discord, Slack ali Teams)

### Načrtovanje lekcij

**Predlagan 10-tedenski urnik:**

- **1.-2. teden**: Uvod (Lekcije 1-4)
- **3.-4. teden**: Delo s podatki (Lekcije 5-8)
- **5.-6. teden**: Vizualizacija podatkov (Lekcije 9-13)
- **7.-8. teden**: Življenjski cikel podatkovne znanosti (Lekcije 14-16)
- **9. teden**: Podatkovna znanost v oblaku (Lekcije 17-19)
- **10. teden**: Resnične aplikacije in zaključni projekti (Lekcija 20)

### Zagon Docsify za dostop brez povezave

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Ocena nalog

- Preglejte študentske Notebooke za dokončane vaje
- Preverite razumevanje prek rezultatov kvizov
- Ocenite zaključne projekte z uporabo načel življenjskega cikla podatkovne znanosti

### Ustvarjanje nalog

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

## Delo brez povezave

### Prenos virov

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Zagon dokumentacije lokalno

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Zagon aplikacije za kvize lokalno

```bash
cd quiz-app
npm run serve
```

## Dostop do prevedene vsebine

Prevodi so na voljo v več kot 40 jezikih:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Vsak prevod ohranja enako strukturo kot angleška različica.

## Dodatni viri

### Nadaljujte z učenjem

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Dodatne učne poti
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Viri za študente
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Skupnostni forum

### Povezani učni načrti

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## Pomoč

- Preverite [TROUBLESHOOTING.md](TROUBLESHOOTING.md) za pogoste težave
- Iščite [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Pridružite se našemu [Discordu](https://aka.ms/ds4beginners/discord)
- Preglejte [CONTRIBUTING.md](CONTRIBUTING.md) za prijavo težav ali prispevanje

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.