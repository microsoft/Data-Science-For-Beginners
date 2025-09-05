<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "472d3fab1c5be50f387336e7a686dbe1",
  "translation_date": "2025-09-05T19:33:17+00:00",
  "source_file": "5-Data-Science-In-Cloud/19-Azure/README.md",
  "language_code": "sl"
}
-->
# Podatkovna znanost v oblaku: Način "Azure ML SDK"

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/19-DataScience-Cloud.png)|
|:---:|
| Podatkovna znanost v oblaku: Azure ML SDK - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Kazalo:

- [Podatkovna znanost v oblaku: Način "Azure ML SDK"](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Predhodni kviz](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [1. Uvod](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [1.1 Kaj je Azure ML SDK?](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [1.2 Projekt napovedovanja srčnega popuščanja in predstavitev podatkov](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [2. Učenje modela z Azure ML SDK](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.1 Ustvarjanje delovnega prostora Azure ML](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.2 Ustvarjanje računalniškega primerka](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.3 Nalaganje podatkov](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.4 Ustvarjanje beležk](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.5 Učenje modela](../../../../5-Data-Science-In-Cloud/19-Azure)
      - [2.5.1 Nastavitev delovnega prostora, eksperimenta, računalniškega grozda in podatkov](../../../../5-Data-Science-In-Cloud/19-Azure)
      - [2.5.2 Konfiguracija AutoML in učenje](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [3. Namestitev modela in uporaba končne točke z Azure ML SDK](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.1 Shranjevanje najboljšega modela](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.2 Namestitev modela](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.3 Uporaba končne točke](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [🚀 Izziv](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Zaključni kviz](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Pregled in samostojno učenje](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Naloga](../../../../5-Data-Science-In-Cloud/19-Azure)

## [Predhodni kviz](https://ff-quizzes.netlify.app/en/ds/quiz/36)

## 1. Uvod

### 1.1 Kaj je Azure ML SDK?

Podatkovni znanstveniki in razvijalci AI uporabljajo Azure Machine Learning SDK za gradnjo in izvajanje delovnih procesov strojnega učenja z uporabo storitve Azure Machine Learning. S storitvijo lahko komunicirate v katerem koli okolju Python, vključno z Jupyter Notebooks, Visual Studio Code ali vašim najljubšim Python IDE.

Ključna področja SDK vključujejo:

- Raziskovanje, pripravo in upravljanje življenjskega cikla vaših podatkovnih nizov, uporabljenih v eksperimentih strojnega učenja.
- Upravljanje oblačnih virov za spremljanje, beleženje in organizacijo vaših eksperimentov strojnega učenja.
- Učenje modelov lokalno ali z uporabo oblačnih virov, vključno z GPU-pospešenim učenjem modelov.
- Uporabo avtomatiziranega strojnega učenja, ki sprejema konfiguracijske parametre in podatke za učenje. Samodejno iterira skozi algoritme in nastavitve hiperparametrov, da najde najboljši model za napovedovanje.
- Namestitev spletnih storitev za pretvorbo vaših naučenih modelov v RESTful storitve, ki jih je mogoče uporabiti v katerikoli aplikaciji.

[Več o Azure Machine Learning SDK](https://docs.microsoft.com/python/api/overview/azure/ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

V [prejšnji lekciji](../18-Low-Code/README.md) smo videli, kako naučiti, namestiti in uporabiti model na način z malo ali brez kode. Uporabili smo podatkovni niz srčnega popuščanja za generiranje modela napovedovanja srčnega popuščanja. V tej lekciji bomo naredili popolnoma enako, vendar z uporabo Azure Machine Learning SDK.

![shema-projekta](../../../../5-Data-Science-In-Cloud/19-Azure/images/project-schema.PNG)

### 1.2 Projekt napovedovanja srčnega popuščanja in predstavitev podatkov

Oglejte si [tukaj](../18-Low-Code/README.md) predstavitev projekta napovedovanja srčnega popuščanja in podatkovnega niza.

## 2. Učenje modela z Azure ML SDK
### 2.1 Ustvarjanje delovnega prostora Azure ML

Za enostavnost bomo delali v jupyter beležki. To pomeni, da že imate delovni prostor in računalniški primer. Če že imate delovni prostor, lahko neposredno preskočite na razdelek 2.3 Ustvarjanje beležk.

Če ga nimate, sledite navodilom v razdelku **2.1 Ustvarjanje delovnega prostora Azure ML** v [prejšnji lekciji](../18-Low-Code/README.md) za ustvarjanje delovnega prostora.

### 2.2 Ustvarjanje računalniškega primerka

V [delovnem prostoru Azure ML](https://ml.azure.com/), ki smo ga ustvarili prej, pojdite v meni za računalniške vire, kjer boste videli različne razpoložljive računalniške vire.

![racunalniski-primer-1](../../../../5-Data-Science-In-Cloud/19-Azure/images/compute-instance-1.PNG)

Ustvarimo računalniški primer za pripravo jupyter beležke. 
1. Kliknite na gumb + New. 
2. Dajte ime svojemu računalniškemu primerku.
3. Izberite možnosti: CPU ali GPU, velikost VM in število jeder.
4. Kliknite na gumb Create.

Čestitamo, pravkar ste ustvarili računalniški primer! Ta primer bomo uporabili za ustvarjanje beležke v razdelku [Ustvarjanje beležk](../../../../5-Data-Science-In-Cloud/19-Azure).

### 2.3 Nalaganje podatkov
Če podatkovnega niza še niste naložili, si oglejte razdelek **2.3 Nalaganje podatkov** v [prejšnji lekciji](../18-Low-Code/README.md).

### 2.4 Ustvarjanje beležk

> **_OPOMBA:_** Za naslednji korak lahko ustvarite novo beležko iz nič ali pa naložite [beležko, ki smo jo ustvarili](../../../../5-Data-Science-In-Cloud/19-Azure/notebook.ipynb) v Azure ML Studio. Za nalaganje preprosto kliknite na meni "Notebook" in naložite beležko.

Beležke so zelo pomemben del procesa podatkovne znanosti. Uporabljajo se lahko za izvedbo raziskovalne analize podatkov (EDA), klicanje računalniškega grozda za učenje modela ali klicanje grozda za sklepanje za namestitev končne točke. 

Za ustvarjanje beležke potrebujemo računalniško vozlišče, ki izvaja jupyter beležko. Vrnite se v [delovni prostor Azure ML](https://ml.azure.com/) in kliknite na Računalniški primerki. Na seznamu računalniških primerkov bi morali videti [primer, ki smo ga ustvarili prej](../../../../5-Data-Science-In-Cloud/19-Azure). 

1. V razdelku Applications kliknite na možnost Jupyter. 
2. Označite polje "Yes, I understand" in kliknite na gumb Continue.
![beležka-1](../../../../5-Data-Science-In-Cloud/19-Azure/images/notebook-1.PNG)
3. To bi moralo odpreti nov zavihek brskalnika z vašim jupyter primerkom beležke. Kliknite na gumb "New" za ustvarjanje beležke.

![beležka-2](../../../../5-Data-Science-In-Cloud/19-Azure/images/notebook-2.PNG)

Zdaj, ko imamo beležko, lahko začnemo z učenjem modela z Azure ML SDK.

### 2.5 Učenje modela

Najprej, če imate kakršne koli dvome, si oglejte [dokumentacijo Azure ML SDK](https://docs.microsoft.com/python/api/overview/azure/ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109). Vsebuje vse potrebne informacije za razumevanje modulov, ki jih bomo obravnavali v tej lekciji.

#### 2.5.1 Nastavitev delovnega prostora, eksperimenta, računalniškega grozda in podatkov

Delovni prostor morate naložiti iz konfiguracijske datoteke z naslednjo kodo:

```python
from azureml.core import Workspace
ws = Workspace.from_config()
```

To vrne objekt tipa `Workspace`, ki predstavlja delovni prostor. Nato morate ustvariti `eksperiment` z naslednjo kodo:

```python
from azureml.core import Experiment
experiment_name = 'aml-experiment'
experiment = Experiment(ws, experiment_name)
```
Za pridobitev ali ustvarjanje eksperimenta iz delovnega prostora zahtevate eksperiment z uporabo imena eksperimenta. Ime eksperimenta mora biti dolgo 3-36 znakov, začeti z črko ali številko ter vsebovati le črke, številke, podčrtaje in vezaje. Če eksperiment ni najden v delovnem prostoru, se ustvari nov eksperiment.

Zdaj morate ustvariti računalniški grozd za učenje z naslednjo kodo. Upoštevajte, da lahko ta korak traja nekaj minut. 

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

Podatkovni niz lahko pridobite iz delovnega prostora z uporabo imena podatkovnega niza na naslednji način:

```python
dataset = ws.datasets['heart-failure-records']
df = dataset.to_pandas_dataframe()
df.describe()
```
#### 2.5.2 Konfiguracija AutoML in učenje

Za nastavitev konfiguracije AutoML uporabite [razred AutoMLConfig](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.automlconfig(class)?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

Kot je opisano v dokumentaciji, je na voljo veliko parametrov, s katerimi se lahko igrate. Za ta projekt bomo uporabili naslednje parametre:

- `experiment_timeout_minutes`: Najdaljši čas (v minutah), ki je dovoljen za izvajanje eksperimenta, preden se samodejno ustavi in rezultati postanejo na voljo.
- `max_concurrent_iterations`: Največje število hkratnih iteracij učenja, dovoljenih za eksperiment.
- `primary_metric`: Glavna metrika, ki se uporablja za določanje statusa eksperimenta.
- `compute_target`: Ciljni računalniški vir Azure Machine Learning za izvajanje eksperimenta avtomatiziranega strojnega učenja.
- `task`: Vrsta naloge za izvajanje. Vrednosti so lahko 'classification', 'regression' ali 'forecasting', odvisno od vrste problema avtomatiziranega strojnega učenja.
- `training_data`: Podatki za učenje, ki se uporabljajo v eksperimentu. Vsebujejo tako značilnosti za učenje kot stolpec z oznakami (po želji tudi stolpec z utežmi vzorcev).
- `label_column_name`: Ime stolpca z oznakami.
- `path`: Celotna pot do mape projekta Azure Machine Learning.
- `enable_early_stopping`: Ali omogočiti zgodnjo prekinitev, če se rezultat kratkoročno ne izboljšuje.
- `featurization`: Indikator, ali naj se korak featurizacije izvede samodejno ali ne, ali naj se uporabi prilagojena featurizacija.
- `debug_log`: Dnevniška datoteka za zapisovanje informacij o odpravljanju napak.

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
Zdaj, ko imate konfiguracijo nastavljeno, lahko model naučite z naslednjo kodo. Ta korak lahko traja do ene ure, odvisno od velikosti vašega grozda.

```python
remote_run = experiment.submit(automl_config)
```
Za prikaz različnih eksperimentov lahko zaženete pripomoček RunDetails.
```python
from azureml.widgets import RunDetails
RunDetails(remote_run).show()
```
## 3. Namestitev modela in uporaba končne točke z Azure ML SDK

### 3.1 Shranjevanje najboljšega modela

`remote_run` je objekt tipa [AutoMLRun](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.run.automlrun?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109). Ta objekt vsebuje metodo `get_output()`, ki vrne najboljši zagon in ustrezni naučeni model.

```python
best_run, fitted_model = remote_run.get_output()
```
Parametre, uporabljene za najboljši model, lahko vidite tako, da preprosto natisnete fitted_model, lastnosti najboljšega modela pa si ogledate z uporabo metode [get_properties()](https://docs.microsoft.com/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py#azureml_core_Run_get_properties?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

```python
best_run.get_properties()
```

Zdaj registrirajte model z metodo [register_model](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.run.automlrun?view=azure-ml-py#register-model-model-name-none--description-none--tags-none--iteration-none--metric-none-?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
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
### 3.2 Namestitev modela

Ko je najboljši model shranjen, ga lahko namestimo z razredom [InferenceConfig](https://docs.microsoft.com/python/api/azureml-core/azureml.core.model.inferenceconfig?view=azure-ml-py?ocid=AID3041109). InferenceConfig predstavlja nastavitve konfiguracije za prilagojeno okolje, uporabljeno za namestitev. Razred [AciWebservice](https://docs.microsoft.com/python/api/azureml-core/azureml.core.webservice.aciwebservice?view=azure-ml-py) predstavlja model strojnega učenja, nameščen kot spletna storitev na končni točki na Azure Container Instances. Nameščena storitev je uravnotežena HTTP končna točka z REST API. Podatke lahko pošljete na ta API in prejmete napoved, ki jo vrne model.

Model je nameščen z metodo [deploy](https://docs.microsoft.com/python/api/azureml-core/azureml.core.model(class)?view=azure-ml-py#deploy-workspace--name--models--inference-config-none--deployment-config-none--deployment-target-none--overwrite-false--show-output-false-?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

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
Ta korak lahko traja nekaj minut.

### 3.3 Uporaba končne točke

Končno točko uporabite tako, da ustvarite vzorčni vhod:

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
Nato lahko ta vhod pošljete svojemu modelu za napovedovanje:
```python
response = aci_service.run(input_data=test_sample)
response
```
To bi moralo vrniti `'{"result": [false]}'`. To pomeni, da je vhod pacienta, ki smo ga poslali na končno točko, ustvaril napoved `false`, kar pomeni, da ta oseba verjetno ne bo doživela srčnega napada.

Čestitke! Pravkar ste uporabili model, ki je bil nameščen in usposobljen na Azure ML z uporabo Azure ML SDK!


> **_NOTE:_** Ko zaključite projekt, ne pozabite izbrisati vseh virov.

## 🚀 Izziv

Obstaja veliko drugih stvari, ki jih lahko naredite prek SDK-ja, žal pa jih v tej lekciji ne moremo obravnavati vseh. Dobra novica je, da vas lahko sposobnost hitrega pregledovanja dokumentacije SDK-ja pripelje zelo daleč. Oglejte si dokumentacijo Azure ML SDK in poiščite razred `Pipeline`, ki vam omogoča ustvarjanje cevovodov. Cevovod je zbirka korakov, ki jih je mogoče izvesti kot delovni tok.

**NAMIG:** Obiščite [dokumentacijo SDK](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) in v iskalno vrstico vnesite ključne besede, kot je "Pipeline". V rezultatih iskanja bi morali najti razred `azureml.pipeline.core.Pipeline`.

## [Kvizi po predavanju](https://ff-quizzes.netlify.app/en/ds/quiz/37)

## Pregled in samostojno učenje

V tej lekciji ste se naučili, kako usposobiti, namestiti in uporabiti model za napovedovanje tveganja srčnega popuščanja z uporabo Azure ML SDK v oblaku. Oglejte si to [dokumentacijo](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) za dodatne informacije o Azure ML SDK. Poskusite ustvariti svoj model z uporabo Azure ML SDK.

## Naloga

[Projekt podatkovne znanosti z uporabo Azure ML SDK](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.