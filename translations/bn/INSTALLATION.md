<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:17:50+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "bn"
}
-->
# ইনস্টলেশন গাইড

এই গাইডটি আপনাকে Data Science for Beginners কারিকুলামের জন্য আপনার পরিবেশ সেট আপ করতে সাহায্য করবে।

## সূচিপত্র

- [প্রয়োজনীয়তা](../..)
- [দ্রুত শুরু করার বিকল্প](../..)
- [লোকাল ইনস্টলেশন](../..)
- [আপনার ইনস্টলেশন যাচাই করুন](../..)

## প্রয়োজনীয়তা

শুরু করার আগে আপনার যা থাকা উচিত:

- কমান্ড লাইন/টার্মিনালের সাথে মৌলিক পরিচিতি
- একটি GitHub অ্যাকাউন্ট (ফ্রি)
- প্রাথমিক সেটআপের জন্য স্থিতিশীল ইন্টারনেট সংযোগ

## দ্রুত শুরু করার বিকল্প

### বিকল্প ১: GitHub Codespaces (শুরুকারীদের জন্য সুপারিশকৃত)

শুরু করার সবচেয়ে সহজ উপায় হল GitHub Codespaces ব্যবহার করা, যা আপনার ব্রাউজারে একটি সম্পূর্ণ ডেভেলপমেন্ট পরিবেশ প্রদান করে।

1. [রিপোজিটরি](https://github.com/microsoft/Data-Science-For-Beginners) এ যান
2. **Code** ড্রপডাউন মেনুতে ক্লিক করুন
3. **Codespaces** ট্যাব নির্বাচন করুন
4. **Create codespace on main** এ ক্লিক করুন
5. পরিবেশটি ইনিশিয়ালাইজ হওয়ার জন্য অপেক্ষা করুন (২-৩ মিনিট)

আপনার পরিবেশ এখন সমস্ত ডিপেনডেন্সি প্রি-ইনস্টলড অবস্থায় প্রস্তুত!

### বিকল্প ২: লোকাল ডেভেলপমেন্ট

আপনার নিজের কম্পিউটারে কাজ করার জন্য নিচের বিস্তারিত নির্দেশনা অনুসরণ করুন।

## লোকাল ইনস্টলেশন

### ধাপ ১: Git ইনস্টল করুন

রিপোজিটরি ক্লোন করতে এবং আপনার পরিবর্তনগুলি ট্র্যাক করতে Git প্রয়োজন।

**Windows:**
- [git-scm.com](https://git-scm.com/download/win) থেকে ডাউনলোড করুন
- ডিফল্ট সেটিংস দিয়ে ইনস্টলার চালান

**macOS:**
- Homebrew ব্যবহার করে ইনস্টল করুন: `brew install git`
- অথবা [git-scm.com](https://git-scm.com/download/mac) থেকে ডাউনলোড করুন

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

### ধাপ ২: রিপোজিটরি ক্লোন করুন

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### ধাপ ৩: Python এবং Jupyter ইনস্টল করুন

ডেটা সায়েন্স লেসনের জন্য Python 3.7 বা তার বেশি প্রয়োজন।

**Windows:**
1. [python.org](https://www.python.org/downloads/) থেকে Python ডাউনলোড করুন
2. ইনস্টলেশনের সময় "Add Python to PATH" চেক করুন
3. ইনস্টলেশন যাচাই করুন:
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

### ধাপ ৪: Python পরিবেশ সেট আপ করুন

ডিপেনডেন্সিগুলি আলাদা রাখতে ভার্চুয়াল পরিবেশ ব্যবহার করার সুপারিশ করা হয়।

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### ধাপ ৫: Python প্যাকেজ ইনস্টল করুন

প্রয়োজনীয় ডেটা সায়েন্স লাইব্রেরিগুলি ইনস্টল করুন:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### ধাপ ৬: Node.js এবং npm ইনস্টল করুন (কুইজ অ্যাপের জন্য)

কুইজ অ্যাপ্লিকেশনের জন্য Node.js এবং npm প্রয়োজন।

**Windows/macOS:**
- [nodejs.org](https://nodejs.org/) থেকে ডাউনলোড করুন (LTS সংস্করণ সুপারিশকৃত)
- ইনস্টলার চালান

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

### ধাপ ৭: কুইজ অ্যাপ ডিপেনডেন্সি ইনস্টল করুন

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### ধাপ ৮: Docsify ইনস্টল করুন (ঐচ্ছিক)

ডকুমেন্টেশনের অফলাইন অ্যাক্সেসের জন্য:

```bash
npm install -g docsify-cli
```

## আপনার ইনস্টলেশন যাচাই করুন

### Python এবং Jupyter পরীক্ষা করুন

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

আপনার ব্রাউজারটি Jupyter ইন্টারফেস সহ খুলবে। এখন আপনি যেকোনো লেসনের `.ipynb` ফাইল নেভিগেট করতে পারেন।

### কুইজ অ্যাপ্লিকেশন পরীক্ষা করুন

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

কুইজ অ্যাপটি `http://localhost:8080` (অথবা যদি 8080 ব্যস্ত থাকে তবে অন্য পোর্টে) উপলব্ধ হওয়া উচিত।

### ডকুমেন্টেশন সার্ভার পরীক্ষা করুন

```bash
# From the root directory of the repository
docsify serve
```

ডকুমেন্টেশনটি `http://localhost:3000` এ উপলব্ধ হওয়া উচিত।

## VS Code Dev Containers ব্যবহার করা

যদি আপনার Docker ইনস্টল করা থাকে, আপনি VS Code Dev Containers ব্যবহার করতে পারেন:

1. [Docker Desktop](https://www.docker.com/products/docker-desktop) ইনস্টল করুন
2. [Visual Studio Code](https://code.visualstudio.com/) ইনস্টল করুন
3. [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) ইনস্টল করুন
4. রিপোজিটরি VS Code-এ খুলুন
5. `F1` চাপুন এবং "Remote-Containers: Reopen in Container" নির্বাচন করুন
6. কন্টেইনারটি তৈরি হওয়ার জন্য অপেক্ষা করুন (শুধুমাত্র প্রথমবার)

## পরবর্তী পদক্ষেপ

- কারিকুলামের ওভারভিউয়ের জন্য [README.md](README.md) অন্বেষণ করুন
- সাধারণ ওয়ার্কফ্লো এবং উদাহরণের জন্য [USAGE.md](USAGE.md) পড়ুন
- যদি কোনো সমস্যা হয় তবে [TROUBLESHOOTING.md](TROUBLESHOOTING.md) পরীক্ষা করুন
- অবদান রাখতে চাইলে [CONTRIBUTING.md](CONTRIBUTING.md) পর্যালোচনা করুন

## সাহায্য পাওয়া

যদি কোনো সমস্যা হয়:

1. [TROUBLESHOOTING.md](TROUBLESHOOTING.md) গাইড পরীক্ষা করুন
2. বিদ্যমান [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) অনুসন্ধান করুন
3. আমাদের [Discord কমিউনিটি](https://aka.ms/ds4beginners/discord) এ যোগ দিন
4. আপনার সমস্যার বিস্তারিত তথ্য সহ একটি নতুন ইস্যু তৈরি করুন

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতা নিশ্চিত করার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।