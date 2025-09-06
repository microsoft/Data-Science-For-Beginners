<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "472d3fab1c5be50f387336e7a686dbe1",
  "translation_date": "2025-09-06T07:41:42+00:00",
  "source_file": "5-Data-Science-In-Cloud/19-Azure/README.md",
  "language_code": "ne"
}
-->
# क्लाउडमा डेटा साइन्स: "Azure ML SDK" बाट 

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/19-DataScience-Cloud.png)|
|:---:|
| क्लाउडमा डेटा साइन्स: Azure ML SDK - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

सामग्री सूची:

- [क्लाउडमा डेटा साइन्स: "Azure ML SDK" बाट](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [पाठ अघि क्विज](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [१. परिचय](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [१.१ Azure ML SDK के हो?](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [१.२ हृदय विफलता भविष्यवाणी परियोजना र डाटासेटको परिचय](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [२. Azure ML SDK प्रयोग गरेर मोडेल प्रशिक्षण](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [२.१ Azure ML कार्यक्षेत्र सिर्जना गर्नुहोस्](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [२.२ कम्प्युट इन्स्ट्यान्स सिर्जना गर्नुहोस्](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [२.३ डाटासेट लोड गर्दै](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [२.४ नोटबुकहरू सिर्जना गर्दै](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [२.५ मोडेल प्रशिक्षण](../../../../5-Data-Science-In-Cloud/19-Azure)
      - [२.५.१ कार्यक्षेत्र, प्रयोग, कम्प्युट क्लस्टर र डाटासेट सेटअप गर्नुहोस्](../../../../5-Data-Science-In-Cloud/19-Azure)
      - [२.५.२ AutoML कन्फिगरेसन र प्रशिक्षण](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [३. Azure ML SDK प्रयोग गरेर मोडेल परिनियोजन र अन्तबिन्दु उपभोग](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [३.१ उत्कृष्ट मोडेल सुरक्षित गर्नुहोस्](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [३.२ मोडेल परिनियोजन](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [३.३ अन्तबिन्दु उपभोग](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [🚀 चुनौती](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [पाठपछि क्विज](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [समीक्षा र आत्म अध्ययन](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [कार्य](../../../../5-Data-Science-In-Cloud/19-Azure)

## [पाठ अघि क्विज](https://ff-quizzes.netlify.app/en/ds/quiz/36)

## १. परिचय

### १.१ Azure ML SDK के हो?

डेटा वैज्ञानिक र एआई विकासकर्ताहरूले Azure Machine Learning SDK प्रयोग गरेर Azure Machine Learning सेवासँग मेसिन लर्निङ वर्कफ्लो निर्माण र सञ्चालन गर्छन्। तपाईंले यो सेवा कुनै पनि Python वातावरणमा, जस्तै Jupyter Notebooks, Visual Studio Code, वा तपाईंको मनपर्ने Python IDE मा प्रयोग गर्न सक्नुहुन्छ।

SDK का मुख्य क्षेत्रहरू:

- मेसिन लर्निङ प्रयोगहरूमा प्रयोग गरिने डाटासेटहरूको जीवनचक्र अन्वेषण, तयारी र व्यवस्थापन गर्नुहोस्।
- मेसिन लर्निङ प्रयोगहरूको अनुगमन, लगिङ, र व्यवस्थापनका लागि क्लाउड स्रोतहरू व्यवस्थापन गर्नुहोस्।
- मोडेलहरूलाई स्थानीय रूपमा वा GPU-प्रेरित प्रशिक्षण सहित क्लाउड स्रोतहरू प्रयोग गरेर प्रशिक्षण गर्नुहोस्।
- स्वचालित मेसिन लर्निङ प्रयोग गर्नुहोस्, जसले कन्फिगरेसन प्यारामिटरहरू र प्रशिक्षण डाटा स्वीकार्छ। यसले भविष्यवाणीहरू चलाउनका लागि उत्तम मोडेल फेला पार्न एल्गोरिदम र हाइपरप्यारामिटर सेटिङहरूमा स्वचालित रूपमा पुनरावृत्ति गर्दछ।
- वेब सेवाहरू परिनियोजन गर्नुहोस् जसले तपाईंको प्रशिक्षित मोडेलहरूलाई कुनै पनि अनुप्रयोगमा उपभोग गर्न सकिने RESTful सेवाहरूमा रूपान्तरण गर्दछ।

[Azure Machine Learning SDK को बारेमा थप जान्नुहोस्](https://docs.microsoft.com/python/api/overview/azure/ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

[अघिल्लो पाठ](../18-Low-Code/README.md) मा, हामीले कसरी कम कोड/नो कोड तरिकामा मोडेल प्रशिक्षण, परिनियोजन र उपभोग गर्ने देख्यौं। हामीले हृदय विफलता डाटासेट प्रयोग गरेर हृदय विफलता भविष्यवाणी मोडेल निर्माण गरेका थियौं। यस पाठमा, हामी ठ्याक्कै त्यही कुरा गर्नेछौं तर Azure Machine Learning SDK प्रयोग गरेर।

![project-schema](../../../../5-Data-Science-In-Cloud/19-Azure/images/project-schema.PNG)

### १.२ हृदय विफलता भविष्यवाणी परियोजना र डाटासेटको परिचय

[यहाँ](../18-Low-Code/README.md) हृदय विफलता भविष्यवाणी परियोजना र डाटासेटको परिचय हेर्नुहोस्।

## २. Azure ML SDK प्रयोग गरेर मोडेल प्रशिक्षण
### २.१ Azure ML कार्यक्षेत्र सिर्जना गर्नुहोस्

सरलताका लागि, हामी जुपिटर नोटबुकमा काम गर्नेछौं। यसको मतलब तपाईंले पहिले नै कार्यक्षेत्र र कम्प्युट इन्स्ट्यान्स बनाइसक्नुभएको छ। यदि तपाईंले पहिले नै कार्यक्षेत्र बनाइसक्नुभएको छ भने, तपाईं सिधै खण्ड २.३ नोटबुक सिर्जना गर्न जान सक्नुहुन्छ।

यदि छैन भने, कृपया [अघिल्लो पाठ](../18-Low-Code/README.md) को खण्ड **२.१ Azure ML कार्यक्षेत्र सिर्जना गर्नुहोस्** मा दिइएका निर्देशनहरू पालना गर्नुहोस्।

### २.२ कम्प्युट इन्स्ट्यान्स सिर्जना गर्नुहोस्

हामीले पहिले बनाएको [Azure ML कार्यक्षेत्र](https://ml.azure.com/) मा जानुहोस्, कम्प्युट मेनुमा जानुहोस् र तपाईंले उपलब्ध विभिन्न कम्प्युट स्रोतहरू देख्नुहुनेछ।

![compute-instance-1](../../../../5-Data-Science-In-Cloud/19-Azure/images/compute-instance-1.PNG)

जुपिटर नोटबुकको लागि कम्प्युट इन्स्ट्यान्स सिर्जना गरौं। 
1. + New बटनमा क्लिक गर्नुहोस्। 
2. तपाईंको कम्प्युट इन्स्ट्यान्सलाई नाम दिनुहोस्।
3. तपाईंको विकल्पहरू चयन गर्नुहोस्: CPU वा GPU, VM साइज र कोर संख्या।
4. Create बटनमा क्लिक गर्नुहोस्।

बधाई छ, तपाईंले कम्प्युट इन्स्ट्यान्स सिर्जना गर्नुभयो! हामी यो कम्प्युट इन्स्ट्यान्सलाई [नोटबुक सिर्जना गर्ने खण्ड](../../../../5-Data-Science-In-Cloud/19-Azure) मा प्रयोग गर्नेछौं।

### २.३ डाटासेट लोड गर्दै
यदि तपाईंले अझै डाटासेट अपलोड गर्नुभएको छैन भने, [अघिल्लो पाठ](../18-Low-Code/README.md) को खण्ड **२.३ डाटासेट लोड गर्दै** हेर्नुहोस्।

### २.४ नोटबुकहरू सिर्जना गर्दै

> **_NOTE:_** अर्को चरणका लागि तपाईं नयाँ नोटबुक खालि बाट सिर्जना गर्न सक्नुहुन्छ, वा तपाईंले [हामीले बनाएको नोटबुक](../../../../5-Data-Science-In-Cloud/19-Azure/notebook.ipynb) Azure ML स्टुडियोमा अपलोड गर्न सक्नुहुन्छ। अपलोड गर्न, "Notebook" मेनुमा क्लिक गर्नुहोस् र नोटबुक अपलोड गर्नुहोस्।

नोटबुकहरू डेटा साइन्स प्रक्रियाको एकदम महत्त्वपूर्ण हिस्सा हुन्। तिनीहरूलाई अन्वेषणात्मक डेटा विश्लेषण (EDA) गर्न, कम्प्युटर क्लस्टरलाई मोडेल प्रशिक्षण गर्न बोलाउन, वा अन्तबिन्दु परिनियोजन गर्न प्रयोग गर्न सकिन्छ।

नोटबुक सिर्जना गर्न, हामीलाई जुपिटर नोटबुक इन्स्ट्यान्स चलाइरहेको कम्प्युट नोड चाहिन्छ। [Azure ML कार्यक्षेत्र](https://ml.azure.com/) मा फर्कनुहोस् र कम्प्युट इन्स्ट्यान्सहरूमा क्लिक गर्नुहोस्। कम्प्युट इन्स्ट्यान्सहरूको सूचीमा तपाईंले [पहिले सिर्जना गरिएको कम्प्युट इन्स्ट्यान्स](../../../../5-Data-Science-In-Cloud/19-Azure) देख्नुहुनेछ। 

1. Applications खण्डमा, Jupyter विकल्पमा क्लिक गर्नुहोस्। 
2. "Yes, I understand" बक्समा टिक गर्नुहोस् र Continue बटनमा क्लिक गर्नुहोस्।
![notebook-1](../../../../5-Data-Science-In-Cloud/19-Azure/images/notebook-1.PNG)
3. यसले तपाईंको ब्राउजरमा नयाँ ट्याब खोल्छ जसमा तपाईंको जुपिटर नोटबुक इन्स्ट्यान्स देखिन्छ। नयाँ नोटबुक सिर्जना गर्न "New" बटनमा क्लिक गर्नुहोस्।

![notebook-2](../../../../5-Data-Science-In-Cloud/19-Azure/images/notebook-2.PNG)

अब हामीसँग नोटबुक छ, हामी Azure ML SDK प्रयोग गरेर मोडेल प्रशिक्षण सुरु गर्न सक्छौं।

### २.५ मोडेल प्रशिक्षण

सबैभन्दा पहिले, यदि तपाईंलाई कहिल्यै शंका लाग्छ भने, [Azure ML SDK डकुमेन्टेसन](https://docs.microsoft.com/python/api/overview/azure/ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) हेर्नुहोस्। यसमा हामीले यस पाठमा हेर्ने मोड्युलहरू बुझ्न आवश्यक पर्ने सबै जानकारी समावेश छ।

#### २.५.१ कार्यक्षेत्र, प्रयोग, कम्प्युट क्लस्टर र डाटासेट सेटअप गर्नुहोस्

तपाईंले निम्न कोड प्रयोग गरेर कन्फिगरेसन फाइलबाट `workspace` लोड गर्न आवश्यक छ:

```python
from azureml.core import Workspace
ws = Workspace.from_config()
```

यसले `Workspace` प्रकारको वस्तु फिर्ता गर्छ, जसले कार्यक्षेत्रलाई प्रतिनिधित्व गर्छ। त्यसपछि तपाईंले निम्न कोड प्रयोग गरेर `experiment` सिर्जना गर्न आवश्यक छ:

```python
from azureml.core import Experiment
experiment_name = 'aml-experiment'
experiment = Experiment(ws, experiment_name)
```
कार्यक्षेत्रबाट प्रयोग प्राप्त गर्न वा सिर्जना गर्न, तपाईंले प्रयोगको नाम अनुरोध गर्नुहुन्छ। प्रयोगको नाम ३-३६ वर्णको हुनुपर्छ, अक्षर वा नम्बरबाट सुरु हुनुपर्छ, र केवल अक्षर, नम्बर, अन्डरस्कोर, र ड्यासहरू समावेश गर्न सक्छ। यदि कार्यक्षेत्रमा प्रयोग फेला परेन भने, नयाँ प्रयोग सिर्जना गरिन्छ।

अब तपाईंले निम्न कोड प्रयोग गरेर प्रशिक्षणका लागि कम्प्युट क्लस्टर सिर्जना गर्न आवश्यक छ। ध्यान दिनुहोस्, यो चरणमा केही मिनेट लाग्न सक्छ। 

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

तपाईंले कार्यक्षेत्रबाट डाटासेट नाम प्रयोग गरेर डाटासेट प्राप्त गर्न सक्नुहुन्छ:

```python
dataset = ws.datasets['heart-failure-records']
df = dataset.to_pandas_dataframe()
df.describe()
```
#### २.५.२ AutoML कन्फिगरेसन र प्रशिक्षण

AutoML कन्फिगरेसन सेट गर्न, [AutoMLConfig कक्षा](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.automlconfig(class)?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) प्रयोग गर्नुहोस्।

डकुमेन्टेसनमा वर्णन गरिएझैं, तपाईंले खेल्न सक्ने धेरै प्यारामिटरहरू छन्। यस परियोजनाका लागि, हामी निम्न प्यारामिटरहरू प्रयोग गर्नेछौं:

- `experiment_timeout_minutes`: प्रयोगलाई स्वचालित रूपमा रोक्न र परिणामहरू उपलब्ध गराउन अनुमति दिइएको अधिकतम समय (मिनेटमा)।
- `max_concurrent_iterations`: प्रयोगका लागि अनुमति दिइएको अधिकतम समवर्ती प्रशिक्षण पुनरावृत्तिहरू।
- `primary_metric`: प्रयोगको स्थिति निर्धारण गर्न प्रयोग गरिएको प्राथमिक मेट्रिक।
- `compute_target`: स्वचालित मेसिन लर्निङ प्रयोग चलाउन प्रयोग गरिएको Azure Machine Learning कम्प्युट लक्ष्य।
- `task`: चलाउनुपर्ने कार्यको प्रकार। मानहरू 'classification', 'regression', वा 'forecasting' हुन सक्छ।
- `training_data`: प्रयोग भित्र प्रयोग गर्नुपर्ने प्रशिक्षण डाटा। यसमा प्रशिक्षण सुविधाहरू र लेबल स्तम्भ (वैकल्पिक रूपमा नमूना तौल स्तम्भ) समावेश हुनुपर्छ।
- `label_column_name`: लेबल स्तम्भको नाम।
- `path`: Azure Machine Learning परियोजना फोल्डरको पूर्ण पथ।
- `enable_early_stopping`: छोटो अवधिमा स्कोर सुधार नभएमा प्रारम्भिक समाप्ति सक्षम गर्ने कि नगर्ने।
- `featurization`: स्वतः सुविधाकरण चरण गर्नुपर्ने कि नगर्ने, वा अनुकूलित सुविधाकरण प्रयोग गर्ने।
- `debug_log`: डिबग जानकारी लेख्न फाइल लग गर्नुहोस्।

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
अब तपाईंको कन्फिगरेसन सेट भयो, तपाईंले निम्न कोड प्रयोग गरेर मोडेल प्रशिक्षण गर्न सक्नुहुन्छ। यो चरणमा तपाईंको क्लस्टर साइजमा निर्भर गर्दै एक घण्टासम्म लाग्न सक्छ।

```python
remote_run = experiment.submit(automl_config)
```
तपाईंले RunDetails विजेट चलाएर विभिन्न प्रयोगहरू देखाउन सक्नुहुन्छ।
```python
from azureml.widgets import RunDetails
RunDetails(remote_run).show()
```
## ३. Azure ML SDK प्रयोग गरेर मोडेल परिनियोजन र अन्तबिन्दु उपभोग

### ३.१ उत्कृष्ट मोडेल सुरक्षित गर्नुहोस्

`remote_run` [AutoMLRun](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.run.automlrun?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) प्रकारको वस्तु हो। यस वस्तुमा `get_output()` विधि हुन्छ, जसले उत्कृष्ट रन र सम्बन्धित फिट गरिएको मोडेल फिर्ता गर्छ।

```python
best_run, fitted_model = remote_run.get_output()
```
तपाईंले उत्कृष्ट मोडेलका लागि प्रयोग गरिएका प्यारामिटरहरू केवल फिट गरिएको मोडेल प्रिन्ट गरेर हेर्न सक्नुहुन्छ र [get_properties()](https://docs.microsoft.com/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py#azureml_core_Run_get_properties?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) विधि प्रयोग गरेर उत्कृष्ट मोडेलका गुणहरू हेर्न सक्नुहुन्छ।

```python
best_run.get_properties()
```

अब [register_model](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.run.automlrun?view=azure-ml-py#register-model-model-name-none--description-none--tags-none--iteration-none--metric-none-?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) विधि प्रयोग गरेर मोडेल दर्ता गर्नुहोस्।
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
### ३.२ मोडेल परिनियोजन

एकपटक उत्कृष्ट मोडेल सुरक्षित भएपछि, हामी यसलाई [InferenceConfig](https://docs.microsoft.com/python/api/azureml-core/azureml.core.model.inferenceconfig?view=azure-ml-py?ocid=AID3041109) कक्षा प्रयोग गरेर परिनियोजन गर्न सक्छौं। InferenceConfig परिनियोजनका लागि प्रयोग गरिने अनुकूल वातावरणका कन्फिगरेसन सेटिङहरू प्रतिनिधित्व गर्दछ। [AciWebservice](https://docs.microsoft.com/python/api/azureml-core/azureml.core.webservice.aciwebservice?view=azure-ml-py) कक्षाले Azure Container Instances मा वेब सेवा अन्तबिन्दुका रूपमा परिनियोजित मेसिन लर्निङ मोडेललाई प्रतिनिधित्व गर्दछ। परिनियोजित सेवाले मोडेल, स्क्रिप्ट, र सम्बन्धित फाइलहरूबाट सिर्जना गरिएको हो। परिणामस्वरूप वेब सेवा लोड-ब्यालेन्स गरिएको, HTTP अन्तबिन्दु हो जसमा REST API हुन्छ। तपाईंले यस API मा डाटा पठाउन सक्नुहुन्छ र मोडेलले फिर्ता गरेको भविष्यवाणी प्राप्त गर्न सक्नुहुन्छ।

मोडेल [deploy](https://docs.microsoft.com/python/api/azureml-core/azureml.core.model(class)?view=azure-ml-py#deploy-workspace--name--models--inference-config-none--deployment-config-none--deployment-target-none--overwrite-false--show-output-false-?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) विधि प्रयोग गरेर परिनियोजित गरिन्छ।

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
यो चरणमा केही मिनेट लाग्न सक्छ।

### ३.३ अन्तबिन्दु उपभोग

तपाईंको अन्तबिन्दु उपभोग गर्न, नमूना इनपुट सिर्जना गर्नुहोस्:

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
र त्यसपछि तपाईंले यो इनपुटलाई भविष्यवाणीका लागि आफ्नो मोडेलमा पठाउन सक्नुहुन्छ:
```python
response = aci_service.run(input_data=test_sample)
response
```
यसले `'{"result": [false]}'` आउटपुट दिनुपर्छ। यसको अर्थ, हामीले एन्डपोइन्टमा पठाएको बिरामीको इनपुटले `false` भविष्यवाणी उत्पन्न गर्‍यो, जसको अर्थ यो व्यक्तिलाई हृदयघात हुने सम्भावना छैन।

बधाई छ! तपाईंले Azure ML मा तैनाथ र प्रशिक्षित गरिएको मोडेललाई Azure ML SDK प्रयोग गरेर उपभोग गर्नुभयो!

> **_NOTE:_** परियोजना समाप्त भएपछि, सबै स्रोतहरू मेटाउन नबिर्सनुहोस्।

## 🚀 चुनौती

SDK मार्फत गर्न सकिने धेरै अन्य कार्यहरू छन्, तर दुर्भाग्यवश, हामी यस पाठमा तिनीहरू सबै हेर्न सक्दैनौं। तर राम्रो खबर, SDK डकुमेन्टेसनलाई कसरी छिटो हेर्ने सिक्नाले तपाईंलाई धेरै टाढा लैजान सक्छ। Azure ML SDK डकुमेन्टेसन हेर्नुहोस् र `Pipeline` क्लास खोज्नुहोस्, जसले तपाईंलाई पाइपलाइनहरू बनाउन अनुमति दिन्छ। पाइपलाइन भनेको चरणहरूको संग्रह हो, जसलाई वर्कफ्लोको रूपमा कार्यान्वयन गर्न सकिन्छ।

**सुझाव:** [SDK डकुमेन्टेसन](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) मा जानुहोस् र "Pipeline" जस्ता कुञ्जीशब्दहरू खोजी बारमा टाइप गर्नुहोस्। तपाईंले खोज परिणामहरूमा `azureml.pipeline.core.Pipeline` क्लास पाउनुहुनेछ।

## [पाठपछिको क्विज](https://ff-quizzes.netlify.app/en/ds/quiz/37)

## समीक्षा र आत्म-अध्ययन

यस पाठमा, तपाईंले Azure ML SDK प्रयोग गरेर क्लाउडमा हृदयघातको जोखिम भविष्यवाणी गर्न मोडेललाई कसरी प्रशिक्षण, तैनाथ र उपभोग गर्ने सिक्नुभयो। Azure ML SDK सम्बन्धी थप जानकारीका लागि यो [डकुमेन्टेसन](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) हेर्नुहोस्। Azure ML SDK प्रयोग गरेर आफ्नो मोडेल बनाउन प्रयास गर्नुहोस्।

## असाइनमेन्ट

[Azure ML SDK प्रयोग गरेर डेटा साइन्स परियोजना](assignment.md)

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।