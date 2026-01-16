<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea67c0c40808fd723594de6896c37ccf",
  "translation_date": "2025-08-28T15:33:29+00:00",
  "source_file": "3-Data-Visualization/R/10-visualization-distributions/README.md",
  "language_code": "nl"
}
-->
# Visualiseren van distributies

|![ Sketchnote door [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Visualiseren van distributies - _Sketchnote door [@nitya](https://twitter.com/nitya)_ |

In de vorige les heb je enkele interessante feiten geleerd over een dataset over de vogels van Minnesota. Je hebt foutieve gegevens gevonden door uitschieters te visualiseren en keek naar de verschillen tussen vogelcategorieën op basis van hun maximale lengte.

## [Quiz voorafgaand aan de les](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## Verken de vogeldataset

Een andere manier om gegevens te onderzoeken is door te kijken naar de distributie, of hoe de gegevens langs een as zijn georganiseerd. Misschien wil je bijvoorbeeld meer weten over de algemene distributie, voor deze dataset, van de maximale vleugelspanwijdte of maximale lichaamsmassa van de vogels van Minnesota.

Laten we enkele feiten ontdekken over de distributies van gegevens in deze dataset. Importeer in je R-console `ggplot2` en de database. Verwijder de uitschieters uit de database, net zoals in het vorige onderwerp.

```r
library(ggplot2)

birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")

birds_filtered <- subset(birds, MaxWingspan < 500)
head(birds_filtered)
```
|      | Naam                         | WetenschappelijkeNaam  | Categorie             | Orde         | Familie  | Geslacht    | Beschermingsstatus  | MinLengte | MaxLengte | MinLichaamsmassa | MaxLichaamsmassa | MinVleugelspan | MaxVleugelspan |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | --------------: | --------------: | -------------: | -------------: |
|    0 | Zwartbuikfluiteend           | Dendrocygna autumnalis | Eenden/Ganzen/Watervogels | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |             652 |            1020 |             76 |             94 |
|    1 | Rosse fluiteend              | Dendrocygna bicolor    | Eenden/Ganzen/Watervogels | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |             712 |            1050 |             85 |             93 |
|    2 | Sneeuwgans                   | Anser caerulescens     | Eenden/Ganzen/Watervogels | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |            2050 |            4050 |            135 |            165 |
|    3 | Ross' gans                   | Anser rossii           | Eenden/Ganzen/Watervogels | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |            1066 |            1567 |            113 |            116 |
|    4 | Grote rietgans               | Anser albifrons        | Eenden/Ganzen/Watervogels | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |            1930 |            3310 |            130 |            165 |

Over het algemeen kun je snel kijken naar hoe gegevens zijn verdeeld door een spreidingsdiagram te gebruiken, zoals we in de vorige les deden:

```r
ggplot(data=birds_filtered, aes(x=Order, y=MaxLength,group=1)) +
  geom_point() +
  ggtitle("Max Length per order") + coord_flip()
```
![max lengte per orde](../../../../../translated_images/nl/max-length-per-order.e5b283d952c78c12b091307c5d3cf67132dad6fefe80a073353b9dc5c2bd3eb8.png)

Dit geeft een overzicht van de algemene verdeling van lichaamslengte per vogelorde, maar het is niet de optimale manier om echte distributies weer te geven. Die taak wordt meestal uitgevoerd door een histogram te maken.
## Werken met histogrammen

`ggplot2` biedt zeer goede manieren om gegevensdistributie te visualiseren met behulp van histogrammen. Dit type diagram lijkt op een staafdiagram waarbij de distributie kan worden gezien via een stijging en daling van de staven. Om een histogram te maken, heb je numerieke gegevens nodig. Om een histogram te maken, kun je een diagram plotten waarbij je het type definieert als 'hist' voor histogram. Dit diagram toont de distributie van MaxBodyMass voor het volledige bereik van numerieke gegevens in de dataset. Door de reeks gegevens op te splitsen in kleinere bins, kan het de distributie van de waarden van de gegevens weergeven:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=10)+ylab('Frequency')
```
![distributie over de hele dataset](../../../../../translated_images/nl/distribution-over-the-entire-dataset.d22afd3fa96be854e4c82213fedec9e3703cba753d07fad4606aadf58cf7e78e.png)

Zoals je kunt zien, valt het merendeel van de 400+ vogels in deze dataset in het bereik van minder dan 2000 voor hun maximale lichaamsmassa. Krijg meer inzicht in de gegevens door de parameter `bins` te wijzigen naar een hoger aantal, bijvoorbeeld 30:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + geom_histogram(bins=30)+ylab('Frequency')
```

![distributie-30bins](../../../../../translated_images/nl/distribution-30bins.6a3921ea7a421bf71f06bf5231009e43d1146f1b8da8dc254e99b5779a4983e5.png)

Dit diagram toont de distributie op een iets meer gedetailleerde manier. Een diagram dat minder naar links is scheefgetrokken, kan worden gemaakt door ervoor te zorgen dat je alleen gegevens selecteert binnen een bepaald bereik:

Filter je gegevens om alleen die vogels te krijgen waarvan de lichaamsmassa onder de 60 ligt, en toon 30 `bins`:

```r
birds_filtered_1 <- subset(birds_filtered, MaxBodyMass > 1 & MaxBodyMass < 60)
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=30)+ylab('Frequency')
```

![gefilterd histogram](../../../../../translated_images/nl/filtered-histogram.6bf5d2bfd82533220e1bd4bc4f7d14308f43746ed66721d9ec8f460732be6674.png)

✅ Probeer enkele andere filters en gegevenspunten. Om de volledige distributie van de gegevens te zien, verwijder je de `['MaxBodyMass']` filter om gelabelde distributies weer te geven.

Het histogram biedt ook enkele leuke kleur- en labelverbeteringen om te proberen:

Maak een 2D-histogram om de relatie tussen twee distributies te vergelijken. Laten we `MaxBodyMass` vergelijken met `MaxLength`. `ggplot2` biedt een ingebouwde manier om convergentie te tonen met behulp van helderdere kleuren:

```r
ggplot(data=birds_filtered_1, aes(x=MaxBodyMass, y=MaxLength) ) +
  geom_bin2d() +scale_fill_continuous(type = "viridis")
```
Er lijkt een verwachte correlatie te zijn tussen deze twee elementen langs een verwachte as, met één bijzonder sterk convergentiepunt:

![2d plot](../../../../../translated_images/nl/2d-plot.c504786f439bd7ebceebf2465c70ca3b124103e06c7ff7214bf24e26f7aec21e.png)

Histogrammen werken standaard goed voor numerieke gegevens. Wat als je distributies wilt zien op basis van tekstgegevens? 
## Verken de dataset voor distributies met behulp van tekstgegevens 

Deze dataset bevat ook goede informatie over de vogelcategorie en zijn geslacht, soort en familie, evenals zijn beschermingsstatus. Laten we deze beschermingsinformatie onderzoeken. Wat is de distributie van de vogels volgens hun beschermingsstatus?

> ✅ In de dataset worden verschillende acroniemen gebruikt om de beschermingsstatus te beschrijven. Deze acroniemen komen van de [IUCN Red List Categories](https://www.iucnredlist.org/), een organisatie die de status van soorten catalogiseert.
> 
> - CR: Kritiek Bedreigd
> - EN: Bedreigd
> - EX: Uitgestorven
> - LC: Minste Zorg
> - NT: Bijna Bedreigd
> - VU: Kwetsbaar

Dit zijn tekstgebaseerde waarden, dus je moet een transformatie uitvoeren om een histogram te maken. Gebruik de filteredBirds dataframe om de beschermingsstatus weer te geven naast de minimale vleugelspanwijdte. Wat zie je?

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

![vleugelspan en beschermingsstatus](../../../../../translated_images/nl/wingspan-conservation-collation.4024e9aa6910866aa82f0c6cb6a6b4b925bd10079e6b0ef8f92eefa5a6792f76.png)

Er lijkt geen goede correlatie te zijn tussen minimale vleugelspanwijdte en beschermingsstatus. Test andere elementen van de dataset met deze methode. Je kunt ook verschillende filters proberen. Vind je enige correlatie?

## Dichtheidsdiagrammen

Je hebt misschien gemerkt dat de histogrammen die we tot nu toe hebben bekeken 'getrapt' zijn en niet soepel in een boog verlopen. Om een vloeiender dichtheidsdiagram te tonen, kun je een dichtheidsplot proberen.

Laten we nu werken met dichtheidsdiagrammen!

```r
ggplot(data = birds_filtered_1, aes(x = MinWingspan)) + 
  geom_density()
```
![dichtheidsdiagram](../../../../../translated_images/nl/density-plot.675ccf865b76c690487fb7f69420a8444a3515f03bad5482886232d4330f5c85.png)

Je kunt zien hoe het diagram het vorige voor minimale vleugelspanwijdte gegevens weerspiegelt; het is gewoon iets vloeiender. Als je die hoekige MaxBodyMass-lijn in het tweede diagram dat je hebt gemaakt opnieuw wilt bekijken, kun je deze heel goed gladstrijken door deze opnieuw te maken met deze methode:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density()
```
![lichaamsmassa dichtheid](../../../../../translated_images/nl/bodymass-smooth.d31ce526d82b0a1f19a073815dea28ecfbe58145ec5337e4ef7e8cdac81120b3.png)

Als je een gladde, maar niet te gladde lijn wilt, bewerk dan de parameter `adjust`: 

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density(adjust = 1/5)
```
![minder gladde lichaamsmassa](../../../../../translated_images/nl/less-smooth-bodymass.10f4db8b683cc17d17b2d33f22405413142004467a1493d416608dafecfdee23.png)

✅ Lees over de beschikbare parameters voor dit type diagram en experimenteer!

Dit type diagram biedt prachtig verklarende visualisaties. Met een paar regels code kun je bijvoorbeeld de maximale lichaamsmassa dichtheid per vogelorde tonen:

```r
ggplot(data=birds_filtered_1,aes(x = MaxBodyMass, fill = Order)) +
  geom_density(alpha=0.5)
```
![lichaamsmassa per orde](../../../../../translated_images/nl/bodymass-per-order.9d2b065dd931b928c839d8cdbee63067ab1ae52218a1b90717f4bc744354f485.png)

## 🚀 Uitdaging

Histogrammen zijn een meer geavanceerd type diagram dan eenvoudige spreidingsdiagrammen, staafdiagrammen of lijndiagrammen. Ga op zoek op het internet naar goede voorbeelden van het gebruik van histogrammen. Hoe worden ze gebruikt, wat tonen ze aan, en in welke velden of gebieden van onderzoek worden ze vaak gebruikt?

## [Quiz na de les](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## Herziening & Zelfstudie

In deze les heb je `ggplot2` gebruikt en ben je begonnen met het maken van meer geavanceerde diagrammen. Doe wat onderzoek naar `geom_density_2d()` een "continue waarschijnlijkheidsdichtheidscurve in één of meer dimensies". Lees de [documentatie](https://ggplot2.tidyverse.org/reference/geom_density_2d.html) om te begrijpen hoe het werkt.

## Opdracht

[Pas je vaardigheden toe](assignment.md)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.