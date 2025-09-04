<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "79ca8a5a3135e94d2d43f56ba62d5205",
  "translation_date": "2025-09-04T20:06:23+00:00",
  "source_file": "4-Data-Science-Lifecycle/14-Introduction/README.md",
  "language_code": "he"
}
-->
# מבוא למחזור החיים של מדעי הנתונים

|![ סקצ'נוט מאת [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/14-DataScience-Lifecycle.png)|
|:---:|
| מבוא למחזור החיים של מדעי הנתונים - _סקצ'נוט מאת [@nitya](https://twitter.com/nitya)_ |

## [שאלון לפני השיעור](https://red-water-0103e7a0f.azurestaticapps.net/quiz/26)

בשלב זה, כנראה כבר הבנתם שמדעי הנתונים הם תהליך. תהליך זה ניתן לחלק לחמישה שלבים:

- איסוף
- עיבוד
- ניתוח
- תקשורת
- תחזוקה

השיעור הזה מתמקד בשלושה חלקים מתוך מחזור החיים: איסוף, עיבוד ותחזוקה.

![תרשים של מחזור החיים של מדעי הנתונים](../../../../translated_images/data-science-lifecycle.a1e362637503c4fb0cd5e859d7552edcdb4aa629a279727008baa121f2d33f32.he.jpg)
> תמונה מאת [Berkeley School of Information](https://ischoolonline.berkeley.edu/data-science/what-is-data-science/)

## איסוף

השלב הראשון במחזור החיים הוא חשוב מאוד, שכן השלבים הבאים תלויים בו. למעשה, מדובר בשני שלבים שמאוחדים לאחד: רכישת הנתונים והגדרת המטרה והבעיות שיש לטפל בהן.  
הגדרת מטרות הפרויקט תדרוש הבנה מעמיקה יותר של הבעיה או השאלה. ראשית, עלינו לזהות ולרכוש את מי שזקוקים לפתרון הבעיה שלהם. אלו יכולים להיות בעלי עניין בעסק או נותני חסות לפרויקט, שיכולים לעזור לזהות מי או מה ייהנה מהפרויקט הזה, כמו גם מה הם צריכים ולמה. מטרה מוגדרת היטב צריכה להיות מדידה וכמותית כדי להגדיר תוצאה מקובלת.

שאלות שמדען נתונים עשוי לשאול:
- האם הבעיה הזו נבחנה בעבר? מה התגלה?
- האם המטרה והיעד מובנים על ידי כל המעורבים?
- האם יש עמימות וכיצד ניתן להפחית אותה?
- מהם המגבלות?
- איך תיראה התוצאה הסופית?
- כמה משאבים (זמן, אנשים, חישוביים) זמינים?

השלב הבא הוא זיהוי, איסוף ולבסוף חקר הנתונים הדרושים להשגת המטרות שהוגדרו. בשלב זה של רכישת הנתונים, מדעני נתונים חייבים גם להעריך את הכמות והאיכות של הנתונים. זה דורש חקר נתונים כדי לאשר שהנתונים שנאספו יתמכו בהשגת התוצאה הרצויה.

שאלות שמדען נתונים עשוי לשאול על הנתונים:
- אילו נתונים כבר זמינים לי?
- מי הבעלים של הנתונים האלה?
- מהם החששות לגבי פרטיות?
- האם יש לי מספיק נתונים כדי לפתור את הבעיה?
- האם הנתונים באיכות מספקת עבור הבעיה הזו?
- אם אני מגלה מידע נוסף דרך הנתונים האלה, האם כדאי לשקול לשנות או להגדיר מחדש את המטרות?

## עיבוד

שלב העיבוד במחזור החיים מתמקד בגילוי דפוסים בנתונים ובבניית מודלים. חלק מהטכניקות בשלב העיבוד דורשות שיטות סטטיסטיות כדי לחשוף את הדפוסים. בדרך כלל, זו תהיה משימה מייגעת עבור אדם להתמודד עם מערך נתונים גדול, ולכן מסתמכים על מחשבים כדי להאיץ את התהליך. בשלב זה מדעי הנתונים ולמידת מכונה מצטלבים. כפי שלמדתם בשיעור הראשון, למידת מכונה היא תהליך בניית מודלים להבנת הנתונים. מודלים הם ייצוג של הקשר בין משתנים בנתונים שמסייעים לחזות תוצאות.

טכניקות נפוצות בשלב זה מכוסות בתוכנית הלימודים של ML למתחילים. עקבו אחר הקישורים כדי ללמוד עליהן:

- [סיווג](https://github.com/microsoft/ML-For-Beginners/tree/main/4-Classification): ארגון נתונים לקטגוריות לשימוש יעיל יותר.
- [אשכולות](https://github.com/microsoft/ML-For-Beginners/tree/main/5-Clustering): קיבוץ נתונים לקבוצות דומות.
- [רגרסיה](https://github.com/microsoft/ML-For-Beginners/tree/main/2-Regression): קביעת הקשרים בין משתנים כדי לחזות או לצפות ערכים.

## תחזוקה

בתרשים של מחזור החיים, אולי שמתם לב שתחזוקה נמצאת בין איסוף לעיבוד. תחזוקה היא תהליך מתמשך של ניהול, אחסון ואבטחת הנתונים לאורך כל תהליך הפרויקט, ויש לקחת אותה בחשבון לאורך כל הפרויקט.

### אחסון נתונים
שיקולים לגבי איך והיכן הנתונים מאוחסנים יכולים להשפיע על עלות האחסון כמו גם על ביצועי הגישה לנתונים. החלטות כאלה לא סביר שיתקבלו על ידי מדען נתונים בלבד, אך ייתכן שהוא יצטרך לבחור כיצד לעבוד עם הנתונים בהתאם לאופן שבו הם מאוחסנים.

הנה כמה היבטים של מערכות אחסון נתונים מודרניות שיכולים להשפיע על הבחירות הללו:

**במקום מול מחוץ למקום מול ענן ציבורי או פרטי**

"במקום" מתייחס לאחסון וניהול הנתונים על ציוד בבעלותכם, כמו שרת עם כוננים קשיחים שמאחסנים את הנתונים, בעוד "מחוץ למקום" מסתמך על ציוד שאינו בבעלותכם, כמו מרכז נתונים. הענן הציבורי הוא בחירה פופולרית לאחסון נתונים שאינה דורשת ידע על איך או איפה בדיוק הנתונים מאוחסנים, כאשר "ציבורי" מתייחס לתשתית אחידה שמשותפת לכל מי שמשתמש בענן. חלק מהארגונים מחזיקים במדיניות אבטחה מחמירה שדורשת גישה מלאה לציוד שבו הנתונים מאוחסנים, ולכן הם מסתמכים על ענן פרטי שמספק שירותי ענן משלו. תלמדו יותר על נתונים בענן בשיעורים [מאוחרים יותר](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/5-Data-Science-In-Cloud).

**נתונים "קרים" מול נתונים "חמים"**

כאשר אתם מאמנים את המודלים שלכם, ייתכן שתזדקקו ליותר נתוני אימון. אם אתם מרוצים מהמודל שלכם, נתונים נוספים יגיעו כדי שהמודל יוכל לשרת את מטרתו. בכל מקרה, עלות אחסון וגישה לנתונים תגדל ככל שתצברו יותר מהם. הפרדת נתונים שנעשה בהם שימוש לעיתים רחוקות, המכונים נתונים "קרים", מנתונים שנעשה בהם שימוש תדיר, המכונים נתונים "חמים", יכולה להיות אפשרות אחסון נתונים זולה יותר באמצעות שירותי חומרה או תוכנה. אם יש צורך לגשת לנתונים "קרים", ייתכן שייקח מעט יותר זמן לשלוף אותם בהשוואה לנתונים "חמים".

### ניהול נתונים
במהלך העבודה עם נתונים, ייתכן שתגלו שחלק מהנתונים צריכים לעבור ניקוי באמצעות הטכניקות שנלמדו בשיעור על [הכנת נתונים](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/08-data-preparation) כדי לבנות מודלים מדויקים. כאשר נתונים חדשים מגיעים, יהיה צורך ליישם את אותן טכניקות כדי לשמור על עקביות באיכות. חלק מהפרויקטים יכללו שימוש בכלי אוטומטי לניקוי, צבירה ודחיסה לפני שהנתונים מועברים למיקומם הסופי. Azure Data Factory הוא דוגמה לאחד הכלים הללו.

### אבטחת נתונים
אחד היעדים המרכזיים באבטחת נתונים הוא להבטיח שמי שעובד עם הנתונים שולט במה שנאסף ובאיזה הקשר נעשה בו שימוש. שמירה על אבטחת נתונים כוללת הגבלת גישה רק למי שזקוק לה, עמידה בחוקים ובתקנות המקומיים, כמו גם שמירה על סטנדרטים אתיים, כפי שנלמד בשיעור על [אתיקה](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/02-ethics).

הנה כמה דברים שצוות עשוי לעשות מתוך מחשבה על אבטחה:
- לוודא שכל הנתונים מוצפנים
- לספק ללקוחות מידע על איך הנתונים שלהם משמשים
- להסיר גישה לנתונים ממי שעזב את הפרויקט
- לאפשר רק לחברי פרויקט מסוימים לשנות את הנתונים

## 🚀 אתגר

ישנם גרסאות רבות למחזור החיים של מדעי הנתונים, כאשר כל שלב עשוי להיקרא בשם שונה או לכלול מספר שונה של שלבים, אך יכיל את אותם תהליכים שהוזכרו בשיעור הזה.

חקור את [מחזור החיים של תהליך מדעי הנתונים בצוות](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/lifecycle) ואת [התקן התעשייתי לתהליך כריית נתונים](https://www.datascience-pm.com/crisp-dm-2/). ציין 3 דמיון ו-3 הבדלים בין השניים.

|תהליך מדעי הנתונים בצוות (TDSP)|התקן התעשייתי לתהליך כריית נתונים (CRISP-DM)|
|--|--|
|![מחזור החיים של מדעי הנתונים בצוות](../../../../translated_images/tdsp-lifecycle2.e19029d598e2e73d5ef8a4b98837d688ec6044fe332c905d4dbb69eb6d5c1d96.he.png) | ![תמונה של תהליך מדעי הנתונים](../../../../translated_images/CRISP-DM.8bad2b4c66e62aa75278009e38e3e99902c73b0a6f63fd605a67c687a536698c.he.png) |
| תמונה מאת [Microsoft](https://docs.microsoft.comazure/architecture/data-science-process/lifecycle) | תמונה מאת [Data Science Process Alliance](https://www.datascience-pm.com/crisp-dm-2/) |

## [שאלון אחרי השיעור](https://ff-quizzes.netlify.app/en/ds/)

## סקירה ולימוד עצמי

יישום מחזור החיים של מדעי הנתונים כולל תפקידים ומשימות מרובים, כאשר חלקם עשויים להתמקד בחלקים מסוימים בכל שלב. תהליך מדעי הנתונים בצוות מספק כמה משאבים שמסבירים את סוגי התפקידים והמשימות שמישהו עשוי לבצע בפרויקט.

* [תפקידים ומשימות בתהליך מדעי הנתונים בצוות](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/roles-tasks)
* [ביצוע משימות מדעי נתונים: חקר, בניית מודלים ופריסה](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/execute-data-science-tasks)

## משימה

[הערכת מערך נתונים](assignment.md)

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.