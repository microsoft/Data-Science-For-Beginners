<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea67c0c40808fd723594de6896c37ccf",
  "translation_date": "2025-08-28T02:37:12+00:00",
  "source_file": "3-Data-Visualization/R/10-visualization-distributions/README.md",
  "language_code": "tl"
}
-->
# Pagpapakita ng Pamamahagi

|![ Sketchnote ni [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Pagpapakita ng Pamamahagi - _Sketchnote ni [@nitya](https://twitter.com/nitya)_ |

Sa nakaraang aralin, natutunan mo ang ilang kawili-wiling impormasyon tungkol sa dataset ng mga ibon sa Minnesota. Nakakita ka ng maling datos sa pamamagitan ng pagpapakita ng mga outlier at tiningnan ang mga pagkakaiba sa pagitan ng mga kategorya ng ibon batay sa kanilang maximum na haba.

## [Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## Tuklasin ang dataset ng mga ibon

Isa pang paraan upang suriin ang datos ay sa pamamagitan ng pagtingin sa pamamahagi nito, o kung paano nakaayos ang datos sa isang axis. Halimbawa, maaaring gusto mong malaman ang pangkalahatang pamamahagi, para sa dataset na ito, ng maximum na wingspan o maximum na body mass ng mga ibon sa Minnesota.

Tuklasin natin ang ilang impormasyon tungkol sa pamamahagi ng datos sa dataset na ito. Sa iyong R console, i-import ang `ggplot2` at ang database. Alisin ang mga outlier mula sa database tulad ng ginawa sa nakaraang paksa.

```r
library(ggplot2)

birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")

birds_filtered <- subset(birds, MaxWingspan < 500)
head(birds_filtered)
```
|      | Pangalan                     | Pangalan Siyentipiko    | Kategorya             | Order        | Pamilya  | Genus       | Kalagayan ng Konserbasyon | MinLength | MaxLength | MinBodyMass | MaxBodyMass | MinWingspan | MaxWingspan |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :------------------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                         |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                         |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                         |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                         |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                         |        64 |        81 |        1930 |        3310 |         130 |         165 |

Sa pangkalahatan, maaari mong mabilisang tingnan kung paano nakapamahagi ang datos sa pamamagitan ng paggamit ng scatter plot tulad ng ginawa natin sa nakaraang aralin:

```r
ggplot(data=birds_filtered, aes(x=Order, y=MaxLength,group=1)) +
  geom_point() +
  ggtitle("Max Length per order") + coord_flip()
```
![max length per order](../../../../../translated_images/tl/max-length-per-order.e5b283d952c78c12b091307c5d3cf67132dad6fefe80a073353b9dc5c2bd3eb8.png)

Ipinapakita nito ang pangkalahatang pamamahagi ng haba ng katawan bawat Order ng ibon, ngunit hindi ito ang pinakamainam na paraan upang ipakita ang tunay na pamamahagi. Ang gawaing ito ay karaniwang ginagawa sa pamamagitan ng paglikha ng Histogram.

## Paggamit ng histograms

Nag-aalok ang `ggplot2` ng mahusay na paraan upang ipakita ang pamamahagi ng datos gamit ang Histograms. Ang ganitong uri ng tsart ay parang bar chart kung saan makikita ang pamamahagi sa pamamagitan ng pagtaas at pagbaba ng mga bar. Upang makabuo ng histogram, kailangan mo ng numeric na datos. Upang makabuo ng Histogram, maaari kang mag-plot ng tsart na tinutukoy ang uri bilang 'hist' para sa Histogram. Ang tsart na ito ay nagpapakita ng pamamahagi ng MaxBodyMass para sa buong saklaw ng numeric na datos sa dataset. Sa pamamagitan ng paghahati ng array ng datos sa mas maliliit na bins, maaari nitong ipakita ang pamamahagi ng mga halaga ng datos:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=10)+ylab('Frequency')
```
![distribution over entire dataset](../../../../../translated_images/tl/distribution-over-the-entire-dataset.d22afd3fa96be854e4c82213fedec9e3703cba753d07fad4606aadf58cf7e78e.png)

Makikita mo na karamihan sa 400+ na ibon sa dataset na ito ay nasa saklaw na mas mababa sa 2000 para sa kanilang Max Body Mass. Makakuha ng mas maraming insight sa datos sa pamamagitan ng pagbabago ng `bins` parameter sa mas mataas na numero, tulad ng 30:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + geom_histogram(bins=30)+ylab('Frequency')
```

![distribution-30bins](../../../../../translated_images/tl/distribution-30bins.6a3921ea7a421bf71f06bf5231009e43d1146f1b8da8dc254e99b5779a4983e5.png)

Ipinapakita ng tsart na ito ang pamamahagi sa mas detalyadong paraan. Ang isang tsart na hindi masyadong skewed sa kaliwa ay maaaring malikha sa pamamagitan ng pagtiyak na pipiliin mo lamang ang datos sa loob ng isang ibinigay na saklaw:

I-filter ang iyong datos upang makuha lamang ang mga ibon na ang body mass ay mas mababa sa 60, at ipakita ang 30 `bins`:

```r
birds_filtered_1 <- subset(birds_filtered, MaxBodyMass > 1 & MaxBodyMass < 60)
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=30)+ylab('Frequency')
```

![filtered histogram](../../../../../translated_images/tl/filtered-histogram.6bf5d2bfd82533220e1bd4bc4f7d14308f43746ed66721d9ec8f460732be6674.png)

✅ Subukan ang iba pang mga filter at puntos ng datos. Upang makita ang buong pamamahagi ng datos, alisin ang `['MaxBodyMass']` filter upang ipakita ang mga labeled distributions.

Nag-aalok ang histogram ng magagandang enhancement sa kulay at labeling na maaari mong subukan:

Gumawa ng 2D histogram upang ihambing ang relasyon sa pagitan ng dalawang pamamahagi. Ihambing natin ang `MaxBodyMass` vs. `MaxLength`. Nag-aalok ang `ggplot2` ng built-in na paraan upang ipakita ang convergence gamit ang mas maliwanag na kulay:

```r
ggplot(data=birds_filtered_1, aes(x=MaxBodyMass, y=MaxLength) ) +
  geom_bin2d() +scale_fill_continuous(type = "viridis")
```
Mukhang may inaasahang ugnayan sa pagitan ng dalawang elementong ito sa isang inaasahang axis, na may isang partikular na malakas na punto ng convergence:

![2d plot](../../../../../translated_images/tl/2d-plot.c504786f439bd7ebceebf2465c70ca3b124103e06c7ff7214bf24e26f7aec21e.png)

Ang histograms ay mahusay na gumagana bilang default para sa numeric na datos. Paano kung kailangan mong makita ang pamamahagi ayon sa text na datos?

## Tuklasin ang dataset para sa pamamahagi gamit ang text na datos 

Ang dataset na ito ay naglalaman din ng magagandang impormasyon tungkol sa kategorya ng ibon at ang genus, species, at pamilya nito pati na rin ang kalagayan ng konserbasyon nito. Tuklasin natin ang impormasyon ng konserbasyon na ito. Ano ang pamamahagi ng mga ibon ayon sa kanilang kalagayan ng konserbasyon?

> ✅ Sa dataset, ilang acronyms ang ginagamit upang ilarawan ang kalagayan ng konserbasyon. Ang mga acronyms na ito ay mula sa [IUCN Red List Categories](https://www.iucnredlist.org/), isang organisasyon na nagkatalogo ng kalagayan ng mga species.
> 
> - CR: Critically Endangered
> - EN: Endangered
> - EX: Extinct
> - LC: Least Concern
> - NT: Near Threatened
> - VU: Vulnerable

Ang mga ito ay text-based na halaga kaya kailangan mong gumawa ng transform upang makabuo ng histogram. Gamit ang filteredBirds dataframe, ipakita ang kalagayan ng konserbasyon nito kasabay ng Minimum Wingspan. Ano ang nakikita mo?

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

![wingspan and conservation collation](../../../../../translated_images/tl/wingspan-conservation-collation.4024e9aa6910866aa82f0c6cb6a6b4b925bd10079e6b0ef8f92eefa5a6792f76.png)

Mukhang walang magandang ugnayan sa pagitan ng minimum wingspan at kalagayan ng konserbasyon. Subukan ang iba pang mga elemento ng dataset gamit ang pamamaraang ito. Maaari kang mag-eksperimento sa iba't ibang filter. May nakikita ka bang ugnayan?

## Density plots

Maaaring napansin mo na ang mga histogram na tiningnan natin hanggang ngayon ay 'stepped' at hindi dumadaloy nang maayos sa isang arc. Upang ipakita ang mas maayos na density chart, maaari kang gumamit ng density plot.

Subukan natin ang density plot ngayon!

```r
ggplot(data = birds_filtered_1, aes(x = MinWingspan)) + 
  geom_density()
```
![density plot](../../../../../translated_images/tl/density-plot.675ccf865b76c690487fb7f69420a8444a3515f03bad5482886232d4330f5c85.png)

Makikita mo kung paano ginagaya ng plot ang naunang isa para sa Minimum Wingspan na datos; medyo mas maayos lang ito. Kung nais mong balikan ang jagged MaxBodyMass line sa pangalawang tsart na ginawa mo, maaari mo itong gawing mas maayos sa pamamagitan ng muling paggawa nito gamit ang pamamaraang ito:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density()
```
![bodymass density](../../../../../translated_images/tl/bodymass-smooth.d31ce526d82b0a1f19a073815dea28ecfbe58145ec5337e4ef7e8cdac81120b3.png)

Kung nais mo ng maayos, ngunit hindi masyadong maayos na linya, i-edit ang `adjust` parameter:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density(adjust = 1/5)
```
![less smooth bodymass](../../../../../translated_images/tl/less-smooth-bodymass.10f4db8b683cc17d17b2d33f22405413142004467a1493d416608dafecfdee23.png)

✅ Basahin ang tungkol sa mga parameter na magagamit para sa ganitong uri ng plot at mag-eksperimento!

Ang ganitong uri ng tsart ay nag-aalok ng magagandang paliwanag na visualizations. Sa ilang linya ng code, halimbawa, maaari mong ipakita ang max body mass density bawat Order ng ibon:

```r
ggplot(data=birds_filtered_1,aes(x = MaxBodyMass, fill = Order)) +
  geom_density(alpha=0.5)
```
![bodymass per order](../../../../../translated_images/tl/bodymass-per-order.9d2b065dd931b928c839d8cdbee63067ab1ae52218a1b90717f4bc744354f485.png)

## 🚀 Hamon

Ang histograms ay mas sopistikadong uri ng tsart kaysa sa mga basic scatterplots, bar charts, o line charts. Maghanap sa internet ng magagandang halimbawa ng paggamit ng histograms. Paano sila ginagamit, ano ang kanilang ipinapakita, at sa anong mga larangan o lugar ng pag-aaral sila karaniwang ginagamit?

## [Post-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## Review & Self Study

Sa araling ito, ginamit mo ang `ggplot2` at nagsimulang magpakita ng mas sopistikadong mga tsart. Mag-research tungkol sa `geom_density_2d()` isang "continuous probability density curve in one or more dimensions". Basahin ang [documentation](https://ggplot2.tidyverse.org/reference/geom_density_2d.html) upang maunawaan kung paano ito gumagana.

## Takdang Aralin

[Ilapat ang iyong mga kasanayan](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.