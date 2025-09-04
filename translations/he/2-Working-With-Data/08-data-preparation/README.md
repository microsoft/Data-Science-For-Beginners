<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90a815d332aea41a222f4c6372e7186e",
  "translation_date": "2025-09-04T20:04:58+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "he"
}
-->
# עבודה עם נתונים: הכנת נתונים

|![ סקיצה מאת [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|הכנת נתונים - _סקיצה מאת [@nitya](https://twitter.com/nitya)_ |

## [שאלון לפני השיעור](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

בהתאם למקורו, נתונים גולמיים עשויים להכיל אי-סדירויות שיגרמו לאתגרים בניתוח ובמודלים. במילים אחרות, נתונים אלו יכולים להיות מסווגים כ"מלוכלכים" ויהיה צורך לנקותם. שיעור זה מתמקד בטכניקות לניקוי והמרת נתונים כדי להתמודד עם אתגרים של נתונים חסרים, לא מדויקים או לא שלמים. הנושאים הנלמדים בשיעור זה יעשו שימוש ב-Python ובספריית Pandas ויודגמו [במחברת](notebook.ipynb) בתוך תיקייה זו.

## החשיבות של ניקוי נתונים

- **קלות שימוש ושימוש חוזר**: כאשר נתונים מאורגנים ומנורמלים כראוי, קל יותר לחפש, להשתמש ולשתף אותם עם אחרים.

- **עקביות**: מדע הנתונים לעיתים קרובות דורש עבודה עם יותר ממערך נתונים אחד, כאשר מערכי נתונים ממקורות שונים צריכים להיות משולבים יחד. הבטחת סטנדרטיזציה משותפת לכל מערך נתונים תבטיח שהנתונים יהיו שימושיים גם כאשר הם משולבים למערך נתונים אחד.

- **דיוק המודל**: נתונים שנוקו משפרים את דיוק המודלים שמסתמכים עליהם.

## מטרות וטקטיקות נפוצות לניקוי נתונים

- **חקירת מערך נתונים**: חקירת נתונים, אשר נלמדת [בשיעור מאוחר יותר](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), יכולה לעזור לך לזהות נתונים שזקוקים לניקוי. התבוננות חזותית בערכים בתוך מערך נתונים יכולה להגדיר ציפיות לגבי איך שאר הנתונים ייראו, או לספק רעיון לגבי בעיות שניתן לפתור. חקירה יכולה לכלול שאילתות בסיסיות, ויזואליזציות ודגימות.

- **עיצוב**: בהתאם למקור, נתונים יכולים להכיל אי-סדירויות באופן שבו הם מוצגים. זה יכול לגרום לבעיות בחיפוש ובייצוג הערך, כאשר הוא נראה בתוך מערך הנתונים אך אינו מיוצג כראוי בוויזואליזציות או בתוצאות שאילתה. בעיות עיצוב נפוצות כוללות פתרון רווחים, תאריכים וסוגי נתונים. פתרון בעיות עיצוב הוא בדרך כלל באחריות האנשים שמשתמשים בנתונים. לדוגמה, סטנדרטים לגבי איך תאריכים ומספרים מוצגים יכולים להשתנות ממדינה למדינה.

- **כפילויות**: נתונים שמופיעים יותר מפעם אחת יכולים להפיק תוצאות לא מדויקות ובדרך כלל יש להסירם. זה יכול להיות נפוץ כאשר משלבים שני מערכי נתונים או יותר יחד. עם זאת, ישנם מקרים שבהם כפילויות במערכי נתונים משולבים מכילות חלקים שיכולים לספק מידע נוסף וייתכן שיהיה צורך לשמרם.

- **נתונים חסרים**: נתונים חסרים יכולים לגרום לתוצאות לא מדויקות כמו גם לתוצאות חלשות או מוטות. לפעמים ניתן לפתור זאת על ידי "טעינה מחדש" של הנתונים, מילוי הערכים החסרים באמצעות חישוב וקוד כמו Python, או פשוט הסרת הערך והנתונים המתאימים. ישנן סיבות רבות לכך שנתונים עשויים להיות חסרים והפעולות שננקטות כדי לפתור ערכים חסרים אלו יכולות להיות תלויות באיך ולמה הם נעלמו מלכתחילה.

## חקירת מידע על DataFrame
> **מטרת הלמידה:** בסיום תת-הסעיף הזה, תרגישו בנוח למצוא מידע כללי על הנתונים המאוחסנים ב-DataFrames של pandas.

לאחר טעינת הנתונים ל-pandas, סביר להניח שהם יהיו ב-DataFrame (עיינו [בשיעור הקודם](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) לסקירה מפורטת). עם זאת, אם מערך הנתונים ב-DataFrame שלכם מכיל 60,000 שורות ו-400 עמודות, איך בכלל מתחילים להבין עם מה אתם עובדים? למרבה המזל, [pandas](https://pandas.pydata.org/) מספקת כלים נוחים להצצה מהירה על מידע כללי על DataFrame בנוסף לשורות הראשונות והאחרונות.

כדי לחקור את הפונקציונליות הזו, נייבא את ספריית scikit-learn של Python ונשתמש במערך נתונים איקוני: **מערך הנתונים של Iris**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |sepal length (cm)|sepal width (cm)|petal length (cm)|petal width (cm)|
|----------------------------------------|-----------------|----------------|-----------------|----------------|
|0                                       |5.1              |3.5             |1.4              |0.2             |
|1                                       |4.9              |3.0             |1.4              |0.2             |
|2                                       |4.7              |3.2             |1.3              |0.2             |
|3                                       |4.6              |3.1             |1.5              |0.2             |
|4                                       |5.0              |3.6             |1.4              |0.2             |

- **DataFrame.info**: כדי להתחיל, משתמשים בשיטת `info()` להדפסת סיכום של התוכן הקיים ב-`DataFrame`. בואו נסתכל על מערך הנתונים הזה כדי לראות מה יש לנו:
```python
iris_df.info()
```
```
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
dtypes: float64(4)
memory usage: 4.8 KB
```
מכך, אנו יודעים שמערך הנתונים *Iris* מכיל 150 רשומות בארבע עמודות ללא ערכים ריקים. כל הנתונים מאוחסנים כמספרים בנקודה צפה של 64 ביט.

- **DataFrame.head()**: לאחר מכן, כדי לבדוק את התוכן בפועל של ה-`DataFrame`, אנו משתמשים בשיטת `head()`. בואו נראה איך נראות השורות הראשונות של `iris_df` שלנו:
```python
iris_df.head()
```
```
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
```
- **DataFrame.tail()**: לעומת זאת, כדי לבדוק את השורות האחרונות של ה-`DataFrame`, אנו משתמשים בשיטת `tail()`:
```python
iris_df.tail()
```
```
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
145                6.7               3.0                5.2               2.3
146                6.3               2.5                5.0               1.9
147                6.5               3.0                5.2               2.0
148                6.2               3.4                5.4               2.3
149                5.9               3.0                5.1               1.8
```
> **מסקנה:** אפילו רק על ידי התבוננות במטא-נתונים על המידע ב-DataFrame או בערכים הראשונים והאחרונים בו, ניתן לקבל מושג מיידי על הגודל, הצורה והתוכן של הנתונים שאתם מתמודדים איתם.

## התמודדות עם נתונים חסרים
> **מטרת הלמידה:** בסיום תת-הסעיף הזה, תדעו כיצד להחליף או להסיר ערכים ריקים מ-DataFrames.

ברוב המקרים מערכי הנתונים שתרצו להשתמש בהם (או שתצטרכו להשתמש בהם) מכילים ערכים חסרים. האופן שבו מתמודדים עם נתונים חסרים נושא עמו פשרות עדינות שיכולות להשפיע על הניתוח הסופי ועל תוצאות בעולם האמיתי.

Pandas מתמודדת עם ערכים חסרים בשתי דרכים. הראשונה שראיתם קודם לכן בסעיפים קודמים: `NaN`, או Not a Number. זהו למעשה ערך מיוחד שהוא חלק ממפרט הנקודה הצפה של IEEE והוא משמש רק לציון ערכים חסרים בנקודה צפה.

לערכים חסרים שאינם נקודות צפות, pandas משתמשת באובייקט `None` של Python. למרות שזה עשוי להיראות מבלבל שתיתקלו בשני סוגים שונים של ערכים שאומרים למעשה את אותו הדבר, יש לכך סיבות תכנותיות טובות ובפועל, גישה זו מאפשרת ל-pandas לספק פשרה טובה עבור רוב המקרים. עם זאת, גם `None` וגם `NaN` נושאים מגבלות שצריך להיות מודעים אליהן לגבי איך ניתן להשתמש בהם.

למידע נוסף על `NaN` ו-`None`, עיינו ב-[מחברת](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **זיהוי ערכים ריקים**: ב-`pandas`, השיטות `isnull()` ו-`notnull()` הן השיטות העיקריות שלכם לזיהוי נתונים ריקים. שתיהן מחזירות מסכות בוליאניות על הנתונים שלכם. נשתמש ב-`numpy` עבור ערכי `NaN`:
```python
import numpy as np

example1 = pd.Series([0, np.nan, '', None])
example1.isnull()
```
```
0    False
1     True
2    False
3     True
dtype: bool
```
התבוננו היטב בתוצאה. האם משהו מפתיע אתכם? בעוד ש-`0` הוא ערך אריתמטי ריק, הוא בכל זאת מספר שלם תקין ו-pandas מתייחסת אליו ככזה. `''` הוא קצת יותר עדין. בעוד שהשתמשנו בו בסעיף 1 כדי לייצג ערך מחרוזת ריק, הוא בכל זאת אובייקט מחרוזת ולא ייצוג של ריק מבחינת pandas.

עכשיו, בואו נהפוך את זה ונשתמש בשיטות אלו בצורה דומה יותר לאופן שבו תשתמשו בהן בפועל. ניתן להשתמש במסכות בוליאניות ישירות כ-``Series`` או ``DataFrame`` אינדקס, מה שיכול להיות שימושי כאשר מנסים לעבוד עם ערכים ריקים (או קיימים) מבודדים.

> **מסקנה**: גם השיטות `isnull()` וגם `notnull()` מפיקות תוצאות דומות כאשר משתמשים בהן ב-`DataFrame`s: הן מציגות את התוצאות ואת האינדקס של אותן תוצאות, מה שיעזור לכם מאוד כאשר תתמודדו עם הנתונים שלכם.

- **הסרת ערכים ריקים**: מעבר לזיהוי ערכים חסרים, pandas מספקת דרך נוחה להסרת ערכים ריקים מ-`Series` ו-`DataFrame`s. (במיוחד במערכי נתונים גדולים, לעיתים קרובות מומלץ יותר פשוט להסיר ערכים חסרים [NA] מהניתוח שלכם מאשר להתמודד איתם בדרכים אחרות.) כדי לראות זאת בפעולה, נחזור ל-`example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
שימו לב שזה אמור להיראות כמו התוצאה שלכם מ-`example3[example3.notnull()]`. ההבדל כאן הוא שבמקום רק לאנדקס על הערכים המוסתרים, `dropna` הסירה את הערכים החסרים מ-`Series` `example1`.

מכיוון של-`DataFrame`s יש שתי ממדים, הם מציעים יותר אפשרויות להסרת נתונים.

```python
example2 = pd.DataFrame([[1,      np.nan, 7], 
                         [2,      5,      8], 
                         [np.nan, 6,      9]])
example2
```
|      | 0 | 1 | 2 |
|------|---|---|---|
|0     |1.0|NaN|7  |
|1     |2.0|5.0|8  |
|2     |NaN|6.0|9  |

(שמתם לב ש-pandas שדרגה שתי עמודות לנקודות צפות כדי להתאים ל-`NaN`s?)

לא ניתן להסיר ערך יחיד מ-`DataFrame`, ולכן יש להסיר שורות או עמודות שלמות. תלוי במה שאתם עושים, ייתכן שתרצו לעשות אחד או השני, ולכן pandas נותנת לכם אפשרויות לשניהם. מכיוון שבמדע הנתונים, עמודות בדרך כלל מייצגות משתנים ושורות מייצגות תצפיות, סביר יותר שתסירו שורות של נתונים; ההגדרה המחדלית של `dropna()` היא להסיר את כל השורות שמכילות ערכים ריקים כלשהם:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
אם יש צורך, ניתן להסיר ערכי NA מעמודות. השתמשו ב-`axis=1` כדי לעשות זאת:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
שימו לב שזה יכול להסיר הרבה נתונים שייתכן שתרצו לשמור, במיוחד במערכי נתונים קטנים יותר. מה אם אתם רוצים להסיר רק שורות או עמודות שמכילות כמה או אפילו את כל הערכים הריקים? ניתן להגדיר את ההגדרות הללו ב-`dropna` עם הפרמטרים `how` ו-`thresh`.

במחדל, `how='any'` (אם תרצו לבדוק בעצמכם או לראות אילו פרמטרים נוספים יש לשיטה, הריצו `example4.dropna?` בתא קוד). ניתן גם להגדיר `how='all'` כדי להסיר רק שורות או עמודות שמכילות את כל הערכים הריקים. בואו נרחיב את דוגמת ה-`DataFrame` שלנו כדי לראות זאת בפעולה.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

הפרמטר `thresh` נותן לכם שליטה מדויקת יותר: אתם מגדירים את מספר הערכים *שאינם ריקים* ששורה או עמודה צריכה להכיל כדי להישמר:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
כאן, השורה הראשונה והאחרונה הוסרו, מכיוון שהן מכילות רק שני ערכים שאינם ריקים.

- **מילוי ערכים ריקים**: בהתאם למערך הנתונים שלכם, לפעמים הגיוני יותר למלא ערכים ריקים בערכים תקפים מאשר להסירם. ניתן להשתמש ב-`isnull` כדי לעשות זאת במקום, אך זה יכול להיות מייגע, במיוחד אם יש לכם הרבה ערכים למלא. מכיוון שזו משימה נפוצה במדע הנתונים, pandas מספקת את `fillna`, שמחזירה עותק של ה-`Series` או ה-`DataFrame` עם הערכים החסרים מוחלפים באחד שתבחרו. בואו ניצור דוגמת `Series` נוספת כדי לראות איך זה עובד בפועל.
```python
example3 = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
example3
```
```
a    1.0
b    NaN
c    2.0
d    NaN
e    3.0
dtype: float64
```
ניתן למלא את כל הערכים הריקים בערך יחיד, כמו `0`:
```python
example3.fillna(0)
```
```
a    1.0
b    0.0
c    2.0
d    0.0
e    3.0
dtype: float64
```
ניתן **למלא קדימה** ערכים ריקים, כלומר להשתמש בערך התקף האחרון כדי למלא ערך ריק:
```python
example3.fillna(method='ffill')
```
```
a    1.0
b    1.0
c    2.0
d    2.0
e    3.0
dtype: float64
```
ניתן גם **למלא אחורה** כדי להפיץ את הערך התקף הבא אחורה כדי למלא ערך ריק:
```python
example3.fillna(method='bfill')
```
```
a    1.0
b    2.0
c    2.0
d    3.0
e    3.0
dtype: float64
```
כפי שניתן לנחש, זה עובד באותו אופן עם `DataFrame`s, אך ניתן גם להגדיר `axis` לאורך המילוי של ערכים ריקים. תוך שימוש שוב ב-`example2`:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
שימו לב שכאשר ערך קודם אינו זמין למילוי קדימה, הערך הריק נשאר.
> **עיקרון חשוב:** ישנן דרכים רבות להתמודד עם ערכים חסרים במערכי הנתונים שלך. האסטרטגיה הספציפית שבה תשתמש (הסרתם, החלפתם, או אפילו איך להחליף אותם) צריכה להיות מותאמת למאפיינים של הנתונים הללו. ככל שתתעסק ותעבוד יותר עם מערכי נתונים, תפתח תחושה טובה יותר כיצד להתמודד עם ערכים חסרים.

## הסרת נתונים כפולים

> **מטרת הלמידה:** בסיום תת-הפרק הזה, תרגיש בנוח לזהות ולהסיר ערכים כפולים מ-DataFrames.

בנוסף לערכים חסרים, לעיתים קרובות תיתקל בנתונים כפולים במערכי נתונים בעולם האמיתי. למרבה המזל, `pandas` מספקת דרך פשוטה לזהות ולהסיר רשומות כפולות.

- **זיהוי כפילויות: `duplicated`**: ניתן לזהות בקלות ערכים כפולים באמצעות המתודה `duplicated` ב-pandas, שמחזירה מסכה בוליאנית המציינת האם רשומה ב-`DataFrame` היא כפולה של רשומה קודמת. בואו ניצור דוגמה נוספת של `DataFrame` כדי לראות זאת בפעולה.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |letters|numbers|
|------|-------|-------|
|0     |A      |1      |
|1     |B      |2      |
|2     |A      |1      |
|3     |B      |3      |
|4     |B      |3      |

```python
example4.duplicated()
```
```
0    False
1    False
2     True
3    False
4     True
dtype: bool
```
- **הסרת כפילויות: `drop_duplicates`:** מחזירה פשוט עותק של הנתונים שבו כל הערכים הכפולים הם `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
גם `duplicated` וגם `drop_duplicates` בברירת מחדל מתייחסים לכל העמודות, אך ניתן להגדיר שהם יבדקו רק תת-קבוצה של עמודות ב-`DataFrame` שלך:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **עיקרון חשוב:** הסרת נתונים כפולים היא חלק חיוני כמעט בכל פרויקט מדעי נתונים. נתונים כפולים יכולים לשנות את תוצאות הניתוחים שלך ולספק תוצאות לא מדויקות!


## 🚀 אתגר

כל החומרים שנדונו זמינים כ-[Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). בנוסף, ישנם תרגילים לאחר כל חלק, נסה אותם!

## [שאלון לאחר ההרצאה](https://ff-quizzes.netlify.app/en/ds/)



## סקירה ולימוד עצמי

ישנן דרכים רבות לגלות ולגשת להכנת הנתונים שלך לניתוח ולמודלים, וניקוי הנתונים הוא שלב חשוב שהוא חוויה מעשית. נסה את האתגרים הללו מ-Kaggle כדי לחקור טכניקות שהשיעור הזה לא כיסה.

- [אתגר ניקוי נתונים: ניתוח תאריכים](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [אתגר ניקוי נתונים: סקל ונרמול נתונים](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## משימה

[הערכת נתונים מטופס](assignment.md)

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.