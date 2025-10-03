<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:27:30+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "uk"
}
-->
# Посібник з встановлення

Цей посібник допоможе вам налаштувати середовище для роботи з навчальною програмою "Основи Data Science".

## Зміст

- [Попередні вимоги](../..)
- [Швидкі варіанти старту](../..)
- [Локальне встановлення](../..)
- [Перевірка встановлення](../..)

## Попередні вимоги

Перед початком роботи вам потрібно:

- Базове розуміння командного рядка/терміналу
- Обліковий запис GitHub (безкоштовний)
- Стабільне інтернет-з'єднання для початкового налаштування

## Швидкі варіанти старту

### Варіант 1: GitHub Codespaces (Рекомендовано для початківців)

Найпростіший спосіб почати — це використання GitHub Codespaces, який забезпечує повне середовище розробки у вашому браузері.

1. Перейдіть до [репозиторію](https://github.com/microsoft/Data-Science-For-Beginners)
2. Натисніть на випадаюче меню **Code**
3. Виберіть вкладку **Codespaces**
4. Натисніть **Create codespace on main**
5. Зачекайте, поки середовище ініціалізується (2-3 хвилини)

Ваше середовище готове з усіма попередньо встановленими залежностями!

### Варіант 2: Локальна розробка

Для роботи на вашому комп'ютері дотримуйтесь детальних інструкцій нижче.

## Локальне встановлення

### Крок 1: Встановіть Git

Git потрібен для клонування репозиторію та відстеження ваших змін.

**Windows:**
- Завантажте з [git-scm.com](https://git-scm.com/download/win)
- Запустіть інсталятор із налаштуваннями за замовчуванням

**macOS:**
- Встановіть через Homebrew: `brew install git`
- Або завантажте з [git-scm.com](https://git-scm.com/download/mac)

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

### Крок 2: Клонуйте репозиторій

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### Крок 3: Встановіть Python і Jupyter

Для уроків з Data Science потрібен Python версії 3.7 або новішої.

**Windows:**
1. Завантажте Python з [python.org](https://www.python.org/downloads/)
2. Під час встановлення поставте галочку "Add Python to PATH"
3. Перевірте встановлення:
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

### Крок 4: Налаштуйте Python-середовище

Рекомендується використовувати віртуальне середовище для ізоляції залежностей.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Крок 5: Встановіть Python-бібліотеки

Встановіть необхідні бібліотеки для Data Science:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Крок 6: Встановіть Node.js і npm (для додатку з вікторинами)

Для додатку з вікторинами потрібні Node.js і npm.

**Windows/macOS:**
- Завантажте з [nodejs.org](https://nodejs.org/) (рекомендується LTS-версія)
- Запустіть інсталятор

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

### Крок 7: Встановіть залежності для додатку з вікторинами

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### Крок 8: Встановіть Docsify (опціонально)

Для офлайн-доступу до документації:

```bash
npm install -g docsify-cli
```

## Перевірка встановлення

### Тестування Python і Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

Ваш браузер має відкритися з інтерфейсом Jupyter. Тепер ви можете перейти до будь-якого файлу `.ipynb` уроку.

### Тестування додатку з вікторинами

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Додаток з вікторинами має бути доступний за адресою `http://localhost:8080` (або іншим портом, якщо 8080 зайнятий).

### Тестування сервера документації

```bash
# From the root directory of the repository
docsify serve
```

Документація має бути доступна за адресою `http://localhost:3000`.

## Використання Dev Containers у VS Code

Якщо у вас встановлений Docker, ви можете використовувати Dev Containers у VS Code:

1. Встановіть [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Встановіть [Visual Studio Code](https://code.visualstudio.com/)
3. Встановіть розширення [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Відкрийте репозиторій у VS Code
5. Натисніть `F1` і виберіть "Remote-Containers: Reopen in Container"
6. Зачекайте, поки контейнер побудується (лише при першому запуску)

## Наступні кроки

- Ознайомтеся з [README.md](README.md) для огляду навчальної програми
- Прочитайте [USAGE.md](USAGE.md) для поширених робочих процесів і прикладів
- Перегляньте [TROUBLESHOOTING.md](TROUBLESHOOTING.md), якщо виникнуть проблеми
- Ознайомтеся з [CONTRIBUTING.md](CONTRIBUTING.md), якщо хочете зробити внесок

## Отримання допомоги

Якщо ви зіткнулися з проблемами:

1. Перевірте посібник [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Знайдіть існуючі [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Приєднайтеся до нашої [спільноти Discord](https://aka.ms/ds4beginners/discord)
4. Створіть новий Issue з детальною інформацією про вашу проблему

---

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, звертаємо вашу увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ мовою оригіналу слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.