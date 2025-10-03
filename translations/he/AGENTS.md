<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:28:59+00:00",
  "source_file": "AGENTS.md",
  "language_code": "he"
}
-->
# AGENTS.md

## סקירת הפרויקט

"מדעי הנתונים למתחילים" הוא תוכנית לימודים מקיפה בת 10 שבועות ו-20 שיעורים שנוצרה על ידי Microsoft Azure Cloud Advocates. המאגר הוא משאב לימודי שמלמד מושגי יסוד במדעי הנתונים באמצעות שיעורים מבוססי פרויקטים, כולל מחברות Jupyter, חידונים אינטראקטיביים ומשימות מעשיות.

**טכנולוגיות מרכזיות:**
- **מחברות Jupyter**: אמצעי הלמידה העיקרי באמצעות Python 3
- **ספריות Python**: pandas, numpy, matplotlib לניתוח נתונים והדמיה
- **Vue.js 2**: אפליקציית חידונים (תיקיית quiz-app)
- **Docsify**: מחולל אתרי תיעוד לגישה לא מקוונת
- **Node.js/npm**: ניהול חבילות עבור רכיבי JavaScript
- **Markdown**: כל תוכן השיעורים והתיעוד

**ארכיטקטורה:**
- מאגר חינוכי רב-שפתי עם תרגומים נרחבים
- מחולק למודולי שיעורים (1-Introduction עד 6-Data-Science-In-Wild)
- כל שיעור כולל README, מחברות, משימות וחידונים
- אפליקציית חידונים עצמאית מבוססת Vue.js להערכות לפני/אחרי שיעור
- תמיכה ב-GitHub Codespaces ובמכולות פיתוח של VS Code

## פקודות התקנה

### התקנת המאגר
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### התקנת סביבת Python
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### התקנת אפליקציית החידונים
```bash
# Navigate to quiz app
cd quiz-app

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint and fix files
npm run lint
```

### שרת תיעוד Docsify
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### התקנת פרויקטי הדמיה
לפרויקטי הדמיה כמו meaningful-visualizations (שיעור 13):
```bash
# Navigate to starter or solution folder
cd 3-Data-Visualization/13-meaningful-visualizations/starter

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint files
npm run lint
```


## זרימת עבודה לפיתוח

### עבודה עם מחברות Jupyter
1. הפעל את Jupyter משורש המאגר: `jupyter notebook`
2. נווט לתיקיית השיעור הרצויה
3. פתח קבצי `.ipynb` כדי לעבוד על התרגילים
4. המחברות הן עצמאיות וכוללות הסברים ותאי קוד
5. רוב המחברות משתמשות ב-pandas, numpy ו-matplotlib - ודא שהן מותקנות

### מבנה השיעור
כל שיעור בדרך כלל כולל:
- `README.md` - תוכן השיעור הראשי עם תיאוריה ודוגמאות
- `notebook.ipynb` - תרגילים מעשיים במחברת Jupyter
- `assignment.ipynb` או `assignment.md` - משימות לתרגול
- תיקיית `solution/` - מחברות פתרון וקוד
- תיקיית `images/` - חומרים חזותיים תומכים

### פיתוח אפליקציית החידונים
- אפליקציה מבוססת Vue.js 2 עם טעינה מחדש בזמן הפיתוח
- החידונים מאוחסנים ב-`quiz-app/src/assets/translations/`
- לכל שפה יש תיקיית תרגום משלה (en, fr, es וכו')
- מספור החידונים מתחיל ב-0 ומגיע עד 39 (40 חידונים בסך הכל)

### הוספת תרגומים
- תרגומים נמצאים בתיקיית `translations/` בשורש המאגר
- לכל שפה יש מבנה שיעור מלא שמראה את המבנה באנגלית
- תרגום אוטומטי באמצעות GitHub Actions (co-op-translator.yml)

## הוראות בדיקה

### בדיקת אפליקציית החידונים
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### בדיקת מחברות
- אין מסגרת בדיקה אוטומטית למחברות
- אימות ידני: הפעל את כל התאים ברצף כדי לוודא שאין שגיאות
- בדוק שהקבצים זמינים והתוצאות נוצרות כראוי
- ודא שההדמיות מוצגות כראוי

### בדיקת תיעוד
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### בדיקות איכות קוד
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## הנחיות לסגנון קוד

### Python (מחברות Jupyter)
- עקוב אחר הנחיות סגנון PEP 8 לקוד Python
- השתמש בשמות משתנים ברורים שמסבירים את הנתונים המנותחים
- הוסף תאי Markdown עם הסברים לפני תאי קוד
- שמור על תאי קוד ממוקדים על מושגים או פעולות בודדות
- השתמש ב-pandas למניפולציה של נתונים, matplotlib להדמיה
- דפוס ייבוא נפוץ:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- עקוב אחר מדריך הסגנון והפרקטיקות הטובות של Vue.js 2
- תצורת ESLint ב-`quiz-app/package.json`
- השתמש ברכיבי Vue בקבצים בודדים (.vue)
- שמור על ארכיטקטורה מבוססת רכיבים
- הפעל `npm run lint` לפני ביצוע שינויים

### תיעוד Markdown
- השתמש בהיררכיית כותרות ברורה (# ## ### וכו')
- הוסף קטעי קוד עם מפרטי שפה
- הוסף טקסט חלופי לתמונות
- קשר לשיעורים ומשאבים קשורים
- שמור על אורך שורות סביר לקריאות

### ארגון קבצים
- תוכן שיעורים בתיקיות ממוספרות (01-defining-data-science וכו')
- פתרונות בתיקיות משנה ייעודיות `solution/`
- תרגומים משקפים את המבנה באנגלית בתיקיית `translations/`
- שמור קבצי נתונים בתיקיית `data/` או בתיקיות ספציפיות לשיעור

## בנייה ופריסה

### פריסת אפליקציית החידונים
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### פריסת Azure Static Web Apps
ניתן לפרוס את quiz-app ל-Azure Static Web Apps:
1. צור משאב Azure Static Web App
2. התחבר למאגר GitHub
3. הגדר הגדרות בנייה:
   - מיקום האפליקציה: `quiz-app`
   - מיקום הפלט: `dist`
4. זרימת העבודה של GitHub Actions תפרוס אוטומטית בעת ביצוע שינויים

### אתר תיעוד
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- המאגר כולל תצורת מכולת פיתוח
- Codespaces מגדיר אוטומטית את סביבת Python ו-Node.js
- פתח את המאגר ב-Codespace דרך ממשק GitHub
- כל התלויות מותקנות אוטומטית

## הנחיות לבקשות משיכה

### לפני הגשה
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### פורמט כותרת PR
- השתמש בכותרות ברורות ותיאוריות
- פורמט: `[רכיב] תיאור קצר`
- דוגמאות:
  - `[שיעור 7] תיקון שגיאת ייבוא במחברת Python`
  - `[אפליקציית חידונים] הוספת תרגום לגרמנית`
  - `[תיעוד] עדכון README עם דרישות חדשות`

### בדיקות נדרשות
- ודא שכל הקוד פועל ללא שגיאות
- בדוק שהמחברות מבוצעות במלואן
- אשר שאפליקציות Vue.js נבנות בהצלחה
- בדוק שקישורי התיעוד עובדים
- בדוק את אפליקציית החידונים אם שונתה
- אשר שהתרגומים שומרים על מבנה עקבי

### הנחיות לתרומה
- עקוב אחר סגנון הקוד והדפוסים הקיימים
- הוסף הערות הסבר ללוגיקה מורכבת
- עדכן את התיעוד הרלוונטי
- בדוק שינויים על פני מודולי שיעורים שונים אם רלוונטי
- עיין בקובץ CONTRIBUTING.md

## הערות נוספות

### ספריות נפוצות בשימוש
- **pandas**: מניפולציה וניתוח נתונים
- **numpy**: חישובים נומריים
- **matplotlib**: הדמיה וגרפים
- **seaborn**: הדמיה סטטיסטית (חלק מהשיעורים)
- **scikit-learn**: למידת מכונה (שיעורים מתקדמים)

### עבודה עם קבצי נתונים
- קבצי נתונים ממוקמים בתיקיית `data/` או בתיקיות ספציפיות לשיעור
- רוב המחברות מצפות לקבצי נתונים בנתיבים יחסיים
- קבצי CSV הם פורמט הנתונים העיקרי
- חלק מהשיעורים משתמשים ב-JSON לדוגמאות נתונים לא-רלציוניים

### תמיכה רב-שפתית
- מעל 40 תרגומים לשפות באמצעות GitHub Actions אוטומטיים
- זרימת עבודה לתרגום ב-`.github/workflows/co-op-translator.yml`
- תרגומים בתיקיית `translations/` עם קודי שפה
- תרגומי חידונים ב-`quiz-app/src/assets/translations/`

### אפשרויות סביבת פיתוח
1. **פיתוח מקומי**: התקן Python, Jupyter, Node.js מקומית
2. **GitHub Codespaces**: סביבת פיתוח מיידית מבוססת ענן
3. **מכולות פיתוח של VS Code**: פיתוח מקומי מבוסס מכולות
4. **Binder**: הפעל מחברות בענן (אם מוגדר)

### הנחיות לתוכן שיעורים
- כל שיעור הוא עצמאי אך בונה על מושגים קודמים
- חידונים לפני שיעור בודקים ידע קודם
- חידונים אחרי שיעור מחזקים את הלמידה
- משימות מספקות תרגול מעשי
- Sketchnotes מספקים סיכומים חזותיים

### פתרון בעיות נפוצות

**בעיות Kernel ב-Jupyter:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**כשלי התקנה של npm:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**שגיאות ייבוא במחברות:**
- ודא שכל הספריות הנדרשות מותקנות
- בדוק תאימות גרסת Python (מומלץ Python 3.7+)
- ודא שסביבת העבודה הווירטואלית מופעלת

**Docsify לא נטען:**
- ודא שאתה משרת משורש המאגר
- בדוק שקובץ `index.html` קיים
- ודא גישה נכונה לרשת (פורט 3000)

### שיקולי ביצועים
- מערכי נתונים גדולים עשויים לקחת זמן לטעון במחברות
- הדמיות עשויות להיות איטיות עבור גרפים מורכבים
- שרת הפיתוח של Vue.js מאפשר טעינה מחדש מהירה
- בניות ייצור אופטימליות וממוזערות

### הערות אבטחה
- אין להעלות נתונים רגישים או אישורים
- השתמש במשתני סביבה עבור מפתחות API בשיעורי ענן
- שיעורים הקשורים ל-Azure עשויים לדרוש אישורי חשבון Azure
- שמור על עדכון תלויות עבור תיקוני אבטחה

## תרומה לתרגומים
- תרגומים אוטומטיים מנוהלים באמצעות GitHub Actions
- תיקונים ידניים מתקבלים לשיפור דיוק התרגום
- עקוב אחר מבנה תיקיות התרגום הקיים
- עדכן קישורי חידונים לכלול פרמטר שפה: `?loc=fr`
- בדוק שיעורים מתורגמים לוודא הצגה תקינה

## משאבים קשורים
- תוכנית הלימודים הראשית: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- פורום דיונים: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- תוכניות לימודים אחרות של Microsoft: ML for Beginners, AI for Beginners, Web Dev for Beginners

## תחזוקת הפרויקט
- עדכונים שוטפים לשמירה על תוכן עדכני
- תרומות קהילתיות מתקבלות בברכה
- מעקב אחר בעיות ב-GitHub
- בקשות משיכה נבדקות על ידי מנהלי התוכנית
- סקירות ועדכונים חודשיים לתוכן

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.