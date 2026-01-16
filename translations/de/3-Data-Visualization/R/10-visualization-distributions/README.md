<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea67c0c40808fd723594de6896c37ccf",
  "translation_date": "2025-08-24T22:43:18+00:00",
  "source_file": "3-Data-Visualization/R/10-visualization-distributions/README.md",
  "language_code": "de"
}
-->
# Visualisierung von Verteilungen

|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Visualisierung von Verteilungen - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

In der vorherigen Lektion hast du einige interessante Fakten über einen Datensatz zu den Vögeln von Minnesota gelernt. Du hast fehlerhafte Daten durch die Visualisierung von Ausreißern entdeckt und die Unterschiede zwischen Vogelkategorien anhand ihrer maximalen Länge betrachtet.

## [Quiz vor der Lektion](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## Erkunde den Vogeldatensatz

Eine weitere Möglichkeit, Daten zu analysieren, besteht darin, ihre Verteilung zu betrachten, also wie die Daten entlang einer Achse organisiert sind. Vielleicht möchtest du beispielsweise die allgemeine Verteilung der maximalen Flügelspannweite oder der maximalen Körpermasse der Vögel von Minnesota in diesem Datensatz untersuchen.

Lass uns einige Fakten über die Verteilungen der Daten in diesem Datensatz entdecken. Importiere in deiner R-Konsole `ggplot2` und die Datenbank. Entferne die Ausreißer aus der Datenbank, wie im vorherigen Thema beschrieben.

```r
library(ggplot2)

birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")

birds_filtered <- subset(birds, MaxWingspan < 500)
head(birds_filtered)
```
|      | Name                         | Wissenschaftlicher Name | Kategorie             | Ordnung      | Familie  | Gattung     | Schutzstatus         | MinLänge | MaxLänge | MinKörpermasse | MaxKörpermasse | MinFlügelspannweite | MaxFlügelspannweite |
| ---: | :--------------------------- | :---------------------- | :-------------------- | :----------- | :------- | :---------- | :------------------- | --------: | --------: | -------------: | -------------: | ------------------: | ------------------: |
|    0 | Schwarzbauch-Pfeifgans       | Dendrocygna autumnalis  | Enten/Gänse/Wasservögel | Anseriformes | Anatidae | Dendrocygna | LC                   |        47 |        56 |           652  |          1020  |                76   |                94   |
|    1 | Fuchsrote Pfeifgans          | Dendrocygna bicolor     | Enten/Gänse/Wasservögel | Anseriformes | Anatidae | Dendrocygna | LC                   |        45 |        53 |           712  |          1050  |                85   |                93   |
|    2 | Schneegans                   | Anser caerulescens      | Enten/Gänse/Wasservögel | Anseriformes | Anatidae | Anser       | LC                   |        64 |        79 |          2050  |          4050  |               135   |               165   |
|    3 | Zwerggans                    | Anser rossii            | Enten/Gänse/Wasservögel | Anseriformes | Anatidae | Anser       | LC                   |      57.3 |        64 |          1066  |          1567  |               113   |               116   |
|    4 | Blässgans                    | Anser albifrons         | Enten/Gänse/Wasservögel | Anseriformes | Anatidae | Anser       | LC                   |        64 |        81 |          1930  |          3310  |               130   |               165   |

Im Allgemeinen kannst du die Verteilung der Daten schnell mit einem Streudiagramm betrachten, wie wir es in der vorherigen Lektion gemacht haben:

```r
ggplot(data=birds_filtered, aes(x=Order, y=MaxLength,group=1)) +
  geom_point() +
  ggtitle("Max Length per order") + coord_flip()
```
![max Länge pro Ordnung](../../../../../translated_images/de/max-length-per-order.e5b283d952c78c12b091307c5d3cf67132dad6fefe80a073353b9dc5c2bd3eb8.png)

Dies gibt einen Überblick über die allgemeine Verteilung der Körperlänge pro Vogelordnung, ist jedoch nicht die optimale Methode, um echte Verteilungen darzustellen. Diese Aufgabe wird normalerweise durch die Erstellung eines Histogramms gelöst.

## Arbeiten mit Histogrammen

`ggplot2` bietet sehr gute Möglichkeiten, die Datenverteilung mit Histogrammen zu visualisieren. Diese Art von Diagramm ähnelt einem Balkendiagramm, bei dem die Verteilung durch das Ansteigen und Abfallen der Balken sichtbar wird. Um ein Histogramm zu erstellen, benötigst du numerische Daten. Um ein Histogramm zu erstellen, kannst du ein Diagramm mit der Art 'hist' für Histogramm zeichnen. Dieses Diagramm zeigt die Verteilung der MaxKörpermasse für den gesamten numerischen Datenbereich des Datensatzes. Indem die Daten in kleinere Intervalle unterteilt werden, kann die Verteilung der Werte dargestellt werden:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=10)+ylab('Frequency')
```
![Verteilung über den gesamten Datensatz](../../../../../translated_images/de/distribution-over-the-entire-dataset.d22afd3fa96be854e4c82213fedec9e3703cba753d07fad4606aadf58cf7e78e.png)

Wie du sehen kannst, fallen die meisten der über 400 Vögel in diesem Datensatz in den Bereich unter 2000 für ihre maximale Körpermasse. Erhalte mehr Einblicke in die Daten, indem du den `bins`-Parameter auf eine höhere Zahl, z. B. 30, änderst:

```r
ggplot(data = birds_filtered, aes(x = MaxBodyMass)) + geom_histogram(bins=30)+ylab('Frequency')
```

![Verteilung-30bins](../../../../../translated_images/de/distribution-30bins.6a3921ea7a421bf71f06bf5231009e43d1146f1b8da8dc254e99b5779a4983e5.png)

Dieses Diagramm zeigt die Verteilung etwas detaillierter. Ein weniger nach links verzerrtes Diagramm könnte erstellt werden, indem du sicherstellst, dass du nur Daten innerhalb eines bestimmten Bereichs auswählst:

Filtere deine Daten, um nur die Vögel zu erhalten, deren Körpermasse unter 60 liegt, und zeige 30 `bins`:

```r
birds_filtered_1 <- subset(birds_filtered, MaxBodyMass > 1 & MaxBodyMass < 60)
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_histogram(bins=30)+ylab('Frequency')
```

![gefiltertes Histogramm](../../../../../translated_images/de/filtered-histogram.6bf5d2bfd82533220e1bd4bc4f7d14308f43746ed66721d9ec8f460732be6674.png)

✅ Probiere einige andere Filter und Datenpunkte aus. Um die vollständige Verteilung der Daten zu sehen, entferne den `['MaxBodyMass']`-Filter, um beschriftete Verteilungen anzuzeigen.

Das Histogramm bietet auch einige schöne Farb- und Beschriftungsoptionen, die du ausprobieren kannst:

Erstelle ein 2D-Histogramm, um die Beziehung zwischen zwei Verteilungen zu vergleichen. Lass uns `MaxBodyMass` mit `MaxLength` vergleichen. `ggplot2` bietet eine integrierte Möglichkeit, Konvergenzen mit helleren Farben darzustellen:

```r
ggplot(data=birds_filtered_1, aes(x=MaxBodyMass, y=MaxLength) ) +
  geom_bin2d() +scale_fill_continuous(type = "viridis")
```
Es scheint eine erwartete Korrelation zwischen diesen beiden Elementen entlang einer erwarteten Achse zu geben, mit einem besonders starken Konvergenzpunkt:

![2D-Diagramm](../../../../../translated_images/de/2d-plot.c504786f439bd7ebceebf2465c70ca3b124103e06c7ff7214bf24e26f7aec21e.png)

Histogramme funktionieren standardmäßig gut für numerische Daten. Was ist, wenn du Verteilungen basierend auf Textdaten sehen möchtest?  
## Erkunde den Datensatz nach Verteilungen mit Textdaten

Dieser Datensatz enthält auch gute Informationen über die Vogelkategorie sowie deren Gattung, Art und Familie sowie deren Schutzstatus. Lass uns diese Schutzstatus-Informationen genauer betrachten. Wie ist die Verteilung der Vögel nach ihrem Schutzstatus?

> ✅ Im Datensatz werden mehrere Abkürzungen verwendet, um den Schutzstatus zu beschreiben. Diese Abkürzungen stammen von den [IUCN Red List Categories](https://www.iucnredlist.org/), einer Organisation, die den Status von Arten katalogisiert.
> 
> - CR: Kritisch gefährdet
> - EN: Gefährdet
> - EX: Ausgestorben
> - LC: Geringste Sorge
> - NT: Potenziell gefährdet
> - VU: Verletzlich

Da es sich um textbasierte Werte handelt, musst du eine Transformation durchführen, um ein Histogramm zu erstellen. Verwende den `filteredBirds`-Dataframe, um den Schutzstatus zusammen mit der minimalen Flügelspannweite anzuzeigen. Was siehst du?

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

![Flügelspannweite und Schutzstatus](../../../../../translated_images/de/wingspan-conservation-collation.4024e9aa6910866aa82f0c6cb6a6b4b925bd10079e6b0ef8f92eefa5a6792f76.png)

Es scheint keine gute Korrelation zwischen minimaler Flügelspannweite und Schutzstatus zu geben. Teste andere Elemente des Datensatzes mit dieser Methode. Kannst du eine Korrelation finden?

## Dichteplots

Vielleicht ist dir aufgefallen, dass die Histogramme, die wir bisher betrachtet haben, 'stufig' sind und nicht fließend in einem Bogen verlaufen. Um ein glatteres Dichtediagramm zu zeigen, kannst du einen Dichteplot ausprobieren.

Lass uns jetzt mit Dichteplots arbeiten!

```r
ggplot(data = birds_filtered_1, aes(x = MinWingspan)) + 
  geom_density()
```
![Dichteplot](../../../../../translated_images/de/density-plot.675ccf865b76c690487fb7f69420a8444a3515f03bad5482886232d4330f5c85.png)

Du kannst sehen, wie der Plot das vorherige Diagramm für die minimale Flügelspannweite widerspiegelt; es ist nur etwas glatter. Wenn du die gezackte MaxKörpermasse-Linie im zweiten Diagramm, das du erstellt hast, glätten möchtest, könntest du dies sehr gut mit dieser Methode tun:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density()
```
![Körpermasse-Dichte](../../../../../translated_images/de/bodymass-smooth.d31ce526d82b0a1f19a073815dea28ecfbe58145ec5337e4ef7e8cdac81120b3.png)

Wenn du eine glatte, aber nicht zu glatte Linie möchtest, bearbeite den `adjust`-Parameter:

```r
ggplot(data = birds_filtered_1, aes(x = MaxBodyMass)) + 
  geom_density(adjust = 1/5)
```
![weniger glatte Körpermasse](../../../../../translated_images/de/less-smooth-bodymass.10f4db8b683cc17d17b2d33f22405413142004467a1493d416608dafecfdee23.png)

✅ Lies über die verfügbaren Parameter für diesen Diagrammtyp und experimentiere!

Diese Art von Diagramm bietet wunderschön erklärende Visualisierungen. Mit nur wenigen Codezeilen kannst du beispielsweise die maximale Körpermassendichte pro Vogelordnung anzeigen:

```r
ggplot(data=birds_filtered_1,aes(x = MaxBodyMass, fill = Order)) +
  geom_density(alpha=0.5)
```
![Körpermasse pro Ordnung](../../../../../translated_images/de/bodymass-per-order.9d2b065dd931b928c839d8cdbee63067ab1ae52218a1b90717f4bc744354f485.png)

## 🚀 Herausforderung

Histogramme sind eine anspruchsvollere Art von Diagrammen als einfache Streudiagramme, Balkendiagramme oder Liniendiagramme. Suche im Internet nach guten Beispielen für die Verwendung von Histogrammen. Wie werden sie verwendet, was zeigen sie und in welchen Bereichen oder Forschungsfeldern werden sie häufig eingesetzt?

## [Quiz nach der Lektion](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## Rückblick & Selbststudium

In dieser Lektion hast du `ggplot2` verwendet und begonnen, anspruchsvollere Diagramme zu erstellen. Recherchiere zu `geom_density_2d()`, einer "kontinuierlichen Wahrscheinlichkeitsdichtekurve in einer oder mehreren Dimensionen". Lies die [Dokumentation](https://ggplot2.tidyverse.org/reference/geom_density_2d.html), um zu verstehen, wie es funktioniert.

## Aufgabe

[Wende deine Fähigkeiten an](assignment.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.