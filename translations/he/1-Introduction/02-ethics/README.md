<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a34157cc63516eba97c89a0b2f8c3e6",
  "translation_date": "2025-09-03T21:34:30+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "he"
}
-->
# מבוא לאתיקה של נתונים

|![ סקיצה מאת [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| אתיקה במדעי הנתונים - _סקיצה מאת [@nitya](https://twitter.com/nitya)_ |

---

כולנו אזרחים של נתונים החיים בעולם מבוסס נתונים.

מגמות השוק מראות שעד שנת 2022, אחת מתוך שלוש ארגונים גדולים תקנה ותמכור את הנתונים שלה דרך [שווקים ומרכזי מסחר](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/) מקוונים. בתור **מפתחי אפליקציות**, יהיה לנו קל וזול יותר לשלב תובנות מבוססות נתונים ואוטומציה מבוססת אלגוריתמים בחוויות היומיומיות של המשתמשים. אך ככל שהבינה המלאכותית הופכת לנפוצה, נצטרך גם להבין את הנזקים הפוטנציאליים הנגרמים מ[שימוש לרעה](https://www.youtube.com/watch?v=TQHs8SA1qpk) באלגוריתמים כאלה בקנה מידה רחב.

מגמות נוספות מצביעות על כך שניצור ונצרוך מעל [180 זטה-בייטים](https://www.statista.com/statistics/871513/worldwide-data-created/) של נתונים עד שנת 2025. בתור **מדעני נתונים**, זה מעניק לנו רמות חסרות תקדים של גישה לנתונים אישיים. המשמעות היא שנוכל לבנות פרופילים התנהגותיים של משתמשים ולהשפיע על קבלת ההחלטות בדרכים שיוצרות [אשליה של בחירה חופשית](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice), תוך כדי דחיפת המשתמשים לתוצאות שאנחנו מעדיפים. זה גם מעלה שאלות רחבות יותר על פרטיות נתונים והגנה על משתמשים.

אתיקה של נתונים היא כיום _מסגרת הכרחית_ למדעי הנתונים וההנדסה, המסייעת לנו למזער נזקים פוטנציאליים ותוצאות בלתי צפויות מפעולותינו המבוססות על נתונים. [מעגל ההייפ של גרטנר עבור AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) מזהה מגמות רלוונטיות באתיקה דיגיטלית, AI אחראי, וממשל AI כגורמים מרכזיים למגמות רחבות יותר סביב _דמוקרטיזציה_ ו_תיעוש_ של AI.

![מעגל ההייפ של גרטנר עבור AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

בשיעור זה, נחקור את התחום המרתק של אתיקה של נתונים - החל ממושגים ואתגרים מרכזיים, דרך מחקרי מקרה ועד מושגים יישומיים של AI כמו ממשל - המסייעים לבסס תרבות אתית בצוותים ובארגונים העובדים עם נתונים ו-AI.

## [שאלון לפני השיעור](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## הגדרות בסיסיות

נתחיל בהבנת המונחים הבסיסיים.

המילה "אתיקה" מגיעה מ[המילה היוונית "ethikos"](https://en.wikipedia.org/wiki/Ethics) (ושורשה "ethos") שמשמעותה _אופי או טבע מוסרי_. 

**אתיקה** עוסקת בערכים משותפים ועקרונות מוסריים שמנחים את התנהגותנו בחברה. אתיקה מבוססת לא על חוקים אלא על נורמות מקובלות של מה "נכון מול לא נכון". עם זאת, שיקולים אתיים יכולים להשפיע על יוזמות ממשל תאגידי ורגולציות ממשלתיות שיוצרות תמריצים נוספים לציות.

**אתיקה של נתונים** היא [ענף חדש של אתיקה](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1) שחוקר ומעריך בעיות מוסריות הקשורות ל_נתונים, אלגוריתמים ופרקטיקות תואמות_. כאן, **"נתונים"** מתמקדים בפעולות הקשורות ליצירה, הקלטה, אצירה, עיבוד, הפצה, שיתוף ושימוש; **"אלגוריתמים"** מתמקדים ב-AI, סוכנים, למידת מכונה ורובוטים; ו**"פרקטיקות"** מתמקדות בנושאים כמו חדשנות אחראית, תכנות, פריצה וקודי אתיקה.

**אתיקה יישומית** היא [היישום המעשי של שיקולים מוסריים](https://en.wikipedia.org/wiki/Applied_ethics). זהו תהליך של חקירה פעילה של סוגיות אתיות בהקשר של _פעולות, מוצרים ותהליכים בעולם האמיתי_, ולקיחת צעדים מתקנים כדי להבטיח שהם נשארים מיושרים עם הערכים האתיים שהוגדרו.

**תרבות אתית** עוסקת ב[_הפעלה_ של אתיקה יישומית](https://hbr.org/2019/05/how-to-design-an-ethical-organization) כדי להבטיח שהעקרונות והפרקטיקות האתיים שלנו יאומצו באופן עקבי ובר-קיימא בכל רחבי הארגון. תרבויות אתיות מצליחות מגדירות עקרונות אתיים ברמת הארגון, מספקות תמריצים משמעותיים לציות, ומחזקות נורמות אתיות על ידי עידוד והגברת התנהגויות רצויות בכל רמות הארגון.

## מושגי אתיקה

בקטע זה נדון במושגים כמו **ערכים משותפים** (עקרונות) ו**אתגרים אתיים** (בעיות) באתיקה של נתונים - ונחקור **מחקרי מקרה** שיעזרו לכם להבין את המושגים הללו בהקשרים של העולם האמיתי.

### 1. עקרונות אתיים

כל אסטרטגיה של אתיקה של נתונים מתחילה בהגדרת _עקרונות אתיים_ - "הערכים המשותפים" שמתארים התנהגויות מקובלות ומנחים פעולות תואמות בפרויקטים שלנו של נתונים ו-AI. ניתן להגדיר אותם ברמה אישית או צוותית. עם זאת, רוב הארגונים הגדולים מגדירים אותם בהצהרת משימה או מסגרת של _AI אתי_ ברמת הארגון, ומיישמים אותם באופן עקבי בכל הצוותים.

**דוגמה:** הצהרת המשימה של [Microsoft Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai) אומרת: _"אנחנו מחויבים לקידום AI מונחה עקרונות אתיים שמעמידים את האדם במרכז"_ - ומזהה 6 עקרונות אתיים במסגרת הבאה:

![AI אחראי במיקרוסופט](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

בואו נחקור בקצרה את העקרונות הללו. _שקיפות_ ו_אחריות_ הם ערכים יסודיים שעליהם נבנים עקרונות אחרים - אז נתחיל שם:

* [**אחריות**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) הופכת את העוסקים בתחום ל_אחראים_ על פעולותיהם בתחום הנתונים וה-AI, ועל הציות לעקרונות האתיים הללו.
* [**שקיפות**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) מבטיחה שפעולות הנתונים וה-AI יהיו _מובנות_ (ניתנות לפרשנות) למשתמשים, ומסבירה את ה"מה" וה"למה" מאחורי ההחלטות.
* [**הוגנות**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - מתמקדת בהבטחת יחס _הוגן_ לכל האנשים, תוך התמודדות עם הטיות חברתיות-טכניות מערכתיות או סמיות בנתונים ובמערכות.
* [**אמינות ובטיחות**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - מבטיחה ש-AI מתנהג _בעקביות_ עם ערכים מוגדרים, וממזערת נזקים פוטנציאליים או תוצאות בלתי צפויות.
* [**פרטיות ואבטחה**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - עוסקת בהבנת מקור הנתונים ובמתן _הגנה על פרטיות נתונים_ למשתמשים.
* [**הכללה**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - עוסקת בעיצוב פתרונות AI מתוך כוונה, והתאמתם למגוון רחב של _צרכים ויכולות אנושיות_.

> 🚨 חשבו על מה יכולה להיות הצהרת המשימה של אתיקה של נתונים שלכם. חקרו מסגרות AI אתיות מארגונים אחרים - הנה דוגמאות מ-[IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles), ו-[Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). אילו ערכים משותפים יש להם? כיצד עקרונות אלה קשורים למוצרי AI או לתעשייה שבה הם פועלים?

### 2. אתגרים אתיים

לאחר שהגדרנו עקרונות אתיים, השלב הבא הוא להעריך את פעולות הנתונים וה-AI שלנו כדי לראות אם הן מתיישרות עם הערכים המשותפים הללו. חשבו על הפעולות שלכם בשתי קטגוריות: _איסוף נתונים_ ו_עיצוב אלגוריתמים_.

באיסוף נתונים, הפעולות יכללו ככל הנראה **נתונים אישיים** או מידע אישי מזהה (PII) עבור אנשים מזוהים. זה כולל [פריטים מגוונים של נתונים לא אישיים](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en) שמזהים _ביחד_ אדם. אתגרים אתיים יכולים להיות קשורים ל_פרטיות נתונים_, _בעלות על נתונים_, ונושאים קשורים כמו _הסכמה מדעת_ ו_זכויות קניין רוחני_ למשתמשים.

בעיצוב אלגוריתמים, הפעולות יכללו איסוף ואצירה של **מאגרי נתונים**, ואז שימוש בהם לאימון ופריסה של **מודלים נתונים** שמנבאים תוצאות או מבצעים אוטומציה של החלטות בהקשרים של העולם האמיתי. אתגרים אתיים יכולים לנבוע מ_הטיות במאגרי נתונים_, _בעיות איכות נתונים_, _חוסר הוגנות_, ו_ייצוג שגוי_ באלגוריתמים - כולל כמה בעיות שהן מערכתיות בטבען.

בשני המקרים, אתגרים אתיים מדגישים תחומים שבהם הפעולות שלנו עשויות להתנגש עם הערכים המשותפים שלנו. כדי לזהות, למזער, למנוע או לבטל את החששות הללו - עלינו לשאול שאלות מוסריות "כן/לא" הקשורות לפעולותינו, ואז לנקוט צעדים מתקנים לפי הצורך. בואו נבחן כמה אתגרים אתיים והשאלות המוסריות שהם מעלים:

#### 2.1 בעלות על נתונים

איסוף נתונים כולל לעיתים קרובות נתונים אישיים שיכולים לזהות את נושאי הנתונים. [בעלות על נתונים](https://permission.io/blog/data-ownership) עוסקת ב_שליטה_ ו[_זכויות משתמשים_](https://permission.io/blog/data-ownership) הקשורות ליצירה, עיבוד והפצה של נתונים.

השאלות המוסריות שעלינו לשאול הן:
 * מי הבעלים של הנתונים? (משתמש או ארגון)
 * אילו זכויות יש לנושאי הנתונים? (לדוגמה: גישה, מחיקה, ניידות)
 * אילו זכויות יש לארגונים? (לדוגמה: תיקון ביקורות משתמשים מזיקות)

#### 2.2 הסכמה מדעת

[הסכמה מדעת](https://legaldictionary.net/informed-consent/) מגדירה את פעולת המשתמשים בהסכמה לפעולה (כמו איסוף נתונים) עם _הבנה מלאה_ של העובדות הרלוונטיות כולל המטרה, הסיכונים הפוטנציאליים והחלופות.

שאלות לחקור כאן הן:
 * האם המשתמש (נושא הנתונים) נתן רשות ללכידת נתונים ושימוש בהם?
 * האם המשתמש הבין את המטרה שלשמה הנתונים נלכדו?
 * האם המשתמש הבין את הסיכונים הפוטנציאליים מהשתתפותו?

#### 2.3 קניין רוחני

[קניין רוחני](https://en.wikipedia.org/wiki/Intellectual_property) מתייחס ליצירות בלתי מוחשיות הנובעות מיוזמה אנושית, שעשויות _להיות בעלות ערך כלכלי_ לאנשים או עסקים.

שאלות לחקור כאן הן:
 * האם הנתונים שנאספו היו בעלי ערך כלכלי למשתמש או לעסק?
 * האם ל**משתמש** יש קניין רוחני כאן?
 * האם ל**ארגון** יש קניין רוחני כאן?
 * אם זכויות אלו קיימות, כיצד אנו מגנים עליהן?

#### 2.4 פרטיות נתונים

[פרטיות נתונים](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) או פרטיות מידע מתייחסת לשמירה על פרטיות המשתמש והגנה על זהותו ביחס למידע אישי מזהה.

שאלות לחקור כאן הן:
 * האם הנתונים האישיים של המשתמשים מוגנים מפני פריצות ודליפות?
 * האם הנתונים של המשתמשים נגישים רק למשתמשים מורשים ולהקשרים מורשים?
 * האם האנונימיות של המשתמשים נשמרת כאשר הנתונים משותפים או מופצים?
 * האם ניתן להסיר זיהוי של משתמש ממאגרי נתונים אנונימיים?

#### 2.5 הזכות להישכח

[הזכות להישכח](https://en.wikipedia.org/wiki/Right_to_be_forgotten) או [הזכות למחיקה](https://www.gdpreu.org/right-to-be-forgotten/) מספקת הגנה נוספת על נתונים אישיים למשתמשים. באופן ספציפי, היא מעניקה למשתמשים את הזכות לבקש מחיקה או הסרה של נתונים אישיים מחיפושים באינטרנט וממקומות אחרים, _בתנאים מסוימים_ - ומאפשרת להם התחלה חדשה ברשת מבלי שפעולות עבר יעמדו נגדם.

שאלות לחקור כאן הן:
 * האם המערכת מאפשרת לנושאי נתונים לבקש מחיקה?
 * האם ביטול הסכמת המשתמש צריך להפעיל מחיקה אוטומטית?
 * האם נתונים נאספו ללא הסכמה או באמצעים בלתי חוקיים?
 * האם אנו עומדים בתקנות ממשלתיות לפרטיות נתונים?

#### 2.6 הטיות במאגרי נתונים

הטיות במאגרי נתונים או [הטיות באיסוף](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) עוסקות בבחירת תת-קבוצה _לא מייצגת_ של נתונים לפיתוח אלגוריתמים, מה שיוצר פוטנציאל לחוסר הוגנות בתוצאות עבור קבוצות מגוונות. סוגי הטיות כוללים הטיית בחירה או דגימה, הטיית מתנדבים, והטיית מכשירים.

שאלות לחקור כאן הן:
 * האם גייסנו קבוצה מייצגת של נושאי נתונים?
 * האם בדקנו את מאגר הנתונים שנאסף או נאצר עבור הטיות שונות?
 * האם אנו יכולים למזער או להסיר הטיות שהתגלו?

#### 2.7 איכות נתונים

[איכות נתונים](https://lakefs.io/data-quality-testing/) בוחנת את תקפות מאגר הנתונים שנאצר לשם פיתוח האלגוריתמים שלנו, ובודקת אם התכונות והרשומות עומדות בדרישות לרמת דיוק ועקביות הנדרשת למטרת ה-AI שלנו.

שאלות לחקור כאן הן:
 * האם לכדנו תכונות _תקפות_ למקרה השימוש שלנו?
 * האם נתונים נלכדו _בעקביות_ ממקורות נתונים מגוונים?
 * האם מאגר הנתונים _שלם_ עבור תנאים או תרחישים מגוונים?
 * האם מידע שנלכד _מדויק_ ומשקף את המציאות?
[Algorithm Fairness](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) בודק האם עיצוב האלגוריתם מפלה באופן שיטתי נגד קבוצות משנה מסוימות של נבדקים, מה שמוביל ל[נזקים פוטנציאליים](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) ב_הקצאה_ (כאשר משאבים נשללים או נמנעים מאותה קבוצה) וב_איכות השירות_ (כאשר הבינה המלאכותית אינה מדויקת באותה מידה עבור קבוצות משנה מסוימות כמו שהיא עבור אחרות).

שאלות שכדאי לבחון כאן:
 * האם הערכנו את דיוק המודל עבור קבוצות משנה ותנאים מגוונים?
 * האם בחנו את המערכת לנזקים פוטנציאליים (לדוגמה, סטריאוטיפים)?
 * האם ניתן לשנות נתונים או לאמן מחדש מודלים כדי לצמצם נזקים שזוהו?

חקור משאבים כמו [AI Fairness checklists](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) כדי ללמוד עוד.

#### 2.9 ייצוג שגוי

[ייצוג שגוי של נתונים](https://www.sciencedirect.com/topics/computer-science/misrepresentation) עוסק בשאלה האם אנו מעבירים תובנות מנתונים שדווחו בכנות באופן מטעה כדי לתמוך בנרטיב רצוי.

שאלות שכדאי לבחון כאן:
 * האם אנו מדווחים נתונים לא שלמים או לא מדויקים?
 * האם אנו מציגים נתונים באופן שמוביל למסקנות מטעות?
 * האם אנו משתמשים בטכניקות סטטיסטיות סלקטיביות כדי לעוות תוצאות?
 * האם קיימות הסברים חלופיים שיכולים להציע מסקנה שונה?

#### 2.10 בחירה חופשית
[אשליית הבחירה החופשית](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) מתרחשת כאשר "ארכיטקטורות בחירה" של מערכות משתמשות באלגוריתמים לקבלת החלטות כדי להניע אנשים לקחת תוצאה מועדפת תוך יצירת רושם שיש להם אפשרויות ושליטה. [דפוסים אפלים](https://www.darkpatterns.org/) אלו יכולים לגרום לנזקים חברתיים וכלכליים למשתמשים. מכיוון שהחלטות משתמש משפיעות על פרופילי התנהגות, פעולות אלו עשויות להניע בחירות עתידיות שיכולות להעצים או להרחיב את השפעת הנזקים הללו.

שאלות שכדאי לבחון כאן:
 * האם המשתמש הבין את ההשלכות של קבלת הבחירה הזו?
 * האם המשתמש היה מודע לבחירות (חלופיות) וליתרונות והחסרונות של כל אחת?
 * האם המשתמש יכול להפוך בחירה אוטומטית או מושפעת מאוחר יותר?

### 3. מחקרי מקרה

כדי לשים את האתגרים האתיים הללו בהקשרים של העולם האמיתי, כדאי לבחון מחקרי מקרה שמדגישים את הנזקים וההשלכות הפוטנציאליים על יחידים וחברה, כאשר הפרות אתיות כאלה נעלמות מעינינו.

להלן כמה דוגמאות:

| אתגר אתי | מחקר מקרה | 
|--- |--- |
| **הסכמה מדעת** | 1972 - [מחקר העגבת בטסקיגי](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - גברים אפרו-אמריקאים שהשתתפו במחקר הובטחה להם טיפול רפואי חינם _אך הוטעו_ על ידי חוקרים שלא יידעו את הנבדקים על האבחנה שלהם או על זמינות הטיפול. רבים מהנבדקים מתו, ושותפים או ילדים נפגעו; המחקר נמשך 40 שנה. | 
| **פרטיות נתונים** | 2007 - [פרס נתוני נטפליקס](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) סיפק לחוקרים _10 מיליון דירוגי סרטים אנונימיים מ-50 אלף לקוחות_ כדי לעזור לשפר אלגוריתמי המלצות. עם זאת, החוקרים הצליחו לקשר נתונים אנונימיים לנתונים מזהים אישית ב_מאגרי נתונים חיצוניים_ (לדוגמה, תגובות IMDb) - למעשה "דה-אנונימיזציה" של חלק ממנויי נטפליקס.|
| **הטיה באיסוף נתונים** | 2013 - עיריית בוסטון [פיתחה את Street Bump](https://www.boston.gov/transportation/street-bump), אפליקציה שאפשרה לתושבים לדווח על בורות, מה שנתן לעיר נתוני כבישים טובים יותר כדי למצוא ולתקן בעיות. עם זאת, [לאנשים בקבוצות הכנסה נמוכה הייתה פחות גישה למכוניות וטלפונים](https://hbr.org/2013/04/the-hidden-biases-in-big-data), מה שהפך את בעיות הכבישים שלהם לבלתי נראות באפליקציה זו. המפתחים עבדו עם אקדמאים כדי לטפל ב_נושאי גישה שוויונית ופערים דיגיטליים_ למען הוגנות. |
| **הוגנות אלגוריתמית** | 2018 - מחקר [Gender Shades של MIT](http://gendershades.org/overview.html) העריך את דיוק מוצרי AI לסיווג מגדר, וחשף פערים בדיוק עבור נשים ואנשים בעלי צבע עור כהה. [כרטיס האשראי של אפל ב-2019](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) נראה שהציע פחות אשראי לנשים מאשר לגברים. שניהם הדגימו בעיות בהטיה אלגוריתמית שהובילה לנזקים חברתיים-כלכליים.|
| **ייצוג שגוי של נתונים** | 2020 - [משרד הבריאות של ג'ורג'יה פרסם גרפים של מקרי COVID-19](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) שנראה כי הטעו את האזרחים לגבי מגמות במקרים מאושרים עם סדר לא כרונולוגי על ציר ה-x. זה מדגים ייצוג שגוי באמצעות טריקים ויזואליים. |
| **אשליית הבחירה החופשית** | 2020 - אפליקציית הלמידה [ABCmouse שילמה 10 מיליון דולר כדי ליישב תלונה של ה-FTC](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) שבה הורים נלכדו בתשלום עבור מנויים שלא יכלו לבטל. זה מדגים דפוסים אפלים בארכיטקטורות בחירה, שבהן משתמשים הונעו לעבר בחירות שעלולות להזיק. |
| **פרטיות נתונים וזכויות משתמש** | 2021 - [פרצת נתונים בפייסבוק](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) חשפה נתונים מ-530 מיליון משתמשים, מה שהוביל להסדר של 5 מיליארד דולר עם ה-FTC. עם זאת, החברה סירבה להודיע למשתמשים על הפרצה, מה שהפר את זכויות המשתמשים בנוגע לשקיפות נתונים וגישה. |

רוצה לחקור עוד מחקרי מקרה? בדוק את המשאבים הבאים:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - דילמות אתיות בתעשיות מגוונות. 
* [קורס אתיקה במדעי הנתונים](https://www.coursera.org/learn/data-science-ethics#syllabus) - מחקרי מקרה מרכזיים נבחנים.
* [מקרים שבהם דברים השתבשו](https://deon.drivendata.org/examples/) - רשימת בדיקה של Deon עם דוגמאות.

> 🚨 חשבו על מחקרי המקרה שראיתם - האם חוויתם או הושפעתם מאתגר אתי דומה בחייכם? האם אתם יכולים לחשוב על לפחות מחקר מקרה אחד נוסף שממחיש אחד מהאתגרים האתיים שדנו בהם בסעיף זה?

## אתיקה יישומית

דיברנו על מושגי אתיקה, אתגרים ומחקרי מקרה בהקשרים של העולם האמיתי. אבל איך מתחילים _ליישם_ עקרונות ושיטות אתיים בפרויקטים שלנו? ואיך _מפעילים_ את השיטות הללו למען ממשל טוב יותר? בואו נחקור כמה פתרונות בעולם האמיתי:

### 1. קודים מקצועיים

קודים מקצועיים מציעים אפשרות אחת לארגונים "לתמרץ" חברים לתמוך בעקרונות האתיים שלהם ובהצהרת המשימה. קודים הם _הנחיות מוסריות_ להתנהגות מקצועית, המסייעים לעובדים או חברים לקבל החלטות שמתיישרות עם עקרונות הארגון שלהם. הם טובים רק כמו הציות מרצון מצד החברים; עם זאת, ארגונים רבים מציעים תגמולים ועונשים נוספים כדי להניע ציות מצד החברים.

דוגמאות כוללות:

 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Code of Ethics
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Code of Conduct (נוצר ב-2013)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (מאז 1993)

> 🚨 האם אתם חברים בארגון מקצועי להנדסה או מדעי הנתונים? חקרו את האתר שלהם כדי לראות אם הם מגדירים קוד אתיקה מקצועי. מה זה אומר על העקרונות האתיים שלהם? איך הם "מתמרצים" חברים לעקוב אחרי הקוד?

### 2. רשימות בדיקה אתיות

בעוד שקודים מקצועיים מגדירים _התנהגות אתית נדרשת_ מצד העוסקים בתחום, הם [מוגבלים ידועים](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) באכיפה, במיוחד בפרויקטים רחבי היקף. במקום זאת, מומחי מדעי הנתונים רבים [ממליצים על רשימות בדיקה](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), שיכולות **לחבר עקרונות לשיטות** בדרכים יותר דטרמיניסטיות וניתנות לפעולה.

רשימות בדיקה ממירות שאלות למשימות "כן/לא" שניתן להפעיל, ומאפשרות לעקוב אחריהן כחלק מזרימות עבודה סטנדרטיות לשחרור מוצרים.

דוגמאות כוללות:
 * [Deon](https://deon.drivendata.org/) - רשימת בדיקה כללית לאתיקה במדעי הנתונים שנוצרה מתוך [המלצות תעשייה](https://deon.drivendata.org/#checklist-citations) עם כלי שורת פקודה לשילוב קל.
 * [Privacy Audit Checklist](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - מספקת הנחיות כלליות לשיטות טיפול במידע מנקודות מבט משפטיות וחברתיות.
 * [AI Fairness Checklist](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - נוצרה על ידי מומחי AI כדי לתמוך באימוץ ושילוב בדיקות הוגנות במחזורי פיתוח AI.
 * [22 שאלות לאתיקה במדעי הנתונים ובינה מלאכותית](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - מסגרת פתוחה יותר, מובנית לחקירה ראשונית של סוגיות אתיות בעיצוב, יישום והקשרים ארגוניים.

### 3. רגולציות אתיות

אתיקה עוסקת בהגדרת ערכים משותפים ועשיית הדבר הנכון _מרצון_. **ציות** עוסק ב_עמידה בחוק_ אם וכאשר מוגדר. **ממשל** מכסה באופן רחב את כל הדרכים שבהן ארגונים פועלים כדי לאכוף עקרונות אתיים ולעמוד בחוקים שנקבעו.

כיום, ממשל לובש שתי צורות בתוך ארגונים. ראשית, מדובר בהגדרת עקרונות **AI אתיים** וביסוס שיטות להפעלת אימוץ בכל הפרויקטים הקשורים ל-AI בארגון. שנית, מדובר בעמידה בכל **רגולציות הגנת נתונים** שהממשלה מחייבת עבור האזורים שבהם היא פועלת.

דוגמאות לרגולציות הגנת נתונים ופרטיות:
 * `1974`, [חוק הפרטיות בארה"ב](https://www.justice.gov/opcl/privacy-act-1974) - מסדיר את איסוף, השימוש והגילוי של מידע אישי על ידי _הממשלה הפדרלית_.
 * `1996`, [חוק הניידות והאחריות של ביטוח בריאות בארה"ב (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - מגן על נתוני בריאות אישיים.
 * `1998`, [חוק הגנת פרטיות ילדים באינטרנט בארה"ב (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - מגן על פרטיות נתונים של ילדים מתחת לגיל 13.
 * `2018`, [רגולציית הגנת נתונים כללית (GDPR)](https://gdpr-info.eu/) - מספקת זכויות משתמש, הגנת נתונים ופרטיות.
 * `2018`, [חוק פרטיות הצרכן של קליפורניה (CCPA)](https://www.oag.ca.gov/privacy/ccpa) מעניק לצרכנים יותר _זכויות_ על הנתונים האישיים שלהם.
 * `2021`, חוק [הגנת מידע אישי של סין](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) עבר זה עתה, ויוצר אחת הרגולציות החזקות ביותר לפרטיות נתונים באינטרנט בעולם.

> 🚨 האיחוד האירופי הגדיר את GDPR (רגולציית הגנת נתונים כללית) שנשארת אחת הרגולציות המשפיעות ביותר לפרטיות נתונים כיום. האם ידעתם שהיא גם מגדירה [8 זכויות משתמש](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) כדי להגן על פרטיות דיגיטלית ומידע אישי של אזרחים? למדו על מה הן, ולמה הן חשובות.

### 4. תרבות אתית

שימו לב שעדיין קיים פער בלתי מוחשי בין _ציות_ (עשיית מספיק כדי לעמוד "באות החוק") לבין טיפול ב[בעיות מערכתיות](https://www.coursera.org/learn/data-science-ethics/home/week/4) (כמו אוסיפיקציה, אסימטריה מידעית ואי-שוויון חלוקתי) שיכולות להאיץ את חימוש ה-AI.

האחרון דורש [גישות שיתופיות להגדרת תרבויות אתיות](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f) שבונות קשרים רגשיים וערכים משותפים עקביים _בין ארגונים_ בתעשייה. זה קורא ליותר [תרבויות אתיות פורמליות במדעי הנתונים](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) בארגונים - שמאפשרות _לכל אחד_ [למשוך את חוט האנדון](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (כדי להעלות חששות אתיים מוקדם בתהליך) והופכות _הערכות אתיות_ (לדוגמה, בגיוס עובדים) לקריטריון מרכזי בהרכבת צוותים בפרויקטים של AI.

---
## [שאלון לאחר ההרצאה](https://ff-quizzes.netlify.app/en/ds/) 🎯
## סקירה ולימוד עצמי

קורסים וספרים עוזרים בהבנת מושגי אתיקה מרכזיים ואתגרים, בעוד שמחקרי מקרה וכלים עוזרים בשיטות אתיקה יישומיות בהקשרים של העולם האמיתי. הנה כמה משאבים להתחיל איתם:

* [Machine Learning For Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - שיעור על הוגנות, ממיקרוסופט.
* [עקרונות הבינה המלאכותית האחראית](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - מסלול לימוד חינמי מ-Microsoft Learn.  
* [אתיקה ומדעי הנתונים](https://resources.oreilly.com/examples/0636920203964) - ספר אלקטרוני של O'Reilly (מ. לוקיידס, ה. מייסון ואחרים).  
* [אתיקה במדעי הנתונים](https://www.coursera.org/learn/data-science-ethics#syllabus) - קורס מקוון מאוניברסיטת מישיגן.  
* [אתיקה ללא כיסוי](https://ethicsunwrapped.utexas.edu/case-studies) - מחקרי מקרה מאוניברסיטת טקסס.  

# משימה  

[כתיבת מחקר מקרה בנושא אתיקה בנתונים](assignment.md)  

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.