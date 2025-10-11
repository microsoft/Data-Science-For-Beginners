<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea67c0c40808fd723594de6896c37ccf",
  "translation_date": "2025-10-11T15:57:48+00:00",
  "source_file": "3-Data-Visualization/R/10-visualization-distributions/README.md",
  "language_code": "et"
}
-->
# Andmete jaotuse visualiseerimine

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Andmete jaotuse visualiseerimine - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Eelmises tunnis õppisite huvitavaid fakte Minnesota lindude andmestiku kohta. Leidsite vigaseid andmeid, visualiseerides kõrvalekaldeid, ja uurisite erinevusi lindude kategooriate vahel nende maksimaalse pikkuse järgi.

## [Eelloengu viktoriin](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## Uurime lindude andmestikku

Üks viis andmete sügavamaks uurimiseks on vaadata nende jaotust ehk seda, kuidas andmed on telje ulatuses organiseeritud. Näiteks võiksite teada saada, kuidas on jaotunud Minnesota lindude maksimaalne tiivaulatus või maksimaalne kehamass.

Avastame mõned faktid selle andmestiku jaotuste kohta. Oma R konsoolis importige `ggplot2` ja andmebaas. Eemaldage andmebaasist kõrvalekalded, nagu tegite eelmises teemas.

```r
library(ggplot2)

birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")

birds_filtered <- subset(birds, MaxWingspan < 500)
head(birds_filtered)
```
|      | Nimi                         | Teaduslik nimi         | Kategooria            | Selts        | Sugukond | Perekond    | Kaitsestaatus       | MinPikkus | MaxPikkus | MinKehamass | MaxKehamass | MinTiivaulatus | MaxTiivaulatus |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Mustkõht-vilepart            | Dendrocygna autumnalis | Pardid/Haned/Vesilinnud | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Kollakas-vilepart            | Dendrocygna bicolor    | Pardid/Haned/Vesilinnud | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Lumehani                     | Anser caerulescens     | Pardid/Haned/Vesilinnud | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Rossi hani                   | Anser rossii           | Pardid/Haned/Vesilinnud | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Suur-valgehan                | Anser albifrons        | Pardid/Haned/Vesilinnud | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Üldiselt saate andmete jaotust kiiresti vaadata hajuvusdiagrammi abil, nagu tegime eelmises tunnis:

```r
ggplot(data=birds_filtered, aes(x=Order, y=MaxLength,group=1)) +
  geom_point() +
  ggtitle("Max Length per order") + coord_flip()
```
![maksimaalne pikkus seltsi järgi](../../../../../translated_images/max-length-per-order.e5b283d952c78c12b091307c5d3cf67132dad6fefe80a073353b9dc5c2bd3eb8.et.png)

See annab ülevaate lindude pikkuse jaotusest seltsi järgi, kuid see pole parim viis tõeliste jaotuste kuvamiseks. Selle ülesande jaoks kasutatakse tavaliselt histogrammi.
## Töötamine histogrammidega

`ggplot2` pakub väga häid viise andmete jaotuse visualiseerimiseks histogrammide abil. See diagrammitüüp sarnaneb tulpdiagrammiga, kus jaotust saab näha tulpade tõusu ja languse kaudu. Histogrammi loomiseks on vaja numbrilisi andmeid. Histogrammi loomiseks saate määrata diagrammi tüübi 'hist' histogrammi jaoks. See diagramm näitab MaxBodyMass jaotust kogu andmestiku numbriliste andmete ulatuses. Jagades andmete massiivi väiksemateks osadeks, saab kuvada andmete väärtuste jaotust:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=10)+ylab('Frequency')
```
![jaotus kogu andmestikus](../../../../../translated_images/distribution-over-the-entire-dataset.d22afd3fa96be854e4c82213fedec9e3703cba753d07fad4606aadf58cf7e78e.et.png)

Nagu näete, kuulub enamik 400+ linnust selles andmestikus Max Body Mass väärtusega alla 2000. Saate andmetest rohkem aru, kui muudate `bins` parameetri kõrgemaks, näiteks 30:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + geom_histogram(bins=30)+ylab('Frequency')
```

![jaotus-30bins](../../../../../translated_images/distribution-30bins.6a3921ea7a421bf71f06bf5231009e43d1146f1b8da8dc254e99b5779a4983e5.et.png)

See diagramm näitab jaotust veidi detailsemalt. Vähem vasakule kaldu diagrammi saab luua, kui valite andmed ainult teatud vahemikus:

Filtreerige oma andmed, et saada ainult need linnud, kelle kehamass on alla 60, ja kuvage 30 `bins`:

```r
birds_filtered_1 <- subset(birds_filtered, MaxBodyMass > 1 & MaxBodyMass < 60)
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=30)+ylab('Frequency')
```

![filtreeritud histogramm](../../../../../translated_images/filtered-histogram.6bf5d2bfd82533220e1bd4bc4f7d14308f43746ed66721d9ec8f460732be6674.et.png)

✅ Proovige mõnda muud filtrit ja andmepunkti. Andmete täieliku jaotuse nägemiseks eemaldage `['MaxBodyMass']` filter, et kuvada märgistatud jaotused.

Histogramm pakub ka mõningaid toredaid värvi- ja märgistuse täiustusi, mida proovida:

Looge 2D histogramm, et võrrelda kahe jaotuse vahelist seost. Võrdleme `MaxBodyMass` ja `MaxLength`. `ggplot2` pakub sisseehitatud viisi kokkulangevuse kuvamiseks heledamate värvide abil:

```r
ggplot(data=birds_filtered_1, aes(x=MaxBodyMass, y=MaxLength) ) +
  geom_bin2d() +scale_fill_continuous(type = "viridis")
```
Tundub, et nende kahe elemendi vahel on oodatud korrelatsioon mööda oodatud telge, kus üks kokkulangevuse punkt on eriti tugev:

![2d diagramm](../../../../../translated_images/2d-plot.c504786f439bd7ebceebf2465c70ca3b124103e06c7ff7214bf24e26f7aec21e.et.png)

Histogrammid töötavad vaikimisi hästi numbriliste andmetega. Aga mis siis, kui peate nägema jaotusi tekstiliste andmete järgi? 
## Uurime andmestikku jaotuste leidmiseks tekstiliste andmete abil 

See andmestik sisaldab ka head teavet lindude kategooria, perekonna, liigi ja sugukonna kohta ning nende kaitsestaatuse kohta. Uurime seda kaitsestaatuse teavet. Milline on lindude jaotus nende kaitsestaatuse järgi?

> ✅ Andmestikus kasutatakse mitmeid lühendeid kaitsestaatuse kirjeldamiseks. Need lühendid pärinevad [IUCN Red List Categories](https://www.iucnredlist.org/) organisatsioonilt, mis kataloogib liikide staatust.
> 
> - CR: Kriitiliselt ohustatud
> - EN: Ohustatud
> - EX: Väljasurnud
> - LC: Vähem muret tekitav
> - NT: Ohulähedane
> - VU: Haavatav

Need on tekstipõhised väärtused, seega peate histogrammi loomiseks tegema teisenduse. Kasutades filtritudBirds andmeraami, kuvage selle kaitsestaatus koos minimaalse tiivaulatusega. Mida te näete? 

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

![tiivaulatus ja kaitsestaatuse seos](../../../../../translated_images/wingspan-conservation-collation.4024e9aa6910866aa82f0c6cb6a6b4b925bd10079e6b0ef8f92eefa5a6792f76.et.png)

Tundub, et minimaalse tiivaulatuse ja kaitsestaatuse vahel pole head korrelatsiooni. Testige selle meetodiga andmestiku teisi elemente. Võite proovida ka erinevaid filtreid. Kas leiate korrelatsiooni?

## Tiheduse diagrammid

Võib-olla olete märganud, et seni vaadatud histogrammid on "astmelised" ega voola sujuvalt kaares. Sujuvama tiheduse diagrammi kuvamiseks võite proovida tiheduse diagrammi.

Töötame nüüd tiheduse diagrammidega!

```r
ggplot(data = birds_filtered_1, aes(x = MinWingspan)) + 
  geom_density()
```
![tiheduse diagramm](../../../../../translated_images/density-plot.675ccf865b76c690487fb7f69420a8444a3515f03bad5482886232d4330f5c85.et.png)

Näete, kuidas diagramm kajastab varasemat minimaalse tiivaulatuse diagrammi; see on lihtsalt veidi sujuvam. Kui soovite uuesti vaadata seda sakilist MaxBodyMass joont teises loodud diagrammis, saate selle väga hästi siluda, luues selle uuesti selle meetodiga:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density()
```
![kehamassi tihedus](../../../../../translated_images/bodymass-smooth.d31ce526d82b0a1f19a073815dea28ecfbe58145ec5337e4ef7e8cdac81120b3.et.png)

Kui soovite sujuvat, kuid mitte liiga sujuvat joont, muutke `adjust` parameetrit: 

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density(adjust = 1/5)
```
![vähem sujuv kehamass](../../../../../translated_images/less-smooth-bodymass.10f4db8b683cc17d17b2d33f22405413142004467a1493d416608dafecfdee23.et.png)

✅ Lugege selle diagrammitüübi jaoks saadaolevate parameetrite kohta ja katsetage!

See diagrammitüüp pakub kaunilt selgitavaid visualiseeringuid. Näiteks mõne koodirea abil saate näidata maksimaalse kehamassi tihedust lindude seltsi järgi:

```r
ggplot(data=birds_filtered_1,aes(x = MaxBodyMass, fill = Order)) +
  geom_density(alpha=0.5)
```
![kehamass seltsi järgi](../../../../../translated_images/bodymass-per-order.9d2b065dd931b928c839d8cdbee63067ab1ae52218a1b90717f4bc744354f485.et.png)

## 🚀 Väljakutse

Histogrammid on keerukamad diagrammitüübid kui lihtsad hajuvusdiagrammid, tulpdiagrammid või joondiagrammid. Otsige internetist häid näiteid histogrammide kasutamise kohta. Kuidas neid kasutatakse, mida need näitavad ja millistes valdkondades või uurimisvaldkondades neid tavaliselt kasutatakse?

## [Järelloengu viktoriin](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## Ülevaade ja iseseisev õppimine

Selles tunnis kasutasite `ggplot2` ja hakkasite looma keerukamaid diagramme. Tehke uurimistööd `geom_density_2d()` kohta, mis on "pidev tõenäosuse tiheduse kõver ühes või mitmes dimensioonis". Lugege [dokumentatsiooni](https://ggplot2.tidyverse.org/reference/geom_density_2d.html), et mõista, kuidas see töötab.

## Ülesanne

[Rakendage oma oskusi](assignment.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.