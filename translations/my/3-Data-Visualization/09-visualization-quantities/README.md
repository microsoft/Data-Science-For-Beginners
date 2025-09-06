<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a49d78e32e280c410f04e5f2a2068e77",
  "translation_date": "2025-09-05T20:18:57+00:00",
  "source_file": "3-Data-Visualization/09-visualization-quantities/README.md",
  "language_code": "my"
}
-->
# အရေအတွက်များကို ရှင်းလင်းဖော်ပြခြင်း

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| အရေအတွက်များကို ရှင်းလင်းဖော်ပြခြင်း - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

ဒီသင်ခန်းစာမှာ Python libraries များကို အသုံးပြုပြီး အရေအတွက်ဆိုင်ရာ အထူးစိတ်ဝင်စားဖွယ် ရှင်းလင်းဖော်ပြချက်များကို ဖန်တီးပုံကို လေ့လာပါမည်။ Minnesota ရှိ ငှက်များအကြောင်းကို ရှင်းလင်းထားသော dataset ကို အသုံးပြု၍ ဒေသတွင်း သဘာဝတောရိုင်းအကြောင်း စိတ်ဝင်စားဖွယ် အချက်အလက်များကို သင်လေ့လာနိုင်ပါသည်။

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/16)

## Matplotlib ဖြင့် အတောင်ပံအကျယ်ကို ကြည့်ရှုခြင်း

ရိုးရှင်းပြီး ခက်ခဲသော အမျိုးမျိုးသော ပုံစံများနှင့် ဇယားများ ဖန်တီးရန် အထူးကောင်းမွန်သော library တစ်ခုမှာ [Matplotlib](https://matplotlib.org/stable/index.html) ဖြစ်သည်။ အထွေထွေအားဖြင့်၊ ဒီ library များကို အသုံးပြု၍ ဒေတာကို ဇယားပုံဖော်ခြင်းလုပ်ငန်းစဉ်မှာ dataframe ရဲ့ သင်ရည်ရွယ်ထားသော အပိုင်းများကို ရွေးချယ်ခြင်း၊ ဒေတာကို ပြောင်းလဲမှုများ ပြုလုပ်ခြင်း၊ x-axis နှင့် y-axis တန်ဖိုးများကို သတ်မှတ်ခြင်း၊ ဘယ်လိုဇယားကို ဖော်ပြမည်ဆိုတာ ဆုံးဖြတ်ခြင်း၊ ပြီးတော့ ဇယားကို ဖော်ပြခြင်းတို့ ပါဝင်သည်။ Matplotlib မှာ visualization အမျိုးမျိုးကို ပေးစွမ်းနိုင်သော်လည်း၊ ဒီသင်ခန်းစာအတွက် အရေအတွက်ကို ရှင်းလင်းဖော်ပြရန် သင့်တော်သော line charts, scatterplots, နှင့် bar plots များကို အဓိကထားပါမည်။

> ✅ သင့်ဒေတာရဲ့ ဖွဲ့စည်းပုံနှင့် သင်ပြောလိုသော အကြောင်းအရာကို သင့်တော်သော ဇယားကို အသုံးပြုပါ။
> - အချိန်အတွင်း အလားအလာကို ခွဲခြားရန်: line
> - တန်ဖိုးများကို နှိုင်းယှဉ်ရန်: bar, column, pie, scatterplot
> - အပိုင်းများသည် တစ်ခုလုံးနှင့် ဘယ်လိုဆက်စပ်နေသည်ကို ဖော်ပြရန်: pie
> - ဒေတာ၏ ဖြန့်ဝေမှုကို ဖော်ပြရန်: scatterplot, bar
> - အလားအလာကို ဖော်ပြရန်: line, column
> - တန်ဖိုးများအကြား ဆက်နွယ်မှုကို ဖော်ပြရန်: line, scatterplot, bubble

သင့်မှာ dataset ရှိပြီး အကြောင်းအရာတစ်ခုစီမှာ ဘယ်လောက်ရှိသည်ကို သိလိုပါက၊ ပထမဦးဆုံးလုပ်ဆောင်ရမည့်အလုပ်မှာ ဒေတာတန်ဖိုးများကို စစ်ဆေးခြင်းဖြစ်ပါသည်။

✅ Matplotlib အတွက် 'cheat sheets' ကောင်းများကို [ဒီမှာ](https://matplotlib.org/cheatsheets/cheatsheets.pdf) ရနိုင်ပါသည်။

## ငှက်အတောင်ပံအကျယ်တန်ဖိုးများအတွက် line plot တစ်ခု ဖန်တီးပါ

ဒီသင်ခန်းစာ folder ရဲ့ root မှာရှိတဲ့ `notebook.ipynb` ဖိုင်ကို ဖွင့်ပြီး cell တစ်ခု ထည့်ပါ။

> Note: ဒေတာကို ဒီ repo ရဲ့ root မှာရှိတဲ့ `/data` folder မှာ သိမ်းထားပါသည်။

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```  
ဒီဒေတာမှာ စာသားနှင့် နံပါတ်များရောနှောထားသည်။

|      | Name                         | ScientificName         | Category              | Order        | Family   | Genus       | ConservationStatus | MinLength | MaxLength | MinBodyMass | MaxBodyMass | MinWingspan | MaxWingspan |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

ငှက်များရဲ့ အတောင်ပံအကျယ်အမြင့်တန်ဖိုးကို ရှင်းလင်းဖော်ပြရန် ရိုးရှင်းသော line plot တစ်ခုကို စတင်ဖန်တီးပါ။

```python
wingspan = birds['MaxWingspan'] 
wingspan.plot()
```  
![Max Wingspan](../../../../3-Data-Visualization/09-visualization-quantities/images/max-wingspan-02.png)

သင်ဘာတွေ ချက်ချင်းသတိထားမိပါသလဲ? အနည်းဆုံး outlier တစ်ခုရှိသလိုပဲ - အတောင်ပံအကျယ်တန်ဖိုးက တော်တော်လေး ထူးဆန်းပါတယ်! 2300 စင်တီမီတာအတောင်ပံအကျယ်ဆိုတာ 23 မီတာလောက်ရှိတယ် - Minnesota မှာ Pterodactyls တွေ လှည့်လည်နေပါသလား? စစ်ဆေးကြည့်ရအောင်။

Excel မှာ sort လုပ်ပြီး outliers တွေကို အလွယ်တကူရှာဖွေနိုင်သော်လည်း၊ visualization လုပ်ငန်းစဉ်ကို ဇယားအတွင်းမှ ဆက်လက်လုပ်ဆောင်ပါ။

x-axis မှာ ငှက်အမျိုးအစားများကို ဖော်ပြရန် label များထည့်ပါ:

```
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.xticks(rotation=45)
x = birds['Name'] 
y = birds['MaxWingspan']

plt.plot(x, y)

plt.show()
```  
![wingspan with labels](../../../../3-Data-Visualization/09-visualization-quantities/images/max-wingspan-labels-02.png)

label များကို 45 ဒီဂရီလှည့်ထားသော်လည်း၊ ဖတ်ရန် အလွန်များနေပါသည်။ အခြားနည်းလမ်းကို စမ်းကြည့်ရအောင် - outliers များကိုသာ label လုပ်ပြီး ဇယားအတွင်းမှာ label များကို ထည့်ပါ။ scatter chart ကို အသုံးပြု၍ label များအတွက် နေရာပိုမိုရနိုင်ပါသည်။

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)

for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    plt.plot(x, y, 'bo')
    if birds['MaxWingspan'][i] > 500:
        plt.text(x, y * (1 - 0.05), birds['Name'][i], fontsize=12)
    
plt.show()
```  
ဒီမှာ ဘာဖြစ်နေလဲ? သင် `tick_params` ကို အသုံးပြု၍ အောက်ဆုံး label များကို ဖျောက်ပြီး၊ birds dataset ကို loop လုပ်ခဲ့ပါသည်။ `bo` ကို အသုံးပြု၍ အပြာရောင်အဝိုင်းလေးများဖြင့် ဇယားကို plot လုပ်ပြီး၊ အတောင်ပံအကျယ်အမြင့် 500 ထက်ပိုသော ငှက်များကို စစ်ဆေးကာ dot အနီးမှာ label ကို ဖော်ပြခဲ့ပါသည်။ label များကို y axis မှာ အနည်းငယ် offset လုပ်ပြီး (`y * (1 - 0.05)`) ငှက်အမည်ကို label အဖြစ် အသုံးပြုခဲ့သည်။

သင်ဘာတွေ ရှာဖွေမိပါသလဲ?

![outliers](../../../../3-Data-Visualization/09-visualization-quantities/images/labeled-wingspan-02.png)

## သင့်ဒေတာကို Filter လုပ်ပါ

Bald Eagle နှင့် Prairie Falcon တို့သည် အတော်လေးကြီးမားသော ငှက်များဖြစ်နိုင်သော်လည်း၊ အတောင်ပံအကျယ်အမြင့်မှာ အပို `0` တစ်ခု ထည့်ထားသော typo ဖြစ်နိုင်ပါသည်။ Bald Eagle ရဲ့ အတောင်ပံအကျယ် 25 မီတာရှိတယ်ဆိုရင်၊ ကျေးဇူးပြု၍ ကျွန်ုပ်တို့ကို အသိပေးပါ! ဒီ outliers နှစ်ခုမပါသော dataframe အသစ်တစ်ခု ဖန်တီးပါ:

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)
for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    if birds['Name'][i] not in ['Bald eagle', 'Prairie falcon']:
        plt.plot(x, y, 'bo')
plt.show()
```  

outliers များကို ဖယ်ရှားခြင်းအားဖြင့်၊ သင့်ဒေတာသည် ပိုမိုညီညွတ်ပြီး နားလည်ရလွယ်ကူလာပါသည်။

![scatterplot of wingspans](../../../../3-Data-Visualization/09-visualization-quantities/images/scatterplot-wingspan-02.png)

အတောင်ပံအကျယ်အမြင့်အရ dataset ကို သန့်စင်ပြီးနောက်၊ ငှက်များအကြောင်းကို ပိုမိုရှာဖွေပါ။

line နှင့် scatter plots များသည် ဒေတာတန်ဖိုးများနှင့် ၎င်းတို့၏ ဖြန့်ဝေမှုကို ဖော်ပြနိုင်သော်လည်း၊ dataset ရဲ့ inherent values အကြောင်းကို စဉ်းစားလိုက်ပါ။ သင်အောက်ပါအရေအတွက်ဆိုင်ရာမေးခွန်းများကို visualizations ဖန်တီးပြီး ဖြေရှင်းနိုင်ပါသည်။

> ငှက်အမျိုးအစားများ ဘယ်လောက်ရှိပြီး၊ ၎င်းတို့ရဲ့ အရေအတွက်များ ဘယ်လောက်ရှိသလဲ?  
> ငှက်များ extinction, endangered, rare, common ဖြစ်မှု ဘယ်လောက်ရှိသလဲ?  
> Linnaeus ရဲ့ terminology အရ genus နှင့် orders များ ဘယ်လောက်ရှိသလဲ?  

## Bar charts ကို လေ့လာပါ

Bar charts များသည် ဒေတာကို အုပ်စုဖွဲ့ဖော်ပြရန် အလွန်အသုံးဝင်သည်။ dataset ရဲ့ ငှက်အမျိုးအစားများကို လေ့လာပြီး အများဆုံးရှိသောအမျိုးအစားကို ကြည့်ရှုပါ။

notebook ဖိုင်တွင် ရိုးရှင်းသော bar chart တစ်ခု ဖန်တီးပါ။

✅ အရင်ပိုင်းက outlier ငှက်နှစ်ကောင်ကို ဖယ်ရှားခြင်း၊ ၎င်းတို့ရဲ့ typo ကို ပြင်ဆင်ခြင်း၊ သို့မဟုတ် wingspan values မပေါ်မူတည်သော ဒီလေ့လာမှုများအတွက် ၎င်းတို့ကို ထားရှိခြင်းတို့ကို ရွေးချယ်နိုင်သည်။

bar chart တစ်ခု ဖန်တီးလိုပါက၊ သင်အာရုံစိုက်လိုသော ဒေတာကို ရွေးချယ်နိုင်ပါသည်။ Bar charts များကို raw data မှ ဖန်တီးနိုင်သည်။

```python
birds.plot(x='Category',
        kind='bar',
        stacked=True,
        title='Birds of Minnesota')

```  
![full data as a bar chart](../../../../3-Data-Visualization/09-visualization-quantities/images/full-data-bar-02.png)

သို့သော် ဒီ bar chart က ဖတ်ရှုရန် မဖြစ်နိုင်လောက်အောင် များနေသည်။ သင် plot လုပ်လိုသော ဒေတာကိုသာ ရွေးချယ်ရန် လိုအပ်သည်။ ငှက်အမျိုးအစားအပေါ်မူတည်၍ အရှည်ကို ကြည့်ရှုပါ။

သင့်ဒေတာကို ငှက်အမျိုးအစားကိုသာ ထည့်သွင်းရန် filter လုပ်ပါ။

✅ သင် Pandas ကို အသုံးပြု၍ ဒေတာကို စီမံပြီး၊ Matplotlib ကို ဇယားဖော်ပြရန် အသုံးပြုပါ။

အမျိုးအစားများ များစွာရှိသည့်အတွက်၊ ဒီဇယားကို vertical display လုပ်ပြီး၊ height ကို တိုင်းတာကာ ဒေတာအားလုံးကို ထည့်သွင်းပါ:

```python
category_count = birds.value_counts(birds['Category'].values, sort=True)
plt.rcParams['figure.figsize'] = [6, 12]
category_count.plot.barh()
```  
![category and length](../../../../3-Data-Visualization/09-visualization-quantities/images/category-counts-02.png)

ဒီ bar chart က ငှက်အမျိုးအစားတစ်ခုစီရဲ့ အရေအတွက်ကို ကောင်းစွာဖော်ပြထားသည်။ Minnesota မှာ Ducks/Geese/Waterfowl အမျိုးအစားရှိသော ငှက်များ အများဆုံးဖြစ်သည်ကို ချက်ချင်းမြင်နိုင်သည်။ Minnesota သည် '10,000 ရေကန်များ၏ မြေ' ဖြစ်သောကြောင့်၊ ဒီအချက်အလက်သည် အံ့ဩစရာမဟုတ်ပါ။

✅ ဒီ dataset ကို အသုံးပြု၍ အခြား count များကို စမ်းကြည့်ပါ။ သင်အံ့ဩစရာတစ်ခုခု ရှာဖွေမိပါသလား?

## ဒေတာများကို နှိုင်းယှဉ်ခြင်း

Grouped data များကို နှိုင်းယှဉ်ရန် axes အသစ်များ ဖန်တီးနိုင်သည်။ ငှက်အမျိုးအစားအပေါ်မူတည်၍ MaxLength ကို နှိုင်းယှဉ်ကြည့်ပါ:

```python
maxlength = birds['MaxLength']
plt.barh(y=birds['Category'], width=maxlength)
plt.rcParams['figure.figsize'] = [6, 12]
plt.show()
```  
![comparing data](../../../../3-Data-Visualization/09-visualization-quantities/images/category-length-02.png)

ဒီမှာ အံ့ဩစရာမရှိပါ: hummingbirds တွေက Pelicans သို့မဟုတ် Geese တွေထက် MaxLength အနည်းဆုံးရှိသည်။ ဒေတာက အလွယ်တကူ အဓိပ္ပာယ်ရနိုင်တာကောင်းပါတယ်!

Bar charts များကို ဒေတာများကို superimpose လုပ်ခြင်းအားဖြင့် ပိုမိုစိတ်ဝင်စားဖွယ် ဖန်တီးနိုင်သည်။ Minimum နှင့် Maximum Length ကို ငှက်အမျိုးအစားတစ်ခုစီမှာ superimpose လုပ်ကြည့်ပါ:

```python
minLength = birds['MinLength']
maxLength = birds['MaxLength']
category = birds['Category']

plt.barh(category, maxLength)
plt.barh(category, minLength)

plt.show()
```  
ဒီဇယားမှာ၊ Minimum Length နှင့် Maximum Length တစ်ခုစီရဲ့ range ကို ငှက်အမျိုးအစားတစ်ခုစီအပေါ်မှာ မြင်နိုင်သည်။ ဒီဒေတာအရ၊ ငှက်က càng ကြီးမားလျှင်၊ length range càng ကြီးမားသည်ကို သင်ယုံကြည်စွာပြောနိုင်သည်။ စိတ်ဝင်စားဖွယ်ကောင်းပါတယ်!

![superimposed values](../../../../3-Data-Visualization/09-visualization-quantities/images/superimposed-02.png)

## 🚀 စိန်ခေါ်မှု

ဒီငှက် dataset က ecosystem တစ်ခုအတွင်းရှိ ငှက်အမျိုးအစားများအကြောင်း အချက်အလက်များစွာကို ပေးစွမ်းပါသည်။ အင်တာနက်ပေါ်မှာ ရှာဖွေပြီး အခြားငှက်ဆိုင်ရာ datasets များကို ရှာဖွေပါ။ ဒီငှက်များအကြောင်းကို ဇယားများနှင့် ဂရပ်များ ဖန်တီးပြီး သင်မသိခဲ့သော အချက်အလက်များကို ရှာဖွေပါ။

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/17)

## ပြန်လည်သုံးသပ်ခြင်းနှင့် ကိုယ်တိုင်လေ့လာခြင်း

ဒီပထမဆုံးသင်ခန်းစာက Matplotlib ကို အသုံးပြု၍ အရေအတွက်များကို ရှင်းလင်းဖော်ပြပုံအကြောင်း အချက်အလက်များကို ပေးခဲ့သည်။ visualization အတွက် datasets များကို အသုံးပြုရန် အခြားနည်းလမ်းများကို လေ့လာပါ။ [Plotly](https://github.com/plotly/plotly.py) သည် ဒီသင်ခန်းစာများတွင် မဖော်ပြမည့် library တစ်ခုဖြစ်သဖြင့်၊ ၎င်းက ဘာတွေ ပေးစွမ်းနိုင်သည်ကို ကြည့်ရှုပါ။

## လုပ်ငန်းတာဝန်

[Lines, Scatters, and Bars](assignment.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် ရှုလေ့လာသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲသုံးစားမှု သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။