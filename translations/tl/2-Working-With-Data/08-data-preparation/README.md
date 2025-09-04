<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90a815d332aea41a222f4c6372e7186e",
  "translation_date": "2025-09-04T20:58:13+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "tl"
}
-->
# Paggawa gamit ang Data: Paghahanda ng Data

|![ Sketchnote ni [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Paghahanda ng Data - _Sketchnote ni [@nitya](https://twitter.com/nitya)_ |

## [Pre-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

Depende sa pinagmulan nito, ang raw data ay maaaring maglaman ng ilang mga inconsistency na magdudulot ng hamon sa pagsusuri at pagmomodelo. Sa madaling salita, ang data na ito ay maaaring ituring na "marumi" at kailangang linisin. Ang araling ito ay nakatuon sa mga teknik para sa paglilinis at pagbabago ng data upang matugunan ang mga hamon ng nawawala, hindi tama, o hindi kumpletong data. Ang mga paksang saklaw sa araling ito ay gagamit ng Python at ang Pandas library at ipapakita sa [notebook](notebook.ipynb) sa loob ng direktoryong ito.

## Ang kahalagahan ng paglilinis ng data

- **Madaling gamitin at muling gamitin**: Kapag ang data ay maayos na nakaayos at na-normalize, mas madali itong hanapin, gamitin, at ibahagi sa iba.

- **Pagkakapare-pareho**: Ang data science ay madalas na nangangailangan ng paggamit ng higit sa isang dataset, kung saan ang mga dataset mula sa iba't ibang pinagmulan ay kailangang pagsamahin. Ang pagtiyak na ang bawat indibidwal na dataset ay may karaniwang pamantayan ay magtitiyak na ang data ay kapaki-pakinabang pa rin kapag pinagsama-sama sa isang dataset.

- **Katumpakan ng modelo**: Ang data na nalinis ay nagpapabuti sa katumpakan ng mga modelong umaasa dito.

## Karaniwang layunin at estratehiya sa paglilinis

- **Paggalugad ng dataset**: Ang paggalugad ng data, na saklaw sa [susunod na aralin](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), ay makakatulong sa iyo na matuklasan ang data na kailangang linisin. Ang visual na pagmamasid sa mga halaga sa loob ng dataset ay maaaring magtakda ng mga inaasahan kung ano ang hitsura ng natitirang bahagi nito, o magbigay ng ideya ng mga problemang maaaring malutas. Ang paggalugad ay maaaring magsangkot ng mga pangunahing query, visualizations, at sampling.

- **Pag-format**: Depende sa pinagmulan, ang data ay maaaring magkaroon ng mga inconsistency sa kung paano ito ipinapakita. Maaari itong magdulot ng mga problema sa paghahanap at representasyon ng halaga, kung saan ito nakikita sa loob ng dataset ngunit hindi maayos na kinakatawan sa mga visualization o resulta ng query. Ang mga karaniwang problema sa pag-format ay kinabibilangan ng pag-aayos ng whitespace, mga petsa, at mga uri ng data. Ang pag-aayos ng mga isyu sa pag-format ay karaniwang nasa mga taong gumagamit ng data. Halimbawa, ang mga pamantayan sa kung paano ipinapakita ang mga petsa at numero ay maaaring magkaiba sa bawat bansa.

- **Pag-uulit**: Ang data na may higit sa isang paglitaw ay maaaring magdulot ng hindi tamang resulta at karaniwang dapat alisin. Ito ay maaaring karaniwang mangyari kapag pinagsama ang dalawa o higit pang mga dataset. Gayunpaman, may mga pagkakataon kung saan ang pag-uulit sa pinagsamang mga dataset ay naglalaman ng mga piraso na maaaring magbigay ng karagdagang impormasyon at maaaring kailangang panatilihin.

- **Nawawalang Data**: Ang nawawalang data ay maaaring magdulot ng hindi tamang resulta pati na rin mahina o bias na mga resulta. Minsan ang mga ito ay maaaring malutas sa pamamagitan ng "reload" ng data, pagpuno sa nawawalang mga halaga gamit ang computation at code tulad ng Python, o simpleng pag-aalis ng halaga at kaukulang data. Maraming mga dahilan kung bakit maaaring mawala ang data, at ang mga aksyon na ginawa upang malutas ang mga nawawalang halaga ay maaaring depende sa kung paano at bakit sila nawala.

## Paggalugad ng impormasyon ng DataFrame
> **Layunin ng pag-aaral:** Sa pagtatapos ng bahaging ito, dapat kang komportable sa paghahanap ng pangkalahatang impormasyon tungkol sa data na nakaimbak sa pandas DataFrames.

Kapag na-load mo na ang iyong data sa pandas, malamang na ito ay nasa isang DataFrame (tingnan ang nakaraang [aralin](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) para sa detalyadong overview). Gayunpaman, kung ang dataset sa iyong DataFrame ay may 60,000 rows at 400 columns, paano mo sisimulan ang pag-unawa sa kung ano ang iyong pinagtatrabahuhan? Sa kabutihang-palad, ang [pandas](https://pandas.pydata.org/) ay nagbibigay ng ilang maginhawang tools upang mabilis na makita ang pangkalahatang impormasyon tungkol sa isang DataFrame, pati na rin ang unang ilang at huling ilang rows.

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
Mula dito, nalaman natin na ang *Iris* dataset ay may 150 entries sa apat na columns na walang null entries. Ang lahat ng data ay nakaimbak bilang 64-bit floating-point numbers.

- **DataFrame.head()**: Susunod, upang suriin ang aktwal na nilalaman ng `DataFrame`, ginagamit natin ang `head()` method. Tingnan natin ang unang ilang rows ng ating `iris_df`:
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
- **DataFrame.tail()**: Sa kabaligtaran, upang suriin ang huling ilang rows ng `DataFrame`, ginagamit natin ang `tail()` method:
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
> **Takeaway:** Kahit sa pamamagitan lamang ng pagtingin sa metadata tungkol sa impormasyon sa isang DataFrame o sa unang at huling ilang halaga nito, maaari kang magkaroon ng agarang ideya tungkol sa laki, hugis, at nilalaman ng data na iyong pinagtatrabahuhan.

## Pagtugon sa Nawawalang Data
> **Layunin ng pag-aaral:** Sa pagtatapos ng bahaging ito, dapat mong malaman kung paano palitan o alisin ang mga null values mula sa DataFrames.

Kadalasan, ang mga dataset na nais mong gamitin (o kailangang gamitin) ay may mga nawawalang halaga. Ang paraan ng paghawak sa nawawalang data ay may kasamang mga banayad na tradeoffs na maaaring makaapekto sa iyong panghuling pagsusuri at mga resulta sa totoong mundo.

Ang pandas ay humahawak sa nawawalang mga halaga sa dalawang paraan. Ang una ay nakita mo na sa mga nakaraang seksyon: `NaN`, o Not a Number. Ito ay isang espesyal na halaga na bahagi ng IEEE floating-point specification at ginagamit lamang upang ipahiwatig ang nawawalang floating-point values.

Para sa nawawalang mga halaga bukod sa floats, ginagamit ng pandas ang Python `None` object. Habang maaaring mukhang nakakalito na makakakita ka ng dalawang magkaibang uri ng mga halaga na nagsasabi ng halos pareho, may mga tunog na programmatic na dahilan para sa pagpili ng disenyo na ito, at sa pagsasanay, ang pagpunta sa rutang ito ay nagbibigay-daan sa pandas na maghatid ng magandang kompromiso para sa karamihan ng mga kaso. Gayunpaman, ang parehong `None` at `NaN` ay may mga limitasyon na kailangan mong tandaan tungkol sa kung paano sila magagamit.

Tingnan ang higit pa tungkol sa `NaN` at `None` mula sa [notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Pag-detect ng null values**: Sa `pandas`, ang `isnull()` at `notnull()` methods ang iyong pangunahing paraan para sa pag-detect ng null data. Parehong nagbabalik ng Boolean masks sa iyong data. Gagamit tayo ng `numpy` para sa `NaN` values:
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
Tingnan nang mabuti ang output. Mayroon bang anumang nagulat sa iyo? Habang ang `0` ay isang arithmetic null, ito ay gayunpaman isang perpektong integer at tinatrato ito ng pandas bilang ganoon. Ang `''` ay medyo mas banayad. Habang ginamit natin ito sa Seksyon 1 upang kumatawan sa isang walang laman na string value, ito ay gayunpaman isang string object at hindi isang representasyon ng null ayon sa pandas.

Ngayon, baliktarin natin ito at gamitin ang mga method na ito sa paraang mas katulad ng gagamitin mo sa pagsasanay. Maaari mong gamitin ang Boolean masks nang direkta bilang isang ``Series`` o ``DataFrame`` index, na maaaring maging kapaki-pakinabang kapag sinusubukang magtrabaho sa mga nakahiwalay na nawawala (o naroroon) na mga halaga.

> **Takeaway**: Parehong ang `isnull()` at `notnull()` methods ay gumagawa ng magkatulad na resulta kapag ginamit mo ang mga ito sa `DataFrame`s: ipinapakita nila ang mga resulta at ang index ng mga resulta, na makakatulong sa iyo nang malaki habang nakikipagbuno ka sa iyong data.

- **Pag-aalis ng null values**: Bukod sa pagtukoy sa nawawalang mga halaga, ang pandas ay nagbibigay ng maginhawang paraan upang alisin ang mga null values mula sa `Series` at `DataFrame`s. (Lalo na sa malalaking dataset, mas maipapayo na alisin na lang ang nawawalang [NA] values mula sa iyong pagsusuri kaysa harapin ang mga ito sa ibang paraan.) Upang makita ito sa aksyon, bumalik tayo sa `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Tandaan na dapat itong magmukhang iyong output mula sa `example3[example3.notnull()]`. Ang pagkakaiba dito ay, sa halip na i-index lamang ang mga masked values, inalis ng `dropna` ang mga nawawalang halaga mula sa `Series` `example1`.

Dahil ang `DataFrame`s ay may dalawang dimensyon, nagbibigay ito ng mas maraming opsyon para sa pag-aalis ng data.

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

(Napansin mo ba na ang pandas ay nag-upcast ng dalawa sa mga column sa floats upang mapa-accommodate ang mga `NaN`s?)

Hindi mo maaaring alisin ang isang solong halaga mula sa isang `DataFrame`, kaya kailangan mong alisin ang buong rows o columns. Depende sa kung ano ang iyong ginagawa, maaaring gusto mong gawin ang isa o ang isa pa, kaya binibigyan ka ng pandas ng mga opsyon para sa pareho. Dahil sa data science, ang mga column ay karaniwang kumakatawan sa mga variable at ang mga row ay kumakatawan sa mga obserbasyon, mas malamang na alisin mo ang mga row ng data; ang default na setting para sa `dropna()` ay alisin ang lahat ng rows na naglalaman ng anumang null values:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Kung kinakailangan, maaari mong alisin ang mga NA values mula sa mga column. Gamitin ang `axis=1` upang gawin ito:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Tandaan na maaari itong mag-alis ng maraming data na maaaring gusto mong panatilihin, lalo na sa mas maliliit na dataset. Paano kung gusto mo lang alisin ang mga row o column na naglalaman ng ilang o kahit lahat ng null values? Tukuyin mo ang mga setting na iyon sa `dropna` gamit ang `how` at `thresh` parameters.

Sa default, `how='any'` (kung gusto mong suriin para sa iyong sarili o makita kung ano ang iba pang mga parameter na mayroon ang method, patakbuhin ang `example4.dropna?` sa isang code cell). Maaari mo ring tukuyin ang `how='all'` upang alisin lamang ang mga row o column na naglalaman ng lahat ng null values. Palawakin natin ang halimbawa ng `DataFrame` upang makita ito sa aksyon.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

Ang `thresh` parameter ay nagbibigay sa iyo ng mas pinong kontrol: itinatakda mo ang bilang ng *non-null* values na kailangan ng isang row o column upang mapanatili:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Dito, ang unang at huling row ay inalis, dahil naglalaman lamang sila ng dalawang non-null values.

- **Pagpuno sa null values**: Depende sa iyong dataset, minsan mas may katuturan na punan ang mga null values ng valid na mga halaga kaysa alisin ang mga ito. Maaari mong gamitin ang `isnull` upang gawin ito sa lugar, ngunit maaaring matrabaho ito, lalo na kung marami kang mga halaga na kailangang punan. Dahil ito ay isang karaniwang gawain sa data science, ang pandas ay nagbibigay ng `fillna`, na nagbabalik ng kopya ng `Series` o `DataFrame` na may mga nawawalang halaga na pinalitan ng isa sa iyong pinili. Gumawa tayo ng isa pang halimbawa ng `Series` upang makita kung paano ito gumagana sa pagsasanay.
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
Maaari mong punan ang lahat ng mga null entries gamit ang isang solong halaga, tulad ng `0`:
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
Maaari mong **forward-fill** ang mga null values, na ang ibig sabihin ay gamitin ang huling valid na halaga upang punan ang null:
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
Tulad ng iyong inaasahan, gumagana ito nang pareho sa `DataFrame`s, ngunit maaari mo ring tukuyin ang isang `axis` kung saan pupunan ang mga null values. Gamit ang dati nang ginamit na `example2`:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Tandaan na kapag ang isang nakaraang halaga ay hindi magagamit para sa forward-filling, ang null value ay nananatili.
> **Pangunahing Punto:** Maraming paraan upang harapin ang nawawalang mga halaga sa iyong mga dataset. Ang partikular na estratehiya na gagamitin mo (pag-aalis, pagpapalit, o kung paano mo papalitan) ay dapat nakabatay sa mga detalye ng data. Mas magkakaroon ka ng mas mahusay na pag-unawa sa paghawak ng nawawalang mga halaga habang mas madalas kang humawak at makipag-ugnayan sa mga dataset.

## Pag-aalis ng duplikadong data

> **Layunin ng Pag-aaral:** Sa pagtatapos ng bahaging ito, dapat kang komportable sa pagtukoy at pag-aalis ng mga duplikadong halaga mula sa mga DataFrame.

Bukod sa nawawalang data, madalas kang makakakita ng duplikadong data sa mga dataset sa totoong mundo. Sa kabutihang-palad, nagbibigay ang `pandas` ng madaling paraan upang matukoy at alisin ang mga duplikadong entry.

- **Pagtukoy sa mga duplikado: `duplicated`**: Madali mong makikita ang mga duplikadong halaga gamit ang `duplicated` method sa pandas, na nagbabalik ng Boolean mask na nagpapahiwatig kung ang isang entry sa `DataFrame` ay duplikado ng naunang isa. Gumawa tayo ng isa pang halimbawa ng `DataFrame` upang makita ito sa aksyon.
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
- **Pag-aalis ng duplikado: `drop_duplicates`:** simpleng nagbabalik ng kopya ng data kung saan lahat ng `duplicated` na halaga ay `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Parehong `duplicated` at `drop_duplicates` ay default na isinasaalang-alang ang lahat ng mga column ngunit maaari mong tukuyin na suriin lamang nila ang isang subset ng mga column sa iyong `DataFrame`:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Pangunahing Punto:** Ang pag-aalis ng duplikadong data ay mahalagang bahagi ng halos bawat proyekto sa agham ng datos. Ang duplikadong data ay maaaring magbago ng mga resulta ng iyong pagsusuri at magbigay sa iyo ng hindi tamang resulta!


## 🚀 Hamon

Ang lahat ng tinalakay na materyales ay ibinigay bilang isang [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Bukod dito, may mga ehersisyo pagkatapos ng bawat seksyon, subukan mo sila!

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/)



## Review at Sariling Pag-aaral

Maraming paraan upang matuklasan at lapitan ang paghahanda ng iyong data para sa pagsusuri at pagmomodelo, at ang paglilinis ng data ay isang mahalagang hakbang na nangangailangan ng "hands-on" na karanasan. Subukan ang mga hamon na ito mula sa Kaggle upang tuklasin ang mga teknik na hindi saklaw ng araling ito.

- [Data Cleaning Challenge: Parsing Dates](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Data Cleaning Challenge: Scale and Normalize Data](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Takdang-Aralin

[Pag-evaluate ng Data mula sa isang Form](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.