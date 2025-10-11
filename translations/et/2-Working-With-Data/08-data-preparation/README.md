<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1b560955ff39a2bcf2a049fce474a951",
  "translation_date": "2025-10-11T15:21:34+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "et"
}
-->
# Töötamine andmetega: Andmete ettevalmistamine

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Andmete ettevalmistamine - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Eelloengu viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/14)

Sõltuvalt allikast võivad toorandmed sisaldada ebakõlasid, mis tekitavad analüüsimisel ja modelleerimisel probleeme. Teisisõnu, selliseid andmeid võib pidada "räpasteks" ja need tuleb puhastada. Selles õppetükis keskendutakse tehnikatele, mis aitavad andmeid puhastada ja muuta, et lahendada puuduvate, ebatäpsete või mittetäielike andmete probleeme. Õppetükis käsitletavad teemad kasutavad Pythonit ja Pandase teeki ning neid [näidatakse märkmikus](notebook.ipynb) selles kataloogis.

## Andmete puhastamise tähtsus

- **Lihtne kasutada ja taaskasutada**: Kui andmed on korralikult organiseeritud ja normaliseeritud, on neid lihtsam otsida, kasutada ja teistega jagada.

- **Järjepidevus**: Andmeteadus nõuab sageli mitme andmekogumiga töötamist, kus erinevatest allikatest pärit andmekogumid tuleb ühendada. Veendudes, et iga üksik andmekogum on standardiseeritud, tagatakse, et andmed on kasulikud ka siis, kui need kõik ühte andmekogumisse ühendatakse.

- **Mudeli täpsus**: Puhastatud andmed parandavad mudelite täpsust, mis neile tuginevad.

## Tavalised puhastamise eesmärgid ja strateegiad

- **Andmekogumi uurimine**: Andmete uurimine, mida käsitletakse [hilisemas õppetükis](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), aitab avastada andmeid, mida tuleb puhastada. Andmekogumi väärtuste visuaalne vaatlemine võib luua ootusi selle kohta, milline ülejäänud andmekogum välja näeb, või anda aimu probleemidest, mida saab lahendada. Uurimine võib hõlmata lihtsaid päringuid, visualiseeringuid ja proovivõtteid.

- **Formaatimine**: Sõltuvalt allikast võivad andmed olla esitatud ebajärjekindlalt. See võib tekitada probleeme väärtuste otsimisel ja esitamisel, kus väärtus on küll andmekogumis olemas, kuid ei ole korralikult visualiseeritud või päringutulemustes esitatud. Tavalised formaatimisprobleemid hõlmavad tühikute, kuupäevade ja andmetüüpide lahendamist. Formaatimisprobleemide lahendamine on tavaliselt andmete kasutajate ülesanne. Näiteks kuupäevade ja numbrite esitamise standardid võivad riigiti erineda.

- **Duplikaadid**: Andmed, millel on rohkem kui üks esinemine, võivad anda ebatäpseid tulemusi ja tavaliselt tuleks need eemaldada. See on tavaline probleem, kui ühendada kaks või enam andmekogumit. Siiski on juhtumeid, kus ühendatud andmekogumite duplikaadid sisaldavad lisainfot, mida võib olla vaja säilitada.

- **Puuduvad andmed**: Puuduvad andmed võivad põhjustada ebatäpsusi ning nõrku või kallutatud tulemusi. Mõnikord saab neid lahendada andmete "taaslaadimisega", puuduvate väärtuste täitmisega arvutuste ja koodiga nagu Python, või lihtsalt väärtuse ja vastava andme eemaldamisega. Puuduvate andmete põhjused võivad olla mitmesugused ja nende lahendamise meetodid sõltuvad sellest, kuidas ja miks need kaduma läksid.

## DataFrame'i teabe uurimine
> **Õppimise eesmärk:** Selle alajaotuse lõpuks peaksite olema mugav üldise teabe leidmisel pandas DataFrame'ides salvestatud andmete kohta.

Kui olete oma andmed Pandasesse laadinud, on need tõenäoliselt DataFrame'is (vaadake eelmist [õppetundi](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) üksikasjaliku ülevaate saamiseks). Kuid kui teie DataFrame'is on 60 000 rida ja 400 veergu, kuidas te üldse alustate arusaamist, millega te töötate? Õnneks pakub [pandas](https://pandas.pydata.org/) mugavaid tööriistu, et kiiresti vaadata DataFrame'i üldist teavet, samuti esimesi ja viimaseid ridu.

Selle funktsionaalsuse uurimiseks impordime Python scikit-learn teegi ja kasutame ikoonilist andmekogumit: **Irise andmekogumit**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |sepal length (cm)|sepal width (cm)|petal length (cm)|petal width (cm)|
|----------------------------------------|-----------------|----------------|-----------------|----------------|
|0                                       |5.1              |3.5             |1.4              |0.2             |
|1                                       |4.9              |3.0             |1.4              |0.2             |
|2                                       |4.7              |3.2             |1.3              |0.2             |
|3                                       |4.6              |3.1             |1.5              |0.2             |
|4                                       |5.0              |3.6             |1.4              |0.2             |

- **DataFrame.info**: Alustuseks kasutatakse `info()` meetodit, et printida kokkuvõte DataFrame'is olevast sisust. Vaatame seda andmekogumit, et näha, mis meil on:
```python
iris_df.info()
```
```
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
dtypes: float64(4)
memory usage: 4.8 KB
```
Sellest saame teada, et *Irise* andmekogumis on 150 kirjet neljas veerus, kus puuduvad nullkirjed. Kõik andmed on salvestatud 64-bitiste ujukomaarvudena.

- **DataFrame.head()**: Järgmiseks, et kontrollida DataFrame'i tegelikku sisu, kasutame `head()` meetodit. Vaatame, millised näevad välja meie `iris_df` esimesed read:
```python
iris_df.head()
```
```
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
```
- **DataFrame.tail()**: Vastupidiselt, et kontrollida DataFrame'i viimaseid ridu, kasutame `tail()` meetodit:
```python
iris_df.tail()
```
```
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
145                6.7               3.0                5.2               2.3
146                6.3               2.5                5.0               1.9
147                6.5               3.0                5.2               2.0
148                6.2               3.4                5.4               2.3
149                5.9               3.0                5.1               1.8
```
> **Järeldus:** Juba lihtsalt vaadates DataFrame'i metaandmeid või esimesi ja viimaseid väärtusi, saate kohe aimu andmete suurusest, kujust ja sisust, millega tegelete.

## Puuduvate andmete käsitlemine
> **Õppimise eesmärk:** Selle alajaotuse lõpuks peaksite teadma, kuidas asendada või eemaldada nullväärtusi DataFrame'idest.

Enamasti on andmekogumites, mida soovite kasutada (või peate kasutama), puuduvaid väärtusi. Puuduvate andmete käsitlemine toob kaasa peened kompromissid, mis võivad mõjutada teie lõplikku analüüsi ja reaalse maailma tulemusi.

Pandas käsitleb puuduvaid väärtusi kahel viisil. Esimene, mida olete näinud varasemates osades, on `NaN` ehk Not a Number. See on tegelikult eriväärtus, mis on osa IEEE ujukomaarvu spetsifikatsioonist ja seda kasutatakse ainult puuduvate ujukomaarvude tähistamiseks.

Muude kui ujukomaarvude puuduvate väärtuste jaoks kasutab pandas Python `None` objekti. Kuigi võib tunduda segane, et kohtate kahte erinevat tüüpi väärtusi, mis sisuliselt tähendavad sama asja, on selle disainivaliku taga kindlad programmilised põhjused ja praktikas võimaldab see Pandasel pakkuda head kompromissi enamiku juhtumite jaoks. Sellegipoolest on nii `None` kui ka `NaN` piirangud, mida peate arvestama nende kasutamise osas.

Lugege rohkem `NaN` ja `None` kohta [märkmikust](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Nullväärtuste tuvastamine**: Pandases on `isnull()` ja `notnull()` meetodid peamised vahendid nullandmete tuvastamiseks. Mõlemad tagastavad Boole'i maskid teie andmete kohta. Kasutame `numpy` `NaN` väärtuste jaoks:
```python
import numpy as np

example1 = pd.Series([0, np.nan, '', None])
example1.isnull()
```
```
0    False
1     True
2    False
3     True
dtype: bool
```
Vaadake väljundit tähelepanelikult. Kas miski üllatab teid? Kuigi `0` on aritmeetiline null, on see siiski täiesti sobiv täisarv ja pandas käsitleb seda sellisena. `''` on veidi peenem. Kuigi kasutasime seda 1. osas tühja stringiväärtuse tähistamiseks, on see siiski stringiobjekt ja pandas ei käsitle seda nullina.

Nüüd pöörame selle ümber ja kasutame neid meetodeid viisil, nagu te neid praktikas kasutate. Boole'i maske saab kasutada otse ``Series`` või ``DataFrame`` indeksina, mis on kasulik, kui proovite töötada eraldatud puuduvate (või olemasolevate) väärtustega.

> **Järeldus**: Nii `isnull()` kui ka `notnull()` meetodid annavad sarnaseid tulemusi, kui kasutate neid `DataFrame`-ides: need näitavad tulemusi ja nende tulemuste indeksi, mis aitab teid tohutult, kui tegelete oma andmetega.

- **Nullväärtuste eemaldamine**: Lisaks puuduvate väärtuste tuvastamisele pakub pandas mugavat viisi nullväärtuste eemaldamiseks `Series` ja `DataFrame`-idest. (Eriti suurte andmekogumite puhul on sageli soovitatav lihtsalt eemaldada puuduvad [NA] väärtused oma analüüsist, mitte tegeleda nendega muul viisil.) Vaatame seda tegevuses, pöördudes tagasi `example1` juurde:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Pange tähele, et see peaks välja nägema nagu teie väljund `example3[example3.notnull()]`. Erinevus seisneb selles, et `dropna` on eemaldanud need puuduvad väärtused `Series`-ist `example1`.

Kuna `DataFrame`-idel on kaks mõõdet, pakuvad need rohkem võimalusi andmete eemaldamiseks.

```python
example2 = pd.DataFrame([[1,      np.nan, 7], 
                         [2,      5,      8], 
                         [np.nan, 6,      9]])
example2
```
|      | 0 | 1 | 2 |
|------|---|---|---|
|0     |1.0|NaN|7  |
|1     |2.0|5.0|8  |
|2     |NaN|6.0|9  |

(Kas märkasite, et pandas muutis kaks veergu ujukomaarvudeks, et mahutada `NaN`-id?)

Te ei saa `DataFrame`-ist eemaldada üksikut väärtust, seega peate eemaldama terveid ridu või veerge. Sõltuvalt sellest, mida te teete, võite soovida teha üht või teist, ja pandas annab teile mõlemaks võimaluse. Kuna andmeteaduses esindavad veerud üldiselt muutujaid ja read vaatlusi, on tõenäolisem, et eemaldate andmeridu; `dropna()` vaikeseade on eemaldada kõik read, mis sisaldavad nullväärtusi:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Kui vaja, saate eemaldada NA väärtused veergudest. Kasutage selleks `axis=1`:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Pange tähele, et see võib eemaldada palju andmeid, mida võiksite säilitada, eriti väiksemates andmekogumites. Mis siis, kui soovite eemaldada ainult read või veerud, mis sisaldavad mitmeid või isegi kõiki nullväärtusi? Need seaded saate määrata `dropna` abil `how` ja `thresh` parameetrites.

Vaikimisi on `how='any'` (kui soovite ise kontrollida või näha, millised muud parameetrid meetodil on, käivitage `example4.dropna?` koodirakus). Võite alternatiivselt määrata `how='all'`, et eemaldada ainult read või veerud, mis sisaldavad kõiki nullväärtusi. Laiendame oma näidet `DataFrame`, et näha seda tegevuses.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

`thresh` parameeter annab teile peenema kontrolli: määrate mitme *mitte-null* väärtuse arvu, mida rida või veerg peab sisaldama, et seda säilitada:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Siin on esimene ja viimane rida eemaldatud, kuna need sisaldavad ainult kahte mitte-null väärtust.

- **Nullväärtuste täitmine**: Sõltuvalt teie andmekogumist võib mõnikord olla mõistlikum täita nullväärtused kehtivate väärtustega, mitte neid eemaldada. Võiksite kasutada `isnull`, et seda kohapeal teha, kuid see võib olla töömahukas, eriti kui teil on palju väärtusi, mida täita. Kuna see on andmeteaduses nii levinud ülesanne, pakub pandas `fillna`, mis tagastab koopia `Series` või `DataFrame`-ist, kus puuduvad väärtused on asendatud teie valitud väärtusega. Loome veel ühe näite `Series`, et näha, kuidas see praktikas töötab.
```python
example3 = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
example3
```
```
a    1.0
b    NaN
c    2.0
d    NaN
e    3.0
dtype: float64
```
Saate täita kõik nullkirjed ühe väärtusega, näiteks `0`:
```python
example3.fillna(0)
```
```
a    1.0
b    0.0
c    2.0
d    0.0
e    3.0
dtype: float64
```
Saate **edasi täita** nullväärtused, kasutades viimast kehtivat väärtust nulli täitmiseks:
```python
example3.fillna(method='ffill')
```
```
a    1.0
b    1.0
c    2.0
d    2.0
e    3.0
dtype: float64
```
Samuti saate **tagasi täita**, et levitada järgmist kehtivat väärtust tagasi nulli täitmiseks:
```python
example3.fillna(method='bfill')
```
```
a    1.0
b    2.0
c    2.0
d    3.0
e    3.0
dtype: float64
```
Nagu võite arvata, töötab see sama moodi `DataFrame`-idega, kuid saate määrata ka `axis`, mille järgi nullväärtusi täita. Kasutades taas varem kasutatud `example2`:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Pange tähele, et kui eelmine väärtus ei ole saadaval edasi täitmiseks, jääb nullväärtus alles.
> **Peamine mõte:** Puuduvate väärtuste käsitlemiseks andmekogumites on mitmeid viise. Konkreetne strateegia (nende eemaldamine, asendamine või isegi asendamise viis) peaks olema määratud andmete eripärade järgi. Mida rohkem te andmekogumitega töötate ja nendega suhtlete, seda paremini õpite puuduvate väärtustega toime tulema.

## Duplikaatandmete eemaldamine

> **Õppimise eesmärk:** Selle alajaotuse lõpuks peaksite olema kindel, kuidas tuvastada ja eemaldada duplikaatväärtusi DataFrame'ist.

Lisaks puuduvatele andmetele kohtate päriselu andmekogumites sageli ka duplikaatandmeid. Õnneks pakub `pandas` lihtsat viisi duplikaatkirjete tuvastamiseks ja eemaldamiseks.

- **Duplikaatide tuvastamine: `duplicated`**: Duplikaatväärtusi saab hõlpsasti tuvastada pandas meetodiga `duplicated`, mis tagastab Boole'i maski, mis näitab, kas `DataFrame`-i kirje on varasema kirje duplikaat. Loome veel ühe näidis-`DataFrame`i, et seda tegevuses näha.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |tähed  |numbrid|
|------|-------|-------|
|0     |A      |1      |
|1     |B      |2      |
|2     |A      |1      |
|3     |B      |3      |
|4     |B      |3      |

```python
example4.duplicated()
```
```
0    False
1    False
2     True
3    False
4     True
dtype: bool
```
- **Duplikaatide eemaldamine: `drop_duplicates`:** tagastab lihtsalt koopia andmetest, kus kõik `duplicated` väärtused on `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Nii `duplicated` kui ka `drop_duplicates` vaikimisi arvestavad kõiki veerge, kuid saate määrata, et nad uuriksid ainult `DataFrame`i veergude alamhulka:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Peamine mõte:** Duplikaatandmete eemaldamine on oluline osa peaaegu igast andmeteaduse projektist. Duplikaatandmed võivad analüüsi tulemusi muuta ja anda ebatäpseid tulemusi!


## 🚀 Väljakutse

Kõik käsitletud materjalid on saadaval [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb) kujul. Lisaks on igas jaotises harjutused, proovige neid kindlasti!

## [Loengu järgne viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/15)



## Ülevaade ja iseseisev õppimine

Andmete ettevalmistamiseks analüüsiks ja modelleerimiseks on palju viise ning andmete puhastamine on oluline samm, mis nõuab praktilist lähenemist. Proovige neid Kaggle väljakutseid, et uurida tehnikaid, mida selles õppetükis ei käsitletud.

- [Andmete puhastamise väljakutse: kuupäevade parsimine](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Andmete puhastamise väljakutse: andmete skaleerimine ja normaliseerimine](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Ülesanne

[Andmete hindamine vormilt](assignment.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta arusaamatuste või valesti tõlgenduste eest, mis võivad tekkida selle tõlke kasutamise tõttu.