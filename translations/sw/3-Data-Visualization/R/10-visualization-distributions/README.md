<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea67c0c40808fd723594de6896c37ccf",
  "translation_date": "2025-08-26T16:58:41+00:00",
  "source_file": "3-Data-Visualization/R/10-visualization-distributions/README.md",
  "language_code": "sw"
}
-->
# Kuonyesha Usambazaji wa Takwimu

|![ Sketchnote na [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Kuonyesha Usambazaji wa Takwimu - _Sketchnote na [@nitya](https://twitter.com/nitya)_ |

Katika somo lililopita, ulijifunza mambo ya kuvutia kuhusu seti ya data ya ndege wa Minnesota. Ulitambua data yenye makosa kwa kuonyesha vipimo vya nje na ukaangalia tofauti kati ya makundi ya ndege kulingana na urefu wao wa juu zaidi.

## [Jaribio la kabla ya somo](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## Chunguza seti ya data ya ndege

Njia nyingine ya kuchunguza data ni kwa kuangalia usambazaji wake, yaani jinsi data imepangwa kwenye mhimili. Labda, kwa mfano, ungependa kujifunza kuhusu usambazaji wa jumla wa urefu wa mabawa wa juu zaidi au uzito wa juu zaidi wa mwili wa ndege wa Minnesota katika seti hii ya data.

Hebu tugundue baadhi ya ukweli kuhusu usambazaji wa data katika seti hii ya data. Katika R console yako, ingiza `ggplot2` na hifadhidata. Ondoa vipimo vya nje kutoka kwenye hifadhidata kama ulivyofanya katika mada iliyopita.

```r
library(ggplot2)

birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")

birds_filtered <- subset(birds, MaxWingspan < 500)
head(birds_filtered)
```
|      | Jina                          | Jina la Kisayansi      | Jamii                | Oda          | Familia  | Jinsia      | Hali ya Uhifadhi   | UrefuMdogo | UrefuMkuu | UzitoMdogo  | UzitoMkuu   | MabawaMdogo | MabawaMkuu  |
| ---: | :--------------------------- | :--------------------- | :------------------- | :----------- | :------- | :---------- | :---------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Bata/Bata-maji       | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Bata/Bata-maji       | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Bata/Bata-maji       | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Bata/Bata-maji       | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Bata/Bata-maji       | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Kwa ujumla, unaweza kuangalia haraka jinsi data inavyosambazwa kwa kutumia mchoro wa alama kama tulivyofanya katika somo lililopita:

```r
ggplot(data=birds_filtered, aes(x=Order, y=MaxLength,group=1)) +
  geom_point() +
  ggtitle("Max Length per order") + coord_flip()
```
![urefu wa juu kwa oda](../../../../../translated_images/sw/max-length-per-order.e5b283d952c78c12b091307c5d3cf67132dad6fefe80a073353b9dc5c2bd3eb8.png)

Hii inatoa muhtasari wa usambazaji wa jumla wa urefu wa mwili kwa kila Oda ya ndege, lakini si njia bora ya kuonyesha usambazaji wa kweli. Kazi hii kawaida hufanywa kwa kuunda Histogramu.

## Kufanya kazi na histogramu

`ggplot2` inatoa njia nzuri sana za kuonyesha usambazaji wa data kwa kutumia Histogramu. Aina hii ya mchoro ni kama mchoro wa nguzo ambapo usambazaji unaweza kuonekana kupitia kupanda na kushuka kwa nguzo. Ili kujenga histogramu, unahitaji data ya namba. Ili kujenga Histogramu, unaweza kuchora mchoro ukifafanua aina kama 'hist' kwa Histogramu. Mchoro huu unaonyesha usambazaji wa UzitoMkuu wa Mwili kwa seti nzima ya data ya namba. Kwa kugawanya safu ya data iliyotolewa katika sehemu ndogo, inaweza kuonyesha usambazaji wa thamani za data:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=10)+ylab('Frequency')
```
![usambazaji wa seti nzima ya data](../../../../../translated_images/sw/distribution-over-the-entire-dataset.d22afd3fa96be854e4c82213fedec9e3703cba753d07fad4606aadf58cf7e78e.png)

Kama unavyoona, ndege wengi zaidi ya 400 katika seti hii ya data wanaangukia katika safu ya chini ya 2000 kwa UzitoMkuu wa Mwili wao. Pata ufahamu zaidi kuhusu data kwa kubadilisha kipengele cha `bins` kuwa namba kubwa zaidi, kama 30:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + geom_histogram(bins=30)+ylab('Frequency')
```

![usambazaji-30bins](../../../../../translated_images/sw/distribution-30bins.6a3921ea7a421bf71f06bf5231009e43d1146f1b8da8dc254e99b5779a4983e5.png)

Mchoro huu unaonyesha usambazaji kwa undani zaidi. Mchoro usioegemea sana upande wa kushoto unaweza kuundwa kwa kuhakikisha kuwa unachagua tu data ndani ya safu fulani:

Chuja data yako ili kupata ndege wale tu ambao uzito wa mwili wao uko chini ya 60, na uonyeshe `bins` 30:

```r
birds_filtered_1 <- subset(birds_filtered, MaxBodyMass > 1 & MaxBodyMass < 60)
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=30)+ylab('Frequency')
```

![histogramu iliyochujwa](../../../../../translated_images/sw/filtered-histogram.6bf5d2bfd82533220e1bd4bc4f7d14308f43746ed66721d9ec8f460732be6674.png)

✅ Jaribu vichujio vingine na pointi za data. Ili kuona usambazaji kamili wa data, ondoa kichujio cha `['MaxBodyMass']` ili kuonyesha usambazaji ulio na lebo.

Histogramu inatoa rangi nzuri na maboresho ya kuweka lebo pia:

Unda histogramu ya 2D ili kulinganisha uhusiano kati ya usambazaji mbili. Hebu tulinganishe `MaxBodyMass` dhidi ya `MaxLength`. `ggplot2` inatoa njia iliyojengwa ndani ya kuonyesha mwelekeo kwa kutumia rangi angavu zaidi:

```r
ggplot(data=birds_filtered_1, aes(x=MaxBodyMass, y=MaxLength) ) +
  geom_bin2d() +scale_fill_continuous(type = "viridis")
```
Inaonekana kuna uhusiano unaotarajiwa kati ya vipengele hivi viwili kwenye mhimili unaotarajiwa, na sehemu moja yenye nguvu ya mwelekeo:

![mchoro wa 2d](../../../../../translated_images/sw/2d-plot.c504786f439bd7ebceebf2465c70ca3b124103e06c7ff7214bf24e26f7aec21e.png)

Histogramu hufanya kazi vizuri kwa chaguo-msingi kwa data ya namba. Je, unahitaji kuona usambazaji kulingana na data ya maandishi?

## Chunguza seti ya data kwa usambazaji kwa kutumia data ya maandishi 

Seti hii ya data pia inajumuisha taarifa nzuri kuhusu jamii ya ndege na jinsia, spishi, na familia yao pamoja na hali yao ya uhifadhi. Hebu tuchunguze taarifa hii ya uhifadhi. Je, usambazaji wa ndege kulingana na hali yao ya uhifadhi ukoje?

> ✅ Katika seti ya data, vifupisho kadhaa vinatumika kuelezea hali ya uhifadhi. Vifupisho hivi vinatoka kwa [IUCN Red List Categories](https://www.iucnredlist.org/), shirika linaloorodhesha hali ya spishi.
> 
> - CR: Hatari Sana
> - EN: Hatari
> - EX: Waliotoweka
> - LC: Wasiokuwa na Wasiwasi
> - NT: Karibu na Hatari
> - VU: Wenye Hatari

Hizi ni thamani za maandishi kwa hivyo utahitaji kufanya mabadiliko ili kuunda histogramu. Ukichukua dataframe ya filteredBirds, onyesha hali yake ya uhifadhi pamoja na MabawaMdogo. Unaona nini?

```r
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'EX'] <- 'x1' 
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'CR'] <- 'x2'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'EN'] <- 'x3'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'NT'] <- 'x4'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'VU'] <- 'x5'
birds_filtered_1$ConservationStatus[birds_filtered_1$ConservationStatus == 'LC'] <- 'x6'

ggplot(data=birds_filtered_1, aes(x = MinWingspan, fill = ConservationStatus)) +
  geom_histogram(position = "identity", alpha = 0.4, bins = 20) +
  scale_fill_manual(name="Conservation Status",values=c("red","green","blue","pink"),labels=c("Endangered","Near Threathened","Vulnerable","Least Concern"))
```

![mabawa na hali ya uhifadhi](../../../../../translated_images/sw/wingspan-conservation-collation.4024e9aa6910866aa82f0c6cb6a6b4b925bd10079e6b0ef8f92eefa5a6792f76.png)

Haionekani kuwa na uhusiano mzuri kati ya mabawa madogo na hali ya uhifadhi. Jaribu vipengele vingine vya seti ya data kwa kutumia njia hii. Je, unapata uhusiano wowote?

## Mchoro wa Msongamano

Huenda umeona kuwa histogramu tulizozitazama hadi sasa ni za 'vipande' na hazina mtiririko mzuri wa mviringo. Ili kuonyesha mchoro wa msongamano ulio laini zaidi, unaweza kujaribu mchoro wa msongamano.

Hebu tufanye kazi na mchoro wa msongamano sasa!

```r
ggplot(data = birds_filtered_1, aes(x = MinWingspan)) + 
  geom_density()
```
![mchoro wa msongamano](../../../../../translated_images/sw/density-plot.675ccf865b76c690487fb7f69420a8444a3515f03bad5482886232d4330f5c85.png)

Unaweza kuona jinsi mchoro unavyoakisi ule wa awali wa data ya MabawaMdogo; ni laini kidogo tu. Ikiwa ungependa kurejea mstari wa vipande wa UzitoMkuu wa Mwili katika mchoro wa pili uliounda, ungeweza kuulainisha vizuri kwa kuunda upya kwa kutumia njia hii:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density()
```
![msongamano wa uzito wa mwili](../../../../../translated_images/sw/bodymass-smooth.d31ce526d82b0a1f19a073815dea28ecfbe58145ec5337e4ef7e8cdac81120b3.png)

Ikiwa ungependa mstari ulio laini, lakini si laini sana, hariri kipengele cha `adjust`: 

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density(adjust = 1/5)
```
![msongamano wa uzito wa mwili usio laini sana](../../../../../translated_images/sw/less-smooth-bodymass.10f4db8b683cc17d17b2d33f22405413142004467a1493d416608dafecfdee23.png)

✅ Soma kuhusu vigezo vinavyopatikana kwa aina hii ya mchoro na ujaribu!

Aina hii ya mchoro inatoa vielelezo vya kuelezea vizuri. Kwa mistari michache ya msimbo, kwa mfano, unaweza kuonyesha msongamano wa uzito wa juu wa mwili kwa kila Oda ya ndege:

```r
ggplot(data=birds_filtered_1,aes(x = MaxBodyMass, fill = Order)) +
  geom_density(alpha=0.5)
```
![uzito wa mwili kwa oda](../../../../../translated_images/sw/bodymass-per-order.9d2b065dd931b928c839d8cdbee63067ab1ae52218a1b90717f4bc744354f485.png)

## 🚀 Changamoto

Histogramu ni aina ya mchoro wa hali ya juu zaidi kuliko michoro ya alama, nguzo, au mistari ya msingi. Tafuta mifano mizuri ya matumizi ya histogramu kwenye mtandao. Zinatumika vipi, zinaonyesha nini, na katika nyanja au maeneo gani ya uchunguzi zinatumiwa mara nyingi?

## [Jaribio la baada ya somo](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## Mapitio na Kujisomea

Katika somo hili, ulitumia `ggplot2` na kuanza kufanya kazi kuonyesha michoro ya hali ya juu zaidi. Fanya utafiti kuhusu `geom_density_2d()` ambayo ni "mchoro wa msongamano wa uwezekano unaoendelea katika mwelekeo mmoja au zaidi". Soma [nyaraka](https://ggplot2.tidyverse.org/reference/geom_density_2d.html) ili kuelewa jinsi inavyofanya kazi.

## Kazi

[Tumia ujuzi wako](assignment.md)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.