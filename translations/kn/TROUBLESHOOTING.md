<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-12-19T12:59:04+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "kn"
}
-->
# ಸಮಸ್ಯೆ ಪರಿಹಾರ ಮಾರ್ಗದರ್ಶಿ

ಈ ಮಾರ್ಗದರ್ಶಿ ಡೇಟಾ ಸೈನ್ಸ್ ಫಾರ್ ಬಿಗಿನರ್ಸ್ ಪಠ್ಯಕ್ರಮದೊಂದಿಗೆ ಕೆಲಸ ಮಾಡುವಾಗ ನೀವು ಎದುರಿಸಬಹುದಾದ ಸಾಮಾನ್ಯ ಸಮಸ್ಯೆಗಳಿಗೆ ಪರಿಹಾರಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ.

## ವಿಷಯಗಳ ಪಟ್ಟಿಯು

- [ಪೈಥಾನ್ ಮತ್ತು ಜುಪಿಟರ್ ಸಮಸ್ಯೆಗಳು](../..)
- [ಪ್ಯಾಕೇಜ್ ಮತ್ತು ಅವಲಂಬನೆ ಸಮಸ್ಯೆಗಳು](../..)
- [ಜುಪಿಟರ್ ನೋಟ್ಬುಕ್ ಸಮಸ್ಯೆಗಳು](../..)
- [ಕ್ವಿಜ್ ಅಪ್ಲಿಕೇಶನ್ ಸಮಸ್ಯೆಗಳು](../..)
- [ಗಿಟ್ ಮತ್ತು ಗಿಟ್‌ಹಬ್ ಸಮಸ್ಯೆಗಳು](../..)
- [ಡಾಕ್ಸಿಫೈ ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ಸಮಸ್ಯೆಗಳು](../..)
- [ಡೇಟಾ ಮತ್ತು ಫೈಲ್ ಸಮಸ್ಯೆಗಳು](../..)
- [ಕಾರ್ಯಕ್ಷಮತೆ ಸಮಸ್ಯೆಗಳು](../..)
- [ಹೆಚ್ಚಿನ ಸಹಾಯ ಪಡೆಯುವುದು](../..)

## ಪೈಥಾನ್ ಮತ್ತು ಜುಪಿಟರ್ ಸಮಸ್ಯೆಗಳು

### ಪೈಥಾನ್ ಕಂಡುಬರಲಿಲ್ಲ ಅಥವಾ ತಪ್ಪು ಆವೃತ್ತಿ

**ಸಮಸ್ಯೆ:** `python: command not found` ಅಥವಾ ತಪ್ಪು ಪೈಥಾನ್ ಆವೃತ್ತಿ

**ಪರಿಹಾರ:**

```bash
# ಪೈಥಾನ್ ಆವೃತ್ತಿಯನ್ನು ಪರಿಶೀಲಿಸಿ
python --version
python3 --version

# ಪೈಥಾನ್ 3 'python3' ಎಂದು ಸ್ಥಾಪಿತವಾಗಿದ್ದರೆ, ಒಂದು ಅಲಿಯಾಸ್ ರಚಿಸಿ
# macOS/Linux ನಲ್ಲಿ, ~/.bashrc ಅಥವಾ ~/.zshrc ಗೆ ಸೇರಿಸಿ:
alias python=python3
alias pip=pip3

# ಅಥವಾ python3 ಅನ್ನು ಸ್ಪಷ್ಟವಾಗಿ ಬಳಸಿ
python3 -m pip install jupyter
```

**ವಿಂಡೋಸ್ ಪರಿಹಾರ:**
1. [python.org](https://www.python.org/) ನಿಂದ ಪೈಥಾನ್ ಮರುಸ್ಥಾಪಿಸಿ
2. ಸ್ಥಾಪನೆಯಾಗುತ್ತಿರುವಾಗ, "Add Python to PATH" ಅನ್ನು ಪರಿಶೀಲಿಸಿ
3. ನಿಮ್ಮ ಟರ್ಮಿನಲ್/ಕಮಾಂಡ್ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಮರುಪ್ರಾರಂಭಿಸಿ

### ವರ್ಚುವಲ್ ಎನ್ವಿರಾನ್‌ಮೆಂಟ್ ಸಕ್ರಿಯಗೊಳಿಸುವ ಸಮಸ್ಯೆಗಳು

**ಸಮಸ್ಯೆ:** ವರ್ಚುವಲ್ ಎನ್ವಿರಾನ್‌ಮೆಂಟ್ ಸಕ್ರಿಯಗೊಳ್ಳುತ್ತಿಲ್ಲ

**ಪರಿಹಾರ:**

**ವಿಂಡೋಸ್:**
```bash
# ನೀವು ಕಾರ್ಯಗತಗೊಳಿಸುವ ನೀತಿ ದೋಷವನ್ನು ಪಡೆದರೆ
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# ನಂತರ ಸಕ್ರಿಯಗೊಳಿಸಿ
venv\Scripts\activate
```

**ಮ್ಯಾಕ್‌ಒಎಸ್/ಲಿನಕ್ಸ್ನಲ್ಲಿ:**
```bash
# ಸಕ್ರಿಯಗೊಳಿಸುವ ಸ್ಕ್ರಿಪ್ಟ್ ಕಾರ್ಯನಿರ್ವಹಣೀಯವಾಗಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ
chmod +x venv/bin/activate

# ನಂತರ ಸಕ್ರಿಯಗೊಳಿಸಿ
source venv/bin/activate
```

**ಸಕ್ರಿಯಗೊಳಿಸುವಿಕೆ ಪರಿಶೀಲಿಸಿ:**
```bash
# ನಿಮ್ಮ ಪ್ರಾಂಪ್ಟ್ (venv) ಅನ್ನು ತೋರಿಸಬೇಕು
# ಪೈಥಾನ್ ಸ್ಥಳವನ್ನು ಪರಿಶೀಲಿಸಿ
which python  # venv ಗೆ ಸೂಚಿಸಬೇಕು
```

### ಜುಪಿಟರ್ ಕರ್ಣಲ್ ಸಮಸ್ಯೆಗಳು

**ಸಮಸ್ಯೆ:** "Kernel not found" ಅಥವಾ "Kernel keeps dying"

**ಪರಿಹಾರ:**

```bash
# ಕರ್ಣಲ್ ಅನ್ನು ಮರುಸ್ಥಾಪಿಸಿ
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# ಅಥವಾ ಡೀಫಾಲ್ಟ್ ಕರ್ಣಲ್ ಅನ್ನು ಬಳಸಿ
python -m ipykernel install --user

# ಜುಪೈಟರ್ ಅನ್ನು ಮರುಪ್ರಾರಂಭಿಸಿ
jupyter notebook
```

**ಸಮಸ್ಯೆ:** ಜುಪಿಟರ್‌ನಲ್ಲಿ ತಪ್ಪು ಪೈಥಾನ್ ಆವೃತ್ತಿ

**ಪರಿಹಾರ:**
```bash
# ನಿಮ್ಮ ವರ್ಚುವಲ್ ಪರಿಸರದಲ್ಲಿ ಜುಪೈಟರ್ ಅನ್ನು ಸ್ಥಾಪಿಸಿ
source venv/bin/activate  # ಮೊದಲು ಸಕ್ರಿಯಗೊಳಿಸಿ
pip install jupyter ipykernel

# ಕರ್ಣಲ್ ಅನ್ನು ನೋಂದಣಿ ಮಾಡಿ
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# ಜುಪೈಟರ್‌ನಲ್ಲಿ, Kernel -> Change kernel -> Python (venv) ಆಯ್ಕೆಮಾಡಿ
```

## ಪ್ಯಾಕೇಜ್ ಮತ್ತು ಅವಲಂಬನೆ ಸಮಸ್ಯೆಗಳು

### ಆಮದು ದೋಷಗಳು

**ಸಮಸ್ಯೆ:** `ModuleNotFoundError: No module named 'pandas'` (ಅಥವಾ ಇತರ ಪ್ಯಾಕೇಜ್‌ಗಳು)

**ಪರಿಹಾರ:**

```bash
# ವರ್ಚುವಲ್ ಪರಿಸರ ಸಕ್ರಿಯವಾಗಿದೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # ವಿಂಡೋಸ್

# ಕಾಣೆಯಾದ ಪ್ಯಾಕೇಜ್ ಅನ್ನು ಸ್ಥಾಪಿಸಿ
pip install pandas

# ಎಲ್ಲಾ ಸಾಮಾನ್ಯ ಪ್ಯಾಕೇಜ್‌ಗಳನ್ನು ಸ್ಥಾಪಿಸಿ
pip install jupyter pandas numpy matplotlib seaborn scikit-learn

# ಸ್ಥಾಪನೆ ಪರಿಶೀಲಿಸಿ
python -c "import pandas; print(pandas.__version__)"
```

### ಪಿಪ್ ಸ್ಥಾಪನೆ ವಿಫಲತೆಗಳು

**ಸಮಸ್ಯೆ:** ಅನುಮತಿ ದೋಷಗಳೊಂದಿಗೆ `pip install` ವಿಫಲವಾಗಿದೆ

**ಪರಿಹಾರ:**

```bash
# --user ಧ್ವಜವನ್ನು ಬಳಸಿ
pip install --user package-name

# ಅಥವಾ ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ಬಳಸಿ (ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**ಸಮಸ್ಯೆ:** SSL ಪ್ರಮಾಣಪತ್ರ ದೋಷಗಳೊಂದಿಗೆ `pip install` ವಿಫಲವಾಗಿದೆ

**ಪರಿಹಾರ:**

```bash
# ಮೊದಲು ಪಿಪ್ ಅನ್ನು ನವೀಕರಿಸಿ
python -m pip install --upgrade pip

# ನಂಬಿಗಸ್ತ ಹೋಸ್ಟ್‌ನೊಂದಿಗೆ ಸ್ಥಾಪಿಸಲು ಪ್ರಯತ್ನಿಸಿ (ತಾತ್ಕಾಲಿಕ ಪರಿಹಾರ)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### ಪ್ಯಾಕೇಜ್ ಆವೃತ್ತಿ ಸಂಘರ್ಷಗಳು

**ಸಮಸ್ಯೆ:** ಅಸಂಗತ ಪ್ಯಾಕೇಜ್ ಆವೃತ್ತಿಗಳು

**ಪರಿಹಾರ:**

```bash
# ಹೊಸ ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ರಚಿಸಿ
python -m venv venv-new
source venv-new/bin/activate  # ಅಥವಾ ವಿಂಡೋಸ್‌ನಲ್ಲಿ venv-new\Scripts\activate

# ಅಗತ್ಯವಿದ್ದರೆ ನಿರ್ದಿಷ್ಟ ಆವೃತ್ತಿಗಳೊಂದಿಗೆ ಪ್ಯಾಕೇಜುಗಳನ್ನು ಸ್ಥಾಪಿಸಿ
pip install pandas==1.3.0
pip install numpy==1.21.0

# ಅಥವಾ pip ಗೆ ಅವಲಂಬನೆಗಳನ್ನು ಪರಿಹರಿಸಲು ಬಿಡಿ
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

## ಜುಪಿಟರ್ ನೋಟ್ಬುಕ್ ಸಮಸ್ಯೆಗಳು

### ಜುಪಿಟರ್ ಪ್ರಾರಂಭವಾಗುತ್ತಿಲ್ಲ

**ಸಮಸ್ಯೆ:** `jupyter notebook` ಕಮಾಂಡ್ ಕಂಡುಬರಲಿಲ್ಲ

**ಪರಿಹಾರ:**

```bash
# ಜುಪೈಟರ್ ಅನ್ನು ಸ್ಥಾಪಿಸಿ
pip install jupyter

# ಅಥವಾ python -m ಬಳಸಿ
python -m jupyter notebook

# ಅಗತ್ಯವಿದ್ದರೆ PATH ಗೆ ಸೇರಿಸಿ (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### ನೋಟ್ಬುಕ್ ಲೋಡ್ ಅಥವಾ ಉಳಿಸುವುದಿಲ್ಲ

**ಸಮಸ್ಯೆ:** "Notebook failed to load" ಅಥವಾ ಉಳಿಸುವ ದೋಷಗಳು

**ಪರಿಹಾರ:**

1. ಫೈಲ್ ಅನುಮತಿಗಳನ್ನು ಪರಿಶೀಲಿಸಿ
```bash
# ನೀವು ಬರೆಯಲು ಅನುಮತಿಗಳನ್ನು ಹೊಂದಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # ಅಗತ್ಯವಿದ್ದರೆ
```

2. ಫೈಲ್ ಹಾಳಾಗಿರುವುದಿಲ್ಲ ಎಂದು ಪರಿಶೀಲಿಸಿ
```bash
# JSON ರಚನೆಯನ್ನು ಪರಿಶೀಲಿಸಲು ಪಠ್ಯ ಸಂಪಾದಕದಲ್ಲಿ ತೆರೆಯಲು ಪ್ರಯತ್ನಿಸಿ
# ಹಾಳಾಗಿದ್ದರೆ ವಿಷಯವನ್ನು ಹೊಸ ನೋಟ್ಬುಕ್‌ಗೆ ನಕಲಿಸಿ
```

3. ಜುಪಿಟರ್ ಕ್ಯಾಶೆ ತೆರವುಗೊಳಿಸಿ
```bash
jupyter notebook --clear-cache
```

### ಸೆಲ್ ಕಾರ್ಯಗತಗೊಳ್ಳುತ್ತಿಲ್ಲ

**ಸಮಸ್ಯೆ:** ಸೆಲ್ "In [*]" ನಲ್ಲಿ ಅಂಟಿಕೊಂಡಿದೆ ಅಥವಾ ಬಹಳ ಸಮಯ ತೆಗೆದುಕೊಳ್ಳುತ್ತಿದೆ

**ಪರಿಹಾರ:**

1. **ಕರ್ಣಲ್ ಅನ್ನು ಮಧ್ಯಂತರಗೊಳಿಸಿ**: "Interrupt" ಬಟನ್ ಕ್ಲಿಕ್ ಮಾಡಿ ಅಥವಾ `I, I` ಒತ್ತಿ
2. **ಕರ್ಣಲ್ ಮರುಪ್ರಾರಂಭಿಸಿ**: Kernel ಮೆನು → Restart
3. ನಿಮ್ಮ ಕೋಡ್‌ನಲ್ಲಿ **ಅನಂತ ಲೂಪ್ಗಳಿಗಾಗಿ ಪರಿಶೀಲಿಸಿ**
4. **ಔಟ್‌ಪುಟ್ ತೆರವುಗೊಳಿಸಿ**: ಸೆಲ್ → All Output → Clear

### ಪ್ಲಾಟ್‌ಗಳು ಪ್ರದರ್ಶಿಸಲಾಗುತ್ತಿಲ್ಲ

**ಸಮಸ್ಯೆ:** `matplotlib` ಪ್ಲಾಟ್‌ಗಳು ನೋಟ್ಬುಕ್‌ನಲ್ಲಿ ತೋರಿಸುತ್ತಿಲ್ಲ

**ಪರಿಹಾರ:**

```python
# ನೋಟ್ಬುಕ್‌ನ ಮೇಲ್ಭಾಗದಲ್ಲಿ ಮಾಯಾಜಾಲ ಆಜ್ಞೆಯನ್ನು ಸೇರಿಸಿ
%matplotlib inline

import matplotlib.pyplot as plt

# ಚಿತ್ರ ರಚಿಸಿ
plt.plot([1, 2, 3, 4])
plt.show()  # show() ಅನ್ನು ಕರೆಮಾಡುವುದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ
```

**ಇಂಟರಾಕ್ಟಿವ್ ಪ್ಲಾಟ್‌ಗಳಿಗೆ ಪರ್ಯಾಯ:**
```python
%matplotlib notebook
# ಅಥವಾ
%matplotlib widget
```

## ಕ್ವಿಜ್ ಅಪ್ಲಿಕೇಶನ್ ಸಮಸ್ಯೆಗಳು

### npm install ವಿಫಲವಾಗಿದೆ

**ಸಮಸ್ಯೆ:** `npm install` ಸಮಯದಲ್ಲಿ ದೋಷಗಳು

**ಪರಿಹಾರ:**

```bash
# npm ಕ್ಯಾಶೆ ತೆರವುಗೊಳಿಸಿ
npm cache clean --force

# node_modules ಮತ್ತು package-lock.json ಅನ್ನು ತೆಗೆದುಹಾಕಿ
rm -rf node_modules package-lock.json

# ಮರುಸ್ಥಾಪಿಸಿ
npm install

# ಇನ್ನೂ ವಿಫಲವಾಗಿದ್ದರೆ, ಹಳೆಯ ಪಿಯರ್ ಡಿಪ್ಸ್ ಜೊತೆಗೆ ಪ್ರಯತ್ನಿಸಿ
npm install --legacy-peer-deps
```

### ಕ್ವಿಜ್ ಅಪ್ಲಿಕೇಶನ್ ಪ್ರಾರಂಭವಾಗುತ್ತಿಲ್ಲ

**ಸಮಸ್ಯೆ:** `npm run serve` ವಿಫಲವಾಗಿದೆ

**ಪರಿಹಾರ:**

```bash
# Node.js ಆವೃತ್ತಿಯನ್ನು ಪರಿಶೀಲಿಸಿ
node --version  # 12.x ಅಥವಾ ಅದಕ್ಕಿಂತ ಹೆಚ್ಚಿನದಾಗಿರಬೇಕು

# ಅವಲಂಬನೆಗಳನ್ನು ಮರುಸ್ಥಾಪಿಸಿ
cd quiz-app
rm -rf node_modules package-lock.json
npm install

# ವಿಭಿನ್ನ ಪೋರ್ಟ್ ಪ್ರಯತ್ನಿಸಿ
npm run serve -- --port 8081
```

### ಪೋರ್ಟ್ ಈಗಾಗಲೇ ಬಳಕೆಯಲ್ಲಿದೆ

**ಸಮಸ್ಯೆ:** "Port 8080 is already in use"

**ಪರಿಹಾರ:**

```bash
# 8080 ಪೋರ್ಟ್‌ನಲ್ಲಿ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಹುಡುಕಿ ಮತ್ತು ಕೊಲ್ಲಿರಿ
# macOS/Linux:
lsof -ti:8080 | xargs kill -9

# Windows:
netstat -ano | findstr :8080
taskkill /PID <PID> /F

# ಅಥವಾ ಬೇರೆ ಪೋರ್ಟ್ ಬಳಸಿ
npm run serve -- --port 8081
```

### ಕ್ವಿಜ್ ಲೋಡ್ ಆಗುತ್ತಿಲ್ಲ ಅಥವಾ ಖಾಲಿ ಪುಟ

**ಸಮಸ್ಯೆ:** ಕ್ವಿಜ್ ಅಪ್ಲಿಕೇಶನ್ ಲೋಡ್ ಆಗುತ್ತದೆ ಆದರೆ ಖಾಲಿ ಪುಟ ತೋರಿಸುತ್ತದೆ

**ಪರಿಹಾರ:**

1. ಬ್ರೌಸರ್ ಕಾನ್ಸೋಲ್‌ನಲ್ಲಿ ದೋಷಗಳನ್ನು ಪರಿಶೀಲಿಸಿ (F12)
2. ಬ್ರೌಸರ್ ಕ್ಯಾಶೆ ಮತ್ತು ಕುಕೀಸ್ ತೆರವುಗೊಳಿಸಿ
3. ಬೇರೆ ಬ್ರೌಸರ್ ಪ್ರಯತ್ನಿಸಿ
4. ಜಾವಾಸ್ಕ್ರಿಪ್ಟ್ ಸಕ್ರಿಯವಾಗಿದೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ
5. ಜಾಹೀರಾತು ತಡೆಗಟ್ಟುವವರನ್ನು ಪರಿಶೀಲಿಸಿ

```bash
# ಆಪ್ ಅನ್ನು ಮರುನಿರ್ಮಿಸಿ
npm run build
npm run serve
```

## ಗಿಟ್ ಮತ್ತು ಗಿಟ್‌ಹಬ್ ಸಮಸ್ಯೆಗಳು

### ಗಿಟ್ ಗುರುತಿಸಲಾಗುತ್ತಿಲ್ಲ

**ಸಮಸ್ಯೆ:** `git: command not found`

**ಪರಿಹಾರ:**

**ವಿಂಡೋಸ್:**
- [git-scm.com](https://git-scm.com/) ನಿಂದ ಗಿಟ್ ಅನ್ನು ಸ್ಥಾಪಿಸಿ
- ಸ್ಥಾಪನೆಯ ನಂತರ ಟರ್ಮಿನಲ್ ಮರುಪ್ರಾರಂಭಿಸಿ

**ಮ್ಯಾಕ್‌ಒಎಸ್:**

> **ಗಮನಿಸಿ:** ನೀವು ಹೋಮ್‌ಬ್ರೂ ಸ್ಥಾಪಿಸದಿದ್ದರೆ, ಮೊದಲು ಅದನ್ನು ಸ್ಥಾಪಿಸಲು [https://brew.sh/](https://brew.sh/) ನಲ್ಲಿ ಸೂಚನೆಗಳನ್ನು ಅನುಸರಿಸಿ.
```bash
# ಹೋಮ್‌ಬ್ರೂ ಮೂಲಕ ಸ್ಥಾಪಿಸಿ
brew install git

# ಅಥವಾ Xcode ಕಮಾಂಡ್ ಲೈನ್ ಟೂಲ್ಸ್ ಅನ್ನು ಸ್ಥಾಪಿಸಿ
xcode-select --install
```

**ಲಿನಕ್ಸ್ನಲ್ಲಿ:**
```bash
sudo apt-get install git  # ಡೆಬಿಯನ್/ಉಬುಂಟು
sudo dnf install git      # ಫೆಡೋರಾ
```

### ಕ್ಲೋನ್ ವಿಫಲವಾಗಿದೆ

**ಸಮಸ್ಯೆ:** `git clone` ಪ್ರಮಾಣೀಕರಣ ದೋಷಗಳೊಂದಿಗೆ ವಿಫಲವಾಗಿದೆ

**ಪರಿಹಾರ:**

```bash
# HTTPS URL ಅನ್ನು ಬಳಸಿ
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# ನೀವು GitHub ನಲ್ಲಿ 2FA ಸಕ್ರಿಯಗೊಳಿಸಿದ್ದರೆ, ವೈಯಕ್ತಿಕ ಪ್ರವೇಶ ಟೋಕನ್ ಅನ್ನು ಬಳಸಿ
# ಟೋಕನ್ ಅನ್ನು ರಚಿಸಿ: https://github.com/settings/tokens
# ಕೇಳಿದಾಗ ಪಾಸ್ವರ್ಡ್ ಆಗಿ ಟೋಕನ್ ಅನ್ನು ಬಳಸಿ
```

### ಅನುಮತಿ ನಿರಾಕರಿಸಲಾಗಿದೆ (publickey)

**ಸಮಸ್ಯೆ:** SSH ಕೀ ಪ್ರಮಾಣೀಕರಣ ವಿಫಲವಾಗಿದೆ

**ಪರಿಹಾರ:**

```bash
# SSH ಕೀ ರಚಿಸಿ
ssh-keygen -t ed25519 -C "your_email@example.com"

# ಕೀ ಅನ್ನು ssh-agent ಗೆ ಸೇರಿಸಿ
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# ಸಾರ್ವಜನಿಕ ಕೀ GitHub ಗೆ ಸೇರಿಸಿ
# ಕೀ ನಕಲಿಸಿ: cat ~/.ssh/id_ed25519.pub
# ಇಲ್ಲಿ ಸೇರಿಸಿ: https://github.com/settings/keys
```

## ಡಾಕ್ಸಿಫೈ ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ಸಮಸ್ಯೆಗಳು

### ಡಾಕ್ಸಿಫೈ ಕಮಾಂಡ್ ಕಂಡುಬರಲಿಲ್ಲ

**ಸಮಸ್ಯೆ:** `docsify: command not found`

**ಪರಿಹಾರ:**

```bash
# ಜಾಗತಿಕವಾಗಿ ಸ್ಥಾಪಿಸಿ
npm install -g docsify-cli

# macOS/Linux ನಲ್ಲಿ ಅನುಮತಿ ದೋಷ ಇದ್ದರೆ
sudo npm install -g docsify-cli

# ಸ್ಥಾಪನೆಯನ್ನು ಪರಿಶೀಲಿಸಿ
docsify --version

# ಇನ್ನೂ ಕಂಡುಬಂದಿಲ್ಲದಿದ್ದರೆ, npm ಜಾಗತಿಕ ಮಾರ್ಗವನ್ನು ಸೇರಿಸಿ
# npm ಜಾಗತಿಕ ಮಾರ್ಗವನ್ನು ಹುಡುಕಿ
npm config get prefix

# PATH ಗೆ ಸೇರಿಸಿ (~/.bashrc ಅಥವಾ ~/.zshrc ಗೆ ಸೇರಿಸಿ)
export PATH="$PATH:/usr/local/bin"
```

### ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ಲೋಡ್ ಆಗುತ್ತಿಲ್ಲ

**ಸಮಸ್ಯೆ:** ಡಾಕ್ಸಿಫೈ ಸೇವ್ ಮಾಡುತ್ತದೆ ಆದರೆ ವಿಷಯ ಲೋಡ್ ಆಗುವುದಿಲ್ಲ

**ಪರಿಹಾರ:**

```bash
# ನೀವು ರೆಪೊಸಿಟರಿ ರೂಟ್‌ನಲ್ಲಿ ಇದ್ದೀರಾ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ
cd Data-Science-For-Beginners

# index.html ಅನ್ನು ಪರಿಶೀಲಿಸಿ
ls index.html

# ನಿರ್ದಿಷ್ಟ ಪೋರ್ಟ್‌ನೊಂದಿಗೆ ಸೇವೆ ನೀಡಿ
docsify serve --port 3000

# ದೋಷಗಳಿಗಾಗಿ ಬ್ರೌಸರ್ ಕಾನ್ಸೋಲ್ ಪರಿಶೀಲಿಸಿ (F12)
```

### ಚಿತ್ರಗಳು ಪ್ರದರ್ಶಿಸಲಾಗುತ್ತಿಲ್ಲ

**ಸಮಸ್ಯೆ:** ಚಿತ್ರಗಳು ಮುರಿದ ಲಿಂಕ್ ಐಕಾನ್ ತೋರಿಸುತ್ತಿವೆ

**ಪರಿಹಾರ:**

1. ಚಿತ್ರ ಮಾರ್ಗಗಳು ಸಂಬಂಧಿತವಾಗಿವೆ ಎಂದು ಪರಿಶೀಲಿಸಿ
2. ಚಿತ್ರ ಫೈಲ್‌ಗಳು ರೆಪೊಸಿಟರಿಯಲ್ಲಿ ಇವೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ
3. ಬ್ರೌಸರ್ ಕ್ಯಾಶೆ ತೆರವುಗೊಳಿಸಿ
4. ಫೈಲ್ ವಿಸ್ತರಣೆಗಳು ಹೊಂದಿಕೆಯಾಗಿವೆ ಎಂದು ಪರಿಶೀಲಿಸಿ (ಕೆಲವು ವ್ಯವಸ್ಥೆಗಳಲ್ಲಿ ಕೇಸ್-ಸೆನ್ಸಿಟಿವ್)

## ಡೇಟಾ ಮತ್ತು ಫೈಲ್ ಸಮಸ್ಯೆಗಳು

### ಫೈಲ್ ಕಂಡುಬರದ ದೋಷಗಳು

**ಸಮಸ್ಯೆ:** ಡೇಟಾ ಲೋಡ್ ಮಾಡುವಾಗ `FileNotFoundError`

**ಪರಿಹಾರ:**

```python
import os

# ಪ್ರಸ್ತುತ ಕಾರ್ಯನಿರ್ವಹಣಾ ಡೈರೆಕ್ಟರಿಯನ್ನು ಪರಿಶೀಲಿಸಿ
print(os.getcwd())

# ಪೂರ್ಣ ಪಥವನ್ನು ಬಳಸಿ
data_path = os.path.join(os.getcwd(), 'data', 'filename.csv')
df = pd.read_csv(data_path)

# ಅಥವಾ ನೋಟ್ಬುಕ್ ಸ್ಥಳದಿಂದ ಸಂಬಂಧಿತ ಪಥವನ್ನು ಬಳಸಿ
df = pd.read_csv('../data/filename.csv')

# ಫೈಲ್ ಅಸ್ತಿತ್ವದಲ್ಲಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ
print(os.path.exists('data/filename.csv'))
```

### CSV ಓದುವ ದೋಷಗಳು

**ಸಮಸ್ಯೆ:** CSV ಫೈಲ್‌ಗಳನ್ನು ಓದುವಾಗ ದೋಷಗಳು

**ಪರಿಹಾರ:**

```python
import pandas as pd

# ವಿಭಿನ್ನ ಎನ್‌ಕೋಡಿಂಗ್‌ಗಳನ್ನು ಪ್ರಯತ್ನಿಸಿ
df = pd.read_csv('file.csv', encoding='utf-8')
# ಅಥವಾ
df = pd.read_csv('file.csv', encoding='latin-1')
# ಅಥವಾ
df = pd.read_csv('file.csv', encoding='ISO-8859-1')

# ಕಾಣೆಯಾದ ಮೌಲ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸಿ
df = pd.read_csv('file.csv', na_values=['NA', 'N/A', ''])

# ಕಾಮಾ ಅಲ್ಲದಿದ್ದರೆ ಡೆಲಿಮಿಟರ್ ಅನ್ನು ಸೂಚಿಸಿ
df = pd.read_csv('file.csv', delimiter=';')
```

### ದೊಡ್ಡ ಡೇಟಾಸೆಟ್‌ಗಳೊಂದಿಗೆ ಮೆಮೊರಿ ದೋಷಗಳು

**ಸಮಸ್ಯೆ:** ದೊಡ್ಡ ಫೈಲ್‌ಗಳನ್ನು ಲೋಡ್ ಮಾಡುವಾಗ `MemoryError`

**ಪರಿಹಾರ:**

```python
# ತುಂಡುಗಳಾಗಿ ಓದಿ
chunk_size = 10000
chunks = []
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # ತುಂಡನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಿ
    chunks.append(chunk)
df = pd.concat(chunks)

# ಅಥವಾ ನಿರ್ದಿಷ್ಟ ಕಾಲಮ್‌ಗಳನ್ನು ಮಾತ್ರ ಓದಿ
df = pd.read_csv('file.csv', usecols=['col1', 'col2'])

# ಹೆಚ್ಚು ಪರಿಣಾಮಕಾರಿಯಾದ ಡೇಟಾ ಪ್ರಕಾರಗಳನ್ನು ಬಳಸಿ
df = pd.read_csv('file.csv', dtype={'column_name': 'int32'})
```

## ಕಾರ್ಯಕ್ಷಮತೆ ಸಮಸ್ಯೆಗಳು

### ನೋಟ್ಬುಕ್ ನಿಧಾನ ಕಾರ್ಯಕ್ಷಮತೆ

**ಸಮಸ್ಯೆ:** ನೋಟ್ಬುಕ್‌ಗಳು ಬಹಳ ನಿಧಾನವಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತಿವೆ

**ಪರಿಹಾರ:**

1. **ಕರ್ಣಲ್ ಮರುಪ್ರಾರಂಭಿಸಿ ಮತ್ತು ಔಟ್‌ಪುಟ್ ತೆರವುಗೊಳಿಸಿ**
   - Kernel → Restart & Clear Output

2. **ಬಳಸದ ನೋಟ್ಬುಕ್‌ಗಳನ್ನು ಮುಚ್ಚಿ**

3. **ಕೋಡ್ ಅನ್ನು ಆಪ್ಟಿಮೈಸ್ ಮಾಡಿ:**
```python
# ಲೂಪ್ಗಳ ಬದಲು ವೆಕ್ಟರೈಜ್ಡ್ ಕಾರ್ಯಾಚರಣೆಗಳನ್ನು ಬಳಸಿ
# ಕೆಟ್ಟದು:
result = []
for x in data:
    result.append(x * 2)

# ಉತ್ತಮ:
result = data * 2  # ನಮ್‌ಪೈ/ಪಾಂಡಾಸ್ ವೆಕ್ಟರೈಜೆಷನ್
```

4. **ದೊಡ್ಡ ಡೇಟಾಸೆಟ್‌ಗಳ ಮಾದರಿಯನ್ನು ತೆಗೆದುಕೊಳ್ಳಿ:**
```python
# ಅಭಿವೃದ್ಧಿಯ ಸಮಯದಲ್ಲಿ ಮಾದರಿಯೊಂದಿಗೆ ಕೆಲಸ ಮಾಡಿ
df_sample = df.sample(n=1000)  # ಅಥವಾ df.head(1000)
```

### ಬ್ರೌಸರ್ ಕ್ರ್ಯಾಶ್ ಆಗುವುದು

**ಸಮಸ್ಯೆ:** ಬ್ರೌಸರ್ ಕ್ರ್ಯಾಶ್ ಆಗುತ್ತದೆ ಅಥವಾ ಪ್ರತಿಕ್ರಿಯೆ ನೀಡುವುದಿಲ್ಲ

**ಪರಿಹಾರ:**

1. ಬಳಸದ ಟ್ಯಾಬ್‌ಗಳನ್ನು ಮುಚ್ಚಿ
2. ಬ್ರೌಸರ್ ಕ್ಯಾಶೆ ತೆರವುಗೊಳಿಸಿ
3. ಬ್ರೌಸರ್ ಮೆಮೊರಿ ಹೆಚ್ಚಿಸಿ (ಕ್ರೋಮ್: `chrome://settings/system`)
4. ಜುಪಿಟರ್‌ಲ್ಯಾಬ್ ಬಳಸಿ:
```bash
pip install jupyterlab
jupyter lab
```

## ಹೆಚ್ಚುವರಿ ಸಹಾಯ ಪಡೆಯುವುದು

### ಸಹಾಯ ಕೇಳುವ ಮೊದಲು

1. ಈ ಸಮಸ್ಯೆ ಪರಿಹಾರ ಮಾರ್ಗದರ್ಶಿಯನ್ನು ಪರಿಶೀಲಿಸಿ
2. [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues) ನಲ್ಲಿ ಹುಡುಕಿ
3. [INSTALLATION.md](INSTALLATION.md) ಮತ್ತು [USAGE.md](USAGE.md) ಪರಿಶೀಲಿಸಿ
4. ದೋಷ ಸಂದೇಶವನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಹುಡುಕಿ

### ಸಹಾಯ ಕೇಳುವುದು ಹೇಗೆ

ಸಮಸ್ಯೆ ಸೃಷ್ಟಿಸುವಾಗ ಅಥವಾ ಸಹಾಯ ಕೇಳುವಾಗ, ಈ ಮಾಹಿತಿಯನ್ನು ಸೇರಿಸಿ:

1. **ಆಪರೇಟಿಂಗ್ ಸಿಸ್ಟಮ್**: ವಿಂಡೋಸ್, ಮ್ಯಾಕ್‌ಒಎಸ್ ಅಥವಾ ಲಿನಕ್ಸ್ (ಯಾವ ಡಿಸ್ಟ್ರಿಬ್ಯೂಷನ್)
2. **ಪೈಥಾನ್ ಆವೃತ್ತಿ**: `python --version` ಅನ್ನು ರನ್ ಮಾಡಿ
3. **ದೋಷ ಸಂದೇಶ**: ಸಂಪೂರ್ಣ ದೋಷ ಸಂದೇಶವನ್ನು ನಕಲಿಸಿ
4. **ಪುನರಾವರ್ತಿಸುವ ಹಂತಗಳು**: ದೋಷ ಸಂಭವಿಸುವ ಮೊದಲು ನೀವು ಏನು ಮಾಡಿದ್ದೀರಿ
5. **ನೀವು ಪ್ರಯತ್ನಿಸಿದವು**: ನೀವು ಈಗಾಗಲೇ ಪ್ರಯತ್ನಿಸಿದ ಪರಿಹಾರಗಳು

**ಉದಾಹರಣೆ:**
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

### ಸಮುದಾಯ ಸಂಪನ್ಮೂಲಗಳು

- **GitHub Issues**: [ಸಮಸ್ಯೆ ಸೃಷ್ಟಿಸಿ](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [ನಮ್ಮ ಸಮುದಾಯದಲ್ಲಿ ಸೇರಿ](https://aka.ms/ds4beginners/discord)
- **ಚರ್ಚೆಗಳು**: [GitHub Discussions](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [ಪ್ರಶ್ನೋತ್ತರ ವೇದಿಕೆಗಳು](https://docs.microsoft.com/answers/)

### ಸಂಬಂಧಿತ ಡಾಕ್ಯುಮೆಂಟೇಶನ್

- [INSTALLATION.md](INSTALLATION.md) - ಸ್ಥಾಪನೆ ಸೂಚನೆಗಳು
- [USAGE.md](USAGE.md) - ಪಠ್ಯಕ್ರಮವನ್ನು ಹೇಗೆ ಬಳಸುವುದು
- [CONTRIBUTING.md](CONTRIBUTING.md) - ಹೇಗೆ ಕೊಡುಗೆ ನೀಡುವುದು
- [README.md](README.md) - ಯೋಜನೆಯ ಅವಲೋಕನ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->