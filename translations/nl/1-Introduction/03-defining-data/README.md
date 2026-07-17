# Data Definiëren

|![ Sketchnote door [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Data Definiëren - _Sketchnote door [@nitya](https://twitter.com/nitya)_ |

Data is feiten, informatie, observaties en metingen die worden gebruikt om ontdekkingen te doen en om geïnformeerde beslissingen te ondersteunen. Een datapunt is een enkele eenheid data binnen een dataset, wat een verzameling datapoints is. Datasets kunnen in verschillende formaten en structuren voorkomen en zullen meestal gebaseerd zijn op de bron, of waar de data vandaan komt. Bijvoorbeeld, de maandelijkse inkomsten van een bedrijf kunnen in een spreadsheet staan, maar uurlijkse hartslagdata van een smartwatch kunnen in [JSON](https://stackoverflow.com/a/383699) formaat zijn. Het is gebruikelijk dat datawetenschappers met verschillende soorten data binnen een dataset werken.

Deze les richt zich op het identificeren en classificeren van data op basis van de kenmerken en de bronnen.

## [Pre-Lectuur Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Hoe Data Wordt Beschreven

### Ruwe Data
Ruwe data is data die afkomstig is van de bron in de oorspronkelijke staat en niet is geanalyseerd of georganiseerd. Om te begrijpen wat er gebeurt met een dataset, moet deze worden georganiseerd in een formaat dat zowel door mensen als de technologie die ze mogelijk gebruiken om het verder te analyseren, begrepen kan worden. De structuur van een dataset beschrijft hoe het georganiseerd is en kan worden geclassificeerd als gestructureerd, ongestructureerd en semi-gestructureerd. Deze soorten structuren zullen variëren, afhankelijk van de bron maar zullen uiteindelijk in deze drie categorieën passen.

### Kwantitatieve Data
Kwantitatieve data zijn numerieke observaties binnen een dataset en kunnen typisch worden geanalyseerd, gemeten en wiskundig gebruikt. Enkele voorbeelden van kwantitatieve data zijn: de bevolking van een land, de lengte van een persoon of de kwartaalomzet van een bedrijf. Met wat extra analyse kan kwantitatieve data worden gebruikt om seizoensgebonden trends van de Luchtkwaliteitsindex (AQI) te ontdekken of de waarschijnlijkheid van spitsuurverkeer op een typische werkdag te schatten.

### Kwalitatieve Data
Kwalitatieve data, ook bekend als categorische data, zijn data die niet objectief kunnen worden gemeten zoals observaties van kwantitatieve data. Het is over het algemeen verschillende vormen van subjectieve data die de kwaliteit van iets vastleggen, zoals een product of proces. Soms is kwalitatieve data numeriek en wordt het normaal gesproken niet wiskundig gebruikt, zoals telefoonnummers of tijdstempels. Enkele voorbeelden van kwalitatieve data zijn: videocomentaren, het merk en model van een auto of de favoriete kleur van je beste vrienden. Kwalitatieve data kan worden gebruikt om te begrijpen welke producten consumenten het leukst vinden of het identificeren van populaire zoekwoorden in sollicitatieresumes.

### Gestructureerde Data
Gestructureerde data is data die is georganiseerd in rijen en kolommen, waarbij elke rij dezelfde set kolommen heeft. Kolommen representeren een waarde van een bepaald type en worden geïdentificeerd met een naam die beschrijft wat de waarde vertegenwoordigt, terwijl rijen de daadwerkelijke waarden bevatten. Kolommen hebben vaak een specifiek stel regels of beperkingen op de waarden om ervoor te zorgen dat de waarden de kolom nauwkeurig vertegenwoordigen. Stel bijvoorbeeld een spreadsheet voor van klanten waar elke rij een telefoonnummer moet hebben en de telefoonnummers nooit alfabetische tekens bevatten. Er kunnen regels worden toegepast op de telefoonnummerkolom om ervoor te zorgen dat deze nooit leeg is en alleen nummers bevat.

Een voordeel van gestructureerde data is dat het zo georganiseerd kan worden dat het gerelateerd kan worden aan andere gestructureerde data. Echter, omdat de data is ontworpen om op een specifieke manier georganiseerd te worden, kan het veel moeite kosten om wijzigingen aan te brengen in de algemene structuur. Bijvoorbeeld, het toevoegen van een e-mailkolom aan de klantenspreadsheet die niet leeg mag zijn betekent dat je moet uitzoeken hoe je deze waarden aan de bestaande rijen van klanten in de dataset toevoegt.

Voorbeelden van gestructureerde data: spreadsheets, relationele databases, telefoonnummers, bankafschriften

### Ongestructureerde Data
Ongestructureerde data kan meestal niet worden gecategoriseerd in rijen of kolommen en bevat geen formaat of reeks regels om te volgen. Omdat ongestructureerde data minder beperkingen heeft op zijn structuur, is het gemakkelijker om nieuwe informatie toe te voegen in vergelijking met een gestructureerde dataset. Als een sensor die data meet over barometrische druk elke 2 minuten een update ontvangt waardoor het nu temperatuur kan meten en registreren, is het niet nodig de bestaande data aan te passen als het ongestructureerd is. Dit kan er echter voor zorgen dat het analyseren of onderzoeken van dit type data langer duurt. Bijvoorbeeld, een wetenschapper die het gemiddelde van de temperatuur van de vorige maand wil vinden vanuit de sensordata, maar ontdekt dat de sensor een "e" heeft geregistreerd in sommige data om aan te geven dat hij stuk was in plaats van een typisch nummer, wat betekent dat de data incompleet is.

Voorbeelden van ongestructureerde data: tekstbestanden, tekstberichten, videobestanden

### Semi-gestructureerd
Semi-gestructureerde data heeft kenmerken die het een combinatie maken van gestructureerde en ongestructureerde data. Het voldoet meestal niet aan het formaat van rijen en kolommen, maar is georganiseerd op een manier die als gestructureerd wordt beschouwd en kan een vast formaat of reeks regels volgen. De structuur kan variëren tussen bronnen, van een goed gedefinieerde hiërarchie tot iets flexibels dat gemakkelijke integratie van nieuwe informatie toestaat. Metadata zijn indicatoren die helpen te bepalen hoe de data is georganiseerd en opgeslagen en zullen verschillende namen hebben, afhankelijk van het type data. Veelvoorkomende namen voor metadata zijn tags, elementen, entiteiten en attributen. Bijvoorbeeld, een typische e-mail heeft een onderwerp, inhoud en een set ontvangers en kan worden georganiseerd op wie of wanneer het is verzonden.

Voorbeelden van semi-gestructureerde data: HTML, CSV-bestanden, JavaScript Object Notation (JSON)

## Bronnen van Data

Een databron is de oorspronkelijke locatie waar de data is gegenereerd, of waar het "woont" en zal variëren afhankelijk van hoe en wanneer het werd verzameld. Data gegenereerd door de gebruiker(s) worden primaire data genoemd, terwijl secundaire data afkomstig is van een bron die gegevens heeft verzameld voor algemeen gebruik. Bijvoorbeeld, een groep wetenschappers die observaties verzamelt in een regenwoud wordt als primair beschouwd en als ze het met andere wetenschappers delen wordt het beschouwd als secundair voor degenen die het gebruiken.

Databases zijn een veelvoorkomende bron en vertrouwen op een databasebeheersysteem om de data te hosten en te onderhouden waar gebruikers commando's genaamd queries gebruiken om de data te verkennen. Bestanden als databronnen kunnen audio-, beeld- en videobestanden zijn evenals spreadsheets zoals Excel. Internetbronnen zijn een veelvoorkomende locatie voor het hosten van data, waar databases en bestanden te vinden zijn. Application programming interfaces, ook wel API's genoemd, stellen programmeurs in staat manieren te creëren om data te delen met externe gebruikers via het internet, terwijl het proces van web scraping data van een webpagina extraheert. De [lessen in Werken met Data](../../../../../../../../../2-Working-With-Data) richten zich op hoe verschillende databronnen te gebruiken.

## Conclusie

In deze les hebben we geleerd:

- Wat data is
- Hoe data wordt beschreven
- Hoe data wordt geclassificeerd en gecategoriseerd
- Waar data te vinden is

## 🚀 Uitdaging

Kaggle is een uitstekende bron van open datasets. Gebruik de [dataset zoektool](https://www.kaggle.com/datasets) om interessante datasets te vinden en classificeer 3-5 datasets volgens dit criterium:

- Is de data kwantitatief of kwalitatief?
- Is de data gestructureerd, ongestructureerd of semi-gestructureerd?

## [Post-lectuur quiz](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Review & Zelfstudie

- Deze Microsoft Learn-unit, getiteld [Identificeer dataformaten](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text) heeft een gedetailleerde uiteenzetting van gestructureerde, semi-gestructureerde en ongestructureerde data.

## Opdracht

[Datasets Classificeren](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->