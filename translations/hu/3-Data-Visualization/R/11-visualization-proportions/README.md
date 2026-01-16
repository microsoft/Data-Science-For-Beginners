<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "47028abaaafa2bcb1079702d20569066",
  "translation_date": "2025-08-26T17:19:17+00:00",
  "source_file": "3-Data-Visualization/R/11-visualization-proportions/README.md",
  "language_code": "hu"
}
-->
# Arányok vizualizálása

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Arányok vizualizálása - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Ebben a leckében egy természetközpontú adatállományt fogsz használni, hogy vizualizáld az arányokat, például azt, hogy hány különböző gombafaj található egy adott adatállományban a gombákról. Fedezzük fel ezeket a lenyűgöző gombákat egy Audubon által összeállított adatállomány segítségével, amely 23 lemezes gombafajt tartalmaz az Agaricus és Lepiota családokból. Kísérletezni fogsz ínycsiklandó vizualizációkkal, mint például:

- Torta diagramok 🥧
- Fánk diagramok 🍩
- Waffle diagramok 🧇

> 💡 Egy nagyon érdekes projekt, a [Charticulator](https://charticulator.com) a Microsoft Research-től, ingyenes drag-and-drop felületet kínál adatvizualizációkhoz. Az egyik oktatóanyagukban szintén ezt a gomba adatállományt használják! Így egyszerre fedezheted fel az adatokat és tanulhatod meg a könyvtár használatát: [Charticulator oktatóanyag](https://charticulator.com/tutorials/tutorial4.html).

## [Előadás előtti kvíz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## Ismerd meg a gombáidat 🍄

A gombák nagyon érdekesek. Importáljunk egy adatállományt, hogy tanulmányozhassuk őket:

```r
mushrooms = read.csv('../../data/mushrooms.csv')
head(mushrooms)
```
Egy táblázat jelenik meg, amely remek elemzési adatokat tartalmaz:


| osztály   | kalap-alak | kalap-felület | kalap-szín | zúzódások | illat    | lemez-csatlakozás | lemez-távolság | lemez-méret | lemez-szín | szár-alak | szár-gyökér | szár-felület-gyűrű-felett | szár-felület-gyűrű-alatt | szár-szín-gyűrű-felett | szár-szín-gyűrű-alatt | fátyol-típus | fátyol-szín | gyűrű-szám | gyűrű-típus | spóra-nyomat-szín | populáció | élőhely |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Mérgező   | Domború   | Sima        | Barna     | Zúzódik | Erős    | Szabad          | Szoros       | Keskeny   | Fekete     | Vastagodó   | Egyenlő    | Sima                     | Sima                     | Fehér                  | Fehér                  | Részleges  | Fehér      | Egy         | Függőleges | Fekete            | Szórványos | Városi  |
| Ehető     | Domború   | Sima        | Sárga     | Zúzódik | Mandula | Szabad          | Szoros       | Széles    | Fekete     | Vastagodó   | Klub       | Sima                     | Sima                     | Fehér                  | Fehér                  | Részleges  | Fehér      | Egy         | Függőleges | Barna             | Számos     | Füves   |
| Ehető     | Harang    | Sima        | Fehér     | Zúzódik | Ánizs   | Szabad          | Szoros       | Széles    | Barna      | Vastagodó   | Klub       | Sima                     | Sima                     | Fehér                  | Fehér                  | Részleges  | Fehér      | Egy         | Függőleges | Barna             | Számos     | Rét     |
| Mérgező   | Domború   | Pikkelyes   | Fehér     | Zúzódik | Erős    | Szabad          | Szoros       | Keskeny   | Barna      | Vastagodó   | Egyenlő    | Sima                     | Sima                     | Fehér                  | Fehér                  | Részleges  | Fehér      | Egy         | Függőleges | Fekete            | Szórványos | Városi 
| Ehető     | Domború   | Sima        | Zöld      | Nem zúzódik | Nincs | Szabad          | Zsúfolt     | Széles    | Fekete     | Keskenyedő | Egyenlő    | Sima                     | Sima                     | Fehér                  | Fehér                  | Részleges  | Fehér      | Egy         | Elillanó  | Barna             | Bőséges    | Füves   |
| Ehető     | Domború   | Pikkelyes   | Sárga     | Zúzódik | Mandula | Szabad          | Szoros       | Széles    | Barna      | Vastagodó   | Klub       | Sima                     | Sima                     | Fehér                  | Fehér                  | Részleges  | Fehér      | Egy         | Függőleges | Fekete            | Számos     | Füves   

Rögtön észreveheted, hogy az összes adat szöveges. Az adatokat át kell alakítanod, hogy diagramon használhatóak legyenek. Valójában az adatok többsége objektumként van ábrázolva:

```r
names(mushrooms)
```

Az eredmény:

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
Konvertáld az 'osztály' oszlopot kategóriává:

```r
library(dplyr)
grouped=mushrooms %>%
  group_by(class) %>%
  summarise(count=n())
```

Most, ha kinyomtatod a gomba adatokat, láthatod, hogy azokat kategóriákba csoportosították a mérgező/ehető osztály szerint:
```r
View(grouped)
```


| osztály | darabszám |
| --------- | --------- |
| Ehető     | 4208     |
| Mérgező   | 3916     |


Ha követed a táblázatban bemutatott sorrendet az osztály kategória címkék létrehozásához, készíthetsz egy torta diagramot.

## Torta!

```r
pie(grouped$count,grouped$class, main="Edible?")
```
Voilá, egy torta diagram, amely bemutatja az adatok arányait a gombák két osztálya szerint. Nagyon fontos, hogy a címkék sorrendje helyes legyen, különösen itt, ezért ellenőrizd a címke tömb létrehozásának sorrendjét!

![torta diagram](../../../../../translated_images/hu/pie1-wb.685df063673751f4b0b82127f7a52c7f9a920192f22ae61ad28412ba9ace97bf.png)

## Fánkok!

Egy vizuálisan érdekesebb torta diagram a fánk diagram, amely egy lyukkal rendelkező torta diagram. Nézzük meg az adatainkat ezzel a módszerrel.

Nézd meg a különböző élőhelyeket, ahol a gombák nőnek:

```r
library(dplyr)
habitat=mushrooms %>%
  group_by(habitat) %>%
  summarise(count=n())
View(habitat)
```
Az eredmény:
| élőhely | darabszám |
| --------- | --------- |
| Füves     | 2148     |
| Levelek   | 832      |
| Rét       | 292      |
| Ösvények  | 1144     |
| Városi    | 368      |
| Hulladék  | 192      |
| Fa        | 3148     |


Itt az adatokat élőhely szerint csoportosítod. Hét élőhely van felsorolva, ezeket használd címkékként a fánk diagramhoz:

```r
library(ggplot2)
library(webr)
PieDonut(habitat, aes(habitat, count=count))
```

![fánk diagram](../../../../../translated_images/hu/donut-wb.34e6fb275da9d834c2205145e39a3de9b6878191dcdba6f7a9e85f4b520449bc.png)

Ez a kód két könyvtárat használ - ggplot2 és webr. A webr könyvtár PieDonut függvényével könnyen készíthetünk fánk diagramot!

Fánk diagramokat R-ben csak a ggplot2 könyvtár segítségével is lehet készíteni. Erről többet megtudhatsz [itt](https://www.r-graph-gallery.com/128-ring-or-donut-plot.html), és kipróbálhatod magad.

Most, hogy tudod, hogyan csoportosítsd az adatokat, majd jelenítsd meg őket torta vagy fánk diagramként, felfedezhetsz más típusú diagramokat is. Próbálj ki egy waffle diagramot, amely egy másik módja a mennyiségek vizualizálásának.
## Waffle!

A 'waffle' típusú diagram egy másik módja a mennyiségek vizualizálásának, egy 2D négyzetes tömb formájában. Próbáld meg vizualizálni a gombakalap színek különböző mennyiségeit ebben az adatállományban. Ehhez telepítened kell egy segédkönyvtárat, a [waffle](https://cran.r-project.org/web/packages/waffle/waffle.pdf) könyvtárat, és használnod kell a vizualizáció létrehozásához:

```r
install.packages("waffle", repos = "https://cinc.rud.is")
```

Válassz ki egy adat szegmenst a csoportosításhoz:

```r
library(dplyr)
cap_color=mushrooms %>%
  group_by(cap.color) %>%
  summarise(count=n())
View(cap_color)
```

Hozz létre egy waffle diagramot címkék létrehozásával, majd csoportosítsd az adatokat:

```r
library(waffle)
names(cap_color$count) = paste0(cap_color$cap.color)
waffle((cap_color$count/10), rows = 7, title = "Waffle Chart")+scale_fill_manual(values=c("brown", "#F0DC82", "#D2691E", "green", 
                                                                                     "pink", "purple", "red", "grey", 
                                                                                     "yellow","white"))
```

A waffle diagram segítségével egyértelműen láthatod a gombakalap színek arányait ebben az adatállományban. Érdekes módon sok zöld kalapú gomba van!

![waffle diagram](../../../../../translated_images/hu/waffle.aaa75c5337735a6ef32ace0ffb6506ef49e5aefe870ffd72b1bb080f4843c217.png)

Ebben a leckében három módot tanultál meg az arányok vizualizálására. Először csoportosítanod kell az adatokat kategóriákba, majd eldönteni, hogy melyik a legjobb módja az adatok megjelenítésének - torta, fánk vagy waffle. Mindegyik ínycsiklandó, és azonnali pillanatképet nyújt az adatállományról.

## 🚀 Kihívás

Próbáld meg újra létrehozni ezeket az ínycsiklandó diagramokat a [Charticulator](https://charticulator.com) segítségével.
## [Előadás utáni kvíz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## Áttekintés és önálló tanulás

Néha nem egyértelmű, hogy mikor használjunk torta, fánk vagy waffle diagramot. Íme néhány cikk, amit elolvashatsz a témában:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Végezz kutatást, hogy további információkat találj erről a nehéz döntésről.
## Feladat

[Próbáld ki Excelben](assignment.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.