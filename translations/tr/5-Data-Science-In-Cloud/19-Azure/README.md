<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "472d3fab1c5be50f387336e7a686dbe1",
  "translation_date": "2025-09-06T08:55:23+00:00",
  "source_file": "5-Data-Science-In-Cloud/19-Azure/README.md",
  "language_code": "tr"
}
-->
# Bulutta Veri Bilimi: "Azure ML SDK" Yöntemi

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/19-DataScience-Cloud.png)|
|:---:|
| Bulutta Veri Bilimi: Azure ML SDK - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

İçindekiler:

- [Bulutta Veri Bilimi: "Azure ML SDK" Yöntemi](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Ders Öncesi Test](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [1. Giriş](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [1.1 Azure ML SDK Nedir?](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [1.2 Kalp yetmezliği tahmin projesi ve veri seti tanıtımı](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [2. Azure ML SDK ile Model Eğitimi](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.1 Azure ML çalışma alanı oluşturma](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.2 Hesaplama örneği oluşturma](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.3 Veri Setini Yükleme](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.4 Not Defteri Oluşturma](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.5 Model Eğitimi](../../../../5-Data-Science-In-Cloud/19-Azure)
      - [2.5.1 Çalışma alanı, deney, hesaplama kümesi ve veri seti ayarları](../../../../5-Data-Science-In-Cloud/19-Azure)
      - [2.5.2 AutoML Yapılandırması ve Eğitim](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [3. Azure ML SDK ile Model Dağıtımı ve Uç Nokta Tüketimi](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.1 En iyi modeli kaydetme](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.2 Model Dağıtımı](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.3 Uç nokta tüketimi](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [🚀 Meydan Okuma](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Ders Sonrası Test](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Gözden Geçirme ve Kendi Kendine Çalışma](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Ödev](../../../../5-Data-Science-In-Cloud/19-Azure)

## [Ders Öncesi Test](https://ff-quizzes.netlify.app/en/ds/quiz/36)

## 1. Giriş

### 1.1 Azure ML SDK Nedir?

Veri bilimciler ve yapay zeka geliştiricileri, Azure Machine Learning SDK'sını kullanarak Azure Machine Learning hizmeti ile makine öğrenimi iş akışları oluşturur ve çalıştırır. Bu hizmetle Jupyter Notebooks, Visual Studio Code veya tercih ettiğiniz Python IDE gibi herhangi bir Python ortamında etkileşim kurabilirsiniz.

SDK'nın temel alanları şunlardır:

- Makine öğrenimi deneylerinde kullanılan veri setlerinin yaşam döngüsünü keşfetmek, hazırlamak ve yönetmek.
- Makine öğrenimi deneylerinizi izlemek, günlük kaydı yapmak ve düzenlemek için bulut kaynaklarını yönetmek.
- Modelleri yerel olarak veya GPU hızlandırmalı model eğitimi dahil bulut kaynaklarını kullanarak eğitmek.
- Yapılandırma parametrelerini ve eğitim verilerini kabul eden otomatik makine öğrenimini kullanmak. Algoritmalar ve hiperparametre ayarları arasında otomatik olarak iterasyon yaparak tahminler için en iyi modeli bulur.
- Eğitilmiş modellerinizi RESTful hizmetlere dönüştürerek herhangi bir uygulamada tüketilebilecek web hizmetleri olarak dağıtmak.

[Azure Machine Learning SDK hakkında daha fazla bilgi edinin](https://docs.microsoft.com/python/api/overview/azure/ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

[Önceki derste](../18-Low-Code/README.md), düşük kodlu/yok kodlu bir yaklaşımla bir modeli nasıl eğiteceğimizi, dağıtacağımızı ve tüketeceğimizi gördük. Kalp Yetmezliği veri setini kullanarak bir kalp yetmezliği tahmin modeli oluşturduk. Bu derste, aynı işlemi Azure Machine Learning SDK kullanarak yapacağız.

![proje şeması](../../../../5-Data-Science-In-Cloud/19-Azure/images/project-schema.PNG)

### 1.2 Kalp yetmezliği tahmin projesi ve veri seti tanıtımı

Kalp yetmezliği tahmin projesi ve veri seti tanıtımı için [buraya](../18-Low-Code/README.md) göz atın.

## 2. Azure ML SDK ile Model Eğitimi
### 2.1 Azure ML çalışma alanı oluşturma

Basitlik açısından, bir Jupyter not defteri üzerinde çalışacağız. Bu, zaten bir Çalışma Alanı ve bir hesaplama örneğiniz olduğu anlamına gelir. Eğer zaten bir Çalışma Alanınız varsa, doğrudan **2.3 Not Defteri Oluşturma** bölümüne geçebilirsiniz.

Eğer yoksa, bir çalışma alanı oluşturmak için [önceki dersteki](../18-Low-Code/README.md) **2.1 Azure ML çalışma alanı oluşturma** bölümündeki talimatları takip edin.

### 2.2 Hesaplama örneği oluşturma

Daha önce oluşturduğumuz [Azure ML çalışma alanına](https://ml.azure.com/) gidin ve hesaplama menüsüne tıklayın. Burada mevcut hesaplama kaynaklarını göreceksiniz.

![hesaplama-örneği-1](../../../../5-Data-Science-In-Cloud/19-Azure/images/compute-instance-1.PNG)

Bir Jupyter not defteri sağlamak için bir hesaplama örneği oluşturalım. 
1. + Yeni düğmesine tıklayın. 
2. Hesaplama örneğinize bir ad verin.
3. Seçeneklerinizi belirleyin: CPU veya GPU, VM boyutu ve çekirdek sayısı.
4. Oluştur düğmesine tıklayın.

Tebrikler, bir hesaplama örneği oluşturdunuz! Bu hesaplama örneğini [Not Defteri Oluşturma bölümünde](../../../../5-Data-Science-In-Cloud/19-Azure) kullanacağız.

### 2.3 Veri Setini Yükleme
Eğer veri setini henüz yüklemediyseniz, [önceki dersteki](../18-Low-Code/README.md) **2.3 Veri Setini Yükleme** bölümüne bakın.

### 2.4 Not Defteri Oluşturma

> **_NOT:_** Bir sonraki adım için ya sıfırdan yeni bir not defteri oluşturabilir ya da [önceden oluşturduğumuz not defterini](../../../../5-Data-Science-In-Cloud/19-Azure/notebook.ipynb) Azure ML Studio'ya yükleyebilirsiniz. Yüklemek için, "Not Defteri" menüsüne tıklayın ve not defterini yükleyin.

Not defterleri, veri bilimi sürecinin çok önemli bir parçasıdır. Keşifsel Veri Analizi (EDA) yapmak, bir hesaplama kümesine model eğitimi çağrısı yapmak, bir tahmin kümesine uç nokta dağıtımı çağrısı yapmak için kullanılabilirler.

Bir not defteri oluşturmak için, Jupyter not defteri örneğini çalıştıran bir hesaplama düğümüne ihtiyacımız var. [Azure ML çalışma alanına](https://ml.azure.com/) geri dönün ve Hesaplama örneklerine tıklayın. Daha önce oluşturduğumuz [hesaplama örneğini](../../../../5-Data-Science-In-Cloud/19-Azure) listede görmelisiniz.

1. Uygulamalar bölümünde Jupyter seçeneğine tıklayın. 
2. "Evet, anladım" kutusunu işaretleyin ve Devam düğmesine tıklayın.
![not-defteri-1](../../../../5-Data-Science-In-Cloud/19-Azure/images/notebook-1.PNG)
3. Bu, Jupyter not defteri örneğinizle yeni bir tarayıcı sekmesi açmalıdır. "Yeni" düğmesine tıklayarak bir not defteri oluşturun.

![not-defteri-2](../../../../5-Data-Science-In-Cloud/19-Azure/images/notebook-2.PNG)

Artık bir not defterimiz olduğuna göre, Azure ML SDK ile modeli eğitmeye başlayabiliriz.

### 2.5 Model Eğitimi

Öncelikle, herhangi bir şüpheniz olduğunda [Azure ML SDK belgelerine](https://docs.microsoft.com/python/api/overview/azure/ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) başvurun. Bu belgeler, bu derste göreceğimiz modülleri anlamak için gerekli tüm bilgileri içerir.

#### 2.5.1 Çalışma alanı, deney, hesaplama kümesi ve veri seti ayarları

Aşağıdaki kodu kullanarak `workspace`'i yapılandırma dosyasından yüklemeniz gerekiyor:

```python
from azureml.core import Workspace
ws = Workspace.from_config()
```

Bu, çalışma alanını temsil eden `Workspace` türünde bir nesne döndürür. Ardından, aşağıdaki kodu kullanarak bir `deney` oluşturmanız gerekiyor:

```python
from azureml.core import Experiment
experiment_name = 'aml-experiment'
experiment = Experiment(ws, experiment_name)
```
Bir çalışma alanından deney almak veya oluşturmak için, deney adını kullanarak istekte bulunursunuz. Deney adı 3-36 karakter arasında olmalı, bir harf veya sayı ile başlamalı ve yalnızca harfler, sayılar, alt çizgiler ve tireler içermelidir. Çalışma alanında deney bulunmazsa, yeni bir deney oluşturulur.

Şimdi, aşağıdaki kodu kullanarak eğitim için bir hesaplama kümesi oluşturmanız gerekiyor. Bu adım birkaç dakika sürebilir.

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

Veri setini çalışma alanından veri seti adını kullanarak şu şekilde alabilirsiniz:

```python
dataset = ws.datasets['heart-failure-records']
df = dataset.to_pandas_dataframe()
df.describe()
```
#### 2.5.2 AutoML Yapılandırması ve Eğitim

AutoML yapılandırmasını ayarlamak için [AutoMLConfig sınıfını](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.automlconfig(class)?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) kullanın.

Belgelerde açıklandığı gibi, üzerinde oynayabileceğiniz birçok parametre bulunmaktadır. Bu proje için aşağıdaki parametreleri kullanacağız:

- `experiment_timeout_minutes`: Deneyin otomatik olarak durdurulmadan ve sonuçların otomatik olarak kullanılabilir hale getirilmeden önce çalışmasına izin verilen maksimum süre (dakika cinsinden).
- `max_concurrent_iterations`: Deney için izin verilen maksimum eş zamanlı eğitim iterasyonu sayısı.
- `primary_metric`: Deneyin durumunu belirlemek için kullanılan birincil metrik.
- `compute_target`: Otomatik Makine Öğrenimi deneyini çalıştırmak için kullanılan Azure Machine Learning hesaplama hedefi.
- `task`: Çalıştırılacak görev türü. Değerler 'classification', 'regression' veya 'forecasting' olabilir.
- `training_data`: Deneyde kullanılacak eğitim verileri. Hem eğitim özelliklerini hem de bir etiket sütununu (isteğe bağlı olarak bir örnek ağırlıkları sütunu) içermelidir.
- `label_column_name`: Etiket sütununun adı.
- `path`: Azure Machine Learning proje klasörünün tam yolu.
- `enable_early_stopping`: Kısa vadede skor iyileşmiyorsa erken sonlandırmayı etkinleştirip etkinleştirmeyeceğinizi belirtir.
- `featurization`: Özellik oluşturma adımının otomatik olarak mı yapılacağını, yoksa özelleştirilmiş bir özellik oluşturmanın mı kullanılacağını belirtir.
- `debug_log`: Hata ayıklama bilgilerini yazmak için kullanılan günlük dosyası.

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
Yapılandırmanızı ayarladıktan sonra, aşağıdaki kodu kullanarak modeli eğitebilirsiniz. Bu adım, küme boyutunuza bağlı olarak bir saate kadar sürebilir.

```python
remote_run = experiment.submit(automl_config)
```
Farklı deneyleri göstermek için RunDetails widget'ını çalıştırabilirsiniz.
```python
from azureml.widgets import RunDetails
RunDetails(remote_run).show()
```
## 3. Azure ML SDK ile Model Dağıtımı ve Uç Nokta Tüketimi

### 3.1 En iyi modeli kaydetme

`remote_run`, [AutoMLRun](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.run.automlrun?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) türünde bir nesnedir. Bu nesne, en iyi çalışmayı ve ilgili uyarlanmış modeli döndüren `get_output()` yöntemini içerir.

```python
best_run, fitted_model = remote_run.get_output()
```
En iyi model için kullanılan parametreleri sadece fitted_model'i yazdırarak görebilir ve en iyi modelin özelliklerini [get_properties()](https://docs.microsoft.com/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py#azureml_core_Run_get_properties?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) yöntemiyle inceleyebilirsiniz.

```python
best_run.get_properties()
```

Şimdi modeli [register_model](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.run.automlrun?view=azure-ml-py#register-model-model-name-none--description-none--tags-none--iteration-none--metric-none-?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) yöntemiyle kaydedin.
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
### 3.2 Model Dağıtımı

En iyi model kaydedildikten sonra, [InferenceConfig](https://docs.microsoft.com/python/api/azureml-core/azureml.core.model.inferenceconfig?view=azure-ml-py?ocid=AID3041109) sınıfını kullanarak modeli dağıtabilirsiniz. InferenceConfig, dağıtım için kullanılan özel bir ortamın yapılandırma ayarlarını temsil eder. [AciWebservice](https://docs.microsoft.com/python/api/azureml-core/azureml.core.webservice.aciwebservice?view=azure-ml-py) sınıfı, Azure Container Instances üzerinde bir web hizmeti uç noktası olarak dağıtılmış bir makine öğrenimi modelini temsil eder. Dağıtılmış bir hizmet, bir model, betik ve ilgili dosyalardan oluşturulur. Ortaya çıkan web hizmeti, bir yük dengeleyici, HTTP uç noktası ve bir REST API içerir. Bu API'ye veri gönderebilir ve model tarafından döndürülen tahmini alabilirsiniz.

Model, [deploy](https://docs.microsoft.com/python/api/azureml-core/azureml.core.model(class)?view=azure-ml-py#deploy-workspace--name--models--inference-config-none--deployment-config-none--deployment-target-none--overwrite-false--show-output-false-?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) yöntemiyle dağıtılır.

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
Bu adım birkaç dakika sürebilir.

### 3.3 Uç nokta tüketimi

Uç noktanızı bir örnek giriş oluşturarak tüketebilirsiniz:

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
Ve ardından bu girişi tahmin için modelinize gönderebilirsiniz:
```python
response = aci_service.run(input_data=test_sample)
response
```
Bu, `'{"result": [false]}'` çıktısını vermelidir. Bu, uç noktaya gönderdiğimiz hasta girdisinin `false` tahminini oluşturduğu anlamına gelir, yani bu kişinin kalp krizi geçirme olasılığı düşük.

Tebrikler! Azure ML SDK ile Azure ML üzerinde eğitilmiş ve dağıtılmış modeli başarıyla kullandınız!

> **_NOT:_** Projeyi tamamladıktan sonra tüm kaynakları silmeyi unutmayın.

## 🚀 Zorluk

SDK ile yapabileceğiniz birçok şey var, ne yazık ki bu ders kapsamında hepsini inceleyemiyoruz. Ama iyi haber, SDK dokümantasyonunu nasıl hızlıca gözden geçireceğinizi öğrenmek, kendi başınıza çok yol almanızı sağlayabilir. Azure ML SDK dokümantasyonuna göz atın ve size iş akışı olarak çalıştırılabilecek adımlar koleksiyonu oluşturmaya olanak tanıyan `Pipeline` sınıfını bulun.

**İPUCU:** [SDK dokümantasyonu](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) sayfasına gidin ve arama çubuğuna "Pipeline" gibi anahtar kelimeler yazın. Arama sonuçlarında `azureml.pipeline.core.Pipeline` sınıfını bulmalısınız.

## [Ders sonrası sınav](https://ff-quizzes.netlify.app/en/ds/quiz/37)

## Gözden Geçirme ve Kendi Kendine Çalışma

Bu derste, Azure ML SDK ile bulutta kalp yetmezliği riskini tahmin eden bir modeli nasıl eğiteceğinizi, dağıtacağınızı ve kullanacağınızı öğrendiniz. Azure ML SDK hakkında daha fazla bilgi için bu [dokümantasyona](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) göz atın. Azure ML SDK ile kendi modelinizi oluşturmaya çalışın.

## Ödev

[Azure ML SDK kullanarak Veri Bilimi projesi](assignment.md)

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.