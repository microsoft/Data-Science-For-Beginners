<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:09:05+00:00",
  "source_file": "USAGE.md",
  "language_code": "sk"
}
-->
# Návod na použitie

Tento návod poskytuje príklady a bežné pracovné postupy na používanie učebných osnov Data Science for Beginners.

## Obsah

- [Ako používať tieto učebné osnovy](../..)
- [Práca s lekciami](../..)
- [Práca s Jupyter Notebooks](../..)
- [Používanie aplikácie na kvízy](../..)
- [Bežné pracovné postupy](../..)
- [Tipy pre samoukov](../..)
- [Tipy pre učiteľov](../..)

## Ako používať tieto učebné osnovy

Tieto učebné osnovy sú navrhnuté tak, aby boli flexibilné a mohli sa používať rôznymi spôsobmi:

- **Samostatné štúdium**: Prechádzajte lekcie nezávisle vlastným tempom
- **Výučba v triede**: Používajte ako štruktúrovaný kurz s vedenou výučbou
- **Študijné skupiny**: Učte sa spolu s kolegami
- **Workshopový formát**: Intenzívne krátkodobé vzdelávacie sedenia

## Práca s lekciami

Každá lekcia má konzistentnú štruktúru na maximalizáciu učenia:

### Štruktúra lekcie

1. **Kvíz pred lekciou**: Otestujte svoje existujúce znalosti
2. **Sketchnote** (voliteľné): Vizuálne zhrnutie kľúčových konceptov
3. **Video** (voliteľné): Doplnkový video obsah
4. **Písaná lekcia**: Základné koncepty a vysvetlenia
5. **Jupyter Notebook**: Praktické cvičenia v kódovaní
6. **Úloha**: Precvičte si, čo ste sa naučili
7. **Kvíz po lekcii**: Posilnite svoje porozumenie

### Príklad pracovného postupu pre lekciu

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

## Práca s Jupyter Notebooks

### Spustenie Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Spúšťanie buniek v notebooku

1. **Spustenie bunky**: Stlačte `Shift + Enter` alebo kliknite na tlačidlo "Run"
2. **Spustenie všetkých buniek**: Vyberte "Cell" → "Run All" z menu
3. **Reštartovanie jadra**: Vyberte "Kernel" → "Restart", ak narazíte na problémy

### Príklad: Práca s dátami v notebooku

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

### Ukladanie vašej práce

- Jupyter automaticky ukladá pravidelne
- Manuálne uloženie: Stlačte `Ctrl + S` (alebo `Cmd + S` na macOS)
- Váš pokrok sa uloží do súboru `.ipynb`

## Používanie aplikácie na kvízy

### Spustenie aplikácie na kvízy lokálne

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Riešenie kvízov

1. Kvízy pred lekciou sú uvedené na začiatku každej lekcie
2. Kvízy po lekcii sú uvedené na konci každej lekcie
3. Každý kvíz má 3 otázky
4. Kvízy sú navrhnuté na posilnenie učenia, nie na vyčerpávajúce testovanie

### Číslovanie kvízov

- Kvízy sú očíslované 0-39 (celkovo 40 kvízov)
- Každá lekcia má zvyčajne kvíz pred a po lekcii
- URL kvízov obsahujú číslo kvízu: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Bežné pracovné postupy

### Pracovný postup 1: Cesta úplného začiatočníka

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

### Pracovný postup 2: Učenie zamerané na konkrétnu tému

Ak vás zaujíma konkrétna téma:

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

### Pracovný postup 3: Učenie založené na projektoch

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Pracovný postup 4: Cloudová data science

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Tipy pre samoukov

### Zostaňte organizovaní

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Pravidelne cvičte

- Vyhraďte si každý deň alebo týždeň čas na učenie
- Dokončite aspoň jednu lekciu týždenne
- Pravidelne si opakujte predchádzajúce lekcie

### Zapojte sa do komunity

- Pripojte sa k [Discord komunite](https://aka.ms/ds4beginners/discord)
- Zúčastnite sa #Data-Science-for-Beginners kanála na Discorde [Diskusie na Discorde](https://aka.ms/ds4beginners/discord)
- Zdieľajte svoj pokrok a kladte otázky

### Vytvárajte vlastné projekty

Po dokončení lekcií aplikujte koncepty na osobné projekty:

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

## Tipy pre učiteľov

### Nastavenie triedy

1. Preštudujte si [for-teachers.md](for-teachers.md) pre podrobné pokyny
2. Nastavte zdieľané prostredie (GitHub Classroom alebo Codespaces)
3. Zriaďte komunikačný kanál (Discord, Slack alebo Teams)

### Plánovanie lekcií

**Navrhovaný 10-týždňový rozvrh:**

- **Týždeň 1-2**: Úvod (Lekcie 1-4)
- **Týždeň 3-4**: Práca s dátami (Lekcie 5-8)
- **Týždeň 5-6**: Vizualizácia dát (Lekcie 9-13)
- **Týždeň 7-8**: Životný cyklus data science (Lekcie 14-16)
- **Týždeň 9**: Cloudová data science (Lekcie 17-19)
- **Týždeň 10**: Reálne aplikácie a záverečné projekty (Lekcia 20)

### Spustenie Docsify pre offline prístup

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Hodnotenie úloh

- Skontrolujte študentské notebooky na dokončené cvičenia
- Overte porozumenie prostredníctvom výsledkov kvízov
- Hodnoťte záverečné projekty na základe princípov životného cyklu data science

### Vytváranie úloh

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

## Práca offline

### Stiahnutie zdrojov

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Spustenie dokumentácie lokálne

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Spustenie aplikácie na kvízy lokálne

```bash
cd quiz-app
npm run serve
```

## Prístup k preloženému obsahu

Preklady sú dostupné vo viac ako 40 jazykoch:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Každý preklad zachováva rovnakú štruktúru ako anglická verzia.

## Ďalšie zdroje

### Pokračujte v učení

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Ďalšie vzdelávacie cesty
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Zdroje pre študentov
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Komunitné fórum

### Súvisiace učebné osnovy

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## Získanie pomoci

- Skontrolujte [TROUBLESHOOTING.md](TROUBLESHOOTING.md) pre bežné problémy
- Vyhľadajte [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Pripojte sa k našemu [Discordu](https://aka.ms/ds4beginners/discord)
- Preštudujte si [CONTRIBUTING.md](CONTRIBUTING.md) na nahlásenie problémov alebo prispievanie

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.