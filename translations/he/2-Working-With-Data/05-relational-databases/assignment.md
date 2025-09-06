<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-28T15:19:34+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "he"
}
-->
# הצגת נתוני שדות תעופה

ניתן לך [מאגר נתונים](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) המבוסס על [SQLite](https://sqlite.org/index.html) שמכיל מידע על שדות תעופה. הסכימה מוצגת למטה. תשתמש/י ב-[תוסף SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ב-[Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) כדי להציג מידע על שדות תעופה בערים שונות.

## הוראות

כדי להתחיל במשימה, תצטרך/י לבצע כמה שלבים. תצטרך/י להתקין כמה כלים ולהוריד את מאגר הנתונים לדוגמה.

### הגדרת המערכת שלך

תוכל/י להשתמש ב-Visual Studio Code ובתוסף SQLite כדי לעבוד עם מאגר הנתונים.

1. גש/י ל-[code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) ופעל/י לפי ההוראות להתקנת Visual Studio Code
1. התקן/י את [תוסף SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) כפי שמוסבר בדף ה-Marketplace

### הורדה ופתיחת מאגר הנתונים

כעת תוריד/י ותפתח/י את מאגר הנתונים.

1. הורד/י את [קובץ המאגר מ-GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) ושמור/י אותו בתיקייה
1. פתח/י את Visual Studio Code
1. פתח/י את מאגר הנתונים בתוסף SQLite על ידי בחירה ב-**Ctl-Shift-P** (או **Cmd-Shift-P** במק) והקלדת `SQLite: Open database`
1. בחר/י **Choose database from file** ופתח/י את קובץ **airports.db** שהורדת קודם
1. לאחר פתיחת מאגר הנתונים (לא תראה/י עדכון על המסך), צור/י חלון שאילתות חדש על ידי בחירה ב-**Ctl-Shift-P** (או **Cmd-Shift-P** במק) והקלדת `SQLite: New query`

לאחר הפתיחה, ניתן להשתמש בחלון השאילתות החדש כדי להריץ פקודות SQL על מאגר הנתונים. ניתן להשתמש בפקודה **Ctl-Shift-Q** (או **Cmd-Shift-Q** במק) כדי להריץ שאילתות על המאגר.

> [!NOTE] למידע נוסף על תוסף SQLite, ניתן לעיין ב-[תיעוד](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## סכימת מאגר הנתונים

הסכימה של מאגר נתונים היא עיצוב המבנה והטבלאות שלו. מאגר הנתונים **airports** מכיל שתי טבלאות: `cities`, שמכילה רשימת ערים בבריטניה ואירלנד, ו-`airports`, שמכילה רשימת כל שדות התעופה. מכיוון שלחלק מהערים יש מספר שדות תעופה, נוצרו שתי טבלאות לאחסון המידע. בתרגיל זה תשתמש/י ב-Joins כדי להציג מידע על ערים שונות.

| ערים             |
| ---------------- |
| id (PK, integer) |
| city (text)      |
| country (text)   |

| שדות תעופה                     |
| ------------------------------ |
| id (PK, integer)               |
| name (text)                    |
| code (text)                    |
| city_id (FK to id in **Cities**) |

## משימה

צור/י שאילתות שיחזירו את המידע הבא:

1. כל שמות הערים בטבלת `Cities`
1. כל הערים באירלנד בטבלת `Cities`
1. כל שמות שדות התעופה עם העיר והמדינה שלהם
1. כל שדות התעופה בלונדון, בריטניה

## קריטריונים להערכה

| מצטיין | מספק | דורש שיפור |
| ------- | ----- | ---------- |

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. איננו נושאים באחריות לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.