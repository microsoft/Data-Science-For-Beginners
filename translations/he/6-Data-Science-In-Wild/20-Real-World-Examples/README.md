<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "06bac7959b46b6e8aedcae014278c476",
  "translation_date": "2025-09-05T23:29:15+00:00",
  "source_file": "6-Data-Science-In-Wild/20-Real-World-Examples/README.md",
  "language_code": "he"
}
-->
# מדע הנתונים בעולם האמיתי

| ![ סקיצה מאת [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-RealWorld.png) |
| :--------------------------------------------------------------------------------------------------------------: |
|               מדע הנתונים בעולם האמיתי - _סקיצה מאת [@nitya](https://twitter.com/nitya)_               |

אנחנו כמעט בסוף מסע הלמידה הזה!

התחלנו עם הגדרות של מדע הנתונים ואתיקה, חקרנו כלים וטכניקות שונות לניתוח ויזואליזציה של נתונים, סקרנו את מחזור החיים של מדע הנתונים, ובחנו כיצד ניתן להרחיב ולייעל תהליכי עבודה של מדע הנתונים באמצעות שירותי מחשוב ענן. אז אתם בטח שואלים: _"איך בדיוק אני ממפה את כל הלמידות הללו להקשרים בעולם האמיתי?"_

בשיעור הזה, נחקור יישומים בעולם האמיתי של מדע הנתונים בתעשייה ונצלול לדוגמאות ספציפיות במחקר, מדעי הרוח הדיגיטליים וקיימות. נבחן הזדמנויות לפרויקטים לסטודנטים ונסיים עם משאבים שימושיים שיעזרו לכם להמשיך את מסע הלמידה שלכם!

## שאלון לפני השיעור

## [שאלון לפני השיעור](https://ff-quizzes.netlify.app/en/ds/quiz/38)

## מדע הנתונים + תעשייה

בזכות הדמוקרטיזציה של AI, מפתחים מוצאים כיום קל יותר לעצב ולשלב תובנות מונעות AI והחלטות מבוססות נתונים בחוויות משתמש ובתהליכי פיתוח. הנה כמה דוגמאות כיצד מדע הנתונים "מיושם" ביישומים בעולם האמיתי בתעשייה:

 * [Google Flu Trends](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) השתמש במדע הנתונים כדי לקשר בין מונחי חיפוש למגמות שפעת. למרות שהגישה הייתה פגומה, היא העלתה מודעות לאפשרויות (ולאתגרים) של תחזיות בריאות מבוססות נתונים.

 * [UPS Routing Predictions](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - מסביר כיצד UPS משתמשת במדע הנתונים ובלמידת מכונה כדי לחזות מסלולים אופטימליים למשלוח, תוך התחשבות בתנאי מזג האוויר, דפוסי תנועה, מועדי אספקה ועוד.

 * [NYC Taxicab Route Visualization](http://chriswhong.github.io/nyctaxi/) - נתונים שנאספו באמצעות [חוקי חופש המידע](https://chriswhong.com/open-data/foil_nyc_taxi/) סייעו להמחיש יום בחיי המוניות בניו יורק, ועזרו לנו להבין כיצד הן מנווטות בעיר העמוסה, הכסף שהן מרוויחות, ומשך הנסיעות בכל תקופה של 24 שעות.

 * [Uber Data Science Workbench](https://eng.uber.com/dsw/) - משתמש בנתונים (על מיקומי איסוף והורדה, משך נסיעות, מסלולים מועדפים וכו') שנאספו ממיליוני נסיעות יומיות של Uber כדי לבנות כלי אנליטיקה נתונים המסייע בתמחור, בטיחות, זיהוי הונאות והחלטות ניווט.

 * [Sports Analytics](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - מתמקד ב_אנליטיקה חזויה_ (ניתוח קבוצות ושחקנים - כמו [Moneyball](https://datasciencedegree.wisconsin.edu/blog/moneyball-proves-importance-big-data-big-ideas/) - וניהול אוהדים) וב_ויזואליזציה של נתונים_ (לוחות מחוונים של קבוצות ואוהדים, משחקים וכו') עם יישומים כמו סקאוטינג כישרונות, הימורים ספורטיביים וניהול מלאי/מקומות.

 * [Data Science in Banking](https://data-flair.training/blogs/data-science-in-banking/) - מדגיש את הערך של מדע הנתונים בתעשיית הפיננסים עם יישומים החל ממידול סיכונים וזיהוי הונאות, ועד סגמנטציה של לקוחות, תחזיות בזמן אמת ומערכות המלצה. אנליטיקה חזויה גם מניעה מדדים קריטיים כמו [ציוני אשראי](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit).

 * [Data Science in Healthcare](https://data-flair.training/blogs/data-science-in-healthcare/) - מדגיש יישומים כמו הדמיה רפואית (למשל, MRI, רנטגן, CT-Scan), גנומיקה (ריצוף DNA), פיתוח תרופות (הערכת סיכונים, תחזית הצלחה), אנליטיקה חזויה (טיפול בחולים ולוגיסטיקה של אספקה), מעקב ומניעת מחלות ועוד.

![יישומי מדע הנתונים בעולם האמיתי](../../../../6-Data-Science-In-Wild/20-Real-World-Examples/images/data-science-applications.png) קרדיט תמונה: [Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

התרשים מציג תחומים ודוגמאות נוספים ליישום טכניקות מדע הנתונים. רוצים לחקור יישומים נוספים? בדקו את [סקירה ולימוד עצמי](../../../../6-Data-Science-In-Wild/20-Real-World-Examples) למטה.

## מדע הנתונים + מחקר

| ![ סקיצה מאת [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Research.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              מדע הנתונים ומחקר - _סקיצה מאת [@nitya](https://twitter.com/nitya)_              |

בעוד שיישומים בעולם האמיתי מתמקדים לעיתים קרובות במקרי שימוש בתעשייה בקנה מידה רחב, יישומי _מחקר_ ופרויקטים יכולים להיות שימושיים משתי פרספקטיבות:

* _הזדמנויות חדשנות_ - חקר אב טיפוס מהיר של רעיונות מתקדמים ובדיקת חוויות משתמש ליישומים של הדור הבא.
* _אתגרי פריסה_ - חקר נזקים פוטנציאליים או השלכות בלתי צפויות של טכנולוגיות מדע הנתונים בהקשרים בעולם האמיתי.

עבור סטודנטים, פרויקטי מחקר יכולים לספק גם הזדמנויות למידה ושיתוף פעולה שיכולות לשפר את ההבנה שלכם בנושא, ולהרחיב את המודעות והמעורבות שלכם עם אנשים או צוותים רלוונטיים שעובדים בתחומי עניין. אז איך נראים פרויקטי מחקר וכיצד הם יכולים להשפיע?

בואו נבחן דוגמה אחת - [MIT Gender Shades Study](http://gendershades.org/overview.html) של ג'וי בואולמוויני (MIT Media Labs) עם [מאמר מחקר מוביל](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf) שנכתב בשיתוף עם טימניט גברו (אז ב-Microsoft Research) שהתמקד ב:

 * **מה:** מטרת פרויקט המחקר הייתה _להעריך הטיה קיימת באלגוריתמים ובמאגרי נתונים של ניתוח פנים אוטומטי_ בהתבסס על מגדר וסוג עור.
 * **למה:** ניתוח פנים משמש בתחומים כמו אכיפת חוק, אבטחת שדות תעופה, מערכות גיוס ועוד - הקשרים שבהם סיווגים לא מדויקים (למשל, עקב הטיה) יכולים לגרום לנזקים כלכליים וחברתיים פוטנציאליים לאנשים או קבוצות מושפעות. הבנת הטיות (והסרתן או הפחתתן) היא מפתח להוגנות בשימוש.
 * **איך:** החוקרים זיהו שמדדי הביצועים הקיימים השתמשו בעיקר בנבדקים בעלי עור בהיר, ואספו מאגר נתונים חדש (1000+ תמונות) שהיה _מאוזן יותר_ לפי מגדר וסוג עור. מאגר הנתונים שימש להערכת דיוק של שלושה מוצרים לסיווג מגדר (מ-Microsoft, IBM ו-Face++).

התוצאות הראו שלמרות שהדיוק הכולל בסיווג היה טוב, הייתה הבחנה ניכרת בשיעורי השגיאות בין קבוצות שונות - עם **שגיאות סיווג מגדרי** גבוהות יותר לנשים או אנשים בעלי עור כהה, מה שמעיד על הטיה.

**תוצאות מרכזיות:** העלאת מודעות לכך שמדע הנתונים זקוק ל_מאגרי נתונים מייצגים יותר_ (קבוצות מאוזנות) ול_צוותים כוללים יותר_ (רקע מגוון) כדי לזהות ולהסיר או להפחית הטיות כאלה מוקדם יותר בפתרונות AI. מאמצי מחקר כמו זה גם תורמים להגדרת עקרונות ופרקטיקות ל_בינה מלאכותית אחראית_ בארגונים רבים כדי לשפר את ההוגנות במוצרים ותהליכים של AI.

**רוצים ללמוד על מאמצי מחקר רלוונטיים ב-Microsoft?**

* בדקו את [פרויקטי המחקר של Microsoft](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project) בתחום הבינה המלאכותית.
* חקרו פרויקטים לסטודנטים מ[בית הספר לקיץ במדע הנתונים של Microsoft Research](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/).
* בדקו את פרויקט [Fairlearn](https://fairlearn.org/) ואת יוזמות [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6).

## מדע הנתונים + מדעי הרוח

| ![ סקיצה מאת [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              מדע הנתונים ומדעי הרוח הדיגיטליים - _סקיצה מאת [@nitya](https://twitter.com/nitya)_              |

מדעי הרוח הדיגיטליים [הוגדרו](https://digitalhumanities.stanford.edu/about-dh-stanford) כ"אוסף של פרקטיקות וגישות המשלבות שיטות חישוביות עם חקירה הומניסטית". [פרויקטים של סטנפורד](https://digitalhumanities.stanford.edu/projects) כמו _"היסטוריה מחדש"_ ו_"חשיבה פואטית"_ מדגימים את הקשר בין [מדעי הרוח הדיגיטליים ומדע הנתונים](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science) - תוך הדגשת טכניקות כמו ניתוח רשתות, ויזואליזציה של מידע, ניתוח מרחבי וטקסט שיכולים לעזור לנו לבחון מחדש מערכי נתונים היסטוריים וספרותיים כדי להפיק תובנות ופרספקטיבות חדשות.

*רוצים לחקור ולהרחיב פרויקט בתחום הזה?*

בדקו את ["אמילי דיקנסון ומטר המצב רוח"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671) - דוגמה נהדרת מ[ג'ן לופר](https://twitter.com/jenlooper) ששואלת כיצד נוכל להשתמש במדע הנתונים כדי לבחון מחדש שירה מוכרת ולהעריך מחדש את משמעותה ואת תרומתה של המחברת בהקשרים חדשים. לדוגמה, _האם נוכל לחזות את העונה שבה נכתבה שירה על ידי ניתוח הטון או הרגש שלה_ - ומה זה אומר על מצב הרוח של המחברת בתקופה הרלוונטית?

כדי לענות על השאלה הזו, אנו עוקבים אחר שלבי מחזור החיים של מדע הנתונים:
 * [`רכישת נתונים`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#acquiring-the-dataset) - לאסוף מערך נתונים רלוונטי לניתוח. אפשרויות כוללות שימוש ב-API (למשל, [Poetry DB API](https://poetrydb.org/index.html)) או גרידת דפי אינטרנט (למשל, [Project Gutenberg](https://www.gutenberg.org/files/12242/12242-h/12242-h.htm)) באמצעות כלים כמו [Scrapy](https://scrapy.org/).
 * [`ניקוי נתונים`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#clean-the-data) - מסביר כיצד ניתן לעצב, לנקות ולפשט טקסט באמצעות כלים בסיסיים כמו Visual Studio Code ו-Microsoft Excel.
 * [`ניתוח נתונים`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#working-with-the-data-in-a-notebook) - מסביר כיצד ניתן לייבא את מערך הנתונים ל"מחברות" לניתוח באמצעות חבילות Python (כמו pandas, numpy ו-matplotlib) כדי לארגן ולחזות את הנתונים.
 * [`ניתוח רגשות`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#sentiment-analysis-using-cognitive-services) - מסביר כיצד ניתן לשלב שירותי ענן כמו Text Analytics, באמצעות כלים עם קוד נמוך כמו [Power Automate](https://flow.microsoft.com/en-us/) עבור תהליכי עבודה אוטומטיים לעיבוד נתונים.

באמצעות תהליך זה, נוכל לחקור את ההשפעות העונתיות על הרגש של השירים, ולעזור לנו לעצב פרספקטיבות משלנו על המחברת. נסו זאת בעצמכם - ואז הרחיבו את המחברת כדי לשאול שאלות נוספות או להציג את הנתונים בדרכים חדשות!

> תוכלו להשתמש בכמה מהכלים ב[ערכת הכלים של מדעי הרוח הדיגיטליים](https://github.com/Digital-Humanities-Toolkit) כדי להמשיך לחקור תחום זה.

## מדע הנתונים + קיימות

| ![ סקיצה מאת [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Sustainability.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              מדע הנתונים וקיימות - _סקיצה מאת [@nitya](https://twitter.com/nitya)_              |

[אג'נדה 2030 לפיתוח בר קיימא](https://sdgs.un.org/2030agenda) - שאומצה על ידי כל חברי האומות המאוחדות בשנת 2015 - מזהה 17 יעדים כולל כאלה שמתמקדים ב**הגנה על כדור הארץ** מפני התדרדרות והשפעת שינויי האקלים. יוזמת [Microsoft Sustainability](https://www.microsoft.com/en-us/sustainability) תומכת ביעדים אלה על ידי חקר דרכים שבהן פתרונות טכנולוגיים יכולים לתמוך ולבנות עתיד בר קיימא יותר עם [מיקוד ב-4 יעדים](https://dev.to/azure/a-visual-guide-to-sustainable-software-engineering-53hh) - להיות שליליים בפחמן, חיוביים במים, אפס פסולת, וביודיוורסיים עד 2030.

התמודדות עם אתגרים אלה בצורה רחבת היקף ובזמן דורשת חשיבה בקנה מידה ענני - ונתונים רחבי היקף. יוזמת [Planetary Computer](https://planetarycomputer.microsoft.com/) מספקת 4 רכיבים כדי לעזור למדעני נתונים ולמפתחים במאמץ זה:

 * [קטלוג נתונים](https://planetarycomputer.microsoft.com/catalog) - עם פטה-בייטים של נתוני מערכות כדור הארץ (חינם ומאוחסן ב-Azure).
 * [Planetary API](https://planetarycomputer.microsoft.com/docs/reference/stac/) - כדי לעזור למשתמשים לחפש נתונים רלוונטיים במרחב ובזמן.
 * [Hub](https://planetarycomputer.microsoft.com/docs/overview/environment/) - סביבה מנוהלת למדענים לעיבוד מערכי נתונים גיאו-מרחביים עצומים.
 * [יישומים](https://planetarycomputer.microsoft.com/applications) - מציגים מקרי שימוש וכלים לתובנות קיימות.
**פרויקט המחשב הפלנטרי נמצא כרגע בתצוגה מקדימה (נכון לספטמבר 2021)** - כך תוכלו להתחיל לתרום לפתרונות קיימות באמצעות מדע הנתונים.

* [בקשו גישה](https://planetarycomputer.microsoft.com/account/request) כדי להתחיל לחקור ולהתחבר לעמיתים.
* [חקור את התיעוד](https://planetarycomputer.microsoft.com/docs/overview/about) כדי להבין אילו מערכי נתונים ו-APIs נתמכים.
* חקור יישומים כמו [מעקב אחר מערכות אקולוגיות](https://analytics-lab.org/ecosystemmonitoring/) לקבלת השראה לרעיונות ליישומים.

חשבו כיצד תוכלו להשתמש בהדמיית נתונים כדי לחשוף או להעצים תובנות רלוונטיות בתחומים כמו שינויי אקלים וכריתת יערות. או חשבו כיצד ניתן להשתמש בתובנות כדי ליצור חוויות משתמש חדשות שמניעות שינויים התנהגותיים לחיים ברי קיימא יותר.

## מדע הנתונים + סטודנטים

דיברנו על יישומים בעולם האמיתי בתעשייה ובמחקר, וחקרנו דוגמאות ליישומי מדע הנתונים במדעי הרוח הדיגיטליים ובקיימות. אז איך תוכלו לפתח את הכישורים שלכם ולשתף את המומחיות שלכם כמתחילים במדע הנתונים?

הנה כמה דוגמאות לפרויקטים של סטודנטים במדע הנתונים שיתנו לכם השראה.

* [בית הספר לקיץ במדע הנתונים של MSR](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/#!projects) עם [פרויקטים](https://github.com/msr-ds3) ב-GitHub שחוקרים נושאים כמו:
   - [הטיה גזעית בשימוש בכוח על ידי המשטרה](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2019-replicating-an-empirical-analysis-of-racial-differences-in-police-use-of-force/) | [Github](https://github.com/msr-ds3/stop-question-frisk)
   - [אמינות מערכת הרכבת התחתית של ניו יורק](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2018-exploring-the-reliability-of-the-nyc-subway-system/) | [Github](https://github.com/msr-ds3/nyctransit)
* [דיגיטציה של תרבות חומרית: חקר התפלגויות סוציו-אקונומיות בסירקאפ](https://claremont.maps.arcgis.com/apps/Cascade/index.html?appid=bdf2aef0f45a4674ba41cd373fa23afc) - מאת [אורנלה אלטוניאן](https://twitter.com/ornelladotcom) והצוות בקלרמונט, תוך שימוש ב-[ArcGIS StoryMaps](https://storymaps.arcgis.com/).

## 🚀 אתגר

חפשו מאמרים שממליצים על פרויקטים במדע הנתונים שמתאימים למתחילים - כמו [50 תחומי הנושא האלו](https://www.upgrad.com/blog/data-science-project-ideas-topics-beginners/) או [21 רעיונות לפרויקטים האלו](https://www.intellspot.com/data-science-project-ideas) או [16 הפרויקטים האלו עם קוד מקור](https://data-flair.training/blogs/data-science-project-ideas/) שתוכלו לפרק ולהרכיב מחדש. ואל תשכחו לכתוב בלוג על מסעות הלמידה שלכם ולשתף את התובנות שלכם איתנו.

## חידון לאחר ההרצאה

## [חידון לאחר ההרצאה](https://ff-quizzes.netlify.app/en/ds/quiz/39)

## סקירה ולמידה עצמית

רוצים לחקור עוד מקרי שימוש? הנה כמה מאמרים רלוונטיים:
* [17 יישומים ודוגמאות של מדע הנתונים](https://builtin.com/data-science/data-science-applications-examples) - יולי 2021
* [11 יישומים עוצרי נשימה של מדע הנתונים בעולם האמיתי](https://myblindbird.com/data-science-applications-real-world/) - מאי 2021
* [מדע הנתונים בעולם האמיתי](https://towardsdatascience.com/data-science-in-the-real-world/home) - אוסף מאמרים
* מדע הנתונים ב: [חינוך](https://data-flair.training/blogs/data-science-in-education/), [חקלאות](https://data-flair.training/blogs/data-science-in-agriculture/), [פיננסים](https://data-flair.training/blogs/data-science-in-finance/), [סרטים](https://data-flair.training/blogs/data-science-at-movies/) ועוד.

## משימה

[חקור מערך נתונים של המחשב הפלנטרי](assignment.md)

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית נחשב למקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי בני אדם. איננו נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.  