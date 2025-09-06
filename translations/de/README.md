<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5443b88ba402d2ec7b000e4de6cecb8",
  "translation_date": "2025-08-30T08:55:31+00:00",
  "source_file": "README.md",
  "language_code": "de"
}
-->
# Datenwissenschaft für Anfänger – Ein Lehrplan

Azure Cloud Advocates bei Microsoft freuen sich, einen 10-wöchigen, 20-Lektionen umfassenden Lehrplan rund um Datenwissenschaft anzubieten. Jede Lektion enthält Quizfragen vor und nach der Lektion, schriftliche Anleitungen zur Durchführung der Lektion, eine Lösung und eine Aufgabe. Unsere projektbasierte Pädagogik ermöglicht es Ihnen, durch praktisches Arbeiten zu lernen – eine bewährte Methode, um neue Fähigkeiten nachhaltig zu erlernen.

**Ein herzliches Dankeschön an unsere Autor*innen:** [Jasmine Greenaway](https://www.twitter.com/paladique), [Dmitry Soshnikov](http://soshnikov.com), [Nitya Narasimhan](https://twitter.com/nitya), [Jalen McGee](https://twitter.com/JalenMcG), [Jen Looper](https://twitter.com/jenlooper), [Maud Levy](https://twitter.com/maudstweets), [Tiffany Souterre](https://twitter.com/TiffanySouterre), [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏 Besonderer Dank 🙏 an unsere [Microsoft Student Ambassador](https://studentambassadors.microsoft.com/)-Autor*innen, Prüfer*innen und Inhaltsbeitragende,** insbesondere Aaryan Arora, [Aditya Garg](https://github.com/AdityaGarg00), [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/), [Ankita Singh](https://www.linkedin.com/in/ankitasingh007), [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/), [Arpita Das](https://www.linkedin.com/in/arpitadas01/), ChhailBihari Dubey, [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor), [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [Majd Safi](https://www.linkedin.com/in/majd-s/), [Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/), [Miguel Correa](https://www.linkedin.com/in/miguelmque/), [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119), [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum), [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/), [Rohit Yadav](https://www.linkedin.com/in/rty2423), Samridhi Sharma, [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200), [Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/), [Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/), Yogendrasingh Pawar, [Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/), [Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![Sketchnote von @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.de.png)|
|:---:|
| Datenwissenschaft für Anfänger – _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

### 🌐 Mehrsprachige Unterstützung

#### Unterstützt durch GitHub Action (Automatisiert & Immer aktuell)

[Französisch](../fr/README.md) | [Spanisch](../es/README.md) | [Deutsch](./README.md) | [Russisch](../ru/README.md) | [Arabisch](../ar/README.md) | [Persisch (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinesisch (Vereinfacht)](../zh/README.md) | [Chinesisch (Traditionell, Macau)](../mo/README.md) | [Chinesisch (Traditionell, Hongkong)](../hk/README.md) | [Chinesisch (Traditionell, Taiwan)](../tw/README.md) | [Japanisch](../ja/README.md) | [Koreanisch](../ko/README.md) | [Hindi](../hi/README.md) | [Bengalisch](../bn/README.md) | [Marathi](../mr/README.md) | [Nepalesisch](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portugiesisch (Portugal)](../pt/README.md) | [Portugiesisch (Brasilien)](../br/README.md) | [Italienisch](../it/README.md) | [Polnisch](../pl/README.md) | [Türkisch](../tr/README.md) | [Griechisch](../el/README.md) | [Thailändisch](../th/README.md) | [Schwedisch](../sv/README.md) | [Dänisch](../da/README.md) | [Norwegisch](../no/README.md) | [Finnisch](../fi/README.md) | [Niederländisch](../nl/README.md) | [Hebräisch](../he/README.md) | [Vietnamesisch](../vi/README.md) | [Indonesisch](../id/README.md) | [Malaiisch](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Suaheli](../sw/README.md) | [Ungarisch](../hu/README.md) | [Tschechisch](../cs/README.md) | [Slowakisch](../sk/README.md) | [Rumänisch](../ro/README.md) | [Bulgarisch](../bg/README.md) | [Serbisch (Kyrillisch)](../sr/README.md) | [Kroatisch](../hr/README.md) | [Slowenisch](../sl/README.md) | [Ukrainisch](../uk/README.md) | [Birmanisch (Myanmar)](../my/README.md)

**Falls Sie zusätzliche Übersetzungen wünschen, finden Sie die unterstützten Sprachen [hier](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

#### Treten Sie unserer Community bei 
[![Azure AI Discord](https://dcbadge.limes.pink/api/server/kzRShWzttr)](https://discord.gg/kzRShWzttr)

# Sind Sie ein*e Schüler*in oder Student*in?

Starten Sie mit den folgenden Ressourcen:

- [Student Hub-Seite](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) Auf dieser Seite finden Sie Ressourcen für Anfänger*innen, Student*innenpakete und sogar Möglichkeiten, einen kostenlosen Zertifizierungsgutschein zu erhalten. Diese Seite sollten Sie sich als Lesezeichen speichern und regelmäßig besuchen, da wir den Inhalt mindestens monatlich aktualisieren.
- [Microsoft Learn Student Ambassadors](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) Treten Sie einer globalen Community von Student*innenbotschafter*innen bei – dies könnte Ihr Einstieg bei Microsoft sein.

# Erste Schritte

> **Lehrer*innen**: Wir haben [einige Vorschläge](for-teachers.md) hinzugefügt, wie Sie diesen Lehrplan nutzen können. Wir freuen uns über Ihr Feedback [in unserem Diskussionsforum](https://github.com/microsoft/Data-Science-For-Beginners/discussions)!

> **[Schüler*innen/Student*innen](https://aka.ms/student-page)**: Um diesen Lehrplan eigenständig zu nutzen, forken Sie das gesamte Repository und bearbeiten Sie die Übungen selbstständig, beginnend mit einem Quiz vor der Lektion. Lesen Sie dann die Lektion und führen Sie die restlichen Aktivitäten durch. Versuchen Sie, die Projekte zu erstellen, indem Sie die Lektionen verstehen, anstatt den Lösungscode zu kopieren; dieser ist jedoch in den /solutions-Ordnern jeder projektorientierten Lektion verfügbar. Eine weitere Idee wäre, eine Lerngruppe mit Freund*innen zu bilden und den Inhalt gemeinsam durchzugehen. Für weiterführendes Lernen empfehlen wir [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum).

## Lernen Sie das Team kennen

[![Promo-Video](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "Promo-Video")

**Gif von** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)

> 🎥 Klicken Sie auf das Bild oben, um ein Video über das Projekt und die Personen, die es erstellt haben, anzusehen!

## Pädagogik

Wir haben zwei pädagogische Grundsätze bei der Erstellung dieses Lehrplans gewählt: sicherzustellen, dass er projektbasiert ist, und häufige Quizfragen einzubinden. Am Ende dieser Serie werden die Schüler*innen grundlegende Prinzipien der Datenwissenschaft gelernt haben, einschließlich ethischer Konzepte, Datenvorbereitung, verschiedener Arbeitsweisen mit Daten, Datenvisualisierung, Datenanalyse, realer Anwendungsfälle der Datenwissenschaft und mehr.

Darüber hinaus setzt ein niedrigschwelliges Quiz vor einer Lektion die Intention der Schüler*innen, ein Thema zu lernen, während ein zweites Quiz nach der Lektion das Gelernte weiter festigt. Dieser Lehrplan wurde so gestaltet, dass er flexibel und unterhaltsam ist und ganz oder teilweise genutzt werden kann. Die Projekte beginnen klein und werden im Laufe des 10-wöchigen Zyklus zunehmend komplexer.
> Finden Sie unseren [Verhaltenskodex](CODE_OF_CONDUCT.md), [Beitragsrichtlinien](CONTRIBUTING.md), [Übersetzungsrichtlinien](TRANSLATIONS.md). Wir freuen uns über Ihr konstruktives Feedback!
## Jede Lektion beinhaltet:

- Optionale Sketchnote
- Optionales ergänzendes Video
- Warm-up-Quiz vor der Lektion
- Geschriebene Lektion
- Für projektbasierte Lektionen: Schritt-für-Schritt-Anleitungen zum Erstellen des Projekts
- Wissensüberprüfungen
- Eine Herausforderung
- Ergänzende Lektüre
- Aufgabe
- [Quiz nach der Lektion](https://ff-quizzes.netlify.app/en/)

> **Eine Anmerkung zu den Quizfragen**: Alle Quizfragen befinden sich im Ordner Quiz-App, insgesamt 40 Quizfragen mit jeweils drei Fragen. Sie sind in den Lektionen verlinkt, aber die Quiz-App kann lokal oder auf Azure ausgeführt werden; folgen Sie den Anweisungen im `quiz-app`-Ordner. Sie werden nach und nach lokalisiert.

## Lektionen

|![ Sketchnote von @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Roadmap.4905d6567dff47532b9bfb8e0b8980fc6b0b1292eebb24181c1a9753b33bc0f5.de.png)|
|:---:|
| Data Science für Anfänger: Roadmap - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

| Lektion Nummer | Thema | Lektion Gruppierung | Lernziele | Verlinkte Lektion | Autor |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | Definition von Data Science | [Einführung](1-Introduction/README.md) | Lernen Sie die grundlegenden Konzepte der Data Science und wie sie mit künstlicher Intelligenz, maschinellem Lernen und Big Data zusammenhängt. | [Lektion](1-Introduction/01-defining-data-science/README.md) [Video](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | Ethik in der Data Science | [Einführung](1-Introduction/README.md) | Konzepte, Herausforderungen und Rahmenbedingungen der Datenethik. | [Lektion](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | Definition von Daten | [Einführung](1-Introduction/README.md) | Wie Daten klassifiziert werden und ihre häufigsten Quellen. | [Lektion](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | Einführung in Statistik und Wahrscheinlichkeit | [Einführung](1-Introduction/README.md) | Die mathematischen Techniken der Wahrscheinlichkeit und Statistik, um Daten zu verstehen. | [Lektion](1-Introduction/04-stats-and-probability/README.md) [Video](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | Arbeiten mit relationalen Daten | [Arbeiten mit Daten](2-Working-With-Data/README.md) | Einführung in relationale Daten und die Grundlagen der Exploration und Analyse relationaler Daten mit der Structured Query Language, auch bekannt als SQL (ausgesprochen „see-quell“). | [Lektion](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | Arbeiten mit NoSQL-Daten | [Arbeiten mit Daten](2-Working-With-Data/README.md) | Einführung in nicht-relationale Daten, ihre verschiedenen Typen und die Grundlagen der Exploration und Analyse von Dokumentdatenbanken. | [Lektion](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | Arbeiten mit Python | [Arbeiten mit Daten](2-Working-With-Data/README.md) | Grundlagen der Verwendung von Python zur Datenexploration mit Bibliotheken wie Pandas. Grundlegendes Verständnis der Python-Programmierung wird empfohlen. | [Lektion](2-Working-With-Data/07-python/README.md) [Video](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | Datenvorbereitung | [Arbeiten mit Daten](2-Working-With-Data/README.md) | Themen zu Datentechniken für das Bereinigen und Transformieren von Daten, um Herausforderungen wie fehlende, ungenaue oder unvollständige Daten zu bewältigen. | [Lektion](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | Visualisierung von Mengen | [Datenvisualisierung](3-Data-Visualization/README.md) | Lernen Sie, wie Sie Matplotlib verwenden, um Vogeldaten 🦆 zu visualisieren. | [Lektion](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | Visualisierung von Datenverteilungen | [Datenvisualisierung](3-Data-Visualization/README.md) | Beobachtungen und Trends innerhalb eines Intervalls visualisieren. | [Lektion](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | Visualisierung von Proportionen | [Datenvisualisierung](3-Data-Visualization/README.md) | Diskrete und gruppierte Prozentsätze visualisieren. | [Lektion](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | Visualisierung von Beziehungen | [Datenvisualisierung](3-Data-Visualization/README.md) | Verbindungen und Korrelationen zwischen Datensätzen und ihren Variablen visualisieren. | [Lektion](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | Sinnvolle Visualisierungen | [Datenvisualisierung](3-Data-Visualization/README.md) | Techniken und Leitlinien, um Ihre Visualisierungen wertvoll für effektive Problemlösungen und Erkenntnisse zu machen. | [Lektion](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | Einführung in den Data Science-Lebenszyklus | [Lebenszyklus](4-Data-Science-Lifecycle/README.md) | Einführung in den Data Science-Lebenszyklus und seinen ersten Schritt: Daten erfassen und extrahieren. | [Lektion](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | Analyse | [Lebenszyklus](4-Data-Science-Lifecycle/README.md) | Diese Phase des Data Science-Lebenszyklus konzentriert sich auf Techniken zur Datenanalyse. | [Lektion](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | Kommunikation | [Lebenszyklus](4-Data-Science-Lifecycle/README.md) | Diese Phase des Data Science-Lebenszyklus konzentriert sich darauf, die Erkenntnisse aus den Daten so zu präsentieren, dass Entscheidungsträger sie leichter verstehen können. | [Lektion](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | Data Science in der Cloud | [Cloud-Daten](5-Data-Science-In-Cloud/README.md) | Diese Serie von Lektionen führt in Data Science in der Cloud und ihre Vorteile ein. | [Lektion](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) und [Maud](https://twitter.com/maudstweets) |
| 18 | Data Science in der Cloud | [Cloud-Daten](5-Data-Science-In-Cloud/README.md) | Modelle mit Low-Code-Tools trainieren. |[Lektion](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) und [Maud](https://twitter.com/maudstweets) |
| 19 | Data Science in der Cloud | [Cloud-Daten](5-Data-Science-In-Cloud/README.md) | Modelle mit Azure Machine Learning Studio bereitstellen. | [Lektion](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) und [Maud](https://twitter.com/maudstweets) |
| 20 | Data Science in der Praxis | [In der Praxis](6-Data-Science-In-Wild/README.md) | Datenwissenschaftlich getriebene Projekte in der realen Welt. | [Lektion](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

Folgen Sie diesen Schritten, um dieses Beispiel in einem Codespace zu öffnen:
1. Klicken Sie auf das Code-Dropdown-Menü und wählen Sie die Option Mit Codespaces öffnen.
2. Wählen Sie + Neuer Codespace unten im Fenster.
Weitere Informationen finden Sie in der [GitHub-Dokumentation](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace).

## VSCode Remote - Containers
Folgen Sie diesen Schritten, um dieses Repository in einem Container mit Ihrer lokalen Maschine und VSCode mithilfe der VS Code Remote - Containers-Erweiterung zu öffnen:

1. Wenn Sie zum ersten Mal einen Entwicklungscontainer verwenden, stellen Sie sicher, dass Ihr System die Voraussetzungen erfüllt (z. B. Docker installiert ist), wie in der [Einführungsdokumentation](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started) beschrieben.

Um dieses Repository zu verwenden, können Sie entweder das Repository in einem isolierten Docker-Volume öffnen:

**Hinweis**: Im Hintergrund wird der Remote-Containers-Befehl **Repository in Container-Volume klonen...** verwendet, um den Quellcode in einem Docker-Volume anstelle des lokalen Dateisystems zu klonen. [Volumes](https://docs.docker.com/storage/volumes/) sind das bevorzugte Mechanismus zur Persistierung von Containerdaten.

Oder öffnen Sie eine lokal geklonte oder heruntergeladene Version des Repositorys:

- Klonen Sie dieses Repository auf Ihr lokales Dateisystem.
- Drücken Sie F1 und wählen Sie den Befehl **Remote-Containers: Ordner im Container öffnen...**.
- Wählen Sie die geklonte Kopie dieses Ordners, warten Sie, bis der Container gestartet ist, und probieren Sie es aus.

## Offline-Zugriff

Sie können diese Dokumentation offline ausführen, indem Sie [Docsify](https://docsify.js.org/#/) verwenden. Forken Sie dieses Repository, [installieren Sie Docsify](https://docsify.js.org/#/quickstart) auf Ihrer lokalen Maschine, und geben Sie dann im Stammordner dieses Repositorys `docsify serve` ein. Die Website wird auf Port 3000 auf Ihrem localhost bereitgestellt: `localhost:3000`.

> Hinweis: Notebooks werden nicht über Docsify gerendert, daher sollten Sie ein Notebook separat in VS Code mit einem Python-Kernel ausführen.

## Weitere Lehrpläne

Unser Team erstellt weitere Lehrpläne! Schauen Sie sich an:

- [Generative KI für Anfänger](https://aka.ms/genai-beginners)
- [Generative KI für Anfänger .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative KI mit JavaScript](https://github.com/microsoft/generative-ai-with-javascript)
- [Generative KI mit Java](https://aka.ms/genaijava)
- [KI für Anfänger](https://aka.ms/ai-beginners)
- [Data Science für Anfänger](https://aka.ms/datascience-beginners)
- [ML für Anfänger](https://aka.ms/ml-beginners)
- [Cybersicherheit für Anfänger](https://github.com/microsoft/Security-101) 
- [Webentwicklung für Anfänger](https://aka.ms/webdev-beginners)
- [IoT für Anfänger](https://aka.ms/iot-beginners)
- [XR-Entwicklung für Anfänger](https://github.com/microsoft/xr-development-for-beginners)
- [GitHub Copilot für Pair-Programming meistern](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)
- [GitHub Copilot für C#/.NET-Entwickler meistern](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers)
- [Wählen Sie Ihr eigenes Copilot-Abenteuer](https://github.com/microsoft/CopilotAdventures)

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.