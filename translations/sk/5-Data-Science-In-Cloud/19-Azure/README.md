<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5da2d6b3736f6d668b89de9bf3bdd31b",
  "translation_date": "2025-09-05T05:41:17+00:00",
  "source_file": "5-Data-Science-In-Cloud/19-Azure/README.md",
  "language_code": "sk"
}
-->
# Data Science v cloude: Cesta "Azure ML SDK"

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/19-DataScience-Cloud.png)|
|:---:|
| Data Science v cloude: Azure ML SDK - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

Obsah:

- [Data Science v cloude: Cesta "Azure ML SDK"](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Kvíz pred prednáškou](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [1. Úvod](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [1.1 Čo je Azure ML SDK?](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [1.2 Projekt predikcie zlyhania srdca a úvod do datasetu](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [2. Tréning modelu pomocou Azure ML SDK](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.1 Vytvorenie Azure ML pracovného priestoru](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.2 Vytvorenie výpočtového uzla](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.3 Načítanie datasetu](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.4 Vytváranie notebookov](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.5 Tréning modelu](../../../../5-Data-Science-In-Cloud/19-Azure)
      - [2.5.1 Nastavenie pracovného priestoru, experimentu, výpočtového klastru a datasetu](../../../../5-Data-Science-In-Cloud/19-Azure)
      - [2.5.2 Konfigurácia AutoML a tréning](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [3. Nasadenie modelu a využitie endpointu pomocou Azure ML SDK](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.1 Uloženie najlepšieho modelu](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.2 Nasadenie modelu](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.3 Využitie endpointu](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [🚀 Výzva](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Kvíz po prednáške](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Recenzia a samostatné štúdium](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Úloha](../../../../5-Data-Science-In-Cloud/19-Azure)

## [Kvíz pred prednáškou](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/36)

## 1. Úvod

### 1.1 Čo je Azure ML SDK?

Data scientisti a vývojári AI používajú Azure Machine Learning SDK na vytváranie a spúšťanie workflowov strojového učenia pomocou služby Azure Machine Learning. So službou môžete pracovať v akomkoľvek prostredí Pythonu, vrátane Jupyter Notebookov, Visual Studio Code alebo vášho obľúbeného Python IDE.

Kľúčové oblasti SDK zahŕňajú:

- Preskúmanie, príprava a správa životného cyklu datasetov používaných v experimentoch strojového učenia.
- Správa cloudových zdrojov na monitorovanie, logovanie a organizovanie experimentov strojového učenia.
- Tréning modelov buď lokálne, alebo pomocou cloudových zdrojov, vrátane tréningu modelov akcelerovaných GPU.
- Použitie automatizovaného strojového učenia, ktoré prijíma konfiguračné parametre a tréningové dáta. Automaticky iteruje cez algoritmy a nastavenia hyperparametrov, aby našiel najlepší model na predikcie.
- Nasadenie webových služieb na konverziu vašich trénovaných modelov na RESTful služby, ktoré môžu byť využité v akejkoľvek aplikácii.

[Viac informácií o Azure Machine Learning SDK](https://docs.microsoft.com/python/api/overview/azure/ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

V [predchádzajúcej lekcii](../18-Low-Code/README.md) sme videli, ako trénovať, nasadiť a využívať model v režime Low code/No code. Použili sme dataset zlyhania srdca na generovanie modelu predikcie zlyhania srdca. V tejto lekcii urobíme presne to isté, ale pomocou Azure Machine Learning SDK.

![projektová schéma](../../../../5-Data-Science-In-Cloud/19-Azure/images/project-schema.PNG)

### 1.2 Projekt predikcie zlyhania srdca a úvod do datasetu

Pozrite si [tu](../18-Low-Code/README.md) úvod do projektu predikcie zlyhania srdca a datasetu.

## 2. Tréning modelu pomocou Azure ML SDK
### 2.1 Vytvorenie Azure ML pracovného priestoru

Pre jednoduchosť budeme pracovať v jupyter notebooku. To znamená, že už máte pracovný priestor a výpočtový uzol. Ak už máte pracovný priestor, môžete preskočiť priamo na sekciu 2.3 Vytváranie notebookov.

Ak nie, postupujte podľa pokynov v sekcii **2.1 Vytvorenie Azure ML pracovného priestoru** v [predchádzajúcej lekcii](../18-Low-Code/README.md) na vytvorenie pracovného priestoru.

### 2.2 Vytvorenie výpočtového uzla

V [Azure ML pracovnom priestore](https://ml.azure.com/), ktorý sme vytvorili skôr, prejdite do menu Compute a uvidíte rôzne dostupné výpočtové zdroje.

![compute-instance-1](../../../../5-Data-Science-In-Cloud/19-Azure/images/compute-instance-1.PNG)

Vytvorme výpočtový uzol na zriadenie jupyter notebooku. 
1. Kliknite na tlačidlo + New. 
2. Dajte názov vášmu výpočtovému uzlu.
3. Vyberte možnosti: CPU alebo GPU, veľkosť VM a počet jadier.
4. Kliknite na tlačidlo Create.

Gratulujeme, práve ste vytvorili výpočtový uzol! Tento výpočtový uzol použijeme na vytvorenie notebooku v sekcii [Vytváranie notebookov](../../../../5-Data-Science-In-Cloud/19-Azure).

### 2.3 Načítanie datasetu
Ak ste dataset ešte nenahrali, pozrite si sekciu **2.3 Načítanie datasetu** v [predchádzajúcej lekcii](../18-Low-Code/README.md).

### 2.4 Vytváranie notebookov

> **_POZNÁMKA:_** Pre ďalší krok môžete buď vytvoriť nový notebook od začiatku, alebo nahrať [notebook, ktorý sme vytvorili](../../../../5-Data-Science-In-Cloud/19-Azure/notebook.ipynb) do vášho Azure ML Studio. Na jeho nahratie jednoducho kliknite na menu "Notebook" a nahrajte notebook.

Notebooky sú veľmi dôležitou súčasťou procesu data science. Môžu byť použité na vykonávanie prieskumných analýz dát (EDA), volanie výpočtového klastru na tréning modelu, alebo volanie inferenčného klastru na nasadenie endpointu. 

Na vytvorenie notebooku potrebujeme výpočtový uzol, ktorý poskytuje jupyter notebook. Vráťte sa do [Azure ML pracovného priestoru](https://ml.azure.com/) a kliknite na Compute instances. V zozname výpočtových uzlov by ste mali vidieť [výpočtový uzol, ktorý sme vytvorili skôr](../../../../5-Data-Science-In-Cloud/19-Azure). 

1. V sekcii Applications kliknite na možnosť Jupyter. 
2. Zaškrtnite políčko "Yes, I understand" a kliknite na tlačidlo Continue.
![notebook-1](../../../../5-Data-Science-In-Cloud/19-Azure/images/notebook-1.PNG)
3. Toto by malo otvoriť nový prehliadačový tab s vaším jupyter notebookom. Kliknite na tlačidlo "New" na vytvorenie notebooku.

![notebook-2](../../../../5-Data-Science-In-Cloud/19-Azure/images/notebook-2.PNG)

Teraz, keď máme notebook, môžeme začať trénovať model pomocou Azure ML SDK.

### 2.5 Tréning modelu

Najprv, ak máte akékoľvek pochybnosti, pozrite si [dokumentáciu Azure ML SDK](https://docs.microsoft.com/python/api/overview/azure/ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109). Obsahuje všetky potrebné informácie na pochopenie modulov, ktoré uvidíme v tejto lekcii.

#### 2.5.1 Nastavenie pracovného priestoru, experimentu, výpočtového klastru a datasetu

Pracovný priestor musíte načítať z konfiguračného súboru pomocou nasledujúceho kódu:

```python
from azureml.core import Workspace
ws = Workspace.from_config()
```

Toto vráti objekt typu `Workspace`, ktorý reprezentuje pracovný priestor. Potom musíte vytvoriť `experiment` pomocou nasledujúceho kódu:

```python
from azureml.core import Experiment
experiment_name = 'aml-experiment'
experiment = Experiment(ws, experiment_name)
```
Na získanie alebo vytvorenie experimentu z pracovného priestoru požiadate experiment pomocou názvu experimentu. Názov experimentu musí mať 3-36 znakov, začínať písmenom alebo číslom a môže obsahovať iba písmená, čísla, podčiarkovníky a pomlčky. Ak experiment nie je nájdený v pracovnom priestore, vytvorí sa nový experiment.

Teraz musíte vytvoriť výpočtový klaster na tréning pomocou nasledujúceho kódu. Upozorňujeme, že tento krok môže trvať niekoľko minút. 

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

Dataset môžete získať z pracovného priestoru pomocou názvu datasetu nasledujúcim spôsobom:

```python
dataset = ws.datasets['heart-failure-records']
df = dataset.to_pandas_dataframe()
df.describe()
```
#### 2.5.2 Konfigurácia AutoML a tréning

Na nastavenie konfigurácie AutoML použite [AutoMLConfig triedu](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.automlconfig(class)?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

Ako je popísané v dokumentácii, existuje veľa parametrov, s ktorými môžete experimentovať. Pre tento projekt použijeme nasledujúce parametre:

- `experiment_timeout_minutes`: Maximálny čas (v minútach), ktorý je experimentu povolený pred automatickým zastavením a sprístupnením výsledkov.
- `max_concurrent_iterations`: Maximálny počet súbežných tréningových iterácií povolených pre experiment.
- `primary_metric`: Primárna metrika používaná na určenie stavu experimentu.
- `compute_target`: Výpočtový cieľ Azure Machine Learning na spustenie experimentu automatizovaného strojového učenia.
- `task`: Typ úlohy na spustenie. Hodnoty môžu byť 'classification', 'regression' alebo 'forecasting' v závislosti od typu problému automatizovaného ML na riešenie.
- `training_data`: Tréningové dáta, ktoré sa majú použiť v rámci experimentu. Mali by obsahovať tréningové vlastnosti aj stĺpec s označením (voliteľne stĺpec s váhami vzoriek).
- `label_column_name`: Názov stĺpca s označením.
- `path`: Plná cesta k priečinku projektu Azure Machine Learning.
- `enable_early_stopping`: Či povoliť predčasné ukončenie, ak skóre krátkodobo nezlepšuje.
- `featurization`: Indikátor, či má byť krok featurizácie vykonaný automaticky alebo nie, alebo či má byť použitá prispôsobená featurizácia.
- `debug_log`: Súbor logov na zapisovanie informácií o ladení.

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
Teraz, keď máte nastavenú konfiguráciu, môžete trénovať model pomocou nasledujúceho kódu. Tento krok môže trvať až hodinu v závislosti od veľkosti vášho klastru.

```python
remote_run = experiment.submit(automl_config)
```
Môžete spustiť widget RunDetails na zobrazenie rôznych experimentov.
```python
from azureml.widgets import RunDetails
RunDetails(remote_run).show()
```
## 3. Nasadenie modelu a využitie endpointu pomocou Azure ML SDK

### 3.1 Uloženie najlepšieho modelu

`remote_run` je objekt typu [AutoMLRun](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.run.automlrun?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109). Tento objekt obsahuje metódu `get_output()`, ktorá vráti najlepší beh a zodpovedajúci trénovaný model.

```python
best_run, fitted_model = remote_run.get_output()
```
Parametre použité pre najlepší model môžete vidieť jednoducho vytlačením fitted_model a vlastnosti najlepšieho modelu môžete zobraziť pomocou metódy [get_properties()](https://docs.microsoft.com/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py#azureml_core_Run_get_properties?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

```python
best_run.get_properties()
```

Teraz zaregistrujte model pomocou metódy [register_model](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.run.automlrun?view=azure-ml-py#register-model-model-name-none--description-none--tags-none--iteration-none--metric-none-?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
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
### 3.2 Nasadenie modelu

Keď je najlepší model uložený, môžeme ho nasadiť pomocou triedy [InferenceConfig](https://docs.microsoft.com/python/api/azureml-core/azureml.core.model.inferenceconfig?view=azure-ml-py?ocid=AID3041109). InferenceConfig predstavuje konfiguračné nastavenia pre vlastné prostredie použité na nasadenie. Trieda [AciWebservice](https://docs.microsoft.com/python/api/azureml-core/azureml.core.webservice.aciwebservice?view=azure-ml-py) predstavuje model strojového učenia nasadený ako endpoint webovej služby na Azure Container Instances. Nasadená služba je vyvážený HTTP endpoint s REST API. Môžete poslať dáta na toto API a získať predikciu vrátenú modelom.

Model je nasadený pomocou metódy [deploy](https://docs.microsoft.com/python/api/azureml-core/azureml.core.model(class)?view=azure-ml-py#deploy-workspace--name--models--inference-config-none--deployment-config-none--deployment-target-none--overwrite-false--show-output-false-?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

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
Tento krok by mal trvať niekoľko minút.

### 3.3 Využitie endpointu

Endpoint môžete využiť vytvorením vzorového vstupu:

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
A potom môžete tento vstup poslať vášmu modelu na predikciu:
```python
response = aci_service.run(input_data=test_sample)
response
```
Toto by malo vrátiť `'{"result": [false]}'`. To znamená, že vstup pacienta, ktorý sme poslali na endpoint, vygeneroval predikciu `false`, čo znamená, že táto osoba pravdepodobne nedostane infarkt.

Gratulujeme! Práve ste použili model nasadený a trénovaný na Azure ML pomocou Azure ML SDK!


> **_NOTE:_** Keď dokončíte projekt, nezabudnite vymazať všetky zdroje.

## 🚀 Výzva

Existuje mnoho ďalších vecí, ktoré môžete robiť prostredníctvom SDK, bohužiaľ, nemôžeme ich všetky prejsť v tejto lekcii. Ale dobrá správa je, že naučiť sa prechádzať dokumentáciou SDK vám môže veľmi pomôcť. Pozrite si dokumentáciu Azure ML SDK a nájdite triedu `Pipeline`, ktorá vám umožňuje vytvárať pipeline. Pipeline je kolekcia krokov, ktoré môžu byť vykonané ako pracovný postup.

**TIP:** Prejdite na [dokumentáciu SDK](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) a zadajte kľúčové slová do vyhľadávacieho poľa, ako napríklad "Pipeline". Mali by ste mať triedu `azureml.pipeline.core.Pipeline` vo výsledkoch vyhľadávania.

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ds/)

## Prehľad & Samoštúdium

V tejto lekcii ste sa naučili, ako trénovať, nasadiť a používať model na predikciu rizika zlyhania srdca pomocou Azure ML SDK v cloude. Pozrite si túto [dokumentáciu](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) pre ďalšie informácie o Azure ML SDK. Skúste vytvoriť vlastný model pomocou Azure ML SDK. 

## Zadanie

[Projekt Data Science pomocou Azure ML SDK](assignment.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.