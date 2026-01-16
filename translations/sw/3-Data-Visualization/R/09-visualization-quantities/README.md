<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-26T17:07:10+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "sw"
}
-->
# Kuonyesha Kiasi
|![ Sketchnote na [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Kuonyesha Kiasi - _Sketchnote na [@nitya](https://twitter.com/nitya)_ |

Katika somo hili, utachunguza jinsi ya kutumia baadhi ya maktaba za R zilizopo ili kujifunza jinsi ya kuunda taswira za kuvutia zinazohusiana na dhana ya kiasi. Kwa kutumia seti ya data iliyosafishwa kuhusu ndege wa Minnesota, unaweza kujifunza mambo mengi ya kuvutia kuhusu wanyama wa porini wa eneo hilo.  
## [Jaribio la kabla ya somo](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## Angalia upana wa mabawa kwa ggplot2
Maktaba bora ya kuunda michoro rahisi na ya kisasa ya aina mbalimbali ni [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html). Kwa ujumla, mchakato wa kuchora data kwa kutumia maktaba hizi unajumuisha kutambua sehemu za dataframe unazotaka kulenga, kufanya mabadiliko yoyote yanayohitajika kwenye data hiyo, kuainisha thamani za x na y, kuamua aina ya mchoro wa kuonyesha, na kisha kuonyesha mchoro huo.

`ggplot2` ni mfumo wa kuunda michoro kwa njia ya maelezo, kulingana na The Grammar of Graphics. [Grammar of Graphics](https://en.wikipedia.org/wiki/Ggplot2) ni mpango wa jumla wa taswira ya data ambao unagawanya grafu katika vipengele vya maana kama vile mizani na tabaka. Kwa maneno mengine, urahisi wa kuunda michoro na grafu kwa data ya univariate au multivariate kwa kutumia msimbo mdogo hufanya `ggplot2` kuwa kifurushi maarufu zaidi kinachotumika kwa taswira katika R. Mtumiaji huambia `ggplot2` jinsi ya kuunganisha vigezo na aesthetics, primitives za kielelezo za kutumia, na `ggplot2` hushughulikia kilichobaki.

> ✅ Mchoro = Data + Aesthetics + Geometry  
> - Data inahusu seti ya data  
> - Aesthetics inaonyesha vigezo vya kuchunguzwa (vigezo vya x na y)  
> - Geometry inahusu aina ya mchoro (mchoro wa mstari, mchoro wa bar, n.k.)  

Chagua geometry bora (aina ya mchoro) kulingana na data yako na hadithi unayotaka kusimulia kupitia mchoro huo.  

> - Kuchambua mwenendo: mstari, safu  
> - Kulinganisha thamani: bar, safu, pie, scatterplot  
> - Kuonyesha jinsi sehemu zinavyohusiana na jumla: pie  
> - Kuonyesha usambazaji wa data: scatterplot, bar  
> - Kuonyesha uhusiano kati ya thamani: mstari, scatterplot, bubble  

✅ Unaweza pia kuangalia [cheatsheet](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf) hii ya maelezo kwa ggplot2.

## Unda mchoro wa mstari kuhusu thamani za upana wa mabawa ya ndege

Fungua console ya R na uingize seti ya data.  
> Kumbuka: Seti ya data imehifadhiwa katika mzizi wa repo hii kwenye folda ya `/data`.

Hebu tuingize seti ya data na tuangalie kichwa (mistari 5 ya juu) ya data.

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```  
Kichwa cha data kina mchanganyiko wa maandishi na namba:

|      | Jina                          | Jina la Kisayansi      | Kategoria             | Order        | Family   | Genus       | Hali ya Uhifadhi   | MinLength | MaxLength | MinBodyMass | MaxBodyMass | MinWingspan | MaxWingspan |
| ---: | :---------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Hebu tuanze kwa kuchora baadhi ya data ya namba kwa kutumia mchoro wa mstari wa msingi. Tuseme unataka mtazamo wa upana wa mabawa wa juu zaidi kwa ndege hawa wa kuvutia.

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```  
Hapa, unasakinisha kifurushi cha `ggplot2` na kisha unakileta kwenye workspace kwa kutumia amri `library("ggplot2")`. Ili kuchora mchoro wowote katika ggplot, kazi ya `ggplot()` inatumika na unataja seti ya data, vigezo vya x na y kama sifa. Katika kesi hii, tunatumia kazi ya `geom_line()` kwa kuwa tunalenga kuchora mchoro wa mstari.

![MaxWingspan-lineplot](../../../../../translated_images/sw/MaxWingspan-lineplot.b12169f99d26fdd263f291008dfd73c18a4ba8f3d32b1fda3d74af51a0a28616.png)

Unagundua nini mara moja? Inaonekana kuna angalau kipengele kimoja cha nje - huo ni upana wa mabawa wa ajabu! Upana wa mabawa wa zaidi ya sentimita 2000 ni zaidi ya mita 20 - kuna Pterodactyls wanaozunguka Minnesota? Hebu tuchunguze.

Ingawa unaweza kufanya upangaji wa haraka katika Excel ili kupata vipengele vya nje, ambavyo labda ni makosa ya kuandika, endelea na mchakato wa taswira kwa kufanya kazi kutoka ndani ya mchoro.

Ongeza lebo kwenye mhimili wa x ili kuonyesha aina gani ya ndege zinahusika:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```  
Tunataja pembe katika `theme` na tunataja lebo za mhimili wa x na y katika `xlab()` na `ylab()` mtawalia. `ggtitle()` inatoa jina kwa grafu/mchoro.

![MaxWingspan-lineplot-improved](../../../../../translated_images/sw/MaxWingspan-lineplot-improved.04b73b4d5a59552a6bc7590678899718e1f065abe9eada9ebb4148939b622fd4.png)

Hata kwa mzunguko wa lebo uliowekwa kwa digrii 45, kuna nyingi sana kusoma. Hebu jaribu mkakati tofauti: lebo tu kwa vipengele vya nje na weka lebo ndani ya mchoro. Unaweza kutumia mchoro wa scatter ili kutoa nafasi zaidi kwa kuweka lebo:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```  
Nini kinaendelea hapa? Ulitumia kazi ya `geom_point()` kuchora alama za scatter. Kwa hili, uliongeza lebo kwa ndege ambao walikuwa na `MaxWingspan > 500` na pia ulificha lebo kwenye mhimili wa x ili kupunguza msongamano wa mchoro.

Unagundua nini?

![MaxWingspan-scatterplot](../../../../../translated_images/sw/MaxWingspan-scatterplot.60dc9e0e19d32700283558f253841fdab5104abb62bc96f7d97f9c0ee857fa8b.png)

## Chuja data yako

Bald Eagle na Prairie Falcon, ingawa labda ni ndege wakubwa sana, inaonekana wamepewa lebo vibaya, na sifuri ya ziada imeongezwa kwenye upana wao wa mabawa wa juu zaidi. Haiwezekani kukutana na Bald Eagle mwenye upana wa mabawa wa mita 25, lakini ikiwa ni hivyo, tafadhali tujulishe! Hebu tuunde dataframe mpya bila vipengele hivyo vya nje:

```r
birds_filtered <- subset(birds, MaxWingspan < 500)

ggplot(data=birds_filtered, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  ylab("Wingspan (CM)") +
  xlab("Birds") +
  ggtitle("Max Wingspan in Centimeters") + 
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) +
  theme(axis.text.x=element_blank(), axis.ticks.x=element_blank())
```  
Tulitengeneza dataframe mpya `birds_filtered` na kisha tukachora mchoro wa scatter. Kwa kuchuja vipengele vya nje, data yako sasa ni ya mshikamano zaidi na inayoeleweka.

![MaxWingspan-scatterplot-improved](../../../../../translated_images/sw/MaxWingspan-scatterplot-improved.7d0af81658c65f3e75b8fedeb2335399e31108257e48db15d875ece608272051.png)

Sasa kwa kuwa tuna seti ya data safi angalau kwa suala la upana wa mabawa, hebu tujifunze zaidi kuhusu ndege hawa.

Ingawa michoro ya mstari na scatter inaweza kuonyesha taarifa kuhusu thamani za data na usambazaji wake, tunataka kufikiria kuhusu thamani zilizomo katika seti hii ya data. Unaweza kuunda taswira ili kujibu maswali yafuatayo kuhusu kiasi:

> Kuna kategoria ngapi za ndege, na idadi yao ni ngapi?  
> Kuna ndege wangapi waliopotea, walio hatarini, adimu, au wa kawaida?  
> Kuna idadi gani ya genus na order mbalimbali katika terminolojia ya Linnaeus?  
## Chunguza michoro ya bar

Michoro ya bar ni ya vitendo unapohitaji kuonyesha makundi ya data. Hebu tuchunguze kategoria za ndege zilizopo katika seti hii ya data ili kuona ni ipi iliyo ya kawaida zaidi kwa idadi.  
Hebu tuunde mchoro wa bar kwenye data iliyochujwa.

```r
install.packages("dplyr")
install.packages("tidyverse")

library(lubridate)
library(scales)
library(dplyr)
library(ggplot2)
library(tidyverse)

birds_filtered %>% group_by(Category) %>%
  summarise(n=n(),
  MinLength = mean(MinLength),
  MaxLength = mean(MaxLength),
  MinBodyMass = mean(MinBodyMass),
  MaxBodyMass = mean(MaxBodyMass),
  MinWingspan=mean(MinWingspan),
  MaxWingspan=mean(MaxWingspan)) %>% 
  gather("key", "value", - c(Category, n)) %>%
  ggplot(aes(x = Category, y = value, group = key, fill = key)) +
  geom_bar(stat = "identity") +
  scale_fill_manual(values = c("#D62728", "#FF7F0E", "#8C564B","#2CA02C", "#1F77B4", "#9467BD")) +                   
  xlab("Category")+ggtitle("Birds of Minnesota")

```  
Katika kipande kinachofuata, tunasakinisha vifurushi vya [dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8) na [lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0) ili kusaidia kudhibiti na kuunda data kwa lengo la kuchora mchoro wa bar uliojaa. Kwanza, unagawanya data kwa `Category` ya ndege na kisha unatoa muhtasari wa safu za `MinLength`, `MaxLength`, `MinBodyMass`, `MaxBodyMass`, `MinWingspan`, `MaxWingspan`. Kisha, unachora mchoro wa bar kwa kutumia kifurushi cha `ggplot2` na kutaja rangi kwa kategoria tofauti na lebo.

![Stacked bar chart](../../../../../translated_images/sw/stacked-bar-chart.0c92264e89da7b391a7490224d1e7059a020e8b74dcd354414aeac78871c02f1.png)

Hata hivyo, mchoro huu wa bar hauwezi kusomeka kwa sababu kuna data nyingi isiyogawanywa. Unahitaji kuchagua tu data unayotaka kuchora, kwa hivyo hebu tuangalie urefu wa ndege kulingana na kategoria yao.

Chuja data yako ili kujumuisha tu kategoria ya ndege.

Kwa kuwa kuna kategoria nyingi, unaweza kuonyesha mchoro huu kwa wima na kurekebisha urefu wake ili kuzingatia data yote:

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```  
Kwanza unahesabu thamani za kipekee katika safu ya `Category` na kisha unazipanga katika dataframe mpya `birds_count`. Data hii iliyopangwa kisha inafanywa kuwa ya kiwango sawa ili iweze kuchorwa kwa mpangilio uliopangwa. Kwa kutumia `ggplot2` unachora data katika mchoro wa bar. `coord_flip()` inachora bar wima.

![category-length](../../../../../translated_images/sw/category-length.7e34c296690e85d64f7e4d25a56077442683eca96c4f5b4eae120a64c0755636.png)

Mchoro huu wa bar unaonyesha mtazamo mzuri wa idadi ya ndege katika kila kategoria. Kwa haraka, unaona kwamba idadi kubwa ya ndege katika eneo hili wako katika kategoria ya Ducks/Geese/Waterfowl. Minnesota ni 'ardhi ya maziwa 10,000' kwa hivyo hili si la kushangaza!

✅ Jaribu hesabu nyingine kwenye seti hii ya data. Kuna kitu kinachokushangaza?

## Kulinganisha data

Unaweza kujaribu kulinganisha tofauti za data iliyogawanywa kwa kuunda axes mpya. Jaribu kulinganisha MaxLength ya ndege, kulingana na kategoria yake:

```r
birds_grouped <- birds_filtered %>%
  group_by(Category) %>%
  summarise(
  MaxLength = max(MaxLength, na.rm = T),
  MinLength = max(MinLength, na.rm = T)
           ) %>%
  arrange(Category)
  
ggplot(birds_grouped,aes(Category,MaxLength))+geom_bar(stat="identity")+coord_flip()
```  
Tunagawanya data ya `birds_filtered` kwa `Category` na kisha tunachora mchoro wa bar.

![comparing data](../../../../../translated_images/sw/comparingdata.f486a450d61c7ca5416f27f3f55a6a4465d00df3be5e6d33936e9b07b95e2fdd.png)

Hakuna la kushangaza hapa: hummingbirds wana MaxLength ndogo zaidi ikilinganishwa na Pelicans au Geese. Ni vizuri wakati data ina mantiki!

Unaweza kuunda taswira za kuvutia zaidi za michoro ya bar kwa kuweka data juu ya nyingine. Hebu tuweke Minimum na Maximum Length kwenye kategoria fulani ya ndege:

```r
ggplot(data=birds_grouped, aes(x=Category)) +
  geom_bar(aes(y=MaxLength), stat="identity", position ="identity",  fill='blue') +
  geom_bar(aes(y=MinLength), stat="identity", position="identity", fill='orange')+
  coord_flip()
```  
![super-imposed values](../../../../../translated_images/sw/superimposed-values.5363f0705a1da4167625a373a1064331ea3cb7a06a297297d0734fcc9b3819a0.png)

## 🚀 Changamoto

Seti hii ya data ya ndege inatoa utajiri wa taarifa kuhusu aina tofauti za ndege ndani ya mfumo fulani wa ikolojia. Tafuta mtandaoni na uone kama unaweza kupata seti nyingine za data zinazohusiana na ndege. Fanya mazoezi ya kujenga michoro na grafu kuhusu ndege hawa ili kugundua ukweli ambao hukujua.

## [Jaribio la baada ya somo](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## Mapitio na Kujisomea

Somo hili la kwanza limekupa taarifa kuhusu jinsi ya kutumia `ggplot2` kuonyesha kiasi. Fanya utafiti kuhusu njia nyingine za kufanya kazi na seti za data kwa taswira. Tafuta na angalia seti za data ambazo unaweza kuonyesha kwa kutumia vifurushi vingine kama [Lattice](https://stat.ethz.ch/R-manual/R-devel/library/lattice/html/Lattice.html) na [Plotly](https://github.com/plotly/plotly.R#readme).

## Kazi  
[Lines, Scatters, and Bars](assignment.md)  

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.