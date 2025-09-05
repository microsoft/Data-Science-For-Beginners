<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f95679140c7cb39c30ccba535cd8f03f",
  "translation_date": "2025-09-05T05:24:46+00:00",
  "source_file": "6-Data-Science-In-Wild/20-Real-World-Examples/README.md",
  "language_code": "my"
}
-->
# အမှန်တကယ်ကမ္ဘာတွင် ဒေတာသိပ္ပံ

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-RealWorld.png) |
| :--------------------------------------------------------------------------------------------------------------: |
|               အမှန်တကယ်ကမ္ဘာတွင် ဒေတာသိပ္ပံ - _Sketchnote by [@nitya](https://twitter.com/nitya)_               |

ကျွန်တော်တို့ သင်ယူမှုခရီးလမ်း၏ နောက်ဆုံးအပိုင်းကို ရောက်လာပြီ!

ကျွန်တော်တို့ ဒေတာသိပ္ပံနှင့် အကျင့်သိက္ခာ၏ အဓိပ္ပါယ်များနှင့် စတင်ခဲ့ပြီး၊ ဒေတာခွဲခြမ်းစိတ်ဖြာခြင်းနှင့် အမြင်အာရုံဖော်ပြခြင်းအတွက် အမျိုးမျိုးသော ကိရိယာများနှင့် နည်းလမ်းများကို လေ့လာခဲ့ပြီး၊ ဒေတာသိပ္ပံ၏ အသက်တာစဉ်ကို ပြန်လည်သုံးသပ်ခဲ့ပြီး၊ cloud computing services များဖြင့် ဒေတာသိပ္ပံ workflow များကို အတိုင်းအတာချဲ့ထွင်ခြင်းနှင့် အလိုအလျောက်လုပ်ဆောင်ခြင်းကို လေ့လာခဲ့ပါတယ်။ ဒါကြောင့် သင်ဟာ _"ဒီသင်ယူမှုအားလုံးကို အမှန်တကယ်ကမ္ဘာ့အခြေအနေများနှင့် ဘယ်လိုချိတ်ဆက်ရမလဲ?"_ ဆိုပြီး စဉ်းစားနေရမယ်။

ဒီသင်ခန်းစာမှာ၊ ကျွန်တော်တို့ ဒေတာသိပ္ပံကို စက်မှုလုပ်ငန်းများတွင် အမှန်တကယ်အသုံးချမှုများကို လေ့လာပြီး၊ သုတေသန၊ ဒစ်ဂျစ်တယ် လူ့ဘောင်နှင့် တာဆောင်မှုဆိုင်ရာ အခြေအနေများတွင် အထူးနမူနာများကို ဆွေးနွေးပါမယ်။ ကျောင်းသား project အခွင့်အလမ်းများကို လေ့လာပြီး သင့်ရဲ့ သင်ယူမှုခရီးလမ်းကို ဆက်လက်တိုးတက်စေဖို့ အသုံးဝင်သော အရင်းအမြစ်များနှင့် အဆုံးသတ်ပါမယ်။

## သင်ခန်းစာမတိုင်မီ စစ်တမ်း

[Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ds/)

## ဒေတာသိပ္ပံ + စက်မှုလုပ်ငန်း

AI ကို လူတိုင်းအသုံးပြုနိုင်စေမှုကြောင့်၊ developer များအတွက် AI အခြေပြု ဆုံးဖြတ်ချက်များနှင့် ဒေတာအခြေပြု အမြင်များကို user experience နှင့် development workflow များတွင် ပေါင်းစပ်ထည့်သွင်းဖန်တီးရန် ပိုမိုလွယ်ကူလာပါတယ်။ ဒေတာသိပ္ပံကို စက်မှုလုပ်ငန်းများတွင် "အမှန်တကယ်အသုံးချမှု" အဖြစ် အသုံးပြုသည့် နမူနာအချို့ကို ကြည့်ပါ။

 * [Google Flu Trends](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) သည် ရောဂါဖြစ်ပွားမှုများနှင့် ရှာဖွေမှုစာလုံးများကို ဆက်စပ်ရန် ဒေတာသိပ္ပံကို အသုံးပြုခဲ့သည်။ နည်းလမ်းတွင် အားနည်းချက်များရှိသော်လည်း၊ ဒေတာအခြေပြု ကျန်းမာရေးခန့်မှန်းမှုများ၏ အခွင့်အလမ်းများ (နှင့် စိန်ခေါ်မှုများ) အပေါ် သတိပေးမှုကို ရရှိစေခဲ့သည်။

 * [UPS Routing Predictions](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - UPS သည် ဒေတာသိပ္ပံနှင့် machine learning ကို အသုံးပြု၍ ရာသီဥတုအခြေအနေများ၊ လမ်းပန်းဆက်သွယ်မှု pattern များ၊ ပို့ဆောင်မှုအချိန်ကန့်သတ်ချက်များကို ထည့်သွင်းပြီး ပို့ဆောင်မှုအတွက် အကောင်းဆုံးလမ်းကြောင်းများကို ခန့်မှန်းသည်။

 * [NYC Taxicab Route Visualization](http://chriswhong.github.io/nyctaxi/) - [Freedom Of Information Laws](https://chriswhong.com/open-data/foil_nyc_taxi/) ကို အသုံးပြု၍ ရရှိသော ဒေတာများကို အသုံးပြု၍ NYC taxi များ၏ နေ့စဉ်လှုပ်ရှားမှုများကို visualization ပြုလုပ်သည်။ ဒါဟာ မြို့ကြီးကို ဘယ်လို navigate လုပ်သလဲ၊ ဘယ်လောက်ငွေရှာရသလဲ၊ ၂၄ နာရီအတွင်း ခရီးစဉ်များ၏ ကြာမြင့်ချိန်ကို နားလည်စေသည်။

 * [Uber Data Science Workbench](https://eng.uber.com/dsw/) - Uber ခရီးစဉ်များမှ ရရှိသော pickup & dropoff location, ခရီးစဉ်ကြာမြင့်ချိန်၊ နှစ်သက်သောလမ်းကြောင်းများစသည့် ဒေတာများကို အသုံးပြု၍ data analytics tool တစ်ခုကို ဖန်တီးသည်။ ဒါဟာ စျေးနှုန်းချမှတ်ခြင်း၊ လုံခြုံရေး၊ လိမ်လည်မှုရှာဖွေခြင်းနှင့် လမ်းကြောင်းဆုံးဖြတ်ချက်များအတွက် အထောက်အကူပြုသည်။

 * [Sports Analytics](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - _predictive analytics_ (အသင်းနှင့် ကစားသမားခန့်မှန်းမှု - [Moneyball](https://datasciencedegree.wisconsin.edu/blog/moneyball-proves-importance-big-data-big-ideas/) ကို စဉ်းစားပါ - နှင့် ပရိသတ်စီမံခန့်ခွဲမှု) နှင့် _data visualization_ (အသင်းနှင့် ပရိသတ် dashboard များ၊ ကစားပွဲများစသည်) ကို အဓိကထားသည်။ ဒါဟာ talent scouting, sports gambling နှင့် inventory/venue management အတွက် အသုံးချနိုင်သည်။

 * [Data Science in Banking](https://data-flair.training/blogs/data-science-in-banking/) - ဘဏ္ဍာရေးလုပ်ငန်းတွင် ဒေတာသိပ္ပံ၏ တန်ဖိုးကို ဖော်ပြသည်။ ဒါဟာ risk modeling, fraud detection, customer segmentation, real-time prediction နှင့် recommender systems အထိ applications များကို အကျယ်တဝင့်ဖော်ပြသည်။ Predictive analytics သည် [credit scores](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit) ကဲ့သို့သော အရေးကြီးသော အတိုင်းအတာများကိုလည်း drive လုပ်သည်။

 * [Data Science in Healthcare](https://data-flair.training/blogs/data-science-in-healthcare/) - ဒါဟာ medical imaging (ဥပမာ MRI, X-Ray, CT-Scan), genomics (DNA sequencing), drug development (risk assessment, success prediction), predictive analytics (လူနာစောင့်ရှောက်မှုနှင့် ပစ္စည်းထောက်ပံ့မှု logistics), disease tracking & prevention စသည်တို့ကို အဓိကထားသည်။

![Data Science Applications in The Real World](../../../../6-Data-Science-In-Wild/20-Real-World-Examples/images/data-science-applications.png) Image Credit: [Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

ဤပုံသည် ဒေတာသိပ္ပံနည်းလမ်းများကို အသုံးချနိုင်သော အခြား domains နှင့် နမူနာများကို ဖော်ပြသည်။ အခြား applications များကို လေ့လာလိုပါသလား? [Review & Self Study](../../../../6-Data-Science-In-Wild/20-Real-World-Examples) အပိုင်းကို ကြည့်ပါ။

## ဒေတာသိပ္ပံ + သုတေသန

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Research.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              ဒေတာသိပ္ပံနှင့် သုတေသန - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

အမှန်တကယ်အသုံးချမှုများသည် အများအားဖြင့် စက်မှုလုပ်ငန်းများတွင် အတိုင်းအတာချဲ့ထွင်မှုများကို အဓိကထားသော်လည်း၊ _သုတေသန_ applications နှင့် project များသည် အောက်ပါနှစ်ခုအနေဖြင့် အသုံးဝင်နိုင်သည်။

* _innovation opportunities_ - အဆင့်မြင့် concepts များကို prototype လုပ်ခြင်းနှင့် နောက်မျိုးဆက် applications များအတွက် user experience များကို စမ်းသပ်ခြင်း။
* _deployment challenges_ - ဒေတာသိပ္ပံနည်းပညာများ၏ အမှန်တကယ်အသုံးချမှုများတွင် ဖြစ်နိုင်သော အန္တရာယ်များ သို့မဟုတ် မျှော်လင့်မထားသော အကျိုးဆက်များကို စုံစမ်းခြင်း။

ကျောင်းသားများအတွက်၊ သုတေသန project များသည် သင့်ရဲ့ နားလည်မှုကို တိုးတက်စေပြီး၊ သင့်ရဲ့ စိတ်ဝင်စားမှုရှိသော နယ်ပယ်များတွင် လုပ်ကိုင်နေသော လူများ သို့မဟုတ် အဖွဲ့များနှင့် ပိုမိုကျယ်ပြန့်သော awareness နှင့် engagement ကို ရရှိစေမည်ဖြစ်သည်။ ဒါဆိုရင် သုတေသန project များက ဘယ်လိုပုံစံရှိပြီး ဘယ်လို အကျိုးသက်ရောက်မှုရှိနိုင်မလဲ?

နမူနာတစ်ခုကို ကြည့်ပါ - [MIT Gender Shades Study](http://gendershades.org/overview.html) Joy Buolamwini (MIT Media Labs) မှ [signature research paper](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf) ကို Timnit Gebru (Microsoft Research) နှင့် ပူးပေါင်းရေးသားခဲ့သည်။ 

 * **ဘာလဲ:** သုတေသန project ၏ ရည်ရွယ်ချက်မှာ _gender နှင့် skin type အပေါ် အလိုအလျောက် facial analysis algorithm များနှင့် dataset များတွင် bias ရှိမှုကို အကဲဖြတ်ရန်_ ဖြစ်သည်။
 * **ဘာကြောင့်:** Facial analysis ကို ရဲတပ်ဖွဲ့၊ လေဆိပ်လုံခြုံရေး၊ အလုပ်ခန့်ထားမှုစနစ်များကဲ့သို့သော နယ်ပယ်များတွင် အသုံးပြုသည်။ အမှားအယွင်းများ (ဥပမာ bias ကြောင့်) သည် ထိခိုက်သော လူများ သို့မဟုတ် အုပ်စုများအတွက် စီးပွားရေးနှင့် လူမှုရေးအန္တရာယ်များ ဖြစ်စေနိုင်သည်။ Bias များကို နားလည်ခြင်း (နှင့် ဖယ်ရှားခြင်း သို့မဟုတ် လျှော့ချခြင်း) သည် အသုံးပြုမှုတွင် တရားမျှတမှုအတွက် အရေးကြီးသည်။
 * **ဘယ်လို:** သုတေသနသူများသည် ရှိပြီးသား benchmark များသည် အများအားဖြင့် အရောင်နုသော subject များကို အသုံးပြုသည်ကို သိရှိခဲ့ပြီး၊ gender နှင့် skin type အပေါ် _ပိုမိုထိန်းညှိထားသော_ dataset (1000+ images) ကို curate လုပ်ခဲ့သည်။ dataset ကို Microsoft, IBM နှင့် Face++ မှ gender classification products သုံးခု၏ တိကျမှုကို အကဲဖြတ်ရန် အသုံးပြုခဲ့သည်။

ရလဒ်များအရ classification accuracy သည် အထူးသဖြင့် ကောင်းမွန်သော်လည်း၊ အုပ်စုခွဲခြားမှုများအကြား error rate တွင် အားသာချက်များရှိသည်ကို တွေ့ရှိခဲ့သည်။ **misgendering** သည် အမျိုးသမီးများ သို့မဟုတ် အရောင်နက်သော skin type များတွင် ပိုမိုမြင့်မားသည်ကို ဖော်ပြသည်။

**အဓိကရလဒ်များ:** ဒေတာသိပ္ပံသည် _အထောက်အထားပြည့်စုံသော dataset များ_ (subgroup များကို balance လုပ်ထားသော) နှင့် _အဖွဲ့များ၏ အမျိုးမျိုးသော background_ (diverse teams) ကို ပိုမိုလိုအပ်သည်ကို သတိပေးခဲ့သည်။ AI solution များတွင် bias များကို စောစောဖယ်ရှားရန် သို့မဟုတ် လျှော့ချရန် အရေးကြီးသည်။ သုတေသနများသည် _responsible AI_ ကို ဖော်ဆောင်ရန် အဖွဲ့အစည်းများအတွက် အရေးကြီးသော principle များနှင့် လုပ်ထုံးလုပ်နည်းများကို သတ်မှတ်ရန် အထောက်အကူပြုသည်။

**Microsoft ၏ သက်ဆိုင်သော သုတေသနများကို လေ့လာလိုပါသလား?**

* Artificial Intelligence အပေါ် [Microsoft Research Projects](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project) ကို ကြည့်ပါ။
* [Microsoft Research Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/) မှ ကျောင်းသား project များကို လေ့လာပါ။
* [Fairlearn](https://fairlearn.org/) project နှင့် [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) အစီအစဉ်များကို ကြည့်ပါ။

## ဒေတာသိပ္ပံ + လူ့ဘောင်

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              ဒေတာသိပ္ပံနှင့် ဒစ်ဂျစ်တယ် လူ့ဘောင် - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

ဒစ်ဂျစ်တယ် လူ့ဘောင် [ကို အဓိပ္ပာယ်ဖော်ပြထားသည်](https://digitalhumanities.stanford.edu/about-dh-stanford) - "computational methods နှင့် humanistic inquiry ကို ပေါင်းစပ်ထားသော လုပ်ထုံးလုပ်နည်းများနှင့် လမ်းလျှောက်မှုများ၏ စုစည်းမှု" ဟု။ [Stanford projects](https://digitalhumanities.stanford.edu/projects) ကဲ့သို့သော _"rebooting history"_ နှင့် _"poetic thinking"_ သည် [Digital Humanities နှင့် Data Science](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science) အကြား ဆက်နွယ်မှုကို ဖော်ပြသည်။ network analysis, information visualization, spatial နှင့် text analysis ကဲ့သို့သော နည်းလမ်းများကို အဓိကထားပြီး၊ သမိုင်းနှင့် စာပေ dataset များကို ပြန်လည်သုံးသပ်ရန် အသုံးပြုသည်။

*ဒီနယ်ပယ်တွင် project တစ်ခုကို လေ့လာပြီး တိုးတက်စေလိုပါသလား?*

["Emily Dickinson and the Meter of Mood"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671) ကို ကြည့်ပါ - [Jen Looper](https://twitter.com/jenlooper) မှ ဖန်တီးထားသော နမူနာတစ်ခုဖြစ်ပြီး၊ ဒေတာသိပ္ပံကို အသုံးပြု၍ ကဗျာများကို ပြန်လည်သုံးသပ်ပြီး၊ ၎င်း၏ အဓိပ္ပါယ်နှင့် စာရေးသူ၏ အထောက်အပံ့ကို အသစ်သောအခြေအနေများတွင် ပြန်လည်အကဲဖြတ်နိုင်မည်ကို မေးမြန်းသည်။ ဥပမာအားဖြင့်၊ _ကဗျာ၏ tone သို့မဟုတ် sentiment ကို ခွဲခြားခြင်းအားဖြင့် ကဗျာရေးသားခဲ့သော ရာသီဥတုကို ခန့်မှန်းနိုင်မလား_ - ၎င်းသည် သက်ဆိုင်ရာကာလအတွင်း စာရေးသူ၏ စိတ်နေအခြေအနေကို ဘာကို ပြောပြနိုင်သလဲ?

ဒီမေးခွန်းကို ဖြေရှင်းရန်၊ ဒေတာသိပ္ပံ၏ အသက်တာစဉ်ကို လိုက်နာပါ။

 * [`Data Acquisition`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#acquiring-the-dataset) - analysis အတွက် သက်ဆိုင်သော dataset ကို စုဆောင်းရန်။ API (ဥပမာ [Poetry DB API](https://poetrydb.org/index.html)) သို့မဟုတ် web page များကို scraping ([Project Gutenberg](https://www.gutenberg.org/files/12242/12242-h/12242-h.htm)) tools ([Scrapy](https://scrapy.org/)) ကို အသုံးပြုနိုင်သည်။
 * [`Data Cleaning`](https://gist.github.com/jlooper/ce4d102efd057137bc000db
**Planetary Computer Project သည် (Sep 2021 အခြေအနေဖြင့်) စမ်းသပ်မှုအဆင့်တွင်ရှိနေပါသည်** - ဒေတာသိပ္ပံကို အသုံးပြု၍ တာဆောင်မှုဆိုင်ရာ ဖြေရှင်းချက်များကို အထောက်အကူပြုရန် စတင်ပါ။

* [Access တောင်းဆိုပါ](https://planetarycomputer.microsoft.com/account/request) - စတင်လေ့လာပြီး မိတ်ဆွေများနှင့် ချိတ်ဆက်ပါ။
* [Documentation ကိုလေ့လာပါ](https://planetarycomputer.microsoft.com/docs/overview/about) - အထောက်အပံ့ပေးထားသော ဒေတာများနှင့် API များကို နားလည်ရန်။
* [Ecosystem Monitoring](https://analytics-lab.org/ecosystemmonitoring/) ကဲ့သို့သော အက်ပလီကေးရှင်းများကို လေ့လာပြီး အက်ပလီကေးရှင်းအကြံဉာဏ်များအတွက် အားဆွေးပါ။

ဒေတာကို အသုံးပြု၍ ရှုထောင့်များကို ဖော်ထုတ်ခြင်း သို့မဟုတ် အရေးပါသော အချက်အလက်များကို ပိုမိုမြင်သာအောင် ဖော်ပြခြင်းအတွက် visualization ကို ဘယ်လိုအသုံးပြုနိုင်မလဲ စဉ်းစားပါ။ ဒါမှမဟုတ် အချက်အလက်များကို အသုံးပြု၍ သက်သာသောနေထိုင်မှုအတွက် အပြုအမူပြောင်းလဲမှုများကို လှုံ့ဆော်နိုင်သော အသုံးပြုသူအတွေ့အကြုံအသစ်များ ဖန်တီးနိုင်မည့် နည်းလမ်းများကို စဉ်းစားပါ။

## ဒေတာသိပ္ပံ + ကျောင်းသားများ

စက်မှုလုပ်ငန်းနှင့် သုတေသနတွင် အမှန်တကယ်အသုံးချနိုင်သော လျှောက်လွှာများကို ပြောခဲ့ပြီး၊ ဒစ်ဂျစ်တယ် လူ့ဘာသာရပ်များနှင့် တာဆောင်မှုဆိုင်ရာတွင် ဒေတာသိပ္ပံ လျှောက်လွှာ ဥပမာများကို လေ့လာခဲ့ပါသည်။ ဒါဆိုရင် ဒေတာသိပ္ပံကို စတင်လေ့လာနေသူများအနေဖြင့် သင့်ရဲ့ ကျွမ်းကျင်မှုကို ဘယ်လိုတိုးတက်စေပြီး အတူတူမျှဝေနိုင်မလဲ?

ဒီမှာ ကျောင်းသားများအတွက် ဒေတာသိပ္ပံပရောဂျက် ဥပမာများကို တင်ပြထားပါတယ်။

* [MSR Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/#!projects) မှ GitHub [projects](https://github.com/msr-ds3) တွင် အောက်ပါအကြောင်းအရာများကို လေ့လာပါ။
    - [Racial Bias in Police Use of Force](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2019-replicating-an-empirical-analysis-of-racial-differences-in-police-use-of-force/) | [Github](https://github.com/msr-ds3/stop-question-frisk)
    - [Reliability of NYC Subway System](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2018-exploring-the-reliability-of-the-nyc-subway-system/) | [Github](https://github.com/msr-ds3/nyctransit)
* [Digitizing Material Culture: Exploring socio-economic distributions in Sirkap](https://claremont.maps.arcgis.com/apps/Cascade/index.html?appid=bdf2aef0f45a4674ba41cd373fa23afc) - [Ornella Altunyan](https://twitter.com/ornelladotcom) နှင့် Claremont မှ အဖွဲ့၏ [ArcGIS StoryMaps](https://storymaps.arcgis.com/) အသုံးပြုမှု။

## 🚀 စိန်ခေါ်မှု

စတင်လေ့လာသူများအတွက် သင့်လျော်သော ဒေတာသိပ္ပံပရောဂျက်များကို အကြံပြုထားသော ဆောင်းပါးများကို ရှာဖွေပါ - [ဒီ 50 အကြောင်းအရာများ](https://www.upgrad.com/blog/data-science-project-ideas-topics-beginners/) သို့မဟုတ် [ဒီ 21 ပရောဂျက်အကြံဉာဏ်များ](https://www.intellspot.com/data-science-project-ideas) သို့မဟုတ် [ဒီ 16 ပရောဂျက်များနှင့် အရင်းအမြစ်ကုဒ်](https://data-flair.training/blogs/data-science-project-ideas/) ကဲ့သို့သော ပရောဂျက်များကို ဖွင့်လှစ်ပြီး ပြန်လည်ဖန်တီးပါ။ သင့်ရဲ့ လေ့လာမှုခရီးစဉ်များကို ဘလော့ဂ်ရေးပြီး အတွေ့အကြုံများကို အားလုံးနဲ့ မျှဝေဖို့ မမေ့ပါနဲ့။

## Post-Lecture Quiz

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/)

## ပြန်လည်သုံးသပ်ခြင်းနှင့် ကိုယ်တိုင်လေ့လာခြင်း

ပိုမိုအသုံးချနိုင်သော နေရာများကို လေ့လာချင်ပါသလား? ဒီမှာ သက်ဆိုင်ရာ ဆောင်းပါးအချို့ကို တင်ပြထားပါတယ်။
* [17 Data Science Applications and Examples](https://builtin.com/data-science/data-science-applications-examples) - Jul 2021
* [11 Breathtaking Data Science Applications in Real World](https://myblindbird.com/data-science-applications-real-world/) - May 2021
* [Data Science In The Real World](https://towardsdatascience.com/data-science-in-the-real-world/home) - ဆောင်းပါးစုစည်းမှု
* ဒေတာသိပ္ပံတွင်: [ပညာရေး](https://data-flair.training/blogs/data-science-in-education/), [စိုက်ပျိုးရေး](https://data-flair.training/blogs/data-science-in-agriculture/), [ဘဏ္ဍာရေး](https://data-flair.training/blogs/data-science-in-finance/), [ရုပ်ရှင်](https://data-flair.training/blogs/data-science-at-movies/) နှင့် အခြားများ။

## လုပ်ငန်းတာဝန်

[Explore A Planetary Computer Dataset](assignment.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါရှိနိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွဲအမှားအမှားများ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။