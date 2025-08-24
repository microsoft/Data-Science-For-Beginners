<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cad419b574d5c35eaa417e9abfdcb0c8",
  "translation_date": "2025-08-24T01:05:22+00:00",
  "source_file": "3-Data-Visualization/12-visualization-relationships/README.md",
  "language_code": "de"
}
-->
# Visualisierung von Beziehungen: Alles über Honig 🍯

|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Visualisierung von Beziehungen - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

Im Rahmen unseres forschungsorientierten Naturfokus entdecken wir interessante Visualisierungen, um die Beziehungen zwischen verschiedenen Honigsorten darzustellen. Grundlage ist ein Datensatz des [United States Department of Agriculture](https://www.nass.usda.gov/About_NASS/index.php). 

Dieser Datensatz mit etwa 600 Einträgen zeigt die Honigproduktion in vielen US-Bundesstaaten. So kann man beispielsweise die Anzahl der Bienenvölker, den Ertrag pro Volk, die Gesamtproduktion, Lagerbestände, den Preis pro Pfund und den Wert des produzierten Honigs in einem bestimmten Bundesstaat von 1998 bis 2012 betrachten, wobei jede Zeile ein Jahr pro Bundesstaat repräsentiert. 

Es wäre interessant, die Beziehung zwischen der jährlichen Produktion eines Bundesstaates und beispielsweise dem Honigpreis in diesem Bundesstaat zu visualisieren. Alternativ könnte man die Beziehung zwischen den Erträgen pro Volk in verschiedenen Bundesstaaten darstellen. Dieser Zeitraum umfasst auch das verheerende 'CCD' oder 'Colony Collapse Disorder', das erstmals 2006 beobachtet wurde (http://npic.orst.edu/envir/ccd.html). Ein bewegender Datensatz zum Studieren. 🐝

## [Quiz vor der Lektion](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

In dieser Lektion kannst du Seaborn verwenden, das du bereits kennst, um Beziehungen zwischen Variablen zu visualisieren. Besonders interessant ist die Verwendung der `relplot`-Funktion von Seaborn, die es ermöglicht, mit Streu- und Liniendiagrammen schnell '[statistische Beziehungen](https://seaborn.pydata.org/tutorial/relational.html?highlight=relationships)' darzustellen. Dies hilft Datenwissenschaftlern, besser zu verstehen, wie Variablen miteinander in Beziehung stehen.

## Streudiagramme

Verwende ein Streudiagramm, um zu zeigen, wie sich der Honigpreis Jahr für Jahr in den einzelnen Bundesstaaten entwickelt hat. Seaborn gruppiert mit `relplot` die Daten der Bundesstaaten und zeigt Datenpunkte sowohl für kategoriale als auch für numerische Daten an. 

Beginnen wir mit dem Import der Daten und Seaborn:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
honey = pd.read_csv('../../data/honey.csv')
honey.head()
```
Du wirst feststellen, dass die Honigdaten mehrere interessante Spalten enthalten, darunter Jahr und Preis pro Pfund. Lass uns diese Daten erkunden, gruppiert nach US-Bundesstaat:

| state | numcol | yieldpercol | totalprod | stocks   | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL    | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ    | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR    | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA    | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO    | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |

Erstelle ein einfaches Streudiagramm, um die Beziehung zwischen dem Preis pro Pfund Honig und seinem Herkunftsbundesstaat darzustellen. Mache die `y`-Achse hoch genug, um alle Bundesstaaten anzuzeigen:

```python
sns.relplot(x="priceperlb", y="state", data=honey, height=15, aspect=.5);
```
![scatterplot 1](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter1.png)

Zeige nun dieselben Daten mit einer honigfarbenen Farbpalette, um zu zeigen, wie sich der Preis im Laufe der Jahre entwickelt hat. Dies kannst du tun, indem du einen 'hue'-Parameter hinzufügst, der die Veränderung Jahr für Jahr anzeigt:

> ✅ Erfahre mehr über die [Farbpaletten, die du in Seaborn verwenden kannst](https://seaborn.pydata.org/tutorial/color_palettes.html) – probiere eine schöne Regenbogen-Farbpalette aus!

```python
sns.relplot(x="priceperlb", y="state", hue="year", palette="YlOrBr", data=honey, height=15, aspect=.5);
```
![scatterplot 2](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter2.png)

Mit dieser Farbänderung kannst du deutlich erkennen, dass es im Laufe der Jahre eine starke Entwicklung des Honigpreises pro Pfund gibt. Wenn du beispielsweise einen bestimmten Bundesstaat wie Arizona betrachtest, kannst du ein Muster von Preissteigerungen Jahr für Jahr mit wenigen Ausnahmen erkennen:

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

Eine andere Möglichkeit, diese Entwicklung zu visualisieren, ist die Verwendung der Größe anstelle von Farbe. Für farbenblinde Nutzer könnte dies eine bessere Option sein. Bearbeite deine Visualisierung, um eine Preissteigerung durch eine Zunahme des Punktumfangs darzustellen:

```python
sns.relplot(x="priceperlb", y="state", size="year", data=honey, height=15, aspect=.5);
```
Du kannst sehen, dass die Größe der Punkte allmählich zunimmt.

![scatterplot 3](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter3.png)

Ist dies ein einfacher Fall von Angebot und Nachfrage? Aufgrund von Faktoren wie Klimawandel und dem Zusammenbruch von Bienenvölkern – gibt es Jahr für Jahr weniger Honig zu kaufen, und daher steigen die Preise?

Um eine Korrelation zwischen einigen Variablen in diesem Datensatz zu entdecken, lass uns einige Liniendiagramme erkunden.

## Liniendiagramme

Frage: Gibt es einen klaren Anstieg des Honigpreises pro Pfund Jahr für Jahr? Dies kannst du am einfachsten durch ein einzelnes Liniendiagramm herausfinden:

```python
sns.relplot(x="year", y="priceperlb", kind="line", data=honey);
```
Antwort: Ja, mit einigen Ausnahmen um das Jahr 2003:

![line chart 1](../../../../3-Data-Visualization/12-visualization-relationships/images/line1.png)

✅ Da Seaborn die Daten um eine Linie aggregiert, zeigt es "die mehrfachen Messungen an jedem x-Wert, indem es den Mittelwert und das 95%-Konfidenzintervall um den Mittelwert herum darstellt". [Quelle](https://seaborn.pydata.org/tutorial/relational.html). Dieses zeitaufwändige Verhalten kann durch Hinzufügen von `ci=None` deaktiviert werden.

Frage: Kann man im Jahr 2003 auch einen Anstieg des Honigangebots erkennen? Was passiert, wenn du die Gesamtproduktion Jahr für Jahr betrachtest?

```python
sns.relplot(x="year", y="totalprod", kind="line", data=honey);
```

![line chart 2](../../../../3-Data-Visualization/12-visualization-relationships/images/line2.png)

Antwort: Nicht wirklich. Wenn du die Gesamtproduktion betrachtest, scheint sie in diesem Jahr tatsächlich gestiegen zu sein, obwohl die Honigproduktion in diesen Jahren insgesamt rückläufig ist.

Frage: Was könnte also den Preisanstieg für Honig um das Jahr 2003 verursacht haben? 

Um dies herauszufinden, kannst du ein Facet Grid erkunden.

## Facet Grids

Facet Grids nehmen eine Facette deines Datensatzes (in unserem Fall kannst du 'Jahr' wählen, um zu vermeiden, dass zu viele Facetten erstellt werden). Seaborn kann dann für jede dieser Facetten deiner gewählten x- und y-Koordinaten ein Diagramm erstellen, um den Vergleich zu erleichtern. Fällt das Jahr 2003 in diesem Vergleich auf?

Erstelle ein Facet Grid, indem du weiterhin `relplot` verwendest, wie in der [Seaborn-Dokumentation](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html?highlight=facetgrid#seaborn.FacetGrid) empfohlen wird.

```python
sns.relplot(
    data=honey, 
    x="yieldpercol", y="numcol",
    col="year", 
    col_wrap=3,
    kind="line"
```
In dieser Visualisierung kannst du den Ertrag pro Volk und die Anzahl der Völker Jahr für Jahr nebeneinander vergleichen, mit einer Wrap-Einstellung von 3 für die Spalten:

![facet grid](../../../../3-Data-Visualization/12-visualization-relationships/images/facet.png)

Für diesen Datensatz fällt nichts Besonderes in Bezug auf die Anzahl der Völker und deren Ertrag Jahr für Jahr und Bundesstaat für Bundesstaat auf. Gibt es eine andere Möglichkeit, eine Korrelation zwischen diesen beiden Variablen zu finden?

## Dual-Line-Diagramme

Versuche ein Mehrlinien-Diagramm, indem du zwei Liniendiagramme übereinanderlegst, Seaborns 'despine' verwendest, um die oberen und rechten Achsen zu entfernen, und `ax.twinx` [abgeleitet von Matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html) nutzt. Twinx ermöglicht es einem Diagramm, die x-Achse zu teilen und zwei y-Achsen anzuzeigen. Zeige also den Ertrag pro Volk und die Anzahl der Völker übereinandergelegt an:

```python
fig, ax = plt.subplots(figsize=(12,6))
lineplot = sns.lineplot(x=honey['year'], y=honey['numcol'], data=honey, 
                        label = 'Number of bee colonies', legend=False)
sns.despine()
plt.ylabel('# colonies')
plt.title('Honey Production Year over Year');

ax2 = ax.twinx()
lineplot2 = sns.lineplot(x=honey['year'], y=honey['yieldpercol'], ax=ax2, color="r", 
                         label ='Yield per colony', legend=False) 
sns.despine(right=False)
plt.ylabel('colony yield')
ax.figure.legend();
```
![superimposed plots](../../../../3-Data-Visualization/12-visualization-relationships/images/dual-line.png)

Auch wenn um das Jahr 2003 nichts ins Auge springt, können wir diese Lektion mit einer etwas erfreulicheren Note beenden: Während die Anzahl der Völker insgesamt abnimmt, stabilisiert sich die Anzahl der Völker, auch wenn ihr Ertrag pro Volk sinkt.

Go, bees, go!

🐝❤️
## 🚀 Herausforderung

In dieser Lektion hast du mehr über die Verwendung von Streudiagrammen und Linienrastern, einschließlich Facet Grids, gelernt. Fordere dich selbst heraus, ein Facet Grid mit einem anderen Datensatz zu erstellen, vielleicht einem, den du in früheren Lektionen verwendet hast. Beachte, wie lange sie zur Erstellung benötigen und wie du darauf achten musst, wie viele Grids du mit diesen Techniken zeichnen möchtest.
## [Quiz nach der Lektion](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## Rückblick & Selbststudium

Liniendiagramme können einfach oder recht komplex sein. Lies ein wenig in der [Seaborn-Dokumentation](https://seaborn.pydata.org/generated/seaborn.lineplot.html) über die verschiedenen Möglichkeiten, wie du sie erstellen kannst. Versuche, die Liniendiagramme, die du in dieser Lektion erstellt hast, mit anderen in der Dokumentation aufgeführten Methoden zu verbessern.
## Aufgabe

[Abtauchen in den Bienenstock](assignment.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.