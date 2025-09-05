<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "57f7db1f4c3ae3361c1d1fbafcdd690c",
  "translation_date": "2025-09-05T05:12:51+00:00",
  "source_file": "2-Working-With-Data/07-python/README.md",
  "language_code": "my"
}
-->
# ဒေတာနှင့်အလုပ်လုပ်ခြင်း: Python နှင့် Pandas Library

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/07-WorkWithPython.png) |
| :-------------------------------------------------------------------------------------------------------: |
|                 Python နှင့်အလုပ်လုပ်ခြင်း - _Sketchnote by [@nitya](https://twitter.com/nitya)_                 |

[![Intro Video](../../../../2-Working-With-Data/07-python/images/video-ds-python.png)](https://youtu.be/dZjWOGbsN4Y)

ဒေတာများကို သိမ်းဆည်းရန်နှင့် query languages အသုံးပြု၍ ရှာဖွေရန်အတွက် databases သည် အလွန်ထိရောက်သောနည်းလမ်းများပေးနိုင်သော်လည်း၊ ဒေတာကို ကိုယ်တိုင်ရေးသားထားသော program ဖြင့် ပြုပြင်ရန်သည် အလွန် flexible ဖြစ်သည်။ အချို့သောအခြေအနေများတွင် database query သည် ပိုထိရောက်နိုင်သော်လည်း၊ SQL ဖြင့် လွယ်ကူစွာလုပ်ဆောင်၍မရသော အဆင့်မြင့်ဒေတာလုပ်ငန်းများအတွက် program ရေးသားရန်လိုအပ်နိုင်သည်။  
ဒေတာလုပ်ငန်းများကို programming language မည်သည့်အမျိုးအစားဖြင့်မဆို ရေးသားနိုင်သော်လည်း၊ ဒေတာနှင့်အလုပ်လုပ်ရန်အတွက် အဆင့်မြင့်သော programming languages ရှိသည်။ ဒေတာသိပ္ပံပညာရှင်များသည် အောက်ပါဘာသာစကားများကို အများအားဖြင့်နှစ်သက်ကြသည်-

* **[Python](https://www.python.org/)** - အထွေထွေရည်ရွယ်ချက် programming language ဖြစ်ပြီး၊ ရိုးရှင်းမှုကြောင့် beginner များအတွက် အကောင်းဆုံးရွေးချယ်မှုတစ်ခုအဖြစ်အများအားဖြင့် သတ်မှတ်ထားသည်။ Python တွင် ZIP archive မှ ဒေတာထုတ်ယူခြင်း၊ သို့မဟုတ် ပုံကို grayscale သို့ပြောင်းခြင်းကဲ့သို့သော အများအပြားသော အကူအညီပေးနိုင်သော libraries များပါဝင်သည်။ ဒေတာသိပ္ပံအပြင် Python ကို web development အတွက်လည်း အသုံးပြုကြသည်။
* **[R](https://www.r-project.org/)** - စာရင်းဇယားဒေတာလုပ်ငန်းများအတွက် ထုတ်လုပ်ထားသော traditional toolbox ဖြစ်သည်။ CRAN libraries များပါဝင်သောကြောင့် ဒေတာလုပ်ငန်းများအတွက် ရွေးချယ်ရန်ကောင်းသည်။ သို့သော် R သည် အထွေထွေရည်ရွယ်ချက် programming language မဟုတ်သည့်အပြင် ဒေတာသိပ္ပံနယ်ပယ်အပြင် အခြားနယ်ပယ်များတွင် ရှားပါးစွာအသုံးပြုသည်။
* **[Julia](https://julialang.org/)** - ဒေတာသိပ္ပံအတွက် အထူးထုတ်လုပ်ထားသော programming language ဖြစ်သည်။ Python ထက် performance ပိုကောင်းစေရန် ရည်ရွယ်ထားပြီး၊ သိပ္ပံလေ့လာမှုများအတွက် tool ကောင်းတစ်ခုဖြစ်သည်။

ဒီသင်ခန်းစာတွင် Python ကို အသုံးပြု၍ ရိုးရှင်းသော ဒေတာလုပ်ငန်းများကို အဓိကထားဆွေးနွေးမည်ဖြစ်သည်။ Python ဘာသာစကားနှင့် အခြေခံကျွမ်းကျင်မှုရှိသည်ဟုယူဆမည်။ Python ကို ပိုမိုနက်ရှိုင်းစွာလေ့လာလိုပါက အောက်ပါ resources များကို ရည်ညွှန်းနိုင်သည်-

* [Learn Python in a Fun Way with Turtle Graphics and Fractals](https://github.com/shwars/pycourse) - GitHub-based Python Programming အကျဉ်း course
* [Take your First Steps with Python](https://docs.microsoft.com/en-us/learn/paths/python-first-steps/?WT.mc_id=academic-77958-bethanycheum) Microsoft Learn တွင် Learning Path

ဒေတာသည် အမျိုးမျိုးသောပုံစံများဖြင့် ရှိနိုင်သည်။ ဒီသင်ခန်းစာတွင် **tabular data**, **text** နှင့် **images** ဆိုသည့် ဒေတာပုံစံ ၃ မျိုးကို ဆွေးနွေးမည်ဖြစ်သည်။

ဒေတာလုပ်ငန်းများနှင့်ပတ်သက်သော libraries အားလုံးကို အပြည့်အစုံမဖော်ပြဘဲ၊ အချို့သော ဥပမာများကိုသာ အဓိကထားဆွေးနွေးမည်ဖြစ်သည်။ ဒါက သင်ကို အဓိကအကြောင်းအရာကို နားလည်စေပြီး၊ လိုအပ်သောအခါတွင် သင့်ပြဿနာများအတွက် ဖြေရှင်းချက်များကို ရှာဖွေရန် နားလည်မှုရရှိစေမည်ဖြစ်သည်။

> **အရေးကြီးသောအကြံပေးချက်** - သင်မသိသော ဒေတာလုပ်ငန်းတစ်ခုကို လုပ်ဆောင်ရန်လိုအပ်ပါက၊ အင်တာနက်တွင် ရှာဖွေကြည့်ပါ။ [Stackoverflow](https://stackoverflow.com/) တွင် Python ဖြင့် အများအပြားသော ရိုးရှင်းသောလုပ်ငန်းများအတွက် အသုံးဝင်သော code sample များပါဝင်သည်။

## [Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/12)

## Tabular Data နှင့် Dataframes

Relational databases အကြောင်းပြောသောအခါတွင် သင်သည် tabular data ကို ရှိပြီးသားဖြစ်သည်။ ဒေတာများအများကြီးရှိပြီး၊ အမျိုးမျိုးသော tables များတွင် ချိတ်ဆက်ထားသောအခါ SQL ကို အသုံးပြု၍ အလုပ်လုပ်ရန် make sense ဖြစ်သည်။ သို့သော် အချို့သောအခြေအနေများတွင် table တစ်ခုရှိသော ဒေတာကို **နားလည်မှု** သို့မဟုတ် **insights** ရရှိရန်လိုအပ်သည်။ ဥပမာအားဖြင့် distribution, correlation between values စသည်ဖြင့်။ ဒေတာသိပ္ပံတွင် အများအားဖြင့် original data ကို transformation ပြုလုပ်ပြီး visualization လုပ်ရန်လိုအပ်သည်။ ဒီအဆင့် ၂ ခုကို Python ဖြင့် လွယ်ကူစွာလုပ်ဆောင်နိုင်သည်။

Python တွင် tabular data ကို handle လုပ်ရန် အထူးအသုံးဝင်သော libraries ၂ ခုရှိသည်-

* **[Pandas](https://pandas.pydata.org/)** - **Dataframes** ကို manipulate လုပ်ရန်အတွက် အသုံးပြုသည်။ Dataframes သည် relational tables နှင့် ဆင်တူသည်။ Named columns ရှိပြီး၊ rows, columns နှင့် dataframes အပေါ်တွင် အမျိုးမျိုးသောလုပ်ငန်းများကို လုပ်ဆောင်နိုင်သည်။
* **[Numpy](https://numpy.org/)** - **tensors** (multi-dimensional **arrays**) နှင့်အလုပ်လုပ်ရန် library ဖြစ်သည်။ Array သည် တူညီသော underlying type ရှိသော values များပါဝင်ပြီး၊ dataframe ထက် ရိုးရှင်းပြီး mathematical operations ပိုမိုလုပ်ဆောင်နိုင်သည်။

အထူးသိထားသင့်သော libraries အချို့လည်းရှိသည်-

* **[Matplotlib](https://matplotlib.org/)** - ဒေတာကို visualization လုပ်ရန်နှင့် graph များကို plot လုပ်ရန်အသုံးပြုသည်။
* **[SciPy](https://www.scipy.org/)** - probability နှင့် statistics အကြောင်းပြောသောအခါ တွေ့ရှိခဲ့သော additional scientific functions ပါဝင်သော library ဖြစ်သည်။

Python program ရဲ့အစမှာ libraries များကို import လုပ်ရန် typically အသုံးပြုသော code ကတော့:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import ... # you need to specify exact sub-packages that you need
``` 

Pandas သည် အခြေခံ concepts အချို့ကို အဓိကထားသည်။

### Series 

**Series** သည် list သို့မဟုတ် numpy array နှင့် ဆင်တူသော values များ၏ အစဉ်ဖြစ်သည်။ အဓိကကွာခြားချက်မှာ series တွင် **index** ပါဝင်ပြီး၊ series အပေါ်တွင် လုပ်ဆောင်သောအခါ (ဥပမာ- add လုပ်ခြင်း) index ကို အရေးထားသည်။ Index သည် list သို့မဟုတ် array မှ default အနေဖြင့် integer row number ဖြစ်နိုင်သလို၊ date interval ကဲ့သို့သော complex structure ဖြစ်နိုင်သည်။

> **Note**: Pandas code အချို့ကို notebook [`notebook.ipynb`](../../../../2-Working-With-Data/07-python/notebook.ipynb) တွင်ပါဝင်သည်။ ဤနေရာတွင် အချို့သောဥပမာများကို outline လုပ်ထားပြီး၊ notebook အပြည့်အစုံကို ကြည့်ရှုရန်လည်း ကြိုဆိုပါသည်။

ဥပမာအားဖြင့်- ice-cream spot ရဲ့ sales ကို analysis လုပ်လိုပါက၊ sales numbers (နေ့စဉ်ရောင်းချသော items အရေအတွက်) ကို series အဖြစ် generate လုပ်နိုင်သည်:

```python
start_date = "Jan 1, 2020"
end_date = "Mar 31, 2020"
idx = pd.date_range(start_date,end_date)
print(f"Length of index is {len(idx)}")
items_sold = pd.Series(np.random.randint(25,50,size=len(idx)),index=idx)
items_sold.plot()
```
![Time Series Plot](../../../../2-Working-With-Data/07-python/images/timeseries-1.png)

အပတ်စဉ်တွင် party များကျင်းပပြီး၊ party အတွက် ice-cream packs ၁၀ ခုကို ထပ်ယူသည်ဟုယူဆပါက၊ အပတ်အလိုက် index ဖြင့် series တစ်ခုကို ဖန်တီးနိုင်သည်:
```python
additional_items = pd.Series(10,index=pd.date_range(start_date,end_date,freq="W"))
```
series ၂ ခုကို ပေါင်းပြီး total number ရရှိသည်:
```python
total_items = items_sold.add(additional_items,fill_value=0)
total_items.plot()
```
![Time Series Plot](../../../../2-Working-With-Data/07-python/images/timeseries-2.png)

> **Note** - `total_items+additional_items` syntax ကို ရိုးရှင်းစွာအသုံးပြုခြင်းမဟုတ်ပါ။ ထို syntax ကို အသုံးပြုပါက `NaN` (*Not a Number*) values များကို ရရှိမည်ဖြစ်သည်။ ဒါဟာ `additional_items` series ရဲ့ index point အချို့တွင် missing values ရှိသောကြောင့်ဖြစ်ပြီး၊ `NaN` ကို ပေါင်းခြင်းသည် `NaN` ကိုပေးသည်။ ထို့ကြောင့် addition လုပ်သောအခါ `fill_value` parameter ကို သတ်မှတ်ရန်လိုအပ်သည်။

Time series တွင် **resample** လုပ်၍ time interval များကို ပြောင်းနိုင်သည်။ ဥပမာအားဖြင့်- monthly mean sales volume ကိုတွက်လိုပါက အောက်ပါ code ကို အသုံးပြုနိုင်သည်:
```python
monthly = total_items.resample("1M").mean()
ax = monthly.plot(kind='bar')
```
![Monthly Time Series Averages](../../../../2-Working-With-Data/07-python/images/timeseries-3.png)

### DataFrame

DataFrame သည် index တူညီသော series များ၏ collection ဖြစ်သည်။ Series များကို DataFrame အဖြစ်ပေါင်းစည်းနိုင်သည်:
```python
a = pd.Series(range(1,10))
b = pd.Series(["I","like","to","play","games","and","will","not","change"],index=range(0,9))
df = pd.DataFrame([a,b])
```
ဤသည်မှာ အောက်ပါ table ကို ဖန်တီးမည်ဖြစ်သည်:
|     | 0   | 1    | 2   | 3   | 4      | 5   | 6      | 7    | 8    |
| --- | --- | ---- | --- | --- | ------ | --- | ------ | ---- | ---- |
| 0   | 1   | 2    | 3   | 4   | 5      | 6   | 7      | 8    | 9    |
| 1   | I   | like | to  | use | Python | and | Pandas | very | much |

Series များကို columns အဖြစ်အသုံးပြုပြီး၊ dictionary အသုံးပြု၍ column names ကို သတ်မှတ်နိုင်သည်:
```python
df = pd.DataFrame({ 'A' : a, 'B' : b })
```
ဤသည်မှာ အောက်ပါ table ကိုရရှိမည်ဖြစ်သည်:

|     | A   | B      |
| --- | --- | ------ |
| 0   | 1   | I      |
| 1   | 2   | like   |
| 2   | 3   | to     |
| 3   | 4   | use    |
| 4   | 5   | Python |
| 5   | 6   | and    |
| 6   | 7   | Pandas |
| 7   | 8   | very   |
| 8   | 9   | much   |

**Note** - `.T` ကို အသုံးပြု၍ DataFrame ကို transpose လုပ်နိုင်သည်။ Transpose သည် rows နှင့် columns ကို ပြောင်းလဲခြင်းဖြစ်ပြီး၊ `rename` operation ကို အသုံးပြု၍ column names ကို ပြောင်းနိုင်သည်။

DataFrame အပေါ်တွင် လုပ်ဆောင်နိုင်သော အရေးကြီးသောလုပ်ငန်းများအချို့မှာ-

**Column selection** - Individual columns ကို `df['A']` ဖြင့် ရွေးနိုင်သည်။ Subset of columns ကို `df[['B','A']]` ဖြင့် DataFrame အခြားတစ်ခုအဖြစ် ရွေးနိုင်သည်။

**Filtering** - Row များကို criteria အပေါ်အခြေခံ၍ ရွေးနိုင်သည်။ ဥပမာအားဖြင့်- column `A` > 5 ဖြစ်သော rows များကို ရွေးရန် `df[df['A']>5]` ကို အသုံးပြုနိုင်သည်။

> **Note** - Filtering သည် boolean series ကို အသုံးပြုသည်။ Boolean series သည် expression `True` သို့မဟုတ် `False` ဖြစ်သည်ကို ပြသသည်။ Boolean series ကို index အဖြစ်အသုံးပြုသောအခါ DataFrame ရဲ့ subset rows ကို ပြန်ပေးသည်။ Python boolean expression များကို ရိုးရှင်းစွာအသုံးပြု၍မရပါ။ ဥပမာ- `df[df['A']>5 and df['A']<7]` မှားနေသည်။ `&` operation ကို boolean series အပေါ်တွင် အသုံးပြုရမည်။ ဥပမာ- `df[(df['A']>5) & (df['A']<7)]` (*brackets အရေးကြီးသည်*).

**Creating new computable columns** - DataFrame အတွက် computable columns အသစ်များကို ရိုးရှင်းသော expression ဖြင့် ဖန်တီးနိုင်သည်:
```python
df['DivA'] = df['A']-df['A'].mean() 
``` 
ဤဥပမာသည် column `A` ရဲ့ mean value မှ divergence ကိုတွက်ချက်သည်။ Series ကို left-hand-side တွင် assign လုပ်ပြီး column အသစ်ကို ဖန်တီးသည်။ Series နှင့်မကိုက်ညီသော operations များကို အသုံးပြု၍ column ဖန်တီး၍မရပါ။ ဥပမာ- အောက်ပါ code မှားနေသည်:
```python
# Wrong code -> df['ADescr'] = "Low" if df['A'] < 5 else "Hi"
df['LenB'] = len(df['B']) # <- Wrong result
``` 
Syntax မှန်သော်လည်း၊ column ရဲ့ individual elements ရဲ့ length မဟုတ်ဘဲ series `B` ရဲ့ length ကို assign လုပ်သည်။

Complex expressions တွက်ရန် `apply` function ကို အသုံးပြုနိုင်သည်။ အထက်ပါဥပမာကို အောက်ပါအတိုင်းရေးနိုင်သည်:
```python
df['LenB'] = df['B'].apply(lambda x : len(x))
# or 
df['LenB'] = df['B'].apply(len)
```

အထက်ပါ operations များပြီးနောက် DataFrame ရဲ့အခြေအနေမှာ-

|     | A   | B      | DivA | LenB |
| --- | --- | ------ | ---- | ---- |
| 0   | 1   | I      | -4.0 | 1    |
| 1   | 2   | like   | -3.0 | 4    |
| 2   | 3   | to     | -2.0 | 2    |
| 3   | 4   | use    | -1.0 | 3    |
| 4   | 5   | Python | 0.0  | 6    |
| 5   | 6   | and    | 1.0  | 3    |
| 6   | 7   | Pandas | 2.0  | 6    |
| 7   | 8   | very   | 3.0  | 4    |
| 8   | 9   | much   | 4.0  | 4    |

**Selecting rows based on numbers** - `iloc` ကို အသုံးပြု၍ rows များကို ရွေးနိုင်သည်။ ဥပမာ- DataFrame ရဲ့ rows ၅ ခုကို ရွေးရန်:
```python
df.iloc[:5]
```

**Grouping** - Excel ရဲ့ *pivot tables* ကဲ့သို့သောရလဒ်ရရန် အသုံးပြုသည်။ ဥပမာ- column `A` ရဲ့ mean value ကို `LenB` အပေါ်အခြေခံ၍တွက်လိုပါက DataFrame ကို `LenB` ဖြင့် group လုပ်ပြီး `mean` ကိုခေါ်နိုင်သည်:
```python
df.groupby(by='LenB').mean()
```
Mean နှင့် group ရဲ့ element အရေအတွက်ကိုတွက်လိုပါက `aggregate` function ကို အသုံးပြုနိုင်သည်:
```python
df.groupby(by='LenB') \
 .aggregate({ 'DivA' : len, 'A' : lambda x: x.mean() }) \
 .rename(columns={ 'DivA' : 'Count', 'A' : 'Mean'})
```
ဤသည်မှာ အောက်ပါ table ကိုရရှိမည်-

| LenB | Count | Mean     |
| ---- | ----- | -------- |
| 1    | 1     | 1.000000 |
| 2    | 1     | 3.000000 |
| 3    | 2     | 5.000000 |
| 4    | 3     | 6.333333 |
| 6    | 2     | 6.000000 |

### ဒေတာရယူခြင်း
Python object တွေကို သုံးပြီး Series နဲ့ DataFrame တွေကို ဖန်တီးတာ ဘယ်လောက်လွယ်ကူတယ်ဆိုတာကို ကြည့်ပြီးပါပြီ။ သို့သော် အချက်အလက်တွေဟာ အများအားဖြင့် text file သို့မဟုတ် Excel table အနေနဲ့ ရှိတတ်ပါတယ်။ ကံကောင်းစွာ Pandas က disk မှ အချက်အလက်တွေကို load လုပ်ဖို့ လွယ်ကူတဲ့နည်းလမ်းတစ်ခုကို ပေးထားပါတယ်။ ဥပမာအားဖြင့် CSV file ကို ဖတ်ဖို့အတွက် အောက်ပါနည်းလမ်းကို အသုံးပြုနိုင်ပါတယ်:  
```python
df = pd.read_csv('file.csv')
```  
"Challenge" အပိုင်းမှာ အခြားသော အချက်အလက်တွေကို load လုပ်နည်းနဲ့ အပြင်ဘက် website တွေကနေ fetch လုပ်နည်းကို ပိုမိုကြည့်ရှုနိုင်ပါမယ်။  

### Printing နဲ့ Plotting  

Data Scientist တစ်ဦးအနေနဲ့ အချက်အလက်တွေကို ရှာဖွေဖို့ လိုအပ်တတ်ပါတယ်၊ ဒါကြောင့် visualization လုပ်နိုင်ဖို့ အရေးကြီးပါတယ်။ DataFrame ကြီးတစ်ခုကို handle လုပ်တဲ့အခါမှာ အများအားဖြင့် ပထမဆုံးအတန်းတွေကို print လုပ်ပြီး အားလုံးကို မှန်ကန်စွာလုပ်နေတယ်လို့ သေချာစေချင်တတ်ပါတယ်။ ဒါကို `df.head()` ကို ခေါ်ပြီး လုပ်နိုင်ပါတယ်။ Jupyter Notebook မှာ run လုပ်ရင် DataFrame ကို tabular form လှပလှပနဲ့ ပြသပေးပါမယ်။  

`plot` function ကို သုံးပြီး column တချို့ကို visualize လုပ်နည်းကို ကြည့်ပြီးပါပြီ။ `plot` ဟာ အလုပ်အတော်များစွာအတွက် အသုံးဝင်ပြီး `kind=` parameter ကို သုံးပြီး graph အမျိုးအစားများစွာကို support လုပ်ပေးနိုင်ပါတယ်။ သို့သော် `matplotlib` library ကို သုံးပြီး ပိုမိုရှုပ်ထွေးတဲ့အရာတွေကို plot လုပ်နိုင်ပါတယ်။ Data visualization ကို အခြားသော course lesson တွေမှာ အသေးစိတ်လေ့လာပါမယ်။  

ဒီအကျဉ်းချုပ်မှာ Pandas ရဲ့ အရေးကြီးဆုံး concept တွေကို ဖော်ပြထားပါတယ်၊ သို့သော် library ဟာ အလွန်ချောမွေ့ပြီး မလုပ်နိုင်တဲ့အရာမရှိပါဘူး! အခုတော့ ဒီအတတ်ပညာကို သုံးပြီး အထူးပြဿနာတွေကို ဖြေရှင်းကြည့်ရအောင်။  

## 🚀 Challenge 1: COVID ပျံ့နှံ့မှုကို ခွဲခြမ်းစိတ်ဖြာခြင်း  

ပထမပြဿနာမှာ COVID-19 ရောဂါပျံ့နှံ့မှုကို မော်ဒယ်တစ်ခုအနေနဲ့ ဖော်ပြဖို့ အာရုံစိုက်ပါမယ်။ ဒါကိုလုပ်ဖို့အတွက် [Center for Systems Science and Engineering](https://systems.jhu.edu/) (CSSE) မှ [Johns Hopkins University](https://jhu.edu/) က ပေးထားတဲ့ အမျိုးသားအသီးသီးမှာ COVID-19 ရောဂါပိုးကူးခံရသူအရေအတွက်အချက်အလက်တွေကို အသုံးပြုပါမယ်။ Dataset ကို [GitHub Repository](https://github.com/CSSEGISandData/COVID-19) မှာ ရနိုင်ပါတယ်။  

အချက်အလက်တွေကို handle လုပ်နည်းကို ပြသဖို့ [`notebook-covidspread.ipynb`](../../../../2-Working-With-Data/07-python/notebook-covidspread.ipynb) ကို ဖွင့်ပြီး အပေါ်မှ အောက်အထိ ဖတ်ပါ။ Cell တွေကို run လုပ်နိုင်ပြီး အဆုံးမှာ ကျွန်တော်တို့ထားခဲ့တဲ့ challenge တွေကို လုပ်နိုင်ပါတယ်။  

![COVID Spread](../../../../2-Working-With-Data/07-python/images/covidspread.png)  

> Jupyter Notebook မှာ code run လုပ်နည်းကို မသိရင် [ဒီဆောင်းပါး](https://soshnikov.com/education/how-to-execute-notebooks-from-github/) ကို ကြည့်ပါ။  

## Unstructured Data နဲ့ အလုပ်လုပ်ခြင်း  

အချက်အလက်တွေဟာ tabular form နဲ့ ရှိတတ်ပေမယ့် တချို့အခါမှာ text သို့မဟုတ် image လို structured မဟုတ်တဲ့ အချက်အလက်တွေနဲ့ အလုပ်လုပ်ဖို့ လိုအပ်တတ်ပါတယ်။ ဒီအခါမှာ အပေါ်မှာ ပြထားတဲ့ data processing နည်းလမ်းတွေကို အသုံးပြုဖို့ structured data ကို **extract** လုပ်ဖို့ လိုအပ်ပါတယ်။ ဥပမာအချို့မှာ:  

* Text မှ keyword တွေကို extract လုပ်ပြီး keyword တွေ ဘယ်လောက်ကြိမ်တွေ့ရလဲဆိုတာ ကြည့်ရှုခြင်း  
* Neural network တွေကို သုံးပြီး ပုံထဲမှာ object တွေကို extract လုပ်ခြင်း  
* Video camera feed မှ လူတွေ့ရဲ့ အာရုံခံစားမှုကို သိရှိခြင်း  

## 🚀 Challenge 2: COVID Papers ကို ခွဲခြမ်းစိတ်ဖြာခြင်း  

ဒီ challenge မှာ COVID pandemic နဲ့ ဆက်စပ်တဲ့ သိပ္ပံစာတမ်းတွေကို process လုပ်ဖို့ အာရုံစိုက်ပါမယ်။ [CORD-19 Dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) မှာ metadata နဲ့ abstract တွေပါဝင်တဲ့ COVID အကြောင်းစာတမ်း 7000 ကျော် (ရေးသားချိန်အတိုင်း) ရနိုင်ပါတယ်။  

[Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health/?WT.mc_id=academic-77958-bethanycheum) cognitive service ကို အသုံးပြုပြီး dataset ကို ခွဲခြမ်းစိတ်ဖြာနည်းကို [ဒီ blog post](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) မှာ ပြထားပါတယ်။ ကျွန်တော်တို့ ဒီ analysis ရဲ့ ရိုးရှင်းတဲ့ version ကို ဆွေးနွေးပါမယ်။  

> **NOTE**: Dataset ကို repository မှာ မပါဝင်ပေးထားပါဘူး။ [Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge?select=metadata.csv) မှာ [`metadata.csv`](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge?select=metadata.csv) ကို download လုပ်ဖို့လိုအပ်နိုင်ပါတယ်။ Kaggle မှာ registration လုပ်ဖို့လိုအပ်နိုင်ပါတယ်။ [ဒီနေရာ](https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases.html) မှာ registration မလိုအပ်ဘဲ dataset ကို download လုပ်နိုင်ပါတယ်၊ ဒါပေမယ့် metadata file အပြင် full text တွေပါဝင်ပါမယ်။  

[`notebook-papers.ipynb`](../../../../2-Working-With-Data/07-python/notebook-papers.ipynb) ကို ဖွင့်ပြီး အပေါ်မှ အောက်အထိ ဖတ်ပါ။ Cell တွေကို run လုပ်နိုင်ပြီး အဆုံးမှာ ကျွန်တော်တို့ထားခဲ့တဲ့ challenge တွေကို လုပ်နိုင်ပါတယ်။  

![Covid Medical Treatment](../../../../2-Working-With-Data/07-python/images/covidtreat.png)  

## Image Data ကို Process လုပ်ခြင်း  

လတ်တလောမှာ ပုံတွေကို နားလည်နိုင်တဲ့ အလွန်အစွမ်းထက်တဲ့ AI model တွေ ဖွံ့ဖြိုးလာပါတယ်။ Pre-trained neural network တွေ သို့မဟုတ် cloud service တွေကို အသုံးပြုပြီး အလုပ်အမျိုးမျိုးကို ဖြေရှင်းနိုင်ပါတယ်။ ဥပမာအချို့မှာ:  

* **Image Classification** - ပုံကို pre-defined class တစ်ခုမှာ categorize လုပ်နိုင်ပါတယ်။ [Custom Vision](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/?WT.mc_id=academic-77958-bethanycheum) ကို သုံးပြီး ကိုယ်ပိုင် image classifier တွေကို လွယ်ကူစွာ train လုပ်နိုင်ပါတယ်။  
* **Object Detection** - ပုံထဲမှာ object တွေကို detect လုပ်နိုင်ပါတယ်။ [computer vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/?WT.mc_id=academic-77958-bethanycheum) က အများအားဖြင့် common object တွေကို detect လုပ်နိုင်ပြီး [Custom Vision](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/?WT.mc_id=academic-77958-bethanycheum) ကို သုံးပြီး အထူး object တွေကို detect လုပ်နိုင်ပါတယ်။  
* **Face Detection** - အသက်၊ ကျား/မ၊ အာရုံခံစားမှု detection ပါဝင်ပါတယ်။ [Face API](https://azure.microsoft.com/services/cognitive-services/face/?WT.mc_id=academic-77958-bethanycheum) ကို အသုံးပြုနိုင်ပါတယ်။  

Python SDK တွေကို သုံးပြီး cloud service တွေကို ခေါ်နိုင်ပြီး data exploration workflow မှာ အလွယ်တကူ ထည့်သွင်းနိုင်ပါတယ်။  

Image data source တွေကို explore လုပ်နည်း ဥပမာအချို့:  
* [How to Learn Data Science without Coding](https://soshnikov.com/azure/how-to-learn-data-science-without-coding/) blog post မှာ Instagram ပုံတွေကို explore လုပ်ပြီး ပုံတစ်ပုံကို ဘယ်လိုလူတွေက ပိုပြီး like လုပ်တယ်ဆိုတာကို နားလည်ဖို့ ကြိုးစားပါတယ်။ [computer vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/?WT.mc_id=academic-77958-bethanycheum) ကို သုံးပြီး ပုံတွေကနေ အချက်အလက်တွေကို extract လုပ်ပြီး [Azure Machine Learning AutoML](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml/?WT.mc_id=academic-77958-bethanycheum) ကို သုံးပြီး interpretable model တစ်ခုကို တည်ဆောက်ပါတယ်။  
* [Facial Studies Workshop](https://github.com/CloudAdvocacy/FaceStudies) မှာ [Face API](https://azure.microsoft.com/services/cognitive-services/face/?WT.mc_id=academic-77958-bethanycheum) ကို သုံးပြီး ပုံထဲမှာ လူတွေ့ရဲ့ အာရုံခံစားမှုကို extract လုပ်ပြီး လူတွေကို ပျော်ရွှင်စေတဲ့အရာကို နားလည်ဖို့ ကြိုးစားပါတယ်။  

## နိဂုံး  

Structured data သို့မဟုတ် unstructured data ရှိပါက Python ကို သုံးပြီး data processing နဲ့ နားလည်မှုနဲ့ ပတ်သက်တဲ့ အဆင့်အားလုံးကို လုပ်ဆောင်နိုင်ပါတယ်။ Python ဟာ data processing အတွက် အ flexibilty အများဆုံးနည်းလမ်းဖြစ်ပြီး data scientist အများစုက Python ကို အဓိက tool အနေနဲ့ အသုံးပြုကြပါတယ်။ Data science journey ကို အလေးထားပြီး လေ့လာချင်ရင် Python ကို အနက်အနက် လေ့လာဖို့ အကြံပေးပါတယ်!  

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/)  

## Review & Self Study  

**Books**  
* [Wes McKinney. Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython](https://www.amazon.com/gp/product/1491957662)  

**Online Resources**  
* Official [10 minutes to Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) tutorial  
* [Documentation on Pandas Visualization](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)  

**Learning Python**  
* [Learn Python in a Fun Way with Turtle Graphics and Fractals](https://github.com/shwars/pycourse)  
* [Take your First Steps with Python](https://docs.microsoft.com/learn/paths/python-first-steps/?WT.mc_id=academic-77958-bethanycheum) Learning Path on [Microsoft Learn](http://learn.microsoft.com/?WT.mc_id=academic-77958-bethanycheum)  

## Assignment  

[Perform more detailed data study for the challenges above](assignment.md)  

## Credits  

ဒီ lesson ကို [Dmitry Soshnikov](http://soshnikov.com) မှ ♥️ နဲ့ ရေးသားထားပါတယ်။  

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။