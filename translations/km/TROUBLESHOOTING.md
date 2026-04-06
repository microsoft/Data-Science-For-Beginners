# មគ្គុទេសក៍ដោះស្រាយបញ្ហា

មគ្គុទេសក៍នេះផ្តល់ដំណោះស្រាយចំពោះបញ្ហាទូទៅដែលអ្នកអាចជួបប្រទៈនៅពេលធ្វើការជាមួយមេរៀន Data Science សម្រាប់អ្នកដើម។

## តារាងមាតិកា

- [បញ្ហា Python និង Jupyter](#បញ្ហា-python-និង-jupyter)
- [បញ្ហា Package និង Dependency](#បញ្ហា-package-និង-dependency)
- [បញ្ហា Jupyter Notebook](#បញ្ហា-jupyter-notebook)
- [បញ្ហាកម្មវិធី Quiz](#បញ្ហាកម្មវិធី-quiz)
- [បញ្ហា Git និង GitHub](#បញ្ហា-git-និង-github)
- [បញ្ហា Docsify Documentation](#បញ្ហា-docsify-documentation)
- [បញ្ហារបស់ Data និង File](#បញ្ហារបស់-data-និង-file)
- [បញ្ហាសមត្ថភាព](#បញ្ហាសមត្ថភាព)
- [ការទទួលបានជំនួយបន្ថែម](#ការទទួលបានជំនួយបន្ថែម)

## បញ្ហា Python និង Jupyter

### មិនឃើញ Python ឬ ជំនាន់មិនត្រឹមត្រូវ

**បញ្ហា:** `python: command not found` ឬ ជំនាន់ Python មិនត្រឹមត្រូវ

**ដំណោះស្រាយ:**

```bash
# ពិនិត្យ​ប្រភេទ Python
python --version
python3 --version

# បើ python3 បានដំឡើងជា 'python3', បង្កើត alias
# លើ macOS/Linux, បន្ថែមទៅ ~/.bashrc ឬ ~/.zshrc:
alias python=python3
alias pip=pip3

# ឬ​ប្រើ python3 យ៉ាងបញ្ជាក់
python3 -m pip install jupyter
```

**ដំណោះស្រាយសម្រាប់ Windows:**
1. តម្លើង Python ពី [python.org](https://www.python.org/)
2. នៅពេលតម្លើង សូមពិនិត្យ "Add Python to PATH"
3. បើកបញ្ចាញបញ្ជា/Terminal ឡើងវិញ

### បញ្ហាចាប់ផ្តើម Virtual Environment

**បញ្ហា:** Virtual environment មិនអាចចាប់ផ្តើមបាន

**ដំណោះស្រាយ:**

**Windows:**
```bash
# ប្រសិនបើអ្នកទទួលមានកំហុសគោលនយោបាយអនុវត្ត
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# បន្ទាប់មកបើកអ្នក
venv\Scripts\activate
```

**macOS/Linux:**
```bash
# បញ្ចាក់ឲ្យបានថា script បើកដំណើរការអាចប្រតិបត្តិបាន
chmod +x venv/bin/activate

# បន្ទាប់មកបើកដំណើរការ
source venv/bin/activate
```

**ตรวจสอบการเปิดใช้งาน:**
```bash
# បញ្ជាក់របស់អ្នកគួរតែបង្ហាញ (venv)
# ពិនិត្យទីតាំង Python
which python  # គួរតែចង្អុលទៅ venv
```

### បញ្ហា Kernel Jupyter

**បញ្ហា:** "Kernel not found" ឬ "Kernel keeps dying"

**ដំណោះស្រាយ:**

```bash
# ដំឡើង kernel ថ្មី
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# ឬប្រើ kernel លំនាំដើម
python -m ipykernel install --user

# ចាប់ផ្ដើម Jupyter ថ្មីម្តង
jupyter notebook
```

**បញ្ហា:** ជំនាន់ Python មិនត្រឹមត្រូវនៅក្នុង Jupyter

**ដំណោះស្រាយ:**
```bash
# តំឡើង Jupyter នៅក្នុងបរិបទវីរុសរបស់អ្នក
source venv/bin/activate  # បើកដំណើរការជាមុន
pip install jupyter ipykernel

# ចុះឈ្មោះកណ្តុរពហុ
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# នៅក្នុង Jupyter, ជ្រើស Kernel -> ប្ដូរកណ្តុរពហុ -> Python (venv)
```

## បញ្ហា Package និង Dependency

### បញ្ហា Import

**បញ្ហា:** `ModuleNotFoundError: No module named 'pandas'` (ឬ package ផ្សេង)

**ដំណោះស្រាយ:**

```bash
# ប្រាកដថាបរិយាកាសពិតត្រូវបានបើកបរ
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # វីនដូ

# ដំឡើងផ្នែកបាក់កេសដែលខ្វះ
pip install pandas

# ដំឡើងផ្នែកបាក់កេសទូទៅទាំងអស់
pip install jupyter pandas numpy matplotlib seaborn scikit-learn

# បញ្ជាក់ការដំឡើង
python -c "import pandas; print(pandas.__version__)"
```

### បិទការតម្លើង Pip

**បញ្ហា:** `pip install` បរាជ័យដោយសារមានបញ្ហារបស់ការអនុញ្ញាត

**ដំណោះស្រាយ:**

```bash
# ប្រើទង់ដង់ --user
pip install --user package-name

# ឬប្រើបរិយាកាសវត្ថុសូរ (ណែនាំ)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**បញ្ហា:** `pip install` បរាជ័យដោយសារត្រូវបាន SSL certificate

**ដំណោះស្រាយ:**

```bash
# បន្ទាន់សម័យ pip ជាមុនសិន
python -m pip install --upgrade pip

# សាកល្បងដំឡើងជាមួយម៉ាស៊ីនឧបត្ថម្ភដែលទុកចិត្តបាន (វិធីជួយបណ្តោះអាសន្ន)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### បញ្ហា Package មានជំនាន់ផ្ទុះ

**បញ្ហា:** ជំនាន់ package មិនត្រូវគ្នា

**ដំណោះស្រាយ:**

```bash
# បង្កើតបរិបទវើឌឺជាទំនើប
python -m venv venv-new
source venv-new/bin/activate  # ឬ venv-new\Scripts\activate នៅលើប្រព័ន្ធប្រតិបត្តិការ Windows

# ដំឡើងកញ្ចប់ជាមួយនឹងកំណែជាក់លាក់ ប្រសិនបើចាំបាច់
pip install pandas==1.3.0
pip install numpy==1.21.0

# ឬអនុញ្ញាតឲ្យ pip បញ្ចេញទំនាក់ទំនងដែលត្រូវការ
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

## បញ្ហា Jupyter Notebook

### Jupyter មិនចាប់ផ្តើម

**បញ្ហា:** ពាក្យបញ្ជា `jupyter notebook` មិនឃើញ

**ដំណោះស្រាយ:**

```bash
# ដំឡើង Jupyter
pip install jupyter

# ឬប្រើ python -m
python -m jupyter notebook

# បន្ថែមទៅ PATH ប្រសិនបើចាំបាច់ (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### Notebook មិនផ្ទុក ឬ មិនរក្សាទុក

**បញ្ហា:** "Notebook failed to load" ឬ បញ្ហាក្នុងការរក្សាទុក

**ដំណោះស្រាយ:**

1. ពិនិត្យសិទ្ធិលើ File
```bash
# ត្រូវប្រាកដថាអ្នកមានសិទ្ធិសរសេរ
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # ប្រសិនបើត្រូវការ
```

2. ពិនិត្យការខូចខាតនៅលើ File
```bash
# សាកល្បងបើកនៅកម្មវិធីកែសម្រួលអត្ថបទដើម្បីត្រួតពិនិត្យរចនាសម្ព័ន្ធ JSON
# បញ្ចូលមាតិកាទៅកាន់សៀវភៅកំណត់ត្រាថ្មី ប្រសិនបើខូចខាត
```

3. សម្អាត cache Jupyter
```bash
jupyter notebook --clear-cache
```

### Cell មិនអាចសម្រឹងបាន

**បញ្ហា:** Cell ឈរនៅ "In [*]" ឬ ប្រើពេលយូរ

**ដំណោះស្រាយ:**

1. **ដកចេញ kernel**: ចុចប៊ូតុង "Interrupt" ឬចុច `I, I`
2. **ចាប់ផ្តើម kernel ម្តងទៀត**: របារទំព័រ Kernel → Restart
3. **ពិនិត្យរក loop មិនចប់** ក្នុង code របស់អ្នក
4. **សម្អាតចេញលទ្ធផល**: Cell → All Output → Clear

### ការបង្ហាញផ្ទាំងរេចតាមប្រព័ន្ធមិនបង្ហាញ

**បញ្ហា:** `matplotlib` បង្ហាញគូលនៅក្នុង notebook មិនបាន

**ដំណោះស្រាយ:**

```python
# បន្ថែមពាក្យបញ្ជាមន្តអោយនៅកំពូលសៀវភៅកំណត់ត្រា
%matplotlib inline

import matplotlib.pyplot as plt

# បង្កើតផ្លុក
plt.plot([1, 2, 3, 4])
plt.show()  # បញ្ជាក់អោយហៅ show()
```

**ជម្រើសផ្សេងសម្រាប់ផ្ទាំងរេចតាមប្រព័ន្ធអន្តរកម្ម:**
```python
%matplotlib notebook
# ឬ
%matplotlib widget
```

## បញ្ហាកម្មវិធី Quiz

### ការតម្លើង npm បរាជ័យ

**បញ្ហា:** មានកំហុសនៅពេល `npm install`

**ដំណោះស្រាយ:**

```bash
# សម្អាត cache npm
npm cache clean --force

# យក node_modules និង package-lock.json ចេញ
rm -rf node_modules package-lock.json

# ដំឡើងឡើងវិញ
npm install

# ប្រសិនបើនៅតែបរាជ័យ សូមសាកល្បងជាមួយ legacy peer deps
npm install --legacy-peer-deps
```

### កម្មវិធី Quiz មិនចាប់ផ្តើម

**បញ្ហា:** `npm run serve` បរាជ័យ

**ដំណោះស្រាយ:**

```bash
# ពិនិត្យកំណែ Node.js
node --version  # គួរតែជាកំណែ 12.x ឬខ្ពស់ជាងនេះ

# ដំឡើងតម្រូវការឡើងវិញ
cd quiz-app
rm -rf node_modules package-lock.json
npm install

# សាកល្បងច្រកផ្សេងទៀត
npm run serve -- --port 8081
```

### ច្រក (Port) មានការប្រើប្រាស់រួចហើយ

**បញ្ហា:** "Port 8080 is already in use"

**ដំណោះស្រាយ:**

```bash
# ស្វែងរក និងបាញ់បណ្តាលដំណើរការនៅលើព្រលង់ 8080
# macOS/Linux:
lsof -ti:8080 | xargs kill -9

# Windows:
netstat -ano | findstr :8080
taskkill /PID <PID> /F

# ឬប្រើព្រលង់ផ្សេងទៀត
npm run serve -- --port 8081
```

### កម្មវិធី Quiz មិនផ្ទុក ឬ ទំព័របង្ហាញទទេ

**បញ្ហា:** កម្មវិធី Quiz ផ្ទុកប៉ុន្តែនៅទំព័រទទេ

**ដំណោះស្រាយ:**

1. ពិនិត្យ console របស់ browser សម្រាប់កំហុស (F12)
2. សម្អាត cache និង cookies របស់ browser
3. សាក browser ផ្សេងទៀត
4. ធានាបានថា JavaScript បានបើក
5. ពិនិត្យថាមិនមានកម្មវិធីរារាំងផ្សាយពាណិជ្ជកម្ម (ad blocker) រារាំង

```bash
# សាងសង់កម្មវិធីឡើងវិញ
npm run build
npm run serve
```

## បញ្ហា Git និង GitHub

### មិនកំណត់ស្គាល់ git

**បញ្ហា:** `git: command not found`

**ដំណោះស្រាយ:**

**Windows:**
- តម្លើង Git ពី [git-scm.com](https://git-scm.com/)
- បើក terminal ម្តងទៀតបន្ទាប់ពីតម្លើង

**macOS:**

> **ចំណាំ:** ប្រសិនបើអ្នកមិនមាន Homebrew ត្រូវធ្វើតាមការណែនាំនៅ [https://brew.sh/](https://brew.sh/) ដើម្បីតម្លើងជាមុន។
```bash
# ដំឡើងតាមរយៈ Homebrew
brew install git

# ឬដំឡើងឧបករណ៍បញ្ជារបន្ទាត់ Xcode
xcode-select --install
```

**Linux:**
```bash
sudo apt-get install git  # Debian/Ubuntu
sudo dnf install git      # Fedora
```

### ការចម្លង clone បរាជ័យ

**បញ្ហា:** `git clone` បរាជ័យដោយសារការផ្ទៀងផ្ទាត់មិនបាន

**ដំណោះស្រាយ:**

```bash
# ប្រើ URL HTTPS
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# ប្រសិនបើអ្នកបានបើក 2FA នៅលើ GitHub សូមប្រើ Personal Access Token
# បង្កើត token នៅ: https://github.com/settings/tokens
# ប្រើ token ជាពាក្យសម្ងាត់នៅពេលដែលត្រូវបានស្នើសុំ
```

### សិទ្ធិដាក់បដិសេធ (publickey)

**បញ្ហា:** ការផ្ទៀងផ្ទាត់សោ SSH បរាជ័យ

**ដំណោះស្រាយ:**

```bash
# បង្កើតកូនសោ SSH
ssh-keygen -t ed25519 -C "your_email@example.com"

# បញ្ចូលកូនសោទៅ ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# បន្ថែមកូនសោសាធារណៈទៅ GitHub
# ចម្លងកូនសោៈ cat ~/.ssh/id_ed25519.pub
# បន្ថែមនៅ៖ https://github.com/settings/keys
```

## បញ្ហា Docsify Documentation

### ពាក្យបញ្ជា Docsify មិនឃើញ

**បញ្ហា:** `docsify: command not found`

**ដំណោះស្រាយ:**

```bash
# ដំឡើងជាសកល
npm install -g docsify-cli

# ប្រសិនបើមានកំហុសសិទ្ធិលើ macOS/Linux
sudo npm install -g docsify-cli

# ផ្ទៀងផ្ទាត់ការដំឡើង
docsify --version

# ប្រសិនបើនៅតែមិនបានរកឃើញ ចូរបន្ថែមផ្លូវ npm ជាសកល
# រកផ្លូវ npm ជាសកល
npm config get prefix

# បន្ថែមទៅ PATH (បន្ថែមចូលក្នុង ~/.bashrc ឬ ~/.zshrc)
export PATH="$PATH:/usr/local/bin"
```

### ការរចនាឯកសារ មិនផ្ទុក

**បញ្ហា:** Docsify ប្រើប្រាស់បាន ប៉ុន្តែមាតិកាមិនផ្ទុក

**ដំណោះស្រាយ:**

```bash
# ការធានាថាអ្នកនៅក្នុងឫសកន្លែងបញ្ជូន
cd Data-Science-For-Beginners

# ពិនិត្យមើលសម្រាប់ index.html
ls index.html

# បម្រើជាមួយព័រត់ជាក់លាក់
docsify serve --port 3000

# ពិនិត្យមើលកុងសូលកម្មវិធីរុករកសម្រាប់កំហុស (F12)
```

### រូបភាពមិនបង្ហាញ

**បញ្ហា:** រូបភាពបង្ហាញការខូចខាត

**ដំណោះស្រាយ:**

1. ពិនិត្យវិថីរូបភាពគឺជាវិថីនិបាត
2. ធានាថារូបភាពមាននៅក្នុងធរណីមួយ
3. សម្អាត cache របស់ browser
4. ពិនិត្យឱ្យប្រាកដថាគ្មានកំហុសនៅក្នុងបន្ថែមទីបញ្ចូលឯកសារ (case-sensitive នៅលើប្រព័ន្ធខ្លះ)

## បញ្ហារបស់ Data និង File

### កំហុសមិនឃើញ File

**បញ្ហា:** `FileNotFoundError` ពេលដំណើរការទិន្នន័យ

**ដំណោះស្រាយ:**

```python
import os

# ពិនិត្យថាតើថតកំពុងធ្វើការបច្ចុប្បន្ន
print(os.getcwd())

# ប្រើផ្លូវដាច់ដោយឡែក
data_path = os.path.join(os.getcwd(), 'data', 'filename.csv')
df = pd.read_csv(data_path)

# ឬប្រើផ្លូវទាក់ទងពីទីតាំងសៀវភៅសរសេរ
df = pd.read_csv('../data/filename.csv')

# ផ្ទៀងផ្ទាត់ឯកសារមាននៅ
print(os.path.exists('data/filename.csv'))
```

### កំហុសអាន CSV

**បញ្ហា:** កំហុសនៅពេលអានឯកសារ CSV

**ដំណោះស្រាយ:**

```python
import pandas as pd

# ព្យាយាមការបង្កូតផ្សេងៗ
df = pd.read_csv('file.csv', encoding='utf-8')
# ឬ
df = pd.read_csv('file.csv', encoding='latin-1')
# ឬ
df = pd.read_csv('file.csv', encoding='ISO-8859-1')

# គ្រប់គ្រងតម្លៃដែលបាត់បង់
df = pd.read_csv('file.csv', na_values=['NA', 'N/A', ''])

# បញ្ជាក់អថេរបំបែក ប្រសិនបើមិនមែនជាក្បៀសកុម្ភៈ
df = pd.read_csv('file.csv', delimiter=';')
```

### កំហុសម៉ឺម៉ូរីជាមួយឯកសារច្រើន

**បញ្ហា:** `MemoryError` ពេលដំណើរការឯកសារធំ

**ដំណោះស្រាយ:**

```python
# អានជាផ្នែកៗ
chunk_size = 10000
chunks = []
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # ដំណើរការផ្នែក
    chunks.append(chunk)
df = pd.concat(chunks)

# ឬអានតែជួរឈរពិសេសប៉ុណ្ណោះ
df = pd.read_csv('file.csv', usecols=['col1', 'col2'])

# ប្រើប្រភេទទិន្នន័យដែលមានប្រសិទ្ធភាពច្រើនជាង
df = pd.read_csv('file.csv', dtype={'column_name': 'int32'})
```

## បញ្ហាសមត្ថភាព

### សមត្ថភាព Notebook យឺត

**បញ្ហា:** Notebook ធ្វើការយឺតខ្លាំង

**ដំណោះស្រាយ:**

1. **ចាប់ផ្តើម kernel ម្តងទៀត និងសម្អាតលទ្ធផល**
   - Kernel → Restart & Clear Output

2. **បិទ notebooks ដែលមិនប្រើប្រាស់**

3. **បង្កើនប្រសិទ្ធភាព code:**
```python
# ប្រើប្រតិបត្តិការវិចទ័រជំនួសការលោត
# អាក្រក់:
result = []
for x in data:
    result.append(x * 2)

# ល្អ:
result = data * 2  # វិចទ័រកម្ម NumPy/Pandas
```

4. **យកតែទិន្នន័យគំរូពី dataset ធំៗ:**
```python
# ធ្វើការជាមួយ​គំរូក្នុងអំឡុងពេលអភិវឌ្ឍន៍
df_sample = df.sample(n=1000)  # ឬ df.head(1000)
```

### Browser ធ្លាក់ឬមិនចាប់ផ្តើមបាន

**បញ្ហា:** Browser ធ្លាក់ ឬមិនប្រតិបត្តិការក្នុងលក្ខខណ្ឌល្អ

**ដំណោះស្រាយ:**

1. បិទផ្ទាំងបើកមិនប្រើប្រាស់
2. សម្អាត cache របស់ browser
3. បង្កើនម៉ឺម៉ូរី browser (Chrome: `chrome://settings/system`)
4. ប្រើ JupyterLab ជំនួស:
```bash
pip install jupyterlab
jupyter lab
```

## ការទទួលបានជំនួយបន្ថែម

### មុនសុំជំនួយ

1. សូមពិនិត្យមើលមគ្គុទេសក៍ដោះស្រាយបញ្ហានេះ
2. ស្វែងរកនៅ [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. ពិនិត្យឯកសារ [INSTALLATION.md](INSTALLATION.md) និង [USAGE.md](USAGE.md)
4. សាកសួរពាក្យកំហុសនៅលើអ៊ីនធើណេត

### របៀបសុំជំនួយ

ពេលបង្កើតបញ្ហា ឬសុំជំនួយ សូមបញ្ចូល:

1. **ប្រព័ន្ធប្រតិបត្តិការ**: Windows, macOS, ឬ Linux (ចុះដឹងប្រភេទ)
2. **ជំនាន់ Python**: រត់ `python --version`
3. **សារកំហុស**: ចម្លងសារបញ្ហាពេញលេញ
4. **ជំហានដែលបានធ្វើ**: ការប្រតិបត្តិមុនកើតកំហុស
5. **អ្វីដែលបានសាកល្បង**: ដំណោះស្រាយដែលអ្នកបានព្យាយាមរួច

**ឧទាហរណ៍:**
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

### ប្រភពធនធានសហគមន៍

- **GitHub Issues**: [បង្កើតបញ្ហា](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [ចូលរួមសហគមន៍](https://aka.ms/ds4beginners/discord)
- **Discussions**: [ការ​ពិភាក្សា GitHub](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [កន្លែងសួរសំណួរ Q&A](https://docs.microsoft.com/answers/)

### ឯកសារពាក់ព័ន្ធ

- [INSTALLATION.md](INSTALLATION.md) - មគ្គុទេសក៍ដំឡើង
- [USAGE.md](USAGE.md) - របៀបប្រើប្រាស់មេរៀន
- [CONTRIBUTING.md](CONTRIBUTING.md) - របៀបចូលរួម
- [README.md](README.md) - ពត៌មានសង្ខេបគម្រោង

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ បើទោះបីយើងខិតខំកទ្រឹងភាពត្រឹមត្រូវ ក៏ដោយ សូមជ្រាបថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុសឬមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសា​ដើមគួរត្រូវបានគិតថាជាឯកសារដែលមានភាពអប់រំខ្ពស់បំផុត។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើការបកប្រែដោយអ្នកជំនាញមនុស្សវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំនឹងឬការបោះពុម្ពអត់ត្រឹមត្រូវណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->