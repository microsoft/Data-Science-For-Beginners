<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:45:38+00:00",
  "source_file": "AGENTS.md",
  "language_code": "uk"
}
-->
# AGENTS.md

## Огляд проєкту

Data Science for Beginners — це комплексна навчальна програма на 10 тижнів, що складається з 20 уроків, створена командою Microsoft Azure Cloud Advocates. Репозиторій є навчальним ресурсом, який викладає основні концепції науки про дані через проєктно-орієнтовані уроки, включаючи Jupyter ноутбуки, інтерактивні вікторини та практичні завдання.

**Основні технології:**
- **Jupyter Notebooks**: Основний навчальний інструмент з використанням Python 3
- **Бібліотеки Python**: pandas, numpy, matplotlib для аналізу даних та візуалізації
- **Vue.js 2**: Додаток для вікторин (папка quiz-app)
- **Docsify**: Генератор сайту документації для офлайн-доступу
- **Node.js/npm**: Управління пакетами для компонентів JavaScript
- **Markdown**: Весь контент уроків та документація

**Архітектура:**
- Багатомовний освітній репозиторій з широкими перекладами
- Структурований у модулі уроків (від 1-Introduction до 6-Data-Science-In-Wild)
- Кожен урок включає README, ноутбуки, завдання та вікторини
- Автономний додаток для вікторин на Vue.js для оцінювання до/після уроків
- Підтримка GitHub Codespaces та контейнерів розробки VS Code

## Команди налаштування

### Налаштування репозиторію
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Налаштування середовища Python
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Налаштування додатка для вікторин
```bash
# Navigate to quiz app
cd quiz-app

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint and fix files
npm run lint
```

### Сервер документації Docsify
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Налаштування проєктів візуалізації
Для проєктів візуалізації, таких як meaningful-visualizations (урок 13):
```bash
# Navigate to starter or solution folder
cd 3-Data-Visualization/13-meaningful-visualizations/starter

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint files
npm run lint
```


## Робочий процес розробки

### Робота з Jupyter ноутбуками
1. Запустіть Jupyter у корені репозиторію: `jupyter notebook`
2. Перейдіть до потрібної папки уроку
3. Відкрийте файли `.ipynb`, щоб виконувати вправи
4. Ноутбуки є самодостатніми з поясненнями та кодовими блоками
5. Більшість ноутбуків використовують pandas, numpy та matplotlib — переконайтеся, що вони встановлені

### Структура уроку
Кожен урок зазвичай містить:
- `README.md` - Основний контент уроку з теорією та прикладами
- `notebook.ipynb` - Практичні вправи в Jupyter ноутбуках
- `assignment.ipynb` або `assignment.md` - Практичні завдання
- Папка `solution/` - Ноутбуки з рішеннями та кодом
- Папка `images/` - Додаткові візуальні матеріали

### Розробка додатка для вікторин
- Додаток на Vue.js 2 з функцією гарячого перезавантаження під час розробки
- Вікторини зберігаються в `quiz-app/src/assets/translations/`
- Кожна мова має власну папку перекладів (en, fr, es тощо)
- Нумерація вікторин починається з 0 і доходить до 39 (всього 40 вікторин)

### Додавання перекладів
- Переклади розміщуються в папці `translations/` у корені репозиторію
- Кожна мова має повну структуру уроків, дзеркальну до англійської
- Автоматичний переклад через GitHub Actions (co-op-translator.yml)

## Інструкції з тестування

### Тестування додатка для вікторин
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Тестування ноутбуків
- Автоматизованої системи тестування для ноутбуків немає
- Ручна перевірка: Виконайте всі блоки коду послідовно, щоб переконатися у відсутності помилок
- Перевірте доступність файлів даних та правильність вихідних результатів
- Переконайтеся, що візуалізації відображаються правильно

### Тестування документації
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Перевірка якості коду
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Рекомендації щодо стилю коду

### Python (Jupyter ноутбуки)
- Дотримуйтесь стилю PEP 8 для Python коду
- Використовуйте зрозумілі назви змінних, які пояснюють аналізовані дані
- Додавайте markdown блоки з поясненнями перед кодовими блоками
- Зосереджуйте кодові блоки на окремих концепціях або операціях
- Використовуйте pandas для обробки даних, matplotlib для візуалізації
- Загальний шаблон імпорту:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Дотримуйтесь стилю та найкращих практик Vue.js 2
- Конфігурація ESLint у `quiz-app/package.json`
- Використовуйте однофайлові компоненти Vue (.vue файли)
- Підтримуйте архітектуру, засновану на компонентах
- Запустіть `npm run lint` перед внесенням змін

### Документація Markdown
- Використовуйте чітку ієрархію заголовків (# ## ### тощо)
- Додавайте блоки коду з вказівкою мови
- Додавайте альтернативний текст для зображень
- Посилайтеся на пов’язані уроки та ресурси
- Зберігайте розумну довжину рядків для зручності читання

### Організація файлів
- Контент уроків у пронумерованих папках (01-defining-data-science тощо)
- Рішення у спеціальних підпапках `solution/`
- Переклади дзеркалять структуру англійської у папці `translations/`
- Файли даних у папці `data/` або у папках, специфічних для уроків

## Збірка та розгортання

### Розгортання додатка для вікторин
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Розгортання Azure Static Web Apps
Додаток quiz-app можна розгорнути на Azure Static Web Apps:
1. Створіть ресурс Azure Static Web App
2. Підключіть до репозиторію GitHub
3. Налаштуйте параметри збірки:
   - Розташування додатка: `quiz-app`
   - Розташування вихідних даних: `dist`
4. GitHub Actions автоматично розгорне при пуші

### Сайт документації
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Репозиторій включає конфігурацію контейнера розробки
- Codespaces автоматично налаштовує середовище Python та Node.js
- Відкрийте репозиторій у Codespace через інтерфейс GitHub
- Усі залежності встановлюються автоматично

## Рекомендації щодо Pull Request

### Перед поданням
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Формат заголовка PR
- Використовуйте чіткі, описові заголовки
- Формат: `[Компонент] Короткий опис`
- Приклади:
  - `[Lesson 7] Виправлення помилки імпорту в Python ноутбуці`
  - `[Quiz App] Додано переклад німецькою`
  - `[Docs] Оновлено README з новими вимогами`

### Обов’язкові перевірки
- Переконайтеся, що весь код виконується без помилок
- Перевірте повне виконання ноутбуків
- Переконайтеся, що додатки Vue.js успішно збираються
- Перевірте, чи працюють посилання в документації
- Тестуйте додаток для вікторин, якщо він змінений
- Переконайтеся, що переклади зберігають послідовну структуру

### Рекомендації щодо внесків
- Дотримуйтесь існуючого стилю та шаблонів коду
- Додавайте пояснювальні коментарі для складної логіки
- Оновлюйте відповідну документацію
- Тестуйте зміни в різних модулях уроків, якщо це можливо
- Ознайомтеся з файлом CONTRIBUTING.md

## Додаткові примітки

### Використовувані бібліотеки
- **pandas**: Обробка та аналіз даних
- **numpy**: Числові обчислення
- **matplotlib**: Візуалізація даних та побудова графіків
- **seaborn**: Статистична візуалізація даних (деякі уроки)
- **scikit-learn**: Машинне навчання (просунуті уроки)

### Робота з файлами даних
- Файли даних розташовані в папці `data/` або у папках, специфічних для уроків
- Більшість ноутбуків очікують файли даних у відносних шляхах
- Основний формат даних — CSV
- Деякі уроки використовують JSON для прикладів нереляційних даних

### Підтримка багатомовності
- 40+ мовних перекладів через автоматизовані GitHub Actions
- Робочий процес перекладу в `.github/workflows/co-op-translator.yml`
- Переклади в папці `translations/` з кодами мов
- Переклади вікторин у `quiz-app/src/assets/translations/`

### Варіанти середовища розробки
1. **Локальна розробка**: Встановіть Python, Jupyter, Node.js локально
2. **GitHub Codespaces**: Хмарне миттєве середовище розробки
3. **VS Code Dev Containers**: Локальна розробка на основі контейнерів
4. **Binder**: Запуск ноутбуків у хмарі (якщо налаштовано)

### Рекомендації щодо контенту уроків
- Кожен урок є самостійним, але базується на попередніх концепціях
- Вікторини перед уроком перевіряють попередні знання
- Вікторини після уроку закріплюють навчання
- Завдання забезпечують практичне застосування
- Скетчноти надають візуальні резюме

### Вирішення поширених проблем

**Проблеми з ядром Jupyter:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Помилки встановлення npm:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Помилки імпорту в ноутбуках:**
- Переконайтеся, що всі необхідні бібліотеки встановлені
- Перевірте сумісність версії Python (рекомендується Python 3.7+)
- Переконайтеся, що віртуальне середовище активоване

**Docsify не завантажується:**
- Переконайтеся, що ви запускаєте сервер з кореня репозиторію
- Перевірте наявність файлу `index.html`
- Переконайтеся у правильному доступі до мережі (порт 3000)

### Міркування щодо продуктивності
- Великі набори даних можуть займати час для завантаження в ноутбуках
- Візуалізація може бути повільною для складних графіків
- Сервер розробки Vue.js забезпечує гаряче перезавантаження для швидкої ітерації
- Виробничі збірки оптимізовані та мінімізовані

### Примітки щодо безпеки
- Не слід зберігати конфіденційні дані або облікові дані в репозиторії
- Використовуйте змінні середовища для будь-яких ключів API у хмарних уроках
- Уроки, пов’язані з Azure, можуть вимагати облікових даних облікового запису Azure
- Оновлюйте залежності для усунення вразливостей

## Внесок у переклади
- Автоматизовані переклади керуються через GitHub Actions
- Вітаються ручні виправлення для точності перекладу
- Дотримуйтесь існуючої структури папок перекладу
- Оновлюйте посилання на вікторини, додаючи параметр мови: `?loc=fr`
- Тестуйте перекладені уроки на правильність відображення

## Пов’язані ресурси
- Основна навчальна програма: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Студентський центр: https://docs.microsoft.com/learn/student-hub
- Форум обговорень: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Інші навчальні програми Microsoft: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Підтримка проєкту
- Регулярні оновлення для актуалізації контенту
- Вітаються внески від спільноти
- Проблеми відстежуються на GitHub
- PR перевіряються кураторами навчальної програми
- Щомісячні огляди та оновлення контенту

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.