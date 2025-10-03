<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a64d8afa22ffcc2016bb239188d6acb1",
  "translation_date": "2025-10-03T15:22:36+00:00",
  "source_file": "INSTALLATION.md",
  "language_code": "he"
}
-->
# מדריך התקנה

מדריך זה יעזור לך להגדיר את סביבת העבודה שלך כדי לעבוד עם תוכנית הלימודים של מדעי הנתונים למתחילים.

## תוכן עניינים

- [דרישות מוקדמות](../..)
- [אפשרויות התחלה מהירה](../..)
- [התקנה מקומית](../..)
- [אימות ההתקנה](../..)

## דרישות מוקדמות

לפני שתתחיל, עליך לוודא שיש לך:

- היכרות בסיסית עם שורת הפקודה/טרמינל
- חשבון GitHub (חינמי)
- חיבור אינטרנט יציב לצורך ההגדרה הראשונית

## אפשרויות התחלה מהירה

### אפשרות 1: GitHub Codespaces (מומלץ למתחילים)

הדרך הקלה ביותר להתחיל היא עם GitHub Codespaces, המספק סביבת פיתוח מלאה בדפדפן שלך.

1. עבור אל [הריפוזיטורי](https://github.com/microsoft/Data-Science-For-Beginners)
2. לחץ על תפריט הנפתח **Code**
3. בחר בלשונית **Codespaces**
4. לחץ על **Create codespace on main**
5. המתן עד שסביבת העבודה תתאפס (2-3 דקות)

סביבת העבודה שלך מוכנה עכשיו עם כל התלויות מותקנות מראש!

### אפשרות 2: פיתוח מקומי

לעבודה על המחשב שלך, עקוב אחר ההוראות המפורטות למטה.

## התקנה מקומית

### שלב 1: התקן Git

Git נדרש כדי לשכפל את הריפוזיטורי ולעקוב אחר השינויים שלך.

**Windows:**
- הורד מ-[git-scm.com](https://git-scm.com/download/win)
- הפעל את ההתקנה עם ההגדרות ברירת המחדל

**macOS:**
- התקן באמצעות Homebrew: `brew install git`
- או הורד מ-[git-scm.com](https://git-scm.com/download/mac)

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

### שלב 2: שכפל את הריפוזיטורי

```bash
# Clone the repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Navigate to the directory
cd Data-Science-For-Beginners
```

### שלב 3: התקן Python ו-Jupyter

נדרש Python 3.7 או גרסה גבוהה יותר עבור שיעורי מדעי הנתונים.

**Windows:**
1. הורד את Python מ-[python.org](https://www.python.org/downloads/)
2. במהלך ההתקנה, סמן "Add Python to PATH"
3. אמת את ההתקנה:
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

### שלב 4: הגדר סביבת Python

מומלץ להשתמש בסביבה וירטואלית כדי לשמור על התלויות מבודדות.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### שלב 5: התקן חבילות Python

התקן את ספריות מדעי הנתונים הנדרשות:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### שלב 6: התקן Node.js ו-npm (עבור אפליקציית השאלון)

אפליקציית השאלון דורשת Node.js ו-npm.

**Windows/macOS:**
- הורד מ-[nodejs.org](https://nodejs.org/) (מומלץ גרסת LTS)
- הפעל את ההתקנה

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

### שלב 7: התקן תלויות אפליקציית השאלון

```bash
# Navigate to quiz app directory
cd quiz-app

# Install dependencies
npm install

# Return to root directory
cd ..
```

### שלב 8: התקן Docsify (אופציונלי)

לגישה לא מקוונת לתיעוד:

```bash
npm install -g docsify-cli
```

## אימות ההתקנה

### בדוק את Python ו-Jupyter

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Start Jupyter Notebook
jupyter notebook
```

הדפדפן שלך אמור להיפתח עם ממשק Jupyter. כעת תוכל לנווט לכל קובץ `.ipynb` של שיעור.

### בדוק את אפליקציית השאלון

```bash
# Navigate to quiz app
cd quiz-app

# Start development server
npm run serve
```

אפליקציית השאלון אמורה להיות זמינה בכתובת `http://localhost:8080` (או פורט אחר אם 8080 תפוס).

### בדוק את שרת התיעוד

```bash
# From the root directory of the repository
docsify serve
```

התיעוד אמור להיות זמין בכתובת `http://localhost:3000`.

## שימוש במכולות פיתוח של VS Code

אם התקנת Docker, תוכל להשתמש במכולות פיתוח של VS Code:

1. התקן את [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. התקן את [Visual Studio Code](https://code.visualstudio.com/)
3. התקן את [הרחבת Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. פתח את הריפוזיטורי ב-VS Code
5. לחץ `F1` ובחר "Remote-Containers: Reopen in Container"
6. המתן עד שהמכולה תיבנה (רק בפעם הראשונה)

## צעדים הבאים

- חקור את [README.md](README.md) לקבלת סקירה כללית של תוכנית הלימודים
- קרא את [USAGE.md](USAGE.md) עבור תהליכי עבודה ודוגמאות נפוצים
- בדוק את [TROUBLESHOOTING.md](TROUBLESHOOTING.md) אם נתקלת בבעיות
- עיין ב-[CONTRIBUTING.md](CONTRIBUTING.md) אם ברצונך לתרום

## קבלת עזרה

אם נתקלת בבעיות:

1. בדוק את מדריך [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. חפש בעיות קיימות ב-[GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
3. הצטרף לקהילת [Discord שלנו](https://aka.ms/ds4beginners/discord)
4. צור בעיה חדשה עם מידע מפורט על הבעיה שלך

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.