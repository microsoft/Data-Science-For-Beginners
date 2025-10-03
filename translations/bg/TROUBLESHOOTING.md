<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:47:38+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "bg"
}
-->
# Ръководство за отстраняване на проблеми

Това ръководство предоставя решения на често срещани проблеми, които може да срещнете, докато работите с учебната програма "Наука за данни за начинаещи".

## Съдържание

- [Проблеми с Python и Jupyter](../..)
- [Проблеми с пакети и зависимости](../..)
- [Проблеми с Jupyter Notebook](../..)
- [Проблеми с приложението за тестове](../..)
- [Проблеми с Git и GitHub](../..)
- [Проблеми с документацията на Docsify](../..)
- [Проблеми с данни и файлове](../..)
- [Проблеми с производителността](../..)
- [Получаване на допълнителна помощ](../..)

## Проблеми с Python и Jupyter

### Python не е намерен или е грешна версия

**Проблем:** `python: command not found` или грешна версия на Python

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

**Решение за Windows:**
1. Преинсталирайте Python от [python.org](https://www.python.org/)
2. По време на инсталацията, маркирайте "Add Python to PATH"
3. Рестартирайте терминала/командния ред

### Проблеми с активиране на виртуална среда

**Проблем:** Виртуалната среда не се активира

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

**Проверка на активацията:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Проблеми с ядрото на Jupyter

**Проблем:** "Kernel not found" или "Kernel keeps dying"

**Решение:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Проблем:** Грешна версия на Python в Jupyter

**Решение:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Проблеми с пакети и зависимости

### Грешки при импортиране

**Проблем:** `ModuleNotFoundError: No module named 'pandas'` (или други пакети)

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

### Неуспехи при инсталиране с pip

**Проблем:** `pip install` не успява с грешки за разрешения

**Решение:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Проблем:** `pip install` не успява с грешки за SSL сертификати

**Решение:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Конфликти на версии на пакети

**Проблем:** Несъвместими версии на пакети

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

## Проблеми с Jupyter Notebook

### Jupyter не стартира

**Проблем:** Командата `jupyter notebook` не е намерена

**Решение:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook не се зарежда или не се записва

**Проблем:** "Notebook failed to load" или грешки при запис

**Решение:**

1. Проверете разрешенията на файла
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Проверете за повреда на файла
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Изчистете кеша на Jupyter
```bash
jupyter notebook --clear-cache
```

### Клетката не се изпълнява

**Проблем:** Клетката остава на "In [*]" или отнема твърде много време

**Решение:**

1. **Прекъснете ядрото:** Кликнете върху бутона "Interrupt" или натиснете `I, I`
2. **Рестартирайте ядрото:** Меню Kernel → Restart
3. **Проверете за безкрайни цикли** в кода си
4. **Изчистете изхода:** Меню Cell → All Output → Clear

### Графики не се показват

**Проблем:** Графиките на `matplotlib` не се показват в notebook

**Решение:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Алтернатива за интерактивни графики:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Проблеми с приложението за тестове

### npm install не успява

**Проблем:** Грешки по време на `npm install`

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

### Приложението за тестове не стартира

**Проблем:** `npm run serve` не успява

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

### Портът вече се използва

**Проблем:** "Port 8080 is already in use"

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

### Тестът не се зарежда или показва празна страница

**Проблем:** Приложението за тестове се зарежда, но показва празна страница

**Решение:**

1. Проверете конзолата на браузъра за грешки (F12)
2. Изчистете кеша и бисквитките на браузъра
3. Опитайте с друг браузър
4. Уверете се, че JavaScript е активиран
5. Проверете дали блокиращи реклами пречат

```bash
# Rebuild the app
npm run build
npm run serve
```

## Проблеми с Git и GitHub

### Git не е разпознат

**Проблем:** `git: command not found`

**Решение:**

**Windows:**
- Инсталирайте Git от [git-scm.com](https://git-scm.com/)
- Рестартирайте терминала след инсталацията

**macOS:**

> **Забележка:** Ако нямате инсталиран Homebrew, следвайте инструкциите на [https://brew.sh/](https://brew.sh/), за да го инсталирате.
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

### Неуспех при клониране

**Проблем:** `git clone` не успява с грешки за автентикация

**Решение:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Отказан достъп (publickey)

**Проблем:** Грешка при автентикация с SSH ключ

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

## Проблеми с документацията на Docsify

### Командата Docsify не е намерена

**Проблем:** `docsify: command not found`

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

### Документацията не се зарежда

**Проблем:** Docsify се стартира, но съдържанието не се зарежда

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

### Изображенията не се показват

**Проблем:** Изображенията показват икона за счупена връзка

**Решение:**

1. Проверете дали пътищата на изображенията са относителни
2. Уверете се, че файловете с изображения съществуват в хранилището
3. Изчистете кеша на браузъра
4. Проверете дали разширенията на файловете съвпадат (чувствителни към малки/големи букви на някои системи)

## Проблеми с данни и файлове

### Грешки "Файлът не е намерен"

**Проблем:** `FileNotFoundError` при зареждане на данни

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

### Грешки при четене на CSV

**Проблем:** Грешки при четене на CSV файлове

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

### Грешки с паметта при големи набори от данни

**Проблем:** `MemoryError` при зареждане на големи файлове

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

## Проблеми с производителността

### Бавна производителност на notebook

**Проблем:** Notebook-ите работят много бавно

**Решение:**

1. **Рестартирайте ядрото и изчистете изхода**
   - Kernel → Restart & Clear Output

2. **Затворете неизползвани notebook-и**

3. **Оптимизирайте кода:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Извадете проба от големи набори от данни:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Сривове на браузъра

**Проблем:** Браузърът се срива или става неотзивчив

**Решение:**

1. Затворете неизползвани раздели
2. Изчистете кеша на браузъра
3. Увеличете паметта на браузъра (Chrome: `chrome://settings/system`)
4. Използвайте JupyterLab вместо това:
```bash
pip install jupyterlab
jupyter lab
```

## Получаване на допълнителна помощ

### Преди да поискате помощ

1. Проверете това ръководство за отстраняване на проблеми
2. Търсете в [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Прегледайте [INSTALLATION.md](INSTALLATION.md) и [USAGE.md](USAGE.md)
4. Опитайте да потърсите съобщението за грешка онлайн

### Как да поискате помощ

Когато създавате проблем или искате помощ, включете:

1. **Операционна система**: Windows, macOS или Linux (коя дистрибуция)
2. **Версия на Python**: Изпълнете `python --version`
3. **Съобщение за грешка**: Копирайте пълното съобщение за грешка
4. **Стъпки за възпроизвеждане**: Какво направихте преди да се появи грешката
5. **Какво сте опитали**: Решения, които вече сте пробвали

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

### Ресурси на общността

- **GitHub Issues**: [Създайте проблем](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Присъединете се към нашата общност](https://aka.ms/ds4beginners/discord)
- **Дискусии**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Форуми за въпроси и отговори](https://docs.microsoft.com/answers/)

### Свързана документация

- [INSTALLATION.md](INSTALLATION.md) - Инструкции за настройка
- [USAGE.md](USAGE.md) - Как да използвате учебната програма
- [CONTRIBUTING.md](CONTRIBUTING.md) - Как да допринесете
- [README.md](README.md) - Преглед на проекта

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.