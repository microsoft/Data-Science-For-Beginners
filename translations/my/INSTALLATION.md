<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:27:05+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "my"
}
-->
# တပ်ဆင်ရန်လမ်းညွှန်

ဒီလမ်းညွှန်က Data Science for Beginners သင်ခန်းစာများအတွက် သင့်ပတ်ဝန်းကျင်ကို စတင်ပြင်ဆင်ရန် ကူညီပေးပါမည်။

## အကြောင်းအရာများ

- [လိုအပ်ချက်များ](../..)
- [အမြန်စတင်ရန်ရွေးချယ်မှုများ](../..)
- [Local Installation](../..)
- [သင့်တပ်ဆင်မှုကို စစ်ဆေးပါ](../..)

## လိုအပ်ချက်များ

စတင်မလုပ်မီ သင့်တွင် အောက်ပါအရာများရှိရမည်။

- Command line/terminal ကို အခြေခံအသုံးပြုနိုင်မှု
- GitHub အကောင့် (အခမဲ့)
- စတင်ပြင်ဆင်မှုအတွက် တည်ငြိမ်သော အင်တာနက်ချိတ်ဆက်မှု

## အမြန်စတင်ရန်ရွေးချယ်မှုများ

### ရွေးချယ်မှု ၁: GitHub Codespaces (Beginner များအတွက် အကြံပြုသည်)

စတင်ရန် အလွယ်ဆုံးနည်းလမ်းမှာ GitHub Codespaces ကို အသုံးပြုခြင်းဖြစ်ပြီး၊ သင့်ဘရောက်ဇာတွင် အပြည့်အစုံသော ဖွံ့ဖြိုးရေးပတ်ဝန်းကျင်ကို ပေးစွမ်းပါသည်။

1. [repository](https://github.com/microsoft/Data-Science-For-Beginners) သို့ သွားပါ
2. **Code** dropdown menu ကို နှိပ်ပါ
3. **Codespaces** tab ကို ရွေးပါ
4. **Create codespace on main** ကို နှိပ်ပါ
5. ပတ်ဝန်းကျင်ကို စတင်ပြင်ဆင်ရန် (၂-၃ မိနစ်) စောင့်ပါ

Dependencies အားလုံးကို ကြိုတင်တပ်ဆင်ပြီး သင့်ပတ်ဝန်းကျင် အသင့်ဖြစ်နေပါပြီ!

### ရွေးချယ်မှု ၂: Local Development

သင့်ကိုယ်ပိုင်ကွန်ပျူတာပေါ်တွင် အလုပ်လုပ်ရန် အောက်ပါ အသေးစိတ်ညွှန်ကြားချက်များကို လိုက်နာပါ။

## Local Installation

### အဆင့် ၁: Git ကို တပ်ဆင်ပါ

Git သည် repository ကို clone လုပ်ရန်နှင့် သင့်ပြောင်းလဲမှုများကို ထိန်းသိမ်းရန် လိုအပ်သည်။

**Windows:**
- [git-scm.com](https://git-scm.com/download/win) မှ ဒေါင်းလုပ်ဆွဲပါ
- Installer ကို default settings ဖြင့် run လုပ်ပါ

**macOS:**
- Homebrew မှတဆင့် တပ်ဆင်ပါ: `brew install git`
- သို့မဟုတ် [git-scm.com](https://git-scm.com/download/mac) မှ ဒေါင်းလုပ်ဆွဲပါ

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

### အဆင့် ၂: Repository ကို Clone လုပ်ပါ

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### အဆင့် ၃: Python နှင့် Jupyter ကို တပ်ဆင်ပါ

Data science သင်ခန်းစာများအတွက် Python 3.7 သို့မဟုတ် အထက်ကို လိုအပ်သည်။

**Windows:**
1. [python.org](https://www.python.org/downloads/) မှ Python ကို ဒေါင်းလုပ်ဆွဲပါ
2. Installation လုပ်စဉ်တွင် "Add Python to PATH" ကို အမှန်ခြစ်ပါ
3. Installation ကို စစ်ဆေးပါ:
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

### အဆင့် ၄: Python Environment ကို ပြင်ဆင်ပါ

Dependencies များကို သီးသန့်ထားရန် virtual environment ကို အသုံးပြုရန် အကြံပြုပါသည်။

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### အဆင့် ၅: Python Packages များကို တပ်ဆင်ပါ

လိုအပ်သော data science libraries များကို တပ်ဆင်ပါ:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### အဆင့် ၆: Node.js နှင့် npm ကို တပ်ဆင်ပါ (Quiz App အတွက်)

Quiz application အတွက် Node.js နှင့် npm လိုအပ်သည်။

**Windows/macOS:**
- [nodejs.org](https://nodejs.org/) မှ ဒေါင်းလုပ်ဆွဲပါ (LTS version ကို အကြံပြုသည်)
- Installer ကို run လုပ်ပါ

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

### အဆင့် ၇: Quiz App Dependencies များကို တပ်ဆင်ပါ

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### အဆင့် ၈: Docsify ကို တပ်ဆင်ပါ (Optional)

Documentation ကို offline access ရရှိရန်:

```bash
npm install -g docsify-cli
```

## သင့်တပ်ဆင်မှုကို စစ်ဆေးပါ

### Python နှင့် Jupyter ကို စမ်းသပ်ပါ

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

သင့် browser သည် Jupyter interface ဖြင့် ဖွင့်လှစ်သင့်ပါသည်။ သင်သည် `.ipynb` ဖိုင်များကို သွားရောက်ကြည့်ရှုနိုင်ပါသည်။

### Quiz Application ကို စမ်းသပ်ပါ

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

Quiz app သည် `http://localhost:8080` (သို့မဟုတ် 8080 port အလုပ်မလုပ်ပါက အခြား port) တွင် ရရှိနိုင်သင့်ပါသည်။

### Documentation Server ကို စမ်းသပ်ပါ

```bash
# From the root directory of the repository
docsify serve
```

Documentation သည် `http://localhost:3000` တွင် ရရှိနိုင်သင့်ပါသည်။

## VS Code Dev Containers ကို အသုံးပြုခြင်း

Docker ကို တပ်ဆင်ထားပါက သင်သည် VS Code Dev Containers ကို အသုံးပြုနိုင်ပါသည်။

1. [Docker Desktop](https://www.docker.com/products/docker-desktop) ကို တပ်ဆင်ပါ
2. [Visual Studio Code](https://code.visualstudio.com/) ကို တပ်ဆင်ပါ
3. [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) ကို တပ်ဆင်ပါ
4. Repository ကို VS Code တွင် ဖွင့်ပါ
5. `F1` ကို နှိပ်ပြီး "Remote-Containers: Reopen in Container" ကို ရွေးပါ
6. Container ကို build လုပ်ရန် (ပထမဆုံးအကြိမ်) စောင့်ပါ

## နောက်တစ်ဆင့်များ

- သင်ခန်းစာများအကြောင်းအရာကို [README.md](README.md) တွင် ရှာဖွေပါ
- [USAGE.md](USAGE.md) ကို ဖွင့်ကြည့်ပြီး အလုပ်လုပ်ပုံများနှင့် ဥပမာများကို ဖတ်ရှုပါ
- ပြဿနာများရှိပါက [TROUBLESHOOTING.md](TROUBLESHOOTING.md) ကို ကြည့်ပါ
- အထောက်အကူပြုလိုပါက [CONTRIBUTING.md](CONTRIBUTING.md) ကို ဖတ်ရှုပါ

## အကူအညီရယူခြင်း

ပြဿနာများရှိပါက:

1. [TROUBLESHOOTING.md](TROUBLESHOOTING.md) လမ်းညွှန်ကို ကြည့်ပါ
2. ရှိပြီးသား [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) ကို ရှာဖွေပါ
3. [Discord community](https://aka.ms/ds4beginners/discord) တွင် ပါဝင်ပါ
4. သင့်ပြဿနာအကြောင်း အသေးစိတ်ဖြင့် အသစ်သော issue တစ်ခု ဖန်တီးပါ

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူလဘာသာစကားဖြင့် အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။