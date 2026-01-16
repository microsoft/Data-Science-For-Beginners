<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-26T17:09:49+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "sk"
}
-->
# Vizualizácia množstiev
|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Vizualizácia množstiev - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

V tejto lekcii preskúmate, ako používať niektoré z mnohých dostupných knižníc balíkov R na vytváranie zaujímavých vizualizácií založených na koncepte množstva. Pomocou vyčisteného datasetu o vtákoch z Minnesoty sa môžete dozvedieť veľa zaujímavých faktov o miestnej faune.

## [Kvíz pred prednáškou](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## Pozorovanie rozpätia krídel s ggplot2
Vynikajúcou knižnicou na vytváranie jednoduchých aj sofistikovaných grafov a diagramov rôznych typov je [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html). Vo všeobecnosti proces vytvárania grafov pomocou týchto knižníc zahŕňa identifikáciu častí vášho dataframe, ktoré chcete zacieliť, vykonanie potrebných transformácií na tieto údaje, priradenie hodnôt osi x a y, rozhodnutie o type grafu a následné zobrazenie grafu.

`ggplot2` je systém na deklaratívne vytváranie grafiky, založený na Gramatike grafov. [Gramatika grafov](https://en.wikipedia.org/wiki/Ggplot2) je všeobecná schéma pre vizualizáciu údajov, ktorá rozdeľuje grafy na semantické komponenty, ako sú škály a vrstvy. Inými slovami, jednoduchosť vytvárania grafov pre jednorozmerné alebo viacrozmerné údaje s minimálnym kódom robí z `ggplot2` najpopulárnejší balík používaný na vizualizácie v R. Používateľ určuje, ako mapovať premenné na estetiku, grafické prvky, a `ggplot2` sa postará o zvyšok.

> ✅ Graf = Údaje + Estetika + Geometria
> - Údaje sa týkajú datasetu
> - Estetika označuje premenné, ktoré sa majú skúmať (premenné x a y)
> - Geometria označuje typ grafu (čiarový graf, stĺpcový graf, atď.)

Vyberte najlepšiu geometriu (typ grafu) podľa vašich údajov a príbehu, ktorý chcete grafom vyrozprávať.

> - Na analýzu trendov: čiarový, stĺpcový
> - Na porovnanie hodnôt: stĺpcový, koláčový, bodový graf
> - Na zobrazenie vzťahu častí k celku: koláčový
> - Na zobrazenie distribúcie údajov: bodový graf, stĺpcový
> - Na zobrazenie vzťahov medzi hodnotami: čiarový, bodový graf, bublinový

✅ Môžete si tiež pozrieť tento popisný [cheatsheet](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf) pre ggplot2.

## Vytvorenie čiarového grafu o hodnotách rozpätia krídel vtákov

Otvorte konzolu R a importujte dataset.  
> Poznámka: Dataset je uložený v koreňovom adresári tohto repozitára v priečinku `/data`.

Importujme dataset a pozrime sa na jeho hlavičku (prvých 5 riadkov).

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```
Hlavička datasetu obsahuje mix textu a čísel:

|      | Názov                        | Vedecký názov          | Kategória             | Rád          | Čeľaď    | Rod         | Stav ochrany         | MinDĺžka | MaxDĺžka | MinHmotnosť | MaxHmotnosť | MinRozpätie | MaxRozpätie |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :------------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Čiernobruchá pískajúca kačica | Dendrocygna autumnalis | Kačice/Husi/Vodné vtáky | Anseriformes | Anatidae | Dendrocygna | LC                   |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Hnedá pískajúca kačica        | Dendrocygna bicolor    | Kačice/Husi/Vodné vtáky | Anseriformes | Anatidae | Dendrocygna | LC                   |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snežná hus                   | Anser caerulescens     | Kačice/Husi/Vodné vtáky | Anseriformes | Anatidae | Anser       | LC                   |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Rossova hus                  | Anser rossii           | Kačice/Husi/Vodné vtáky | Anseriformes | Anatidae | Anser       | LC                   |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Veľká bieločelá hus          | Anser albifrons        | Kačice/Husi/Vodné vtáky | Anseriformes | Anatidae | Anser       | LC                   |        64 |        81 |        1930 |        3310 |         130 |         165 |

Začnime vykresľovaním niektorých číselných údajov pomocou základného čiarového grafu. Predpokladajme, že chcete zobraziť maximálne rozpätie krídel týchto zaujímavých vtákov.

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```
Tu nainštalujete balík `ggplot2` a potom ho importujete do pracovného priestoru pomocou príkazu `library("ggplot2")`. Na vykreslenie akéhokoľvek grafu v ggplot sa používa funkcia `ggplot()` a špecifikujete dataset, premenné x a y ako atribúty. V tomto prípade používame funkciu `geom_line()`, pretože chceme vykresliť čiarový graf.

![MaxRozpätie-čiarový graf](../../../../../translated_images/sk/MaxWingspan-lineplot.b12169f99d26fdd263f291008dfd73c18a4ba8f3d32b1fda3d74af51a0a28616.png)

Čo si všimnete okamžite? Zdá sa, že existuje aspoň jeden extrémny údaj - to je poriadne rozpätie krídel! Rozpätie krídel viac ako 2000 centimetrov znamená viac ako 20 metrov - potulujú sa v Minnesote pterodaktyly? Poďme to preskúmať.

Aj keď by ste mohli rýchlo zoradiť údaje v Exceli, aby ste našli tieto extrémne hodnoty, ktoré sú pravdepodobne preklepy, pokračujte vo vizualizačnom procese priamo z grafu.

Pridajte štítky na os x, aby ste ukázali, o aké vtáky ide:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```
Špecifikujeme uhol v `theme` a špecifikujeme štítky osí x a y v `xlab()` a `ylab()` respektíve. Funkcia `ggtitle()` dáva grafu názov.

![MaxRozpätie-čiarový graf-vylepšený](../../../../../translated_images/sk/MaxWingspan-lineplot-improved.04b73b4d5a59552a6bc7590678899718e1f065abe9eada9ebb4148939b622fd4.png)

Aj s rotáciou štítkov nastavenou na 45 stupňov je ich príliš veľa na čítanie. Skúsme inú stratégiu: označme iba tie extrémne hodnoty a nastavme štítky priamo v grafe. Môžete použiť bodový graf, aby ste získali viac priestoru na označovanie:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```
Čo sa tu deje? Použili ste funkciu `geom_point()` na vykreslenie bodov. S týmto ste pridali štítky pre vtáky, ktoré mali `MaxRozpätie > 500`, a tiež skryli štítky na osi x, aby ste graf vyčistili.

Čo objavíte?

![MaxRozpätie-bodový graf](../../../../../translated_images/sk/MaxWingspan-scatterplot.60dc9e0e19d32700283558f253841fdab5104abb62bc96f7d97f9c0ee857fa8b.png)

## Filtrovanie údajov

Orol skalný a sokol prériový, aj keď sú pravdepodobne veľmi veľké vtáky, sa zdajú byť nesprávne označené, s pridanou nulou k ich maximálnemu rozpätí krídel. Je nepravdepodobné, že by ste stretli orla skalného s rozpätím krídel 25 metrov, ale ak áno, dajte nám vedieť! Vytvorme nový dataframe bez týchto dvoch extrémnych hodnôt:

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
Vytvorili sme nový dataframe `birds_filtered` a potom vykreslili bodový graf. Filtrovaním extrémnych hodnôt sú vaše údaje teraz súdržnejšie a zrozumiteľnejšie.

![MaxRozpätie-bodový graf-vylepšený](../../../../../translated_images/sk/MaxWingspan-scatterplot-improved.7d0af81658c65f3e75b8fedeb2335399e31108257e48db15d875ece608272051.png)

Teraz, keď máme čistejší dataset aspoň z hľadiska rozpätia krídel, poďme objaviť viac o týchto vtákoch.

Aj keď čiarové a bodové grafy môžu zobrazovať informácie o hodnotách údajov a ich distribúciách, chceme premýšľať o hodnotách inherentných v tomto datasete. Mohli by ste vytvoriť vizualizácie na zodpovedanie nasledujúcich otázok o množstve:

> Koľko kategórií vtákov existuje a aké sú ich počty?  
> Koľko vtákov je vyhynutých, ohrozených, vzácnych alebo bežných?  
> Koľko je rôznych rodov a rádov podľa Linnaeusovej terminológie?  

## Preskúmajte stĺpcové grafy

Stĺpcové grafy sú praktické, keď potrebujete zobraziť skupiny údajov. Preskúmajme kategórie vtákov, ktoré existujú v tomto datasete, aby sme zistili, ktorá je najbežnejšia podľa počtu.  
Vytvorme stĺpcový graf na filtrovaných údajoch.

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
V nasledujúcom úryvku inštalujeme balíky [dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8) a [lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0), ktoré pomáhajú manipulovať a zoskupovať údaje na vykreslenie zoskupeného stĺpcového grafu. Najprv zoskupíte údaje podľa `Category` vtákov a potom sumarizujete stĺpce `MinLength`, `MaxLength`, `MinBodyMass`, `MaxBodyMass`, `MinWingspan`, `MaxWingspan`. Potom vykreslíte stĺpcový graf pomocou balíka `ggplot2` a špecifikujete farby pre rôzne kategórie a štítky.

![Zoskupený stĺpcový graf](../../../../../translated_images/sk/stacked-bar-chart.0c92264e89da7b391a7490224d1e7059a020e8b74dcd354414aeac78871c02f1.png)

Tento stĺpcový graf je však nečitateľný, pretože obsahuje príliš veľa nezoskupených údajov. Musíte vybrať iba údaje, ktoré chcete vykresliť, takže sa pozrime na dĺžku vtákov podľa ich kategórie.

Filtrovanie údajov na zahrnutie iba kategórie vtákov.

Keďže existuje veľa kategórií, môžete tento graf zobraziť vertikálne a upraviť jeho výšku, aby sa zobrazili všetky údaje:

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```
Najprv spočítate unikátne hodnoty v stĺpci `Category` a potom ich zoradíte do nového dataframe `birds_count`. Tieto zoradené údaje sú potom faktorizované na rovnakej úrovni, aby boli vykreslené v zoradenom poradí. Pomocou `ggplot2` potom vykreslíte údaje v stĺpcovom grafe. Funkcia `coord_flip()` vykreslí horizontálne stĺpce.

![kategória-dĺžka](../../../../../translated_images/sk/category-length.7e34c296690e85d64f7e4d25a56077442683eca96c4f5b4eae120a64c0755636.png)

Tento stĺpcový graf poskytuje dobrý prehľad o počte vtákov v každej kategórii. Na prvý pohľad vidíte, že najväčší počet vtákov v tomto regióne patrí do kategórie Kačice/Husi/Vodné vtáky. Minnesota je "krajina 10 000 jazier", takže to nie je prekvapujúce!

✅ Skúste niektoré ďalšie počty v tomto datasete. Prekvapí vás niečo?

## Porovnávanie údajov

Môžete skúsiť rôzne porovnania zoskupených údajov vytvorením nových osí. Skúste porovnanie MaxDĺžky vtákov podľa ich kategórie:

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
Zoskupíme údaje `birds_filtered` podľa `Category` a potom vykreslíme stĺpcový graf.

![porovnávanie údajov](../../../../../translated_images/sk/comparingdata.f486a450d61c7ca5416f27f3f55a6a4465d00df3be5e6d33936e9b07b95e2fdd.png)

Tu nie je nič prekvapujúce: kolibríky majú najmenšiu MaxDĺžku v porovnaní s pelikánmi alebo husami. Je dobré, keď údaje dávajú logický zmysel!

Môžete vytvoriť zaujímavejšie vizualizácie stĺpcových grafov prekrytím údajov. Prekryme Minimálnu a Maximálnu Dĺžku na danej kategórii vtákov:

```r
ggplot(data=birds_grouped, aes(x=Category)) +
  geom_bar(aes(y=MaxLength), stat="identity", position ="identity",  fill='blue') +
  geom_bar(aes(y=MinLength), stat="identity", position="identity", fill='orange')+
  coord_flip()
```
![prekryté hodnoty](../../../../../translated_images/sk/superimposed-values.5363f0705a1da4167625a373a1064331ea3cb7a06a297297d0734fcc9b3819a0.png)

## 🚀 Výzva

Tento dataset o vtákoch ponúka množstvo informácií o rôznych typoch vtákov v konkrétnom ekosystéme. Vyhľadajte na internete a zistite, či nájdete iné datasety orientované na vtáky. Precvičte si vytváranie grafov a diagramov o týchto vtákoch, aby ste objavili fakty, ktoré ste si neuvedomovali.

## [Kvíz po prednáške](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## Prehľad a samostatné štúdium

Táto prvá lekcia vám poskytla informácie o tom, ako používať `ggplot2` na vizualizáciu množstiev. Urobte si výskum o iných spôsoboch práce s datasetmi na vizualizáciu. Vyhľadajte a preskúmajte datasety, ktoré by ste mohli vizualizovať pomocou iných balíkov, ako sú [Lattice](https://stat.ethz.ch/R-manual/R-devel/library/lattice/html/Lattice.html) a [Plotly](https://github.com/plotly/plotly.R#readme).

## Zadanie
[Čiary, body a stĺpce](assignment.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.