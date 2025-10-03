<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93a6a8a8a209128cbfedcbc076ee21b0",
  "translation_date": "2025-10-03T15:42:55+00:00",
  "source_file": "TROUBLESHOOTING.md",
  "language_code": "he"
}
-->
# מדריך לפתרון בעיות

מדריך זה מספק פתרונות לבעיות נפוצות שעשויות להתרחש בעת עבודה עם תוכנית הלימודים "מדעי הנתונים למתחילים".

## תוכן עניינים

- [בעיות Python ו-Jupyter](../..)
- [בעיות חבילות ותלויות](../..)
- [בעיות במחברת Jupyter](../..)
- [בעיות באפליקציית השאלונים](../..)
- [בעיות Git ו-GitHub](../..)
- [בעיות תיעוד Docsify](../..)
- [בעיות נתונים וקבצים](../..)
- [בעיות ביצועים](../..)
- [קבלת עזרה נוספת](../..)

## בעיות Python ו-Jupyter

### Python לא נמצא או גרסה שגויה

**בעיה:** `python: command not found` או גרסת Python שגויה

**פתרון:**

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

**פתרון ל-Windows:**
1. התקן מחדש את Python מ-[python.org](https://www.python.org/)
2. במהלך ההתקנה, סמן "Add Python to PATH"
3. הפעל מחדש את הטרמינל/שורת הפקודה

### בעיות בהפעלת סביבה וירטואלית

**בעיה:** הסביבה הווירטואלית לא מופעלת

**פתרון:**

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

**אימות הפעלה:**
```bash
# Your prompt should show (venv)
# Check Python location
which python  # Should point to venv
```

### בעיות Kernel ב-Jupyter

**בעיה:** "Kernel לא נמצא" או "Kernel ממשיך לקרוס"

**פתרון:**

```bash
# Reinstall kernel
python -m ipykernel install --user --name=datascience --display-name="Python (Data Science)"

# Or use the default kernel
python -m ipykernel install --user

# Restart Jupyter
jupyter notebook
```

**בעיה:** גרסת Python שגויה ב-Jupyter

**פתרון:**
```bash
# Install Jupyter in your virtual environment
source venv/bin/activate  # Activate first
pip install jupyter ipykernel

# Register the kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"

# In Jupyter, select Kernel -> Change kernel -> Python (venv)
```

## בעיות חבילות ותלויות

### שגיאות ייבוא

**בעיה:** `ModuleNotFoundError: No module named 'pandas'` (או חבילות אחרות)

**פתרון:**

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

### כשלי התקנה של pip

**בעיה:** `pip install` נכשל עם שגיאות הרשאה

**פתרון:**

```bash
# Use --user flag
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

**בעיה:** `pip install` נכשל עם שגיאות תעודת SSL

**פתרון:**

```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing with trusted host (temporary workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### קונפליקטים בין גרסאות חבילות

**בעיה:** גרסאות חבילות לא תואמות

**פתרון:**

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

## בעיות במחברת Jupyter

### Jupyter לא מופעל

**בעיה:** הפקודה `jupyter notebook` לא נמצאה

**פתרון:**

```bash
# Install Jupyter
pip install jupyter

# Or use python -m
python -m jupyter notebook

# Add to PATH if needed (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

### המחברת לא נטענת או לא נשמרת

**בעיה:** "Notebook failed to load" או שגיאות שמירה

**פתרון:**

1. בדוק הרשאות קבצים
```bash
# Make sure you have write permissions
ls -l notebook.ipynb
chmod 644 notebook.ipynb  # If needed
```

2. בדוק אם הקובץ פגום
```bash
# Try opening in text editor to check JSON structure
# Copy content to new notebook if corrupted
```

3. נקה את המטמון של Jupyter
```bash
jupyter notebook --clear-cache
```

### תא לא מבוצע

**בעיה:** תא תקוע על "In [*]" או לוקח זמן רב מדי

**פתרון:**

1. **הפסק את ה-Kernel**: לחץ על כפתור "Interrupt" או לחץ `I, I`
2. **הפעל מחדש את ה-Kernel**: תפריט Kernel → Restart
3. **בדוק לולאות אינסופיות** בקוד שלך
4. **נקה פלט**: Cell → All Output → Clear

### גרפים לא מוצגים

**בעיה:** גרפי `matplotlib` לא מוצגים במחברת

**פתרון:**

```python
# Add magic command at the top of notebook
%matplotlib inline

import matplotlib.pyplot as plt

# Create plot
plt.plot([1, 2, 3, 4])
plt.show()  # Make sure to call show()
```

**חלופה לגרפים אינטראקטיביים:**
```python
%matplotlib notebook
# Or
%matplotlib widget
```

## בעיות באפליקציית השאלונים

### npm install נכשל

**בעיה:** שגיאות במהלך `npm install`

**פתרון:**

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

### אפליקציית השאלונים לא מופעלת

**בעיה:** `npm run serve` נכשל

**פתרון:**

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

### פורט כבר בשימוש

**בעיה:** "Port 8080 is already in use"

**פתרון:**

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

### שאלון לא נטען או דף ריק

**בעיה:** אפליקציית השאלונים נטענת אך מציגה דף ריק

**פתרון:**

1. בדוק שגיאות בקונסול של הדפדפן (F12)
2. נקה מטמון ועוגיות בדפדפן
3. נסה דפדפן אחר
4. ודא ש-JavaScript מופעל
5. בדוק אם חסמי פרסומות מפריעים

```bash
# Rebuild the app
npm run build
npm run serve
```

## בעיות Git ו-GitHub

### Git לא מזוהה

**בעיה:** `git: command not found`

**פתרון:**

**Windows:**
- התקן Git מ-[git-scm.com](https://git-scm.com/)
- הפעל מחדש את הטרמינל לאחר ההתקנה

**macOS:**

> **הערה:** אם Homebrew לא מותקן, עקוב אחר ההוראות ב-[https://brew.sh/](https://brew.sh/) להתקנה.
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

### כשלי שיבוט

**בעיה:** `git clone` נכשל עם שגיאות אימות

**פתרון:**

```bash
# Use HTTPS URL
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# If you have 2FA enabled on GitHub, use Personal Access Token
# Create token at: https://github.com/settings/tokens
# Use token as password when prompted
```

### הרשאה נדחתה (publickey)

**בעיה:** אימות מפתח SSH נכשל

**פתרון:**

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

## בעיות תיעוד Docsify

### פקודת Docsify לא נמצאה

**בעיה:** `docsify: command not found`

**פתרון:**

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

### התיעוד לא נטען

**בעיה:** Docsify מופעל אך התוכן לא נטען

**פתרון:**

```bash
# Ensure you're in the repository root
cd Data-Science-For-Beginners

# Check for index.html
ls index.html

# Serve with specific port
docsify serve --port 3000

# Check browser console for errors (F12)
```

### תמונות לא מוצגות

**בעיה:** תמונות מציגות אייקון קישור שבור

**פתרון:**

1. בדוק שהנתיבים לתמונות יחסיים
2. ודא שקבצי התמונות קיימים במאגר
3. נקה מטמון בדפדפן
4. בדוק שהסיומות תואמות (רגישות לאותיות במערכות מסוימות)

## בעיות נתונים וקבצים

### שגיאות קובץ לא נמצא

**בעיה:** `FileNotFoundError` בעת טעינת נתונים

**פתרון:**

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

### שגיאות קריאה של CSV

**בעיה:** שגיאות בקריאת קבצי CSV

**פתרון:**

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

### שגיאות זיכרון עם מערכי נתונים גדולים

**בעיה:** `MemoryError` בעת טעינת קבצים גדולים

**פתרון:**

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

## בעיות ביצועים

### ביצועים איטיים במחברת

**בעיה:** מחברות פועלות באיטיות רבה

**פתרון:**

1. **הפעל מחדש את ה-Kernel ונקה פלט**
   - Kernel → Restart & Clear Output

2. **סגור מחברות לא בשימוש**

3. **ייעל את הקוד:**
```python
# Use vectorized operations instead of loops
# Bad:
result = []
for x in data:
    result.append(x * 2)

# Good:
result = data * 2  # NumPy/Pandas vectorization
```

4. **דגום מערכי נתונים גדולים:**
```python
# Work with sample during development
df_sample = df.sample(n=1000)  # or df.head(1000)
```

### קריסות דפדפן

**בעיה:** הדפדפן קורס או הופך ללא מגיב

**פתרון:**

1. סגור כרטיסיות לא בשימוש
2. נקה מטמון בדפדפן
3. הגדל את זיכרון הדפדפן (Chrome: `chrome://settings/system`)
4. השתמש ב-JupyterLab במקום:
```bash
pip install jupyterlab
jupyter lab
```

## קבלת עזרה נוספת

### לפני בקשת עזרה

1. בדוק את מדריך פתרון הבעיות הזה
2. חפש [בעיות ב-GitHub](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. עיין ב-[INSTALLATION.md](INSTALLATION.md) וב-[USAGE.md](USAGE.md)
4. נסה לחפש את הודעת השגיאה באינטרנט

### איך לבקש עזרה

כאשר יוצרים בעיה או מבקשים עזרה, כלול:

1. **מערכת הפעלה**: Windows, macOS או Linux (איזו הפצה)
2. **גרסת Python**: הפעל `python --version`
3. **הודעת שגיאה**: העתק את הודעת השגיאה המלאה
4. **שלבים לשחזור**: מה עשית לפני שהשגיאה התרחשה
5. **מה ניסית**: פתרונות שכבר ניסית

**דוגמה:**
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

### משאבי קהילה

- **בעיות ב-GitHub**: [צור בעיה](https://github.com/microsoft/Data-Science-For-Beginners/issues/new)
- **Discord**: [הצטרף לקהילה שלנו](https://aka.ms/ds4beginners/discord)
- **דיונים**: [דיונים ב-GitHub](https://github.com/microsoft/Data-Science-For-Beginners/discussions)
- **Microsoft Learn**: [פורומי שאלות ותשובות](https://docs.microsoft.com/answers/)

### תיעוד קשור

- [INSTALLATION.md](INSTALLATION.md) - הוראות התקנה
- [USAGE.md](USAGE.md) - איך להשתמש בתוכנית הלימודים
- [CONTRIBUTING.md](CONTRIBUTING.md) - איך לתרום
- [README.md](README.md) - סקירת הפרויקט

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.