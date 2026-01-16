<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "47028abaaafa2bcb1079702d20569066",
  "translation_date": "2025-08-26T17:18:48+00:00",
  "source_file": "3-Data-Visualization/R/11-visualization-proportions/README.md",
  "language_code": "sw"
}
-->
# Kuonyesha Uwiano

|![ Sketchnote na [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Kuonyesha Uwiano - _Sketchnote na [@nitya](https://twitter.com/nitya)_ |

Katika somo hili, utatumia seti ya data inayohusiana na asili ili kuonyesha uwiano, kama vile idadi ya aina tofauti za uyoga zinazopatikana katika seti ya data kuhusu uyoga. Hebu tuchunguze uyoga huu wa kuvutia kwa kutumia seti ya data kutoka Audubon inayoorodhesha maelezo kuhusu spishi 23 za uyoga wenye magamba katika familia za Agaricus na Lepiota. Utajaribu mbinu za kuvutia za kuonyesha data kama:

- Chati za pai 🥧
- Chati za donati 🍩
- Chati za waffle 🧇

> 💡 Mradi wa kuvutia sana unaoitwa [Charticulator](https://charticulator.com) na Microsoft Research unatoa kiolesura cha bure cha kuburuta na kudondosha kwa ajili ya kuonyesha data. Katika mojawapo ya mafunzo yao wanatumia seti ya data ya uyoga! Kwa hivyo unaweza kuchunguza data na kujifunza maktaba hiyo kwa wakati mmoja: [Mafunzo ya Charticulator](https://charticulator.com/tutorials/tutorial4.html).

## [Jaribio la kabla ya somo](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## Fahamu uyoga wako 🍄

Uyoga ni wa kuvutia sana. Hebu tuingize seti ya data ili kuwasoma:

```r
mushrooms = read.csv('../../data/mushrooms.csv')
head(mushrooms)
```
Jedwali linachapishwa likiwa na data nzuri kwa uchambuzi:


| darasa     | umbo la kofia | uso wa kofia | rangi ya kofia | majeraha | harufu    | kiambatisho cha magamba | nafasi ya magamba | ukubwa wa magamba | rangi ya magamba | umbo la shina | mzizi wa shina | uso wa shina juu ya pete | uso wa shina chini ya pete | rangi ya shina juu ya pete | rangi ya shina chini ya pete | aina ya pazia | rangi ya pazia | idadi ya pete | aina ya pete | rangi ya uchapaji wa spora | idadi ya watu | makazi |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Sumu | Mbonyeo    | Laini      | Kahawia     | Majeraha | Chungu | Huru            | Karibu        | Nyembamba    | Nyeusi      | Inapanuka   | Sawa      | Laini                   | Laini                   | Nyeupe                  | Nyeupe                  | Sehemu   | Nyeupe      | Moja         | Inaning'inia   | Nyeusi             | Imetawanyika  | Mjini   |
| Chakula    | Mbonyeo    | Laini      | Njano    | Majeraha | Mlozi  | Huru            | Karibu        | Pana     | Nyeusi      | Inapanuka   | Klabu       | Laini                   | Laini                   | Nyeupe                  | Nyeupe                  | Sehemu   | Nyeupe      | Moja         | Inaning'inia   | Kahawia             | Nyingi   | Nyasi |
| Chakula    | Kengele      | Laini      | Nyeupe     | Majeraha | Anise   | Huru            | Karibu        | Pana     | Kahawia      | Inapanuka   | Klabu       | Laini                   | Laini                   | Nyeupe                  | Nyeupe                  | Sehemu   | Nyeupe      | Moja         | Inaning'inia   | Kahawia             | Nyingi   | Malisho |
| Sumu | Mbonyeo    | Magamba       | Nyeupe     | Majeraha | Chungu | Huru            | Karibu        | Nyembamba    | Kahawia      | Inapanuka   | Sawa      | Laini                   | Laini                   | Nyeupe                  | Nyeupe                  | Sehemu   | Nyeupe      | Moja         | Inaning'inia   | Nyeusi             | Imetawanyika  | Mjini 
| Chakula | Mbonyeo       |Laini       | Kijani     | Hakuna Majeraha| Hakuna   |Huru            | Imejaa       | Pana     | Nyeusi      | Inakonda   | Sawa      |  Laini | Laini                    | Nyeupe                 | Nyeupe                  | Sehemu    | Nyeupe     | Moja         | Inatoweka | Kahawia             | Tele | Nyasi
|Chakula  |  Mbonyeo      | Magamba   | Njano         | Majeraha  | Mlozi  | Huru | Karibu  |   Pana   |   Kahawia  | Inapanuka   |   Klabu                      | Laini                  | Laini    | Nyeupe                 |  Nyeupe                | Sehemu      | Nyeupe    |  Moja  |  Inaning'inia | Nyeusi   | Nyingi | Nyasi
      
Mara moja, unagundua kuwa data yote ni ya maandishi. Utalazimika kubadilisha data hii ili uweze kuitumia katika chati. Kwa kweli, data nyingi inawakilishwa kama kitu:

```r
names(mushrooms)
```

Matokeo ni:

```output
[1] "class"                    "cap.shape"               
 [3] "cap.surface"              "cap.color"               
 [5] "bruises"                  "odor"                    
 [7] "gill.attachment"          "gill.spacing"            
 [9] "gill.size"                "gill.color"              
[11] "stalk.shape"              "stalk.root"              
[13] "stalk.surface.above.ring" "stalk.surface.below.ring"
[15] "stalk.color.above.ring"   "stalk.color.below.ring"  
[17] "veil.type"                "veil.color"              
[19] "ring.number"              "ring.type"               
[21] "spore.print.color"        "population"              
[23] "habitat"            
```
Chukua data hii na ubadilishe safu ya 'darasa' kuwa kategoria:

```r
library(dplyr)
grouped=mushrooms %>%
  group_by(class) %>%
  summarise(count=n())
```


Sasa, ukichapisha data ya uyoga, utaona kuwa imepangwa katika kategoria kulingana na darasa la sumu/chakula:
```r
View(grouped)
```


| darasa | idadi |
| --------- | --------- |
| Chakula | 4208 |
| Sumu| 3916 |



Ukifuata mpangilio uliowasilishwa katika jedwali hili kuunda lebo za kategoria za darasa, unaweza kujenga chati ya pai. 

## Pai!

```r
pie(grouped$count,grouped$class, main="Edible?")
```
Voila, chati ya pai inayoonyesha uwiano wa data hii kulingana na madarasa haya mawili ya uyoga. Ni muhimu sana kupata mpangilio wa lebo sahihi, hasa hapa, kwa hivyo hakikisha unathibitisha mpangilio ambao safu ya lebo imejengwa!

![chati ya pai](../../../../../translated_images/sw/pie1-wb.685df063673751f4b0b82127f7a52c7f9a920192f22ae61ad28412ba9ace97bf.png)

## Donati!

Chati ya pai yenye kuvutia zaidi kwa macho ni chati ya donati, ambayo ni chati ya pai yenye shimo katikati. Hebu tuangalie data yetu kwa kutumia mbinu hii.

Angalia makazi mbalimbali ambapo uyoga hukua:

```r
library(dplyr)
habitat=mushrooms %>%
  group_by(habitat) %>%
  summarise(count=n())
View(habitat)
```
Matokeo ni:
| makazi| idadi |
| --------- | --------- |
| Nyasi    | 2148 |
| Majani| 832 |
| Malisho    | 292 |
| Njia| 1144 |
| Mjini    | 368 |
| Taka| 192 |
| Miti| 3148 |


Hapa, unapangilia data yako kwa makazi. Kuna 7 yaliyoorodheshwa, kwa hivyo tumia hayo kama lebo za chati yako ya donati:

```r
library(ggplot2)
library(webr)
PieDonut(habitat, aes(habitat, count=count))
```

![chati ya donati](../../../../../translated_images/sw/donut-wb.34e6fb275da9d834c2205145e39a3de9b6878191dcdba6f7a9e85f4b520449bc.png)

Msimbo huu unatumia maktaba mbili - ggplot2 na webr. Kwa kutumia kipengele cha PieDonut cha maktaba ya webr, tunaweza kuunda chati ya donati kwa urahisi!

Chati za donati katika R zinaweza kufanywa kwa kutumia maktaba ya ggplot2 pekee pia. Unaweza kujifunza zaidi kuhusu hilo [hapa](https://www.r-graph-gallery.com/128-ring-or-donut-plot.html) na ujaribu mwenyewe.

Sasa kwa kuwa unajua jinsi ya kupanga data yako na kisha kuionyesha kama pai au donati, unaweza kuchunguza aina nyingine za chati. Jaribu chati ya waffle, ambayo ni njia tofauti ya kuchunguza idadi.

## Waffle!

Chati ya aina ya 'waffle' ni njia tofauti ya kuonyesha idadi kama safu ya 2D ya miraba. Jaribu kuonyesha idadi tofauti za rangi za kofia za uyoga katika seti hii ya data. Ili kufanya hivyo, unahitaji kusakinisha maktaba ya msaidizi inayoitwa [waffle](https://cran.r-project.org/web/packages/waffle/waffle.pdf) na kuitumia kuunda chati yako:

```r
install.packages("waffle", repos = "https://cinc.rud.is")
```

Chagua sehemu ya data yako ili kupanga:

```r
library(dplyr)
cap_color=mushrooms %>%
  group_by(cap.color) %>%
  summarise(count=n())
View(cap_color)
```

Unda chati ya waffle kwa kuunda lebo na kisha kupanga data yako:

```r
library(waffle)
names(cap_color$count) = paste0(cap_color$cap.color)
waffle((cap_color$count/10), rows = 7, title = "Waffle Chart")+scale_fill_manual(values=c("brown", "#F0DC82", "#D2691E", "green", 
                                                                                     "pink", "purple", "red", "grey", 
                                                                                     "yellow","white"))
```

Kwa kutumia chati ya waffle, unaweza kuona wazi uwiano wa rangi za kofia za uyoga katika seti hii ya data. Cha kuvutia, kuna uyoga wengi wenye kofia za kijani!

![chati ya waffle](../../../../../translated_images/sw/waffle.aaa75c5337735a6ef32ace0ffb6506ef49e5aefe870ffd72b1bb080f4843c217.png)

Katika somo hili, ulijifunza njia tatu za kuonyesha uwiano. Kwanza, unahitaji kupanga data yako katika kategoria na kisha kuamua ni njia gani bora ya kuonyesha data - pai, donati, au waffle. Zote ni tamu na zinamfurahisha mtumiaji kwa muhtasari wa haraka wa seti ya data.

## 🚀 Changamoto

Jaribu kuunda upya chati hizi tamu katika [Charticulator](https://charticulator.com).
## [Jaribio la baada ya somo](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## Mapitio & Kujisomea

Wakati mwingine si rahisi kujua ni lini utumie pai, donati, au chati ya waffle. Hapa kuna makala za kusoma kuhusu mada hii:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Fanya utafiti ili kupata maelezo zaidi kuhusu uamuzi huu mgumu.

## Kazi

[Jaribu katika Excel](assignment.md)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.