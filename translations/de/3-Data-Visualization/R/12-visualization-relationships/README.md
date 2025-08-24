<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a33c5d4b4156a2b41788d8720b6f724c",
  "translation_date": "2025-08-24T01:12:59+00:00",
  "source_file": "3-Data-Visualization/R/12-visualization-relationships/README.md",
  "language_code": "de"
}
-->
# Beziehungen visualisieren: Alles über Honig 🍯

|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Beziehungen visualisieren - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

Im Rahmen unseres naturbezogenen Forschungsfokus wollen wir interessante Visualisierungen entdecken, um die Beziehungen zwischen verschiedenen Honigsorten darzustellen, basierend auf einem Datensatz des [United States Department of Agriculture](https://www.nass.usda.gov/About_NASS/index.php).

Dieser Datensatz mit etwa 600 Einträgen zeigt die Honigproduktion in vielen US-Bundesstaaten. So können Sie beispielsweise die Anzahl der Bienenvölker, den Ertrag pro Volk, die Gesamtproduktion, Lagerbestände, den Preis pro Pfund und den Wert des produzierten Honigs in einem bestimmten Bundesstaat von 1998 bis 2012 betrachten, wobei jede Zeile ein Jahr pro Bundesstaat darstellt.

Es wäre interessant, die Beziehung zwischen der jährlichen Produktion eines Bundesstaates und beispielsweise dem Honigpreis in diesem Bundesstaat zu visualisieren. Alternativ könnten Sie die Beziehung zwischen den Erträgen pro Volk in verschiedenen Bundesstaaten darstellen. Dieser Zeitraum umfasst das verheerende 'CCD' oder 'Colony Collapse Disorder', das erstmals 2006 beobachtet wurde (http://npic.orst.edu/envir/ccd.html), was diesen Datensatz besonders relevant macht. 🐝

## [Quiz vor der Lektion](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

In dieser Lektion können Sie ggplot2 verwenden, das Sie bereits kennen, als eine gute Bibliothek zur Visualisierung von Beziehungen zwischen Variablen. Besonders interessant ist die Verwendung der `geom_point`- und `qplot`-Funktion von ggplot2, die Streu- und Linienplots ermöglicht, um schnell '[statistische Beziehungen](https://ggplot2.tidyverse.org/)' zu visualisieren. Dies hilft Datenwissenschaftlern, besser zu verstehen, wie Variablen miteinander in Beziehung stehen.

## Streudiagramme

Verwenden Sie ein Streudiagramm, um zu zeigen, wie sich der Honigpreis Jahr für Jahr in den einzelnen Bundesstaaten entwickelt hat. Mit ggplot2 können Sie mit `ggplot` und `geom_point` die Daten der Bundesstaaten bequem gruppieren und Datenpunkte für sowohl kategorische als auch numerische Daten anzeigen.

Beginnen wir mit dem Import der Daten und Seaborn:

```r
honey=read.csv('../../data/honey.csv')
head(honey)
```
Sie werden feststellen, dass die Honigdaten mehrere interessante Spalten enthalten, darunter Jahr und Preis pro Pfund. Lassen Sie uns diese Daten erkunden, gruppiert nach US-Bundesstaat:

| Bundesstaat | numcol | yieldpercol | totalprod | stocks   | priceperlb | prodvalue | year |
| ----------- | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL          | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ          | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR          | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA          | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO          | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |
| FL          | 230000 | 98          |22540000   | 4508000  | 0.64       | 14426000  | 1998 |

Erstellen Sie ein einfaches Streudiagramm, um die Beziehung zwischen dem Preis pro Pfund Honig und seinem Herkunftsbundesstaat darzustellen. Machen Sie die `y`-Achse hoch genug, um alle Bundesstaaten anzuzeigen:

```r
library(ggplot2)
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(colour = "blue")
```
![Streudiagramm 1](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/scatter1.png)

Zeigen Sie nun dieselben Daten mit einem honigfarbenen Farbschema, um zu zeigen, wie sich der Preis im Laufe der Jahre entwickelt. Sie können dies tun, indem Sie den Parameter 'scale_color_gradientn' hinzufügen, um die Veränderung Jahr für Jahr darzustellen:

> ✅ Erfahren Sie mehr über [scale_color_gradientn](https://www.rdocumentation.org/packages/ggplot2/versions/0.9.1/topics/scale_colour_gradientn) - probieren Sie ein wunderschönes Regenbogen-Farbschema aus!

```r
ggplot(honey, aes(x = priceperlb, y = state, color=year)) +
  geom_point()+scale_color_gradientn(colours = colorspace::heat_hcl(7))
```
![Streudiagramm 2](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/scatter2.png)

Mit dieser Farbänderung können Sie deutlich sehen, dass es im Laufe der Jahre eine starke Entwicklung des Honigpreises pro Pfund gibt. Wenn Sie beispielsweise einen Bundesstaat wie Arizona auswählen, können Sie ein Muster von Preissteigerungen Jahr für Jahr mit wenigen Ausnahmen erkennen:

| Bundesstaat | numcol | yieldpercol | totalprod | stocks  | priceperlb | prodvalue | year |
| ----------- | ------ | ----------- | --------- | ------- | ---------- | --------- | ---- |
| AZ          | 55000  | 60          | 3300000   | 1485000 | 0.64       | 2112000   | 1998 |
| AZ          | 52000  | 62          | 3224000   | 1548000 | 0.62       | 1999000   | 1999 |
| AZ          | 40000  | 59          | 2360000   | 1322000 | 0.73       | 1723000   | 2000 |
| AZ          | 43000  | 59          | 2537000   | 1142000 | 0.72       | 1827000   | 2001 |
| AZ          | 38000  | 63          | 2394000   | 1197000 | 1.08       | 2586000   | 2002 |
| AZ          | 35000  | 72          | 2520000   | 983000  | 1.34       | 3377000   | 2003 |
| AZ          | 32000  | 55          | 1760000   | 774000  | 1.11       | 1954000   | 2004 |
| AZ          | 36000  | 50          | 1800000   | 720000  | 1.04       | 1872000   | 2005 |
| AZ          | 30000  | 65          | 1950000   | 839000  | 0.91       | 1775000   | 2006 |
| AZ          | 30000  | 64          | 1920000   | 902000  | 1.26       | 2419000   | 2007 |
| AZ          | 25000  | 64          | 1600000   | 336000  | 1.26       | 2016000   | 2008 |
| AZ          | 20000  | 52          | 1040000   | 562000  | 1.45       | 1508000   | 2009 |
| AZ          | 24000  | 77          | 1848000   | 665000  | 1.52       | 2809000   | 2010 |
| AZ          | 23000  | 53          | 1219000   | 427000  | 1.55       | 1889000   | 2011 |
| AZ          | 22000  | 46          | 1012000   | 253000  | 1.79       | 1811000   | 2012 |

Eine andere Möglichkeit, diese Entwicklung zu visualisieren, ist die Verwendung von Größe statt Farbe. Für farbenblinde Nutzer könnte dies eine bessere Option sein. Bearbeiten Sie Ihre Visualisierung, um eine Preissteigerung durch eine Zunahme des Punktumfangs darzustellen:

```r
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(aes(size = year),colour = "blue") +
  scale_size_continuous(range = c(0.25, 3))
```
Sie können sehen, wie die Größe der Punkte allmählich zunimmt.

![Streudiagramm 3](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/scatter3.png)

Ist dies ein einfacher Fall von Angebot und Nachfrage? Aufgrund von Faktoren wie Klimawandel und dem Zusammenbruch von Bienenvölkern gibt es Jahr für Jahr weniger Honig zu kaufen, und daher steigen die Preise?

Um eine Korrelation zwischen einigen der Variablen in diesem Datensatz zu entdecken, lassen Sie uns einige Liniendiagramme erkunden.

## Liniendiagramme

Frage: Gibt es einen klaren Anstieg des Honigpreises pro Pfund Jahr für Jahr? Dies können Sie am einfachsten durch ein einzelnes Liniendiagramm herausfinden:

```r
qplot(honey$year,honey$priceperlb, geom='smooth', span =0.5, xlab = "year",ylab = "priceperlb")
```
Antwort: Ja, mit einigen Ausnahmen um das Jahr 2003:

![Liniendiagramm 1](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/line1.png)

Frage: Nun, können wir im Jahr 2003 auch einen Anstieg des Honigangebots sehen? Was passiert, wenn Sie die Gesamtproduktion Jahr für Jahr betrachten?

```python
qplot(honey$year,honey$totalprod, geom='smooth', span =0.5, xlab = "year",ylab = "totalprod")
```

![Liniendiagramm 2](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/line2.png)

Antwort: Nicht wirklich. Wenn Sie die Gesamtproduktion betrachten, scheint sie in diesem Jahr tatsächlich gestiegen zu sein, obwohl die Honigproduktion insgesamt in diesen Jahren rückläufig ist.

Frage: Was könnte in diesem Fall den Preisanstieg für Honig um das Jahr 2003 verursacht haben?

Um dies herauszufinden, können Sie ein Facet Grid erkunden.

## Facet Grids

Facet Grids nehmen eine Facette Ihres Datensatzes (in unserem Fall können Sie 'Jahr' wählen, um zu vermeiden, dass zu viele Facetten erstellt werden). Seaborn kann dann für jede dieser Facetten Ihrer gewählten x- und y-Koordinaten eine Grafik erstellen, um den Vergleich zu erleichtern. Sticht das Jahr 2003 in dieser Art von Vergleich hervor?

Erstellen Sie ein Facet Grid mit `facet_wrap`, wie in der [ggplot2-Dokumentation](https://ggplot2.tidyverse.org/reference/facet_wrap.html) empfohlen.

```r
ggplot(honey, aes(x=yieldpercol, y = numcol,group = 1)) + 
  geom_line() + facet_wrap(vars(year))
```
In dieser Visualisierung können Sie den Ertrag pro Volk und die Anzahl der Bienenvölker Jahr für Jahr nebeneinander vergleichen, mit einer Wrap-Einstellung von 3 für die Spalten:

![Facet Grid](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/facet.png)

Für diesen Datensatz fällt nichts Besonderes in Bezug auf die Anzahl der Bienenvölker und deren Ertrag Jahr für Jahr und Bundesstaat für Bundesstaat auf. Gibt es eine andere Möglichkeit, eine Korrelation zwischen diesen beiden Variablen zu finden?

## Dual-Line-Plots

Versuchen Sie ein mehrzeiliges Diagramm, indem Sie zwei Liniendiagramme übereinander legen, mit R's `par` und `plot`-Funktion. Wir werden das Jahr auf der x-Achse darstellen und zwei y-Achsen anzeigen. Zeigen Sie den Ertrag pro Volk und die Anzahl der Bienenvölker übereinander:

```r
par(mar = c(5, 4, 4, 4) + 0.3)              
plot(honey$year, honey$numcol, pch = 16, col = 2,type="l")              
par(new = TRUE)                             
plot(honey$year, honey$yieldpercol, pch = 17, col = 3,              
     axes = FALSE, xlab = "", ylab = "",type="l")
axis(side = 4, at = pretty(range(y2)))      
mtext("colony yield", side = 4, line = 3)   
```
![Überlagerte Diagramme](../../../../../3-Data-Visualization/R/12-visualization-relationships/images/dual-line.png)

Während nichts um das Jahr 2003 besonders auffällt, können wir diese Lektion mit einer etwas erfreulicheren Note abschließen: Obwohl die Anzahl der Bienenvölker insgesamt abnimmt, stabilisiert sich die Anzahl der Bienenvölker, auch wenn ihr Ertrag pro Volk sinkt.

Go, bees, go!

🐝❤️
## 🚀 Herausforderung

In dieser Lektion haben Sie mehr über andere Anwendungen von Streudiagrammen und Linienrastern, einschließlich Facet Grids, gelernt. Fordern Sie sich selbst heraus, ein Facet Grid mit einem anderen Datensatz zu erstellen, vielleicht einem, den Sie vor diesen Lektionen verwendet haben. Beachten Sie, wie lange es dauert, sie zu erstellen, und wie Sie darauf achten müssen, wie viele Grids Sie mit diesen Techniken zeichnen.

## [Quiz nach der Lektion](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## Überprüfung & Selbststudium

Liniendiagramme können einfach oder ziemlich komplex sein. Lesen Sie ein wenig in der [ggplot2-Dokumentation](https://ggplot2.tidyverse.org/reference/geom_path.html#:~:text=geom_line()%20connects%20them%20in,which%20cases%20are%20connected%20together) über die verschiedenen Möglichkeiten, wie Sie sie erstellen können. Versuchen Sie, die Liniendiagramme, die Sie in dieser Lektion erstellt haben, mit anderen in den Dokumenten aufgeführten Methoden zu verbessern.

## Aufgabe

[Tauchen Sie in den Bienenstock ein](assignment.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.