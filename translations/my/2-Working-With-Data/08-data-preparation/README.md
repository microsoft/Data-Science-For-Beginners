<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1b560955ff39a2bcf2a049fce474a951",
  "translation_date": "2025-09-05T20:13:04+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "my"
}
-->
# ဒေတာနှင့်အလုပ်လုပ်ခြင်း: ဒေတာပြင်ဆင်ခြင်း

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|ဒေတာပြင်ဆင်ခြင်း - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Pre-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/14)

ဒေတာရင်းမြစ်ပေါ်မူတည်ပြီး၊ အစွန်းရောက်မညီညွတ်မှုများပါဝင်နိုင်ပြီး၊ ဒါဟာခွဲခြမ်းစိတ်ဖြာခြင်းနှင့်မော်ဒယ်တည်ဆောက်ခြင်းတွင်အခက်အခဲများဖြစ်စေပါသည်။ အခြားနည်းဖြင့်၊ ဒီဒေတာကို "ညစ်ပတ်" ဟုခေါ်နိုင်ပြီး၊ သန့်ရှင်းစေရန်လိုအပ်ပါသည်။ ဒီသင်ခန်းစာမှာ မရှိသော၊ မမှန်သော၊ မပြည့်စုံသောဒေတာများကို ကိုင်တွယ်နိုင်ရန် သန့်ရှင်းရေးနှင့် ပြောင်းလဲခြင်းနည်းလမ်းများကို အဓိကထားပါသည်။ Python နှင့် Pandas library ကိုအသုံးပြုပြီး၊ ဒီ directory ထဲမှာ [notebook](../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb) မှာ ပြသထားသောနည်းလမ်းများကိုလေ့လာပါမည်။

## ဒေတာသန့်ရှင်းရေး၏အရေးပါမှု

- **အသုံးပြုရလွယ်ကူမှုနှင့် ပြန်လည်အသုံးပြုနိုင်မှု**: ဒေတာကို သေချာစွာစီစဉ်ပြီး ပုံမှန်အခြေအနေဖြစ်စေပါက ရှာဖွေခြင်း၊ အသုံးပြုခြင်းနှင့် အခြားသူများနှင့်မျှဝေခြင်းမှာ ပိုမိုလွယ်ကူပါသည်။

- **ညီညွတ်မှု**: ဒေတာသိပ္ပံမှာ မတူညီတဲ့ရင်းမြစ်များမှ ဒေတာများကိုပေါင်းစည်းရသောအခါ၊ တစ်ခုချင်းစီမှာပုံမှန်စံချိန်စံညွှန်းရှိစေရန်လိုအပ်ပါသည်။ ဒါဟာ ဒေတာများကိုပေါင်းစည်းပြီး dataset တစ်ခုအဖြစ်အသုံးပြုတဲ့အခါမှာ အသုံးဝင်မှုရှိစေပါသည်။

- **မော်ဒယ်တိကျမှု**: သန့်ရှင်းထားသောဒေတာသည် မော်ဒယ်များ၏တိကျမှုကိုတိုးတက်စေပါသည်။

## သန့်ရှင်းရေးရည်မှန်းချက်များနှင့်နည်းလမ်းများ

- **ဒေတာကိုလေ့လာခြင်း**: [နောက်ဆုံးသင်ခန်းစာ](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing) မှာဖော်ပြထားသော ဒေတာလေ့လာခြင်းသည် သန့်ရှင်းရေးလိုအပ်သောဒေတာကိုရှာဖွေစေပါသည်။ ဒေတာကိုမြင်သာစွာကြည့်ရှုခြင်းသည် အခြားအပိုင်းများ၏ပုံစံကိုခန့်မှန်းနိုင်စေပြီး၊ ဖြေရှင်းနိုင်သောပြဿနာများကိုအကြံပေးနိုင်ပါသည်။ ဒေတာလေ့လာခြင်းမှာ မေးခွန်းထုတ်ခြင်း၊ visualization နှင့် sampling ပါဝင်နိုင်ပါသည်။

- **ပုံစံချိန်ညှိခြင်း**: ဒေတာရင်းမြစ်ပေါ်မူတည်ပြီး၊ ပုံစံမညီညွတ်မှုများရှိနိုင်ပါသည်။ ဒါဟာ visualization သို့မဟုတ် query ရလဒ်များတွင်မှန်ကန်စွာဖော်ပြမရသောပြဿနာများကိုဖြစ်စေပါသည်။ ပုံစံပြဿနာများကို whitespace, date, data type စသည်ဖြင့်ဖြေရှင်းရပါမည်။ 

- **ထပ်နေသောဒေတာများ**: ထပ်နေသောဒေတာများသည် မမှန်ကန်သောရလဒ်များကိုဖြစ်စေပြီး၊ ပုံမှန်အားဖြင့်ဖယ်ရှားရပါသည်။ ဒါဟာ datasets များကိုပေါင်းစည်းတဲ့အခါမှာဖြစ်နိုင်ပါတယ်။ 

- **မရှိသောဒေတာများ**: မရှိသောဒေတာများသည် မမှန်ကန်သောရလဒ်များနှင့် bias ဖြစ်စေနိုင်ပါသည်။ ဒါကို reload, computation, code သို့မဟုတ် ဖယ်ရှားခြင်းဖြင့်ဖြေရှင်းနိုင်ပါသည်။

## DataFrame အချက်အလက်များကိုလေ့လာခြင်း
> **သင်ယူရည်မှန်းချက်**: ဒီအပိုင်းအဆုံးမှာ pandas DataFrames ထဲမှာရှိတဲ့ဒေတာအကြောင်းကိုရှာဖွေတတ်စေပါမည်။

Pandas မှာဒေတာကို DataFrame အဖြစ်သိမ်းဆည်းထားပြီး၊ 60,000 rows နှင့် 400 columns ရှိတဲ့ DataFrame ကိုဘယ်လိုစတင်လေ့လာရမလဲ? [pandas](https://pandas.pydata.org/) မှာ DataFrame အကြောင်းကိုမြန်ဆန်စွာကြည့်ရှုနိုင်တဲ့ tools တွေရှိပါတယ်။

ဒီ functionality ကိုလေ့လာဖို့ Python scikit-learn library ကို import လုပ်ပြီး **Iris data set** ကိုအသုံးပြုပါမည်။

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

- **DataFrame.info**: `info()` method ကိုအသုံးပြုပြီး DataFrame ထဲမှာရှိတဲ့ content အကြောင်းကို summary အနေနဲ့ကြည့်ရှုနိုင်ပါတယ်။
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
ဒီမှာ *Iris* dataset မှာ 150 entries ရှိပြီး၊ null entries မရှိပါဘူး။ ဒေတာအားလုံးကို 64-bit floating-point numbers အဖြစ်သိမ်းဆည်းထားပါတယ်။

- **DataFrame.head()**: `head()` method ကိုအသုံးပြုပြီး DataFrame ရဲ့ပထမဆုံး rows တွေကိုကြည့်ရှုနိုင်ပါတယ်။
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
- **DataFrame.tail()**: `tail()` method ကိုအသုံးပြုပြီး DataFrame ရဲ့နောက်ဆုံး rows တွေကိုကြည့်ရှုနိုင်ပါတယ်။
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
> **Takeaway:** DataFrame ရဲ့ metadata, ပထမဆုံး rows, နောက်ဆုံး rows တွေကိုကြည့်ရှုခြင်းအားဖြင့် ဒေတာရဲ့အရွယ်အစား၊ ပုံစံ၊ အကြောင်းအရာကိုမြန်ဆန်စွာနားလည်နိုင်ပါတယ်။

## မရှိသောဒေတာကိုကိုင်တွယ်ခြင်း
> **သင်ယူရည်မှန်းချက်**: ဒီအပိုင်းအဆုံးမှာ DataFrames ထဲက null values တွေကိုအစားထိုးခြင်း သို့မဟုတ် ဖယ်ရှားခြင်းကိုသိရှိနိုင်ပါမည်။

Dataset များမှာ မရှိသောဒေတာများပါဝင်နိုင်ပါတယ်။ ဒေတာကိုဘယ်လိုကိုင်တွယ်မလဲဆိုတာက analysis နှင့်ရလဒ်များကိုအကျိုးသက်ရောက်စေပါသည်။

Pandas မှာ missing values တွေကို `NaN` (Not a Number) နှင့် Python `None` object ကိုအသုံးပြုပါတယ်။ 

- **Detecting null values**: `pandas` မှာ `isnull()` နှင့် `notnull()` methods တွေကို null data ကိုရှာဖွေဖို့အသုံးပြုနိုင်ပါတယ်။
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

> **Takeaway**: `isnull()` နှင့် `notnull()` methods တွေက Boolean masks ကိုပြသပြီး၊ ဒေတာကိုကိုင်တွယ်တဲ့အခါမှာအထောက်အကူဖြစ်စေပါတယ်။

- **Dropping null values**: Null values တွေကိုဖယ်ရှားဖို့ pandas မှာ `dropna()` method ကိုအသုံးပြုနိုင်ပါတယ်။
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```

DataFrame မှာ rows သို့မဟုတ် columns တစ်ခုလုံးကိုဖယ်ရှားရပါမည်။
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

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```

Columns ကိုဖယ်ရှားဖို့ `axis=1` ကိုအသုံးပြုပါ:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```

`how` နှင့် `thresh` parameters ကိုအသုံးပြုပြီး null values တွေကိုပိုမိုထိန်းချုပ်နိုင်ပါတယ်။
```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```

- **Filling null values**: Null values တွေကို valid values တွေနဲ့အစားထိုးဖို့ `fillna` method ကိုအသုံးပြုနိုင်ပါတယ်။
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

Null values တွေကို single value (ဥပမာ `0`) နဲ့အစားထိုးနိုင်ပါတယ်:
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

**Forward-fill** method ကိုအသုံးပြုပြီး null values တွေကိုအစားထိုးနိုင်ပါတယ်:
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

**Back-fill** method ကိုအသုံးပြုပြီး null values တွေကိုအစားထိုးနိုင်ပါတယ်:
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

DataFrame တွေမှာ axis ကိုသတ်မှတ်ပြီး null values တွေကိုအစားထိုးနိုင်ပါတယ်။
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```

Forward-fill method မှာ null value အနီးမှာ valid value မရှိရင် null value ကိုမပြောင်းလဲပါ။
> **အရေးကြီးချက်:** သင့်ဒေတာစနစ်များတွင် ပျောက်ဆုံးနေသောတန်ဖိုးများကို ကိုင်တွယ်ရန် နည်းလမ်းများစွာရှိသည်။ သင့်အသုံးပြုမည့် အထူးနည်းလမ်း (ပျောက်ဆုံးနေသောတန်ဖိုးများကို ဖယ်ရှားခြင်း၊ အစားထိုးခြင်း၊ သို့မဟုတ် အစားထိုးပုံစံကို ရွေးချယ်ခြင်း) သည် အဆိုပါဒေတာ၏ အထူးသက်ဆိုင်မှုများအပေါ် မူတည်ရမည်ဖြစ်သည်။ ဒေတာစနစ်များကို ပိုမိုကိုင်တွယ်ပြီး အလုပ်လုပ်သည့်အခါ ပျောက်ဆုံးနေသောတန်ဖိုးများကို ကိုင်တွယ်ရန် ပိုမိုကောင်းမွန်သော အမြင်တစ်ခုကို ဖွံ့ဖြိုးလာမည်။
## အချက်အလက်များ ထပ်နေမှုကို ဖယ်ရှားခြင်း

> **သင်ယူရည်မှန်းချက်:** ဒီအခန်းငယ်ကို ပြီးဆုံးတဲ့အချိန်မှာ DataFrame တွေထဲက ထပ်နေတဲ့တန်ဖိုးတွေကို ရှာဖွေပြီး ဖယ်ရှားနိုင်ဖို့ အဆင်ပြေဖြစ်ရမယ်။

အချက်အလက်များ ပျောက်နေမှုအပြင်၊ အမှန်တကယ်ရှိတဲ့ dataset တွေမှာ အချက်အလက်တွေ ထပ်နေမှုကိုလည်း မကြာခဏတွေ့ရတတ်ပါတယ်။ ကံကောင်းစွာ `pandas` က ထပ်နေတဲ့ entry တွေကို ရှာဖွေပြီး ဖယ်ရှားဖို့ လွယ်ကူတဲ့နည်းလမ်းကို ပေးထားပါတယ်။

- **ထပ်နေမှုကို ရှာဖွေခြင်း: `duplicated`**: pandas ရဲ့ `duplicated` method ကို သုံးပြီး ထပ်နေတဲ့တန်ဖိုးတွေကို လွယ်လွယ်ကူကူ ရှာဖွေနိုင်ပါတယ်။ ဒီ method က Boolean mask ကို ပြန်ပေးပြီး DataFrame ထဲမှာ အရင်တစ်ခုနဲ့ ထပ်နေတဲ့ entry ဖြစ်မဖြစ်ကို ပြသပါတယ်။ ဒီကို လက်တွေ့ကြည့်ရှုနိုင်ဖို့ နောက်ထပ် DataFrame တစ်ခုကို ဖန်တီးကြည့်ရအောင်။
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
- **ထပ်နေမှုကို ဖယ်ရှားခြင်း: `drop_duplicates`:** `duplicated` value တွေ `False` ဖြစ်တဲ့ data ကိုသာ ပြန်ပေးတဲ့ copy ကို ရရှိစေပါတယ်။
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
`duplicated` နဲ့ `drop_duplicates` တို့က default အနေဖြင့် column အားလုံးကို စဉ်းစားပေမယ့် သင့် DataFrame ထဲက column အချို့ကိုသာ စဉ်းစားဖို့ သတ်မှတ်နိုင်ပါတယ်။
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **အရေးကြီးသော အချက်:** ထပ်နေတဲ့အချက်အလက်တွေကို ဖယ်ရှားခြင်းဟာ data-science project တစ်ခုစီမှာ မရှိမဖြစ် လိုအပ်တဲ့အပိုင်းဖြစ်ပါတယ်။ ထပ်နေတဲ့အချက်အလက်တွေက သင့် analysis ရလဒ်တွေကို ပြောင်းလဲစေပြီး မမှန်ကန်တဲ့ရလဒ်တွေကို ရရှိစေတတ်ပါတယ်။


## 🚀 စိန်ခေါ်မှု

ဒီအခန်းမှာ ပြောထားတဲ့ အကြောင်းအရာအားလုံးကို [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb) အနေနဲ့ ပေးထားပါတယ်။ ထို့အပြင် အခန်းတစ်ခုစီရဲ့ နောက်မှာ လေ့ကျင့်ခန်းတွေ ပါဝင်ပြီး၊ အဲဒီကို စမ်းကြည့်ပါ။

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/15)



## ပြန်လည်သုံးသပ်ခြင်းနှင့် ကိုယ်တိုင်လေ့လာခြင်း

သင့်အချက်အလက်တွေကို analysis နဲ့ modeling အတွက် ပြင်ဆင်ဖို့ နည်းလမ်းအမျိုးမျိုး ရှာဖွေပြီး ချဉ်းကပ်နိုင်ပါတယ်။ အချက်အလက်တွေကို သန့်စင်ဖို့ လုပ်ငန်းစဉ်က "လက်တွေ့လုပ်ဆောင်ရမယ့်" အတွေ့အကြုံတစ်ခုဖြစ်ပါတယ်။ ဒီသင်ခန်းစာမှာ မဖော်ပြထားတဲ့ နည်းလမ်းတွေကို ရှာဖွေဖို့ Kaggle ရဲ့ စိန်ခေါ်မှုတွေကို စမ်းကြည့်ပါ။

- [Data Cleaning Challenge: Parsing Dates](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Data Cleaning Challenge: Scale and Normalize Data](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## လုပ်ငန်းတာဝန်

[Evaluating Data from a Form](assignment.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူလဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် ရှုလေ့လာသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှု ဝန်ဆောင်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။