<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "42119bcc97bee88254e381156d770f3c",
  "translation_date": "2025-09-06T06:42:26+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "ur"
}
-->
# تناسبات کی بصری نمائندگی

|![ [(@sketchthedocs)](https://sketchthedocs.dev) کی اسکیچ نوٹ ](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|تناسبات کی بصری نمائندگی - _[@nitya](https://twitter.com/nitya) کی اسکیچ نوٹ_ |

اس سبق میں، آپ ایک مختلف قدرتی ڈیٹا سیٹ استعمال کریں گے تاکہ تناسبات کو بصری طور پر سمجھ سکیں، جیسے کہ مشرومز کے بارے میں دیے گئے ڈیٹا سیٹ میں کتنی مختلف اقسام کے فنگس موجود ہیں۔ آئیے ان دلچسپ فنگس کو ایک ڈیٹا سیٹ کے ذریعے دریافت کریں جو آڈوبون سے حاصل کیا گیا ہے اور اس میں ایگاریکس اور لیپیوٹا خاندانوں کے 23 اقسام کے مشرومز کی تفصیلات شامل ہیں۔ آپ مزیدار بصری نمائندگیوں کے ساتھ تجربہ کریں گے جیسے:

- پائی چارٹس 🥧
- ڈونٹ چارٹس 🍩
- وافل چارٹس 🧇

> 💡 مائیکروسافٹ ریسرچ کا ایک بہت دلچسپ پروجیکٹ [Charticulator](https://charticulator.com) ایک مفت ڈریگ اینڈ ڈراپ انٹرفیس فراہم کرتا ہے ڈیٹا ویژولائزیشن کے لیے۔ ان کے ایک ٹیوٹوریل میں بھی یہ مشروم ڈیٹا سیٹ استعمال کیا گیا ہے! تو آپ ڈیٹا کو دریافت کر سکتے ہیں اور ساتھ ہی لائبریری سیکھ سکتے ہیں: [Charticulator tutorial](https://charticulator.com/tutorials/tutorial4.html)۔

## [لیکچر سے پہلے کا کوئز](https://ff-quizzes.netlify.app/en/ds/quiz/20)

## اپنے مشرومز کو جانیں 🍄

مشرومز بہت دلچسپ ہیں۔ آئیے ایک ڈیٹا سیٹ درآمد کریں تاکہ ان کا مطالعہ کیا جا سکے:

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```
ایک ٹیبل پرنٹ ہوتا ہے جس میں تجزیے کے لیے بہترین ڈیٹا موجود ہے:


| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Poisonous | Convex    | Smooth      | Brown     | Bruises | Pungent | Free            | Close        | Narrow    | Black      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |
| Edible    | Convex    | Smooth      | Yellow    | Bruises | Almond  | Free            | Close        | Broad     | Black      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Grasses |
| Edible    | Bell      | Smooth      | White     | Bruises | Anise   | Free            | Close        | Broad     | Brown      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Meadows |
| Poisonous | Convex    | Scaly       | White     | Bruises | Pungent | Free            | Close        | Narrow    | Brown      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |

فوراً آپ دیکھتے ہیں کہ تمام ڈیٹا متنی ہے۔ آپ کو اس ڈیٹا کو چارٹ میں استعمال کرنے کے قابل بنانے کے لیے تبدیل کرنا ہوگا۔ حقیقت میں، زیادہ تر ڈیٹا ایک آبجیکٹ کے طور پر ظاہر ہوتا ہے:

```python
print(mushrooms.select_dtypes(["object"]).columns)
```

آؤٹ پٹ ہے:

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```
اس ڈیٹا کو لیں اور 'class' کالم کو ایک کیٹیگری میں تبدیل کریں:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```

اب، اگر آپ مشرومز کا ڈیٹا پرنٹ کریں، تو آپ دیکھ سکتے ہیں کہ اسے زہریلے/کھانے کے قابل کلاس کے مطابق کیٹیگریز میں گروپ کیا گیا ہے:


|           | cap-shape | cap-surface | cap-color | bruises | odor | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | ... | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ---- | --------------- | ------------ | --------- | ---------- | ----------- | --- | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| class     |           |             |           |         |      |                 |              |           |            |             |     |                          |                        |                        |           |            |             |           |                   |            |         |
| Edible    | 4208      | 4208        | 4208      | 4208    | 4208 | 4208            | 4208         | 4208      | 4208       | 4208        | ... | 4208                     | 4208                   | 4208                   | 4208      | 4208       | 4208        | 4208      | 4208              | 4208       | 4208    |
| Poisonous | 3916      | 3916        | 3916      | 3916    | 3916 | 3916            | 3916         | 3916      | 3916       | 3916        | ... | 3916                     | 3916                   | 3916                   | 3916      | 3916       | 3916        | 3916      | 3916              | 3916       | 3916    |

اگر آپ اس ٹیبل میں پیش کردہ ترتیب کے مطابق اپنی کلاس کیٹیگری لیبلز بنائیں، تو آپ ایک پائی چارٹ بنا سکتے ہیں:

## پائی!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```
دیکھیں، ایک پائی چارٹ جو اس ڈیٹا کو ان دو مشرومز کی کلاسز کے مطابق تناسبات دکھاتا ہے۔ لیبلز کی ترتیب کو درست رکھنا خاص طور پر یہاں بہت اہم ہے، لہذا لیبل آرے کی ترتیب کی تصدیق ضرور کریں!

![پائی چارٹ](../../../../3-Data-Visualization/11-visualization-proportions/images/pie1-wb.png)

## ڈونٹس!

ایک قدرے زیادہ بصری دلچسپ پائی چارٹ ڈونٹ چارٹ ہے، جو ایک پائی چارٹ ہے جس کے درمیان میں ایک سوراخ ہوتا ہے۔ آئیے اپنے ڈیٹا کو اس طریقے سے دیکھتے ہیں۔

مشرومز کے مختلف رہائش گاہوں پر نظر ڈالیں:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```
یہاں، آپ اپنے ڈیٹا کو رہائش گاہ کے مطابق گروپ کر رہے ہیں۔ سات درج ہیں، لہذا انہیں اپنے ڈونٹ چارٹ کے لیبلز کے طور پر استعمال کریں:

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

![ڈونٹ چارٹ](../../../../3-Data-Visualization/11-visualization-proportions/images/donut-wb.png)

یہ کوڈ ایک چارٹ اور ایک مرکز کا دائرہ بناتا ہے، پھر اس مرکز کے دائرے کو چارٹ میں شامل کرتا ہے۔ مرکز کے دائرے کی چوڑائی کو تبدیل کرنے کے لیے `0.40` کو کسی اور قدر میں تبدیل کریں۔

ڈونٹ چارٹس کو کئی طریقوں سے ایڈجسٹ کیا جا سکتا ہے تاکہ لیبلز کو تبدیل کیا جا سکے۔ خاص طور پر لیبلز کو پڑھنے میں آسانی کے لیے نمایاں کیا جا سکتا ہے۔ مزید معلومات کے لیے [docs](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut) دیکھیں۔

اب جب کہ آپ نے اپنے ڈیٹا کو گروپ کرنا اور پھر اسے پائی یا ڈونٹ کے طور پر دکھانا سیکھ لیا ہے، آپ دیگر اقسام کے چارٹس کو بھی دریافت کر سکتے ہیں۔ ایک وافل چارٹ آزمائیں، جو مقدار کو دریافت کرنے کا ایک مختلف طریقہ ہے۔
## وافلز!

'وافل' قسم کا چارٹ مقدار کو 2D مربعوں کی صف کے طور پر بصری طور پر ظاہر کرنے کا ایک مختلف طریقہ ہے۔ اس ڈیٹا سیٹ میں مشرومز کی مختلف ٹوپی کے رنگوں کی مقدار کو بصری طور پر دیکھنے کی کوشش کریں۔ ایسا کرنے کے لیے، آپ کو ایک مددگار لائبریری [PyWaffle](https://pypi.org/project/pywaffle/) انسٹال کرنی ہوگی اور Matplotlib استعمال کرنا ہوگا:

```python
pip install pywaffle
```

اپنے ڈیٹا کے ایک حصے کو گروپ کرنے کے لیے منتخب کریں:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```

لیبلز بنا کر اور پھر اپنے ڈیٹا کو گروپ کر کے ایک وافل چارٹ بنائیں:

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

وافل چارٹ کا استعمال کرتے ہوئے، آپ اس مشرومز ڈیٹا سیٹ کے ٹوپی کے رنگوں کے تناسب کو واضح طور پر دیکھ سکتے ہیں۔ دلچسپ بات یہ ہے کہ بہت سے سبز ٹوپی والے مشرومز موجود ہیں!

![وافل چارٹ](../../../../3-Data-Visualization/11-visualization-proportions/images/waffle.png)

✅ Pywaffle چارٹس میں آئیکنز کی حمایت کرتا ہے جو [Font Awesome](https://fontawesome.com/) میں دستیاب کسی بھی آئیکن کو استعمال کرتے ہیں۔ آئیکنز کے بجائے مربعوں کا استعمال کرتے ہوئے ایک اور دلچسپ وافل چارٹ بنانے کے لیے کچھ تجربات کریں۔

اس سبق میں، آپ نے تناسبات کو بصری طور پر ظاہر کرنے کے تین طریقے سیکھے۔ پہلے، آپ کو اپنے ڈیٹا کو کیٹیگریز میں گروپ کرنا ہوگا اور پھر فیصلہ کرنا ہوگا کہ ڈیٹا کو ظاہر کرنے کا بہترین طریقہ کون سا ہے - پائی، ڈونٹ، یا وافل۔ یہ سب مزیدار ہیں اور صارف کو ڈیٹا سیٹ کا فوری جائزہ فراہم کرتے ہیں۔

## 🚀 چیلنج

[Charticulator](https://charticulator.com) میں ان مزیدار چارٹس کو دوبارہ بنانے کی کوشش کریں۔
## [لیکچر کے بعد کا کوئز](https://ff-quizzes.netlify.app/en/ds/quiz/21)

## جائزہ اور خود مطالعہ

کبھی کبھی یہ واضح نہیں ہوتا کہ پائی، ڈونٹ، یا وافل چارٹ کب استعمال کرنا ہے۔ اس موضوع پر پڑھنے کے لیے کچھ مضامین یہ ہیں:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

مزید معلومات حاصل کرنے کے لیے اس مشکل فیصلے پر تحقیق کریں۔
## اسائنمنٹ

[Excel میں آزمائیں](assignment.md)

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔