<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "47028abaaafa2bcb1079702d20569066",
  "translation_date": "2025-08-26T17:20:18+00:00",
  "source_file": "3-Data-Visualization/R/11-visualization-proportions/README.md",
  "language_code": "sk"
}
-->
# Vizualizácia proporcií

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Vizualizácia proporcií - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

V tejto lekcii použijete dataset zameraný na prírodu na vizualizáciu proporcií, napríklad koľko rôznych druhov húb sa nachádza v danom datasete o hubách. Poďme preskúmať tieto fascinujúce huby pomocou datasetu pochádzajúceho z Audubon, ktorý obsahuje podrobnosti o 23 druhoch húb s lupeňmi z rodov Agaricus a Lepiota. Budete experimentovať s chutnými vizualizáciami, ako sú:

- Koláčové grafy 🥧
- Donutové grafy 🍩
- Waflové grafy 🧇

> 💡 Veľmi zaujímavý projekt s názvom [Charticulator](https://charticulator.com) od Microsoft Research ponúka bezplatné rozhranie na tvorbu vizualizácií pomocou drag and drop. V jednom z ich tutoriálov tiež používajú tento dataset o hubách! Takže môžete preskúmať dáta a zároveň sa naučiť používať túto knižnicu: [Charticulator tutorial](https://charticulator.com/tutorials/tutorial4.html).

## [Kvíz pred lekciou](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## Spoznajte svoje huby 🍄

Huby sú veľmi zaujímavé. Importujme dataset, aby sme ich mohli študovať:

```r
mushrooms = read.csv('../../data/mushrooms.csv')
head(mushrooms)
```
Tabuľka sa zobrazí s niekoľkými skvelými údajmi na analýzu:


| trieda     | tvar klobúka | povrch klobúka | farba klobúka | modriny | vôňa    | pripojenie lupeňov | rozostup lupeňov | veľkosť lupeňov | farba lupeňov | tvar hlúbika | koreň hlúbika | povrch nad prsteňom | povrch pod prsteňom | farba nad prsteňom | farba pod prsteňom | typ závoja | farba závoja | počet prsteňov | typ prsteňa | farba výtrusov | populácia | biotop |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Jedovatá | Konvexný    | Hladký      | Hnedý     | Modriny | Štipľavá | Voľné            | Tesné        | Úzke    | Čierna      | Rozširujúci   | Rovný      | Hladký                   | Hladký                   | Biela                  | Biela                  | Čiastočný   | Biela      | Jeden         | Visutý   | Čierna             | Roztrúsená  | Mestský   |
| Jedlá    | Konvexný    | Hladký      | Žltý    | Modriny | Mandľová  | Voľné            | Tesné        | Široké     | Čierna      | Rozširujúci   | Kyjakovitý       | Hladký                   | Hladký                   | Biela                  | Biela                  | Čiastočný   | Biela      | Jeden         | Visutý   | Hnedá             | Početná   | Trávnaté |
| Jedlá    | Zvonovitý      | Hladký      | Biela     | Modriny | Anízová   | Voľné            | Tesné        | Široké     | Hnedá      | Rozširujúci   | Kyjakovitý       | Hladký                   | Hladký                   | Biela                  | Biela                  | Čiastočný   | Biela      | Jeden         | Visutý   | Hnedá             | Početná   | Lúky |
| Jedovatá | Konvexný    | Šupinatý       | Biela     | Modriny | Štipľavá | Voľné            | Tesné        | Úzke    | Hnedá      | Rozširujúci   | Rovný      | Hladký                   | Hladký                   | Biela                  | Biela                  | Čiastočný   | Biela      | Jeden         | Visutý   | Čierna             | Roztrúsená  | Mestský 
| Jedlá | Konvexný       |Hladký       | Zelený     | Bez modrín| Žiadna   |Voľné            | Preplnené       | Široké     | Čierna      | Zužujúci   | Rovný      |  Hladký | Hladký                    | Biela                 | Biela                  | Čiastočný    | Biela     | Jeden         | Pominuteľný | Hnedá             | Hojná | Trávnaté
|Jedlá  |  Konvexný      | Šupinatý   | Žltý         | Modriny  | Mandľová  | Voľné | Tesné  |   Široké   |   Hnedá  | Rozširujúci   |   Kyjakovitý                      | Hladký                  | Hladký    | Biela                 |  Biela                | Čiastočný      | Biela    |  Jeden  |  Visutý | Čierna   | Početná | Trávnaté
      
Hneď si všimnete, že všetky údaje sú textové. Budete ich musieť konvertovať, aby ste ich mohli použiť v grafe. Väčšina údajov je v skutočnosti reprezentovaná ako objekt:

```r
names(mushrooms)
```

Výstup je:

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
Vezmite tieto údaje a konvertujte stĺpec 'trieda' na kategóriu:

```r
library(dplyr)
grouped=mushrooms %>%
  group_by(class) %>%
  summarise(count=n())
```


Teraz, ak vytlačíte údaje o hubách, uvidíte, že boli rozdelené do kategórií podľa triedy jedovaté/jedlé:
```r
View(grouped)
```


| trieda | počet |
| --------- | --------- |
| Jedlá | 4208 |
| Jedovatá| 3916 |



Ak budete postupovať podľa poradia uvedeného v tejto tabuľke na vytvorenie kategórií tried, môžete vytvoriť koláčový graf. 

## Koláč!

```r
pie(grouped$count,grouped$class, main="Edible?")
```
Voila, koláčový graf zobrazujúci proporcie týchto údajov podľa dvoch tried húb. Je veľmi dôležité správne zoradiť poradie štítkov, najmä tu, preto si overte poradie, v akom je pole štítkov vytvorené!

![koláčový graf](../../../../../translated_images/sk/pie1-wb.685df063673751f4b0b82127f7a52c7f9a920192f22ae61ad28412ba9ace97bf.png)

## Donuty!

O niečo vizuálne zaujímavejší koláčový graf je donutový graf, čo je koláčový graf s dierou v strede. Pozrime sa na naše údaje pomocou tejto metódy.

Pozrite sa na rôzne biotopy, kde huby rastú:

```r
library(dplyr)
habitat=mushrooms %>%
  group_by(habitat) %>%
  summarise(count=n())
View(habitat)
```
Výstup je:
| biotop| počet |
| --------- | --------- |
| Trávnaté    | 2148 |
| Listy| 832 |
| Lúky    | 292 |
| Cesty| 1144 |
| Mestský    | 368 |
| Odpad| 192 |
| Lesy| 3148 |


Tu zoskupujete svoje údaje podľa biotopu. Je ich uvedených 7, takže ich použite ako štítky pre váš donutový graf:

```r
library(ggplot2)
library(webr)
PieDonut(habitat, aes(habitat, count=count))
```

![donutový graf](../../../../../translated_images/sk/donut-wb.34e6fb275da9d834c2205145e39a3de9b6878191dcdba6f7a9e85f4b520449bc.png)

Tento kód používa dve knižnice - ggplot2 a webr. Pomocou funkcie PieDonut z knižnice webr môžeme ľahko vytvoriť donutový graf!

Donutové grafy v R je možné vytvoriť aj pomocou samotnej knižnice ggplot2. Viac sa o tom môžete dozvedieť [tu](https://www.r-graph-gallery.com/128-ring-or-donut-plot.html) a vyskúšať si to sami.

Teraz, keď viete, ako zoskupiť svoje údaje a potom ich zobraziť ako koláč alebo donut, môžete preskúmať iné typy grafov. Skúste waflový graf, ktorý je len iným spôsobom skúmania kvantity.
## Wafle!

Graf typu 'waffle' je iný spôsob vizualizácie kvantít ako 2D pole štvorcov. Skúste vizualizovať rôzne kvantity farieb klobúkov húb v tomto datasete. Na to potrebujete nainštalovať pomocnú knižnicu s názvom [waffle](https://cran.r-project.org/web/packages/waffle/waffle.pdf) a použiť ju na vytvorenie svojej vizualizácie:

```r
install.packages("waffle", repos = "https://cinc.rud.is")
```

Vyberte segment svojich údajov na zoskupenie:

```r
library(dplyr)
cap_color=mushrooms %>%
  group_by(cap.color) %>%
  summarise(count=n())
View(cap_color)
```

Vytvorte waflový graf vytvorením štítkov a následným zoskupením údajov:

```r
library(waffle)
names(cap_color$count) = paste0(cap_color$cap.color)
waffle((cap_color$count/10), rows = 7, title = "Waffle Chart")+scale_fill_manual(values=c("brown", "#F0DC82", "#D2691E", "green", 
                                                                                     "pink", "purple", "red", "grey", 
                                                                                     "yellow","white"))
```

Pomocou waflového grafu môžete jasne vidieť proporcie farieb klobúkov v tomto datasete húb. Zaujímavé je, že existuje veľa húb so zelenými klobúkmi!

![waflový graf](../../../../../translated_images/sk/waffle.aaa75c5337735a6ef32ace0ffb6506ef49e5aefe870ffd72b1bb080f4843c217.png)

V tejto lekcii ste sa naučili tri spôsoby vizualizácie proporcií. Najprv musíte zoskupiť svoje údaje do kategórií a potom sa rozhodnúť, ktorý spôsob zobrazenia údajov je najlepší - koláč, donut alebo waffle. Všetky sú chutné a poskytujú používateľovi okamžitý prehľad o datasete.

## 🚀 Výzva

Skúste tieto chutné grafy vytvoriť v [Charticulator](https://charticulator.com).
## [Kvíz po lekcii](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## Prehľad a samoštúdium

Niekedy nie je zrejmé, kedy použiť koláčový, donutový alebo waflový graf. Tu je niekoľko článkov na túto tému:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Urobte si výskum, aby ste našli viac informácií o tomto náročnom rozhodovaní.
## Zadanie

[Skúste to v Exceli](assignment.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.