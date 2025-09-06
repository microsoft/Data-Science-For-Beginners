<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "06bac7959b46b6e8aedcae014278c476",
  "translation_date": "2025-09-05T20:27:43+00:00",
  "source_file": "6-Data-Science-In-Wild/20-Real-World-Examples/README.md",
  "language_code": "my"
}
-->
# အမှန်တကယ်ကမ္ဘာတွင် ဒေတာသိပ္ပံ

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-RealWorld.png) |
| :--------------------------------------------------------------------------------------------------------------: |
|               အမှန်တကယ်ကမ္ဘာတွင် ဒေတာသိပ္ပံ - _Sketchnote by [@nitya](https://twitter.com/nitya)_               |

ကျွန်ုပ်တို့၏သင်ယူခရီးစဉ်၏အဆုံးသို့ရောက်လာပြီ!

ကျွန်ုပ်တို့သည် ဒေတာသိပ္ပံနှင့် အကျင့်သိက္ခာ၏ အဓိပ္ပါယ်များနှင့် စတင်ခဲ့ပြီး၊ ဒေတာခွဲခြမ်းစိတ်ဖြာခြင်းနှင့် အမြင်အာရုံဖော်ပြခြင်းအတွက် အမျိုးမျိုးသောကိရိယာများနှင့်နည်းလမ်းများကိုလေ့လာခဲ့ပြီး၊ ဒေတာသိပ္ပံ၏ အသက်တာစဉ်ကို ပြန်လည်သုံးသပ်ခဲ့ပြီး၊ cloud computing services များဖြင့် ဒေတာသိပ္ပံ workflow များကို အတိုင်းအတာချဲ့ထွင်ခြင်းနှင့် အလိုအလျောက်လုပ်ဆောင်ခြင်းကိုလေ့လာခဲ့သည်။ ထို့ကြောင့် သင်မေးမိနိုင်သည် - _"ဒီသင်ယူမှုအားလုံးကို အမှန်တကယ်ကမ္ဘာ့အခြေအနေများနှင့် ဘယ်လိုချိတ်ဆက်ရမလဲ?"_

ဒီသင်ခန်းစာမှာ၊ ကျွန်ုပ်တို့သည် စက်မှုလုပ်ငန်းများတွင် ဒေတာသိပ္ပံ၏ အမှန်တကယ်အသုံးချမှုများကိုလေ့လာပြီး၊ သုတေသန၊ ဒစ်ဂျစ်တယ် လူ့ကျမ်းစာများနှင့် တာရှည်ခံမှုဆိုင်ရာ အခြေအနေများတွင် အထူးနမူနာများကို ဆွေးနွေးပါမည်။ ကျောင်းသား project အခွင့်အလမ်းများကိုလေ့လာပြီး၊ သင်၏သင်ယူခရီးစဉ်ကို ဆက်လက်တိုးတက်စေရန် အသုံးဝင်သော အရင်းအမြစ်များနှင့်အတူ အဆုံးသတ်ပါမည်။

## သင်ခန်းစာမတိုင်မီမေးခွန်း

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/38)

## ဒေတာသိပ္ပံ + စက်မှုလုပ်ငန်း

AI ကို လူတိုင်းအသုံးပြုနိုင်စေရန် အခွင့်အရေးများပေးထားသောကြောင့်၊ developer များသည် ယခုအခါ AI အခြေပြုဆုံးဖြတ်မှုများနှင့် ဒေတာအခြေပြု အမြင်အာရုံများကို user experience များနှင့် development workflow များတွင် ပိုမိုလွယ်ကူစွာ ဒီဇိုင်းဆွဲခြင်းနှင့် ပေါင်းစပ်နိုင်ကြသည်။ ဒေတာသိပ္ပံကို စက်မှုလုပ်ငန်းများတွင် "အသုံးချ" နေသည့် နမူနာအချို့ကို အောက်တွင်ဖော်ပြထားသည် -

 * [Google Flu Trends](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) သည် search term များကို flu trends နှင့် ဆက်စပ်ရန် ဒေတာသိပ္ပံကို အသုံးပြုခဲ့သည်။ နည်းလမ်းတွင် အားနည်းချက်များရှိသော်လည်း၊ ဒေတာအခြေပြု ကျန်းမာရေးခန့်မှန်းမှုများ၏ အခွင့်အလမ်းများ (နှင့် စိန်ခေါ်မှုများ) အပေါ် သတိပေးခဲ့သည်။

 * [UPS Routing Predictions](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - UPS သည် ဒေတာသိပ္ပံနှင့် machine learning ကို အသုံးပြု၍ ရာသီဥတုအခြေအနေများ၊ လမ်းပိတ်ဆို့မှုများ၊ ပို့ဆောင်ရမည့်အချိန်များနှင့် အခြားအချက်အလက်များကို ထည့်သွင်းပြီး ပို့ဆောင်မှုအတွက် အကောင်းဆုံးလမ်းကြောင်းများကို ခန့်မှန်းသည်။

 * [NYC Taxicab Route Visualization](http://chriswhong.github.io/nyctaxi/) - [Freedom Of Information Laws](https://chriswhong.com/open-data/foil_nyc_taxi/) ကို အသုံးပြု၍ ရရှိသော ဒေတာများကို အသုံးပြု၍ NYC taxi များ၏ နေ့စဉ်လှုပ်ရှားမှုများကို visualization ပြုလုပ်ခဲ့သည်။ ဒါဟာ မြို့ကြီးမှာ ဘယ်လို navigation လုပ်သလဲ၊ ဘယ်လောက်ငွေရှာသလဲ၊ ၂၄ နာရီအတွင်း ခရီးစဉ်များ၏ အချိန်ကာလကို နားလည်စေခဲ့သည်။

 * [Uber Data Science Workbench](https://eng.uber.com/dsw/) - Uber ခရီးစဉ်များ၏ pickup & dropoff location များ၊ ခရီးစဉ်အချိန်ကာလ၊ နှစ်သက်သောလမ်းကြောင်းများစသည့် ဒေတာများကို *နေ့စဉ်* စုဆောင်းပြီး၊ ဈေးနှုန်းချမှတ်ခြင်း၊ လုံခြုံရေး၊ လိမ်လည်မှုရှာဖွေခြင်းနှင့် navigation ဆုံးဖြတ်ချက်များအတွက် data analytics tool တစ်ခုကို တည်ဆောက်သည်။

 * [Sports Analytics](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - _predictive analytics_ (အသင်းနှင့် ကစားသမားခန့်မှန်းခြင်း - [Moneyball](https://datasciencedegree.wisconsin.edu/blog/moneyball-proves-importance-big-data-big-ideas/) ကိုစဉ်းစားပါ - နှင့် ပရိသတ်စီမံခန့်ခွဲမှု) နှင့် _data visualization_ (အသင်းနှင့် ပရိသတ် dashboard များ၊ ကစားပွဲများစသည်) ကို အဓိကထားပြီး၊ တက်လှမ်းမှုရှာဖွေခြင်း၊ အားကစားလောင်းကစားနှင့် inventory/venue စီမံခန့်ခွဲမှုတို့တွင် အသုံးချသည်။

 * [Data Science in Banking](https://data-flair.training/blogs/data-science-in-banking/) - ဘဏ္ဍာရေးလုပ်ငန်းတွင် ဒေတာသိပ္ပံ၏ တန်ဖိုးကို အဓိကထားပြီး၊ အန္တရာယ်မော်ဒယ်ဖော်ခြင်းနှင့် လိမ်လည်မှုရှာဖွေခြင်း၊ customer segmentation၊ အချိန်နှင့်တပြေးညီ ခန့်မှန်းခြင်းနှင့် recommender systems များအထိ အသုံးချသည်။ Predictive analytics သည် [credit scores](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit) ကဲ့သို့သော အရေးကြီးသောအတိုင်းအတာများကိုလည်း အားပေးသည်။

 * [Data Science in Healthcare](https://data-flair.training/blogs/data-science-in-healthcare/) - medical imaging (ဥပမာ MRI, X-Ray, CT-Scan), genomics (DNA sequencing), ဆေးဝါးဖွံ့ဖြိုးမှု (အန္တရာယ်ခန့်မှန်းခြင်း၊ အောင်မြင်မှုခန့်မှန်းခြင်း), predictive analytics (လူနာစောင့်ရှောက်မှုနှင့် ပစ္စည်းထောက်ပံ့မှု logistics), ရောဂါခြေရာခံခြင်းနှင့် ကာကွယ်ခြင်းစသည်တို့ကဲ့သို့သော လျှောက်လွှာများကို အဓိကထားသည်။

![Data Science Applications in The Real World](../../../../6-Data-Science-In-Wild/20-Real-World-Examples/images/data-science-applications.png) Image Credit: [Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

ဤပုံသည် ဒေတာသိပ္ပံနည်းလမ်းများကို အသုံးချနိုင်သော အခြားနယ်ပယ်များနှင့် နမူနာများကို ဖော်ပြထားသည်။ အခြားလျှောက်လွှာများကို လေ့လာလိုပါသလား? [Review & Self Study](../../../../6-Data-Science-In-Wild/20-Real-World-Examples) အပိုင်းကို ကြည့်ပါ။

## ဒေတာသိပ္ပံ + သုတေသန

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Research.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              ဒေတာသိပ္ပံနှင့် သုတေသန - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

အမှန်တကယ်ကမ္ဘာ့လျှောက်လွှာများသည် အများအားဖြင့် စက်မှုလုပ်ငန်းများတွင် အတိုင်းအတာချဲ့ထွင်မှုကို အဓိကထားသော်လည်း၊ _သုတေသန_ လျှောက်လွှာများနှင့် project များသည် အောက်ပါနှစ်မျိုးသော ရှုထောင့်များမှ အသုံးဝင်နိုင်သည် -

* _ဆန်းသစ်မှုအခွင့်အလမ်းများ_ - အဆင့်မြင့်အယူအဆများကို prototype လုပ်ခြင်းနှင့် နောက်မျိုးဆက်လျှောက်လွှာများအတွက် user experience များကို စမ်းသပ်ခြင်း။
* _တပ်ဆင်မှုစိန်ခေါ်မှုများ_ - အမှန်တကယ်ကမ္ဘာ့အခြေအနေများတွင် ဒေတာသိပ္ပံနည်းပညာများ၏ အန္တရာယ်များ သို့မဟုတ် မျှော်လင့်မထားသော အကျိုးဆက်များကို စုံစမ်းခြင်း။

ကျောင်းသားများအတွက်၊ ဤသုတေသန project များသည် သင်ယူမှုနှင့် ပူးပေါင်းဆောင်ရွက်မှုအခွင့်အလမ်းများကို ပေးနိုင်ပြီး၊ သင်၏အကြောင်းအရာကို နားလည်မှုတိုးတက်စေခြင်းနှင့် သက်ဆိုင်ရာလူများ သို့မဟုတ် အဖွဲ့များနှင့် ပိုမိုကျယ်ပြန့်သော ဆက်ဆံရေးနှင့် ပါဝင်မှုကို တိုးတက်စေပါသည်။ ထို့ကြောင့် သုတေသန project များသည် ဘယ်လိုပုံစံရှိပြီး၊ ဘယ်လိုအကျိုးသက်ရောက်မှုရှိနိုင်သလဲ?

နမူနာတစ်ခုကို ကြည့်ပါ - Joy Buolamwini (MIT Media Labs) မှ [MIT Gender Shades Study](http://gendershades.org/overview.html) နှင့် Timnit Gebru (Microsoft Research) တို့၏ [signature research paper](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf) ကို အဓိကထားပါမည်။

 * **ဘာလဲ:** သုတေသန project ၏ ရည်ရွယ်ချက်မှာ _gender နှင့် skin type အပေါ် automated facial analysis algorithm များနှင့် dataset များတွင် bias ရှိမှုကို အကဲဖြတ်ရန်_ ဖြစ်သည်။
 * **ဘာကြောင့်:** Facial analysis ကို ရဲတပ်ဖွဲ့၊ လေဆိပ်လုံခြုံရေး၊ အလုပ်ခန့်ထားမှုစနစ်များနှင့် အခြားသောနေရာများတွင် အသုံးပြုသည် - အမှန်မမှန်သော ခွဲခြားမှုများ (ဥပမာ bias ကြောင့်) သည် ထိခိုက်သောလူများ သို့မဟုတ် အုပ်စုများအတွက် စီးပွားရေးနှင့် လူမှုရေးအန္တရာယ်များ ဖြစ်စေနိုင်သည်။ Bias များကို နားလည်ခြင်း (နှင့် ဖယ်ရှားခြင်း သို့မဟုတ် လျှော့ချခြင်း) သည် အသုံးပြုမှုတွင် တရားမျှတမှုအတွက် အရေးကြီးသည်။
 * **ဘယ်လို:** သုတေသနသူများသည် ရှိပြီးသား benchmark များသည် အများအားဖြင့် အရောင်နုသောအကြောင်းအရာများကို အသုံးပြုထားသည်ကို သတိပြုခဲ့ပြီး၊ gender နှင့် skin type အပေါ်ပိုမိုချိန်ညှိထားသော dataset (1000+ ပုံများ) ကို curate လုပ်ခဲ့သည်။ dataset ကို Microsoft, IBM နှင့် Face++ တို့၏ gender classification product သုံးခု၏ တိကျမှုကို အကဲဖြတ်ရန် အသုံးပြုခဲ့သည်။

ရလဒ်များအရ classification accuracy သည် အထူးသဖြင့်ကောင်းမွန်သော်လည်း၊ အုပ်စုခွဲခြားမှုများအကြား error rate တွင် ထင်ရှားသောကွာခြားမှုရှိသည်ကို ပြသခဲ့သည် - **misgendering** သည် အမျိုးသမီးများ သို့မဟုတ် အရောင်မည်းသော skin type များတွင် ပိုမိုမြင့်မားသည်ကို ပြသခဲ့ပြီး၊ bias ရှိမှုကို ဖော်ပြခဲ့သည်။

**အဓိကရလဒ်များ:** ဒေတာသိပ္ပံသည် ပိုမို _ကိုယ်စားပြုသော dataset များ_ (subgroup များကို balance လုပ်ထားသော) နှင့် ပိုမို _ပါဝင်မှုရှိသောအဖွဲ့များ_ (background များကွဲပြားသော) ကိုလိုအပ်သည်ကို သတိပေးခဲ့ပြီး၊ AI solution များတွင် bias များကို စောစောဖယ်ရှားခြင်း သို့မဟုတ် လျှော့ချခြင်းအတွက် အရေးကြီးသည်ကို ပြသခဲ့သည်။ ဤသုတေသနများသည် _responsible AI_ ကို အဖွဲ့အစည်းများတွင် သတ်မှတ်ရန်နှင့် AI product များနှင့် process များတွင် တရားမျှတမှုကို တိုးတက်စေရန် အရေးကြီးသည်။

**Microsoft တွင် သက်ဆိုင်သော သုတေသနများကို လေ့လာလိုပါသလား?**

* Artificial Intelligence အပေါ် [Microsoft Research Projects](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project) ကိုကြည့်ပါ။
* [Microsoft Research Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/) မှ ကျောင်းသား project များကိုလေ့လာပါ။
* [Fairlearn](https://fairlearn.org/) project နှင့် [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) အစီအစဉ်များကိုကြည့်ပါ။

## ဒေတာသိပ္ပံ + လူ့ကျမ်းစာ

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              ဒေတာသိပ္ပံနှင့် ဒစ်ဂျစ်တယ် လူ့ကျမ်းစာ - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

Digital Humanities [ကိုအဓိပ္ပာယ်ဖော်ပြထားသည်](https://digitalhumanities.stanford.edu/about-dh-stanford) သည် "computational methods များနှင့် humanistic inquiry ကိုပေါင်းစပ်ထားသော လက်တွေ့ကျသောနည်းလမ်းများနှင့် လုပ်ဆောင်မှုများ" ဟုဆိုသည်။ [Stanford projects](https://digitalhumanities.stanford.edu/projects) ကဲ့သို့သော _"rebooting history"_ နှင့် _"poetic thinking"_ သည် [Digital Humanities နှင့် Data Science](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science) တို့အကြားဆက်နွယ်မှုကို ဖော်ပြထားပြီး၊ network analysis, information visualization, spatial analysis နှင့် text analysis ကဲ့သို့သောနည်းလမ်းများကို အဓိကထားသည်။ ဤနည်းလမ်းများသည် သမိုင်းနှင့် စာပေဒေတာ set များကို ပြန်လည်သုံးသပ်ရန်နှင့် အမြင်အသစ်များကို ရယူရန် အထောက်အကူပြုသည်။

*ဤနယ်ပယ်တွင် project တစ်ခုကို လေ့လာလိုပါသလား?*

["Emily Dickinson and the Meter of Mood"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671) ကိုကြည့်ပါ - [Jen Looper](https://twitter.com/jenlooper) မှ အလွန်ကောင်းမွန်သော နမူနာတစ်ခုဖြစ်ပြီး၊ ဒေတာသိပ္ပံကို အသုံးပြု၍ ရင်းနှီးပြီးသားကဗျာများကို ပြန်လည်သုံးသပ်ပြီး၊ ၎င်း၏ အဓိပ္ပါယ်နှင့် ကဗျာရေးသူ၏ အထောက်အပံ့ကို အခြေအနေအသစ်များတွင် ပြန်လည်အကဲဖြတ်ရန် မေးခွန်းထုတ်ထားသည်။ ဥပမာအားဖြင့် - _ကဗျာ၏ tone သို့မဟုတ် sentiment ကိုခန့်မှန်းခြ
**Planetary Computer Project သည် (Sep 2021 အခြေအနေဖြင့်) စမ်းသပ်မှုအဆင့်တွင်ရှိနေပါသည်** - ဒေတာသိပ္ပံကို အသုံးပြု၍ တာဆောင်မှုဖြေရှင်းမှုများကို အထောက်အကူပြုရန် စတင်ပါ။

* [Access တောင်းဆိုရန်](https://planetarycomputer.microsoft.com/account/request) စတင်လေ့လာပြီး အခြားသူများနှင့် ချိတ်ဆက်ပါ။
* [Documentation ကိုလေ့လာရန်](https://planetarycomputer.microsoft.com/docs/overview/about) ပံ့ပိုးထားသော ဒေတာများနှင့် API များကို နားလည်ပါ။
* [Ecosystem Monitoring](https://analytics-lab.org/ecosystemmonitoring/) ကဲ့သို့သော အက်ပလီကေးရှင်းများကို လေ့လာပြီး အကြံဉာဏ်ရယူပါ။

ဒေတာကို အသုံးပြု၍ ရှုထောင့်များကို ဖော်ထုတ်ခြင်း သို့မဟုတ် သက်ဆိုင်ရာ အချက်အလက်များကို ပိုမိုထင်ရှားစေရန် visualization ကို အသုံးပြုနိုင်မည်ကို စဉ်းစားပါ။ ဒါမှမဟုတ် အချက်အလက်များကို အသုံးပြု၍ သက်ဆိုင်ရာ အပြုအမူများကို အားပေးရန် အသစ်သော အသုံးပြုသူ အတွေ့အကြုံများ ဖန်တီးနိုင်မည်ကို စဉ်းစားပါ။

## ဒေတာသိပ္ပံ + ကျောင်းသားများ

စက်မှုလုပ်ငန်းနှင့် သုတေသနတွင် အမှန်တကယ် အသုံးချမှုများကို ပြောခဲ့ပြီး၊ ဒစ်ဂျစ်တယ် လူ့ဘာသာရပ်များနှင့် တာဆောင်မှုဆိုင်ရာ ဒေတာသိပ္ပံ အက်ပလီကေးရှင်း ဥပမာများကို လေ့လာခဲ့ပါသည်။ ဒါဆိုရင် ဒေတာသိပ္ပံ စတင်လေ့လာသူများအနေဖြင့် သင်၏ ကျွမ်းကျင်မှုများကို တိုးတက်စေပြီး အတတ်ပညာများကို မျှဝေမည်ကဲ့သို့လုပ်နိုင်မလဲ?

ဒီမှာ ကျောင်းသားများအတွက် ဒေတာသိပ္ပံ ပရောဂျက်များ၏ ဥပမာများကို ဖော်ပြထားသည်။

* [MSR Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/#!projects) GitHub [projects](https://github.com/msr-ds3) တွင် အောက်ပါအကြောင်းအရာများကို လေ့လာပါ။
    - [Racial Bias in Police Use of Force](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2019-replicating-an-empirical-analysis-of-racial-differences-in-police-use-of-force/) | [Github](https://github.com/msr-ds3/stop-question-frisk)
    - [Reliability of NYC Subway System](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2018-exploring-the-reliability-of-the-nyc-subway-system/) | [Github](https://github.com/msr-ds3/nyctransit)
* [Digitizing Material Culture: Exploring socio-economic distributions in Sirkap](https://claremont.maps.arcgis.com/apps/Cascade/index.html?appid=bdf2aef0f45a4674ba41cd373fa23afc) - [Ornella Altunyan](https://twitter.com/ornelladotcom) နှင့် Claremont မှ အဖွဲ့က [ArcGIS StoryMaps](https://storymaps.arcgis.com/) ကို အသုံးပြု၍ ဖန်တီးထားသည်။

## 🚀 စိန်ခေါ်မှု

ဒေတာသိပ္ပံ စတင်လေ့လာသူများအတွက် သင့်လျော်သော ပရောဂျက်များကို အကြံပြုထားသော ဆောင်းပါးများကို ရှာဖွေပါ - [ဒီ 50 အကြောင်းအရာများ](https://www.upgrad.com/blog/data-science-project-ideas-topics-beginners/) သို့မဟုတ် [ဒီ 21 ပရောဂျက် အကြံဉာဏ်များ](https://www.intellspot.com/data-science-project-ideas) သို့မဟုတ် [ဒီ 16 ပရောဂျက်များနှင့် အရင်းအမြစ်ကုဒ်](https://data-flair.training/blogs/data-science-project-ideas/) ကို ဖွင့်လှစ်ပြီး ပြန်လည်ဖန်တီးပါ။ သင်၏ လေ့လာမှု ခရီးစဉ်များကို ဘလော့ဂ်ရေးပြီး အတွေ့အကြုံများကို မျှဝေဖို့ မမေ့ပါနှင့်။

## Post-Lecture Quiz

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/39)

## ပြန်လည်သုံးသပ်ခြင်းနှင့် ကိုယ်တိုင်လေ့လာခြင်း

အသုံးချမှုများကို ပိုမိုလေ့လာလိုပါသလား? သက်ဆိုင်ရာ ဆောင်းပါးအချို့ကို ဖော်ပြထားသည်။
* [17 Data Science Applications and Examples](https://builtin.com/data-science/data-science-applications-examples) - Jul 2021
* [11 Breathtaking Data Science Applications in Real World](https://myblindbird.com/data-science-applications-real-world/) - May 2021
* [Data Science In The Real World](https://towardsdatascience.com/data-science-in-the-real-world/home) - ဆောင်းပါးစုစည်းမှု
* ဒေတာသိပ္ပံ: [ပညာရေး](https://data-flair.training/blogs/data-science-in-education/), [လယ်ယာ](https://data-flair.training/blogs/data-science-in-agriculture/), [ဘဏ္ဍာရေး](https://data-flair.training/blogs/data-science-in-finance/), [ရုပ်ရှင်](https://data-flair.training/blogs/data-science-at-movies/) နှင့် အခြားများ။

## လုပ်ငန်းတာဝန်

[Explore A Planetary Computer Dataset](assignment.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။