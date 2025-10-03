<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:10:18+00:00",
  "source_file": "USAGE.md",
  "language_code": "sr"
}
-->
# Водич за коришћење

Овај водич пружа примере и уобичајене радне токове за коришћење наставног програма „Наука о подацима за почетнике“.

## Садржај

- [Како користити овај наставни програм](../..)
- [Рад са лекцијама](../..)
- [Рад са Jupyter бележницама](../..)
- [Коришћење апликације за квиз](../..)
- [Уобичајени радни токови](../..)
- [Савети за самосталне ученике](../..)
- [Савети за наставнике](../..)

## Како користити овај наставни програм

Овај наставни програм је дизајниран да буде флексибилан и може се користити на више начина:

- **Самостално учење**: Радите кроз лекције независно, сопственим темпом
- **Настава у учионици**: Користите као структуриран курс са вођеним инструкцијама
- **Студијске групе**: Учење у сарадњи са вршњацима
- **Формат радионице**: Интензивне краткорочне сесије учења

## Рад са лекцијама

Свака лекција прати конзистентну структуру ради максималног учења:

### Структура лекције

1. **Квиз пре лекције**: Тестирајте своје постојеће знање
2. **Скетчнота** (опционо): Визуелни резиме кључних концепата
3. **Видео** (опционо): Допунски видео садржај
4. **Писана лекција**: Основни концепти и објашњења
5. **Jupyter бележница**: Практичне вежбе кодирања
6. **Задатак**: Вежбајте оно што сте научили
7. **Квиз после лекције**: Учврстите своје разумевање

### Пример радног тока за лекцију

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

## Рад са Jupyter бележницама

### Покретање Jupyter-а

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Покретање ћелија у бележници

1. **Извршите ћелију**: Притисните `Shift + Enter` или кликните на дугме „Run“
2. **Извршите све ћелије**: Изаберите „Cell“ → „Run All“ из менија
3. **Поновно покретање језгра**: Изаберите „Kernel“ → „Restart“ ако наиђете на проблеме

### Пример: Рад са подацима у бележници

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

### Чување вашег рада

- Jupyter периодично аутоматски чува
- Ручно чување: Притисните `Ctrl + S` (или `Cmd + S` на macOS-у)
- Ваш напредак се чува у `.ipynb` датотеци

## Коришћење апликације за квиз

### Покретање апликације за квиз локално

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Рад са квизовима

1. Квизови пре лекције су повезани на врху сваке лекције
2. Квизови после лекције су повезани на дну сваке лекције
3. Сваки квиз има 3 питања
4. Квизови су дизајнирани да учврсте учење, а не да исцрпно тестирају

### Нумерација квизова

- Квизови су нумерисани од 0-39 (укупно 40 квизова)
- Свака лекција обично има квиз пре и после
- URL-ови квизова укључују број квиза: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Уобичајени радни токови

### Радни ток 1: Пут за потпуне почетнике

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

### Радни ток 2: Учење специфичних тема

Ако вас занима одређена тема:

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

### Радни ток 3: Учење засновано на пројектима

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Радни ток 4: Наука о подацима у облаку

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Савети за самосталне ученике

### Будите организовани

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Редовно вежбајте

- Одвојите посебно време сваког дана или недеље
- Завршите бар једну лекцију недељно
- Периодично прегледајте претходне лекције

### Укључите се у заједницу

- Придружите се [Discord заједници](https://aka.ms/ds4beginners/discord)
- Учествујте у каналу #Data-Science-for-Beginners на Discord-у [Discord дискусије](https://aka.ms/ds4beginners/discord)
- Делите свој напредак и постављајте питања

### Направите сопствене пројекте

Након завршетка лекција, примените концепте на личне пројекте:

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

## Савети за наставнике

### Припрема учионице

1. Прегледајте [for-teachers.md](for-teachers.md) за детаљна упутства
2. Поставите заједничко окружење (GitHub Classroom или Codespaces)
3. Успоставите канал за комуникацију (Discord, Slack или Teams)

### Планирање лекција

**Предложени распоред за 10 недеља:**

- **Недеља 1-2**: Увод (Лекције 1-4)
- **Недеља 3-4**: Рад са подацима (Лекције 5-8)
- **Недеља 5-6**: Визуелизација података (Лекције 9-13)
- **Недеља 7-8**: Животни циклус науке о подацима (Лекције 14-16)
- **Недеља 9**: Наука о подацима у облаку (Лекције 17-19)
- **Недеља 10**: Примена у стварном свету и завршни пројекти (Лекција 20)

### Покретање Docsify-а за офлајн приступ

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Оцењивање задатака

- Прегледајте студентске бележнице за завршене вежбе
- Проверите разумевање кроз резултате квизова
- Оцените завршне пројекте користећи принципе животног циклуса науке о подацима

### Креирање задатака

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

## Рад офлајн

### Преузимање ресурса

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Локално покретање документације

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Локално покретање апликације за квиз

```bash
cd quiz-app
npm run serve
```

## Приступ преведеном садржају

Преводи су доступни на више од 40 језика:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Сваки превод задржава исту структуру као енглеска верзија.

## Додатни ресурси

### Наставите са учењем

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Додатни путеви учења
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Ресурси за студенте
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Форум заједнице

### Повезани наставни програми

- [AI за почетнике](https://aka.ms/ai-beginners)
- [ML за почетнике](https://aka.ms/ml-beginners)
- [Веб развој за почетнике](https://aka.ms/webdev-beginners)
- [Генеративна AI за почетнике](https://aka.ms/genai-beginners)

## Добијање помоћи

- Проверите [TROUBLESHOOTING.md](TROUBLESHOOTING.md) за уобичајене проблеме
- Претражите [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Придружите се нашем [Discord-у](https://aka.ms/ds4beginners/discord)
- Прегледајте [CONTRIBUTING.md](CONTRIBUTING.md) за пријаву проблема или допринос

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење уз помоћ вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу произаћи из коришћења овог превода.