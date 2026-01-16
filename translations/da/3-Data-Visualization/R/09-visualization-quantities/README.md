<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-26T23:06:37+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "da"
}
-->
# Visualisering af mængder
|![ Sketchnote af [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Visualisering af mængder - _Sketchnote af [@nitya](https://twitter.com/nitya)_ |

I denne lektion vil du udforske, hvordan du kan bruge nogle af de mange tilgængelige R-pakker til at lære at skabe interessante visualiseringer omkring begrebet mængde. Ved at bruge et renset datasæt om fuglene i Minnesota kan du lære mange interessante fakta om det lokale dyreliv.  
## [Quiz før lektionen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## Observer vingefang med ggplot2
Et fremragende bibliotek til at skabe både simple og avancerede diagrammer og grafer af forskellige slags er [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html). Generelt indebærer processen med at plotte data ved hjælp af disse biblioteker at identificere de dele af din dataframe, du vil fokusere på, udføre nødvendige transformationer på dataene, tildele værdier til x- og y-aksen, beslutte hvilken type diagram der skal vises, og derefter vise diagrammet.

`ggplot2` er et system til deklarativt at skabe grafik baseret på "The Grammar of Graphics". [Grammar of Graphics](https://en.wikipedia.org/wiki/Ggplot2) er en generel tilgang til datavisualisering, der opdeler grafer i semantiske komponenter som skalaer og lag. Med andre ord gør enkeltheden i at skabe grafer og diagrammer for univariat eller multivariat data med lidt kode `ggplot2` til den mest populære pakke til visualiseringer i R. Brugeren fortæller `ggplot2`, hvordan variabler skal mappes til æstetik, hvilke grafiske elementer der skal bruges, og `ggplot2` tager sig af resten.

> ✅ Diagram = Data + Æstetik + Geometri  
> - Data refererer til datasættet  
> - Æstetik angiver de variabler, der skal undersøges (x- og y-variabler)  
> - Geometri refererer til typen af diagram (linjediagram, søjlediagram osv.)  

Vælg den bedste geometri (diagramtype) i forhold til dine data og den historie, du vil fortælle gennem diagrammet.

> - For at analysere tendenser: linje, søjle  
> - For at sammenligne værdier: søjle, cirkel, punktdiagram  
> - For at vise, hvordan dele relaterer sig til helheden: cirkeldiagram  
> - For at vise fordelingen af data: punktdiagram, søjle  
> - For at vise relationer mellem værdier: linje, punktdiagram, boblediagram  

✅ Du kan også tjekke dette beskrivende [cheatsheet](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf) for ggplot2.

## Byg et linjediagram over fuglenes vingefang

Åbn R-konsollen og importer datasættet.  
> Bemærk: Datasættet er gemt i roden af dette repo i `/data`-mappen.

Lad os importere datasættet og observere de første fem rækker af dataene.

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```  
De første rækker af dataene indeholder en blanding af tekst og tal:

|      | Navn                         | VidenskabeligtNavn     | Kategori              | Orden        | Familie  | Slægt       | Bevaringsstatus     | MinLængde | MaxLængde | MinKropsvægt | MaxKropsvægt | MinVingefang | MaxVingefang |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Sortbuget fløjlsand          | Dendrocygna autumnalis | Ænder/Gæs/Vandfugle   | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fløjlsand                    | Dendrocygna bicolor    | Ænder/Gæs/Vandfugle   | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snegås                       | Anser caerulescens     | Ænder/Gæs/Vandfugle   | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross' gås                    | Anser rossii           | Ænder/Gæs/Vandfugle   | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Stor hvidkindet gås          | Anser albifrons        | Ænder/Gæs/Vandfugle   | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Lad os starte med at plotte nogle af de numeriske data ved hjælp af et grundlæggende linjediagram. Antag, at du vil have et overblik over det maksimale vingefang for disse interessante fugle.

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```  
Her installerer du `ggplot2`-pakken og importerer den derefter til arbejdsområdet ved hjælp af kommandoen `library("ggplot2")`. For at plotte et diagram i ggplot bruges funktionen `ggplot()`, hvor du angiver datasættet samt x- og y-variabler som attributter. I dette tilfælde bruger vi funktionen `geom_line()`, da vi ønsker at plotte et linjediagram.

![MaxWingspan-lineplot](../../../../../translated_images/da/MaxWingspan-lineplot.b12169f99d26fdd263f291008dfd73c18a4ba8f3d32b1fda3d74af51a0a28616.png)

Hvad bemærker du med det samme? Der ser ud til at være mindst én outlier – det er et ret stort vingefang! Et vingefang på over 2000 centimeter svarer til mere end 20 meter – er der pterodaktyler i Minnesota? Lad os undersøge det nærmere.

Selvom du hurtigt kunne sortere i Excel for at finde disse outliers, som sandsynligvis er tastefejl, fortsæt visualiseringsprocessen ved at arbejde direkte fra diagrammet.

Tilføj labels til x-aksen for at vise, hvilke fugle der er tale om:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```  
Vi angiver vinklen i `theme` og specificerer labels for x- og y-aksen i henholdsvis `xlab()` og `ylab()`. `ggtitle()` giver diagrammet en titel.

![MaxWingspan-lineplot-improved](../../../../../translated_images/da/MaxWingspan-lineplot-improved.04b73b4d5a59552a6bc7590678899718e1f065abe9eada9ebb4148939b622fd4.png)

Selv med rotationen af labels sat til 45 grader er der for mange til at læse. Lad os prøve en anden strategi: kun at label outliers og placere labels inden for diagrammet. Du kan bruge et punktdiagram for at skabe mere plads til labeling:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```  
Hvad sker der her? Du brugte funktionen `geom_point()` til at plotte punkter. Med dette tilføjede du labels for fugle med `MaxWingspan > 500` og skjulte også labels på x-aksen for at rydde op i diagrammet.

Hvad opdager du?

![MaxWingspan-scatterplot](../../../../../translated_images/da/MaxWingspan-scatterplot.60dc9e0e19d32700283558f253841fdab5104abb62bc96f7d97f9c0ee857fa8b.png)

## Filtrer dine data

Både den skaldede ørn og præriefalken, som sandsynligvis er meget store fugle, ser ud til at være fejlmærkede med et ekstra 0 tilføjet til deres maksimale vingefang. Det er usandsynligt, at du møder en skaldet ørn med et vingefang på 25 meter, men hvis du gør, så lad os det vide! Lad os oprette en ny dataframe uden disse to outliers:

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
Vi oprettede en ny dataframe `birds_filtered` og plottede derefter et punktdiagram. Ved at filtrere outliers ud er dine data nu mere sammenhængende og forståelige.

![MaxWingspan-scatterplot-improved](../../../../../translated_images/da/MaxWingspan-scatterplot-improved.7d0af81658c65f3e75b8fedeb2335399e31108257e48db15d875ece608272051.png)

Nu hvor vi har et renere datasæt, i det mindste hvad angår vingefang, lad os opdage mere om disse fugle.

Mens linje- og punktdiagrammer kan vise information om dataværdier og deres fordeling, vil vi tænke over de værdier, der er iboende i dette datasæt. Du kunne skabe visualiseringer for at besvare følgende spørgsmål om mængde:

> Hvor mange kategorier af fugle er der, og hvad er deres antal?  
> Hvor mange fugle er uddøde, truede, sjældne eller almindelige?  
> Hvor mange er der af de forskellige slægter og ordener i Linnaeus' terminologi?  

## Udforsk søjlediagrammer

Søjlediagrammer er praktiske, når du skal vise grupperinger af data. Lad os udforske kategorierne af fugle, der findes i dette datasæt, for at se, hvilken der er mest almindelig i antal.  
Lad os oprette et søjlediagram baseret på de filtrerede data.

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
I det følgende snippet installerer vi pakkerne [dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8) og [lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0) for at hjælpe med at manipulere og gruppere data for at plotte et stablet søjlediagram. Først grupperer du dataene efter fuglenes `Category` og opsummerer kolonnerne `MinLength`, `MaxLength`, `MinBodyMass`, `MaxBodyMass`, `MinWingspan`, `MaxWingspan`. Derefter plottes søjlediagrammet ved hjælp af `ggplot2`-pakken, hvor du specificerer farverne for de forskellige kategorier og labels.

![Stablet søjlediagram](../../../../../translated_images/da/stacked-bar-chart.0c92264e89da7b391a7490224d1e7059a020e8b74dcd354414aeac78871c02f1.png)

Dette søjlediagram er dog ulæseligt, fordi der er for mange ikke-grupperede data. Du skal vælge kun de data, du vil plotte, så lad os se på længden af fugle baseret på deres kategori.

Filtrer dine data til kun at inkludere fuglenes kategori.

Da der er mange kategorier, kan du vise dette diagram lodret og justere højden for at tage højde for alle dataene:

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```  
Du tæller først unikke værdier i kolonnen `Category` og sorterer dem derefter i en ny dataframe `birds_count`. Disse sorterede data faktoreres derefter på samme niveau, så de plottes i den sorterede rækkefølge. Ved hjælp af `ggplot2` plottes dataene derefter i et søjlediagram. `coord_flip()` plottes som vandrette søjler.

![kategori-længde](../../../../../translated_images/da/category-length.7e34c296690e85d64f7e4d25a56077442683eca96c4f5b4eae120a64c0755636.png)

Dette søjlediagram giver et godt overblik over antallet af fugle i hver kategori. Med et øjeblik ser du, at det største antal fugle i denne region tilhører kategorien Ænder/Gæs/Vandfugle. Minnesota er trods alt "de 10.000 søers land", så det er ikke overraskende!

✅ Prøv nogle andre optællinger på dette datasæt. Er der noget, der overrasker dig?

## Sammenligning af data

Du kan prøve forskellige sammenligninger af grupperede data ved at oprette nye akser. Prøv en sammenligning af fuglenes MaxLength baseret på deres kategori:

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
Vi grupperer dataene `birds_filtered` efter `Category` og plottede derefter et søjlediagram.

![sammenligning af data](../../../../../translated_images/da/comparingdata.f486a450d61c7ca5416f27f3f55a6a4465d00df3be5e6d33936e9b07b95e2fdd.png)

Intet er overraskende her: kolibrier har den mindste MaxLength sammenlignet med pelikaner eller gæs. Det er godt, når data giver logisk mening!

Du kan skabe mere interessante visualiseringer af søjlediagrammer ved at overlejre data. Lad os overlejre Minimum og Maksimum Længde på en given fuglekategori:

```r
ggplot(data=birds_grouped, aes(x=Category)) +
  geom_bar(aes(y=MaxLength), stat="identity", position ="identity",  fill='blue') +
  geom_bar(aes(y=MinLength), stat="identity", position="identity", fill='orange')+
  coord_flip()
```  
![overlejrede værdier](../../../../../translated_images/da/superimposed-values.5363f0705a1da4167625a373a1064331ea3cb7a06a297297d0734fcc9b3819a0.png)

## 🚀 Udfordring

Dette fugledatasæt tilbyder en rigdom af information om forskellige typer fugle inden for et bestemt økosystem. Søg på internettet og se, om du kan finde andre datasæt om fugle. Øv dig i at bygge diagrammer og grafer omkring disse fugle for at opdage fakta, du ikke kendte.

## [Quiz efter lektionen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## Gennemgang & Selvstudie

Denne første lektion har givet dig noget information om, hvordan du bruger `ggplot2` til at visualisere mængder. Lav noget research om andre måder at arbejde med datasæt til visualisering. Undersøg og kig efter datasæt, som du kunne visualisere ved hjælp af andre pakker som [Lattice](https://stat.ethz.ch/R-manual/R-devel/library/lattice/html/Lattice.html) og [Plotly](https://github.com/plotly/plotly.R#readme).

## Opgave
[Linjer, punkter og søjler](assignment.md)  

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.