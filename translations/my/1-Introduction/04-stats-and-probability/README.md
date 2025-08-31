<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b706a07cfa87ba091cbb91e0aa775600",
  "translation_date": "2025-08-30T19:24:56+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/README.md",
  "language_code": "my"
}
-->
# စာရင်းအင်းနှင့် အလားအလာအကြောင်း အကျဉ်းချုပ်

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/04-Statistics-Probability.png)|
|:---:|
| စာရင်းအင်းနှင့် အလားအလာ - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

စာရင်းအင်းနှင့် အလားအလာ သီအိုရီများသည် သင်္ချာ၏ အလွန်နီးစပ်သော နယ်ပယ်နှစ်ခုဖြစ်ပြီး ဒေတာသိပ္ပံတွင် အလွန်အရေးပါသည်။ သင်္ချာအကြောင်းနက်နက်ရှိုင်းရှိုင်း မသိဘဲ ဒေတာနှင့် လုပ်ဆောင်နိုင်သည်။ သို့သော် အခြေခံအယူအဆများကို အနည်းဆုံး သိထားခြင်းက ပိုမိုကောင်းမွန်ပါသည်။ ဒီမှာ သင်စတင်နိုင်ရန် အကျိုးရှိမည့် အကျဉ်းချုပ်ကို တင်ပြပေးပါမည်။

[![Intro Video](../../../../translated_images/video-prob-and-stats.e4282e5efa2f2543400843ed98b1057065c9600cebfc8a728e8931b5702b2ae4.my.png)](https://youtu.be/Z5Zy85g4Yjw)

## [Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/6)

## အလားအလာနှင့် အလားအလာမရေရာသော အပြောင်းအလဲများ

**အလားအလာ** ဆိုသည်မှာ 0 နှင့် 1 အကြားရှိ နံပါတ်တစ်ခုဖြစ်ပြီး **အဖြစ်အပျက်** တစ်ခုဖြစ်နိုင်မှုကို ဖော်ပြသည်။ ၎င်းကို အဖြစ်အပျက်ကို ဖြစ်စေသော အကောင်းဆုံးရလဒ်များ၏ အရေအတွက်ကို အားလုံးတူညီစွာဖြစ်နိုင်သော ရလဒ်များ၏ စုစုပေါင်းအရေအတွက်ဖြင့် ခွဲခြားခြင်းဖြင့် သတ်မှတ်သည်။ ဥပမာအားဖြင့် ကစားသမားတစ်ခုကို လွှဲလိုက်သောအခါ၊ စဉ်ကိန်းရရှိနိုင်မှုမှာ 3/6 = 0.5 ဖြစ်သည်။

အဖြစ်အပျက်များကို ပြောသောအခါ **အလားအလာမရေရာသော အပြောင်းအလဲများ** ကို အသုံးပြုသည်။ ဥပမာအားဖြင့် ကစားသမားတစ်ခုကို လွှဲလိုက်သောအခါရရှိသော နံပါတ်ကို ကိုယ်စားပြုသော အလားအလာမရေရာသော အပြောင်းအလဲသည် 1 မှ 6 အထိ တန်ဖိုးများကို ယူပါမည်။ 1 မှ 6 အထိ နံပါတ်များ၏ စုစုပေါင်းကို **နမူနာအကျယ်** ဟုခေါ်သည်။ အလားအလာမရေရာသော အပြောင်းအလဲသည် တန်ဖိုးတစ်ခုကို ယူနိုင်မှုအလားအလာကို ပြောနိုင်သည်။ ဥပမာအားဖြင့် P(X=3)=1/6 ဖြစ်သည်။

အထက်ပါ ဥပမာတွင် အလားအလာမရေရာသော အပြောင်းအလဲကို **Discrete** ဟုခေါ်သည်။ အကြောင်းမှာ ၎င်းတွင် ရေတွက်နိုင်သော နမူနာအကျယ်ရှိပြီး၊ သီးခြားတန်ဖိုးများကို ရေတွက်နိုင်သည်။ နမူနာအကျယ်သည် အမှန်တကယ်နံပါတ်များ၏ အကွာအဝေး သို့မဟုတ် အမှန်တကယ်နံပါတ်များ၏ စုံလုံးဖြစ်သော အခြေအနေများလည်း ရှိနိုင်သည်။ ၎င်းတို့ကို **Continuous** ဟုခေါ်သည်။ ကောင်းမွန်သော ဥပမာတစ်ခုမှာ ဘတ်စ်ကားရောက်ရှိချိန်ဖြစ်သည်။

## အလားအလာဖြန့်ဖြူးမှု

Discrete အလားအလာမရေရာသော အပြောင်းအလဲများ၏ အခြေအနေတွင်၊ အဖြစ်အပျက်တစ်ခုစီ၏ အလားအလာကို P(X) ဟုခေါ်သော အလုပ်လုပ်ပုံတစ်ခုဖြင့် ရှင်းလင်းဖော်ပြရန် လွယ်ကူသည်။ နမူနာအကျယ် *S* မှ တန်ဖိုး *s* တစ်ခုစီအတွက်၊ ၎င်းသည် 0 မှ 1 အထိ နံပါတ်တစ်ခုကို ပေးမည်ဖြစ်ပြီး၊ အဖြစ်အပျက်အားလုံးအတွက် P(X=s) တန်ဖိုးများ၏ စုစုပေါင်းသည် 1 ဖြစ်ရမည်။

အလွန်ကျော်ကြားသော Discrete ဖြန့်ဖြူးမှုတစ်ခုမှာ **Uniform Distribution** ဖြစ်ပြီး၊ ၎င်းတွင် N အစိတ်အပိုင်းများပါရှိသော နမူနာအကျယ်ရှိပြီး၊ ၎င်းတို့၏ တစ်ခုစီအတွက် အလားအလာမှာ 1/N ဖြစ်သည်။

Continuous အပြောင်းအလဲတစ်ခု၏ အလားအလာဖြန့်ဖြူးမှုကို ဖော်ပြရန် ပိုမိုခက်ခဲသည်။ ၎င်းတွင် [a,b] အကွာအဝေး သို့မဟုတ် အမှန်တကယ်နံပါတ်များ၏ စုံလုံး ℝ မှ တန်ဖိုးများကို ရယူသည်။ ဘတ်စ်ကားရောက်ရှိချိန်ကို စဉ်းစားပါ။ အမှန်တကယ်တွင်၊ တိကျသောရောက်ရှိချိန် *t* တစ်ခုအတွက်၊ ဘတ်စ်ကားသည် အတိအကျအချိန်၌ ရောက်ရှိနိုင်မှုအလားအလာမှာ 0 ဖြစ်သည်။

> အလားအလာ 0 ရှိသော အဖြစ်အပျက်များသည် ဖြစ်ပျက်လေ့ရှိပြီး၊ အနည်းဆုံး ဘတ်စ်ကားရောက်ရှိသောအချိန်တိုင်း ဖြစ်ပျက်သည်။

ကျွန်ုပ်တို့သည် အပြောင်းအလဲတစ်ခုသည် တန်ဖိုးများ၏ အကွာအဝေးတစ်ခုတွင် ရောက်ရှိနိုင်မှုအလားအလာကိုသာ ပြောနိုင်သည်။ ဥပမာအားဖြင့် P(t<sub>1</sub>≤X<t<sub>2</sub>) ဖြစ်သည်။ ဒီအခြေအနေတွင်၊ အလားအလာဖြန့်ဖြူးမှုကို **Probability Density Function** p(x) ဖြင့် ဖော်ပြသည်။

![P(t_1\le X<t_2)=\int_{t_1}^{t_2}p(x)dx](../../../../translated_images/probability-density.a8aad29f17a14afb519b407c7b6edeb9f3f9aa5f69c9e6d9445f604e5f8a2bf7.my.png)

Continuous Uniform ဖြန့်ဖြူးမှုသည် Uniform Distribution ၏ Continuous အနုနယ်ဖြစ်ပြီး၊ ၎င်းကို အကွာအဝေးတစ်ခုတွင် သတ်မှတ်သည်။ X တန်ဖိုးသည် အကွာအဝေးတစ်ခုတွင် ရောက်ရှိနိုင်မှုအလားအလာသည် အကွာအဝေး၏ အလျားနှင့် အချိုးကျပြီး၊ 1 အထိ မြင့်တက်သည်။

အရေးပါသော ဖြန့်ဖြူးမှုတစ်ခုမှာ **Normal Distribution** ဖြစ်ပြီး၊ ကျွန်ုပ်တို့သည် အောက်တွင် ပိုမိုအသေးစိတ်ဆွေးနွေးမည်။

## ပျမ်းမျှတန်ဖိုး၊ အပြောင်းအလဲနှင့် စံအလျားအပြောင်းအလဲ

အလားအလာမရေရာသော အပြောင်းအလဲ X ၏ နမူနာများ n ခုကို ရွေးချယ်ကြောင်း စဉ်းစားပါ။ x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub> ဖြစ်သည်။ **ပျမ်းမျှတန်ဖိုး** (သို့မဟုတ် **အက္ခရာပျမ်းမျှ**) ကို (x<sub>1</sub>+x<sub>2</sub>+x<sub>n</sub>)/n အဖြစ် ရိုးရှင်းသောနည်းလမ်းဖြင့် သတ်မှတ်နိုင်သည်။ နမူနာအရွယ်အစားကို ကြီးထွားလာသည် (n→∞ ဖြစ်သည်) ဟုယူဆပါက၊ ဖြန့်ဖြူးမှု၏ ပျမ်းမျှတန်ဖိုး (**မျှော်လင့်ချက်**) ကို ရရှိမည်ဖြစ်သည်။ **E**(x) ဟု မျှော်လင့်ချက်ကို မှတ်သားမည်။

> Discrete ဖြန့်ဖြူးမှုတစ်ခုသည် {x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>N</sub>} တန်ဖိုးများနှင့် p<sub>1</sub>, p<sub>2</sub>, ..., p<sub>N</sub> အလားအလာများပါရှိသည်ဟုယူဆပါက၊ မျှော်လင့်ချက်သည် E(X)=x<sub>1</sub>p<sub>1</sub>+x<sub>2</sub>p<sub>2</sub>+...+x<sub>N</sub>p<sub>N</sub> ဖြစ်သည်။

တန်ဖိုးများသည် ဘယ်လောက်အထိ ပျံ့နှံ့နေသည်ကို သိရန်၊ အပြောင်းအလဲ σ<sup>2</sup> = ∑(x<sub>i</sub> - μ)<sup>2</sup>/n ကို တွက်ချက်နိုင်သည်။ μ သည် စဉ်၏ ပျမ်းမျှတန်ဖိုးဖြစ်သည်။ σ ကို **စံအလျားအပြောင်းအလဲ** ဟုခေါ်ပြီး၊ σ<sup>2</sup> ကို **အပြောင်းအလဲ** ဟုခေါ်သည်။

## Mode, Median နှင့် Quartiles

တစ်ခါတစ်ရံ၊ ပျမ်းမျှတန်ဖိုးသည် ဒေတာ၏ "ပုံမှန်" တန်ဖိုးကို လုံလောက်စွာ ကိုယ်စားပြုမထားနိုင်ပါ။ ဥပမာအားဖြင့်၊ အလွန်အမင်းတန်ဖိုးများရှိပြီး၊ ၎င်းတို့သည် ပျမ်းမျှတန်ဖိုးကို ထိခိုက်စေပါက၊ ပျမ်းမျှတန်ဖိုးကို ထိခိုက်စေပါသည်။ **Median** သည် ဒေတာအချက်အလက်၏ တစ်ဝက်သည် ၎င်းထက်နိမ့်ပြီး၊ တစ်ဝက်သည် ၎င်းထက်မြင့်သော တန်ဖိုးဖြစ်သည်။

Quartiles ကို အသုံးပြုခြင်းသည် ဒေတာဖြန့်ဖြူးမှုကို နားလည်ရန် အထောက်အကူဖြစ်သည်။

* ပထမ Quartile (Q1) သည် ဒေတာ၏ 25% သည် ၎င်းထက်နိမ့်သော တန်ဖိုးဖြစ်သည်။
* တတိယ Quartile (Q3) သည် ဒေတာ၏ 75% သည် ၎င်းထက်နိမ့်သော တန်ဖိုးဖြစ်သည်။

Median နှင့် Quartiles တို့၏ ဆက်နွယ်မှုကို **Box Plot** ဟုခေါ်သော အကြမ်းဖျင်းပုံစံတွင် ဖော်ပြနိုင်သည်။

<img src="images/boxplot_explanation.png" width="50%"/>

ဒီမှာ **Inter-quartile Range** IQR=Q3-Q1 ကို တွက်ချက်ပြီး၊ **Outliers** ဟုခေါ်သော တန်ဖိုးများကို တွေ့နိုင်သည်။ ၎င်းတို့သည် [Q1-1.5*IQR,Q3+1.5*IQR] အကွာအဝေးအပြင်ရှိသည်။

နည်းနည်းသော တန်ဖိုးများပါရှိသော အကန့်အသတ်ဖြန့်ဖြူးမှုအတွက်၊ "ပုံမှန်" တန်ဖိုးက အများဆုံးထပ်နေသော တန်ဖိုးဖြစ်ပြီး၊ ၎င်းကို **Mode** ဟုခေါ်သည်။ ၎င်းကို အရောင်များကဲ့သို့သော အမျိုးအစားဒေတာတွင် အများဆုံးအသုံးပြုသည်။ 

ဥပမာအားဖြင့်၊ လူအုပ်နှစ်အုပ်ရှိပြီး၊ တစ်အုပ်သည် အနီရောင်ကို အလွန်နှစ်သက်ပြီး၊ တစ်အုပ်သည် အပြာရောင်ကို နှစ်သက်သည်။ အရောင်များကို နံပါတ်များဖြင့် ကုဒ်ဖြင့် သတ်မှတ်ပါက၊ အကြိုက်ဆုံးအရောင်အတွက် ပျမ်းမျှတန်ဖိုးသည် လိမ္မော်-အစိမ်းရောင်အကွာအဝေးတွင် ရှိနိုင်ပြီး၊ ၎င်းသည် အုပ်စုနှစ်ခု၏ အကြိုက်ကို မကိုယ်စားပြုနိုင်ပါ။ သို့သော် Mode သည် အရောင်တစ်ခု သို့မဟုတ် အရောင်နှစ်ခုဖြစ်နိုင်ပြီး၊ ၎င်းတို့ကို မဲပေးသူအရေအတွက်တူညီပါက **Multimodal** ဟုခေါ်သည်။

## အမှန်တကယ်ဒေတာ

အမှန်တကယ်ဒေတာကို ခွဲခြမ်းစိတ်ဖြာသောအခါ၊ ၎င်းတို့သည် အလားအလာမရေရာသော အပြောင်းအလဲများမဟုတ်ပါ။ အကြောင်းမှာ ၎င်းတို့သည် မသိသောရလဒ်များဖြင့် စမ်းသပ်မှုများမလုပ်ဆောင်ပါ။ 

ဥပမာအားဖြင့် ဘေ့စ်ဘောကစားသမားအဖွဲ့တစ်ခုနှင့် ၎င်းတို့၏ ကိုယ်ခန္ဓာဒေတာများ၊ height, weight နှင့် age ကဲ့သို့သော ဒေတာများကို စဉ်းစားပါ။ ၎င်းတို့သည် အလားအလာမရေရာသော အပြောင်းအလဲများမဟုတ်သော်လည်း၊ အလားအလာသီအိုရီများကို အလွယ်တကူ အသုံးပြုနိုင်သည်။ 

ဥပမာအားဖြင့် လူများ၏ အလေးချိန်များ၏ စဉ်သည် အလားအလာမရေရာသော အပြောင်းအလဲတစ်ခုမှ ရယူထားသော တန်ဖိုးများ၏ စဉ်အဖြစ် စဉ်းစားနိုင်သည်။ 

```
[180.0, 215.0, 210.0, 210.0, 188.0, 176.0, 209.0, 200.0, 231.0, 180.0, 188.0, 180.0, 185.0, 160.0, 180.0, 185.0, 197.0, 189.0, 185.0, 219.0]
```

> **Note**: ဒီဒေတာကို အသုံးပြု၍ အလုပ်လုပ်ပုံကို ကြည့်ရန် [accompanying notebook](notebook.ipynb) ကို ကြည့်ပါ။ ၎င်းသင်ခန်းစာတွင် စိန်ခေါ်မှုများစွာပါရှိပြီး၊ ၎င်းတို့ကို notebook တွင် ကုဒ်ထည့်သွင်းခြင်းဖြင့် ပြီးမြောက်နိုင်သည်။ ဒေတာကို လုပ်ဆောင်ရန် မသိပါက စိတ်မပူပါနှင့် - ကျွန်ုပ်တို့သည် Python ကို အသုံးပြု၍ ဒေတာနှင့် လုပ်ဆောင်ခြင်းကို နောက်ပိုင်းတွင် ပြန်လည်ဆွေးနွေးမည်။ Jupyter Notebook တွင် ကုဒ်ကို အကောင်အထည်ဖော်ရန် မသိပါက [ဒီဆောင်းပါး](https://soshnikov.com/education/how-to-execute-notebooks-from-github/) ကို ကြည့်ပါ။

ဒီမှာ ကျွန်ုပ်တို့၏ ဒေတာအတွက် ပျမ်းမျှတန်ဖိုး၊ Median နှင့် Quartiles ကို ဖော်ပြထားသော Box Plot ဖြစ်သည်။

![Weight Box Plot](../../../../translated_images/weight-boxplot.1dbab1c03af26f8a008fff4e17680082c8ab147d6df646cbac440bbf8f5b9c42.my.png)

ကျွန်ုပ်တို့၏ ဒေတာတွင် ကစားသမား **Roles** များအကြောင်း အချက်အလက်များပါရှိသောကြောင့်၊ Role အလိုက် Box Plot ကို ပြုလုပ်နိုင်သည်။ ၎င်းသည် Role အလိုက် Parameter တန်ဖိုးများကွာခြားမှုကို နားလည်ရန် အထောက်အကူဖြစ်စေသည်။ ဒီအကြိမ်မှာ Height ကို စဉ်းစားပါမည်။

![Box plot by role](../../../../translated_images/boxplot_byrole.036b27a1c3f52d42f66fba2324ec5cde0a1bca6a01a619eeb0ce7cd054b2527b.my.png)

ဒီပုံစံသည် ပထမအခြေခံကစားသမား၏ အမြင့်သည် ဒုတိယအခြေခံကစားသမား၏ အမြင့်ထက် ပျမ်းမျှအားဖြင့် မြင့်မားသည်ဟု ဖော်ပြသည်။ ဒီသင်ခန်းစာတွင် ကျွန်ုပ်တို့သည် ဒီအယူအဆကို ပိုမိုတိကျစွာ စမ်းသပ်နည်းများနှင့် ဒေတာသည် အထောက်အထားအလုံလောက်ရှိကြောင်း သက်သေပြနည်းများကို လေ့လာမည်။

> အမှန်တကယ်ဒေတာနှင့် အလုပ်လုပ်သောအခါ၊ ဒေတာအချက်အလက်များအားလုံးသည် အလားအလာဖြန့်ဖြူးမှုတစ်ခုမှ ရယူထားသော နမူနာများဖြစ်သည်ဟု ယူဆပါသည်။ ဒီယူဆချက်သည် Machine Learning နည်းလမ်းများကို အသုံးပြုရန်နှင့် အလုပ်လုပ်နိုင်သော ခန့်မှန်းပုံစံများကို တည်ဆောက်ရန် ခွင့်ပြုသည်။

ကျွန်ုပ်တို့၏ ဒေတာဖြန့်ဖြူးမှုကို ကြည့်ရန် **Histogram** ဟုခေါ်သော ပုံစံကို ရှုနိုင်သည်။ X-axis တွင် အလေးချိန် interval များ (သို့မဟုတ် **bins**) ပါရှိပြီး၊ Y-axis တွင် အလားအလာမရေရာသော အပြောင်းအလဲနမူနာသည် interval တစ်ခုတွင် ရှိနေသော အကြိမ်အရေအတွက်ကို ဖော်ပြသည်။

![Histogram of real world data](../../../../translated_images/weight-histogram.bfd00caf7fc30b145b21e862dba7def41c75635d5280de25d840dd7f0b00545e.my.png)

ဒီ Histogram မှာ အလေးချိန်များ
> **ယုံကြည်မှုအကွာအဝေး** ဆိုသည်မှာ ကျွန်ုပ်တို့၏နမူနာအရ လူဦးရေ၏ အမှန်တကယ်အလယ်တန်းကို ခန့်မှန်းခြင်းဖြစ်ပြီး၊ သတ်မှတ်ထားသော အချို့သောဖြစ်နိုင်ခြေ (သို့မဟုတ် **ယုံကြည်မှုအဆင့်**) ဖြင့် တိကျမှုရှိသည်။
Suppose ကျွန်တော်တို့မှာ X<sub>1</sub>, ..., X<sub>n</sub> ဆိုတဲ့ distribution မှာ sample တစ်ခုရှိတယ်။ Distribution မှာ sample တစ်ခုကို အကြိမ်ကြိမ်ယူတဲ့အခါ mean value μ က မတူညီတဲ့အချိန်တိုင်းရရှိမယ်။ ဒါကြောင့် μ ကို random variable တစ်ခုအနေနဲ့ သတ်မှတ်နိုင်တယ်။ **Confidence interval** ဆိုတာ confidence p ရှိတဲ့ value pair (L<sub>p</sub>,R<sub>p</sub>) ဖြစ်ပြီး **P**(L<sub>p</sub>≤μ≤R<sub>p</sub>) = p ဖြစ်တယ်။ ဒါဟာ mean value တစ်ခု interval အတွင်းမှာ ရောက်ရှိဖို့ probability p ရှိတယ်ဆိုတာကို ဆိုလိုတာပါ။

Confidence interval တွေကို ဘယ်လိုတွက်ချက်ရမယ်ဆိုတာကို အကြမ်းဖျင်းအနေနဲ့ မဖော်ပြနိုင်ပါဘူး။ [Wikipedia](https://en.wikipedia.org/wiki/Confidence_interval) မှာ အချက်အလက်ပိုမိုသိရှိနိုင်ပါတယ်။ အကြမ်းဖျင်းအားဖြင့် population ရဲ့ true mean နဲ့ sample mean ရဲ့ distribution ကို **student distribution** လို့ခေါ်ပါတယ်။

> **စိတ်ဝင်စားစရာအချက်**: Student distribution ကို mathematician William Sealy Gosset ရေးသားခဲ့ပြီး "Student" ဆိုတဲ့ နာမည်နဲ့ စာတမ်းတင်ခဲ့တယ်။ သူ Guinness brewery မှာ အလုပ်လုပ်ခဲ့ပြီး statistical tests တွေကို raw materials ရဲ့ quality ကိုသတ်မှတ်ဖို့ အသုံးပြုတာကို သူ့အလုပ်ရှင်က အများပြည်သူမသိစေချင်ခဲ့တယ်လို့ ဆိုပါတယ်။

Population ရဲ့ mean μ ကို confidence p နဲ့ ခန့်မှန်းချင်ရင် *(1-p)/2-th percentile* ကို Student distribution A မှာယူရမယ်။ Tables မှာယူနိုင်သလို statistical software (ဥပမာ Python, R, စသည်) ရဲ့ built-in functions တွေကို အသုံးပြုနိုင်ပါတယ်။ μ ရဲ့ interval ကို X±A*D/√n နဲ့ ရရှိမယ်။ ဒီမှာ X က sample ရဲ့ mean ဖြစ်ပြီး D က standard deviation ဖြစ်ပါတယ်။

> **Note**: Student distribution နဲ့ ဆက်စပ်တဲ့ [degrees of freedom](https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics)) ဆိုတဲ့ အရေးကြီးသော concept ကို ဒီမှာ မဖော်ပြပါဘူး။ Statistics ပိုမိုနက်နက်ရှိုင်းရှိုင်းလေ့လာချင်ရင် စာအုပ်တွေကို ဖတ်ရှုနိုင်ပါတယ်။

Weight နဲ့ height တွေကို confidence interval တွေတွက်ချက်တဲ့ ဥပမာကို [accompanying notebooks](notebook.ipynb) မှာတွေ့နိုင်ပါတယ်။

| p | Weight mean |
|-----|-----------|
| 0.85 | 201.73±0.94 |
| 0.90 | 201.73±1.08 |
| 0.95 | 201.73±1.28 |

Confidence probability ပိုမြင့်လာတာနဲ့ confidence interval ပိုကျယ်လာတာကို သတိပြုပါ။

## Hypothesis Testing 

Baseball players dataset မှာ player roles မျိုးစုံရှိပြီး အောက်ပါအတိုင်း စုစည်းနိုင်ပါတယ် ([accompanying notebook](notebook.ipynb) ကိုကြည့်ပါ):

| Role | Height | Weight | Count |
|------|--------|--------|-------|
| Catcher | 72.723684 | 204.328947 | 76 |
| Designated_Hitter | 74.222222 | 220.888889 | 18 |
| First_Baseman | 74.000000 | 213.109091 | 55 |
| Outfielder | 73.010309 | 199.113402 | 194 |
| Relief_Pitcher | 74.374603 | 203.517460 | 315 |
| Second_Baseman | 71.362069 | 184.344828 | 58 |
| Shortstop | 71.903846 | 182.923077 | 52 |
| Starting_Pitcher | 74.719457 | 205.163636 | 221 |
| Third_Baseman | 73.044444 | 200.955556 | 45 |

First basemen ရဲ့ mean height က second basemen ရဲ့ height ထက် မြင့်တယ်ဆိုတာကို သတိပြုမိတယ်။ ဒါကြောင့် **first basemen are higher than second basemen** ဆိုတဲ့ အကြောင်းအရာကို သတ်မှတ်ချင်တယ်။

> ဒီ statement ကို **hypothesis** လို့ခေါ်တယ်။ အကြောင်းက ဒီအချက်အလက်ဟာ တကယ်မှန်မမှန် မသိရသေးလို့ပါ။

ဒါပေမယ့် ဒီအချက်အလက်ကို သတ်မှတ်ဖို့ အလွယ်တကူ မဖြစ်နိုင်ပါဘူး။ Mean တစ်ခုစီမှာ confidence interval ရှိပြီး statistical error ဖြစ်နိုင်ပါတယ်။ Hypothesis ကို စမ်းသပ်ဖို့ formal method တစ်ခုလိုအပ်ပါတယ်။

First basemen နဲ့ second basemen ရဲ့ height တွေကို confidence interval တွေတွက်ချက်ကြည့်ရအောင်:

| Confidence | First Basemen | Second Basemen |
|------------|---------------|----------------|
| 0.85 | 73.62..74.38 | 71.04..71.69 |
| 0.90 | 73.56..74.44 | 70.99..71.73 |
| 0.95 | 73.47..74.53 | 70.92..71.81 |

Confidence level မည်သည့်အချိန်မှာမဆို interval တွေ overlap မဖြစ်ပါဘူး။ ဒါဟာ first basemen are higher than second basemen ဆိုတဲ့ hypothesis ကို အတည်ပြုပါတယ်။

Formal အနေနဲ့ ကျွန်တော်တို့ရဲ့ ပြဿနာက **two probability distributions are the same** ဖြစ်မဖြစ်ကို စမ်းသပ်ဖို့ပါ။ Distribution ပေါ်မူတည်ပြီး test မျိုးစုံကို အသုံးပြုရမယ်။ Distribution တွေ normal ဖြစ်တယ်ဆိုရင် **[Student t-test](https://en.wikipedia.org/wiki/Student%27s_t-test)** ကို အသုံးပြုနိုင်ပါတယ်။

Student t-test မှာ **t-value** ကိုတွက်ချက်ပြီး variance ကို ထည့်သွင်းစဉ်းစားတယ်။ T-value ဟာ **student distribution** ကို follow လုပ်ပြီး confidence level **p** အတွက် threshold value ရရှိနိုင်တယ်။ T-value ကို threshold နဲ့ နှိုင်းယှဉ်ပြီး hypothesis ကို approve/reject လုပ်နိုင်ပါတယ်။

Python မှာ **SciPy** package ကို အသုံးပြုနိုင်ပြီး `ttest_ind` function ပါဝင်ပါတယ်။ Function က t-value ကိုတွက်ချက်ပေးပြီး confidence p-value ကို reverse lookup လုပ်ပေးတယ်။ ဒါကြောင့် confidence ကိုကြည့်ပြီး အတည်ပြုနိုင်ပါတယ်။

ဥပမာအားဖြင့် first basemen နဲ့ second basemen ရဲ့ height တွေကို နှိုင်းယှဉ်တဲ့အခါ:
```python
from scipy.stats import ttest_ind

tval, pval = ttest_ind(df.loc[df['Role']=='First_Baseman',['Height']], df.loc[df['Role']=='Designated_Hitter',['Height']],equal_var=False)
print(f"T-value = {tval[0]:.2f}\nP-value: {pval[0]}")
```
```
T-value = 7.65
P-value: 9.137321189738925e-12
```
P-value အနည်းငယ်ရှိတာကြောင့် first basemen are taller ဆိုတဲ့ hypothesis ကို အတည်ပြုနိုင်ပါတယ်။

အခြား hypothesis မျိုးစုံကိုလည်း စမ်းသပ်နိုင်ပါတယ်၊ ဥပမာ:
* Sample တစ်ခုက distribution တစ်ခုကို follow လုပ်တယ်ဆိုတာကို အတည်ပြုဖို့
* Sample ရဲ့ mean value က predefined value တစ်ခုနဲ့ ကိုက်ညီတယ်ဆိုတာကို အတည်ပြုဖို့
* Samples များစွာရဲ့ mean တွေကို နှိုင်းယှဉ်ဖို့ (ဥပမာ: အသက်အရွယ်အုပ်စုများအကြား happiness level တွေကို နှိုင်းယှဉ်)

## Law of Large Numbers and Central Limit Theorem

Normal distribution အရေးကြီးတဲ့အကြောင်းအရင်းတစ်ခုက **central limit theorem** ဖြစ်ပါတယ်။ N→∞ ဖြစ်တဲ့အခါ independent N values X<sub>1</sub>, ..., X<sub>N</sub> ရဲ့ mean Σ<sub>i</sub>X<sub>i</sub> ဟာ normal distribution ဖြစ်တယ်။ Mean က μ ဖြစ်ပြီး variance က σ<sup>2</sup>/N ဖြစ်တယ်။

> Central limit theorem ကို အခြားနည်းလမ်းတစ်ခုနဲ့လည်း ရှင်းလင်းနိုင်ပါတယ်။ Random variable values တွေကို စုပေါင်းပြီး mean တွက်တဲ့အခါ normal distribution ရရှိတယ်။

Central limit theorem က N→∞ ဖြစ်တဲ့အခါ sample mean က μ နဲ့ တူဖို့ probability 1 ရှိတယ်ဆိုတာကိုလည်း ပြောပါတယ်။ ဒါကို **law of large numbers** လို့ခေါ်တယ်။

## Covariance and Correlation

Data Science ရဲ့ အရေးကြီးအပိုင်းတစ်ခုက data တွေကြားဆက်စပ်မှုကို ရှာဖွေဖို့ပါ။ Sequence နှစ်ခု **correlate** လုပ်တယ်ဆိုတာက တစ်ချိန်တည်းမှာ behavior တူတူပြသတယ်ဆိုတာပါ။ Sequence တစ်ခုတက်တဲ့အခါ တစ်ခုကျသွားတာမျိုးလည်း ဖြစ်နိုင်ပါတယ်။

> Correlation ဟာ causal relationship ကို မပြသနိုင်ပါဘူး။ Variables နှစ်ခုဟာ အခြားအကြောင်းအရာတစ်ခုကြောင့် ဆက်စပ်နိုင်ပါတယ်၊ ဒါမှမဟုတ် chance ကြောင့် correlation ဖြစ်နိုင်ပါတယ်။ ဒါပေမယ့် strong mathematical correlation ရှိရင် variables နှစ်ခုကြားမှာ ဆက်စပ်မှုရှိတယ်လို့ သံသယရှိနိုင်ပါတယ်။

Mathematically, random variables နှစ်ခုကြားဆက်စပ်မှုကို **covariance** နဲ့ဖော်ပြတယ်။ Cov(X,Y) = **E**\[(X-**E**(X))(Y-**E**(Y))\] ဖြစ်တယ်။ Variables နှစ်ခု mean values ကနေ ဘယ်လို deviate လုပ်တယ်ဆိုတာကို တွက်ပြီး product တွေကို စုပေါင်းတယ်။ Deviations တူတူဖြစ်ရင် positive covariance ရရှိတယ်။ Deviations မတူရင် negative covariance ရရှိတယ်။ Deviations မဆက်စပ်ရင် covariance က 0 နီးပါးဖြစ်တယ်။

Covariance ရဲ့ absolute value က correlation ရဲ့ အရွယ်အစားကို မပြသနိုင်ပါဘူး။ Standard deviation နဲ့ normalize လုပ်ပြီး **correlation** ရရှိနိုင်တယ်။ Correlation က [-1,1] အတွင်းရှိပြီး 1 က strong positive correlation, -1 က strong negative correlation, 0 က correlation မရှိတာကို ဆိုလိုတယ်။

**ဥပမာ**: Baseball players dataset မှာ weight နဲ့ height ကြား correlation တွက်ကြည့်ရအောင်:
```python
print(np.corrcoef(weights,heights))
```
Result အနေနဲ့ **correlation matrix** ရရှိတယ်:
```
array([[1.        , 0.52959196],
       [0.52959196, 1.        ]])
```

> Correlation matrix C ကို input sequences S<sub>1</sub>, ..., S<sub>n</sub> အတွက် တွက်နိုင်တယ်။ C<sub>ij</sub> က S<sub>i</sub> နဲ့ S<sub>j</sub> ကြား correlation ဖြစ်ပြီး diagonal elements တွေက 1 ဖြစ်တယ် (self-correlation of S<sub>i</sub>).

Weight နဲ့ height ကြား correlation 0.53 ရှိတာက variables နှစ်ခုကြား ဆက်စပ်မှုရှိတယ်ဆိုတာကို ပြသတယ်။ Scatter plot ကိုလည်း ရိုက်ပြီး relationship ကို visually ကြည့်နိုင်တယ်:

![Relationship between weight and height](../../../../translated_images/weight-height-relationship.3f06bde4ca2aba9974182c4ef037ed602acd0fbbbbe2ca91cefd838a9e66bcf9.my.png)

> Correlation နဲ့ covariance ရဲ့ ဥပမာများကို [accompanying notebook](notebook.ipynb) မှာတွေ့နိုင်ပါတယ်။

## နိဂုံး

ဒီအပိုင်းမှာ ကျွန်တော်တို့:

* data ရဲ့ mean, variance, mode, quartiles စတဲ့ statistical properties တွေကို လေ့လာခဲ့တယ်
* random variables ရဲ့ distributions မျိုးစုံကို လေ့လာခဲ့တယ်
* properties မျိုးစုံကြား correlation ရှာဖွေခဲ့တယ်
* math နဲ့ statistics apparatus ကို hypothesis တွေကို အတည်ပြုဖို့ အသုံးပြုခဲ့တယ်
* data sample ရဲ့ random variable အတွက် confidence interval တွေတွက်ခဲ့တယ်

Probability နဲ့ statistics ရဲ့ အခြေခံအချက်အလက်တွေကို လေ့လာခဲ့ပြီး ဒီ course ကို စတင်ဖို့ လုံလောက်ပါတယ်။

## 🚀 Challenge

Notebook မှာ sample code ကို အသုံးပြုပြီး hypothesis အောက်ပါအတိုင်း စမ်းသပ်ပါ:
1. First basemen are older than second basemen
2. First basemen are taller than third basemen
3. Shortstops are taller than second basemen

## [Post-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/7)

## Review & Self Study

Probability နဲ့ statistics ဟာ အကျယ်အဝန်းရှိတဲ့အကြောင်းအရာဖြစ်ပြီး သီးသန့် course တစ်ခုအနေနဲ့လေ့လာဖို့ လိုအပ်ပါတယ်။ Theory ကိုပိုမိုနက်နက်ရှိုင်းရှိုင်းလေ့လာချင်ရင် အောက်ပါစာအုပ်များကို ဖတ်ရှုနိုင်ပါတယ်:

1. [Carlos Fernandez-Granda](https://cims.nyu.edu/~cfgranda/) ရဲ့ [Probability and Statistics for Data Science](https://cims.nyu.edu/~cfgranda/pages/stuff/probability_stats_for_DS.pdf) lecture notes (online မှာရရှိနိုင်ပါတယ်)
1. [Peter and Andrew Bruce. Practical Statistics for Data Scientists.](https://www.oreilly.com/library/view/practical-statistics-for/9781491952955/) [[sample code in R](https://github.com/andrewgbruce/statistics-for-data-scientists)]. 
1. [James D. Miller. Statistics for Data Science](https://www.packtpub.com/product/statistics-for-data-science/9781788290678) [[sample code in R](https://github.com/PacktPublishing/Statistics-for-Data-Science)]

## Assignment

[Small Diabetes Study](assignment.md)

## Credits

ဒီ lesson ကို [Dmitry Soshnikov](http://soshnikov.com) မှ ♥️ နဲ့ရေးသားထားပါတယ်။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါရှိနိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှားမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။