<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "af6a12015c6e250e500b570a9fa42593",
  "translation_date": "2025-08-24T01:31:57+00:00",
  "source_file": "3-Data-Visualization/11-visualization-proportions/README.md",
  "language_code": "de"
}
-->
# Visualisierung von Proportionen

|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Visualisierung von Proportionen - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

In dieser Lektion wirst du ein anderes, naturbezogenes Datenset verwenden, um Proportionen zu visualisieren, z. B. wie viele verschiedene Pilzarten in einem Datenset über Pilze vorkommen. Lass uns diese faszinierenden Pilze mit einem Datenset erkunden, das von Audubon stammt und Details zu 23 Arten von Lamellenpilzen aus den Familien Agaricus und Lepiota enthält. Du wirst mit schmackhaften Visualisierungen experimentieren wie:

- Tortendiagramme 🥧  
- Donut-Diagramme 🍩  
- Waffeldiagramme 🧇  

> 💡 Ein sehr interessantes Projekt namens [Charticulator](https://charticulator.com) von Microsoft Research bietet eine kostenlose Drag-and-Drop-Oberfläche für Datenvisualisierungen. In einem ihrer Tutorials verwenden sie ebenfalls dieses Pilz-Datenset! So kannst du die Daten erkunden und gleichzeitig die Bibliothek kennenlernen: [Charticulator-Tutorial](https://charticulator.com/tutorials/tutorial4.html).

## [Quiz vor der Lektion](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## Lerne deine Pilze kennen 🍄

Pilze sind sehr interessant. Lass uns ein Datenset importieren, um sie zu untersuchen:

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```  
Eine Tabelle wird ausgegeben, die großartige Daten für die Analyse enthält:

| Klasse    | Hutform   | Hutoberfläche | Hutfarbe  | Druckstellen | Geruch   | Lamellenansatz | Lamellenabstand | Lamellengröße | Lamellenfarbe | Stielform   | Stielbasis | Stieloberfläche über Ring | Stieloberfläche unter Ring | Stielfarbe über Ring | Stielfarbe unter Ring | Schleiertyp | Schleierfarbe | Ringanzahl | Ringtyp   | Sporenabdruckfarbe | Population | Lebensraum |
| --------- | --------- | ------------- | --------- | ------------ | -------- | --------------- | ---------------- | ------------- | ------------- | ----------- | ---------- | ------------------------ | -------------------------- | -------------------- | -------------------- | ----------- | ------------- | ---------- | --------- | ------------------ | ---------- | ---------- |
| Giftig    | Konvex    | Glatt         | Braun     | Druckstellen | Stechend | Frei            | Eng              | Schmal        | Schwarz       | Verdickend  | Gleich     | Glatt                   | Glatt                     | Weiß                 | Weiß                 | Partiell    | Weiß          | Eins       | Hängend   | Schwarz            | Vereinzelte | Urban      |
| Essbar    | Konvex    | Glatt         | Gelb      | Druckstellen | Mandel   | Frei            | Eng              | Breit         | Schwarz       | Verdickend  | Keulenförmig | Glatt                   | Glatt                     | Weiß                 | Weiß                 | Partiell    | Weiß          | Eins       | Hängend   | Braun              | Zahlreich   | Wiesen     |
| Essbar    | Glockenförmig | Glatt      | Weiß      | Druckstellen | Anis     | Frei            | Eng              | Breit         | Braun         | Verdickend  | Keulenförmig | Glatt                   | Glatt                     | Weiß                 | Weiß                 | Partiell    | Weiß          | Eins       | Hängend   | Braun              | Zahlreich   | Wiesen     |
| Giftig    | Konvex    | Schuppig      | Weiß      | Druckstellen | Stechend | Frei            | Eng              | Schmal        | Braun         | Verdickend  | Gleich     | Glatt                   | Glatt                     | Weiß                 | Weiß                 | Partiell    | Weiß          | Eins       | Hängend   | Schwarz            | Vereinzelte | Urban      |

Sofort fällt auf, dass alle Daten textuell sind. Du musst diese Daten umwandeln, um sie in einem Diagramm verwenden zu können. Die meisten Daten sind tatsächlich als Objekte dargestellt:

```python
print(mushrooms.select_dtypes(["object"]).columns)
```  

Die Ausgabe ist:

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```  
Nimm diese Daten und konvertiere die Spalte 'class' in eine Kategorie:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```  

```python
edibleclass=mushrooms.groupby(['class']).count()
edibleclass
```  

Wenn du nun die Pilzdaten ausgibst, siehst du, dass sie nach den Kategorien giftig/essbar gruppiert wurden:

|           | Hutform   | Hutoberfläche | Hutfarbe  | Druckstellen | Geruch | Lamellenansatz | Lamellenabstand | Lamellengröße | Lamellenfarbe | Stielform   | ... | Stieloberfläche unter Ring | Stielfarbe über Ring | Stielfarbe unter Ring | Schleiertyp | Schleierfarbe | Ringanzahl | Ringtyp   | Sporenabdruckfarbe | Population | Lebensraum |
| --------- | --------- | ------------- | --------- | ------------ | ------ | --------------- | ---------------- | ------------- | ------------- | ----------- | --- | -------------------------- | -------------------- | -------------------- | ----------- | ------------- | ---------- | --------- | ------------------ | ---------- | ---------- |
| Klasse    |           |               |           |              |        |                 |                  |               |               |             |     |                            |                      |                      |             |               |            |           |                    |            |            |
| Essbar    | 4208      | 4208          | 4208      | 4208         | 4208   | 4208            | 4208             | 4208          | 4208          | 4208        | ... | 4208                     | 4208                 | 4208                 | 4208        | 4208          | 4208       | 4208      | 4208               | 4208       | 4208       |
| Giftig    | 3916      | 3916          | 3916      | 3916         | 3916   | 3916            | 3916             | 3916          | 3916          | 3916        | ... | 3916                     | 3916                 | 3916                 | 3916        | 3916          | 3916       | 3916      | 3916               | 3916       | 3916       |

Wenn du die Reihenfolge in dieser Tabelle befolgst, um deine Kategorienamen für die Klasse zu erstellen, kannst du ein Tortendiagramm erstellen:

## Torte!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```  
Voilà, ein Tortendiagramm, das die Proportionen dieser Daten entsprechend den beiden Pilzklassen zeigt. Es ist sehr wichtig, die Reihenfolge der Labels korrekt zu setzen, besonders hier, also überprüfe die Reihenfolge, in der das Label-Array erstellt wird!

![Tortendiagramm](../../../../3-Data-Visualization/11-visualization-proportions/images/pie1-wb.png)

## Donuts!

Ein etwas visuell interessanteres Tortendiagramm ist ein Donut-Diagramm, das ein Tortendiagramm mit einem Loch in der Mitte ist. Lass uns unsere Daten auf diese Weise betrachten.

Schau dir die verschiedenen Lebensräume an, in denen Pilze wachsen:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```  
Hier gruppierst du deine Daten nach Lebensraum. Es gibt 7 aufgelistete, also verwende diese als Labels für dein Donut-Diagramm:

```python
labels=['Grasses','Leaves','Meadows','Paths','Urban','Waste','Wood']

plt.pie(habitat['class'], labels=labels,
        autopct='%1.1f%%', pctdistance=0.85)
  
center_circle = plt.Circle((0, 0), 0.40, fc='white')
fig = plt.gcf()

fig.gca().add_artist(center_circle)
  
plt.title('Mushroom Habitats')
  
plt.show()
```  

![Donut-Diagramm](../../../../3-Data-Visualization/11-visualization-proportions/images/donut-wb.png)  

Dieser Code zeichnet ein Diagramm und einen mittleren Kreis und fügt dann diesen mittleren Kreis in das Diagramm ein. Passe die Breite des mittleren Kreises an, indem du `0.40` auf einen anderen Wert änderst.

Donut-Diagramme können auf verschiedene Weise angepasst werden, um die Labels zu verändern. Insbesondere die Labels können für bessere Lesbarkeit hervorgehoben werden. Erfahre mehr in den [Dokumentationen](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut).

Jetzt, da du weißt, wie du deine Daten gruppierst und sie dann als Torte oder Donut darstellst, kannst du andere Diagrammtypen erkunden. Probiere ein Waffeldiagramm, das eine andere Möglichkeit bietet, Mengen zu visualisieren.

## Waffeln!

Ein 'Waffel'-Diagramm ist eine andere Möglichkeit, Mengen als 2D-Array von Quadraten zu visualisieren. Versuche, die verschiedenen Mengen an Pilzhutfarben in diesem Datenset zu visualisieren. Dafür musst du eine Hilfsbibliothek namens [PyWaffle](https://pypi.org/project/pywaffle/) installieren und Matplotlib verwenden:

```python
pip install pywaffle
```  

Wähle einen Abschnitt deiner Daten aus, um ihn zu gruppieren:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```  

Erstelle ein Waffeldiagramm, indem du Labels erstellst und dann deine Daten gruppierst:

```python
import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle
  
data ={'color': ['brown', 'buff', 'cinnamon', 'green', 'pink', 'purple', 'red', 'white', 'yellow'],
    'amount': capcolor['class']
     }
  
df = pd.DataFrame(data)
  
fig = plt.figure(
    FigureClass = Waffle,
    rows = 100,
    values = df.amount,
    labels = list(df.color),
    figsize = (30,30),
    colors=["brown", "tan", "maroon", "green", "pink", "purple", "red", "whitesmoke", "yellow"],
)
```  

Mit einem Waffeldiagramm kannst du die Proportionen der Hutfarben in diesem Pilz-Datenset deutlich erkennen. Interessanterweise gibt es viele grünhütige Pilze!

![Waffeldiagramm](../../../../3-Data-Visualization/11-visualization-proportions/images/waffle.png)

✅ PyWaffle unterstützt Icons innerhalb der Diagramme, die jedes Icon aus [Font Awesome](https://fontawesome.com/) verwenden können. Experimentiere, um ein noch interessanteres Waffeldiagramm mit Icons anstelle von Quadraten zu erstellen.

In dieser Lektion hast du drei Möglichkeiten gelernt, Proportionen zu visualisieren. Zuerst musst du deine Daten in Kategorien gruppieren und dann entscheiden, welche die beste Möglichkeit ist, die Daten darzustellen – Torte, Donut oder Waffel. Alle sind köstlich und bieten dem Nutzer einen sofortigen Überblick über ein Datenset.

## 🚀 Herausforderung

Versuche, diese schmackhaften Diagramme in [Charticulator](https://charticulator.com) nachzubauen.

## [Quiz nach der Lektion](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## Rückblick & Selbststudium

Manchmal ist es nicht offensichtlich, wann man ein Torten-, Donut- oder Waffeldiagramm verwenden sollte. Hier sind einige Artikel zu diesem Thema:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart  

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce  

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm  

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402  

Recherchiere, um mehr Informationen zu dieser kniffligen Entscheidung zu finden.

## Aufgabe

[Probiere es in Excel aus](assignment.md)  

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.