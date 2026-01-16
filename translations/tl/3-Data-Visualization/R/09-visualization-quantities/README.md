<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-28T02:35:24+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "tl"
}
-->
# Pagpapakita ng Dami

|![Sketchnote ni [(@sketchthedocs)](https://sketchthedocs.dev)](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Pagpapakita ng Dami - _Sketchnote ni [@nitya](https://twitter.com/nitya)_ |

Sa araling ito, matutuklasan mo kung paano gamitin ang ilan sa maraming magagamit na mga library ng R packages upang matutunan kung paano lumikha ng mga kawili-wiling visualisasyon na nakatuon sa konsepto ng dami. Gamit ang isang nalinis na dataset tungkol sa mga ibon ng Minnesota, maaari kang matuto ng maraming kawili-wiling impormasyon tungkol sa lokal na wildlife.

## [Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## Obserbahan ang wingspan gamit ang ggplot2

Isang mahusay na library para sa paggawa ng parehong simple at sopistikadong mga plot at chart ng iba't ibang uri ay ang [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html). Sa pangkalahatang termino, ang proseso ng pag-plot ng data gamit ang mga library na ito ay kinabibilangan ng pagtukoy sa mga bahagi ng iyong dataframe na nais mong i-target, pagsasagawa ng anumang transformasyon sa data na kinakailangan, pag-assign ng mga x at y axis na halaga, pagpapasya kung anong uri ng plot ang ipapakita, at pagkatapos ay ipakita ang plot.

Ang `ggplot2` ay isang sistema para sa deklaratibong paglikha ng mga graphics, batay sa The Grammar of Graphics. Ang [Grammar of Graphics](https://en.wikipedia.org/wiki/Ggplot2) ay isang pangkalahatang scheme para sa data visualization na naghahati sa mga graph sa semantic components tulad ng scales at layers. Sa madaling salita, ang kadalian ng paglikha ng mga plot at graph para sa univariate o multivariate na data gamit ang kaunting code ay ginagawang `ggplot2` ang pinakasikat na package na ginagamit para sa visualisasyon sa R. Sinasabi ng user sa `ggplot2` kung paano i-map ang mga variable sa aesthetics, ang mga graphical primitives na gagamitin, at ang `ggplot2` ang bahala sa natitira.

> ✅ Plot = Data + Aesthetics + Geometry  
> - Ang Data ay tumutukoy sa dataset  
> - Ang Aesthetics ay nagpapahiwatig ng mga variable na pag-aaralan (x at y variables)  
> - Ang Geometry ay tumutukoy sa uri ng plot (line plot, bar plot, atbp.)  

Piliin ang pinakamahusay na geometry (uri ng plot) ayon sa iyong data at sa kwento na nais mong ipakita sa pamamagitan ng plot.

> - Para sa pagsusuri ng mga trend: line, column  
> - Para sa paghahambing ng mga halaga: bar, column, pie, scatterplot  
> - Para ipakita kung paano nauugnay ang mga bahagi sa kabuuan: pie  
> - Para ipakita ang distribusyon ng data: scatterplot, bar  
> - Para ipakita ang relasyon sa pagitan ng mga halaga: line, scatterplot, bubble  

✅ Maaari mo ring tingnan ang detalyadong [cheatsheet](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf) para sa ggplot2.

## Gumawa ng line plot tungkol sa mga halaga ng wingspan ng ibon

Buksan ang R console at i-import ang dataset.  
> Note: Ang dataset ay naka-imbak sa root ng repo na ito sa `/data` folder.

I-import natin ang dataset at obserbahan ang head (nangungunang 5 rows) ng data.

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```  
Ang head ng data ay may halo ng text at mga numero:

|      | Pangalan                      | ScientificName         | Kategorya             | Order        | Pamilya  | Genus       | ConservationStatus | MinLength | MaxLength | MinBodyMass | MaxBodyMass | MinWingspan | MaxWingspan |
| ---: | :---------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Simulan natin sa pag-plot ng ilang numeric na data gamit ang isang basic line plot. Halimbawa, gusto mong makita ang maximum wingspan ng mga kawili-wiling ibon na ito.

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```  
Dito, ini-install mo ang `ggplot2` package at pagkatapos ay ini-import ito sa workspace gamit ang `library("ggplot2")` command. Para mag-plot ng anumang plot sa ggplot, ginagamit ang `ggplot()` function at tinutukoy mo ang dataset, x at y variables bilang attributes. Sa kasong ito, ginagamit natin ang `geom_line()` function dahil layunin nating mag-plot ng line plot.

![MaxWingspan-lineplot](../../../../../translated_images/tl/MaxWingspan-lineplot.b12169f99d26fdd263f291008dfd73c18a4ba8f3d32b1fda3d74af51a0a28616.png)

Ano ang napansin mo agad? Mukhang mayroong hindi bababa sa isang outlier - napakalaki ng wingspan! Ang wingspan na higit sa 2000 sentimetro ay katumbas ng higit sa 20 metro - may mga Pterodactyl ba sa Minnesota? Suriin natin.

Bagama't maaari kang gumawa ng mabilis na sort sa Excel upang mahanap ang mga outlier na ito, na malamang na mga typo, ipagpatuloy ang proseso ng visualisasyon sa pamamagitan ng pagtatrabaho mula sa loob ng plot.

Magdagdag ng mga label sa x-axis upang ipakita kung anong uri ng mga ibon ang pinag-uusapan:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```  
Tinutukoy natin ang anggulo sa `theme` at tinutukoy ang mga label ng x at y axis sa `xlab()` at `ylab()` ayon sa pagkakabanggit. Ang `ggtitle()` ay nagbibigay ng pangalan sa graph/plot.

![MaxWingspan-lineplot-improved](../../../../../translated_images/tl/MaxWingspan-lineplot-improved.04b73b4d5a59552a6bc7590678899718e1f065abe9eada9ebb4148939b622fd4.png)

Kahit na may rotation ng mga label na nakatakda sa 45 degrees, masyadong marami ang mga ito para basahin. Subukan natin ang ibang estratehiya: lagyan lamang ng label ang mga outlier at itakda ang mga label sa loob ng chart. Maaari kang gumamit ng scatter chart upang magkaroon ng mas maraming espasyo para sa paglalagay ng label:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```  
Ano ang nangyayari dito? Ginamit mo ang `geom_point()` function upang mag-plot ng scatter points. Sa ganito, nagdagdag ka ng mga label para sa mga ibon na may `MaxWingspan > 500` at itinago rin ang mga label sa x axis upang mabawasan ang kalat sa plot.

Ano ang natuklasan mo?

![MaxWingspan-scatterplot](../../../../../translated_images/tl/MaxWingspan-scatterplot.60dc9e0e19d32700283558f253841fdab5104abb62bc96f7d97f9c0ee857fa8b.png)

## I-filter ang iyong data

Ang Bald Eagle at Prairie Falcon, bagama't malamang na napakalaking mga ibon, ay mukhang maling na-label, na may dagdag na 0 na idinagdag sa kanilang maximum wingspan. Hindi malamang na makakita ka ng Bald Eagle na may 25 metrong wingspan, ngunit kung sakali, ipaalam sa amin! Gumawa tayo ng bagong dataframe na walang dalawang outlier na ito:

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
Gumawa tayo ng bagong dataframe `birds_filtered` at pagkatapos ay nag-plot ng scatter plot. Sa pamamagitan ng pag-filter ng mga outlier, ang iyong data ay mas cohesive at mas madaling maunawaan.

![MaxWingspan-scatterplot-improved](../../../../../translated_images/tl/MaxWingspan-scatterplot-improved.7d0af81658c65f3e75b8fedeb2335399e31108257e48db15d875ece608272051.png)

Ngayon na mayroon tayong mas malinis na dataset, hindi bababa sa mga tuntunin ng wingspan, tuklasin natin ang higit pa tungkol sa mga ibon na ito.

Bagama't ang mga line at scatter plots ay maaaring magpakita ng impormasyon tungkol sa mga halaga ng data at kanilang distribusyon, nais nating pag-isipan ang mga halaga na likas sa dataset na ito. Maaari kang lumikha ng mga visualisasyon upang sagutin ang mga sumusunod na tanong tungkol sa dami:

> Ilan ang mga kategorya ng ibon, at ano ang kanilang bilang?  
> Ilan ang mga ibon na extinct, endangered, rare, o common?  
> Ilan ang mayroon sa iba't ibang genus at orders sa terminolohiya ni Linnaeus?  

## Tuklasin ang mga bar chart

Ang mga bar chart ay praktikal kapag kailangan mong ipakita ang mga grupo ng data. Tuklasin natin ang mga kategorya ng ibon na umiiral sa dataset na ito upang makita kung alin ang pinakakaraniwan batay sa bilang.  
Gumawa tayo ng bar chart sa filtered data.

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
Sa sumusunod na snippet, ini-install natin ang [dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8) at [lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0) packages upang makatulong sa pag-manipula at pag-group ng data upang mag-plot ng stacked bar chart. Una, i-group mo ang data batay sa `Category` ng ibon at pagkatapos ay i-summarize ang `MinLength`, `MaxLength`, `MinBodyMass`, `MaxBodyMass`, `MinWingspan`, `MaxWingspan` columns. Pagkatapos, i-plot ang bar chart gamit ang `ggplot2` package at tukuyin ang mga kulay para sa iba't ibang kategorya at mga label.

![Stacked bar chart](../../../../../translated_images/tl/stacked-bar-chart.0c92264e89da7b391a7490224d1e7059a020e8b74dcd354414aeac78871c02f1.png)

Gayunpaman, ang bar chart na ito ay hindi mababasa dahil masyadong maraming hindi naka-group na data. Kailangan mong piliin lamang ang data na nais mong i-plot, kaya't tingnan natin ang haba ng mga ibon batay sa kanilang kategorya.

I-filter ang iyong data upang isama lamang ang kategorya ng ibon.

Dahil maraming kategorya, maaari mong ipakita ang chart na ito nang patayo at i-tweak ang taas nito upang ma-accommodate ang lahat ng data:

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```  
Una mong binibilang ang mga unique na halaga sa `Category` column at pagkatapos ay inaayos ang mga ito sa isang bagong dataframe `birds_count`. Ang sorted data na ito ay pagkatapos ay factored sa parehong level upang ito ay ma-plot sa sorted na paraan. Gamit ang `ggplot2` ay i-plot mo ang data sa isang bar chart. Ang `coord_flip()` ay nag-plot ng horizontal bars.

![category-length](../../../../../translated_images/tl/category-length.7e34c296690e85d64f7e4d25a56077442683eca96c4f5b4eae120a64c0755636.png)

Ang bar chart na ito ay nagpapakita ng magandang view ng bilang ng mga ibon sa bawat kategorya. Sa isang sulyap, makikita mo na ang pinakamalaking bilang ng mga ibon sa rehiyong ito ay nasa kategoryang Ducks/Geese/Waterfowl. Ang Minnesota ay ang 'land of 10,000 lakes' kaya't hindi ito nakakagulat!

✅ Subukan ang ilang iba pang bilang sa dataset na ito. Mayroon bang bagay na ikinagulat mo?

## Paghahambing ng data

Maaari kang mag-eksperimento sa iba't ibang paghahambing ng grouped data sa pamamagitan ng paglikha ng mga bagong axes. Subukan ang paghahambing ng MaxLength ng isang ibon, batay sa kanyang kategorya:

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
I-group natin ang `birds_filtered` data batay sa `Category` at pagkatapos ay mag-plot ng bar graph.

![comparing data](../../../../../translated_images/tl/comparingdata.f486a450d61c7ca5416f27f3f55a6a4465d00df3be5e6d33936e9b07b95e2fdd.png)

Walang nakakagulat dito: ang mga hummingbird ay may pinakamaliit na MaxLength kumpara sa Pelicans o Geese. Maganda kapag ang data ay may lohikal na kahulugan!

Maaari kang lumikha ng mas kawili-wiling visualisasyon ng mga bar chart sa pamamagitan ng pag-superimpose ng data. I-superimpose natin ang Minimum at Maximum Length sa isang ibinigay na kategorya ng ibon:

```r
ggplot(data=birds_grouped, aes(x=Category)) +
  geom_bar(aes(y=MaxLength), stat="identity", position ="identity",  fill='blue') +
  geom_bar(aes(y=MinLength), stat="identity", position="identity", fill='orange')+
  coord_flip()
```  
![super-imposed values](../../../../../translated_images/tl/superimposed-values.5363f0705a1da4167625a373a1064331ea3cb7a06a297297d0734fcc9b3819a0.png)

## 🚀 Hamon

Ang dataset ng ibon na ito ay nag-aalok ng maraming impormasyon tungkol sa iba't ibang uri ng ibon sa loob ng isang partikular na ecosystem. Maghanap sa internet at tingnan kung makakahanap ka ng iba pang mga dataset na nakatuon sa ibon. Magpraktis sa paggawa ng mga chart at graph tungkol sa mga ibon na ito upang matuklasan ang mga bagay na hindi mo inaasahan.

## [Post-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## Review at Pag-aaral ng Sarili

Ang unang araling ito ay nagbigay sa iyo ng ilang impormasyon tungkol sa kung paano gamitin ang `ggplot2` upang mag-visualize ng dami. Mag-research tungkol sa iba pang paraan upang magtrabaho sa mga dataset para sa visualisasyon. Maghanap at mag-research ng mga dataset na maaari mong i-visualize gamit ang iba pang mga package tulad ng [Lattice](https://stat.ethz.ch/R-manual/R-devel/library/lattice/html/Lattice.html) at [Plotly](https://github.com/plotly/plotly.R#readme).

## Takdang-Aralin  
[Lines, Scatters, and Bars](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang orihinal na wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.