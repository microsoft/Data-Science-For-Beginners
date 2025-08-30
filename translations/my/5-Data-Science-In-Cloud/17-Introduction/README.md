<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "408c55cab2880daa4e78616308bd5db7",
  "translation_date": "2025-08-30T17:49:34+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "my"
}
-->
# Cloud တွင် ဒေတာသိပ္ပံကို မိတ်ဆက်ခြင်း

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Cloud တွင် ဒေတာသိပ္ပံ: မိတ်ဆက် - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

ဒီသင်ခန်းစာမှာ Cloud ရဲ့ အခြေခံအချက်တွေကို သင်လေ့လာမယ်၊ Cloud ဝန်ဆောင်မှုတွေကို သင့်ဒေတာသိပ္ပံပရောဂျက်တွေမှာ အသုံးပြုရတဲ့ အကြောင်းရင်းတွေကို နားလည်မယ်၊ နောက်ပြီး Cloud တွင် အကောင်အထည်ဖော်ထားတဲ့ ဒေတာသိပ္ပံပရောဂျက်အချို့ကို ကြည့်ရှုမယ်။

## [Pre-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## Cloud ဆိုတာဘာလဲ?

Cloud (Cloud Computing) ဆိုတာကတော့ အင်တာနက်ပေါ်မှာ တည်ဆောက်ထားတဲ့ အခြေခံအဆောက်အအုံတစ်ခုမှ ပေးအပ်တဲ့ pay-as-you-go စနစ်အောက်ရှိ ကွန်ပျူတာဝန်ဆောင်မှုအမျိုးမျိုးကို ရယူအသုံးပြုခြင်းဖြစ်ပါတယ်။ ဒီဝန်ဆောင်မှုတွေမှာ သိုလှောင်မှု၊ ဒေတာဘေ့စ်၊ နက်ဝက်၊ ဆော့ဖ်ဝဲ၊ သုံးသပ်မှုနဲ့ အတူ အတုအယောင်အဆင့်မြင့်ဝန်ဆောင်မှုတွေ ပါဝင်ပါတယ်။

Cloud တွေကို အများအားဖြင့် Public, Private, Hybrid ဆိုပြီး ခွဲခြားတင်ပြလေ့ရှိပါတယ်။

* Public cloud: Public cloud ဆိုတာက Cloud ဝန်ဆောင်မှုပေးသူတစ်ဦးက ပိုင်ဆိုင်ပြီး အများပြည်သူအတွက် အင်တာနက်မှတဆင့် ကွန်ပျူတာရင်းမြစ်တွေကို ပေးအပ်တဲ့ စနစ်ဖြစ်ပါတယ်။
* Private cloud: Private cloud ဆိုတာက တစ်ဦးချင်းလုပ်ငန်းတစ်ခု သို့မဟုတ် အဖွဲ့အစည်းတစ်ခုအတွက်သာ အသုံးပြုတဲ့ Cloud Computing ရင်းမြစ်တွေကို ဆိုလိုပါတယ်။ ဒီဝန်ဆောင်မှုနဲ့ အခြေခံအဆောက်အအုံတွေကို ပုဂ္ဂလိကနက်ဝက်မှာ ထိန်းသိမ်းထားပါတယ်။
* Hybrid cloud: Hybrid cloud ဆိုတာက Public နဲ့ Private cloud တွေကို ပေါင်းစပ်ထားတဲ့ စနစ်ဖြစ်ပါတယ်။ အသုံးပြုသူတွေက On-premises datacenter ကို ရွေးချယ်ပြီး ဒေတာနဲ့ အပလီကေးရှင်းတွေကို Public cloud တစ်ခု သို့မဟုတ် တစ်ခုထက်ပိုတဲ့ Cloud တွေမှာ လည်ပတ်စေပါတယ်။

Cloud Computing ဝန်ဆောင်မှုအများစုကို အောက်ပါ သုံးမျိုးအဖြစ် ခွဲခြားတင်ပြလေ့ရှိပါတယ် - Infrastructure as a Service (IaaS), Platform as a Service (PaaS), Software as a Service (SaaS)။

* Infrastructure as a Service (IaaS): အသုံးပြုသူတွေက Server, Virtual Machine (VM), Storage, Network, Operating System စတဲ့ IT အခြေခံအဆောက်အအုံတွေကို ငှားယူအသုံးပြုပါတယ်။
* Platform as a Service (PaaS): အသုံးပြုသူတွေက ဆော့ဖ်ဝဲအပလီကေးရှင်းတွေကို ဖန်တီး၊ စမ်းသပ်၊ ပို့ဆောင်၊ စီမံခန့်ခွဲဖို့ အတွက် ပတ်ဝန်းကျင်တစ်ခုကို ငှားယူအသုံးပြုပါတယ်။ Server, Storage, Network, Database စတဲ့ အခြေခံအဆောက်အအုံတွေကို စီမံခန့်ခွဲဖို့ မလိုအပ်ပါဘူး။
* Software as a Service (SaaS): အသုံးပြုသူတွေက အင်တာနက်မှတဆင့် ဆော့ဖ်ဝဲအပလီကေးရှင်းတွေကို လိုအပ်သလို ရယူအသုံးပြုနိုင်ပါတယ်။ Hosting, Maintenance, Software Upgrade, Security Patching စတာတွေကို စိတ်ပူစရာမလိုပါဘူး။

Cloud ဝန်ဆောင်မှုပေးသူအကြီးစားတွေမှာ Amazon Web Services, Google Cloud Platform, Microsoft Azure တို့ ပါဝင်ပါတယ်။

## Cloud ကို ဒေတာသိပ္ပံအတွက် ရွေးချယ်ရတဲ့ အကြောင်းရင်းများ

Developer တွေနဲ့ IT ပရော်ဖက်ရှင်နယ်တွေက Cloud ကို အောက်ပါအကြောင်းရင်းတွေကြောင့် ရွေးချယ်တတ်ကြပါတယ် -

* **Innovation**: Cloud ဝန်ဆောင်မှုပေးသူတွေ ဖန်တီးထားတဲ့ နည်းပညာဆန်းသစ်မှုတွေကို သင့်အပလီကေးရှင်းထဲမှာ တိုက်ရိုက်ပေါင်းစပ်နိုင်ပါတယ်။
* **Flexibility**: လိုအပ်တဲ့ ဝန်ဆောင်မှုတွေကိုသာ ပေးချေပြီး သင့်လိုအပ်ချက်အပေါ်မူတည်ပြီး ဝန်ဆောင်မှုတွေကို ရွေးချယ်နိုင်ပါတယ်။
* **Budget**: Hardware, Software ဝယ်ယူဖို့ စတင်ရင်းနှီးမြှုပ်နှံမှုမလိုအပ်ဘဲ သုံးသလောက်ပေးချေစနစ်နဲ့ အသုံးပြုနိုင်ပါတယ်။
* **Scalability**: သင့်ပရောဂျက်လိုအပ်ချက်အပေါ်မူတည်ပြီး Computing Power, Storage, Bandwidth တွေကို တိုးချဲ့ သို့မဟုတ် လျှော့ချနိုင်ပါတယ်။
* **Productivity**: Datacenter စီမံခန့်ခွဲမှုလိုမျိုး အချိန်စားတဲ့ အလုပ်တွေကို တာဝန်ပေးပြီး သင့်လုပ်ငန်းအပေါ် အာရုံစိုက်နိုင်ပါတယ်။
* **Reliability**: Cloud Computing က ဒေတာကို အမြဲ Backup လုပ်ထားနိုင်တဲ့ နည်းလမ်းတွေကို ပေးစွမ်းပြီး အရေးပေါ်အခြေအနေတွေမှာလည်း Disaster Recovery Plan တွေကို သတ်မှတ်နိုင်ပါတယ်။
* **Security**: သင့်ပရောဂျက်ရဲ့ လုံခြုံရေးကို တိုးတက်စေမယ့် နည်းပညာနဲ့ မူဝါဒတွေကို Cloud မှာ ရရှိနိုင်ပါတယ်။

Cloud ရဲ့ အကျိုးကျေးဇူးတွေကို နားလည်ပြီးတဲ့အခါ ဒေတာသိပ္ပံပညာရှင်တွေနဲ့ ဒေတာအပေါ် အလုပ်လုပ်တဲ့ Developer တွေ ဘယ်လိုအခက်အခဲတွေကို Cloud က ဖြေရှင်းပေးနိုင်မလဲဆိုတာကို ဆက်လက်လေ့လာကြည့်ရအောင် -

* **ဒေတာအများကြီးကို သိုလှောင်ခြင်း**: Server ကြီးတွေကို ဝယ်ယူ၊ စီမံခန့်ခွဲ၊ ကာကွယ်စောင့်ရှောက်ဖို့ မလိုအပ်ဘဲ Azure Cosmos DB, Azure SQL Database, Azure Data Lake Storage စတဲ့ Cloud သိုလှောင်မှုဖြေရှင်းနည်းတွေကို အသုံးပြုနိုင်ပါတယ်။
* **ဒေတာပေါင်းစည်းခြင်း**: ဒေတာပေါင်းစည်းမှုက ဒေတာသိပ္ပံရဲ့ အရေးကြီးတဲ့ အစိတ်အပိုင်းဖြစ်ပြီး ဒေတာစုဆောင်းမှုကနေ လုပ်ဆောင်မှုဆီသို့ ပြောင်းလဲစေပါတယ်။ Cloud မှာရှိတဲ့ Data Factory နဲ့ တစ်နေရာထဲမှာ ဒေတာကို စုဆောင်း၊ ပြောင်းလဲ၊ ပေါင်းစည်းနိုင်ပါတယ်။
* **ဒေတာကို လုပ်ဆောင်ခြင်း**: ဒေတာအများကြီးကို လုပ်ဆောင်ဖို့ Computing Power အများကြီးလိုအပ်ပါတယ်။ Cloud ရဲ့ အင်အားကြီး Computing Power ကို အသုံးပြုပြီး သင့်ဖြေရှင်းနည်းတွေကို လည်ပတ် deploy လုပ်နိုင်ပါတယ်။
* **ဒေတာသုံးသပ်မှုဝန်ဆောင်မှုအသုံးပြုခြင်း**: Azure Synapse Analytics, Azure Stream Analytics, Azure Databricks စတဲ့ Cloud ဝန်ဆောင်မှုတွေက သင့်ဒေတာကို အကျိုးရှိတဲ့ သုံးသပ်ချက်တွေထုတ်ပေးနိုင်ပါတယ်။
* **Machine Learning နဲ့ ဒေတာအတုအယောင်ဝန်ဆောင်မှုအသုံးပြုခြင်း**: AzureML နဲ့ Cloud Provider တွေက ပေးတဲ့ Machine Learning Algorithm တွေကို အသုံးပြုနိုင်ပါတယ်။ Speech-to-text, Text-to-speech, Computer Vision စတဲ့ Cognitive Services တွေကိုလည်း အသုံးပြုနိုင်ပါတယ်။

## Cloud တွင် ဒေတာသိပ္ပံပရောဂျက်နမူနာများ

အခုတော့ နမူနာအချို့ကို ကြည့်ရှုပြီး ပိုမိုရှင်းလင်းစေပါမယ်။

### အချိန်နှင့်တပြေးညီ လူမှုမီဒီယာခံစားချက်သုံးသပ်မှု
Machine Learning စတင်လေ့လာသူတွေ အများအားဖြင့် လေ့လာကြတဲ့ နမူနာတစ်ခုဖြစ်တဲ့ လူမှုမီဒီယာခံစားချက်သုံးသပ်မှုကို စတင်ကြည့်ရှုကြပါစို့။

သင့်မှာ သတင်းမီဒီယာဝဘ်ဆိုက်တစ်ခုရှိပြီး သင့်ဖတ်ရှုသူတွေ စိတ်ဝင်စားမယ့် အကြောင်းအရာတွေကို နားလည်ချင်တယ်ဆိုပါစို့။ Twitter မှာရှိတဲ့ ပိုစ့်တွေကို အချိန်နှင့်တပြေးညီ သုံးသပ်ပြီး သင့်ဖတ်ရှုသူတွေအတွက် အရေးပါတဲ့ အကြောင်းအရာတွေကို သိရှိနိုင်ဖို့ အစီအစဉ်တစ်ခု ဖန်တီးနိုင်ပါတယ်။

ဒီပရောဂျက်ကို ဖန်တီးဖို့ လိုအပ်တဲ့ အဆင့်တွေက -

* Twitter မှာ ဒေတာစုဆောင်းဖို့ Event Hub တစ်ခု ဖန်တီးပါ။
* Twitter Streaming APIs ကို ခေါ်ဖို့ Twitter Client Application တစ်ခုကို စတင် configure လုပ်ပါ။
* Stream Analytics Job တစ်ခု ဖန်တီးပါ။
* Job Input နဲ့ Query ကို သတ်မှတ်ပါ။
* Output Sink တစ်ခု ဖန်တီးပြီး Job Output ကို သတ်မှတ်ပါ။
* Job ကို စတင်ပါ။

အပြည့်အစုံကို ကြည့်ရှုဖို့ [documentation](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099) ကို ကြည့်ပါ။

### သိပ္ပံစာတမ်းများကို သုံးသပ်ခြင်း
ဒီသင်ရိုးညွှန်းတန်းရဲ့ အရေးပါတဲ့ အဖွဲ့ဝင်တစ်ဦးဖြစ်တဲ့ [Dmitry Soshnikov](http://soshnikov.com) ဖန်တီးထားတဲ့ COVID စာတမ်းတွေကို သုံးသပ်တဲ့ ပရောဂျက်တစ်ခုကို ကြည့်ရှုကြပါစို့။

ဒီပရောဂျက်ကို လေ့လာခြင်းအားဖြင့် သိပ္ပံစာတမ်းတွေထဲက အသိပညာကို ထုတ်ယူပြီး သုတေသနလုပ်သူတွေ အတွက် အကျိုးရှိတဲ့ နည်းလမ်းတစ်ခုကို ဖန်တီးနိုင်ပါတယ်။

ဒီပရောဂျက်ရဲ့ အဆင့်တွေက -

* [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) နဲ့ သတင်းအချက်အလက်တွေကို ထုတ်ယူပြီး ကြိုတင်လုပ်ဆောင်ပါ။
* [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) ကို အသုံးပြုပြီး လုပ်ဆောင်မှုကို ပျမ်းမျှလုပ်ဆောင်ပါ။
* [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) ကို အသုံးပြုပြီး သတင်းအချက်အလက်တွေကို သိမ်းဆည်းပြီး ရှာဖွေပါ။
* Power BI ကို အသုံးပြုပြီး ဒေတာကို ရှာဖွေခြင်းနဲ့ ရှင်းလင်းပြသမှုအတွက် Interactive Dashboard တစ်ခု ဖန်တီးပါ။

အပြည့်အစုံကို [Dmitry’s blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) မှာ ကြည့်ရှုနိုင်ပါတယ်။

Cloud ဝန်ဆောင်မှုတွေကို အသုံးပြုပြီး ဒေတာသိပ္ပံလုပ်ငန်းတွေကို အကောင်အထည်ဖော်နိုင်တဲ့ နည်းလမ်းတွေ အများကြီး ရှိပါတယ်။

## Footnote

Sources:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Post-Lecture Quiz

[Post-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/33)

## Assignment

[Market Research](assignment.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါရှိနိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွဲအချော်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။