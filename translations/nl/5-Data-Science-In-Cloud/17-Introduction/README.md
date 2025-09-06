<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-09-05T22:54:01+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "nl"
}
-->
# Introductie tot Data Science in de Cloud

|![ Sketchnote door [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Data Science In The Cloud: Introductie - _Sketchnote door [@nitya](https://twitter.com/nitya)_ |


In deze les leer je de fundamentele principes van de Cloud kennen, ontdek je waarom het interessant kan zijn om Cloud-diensten te gebruiken voor je data science-projecten, en bekijken we enkele voorbeelden van data science-projecten die in de Cloud worden uitgevoerd. 

## [Pre-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## Wat is de Cloud?

De Cloud, of Cloud Computing, is het leveren van een breed scala aan pay-as-you-go computerdiensten die worden gehost op een infrastructuur via het internet. Diensten omvatten oplossingen zoals opslag, databases, netwerken, software, analytics en intelligente diensten. 

We onderscheiden meestal de Publieke, Private en Hybride clouds als volgt: 

* Publieke cloud: een publieke cloud is eigendom van en wordt beheerd door een externe cloudserviceprovider die zijn computermiddelen via het internet aan het publiek levert. 
* Private cloud: verwijst naar cloud computing-middelen die exclusief worden gebruikt door een enkel bedrijf of organisatie, met diensten en een infrastructuur die worden onderhouden op een privé-netwerk. 
* Hybride cloud: de hybride cloud is een systeem dat publieke en private clouds combineert. Gebruikers kiezen voor een datacenter op locatie, terwijl ze gegevens en applicaties laten draaien op een of meer publieke clouds. 

De meeste cloud computing-diensten vallen in drie categorieën: Infrastructure as a Service (IaaS), Platform as a Service (PaaS) en Software as a Service (SaaS).

* Infrastructure as a Service (IaaS): gebruikers huren een IT-infrastructuur zoals servers en virtuele machines (VMs), opslag, netwerken, besturingssystemen. 
* Platform as a Service (PaaS): gebruikers huren een omgeving voor het ontwikkelen, testen, leveren en beheren van softwareapplicaties. Gebruikers hoeven zich geen zorgen te maken over het opzetten of beheren van de onderliggende infrastructuur van servers, opslag, netwerken en databases die nodig zijn voor ontwikkeling. 
* Software as a Service (SaaS): gebruikers krijgen toegang tot softwareapplicaties via het internet, op aanvraag en meestal op abonnementsbasis. Gebruikers hoeven zich geen zorgen te maken over het hosten en beheren van de softwareapplicatie, de onderliggende infrastructuur of het onderhoud, zoals software-upgrades en beveiligingspatches. 

Enkele van de grootste Cloud-providers zijn Amazon Web Services, Google Cloud Platform en Microsoft Azure.

## Waarom kiezen voor de Cloud voor Data Science?

Ontwikkelaars en IT-professionals kiezen om met de Cloud te werken om verschillende redenen, waaronder:

* Innovatie: je kunt je applicaties versterken door innovatieve diensten die door Cloud-providers zijn gecreëerd direct in je apps te integreren.
* Flexibiliteit: je betaalt alleen voor de diensten die je nodig hebt en kunt kiezen uit een breed scala aan diensten. Je betaalt meestal naar gebruik en past je diensten aan op basis van je veranderende behoeften. 
* Budget: je hoeft geen initiële investeringen te doen om hardware en software aan te schaffen, datacenters op locatie op te zetten en te beheren; je betaalt alleen voor wat je gebruikt. 
* Schaalbaarheid: je middelen kunnen worden aangepast aan de behoeften van je project, wat betekent dat je apps meer of minder rekenkracht, opslag en bandbreedte kunnen gebruiken, afhankelijk van externe factoren op elk moment. 
* Productiviteit: je kunt je richten op je bedrijf in plaats van tijd te besteden aan taken die door iemand anders kunnen worden beheerd, zoals het beheren van datacenters. 
* Betrouwbaarheid: Cloud Computing biedt verschillende manieren om je gegevens continu te back-uppen en je kunt rampenherstelplannen opstellen om je bedrijf en diensten draaiende te houden, zelfs in crisistijden.
* Beveiliging: je kunt profiteren van beleidsregels, technologieën en controles die de beveiliging van je project versterken. 

Dit zijn enkele van de meest voorkomende redenen waarom mensen ervoor kiezen om Cloud-diensten te gebruiken. Nu we een beter begrip hebben van wat de Cloud is en wat de belangrijkste voordelen zijn, laten we specifieker kijken naar de taken van datawetenschappers en ontwikkelaars die met data werken, en hoe de Cloud hen kan helpen met verschillende uitdagingen waarmee ze te maken kunnen krijgen:

* Opslaan van grote hoeveelheden data: in plaats van grote servers te kopen, beheren en beschermen, kun je je data direct in de Cloud opslaan, met oplossingen zoals Azure Cosmos DB, Azure SQL Database en Azure Data Lake Storage.
* Uitvoeren van data-integratie: data-integratie is een essentieel onderdeel van Data Science, waarmee je de overgang maakt van dataverzameling naar actie ondernemen. Met data-integratiediensten die in de Cloud worden aangeboden, kun je data verzamelen, transformeren en integreren vanuit verschillende bronnen in een enkel datawarehouse, met Data Factory.
* Verwerken van data: het verwerken van enorme hoeveelheden data vereist veel rekenkracht, en niet iedereen heeft toegang tot krachtige machines, wat de reden is dat veel mensen ervoor kiezen om direct gebruik te maken van de enorme rekenkracht van de Cloud om hun oplossingen uit te voeren en te implementeren.
* Gebruik maken van data-analyse diensten: Cloud-diensten zoals Azure Synapse Analytics, Azure Stream Analytics en Azure Databricks helpen je om je data om te zetten in bruikbare inzichten.
* Gebruik maken van Machine Learning en data-intelligentie diensten: in plaats van vanaf nul te beginnen, kun je gebruik maken van machine learning-algoritmen die door de Cloud-provider worden aangeboden, met diensten zoals AzureML. Je kunt ook cognitieve diensten gebruiken zoals spraak-naar-tekst, tekst-naar-spraak, computervisie en meer.

## Voorbeelden van Data Science in de Cloud

Laten we dit concreter maken door een paar scenario's te bekijken.

### Real-time sentimentanalyse van sociale media
We beginnen met een scenario dat vaak wordt bestudeerd door mensen die beginnen met machine learning: sentimentanalyse van sociale media in real-time.

Stel dat je een nieuwssite beheert en je wilt live data gebruiken om te begrijpen welke content je lezers interessant zouden kunnen vinden. Om daar meer over te weten te komen, kun je een programma bouwen dat real-time sentimentanalyse uitvoert op data van Twitter-publicaties, over onderwerpen die relevant zijn voor je lezers.

De belangrijkste indicatoren waar je naar kijkt, zijn het volume van tweets over specifieke onderwerpen (hashtags) en sentiment, dat wordt vastgesteld met analysetools die sentimentanalyse uitvoeren rond de gespecificeerde onderwerpen.

De stappen die nodig zijn om dit project te maken, zijn als volgt:

* Maak een event hub voor streaming input, die data van Twitter verzamelt.
* Configureer en start een Twitter-clientapplicatie, die de Twitter Streaming APIs aanroept.
* Maak een Stream Analytics-taak.
* Specificeer de taakinput en query.
* Maak een output sink en specificeer de taakoutput.
* Start de taak.

Om het volledige proces te bekijken, raadpleeg de [documentatie](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Analyse van wetenschappelijke artikelen
Laten we een ander voorbeeld nemen van een project dat is gemaakt door [Dmitry Soshnikov](http://soshnikov.com), een van de auteurs van dit curriculum.

Dmitry heeft een tool gemaakt die COVID-artikelen analyseert. Door dit project te bekijken, zie je hoe je een tool kunt maken die kennis uit wetenschappelijke artikelen haalt, inzichten verkrijgt en onderzoekers helpt om efficiënt door grote collecties artikelen te navigeren.

Laten we de verschillende stappen bekijken die hiervoor zijn gebruikt:
* Informatie extraheren en voorbewerken met [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Gebruik maken van [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) om de verwerking te paralleliseren.
* Informatie opslaan en opvragen met [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Een interactieve dashboard maken voor data-exploratie en visualisatie met Power BI.

Om het volledige proces te bekijken, bezoek [Dmitry’s blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Zoals je kunt zien, kunnen we Cloud-diensten op veel manieren benutten om Data Science uit te voeren.

## Voetnoot

Bronnen:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Post-Lecture Quiz

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/33)

## Opdracht

[Marktonderzoek](assignment.md)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, willen we u erop wijzen dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.