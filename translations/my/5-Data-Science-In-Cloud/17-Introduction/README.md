<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-09-05T20:08:56+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "my"
}
-->
# Cloud တွင် Data Science ကိုမိတ်ဆက်ခြင်း

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Cloud တွင် Data Science ကိုမိတ်ဆက်ခြင်း - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

ဒီသင်ခန်းစာမှာ Cloud ရဲ့ အခြေခံအယူအဆတွေကို သင်လေ့လာရမှာဖြစ်ပြီး၊ Cloud ဝန်ဆောင်မှုတွေကို သင့်ရဲ့ Data Science project တွေမှာ အသုံးပြုဖို့ ဘာကြောင့်စိတ်ဝင်စားဖို့ကောင်းတယ်ဆိုတာကိုလည်း သင်မြင်ရမှာဖြစ်ပါတယ်။ ထို့အပြင် Cloud တွင် Data Science project တွေကို အကောင်အထည်ဖော်ထားတဲ့ ဥပမာတွေကိုလည်း ကြည့်ရမှာဖြစ်ပါတယ်။

## [Pre-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## Cloud ဆိုတာဘာလဲ?

Cloud, ဒါမှမဟုတ် Cloud Computing ဆိုတာက အင်တာနက်ပေါ်မှာ host လုပ်ထားတဲ့ infrastructure မှတဆင့် pay-as-you-go computing services အမျိုးမျိုးကို ပေးပို့ခြင်းဖြစ်ပါတယ်။ ဒီဝန်ဆောင်မှုတွေမှာ storage, databases, networking, software, analytics, နဲ့ intelligent services တို့လို solution တွေပါဝင်ပါတယ်။

Cloud တွေကို Public, Private, နဲ့ Hybrid cloud အဖြစ် အောက်ပါအတိုင်း ခွဲခြားတတ်ကြပါတယ်-

* Public cloud: Public cloud ဆိုတာက တတိယပါတီ Cloud ဝန်ဆောင်မှုပေးသူက ပိုင်ဆိုင်ပြီး အင်တာနက်မှတဆင့် လူအများကို computing resources တွေကို ပေးပို့တဲ့စနစ်ဖြစ်ပါတယ်။
* Private cloud: Private cloud ဆိုတာက တစ်ခုတည်းသော စီးပွားရေးလုပ်ငန်း ဒါမှမဟုတ် အဖွဲ့အစည်းတစ်ခုကသာ အသုံးပြုတဲ့ cloud computing resources တွေကို ဆိုလိုပါတယ်။ ဒီဝန်ဆောင်မှုနဲ့ infrastructure တွေကို private network မှာ ထိန်းသိမ်းထားပါတယ်။
* Hybrid cloud: Hybrid cloud ဆိုတာက Public နဲ့ Private cloud တွေကို ပေါင်းစပ်ထားတဲ့စနစ်ဖြစ်ပါတယ်။ အသုံးပြုသူတွေက on-premises datacenter ကို ရွေးချယ်ပြီး data နဲ့ application တွေကို Public cloud တစ်ခု ဒါမှမဟုတ် အများကြီးမှာ run လုပ်နိုင်ပါတယ်။

Cloud computing ဝန်ဆောင်မှုတွေက Infrastructure as a Service (IaaS), Platform as a Service (PaaS), နဲ့ Software as a Service (SaaS) ဆိုတဲ့ အမျိုးအစားသုံးမျိုးအောက်မှာ အများအားဖြင့် ပါဝင်ပါတယ်။

* Infrastructure as a Service (IaaS): အသုံးပြုသူတွေက servers, virtual machines (VMs), storage, networks, operating systems တို့လို IT infrastructure ကို ငှားယူပါတယ်။
* Platform as a Service (PaaS): အသုံးပြုသူတွေက software application တွေကို ဖွံ့ဖြိုးတိုးတက်အောင်လုပ်ခြင်း၊ စမ်းသပ်ခြင်း၊ ပေးပို့ခြင်း၊ နဲ့ စီမံခန့်ခွဲခြင်းအတွက် environment ကို ငှားယူပါတယ်။ အသုံးပြုသူတွေက development အတွက်လိုအပ်တဲ့ servers, storage, network, နဲ့ databases တွေကို စီမံခန့်ခွဲဖို့ စိတ်ပူစရာမလိုပါဘူး။
* Software as a Service (SaaS): အသုံးပြုသူတွေက အင်တာနက်မှတဆင့် software application တွေကို တောင်းဆိုမှုအတိုင်းနဲ့ subscription အခြေခံစနစ်ဖြင့် အသုံးပြုနိုင်ပါတယ်။ Hosting, software application စီမံခန့်ခွဲခြင်း, underlying infrastructure, ဒါမှမဟုတ် maintenance (software upgrades နဲ့ security patching) တွေကို စိတ်ပူစရာမလိုပါဘူး။

Cloud provider အကြီးအကျယ်တွေမှာ Amazon Web Services, Google Cloud Platform နဲ့ Microsoft Azure တို့ပါဝင်ပါတယ်။

## Data Science အတွက် Cloud ကို ဘာကြောင့် ရွေးချယ်သင့်လဲ?

Developer တွေ နဲ့ IT professional တွေက Cloud ကို အောက်ပါအကြောင်းအရင်းတွေကြောင့် ရွေးချယ်တတ်ကြပါတယ်-

* Innovation: Cloud provider တွေက ဖန်တီးထားတဲ့ ဝန်ဆောင်မှုတွေကို သင့် application တွေထဲမှာ တိုက်ရိုက်ပေါင်းစပ်ပြီး သင့် application တွေကို အားဖြည့်နိုင်ပါတယ်။
* Flexibility: သင့်လိုအပ်ချက်အတိုင်း ဝန်ဆောင်မှုတွေကို ရွေးချယ်နိုင်ပြီး သင်လိုအပ်တဲ့ ဝန်ဆောင်မှုအတွက်သာ ပေးဆောင်ရပါတယ်။ သင့်လိုအပ်ချက်အပြောင်းအလဲအတိုင်း ဝန်ဆောင်မှုတွေကို ပြင်ဆင်နိုင်ပါတယ်။
* Budget: Hardware နဲ့ software ဝယ်ယူဖို့၊ on-site datacenter တွေကို စီမံခန့်ခွဲဖို့ စတင်ရင်းနှီးမြှုပ်နှံမှုတွေ မလိုအပ်ပါဘူး။ သင်အသုံးပြုတဲ့အတိုင်းသာ ပေးဆောင်ရပါတယ်။
* Scalability: သင့် project ရဲ့လိုအပ်ချက်အတိုင်း resource တွေကို တိုးချဲ့နိုင်ပါတယ်။ အချိန်အခါအလိုက် computing power, storage, bandwidth တွေကို ပြင်ဆင်နိုင်ပါတယ်။
* Productivity: Datacenter စီမံခန့်ခွဲခြင်းလို အလုပ်တွေကို တစ်ခြားသူတွေကို 맡ပြီး သင့်စီးပွားရေးအပေါ် အာရုံစိုက်နိုင်ပါတယ်။
* Reliability: Cloud Computing က သင့် data ကို အဆက်မပြတ် backup လုပ်ဖို့ နည်းလမ်းအမျိုးမျိုးကို ပေးပြီး၊ အရေးပေါ်အခြေအနေတွေမှာလည်း disaster recovery plan တွေကို စီစဉ်နိုင်ပါတယ်။
* Security: သင့် project ရဲ့လုံခြုံရေးကို အားဖြည့်ပေးတဲ့ policies, technologies နဲ့ controls တွေကို Cloud မှာရရှိနိုင်ပါတယ်။

Cloud ဝန်ဆောင်မှုတွေကို ရွေးချယ်တဲ့ အကြောင်းအရင်းတွေထဲက အများဆုံးတွေက အထက်ပါအချက်တွေဖြစ်ပါတယ်။ Cloud ရဲ့ အဓိကအကျိုးကျေးဇူးတွေကို နားလည်ပြီးတဲ့အခါမှာ Data scientist တွေ နဲ့ data တွေကို အလုပ်လုပ်တဲ့ developer တွေက ရင်ဆိုင်ရတဲ့ စိန်ခေါ်မှုတွေကို Cloud က ဘယ်လိုကူညီနိုင်မလဲဆိုတာကို ကြည့်ရအောင်-

* Data အများကြီးကို သိမ်းဆည်းခြင်း: Server အကြီးကြီးတွေကို ဝယ်ယူ၊ စီမံခန့်ခွဲ၊ နဲ့ ကာကွယ်ဖို့မလိုဘဲ Cloud မှာ data ကို တိုက်ရိုက်သိမ်းဆည်းနိုင်ပါတယ်။ ဥပမာ- Azure Cosmos DB, Azure SQL Database, Azure Data Lake Storage.
* Data Integration လုပ်ဆောင်ခြင်း: Data Integration ဆိုတာ Data Science ရဲ့ အရေးပါတဲ့အစိတ်အပိုင်းဖြစ်ပြီး data collection မှ action လုပ်ဆောင်ခြင်းဆီကို ပြောင်းလဲနိုင်စေပါတယ်။ Cloud မှာရှိတဲ့ Data Factory လို data integration ဝန်ဆောင်မှုတွေကို အသုံးပြုပြီး data source အမျိုးမျိုးက data တွေကို စုဆောင်း၊ ပြောင်းလဲ၊ ပေါင်းစည်းပြီး single data warehouse တစ်ခုထဲမှာ သိမ်းဆည်းနိုင်ပါတယ်။
* Data ကို အ処理လုပ်ခြင်း: Data အများကြီးကို အ処理လုပ်ဖို့ computing power အများကြီးလိုအပ်ပါတယ်။ အားလုံးမှာ အ処理လုပ်ဖို့ လိုအပ်တဲ့ စက်တွေ မရှိနိုင်ပါဘူး။ ဒါကြောင့် Cloud ရဲ့ computing power ကို တိုက်ရိုက်အသုံးပြုပြီး solution တွေကို run နဲ့ deploy လုပ်တတ်ကြပါတယ်။
* Data analytics ဝန်ဆောင်မှုတွေကို အသုံးပြုခြင်း: Azure Synapse Analytics, Azure Stream Analytics, Azure Databricks လို Cloud ဝန်ဆောင်မှုတွေက သင့် data ကို အကျိုးရှိတဲ့ insight တွေဖြစ်အောင် ကူညီပေးနိုင်ပါတယ်။
* Machine Learning နဲ့ data intelligence ဝန်ဆောင်မှုတွေကို အသုံးပြုခြင်း: Cloud provider က ပေးတဲ့ machine learning algorithm တွေကို အသုံးပြုနိုင်ပါတယ်။ ဥပမာ- AzureML. Cognitive services တွေဖြစ်တဲ့ speech-to-text, text-to-speech, computer vision တို့ကိုလည်း အသုံးပြုနိုင်ပါတယ်။

## Cloud တွင် Data Science ရဲ့ ဥပမာများ

### Real-time social media sentiment analysis
Machine learning ကို စတင်လေ့လာသူတွေ အများအားဖြင့် လေ့လာတတ်တဲ့ scenario တစ်ခုဖြစ်တဲ့ social media sentiment analysis ကို real-time မှာ လုပ်ဆောင်ခြင်းကို စတင်ကြည့်ရအောင်။

ဥပမာ- သင့်မှာ news media website တစ်ခုရှိပြီး၊ သင့်ရဲ့ readers တွေ စိတ်ဝင်စားနိုင်တဲ့ content တွေကို နားလည်ဖို့ live data ကို အသုံးပြုချင်တယ်ဆိုပါစို့။ Twitter မှာ post လုပ်ထားတဲ့ data တွေကို real-time sentiment analysis လုပ်ပြီး သင့် readers တွေကို စိတ်ဝင်စားစေမယ့် topic တွေကို သိနိုင်ပါတယ်။

အဓိက indicator တွေက hashtag တွေလို topic တွေမှာ tweet အရေအတွက်နဲ့ sentiment ဖြစ်ပါတယ်။ Sentiment ကို sentiment analysis tool တွေကို အသုံးပြုပြီး သတ်မှတ်ပါတယ်။

ဒီ project ကို ဖန်တီးဖို့ လိုအပ်တဲ့ အဆင့်တွေက-

* Streaming input အတွက် event hub တစ်ခု ဖန်တီးပြီး Twitter မှာ data ကို စုဆောင်းပါ။
* Twitter Streaming APIs ကို ခေါ်ဖို့ Twitter client application ကို configure နဲ့ start လုပ်ပါ။
* Stream Analytics job တစ်ခု ဖန်တီးပါ။
* Job input နဲ့ query ကို သတ်မှတ်ပါ။
* Output sink တစ်ခု ဖန်တီးပြီး job output ကို သတ်မှတ်ပါ။
* Job ကို start လုပ်ပါ။

အပြည့်အစုံကို [documentation](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099) မှာ ကြည့်နိုင်ပါတယ်။

### Scientific papers analysis
ဒီ curriculum ရဲ့ author တစ်ဦးဖြစ်တဲ့ [Dmitry Soshnikov](http://soshnikov.com) ဖန်တီးထားတဲ့ COVID papers ကို analysis လုပ်တဲ့ tool ကို ကြည့်ရအောင်။

Dmitry ရဲ့ project ကို ကြည့်ရင်း၊ သင့်ရဲ့ tool ကို scientific papers မှ knowledge ကို extract လုပ်ပြီး insight တွေ ရယူနိုင်တဲ့ နည်းလမ်းကို သင်လေ့လာနိုင်ပါတယ်။ ထို့အပြင် researcher တွေကို paper collection အကြီးကြီးတွေကို အကျိုးရှိစွာ navigate လုပ်နိုင်ဖို့ ကူညီပေးနိုင်ပါတယ်။

ဒီ project ရဲ့ အဆင့်တွေက-

* [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) ကို အသုံးပြုပြီး အချက်အလက်တွေကို extract နဲ့ pre-process လုပ်ပါ။
* [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) ကို အသုံးပြုပြီး processing ကို parallelize လုပ်ပါ။
* [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) ကို အသုံးပြုပြီး အချက်အလက်တွေကို သိမ်းဆည်းပြီး query လုပ်ပါ။
* Power BI ကို အသုံးပြုပြီး data exploration နဲ့ visualization အတွက် interactive dashboard တစ်ခု ဖန်တီးပါ။

အပြည့်အစုံကို [Dmitry’s blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) မှာ ကြည့်နိုင်ပါတယ်။

Cloud ဝန်ဆောင်မှုတွေကို အသုံးပြုပြီး Data Science ကို အမျိုးမျိုးလုပ်ဆောင်နိုင်တာကို မြင်ရပါပြီ။

## Footnote

Sources:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Post-Lecture Quiz

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/33)

## Assignment

[Market Research](assignment.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါရှိနိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် ရှုလေ့လာသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှုမှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။