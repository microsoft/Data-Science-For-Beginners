# កម្មវិធីដំឡើង

មគ្គុទេសក៍នេះនឹងជួយអ្នកដំឡើងបរិបទសម្រាប់ធ្វើការជាមួយមេរៀន Data Science សម្រាប់អ្នកចាប់ផ្ដើម។

## តារាងមាតិកា

- [លក្ខខណ្ឌដំបូង](#លក្ខខណ្ឌដំបូង)
- [ជម្រើសចាប់ផ្ដើមយ៉ាងលឿន](#ជម្រើសចាប់ផ្ដើមយ៉ាងលឿន)
- [ការដំឡើងក្នុងផ្ទៃ](#ការដំឡើងក្នុងផ្ទៃ)
- [ពិនិត្យការដំឡើងរបស់អ្នក](#ពិនិត្យការដំឡើងរបស់អ្នក)

## លក្ខខណ្ឌដំបូង

មុនពេលអ្នកចាប់ផ្ដើម អ្នកគួរតែមាន៖

- ការជ្រាបខ្លះអំពីបន្ទាត់បញ្ជា/ទំរង់បញ្ជា
- គណនី GitHub (ឥតគិតថ្លៃ)
- ការតភ្ជាប់អ៊ីនធឺណិតមានស្ថិរភាពសម្រាប់ការដំឡើងដំបូង

## ជម្រើសចាប់ផ្ដើមយ៉ាងលឿន

### ជម្រើស 1: GitHub Codespaces (ផ្ញើសម្រាប់អ្នកចាប់ផ្ដើម)

វិធីងាយស្រួលបំផុតក្នុងការចាប់ផ្ដើមគឺប្រើ GitHub Codespaces ដែលផ្ដល់បរិយាកាសអភិវឌ្ឍន៍ពេញលេញនៅក្នុងកម្មវិធីរុករករបស់អ្នក។

1. ទៅកាន់ [repository](https://github.com/microsoft/Data-Science-For-Beginners)
2. ចុចម៉ឺនុយបាញ់ចុច **Code**
3. ជ្រើសរើសផ្ទាំង **Codespaces**
4. ចុច **Create codespace on main**
5. រង់ចាំបរិយាកាសឱ្យចាប់ផ្ដើម (2-3 នាទី)

បរិយាកាសរបស់អ្នកបានរួចរាល់ជាមួយគ្រឿងចម្អិនទាំងអស់ដែលបានដំឡើងមុនហើយ!

### ជម្រើស 2: ការអភិវឌ្ឍក្នុងផ្ទៃ

សម្រាប់ធ្វើការដោយកុំព្យូទ័រផ្ទាល់ខ្លួន សូមអនុវត្តការណែនាំលម្អិតខាងក្រោម។

## ការដំឡើងក្នុងផ្ទៃ

### ជំហាន 1: ដំឡើង Git

Git ត្រូវការដើម្បីបម្លែង repository និងតាមដានការផ្លាស់ប្តូររបស់អ្នក។

**Windows:**
- ទាញយកពី [git-scm.com](https://git-scm.com/download/win)
- ប្រតិបត្តិកម្មវិធីដំឡើងដោយប្រើការកំណត់លំនាំដើម

**macOS:**
- ដំឡើងតាមរយៈ Homebrew: `brew install git`
- ឬទាញយកពី [git-scm.com](https://git-scm.com/download/mac)

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

### ជំហាន 2: បម្លែង Repository

```bash
# ចម្លងហាងទំនិញ
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# ទៅកាន់ថតឯកសារ
cd Data-Science-For-Beginners
```

### ជំហាន 3: ដំឡើង Python និង Jupyter

Python 3.7 ឬខ្ពស់ជាងនេះ ត្រូវការសម្រាប់មេរៀនវិទ្យាសាស្ត្រទិន្នន័យ។

**Windows:**
1. ទាញយក Python ពី [python.org](https://www.python.org/downloads/)
2. ក្នុងអំឡុងដំឡើង សូមពិនិត្យ "Add Python to PATH"
3. ពិនិត្យការដំឡើង:
```bash
python --version
```

**macOS:**
```bash
# ការប្រើប្រាស់ Homebrew
brew install python3

# បញ្ជាក់ការដំឡើង
python3 --version
```

**Linux:**
```bash
# បំពាក់ Python រួចជាលំនាំនៅក្នុងច្រើនចេញផ្សាយលីនុចទាំងអស់
python3 --version

# ប្រសិនបើមិនបានដំឡើង៖
# Debian/Ubuntu
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

### ជំហាន 4: កំណត់បរិយាកាស Python

ផ្ដល់អធិប្បាយឲ្យប្រើបរិយាកាសវិនិយោគផ្ទាល់ខ្លួនដើម្បីរក្សាគ្រឿងចម្អិនឲ្យឡែកពីគ្នា។

```bash
# បង្កើតបរិយាកាសវត្ថុតំណាង
python -m venv venv

# បើកបរិយាកាសវត្ថុតំណាង
# នៅលើ Windows:
venv\Scripts\activate

# នៅលើ macOS/Linux:
source venv/bin/activate
```

### ជំហាន 5: ដំឡើងកញ្ចប់ Python

ដំឡើងបណ្ណាល័យទិន្នន័យដែលត្រូវការ៖

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### ជំហាន 6: ដំឡើង Node.js និង npm (សម្រាប់កម្មវិធី Quiz)

កម្មវិធីសំនួរឡើងចាំបាច់ត្រូវការដំឡើង Node.js និង npm។

**Windows/macOS:**
- ទាញយកពី [nodejs.org](https://nodejs.org/) (ជ្រើសរើស LTS សម្រាប់អ្នកចាប់ផ្ដើម)
- ប្រតិបត្តិកម្មវិធីដំឡើង

**Linux:**
```bash
# Debian/Ubuntu
# ការព្រមាន៖ ការធ្វើបាញ់ script ពីអ៊ីនធើណិតចូលនៅក្នុង bash ប្លែកៗអាចមានហានិភ័យសុវត្ថិភាព។
# គួរតែពិនិត្យ script មុននឹងដំណើរការ៖
#   curl -fsSL https://deb.nodesource.com/setup_lts.x -o setup_lts.x
#   less setup_lts.x
# បន្ទាប់មករត់៖
#   sudo -E bash setup_lts.x
#
# ជាជម្រើសមួយ អ្នកអាចប្រើបន្ទាត់តែមួយខាងក្រោមដោយហានិភ័យផ្ទាល់ខ្លួន៖
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# Fedora
sudo dnf install nodejs

# បញ្ជាក់ការដំឡើង
node --version
npm --version
```

### ជំហាន 7: ដំឡើងចំណាំផ្នែក Quiz App

```bash
# ទៅកាន់ថតកម្មវិធីវាយបញ្ចូល
cd quiz-app

# ដំឡើងឧបករណ៍បន្ទាប់
npm install

# ត្រឡប់ទៅថតឫស
cd ..
```

### ជំហាន 8: ដំឡើង Docsify (ទៅលើវិធីបំពាះ)

សម្រាប់ចូលប្រើឯកសារបានក្រៅបណ្តាញ៖

```bash
npm install -g docsify-cli
```

## ពិនិត្យការដំឡើងរបស់អ្នក

### សាកល្បង Python និង Jupyter

```bash
# បើកបរិស្ថានវេររ៉ូរបស់អ្នក ប្រសិនបើមិនទាន់បើក
# នៅលើ Windows:
venv\Scripts\activate
# នៅលើ macOS/Linux:
source venv/bin/activate

# ចាប់ផ្តើម Jupyter Notebook
jupyter notebook
```

កម្មវិធីរុករករបស់អ្នកគួរតែបើកនូវចំណុចចូល Jupyter។ អ្នកអាចរុករកទៅឯកសារ `.ipynb` នៃម៉ូដែលណាមួយ។

### សាកល្បងកម្មវិធី Quiz

```bash
# បើកទៅកម្មវិធីសំណួរ
cd quiz-app

# ចាប់ផ្តើមម៉ាស៊ីនមេអភិវឌ្ឍន៍
npm run serve
```

កម្មវិធី Quiz គ្រាន់តែមាននៅ `http://localhost:8080` (ឬថែមទៀតដោយច្រកផ្សេងប្រសិនបើ 8080 ត្រូវបានប្រើប្រាស់)។

### សាកល្បងម៉ាស៊ីនបម្រើឯកសារ

```bash
# ចាប់ពីថតដើមនៃឃ្លាំងកូដ
docsify serve
```

ឯកសារគួរតែអាចប្រើបាននៅ `http://localhost:3000`។

## ប្រើ VS Code Dev Containers

ប្រសិនបើអ្នកមានការដំឡើង Docker អ្នកអាចប្រើ VS Code Dev Containers ដូចខាងក្រោម៖

1. ដំឡើង [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. ដំឡើង [Visual Studio Code](https://code.visualstudio.com/)
3. ដំឡើងកម្មវិធីបន្ថែម [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. បើក repository ក្នុង VS Code
5. ចុច `F1` ហើយជ្រើស "Remote-Containers: Reopen in Container"
6. រង់ចាំឲ្យកម្មវិធីកោនតឺន័របង្កើតចប់ (គ្រាន់តែដំណើរការក្នុងលើកដំបូងប៉ុណ្ណោះ)

## ជំហានបន្ទាប់

- ស្វែងយល់ពី [README.md](README.md) សម្រាប់មើលទិដ្ឋភាពទូទៅរបស់មេរៀន
- អាន [USAGE.md](USAGE.md) សម្រាប់ច្បាប់ប្រើប្រាស់ទូទៅ និងឧទាហរណ៍
- ពិនិត្យ [TROUBLESHOOTING.md](TROUBLESHOOTING.md) ប្រសិនបើអ្នកជួបបញ្ហា
- សំរាប់តំរូវចង់ចូលរួម អាន [CONTRIBUTING.md](CONTRIBUTING.md)

## ស្វែងរកជំនួយ

ប្រសិនបើអ្នកជួបបញ្ហា៖

1. ពិនិត្យមើលមគ្គុទេសក៍ [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. ស្វែងរកបញ្ហាមានស្រាប់នៅ [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. ចូលរួមក្នុងសហគមន៍ [Discord](https://aka.ms/ds4beginners/discord)
4. បង្កើតបញ្ហាថ្មីដោយមានព័ត៌មានលម្អិតអំពីបញ្ហារបស់អ្នក

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំរកភាពត្រឹមត្រូវ សូមយល់ថាការបកប្រែដោយស្វ័យប្រវត្តិក្នុងខ្លះអាចមានកំហុស ឬការខ្វះត្រូវបានខ្លះ។ ឯកសារដើមក្នុងភាសាដើមគួរត្រូវបានគេសម្លឹងជារុក្ខជាតិឯកសារដ៏មានសុពលភាព។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែនៅដោយមនុស្សជំនាញគឺត្រូវបានផ្ដល់អនុសាសន៍។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែបញ្ហាដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->