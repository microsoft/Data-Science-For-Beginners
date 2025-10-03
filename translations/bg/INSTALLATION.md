<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:25:40+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "bg"
}
-->
# Ръководство за инсталация

Това ръководство ще ви помогне да настроите вашата среда за работа с учебната програма "Наука за данни за начинаещи".

## Съдържание

- [Предварителни изисквания](../..)
- [Опции за бърз старт](../..)
- [Локална инсталация](../..)
- [Проверка на инсталацията](../..)

## Предварителни изисквания

Преди да започнете, трябва да имате:

- Основни познания за командния ред/терминала
- Акаунт в GitHub (безплатен)
- Стабилна интернет връзка за първоначалната настройка

## Опции за бърз старт

### Опция 1: GitHub Codespaces (Препоръчва се за начинаещи)

Най-лесният начин да започнете е с GitHub Codespaces, който предоставя пълна среда за разработка директно в браузъра.

1. Отидете на [репозиторията](https://github.com/microsoft/Data-Science-For-Beginners)
2. Кликнете върху падащото меню **Code**
3. Изберете таба **Codespaces**
4. Кликнете върху **Create codespace on main**
5. Изчакайте средата да се инициализира (2-3 минути)

Вашата среда вече е готова с всички предварително инсталирани зависимости!

### Опция 2: Локална разработка

За работа на вашия собствен компютър, следвайте подробните инструкции по-долу.

## Локална инсталация

### Стъпка 1: Инсталирайте Git

Git е необходим за клониране на репозиторията и проследяване на вашите промени.

**Windows:**
- Изтеглете от [git-scm.com](https://git-scm.com/download/win)
- Стартирайте инсталатора с настройките по подразбиране

**macOS:**
- Инсталирайте чрез Homebrew: `brew install git`
- Или изтеглете от [git-scm.com](https://git-scm.com/download/mac)

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

### Стъпка 2: Клонирайте репозиторията

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Стъпка 3: Инсталирайте Python и Jupyter

Python 3.7 или по-нова версия е необходим за уроците по наука за данни.

**Windows:**
1. Изтеглете Python от [python.org](https://www.python.org/downloads/)
2. По време на инсталацията, маркирайте "Add Python to PATH"
3. Проверете инсталацията:
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

### Стъпка 4: Настройте Python среда

Препоръчително е да използвате виртуална среда, за да изолирате зависимостите.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Стъпка 5: Инсталирайте Python пакети

Инсталирайте необходимите библиотеки за наука за данни:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Стъпка 6: Инсталирайте Node.js и npm (за приложението с тестове)

Приложението с тестове изисква Node.js и npm.

**Windows/macOS:**
- Изтеглете от [nodejs.org](https://nodejs.org/) (препоръчва се LTS версия)
- Стартирайте инсталатора

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

### Стъпка 7: Инсталирайте зависимости за приложението с тестове

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Стъпка 8: Инсталирайте Docsify (по избор)

За офлайн достъп до документацията:

```bash
npm install -g docsify-cli
```

## Проверка на инсталацията

### Тествайте Python и Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Вашият браузър трябва да се отвори с интерфейса на Jupyter. Сега можете да навигирате до `.ipynb` файл на който и да е урок.

### Тествайте приложението с тестове

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Приложението с тестове трябва да бъде достъпно на `http://localhost:8080` (или друг порт, ако 8080 е зает).

### Тествайте сървъра за документация

```bash
# From the root directory of the repository
docsify serve
```

Документацията трябва да бъде достъпна на `http://localhost:3000`.

## Използване на Dev Containers в VS Code

Ако имате инсталиран Docker, можете да използвате Dev Containers в VS Code:

1. Инсталирайте [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Инсталирайте [Visual Studio Code](https://code.visualstudio.com/)
3. Инсталирайте разширението [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Отворете репозиторията в VS Code
5. Натиснете `F1` и изберете "Remote-Containers: Reopen in Container"
6. Изчакайте контейнерът да се изгради (само при първото стартиране)

## Следващи стъпки

- Разгледайте [README.md](README.md) за общ преглед на учебната програма
- Прочетете [USAGE.md](USAGE.md) за често срещани работни процеси и примери
- Проверете [TROUBLESHOOTING.md](TROUBLESHOOTING.md), ако срещнете проблеми
- Прегледайте [CONTRIBUTING.md](CONTRIBUTING.md), ако искате да допринесете

## Получаване на помощ

Ако срещнете проблеми:

1. Проверете ръководството [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Потърсете съществуващи [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Присъединете се към нашата [Discord общност](https://aka.ms/ds4beginners/discord)
4. Създайте нов проблем с подробна информация за вашия проблем

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.