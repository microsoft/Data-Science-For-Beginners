<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1cf49f029ba1f25a54f0d5bc2fa575fc",
  "translation_date": "2025-09-05T20:21:55+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/README.md",
  "language_code": "my"
}
-->
# စာရင်းအင်းနှင့် အလားအလာအကြောင်း အကျဉ်းချုပ်

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/04-Statistics-Probability.png)|
|:---:|
| စာရင်းအင်းနှင့် အလားအလာ - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

စာရင်းအင်းနှင့် အလားအလာ သီအိုရီများသည် သင်္ချာ၏ အလွန်နီးစပ်သော နယ်ပယ်နှစ်ခုဖြစ်ပြီး ဒေတာသိပ္ပံတွင် အလွန်အရေးပါသည်။ သင်္ချာအကြောင်း အနက်ရှိုင်းစွာ မသိဘဲ ဒေတာနှင့် လုပ်ဆောင်နိုင်သော်လည်း အခြေခံအယူအဆများကို အနည်းဆုံး သိထားခြင်းက ပိုမိုကောင်းမွန်ပါသည်။ ဒီမှာ သင်စတင်နိုင်ရန် အကျဉ်းချုပ်ကို တင်ပြပေးပါမည်။

[![Intro Video](../../../../1-Introduction/04-stats-and-probability/images/video-prob-and-stats.png)](https://youtu.be/Z5Zy85g4Yjw)

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/6)

## အလားအလာနှင့် အလှည့်အပြောင်း အတန်းများ

**အလားအလာ** ဆိုသည်မှာ 0 နှင့် 1 အကြားရှိ နံပါတ်တစ်ခုဖြစ်ပြီး **ဖြစ်ရပ်** တစ်ခုဖြစ်နိုင်မှုကို ဖော်ပြသည်။ ၎င်းကို ဖြစ်နိုင်သော အကျိုးအမြတ်များ (ဖြစ်ရပ်ကို ဖြစ်စေသော) ကို အားလုံးဖြစ်နိုင်သော အကျိုးအမြတ်များဖြင့် ခွဲခြားခြင်းဖြင့် သတ်မှတ်သည်။ ဥပမာအားဖြင့် အံဆွဲကို လွှဲလိုက်သောအခါ ကျွန်ုပ်တို့ အတိအကျနံပါတ်တစ်ခုရရှိနိုင်မှုမှာ 3/6 = 0.5 ဖြစ်သည်။

ဖြစ်ရပ်များအကြောင်း ပြောသောအခါ ကျွန်ုပ်တို့ **အလှည့်အပြောင်း အတန်းများ** ကို အသုံးပြုသည်။ ဥပမာအားဖြင့် အံဆွဲလိုက်သောအခါရရှိသော နံပါတ်ကို ကိုယ်စားပြုသော အလှည့်အပြောင်း အတန်းသည် 1 မှ 6 အထိ တန်ဖိုးများကို ယူပါမည်။ 1 မှ 6 အထိ နံပါတ်များ၏ စုစုပေါင်းကို **နမူနာအကျယ်** ဟုခေါ်သည်။ ကျွန်ုပ်တို့သည် အလှည့်အပြောင်း အတန်းတစ်ခုသည် တန်ဖိုးတစ်ခုကို ယူနိုင်မှု အလားအလာအကြောင်း ပြောနိုင်သည်၊ ဥပမာအားဖြင့် P(X=3)=1/6 ဖြစ်သည်။

ယခင်ဥပမာတွင် အလှည့်အပြောင်း အတန်းသည် **Discrete** ဟုခေါ်သည်၊ အကြောင်းမှာ ၎င်းတွင် ရေတွက်နိုင်သော နမူနာအကျယ်ရှိပြီး သီးခြားတန်ဖိုးများကို ရေတွက်နိုင်သည်။ နမူနာအကျယ်သည် အမှန်တကယ်နံပါတ်များ၏ အကွာအဝေး သို့မဟုတ် အမှန်တကယ်နံပါတ်များ၏ စုစုပေါင်းဖြစ်သော အခြေအနေများလည်း ရှိနိုင်သည်။ ၎င်းတို့ကို **Continuous** ဟုခေါ်သည်။ ကောင်းမွန်သော ဥပမာတစ်ခုမှာ ဘတ်စ်ကားရောက်ရှိချိန်ဖြစ်သည်။

## အလားအလာ ဖြန့်ဖြူးမှု

Discrete အလှည့်အပြောင်း အတန်းများ၏ အခြေအနေတွင် ဖြစ်ရပ်တစ်ခုစီ၏ အလားအလာကို P(X) ဟုခေါ်သော အလုပ်လုပ်ပုံတစ်ခုဖြင့် ဖော်ပြရန် လွယ်ကူသည်။ နမူနာအကျယ် *S* မှ တန်ဖိုး *s* တစ်ခုစီအတွက် ၎င်းသည် 0 မှ 1 အထိ နံပါတ်တစ်ခုကို ပေးမည်ဖြစ်ပြီး P(X=s) ၏ တန်ဖိုးအားလုံး၏ စုစုပေါင်းသည် 1 ဖြစ်ရမည်။

အလွန်ကျော်ကြားသော Discrete ဖြန့်ဖြူးမှုတစ်ခုမှာ **Uniform Distribution** ဖြစ်ပြီး ၎င်းတွင် N အစိတ်အပိုင်းများပါဝင်သော နမူနာအကျယ်ရှိပြီး ၎င်းတို့၏ တစ်ခုစီအတွက် အလားအလာမှာ 1/N ဖြစ်သည်။

Continuous အလှည့်အပြောင်း အတန်း၏ အလားအလာ ဖြန့်ဖြူးမှုကို ဖော်ပြရန် ပိုမိုခက်ခဲသည်၊ ၎င်းတွင် [a,b] အကွာအဝေး သို့မဟုတ် အမှန်တကယ်နံပါတ်များ၏ စုစုပေါင်း ℝ မှ တန်ဖိုးများကို ရယူသည်။ ဘတ်စ်ကားရောက်ရှိချိန်ကို စဉ်းစားပါ။ အမှန်တကယ်အားဖြင့် တိကျသောရောက်ရှိချိန် *t* တစ်ခုအတွက် ဘတ်စ်ကားသည် အတိအကျ ၎င်းအချိန်တွင် ရောက်ရှိနိုင်မှု အလားအလာမှာ 0 ဖြစ်သည်။

> အလားအလာ 0 ရှိသော ဖြစ်ရပ်များ ဖြစ်ပျက်တတ်ကြောင်း၊ အလွန်မကြာခဏ ဖြစ်ပျက်ကြောင်း သင်သိပြီးပါပြီ! အနည်းဆုံး ဘတ်စ်ကားရောက်ရှိသောအခါတိုင်း!

ကျွန်ုပ်တို့သည် တန်ဖိုးများ၏ အကွာအဝေးတစ်ခုတွင် အလှည့်အပြောင်း အတန်းတစ်ခုကျရောက်နိုင်မှု အလားအလာကိုသာ ပြောနိုင်သည်၊ ဥပမာအားဖြင့် P(t<sub>1</sub>≤X<t<sub>2</sub>)။ ဒီအခြေအနေတွင် အလားအလာ ဖြန့်ဖြူးမှုကို **Probability Density Function** p(x) ဖြင့် ဖော်ပြသည်၊ ၎င်းမှာ

![P(t_1\le X<t_2)=\int_{t_1}^{t_2}p(x)dx](../../../../1-Introduction/04-stats-and-probability/images/probability-density.png)

Continuous Uniform ဖြန့်ဖြူးမှုသည် Uniform Distribution ၏ Continuous အနုစဉ်ဖြစ်ပြီး အကွာအဝေးတစ်ခုအတွင်း သတ်မှတ်သည်။ X တန်ဖိုးသည် အကွာအဝေး l တစ်ခုတွင် ကျရောက်နိုင်မှု အလားအလာသည် l နှင့် အချိုးကျပြီး 1 အထိ မြင့်တက်သည်။

အရေးပါသော ဖြန့်ဖြူးမှုတစ်ခုမှာ **Normal Distribution** ဖြစ်ပြီး ကျွန်ုပ်တို့သည် အောက်တွင် ပိုမိုအသေးစိတ် ပြောပါမည်။

## ပျမ်းမျှတန်ဖိုး၊ အပြောင်းအလဲနှင့် စံချိန်လမ်းညွှန်

အလှည့်အပြောင်း အတန်း X ၏ နမူနာ n ခုကို x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub> ဟု ရေးဆွဲကြောင်း ယူဆပါစို့။ **ပျမ်းမျှတန်ဖိုး** (သို့မဟုတ် **အင်္ဂါရပ်ပျမ်းမျှ**) ကို x<sub>1</sub>+x<sub>2</sub>+x<sub>n</sub>/n ဟု ရိုးရှင်းသောနည်းဖြင့် သတ်မှတ်နိုင်သည်။ နမူနာအရွယ်အစားကို ကြီးထွားစေသောအခါ (n→∞ ဖြစ်သောအကန့်အသတ်ကို ယူပါ) ဖြန့်ဖြူးမှု၏ ပျမ်းမျှတန်ဖိုး (**မျှော်လင့်ချက်**) ကို ရရှိမည်။ **E**(x) ဟု မျှော်လင့်ချက်ကို ရေးမည်။

> Discrete ဖြန့်ဖြူးမှုတစ်ခုအတွက် {x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>N</sub>} တန်ဖိုးများနှင့် ၎င်းတို့၏ အလားအလာ p<sub>1</sub>, p<sub>2</sub>, ..., p<sub>N</sub> အတွက် မည်သည့်အခါမဆို မျှော်လင့်ချက်သည် E(X)=x<sub>1</sub>p<sub>1</sub>+x<sub>2</sub>p<sub>2</sub>+...+x<sub>N</sub>p<sub>N</sub> ဖြစ်ကြောင်း သက်သေပြနိုင်သည်။

တန်ဖိုးများသည် ဘယ်လောက်အထိ ပျံ့နှံ့နေသည်ကို သတ်မှတ်ရန် အပြောင်းအလဲ σ<sup>2</sup> = ∑(x<sub>i</sub> - μ)<sup>2</sup>/n ကို တွက်ချက်နိုင်သည်၊ ဤတွင် μ သည် နမူနာ၏ ပျမ်းမျှတန်ဖိုးဖြစ်သည်။ σ ကို **စံချိန်လမ်းညွှန်** ဟုခေါ်ပြီး σ<sup>2</sup> ကို **အပြောင်းအလဲ** ဟုခေါ်သည်။

## Mode, Median နှင့် Quartiles

တစ်ခါတစ်ရံ ပျမ်းမျှတန်ဖိုးသည် ဒေတာအတွက် "ပုံမှန်" တန်ဖိုးကို လုံလောက်စွာ ကိုယ်စားပြုမထားနိုင်ပါ။ ဥပမာအားဖြင့် အလွန်အမင်းသော တန်ဖိုးအချို့သည် အကန့်အသတ်အပြင်မှာရှိပြီး ၎င်းတို့သည် ပျမ်းမျှတန်ဖိုးကို သက်ရောက်စေနိုင်သည်။ အခြားသော ကောင်းမွန်သော အညွှန်းမှာ **Median** ဖြစ်ပြီး ဒေတာအချက်အလက်၏ တစ်ဝက်သည် ၎င်းထက် နိမ့်ပြီး အခြားတစ်ဝက်သည် - မြင့်သည်။

ဒေတာ၏ ဖြန့်ဖြူးမှုကို နားလည်ရန် Quartiles အကြောင်း ပြောခြင်းက အကျိုးရှိသည်-

* ပထမ Quartile သို့မဟုတ် Q1 သည် ဒေတာ၏ 25% သည် ၎င်းထက် နိမ့်ကျသော တန်ဖိုးဖြစ်သည်။
* တတိယ Quartile သို့မဟုတ် Q3 သည် ဒေတာ၏ 75% သည် ၎င်းထက် နိမ့်ကျသော တန်ဖိုးဖြစ်သည်။

Median နှင့် Quartiles တို့၏ ဆက်စပ်မှုကို **Box Plot** ဟုခေါ်သော အကြောင်းအရာတွင် ရှင်းလင်းဖော်ပြနိုင်သည်-

<img src="images/boxplot_explanation.png" width="50%"/>

ဒီမှာ **Inter-quartile Range** IQR=Q3-Q1 ကို တွက်ချက်ပြီး **Outliers** ဟုခေါ်သော တန်ဖိုးများကို တွေ့ရှိသည် - [Q1-1.5*IQR,Q3+1.5*IQR] အကန့်အသတ်များအပြင်ရှိသော တန်ဖိုးများ။

နည်းနည်းသော တန်ဖိုးများပါဝင်သော နမူနာဖြန့်ဖြူးမှုအတွက် "ပုံမှန်" တန်ဖိုးက အများဆုံး ထပ်တလဲလဲ ဖြစ်သော တန်ဖိုးဖြစ်ပြီး ၎င်းကို **Mode** ဟုခေါ်သည်။ ၎င်းကို အရောင်များကဲ့သို့ Categorized ဒေတာများတွင် အများအားဖြင့် အသုံးပြုသည်။ ဥပမာအားဖြင့် လူအုပ်နှစ်စုရှိသည် - အနီရောင်ကို အလွန်နှစ်သက်သောအုပ်စုတစ်ခုနှင့် အပြာရောင်ကို နှစ်သက်သောအုပ်စုတစ်ခု။ အရောင်များကို နံပါတ်များဖြင့် ကုဒ်ပြုလုပ်ပါက အကြိုက်ဆုံးအရောင်အတွက် ပျမ်းမျှတန်ဖိုးသည် လိမ္မော်-အစိမ်းရောင် အကွာအဝေးတွင် ရှိမည်ဖြစ်ပြီး ၎င်းသည် အုပ်စုနှစ်ခု၏ အကြိုက်ကို မကိုယ်စားပြုနိုင်ပါ။ သို့သော် Mode သည် အရောင်တစ်ခု သို့မဟုတ် လူအုပ်နှစ်စု၏ အရေအတွက်တူညီပါက အရောင်နှစ်ခုလုံးဖြစ်နိုင်သည် (ဤအခြေအနေတွင် **Multimodal** ဟုခေါ်သည်)။

## အမှန်တကယ် ဒေတာ

အမှန်တကယ် ဒေတာကို ခွဲခြမ်းစိတ်ဖြာသောအခါ ၎င်းတို့သည် အလှည့်အပြောင်း အတန်းများ မဟုတ်သော အခြေအနေများ များစွာရှိသည်၊ အဓိကအားဖြင့် ကျွန်ုပ်တို့ မသိသောရလဒ်များဖြင့် စမ်းသပ်မှုများ မပြုလုပ်သောအခါ။ ဥပမာအားဖြင့် ဘေ့စ်ဘောကစားသမားအဖွဲ့တစ်ခုနှင့် ၎င်းတို့၏ ကိုယ်ခန္ဓာဒေတာများ၊ အမြင့်၊ အလေးချိန်နှင့် အသက်ကဲ့သို့သော ဒေတာများကို စဉ်းစားပါ။ ၎င်းတို့သည် အလှည့်အပြောင်း အတန်းများ မဟုတ်သော်လည်း အလားတူ သင်္ချာဆိုင်ရာ အယူအဆများကို အသုံးပြုနိုင်သည်။ ဥပမာအားဖြင့် လူများ၏ အလေးချိန်များ၏ အစဉ်သည် အလှည့်အပြောင်း အတန်းတစ်ခုမှ ရယူသော တန်ဖိုးများ၏ အစဉ်အဖြစ် ယူဆနိုင်သည်။ အောက်တွင် [Major League Baseball](http://mlb.mlb.com/index.jsp) မှ ဘေ့စ်ဘောကစားသမားများ၏ အလေးချိန်များ၏ အစဉ်ကို [ဒီဒေတာ](http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights) မှ ယူထားသည် (သင့်အဆင်ပြေစေရန် ပထမ 20 တန်ဖိုးများကိုသာ ဖော်ပြထားသည်)။

```
[180.0, 215.0, 210.0, 210.0, 188.0, 176.0, 209.0, 200.0, 231.0, 180.0, 188.0, 180.0, 185.0, 160.0, 180.0, 185.0, 197.0, 189.0, 185.0, 219.0]
```

> **Note**: ဒီဒေတာကို အသုံးပြု၍ အလုပ်လုပ်ပုံကို ကြည့်ရန် [အတူတကွ Notebook](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb) ကို ကြည့်ပါ။ ဒီသင်ခန်းစာတစ်လျှောက်တွင် စိန်ခေါ်မှုများစွာရှိပြီး ၎င်းတို့ကို Notebook တွင် Code အချို့ ထည့်သွင်းခြင်းဖြင့် ပြီးမြောက်နိုင်သည်။ ဒေတာကို လုပ်ဆောင်ပုံ မသိပါက စိတ်မပူပါနှင့် - ကျွန်ုပ်တို့သည် Python ကို အသုံးပြု၍ ဒေတာနှင့် အလုပ်လုပ်ခြင်းကို နောက်ပိုင်းတွင် ပြန်လည်ဆွေးနွေးပါမည်။ Jupyter Notebook တွင် Code ကို အကောင်အထည်ဖော်ရန် မသိပါက [ဒီဆောင်းပါး](https://soshnikov.com/education/how-to-execute-notebooks-from-github/) ကို ကြည့်ပါ။

ဒီမှာ ကျွန်ုပ်တို့၏ ဒေတာအတွက် ပျမ်းမျှတန်ဖိုး၊ Median နှင့် Quartiles ကို ဖော်ပြသော Box Plot ဖြစ်သည်-

![Weight Box Plot](../../../../1-Introduction/04-stats-and-probability/images/weight-boxplot.png)

ကျွန်ုပ်တို့၏ ဒေတာတွင် ကစားသမား **အခန်းကဏ္ဍ** များအကြောင်း အချက်အလက်များပါဝင်သောကြောင့် Box Plot ကို အခန်းကဏ္ဍအလိုက် ပြုလုပ်နိုင်သည် - ၎င်းသည် အချက်အလက်များ၏ တန်ဖိုးများသည် အခန်းကဏ္ဍအလိုက် ဘယ်လို ကွဲပြားနေသည်ကို နားလည်စေမည်။ ဒီအကြိမ်မှာ ကျွန်ုပ်တို့ အမြင့်ကို စဉ်းစားပါမည်-

![Box plot by role](../../../../1-Introduction/04-stats-and-probability/images/boxplot_byrole.png)

ဒီဇယားက ပထမအမြင့်ကစားသမားများ၏ အမြင့်သည် ဒုတိယအမြင့်ကစားသမားများထက် ပျမ်းမျှအားဖြင့် မြင့်ကြောင်း အကြံပြုသည်။ ဒီသင်ခန်းစာတွင် ကျွန်ုပ်တို့သည် ဒီအယူအဆကို ပိုမိုတိကျစွာ စမ်းသပ်နိုင်ပုံနှင့် ဒေတာသည် သက်သေပြနိုင်သော အချက်အလက်ဖြစ်ကြောင်း သက်သေပြနိုင်ပုံကို လေ့လာပါမည်။

> အမှန်တကယ် ဒေတာနှင့် အလုပ်လုပ်သောအခါ ကျွန်ုပ်တို့သည် ဒေတာအချက်အလက်အားလုံးသည် အလားအလာ ဖြန့်ဖြူးမှုတစ်ခုမှ ရယူသော နမူနာများဖြစ်ကြောင်း ယူဆသည်။ ဒီယူဆချက်က ကျွန်ုပ်တို့ကို Machine Learning နည်းလမ်းများကို အသုံးပြုရန်နှင့် အလုပ်လုပ်နိုင်သော ခန့်မှန်းမော်ဒယ်များ တည်ဆောက်ရန် ခွင့်ပြုသည်။

ကျွန်ုပ်တို့၏ ဒေတာဖြန့်ဖြူးမှုကို ကြည့်ရန် **Histogram** ဟုခေါ်သော ဇယားတစ်ခုကို ရေးဆွဲနိုင်သည်။ X-axis တွင် အလေးချိန်အကွာအဝေးများ (သို့

1</sub>, ..., X<sub>n</sub> ကို ကျွန်ုပ်တို့၏ distribution မှ sample အဖြစ် ရယူပါ။ Distribution မှ sample တစ်ခုစီကို ရယူတိုင်း mean value μ က မတူညီသော တန်ဖိုးဖြစ်လာမည်။ ထို့ကြောင့် μ ကို random variable အဖြစ် သတ်မှတ်နိုင်သည်။ **Confidence interval** သည် confidence p နှင့်အတူ (L<sub>p</sub>,R<sub>p</sub>) တန်ဖိုးနှစ်ခုဖြစ်ပြီး **P**(L<sub>p</sub>≤μ≤R<sub>p</sub>) = p ဖြစ်သည်။ အဆိုပါ interval အတွင်း mean value ရောက်ရှိနိုင်မည့် probability သည် p ဖြစ်သည်။

Confidence interval များကို ဘယ်လိုတွက်ချက်ရမည်ဆိုသည်ကို အကြမ်းဖျင်းအနေနှင့်သာ ရှင်းပြထားပြီး အသေးစိတ်ကို မဖော်ပြပါ။ [Wikipedia](https://en.wikipedia.org/wiki/Confidence_interval) တွင် အသေးစိတ်ကို ရှာဖွေကြည့်နိုင်သည်။ အကျဉ်းချုပ်အားဖြင့် population၏ true mean နှင့် computed sample mean distribution ကို **student distribution** ဟုခေါ်သည်။

> **စိတ်ဝင်စားစရာအချက်**: Student distribution ကို mathematician William Sealy Gosset မှ တီထွင်ခဲ့ပြီး "Student" ဟု အမည်ပေး၍ စာတမ်းတင်ခဲ့သည်။ သူသည် Guinness brewery တွင် အလုပ်လုပ်ခဲ့ပြီး statistical tests ကို raw materials quality စစ်ဆေးရန် အသုံးပြုသည်ကို အများပြည်သူသိစေချင်ခြင်းမရှိသောကြောင့် pseudonym ကို အသုံးပြုခဲ့သည်။

Population၏ mean μ ကို confidence p ဖြင့် ခန့်မှန်းလိုပါက Student distribution A ၏ *(1-p)/2-th percentile* ကို ရယူရမည်။ Tables မှာ ရှာဖွေခြင်းဖြစ်စေ၊ statistical software (ဥပမာ Python, R စသည်) ၏ built-in functions အသုံးပြုခြင်းဖြစ်စေ ရယူနိုင်သည်။ μ အတွက် interval သည် X±A*D/√n ဖြစ်ပြီး X သည် sample၏ mean ဖြစ်သည်။ D သည် standard deviation ဖြစ်သည်။

> **မှတ်ချက်**: Student distribution နှင့်ဆက်စပ်သော [degrees of freedom](https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics)) အရေးပါသော အကြောင်းအရာကို မဖော်ပြပါ။ Statistics အကြောင်းကို နက်နက်ရှိုင်းရှိုင်း လေ့လာလိုပါက စာအုပ်များကို ဖတ်ရှုနိုင်သည်။

Weight နှင့် height အတွက် confidence interval တွက်ချက်မှုကို [accompanying notebooks](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb) တွင် ရှာဖွေကြည့်နိုင်သည်။

| p | Weight mean |
|-----|-----------|
| 0.85 | 201.73±0.94 |
| 0.90 | 201.73±1.08 |
| 0.95 | 201.73±1.28 |

Confidence probability မြင့်မည်ဆိုလျှင် confidence interval ပိုကျယ်လာမည်ကို သတိပြုပါ။

## Hypothesis Testing 

Baseball players dataset တွင် player roles များကို အောက်ပါအတိုင်း စုစည်းထားသည် ([accompanying notebook](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb) တွင် table တွက်ချက်ပုံကို ကြည့်နိုင်သည်):

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

First basemen ၏ mean height သည် second basemen ထက် မြင့်သည်ကို သတိပြုမိနိုင်သည်။ ထို့ကြောင့် **first basemen သည် second basemen ထက် မြင့်သည်** ဟု သတ်မှတ်လို temptation ရှိနိုင်သည်။

> အဆိုပါ statement ကို **hypothesis** ဟုခေါ်သည်။ အချက်အလက်သည် အမှန်ဖြစ်မဖြစ် မသိရသေးသောကြောင့် hypothesis ဖြစ်သည်။

သို့သော် အဆိုပါအချက်ကို သတ်မှတ်နိုင်မည့် အခြေအနေသည် အမြဲမရှိပါ။ အထက်တွင် ဖော်ပြထားသောအတိုင်း mean တစ်ခုစီတွင် confidence interval ပါရှိပြီး statistical error ဖြစ်နိုင်သည်။ Hypothesis ကို စစ်ဆေးရန် formal method တစ်ခုလိုအပ်သည်။

First basemen နှင့် second basemen height များအတွက် confidence interval ကို သီးခြားတွက်ချက်ကြည့်ပါ:

| Confidence | First Basemen | Second Basemen |
|------------|---------------|----------------|
| 0.85 | 73.62..74.38 | 71.04..71.69 |
| 0.90 | 73.56..74.44 | 70.99..71.73 |
| 0.95 | 73.47..74.53 | 70.92..71.81 |

Confidence မည်သည့်အဆင့်တွင်မဆို interval များ overlap မဖြစ်ပါ။ ထို့ကြောင့် first basemen သည် second basemen ထက် မြင့်သည်ဟု hypothesis ကို အတည်ပြုနိုင်သည်။

Formal အနေနှင့် ကျွန်ုပ်တို့၏ problem သည် **two probability distributions တူညီကြောင်း** သို့မဟုတ် အနည်းဆုံး parameters တူညီကြောင်း စစ်ဆေးခြင်းဖြစ်သည်။ Distribution အမျိုးအစားပေါ်မူတည်၍ test များကို အသုံးပြုရမည်။ Distribution များသည် normal ဖြစ်ကြောင်း သိပါက **[Student t-test](https://en.wikipedia.org/wiki/Student%27s_t-test)** ကို အသုံးပြုနိုင်သည်။

Student t-test တွင် **t-value** ကို တွက်ချက်ပြီး variance ကို ထည့်သွင်းစဉ်းစားသည်။ T-value သည် **student distribution** ကို လိုက်နာသည်ကို သက်သေပြနိုင်ပြီး confidence level **p** အတွက် threshold value ကို ရယူနိုင်သည် (tables တွင် ရှာဖွေခြင်းဖြစ်စေ၊ computer တွင် တွက်ချက်ခြင်းဖြစ်စေ ရယူနိုင်သည်)။ T-value ကို threshold နှင့် နှိုင်းယှဉ်ပြီး hypothesis ကို အတည်ပြုရန် သို့မဟုတ် ပယ်ဖျက်ရန် ဆုံးဖြတ်နိုင်သည်။

Python တွင် **SciPy** package ကို အသုံးပြုနိုင်ပြီး `ttest_ind` function ပါဝင်သည်။ Function သည် t-value ကို တွက်ချက်ပေးပြီး confidence p-value ကို reverse lookup ပြုလုပ်သည်။ ထို့ကြောင့် confidence ကိုသာ ကြည့်ပြီး ဆုံးဖြတ်နိုင်သည်။

ဥပမာအားဖြင့် first basemen height နှင့် second basemen height ကို နှိုင်းယှဉ်ခြင်းတွင် အောက်ပါရလဒ်များရရှိသည်: 
```python
from scipy.stats import ttest_ind

tval, pval = ttest_ind(df.loc[df['Role']=='First_Baseman',['Height']], df.loc[df['Role']=='Designated_Hitter',['Height']],equal_var=False)
print(f"T-value = {tval[0]:.2f}\nP-value: {pval[0]}")
```
```
T-value = 7.65
P-value: 9.137321189738925e-12
```
ဤအခြေအနေတွင် p-value သည် အလွန်နည်းပါးပြီး first basemen သည် မြင့်ကြောင်း အတည်ပြုသော strong evidence ရှိသည်။

အခြား hypothesis များကိုလည်း စစ်ဆေးနိုင်သည်၊ ဥပမာ:
* Sample တစ်ခုသည် distribution တစ်ခုကို လိုက်နာကြောင်း သက်သေပြရန်
* Sample ၏ mean value သည် predefined value တစ်ခုနှင့် ကိုက်ညီကြောင်း သက်သေပြရန်
* Samples များ၏ mean value များကို နှိုင်းယှဉ်ရန် (ဥပမာ: အသက်အရွယ်အုပ်စုများအကြား happiness level များ၏ ကွာခြားချက်)

## Law of Large Numbers and Central Limit Theorem

Normal distribution အရေးပါမှုအကြောင်းကို **central limit theorem** ဖြင့် ရှင်းပြနိုင်သည်။ N values X<sub>1</sub>, ..., X<sub>N</sub> ကို independent sample အဖြစ် ရယူပြီး mean μ နှင့် variance σ<sup>2</sup> ရှိသော distribution မှ ရယူပါ။ N သည် အလွန်ကြီးမားသောအခါ (N→∞) mean Σ<sub>i</sub>X<sub>i</sub> သည် normal distribution ဖြစ်လာမည်။ Mean သည် μ ဖြစ်ပြီး variance သည် σ<sup>2</sup>/N ဖြစ်သည်။

> Central limit theorem ကို အခြားနည်းဖြင့် ရှင်းပြနိုင်သည်။ Distribution မည်သည့်အမျိုးအစားဖြစ်စေ random variable values များ၏ mean ကို တွက်ချက်ပါက normal distribution ရရှိမည်။

Central limit theorem မှ N→∞ ဖြစ်သောအခါ sample mean သည် μ နှင့် တူညီမည် probability သည် 1 ဖြစ်သည်ကို သက်သေပြနိုင်သည်။ ဤအချက်ကို **law of large numbers** ဟုခေါ်သည်။

## Covariance and Correlation

Data Science ၏ အရေးပါသော အလုပ်တစ်ခုမှာ data များအကြား ဆက်နွယ်မှုကို ရှာဖွေခြင်းဖြစ်သည်။ Sequence နှစ်ခု **correlate** ဖြစ်သည်ဟု ဆိုသည်မှာ တစ်ချိန်တည်းတွင် တူညီသော အပြုအမူကို ပြသခြင်းဖြစ်သည်။ ဥပမာ: တစ်ခုတက်သည့်အခါ တစ်ခုလည်းတက်ခြင်း၊ တစ်ခုကျသည့်အခါ တစ်ခုလည်းကျခြင်း၊ သို့မဟုတ် တစ်ခုတက်သည့်အခါ တစ်ခုကျခြင်း။

> Correlation သည် causal relationship ကို မသက်သေပြနိုင်ပါ။ Sequence နှစ်ခုသည် အခြားအကြောင်းအရာတစ်ခုကြောင့် ဆက်နွယ်နေခြင်းဖြစ်နိုင်သည်၊ သို့မဟုတ် chance ကြောင့် correlation ဖြစ်နိုင်သည်။ သို့သော် strong mathematical correlation သည် variable နှစ်ခု ဆက်နွယ်နေကြောင်း သက်သေပြနိုင်သည်။

Mathematically, random variables နှစ်ခုအကြား ဆက်နွယ်မှုကို **covariance** ဖြင့် ဖော်ပြနိုင်သည်။ Cov(X,Y) = **E**\[(X-**E**(X))(Y-**E**(Y))\] ဖြစ်သည်။ Variable နှစ်ခု၏ mean value မှ deviation ကို တွက်ချက်ပြီး deviation များ၏ product ကို ရယူသည်။ Variable နှစ်ခုသည် တစ်ချိန်တည်းတွင် deviation ဖြစ်ပါက positive covariance ရရှိမည်။ Variable နှစ်ခုသည် out-of-sync ဖြစ်ပါက negative covariance ရရှိမည်။ Variable များသည် မဆက်နွယ်ပါက covariance သည် 0 အနီးတွင် ရှိမည်။

Covariance ၏ absolute value သည် correlation ၏ အရွယ်အစားကို မပြသနိုင်ပါ။ ထို့ကြောင့် covariance ကို variable နှစ်ခု၏ standard deviation ဖြင့် ခွဲခြားပြီး **correlation** ကို ရယူရမည်။ Correlation သည် [-1,1] အတွင်းရှိပြီး 1 သည် strong positive correlation ကို ပြသသည်။ -1 သည် strong negative correlation ကို ပြသသည်။ 0 သည် correlation မရှိကြောင်း (independent) ကို ပြသသည်။

**ဥပမာ**: Baseball players dataset မှ weight နှင့် height အကြား correlation ကို တွက်ချက်ပါ:
```python
print(np.corrcoef(weights,heights))
```
ရလဒ်အနေဖြင့် **correlation matrix** ကို ရရှိမည်:
```
array([[1.        , 0.52959196],
       [0.52959196, 1.        ]])
```

> Correlation matrix C ကို input sequences S<sub>1</sub>, ..., S<sub>n</sub> အတွက် တွက်ချက်နိုင်သည်။ C<sub>ij</sub> သည် S<sub>i</sub> နှင့် S<sub>j</sub> အကြား correlation ဖြစ်ပြီး diagonal elements သည် အမြဲ 1 ဖြစ်သည်။

ဤအခြေအနေတွင် 0.53 သည် weight နှင့် height အကြား correlation ရှိကြောင်း ပြသသည်။ Scatter plot ကို ပြုလုပ်၍ relationship ကို visually ကြည့်နိုင်သည်:

![Relationship between weight and height](../../../../1-Introduction/04-stats-and-probability/images/weight-height-relationship.png)

> Correlation နှင့် covariance အကြောင်းကို [accompanying notebook](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb) တွင် ရှာဖွေကြည့်နိုင်သည်။

## Conclusion

ဤအပိုင်းတွင် ကျွန်ုပ်တို့ သင်ယူခဲ့သည်မှာ:

* data ၏ basic statistical properties (mean, variance, mode, quartiles)
* random variable distributions (normal distribution အပါအဝင်)
* properties များအကြား correlation ရှာဖွေခြင်း
* math နှင့် statistics apparatus ကို hypothesis အတည်ပြုရန် အသုံးပြုခြင်း
* data sample ကို အသုံးပြု၍ random variable ၏ confidence intervals တွက်ချက်ခြင်း

Probability နှင့် statistics ၏ အခြေခံအချက်များကို သင်ယူခဲ့ပြီး သင်ခန်းစာကို စတင်ရန် လုံလောက်သည်။

## 🚀 Challenge

Notebook တွင် sample code ကို အသုံးပြု၍ အောက်ပါ hypothesis များကို စမ်းသပ်ပါ:
1. First basemen သည် second basemen ထက် အသက်ကြီးသည်။
2. First basemen သည် third basemen ထက် မြင့်သည်။
3. Shortstops သည် second basemen ထက် မြင့်သည်။

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/7)

## Review & Self Study

Probability နှင့် statistics သည် အလွန်ကျယ်ပြန့်သော အကြောင်းအရာဖြစ်ပြီး သီးသန့်သင်တန်းတစ်ခုအဖြစ် သင်ယူရန် လိုအပ်သည်။ Theory ကို နက်နက်ရှိုင်းရှိုင်း လေ့လာလိုပါက အောက်ပါစာအုပ်များကို ဆက်လက်ဖတ်ရှုနိုင်သည်:

1. [Carlos Fernandez-Granda](https://cims.nyu.edu/~cfgranda/) (New York University) ၏ [Probability and Statistics for Data Science](https://cims.nyu.edu/~cfgranda/pages/stuff/probability_stats_for_DS.pdf) lecture notes (online တွင် ရရှိနိုင်သည်)
1. [Peter and Andrew Bruce. Practical Statistics for Data Scientists.](https://www.oreilly.com/library/view/practical-statistics-for/9781491952955/) [[sample code in R](https://github.com/andrewgbruce/statistics-for-data-scientists)]. 
1. [James D. Miller. Statistics for Data Science](https://www.packtpub.com/product/statistics-for-data-science/9781788290678) [[sample code in R](https://github.com/PacktPublishing/Statistics-for-Data-Science)]

## Assignment

[Small Diabetes Study](assignment.md)

## Credits

ဤသင်ခန်းစာကို [Dmitry Soshnikov](http://soshnikov.com) မှ ♥️ ဖြင့် ရေးသားထားသည်။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။