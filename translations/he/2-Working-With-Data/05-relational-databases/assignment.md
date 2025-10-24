<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:56:41+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "he"
}
-->
# הצגת נתוני שדות תעופה

סופקה לכם [מסד נתונים](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) המבוסס על [SQLite](https://sqlite.org/index.html) שמכיל מידע על שדות תעופה. הסכימה מוצגת למטה. תשתמשו ב-[הרחבת SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ב-[Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) כדי להציג מידע על שדות תעופה בערים שונות.

## הוראות

כדי להתחיל במשימה, תצטרכו לבצע כמה שלבים. תצטרכו להתקין כמה כלים ולהוריד את מסד הנתונים לדוגמה.

### הגדרת המערכת שלכם

ניתן להשתמש ב-Visual Studio Code ובהרחבת SQLite כדי לעבוד עם מסד הנתונים.

1. גשו ל-[code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) ופעלו לפי ההוראות להתקנת Visual Studio Code
1. התקינו את [הרחבת SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) כפי שמוסבר בעמוד ה-Marketplace

### הורדה ופתיחת מסד הנתונים

כעת תורידו ותפתחו את מסד הנתונים.

1. הורידו את [קובץ מסד הנתונים מ-GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) ושמרו אותו בתיקייה
1. פתחו את Visual Studio Code
1. פתחו את מסד הנתונים בהרחבת SQLite על ידי לחיצה על **Ctl-Shift-P** (או **Cmd-Shift-P** במק) והקלדת `SQLite: Open database`
1. בחרו **Choose database from file** ופתחו את קובץ **airports.db** שהורדתם קודם
1. לאחר פתיחת מסד הנתונים (לא תראו עדכון על המסך), צרו חלון שאילתה חדש על ידי לחיצה על **Ctl-Shift-P** (או **Cmd-Shift-P** במק) והקלדת `SQLite: New query`

לאחר פתיחת חלון השאילתה החדש, ניתן להשתמש בו להרצת פקודות SQL על מסד הנתונים. ניתן להשתמש בפקודה **Ctl-Shift-Q** (או **Cmd-Shift-Q** במק) כדי להריץ שאילתות על מסד הנתונים.

> [!NOTE] 
> למידע נוסף על הרחבת SQLite, ניתן לעיין ב-[תיעוד](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## סכימת מסד הנתונים

סכימת מסד נתונים היא עיצוב המבנה והטבלאות שלו. מסד הנתונים **airports** מכיל שתי טבלאות, `cities`, שמכילה רשימת ערים בבריטניה ובאירלנד, ו-`airports`, שמכילה רשימת כל שדות התעופה. מכיוון שלחלק מהערים יש מספר שדות תעופה, נוצרו שתי טבלאות לאחסון המידע. בתרגיל זה תשתמשו ב-Joins כדי להציג מידע עבור ערים שונות.

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

צרו שאילתות שיחזירו את המידע הבא:

1. כל שמות הערים בטבלת `Cities`
1. כל הערים באירלנד בטבלת `Cities`
1. כל שמות שדות התעופה עם העיר והמדינה שלהם
1. כל שדות התעופה בלונדון, בריטניה

## קריטריונים להערכה

| מצטיין | מספק | דורש שיפור |
| ------- | ----- | ---------- |

---

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא נושאים באחריות לאי הבנות או פירושים שגויים הנובעים משימוש בתרגום זה.