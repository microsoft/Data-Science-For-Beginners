<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-30T18:43:44+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "sl"
}
-->
# Vizualizacija količin
|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Vizualizacija količin - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

V tej lekciji boste raziskali, kako uporabiti nekatere izmed številnih knjižnic paketov v R-ju za ustvarjanje zanimivih vizualizacij, ki se osredotočajo na koncept količine. Z uporabo očiščenega nabora podatkov o pticah iz Minnesote lahko odkrijete številna zanimiva dejstva o lokalni divjini.  
## [Predlekcijski kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## Opazovanje razpona kril z ggplot2
Odlična knjižnica za ustvarjanje tako preprostih kot sofisticiranih grafov in diagramov različnih vrst je [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html). Na splošno proces risanja podatkov s temi knjižnicami vključuje identifikacijo delov vašega podatkovnega okvira, ki jih želite obdelati, izvedbo potrebnih transformacij podatkov, dodelitev vrednosti za osi x in y, odločitev o vrsti grafa ter prikaz grafa.

`ggplot2` je sistem za deklarativno ustvarjanje grafike, ki temelji na "The Grammar of Graphics". [Grammar of Graphics](https://en.wikipedia.org/wiki/Ggplot2) je splošna shema za vizualizacijo podatkov, ki razdeli grafe na semantične komponente, kot so lestvice in sloji. Z drugimi besedami, enostavnost ustvarjanja grafov za enovariatne ali večvariatne podatke z malo kode naredi `ggplot2` najbolj priljubljen paket za vizualizacije v R-ju. Uporabnik pove `ggplot2`, kako preslikati spremenljivke na estetiko, katere grafične primitivne elemente uporabiti, nato pa `ggplot2` poskrbi za ostalo.

> ✅ Graf = Podatki + Estetika + Geometrija  
> - Podatki se nanašajo na nabor podatkov  
> - Estetika označuje spremenljivke, ki jih preučujemo (spremenljivki x in y)  
> - Geometrija se nanaša na vrsto grafa (črtni graf, stolpični graf itd.)  

Izberite najboljšo geometrijo (vrsto grafa) glede na vaše podatke in zgodbo, ki jo želite povedati skozi graf.  

> - Za analizo trendov: črta, stolpec  
> - Za primerjavo vrednosti: stolpec, tortni diagram, razsevni diagram  
> - Za prikaz, kako deli sestavljajo celoto: tortni diagram  
> - Za prikaz porazdelitve podatkov: razsevni diagram, stolpec  
> - Za prikaz odnosov med vrednostmi: črta, razsevni diagram, mehurčasti diagram  

✅ Oglejte si tudi ta opisni [priročnik](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf) za ggplot2.

## Ustvarite črtni graf za vrednosti razpona kril ptic

Odprite konzolo R in uvozite nabor podatkov.  
> Opomba: Nabor podatkov je shranjen v korenu tega repozitorija v mapi `/data`.

Uvozimo nabor podatkov in si ogledamo glavo (prvih 5 vrstic) podatkov.

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```  
Glava podatkov vsebuje mešanico besedila in številk:

|      | Ime                          | ZnanstvenoIme          | Kategorija            | Red          | Družina  | Rod         | StatusOhranjanja   | MinDolžina | MaxDolžina | MinTelesnaMasa | MaxTelesnaMasa | MinRazponKril | MaxRazponKril |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Črno-trebušna piščalka       | Dendrocygna autumnalis | Race/Gosi/Vodna ptica | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Rjava piščalka               | Dendrocygna bicolor    | Race/Gosi/Vodna ptica | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snežna gos                   | Anser caerulescens     | Race/Gosi/Vodna ptica | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Rossova gos                  | Anser rossii           | Race/Gosi/Vodna ptica | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Velika bela-frontna gos      | Anser albifrons        | Race/Gosi/Vodna ptica | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Začnimo z risanjem nekaterih numeričnih podatkov z osnovnim črtnim grafom. Recimo, da želite pogled na največji razpon kril teh zanimivih ptic.

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```  
Tukaj namestite paket `ggplot2` in ga nato uvozite v delovni prostor z ukazom `library("ggplot2")`. Za risanje grafa v ggplot se uporablja funkcija `ggplot()`, kjer določite nabor podatkov ter spremenljivki x in y kot atribute. V tem primeru uporabimo funkcijo `geom_line()`, saj želimo narisati črtni graf.

![MaxWingspan-lineplot](../../../../../translated_images/sl/MaxWingspan-lineplot.b12169f99d26fdd263f291008dfd73c18a4ba8f3d32b1fda3d74af51a0a28616.png)

Kaj takoj opazite? Zdi se, da obstaja vsaj en odstopajoč podatek - to je kar razpon kril! Razpon kril več kot 2000 centimetrov pomeni več kot 20 metrov - ali v Minnesoti živijo pterodaktili? Raziščimo.

Čeprav bi lahko hitro razvrstili podatke v Excelu, da bi našli te odstopajoče podatke, ki so verjetno tipkarske napake, nadaljujte proces vizualizacije z delom znotraj grafa.

Dodajte oznake na os x, da pokažete, za katere ptice gre:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```  
Kot oznak določimo v `theme` in določimo oznake osi x in y v `xlab()` in `ylab()`. Funkcija `ggtitle()` doda ime grafu.

![MaxWingspan-lineplot-improved](../../../../../translated_images/sl/MaxWingspan-lineplot-improved.04b73b4d5a59552a6bc7590678899718e1f065abe9eada9ebb4148939b622fd4.png)

Tudi z rotacijo oznak na 45 stopinj je preveč podatkov za branje. Poskusimo drugačno strategijo: označimo samo odstopajoče podatke in postavimo oznake znotraj grafa. Uporabite razsevni diagram, da ustvarite več prostora za označevanje:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```  
Kaj se tukaj dogaja? Uporabili ste funkcijo `geom_point()` za risanje razsevnih točk. S tem ste dodali oznake za ptice, katerih `MaxWingspan > 500`, in tudi skrili oznake na osi x, da zmanjšate natrpanost grafa.  

Kaj odkrijete?

![MaxWingspan-scatterplot](../../../../../translated_images/sl/MaxWingspan-scatterplot.60dc9e0e19d32700283558f253841fdab5104abb62bc96f7d97f9c0ee857fa8b.png)

## Filtrirajte svoje podatke

Tako plešasti orel kot prerijski sokol, čeprav sta verjetno zelo veliki ptici, sta očitno napačno označena, z dodatno ničlo pri največjem razponu kril. Malo verjetno je, da boste srečali plešastega orla z razponom kril 25 metrov, vendar če ga, nam prosim sporočite! Ustvarimo nov podatkovni okvir brez teh dveh odstopajočih podatkov:

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
Ustvarili smo nov podatkovni okvir `birds_filtered` in nato narisali razsevni diagram. Z odstranitvijo odstopajočih podatkov so vaši podatki zdaj bolj skladni in razumljivi.

![MaxWingspan-scatterplot-improved](../../../../../translated_images/sl/MaxWingspan-scatterplot-improved.7d0af81658c65f3e75b8fedeb2335399e31108257e48db15d875ece608272051.png)

Zdaj, ko imamo vsaj očiščen nabor podatkov glede razpona kril, odkrijmo več o teh pticah.

Čeprav črtni in razsevni diagrami lahko prikazujejo informacije o vrednostih podatkov in njihovih porazdelitvah, želimo razmisliti o vrednostih, ki so inherentne v tem naboru podatkov. Lahko ustvarite vizualizacije za odgovore na naslednja vprašanja o količinah:

> Koliko kategorij ptic obstaja in kakšno je njihovo število?  
> Koliko ptic je izumrlih, ogroženih, redkih ali pogostih?  
> Koliko jih je v različnih rodovih in redih po Linnaeusovi terminologiji?  
## Raziskovanje stolpičnih grafov

Stolpični grafi so praktični, ko morate prikazati skupine podatkov. Raziskujmo kategorije ptic, ki obstajajo v tem naboru podatkov, da vidimo, katera je najpogostejša po številu.  
Ustvarimo stolpični graf na filtriranih podatkih.

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
V naslednjem odlomku namestimo paketa [dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8) in [lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0), da pomagata pri manipulaciji in grupiranju podatkov za risanje zloženega stolpičnega grafa. Najprej grupirate podatke po `Category` ptic in nato povzamete stolpce `MinLength`, `MaxLength`, `MinBodyMass`, `MaxBodyMass`, `MinWingspan`, `MaxWingspan`. Nato narišete stolpični graf z uporabo paketa `ggplot2` in določite barve za različne kategorije ter oznake.  

![Stacked bar chart](../../../../../translated_images/sl/stacked-bar-chart.0c92264e89da7b391a7490224d1e7059a020e8b74dcd354414aeac78871c02f1.png)

Ta stolpični graf je neberljiv, ker je preveč nepovezanih podatkov. Izbrati morate samo podatke, ki jih želite prikazati, zato si oglejmo dolžino ptic glede na njihovo kategorijo.

Filtrirajte svoje podatke, da vključite samo kategorijo ptic.

Ker je kategorij veliko, lahko ta graf prikažete vertikalno in prilagodite njegovo višino, da upoštevate vse podatke:

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```  
Najprej preštejete unikatne vrednosti v stolpcu `Category` in jih nato razvrstite v nov podatkovni okvir `birds_count`. Te razvrščene podatke nato razvrstite na isti ravni, da so narisani v razvrščenem vrstnem redu. Z uporabo `ggplot2` nato narišete podatke v stolpičnem grafu. Funkcija `coord_flip()` nariše horizontalne stolpce.  

![category-length](../../../../../translated_images/sl/category-length.7e34c296690e85d64f7e4d25a56077442683eca96c4f5b4eae120a64c0755636.png)

Ta stolpični graf prikazuje dober pogled na število ptic v vsaki kategoriji. Na prvi pogled vidite, da je največ ptic v tej regiji v kategoriji Race/Gosi/Vodna ptica. Minnesota je 'dežela 10.000 jezer', zato to ni presenetljivo!

✅ Poskusite nekaj drugih štetij na tem naboru podatkov. Vas kaj preseneti?

## Primerjava podatkov

Poskusite različne primerjave grupiranih podatkov z ustvarjanjem novih osi. Poskusite primerjavo največje dolžine ptice glede na njeno kategorijo:

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
Grupiramo podatke `birds_filtered` po `Category` in nato narišemo stolpični graf.  

![comparing data](../../../../../translated_images/sl/comparingdata.f486a450d61c7ca5416f27f3f55a6a4465d00df3be5e6d33936e9b07b95e2fdd.png)

Tukaj ni nič presenetljivega: kolibriji imajo najmanjšo največjo dolžino v primerjavi s pelikani ali gosmi. Dobro je, ko podatki logično ustrezajo!

Lahko ustvarite bolj zanimive vizualizacije stolpičnih grafov z nadgrajevanjem podatkov. Nadgradimo minimalno in maksimalno dolžino na določeno kategorijo ptic:

```r
ggplot(data=birds_grouped, aes(x=Category)) +
  geom_bar(aes(y=MaxLength), stat="identity", position ="identity",  fill='blue') +
  geom_bar(aes(y=MinLength), stat="identity", position="identity", fill='orange')+
  coord_flip()
```  
![super-imposed values](../../../../../translated_images/sl/superimposed-values.5363f0705a1da4167625a373a1064331ea3cb7a06a297297d0734fcc9b3819a0.png)

## 🚀 Izziv

Ta nabor podatkov o pticah ponuja bogastvo informacij o različnih vrstah ptic znotraj določenega ekosistema. Poiščite po internetu in preverite, ali lahko najdete druge nabore podatkov o pticah. Vadite risanje grafov in diagramov o teh pticah, da odkrijete dejstva, ki jih niste poznali.  
## [Po-lekcijski kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## Pregled in samostojno učenje

Ta prva lekcija vam je dala nekaj informacij o tem, kako uporabiti `ggplot2` za vizualizacijo količin. Raziskujte druge načine dela z nabori podatkov za vizualizacijo. Raziskujte in poiščite nabore podatkov, ki jih lahko vizualizirate z drugimi paketi, kot sta [Lattice](https://stat.ethz.ch/R-manual/R-devel/library/lattice/html/Lattice.html) in [Plotly](https://github.com/plotly/plotly.R#readme).

## Naloga  
[Črte, razsevni diagrami in stolpci](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.