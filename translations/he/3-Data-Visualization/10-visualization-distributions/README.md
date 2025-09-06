<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a20467e046d312809d008395051fc7",
  "translation_date": "2025-09-05T23:23:22+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "he"
}
-->
# ויזואליזציה של התפלגויות

|![סקיצה מאת [(@sketchthedocs)](https://sketchthedocs.dev)](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| ויזואליזציה של התפלגויות - _סקיצה מאת [@nitya](https://twitter.com/nitya)_ |

בשיעור הקודם למדתם כמה עובדות מעניינות על מערך נתונים של ציפורים ממינסוטה. זיהיתם נתונים שגויים על ידי ויזואליזציה של ערכים חריגים ובחנתם את ההבדלים בין קטגוריות ציפורים לפי האורך המרבי שלהן.

## [שאלון לפני השיעור](https://ff-quizzes.netlify.app/en/ds/quiz/18)
## חקר מערך הנתונים של הציפורים

דרך נוספת לחקור נתונים היא על ידי בחינת ההתפלגות שלהם, כלומר איך הנתונים מאורגנים לאורך ציר. אולי, לדוגמה, תרצו ללמוד על ההתפלגות הכללית, עבור מערך הנתונים הזה, של מוטת הכנפיים המרבית או מסת הגוף המרבית של ציפורי מינסוטה.

בואו נגלה כמה עובדות על התפלגויות הנתונים במערך הנתונים הזה. בקובץ _notebook.ipynb_ שנמצא בתיקיית השיעור, ייבאו את Pandas, Matplotlib ואת הנתונים שלכם:

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | שם                          | שם מדעי                | קטגוריה               | סדר          | משפחה   | סוג         | סטטוס שימור         | אורך מינימלי | אורך מקסימלי | מסה מינימלית | מסה מקסימלית | מוטת כנפיים מינימלית | מוטת כנפיים מקסימלית |
| ---: | :-------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------:    | --------:    | ----------:  | ----------:  | ----------:          | ----------:          |
|    0 | ברווז שרוק שחור-בטן        | Dendrocygna autumnalis | ברווזים/אווזים/עופות מים | Anseriformes | Anatidae | Dendrocygna | LC                 |        47     |        56     |         652   |        1020   |          76          |          94          |
|    1 | ברווז שרוק חום              | Dendrocygna bicolor    | ברווזים/אווזים/עופות מים | Anseriformes | Anatidae | Dendrocygna | LC                 |        45     |        53     |         712   |        1050   |          85          |          93          |
|    2 | אווז השלג                   | Anser caerulescens     | ברווזים/אווזים/עופות מים | Anseriformes | Anatidae | Anser       | LC                 |        64     |        79     |        2050   |        4050   |         135          |         165          |
|    3 | אווז רוס                    | Anser rossii           | ברווזים/אווזים/עופות מים | Anseriformes | Anatidae | Anser       | LC                 |      57.3     |        64     |        1066   |        1567   |         113          |         116          |
|    4 | אווז לבן-מצח גדול           | Anser albifrons        | ברווזים/אווזים/עופות מים | Anseriformes | Anatidae | Anser       | LC                 |        64     |        81     |        1930   |        3310   |         130          |         165          |

באופן כללי, ניתן לבחון במהירות את אופן ההתפלגות של הנתונים באמצעות תרשים פיזור, כפי שעשינו בשיעור הקודם:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![אורך מקסימלי לפי סדר](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

זה נותן מבט כללי על ההתפלגות של אורך הגוף לפי סדר הציפורים, אך זו אינה הדרך האופטימלית להציג התפלגויות אמיתיות. משימה זו מתבצעת בדרך כלל על ידי יצירת היסטוגרמה.

## עבודה עם היסטוגרמות

Matplotlib מציעה דרכים מצוינות לויזואליזציה של התפלגות נתונים באמצעות היסטוגרמות. סוג תרשים זה דומה לתרשים עמודות שבו ההתפלגות נראית דרך עלייה וירידה של העמודות. כדי לבנות היסטוגרמה, יש צורך בנתונים מספריים. ניתן לבנות היסטוגרמה על ידי הגדרת סוג התרשים כ-'hist'. תרשים זה מציג את ההתפלגות של MaxBodyMass עבור כל טווח הנתונים המספריים במערך הנתונים. על ידי חלוקת מערך הנתונים למקטעים קטנים יותר, ניתן להציג את התפלגות הערכים:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![התפלגות על פני כל מערך הנתונים](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

כפי שניתן לראות, רוב 400+ הציפורים במערך הנתונים הזה נמצאות בטווח של מתחת ל-2000 עבור מסת הגוף המרבית שלהן. ניתן לקבל תובנות נוספות על ידי שינוי הפרמטר `bins` למספר גבוה יותר, כמו 30:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![התפלגות על פני כל מערך הנתונים עם פרמטר bins גדול יותר](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

תרשים זה מציג את ההתפלגות בצורה מעט יותר מפורטת. ניתן ליצור תרשים פחות מוטה שמאלה על ידי בחירת נתונים בטווח מסוים בלבד:

סננו את הנתונים כך שיכללו רק ציפורים שמסת הגוף שלהן מתחת ל-60, והציגו 40 `bins`:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![היסטוגרמה מסוננת](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ נסו מסננים ונקודות נתונים אחרות. כדי לראות את ההתפלגות המלאה של הנתונים, הסירו את המסנן `['MaxBodyMass']` כדי להציג התפלגויות עם תוויות.

ההיסטוגרמה מציעה גם שיפורים נחמדים בצבעים ובתוויות שכדאי לנסות.

צרו היסטוגרמה דו-ממדית כדי להשוות בין שתי התפלגויות. בואו נשווה בין `MaxBodyMass` ל-`MaxLength`. Matplotlib מציעה דרך מובנית להראות התכנסות באמצעות צבעים בהירים יותר:

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
נראה שיש מתאם צפוי בין שני האלמנטים הללו לאורך ציר צפוי, עם נקודת התכנסות חזקה במיוחד:

![תרשים דו-ממדי](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

היסטוגרמות עובדות היטב כברירת מחדל עבור נתונים מספריים. מה אם תרצו לראות התפלגויות לפי נתונים טקסטואליים?

## חקר מערך הנתונים להתפלגויות לפי נתונים טקסטואליים

מערך הנתונים הזה כולל גם מידע טוב על קטגוריית הציפורים, סוגן, מינן ומשפחתן, כמו גם על סטטוס השימור שלהן. בואו נחקור את המידע על סטטוס השימור. מהי ההתפלגות של הציפורים לפי סטטוס השימור שלהן?

> ✅ במערך הנתונים, נעשה שימוש בכמה ראשי תיבות לתיאור סטטוס השימור. ראשי תיבות אלו מגיעים מ-[קטגוריות הרשימה האדומה של IUCN](https://www.iucnredlist.org/), ארגון שמקטלג את הסטטוס של מינים.
> 
> - CR: בסכנת הכחדה חמורה
> - EN: בסכנת הכחדה
> - EX: נכחד
> - LC: ללא חשש
> - NT: קרוב לסיכון
> - VU: פגיע

אלו ערכים מבוססי טקסט ולכן תצטרכו לבצע המרה כדי ליצור היסטוגרמה. השתמשו ב-DataFrame המסונן של הציפורים, והציגו את סטטוס השימור שלהן לצד מוטת הכנפיים המינימלית שלהן. מה אתם רואים?

```python
x1 = filteredBirds.loc[filteredBirds.ConservationStatus=='EX', 'MinWingspan']
x2 = filteredBirds.loc[filteredBirds.ConservationStatus=='CR', 'MinWingspan']
x3 = filteredBirds.loc[filteredBirds.ConservationStatus=='EN', 'MinWingspan']
x4 = filteredBirds.loc[filteredBirds.ConservationStatus=='NT', 'MinWingspan']
x5 = filteredBirds.loc[filteredBirds.ConservationStatus=='VU', 'MinWingspan']
x6 = filteredBirds.loc[filteredBirds.ConservationStatus=='LC', 'MinWingspan']

kwargs = dict(alpha=0.5, bins=20)

plt.hist(x1, **kwargs, color='red', label='Extinct')
plt.hist(x2, **kwargs, color='orange', label='Critically Endangered')
plt.hist(x3, **kwargs, color='yellow', label='Endangered')
plt.hist(x4, **kwargs, color='green', label='Near Threatened')
plt.hist(x5, **kwargs, color='blue', label='Vulnerable')
plt.hist(x6, **kwargs, color='gray', label='Least Concern')

plt.gca().set(title='Conservation Status', ylabel='Min Wingspan')
plt.legend();
```

![מוטת כנפיים וסטטוס שימור](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

נראה שאין מתאם טוב בין מוטת הכנפיים המינימלית לסטטוס השימור. בדקו אלמנטים אחרים במערך הנתונים באמצעות שיטה זו. תוכלו לנסות מסננים שונים גם כן. האם אתם מוצאים מתאם כלשהו?

## תרשימי צפיפות

ייתכן ששמתם לב שההיסטוגרמות שראינו עד כה הן 'מדורגות' ואינן זורמות בצורה חלקה בקשת. כדי להציג תרשים צפיפות חלק יותר, תוכלו לנסות תרשים צפיפות.

כדי לעבוד עם תרשימי צפיפות, הכירו ספריית תרשימים חדשה, [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html).

טענו את Seaborn ונסו תרשים צפיפות בסיסי:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![תרשים צפיפות](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

ניתן לראות כיצד התרשים משקף את הקודם עבור נתוני מוטת הכנפיים המינימלית; הוא פשוט חלק יותר. לפי התיעוד של Seaborn, "בהשוואה להיסטוגרמה, KDE יכול להפיק תרשים שהוא פחות עמוס ויותר ניתן לפרשנות, במיוחד כאשר מציירים התפלגויות מרובות. אך יש לו פוטנציאל להכניס עיוותים אם ההתפלגות הבסיסית מוגבלת או לא חלקה. כמו בהיסטוגרמה, איכות הייצוג תלויה גם בבחירת פרמטרי החלקה טובים." [מקור](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) במילים אחרות, ערכים חריגים, כמו תמיד, יגרמו לתרשימים שלכם להתנהג בצורה לא צפויה.

אם תרצו לחזור לקו המשונן של MaxBodyMass בתרשים השני שבניתם, תוכלו להחליק אותו היטב על ידי יצירתו מחדש בשיטה זו:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![קו מסת גוף חלק](../../../../3-Data-Visualization/10-visualization-distributions/images/density2.png)

אם תרצו קו חלק, אך לא חלק מדי, ערכו את הפרמטר `bw_adjust`:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![קו מסת גוף פחות חלק](../../../../3-Data-Visualization/10-visualization-distributions/images/density3.png)

✅ קראו על הפרמטרים הזמינים עבור סוג תרשים זה ונסו אותם!

סוג תרשים זה מציע ויזואליזציות מסבירות בצורה יפהפייה. עם כמה שורות קוד, לדוגמה, תוכלו להציג את צפיפות מסת הגוף המרבית לפי סדר הציפורים:

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![מסת גוף לפי סדר](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

תוכלו גם למפות את הצפיפות של כמה משתנים בתרשים אחד. בדקו את האורך המרבי והמינימלי של ציפור בהשוואה לסטטוס השימור שלה:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![צפיפויות מרובות, חופפות](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

אולי כדאי לחקור האם האשכול של ציפורים 'פגיעות' לפי אורכן הוא משמעותי או לא.

## 🚀 אתגר

היסטוגרמות הן סוג תרשים מתוחכם יותר מאשר תרשימי פיזור, עמודות או קווים בסיסיים. חפשו באינטרנט דוגמאות טובות לשימוש בהיסטוגרמות. כיצד הן משמשות, מה הן מדגימות, ובאילו תחומים או תחומי מחקר הן נוטות להיות בשימוש?

## [שאלון לאחר השיעור](https://ff-quizzes.netlify.app/en/ds/quiz/19)

## סקירה ולימוד עצמי

בשיעור זה השתמשתם ב-Matplotlib והתחלתם לעבוד עם Seaborn כדי להציג תרשימים מתוחכמים יותר. בצעו מחקר על `kdeplot` ב-Seaborn, "עקומת צפיפות הסתברות רציפה בממד אחד או יותר". קראו את [התיעוד](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) כדי להבין כיצד הוא עובד.

## משימה

[יישמו את הכישורים שלכם](assignment.md)

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית נחשב למקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. איננו נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.