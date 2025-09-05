<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a0556b17de4c8d1a9470b02247b01d4",
  "translation_date": "2025-09-05T05:10:51+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "my"
}
-->
# Cloud တွင် Data Science ကိုမိတ်ဆက်ခြင်း

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Cloud တွင် Data Science ကိုမိတ်ဆက်ခြင်း - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

ဒီသင်ခန်းစာမှာ Cloud ရဲ့ အခြေခံအယူအဆတွေကို သင်လေ့လာမယ်၊ Cloud ကို သင့် Data Science project တွေမှာ အသုံးပြုဖို့ ဘာကြောင့် စိတ်ဝင်စားစရာကောင်းတယ်ဆိုတာကို သိရှိရမယ်၊ နောက်ပြီး Cloud တွင် Data Science project တွေကို အကောင်အထည်ဖော်ထားတဲ့ ဥပမာတွေကို ကြည့်မယ်။

## [Pre-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## Cloud ဆိုတာဘာလဲ?

Cloud, ဒါမှမဟုတ် Cloud Computing ဆိုတာက အင်တာနက်ပေါ်မှာ pay-as-you-go အခြေခံနဲ့ ဝန်ဆောင်မှုအမျိုးမျိုးကို ပေးပို့တဲ့ နည်းလမ်းတစ်ခုဖြစ်ပါတယ်။ ဒီဝန်ဆောင်မှုတွေမှာ storage, databases, networking, software, analytics, နဲ့ intelligent services တို့ပါဝင်ပါတယ်။

Cloud တွေကို Public, Private, နဲ့ Hybrid ဆိုပြီး ခွဲခြားတယ်။

* Public cloud: Public cloud ဆိုတာက တတိယပါတီ Cloud ဝန်ဆောင်မှုပေးသူက ပိုင်ဆိုင်ပြီး အင်တာနက်ပေါ်မှာ လူအများကို computing resources တွေ ပေးပို့တဲ့ စနစ်ဖြစ်ပါတယ်။
* Private cloud: Private cloud ဆိုတာက တစ်ခုတည်းသော လုပ်ငန်းသို့မဟုတ် အဖွဲ့အစည်းအတွက်သာ အသုံးပြုတဲ့ Cloud computing resources တွေကို ဆိုလိုပါတယ်။ ဒီဝန်ဆောင်မှုနဲ့ infrastructure တွေကို private network ပေါ်မှာ ထိန်းသိမ်းထားပါတယ်။
* Hybrid cloud: Hybrid cloud ဆိုတာက Public နဲ့ Private cloud တွေကို ပေါင်းစပ်ထားတဲ့ စနစ်ဖြစ်ပါတယ်။ အသုံးပြုသူတွေက on-premises datacenter ကို ရွေးချယ်ပြီး data နဲ့ applications တွေကို Public cloud တစ်ခု သို့မဟုတ် အများကြီးမှာ run လုပ်နိုင်ပါတယ်။

Cloud computing ဝန်ဆောင်မှုတွေကို အဓိကအားဖြင့် Infrastructure as a Service (IaaS), Platform as a Service (PaaS), နဲ့ Software as a Service (SaaS) ဆိုပြီး ခွဲခြားတယ်။

* Infrastructure as a Service (IaaS): အသုံးပြုသူတွေက servers, virtual machines (VMs), storage, networks, operating systems စတဲ့ IT infrastructure တွေကို ငှားယူပါတယ်။
* Platform as a Service (PaaS): အသုံးပြုသူတွေက software applications တွေကို ဖွံ့ဖြိုးတိုးတက်အောင်လုပ်ဖို့၊ စမ်းသပ်ဖို့၊ ပေးပို့ဖို့၊ နဲ့ စီမံခန့်ခွဲဖို့ environment ကို ငှားယူပါတယ်။ underlying infrastructure ကို စီမံခန့်ခွဲဖို့ မလိုအပ်ပါဘူး။
* Software as a Service (SaaS): အသုံးပြုသူတွေက အင်တာနက်ပေါ်မှာ software applications တွေကို subscription အခြေခံနဲ့ အသုံးပြုနိုင်ပါတယ်။ hosting, maintenance, နဲ့ security patching စတာတွေကို စိတ်ပူစရာမလိုပါဘူး။

Cloud provider အကြီးအကျယ်တွေမှာ Amazon Web Services, Google Cloud Platform, Microsoft Azure တို့ပါဝင်ပါတယ်။

## Data Science အတွက် Cloud ကို ဘာကြောင့် ရွေးချယ်သင့်လဲ?

Developer တွေ နဲ့ IT professional တွေက Cloud ကို အောက်ပါအကြောင်းအရင်းတွေကြောင့် ရွေးချယ်တယ်။

* Innovation: Cloud provider တွေက ဖန်တီးထားတဲ့ ဝန်ဆောင်မှုတွေကို သင့် application တွေမှာ တိုက်ရိုက်ပေါင်းစပ်နိုင်ပါတယ်။
* Flexibility: သင့်လိုအပ်ချက်အတိုင်း ဝန်ဆောင်မှုတွေကို ရွေးချယ်နိုင်ပြီး pay-as-you-go စနစ်နဲ့ အသုံးပြုနိုင်ပါတယ်။
* Budget: hardware နဲ့ software ဝယ်ယူဖို့၊ on-site datacenter တွေကို စီမံခန့်ခွဲဖို့ စတင်ရင်းနှီးမြှုပ်နှံမှု မလိုအပ်ပါဘူး။
* Scalability: project ရဲ့ လိုအပ်ချက်အတိုင်း resources တွေကို အလိုအလျောက် တိုးမြှင့်နိုင်ပါတယ်။
* Productivity: datacenter စီမံခန့်ခွဲမှုလိုမျိုး task တွေကို အခြားသူတွေကို 맡ပြီး သင့်လုပ်ငန်းပေါ်မှာ အာရုံစိုက်နိုင်ပါတယ်။
* Reliability: Cloud Computing က သင့် data ကို backup လုပ်ဖို့ နည်းလမ်းအမျိုးမျိုးပေးပြီး disaster recovery plan တွေကို ဖန်တီးနိုင်ပါတယ်။
* Security: Cloud provider တွေက သင့် project ရဲ့ လုံခြုံရေးကို အားကောင်းစေတဲ့ နည်းပညာနဲ့ policy တွေကို ပေးပါတယ်။

Cloud ရဲ့ အကျိုးကျေးဇူးတွေကို နားလည်ပြီးရင် Data scientist တွေ နဲ့ data ကို အလုပ်လုပ်တဲ့ developer တွေ ဘယ်လို challenges တွေကို Cloud က ကူညီနိုင်မလဲဆိုတာကို ကြည့်ကြမယ်။

* Data အများကြီးကို သိမ်းဆည်းခြင်း: server ใหญ่တွေကို ဝယ်ယူ၊ စီမံခန့်ခွဲ၊ နဲ့ ကာကွယ်ဖို့မလိုဘဲ Cloud မှာ data ကို သိမ်းဆည်းနိုင်ပါတယ်။
* Data Integration လုပ်ဆောင်ခြင်း: Cloud မှာ Data Factory နဲ့ data integration ကို လွယ်ကူစွာလုပ်နိုင်ပါတယ်။
* Data ကို process လုပ်ခြင်း: Cloud ရဲ့ computing power ကို အသုံးပြုပြီး data ကို process လုပ်နိုင်ပါတယ်။
* Data analytics ဝန်ဆောင်မှုတွေကို အသုံးပြုခြင်း: Azure Synapse Analytics, Azure Stream Analytics, Azure Databricks စတဲ့ tools တွေကို အသုံးပြုနိုင်ပါတယ်။
* Machine Learning နဲ့ data intelligence ဝန်ဆောင်မှုတွေကို အသုံးပြုခြင်း: AzureML နဲ့ cognitive services တွေကို အသုံးပြုနိုင်ပါတယ်။

## Cloud တွင် Data Science project ဥပမာများ

### Real-time social media sentiment analysis
Machine learning စတင်လေ့လာသူတွေ အများအားဖြင့် လေ့လာတဲ့ scenario တစ်ခုဖြစ်တဲ့ social media sentiment analysis ကို ကြည့်မယ်။

ဥပမာအားဖြင့် သင့်ရဲ့ news media website မှာ Twitter data ကို sentiment analysis လုပ်ပြီး သင့်ရဲ့ readers တွေ စိတ်ဝင်စားမယ့် content ကို သိရှိနိုင်ဖို့ project တစ်ခု ဖန်တီးနိုင်ပါတယ်။

ဒီ project ကို ဖန်တီးဖို့ လိုအပ်တဲ့ အဆင့်တွေက:

* Twitter data ကို စုဆောင်းဖို့ event hub တစ်ခု ဖန်တီးပါ။
* Twitter Streaming APIs ကို ခေါ်ဖို့ Twitter client application တစ်ခုကို စတင်ပါ။
* Stream Analytics job တစ်ခု ဖန်တီးပါ။
* Job input နဲ့ query ကို သတ်မှတ်ပါ။
* Output sink တစ်ခု ဖန်တီးပြီး job output ကို သတ်မှတ်ပါ။
* Job ကို စတင်ပါ။

အပြည့်အစုံကို [documentation](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099) မှာ ကြည့်ပါ။

### Scientific papers analysis
[Dmitry Soshnikov](http://soshnikov.com) ရဲ့ COVID papers analysis tool ကို ကြည့်မယ်။

ဒီ project မှာ:

* [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) နဲ့ information ကို extract နဲ့ pre-process လုပ်ပါ။
* [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) ကို အသုံးပြုပြီး processing ကို parallelize လုပ်ပါ။
* [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) ကို အသုံးပြုပြီး information ကို သိမ်းဆည်းပါ။
* Power BI ကို အသုံးပြုပြီး interactive dashboard တစ်ခု ဖန်တီးပါ။

အပြည့်အစုံကို [Dmitry’s blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) မှာ ကြည့်ပါ။

Cloud services တွေကို Data Science project တွေမှာ ဘယ်လိုအသုံးချနိုင်လဲဆိုတာကို အထက်ပါ ဥပမာတွေက ပြသထားပါတယ်။

## Footnote

Sources:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Post-Lecture Quiz

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/)

## Assignment

[Market Research](assignment.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။