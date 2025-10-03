<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:41:29+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sr"
}
-->
# AGENTS.md

## Преглед пројекта

Наука о подацима за почетнике је свеобухватан наставни план и програм од 10 недеља и 20 лекција који је креирао тим Microsoft Azure Cloud Advocates. Репозиторијум је ресурс за учење који кроз лекције засноване на пројектима подучава основне концепте науке о подацима, укључујући Jupyter бележнице, интерактивне квизове и практичне задатке.

**Кључне технологије:**
- **Jupyter бележнице**: Примарни медијум за учење уз коришћење Python 3
- **Python библиотеке**: pandas, numpy, matplotlib за анализу и визуализацију података
- **Vue.js 2**: Апликација за квизове (папка quiz-app)
- **Docsify**: Генератор сајтова за документацију за офлајн приступ
- **Node.js/npm**: Управљање пакетима за JavaScript компоненте
- **Markdown**: Садржај лекција и документација

**Архитектура:**
- Образовни репозиторијум на више језика са обимним преводима
- Структурисан у модуле лекција (1-Introduction до 6-Data-Science-In-Wild)
- Свака лекција укључује README, бележнице, задатке и квизове
- Самостална Vue.js апликација за квизове за процену пре/после лекције
- Подршка за GitHub Codespaces и VS Code dev контейнере

## Команде за подешавање

### Подешавање репозиторијума
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Подешавање Python окружења
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Подешавање апликације за квизове
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

### Docsify сервер за документацију
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Подешавање пројеката за визуализацију
За пројекте визуализације као што је meaningful-visualizations (лекција 13):
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


## Радни ток развоја

### Рад са Jupyter бележницама
1. Покрените Jupyter у корену репозиторијума: `jupyter notebook`
2. Навигирајте до жељене папке лекције
3. Отворите `.ipynb` датотеке за рад на вежбама
4. Бележнице су самосталне са објашњењима и кодним ћелијама
5. Већина бележница користи pandas, numpy и matplotlib - уверите се да су инсталирани

### Структура лекције
Свака лекција обично садржи:
- `README.md` - Главни садржај лекције са теоријом и примерима
- `notebook.ipynb` - Практичне вежбе у Jupyter бележници
- `assignment.ipynb` или `assignment.md` - Задаци за вежбање
- `solution/` папка - Бележнице са решењима и код
- `images/` папка - Подршка за визуелне материјале

### Развој апликације за квизове
- Vue.js 2 апликација са hot-reload током развоја
- Квизови се чувају у `quiz-app/src/assets/translations/`
- Сваки језик има своју папку за преводе (en, fr, es, итд.)
- Нумерација квизова почиње од 0 и иде до 39 (укупно 40 квизова)

### Додавање превода
- Преводи се додају у `translations/` папку у корену репозиторијума
- Сваки језик има комплетну структуру лекција као у енглеском
- Аутоматски превод преко GitHub Actions (co-op-translator.yml)

## Упутства за тестирање

### Тестирање апликације за квизове
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Тестирање бележница
- Не постоји аутоматски тест оквир за бележнице
- Ручна провера: Покрените све ћелије редом да бисте се уверили да нема грешака
- Проверите да ли су датотеке са подацима доступне и да ли се излаз правилно генерише
- Проверите да ли се визуализације правилно приказују

### Тестирање документације
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Провере квалитета кода
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Упутства за стил кода

### Python (Jupyter бележнице)
- Придржавајте се PEP 8 смерница за стил Python кода
- Користите јасна имена променљивих која објашњавају податке који се анализирају
- Укључите markdown ћелије са објашњењима пре кодних ћелија
- Држите кодне ћелије фокусиране на један концепт или операцију
- Користите pandas за манипулацију подацима, matplotlib за визуализацију
- Уобичајени образац за увоз:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Придржавајте се Vue.js 2 смерница за стил и најбољих пракси
- ESLint конфигурација у `quiz-app/package.json`
- Користите Vue компоненте у једној датотеци (.vue датотеке)
- Одржавајте архитектуру засновану на компонентама
- Покрените `npm run lint` пре него што пошаљете измене

### Markdown документација
- Користите јасну хијерархију наслова (# ## ### итд.)
- Укључите блокове кода са спецификацијом језика
- Додајте alt текст за слике
- Линкујте повезане лекције и ресурсе
- Држите дужину линија разумном ради читљивости

### Организација датотека
- Садржај лекција у нумерисаним папкама (01-defining-data-science, итд.)
- Решења у посебним `solution/` подфолдерима
- Преводи огледају структуру енглеског у `translations/` папци
- Датотеке са подацима чувајте у `data/` или специфичним папкама лекција

## Изградња и распоређивање

### Распоређивање апликације за квизове
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Распоређивање Azure Static Web Apps
Апликација за квизове може се распоредити на Azure Static Web Apps:
1. Креирајте Azure Static Web App ресурс
2. Повежите се са GitHub репозиторијумом
3. Конфигуришите подешавања изградње:
   - Локација апликације: `quiz-app`
   - Локација излаза: `dist`
4. GitHub Actions workflow ће аутоматски распоредити на push

### Сајт за документацију
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Репозиторијум укључује конфигурацију dev контейнера
- Codespaces аутоматски подешава Python и Node.js окружење
- Отворите репозиторијум у Codespace преко GitHub UI
- Све зависности се аутоматски инсталирају

## Упутства за Pull Request

### Пре слања
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Формат наслова PR-а
- Користите јасне, описне наслове
- Формат: `[Компонента] Кратак опис`
- Примери:
  - `[Лекција 7] Поправка грешке увоза у Python бележници`
  - `[Апликација за квизове] Додавање немачког превода`
  - `[Документација] Ажурирање README са новим предусловима`

### Потребне провере
- Уверите се да се сав код извршава без грешака
- Проверите да бележнице извршавају потпуно
- Потврдите да се Vue.js апликације успешно граде
- Проверите да линкови у документацији раде
- Тестирајте апликацију за квизове ако је модификована
- Проверите да преводи одржавају конзистентну структуру

### Смернице за допринос
- Придржавајте се постојећег стила и образаца кода
- Додајте објашњавајуће коментаре за сложену логику
- Ажурирајте релевантну документацију
- Тестирајте измене у различитим модулима лекција ако је применљиво
- Прегледајте датотеку CONTRIBUTING.md

## Додатне напомене

### Уобичајене коришћене библиотеке
- **pandas**: Манипулација и анализа података
- **numpy**: Нумеричко рачунање
- **matplotlib**: Визуелизација и графикони података
- **seaborn**: Статистичка визуализација података (неке лекције)
- **scikit-learn**: Машинско учење (напредне лекције)

### Рад са датотекама података
- Датотеке са подацима се налазе у `data/` папци или специфичним директоријумима лекција
- Већина бележница очекује датотеке са подацима у релативним путевима
- CSV датотеке су примарни формат података
- Неке лекције користе JSON за примере нерелационих података

### Подршка за више језика
- Преводи на 40+ језика преко аутоматских GitHub Actions
- Радни ток превода у `.github/workflows/co-op-translator.yml`
- Преводи у `translations/` папци са кодовима језика
- Преводи квизова у `quiz-app/src/assets/translations/`

### Опције развојног окружења
1. **Локални развој**: Инсталирајте Python, Jupyter, Node.js локално
2. **GitHub Codespaces**: Cloud-based instant развојно окружење
3. **VS Code Dev Containers**: Локално окружење засновано на контейнерима
4. **Binder**: Покрените бележнице у облаку (ако је конфигурисано)

### Смернице за садржај лекција
- Свака лекција је самостална, али се надовезује на претходне концепте
- Квизови пре лекције тестирају претходно знање
- Квизови после лекције учвршћују научено
- Задаци пружају практично искуство
- Sketchnotes пружају визуелне резимеје

### Решавање уобичајених проблема

**Проблеми са Jupyter кернелом:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Неуспех инсталације npm:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Грешке увоза у бележницама:**
- Проверите да ли су све потребне библиотеке инсталиране
- Проверите компатибилност верзије Python-а (препоручује се Python 3.7+)
- Уверите се да је виртуелно окружење активирано

**Docsify се не учитава:**
- Проверите да ли служите из корена репозиторијума
- Проверите да ли `index.html` постоји
- Уверите се да је омогућен правилан приступ мрежи (порт 3000)

### Напомене о перформансама
- Велики скупови података могу захтевати време за учитавање у бележницама
- Приказивање визуализација може бити споро за сложене графиконе
- Vue.js dev сервер омогућава hot-reload за брзу итерацију
- Производне верзије су оптимизоване и минимизиране

### Напомене о безбедности
- Не би требало да се чувају осетљиви подаци или акредитиви
- Користите променљиве окружења за било које API кључеве у лекцијама о облаку
- Лекције повезане са Azure-ом могу захтевати акредитиве Azure налога
- Одржавајте зависности ажурним ради безбедносних закрпа

## Допринос преводима
- Аутоматски преводи управљани преко GitHub Actions
- Ручне исправке су добродошле ради тачности превода
- Придржавајте се постојеће структуре папки за преводе
- Ажурирајте линкове за квизове да укључе параметар језика: `?loc=fr`
- Тестирајте преведене лекције ради правилног приказивања

## Повезани ресурси
- Главни наставни план: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Форум за дискусију: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Други наставни планови Microsoft-а: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Одржавање пројекта
- Редовна ажурирања ради одржавања актуелности садржаја
- Доприноси заједнице су добродошли
- Проблеми се прате на GitHub-у
- PR-ове прегледају одржаваоци наставног плана
- Месечни прегледи и ажурирања садржаја

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.