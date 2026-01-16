<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "47028abaaafa2bcb1079702d20569066",
  "translation_date": "2025-08-28T02:34:20+00:00",
  "source_file": "3-Data-Visualization/R/11-visualization-proportions/README.md",
  "language_code": "tl"
}
-->
# Pagpapakita ng Proporsyon

|![ Sketchnote ni [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Pagpapakita ng Proporsyon - _Sketchnote ni [@nitya](https://twitter.com/nitya)_ |

Sa araling ito, gagamit ka ng dataset na may temang kalikasan upang ipakita ang proporsyon, tulad ng kung gaano karaming iba't ibang uri ng fungi ang makikita sa isang dataset tungkol sa kabute. Tuklasin natin ang mga kamangha-manghang fungi gamit ang dataset mula sa Audubon na naglalaman ng detalye tungkol sa 23 species ng gilled mushrooms sa mga pamilya ng Agaricus at Lepiota. Mag-eeksperimento ka sa masarap na mga visualisasyon tulad ng:

- Pie charts 🥧
- Donut charts 🍩
- Waffle charts 🧇

> 💡 Isang napaka-interesanteng proyekto na tinatawag na [Charticulator](https://charticulator.com) mula sa Microsoft Research ang nag-aalok ng libreng drag-and-drop na interface para sa data visualizations. Sa isa sa kanilang mga tutorial, ginamit din nila ang dataset ng kabute! Kaya maaari mong tuklasin ang data at matutunan ang library nang sabay: [Charticulator tutorial](https://charticulator.com/tutorials/tutorial4.html).

## [Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## Kilalanin ang Iyong mga Kabute 🍄

Ang mga kabute ay napaka-interesante. Mag-import tayo ng dataset upang pag-aralan ang mga ito:

```r
mushrooms = read.csv('../../data/mushrooms.csv')
head(mushrooms)
```
Isang table ang ipinapakita na may magagandang datos para sa pagsusuri:

| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Poisonous | Convex    | Smooth      | Brown     | Bruises | Pungent | Free            | Close        | Narrow    | Black      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |
| Edible    | Convex    | Smooth      | Yellow    | Bruises | Almond  | Free            | Close        | Broad     | Black      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Grasses |
| Edible    | Bell      | Smooth      | White     | Bruises | Anise   | Free            | Close        | Broad     | Brown      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Meadows |
| Poisonous | Convex    | Scaly       | White     | Bruises | Pungent | Free            | Close        | Narrow    | Brown      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban 
| Edible | Convex       |Smooth       | Green     | No Bruises| None   |Free            | Crowded       | Broad     | Black      | Tapering   | Equal      |  Smooth | Smooth                    | White                 | White                  | Partial    | White     | One         | Evanescent | Brown             | Abundant | Grasses
|Edible  |  Convex      | Scaly   | Yellow         | Bruises  | Almond  | Free | Close  |   Broad   |   Brown  | Enlarging   |   Club                      | Smooth                  | Smooth    | White                 |  White                | Partial      | White    |  One  |  Pendant | Black   | Numerous | Grasses
      
Mapapansin mo agad na ang lahat ng datos ay tekstwal. Kailangan mong i-convert ang datos na ito upang magamit ito sa isang chart. Karamihan sa datos, sa katunayan, ay kinakatawan bilang isang object:

```r
names(mushrooms)
```

Ang output ay:

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
Kunin ang datos na ito at i-convert ang 'class' column sa isang kategorya:

```r
library(dplyr)
grouped=mushrooms %>%
  group_by(class) %>%
  summarise(count=n())
```

Ngayon, kung ipi-print mo ang datos ng kabute, makikita mo na ito ay na-grupo sa mga kategorya ayon sa poisonous/edible class:
```r
View(grouped)
```

| class | count |
| --------- | --------- |
| Edible | 4208 |
| Poisonous| 3916 |

Kung susundin mo ang pagkakasunod na ipinakita sa table na ito upang lumikha ng iyong class category labels, maaari kang gumawa ng pie chart.

## Pie!

```r
pie(grouped$count,grouped$class, main="Edible?")
```
Voila, isang pie chart na nagpapakita ng proporsyon ng datos ayon sa dalawang klase ng kabute. Napakahalaga na makuha ang tamang pagkakasunod ng labels, lalo na dito, kaya siguraduhing i-verify ang pagkakasunod ng label array!

![pie chart](../../../../../translated_images/tl/pie1-wb.685df063673751f4b0b82127f7a52c7f9a920192f22ae61ad28412ba9ace97bf.png)

## Donuts!

Ang isang mas visually interesting na pie chart ay isang donut chart, na isang pie chart na may butas sa gitna. Tingnan natin ang ating datos gamit ang pamamaraang ito.

Tingnan ang iba't ibang habitat kung saan tumutubo ang mga kabute:

```r
library(dplyr)
habitat=mushrooms %>%
  group_by(habitat) %>%
  summarise(count=n())
View(habitat)
```
Ang output ay:
| habitat| count |
| --------- | --------- |
| Grasses    | 2148 |
| Leaves| 832 |
| Meadows    | 292 |
| Paths| 1144 |
| Urban    | 368 |
| Waste| 192 |
| Wood| 3148 |

Dito, ini-group mo ang iyong datos ayon sa habitat. Mayroong 7 na nakalista, kaya gamitin ang mga ito bilang labels para sa iyong donut chart:

```r
library(ggplot2)
library(webr)
PieDonut(habitat, aes(habitat, count=count))
```

![donut chart](../../../../../translated_images/tl/donut-wb.34e6fb275da9d834c2205145e39a3de9b6878191dcdba6f7a9e85f4b520449bc.png)

Ang code na ito ay gumagamit ng dalawang library - ggplot2 at webr. Gamit ang PieDonut function ng webr library, madali tayong makakagawa ng donut chart!

Ang mga donut chart sa R ay maaaring gawin gamit lamang ang ggplot2 library. Maaari kang matuto pa tungkol dito [dito](https://www.r-graph-gallery.com/128-ring-or-donut-plot.html) at subukan ito.

Ngayon na alam mo kung paano i-group ang iyong datos at ipakita ito bilang pie o donut, maaari mong tuklasin ang iba pang uri ng chart. Subukan ang waffle chart, na isang kakaibang paraan ng pagpapakita ng dami.

## Waffles!

Ang 'waffle' type chart ay isang kakaibang paraan upang ipakita ang dami bilang isang 2D array ng mga square. Subukang ipakita ang iba't ibang dami ng mushroom cap colors sa dataset na ito. Upang gawin ito, kailangan mong mag-install ng helper library na tinatawag na [waffle](https://cran.r-project.org/web/packages/waffle/waffle.pdf) at gamitin ito upang lumikha ng iyong visualization:

```r
install.packages("waffle", repos = "https://cinc.rud.is")
```

Pumili ng segment ng iyong datos upang i-group:

```r
library(dplyr)
cap_color=mushrooms %>%
  group_by(cap.color) %>%
  summarise(count=n())
View(cap_color)
```

Gumawa ng waffle chart sa pamamagitan ng paglikha ng labels at pagkatapos ay i-group ang iyong datos:

```r
library(waffle)
names(cap_color$count) = paste0(cap_color$cap.color)
waffle((cap_color$count/10), rows = 7, title = "Waffle Chart")+scale_fill_manual(values=c("brown", "#F0DC82", "#D2691E", "green", 
                                                                                     "pink", "purple", "red", "grey", 
                                                                                     "yellow","white"))
```

Gamit ang waffle chart, makikita mo nang malinaw ang proporsyon ng mga cap colors sa dataset ng kabute. Nakakatuwa, maraming green-capped mushrooms!

![waffle chart](../../../../../translated_images/tl/waffle.aaa75c5337735a6ef32ace0ffb6506ef49e5aefe870ffd72b1bb080f4843c217.png)

Sa araling ito, natutunan mo ang tatlong paraan upang ipakita ang proporsyon. Una, kailangan mong i-group ang iyong datos sa mga kategorya at pagkatapos ay magdesisyon kung alin ang pinakamahusay na paraan upang ipakita ang datos - pie, donut, o waffle. Lahat ay masarap at nagbibigay ng instant snapshot ng dataset sa user.

## 🚀 Hamon

Subukang muling likhain ang mga masarap na chart na ito sa [Charticulator](https://charticulator.com).

## [Post-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## Review & Self Study

Minsan hindi halata kung kailan gagamit ng pie, donut, o waffle chart. Narito ang ilang artikulo na maaaring basahin tungkol sa paksang ito:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Mag-research upang makahanap ng higit pang impormasyon tungkol sa desisyong ito.

## Assignment

[Subukan ito sa Excel](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.