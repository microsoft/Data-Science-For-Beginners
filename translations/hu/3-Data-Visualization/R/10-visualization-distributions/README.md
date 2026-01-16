<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea67c0c40808fd723594de6896c37ccf",
  "translation_date": "2025-08-26T16:59:09+00:00",
  "source_file": "3-Data-Visualization/R/10-visualization-distributions/README.md",
  "language_code": "hu"
}
-->
# Az eloszlások vizualizálása

|![ Sketchnote készítette: [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Az eloszlások vizualizálása - _Sketchnote készítette: [@nitya](https://twitter.com/nitya)_ |

Az előző leckében érdekes tényeket tanultál a Minnesotában élő madarakról szóló adathalmazról. Hibás adatokat találtál a kiugró értékek vizualizálásával, és megvizsgáltad a madárkategóriák közötti különbségeket a maximális hosszúságuk alapján.

## [Előadás előtti kvíz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## Fedezd fel a madarak adathalmazát

Egy másik módja az adatok mélyebb megértésének, ha megvizsgáljuk azok eloszlását, vagyis azt, hogy az adatok hogyan rendeződnek el egy tengely mentén. Például szeretnéd megtudni, hogy milyen az általános eloszlás ebben az adathalmazban a Minnesotában élő madarak maximális szárnyfesztávolsága vagy maximális testtömege alapján.

Fedezzünk fel néhány tényt az adatok eloszlásáról ebben az adathalmazban. Az R konzolban importáld a `ggplot2` csomagot és az adatbázist. Távolítsd el a kiugró értékeket az adatbázisból, ahogy az előző témában is tetted.

```r
library(ggplot2)

birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")

birds_filtered <- subset(birds, MaxWingspan < 500)
head(birds_filtered)
```
|      | Név                          | TudományosNév          | Kategória             | Rend         | Család   | Nemzetség   | TermészetvédelmiStátusz | MinHossz | MaxHossz | MinTestTömeg | MaxTestTömeg | MinSzárnyfesztáv | MaxSzárnyfesztáv |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :---------------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Feketehasú sípoló kacsa      | Dendrocygna autumnalis | Kacsák/Ludak/Vízimadarak | Anseriformes | Anatidae | Dendrocygna | LC                     |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous sípoló kacsa         | Dendrocygna bicolor    | Kacsák/Ludak/Vízimadarak | Anseriformes | Anatidae | Dendrocygna | LC                     |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Hóliba                       | Anser caerulescens     | Kacsák/Ludak/Vízimadarak | Anseriformes | Anatidae | Anser       | LC                     |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross-liba                    | Anser rossii           | Kacsák/Ludak/Vízimadarak | Anseriformes | Anatidae | Anser       | LC                     |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Nagy fehérhomlokú lúd        | Anser albifrons        | Kacsák/Ludak/Vízimadarak | Anseriformes | Anatidae | Anser       | LC                     |        64 |        81 |        1930 |        3310 |         130 |         165 |

Általánosságban gyorsan megvizsgálhatod az adatok eloszlását egy szórásdiagram segítségével, ahogy az előző leckében is tettük:

```r
ggplot(data=birds_filtered, aes(x=Order, y=MaxLength,group=1)) +
  geom_point() +
  ggtitle("Max Length per order") + coord_flip()
```
![max hosszúság rendenként](../../../../../translated_images/hu/max-length-per-order.e5b283d952c78c12b091307c5d3cf67132dad6fefe80a073353b9dc5c2bd3eb8.png)

Ez egy áttekintést ad a madarak testhosszának eloszlásáról rendenként, de nem a legoptimálisabb módja az igazi eloszlások megjelenítésének. Ezt a feladatot általában hisztogramokkal oldják meg.

## Hisztogramok használata

A `ggplot2` kiváló eszközöket kínál az adatok eloszlásának vizualizálására hisztogramok segítségével. Ez a fajta diagram hasonlít az oszlopdiagramhoz, ahol az eloszlás a sávok emelkedésén és csökkenésén keresztül látható. Hisztogram készítéséhez numerikus adatokra van szükség. Hisztogram létrehozásához a diagram típusát 'hist'-ként kell megadni. Ez a diagram megmutatja az adathalmaz MaxTestTömeg értékeinek eloszlását az egész numerikus adat tartományban. Az adatok tömbjét kisebb bin-ekre osztva megjeleníti az értékek eloszlását:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=10)+ylab('Frequency')
```
![eloszlás az egész adathalmazon](../../../../../translated_images/hu/distribution-over-the-entire-dataset.d22afd3fa96be854e4c82213fedec9e3703cba753d07fad4606aadf58cf7e78e.png)

Ahogy látható, a több mint 400 madár többsége ebben az adathalmazban 2000 alatti MaxTestTömeg tartományba esik. Mélyebb betekintést nyerhetsz az adatokba, ha a `bins` paramétert magasabb számra, például 30-ra állítod:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + geom_histogram(bins=30)+ylab('Frequency')
```

![eloszlás 30 bin-nel](../../../../../translated_images/hu/distribution-30bins.6a3921ea7a421bf71f06bf5231009e43d1146f1b8da8dc254e99b5779a4983e5.png)

Ez a diagram kicsit részletesebb módon mutatja az eloszlást. Egy kevésbé balra torzított diagramot hozhatsz létre, ha csak egy adott tartományon belüli adatokat választasz ki:

Szűrd az adatokat úgy, hogy csak azok a madarak maradjanak, amelyek testtömege 60 alatt van, és állítsd be a `bins` értékét 30-ra:

```r
birds_filtered_1 <- subset(birds_filtered, MaxBodyMass > 1 & MaxBodyMass < 60)
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=30)+ylab('Frequency')
```

![szűrt hisztogram](../../../../../translated_images/hu/filtered-histogram.6bf5d2bfd82533220e1bd4bc4f7d14308f43746ed66721d9ec8f460732be6674.png)

✅ Próbálj ki más szűrőket és adatpontokat. Az adatok teljes eloszlásának megtekintéséhez távolítsd el a `['MaxBodyMass']` szűrőt, hogy címkézett eloszlásokat mutass.

A hisztogram további színezési és címkézési lehetőségeket is kínál:

Hozz létre egy 2D hisztogramot, hogy összehasonlítsd két eloszlás kapcsolatát. Hasonlítsuk össze a `MaxBodyMass` és a `MaxLength` értékeket. A `ggplot2` beépített módot kínál a konvergencia megjelenítésére élénkebb színek használatával:

```r
ggplot(data=birds_filtered_1, aes(x=MaxBodyMass, y=MaxLength) ) +
  geom_bin2d() +scale_fill_continuous(type = "viridis")
```
Úgy tűnik, hogy van egy várható korreláció a két elem között egy előre látható tengely mentén, egy különösen erős konvergencia ponttal:

![2d diagram](../../../../../translated_images/hu/2d-plot.c504786f439bd7ebceebf2465c70ca3b124103e06c7ff7214bf24e26f7aec21e.png)

A hisztogramok alapértelmezés szerint jól működnek numerikus adatokkal. Mi van akkor, ha szöveges adatok szerint szeretnéd látni az eloszlásokat? 
## Az adathalmaz eloszlásának vizsgálata szöveges adatok alapján 

Ez az adathalmaz jó információkat tartalmaz a madárkategóriáról, nemzetségről, fajról és családról, valamint természetvédelmi státuszáról. Nézzük meg közelebbről ezt a természetvédelmi információt. Mi a madarak eloszlása természetvédelmi státuszuk szerint?

> ✅ Az adathalmazban több rövidítés található a természetvédelmi státusz leírására. Ezek a rövidítések az [IUCN Vörös Lista Kategóriákból](https://www.iucnredlist.org/) származnak, amely egy szervezet, amely a fajok státuszát katalogizálja.
> 
> - CR: Kritikus veszélyeztetett
> - EN: Veszélyeztetett
> - EX: Kihalt
> - LC: Legkevésbé aggasztó
> - NT: Közel fenyegetett
> - VU: Sebezhető

Ezek szöveges értékek, így transzformációra lesz szükséged a hisztogram létrehozásához. Használva a szűrtBirds adatkeretet, jelenítsd meg a természetvédelmi státuszt a Minimális Szárnyfesztáv mellett. Mit látsz? 

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

![szárnyfesztáv és természetvédelmi státusz](../../../../../translated_images/hu/wingspan-conservation-collation.4024e9aa6910866aa82f0c6cb6a6b4b925bd10079e6b0ef8f92eefa5a6792f76.png)

Úgy tűnik, hogy nincs jó korreláció a minimális szárnyfesztáv és a természetvédelmi státusz között. Tesztelj más elemeket az adathalmazból ezzel a módszerrel. Próbálj ki különböző szűrőket is. Találsz bármilyen korrelációt?

## Sűrűségdiagramok

Észrevehetted, hogy az eddig vizsgált hisztogramok "lépcsőzetesek", és nem folynak simán ívben. Ha simább sűrűségi diagramot szeretnél, próbálj ki egy sűrűségdiagramot.

Most dolgozzunk sűrűségdiagramokkal!

```r
ggplot(data = birds_filtered_1, aes(x = MinWingspan)) + 
  geom_density()
```
![sűrűségdiagram](../../../../../translated_images/hu/density-plot.675ccf865b76c690487fb7f69420a8444a3515f03bad5482886232d4330f5c85.png)

Láthatod, hogy a diagram visszatükrözi a korábbi Minimális Szárnyfesztáv adatokat; csak egy kicsit simább. Ha szeretnéd újraalkotni a második diagramon látott MaxTestTömeg "szaggatott" vonalat, nagyon jól kisimíthatod ezt a módszert használva:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density()
```
![testtömeg sűrűség](../../../../../translated_images/hu/bodymass-smooth.d31ce526d82b0a1f19a073815dea28ecfbe58145ec5337e4ef7e8cdac81120b3.png)

Ha sima, de nem túl sima vonalat szeretnél, szerkeszd az `adjust` paramétert: 

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density(adjust = 1/5)
```
![kevésbé sima testtömeg](../../../../../translated_images/hu/less-smooth-bodymass.10f4db8b683cc17d17b2d33f22405413142004467a1493d416608dafecfdee23.png)

✅ Olvass utána az elérhető paramétereknek ehhez a diagramtípushoz, és kísérletezz!

Ez a diagramtípus gyönyörűen magyarázó vizualizációkat kínál. Például néhány kódsorral megmutathatod a madarak rendenkénti maximális testtömeg sűrűségét:

```r
ggplot(data=birds_filtered_1,aes(x = MaxBodyMass, fill = Order)) +
  geom_density(alpha=0.5)
```
![testtömeg rendenként](../../../../../translated_images/hu/bodymass-per-order.9d2b065dd931b928c839d8cdbee63067ab1ae52218a1b90717f4bc744354f485.png)

## 🚀 Kihívás

A hisztogramok kifinomultabb diagramtípusok, mint az alapvető szórásdiagramok, oszlopdiagramok vagy vonaldiagramok. Keress jó példákat az interneten a hisztogramok használatára. Hogyan használják őket, mit mutatnak be, és milyen területeken vagy kutatási területeken alkalmazzák őket?

## [Előadás utáni kvíz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## Áttekintés és önálló tanulás

Ebben a leckében a `ggplot2` csomagot használtad, és elkezdtél kifinomultabb diagramokat készíteni. Kutass a `geom_density_2d()` funkcióról, amely "folyamatos valószínűségi sűrűség görbét mutat egy vagy több dimenzióban". Olvasd el [a dokumentációt](https://ggplot2.tidyverse.org/reference/geom_density_2d.html), hogy megértsd, hogyan működik.

## Feladat

[Alkalmazd a tudásod](assignment.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.