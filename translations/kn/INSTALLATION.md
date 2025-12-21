<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-12-19T13:13:01+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "kn"
}
-->
# ಸ್ಥಾಪನೆ ಮಾರ್ಗದರ್ಶಿ

ಈ ಮಾರ್ಗದರ್ಶಿ ನಿಮಗೆ Data Science for Beginners ಪಠ್ಯಕ್ರಮದೊಂದಿಗೆ ಕೆಲಸ ಮಾಡಲು ನಿಮ್ಮ ಪರಿಸರವನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.

## ವಿಷಯಗಳ ಪಟ್ಟಿಯು

- [ಪೂರ್ವಾಪೇಕ್ಷೆಗಳು](../..)
- [ತ್ವರಿತ ಪ್ರಾರಂಭ ಆಯ್ಕೆಗಳು](../..)
- [ಸ್ಥಳೀಯ ಸ್ಥಾಪನೆ](../..)
- [ನಿಮ್ಮ ಸ್ಥಾಪನೆಯನ್ನು ಪರಿಶೀಲಿಸಿ](../..)

## ಪೂರ್ವಾಪೇಕ್ಷೆಗಳು

ನೀವು ಪ್ರಾರಂಭಿಸುವ ಮೊದಲು, ನಿಮಗೆ ಇರಬೇಕು:

- ಕಮಾಂಡ್ ಲೈನ್/ಟರ್ಮಿನಲ್ ಬಗ್ಗೆ ಮೂಲ ಪರಿಚಯ
- GitHub ಖಾತೆ (ಉಚಿತ)
- ಪ್ರಾಥಮಿಕ ಸೆಟ್ ಅಪ್‌ಗಾಗಿ ಸ್ಥಿರ ಇಂಟರ್ನೆಟ್ ಸಂಪರ್ಕ

## ತ್ವರಿತ ಪ್ರಾರಂಭ ಆಯ್ಕೆಗಳು

### ಆಯ್ಕೆ 1: GitHub Codespaces (ಆರಂಭಿಕರಿಗೆ ಶಿಫಾರಸು)

ತ್ವರಿತವಾಗಿ ಪ್ರಾರಂಭಿಸುವ ಸುಲಭ ಮಾರ್ಗ GitHub Codespaces, ಇದು ನಿಮ್ಮ ಬ್ರೌಸರ್‌ನಲ್ಲಿ ಸಂಪೂರ್ಣ ಅಭಿವೃದ್ಧಿ ಪರಿಸರವನ್ನು ಒದಗಿಸುತ್ತದೆ.

1. [repository](https://github.com/microsoft/Data-Science-For-Beginners) ಗೆ ಹೋಗಿ
2. **Code** ಡ್ರಾಪ್‌ಡೌನ್ ಮೆನು ಕ್ಲಿಕ್ ಮಾಡಿ
3. **Codespaces** ಟ್ಯಾಬ್ ಆಯ್ಕೆಮಾಡಿ
4. **Create codespace on main** ಕ್ಲಿಕ್ ಮಾಡಿ
5. ಪರಿಸರ ಆರಂಭವಾಗಲು ಕಾಯಿರಿ (2-3 ನಿಮಿಷಗಳು)

ನಿಮ್ಮ ಪರಿಸರ ಈಗ ಎಲ್ಲಾ ಅವಲಂಬನೆಗಳೊಂದಿಗೆ ಸಿದ್ಧವಾಗಿದೆ!

### ಆಯ್ಕೆ 2: ಸ್ಥಳೀಯ ಅಭಿವೃದ್ಧಿ

ನಿಮ್ಮ ಸ್ವಂತ ಕಂಪ್ಯೂಟರ್‌ನಲ್ಲಿ ಕೆಲಸ ಮಾಡಲು, ಕೆಳಗಿನ ವಿವರವಾದ ಸೂಚನೆಗಳನ್ನು ಅನುಸರಿಸಿ.

## ಸ್ಥಳೀಯ ಸ್ಥಾಪನೆ

### ಹಂತ 1: Git ಅನ್ನು ಸ್ಥಾಪಿಸಿ

Git ಅನ್ನು ರೆಪೊಸಿಟರಿಯನ್ನು ಕ್ಲೋನ್ ಮಾಡಲು ಮತ್ತು ನಿಮ್ಮ ಬದಲಾವಣೆಗಳನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಲು ಅಗತ್ಯವಿದೆ.

**Windows:**
- [git-scm.com](https://git-scm.com/download/win) ನಿಂದ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ
- ಡೀಫಾಲ್ಟ್ ಸೆಟ್ಟಿಂಗ್‌ಗಳೊಂದಿಗೆ ಇನ್‌ಸ್ಟಾಲರ್ ಅನ್ನು ರನ್ ಮಾಡಿ

**macOS:**
- Homebrew ಮೂಲಕ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ: `brew install git`
- ಅಥವಾ [git-scm.com](https://git-scm.com/download/mac) ನಿಂದ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ

**Linux:**
```bash
# ಡೆಬಿಯನ್/ಉಬುಂಟು
sudo apt-get update
sudo apt-get install git

# ಫೆಡೋರಾ
sudo dnf install git

# ಆರ್ಚ್
sudo pacman -S git
```

### ಹಂತ 2: ರೆಪೊಸಿಟರಿಯನ್ನು ಕ್ಲೋನ್ ಮಾಡಿ

```bash
# ರೆಪೊಸಿಟರಿಯನ್ನು ಕ್ಲೋನ್ ಮಾಡಿ
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# ಡೈರೆಕ್ಟರಿಯ ಕಡೆಗೆ ನವಿಗೇಟ್ ಮಾಡಿ
cd Data-Science-For-Beginners
```

### ಹಂತ 3: Python ಮತ್ತು Jupyter ಅನ್ನು ಸ್ಥಾಪಿಸಿ

Python 3.7 ಅಥವಾ ಹೆಚ್ಚಿನ ಆವೃತ್ತಿ ಡೇಟಾ ಸೈನ್ಸ್ ಪಾಠಗಳಿಗೆ ಅಗತ್ಯವಿದೆ.

**Windows:**
1. [python.org](https://www.python.org/downloads/) ನಿಂದ Python ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ
2. ಸ್ಥಾಪನೆಯ ಸಮಯದಲ್ಲಿ "Add Python to PATH" ಅನ್ನು ಪರಿಶೀಲಿಸಿ
3. ಸ್ಥಾಪನೆಯನ್ನು ಪರಿಶೀಲಿಸಿ:
```bash
python --version
```

**macOS:**
```bash
# ಹೋಮ್‌ಬ್ರೂ ಬಳಸಿ
brew install python3

# ಸ್ಥಾಪನೆಯನ್ನು ಪರಿಶೀಲಿಸಿ
python3 --version
```

**Linux:**
```bash
# ಬಹುತೇಕ ಲಿನಕ್ಸ್ನ ವಿತರಣೆಗಳು ಪೈಥಾನ್ ಅನ್ನು ಪೂರ್ವಸ್ಥಾಪಿತವಾಗಿ ಹೊಂದಿವೆ
python3 --version

# ಸ್ಥಾಪಿಸಲಾಗದಿದ್ದರೆ:
# ಡೆಬಿಯನ್/ಉಬುಂಟು
sudo apt-get install python3 python3-pip

# ಫೆಡೋರಾ
sudo dnf install python3 python3-pip
```

### ಹಂತ 4: Python ಪರಿಸರವನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಿ

ಅವಲಂಬನೆಗಳನ್ನು ಪ್ರತ್ಯೇಕವಾಗಿ ಇಡಲು ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ಬಳಸಲು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ.

```bash
# ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ರಚಿಸಿ
python -m venv venv

# ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ
# ವಿಂಡೋಸ್‌ನಲ್ಲಿ:
venv\Scripts\activate

# ಮ್ಯಾಕ್‌ಒಎಸ್/ಲಿನಕ್ಸ್ನಲ್ಲಿ:
source venv/bin/activate
```

### ಹಂತ 5: Python ಪ್ಯಾಕೇಜುಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

ಅಗತ್ಯವಿರುವ ಡೇಟಾ ಸೈನ್ಸ್ ಲೈಬ್ರರಿಗಳನ್ನು ಸ್ಥಾಪಿಸಿ:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### ಹಂತ 6: Node.js ಮತ್ತು npm ಅನ್ನು ಸ್ಥಾಪಿಸಿ (Quiz ಅಪ್ಲಿಕೇಶನ್‌ಗಾಗಿ)

ಕ್ವಿಜ್ ಅಪ್ಲಿಕೇಶನ್‌ಗೆ Node.js ಮತ್ತು npm ಅಗತ್ಯವಿದೆ.

**Windows/macOS:**
- [nodejs.org](https://nodejs.org/) ನಿಂದ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ (LTS ಆವೃತ್ತಿ ಶಿಫಾರಸು)
- ಇನ್‌ಸ್ಟಾಲರ್ ಅನ್ನು ರನ್ ಮಾಡಿ

**Linux:**
```bash
# ಡೆಬಿಯನ್/ಉಬುಂಟು
# ಎಚ್ಚರಿಕೆ: ಇಂಟರ್ನೆಟ್‌ನಿಂದ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳನ್ನು ನೇರವಾಗಿ ಬಾಷ್‌ಗೆ ಪೈಪ್ ಮಾಡುವುದು ಭದ್ರತಾ ಅಪಾಯವಾಗಬಹುದು.
# ಸ್ಕ್ರಿಪ್ಟ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡುವ ಮೊದಲು ಪರಿಶೀಲಿಸುವುದು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ:
#   curl -fsSL https://deb.nodesource.com/setup_lts.x -o setup_lts.x
#   less setup_lts.x
# ನಂತರ ಚಾಲನೆ ಮಾಡಿ:
#   sudo -E bash setup_lts.x
#
# ಬದಲಾಗಿ, ಕೆಳಗಿನ ಒನ್-ಲೈನರ್ ಅನ್ನು ನಿಮ್ಮ ಸ್ವಂತ ಅಪಾಯದಲ್ಲಿ ಬಳಸಬಹುದು:
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# ಫೆಡೋರಾ
sudo dnf install nodejs

# ಸ್ಥಾಪನೆಯನ್ನು ಪರಿಶೀಲಿಸಿ
node --version
npm --version
```

### ಹಂತ 7: Quiz ಅಪ್ಲಿಕೇಶನ್ ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

```bash
# ಕ್ವಿಜ್ ಅಪ್ಲಿಕೇಶನ್ ಡೈರೆಕ್ಟರಿಗೆ ನ್ಯಾವಿಗೇಟ್ ಮಾಡಿ
cd quiz-app

# ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ
npm install

# ರೂಟ್ ಡೈರೆಕ್ಟರಿಗೆ ಮರಳಿ ಹೋಗಿ
cd ..
```

### ಹಂತ 8: Docsify ಅನ್ನು ಸ್ಥಾಪಿಸಿ (ಐಚ್ಛಿಕ)

ಡಾಕ್ಯುಮೆಂಟೇಶನ್‌ಗೆ ಆಫ್‌ಲೈನ್ ಪ್ರವೇಶಕ್ಕಾಗಿ:

```bash
npm install -g docsify-cli
```

## ನಿಮ್ಮ ಸ್ಥಾಪನೆಯನ್ನು ಪರಿಶೀಲಿಸಿ

### Python ಮತ್ತು Jupyter ಅನ್ನು ಪರೀಕ್ಷಿಸಿ

```bash
# ನಿಮ್ಮ ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ಈಗಾಗಲೇ ಸಕ್ರಿಯಗೊಳಿಸದಿದ್ದರೆ ಸಕ್ರಿಯಗೊಳಿಸಿ
# ವಿಂಡೋಸ್‌ನಲ್ಲಿ:
venv\Scripts\activate
# ಮ್ಯಾಕ್‌ಒಎಸ್/ಲಿನಕ್ಸ್ನಲ್ಲಿ:
source venv/bin/activate

# ಜುಪೈಟರ್ ನೋಟ್ಬುಕ್ ಪ್ರಾರಂಭಿಸಿ
jupyter notebook
```

ನಿಮ್ಮ ಬ್ರೌಸರ್ Jupyter ಇಂಟರ್ಫೇಸ್ ಅನ್ನು ತೆರೆಯಬೇಕು. ನೀವು ಈಗ ಯಾವುದೇ ಪಾಠದ `.ipynb` ಫೈಲ್‌ಗೆ ಹೋಗಬಹುದು.

### Quiz ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಪರೀಕ್ಷಿಸಿ

```bash
# ಕ್ವಿಜ್ ಅಪ್ಲಿಕೇಶನ್‌ಗೆ ನ್ಯಾವಿಗೇಟ್ ಮಾಡಿ
cd quiz-app

# ಅಭಿವೃದ್ಧಿ ಸರ್ವರ್ ಪ್ರಾರಂಭಿಸಿ
npm run serve
```

ಕ್ವಿಜ್ ಅಪ್ಲಿಕೇಶನ್ `http://localhost:8080` (ಅಥವಾ 8080 ಬ್ಯುಸಿ ಇದ್ದರೆ ಬೇರೆ ಪೋರ್ಟ್) ನಲ್ಲಿ ಲಭ್ಯವಿರಬೇಕು.

### ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ಸರ್ವರ್ ಅನ್ನು ಪರೀಕ್ಷಿಸಿ

```bash
# ಸಂಗ್ರಹಣೆಯ ಮೂಲ ಡೈರೆಕ್ಟರಿಯಿಂದ
docsify serve
```

ಡಾಕ್ಯುಮೆಂಟೇಶನ್ `http://localhost:3000` ನಲ್ಲಿ ಲಭ್ಯವಿರಬೇಕು.

## VS Code Dev Containers ಬಳಕೆ

ನೀವು Docker ಅನ್ನು ಸ್ಥಾಪಿಸಿಕೊಂಡಿದ್ದರೆ, ನೀವು VS Code Dev Containers ಅನ್ನು ಬಳಸಬಹುದು:

1. [Docker Desktop](https://www.docker.com/products/docker-desktop) ಅನ್ನು ಸ್ಥಾಪಿಸಿ
2. [Visual Studio Code](https://code.visualstudio.com/) ಅನ್ನು ಸ್ಥಾಪಿಸಿ
3. [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) ಅನ್ನು ಸ್ಥಾಪಿಸಿ
4. ರೆಪೊಸಿಟರಿಯನ್ನು VS Code ನಲ್ಲಿ ತೆರೆಯಿರಿ
5. `F1` ಒತ್ತಿ ಮತ್ತು "Remote-Containers: Reopen in Container" ಆಯ್ಕೆಮಾಡಿ
6. ಕಂಟೈನರ್ ನಿರ್ಮಾಣವಾಗಲು ಕಾಯಿರಿ (ಮೊದಲ ಬಾರಿ ಮಾತ್ರ)

## ಮುಂದಿನ ಹಂತಗಳು

- ಪಠ್ಯಕ್ರಮದ ಅವಲೋಕನಕ್ಕಾಗಿ [README.md](README.md) ಅನ್ನು ಅನ್ವೇಷಿಸಿ
- ಸಾಮಾನ್ಯ ಕಾರ್ಯಪ್ರವಾಹಗಳು ಮತ್ತು ಉದಾಹರಣೆಗಳಿಗಾಗಿ [USAGE.md](USAGE.md) ಓದಿ
- ಸಮಸ್ಯೆಗಳು ಎದುರಾದರೆ [TROUBLESHOOTING.md](TROUBLESHOOTING.md) ಪರಿಶೀಲಿಸಿ
- ಕೊಡುಗೆ ನೀಡಲು ಬಯಸಿದರೆ [CONTRIBUTING.md](CONTRIBUTING.md) ಪರಿಶೀಲಿಸಿ

## ಸಹಾಯ ಪಡೆಯುವುದು

ನೀವು ಸಮಸ್ಯೆಗಳನ್ನು ಎದುರಿಸಿದರೆ:

1. [TROUBLESHOOTING.md](TROUBLESHOOTING.md) ಮಾರ್ಗದರ್ಶಿಯನ್ನು ಪರಿಶೀಲಿಸಿ
2. ಇತ್ತೀಚಿನ [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) ಹುಡುಕಿ
3. ನಮ್ಮ [Discord ಸಮುದಾಯ](https://aka.ms/ds4beginners/discord) ಸೇರಿ
4. ನಿಮ್ಮ ಸಮಸ್ಯೆಯ ವಿವರಗಳೊಂದಿಗೆ ಹೊಸ issue ರಚಿಸಿ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯತ್ತ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->