<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "02ce904bc1e2bfabb7dc05c25aae375c",
  "translation_date": "2025-09-05T06:34:37+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "sw"
}
-->
# Kuonyesha Usambazaji

|![ Sketchnote na [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Kuonyesha Usambazaji - _Sketchnote na [@nitya](https://twitter.com/nitya)_ |

Katika somo lililopita, ulijifunza mambo ya kuvutia kuhusu seti ya data ya ndege wa Minnesota. Ulipata data yenye makosa kwa kuonyesha vipimo vya nje na ukaangalia tofauti kati ya makundi ya ndege kulingana na urefu wao wa juu zaidi.

## [Maswali ya awali ya somo](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## Chunguza seti ya data ya ndege

Njia nyingine ya kuchunguza data ni kwa kuangalia usambazaji wake, au jinsi data imepangwa kulingana na mhimili. Labda, kwa mfano, ungependa kujifunza kuhusu usambazaji wa jumla, kwa seti hii ya data, wa upana wa mabawa wa juu zaidi au uzito wa mwili wa juu zaidi wa ndege wa Minnesota.

Hebu tujifunze baadhi ya ukweli kuhusu usambazaji wa data katika seti hii ya data. Katika faili _notebook.ipynb_ kwenye mzizi wa folda ya somo hili, leta Pandas, Matplotlib, na data yako:

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | Jina                         | Jina la Kisayansi      | Kategoria             | Oda          | Familia  | Jenasi      | Hali ya Uhifadhi   | Urefu wa Min | Urefu wa Max | Uzito wa Min | Uzito wa Max | Upana wa Min | Upana wa Max |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------:    | --------:    | ----------:  | ----------:  | ----------:  | ----------:  |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        47    |        56    |         652  |        1020  |          76  |          94  |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        45    |        53    |         712  |        1050  |          85  |          93  |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64    |        79    |        2050  |        4050  |         135  |         165  |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |      57.3    |        64    |        1066  |        1567  |         113  |         116  |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64    |        81    |        1930  |        3310  |         130  |         165  |

Kwa ujumla, unaweza kuangalia haraka jinsi data inavyosambazwa kwa kutumia mchoro wa alama kama tulivyofanya katika somo lililopita:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![urefu wa juu zaidi kwa oda](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

Hii inatoa muhtasari wa usambazaji wa jumla wa urefu wa mwili kwa kila Oda ya ndege, lakini si njia bora ya kuonyesha usambazaji wa kweli. Kazi hiyo kwa kawaida hufanywa kwa kuunda Histogramu.

## Kufanya kazi na histogramu

Matplotlib inatoa njia nzuri za kuonyesha usambazaji wa data kwa kutumia Histogramu. Aina hii ya mchoro ni kama mchoro wa bar ambapo usambazaji unaweza kuonekana kupitia kupanda na kushuka kwa mabara. Ili kujenga histogramu, unahitaji data ya nambari. Ili kujenga Histogramu, unaweza kuchora mchoro ukifafanua aina kama 'hist' kwa Histogramu. Mchoro huu unaonyesha usambazaji wa MaxBodyMass kwa seti nzima ya data ya nambari. Kwa kugawanya safu ya data iliyotolewa katika vikundi vidogo, inaweza kuonyesha usambazaji wa thamani za data:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![usambazaji katika seti nzima ya data](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

Kama unavyoona, ndege wengi kati ya 400+ katika seti hii ya data wana uzito wa mwili wa juu zaidi chini ya 2000. Pata ufahamu zaidi kuhusu data kwa kubadilisha parameter ya `bins` kuwa nambari kubwa zaidi, kama 30:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![usambazaji katika seti nzima ya data na param ya vikundi vikubwa](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

Mchoro huu unaonyesha usambazaji kwa undani zaidi. Mchoro usioegemea sana upande wa kushoto unaweza kuundwa kwa kuhakikisha kuwa unachagua tu data ndani ya safu fulani:

Chuja data yako ili kupata ndege tu ambao uzito wa mwili uko chini ya 60, na onyesha vikundi 40 `bins`:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![histogramu iliyochujwa](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ Jaribu vichujio vingine na vidokezo vya data. Ili kuona usambazaji kamili wa data, ondoa kichujio cha `['MaxBodyMass']` ili kuonyesha usambazaji ulio na lebo.

Histogramu inatoa maboresho mazuri ya rangi na lebo pia:

Unda histogramu ya 2D ili kulinganisha uhusiano kati ya usambazaji mbili. Hebu linganisha `MaxBodyMass` dhidi ya `MaxLength`. Matplotlib inatoa njia ya kujengwa kuonyesha muunganiko kwa kutumia rangi angavu zaidi:

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
Inaonekana kuna uhusiano unaotarajiwa kati ya vipengele hivi viwili kulingana na mhimili unaotarajiwa, na kuna sehemu moja yenye nguvu ya muunganiko:

![mchoro wa 2D](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

Histogramu hufanya kazi vizuri kwa chaguo-msingi kwa data ya nambari. Je, unahitaji kuona usambazaji kulingana na data ya maandishi?

## Chunguza seti ya data kwa usambazaji kwa kutumia data ya maandishi 

Seti hii ya data pia inajumuisha taarifa nzuri kuhusu kategoria ya ndege na jenasi, spishi, na familia yake pamoja na hali yake ya uhifadhi. Hebu tuchunguze taarifa hii ya uhifadhi. Usambazaji wa ndege kulingana na hali yao ya uhifadhi ukoje?

> ✅ Katika seti ya data, vifupisho kadhaa vinatumika kuelezea hali ya uhifadhi. Vifupisho hivi vinatoka kwa [IUCN Red List Categories](https://www.iucnredlist.org/), shirika linaloorodhesha hali ya spishi.
> 
> - CR: Hatari Sana
> - EN: Hatari
> - EX: Imeangamia
> - LC: Wasiwasi Mdogo
> - NT: Karibu na Hatari
> - VU: Hatarini

Hizi ni thamani za maandishi kwa hivyo utahitaji kufanya mabadiliko ili kuunda histogramu. Kwa kutumia dataframe ya filteredBirds, onyesha hali yake ya uhifadhi pamoja na Upana wa Mabawa wa Min. Unaona nini?

```python
x1 = filteredBirds.loc[filteredBirds.ConservationStatus=='EX', 'MinWingspan']
x2 = filteredBirds.loc[filteredBirds.ConservationStatus=='CR', 'MinWingspan']
x3 = filteredBirds.loc[filteredBirds.ConservationStatus=='EN', 'MinWingspan']
x4 = filteredBirds.loc[filteredBirds.ConservationStatus=='NT', 'MinWingspan']
x5 = filteredBirds.loc[filteredBirds.ConservationStatus=='VU', 'MinWingspan']
x6 = filteredBirds.loc[filteredBirds.ConservationStatus=='LC', 'MinWingspan']

kwargs = dict(alpha=0.5, bins=20)

plt.hist(x1, **kwargs, color='red', label='Extinct')
plt.hist(x2, **kwargs, color='orange', label='Critically Endangered')
plt.hist(x3, **kwargs, color='yellow', label='Endangered')
plt.hist(x4, **kwargs, color='green', label='Near Threatened')
plt.hist(x5, **kwargs, color='blue', label='Vulnerable')
plt.hist(x6, **kwargs, color='gray', label='Least Concern')

plt.gca().set(title='Conservation Status', ylabel='Min Wingspan')
plt.legend();
```

![muunganiko wa mabawa na uhifadhi](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

Haionekani kuwa na uhusiano mzuri kati ya upana wa mabawa wa chini na hali ya uhifadhi. Jaribu vipengele vingine vya seti ya data kwa kutumia njia hii. Unaweza kujaribu vichujio tofauti pia. Je, unapata uhusiano wowote?

## Mchoro wa wingi

Huenda umeona kwamba histogramu tulizozitazama hadi sasa ni 'zimepangwa' na hazionyeshi mtiririko laini katika umbo la mviringo. Ili kuonyesha mchoro wa wingi ulio laini zaidi, unaweza kujaribu mchoro wa wingi.

Ili kufanya kazi na mchoro wa wingi, jifunze kuhusu maktaba mpya ya kuchora, [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html). 

Ukileta Seaborn, jaribu mchoro wa wingi wa msingi:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![Mchoro wa wingi](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

Unaweza kuona jinsi mchoro unavyoakisi ule wa awali kwa data ya Upana wa Mabawa wa Min; ni laini kidogo tu. Kulingana na nyaraka za Seaborn, "Ikilinganishwa na histogramu, KDE inaweza kutoa mchoro ambao haujachanganyika sana na unaeleweka zaidi, hasa wakati wa kuchora usambazaji mwingi. Lakini ina uwezo wa kuleta upotoshaji ikiwa usambazaji wa msingi umefungwa au si laini. Kama histogramu, ubora wa uwakilishi pia unategemea uteuzi wa vigezo vya kulainisha vizuri." [chanzo](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) Kwa maneno mengine, vipimo vya nje kama kawaida vitafanya michoro yako kuwa na tabia mbaya.

Ikiwa ungependa kurudia mstari wa MaxBodyMass ulio na pembe katika mchoro wa pili uliouunda, unaweza kuulainisha vizuri kwa kuutengeneza upya kwa kutumia njia hii:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![mstari laini wa uzito wa mwili](../../../../3-Data-Visualization/10-visualization-distributions/images/density2.png)

Ikiwa ungependa mstari ulio laini, lakini si laini sana, hariri parameter ya `bw_adjust`: 

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![mstari usio laini sana wa uzito wa mwili](../../../../3-Data-Visualization/10-visualization-distributions/images/density3.png)

✅ Soma kuhusu vigezo vinavyopatikana kwa aina hii ya mchoro na jaribu!

Aina hii ya mchoro inatoa maelezo mazuri ya kuona. Kwa mistari michache ya msimbo, kwa mfano, unaweza kuonyesha wingi wa uzito wa mwili wa juu zaidi kwa kila Oda ya ndege:

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![uzito wa mwili kwa oda](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

Unaweza pia kuonyesha wingi wa vipengele kadhaa katika mchoro mmoja. Linganisha Urefu wa Max na Urefu wa Min wa ndege kulingana na hali yao ya uhifadhi:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![wingi mwingi, umewekwa juu](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

Labda inafaa kuchunguza ikiwa mkusanyiko wa ndege 'Hatarini' kulingana na urefu wao una maana au la.

## 🚀 Changamoto

Histogramu ni aina ya mchoro wa kisasa zaidi kuliko michoro ya alama, michoro ya bar, au michoro ya mstari. Tafuta mifano mizuri ya matumizi ya histogramu kwenye mtandao. Zinatumika vipi, zinaonyesha nini, na katika nyanja au maeneo gani ya uchunguzi zinatumiwa mara nyingi?

## [Maswali ya baada ya somo](https://ff-quizzes.netlify.app/en/ds/)

## Mapitio & Kujisomea

Katika somo hili, ulitumia Matplotlib na ukaanza kufanya kazi na Seaborn kuonyesha michoro ya kisasa zaidi. Fanya utafiti kuhusu `kdeplot` katika Seaborn, "mchoro wa wingi wa uwezekano endelevu katika mwelekeo mmoja au zaidi". Soma [nyaraka](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) ili kuelewa jinsi inavyofanya kazi.

## Kazi

[Tumia ujuzi wako](assignment.md)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutokuelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.