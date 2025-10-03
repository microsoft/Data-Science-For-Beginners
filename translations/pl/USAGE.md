<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:02:00+00:00",
  "source_file": "USAGE.md",
  "language_code": "pl"
}
-->
# Przewodnik użytkowania

Ten przewodnik zawiera przykłady i typowe procesy pracy związane z korzystaniem z programu nauczania "Data Science for Beginners".

## Spis treści

- [Jak korzystać z tego programu nauczania](../..)
- [Praca z lekcjami](../..)
- [Praca z Jupyter Notebooks](../..)
- [Korzystanie z aplikacji quizowej](../..)
- [Typowe procesy pracy](../..)
- [Wskazówki dla samouków](../..)
- [Wskazówki dla nauczycieli](../..)

## Jak korzystać z tego programu nauczania

Ten program nauczania został zaprojektowany tak, aby był elastyczny i można go używać na różne sposoby:

- **Nauka we własnym tempie**: Pracuj nad lekcjami samodzielnie, w swoim własnym tempie
- **Instrukcja w klasie**: Używaj jako strukturalnego kursu z prowadzeniem nauczyciela
- **Grupy studenckie**: Ucz się wspólnie z rówieśnikami
- **Format warsztatowy**: Intensywne sesje nauki w krótkim czasie

## Praca z lekcjami

Każda lekcja ma spójną strukturę, aby maksymalizować efektywność nauki:

### Struktura lekcji

1. **Quiz przed lekcją**: Sprawdź swoją dotychczasową wiedzę
2. **Sketchnote** (Opcjonalne): Wizualne podsumowanie kluczowych pojęć
3. **Wideo** (Opcjonalne): Dodatkowe materiały wideo
4. **Lekcja pisemna**: Podstawowe pojęcia i wyjaśnienia
5. **Jupyter Notebook**: Ćwiczenia praktyczne z kodowaniem
6. **Zadanie**: Praktyka zdobytej wiedzy
7. **Quiz po lekcji**: Utrwal swoją wiedzę

### Przykładowy proces pracy z lekcją

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

## Praca z Jupyter Notebooks

### Uruchamianie Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Uruchamianie komórek w notebooku

1. **Uruchom komórkę**: Naciśnij `Shift + Enter` lub kliknij przycisk "Run"
2. **Uruchom wszystkie komórki**: Wybierz "Cell" → "Run All" z menu
3. **Restartuj kernel**: Wybierz "Kernel" → "Restart", jeśli napotkasz problemy

### Przykład: Praca z danymi w notebooku

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

### Zapisywanie pracy

- Jupyter automatycznie zapisuje co jakiś czas
- Ręczne zapisywanie: Naciśnij `Ctrl + S` (lub `Cmd + S` na macOS)
- Twój postęp jest zapisywany w pliku `.ipynb`

## Korzystanie z aplikacji quizowej

### Uruchamianie aplikacji quizowej lokalnie

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Rozwiązywanie quizów

1. Quizy przed lekcją są podlinkowane na początku każdej lekcji
2. Quizy po lekcji są podlinkowane na końcu każdej lekcji
3. Każdy quiz zawiera 3 pytania
4. Quizy mają na celu utrwalenie wiedzy, a nie wyczerpujące testowanie

### Numeracja quizów

- Quizy są numerowane od 0 do 39 (łącznie 40 quizów)
- Każda lekcja zazwyczaj ma quiz przed i po lekcji
- URL quizów zawiera numer quizu: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Typowe procesy pracy

### Proces 1: Ścieżka dla zupełnie początkujących

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

### Proces 2: Nauka tematyczna

Jeśli interesuje Cię konkretny temat:

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

### Proces 3: Nauka oparta na projektach

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Proces 4: Data Science w chmurze

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Wskazówki dla samouków

### Organizacja pracy

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Regularna praktyka

- Przeznacz dedykowany czas każdego dnia lub tygodnia
- Ukończ co najmniej jedną lekcję tygodniowo
- Okresowo przeglądaj wcześniejsze lekcje

### Zaangażowanie w społeczność

- Dołącz do [społeczności Discord](https://aka.ms/ds4beginners/discord)
- Uczestnicz w kanale #Data-Science-for-Beginners na Discord [Dyskusje na Discord](https://aka.ms/ds4beginners/discord)
- Dziel się postępami i zadawaj pytania

### Tworzenie własnych projektów

Po ukończeniu lekcji zastosuj zdobyte pojęcia w projektach osobistych:

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

## Wskazówki dla nauczycieli

### Przygotowanie klasy

1. Przejrzyj [for-teachers.md](for-teachers.md) dla szczegółowych wskazówek
2. Skonfiguruj wspólne środowisko (GitHub Classroom lub Codespaces)
3. Ustal kanał komunikacji (Discord, Slack lub Teams)

### Planowanie lekcji

**Proponowany harmonogram 10-tygodniowy:**

- **Tydzień 1-2**: Wprowadzenie (Lekcje 1-4)
- **Tydzień 3-4**: Praca z danymi (Lekcje 5-8)
- **Tydzień 5-6**: Wizualizacja danych (Lekcje 9-13)
- **Tydzień 7-8**: Cykl życia Data Science (Lekcje 14-16)
- **Tydzień 9**: Data Science w chmurze (Lekcje 17-19)
- **Tydzień 10**: Zastosowania w rzeczywistości i projekty końcowe (Lekcja 20)

### Uruchamianie Docsify dla dostępu offline

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Ocena zadań

- Przeglądaj notatniki uczniów pod kątem ukończonych ćwiczeń
- Sprawdzaj zrozumienie na podstawie wyników quizów
- Oceniaj projekty końcowe, stosując zasady cyklu życia Data Science

### Tworzenie zadań

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

## Praca offline

### Pobieranie zasobów

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Uruchamianie dokumentacji lokalnie

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Uruchamianie aplikacji quizowej lokalnie

```bash
cd quiz-app
npm run serve
```

## Dostęp do przetłumaczonej treści

Tłumaczenia są dostępne w ponad 40 językach:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Każde tłumaczenie zachowuje tę samą strukturę co wersja angielska.

## Dodatkowe zasoby

### Kontynuacja nauki

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Dodatkowe ścieżki nauki
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Zasoby dla studentów
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Forum społecznościowe

### Powiązane programy nauczania

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## Uzyskiwanie pomocy

- Sprawdź [TROUBLESHOOTING.md](TROUBLESHOOTING.md) dla typowych problemów
- Przeszukaj [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Dołącz do naszego [Discord](https://aka.ms/ds4beginners/discord)
- Przejrzyj [CONTRIBUTING.md](CONTRIBUTING.md), aby zgłaszać problemy lub wnosić wkład

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.