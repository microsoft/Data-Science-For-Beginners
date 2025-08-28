<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "356d12cffc3125db133a2d27b827a745",
  "translation_date": "2025-08-28T15:52:30+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "nl"
}
-->
# Data Definiëren

|![ Sketchnote door [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Data Definiëren - _Sketchnote door [@nitya](https://twitter.com/nitya)_ |

Data zijn feiten, informatie, observaties en metingen die worden gebruikt om ontdekkingen te doen en om weloverwogen beslissingen te ondersteunen. Een datapunt is een enkele eenheid van data binnen een dataset, wat een verzameling van datapunten is. Datasets kunnen in verschillende formaten en structuren voorkomen en zijn meestal gebaseerd op de bron, of waar de data vandaan komt. Bijvoorbeeld, de maandelijkse inkomsten van een bedrijf kunnen in een spreadsheet staan, terwijl gegevens over de hartslag per uur van een smartwatch in [JSON](https://stackoverflow.com/a/383699)-formaat kunnen zijn. Het is gebruikelijk dat datawetenschappers met verschillende soorten data binnen een dataset werken.

Deze les richt zich op het identificeren en classificeren van data op basis van de kenmerken en bronnen ervan.

## [Pre-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)
## Hoe Data Wordt Beschreven

### Ruwe Data
Ruwe data is data die afkomstig is van de bron in zijn oorspronkelijke staat en nog niet is geanalyseerd of georganiseerd. Om te begrijpen wat er met een dataset gebeurt, moet deze worden georganiseerd in een formaat dat begrijpelijk is voor mensen en de technologie die ze mogelijk gebruiken om het verder te analyseren. De structuur van een dataset beschrijft hoe deze is georganiseerd en kan worden geclassificeerd als gestructureerd, ongestructureerd en semi-gestructureerd. Deze structuren variëren afhankelijk van de bron, maar vallen uiteindelijk in een van deze drie categorieën.

### Kwantitatieve Data
Kwantitatieve data zijn numerieke observaties binnen een dataset en kunnen doorgaans worden geanalyseerd, gemeten en wiskundig gebruikt. Enkele voorbeelden van kwantitatieve data zijn: de bevolking van een land, de lengte van een persoon of de kwartaalinkomsten van een bedrijf. Met aanvullende analyses kan kwantitatieve data worden gebruikt om seizoensgebonden trends in de luchtkwaliteitsindex (AQI) te ontdekken of de kans op spitsverkeer op een typische werkdag te schatten.

### Kwalitatieve Data
Kwalitatieve data, ook wel categorische data genoemd, is data die niet objectief kan worden gemeten zoals kwantitatieve data. Het is over het algemeen subjectieve data in verschillende formaten die de kwaliteit van iets vastleggen, zoals een product of proces. Soms is kwalitatieve data numeriek, maar wordt het niet wiskundig gebruikt, zoals telefoonnummers of tijdstempels. Enkele voorbeelden van kwalitatieve data zijn: videocommentaren, het merk en model van een auto of de favoriete kleur van je beste vrienden. Kwalitatieve data kan worden gebruikt om te begrijpen welke producten consumenten het beste vinden of om populaire trefwoorden in sollicitatieresumes te identificeren.

### Gestructureerde Data
Gestructureerde data is data die is georganiseerd in rijen en kolommen, waarbij elke rij dezelfde set kolommen heeft. Kolommen vertegenwoordigen een waarde van een bepaald type en worden geïdentificeerd met een naam die beschrijft wat de waarde vertegenwoordigt, terwijl rijen de daadwerkelijke waarden bevatten. Kolommen hebben vaak een specifieke set regels of beperkingen voor de waarden om ervoor te zorgen dat de waarden de kolom nauwkeurig vertegenwoordigen. Stel je bijvoorbeeld een spreadsheet voor met klanten, waarbij elke rij een telefoonnummer moet hebben en de telefoonnummers nooit alfabetische tekens bevatten. Er kunnen regels worden toegepast op de kolom met telefoonnummers om ervoor te zorgen dat deze nooit leeg is en alleen cijfers bevat.

Een voordeel van gestructureerde data is dat het zo kan worden georganiseerd dat het kan worden gerelateerd aan andere gestructureerde data. Omdat de data echter is ontworpen om op een specifieke manier te worden georganiseerd, kan het veel moeite kosten om wijzigingen aan te brengen in de algehele structuur. Stel bijvoorbeeld dat je een e-mailkolom toevoegt aan de klanten-spreadsheet die niet leeg mag zijn; dan moet je bedenken hoe je deze waarden toevoegt aan de bestaande rijen klanten in de dataset.

Voorbeelden van gestructureerde data: spreadsheets, relationele databases, telefoonnummers, bankafschriften.

### Ongestructureerde Data
Ongestructureerde data kan meestal niet worden gecategoriseerd in rijen of kolommen en bevat geen formaat of set regels om te volgen. Omdat ongestructureerde data minder beperkingen heeft op de structuur, is het gemakkelijker om nieuwe informatie toe te voegen in vergelijking met een gestructureerde dataset. Als een sensor die elke 2 minuten gegevens over luchtdruk vastlegt een update ontvangt waarmee het nu ook temperatuur kan meten en registreren, hoeft de bestaande data niet te worden aangepast als deze ongestructureerd is. Dit kan echter betekenen dat het analyseren of onderzoeken van dit type data langer duurt. Stel bijvoorbeeld dat een wetenschapper de gemiddelde temperatuur van de vorige maand wil berekenen op basis van de gegevens van de sensor, maar ontdekt dat de sensor een "e" heeft geregistreerd in sommige van zijn gegevens om aan te geven dat deze kapot was in plaats van een typisch getal, wat betekent dat de data onvolledig is.

Voorbeelden van ongestructureerde data: tekstbestanden, sms-berichten, videobestanden.

### Semi-gestructureerde Data
Semi-gestructureerde data heeft kenmerken die het een combinatie maken van gestructureerde en ongestructureerde data. Het voldoet meestal niet aan een formaat van rijen en kolommen, maar is georganiseerd op een manier die als gestructureerd wordt beschouwd en kan een vast formaat of een set regels volgen. De structuur varieert per bron, van een goed gedefinieerde hiërarchie tot iets flexibelers dat eenvoudige integratie van nieuwe informatie mogelijk maakt. Metadata zijn indicatoren die helpen bepalen hoe de data is georganiseerd en opgeslagen en hebben verschillende namen, afhankelijk van het type data. Enkele veelvoorkomende namen voor metadata zijn tags, elementen, entiteiten en attributen. Een typisch e-mailbericht heeft bijvoorbeeld een onderwerp, een hoofdtekst en een set ontvangers en kan worden georganiseerd op basis van wie het heeft verzonden of wanneer het is verzonden.

Voorbeelden van semi-gestructureerde data: HTML, CSV-bestanden, JavaScript Object Notation (JSON).

## Bronnen van Data

Een databron is de oorspronkelijke locatie waar de data is gegenereerd of waar het "leeft" en varieert afhankelijk van hoe en wanneer het is verzameld. Data die door de gebruiker(s) zelf wordt gegenereerd, wordt primaire data genoemd, terwijl secundaire data afkomstig is van een bron die data heeft verzameld voor algemeen gebruik. Bijvoorbeeld, een groep wetenschappers die observaties in een regenwoud verzamelt, wordt als primair beschouwd, en als ze besluiten deze te delen met andere wetenschappers, wordt het als secundair beschouwd voor degenen die het gebruiken.

Databases zijn een veelvoorkomende bron en vertrouwen op een databasebeheersysteem om de data te hosten en te onderhouden, waarbij gebruikers opdrachten genaamd queries gebruiken om de data te verkennen. Bestanden als databronnen kunnen audio-, beeld- en videobestanden zijn, evenals spreadsheets zoals Excel. Internetbronnen zijn een veelvoorkomende locatie voor het hosten van data, waar zowel databases als bestanden te vinden zijn. Application programming interfaces, ook wel API's genoemd, stellen programmeurs in staat om manieren te creëren om data via het internet te delen met externe gebruikers, terwijl het proces van webscraping data van een webpagina extraheert. De [lessen in Werken met Data](../../../../../../../../../2-Working-With-Data) richten zich op hoe je verschillende databronnen kunt gebruiken.

## Conclusie

In deze les hebben we geleerd:

- Wat data is  
- Hoe data wordt beschreven  
- Hoe data wordt geclassificeerd en gecategoriseerd  
- Waar data te vinden is  

## 🚀 Uitdaging

Kaggle is een uitstekende bron voor open datasets. Gebruik de [dataset zoektool](https://www.kaggle.com/datasets) om enkele interessante datasets te vinden en classificeer 3-5 datasets volgens deze criteria:

- Is de data kwantitatief of kwalitatief?  
- Is de data gestructureerd, ongestructureerd of semi-gestructureerd?  

## [Post-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/5)

## Review & Zelfstudie

- Deze Microsoft Learn-eenheid, getiteld [Classificeer je Data](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data), biedt een gedetailleerd overzicht van gestructureerde, semi-gestructureerde en ongestructureerde data.

## Opdracht

[Datasets Classificeren](assignment.md)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, willen we u erop wijzen dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.