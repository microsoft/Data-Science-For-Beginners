<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "47028abaaafa2bcb1079702d20569066",
  "translation_date": "2025-08-24T22:58:08+00:00",
  "source_file": "3-Data-Visualization/R/11-visualization-proportions/README.md",
  "language_code": "de"
}
-->
# Visualisierung von Proportionen

|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Visualisierung von Proportionen - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

In dieser Lektion wirst du ein naturbezogenes Datenset verwenden, um Proportionen zu visualisieren, wie z. B. die Anzahl der verschiedenen Pilzarten in einem Datenset über Pilze. Lass uns diese faszinierenden Pilze mit einem Datenset erkunden, das von Audubon stammt und Details zu 23 Arten von Lamellenpilzen aus den Familien Agaricus und Lepiota enthält. Du wirst mit köstlichen Visualisierungen experimentieren, wie:

- Tortendiagramme 🥧
- Donut-Diagramme 🍩
- Waffel-Diagramme 🧇

> 💡 Ein sehr interessantes Projekt namens [Charticulator](https://charticulator.com) von Microsoft Research bietet eine kostenlose Drag-and-Drop-Oberfläche für Datenvisualisierungen. In einem ihrer Tutorials verwenden sie ebenfalls dieses Pilz-Datenset! Du kannst also die Daten erkunden und gleichzeitig die Bibliothek kennenlernen: [Charticulator-Tutorial](https://charticulator.com/tutorials/tutorial4.html).

## [Quiz vor der Lektion](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## Lerne deine Pilze kennen 🍄

Pilze sind sehr interessant. Lass uns ein Datenset importieren, um sie zu untersuchen:

```r
mushrooms = read.csv('../../data/mushrooms.csv')
head(mushrooms)
```
Eine Tabelle wird ausgegeben, die großartige Daten für die Analyse enthält:

| Klasse     | Hutform   | Hutoberfläche | Hutfarbe  | Druckstellen | Geruch   | Lamellenansatz | Lamellenabstand | Lamellengröße | Lamellenfarbe | Stielform   | Stielbasis | Stieloberfläche über dem Ring | Stieloberfläche unter dem Ring | Stielfarbe über dem Ring | Stielfarbe unter dem Ring | Schleierart | Schleierfarbe | Ringanzahl | Ringart   | Sporenabdruckfarbe | Population | Lebensraum |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Giftig    | Konvex    | Glatt       | Braun     | Druckstellen | Stechend | Frei            | Eng          | Schmal    | Schwarz    | Vergrößernd | Gleichmäßig | Glatt                   | Glatt                   | Weiß                   | Weiß                   | Teilweise | Weiß       | Eins        | Hängend   | Schwarz           | Vereinzelt | Urban   |
| Essbar    | Konvex    | Glatt       | Gelb      | Druckstellen | Mandel  | Frei            | Eng          | Breit     | Schwarz    | Vergrößernd | Keulenförmig | Glatt                   | Glatt                   | Weiß                   | Weiß                   | Teilweise | Weiß       | Eins        | Hängend   | Braun             | Zahlreich  | Gräser  |
| Essbar    | Glockenförmig | Glatt   | Weiß      | Druckstellen | Anis    | Frei            | Eng          | Breit     | Braun      | Vergrößernd | Keulenförmig | Glatt                   | Glatt                   | Weiß                   | Weiß                   | Teilweise | Weiß       | Eins        | Hängend   | Braun             | Zahlreich  | Wiesen  |
| Giftig    | Konvex    | Schuppig    | Weiß      | Druckstellen | Stechend | Frei            | Eng          | Schmal    | Braun      | Vergrößernd | Gleichmäßig | Glatt                   | Glatt                   | Weiß                   | Weiß                   | Teilweise | Weiß       | Eins        | Hängend   | Schwarz           | Vereinzelt | Urban   |
| Essbar    | Konvex    | Glatt       | Grün      | Keine Druckstellen | Kein Geruch | Frei | Gedrängt | Breit | Schwarz | Verjüngend | Gleichmäßig | Glatt | Glatt | Weiß | Weiß | Teilweise | Weiß | Eins | Vergänglich | Braun | Reichlich | Gräser |
| Essbar    | Konvex    | Schuppig    | Gelb      | Druckstellen | Mandel  | Frei | Eng | Breit | Braun | Vergrößernd | Keulenförmig | Glatt | Glatt | Weiß | Weiß | Teilweise | Weiß | Eins | Hängend | Schwarz | Zahlreich | Gräser |

Sofort fällt auf, dass alle Daten textuell sind. Du musst diese Daten umwandeln, um sie in einem Diagramm verwenden zu können. Tatsächlich sind die meisten Daten als Objekt dargestellt:

```r
names(mushrooms)
```

Die Ausgabe ist:

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
Nimm diese Daten und konvertiere die Spalte 'Klasse' in eine Kategorie:

```r
library(dplyr)
grouped=mushrooms %>%
  group_by(class) %>%
  summarise(count=n())
```

Wenn du nun die Pilzdaten ausgibst, siehst du, dass sie nach den Kategorien giftig/essbar gruppiert wurden:
```r
View(grouped)
```

| Klasse | Anzahl |
| --------- | --------- |
| Essbar   | 4208 |
| Giftig   | 3916 |

Wenn du die Reihenfolge in dieser Tabelle befolgst, um deine Kategorien für die Klasse zu erstellen, kannst du ein Tortendiagramm erstellen.

## Torte!

```r
pie(grouped$count,grouped$class, main="Edible?")
```
Voila, ein Tortendiagramm, das die Proportionen dieser Daten entsprechend den beiden Pilzklassen zeigt. Es ist sehr wichtig, die Reihenfolge der Labels korrekt zu setzen, besonders hier, also überprüfe unbedingt die Reihenfolge, in der das Label-Array erstellt wird!

![Tortendiagramm](../../../../../translated_images/de/pie1-wb.685df063673751f4b0b82127f7a52c7f9a920192f22ae61ad28412ba9ace97bf.png)

## Donuts!

Ein optisch etwas interessanteres Tortendiagramm ist ein Donut-Diagramm, ein Tortendiagramm mit einem Loch in der Mitte. Lass uns unsere Daten mit dieser Methode betrachten.

Schau dir die verschiedenen Lebensräume an, in denen Pilze wachsen:

```r
library(dplyr)
habitat=mushrooms %>%
  group_by(habitat) %>%
  summarise(count=n())
View(habitat)
```
Die Ausgabe ist:
| Lebensraum | Anzahl |
| --------- | --------- |
| Gräser    | 2148 |
| Blätter   | 832 |
| Wiesen    | 292 |
| Wege      | 1144 |
| Urban     | 368 |
| Abfall    | 192 |
| Holz      | 3148 |

Hier gruppierst du deine Daten nach Lebensraum. Es gibt 7 gelistete Lebensräume, also verwende diese als Labels für dein Donut-Diagramm:

```r
library(ggplot2)
library(webr)
PieDonut(habitat, aes(habitat, count=count))
```

![Donut-Diagramm](../../../../../translated_images/de/donut-wb.34e6fb275da9d834c2205145e39a3de9b6878191dcdba6f7a9e85f4b520449bc.png)

Dieser Code verwendet die beiden Bibliotheken ggplot2 und webr. Mit der PieDonut-Funktion der webr-Bibliothek können wir ein Donut-Diagramm einfach erstellen!

Donut-Diagramme in R können auch nur mit der ggplot2-Bibliothek erstellt werden. Du kannst mehr darüber [hier](https://www.r-graph-gallery.com/128-ring-or-donut-plot.html) erfahren und es selbst ausprobieren.

Jetzt, da du weißt, wie du deine Daten gruppierst und sie als Torte oder Donut darstellst, kannst du andere Diagrammtypen erkunden. Probiere ein Waffel-Diagramm aus, das eine andere Möglichkeit bietet, Mengen darzustellen.

## Waffeln!

Ein 'Waffel'-Diagramm ist eine andere Möglichkeit, Mengen als 2D-Array von Quadraten zu visualisieren. Versuche, die verschiedenen Mengen von Pilzhutfarben in diesem Datenset zu visualisieren. Dazu musst du eine Hilfsbibliothek namens [waffle](https://cran.r-project.org/web/packages/waffle/waffle.pdf) installieren und sie verwenden, um deine Visualisierung zu erstellen:

```r
install.packages("waffle", repos = "https://cinc.rud.is")
```

Wähle einen Abschnitt deiner Daten aus, um ihn zu gruppieren:

```r
library(dplyr)
cap_color=mushrooms %>%
  group_by(cap.color) %>%
  summarise(count=n())
View(cap_color)
```

Erstelle ein Waffel-Diagramm, indem du Labels erstellst und dann deine Daten gruppierst:

```r
library(waffle)
names(cap_color$count) = paste0(cap_color$cap.color)
waffle((cap_color$count/10), rows = 7, title = "Waffle Chart")+scale_fill_manual(values=c("brown", "#F0DC82", "#D2691E", "green", 
                                                                                     "pink", "purple", "red", "grey", 
                                                                                     "yellow","white"))
```

Mit einem Waffel-Diagramm kannst du die Proportionen der Hutfarben in diesem Pilz-Datenset deutlich sehen. Interessanterweise gibt es viele Pilze mit grünen Hüten!

![Waffel-Diagramm](../../../../../translated_images/de/waffle.aaa75c5337735a6ef32ace0ffb6506ef49e5aefe870ffd72b1bb080f4843c217.png)

In dieser Lektion hast du drei Möglichkeiten gelernt, Proportionen zu visualisieren. Zuerst musst du deine Daten in Kategorien gruppieren und dann entscheiden, welche die beste Möglichkeit ist, die Daten darzustellen - Torte, Donut oder Waffel. Alle sind köstlich und bieten dem Benutzer einen sofortigen Überblick über ein Datenset.

## 🚀 Herausforderung

Versuche, diese köstlichen Diagramme in [Charticulator](https://charticulator.com) nachzubilden.

## [Quiz nach der Lektion](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## Rückblick & Selbststudium

Manchmal ist es nicht offensichtlich, wann man ein Torten-, Donut- oder Waffel-Diagramm verwenden sollte. Hier sind einige Artikel zu diesem Thema:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Recherchiere, um mehr Informationen zu dieser schwierigen Entscheidung zu finden.

## Aufgabe

[Probiere es in Excel aus](assignment.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.