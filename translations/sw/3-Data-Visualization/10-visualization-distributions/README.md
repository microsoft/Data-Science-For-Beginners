<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a20467e046d312809d008395051fc7",
  "translation_date": "2025-09-05T17:14:52+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "sw"
}
-->
# Kuonyesha Usambazaji

|![ Sketchnote na [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Kuonyesha Usambazaji - _Sketchnote na [@nitya](https://twitter.com/nitya)_ |

Katika somo lililopita, ulijifunza mambo ya kuvutia kuhusu seti ya data ya ndege wa Minnesota. Ulipata data yenye makosa kwa kuonyesha vipimo vya nje na ukaangalia tofauti kati ya makundi ya ndege kulingana na urefu wao wa juu zaidi.

## [Jaribio la kabla ya somo](https://ff-quizzes.netlify.app/en/ds/quiz/18)
## Chunguza seti ya data ya ndege

Njia nyingine ya kuchunguza data ni kwa kuangalia usambazaji wake, yaani jinsi data imepangwa kwenye mhimili. Labda, kwa mfano, ungependa kujifunza kuhusu usambazaji wa jumla, kwa seti hii ya data, wa upana wa mabawa wa juu zaidi au uzito wa mwili wa juu zaidi wa ndege wa Minnesota.

Hebu tujifunze baadhi ya ukweli kuhusu usambazaji wa data katika seti hii ya data. Katika faili _notebook.ipynb_ kwenye mzizi wa folda ya somo hili, leta Pandas, Matplotlib, na data yako:

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | Jina                          | Jina la Kisayansi      | Kategoria             | Oda          | Familia  | Jenasi      | Hali ya Uhifadhi   | UrefuMdogo | UrefuMkuu | UzitoMdogo  | UzitoMkuu   | MabawaMdogo | MabawaMkuu  |
| ---: | :---------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Kwa ujumla, unaweza kuangalia haraka jinsi data inavyosambazwa kwa kutumia mchoro wa alama kama tulivyofanya katika somo lililopita:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![urefu wa juu zaidi kwa oda](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

Hii inatoa muhtasari wa usambazaji wa jumla wa urefu wa mwili kwa kila Oda ya ndege, lakini si njia bora ya kuonyesha usambazaji wa kweli. Kazi hii kwa kawaida hufanywa kwa kuunda Histogramu.

## Kufanya kazi na histogramu

Matplotlib inatoa njia nzuri za kuonyesha usambazaji wa data kwa kutumia Histogramu. Aina hii ya mchoro ni kama mchoro wa nguzo ambapo usambazaji unaweza kuonekana kupitia kupanda na kushuka kwa nguzo. Ili kujenga histogramu, unahitaji data ya namba. Ili kujenga Histogramu, unaweza kuchora mchoro ukifafanua aina kama 'hist' kwa Histogramu. Mchoro huu unaonyesha usambazaji wa UzitoMkuu wa Mwili kwa seti nzima ya data ya namba. Kwa kugawanya safu ya data iliyotolewa katika sehemu ndogo, inaweza kuonyesha usambazaji wa thamani za data:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![usambazaji kwenye seti nzima ya data](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

Kama unavyoona, ndege wengi kati ya 400+ katika seti hii ya data wanaangukia katika safu ya chini ya 2000 kwa UzitoMkuu wa Mwili wao. Pata ufahamu zaidi kuhusu data kwa kubadilisha parameter ya `bins` kuwa namba kubwa zaidi, kama 30:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![usambazaji kwenye seti nzima ya data na param ya bins kubwa](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

Mchoro huu unaonyesha usambazaji kwa undani zaidi. Mchoro usioegemea sana upande wa kushoto unaweza kuundwa kwa kuhakikisha kuwa unachagua tu data ndani ya safu fulani:

Chuja data yako ili kupata ndege tu ambao uzito wa mwili uko chini ya 60, na onyesha `bins` 40:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![histogramu iliyochujwa](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ Jaribu vichujio vingine na vipengele vya data. Ili kuona usambazaji kamili wa data, ondoa kichujio cha `['MaxBodyMass']` ili kuonyesha usambazaji ulio na lebo.

Histogramu inatoa maboresho mazuri ya rangi na lebo pia:

Unda histogramu ya 2D ili kulinganisha uhusiano kati ya usambazaji mbili. Hebu linganisha `MaxBodyMass` dhidi ya `MaxLength`. Matplotlib inatoa njia ya kujengwa kuonyesha mwelekeo kwa kutumia rangi angavu zaidi:

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
Inaonekana kuna uhusiano unaotarajiwa kati ya vipengele hivi viwili kwenye mhimili unaotarajiwa, na sehemu moja yenye nguvu ya mwelekeo:

![mchoro wa 2D](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

Histogramu hufanya kazi vizuri kwa chaguo-msingi kwa data ya namba. Je, unahitaji kuona usambazaji kulingana na data ya maandishi?

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

Hizi ni thamani za maandishi kwa hivyo utahitaji kufanya mabadiliko ili kuunda histogramu. Kwa kutumia dataframe ya filteredBirds, onyesha hali yake ya uhifadhi pamoja na MabawaMdogo. Unaona nini?

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

![mabawa na uhifadhi](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

Haionekani kuwa na uhusiano mzuri kati ya mabawa ya chini na hali ya uhifadhi. Jaribu vipengele vingine vya seti ya data kwa kutumia njia hii. Unaweza kujaribu vichujio tofauti pia. Je, unapata uhusiano wowote?

## Mchoro wa wingi

Huenda umeona kuwa histogramu tulizozitazama hadi sasa ni 'zimepangwa' na hazionyeshi mtiririko laini katika umbo la mviringo. Ili kuonyesha mchoro wa wingi ulio laini zaidi, unaweza kujaribu mchoro wa wingi.

Ili kufanya kazi na michoro ya wingi, jifunze kuhusu maktaba mpya ya kuchora, [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html). 

Ukileta Seaborn, jaribu mchoro wa wingi wa msingi:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![Mchoro wa wingi](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

Unaweza kuona jinsi mchoro unavyoakisi ule wa awali kwa data ya MabawaMdogo; ni laini kidogo tu. Kulingana na nyaraka za Seaborn, "Ikilinganishwa na histogramu, KDE inaweza kutoa mchoro ambao si wa fujo na unaeleweka zaidi, hasa wakati wa kuchora usambazaji mwingi. Lakini ina uwezo wa kuleta upotoshaji ikiwa usambazaji wa msingi umefungwa au si laini. Kama histogramu, ubora wa uwakilishi pia unategemea uteuzi wa vigezo vya kulainisha vizuri." [chanzo](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) Kwa maneno mengine, vipimo vya nje kama kawaida vitafanya michoro yako kuwa na tabia mbaya.

Ikiwa ungependa kurudia mstari wa UzitoMkuu wa Mwili ulio na pembe katika mchoro wa pili uliouunda, unaweza kuulainisha vizuri kwa kuutengeneza upya kwa kutumia njia hii:

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

Aina hii ya mchoro inatoa michoro yenye maelezo mazuri. Kwa mistari michache ya msimbo, kwa mfano, unaweza kuonyesha wingi wa uzito wa mwili wa juu zaidi kwa kila Oda ya ndege:

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![uzito wa mwili kwa oda](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

Unaweza pia kuonyesha wingi wa vipengele kadhaa katika mchoro mmoja. Linganisha UrefuMkuu na UrefuMdogo wa ndege kulingana na hali yao ya uhifadhi:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![wingi mwingi, umewekwa juu juu](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

Labda inafaa kufanya utafiti ikiwa mkusanyiko wa ndege 'Hatarini' kulingana na urefu wao una maana au la.

## 🚀 Changamoto

Histogramu ni aina ya mchoro wa kisasa zaidi kuliko michoro ya alama, michoro ya nguzo, au michoro ya mstari ya msingi. Tafuta mifano mizuri ya matumizi ya histogramu kwenye mtandao. Zinatumika vipi, zinaonyesha nini, na katika nyanja au maeneo gani ya uchunguzi zinatumiwa zaidi?

## [Jaribio la baada ya somo](https://ff-quizzes.netlify.app/en/ds/quiz/19)

## Mapitio & Kujisomea

Katika somo hili, ulitumia Matplotlib na kuanza kufanya kazi na Seaborn kuonyesha michoro ya kisasa zaidi. Fanya utafiti kuhusu `kdeplot` katika Seaborn, "mchoro wa wingi wa uwezekano endelevu katika mwelekeo mmoja au zaidi". Soma [nyaraka](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) ili kuelewa jinsi inavyofanya kazi.

## Kazi

[Tumia ujuzi wako](assignment.md)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.