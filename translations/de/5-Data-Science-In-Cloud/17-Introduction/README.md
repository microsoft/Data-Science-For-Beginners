<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "408c55cab2880daa4e78616308bd5db7",
  "translation_date": "2025-08-24T22:02:51+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "de"
}
-->
# Einführung in Data Science in der Cloud

|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Data Science in der Cloud: Einführung - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

In dieser Lektion lernen Sie die grundlegenden Prinzipien der Cloud kennen. Sie erfahren, warum es interessant sein kann, Cloud-Dienste für Ihre Data-Science-Projekte zu nutzen, und wir betrachten einige Beispiele für Data-Science-Projekte, die in der Cloud durchgeführt werden.

## [Quiz vor der Vorlesung](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## Was ist die Cloud?

Die Cloud, oder Cloud Computing, bezeichnet die Bereitstellung einer Vielzahl von nutzungsbasierten IT-Diensten, die über das Internet auf einer Infrastruktur gehostet werden. Zu den Diensten gehören Lösungen wie Speicher, Datenbanken, Netzwerke, Software, Analysen und intelligente Dienste.

Wir unterscheiden in der Regel zwischen Public, Private und Hybrid Clouds:

* Public Cloud: Eine Public Cloud wird von einem Drittanbieter betrieben, der seine IT-Ressourcen über das Internet der Öffentlichkeit zur Verfügung stellt.
* Private Cloud: Bezieht sich auf IT-Ressourcen, die ausschließlich von einem Unternehmen oder einer Organisation genutzt werden, wobei die Dienste und die Infrastruktur in einem privaten Netzwerk verwaltet werden.
* Hybrid Cloud: Ein System, das Public und Private Clouds kombiniert. Nutzer verwenden ein lokales Rechenzentrum, während Daten und Anwendungen auf einer oder mehreren Public Clouds ausgeführt werden können.

Die meisten Cloud-Computing-Dienste lassen sich in drei Kategorien einteilen: Infrastructure as a Service (IaaS), Platform as a Service (PaaS) und Software as a Service (SaaS).

* Infrastructure as a Service (IaaS): Nutzer mieten eine IT-Infrastruktur wie Server, virtuelle Maschinen (VMs), Speicher, Netzwerke und Betriebssysteme.
* Platform as a Service (PaaS): Nutzer mieten eine Umgebung für die Entwicklung, das Testen, die Bereitstellung und das Management von Softwareanwendungen. Sie müssen sich nicht um die Einrichtung oder Verwaltung der zugrunde liegenden Infrastruktur kümmern.
* Software as a Service (SaaS): Nutzer erhalten Zugriff auf Softwareanwendungen über das Internet, auf Abruf und in der Regel auf Abonnementbasis. Sie müssen sich nicht um Hosting, Verwaltung oder Wartung der Software kümmern.

Zu den größten Cloud-Anbietern gehören Amazon Web Services, Google Cloud Platform und Microsoft Azure.

## Warum die Cloud für Data Science wählen?

Entwickler und IT-Profis entscheiden sich aus vielen Gründen für die Arbeit mit der Cloud, darunter:

* Innovation: Sie können Ihre Anwendungen durch die Integration innovativer Dienste, die von Cloud-Anbietern bereitgestellt werden, erweitern.
* Flexibilität: Sie zahlen nur für die Dienste, die Sie benötigen, und können aus einer Vielzahl von Diensten wählen. In der Regel zahlen Sie nach Bedarf und passen Ihre Dienste an Ihre sich ändernden Anforderungen an.
* Budget: Sie müssen keine Anfangsinvestitionen tätigen, um Hardware und Software zu kaufen, Rechenzentren vor Ort einzurichten und zu betreiben. Sie zahlen nur für das, was Sie nutzen.
* Skalierbarkeit: Ihre Ressourcen können entsprechend den Anforderungen Ihres Projekts skaliert werden. Das bedeutet, dass Ihre Anwendungen je nach externen Faktoren mehr oder weniger Rechenleistung, Speicherplatz und Bandbreite nutzen können.
* Produktivität: Sie können sich auf Ihr Geschäft konzentrieren, anstatt Zeit mit Aufgaben zu verbringen, die von anderen verwaltet werden können, wie z. B. die Verwaltung von Rechenzentren.
* Zuverlässigkeit: Cloud Computing bietet verschiedene Möglichkeiten, Ihre Daten kontinuierlich zu sichern, und Sie können Notfallwiederherstellungspläne einrichten, um Ihr Geschäft und Ihre Dienste auch in Krisenzeiten aufrechtzuerhalten.
* Sicherheit: Sie profitieren von Richtlinien, Technologien und Kontrollen, die die Sicherheit Ihres Projekts stärken.

Dies sind einige der häufigsten Gründe, warum Menschen sich für die Nutzung von Cloud-Diensten entscheiden. Jetzt, da wir ein besseres Verständnis davon haben, was die Cloud ist und welche Hauptvorteile sie bietet, schauen wir uns genauer an, wie Data Scientists und Entwickler, die mit Daten arbeiten, von der Cloud profitieren können:

* Speicherung großer Datenmengen: Anstatt große Server zu kaufen, zu verwalten und zu schützen, können Sie Ihre Daten direkt in der Cloud speichern, mit Lösungen wie Azure Cosmos DB, Azure SQL Database und Azure Data Lake Storage.
* Datenintegration durchführen: Datenintegration ist ein wesentlicher Bestandteil von Data Science, der den Übergang von der Datenerfassung zur Handlung ermöglicht. Mit Cloud-Datenintegrationsdiensten können Sie Daten aus verschiedenen Quellen sammeln, transformieren und in ein einziges Data Warehouse integrieren, z. B. mit Data Factory.
* Datenverarbeitung: Die Verarbeitung großer Datenmengen erfordert viel Rechenleistung, die nicht jedem zur Verfügung steht. Deshalb nutzen viele Menschen direkt die enorme Rechenleistung der Cloud, um ihre Lösungen auszuführen und bereitzustellen.
* Nutzung von Datenanalysediensten: Cloud-Dienste wie Azure Synapse Analytics, Azure Stream Analytics und Azure Databricks helfen Ihnen, Ihre Daten in umsetzbare Erkenntnisse zu verwandeln.
* Nutzung von Machine-Learning- und Datenintelligenzdiensten: Anstatt bei null anzufangen, können Sie Machine-Learning-Algorithmen des Cloud-Anbieters nutzen, z. B. mit AzureML. Sie können auch kognitive Dienste wie Sprach-zu-Text, Text-zu-Sprache, Computer Vision und mehr verwenden.

## Beispiele für Data Science in der Cloud

Lassen Sie uns dies anhand einiger Szenarien greifbarer machen.

### Echtzeit-Sentiment-Analyse in sozialen Medien

Wir beginnen mit einem Szenario, das häufig von Personen untersucht wird, die mit Machine Learning beginnen: Sentiment-Analyse in sozialen Medien in Echtzeit.

Angenommen, Sie betreiben eine Nachrichten-Website und möchten Live-Daten nutzen, um zu verstehen, welche Inhalte Ihre Leser interessieren könnten. Um mehr darüber zu erfahren, können Sie ein Programm erstellen, das in Echtzeit eine Sentiment-Analyse von Twitter-Daten zu Themen durchführt, die für Ihre Leser relevant sind.

Die wichtigsten Indikatoren, die Sie betrachten, sind das Volumen der Tweets zu bestimmten Themen (Hashtags) und die Stimmung, die mit Analysetools ermittelt wird, die Sentiment-Analysen zu den angegebenen Themen durchführen.

Die notwendigen Schritte zur Erstellung dieses Projekts sind:

* Erstellen eines Event Hubs für Streaming-Eingaben, der Daten von Twitter sammelt
* Konfigurieren und Starten einer Twitter-Client-Anwendung, die die Twitter-Streaming-APIs aufruft
* Erstellen eines Stream-Analytics-Jobs
* Festlegen der Job-Eingabe und -Abfrage
* Erstellen eines Ausgabeziels und Festlegen der Job-Ausgabe
* Starten des Jobs

Um den gesamten Prozess zu sehen, lesen Sie die [Dokumentation](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Analyse wissenschaftlicher Artikel

Betrachten wir ein weiteres Beispiel für ein Projekt, das von [Dmitry Soshnikov](http://soshnikov.com), einem der Autoren dieses Curriculums, erstellt wurde.

Dmitry hat ein Tool entwickelt, das COVID-Artikel analysiert. Durch die Überprüfung dieses Projekts sehen Sie, wie Sie ein Tool erstellen können, das Wissen aus wissenschaftlichen Artikeln extrahiert, Erkenntnisse gewinnt und Forschern hilft, große Sammlungen von Artikeln effizient zu durchsuchen.

Die verschiedenen Schritte sind:

* Extrahieren und Vorverarbeiten von Informationen mit [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)
* Nutzung von [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) zur Parallelisierung der Verarbeitung
* Speichern und Abfragen von Informationen mit [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)
* Erstellen eines interaktiven Dashboards zur Datenexploration und -visualisierung mit Power BI

Um den gesamten Prozess zu sehen, besuchen Sie [Dmitrys Blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Wie Sie sehen, können wir Cloud-Dienste auf vielfältige Weise nutzen, um Data Science zu betreiben.

## Fußnote

Quellen:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Quiz nach der Vorlesung

[Quiz nach der Vorlesung](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/33)

## Aufgabe

[Marktforschung](assignment.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.