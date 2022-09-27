# Definitie van Data Science

| ![ Sketchnote door [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------: |
|              Defining Data Science - _Sketchnote by [@nitya](https://twitter.com/nitya)_               |

---

[![Defining Data Science Video](../images/video-def-ds.png)](https://youtu.be/beZ7Mb_oz9I)

## [Starttoets data science](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/0)

## Wat is Data?
In ons dagelijks leven zijn we voortdurend omringd door data. De tekst die je nu leest is data.  De lijst met telefoonnummers van je vrienden op je smartphone is data, evenals de huidige tijd die op je horloge wordt weergegeven. Als mens werken we van nature met data, denk aan het geld dat we moeten tellen of door berichten te schrijven aan onze vrienden.

Gegevens werden echter veel belangrijker met de introductie van computers.  De primaire rol van computers is om berekeningen uit te voeren, maar ze hebben gegevens nodig om mee te werken.  We moeten dus begrijpen hoe computers gegevens opslaan en verwerken.

Met de opkomst van het internet nam de rol van computers als gegevensverwerkingsapparatuur toe.  Als je erover nadenkt, gebruiken we computers nu steeds meer voor gegevensverwerking en communicatie, in plaats van echte berekeningen. Wanneer we een e-mail schrijven naar een vriend of zoeken naar informatie op internet, creëren, bewaren, verzenden en manipuleren we in wezen gegevens.
> Kan jij je herinneren wanneer jij voor het laatste echte berekeningen door een computer hebt laten uitvoeren?

## Wat is Data Science?

[Wikipedia](https://en.wikipedia.org/wiki/Data_science) definieert **Data Science** als *een interdisciplinair onderzoeksveld met betrekking tot wetenschappelijke methoden, processen en systemen om kennis en inzichten te onttrekken uit (zowel gestructureerde als ongestructureerde) data.* 

Deze definitie belicht de volgende belangrijke aspecten van data science:

* Het belangrijkste doel van data science is om **kennis** uit gegevens te destilleren, in andere woorden - om data **te begrijpen**, verborgen relaties te vinden en een **model** te bouwen.
* Data science maakt gebruik van **wetenschappelijke methoden**, zoals waarschijnlijkheid en statistiek.  Toen de term *data science* voor het eerst werd geïntroduceerd, beweerden sommige mensen zelfs dat data science slechts een nieuwe mooie naam voor statistiek was.  Tegenwoordig is duidelijk geworden dat het veld veel breder is.    
* Verkregen kennis moet worden toegepast om enkele **bruikbare inzichten** te produceren, d.w.z. praktische inzichten die je kunt toepassen op echte bedrijfssituaties.
* We moeten in staat zijn om te werken met zowel **gestructureerde** als **ongestructureerde** data.  We komen later in de cursus terug om verschillende soorten gegevens te bespreken.
* **Toepassingsdomein** is een belangrijk begrip, en datawetenschappers hebben vaak minstens een zekere mate van expertise nodig in het probleemdomein, bijvoorbeeld: financiën, geneeskunde, marketing, enz.

> Een ander belangrijk aspect van Data Science is dat het bestudeert hoe gegevens kunnen worden verzameld, opgeslagen en bediend met behulp van computers.  Terwijl statistiek ons wiskundige grondslagen geeft, past data science wiskundige concepten toe om daadwerkelijk inzichten uit gegevens te halen.


Een van de manieren (toegeschreven aan [Jim Gray](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) om naar de data science te kijken, is om het te beschouwen als een apart paradigma van de wetenschap:
* **Empirisch**, waarbij we vooral vertrouwen op waarnemingen en resultaten van experimenten
* **Theoretisch**, waar nieuwe concepten voortkomen uit bestaande wetenschappelijke kennis
* **Computational**, waar we nieuwe principes ontdekken op basis van enkele computationele experimenten
* **Data-Driven**, gebaseerd op het ontdekken van relaties en patronen in de data  

## Andere gerelateerde vakgebieden

Omdat data alomtegenwoordig is, is data science zelf ook een breed vakgebied, dat veel andere disciplines raakt.

<dl>
<dt>Databases</dt>
<dd>
Een kritische overweging is **hoe de gegevens op te slaan**, d.w.z. hoe deze te structureren op een manier die een snellere verwerking mogelijk maakt.  Er zijn verschillende soorten databases die gestructureerde en ongestructureerde gegevens opslaan, welke <a href ="../../../2-Working-With-Data/README.md">we in onze cursus zullen overwegen</a>.
</dd>
<dt>Big Data</dt>
<dd>
Vaak moeten we zeer grote hoeveelheden gegevens opslaan en verwerken met een relatief eenvoudige structuur.  Er zijn speciale benaderingen en hulpmiddelen om die gegevens op een gedistribueerde manier op een computercluster op te slaan en efficiënt te verwerken.
</dd>
<dt>Machine learning</dt>
<dd>
Een manier om gegevens te begrijpen is door **een model** te bouwen dat in staat zal zijn om een gewenste uitkomst te voorspellen.  Het ontwikkelen van modellen op basis van data wordt **machine learning** genoemd. Misschien wilt u een kijkje nemen op onze <a href = "https://aka.ms/ml-beginners">Machine Learning for Beginners</a> Curriculum om er meer over te weten te komen.
</dd>
<dt>kunstmatige intelligentie</dt>
<dd>
Een gebied van machine learning dat bekend staat als Artificial Intelligence (AI) is ook afhankelijk van gegevens en betreft het bouwen van modellen met een hoge complexiteit die menselijke denkprocessen nabootsen.  AI-methoden stellen ons vaak in staat om ongestructureerde data (bijvoorbeeld natuurlijke taal) om te zetten in gestructureerde inzichten. 
</dd>
<dt>visualisatie</dt>
<dd>
Enorme hoeveelheden gegevens zijn onbegrijpelijk voor een mens, maar zodra we nuttige visualisaties maken met behulp van die gegevens, kunnen we de gegevens beter begrijpen en enkele conclusies trekken. Het is dus belangrijk om veel manieren te kennen om informatie te visualiseren - iets dat we zullen behandelen in <a href="../../../3-Data-Visualization/README.md">Sectie 3</a> van onze cursus. Gerelateerde velden omvatten ook **Infographics** en **Mens-computerinteractie** in het algemeen. 
</dd>
</dl>

## Typen van Data

Zoals we al hebben vermeld, zijn gegevens overal te vinden.  We moeten het gewoon op de juiste manier vastleggen!  Het is handig om onderscheid te maken tussen **gestructureerde** en **ongestructureerde** data. De eerste wordt meestal weergegeven in een goed gestructureerde vorm, vaak als een tabel of een aantal tabellen, terwijl de laatste slechts een verzameling bestanden is.  Soms kunnen we het ook hebben over **semigestructureerde** gegevens, die een soort structuur hebben die sterk kan variëren.

| Gestructureerde                                                                         | Semi-gestructureerde                                                                                        | Ongestructureerde                          |
| --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| Lijst van mensen met hun telefoonnummer                                                 | Wikipedia pagina's met links                                                                                | Tekst van encyclopaedia Britannica         |
| Temperatuur in alle kamers van een gebouw op elke minuut gedurende de laatste 20 jaar   | Verzameling van wetenschappelijke artikelen in JSON-formaat met auteurs, publicatiegegevens en een abstract | Bestanden opslag met bedrijfsdocumenten    |
| Gegevens van leeftijd en geslacht van alle mensen die het gebouw betreden               | Internet pagina's                                                                                           | Onbewerkte videofeed van bewakingscamera's |

## Waar data vandaan te halen

Er zijn veel mogelijke gegevensbronnen en het zal onmogelijk zijn om ze allemaal op te sommen! Laten we echter enkele van de typische plaatsen noemen waar u gegevens kunt krijgen:

* **Gestructureerd**
  - **Internet of Things** (IoT), inclusief data van verschillende sensoren, zoals temperatuur- of druksensoren, leveren veel bruikbare data op.  Als een kantoorgebouw bijvoorbeeld is uitgerust met IoT-sensoren, kunnen we automatisch verwarming en verlichting regelen om de kosten te minimaliseren. 
  - **Enquêtes** die we gebruikers vragen in te vullen na een aankoop of na een bezoek aan een website.
  - **Analyse van gedrag** kan ons bijvoorbeeld helpen begrijpen hoe diep een gebruiker in een website gaat en wat de typische reden is om de site te verlaten.
* **Ongestructureerd **
  - **Teksten** kunnen een rijke bron van inzichten zijn, zoals een algemene **sentimentscore**, of het extraheren van trefwoorden en semantische betekenis.
  - **Afbeeldingen** of **Video**. Een video van een bewakingscamera kan worden gebruikt om het verkeer op de weg in te schatten en mensen te informeren over mogelijke files.
  - Webserver **Logs** kunnen worden gebruikt om te begrijpen welke pagina's van onze site het vaakst worden bezocht en voor hoe lang.
* Semi-gestructureerd
  - **Social Network** grafieken kunnen geweldige bronnen van gegevens zijn over gebruikerspersoonlijkheden en potentiële effectiviteit bij het verspreiden van informatie.
  - Wanneer we een heleboel foto's van een feest hebben, kunnen we proberen **Group Dynamics**-gegevens te extraheren door een grafiek te maken van mensen die met elkaar foto's maken.

Door verschillende mogelijke databronnen te kennen, kun je proberen na te denken over verschillende scenario's waarin data science technieken kunnen worden toegepast om de situatie beter te leren kennen en bedrijfsprocessen te verbeteren.

## Wat je met Data kunt doen

In Data Science richten we ons op de volgende stappen van data journey:

<dl>
<dt>1) Data-acquisitie</dt>
<dd>
De eerste stap is het verzamelen van de gegevens.  Hoewel het in veel gevallen een eenvoudig proces kan zijn, zoals gegevens die vanuit een webapplicatie naar een database komen, moeten we soms speciale technieken gebruiken. Gegevens van IoT-sensoren kunnen bijvoorbeeld overweldigend zijn en het is een goede gewoonte om bufferingseindpunten zoals IoT Hub te gebruiken om alle gegevens te verzamelen voordat ze verder worden verwerkt.
</dd>
<dt>2) Gegevensopslag</dt>
<dd>
Het opslaan van gegevens kan een uitdaging zijn, vooral als we het hebben over big data.  Wanneer u beslist hoe u gegevens wilt opslaan, is het logisch om te anticiperen op de manier waarop u de gegevens in de toekomst zou opvragen.  Er zijn verschillende manieren waarop gegevens kunnen worden opgeslagen:
<ul>
<li>Een relationele database slaat een verzameling tabellen op en gebruikt een speciale taal genaamd SQL om deze op te vragen.  Tabellen zijn meestal georganiseerd in verschillene groepen die schema's worden genoemd.  In veel gevallen moeten we de gegevens van de oorspronkelijke vorm converteren naar het schema.</li>
<li><a href="https://en.wikipedia.org/wiki/NoSQL">A NoSQL</a> database, zoals <a href="https://azure.microsoft.com/services/cosmos-db/?WT.mc_id=academic-77958-bethanycheum">CosmosDB</a>, dwingt geen schema's af op gegevens en maakt het opslaan van complexere gegevens mogelijk, bijvoorbeeld hiërarchische JSON-documenten of grafieken. NoSQL-databases hebben echter niet de uitgebreide querymogelijkheden van SQL en kunnen geen referentiële integriteit afdwingen, d.w.z. regels over hoe de gegevens in tabellen zijn gestructureerd en de relaties tussen tabellen regelen.</li>
<li><a href="https://en.wikipedia.org/wiki/Data_lake">Data Lake</a> opslag wordt gebruikt voor grote verzamelingen gegevens in ruwe, ongestructureerde vorm. Data lakes worden vaak gebruikt met big data, waarbij alle data niet op één machine past en moet worden opgeslagen en verwerkt door een cluster van servers. <a href="https://en.wikipedia.org/wiki/Apache_Parquet">Parquet</a> is het gegevensformaat dat vaak wordt gebruikt in combinatie met big data.</li> 
</ul>
</dd>
<dt>3) Gegevensverwerking</dt>
<dd>
Dit is het meest spannende deel van het gegevenstraject, waarbij de gegevens van de oorspronkelijke vorm worden omgezet in een vorm die kan worden gebruikt voor visualisatie / modeltraining.  Bij het omgaan met ongestructureerde gegevens zoals tekst of afbeeldingen, moeten we mogelijk enkele AI-technieken gebruiken om **functies** uit de gegevens te destilleren en deze zo naar gestructureerde vorm te converteren.
</dd>
<dt>4) Visualisatie / Menselijke inzichten</dt>
<dd>
Vaak moeten we, om de gegevens te begrijpen, deze visualiseren.  Met veel verschillende visualisatietechnieken in onze toolbox kunnen we de juiste weergave vinden om inzicht te krijgen.  Vaak moet een data scientist "spelen met data", deze vele malen visualiseren en op zoek gaan naar wat relaties.  Ook kunnen we statistische technieken gebruiken om een hypothese te testen of een correlatie tussen verschillende gegevens te bewijzen.   
</dd>
<dt>5) Het trainen van een voorspellend model</dt>
<dd>
Omdat het uiteindelijke doel van data science is om beslissingen te kunnen nemen op basis van data, willen we misschien de technieken van <a href="http://github.com/microsoft/ml-for-beginners">Machine Learning</a> gebruiken om een voorspellend model te bouwen.  We kunnen dit vervolgens gebruiken om voorspellingen te doen met behulp van nieuwe datasets met vergelijkbare structuren.
</dd>
</dl>

Natuurlijk, afhankelijk van de werkelijke gegevens, kunnen sommige stappen ontbreken (bijvoorbeeld wanneer we de gegevens al in de database hebben opgeslagen of wanneer we geen modeltraining nodig hebben), of sommige stappen kunnen meerdere keren worden herhaald (zoals gegevensverwerking).

## Digitalisering en digitale transformatie

In het afgelopen decennium begonnen veel bedrijven het belang van gegevens te begrijpen bij het nemen van zakelijke beslissingen.  Om data science-principes toe te passen op het opereren van een bedrijf, moet men eerst wat gegevens verzamelen, d.w.z. bedrijfsprocessen vertalen naar digitale vorm. Dit staat bekend als **digitalisering**.  Het toepassen van data science-technieken op deze gegevens om beslissingen te sturen, kan leiden tot aanzienlijke productiviteitsstijgingen (of zelfs zakelijke spil), **digitale transformatie** genoemd.

Laten we een voorbeeld nemen.  Stel dat we een data science-cursus hebben (zoals deze) die we online aan studenten geven, en we willen data science gebruiken om het te verbeteren.  Hoe kunnen we dat doen?

We kunnen beginnen met de vraag "Wat kan worden gedigitaliseerd?"  De eenvoudigste manier zou zijn om de tijd te meten die elke student nodig heeft om elke module te voltooien en om de verkregen kennis te meten door aan het einde van elke module een meerkeuzetest te geven.  Door het gemiddelde te nemen van de time-to-complete over alle studenten, kunnen we erachter komen welke modules de meeste problemen veroorzaken voor studenten en werken aan het vereenvoudigen ervan.

> Je zou kunnen stellen dat deze aanpak niet ideaal is, omdat modules van verschillende lengtes kunnen zijn.  Het is waarschijnlijk eerlijker om de tijd te delen door de lengte van de module (in aantal tekens) en in plaats daarvan die waarden te vergelijken.

Wanneer we beginnen met het analyseren van resultaten van meerkeuzetoetsen, kunnen we proberen te bepalen welke concepten studenten moeilijk kunnen begrijpen en die informatie gebruiken om de inhoud te verbeteren.  Om dat te doen, moeten we tests zo ontwerpen dat elke vraag is toegewezen aan een bepaald concept of een deel van de kennis.

Als we het nog ingewikkelder willen maken, kunnen we de tijd die voor elke module nodig is, uitzetten tegen de leeftijdscategorie van studenten.  We kunnen erachter komen dat het voor sommige leeftijdscategorieën ongepast lang duurt om de module te voltooien, of dat studenten afhaken voordat ze het voltooien.  Dit kan ons helpen leeftijdsaanbevelingen voor de module te geven en de ontevredenheid van mensen over verkeerde verwachtingen te minimaliseren.

## 🚀 Uitdaging

In deze challenge proberen we concepten te vinden die relevant zijn voor het vakgebied Data Science door te kijken naar teksten.  We nemen een Wikipedia-artikel over Data Science, downloaden en verwerken de tekst en bouwen vervolgens een woordwolk zoals deze:

![Word Cloud for Data Science](../images/ds_wordcloud.png)

Ga naar ['notebook.ipynb'](notebook.ipynb) om de code door te lezen.  Je kunt de code ook uitvoeren en zien hoe alle gegevenstransformaties in realtime worden uitgevoerd. 

> Als je niet weet hoe je code in een Jupyter Notebook moet uitvoeren, kijk dan eens naar [dit artikel](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Post-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/1)

## Opdrachten

* **Taak 1**: Wijzig de bovenstaande code om gerelateerde concepten te achterhalen voor de velden **Big Data** en **Machine Learning**
* **Taak 2**: [Denk na over Data Science-scenario's] (assignment.md)

## Credits

Deze les is geschreven met ♥️ door [Dmitry Soshnikov] (http://soshnikov.com)