<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-11T15:11:34+00:00",
  "source_file": "USAGE.md",
  "language_code": "et"
}
-->
# Kasutusjuhend

See juhend sisaldab näiteid ja tavapäraseid töövooge algajatele mõeldud andmeteaduse õppekava kasutamiseks.

## Sisukord

- [Kuidas seda õppekava kasutada](../..)
- [Töö tundidega](../..)
- [Töö Jupyter Notebookidega](../..)
- [Küsimustiku rakenduse kasutamine](../..)
- [Tavapärased töövood](../..)
- [Nõuanded iseseisvatele õppijatele](../..)
- [Nõuanded õpetajatele](../..)

## Kuidas seda õppekava kasutada

See õppekava on loodud paindlikuks ja seda saab kasutada mitmel viisil:

- **Iseseisev õppimine**: Töötage tundidega iseseisvalt omas tempos
- **Klassiõpe**: Kasutage struktureeritud kursusena juhendatud õpetusega
- **Õpperühmad**: Õppige koostöös kaaslastega
- **Töötoa formaat**: Intensiivsed lühiajalised õppesessioonid

## Töö tundidega

Iga tund järgib järjepidevat struktuuri, et maksimeerida õppimist:

### Tunni struktuur

1. **Eeltest**: Kontrollige oma olemasolevaid teadmisi
2. **Visuaalne kokkuvõte** (valikuline): Oluliste mõistete visuaalne kokkuvõte
3. **Video** (valikuline): Täiendav videomaterjal
4. **Kirjalik tund**: Põhimõisted ja selgitused
5. **Jupyter Notebook**: Praktilised kodeerimisharjutused
6. **Ülesanne**: Harjutage õpitut
7. **Järeltest**: Kinnistage oma arusaamist

### Näide tunni töövoost

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

## Töö Jupyter Notebookidega

### Jupyteri käivitamine

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Notebooki lahtrite käivitamine

1. **Lahtri käivitamine**: Vajutage `Shift + Enter` või klõpsake "Run" nuppu
2. **Kõigi lahtrite käivitamine**: Valige menüüst "Cell" → "Run All"
3. **Tuuma taaskäivitamine**: Valige "Kernel" → "Restart", kui tekib probleeme

### Näide: Andmetega töötamine Notebookis

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

### Oma töö salvestamine

- Jupyter salvestab automaatselt perioodiliselt
- Käsitsi salvestamine: Vajutage `Ctrl + S` (või `Cmd + S` macOS-is)
- Teie edusammud salvestatakse `.ipynb` faili

## Küsimustiku rakenduse kasutamine

### Küsimustiku rakenduse käivitamine kohapeal

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Küsimustike täitmine

1. Eeltestid on lingitud iga tunni alguses
2. Järeltestid on lingitud iga tunni lõpus
3. Igas testis on 3 küsimust
4. Testid on mõeldud õppimise kinnistamiseks, mitte põhjalikuks hindamiseks

### Küsimustike nummerdamine

- Küsimustikud on nummerdatud 0-39 (kokku 40 küsimustikku)
- Igal tunnil on tavaliselt eel- ja järeltest
- Küsimustiku URL-id sisaldavad küsimustiku numbrit: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Tavapärased töövood

### Töövoog 1: Algaja tee

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

### Töövoog 2: Teemaspetsiifiline õppimine

Kui olete huvitatud konkreetsest teemast:

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

### Töövoog 3: Projektipõhine õppimine

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Töövoog 4: Pilvepõhine andmeteadus

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Nõuanded iseseisvatele õppijatele

### Olge organiseeritud

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Harjutage regulaarselt

- Pühendage iga päev või nädal kindel aeg õppimisele
- Täitke vähemalt üks tund nädalas
- Korrake varasemaid tunde perioodiliselt

### Suhelge kogukonnaga

- Liituge [Discordi kogukonnaga](https://aka.ms/ds4beginners/discord)
- Osalege #Data-Science-for-Beginners kanalil Discordis [Discordi arutelud](https://aka.ms/ds4beginners/discord)
- Jagage oma edusamme ja esitage küsimusi

### Looge oma projektid

Pärast tundide läbimist rakendage mõisteid isiklikes projektides:

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

## Nõuanded õpetajatele

### Klassiruumi ettevalmistamine

1. Vaadake [for-teachers.md](for-teachers.md) üksikasjalike juhiste saamiseks
2. Seadistage jagatud keskkond (GitHub Classroom või Codespaces)
3. Looge suhtluskanal (Discord, Slack või Teams)

### Tunni planeerimine

**Soovitatav 10-nädalane ajakava:**

- **1.-2. nädal**: Sissejuhatus (tunnid 1-4)
- **3.-4. nädal**: Töö andmetega (tunnid 5-8)
- **5.-6. nädal**: Andmete visualiseerimine (tunnid 9-13)
- **7.-8. nädal**: Andmeteaduse elutsükkel (tunnid 14-16)
- **9. nädal**: Pilvepõhine andmeteadus (tunnid 17-19)
- **10. nädal**: Päriselu rakendused ja lõppprojektid (tund 20)

### Docsify käivitamine võrguühenduseta kasutamiseks

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Ülesannete hindamine

- Vaadake õpilaste notebooke, et kontrollida harjutuste täitmist
- Kontrollige arusaamist testide tulemuste kaudu
- Hinnake lõppprojekte andmeteaduse elutsükli põhimõtete alusel

### Ülesannete loomine

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

## Töö võrguühenduseta

### Ressursside allalaadimine

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Dokumentatsiooni käivitamine kohapeal

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Küsimustiku rakenduse käivitamine kohapeal

```bash
cd quiz-app
npm run serve
```

## Tõlgitud sisu kasutamine

Tõlked on saadaval enam kui 40 keeles:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Iga tõlge säilitab sama struktuuri nagu ingliskeelne versioon.

## Täiendavad ressursid

### Õppimise jätkamine

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Täiendavad õppeprogrammid
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Ressursid õpilastele
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Kogukonna foorum

### Seotud õppekavad

- [AI algajatele](https://aka.ms/ai-beginners)
- [ML algajatele](https://aka.ms/ml-beginners)
- [Veebiarendus algajatele](https://aka.ms/webdev-beginners)
- [Generatiivne AI algajatele](https://aka.ms/genai-beginners)

## Abi saamine

- Vaadake [TROUBLESHOOTING.md](TROUBLESHOOTING.md) levinud probleemide lahendamiseks
- Otsige [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Liituge meie [Discordiga](https://aka.ms/ds4beginners/discord)
- Vaadake [CONTRIBUTING.md](CONTRIBUTING.md), et raporteerida probleeme või panustada

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.