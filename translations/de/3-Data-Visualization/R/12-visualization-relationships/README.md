<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a33c5d4b4156a2b41788d8720b6f724c",
  "translation_date": "2025-08-24T22:46:42+00:00",
  "source_file": "3-Data-Visualization/R/12-visualization-relationships/README.md",
  "language_code": "de"
}
-->
# Visualisierung von Beziehungen: Alles über Honig 🍯

|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Visualisierung von Beziehungen - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

Im Einklang mit dem naturbezogenen Fokus unserer Forschung wollen wir interessante Visualisierungen entdecken, um die Beziehungen zwischen verschiedenen Honigsorten darzustellen, basierend auf einem Datensatz des [United States Department of Agriculture](https://www.nass.usda.gov/About_NASS/index.php).

Dieser Datensatz mit etwa 600 Einträgen zeigt die Honigproduktion in vielen US-Bundesstaaten. So kann man beispielsweise die Anzahl der Bienenvölker, den Ertrag pro Volk, die Gesamtproduktion, die Lagerbestände, den Preis pro Pfund und den Wert des produzierten Honigs in einem bestimmten Bundesstaat von 1998 bis 2012 betrachten, wobei jede Zeile ein Jahr pro Bundesstaat repräsentiert.

Es könnte interessant sein, die Beziehung zwischen der jährlichen Produktion eines Bundesstaates und beispielsweise dem Honigpreis in diesem Bundesstaat zu visualisieren. Alternativ könnte man die Beziehung zwischen den Erträgen pro Volk in verschiedenen Bundesstaaten darstellen. Dieser Zeitraum umfasst das verheerende Phänomen des 'CCD' oder 'Colony Collapse Disorder', das erstmals 2006 beobachtet wurde (http://npic.orst.edu/envir/ccd.html), was diesen Datensatz besonders bedeutsam macht. 🐝

## [Quiz vor der Lektion](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

In dieser Lektion kannst du ggplot2 verwenden, eine Bibliothek, die du bereits kennst, um Beziehungen zwischen Variablen zu visualisieren. Besonders interessant ist die Verwendung der `geom_point`- und `qplot`-Funktionen von ggplot2, die Streu- und Linienplots ermöglichen, um schnell '[statistische Beziehungen](https://ggplot2.tidyverse.org/)' darzustellen. Diese helfen Datenwissenschaftler:innen, besser zu verstehen, wie Variablen miteinander in Beziehung stehen.

## Streudiagramme

Verwende ein Streudiagramm, um zu zeigen, wie sich der Honigpreis Jahr für Jahr in den einzelnen Bundesstaaten entwickelt hat. Mit ggplot2 kannst du mithilfe von `ggplot` und `geom_point` die Daten der Bundesstaaten gruppieren und Datenpunkte für sowohl kategoriale als auch numerische Daten anzeigen.

Beginnen wir mit dem Import der Daten und Seaborn:

```r
honey=read.csv('../../data/honey.csv')
head(honey)
```
Du wirst feststellen, dass die Honigdaten mehrere interessante Spalten enthalten, darunter Jahr und Preis pro Pfund. Lass uns diese Daten, gruppiert nach US-Bundesstaaten, erkunden:

| state | numcol | yieldpercol | totalprod | stocks   | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL    | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ    | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR    | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA    | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO    | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |
| FL    | 230000 | 98          |22540000   | 4508000  | 0.64       | 14426000  | 1998 |

Erstelle ein einfaches Streudiagramm, um die Beziehung zwischen dem Preis pro Pfund Honig und seinem Herkunftsbundesstaat darzustellen. Mache die `y`-Achse hoch genug, um alle Bundesstaaten anzuzeigen:

```r
library(ggplot2)
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(colour = "blue")
```
![scatterplot 1](../../../../../translated_images/de/scatter1.86b8900674d88b26dd3353a83fe604e9ab3722c4680cc40ee9beb452ff02cdea.png)

Zeige nun dieselben Daten mit einem honigfarbenen Farbschema, um zu verdeutlichen, wie sich der Preis im Laufe der Jahre entwickelt hat. Dies kannst du erreichen, indem du den Parameter 'scale_color_gradientn' hinzufügst, um die Veränderung Jahr für Jahr darzustellen:

> ✅ Erfahre mehr über [scale_color_gradientn](https://www.rdocumentation.org/packages/ggplot2/versions/0.9.1/topics/scale_colour_gradientn) – probiere ein schönes Regenbogen-Farbschema aus!

```r
ggplot(honey, aes(x = priceperlb, y = state, color=year)) +
  geom_point()+scale_color_gradientn(colours = colorspace::heat_hcl(7))
```
![scatterplot 2](../../../../../translated_images/de/scatter2.4d1cbc693bad20e2b563888747eb6bdf65b73ce449d903f7cd4068a78502dcff.png)

Mit dieser Farbänderung kannst du deutlich erkennen, dass es im Laufe der Jahre eine starke Preissteigerung pro Pfund Honig gibt. Wenn du beispielsweise einen bestimmten Bundesstaat wie Arizona betrachtest, kannst du ein Muster von Preissteigerungen Jahr für Jahr erkennen, mit wenigen Ausnahmen:

| state | numcol | yieldpercol | totalprod | stocks  | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | ------- | ---------- | --------- | ---- |
| AZ    | 55000  | 60          | 3300000   | 1485000 | 0.64       | 2112000   | 1998 |
| AZ    | 52000  | 62          | 3224000   | 1548000 | 0.62       | 1999000   | 1999 |
| AZ    | 40000  | 59          | 2360000   | 1322000 | 0.73       | 1723000   | 2000 |
| AZ    | 43000  | 59          | 2537000   | 1142000 | 0.72       | 1827000   | 2001 |
| AZ    | 38000  | 63          | 2394000   | 1197000 | 1.08       | 2586000   | 2002 |
| AZ    | 35000  | 72          | 2520000   | 983000  | 1.34       | 3377000   | 2003 |
| AZ    | 32000  | 55          | 1760000   | 774000  | 1.11       | 1954000   | 2004 |
| AZ    | 36000  | 50          | 1800000   | 720000  | 1.04       | 1872000   | 2005 |
| AZ    | 30000  | 65          | 1950000   | 839000  | 0.91       | 1775000   | 2006 |
| AZ    | 30000  | 64          | 1920000   | 902000  | 1.26       | 2419000   | 2007 |
| AZ    | 25000  | 64          | 1600000   | 336000  | 1.26       | 2016000   | 2008 |
| AZ    | 20000  | 52          | 1040000   | 562000  | 1.45       | 1508000   | 2009 |
| AZ    | 24000  | 77          | 1848000   | 665000  | 1.52       | 2809000   | 2010 |
| AZ    | 23000  | 53          | 1219000   | 427000  | 1.55       | 1889000   | 2011 |
| AZ    | 22000  | 46          | 1012000   | 253000  | 1.79       | 1811000   | 2012 |

Eine andere Möglichkeit, diese Entwicklung darzustellen, ist die Verwendung der Größe anstelle von Farben. Für farbenblinde Nutzer:innen könnte dies eine bessere Option sein. Bearbeite deine Visualisierung so, dass die Preissteigerung durch eine Zunahme des Punktumfangs dargestellt wird:

```r
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(aes(size = year),colour = "blue") +
  scale_size_continuous(range = c(0.25, 3))
```
Du kannst sehen, dass die Größe der Punkte allmählich zunimmt.

![scatterplot 3](../../../../../translated_images/de/scatter3.722d21e6f20b3ea2e18339bb9b10d75906126715eb7d5fdc88fe74dcb6d7066a.png)

Ist dies ein einfacher Fall von Angebot und Nachfrage? Aufgrund von Faktoren wie Klimawandel und dem Zusammenbruch von Bienenvölkern – gibt es Jahr für Jahr weniger Honig zu kaufen, und daher steigen die Preise?

Um eine Korrelation zwischen einigen Variablen in diesem Datensatz zu entdecken, lass uns einige Liniendiagramme untersuchen.

## Liniendiagramme

Frage: Gibt es einen klaren Anstieg des Preises pro Pfund Honig Jahr für Jahr? Dies lässt sich am einfachsten durch ein einzelnes Liniendiagramm herausfinden:

```r
qplot(honey$year,honey$priceperlb, geom='smooth', span =0.5, xlab = "year",ylab = "priceperlb")
```
Antwort: Ja, mit einigen Ausnahmen um das Jahr 2003:

![line chart 1](../../../../../translated_images/de/line1.299b576fbb2a59e60a59e7130030f59836891f90302be084e4e8d14da0562e2a.png)

Frage: Gab es im Jahr 2003 auch einen Anstieg des Honigangebots? Was ist, wenn du die Gesamtproduktion Jahr für Jahr betrachtest?

```python
qplot(honey$year,honey$totalprod, geom='smooth', span =0.5, xlab = "year",ylab = "totalprod")
```

![line chart 2](../../../../../translated_images/de/line2.3b18fcda7176ceba5b6689eaaabb817d49c965e986f11cac1ae3f424030c34d8.png)

Antwort: Nicht wirklich. Wenn du die Gesamtproduktion betrachtest, scheint sie in diesem Jahr tatsächlich gestiegen zu sein, obwohl die Honigproduktion im Allgemeinen in diesen Jahren rückläufig ist.

Frage: Was könnte in diesem Fall den Preisanstieg für Honig um das Jahr 2003 verursacht haben?

Um dies herauszufinden, kannst du ein Facet Grid untersuchen.

## Facet Grids

Facet Grids nehmen eine Facette deines Datensatzes (in unserem Fall kannst du 'Jahr' wählen, um zu vermeiden, dass zu viele Facetten erstellt werden). Seaborn kann dann für jede dieser Facetten deiner gewählten x- und y-Koordinaten ein Diagramm erstellen, um den Vergleich zu erleichtern. Fällt das Jahr 2003 in diesem Vergleich auf?

Erstelle ein Facet Grid, indem du `facet_wrap` wie in der [ggplot2-Dokumentation](https://ggplot2.tidyverse.org/reference/facet_wrap.html) empfohlen verwendest.

```r
ggplot(honey, aes(x=yieldpercol, y = numcol,group = 1)) + 
  geom_line() + facet_wrap(vars(year))
```
In dieser Visualisierung kannst du den Ertrag pro Volk und die Anzahl der Völker Jahr für Jahr nebeneinander vergleichen, wobei die Wrap-Einstellung auf 3 Spalten gesetzt ist:

![facet grid](../../../../../translated_images/de/facet.491ad90d61c2a7cc69b50c929f80786c749e38217ccedbf1e22ed8909b65987c.png)

Für diesen Datensatz fällt nichts Besonderes in Bezug auf die Anzahl der Völker und deren Ertrag Jahr für Jahr und Bundesstaat für Bundesstaat auf. Gibt es eine andere Möglichkeit, eine Korrelation zwischen diesen beiden Variablen zu finden?

## Dual-Line-Plots

Versuche ein Mehrlinien-Diagramm, indem du zwei Liniendiagramme übereinander legst, mit R's `par`- und `plot`-Funktion. Wir werden das Jahr auf der x-Achse darstellen und zwei y-Achsen anzeigen. Zeige den Ertrag pro Volk und die Anzahl der Völker übereinander:

```r
par(mar = c(5, 4, 4, 4) + 0.3)              
plot(honey$year, honey$numcol, pch = 16, col = 2,type="l")              
par(new = TRUE)                             
plot(honey$year, honey$yieldpercol, pch = 17, col = 3,              
     axes = FALSE, xlab = "", ylab = "",type="l")
axis(side = 4, at = pretty(range(y2)))      
mtext("colony yield", side = 4, line = 3)   
```
![superimposed plots](../../../../../translated_images/de/dual-line.fc4665f360a54018d7df9bc6abcc26460112e17dcbda18d3b9ae6109b32b36c3.png)

Auch wenn nichts um das Jahr 2003 ins Auge springt, können wir diese Lektion mit einer etwas erfreulicheren Note beenden: Während die Gesamtzahl der Bienenvölker insgesamt abnimmt, stabilisiert sich die Anzahl der Völker, auch wenn ihr Ertrag pro Volk sinkt.

Go, bees, go!

🐝❤️
## 🚀 Herausforderung

In dieser Lektion hast du mehr über die Verwendung von Streudiagrammen und Liniengittern, einschließlich Facet Grids, gelernt. Fordere dich selbst heraus, ein Facet Grid mit einem anderen Datensatz zu erstellen, vielleicht einem, den du in früheren Lektionen verwendet hast. Beachte, wie lange sie zur Erstellung benötigen und wie du darauf achten musst, wie viele Gitter du mit diesen Techniken zeichnen möchtest.
## [Quiz nach der Lektion](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## Rückblick & Selbststudium

Liniendiagramme können einfach oder recht komplex sein. Lies ein wenig in der [ggplot2-Dokumentation](https://ggplot2.tidyverse.org/reference/geom_path.html#:~:text=geom_line()%20connects%20them%20in,which%20cases%20are%20connected%20together) über die verschiedenen Möglichkeiten, wie du sie erstellen kannst. Versuche, die in dieser Lektion erstellten Liniendiagramme mit anderen in der Dokumentation aufgeführten Methoden zu verbessern.
## Aufgabe

[Tauche in den Bienenstock ein](assignment.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.