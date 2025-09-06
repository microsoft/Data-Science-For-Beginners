<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1341f6da63d434f5ba31b08ea951b02c",
  "translation_date": "2025-09-05T23:07:27+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "nl"
}
-->
# Introductie tot Data-ethiek

|![ Sketchnote door [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Data Science Ethics - _Sketchnote door [@nitya](https://twitter.com/nitya)_ |

---

We zijn allemaal databurgers die leven in een gedataficeerde wereld.

Markttrends laten zien dat tegen 2022, 1 op de 3 grote organisaties hun data zal kopen en verkopen via online [marktplaatsen en beurzen](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/). Als **app-ontwikkelaars** wordt het voor ons gemakkelijker en goedkoper om datagestuurde inzichten en algoritmegestuurde automatisering te integreren in dagelijkse gebruikerservaringen. Maar naarmate AI alomtegenwoordig wordt, moeten we ook de potentiële schade begrijpen die wordt veroorzaakt door de [bewapening](https://www.youtube.com/watch?v=TQHs8SA1qpk) van dergelijke algoritmen op grote schaal.

Trends geven ook aan dat we tegen 2025 meer dan [180 zettabytes](https://www.statista.com/statistics/871513/worldwide-data-created/) aan data zullen creëren en consumeren. Als **datawetenschappers** geeft dit ons ongekende toegang tot persoonlijke gegevens. Dit betekent dat we gedragsprofielen van gebruikers kunnen opbouwen en besluitvorming kunnen beïnvloeden op manieren die een [illusie van vrije keuze](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) creëren, terwijl we gebruikers mogelijk naar door ons gewenste uitkomsten sturen. Dit roept ook bredere vragen op over gegevensprivacy en gebruikersbescherming.

Data-ethiek is nu een _noodzakelijke vangrail_ voor datawetenschap en -techniek, die ons helpt potentiële schade en onbedoelde gevolgen van onze datagestuurde acties te minimaliseren. De [Gartner Hype Cycle voor AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) identificeert relevante trends in digitale ethiek, verantwoordelijke AI en AI-governance als belangrijke drijfveren voor grotere megatrends rond _democratisering_ en _industrialisering_ van AI.

![Gartner's Hype Cycle voor AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

In deze les verkennen we het fascinerende gebied van data-ethiek - van kernconcepten en uitdagingen tot casestudy's en toegepaste AI-concepten zoals governance - die helpen een ethische cultuur te vestigen in teams en organisaties die met data en AI werken.

## [Quiz voorafgaand aan de les](https://ff-quizzes.netlify.app/en/ds/quiz/2) 🎯

## Basisdefinities

Laten we beginnen met het begrijpen van de basisbegrippen.

Het woord "ethiek" komt van het [Griekse woord "ethikos"](https://en.wikipedia.org/wiki/Ethics) (en de wortel "ethos") wat _karakter of morele aard_ betekent.

**Ethiek** gaat over de gedeelde waarden en morele principes die ons gedrag in de samenleving sturen. Ethiek is niet gebaseerd op wetten, maar op algemeen geaccepteerde normen van wat "goed versus fout" is. Echter, ethische overwegingen kunnen invloed hebben op initiatieven voor corporate governance en overheidsreguleringen die meer prikkels creëren voor naleving.

**Data-ethiek** is een [nieuwe tak van ethiek](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1) die "morele problemen bestudeert en evalueert met betrekking tot _data, algoritmen en bijbehorende praktijken_". Hier richt **"data"** zich op acties zoals het genereren, vastleggen, beheren, verwerken, verspreiden, delen en gebruiken van gegevens. **"Algoritmen"** richten zich op AI, agenten, machine learning en robots, en **"praktijken"** richten zich op onderwerpen zoals verantwoord innoveren, programmeren, hacken en ethische codes.

**Toegepaste ethiek** is de [praktische toepassing van morele overwegingen](https://en.wikipedia.org/wiki/Applied_ethics). Het is het proces van actief onderzoeken van ethische kwesties in de context van _real-world acties, producten en processen_, en het nemen van corrigerende maatregelen om ervoor te zorgen dat deze in lijn blijven met onze gedefinieerde ethische waarden.

**Ethische cultuur** gaat over het [_operationeel maken_ van toegepaste ethiek](https://hbr.org/2019/05/how-to-design-an-ethical-organization) om ervoor te zorgen dat onze ethische principes en praktijken op een consistente en schaalbare manier worden toegepast in de hele organisatie. Succesvolle ethische culturen definiëren organisatiebrede ethische principes, bieden zinvolle prikkels voor naleving en versterken ethische normen door gewenst gedrag op elk niveau van de organisatie aan te moedigen en te versterken.

## Ethiekconcepten

In deze sectie bespreken we concepten zoals **gedeelde waarden** (principes) en **ethische uitdagingen** (problemen) voor data-ethiek - en verkennen we **casestudy's** die je helpen deze concepten in real-world contexten te begrijpen.

### 1. Ethiekprincipes

Elke data-ethiekstrategie begint met het definiëren van _ethische principes_ - de "gedeelde waarden" die acceptabel gedrag beschrijven en compliant acties sturen in onze data- en AI-projecten. Je kunt deze definiëren op individueel of teamniveau. Echter, de meeste grote organisaties schetsen deze in een _ethische AI_-missieverklaring of kader dat op bedrijfsniveau wordt gedefinieerd en consequent wordt gehandhaafd in alle teams.

**Voorbeeld:** Microsoft's [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai)-missieverklaring luidt: _"We zijn toegewijd aan de vooruitgang van AI, gedreven door ethische principes die mensen centraal stellen"_ - met daarin 6 ethische principes zoals hieronder weergegeven:

![Responsible AI bij Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Laten we deze principes kort verkennen. _Transparantie_ en _verantwoordelijkheid_ zijn fundamentele waarden waarop andere principes zijn gebouwd - laten we daar beginnen:

* [**Verantwoordelijkheid**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) maakt beoefenaars _verantwoordelijk_ voor hun data- en AI-operaties, en naleving van deze ethische principes.
* [**Transparantie**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) zorgt ervoor dat data- en AI-acties _begrijpelijk_ (interpreteerbaar) zijn voor gebruikers, waarbij wordt uitgelegd wat en waarom beslissingen worden genomen.
* [**Eerlijkheid**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) richt zich op het waarborgen dat AI _alle mensen_ eerlijk behandelt, en systemische of impliciete sociaal-technische vooroordelen in data en systemen aanpakt.
* [**Betrouwbaarheid en veiligheid**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) zorgt ervoor dat AI zich _consistent_ gedraagt met gedefinieerde waarden, en potentiële schade of onbedoelde gevolgen minimaliseert.
* [**Privacy en beveiliging**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) draait om het begrijpen van de herkomst van data en het bieden van _gegevensprivacy en gerelateerde bescherming_ aan gebruikers.
* [**Inclusiviteit**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) gaat over het ontwerpen van AI-oplossingen met intentie, en deze aanpassen om te voldoen aan een _breed scala aan menselijke behoeften_ en mogelijkheden.

> 🚨 Denk na over wat jouw data-ethiek missieverklaring zou kunnen zijn. Verken ethische AI-kaders van andere organisaties - hier zijn voorbeelden van [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles), en [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Welke gedeelde waarden hebben ze gemeen? Hoe relateren deze principes aan het AI-product of de industrie waarin ze opereren?

### 2. Ethiekuitdagingen

Zodra we ethische principes hebben gedefinieerd, is de volgende stap om onze data- en AI-acties te evalueren om te zien of ze in lijn zijn met die gedeelde waarden. Denk aan je acties in twee categorieën: _dataverzameling_ en _algoritmeontwerp_.

Bij dataverzameling zullen acties waarschijnlijk betrekking hebben op **persoonlijke gegevens** of persoonlijk identificeerbare informatie (PII) van identificeerbare levende individuen. Dit omvat [diverse items van niet-persoonlijke gegevens](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en) die _gezamenlijk_ een individu identificeren. Ethische uitdagingen kunnen betrekking hebben op _gegevensprivacy_, _gegevensbezit_ en gerelateerde onderwerpen zoals _geïnformeerde toestemming_ en _intellectuele eigendomsrechten_ voor gebruikers.

Bij algoritmeontwerp zullen acties betrekking hebben op het verzamelen en beheren van **datasets**, en deze vervolgens gebruiken om **datamodellen** te trainen en in te zetten die uitkomsten voorspellen of beslissingen automatiseren in real-world contexten. Ethische uitdagingen kunnen voortkomen uit _datasetbias_, _gegevenskwaliteit_, _oneerlijkheid_ en _verkeerde voorstelling_ in algoritmen - inclusief enkele kwesties die systemisch van aard zijn.

In beide gevallen benadrukken ethische uitdagingen gebieden waar onze acties in conflict kunnen komen met onze gedeelde waarden. Om deze zorgen te detecteren, te beperken, te minimaliseren of te elimineren, moeten we morele "ja/nee"-vragen stellen met betrekking tot onze acties, en indien nodig corrigerende maatregelen nemen. Laten we enkele ethische uitdagingen en de morele vragen die ze oproepen bekijken:

#### 2.1 Gegevensbezit

Dataverzameling omvat vaak persoonlijke gegevens die de betrokkenen kunnen identificeren. [Gegevensbezit](https://permission.io/blog/data-ownership) gaat over _controle_ en [_gebruikersrechten_](https://permission.io/blog/data-ownership) met betrekking tot het creëren, verwerken en verspreiden van gegevens.

De morele vragen die we moeten stellen zijn:
 * Wie bezit de gegevens? (gebruiker of organisatie)
 * Welke rechten hebben betrokkenen? (bijv. toegang, verwijdering, overdraagbaarheid)
 * Welke rechten hebben organisaties? (bijv. corrigeren van schadelijke gebruikersrecensies)

#### 2.2 Geïnformeerde Toestemming

[Geïnformeerde toestemming](https://legaldictionary.net/informed-consent/) definieert de handeling waarbij gebruikers instemmen met een actie (zoals dataverzameling) met een _volledig begrip_ van relevante feiten, inclusief het doel, potentiële risico's en alternatieven.

Vragen om hier te onderzoeken zijn:
 * Heeft de gebruiker (betrokkene) toestemming gegeven voor gegevensverzameling en -gebruik?
 * Begrijpt de gebruiker het doel waarvoor die gegevens zijn verzameld?
 * Begrijpt de gebruiker de potentiële risico's van hun deelname?

#### 2.3 Intellectuele Eigendom

[Intellectuele eigendom](https://en.wikipedia.org/wiki/Intellectual_property) verwijst naar immateriële creaties die voortkomen uit menselijke initiatieven en _economische waarde_ kunnen hebben voor individuen of bedrijven.

Vragen om hier te onderzoeken zijn:
 * Hadden de verzamelde gegevens economische waarde voor een gebruiker of bedrijf?
 * Heeft de **gebruiker** hier intellectuele eigendom?
 * Heeft de **organisatie** hier intellectuele eigendom?
 * Als deze rechten bestaan, hoe beschermen we ze?

#### 2.4 Gegevensprivacy

[Gegevensprivacy](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) of informatieprivacy verwijst naar het behoud van gebruikersprivacy en de bescherming van gebruikersidentiteit met betrekking tot persoonlijk identificeerbare informatie.

Vragen om hier te onderzoeken zijn:
 * Zijn de (persoonlijke) gegevens van gebruikers beveiligd tegen hacks en lekken?
 * Zijn de gegevens van gebruikers alleen toegankelijk voor geautoriseerde gebruikers en contexten?
 * Wordt de anonimiteit van gebruikers behouden wanneer gegevens worden gedeeld of verspreid?
 * Kan een gebruiker worden geanonimiseerd uit geanonimiseerde datasets?

#### 2.5 Recht Om Vergeten Te Worden

Het [Recht Om Vergeten Te Worden](https://en.wikipedia.org/wiki/Right_to_be_forgotten) of [Recht op Verwijdering](https://www.gdpreu.org/right-to-be-forgotten/) biedt extra bescherming van persoonlijke gegevens aan gebruikers. Het geeft gebruikers specifiek het recht om verwijdering of verwijdering van persoonlijke gegevens van internetzoekopdrachten en andere locaties te verzoeken, _onder specifieke omstandigheden_ - zodat ze een nieuwe start online kunnen maken zonder dat eerdere acties tegen hen worden gebruikt.

Vragen om hier te onderzoeken zijn:
 * Staat het systeem betrokkenen toe om verwijdering te verzoeken?
 * Moet het intrekken van gebruikersinstemming automatische verwijdering activeren?
 * Zijn gegevens verzameld zonder toestemming of op onwettige wijze?
 * Zijn we compliant met overheidsregels voor gegevensprivacy?

#### 2.6 Datasetbias

Dataset- of [verzamelbias](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) gaat over het selecteren van een _niet-representatieve_ subset van gegevens voor algoritmeontwikkeling, wat mogelijk oneerlijkheid in uitkomsten voor diverse groepen creëert. Soorten bias omvatten selectie- of steekproefbias, vrijwilligersbias en instrumentbias.

Vragen om hier te onderzoeken zijn:
 * Hebben we een representatieve set van betrokkenen gerekruteerd?
 * Hebben we onze verzamelde of samengestelde dataset getest op verschillende vormen van bias?
 * Kunnen we ontdekte bias beperken of verwijderen?

#### 2.7 Gegevenskwaliteit

[Gegevenskwaliteit](https://lakefs.io/data-quality-testing/) kijkt naar de geldigheid van de samengestelde dataset die wordt gebruikt voor de ontwikkeling van onze algoritmen, en controleert of kenmerken en records voldoen aan de vereisten voor het niveau van nauwkeurigheid en consistentie dat nodig is voor ons AI-doel.

Vragen om hier te onderzoeken zijn:
 * Hebben we geldige _kenmerken_ vastgelegd voor ons gebruiksscenario?
 * Zijn gegevens _consistent_ vastgelegd over diverse gegevensbronnen heen?
 * Is de dataset _compleet_ voor diverse omstandigheden of scenario's?
 * Is informatie _nauwkeurig_ vastgelegd in het weerspiegelen van de werkelijkheid?

#### 2.8 Algoritmische Eerlijkheid
[Algorithmische Eerlijkheid](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) onderzoekt of het ontwerp van een algoritme systematisch discrimineert tegen specifieke subgroepen van gegevenssubjecten, wat kan leiden tot [mogelijke schade](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) in _toewijzing_ (waar middelen worden geweigerd of onthouden aan die groep) en _kwaliteit van dienstverlening_ (waar AI minder accuraat is voor sommige subgroepen dan voor anderen).

Vragen om hier te onderzoeken zijn:
 * Hebben we de modelnauwkeurigheid geëvalueerd voor diverse subgroepen en omstandigheden?
 * Hebben we het systeem onderzocht op mogelijke schade (bijv. stereotypering)?
 * Kunnen we gegevens herzien of modellen opnieuw trainen om geïdentificeerde schade te beperken?

Verken bronnen zoals [AI Fairness checklists](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) om meer te leren.

#### 2.9 Misrepresentatie

[Gegevensmisrepresentatie](https://www.sciencedirect.com/topics/computer-science/misrepresentation) gaat over de vraag of we inzichten uit eerlijk gerapporteerde gegevens op een misleidende manier communiceren om een gewenst narratief te ondersteunen.

Vragen om hier te onderzoeken zijn:
 * Rapporteren we onvolledige of onnauwkeurige gegevens?
 * Visualiseren we gegevens op een manier die tot misleidende conclusies leidt?
 * Gebruiken we selectieve statistische technieken om uitkomsten te manipuleren?
 * Zijn er alternatieve verklaringen die tot een andere conclusie kunnen leiden?

#### 2.10 Vrije Keuze
De [Illusie van Vrije Keuze](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) ontstaat wanneer "keuzearchitecturen" in systemen besluitvormingsalgoritmen gebruiken om mensen subtiel te sturen naar een gewenste uitkomst, terwijl het lijkt alsof ze opties en controle hebben. Deze [dark patterns](https://www.darkpatterns.org/) kunnen sociale en economische schade veroorzaken voor gebruikers. Omdat gebruikersbeslissingen gedragsprofielen beïnvloeden, kunnen deze acties toekomstige keuzes sturen en de impact van deze schade versterken of verlengen.

Vragen om hier te onderzoeken zijn:
 * Begrijpt de gebruiker de implicaties van het maken van die keuze?
 * Was de gebruiker zich bewust van (alternatieve) keuzes en de voor- en nadelen van elke optie?
 * Kan de gebruiker een geautomatiseerde of beïnvloede keuze later terugdraaien?

### 3. Casestudies

Om deze ethische uitdagingen in een real-world context te plaatsen, is het nuttig om casestudies te bekijken die de mogelijke schade en gevolgen voor individuen en de samenleving benadrukken wanneer dergelijke ethische schendingen over het hoofd worden gezien.

Hier zijn enkele voorbeelden:

| Ethische Uitdaging | Casestudy  | 
|--- |--- |
| **Informed Consent** | 1972 - [Tuskegee Syfilis Studie](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Afro-Amerikaanse mannen die deelnamen aan de studie kregen gratis medische zorg beloofd, _maar werden misleid_ door onderzoekers die hen niet informeerden over hun diagnose of de beschikbaarheid van behandeling. Veel deelnemers stierven en partners of kinderen werden getroffen; de studie duurde 40 jaar. | 
| **Gegevensprivacy** |  2007 - De [Netflix data prijs](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) gaf onderzoekers _10 miljoen geanonimiseerde filmbeoordelingen van 50.000 klanten_ om aanbevelingsalgoritmen te verbeteren. Onderzoekers konden echter geanonimiseerde gegevens correleren met persoonlijk identificeerbare gegevens in _externe datasets_ (bijv. IMDb-reacties), waardoor sommige Netflix-abonnees effectief werden "gedeanonimiseerd".|
| **Verzamelingsbias**  | 2013 - De stad Boston [ontwikkelde Street Bump](https://www.boston.gov/transportation/street-bump), een app waarmee burgers kuilen konden melden, zodat de stad betere gegevens kreeg om problemen op wegen te vinden en op te lossen. Echter, [mensen in lagere inkomensgroepen hadden minder toegang tot auto's en telefoons](https://hbr.org/2013/04/the-hidden-biases-in-big-data), waardoor hun wegproblemen onzichtbaar bleven in deze app. Ontwikkelaars werkten samen met academici om _eerlijke toegang en digitale ongelijkheden_ aan te pakken. |
| **Algorithmische Eerlijkheid**  | 2018 - De MIT [Gender Shades Studie](http://gendershades.org/overview.html) evalueerde de nauwkeurigheid van AI-producten voor geslachtsclassificatie en onthulde hiaten in nauwkeurigheid voor vrouwen en mensen van kleur. Een [2019 Apple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) leek minder krediet te bieden aan vrouwen dan aan mannen. Beide illustreerden problemen met algoritmische bias die tot sociaal-economische schade leidden.|
| **Gegevensmisrepresentatie** | 2020 - Het [Georgia Department of Public Health bracht COVID-19-grafieken uit](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) die burgers leken te misleiden over trends in bevestigde gevallen door niet-chronologische ordening op de x-as. Dit illustreert misrepresentatie door visualisatietrucs. |
| **Illusie van vrije keuze** | 2020 - Leerapp [ABCmouse betaalde $10M om een FTC-klacht te schikken](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) waarbij ouders vastzaten aan abonnementen die ze niet konden annuleren. Dit illustreert dark patterns in keuzearchitecturen, waarbij gebruikers subtiel werden gestuurd naar potentieel schadelijke keuzes. |
| **Gegevensprivacy & Gebruikersrechten** | 2021 - Facebook [Data Lek](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) lekte gegevens van 530 miljoen gebruikers, wat resulteerde in een schikking van $5 miljard met de FTC. Het weigerde echter gebruikers op de hoogte te stellen van het lek, wat in strijd was met gebruikersrechten rond gegevenstransparantie en toegang. |

Wil je meer casestudies verkennen? Bekijk deze bronnen:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - ethische dilemma's in diverse industrieën. 
* [Data Science Ethics course](https://www.coursera.org/learn/data-science-ethics#syllabus) - landmark casestudies onderzocht.
* [Waar het misging](https://deon.drivendata.org/examples/) - deon checklist met voorbeelden.


> 🚨 Denk na over de casestudies die je hebt gezien - heb je een vergelijkbare ethische uitdaging in je leven ervaren of ondervonden? Kun je minstens één andere casestudy bedenken die een van de ethische uitdagingen illustreert die we in deze sectie hebben besproken?

## Toegepaste Ethiek

We hebben het gehad over ethische concepten, uitdagingen en casestudies in real-world contexten. Maar hoe beginnen we met het _toepassen_ van ethische principes en praktijken in onze projecten? En hoe _operationeel_ maken we deze praktijken voor betere governance? Laten we enkele real-world oplossingen verkennen:

### 1. Professionele Codes

Professionele codes bieden een optie voor organisaties om leden te "stimuleren" om hun ethische principes en missieverklaring te ondersteunen. Codes zijn _morele richtlijnen_ voor professioneel gedrag, die werknemers of leden helpen beslissingen te nemen die in lijn zijn met de principes van hun organisatie. Ze zijn alleen zo effectief als de vrijwillige naleving door leden; veel organisaties bieden echter extra beloningen en sancties om naleving te motiveren.

Voorbeelden zijn:

 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Code of Ethics
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Code of Conduct (gecreëerd in 2013)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (sinds 1993)

> 🚨 Behoor je tot een professionele ingenieurs- of datawetenschapsorganisatie? Verken hun site om te zien of ze een professionele gedragscode definiëren. Wat zegt dit over hun ethische principes? Hoe "stimuleren" ze leden om de code te volgen?

### 2. Ethiek Checklists

Hoewel professionele codes vereist _ethisch gedrag_ van beoefenaars definiëren, hebben ze [bekende beperkingen](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) in handhaving, vooral in grootschalige projecten. In plaats daarvan pleiten veel datawetenschapsexperts voor [checklists](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), die **principes verbinden met praktijken** op meer deterministische en actiegerichte manieren.

Checklists zetten vragen om in "ja/nee"-taken die operationeel kunnen worden gemaakt, zodat ze kunnen worden gevolgd als onderdeel van standaard productrelease-workflows.

Voorbeelden zijn:
 * [Deon](https://deon.drivendata.org/) - een algemene data-ethiek checklist, gemaakt op basis van [industrieaanbevelingen](https://deon.drivendata.org/#checklist-citations) met een command-line tool voor eenvoudige integratie.
 * [Privacy Audit Checklist](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - biedt algemene richtlijnen voor informatieverwerkingspraktijken vanuit juridische en sociale blootstellingsperspectieven.
 * [AI Fairness Checklist](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - gemaakt door AI-practitioners om de adoptie en integratie van eerlijkheidscontroles in AI-ontwikkelingscycli te ondersteunen.
 * [22 vragen voor ethiek in data en AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - een meer open kader, gestructureerd voor initiële verkenning van ethische kwesties in ontwerp, implementatie en organisatorische contexten.

### 3. Ethiek Regelgeving

Ethiek gaat over het definiëren van gedeelde waarden en vrijwillig het juiste doen. **Naleving** gaat over _het volgen van de wet_ waar en wanneer die is gedefinieerd. **Governance** omvat alle manieren waarop organisaties opereren om ethische principes af te dwingen en te voldoen aan vastgestelde wetten.

Tegenwoordig neemt governance twee vormen aan binnen organisaties. Ten eerste gaat het om het definiëren van **ethische AI**-principes en het vaststellen van praktijken om adoptie te operationaliseren in alle AI-gerelateerde projecten binnen de organisatie. Ten tweede gaat het om naleving van alle door de overheid opgelegde **gegevensbeschermingsregelgeving** voor de regio's waarin het opereert.

Voorbeelden van gegevensbeschermings- en privacyregelgeving:

 * `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - reguleert _federale overheid_ verzameling, gebruik en openbaarmaking van persoonlijke informatie.
 * `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - beschermt persoonlijke gezondheidsgegevens.
 * `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - beschermt gegevensprivacy van kinderen onder de 13.
 * `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - biedt gebruikersrechten, gegevensbescherming en privacy.
 * `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) geeft consumenten meer _rechten_ over hun (persoonlijke) gegevens.
 * `2021`, China's [Personal Information Protection Law](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) net aangenomen, een van de sterkste online gegevensprivacyregelgevingen wereldwijd.

> 🚨 De Europese Unie definieerde GDPR (General Data Protection Regulation) blijft een van de meest invloedrijke gegevensprivacyregelgevingen vandaag. Wist je dat het ook [8 gebruikersrechten](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) definieert om de digitale privacy en persoonlijke gegevens van burgers te beschermen? Leer wat deze rechten zijn en waarom ze belangrijk zijn.

### 4. Ethiek Cultuur

Let op dat er een ongrijpbare kloof blijft tussen _naleving_ (genoeg doen om "de letter van de wet" te volgen) en het aanpakken van [systemische problemen](https://www.coursera.org/learn/data-science-ethics/home/week/4) (zoals verstarring, informatie-asymmetrie en verdelingsonrechtvaardigheid) die de wapenisering van AI kunnen versnellen.

Dit laatste vereist [samenwerkingsbenaderingen om ethische culturen te definiëren](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f) die emotionele verbindingen en consistente gedeelde waarden _binnen organisaties_ in de industrie opbouwen. Dit vraagt om meer [geformaliseerde data-ethiek culturen](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) in organisaties - waardoor _iedereen_ [de Andon-kabel kan trekken](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (om ethische zorgen vroeg in het proces aan te kaarten) en _ethische beoordelingen_ (bijv. bij werving) een kerncriterium te maken voor teamvorming in AI-projecten.

---
## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/3) 🎯
## Review & Zelfstudie 

Cursussen en boeken helpen bij het begrijpen van kernconcepten en uitdagingen op het gebied van ethiek, terwijl casestudies en tools helpen bij toegepaste ethische praktijken in real-world contexten. Hier zijn enkele bronnen om mee te beginnen:

* [Machine Learning For Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - les over eerlijkheid, van Microsoft.
* [Principes van Verantwoorde AI](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - gratis leerpad van Microsoft Learn.  
* [Ethiek en Datawetenschap](https://resources.oreilly.com/examples/0636920203964) - O'Reilly EBook (M. Loukides, H. Mason et. al)  
* [Datawetenschap en Ethiek](https://www.coursera.org/learn/data-science-ethics#syllabus) - online cursus van de Universiteit van Michigan.  
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - casestudies van de Universiteit van Texas.  

# Opdracht  

[Schrijf Een Casestudy Over Data-Ethiek](assignment.md)  

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, willen we u erop wijzen dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.