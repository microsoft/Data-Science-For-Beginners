<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "69b32b6789a91f796ebc7a02f5575e03",
  "translation_date": "2025-09-05T05:20:22+00:00",
  "source_file": "3-Data-Visualization/09-visualization-quantities/README.md",
  "language_code": "my"
}
-->
# အရေအတွက်များကို ရှင်းလင်းဖော်ပြခြင်း

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| အရေအတွက်များကို ရှင်းလင်းဖော်ပြခြင်း - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

ဒီသင်ခန်းစာမှာ Python libraries တွေကို အသုံးပြုပြီး အရေအတွက်ဆိုင်ရာ အထူးစိတ်ဝင်စားဖွယ် ရှင်းလင်းဖော်ပြချက်တွေ ဖန်တီးပုံကို လေ့လာပါမယ်။ Minnesota ရဲ့ ငှက်များအကြောင်း ရှင်းလင်းထားတဲ့ dataset ကို အသုံးပြုပြီး ဒေသတွင်း သဘာဝတောရိုင်းအကြောင်း စိတ်ဝင်စားဖွယ် အချက်အလက်များကို သိရှိနိုင်ပါမယ်။

## [Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## Matplotlib ဖြင့် အတောင်ပံအကျယ်ကို ကြည့်ရှုခြင်း

ရိုးရှင်းပြီး ခက်ခဲတဲ့ အမျိုးမျိုးသော plot နှင့် chart များ ဖန်တီးရန် အကောင်းဆုံး library တစ်ခုက [Matplotlib](https://matplotlib.org/stable/index.html) ဖြစ်ပါတယ်။ အထွေထွေအားဖြင့် ဒီ library တွေကို အသုံးပြုပြီး data ကို plot လုပ်တဲ့ လုပ်ငန်းစဉ်မှာ dataframe ရဲ့ target လုပ်လိုတဲ့ အပိုင်းတွေကို ရွေးချယ်ခြင်း၊ data ကို transform လုပ်ခြင်း၊ x-axis နဲ့ y-axis values တွေကို assign လုပ်ခြင်း၊ ဖော်ပြချင်တဲ့ plot အမျိုးအစားကို ဆုံးဖြတ်ခြင်း၊ နောက်ဆုံးမှာ plot ကို ဖော်ပြခြင်းတို့ ပါဝင်ပါတယ်။ Matplotlib က visualizations အမျိုးအစား အများကြီး ပေးထားပေမယ့် ဒီသင်ခန်းစာအတွက် အရေအတွက်ကို ရှင်းလင်းဖော်ပြဖို့ သင့်တော်တဲ့ line charts, scatterplots, နဲ့ bar plots တွေကို အဓိကထားပါမယ်။

> ✅ သင့် data ရဲ့ ဖွဲ့စည်းပုံနဲ့ ပြောပြချင်တဲ့ အကြောင်းအရာကို သင့်တော်တဲ့ chart ကို အသုံးပြုပါ။
> - အချိန်အတွင်းမှာ trend တွေကို ခွဲခြားဖော်ပြရန်: line
> - တန်ဖိုးတွေကို နှိုင်းယှဉ်ရန်: bar, column, pie, scatterplot
> - အစိတ်အပိုင်းတွေက တစ်ခုလုံးနဲ့ ဘယ်လိုဆက်စပ်နေသလဲဆိုတာ ဖော်ပြရန်: pie
> - data ရဲ့ distribution ကို ဖော်ပြရန်: scatterplot, bar
> - trend တွေကို ဖော်ပြရန်: line, column
> - တန်ဖိုးတွေကြား ဆက်စပ်မှုကို ဖော်ပြရန်: line, scatterplot, bubble

သင့်မှာ dataset ရှိပြီး အချို့သော item ရဲ့ အရေအတွက်ကို သိရှိဖို့လိုအပ်ရင် ပထမဆုံးလုပ်ဆောင်ရမယ့်အရာက အဲဒီ values တွေကို စစ်ဆေးဖို့ ဖြစ်ပါတယ်။

✅ Matplotlib အတွက် 'cheat sheets' အလွန်ကောင်းတဲ့ resource [ဒီမှာ](https://matplotlib.org/cheatsheets/cheatsheets.pdf) ရနိုင်ပါတယ်။

## ငှက်အတောင်ပံအကျယ်အတွက် line plot တစ်ခု ဖန်တီးပါ

ဒီသင်ခန်းစာ folder ရဲ့ root မှာရှိတဲ့ `notebook.ipynb` ဖိုင်ကို ဖွင့်ပြီး cell တစ်ခု ထည့်ပါ။

> Note: data ကို ဒီ repo ရဲ့ root မှာရှိတဲ့ `/data` folder မှာ သိမ်းထားပါတယ်။

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```
ဒီ data က text နဲ့ numbers တွေ ရောထားပါတယ်:

|      | Name                         | ScientificName         | Category              | Order        | Family   | Genus       | ConservationStatus | MinLength | MaxLength | MinBodyMass | MaxBodyMass | MinWingspan | MaxWingspan |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

ငှက်တွေ့ရတဲ့ အတောင်ပံအကျယ်အတွက် maximum value ကို basic line plot တစ်ခုနဲ့ စတင်ဖော်ပြပါ။

```python
wingspan = birds['MaxWingspan'] 
wingspan.plot()
```
![Max Wingspan](../../../../3-Data-Visualization/09-visualization-quantities/images/max-wingspan-02.png)

ဘာတွေကို ချက်ချင်းသတိထားမိပါသလဲ? အနည်းဆုံး outlier တစ်ခုရှိနေသလိုပဲ - အတောင်ပံအကျယ်က အလွန်ကြီးမားပါတယ်! 2300 စင်တီမီတာအတောင်ပံအကျယ်က 23 မီတာနဲ့ တူပါတယ် - Minnesota မှာ Pterodactyls တွေ လှည့်လည်နေပါသလား? စစ်ဆေးကြည့်ရအောင်။

Excel မှာ sort လုပ်ပြီး အဲဒီ outliers တွေကို အလွယ်တကူရှာဖွေနိုင်ပေမယ့် plot ထဲကနေ ဆက်လက်ရှင်းလင်းဖော်ပြခြင်းလုပ်ငန်းစဉ်ကို ဆက်လုပ်ပါ။

x-axis မှာ ငှက်အမျိုးအစားတွေကို label ထည့်ပါ:

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

label တွေကို 45 ဒီဂရီလှည့်ထားပေမယ့် ဖတ်ရှုရန် အလွန်ခက်ခဲနေပါတယ်။ အခြား strategy တစ်ခုကို စမ်းကြည့်ရအောင် - outliers တွေကိုသာ label လုပ်ပြီး chart ထဲမှာ label တွေကို ထည့်ပါ။ scatter chart ကို အသုံးပြုပြီး label တွေကို ထည့်ဖို့ နေရာပိုရနိုင်ပါတယ်:

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
ဒီမှာ ဘာဖြစ်နေလဲ? `tick_params` ကို အသုံးပြုပြီး အောက်ဆုံး label တွေကို ဖျောက်ထားပြီး birds dataset ကို loop လုပ်ထားပါတယ်။ `bo` ကို အသုံးပြုပြီး အပြာရောင်လုံးလေးတွေကို plot လုပ်ပြီး maximum wingspan 500 ထက်ပိုတဲ့ ငှက်တွေကို စစ်ဆေးပြီး dot ရဲ့ အနားမှာ label ထည့်ထားပါတယ်။ label တွေကို y axis မှာ နည်းနည်း offset လုပ်ထားပြီး ငှက်နာမည်ကို label အဖြစ် အသုံးပြုထားပါတယ်။

ဘာတွေကို ရှာဖွေမိပါသလဲ?

![outliers](../../../../3-Data-Visualization/09-visualization-quantities/images/labeled-wingspan-02.png)

## သင့် data ကို filter လုပ်ပါ

Bald Eagle နဲ့ Prairie Falcon ဟာ အလွန်ကြီးမားတဲ့ ငှက်တွေဖြစ်နိုင်ပေမယ့် maximum wingspan မှာ အပို `0` တစ်ခု ထည့်ထားတဲ့ typo ဖြစ်နိုင်ပါတယ်။ Bald Eagle ရဲ့ 25 မီတာအတောင်ပံအကျယ်ကို တွေ့ရင် ကျေးဇူးပြု၍ ကျွန်တော်တို့ကို အသိပေးပါ! ဒီ outliers နှစ်ခုမပါတဲ့ dataframe အသစ်တစ်ခု ဖန်တီးပါ:

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

outliers တွေကို ဖယ်ရှားပြီးနောက် သင့် data က ပိုပြီး cohesive နဲ့ နားလည်ရလွယ်ကူလာပါတယ်။

![scatterplot of wingspans](../../../../3-Data-Visualization/09-visualization-quantities/images/scatterplot-wingspan-02.png)

အတောင်ပံအကျယ်အတွက် data ကို သန့်စင်ပြီးနောက် ဒီငှက်တွေကို ပိုမိုလေ့လာကြည့်ရအောင်။

line နဲ့ scatter plots တွေက data values နဲ့ distribution အကြောင်းကို ဖော်ပြနိုင်ပေမယ့် dataset ရဲ့ inherent values တွေကို စဉ်းစားဖို့လိုပါတယ်။ အရေအတွက်ဆိုင်ရာ အောက်ပါမေးခွန်းတွေကို visualizations ဖန်တီးပြီး ဖြေရှင်းနိုင်ပါတယ်:

> ငှက်အမျိုးအစား ဘယ်လောက်ရှိပြီး အရေအတွက်ဘယ်လောက်ရှိသလဲ?
> ဘယ်ငှက်တွေ extinct, endangered, rare, common ဖြစ်သလဲ?
> Linnaeus ရဲ့ terminology အရ genus နဲ့ orders အမျိုးအစား ဘယ်လောက်ရှိသလဲ?

## Bar charts ကို လေ့လာပါ

Bar charts တွေက data groupings ကို ဖော်ပြဖို့ အလွန်အသုံးဝင်ပါတယ်။ dataset ထဲမှာရှိတဲ့ ငှက်အမျိုးအစားတွေကို လေ့လာပြီး အများဆုံးရှိတဲ့အမျိုးအစားကို ကြည့်ရှုရအောင်။

notebook ဖိုင်ထဲမှာ basic bar chart တစ်ခု ဖန်တီးပါ။

✅ အရင်ပိုင်းမှာ ရှာဖွေခဲ့တဲ့ outlier ငှက်နှစ်ကောင်ကို ဖယ်ရှားမလား၊ wingspan မှာ typo ကို ပြင်မလား၊ ဒါမှမဟုတ် ဒီ exercises တွေမှာ wingspan values မလိုအပ်တဲ့အတွက် ထည့်ထားမလားဆိုတာ သင့်စိတ်ကြိုက်လုပ်နိုင်ပါတယ်။

bar chart ဖန်တီးချင်ရင် target လုပ်ချင်တဲ့ data ကို ရွေးချယ်နိုင်ပါတယ်။ Bar charts တွေကို raw data ကနေ ဖန်တီးနိုင်ပါတယ်:

```python
birds.plot(x='Category',
        kind='bar',
        stacked=True,
        title='Birds of Minnesota')

```
![full data as a bar chart](../../../../3-Data-Visualization/09-visualization-quantities/images/full-data-bar-02.png)

ဒီ bar chart ကတော့ data များလွန်းလို့ ဖတ်ရှုရန် အလွန်ခက်ခဲနေပါတယ်။ plot လုပ်ချင်တဲ့ data ကိုသာ ရွေးချယ်ဖို့လိုပါတယ်။ ငှက်အမျိုးအစားအပေါ်မူတည်ပြီး အရှည်ကို ကြည့်ရှုရအောင်။

data ကို ငှက်ရဲ့ category ကိုသာ ထည့်သွင်းဖို့ filter လုပ်ပါ။

✅ Pandas ကို data ကို စီမံဖို့ အသုံးပြုပြီး Matplotlib ကို chart ဖန်တီးဖို့ အသုံးပြုထားပါတယ်။

category များစွာရှိတဲ့အတွက် chart ကို vertical display လုပ်ပြီး height ကို data အားလုံးကို ထည့်သွင်းဖို့ tweak လုပ်နိုင်ပါတယ်:

```python
category_count = birds.value_counts(birds['Category'].values, sort=True)
plt.rcParams['figure.figsize'] = [6, 12]
category_count.plot.barh()
```
![category and length](../../../../3-Data-Visualization/09-visualization-quantities/images/category-counts-02.png)

ဒီ bar chart က category တစ်ခုချင်းစီမှာ ငှက်အရေအတွက်ကို ကောင်းစွာဖော်ပြထားပါတယ်။ Minnesota ဟာ '10,000 ရေကန်များ၏မြေ' ဖြစ်တဲ့အတွက် Ducks/Geese/Waterfowl category မှာ ငှက်အများဆုံးရှိတာက အံ့မခန်းမဟုတ်ပါဘူး။

✅ ဒီ dataset ကို အသုံးပြုပြီး count အခြားအမျိုးအစားတွေကို စမ်းကြည့်ပါ။ ဘာတွေက သင့်ကို အံ့ဩစေပါသလဲ?

## Data ကို နှိုင်းယှဉ်ခြင်း

grouped data တွေကို နှိုင်းယှဉ်ဖို့ axes အသစ်တွေ ဖန်တီးနိုင်ပါတယ်။ MaxLength ကို category အပေါ်မူတည်ပြီး နှိုင်းယှဉ်ကြည့်ပါ:

```python
maxlength = birds['MaxLength']
plt.barh(y=birds['Category'], width=maxlength)
plt.rcParams['figure.figsize'] = [6, 12]
plt.show()
```
![comparing data](../../../../3-Data-Visualization/09-visualization-quantities/images/category-length-02.png)

ဒီမှာ အံ့မခန်းမရှိပါဘူး - hummingbirds တွေက Pelicans နဲ့ Geese တွေထက် MaxLength အနည်းဆုံးရှိပါတယ်။ Data က logical make sense ဖြစ်တဲ့အခါကောင်းပါတယ်!

Bar charts တွေကို data superimpose လုပ်ပြီး ပိုမိုစိတ်ဝင်စားဖွယ် visualizations ဖန်တီးနိုင်ပါတယ်။ Minimum နဲ့ Maximum Length ကို bird category တစ်ခုချင်းစီမှာ superimpose လုပ်ကြည့်ရအောင်:

```python
minLength = birds['MinLength']
maxLength = birds['MaxLength']
category = birds['Category']

plt.barh(category, maxLength)
plt.barh(category, minLength)

plt.show()
```
ဒီ plot မှာ Minimum Length နဲ့ Maximum Length ရဲ့ range ကို bird category တစ်ခုချင်းစီမှာ ကြည့်ရှုနိုင်ပါတယ်။ ဒီ data အရ ငှက်က càng ကြီး càng အရှည် range ကြီးတယ်လို့ သေချာပြောနိုင်ပါတယ်။ စိတ်ဝင်စားဖွယ်ကောင်းပါတယ်!

![superimposed values](../../../../3-Data-Visualization/09-visualization-quantities/images/superimposed-02.png)

## 🚀 စိန်ခေါ်မှု

ဒီ ငှက် dataset က ecosystem တစ်ခုထဲမှာရှိတဲ့ ငှက်အမျိုးအစားအမျိုးမျိုးအကြောင်း အချက်အလက်များစွာ ပေးထားပါတယ်။ အင်တာနက်မှာ ရှာဖွေပြီး ငှက်များနှင့်ဆိုင်သော အခြား dataset များကို ရှာဖွေပါ။ ငှက်များအကြောင်း မသိခဲ့တဲ့ အချက်အလက်များကို ရှာဖွေဖို့ charts နဲ့ graphs တွေ ဖန်တီးပြီး လေ့ကျင့်ပါ။

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/)

## ပြန်လည်သုံးသပ်ခြင်းနှင့် ကိုယ်တိုင်လေ့လာခြင်း

ဒီပထမဆုံးသင်ခန်းစာက Matplotlib ကို အသုံးပြုပြီး အရေအတွက်များကို ရှင်းလင်းဖော်ပြပုံအကြောင်း အချက်အလက်များပေးထားပါတယ်။ visualization အတွက် datasets တွေကို အသုံးပြုပုံအခြားနည်းလမ်းများကို လေ့လာပါ။ [Plotly](https://github.com/plotly/plotly.py) က ဒီသင်ခန်းစာတွေမှာ မဖော်ပြထားတဲ့ library တစ်ခုဖြစ်တဲ့အတွက် အဲဒီမှာ ဘာတွေ ပေးနိုင်သလဲဆိုတာ ကြည့်ရှုပါ။

## လုပ်ငန်းစဉ်

[Lines, Scatters, and Bars](assignment.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် ရှုလေ့လာသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှု ဝန်ဆောင်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွဲအချော်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။