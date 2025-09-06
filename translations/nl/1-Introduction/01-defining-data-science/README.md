<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a76ab694b1534fa57981311975660bfe",
  "translation_date": "2025-09-06T12:24:17+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "nl"
}
-->
## Soorten Data

Zoals we al hebben vermeld, is data overal. We hoeven het alleen op de juiste manier vast te leggen! Het is handig om onderscheid te maken tussen **gestructureerde** en **ongestructureerde** data. Gestructureerde data wordt meestal weergegeven in een goed georganiseerde vorm, vaak als een tabel of meerdere tabellen, terwijl ongestructureerde data gewoon een verzameling bestanden is. Soms spreken we ook over **semi-gestructureerde** data, die een bepaalde mate van structuur heeft die sterk kan variëren.

| Gestructureerd                                                              | Semi-gestructureerd                                                                           | Ongestructureerd                        |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------- |
| Lijst van mensen met hun telefoonnummers                                    | Wikipedia-pagina's met links                                                                  | Tekst van de Encyclopaedia Britannica   |
| Temperatuur in alle kamers van een gebouw, elke minuut gedurende de laatste 20 jaar | Verzameling wetenschappelijke artikelen in JSON-formaat met auteurs, publicatiedatum en samenvatting | Bestandsdeling met bedrijfsdocumenten   |
| Gegevens over leeftijd en geslacht van alle mensen die het gebouw binnenkomen | Internetpagina's                                                                               | Ruwe videobeelden van een bewakingscamera |

## Waar Data vandaan halen

Er zijn veel mogelijke bronnen van data, en het is onmogelijk om ze allemaal op te sommen! Laten we echter enkele typische plekken noemen waar je data kunt vinden:

* **Gestructureerd**
  - **Internet of Things** (IoT), inclusief data van verschillende sensoren, zoals temperatuur- of druksensoren, biedt veel nuttige data. Bijvoorbeeld, als een kantoorgebouw is uitgerust met IoT-sensoren, kunnen we automatisch verwarming en verlichting regelen om kosten te minimaliseren.
  - **Enquêtes** die we gebruikers vragen in te vullen na een aankoop of na het bezoeken van een website.
  - **Gedragsanalyse** kan ons bijvoorbeeld helpen te begrijpen hoe diep een gebruiker een site verkent en wat de typische reden is om de site te verlaten.
* **Ongestructureerd**
  - **Teksten** kunnen een rijke bron van inzichten zijn, zoals een algemene **sentimentscore**, of het extraheren van trefwoorden en semantische betekenis.
  - **Afbeeldingen** of **Video**. Een video van een bewakingscamera kan worden gebruikt om het verkeer op de weg te schatten en mensen te informeren over mogelijke verkeersopstoppingen.
  - Webserver **Logs** kunnen worden gebruikt om te begrijpen welke pagina's van onze site het vaakst worden bezocht en hoe lang.
* **Semi-gestructureerd**
  - **Sociale Netwerk**-grafieken kunnen geweldige bronnen van data zijn over gebruikerspersoonlijkheden en potentiële effectiviteit in het verspreiden van informatie.
  - Wanneer we een verzameling foto's van een feestje hebben, kunnen we proberen **Groepsdynamiek**-data te extraheren door een grafiek te bouwen van mensen die foto's met elkaar maken.

Door verschillende mogelijke bronnen van data te kennen, kun je nadenken over verschillende scenario's waarin data science-technieken kunnen worden toegepast om de situatie beter te begrijpen en bedrijfsprocessen te verbeteren.

## Wat je kunt doen met Data

In Data Science richten we ons op de volgende stappen in de datareis:

## Digitalisering en Digitale Transformatie

In het afgelopen decennium zijn veel bedrijven gaan begrijpen hoe belangrijk data is bij het nemen van zakelijke beslissingen. Om data science-principes toe te passen op het runnen van een bedrijf, moet je eerst wat data verzamelen, oftewel bedrijfsprocessen vertalen naar digitale vorm. Dit staat bekend als **digitalisering**. Het toepassen van data science-technieken op deze data om beslissingen te sturen kan leiden tot aanzienlijke productiviteitsverhogingen (of zelfs een bedrijfsomslag), wat **digitale transformatie** wordt genoemd.

Laten we een voorbeeld bekijken. Stel dat we een data science-cursus hebben (zoals deze) die we online aan studenten aanbieden, en we willen data science gebruiken om deze te verbeteren. Hoe kunnen we dat doen?

We kunnen beginnen met de vraag: "Wat kan worden gedigitaliseerd?" De eenvoudigste manier zou zijn om de tijd te meten die elke student nodig heeft om elk module af te ronden, en de verworven kennis te meten door een meerkeuzetest aan het einde van elke module te geven. Door de gemiddelde tijd-om-te-voltooien over alle studenten te berekenen, kunnen we ontdekken welke modules de meeste moeilijkheden veroorzaken voor studenten en werken aan het vereenvoudigen ervan.
Je zou kunnen stellen dat deze aanpak niet ideaal is, omdat modules verschillende lengtes kunnen hebben. Het is waarschijnlijk eerlijker om de tijd te verdelen door de lengte van de module (in aantal tekens) en die waarden met elkaar te vergelijken.
Wanneer we beginnen met het analyseren van de resultaten van meerkeuzetests, kunnen we proberen te bepalen welke concepten studenten moeilijk vinden om te begrijpen, en die informatie gebruiken om de inhoud te verbeteren. Om dat te doen, moeten we tests zo ontwerpen dat elke vraag gekoppeld is aan een bepaald concept of kennisblok.

Als we het nog ingewikkelder willen maken, kunnen we de tijd die nodig is voor elk module plotten tegen de leeftijdscategorie van de studenten. We kunnen ontdekken dat het voor sommige leeftijdscategorieën onevenredig lang duurt om de module te voltooien, of dat studenten afhaken voordat ze deze hebben afgerond. Dit kan ons helpen leeftijdsaanbevelingen voor de module te geven en de ontevredenheid van mensen door verkeerde verwachtingen te minimaliseren.

## 🚀 Uitdaging

In deze uitdaging gaan we proberen concepten te vinden die relevant zijn voor het vakgebied Data Science door naar teksten te kijken. We nemen een Wikipedia-artikel over Data Science, downloaden en verwerken de tekst, en bouwen vervolgens een woordwolk zoals deze:

![Woordwolk voor Data Science](../../../../translated_images/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.nl.png)

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
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen om nauwkeurigheid te waarborgen, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.