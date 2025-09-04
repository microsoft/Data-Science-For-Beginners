<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "02ce904bc1e2bfabb7dc05c25aae375c",
  "translation_date": "2025-09-04T20:11:41+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "he"
}
-->
# הצגת התפלגויות

|![סקיצה מאת [(@sketchthedocs)](https://sketchthedocs.dev)](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| הצגת התפלגויות - _סקיצה מאת [@nitya](https://twitter.com/nitya)_ |

בשיעור הקודם למדתם כמה עובדות מעניינות על מערך נתונים של ציפורים ממינסוטה. זיהיתם נתונים שגויים על ידי הצגת ערכים חריגים ובחנתם את ההבדלים בין קטגוריות של ציפורים לפי האורך המרבי שלהן.

## [שאלון לפני השיעור](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## חקר מערך הנתונים של הציפורים

דרך נוספת לחקור נתונים היא לבחון את ההתפלגות שלהם, כלומר איך הנתונים מאורגנים לאורך ציר. ייתכן, למשל, שתרצו ללמוד על ההתפלגות הכללית של מוטת הכנפיים המרבית או המסה המרבית של הציפורים במינסוטה.

בואו נגלה כמה עובדות על התפלגויות הנתונים במערך הנתונים הזה. בקובץ _notebook.ipynb_ שנמצא בתיקיית השיעור, ייבאו את Pandas, Matplotlib ואת הנתונים שלכם:

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | שם                          | שם מדעי                | קטגוריה               | סדר          | משפחה   | סוג         | מצב שימור          | אורך מינימלי | אורך מרבי | מסה מינימלית | מסה מרבית | מוטת כנפיים מינימלית | מוטת כנפיים מרבית |
| ---: | :-------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | ברווז שורק שחור-בטן        | Dendrocygna autumnalis | ברווזים/אווזים/עופות מים | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | ברווז שורק חום              | Dendrocygna bicolor    | ברווזים/אווזים/עופות מים | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | אווז שלג                    | Anser caerulescens     | ברווזים/אווזים/עופות מים | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | אווז רוס                   | Anser rossii           | ברווזים/אווזים/עופות מים | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | אווז לבן-מצח גדול           | Anser albifrons        | ברווזים/אווזים/עופות מים | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

באופן כללי, ניתן לבחון במהירות את אופן התפלגות הנתונים באמצעות תרשים פיזור כפי שעשינו בשיעור הקודם:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![אורך מרבי לפי סדר](../../../../translated_images/scatter-wb.9d98b0ed7f0388af979441853361a11df5f518f5307938a503ca7913e986111b.he.png)

תרשים זה מספק מבט כללי על התפלגות האורך המרבי של הגוף לפי סדר הציפורים, אך הוא אינו הדרך האופטימלית להציג התפלגויות אמיתיות. משימה זו מתבצעת בדרך כלל באמצעות יצירת היסטוגרמה.

## עבודה עם היסטוגרמות

Matplotlib מציעה דרכים מצוינות להציג התפלגות נתונים באמצעות היסטוגרמות. סוג תרשים זה דומה לתרשים עמודות שבו ניתן לראות את ההתפלגות דרך עלייה וירידה של העמודות. כדי לבנות היסטוגרמה, יש צורך בנתונים מספריים. ניתן ליצור היסטוגרמה על ידי הגדרת סוג התרשים כ-'hist'. תרשים זה מציג את התפלגות המסה המרבית של כל מערך הנתונים. על ידי חלוקת מערך הנתונים לתאים קטנים יותר, ניתן להציג את התפלגות הערכים:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![התפלגות על פני כל מערך הנתונים](../../../../translated_images/dist1-wb.0d0cac82e2974fbbec635826fefead401af795f82e2279e2e2678bf2c117d827.he.png)

כפי שניתן לראות, רוב 400+ הציפורים במערך הנתונים הזה נופלות בטווח של פחות מ-2000 עבור המסה המרבית שלהן. ניתן לקבל תובנות נוספות על ידי שינוי הפרמטר `bins` למספר גבוה יותר, כמו 30:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![התפלגות על פני כל מערך הנתונים עם פרמטר תאים גדול יותר](../../../../translated_images/dist2-wb.2c0a7a3499b2fbf561e9f93b69f265dfc538dc78f6de15088ba84a88152e26ba.he.png)

תרשים זה מציג את ההתפלגות בצורה מעט יותר מפורטת. ניתן ליצור תרשים פחות מוטה שמאלה על ידי בחירת נתונים בטווח מסוים בלבד:

סננו את הנתונים כך שיכללו רק ציפורים שמסת גופן פחותה מ-60, והציגו 40 `bins`:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![היסטוגרמה מסוננת](../../../../translated_images/dist3-wb.64b88db7f9780200bd486a2c2a3252548dd439672dbd3f778193db7f654b100c.he.png)

✅ נסו מסננים ונקודות נתונים אחרות. כדי לראות את ההתפלגות המלאה של הנתונים, הסירו את המסנן `['MaxBodyMass']` כדי להציג התפלגויות מתויגות.

ההיסטוגרמה מציעה גם שיפורים בצבעים ובתיוג שכדאי לנסות:

צרו היסטוגרמה דו-ממדית כדי להשוות בין שתי התפלגויות. בואו נשווה בין `MaxBodyMass` ל-`MaxLength`. Matplotlib מציעה דרך מובנית להציג התכנסות באמצעות צבעים בהירים יותר:

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
נראה שיש מתאם צפוי בין שני האלמנטים הללו לאורך ציר צפוי, עם נקודת התכנסות חזקה במיוחד:

![תרשים דו-ממדי](../../../../translated_images/2D-wb.ae22fdd33936507a41e3af22e11e4903b04a9be973b23a4e05214efaccfd66c8.he.png)

היסטוגרמות עובדות היטב כברירת מחדל עבור נתונים מספריים. מה אם תרצו לראות התפלגויות לפי נתונים טקסטואליים? 
## חקר מערך הנתונים להתפלגויות לפי נתונים טקסטואליים 

מערך הנתונים הזה כולל גם מידע טוב על קטגוריית הציפורים, סוגן, מינן ומשפחתן, כמו גם על מצב השימור שלהן. בואו נעמיק במידע על מצב השימור. מהי התפלגות הציפורים לפי מצב השימור שלהן?

> ✅ במערך הנתונים נעשה שימוש בכמה ראשי תיבות לתיאור מצב השימור. ראשי תיבות אלו מגיעים מ-[קטגוריות הרשימה האדומה של IUCN](https://www.iucnredlist.org/), ארגון שמקטלג את מצבם של מינים.
> 
> - CR: בסכנת הכחדה חמורה
> - EN: בסכנת הכחדה
> - EX: נכחד
> - LC: ללא חשש
> - NT: קרוב לאיום
> - VU: פגיע

אלו ערכים מבוססי טקסט ולכן תצטרכו לבצע המרה כדי ליצור היסטוגרמה. השתמשו ב-DataFrame המסונן של הציפורים והציגו את מצב השימור לצד מוטת הכנפיים המינימלית שלהן. מה אתם רואים?

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

![קולאז' מוטת כנפיים ומצב שימור](../../../../translated_images/histogram-conservation-wb.3c40450eb072c14de7a1a3ec5c0fcba4995531024760741b392911b567fd8b70.he.png)

לא נראה שיש מתאם טוב בין מוטת הכנפיים המינימלית למצב השימור. בדקו אלמנטים אחרים במערך הנתונים באמצעות שיטה זו. תוכלו לנסות מסננים שונים גם כן. האם אתם מוצאים מתאם כלשהו?

## תרשימי צפיפות

ייתכן ששמתם לב שההיסטוגרמות שראינו עד כה הן 'מדורגות' ואינן זורמות בצורה חלקה בקשת. כדי להציג תרשים צפיפות חלק יותר, תוכלו לנסות תרשים צפיפות.

כדי לעבוד עם תרשימי צפיפות, הכירו ספריית תרשימים חדשה, [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html). 

לאחר טעינת Seaborn, נסו תרשים צפיפות בסיסי:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![תרשים צפיפות](../../../../translated_images/density1.8801043bd4af2567b0f706332b5853c7614e5e4b81b457acc27eb4e092a65cbd.he.png)

ניתן לראות כיצד התרשים מהדהד את הקודם עבור נתוני מוטת הכנפיים המינימלית; הוא פשוט מעט חלק יותר. לפי התיעוד של Seaborn, "בהשוואה להיסטוגרמה, KDE יכול להפיק תרשים פחות עמוס ויותר ניתן לפרשנות, במיוחד כאשר מציגים התפלגויות מרובות. אך יש לו פוטנציאל להכניס עיוותים אם ההתפלגות הבסיסית מוגבלת או לא חלקה. כמו בהיסטוגרמה, איכות הייצוג תלויה גם בבחירת פרמטרי החלקה טובים." [מקור](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) במילים אחרות, ערכים חריגים, כמו תמיד, יגרמו לתרשימים שלכם להתנהג בצורה לא צפויה.

אם תרצו לחזור לקו המחוספס של MaxBodyMass בתרשים השני שיצרתם, תוכלו להחליק אותו היטב על ידי יצירתו מחדש בשיטה זו:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![קו מסה חלק](../../../../translated_images/density2.8e7647257060ff544a1aaded57e8dd1887586bfe340139e9b77ac1e5287f7977.he.png)

אם תרצו קו חלק, אך לא חלק מדי, ערכו את הפרמטר `bw_adjust`: 

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![קו מסה פחות חלק](../../../../translated_images/density3.84ae27da82f31e6b83ad977646f029a1d21186574d7581facd70123b3eb257ee.he.png)

✅ קראו על הפרמטרים הזמינים עבור סוג תרשים זה ונסו להתנסות!

סוג תרשים זה מציע ויזואליזציות מסבירות בצורה יפהפייה. עם כמה שורות קוד, למשל, תוכלו להציג את צפיפות המסה המרבית לפי סדר הציפורים:

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![מסה לפי סדר](../../../../translated_images/density4.e9d6c033f15c500fd33df94cb592b9f5cf1ed2a3d213c448a3f9e97ba39573ce.he.png)

תוכלו גם למפות את הצפיפות של כמה משתנים בתרשים אחד. בדקו את האורך המרבי והמינימלי של ציפור בהשוואה למצב השימור שלה:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![צפיפויות מרובות, חופפות](../../../../translated_images/multi.56548caa9eae8d0fd9012a8586295538c7f4f426e2abc714ba070e2e4b1fc2c1.he.png)

אולי כדאי לחקור האם הצבר של ציפורים 'פגיעות' לפי אורכן הוא משמעותי או לא.

## 🚀 אתגר

היסטוגרמות הן סוג תרשים מתוחכם יותר מאשר תרשימי פיזור, עמודות או קווים בסיסיים. חפשו באינטרנט דוגמאות טובות לשימוש בהיסטוגרמות. כיצד הן משמשות, מה הן מדגימות, ובאילו תחומים או תחומי מחקר הן נוטות לשמש?

## [שאלון לאחר השיעור](https://ff-quizzes.netlify.app/en/ds/)

## סקירה ולמידה עצמית

בשיעור זה השתמשתם ב-Matplotlib והתחלתם לעבוד עם Seaborn כדי להציג תרשימים מתוחכמים יותר. בצעו מחקר על `kdeplot` ב-Seaborn, "עקומת צפיפות הסתברות רציפה בממד אחד או יותר". קראו את [התיעוד](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) כדי להבין כיצד הוא עובד.

## משימה

[יישמו את הכישורים שלכם](assignment.md)

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.