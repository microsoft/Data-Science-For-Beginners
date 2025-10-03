<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58860ce9a4b8a564003d2752f7c72851",
  "translation_date": "2025-10-03T15:59:55+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "de"
}
-->
# Einführung in Datenethik

|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Datenethik - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

---

Wir sind alle Datenbürger, die in einer datengetriebenen Welt leben.

Markttrends zeigen, dass bis 2022 jede dritte große Organisation ihre Daten über Online-[Marktplätze und Börsen](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/) kaufen und verkaufen wird. Als **App-Entwickler** wird es für uns einfacher und kostengünstiger, datengesteuerte Erkenntnisse und algorithmusgesteuerte Automatisierung in den täglichen Nutzererfahrungen zu integrieren. Doch während KI allgegenwärtig wird, müssen wir auch die potenziellen Schäden verstehen, die durch die [Instrumentalisierung](https://www.youtube.com/watch?v=TQHs8SA1qpk) solcher Algorithmen in großem Maßstab entstehen können.

Trends deuten darauf hin, dass wir bis 2025 über [180 Zettabyte](https://www.statista.com/statistics/871513/worldwide-data-created/) an Daten erzeugen und konsumieren werden. Für **Datenwissenschaftler** bietet diese Informationsflut beispiellosen Zugang zu persönlichen und Verhaltensdaten. Damit kommt die Macht, detaillierte Nutzerprofile zu erstellen und subtil Entscheidungen zu beeinflussen – oft auf eine Weise, die eine [Illusion der freien Wahl](https://www.datasciencecentral.com/the-pareto-set-and-the-paradox-of-choice/) fördert. Dies kann genutzt werden, um Nutzer zu bevorzugten Ergebnissen zu lenken, wirft jedoch auch kritische Fragen zu Datenschutz, Autonomie und den ethischen Grenzen algorithmischer Einflussnahme auf.

Datenethik sind heute _notwendige Leitplanken_ für Datenwissenschaft und Ingenieurwesen, um potenzielle Schäden und unbeabsichtigte Konsequenzen unserer datengetriebenen Handlungen zu minimieren. Der [Gartner Hype Cycle für KI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) identifiziert relevante Trends in digitaler Ethik, verantwortungsvoller KI und KI-Governance als Schlüsseltreiber für größere Megatrends rund um die _Demokratisierung_ und _Industrialisierung_ von KI.

![Gartner's Hype Cycle für KI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

In dieser Lektion werden wir den faszinierenden Bereich der Datenethik erkunden – von grundlegenden Konzepten und Herausforderungen bis hin zu Fallstudien und angewandten KI-Konzepten wie Governance –, die dazu beitragen, eine Ethikkultur in Teams und Organisationen zu etablieren, die mit Daten und KI arbeiten.

## [Quiz vor der Vorlesung](https://ff-quizzes.netlify.app/en/ds/quiz/2) 🎯

## Grundlegende Definitionen

Beginnen wir mit dem Verständnis der grundlegenden Terminologie.

Das Wort "Ethik" stammt aus dem [griechischen Wort "ethikos"](https://en.wikipedia.org/wiki/Ethics) (und dessen Wurzel "ethos"), was _Charakter oder moralische Natur_ bedeutet.

**Ethik** bezieht sich auf die gemeinsamen Werte und moralischen Prinzipien, die unser Verhalten in der Gesellschaft bestimmen. Ethik basiert nicht auf Gesetzen, sondern auf allgemein akzeptierten Normen dessen, was "richtig vs. falsch" ist. Dennoch können ethische Überlegungen Initiativen zur Unternehmensführung und staatliche Vorschriften beeinflussen, die mehr Anreize für die Einhaltung schaffen.

**Datenethik** ist ein [neuer Zweig der Ethik](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1), der "moralische Probleme im Zusammenhang mit _Daten, Algorithmen und entsprechenden Praktiken_ untersucht und bewertet". Hierbei konzentriert sich **"Daten"** auf Aktionen im Zusammenhang mit Erzeugung, Aufzeichnung, Pflege, Verarbeitung, Verbreitung, Teilen und Nutzung, **"Algorithmen"** auf KI, Agenten, maschinelles Lernen und Roboter, und **"Praktiken"** auf Themen wie verantwortungsvolle Innovation, Programmierung, Hacking und Ethikkodizes.

**Angewandte Ethik** ist die [praktische Anwendung moralischer Überlegungen](https://en.wikipedia.org/wiki/Applied_ethics). Es handelt sich um den Prozess der aktiven Untersuchung ethischer Fragen im Kontext von _realen Handlungen, Produkten und Prozessen_ und der Ergreifung von Korrekturmaßnahmen, um sicherzustellen, dass diese mit unseren definierten ethischen Werten übereinstimmen.

**Ethikkultur** bezieht sich auf die [_Operationalisierung_ der angewandten Ethik](https://hbr.org/2019/05/how-to-design-an-ethical-organization), um sicherzustellen, dass unsere ethischen Prinzipien und Praktiken konsistent und skalierbar in der gesamten Organisation übernommen werden. Erfolgreiche Ethikkulturen definieren organisationsweite ethische Prinzipien, bieten sinnvolle Anreize für die Einhaltung und verstärken ethische Normen, indem sie gewünschte Verhaltensweisen auf allen Ebenen der Organisation fördern und verstärken.

## Ethikkonzepte

In diesem Abschnitt werden wir Konzepte wie **gemeinsame Werte** (Prinzipien) und **ethische Herausforderungen** (Probleme) für die Datenethik diskutieren – und **Fallstudien** untersuchen, die Ihnen helfen, diese Konzepte in realen Kontexten zu verstehen.

### 1. Ethische Prinzipien

Jede Datenethikstrategie beginnt mit der Definition von _ethischen Prinzipien_ – den "gemeinsamen Werten", die akzeptables Verhalten beschreiben und konforme Handlungen in unseren Daten- und KI-Projekten leiten. Sie können diese auf individueller oder Teamebene definieren. Die meisten großen Organisationen legen diese jedoch in einer _ethischen KI-Missionserklärung_ oder einem Rahmenwerk fest, das auf Unternehmensebene definiert und konsistent über alle Teams hinweg durchgesetzt wird.

**Beispiel:** Microsofts [Verantwortungsvolle KI](https://www.microsoft.com/en-us/ai/responsible-ai)-Missionserklärung lautet: _"Wir sind der Förderung von KI verpflichtet, die von ethischen Prinzipien geleitet wird und den Menschen in den Mittelpunkt stellt"_ – und identifiziert 6 ethische Prinzipien im untenstehenden Rahmenwerk:

![Verantwortungsvolle KI bei Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Lassen Sie uns diese Prinzipien kurz erkunden. _Transparenz_ und _Verantwortlichkeit_ sind grundlegende Werte, auf denen andere Prinzipien aufbauen – beginnen wir also damit:

* [**Verantwortlichkeit**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) macht Praktiker _verantwortlich_ für ihre Daten- und KI-Operationen sowie die Einhaltung dieser ethischen Prinzipien.
* [**Transparenz**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) stellt sicher, dass Daten- und KI-Aktionen für Nutzer _verständlich_ (interpretierbar) sind und die Entscheidungen sowie deren Gründe erklärt werden.
* [**Fairness**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) – konzentriert sich darauf, sicherzustellen, dass KI _alle Menschen_ fair behandelt und systemische oder implizite sozio-technische Vorurteile in Daten und Systemen angeht.
* [**Zuverlässigkeit & Sicherheit**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) – stellt sicher, dass KI _konsistent_ mit definierten Werten agiert und potenzielle Schäden oder unbeabsichtigte Konsequenzen minimiert.
* [**Privatsphäre & Sicherheit**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) – bezieht sich auf das Verständnis der Datenherkunft und bietet Nutzern _Datenschutz und verwandte Schutzmaßnahmen_.
* [**Inklusivität**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) – geht darum, KI-Lösungen mit Absicht zu gestalten und sie so anzupassen, dass sie _eine breite Palette menschlicher Bedürfnisse_ und Fähigkeiten erfüllen.

> 🚨 Überlegen Sie, was Ihre Datenethik-Missionserklärung sein könnte. Erkunden Sie ethische KI-Rahmenwerke anderer Organisationen – hier sind Beispiele von [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles) und [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Welche gemeinsamen Werte haben sie? Wie beziehen sich diese Prinzipien auf das KI-Produkt oder die Branche, in der sie tätig sind?

### 2. Ethische Herausforderungen

Sobald wir ethische Prinzipien definiert haben, besteht der nächste Schritt darin, unsere Daten- und KI-Aktionen zu bewerten, um festzustellen, ob sie mit diesen gemeinsamen Werten übereinstimmen. Denken Sie über Ihre Aktionen in zwei Kategorien nach: _Datenerhebung_ und _Algorithmendesign_.

Bei der Datenerhebung werden Aktionen wahrscheinlich **persönliche Daten** oder persönlich identifizierbare Informationen (PII) für identifizierbare lebende Personen umfassen. Dazu gehören [verschiedene Arten nicht-personenbezogener Daten](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en), die _zusammen_ eine Person identifizieren können. Ethische Herausforderungen können sich auf _Datenschutz_, _Datenbesitz_ und verwandte Themen wie _informierte Zustimmung_ und _geistige Eigentumsrechte_ für Nutzer beziehen.

Beim Algorithmendesign umfassen Aktionen das Sammeln und Pflegen von **Datensätzen**, die dann verwendet werden, um **Datenmodelle** zu trainieren und einzusetzen, die Ergebnisse vorhersagen oder Entscheidungen in realen Kontexten automatisieren. Ethische Herausforderungen können sich aus _Datensatzverzerrungen_, _Datenqualitätsproblemen_, _Unfairness_ und _Fehldarstellungen_ in Algorithmen ergeben – einschließlich einiger systemischer Probleme.

In beiden Fällen heben ethische Herausforderungen Bereiche hervor, in denen unsere Aktionen möglicherweise mit unseren gemeinsamen Werten in Konflikt geraten. Um diese Bedenken zu erkennen, zu mindern, zu minimieren oder zu beseitigen, müssen wir moralische "Ja/Nein"-Fragen zu unseren Aktionen stellen und gegebenenfalls Korrekturmaßnahmen ergreifen. Schauen wir uns einige ethische Herausforderungen und die moralischen Fragen an, die sie aufwerfen:

#### 2.1 Datenbesitz

Die Datenerhebung umfasst oft persönliche Daten, die die Datensubjekte identifizieren können. [Datenbesitz](https://permission.io/blog/data-ownership) bezieht sich auf _Kontrolle_ und [_Nutzerrechte_](https://permission.io/blog/data-ownership) im Zusammenhang mit der Erstellung, Verarbeitung und Verbreitung von Daten.

Die moralischen Fragen, die wir stellen müssen, sind:
 * Wem gehören die Daten? (Nutzer oder Organisation)
 * Welche Rechte haben Datensubjekte? (z. B. Zugriff, Löschung, Übertragbarkeit)
 * Welche Rechte haben Organisationen? (z. B. Korrektur böswilliger Nutzerbewertungen)

#### 2.2 Informierte Zustimmung

[Informierte Zustimmung](https://legaldictionary.net/informed-consent/) definiert den Akt, bei dem Nutzer einer Aktion (wie der Datenerhebung) mit einem _vollständigen Verständnis_ relevanter Fakten einschließlich Zweck, potenzieller Risiken und Alternativen zustimmen.

Fragen, die hier zu erkunden sind:
 * Hat der Nutzer (Datensubjekt) die Erfassung und Nutzung von Daten erlaubt?
 * Hat der Nutzer den Zweck verstanden, für den die Daten erfasst wurden?
 * Hat der Nutzer die potenziellen Risiken seiner Teilnahme verstanden?

#### 2.3 Geistiges Eigentum

[Geistiges Eigentum](https://en.wikipedia.org/wiki/Intellectual_property) bezieht sich auf immaterielle Schöpfungen, die aus menschlicher Initiative resultieren und _wirtschaftlichen Wert_ für Einzelpersonen oder Unternehmen haben können.

Fragen, die hier zu erkunden sind:
 * Hatten die gesammelten Daten wirtschaftlichen Wert für einen Nutzer oder ein Unternehmen?
 * Hat der **Nutzer** hier geistiges Eigentum?
 * Hat die **Organisation** hier geistiges Eigentum?
 * Wenn diese Rechte existieren, wie schützen wir sie?

#### 2.4 Datenschutz

[Datenschutz](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) oder Informationsschutz bezieht sich auf die Wahrung der Privatsphäre und den Schutz der Identität von Nutzern in Bezug auf persönlich identifizierbare Informationen.

Fragen, die hier zu erkunden sind:
 * Sind die (persönlichen) Daten der Nutzer gegen Hacks und Lecks gesichert?
 * Sind die Daten der Nutzer nur für autorisierte Nutzer und Kontexte zugänglich?
 * Wird die Anonymität der Nutzer gewahrt, wenn Daten geteilt oder verbreitet werden?
 * Kann ein Nutzer aus anonymisierten Datensätzen de-identifiziert werden?

#### 2.5 Recht auf Vergessenwerden

Das [Recht auf Vergessenwerden](https://en.wikipedia.org/wiki/Right_to_be_forgotten) oder [Recht auf Löschung](https://www.gdpreu.org/right-to-be-forgotten/) bietet Nutzern zusätzlichen Schutz persönlicher Daten. Insbesondere gibt es Nutzern das Recht, die Löschung oder Entfernung persönlicher Daten aus Internetsuchen und anderen Orten _unter bestimmten Umständen_ zu verlangen – und ihnen so einen Neuanfang online zu ermöglichen, ohne dass vergangene Handlungen gegen sie verwendet werden.

Fragen, die hier zu erkunden sind:
 * Ermöglicht das System Datensubjekten, die Löschung zu beantragen?
 * Sollte der Widerruf der Nutzerzustimmung eine automatisierte Löschung auslösen?
 * Wurden Daten ohne Zustimmung oder auf rechtswidrige Weise erhoben?
 * Sind wir konform mit staatlichen Vorschriften zum Datenschutz?

#### 2.6 Datensatzverzerrung

Datensatz- oder [Erhebungsverzerrung](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) bezieht sich auf die Auswahl eines _nicht repräsentativen_ Teils von Daten für die Algorithmusentwicklung, was potenzielle Unfairness in den Ergebnissen für verschiedene Gruppen schaffen kann. Arten von Verzerrungen umfassen Auswahl- oder Stichprobenverzerrung, Freiwilligenverzerrung und Instrumentenverzerrung.

Fragen, die hier zu erkunden sind:
 * Haben wir eine repräsentative Gruppe von Datensubjekten rekrutiert?
 * Haben wir unseren gesammelten oder gepflegten Datensatz auf verschiedene Verzerrungen getestet?
 * Können wir entdeckte Verzerrungen mindern oder entfernen?

#### 2.7 Datenqualität

[Datenqualität](https://lakefs.io/data-quality-testing/) untersucht die Validität des gepflegten Datensatzes, der zur Entwicklung unserer Algorithmen verwendet wird, und prüft, ob Merkmale und Datensätze die Anforderungen an die Genauigkeit und Konsistenz für unseren KI-Zweck erfüllen.

Fragen, die hier zu erkunden sind:
 * Haben wir gültige _Merkmale_ für unseren Anwendungsfall erfasst?
 * Wurden Daten _konsistent_ über verschiedene Datenquellen hinweg erfasst?
 * Ist der Datensatz _vollständig_ für verschiedene Bedingungen oder Szenarien?
* Wird die Information _genau_ erfasst und spiegelt sie die Realität wider?

#### 2.8 Fairness von Algorithmen

[Fairness von Algorithmen](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) untersucht, ob das Design des Algorithmus systematisch bestimmte Untergruppen von Datenpersonen diskriminiert, was zu [potenziellen Schäden](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) in der _Ressourcenverteilung_ (bei der Ressourcen verweigert oder zurückgehalten werden) und der _Servicequalität_ (bei der KI für einige Untergruppen weniger genau ist als für andere) führen kann.

Fragen, die hier untersucht werden sollten:
* Haben wir die Modellgenauigkeit für verschiedene Untergruppen und Bedingungen bewertet?
* Haben wir das System auf potenzielle Schäden (z. B. Stereotypisierung) überprüft?
* Können wir Daten überarbeiten oder Modelle neu trainieren, um identifizierte Schäden zu mindern?

Erkunden Sie Ressourcen wie [Checklisten zur Fairness von KI](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA), um mehr zu erfahren.

#### 2.9 Fehlrepräsentation

[Fehlrepräsentation von Daten](https://www.sciencedirect.com/topics/computer-science/misrepresentation) bezieht sich darauf, ob wir Erkenntnisse aus ehrlich berichteten Daten auf eine täuschende Weise kommunizieren, um eine gewünschte Erzählung zu unterstützen.

Fragen, die hier untersucht werden sollten:
* Berichten wir unvollständige oder ungenaue Daten?
* Visualisieren wir Daten so, dass sie zu irreführenden Schlussfolgerungen führen?
* Verwenden wir selektive statistische Techniken, um Ergebnisse zu manipulieren?
* Gibt es alternative Erklärungen, die zu einer anderen Schlussfolgerung führen könnten?

#### 2.10 Freie Wahl

Die [Illusion der freien Wahl](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) tritt auf, wenn "Entscheidungsarchitekturen" von Systemen Algorithmen verwenden, um Menschen dazu zu bewegen, ein bevorzugtes Ergebnis zu wählen, während sie scheinbar Optionen und Kontrolle haben. Diese [dunklen Muster](https://www.darkpatterns.org/) können sozialen und wirtschaftlichen Schaden für Nutzer verursachen. Da Nutzerentscheidungen Verhaltensprofile beeinflussen, können diese Aktionen zukünftige Entscheidungen antreiben, die die Auswirkungen dieser Schäden verstärken oder verlängern.

Fragen, die hier untersucht werden sollten:
* Hat der Nutzer die Auswirkungen dieser Entscheidung verstanden?
* War sich der Nutzer der (alternativen) Optionen und der Vor- und Nachteile jeder Option bewusst?
* Kann der Nutzer eine automatisierte oder beeinflusste Entscheidung später rückgängig machen?

### 3. Fallstudien

Um diese ethischen Herausforderungen in realen Kontexten zu verstehen, hilft es, Fallstudien zu betrachten, die die potenziellen Schäden und Konsequenzen für Einzelpersonen und die Gesellschaft aufzeigen, wenn solche ethischen Verstöße übersehen werden.

Hier sind einige Beispiele:

| Ethische Herausforderung | Fallstudie | 
|--- |--- |
| **Informierte Zustimmung** | 1972 - [Tuskegee-Syphilis-Studie](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Afroamerikanische Männer, die an der Studie teilnahmen, wurden kostenlose medizinische Versorgung versprochen, _aber von Forschern getäuscht_, die die Teilnehmer nicht über ihre Diagnose oder die Verfügbarkeit von Behandlung informierten. Viele Teilnehmer starben, und Partner oder Kinder waren betroffen; die Studie dauerte 40 Jahre. | 
| **Datenschutz** | 2007 - Der [Netflix-Datenpreis](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) stellte Forschern _10 Millionen anonymisierte Filmbewertungen von 50.000 Kunden_ zur Verfügung, um Empfehlungsalgorithmen zu verbessern. Forscher konnten jedoch anonymisierte Daten mit persönlich identifizierbaren Daten in _externen Datensätzen_ (z. B. IMDb-Kommentaren) korrelieren und einige Netflix-Abonnenten effektiv "de-anonymisieren". |
| **Sammlungsbias** | 2013 - Die Stadt Boston [entwickelte Street Bump](https://www.boston.gov/transportation/street-bump), eine App, mit der Bürger Schlaglöcher melden konnten, um der Stadt bessere Straßendaten zur Verfügung zu stellen. Allerdings hatten [Menschen in einkommensschwächeren Gruppen weniger Zugang zu Autos und Telefonen](https://hbr.org/2013/04/the-hidden-biases-in-big-data), wodurch ihre Straßenprobleme in dieser App unsichtbar wurden. Entwickler arbeiteten mit Akademikern zusammen, um _Probleme des gerechten Zugangs und der digitalen Kluft_ für mehr Fairness zu lösen. |
| **Fairness von Algorithmen** | 2018 - Die MIT-Studie [Gender Shades](http://gendershades.org/overview.html) bewertete die Genauigkeit von KI-Produkten zur Geschlechtsklassifikation und deckte Lücken in der Genauigkeit für Frauen und farbige Personen auf. Eine [Apple Card 2019](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) schien Frauen weniger Kredit zu gewähren als Männern. Beide Fälle illustrierten Probleme des algorithmischen Bias, die zu sozioökonomischen Schäden führten. |
| **Fehlrepräsentation von Daten** | 2020 - Das [Georgia Department of Public Health veröffentlichte COVID-19-Diagramme](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening), die Bürger über Trends bei bestätigten Fällen mit nicht-chronologischer Reihenfolge auf der x-Achse irreführen sollten. Dies zeigt Fehlrepräsentation durch Visualisierungstricks. |
| **Illusion der freien Wahl** | 2020 - Lern-App [ABCmouse zahlte $10M, um eine FTC-Beschwerde beizulegen](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/), bei der Eltern in Abonnements gefangen waren, die sie nicht kündigen konnten. Dies zeigt dunkle Muster in Entscheidungsarchitekturen, bei denen Nutzer zu potenziell schädlichen Entscheidungen gedrängt wurden. |
| **Datenschutz & Nutzerrechte** | 2021 - Facebook [Datenleck](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) enthüllte Daten von 530 Millionen Nutzern, was zu einer $5B-Einigung mit der FTC führte. Facebook weigerte sich jedoch, die Nutzer über das Leck zu informieren, was die Nutzerrechte in Bezug auf Datentransparenz und Zugang verletzte. |

Möchten Sie weitere Fallstudien erkunden? Schauen Sie sich diese Ressourcen an:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - ethische Dilemmata in verschiedenen Branchen.
* [Data Science Ethics course](https://www.coursera.org/learn/data-science-ethics#syllabus) - wegweisende Fallstudien.
* [Wo Dinge schiefgelaufen sind](https://deon.drivendata.org/examples/) - Deon-Checkliste mit Beispielen.

> 🚨 Denken Sie an die Fallstudien, die Sie gesehen haben – haben Sie ähnliche ethische Herausforderungen in Ihrem Leben erlebt oder waren davon betroffen? Können Sie mindestens eine weitere Fallstudie nennen, die eine der ethischen Herausforderungen in diesem Abschnitt illustriert?

## Angewandte Ethik

Wir haben über ethische Konzepte, Herausforderungen und Fallstudien in realen Kontexten gesprochen. Aber wie beginnen wir, _ethische Prinzipien und Praktiken_ in unseren Projekten anzuwenden? Und wie _operationalisieren_ wir diese Praktiken für eine bessere Governance? Lassen Sie uns einige Lösungen aus der Praxis erkunden:

### 1. Berufliche Kodizes

Berufliche Kodizes bieten eine Möglichkeit für Organisationen, Mitglieder zu "motivieren", ihre ethischen Prinzipien und ihre Mission zu unterstützen. Kodizes sind _moralische Leitlinien_ für berufliches Verhalten, die Mitarbeitern oder Mitgliedern helfen, Entscheidungen zu treffen, die mit den Prinzipien ihrer Organisation übereinstimmen. Sie sind nur so gut wie die freiwillige Einhaltung durch die Mitglieder; viele Organisationen bieten jedoch zusätzliche Belohnungen und Strafen, um die Einhaltung zu fördern.

Beispiele:
* [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Ethikkodex
* [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Verhaltenskodex (erstellt 2013)
* [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (seit 1993)

> 🚨 Sind Sie Mitglied einer professionellen Ingenieur- oder Datenwissenschaftsorganisation? Erkunden Sie deren Website, um zu sehen, ob sie einen beruflichen Ethikkodex definieren. Was sagt dieser über ihre ethischen Prinzipien aus? Wie motivieren sie Mitglieder, den Kodex zu befolgen?

### 2. Ethik-Checklisten

Während berufliche Kodizes das erforderliche _ethische Verhalten_ von Praktikern definieren, haben sie [bekannte Einschränkungen](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) bei der Durchsetzung, insbesondere in groß angelegten Projekten. Stattdessen befürworten viele Datenwissenschaftler [Checklisten](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), die **Prinzipien mit Praktiken** auf deterministische und umsetzbare Weise verbinden können.

Checklisten wandeln Fragen in "Ja/Nein"-Aufgaben um, die operationalisiert werden können, sodass sie als Teil standardmäßiger Produktfreigabeworkflows verfolgt werden können.

Beispiele:
* [Deon](https://deon.drivendata.org/) - eine allgemeine Checkliste für Datenethik, erstellt aus [Brancheneempfehlungen](https://deon.drivendata.org/#checklist-citations) mit einem Befehlszeilentool für einfache Integration.
* [Privacy Audit Checklist](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - bietet allgemeine Leitlinien für Informationshandhabungspraktiken aus rechtlicher und sozialer Perspektive.
* [AI Fairness Checklist](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - erstellt von KI-Praktikern zur Unterstützung der Integration von Fairness-Checks in KI-Entwicklungszyklen.
* [22 Fragen zur Ethik in Daten und KI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - ein offeneres Framework, strukturiert für die erste Untersuchung ethischer Fragen in Design-, Implementierungs- und Organisationskontexten.

### 3. Ethik-Regulierungen

Ethik bedeutet, gemeinsame Werte zu definieren und das Richtige _freiwillig_ zu tun. **Compliance** bedeutet, _das Gesetz zu befolgen_, wenn und wo es definiert ist. **Governance** umfasst allgemein alle Möglichkeiten, wie Organisationen ethische Prinzipien durchsetzen und gesetzliche Vorschriften einhalten.

Heute nimmt Governance in Organisationen zwei Formen an. Erstens geht es darum, **ethische KI**-Prinzipien zu definieren und Praktiken zu etablieren, um die Einführung in allen KI-bezogenen Projekten der Organisation zu operationalisieren. Zweitens geht es darum, alle staatlich vorgeschriebenen **Datenschutzvorschriften** für die Regionen, in denen sie tätig sind, einzuhalten.

Beispiele für Datenschutz- und Privatsphäre-Regulierungen:
* `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - regelt die Sammlung, Nutzung und Offenlegung persönlicher Informationen durch die _Bundesregierung_.
* `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - schützt persönliche Gesundheitsdaten.
* `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - schützt die Datenprivatsphäre von Kindern unter 13 Jahren.
* `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - bietet Nutzerrechte, Datenschutz und Privatsphäre.
* `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) gibt Verbrauchern mehr _Rechte_ über ihre (persönlichen) Daten.
* `2021`, Chinas [Gesetz zum Schutz persönlicher Informationen](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) wurde gerade verabschiedet und schafft eine der weltweit stärksten Online-Datenschutzvorschriften.

> 🚨 Die Europäische Union hat die GDPR (General Data Protection Regulation) definiert, die heute eine der einflussreichsten Datenschutzvorschriften ist. Wussten Sie, dass sie auch [8 Nutzerrechte](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) definiert, um die digitale Privatsphäre und persönlichen Daten der Bürger zu schützen? Lernen Sie, was diese sind und warum sie wichtig sind.

### 4. Ethikkultur

Beachten Sie, dass es eine immaterielle Lücke zwischen _Compliance_ (genug tun, um "den Buchstaben des Gesetzes" zu erfüllen) und der Bewältigung [systemischer Probleme](https://www.coursera.org/learn/data-science-ethics/home/week/4) (wie Versteinerung, Informationsasymmetrie und Verteilungsungerechtigkeit) gibt, die die Waffenfähigkeit von KI beschleunigen können.

Letzteres erfordert [kollaborative Ansätze zur Definition von Ethikkulturen](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f), die emotionale Verbindungen und konsistente gemeinsame Werte _über Organisationen hinweg_ in der Branche schaffen. Dies erfordert mehr [formalisierte Datenethikkulturen](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) in Organisationen – sodass _jeder_ [die Andon-Schnur ziehen](https://en.wikipedia.org/wiki/Andon_(manufacturing)) kann (um ethische Bedenken frühzeitig im Prozess zu äußern) und _ethische Bewertungen_ (z. B. bei der Einstellung) zu einem Kernkriterium der Teamzusammenstellung in KI-Projekten macht.

---
## [Quiz nach der Vorlesung](https://ff-quizzes.netlify.app/en/ds/quiz/3) 🎯
## Überprüfung & Selbststudium

Kurse und Bücher helfen, die grundlegenden ethischen Konzepte und Herausforderungen zu verstehen, während Fallstudien und Tools bei der Anwendung ethischer Praktiken in realen Kontexten helfen. Hier sind einige Ressourcen, um zu beginnen.
* [Maschinelles Lernen für Anfänger](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - Lektion über Fairness von Microsoft.  
* [Grundsätze der verantwortungsvollen KI](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - kostenloser Lernpfad von Microsoft Learn.  
* [Ethik und Data Science](https://resources.oreilly.com/examples/0636920203964) - O'Reilly E-Book (M. Loukides, H. Mason et. al).  
* [Ethik in der Datenwissenschaft](https://www.coursera.org/learn/data-science-ethics#syllabus) - Online-Kurs der Universität von Michigan.  
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - Fallstudien der Universität von Texas.  

# Aufgabe  

[Schreiben Sie eine Fallstudie zur Datenethik](assignment.md)  

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.