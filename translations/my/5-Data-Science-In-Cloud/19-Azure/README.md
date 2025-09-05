<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "472d3fab1c5be50f387336e7a686dbe1",
  "translation_date": "2025-09-05T20:09:32+00:00",
  "source_file": "5-Data-Science-In-Cloud/19-Azure/README.md",
  "language_code": "my"
}
-->
# Cloud တွင် Data Science: "Azure ML SDK" နည်းလမ်း

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/19-DataScience-Cloud.png)|
|:---:|
| Cloud တွင် Data Science: Azure ML SDK - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

အကြောင်းအရာများစာရင်း:

- [Cloud တွင် Data Science: "Azure ML SDK" နည်းလမ်း](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Pre-Lecture Quiz](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [1. အကျဉ်းချုပ်](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [1.1 Azure ML SDK ဆိုတာဘာလဲ?](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [1.2 နှလုံးရောဂါခန့်မှန်းမှုပရောဂျက်နှင့်ဒေတာအချက်အလက်မိတ်ဆက်](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [2. Azure ML SDK ဖြင့်မော်ဒယ်တစ်ခုကိုလေ့ကျင့်ခြင်း](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.1 Azure ML workspace တစ်ခုဖန်တီးခြင်း](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.2 Compute instance တစ်ခုဖန်တီးခြင်း](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.3 ဒေတာအချက်အလက်တင်သွင်းခြင်း](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.4 Notebook ဖန်တီးခြင်း](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.5 မော်ဒယ်လေ့ကျင့်ခြင်း](../../../../5-Data-Science-In-Cloud/19-Azure)
      - [2.5.1 Workspace, experiment, compute cluster နှင့် dataset ကိုတပ်ဆင်ခြင်း](../../../../5-Data-Science-In-Cloud/19-Azure)
      - [2.5.2 AutoML Configuration နှင့်လေ့ကျင့်ခြင်း](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [3. Azure ML SDK ဖြင့်မော်ဒယ်တင်သွင်းခြင်းနှင့် endpoint အသုံးပြုခြင်း](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.1 အကောင်းဆုံးမော်ဒယ်ကိုသိမ်းဆည်းခြင်း](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.2 မော်ဒယ်တင်သွင်းခြင်း](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.3 Endpoint အသုံးပြုခြင်း](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [🚀 စိန်ခေါ်မှု](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Post-lecture quiz](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [ပြန်လည်သုံးသပ်ခြင်းနှင့်ကိုယ်တိုင်လေ့လာခြင်း](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [အလုပ်ပေးစာ](../../../../5-Data-Science-In-Cloud/19-Azure)

## [Pre-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/36)

## 1. အကျဉ်းချုပ်

### 1.1 Azure ML SDK ဆိုတာဘာလဲ?

Data scientist များနှင့် AI developer များသည် Azure Machine Learning SDK ကိုအသုံးပြု၍ Azure Machine Learning service ဖြင့် machine learning workflow များကိုတည်ဆောက်ပြီးအကောင်အထည်ဖော်ပါသည်။ Python environment မည်သည့်အမျိုးအစားမဆို (Jupyter Notebooks, Visual Studio Code, သို့မဟုတ် သင်နှစ်သက်သော Python IDE) မှာ service ကိုအသုံးပြုနိုင်ပါသည်။

SDK ၏အဓိကအပိုင်းများမှာ:

- Machine learning experiment များတွင်အသုံးပြုသော dataset များကိုလေ့လာခြင်း၊ ပြင်ဆင်ခြင်းနှင့် lifecycle ကိုစီမံခန့်ခွဲခြင်း။
- Cloud resources များကိုစီမံခန့်ခွဲခြင်း၊ log မှတ်တမ်းများနှင့် experiment များကိုစီမံခန့်ခွဲခြင်း။
- မော်ဒယ်များကို local တွင်လေ့ကျင့်ခြင်း သို့မဟုတ် GPU acceleration ပါသော cloud resources အသုံးပြု၍လေ့ကျင့်ခြင်း။
- Automated machine learning ကိုအသုံးပြုခြင်း၊ configuration parameters နှင့် training data ကိုလက်ခံပြီး အကောင်းဆုံးမော်ဒယ်ကို algorithms နှင့် hyperparameter settings များဖြင့်အလိုအလျောက်ရှာဖွေခြင်း။
- Web services များကို deploy လုပ်၍ trained model များကို RESTful services အဖြစ်ပြောင်းလဲပြီး application များတွင်အသုံးပြုနိုင်ခြင်း။

[Azure Machine Learning SDK အကြောင်းပိုမိုလေ့လာရန်](https://docs.microsoft.com/python/api/overview/azure/ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

[ယခင်သင်ခန်းစာ](../18-Low-Code/README.md) တွင် Low code/No code နည်းလမ်းဖြင့် မော်ဒယ်ကိုလေ့ကျင့်ခြင်း၊ တင်သွင်းခြင်းနှင့်အသုံးပြုခြင်းကိုကြည့်ခဲ့ပါသည်။ Heart Failure dataset ကိုအသုံးပြု၍ Heart failure prediction model ကိုဖန်တီးခဲ့ပါသည်။ ဒီသင်ခန်းစာတွင် Azure Machine Learning SDK ကိုအသုံးပြု၍ အတူတူသောအရာကိုပြုလုပ်သွားမည်ဖြစ်သည်။

![project-schema](../../../../5-Data-Science-In-Cloud/19-Azure/images/project-schema.PNG)

### 1.2 နှလုံးရောဂါခန့်မှန်းမှုပရောဂျက်နှင့်ဒေတာအချက်အလက်မိတ်ဆက်

[ဒီနေရာ](../18-Low-Code/README.md) တွင် Heart failure prediction project နှင့် dataset မိတ်ဆက်ကိုကြည့်ပါ။

## 2. Azure ML SDK ဖြင့်မော်ဒယ်တစ်ခုကိုလေ့ကျင့်ခြင်း
### 2.1 Azure ML workspace တစ်ခုဖန်တီးခြင်း

ရိုးရှင်းစွာ Jupyter notebook တွင်အလုပ်လုပ်မည်ဖြစ်သည်။ ဒါက Workspace နှင့် compute instance ရှိပြီးသားဖြစ်သည်ကိုဆိုလိုသည်။ Workspace ရှိပြီးသားဖြစ်ပါက **2.3 Notebook ဖန်တီးခြင်း** အပိုင်းသို့တိုက်ရိုက်သွားနိုင်ပါသည်။

Workspace မရှိသေးပါက [ယခင်သင်ခန်းစာ](../18-Low-Code/README.md) တွင် **2.1 Azure ML workspace တစ်ခုဖန်တီးခြင်း** အပိုင်းကိုလိုက်နာ၍ workspace တစ်ခုဖန်တီးပါ။

### 2.2 Compute instance တစ်ခုဖန်တီးခြင်း

[Azure ML workspace](https://ml.azure.com/) တွင် Compute menu သို့သွားပါ။ Compute resources များကိုတွေ့မြင်နိုင်ပါသည်။

![compute-instance-1](../../../../5-Data-Science-In-Cloud/19-Azure/images/compute-instance-1.PNG)

Jupyter notebook ကို provision လုပ်ရန် compute instance တစ်ခုဖန်တီးပါ။
1. + New button ကိုနှိပ်ပါ။
2. Compute instance ကိုအမည်ပေးပါ။
3. CPU သို့မဟုတ် GPU, VM size နှင့် core အရေအတွက်ကိုရွေးပါ။
4. Create button ကိုနှိပ်ပါ။

အောင်မြင်စွာ compute instance တစ်ခုဖန်တီးပြီးပါပြီ! [Notebook ဖန်တီးခြင်း](../../../../5-Data-Science-In-Cloud/19-Azure) အပိုင်းတွင် compute instance ကိုအသုံးပြုမည်ဖြစ်သည်။

### 2.3 ဒေတာအချက်အလက်တင်သွင်းခြင်း
Dataset ကို upload မလုပ်ရသေးပါက [ယခင်သင်ခန်းစာ](../18-Low-Code/README.md) တွင် **2.3 Loading the Dataset** အပိုင်းကိုကြည့်ပါ။

### 2.4 Notebook ဖန်တီးခြင်း

> **_NOTE:_** နောက်တစ်ဆင့်တွင် notebook အသစ်တစ်ခုကိုစတင်ဖန်တီးနိုင်သလို [ယခင်ဖန်တီးထားသော notebook](../../../../5-Data-Science-In-Cloud/19-Azure/notebook.ipynb) ကို upload လုပ်နိုင်ပါသည်။ Upload လုပ်ရန် "Notebook" menu ကိုနှိပ်ပြီး notebook ကို upload လုပ်ပါ။

Notebook များသည် data science လုပ်ငန်းစဉ်တွင်အရေးပါသောအခန်းကဏ္ဍတစ်ခုဖြစ်သည်။ EDA (Exploratory Data Analysis) ပြုလုပ်ခြင်း၊ compute cluster သို့ခေါ်သွား၍ မော်ဒယ်ကိုလေ့ကျင့်ခြင်း၊ inference cluster သို့ခေါ်သွား၍ endpoint ကို deploy လုပ်ခြင်းတို့အတွက်အသုံးပြုနိုင်သည်။

Notebook ဖန်တီးရန် Jupyter notebook instance ကို run လုပ်နေသော compute node တစ်ခုလိုအပ်သည်။ [Azure ML workspace](https://ml.azure.com/) သို့ပြန်သွားပြီး Compute instances ကိုနှိပ်ပါ။ [ယခင်ဖန်တီးထားသော compute instance](../../../../5-Data-Science-In-Cloud/19-Azure) ကိုတွေ့မြင်နိုင်ပါသည်။

1. Applications အပိုင်းတွင် Jupyter option ကိုနှိပ်ပါ။
2. "Yes, I understand" box ကိုအမှန်ခြစ်ပြီး Continue button ကိုနှိပ်ပါ။
![notebook-1](../../../../5-Data-Science-In-Cloud/19-Azure/images/notebook-1.PNG)
3. Jupyter notebook instance ကို browser tab အသစ်တွင်ဖွင့်ပါ။ "New" button ကိုနှိပ်ပြီး notebook တစ်ခုဖန်တီးပါ။

![notebook-2](../../../../5-Data-Science-In-Cloud/19-Azure/images/notebook-2.PNG)

Notebook ရရှိပြီးပါက Azure ML SDK ဖြင့်မော်ဒယ်ကိုလေ့ကျင့်နိုင်ပါပြီ။

### 2.5 မော်ဒယ်လေ့ကျင့်ခြင်း

မည်သည့်အချိန်တွင်မဆို သင်မသေချာပါက [Azure ML SDK documentation](https://docs.microsoft.com/python/api/overview/azure/ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) ကိုကြည့်ပါ။ ဒီသင်ခန်းစာတွင်တွေ့မြင်မည့် module များကိုနားလည်ရန်လိုအပ်သောအချက်အလက်များပါဝင်သည်။

#### 2.5.1 Workspace, experiment, compute cluster နှင့် dataset ကိုတပ်ဆင်ခြင်း

Configuration file မှ `workspace` ကို load လုပ်ရန်အောက်ပါ code ကိုအသုံးပြုပါ:

```python
from azureml.core import Workspace
ws = Workspace.from_config()
```

ဒီ code သည် workspace ကိုကိုယ်စားပြုသော `Workspace` အမျိုးအစား object ကိုပြန်ပေးသည်။ experiment တစ်ခုကိုအောက်ပါ code ဖြင့်ဖန်တီးရန်လိုအပ်သည်:

```python
from azureml.core import Experiment
experiment_name = 'aml-experiment'
experiment = Experiment(ws, experiment_name)
```
Workspace မှ experiment ကိုရယူရန် experiment name ကိုအသုံးပြုပါ။ Experiment name သည် 3-36 characters ရှိရမည်၊ အက္ခရာ သို့မဟုတ် နံပါတ်ဖြင့်စရမည်၊ အက္ခရာ၊ နံပါတ်၊ underscore နှင့် dash များသာပါဝင်နိုင်သည်။ Workspace တွင် experiment မရှိပါက အသစ်တစ်ခုဖန်တီးမည်ဖြစ်သည်။

Training အတွက် compute cluster တစ်ခုဖန်တီးရန်အောက်ပါ code ကိုအသုံးပြုပါ။ ဒီအဆင့်သည်မိနစ်အနည်းငယ်ကြာနိုင်သည်။

```python
from azureml.core.compute import AmlCompute

aml_name = "heart-f-cluster"
try:
    aml_compute = AmlCompute(ws, aml_name)
    print('Found existing AML compute context.')
except:
    print('Creating new AML compute context.')
    aml_config = AmlCompute.provisioning_configuration(vm_size = "Standard_D2_v2", min_nodes=1, max_nodes=3)
    aml_compute = AmlCompute.create(ws, name = aml_name, provisioning_configuration = aml_config)
    aml_compute.wait_for_completion(show_output = True)

cts = ws.compute_targets
compute_target = cts[aml_name]
```

Workspace မှ dataset ကို dataset name ဖြင့်ရယူနိုင်သည်:

```python
dataset = ws.datasets['heart-failure-records']
df = dataset.to_pandas_dataframe()
df.describe()
```
#### 2.5.2 AutoML Configuration နှင့်လေ့ကျင့်ခြင်း

AutoML configuration ကို [AutoMLConfig class](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.automlconfig(class)?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) ကိုအသုံးပြု၍တပ်ဆင်ပါ။

Doc တွင်ဖော်ပြထားသည့်အတိုင်း parameter များစွာရှိပြီး သင်စိတ်ကြိုက်ပြင်ဆင်နိုင်သည်။ ဒီ project အတွက် အောက်ပါ parameter များကိုအသုံးပြုမည်ဖြစ်သည်:

- `experiment_timeout_minutes`: Experiment ကို run လုပ်ခွင့်ရရှိသည့်အချိန်အများဆုံး (မိနစ်)။
- `max_concurrent_iterations`: Experiment အတွက် concurrent training iteration အများဆုံး။
- `primary_metric`: Experiment ၏အခြေအနေကိုသတ်မှတ်ရန်အသုံးပြုသော primary metric။
- `compute_target`: Automated Machine Learning experiment ကို run လုပ်ရန် Azure Machine Learning compute target။
- `task`: Run လုပ်ရန် task အမျိုးအစား။ 'classification', 'regression', 'forecasting' တို့ဖြစ်နိုင်သည်။
- `training_data`: Experiment အတွင်း training data အဖြစ်အသုံးပြုမည့် data။
- `label_column_name`: Label column ၏အမည်။
- `path`: Azure Machine Learning project folder ၏လမ်းကြောင်း။
- `enable_early_stopping`: အချိန်တိုအတွင်း score မတိုးတက်ပါက early termination ကိုဖွင့်ရန်။
- `featurization`: Featurization ကိုအလိုအလျောက်လုပ်ရန် သို့မဟုတ် customized featurization ကိုအသုံးပြုရန်။
- `debug_log`: Debug အချက်အလက်များကိုရေးသားရန် log file။

```python
from azureml.train.automl import AutoMLConfig

project_folder = './aml-project'

automl_settings = {
    "experiment_timeout_minutes": 20,
    "max_concurrent_iterations": 3,
    "primary_metric" : 'AUC_weighted'
}

automl_config = AutoMLConfig(compute_target=compute_target,
                             task = "classification",
                             training_data=dataset,
                             label_column_name="DEATH_EVENT",
                             path = project_folder,  
                             enable_early_stopping= True,
                             featurization= 'auto',
                             debug_log = "automl_errors.log",
                             **automl_settings
                            )
```
Configuration ကိုတပ်ဆင်ပြီးပါက အောက်ပါ code ဖြင့်မော်ဒယ်ကိုလေ့ကျင့်နိုင်သည်။ ဒီအဆင့်သည် cluster size ပေါ်မူတည်၍ တစ်နာရီအထိကြာနိုင်သည်။

```python
remote_run = experiment.submit(automl_config)
```
RunDetails widget ကို run လုပ်၍ experiment များကိုပြသနိုင်သည်။
```python
from azureml.widgets import RunDetails
RunDetails(remote_run).show()
```
## 3. Azure ML SDK ဖြင့်မော်ဒယ်တင်သွင်းခြင်းနှင့် endpoint အသုံးပြုခြင်း

### 3.1 အကောင်းဆုံးမော်ဒယ်ကိုသိမ်းဆည်းခြင်း

`remote_run` သည် [AutoMLRun](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.run.automlrun?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) အမျိုးအစား object ဖြစ်သည်။ ဒီ object တွင် `get_output()` method ပါဝင်ပြီး အကောင်းဆုံး run နှင့်သက်ဆိုင်သော fitted model ကိုပြန်ပေးသည်။

```python
best_run, fitted_model = remote_run.get_output()
```
အကောင်းဆုံးမော်ဒယ်တွင်အသုံးပြုသော parameters ကို fitted_model ကို print လုပ်၍ကြည့်နိုင်သည်။ [get_properties()](https://docs.microsoft.com/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py#azureml_core_Run_get_properties?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) method ကိုအသုံးပြု၍ မော်ဒယ်၏ properties ကိုကြည့်နိုင်သည်။

```python
best_run.get_properties()
```

အကောင်းဆုံးမော်ဒယ်ကို [register_model](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.run.automlrun?view=azure-ml-py#register-model-model-name-none--description-none--tags-none--iteration-none--metric-none-?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) method ဖြင့် register လုပ်ပါ။
```python
model_name = best_run.properties['model_name']
script_file_name = 'inference/score.py'
best_run.download_file('outputs/scoring_file_v_1_0_0.py', 'inference/score.py')
description = "aml heart failure project sdk"
model = best_run.register_model(model_name = model_name,
                                model_path = './outputs/',
                                description = description,
                                tags = None)
```
### 3.2 မော်ဒယ်တင်သွင်းခြင်း

အကောင်းဆုံးမော်ဒယ်ကိုသိမ်းဆည်းပြီးပါက [InferenceConfig](https://docs.microsoft.com/python/api/azureml-core/azureml.core.model.inferenceconfig?view=azure-ml-py?ocid=AID3041109) class ကိုအသုံးပြု၍ deploy လုပ်နိုင်သည်။ InferenceConfig သည် deployment အတွက် custom environment settings ကိုကိုယ်စားပြုသည်။ [AciWebservice](https://docs.microsoft.com/python/api/azureml-core/azureml.core.webservice.aciwebservice?view=azure-ml-py) class သည် Azure Container Instances တွင် web service endpoint အဖြစ် deploy လုပ်ထားသော machine learning model ကိုကိုယ်စားပြုသည်။ Deploy လုပ်ထားသော service သည် load-balanced HTTP endpoint ဖြစ်ပြီး REST API ပါဝင်သည်။ API သို့ data ပေးပို့ပြီး မော်ဒယ်မှ prediction ကိုပြန်လည်ရယူနိုင်သည်။

မော်ဒယ်ကို [deploy](https://docs.microsoft.com/python/api/azureml-core/azureml.core.model(class)?view=azure-ml-py#deploy-workspace--name--models--inference-config-none--deployment-config-none--deployment-target-none--overwrite-false--show-output-false-?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) method ဖြင့် deploy လုပ်ပါ။

```python
from azureml.core.model import InferenceConfig, Model
from azureml.core.webservice import AciWebservice

inference_config = InferenceConfig(entry_script=script_file_name, environment=best_run.get_environment())

aciconfig = AciWebservice.deploy_configuration(cpu_cores = 1,
                                               memory_gb = 1,
                                               tags = {'type': "automl-heart-failure-prediction"},
                                               description = 'Sample service for AutoML Heart Failure Prediction')

aci_service_name = 'automl-hf-sdk'
aci_service = Model.deploy(ws, aci_service_name, [model], inference_config, aciconfig)
aci_service.wait_for_deployment(True)
print(aci_service.state)
```
ဒီအဆင့်သည်မိနစ်အနည်းငယ်ကြာနိုင်သည်။

### 3.3 Endpoint အသုံးပြုခြင်း

Endpoint ကိုအသုံးပြုရန် sample input တစ်ခုဖန်တီးပါ:

```python
data = {
    "data":
    [
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

test_sample = str.encode(json.dumps(data))
```
ပြီးနောက် input ကိုမော်ဒယ်သို့ပေးပို့၍ prediction ရယူနိုင်သည်:
```python
response = aci_service.run(input_data=test_sample)
response
```  
ဤအရာသည် `'{"result": [false]}'` ကို output ပြုလုပ်သင့်သည်။ ၎င်းသည် ကျွန်ုပ်တို့ endpoint သို့ ပေးပို့ခဲ့သော လူနာ input မှ `false` ဟုခန့်မှန်းချက်ကို ထုတ်လုပ်ခဲ့သည်ကို ဆိုလိုသည်။ ၎င်းသည် ဤပုဂ္ဂိုလ်သည် နှလုံးရောဂါဖြစ်နိုင်ခြေမရှိကြောင်းကို အဓိပ္ပါယ်ရသည်။

ဂုဏ်ယူပါတယ်! Azure ML SDK ကို အသုံးပြု၍ Azure ML တွင် train လုပ်ပြီး deploy လုပ်ထားသော model ကို သင်အသုံးပြုနိုင်ခဲ့ပါပြီ!

> **_NOTE:_** သင်၏ project ကို ပြီးဆုံးသောအခါတွင် resource အားလုံးကို မမေ့ပါနှင့် delete လုပ်ပါ။

## 🚀 စိန်ခေါ်မှု

SDK မှတဆင့် ပြုလုပ်နိုင်သော အခြားအရာများစွာရှိပါသေးသည်။ သို့သော် အကောင်းတစ်ခုကတော့ ဤသင်ခန်းစာတွင် အားလုံးကို မဖော်ပြနိုင်သော်လည်း SDK documentation ကို လေ့လာသင်ယူခြင်းဖြင့် သင်ကိုယ်တိုင်အတွက် အတော်လေးအထောက်အကူဖြစ်စေမည်ဖြစ်သည်။ Azure ML SDK documentation ကို ကြည့်ပြီး `Pipeline` class ကို ရှာဖွေပါ။ Pipeline သည် workflow အနေဖြင့် အဆင့်ဆင့်အလုပ်များကို စနစ်တကျ အကောင်အထည်ဖော်နိုင်သော collection ဖြစ်သည်။

**HINT:** [SDK documentation](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) သို့ သွားပြီး "Pipeline" ကဲ့သို့သော keyword များကို ရှာဖွေပါ။ `azureml.pipeline.core.Pipeline` class ကို ရလဒ်များတွင် တွေ့ရမည်ဖြစ်သည်။

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/37)

## ပြန်လည်သုံးသပ်ခြင်းနှင့် ကိုယ်တိုင်လေ့လာခြင်း

ဤသင်ခန်းစာတွင် သင်သည် Azure ML SDK ကို cloud တွင် အသုံးပြု၍ နှလုံးရောဂါဖြစ်နိုင်ခြေကို ခန့်မှန်းရန် model ကို train လုပ်ခြင်း၊ deploy လုပ်ခြင်းနှင့် အသုံးပြုခြင်းကို သင်ယူခဲ့ပါသည်။ Azure ML SDK အကြောင်း အခြားသော အချက်အလက်များကို သိရှိရန် [documentation](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) ကို ကြည့်ပါ။ Azure ML SDK ကို အသုံးပြု၍ သင်၏ကိုယ်ပိုင် model ကို ဖန်တီးကြည့်ပါ။

## လုပ်ငန်းတာဝန်

[Azure ML SDK ကို အသုံးပြုသော Data Science project](assignment.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါရှိနိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။