# Inleiding tot gegevensethiek

|![ Sketchnote door [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/02-Ethics.png)|
|:---:|
| Ethiek van gegevenswetenschap - _Sketchnote door [@nitya](https://twitter.com/nitya)_ |

---

We zijn allemaal databurgers die in een datafied wereld leven.

Markttrends vertellen ons dat tegen 2022 1-op-3 grote organisaties hun data zullen kopen en verkopen via online [Marketplaces and Exchanges](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020). Als **App-ontwikkelaars** zullen we het gemakkelijker en goedkoper vinden om gegevensgestuurde inzichten en algoritmegestuurde automatisering te integreren in dagelijkse gebruikerservaringen. Maar naarmate AI steeds meer voorkomt, moeten we ook de mogelijke schade begrijpen die wordt veroorzaakt door de [bewapening](https://www.youtube.com/watch?v=TQHs8SA1qpk) van dergelijke algoritmen op grote schaal.

Trends geven ook aan dat we tegen 2025 meer dan [180 zettabytes](https://www.statista.com/statistics/871513/worldwide-data-created/) aan gegevens zullen creëren en consumeren. Als **Data Scientists** geeft dit ons ongekende niveaus van toegang tot persoonlijke gegevens. Dit betekent dat we gedragsprofielen van gebruikers kunnen maken en de besluitvorming kunnen beïnvloeden op een manier die een [illusie van vrije keuze](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) creëert, terwijl gebruikers aangespoord worden naar resultaten die onze voorkeur hebben. Het roept ook bredere vragen op over gegevensprivacy en gebruikersbescherming.

Gegevensethiek is nu een _noodzakelijke vangrails_ voor datawetenschap en -engineering, waardoor we mogelijke schade en onbedoelde gevolgen van onze gegevensgestuurde acties kunnen minimaliseren. De [Gartner Hype Cycle for AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) identificeert relevante trends in digitale ethiek, verantwoorde AI en AI-governance als belangrijke drijfveren voor grotere megatrends rond _democratisering_ en _industrialisering_ van AI.

![Gartner's hypecyclus voor AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

In deze les verkennen we het fascinerende gebied van data-ethiek - van kernconcepten en uitdagingen tot casestudy's en toegepaste AI-concepten zoals governance - die helpen een ethische cultuur tot stand te brengen in teams en organisaties die met data en AI werken.




## [Pre-college quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## Basisdefinities

Laten we beginnen met het begrijpen van de basisterminologie.

Het woord "ethiek" komt van het [Griekse woord "ethikos"](https://en.wikipedia.org/wiki/Ethics) (en de wortel "ethos") wat _karakter of morele aard_ betekent.

**Ethiek** gaat over de gedeelde waarden en morele principes die ons gedrag in de samenleving bepalen. Ethiek is niet gebaseerd op wetten maar op
algemeen aanvaarde normen van wat "goed versus fout" is. Ethische overwegingen kunnen echter van invloed zijn op initiatieven op het gebied van corporate governance en overheidsregelgeving die meer prikkels voor compliance creëren.

**Data-ethiek** is een [nieuwe tak van ethiek](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1) die "morele problemen met betrekking tot _data, algoritmen en overeenkomstige praktijken_" bestudeerd. Hier richt **"data"** zich op acties met betrekking tot het genereren, opnemen, beheren, verwerken, verspreiden, delen en gebruiken. **"Algoritmen"** richt zich op AI, agents, machine learning en robots, en **"practices"** richt zich op onderwerpen als verantwoord innoveren, programmeren, hacken en ethische codes.

**Toegepaste ethiek** is de [praktische toepassing van morele overwegingen](https://en.wikipedia.org/wiki/Applied_ethics). Het is het proces van het actief onderzoeken van ethische kwesties in de context van _real-world acties, producten en processen_, en het nemen van corrigerende maatregelen om ervoor te zorgen dat deze in overeenstemming blijven met onze gedefinieerde ethische waarden.

**Ethische cultuur** gaat over [toegepaste ethiek _activeren_](https://hbr.org/2019/05/how-to-design-an-ethical-organization) om ervoor te zorgen dat onze ethische principes en praktijken worden toegepast in een consistente en schaalbare manier door de hele organisatie heen. Succesvolle ethische culturen definiëren organisatiebrede ethische principes, bieden zinvolle prikkels voor naleving en versterken ethische normen door gewenst gedrag op elk niveau van de organisatie aan te moedigen en te versterken.


## Ethische concepten

In dit gedeelte bespreken we concepten als **gedeelde waarden** (principes) en **ethische uitdagingen** (problemen) voor data-ethiek - en onderzoeken we **casestudy's** die je helpen deze concepten in context van de echte wereld te begrijpen.

### 1. Ethische principes

Elke data-ethiekstrategie begint met het definiëren van _ethische principes_ - de 'gedeelde waarden' die acceptabel gedrag beschrijven en richting geven aan daaraan conformerende acties in onze data- en AI-projecten. Je kunt deze op individueel of teamniveau definiëren. De meeste grote organisaties schetsen deze echter in een _ethische AI_-missieverklaring of -kader dat op bedrijfsniveau is gedefinieerd en consistent wordt gehandhaafd in alle teams.

**Voorbeeld:** Microsoft's [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai) mission statement luidt: _"We zetten ons in voor de vooruitgang van AI-driven door ethische principes die de mens centraal stellen"_ - door middel van 6 ethische principes in het onderstaande kader:

![Verantwoordelijke AI bij Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Laten we deze principes kort onderzoeken. _Transparantie_ en _accountability_ zijn fundamentele waarden waarop andere principes voortbouwen - dus laten we daar beginnen:

* [**Verantwoording**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) maakt beoefenaars _verantwoordelijk_ voor hun gegevens- en AI-operaties, en naleving van deze ethische principes.
* [**Transparantie**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) zorgt ervoor dat gegevens en AI-acties _begrijpelijk_ (interpreteerbaar) zijn voor gebruikers, zoals het wat en waarom achter beslissingen.
* [**Eerlijkheid**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - richt zich op het waarborgen dat AI _alle mensen_ eerlijk behandelt, waarbij alle systemische of impliciete socio-technische vooroordelen in data en systemen worden geaddresseerd.
* [**Betrouwbaarheid en veiligheid**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - zorgt ervoor dat AI zich _consistent_ gedraagt ​​met gedefinieerde waarden, waardoor potentiële schade of onbedoelde gevolgen worden geminimaliseerd.
* [**Privacy en beveiliging**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - gaat over het begrijpen van gegevensafstamming en het bieden van _gegevensprivacy en gerelateerde beschermingen_ voor gebruikers.
* [**Inclusiviteit**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - gaat over het ontwerpen van AI-oplossingen met intentie, ze aanpassen om te voldoen aan een _brede scala aan menselijke behoeften_ en mogelijkheden.

> 🚨 Denk na over wat jouw missie voor gegevensethiek zou kunnen zijn. Verken ethische AI-kaders van andere organisaties - hier zijn voorbeelden van [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles), en [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Welke gedeelde waarden hebben ze gemeen? Hoe verhouden deze principes zich tot het AI-product of de industrie waarin ze actief zijn?

### 2. Ethische uitdagingen

Zodra we ethische principes hebben gedefinieerd, is de volgende stap het evalueren van onze gegevens en AI-acties om te zien of ze in overeenstemming zijn met die gedeelde waarden. Denk na over je acties in twee categorieën: _gegevensverzameling_ en _algoritmeontwerp_.

Bij het verzamelen van gegevens zullen acties waarschijnlijk betrekking hebben op **persoonlijke gegevens** of persoonlijk identificeerbare informatie (PII) voor identificeerbare levende personen. Dit omvat [diverse items van niet-persoonlijke gegevens](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en) die _collectief_ een persoon identificeren. Ethische uitdagingen kunnen betrekking hebben op _gegevensprivacy_, _eigendom van gegevens_ en gerelateerde onderwerpen zoals _geïnformeerde toestemming_ en _intellectuele eigendomsrechten_ voor gebruikers.

Bij het ontwerpen van algoritmen zullen acties bestaan ​​uit het verzamelen en beheren van **datasets**, en deze vervolgens gebruiken om **datamodellen** te trainen en in te zetten die resultaten voorspellen of beslissingen automatiseren in reële contexten. Ethische uitdagingen kunnen ontstaan ​​door _dataset bias_, _data quality_ issues, _unfairness_ en _misrepresentation_ (onvoldoende vertegenwoordiging) in algoritmen - inclusief enkele problemen die systemisch van aard zijn.

In beide gevallen wijzen ethische uitdagingen op gebieden waar onze acties in conflict kunnen komen met onze gedeelde waarden. Om deze zorgen op te sporen, te verminderen, te minimaliseren of weg te nemen, moeten we morele "ja/nee"-vragen stellen met betrekking tot onze acties en vervolgens corrigerende maatregelen nemen als dat nodig is. Laten we eens kijken naar enkele ethische uitdagingen en de morele vragen die ze oproepen:

#### 2.1 Gegevenseigendom

Bij het verzamelen van gegevens gaat het vaak om persoonsgegevens die de betrokkenen kunnen identificeren. [Data-eigendom](https://permission.io/blog/data-ownership) gaat over _controle_ en [_gebruikers rechten_](https://permission.io/blog/data-ownership) met betrekking tot het aanmaken, verwerken en verspreiding van gegevens.

De morele vragen die we moeten stellen zijn:
 * Wie is eigenaar van de gegevens? (gebruiker of organisatie)
 * Welke rechten hebben betrokkenen? (bijvoorbeeld: toegang, wissen, overdraagbaarheid)
 * Welke rechten hebben organisaties? (bijvoorbeeld: kwaadwillende gebruikersrecensies corrigeren)

#### 2.2 Geïnformeerde toestemming

[Informed consent](https://legaldictionary.net/informed-consent/) definieert de handeling van gebruikers die instemmen met een actie (zoals gegevensverzameling) met een _volledig begrip_ van relevante feiten, waaronder het doel, potentiële risico's en alternatieven.

Vragen om hier te onderzoeken zijn:
 * Heeft de gebruiker (betrokkene) toestemming gegeven voor het vastleggen en gebruiken van gegevens?
 * Begreep de gebruiker het doel waarvoor die gegevens werden vastgelegd?
 * Begreep de gebruiker de mogelijke risico's van zijn deelname?

#### 2.3 Intellectuele eigendom

[Intellectuele eigendom](https://en.wikipedia.org/wiki/Intellectual_property) verwijst naar immateriële creaties die het resultaat zijn van menselijk initiatief en die _economische waarde_ kunnen hebben voor individuen of bedrijven.

Vragen om hier te onderzoeken zijn:
 * Hadden de verzamelde gegevens economische waarde voor een gebruiker of bedrijf?
 * Heeft de **gebruiker** hier intellectueel eigendom?
 * Heeft de **organisatie** hier intellectueel eigendom?
 * Als deze rechten bestaan, hoe beschermen we ze dan?

#### 2.4 Gegevensprivacy

[Data privacy](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) of informatieprivacy verwijst naar het behoud van de gebruikersprivacy en bescherming van de gebruikersidentiteit met betrekking tot persoonlijk identificeerbare informatie.

Vragen om hier te onderzoeken zijn:
 * Zijn (persoons)gegevens van gebruikers beveiligd tegen hacks en lekken?
 * Zijn gebruikersgegevens alleen toegankelijk voor geautoriseerde gebruikers en contexten?
 * Blijft de anonimiteit van gebruikers behouden wanneer gegevens worden gedeeld of verspreid?
 * Kan een gebruiker worden geanonimiseerd voor een geanonimiseerde datasets?

#### 2.5 Recht om vergeten te worden

Het [Recht om te worden vergeten](https://en.wikipedia.org/wiki/Right_to_be_forgotten) of [Recht tot verwijdering](https://www.gdpreu.org/right-to-be-forgotten/) biedt aanvullende bescherming van persoonsgegevens voor gebruikers. Het geeft gebruikers met name het recht om _onder specifieke omstandigheden_ persoonlijke gegevens van zoekopdrachten op internet en andere locaties te verzoeken tot wissen of verwijdering van persoonlijke gegevens, waardoor ze een nieuwe start online kunnen maken zonder dat er eerdere acties tegen hen worden ondernomen.

Vragen om hier te onderzoeken zijn:
 * Staat het systeem de betrokkenen toe om verwijdering aan te vragen?
 * Moet het intrekken van de toestemming van de gebruiker leiden tot automatische verwijdering?
 * Zijn er gegevens verzameld zonder toestemming of op onrechtmatige wijze?
 * Voldoen we aan de overheidsvoorschriften voor gegevensprivacy?

 #### 2.6 Gegevenssetbias

Dataset of [Verzamel Bias](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) gaat over het selecteren van een _niet-representatieve_ subset van gegevens voor de ontwikkeling van algoritmen, waardoor potentiële oneerlijkheid in resultaatuitkomsten voor diverse groepen ontstaat. Soorten bias zijn onder meer selectie- , vrijwilligers- en instrumentbias.

Vragen om hier te onderzoeken zijn:
 * Hebben we een representatieve set van betrokkenen geworven?
 * Hebben we onze verzamelde of samengestelde dataset getest op verschillende vooroordelen?
 * Kunnen we ontdekte vooroordelen verminderen of verwijderen?

#### 2.7 Gegevenskwaliteit

[Data Quality](https://lakefs.io/data-quality-testing/) kijkt naar de validiteit van de samengestelde dataset die is gebruikt om onze algoritmen te ontwikkelen en controleert of functies en records voldoen aan de vereisten voor het niveau van nauwkeurigheid en consistentie nodig voor ons AI-doel.

Vragen om hier te onderzoeken zijn:
 * Hebben we geldige _features_ vastgelegd voor onze use case?
 * Zijn gegevens _consistent_ vastgelegd in verschillende gegevensbronnen?
 * Is de dataset _compleet_ voor diverse omstandigheden of scenario's?
 * Wordt informatie _nauwkeurig_ vastgelegd in weerspiegeling van de werkelijkheid?

#### 2.8 Algoritme Eerlijkheid

[Algorithm Fairness](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) controleert of het ontwerp van het algoritme systematisch discrimineert tegen specifieke subgroepen van betrokkenen die leiden tot [potentiële schade](https://docs .microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) in _allocation_ (waar middelen worden geweigerd of onthouden aan die groep) en _quality of service_ (waar AI voor sommige subgroepen niet zo nauwkeurig is als het is voor anderen).

Vragen om hier te onderzoeken zijn:
 * Hebben we de modelnauwkeurigheid geëvalueerd voor verschillende subgroepen en condities?
 * Hebben we het systeem onderzocht op mogelijke schade (bijv. stereotypering)?
 * Kunnen we gegevens herzien of modellen omscholen om geïdentificeerde schade te beperken?

Verken bronnen zoals [AI Fairness checklists](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) voor meer informatie.

#### 2.9 Verkeerde voorstelling van zaken

[Vertegenwoordigende data](https://www.sciencedirect.com/topics/computer-science/misrepresentation) gaat over de vraag of we inzichten uit eerlijk gerapporteerde gegevens op een misleidende manier communiceren om een ​​gewenst verhaal te ondersteunen.

Vragen om hier te onderzoeken zijn:
 * Rapporteren we onvolledige of onjuiste gegevens?
 * Visualiseren we gegevens op een manier die leidt tot misleidende conclusies?
 * Gebruiken we selectieve statistische technieken om uitkomsten te manipuleren?
 * Zijn er alternatieve verklaringen die tot een andere conclusie kunnen leiden?

#### 2.10 Vrije keuze
De [Illusie van Vrije Keuze](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) treedt op wanneer systeem-keuze-architecturen besluitvormingsalgoritmen gebruiken om mensen ertoe aan te zetten een gewenste uitkomst te kiezen terwijl het hen opties en controle lijkt te geven. Deze ['darkpatterns'](https://www.darkpatterns.org/) kunnen gebruikers sociale en economische schade toebrengen. Omdat beslissingen van gebruikers van invloed zijn op gedragsprofielen, kunnen deze acties toekomstige keuzes stimuleren die de impact van deze schade kunnen vergroten of uitbreiden.

Vragen om hier te onderzoeken zijn:
 * Begreep de gebruiker de implicaties van het maken van die keuze?
 * Was de gebruiker op de hoogte van (alternatieve) keuzes en de voor- en nadelen van elk?
 * Kan de gebruiker een geautomatiseerde of beïnvloede keuze later terugdraaien?
 ### 3. Casestudy's

Om deze ethische uitdagingen in een reële context te plaatsen, helpt het om casestudies te bekijken die de potentiële schade en gevolgen voor individuen en de samenleving benadrukken, wanneer dergelijke ethische schendingen over het hoofd worden gezien.

Hier zijn een paar voorbeelden:

| Ethische uitdaging | Casestudy |
|--- |--- |
| **Informed Consent** | 1972 - [Tuskegee Syphilis Study](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Afro-Amerikaanse mannen die deelnamen aan het onderzoek kregen gratis medische zorg beloofd _maar werden misleid_ door onderzoekers die de proefpersonen niet informeerden over hun diagnose of over beschikbaarheid van de behandeling. Veel proefpersonen stierven en ook partners en kinderen werden hierdoor getroffen; de studie duurde 40 jaar. |
| **Gegevensprivacy** | 2007 - De [Netflix-gegevensprijs](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) voorzag onderzoekers van _10 miljoen geanonimiseerde filmranglijsten van 50.000 klanten_ om aanbevelingsalgoritmen te helpen verbeteren. Onderzoekers waren echter in staat om geanonimiseerde gegevens te correleren met persoonlijk identificeerbare gegevens in _externe datasets_ (bijv. IMDb-commentaren) - waardoor sommige Netflix-abonnees effectief te "de-anonimiseren" waren.|
| **Verzamelingsbias** | 2013 - De stad Boston [ontwikkelde Street Bump](https://www.boston.gov/transportation/street-bump), een app waarmee burgers kuilen kunnen melden, waardoor de stad betere weggegevens krijgt om problemen op te sporen en op te lossen. [mensen in lagere inkomensgroepen hadden echter minder toegang tot auto's en telefoons](https://hbr.org/2013/04/the-hidden-biases-in-big-data), waardoor hun problemen met de rijbaan onzichtbaar werden in deze app . Ontwikkelaars werkten samen met academici aan _gelijke toegang en digitale scheidslijnen_ kwesties voor eerlijkheid. |
| **Algoritmische eerlijkheid** | 2018 - De MIT [Gender Shades Study](http://gendershades.org/overview.html) evalueerde de nauwkeurigheid van AI-producten voor genderclassificatie, waarbij hiaten in de nauwkeurigheid voor vrouwen en personen van kleur werden blootgelegd. Een [Apple Card uit 2019](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) leek vrouwen minder krediet te bieden dan mannen. Beide illustreerden problemen in algoritmische bias die tot sociaaleconomische schade leiden.|
| **Onjuiste voorstelling van gegevens** | 2020 - Het [Departement van Volksgezondheid van Georgië heeft COVID-19-kaarten vrijgegeven](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid- 19-gevallen-afnemende-heropening) die burgers leek te misleiden over trends in bevestigde gevallen met niet-chronologische volgorde op de x-as. Dit illustreert een verkeerde voorstelling van zaken door middel van visualisatietrucs. |
| **Illusie van vrije keuze** | 2020 - Leerapp [ABCmouse betaalde $ 10 miljoen om een ​​FTC-klacht op te lossen](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) waar ouders aan een abonnementen vastzaten die ze niet konden opzeggen. Dit illustreert duistere patronen in keuzearchitecturen, waarbij gebruikers naar potentieel schadelijke keuzes werden gepusht. |
| **Gegevensprivacy en gebruikersrechten** | 2021 - Facebook [Data Breach](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify- gebruikers) gegevens van 530 miljoen gebruikers werden openbaar gemaakt, wat resulteerde in een schikking van $ 5 miljard aan de FTC. De organisatie weigerde echter gebruikers op de hoogte te stellen van de inbreuk die de gebruikersrechten rond gegevenstransparantie en -toegang schendt. |

Meer casestudy's bekijken? Bekijk deze bronnen:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - ethische dilemma's in verschillende sectoren.
* [cursus Data Science Ethics](https://www.coursera.org/learn/data-science-ethics#syllabus) - baanbrekende casestudies onderzocht.
* [Waar het mis is gegaan](https://deon.drivendata.org/examples/) - deon checklist met voorbeelden

> 🚨 Denk eens aan de casestudies die u hebt gezien - heeft u in uw leven een soortgelijke ethische uitdaging meegemaakt of erdoor getroffen? Kun je ten minste één andere casestudy bedenken die een van de ethische uitdagingen illustreert die we in deze sectie hebben besproken?

## Toegepaste ethiek

We hebben gesproken over ethische concepten, uitdagingen en casestudy's in reële contexten. Maar hoe beginnen we met het _toepassen_ van ethische principes en praktijken in onze projecten? En hoe _operationaliseren_ we deze praktijken voor beter bestuur? Laten we enkele echte oplossingen verkennen:

### 1. Professionele codes

Beroepscodes bieden organisaties één mogelijkheid om leden te "stimuleren" om hun ethische principes en missieverklaring te ondersteunen. Codes zijn _morele richtlijnen_ voor professioneel gedrag en helpen werknemers of leden om beslissingen te nemen die in lijn zijn met de principes van hun organisatie. Ze zijn slechts zo goed als de vrijwillige medewerking van leden; veel organisaties bieden echter extra beloningen en boetes om naleving door leden te motiveren.

Voorbeelden zijn:

 * [Oxford München](http://www.code-of-ethics.org/code-of-conduct/) Ethische code
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Gedragscode (gemaakt in 2013)
 * [ACM-code voor ethiek en professioneel gedrag](https://www.acm.org/code-of-ethics) (sinds 1993)

> 🚨 Behoor jij tot een professionele engineering- of datawetenschapsorganisatie? Verken hun site om te zien of ze een professionele ethische code definiëren. Wat zegt dit over hun ethische principes? Hoe "stimuleren" ze leden om de code te volgen?

### 2. Ethische checklists

Hoewel professionele richtlijnen _ethisch gedrag_ van beoefenaars definiëren, hebben ze [bekende beperkingen](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) bij de handhaving, met name bij grootschalige projecten. In plaats daarvan pleiten veel data Science-experts [voor checklists](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), die **principes kunnen verbinden met praktijken** in meer deterministische en bruikbare manieren.

Checklists zetten vragen om in "ja/nee"-taken die kunnen worden geoperationaliseerd, zodat ze kunnen worden gevolgd als onderdeel van standaard workflows voor productreleases.

Voorbeelden zijn:
 * [Deon](https://deon.drivendata.org/) - een checklist voor gegevensethiek voor algemene doeleinden gemaakt op basis van [aanbevelingen voor de sector](https://deon.drivendata.org/#checklist-citations) met een opdracht- line tool voor eenvoudige integratie.
 * [Privacy Audit Checklist](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - biedt algemene richtlijnen voor informatieverwerkingspraktijken vanuit juridische en sociale blootstellingsperspectieven.
 * [AI Fairness Checklist](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - gemaakt door AI-beoefenaars ter ondersteuning van de invoering en integratie van eerlijkheidscontroles in AI-ontwikkelingscycli .
 * [22 vragen voor ethiek in data en AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - meer open kader, gestructureerd voor de eerste verkenning van ethische kwesties in ontwerp-, implementatie- en organisatorische contexten.

 ### 3. Ethische voorschriften

Ethiek gaat over het definiëren van gedeelde waarden en het _vrijwillig_ doen van de juiste dingen. **Compliance** gaat over het _volgen van de wet_ indien en waar gedefinieerd. **Governance** omvat in grote lijnen alle manieren waarop organisaties handelen om ethische principes af te dwingen en te voldoen aan gevestigde wetten.

Tegenwoordig neemt governance binnen organisaties twee vormen aan. Ten eerste gaat het om het definiëren van **ethische AI**-principes en het vaststellen van praktijken om de acceptatie in alle AI-gerelateerde projecten in de organisatie te operationaliseren. Ten tweede gaat het om het naleven van alle door de overheid opgelegde **gegevensbeschermingsvoorschriften** voor de regio's waarin het actief is.

Voorbeelden van gegevensbescherming en privacyregelgeving:

 * `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - regelt de verzameling, het gebruik en de openbaarmaking van persoonlijke informatie door de federale overheid.
 * `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - beschermt persoonlijke gezondheidsgegevens.
 * `1998`, [Amerikaanse Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - beschermt de gegevensprivacy van kinderen onder de 13 jaar.
 * `2018`, [Algemene Verordening Gegevensbescherming (AVG)](https://gdpr-info.eu/) - biedt gebruikersrechten, gegevensbescherming en privacy.
 * `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) geeft consumenten meer _rechten_ over hun (persoonlijke) gegevens.
 * `2021`, China's [wet ter bescherming van persoonsgegevens](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021 -08-20/) zojuist gepasseerd, waardoor een van de sterkste online gegevensprivacyregels ter wereld is gecreëerd.

> 🚨 De door de Europese Unie gedefinieerde AVG (Algemene Verordening Gegevensbescherming) blijft vandaag een van de meest invloedrijke regels voor gegevensprivacy. Wist u dat het ook [8 gebruikersrechten](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) definieert om de digitale privacy en persoonlijke gegevens van burgers te beschermen? Lees wat deze zijn en waarom ze belangrijk zijn.


### 4. Ethische cultuur

Onthoud dat er een ongrijpbare kloof blijft tussen _compliance_ (genoeg doen om te voldoen aan "de letter van de wet") en het aanpakken van [systeemproblemen](https://www.coursera.org/learn/data-science-ethics/home/week /4) (zoals ossificatie, informatieasymmetrie en oneerlijke verdeling) die de bewapening van AI kunnen versnellen.

Dit laatste vereist [samenwerkingsbenaderingen voor het definiëren van ethische culturen](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f) die emotionele verbindingen en consistente gedeelde waarden _over organisaties_ in de industrie. Dit vraagt ​​om meer [geformaliseerde data-ethiekculturen](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) in organisaties - waardoor _iedereen_ [aan het Andon-koord kan trekken](https:/ /en.wikipedia.org/wiki/Andon_(manufacturing)) (om ethische problemen vroeg in het proces aan de orde te stellen) en het maken van _ethische beoordelingen_ (bijvoorbeeld bij het aannemen) een kerncriterium voor teamvorming in AI-projecten.

---
## [Quiz voor na het college](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/3) 🎯
## Review & Zelfstudie

Cursussen en boeken helpen bij het begrijpen van kernconcepten en uitdagingen op het gebied van ethiek, terwijl casestudy's en hulpmiddelen helpen bij toegepaste ethische praktijken in echte contexten. Hier zijn een paar bronnen om mee te beginnen.

* [Machine Learning voor beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - les over eerlijkheid, van Microsoft.
* [Principles of Responsible AI](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - gratis leertraject van Microsoft Learn.
* [Ethiek en gegevenswetenschap](https://resources.oreilly.com/examples/0636920203964) - O'Reilly EBook (M. Loukides, H. Mason et. al)
* [Data Science Ethics](https://www.coursera.org/learn/data-science-ethics#syllabus) - online cursus van de Universiteit van Michigan.
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - casestudy's van de Universiteit van Texas.

# Opdracht

[Schrijf een data-ethiek case study](/assignment.nl.md)