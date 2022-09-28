# 클라우드의 데이터 사이언스: "Azure ML SDK" 방식

|![ [(@sketchthedocs)의 스케치노트](https://sketchthedocs.dev) ](../../../sketchnotes/19-DataScience-Cloud.png)|
|:---:|
| 클라우드의 데이터 사이언스: Azure ML SDK - _[@nitya](https://twitter.com/nitya)_ 의 스케치노트 |

목차:

- [클라우드의 데이터 사이언스: "Azure ML SDK" 방식](#data-science-in-the-cloud-the-azure-ml-sdk-way)
  - [강의 전 퀴즈](#pre-lecture-quiz)
  - [1. 서론](#1-서론)
    - [1.1 Azure ML SDK란?](#11-what-is-azure-ml-sdk)
    - [1.2 심부전예측 프로젝트 및 데이터셋 도입](#12-heart-failure-prediction-project-and-dataset-introduction)
  - [2. Azure ML SDK로 모델 학습](#2-training-a-model-with-the-azure-ml-sdk)
    - [2.1 Azure ML 작업 영역 만들기](#21-create-an-azure-ml-workspace)
    - [2.2 컴퓨팅 인스턴스 생성](#22-create-a-compute-instance)
    - [2.3 데이터셋 불러오기](#23-loading-the-dataset)
    - [2.4 Notebook 만들기](#24-creating-notebooks)
    - [2.5 모델 훈련](#25-training-a-model)
      - [2.5.1 설정 작업 공간, 실험, 컴퓨팅 클러스터 및 데이터셋](#251-setup-workspace-experiment-compute-cluster-and-dataset)
      - [2.5.2 AutoML 구성 및 교육](#252-automl-configuration-and-training)
  - [삼. Azure ML SDK를 사용한 모델 배포 및 끝점 소비](#3-model-deployment-and-endpoint-consumption-with-the-azure-ml-sdk)
    - [3.1 베스트 모델 저장](#31-saving-the-best-model)
    - [3.2 모델 배포](#32-model-deployment)
    - [3.3 엔드포인트 소비](#33-endpoint-consumption)
  - [🚀챌린지](#-챌린지)
  - [강의후퀴즈](#강의후퀴즈)
  - [리뷰&자습](#리뷰--자습)
  - [과제](#과제)

## [강의전 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/36)

## 1. 소개

### 1.1 Azure ML SDK란 무엇입니까?

데이터 사이언스자와 AI 개발자는 Azure Machine Learning SDK를 사용하여 Azure Machine Learning 서비스로 기계 학습 워크플로를 빌드하고 실행합니다. Jupyter Notebook, Visual Studio Code 또는 선호하는 Python IDE를 비롯한 모든 Python 환경에서 서비스와 상호 작용할 수 있습니다.

SDK의 주요 영역은 다음과 같습니다.

- 기계 학습 실험에 사용되는 데이터셋의 수명 주기를 탐색, 준비 및 관리합니다.
- 머신 러닝 실험을 모니터링, 로깅 및 구성하기 위한 클라우드 리소스를 관리합니다.
- GPU 가속 모델 교육을 포함하여 로컬에서 또는 클라우드 리소스를 사용하여 모델을 교육합니다.
- 구성 매개변수 및 교육 데이터를 허용하는 자동화된 기계 학습을 사용합니다. 알고리즘과 하이퍼파라미터 설정을 자동으로 반복하여 예측 실행에 가장 적합한 모델을 찾습니다.
- 웹 서비스를 배포하여 훈련된 모델을 모든 애플리케이션에서 사용할 수 있는 RESTful 서비스로 변환합니다.

[Azure Machine Learning SDK에 대해 자세히 알아보기](https://docs.microsoft.com/python/api/overview/azure/ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

[이전 강의](../../18-Low-Code/translations/README.ko.md)에서 Low code/No code 방식으로 모델을 훈련, 배포 및 소비하는 방법을 살펴보았습니다. 심부전 데이터셋을 사용하여 심부전 예측 모델을 생성했습니다. 이 단원에서는 Azure Machine Learning SDK를 사용하여 똑같은 작업을 수행할 것입니다.

![프로젝트 스키마](../images/project-schema.PNG)

### 1.2 심부전 예측 프로젝트 및 데이터셋 소개

[여기](../../18-Low-Code/translations/README.ko.md)에서 심부전예측 프로젝트 및 데이터셋 소개를 확인하세요.

## 2. Azure ML SDK로 모델 학습
### 2.1 Azure ML 작업 영역 만들기

간단히 하기 위해 우리는 jupyter Notebook에서 작업할 것입니다. 이는 이미 작업 공간과 컴퓨팅 인스턴스가 있음을 의미합니다. 이미 작업 공간이 있는 경우 섹션 2.3 Notebook 생성으로 바로 이동할 수 있습니다.

그렇지 않은 경우 [이전 강의](../../18-Low-Code/translations/README.ko.md)의 **2.1 Azure ML 워크스페이스 만들기** 섹션의 지침에 따라 워크스페이스을 만듭니다.

### 2.2 컴퓨팅 인스턴스 생성

앞서 만든 [Azure ML 워크스페이스](https://ml.azure.com/)에서 컴퓨팅 메뉴로 이동하면 사용 가능한 다양한 컴퓨팅 리소스가 표시됩니다.

![compute-instance-1](../images/compute-instance-1.PNG)

Jupyter Notebook을 프로비저닝할 컴퓨팅 인스턴스를 생성해 보겠습니다.
1. + 새로 만들기 버튼을 클릭합니다.
2. 컴퓨팅 인스턴스에 이름을 지정합니다.
3. CPU 또는 GPU, VM 크기 및 코어 번호 중에서 옵션을 선택합니다.
4. 만들기 버튼을 클릭합니다.

축하합니다. 방금 컴퓨팅 인스턴스를 만들었습니다! 이 컴퓨팅 인스턴스를 사용하여 [Notebook 생성 섹션](#23-creating-notebooks)에서 Notebook을 생성합니다.

### 2.3 데이터셋 로드
아직 데이터셋을 업로드하지 않았다면 **2.3 데이터셋 로드하기** 섹션의 [이전 강의](../../18-Low-Code/translations/README.ko.md)를 참조하세요.

### 2.4 Notebook 만들기

> **_참고:_** 다음 단계에서는 처음부터 새 Notebook을 만들거나 Azure ML Studio에서 [우리가 만든 Notebook](../notebook.ipynb)을 업로드할 수 있습니다. 그것을 업로드하려면 "Notebook" 메뉴를 클릭하고 Notebook을 업로드하십시오.

Notebook은 데이터 사이언스 프로세스에서 정말 중요한 부분입니다. 탐색적 데이터 분석(EDA)을 수행하고, 모델을 훈련하기 위해 컴퓨터 클러스터를 호출하고, 엔드포인트를 배포하기 위해 추론 클러스터를 호출하는 데 사용할 수 있습니다.

Notebook을 생성하려면 jupyter Notebook 인스턴스를 제공하는 컴퓨팅 노드가 필요합니다. [Azure ML 작업 영역](https://ml.azure.com/)으로 돌아가서 Compute 인스턴스를 클릭합니다. 컴퓨팅 인스턴스 목록에서 [이전에 생성한 컴퓨팅 인스턴스](#22-create-a-compute-instance)가 표시되어야 합니다.

1. 애플리케이션 섹션에서 Jupyter 옵션을 클릭합니다.
2. "예, 이해합니다" 상자를 선택하고 계속 버튼을 클릭합니다.
![notebook-1](../images/notebook-1.PNG)
3. 그러면 다음과 같이 jupyter Notebook 인스턴스가 있는 새 브라우저 탭이 열립니다. "새로 만들기" 버튼을 클릭하여 Notebook을 만듭니다.

![notebook-2](../images/notebook-2.PNG)

이제 Notebook이 있으므로 Azure ML SDK를 사용하여 모델 학습을 시작할 수 있습니다.

### 2.5 모델 학습

먼저 궁금한 점이 있으시면 [Azure ML SDK 설명서](https://docs.microsoft.com/python/api/overview/azure/ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)을 참고할 수 있습니다. 여기에는 이 단원에서 보게 될 모듈을 이해하는 데 필요한 모든 정보가 포함되어 있습니다.

#### 2.5.1 작업 공간, 실험, 컴퓨팅 클러스터 및 데이터셋 설정

다음 코드를 사용하여 구성 파일에서 '작업 공간'을 로드해야 합니다.

```python
from azureml.core import Workspace
ws = Workspace.from_config()
```

이것은 작업 공간을 나타내는 '작업 공간' 유형의 개체를 반환합니다. 다음 코드를 사용하여 '실험'을 생성해야 합니다.

```python
from azureml.core import Experiment
experiment_name = 'aml-experiment'
experiment = Experiment(ws, experiment_name)
```
작업 공간에서 실험을 가져오거나 생성하려면 실험 이름을 사용하여 실험을 요청합니다. 실험 이름은 3-36자여야 하며 문자 또는 숫자로 시작해야 하며 문자, 숫자, 밑줄 및 대시만 포함할 수 있습니다. 작업 공간에 실험이 없으면 새 실험이 생성됩니다.

이제 다음 코드를 사용하여 훈련을 위한 컴퓨팅 클러스터를 생성해야 합니다. 이 단계는 몇 분 정도 걸릴 수 있습니다.

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

다음과 같은 방법으로 데이터셋 이름을 사용하여 작업 공간에서 데이터셋을 가져올 수 있습니다.

```python
dataset = ws.datasets['heart-failure-records']
df = dataset.to_pandas_dataframe()
df.describe()
```
#### 2.5.2 AutoML 구성 및 교육

AutoML 구성을 설정하려면 [AutoMLConfig 클래스](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.automlconfig(class)?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)를 사용하세요.

문서에 설명된 대로 가지고 놀 수 있는 많은 매개변수가 있습니다. 이 프로젝트에서는 다음 매개변수를 사용합니다.

- `experiment_timeout_minutes`: 실험이 자동으로 중지되고 결과가 자동으로 제공되기 전에 실행할 수 있는 최대 시간(분)
- `max_concurrent_iterations`: 실험에 허용되는 최대 동시 학습 반복 횟수입니다.
- `primary_metric`: 실험 상태를 결정하는 데 사용되는 기본 측정항목입니다.
- `compute_target`: 자동화된 기계 학습 실험을 실행할 Azure 기계 학습 계산 대상입니다.
- `task`: 실행할 작업의 유형입니다. 값은 해결할 자동화된 ML 문제 유형에 따라 '분류', '회귀' 또는 '예측'일 수 있습니다.
- `training_data`: 실험 내에서 사용할 훈련 데이터입니다. 여기에는 훈련 기능과 레이블 열(선택적으로 샘플 가중치 열)이 모두 포함되어야 합니다.
- `label_column_name`: 레이블 열의 이름입니다.
- `경로`: Azure Machine Learning 프로젝트 폴더의 전체 경로입니다.
- `enable_early_stopping`: 단기간에 점수가 오르지 않을 경우 조기종료 가능 여부.
- `featurization`: 피처링 단계를 자동으로 수행할지 여부 또는 사용자 정의 기능화(featurization)를 사용해야 하는지 여부를 나타내는 표시기(indicator)입니다.
- `debug_log`: 디버그 정보를 기록할 로그 파일입니다.

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
이제 구성이 설정되었으므로 다음 코드를 사용하여 모델을 훈련할 수 있습니다. 이 단계는 클러스터 크기에 따라 최대 1시간이 소요될 수 있습니다.

```python
remote_run = experiment.submit(automl_config)
```
RunDetails 위젯을 실행하여 다양한 실험을 표시할 수 있습니다.
```python
from azureml.widgets import RunDetails
RunDetails(remote_run).show()
```
## 3. Azure ML SDK를 사용한 모델 배포 및 엔드포인트 사용

### 3.1 최고의 모델 저장

[AutoMLRun](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.run.automlrun?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)타입 중 하나인 `remote_run` 객체. 이 객체에는 최상의 실행과 해당하는 적합 모델을 반환하는 `get_output()` 메서드가 포함되어 있습니다.

```python
best_run, fitted_model = remote_run.get_output()
```
fit_model을 출력하기만 하면 최상의 모델에 사용된 매개변수를 볼 수 있고 [get_properties()](https://docs.microsoft.com/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py#azureml_core_Run_get_properties?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) 메소드를 사용하여 최상의 모델의 속성을 볼 수 있습니다.

```python
best_run.get_properties()
```

이제 [register_model](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.run.automlrun?view=azure-ml-py#register-model-model-name-none--description-none--tags-none--iteration-none--metric-none-?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) 방법을 사용해 모델을 등록해봅시다.
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
### 3.2 모델 배포

최상의 모델이 저장되면 [InferenceConfig](https://docs.microsoft.com/python/api/azureml-core/azureml.core.model.inferenceconfig?view=azure-ml-py?ocid=AID3041109) 클래스를 사용하여 배포할 수 있습니다. InferenceConfig는 배포에 사용되는 사용자 지정 환경에 대한 구성 설정을 나타냅니다. [AciWebservice](https://docs.microsoft.com/python/api/azureml-core/azureml.core.webservice.aciwebservice?view=azure-ml-py) 클래스는 웹 서비스로 배포된 기계 학습 모델을 나타냅니다. Azure Container Instances의 엔드포인트. 배포된 서비스는 모델, 스크립트 및 관련 파일에서 생성됩니다. 결과 웹 서비스는 REST API가 있는 로드 밸런싱된 HTTP 엔드포인트입니다. 이 API로 데이터를 보내고 모델에서 반환된 예측을 받을 수 있습니다.

모델은 [deploy](https://docs.microsoft.com/python/api/azureml-core/azureml.core.model(class)?view=azure-ml-py#deploy-workspace--name--models--inference-config-none--deployment-config-none--deployment-target-none--overwrite-false--show-output-false-?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) 방법을 사용하여 배포됩니다.

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
이 과정은 몇 분의 시간이 걸릴 수 있습니다.

### 3.3 Endpoint 소비

샘플 입력을 생성하여 엔드포인트를 사용합니다:

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
그런 다음 예측을 위해 이 입력을 모델에 보낼 수 있습니다.

```python
response = aci_service.run(input_data=test_sample)
response
```
이것은 `'{"result": [false]}'`를 출력해야 합니다. 이것은 우리가 끝점에 보낸 환자 입력이 예측 '거짓'을 생성했음을 의미합니다.

축하합니다! Azure ML SDK를 사용하여 Azure ML에 배포 및 학습된 모델을 사용했습니다!

> **_참고:_** 프로젝트가 끝나면 모든 리소스를 삭제하는 것을 잊지 마십시오.

## 🚀 도전

 SDK를 통해 수행할 수 있는 다른 많은 작업이 있지만 불행히도 이 강의에서 모두 볼 수는 없습니다. 그러나 좋은 소식은 SDK 문서를 훑어보는 방법을 배우면 스스로 많은 시간을 할애할 수 있다는 것입니다. Azure ML SDK 설명서를 살펴보고 파이프라인을 만들 수 있는 'Pipeline' 클래스를 찾으세요. 파이프라인은 워크플로로 실행할 수 있는 단계 모음입니다.

**힌트:** [SDK 설명서](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) 로 이동합니다. 검색창에 "파이프라인"과 같은 키워드를 입력합니다. 검색 결과에 `azureml.pipeline.core.Pipeline` 클래스가 있어야 합니다.

## [강의 후 퀴즈](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/37)

## 복습 및 독학

이 단원에서는 클라우드에서 Azure ML SDK를 사용하여 심부전 위험을 예측하기 위해 모델을 학습, 배포 및 사용하는 방법을 배웠습니다. 자세한 내용은 이 [문서](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)를 확인하세요. Azure ML SDK에 대해 Azure ML SDK를 사용하여 고유한 모델을 만들어 보세요.

## 과제

[Azure ML SDK를 이용한 Data Science 프로젝트](./assignment.ko.md)


