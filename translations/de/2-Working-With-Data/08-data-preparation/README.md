<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3ade580a06b5f04d57cc83a768a8fb77",
  "translation_date": "2025-08-24T20:58:28+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "de"
}
-->
# Arbeiten mit Daten: Datenaufbereitung

|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Datenaufbereitung - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

## [Quiz vor der Vorlesung](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

Je nach Quelle können Rohdaten Inkonsistenzen enthalten, die bei der Analyse und Modellierung Probleme verursachen. Mit anderen Worten, diese Daten können als "schmutzig" kategorisiert werden und müssen bereinigt werden. Diese Lektion konzentriert sich auf Techniken zur Bereinigung und Transformation von Daten, um Herausforderungen wie fehlende, ungenaue oder unvollständige Daten zu bewältigen. Die behandelten Themen nutzen Python und die Pandas-Bibliothek und werden [im Notebook](../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb) in diesem Verzeichnis demonstriert.

## Die Bedeutung der Datenbereinigung

- **Einfachere Nutzung und Wiederverwendung**: Wenn Daten richtig organisiert und normalisiert sind, lassen sie sich leichter durchsuchen, verwenden und mit anderen teilen.

- **Konsistenz**: Datenwissenschaft erfordert oft die Arbeit mit mehreren Datensätzen, bei denen Datensätze aus verschiedenen Quellen zusammengeführt werden müssen. Die Sicherstellung, dass jeder einzelne Datensatz eine gemeinsame Standardisierung aufweist, garantiert, dass die Daten auch nach der Zusammenführung in einem Datensatz nützlich bleiben.

- **Modellgenauigkeit**: Bereinigte Daten verbessern die Genauigkeit der Modelle, die auf ihnen basieren.

## Häufige Ziele und Strategien der Datenbereinigung

- **Einen Datensatz erkunden**: Die Datenexploration, die in einer [späteren Lektion](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing) behandelt wird, kann helfen, Daten zu entdecken, die bereinigt werden müssen. Das visuelle Beobachten von Werten innerhalb eines Datensatzes kann Erwartungen darüber setzen, wie der Rest aussehen wird, oder eine Vorstellung von den Problemen geben, die gelöst werden können. Exploration kann grundlegende Abfragen, Visualisierungen und Stichproben umfassen.

- **Formatierung**: Je nach Quelle können Daten Inkonsistenzen in ihrer Darstellung aufweisen. Dies kann Probleme beim Suchen und Darstellen von Werten verursachen, bei denen sie zwar im Datensatz vorhanden sind, aber nicht korrekt in Visualisierungen oder Abfrageergebnissen dargestellt werden. Häufige Formatierungsprobleme umfassen das Beheben von Leerzeichen, Datumsangaben und Datentypen. Die Behebung von Formatierungsproblemen liegt typischerweise in der Verantwortung der Personen, die die Daten verwenden. Zum Beispiel können sich Standards zur Darstellung von Daten und Zahlen je nach Land unterscheiden.

- **Duplikate**: Daten, die mehr als einmal vorkommen, können ungenaue Ergebnisse liefern und sollten in der Regel entfernt werden. Dies kann häufig auftreten, wenn zwei oder mehr Datensätze zusammengeführt werden. Es gibt jedoch Fälle, in denen Duplikate in zusammengeführten Datensätzen zusätzliche Informationen enthalten können und möglicherweise erhalten bleiben müssen.

- **Fehlende Daten**: Fehlende Daten können zu Ungenauigkeiten sowie schwachen oder verzerrten Ergebnissen führen. Manchmal können diese durch ein "Neuladen" der Daten, das Auffüllen der fehlenden Werte mit Berechnungen und Code wie Python oder einfach durch Entfernen des Wertes und der entsprechenden Daten gelöst werden. Es gibt zahlreiche Gründe, warum Daten fehlen können, und die Maßnahmen zur Behebung dieser fehlenden Werte hängen davon ab, wie und warum sie ursprünglich verloren gegangen sind.

## Informationen über DataFrames erkunden
> **Lernziel:** Am Ende dieses Abschnitts sollten Sie in der Lage sein, allgemeine Informationen über die in pandas-DataFrames gespeicherten Daten zu finden.

Sobald Sie Ihre Daten in pandas geladen haben, befinden sie sich höchstwahrscheinlich in einem DataFrame (siehe die vorherige [Lektion](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) für eine detaillierte Übersicht). Wenn der Datensatz in Ihrem DataFrame jedoch 60.000 Zeilen und 400 Spalten umfasst, wie fangen Sie dann an, sich einen Überblick zu verschaffen? Glücklicherweise bietet [pandas](https://pandas.pydata.org/) einige praktische Werkzeuge, um schnell allgemeine Informationen über einen DataFrame sowie die ersten und letzten Zeilen zu betrachten.

Um diese Funktionalität zu erkunden, importieren wir die Python-Bibliothek scikit-learn und verwenden einen ikonischen Datensatz: den **Iris-Datensatz**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |Kelchblattlänge (cm)|Kelchblattbreite (cm)|Kronblattlänge (cm)|Kronblattbreite (cm)|
|----------------------------------------|--------------------|---------------------|-------------------|--------------------|
|0                                       |5.1                 |3.5                  |1.4                |0.2                 |
|1                                       |4.9                 |3.0                  |1.4                |0.2                 |
|2                                       |4.7                 |3.2                  |1.3                |0.2                 |
|3                                       |4.6                 |3.1                  |1.5                |0.2                 |
|4                                       |5.0                 |3.6                  |1.4                |0.2                 |

- **DataFrame.info**: Zu Beginn wird die Methode `info()` verwendet, um eine Zusammenfassung des Inhalts eines `DataFrame` auszugeben. Schauen wir uns diesen Datensatz an, um zu sehen, was wir haben:
```python
iris_df.info()
```
```
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
dtypes: float64(4)
memory usage: 4.8 KB
```
Aus diesen Informationen wissen wir, dass der *Iris*-Datensatz 150 Einträge in vier Spalten ohne Nullwerte enthält. Alle Daten sind als 64-Bit-Gleitkommazahlen gespeichert.

- **DataFrame.head()**: Um den tatsächlichen Inhalt des `DataFrame` zu überprüfen, verwenden wir die Methode `head()`. Schauen wir uns die ersten Zeilen unseres `iris_df` an:
```python
iris_df.head()
```
```
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
```
- **DataFrame.tail()**: Umgekehrt verwenden wir die Methode `tail()`, um die letzten Zeilen des `DataFrame` zu überprüfen:
```python
iris_df.tail()
```
```
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
145                6.7               3.0                5.2               2.3
146                6.3               2.5                5.0               1.9
147                6.5               3.0                5.2               2.0
148                6.2               3.4                5.4               2.3
149                5.9               3.0                5.1               1.8
```
> **Fazit:** Schon durch das Betrachten der Metadaten eines DataFrame oder der ersten und letzten Werte kann man sich schnell einen Überblick über die Größe, Form und den Inhalt der Daten verschaffen.

## Umgang mit fehlenden Daten
> **Lernziel:** Am Ende dieses Abschnitts sollten Sie wissen, wie Sie Nullwerte in DataFrames ersetzen oder entfernen können.

Die meisten Datensätze, die Sie verwenden möchten (oder müssen), enthalten fehlende Werte. Der Umgang mit fehlenden Daten bringt subtile Kompromisse mit sich, die Ihre endgültige Analyse und reale Ergebnisse beeinflussen können.

Pandas behandelt fehlende Werte auf zwei Arten. Die erste haben Sie bereits in früheren Abschnitten gesehen: `NaN`, oder Not a Number. Dies ist ein spezieller Wert, der Teil der IEEE-Gleitkomma-Spezifikation ist und nur verwendet wird, um fehlende Gleitkommawerte anzuzeigen.

Für fehlende Werte, die keine Gleitkommazahlen sind, verwendet pandas das Python-Objekt `None`. Obwohl es verwirrend erscheinen mag, dass Sie zwei verschiedene Arten von Werten sehen, die im Wesentlichen dasselbe aussagen, gibt es programmatische Gründe für diese Designentscheidung. In der Praxis ermöglicht dieser Ansatz pandas, in den meisten Fällen eine gute Balance zu bieten. Dennoch haben sowohl `None` als auch `NaN` Einschränkungen, die Sie im Hinblick auf ihre Verwendung beachten müssen.

Erfahren Sie mehr über `NaN` und `None` im [Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Nullwerte erkennen**: In `pandas` sind die Methoden `isnull()` und `notnull()` Ihre Hauptwerkzeuge, um Nullwerte zu erkennen. Beide geben boolesche Masken über Ihre Daten zurück. Wir werden `numpy` für `NaN`-Werte verwenden:
```python
import numpy as np

example1 = pd.Series([0, np.nan, '', None])
example1.isnull()
```
```
0    False
1     True
2    False
3     True
dtype: bool
```
Schauen Sie sich die Ausgabe genau an. Überrascht Sie etwas? Während `0` ein arithmetisches Null ist, ist es dennoch eine gültige Ganzzahl, und pandas behandelt es entsprechend. `''` ist etwas subtiler. Obwohl wir es in Abschnitt 1 verwendet haben, um einen leeren Zeichenfolgenwert darzustellen, ist es dennoch ein Zeichenfolgenobjekt und keine Darstellung von Null aus Sicht von pandas.

Nun drehen wir das Ganze um und verwenden diese Methoden so, wie Sie sie in der Praxis verwenden würden. Sie können boolesche Masken direkt als ``Series``- oder ``DataFrame``-Index verwenden, was nützlich ist, wenn Sie mit isolierten fehlenden (oder vorhandenen) Werten arbeiten möchten.

> **Fazit**: Sowohl die Methoden `isnull()` als auch `notnull()` liefern ähnliche Ergebnisse, wenn Sie sie in `DataFrame`s verwenden: Sie zeigen die Ergebnisse und den Index dieser Ergebnisse an, was Ihnen enorm helfen wird, wenn Sie mit Ihren Daten arbeiten.

- **Nullwerte entfernen**: Neben der Identifizierung fehlender Werte bietet pandas eine bequeme Möglichkeit, Nullwerte aus `Series` und `DataFrame`s zu entfernen. (Insbesondere bei großen Datensätzen ist es oft ratsamer, fehlende [NA]-Werte einfach aus Ihrer Analyse zu entfernen, anstatt sie auf andere Weise zu behandeln.) Um dies in Aktion zu sehen, kehren wir zu `example1` zurück:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Beachten Sie, dass dies wie Ihre Ausgabe von `example3[example3.notnull()]` aussehen sollte. Der Unterschied hier ist, dass `dropna` diese fehlenden Werte aus der `Series` `example1` entfernt hat, anstatt nur auf die maskierten Werte zuzugreifen.

Da `DataFrame`s zwei Dimensionen haben, bieten sie mehr Optionen zum Entfernen von Daten.

```python
example2 = pd.DataFrame([[1,      np.nan, 7], 
                         [2,      5,      8], 
                         [np.nan, 6,      9]])
example2
```
|      | 0 | 1 | 2 |
|------|---|---|---|
|0     |1.0|NaN|7  |
|1     |2.0|5.0|8  |
|2     |NaN|6.0|9  |

(Haben Sie bemerkt, dass pandas zwei der Spalten in Gleitkommazahlen umgewandelt hat, um die `NaN`s zu berücksichtigen?)

Sie können keinen einzelnen Wert aus einem `DataFrame` entfernen, daher müssen Sie ganze Zeilen oder Spalten entfernen. Je nachdem, was Sie tun, möchten Sie möglicherweise das eine oder das andere tun, und pandas gibt Ihnen Optionen für beides. Da in der Datenwissenschaft Spalten im Allgemeinen Variablen und Zeilen Beobachtungen darstellen, entfernen Sie eher Zeilen von Daten; die Standardeinstellung für `dropna()` ist, alle Zeilen zu entfernen, die Nullwerte enthalten:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Falls erforderlich, können Sie NA-Werte aus Spalten entfernen. Verwenden Sie `axis=1`, um dies zu tun:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Beachten Sie, dass dies viele Daten entfernen kann, die Sie möglicherweise behalten möchten, insbesondere bei kleineren Datensätzen. Was ist, wenn Sie nur Zeilen oder Spalten entfernen möchten, die mehrere oder sogar alle Nullwerte enthalten? Sie können diese Einstellungen in `dropna` mit den Parametern `how` und `thresh` angeben.

Standardmäßig ist `how='any'` (wenn Sie dies selbst überprüfen oder sehen möchten, welche anderen Parameter die Methode hat, führen Sie `example4.dropna?` in einer Codezelle aus). Sie könnten alternativ `how='all'` angeben, um nur Zeilen oder Spalten zu entfernen, die ausschließlich Nullwerte enthalten. Lassen Sie uns unser Beispiel-`DataFrame` erweitern, um dies in Aktion zu sehen.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

Der Parameter `thresh` gibt Ihnen eine feinere Kontrolle: Sie legen die Anzahl der *nicht-null* Werte fest, die eine Zeile oder Spalte haben muss, um beibehalten zu werden:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Hier wurden die erste und letzte Zeile entfernt, da sie nur zwei nicht-null Werte enthalten.

- **Nullwerte auffüllen**: Je nach Datensatz kann es manchmal sinnvoller sein, Nullwerte durch gültige Werte zu ersetzen, anstatt sie zu entfernen. Sie könnten `isnull` verwenden, um dies direkt zu tun, aber das kann mühsam sein, insbesondere wenn Sie viele Werte auffüllen müssen. Da dies eine so häufige Aufgabe in der Datenwissenschaft ist, bietet pandas `fillna`, das eine Kopie der `Series` oder des `DataFrame` zurückgibt, bei der die fehlenden Werte durch einen von Ihnen gewählten Wert ersetzt werden. Lassen Sie uns eine weitere Beispiel-`Series` erstellen, um zu sehen, wie dies in der Praxis funktioniert.
```python
example3 = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
example3
```
```
a    1.0
b    NaN
c    2.0
d    NaN
e    3.0
dtype: float64
```
Sie können alle Nullwerte durch einen einzigen Wert, wie `0`, ersetzen:
```python
example3.fillna(0)
```
```
a    1.0
b    0.0
c    2.0
d    0.0
e    3.0
dtype: float64
```
Sie können Nullwerte **vorwärts auffüllen**, indem Sie den letzten gültigen Wert verwenden, um eine Null zu ersetzen:
```python
example3.fillna(method='ffill')
```
```
a    1.0
b    1.0
c    2.0
d    2.0
e    3.0
dtype: float64
```
Sie können auch **rückwärts auffüllen**, um den nächsten gültigen Wert rückwärts zu propagieren und eine Null zu ersetzen:
```python
example3.fillna(method='bfill')
```
```
a    1.0
b    2.0
c    2.0
d    3.0
e    3.0
dtype: float64
```
Wie Sie sich denken können, funktioniert dies genauso mit `DataFrame`s, aber Sie können auch eine `axis` angeben, entlang der Nullwerte aufgefüllt werden sollen. Nehmen wir erneut das zuvor verwendete `example2`:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Beachten Sie, dass, wenn ein vorheriger Wert für das Vorwärtsauffüllen nicht verfügbar ist, der Nullwert bestehen bleibt.
> **Wichtig:** Es gibt mehrere Möglichkeiten, mit fehlenden Werten in deinen Datensätzen umzugehen. Die spezifische Strategie, die du anwendest (Entfernen, Ersetzen oder wie du sie ersetzt), sollte von den Besonderheiten der Daten abhängen. Je mehr du mit Datensätzen arbeitest und interagierst, desto besser wirst du ein Gefühl dafür entwickeln, wie man mit fehlenden Werten umgeht.

## Entfernen von doppelten Daten

> **Lernziel:** Am Ende dieses Abschnitts solltest du in der Lage sein, doppelte Werte in DataFrames zu identifizieren und zu entfernen.

Neben fehlenden Daten wirst du in realen Datensätzen häufig auf doppelte Daten stoßen. Glücklicherweise bietet `pandas` eine einfache Möglichkeit, doppelte Einträge zu erkennen und zu entfernen.

- **Identifizieren von Duplikaten: `duplicated`**: Mit der Methode `duplicated` in pandas kannst du doppelte Werte leicht erkennen. Sie gibt eine Boolesche Maske zurück, die anzeigt, ob ein Eintrag in einem `DataFrame` ein Duplikat eines früheren Eintrags ist. Lass uns ein weiteres Beispiel-`DataFrame` erstellen, um dies in Aktion zu sehen.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |letters|numbers|
|------|-------|-------|
|0     |A      |1      |
|1     |B      |2      |
|2     |A      |1      |
|3     |B      |3      |
|4     |B      |3      |

```python
example4.duplicated()
```
```
0    False
1    False
2     True
3    False
4     True
dtype: bool
```
- **Duplikate entfernen: `drop_duplicates`:** gibt einfach eine Kopie der Daten zurück, bei der alle `duplicated`-Werte `False` sind:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Sowohl `duplicated` als auch `drop_duplicates` berücksichtigen standardmäßig alle Spalten, aber du kannst festlegen, dass sie nur eine Teilmenge der Spalten in deinem `DataFrame` untersuchen:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Wichtig:** Das Entfernen von doppelten Daten ist ein wesentlicher Bestandteil fast jedes Data-Science-Projekts. Doppelte Daten können die Ergebnisse deiner Analysen verändern und dir ungenaue Resultate liefern!


## 🚀 Herausforderung

Alle besprochenen Materialien stehen als [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb) zur Verfügung. Zusätzlich gibt es nach jedem Abschnitt Übungen – probiere sie aus!

## [Quiz nach der Vorlesung](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/15)



## Rückblick & Selbststudium

Es gibt viele Möglichkeiten, Daten für Analysen und Modellierungen vorzubereiten, und das Bereinigen der Daten ist ein wichtiger Schritt, der praktische Erfahrung erfordert. Probiere diese Herausforderungen von Kaggle aus, um Techniken zu erkunden, die in dieser Lektion nicht behandelt wurden.

- [Data Cleaning Challenge: Parsing Dates](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Data Cleaning Challenge: Scale and Normalize Data](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Aufgabe

[Bewertung von Daten aus einem Formular](assignment.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.