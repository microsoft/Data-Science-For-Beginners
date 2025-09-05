<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "02ce904bc1e2bfabb7dc05c25aae375c",
  "translation_date": "2025-09-05T05:22:29+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "my"
}
-->
# အနံ့အကျယ်များကို မြင်သာအောင် ဖော်ပြခြင်း

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| အနံ့အကျယ်များကို မြင်သာအောင် ဖော်ပြခြင်း - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

ယခင် သင်ခန်းစာတွင် Minnesota ရှိ ငှက်များအကြောင်း ဒေတာအချို့ကို သင်လေ့လာခဲ့ပါသည်။ သင်သည် အနံ့အကျယ်များကို မြင်သာအောင် ဖော်ပြခြင်းဖြင့် အမှားပါသော ဒေတာများကို ရှာဖွေခဲ့ပြီး ငှက်အမျိုးအစားများ၏ အရှည်အမြင့်အများဆုံးအကြား ကွာခြားချက်များကို ကြည့်ရှုခဲ့ပါသည်။

## [Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## ငှက်များ၏ ဒေတာကို လေ့လာခြင်း

ဒေတာကို အနက်ရှိုင်းစွာ လေ့လာရန် နောက်ထပ်နည်းလမ်းတစ်ခုမှာ ဒေတာကို အချိုးအစားအနေနှင့် (distribution) ကြည့်ရှုခြင်းဖြစ်သည်။ ဥပမာအားဖြင့် Minnesota ရှိ ငှက်များ၏ အမြင့်ဆုံးတောင်ပံအကျယ် (maximum wingspan) သို့မဟုတ် အမြင့်ဆုံးကိုယ်အလေးချိန် (maximum body mass) အကြောင်းကို သိလိုပါက ဒေတာ၏ အချိုးအစားကို လေ့လာနိုင်ပါသည်။

ဒီ ဒေတာအချိုးအစားများအကြောင်း အချက်အလက်အချို့ကို ရှာဖွေကြည့်ရအောင်။ ဒီ သင်ခန်းစာဖိုလ်ဒါ၏ အရင်းအမြစ်တွင်ရှိသော _notebook.ipynb_ ဖိုင်တွင် Pandas, Matplotlib နှင့် သင့်ဒေတာကို import လုပ်ပါ။

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | Name                         | ScientificName         | Category              | Order        | Family   | Genus       | ConservationStatus | MinLength | MaxLength | MinBodyMass | MaxBodyMass | MinWingspan | MaxWingspan |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

ယေဘူယျအားဖြင့် ဒေတာကို အချိုးအစားအနေနှင့် မြင်သာအောင် ဖော်ပြရန် scatter plot ကို အသုံးပြုနိုင်ပါသည်။ ယခင် သင်ခန်းစာတွင် ကျွန်ုပ်တို့ ပြုလုပ်ခဲ့သည့်အတိုင်းပါ:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![max length per order](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

ဤအချက်အလက်သည် ငှက်အမျိုးအစား (Order) တစ်ခုချင်းစီအတွက် ကိုယ်အရှည်အမြင့်၏ အချိုးအစားကို ယေဘူယျအားဖြင့် ဖော်ပြပေးသည်။ သို့သော် ဒေတာ၏ အမှန်တကယ် အချိုးအစားကို ဖော်ပြရန် အကောင်းဆုံးနည်းလမ်းမဟုတ်ပါ။ အဲဒီအလုပ်ကို Histogram ဖန်တီးခြင်းဖြင့် ပြုလုပ်နိုင်ပါသည်။

## Histogram နှင့် အလုပ်လုပ်ခြင်း

Matplotlib သည် Histogram အသုံးပြု၍ ဒေတာအချိုးအစားကို မြင်သာအောင် ဖော်ပြရန် အကောင်းဆုံးနည်းလမ်းများကို ပေးသည်။ ဒီအမျိုးအစား chart သည် bar chart နှင့် ဆင်တူပြီး bar များ၏ မြင့်တက်နှင့် ကျဆင်းမှုမှတစ်ဆင့် ဒေတာအချိုးအစားကို မြင်နိုင်သည်။ Histogram ဖန်တီးရန် သင်Numeric ဒေတာလိုအပ်ပါသည်။ Histogram ဖန်တီးရန် chart ကို 'hist' အမျိုးအစားအဖြစ် သတ်မှတ်ပြီး ဖန်တီးနိုင်ပါသည်။ ဤ chart သည် MaxBodyMass အတွက် ဒေတာ၏ အချိုးအစားကို ဖော်ပြသည်။ ဒေတာ array ကို bin များသို့ ခွဲခြားခြင်းဖြင့် ဒေတာ၏ အချိုးအစားကို ဖော်ပြနိုင်သည်။

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![distribution over the entire dataset](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

သင်မြင်နိုင်သည့်အတိုင်း ဒီ dataset တွင်ပါဝင်သော 400+ ငှက်များ၏ အများစုသည် Max Body Mass 2000 အောက်တွင် ရှိသည်။ `bins` parameter ကို 30 အဖြစ် ပြောင်းလဲခြင်းဖြင့် ဒေတာအကြောင်းကို ပိုမိုနက်ရှိုင်းစွာ သိရှိနိုင်ပါသည်။

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![distribution over the entire dataset with larger bins param](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

ဤ chart သည် အချိုးအစားကို ပိုမိုအသေးစိတ် ဖော်ပြပေးသည်။ ပိုမိုလက်ဝါးကပ်သော chart ကို ဖန်တီးရန် သတ်မှတ်ထားသော range အတွင်းရှိ ဒေတာကိုသာ ရွေးချယ်ပါ:

ကိုယ်အလေးချိန် 60 အောက်ရှိ ငှက်များကို filter လုပ်ပြီး `bins` ကို 40 အဖြစ် ပြပါ:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![filtered histogram](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ အခြား filter များနှင့် ဒေတာအချက်အလက်များကို စမ်းကြည့်ပါ။ ဒေတာ၏ အပြည့်အစုံအချိုးအစားကို မြင်ရန် `['MaxBodyMass']` filter ကို ဖယ်ရှားပြီး label ထည့်ထားသော အချိုးအစားများကို ပြပါ။

Histogram သည် အရောင်နှင့် label အဆင်ပြေမှုများကိုလည်း စမ်းသပ်နိုင်ပါသည်။

2D histogram ဖန်တီးပြီး အချိုးအစားနှစ်ခုအကြား ဆက်နွယ်မှုကို နှိုင်းယှဉ်ကြည့်ပါ။ `MaxBodyMass` နှင့် `MaxLength` ကို နှိုင်းယှဉ်ကြည့်ရအောင်။ Matplotlib သည် အလင်းရောင်များကို အသုံးပြု၍ ဆက်နွယ်မှုကို ဖော်ပြရန် built-in နည်းလမ်းကို ပေးသည်။

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
ဤ chart တွင် အချိုးအစားနှစ်ခုအကြား ဆက်နွယ်မှုရှိသည်ကို မြင်နိုင်ပြီး တစ်နေရာမှာ အထူးအားကောင်းသော ဆက်နွယ်မှုကို တွေ့နိုင်သည်။

![2D plot](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

Histogram များသည် Numeric ဒေတာအတွက် အလွန်ကောင်းမွန်စွာ အလုပ်လုပ်သည်။ Text-based ဒေတာအချိုးအစားကို မြင်ရန်လိုပါက ဘာလုပ်ရမလဲ?

## Text-based ဒေတာအချိုးအစားများကို လေ့လာခြင်း

ဤ dataset တွင် ငှက်အမျိုးအစား၊ genus, species, family နှင့် conservation status အကြောင်း အချက်အလက်များပါဝင်သည်။ conservation status အကြောင်းကို လေ့လာကြည့်ရအောင်။ ငှက်များ၏ conservation status အချိုးအစားကို ဘယ်လိုဖြစ်နေသလဲ?

> ✅ Dataset တွင် conservation status ကို ဖော်ပြရန် အတိုကောက်များကို အသုံးပြုထားသည်။ ဤအတိုကောက်များသည် [IUCN Red List Categories](https://www.iucnredlist.org/) မှ ရရှိသည်။
> 
> - CR: အလွန်အန္တရာယ်ရှိသော
> - EN: အန္တရာယ်ရှိသော
> - EX: မျိုးတုံးသွားသော
> - LC: အနည်းဆုံး စိုးရိမ်ရသော
> - NT: အနီးကပ် စိုးရိမ်ရသော
> - VU: အန္တရာယ်ရှိနိုင်သော

ဤအချက်အလက်များသည် text-based ဖြစ်သောကြောင့် histogram ဖန်တီးရန် transform လုပ်ရန်လိုအပ်ပါသည်။ filteredBirds dataframe ကို အသုံးပြု၍ conservation status ကို Minimum Wingspan နှင့်အတူ ဖော်ပြပါ။ သင်ဘာတွေ့ရမလဲ?

```python
x1 = filteredBirds.loc[filteredBirds.ConservationStatus=='EX', 'MinWingspan']
x2 = filteredBirds.loc[filteredBirds.ConservationStatus=='CR', 'MinWingspan']
x3 = filteredBirds.loc[filteredBirds.ConservationStatus=='EN', 'MinWingspan']
x4 = filteredBirds.loc[filteredBirds.ConservationStatus=='NT', 'MinWingspan']
x5 = filteredBirds.loc[filteredBirds.ConservationStatus=='VU', 'MinWingspan']
x6 = filteredBirds.loc[filteredBirds.ConservationStatus=='LC', 'MinWingspan']

kwargs = dict(alpha=0.5, bins=20)

plt.hist(x1, **kwargs, color='red', label='Extinct')
plt.hist(x2, **kwargs, color='orange', label='Critically Endangered')
plt.hist(x3, **kwargs, color='yellow', label='Endangered')
plt.hist(x4, **kwargs, color='green', label='Near Threatened')
plt.hist(x5, **kwargs, color='blue', label='Vulnerable')
plt.hist(x6, **kwargs, color='gray', label='Least Concern')

plt.gca().set(title='Conservation Status', ylabel='Min Wingspan')
plt.legend();
```

![wingspan and conservation collation](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

Minimum Wingspan နှင့် conservation status အကြား ဆက်နွယ်မှုကောင်းကောင်း မရှိသလိုပုံရသည်။ dataset ၏ အခြား element များကို ဒီနည်းလမ်းဖြင့် စမ်းကြည့်ပါ။ အခြား filter များကိုလည်း စမ်းကြည့်ပါ။ သင် ဆက်နွယ်မှုတစ်ခုခုကို တွေ့နိုင်ပါသလား?

## Density plots

ယခင်တွင် ကြည့်ရှုခဲ့သော histogram များသည် 'stepped' ဖြစ်ပြီး arc အနေနှင့် မပြေပြစ်သောပုံစံဖြစ်သည်ကို သတိထားမိနိုင်ပါသည်။ arc ပုံစံဖြင့် ပိုမိုပြေပြစ်သော density chart ကို ဖော်ပြရန် density plot ကို စမ်းကြည့်နိုင်ပါသည်။

Density plot များနှင့် အလုပ်လုပ်ရန် [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) ဆိုသော plotting library အသစ်ကို လေ့လာပါ။

Seaborn ကို load လုပ်ပြီး basic density plot တစ်ခုကို စမ်းကြည့်ပါ:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![Density plot](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

ဤ plot သည် Minimum Wingspan data အတွက် ယခင် histogram ကို echo လုပ်ပေးသည်။ သို့သော် ပိုမိုပြေပြစ်သောပုံစံဖြစ်သည်။ Seaborn ၏ documentation အရ "Histogram နှင့် နှိုင်းယှဉ်ပါက KDE သည် ပိုမိုရှင်းလင်းပြီး အဓိပ္ပာယ်ရှိသော plot ကို ဖန်တီးပေးနိုင်သည်။ သို့သော် underlying distribution bounded မဖြစ်ပါက distortion ဖြစ်နိုင်သည်။ Histogram နှင့်တူပင် representation quality သည် smoothing parameters ရွေးချယ်မှုကောင်းမွန်မှုအပေါ် မူတည်သည်။" [source](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) အဆိုအရ outliers များသည် အမြဲ chart များကို မကောင်းစေမည်ဖြစ်သည်။

ယခင်တွင် ဖန်တီးခဲ့သော jagged MaxBodyMass line ကို ပြေပြစ်စွာ ဖော်ပြလိုပါက ဒီနည်းလမ်းဖြင့် ပြန်ဖန်တီးနိုင်ပါသည်။

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![smooth bodymass line](../../../../3-Data-Visualization/10-visualization-distributions/images/density2.png)

Smooth ဖြစ်သော်လည်း အလွန်ပြေပြစ်မဖြစ်စေရန် `bw_adjust` parameter ကို ပြင်ဆင်ပါ:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![less smooth bodymass line](../../../../3-Data-Visualization/10-visualization-distributions/images/density3.png)

✅ ဒီအမျိုးအစား plot အတွက် ရရှိနိုင်သော parameters များကို ဖတ်ရှုပြီး စမ်းကြည့်ပါ!

ဤ chart အမျိုးအစားသည် အလွန်ရှင်းလင်းသော visualizations ကို ဖန်တီးပေးသည်။ ဥပမာအားဖြင့် ငှက်အမျိုးအစား (Order) တစ်ခုချင်းစီအတွက် max body mass density ကို ဖော်ပြနိုင်သည်။

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![bodymass per order](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

တစ်ခုချင်းစီ plot များကို map လုပ်ပြီး chart တစ်ခုထဲတွင် variables များစွာကို ဖော်ပြနိုင်သည်။ ငှက်၏ MaxLength နှင့် MinLength ကို conservation status နှင့် နှိုင်းယှဉ်ကြည့်ပါ:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![multiple densities, superimposed](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

'Vulnerable' ငှက်များ၏ အရှည်အချိုးအစားအကြောင်း cluster သည် အဓိပ္ပာယ်ရှိမရှိကို သုတေသနလုပ်ရန် တန်ဖိုးရှိနိုင်ပါသည်။

## 🚀 စိန်ခေါ်မှု

Histogram များသည် scatterplots, bar charts, သို့မဟုတ် line charts ထက် ပိုမိုရှုပ်ထွေးသော chart အမျိုးအစားဖြစ်သည်။ Histogram များကို အသုံးပြုထားသော ကောင်းမွန်သော ဥပမာများကို အင်တာနက်တွင် ရှာဖွေပါ။ Histogram များကို ဘယ်လိုအသုံးပြုထားသည်၊ ဘာကို ဖော်ပြပေးသည်၊ ဘယ်လောကများတွင် အသုံးပြုလေ့ရှိသည်ဆိုတာကို လေ့လာပါ။

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/)

## ပြန်လည်သုံးသပ်ခြင်းနှင့် ကိုယ်တိုင်လေ့လာခြင်း

ဤသင်ခန်းစာတွင် Matplotlib ကို အသုံးပြုပြီး Seaborn ကို စတင်အသုံးပြုကာ ပိုမိုရှုပ်ထွေးသော chart များကို ဖော်ပြခဲ့ပါသည်။ Seaborn တွင် `kdeplot` အကြောင်း သုတေသနလုပ်ပါ။ "continuous probability density curve in one or more dimensions" ဖြစ်သည်။ [documentation](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) ကို ဖတ်ရှုကာ ၎င်း၏ အလုပ်လုပ်ပုံကို နားလည်ပါ။

## လုပ်ငန်း

[သင်၏ ကျွမ်းကျင်မှုကို အသုံးချပါ](assignment.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားများ သို့မဟုတ် အဓိပ္ပာယ်မှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။