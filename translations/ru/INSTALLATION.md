<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:14:25+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "ru"
}
-->
# Руководство по установке

Это руководство поможет вам настроить среду для работы с учебной программой «Основы Data Science».

## Содержание

- [Предварительные требования](../..)
- [Быстрые варианты начала работы](../..)
- [Локальная установка](../..)
- [Проверка установки](../..)

## Предварительные требования

Перед началом работы вам потребуется:

- Базовые знания работы с командной строкой/терминалом
- Аккаунт на GitHub (бесплатный)
- Стабильное интернет-соединение для начальной настройки

## Быстрые варианты начала работы

### Вариант 1: GitHub Codespaces (рекомендуется для новичков)

Самый простой способ начать — использовать GitHub Codespaces, который предоставляет готовую среду разработки прямо в браузере.

1. Перейдите в [репозиторий](https://github.com/microsoft/Data-Science-For-Beginners)
2. Нажмите на выпадающее меню **Code**
3. Выберите вкладку **Codespaces**
4. Нажмите **Create codespace on main**
5. Дождитесь инициализации среды (2-3 минуты)

Ваша среда готова, и все зависимости уже установлены!

### Вариант 2: Локальная разработка

Для работы на вашем компьютере следуйте подробным инструкциям ниже.

## Локальная установка

### Шаг 1: Установите Git

Git необходим для клонирования репозитория и отслеживания изменений.

**Windows:**
- Скачайте с [git-scm.com](https://git-scm.com/download/win)
- Запустите установщик с настройками по умолчанию

**macOS:**
- Установите через Homebrew: `brew install git`
- Или скачайте с [git-scm.com](https://git-scm.com/download/mac)

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

### Шаг 2: Клонируйте репозиторий

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Шаг 3: Установите Python и Jupyter

Для уроков по Data Science требуется Python версии 3.7 или выше.

**Windows:**
1. Скачайте Python с [python.org](https://www.python.org/downloads/)
2. Во время установки отметьте «Add Python to PATH»
3. Проверьте установку:
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

### Шаг 4: Настройте Python-среду

Рекомендуется использовать виртуальную среду для изоляции зависимостей.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Шаг 5: Установите Python-библиотеки

Установите необходимые библиотеки для Data Science:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Шаг 6: Установите Node.js и npm (для приложения викторины)

Для работы приложения викторины требуется Node.js и npm.

**Windows/macOS:**
- Скачайте с [nodejs.org](https://nodejs.org/) (рекомендуется версия LTS)
- Запустите установщик

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

### Шаг 7: Установите зависимости для приложения викторины

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Шаг 8: Установите Docsify (опционально)

Для офлайн-доступа к документации:

```bash
npm install -g docsify-cli
```

## Проверка установки

### Тестирование Python и Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Ваш браузер должен открыть интерфейс Jupyter. Теперь вы можете перейти к любому файлу `.ipynb` из уроков.

### Тестирование приложения викторины

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Приложение викторины должно быть доступно по адресу `http://localhost:8080` (или другому порту, если 8080 занят).

### Тестирование сервера документации

```bash
# From the root directory of the repository
docsify serve
```

Документация должна быть доступна по адресу `http://localhost:3000`.

## Использование Dev Containers в VS Code

Если у вас установлен Docker, вы можете использовать Dev Containers в VS Code:

1. Установите [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Установите [Visual Studio Code](https://code.visualstudio.com/)
3. Установите расширение [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Откройте репозиторий в VS Code
5. Нажмите `F1` и выберите «Remote-Containers: Reopen in Container»
6. Дождитесь сборки контейнера (только при первом запуске)

## Следующие шаги

- Ознакомьтесь с [README.md](README.md) для обзора учебной программы
- Прочитайте [USAGE.md](USAGE.md) для примеров и часто используемых рабочих процессов
- Ознакомьтесь с [TROUBLESHOOTING.md](TROUBLESHOOTING.md), если столкнетесь с проблемами
- Изучите [CONTRIBUTING.md](CONTRIBUTING.md), если хотите внести вклад

## Получение помощи

Если вы столкнулись с проблемами:

1. Ознакомьтесь с руководством [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Найдите существующие [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Присоединяйтесь к нашему [сообществу в Discord](https://aka.ms/ds4beginners/discord)
4. Создайте новый issue с подробным описанием вашей проблемы

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.