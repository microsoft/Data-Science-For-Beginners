<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "472d3fab1c5be50f387336e7a686dbe1",
  "translation_date": "2025-09-05T19:50:49+00:00",
  "source_file": "5-Data-Science-In-Cloud/19-Azure/README.md",
  "language_code": "uk"
}
-->
# Наука про дані в хмарі: шлях "Azure ML SDK"

|![Скетчноут від [(@sketchthedocs)](https://sketchthedocs.dev)](../../sketchnotes/19-DataScience-Cloud.png)|
|:---:|
| Наука про дані в хмарі: Azure ML SDK - _Скетчноут від [@nitya](https://twitter.com/nitya)_ |

Зміст:

- [Наука про дані в хмарі: шлях "Azure ML SDK"](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Тест перед лекцією](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [1. Вступ](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [1.1 Що таке Azure ML SDK?](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [1.2 Проєкт прогнозування серцевої недостатності та введення до набору даних](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [2. Навчання моделі за допомогою Azure ML SDK](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.1 Створення робочого простору Azure ML](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.2 Створення обчислювального екземпляра](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.3 Завантаження набору даних](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.4 Створення блокнотів](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.5 Навчання моделі](../../../../5-Data-Science-In-Cloud/19-Azure)
      - [2.5.1 Налаштування робочого простору, експерименту, обчислювального кластеру та набору даних](../../../../5-Data-Science-In-Cloud/19-Azure)
      - [2.5.2 Конфігурація AutoML та навчання](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [3. Розгортання моделі та використання кінцевої точки за допомогою Azure ML SDK](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.1 Збереження найкращої моделі](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.2 Розгортання моделі](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.3 Використання кінцевої точки](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [🚀 Виклик](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Тест після лекції](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Огляд та самостійне навчання](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Завдання](../../../../5-Data-Science-In-Cloud/19-Azure)

## [Тест перед лекцією](https://ff-quizzes.netlify.app/en/ds/quiz/36)

## 1. Вступ

### 1.1 Що таке Azure ML SDK?

Науковці з даних та розробники штучного інтелекту використовують Azure Machine Learning SDK для створення та виконання робочих процесів машинного навчання за допомогою сервісу Azure Machine Learning. Ви можете взаємодіяти із сервісом у будь-якому середовищі Python, включаючи Jupyter Notebooks, Visual Studio Code або ваш улюблений IDE для Python.

Основні можливості SDK включають:

- Дослідження, підготовка та управління життєвим циклом наборів даних, які використовуються в експериментах машинного навчання.
- Управління хмарними ресурсами для моніторингу, ведення журналів та організації експериментів машинного навчання.
- Навчання моделей локально або за допомогою хмарних ресурсів, включаючи навчання моделей із прискоренням GPU.
- Використання автоматизованого машинного навчання, яке приймає параметри конфігурації та навчальні дані. Воно автоматично перебирає алгоритми та налаштування гіперпараметрів, щоб знайти найкращу модель для прогнозування.
- Розгортання вебсервісів для перетворення ваших навчальних моделей у RESTful сервіси, які можна використовувати в будь-якому додатку.

[Дізнайтеся більше про Azure Machine Learning SDK](https://docs.microsoft.com/python/api/overview/azure/ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

У [попередньому уроці](../18-Low-Code/README.md) ми розглянули, як навчати, розгортати та використовувати модель у форматі Low code/No code. Ми використовували набір даних про серцеву недостатність для створення моделі прогнозування серцевої недостатності. У цьому уроці ми зробимо те саме, але використовуючи Azure Machine Learning SDK.

![схема-проєкту](../../../../5-Data-Science-In-Cloud/19-Azure/images/project-schema.PNG)

### 1.2 Проєкт прогнозування серцевої недостатності та введення до набору даних

Перегляньте [тут](../18-Low-Code/README.md) введення до проєкту прогнозування серцевої недостатності та набору даних.

## 2. Навчання моделі за допомогою Azure ML SDK

### 2.1 Створення робочого простору Azure ML

Для простоти ми будемо працювати в блокноті Jupyter. Це означає, що у вас вже є робочий простір і обчислювальний екземпляр. Якщо у вас вже є робочий простір, ви можете перейти безпосередньо до розділу 2.3 Створення блокнотів.

Якщо ні, будь ласка, дотримуйтесь інструкцій у розділі **2.1 Створення робочого простору Azure ML** у [попередньому уроці](../18-Low-Code/README.md), щоб створити робочий простір.

### 2.2 Створення обчислювального екземпляра

У [робочому просторі Azure ML](https://ml.azure.com/), який ми створили раніше, перейдіть до меню обчислень, і ви побачите різні доступні обчислювальні ресурси.

![compute-instance-1](../../../../5-Data-Science-In-Cloud/19-Azure/images/compute-instance-1.PNG)

Давайте створимо обчислювальний екземпляр для розгортання блокнота Jupyter.  
1. Натисніть кнопку + New.  
2. Дайте ім'я вашому обчислювальному екземпляру.  
3. Виберіть параметри: CPU або GPU, розмір VM та кількість ядер.  
4. Натисніть кнопку Create.  

Вітаємо, ви щойно створили обчислювальний екземпляр! Ми будемо використовувати цей екземпляр для створення блокнота в розділі [Створення блокнотів](../../../../5-Data-Science-In-Cloud/19-Azure).

### 2.3 Завантаження набору даних

Якщо ви ще не завантажили набір даних, зверніться до розділу **2.3 Завантаження набору даних** у [попередньому уроці](../18-Low-Code/README.md).

### 2.4 Створення блокнотів

> **_NOTE:_** Для наступного кроку ви можете створити новий блокнот з нуля або завантажити [блокнот, який ми створили](../../../../5-Data-Science-In-Cloud/19-Azure/notebook.ipynb), у вашому Azure ML Studio. Щоб завантажити його, просто натисніть на меню "Notebook" і завантажте блокнот.

Блокноти є дуже важливою частиною процесу науки про дані. Їх можна використовувати для проведення дослідження даних (EDA), виклику обчислювального кластеру для навчання моделі, виклику кластеру для розгортання кінцевої точки.

Щоб створити блокнот, нам потрібен обчислювальний вузол, який обслуговує екземпляр блокнота Jupyter. Поверніться до [робочого простору Azure ML](https://ml.azure.com/) і натисніть на Compute instances. У списку обчислювальних екземплярів ви повинні побачити [обчислювальний екземпляр, який ми створили раніше](../../../../5-Data-Science-In-Cloud/19-Azure).

1. У розділі Applications натисніть на опцію Jupyter.  
2. Поставте галочку "Yes, I understand" і натисніть кнопку Continue.  
![notebook-1](../../../../5-Data-Science-In-Cloud/19-Azure/images/notebook-1.PNG)  
3. Це має відкрити нову вкладку браузера з вашим екземпляром блокнота Jupyter. Натисніть кнопку "New", щоб створити блокнот.  

![notebook-2](../../../../5-Data-Science-In-Cloud/19-Azure/images/notebook-2.PNG)

Тепер, коли у нас є блокнот, ми можемо почати навчання моделі за допомогою Azure ML SDK.

### 2.5 Навчання моделі

Перш за все, якщо у вас виникнуть сумніви, зверніться до [документації Azure ML SDK](https://docs.microsoft.com/python/api/overview/azure/ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109). Вона містить всю необхідну інформацію для розуміння модулів, які ми будемо розглядати в цьому уроці.

#### 2.5.1 Налаштування робочого простору, експерименту, обчислювального кластеру та набору даних

Вам потрібно завантажити `workspace` з конфігураційного файлу за допомогою наступного коду:

```python
from azureml.core import Workspace
ws = Workspace.from_config()
```

Це повертає об'єкт типу `Workspace`, який представляє робочий простір. Потім вам потрібно створити `experiment` за допомогою наступного коду:

```python
from azureml.core import Experiment
experiment_name = 'aml-experiment'
experiment = Experiment(ws, experiment_name)
```

Щоб отримати або створити експеримент у робочому просторі, ви запитуєте експеримент за його назвою. Назва експерименту повинна містити від 3 до 36 символів, починатися з літери або цифри і може містити лише літери, цифри, підкреслення та дефіси. Якщо експеримент не знайдено в робочому просторі, створюється новий експеримент.

Тепер вам потрібно створити обчислювальний кластер для навчання за допомогою наступного коду. Зверніть увагу, що цей крок може зайняти кілька хвилин.

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

Ви можете отримати набір даних із робочого простору за назвою набору даних наступним чином:

```python
dataset = ws.datasets['heart-failure-records']
df = dataset.to_pandas_dataframe()
df.describe()
```

#### 2.5.2 Конфігурація AutoML та навчання

Щоб налаштувати конфігурацію AutoML, використовуйте [клас AutoMLConfig](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.automlconfig(class)?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

Як описано в документації, існує багато параметрів, з якими можна працювати. Для цього проєкту ми будемо використовувати наступні параметри:

- `experiment_timeout_minutes`: Максимальний час (у хвилинах), протягом якого експеримент може виконуватися перед автоматичним завершенням і доступністю результатів.
- `max_concurrent_iterations`: Максимальна кількість одночасних ітерацій навчання, дозволених для експерименту.
- `primary_metric`: Основний показник, який використовується для визначення статусу експерименту.
- `compute_target`: Обчислювальна ціль Azure Machine Learning для запуску експерименту автоматизованого машинного навчання.
- `task`: Тип завдання для виконання. Значення можуть бути 'classification', 'regression' або 'forecasting' залежно від типу проблеми автоматизованого ML.
- `training_data`: Навчальні дані, які будуть використовуватися в експерименті. Вони повинні містити як навчальні ознаки, так і стовпець міток (опціонально стовпець ваг зразків).
- `label_column_name`: Назва стовпця міток.
- `path`: Повний шлях до папки проєкту Azure Machine Learning.
- `enable_early_stopping`: Чи дозволити раннє завершення, якщо показник не покращується в короткостроковій перспективі.
- `featurization`: Показник того, чи слід автоматично виконувати крок феатуризації, чи використовувати налаштовану феатуризацію.
- `debug_log`: Файл журналу для запису інформації про налагодження.

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

Тепер, коли конфігурація налаштована, ви можете навчити модель за допомогою наступного коду. Цей крок може зайняти до години залежно від розміру кластеру.

```python
remote_run = experiment.submit(automl_config)
```

Ви можете запустити віджет RunDetails, щоб показати різні експерименти.

```python
from azureml.widgets import RunDetails
RunDetails(remote_run).show()
```

## 3. Розгортання моделі та використання кінцевої точки за допомогою Azure ML SDK

### 3.1 Збереження найкращої моделі

`remote_run` — це об'єкт типу [AutoMLRun](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.run.automlrun?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109). Цей об'єкт містить метод `get_output()`, який повертає найкращий запуск і відповідну навчальну модель.

```python
best_run, fitted_model = remote_run.get_output()
```

Ви можете побачити параметри, використані для найкращої моделі, просто надрукувавши fitted_model, і переглянути властивості найкращої моделі за допомогою методу [get_properties()](https://docs.microsoft.com/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py#azureml_core_Run_get_properties?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

```python
best_run.get_properties()
```

Тепер зареєструйте модель за допомогою методу [register_model](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.run.automlrun?view=azure-ml-py#register-model-model-name-none--description-none--tags-none--iteration-none--metric-none-?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

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

### 3.2 Розгортання моделі

Після збереження найкращої моделі ми можемо розгорнути її за допомогою класу [InferenceConfig](https://docs.microsoft.com/python/api/azureml-core/azureml.core.model.inferenceconfig?view=azure-ml-py?ocid=AID3041109). InferenceConfig представляє налаштування конфігурації для користувацького середовища, яке використовується для розгортання. Клас [AciWebservice](https://docs.microsoft.com/python/api/azureml-core/azureml.core.webservice.aciwebservice?view=azure-ml-py) представляє модель машинного навчання, розгорнуту як кінцева точка вебсервісу на Azure Container Instances. Розгорнутий сервіс створюється з моделі, скрипту та пов'язаних файлів. Результуючий вебсервіс є збалансованою HTTP-кінцевою точкою з REST API. Ви можете надсилати дані до цього API і отримувати прогноз, повернутий моделлю.

Модель розгортається за допомогою методу [deploy](https://docs.microsoft.com/python/api/azureml-core/azureml.core.model(class)?view=azure-ml-py#deploy-workspace--name--models--inference-config-none--deployment-config-none--deployment-target-none--overwrite-false--show-output-false-?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

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

Цей крок має зайняти кілька хвилин.

### 3.3 Використання кінцевої точки

Ви використовуєте вашу кінцеву точку, створюючи зразок введення:

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

А потім можете надіслати цей введений зразок до вашої моделі для прогнозування:
```python
response = aci_service.run(input_data=test_sample)
response
```
Це має вивести `'{"result": [false]}'`. Це означає, що введені дані пацієнта, які ми надіслали на кінцеву точку, згенерували прогноз `false`, що означає, що ця людина, ймовірно, не матиме серцевого нападу.

Вітаємо! Ви щойно використали модель, розгорнуту та навчану на Azure ML за допомогою Azure ML SDK!

> **_NOTE:_** Коли завершите проєкт, не забудьте видалити всі ресурси.

## 🚀 Виклик

Існує багато інших речей, які можна зробити за допомогою SDK, на жаль, ми не можемо розглянути їх усі в цьому уроці. Але гарна новина — навчитися швидко переглядати документацію SDK може значно допомогти вам самостійно. Ознайомтеся з документацією Azure ML SDK і знайдіть клас `Pipeline`, який дозволяє створювати конвеєри. Конвеєр — це набір кроків, які можна виконувати як робочий процес.

**ПІДКАЗКА:** Перейдіть до [документації SDK](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) і введіть ключові слова в пошуковий рядок, наприклад "Pipeline". У результатах пошуку має з’явитися клас `azureml.pipeline.core.Pipeline`.

## [Тест після лекції](https://ff-quizzes.netlify.app/en/ds/quiz/37)

## Огляд і самостійне навчання

У цьому уроці ви дізналися, як навчати, розгортати та використовувати модель для прогнозування ризику серцевої недостатності за допомогою Azure ML SDK у хмарі. Ознайомтеся з цією [документацією](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) для отримання додаткової інформації про Azure ML SDK. Спробуйте створити власну модель за допомогою Azure ML SDK.

## Завдання

[Проєкт з Data Science за допомогою Azure ML SDK](assignment.md)

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.