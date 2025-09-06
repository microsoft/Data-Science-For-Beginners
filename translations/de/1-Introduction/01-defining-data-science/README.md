<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a0516588d172f82f35f7a0d4a001e5d0",
  "translation_date": "2025-09-05T14:02:36+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "de"
}
-->
## Definition von Daten

In unserem Alltag sind wir ständig von Daten umgeben. Der Text, den Sie gerade lesen, ist Daten. Die Liste der Telefonnummern Ihrer Freunde auf Ihrem Smartphone sind Daten, ebenso wie die aktuelle Uhrzeit auf Ihrer Uhr. Als Menschen arbeiten wir ganz natürlich mit Daten, sei es beim Zählen unseres Geldes oder beim Schreiben von Briefen an Freunde.

Mit der Erfindung von Computern wurden Daten jedoch wesentlich wichtiger. Die Hauptaufgabe von Computern ist es, Berechnungen durchzuführen, aber sie benötigen Daten, um arbeiten zu können. Daher müssen wir verstehen, wie Computer Daten speichern und verarbeiten.

Mit dem Aufkommen des Internets hat sich die Rolle von Computern als Datenverarbeitungsgeräte verstärkt. Wenn man darüber nachdenkt, nutzen wir Computer heutzutage immer mehr für die Datenverarbeitung und Kommunikation, anstatt für tatsächliche Berechnungen. Wenn wir eine E-Mail an einen Freund schreiben oder Informationen im Internet suchen, erstellen, speichern, übertragen und manipulieren wir im Wesentlichen Daten.
> Können Sie sich daran erinnern, wann Sie das letzte Mal einen Computer tatsächlich für Berechnungen genutzt haben?

## Was ist Data Science?

Laut [Wikipedia](https://en.wikipedia.org/wiki/Data_science) wird **Data Science** definiert als *ein wissenschaftliches Feld, das wissenschaftliche Methoden nutzt, um Wissen und Erkenntnisse aus strukturierten und unstrukturierten Daten zu gewinnen und dieses Wissen sowie umsetzbare Erkenntnisse aus Daten in einer Vielzahl von Anwendungsbereichen anzuwenden*.

Diese Definition hebt die folgenden wichtigen Aspekte der Data Science hervor:

* Das Hauptziel der Data Science ist es, **Wissen aus Daten zu gewinnen**, also Daten zu **verstehen**, versteckte Zusammenhänge zu finden und ein **Modell** zu erstellen.
* Data Science verwendet **wissenschaftliche Methoden**, wie Wahrscheinlichkeitsrechnung und Statistik. Tatsächlich argumentierten einige, als der Begriff *Data Science* erstmals eingeführt wurde, dass es sich lediglich um einen neuen, schicken Namen für Statistik handele. Heute ist klar, dass das Feld viel breiter ist.
* Das gewonnene Wissen sollte genutzt werden, um **umsetzbare Erkenntnisse** zu liefern, d.h. praktische Einsichten, die in realen Geschäftssituationen angewendet werden können.
* Wir sollten in der Lage sein, sowohl mit **strukturierten** als auch mit **unstrukturierten** Daten zu arbeiten. Später im Kurs werden wir auf die verschiedenen Datentypen zurückkommen.
* **Anwendungsbereiche** sind ein wichtiger Aspekt, und Data Scientists benötigen oft zumindest ein gewisses Maß an Fachwissen im jeweiligen Problemfeld, z.B. Finanzen, Medizin, Marketing usw.

> Ein weiterer wichtiger Aspekt der Data Science ist, dass sie untersucht, wie Daten mit Computern gesammelt, gespeichert und verarbeitet werden können. Während die Statistik uns die mathematischen Grundlagen liefert, wendet die Data Science mathematische Konzepte an, um tatsächlich Erkenntnisse aus Daten zu gewinnen.

Eine Möglichkeit (zugeschrieben [Jim Gray](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))), Data Science zu betrachten, ist, sie als ein eigenes Paradigma der Wissenschaft zu sehen:
* **Empirisch**, wobei wir uns hauptsächlich auf Beobachtungen und Ergebnisse von Experimenten stützen
* **Theoretisch**, wo neue Konzepte aus bestehendem wissenschaftlichem Wissen entstehen
* **Computational**, wo wir neue Prinzipien basierend auf computergestützten Experimenten entdecken
* **Datengetrieben**, basierend auf der Entdeckung von Zusammenhängen und Mustern in den Daten  

## Andere verwandte Bereiche

Da Daten allgegenwärtig sind, ist auch Data Science ein breites Feld, das viele andere Disziplinen berührt.

## Datentypen

Wie bereits erwähnt, sind Daten überall. Wir müssen sie nur auf die richtige Weise erfassen! Es ist hilfreich, zwischen **strukturierten** und **unstrukturierten** Daten zu unterscheiden. Erstere werden typischerweise in einer gut strukturierten Form dargestellt, oft als Tabelle oder mehrere Tabellen, während letztere einfach eine Sammlung von Dateien sind. Manchmal sprechen wir auch von **halbstrukturierten** Daten, die eine gewisse Struktur haben, die jedoch stark variieren kann.

| Strukturiert                                                                | Halbstrukturiert                                                                                 | Unstrukturiert                          |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | --------------------------------------- |
| Liste von Personen mit ihren Telefonnummern                                 | Wikipedia-Seiten mit Links                                                                       | Text der Encyclopedia Britannica        |
| Temperatur in allen Räumen eines Gebäudes jede Minute der letzten 20 Jahre  | Sammlung wissenschaftlicher Artikel im JSON-Format mit Autoren, Veröffentlichungsdatum und Abstract | Dateifreigabe mit Unternehmensdokumenten |
| Daten zu Alter und Geschlecht aller Personen, die das Gebäude betreten      | Internetseiten                                                                                   | Rohes Videomaterial von Überwachungskameras |

## Woher bekommt man Daten?

Es gibt viele mögliche Datenquellen, und es wäre unmöglich, alle aufzuzählen! Lassen Sie uns jedoch einige typische Orte erwähnen, an denen Sie Daten finden können:

* **Strukturiert**
  - **Internet of Things** (IoT), einschließlich Daten von verschiedenen Sensoren wie Temperatur- oder Drucksensoren, liefert viele nützliche Daten. Zum Beispiel können wir, wenn ein Bürogebäude mit IoT-Sensoren ausgestattet ist, automatisch Heizung und Beleuchtung steuern, um Kosten zu minimieren.
  - **Umfragen**, die wir Benutzer nach einem Kauf oder nach dem Besuch einer Website ausfüllen lassen.
  - **Verhaltensanalysen** können uns beispielsweise helfen zu verstehen, wie tief ein Benutzer in eine Website eintaucht und was der typische Grund für das Verlassen der Seite ist.
* **Unstrukturiert**
  - **Texte** können eine reiche Quelle von Erkenntnissen sein, wie z.B. eine allgemeine **Stimmungsbewertung** oder das Extrahieren von Schlüsselwörtern und semantischen Bedeutungen.
  - **Bilder** oder **Videos**. Ein Video von einer Überwachungskamera kann verwendet werden, um den Verkehr auf der Straße zu schätzen und Menschen über mögliche Staus zu informieren.
  - **Webserver-Logs** können verwendet werden, um zu verstehen, welche Seiten unserer Website am häufigsten besucht werden und wie lange.
* **Halbstrukturiert**
  - **Soziale Netzwerke** können großartige Datenquellen über Benutzerpersönlichkeiten und potenzielle Effektivität bei der Verbreitung von Informationen sein.
  - Wenn wir eine Sammlung von Fotos von einer Party haben, können wir versuchen, **Gruppendynamik**-Daten zu extrahieren, indem wir ein Netzwerk von Personen erstellen, die miteinander fotografiert wurden.

Indem Sie verschiedene mögliche Datenquellen kennen, können Sie über verschiedene Szenarien nachdenken, in denen Data-Science-Techniken angewendet werden können, um die Situation besser zu verstehen und Geschäftsprozesse zu verbessern.

## Was Sie mit Daten machen können

In der Data Science konzentrieren wir uns auf die folgenden Schritte der Datenreise:

Natürlich können je nach den tatsächlichen Daten einige Schritte fehlen (z.B. wenn wir die Daten bereits in der Datenbank haben oder wenn wir kein Modelltraining benötigen), oder einige Schritte können mehrmals wiederholt werden (wie die Datenverarbeitung).

## Digitalisierung und digitale Transformation

In den letzten zehn Jahren haben viele Unternehmen begonnen, die Bedeutung von Daten bei Geschäftsentscheidungen zu erkennen. Um Data-Science-Prinzipien auf ein Unternehmen anzuwenden, muss zunächst eine Datensammlung erfolgen, d.h. Geschäftsprozesse müssen in digitale Form übersetzt werden. Dies wird als **Digitalisierung** bezeichnet. Die Anwendung von Data-Science-Techniken auf diese Daten zur Entscheidungsfindung kann zu erheblichen Produktivitätssteigerungen (oder sogar zu einer Neuausrichtung des Unternehmens) führen, was als **digitale Transformation** bezeichnet wird.

Betrachten wir ein Beispiel. Angenommen, wir haben einen Data-Science-Kurs (wie diesen hier), den wir online an Studenten anbieten, und wir möchten Data Science nutzen, um ihn zu verbessern. Wie können wir das tun?

Wir können damit beginnen, uns zu fragen: "Was kann digitalisiert werden?" Der einfachste Weg wäre, die Zeit zu messen, die jeder Student benötigt, um jedes Modul abzuschließen, und das erworbene Wissen zu messen, indem am Ende jedes Moduls ein Multiple-Choice-Test durchgeführt wird. Indem wir die Abschlusszeiten aller Studenten mitteln, können wir herausfinden, welche Module den Studenten die größten Schwierigkeiten bereiten, und daran arbeiten, sie zu vereinfachen.
> Man könnte argumentieren, dass dieser Ansatz nicht ideal ist, da Module unterschiedlich lang sein können. Es wäre wahrscheinlich fairer, die Zeit durch die Länge des Moduls (in Anzahl der Zeichen) zu teilen und stattdessen diese Werte zu vergleichen.
Wenn wir beginnen, die Ergebnisse von Multiple-Choice-Tests zu analysieren, können wir versuchen herauszufinden, welche Konzepte den Schülern Schwierigkeiten bereiten, und diese Informationen nutzen, um die Inhalte zu verbessern. Um dies zu erreichen, müssen wir Tests so gestalten, dass jede Frage einem bestimmten Konzept oder Wissensbereich zugeordnet werden kann.

Wenn wir noch weiter ins Detail gehen möchten, können wir die benötigte Zeit für jedes Modul mit der Alterskategorie der Schüler vergleichen. Dabei könnten wir feststellen, dass es für bestimmte Altersgruppen unangemessen lange dauert, ein Modul abzuschließen, oder dass Schüler abbrechen, bevor sie es beendet haben. Dies kann uns helfen, Altersempfehlungen für das Modul zu geben und die Unzufriedenheit durch falsche Erwartungen zu minimieren.

## 🚀 Herausforderung

In dieser Herausforderung werden wir versuchen, relevante Konzepte für den Bereich Data Science zu finden, indem wir Texte analysieren. Wir nehmen einen Wikipedia-Artikel über Data Science, laden den Text herunter, verarbeiten ihn und erstellen dann eine Wortwolke wie diese:

![Wortwolke für Data Science](../../../../1-Introduction/01-defining-data-science/images/ds_wordcloud.png)

Besuche [`notebook.ipynb`](../../../../../../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore'), um den Code durchzulesen. Du kannst den Code auch ausführen und sehen, wie er alle Datentransformationen in Echtzeit durchführt.

> Wenn du nicht weißt, wie man Code in einem Jupyter Notebook ausführt, schau dir [diesen Artikel](https://soshnikov.com/education/how-to-execute-notebooks-from-github/) an.

## [Quiz nach der Vorlesung](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Aufgaben

* **Aufgabe 1**: Ändere den oben genannten Code, um verwandte Konzepte für die Bereiche **Big Data** und **Machine Learning** zu finden.
* **Aufgabe 2**: [Denke über Data-Science-Szenarien nach](assignment.md)

## Credits

Diese Lektion wurde mit ♥️ von [Dmitry Soshnikov](http://soshnikov.com) verfasst.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.