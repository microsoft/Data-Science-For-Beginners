<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "42119bcc97bee88254e381156d770f3c",
  "translation_date": "2025-09-05T23:21:03+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "he"
}
-->
# הצגת פרופורציות

|![סקצ'נוט מאת [(@sketchthedocs)](https://sketchthedocs.dev)](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|הצגת פרופורציות - _סקצ'נוט מאת [@nitya](https://twitter.com/nitya)_ |

בשיעור זה, תשתמשו במאגר נתונים ממוקד-טבע כדי להציג פרופורציות, כמו כמה סוגים שונים של פטריות מופיעים במאגר נתונים מסוים על פטריות. בואו נחקור את הפטריות המרתקות הללו באמצעות מאגר נתונים שמקורו ב-Audubon, הכולל פרטים על 23 מינים של פטריות בעלות זימים ממשפחות Agaricus ו-Lepiota. תתנסו בהדמיות מעניינות כמו:

- תרשימי עוגה 🥧  
- תרשימי דונאט 🍩  
- תרשימי וופל 🧇  

> 💡 פרויקט מעניין מאוד בשם [Charticulator](https://charticulator.com) מבית Microsoft Research מציע ממשק גרירה ושחרור חינמי ליצירת הדמיות נתונים. באחד המדריכים שלהם הם משתמשים גם במאגר הנתונים הזה על פטריות! כך תוכלו לחקור את הנתונים וללמוד את הספרייה בו-זמנית: [מדריך Charticulator](https://charticulator.com/tutorials/tutorial4.html).

## [שאלון לפני השיעור](https://ff-quizzes.netlify.app/en/ds/quiz/20)

## הכירו את הפטריות שלכם 🍄

פטריות הן מאוד מעניינות. בואו נייבא מאגר נתונים כדי ללמוד עליהן:

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```  
טבלה מוצגת עם נתונים נהדרים לניתוח:

| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| רעילה     | קמורה    | חלקה        | חומה      | חבורות  | חריפה   | חופשית          | צפופה        | צרה       | שחורה      | מתרחבת      | שווה       | חלקה                     | חלקה                     | לבנה                   | לבנה                   | חלקית     | לבנה       | אחת         | תלויה    | שחורה             | מפוזרת     | עירונית |
| אכילה     | קמורה    | חלקה        | צהובה     | חבורות  | שקדים   | חופשית          | צפופה        | רחבה      | שחורה      | מתרחבת      | מועדון     | חלקה                     | חלקה                     | לבנה                   | לבנה                   | חלקית     | לבנה       | אחת         | תלויה    | חומה              | מרובה      | עשב |
| אכילה     | פעמון    | חלקה        | לבנה      | חבורות  | אניס    | חופשית          | צפופה        | רחבה      | חומה       | מתרחבת      | מועדון     | חלקה                     | חלקה                     | לבנה                   | לבנה                   | חלקית     | לבנה       | אחת         | תלויה    | חומה              | מרובה      | אחו |
| רעילה     | קמורה    | קשקשית      | לבנה      | חבורות  | חריפה   | חופשית          | צפופה        | צרה       | חומה       | מתרחבת      | שווה       | חלקה                     | חלקה                     | לבנה                   | לבנה                   | חלקית     | לבנה       | אחת         | תלויה    | שחורה             | מפוזרת     | עירונית |

מיד שמים לב שכל הנתונים הם טקסטואליים. תצטרכו להמיר את הנתונים הללו כדי שתוכלו להשתמש בהם בתרשים. רוב הנתונים, למעשה, מיוצגים כאובייקט:

```python
print(mushrooms.select_dtypes(["object"]).columns)
```

הפלט הוא:

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```  
קחו את הנתונים הללו והמירו את עמודת 'class' לקטגוריה:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```

כעת, אם תדפיסו את נתוני הפטריות, תוכלו לראות שהם חולקו לקטגוריות לפי מחלקת רעילות/אכילה:

|           | cap-shape | cap-surface | cap-color | bruises | odor | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | ... | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ---- | --------------- | ------------ | --------- | ---------- | ----------- | --- | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| class     |           |             |           |         |      |                 |              |           |            |             |     |                          |                        |                        |           |            |             |           |                   |            |         |
| אכילה     | 4208      | 4208        | 4208      | 4208    | 4208 | 4208            | 4208         | 4208      | 4208       | 4208        | ... | 4208                     | 4208                   | 4208                   | 4208      | 4208       | 4208        | 4208      | 4208              | 4208       | 4208    |
| רעילה     | 3916      | 3916        | 3916      | 3916    | 3916 | 3916            | 3916         | 3916      | 3916       | 3916        | ... | 3916                     | 3916                   | 3916                   | 3916      | 3916       | 3916        | 3916      | 3916              | 3916       | 3916    |

אם תעקבו אחר הסדר המוצג בטבלה זו ליצירת תוויות קטגוריות, תוכלו לבנות תרשים עוגה:

## עוגה!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```  
והנה, תרשים עוגה שמציג את הפרופורציות של נתונים אלו לפי שתי הקטגוריות של פטריות. חשוב מאוד לוודא שהסדר של התוויות נכון, במיוחד כאן, אז הקפידו לבדוק את הסדר שבו נבנית מערך התוויות!

![תרשים עוגה](../../../../3-Data-Visualization/11-visualization-proportions/images/pie1-wb.png)

## דונאט!

תרשים עוגה מעניין יותר מבחינה ויזואלית הוא תרשים דונאט, שהוא תרשים עוגה עם חור במרכז. בואו נסתכל על הנתונים שלנו בשיטה זו.

הסתכלו על בתי הגידול השונים שבהם פטריות גדלות:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```  
כאן, אתם מקבצים את הנתונים לפי בית גידול. ישנם 7 בתי גידול רשומים, אז השתמשו בהם כתוויות לתרשים הדונאט שלכם:

```python
labels=['Grasses','Leaves','Meadows','Paths','Urban','Waste','Wood']

plt.pie(habitat['class'], labels=labels,
        autopct='%1.1f%%', pctdistance=0.85)
  
center_circle = plt.Circle((0, 0), 0.40, fc='white')
fig = plt.gcf()

fig.gca().add_artist(center_circle)
  
plt.title('Mushroom Habitats')
  
plt.show()
```

![תרשים דונאט](../../../../3-Data-Visualization/11-visualization-proportions/images/donut-wb.png)

הקוד הזה מצייר תרשים ומעגל מרכזי, ואז מוסיף את המעגל המרכזי לתרשים. ערכו את רוחב המעגל המרכזי על ידי שינוי `0.40` לערך אחר.

ניתן לשנות תרשימי דונאט בדרכים שונות כדי לשפר את התוויות. התוויות בפרט יכולות להיות מודגשות לקריאות טובה יותר. למדו עוד ב-[תיעוד](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut).

כעת, כשאתם יודעים כיצד לקבץ את הנתונים שלכם ואז להציגם כעוגה או דונאט, תוכלו לחקור סוגים אחרים של תרשימים. נסו תרשים וופל, שהוא פשוט דרך שונה לחקור כמויות.

## וופלים!

תרשים מסוג 'וופל' הוא דרך שונה להציג כמויות כטבלה דו-ממדית של ריבועים. נסו להציג את הכמויות השונות של צבעי כובע הפטריות במאגר הנתונים הזה. לשם כך, תצטרכו להתקין ספריית עזר בשם [PyWaffle](https://pypi.org/project/pywaffle/) ולהשתמש ב-Matplotlib:

```python
pip install pywaffle
```

בחרו קטע מהנתונים שלכם לקיבוץ:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```

צרו תרשים וופל על ידי יצירת תוויות ואז קיבוץ הנתונים שלכם:

```python
import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle
  
data ={'color': ['brown', 'buff', 'cinnamon', 'green', 'pink', 'purple', 'red', 'white', 'yellow'],
    'amount': capcolor['class']
     }
  
df = pd.DataFrame(data)
  
fig = plt.figure(
    FigureClass = Waffle,
    rows = 100,
    values = df.amount,
    labels = list(df.color),
    figsize = (30,30),
    colors=["brown", "tan", "maroon", "green", "pink", "purple", "red", "whitesmoke", "yellow"],
)
```

באמצעות תרשים וופל, ניתן לראות בבירור את הפרופורציות של צבעי כובעי הפטריות במאגר הנתונים הזה. מעניין לראות שיש הרבה פטריות עם כובעים ירוקים!

![תרשים וופל](../../../../3-Data-Visualization/11-visualization-proportions/images/waffle.png)

✅ PyWaffle תומכת באייקונים בתוך התרשימים שמשתמשים בכל אייקון זמין ב-[Font Awesome](https://fontawesome.com/). ערכו ניסויים ליצירת תרשים וופל מעניין יותר באמצעות אייקונים במקום ריבועים.

בשיעור זה למדתם שלוש דרכים להציג פרופורציות. ראשית, עליכם לקבץ את הנתונים שלכם לקטגוריות ואז להחליט מהי הדרך הטובה ביותר להציג את הנתונים - עוגה, דונאט, או וופל. כל הדרכים טעימות ומספקות למשתמש תמונת מצב מיידית של מאגר הנתונים.

## 🚀 אתגר

נסו לשחזר את התרשימים הטעימים הללו ב-[Charticulator](https://charticulator.com).

## [שאלון לאחר השיעור](https://ff-quizzes.netlify.app/en/ds/quiz/21)

## סקירה ולמידה עצמית

לפעמים לא ברור מתי להשתמש בתרשים עוגה, דונאט, או וופל. הנה כמה מאמרים לקריאה בנושא:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

ערכו מחקר נוסף כדי למצוא מידע נוסף על ההחלטה הדביקה הזו.

## משימה

[נסו זאת ב-Excel](assignment.md)  

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית נחשב למקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי בני אדם. איננו נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.