<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "39f3b3a9d873eaa522c2e792ce0ca503",
  "translation_date": "2025-09-05T05:09:34+00:00",
  "source_file": "5-Data-Science-In-Cloud/18-Low-Code/README.md",
  "language_code": "my"
}
-->
# Cloud တွင် Data Science: "Low code/No code" နည်းလမ်း

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/18-DataScience-Cloud.png)|
|:---:|
| Cloud တွင် Data Science: Low Code - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

အကြောင်းအရာများ:

- [Cloud တွင် Data Science: "Low code/No code" နည်းလမ်း](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Pre-Lecture quiz](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [1. အကျဉ်းချုပ်](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.1 Azure Machine Learning ဆိုတာဘာလဲ?](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.2 Heart Failure Prediction Project:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [1.3 Heart Failure Dataset:](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [2. Azure ML Studio တွင် Low code/No code နည်းလမ်းဖြင့် မော်ဒယ်ကို လေ့ကျင့်ခြင်း](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.1 Azure ML workspace တစ်ခု ဖန်တီးခြင်း](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.2 Compute Resources](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.1 Compute resources အတွက် ရွေးချယ်မှုများ](../../../../5-Data-Science-In-Cloud/18-Low-Code)
      - [2.2.2 Compute cluster တစ်ခု ဖန်တီးခြင်း](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.3 Dataset ကို Load လုပ်ခြင်း](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [2.4 AutoML ဖြင့် Low code/No code လေ့ကျင့်ခြင်း](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [3. Low code/No code မော်ဒယ်ကို တင်သွင်းခြင်းနှင့် Endpoint ကို အသုံးပြုခြင်း](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.1 မော်ဒယ် တင်သွင်းခြင်း](../../../../5-Data-Science-In-Cloud/18-Low-Code)
    - [3.2 Endpoint ကို အသုံးပြုခြင်း](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [🚀 စိန်ခေါ်မှု](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Post-Lecture Quiz](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Review & Self Study](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  - [Assignment](../../../../5-Data-Science-In-Cloud/18-Low-Code)
  
## [Pre-Lecture quiz](https://ff-quizzes.netlify.app/en/ds/)

## 1. အကျဉ်းချုပ်
### 1.1 Azure Machine Learning ဆိုတာဘာလဲ?

Azure cloud platform သည် 200 ကျော်သော ထုတ်ကုန်များနှင့် cloud ဝန်ဆောင်မှုများကို ပေးဆောင်ပြီး သင့်ရဲ့ အစီအစဉ်အသစ်များကို ဖန်တီးရန် အထောက်အကူပြုသည်။  
Data scientist များသည် အချိန်များစွာကို ဒေတာကို စူးစမ်းခြင်း၊ ကြိုတင်လုပ်ဆောင်ခြင်းနှင့် မော်ဒယ်လေ့ကျင့်မှု algorithm များကို စမ်းသပ်ခြင်းတွင် အသုံးပြုရသည်။ ဤလုပ်ငန်းစဉ်များသည် အချိန်စားပြီး အချို့သော အဆင့်မြင့် hardware များကို မထိရောက်စွာ အသုံးပြုစေသည်။

[Azure ML](https://docs.microsoft.com/azure/machine-learning/overview-what-is-azure-machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) သည် Azure တွင် machine learning ဖြေရှင်းချက်များကို ဖန်တီးရန်နှင့် လုပ်ဆောင်ရန် cloud-based platform တစ်ခုဖြစ်သည်။  
ဤ platform တွင် data scientist များအတွက် အချိန်စားသော လုပ်ငန်းစဉ်များကို အလိုအလျောက်လုပ်ဆောင်ရန် feature များစွာ ပါဝင်ပြီး cloud-based compute resources များကို အသုံးပြုနိုင်စေသည်။  
ဤ resource များသည် ဒေတာအများအပြားကို ထိရောက်စွာ စီမံနိုင်ပြီး အသုံးပြုချိန်တွင်သာ ကုန်ကျစရိတ်ရှိသည်။

Azure ML တွင် machine learning workflow များအတွက် developer များနှင့် data scientist များအတွက် လိုအပ်သော tools များပါဝင်သည်။  
ဤ tools များတွင် ပါဝင်သောအရာများမှာ:

- **Azure Machine Learning Studio**: မော်ဒယ်လေ့ကျင့်ခြင်း၊ တင်သွင်းခြင်း၊ automation၊ tracking နှင့် asset management အတွက် low-code နှင့် no-code ရွေးချယ်မှုများကို ပေးသော web portal ဖြစ်သည်။
- **Jupyter Notebooks**: ML မော်ဒယ်များကို prototype နှင့် စမ်းသပ်ရန် အလွယ်တကူ အသုံးပြုနိုင်သည်။
- **Azure Machine Learning Designer**: drag-n-drop modules များကို အသုံးပြု၍ low-code ပတ်ဝန်းကျင်တွင် စမ်းသပ်မှုများကို ဖန်တီးပြီး pipeline များကို တင်သွင်းနိုင်သည်။
- **Automated machine learning UI (AutoML)**: ML မော်ဒယ်ဖွံ့ဖြိုးမှု၏ iterative လုပ်ငန်းစဉ်များကို အလိုအလျောက်လုပ်ဆောင်ပြီး model quality ကို ထိန်းသိမ်းထားနိုင်သည်။
- **Data Labelling**: ML tool တစ်ခုဖြစ်ပြီး ဒေတာကို အလိုအလျောက် label လုပ်ပေးသည်။
- **Machine learning extension for Visual Studio Code**: ML project များကို ဖန်တီးရန်နှင့် စီမံရန် အပြည့်အစုံ development environment ကို ပေးသည်။
- **Machine learning CLI**: command line မှတစ်ဆင့် Azure ML resources များကို စီမံရန် command များကို ပေးသည်။
- **Open-source frameworks နှင့် ပေါင်းစည်းမှု**: PyTorch, TensorFlow, Scikit-learn စသည်တို့ကို training, deployment နှင့် ML process အဆုံးအထိ စီမံရန် အသုံးပြုနိုင်သည်။
- **MLflow**: ML experiment များ၏ life cycle ကို စီမံရန် open-source library ဖြစ်သည်။ **MLFlow Tracking** သည် training run metrics နှင့် model artifacts များကို log နှင့် track လုပ်ပေးသည်။

### 1.2 Heart Failure Prediction Project:

Project တစ်ခုကို ဖန်တီးခြင်းနှင့် တည်ဆောက်ခြင်းသည် သင်၏ ကျွမ်းကျင်မှုနှင့် အသိပညာကို စမ်းသပ်ရန် အကောင်းဆုံးနည်းလမ်းဖြစ်သည်။  
ဤသင်ခန်းစာတွင် Heart Failure Prediction Project ကို Azure ML Studio တွင် Low code/No code နည်းလမ်းနှင့် Azure ML SDK နည်းလမ်းဖြင့် တည်ဆောက်ခြင်းကို လေ့လာမည်။

![project-schema](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/project-schema.PNG)

Low code/No code နည်းလမ်းသည် GUI (Graphical User Interface) ကို အသုံးပြု၍ စတင်ရန် လွယ်ကူပြီး code အတွေ့အကြုံမလိုအပ်ပါ။  
POC (Proof Of Concept) ဖန်တီးရန် အလွယ်တကူ စမ်းသပ်နိုင်သည်။  
သို့သော် project ကြီးထွားလာသည်နှင့်အမျှ production-ready ဖြစ်ရန် GUI ဖြင့် resource များကို ဖန်တီးရန် မလုံလောက်တော့ပါ။  
ဤအချိန်တွင် Azure ML SDK ကို အသုံးပြု၍ programmatically automate လုပ်ဆောင်ရန် လိုအပ်သည်။

|                   | Low code/No code | Azure ML SDK              |
|-------------------|------------------|---------------------------|
| Code ကျွမ်းကျင်မှု | မလိုအပ်          | လိုအပ်                   |
| ဖွံ့ဖြိုးမှုအချိန် | လွယ်ကူနှင့် မြန် | Code ကျွမ်းကျင်မှုအပေါ် မူတည် |
| Production-ready  | မဟုတ်            | ဟုတ်                     |

### 1.3 Heart Failure Dataset: 

Cardiovascular diseases (CVDs) သည် ကမ္ဘာ့သေဆုံးမှုများ၏ 31% ကို ဖြစ်စေသော အကြီးဆုံးအကြောင်းရင်းဖြစ်သည်။  
တံငါ၊ မကျန်းမာသော အစားအစာ၊ အလေးချိန်ပိုများခြင်း၊ ရုပ်ပိုင်းဆိုင်ရာ မလှုပ်ရှားခြင်းနှင့် အရက်သောက်မှုများကဲ့သို့သော အပြင်ပနှင့် အပြုအမူဆိုင်ရာ အန္တရာယ်များကို estimation model များအတွက် feature အဖြစ် အသုံးပြုနိုင်သည်။  
CVD ဖြစ်နိုင်ခြေကို ခန့်မှန်းနိုင်ခြင်းသည် အန္တရာယ်ရှိသော လူများကို ကာကွယ်ရန် အထောက်အကူပြုနိုင်သည်။

Kaggle တွင် [Heart Failure dataset](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data) ကို အများပြည်သူအတွက် ရရှိနိုင်ပြီး project အတွက် အသုံးပြုမည်။  
ဤ dataset သည် 13 ကော်လံ (12 features နှင့် 1 target variable) နှင့် 299 rows ပါဝင်သော tabular dataset ဖြစ်သည်။

|    | Variable name             | Type            | Description                                               | Example           |
|----|---------------------------|-----------------|-----------------------------------------------------------|-------------------|
| 1  | age                       | numerical       | လူနာ၏ အသက်                                             | 25                |
| 2  | anaemia                   | boolean         | အနီရောင်သွေးဆဲလ်များ သို့မဟုတ် haemoglobin လျော့နည်းခြင်း | 0 or 1            |
| 3  | creatinine_phosphokinase  | numerical       | သွေးထဲရှိ CPK enzyme အဆင့်                              | 542               |
| 4  | diabetes                  | boolean         | လူနာသည် ဆီးချိုရောဂါရှိ/မရှိ                          | 0 or 1            |
| 5  | ejection_fraction         | numerical       | နှလုံး contraction တစ်ခုစီတွင် သွေးထွက်မှု ရာခိုင်နှုန်း | 45                |
| 6  | high_blood_pressure       | boolean         | လူနာသည် သွေးတိုးရောဂါရှိ/မရှိ                          | 0 or 1            |
| 7  | platelets                 | numerical       | သွေးထဲရှိ platelets အရေအတွက်                           | 149000            |
| 8  | serum_creatinine          | numerical       | သွေးထဲရှိ serum creatinine အဆင့်                        | 0.5               |
| 9  | serum_sodium              | numerical       | သွေးထဲရှိ serum sodium အဆင့်                            | jun               |
| 10 | sex                       | boolean         | အမျိုးသမီး သို့မဟုတ် အမျိုးသား                          | 0 or 1            |
| 11 | smoking                   | boolean         | လူနာသည် ဆေးလိပ်သောက်/မသောက်                           | 0 or 1            |
| 12 | time                      | numerical       | follow-up အချိန် (ရက်)                                   | 4                 |
|----|---------------------------|-----------------|-----------------------------------------------------------|-------------------|
| 21 | DEATH_EVENT [Target]      | boolean         | follow-up အချိန်အတွင်း လူနာ သေဆုံး/မသေဆုံး               | 0 or 1            |

Dataset ရရှိပြီးပါက Azure တွင် project ကို စတင်နိုင်ပါသည်။

## 2. Azure ML Studio တွင် Low code/No code နည်းလမ်းဖြင့် မော်ဒယ်ကို လေ့ကျင့်ခြင်း
### 2.1 Azure ML workspace တစ်ခု ဖန်တီးခြင်း
Azure ML တွင် မော်ဒယ်ကို လေ့ကျင့်ရန်အတွက် အရင်ဆုံး Azure ML workspace တစ်ခု ဖန်တီးရန် လိုအပ်သည်။  
Workspace သည် Azure Machine Learning အတွက် အထက်ဆုံး resource ဖြစ်ပြီး ML လုပ်ငန်းစဉ်များနှင့် ဆက်စပ်သော artifacts များကို စီမံရန် အချက်အလက်များကို စုစည်းထားသည်။  
Workspace သည် training run များ၏ မှတ်တမ်းများ၊ log များ၊ metrics များ၊ output များနှင့် script များ၏ snapshot ကို သိမ်းဆည်းထားသည်။  
ဤအချက်အလက်များကို အသုံးပြု၍ အကောင်းဆုံး မော်ဒယ်ကို ဖန်တီးနိုင်သည်။ [ပိုမိုလေ့လာရန်](https://docs.microsoft.com/azure/machine-learning/concept-workspace?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

အောက်ပါ browser များကို အသုံးပြုရန် အကြံပြုသည်:

- Microsoft Edge (နောက်ဆုံး version)
- Safari (Mac အတွက် နောက်ဆုံး version)
- Chrome (နောက်ဆုံး version)
- Firefox (နောက်ဆုံး version)

Azure Machine Learning ကို အသုံးပြုရန်အတွက် သင့် Azure subscription တွင် workspace တစ်ခု ဖန်တီးပါ။  
ဤ workspace ကို ML workload များနှင့် ဆက်စပ်သော data, compute resources, code, models နှင့် artifacts များကို စီမံရန် အသုံးပြုနိုင်သည်။

> **_မှတ်ချက်:_** Azure ML workspace ရှိနေသ zolang Azure subscription တွင် data storage အတွက် အနည်းငယ်ကုန်ကျစရိတ်ရှိမည်ဖြစ်သောကြောင့် workspace ကို မလိုအပ်တော့ပါက ဖျက်ရန် အကြံပြုသည်။

1. [Azure portal](https://ms.portal.azure.com/) တွင် Microsoft credentials ဖြင့် လိုင်အင်ဝင်ပါ။
2. **＋Create a resource** ကို ရွေးပါ
   
   ![workspace-1](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-1.PNG)

   Machine Learning ကို ရှာပြီး Machine Learning tile ကို ရွေးပါ

   ![workspace-2](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-2.PNG)

   Create button ကို နှိပ်ပါ

   ![workspace-3](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-3.PNG)

   အောက်ပါအတိုင်း setting များကို ဖြည့်ပါ:
   - Subscription: သင့် Azure subscription
   - Resource group: Resource group တစ်ခု ဖန်တီးပါ သို့မဟုတ် ရွေးပါ
   - Workspace name: သင့် workspace အတွက် ထူးခြားသော နာမည်တစ်ခု ထည့်ပါ
   - Region: သင့်နီးစပ်သော ဒေသကို ရွေးပါ
   - Storage account: Workspace အတွက် ဖန်တီးမည့် default storage account ကို မှတ်သားပါ
   - Key vault: Workspace အတွက် ဖန်တီးမည့် default key vault ကို မှတ်သားပါ
   - Application insights: Workspace အတွက် ဖန်တီးမည့် default application insights resource ကို မှတ်သားပါ
   - Container registry: None (မော်ဒယ်ကို container သို့ တင်သွင်းသောအခါ အလိုအလျောက် ဖန်တီးမည်)

    ![workspace-4](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-4.PNG)

   - Create + review ကို နှိပ်ပြီး create button ကို နှိပ်ပါ
3. Workspace ဖန်တီးမှုအတွက် မိနစ်အနည်းငယ် စောင့်ပါ။ ပြီးလျှင် portal တွင် workspace ကို သွားပါ။ Machine Learning Azure service မှတစ်ဆင့် ရှာနိုင်သည်။
4. Workspace ၏ Overview စာမျက်နှာတွင် Azure Machine Learning studio ကို ဖွင့်ပါ (သို့မဟုတ် browser tab အသစ်တွင် https://ml.azure.com သို့ သွားပါ)။ Microsoft account ဖြင့် ML studio တွင် လိုင်အင်ဝင်ပါ။  
   Azure directory, subscription နှင့် ML workspace ကို ရွေးပါ။

![workspace-5](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-5.PNG)

5. Azure Machine Learning studio တွင် ☰ icon ကို အပေါ်ဘက်တွင် toggle လုပ်ပြီး interface ၏ စာမျက်နှာများကို ကြည့်ပါ။  
   Workspace resources များကို စီမံရန် ဤစာမျက်နှာများကို အသုံးပြုနိုင်သည်။

![workspace-6](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/workspace-6.PNG)

Azure portal ကို အသုံးပြု၍ workspace ကို စီမံနိုင်သော်လည်း data scientist များနှင့် ML operations engineer များအတွက် Azure Machine Learning Studio သည် workspace resources များကို စီမံရန် ပိုမိုအာရုံစိုက်သော user interface ကို ပေးသည်။

### 2.2 Compute Resources

Compute Resources သည် cloud-based resource များဖြစ်ပြီး ML မော်ဒယ်လေ့ကျင့်ခြင်းနှင့် data စူးစမ်းမှုလုပ်ငန်းစဉ်များကို run လုပ်ရန် အသုံးပြုနိုင်သည်။  
Compute resource များတွင် အောက်ပါအမျိုးအစား ၄ မျိုး ပါဝင်သည်:

- **Compute Instances**: Data scientist များအတွက် development workstation များဖြစ်ပြီး Virtual Machine (VM) တစ်ခု ဖန်တီးပြီး notebook instance ကို ဖွင့်နိုင်သည်။ Notebook မှ compute cluster ကို ခေါ်ပြီး မော်ဒယ်ကို လေ့ကျင့်နိုင်သည်။
- **Compute Clusters**: VM များ၏ scalable cluster များဖြစ်ပြီး experiment code ကို on-demand ဖြင့် process လုပ်ရန် အသုံးပြုသည်။  
   မော်ဒယ်ကို လေ့ကျင့်ရန်
- **Attached Compute**: Azure ရဲ့ Virtual Machines သို့မဟုတ် Azure Databricks clusters ကဲ့သို့သော ရှိပြီးသား Azure compute resources များနှင့် ချိတ်ဆက်ထားသည်။

#### 2.2.1 သင့် compute resources အတွက် ရွေးချယ်မှုများကို မှန်ကန်စွာ ရွေးချယ်ခြင်း

Compute resource တစ်ခုကို ဖန်တီးရာတွင် အရေးကြီးသော ဆုံးဖြတ်ချက်များကို လုပ်ဆောင်ရန် အဓိကအချက်အချို့ကို စဉ်းစားရန် လိုအပ်သည်။

**CPU သို့မဟုတ် GPU လိုအပ်ပါသလား?**

CPU (Central Processing Unit) သည် ကွန်ပျူတာပရိုဂရမ်၏ အမိန့်များကို အကောင်အထည်ဖော်ဆောင်ရွက်သော အီလက်ထရောနစ် စက်ကိရိယာဖြစ်သည်။ GPU (Graphics Processing Unit) သည် အမြန်နှုန်းမြင့်သော rate ဖြင့် ဂရပ်ဖစ်ဆိုင်ရာ ကုဒ်များကို ဆောင်ရွက်နိုင်သော အထူးပြု အီလက်ထရောနစ် စက်ကိရိယာဖြစ်သည်။

CPU နှင့် GPU architecture အကြား အဓိကကွာခြားချက်မှာ CPU သည် tasks များကို အမြန်နှုန်းမြင့် (CPU clock speed ဖြင့် တိုင်းတာသည်) ဖြင့် ဆောင်ရွက်ရန် အတွက် ဒီဇိုင်းထုတ်ထားပြီး တစ်ချိန်တည်းတွင် ဆောင်ရွက်နိုင်သော tasks များအရေအတွက်မှာ ကန့်သတ်ထားသည်။ GPU များသည် parallel computing အတွက် ဒီဇိုင်းထုတ်ထားပြီး deep learning tasks များတွင် ပိုမိုထူးချွန်သည်။

| CPU                                     | GPU                         |
|-----------------------------------------|-----------------------------|
| စျေးနှုန်းသက်သာ                          | စျေးနှုန်းမြင့်              |
| Concurrency အဆင့်နိမ့်                  | Concurrency အဆင့်မြင့်       |
| Deep learning models များကို လေ့ကျင့်ရာတွင် နှေး | Deep learning အတွက် အကောင်းဆုံး |

**Cluster Size**

Cluster အရွယ်အစားကြီးသည် စျေးကြီးသော်လည်း ပိုမိုတုံ့ပြန်မှုကောင်းမွန်စေသည်။ ထို့ကြောင့် အချိန်ရှိပြီး ငွေမလုံလောက်ပါက cluster သေးငယ်ကို စတင်သင့်သည်။ အချိန်မရှိဘဲ ငွေရှိပါက cluster ကြီးကို စတင်သင့်သည်။

**VM Size**

RAM, disk, core အရေအတွက်နှင့် clock speed အရွယ်အစားကို သင့်အချိန်နှင့် ဘတ်ဂျက်အကန့်အသတ်အပေါ် မူတည်၍ ပြောင်းလဲနိုင်သည်။ အဆိုပါ parameters များအားလုံးကို တိုးမြှင့်ခြင်းသည် စျေးကြီးသော်လည်း performance ကောင်းမွန်စေသည်။

**Dedicated သို့မဟုတ် Low-Priority Instances?**

Low-priority instance သည် interruptible ဖြစ်သည်။ Microsoft Azure သည် အဆိုပါ resources များကို အခြား task တစ်ခုသို့ ပေးအပ်နိုင်ပြီး job ကို ခေတ္တရပ်တန့်စေသည်။ Dedicated instance သို့မဟုတ် non-interruptible သည် သင့်ခွင့်ပြုချက်မရှိဘဲ job ကို ရပ်တန့်မည်မဟုတ်ပါ။ 

ဤသည်မှာ အချိန်နှင့် ငွေကြား ဆုံးဖြတ်ချက်တစ်ခုဖြစ်ပြီး interruptible instances များသည် dedicated instances များထက် စျေးသက်သာသည်။

#### 2.2.2 Compute cluster ဖန်တီးခြင်း

[Azure ML workspace](https://ml.azure.com/) တွင် compute ကို သွားပြီး compute instances, compute clusters, inference clusters နှင့် attached compute ကဲ့သို့သော compute resources များကို ကြည့်ရှုနိုင်သည်။ ဤ project အတွက် model training အတွက် compute cluster တစ်ခုလိုအပ်သည်။ Studio တွင် "Compute" menu ကို click လုပ်ပြီး "Compute cluster" tab ကို ရွေးချယ်ပါ။ "+ New" button ကို click လုပ်၍ compute cluster တစ်ခု ဖန်တီးပါ။

![22](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-1.PNG)

1. Dedicated vs Low priority, CPU or GPU, VM size နှင့် core အရေအတွက်ကို ရွေးချယ်ပါ (ဤ project အတွက် default settings ကို ထားနိုင်သည်)။
2. Next button ကို click လုပ်ပါ။

![23](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-2.PNG)

3. Cluster ကို compute name တစ်ခုပေးပါ။
4. Minimum/Maximum nodes အရေအတွက်, Idle seconds before scale down, SSH access ကို ရွေးချယ်ပါ။ Minimum nodes အရေအတွက် 0 ဖြစ်ပါက cluster idle ဖြစ်နေစဉ် ငွေသက်သာစေပါသည်။ Maximum nodes အရေအတွက်မြင့်မားသည် training အချိန်ကို လျှော့ချစေပါသည်။ Maximum nodes အရေအတွက်အများဆုံး 3 ဖြစ်သည်။
5. "Create" button ကို click လုပ်ပါ။ ဤအဆင့်သည် မိနစ်အနည်းငယ်ကြာနိုင်သည်။

![29](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/cluster-3.PNG)

အံ့မခန်းပါ! ယခု Compute cluster ရှိပြီးဖြစ်သောကြောင့် Azure ML Studio သို့ data ကို load လုပ်ရန် လိုအပ်ပါသည်။

### 2.3 Dataset ကို Load လုပ်ခြင်း

1. [Azure ML workspace](https://ml.azure.com/) တွင် "Datasets" ကို click လုပ်ပြီး "+ Create dataset" button ကို click လုပ်ပါ။ "From local files" option ကို ရွေးချယ်ပြီး ယခင်က download လုပ်ထားသော Kaggle dataset ကို ရွေးပါ။

   ![24](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-1.PNG)

2. Dataset ကို name, type နှင့် description ပေးပါ။ Next ကို click လုပ်ပါ။ Files မှ data ကို upload လုပ်ပါ။ Next ကို click လုပ်ပါ။

   ![25](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-2.PNG)

3. Schema တွင် anaemia, diabetes, high blood pressure, sex, smoking, နှင့် DEATH_EVENT အတွက် data type ကို Boolean သို့ ပြောင်းပါ။ Next ကို click လုပ်ပြီး Create ကို click လုပ်ပါ။

   ![26](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/dataset-3.PNG)

အလွန်ကောင်းမွန်ပါသည်! Dataset ရှိပြီး Compute cluster ဖန်တီးပြီးဖြစ်သောကြောင့် model training ကို စတင်နိုင်ပါပြီ!

### 2.4 AutoML ဖြင့် Low code/No Code training

Traditional machine learning model ဖွံ့ဖြိုးတိုးတက်မှုသည် အရင်းအမြစ်များကို အလွန်လိုအပ်ပြီး domain knowledge နှင့် အချိန်များကို model များစွာ ဖန်တီးနှိုင်းယှဉ်ရန် လိုအပ်သည်။ Automated machine learning (AutoML) သည် machine learning model ဖွံ့ဖြိုးတိုးတက်မှု၏ အချိန်စား iterative tasks များကို အလိုအလျောက်လုပ်ဆောင်ခြင်းဖြစ်သည်။ 

AutoML သည် data scientists, analysts, နှင့် developers များကို ML models များကို အမြင့်ဆုံး scale, efficiency, နှင့် productivity ဖြင့် ဖန်တီးရန် ခွင့်ပြုသည်။ [Learn more](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

1. [Azure ML workspace](https://ml.azure.com/) တွင် "Automated ML" ကို click လုပ်ပြီး upload လုပ်ထားသော dataset ကို ရွေးပါ။ Next ကို click လုပ်ပါ။

   ![27](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-1.PNG)

2. Experiment name အသစ်, target column (DEATH_EVENT) နှင့် ဖန်တီးထားသော compute cluster ကို ထည့်ပါ။ Next ကို click လုပ်ပါ။

   ![28](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-2.PNG)

3. "Classification" ကို ရွေးပြီး Finish ကို click လုပ်ပါ။ ဤအဆင့်သည် compute cluster size အပေါ်မူတည်၍ 30 မိနစ်မှ 1 နာရီကြား ကြာနိုင်သည်။

    ![30](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-3.PNG)

4. Run ပြီးဆုံးသောအခါ "Automated ML" tab ကို click လုပ်ပြီး run ကို click လုပ်ပါ။ "Best model summary" card တွင် Algorithm ကို click လုပ်ပါ။

    ![31](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/aml-4.PNG)

ဒီနေရာတွင် AutoML ဖန်တီးထားသော အကောင်းဆုံး model ၏ အသေးစိတ်ဖော်ပြချက်ကို ကြည့်ရှုနိုင်ပါသည်။ Models tab တွင် ဖန်တီးထားသော အခြား mode များကိုလည်း စူးစမ်းနိုင်ပါသည်။ Explanations (preview button) တွင် models များကို စစ်ဆေးရန် အချိန်ယူပါ။ AutoML ရွေးချယ်ထားသော အကောင်းဆုံး model ကို ရွေးချယ်ပြီး deployment လုပ်ပုံကို ကြည့်ရှုမည်။

## 3. Low code/No Code model deployment နှင့် endpoint consumption
### 3.1 Model deployment

Automated machine learning interface သည် အကောင်းဆုံး model ကို web service အဖြစ် deployment လုပ်ရန် အဆင့်အနည်းငယ်ဖြင့် ခွင့်ပြုသည်။ Deployment သည် model ကို အသစ်သော data အပေါ် အတိအကျခန့်မှန်းနိုင်ရန်နှင့် အခွင့်အလမ်းများကို ရှာဖွေရန် အIntegration ဖြစ်သည်။ 

Best model description တွင် "Deploy" button ကို click လုပ်ပါ။

![deploy-1](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-1.PNG)

15. Name, description, compute type (Azure Container Instance), authentication ကို enable လုပ်ပြီး Deploy ကို click လုပ်ပါ။ ဤအဆင့်သည် 20 မိနစ်ခန့် ကြာနိုင်သည်။ Deployment process တွင် model ကို register လုပ်ခြင်း၊ resources များကို ဖန်တီးခြင်းနှင့် web service အတွက် configure လုပ်ခြင်းတို့ ပါဝင်သည်။ Deploy status အောက်တွင် status message တစ်ခု ပေါ်လာသည်။ Refresh ကို အကြိမ်ကြိမ် click လုပ်၍ deployment status ကို စစ်ဆေးပါ။ Status "Healthy" ဖြစ်သောအခါ deployment ပြီးဆုံးပြီး run ဖြစ်နေသည်။

![deploy-2](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-2.PNG)

16. Deployment ပြီးဆုံးသောအခါ Endpoint tab ကို click လုပ်ပြီး deploy လုပ်ထားသော endpoint ကို click လုပ်ပါ။ Endpoint အကြောင်းအသေးစိတ်ကို ဒီနေရာတွင် ကြည့်ရှုနိုင်ပါသည်။

![deploy-3](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/deploy-3.PNG)

အံ့မခန်းပါ! Model ကို deploy လုပ်ပြီးဖြစ်သောကြောင့် endpoint consumption ကို စတင်နိုင်ပါပြီ။

### 3.2 Endpoint consumption

"Consume" tab ကို click လုပ်ပါ။ REST endpoint နှင့် consumption option တွင် python script ကို တွေ့နိုင်ပါသည်။ Python code ကို အချိန်ယူဖတ်ပါ။

ဤ script ကို သင့် local machine မှ တိုက်ရိုက် run လုပ်နိုင်ပြီး endpoint ကို consume လုပ်ပါမည်။

![35](../../../../5-Data-Science-In-Cloud/18-Low-Code/images/consumption-1.PNG)

ဤကုဒ်၏ 2 လိုင်းကို စစ်ဆေးပါ:

```python
url = 'http://98e3715f-xxxx-xxxx-xxxx-9ec22d57b796.centralus.azurecontainer.io/score'
api_key = '' # Replace this with the API key for the web service
```  
`url` variable သည် consume tab တွင် တွေ့ရသော REST endpoint ဖြစ်ပြီး `api_key` variable သည် consume tab တွင် တွေ့ရသော primary key ဖြစ်သည် (authentication ကို enable လုပ်ထားသောအခါတွင်သာပါဝင်သည်)။ Script သည် endpoint ကို consume လုပ်ပုံမှာ ဤပုံစံဖြစ်သည်။

18. Script ကို run လုပ်ပါက အောက်ပါ output ကို တွေ့ရမည်:
    ```python
    b'"{\\"result\\": [true]}"'
    ```  
ဤသည်မှာ heart failure အတွက် prediction သည် true ဖြစ်ကြောင်းကို ဆိုလိုသည်။ Script တွင် default data အားလုံးသည် 0 နှင့် false ဖြစ်နေသောကြောင့် ဤအချက်အလက်သည် make sense ဖြစ်သည်။ Input sample အောက်ပါအတိုင်း data ကို ပြောင်းလဲနိုင်သည်:

```python
data = {
    "data":
    [
        {
            'age': "0",
            'anaemia': "false",
            'creatinine_phosphokinase': "0",
            'diabetes': "false",
            'ejection_fraction': "0",
            'high_blood_pressure': "false",
            'platelets': "0",
            'serum_creatinine': "0",
            'serum_sodium': "0",
            'sex': "false",
            'smoking': "false",
            'time': "0",
        },
        {
            'age': "60",
            'anaemia': "false",
            'creatinine_phosphokinase': "500",
            'diabetes': "false",
            'ejection_fraction': "38",
            'high_blood_pressure': "false",
            'platelets': "260000",
            'serum_creatinine': "1.40",
            'serum_sodium': "137",
            'sex': "false",
            'smoking': "false",
            'time': "130",
        },
    ],
}
```  
Script သည် အောက်ပါ output ကို ပြန်ပေးမည်:
    ```python
    b'"{\\"result\\": [true, false]}"'
    ```  

ဂုဏ်ယူပါတယ်! Azure ML တွင် model ကို train လုပ်ပြီး deploy လုပ်ပြီး consume လုပ်ပြီးဖြစ်ပါပြီ!

> **_NOTE:_** Project ပြီးဆုံးသောအခါ resources အားလုံးကို delete လုပ်ရန် မမေ့ပါနှင့်။
## 🚀 Challenge

AutoML ဖန်တီးထားသော အကောင်းဆုံး models များ၏ explanations နှင့် details ကို စစ်ဆေးပါ။ အကောင်းဆုံး model သည် အခြား model များထက် အကောင်းဆုံးဖြစ်ရသည့် အကြောင်းရင်းကို နားလည်ရန် ကြိုးစားပါ။ Compare လုပ်ထားသော algorithms များက ဘာတွေလဲ? အကြားကွာခြားချက်များက ဘာတွေလဲ? ဤအခါတွင် အကောင်းဆုံး model သည် ဘာကြောင့် ပိုမိုထူးချွန်သနည်း?

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/)

## Review & Self Study

ဤသင်ခန်းစာတွင် heart failure risk ကို cloud တွင် Low code/No code နည်းဖြင့် predict လုပ်ရန် model ကို train, deploy နှင့် consume လုပ်ပုံကို သင်ယူခဲ့ပါသည်။ AutoML ဖန်တီးထားသော model explanations များကို စူးစမ်းပြီး အကောင်းဆုံး model သည် အခြား model များထက် အကောင်းဆုံးဖြစ်ရသည့် အကြောင်းရင်းကို နားလည်ရန် ကြိုးစားပါ။

Low code/No code AutoML အကြောင်းကို [documentation](https://docs.microsoft.com/azure/machine-learning/tutorial-first-experiment-automated-ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) ကို ဖတ်ရှုခြင်းဖြင့် ပိုမိုနက်နက်ရှိုင်းရှိုင်း သင်ယူနိုင်ပါသည်။

## Assignment

[Low code/No code Data Science project on Azure ML](assignment.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် ရှုလို့ရပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှု ဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။