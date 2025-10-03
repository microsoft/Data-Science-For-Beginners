<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:01:41+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ru"
}
-->
# AGENTS.md

## Обзор проекта

"Data Science for Beginners" — это комплексная 10-недельная программа из 20 уроков, созданная командой Microsoft Azure Cloud Advocates. Этот репозиторий является учебным ресурсом, который обучает основам науки о данных через проектно-ориентированные уроки, включая Jupyter-ноутбуки, интерактивные викторины и практические задания.

**Ключевые технологии:**
- **Jupyter Notebooks**: Основной инструмент обучения с использованием Python 3
- **Библиотеки Python**: pandas, numpy, matplotlib для анализа и визуализации данных
- **Vue.js 2**: Приложение для викторин (папка quiz-app)
- **Docsify**: Генератор сайтов документации для оффлайн-доступа
- **Node.js/npm**: Управление пакетами для компонентов JavaScript
- **Markdown**: Весь контент уроков и документация

**Архитектура:**
- Многоязычный образовательный репозиторий с обширными переводами
- Структурирован в модули уроков (от 1-Introduction до 6-Data-Science-In-Wild)
- Каждый урок включает README, ноутбуки, задания и викторины
- Автономное приложение на Vue.js для оценки знаний до и после уроков
- Поддержка GitHub Codespaces и контейнеров разработки VS Code

## Команды для настройки

### Настройка репозитория
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Настройка среды Python
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Настройка приложения для викторин
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

### Сервер документации Docsify
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Настройка проектов визуализации
Для проектов визуализации, таких как meaningful-visualizations (урок 13):
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


## Рабочий процесс разработки

### Работа с Jupyter-ноутбуками
1. Запустите Jupyter в корне репозитория: `jupyter notebook`
2. Перейдите в папку с нужным уроком
3. Откройте файлы `.ipynb`, чтобы выполнить упражнения
4. Ноутбуки являются автономными и содержат объяснения и ячейки с кодом
5. Большинство ноутбуков используют pandas, numpy и matplotlib — убедитесь, что они установлены

### Структура урока
Каждый урок обычно включает:
- `README.md` — Основной контент урока с теорией и примерами
- `notebook.ipynb` — Практические упражнения в Jupyter-ноутбуке
- `assignment.ipynb` или `assignment.md` — Практические задания
- Папка `solution/` — Решения и код
- Папка `images/` — Вспомогательные визуальные материалы

### Разработка приложения для викторин
- Приложение на Vue.js 2 с функцией горячей перезагрузки во время разработки
- Викторины хранятся в `quiz-app/src/assets/translations/`
- Для каждого языка есть своя папка перевода (en, fr, es и т. д.)
- Нумерация викторин начинается с 0 и заканчивается на 39 (всего 40 викторин)

### Добавление переводов
- Переводы размещаются в папке `translations/` в корне репозитория
- Для каждого языка структура уроков полностью повторяет английскую
- Автоматический перевод через GitHub Actions (co-op-translator.yml)

## Инструкции по тестированию

### Тестирование приложения для викторин
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Тестирование ноутбуков
- Для ноутбуков нет автоматической системы тестирования
- Ручная проверка: выполните все ячейки по порядку, чтобы убедиться в отсутствии ошибок
- Убедитесь, что файлы данных доступны и результаты генерируются корректно
- Проверьте, что визуализации отображаются правильно

### Тестирование документации
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Проверка качества кода
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Руководство по стилю кода

### Python (Jupyter-ноутбуки)
- Следуйте рекомендациям стиля PEP 8 для кода на Python
- Используйте понятные имена переменных, объясняющие анализируемые данные
- Добавляйте ячейки Markdown с объяснениями перед ячейками с кодом
- Сосредотачивайте ячейки с кодом на одной концепции или операции
- Используйте pandas для обработки данных, matplotlib для визуализации
- Общий шаблон импорта:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Следуйте рекомендациям по стилю Vue.js 2 и лучшим практикам
- Конфигурация ESLint находится в `quiz-app/package.json`
- Используйте однофайловые компоненты Vue (.vue файлы)
- Поддерживайте архитектуру, основанную на компонентах
- Выполняйте `npm run lint` перед коммитом изменений

### Документация Markdown
- Используйте четкую иерархию заголовков (# ## ### и т. д.)
- Включайте блоки кода с указанием языка
- Добавляйте альтернативный текст для изображений
- Ссылайтесь на связанные уроки и ресурсы
- Соблюдайте разумную длину строк для удобства чтения

### Организация файлов
- Контент уроков в папках с номерами (01-defining-data-science и т. д.)
- Решения в выделенных подпапках `solution/`
- Переводы повторяют структуру английской версии в папке `translations/`
- Файлы данных хранятся в папке `data/` или в папках, связанных с уроками

## Сборка и развертывание

### Развертывание приложения для викторин
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Развертывание Azure Static Web Apps
Приложение quiz-app можно развернуть в Azure Static Web Apps:
1. Создайте ресурс Azure Static Web App
2. Подключите репозиторий GitHub
3. Настройте параметры сборки:
   - Расположение приложения: `quiz-app`
   - Расположение выходных данных: `dist`
4. GitHub Actions автоматически развернет приложение при каждом пуше

### Сайт документации
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Репозиторий включает конфигурацию контейнера разработки
- Codespaces автоматически настраивает среду Python и Node.js
- Откройте репозиторий в Codespace через интерфейс GitHub
- Все зависимости устанавливаются автоматически

## Руководство по Pull Request

### Перед отправкой
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Формат заголовка PR
- Используйте четкие, описательные заголовки
- Формат: `[Компонент] Краткое описание`
- Примеры:
  - `[Lesson 7] Исправление ошибки импорта в Python-ноутбуке`
  - `[Quiz App] Добавление перевода на немецкий`
  - `[Docs] Обновление README с новыми требованиями`

### Обязательные проверки
- Убедитесь, что весь код выполняется без ошибок
- Проверьте, что ноутбуки полностью выполняются
- Убедитесь, что приложения на Vue.js успешно собираются
- Проверьте работоспособность ссылок в документации
- Протестируйте приложение для викторин, если оно изменено
- Убедитесь, что переводы сохраняют согласованную структуру

### Руководство по внесению изменений
- Следуйте существующему стилю и шаблонам кода
- Добавляйте поясняющие комментарии для сложной логики
- Обновляйте соответствующую документацию
- Тестируйте изменения в разных модулях уроков, если это применимо
- Ознакомьтесь с файлом CONTRIBUTING.md

## Дополнительные заметки

### Используемые библиотеки
- **pandas**: Обработка и анализ данных
- **numpy**: Численные вычисления
- **matplotlib**: Визуализация и построение графиков
- **seaborn**: Статистическая визуализация данных (некоторые уроки)
- **scikit-learn**: Машинное обучение (продвинутые уроки)

### Работа с файлами данных
- Файлы данных находятся в папке `data/` или в папках, связанных с уроками
- Большинство ноутбуков ожидают файлы данных в относительных путях
- Основной формат данных — CSV
- Некоторые уроки используют JSON для примеров нереляционных данных

### Многоязычная поддержка
- Более 40 языков переведены с помощью автоматизации через GitHub Actions
- Рабочий процесс перевода описан в `.github/workflows/co-op-translator.yml`
- Переводы находятся в папке `translations/` с кодами языков
- Переводы викторин находятся в `quiz-app/src/assets/translations/`

### Варианты среды разработки
1. **Локальная разработка**: Установите Python, Jupyter, Node.js локально
2. **GitHub Codespaces**: Облачная мгновенная среда разработки
3. **Контейнеры разработки VS Code**: Локальная разработка на основе контейнеров
4. **Binder**: Запуск ноутбуков в облаке (если настроено)

### Руководство по контенту уроков
- Каждый урок автономен, но основывается на предыдущих концепциях
- Викторины перед уроком проверяют начальные знания
- Викторины после урока закрепляют материал
- Задания предоставляют практический опыт
- Скетчноуты дают визуальные резюме

### Устранение распространенных проблем

**Проблемы с ядром Jupyter:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Ошибки установки npm:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Ошибки импорта в ноутбуках:**
- Убедитесь, что все необходимые библиотеки установлены
- Проверьте совместимость версии Python (рекомендуется Python 3.7+)
- Убедитесь, что виртуальная среда активирована

**Docsify не загружается:**
- Убедитесь, что вы запускаете сервер из корня репозитория
- Проверьте наличие файла `index.html`
- Убедитесь в наличии сетевого доступа (порт 3000)

### Учет производительности
- Загрузка больших наборов данных в ноутбуках может занять время
- Отрисовка сложных графиков может быть медленной
- Сервер разработки Vue.js поддерживает горячую перезагрузку для быстрой итерации
- Продуктивные сборки оптимизированы и минимизированы

### Заметки по безопасности
- Не добавляйте конфиденциальные данные или учетные данные в репозиторий
- Используйте переменные окружения для любых ключей API в облачных уроках
- Уроки, связанные с Azure, могут требовать учетных данных Azure
- Обновляйте зависимости для устранения уязвимостей

## Участие в переводах
- Автоматические переводы управляются через GitHub Actions
- Ручные исправления приветствуются для повышения точности перевода
- Следуйте существующей структуре папок для переводов
- Обновляйте ссылки на викторины, добавляя параметр языка: `?loc=fr`
- Тестируйте переведенные уроки на корректность отображения

## Связанные ресурсы
- Основной курс: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Студенческий центр: https://docs.microsoft.com/learn/student-hub
- Форум обсуждений: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Другие курсы Microsoft: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Поддержка проекта
- Регулярные обновления для актуализации контента
- Приветствуются вклады сообщества
- Проблемы отслеживаются на GitHub
- PR проверяются кураторами курса
- Ежемесячные обзоры и обновления контента

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.