<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:29:52+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "ru"
}
-->
# Руководство по устранению неполадок

Это руководство предлагает решения для распространенных проблем, которые могут возникнуть при работе с учебной программой "Data Science for Beginners".

## Содержание

- [Проблемы с Python и Jupyter](../..)
- [Проблемы с пакетами и зависимостями](../..)
- [Проблемы с Jupyter Notebook](../..)
- [Проблемы с приложением для викторин](../..)
- [Проблемы с Git и GitHub](../..)
- [Проблемы с документацией Docsify](../..)
- [Проблемы с данными и файлами](../..)
- [Проблемы с производительностью](../..)
- [Получение дополнительной помощи](../..)

## Проблемы с Python и Jupyter

### Python не найден или неправильная версия

**Проблема:** `python: command not found` или неправильная версия Python

**Решение:**

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

**Решение для Windows:**
1. Переустановите Python с [python.org](https://www.python.org/)
2. Во время установки отметьте "Add Python to PATH"
3. Перезапустите терминал/командную строку

### Проблемы с активацией виртуального окружения

**Проблема:** Виртуальное окружение не активируется

**Решение:**

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

**Проверка активации:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Проблемы с ядром Jupyter

**Проблема:** "Kernel not found" или "Kernel keeps dying"

**Решение:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Проблема:** Неправильная версия Python в Jupyter

**Решение:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Проблемы с пакетами и зависимостями

### Ошибки импорта

**Проблема:** `ModuleNotFoundError: No module named 'pandas'` (или других пакетов)

**Решение:**

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

### Ошибки установки через pip

**Проблема:** `pip install` завершается ошибкой из-за проблем с правами

**Решение:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Проблема:** `pip install` завершается ошибкой SSL-сертификата

**Решение:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Конфликты версий пакетов

**Проблема:** Несовместимые версии пакетов

**Решение:**

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

## Проблемы с Jupyter Notebook

### Jupyter не запускается

**Проблема:** Команда `jupyter notebook` не найдена

**Решение:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook не загружается или не сохраняется

**Проблема:** "Notebook failed to load" или ошибки сохранения

**Решение:**

1. Проверьте права доступа к файлу
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Проверьте файл на повреждения
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Очистите кэш Jupyter
```bash
jupyter notebook --clear-cache
```

### Ячейка не выполняется

**Проблема:** Ячейка зависает на "In [*]" или выполняется слишком долго

**Решение:**

1. **Прервите выполнение ядра**: Нажмите кнопку "Interrupt" или `I, I`
2. **Перезапустите ядро**: Меню Kernel → Restart
3. **Проверьте код на наличие бесконечных циклов**
4. **Очистите вывод**: Cell → All Output → Clear

### Графики не отображаются

**Проблема:** Графики `matplotlib` не отображаются в ноутбуке

**Решение:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Альтернатива для интерактивных графиков:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Проблемы с приложением для викторин

### Ошибки при npm install

**Проблема:** Ошибки во время выполнения `npm install`

**Решение:**

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

### Приложение для викторин не запускается

**Проблема:** `npm run serve` завершается ошибкой

**Решение:**

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

### Порт уже используется

**Проблема:** "Port 8080 is already in use"

**Решение:**

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

### Викторина не загружается или пустая страница

**Проблема:** Приложение загружается, но отображает пустую страницу

**Решение:**

1. Проверьте консоль браузера на наличие ошибок (F12)
2. Очистите кэш и куки браузера
3. Попробуйте другой браузер
4. Убедитесь, что JavaScript включен
5. Проверьте, не мешают ли блокировщики рекламы

```bash
# Rebuild the app
npm run build
npm run serve
```

## Проблемы с Git и GitHub

### Git не распознается

**Проблема:** `git: command not found`

**Решение:**

**Windows:**
- Установите Git с [git-scm.com](https://git-scm.com/)
- Перезапустите терминал после установки

**macOS:**

> **Примечание:** Если у вас не установлен Homebrew, следуйте инструкциям на [https://brew.sh/](https://brew.sh/) для его установки.
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

### Ошибки при клонировании

**Проблема:** `git clone` завершается ошибкой аутентификации

**Решение:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Permission Denied (publickey)

**Проблема:** Ошибка аутентификации через SSH-ключ

**Решение:**

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

## Проблемы с документацией Docsify

### Команда Docsify не найдена

**Проблема:** `docsify: command not found`

**Решение:**

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

### Документация не загружается

**Проблема:** Docsify запускается, но контент не загружается

**Решение:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Изображения не отображаются

**Проблема:** Изображения отображаются как значок сломанной ссылки

**Решение:**

1. Проверьте, что пути к изображениям относительные
2. Убедитесь, что файлы изображений существуют в репозитории
3. Очистите кэш браузера
4. Проверьте, что расширения файлов совпадают (учитывая регистр на некоторых системах)

## Проблемы с данными и файлами

### Ошибки "Файл не найден"

**Проблема:** `FileNotFoundError` при загрузке данных

**Решение:**

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

### Ошибки при чтении CSV

**Проблема:** Ошибки при чтении CSV-файлов

**Решение:**

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

### Ошибки памяти при работе с большими наборами данных

**Проблема:** `MemoryError` при загрузке больших файлов

**Решение:**

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

## Проблемы с производительностью

### Медленная работа ноутбуков

**Проблема:** Ноутбуки работают очень медленно

**Решение:**

1. **Перезапустите ядро и очистите вывод**
   - Kernel → Restart & Clear Output

2. **Закройте неиспользуемые ноутбуки**

3. **Оптимизируйте код:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Используйте выборку из больших наборов данных:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Сбои браузера

**Проблема:** Браузер зависает или становится неотзывчивым

**Решение:**

1. Закройте неиспользуемые вкладки
2. Очистите кэш браузера
3. Увеличьте память браузера (Chrome: `chrome://settings/system`)
4. Используйте JupyterLab вместо Jupyter Notebook:
```bash
pip install jupyterlab
jupyter lab
```

## Получение дополнительной помощи

### Перед обращением за помощью

1. Ознакомьтесь с этим руководством по устранению неполадок
2. Поиск в [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Ознакомьтесь с [INSTALLATION.md](INSTALLATION.md) и [USAGE.md](USAGE.md)
4. Попробуйте найти сообщение об ошибке в интернете

### Как запросить помощь

При создании запроса или обращении за помощью укажите:

1. **Операционная система**: Windows, macOS или Linux (какое именно дистрибутив)
2. **Версия Python**: Выполните `python --version`
3. **Сообщение об ошибке**: Скопируйте полное сообщение об ошибке
4. **Шаги для воспроизведения**: Что вы сделали перед возникновением ошибки
5. **Что вы уже пробовали**: Решения, которые вы уже попытались применить

**Пример:**
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

### Ресурсы сообщества

- **GitHub Issues**: [Создать запрос](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Присоединиться к сообществу](https://aka.ms/ds4beginners/discord)
- **Обсуждения**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Форумы вопросов и ответов](https://docs.microsoft.com/answers/)

### Связанная документация

- [INSTALLATION.md](INSTALLATION.md) - Инструкции по установке
- [USAGE.md](USAGE.md) - Как использовать учебную программу
- [CONTRIBUTING.md](CONTRIBUTING.md) - Как внести вклад
- [README.md](README.md) - Обзор проекта

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.