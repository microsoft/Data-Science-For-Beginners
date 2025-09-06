<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c182e87f9f80be7e7cdffc7b40bbfccf",
  "translation_date": "2025-09-05T23:13:00+00:00",
  "source_file": "2-Working-With-Data/06-non-relational/README.md",
  "language_code": "he"
}
-->
# עבודה עם נתונים: נתונים לא-רלציוניים

|![סקיצה מאת [(@sketchthedocs)](https://sketchthedocs.dev)](../../sketchnotes/06-NoSQL.png)|
|:---:|
|עבודה עם נתוני NoSQL - _סקיצה מאת [@nitya](https://twitter.com/nitya)_|

## [שאלון לפני ההרצאה](https://ff-quizzes.netlify.app/en/ds/quiz/10)

נתונים אינם מוגבלים רק למסדי נתונים רלציוניים. שיעור זה מתמקד בנתונים לא-רלציוניים ויכסה את היסודות של גיליונות אלקטרוניים ו-NoSQL.

## גיליונות אלקטרוניים

גיליונות אלקטרוניים הם דרך פופולרית לאחסן ולחקור נתונים מכיוון שהם דורשים פחות עבודה כדי להגדיר ולהתחיל. בשיעור זה תלמדו את הרכיבים הבסיסיים של גיליון אלקטרוני, כמו גם נוסחאות ופונקציות. הדוגמאות יודגמו באמצעות Microsoft Excel, אך רוב החלקים והנושאים יהיו בעלי שמות ושלבים דומים בהשוואה לתוכנות גיליונות אלקטרוניים אחרות.

![חוברת עבודה ריקה של Microsoft Excel עם שני גיליונות עבודה](../../../../2-Working-With-Data/06-non-relational/images/parts-of-spreadsheet.png)

גיליון אלקטרוני הוא קובץ ויהיה נגיש במערכת הקבצים של מחשב, מכשיר או מערכת קבצים מבוססת ענן. התוכנה עצמה עשויה להיות מבוססת דפדפן או יישום שצריך להתקין על מחשב או להוריד כאפליקציה. ב-Excel קבצים אלו מוגדרים גם כ-**חוברות עבודה**, ומונח זה ישמש בשאר השיעור.

חוברת עבודה מכילה גיליון עבודה אחד או יותר, כאשר כל גיליון עבודה מסומן באמצעות כרטיסיות. בתוך גיליון עבודה ישנם מלבנים הנקראים **תאים**, המכילים את הנתונים בפועל. תא הוא החיתוך של שורה ועמודה, כאשר העמודות מסומנות באותיות אלפביתיות והשורות ממוספרות. חלק מהגיליונות האלקטרוניים יכילו כותרות בשורות הראשונות כדי לתאר את הנתונים בתא.

עם רכיבים בסיסיים אלו של חוברת עבודה ב-Excel, נשתמש בדוגמה מתוך [תבניות Microsoft](https://templates.office.com/) המתמקדת במלאי כדי לעבור על חלקים נוספים של גיליון אלקטרוני.

### ניהול מלאי

קובץ הגיליון האלקטרוני בשם "InventoryExample" הוא גיליון מעוצב של פריטים במלאי המכיל שלושה גיליונות עבודה, כאשר הכרטיסיות מסומנות "Inventory List", "Inventory Pick List" ו-"Bin Lookup". שורה 4 בגיליון העבודה Inventory List היא הכותרת, שמתארת את הערך של כל תא בעמודת הכותרת.

![נוסחה מסומנת מתוך רשימת מלאי לדוגמה ב-Microsoft Excel](../../../../2-Working-With-Data/06-non-relational/images/formula-excel.png)

ישנם מקרים שבהם תא תלוי בערכים של תאים אחרים כדי ליצור את ערכו. גיליון העבודה Inventory List עוקב אחר העלות של כל פריט במלאי שלו, אך מה אם נצטרך לדעת את הערך של כל המלאי? [**נוסחאות**](https://support.microsoft.com/en-us/office/overview-of-formulas-34519a4e-1e8d-4f4b-84d4-d642c4f63263) מבצעות פעולות על נתוני תאים ומשמשות לחישוב עלות המלאי בדוגמה זו. גיליון זה השתמש בנוסחה בעמודת Inventory Value כדי לחשב את הערך של כל פריט על ידי הכפלת הכמות תחת כותרת QTY והעלויות תחת כותרת COST. לחיצה כפולה או סימון תא תציג את הנוסחה. תבחינו שנוסחאות מתחילות בסימן שווה, ואחריו החישוב או הפעולה.

![פונקציה מסומנת מתוך רשימת מלאי לדוגמה ב-Microsoft Excel](../../../../2-Working-With-Data/06-non-relational/images/function-excel.png)

ניתן להשתמש בנוסחה נוספת כדי להוסיף את כל הערכים של Inventory Value יחד כדי לקבל את הערך הכולל. ניתן לחשב זאת על ידי הוספת כל תא כדי ליצור את הסכום, אך זו יכולה להיות משימה מייגעת. ל-Excel יש [**פונקציות**](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89), או נוסחאות מוגדרות מראש לביצוע חישובים על ערכי תאים. פונקציות דורשות ארגומנטים, שהם הערכים הנדרשים לביצוע חישובים אלו. כאשר פונקציות דורשות יותר מארגומנט אחד, יש לרשום אותם בסדר מסוים אחרת הפונקציה עשויה לא לחשב את הערך הנכון. בדוגמה זו נעשה שימוש בפונקציה SUM, והיא משתמשת בערכים של Inventory Value כארגומנט כדי להוסיף את הסכום הכולל המופיע תחת שורה 3, עמודה B (המכונה גם B3).

## NoSQL

NoSQL הוא מונח כולל לדרכים השונות לאחסן נתונים לא-רלציוניים וניתן לפרשו כ"לא-SQL", "לא-רלציוני" או "לא רק SQL". מערכות מסדי נתונים מסוג זה יכולות להיות מסווגות לארבעה סוגים.

![ייצוג גרפי של מסד נתונים מסוג key-value המציג 4 מפתחות ייחודיים המשויכים ל-4 ערכים שונים](../../../../2-Working-With-Data/06-non-relational/images/kv-db.png)
> מקור: [בלוג של מיכאל ביאלקי](https://www.michalbialecki.com/2018/03/18/azure-cosmos-db-key-value-database-cloud/)

[מסדי נתונים מסוג key-value](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#keyvalue-data-stores) משייכים מפתחות ייחודיים, שהם מזהים ייחודיים המשויכים לערך. זוגות אלו נשמרים באמצעות [טבלת hash](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/) עם פונקציית hash מתאימה.

![ייצוג גרפי של מסד נתונים מסוג גרף המציג את הקשרים בין אנשים, תחומי העניין שלהם ומיקומים](../../../../2-Working-With-Data/06-non-relational/images/graph-db.png)
> מקור: [Microsoft](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/graph-introduction#graph-database-by-example)

[מסדי נתונים מסוג גרף](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#graph-data-stores) מתארים קשרים בנתונים ומיוצגים כאוסף של צמתים וקשתות. צומת מייצג ישות, משהו שקיים בעולם האמיתי כמו סטודנט או דוח בנקאי. קשתות מייצגות את הקשר בין שתי ישויות. לכל צומת וקשת יש מאפיינים המספקים מידע נוסף על כל אחד מהם.

![ייצוג גרפי של מסד נתונים עמודתי המציג מסד נתונים של לקוחות עם שתי משפחות עמודות בשם Identity ו-Contact Info](../../../../2-Working-With-Data/06-non-relational/images/columnar-db.png)

[מסדי נתונים עמודתיים](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#columnar-data-stores) מארגנים נתונים לעמודות ושורות כמו מבנה נתונים רלציוני, אך כל עמודה מחולקת לקבוצות הנקראות משפחת עמודות, שבה כל הנתונים תחת עמודה אחת קשורים וניתנים לשליפה ושינוי כיחידה אחת.

### מסדי נתונים מסמכים עם Azure Cosmos DB

[מסדי נתונים מסמכים](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#document-data-stores) מבוססים על הרעיון של מסד נתונים מסוג key-value ומורכבים מסדרה של שדות ואובייקטים. חלק זה יחקור מסדי נתונים מסמכים עם אמולטור Cosmos DB.

מסד נתונים של Cosmos DB מתאים להגדרה של "לא רק SQL", כאשר מסד הנתונים המסמכים של Cosmos DB מסתמך על SQL כדי לשאול את הנתונים. [השיעור הקודם](../05-relational-databases/README.md) על SQL מכסה את היסודות של השפה, ונוכל ליישם כמה מהשאילתות גם כאן. נשתמש באמולטור Cosmos DB, שמאפשר לנו ליצור ולחקור מסד נתונים מסמכים באופן מקומי על מחשב. קראו עוד על האמולטור [כאן](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21).

מסמך הוא אוסף של שדות וערכי אובייקטים, כאשר השדות מתארים מה מייצג ערך האובייקט. להלן דוגמה למסמך:

```json
{
    "firstname": "Eva",
    "age": 44,
    "id": "8c74a315-aebf-4a16-bb38-2430a9896ce5",
    "_rid": "bHwDAPQz8s0BAAAAAAAAAA==",
    "_self": "dbs/bHwDAA==/colls/bHwDAPQz8s0=/docs/bHwDAPQz8s0BAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f95-010a691e01d7\"",
    "_attachments": "attachments/",
    "_ts": 1630544034
}
```

השדות המעניינים במסמך זה הם: `firstname`, `id`, ו-`age`. שאר השדות עם הקווים התחתונים נוצרו על ידי Cosmos DB.

#### חקר נתונים עם אמולטור Cosmos DB

ניתן להוריד ולהתקין את האמולטור [ל-Windows כאן](https://aka.ms/cosmosdb-emulator). עיינו בתיעוד זה [כאן](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos) לאפשרויות הפעלה עבור macOS ו-Linux.

האמולטור פותח חלון דפדפן, שבו תצוגת Explorer מאפשרת לחקור מסמכים.

![תצוגת Explorer של אמולטור Cosmos DB](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-explorer.png)

אם אתם עוקבים, לחצו על "Start with Sample" כדי ליצור מסד נתונים לדוגמה בשם SampleDB. אם תרחיבו את SampleDB על ידי לחיצה על החץ, תמצאו מיכל בשם `Persons`. מיכל מחזיק אוסף של פריטים, שהם המסמכים בתוך המיכל. תוכלו לחקור את ארבעת המסמכים האישיים תחת `Items`.

![חקר נתונים לדוגמה באמולטור Cosmos DB](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons.png)

#### שאילתת נתוני מסמכים עם אמולטור Cosmos DB

ניתן גם לבצע שאילתות על הנתונים לדוגמה על ידי לחיצה על כפתור השאילתה SQL Query החדש (הכפתור השני משמאל).

`SELECT * FROM c` מחזיר את כל המסמכים במיכל. נוסיף תנאי where ונמצא את כל מי שגילו פחות מ-40.

`SELECT * FROM c where c.age < 40`

![הרצת שאילתת SELECT על נתונים לדוגמה באמולטור Cosmos DB למציאת מסמכים שבהם הערך בשדה age קטן מ-40](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons-query.png)

השאילתה מחזירה שני מסמכים. שימו לב שהערך בשדה age עבור כל מסמך קטן מ-40.

#### JSON ומסמכים

אם אתם מכירים את JavaScript Object Notation (JSON), תבחינו שהמסמכים נראים דומים ל-JSON. ישנו קובץ בשם `PersonsData.json` בתיקייה זו עם נתונים נוספים שניתן להעלות למיכל Persons באמולטור באמצעות כפתור `Upload Item`.

ברוב המקרים, APIs שמחזירים נתוני JSON יכולים להיות מועברים ישירות ולהישמר במסדי נתונים מסמכים. להלן מסמך נוסף, המייצג ציוצים מחשבון הטוויטר של Microsoft שנשלפו באמצעות Twitter API ואז הוזנו ל-Cosmos DB.

```json
{
    "created_at": "2021-08-31T19:03:01.000Z",
    "id": "1432780985872142341",
    "text": "Blank slate. Like this tweet if you’ve ever painted in Microsoft Paint before. https://t.co/cFeEs8eOPK",
    "_rid": "dhAmAIUsA4oHAAAAAAAAAA==",
    "_self": "dbs/dhAmAA==/colls/dhAmAIUsA4o=/docs/dhAmAIUsA4oHAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f84-a0958ad901d7\"",
    "_attachments": "attachments/",
    "_ts": 1630537000
```

השדות המעניינים במסמך זה הם: `created_at`, `id`, ו-`text`.

## 🚀 אתגר

ישנו קובץ בשם `TwitterData.json` שניתן להעלות למסד הנתונים SampleDB. מומלץ להוסיף אותו למיכל נפרד. ניתן לעשות זאת על ידי:

1. לחיצה על כפתור המיכל החדש בפינה הימנית העליונה
2. בחירת מסד הנתונים הקיים (SampleDB) ויצירת מזהה מיכל עבור המיכל
3. הגדרת מפתח החלוקה ל-`/id`
4. לחיצה על OK (ניתן להתעלם משאר המידע בתצוגה זו מכיוון שמדובר במערך נתונים קטן שרץ מקומית על המחשב שלכם)
5. פתיחת המיכל החדש והעלאת קובץ נתוני הטוויטר באמצעות כפתור `Upload Item`

נסו להריץ כמה שאילתות SELECT כדי למצוא מסמכים שבהם מופיעה המילה Microsoft בשדה הטקסט. רמז: נסו להשתמש במילת המפתח [LIKE](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character).

## [שאלון לאחר ההרצאה](https://ff-quizzes.netlify.app/en/ds/quiz/11)

## סקירה ולמידה עצמית

- ישנם עיצובים ותכונות נוספים שנוספו לגיליון האלקטרוני שאינם מכוסים בשיעור זה. ל-Microsoft יש [ספרייה גדולה של תיעוד וסרטונים](https://support.microsoft.com/excel) על Excel אם אתם מעוניינים ללמוד עוד.

- תיעוד ארכיטקטוני זה מפרט את המאפיינים של סוגי הנתונים הלא-רלציוניים השונים: [נתונים לא-רלציוניים ו-NoSQL](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data)

- Cosmos DB הוא מסד נתונים מבוסס ענן שיכול גם לאחסן את סוגי ה-NoSQL השונים שהוזכרו בשיעור זה. למדו עוד על סוגים אלו במודול Microsoft Learn של [Cosmos DB](https://docs.microsoft.com/en-us/learn/paths/work-with-nosql-data-in-azure-cosmos-db/).

## משימה

[רווחי סודה](assignment.md)

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית נחשב למקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי בני אדם. איננו נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.