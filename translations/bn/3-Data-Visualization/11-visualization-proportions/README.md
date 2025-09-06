<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "42119bcc97bee88254e381156d770f3c",
  "translation_date": "2025-09-06T07:13:40+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "bn"
}
-->
# অনুপাতের ভিজ্যুয়ালাইজেশন

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|অনুপাতের ভিজ্যুয়ালাইজেশন - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

এই পাঠে, আপনি একটি প্রকৃতি-কেন্দ্রিক ডেটাসেট ব্যবহার করে অনুপাতের ভিজ্যুয়ালাইজেশন করবেন, যেমন একটি মাশরুম সম্পর্কিত ডেটাসেটে বিভিন্ন ধরনের ছত্রাকের সংখ্যা। আসুন এই চমৎকার ছত্রাকগুলো অন্বেষণ করি, যা Audubon থেকে সংগৃহীত একটি ডেটাসেট ব্যবহার করে Agaricus এবং Lepiota পরিবারের ২৩ প্রজাতির গিল্ড মাশরুমের বিবরণ প্রদান করে। আপনি নিম্নলিখিত আকর্ষণীয় ভিজ্যুয়ালাইজেশন নিয়ে পরীক্ষা করবেন:

- পাই চার্ট 🥧
- ডোনাট চার্ট 🍩
- ওয়াফেল চার্ট 🧇

> 💡 Microsoft Research-এর একটি খুব আকর্ষণীয় প্রকল্প [Charticulator](https://charticulator.com) একটি বিনামূল্যের ড্র্যাগ এবং ড্রপ ইন্টারফেস প্রদান করে ডেটা ভিজ্যুয়ালাইজেশনের জন্য। তাদের একটি টিউটোরিয়ালে তারা এই মাশরুম ডেটাসেটও ব্যবহার করে! তাই আপনি ডেটা অন্বেষণ করতে পারেন এবং একই সময়ে লাইব্রেরি শিখতে পারেন: [Charticulator tutorial](https://charticulator.com/tutorials/tutorial4.html)।

## [পাঠ-পূর্ব কুইজ](https://ff-quizzes.netlify.app/en/ds/quiz/20)

## আপনার মাশরুম সম্পর্কে জানুন 🍄

মাশরুম খুবই আকর্ষণীয়। আসুন একটি ডেটাসেট আমদানি করে এগুলো অধ্যয়ন করি:

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```
একটি টেবিল প্রিন্ট করা হয়েছে যা বিশ্লেষণের জন্য চমৎকার ডেটা প্রদান করে:


| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Poisonous | Convex    | Smooth      | Brown     | Bruises | Pungent | Free            | Close        | Narrow    | Black      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |
| Edible    | Convex    | Smooth      | Yellow    | Bruises | Almond  | Free            | Close        | Broad     | Black      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Grasses |
| Edible    | Bell      | Smooth      | White     | Bruises | Anise   | Free            | Close        | Broad     | Brown      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Meadows |
| Poisonous | Convex    | Scaly       | White     | Bruises | Pungent | Free            | Close        | Narrow    | Brown      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |

প্রথমেই, আপনি লক্ষ্য করবেন যে সমস্ত ডেটা টেক্সট আকারে রয়েছে। এই ডেটাকে চার্টে ব্যবহার করার জন্য আপনাকে এটি রূপান্তর করতে হবে। প্রকৃতপক্ষে, বেশিরভাগ ডেটা একটি অবজেক্ট হিসেবে উপস্থাপিত হয়েছে:

```python
print(mushrooms.select_dtypes(["object"]).columns)
```

আউটপুট হলো:

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```
এই ডেটা নিন এবং 'class' কলামকে একটি ক্যাটাগরিতে রূপান্তর করুন:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```

এখন, যদি আপনি মাশরুম ডেটা প্রিন্ট করেন, আপনি দেখতে পাবেন যে এটি বিষাক্ত/খাদ্যযোগ্য শ্রেণী অনুযায়ী ক্যাটাগরিতে গ্রুপ করা হয়েছে:


|           | cap-shape | cap-surface | cap-color | bruises | odor | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | ... | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ---- | --------------- | ------------ | --------- | ---------- | ----------- | --- | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| class     |           |             |           |         |      |                 |              |           |            |             |     |                          |                        |                        |           |            |             |           |                   |            |         |
| Edible    | 4208      | 4208        | 4208      | 4208    | 4208 | 4208            | 4208         | 4208      | 4208       | 4208        | ... | 4208                     | 4208                   | 4208                   | 4208      | 4208       | 4208        | 4208      | 4208              | 4208       | 4208    |
| Poisonous | 3916      | 3916        | 3916      | 3916    | 3916 | 3916            | 3916         | 3916      | 3916       | 3916        | ... | 3916                     | 3916                   | 3916                   | 3916      | 3916       | 3916        | 3916      | 3916              | 3916       | 3916    |

যদি আপনি এই টেবিলে প্রদত্ত ক্রম অনুসরণ করে আপনার শ্রেণী ক্যাটাগরি লেবেল তৈরি করেন, তাহলে আপনি একটি পাই চার্ট তৈরি করতে পারবেন:

## পাই!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```
দেখুন, একটি পাই চার্ট যা এই ডেটার অনুপাত দেখাচ্ছে মাশরুমের এই দুই শ্রেণী অনুযায়ী। এখানে লেবেলের ক্রম সঠিকভাবে পাওয়া খুবই গুরুত্বপূর্ণ, তাই নিশ্চিত করুন যে লেবেল অ্যারে তৈরি করার ক্রমটি যাচাই করেছেন!

![pie chart](../../../../3-Data-Visualization/11-visualization-proportions/images/pie1-wb.png)

## ডোনাট!

একটি কিছুটা বেশি আকর্ষণীয় পাই চার্ট হলো ডোনাট চার্ট, যা একটি পাই চার্টের মাঝখানে একটি গর্ত থাকে। আসুন এই পদ্ধতি ব্যবহার করে আমাদের ডেটা দেখি।

মাশরুমের বিভিন্ন আবাসস্থল দেখুন:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```
এখানে, আপনি আপনার ডেটাকে আবাসস্থল অনুযায়ী গ্রুপ করছেন। ৭টি তালিকাভুক্ত রয়েছে, তাই আপনার ডোনাট চার্টের জন্য সেগুলোকে লেবেল হিসেবে ব্যবহার করুন:

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

![donut chart](../../../../3-Data-Visualization/11-visualization-proportions/images/donut-wb.png)

এই কোডটি একটি চার্ট এবং একটি কেন্দ্র বৃত্ত আঁকে, তারপর সেই কেন্দ্র বৃত্তটি চার্টে যোগ করে। কেন্দ্র বৃত্তের প্রস্থ পরিবর্তন করতে `0.40`-কে অন্য মানে পরিবর্তন করুন।

ডোনাট চার্ট বিভিন্নভাবে পরিবর্তন করা যায় লেবেল পরিবর্তনের জন্য। বিশেষ করে লেবেলগুলোকে পড়ার সুবিধার্থে হাইলাইট করা যায়। আরও জানুন [ডকুমেন্টেশন](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut) থেকে।

এখন আপনি জানেন কিভাবে আপনার ডেটাকে গ্রুপ করতে হয় এবং তারপর এটি পাই বা ডোনাট হিসেবে প্রদর্শন করতে হয়, আপনি অন্যান্য ধরনের চার্ট অন্বেষণ করতে পারেন। একটি ওয়াফেল চার্ট চেষ্টা করুন, যা পরিমাণ অন্বেষণের একটি ভিন্ন উপায়।

## ওয়াফেল!

একটি 'ওয়াফেল' টাইপ চার্ট হলো একটি ২D স্কোয়ার অ্যারের মাধ্যমে পরিমাণের ভিজ্যুয়ালাইজেশনের একটি ভিন্ন উপায়। এই ডেটাসেটে মাশরুমের ক্যাপ রঙের বিভিন্ন পরিমাণ দেখানোর চেষ্টা করুন। এটি করতে, আপনাকে একটি সহায়ক লাইব্রেরি [PyWaffle](https://pypi.org/project/pywaffle/) ইনস্টল করতে হবে এবং Matplotlib ব্যবহার করতে হবে:

```python
pip install pywaffle
```

আপনার ডেটার একটি অংশ নির্বাচন করুন গ্রুপ করার জন্য:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```

লেবেল তৈরি করে এবং তারপর আপনার ডেটাকে গ্রুপ করে একটি ওয়াফেল চার্ট তৈরি করুন:

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

একটি ওয়াফেল চার্ট ব্যবহার করে, আপনি স্পষ্টভাবে এই মাশরুম ডেটাসেটের ক্যাপ রঙের অনুপাত দেখতে পারেন। মজার বিষয় হলো, অনেক সবুজ ক্যাপযুক্ত মাশরুম রয়েছে!

![waffle chart](../../../../3-Data-Visualization/11-visualization-proportions/images/waffle.png)

✅ Pywaffle [Font Awesome](https://fontawesome.com/) থেকে উপলব্ধ যেকোনো আইকন ব্যবহার করে চার্টে আইকন সমর্থন করে। স্কোয়ারের পরিবর্তে আইকন ব্যবহার করে আরও আকর্ষণীয় ওয়াফেল চার্ট তৈরি করতে কিছু পরীক্ষা করুন।

এই পাঠে, আপনি অনুপাতের ভিজ্যুয়ালাইজেশনের তিনটি উপায় শিখেছেন। প্রথমে, আপনাকে আপনার ডেটাকে ক্যাটাগরিতে গ্রুপ করতে হবে এবং তারপর সিদ্ধান্ত নিতে হবে কোনটি ডেটা প্রদর্শনের সেরা উপায় - পাই, ডোনাট, বা ওয়াফেল। সবগুলোই সুস্বাদু এবং ব্যবহারকারীকে একটি ডেটাসেটের তাৎক্ষণিক স্ন্যাপশট প্রদান করে।

## 🚀 চ্যালেঞ্জ

এই সুস্বাদু চার্টগুলো [Charticulator](https://charticulator.com) এ পুনরায় তৈরি করার চেষ্টা করুন।
## [পাঠ-পরবর্তী কুইজ](https://ff-quizzes.netlify.app/en/ds/quiz/21)

## পর্যালোচনা ও স্ব-অধ্যয়ন

কখন পাই, ডোনাট, বা ওয়াফেল চার্ট ব্যবহার করতে হবে তা কখনও কখনও স্পষ্ট নয়। এই বিষয়ে পড়ার জন্য কিছু নিবন্ধ এখানে দেওয়া হলো:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

আরও তথ্য খুঁজে বের করতে কিছু গবেষণা করুন এই কঠিন সিদ্ধান্ত সম্পর্কে।

## অ্যাসাইনমেন্ট

[Excel-এ চেষ্টা করুন](assignment.md)

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিক অনুবাদ প্রদানের চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা তার জন্য দায়ী থাকব না।