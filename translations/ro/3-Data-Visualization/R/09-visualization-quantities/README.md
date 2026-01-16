<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-26T17:10:28+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "ro"
}
-->
# Vizualizarea Cantităților
|![ Sketchnote de [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Vizualizarea Cantităților - _Sketchnote de [@nitya](https://twitter.com/nitya)_ |

În această lecție vei explora cum să folosești unele dintre numeroasele biblioteci disponibile în pachetele R pentru a învăța să creezi vizualizări interesante în jurul conceptului de cantitate. Folosind un set de date curățat despre păsările din Minnesota, poți descoperi multe informații interesante despre fauna locală.  
## [Chestionar înainte de lecție](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## Observă anvergura aripilor cu ggplot2
O bibliotecă excelentă pentru crearea atât a graficelor simple, cât și a celor sofisticate este [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html). În termeni generali, procesul de realizare a graficelor folosind aceste biblioteci include identificarea părților din cadrul de date pe care vrei să le analizezi, efectuarea transformărilor necesare asupra datelor, atribuirea valorilor pentru axele x și y, alegerea tipului de grafic și apoi afișarea graficului.

`ggplot2` este un sistem pentru crearea graficelor în mod declarativ, bazat pe Gramatica Graficelor. [Gramatica Graficelor](https://en.wikipedia.org/wiki/Ggplot2) este o schemă generală pentru vizualizarea datelor care împarte graficele în componente semantice, cum ar fi scalele și straturile. Cu alte cuvinte, ușurința de a crea grafice pentru date univariate sau multivariate cu puțin cod face ca `ggplot2` să fie cel mai popular pachet utilizat pentru vizualizări în R. Utilizatorul spune `ggplot2` cum să mapese variabilele la estetici, ce primitive grafice să folosească, iar `ggplot2` se ocupă de restul.

> ✅ Grafic = Date + Estetici + Geometrie  
> - Datele se referă la setul de date  
> - Esteticile indică variabilele care urmează să fie studiate (variabilele x și y)  
> - Geometria se referă la tipul de grafic (grafic liniar, grafic cu bare etc.)  

Alege cea mai bună geometrie (tip de grafic) în funcție de datele tale și povestea pe care vrei să o spui prin grafic.  

> - Pentru a analiza tendințele: linie, coloană  
> - Pentru a compara valori: bare, coloană, plăcintă, scatterplot  
> - Pentru a arăta cum părțile se raportează la întreg: plăcintă  
> - Pentru a arăta distribuția datelor: scatterplot, bare  
> - Pentru a arăta relațiile dintre valori: linie, scatterplot, bubble  

✅ Poți consulta și acest [cheatsheet descriptiv](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf) pentru ggplot2.

## Construiește un grafic liniar despre valorile anvergurii aripilor păsărilor

Deschide consola R și importă setul de date.  
> Notă: Setul de date este stocat în rădăcina acestui repo în folderul `/data`.

Să importăm setul de date și să observăm primele 5 rânduri ale datelor.

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```  
Primele rânduri ale datelor conțin un amestec de text și numere:

|      | Nume                         | NumeȘtiințific         | Categorie              | Ordin        | Familie   | Genus       | StatusConservare | LungimeMin | LungimeMax | MasăCorpMin | MasăCorpMax | AnvergurăMin | AnvergurăMax |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Rața fluierătoare cu burtă neagră | Dendrocygna autumnalis | Rațe/Gâște/Păsări acvatice | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Rața fluierătoare fulvoasă       | Dendrocygna bicolor    | Rațe/Gâște/Păsări acvatice | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Gâsca de zăpadă                   | Anser caerulescens     | Rațe/Gâște/Păsări acvatice | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Gâsca lui Ross                 | Anser rossii           | Rațe/Gâște/Păsări acvatice | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Gâsca albă cu frunte mare  | Anser albifrons        | Rațe/Gâște/Păsări acvatice | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Să începem prin a reprezenta grafic unele dintre datele numerice folosind un grafic liniar de bază. Să presupunem că vrei să vezi anvergura maximă a aripilor acestor păsări interesante.

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```  
Aici, instalezi pachetul `ggplot2` și apoi îl importi în spațiul de lucru folosind comanda `library("ggplot2")`. Pentru a crea orice grafic în ggplot, se folosește funcția `ggplot()` și specifici setul de date, variabilele x și y ca atribute. În acest caz, folosim funcția `geom_line()` deoarece dorim să creăm un grafic liniar.

![MaxWingspan-lineplot](../../../../../translated_images/ro/MaxWingspan-lineplot.b12169f99d26fdd263f291008dfd73c18a4ba8f3d32b1fda3d74af51a0a28616.png)

Ce observi imediat? Pare să existe cel puțin un outlier - ce anvergură impresionantă! O anvergură de peste 2000 de centimetri înseamnă mai mult de 20 de metri - sunt Pterodactili care zboară prin Minnesota? Să investigăm.

Deși ai putea face o sortare rapidă în Excel pentru a găsi acești outlieri, care sunt probabil erori de tipar, continuă procesul de vizualizare lucrând direct din grafic.

Adaugă etichete pe axa x pentru a arăta ce tip de păsări sunt în discuție:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```  
Specificăm unghiul în `theme` și specificăm etichetele axelor x și y în `xlab()` și `ylab()` respectiv. Funcția `ggtitle()` oferă un nume graficului.

![MaxWingspan-lineplot-improved](../../../../../translated_images/ro/MaxWingspan-lineplot-improved.04b73b4d5a59552a6bc7590678899718e1f065abe9eada9ebb4148939b622fd4.png)

Chiar și cu rotația etichetelor setată la 45 de grade, sunt prea multe pentru a fi citite. Să încercăm o strategie diferită: etichetează doar outlierii și setează etichetele în interiorul graficului. Poți folosi un grafic scatter pentru a face mai mult loc etichetării:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```  
Ce se întâmplă aici? Ai folosit funcția `geom_point()` pentru a reprezenta puncte scatter. Cu aceasta, ai adăugat etichete pentru păsările care au `MaxWingspan > 500` și ai ascuns etichetele de pe axa x pentru a decluttera graficul.  

Ce descoperi?

![MaxWingspan-scatterplot](../../../../../translated_images/ro/MaxWingspan-scatterplot.60dc9e0e19d32700283558f253841fdab5104abb62bc96f7d97f9c0ee857fa8b.png)

## Filtrează datele tale

Atât Vulturul Pleșuv, cât și Șoimul de Prerie, deși probabil păsări foarte mari, par să fie etichetate greșit, cu un zero în plus adăugat la anvergura maximă a aripilor. Este puțin probabil să întâlnești un Vultur Pleșuv cu o anvergură de 25 de metri, dar dacă da, te rugăm să ne anunți! Să creăm un nou cadru de date fără acești doi outlieri:

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
Am creat un nou cadru de date `birds_filtered` și apoi am reprezentat un grafic scatter. Prin filtrarea outlierilor, datele tale sunt acum mai coerente și mai ușor de înțeles.

![MaxWingspan-scatterplot-improved](../../../../../translated_images/ro/MaxWingspan-scatterplot-improved.7d0af81658c65f3e75b8fedeb2335399e31108257e48db15d875ece608272051.png)

Acum că avem un set de date mai curat, cel puțin în ceea ce privește anvergura aripilor, să descoperim mai multe despre aceste păsări.

Deși graficele liniare și scatter pot afișa informații despre valorile datelor și distribuțiile lor, vrem să ne gândim la valorile inerente acestui set de date. Ai putea crea vizualizări pentru a răspunde la următoarele întrebări despre cantitate:

> Câte categorii de păsări există și care sunt numerele lor?  
> Câte păsări sunt dispărute, pe cale de dispariție, rare sau comune?  
> Câte sunt din diferitele genuri și ordine în terminologia lui Linnaeus?  
## Explorează graficele cu bare

Graficele cu bare sunt practice atunci când trebuie să arăți grupări de date. Să explorăm categoriile de păsări care există în acest set de date pentru a vedea care este cea mai comună ca număr.  
Să creăm un grafic cu bare pe datele filtrate.

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
În următorul fragment, instalăm pachetele [dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8) și [lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0) pentru a ajuta la manipularea și gruparea datelor în vederea creării unui grafic cu bare stivuite. Mai întâi, grupăm datele după `Category` și apoi sumarizăm coloanele `MinLength`, `MaxLength`, `MinBodyMass`, `MaxBodyMass`, `MinWingspan`, `MaxWingspan`. Apoi, reprezentăm graficul cu bare folosind pachetul `ggplot2` și specificăm culorile pentru diferitele categorii și etichetele.  

![Stacked bar chart](../../../../../translated_images/ro/stacked-bar-chart.0c92264e89da7b391a7490224d1e7059a020e8b74dcd354414aeac78871c02f1.png)

Acest grafic cu bare, totuși, este greu de citit deoarece există prea multe date negrupate. Trebuie să selectezi doar datele pe care vrei să le reprezinți grafic, așa că să analizăm lungimea păsărilor în funcție de categoria lor.

Filtrează datele pentru a include doar categoria păsărilor.

Deoarece există multe categorii, poți afișa acest grafic vertical și ajusta înălțimea pentru a include toate datele:

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```  
Mai întâi numeri valorile unice din coloana `Category` și apoi le sortezi într-un nou cadru de date `birds_count`. Aceste date sortate sunt apoi factorizate la același nivel pentru a fi reprezentate grafic în mod ordonat. Folosind `ggplot2`, reprezinți grafic datele într-un grafic cu bare. Funcția `coord_flip()` afișează barele orizontal.  

![category-length](../../../../../translated_images/ro/category-length.7e34c296690e85d64f7e4d25a56077442683eca96c4f5b4eae120a64c0755636.png)

Acest grafic cu bare oferă o vedere bună asupra numărului de păsări din fiecare categorie. Dintr-o privire, vezi că cel mai mare număr de păsări din această regiune sunt în categoria Rațe/Gâște/Păsări acvatice. Minnesota este 'țara celor 10.000 de lacuri', așa că acest lucru nu este surprinzător!

✅ Încearcă alte numărători pe acest set de date. Te surprinde ceva?

## Compararea datelor

Poți încerca diferite comparații ale datelor grupate prin crearea de noi axe. Încearcă o comparație a LungimiiMaxime a unei păsări, bazată pe categoria sa:

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
Grupăm datele `birds_filtered` după `Category` și apoi reprezentăm grafic un grafic cu bare.  

![comparing data](../../../../../translated_images/ro/comparingdata.f486a450d61c7ca5416f27f3f55a6a4465d00df3be5e6d33936e9b07b95e2fdd.png)

Nimic nu este surprinzător aici: colibrii au cea mai mică LungimeMaximă comparativ cu Pelicanii sau Gâștele. Este bine când datele au sens logic!

Poți crea vizualizări mai interesante ale graficelor cu bare prin suprapunerea datelor. Să suprapunem LungimeaMinimă și LungimeaMaximă pe o categorie de păsări dată:

```r
ggplot(data=birds_grouped, aes(x=Category)) +
  geom_bar(aes(y=MaxLength), stat="identity", position ="identity",  fill='blue') +
  geom_bar(aes(y=MinLength), stat="identity", position="identity", fill='orange')+
  coord_flip()
```  
![super-imposed values](../../../../../translated_images/ro/superimposed-values.5363f0705a1da4167625a373a1064331ea3cb7a06a297297d0734fcc9b3819a0.png)

## 🚀 Provocare

Acest set de date despre păsări oferă o bogăție de informații despre diferite tipuri de păsări dintr-un anumit ecosistem. Caută pe internet și vezi dacă poți găsi alte seturi de date orientate spre păsări. Exersează construirea de grafice și diagrame despre aceste păsări pentru a descoperi fapte pe care nu le știai.

## [Chestionar după lecție](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## Recapitulare & Studiu Individual

Această primă lecție ți-a oferit câteva informații despre cum să folosești `ggplot2` pentru a vizualiza cantități. Fă cercetări despre alte moduri de a lucra cu seturi de date pentru vizualizare. Cercetează și caută seturi de date pe care le-ai putea vizualiza folosind alte pachete precum [Lattice](https://stat.ethz.ch/R-manual/R-devel/library/lattice/html/Lattice.html) și [Plotly](https://github.com/plotly/plotly.R#readme).

## Temă
[Grafice liniare, scatter și bare](assignment.md)

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.