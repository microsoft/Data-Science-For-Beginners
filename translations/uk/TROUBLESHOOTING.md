<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:50:02+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "uk"
}
-->
# Посібник з усунення несправностей

Цей посібник містить рішення для поширених проблем, які можуть виникнути під час роботи з навчальною програмою "Data Science for Beginners".

## Зміст

- [Проблеми з Python і Jupyter](../..)
- [Проблеми з пакетами та залежностями](../..)
- [Проблеми з Jupyter Notebook](../..)
- [Проблеми з додатком для тестів](../..)
- [Проблеми з Git і GitHub](../..)
- [Проблеми з документацією Docsify](../..)
- [Проблеми з даними та файлами](../..)
- [Проблеми з продуктивністю](../..)
- [Додаткова допомога](../..)

## Проблеми з Python і Jupyter

### Python не знайдено або неправильна версія

**Проблема:** `python: command not found` або неправильна версія Python

**Рішення:**

```bash
# Check Python version
python --version
python3 --version

# If Python 3 is installed as 'python3', create an alias
# On macOS/Linux, add to ~/.bashrc or ~/.zshrc:
alias python=python3
alias pip=pip3

# Or use python3 explicitly
python3 -m pip install jupyter
```

**Рішення для Windows:**
1. Перевстановіть Python з [python.org](https://www.python.org/)
2. Під час встановлення виберіть "Add Python to PATH"
3. Перезапустіть термінал/командний рядок

### Проблеми з активацією віртуального середовища

**Проблема:** Віртуальне середовище не активується

**Рішення:**

**Windows:**
```bash
# If you get execution policy error
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
venv\Scripts\activate
```

**macOS/Linux:**
```bash
# Ensure the activate script is executable
chmod +x venv/bin/activate

# Then activate
source venv/bin/activate
```

**Перевірка активації:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Проблеми з ядром Jupyter

**Проблема:** "Kernel not found" або "Kernel keeps dying"

**Рішення:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Проблема:** Неправильна версія Python у Jupyter

**Рішення:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Проблеми з пакетами та залежностями

### Помилки імпорту

**Проблема:** `ModuleNotFoundError: No module named 'pandas'` (або інші пакети)

**Рішення:**

```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install missing package
pip install pandas

# Install all common packages
pip install jupyter pandas numpy matplotlib seaborn scikit-learn

# Verify installation
python -c "import pandas; print(pandas.__version__)"
```

### Помилки встановлення через pip

**Проблема:** `pip install` завершується з помилками дозволу

**Рішення:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Проблема:** `pip install` завершується з помилками SSL-сертифікатів

**Рішення:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Конфлікти версій пакетів

**Проблема:** Несумісні версії пакетів

**Рішення:**

```bash
# Create fresh virtual environment
python -m venv venv-new
source venv-new/bin/activate  # or venv-new\Scripts\activate on Windows

# Install packages with specific versions if needed
pip install pandas==1.3.0
pip install numpy==1.21.0

# Or let pip resolve dependencies
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

## Проблеми з Jupyter Notebook

### Jupyter не запускається

**Проблема:** Команда `jupyter notebook` не знайдена

**Рішення:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Зошит не завантажується або не зберігається

**Проблема:** "Notebook failed to load" або помилки збереження

**Рішення:**

1. Перевірте дозволи файлів
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Перевірте на пошкодження файлів
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Очистіть кеш Jupyter
```bash
jupyter notebook --clear-cache
```

### Комірка не виконується

**Проблема:** Комірка зависає на "In [*]" або виконується дуже довго

**Рішення:**

1. **Перервіть ядро**: Натисніть кнопку "Interrupt" або клавіші `I, I`
2. **Перезапустіть ядро**: Меню Kernel → Restart
3. **Перевірте код на наявність нескінченних циклів**
4. **Очистіть вивід**: Cell → All Output → Clear

### Графіки не відображаються

**Проблема:** Графіки `matplotlib` не показуються в зошиті

**Рішення:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Альтернатива для інтерактивних графіків:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Проблеми з додатком для тестів

### npm install завершується з помилками

**Проблема:** Помилки під час виконання `npm install`

**Рішення:**

```bash
# Clear npm cache
npm cache clean --force

# Remove node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Reinstall
npm install

# If still failing, try with legacy peer deps
npm install --legacy-peer-deps
```

### Додаток для тестів не запускається

**Проблема:** `npm run serve` завершується з помилками

**Рішення:**

```bash
# Check Node.js version
node --version  # Should be 12.x or higher

# Reinstall dependencies
cd quiz-app
rm -rf node_modules package-lock.json
npm install

# Try different port
npm run serve -- --port 8081
```

### Порт вже використовується

**Проблема:** "Port 8080 is already in use"

**Рішення:**

```bash
# Find and kill process on port 8080
# macOS/Linux:
lsof -ti:8080 | xargs kill -9

# Windows:
netstat -ano | findstr :8080
taskkill /PID <PID> /F

# Or use a different port
npm run serve -- --port 8081
```

### Тест не завантажується або порожня сторінка

**Проблема:** Додаток для тестів завантажується, але показує порожню сторінку

**Рішення:**

1. Перевірте консоль браузера на наявність помилок (F12)
2. Очистіть кеш і файли cookie браузера
3. Спробуйте інший браузер
4. Переконайтеся, що JavaScript увімкнено
5. Перевірте, чи не заважають блокувальники реклами

```bash
# Rebuild the app
npm run build
npm run serve
```

## Проблеми з Git і GitHub

### Git не розпізнається

**Проблема:** `git: command not found`

**Рішення:**

**Windows:**
- Встановіть Git з [git-scm.com](https://git-scm.com/)
- Перезапустіть термінал після встановлення

**macOS:**

> **Примітка:** Якщо у вас не встановлено Homebrew, дотримуйтесь інструкцій на [https://brew.sh/](https://brew.sh/) для встановлення.
```bash
# Install via Homebrew
brew install git

# Or install Xcode Command Line Tools
xcode-select --install
```

**Linux:**
```bash
sudo apt-get install git  # Debian/Ubuntu
sudo dnf install git      # Fedora
```

### Помилки клонування

**Проблема:** `git clone` завершується з помилками автентифікації

**Рішення:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Відмовлено в доступі (publickey)

**Проблема:** Помилки автентифікації SSH-ключа

**Рішення:**

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add key to ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Add public key to GitHub
# Copy key: cat ~/.ssh/id_ed25519.pub
# Add at: https://github.com/settings/keys
```

## Проблеми з документацією Docsify

### Команда Docsify не знайдена

**Проблема:** `docsify: command not found`

**Рішення:**

```bash
# Install globally
npm install -g docsify-cli

# If permission error on macOS/Linux
sudo npm install -g docsify-cli

# Verify installation
docsify --version

# If still not found, add npm global path
# Find npm global path
npm config get prefix

# Add to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH="$PATH:/usr/local/bin"
```

### Документація не завантажується

**Проблема:** Docsify запускається, але контент не завантажується

**Рішення:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Зображення не відображаються

**Проблема:** Зображення показують значок зламаного посилання

**Рішення:**

1. Перевірте, чи шляхи до зображень є відносними
2. Переконайтеся, що файли зображень існують у репозиторії
3. Очистіть кеш браузера
4. Перевірте, чи збігаються розширення файлів (чутливість до регістру на деяких системах)

## Проблеми з даними та файлами

### Помилки "Файл не знайдено"

**Проблема:** `FileNotFoundError` під час завантаження даних

**Рішення:**

```python
import os

# Check current working directory
print(os.getcwd())

# Use absolute path
data_path = os.path.join(os.getcwd(), 'data', 'filename.csv')
df = pd.read_csv(data_path)

# Or use relative path from notebook location
df = pd.read_csv('../data/filename.csv')

# Verify file exists
print(os.path.exists('data/filename.csv'))
```

### Помилки читання CSV

**Проблема:** Помилки під час читання файлів CSV

**Рішення:**

```python
import pandas as pd

# Try different encodings
df = pd.read_csv('file.csv', encoding='utf-8')
# or
df = pd.read_csv('file.csv', encoding='latin-1')
# or
df = pd.read_csv('file.csv', encoding='ISO-8859-1')

# Handle missing values
df = pd.read_csv('file.csv', na_values=['NA', 'N/A', ''])

# Specify delimiter if not comma
df = pd.read_csv('file.csv', delimiter=';')
```

### Помилки пам'яті з великими наборами даних

**Проблема:** `MemoryError` під час завантаження великих файлів

**Рішення:**

```python
# Read in chunks
chunk_size = 10000
chunks = []
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # Process chunk
    chunks.append(chunk)
df = pd.concat(chunks)

# Or read specific columns only
df = pd.read_csv('file.csv', usecols=['col1', 'col2'])

# Use more efficient data types
df = pd.read_csv('file.csv', dtype={'column_name': 'int32'})
```

## Проблеми з продуктивністю

### Повільна робота зошитів

**Проблема:** Зошити працюють дуже повільно

**Рішення:**

1. **Перезапустіть ядро та очистіть вивід**
   - Kernel → Restart & Clear Output

2. **Закрийте невикористовувані зошити**

3. **Оптимізуйте код:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Вибіркове використання великих наборів даних:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Збої браузера

**Проблема:** Браузер зависає або стає нереспонсивним

**Рішення:**

1. Закрийте невикористовувані вкладки
2. Очистіть кеш браузера
3. Збільште пам'ять браузера (Chrome: `chrome://settings/system`)
4. Використовуйте JupyterLab замість:
```bash
pip install jupyterlab
jupyter lab
```

## Додаткова допомога

### Перед тим, як просити допомогу

1. Перевірте цей посібник з усунення несправностей
2. Шукайте [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Ознайомтеся з [INSTALLATION.md](INSTALLATION.md) і [USAGE.md](USAGE.md)
4. Спробуйте знайти повідомлення про помилку в інтернеті

### Як просити допомогу

Коли створюєте запит або просите допомогу, включіть:

1. **Операційна система**: Windows, macOS або Linux (який дистрибутив)
2. **Версія Python**: Виконайте `python --version`
3. **Повідомлення про помилку**: Скопіюйте повне повідомлення про помилку
4. **Кроки для відтворення**: Що ви зробили перед виникненням помилки
5. **Що ви вже пробували**: Рішення, які ви вже спробували

**Приклад:**
```
**Operating System:** macOS 12.0
**Python Version:** 3.9.7
**Error Message:** ModuleNotFoundError: No module named 'pandas'
**Steps to Reproduce:**
1. Activated virtual environment
2. Started Jupyter notebook
3. Tried to import pandas

**What I've Tried:**
- Ran pip install pandas
- Restarted Jupyter
```

### Ресурси спільноти

- **GitHub Issues**: [Створити запит](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Приєднатися до спільноти](https://aka.ms/ds4beginners/discord)
- **Обговорення**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Форуми Q&A](https://docs.microsoft.com/answers/)

### Супутня документація

- [INSTALLATION.md](INSTALLATION.md) - Інструкції з налаштування
- [USAGE.md](USAGE.md) - Як використовувати навчальну програму
- [CONTRIBUTING.md](CONTRIBUTING.md) - Як зробити внесок
- [README.md](README.md) - Огляд проєкту

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.