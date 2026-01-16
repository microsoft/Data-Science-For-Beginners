<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-28T15:30:53+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "he"
}
-->
# ויזואליזציה של כמויות
|![סקצ'נוט מאת [(@sketchthedocs)](https://sketchthedocs.dev)](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| ויזואליזציה של כמויות - _סקצ'נוט מאת [@nitya](https://twitter.com/nitya)_ |

בשיעור זה תלמדו כיצד להשתמש בכמה מהספריות הרבות הזמינות ב-R כדי ליצור ויזואליזציות מעניינות סביב מושג הכמות. באמצעות מערך נתונים נקי על ציפורים ממינסוטה, תוכלו ללמוד עובדות מעניינות רבות על חיי הבר המקומיים.  
## [שאלון לפני השיעור](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## התבוננות במוטת כנפיים עם ggplot2
ספרייה מצוינת ליצירת גרפים ותרשימים פשוטים ומורכבים מסוגים שונים היא [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html). באופן כללי, תהליך יצירת גרפים באמצעות ספריות אלו כולל זיהוי החלקים במערך הנתונים שברצונכם למקד, ביצוע טרנספורמציות נחוצות על הנתונים, הקצאת ערכי ציר x ו-y, בחירת סוג הגרף להצגה, ואז הצגת הגרף.

`ggplot2` היא מערכת ליצירת גרפיקה באופן דקלרטיבי, המבוססת על "דקדוק הגרפיקה". [דקדוק הגרפיקה](https://en.wikipedia.org/wiki/Ggplot2) הוא שיטה כללית לויזואליזציה של נתונים שמפרקת גרפים לרכיבים סמנטיים כמו סולמות ושכבות. במילים אחרות, הקלות שבה ניתן ליצור גרפים ותרשימים לנתונים חד-משתניים או רב-משתניים עם מעט קוד הופכת את `ggplot2` לחבילה הפופולרית ביותר לויזואליזציה ב-R. המשתמש מציין ל-`ggplot2` כיצד למפות את המשתנים לאסתטיקה, אילו פרימיטיבים גרפיים להשתמש, ו-`ggplot2` מטפלת בשאר.

> ✅ גרף = נתונים + אסתטיקה + גיאומטריה  
> - נתונים מתייחסים למערך הנתונים  
> - אסתטיקה מציינת את המשתנים הנחקרים (משתני x ו-y)  
> - גיאומטריה מתייחסת לסוג הגרף (גרף קווי, גרף עמודות וכו')  

בחרו את הגיאומטריה המתאימה (סוג הגרף) בהתאם לנתונים ולסיפור שברצונכם לספר באמצעות הגרף.

> - לניתוח מגמות: קו, עמודות  
> - להשוואת ערכים: עמודות, עוגה, פיזור  
> - להראות כיצד חלקים קשורים לשלם: עוגה  
> - להראות התפלגות נתונים: פיזור, עמודות  
> - להראות קשרים בין ערכים: קו, פיזור, בועה  

✅ תוכלו גם לעיין ב[דף עזר](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf) המתאר את ggplot2.

## יצירת גרף קווי על ערכי מוטת כנפיים של ציפורים

פתחו את קונסולת R וייבאו את מערך הנתונים.  
> הערה: מערך הנתונים מאוחסן בתיקיית `/data` בשורש המאגר.

ייבאו את מערך הנתונים והתבוננו ב-5 השורות הראשונות של הנתונים.

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```  
הנתונים כוללים תערובת של טקסט ומספרים:

|      | שם                          | שם מדעי                | קטגוריה               | סדר          | משפחה   | סוג         | מצב שימור         | אורך מינימלי | אורך מקסימלי | מסה מינימלית | מסה מקסימלית | מוטת כנפיים מינימלית | מוטת כנפיים מקסימלית |
| ---: | :-------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :---------------- | ------------: | ------------: | ------------: | ------------: | --------------------: | --------------------: |
|    0 | ברווז שורק שחור-בטן        | Dendrocygna autumnalis | ברווזים/אווזים/עופות מים | Anseriformes | Anatidae | Dendrocygna | LC                 |        47     |        56     |         652   |        1020   |          76          |          94          |
|    1 | ברווז שורק חום              | Dendrocygna bicolor    | ברווזים/אווזים/עופות מים | Anseriformes | Anatidae | Dendrocygna | LC                 |        45     |        53     |         712   |        1050   |          85          |          93          |
|    2 | אווז שלג                    | Anser caerulescens     | ברווזים/אווזים/עופות מים | Anseriformes | Anatidae | Anser       | LC                 |        64     |        79     |        2050   |        4050   |         135          |         165          |
|    3 | אווז רוס                   | Anser rossii           | ברווזים/אווזים/עופות מים | Anseriformes | Anatidae | Anser       | LC                 |      57.3     |        64     |        1066   |        1567   |         113          |         116          |
|    4 | אווז לבן-מצח גדול           | Anser albifrons        | ברווזים/אווזים/עופות מים | Anseriformes | Anatidae | Anser       | LC                 |        64     |        81     |        1930   |        3310   |         130          |         165          |

נתחיל בשרטוט נתונים מספריים באמצעות גרף קווי בסיסי. נניח שברצונכם לראות את מוטת הכנפיים המקסימלית של הציפורים המעניינות הללו.

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```  
כאן, אתם מתקינים את חבילת `ggplot2` ואז מייבאים אותה לסביבת העבודה באמצעות הפקודה `library("ggplot2")`. כדי לשרטט כל גרף ב-ggplot, משתמשים בפונקציה `ggplot()` ומציינים את מערך הנתונים, משתני x ו-y כמאפיינים. במקרה זה, אנו משתמשים בפונקציה `geom_line()` מכיוון שאנו מכוונים לשרטט גרף קווי.

![MaxWingspan-lineplot](../../../../../translated_images/he/MaxWingspan-lineplot.b12169f99d26fdd263f291008dfd73c18a4ba8f3d32b1fda3d74af51a0a28616.png)

מה אתם מבחינים מיד? נראה שיש לפחות ערך חריג אחד - זו מוטת כנפיים מרשימה! מוטת כנפיים של יותר מ-2000 ס"מ שווה ליותר מ-20 מטרים - האם יש פטרודקטילים במינסוטה? בואו נחקור.

בעוד שתוכלו לבצע מיון מהיר ב-Excel כדי למצוא את הערכים החריגים, שהם כנראה טעויות הקלדה, המשיכו בתהליך הוויזואליזציה מתוך הגרף.

הוסיפו תוויות לציר ה-x כדי להראות אילו סוגי ציפורים מדובר:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```  
אנו מציינים את הזווית ב-`theme` ומציינים את התוויות של צירי x ו-y ב-`xlab()` ו-`ylab()` בהתאמה. הפונקציה `ggtitle()` נותנת שם לגרף/תרשים.

![MaxWingspan-lineplot-improved](../../../../../translated_images/he/MaxWingspan-lineplot-improved.04b73b4d5a59552a6bc7590678899718e1f065abe9eada9ebb4148939b622fd4.png)

גם עם סיבוב התוויות ל-45 מעלות, יש יותר מדי תוויות לקריאה. בואו ננסה אסטרטגיה שונה: תייגו רק את הערכים החריגים והציבו את התוויות בתוך הגרף. תוכלו להשתמש בגרף פיזור כדי לפנות יותר מקום לתיוג:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```  
מה קורה כאן? השתמשתם בפונקציה `geom_point()` כדי לשרטט נקודות פיזור. עם זאת, הוספתם תוויות לציפורים שמוטת הכנפיים המקסימלית שלהן `MaxWingspan > 500` וגם הסתרתם את התוויות על ציר x כדי להפחית עומס בגרף.

מה אתם מגלים?

![MaxWingspan-scatterplot](../../../../../translated_images/he/MaxWingspan-scatterplot.60dc9e0e19d32700283558f253841fdab5104abb62bc96f7d97f9c0ee857fa8b.png)

## סינון הנתונים

גם העיט הקירח וגם הבז הערבתי, למרות שהם כנראה ציפורים גדולות מאוד, נראים כמתויגים באופן שגוי, עם תוספת של 0 למוטת הכנפיים המקסימלית שלהם. לא סביר שתפגשו עיט קירח עם מוטת כנפיים של 25 מטרים, אבל אם כן, אנא עדכנו אותנו! בואו ניצור מערך נתונים חדש ללא שני הערכים החריגים הללו:

```r
birds_filtered <- subset(birds, MaxWingspan < 500)

ggplot(data=birds_filtered, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  ylab("Wingspan (CM)") +
  xlab("Birds") +
  ggtitle("Max Wingspan in Centimeters") + 
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) +
  theme(axis.text.x=element_blank(), axis.ticks.x=element_blank())
```  
יצרנו מערך נתונים חדש `birds_filtered` ואז שרטטנו גרף פיזור. על ידי סינון הערכים החריגים, הנתונים שלכם כעת יותר קוהרנטיים ומובנים.

![MaxWingspan-scatterplot-improved](../../../../../translated_images/he/MaxWingspan-scatterplot-improved.7d0af81658c65f3e75b8fedeb2335399e31108257e48db15d875ece608272051.png)

כעת, כשיש לנו מערך נתונים נקי יותר לפחות מבחינת מוטת כנפיים, בואו נגלה עוד על הציפורים הללו.

בעוד שגרפים קוויים וגרפי פיזור יכולים להציג מידע על ערכי נתונים וההתפלגות שלהם, אנו רוצים לחשוב על הערכים הטמונים במערך הנתונים הזה. תוכלו ליצור ויזואליזציות כדי לענות על השאלות הבאות על כמויות:

> כמה קטגוריות של ציפורים יש, ומה המספרים שלהן?  
> כמה ציפורים נכחדו, בסכנת הכחדה, נדירות או נפוצות?  
> כמה יש מכל סוג וסדר במינוח של לינאוס?  
## חקר גרפי עמודות

גרפי עמודות הם פרקטיים כאשר יש צורך להציג קבוצות של נתונים. בואו נחקור את קטגוריות הציפורים הקיימות במערך הנתונים הזה כדי לראות איזו קטגוריה היא הנפוצה ביותר לפי מספר.  
ניצור גרף עמודות על נתונים מסוננים.

```r
install.packages("dplyr")
install.packages("tidyverse")

library(lubridate)
library(scales)
library(dplyr)
library(ggplot2)
library(tidyverse)

birds_filtered %>% group_by(Category) %>%
  summarise(n=n(),
  MinLength = mean(MinLength),
  MaxLength = mean(MaxLength),
  MinBodyMass = mean(MinBodyMass),
  MaxBodyMass = mean(MaxBodyMass),
  MinWingspan=mean(MinWingspan),
  MaxWingspan=mean(MaxWingspan)) %>% 
  gather("key", "value", - c(Category, n)) %>%
  ggplot(aes(x = Category, y = value, group = key, fill = key)) +
  geom_bar(stat = "identity") +
  scale_fill_manual(values = c("#D62728", "#FF7F0E", "#8C564B","#2CA02C", "#1F77B4", "#9467BD")) +                   
  xlab("Category")+ggtitle("Birds of Minnesota")

```  
בקטע הבא, אנו מתקינים את החבילות [dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8) ו-[lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0) כדי לעזור במניפולציה וקיבוץ נתונים לצורך שרטוט גרף עמודות מוערם. תחילה, מקבצים את הנתונים לפי `Category` של הציפור ואז מסכמים את העמודות `MinLength`, `MaxLength`, `MinBodyMass`, `MaxBodyMass`, `MinWingspan`, `MaxWingspan`. לאחר מכן, שרטטו את גרף העמודות באמצעות חבילת `ggplot2` וציינו את הצבעים עבור הקטגוריות השונות והתוויות.

![Stacked bar chart](../../../../../translated_images/he/stacked-bar-chart.0c92264e89da7b391a7490224d1e7059a020e8b74dcd354414aeac78871c02f1.png)

גרף העמודות הזה, עם זאת, אינו קריא מכיוון שיש יותר מדי נתונים לא מקובצים. יש לבחור רק את הנתונים שברצונכם לשרטט, אז בואו נסתכל על אורך הציפורים לפי הקטגוריה שלהן.

סננו את הנתונים כך שיכללו רק את קטגוריית הציפורים.

מכיוון שיש קטגוריות רבות, תוכלו להציג את הגרף הזה בצורה אנכית ולהתאים את גובהו כך שיכלול את כל הנתונים:

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```  
תחילה סופרים ערכים ייחודיים בעמודת `Category` ואז ממיינים אותם למערך נתונים חדש `birds_count`. נתונים ממיונים אלו מתועלים באותה רמה כך שהם משורטטים בסדר המיועד. באמצעות `ggplot2` אתם שרטטתם את הנתונים בגרף עמודות. הפונקציה `coord_flip()` מציגה עמודות אופקיות.

![category-length](../../../../../translated_images/he/category-length.7e34c296690e85d64f7e4d25a56077442683eca96c4f5b4eae120a64c0755636.png)

גרף העמודות הזה מציג מבט טוב על מספר הציפורים בכל קטגוריה. במבט חטוף, ניתן לראות שמספר הציפורים הגדול ביותר באזור זה שייך לקטגוריית ברווזים/אווזים/עופות מים. מינסוטה היא "ארץ 10,000 האגמים", כך שזה לא מפתיע!

✅ נסו לספור נתונים אחרים במערך הנתונים הזה. האם משהו מפתיע אתכם?

## השוואת נתונים

תוכלו לנסות השוואות שונות של נתונים מקובצים על ידי יצירת צירים חדשים. נסו השוואה של האורך המקסימלי של ציפור, בהתבסס על הקטגוריה שלה:

```r
birds_grouped <- birds_filtered %>%
  group_by(Category) %>%
  summarise(
  MaxLength = max(MaxLength, na.rm = T),
  MinLength = max(MinLength, na.rm = T)
           ) %>%
  arrange(Category)
  
ggplot(birds_grouped,aes(Category,MaxLength))+geom_bar(stat="identity")+coord_flip()
```  
אנו מקבצים את הנתונים המסוננים `birds_filtered` לפי `Category` ואז שרטטנו גרף עמודות.

![comparing data](../../../../../translated_images/he/comparingdata.f486a450d61c7ca5416f27f3f55a6a4465d00df3be5e6d33936e9b07b95e2fdd.png)

אין כאן הפתעות: לקוליברי יש את האורך המקסימלי הקטן ביותר בהשוואה לפליקנים או אווזים. זה טוב כאשר הנתונים הגיוניים מבחינה לוגית!

תוכלו ליצור ויזואליזציות מעניינות יותר של גרפי עמודות על ידי חפיפת נתונים. בואו נחפוף את האורך המינימלי והמקסימלי על קטגוריית ציפור נתונה:

```r
ggplot(data=birds_grouped, aes(x=Category)) +
  geom_bar(aes(y=MaxLength), stat="identity", position ="identity",  fill='blue') +
  geom_bar(aes(y=MinLength), stat="identity", position="identity", fill='orange')+
  coord_flip()
```  
![super-imposed values](../../../../../translated_images/he/superimposed-values.5363f0705a1da4167625a373a1064331ea3cb7a06a297297d0734fcc9b3819a0.png)

## 🚀 אתגר

מערך הנתונים הזה על ציפורים מציע שפע של מידע על סוגים שונים של ציפורים בתוך מערכת אקולוגית מסוימת. חפשו באינטרנט ונסו למצוא מערכי נתונים נוספים על ציפורים. תרגלו יצירת גרפים ותרשימים סביב הציפורים הללו כדי לגלות עובדות שלא ידעתם.

## [שאלון לאחר השיעור](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## סקירה ולימוד עצמי

השיעור הראשון הזה נתן לכם מידע על איך להשתמש ב-`ggplot2` לויזואליזציה של כמויות. בצעו מחקר על דרכים נוספות לעבודה עם מערכי נתונים לויזואליזציה. חפשו מערכי נתונים שתוכלו לויזואליזציה באמצעות חבילות אחרות כמו [Lattice](https://stat.ethz.ch/R-manual/R-devel/library/lattice/html/Lattice.html) ו-[Plotly](https://github.com/plotly/plotly.R#readme).

## משימה  
[קווים, פיזורים ועמודות](assignment.md)  

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו אחראים לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.