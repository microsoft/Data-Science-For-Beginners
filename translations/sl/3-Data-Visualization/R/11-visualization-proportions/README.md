<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "47028abaaafa2bcb1079702d20569066",
  "translation_date": "2025-08-30T18:40:59+00:00",
  "source_file": "3-Data-Visualization/R/11-visualization-proportions/README.md",
  "language_code": "sl"
}
-->
# Vizualizacija deležev

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Vizualizacija deležev - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

V tej lekciji boste uporabili naravoslovno usmerjen nabor podatkov za vizualizacijo deležev, na primer koliko različnih vrst gliv je prisotnih v določenem naboru podatkov o gobah. Raziskali bomo te fascinantne glive z naborom podatkov, pridobljenim iz Audubona, ki vsebuje podrobnosti o 23 vrstah gob z lističi iz družin Agaricus in Lepiota. Eksperimentirali boste z okusnimi vizualizacijami, kot so:

- Torte 🥧
- Krofi 🍩
- Vaflji 🧇

> 💡 Zelo zanimiv projekt, imenovan [Charticulator](https://charticulator.com) iz Microsoft Research, ponuja brezplačen vmesnik za vizualizacijo podatkov z metodo povleci in spusti. V enem od njihovih vaj uporabljajo tudi ta nabor podatkov o gobah! Tako lahko raziskujete podatke in hkrati spoznate knjižnico: [Charticulator tutorial](https://charticulator.com/tutorials/tutorial4.html).

## [Predlekcijski kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## Spoznajte svoje gobe 🍄

Gobe so zelo zanimive. Uvozimo nabor podatkov, da jih preučimo:

```r
mushrooms = read.csv('../../data/mushrooms.csv')
head(mushrooms)
```
Izpiše se tabela z odličnimi podatki za analizo:


| razred     | oblika klobuka | površina klobuka | barva klobuka | modrice | vonj    | pritrditev lističev | razmik lističev | velikost lističev | barva lističev | oblika bet | koren bet | površina nad obročem | površina pod obročem | barva nad obročem | barva pod obročem | tip zastiralca | barva zastiralca | število obročev | tip obroča | barva trosov | populacija | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Strupena | Konveksna    | Gladka      | Rjava     | Modrice | Ostri vonj | Prosto            | Tesno        | Ozki    | Črna      | Širjenje   | Enak      | Gladka                   | Gladka                   | Bela                  | Bela                  | Delna   | Bela      | Ena         | Viseči   | Črna             | Razpršena  | Urbana   |
| Užitna    | Konveksna    | Gladka      | Rumena    | Modrice | Mandelj  | Prosto            | Tesno        | Široki     | Črna      | Širjenje   | Klub       | Gladka                   | Gladka                   | Bela                  | Bela                  | Delna   | Bela      | Ena         | Viseči   | Rjava             | Številna   | Trave |
| Užitna    | Zvonec      | Gladka      | Bela     | Modrice | Janež   | Prosto            | Tesno        | Široki     | Rjava      | Širjenje   | Klub       | Gladka                   | Gladka                   | Bela                  | Bela                  | Delna   | Bela      | Ena         | Viseči   | Rjava             | Številna   | Travniki |
| Strupena | Konveksna    | Luskasta       | Bela     | Modrice | Ostri vonj | Prosto            | Tesno        | Ozki    | Rjava      | Širjenje   | Enak      | Gladka                   | Gladka                   | Bela                  | Bela                  | Delna   | Bela      | Ena         | Viseči   | Črna             | Razpršena  | Urbana 
| Užitna | Konveksna       |Gladka       | Zelena     | Brez modric| Brez vonja   |Prosto            | Gosto       | Široki     | Črna      | Zoženje   | Enak      |  Gladka | Gladka                    | Bela                 | Bela                  | Delna    | Bela     | Ena         | Izginjajoči | Rjava             | Obilna | Trave
|Užitna  |  Konveksna      | Luskasta   | Rumena         | Modrice  | Mandelj  | Prosto | Tesno  |   Široki   |   Rjava  | Širjenje   |   Klub                      | Gladka                  | Gladka    | Bela                 |  Bela                | Delna      | Bela    |  Ena  |  Viseči | Črna   | Številna | Trave
      
Takoj opazite, da so vsi podatki tekstovni. Te podatke boste morali pretvoriti, da jih boste lahko uporabili v grafu. Večina podatkov je dejansko predstavljena kot objekt:

```r
names(mushrooms)
```

Rezultat je:

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
Vzemite te podatke in pretvorite stolpec 'razred' v kategorijo:

```r
library(dplyr)
grouped=mushrooms %>%
  group_by(class) %>%
  summarise(count=n())
```


Zdaj, če izpišete podatke o gobah, lahko vidite, da so razvrščeni v kategorije glede na razred strupenosti/užitnosti:
```r
View(grouped)
```


| razred | število |
| --------- | --------- |
| Užitna | 4208 |
| Strupena| 3916 |



Če sledite vrstnemu redu, predstavljenemu v tej tabeli, da ustvarite oznake kategorij razreda, lahko ustvarite tortni graf.

## Torta!

```r
pie(grouped$count,grouped$class, main="Edible?")
```
Voila, tortni graf, ki prikazuje deleže teh podatkov glede na ti dve kategoriji gob. Zelo pomembno je, da je vrstni red oznak pravilen, še posebej tukaj, zato preverite vrstni red, s katerim je ustvarjen niz oznak!

![tortni graf](../../../../../translated_images/sl/pie1-wb.685df063673751f4b0b82127f7a52c7f9a920192f22ae61ad28412ba9ace97bf.png)

## Krofi!

Malce bolj vizualno zanimiv tortni graf je krofni graf, ki je tortni graf z luknjo v sredini. Poglejmo naše podatke s to metodo.

Oglejte si različna okolja, kjer rastejo gobe:

```r
library(dplyr)
habitat=mushrooms %>%
  group_by(habitat) %>%
  summarise(count=n())
View(habitat)
```
Rezultat je:
| habitat| število |
| --------- | --------- |
| Trave    | 2148 |
| Listje| 832 |
| Travniki    | 292 |
| Poti| 1144 |
| Urbana    | 368 |
| Odpadki| 192 |
| Les| 3148 |


Tukaj razvrščate svoje podatke po habitatih. Naštetih je 7, zato jih uporabite kot oznake za krofni graf:

```r
library(ggplot2)
library(webr)
PieDonut(habitat, aes(habitat, count=count))
```

![krofni graf](../../../../../translated_images/sl/donut-wb.34e6fb275da9d834c2205145e39a3de9b6878191dcdba6f7a9e85f4b520449bc.png)

Ta koda uporablja dve knjižnici - ggplot2 in webr. Z uporabo funkcije PieDonut iz knjižnice webr lahko enostavno ustvarimo krofni graf!

Krofne grafe v R lahko ustvarimo tudi samo z uporabo knjižnice ggplot2. Več o tem lahko izveste [tukaj](https://www.r-graph-gallery.com/128-ring-or-donut-plot.html) in poskusite sami.

Zdaj, ko veste, kako razvrstiti svoje podatke in jih nato prikazati kot torto ali krof, lahko raziščete druge vrste grafov. Poskusite vafeljni graf, ki je le drugačen način raziskovanja količine.
## Vaflji!

Graf tipa 'vafelj' je drugačen način vizualizacije količin kot 2D matrika kvadratov. Poskusite vizualizirati različne količine barv klobukov gob v tem naboru podatkov. Za to morate namestiti pomožno knjižnico, imenovano [waffle](https://cran.r-project.org/web/packages/waffle/waffle.pdf), in jo uporabiti za ustvarjanje svoje vizualizacije:

```r
install.packages("waffle", repos = "https://cinc.rud.is")
```

Izberite segment svojih podatkov za razvrščanje:

```r
library(dplyr)
cap_color=mushrooms %>%
  group_by(cap.color) %>%
  summarise(count=n())
View(cap_color)
```

Ustvarite vafeljni graf z ustvarjanjem oznak in nato razvrščanjem svojih podatkov:

```r
library(waffle)
names(cap_color$count) = paste0(cap_color$cap.color)
waffle((cap_color$count/10), rows = 7, title = "Waffle Chart")+scale_fill_manual(values=c("brown", "#F0DC82", "#D2691E", "green", 
                                                                                     "pink", "purple", "red", "grey", 
                                                                                     "yellow","white"))
```

Z uporabo vafeljnega grafa lahko jasno vidite deleže barv klobukov v tem naboru podatkov o gobah. Zanimivo je, da je veliko gob z zelenimi klobuki!

![vafeljni graf](../../../../../translated_images/sl/waffle.aaa75c5337735a6ef32ace0ffb6506ef49e5aefe870ffd72b1bb080f4843c217.png)

V tej lekciji ste se naučili treh načinov vizualizacije deležev. Najprej morate razvrstiti svoje podatke v kategorije in nato odločiti, kateri je najboljši način za prikaz podatkov - torta, krof ali vafelj. Vsi so okusni in uporabniku takoj ponudijo vpogled v nabor podatkov.

## 🚀 Izziv

Poskusite ponovno ustvariti te okusne grafe v [Charticulator](https://charticulator.com).
## [Po-lekcijski kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## Pregled in samostojno učenje

Včasih ni očitno, kdaj uporabiti tortni, krofni ali vafeljni graf. Tukaj je nekaj člankov za branje na to temo:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Raziskujte, da bi našli več informacij o tej težki odločitvi.
## Naloga

[Poskusite v Excelu](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.