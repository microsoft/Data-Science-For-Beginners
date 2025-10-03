<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:05:57+00:00",
  "source_file": "USAGE.md",
  "language_code": "he"
}
-->
# מדריך שימוש

מדריך זה מספק דוגמאות ותהליכי עבודה נפוצים לשימוש בתוכנית הלימודים "מדעי הנתונים למתחילים".

## תוכן עניינים

- [איך להשתמש בתוכנית הלימודים הזו](../..)
- [עבודה עם שיעורים](../..)
- [עבודה עם מחברות Jupyter](../..)
- [שימוש באפליקציית החידונים](../..)
- [תהליכי עבודה נפוצים](../..)
- [טיפים ללומדים עצמאיים](../..)
- [טיפים למורים](../..)

## איך להשתמש בתוכנית הלימודים הזו

תוכנית הלימודים הזו נועדה להיות גמישה וניתן להשתמש בה בדרכים שונות:

- **לימוד בקצב אישי**: עבודה עצמאית דרך השיעורים בקצב שלך
- **הוראה בכיתה**: שימוש כקורס מובנה עם הדרכה
- **קבוצות לימוד**: למידה שיתופית עם עמיתים
- **פורמט סדנה**: מפגשי לימוד אינטנסיביים לטווח קצר

## עבודה עם שיעורים

כל שיעור בנוי במבנה עקבי כדי למקסם את הלמידה:

### מבנה שיעור

1. **חידון לפני השיעור**: בדיקת הידע הקיים שלך
2. **סקצ'נוט** (אופציונלי): סיכום חזותי של מושגים מרכזיים
3. **וידאו** (אופציונלי): תוכן וידאו משלים
4. **שיעור כתוב**: מושגים והסברים מרכזיים
5. **מחברת Jupyter**: תרגילי קוד מעשיים
6. **מטלה**: תרגול החומר הנלמד
7. **חידון אחרי השיעור**: חיזוק ההבנה שלך

### דוגמה לתהליך עבודה עם שיעור

```bash
# 1. Navigate to the lesson directory
cd 1-Introduction/01-defining-data-science

# 2. Read the README.md
# Open README.md in your browser or editor

# 3. Take the pre-lesson quiz
# Click the quiz link in the README

# 4. Open the Jupyter notebook (if available)
jupyter notebook

# 5. Complete the exercises in the notebook

# 6. Work on the assignment

# 7. Take the post-lesson quiz
```

## עבודה עם מחברות Jupyter

### התחלת Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### הרצת תאים במחברת

1. **הרצת תא**: לחץ `Shift + Enter` או על כפתור "Run"
2. **הרצת כל התאים**: בחר "Cell" → "Run All" בתפריט
3. **אתחול הליבה**: בחר "Kernel" → "Restart" אם נתקלת בבעיות

### דוגמה: עבודה עם נתונים במחברת

```python
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load a dataset
df = pd.read_csv('data/sample.csv')

# Explore the data
df.head()
df.info()
df.describe()

# Create a visualization
plt.figure(figsize=(10, 6))
plt.plot(df['column_name'])
plt.title('Sample Visualization')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()
```

### שמירת העבודה שלך

- Jupyter שומר באופן אוטומטי מדי פעם
- שמירה ידנית: לחץ `Ctrl + S` (או `Cmd + S` ב-macOS)
- ההתקדמות שלך נשמרת בקובץ `.ipynb`

## שימוש באפליקציית החידונים

### הרצת אפליקציית החידונים באופן מקומי

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### ביצוע חידונים

1. חידוני לפני השיעור מקושרים בראש כל שיעור
2. חידוני אחרי השיעור מקושרים בתחתית כל שיעור
3. כל חידון כולל 3 שאלות
4. החידונים נועדו לחיזוק הלמידה, לא לבחינה מקיפה

### מספור החידונים

- החידונים ממוספרים 0-39 (סה"כ 40 חידונים)
- לכל שיעור יש בדרך כלל חידון לפני ואחרי
- כתובת ה-URL של החידון כוללת את מספר החידון: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## תהליכי עבודה נפוצים

### תהליך עבודה 1: מסלול למתחילים מוחלטים

```bash
# 1. Set up your environment (see INSTALLATION.md)

# 2. Start with Lesson 1
cd 1-Introduction/01-defining-data-science

# 3. For each lesson:
#    - Take pre-lesson quiz
#    - Read the lesson content
#    - Work through the notebook
#    - Complete the assignment
#    - Take post-lesson quiz

# 4. Progress through all 20 lessons sequentially
```

### תהליך עבודה 2: למידה לפי נושא

אם אתה מתעניין בנושא מסוים:

```bash
# Example: Focus on Data Visualization
cd 3-Data-Visualization

# Explore lessons 9-13:
# - Lesson 9: Visualizing Quantities
# - Lesson 10: Visualizing Distributions
# - Lesson 11: Visualizing Proportions
# - Lesson 12: Visualizing Relationships
# - Lesson 13: Meaningful Visualizations
```

### תהליך עבודה 3: למידה מבוססת פרויקטים

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### תהליך עבודה 4: מדעי נתונים מבוססי ענן

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## טיפים ללומדים עצמאיים

### שמירה על סדר

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### תרגול קבוע

- הקדש זמן ייעודי מדי יום או שבוע
- השלם לפחות שיעור אחד בשבוע
- חזור על שיעורים קודמים מדי פעם

### מעורבות בקהילה

- הצטרף ל-[קהילת Discord](https://aka.ms/ds4beginners/discord)
- השתתף בערוץ #Data-Science-for-Beginners ב-Discord [דיונים ב-Discord](https://aka.ms/ds4beginners/discord)
- שתף את ההתקדמות שלך ושאל שאלות

### בניית פרויקטים אישיים

לאחר השלמת השיעורים, יישם את המושגים בפרויקטים אישיים:

```python
# Example: Analyze your own dataset
import pandas as pd

# Load your own data
my_data = pd.read_csv('my-project/data.csv')

# Apply techniques learned
# - Data cleaning (Lesson 8)
# - Exploratory data analysis (Lesson 7)
# - Visualization (Lessons 9-13)
# - Analysis (Lesson 15)
```

## טיפים למורים

### הכנת הכיתה

1. עיין ב-[for-teachers.md](for-teachers.md) לקבלת הנחיות מפורטות
2. הקם סביבה משותפת (GitHub Classroom או Codespaces)
3. הקם ערוץ תקשורת (Discord, Slack או Teams)

### תכנון שיעורים

**לוח זמנים מוצע ל-10 שבועות:**

- **שבוע 1-2**: מבוא (שיעורים 1-4)
- **שבוע 3-4**: עבודה עם נתונים (שיעורים 5-8)
- **שבוע 5-6**: ויזואליזציה של נתונים (שיעורים 9-13)
- **שבוע 7-8**: מחזור החיים של מדעי הנתונים (שיעורים 14-16)
- **שבוע 9**: מדעי נתונים בענן (שיעורים 17-19)
- **שבוע 10**: יישומים בעולם האמיתי ופרויקטים סופיים (שיעור 20)

### הרצת Docsify לגישה לא מקוונת

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### הערכת מטלות

- בדוק מחברות תלמידים עבור תרגילים שהושלמו
- בדוק הבנה דרך ציוני חידונים
- הערך פרויקטים סופיים באמצעות עקרונות מחזור החיים של מדעי הנתונים

### יצירת מטלות

```python
# Example custom assignment template
"""
Assignment: [Topic]

Objective: [Learning goal]

Dataset: [Provide or have students find one]

Tasks:
1. Load and explore the dataset
2. Clean and prepare the data
3. Create at least 3 visualizations
4. Perform analysis
5. Communicate findings

Deliverables:
- Jupyter notebook with code and explanations
- Written summary of findings
"""
```

## עבודה לא מקוונת

### הורדת משאבים

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### הרצת תיעוד באופן מקומי

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### הרצת אפליקציית החידונים באופן מקומי

```bash
cd quiz-app
npm run serve
```

## גישה לתוכן מתורגם

תרגומים זמינים ביותר מ-40 שפות:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

כל תרגום שומר על אותו מבנה כמו הגרסה באנגלית.

## משאבים נוספים

### המשך הלמידה

- [Microsoft Learn](https://docs.microsoft.com/learn/) - מסלולי למידה נוספים
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - משאבים לסטודנטים
- [Azure AI Foundry](https://aka.ms/foundry/forum) - פורום קהילתי

### תוכניות לימודים קשורות

- [AI למתחילים](https://aka.ms/ai-beginners)
- [ML למתחילים](https://aka.ms/ml-beginners)
- [פיתוח אתרים למתחילים](https://aka.ms/webdev-beginners)
- [Generative AI למתחילים](https://aka.ms/genai-beginners)

## קבלת עזרה

- עיין ב-[TROUBLESHOOTING.md](TROUBLESHOOTING.md) לבעיות נפוצות
- חפש [בעיות ב-GitHub](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- הצטרף ל-[Discord](https://aka.ms/ds4beginners/discord)
- עיין ב-[CONTRIBUTING.md](CONTRIBUTING.md) לדיווח על בעיות או תרומה

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.