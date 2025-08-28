<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d92f57eb110dc7f765c05cbf0f837c77",
  "translation_date": "2025-08-28T15:22:31+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "nl"
}
-->
# De levenscyclus van Data Science: Analyseren

|![ Sketchnote door [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Levenscyclus van Data Science: Analyseren - _Sketchnote door [@nitya](https://twitter.com/nitya)_ |

## Quiz voorafgaand aan de les

## [Quiz voorafgaand aan de les](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

Het analyseren in de levenscyclus van data bevestigt dat de data de gestelde vragen kan beantwoorden of een specifiek probleem kan oplossen. Deze stap richt zich ook op het bevestigen dat een model deze vragen en problemen correct aanpakt. Deze les richt zich op Exploratory Data Analysis (EDA), technieken om kenmerken en relaties binnen de data te definiëren en de data voor te bereiden op modellering.

We gebruiken een voorbeelddataset van [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) om te laten zien hoe dit kan worden toegepast met Python en de Pandas-bibliotheek. Deze dataset bevat een telling van enkele veelvoorkomende woorden in e-mails, waarbij de bronnen van deze e-mails anoniem zijn. Gebruik het [notebook](notebook.ipynb) in deze map om mee te volgen.

## Exploratory Data Analysis

De fase van het verzamelen in de levenscyclus is waar de data wordt verkregen, evenals de problemen en vragen die moeten worden beantwoord. Maar hoe weten we of de data kan bijdragen aan het eindresultaat? 
Herinner je dat een datawetenschapper de volgende vragen kan stellen bij het verkrijgen van data:
-   Heb ik genoeg data om dit probleem op te lossen?
-   Is de kwaliteit van de data acceptabel voor dit probleem?
-   Als ik aanvullende informatie ontdek via deze data, moeten we dan overwegen de doelen te wijzigen of opnieuw te definiëren?

Exploratory Data Analysis is het proces van het leren kennen van de data en kan worden gebruikt om deze vragen te beantwoorden, evenals om de uitdagingen van het werken met de dataset te identificeren. Laten we ons richten op enkele technieken die hiervoor worden gebruikt.

## Data profileren, beschrijvende statistieken en Pandas
Hoe beoordelen we of we genoeg data hebben om dit probleem op te lossen? Data profileren kan een samenvatting geven en algemene informatie over onze dataset verzamelen via technieken van beschrijvende statistieken. Data profileren helpt ons te begrijpen wat beschikbaar is, en beschrijvende statistieken helpen ons te begrijpen hoeveel er beschikbaar is.

In enkele van de vorige lessen hebben we Pandas gebruikt om beschrijvende statistieken te leveren met de [`describe()`-functie](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Deze functie geeft de telling, maximale en minimale waarden, gemiddelde, standaarddeviatie en kwantielen van de numerieke data. Het gebruik van beschrijvende statistieken zoals de `describe()`-functie kan je helpen te beoordelen hoeveel je hebt en of je meer nodig hebt.

## Steekproeven nemen en query's uitvoeren
Het volledig verkennen van een grote dataset kan erg tijdrovend zijn en is meestal een taak die aan een computer wordt overgelaten. Steekproeven nemen is echter een nuttig hulpmiddel om inzicht te krijgen in de data en stelt ons in staat beter te begrijpen wat er in de dataset zit en wat het vertegenwoordigt. Met een steekproef kun je waarschijnlijkheid en statistiek toepassen om tot algemene conclusies over je data te komen. Hoewel er geen vaste regel is over hoeveel data je moet bemonsteren, is het belangrijk op te merken dat hoe meer data je bemonstert, hoe nauwkeuriger je generalisaties over de data kunnen zijn.

Pandas heeft de [`sample()`-functie in zijn bibliotheek](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), waarmee je een argument kunt doorgeven van hoeveel willekeurige steekproeven je wilt ontvangen en gebruiken.

Algemene query's op de data kunnen je helpen enkele algemene vragen en theorieën te beantwoorden die je hebt. In tegenstelling tot steekproeven stellen query's je in staat controle te hebben en je te richten op specifieke delen van de data waar je vragen over hebt. De [`query()`-functie](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) in de Pandas-bibliotheek stelt je in staat kolommen te selecteren en eenvoudige antwoorden te krijgen over de data via de opgehaalde rijen.

## Verkennen met visualisaties
Je hoeft niet te wachten tot de data volledig is opgeschoond en geanalyseerd om visualisaties te maken. Sterker nog, het hebben van een visuele weergave tijdens het verkennen kan helpen patronen, relaties en problemen in de data te identificeren. Bovendien bieden visualisaties een communicatiemiddel met degenen die niet betrokken zijn bij het beheren van de data en kunnen ze een kans zijn om aanvullende vragen te delen en te verduidelijken die niet in de verzamelingsfase zijn behandeld. Raadpleeg de [sectie over visualisaties](../../../../../../../../../3-Data-Visualization) om meer te leren over enkele populaire manieren om visueel te verkennen.

## Verkennen om inconsistenties te identificeren
Alle onderwerpen in deze les kunnen helpen ontbrekende of inconsistente waarden te identificeren, maar Pandas biedt functies om enkele hiervan te controleren. [isna() of isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) kunnen controleren op ontbrekende waarden. Een belangrijk onderdeel van het onderzoeken van deze waarden in je data is om te onderzoeken waarom ze überhaupt op die manier zijn ontstaan. Dit kan je helpen beslissen welke [acties je moet ondernemen om ze op te lossen](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Quiz voorafgaand aan de les](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/27)

## Opdracht

[Verkennen voor antwoorden](assignment.md)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.