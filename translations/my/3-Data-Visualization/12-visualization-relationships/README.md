<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b29e427401499e81f4af55a8c4afea76",
  "translation_date": "2025-09-05T05:21:45+00:00",
  "source_file": "3-Data-Visualization/12-visualization-relationships/README.md",
  "language_code": "my"
}
-->
# ဆက်ဆံရေးများကိုမြင်နိုင်စေခြင်း: ပျားရည်အကြောင်း 🍯

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|ဆက်ဆံရေးများကိုမြင်နိုင်စေခြင်း - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

သဘာဝအပေါ်အာရုံစိုက်မှုကိုဆက်လက်လေ့လာရင်း၊ အမျိုးမျိုးသောပျားရည်အမျိုးအစားများအကြားဆက်ဆံရေးများကိုဖော်ပြရန်စိတ်ဝင်စားဖွယ်မြင်ကွင်းများကိုရှာဖွေကြမယ်။ ဒီအချက်အလက်များကို [အမေရိကန်စိုက်ပျိုးရေးဌာန](https://www.nass.usda.gov/About_NASS/index.php) မှရရှိသောဒေတာအရဖော်ပြထားပါတယ်။

ဤဒေတာတွင် ၆၀၀ ကျော်သောအချက်အလက်များပါဝင်ပြီး အမေရိကန်ပြည်နယ်များတွင်ပျားရည်ထုတ်လုပ်မှုကိုဖော်ပြထားပါတယ်။ ဥပမာအားဖြင့်၊ ၁၉၉၈-၂၀၁၂ အတွင်းတစ်ပြည်နယ်စီ၏တစ်နှစ်စီအတွက်ပျားအုပ်အရေအတွက်၊ တစ်ပျားအုပ်လျှင်ထုတ်လုပ်မှု၊ စုစုပေါင်းထုတ်လုပ်မှု၊ စတော့များ၊ တစ်ပေါင်လျှင်ဈေးနှုန်းနှင့် ထုတ်လုပ်မှုတန်ဖိုးတို့ကိုကြည့်နိုင်ပါတယ်။

တစ်ပြည်နယ်၏တစ်နှစ်စီထုတ်လုပ်မှုနှင့် ထိုပြည်နယ်ရှိပျားရည်ဈေးနှုန်းအကြားဆက်ဆံရေးကိုမြင်နိုင်စေဖို့စိတ်ဝင်စားဖွယ်ကောင်းပါတယ်။ ဒါမှမဟုတ်၊ တစ်ပြည်နယ်စီ၏တစ်ပျားအုပ်လျှင်ပျားရည်ထုတ်လုပ်မှုအကြားဆက်ဆံရေးကိုမြင်နိုင်စေဖို့လည်းစိတ်ဝင်စားဖွယ်ကောင်းပါတယ်။ ဒီနှစ်အကွာအဝေးသည် ၂၀၀၆ ခုနှစ်တွင်ပထမဆုံးတွေ့ရှိခဲ့သော 'CCD' သို့မဟုတ် 'Colony Collapse Disorder' (http://npic.orst.edu/envir/ccd.html) ကိုဖော်ပြထားပြီး လေ့လာရန်အရေးကြီးသောဒေတာတစ်ခုဖြစ်ပါတယ်။ 🐝

## [Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

ဒီသင်ခန်းစာမှာ၊ သင်ဟာ Seaborn ကိုအသုံးပြုနိုင်ပြီး၊ ဒေတာအကြားဆက်ဆံရေးများကိုမြင်နိုင်စေဖို့ကောင်းသောစာကြည့်တိုက်တစ်ခုဖြစ်ပါတယ်။ အထူးသဖြင့် Seaborn ရဲ့ `relplot` function ကိုအသုံးပြုခြင်းဖြင့် scatter plots နှင့် line plots ကိုမြန်ဆန်စွာဖော်ပြနိုင်ပြီး '[statistical relationships](https://seaborn.pydata.org/tutorial/relational.html?highlight=relationships)' ကိုမြင်နိုင်စေပါတယ်။ ဒါဟာဒေတာသိပ္ပံပညာရှင်များအတွက် variable များအကြားဆက်ဆံရေးကိုပိုမိုနားလည်စေပါတယ်။

## Scatterplots

ပျားရည်ဈေးနှုန်းသည်နှစ်အလိုက်၊ ပြည်နယ်အလိုက်ဘယ်လိုပြောင်းလဲလာသလဲဆိုတာကို scatterplot ဖြင့်ဖော်ပြပါ။ Seaborn ရဲ့ `relplot` ကိုအသုံးပြုခြင်းဖြင့် ပြည်နယ်ဒေတာကိုအုပ်စုဖွဲ့ပြီး categorical နှင့် numeric ဒေတာများအတွက် data points များကိုဖော်ပြနိုင်ပါတယ်။

ပထမဆုံး ဒေတာနှင့် Seaborn ကို import လုပ်ပါ:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
honey = pd.read_csv('../../data/honey.csv')
honey.head()
```
သင်တွေ့ရှိမယ့်အတိုင်း၊ ပျားရည်ဒေတာတွင်နှစ်နှင့်တစ်ပေါင်လျှင်ဈေးနှုန်းတို့အပါအဝင်စိတ်ဝင်စားဖွယ် column များစွာပါဝင်ပါတယ်။ အမေရိကန်ပြည်နယ်အလိုက်အုပ်စုဖွဲ့ထားသောဤဒေတာကိုလေ့လာကြည့်ပါ:

| state | numcol | yieldpercol | totalprod | stocks   | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL    | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ    | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR    | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA    | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO    | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |

ပျားရည်တစ်ပေါင်လျှင်ဈေးနှုန်းနှင့် အမေရိကန်ပြည်နယ်၏မူလအစအကြားဆက်ဆံရေးကိုဖော်ပြရန်အခြေခံ scatterplot တစ်ခုဖန်တီးပါ။ `y` axis ကိုပြည်နယ်အားလုံးကိုဖော်ပြနိုင်အောင်လုံလောက်အောင်မြင့်ပါ:

```python
sns.relplot(x="priceperlb", y="state", data=honey, height=15, aspect=.5);
```
![scatterplot 1](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter1.png)

အခုတော့၊ နှစ်အလိုက်ဈေးနှုန်းပြောင်းလဲမှုကိုဖော်ပြရန် ပျားရည်အရောင် scheme ကိုအသုံးပြုပါ။ hue parameter ကိုထည့်သွင်းခြင်းဖြင့်နှစ်အလိုက်ပြောင်းလဲမှုကိုဖော်ပြနိုင်ပါတယ်:

> ✅ Seaborn တွင်အသုံးပြုနိုင်သော [အရောင် palettes](https://seaborn.pydata.org/tutorial/color_palettes.html) အကြောင်းပိုမိုလေ့လာပါ - လှပသော rainbow color scheme ကိုစမ်းကြည့်ပါ!

```python
sns.relplot(x="priceperlb", y="state", hue="year", palette="YlOrBr", data=honey, height=15, aspect=.5);
```
![scatterplot 2](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter2.png)

ဒီအရောင် scheme ပြောင်းလဲမှုဖြင့်၊ ပျားရည်တစ်ပေါင်လျှင်ဈေးနှုန်းသည်နှစ်အလိုက်တိုးတက်မှုရှိနေသည်ကိုရှင်းလင်းစွာမြင်နိုင်ပါတယ်။ အမှန်တကယ်၊ ဒေတာထဲမှနမူနာတစ်ခုကိုစစ်ဆေးကြည့်ပါက (ဥပမာအားဖြင့် Arizona ပြည်နယ်) နှစ်အလိုက်ဈေးနှုန်းတိုးတက်မှု pattern ကိုရှုမြင်နိုင်ပါတယ်၊ အချို့သောကွဲလွဲမှုများရှိသော်လည်း:

| state | numcol | yieldpercol | totalprod | stocks  | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | ------- | ---------- | --------- | ---- |
| AZ    | 55000  | 60          | 3300000   | 1485000 | 0.64       | 2112000   | 1998 |
| AZ    | 52000  | 62          | 3224000   | 1548000 | 0.62       | 1999000   | 1999 |
| AZ    | 40000  | 59          | 2360000   | 1322000 | 0.73       | 1723000   | 2000 |
| AZ    | 43000  | 59          | 2537000   | 1142000 | 0.72       | 1827000   | 2001 |
| AZ    | 38000  | 63          | 2394000   | 1197000 | 1.08       | 2586000   | 2002 |
| AZ    | 35000  | 72          | 2520000   | 983000  | 1.34       | 3377000   | 2003 |
| AZ    | 32000  | 55          | 1760000   | 774000  | 1.11       | 1954000   | 2004 |
| AZ    | 36000  | 50          | 1800000   | 720000  | 1.04       | 1872000   | 2005 |
| AZ    | 30000  | 65          | 1950000   | 839000  | 0.91       | 1775000   | 2006 |
| AZ    | 30000  | 64          | 1920000   | 902000  | 1.26       | 2419000   | 2007 |
| AZ    | 25000  | 64          | 1600000   | 336000  | 1.26       | 2016000   | 2008 |
| AZ    | 20000  | 52          | 1040000   | 562000  | 1.45       | 1508000   | 2009 |
| AZ    | 24000  | 77          | 1848000   | 665000  | 1.52       | 2809000   | 2010 |
| AZ    | 23000  | 53          | 1219000   | 427000  | 1.55       | 1889000   | 2011 |
| AZ    | 22000  | 46          | 1012000   | 253000  | 1.79       | 1811000   | 2012 |

အရောင်မမြင်နိုင်သောသူများအတွက်၊ အရောင်အစား dot size ကိုအသုံးပြုခြင်းသည်ပိုမိုကောင်းမွန်နိုင်ပါတယ်။ dot circumference တိုးတက်မှုဖြင့်ဈေးနှုန်းတိုးတက်မှုကိုဖော်ပြရန် visualization ကိုပြင်ဆင်ပါ:

```python
sns.relplot(x="priceperlb", y="state", size="year", data=honey, height=15, aspect=.5);
```
dot size များသည်တဖြည်းဖြည်းကြီးထွားလာသည်ကိုမြင်နိုင်ပါတယ်။

![scatterplot 3](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter3.png)

ဒါဟာ supply နှင့် demand ရိုးရှင်းသောအခြေအနေတစ်ခုလား? ရာသီဥတုပြောင်းလဲမှုနှင့် colony collapse ကဲ့သို့သောအကြောင်းအရင်းများကြောင့်နှစ်အလိုက်ပျားရည်ရရှိနိုင်မှုနည်းလာပြီးဈေးနှုန်းတိုးတက်လာတာလား?

ဒီဒေတာအတွင်း variable များအကြားဆက်ဆံရေးကိုရှာဖွေဖို့၊ line charts များကိုလေ့လာကြည့်ပါ။

## Line charts

မေးခွန်း: ပျားရည်တစ်ပေါင်လျှင်ဈေးနှုန်းသည်နှစ်အလိုက်တိုးတက်မှုရှိနေသလား? single line chart တစ်ခုဖန်တီးခြင်းဖြင့်အလွယ်တကူရှာဖွေနိုင်ပါတယ်:

```python
sns.relplot(x="year", y="priceperlb", kind="line", data=honey);
```
အဖြေ: ဟုတ်ပါတယ်၊ ၂၀၀၃ ခုနှစ်အနီးတွင်အချို့သောကွဲလွဲမှုများရှိသည်:

![line chart 1](../../../../3-Data-Visualization/12-visualization-relationships/images/line1.png)

✅ Seaborn သည် x value တစ်ခုစီတွင် "mean နှင့် mean အပေါ် 95% confidence interval ကိုဖော်ပြခြင်းဖြင့် measurement များစွာကိုအစုဖွဲ့ထားသည်"။ [အရင်းအမြစ်](https://seaborn.pydata.org/tutorial/relational.html)။ ဒီအချိန်စားသော behavior ကို `ci=None` ထည့်သွင်းခြင်းဖြင့်ပယ်ဖျက်နိုင်ပါတယ်။

မေးခွန်း: ၂၀၀၃ ခုနှစ်တွင်ပျားရည် supply spike ဖြစ်တာကိုလည်းမြင်နိုင်လား? စုစုပေါင်းထုတ်လုပ်မှုနှစ်အလိုက်ကြည့်ပါ:

```python
sns.relplot(x="year", y="totalprod", kind="line", data=honey);
```

![line chart 2](../../../../3-Data-Visualization/12-visualization-relationships/images/line2.png)

အဖြေ: အတိအကျမဟုတ်ပါဘူး။ စုစုပေါင်းထုတ်လုပ်မှုကိုကြည့်ပါက၊ အထူးသဖြင့်ပျားရည်ထုတ်လုပ်မှုအရေအတွက်သည်ဒီနှစ်များအတွင်းလျော့နည်းနေသော်လည်း၊ ထိုနှစ်တွင်တိုးတက်မှုရှိသည့်ပုံရသည်။

မေးခွန်း: ဒီအခြေအနေမှာ၊ ၂၀၀၃ ခုနှစ်တွင်ပျားရည်ဈေးနှုန်း spike ဖြစ်စေသောအကြောင်းအရင်းကဘာဖြစ်နိုင်မလဲ?

ဤအကြောင်းအရင်းကိုရှာဖွေဖို့၊ facet grid ကိုလေ့လာကြည့်ပါ။

## Facet grids

Facet grids သည် dataset ၏တစ်ခုသော facet ကိုယူပြီး (ဤအခါတွင် 'year' ကိုရွေးချယ်နိုင်သည်) သင်ရွေးချယ်ထားသော x နှင့် y coordinates အတွက် plot တစ်ခုစီကိုဖန်တီးနိုင်သည်။ ၂၀၀၃ ခုနှစ်သည်ဤမျှတမျှတသောနှိုင်းယှဉ်မှုတွင်ထူးထူးခြားခြားပေါ်လွင်ပါသလား?

Seaborn ရဲ့ [documentation](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html?highlight=facetgrid#seaborn.FacetGrid) မှအကြံပြုထားသည့်အတိုင်း `relplot` ကိုဆက်လက်အသုံးပြုခြင်းဖြင့် facet grid တစ်ခုဖန်တီးပါ။

```python
sns.relplot(
    data=honey, 
    x="yieldpercol", y="numcol",
    col="year", 
    col_wrap=3,
    kind="line"
```
ဤ visualization တွင် yield per colony နှင့် number of colonies ကိုနှစ်အလိုက်၊ ပြည်နယ်အလိုက်၊ wrap ကို column 3 အဖြစ်ထားပြီး side by side နှိုင်းယှဉ်နိုင်ပါတယ်:

![facet grid](../../../../3-Data-Visualization/12-visualization-relationships/images/facet.png)

ဤဒေတာအတွက်၊ number of colonies နှင့် yield တို့နှစ်အလိုက်၊ ပြည်နယ်အလိုက်ထူးထူးခြားခြားပေါ်လွင်သောအရာမရှိပါ။ ဤ variable နှစ်ခုအကြား correlation ရှာဖွေရန်အခြားနည်းလမ်းတစ်ခုရှိပါသလား?

## Dual-line Plots

Seaborn ရဲ့ 'despine' ကိုအသုံးပြု၍ top နှင့် right spines ကိုဖယ်ရှားပြီး၊ Matplotlib မှ [ax.twinx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html) ကိုအသုံးပြုပါ။ Twinx သည် x axis ကိုမျှဝေပြီး y axis နှစ်ခုကိုဖော်ပြနိုင်သည်။ yield per colony နှင့် number of colonies ကို superimposed ဖော်ပြပါ:

```python
fig, ax = plt.subplots(figsize=(12,6))
lineplot = sns.lineplot(x=honey['year'], y=honey['numcol'], data=honey, 
                        label = 'Number of bee colonies', legend=False)
sns.despine()
plt.ylabel('# colonies')
plt.title('Honey Production Year over Year');

ax2 = ax.twinx()
lineplot2 = sns.lineplot(x=honey['year'], y=honey['yieldpercol'], ax=ax2, color="r", 
                         label ='Yield per colony', legend=False) 
sns.despine(right=False)
plt.ylabel('colony yield')
ax.figure.legend();
```
![superimposed plots](../../../../3-Data-Visualization/12-visualization-relationships/images/dual-line.png)

၂၀၀၃ ခုနှစ်အနီးတွင်ထူးထူးခြားခြားပေါ်လွင်သောအရာမရှိသော်လည်း၊ ဒီသင်ခန်းစာကိုအနည်းငယ်ပျော်ရွှင်စေသောအချက်တစ်ခုဖြင့်အဆုံးသတ်နိုင်ပါတယ် - colonies အရေအတွက်သည်လျော့နည်းနေသော်လည်း၊ yield per colony လျော့နည်းနေသည့်အချိန်တွင် colonies အရေအတွက်သည်တည်ငြိမ်နေသည်။

ပျားများအားပေးပါ!

🐝❤️
## 🚀 စိန်ခေါ်မှု

ဒီသင်ခန်းစာမှာ၊ scatterplots နှင့် line grids ၏အခြားအသုံးများအကြောင်း၊ facet grids အပါအဝင်၊ ပိုမိုလေ့လာခဲ့ပါတယ်။ သင်ယခင်သင်ခန်းစာများတွင်အသုံးပြုခဲ့သော dataset တစ်ခုကိုအသုံးပြု၍ facet grid တစ်ခုဖန်တီးရန်ကိုယ်တိုင်စိန်ခေါ်ပါ။ ဤနည်းလမ်းများကိုအသုံးပြု၍ grid များဖန်တီးရန်အချိန်ကြာမြင့်မှုနှင့် grid အရေအတွက်ကိုသတိထားရန်လိုအပ်မှုကိုမှတ်သားပါ။

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/)

## ပြန်လည်သုံးသပ်ခြင်းနှင့် ကိုယ်တိုင်လေ့လာခြင်း

Line plots များသည်ရိုးရှင်းသော်လည်းအလွန်ရှုပ်ထွေးနိုင်သည်။ [Seaborn documentation](https://seaborn.pydata.org/generated/seaborn.lineplot.html) တွင်ဖော်ပြထားသော line charts ဖန်တီးနည်းများအကြောင်းပိုမိုလေ့လာပါ။ ဒီသင်ခန်းစာတွင်ဖန်တီးခဲ့သော line charts များကို documentation တွင်ဖော်ပြထားသောနည်းလမ်းများဖြင့်တိုးတက်အောင်လုပ်ကြည့်ပါ။
## လုပ်ငန်း

[Dive into the beehive](assignment.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။