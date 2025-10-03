<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:48:11+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "sr"
}
-->
# Водич за решавање проблема

Овај водич пружа решења за уобичајене проблеме на које можете наићи док радите са наставним планом и програмом "Наука о подацима за почетнике".

## Садржај

- [Проблеми са Python-ом и Jupyter-ом](../..)
- [Проблеми са пакетима и зависностима](../..)
- [Проблеми са Jupyter Notebook-ом](../..)
- [Проблеми са апликацијом за квиз](../..)
- [Проблеми са Git-ом и GitHub-ом](../..)
- [Проблеми са документацијом Docsify](../..)
- [Проблеми са подацима и датотекама](../..)
- [Проблеми са перформансама](../..)
- [Добијање додатне помоћи](../..)

## Проблеми са Python-ом и Jupyter-ом

### Python није пронађен или је погрешна верзија

**Проблем:** `python: command not found` или погрешна верзија Python-а

**Решење:**

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

**Решење за Windows:**
1. Поново инсталирајте Python са [python.org](https://www.python.org/)
2. Током инсталације, означите "Add Python to PATH"
3. Поново покрените терминал/командну линију

### Проблеми са активацијом виртуелног окружења

**Проблем:** Виртуелно окружење се не активира

**Решење:**

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

**Потврдите активацију:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### Проблеми са Jupyter кернелом

**Проблем:** "Kernel not found" или "Kernel keeps dying"

**Решење:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**Проблем:** Погрешна верзија Python-а у Jupyter-у

**Решење:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## Проблеми са пакетима и зависностима

### Грешке при увозу

**Проблем:** `ModuleNotFoundError: No module named 'pandas'` (или други пакети)

**Решење:**

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

### Неуспех при инсталацији преко pip-а

**Проблем:** `pip install` не успева због грешака са дозволама

**Решење:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**Проблем:** `pip install` не успева због SSL сертификатских грешака

**Решење:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Конфликти верзија пакета

**Проблем:** Неусаглашене верзије пакета

**Решење:**

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

## Проблеми са Jupyter Notebook-ом

### Jupyter се не покреће

**Проблем:** Команда `jupyter notebook` није пронађена

**Решење:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook се не учитава или не чува

**Проблем:** "Notebook failed to load" или грешке при чувању

**Решење:**

1. Проверите дозволе за датотеке
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. Проверите да ли је датотека оштећена
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. Очистите Jupyter кеш
```bash
jupyter notebook --clear-cache
```

### Ћелија се не извршава

**Проблем:** Ћелија заглављена на "In [*]" или траје предуго

**Решење:**

1. **Прекините кернел**: Кликните на дугме "Interrupt" или притисните `I, I`
2. **Поново покрените кернел**: Мени Kernel → Restart
3. **Проверите да ли постоје бесконачне петље** у вашем коду
4. **Очистите излаз**: Cell → All Output → Clear

### Графикони се не приказују

**Проблем:** `matplotlib` графикони се не приказују у Notebook-у

**Решење:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**Алтернатива за интерактивне графиконе:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## Проблеми са апликацијом за квиз

### npm install не успева

**Проблем:** Грешке током `npm install`

**Решење:**

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

### Апликација за квиз се не покреће

**Проблем:** `npm run serve` не успева

**Решење:**

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

### Порт је већ у употреби

**Проблем:** "Port 8080 is already in use"

**Решење:**

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

### Квиз се не учитава или празна страница

**Проблем:** Апликација за квиз се учитава, али приказује празну страницу

**Решење:**

1. Проверите конзолу прегледача за грешке (F12)
2. Очистите кеш и колачиће прегледача
3. Пробајте други прегледач
4. Уверите се да је JavaScript омогућен
5. Проверите да ли блокатори реклама ометају рад

```bash
# Rebuild the app
npm run build
npm run serve
```

## Проблеми са Git-ом и GitHub-ом

### Git није препознат

**Проблем:** `git: command not found`

**Решење:**

**Windows:**
- Инсталирајте Git са [git-scm.com](https://git-scm.com/)
- Поново покрените терминал након инсталације

**macOS:**

> **Напомена:** Ако немате инсталиран Homebrew, пратите упутства на [https://brew.sh/](https://brew.sh/) да га прво инсталирате.
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

### Неуспех при клонирању

**Проблем:** `git clone` не успева због грешака у аутентификацији

**Решење:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### Дозвола одбијена (publickey)

**Проблем:** Аутентификација преко SSH кључа не успева

**Решење:**

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

## Проблеми са документацијом Docsify

### Команда Docsify није пронађена

**Проблем:** `docsify: command not found`

**Решење:**

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

### Документација се не учитава

**Проблем:** Docsify се покреће, али садржај се не учитава

**Решење:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### Слике се не приказују

**Проблем:** Слике приказују икону сломљеног линка

**Решење:**

1. Проверите да ли су путање до слика релативне
2. Уверите се да датотеке слика постоје у репозиторијуму
3. Очистите кеш прегледача
4. Проверите да ли се екстензије датотека поклапају (осетљивост на велика и мала слова на неким системима)

## Проблеми са подацима и датотекама

### Грешке "File Not Found"

**Проблем:** `FileNotFoundError` приликом учитавања података

**Решење:**

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

### Грешке при читању CSV датотека

**Проблем:** Грешке при читању CSV датотека

**Решење:**

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

### Грешке са меморијом код великих скупова података

**Проблем:** `MemoryError` приликом учитавања великих датотека

**Решење:**

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

## Проблеми са перформансама

### Спор рад Notebook-а

**Проблем:** Notebook-и раде веома споро

**Решење:**

1. **Поново покрените кернел и очистите излаз**
   - Kernel → Restart & Clear Output

2. **Затворите непотребне Notebook-е**

3. **Оптимизујте код:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **Узмите узорак великих скупова података:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### Прегледач се руши

**Проблем:** Прегледач се руши или постаје неупотребљив

**Решење:**

1. Затворите непотребне картице
2. Очистите кеш прегледача
3. Повећајте меморију прегледача (Chrome: `chrome://settings/system`)
4. Користите JupyterLab уместо:
```bash
pip install jupyterlab
jupyter lab
```

## Добијање додатне помоћи

### Пре него што затражите помоћ

1. Проверите овај водич за решавање проблема
2. Претражите [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. Прегледајте [INSTALLATION.md](INSTALLATION.md) и [USAGE.md](USAGE.md)
4. Покушајте да претражите поруку о грешци на интернету

### Како затражити помоћ

Када креирате питање или тражите помоћ, укључите:

1. **Оперативни систем**: Windows, macOS или Linux (која дистрибуција)
2. **Верзија Python-а**: Покрените `python --version`
3. **Порука о грешци**: Копирајте комплетну поруку о грешци
4. **Кораци за репродукцију**: Шта сте урадили пре него што се грешка догодила
5. **Шта сте већ пробали**: Решења која сте већ испробали

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

### Ресурси за заједницу

- **GitHub Issues**: [Креирајте питање](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [Придружите се нашој заједници](https://aka.ms/ds4beginners/discord)
- **Дискусије**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [Форуми за питања и одговоре](https://docs.microsoft.com/answers/)

### Повезана документација

- [INSTALLATION.md](INSTALLATION.md) - Упутства за подешавање
- [USAGE.md](USAGE.md) - Како користити наставни план и програм
- [CONTRIBUTING.md](CONTRIBUTING.md) - Како допринети
- [README.md](README.md) - Преглед пројекта

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.