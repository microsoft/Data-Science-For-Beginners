<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-09-05T13:49:35+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "de"
}
-->
# Einführung in Data Science in der Cloud

|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Data Science in der Cloud: Einführung - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

In dieser Lektion lernen Sie die grundlegenden Prinzipien der Cloud kennen, erfahren, warum es interessant sein könnte, Cloud-Dienste für Ihre Data-Science-Projekte zu nutzen, und sehen einige Beispiele für Data-Science-Projekte, die in der Cloud durchgeführt werden.

## [Quiz vor der Vorlesung](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## Was ist die Cloud?

Die Cloud, oder Cloud Computing, bezeichnet die Bereitstellung einer Vielzahl von nutzungsbasierten Computing-Diensten, die über eine Infrastruktur im Internet gehostet werden. Zu den Diensten gehören Lösungen wie Speicher, Datenbanken, Netzwerke, Software, Analysen und intelligente Dienste.

Wir unterscheiden üblicherweise zwischen öffentlicher, privater und hybrider Cloud wie folgt:

* Öffentliche Cloud: Eine öffentliche Cloud wird von einem Drittanbieter betrieben, der seine Computing-Ressourcen über das Internet der Öffentlichkeit zur Verfügung stellt.
* Private Cloud: Bezieht sich auf Computing-Ressourcen, die ausschließlich von einem Unternehmen oder einer Organisation genutzt werden, mit Diensten und einer Infrastruktur, die in einem privaten Netzwerk verwaltet werden.
* Hybride Cloud: Die hybride Cloud kombiniert öffentliche und private Clouds. Nutzer entscheiden sich für ein lokales Rechenzentrum, während Daten und Anwendungen auf einer oder mehreren öffentlichen Clouds betrieben werden können.

Die meisten Cloud-Computing-Dienste fallen in drei Kategorien: Infrastructure as a Service (IaaS), Platform as a Service (PaaS) und Software as a Service (SaaS).

* Infrastructure as a Service (IaaS): Nutzer mieten eine IT-Infrastruktur wie Server, virtuelle Maschinen (VMs), Speicher, Netzwerke und Betriebssysteme.
* Platform as a Service (PaaS): Nutzer mieten eine Umgebung für die Entwicklung, das Testen, die Bereitstellung und das Management von Softwareanwendungen. Sie müssen sich nicht um die Einrichtung oder Verwaltung der zugrunde liegenden Infrastruktur kümmern.
* Software as a Service (SaaS): Nutzer erhalten Zugriff auf Softwareanwendungen über das Internet, auf Abruf und meist auf Abonnementbasis. Sie müssen sich nicht um Hosting, Management oder Wartung der Software kümmern, wie z. B. Software-Upgrades und Sicherheitsupdates.

Zu den größten Cloud-Anbietern gehören Amazon Web Services, Google Cloud Platform und Microsoft Azure.

## Warum die Cloud für Data Science wählen?

Entwickler und IT-Experten entscheiden sich aus vielen Gründen für die Arbeit mit der Cloud, darunter:

* Innovation: Sie können Ihre Anwendungen mit innovativen Diensten, die von Cloud-Anbietern bereitgestellt werden, direkt erweitern.
* Flexibilität: Sie zahlen nur für die Dienste, die Sie benötigen, und können aus einer Vielzahl von Diensten wählen. Meistens zahlen Sie nach Bedarf und passen Ihre Dienste an Ihre sich entwickelnden Anforderungen an.
* Budget: Sie müssen keine Anfangsinvestitionen für den Kauf von Hardware und Software tätigen, keine lokalen Rechenzentren einrichten und betreiben, sondern zahlen nur für das, was Sie nutzen.
* Skalierbarkeit: Ihre Ressourcen können je nach Bedarf Ihres Projekts skaliert werden, sodass Ihre Anwendungen mehr oder weniger Rechenleistung, Speicher und Bandbreite nutzen können, indem sie sich zu jedem Zeitpunkt an externe Faktoren anpassen.
* Produktivität: Sie können sich auf Ihr Geschäft konzentrieren, anstatt Zeit mit Aufgaben zu verbringen, die von jemand anderem verwaltet werden können, wie z. B. die Verwaltung von Rechenzentren.
* Zuverlässigkeit: Cloud Computing bietet verschiedene Möglichkeiten, Ihre Daten kontinuierlich zu sichern, und Sie können Notfallwiederherstellungspläne einrichten, um Ihr Geschäft und Ihre Dienste auch in Krisenzeiten aufrechtzuerhalten.
* Sicherheit: Sie profitieren von Richtlinien, Technologien und Kontrollen, die die Sicherheit Ihres Projekts stärken.

Dies sind einige der häufigsten Gründe, warum Menschen sich für die Nutzung von Cloud-Diensten entscheiden. Jetzt, da wir ein besseres Verständnis davon haben, was die Cloud ist und welche Hauptvorteile sie bietet, schauen wir uns genauer die Aufgaben von Data Scientists und Entwicklern an, die mit Daten arbeiten, und wie die Cloud ihnen bei verschiedenen Herausforderungen helfen kann:

* Speicherung großer Datenmengen: Anstatt große Server zu kaufen, zu verwalten und zu schützen, können Sie Ihre Daten direkt in der Cloud speichern, mit Lösungen wie Azure Cosmos DB, Azure SQL Database und Azure Data Lake Storage.
* Datenintegration durchführen: Datenintegration ist ein wesentlicher Bestandteil der Data Science, der den Übergang von der Datenerfassung zur Handlung ermöglicht. Mit Datenintegrationsdiensten in der Cloud können Sie Daten aus verschiedenen Quellen sammeln, transformieren und in ein einziges Data Warehouse integrieren, z. B. mit Data Factory.
* Daten verarbeiten: Die Verarbeitung großer Datenmengen erfordert viel Rechenleistung, und nicht jeder hat Zugang zu leistungsstarken Maschinen. Deshalb entscheiden sich viele dafür, die enorme Rechenleistung der Cloud direkt zu nutzen, um ihre Lösungen auszuführen und bereitzustellen.
* Nutzung von Datenanalyse-Diensten: Cloud-Dienste wie Azure Synapse Analytics, Azure Stream Analytics und Azure Databricks helfen Ihnen, Ihre Daten in umsetzbare Erkenntnisse umzuwandeln.
* Nutzung von Machine-Learning- und Datenintelligenz-Diensten: Anstatt von Grund auf neu zu beginnen, können Sie Machine-Learning-Algorithmen nutzen, die vom Cloud-Anbieter bereitgestellt werden, z. B. mit AzureML. Sie können auch kognitive Dienste wie Sprach-zu-Text, Text-zu-Sprache, Computer Vision und mehr verwenden.

## Beispiele für Data Science in der Cloud

Machen wir das greifbarer, indem wir uns ein paar Szenarien ansehen.

### Echtzeit-Sentiment-Analyse von sozialen Medien
Beginnen wir mit einem Szenario, das häufig von Personen untersucht wird, die mit Machine Learning beginnen: Echtzeit-Sentiment-Analyse von sozialen Medien.

Angenommen, Sie betreiben eine Nachrichten-Website und möchten Live-Daten nutzen, um zu verstehen, welche Inhalte Ihre Leser interessieren könnten. Um mehr darüber zu erfahren, können Sie ein Programm erstellen, das eine Echtzeit-Sentiment-Analyse von Twitter-Daten zu relevanten Themen durchführt.

Die wichtigsten Indikatoren, die Sie betrachten, sind das Volumen der Tweets zu bestimmten Themen (Hashtags) und die Stimmung, die mithilfe von Analysetools ermittelt wird, die eine Sentiment-Analyse zu den angegebenen Themen durchführen.

Die Schritte zur Erstellung dieses Projekts sind wie folgt:

* Erstellen eines Event Hubs für Streaming-Eingaben, der Daten von Twitter sammelt
* Konfigurieren und Starten einer Twitter-Client-Anwendung, die die Twitter Streaming APIs aufruft
* Erstellen eines Stream Analytics Jobs
* Festlegen der Job-Eingabe und Abfrage
* Erstellen eines Ausgabeziels und Festlegen der Job-Ausgabe
* Starten des Jobs

Um den vollständigen Prozess zu sehen, besuchen Sie die [Dokumentation](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Analyse wissenschaftlicher Artikel
Betrachten wir ein weiteres Beispiel für ein Projekt, das von [Dmitry Soshnikov](http://soshnikov.com), einem der Autoren dieses Curriculums, erstellt wurde.

Dmitry hat ein Tool entwickelt, das COVID-Artikel analysiert. Durch die Überprüfung dieses Projekts sehen Sie, wie Sie ein Tool erstellen können, das Wissen aus wissenschaftlichen Artikeln extrahiert, Erkenntnisse gewinnt und Forschern hilft, große Sammlungen von Artikeln effizient zu durchsuchen.

Die verschiedenen Schritte für dieses Projekt sind:

* Extrahieren und Vorverarbeiten von Informationen mit [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)
* Nutzung von [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) zur Parallelisierung der Verarbeitung
* Speichern und Abfragen von Informationen mit [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)
* Erstellen eines interaktiven Dashboards zur Datenexploration und Visualisierung mit Power BI

Um den vollständigen Prozess zu sehen, besuchen Sie [Dmitrys Blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Wie Sie sehen, können wir Cloud-Dienste auf viele Arten nutzen, um Data Science durchzuführen.

## Fußnote

Quellen:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Quiz nach der Vorlesung

## [Quiz nach der Vorlesung](https://ff-quizzes.netlify.app/en/ds/quiz/33)

## Aufgabe

[Marktforschung](assignment.md)

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.