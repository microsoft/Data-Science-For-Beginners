<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "47028abaaafa2bcb1079702d20569066",
  "translation_date": "2025-08-30T18:40:34+00:00",
  "source_file": "3-Data-Visualization/R/11-visualization-proportions/README.md",
  "language_code": "hr"
}
-->
# Vizualizacija proporcija

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Vizualizacija proporcija - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

U ovoj lekciji koristit ćete drugačiji dataset fokusiran na prirodu kako biste vizualizirali proporcije, poput broja različitih vrsta gljiva u datasetu o gljivama. Istražimo ove fascinantne gljive koristeći dataset preuzet od Audubona koji sadrži detalje o 23 vrste gljiva s listićima iz obitelji Agaricus i Lepiota. Eksperimentirat ćete s ukusnim vizualizacijama poput:

- Tortnih grafikona 🥧
- Grafičkih prikaza u obliku prstena 🍩
- Grafičkih prikaza u obliku vafla 🧇

> 💡 Vrlo zanimljiv projekt pod nazivom [Charticulator](https://charticulator.com) od Microsoft Researcha nudi besplatno sučelje za vizualizaciju podataka putem povlačenja i ispuštanja. U jednom od njihovih tutorijala također koriste ovaj dataset o gljivama! Tako možete istražiti podatke i istovremeno naučiti koristiti biblioteku: [Charticulator tutorial](https://charticulator.com/tutorials/tutorial4.html).

## [Kviz prije predavanja](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## Upoznajte svoje gljive 🍄

Gljive su vrlo zanimljive. Uvezimo dataset kako bismo ih proučili:

```r
mushrooms = read.csv('../../data/mushrooms.csv')
head(mushrooms)
```
Ispisuje se tablica s odličnim podacima za analizu:


| klasa     | oblik klobuka | površina klobuka | boja klobuka | modrice | miris    | pričvršćenje listića | razmak listića | veličina listića | boja listića | oblik stručka | korijen stručka | površina iznad prstena | površina ispod prstena | boja iznad prstena | boja ispod prstena | vrsta vela | boja vela | broj prstena | vrsta prstena | boja spora | populacija | stanište |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Otrovna | Konveksna    | Glatka      | Smeđa     | Modrice | Oštar miris | Slobodni            | Blizu        | Uski    | Crna      | Širi se   | Jednaka      | Glatka                   | Glatka                   | Bijela                  | Bijela                  | Djelomični   | Bijela      | Jedan         | Viseći   | Crna             | Raspršena  | Urbano   |
| Jestiva    | Konveksna    | Glatka      | Žuta    | Modrice | Badem  | Slobodni            | Blizu        | Široki     | Crna      | Širi se   | Klub       | Glatka                   | Glatka                   | Bijela                  | Bijela                  | Djelomični   | Bijela      | Jedan         | Viseći   | Smeđa             | Brojna   | Trava |
| Jestiva    | Zvono      | Glatka      | Bijela     | Modrice | Anis   | Slobodni            | Blizu        | Široki     | Smeđa      | Širi se   | Klub       | Glatka                   | Glatka                   | Bijela                  | Bijela                  | Djelomični   | Bijela      | Jedan         | Viseći   | Smeđa             | Brojna   | Livade |
| Otrovna | Konveksna    | Ljuskava       | Bijela     | Modrice | Oštar miris | Slobodni            | Blizu        | Uski    | Smeđa      | Širi se   | Jednaka      | Glatka                   | Glatka                   | Bijela                  | Bijela                  | Djelomični   | Bijela      | Jedan         | Viseći   | Crna             | Raspršena  | Urbano 
| Jestiva | Konveksna       |Glatka       | Zelena     | Bez modrica| Bez mirisa   |Slobodni            | Zbijeni       | Široki     | Crna      | Sužava se   | Jednaka      |  Glatka | Glatka                    | Bijela                 | Bijela                  | Djelomični    | Bijela     | Jedan         | Nestajući | Smeđa             | Obilna | Trava
|Jestiva  |  Konveksna      | Ljuskava   | Žuta         | Modrice  | Badem  | Slobodni | Blizu  |   Široki   |   Smeđa  | Širi se   |   Klub                      | Glatka                  | Glatka    | Bijela                 |  Bijela                | Djelomični      | Bijela    |  Jedan  |  Viseći | Crna   | Brojna | Trava
      
Odmah primjećujete da su svi podaci tekstualni. Morat ćete ih konvertirati kako biste ih mogli koristiti u grafičkom prikazu. Većina podataka, zapravo, predstavljena je kao objekt:

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
Uzmite ove podatke i konvertirajte stupac 'klasa' u kategoriju:

```r
library(dplyr)
grouped=mushrooms %>%
  group_by(class) %>%
  summarise(count=n())
```


Sada, ako ispišete podatke o gljivama, možete vidjeti da su grupirani u kategorije prema klasi otrovno/jestivo:
```r
View(grouped)
```


| klasa | broj |
| --------- | --------- |
| Jestiva | 4208 |
| Otrovna| 3916 |



Ako slijedite redoslijed prikazan u ovoj tablici za kreiranje oznaka kategorija klase, možete izraditi tortni grafikon. 

## Torta!

```r
pie(grouped$count,grouped$class, main="Edible?")
```
Voila, tortni grafikon koji prikazuje proporcije ovih podataka prema ove dvije klase gljiva. Vrlo je važno dobiti redoslijed oznaka točno, posebno ovdje, pa svakako provjerite redoslijed kojim je niz oznaka izgrađen!

![tortni grafikon](../../../../../translated_images/hr/pie1-wb.685df063673751f4b0b82127f7a52c7f9a920192f22ae61ad28412ba9ace97bf.png)

## Prstenovi!

Vizualno zanimljiviji tortni grafikon je grafikon u obliku prstena, koji je tortni grafikon s rupom u sredini. Pogledajmo naše podatke koristeći ovu metodu.

Pogledajte različita staništa u kojima gljive rastu:

```r
library(dplyr)
habitat=mushrooms %>%
  group_by(habitat) %>%
  summarise(count=n())
View(habitat)
```
Rezultat je:
| stanište| broj |
| --------- | --------- |
| Trava    | 2148 |
| Lišće| 832 |
| Livade    | 292 |
| Staze| 1144 |
| Urbano    | 368 |
| Otpad| 192 |
| Drvo| 3148 |


Ovdje grupirate svoje podatke prema staništu. Ima ih 7 navedenih, pa ih koristite kao oznake za grafikon u obliku prstena:

```r
library(ggplot2)
library(webr)
PieDonut(habitat, aes(habitat, count=count))
```

![grafikon u obliku prstena](../../../../../translated_images/hr/donut-wb.34e6fb275da9d834c2205145e39a3de9b6878191dcdba6f7a9e85f4b520449bc.png)

Ovaj kod koristi dvije biblioteke - ggplot2 i webr. Koristeći funkciju PieDonut iz webr biblioteke, lako možemo kreirati grafikon u obliku prstena!

Grafikoni u obliku prstena u R-u mogu se izraditi koristeći samo ggplot2 biblioteku. Više o tome možete naučiti [ovdje](https://www.r-graph-gallery.com/128-ring-or-donut-plot.html) i isprobati sami.

Sada kada znate kako grupirati svoje podatke i prikazati ih kao tortu ili prsten, možete istražiti druge vrste grafikona. Isprobajte grafikon u obliku vafla, koji je samo drugačiji način istraživanja količine.
## Vafli!

Grafikon tipa 'vafla' je drugačiji način vizualizacije količina kao 2D niz kvadrata. Pokušajte vizualizirati različite količine boja klobuka gljiva u ovom datasetu. Da biste to učinili, trebate instalirati pomoćnu biblioteku pod nazivom [waffle](https://cran.r-project.org/web/packages/waffle/waffle.pdf) i koristiti je za generiranje svoje vizualizacije:

```r
install.packages("waffle", repos = "https://cinc.rud.is")
```

Odaberite segment svojih podataka za grupiranje:

```r
library(dplyr)
cap_color=mushrooms %>%
  group_by(cap.color) %>%
  summarise(count=n())
View(cap_color)
```

Izradite grafikon u obliku vafla kreiranjem oznaka i zatim grupiranjem svojih podataka:

```r
library(waffle)
names(cap_color$count) = paste0(cap_color$cap.color)
waffle((cap_color$count/10), rows = 7, title = "Waffle Chart")+scale_fill_manual(values=c("brown", "#F0DC82", "#D2691E", "green", 
                                                                                     "pink", "purple", "red", "grey", 
                                                                                     "yellow","white"))
```

Koristeći grafikon u obliku vafla, jasno možete vidjeti proporcije boja klobuka u ovom datasetu gljiva. Zanimljivo je da postoji mnogo gljiva sa zelenim klobukom!

![grafikon u obliku vafla](../../../../../translated_images/hr/waffle.aaa75c5337735a6ef32ace0ffb6506ef49e5aefe870ffd72b1bb080f4843c217.png)

U ovoj lekciji naučili ste tri načina za vizualizaciju proporcija. Prvo, trebate grupirati svoje podatke u kategorije, a zatim odlučiti koji je najbolji način za prikaz podataka - torta, prsten ili vafl. Svi su ukusni i pružaju korisniku trenutni pregled dataset-a.

## 🚀 Izazov

Pokušajte ponovno kreirati ove ukusne grafikone u [Charticulator](https://charticulator.com).
## [Kviz nakon predavanja](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## Pregled i samostalno učenje

Ponekad nije očito kada koristiti tortu, prsten ili vafl grafikon. Evo nekoliko članaka za čitanje na ovu temu:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Provedite istraživanje kako biste pronašli više informacija o ovoj odluci.

## Zadatak

[Pokušajte u Excelu](assignment.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.