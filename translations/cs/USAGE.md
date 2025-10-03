<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:08:40+00:00",
  "source_file": "USAGE.md",
  "language_code": "cs"
}
-->
# Průvodce použitím

Tento průvodce poskytuje příklady a běžné pracovní postupy pro použití kurikula Data Science for Beginners.

## Obsah

- [Jak používat toto kurikulum](../..)
- [Práce s lekcemi](../..)
- [Práce s Jupyter Notebooks](../..)
- [Použití aplikace pro kvízy](../..)
- [Běžné pracovní postupy](../..)
- [Tipy pro samouky](../..)
- [Tipy pro učitele](../..)

## Jak používat toto kurikulum

Toto kurikulum je navrženo tak, aby bylo flexibilní a mohlo být použito různými způsoby:

- **Samostudium**: Procházejte lekce nezávisle vlastním tempem
- **Výuka ve třídě**: Použijte jako strukturovaný kurz s vedenou výukou
- **Studijní skupiny**: Učte se společně s kolegy
- **Workshopový formát**: Intenzivní krátkodobé vzdělávací sezení

## Práce s lekcemi

Každá lekce má konzistentní strukturu, která maximalizuje učení:

### Struktura lekce

1. **Kvíz před lekcí**: Otestujte své stávající znalosti
2. **Sketchnote** (volitelné): Vizuální shrnutí klíčových konceptů
3. **Video** (volitelné): Doplňkový video obsah
4. **Psaná lekce**: Základní koncepty a vysvětlení
5. **Jupyter Notebook**: Praktická cvičení v kódování
6. **Úkol**: Procvičte si, co jste se naučili
7. **Kvíz po lekci**: Posilte své porozumění

### Příklad pracovního postupu pro lekci

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

## Práce s Jupyter Notebooks

### Spuštění Jupyteru

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Spouštění buněk v notebooku

1. **Spuštění buňky**: Stiskněte `Shift + Enter` nebo klikněte na tlačítko "Run"
2. **Spuštění všech buněk**: Vyberte "Cell" → "Run All" v menu
3. **Restartování kernelu**: Vyberte "Kernel" → "Restart", pokud narazíte na problémy

### Příklad: Práce s daty v notebooku

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

### Ukládání práce

- Jupyter automaticky ukládá pravidelně
- Ruční uložení: Stiskněte `Ctrl + S` (nebo `Cmd + S` na macOS)
- Váš pokrok je uložen v souboru `.ipynb`

## Použití aplikace pro kvízy

### Spuštění aplikace pro kvízy lokálně

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Absolvování kvízů

1. Kvízy před lekcí jsou uvedeny na začátku každé lekce
2. Kvízy po lekci jsou uvedeny na konci každé lekce
3. Každý kvíz obsahuje 3 otázky
4. Kvízy jsou navrženy tak, aby posilovaly učení, nikoli aby vyčerpávajícím způsobem testovaly

### Číslování kvízů

- Kvízy jsou očíslovány 0-39 (celkem 40 kvízů)
- Každá lekce obvykle obsahuje kvíz před a po lekci
- URL kvízů obsahují číslo kvízu: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Běžné pracovní postupy

### Pracovní postup 1: Cesta pro úplné začátečníky

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

### Pracovní postup 2: Učení zaměřené na konkrétní téma

Pokud vás zajímá konkrétní téma:

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

### Pracovní postup 3: Učení založené na projektech

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Pracovní postup 4: Data Science v cloudu

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Tipy pro samouky

### Zůstaňte organizovaní

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Pravidelně procvičujte

- Vyhraďte si každý den nebo týden čas na učení
- Dokončete alespoň jednu lekci týdně
- Pravidelně si opakujte předchozí lekce

### Zapojte se do komunity

- Připojte se k [Discord komunitě](https://aka.ms/ds4beginners/discord)
- Účastněte se kanálu #Data-Science-for-Beginners na Discordu [Diskuze na Discordu](https://aka.ms/ds4beginners/discord)
- Sdílejte svůj pokrok a kladte otázky

### Vytvářejte vlastní projekty

Po dokončení lekcí aplikujte koncepty na osobní projekty:

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

## Tipy pro učitele

### Nastavení třídy

1. Projděte si [for-teachers.md](for-teachers.md) pro podrobné pokyny
2. Nastavte sdílené prostředí (GitHub Classroom nebo Codespaces)
3. Zaveďte komunikační kanál (Discord, Slack nebo Teams)

### Plánování lekcí

**Navrhovaný 10týdenní rozvrh:**

- **Týden 1-2**: Úvod (Lekce 1-4)
- **Týden 3-4**: Práce s daty (Lekce 5-8)
- **Týden 5-6**: Vizualizace dat (Lekce 9-13)
- **Týden 7-8**: Životní cyklus Data Science (Lekce 14-16)
- **Týden 9**: Data Science v cloudu (Lekce 17-19)
- **Týden 10**: Reálné aplikace & závěrečné projekty (Lekce 20)

### Spuštění Docsify pro offline přístup

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Hodnocení úkolů

- Projděte studentské notebooky s dokončenými cvičeními
- Ověřte porozumění pomocí výsledků kvízů
- Hodnoťte závěrečné projekty podle principů životního cyklu Data Science

### Vytváření úkolů

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

## Práce offline

### Stažení zdrojů

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Spuštění dokumentace lokálně

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Spuštění aplikace pro kvízy lokálně

```bash
cd quiz-app
npm run serve
```

## Přístup k přeloženému obsahu

Překlady jsou dostupné ve více než 40 jazycích:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Každý překlad zachovává stejnou strukturu jako anglická verze.

## Další zdroje

### Pokračujte v učení

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Další vzdělávací cesty
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Zdroje pro studenty
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Komunitní fórum

### Související kurikula

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## Získání pomoci

- Projděte si [TROUBLESHOOTING.md](TROUBLESHOOTING.md) pro běžné problémy
- Vyhledejte [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Připojte se k našemu [Discordu](https://aka.ms/ds4beginners/discord)
- Projděte si [CONTRIBUTING.md](CONTRIBUTING.md) pro hlášení problémů nebo přispění

---

**Upozornění**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme zodpovědní za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.