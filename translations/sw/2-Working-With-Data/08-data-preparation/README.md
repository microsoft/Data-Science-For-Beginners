<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1b560955ff39a2bcf2a049fce474a951",
  "translation_date": "2025-09-05T17:08:39+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "sw"
}
-->
# Kufanya Kazi na Data: Maandalizi ya Data

|![ Sketchnote na [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Maandalizi ya Data - _Sketchnote na [@nitya](https://twitter.com/nitya)_ |

## [Maswali ya Awali ya Somo](https://ff-quizzes.netlify.app/en/ds/quiz/14)

Kutegemea chanzo chake, data ghafi inaweza kuwa na kutokubaliana fulani ambazo zitasababisha changamoto katika uchambuzi na uundaji wa mifano. Kwa maneno mengine, data hii inaweza kuainishwa kama "chafu" na itahitaji kusafishwa. Somo hili linazingatia mbinu za kusafisha na kubadilisha data ili kushughulikia changamoto za data iliyopotea, isiyo sahihi, au isiyokamilika. Mada zilizojadiliwa katika somo hili zitatumia Python na maktaba ya Pandas na zitaonyeshwa katika [notebook](../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb) ndani ya saraka hii.

## Umuhimu wa Kusafisha Data

- **Urahisi wa matumizi na matumizi tena**: Wakati data imepangwa vizuri na kuhalalishwa, ni rahisi kuitafuta, kuitumia, na kushirikiana na wengine.

- **Uthabiti**: Sayansi ya data mara nyingi inahitaji kufanya kazi na seti zaidi ya moja ya data, ambapo seti za data kutoka vyanzo tofauti zinahitaji kuunganishwa pamoja. Kuhakikisha kwamba kila seti ya data ina kiwango cha kawaida cha uhalalishaji kutahakikisha kuwa data bado ni muhimu wakati zote zimeunganishwa kuwa seti moja ya data.

- **Usahihi wa mifano**: Data ambayo imesafishwa inaboresha usahihi wa mifano inayotegemea data hiyo.

## Malengo na Mikakati ya Kawaida ya Kusafisha

- **Kuchunguza seti ya data**: Uchunguzi wa data, ambao unajadiliwa katika [somo la baadaye](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), unaweza kukusaidia kugundua data inayohitaji kusafishwa. Kuangalia kwa macho thamani ndani ya seti ya data kunaweza kuweka matarajio ya jinsi sehemu nyingine itakavyokuwa, au kutoa wazo la matatizo yanayoweza kutatuliwa. Uchunguzi unaweza kuhusisha kuuliza maswali ya msingi, kuonyesha data kwa njia ya picha, na kuchukua sampuli.

- **Uundaji**: Kutegemea chanzo, data inaweza kuwa na kutokubaliana katika jinsi inavyowasilishwa. Hii inaweza kusababisha matatizo katika kutafuta na kuwakilisha thamani, ambapo inaonekana ndani ya seti ya data lakini haijawakilishwa vizuri katika picha au matokeo ya maswali. Matatizo ya kawaida ya uundaji yanahusisha kutatua nafasi tupu, tarehe, na aina za data. Kutatua masuala ya uundaji kwa kawaida ni jukumu la watu wanaotumia data. Kwa mfano, viwango vya jinsi tarehe na namba zinavyowasilishwa vinaweza kutofautiana kulingana na nchi.

- **Marudio**: Data ambayo ina tukio zaidi ya moja inaweza kutoa matokeo yasiyo sahihi na kwa kawaida inapaswa kuondolewa. Hii inaweza kuwa tukio la kawaida wakati wa kuunganisha seti mbili au zaidi za data pamoja. Hata hivyo, kuna hali ambapo marudio katika seti za data zilizounganishwa zina vipande vinavyoweza kutoa taarifa za ziada na zinaweza kuhitaji kuhifadhiwa.

- **Data Iliyopotea**: Data iliyopotea inaweza kusababisha matokeo yasiyo sahihi pamoja na matokeo dhaifu au yenye upendeleo. Wakati mwingine haya yanaweza kutatuliwa kwa "kupakia tena" data, kujaza thamani zilizopotea kwa hesabu na msimbo kama Python, au kwa urahisi kuondoa thamani na data inayohusiana. Kuna sababu nyingi kwa nini data inaweza kupotea na hatua zinazochukuliwa kutatua thamani hizi zilizopotea zinaweza kutegemea jinsi na kwa nini zilipotea.

## Kuchunguza Taarifa za DataFrame
> **Lengo la kujifunza:** Mwisho wa sehemu hii ndogo, unapaswa kuwa na ujuzi wa kupata taarifa za jumla kuhusu data iliyohifadhiwa katika DataFrames za pandas.

Mara tu unapopakia data yako kwenye pandas, kuna uwezekano mkubwa kuwa itakuwa katika DataFrame (rejelea [somo la awali](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) kwa muhtasari wa kina). Hata hivyo, ikiwa seti ya data katika DataFrame yako ina safu 60,000 na nguzo 400, unaanzaje kupata hisia ya unachofanya kazi nacho? Kwa bahati nzuri, [pandas](https://pandas.pydata.org/) hutoa zana rahisi za kuangalia haraka taarifa za jumla kuhusu DataFrame pamoja na safu chache za mwanzo na za mwisho.

Ili kuchunguza utendaji huu, tutaleta maktaba ya Python scikit-learn na kutumia seti ya data maarufu: **Seti ya data ya Iris**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |urefu wa sepal (cm)|upana wa sepal (cm)|urefu wa petal (cm)|upana wa petal (cm)|
|----------------------------------------|-------------------|-------------------|-------------------|-------------------|
|0                                       |5.1                |3.5                |1.4                |0.2                |
|1                                       |4.9                |3.0                |1.4                |0.2                |
|2                                       |4.7                |3.2                |1.3                |0.2                |
|3                                       |4.6                |3.1                |1.5                |0.2                |
|4                                       |5.0                |3.6                |1.4                |0.2                |

- **DataFrame.info**: Kuanza, njia ya `info()` inatumika kuchapisha muhtasari wa yaliyomo katika `DataFrame`. Hebu tuangalie seti hii ya data ili kuona tunachonacho:
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
Kutoka hapa, tunajua kwamba seti ya data ya *Iris* ina maingizo 150 katika nguzo nne bila maingizo tupu. Data yote imehifadhiwa kama namba za nukta zinazozunguka za 64-bit.

- **DataFrame.head()**: Kisha, ili kuangalia yaliyomo halisi ya `DataFrame`, tunatumia njia ya `head()`. Hebu tuone safu chache za mwanzo za `iris_df` yetu:
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
- **DataFrame.tail()**: Kinyume chake, ili kuangalia safu chache za mwisho za `DataFrame`, tunatumia njia ya `tail()`:
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
> **Hitimisho:** Hata kwa kuangalia tu metadata kuhusu taarifa katika DataFrame au thamani chache za mwanzo na za mwisho, unaweza kupata wazo la haraka kuhusu ukubwa, umbo, na yaliyomo ya data unayoshughulika nayo.

## Kushughulikia Data Iliyopotea
> **Lengo la kujifunza:** Mwisho wa sehemu hii ndogo, unapaswa kujua jinsi ya kubadilisha au kuondoa thamani tupu kutoka DataFrames.

Mara nyingi seti za data unazotaka kutumia (au unazopaswa kutumia) zina thamani zilizopotea ndani yake. Jinsi data iliyopotea inavyoshughulikiwa ina athari ndogo ambazo zinaweza kuathiri uchambuzi wako wa mwisho na matokeo halisi ya ulimwengu.

Pandas hushughulikia thamani zilizopotea kwa njia mbili. Ya kwanza umeiona hapo awali katika sehemu zilizopita: `NaN`, au Not a Number. Hii ni thamani maalum ambayo ni sehemu ya maelezo ya nukta zinazozunguka za IEEE na hutumika tu kuonyesha thamani za nukta zinazozunguka zilizopotea.

Kwa thamani zilizopotea mbali na nukta zinazozunguka, pandas hutumia kitu cha Python `None`. Ingawa inaweza kuonekana kuwa ni mkanganyiko kwamba utakutana na aina mbili tofauti za thamani zinazosema kimsingi kitu kimoja, kuna sababu za kimaandishi za programu kwa chaguo hili la muundo na, kwa mazoezi, njia hii inaiwezesha pandas kutoa suluhisho nzuri kwa hali nyingi. Licha ya hili, zote `None` na `NaN` zina vizuizi ambavyo unahitaji kuzingatia kuhusu jinsi zinavyoweza kutumika.

Angalia zaidi kuhusu `NaN` na `None` kutoka [notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Kugundua thamani tupu**: Katika `pandas`, njia za `isnull()` na `notnull()` ni njia zako kuu za kugundua data tupu. Zote zinarudisha maski za Boolean juu ya data yako. Tutatumia `numpy` kwa thamani za `NaN`:
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
Angalia kwa makini matokeo. Je, kuna lolote linalokushangaza? Ingawa `0` ni null ya hesabu, bado ni namba kamili nzuri na pandas inaitendea kama hiyo. `''` ni kidogo zaidi ya hila. Ingawa tulitumia katika Sehemu ya 1 kuwakilisha thamani ya kamba tupu, bado ni kitu cha kamba na si uwakilishi wa null kulingana na pandas.

Sasa, hebu tugeuze hili na kutumia njia hizi kwa namna zaidi kama unavyotumia kwa mazoezi. Unaweza kutumia maski za Boolean moja kwa moja kama `Series` au `DataFrame` index, ambayo inaweza kuwa muhimu wakati wa kujaribu kufanya kazi na thamani zilizopotea (au zilizopo) pekee.

> **Hitimisho:** Zote `isnull()` na `notnull()` hutoa matokeo yanayofanana unapotumia katika `DataFrame`s: zinaonyesha matokeo na index ya matokeo hayo, ambayo yatakusaidia sana unaposhughulika na data yako.

- **Kuondoa thamani tupu**: Zaidi ya kutambua thamani zilizopotea, pandas hutoa njia rahisi ya kuondoa thamani tupu kutoka `Series` na `DataFrame`s. (Hasa kwenye seti kubwa za data, mara nyingi ni busara zaidi kuondoa thamani zilizopotea [NA] kutoka uchambuzi wako kuliko kushughulika nazo kwa njia nyingine.) Ili kuona hili kwa vitendo, hebu turudi kwa `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Kumbuka kwamba hii inapaswa kuonekana kama matokeo yako kutoka `example3[example3.notnull()]`. Tofauti hapa ni kwamba, badala ya kuindex kwenye thamani zilizofichwa, `dropna` imeondoa thamani zilizopotea kutoka `Series` `example1`.

Kwa sababu `DataFrame`s zina vipimo viwili, zinatoa chaguo zaidi za kuondoa data.

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

(Je, uliona kwamba pandas ilibadilisha nguzo mbili kuwa nukta zinazozunguka ili kukidhi `NaN`s?)

Huwezi kuondoa thamani moja kutoka `DataFrame`, kwa hivyo lazima uondoe safu nzima au nguzo. Kutegemea unachofanya, unaweza kutaka kufanya moja au nyingine, na kwa hivyo pandas inakupa chaguo zote mbili. Kwa sababu katika sayansi ya data, nguzo kwa kawaida zinawakilisha vigezo na safu zinawakilisha uchunguzi, una uwezekano mkubwa wa kuondoa safu za data; mpangilio wa msingi wa `dropna()` ni kuondoa safu zote zinazojumuisha thamani yoyote tupu:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Ikiwa ni lazima, unaweza kuondoa thamani za NA kutoka nguzo. Tumia `axis=1` kufanya hivyo:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Kumbuka kwamba hii inaweza kuondoa data nyingi ambayo unaweza kutaka kuhifadhi, hasa katika seti ndogo za data. Je, ikiwa unataka tu kuondoa safu au nguzo zinazojumuisha kadhaa au hata thamani zote tupu? Unaweza kutaja mipangilio hiyo katika `dropna` kwa vigezo vya `how` na `thresh`.

Kwa msingi, `how='any'` (ikiwa ungependa kuangalia mwenyewe au kuona vigezo vingine ambavyo njia hiyo ina, endesha `example4.dropna?` katika seli ya msimbo). Unaweza badala yake kutaja `how='all'` ili kuondoa tu safu au nguzo zinazojumuisha thamani zote tupu. Hebu tuongeze `DataFrame` yetu ya mfano ili kuona hili kwa vitendo.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

Kigezo cha `thresh` kinakupa udhibiti wa kina zaidi: unataja idadi ya thamani *zisizo tupu* ambazo safu au nguzo inahitaji kuwa nazo ili kuhifadhiwa:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Hapa, safu ya kwanza na ya mwisho zimeondolewa, kwa sababu zina thamani mbili tu zisizo tupu.

- **Kujaza thamani tupu**: Kutegemea seti yako ya data, wakati mwingine inaweza kuwa na maana zaidi kujaza thamani tupu na zile halali badala ya kuondoa. Unaweza kutumia `isnull` kufanya hivi mahali pake, lakini hiyo inaweza kuwa kazi ngumu, hasa ikiwa una thamani nyingi za kujaza. Kwa sababu hii ni kazi ya kawaida katika sayansi ya data, pandas hutoa `fillna`, ambayo inarudisha nakala ya `Series` au `DataFrame` na thamani zilizopotea kubadilishwa na moja unayochagua. Hebu tuunde `Series` nyingine ya mfano ili kuona jinsi hii inavyofanya kazi kwa mazoezi.
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
Unaweza kujaza maingizo yote tupu na thamani moja, kama `0`:
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
Unaweza **kujaza mbele** thamani tupu, ambayo ni kutumia thamani halali ya mwisho kujaza tupu:
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
Unaweza pia **kujaza nyuma** ili kueneza thamani halali inayofuata nyuma kujaza tupu:
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
Kama unavyoweza kudhani, hii inafanya kazi sawa na `DataFrame`s, lakini unaweza pia kutaja `axis` ambayo kujaza thamani tupu kunafanyika. Ukichukua tena `example2` iliyotumika hapo awali:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Kumbuka kwamba wakati thamani ya awali haipatikani kwa kujaza mbele, thamani tupu inabaki.
> **Mafunzo Muhimu:** Kuna njia nyingi za kushughulikia thamani zinazokosekana katika seti zako za data. Mkakati maalum unaotumia (kuondoa, kubadilisha, au hata jinsi unavyobadilisha) unapaswa kuongozwa na maelezo ya data hiyo. Utapata uelewa bora wa jinsi ya kushughulikia thamani zinazokosekana kadri unavyoshughulikia na kuingiliana na seti za data.
## Kuondoa Takwimu Zilizojirudia

> **Lengo la kujifunza:** Mwisho wa sehemu hii ndogo, unapaswa kuwa na uelewa wa kutambua na kuondoa thamani zinazojirudia kutoka kwa DataFrames.

Mbali na data inayokosekana, mara nyingi utakutana na data iliyojirudia katika seti za data za ulimwengu halisi. Kwa bahati nzuri, `pandas` inatoa njia rahisi ya kugundua na kuondoa maingizo yaliyodukuliwa.

- **Kutambua data zinazojirudia: `duplicated`**: Unaweza kutambua kwa urahisi thamani zinazojirudia kwa kutumia njia ya `duplicated` katika pandas, ambayo inarudisha mask ya Boolean inayoonyesha ikiwa ingizo katika `DataFrame` ni nakala ya ingizo la awali. Hebu tuunde mfano mwingine wa `DataFrame` ili kuona hili likifanya kazi.
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
- **Kuondoa data zinazojirudia: `drop_duplicates`:** inarudisha nakala ya data ambapo thamani zote za `duplicated` ni `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Njia zote mbili `duplicated` na `drop_duplicates` kwa chaguo-msingi huzingatia safu zote, lakini unaweza kubainisha kwamba zichunguze tu sehemu ndogo ya safu katika `DataFrame` yako:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Mafunzo muhimu:** Kuondoa data zinazojirudia ni sehemu muhimu ya karibu kila mradi wa sayansi ya data. Data zinazojirudia zinaweza kubadilisha matokeo ya uchambuzi wako na kukupa matokeo yasiyo sahihi!


## 🚀 Changamoto

Vifaa vyote vilivyojadiliwa vinapatikana kama [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Zaidi ya hayo, kuna mazoezi yaliyopo baada ya kila sehemu, jaribu kuyafanya!

## [Jaribio la baada ya somo](https://ff-quizzes.netlify.app/en/ds/quiz/15)



## Mapitio na Kujisomea

Kuna njia nyingi za kugundua na kukaribia kuandaa data yako kwa uchambuzi na uundaji wa mifano, na kusafisha data ni hatua muhimu ambayo inahitaji uzoefu wa "vitendo". Jaribu changamoto hizi kutoka Kaggle ili kuchunguza mbinu ambazo somo hili halikuzifunika.

- [Changamoto ya Kusafisha Data: Kuchambua Tarehe](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Changamoto ya Kusafisha Data: Kupima na Kuweka Kawaida Data](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Kazi

[Kutathmini Data kutoka Fomu](assignment.md)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutokuelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.