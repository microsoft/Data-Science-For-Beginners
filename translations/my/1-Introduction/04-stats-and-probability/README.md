<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8bbb3fa0d4ad61384a3b4b5f7560226f",
  "translation_date": "2025-09-05T05:23:10+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/README.md",
  "language_code": "my"
}
-->
# စာရင်းအင်းနှင့် အလားအလာအကြောင်း အကျဉ်းချုပ်

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/04-Statistics-Probability.png)|
|:---:|
| စာရင်းအင်းနှင့် အလားအလာ - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

စာရင်းအင်းနှင့် အလားအလာ သီအိုရီများသည် သင်္ချာ၏ အလွန်နီးစပ်သော နယ်ပယ်နှစ်ခုဖြစ်ပြီး ဒေတာသိပ္ပံတွင် အလွန်အရေးပါသည်။ သင်္ချာအကြောင်းနက်နက်ရှိုင်းရှိုင်း မသိဘဲ ဒေတာနှင့် လုပ်ဆောင်နိုင်သော်လည်း အခြေခံအယူအဆများကို အနည်းဆုံး သိထားခြင်းက ပိုမိုကောင်းမွန်ပါသည်။ ဒီမှာ သင်စတင်နိုင်ရန် အကျဉ်းချုပ်ကို တင်ပြပေးပါမည်။

[![Intro Video](../../../../1-Introduction/04-stats-and-probability/images/video-prob-and-stats.png)](https://youtu.be/Z5Zy85g4Yjw)

## [Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/6)

## အလားအလာနှင့် အလားအလာဆိုင်ရာ အပြောင်းအလဲများ

**အလားအလာ** ဆိုသည်မှာ 0 နှင့် 1 အကြားရှိ နံပါတ်တစ်ခုဖြစ်ပြီး **ဖြစ်ရပ်** တစ်ခုဖြစ်နိုင်မှုကို ဖော်ပြသည်။ ၎င်းကို အပေါင်းအဖွဲ့ဖြစ်ရပ်များ (ဖြစ်ရပ်ကို ဖြစ်စေသော) ကို အားလုံးဖြစ်နိုင်သော အဖြေများ၏ စုစုပေါင်းနဲ့ ခွဲခြင်းဖြင့် သတ်မှတ်သည်။ ဥပမာအားဖြင့် အံစာတုံးကို လွှဲလိုက်သောအခါ ကျွန်ုပ်တို့ အစုံနံပါတ်ရရှိနိုင်မှုမှာ 3/6 = 0.5 ဖြစ်သည်။

ဖြစ်ရပ်များအကြောင်း ပြောသောအခါ ကျွန်ုပ်တို့ **အလားအလာဆိုင်ရာ အပြောင်းအလဲများ** ကို အသုံးပြုသည်။ ဥပမာအားဖြင့် အံစာတုံးကို လွှဲလိုက်သောအခါ ရရှိသော နံပါတ်ကို ကိုယ်စားပြုသော အလားအလာဆိုင်ရာ အပြောင်းအလဲသည် 1 မှ 6 အထိ တန်ဖိုးများကို ယူပါမည်။ 1 မှ 6 အထိ နံပါတ်များ၏ စုစုပေါင်းကို **နမူနာအကျယ်** ဟုခေါ်သည်။ ကျွန်ုပ်တို့သည် အလားအလာဆိုင်ရာ အပြောင်းအလဲတစ်ခုသည် တန်ဖိုးတစ်ခုကို ယူနိုင်မှုအလားအလာကို ပြောနိုင်သည်၊ ဥပမာအားဖြင့် P(X=3)=1/6 ဖြစ်သည်။

ယခင်ဥပမာတွင် အလားအလာဆိုင်ရာ အပြောင်းအလဲသည် **Discrete** ဟုခေါ်သည်၊ အကြောင်းမှာ ၎င်းတွင် ရေတွက်နိုင်သော နမူနာအကျယ်ရှိပြီး၊ သီးခြားတန်ဖိုးများကို ရေတွက်နိုင်သည်။ နမူနာအကျယ်သည် အမှန်တကယ်နံပါတ်များ၏ အကွာအဝေး သို့မဟုတ် အမှန်တကယ်နံပါတ်များ၏ စုစုပေါင်းဖြစ်သော အခြေအနေများရှိသည်။ ၎င်းတို့ကို **Continuous** ဟုခေါ်သည်။ ဥပမာအားဖြင့် ဘတ်စ်ကားရောက်ရှိချိန်သည် Continuous အလားအလာဆိုင်ရာ အပြောင်းအလဲတစ်ခုဖြစ်သည်။

## အလားအလာဖြန့်ဖြူးမှု

Discrete အလားအလာဆိုင်ရာ အပြောင်းအလဲများ၏ အခြေအနေတွင် ဖြစ်ရပ်တစ်ခုစီ၏ အလားအလာကို P(X) ဟုခေါ်သော အလုပ်ဆောင်မှုဖြင့် ဖော်ပြရန် လွယ်ကူသည်။ နမူနာအကျယ် *S* မှ တန်ဖိုး *s* တစ်ခုစီအတွက် 0 မှ 1 အထိ နံပါတ်တစ်ခုကို ပေးပြီး၊ P(X=s) ၏ တန်ဖိုးအားလုံး၏ စုစုပေါင်းသည် 1 ဖြစ်ရမည်။

အလွန်ကျော်ကြားသော Discrete ဖြန့်ဖြူးမှုတစ်ခုမှာ **Uniform Distribution** ဖြစ်ပြီး၊ ၎င်းတွင် N အစိတ်အပိုင်းများပါရှိသော နမူနာအကျယ်ရှိပြီး၊ ၎င်းတို့၏ တစ်ခုစီအတွက် အလားအလာမှာ 1/N ဖြစ်သည်။

Continuous အလားအလာဆိုင်ရာ အပြောင်းအလဲ၏ အလားအလာဖြန့်ဖြူးမှုကို ဖော်ပြရန် ပိုမိုခက်ခဲသည်၊ အကြောင်းမှာ ၎င်းတွင် [a,b] အကွာအဝေး သို့မဟုတ် အမှန်တကယ်နံပါတ်များ၏ စုစုပေါင်း ℝ မှ တန်ဖိုးများကို ရယူသည်။ ဘတ်စ်ကားရောက်ရှိချိန်ကို စဉ်းစားပါ။ အမှန်တကယ်တွင် တိကျသောရောက်ရှိချိန် *t* တစ်ခုအတွက် ဘတ်စ်ကားသည် အတိအကျအချိန်၌ ရောက်ရှိနိုင်မှုအလားအလာမှာ 0 ဖြစ်သည်။

> အလားအလာ 0 ရှိသော ဖြစ်ရပ်များသည် ဖြစ်ပျက်တတ်ပြီး၊ အနည်းဆုံး ဘတ်စ်ကားရောက်ရှိသောအချိန်တိုင်း ဖြစ်ပျက်သည်။

ကျွန်ုပ်တို့သည် အလားအလာဆိုင်ရာ အပြောင်းအလဲတစ်ခုသည် တန်ဖိုးများ၏ အကွာအဝေးတစ်ခုတွင် ရောက်ရှိနိုင်မှုအလားအလာကိုသာ ပြောနိုင်သည်၊ ဥပမာအားဖြင့် P(t<sub>1</sub>≤X<t<sub>2</sub>) ဖြစ်သည်။ ဒီအခြေအနေတွင် အလားအလာဖြန့်ဖြူးမှုကို **အလားအလာသိပ်သည်းမှုလုပ်ဆောင်မှု** p(x) ဖြင့် ဖော်ပြသည်၊ ၎င်းမှာ

![P(t_1\le X<t_2)=\int_{t_1}^{t_2}p(x)dx](../../../../1-Introduction/04-stats-and-probability/images/probability-density.png)

Continuous Uniform ဖြန့်ဖြူးမှုသည် Uniform Distribution ၏ Continuous အနုနယ်ဖြစ်ပြီး၊ ၎င်းကို အကွာအဝေးတစ်ခုအတွင်း သတ်မှတ်သည်။ တန်ဖိုး X သည် အကွာအဝေးတစ်ခု၏ အလျား l တွင် ရောက်ရှိနိုင်မှုအလားအလာသည် l နှင့် အချိုးကျပြီး 1 အထိ မြင့်တက်သည်။

အခြားအရေးပါသော ဖြန့်ဖြူးမှုတစ်ခုမှာ **Normal Distribution** ဖြစ်ပြီး၊ ကျွန်ုပ်တို့သည် အောက်တွင် ပိုမိုအသေးစိတ်ဆွေးနွေးမည်။

## ပျမ်းမျှတန်ဖိုး၊ အပြောင်းအလဲနှင့် စံချိန်လှိုင်း

အလားအလာဆိုင်ရာ အပြောင်းအလဲ X ၏ နမူနာများ n ခုကို ဆွဲယူကြောင်း ယူဆပါစို့ - x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>။ **ပျမ်းမျှတန်ဖိုး** (သို့မဟုတ် **အင်္ဂါရပ်ပျမ်းမျှ**) ကို အဆင့်မတူသောနည်းလမ်းဖြင့် သတ်မှတ်နိုင်သည် - (x<sub>1</sub>+x<sub>2</sub>+x<sub>n</sub>)/n။ နမူနာအရွယ်အစားကို ကြီးထွားစေသောအခါ (n→∞ ဖြစ်သောအကန့်အသတ်ကို ယူသောအခါ) ဖြန့်ဖြူးမှု၏ ပျမ်းမျှတန်ဖိုး (သို့မဟုတ် **မျှော်မှန်းချက်**) ကို ရရှိမည်။ **E**(x) ဟု မျှော်မှန်းချက်ကို မှတ်သားမည်။

> Discrete ဖြန့်ဖြူးမှုတစ်ခုသည် {x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>N</sub>} တန်ဖိုးများနှင့် p<sub>1</sub>, p<sub>2</sub>, ..., p<sub>N</sub> အလားအလာများပါရှိသည်ဟု ယူဆပါက၊ မျှော်မှန်းချက်သည် E(X)=x<sub>1</sub>p<sub>1</sub>+x<sub>2</sub>p<sub>2</sub>+...+x<sub>N</sub>p<sub>N</sub> ဖြစ်သည်။

တန်ဖိုးများသည် ဘယ်လောက်အထိ ပျံ့နှံ့နေသည်ကို သိရန်၊ အပြောင်းအလဲ σ<sup>2</sup> = ∑(x<sub>i</sub> - μ)<sup>2</sup>/n ကို တွက်ချက်နိုင်သည်၊ ဤတွင် μ သည် နမူနာ၏ ပျမ်းမျှတန်ဖိုးဖြစ်သည်။ σ ကို **စံချိန်လှိုင်း** ဟုခေါ်ပြီး၊ σ<sup>2</sup> ကို **အပြောင်းအလဲ** ဟုခေါ်သည်။

## Mode, Median နှင့် Quartiles

တစ်ခါတစ်ရံ ပျမ်းမျှတန်ဖိုးသည် ဒေတာ၏ "ပုံမှန်" တန်ဖိုးကို မလုံလောက်စွာ ကိုယ်စားပြုနိုင်ပါ။ ဥပမာအားဖြင့် အလွန်အမင်းတန်ဖိုးများရှိသောအခါ၊ ၎င်းတို့သည် ပျမ်းမျှတန်ဖိုးကို အကျိုးသက်ရောက်စေနိုင်သည်။ **Median** သည် ဒေတာအချက်အလက်၏ တစ်ဝက်သည် ၎င်းထက် နိမ့်ပြီး၊ တစ်ဝက်သည် ၎င်းထက် မြင့်သော တန်ဖိုးဖြစ်သည်။

Quartiles ကို အသုံးပြုခြင်းသည် ဒေတာဖြန့်ဖြူးမှုကို နားလည်ရန် အထောက်အကူဖြစ်သည်။

* **ပထမ Quartile** (Q1) သည် ဒေတာ၏ 25% သည် ၎င်းထက် နိမ့်သော တန်ဖိုးဖြစ်သည်။
* **တတိယ Quartile** (Q3) သည် ဒေတာ၏ 75% သည် ၎င်းထက် နိမ့်သော တန်ဖိုးဖြစ်သည်။

Median နှင့် Quartiles တို့၏ ဆက်စပ်မှုကို **Box Plot** ဟုခေါ်သော အကြောင်းအရာတွင် ရှင်းလင်းဖော်ပြနိုင်သည်။

<img src="images/boxplot_explanation.png" width="50%"/>

ဒီမှာ **Inter-quartile Range** IQR=Q3-Q1 ကို တွက်ချက်ပြီး၊ **Outliers** ဟုခေါ်သော တန်ဖိုးများကို တွေ့နိုင်သည်။ Outliers သည် [Q1-1.5*IQR,Q3+1.5*IQR] အကန့်အသတ်များအပြင်ရှိသော တန်ဖိုးများဖြစ်သည်။

နည်းနည်းသော တန်ဖိုးများပါရှိသော Discrete ဖြန့်ဖြူးမှုအတွက် "ပုံမှန်" တန်ဖိုးက အများဆုံးကြိမ်ရောက်သော တန်ဖိုးဖြစ်ပြီး၊ ၎င်းကို **Mode** ဟုခေါ်သည်။ Mode ကို အရောင်များကဲ့သို့ Categorized ဒေတာတွင် အသုံးပြုနိုင်သည်။ ဥပမာအားဖြင့် လူအုပ်နှစ်အုပ်ရှိပြီး၊ တစ်အုပ်သည် အနီရောင်ကို နှစ်သက်ပြီး၊ တစ်အုပ်သည် အပြာရောင်ကို နှစ်သက်သည်။ Mode သည် အနီရောင် သို့မဟုတ် အပြာရောင်ဖြစ်နိုင်ပြီး၊ လူအရေအတွက်တူညီပါက **Multimodal** ဟုခေါ်သည်။

## အမှန်တကယ် ဒေတာ

အမှန်တကယ် ဒေတာကို ခွဲခြားသောအခါ၊ ၎င်းတို့သည် အလားအလာဆိုင်ရာ အပြောင်းအလဲများမဟုတ်ပါ၊ အကြောင်းမှာ ကျွန်ုပ်တို့သည် မသိသောရလဒ်များဖြင့် စမ်းသပ်မှုများ မလုပ်ဆောင်ပါ။ ဥပမာအားဖြင့် ဘေ့စ်ဘောကစားသမားအဖွဲ့တစ်ခုနှင့် ၎င်းတို့၏ ကိုယ်ခန္ဓာဒေတာများ၊ height, weight နှင့် age ကဲ့သို့သော ဒေတာများကို စဉ်းစားပါ။ ၎င်းတို့သည် တိကျသော အလားအလာဆိုင်ရာ အပြောင်းအလဲများမဟုတ်သော်လည်း၊ အလားအလာသီအိုရီများကို အလွယ်တကူ အသုံးပြုနိုင်သည်။

```
[180.0, 215.0, 210.0, 210.0, 188.0, 176.0, 209.0, 200.0, 231.0, 180.0, 188.0, 180.0, 185.0, 160.0, 180.0, 185.0, 197.0, 189.0, 185.0, 219.0]
```

> **Note**: ဒီဒေတာကို အသုံးပြု၍ အလုပ်လုပ်နည်းကို [accompanying notebook](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb) တွင် ကြည့်ရှုနိုင်သည်။ ၎င်းသင်ခန်းစာတွင် စိန်ခေါ်မှုများစွာပါရှိပြီး၊ notebook တွင် code ထည့်သွင်းခြင်းဖြင့် ပြီးမြောက်နိုင်သည်။ Python အသုံးပြု၍ ဒေတာကို လုပ်ဆောင်နည်းကို ကျွန်ုပ်တို့ နောက်ပိုင်းတွင် ပြန်လည်ဆွေးနွေးမည်။

ဒီမှာ ကျွန်ုပ်တို့၏ ဒေတာအတွက် Mean, Median နှင့် Quartiles ကို ဖော်ပြသော Box Plot ဖြစ်သည်။

![Weight Box Plot](../../../../1-Introduction/04-stats-and-probability/images/weight-boxplot.png)

ကျွန်ုပ်တို့၏ ဒေတာတွင် ကစားသမား **Roles** များပါရှိသောကြောင့်၊ Role အလိုက် Box Plot ကို ပြုလုပ်နိုင်သည်။ ဒီအခါ Height ကို စဉ်းစားပါမည်။

![Box plot by role](../../../../1-Introduction/04-stats-and-probability/images/boxplot_byrole.png)

ဒီ Diagram က ပထမအခြေခံကစားသမားများ၏ Height သည် ဒုတိယအခြေခံကစားသမားများထက် ပျမ်းမျှအားဖြင့် မြင့်မားသည်ကို ဖော်ပြသည်။ 

> အမှန်တကယ် ဒေတာနှင့် အလုပ်လုပ်သောအခါ၊ ဒေတာအချက်အလက်များသည် အလားအလာဖြန့်ဖြူးမှုတစ်ခုမှ ဆွဲယူထားသော နမူနာများဖြစ်သည်ဟု ယူဆသည်။ 

## Normal Distribution

အပေါ်တွင် မြင်ရသော Weight ဖြန့်ဖြူးမှုသည် အလွန်ပုံမှန်ဖြစ်ပြီး၊ အများသော Measurement များသည် အလားတူဖြန့်ဖြူးမှုကို လိုက်နာသည်။ Normal Distribution သည် စာရင်းအင်းတွင် အရေးပါသော အခန်းကဏ္ဍတစ်ခုကို ထိန်းသိမ်းထားသည်။

```python
samples = np.random.normal(mean,std,1000)
```

Normal Distribution ကို အလွန်တိကျသော Histogram အနေဖြင့် ဖော်ပြနိုင်သည်။

![Normal Distribution with mean=0 and std.dev=1](../../../../1-Introduction/04-stats-and-probability/images/normal-histogram.png)

*Mean=0 နှင့် Std.dev=1 ဖြင့် Normal Distribution*

## Confidence Intervals

ဘေ့စ်ဘောကစားသမားများ၏ Weight အကြောင်း ပြောသောအခါ၊ **Random Variable W** တစ်ခုသည် ဘေ့စ်ဘောကစားသမားများ၏ Weight ဖြန့်ဖြူးမှုကို ကိုယ်စားပြုသည်ဟု ယူဆသည်။ 

Confidence Interval သည် Population ၏ Mean နှင့် Variance ကို သိနိုင်မှုအလားအလာကို ဖော်ပြသည်။
> **ယုံကြည်မှုအကွာအဝေး** ဆိုသည်မှာ ကျွန်ုပ်တို့ရရှိထားသော နမူနာအရ လူဦးရေ၏ အမှန်တကယ် အလယ်ပျံကို ခန့်မှန်းခြေခြင်းဖြစ်ပြီး၊ ၎င်းသည် တစ်ခုခုသော အလားအလာ (သို့မဟုတ် **ယုံကြည်မှုအဆင့်**) ဖြင့် တိကျမှုရှိသည်။
Suppose we have a sample X<sub>1</sub>, ..., X<sub>n</sub> from our distribution. Each time we draw a sample from our distribution, we would end up with different mean value μ. Thus μ can be considered to be a random variable. A **confidence interval** with confidence p is a pair of values (L<sub>p</sub>,R<sub>p</sub>), such that **P**(L<sub>p</sub>≤μ≤R<sub>p</sub>) = p, i.e. a probability of measured mean value falling within the interval equals to p.

ဤ confidence interval များကို တွက်ချက်ပုံကို အကြမ်းဖျင်းအနေနဲ့ ရှင်းလင်းထားပြီး အသေးစိတ် မဆွေးနွေးပါ။ အသေးစိတ်ကို [Wikipedia](https://en.wikipedia.org/wiki/Confidence_interval) တွင် ရှာဖွေကြည့်နိုင်ပါသည်။ အကြမ်းဖျင်းအားဖြင့် ကျွန်ုပ်တို့သည် sample mean ကို population mean နှင့် ဆက်စပ်ပြီး **student distribution** ဟုခေါ်သော distribution ကို သတ်မှတ်ပါသည်။

> **စိတ်ဝင်စားစရာအချက်**: Student distribution ကို mathematician William Sealy Gosset မှ နာမည်ပေးခဲ့သည်။ သူသည် "Student" ဟု အမည်လွှဲ၍ စာတမ်းတင်ခဲ့ပြီး Guinness brewery တွင် အလုပ်လုပ်ခဲ့သည်။ တစ်ခုသော version အရ သူ၏အလုပ်ရှင်သည် raw materials ၏ အရည်အသွေးကို သတ်မှတ်ရန် statistical tests ကို အသုံးပြုနေသည်ကို အများပြည်သူ မသိစေလိုခဲ့သည်။

Population mean μ ကို confidence p ဖြင့် ခန့်မှန်းလိုပါက *(1-p)/2-th percentile* ကို Student distribution A မှယူရမည်။ ဤ percentile ကို tables မှာ ရှာနိုင်သလို statistical software (ဥပမာ Python, R စသည်) ၏ built-in functions များကို အသုံးပြု၍ တွက်ချက်နိုင်ပါသည်။ ထို့နောက် μ အတွက် interval ကို X±A*D/√n ဖြင့် ရယူနိုင်ပါသည်။ ဤတွင် X သည် sample ၏ mean ဖြစ်ပြီး D သည် standard deviation ဖြစ်သည်။

> **Note**: Student distribution နှင့် ဆက်စပ်သော [degrees of freedom](https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics)) ၏ အရေးပါမှုကို ဤနေရာတွင် မဆွေးနွေးပါ။ ဤအကြောင်းအရာကို နက်နက်ရှိုင်းရှိုင်း နားလည်ရန် statistics အကြောင်းအရာပါသော စာအုပ်များကို ဖတ်ရှုနိုင်ပါသည်။

Weight နှင့် Height အတွက် confidence interval တွက်ချက်ပုံကို [accompanying notebooks](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb) တွင် ရှာဖွေကြည့်နိုင်ပါသည်။

| p | Weight mean |
|-----|-----------|
| 0.85 | 201.73±0.94 |
| 0.90 | 201.73±1.08 |
| 0.95 | 201.73±1.28 |

Confidence probability မြင့်မားသည့်အခါ confidence interval ကျယ်ပြန့်လာသည်ကို သတိပြုပါ။

## Hypothesis Testing 

Baseball players dataset တွင် player roles များကို အောက်ပါအတိုင်း စုစည်းထားသည် ([accompanying notebook](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb) တွင် ဤဇယားကို တွက်ချက်ပုံကို ကြည့်နိုင်ပါသည်):

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

First basemen ၏ mean height သည် second basemen ၏ mean height ထက် မြင့်မားသည်ကို သတိပြုနိုင်ပါသည်။ ထို့ကြောင့် **first basemen are higher than second basemen** ဟု သတ်မှတ်လို temptation ရှိနိုင်ပါသည်။

> ဤအဆိုကို **hypothesis** ဟုခေါ်သည်။ အချက်အလက်သည် အမှန်ဖြစ်မဖြစ် မသိသေးပါ။

သို့သော် ဤအဆိုကို သတ်မှတ်နိုင်မည်မဟုတ်ပါ။ အထက်တွင် ဆွေးနွေးခဲ့သည့်အတိုင်း mean တစ်ခုစီတွင် confidence interval ပါရှိပြီး statistical error ဖြစ်နိုင်ပါသည်။ Hypothesis ကို စမ်းသပ်ရန် formal method တစ်ခုလိုအပ်ပါသည်။

First basemen နှင့် Second basemen ၏ height များအတွက် confidence interval ကို သီးခြား တွက်ချက်ကြည့်ပါစို့:

| Confidence | First Basemen | Second Basemen |
|------------|---------------|----------------|
| 0.85 | 73.62..74.38 | 71.04..71.69 |
| 0.90 | 73.56..74.44 | 70.99..71.73 |
| 0.95 | 73.47..74.53 | 70.92..71.81 |

Confidence မည်သည့်အဆင့်တွင်မဆို interval များ overlap မဖြစ်ပါ။ ထို့ကြောင့် first basemen are higher than second basemen ဟု hypothesis ကို အတည်ပြုနိုင်ပါသည်။

Formal အနေနှင့် ကျွန်ုပ်တို့၏ ပြဿနာသည် **two probability distributions are the same** သို့မဟုတ် အနည်းဆုံး parameter များတူညီကြောင်း စစ်ဆေးခြင်းဖြစ်သည်။ Distribution အမျိုးအစားပေါ်မူတည်၍ test များကို အသုံးပြုရမည်။ Distribution များသည် normal ဖြစ်ကြောင်း သိပါက **[Student t-test](https://en.wikipedia.org/wiki/Student%27s_t-test)** ကို အသုံးပြုနိုင်ပါသည်။

Student t-test တွင် **t-value** ကို တွက်ချက်ပြီး variance ကို ထည့်သွင်းတွက်ချက်သည်။ t-value သည် **student distribution** ကို လိုက်နာသည်ဟု သက်သေပြထားပြီး confidence level **p** အတွက် threshold value ကို ရယူနိုင်သည် (tables တွင် ရှာနိုင်သလို computer ဖြင့် တွက်ချက်နိုင်ပါသည်)။ ထို့နောက် t-value ကို threshold နှင့် နှိုင်းယှဉ်၍ hypothesis ကို အတည်ပြု သို့မဟုတ် ပယ်ချနိုင်သည်။

Python တွင် **SciPy** package ကို အသုံးပြုနိုင်ပြီး `ttest_ind` function ပါဝင်သည်။ ဤ function သည် t-value ကို တွက်ချက်ပေးပြီး confidence p-value ကို reverse lookup ပြုလုပ်ပေးသည်။ ထို့ကြောင့် confidence ကို ကြည့်ပြီး အတည်ပြုချက်ကို ချမှတ်နိုင်သည်။

ဥပမာအားဖြင့် first basemen နှင့် second basemen height များကို နှိုင်းယှဉ်ခြင်းတွင် အောက်ပါရလဒ်များရရှိသည်: 
```python
from scipy.stats import ttest_ind

tval, pval = ttest_ind(df.loc[df['Role']=='First_Baseman',['Height']], df.loc[df['Role']=='Designated_Hitter',['Height']],equal_var=False)
print(f"T-value = {tval[0]:.2f}\nP-value: {pval[0]}")
```
```
T-value = 7.65
P-value: 9.137321189738925e-12
```
ဤအခါ p-value သည် အလွန်နည်းပါးပြီး first basemen are taller ဟု အတည်ပြုရန် strong evidence ရှိသည်။

အခြား hypothesis များကိုလည်း စမ်းသပ်နိုင်ပါသည်၊ ဥပမာ:
* Sample တစ်ခုသည် distribution တစ်ခုကို လိုက်နာကြောင်း သက်သေပြရန်
* Sample ၏ mean value သည် predefined value တစ်ခုနှင့် ကိုက်ညီကြောင်း သက်သေပြရန်
* Sample များစွာ၏ mean value များကို နှိုင်းယှဉ်ရန် (ဥပမာ အသက်အရွယ်အုပ်စုများအကြား happiness level များ၏ ကွာခြားချက်)

## Law of Large Numbers and Central Limit Theorem

Normal distribution ၏ အရေးပါမှုအကြောင်းအရာတစ်ခုမှာ **central limit theorem** ဖြစ်သည်။ N→∞ ဖြစ်သောအခါ independent N values X<sub>1</sub>, ..., X<sub>N</sub> ကို distribution မည်သည့်အမျိုးအစားမှမဆို sample လုပ်ပါက mean Σ<sub>i</sub>X<sub>i</sub> သည် normal distribution ဖြစ်လာမည်။ Mean သည် μ ဖြစ်ပြီး variance သည် σ<sup>2</sup>/N ဖြစ်သည်။

> Central limit theorem ကို အခြားနည်းဖြင့် အဓိပ္ပါယ်ဖွင့်ဆိုပါက random variable values များ၏ mean ကို တွက်ချက်ပါက normal distribution ကို ရရှိမည်ဟု ဆိုနိုင်သည်။

Central limit theorem မှ N→∞ ဖြစ်သောအခါ sample mean သည် μ နှင့် တူညီမည်ဟု သက်သေပြသည်။ ဤအချက်ကို **law of large numbers** ဟု ခေါ်သည်။

## Covariance and Correlation

Data Science ၏ အရေးပါမှုတစ်ခုမှာ data များအကြား ဆက်နွယ်မှုကို ရှာဖွေခြင်းဖြစ်သည်။ Sequence နှစ်ခု **correlate** သည်ဟု ဆိုပါက အချိန်တစ်ခုတည်းတွင် behavior တူညီမှုကို ပြသသည်။ Sequence နှစ်ခုလုံး တက်/ကျ ဖြစ်ခြင်း သို့မဟုတ် တစ်ခုတက်သောအခါ တစ်ခုကျခြင်းကို ပြသသည်။ အခြားနည်းဖြင့် Sequence နှစ်ခုအကြား ဆက်နွယ်မှုတစ်ခု ရှိသည်ဟု ဆိုနိုင်သည်။

> Correlation သည် causal relationship ကို မသက်သေပြနိုင်ပါ။ Sequence နှစ်ခုသည် အခြားအကြောင်းအရာတစ်ခုကြောင့် ဆက်နွယ်နေခြင်း သို့မဟုတ် chance ကြောင့် correlation ဖြစ်နိုင်သည်။ သို့သော် strong mathematical correlation သည် variable နှစ်ခု ဆက်နွယ်နေကြောင်း သက်သေပြနိုင်သည်။

Mathematically, random variables နှစ်ခုအကြား ဆက်နွယ်မှုကို **covariance** ဖြင့် ဖော်ပြသည်။ Cov(X,Y) = **E**\[(X-**E**(X))(Y-**E**(Y))\] ဖြစ်သည်။ Variable နှစ်ခု၏ mean value မှ deviation ကို တွက်ချက်ပြီး deviation များ၏ product ကို ရယူသည်။ Variable နှစ်ခုသည် တစ်ပြိုင်နက် deviation ဖြစ်ပါက product သည် အမြဲ positive ဖြစ်ပြီး positive covariance ကို ရရှိမည်။ Variable နှစ်ခုသည် out-of-sync deviation ဖြစ်ပါက product သည် negative ဖြစ်ပြီး negative covariance ကို ရရှိမည်။ Deviations များသည် မဆက်နွယ်ပါက covariance သည် 0 အနီးနားတွင် ရှိမည်။

Covariance ၏ absolute value သည် correlation ၏ အရွယ်အစားကို မပြသနိုင်ပါ။ ထို့ကြောင့် covariance ကို variable နှစ်ခု၏ standard deviation ဖြင့် ခွဲခြား၍ **correlation** ကို ရယူနိုင်သည်။ Correlation သည် [-1,1] အတွင်းရှိပြီး 1 သည် strong positive correlation ကို ပြသသည်။ -1 သည် strong negative correlation ကို ပြသသည်။ 0 သည် correlation မရှိကြောင်း (variables မဆက်နွယ်ကြောင်း) ပြသသည်။

**ဥပမာ**: Baseball players dataset မှ weight နှင့် height အကြား correlation ကို တွက်ချက်ပါ:
```python
print(np.corrcoef(weights,heights))
```
ရလဒ်အနေဖြင့် **correlation matrix** ကို ရရှိပါမည်:
```
array([[1.        , 0.52959196],
       [0.52959196, 1.        ]])
```

> Correlation matrix C ကို input sequences S<sub>1</sub>, ..., S<sub>n</sub> အရ တွက်ချက်နိုင်သည်။ C<sub>ij</sub> သည် S<sub>i</sub> နှင့် S<sub>j</sub> အကြား correlation ဖြစ်ပြီး diagonal elements သည် အမြဲ 1 ဖြစ်သည် (self-correlation of S<sub>i</sub>).

ဤအခါ value 0.53 သည် weight နှင့် height အကြား correlation ရှိကြောင်း ပြသသည်။ Scatter plot ကို ပြုလုပ်၍ relationship ကို visually ကြည့်နိုင်ပါ:

![Relationship between weight and height](../../../../1-Introduction/04-stats-and-probability/images/weight-height-relationship.png)

> Correlation နှင့် Covariance အကြောင်း အခြားဥပမာများကို [accompanying notebook](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb) တွင် ရှာဖွေကြည့်နိုင်ပါသည်။

## Conclusion

ဤအခန်းတွင် ကျွန်ုပ်တို့ သင်ယူခဲ့သည်မှာ:

* data ၏ basic statistical properties များ (mean, variance, mode, quartiles)
* random variables ၏ distributions များ (normal distribution အပါအဝင်)
* property များအကြား correlation ရှာဖွေခြင်း
* math နှင့် statistics apparatus ကို hypothesis များကို သက်သေပြရန် အသုံးပြုခြင်း
* data sample ကို အသုံးပြု၍ random variable အတွက် confidence interval တွက်ချက်ခြင်း

Probability နှင့် Statistics ၏ အကြောင်းအရာများကို အစပြုရန် ဤအခန်းသည် လုံလောက်သည်။

## 🚀 Challenge

Notebook ၏ sample code ကို အသုံးပြု၍ အောက်ပါ hypothesis များကို စမ်းသပ်ပါ:
1. First basemen are older than second basemen
2. First basemen are taller than third basemen
3. Shortstops are taller than second basemen

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/)

## Review & Self Study

Probability နှင့် Statistics သည် အလွန်ကျယ်ပြန့်သော အကြောင်းအရာဖြစ်ပြီး သီးသန့်သင်တန်းတစ်ခု ရှိရန် လိုအပ်သည်။ Theory ကို နက်နက်ရှိုင်းရှိုင်း သင်ယူလိုပါက အောက်ပါစာအုပ်များကို ဆက်လက်ဖတ်ရှုနိုင်ပါသည်:

1. [Carlos Fernandez-Granda](https://cims.nyu.edu/~cfgranda/) (New York University) ၏ [Probability and Statistics for Data Science](https://cims.nyu.edu/~cfgranda/pages/stuff/probability_stats_for_DS.pdf) lecture notes
1. [Peter and Andrew Bruce. Practical Statistics for Data Scientists.](https://www.oreilly.com/library/view/practical-statistics-for/9781491952955/) [[sample code in R](https://github.com/andrewgbruce/statistics-for-data-scientists)]. 
1. [James D. Miller. Statistics for Data Science](https://www.packtpub.com/product/statistics-for-data-science/9781788290678) [[sample code in R](https://github.com/PacktPublishing/Statistics-for-Data-Science)]

## Assignment

[Small Diabetes Study](assignment.md)

## Credits

ဤသင်ခန်းစာကို [Dmitry Soshnikov](http://soshnikov.com) မှ ♥️ ဖြင့် ရေးသားထားသည်။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါရှိနိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွဲအချော်အချော်များအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။