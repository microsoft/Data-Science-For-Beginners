<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-26T23:08:16+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "fi"
}
-->
# Määrien visualisointi
|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Määrien visualisointi - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Tässä oppitunnissa tutustut siihen, miten voit käyttää joitakin R:n saatavilla olevia kirjastoja luodaksesi kiinnostavia visualisointeja, jotka liittyvät määrien käsitteeseen. Käyttämällä puhdistettua datasettiä Minnesotan linnuista voit oppia monia mielenkiintoisia asioita paikallisesta eläimistöstä.  
## [Esiluennon kysely](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## Tarkastele siipiväliä ggplot2:n avulla
Erinomainen kirjasto erilaisten yksinkertaisten ja monimutkaisten kaavioiden ja diagrammien luomiseen on [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html). Yleisesti ottaen datan visualisointi näiden kirjastojen avulla sisältää seuraavat vaiheet: määritä, mitä osia dataframesta haluat käyttää, tee tarvittavat muunnokset datalle, määritä x- ja y-akselin arvot, päätä kaaviotyyppi ja näytä kaavio.

`ggplot2` on järjestelmä, joka luo grafiikkaa deklaratiivisesti perustuen "The Grammar of Graphics" -menetelmään. [Grammar of Graphics](https://en.wikipedia.org/wiki/Ggplot2) on yleinen kaavioiden visualisointimenetelmä, joka jakaa kaaviot semanttisiin osiin, kuten skaaloihin ja kerroksiin. Toisin sanoen, `ggplot2` tekee yksinkertaisten ja monimutkaisten kaavioiden luomisesta univariantille tai multivariantille datalle helppoa vähäisellä koodilla, mikä tekee siitä suosituimman visualisointikirjaston R:ssä. Käyttäjä määrittää, miten muuttujat kartoitetaan visuaalisiin ominaisuuksiin, mitä graafisia elementtejä käytetään, ja `ggplot2` hoitaa loput.

> ✅ Kaavio = Data + Esteettisyys + Geometria
> - Data viittaa datasettiin
> - Esteettisyys tarkoittaa tutkittavia muuttujia (x- ja y-muuttujat)
> - Geometria viittaa kaaviotyyppiin (viivakaavio, pylväsdiagrammi jne.)

Valitse paras geometria (kaaviotyyppi) datasi ja tarinan mukaan, jonka haluat kertoa kaavion avulla.

> - Trendien analysointi: viiva, pylväs
> - Arvojen vertailu: pylväs, palkki, piirakka, hajontakaavio
> - Osien suhde kokonaisuuteen: piirakka
> - Datan jakauman näyttäminen: hajontakaavio, palkki
> - Arvojen välisten suhteiden näyttäminen: viiva, hajontakaavio, kupla

✅ Voit myös tutustua tähän kuvaavaan [cheatsheetiin](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf) ggplot2:lle.

## Luo viivakaavio lintujen siipiväliarvoista

Avaa R-konsoli ja tuo datasetti.  
> Huom: Datasetti on tallennettu tämän repositorion juureen `/data`-kansioon.

Tuodaan datasetti ja tarkastellaan datan alkua (ensimmäiset 5 riviä).

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```  
Datan alku sisältää sekoituksen tekstiä ja numeroita:

|      | Nimi                         | Tieteellinen nimi      | Kategoria             | Lahko        | Heimo    | Suku        | Suojelustatus       | MinPituus | MaxPituus | MinPaino    | MaxPaino    | MinSiipiväli | MaxSiipiväli |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Mustavatsainen viheltävä ankka | Dendrocygna autumnalis | Ankat/hanhet/vesilinnut | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Ruostoviheltävä ankka         | Dendrocygna bicolor    | Ankat/hanhet/vesilinnut | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Lumihanhi                     | Anser caerulescens     | Ankat/hanhet/vesilinnut | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Rossin hanhi                  | Anser rossii           | Ankat/hanhet/vesilinnut | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Iso valkoposkihanhi           | Anser albifrons        | Ankat/hanhet/vesilinnut | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Aloitetaan piirtämällä osa numeerisesta datasta perusviivakaavion avulla. Oletetaan, että haluat tarkastella näiden mielenkiintoisten lintujen maksimaalista siipiväliä.

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```  
Tässä asennetaan `ggplot2`-kirjasto ja tuodaan se työtilaan komennolla `library("ggplot2")`. Kaavion piirtämiseen ggplotissa käytetään `ggplot()`-funktiota, jossa määritetään datasetti, x- ja y-muuttujat attribuuteiksi. Tässä tapauksessa käytetään `geom_line()`-funktiota, koska tavoitteena on piirtää viivakaavio.

![MaxWingspan-lineplot](../../../../../translated_images/fi/MaxWingspan-lineplot.b12169f99d26fdd263f291008dfd73c18a4ba8f3d32b1fda3d74af51a0a28616.png)

Mitä huomaat heti? Näyttää olevan ainakin yksi poikkeama - melko vaikuttava siipiväli! Yli 2000 senttimetrin siipiväli vastaa yli 20 metriä - onko Minnesotassa lentäviä pterosauruksia? Tutkitaan asiaa.

Vaikka voisit tehdä nopean lajittelun Excelissä löytääksesi nämä poikkeamat, jotka ovat todennäköisesti kirjoitusvirheitä, jatka visualisointiprosessia työskentelemällä suoraan kaaviosta.

Lisää x-akselille selitteet, jotka näyttävät, minkä tyyppisistä linnuista on kyse:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```  
Määritämme kulman `theme`-osiossa ja määritämme x- ja y-akselin selitteet `xlab()`- ja `ylab()`-funktioilla. `ggtitle()` antaa kaaviolle nimen.

![MaxWingspan-lineplot-improved](../../../../../translated_images/fi/MaxWingspan-lineplot-improved.04b73b4d5a59552a6bc7590678899718e1f065abe9eada9ebb4148939b622fd4.png)

Vaikka selitteiden kiertokulma on asetettu 45 asteeseen, niitä on silti liikaa luettavaksi. Kokeillaan toista strategiaa: merkitään vain poikkeamat ja asetetaan selitteet kaavion sisälle. Voit käyttää hajontakaaviota, jotta selitteille jää enemmän tilaa:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```  
Mitä tässä tapahtuu? Käytit `geom_point()`-funktiota hajontapisteiden piirtämiseen. Tämän avulla lisäsit selitteet linnuille, joiden `MaxWingspan > 500`, ja piilotit x-akselin selitteet kaavion selkeyttämiseksi.

Mitä huomaat?

![MaxWingspan-scatterplot](../../../../../translated_images/fi/MaxWingspan-scatterplot.60dc9e0e19d32700283558f253841fdab5104abb62bc96f7d97f9c0ee857fa8b.png)

## Suodata dataasi

Sekä valkopäämerikotka että preeriakotka, vaikka ovatkin todennäköisesti suuria lintuja, näyttävät olevan virheellisesti merkittyjä, ja niiden maksimaaliseen siipiväliin on lisätty ylimääräinen nolla. On epätodennäköistä, että kohtaat valkopäämerikotkan, jonka siipiväli on 25 metriä, mutta jos näin käy, kerro meille! Luodaan uusi dataframe ilman näitä kahta poikkeamaa:

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
Loimme uuden dataframen `birds_filtered` ja piirsimme hajontakaavion. Suodattamalla poikkeamat datasi on nyt yhtenäisempää ja ymmärrettävämpää.

![MaxWingspan-scatterplot-improved](../../../../../translated_images/fi/MaxWingspan-scatterplot-improved.7d0af81658c65f3e75b8fedeb2335399e31108257e48db15d875ece608272051.png)

Nyt kun meillä on puhtaampi datasetti ainakin siipivälin osalta, tutkitaan lisää näitä lintuja.

Vaikka viiva- ja hajontakaaviot voivat näyttää tietoa datan arvoista ja niiden jakaumista, haluamme pohtia datasetin sisältämiä arvoja. Voisit luoda visualisointeja vastataksesi seuraaviin kysymyksiin määristä:

> Kuinka monta lintukategoriaa on olemassa, ja mikä on niiden lukumäärä?  
> Kuinka monta lintua on sukupuuttoon kuolleita, uhanalaisia, harvinaisia tai yleisiä?  
> Kuinka monta eri sukua ja lahkoa on Linnaeuksen terminologian mukaan?  
## Tutki pylväsdiagrammeja

Pylväsdiagrammit ovat käytännöllisiä, kun haluat näyttää datan ryhmittelyjä. Tutkitaan datasetin lintukategorioita ja katsotaan, mikä on yleisin lukumäärän perusteella.  
Luodaan pylväsdiagrammi suodatetusta datasta.

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
Seuraavassa koodissa asennetaan [dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8)- ja [lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0)-kirjastot, jotka auttavat datan käsittelyssä ja ryhmittelyssä pinotun pylväsdiagrammin piirtämiseksi. Ensin ryhmitellään data lintujen `Category`-sarakkeen mukaan ja tiivistetään sarakkeet `MinLength`, `MaxLength`, `MinBodyMass`, `MaxBodyMass`, `MinWingspan`, `MaxWingspan`. Sitten piirretään pylväsdiagrammi `ggplot2`-kirjaston avulla ja määritetään eri kategorioiden värit ja selitteet.

![Stacked bar chart](../../../../../translated_images/fi/stacked-bar-chart.0c92264e89da7b391a7490224d1e7059a020e8b74dcd354414aeac78871c02f1.png)

Tämä pylväsdiagrammi on kuitenkin vaikeasti luettavissa, koska siinä on liikaa ryhmittelemätöntä dataa. Sinun täytyy valita vain data, jonka haluat piirtää, joten tarkastellaan lintujen pituutta kategorian perusteella.

Suodata dataasi sisältämään vain lintujen kategoriat.

Koska kategorioita on paljon, voit näyttää tämän kaavion pystysuunnassa ja säätää sen korkeutta, jotta kaikki data mahtuu mukaan:

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```  
Ensin lasketaan `Category`-sarakkeen uniikit arvot ja lajitellaan ne uuteen dataframeen `birds_count`. Tämä lajiteltu data järjestetään samalle tasolle, jotta se piirretään järjestyksessä. Käyttämällä `ggplot2`-kirjastoa piirretään data pylväsdiagrammiin. `coord_flip()` piirtää vaakapalkit.

![category-length](../../../../../translated_images/fi/category-length.7e34c296690e85d64f7e4d25a56077442683eca96c4f5b4eae120a64c0755636.png)

Tämä pylväsdiagrammi näyttää hyvän näkymän lintujen lukumäärästä kussakin kategoriassa. Silmänräpäyksessä näet, että suurin osa tämän alueen linnuista kuuluu Ankat/hanhet/vesilinnut-kategoriaan. Minnesota on "10 000 järven maa", joten tämä ei ole yllättävää!

✅ Kokeile joitakin muita laskentoja tästä datasetistä. Yllättääkö jokin sinut?

## Datan vertailu

Voit kokeilla eri ryhmitellyn datan vertailuja luomalla uusia akseleita. Kokeile vertailua lintujen maksimaalisen pituuden perusteella kategorian mukaan:

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
Ryhmämme `birds_filtered`-datan `Category`-sarakkeen mukaan ja piirrämme pylväsdiagrammin.

![comparing data](../../../../../translated_images/fi/comparingdata.f486a450d61c7ca5416f27f3f55a6a4465d00df3be5e6d33936e9b07b95e2fdd.png)

Tässä ei ole mitään yllättävää: kolibrit ovat pienimpiä maksimaalisen pituuden osalta verrattuna pelikaaniin tai hanhiin. On hyvä, kun data on loogista!

Voit luoda mielenkiintoisempia pylväsdiagrammeja päällekkäistämällä dataa. Päällekkäistetään minimipituus ja maksimipituus tiettyyn lintukategoriaan:

```r
ggplot(data=birds_grouped, aes(x=Category)) +
  geom_bar(aes(y=MaxLength), stat="identity", position ="identity",  fill='blue') +
  geom_bar(aes(y=MinLength), stat="identity", position="identity", fill='orange')+
  coord_flip()
```  
![super-imposed values](../../../../../translated_images/fi/superimposed-values.5363f0705a1da4167625a373a1064331ea3cb7a06a297297d0734fcc9b3819a0.png)

## 🚀 Haaste

Tämä lintudatasetti tarjoaa runsaasti tietoa eri lintutyypeistä tietyssä ekosysteemissä. Etsi internetistä muita lintuihin liittyviä datasettiä. Harjoittele kaavioiden ja diagrammien luomista näistä linnuista löytääksesi faktoja, joita et tiennyt.  
## [Luennon jälkeinen kysely](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## Kertaus ja itseopiskelu

Tämä ensimmäinen oppitunti on antanut sinulle tietoa siitä, miten käyttää `ggplot2`:ta määrien visualisointiin. Tutki muita tapoja työskennellä datasetin kanssa visualisointia varten. Etsi ja tutki datasettiä, joita voisit visualisoida muilla kirjastoilla, kuten [Lattice](https://stat.ethz.ch/R-manual/R-devel/library/lattice/html/Lattice.html) ja [Plotly](https://github.com/plotly/plotly.R#readme).

## Tehtävä  
[Viivat, hajonnat ja palkit](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.