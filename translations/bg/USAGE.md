<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:09:52+00:00",
  "source_file": "USAGE.md",
  "language_code": "bg"
}
-->
# Ръководство за използване

Това ръководство предоставя примери и често срещани работни процеси за използване на учебната програма "Наука за данни за начинаещи".

## Съдържание

- [Как да използвате тази учебна програма](../..)
- [Работа с уроци](../..)
- [Работа с Jupyter Notebooks](../..)
- [Използване на приложението за тестове](../..)
- [Често срещани работни процеси](../..)
- [Съвети за самостоятелно обучение](../..)
- [Съвети за преподаватели](../..)

## Как да използвате тази учебна програма

Тази учебна програма е проектирана да бъде гъвкава и може да се използва по различни начини:

- **Самостоятелно обучение**: Работете през уроците независимо със собствено темпо
- **Класна стая**: Използвайте като структурирана програма с насочено обучение
- **Учебни групи**: Учете съвместно с колеги
- **Формат на работилница**: Интензивни краткосрочни учебни сесии

## Работа с уроци

Всеки урок следва последователна структура за максимално усвояване:

### Структура на урока

1. **Тест преди урока**: Проверете съществуващите си знания
2. **Скетчбележка** (по избор): Визуално обобщение на ключовите концепции
3. **Видео** (по избор): Допълнително видео съдържание
4. **Писмен урок**: Основни концепции и обяснения
5. **Jupyter Notebook**: Практически упражнения с код
6. **Задание**: Практикувайте наученото
7. **Тест след урока**: Затвърдете разбирането си

### Примерен работен процес за урок

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

## Работа с Jupyter Notebooks

### Стартиране на Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Изпълнение на клетки в Notebook

1. **Изпълнение на клетка**: Натиснете `Shift + Enter` или кликнете върху бутона "Run"
2. **Изпълнение на всички клетки**: Изберете "Cell" → "Run All" от менюто
3. **Рестартиране на ядрото**: Изберете "Kernel" → "Restart", ако срещнете проблеми

### Пример: Работа с данни в Notebook

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

### Запазване на работата ви

- Jupyter автоматично запазва периодично
- Ръчно запазване: Натиснете `Ctrl + S` (или `Cmd + S` на macOS)
- Напредъкът ви се запазва в `.ipynb` файл

## Използване на приложението за тестове

### Стартиране на приложението за тестове локално

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Попълване на тестове

1. Тестовете преди урока са свързани в началото на всеки урок
2. Тестовете след урока са свързани в края на всеки урок
3. Всеки тест съдържа 3 въпроса
4. Тестовете са предназначени да затвърдят наученото, а не да тестват изчерпателно

### Номериране на тестовете

- Тестовете са номерирани от 0 до 39 (общо 40 теста)
- Всеки урок обикновено има тест преди и след урока
- URL адресите на тестовете включват номера на теста: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Често срещани работни процеси

### Работен процес 1: Път за напълно начинаещи

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

### Работен процес 2: Обучение по конкретна тема

Ако се интересувате от конкретна тема:

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

### Работен процес 3: Обучение чрез проекти

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Работен процес 4: Наука за данни в облака

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Съвети за самостоятелно обучение

### Бъдете организирани

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Практикувайте редовно

- Отделяйте време всеки ден или седмица
- Завършвайте поне един урок седмично
- Преглеждайте предишни уроци периодично

### Включете се в общността

- Присъединете се към [Discord общността](https://aka.ms/ds4beginners/discord)
- Участвайте в канала #Data-Science-for-Beginners в Discord [Discord Discussions](https://aka.ms/ds4beginners/discord)
- Споделяйте напредъка си и задавайте въпроси

### Създавайте собствени проекти

След като завършите уроците, приложете концепциите в лични проекти:

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

## Съвети за преподаватели

### Настройка на класната стая

1. Прегледайте [for-teachers.md](for-teachers.md) за подробни указания
2. Настройте споделена среда (GitHub Classroom или Codespaces)
3. Създайте канал за комуникация (Discord, Slack или Teams)

### Планиране на уроци

**Предложен 10-седмичен график:**

- **Седмица 1-2**: Въведение (Уроци 1-4)
- **Седмица 3-4**: Работа с данни (Уроци 5-8)
- **Седмица 5-6**: Визуализация на данни (Уроци 9-13)
- **Седмица 7-8**: Жизнен цикъл на науката за данни (Уроци 14-16)
- **Седмица 9**: Наука за данни в облака (Уроци 17-19)
- **Седмица 10**: Приложения в реалния свят и финални проекти (Урок 20)

### Стартиране на Docsify за офлайн достъп

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Оценяване на задания

- Преглеждайте студентските notebooks за завършени упражнения
- Проверявайте разбирането чрез резултати от тестове
- Оценявайте финалните проекти, използвайки принципите на жизнения цикъл на науката за данни

### Създаване на задания

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

## Работа офлайн

### Изтегляне на ресурси

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Стартиране на документация локално

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Стартиране на приложението за тестове локално

```bash
cd quiz-app
npm run serve
```

## Достъп до преведено съдържание

Преводите са налични на над 40 езика:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Всеки превод запазва същата структура като английската версия.

## Допълнителни ресурси

### Продължете обучението

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Допълнителни учебни пътеки
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Ресурси за студенти
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Форум на общността

### Свързани учебни програми

- [AI за начинаещи](https://aka.ms/ai-beginners)
- [ML за начинаещи](https://aka.ms/ml-beginners)
- [Уеб разработка за начинаещи](https://aka.ms/webdev-beginners)
- [Генеративен AI за начинаещи](https://aka.ms/genai-beginners)

## Получаване на помощ

- Прегледайте [TROUBLESHOOTING.md](TROUBLESHOOTING.md) за често срещани проблеми
- Търсете в [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Присъединете се към нашия [Discord](https://aka.ms/ds4beginners/discord)
- Прегледайте [CONTRIBUTING.md](CONTRIBUTING.md), за да докладвате проблеми или да допринесете

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.