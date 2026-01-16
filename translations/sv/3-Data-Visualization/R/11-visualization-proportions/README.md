<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "47028abaaafa2bcb1079702d20569066",
  "translation_date": "2025-08-26T23:14:19+00:00",
  "source_file": "3-Data-Visualization/R/11-visualization-proportions/README.md",
  "language_code": "sv"
}
-->
# Visualisera Proportioner

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Visualisera Proportioner - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

I den här lektionen kommer du att använda ett dataset med naturfokus för att visualisera proportioner, till exempel hur många olika typer av svampar som finns i ett dataset om svampar. Låt oss utforska dessa fascinerande svampar med hjälp av ett dataset från Audubon som listar detaljer om 23 arter av skivlingar i Agaricus- och Lepiota-familjerna. Du kommer att experimentera med smakfulla visualiseringar som:

- Pajdiagram 🥧
- Donutdiagram 🍩
- Våffeldiagram 🧇

> 💡 Ett mycket intressant projekt som heter [Charticulator](https://charticulator.com) från Microsoft Research erbjuder ett gratis dra-och-släpp-gränssnitt för datavisualiseringar. I en av deras handledningar använder de också detta svampdataset! Så du kan utforska datan och lära dig biblioteket samtidigt: [Charticulator tutorial](https://charticulator.com/tutorials/tutorial4.html).

## [Quiz före lektionen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## Lär känna dina svampar 🍄

Svampar är väldigt intressanta. Låt oss importera ett dataset för att studera dem:

```r
mushrooms = read.csv('../../data/mushrooms.csv')
head(mushrooms)
```
En tabell skrivs ut med fantastisk data för analys:


| klass     | hattform   | hattyta     | hattfärg  | blåmärken | lukt     | skivfäste       | skivavstånd  | skivstorlek | skivfärg   | fotform     | fotrot     | fotyta-ovanför-ring     | fotyta-under-ring        | fotfärg-ovanför-ring   | fotfärg-under-ring     | slöjtyp   | slöjfärg   | ringantal   | ringtyp   | sporfärg          | population | habitat |
| --------- | ---------- | ----------- | --------- | --------- | -------- | --------------- | ------------ | ----------- | ---------- | ----------- | ---------- | ----------------------- | ----------------------- | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Giftig    | Konvex     | Slät        | Brun      | Blåmärken | Stickande| Fri             | Tät          | Smal        | Svart      | Förstorad   | Lika       | Slät                    | Slät                    | Vit                    | Vit                    | Partiell  | Vit        | En          | Hängande  | Svart             | Spridd     | Urban   |
| Ätlig     | Konvex     | Slät        | Gul       | Blåmärken | Mandel   | Fri             | Tät          | Bred        | Svart      | Förstorad   | Klubba     | Slät                    | Slät                    | Vit                    | Vit                    | Partiell  | Vit        | En          | Hängande  | Brun              | Talrik     | Gräs    |
| Ätlig     | Klockformad| Slät        | Vit       | Blåmärken | Anis     | Fri             | Tät          | Bred        | Brun       | Förstorad   | Klubba     | Slät                    | Slät                    | Vit                    | Vit                    | Partiell  | Vit        | En          | Hängande  | Brun              | Talrik     | Ängar   |
| Giftig    | Konvex     | Fjällig     | Vit       | Blåmärken | Stickande| Fri             | Tät          | Smal        | Brun       | Förstorad   | Lika       | Slät                    | Slät                    | Vit                    | Vit                    | Partiell  | Vit        | En          | Hängande  | Svart             | Spridd     | Urban   |
| Ätlig     | Konvex     | Slät        | Grön      | Inga blåmärken| Ingen | Fri             | Trångt       | Bred        | Svart      | Avsmalnande| Lika       | Slät                    | Slät                    | Vit                    | Vit                    | Partiell  | Vit        | En          | Försvinnande | Brun           | Riklig     | Gräs    |
| Ätlig     | Konvex     | Fjällig     | Gul       | Blåmärken | Mandel   | Fri             | Tät          | Bred        | Brun       | Förstorad   | Klubba     | Slät                    | Slät                    | Vit                    | Vit                    | Partiell  | Vit        | En          | Hängande  | Svart             | Talrik     | Gräs    |

Direkt märker du att all data är textuell. Du måste konvertera denna data för att kunna använda den i ett diagram. Faktum är att det mesta av datan representeras som ett objekt:

```r
names(mushrooms)
```

Utdata är:

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
Ta denna data och konvertera kolumnen 'klass' till en kategori:

```r
library(dplyr)
grouped=mushrooms %>%
  group_by(class) %>%
  summarise(count=n())
```

Nu, om du skriver ut svampdatan, kan du se att den har grupperats i kategorier enligt klassen giftig/ätlig:
```r
View(grouped)
```

| klass | antal |
| --------- | --------- |
| Ätlig     | 4208      |
| Giftig    | 3916      |

Om du följer ordningen i denna tabell för att skapa dina klasskategorietiketter kan du bygga ett pajdiagram.

## Paj!

```r
pie(grouped$count,grouped$class, main="Edible?")
```
Voilà, ett pajdiagram som visar proportionerna av denna data enligt dessa två svampklasser. Det är ganska viktigt att få ordningen på etiketterna rätt, särskilt här, så se till att verifiera ordningen när etikettarrayen byggs!

![pajdiagram](../../../../../translated_images/sv/pie1-wb.685df063673751f4b0b82127f7a52c7f9a920192f22ae61ad28412ba9ace97bf.png)

## Donuts!

Ett något mer visuellt intressant pajdiagram är ett donutdiagram, som är ett pajdiagram med ett hål i mitten. Låt oss titta på vår data med denna metod.

Titta på de olika habitat där svampar växer:

```r
library(dplyr)
habitat=mushrooms %>%
  group_by(habitat) %>%
  summarise(count=n())
View(habitat)
```
Utdata är:
| habitat | antal |
| --------- | --------- |
| Gräs      | 2148      |
| Löv       | 832       |
| Ängar     | 292       |
| Stigar    | 1144      |
| Urban     | 368       |
| Avfall    | 192       |
| Trä       | 3148      |

Här grupperar du din data efter habitat. Det finns 7 listade, så använd dessa som etiketter för ditt donutdiagram:

```r
library(ggplot2)
library(webr)
PieDonut(habitat, aes(habitat, count=count))
```

![donutdiagram](../../../../../translated_images/sv/donut-wb.34e6fb275da9d834c2205145e39a3de9b6878191dcdba6f7a9e85f4b520449bc.png)

Denna kod använder de två biblioteken ggplot2 och webr. Med hjälp av funktionen PieDonut i webr-biblioteket kan vi enkelt skapa ett donutdiagram!

Donutdiagram i R kan också göras med endast ggplot2-biblioteket. Du kan läsa mer om det [här](https://www.r-graph-gallery.com/128-ring-or-donut-plot.html) och prova själv.

Nu när du vet hur du grupperar din data och sedan visar den som paj eller donut kan du utforska andra typer av diagram. Prova ett våffeldiagram, som är ett annat sätt att utforska kvantitet.

## Våfflor!

Ett 'våffel'-diagram är ett annat sätt att visualisera kvantiteter som en 2D-array av rutor. Försök att visualisera de olika mängderna av svamphattfärger i detta dataset. För att göra detta behöver du installera ett hjälpbibliotek som heter [waffle](https://cran.r-project.org/web/packages/waffle/waffle.pdf) och använda det för att skapa din visualisering:

```r
install.packages("waffle", repos = "https://cinc.rud.is")
```

Välj ett segment av din data att gruppera:

```r
library(dplyr)
cap_color=mushrooms %>%
  group_by(cap.color) %>%
  summarise(count=n())
View(cap_color)
```

Skapa ett våffeldiagram genom att skapa etiketter och sedan gruppera din data:

```r
library(waffle)
names(cap_color$count) = paste0(cap_color$cap.color)
waffle((cap_color$count/10), rows = 7, title = "Waffle Chart")+scale_fill_manual(values=c("brown", "#F0DC82", "#D2691E", "green", 
                                                                                     "pink", "purple", "red", "grey", 
                                                                                     "yellow","white"))
```

Med ett våffeldiagram kan du tydligt se proportionerna av hattfärger i detta svampdataset. Intressant nog finns det många svampar med gröna hattar!

![våffeldiagram](../../../../../translated_images/sv/waffle.aaa75c5337735a6ef32ace0ffb6506ef49e5aefe870ffd72b1bb080f4843c217.png)

I den här lektionen lärde du dig tre sätt att visualisera proportioner. Först behöver du gruppera din data i kategorier och sedan bestämma vilket som är det bästa sättet att visa datan - paj, donut eller våffla. Alla är läckra och ger användaren en omedelbar överblick av ett dataset.

## 🚀 Utmaning

Försök återskapa dessa smakfulla diagram i [Charticulator](https://charticulator.com).
## [Quiz efter lektionen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## Granskning & Självstudier

Ibland är det inte uppenbart när man ska använda ett paj-, donut- eller våffeldiagram. Här är några artiklar att läsa om detta ämne:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Gör lite forskning för att hitta mer information om detta knepiga beslut.

## Uppgift

[Prova det i Excel](assignment.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller inexaktheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.