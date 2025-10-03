<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:40:17+00:00",
  "source_file": "AGENTS.md",
  "language_code": "bg"
}
-->
# AGENTS.md

## Преглед на проекта

"Data Science for Beginners" е обширна 10-седмична учебна програма с 20 урока, създадена от Microsoft Azure Cloud Advocates. Репозиторият е учебен ресурс, който преподава основни концепции за анализ на данни чрез уроци, базирани на проекти, включително Jupyter notebooks, интерактивни тестове и практически задачи.

**Основни технологии:**
- **Jupyter Notebooks**: Основен учебен инструмент, използващ Python 3
- **Python библиотеки**: pandas, numpy, matplotlib за анализ и визуализация на данни
- **Vue.js 2**: Приложение за тестове (папка quiz-app)
- **Docsify**: Генератор на документация за офлайн достъп
- **Node.js/npm**: Управление на пакети за JavaScript компоненти
- **Markdown**: Цялото съдържание на уроците и документацията

**Архитектура:**
- Многоезичен образователен репозиторий с обширни преводи
- Структуриран в модули на уроци (1-Introduction до 6-Data-Science-In-Wild)
- Всеки урок включва README, notebooks, задачи и тестове
- Самостоятелно Vue.js приложение за тестове за предварителна/последваща оценка
- Поддръжка на GitHub Codespaces и VS Code dev containers

## Команди за настройка

### Настройка на репозитория
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Настройка на Python среда
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Настройка на приложението за тестове
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

### Docsify сървър за документация
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Настройка на проекти за визуализация
За проекти за визуализация като meaningful-visualizations (урок 13):
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


## Работен процес за разработка

### Работа с Jupyter Notebooks
1. Стартирайте Jupyter в корена на репозитория: `jupyter notebook`
2. Навигирайте до желаната папка с урока
3. Отворете `.ipynb` файлове, за да работите с упражненията
4. Notebook-ите са самостоятелни с обяснения и кодови клетки
5. Повечето notebook-и използват pandas, numpy и matplotlib - уверете се, че са инсталирани

### Структура на урока
Всеки урок обикновено съдържа:
- `README.md` - Основно съдържание на урока с теория и примери
- `notebook.ipynb` - Практически упражнения в Jupyter notebook
- `assignment.ipynb` или `assignment.md` - Практически задачи
- Папка `solution/` - Notebook-и с решения и код
- Папка `images/` - Поддържащи визуални материали

### Разработка на приложението за тестове
- Vue.js 2 приложение с hot-reload по време на разработка
- Тестовете се съхраняват в `quiz-app/src/assets/translations/`
- Всеки език има собствена папка за преводи (en, fr, es и др.)
- Номерацията на тестовете започва от 0 и достига до 39 (общо 40 теста)

### Добавяне на преводи
- Преводите се поставят в папката `translations/` в корена на репозитория
- Всеки език има пълна структура на урока, огледална на английската
- Автоматизиран превод чрез GitHub Actions (co-op-translator.yml)

## Инструкции за тестване

### Тестване на приложението за тестове
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Тестване на notebook-и
- Няма автоматизирана тестова рамка за notebook-и
- Ръчна проверка: Стартирайте всички клетки последователно, за да се уверите, че няма грешки
- Проверете дали файловете с данни са достъпни и дали изходите се генерират правилно
- Уверете се, че визуализациите се рендират правилно

### Тестване на документацията
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Проверки за качество на кода
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Насоки за стил на кода

### Python (Jupyter Notebooks)
- Следвайте насоките за стил PEP 8 за Python код
- Използвайте ясни имена на променливи, които обясняват анализираните данни
- Включвайте markdown клетки с обяснения преди кодовите клетки
- Дръжте кодовите клетки фокусирани върху единични концепции или операции
- Използвайте pandas за манипулация на данни, matplotlib за визуализация
- Общ модел за импортиране:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Следвайте насоките за стил на Vue.js 2 и най-добрите практики
- Конфигурация на ESLint в `quiz-app/package.json`
- Използвайте Vue компоненти с единични файлове (.vue файлове)
- Поддържайте архитектура, базирана на компоненти
- Стартирайте `npm run lint` преди да направите промени

### Markdown документация
- Използвайте ясна йерархия на заглавията (# ## ### и т.н.)
- Включвайте кодови блокове със спецификатори за език
- Добавяйте alt текст за изображения
- Линквайте към свързани уроци и ресурси
- Поддържайте разумна дължина на редовете за четимост

### Организация на файловете
- Съдържание на уроците в номерирани папки (01-defining-data-science и т.н.)
- Решения в специални под-папки `solution/`
- Преводите огледално на английската структура в папката `translations/`
- Съхранявайте файловете с данни в `data/` или специфични за урока папки

## Създаване и разгръщане

### Разгръщане на приложението за тестове
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Разгръщане на Azure Static Web Apps
Приложението quiz-app може да бъде разположено в Azure Static Web Apps:
1. Създайте ресурс Azure Static Web App
2. Свържете се с GitHub репозитория
3. Конфигурирайте настройките за изграждане:
   - Местоположение на приложението: `quiz-app`
   - Местоположение на изхода: `dist`
4. GitHub Actions workflow автоматично ще разположи при push

### Сайт за документация
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Репозиторият включва конфигурация за dev контейнер
- Codespaces автоматично настройва Python и Node.js среда
- Отворете репозитория в Codespace чрез GitHub UI
- Всички зависимости се инсталират автоматично

## Насоки за Pull Request

### Преди подаване
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Формат на заглавието на PR
- Използвайте ясни, описателни заглавия
- Формат: `[Компонент] Кратко описание`
- Примери:
  - `[Lesson 7] Fix Python notebook import error`
  - `[Quiz App] Add German translation`
  - `[Docs] Update README with new prerequisites`

### Задължителни проверки
- Уверете се, че целият код работи без грешки
- Проверете дали notebook-ите се изпълняват напълно
- Уверете се, че Vue.js приложенията се изграждат успешно
- Проверете дали връзките в документацията работят
- Тествайте приложението за тестове, ако е модифицирано
- Уверете се, че преводите поддържат консистентна структура

### Насоки за принос
- Следвайте съществуващия стил и модели на кода
- Добавяйте обяснителни коментари за сложна логика
- Актуализирайте съответната документация
- Тествайте промените в различни модули на уроците, ако е приложимо
- Прегледайте файла CONTRIBUTING.md

## Допълнителни бележки

### Използвани библиотеки
- **pandas**: Манипулация и анализ на данни
- **numpy**: Числови изчисления
- **matplotlib**: Визуализация и графики
- **seaborn**: Статистическа визуализация на данни (някои уроци)
- **scikit-learn**: Машинно обучение (напреднали уроци)

### Работа с файлове с данни
- Файловете с данни се намират в папката `data/` или специфични за урока директории
- Повечето notebook-и очакват файловете с данни в относителни пътища
- CSV файловете са основният формат на данните
- Някои уроци използват JSON за примери с нерелационни данни

### Многоезична поддръжка
- Над 40 езикови преводи чрез автоматизирани GitHub Actions
- Работен процес за превод в `.github/workflows/co-op-translator.yml`
- Преводи в папката `translations/` с езикови кодове
- Преводи на тестове в `quiz-app/src/assets/translations/`

### Опции за среда за разработка
1. **Локална разработка**: Инсталирайте Python, Jupyter, Node.js локално
2. **GitHub Codespaces**: Облачна среда за незабавна разработка
3. **VS Code Dev Containers**: Локална разработка, базирана на контейнери
4. **Binder**: Стартирайте notebook-и в облака (ако е конфигурирано)

### Насоки за съдържание на уроците
- Всеки урок е самостоятелен, но надгражда предишни концепции
- Предварителните тестове проверяват предварителни знания
- Последващите тестове укрепват наученото
- Задачите предоставят практически опит
- Sketchnotes предоставят визуални резюмета

### Отстраняване на често срещани проблеми

**Проблеми с Jupyter Kernel:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Проблеми с npm Install:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Грешки при импортиране в notebook-и:**
- Уверете се, че всички необходими библиотеки са инсталирани
- Проверете съвместимостта на версията на Python (препоръчва се Python 3.7+)
- Уверете се, че виртуалната среда е активирана

**Docsify не се зарежда:**
- Уверете се, че стартирате от корена на репозитория
- Проверете дали `index.html` съществува
- Уверете се за правилен мрежов достъп (порт 3000)

### Съображения за производителност
- Големите набори от данни може да отнемат време за зареждане в notebook-и
- Рендирането на визуализации може да бъде бавно за сложни графики
- Vue.js dev сървърът позволява бърза итерация чрез hot-reload
- Производствените билдове са оптимизирани и минимизирани

### Бележки за сигурност
- Не трябва да се качват чувствителни данни или идентификационни данни
- Използвайте променливи на средата за API ключове в уроци за облака
- Уроците, свързани с Azure, може да изискват идентификационни данни за акаунт в Azure
- Поддържайте зависимостите актуални за корекции на сигурността

## Принос към преводите
- Автоматизираните преводи се управляват чрез GitHub Actions
- Ръчни корекции са добре дошли за точност на преводите
- Следвайте съществуващата структура на папките за преводи
- Актуализирайте връзките към тестовете, за да включват езиков параметър: `?loc=fr`
- Тествайте преведените уроци за правилно рендиране

## Свързани ресурси
- Основна учебна програма: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Форум за дискусии: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Други учебни програми на Microsoft: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Поддръжка на проекта
- Редовни актуализации за поддържане на съдържанието актуално
- Добре дошли са приноси от общността
- Проблемите се проследяват в GitHub
- PR-ите се преглеждат от поддръжниците на учебната програма
- Месечни прегледи и актуализации на съдържанието

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.