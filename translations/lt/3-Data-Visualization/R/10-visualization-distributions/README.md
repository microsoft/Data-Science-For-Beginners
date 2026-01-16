<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea67c0c40808fd723594de6896c37ccf",
  "translation_date": "2025-08-31T05:49:49+00:00",
  "source_file": "3-Data-Visualization/R/10-visualization-distributions/README.md",
  "language_code": "lt"
}
-->
# Vizualizuojant pasiskirstymus

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Vizualizuojant pasiskirstymus - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Ankstesnėje pamokoje sužinojote įdomių faktų apie Minesotos paukščių duomenų rinkinį. Aptikote klaidingus duomenis vizualizuodami išskirtis ir išnagrinėjote skirtumus tarp paukščių kategorijų pagal jų maksimalų ilgį.

## [Prieš paskaitą vykdomas testas](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## Tyrinėkite paukščių duomenų rinkinį

Kitas būdas gilintis į duomenis yra pažvelgti į jų pasiskirstymą arba kaip duomenys yra organizuoti pagal ašį. Pavyzdžiui, galbūt norėtumėte sužinoti apie bendrą maksimalios sparnų amplitudės ar maksimalios kūno masės pasiskirstymą Minesotos paukščių duomenų rinkinyje.

Atraskime keletą faktų apie šio duomenų rinkinio pasiskirstymus. Savo R konsolėje importuokite `ggplot2` ir duomenų bazę. Pašalinkite išskirtis iš duomenų bazės, kaip tai darėte ankstesnėje temoje.

```r
library(ggplot2)

birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")

birds_filtered <- subset(birds, MaxWingspan < 500)
head(birds_filtered)
```
|      | Pavadinimas                  | MokslinisPavadinimas   | Kategorija            | Būrys        | Šeima    | Gentis      | ApsaugosStatusas    | MinIlgis | MaxIlgis | MinKūnoMasa | MaxKūnoMasa | MinSparnųAmplitudė | MaxSparnųAmplitudė |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | -----------------: | -----------------: |
|    0 | Juodapilvė švilpiko antis    | Dendrocygna autumnalis | Antys/Žąsys/Vandensf. | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |                  76 |                  94 |
|    1 | Rudapilvė švilpiko antis     | Dendrocygna bicolor    | Antys/Žąsys/Vandensf. | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |                  85 |                  93 |
|    2 | Snieginė žąsis               | Anser caerulescens     | Antys/Žąsys/Vandensf. | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |                 135 |                 165 |
|    3 | Rosso žąsis                  | Anser rossii           | Antys/Žąsys/Vandensf. | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |                 113 |                 116 |
|    4 | Didžioji baltakaktė žąsis    | Anser albifrons        | Antys/Žąsys/Vandensf. | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |                 130 |                 165 |

Apskritai, galite greitai pažvelgti į tai, kaip duomenys pasiskirstę, naudodami sklaidos diagramą, kaip tai darėme ankstesnėje pamokoje:

```r
ggplot(data=birds_filtered, aes(x=Order, y=MaxLength,group=1)) +
  geom_point() +
  ggtitle("Max Length per order") + coord_flip()
```
![maksimalus ilgis pagal būrį](../../../../../translated_images/lt/max-length-per-order.e5b283d952c78c12b091307c5d3cf67132dad6fefe80a073353b9dc5c2bd3eb8.png)

Tai suteikia bendrą paukščių kūno ilgio pasiskirstymo pagal būrį apžvalgą, tačiau tai nėra optimalus būdas tikriems pasiskirstymams parodyti. Šią užduotį paprastai atlieka histograma.

## Darbas su histogramomis

`ggplot2` siūlo puikius būdus vizualizuoti duomenų pasiskirstymą naudojant histogramas. Šio tipo diagrama yra panaši į stulpelinę diagramą, kur pasiskirstymas matomas per stulpelių kilimą ir kritimą. Norint sukurti histogramą, reikia skaitinių duomenų. Histogramai sukurti galite nurodyti diagramos tipą kaip 'hist'. Ši diagrama rodo MaxBodyMass pasiskirstymą visame duomenų rinkinio skaitinių duomenų diapazone. Padalindama duomenų masyvą į mažesnius intervalus, ji gali parodyti duomenų reikšmių pasiskirstymą:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=10)+ylab('Frequency')
```
![pasiskirstymas visame duomenų rinkinyje](../../../../../translated_images/lt/distribution-over-the-entire-dataset.d22afd3fa96be854e4c82213fedec9e3703cba753d07fad4606aadf58cf7e78e.png)

Kaip matote, dauguma iš 400+ paukščių šiame duomenų rinkinyje patenka į mažesnę nei 2000 Max Kūno Masės ribą. Gaukite daugiau įžvalgų apie duomenis, pakeisdami `bins` parametrą į didesnį skaičių, pavyzdžiui, 30:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + geom_histogram(bins=30)+ylab('Frequency')
```

![pasiskirstymas su 30 intervalų](../../../../../translated_images/lt/distribution-30bins.6a3921ea7a421bf71f06bf5231009e43d1146f1b8da8dc254e99b5779a4983e5.png)

Ši diagrama rodo pasiskirstymą šiek tiek detaliau. Mažiau į kairę pasvirusią diagramą būtų galima sukurti užtikrinant, kad pasirinktumėte tik duomenis tam tikrame diapazone:

Filtruokite savo duomenis, kad gautumėte tik tuos paukščius, kurių kūno masė yra mažesnė nei 60, ir parodykite 30 `bins`:

```r
birds_filtered_1 <- subset(birds_filtered, MaxBodyMass > 1 & MaxBodyMass < 60)
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=30)+ylab('Frequency')
```

![filtruota histograma](../../../../../translated_images/lt/filtered-histogram.6bf5d2bfd82533220e1bd4bc4f7d14308f43746ed66721d9ec8f460732be6674.png)

✅ Išbandykite kitus filtrus ir duomenų taškus. Norėdami pamatyti visą duomenų pasiskirstymą, pašalinkite `['MaxBodyMass']` filtrą, kad parodytumėte pažymėtus pasiskirstymus.

Histograma taip pat siūlo gražius spalvų ir žymėjimo patobulinimus, kuriuos verta išbandyti:

Sukurkite 2D histogramą, kad palygintumėte dviejų pasiskirstymų santykį. Palyginkime `MaxBodyMass` ir `MaxLength`. `ggplot2` siūlo įmontuotą būdą parodyti susiliejimą naudojant ryškesnes spalvas:

```r
ggplot(data=birds_filtered_1, aes(x=MaxBodyMass, y=MaxLength) ) +
  geom_bin2d() +scale_fill_continuous(type = "viridis")
```
Atrodo, kad tarp šių dviejų elementų yra tikėtinas koreliavimas pagal numatomą ašį, su viena ypač stipria susiliejimo vieta:

![2D diagrama](../../../../../translated_images/lt/2d-plot.c504786f439bd7ebceebf2465c70ca3b124103e06c7ff7214bf24e26f7aec21e.png)

Histogramų numatytasis veikimas gerai tinka skaitiniams duomenims. O kas, jei reikia pamatyti pasiskirstymus pagal tekstinius duomenis? 
## Tyrinėkite duomenų rinkinį pagal tekstinius duomenis

Šiame duomenų rinkinyje taip pat yra geros informacijos apie paukščių kategoriją, jų gentį, rūšį, šeimą bei apsaugos statusą. Panagrinėkime šią apsaugos informaciją. Koks yra paukščių pasiskirstymas pagal jų apsaugos statusą?

> ✅ Duomenų rinkinyje naudojami keli akronimai, apibūdinantys apsaugos statusą. Šie akronimai yra iš [IUCN Raudonojo sąrašo kategorijų](https://www.iucnredlist.org/), organizacijos, kataloguojančios rūšių būklę.
> 
> - CR: Kritiškai nykstantis
> - EN: Nykstantis
> - EX: Išnykęs
> - LC: Mažiausiai susirūpinimą keliantis
> - NT: Beveik nykstantis
> - VU: Pažeidžiamas

Kadangi tai yra tekstinės reikšmės, reikės atlikti transformaciją, kad sukurtumėte histogramą. Naudodami `filteredBirds` duomenų rėmelį, parodykite jo apsaugos statusą kartu su minimaliu sparnų amplitudės dydžiu. Ką pastebite?

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

![sparnų amplitudė ir apsaugos statusas](../../../../../translated_images/lt/wingspan-conservation-collation.4024e9aa6910866aa82f0c6cb6a6b4b925bd10079e6b0ef8f92eefa5a6792f76.png)

Atrodo, kad nėra gero koreliavimo tarp minimalaus sparnų amplitudės dydžio ir apsaugos statuso. Išbandykite kitus duomenų rinkinio elementus naudodami šį metodą. Taip pat galite išbandyti skirtingus filtrus. Ar pastebite kokį nors koreliavimą?

## Tankio diagramos

Galbūt pastebėjote, kad iki šiol nagrinėtos histogramos yra „laiptinės“ ir nesudaro sklandžios kreivės. Norėdami parodyti sklandesnę tankio diagramą, galite išbandyti tankio diagramą.

Dabar dirbkime su tankio diagramomis!

```r
ggplot(data = birds_filtered_1, aes(x = MinWingspan)) + 
  geom_density()
```
![tankio diagrama](../../../../../translated_images/lt/density-plot.675ccf865b76c690487fb7f69420a8444a3515f03bad5482886232d4330f5c85.png)

Galite matyti, kaip ši diagrama atspindi ankstesnę minimalaus sparnų amplitudės duomenų diagramą; ji tiesiog šiek tiek sklandesnė. Jei norėtumėte peržiūrėti tą dantytą MaxBodyMass liniją antroje sukurtoje diagramoje, galėtumėte ją labai gerai išlyginti, naudodami šį metodą:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density()
```
![kūno masės tankis](../../../../../translated_images/lt/bodymass-smooth.d31ce526d82b0a1f19a073815dea28ecfbe58145ec5337e4ef7e8cdac81120b3.png)

Jei norėtumėte sklandžios, bet ne per daug sklandžios linijos, redaguokite `adjust` parametrą:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density(adjust = 1/5)
```
![mažiau sklandi kūno masė](../../../../../translated_images/lt/less-smooth-bodymass.10f4db8b683cc17d17b2d33f22405413142004467a1493d416608dafecfdee23.png)

✅ Perskaitykite apie šio tipo diagramos parametrus ir eksperimentuokite!

Šio tipo diagrama siūlo gražiai paaiškinančias vizualizacijas. Pavyzdžiui, su keliomis kodo eilutėmis galite parodyti maksimalios kūno masės tankį pagal paukščių būrį:

```r
ggplot(data=birds_filtered_1,aes(x = MaxBodyMass, fill = Order)) +
  geom_density(alpha=0.5)
```
![kūno masė pagal būrį](../../../../../translated_images/lt/bodymass-per-order.9d2b065dd931b928c839d8cdbee63067ab1ae52218a1b90717f4bc744354f485.png)

## 🚀 Iššūkis

Histogramų naudojimas yra sudėtingesnis nei paprastų sklaidos diagramų, stulpelinių diagramų ar linijinių diagramų. Ieškokite internete gerų histogramų naudojimo pavyzdžių. Kaip jos naudojamos, ką jos parodo ir kokiose srityse ar tyrimų srityse jos dažniausiai naudojamos?

## [Po paskaitos vykdomas testas](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## Apžvalga ir savarankiškas mokymasis

Šioje pamokoje naudojote `ggplot2` ir pradėjote kurti sudėtingesnes diagramas. Atlikite tyrimą apie `geom_density_2d()`, „nepertraukiamą tikimybės tankio kreivę vienoje ar keliose dimensijose“. Perskaitykite [dokumentaciją](https://ggplot2.tidyverse.org/reference/geom_density_2d.html), kad suprastumėte, kaip ji veikia.

## Užduotis

[Praktikuokite savo įgūdžius](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipiame dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudotis profesionalių vertėjų paslaugomis. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, kylančius dėl šio vertimo naudojimo.