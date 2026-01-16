<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea67c0c40808fd723594de6896c37ccf",
  "translation_date": "2025-08-26T22:57:45+00:00",
  "source_file": "3-Data-Visualization/R/10-visualization-distributions/README.md",
  "language_code": "da"
}
-->
# Visualisering af fordelinger

|![ Sketchnote af [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Visualisering af fordelinger - _Sketchnote af [@nitya](https://twitter.com/nitya)_ |

I den forrige lektion lærte du nogle interessante fakta om et datasæt om fuglene i Minnesota. Du fandt nogle fejlagtige data ved at visualisere outliers og kiggede på forskellene mellem fuglekategorier baseret på deres maksimale længde.

## [Quiz før lektionen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## Udforsk fugledatasættet

En anden måde at undersøge data på er ved at se på deres fordeling, eller hvordan dataene er organiseret langs en akse. Måske vil du for eksempel gerne lære om den generelle fordeling i dette datasæt af den maksimale vingefang eller den maksimale kropsmasse for fuglene i Minnesota.

Lad os opdage nogle fakta om fordelingerne af data i dette datasæt. I din R-konsol skal du importere `ggplot2` og databasen. Fjern outliers fra databasen, ligesom vi gjorde i det forrige emne.

```r
library(ggplot2)

birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")

birds_filtered <- subset(birds, MaxWingspan < 500)
head(birds_filtered)
```
|      | Navn                         | VidenskabeligtNavn     | Kategori              | Orden        | Familie  | Slægt       | Bevaringsstatus     | MinLængde | MaxLængde | MinKropsmasse | MaxKropsmasse | MinVingefang | MaxVingefang |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Sortbuget fløjlsand          | Dendrocygna autumnalis | Ænder/Gæs/Vandfugle   | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Rødbrun fløjlsand            | Dendrocygna bicolor    | Ænder/Gæs/Vandfugle   | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snegås                       | Anser caerulescens     | Ænder/Gæs/Vandfugle   | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross' gås                    | Anser rossii           | Ænder/Gæs/Vandfugle   | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Stor hvidkindet gås          | Anser albifrons        | Ænder/Gæs/Vandfugle   | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Generelt kan du hurtigt få et overblik over, hvordan data er fordelt, ved at bruge et scatterplot, som vi gjorde i den forrige lektion:

```r
ggplot(data=birds_filtered, aes(x=Order, y=MaxLength,group=1)) +
  geom_point() +
  ggtitle("Max Length per order") + coord_flip()
```
![maksimal længde pr. orden](../../../../../translated_images/da/max-length-per-order.e5b283d952c78c12b091307c5d3cf67132dad6fefe80a073353b9dc5c2bd3eb8.png)

Dette giver et overblik over den generelle fordeling af kropslængde pr. fugleorden, men det er ikke den optimale måde at vise egentlige fordelinger. Denne opgave håndteres normalt ved at oprette et histogram.
## Arbejde med histogrammer

`ggplot2` tilbyder meget gode måder at visualisere datafordeling ved hjælp af histogrammer. Denne type diagram minder om et søjlediagram, hvor fordelingen kan ses via stigningen og faldet af søjlerne. For at oprette et histogram skal du bruge numeriske data. For at oprette et histogram kan du plotte et diagram og definere typen som 'hist' for histogram. Dette diagram viser fordelingen af MaxBodyMass for hele datasættets række af numeriske data. Ved at opdele dataene i mindre bins kan det vise fordelingen af dataenes værdier:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=10)+ylab('Frequency')
```
![fordeling over hele datasættet](../../../../../translated_images/da/distribution-over-the-entire-dataset.d22afd3fa96be854e4c82213fedec9e3703cba753d07fad4606aadf58cf7e78e.png)

Som du kan se, falder de fleste af de 400+ fugle i dette datasæt inden for området under 2000 for deres maksimale kropsmasse. Få mere indsigt i dataene ved at ændre `bins`-parameteren til et højere tal, f.eks. 30:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + geom_histogram(bins=30)+ylab('Frequency')
```

![fordeling-30bins](../../../../../translated_images/da/distribution-30bins.6a3921ea7a421bf71f06bf5231009e43d1146f1b8da8dc254e99b5779a4983e5.png)

Dette diagram viser fordelingen på en lidt mere detaljeret måde. Et diagram, der er mindre skævt mod venstre, kunne oprettes ved at sikre, at du kun vælger data inden for et givet område:

Filtrer dine data for kun at få de fugle, hvis kropsmasse er under 60, og vis 30 `bins`:

```r
birds_filtered_1 <- subset(birds_filtered, MaxBodyMass > 1 & MaxBodyMass < 60)
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=30)+ylab('Frequency')
```

![filtreret histogram](../../../../../translated_images/da/filtered-histogram.6bf5d2bfd82533220e1bd4bc4f7d14308f43746ed66721d9ec8f460732be6674.png)

✅ Prøv nogle andre filtre og datapunkter. For at se den fulde fordeling af dataene skal du fjerne `['MaxBodyMass']`-filteret for at vise mærkede fordelinger.

Histogrammet tilbyder også nogle flotte farve- og mærkningsforbedringer, som du kan prøve:

Opret et 2D-histogram for at sammenligne forholdet mellem to fordelinger. Lad os sammenligne `MaxBodyMass` vs. `MaxLength`. `ggplot2` tilbyder en indbygget måde at vise konvergens ved hjælp af lysere farver:

```r
ggplot(data=birds_filtered_1, aes(x=MaxBodyMass, y=MaxLength) ) +
  geom_bin2d() +scale_fill_continuous(type = "viridis")
```
Der ser ud til at være en forventet korrelation mellem disse to elementer langs en forventet akse, med et særligt stærkt konvergenspunkt:

![2d plot](../../../../../translated_images/da/2d-plot.c504786f439bd7ebceebf2465c70ca3b124103e06c7ff7214bf24e26f7aec21e.png)

Histogrammer fungerer godt som standard for numeriske data. Hvad hvis du har brug for at se fordelinger baseret på tekstdata? 
## Udforsk datasættet for fordelinger ved hjælp af tekstdata 

Dette datasæt indeholder også gode oplysninger om fuglekategori og dens slægt, art og familie samt dens bevaringsstatus. Lad os undersøge disse bevaringsoplysninger. Hvad er fordelingen af fuglene baseret på deres bevaringsstatus?

> ✅ I datasættet bruges flere akronymer til at beskrive bevaringsstatus. Disse akronymer kommer fra [IUCN Red List Categories](https://www.iucnredlist.org/), en organisation der katalogiserer arters status.
> 
> - CR: Kritisk truet
> - EN: Truet
> - EX: Uddød
> - LC: Mindst bekymring
> - NT: Næsten truet
> - VU: Sårbar

Disse er tekstbaserede værdier, så du skal lave en transformation for at oprette et histogram. Brug den filtreredeBirds-dataramme til at vise dens bevaringsstatus sammen med dens minimumsvingefang. Hvad ser du?

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

![vingefang og bevaringsstatus](../../../../../translated_images/da/wingspan-conservation-collation.4024e9aa6910866aa82f0c6cb6a6b4b925bd10079e6b0ef8f92eefa5a6792f76.png)

Der ser ikke ud til at være en god korrelation mellem minimumsvingefang og bevaringsstatus. Test andre elementer i datasættet ved hjælp af denne metode. Du kan også prøve forskellige filtre. Finder du nogen korrelation?

## Tæthedsdiagrammer

Du har måske bemærket, at de histogrammer, vi har kigget på indtil videre, er 'trappede' og ikke flyder jævnt i en bue. For at vise et mere glat tæthedsdiagram kan du prøve et tæthedsplot.

Lad os arbejde med tæthedsdiagrammer nu!

```r
ggplot(data = birds_filtered_1, aes(x = MinWingspan)) + 
  geom_density()
```
![tæthedsdiagram](../../../../../translated_images/da/density-plot.675ccf865b76c690487fb7f69420a8444a3515f03bad5482886232d4330f5c85.png)

Du kan se, hvordan diagrammet afspejler det tidligere for Minimum Wingspan-data; det er bare lidt glattere. Hvis du ville genbesøge den hakkede MaxBodyMass-linje i det andet diagram, du oprettede, kunne du glatte den meget godt ud ved at genskabe den ved hjælp af denne metode:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density()
```
![kropsmasse tæthed](../../../../../translated_images/da/bodymass-smooth.d31ce526d82b0a1f19a073815dea28ecfbe58145ec5337e4ef7e8cdac81120b3.png)

Hvis du ville have en glat, men ikke alt for glat linje, kan du redigere `adjust`-parameteren: 

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density(adjust = 1/5)
```
![mindre glat kropsmasse](../../../../../translated_images/da/less-smooth-bodymass.10f4db8b683cc17d17b2d33f22405413142004467a1493d416608dafecfdee23.png)

✅ Læs om de tilgængelige parametre for denne type diagram og eksperimentér!

Denne type diagram tilbyder smukt forklarende visualiseringer. Med få linjer kode kan du for eksempel vise den maksimale kropsmasse tæthed pr. fugleorden:

```r
ggplot(data=birds_filtered_1,aes(x = MaxBodyMass, fill = Order)) +
  geom_density(alpha=0.5)
```
![kropsmasse pr. orden](../../../../../translated_images/da/bodymass-per-order.9d2b065dd931b928c839d8cdbee63067ab1ae52218a1b90717f4bc744354f485.png)

## 🚀 Udfordring

Histogrammer er en mere sofistikeret type diagram end grundlæggende scatterplots, søjlediagrammer eller linjediagrammer. Gå på internettet og find gode eksempler på brugen af histogrammer. Hvordan bruges de, hvad demonstrerer de, og inden for hvilke områder eller felter anvendes de typisk?

## [Quiz efter lektionen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## Gennemgang & Selvstudie

I denne lektion brugte du `ggplot2` og begyndte at arbejde med mere sofistikerede diagrammer. Lav noget research om `geom_density_2d()`, en "kontinuerlig sandsynlighedstæthedskurve i en eller flere dimensioner". Læs [dokumentationen](https://ggplot2.tidyverse.org/reference/geom_density_2d.html) for at forstå, hvordan det fungerer.

## Opgave

[Anvend dine færdigheder](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.