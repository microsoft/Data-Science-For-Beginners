<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "47028abaaafa2bcb1079702d20569066",
  "translation_date": "2025-08-27T10:40:42+00:00",
  "source_file": "3-Data-Visualization/R/11-visualization-proportions/README.md",
  "language_code": "bn"
}
-->
# অনুপাতের ভিজ্যুয়ালাইজেশন

|![ স্কেচনোট [(@sketchthedocs)](https://sketchthedocs.dev) দ্বারা ](../../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|অনুপাতের ভিজ্যুয়ালাইজেশন - _[@nitya](https://twitter.com/nitya) দ্বারা স্কেচনোট_ |

এই পাঠে, আপনি প্রকৃতি-কেন্দ্রিক একটি ভিন্ন ডেটাসেট ব্যবহার করে অনুপাতের ভিজ্যুয়ালাইজেশন করবেন, যেমন একটি মাশরুম সম্পর্কিত ডেটাসেটে বিভিন্ন ধরনের ফাঙ্গি কীভাবে উপস্থিত রয়েছে। আসুন এই চমৎকার ফাঙ্গি সম্পর্কে জানি, যা Audubon থেকে সংগৃহীত একটি ডেটাসেট ব্যবহার করে Agaricus এবং Lepiota পরিবারের ২৩ প্রজাতির গিল্ড মাশরুমের তথ্য প্রদান করে। আপনি নিম্নলিখিত মজাদার ভিজ্যুয়ালাইজেশন নিয়ে পরীক্ষা করবেন:

- পাই চার্ট 🥧
- ডোনাট চার্ট 🍩
- ওয়াফল চার্ট 🧇

> 💡 Microsoft Research-এর একটি খুবই আকর্ষণীয় প্রকল্প [Charticulator](https://charticulator.com) একটি বিনামূল্যের ড্র্যাগ এবং ড্রপ ইন্টারফেস প্রদান করে ডেটা ভিজ্যুয়ালাইজেশনের জন্য। তাদের একটি টিউটোরিয়ালে তারা এই মাশরুম ডেটাসেটও ব্যবহার করেছে! তাই আপনি ডেটা অন্বেষণ করতে পারেন এবং একই সময়ে লাইব্রেরি শিখতে পারেন: [Charticulator টিউটোরিয়াল](https://charticulator.com/tutorials/tutorial4.html)।

## [পাঠ-পূর্ব কুইজ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## আপনার মাশরুম সম্পর্কে জানুন 🍄

মাশরুম খুবই আকর্ষণীয়। আসুন একটি ডেটাসেট আমদানি করে তা অধ্যয়ন করি:

```r
mushrooms = read.csv('../../data/mushrooms.csv')
head(mushrooms)
```
একটি টেবিল প্রিন্ট করা হয়েছে যা বিশ্লেষণের জন্য চমৎকার ডেটা প্রদান করে:


| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Poisonous | Convex    | Smooth      | Brown     | Bruises | Pungent | Free            | Close        | Narrow    | Black      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |
| Edible    | Convex    | Smooth      | Yellow    | Bruises | Almond  | Free            | Close        | Broad     | Black      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Grasses |
| Edible    | Bell      | Smooth      | White     | Bruises | Anise   | Free            | Close        | Broad     | Brown      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Meadows |
| Poisonous | Convex    | Scaly       | White     | Bruises | Pungent | Free            | Close        | Narrow    | Brown      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban 
| Edible | Convex       |Smooth       | Green     | No Bruises| None   |Free            | Crowded       | Broad     | Black      | Tapering   | Equal      |  Smooth | Smooth                    | White                 | White                  | Partial    | White     | One         | Evanescent | Brown             | Abundant | Grasses
|Edible  |  Convex      | Scaly   | Yellow         | Bruises  | Almond  | Free | Close  |   Broad   |   Brown  | Enlarging   |   Club                      | Smooth                  | Smooth    | White                 |  White                | Partial      | White    |  One  |  Pendant | Black   | Numerous | Grasses
      
প্রথমেই, আপনি লক্ষ্য করবেন যে সমস্ত ডেটা টেক্সট আকারে রয়েছে। এই ডেটাকে চার্টে ব্যবহার করার জন্য আপনাকে এটি রূপান্তর করতে হবে। প্রকৃতপক্ষে, বেশিরভাগ ডেটা একটি অবজেক্ট হিসেবে উপস্থাপিত হয়েছে:

```r
names(mushrooms)
```

আউটপুট হলো:

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
এই ডেটা নিন এবং 'class' কলামটিকে একটি ক্যাটাগরিতে রূপান্তর করুন:

```r
library(dplyr)
grouped=mushrooms %>%
  group_by(class) %>%
  summarise(count=n())
```


এখন, যদি আপনি মাশরুমের ডেটা প্রিন্ট করেন, আপনি দেখতে পাবেন এটি বিষাক্ত/খাদ্যযোগ্য শ্রেণী অনুযায়ী ক্যাটাগরিতে বিভক্ত হয়েছে:
```r
View(grouped)
```


| class | count |
| --------- | --------- |
| Edible | 4208 |
| Poisonous| 3916 |



যদি আপনি এই টেবিলে প্রদত্ত ক্রম অনুসরণ করে আপনার শ্রেণী ক্যাটাগরি লেবেল তৈরি করেন, তাহলে আপনি একটি পাই চার্ট তৈরি করতে পারবেন।

## পাই!

```r
pie(grouped$count,grouped$class, main="Edible?")
```
দেখুন, একটি পাই চার্ট যা এই ডেটার অনুপাত দেখাচ্ছে এই দুই শ্রেণীর মাশরুম অনুযায়ী। এখানে লেবেলের ক্রম সঠিকভাবে পাওয়া খুবই গুরুত্বপূর্ণ, তাই নিশ্চিত করুন যে লেবেল অ্যারে তৈরি করার সময় ক্রমটি যাচাই করেছেন!

![pie chart](../../../../../translated_images/pie1-wb.685df063673751f4b0b82127f7a52c7f9a920192f22ae61ad28412ba9ace97bf.bn.png)

## ডোনাট!

একটি কিছুটা বেশি আকর্ষণীয় পাই চার্ট হলো ডোনাট চার্ট, যা একটি পাই চার্ট যার মাঝখানে একটি গর্ত রয়েছে। আসুন এই পদ্ধতি ব্যবহার করে আমাদের ডেটা দেখি।

মাশরুমের বিভিন্ন আবাসস্থল দেখুন:

```r
library(dplyr)
habitat=mushrooms %>%
  group_by(habitat) %>%
  summarise(count=n())
View(habitat)
```
আউটপুট হলো:
| habitat| count |
| --------- | --------- |
| Grasses    | 2148 |
| Leaves| 832 |
| Meadows    | 292 |
| Paths| 1144 |
| Urban    | 368 |
| Waste| 192 |
| Wood| 3148 |


এখানে, আপনি আপনার ডেটাকে আবাসস্থল অনুযায়ী গ্রুপ করছেন। এখানে ৭টি তালিকাভুক্ত রয়েছে, তাই আপনার ডোনাট চার্টের জন্য সেগুলোকে লেবেল হিসেবে ব্যবহার করুন:

```r
library(ggplot2)
library(webr)
PieDonut(habitat, aes(habitat, count=count))
```

![donut chart](../../../../../translated_images/donut-wb.34e6fb275da9d834c2205145e39a3de9b6878191dcdba6f7a9e85f4b520449bc.bn.png)

এই কোডটি দুটি লাইব্রেরি ব্যবহার করে - ggplot2 এবং webr। webr লাইব্রেরির PieDonut ফাংশন ব্যবহার করে আমরা সহজেই একটি ডোনাট চার্ট তৈরি করতে পারি!

R-এ শুধুমাত্র ggplot2 লাইব্রেরি ব্যবহার করেও ডোনাট চার্ট তৈরি করা যায়। আপনি এটি সম্পর্কে আরও জানতে পারেন [এখানে](https://www.r-graph-gallery.com/128-ring-or-donut-plot.html) এবং নিজে চেষ্টা করতে পারেন।

এখন আপনি জানেন কীভাবে আপনার ডেটাকে গ্রুপ করতে হয় এবং তারপর এটি পাই বা ডোনাট হিসেবে প্রদর্শন করতে হয়, আপনি অন্যান্য ধরনের চার্ট অন্বেষণ করতে পারেন। একটি ওয়াফল চার্ট চেষ্টা করুন, যা পরিমাণ অন্বেষণের একটি ভিন্ন উপায়।

## ওয়াফল!

একটি 'ওয়াফল' টাইপ চার্ট হলো একটি ২D স্কোয়ারের অ্যারে হিসেবে পরিমাণ ভিজ্যুয়ালাইজ করার একটি ভিন্ন উপায়। এই ডেটাসেটে মাশরুমের ক্যাপ রঙের বিভিন্ন পরিমাণ ভিজ্যুয়ালাইজ করার চেষ্টা করুন। এটি করতে, আপনাকে একটি সহায়ক লাইব্রেরি [waffle](https://cran.r-project.org/web/packages/waffle/waffle.pdf) ইনস্টল করতে হবে এবং এটি ব্যবহার করে আপনার ভিজ্যুয়ালাইজেশন তৈরি করতে হবে:

```r
install.packages("waffle", repos = "https://cinc.rud.is")
```

আপনার ডেটার একটি অংশ নির্বাচন করুন এবং গ্রুপ করুন:

```r
library(dplyr)
cap_color=mushrooms %>%
  group_by(cap.color) %>%
  summarise(count=n())
View(cap_color)
```

লেবেল তৈরি করে এবং আপনার ডেটাকে গ্রুপ করে একটি ওয়াফল চার্ট তৈরি করুন:

```r
library(waffle)
names(cap_color$count) = paste0(cap_color$cap.color)
waffle((cap_color$count/10), rows = 7, title = "Waffle Chart")+scale_fill_manual(values=c("brown", "#F0DC82", "#D2691E", "green", 
                                                                                     "pink", "purple", "red", "grey", 
                                                                                     "yellow","white"))
```

ওয়াফল চার্ট ব্যবহার করে, আপনি স্পষ্টভাবে এই মাশরুম ডেটাসেটের ক্যাপ রঙের অনুপাত দেখতে পারেন। মজার বিষয় হলো, অনেক সবুজ ক্যাপযুক্ত মাশরুম রয়েছে!

![waffle chart](../../../../../translated_images/waffle.aaa75c5337735a6ef32ace0ffb6506ef49e5aefe870ffd72b1bb080f4843c217.bn.png)

এই পাঠে, আপনি অনুপাত ভিজ্যুয়ালাইজ করার তিনটি উপায় শিখেছেন। প্রথমে, আপনাকে আপনার ডেটাকে ক্যাটাগরিতে গ্রুপ করতে হবে এবং তারপর সিদ্ধান্ত নিতে হবে কোনটি ডেটা প্রদর্শনের সেরা উপায় - পাই, ডোনাট, বা ওয়াফল। সবগুলোই মজাদার এবং ব্যবহারকারীকে একটি ডেটাসেটের তাৎক্ষণিক স্ন্যাপশট প্রদান করে।

## 🚀 চ্যালেঞ্জ

এই মজাদার চার্টগুলো [Charticulator](https://charticulator.com) এ পুনরায় তৈরি করার চেষ্টা করুন।
## [পাঠ-পরবর্তী কুইজ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## পর্যালোচনা ও স্ব-অধ্যয়ন

কখন পাই, ডোনাট, বা ওয়াফল চার্ট ব্যবহার করতে হবে তা কখনও কখনও স্পষ্ট নয়। এই বিষয়ে পড়ার জন্য কিছু নিবন্ধ এখানে দেওয়া হলো:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

এই কঠিন সিদ্ধান্ত সম্পর্কে আরও তথ্য পেতে কিছু গবেষণা করুন।

## অ্যাসাইনমেন্ট

[Excel-এ চেষ্টা করুন](assignment.md)

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিক অনুবাদের চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। নথিটির মূল ভাষায় লেখা সংস্করণটিকেই প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ ব্যবহার করার পরামর্শ দেওয়া হচ্ছে। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।