<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0f67a4139454816631526779a456b734",
  "translation_date": "2025-09-06T18:47:57+00:00",
  "source_file": "6-Data-Science-In-Wild/20-Real-World-Examples/README.md",
  "language_code": "my"
}
-->
# အမှန်တကယ်ကမ္ဘာကြီးထဲက ဒေတာသိပ္ပံ

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-RealWorld.png) |
| :--------------------------------------------------------------------------------------------------------------: |
|               အမှန်တကယ်ကမ္ဘာကြီးထဲက ဒေတာသိပ္ပံ - _Sketchnote by [@nitya](https://twitter.com/nitya)_               |

ကျွန်တော်တို့ သင်ယူမှုခရီးလမ်းရဲ့ နောက်ဆုံးအပိုင်းကို ရောက်လာပြီ!

ကျွန်တော်တို့ ဒေတာသိပ္ပံနဲ့ ကျင့်ဝတ်များအကြောင်း အဓိပ္ပါယ်ဖွင့်ဆိုမှုများနဲ့ စတင်ခဲ့ပြီး ဒေတာခွဲခြမ်းစိတ်ဖြာခြင်းနဲ့ အမြင်အာရုံဖော်ပြခြင်းအတွက် အမျိုးမျိုးသော ကိရိယာများနဲ့ နည်းလမ်းများကို လေ့လာခဲ့ပါတယ်။ ဒေတာသိပ္ပံ၏ အသက်တာလှိုင်းကို ပြန်လည်သုံးသပ်ပြီး cloud computing services ကို အသုံးပြု၍ ဒေတာသိပ္ပံ workflow များကို အတိုင်းအတာချဲ့ထွင်ခြင်းနှင့် အလိုအလျောက်လုပ်ဆောင်ခြင်းကို လေ့လာခဲ့ပါတယ်။ ဒါကြောင့် သင်မေးနိုင်ပါတယ် - _"ဒီသင်ယူမှုအားလုံးကို အမှန်တကယ်ကမ္ဘာကြီးထဲမှာ ဘယ်လိုသုံးနိုင်မလဲ?"_

ဒီသင်ခန်းစာမှာ ကျွန်တော်တို့ စက်မှုလုပ်ငန်းများအတွင်း ဒေတာသိပ္ပံ၏ အမှန်တကယ်အသုံးချမှုများကို လေ့လာပြီး သုတေသန၊ ဒစ်ဂျစ်တယ် လူ့ကျမ်းစာများ၊ နှင့် တည်တံ့မှုဆိုင်ရာ အထူးနမူနာများကို ဆွေးနွေးပါမယ်။ ကျောင်းသား project အခွင့်အလမ်းများကို လေ့လာပြီး သင့်ရဲ့ သင်ယူမှုခရီးလမ်းကို ဆက်လက်တိုးတက်စေဖို့ အသုံးဝင်သော အရင်းအမြစ်များနဲ့ အဆုံးသတ်ပါမယ်။

## သင်ခန်းစာမတိုင်မီမေးခွန်း

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/38)

## ဒေတာသိပ္ပံ + စက်မှုလုပ်ငန်း

AI ကို လူတိုင်းအသုံးပြုနိုင်အောင် လွယ်ကူလာတာကြောင့် developer များအတွက် AI အခြေပြု ဆုံးဖြတ်ချက်များနှင့် ဒေတာအခြေပြု အမြင်များကို user experience နှင့် development workflow များထဲသို့ ပေါင်းစပ်ထည့်သွင်းဖန်တီးရန် ပိုမိုလွယ်ကူလာပါတယ်။ ဒေတာသိပ္ပံကို စက်မှုလုပ်ငန်းအတွင်း "အသုံးချ" နေတဲ့ နမူနာအချို့ကို အောက်မှာ ဖော်ပြထားပါတယ်-

 * [Google Flu Trends](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) က search term များကို flu trends နဲ့ ဆက်စပ်ဖို့ ဒေတာသိပ္ပံကို အသုံးပြုခဲ့ပါတယ်။ နည်းလမ်းမှာ အားနည်းချက်များရှိခဲ့ပေမယ့် ဒေတာအခြေပြု ကျန်းမာရေးခန့်မှန်းမှုများ၏ အခွင့်အလမ်းများ (နှင့် စိန်ခေါ်မှုများ) အပေါ် သတိပေးမှုကို တိုးမြှင့်ပေးခဲ့ပါတယ်။

 * [UPS Routing Predictions](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - UPS က ဒေတာသိပ္ပံနှင့် machine learning ကို အသုံးပြု၍ ရေရှည်ပို့ဆောင်မှုအတွက် ရွေးချယ်မှုအကောင်းဆုံးလမ်းကြောင်းများကို ခန့်မှန်းခဲ့ပါတယ်။ ဒါတွင် ရာသီဥတုအခြေအနေများ၊ လမ်းပိတ်ဆို့မှု pattern များ၊ ပို့ဆောင်မှုအချိန်ကန့်သတ်ချက်များ စသည်တို့ကို ထည့်သွင်းစဉ်းစားခဲ့ပါတယ်။

 * [NYC Taxicab Route Visualization](http://chriswhong.github.io/nyctaxi/) - [Freedom Of Information Laws](https://chriswhong.com/open-data/foil_nyc_taxi/) ကို အသုံးပြု၍ ရရှိသော ဒေတာများက NYC taxi များ၏ နေ့စဉ်လှုပ်ရှားမှုကို visualization ပြုလုပ်ပေးခဲ့ပြီး မြို့ကြီးအတွင်းမှာ ဘယ်လို navigation လုပ်သလဲ၊ ဘယ်လောက်ငွေရှာရသလဲ၊ နှင့် ၂၄ နာရီအတွင်း ခရီးစဉ်များ၏ အချိန်ကာလကို နားလည်စေခဲ့ပါတယ်။

 * [Uber Data Science Workbench](https://eng.uber.com/dsw/) - Uber က နေ့စဉ် သန်းပေါင်းများစွာသော ခရီးစဉ်များမှ ရရှိသော pickup & dropoff location, ခရီးစဉ်အချိန်ကာလ၊ နှစ်သက်သောလမ်းကြောင်းများ စသည်တို့ကို အသုံးပြု၍ ဒေတာအာနိသင် tool တစ်ခုကို ဖန်တီးခဲ့ပြီး ဈေးနှုန်းချမှတ်ခြင်း၊ လုံခြုံရေး၊ လိမ်လည်မှုရှာဖွေခြင်း၊ နှင့် navigation ဆုံးဖြတ်ချက်များအတွက် အထောက်အကူပြုခဲ့ပါတယ်။

 * [Sports Analytics](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - _predictive analytics_ (အသင်းနှင့် ကစားသမားခန့်မှန်းခြင်း - [Moneyball](https://datasciencedegree.wisconsin.edu/blog/moneyball-proves-importance-big-data-big-ideas/) ကို စဉ်းစားပါ - နှင့် ပရိသတ်စီမံခန့်ခွဲမှု) နှင့် _data visualization_ (အသင်းနှင့် ပရိသတ် dashboard များ၊ ကစားပွဲများ စသည်တို့) ကို အဓိကထားပြီး talent scouting, sports gambling, inventory/venue management စသည်တို့တွင် အသုံးချနိုင်ပါတယ်။

 * [Data Science in Banking](https://data-flair.training/blogs/data-science-in-banking/) - ဘဏ္ဍာရေးလုပ်ငန်းတွင် ဒေတာသိပ္ပံ၏ တန်ဖိုးကို ဖော်ပြပြီး risk modeling, fraud detection, customer segmentation, real-time prediction, recommender systems စသည်တို့မှ applications များကို ဖော်ပြထားပါတယ်။ Predictive analytics က [credit scores](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit) ကဲ့သို့သော အရေးကြီးသော အတိုင်းအတာများကိုလည်း drive လုပ်ပေးပါတယ်။

 * [Data Science in Healthcare](https://data-flair.training/blogs/data-science-in-healthcare/) - medical imaging (ဥပမာ MRI, X-Ray, CT-Scan), genomics (DNA sequencing), drug development (risk assessment, success prediction), predictive analytics (patient care & supply logistics), disease tracking & prevention စသည်တို့ကဲ့သို့သော applications များကို ဖော်ပြထားပါတယ်။

![Data Science Applications in The Real World](../../../../translated_images/my/data-science-applications.4e5019cd8790ebac2277ff5f08af386f8727cac5d30f77727c7090677e6adb9c.png) Image Credit: [Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

ဤပုံသည် ဒေတာသိပ္ပံနည်းလမ်းများကို အသုံးချနိုင်သော အခြား domains နှင့် နမူနာများကို ဖော်ပြထားသည်။ အခြား applications များကို လေ့လာလိုပါသလား? [Review & Self Study](../../../../6-Data-Science-In-Wild/20-Real-World-Examples) အပိုင်းကို ကြည့်ပါ။

## ဒေတာသိပ္ပံ + သုတေသန

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Research.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              ဒေတာသိပ္ပံနှင့် သုတေသန - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

အမှန်တကယ်အသုံးချမှုများသည် အများအားဖြင့် စက်မှုလုပ်ငန်းအတွင်း အတိုင်းအတာချဲ့ထွင်မှုများကို အဓိကထားသော်လည်း _သုတေသန_ applications နှင့် project များသည် အောက်ပါနှစ်ခုအမြင်မှ အသုံးဝင်နိုင်သည်-

* _innovation opportunities_ - အဆင့်မြင့် concepts များကို prototype လုပ်ခြင်းနှင့် နောက်မျိုးဆက် applications များအတွက် user experience များကို စမ်းသပ်ခြင်း။
* _deployment challenges_ - အမှန်တကယ်ကမ္ဘာကြီးထဲတွင် ဒေတာသိပ္ပံနည်းပညာများ၏ အန္တရာယ်များ သို့မဟုတ် မျှော်လင့်မထားသော အကျိုးဆက်များကို စုံစမ်းလေ့လာခြင်း။

ကျောင်းသားများအတွက် သုတေသန project များသည် သင်ယူမှုနှင့် ပူးပေါင်းဆောင်ရွက်မှုအခွင့်အလမ်းများကို ပေးစွမ်းနိုင်ပြီး သင့်ရဲ့ ချက်ချင်းနားလည်မှုကို တိုးတက်စေပြီး သက်ဆိုင်ရာလူများ သို့မဟုတ် အဖွဲ့များနှင့် ပိုမိုနီးကပ်စေပါမယ်။ ဒါဆို သုတေသန project များက ဘယ်လိုပုံစံရှိပြီး ဘယ်လို အကျိုးသက်ရောက်မှုရှိနိုင်မလဲ?

နမူနာတစ်ခုကို ကြည့်ကြမယ် - Joy Buolamwini (MIT Media Labs) ရဲ့ [MIT Gender Shades Study](http://gendershades.org/overview.html) နှင့် Timnit Gebru (Microsoft Research) တို့ကရေးသားခဲ့သော [signature research paper](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf) ကို အခြေခံထားသည်။

 * **ဘာလဲ:** သုတေသန project ရဲ့ ရည်ရွယ်ချက်မှာ _gender နှင့် skin type အပေါ် automated facial analysis algorithm များနှင့် dataset များတွင် bias ရှိမှုကို အကဲဖြတ်ရန်_ ဖြစ်သည်။
 * **ဘာကြောင့်:** Facial analysis ကို ရဲတပ်ဖွဲ့၊ လေဆိပ်လုံခြုံရေး၊ အလုပ်ခန့်ထားမှုစနစ်များ စသည်တို့တွင် အသုံးပြုသည် - အမှားအယွင်းများ (ဥပမာ bias ကြောင့်) သည် သက်ဆိုင်သော လူများ သို့မဟုတ် အုပ်စုများအပေါ် စီးပွားရေးနှင့် လူမှုရေးအကျိုးသက်ရောက်မှုများ ဖြစ်စေနိုင်သည်။ Bias များကို နားလည်ခြင်း (နှင့် ဖယ်ရှားခြင်း သို့မဟုတ် လျှော့ချခြင်း) သည် အသုံးပြုမှုတွင် တရားမျှတမှုအတွက် အရေးကြီးသည်။
 * **ဘယ်လို:** သုတေသနသူများသည် ရှိပြီးသား benchmark များသည် အဓိကအားဖြင့် အရောင်နုသော subject များကို အသုံးပြုသည်ကို သတိပြုခဲ့ပြီး gender နှင့် skin type အပေါ် _ပိုမိုထိန်းညှိထားသော_ dataset (1000+ images) ကို curate လုပ်ခဲ့သည်။ dataset ကို Microsoft, IBM, Face++ တို့၏ gender classification product သုံးခု၏ တိကျမှုကို အကဲဖြတ်ရန် အသုံးပြုခဲ့သည်။

ရလဒ်များအရ classification accuracy သည် စုစုပေါင်းအားဖြင့် ကောင်းမွန်သော်လည်း အုပ်စုခွဲခြားမှုများအကြား error rate တွင် အထင်အရှားကွာခြားမှုရှိသည်ကို ပြသခဲ့သည် - **misgendering** သည် အမျိုးသမီးများ သို့မဟုတ် အရောင်နက်သော skin type များတွင် ပိုမိုမြင့်မားသည်ကို ပြသခဲ့ပြီး bias ရှိမှုကို ဖော်ပြခဲ့သည်။

**အဓိကရလဒ်များ:** ဒေတာသိပ္ပံသည် _အထောက်အထားပြည့်စုံသော dataset များ_ (subgroup များကို ထိန်းညှိထားသော) နှင့် _ပါဝင်မှုများစွာသော အဖွဲ့များ_ (နောက်ခံအမျိုးမျိုး) ကို ပိုမိုလိုအပ်သည်ကို သတိပေးခဲ့ပြီး AI solution များတွင် bias များကို စောစောဖယ်ရှားရန် သို့မဟုတ် လျှော့ချရန် အရေးကြီးသည်ကို ပြသခဲ့သည်။ ဒီလိုသုတေသနများသည် _တရားမျှတသော AI_ ကို တိုးတက်စေပြီး AI product နှင့် process များတွင် တရားမျှတမှုကို တိုးတက်စေဖို့ အဖွဲ့အစည်းများအတွက် principle နှင့် practice များကို သတ်မှတ်ရန် အရေးကြီးသည်။

**Microsoft ရဲ့ သက်ဆိုင်သော သုတေသနများကို လေ့လာလိုပါသလား?**

* Artificial Intelligence အပေါ် [Microsoft Research Projects](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project) ကို ကြည့်ပါ။
* [Microsoft Research Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/) မှ ကျောင်းသား project များကို လေ့လာပါ။
* [Fairlearn](https://fairlearn.org/) project နှင့် [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) အစီအစဉ်များကို ကြည့်ပါ။

## ဒေတာသိပ္ပံ + လူ့ကျမ်းစာ

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              ဒေတာသိပ္ပံနှင့် ဒစ်ဂျစ်တယ် လူ့ကျမ်းစာ - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

ဒစ်ဂျစ်တယ် လူ့ကျမ်းစာ [ကို အဓိပ္ပါယ်ဖွင့်ဆိုထားသည်](https://digitalhumanities.stanford.edu/about-dh-stanford) - "computational methods နှင့် humanistic inquiry ကို ပေါင်းစပ်ထားသော လုပ်ဆောင်မှုများနှင့် နည်းလမ်းများစုစည်းမှု" ဟု။ [Stanford projects](https://digitalhumanities.stanford.edu/projects) ကဲ့သို့သော _"rebooting history"_ နှင့် _"poetic thinking"_ သည် [Digital Humanities နှင့် Data Science](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science) အကြား ဆက်နွယ်မှုကို ဖော်ပြထားပြီး network analysis, information visualization, spatial နှင့် text analysis ကဲ့သို့သော နည်းလမ်းများကို အဓိကထားသည်။ ဒါက ကျမ်းစာနှင့် စာပေဒေတာများကို ပြန်လည်သုံးသပ်ပြီး အမြင်အသစ်များနှင့် အနက်အဓိပ္ပါယ်များကို ရယူရန် အထောက်အကူပြုသည်။

*ဒီနယ်ပယ်မှာ project တစ်ခုကို လေ့လာပြီး တိုးတက်စေလိုပါသလား?*

["Emily Dickinson and the Meter of Mood"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671) ကို ကြည့်ပါ - [Jen Looper](https://twitter.com/jenlooper) မှ ဖန်တီးထားသော project တစ်ခုဖြစ်ပြီး ဒေတာသိပ္ပံကို အသုံးပြု၍ ကဗျာများကို ပြန်လည်သုံးသပ်ပြီး အရေးအသား၏ အနက်အဓိပ္ပါယ်နှင့် စာရေးသူ၏ အထောက်အပံ့ကို အသစ်သောအမြင်များဖြင့် ပြန်လည်သုံးသပ်ရန် မေးခွန်းထုတ်ထားသည်။ ဥပမာ - _ကဗျာ၏ tone သို့မဟုတ် sentiment ကို ခွဲခြားခြင်းဖြင့် ကဗျာရေးသားခဲ့သော ရာသီဥတုကို ခန့်မှန်းနိုင်မလား_ - ဒါက စာရေးသူ၏ အချိန်ကာလအတွင်း စိတ်နေစိတ်ထားအပေါ် ဘာကို ပြောပြနိုင်မလဲ?

ဒီမေးခွန်းကို ဖြေရှင်းဖို့ ဒေတာသိပ္ပံ၏ အသက်တာလှိုင်းကို လိုက်နာရမယ်-

 * [`Data Acquisition`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#acquiring-the-dataset) - analysis အတွက် သက်ဆိုင်သော dataset ကို စုဆောင်းရန်။ API (ဥပမာ [Poetry DB API](https://poetrydb.org/index.html)) သို့မဟုတ် web page များကို scraping
**Planetary Computer Project သည် (စက်တင်ဘာ 2021 အခြေအနေဖြင့်) စမ်းသပ်မှုအဆင့်တွင်ရှိနေပါသည်** - ဒေတာသိပ္ပံကို အသုံးပြု၍ တာရှည်ခံဖြေရှင်းနည်းများကို အထောက်အကူပြုရန် စတင်ပါ။

* [Request access](https://planetarycomputer.microsoft.com/account/request) ကို အသုံးပြု၍ စတင်လေ့လာပြီး မိတ်ဆွေများနှင့် ချိတ်ဆက်ပါ။
* [Explore documentation](https://planetarycomputer.microsoft.com/docs/overview/about) ကို လေ့လာပြီး ပံ့ပိုးထားသော ဒေတာများနှင့် API များကို နားလည်ပါ။
* [Ecosystem Monitoring](https://analytics-lab.org/ecosystemmonitoring/) ကဲ့သို့သော အက်ပလီကေးရှင်းများကို လေ့လာပြီး အက်ပလီကေးရှင်းအကြံဉာဏ်များအတွက် အားရစရာ ရှာဖွေပါ။

ဒေတာကို အသုံးပြု၍ ရှာဖွေတွေ့ရှိမှုများကို ရှင်းလင်းစွာ ဖော်ပြရန် သို့မဟုတ် ရှာဖွေတွေ့ရှိမှုများကို တိုးမြှင့်ရန် အကောင်းဆုံးနည်းလမ်းများကို စဉ်းစားပါ။ ဥပမာအားဖြင့် ရာသီဥတုပြောင်းလဲမှုနှင့် သစ်တောများဖျက်ဆီးမှုကဲ့သို့သော နယ်ပယ်များတွင် အသုံးပြုနိုင်သော ရှာဖွေတွေ့ရှိမှုများကို စဉ်းစားပါ။ ဒါမှမဟုတ် တာရှည်ခံနေထိုင်မှုအတွက် အပြုသဘောဆောင်သော အပြုအမူပြောင်းလဲမှုများကို လှုံ့ဆော်နိုင်သော အသုံးပြုသူအတွေ့အကြုံအသစ်များ ဖန်တီးရန် ရှာဖွေတွေ့ရှိမှုများကို အသုံးပြုနိုင်သည့် နည်းလမ်းများကို စဉ်းစားပါ။

## ဒေတာသိပ္ပံ + ကျောင်းသားများ

စက်မှုလုပ်ငန်းနှင့် သုတေသနတွင် အမှန်တကယ်အသုံးချနိုင်သော အက်ပလီကေးရှင်းများကို ပြောခဲ့ပြီး၊ ဒစ်ဂျစ်တယ် လူ့ဘာသာရပ်များနှင့် တာရှည်ခံမှုတွင် ဒေတာသိပ္ပံအက်ပလီကေးရှင်း ဥပမာများကို လေ့လာခဲ့ပါသည်။ ဒါဆိုရင် ဒေတာသိပ္ပံအစတန်းကျောင်းသားများအနေဖြင့် သင်၏ ကျွမ်းကျင်မှုများကို တိုးတက်စေရန်နှင့် သင်၏ အတတ်ပညာများကို မျှဝေရန် ဘယ်လိုလုပ်နိုင်မလဲ?

ဒီမှာ ကျောင်းသားများအတွက် ဒေတာသိပ္ပံပရောဂျက်များ၏ ဥပမာများကို ဖော်ပြထားပြီး သင့်အား အားရစရာပေးနိုင်ပါသည်။

* [MSR Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/#!projects) နှင့် GitHub [projects](https://github.com/msr-ds3) တွင် အောက်ပါအကြောင်းအရာများကို လေ့လာပါ။
    - [Racial Bias in Police Use of Force](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2019-replicating-an-empirical-analysis-of-racial-differences-in-police-use-of-force/) | [Github](https://github.com/msr-ds3/stop-question-frisk)
    - [Reliability of NYC Subway System](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2018-exploring-the-reliability-of-the-nyc-subway-system/) | [Github](https://github.com/msr-ds3/nyctransit)
* [Digitizing Material Culture: Exploring socio-economic distributions in Sirkap](https://claremont.maps.arcgis.com/apps/Cascade/index.html?appid=bdf2aef0f45a4674ba41cd373fa23afc) - [Ornella Altunyan](https://twitter.com/ornelladotcom) နှင့် Claremont မှ အဖွဲ့၏ [ArcGIS StoryMaps](https://storymaps.arcgis.com/) ကို အသုံးပြု၍ ဖန်တီးထားသည်။

## 🚀 စိန်ခေါ်မှု

ဒေတာသိပ္ပံအစတန်းကျောင်းသားများအတွက် အဆင်ပြေသော ပရောဂျက်များကို အကြံပြုထားသော ဆောင်းပါးများကို ရှာဖွေပါ - ဥပမာအားဖြင့် [ဒီ 50 ခေါင်းစဉ်](https://www.upgrad.com/blog/data-science-project-ideas-topics-beginners/) သို့မဟုတ် [ဒီ 21 ပရောဂျက်အကြံများ](https://www.intellspot.com/data-science-project-ideas) သို့မဟုတ် [ဒီ 16 ပရောဂျက်များနှင့် အရင်းအမြစ်ကုဒ်](https://data-flair.training/blogs/data-science-project-ideas/) ကို လေ့လာပြီး ပြန်လည်ဖန်တီးပါ။ သင်၏ သင်ယူမှုခရီးစဉ်များကို ဘလော့ဂ်ရေးပြီး သင့်ရှာဖွေတွေ့ရှိမှုများကို ကျွန်ုပ်တို့အား မျှဝေပါ။

## Post-Lecture Quiz

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/39)

## ပြန်လည်သုံးသပ်ခြင်းနှင့် ကိုယ်တိုင်လေ့လာခြင်း

အသုံးချနိုင်သော နေရာများကို ပိုမိုလေ့လာလိုပါသလား? အောက်ပါ ဆောင်းပါးများကို ကြည့်ပါ။
* [17 Data Science Applications and Examples](https://builtin.com/data-science/data-science-applications-examples) - ဇူလိုင် 2021
* [11 Breathtaking Data Science Applications in Real World](https://myblindbird.com/data-science-applications-real-world/) - မေ 2021
* [Data Science In The Real World](https://towardsdatascience.com/data-science-in-the-real-world/home) - ဆောင်းပါးစုစည်းမှု
* [12 Real-World Data Science Applications with Examples](https://www.scaler.com/blog/data-science-applications/) - မေ 2024
* ဒေတာသိပ္ပံတွင်: [ပညာရေး](https://data-flair.training/blogs/data-science-in-education/), [လယ်ယာစိုက်ပျိုးရေး](https://data-flair.training/blogs/data-science-in-agriculture/), [ဘဏ္ဍာရေး](https://data-flair.training/blogs/data-science-in-finance/), [ရုပ်ရှင်](https://data-flair.training/blogs/data-science-at-movies/), [ကျန်းမာရေးစောင့်ရှောက်မှု](https://onlinedegrees.sandiego.edu/data-science-health-care/) နှင့် အခြားများ။

## အလုပ်ပေးစာ

[Explore A Planetary Computer Dataset](assignment.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေပါသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို ကျေးဇူးပြု၍ သိရှိထားပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။