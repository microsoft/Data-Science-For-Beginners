<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:12:33+00:00",
  "source_file": "USAGE.md",
  "language_code": "uk"
}
-->
# Посібник з використання

Цей посібник надає приклади та поширені робочі процеси для використання навчальної програми "Data Science for Beginners".

## Зміст

- [Як використовувати цю навчальну програму](../..)
- [Робота з уроками](../..)
- [Робота з Jupyter Notebooks](../..)
- [Використання додатку для тестів](../..)
- [Поширені робочі процеси](../..)
- [Поради для самостійного навчання](../..)
- [Поради для викладачів](../..)

## Як використовувати цю навчальну програму

Ця навчальна програма розроблена для гнучкого використання і може бути застосована різними способами:

- **Самостійне навчання**: Проходьте уроки самостійно у зручному для вас темпі
- **Класне навчання**: Використовуйте як структурований курс із керованим навчанням
- **Навчальні групи**: Вчіться разом із колегами
- **Формат воркшопу**: Інтенсивні короткострокові навчальні сесії

## Робота з уроками

Кожен урок має послідовну структуру для максимального засвоєння матеріалу:

### Структура уроку

1. **Попередній тест**: Перевірте свої початкові знання
2. **Скетчноут** (опціонально): Візуальний підсумок ключових концепцій
3. **Відео** (опціонально): Додатковий відеоконтент
4. **Письмовий урок**: Основні концепції та пояснення
5. **Jupyter Notebook**: Практичні вправи з програмування
6. **Завдання**: Закріпіть вивчене
7. **Підсумковий тест**: Підтвердьте своє розуміння

### Приклад робочого процесу для уроку

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

## Робота з Jupyter Notebooks

### Запуск Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Виконання комірок у ноутбуці

1. **Виконати комірку**: Натисніть `Shift + Enter` або кнопку "Run"
2. **Виконати всі комірки**: Оберіть "Cell" → "Run All" у меню
3. **Перезапустити ядро**: Оберіть "Kernel" → "Restart", якщо виникають проблеми

### Приклад: Робота з даними у ноутбуці

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

### Збереження роботи

- Jupyter автоматично зберігає прогрес періодично
- Ручне збереження: Натисніть `Ctrl + S` (або `Cmd + S` на macOS)
- Ваш прогрес зберігається у файлі `.ipynb`

## Використання додатку для тестів

### Запуск додатку для тестів локально

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Проходження тестів

1. Попередні тести доступні на початку кожного уроку
2. Підсумкові тести доступні в кінці кожного уроку
3. Кожен тест містить 3 питання
4. Тести створені для закріплення знань, а не для вичерпного оцінювання

### Нумерація тестів

- Тести пронумеровані від 0 до 39 (усього 40 тестів)
- Кожен урок зазвичай має попередній і підсумковий тест
- URL тестів включає номер тесту: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Поширені робочі процеси

### Робочий процес 1: Шлях для повного новачка

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

### Робочий процес 2: Вивчення конкретної теми

Якщо вас цікавить конкретна тема:

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

### Робочий процес 3: Навчання на основі проєктів

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Робочий процес 4: Хмарна наука про дані

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Поради для самостійного навчання

### Будьте організованими

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Практикуйтеся регулярно

- Виділяйте час щодня або щотижня
- Завершуйте принаймні один урок на тиждень
- Періодично переглядайте попередні уроки

### Взаємодійте зі спільнотою

- Приєднуйтесь до [спільноти Discord](https://aka.ms/ds4beginners/discord)
- Беріть участь у каналі #Data-Science-for-Beginners у Discord [Обговорення в Discord](https://aka.ms/ds4beginners/discord)
- Діліться своїм прогресом і ставте запитання

### Створюйте власні проєкти

Після завершення уроків застосовуйте концепції у власних проєктах:

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

## Поради для викладачів

### Налаштування класу

1. Ознайомтеся з [for-teachers.md](for-teachers.md) для детальних інструкцій
2. Налаштуйте спільне середовище (GitHub Classroom або Codespaces)
3. Встановіть канал зв’язку (Discord, Slack або Teams)

### Планування уроків

**Рекомендований 10-тижневий графік:**

- **Тиждень 1-2**: Вступ (Уроки 1-4)
- **Тиждень 3-4**: Робота з даними (Уроки 5-8)
- **Тиждень 5-6**: Візуалізація даних (Уроки 9-13)
- **Тиждень 7-8**: Життєвий цикл науки про дані (Уроки 14-16)
- **Тиждень 9**: Хмарна наука про дані (Уроки 17-19)
- **Тиждень 10**: Реальні застосування та фінальні проєкти (Урок 20)

### Запуск Docsify для офлайн-доступу

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Оцінювання завдань

- Перевіряйте ноутбуки студентів на виконані вправи
- Оцінюйте розуміння за результатами тестів
- Оцінюйте фінальні проєкти за принципами життєвого циклу науки про дані

### Створення завдань

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

## Робота офлайн

### Завантаження ресурсів

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Локальний запуск документації

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Локальний запуск додатку для тестів

```bash
cd quiz-app
npm run serve
```

## Доступ до перекладеного контенту

Переклади доступні більш ніж 40 мовами:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Кожен переклад зберігає ту саму структуру, що й англійська версія.

## Додаткові ресурси

### Продовжуйте навчання

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Додаткові навчальні шляхи
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Ресурси для студентів
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Форум спільноти

### Схожі навчальні програми

- [AI for Beginners](https://aka.ms/ai-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [Generative AI for Beginners](https://aka.ms/genai-beginners)

## Отримання допомоги

- Перегляньте [TROUBLESHOOTING.md](TROUBLESHOOTING.md) для вирішення поширених проблем
- Шукайте [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Приєднуйтесь до нашого [Discord](https://aka.ms/ds4beginners/discord)
- Ознайомтеся з [CONTRIBUTING.md](CONTRIBUTING.md), щоб повідомити про проблеми або зробити внесок

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, зверніть увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.