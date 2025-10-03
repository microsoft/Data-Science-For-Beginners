<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:08:16+00:00",
  "source_file": "USAGE.md",
  "language_code": "hu"
}
-->
# Használati útmutató

Ez az útmutató példákat és gyakori munkafolyamatokat mutat be a "Data Science for Beginners" tananyag használatához.

## Tartalomjegyzék

- [Hogyan használd ezt a tananyagot](../..)
- [Munka a leckékkel](../..)
- [Munka Jupyter Notebookokkal](../..)
- [A kvíz alkalmazás használata](../..)
- [Gyakori munkafolyamatok](../..)
- [Tippek önálló tanulóknak](../..)
- [Tippek tanároknak](../..)

## Hogyan használd ezt a tananyagot

Ez a tananyag rugalmasan használható, többféle módon:

- **Önálló tanulás**: Haladj végig a leckéken saját tempódban
- **Osztálytermi oktatás**: Strukturált kurzusként, irányított oktatással
- **Tanulócsoportok**: Tanulj együtt társaiddal
- **Workshop formátum**: Intenzív, rövid távú tanulási szekciók

## Munka a leckékkel

Minden lecke következetes struktúrát követ a hatékony tanulás érdekében:

### Lecke felépítése

1. **Előzetes kvíz**: Teszteld meglévő tudásodat
2. **Sketchnote** (Opcionális): Kulcsfogalmak vizuális összefoglalója
3. **Videó** (Opcionális): Kiegészítő videós tartalom
4. **Írott lecke**: Alapfogalmak és magyarázatok
5. **Jupyter Notebook**: Gyakorlati kódolási feladatok
6. **Feladat**: Gyakorold, amit tanultál
7. **Utólagos kvíz**: Erősítsd meg a megértésedet

### Példa egy lecke munkafolyamatára

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

## Munka Jupyter Notebookokkal

### Jupyter indítása

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Notebook cellák futtatása

1. **Cellák futtatása**: Nyomd meg a `Shift + Enter` billentyűt, vagy kattints a "Run" gombra
2. **Összes cella futtatása**: Válaszd ki a "Cell" → "Run All" menüpontot
3. **Kernel újraindítása**: Válaszd ki a "Kernel" → "Restart" opciót, ha problémákba ütközöl

### Példa: Adatok kezelése egy Notebookban

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

### Munkád mentése

- A Jupyter időszakosan automatikusan ment
- Kézi mentés: Nyomd meg a `Ctrl + S` (vagy `Cmd + S` macOS-en)
- Az előrehaladásod a `.ipynb` fájlban kerül mentésre

## A kvíz alkalmazás használata

### Kvíz alkalmazás futtatása helyben

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Kvízek kitöltése

1. Az előzetes kvízek a leckék elején találhatók
2. Az utólagos kvízek a leckék végén találhatók
3. Minden kvíz 3 kérdést tartalmaz
4. A kvízek célja a tanulás megerősítése, nem kimerítő tesztelés

### Kvíz számozása

- A kvízek 0-39-ig vannak számozva (összesen 40 kvíz)
- Minden lecke általában tartalmaz előzetes és utólagos kvízt
- A kvíz URL-ek tartalmazzák a kvíz számát: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Gyakori munkafolyamatok

### Munkafolyamat 1: Teljes kezdő útvonal

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

### Munkafolyamat 2: Téma-specifikus tanulás

Ha egy adott téma érdekel:

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

### Munkafolyamat 3: Projekt-alapú tanulás

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Munkafolyamat 4: Felhő-alapú adatkutatás

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Tippek önálló tanulóknak

### Maradj szervezett

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Gyakorolj rendszeresen

- Szánj rá dedikált időt minden nap vagy héten
- Fejezz be legalább egy leckét hetente
- Időnként ismételd át a korábbi leckéket

### Kapcsolódj a közösséghez

- Csatlakozz a [Discord közösséghez](https://aka.ms/ds4beginners/discord)
- Vegyél részt a #Data-Science-for-Beginners csatornán a Discordon [Discord Discussions](https://aka.ms/ds4beginners/discord)
- Oszd meg előrehaladásodat és tegyél fel kérdéseket

### Készíts saját projekteket

A leckék befejezése után alkalmazd a tanultakat saját projektjeidben:

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

## Tippek tanároknak

### Osztálytermi beállítás

1. Tekintsd át a [for-teachers.md](for-teachers.md) fájlt részletes útmutatásért
2. Állíts be egy megosztott környezetet (GitHub Classroom vagy Codespaces)
3. Hozz létre egy kommunikációs csatornát (Discord, Slack vagy Teams)

### Lecke tervezés

**Javasolt 10 hetes ütemterv:**

- **1-2. hét**: Bevezetés (1-4. lecke)
- **3-4. hét**: Adatok kezelése (5-8. lecke)
- **5-6. hét**: Adatvizualizáció (9-13. lecke)
- **7-8. hét**: Adattudomány életciklusa (14-16. lecke)
- **9. hét**: Felhő-alapú adattudomány (17-19. lecke)
- **10. hét**: Valós alkalmazások és záró projektek (20. lecke)

### Docsify futtatása offline hozzáféréshez

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Feladatok értékelése

- Ellenőrizd a diákok notebookjait a befejezett gyakorlatokért
- Vizsgáld meg a megértést a kvíz eredmények alapján
- Értékeld a záró projekteket az adattudomány életciklusának elvei szerint

### Feladatok létrehozása

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

## Offline munka

### Erőforrások letöltése

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Dokumentáció futtatása helyben

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Kvíz alkalmazás futtatása helyben

```bash
cd quiz-app
npm run serve
```

## Fordított tartalom elérése

A fordítások több mint 40 nyelven elérhetők:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Minden fordítás megtartja az angol verzió struktúráját.

## További erőforrások

### Továbbtanulás

- [Microsoft Learn](https://docs.microsoft.com/learn/) - További tanulási útvonalak
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Erőforrások diákoknak
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Közösségi fórum

### Kapcsolódó tananyagok

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## Segítség kérése

- Nézd meg a [TROUBLESHOOTING.md](TROUBLESHOOTING.md) fájlt a gyakori problémákért
- Keress a [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) között
- Csatlakozz a [Discordhoz](https://aka.ms/ds4beginners/discord)
- Tekintsd át a [CONTRIBUTING.md](CONTRIBUTING.md) fájlt, hogy hibát jelents vagy hozzájárulj

---

**Felelősség kizárása**:  
Ezt a dokumentumot az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével fordították le. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.