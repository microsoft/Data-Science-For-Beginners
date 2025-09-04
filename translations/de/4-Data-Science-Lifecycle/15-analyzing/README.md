<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a167aa0bfb1c46ece1b3d21ae939cc0d",
  "translation_date": "2025-09-04T14:10:01+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "de"
}
-->
# Der Lebenszyklus der Datenwissenschaft: Analysieren

|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Lebenszyklus der Datenwissenschaft: Analysieren - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

## Quiz vor der Vorlesung

## [Quiz vor der Vorlesung](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

Das Analysieren im Lebenszyklus der Daten bestätigt, dass die Daten die gestellten Fragen beantworten oder ein bestimmtes Problem lösen können. Dieser Schritt konzentriert sich auch darauf, zu bestätigen, dass ein Modell diese Fragen und Probleme korrekt adressiert. Diese Lektion konzentriert sich auf die explorative Datenanalyse (EDA), Techniken zur Definition von Merkmalen und Beziehungen innerhalb der Daten, die zur Vorbereitung der Daten für die Modellierung verwendet werden können.

Wir verwenden ein Beispieldatensatz von [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1), um zu zeigen, wie dies mit Python und der Pandas-Bibliothek angewendet werden kann. Dieser Datensatz enthält eine Zählung einiger häufiger Wörter, die in E-Mails vorkommen, wobei die Quellen dieser E-Mails anonym sind. Verwenden Sie das [Notebook](notebook.ipynb) in diesem Verzeichnis, um mitzumachen.

## Explorative Datenanalyse

Die Erfassungsphase des Lebenszyklus ist der Punkt, an dem die Daten gesammelt sowie die Probleme und Fragen definiert werden. Aber wie können wir sicherstellen, dass die Daten das Endergebnis unterstützen können? 
Erinnern Sie sich daran, dass ein Datenwissenschaftler folgende Fragen stellen könnte, wenn er die Daten erhält:
-   Habe ich genug Daten, um dieses Problem zu lösen?
-   Sind die Daten von akzeptabler Qualität für dieses Problem?
-   Wenn ich durch diese Daten zusätzliche Informationen entdecke, sollten wir dann die Ziele ändern oder neu definieren?

Die explorative Datenanalyse ist der Prozess, die Daten kennenzulernen, und kann verwendet werden, um diese Fragen zu beantworten sowie die Herausforderungen bei der Arbeit mit dem Datensatz zu identifizieren. Lassen Sie uns einige der Techniken betrachten, die dafür verwendet werden.

## Datenprofilierung, deskriptive Statistik und Pandas
Wie können wir bewerten, ob wir genug Daten haben, um dieses Problem zu lösen? Die Datenprofilierung kann allgemeine Informationen über unseren Datensatz zusammenfassen und sammeln, indem sie Techniken der deskriptiven Statistik verwendet. Die Datenprofilierung hilft uns zu verstehen, was uns zur Verfügung steht, und die deskriptive Statistik hilft uns zu verstehen, wie viele Dinge uns zur Verfügung stehen.

In einigen der vorherigen Lektionen haben wir Pandas verwendet, um einige deskriptive Statistiken mit der [`describe()`-Funktion](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html) bereitzustellen. Sie liefert die Anzahl, Maximal- und Minimalwerte, den Mittelwert, die Standardabweichung und Quantile der numerischen Daten. Die Verwendung von deskriptiven Statistiken wie der `describe()`-Funktion kann Ihnen helfen zu beurteilen, wie viel Sie haben und ob Sie mehr benötigen.

## Sampling und Abfragen
Das Erkunden eines großen Datensatzes kann sehr zeitaufwändig sein und ist normalerweise eine Aufgabe, die einem Computer überlassen wird. Sampling ist jedoch ein hilfreiches Werkzeug, um die Daten besser zu verstehen und zu erkennen, was im Datensatz enthalten ist und was er repräsentiert. Mit einer Stichprobe können Sie Wahrscheinlichkeiten und Statistiken anwenden, um allgemeine Schlussfolgerungen über Ihre Daten zu ziehen. Obwohl es keine festgelegte Regel gibt, wie viele Daten Sie sampeln sollten, ist es wichtig zu beachten, dass je mehr Daten Sie sampeln, desto präziser können Sie eine Generalisierung über die Daten machen.

Pandas bietet die [`sample()`-Funktion](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), bei der Sie ein Argument übergeben können, wie viele zufällige Stichproben Sie erhalten und verwenden möchten.

Allgemeine Abfragen der Daten können Ihnen helfen, einige allgemeine Fragen und Theorien zu beantworten, die Sie haben könnten. Im Gegensatz zum Sampling ermöglichen Abfragen, dass Sie sich auf spezifische Teile der Daten konzentrieren, über die Sie Fragen haben. Die [`query()`-Funktion](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) in der Pandas-Bibliothek ermöglicht es Ihnen, Spalten auszuwählen und einfache Antworten über die Daten durch die abgerufenen Zeilen zu erhalten.

## Erkunden mit Visualisierungen
Sie müssen nicht warten, bis die Daten vollständig bereinigt und analysiert sind, um mit der Erstellung von Visualisierungen zu beginnen. Tatsächlich kann eine visuelle Darstellung während des Erkundens helfen, Muster, Beziehungen und Probleme in den Daten zu identifizieren. Darüber hinaus bieten Visualisierungen eine Möglichkeit, mit Personen zu kommunizieren, die nicht direkt mit der Datenverwaltung beschäftigt sind, und können eine Gelegenheit sein, zusätzliche Fragen zu klären, die in der Erfassungsphase nicht behandelt wurden. Sehen Sie sich den [Abschnitt über Visualisierungen](../../../../../../../../../3-Data-Visualization) an, um mehr über einige beliebte Möglichkeiten zur visuellen Erkundung zu erfahren.

## Erkunden zur Identifizierung von Inkonsistenzen
Alle Themen in dieser Lektion können helfen, fehlende oder inkonsistente Werte zu identifizieren, aber Pandas bietet Funktionen, um einige davon zu überprüfen. [isna() oder isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) können fehlende Werte überprüfen. Ein wichtiger Aspekt beim Erkunden dieser Werte in Ihren Daten ist es, zu untersuchen, warum sie überhaupt so geworden sind. Dies kann Ihnen helfen zu entscheiden, welche [Maßnahmen zur Behebung](/2-Working-With-Data/08-data-preparation/notebook.ipynb) ergriffen werden sollten.

## [Quiz nach der Vorlesung](https://ff-quizzes.netlify.app/en/ds/)

## Aufgabe

[Erkunden für Antworten](assignment.md)

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.