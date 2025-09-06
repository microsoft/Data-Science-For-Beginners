<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "47028abaaafa2bcb1079702d20569066",
  "translation_date": "2025-08-27T10:39:01+00:00",
  "source_file": "3-Data-Visualization/R/11-visualization-proportions/README.md",
  "language_code": "ur"
}
-->
# تناسبات کی بصری نمائندگی

|![ [(@sketchthedocs)](https://sketchthedocs.dev) کی اسکیچ نوٹ ](../../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|تناسبات کی بصری نمائندگی - _[@nitya](https://twitter.com/nitya) کی اسکیچ نوٹ_ |

اس سبق میں، آپ ایک مختلف قدرتی ڈیٹا سیٹ استعمال کریں گے تاکہ تناسبات کو بصری طور پر سمجھ سکیں، جیسے کہ مشرومز کے بارے میں دیے گئے ڈیٹا سیٹ میں کتنی مختلف اقسام کے فنگس موجود ہیں۔ آئیے ان دلچسپ فنگس کو ایک ڈیٹا سیٹ کے ذریعے دریافت کریں جو آڈوبون سے حاصل کیا گیا ہے اور اس میں Agaricus اور Lepiota خاندانوں کے 23 اقسام کے مشرومز کی تفصیلات شامل ہیں۔ آپ مزیدار بصری نمائندگیوں کے ساتھ تجربہ کریں گے جیسے:

- پائی چارٹس 🥧
- ڈونٹ چارٹس 🍩
- وافل چارٹس 🧇

> 💡 مائیکروسافٹ ریسرچ کا ایک بہت دلچسپ پروجیکٹ [Charticulator](https://charticulator.com) ایک مفت ڈریگ اینڈ ڈراپ انٹرفیس فراہم کرتا ہے ڈیٹا بصری نمائندگی کے لیے۔ ان کے ایک ٹیوٹوریل میں بھی یہ مشرومز کا ڈیٹا سیٹ استعمال کیا گیا ہے! تو آپ ڈیٹا کو دریافت کر سکتے ہیں اور لائبریری کو ایک ساتھ سیکھ سکتے ہیں: [Charticulator tutorial](https://charticulator.com/tutorials/tutorial4.html)۔

## [لیکچر سے پہلے کا کوئز](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## اپنے مشرومز کو جانیں 🍄

مشرومز بہت دلچسپ ہیں۔ آئیے ایک ڈیٹا سیٹ درآمد کریں تاکہ ان کا مطالعہ کیا جا سکے:

```r
mushrooms = read.csv('../../data/mushrooms.csv')
head(mushrooms)
```
ایک ٹیبل پرنٹ ہوتا ہے جس میں تجزیے کے لیے بہترین ڈیٹا موجود ہے:


| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Poisonous | Convex    | Smooth      | Brown     | Bruises | Pungent | Free            | Close        | Narrow    | Black      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |
| Edible    | Convex    | Smooth      | Yellow    | Bruises | Almond  | Free            | Close        | Broad     | Black      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Grasses |
| Edible    | Bell      | Smooth      | White     | Bruises | Anise   | Free            | Close        | Broad     | Brown      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Meadows |
| Poisonous | Convex    | Scaly       | White     | Bruises | Pungent | Free            | Close        | Narrow    | Brown      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban 
| Edible | Convex       |Smooth       | Green     | No Bruises| None   |Free            | Crowded       | Broad     | Black      | Tapering   | Equal      |  Smooth | Smooth                    | White                 | White                  | Partial    | White     | One         | Evanescent | Brown             | Abundant | Grasses
|Edible  |  Convex      | Scaly   | Yellow         | Bruises  | Almond  | Free | Close  |   Broad   |   Brown  | Enlarging   |   Club                      | Smooth                  | Smooth    | White                 |  White                | Partial      | White    |  One  |  Pendant | Black   | Numerous | Grasses
      
فوراً آپ دیکھتے ہیں کہ تمام ڈیٹا متنی ہے۔ آپ کو اس ڈیٹا کو چارٹ میں استعمال کرنے کے قابل بنانے کے لیے تبدیل کرنا ہوگا۔ حقیقت میں، زیادہ تر ڈیٹا ایک آبجیکٹ کے طور پر پیش کیا گیا ہے:

```r
names(mushrooms)
```

آؤٹ پٹ ہے:

```output
[1] "class"                    "cap.shape"               
 [3] "cap.surface"              "cap.color"               
 [5] "bruises"                  "odor"                    
 [7] "gill.attachment"          "gill.spacing"            
 [9] "gill.size"                "gill.color"              
[11] "stalk.shape"              "stalk.root"              
[13] "stalk.surface.above.ring" "stalk.surface.below.ring"
[15] "stalk.color.above.ring"   "stalk.color.below.ring"  
[17] "veil.type"                "veil.color"              
[19] "ring.number"              "ring.type"               
[21] "spore.print.color"        "population"              
[23] "habitat"            
```
اس ڈیٹا کو لیں اور 'class' کالم کو ایک کیٹیگری میں تبدیل کریں:

```r
library(dplyr)
grouped=mushrooms %>%
  group_by(class) %>%
  summarise(count=n())
```


اب، اگر آپ مشرومز کا ڈیٹا پرنٹ کریں، تو آپ دیکھ سکتے ہیں کہ اسے زہریلے/کھانے کے قابل کلاس کے مطابق کیٹیگریز میں گروپ کیا گیا ہے:
```r
View(grouped)
```


| class | count |
| --------- | --------- |
| Edible | 4208 |
| Poisonous| 3916 |



اگر آپ اس ٹیبل میں دیے گئے ترتیب کے مطابق اپنی کلاس کیٹیگری لیبلز بنائیں، تو آپ ایک پائی چارٹ بنا سکتے ہیں۔

## پائی!

```r
pie(grouped$count,grouped$class, main="Edible?")
```
دیکھیں، ایک پائی چارٹ جو اس ڈیٹا کو ان دو مشرومز کی کلاسز کے مطابق تناسبات دکھاتا ہے۔ لیبلز کی ترتیب کو درست رکھنا خاص طور پر یہاں بہت اہم ہے، لہذا لیبل آرے کی ترتیب کو ضرور چیک کریں!

![پائی چارٹ](../../../../../translated_images/pie1-wb.685df063673751f4b0b82127f7a52c7f9a920192f22ae61ad28412ba9ace97bf.ur.png)

## ڈونٹس!

پائی چارٹ کا ایک قدرے زیادہ بصری دلچسپ ورژن ڈونٹ چارٹ ہے، جو ایک پائی چارٹ ہے جس کے درمیان میں ایک سوراخ ہوتا ہے۔ آئیے اس طریقے سے اپنے ڈیٹا کو دیکھتے ہیں۔

مشرومز کے مختلف رہائش گاہوں پر نظر ڈالیں:

```r
library(dplyr)
habitat=mushrooms %>%
  group_by(habitat) %>%
  summarise(count=n())
View(habitat)
```
آؤٹ پٹ ہے:
| habitat| count |
| --------- | --------- |
| Grasses    | 2148 |
| Leaves| 832 |
| Meadows    | 292 |
| Paths| 1144 |
| Urban    | 368 |
| Waste| 192 |
| Wood| 3148 |


یہاں، آپ اپنے ڈیٹا کو رہائش گاہ کے مطابق گروپ کر رہے ہیں۔ 7 رہائش گاہیں درج ہیں، لہذا انہیں اپنے ڈونٹ چارٹ کے لیبلز کے طور پر استعمال کریں:

```r
library(ggplot2)
library(webr)
PieDonut(habitat, aes(habitat, count=count))
```

![ڈونٹ چارٹ](../../../../../translated_images/donut-wb.34e6fb275da9d834c2205145e39a3de9b6878191dcdba6f7a9e85f4b520449bc.ur.png)

یہ کوڈ دو لائبریریوں - ggplot2 اور webr - استعمال کرتا ہے۔ webr لائبریری کے PieDonut فنکشن کا استعمال کرتے ہوئے، ہم آسانی سے ایک ڈونٹ چارٹ بنا سکتے ہیں!

R میں ڈونٹ چارٹس صرف ggplot2 لائبریری کا استعمال کرتے ہوئے بھی بنائے جا سکتے ہیں۔ آپ اس کے بارے میں مزید [یہاں](https://www.r-graph-gallery.com/128-ring-or-donut-plot.html) سیکھ سکتے ہیں اور خود آزما سکتے ہیں۔

اب جب کہ آپ جانتے ہیں کہ اپنے ڈیٹا کو گروپ کیسے کرنا ہے اور پھر اسے پائی یا ڈونٹ کے طور پر کیسے دکھانا ہے، آپ دیگر اقسام کے چارٹس کو دریافت کر سکتے ہیں۔ ایک وافل چارٹ آزمائیں، جو مقدار کو دریافت کرنے کا ایک مختلف طریقہ ہے۔
## وافلز!

'وافل' قسم کا چارٹ مقدار کو 2D مربعوں کی صف کے طور پر بصری طور پر دکھانے کا ایک مختلف طریقہ ہے۔ اس ڈیٹا سیٹ میں مشرومز کی ٹوپی کے مختلف رنگوں کی مقدار کو بصری طور پر دیکھنے کی کوشش کریں۔ ایسا کرنے کے لیے، آپ کو ایک مددگار لائبریری [waffle](https://cran.r-project.org/web/packages/waffle/waffle.pdf) انسٹال کرنی ہوگی اور اسے اپنی بصری نمائندگی بنانے کے لیے استعمال کرنا ہوگا:

```r
install.packages("waffle", repos = "https://cinc.rud.is")
```

اپنے ڈیٹا کے ایک حصے کو گروپ کریں:

```r
library(dplyr)
cap_color=mushrooms %>%
  group_by(cap.color) %>%
  summarise(count=n())
View(cap_color)
```

وافل چارٹ بنانے کے لیے لیبلز بنائیں اور پھر اپنے ڈیٹا کو گروپ کریں:

```r
library(waffle)
names(cap_color$count) = paste0(cap_color$cap.color)
waffle((cap_color$count/10), rows = 7, title = "Waffle Chart")+scale_fill_manual(values=c("brown", "#F0DC82", "#D2691E", "green", 
                                                                                     "pink", "purple", "red", "grey", 
                                                                                     "yellow","white"))
```

وافل چارٹ کا استعمال کرتے ہوئے، آپ مشرومز کے اس ڈیٹا سیٹ میں ٹوپی کے رنگوں کے تناسب کو واضح طور پر دیکھ سکتے ہیں۔ دلچسپ بات یہ ہے کہ بہت سے سبز ٹوپی والے مشرومز موجود ہیں!

![وافل چارٹ](../../../../../translated_images/waffle.aaa75c5337735a6ef32ace0ffb6506ef49e5aefe870ffd72b1bb080f4843c217.ur.png)

اس سبق میں، آپ نے تناسبات کو بصری طور پر سمجھنے کے تین طریقے سیکھے۔ پہلے، آپ کو اپنے ڈیٹا کو کیٹیگریز میں گروپ کرنا ہوگا اور پھر فیصلہ کرنا ہوگا کہ ڈیٹا کو دکھانے کا بہترین طریقہ کون سا ہے - پائی، ڈونٹ، یا وافل۔ یہ سب مزیدار ہیں اور صارف کو ڈیٹا سیٹ کا فوری جائزہ فراہم کرتے ہیں۔

## 🚀 چیلنج

[Charticulator](https://charticulator.com) میں ان مزیدار چارٹس کو دوبارہ بنانے کی کوشش کریں۔
## [لیکچر کے بعد کا کوئز](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## جائزہ اور خود مطالعہ

کبھی کبھی یہ واضح نہیں ہوتا کہ پائی، ڈونٹ، یا وافل چارٹ کب استعمال کرنا ہے۔ اس موضوع پر پڑھنے کے لیے کچھ مضامین یہ ہیں:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

مزید معلومات حاصل کرنے کے لیے اس مشکل فیصلے پر تحقیق کریں۔
## اسائنمنٹ

[ایکسسل میں آزمائیں](assignment.md)

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔