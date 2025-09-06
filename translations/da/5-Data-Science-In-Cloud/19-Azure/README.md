<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "472d3fab1c5be50f387336e7a686dbe1",
  "translation_date": "2025-09-05T21:56:51+00:00",
  "source_file": "5-Data-Science-In-Cloud/19-Azure/README.md",
  "language_code": "da"
}
-->
# Data Science i skyen: Den "Azure ML SDK" måde

|![ Sketchnote af [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/19-DataScience-Cloud.png)|
|:---:|
| Data Science i skyen: Azure ML SDK - _Sketchnote af [@nitya](https://twitter.com/nitya)_ |

Indholdsfortegnelse:

- [Data Science i skyen: Den "Azure ML SDK" måde](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Quiz før lektionen](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [1. Introduktion](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [1.1 Hvad er Azure ML SDK?](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [1.2 Projekt om hjertesvigt og introduktion til datasæt](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [2. Træning af en model med Azure ML SDK](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.1 Opret et Azure ML-arbejdsområde](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.2 Opret en beregningsinstans](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.3 Indlæsning af datasæt](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.4 Oprettelse af notebooks](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.5 Træning af en model](../../../../5-Data-Science-In-Cloud/19-Azure)
      - [2.5.1 Opsætning af arbejdsområde, eksperiment, beregningsklynge og datasæt](../../../../5-Data-Science-In-Cloud/19-Azure)
      - [2.5.2 AutoML-konfiguration og træning](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [3. Modeludrulning og forbrug af endpoints med Azure ML SDK](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.1 Gem den bedste model](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.2 Modeludrulning](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.3 Forbrug af endpoints](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [🚀 Udfordring](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Quiz efter lektionen](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Gennemgang & Selvstudie](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Opgave](../../../../5-Data-Science-In-Cloud/19-Azure)

## [Quiz før lektionen](https://ff-quizzes.netlify.app/en/ds/quiz/36)

## 1. Introduktion

### 1.1 Hvad er Azure ML SDK?

Dataforskere og AI-udviklere bruger Azure Machine Learning SDK til at opbygge og køre machine learning-arbejdsgange med Azure Machine Learning-tjenesten. Du kan interagere med tjenesten i ethvert Python-miljø, herunder Jupyter Notebooks, Visual Studio Code eller din foretrukne Python IDE.

Nøgleområder i SDK inkluderer:

- Udforsk, forbered og administrer livscyklussen for dine datasæt, der bruges i machine learning-eksperimenter.
- Administrer cloudressourcer til overvågning, logning og organisering af dine machine learning-eksperimenter.
- Træn modeller enten lokalt eller ved hjælp af cloudressourcer, inklusive GPU-accelereret modeltræning.
- Brug automatiseret machine learning, som accepterer konfigurationsparametre og træningsdata. Det itererer automatisk gennem algoritmer og hyperparameterindstillinger for at finde den bedste model til at køre forudsigelser.
- Udrul webtjenester for at konvertere dine trænede modeller til RESTful-tjenester, der kan forbruges i enhver applikation.

[Læs mere om Azure Machine Learning SDK](https://docs.microsoft.com/python/api/overview/azure/ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

I [den forrige lektion](../18-Low-Code/README.md) så vi, hvordan man træner, udruller og forbruger en model på en Low code/No code-måde. Vi brugte datasættet om hjertesvigt til at generere en model til forudsigelse af hjertesvigt. I denne lektion vil vi gøre præcis det samme, men ved hjælp af Azure Machine Learning SDK.

![projekt-skema](../../../../5-Data-Science-In-Cloud/19-Azure/images/project-schema.PNG)

### 1.2 Projekt om hjertesvigt og introduktion til datasæt

Se [her](../18-Low-Code/README.md) for introduktion til projektet om hjertesvigt og datasættet.

## 2. Træning af en model med Azure ML SDK
### 2.1 Opret et Azure ML-arbejdsområde

For nemheds skyld vil vi arbejde i en Jupyter Notebook. Dette indebærer, at du allerede har et arbejdsområde og en beregningsinstans. Hvis du allerede har et arbejdsområde, kan du gå direkte til afsnittet 2.3 Oprettelse af notebooks.

Hvis ikke, skal du følge instruktionerne i afsnittet **2.1 Opret et Azure ML-arbejdsområde** i [den forrige lektion](../18-Low-Code/README.md) for at oprette et arbejdsområde.

### 2.2 Opret en beregningsinstans

I [Azure ML-arbejdsområdet](https://ml.azure.com/), som vi oprettede tidligere, skal du gå til computermenuen, hvor du vil se de forskellige beregningsressourcer, der er tilgængelige.

![beregningsinstans-1](../../../../5-Data-Science-In-Cloud/19-Azure/images/compute-instance-1.PNG)

Lad os oprette en beregningsinstans for at klargøre en Jupyter Notebook. 
1. Klik på knappen + Ny. 
2. Giv din beregningsinstans et navn.
3. Vælg dine muligheder: CPU eller GPU, VM-størrelse og antal kerner.
4. Klik på knappen Opret.

Tillykke, du har lige oprettet en beregningsinstans! Vi vil bruge denne beregningsinstans til at oprette en notebook i afsnittet [Oprettelse af notebooks](../../../../5-Data-Science-In-Cloud/19-Azure).

### 2.3 Indlæsning af datasæt
Se afsnittet **2.3 Indlæsning af datasæt** i [den forrige lektion](../18-Low-Code/README.md), hvis du endnu ikke har uploadet datasættet.

### 2.4 Oprettelse af notebooks

> **_NOTE:_** Til det næste trin kan du enten oprette en ny notebook fra bunden eller uploade den [notebook, vi oprettede](../../../../5-Data-Science-In-Cloud/19-Azure/notebook.ipynb) i din Azure ML Studio. For at uploade den skal du blot klikke på "Notebook"-menuen og uploade notebooken.

Notebooks er en virkelig vigtig del af data science-processen. De kan bruges til at udføre Exploratory Data Analysis (EDA), kalde en beregningsklynge for at træne en model, eller kalde en inferensklynge for at udrulle et endpoint. 

For at oprette en notebook har vi brug for en beregningsnode, der leverer Jupyter Notebook-instansen. Gå tilbage til [Azure ML-arbejdsområdet](https://ml.azure.com/) og klik på Beregningsinstanser. I listen over beregningsinstanser bør du se [den beregningsinstans, vi oprettede tidligere](../../../../5-Data-Science-In-Cloud/19-Azure). 

1. I sektionen Applikationer skal du klikke på Jupyter-muligheden. 
2. Marker boksen "Ja, jeg forstår" og klik på knappen Fortsæt.
![notebook-1](../../../../5-Data-Science-In-Cloud/19-Azure/images/notebook-1.PNG)
3. Dette skulle åbne en ny browserfane med din Jupyter Notebook-instans som vist. Klik på knappen "Ny" for at oprette en notebook.

![notebook-2](../../../../5-Data-Science-In-Cloud/19-Azure/images/notebook-2.PNG)

Nu hvor vi har en notebook, kan vi begynde at træne modellen med Azure ML SDK.

### 2.5 Træning af en model

Først og fremmest, hvis du nogensinde er i tvivl, henvis til [Azure ML SDK-dokumentationen](https://docs.microsoft.com/python/api/overview/azure/ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109). Den indeholder alle nødvendige oplysninger for at forstå de moduler, vi skal se i denne lektion.

#### 2.5.1 Opsætning af arbejdsområde, eksperiment, beregningsklynge og datasæt

Du skal indlæse `workspace` fra konfigurationsfilen ved hjælp af følgende kode:

```python
from azureml.core import Workspace
ws = Workspace.from_config()
```

Dette returnerer et objekt af typen `Workspace`, der repræsenterer arbejdsområdet. Derefter skal du oprette et `experiment` ved hjælp af følgende kode:

```python
from azureml.core import Experiment
experiment_name = 'aml-experiment'
experiment = Experiment(ws, experiment_name)
```
For at få eller oprette et eksperiment fra et arbejdsområde anmoder du om eksperimentet ved hjælp af eksperimentets navn. Eksperimentnavnet skal være 3-36 tegn, starte med et bogstav eller et tal og kan kun indeholde bogstaver, tal, understregninger og bindestreger. Hvis eksperimentet ikke findes i arbejdsområdet, oprettes et nyt eksperiment.

Nu skal du oprette en beregningsklynge til træningen ved hjælp af følgende kode. Bemærk, at dette trin kan tage et par minutter. 

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

Du kan hente datasættet fra arbejdsområdet ved hjælp af datasætnavnet på følgende måde:

```python
dataset = ws.datasets['heart-failure-records']
df = dataset.to_pandas_dataframe()
df.describe()
```
#### 2.5.2 AutoML-konfiguration og træning

For at konfigurere AutoML skal du bruge [AutoMLConfig-klassen](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.automlconfig(class)?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

Som beskrevet i dokumentationen er der mange parametre, du kan lege med. Til dette projekt vil vi bruge følgende parametre:

- `experiment_timeout_minutes`: Den maksimale tid (i minutter), som eksperimentet må køre, før det automatisk stoppes, og resultaterne automatisk gøres tilgængelige.
- `max_concurrent_iterations`: Det maksimale antal samtidige træningsiterationer, der er tilladt for eksperimentet.
- `primary_metric`: Den primære metrik, der bruges til at bestemme eksperimentets status.
- `compute_target`: Azure Machine Learning-beregningsmålet, som det automatiserede machine learning-eksperiment skal køre på.
- `task`: Typen af opgave, der skal køres. Værdier kan være 'classification', 'regression' eller 'forecasting' afhængigt af typen af automatiseret ML-problem, der skal løses.
- `training_data`: Træningsdataene, der skal bruges i eksperimentet. Det skal indeholde både træningsfunktioner og en label-kolonne (valgfrit en sample weights-kolonne).
- `label_column_name`: Navnet på label-kolonnen.
- `path`: Den fulde sti til Azure Machine Learning-projektmappen.
- `enable_early_stopping`: Om tidlig afslutning skal aktiveres, hvis scoren ikke forbedres på kort sigt.
- `featurization`: Indikator for, om featurization-trinnet skal udføres automatisk eller ej, eller om tilpasset featurization skal bruges.
- `debug_log`: Logfilen til at skrive debug-information til.

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
Nu hvor du har din konfiguration på plads, kan du træne modellen ved hjælp af følgende kode. Dette trin kan tage op til en time afhængigt af din klyngestørrelse.

```python
remote_run = experiment.submit(automl_config)
```
Du kan køre RunDetails-widgeten for at vise de forskellige eksperimenter.
```python
from azureml.widgets import RunDetails
RunDetails(remote_run).show()
```
## 3. Modeludrulning og forbrug af endpoints med Azure ML SDK

### 3.1 Gem den bedste model

`remote_run` er et objekt af typen [AutoMLRun](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.run.automlrun?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109). Dette objekt indeholder metoden `get_output()`, som returnerer den bedste kørsel og den tilsvarende tilpassede model.

```python
best_run, fitted_model = remote_run.get_output()
```
Du kan se de parametre, der blev brugt til den bedste model, ved blot at printe `fitted_model` og se egenskaberne for den bedste model ved hjælp af metoden [get_properties()](https://docs.microsoft.com/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py#azureml_core_Run_get_properties?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

```python
best_run.get_properties()
```

Registrer nu modellen med metoden [register_model](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.run.automlrun?view=azure-ml-py#register-model-model-name-none--description-none--tags-none--iteration-none--metric-none-?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
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
### 3.2 Modeludrulning

Når den bedste model er gemt, kan vi udrulle den med klassen [InferenceConfig](https://docs.microsoft.com/python/api/azureml-core/azureml.core.model.inferenceconfig?view=azure-ml-py?ocid=AID3041109). InferenceConfig repræsenterer konfigurationsindstillingerne for et tilpasset miljø, der bruges til udrulning. Klassen [AciWebservice](https://docs.microsoft.com/python/api/azureml-core/azureml.core.webservice.aciwebservice?view=azure-ml-py) repræsenterer en machine learning-model, der er udrullet som et webtjeneste-endpoint på Azure Container Instances. En udrullet tjeneste oprettes fra en model, et script og tilhørende filer. Den resulterende webtjeneste er et load-balanceret HTTP-endpoint med en REST API. Du kan sende data til denne API og modtage forudsigelsen returneret af modellen.

Modellen udrulles ved hjælp af metoden [deploy](https://docs.microsoft.com/python/api/azureml-core/azureml.core.model(class)?view=azure-ml-py#deploy-workspace--name--models--inference-config-none--deployment-config-none--deployment-target-none--overwrite-false--show-output-false-?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

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
Dette trin bør tage et par minutter.

### 3.3 Forbrug af endpoints

Du forbruger dit endpoint ved at oprette en prøveinput:

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
Og derefter kan du sende dette input til din model for at få en forudsigelse:
```python
response = aci_service.run(input_data=test_sample)
response
```
Dette bør give outputtet `'{"result": [false]}'`. Det betyder, at de patientdata, vi sendte til endpointet, genererede forudsigelsen `false`, hvilket betyder, at denne person sandsynligvis ikke vil få et hjerteanfald.

Tillykke! Du har lige brugt modellen, der er deployeret og trænet på Azure ML med Azure ML SDK!


> **_NOTE:_** Når du er færdig med projektet, så husk at slette alle ressourcer.

## 🚀 Udfordring

Der er mange andre ting, du kan gøre med SDK'en, men desværre kan vi ikke gennemgå dem alle i denne lektion. Men gode nyheder: Hvis du lærer at navigere i SDK-dokumentationen, kan du komme langt på egen hånd. Tag et kig på Azure ML SDK-dokumentationen og find `Pipeline`-klassen, som giver dig mulighed for at oprette pipelines. En pipeline er en samling af trin, der kan udføres som en arbejdsgang.

**TIP:** Gå til [SDK-dokumentationen](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) og skriv nøgleord i søgefeltet som "Pipeline". Du bør finde `azureml.pipeline.core.Pipeline`-klassen i søgeresultaterne.

## [Quiz efter lektionen](https://ff-quizzes.netlify.app/en/ds/quiz/37)

## Gennemgang & Selvstudie

I denne lektion lærte du, hvordan man træner, deployerer og bruger en model til at forudsige risikoen for hjertesvigt med Azure ML SDK i skyen. Tjek denne [dokumentation](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) for yderligere information om Azure ML SDK. Prøv at oprette din egen model med Azure ML SDK.

## Opgave

[Data Science-projekt med Azure ML SDK](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.