<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea67c0c40808fd723594de6896c37ccf",
  "translation_date": "2025-08-24T01:09:24+00:00",
  "source_file": "3-Data-Visualization/R/10-visualization-distributions/README.md",
  "language_code": "de"
}
-->
# Visualisierung von Verteilungen

|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Visualisierung von Verteilungen - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

In der vorherigen Lektion hast du einige interessante Fakten über einen Datensatz zu den Vögeln von Minnesota gelernt. Du hast fehlerhafte Daten durch die Visualisierung von Ausreißern entdeckt und die Unterschiede zwischen Vogelkategorien anhand ihrer maximalen Länge betrachtet.

## [Quiz vor der Vorlesung](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## Erkunde den Vogel-Datensatz

Eine weitere Möglichkeit, Daten zu analysieren, besteht darin, ihre Verteilung zu betrachten, also wie die Daten entlang einer Achse organisiert sind. Vielleicht möchtest du beispielsweise die allgemeine Verteilung der maximalen Flügelspannweite oder des maximalen Körpergewichts der Vögel von Minnesota in diesem Datensatz kennenlernen.

Lass uns einige Fakten über die Verteilungen der Daten in diesem Datensatz entdecken. Importiere in deiner R-Konsole `ggplot2` und die Datenbank. Entferne die Ausreißer aus der Datenbank, wie im vorherigen Thema beschrieben.

```r
library(ggplot2)

birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")

birds_filtered <- subset(birds, MaxWingspan < 500)
head(birds_filtered)
```
|      | Name                         | Wissenschaftlicher Name | Kategorie              | Ordnung      | Familie  | Gattung     | Schutzstatus         | MinLänge | MaxLänge | MinKörpergewicht | MaxKörpergewicht | MinFlügelspannweite | MaxFlügelspannweite |
| ---: | :--------------------------- | :---------------------- | :--------------------- | :----------- | :------- | :---------- | :------------------- | --------: | --------: | ----------------: | ----------------: | ------------------: | ------------------: |
|    0 | Schwarzbauch-Pfeifente       | Dendrocygna autumnalis  | Enten/Gänse/Wasservögel | Anseriformes | Anatidae | Dendrocygna | LC                   |        47 |        56 |              652  |             1020  |                76   |                94   |
|    1 | Fuchsrote Pfeifente          | Dendrocygna bicolor     | Enten/Gänse/Wasservögel | Anseriformes | Anatidae | Dendrocygna | LC                   |        45 |        53 |              712  |             1050  |                85   |                93   |
|    2 | Schneegans                   | Anser caerulescens      | Enten/Gänse/Wasservögel | Anseriformes | Anatidae | Anser       | LC                   |        64 |        79 |             2050  |             4050  |               135   |               165   |
|    3 | Zwerggans                    | Anser rossii            | Enten/Gänse/Wasservögel | Anseriformes | Anatidae | Anser       | LC                   |      57.3 |        64 |             1066  |             1567  |               113   |               116   |
|    4 | Blässgans                    | Anser albifrons         | Enten/Gänse/Wasservögel | Anseriformes | Anatidae | Anser       | LC                   |        64 |        81 |             1930  |             3310  |               130   |               165   |

Im Allgemeinen kannst du die Verteilung der Daten schnell mit einem Streudiagramm betrachten, wie wir es in der vorherigen Lektion gemacht haben:

```r
ggplot(data=birds_filtered, aes(x=Order, y=MaxLength,group=1)) +
  geom_point() +
  ggtitle("Max Length per order") + coord_flip()
```
![maximale Länge pro Ordnung](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/max-length-per-order.png)

Dies gibt einen Überblick über die allgemeine Verteilung der Körperlänge pro Vogelordnung, ist jedoch nicht die optimale Darstellung für echte Verteilungen. Diese Aufgabe wird normalerweise durch die Erstellung eines Histogramms gelöst.

## Arbeiten mit Histogrammen

`ggplot2` bietet sehr gute Möglichkeiten, die Datenverteilung mit Histogrammen zu visualisieren. Diese Art von Diagramm ähnelt einem Balkendiagramm, bei dem die Verteilung durch das Auf und Ab der Balken sichtbar wird. Um ein Histogramm zu erstellen, benötigst du numerische Daten. Um ein Histogramm zu erstellen, kannst du ein Diagramm zeichnen, indem du die Art als 'hist' für Histogramm definierst. Dieses Diagramm zeigt die Verteilung des MaxKörpergewichts für den gesamten numerischen Datenbereich des Datensatzes. Indem die Daten in kleinere Intervalle unterteilt werden, kann die Verteilung der Werte angezeigt werden:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=10)+ylab('Frequency')
```
![Verteilung über den gesamten Datensatz](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/distribution-over-the-entire-dataset.png)

Wie du sehen kannst, fallen die meisten der über 400 Vögel in diesem Datensatz in den Bereich unter 2000 für ihr maximales Körpergewicht. Erhalte mehr Einblicke in die Daten, indem du den `bins`-Parameter auf eine höhere Zahl, beispielsweise 30, änderst:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + geom_histogram(bins=30)+ylab('Frequency')
```

![Verteilung mit 30 Bins](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/distribution-30bins.png)

Dieses Diagramm zeigt die Verteilung etwas detaillierter. Ein weniger nach links verzerrtes Diagramm könnte erstellt werden, indem du sicherstellst, dass du nur Daten innerhalb eines bestimmten Bereichs auswählst:

Filtere deine Daten, um nur die Vögel zu erhalten, deren Körpergewicht unter 60 liegt, und zeige 30 `bins`:

```r
birds_filtered_1 <- subset(birds_filtered, MaxBodyMass > 1 & MaxBodyMass < 60)
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=30)+ylab('Frequency')
```

![gefiltertes Histogramm](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/filtered-histogram.png)

✅ Probiere einige andere Filter und Datenpunkte aus. Um die vollständige Verteilung der Daten zu sehen, entferne den `['MaxBodyMass']`-Filter, um beschriftete Verteilungen anzuzeigen.

Das Histogramm bietet auch einige schöne Farb- und Beschriftungsverbesserungen, die du ausprobieren kannst:

Erstelle ein 2D-Histogramm, um die Beziehung zwischen zwei Verteilungen zu vergleichen. Lass uns `MaxBodyMass` mit `MaxLength` vergleichen. `ggplot2` bietet eine eingebaute Möglichkeit, Konvergenzen mit helleren Farben darzustellen:

```r
ggplot(data=birds_filtered_1, aes(x=MaxBodyMass, y=MaxLength) ) +
  geom_bin2d() +scale_fill_continuous(type = "viridis")
```
Es scheint eine erwartete Korrelation zwischen diesen beiden Elementen entlang einer erwarteten Achse zu geben, mit einem besonders starken Konvergenzpunkt:

![2D-Diagramm](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/2d-plot.png)

Histogramme funktionieren standardmäßig gut für numerische Daten. Was ist, wenn du Verteilungen basierend auf Textdaten sehen möchtest? 
## Erkunde den Datensatz für Verteilungen mit Textdaten 

Dieser Datensatz enthält auch gute Informationen über die Vogelkategorie sowie deren Gattung, Art und Familie sowie deren Schutzstatus. Lass uns diese Schutzstatus-Informationen genauer betrachten. Wie ist die Verteilung der Vögel nach ihrem Schutzstatus?

> ✅ In dem Datensatz werden mehrere Abkürzungen verwendet, um den Schutzstatus zu beschreiben. Diese Abkürzungen stammen aus den [IUCN Red List Categories](https://www.iucnredlist.org/), einer Organisation, die den Status von Arten katalogisiert.
> 
> - CR: Kritisch gefährdet
> - EN: Gefährdet
> - EX: Ausgestorben
> - LC: Nicht gefährdet
> - NT: Potenziell gefährdet
> - VU: Verletzlich

Diese Werte sind textbasiert, daher musst du eine Transformation durchführen, um ein Histogramm zu erstellen. Verwende den gefiltertenBirds-Datenrahmen, um dessen Schutzstatus zusammen mit der minimalen Flügelspannweite anzuzeigen. Was siehst du?

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

![Flügelspannweite und Schutzstatus](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/wingspan-conservation-collation.png)

Es scheint keine gute Korrelation zwischen minimaler Flügelspannweite und Schutzstatus zu geben. Teste andere Elemente des Datensatzes mit dieser Methode. Du kannst auch verschiedene Filter ausprobieren. Findest du eine Korrelation?

## Dichte-Diagramme

Du hast vielleicht bemerkt, dass die Histogramme, die wir bisher betrachtet haben, 'gestuft' sind und nicht glatt in einem Bogen verlaufen. Um ein glatteres Dichte-Diagramm zu zeigen, kannst du ein Dichte-Diagramm ausprobieren.

Lass uns jetzt mit Dichte-Diagrammen arbeiten!

```r
ggplot(data = birds_filtered_1, aes(x = MinWingspan)) + 
  geom_density()
```
![Dichte-Diagramm](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/density-plot.png)

Du kannst sehen, wie das Diagramm das vorherige für die minimale Flügelspannweite-Daten widerspiegelt; es ist nur etwas glatter. Wenn du die gezackte MaxKörpergewicht-Linie im zweiten Diagramm, das du erstellt hast, glätten möchtest, könntest du dies sehr gut mit dieser Methode tun:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density()
```
![Körpergewicht-Dichte](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/bodymass-smooth.png)

Wenn du eine glatte, aber nicht zu glatte Linie möchtest, bearbeite den `adjust`-Parameter: 

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density(adjust = 1/5)
```
![weniger glattes Körpergewicht](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/less-smooth-bodymass.png)

✅ Lies über die verfügbaren Parameter für diese Art von Diagramm und experimentiere!

Diese Art von Diagramm bietet wunderschön erklärende Visualisierungen. Mit wenigen Codezeilen kannst du beispielsweise die maximale Körpergewicht-Dichte pro Vogelordnung anzeigen:

```r
ggplot(data=birds_filtered_1,aes(x = MaxBodyMass, fill = Order)) +
  geom_density(alpha=0.5)
```
![Körpergewicht pro Ordnung](../../../../../3-Data-Visualization/R/10-visualization-distributions/images/bodymass-per-order.png)

## 🚀 Herausforderung

Histogramme sind eine anspruchsvollere Art von Diagramm als einfache Streudiagramme, Balkendiagramme oder Liniendiagramme. Suche im Internet nach guten Beispielen für die Verwendung von Histogrammen. Wie werden sie verwendet, was zeigen sie und in welchen Bereichen oder Forschungsgebieten werden sie häufig eingesetzt?

## [Quiz nach der Vorlesung](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## Rückblick & Selbststudium

In dieser Lektion hast du `ggplot2` verwendet und begonnen, anspruchsvollere Diagramme zu erstellen. Recherchiere zu `geom_density_2d()`, einer "kontinuierlichen Wahrscheinlichkeitsdichtekurve in einer oder mehreren Dimensionen". Lies die [Dokumentation](https://ggplot2.tidyverse.org/reference/geom_density_2d.html), um zu verstehen, wie sie funktioniert.

## Aufgabe

[Wende deine Fähigkeiten an](assignment.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.