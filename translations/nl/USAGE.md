<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:05:36+00:00",
  "source_file": "USAGE.md",
  "language_code": "nl"
}
-->
# Gebruikershandleiding

Deze handleiding biedt voorbeelden en veelvoorkomende workflows voor het gebruik van het curriculum Data Science voor Beginners.

## Inhoudsopgave

- [Hoe gebruik je dit curriculum](../..)
- [Werken met lessen](../..)
- [Werken met Jupyter Notebooks](../..)
- [De quizapplicatie gebruiken](../..)
- [Veelvoorkomende workflows](../..)
- [Tips voor zelfstudie](../..)
- [Tips voor docenten](../..)

## Hoe gebruik je dit curriculum

Dit curriculum is ontworpen om flexibel te zijn en kan op verschillende manieren worden gebruikt:

- **Zelfstudie**: Werk zelfstandig door de lessen in je eigen tempo
- **Klassikale instructie**: Gebruik het als een gestructureerde cursus met begeleide instructie
- **Studiegroepen**: Leer samen met anderen
- **Workshopformaat**: Intensieve kortetermijn leersessies

## Werken met lessen

Elke les volgt een consistente structuur om het leren te maximaliseren:

### Lesstructuur

1. **Pre-les quiz**: Test je bestaande kennis
2. **Sketchnote** (Optioneel): Visuele samenvatting van belangrijke concepten
3. **Video** (Optioneel): Aanvullende videocontent
4. **Geschreven les**: Kernconcepten en uitleg
5. **Jupyter Notebook**: Praktische codeeropdrachten
6. **Opdracht**: Oefen wat je hebt geleerd
7. **Post-les quiz**: Versterk je begrip

### Voorbeeldworkflow voor een les

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

## Werken met Jupyter Notebooks

### Jupyter starten

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Notebookcellen uitvoeren

1. **Voer een cel uit**: Druk op `Shift + Enter` of klik op de knop "Run"
2. **Voer alle cellen uit**: Selecteer "Cell" → "Run All" in het menu
3. **Kernel herstarten**: Selecteer "Kernel" → "Restart" als je problemen ondervindt

### Voorbeeld: Werken met data in een notebook

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

### Je werk opslaan

- Jupyter slaat automatisch periodiek op
- Handmatig opslaan: Druk op `Ctrl + S` (of `Cmd + S` op macOS)
- Je voortgang wordt opgeslagen in het `.ipynb`-bestand

## De quizapplicatie gebruiken

### De quizapp lokaal uitvoeren

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Quizzen maken

1. Pre-les quizzen staan bovenaan elke les
2. Post-les quizzen staan onderaan elke les
3. Elke quiz bevat 3 vragen
4. Quizzen zijn bedoeld om het leren te versterken, niet om uitgebreid te testen

### Quiznummering

- Quizzen zijn genummerd van 0-39 (40 quizzen in totaal)
- Elke les heeft meestal een pre- en post-quiz
- Quiz-URL's bevatten het quiznummer: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Veelvoorkomende workflows

### Workflow 1: Pad voor complete beginners

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

### Workflow 2: Specifiek leren per onderwerp

Als je geïnteresseerd bent in een specifiek onderwerp:

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

### Workflow 3: Projectgebaseerd leren

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Workflow 4: Cloud-gebaseerde data science

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Tips voor zelfstudie

### Blijf georganiseerd

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Oefen regelmatig

- Reserveer elke dag of week tijd om te leren
- Voltooi minstens één les per week
- Herhaal eerdere lessen regelmatig

### Betrek jezelf bij de community

- Word lid van de [Discord-community](https://aka.ms/ds4beginners/discord)
- Doe mee in het #Data-Science-for-Beginners-kanaal op Discord [Discord Discussies](https://aka.ms/ds4beginners/discord)
- Deel je voortgang en stel vragen

### Bouw je eigen projecten

Pas na het voltooien van lessen de concepten toe op persoonlijke projecten:

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

## Tips voor docenten

### Klassikale opzet

1. Bekijk [for-teachers.md](for-teachers.md) voor gedetailleerde richtlijnen
2. Stel een gedeelde omgeving in (GitHub Classroom of Codespaces)
3. Creëer een communicatiekanaal (Discord, Slack of Teams)

### Lesplanning

**Voorgesteld 10-weken schema:**

- **Week 1-2**: Introductie (Lessen 1-4)
- **Week 3-4**: Werken met data (Lessen 5-8)
- **Week 5-6**: Datavisualisatie (Lessen 9-13)
- **Week 7-8**: Data Science Lifecycle (Lessen 14-16)
- **Week 9**: Cloud Data Science (Lessen 17-19)
- **Week 10**: Toepassingen in de praktijk & eindprojecten (Les 20)

### Docsify offline uitvoeren

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Opdrachten beoordelen

- Controleer studentnotebooks op voltooide oefeningen
- Controleer begrip via quizscores
- Beoordeel eindprojecten aan de hand van principes van de data science lifecycle

### Opdrachten maken

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

## Offline werken

### Bronnen downloaden

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Documentatie lokaal uitvoeren

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Quizapp lokaal uitvoeren

```bash
cd quiz-app
npm run serve
```

## Toegang tot vertaalde content

Vertalingen zijn beschikbaar in meer dan 40 talen:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Elke vertaling behoudt dezelfde structuur als de Engelse versie.

## Aanvullende bronnen

### Verder leren

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Aanvullende leerpaden
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Bronnen voor studenten
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Communityforum

### Gerelateerde curricula

- [AI voor Beginners](https://aka.ms/ai-beginners)
- [ML voor Beginners](https://aka.ms/ml-beginners)
- [Webontwikkeling voor Beginners](https://aka.ms/webdev-beginners)
- [Generatieve AI voor Beginners](https://aka.ms/genai-beginners)

## Hulp krijgen

- Bekijk [TROUBLESHOOTING.md](TROUBLESHOOTING.md) voor veelvoorkomende problemen
- Zoek in [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Word lid van onze [Discord](https://aka.ms/ds4beginners/discord)
- Bekijk [CONTRIBUTING.md](CONTRIBUTING.md) om problemen te melden of bij te dragen

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.