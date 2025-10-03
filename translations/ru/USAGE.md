<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T14:52:49+00:00",
  "source_file": "USAGE.md",
  "language_code": "ru"
}
-->
# Руководство по использованию

Это руководство содержит примеры и распространенные рабочие процессы для использования учебной программы "Основы Data Science".

## Содержание

- [Как использовать эту учебную программу](../..)
- [Работа с уроками](../..)
- [Работа с Jupyter Notebooks](../..)
- [Использование приложения для викторин](../..)
- [Распространенные рабочие процессы](../..)
- [Советы для самостоятельного обучения](../..)
- [Советы для преподавателей](../..)

## Как использовать эту учебную программу

Эта учебная программа разработана с учетом гибкости и может использоваться различными способами:

- **Самостоятельное обучение**: Проходите уроки самостоятельно в удобном для вас темпе
- **Классное обучение**: Используйте как структурированный курс с руководством преподавателя
- **Учебные группы**: Учитесь совместно с коллегами
- **Формат воркшопа**: Интенсивные краткосрочные учебные сессии

## Работа с уроками

Каждый урок имеет последовательную структуру, чтобы максимально повысить эффективность обучения:

### Структура урока

1. **Предварительная викторина**: Проверьте свои текущие знания
2. **Скетчноут** (опционально): Визуальное резюме ключевых концепций
3. **Видео** (опционально): Дополнительный видеоматериал
4. **Письменный урок**: Основные концепции и объяснения
5. **Jupyter Notebook**: Практические упражнения по программированию
6. **Задание**: Практика изученного материала
7. **Итоговая викторина**: Закрепите свои знания

### Пример рабочего процесса для урока

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

### Запуск Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Выполнение ячеек в ноутбуке

1. **Выполнить ячейку**: Нажмите `Shift + Enter` или кнопку "Run"
2. **Выполнить все ячейки**: Выберите "Cell" → "Run All" в меню
3. **Перезапустить ядро**: Выберите "Kernel" → "Restart", если возникли проблемы

### Пример: Работа с данными в ноутбуке

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

### Сохранение работы

- Jupyter автоматически сохраняет данные периодически
- Сохранить вручную: Нажмите `Ctrl + S` (или `Cmd + S` на macOS)
- Ваш прогресс сохраняется в файле `.ipynb`

## Использование приложения для викторин

### Запуск приложения викторин локально

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Прохождение викторин

1. Предварительные викторины находятся в начале каждого урока
2. Итоговые викторины находятся в конце каждого урока
3. Каждая викторина содержит 3 вопроса
4. Викторины предназначены для закрепления материала, а не для исчерпывающего тестирования

### Нумерация викторин

- Викторины пронумерованы от 0 до 39 (всего 40 викторин)
- Каждый урок обычно включает предварительную и итоговую викторину
- URL викторин содержит номер викторины: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Распространенные рабочие процессы

### Рабочий процесс 1: Путь для абсолютных новичков

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

### Рабочий процесс 2: Изучение конкретной темы

Если вас интересует определенная тема:

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

### Рабочий процесс 3: Обучение на основе проектов

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Рабочий процесс 4: Облачный Data Science

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Советы для самостоятельного обучения

### Организованность

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Регулярная практика

- Выделяйте время каждый день или неделю
- Проходите хотя бы один урок в неделю
- Периодически пересматривайте предыдущие уроки

### Взаимодействие с сообществом

- Присоединяйтесь к [сообществу Discord](https://aka.ms/ds4beginners/discord)
- Участвуйте в канале #Data-Science-for-Beginners в Discord [Обсуждения в Discord](https://aka.ms/ds4beginners/discord)
- Делитесь своим прогрессом и задавайте вопросы

### Создавайте собственные проекты

После завершения уроков применяйте концепции в личных проектах:

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

## Советы для преподавателей

### Настройка класса

1. Ознакомьтесь с [for-teachers.md](for-teachers.md) для подробных рекомендаций
2. Настройте общую среду (GitHub Classroom или Codespaces)
3. Установите канал связи (Discord, Slack или Teams)

### Планирование уроков

**Рекомендуемый 10-недельный график:**

- **Недели 1-2**: Введение (Уроки 1-4)
- **Недели 3-4**: Работа с данными (Уроки 5-8)
- **Недели 5-6**: Визуализация данных (Уроки 9-13)
- **Недели 7-8**: Жизненный цикл Data Science (Уроки 14-16)
- **Неделя 9**: Облачный Data Science (Уроки 17-19)
- **Неделя 10**: Реальные приложения и финальные проекты (Урок 20)

### Запуск Docsify для офлайн-доступа

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Оценка заданий

- Проверяйте ноутбуки студентов на выполнение упражнений
- Оценивайте понимание через результаты викторин
- Оценивайте финальные проекты с использованием принципов жизненного цикла Data Science

### Создание заданий

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

### Загрузка ресурсов

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Локальный запуск документации

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Локальный запуск приложения викторин

```bash
cd quiz-app
npm run serve
```

## Доступ к переведенному контенту

Переводы доступны на более чем 40 языках:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Каждый перевод сохраняет ту же структуру, что и английская версия.

## Дополнительные ресурсы

### Продолжение обучения

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Дополнительные учебные пути
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Ресурсы для студентов
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Форум сообщества

### Связанные учебные программы

- [AI для начинающих](https://aka.ms/ai-beginners)
- [ML для начинающих](https://aka.ms/ml-beginners)
- [Веб-разработка для начинающих](https://aka.ms/webdev-beginners)
- [Генеративный AI для начинающих](https://aka.ms/genai-beginners)

## Получение помощи

- Ознакомьтесь с [TROUBLESHOOTING.md](TROUBLESHOOTING.md) для решения распространенных проблем
- Ищите ответы в [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Присоединяйтесь к нашему [Discord](https://aka.ms/ds4beginners/discord)
- Ознакомьтесь с [CONTRIBUTING.md](CONTRIBUTING.md), чтобы сообщить о проблемах или внести вклад

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность перевода, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.