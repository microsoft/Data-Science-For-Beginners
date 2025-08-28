<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3ade580a06b5f04d57cc83a768a8fb77",
  "translation_date": "2025-08-28T02:29:45+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "tl"
}
-->
# Paggawa gamit ang Data: Paghahanda ng Datos

|![ Sketchnote ni [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Paghahanda ng Datos - _Sketchnote ni [@nitya](https://twitter.com/nitya)_ |

## [Pre-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

Depende sa pinagmulan nito, ang raw na datos ay maaaring maglaman ng ilang mga inconsistency na magdudulot ng hamon sa pagsusuri at pagmomodelo. Sa madaling salita, ang datos na ito ay maaaring ituring na "marumi" at kailangang linisin. Ang araling ito ay nakatuon sa mga teknik para sa paglilinis at pagbabago ng datos upang matugunan ang mga hamon ng nawawala, hindi tama, o hindi kumpletong datos. Ang mga paksang saklaw sa araling ito ay gagamit ng Python at ang Pandas library at [ipapakita sa notebook](notebook.ipynb) sa loob ng direktoryong ito.

## Ang kahalagahan ng paglilinis ng datos

- **Madaling gamitin at muling gamitin**: Kapag ang datos ay maayos na nakaayos at na-normalize, mas madali itong hanapin, gamitin, at ibahagi sa iba.

- **Pagkakapare-pareho**: Ang agham ng datos ay madalas na nangangailangan ng paggamit ng higit sa isang dataset, kung saan ang mga dataset mula sa iba't ibang pinagmulan ay kailangang pagsamahin. Ang pagtiyak na ang bawat indibidwal na dataset ay may karaniwang standardisasyon ay magtitiyak na ang datos ay kapaki-pakinabang pa rin kapag pinagsama-sama sa isang dataset.

- **Katumpakan ng modelo**: Ang datos na nalinis ay nagpapabuti sa katumpakan ng mga modelong umaasa dito.

## Karaniwang layunin at estratehiya sa paglilinis

- **Paggalugad ng dataset**: Ang paggalugad ng datos, na saklaw sa [susunod na aralin](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), ay makakatulong sa iyo na matuklasan ang datos na kailangang linisin. Ang visual na pagmamasid sa mga halaga sa loob ng dataset ay maaaring magtakda ng mga inaasahan kung ano ang magiging hitsura ng natitirang bahagi nito, o magbigay ng ideya sa mga problemang maaaring malutas. Ang paggalugad ay maaaring magsangkot ng mga simpleng query, visualisasyon, at sampling.

- **Pag-format**: Depende sa pinagmulan, ang datos ay maaaring magkaroon ng mga inconsistency sa kung paano ito ipinapakita. Maaari itong magdulot ng problema sa paghahanap at representasyon ng halaga, kung saan ito nakikita sa loob ng dataset ngunit hindi maayos na naipapakita sa mga visualisasyon o resulta ng query. Ang mga karaniwang problema sa pag-format ay kinabibilangan ng pag-aayos ng whitespace, petsa, at mga uri ng datos. Ang pag-aayos ng mga isyu sa pag-format ay karaniwang responsibilidad ng mga gumagamit ng datos. Halimbawa, ang mga pamantayan sa kung paano ipinapakita ang mga petsa at numero ay maaaring magkaiba sa bawat bansa.

- **Pagdoble**: Ang datos na may higit sa isang paglitaw ay maaaring magdulot ng hindi tamang resulta at karaniwang kailangang alisin. Ito ay karaniwang nangyayari kapag pinagsama ang dalawa o higit pang mga dataset. Gayunpaman, may mga pagkakataon kung saan ang pagdoble sa pinagsamang mga dataset ay naglalaman ng mga piraso na maaaring magbigay ng karagdagang impormasyon at maaaring kailangang panatilihin.

- **Nawawalang Datos**: Ang nawawalang datos ay maaaring magdulot ng hindi tamang resulta pati na rin mahina o bias na mga resulta. Minsan ang mga ito ay maaaring malutas sa pamamagitan ng "reload" ng datos, pagpuno sa nawawalang mga halaga gamit ang computation at code tulad ng Python, o simpleng pag-aalis ng halaga at kaukulang datos. Maraming dahilan kung bakit nawawala ang datos, at ang mga aksyon na ginagawa upang malutas ang mga nawawalang halaga ay maaaring depende sa kung paano at bakit ito nawala.

## Paggalugad ng impormasyon ng DataFrame
> **Layunin ng pag-aaral:** Sa pagtatapos ng bahaging ito, dapat kang komportable sa paghahanap ng pangkalahatang impormasyon tungkol sa datos na nakaimbak sa pandas DataFrames.

Kapag na-load mo na ang iyong datos sa pandas, malamang na ito ay nasa isang DataFrame (tingnan ang nakaraang [aralin](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) para sa detalyadong overview). Gayunpaman, kung ang dataset sa iyong DataFrame ay may 60,000 na mga row at 400 na mga column, paano mo sisimulan ang pag-unawa sa kung ano ang iyong pinagtatrabahuhan? Sa kabutihang-palad, ang [pandas](https://pandas.pydata.org/) ay nagbibigay ng ilang maginhawang tools upang mabilis na makita ang pangkalahatang impormasyon tungkol sa isang DataFrame bukod pa sa unang ilang at huling ilang mga row.

Upang galugarin ang functionality na ito, mag-i-import tayo ng Python scikit-learn library at gagamit ng isang iconic na dataset: ang **Iris dataset**.

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

- **DataFrame.info**: Upang magsimula, ang `info()` method ay ginagamit upang mag-print ng buod ng nilalaman na nasa isang `DataFrame`. Tingnan natin ang dataset na ito upang makita kung ano ang mayroon tayo:
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
Mula dito, nalaman natin na ang *Iris* dataset ay may 150 entries sa apat na column na walang null entries. Ang lahat ng datos ay nakaimbak bilang 64-bit floating-point numbers.

- **DataFrame.head()**: Susunod, upang suriin ang aktwal na nilalaman ng `DataFrame`, ginagamit natin ang `head()` method. Tingnan natin kung ano ang hitsura ng unang ilang row ng ating `iris_df`:
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
- **DataFrame.tail()**: Sa kabaligtaran, upang suriin ang huling ilang row ng `DataFrame`, ginagamit natin ang `tail()` method:
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
> **Takeaway:** Kahit sa simpleng pagtingin lamang sa metadata tungkol sa impormasyon sa isang DataFrame o sa unang at huling ilang mga halaga nito, maaari kang magkaroon ng agarang ideya tungkol sa laki, hugis, at nilalaman ng datos na iyong pinagtatrabahuhan.

## Pagtugon sa Nawawalang Datos
> **Layunin ng pag-aaral:** Sa pagtatapos ng bahaging ito, dapat mong malaman kung paano palitan o alisin ang mga null na halaga mula sa DataFrames.

Kadalasan, ang mga dataset na nais mong gamitin (o kailangang gamitin) ay may mga nawawalang halaga. Ang paraan ng paghawak sa nawawalang datos ay may kasamang mga banayad na tradeoffs na maaaring makaapekto sa iyong huling pagsusuri at mga resulta sa totoong mundo.

Ang pandas ay humahawak sa nawawalang mga halaga sa dalawang paraan. Ang una ay nakita mo na sa mga nakaraang seksyon: `NaN`, o Not a Number. Ito ay isang espesyal na halaga na bahagi ng IEEE floating-point specification at ginagamit lamang upang ipahiwatig ang nawawalang floating-point values.

Para sa nawawalang mga halaga bukod sa floats, ang pandas ay gumagamit ng Python `None` object. Bagama't maaaring mukhang nakakalito na makakakita ka ng dalawang magkaibang uri ng mga halaga na nagsasabi ng halos pareho, may mga tunog na programmatic na dahilan para sa disenyo na ito, at sa pagsasanay, ang ganitong ruta ay nagbibigay-daan sa pandas na maghatid ng magandang kompromiso para sa karamihan ng mga kaso. Gayunpaman, ang parehong `None` at `NaN` ay may mga limitasyon na kailangan mong tandaan tungkol sa kung paano sila magagamit.

Tingnan ang higit pa tungkol sa `NaN` at `None` mula sa [notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Pag-detect ng null na mga halaga**: Sa `pandas`, ang `isnull()` at `notnull()` methods ang iyong pangunahing paraan para sa pag-detect ng null na datos. Parehong nagbabalik ng Boolean masks sa iyong datos. Gagamitin natin ang `numpy` para sa `NaN` values:
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
Tingnan nang mabuti ang output. Mayroon bang anumang nagulat sa iyo? Bagama't ang `0` ay isang arithmetic null, ito ay gayunpaman isang perpektong integer at tinatrato ito ng pandas bilang ganoon. Ang `''` ay medyo mas banayad. Bagama't ginamit natin ito sa Seksyon 1 upang kumatawan sa isang walang laman na string value, ito ay gayunpaman isang string object at hindi isang representasyon ng null ayon sa pandas.

Ngayon, baliktarin natin ito at gamitin ang mga method na ito sa paraang mas katulad ng gagamitin mo sa pagsasanay. Maaari mong gamitin ang Boolean masks nang direkta bilang isang ``Series`` o ``DataFrame`` index, na maaaring maging kapaki-pakinabang kapag sinusubukang magtrabaho sa mga nakahiwalay na nawawala (o naroroon) na mga halaga.

> **Takeaway**: Parehong ang `isnull()` at `notnull()` methods ay gumagawa ng magkatulad na resulta kapag ginamit mo ang mga ito sa `DataFrame`s: ipinapakita nila ang mga resulta at ang index ng mga resulta, na makakatulong sa iyo nang malaki habang nakikipagbuno ka sa iyong datos.

- **Pag-aalis ng null na mga halaga**: Bukod sa pagtukoy sa nawawalang mga halaga, ang pandas ay nagbibigay ng maginhawang paraan upang alisin ang mga null na halaga mula sa `Series` at `DataFrame`s. (Lalo na sa malalaking dataset, mas maipapayo na alisin na lang ang nawawalang [NA] na mga halaga mula sa iyong pagsusuri kaysa harapin ang mga ito sa ibang paraan.) Upang makita ito sa aksyon, bumalik tayo sa `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Pansinin na dapat itong magmukhang iyong output mula sa `example3[example3.notnull()]`. Ang pagkakaiba dito ay, sa halip na i-index lamang ang mga masked na halaga, inalis ng `dropna` ang mga nawawalang halaga mula sa `Series` `example1`.

Dahil ang `DataFrame`s ay may dalawang dimensyon, nagbibigay sila ng mas maraming opsyon para sa pag-aalis ng datos.

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

(Napansin mo ba na ang pandas ay nag-upcast sa dalawang column sa floats upang mapa-accommodate ang `NaN`s?)

Hindi mo maaaring alisin ang isang solong halaga mula sa isang `DataFrame`, kaya kailangan mong alisin ang buong mga row o column. Depende sa kung ano ang iyong ginagawa, maaaring gusto mong gawin ang isa o ang isa pa, kaya binibigyan ka ng pandas ng mga opsyon para sa pareho. Dahil sa agham ng datos, ang mga column ay karaniwang kumakatawan sa mga variable at ang mga row ay kumakatawan sa mga obserbasyon, mas malamang na alisin mo ang mga row ng datos; ang default na setting para sa `dropna()` ay alisin ang lahat ng mga row na naglalaman ng anumang null na mga halaga:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Kung kinakailangan, maaari mong alisin ang mga NA na halaga mula sa mga column. Gamitin ang `axis=1` upang gawin ito:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Pansinin na maaari itong mag-alis ng maraming datos na maaaring gusto mong panatilihin, lalo na sa mas maliliit na dataset. Paano kung gusto mo lang alisin ang mga row o column na naglalaman ng ilang o kahit lahat ng null na mga halaga? Tukuyin mo ang mga setting na iyon sa `dropna` gamit ang `how` at `thresh` parameters.

Sa default, `how='any'` (kung gusto mong suriin para sa iyong sarili o makita kung ano ang iba pang mga parameter na mayroon ang method, patakbuhin ang `example4.dropna?` sa isang code cell). Maaari mo ring tukuyin ang `how='all'` upang alisin lamang ang mga row o column na naglalaman ng lahat ng null na mga halaga. Palawakin natin ang halimbawa ng `DataFrame` upang makita ito sa aksyon.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

Ang `thresh` parameter ay nagbibigay sa iyo ng mas pinong kontrol: itinatakda mo ang bilang ng *non-null* na mga halaga na kailangang magkaroon ng isang row o column upang mapanatili:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Dito, ang unang at huling row ay inalis, dahil naglalaman lamang sila ng dalawang non-null na mga halaga.

- **Pagpuno ng null na mga halaga**: Depende sa iyong dataset, minsan mas may katuturan na punan ang mga null na halaga ng mga valid na halaga kaysa alisin ang mga ito. Maaari mong gamitin ang `isnull` upang gawin ito sa lugar, ngunit maaaring nakakapagod ito, lalo na kung marami kang mga halaga na kailangang punan. Dahil ito ay isang karaniwang gawain sa agham ng datos, ang pandas ay nagbibigay ng `fillna`, na nagbabalik ng kopya ng `Series` o `DataFrame` na may mga nawawalang halaga na pinalitan ng isa sa iyong pinili. Gumawa tayo ng isa pang halimbawa ng `Series` upang makita kung paano ito gumagana sa pagsasanay.
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
Maaari mong punan ang lahat ng mga null na entry gamit ang isang solong halaga, tulad ng `0`:
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
Maaari mong **forward-fill** ang mga null na halaga, na ang ibig sabihin ay gamitin ang huling valid na halaga upang punan ang null:
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
Maaari mo ring **back-fill** upang ipalaganap ang susunod na valid na halaga pabalik upang punan ang null:
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
Tulad ng iyong inaasahan, gumagana ito nang pareho sa `DataFrame`s, ngunit maaari mo ring tukuyin ang isang `axis` kung saan pupunan ang mga null na halaga. Gamitin muli ang `example2` na ginamit dati:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Pansinin na kapag ang isang nakaraang halaga ay hindi magagamit para sa forward-filling, nananatili ang null na halaga.
> **Pangunahing Punto:** Maraming paraan upang harapin ang mga nawawalang halaga sa iyong mga dataset. Ang partikular na estratehiya na gagamitin mo (pag-aalis, pagpapalit, o kung paano mo papalitan ang mga ito) ay dapat nakabatay sa mga detalye ng data. Mas magkakaroon ka ng mas mahusay na pag-unawa kung paano harapin ang mga nawawalang halaga habang mas madalas kang humawak at makipag-ugnayan sa mga dataset.

## Pag-aalis ng mga Dobleng Data

> **Layunin ng Pag-aaral:** Sa pagtatapos ng bahaging ito, dapat kang maging komportable sa pagtukoy at pag-aalis ng mga dobleng halaga mula sa mga DataFrame.

Bukod sa nawawalang data, madalas kang makakakita ng mga dobleng data sa mga totoong dataset. Sa kabutihang-palad, ang `pandas` ay nagbibigay ng madaling paraan upang matukoy at alisin ang mga dobleng entry.

- **Pagtukoy sa mga Doble: `duplicated`**: Madali mong matutukoy ang mga dobleng halaga gamit ang `duplicated` na pamamaraan sa pandas, na nagbabalik ng Boolean mask na nagpapakita kung ang isang entry sa `DataFrame` ay doble ng naunang entry. Gumawa tayo ng isa pang halimbawa ng `DataFrame` upang makita ito sa aksyon.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |letters|numbers|
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
- **Pag-aalis ng mga Doble: `drop_duplicates`:** simpleng nagbabalik ng kopya ng data kung saan lahat ng mga `duplicated` na halaga ay `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Ang parehong `duplicated` at `drop_duplicates` ay default na isinasaalang-alang ang lahat ng mga column, ngunit maaari mong tukuyin na suriin lamang nila ang isang subset ng mga column sa iyong `DataFrame`:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Pangunahing Punto:** Ang pag-aalis ng mga dobleng data ay mahalagang bahagi ng halos bawat proyekto sa agham ng datos. Ang mga dobleng data ay maaaring magbago ng resulta ng iyong mga pagsusuri at magbigay ng hindi tamang resulta!

## 🚀 Hamon

Ang lahat ng tinalakay na materyales ay ibinigay bilang isang [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Bukod dito, may mga pagsasanay pagkatapos ng bawat seksyon, subukan ang mga ito!

## [Post-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/15)

## Pagsusuri at Sariling Pag-aaral

Maraming paraan upang matuklasan at lapitan ang paghahanda ng iyong data para sa pagsusuri at pagmomodelo, at ang paglilinis ng data ay isang mahalagang hakbang na nangangailangan ng "hands-on" na karanasan. Subukan ang mga hamon mula sa Kaggle upang tuklasin ang mga teknik na hindi natalakay sa araling ito.

- [Data Cleaning Challenge: Parsing Dates](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Data Cleaning Challenge: Scale and Normalize Data](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)

## Takdang-Aralin

[Pag-evaluate ng Data mula sa isang Form](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.