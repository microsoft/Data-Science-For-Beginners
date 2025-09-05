<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5da2d6b3736f6d668b89de9bf3bdd31b",
  "translation_date": "2025-09-04T22:08:36+00:00",
  "source_file": "5-Data-Science-In-Cloud/19-Azure/README.md",
  "language_code": "hu"
}
-->
# Adattudomány a felhőben: Az "Azure ML SDK" módszer

|![ Sketchnote készítette: [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/19-DataScience-Cloud.png)|
|:---:|
| Adattudomány a felhőben: Azure ML SDK - _Sketchnote készítette: [@nitya](https://twitter.com/nitya)_ |

Tartalomjegyzék:

- [Adattudomány a felhőben: Az "Azure ML SDK" módszer](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Előadás előtti kvíz](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [1. Bevezetés](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [1.1 Mi az Azure ML SDK?](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [1.2 Szívelégtelenség előrejelzési projekt és adatkészlet bemutatása](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [2. Modell betanítása az Azure ML SDK-val](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.1 Azure ML munkaterület létrehozása](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.2 Számítási példány létrehozása](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.3 Az adatkészlet betöltése](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.4 Jegyzetfüzetek létrehozása](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [2.5 Modell betanítása](../../../../5-Data-Science-In-Cloud/19-Azure)
      - [2.5.1 Munkaterület, kísérlet, számítási fürt és adatkészlet beállítása](../../../../5-Data-Science-In-Cloud/19-Azure)
      - [2.5.2 AutoML konfiguráció és betanítás](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [3. Modell telepítése és végpont fogyasztása az Azure ML SDK-val](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.1 A legjobb modell mentése](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.2 Modell telepítése](../../../../5-Data-Science-In-Cloud/19-Azure)
    - [3.3 Végpont fogyasztása](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [🚀 Kihívás](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Előadás utáni kvíz](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Áttekintés és önálló tanulás](../../../../5-Data-Science-In-Cloud/19-Azure)
  - [Feladat](../../../../5-Data-Science-In-Cloud/19-Azure)

## [Előadás előtti kvíz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/36)

## 1. Bevezetés

### 1.1 Mi az Azure ML SDK?

Az adattudósok és mesterséges intelligencia fejlesztők az Azure Machine Learning SDK-t használják gépi tanulási munkafolyamatok létrehozására és futtatására az Azure Machine Learning szolgáltatással. A szolgáltatással bármilyen Python környezetben dolgozhatunk, beleértve a Jupyter Notebookokat, a Visual Studio Code-ot vagy a kedvenc Python IDE-t.

Az SDK kulcsfontosságú területei:

- Az adatkészletek felfedezése, előkészítése és életciklusának kezelése a gépi tanulási kísérletek során.
- Felhőalapú erőforrások kezelése a kísérletek monitorozásához, naplózásához és szervezéséhez.
- Modellek betanítása helyben vagy felhőalapú erőforrásokkal, beleértve a GPU-gyorsított modell betanítást.
- Automatikus gépi tanulás használata, amely konfigurációs paramétereket és betanítási adatokat fogad. Ez automatikusan iterál algoritmusokon és hiperparaméter-beállításokon, hogy megtalálja a legjobb modellt az előrejelzések futtatásához.
- Webszolgáltatások telepítése, amelyek a betanított modelleket RESTful szolgáltatásokká alakítják, amelyek bármilyen alkalmazásban felhasználhatók.

[További információ az Azure Machine Learning SDK-ról](https://docs.microsoft.com/python/api/overview/azure/ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)

Az [előző leckében](../18-Low-Code/README.md) megvizsgáltuk, hogyan lehet modellt betanítani, telepíteni és fogyasztani alacsony kódú/nem kódú megközelítéssel. A Szívelégtelenség adatkészletet használtuk egy szívelégtelenség előrejelzési modell létrehozásához. Ebben a leckében pontosan ugyanezt fogjuk megtenni, de az Azure Machine Learning SDK használatával.

![projekt-séma](../../../../5-Data-Science-In-Cloud/19-Azure/images/project-schema.PNG)

### 1.2 Szívelégtelenség előrejelzési projekt és adatkészlet bemutatása

Tekintse meg [itt](../18-Low-Code/README.md) a Szívelégtelenség előrejelzési projekt és adatkészlet bemutatását.

## 2. Modell betanítása az Azure ML SDK-val
### 2.1 Azure ML munkaterület létrehozása

Egyszerűség kedvéért egy Jupyter notebookban fogunk dolgozni. Ez azt jelenti, hogy már rendelkeznie kell egy munkaterülettel és egy számítási példánnyal. Ha már van munkaterülete, közvetlenül ugorhat a **2.3 Jegyzetfüzet létrehozása** szakaszra.

Ha nincs, kövesse az utasításokat a [korábbi leckében](../18-Low-Code/README.md) a **2.1 Azure ML munkaterület létrehozása** szakaszban.

### 2.2 Számítási példány létrehozása

Az [Azure ML munkaterületen](https://ml.azure.com/), amelyet korábban létrehoztunk, lépjen a Compute menübe, ahol láthatja a különböző számítási erőforrásokat.

![számítási-példány-1](../../../../5-Data-Science-In-Cloud/19-Azure/images/compute-instance-1.PNG)

Hozzunk létre egy számítási példányt egy Jupyter notebook biztosításához.  
1. Kattintson az + Új gombra.  
2. Adjon nevet a számítási példánynak.  
3. Válassza ki az opciókat: CPU vagy GPU, VM méret és magok száma.  
4. Kattintson a Létrehozás gombra.

Gratulálunk, most hozott létre egy számítási példányt! Ezt a számítási példányt fogjuk használni a [Jegyzetfüzetek létrehozása](../../../../5-Data-Science-In-Cloud/19-Azure) szakaszban.

### 2.3 Az adatkészlet betöltése
Ha még nem töltötte fel az adatkészletet, tekintse meg a [korábbi leckében](../18-Low-Code/README.md) a **2.3 Az adatkészlet betöltése** szakaszt.

### 2.4 Jegyzetfüzetek létrehozása

> **_MEGJEGYZÉS:_** A következő lépéshez vagy létrehozhat egy új jegyzetfüzetet a semmiből, vagy feltöltheti a [korábban létrehozott jegyzetfüzetet](../../../../5-Data-Science-In-Cloud/19-Azure/notebook.ipynb) az Azure ML Stúdióba. A feltöltéshez egyszerűen kattintson a "Jegyzetfüzet" menüre, és töltse fel a jegyzetfüzetet.

A jegyzetfüzetek nagyon fontos részét képezik az adattudományi folyamatnak. Használhatók feltáró adatelemzés (EDA) végrehajtására, számítási fürt hívására modell betanításához, vagy előrejelzési fürt hívására végpont telepítéséhez.

Jegyzetfüzet létrehozásához szükségünk van egy számítási csomópontra, amely a Jupyter notebook példányt szolgáltatja. Térjen vissza az [Azure ML munkaterületre](https://ml.azure.com/), és kattintson a Számítási példányok menüpontra. A számítási példányok listájában látnia kell a [korábban létrehozott számítási példányt](../../../../5-Data-Science-In-Cloud/19-Azure).

1. Az Alkalmazások szakaszban kattintson a Jupyter opcióra.  
2. Jelölje be az "Igen, megértettem" négyzetet, majd kattintson a Folytatás gombra.  
![jegyzetfüzet-1](../../../../5-Data-Science-In-Cloud/19-Azure/images/notebook-1.PNG)  
3. Ez megnyit egy új böngészőfület a Jupyter notebook példányával. Kattintson az "Új" gombra egy jegyzetfüzet létrehozásához.  

![jegyzetfüzet-2](../../../../5-Data-Science-In-Cloud/19-Azure/images/notebook-2.PNG)

Most, hogy van egy jegyzetfüzetünk, elkezdhetjük a modell betanítását az Azure ML SDK-val.

### 2.5 Modell betanítása

Először is, ha bármikor kétségei támadnak, tekintse meg az [Azure ML SDK dokumentációját](https://docs.microsoft.com/python/api/overview/azure/ml?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109). Ez tartalmazza az összes szükséges információt az ebben a leckében tárgyalt modulok megértéséhez.

#### 2.5.1 Munkaterület, kísérlet, számítási fürt és adatkészlet beállítása

A `workspace` betöltéséhez a konfigurációs fájlból használja a következő kódot:

```python
from azureml.core import Workspace
ws = Workspace.from_config()
```

Ez egy `Workspace` típusú objektumot ad vissza, amely a munkaterületet képviseli. Ezután létre kell hoznia egy `experiment`-et a következő kód segítségével:

```python
from azureml.core import Experiment
experiment_name = 'aml-experiment'
experiment = Experiment(ws, experiment_name)
```
Egy kísérlet lekéréséhez vagy létrehozásához a munkaterületről kérje le a kísérletet a nevével. A kísérlet neve 3-36 karakter hosszú lehet, betűvel vagy számmal kell kezdődnie, és csak betűket, számokat, aláhúzásokat és kötőjeleket tartalmazhat. Ha a kísérlet nem található a munkaterületen, egy új kísérlet jön létre.

Most hozzon létre egy számítási fürtöt a betanításhoz a következő kód segítségével. Vegye figyelembe, hogy ez a lépés néhány percet igénybe vehet.

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

Az adatkészletet a munkaterületről a neve alapján kérheti le az alábbi módon:

```python
dataset = ws.datasets['heart-failure-records']
df = dataset.to_pandas_dataframe()
df.describe()
```
#### 2.5.2 AutoML konfiguráció és betanítás

Az AutoML konfiguráció beállításához használja az [AutoMLConfig osztályt](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.automlconfig(class)?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).

A dokumentáció szerint számos paraméterrel játszhatunk. Ehhez a projekthez a következő paramétereket fogjuk használni:

- `experiment_timeout_minutes`: Az a maximális idő (percben), amely alatt a kísérlet futtatható, mielőtt automatikusan leállna, és az eredmények elérhetővé válnának.
- `max_concurrent_iterations`: A kísérlethez engedélyezett maximális egyidejű betanítási iterációk száma.
- `primary_metric`: Az elsődleges metrika, amely alapján a kísérlet állapota meghatározásra kerül.
- `compute_target`: Az Azure Machine Learning számítási cél, amelyen az Automatikus Gépi Tanulási kísérlet fut.
- `task`: A futtatandó feladat típusa. Az értékek lehetnek 'classification', 'regression' vagy 'forecasting', a megoldandó automatikus ML probléma típusától függően.
- `training_data`: A kísérletben használandó betanítási adatok. Tartalmaznia kell mind a betanítási jellemzőket, mind egy címkeoszlopot (opcionálisan egy minta súlyoszlopot).
- `label_column_name`: A címkeoszlop neve.
- `path`: Az Azure Machine Learning projekt mappájának teljes elérési útja.
- `enable_early_stopping`: Engedélyezi-e a korai leállítást, ha a pontszám rövid távon nem javul.
- `featurization`: Jelzi, hogy az automatikus jellemzőképzés történjen-e, vagy sem, illetve hogy egyedi jellemzőképzést kell-e használni.
- `debug_log`: A naplófájl, amelybe a hibakeresési információkat írja.

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
Most, hogy a konfiguráció be van állítva, betaníthatja a modellt a következő kód segítségével. Ez a lépés akár egy órát is igénybe vehet a fürt méretétől függően.

```python
remote_run = experiment.submit(automl_config)
```
A RunDetails widget segítségével megjelenítheti a különböző kísérleteket.
```python
from azureml.widgets import RunDetails
RunDetails(remote_run).show()
```
## 3. Modell telepítése és végpont fogyasztása az Azure ML SDK-val

### 3.1 A legjobb modell mentése

A `remote_run` egy [AutoMLRun](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.run.automlrun?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) típusú objektum. Ez az objektum tartalmazza a `get_output()` metódust, amely visszaadja a legjobb futtatást és a hozzá tartozó betanított modellt.

```python
best_run, fitted_model = remote_run.get_output()
```
A legjobb modell paramétereit egyszerűen a fitted_model kiíratásával láthatja, és a legjobb modell tulajdonságait a [get_properties()](https://docs.microsoft.com/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py#azureml_core_Run_get_properties?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) metódus segítségével tekintheti meg.

```python
best_run.get_properties()
```

Most regisztrálja a modellt a [register_model](https://docs.microsoft.com/python/api/azureml-train-automl-client/azureml.train.automl.run.automlrun?view=azure-ml-py#register-model-model-name-none--description-none--tags-none--iteration-none--metric-none-?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) metódussal.
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
### 3.2 Modell telepítése

Miután a legjobb modell mentésre került, telepíthetjük az [InferenceConfig](https://docs.microsoft.com/python/api/azureml-core/azureml.core.model.inferenceconfig?view=azure-ml-py?ocid=AID3041109) osztály segítségével. Az InferenceConfig a telepítéshez használt egyedi környezet konfigurációs beállításait képviseli. Az [AciWebservice](https://docs.microsoft.com/python/api/azureml-core/azureml.core.webservice.aciwebservice?view=azure-ml-py) osztály egy gépi tanulási modellt képvisel, amely webszolgáltatás végpontként van telepítve az Azure Container Instances-en. A telepített szolgáltatás egy terheléselosztott, HTTP végpont REST API-val. Adatokat küldhetünk ennek az API-nak, és megkapjuk a modell által visszaadott előrejelzést.

A modellt a [deploy](https://docs.microsoft.com/python/api/azureml-core/azureml.core.model(class)?view=azure-ml-py#deploy-workspace--name--models--inference-config-none--deployment-config-none--deployment-target-none--overwrite-false--show-output-false-?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) metódussal telepíthetjük.

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
Ez a lépés néhány percet igénybe vehet.

### 3.3 Végpont fogyasztása


```python
response = aci_service.run(input_data=test_sample)
response
```
Ennek az eredménye `'{"result": [false]}'` kell legyen. Ez azt jelenti, hogy a végponthoz küldött betegadatok alapján a predikció `false`, vagyis ez a személy valószínűleg nem kap szívrohamot.

Gratulálok! Most sikeresen felhasználtad az Azure ML-en az Azure ML SDK-val betanított és telepített modellt!

> **_MEGJEGYZÉS:_** Miután befejezted a projektet, ne felejtsd el törölni az összes erőforrást.

## 🚀 Kihívás

Az SDK-val még rengeteg más dolgot is megtehetsz, de sajnos nem tudunk mindent átvenni ebben a leckében. Jó hír viszont, hogy ha megtanulsz eligazodni az SDK dokumentációjában, az nagyban segíthet önállóan is. Nézd meg az Azure ML SDK dokumentációját, és keresd meg a `Pipeline` osztályt, amely lehetővé teszi, hogy folyamatokat hozz létre. Egy Pipeline lépések gyűjteménye, amelyeket egy munkafolyamatként lehet végrehajtani.

**TIPP:** Látogass el az [SDK dokumentációba](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109), és írj be kulcsszavakat a keresősávba, például "Pipeline". A keresési eredmények között meg kell találnod az `azureml.pipeline.core.Pipeline` osztályt.

## [Óra utáni kvíz](https://ff-quizzes.netlify.app/en/ds/)

## Áttekintés és önálló tanulás

Ebben a leckében megtanultad, hogyan kell betanítani, telepíteni és használni egy modellt, amely a szívelégtelenség kockázatát jósolja az Azure ML SDK-val a felhőben. További információért az Azure ML SDK-ról nézd meg ezt a [dokumentációt](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109). Próbálj meg saját modellt létrehozni az Azure ML SDK-val.

## Feladat

[Adattudományi projekt az Azure ML SDK-val](assignment.md)

---

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.