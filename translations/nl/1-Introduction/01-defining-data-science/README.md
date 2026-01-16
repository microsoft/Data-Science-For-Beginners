<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43212cc1ac137b7bb1dcfb37ca06b0f4",
  "translation_date": "2025-10-25T18:58:03+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "nl"
}
-->
# Definitie van Data Science

| ![ Sketchnote door [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------: |
|              Definitie van Data Science - _Sketchnote door [@nitya](https://twitter.com/nitya)_        |

---

[![Video over de definitie van Data Science](../../../../translated_images/nl/video-def-ds.6623ee2392ef1abf6d7faf3fad10a4163642811749da75f44e35a5bb121de15c.png)](https://youtu.be/beZ7Mb_oz9I)

## [Quiz voorafgaand aan de les](https://ff-quizzes.netlify.app/en/ds/quiz/0)

## Wat is Data?
In ons dagelijks leven worden we voortdurend omringd door data. De tekst die je nu leest is data. De lijst met telefoonnummers van je vrienden in je smartphone is data, net als de huidige tijd die op je horloge wordt weergegeven. Als mensen werken we van nature met data, bijvoorbeeld door geld te tellen of brieven te schrijven aan onze vrienden.

Data werd echter veel belangrijker met de komst van computers. De primaire functie van computers is het uitvoeren van berekeningen, maar ze hebben data nodig om mee te werken. Daarom moeten we begrijpen hoe computers data opslaan en verwerken.

Met de opkomst van het internet is de rol van computers als apparaten voor gegevensverwerking toegenomen. Als je erover nadenkt, gebruiken we computers tegenwoordig steeds meer voor gegevensverwerking en communicatie, in plaats van voor daadwerkelijke berekeningen. Wanneer we een e-mail naar een vriend schrijven of informatie op internet zoeken, zijn we in feite bezig met het creëren, opslaan, verzenden en manipuleren van data.
> Kun je je de laatste keer herinneren dat je een computer hebt gebruikt om echt iets te berekenen?

## Wat is Data Science?

Volgens [Wikipedia](https://en.wikipedia.org/wiki/Data_science) wordt **Data Science** gedefinieerd als *een wetenschappelijk vakgebied dat wetenschappelijke methoden gebruikt om kennis en inzichten te extraheren uit gestructureerde en ongestructureerde data, en deze kennis en bruikbare inzichten uit data toe te passen in een breed scala aan toepassingsdomeinen*.

Deze definitie benadrukt de volgende belangrijke aspecten van data science:

* Het belangrijkste doel van data science is **kennis extraheren** uit data, met andere woorden - **begrijpen** van data, verborgen relaties vinden en een **model** bouwen.
* Data science maakt gebruik van **wetenschappelijke methoden**, zoals kansberekening en statistiek. Toen de term *data science* voor het eerst werd geïntroduceerd, beweerden sommigen dat data science gewoon een nieuwe, hippe naam was voor statistiek. Tegenwoordig is het duidelijk dat het vakgebied veel breder is.
* De verkregen kennis moet worden toegepast om **bruikbare inzichten** te produceren, dat wil zeggen praktische inzichten die je kunt toepassen in echte zakelijke situaties.
* We moeten kunnen werken met zowel **gestructureerde** als **ongestructureerde** data. We zullen later in de cursus terugkomen op de verschillende soorten data.
* **Toepassingsdomein** is een belangrijk concept, en datawetenschappers hebben vaak een zekere mate van expertise nodig in het probleemgebied, bijvoorbeeld: financiën, geneeskunde, marketing, enz.

> Een ander belangrijk aspect van Data Science is dat het bestudeert hoe data kan worden verzameld, opgeslagen en verwerkt met behulp van computers. Terwijl statistiek ons de wiskundige basis geeft, past data science wiskundige concepten toe om daadwerkelijk inzichten uit data te halen.

Een van de manieren (toegeschreven aan [Jim Gray](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) om naar data science te kijken, is door het te beschouwen als een aparte wetenschappelijke benadering:
* **Empirisch**, waarbij we ons voornamelijk baseren op observaties en resultaten van experimenten
* **Theoretisch**, waar nieuwe concepten voortkomen uit bestaande wetenschappelijke kennis
* **Computationeel**, waar we nieuwe principes ontdekken op basis van computationale experimenten
* **Data-gedreven**, gebaseerd op het ontdekken van relaties en patronen in de data  

## Andere Gerelateerde Vakgebieden

Omdat data overal aanwezig is, is data science zelf ook een breed vakgebied dat veel andere disciplines raakt.

<dl>
<dt>Databases</dt>
<dd>
Een cruciale overweging is <b>hoe data op te slaan</b>, oftewel hoe het te structureren op een manier die snelle verwerking mogelijk maakt. Er zijn verschillende soorten databases die gestructureerde en ongestructureerde data opslaan, die <a href="../../2-Working-With-Data/README.md">we in onze cursus zullen behandelen</a>.
</dd>
<dt>Big Data</dt>
<dd>
Vaak moeten we zeer grote hoeveelheden data met een relatief eenvoudige structuur opslaan en verwerken. Er zijn speciale benaderingen en tools om die data op een gedistribueerde manier op een computercluster op te slaan en efficiënt te verwerken.
</dd>
<dt>Machine Learning</dt>
<dd>
Een manier om data te begrijpen is door een <b>model te bouwen</b> dat een gewenst resultaat kan voorspellen. Het ontwikkelen van modellen op basis van data wordt <b>machine learning</b> genoemd. Je kunt onze <a href="https://aka.ms/ml-beginners">Machine Learning voor Beginners</a> Curriculum bekijken om er meer over te leren.
</dd>
<dt>Kunstmatige Intelligentie</dt>
<dd>
Een gebied binnen machine learning, bekend als kunstmatige intelligentie (AI), maakt ook gebruik van data en omvat het bouwen van complexe modellen die menselijke denkprocessen nabootsen. AI-methoden stellen ons vaak in staat om ongestructureerde data (bijv. natuurlijke taal) om te zetten in gestructureerde inzichten.
</dd>
<dt>Visualisatie</dt>
<dd>
Grote hoeveelheden data zijn onbegrijpelijk voor een mens, maar zodra we nuttige visualisaties maken met die data, kunnen we meer inzicht krijgen en conclusies trekken. Daarom is het belangrijk om veel manieren te kennen om informatie te visualiseren - iets dat we zullen behandelen in <a href="../../3-Data-Visualization/README.md">Sectie 3</a> van onze cursus. Gerelateerde vakgebieden zijn ook <b>Infographics</b> en <b>Mens-Computer Interactie</b> in het algemeen.
</dd>
</dl>

## Soorten Data

Zoals we al hebben vermeld, is data overal. We hoeven het alleen maar op de juiste manier vast te leggen! Het is handig om onderscheid te maken tussen **gestructureerde** en **ongestructureerde** data. De eerste wordt meestal weergegeven in een goed gestructureerde vorm, vaak als een tabel of meerdere tabellen, terwijl de laatste gewoon een verzameling bestanden is. Soms kunnen we ook spreken van **semi-gestructureerde** data, die een soort structuur hebben die sterk kan variëren.

| Gestructureerd                                                              | Semi-gestructureerd                                                                           | Ongestructureerd                       |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------- |
| Lijst van mensen met hun telefoonnummers                                    | Wikipedia-pagina's met links                                                                  | Tekst van Encyclopaedia Britannica     |
| Temperatuur in alle kamers van een gebouw op elke minuut van de afgelopen 20 jaar | Verzameling wetenschappelijke artikelen in JSON-formaat met auteurs, publicatiedatum en samenvatting | Bestandenshare met bedrijfsdocumenten  |
| Gegevens over leeftijd en geslacht van alle mensen die het gebouw binnenkomen | Internetpagina's                                                                               | Ruwe videobeelden van bewakingscamera  |

## Waar Data te Vinden

Er zijn veel mogelijke bronnen van data, en het is onmogelijk om ze allemaal op te sommen! Laten we echter enkele typische plekken noemen waar je data kunt vinden:

* **Gestructureerd**
  - **Internet of Things** (IoT), inclusief data van verschillende sensoren, zoals temperatuur- of druksensoren, levert veel nuttige data op. Bijvoorbeeld, als een kantoorgebouw is uitgerust met IoT-sensoren, kunnen we automatisch verwarming en verlichting regelen om kosten te minimaliseren.
  - **Enquêtes** die we gebruikers vragen in te vullen na een aankoop of na een bezoek aan een website.
  - **Analyse van gedrag** kan ons bijvoorbeeld helpen begrijpen hoe diep een gebruiker een site verkent en wat de typische reden is om de site te verlaten.
* **Ongestructureerd**
  - **Teksten** kunnen een rijke bron van inzichten zijn, zoals een algemene **sentimentscore**, of het extraheren van trefwoorden en semantische betekenis.
  - **Afbeeldingen** of **Video**. Een video van een bewakingscamera kan worden gebruikt om het verkeer op de weg in te schatten en mensen te informeren over mogelijke verkeersopstoppingen.
  - Webserver **Logs** kunnen worden gebruikt om te begrijpen welke pagina's van onze site het vaakst worden bezocht en hoe lang.
* Semi-gestructureerd
  - **Sociale netwerken** grafieken kunnen geweldige bronnen van data zijn over persoonlijkheden van gebruikers en potentiële effectiviteit in het verspreiden van informatie.
  - Wanneer we een verzameling foto's van een feestje hebben, kunnen we proberen **groepsdynamiek** data te extraheren door een grafiek te maken van mensen die foto's met elkaar maken.

Door verschillende mogelijke bronnen van data te kennen, kun je nadenken over verschillende scenario's waarin data science-technieken kunnen worden toegepast om de situatie beter te begrijpen en bedrijfsprocessen te verbeteren.

## Wat je kunt doen met Data

In Data Science richten we ons op de volgende stappen in de datareis:

<dl>
<dt>1) Data Verzamelen</dt>
<dd>
De eerste stap is het verzamelen van de data. Hoewel dit in veel gevallen een eenvoudig proces kan zijn, zoals data die naar een database komt vanuit een webapplicatie, moeten we soms speciale technieken gebruiken. Bijvoorbeeld, data van IoT-sensoren kan overweldigend zijn, en het is een goede praktijk om bufferend endpoints zoals IoT Hub te gebruiken om alle data te verzamelen voordat verdere verwerking plaatsvindt.
</dd>
<dt>2) Data Opslag</dt>
<dd>
Het opslaan van data kan een uitdaging zijn, vooral als we het hebben over big data. Bij het beslissen hoe data moet worden opgeslagen, is het verstandig om te anticiperen op de manier waarop je de data in de toekomst wilt opvragen. Er zijn verschillende manieren waarop data kan worden opgeslagen:
<ul>
<li>Een relationele database slaat een verzameling tabellen op en gebruikt een speciale taal genaamd SQL om deze te bevragen. Meestal worden tabellen georganiseerd in verschillende groepen, genaamd schema's. In veel gevallen moeten we de data converteren van de oorspronkelijke vorm om in het schema te passen.</li>
<li><a href="https://en.wikipedia.org/wiki/NoSQL">Een NoSQL</a> database, zoals <a href="https://azure.microsoft.com/services/cosmos-db/?WT.mc_id=academic-77958-bethanycheum">CosmosDB</a>, legt geen schema's op aan data en maakt het mogelijk om complexere data op te slaan, bijvoorbeeld hiërarchische JSON-documenten of grafieken. NoSQL-databases hebben echter niet de uitgebreide querymogelijkheden van SQL en kunnen geen referentiële integriteit afdwingen, dat wil zeggen regels over hoe de data is gestructureerd in tabellen en de relaties tussen tabellen.</li>
<li><a href="https://en.wikipedia.org/wiki/Data_lake">Data Lake</a> opslag wordt gebruikt voor grote verzamelingen data in ruwe, ongestructureerde vorm. Data lakes worden vaak gebruikt bij big data, waar alle data niet op één machine past en moet worden opgeslagen en verwerkt door een cluster van servers. <a href="https://en.wikipedia.org/wiki/Apache_Parquet">Parquet</a> is het dataformaat dat vaak wordt gebruikt in combinatie met big data.</li> 
</ul>
</dd>
<dt>3) Data Verwerking</dt>
<dd>
Dit is het meest spannende deel van de datareis, waarbij de data wordt omgezet van de oorspronkelijke vorm naar een vorm die kan worden gebruikt voor visualisatie/modeltraining. Bij het werken met ongestructureerde data zoals tekst of afbeeldingen, kunnen we enkele AI-technieken gebruiken om <b>kenmerken</b> uit de data te extraheren, waardoor deze wordt omgezet in een gestructureerde vorm.
</dd>
<dt>4) Visualisatie / Menselijke Inzichten</dt>
<dd>
Vaak, om de data te begrijpen, moeten we deze visualiseren. Door veel verschillende visualisatietechnieken in onze toolbox te hebben, kunnen we de juiste weergave vinden om een inzicht te krijgen. Vaak moet een datawetenschapper "spelen met data", deze meerdere keren visualiseren en zoeken naar relaties. Ook kunnen we statistische technieken gebruiken om een hypothese te testen of een correlatie tussen verschillende datastukken te bewijzen.
</dd>
<dt>5) Een voorspellend model trainen</dt>
<dd>
Omdat het uiteindelijke doel van data science is om beslissingen te kunnen nemen op basis van data, willen we misschien de technieken van <a href="http://github.com/microsoft/ml-for-beginners">Machine Learning</a> gebruiken om een voorspellend model te bouwen. We kunnen dit vervolgens gebruiken om voorspellingen te doen met nieuwe datasets met vergelijkbare structuren.
</dd>
</dl>

Natuurlijk, afhankelijk van de daadwerkelijke data, kunnen sommige stappen ontbreken (bijvoorbeeld wanneer we de data al in de database hebben, of wanneer we geen modeltraining nodig hebben), of kunnen sommige stappen meerdere keren worden herhaald (zoals dataverwerking).

## Digitalisering en Digitale Transformatie

In het afgelopen decennium zijn veel bedrijven gaan begrijpen hoe belangrijk data is bij het nemen van zakelijke beslissingen. Om data science-principes toe te passen bij het runnen van een bedrijf, moet je eerst wat data verzamelen, oftewel bedrijfsprocessen vertalen naar digitale vorm. Dit staat bekend als **digitalisering**. Het toepassen van data science-technieken op deze data om beslissingen te sturen kan leiden tot aanzienlijke productiviteitsverhogingen (of zelfs een bedrijfsomslag), wat **digitale transformatie** wordt genoemd.

Laten we een voorbeeld bekijken. Stel dat we een data science-cursus hebben (zoals deze) die we online aan studenten aanbieden, en we willen data science gebruiken om deze te verbeteren. Hoe kunnen we dat doen?

We kunnen beginnen met de vraag: "Wat kan worden gedigitaliseerd?" De eenvoudigste manier zou zijn om de tijd te meten die elke student nodig heeft om elke module te voltooien, en om de verworven kennis te meten door aan het einde van elke module een meerkeuzetest te geven. Door de gemiddelde tijd-om-te-voltooien over alle studenten te berekenen, kunnen we ontdekken welke modules de meeste moeilijkheden veroorzaken voor studenten en eraan werken om ze te vereenvoudigen.
> Je zou kunnen beargumenteren dat deze aanpak niet ideaal is, omdat modules verschillende lengtes kunnen hebben. Het is waarschijnlijk eerlijker om de tijd te delen door de lengte van de module (in aantal tekens) en die waarden te vergelijken.

Wanneer we beginnen met het analyseren van de resultaten van meerkeuzetests, kunnen we proberen te bepalen welke concepten studenten moeilijk begrijpen en die informatie gebruiken om de inhoud te verbeteren. Om dat te doen, moeten we tests zo ontwerpen dat elke vraag gekoppeld is aan een bepaald concept of kennisblok.

Als we het nog ingewikkelder willen maken, kunnen we de tijd die nodig is voor elke module plotten tegen de leeftijdscategorie van de studenten. We kunnen erachter komen dat het voor sommige leeftijdscategorieën onevenredig lang duurt om de module te voltooien, of dat studenten afhaken voordat ze deze hebben afgerond. Dit kan ons helpen leeftijdsaanbevelingen voor de module te geven en de ontevredenheid van mensen door verkeerde verwachtingen te minimaliseren.

## 🚀 Uitdaging

In deze uitdaging gaan we proberen concepten te vinden die relevant zijn voor het vakgebied Data Science door naar teksten te kijken. We nemen een Wikipedia-artikel over Data Science, downloaden en verwerken de tekst, en bouwen vervolgens een woordwolk zoals deze:

![Woordwolk voor Data Science](../../../../translated_images/nl/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.png)

Bezoek [`notebook.ipynb`](../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') om de code door te nemen. Je kunt de code ook uitvoeren en zien hoe het alle datatransformaties in real-time uitvoert.

> Als je niet weet hoe je code moet uitvoeren in een Jupyter Notebook, bekijk dan [dit artikel](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Quiz na de les](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Opdrachten

* **Taak 1**: Pas de bovenstaande code aan om gerelateerde concepten te vinden voor de vakgebieden **Big Data** en **Machine Learning**  
* **Taak 2**: [Denk na over Data Science-scenario's](assignment.md)

## Credits

Deze les is met ♥️ geschreven door [Dmitry Soshnikov](http://soshnikov.com)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.