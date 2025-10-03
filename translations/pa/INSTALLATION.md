<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:18:50+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "pa"
}
-->
# ਇੰਸਟਾਲੇਸ਼ਨ ਗਾਈਡ

ਇਹ ਗਾਈਡ ਤੁਹਾਨੂੰ "ਡਾਟਾ ਸਾਇੰਸ ਫਾਰ ਬਿਗਿਨਰਜ਼" ਕੋਰਸ ਲਈ ਆਪਣਾ ਵਾਤਾਵਰਣ ਸੈਟਅਪ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰੇਗੀ।

## ਸਮੱਗਰੀ ਦੀ ਸੂਚੀ

- [ਪੂਰਵ ਸ਼ਰਤਾਂ](../..)
- [ਤੁਰੰਤ ਸ਼ੁਰੂਆਤ ਦੇ ਵਿਕਲਪ](../..)
- [ਲੋਕਲ ਇੰਸਟਾਲੇਸ਼ਨ](../..)
- [ਆਪਣੀ ਇੰਸਟਾਲੇਸ਼ਨ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ](../..)

## ਪੂਰਵ ਸ਼ਰਤਾਂ

ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਤੁਹਾਨੂੰ ਇਹਨਾਂ ਦੀ ਜਾਣਕਾਰੀ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ:

- ਕਮਾਂਡ ਲਾਈਨ/ਟਰਮੀਨਲ ਦੀ ਬੁਨਿਆਦੀ ਜਾਣਕਾਰੀ
- ਇੱਕ GitHub ਖਾਤਾ (ਮੁਫ਼ਤ)
- ਸ਼ੁਰੂਆਤੀ ਸੈਟਅਪ ਲਈ ਸਥਿਰ ਇੰਟਰਨੈਟ ਕਨੈਕਸ਼ਨ

## ਤੁਰੰਤ ਸ਼ੁਰੂਆਤ ਦੇ ਵਿਕਲਪ

### ਵਿਕਲਪ 1: GitHub Codespaces (ਨਵਾਂ ਸਿਖਣ ਵਾਲਿਆਂ ਲਈ ਸਿਫਾਰਸ਼ੀ)

ਸਭ ਤੋਂ ਆਸਾਨ ਤਰੀਕਾ GitHub Codespaces ਨਾਲ ਸ਼ੁਰੂ ਕਰਨਾ ਹੈ, ਜੋ ਤੁਹਾਡੇ ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਪੂਰਾ ਡਿਵੈਲਪਮੈਂਟ ਵਾਤਾਵਰਣ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

1. [ਰੇਪੋਜ਼ਟਰੀ](https://github.com/microsoft/Data-Science-For-Beginners) 'ਤੇ ਜਾਓ
2. **Code** ਡ੍ਰਾਪਡਾਊਨ ਮੀਨੂ 'ਤੇ ਕਲਿਕ ਕਰੋ
3. **Codespaces** ਟੈਬ ਚੁਣੋ
4. **Create codespace on main** 'ਤੇ ਕਲਿਕ ਕਰੋ
5. ਵਾਤਾਵਰਣ ਨੂੰ ਸ਼ੁਰੂ ਹੋਣ ਲਈ 2-3 ਮਿੰਟ ਦੀ ਉਡੀਕ ਕਰੋ

ਤੁਹਾਡਾ ਵਾਤਾਵਰਣ ਹੁਣ ਸਾਰੇ dependencies ਨਾਲ ਤਿਆਰ ਹੈ!

### ਵਿਕਲਪ 2: ਲੋਕਲ ਡਿਵੈਲਪਮੈਂਟ

ਆਪਣੇ ਕੰਪਿਊਟਰ 'ਤੇ ਕੰਮ ਕਰਨ ਲਈ, ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਵਿਸਥਾਰਵਾਦੀ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ।

## ਲੋਕਲ ਇੰਸਟਾਲੇਸ਼ਨ

### ਪਦਾਅਵਾਰ 1: Git ਇੰਸਟਾਲ ਕਰੋ

Git ਰੇਪੋਜ਼ਟਰੀ ਨੂੰ ਕਲੋਨ ਕਰਨ ਅਤੇ ਤੁਹਾਡੇ ਬਦਲਾਅ ਨੂੰ ਟ੍ਰੈਕ ਕਰਨ ਲਈ ਲੋੜੀਂਦਾ ਹੈ।

**Windows:**
- [git-scm.com](https://git-scm.com/download/win) ਤੋਂ ਡਾਊਨਲੋਡ ਕਰੋ
- ਡਿਫਾਲਟ ਸੈਟਿੰਗਾਂ ਨਾਲ ਇੰਸਟਾਲਰ ਚਲਾਓ

**macOS:**
- Homebrew ਰਾਹੀਂ ਇੰਸਟਾਲ ਕਰੋ: `brew install git`
- ਜਾਂ [git-scm.com](https://git-scm.com/download/mac) ਤੋਂ ਡਾਊਨਲੋਡ ਕਰੋ

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

### ਪਦਾਅਵਾਰ 2: ਰੇਪੋਜ਼ਟਰੀ ਕਲੋਨ ਕਰੋ

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### ਪਦਾਅਵਾਰ 3: Python ਅਤੇ Jupyter ਇੰਸਟਾਲ ਕਰੋ

ਡਾਟਾ ਸਾਇੰਸ ਪਾਠਾਂ ਲਈ Python 3.7 ਜਾਂ ਇਸ ਤੋਂ ਉੱਚਾ ਵਰਜਨ ਲੋੜੀਂਦਾ ਹੈ।

**Windows:**
1. [python.org](https://www.python.org/downloads/) ਤੋਂ Python ਡਾਊਨਲੋਡ ਕਰੋ
2. ਇੰਸਟਾਲੇਸ਼ਨ ਦੌਰਾਨ "Add Python to PATH" ਚੈੱਕ ਕਰੋ
3. ਇੰਸਟਾਲੇਸ਼ਨ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ:
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

### ਪਦਾਅਵਾਰ 4: Python ਵਾਤਾਵਰਣ ਸੈਟਅਪ ਕਰੋ

Dependencies ਨੂੰ ਅਲੱਗ ਰੱਖਣ ਲਈ ਇੱਕ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### ਪਦਾਅਵਾਰ 5: Python ਪੈਕੇਜ ਇੰਸਟਾਲ ਕਰੋ

ਲੋੜੀਂਦੇ ਡਾਟਾ ਸਾਇੰਸ ਲਾਇਬ੍ਰੇਰੀਜ਼ ਇੰਸਟਾਲ ਕਰੋ:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### ਪਦਾਅਵਾਰ 6: Node.js ਅਤੇ npm ਇੰਸਟਾਲ ਕਰੋ (ਕੁਇਜ਼ ਐਪ ਲਈ)

ਕੁਇਜ਼ ਐਪਲੀਕੇਸ਼ਨ ਲਈ Node.js ਅਤੇ npm ਦੀ ਲੋੜ ਹੈ।

**Windows/macOS:**
- [nodejs.org](https://nodejs.org/) ਤੋਂ ਡਾਊਨਲੋਡ ਕਰੋ (LTS ਵਰਜਨ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ)
- ਇੰਸਟਾਲਰ ਚਲਾਓ

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

### ਪਦਾਅਵਾਰ 7: ਕੁਇਜ਼ ਐਪ Dependencies ਇੰਸਟਾਲ ਕਰੋ

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### ਪਦਾਅਵਾਰ 8: Docsify ਇੰਸਟਾਲ ਕਰੋ (ਵਿਕਲਪਿਕ)

ਡਾਕੂਮੈਂਟੇਸ਼ਨ ਨੂੰ ਆਫਲਾਈਨ ਪਹੁੰਚ ਲਈ:

```bash
npm install -g docsify-cli
```

## ਆਪਣੀ ਇੰਸਟਾਲੇਸ਼ਨ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ

### Python ਅਤੇ Jupyter ਟੈਸਟ ਕਰੋ

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

ਤੁਹਾਡਾ ਬ੍ਰਾਊਜ਼ਰ Jupyter ਇੰਟਰਫੇਸ ਨਾਲ ਖੁਲ੍ਹਣਾ ਚਾਹੀਦਾ ਹੈ। ਹੁਣ ਤੁਸੀਂ ਕਿਸੇ ਵੀ ਪਾਠ ਦੇ `.ipynb` ਫਾਈਲ 'ਤੇ ਜਾ ਸਕਦੇ ਹੋ।

### ਕੁਇਜ਼ ਐਪਲੀਕੇਸ਼ਨ ਟੈਸਟ ਕਰੋ

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

ਕੁਇਜ਼ ਐਪ `http://localhost:8080` (ਜਾਂ ਜੇ 8080 ਬਿਜੀ ਹੈ ਤਾਂ ਹੋਰ ਪੋਰਟ) 'ਤੇ ਉਪਲਬਧ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।

### ਡਾਕੂਮੈਂਟੇਸ਼ਨ ਸਰਵਰ ਟੈਸਟ ਕਰੋ

```bash
# From the root directory of the repository
docsify serve
```

ਡਾਕੂਮੈਂਟੇਸ਼ਨ `http://localhost:3000` 'ਤੇ ਉਪਲਬਧ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।

## VS Code Dev Containers ਦੀ ਵਰਤੋਂ

ਜੇ ਤੁਹਾਡੇ ਕੋਲ Docker ਇੰਸਟਾਲ ਹੈ, ਤਾਂ ਤੁਸੀਂ VS Code Dev Containers ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ:

1. [Docker Desktop](https://www.docker.com/products/docker-desktop) ਇੰਸਟਾਲ ਕਰੋ
2. [Visual Studio Code](https://code.visualstudio.com/) ਇੰਸਟਾਲ ਕਰੋ
3. [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) ਇੰਸਟਾਲ ਕਰੋ
4. ਰੇਪੋਜ਼ਟਰੀ ਨੂੰ VS Code ਵਿੱਚ ਖੋਲ੍ਹੋ
5. `F1` ਦਬਾਓ ਅਤੇ "Remote-Containers: Reopen in Container" ਚੁਣੋ
6. ਕੰਟੇਨਰ ਨੂੰ ਬਣਨ ਲਈ ਉਡੀਕ ਕਰੋ (ਸਿਰਫ ਪਹਿਲੀ ਵਾਰ)

## ਅਗਲੇ ਕਦਮ

- ਕੋਰਸ ਦਾ ਜਾਇਜ਼ਾ ਲੈਣ ਲਈ [README.md](README.md) ਨੂੰ ਪੜ੍ਹੋ
- ਆਮ ਵਰਕਫਲੋ ਅਤੇ ਉਦਾਹਰਣਾਂ ਲਈ [USAGE.md](USAGE.md) ਨੂੰ ਪੜ੍ਹੋ
- ਜੇ ਤੁਸੀਂ ਸਮੱਸਿਆਵਾਂ ਦਾ ਸਾਹਮਣਾ ਕਰਦੇ ਹੋ ਤਾਂ [TROUBLESHOOTING.md](TROUBLESHOOTING.md) ਦੀ ਜਾਂਚ ਕਰੋ
- ਜੇ ਤੁਸੀਂ ਯੋਗਦਾਨ ਦੇਣਾ ਚਾਹੁੰਦੇ ਹੋ ਤਾਂ [CONTRIBUTING.md](CONTRIBUTING.md) ਦੀ ਸਮੀਖਿਆ ਕਰੋ

## ਮਦਦ ਪ੍ਰਾਪਤ ਕਰਨਾ

ਜੇ ਤੁਸੀਂ ਸਮੱਸਿਆਵਾਂ ਦਾ ਸਾਹਮਣਾ ਕਰਦੇ ਹੋ:

1. [TROUBLESHOOTING.md](TROUBLESHOOTING.md) ਗਾਈਡ ਦੀ ਜਾਂਚ ਕਰੋ
2. ਮੌਜੂਦਾ [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) ਨੂੰ ਖੋਜੋ
3. ਸਾਡੇ [Discord community](https://aka.ms/ds4beginners/discord) ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ
4. ਆਪਣੀ ਸਮੱਸਿਆ ਬਾਰੇ ਵਿਸਥਾਰਵਾਦੀ ਜਾਣਕਾਰੀ ਦੇ ਨਾਲ ਨਵਾਂ ਇਸ਼ੂ ਬਣਾਓ

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੱਜੇਪਣ ਹੋ ਸਕਦੇ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।