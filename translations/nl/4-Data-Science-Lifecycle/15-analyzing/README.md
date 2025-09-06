<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2baeafe1db4d58ee5b8ec85db9de728a",
  "translation_date": "2025-09-05T22:58:46+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "nl"
}
-->
# De Data Science Lifecycle: Analyseren

|![ Sketchnote door [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Data Science Lifecycle: Analyseren - _Sketchnote door [@nitya](https://twitter.com/nitya)_ |

## Pre-Lecture Quiz

## [Pre-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/28)

Het analyseren in de data lifecycle bevestigt dat de data de gestelde vragen kan beantwoorden of een specifiek probleem kan oplossen. Deze stap richt zich ook op het bevestigen dat een model deze vragen en problemen correct aanpakt. Deze les richt zich op Exploratory Data Analysis (EDA), technieken om kenmerken en relaties binnen de data te definiëren en de data voor te bereiden op modellering.

We gebruiken een voorbeelddataset van [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) om te laten zien hoe dit kan worden toegepast met Python en de Pandas-bibliotheek. Deze dataset bevat een telling van enkele veelvoorkomende woorden die in e-mails worden gevonden, waarbij de bronnen van deze e-mails anoniem zijn. Gebruik het [notebook](../../../../4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) in deze map om mee te volgen.

## Exploratory Data Analysis

De capture-fase van de lifecycle is waar de data wordt verzameld, evenals de problemen en vragen die moeten worden aangepakt. Maar hoe weten we of de data kan helpen het eindresultaat te ondersteunen? 
Herinner je dat een data scientist de volgende vragen kan stellen bij het verkrijgen van de data:
-   Heb ik genoeg data om dit probleem op te lossen?
-   Is de kwaliteit van de data acceptabel voor dit probleem?
-   Als ik aanvullende informatie ontdek via deze data, moeten we dan overwegen de doelen te wijzigen of opnieuw te definiëren?

Exploratory Data Analysis is het proces van het leren kennen van de data en kan worden gebruikt om deze vragen te beantwoorden, evenals het identificeren van de uitdagingen bij het werken met de dataset. Laten we ons richten op enkele technieken die worden gebruikt om dit te bereiken.

## Data Profiling, Beschrijvende Statistieken en Pandas
Hoe evalueren we of we genoeg data hebben om dit probleem op te lossen? Data profiling kan algemene informatie over onze dataset samenvatten en verzamelen via technieken van beschrijvende statistieken. Data profiling helpt ons te begrijpen wat beschikbaar is, en beschrijvende statistieken helpen ons te begrijpen hoeveel er beschikbaar is.

In enkele van de vorige lessen hebben we Pandas gebruikt om beschrijvende statistieken te leveren met de [`describe()` functie](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Deze functie geeft de telling, maximale en minimale waarden, gemiddelde, standaarddeviatie en kwantielen van de numerieke data. Het gebruik van beschrijvende statistieken zoals de `describe()` functie kan je helpen te beoordelen hoeveel je hebt en of je meer nodig hebt.

## Sampling en Querying
Het volledig verkennen van een grote dataset kan erg tijdrovend zijn en is meestal een taak die aan een computer wordt overgelaten. Sampling is echter een nuttig hulpmiddel om de data beter te begrijpen en geeft ons een beter inzicht in wat er in de dataset zit en wat het vertegenwoordigt. Met een sample kun je waarschijnlijkheid en statistiek toepassen om tot algemene conclusies over je data te komen. Hoewel er geen vaste regel is over hoeveel data je moet samplen, is het belangrijk op te merken dat hoe meer data je samplet, hoe preciezer je generalisatie over de data kan zijn. 

Pandas heeft de [`sample()` functie in zijn bibliotheek](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) waarmee je een argument kunt doorgeven over hoeveel willekeurige samples je wilt ontvangen en gebruiken.

Algemene querying van de data kan je helpen enkele algemene vragen en theorieën te beantwoorden die je hebt. In tegenstelling tot sampling, stellen queries je in staat controle te hebben en je te richten op specifieke delen van de data waar je vragen over hebt. De [`query()` functie](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) in de Pandas-bibliotheek stelt je in staat kolommen te selecteren en eenvoudige antwoorden over de data te ontvangen via de opgehaalde rijen.

## Verkennen met Visualisaties
Je hoeft niet te wachten tot de data volledig is opgeschoond en geanalyseerd om visualisaties te maken. Sterker nog, een visuele weergave tijdens het verkennen kan helpen patronen, relaties en problemen in de data te identificeren. Bovendien bieden visualisaties een manier om te communiceren met mensen die niet betrokken zijn bij het beheren van de data en kunnen ze een kans bieden om aanvullende vragen te delen en te verduidelijken die niet in de capture-fase zijn behandeld. Raadpleeg de [sectie over Visualisaties](../../../../../../../../../3-Data-Visualization) om meer te leren over enkele populaire manieren om visueel te verkennen.

## Verkennen om inconsistenties te identificeren
Alle onderwerpen in deze les kunnen helpen bij het identificeren van ontbrekende of inconsistente waarden, maar Pandas biedt functies om enkele hiervan te controleren. [isna() of isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) kan controleren op ontbrekende waarden. Een belangrijk aspect van het verkennen van deze waarden binnen je data is onderzoeken waarom ze überhaupt op die manier zijn terechtgekomen. Dit kan je helpen beslissen welke [acties je moet ondernemen om ze op te lossen](../../../../../../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Opdracht

[Verkennen voor antwoorden](assignment.md)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, willen we u erop wijzen dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.