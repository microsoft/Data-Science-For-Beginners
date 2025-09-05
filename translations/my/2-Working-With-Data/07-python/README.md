<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "577a611517482c3ceaf76d3d8142cba9",
  "translation_date": "2025-09-05T20:11:04+00:00",
  "source_file": "2-Working-With-Data/07-python/README.md",
  "language_code": "my"
}
-->
# ဒေတာနှင့်အလုပ်လုပ်ခြင်း: Python နှင့် Pandas Library

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/07-WorkWithPython.png) |
| :-------------------------------------------------------------------------------------------------------: |
|                 Python နှင့်အလုပ်လုပ်ခြင်း - _Sketchnote by [@nitya](https://twitter.com/nitya)_                 |

[![Intro Video](../../../../2-Working-With-Data/07-python/images/video-ds-python.png)](https://youtu.be/dZjWOGbsN4Y)

ဒေတာများကို သိမ်းဆည်းရန်နှင့် query languages အသုံးပြု၍ ရှာဖွေရန်အတွက် databases သည် အလွန်ထိရောက်သောနည်းလမ်းများပေးနိုင်သော်လည်း၊ ဒေတာကို ကိုယ်တိုင်ရေးသားထားသော program ဖြင့် ပြုပြင်ရန်သည် အလွန် flexible ဖြစ်သည်။ အချို့သောအခြေအနေများတွင် database query သည် ပိုထိရောက်နိုင်သော်လည်း၊ SQL ဖြင့် လွယ်ကူစွာလုပ်ဆောင်၍မရသော အဆင့်မြင့်ဒေတာလုပ်ငန်းများအတွက် program ရေးသားခြင်းသည် မဖြစ်မနေလိုအပ်သည်။  
ဒေတာလုပ်ငန်းများကို programming language မည်သည့်အမျိုးအစားဖြင့်မဆို ရေးသားနိုင်သော်လည်း၊ ဒေတာနှင့်အလုပ်လုပ်ရန်အထူးသင့်လျော်သော programming languages ရှိသည်။ ဒေတာသိပ္ပံပညာရှင်များသည် အောက်ပါဘာသာစကားများကို အများအားဖြင့်နှစ်သက်ကြသည်-

* **[Python](https://www.python.org/)** သည် general-purpose programming language ဖြစ်ပြီး၊ ရိုးရှင်းမှုကြောင့် beginner များအတွက် အကောင်းဆုံးရွေးချယ်မှုတစ်ခုအဖြစ် သတ်မှတ်ခံရသည်။ Python တွင် practical ပြဿနာများကို ဖြေရှင်းရန်အတွက် အထောက်အကူပြု library များစွာပါဝင်သည်။ ဥပမာ- ZIP archive မှ ဒေတာကို extract လုပ်ခြင်း၊ သို့မဟုတ် ပုံကို grayscale သို့ပြောင်းခြင်း။ ဒေတာသိပ္ပံအပြင် Python သည် web development အတွက်လည်း အသုံးများသည်။  
* **[R](https://www.r-project.org/)** သည် statistical data processing အတွက် အထူးထုတ်လုပ်ထားသော traditional toolbox ဖြစ်သည်။ CRAN library များစွာပါဝင်သောကြောင့် ဒေတာလုပ်ငန်းများအတွက် ရွေးချယ်ရန်ကောင်းသည်။ သို့သော် R သည် general-purpose programming language မဟုတ်သည့်အပြင် ဒေတာသိပ္ပံနယ်ပယ်အပြင် အခြားနယ်ပယ်များတွင် အသုံးမများပါ။  
* **[Julia](https://julialang.org/)** သည် ဒေတာသိပ္ပံအတွက် အထူးထုတ်လုပ်ထားသော programming language တစ်ခုဖြစ်သည်။ Python ထက် performance ပိုကောင်းစေရန် ရည်ရွယ်ထားသောကြောင့် သိပ္ပံလေ့လာမှုများအတွက် tool ကောင်းတစ်ခုဖြစ်သည်။

ဒီသင်ခန်းစာတွင် Python ကို simple data processing အတွက် အသုံးပြုခြင်းကို အဓိကထားမည်ဖြစ်သည်။ Python ဘာသာစကားနှင့် အခြေခံကျွမ်းကျင်မှုရှိသည်ဟု သတ်မှတ်ထားမည်။ Python ကို ပိုမိုနက်ရှိုင်းစွာလေ့လာလိုပါက အောက်ပါ resources များကို ရည်ညွှန်းနိုင်သည်-

* [Learn Python in a Fun Way with Turtle Graphics and Fractals](https://github.com/shwars/pycourse) - GitHub-based Python Programming အကျဉ်းသင်တန်း  
* [Take your First Steps with Python](https://docs.microsoft.com/en-us/learn/paths/python-first-steps/?WT.mc_id=academic-77958-bethanycheum) Microsoft Learn တွင် Learning Path  

ဒေတာသည် အမျိုးအစားများစွာရှိနိုင်သည်။ ဒီသင်ခန်းစာတွင် **tabular data**, **text** နှင့် **images** ဆိုသည့် ဒေတာအမျိုးအစား ၃ မျိုးကို လေ့လာမည်ဖြစ်သည်။

ဒီသင်ခန်းစာတွင် library အားလုံးကို အပြည့်အစုံမဖော်ပြဘဲ၊ ဒေတာလုပ်ငန်းများ၏ အဓိကအချက်များကို နားလည်စေရန်အတွက် ဥပမာအချို့ကိုသာ အဓိကထားမည်ဖြစ်သည်။ ဒါက သင်၏ပြဿနာများကို ဖြေရှင်းရန်အတွက် လိုအပ်သော solution များကို ရှာဖွေတတ်စေရန် အထောက်အကူပြုမည်။

> **အရေးကြီးသောအကြံပေးချက်**: သင်မသိသော ဒေတာလုပ်ငန်းတစ်ခုကို လုပ်ဆောင်ရန်လိုအပ်ပါက၊ အင်တာနက်တွင် ရှာဖွေကြည့်ပါ။ [Stackoverflow](https://stackoverflow.com/) တွင် Python ဖြင့် လုပ်ဆောင်နိုင်သော typical task များအတွက် code sample များစွာပါဝင်သည်။  

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/12)

## Tabular Data နှင့် Dataframes

Relational databases အကြောင်းပြောခဲ့သောအခါတွင် သင်သည် tabular data ကို ရင်းနှီးပြီးဖြစ်သည်။ ဒေတာများစွာရှိပြီး၊ အမျိုးမျိုးသော tables များတွင် ချိတ်ဆက်ထားသောအခါ SQL ကို အသုံးပြုရန် make sense ဖြစ်သည်။ သို့သော် တစ်ခါတစ်ရံတွင် table တစ်ခုသာရှိပြီး၊ ဒေတာ၏ **distribution** သို့မဟုတ် **correlation** စသည်တို့ကို နားလည်ရန်လိုအပ်သည်။ ဒေတာသိပ္ပံတွင် original data ကို transformation လုပ်ပြီး visualization ပြုလုပ်ရန်လိုအပ်သောအခါများစွာရှိသည်။ Python သုံးခြင်းဖြင့် အလွယ်တကူလုပ်ဆောင်နိုင်သည်။

Python တွင် tabular data ကို handle လုပ်ရန် အထောက်အကူပြု library ၂ ခုအရေးကြီးဆုံးဖြစ်သည်-
* **[Pandas](https://pandas.pydata.org/)** သည် **Dataframes** ကို manipulate လုပ်ရန်အထောက်အကူပြု library ဖြစ်သည်။ Dataframes သည် relational tables နှင့် ဆင်တူသည်။ Named columns ရှိပြီး၊ rows, columns နှင့် dataframes အပေါ်တွင် အမျိုးမျိုးသော operations လုပ်နိုင်သည်။  
* **[Numpy](https://numpy.org/)** သည် **tensors** (multi-dimensional **arrays**) ကို handle လုပ်ရန် library ဖြစ်သည်။ Array သည် တူညီသော underlying type ရှိသော values များပါဝင်ပြီး၊ dataframe ထက် ရိုးရှင်းသော်လည်း mathematical operations ပိုမိုလုပ်ဆောင်နိုင်သည်။

အခြား library အချို့ကိုလည်း သိထားသင့်သည်-
* **[Matplotlib](https://matplotlib.org/)** သည် data visualization နှင့် graph plotting အတွက် အသုံးပြုသော library  
* **[SciPy](https://www.scipy.org/)** သည် probability နှင့် statistics အကြောင်းပြောခဲ့သောအခါ တွေ့ရှိခဲ့သော additional scientific functions ပါဝင်သော library  

Python program ရဲ့အစမှာ library များကို import လုပ်ရန် typical code:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import ... # you need to specify exact sub-packages that you need
``` 

Pandas သည် အခြေခံ concepts အချို့ကို အဓိကထားသည်။

### Series 

**Series** သည် list သို့မဟုတ် numpy array နှင့် ဆင်တူသော values များ၏ အစဉ်ဖြစ်သည်။ အဓိကကွာခြားချက်မှာ series တွင် **index** ပါဝင်ပြီး၊ series အပေါ်တွင် operation လုပ်သောအခါ index ကို အရေးထားသည်။ Index သည် integer row number (list သို့မဟုတ် array မှ series တစ်ခုဖန်တီးသောအခါ default index) လိုရိုးရှင်းနိုင်သလို၊ date interval လို complex structure ရှိနိုင်သည်။

> **Note**: Pandas code အချို့ကို notebook [`notebook.ipynb`](../../../../2-Working-With-Data/07-python/notebook.ipynb) တွင်ပါဝင်သည်။ ဤနေရာတွင် ဥပမာအချို့ကို outline လုပ်ထားပြီး၊ notebook အပြည့်အစုံကို ကြည့်ရှုရန်လည်း ကြိုဆိုပါသည်။

ဥပမာ- ကျွန်ုပ်တို့၏ ice-cream spot ရဲ့ရောင်းအားကို analysis လုပ်လိုသည်။ sales numbers (နေ့စဉ်ရောင်းအား) series တစ်ခုကို generate လုပ်မည်:

```python
start_date = "Jan 1, 2020"
end_date = "Mar 31, 2020"
idx = pd.date_range(start_date,end_date)
print(f"Length of index is {len(idx)}")
items_sold = pd.Series(np.random.randint(25,50,size=len(idx)),index=idx)
items_sold.plot()
```
![Time Series Plot](../../../../2-Working-With-Data/07-python/images/timeseries-1.png)

အပတ်စဉ် ကျွန်ုပ်တို့သည် party တစ်ခုကို စီစဉ်ပြီး၊ party အတွက် ice-cream 10 packs ထပ်ယူသည်။ အပတ်အလိုက် index ရှိသော series တစ်ခုကို ဖန်တီးနိုင်သည်:
```python
additional_items = pd.Series(10,index=pd.date_range(start_date,end_date,freq="W"))
```
series နှစ်ခုကို ပေါင်းလိုက်သောအခါ total number ရရှိမည်:
```python
total_items = items_sold.add(additional_items,fill_value=0)
total_items.plot()
```
![Time Series Plot](../../../../2-Working-With-Data/07-python/images/timeseries-2.png)

> **Note**: `total_items+additional_items` syntax ကို ရိုးရိုးမသုံးပါ။ သုံးခဲ့လျှင် `NaN` (*Not a Number*) values များစွာရရှိမည်။ ဒါဟာ `additional_items` series ရဲ့ index point အချို့တွင် missing values ရှိသောကြောင့်ဖြစ်ပြီး၊ `NaN` ကို အခြား value နှင့်ပေါင်းလိုက်လျှင် `NaN` ဖြစ်သွားသည်။ ထို့ကြောင့် addition လုပ်သောအခါ `fill_value` parameter ကို သတ်မှတ်ရန်လိုအပ်သည်။

Time series တွင် **resample** လုပ်၍ time interval များကို ပြောင်းနိုင်သည်။ ဥပမာ- monthly mean sales volume ကိုတွက်လိုပါက အောက်ပါ code ကို အသုံးပြုနိုင်သည်:
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
ဤအရာသည် အောက်ပါ table ကို ဖန်တီးမည်:
|     | 0   | 1    | 2   | 3   | 4      | 5   | 6      | 7    | 8    |
| --- | --- | ---- | --- | --- | ------ | --- | ------ | ---- | ---- |
| 0   | 1   | 2    | 3   | 4   | 5      | 6   | 7      | 8    | 9    |
| 1   | I   | like | to  | use | Python | and | Pandas | very | much |

Series များကို columns အဖြစ်အသုံးပြုပြီး၊ dictionary အသုံးပြု၍ column names သတ်မှတ်နိုင်သည်:
```python
df = pd.DataFrame({ 'A' : a, 'B' : b })
```
ဤအရာသည် အောက်ပါ table ကို ဖန်တီးမည်:

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

**Note**: `.T` သည် DataFrame ကို transpose လုပ်ခြင်းဖြစ်ပြီး၊ rows နှင့် columns ကို ပြောင်းလဲသည်။ `rename` operation သည် column names ကို ပြောင်းလဲရန်အတွက် အသုံးပြုသည်။

DataFrame အပေါ်တွင် လုပ်ဆောင်နိုင်သော အရေးကြီးဆုံး operations အချို့မှာ-

**Column selection**. Individual columns ကို `df['A']` ဖြင့် ရွေးနိုင်သည်။ Subset of columns ကို `df[['B','A']]` ဖြင့် DataFrame အသစ်တစ်ခုအဖြစ် ရွေးနိုင်သည်။

**Filtering**. Row များကို criteria အပေါ်မူတည်၍ ရွေးနိုင်သည်။ ဥပမာ- column `A` > 5 ဖြစ်သော rows များကို ရွေးရန် `df[df['A']>5]` ကို အသုံးပြုနိုင်သည်။

> **Note**: Filtering သည် boolean series ကို အသုံးပြုသည်။ Boolean series သည် original series `df['A']` ရဲ့ element တစ်ခုချင်းစီအတွက် `True` သို့မဟုတ် `False` ဖြစ်သည်ကို ပြသည်။ Boolean series ကို index အဖြစ်အသုံးပြုသောအခါ DataFrame ရဲ့ subset rows ကို ပြန်ပေးသည်။ Python boolean expression များကို ရိုးရိုးအသုံးပြု၍မရပါ။ ဥပမာ- `df[df['A']>5 and df['A']<7]` မှားသည်။ `&` operation ကို boolean series အပေါ်အသုံးပြု၍ `df[(df['A']>5) & (df['A']<7)]` ရေးရန်လိုအပ်သည် (*brackets အရေးကြီးသည်*).

**Creating new computable columns**. DataFrame အတွက် computable columns အသစ်များကို ရိုးရှင်းသော expression ဖြင့် ဖန်တီးနိုင်သည်:
```python
df['DivA'] = df['A']-df['A'].mean() 
``` 
ဤဥပမာသည် A ရဲ့ mean value မှ divergence ကိုတွက်ချက်သည်။ Series တစ်ခုကို left-hand-side တွင် assign လုပ်ပြီး၊ column အသစ်တစ်ခုကို ဖန်တီးသည်။ Series နှင့်မကိုက်ညီသော operations များကို အသုံးပြု၍မရပါ။ ဥပမာ- အောက်ပါ code မှားသည်:
```python
# Wrong code -> df['ADescr'] = "Low" if df['A'] < 5 else "Hi"
df['LenB'] = len(df['B']) # <- Wrong result
``` 
ဤဥပမာသည် syntactically မှန်သော်လည်း၊ `B` series ရဲ့ length ကို column value အားလုံးတွင် assign လုပ်သွားသည်။

Complex expressions တွက်ရန် `apply` function ကို အသုံးပြုနိုင်သည်။ အောက်ပါအတိုင်းရေးနိုင်သည်:
```python
df['LenB'] = df['B'].apply(lambda x : len(x))
# or 
df['LenB'] = df['B'].apply(len)
```

အထက်ပါ operations များပြီးဆုံးသောအခါ DataFrame သည် အောက်ပါအတိုင်းဖြစ်မည်:

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

**Selecting rows based on numbers**. `iloc` ကိုအသုံးပြု၍ row များကို ရွေးနိုင်သည်။ ဥပမာ- ပထမ ၅ rows ကို ရွေးရန်:
```python
df.iloc[:5]
```

**Grouping**. Excel ရဲ့ *pivot tables* နှင့်ဆင်တူသော result ရရှိရန် Grouping ကို အသုံးပြုနိုင်သည်။ ဥပမာ- `LenB` တစ်ခုချင်းစီအတွက် column `A` ရဲ့ mean value ကိုတွက်ရန် `LenB` ဖြင့် group လုပ်ပြီး `mean` ကိုခေါ်နိုင်သည်:
```python
df.groupby(by='LenB').mean()
```
Mean နှင့် group ရဲ့ element အရေအတွက်ကိုတွက်ရန် `aggregate` function ကို အသုံးပြုနိုင်သည်:
```python
df.groupby(by='LenB') \
 .aggregate({ 'DivA' : len, 'A' : lambda x: x.mean() }) \
 .rename(columns={ 'DivA' : 'Count', 'A' : 'Mean'})
```
ဤအရာသည် အောက်ပါ table ကို ဖန်တီးမည်:

| LenB | Count | Mean     |
| ---- | ----- | -------- |
| 1    | 1     | 1.000000 |
| 2    | 1     | 3.000000 |
| 3    | 2     | 5.000000 |
| 4    | 3     | 6.333333 |
| 6    | 2     | 6.000000 |

### ဒေတာရယူခြင်း
### Series နှင့် DataFrames ဖန်တီးခြင်း

Python object တွေကို အသုံးပြုပြီး Series နဲ့ DataFrames ဖန်တီးတာ ဘယ်လောက်လွယ်ကူတယ်ဆိုတာကို ကြည့်ပြီးသားဖြစ်ပါတယ်။ သို့သော် အချက်အလက်တွေဟာ အများအားဖြင့် text file သို့မဟုတ် Excel table အနေနဲ့ ရှိတတ်ပါတယ်။ ကံကောင်းစွာ Pandas က disk မှ အချက်အလက်တွေကို load လုပ်ဖို့ လွယ်ကူတဲ့နည်းလမ်းတစ်ခုကို ပေးထားပါတယ်။ ဥပမာ CSV file ကို ဖတ်ရှုဖို့ အလွန်လွယ်ကူပါတယ်:
```python
df = pd.read_csv('file.csv')
```
"Challenge" အပိုင်းမှာ အခြားသော အချက်အလက်တွေကို load လုပ်နည်းနဲ့ အပြင်မှာ website တွေကနေ fetch လုပ်နည်းကို ပိုမိုကြည့်ရှုနိုင်ပါမယ်။

### Printing နှင့် Plotting

Data Scientist တစ်ဦးအနေနဲ့ အချက်အလက်တွေကို လေ့လာဖို့လိုအပ်တာကြောင့် visualization လုပ်နိုင်ဖို့ အရေးကြီးပါတယ်။ DataFrame ကြီးတစ်ခုကို handle လုပ်တဲ့အခါမှာ အစပိုင်း row အနည်းငယ်ကို print လုပ်ပြီး အားလုံးမှန်ကန်နေမလား စစ်ဆေးဖို့လိုတတ်ပါတယ်။ ဒါကို `df.head()` ကို ခေါ်ပြီး လုပ်နိုင်ပါတယ်။ Jupyter Notebook မှာ run လုပ်ရင် DataFrame ကို tabular form လှပလှပနဲ့ ပြသပေးပါမယ်။

`plot` function ကို အသုံးပြုပြီး column တချို့ကို visualize လုပ်နည်းကို ကြည့်ပြီးသားဖြစ်ပါတယ်။ `plot` ဟာ အလုပ်အတော်များများအတွက် အသုံးဝင်ပြီး `kind=` parameter ကို အသုံးပြုပြီး graph အမျိုးအစားများစွာကို support လုပ်ပေးနိုင်ပါတယ်။ သို့သော် `matplotlib` library ကို raw အနေနဲ့ အသုံးပြုပြီး ပိုမိုရှုပ်ထွေးတဲ့ graph တွေကို plot လုပ်နိုင်ပါတယ်။ Data visualization ကို သီးသန့်သင်ခန်းစာတွေမှာ အသေးစိတ်လေ့လာပါမယ်။

ဒီအကျဉ်းချုပ်မှာ Pandas ရဲ့ အရေးကြီးဆုံး concept တွေကို ဖော်ပြထားပါတယ်။ သို့သော် library ဟာ အလွန်ချောမောပြီး မလုပ်နိုင်တာမရှိလို့ ပြောလို့ရပါတယ်။ အခုတော့ ဒီအတတ်ပညာကို အသုံးပြုပြီး အထူးပြဿနာတွေကို ဖြေရှင်းကြပါစို့။

## 🚀 Challenge 1: COVID-19 ကူးစက်မှုကို ခွဲခြမ်းစိတ်ဖြာခြင်း

ပထမပြဿနာမှာ COVID-19 ရောဂါကူးစက်မှုကို မော်ဒယ်တစ်ခုအနေနဲ့ ဖော်ပြဖို့ အာရုံစိုက်ပါမယ်။ ဒါကို ပြုလုပ်ဖို့ [Center for Systems Science and Engineering](https://systems.jhu.edu/) (CSSE) မှ [Johns Hopkins University](https://jhu.edu/) က ပေးထားတဲ့ အမျိုးသားစုံကူးစက်သူအရေအတွက်အချက်အလက်တွေကို အသုံးပြုပါမယ်။ Dataset ကို [GitHub Repository](https://github.com/CSSEGISandData/COVID-19) မှာ ရနိုင်ပါတယ်။

အချက်အလက်တွေကို handle လုပ်နည်းကို ပြသဖို့ [`notebook-covidspread.ipynb`](../../../../2-Working-With-Data/07-python/notebook-covidspread.ipynb) ကို ဖွင့်ပြီး အစမှအဆုံးဖတ်ရှုဖို့ ဖိတ်ခေါ်ပါတယ်။ Cell တွေကို run လုပ်နိုင်ပြီး အဆုံးမှာ ကျွန်တော်တို့ထားခဲ့တဲ့ challenge တွေကို လုပ်ဆောင်နိုင်ပါတယ်။

![COVID Spread](../../../../2-Working-With-Data/07-python/images/covidspread.png)

> Jupyter Notebook မှာ code run လုပ်နည်းကို မသိသေးရင် [ဒီဆောင်းပါး](https://soshnikov.com/education/how-to-execute-notebooks-from-github/) ကို ကြည့်ပါ။

## Unstructured Data ကို Handle လုပ်ခြင်း

အချက်အလက်တွေဟာ tabular form အနေနဲ့ ရှိတတ်ပေမယ့် တချို့အခါမှာ text သို့မဟုတ် image အနေနဲ့ ရှိတတ်ပါတယ်။ ဒီအခါမှာ အပေါ်မှာ ပြထားတဲ့ data processing နည်းလမ်းတွေကို အသုံးပြုဖို့ structured data ကို **extract** လုပ်ဖို့လိုအပ်ပါတယ်။ ဥပမာအချို့မှာ:

* Text မှ keyword တွေကို extract လုပ်ပြီး keyword တွေ ဘယ်လောက်ကြိမ်တွေ့ရလဲ စစ်ဆေးခြင်း
* Neural networks ကို အသုံးပြုပြီး ပုံထဲမှာ object တွေကို extract လုပ်ခြင်း
* Video camera feed မှ လူတွေရဲ့ စိတ်ခံစားမှုကို သိရှိခြင်း

## 🚀 Challenge 2: COVID Papers ကို ခွဲခြမ်းစိတ်ဖြာခြင်း

ဒီ challenge မှာ COVID pandemic နဲ့ ဆက်စပ်တဲ့ သိပ္ပံစာတမ်းတွေကို process လုပ်ခြင်းအပေါ် အာရုံစိုက်ပါမယ်။ [CORD-19 Dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) မှာ metadata နဲ့ abstract တွေပါဝင်တဲ့ COVID အကြောင်းစာတမ်း 7000 ကျော် (ရေးသားချိန်အတိုင်း) ရှိပါတယ်။ အချို့စာတမ်းတွေအတွက် full text ပါဝင်ပါတယ်။

[Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health/?WT.mc_id=academic-77958-bethanycheum) cognitive service ကို အသုံးပြုပြီး dataset ကို ခွဲခြမ်းစိတ်ဖြာနည်းကို [ဒီ blog post](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) မှာ ဖော်ပြထားပါတယ်။ simplified version ကို ဆွေးနွေးပါမယ်။

> **NOTE**: Dataset ကို repository မှာ မပါဝင်ပါဘူး။ [Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge?select=metadata.csv) မှာ [`metadata.csv`](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge?select=metadata.csv) ကို download လုပ်ဖို့လိုအပ်နိုင်ပါတယ်။ Kaggle မှာ registration လုပ်ဖို့လိုအပ်နိုင်ပါတယ်။ [ဒီနေရာ](https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases.html) မှာ registration မလိုအပ်ဘဲ dataset ကို download လုပ်နိုင်ပါတယ်။

[`notebook-papers.ipynb`](../../../../2-Working-With-Data/07-python/notebook-papers.ipynb) ကို ဖွင့်ပြီး အစမှအဆုံးဖတ်ရှုပါ။ Cell တွေကို run လုပ်နိုင်ပြီး ကျွန်တော်တို့ထားခဲ့တဲ့ challenge တွေကို လုပ်ဆောင်နိုင်ပါတယ်။

![Covid Medical Treatment](../../../../2-Working-With-Data/07-python/images/covidtreat.png)

## Image Data ကို Process လုပ်ခြင်း

လတ်တလောမှာ AI model တွေက ပုံတွေကို နားလည်နိုင်ဖို့ အလွန်အစွမ်းထက်လာပါတယ်။ Pre-trained neural networks သို့မဟုတ် cloud services ကို အသုံးပြုပြီး အလုပ်အမျိုးမျိုးကို ဖြေရှင်းနိုင်ပါတယ်။ ဥပမာအချို့မှာ:

* **Image Classification** - ပုံကို pre-defined class တစ်ခုမှာ categorize လုပ်နိုင်ပါတယ်။ [Custom Vision](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/?WT.mc_id=academic-77958-bethanycheum) ကို အသုံးပြုပြီး ကိုယ်ပိုင် image classifier တွေကို လွယ်ကူစွာ train လုပ်နိုင်ပါတယ်။
* **Object Detection** - ပုံထဲမှာ object တွေကို detect လုပ်နိုင်ပါတယ်။ [computer vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/?WT.mc_id=academic-77958-bethanycheum) က common object တွေကို detect လုပ်နိုင်ပြီး [Custom Vision](https://azure.microsoft.com/services/cognitive-services/custom-vision-service/?WT.mc_id=academic-77958-bethanycheum) ကို အသုံးပြုပြီး specific object တွေကို detect လုပ်နိုင်ပါတယ်။
* **Face Detection** - အသက်, ကျား/မ, စိတ်ခံစားမှု detection ပါဝင်ပါတယ်။ [Face API](https://azure.microsoft.com/services/cognitive-services/face/?WT.mc_id=academic-77958-bethanycheum) ကို အသုံးပြုနိုင်ပါတယ်။

Python SDK တွေကို အသုံးပြုပြီး cloud services တွေကို ခေါ်နိုင်ပြီး data exploration workflow မှာ ထည့်သွင်းနိုင်ပါတယ်။

ဥပမာအချို့:
* [How to Learn Data Science without Coding](https://soshnikov.com/azure/how-to-learn-data-science-without-coding/) blog post မှာ Instagram ပုံတွေကို လေ့လာပြီး ပုံတစ်ပုံကို ဘယ်လို likes ပိုရနိုင်မလဲ စစ်ဆေးပါတယ်။ [computer vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/?WT.mc_id=academic-77958-bethanycheum) ကို အသုံးပြုပြီး ပုံတွေကနေ အချက်အလက်တွေကို extract လုပ်ပြီး [Azure Machine Learning AutoML](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml/?WT.mc_id=academic-77958-bethanycheum) ကို အသုံးပြုပြီး model တစ်ခုကို တည်ဆောက်ပါတယ်။
* [Facial Studies Workshop](https://github.com/CloudAdvocacy/FaceStudies) မှာ [Face API](https://azure.microsoft.com/services/cognitive-services/face/?WT.mc_id=academic-77958-bethanycheum) ကို အသုံးပြုပြီး ပုံထဲမှာ လူတွေရဲ့ စိတ်ခံစားမှုကို extract လုပ်ပြီး လူတွေကို ဘယ်လို ပျော်ရွှင်စေမလဲ စစ်ဆေးပါတယ်။

## နိဂုံး

Structured data ဖြစ်ဖြစ်၊ unstructured data ဖြစ်ဖြစ် Python ကို အသုံးပြုပြီး data processing နဲ့ data ကို နားလည်ဖို့ လုပ်ဆောင်နိုင်ပါတယ်။ Python ဟာ data processing အတွက် အ flexibilty အများဆုံးရှိတဲ့ နည်းလမ်းဖြစ်ပြီး Data Scientist အများစုက Python ကို အဓိက tool အနေနဲ့ အသုံးပြုကြပါတယ်။ Data Science ကို အလေးထားပြီး လေ့လာချင်ရင် Python ကို နက်နက်ရှိုင်းရှိုင်း လေ့လာဖို့ အကြံပေးပါတယ်။

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/13)

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

ဒီသင်ခန်းစာကို [Dmitry Soshnikov](http://soshnikov.com) မှ ♥️ နဲ့ရေးသားထားပါတယ်။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေပါသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါရှိနိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူလဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။