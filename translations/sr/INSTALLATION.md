<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:25:59+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "sr"
}
-->
# Водич за инсталацију

Овај водич ће вам помоћи да подесите окружење за рад са наставним планом "Наука о подацима за почетнике".

## Садржај

- [Предуслови](../..)
- [Опције за брзи почетак](../..)
- [Локална инсталација](../..)
- [Провера инсталације](../..)

## Предуслови

Пре него што почнете, требало би да имате:

- Основно познавање командне линије/терминала
- GitHub налог (бесплатан)
- Стабилну интернет везу за почетно подешавање

## Опције за брзи почетак

### Опција 1: GitHub Codespaces (Препоручено за почетнике)

Најлакши начин за почетак је коришћење GitHub Codespaces, који пружа комплетно развојно окружење у вашем претраживачу.

1. Идите на [репозиторијум](https://github.com/microsoft/Data-Science-For-Beginners)
2. Кликните на падајући мени **Code**
3. Изаберите картицу **Codespaces**
4. Кликните на **Create codespace on main**
5. Сачекајте да се окружење иницијализује (2-3 минута)

Ваше окружење је сада спремно са свим унапред инсталираним зависностима!

### Опција 2: Локални развој

За рад на вашем рачунару, пратите детаљна упутства у наставку.

## Локална инсталација

### Корак 1: Инсталирајте Git

Git је потребан за клонирање репозиторијума и праћење ваших измена.

**Windows:**
- Преузмите са [git-scm.com](https://git-scm.com/download/win)
- Покрените инсталер са подразумеваним подешавањима

**macOS:**
- Инсталирајте преко Homebrew-а: `brew install git`
- Или преузмите са [git-scm.com](https://git-scm.com/download/mac)

**Linux:**
```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

### Корак 2: Клонирајте репозиторијум

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Корак 3: Инсталирајте Python и Jupyter

Python 3.7 или новији је потребан за лекције из науке о подацима.

**Windows:**
1. Преузмите Python са [python.org](https://www.python.org/downloads/)
2. Током инсталације, означите "Add Python to PATH"
3. Проверите инсталацију:
```bash
python --version
```

**macOS:**
```bash
# Using Homebrew
brew install python3

# Verify installation
python3 --version
```

**Linux:**
```bash
# Most Linux distributions come with Python pre-installed
python3 --version

# If not installed:
# Debian/Ubuntu
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

### Корак 4: Подесите Python окружење

Препоручује се коришћење виртуелног окружења за изолацију зависности.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Корак 5: Инсталирајте Python пакете

Инсталирајте потребне библиотеке за науку о подацима:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Корак 6: Инсталирајте Node.js и npm (за апликацију квиза)

Апликација за квиз захтева Node.js и npm.

**Windows/macOS:**
- Преузмите са [nodejs.org](https://nodejs.org/) (препоручује се LTS верзија)
- Покрените инсталер

**Linux:**
```bash
# Debian/Ubuntu
# WARNING: Piping scripts from the internet directly into bash can be a security risk.
# It is recommended to review the script before running it:
#   curl -fsSL https://deb.nodesource.com/setup_lts.x -o setup_lts.x
#   less setup_lts.x
# Then run:
#   sudo -E bash setup_lts.x
#
# Alternatively, you can use the one-liner below at your own risk:
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# Fedora
sudo dnf install nodejs

# Verify installation
node --version
npm --version
```

### Корак 7: Инсталирајте зависности за апликацију квиза

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Корак 8: Инсталирајте Docsify (опционо)

За офлајн приступ документацији:

```bash
npm install -g docsify-cli
```

## Провера инсталације

### Тестирајте Python и Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Ваш претраживач би требало да се отвори са Jupyter интерфејсом. Сада можете да приступите било којој `.ipynb` датотеци лекције.

### Тестирајте апликацију квиза

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Апликација за квиз би требало да буде доступна на `http://localhost:8080` (или другом порту ако је 8080 заузет).

### Тестирајте сервер документације

```bash
# From the root directory of the repository
docsify serve
```

Документација би требало да буде доступна на `http://localhost:3000`.

## Коришћење VS Code Dev Containers

Ако имате инсталиран Docker, можете користити VS Code Dev Containers:

1. Инсталирајте [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Инсталирајте [Visual Studio Code](https://code.visualstudio.com/)
3. Инсталирајте екстензију [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Отворите репозиторијум у VS Code-у
5. Притисните `F1` и изаберите "Remote-Containers: Reopen in Container"
6. Сачекајте да се контејнер изгради (само први пут)

## Следећи кораци

- Истражите [README.md](README.md) за преглед наставног плана
- Прочитајте [USAGE.md](USAGE.md) за уобичајене радне токове и примере
- Проверите [TROUBLESHOOTING.md](TROUBLESHOOTING.md) ако наиђете на проблеме
- Прегледајте [CONTRIBUTING.md](CONTRIBUTING.md) ако желите да допринесете

## Добијање помоћи

Ако наиђете на проблеме:

1. Проверите водич [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Претражите постојеће [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Придружите се нашој [Discord заједници](https://aka.ms/ds4beginners/discord)
4. Отворите нови проблем са детаљним информацијама о вашем проблему

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неспоразуме који могу произаћи из коришћења овог превода.