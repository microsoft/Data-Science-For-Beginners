<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "408c55cab2880daa4e78616308bd5db7",
  "translation_date": "2025-08-26T22:08:04+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "sv"
}
-->
# Introduktion till Data Science i Molnet

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Data Science i Molnet: Introduktion - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

I denna lektion kommer du att lära dig de grundläggande principerna för molnet, varför det kan vara intressant att använda molntjänster för att driva dina data science-projekt, och vi kommer att titta på några exempel på data science-projekt som körs i molnet.

## [Quiz före föreläsningen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## Vad är molnet?

Molnet, eller molnbaserad databehandling, är leveransen av ett brett utbud av betalningsbaserade datatjänster som är värd på en infrastruktur via internet. Tjänsterna inkluderar lösningar som lagring, databaser, nätverk, mjukvara, analys och intelligenta tjänster.

Vi brukar skilja mellan offentliga, privata och hybrida moln enligt följande:

* Offentligt moln: ett offentligt moln ägs och drivs av en tredje part som tillhandahåller sina databehandlingsresurser via internet till allmänheten.
* Privat moln: avser databehandlingsresurser som används exklusivt av ett enda företag eller organisation, med tjänster och en infrastruktur som underhålls på ett privat nätverk.
* Hybridmoln: hybridmolnet är ett system som kombinerar offentliga och privata moln. Användare väljer ett datacenter på plats, samtidigt som de tillåter data och applikationer att köras på ett eller flera offentliga moln.

De flesta molntjänster faller inom tre kategorier: Infrastruktur som en tjänst (IaaS), Plattform som en tjänst (PaaS) och Mjukvara som en tjänst (SaaS).

* Infrastruktur som en tjänst (IaaS): användare hyr en IT-infrastruktur som servrar och virtuella maskiner (VM), lagring, nätverk, operativsystem.
* Plattform som en tjänst (PaaS): användare hyr en miljö för att utveckla, testa, leverera och hantera mjukvaruapplikationer. Användare behöver inte oroa sig för att ställa in eller hantera den underliggande infrastrukturen av servrar, lagring, nätverk och databaser som behövs för utveckling.
* Mjukvara som en tjänst (SaaS): användare får tillgång till mjukvaruapplikationer via internet, på begäran och vanligtvis på abonnemangsbasis. Användare behöver inte oroa sig för att värda och hantera mjukvaruapplikationen, den underliggande infrastrukturen eller underhållet, som mjukvaruuppdateringar och säkerhetsåtgärder.

Några av de största molnleverantörerna är Amazon Web Services, Google Cloud Platform och Microsoft Azure.

## Varför välja molnet för Data Science?

Utvecklare och IT-proffs väljer att arbeta med molnet av många skäl, inklusive följande:

* Innovation: du kan driva dina applikationer genom att integrera innovativa tjänster skapade av molnleverantörer direkt i dina appar.
* Flexibilitet: du betalar bara för de tjänster du behöver och kan välja från ett brett utbud av tjänster. Du betalar vanligtvis efter användning och anpassar dina tjänster efter dina föränderliga behov.
* Budget: du behöver inte göra initiala investeringar för att köpa hårdvara och mjukvara, ställa in och driva datacenter på plats, och du kan bara betala för det du använder.
* Skalbarhet: dina resurser kan skalas efter projektets behov, vilket innebär att dina appar kan använda mer eller mindre datorkraft, lagring och bandbredd, genom att anpassa sig till externa faktorer vid varje given tidpunkt.
* Produktivitet: du kan fokusera på din verksamhet istället för att spendera tid på uppgifter som kan hanteras av någon annan, såsom att hantera datacenter.
* Tillförlitlighet: molnbaserad databehandling erbjuder flera sätt att kontinuerligt säkerhetskopiera dina data och du kan skapa katastrofåterställningsplaner för att hålla din verksamhet och dina tjänster igång, även i krissituationer.
* Säkerhet: du kan dra nytta av policyer, teknologier och kontroller som stärker säkerheten för ditt projekt.

Detta är några av de vanligaste anledningarna till varför människor väljer att använda molntjänster. Nu när vi har en bättre förståelse för vad molnet är och dess huvudsakliga fördelar, låt oss titta mer specifikt på arbetet som dataforskare och utvecklare som arbetar med data, och hur molnet kan hjälpa dem med flera utmaningar de kan möta:

* Lagra stora mängder data: istället för att köpa, hantera och skydda stora servrar kan du lagra dina data direkt i molnet, med lösningar som Azure Cosmos DB, Azure SQL Database och Azure Data Lake Storage.
* Utföra dataintegration: dataintegration är en viktig del av Data Science, som låter dig göra övergången från datainsamling till att vidta åtgärder. Med dataintegrationstjänster som erbjuds i molnet kan du samla in, transformera och integrera data från olika källor till ett enda datalager, med Data Factory.
* Bearbeta data: att bearbeta stora mängder data kräver mycket datorkraft, och inte alla har tillgång till tillräckligt kraftfulla maskiner för det, vilket är anledningen till att många väljer att direkt utnyttja molnets enorma datorkraft för att köra och distribuera sina lösningar.
* Använda dataanalystjänster: molntjänster som Azure Synapse Analytics, Azure Stream Analytics och Azure Databricks hjälper dig att omvandla dina data till användbara insikter.
* Använda maskininlärning och dataintelligens-tjänster: istället för att börja från grunden kan du använda maskininlärningsalgoritmer som erbjuds av molnleverantören, med tjänster som AzureML. Du kan också använda kognitiva tjänster som tal-till-text, text-till-tal, datorseende och mer.

## Exempel på Data Science i molnet

Låt oss göra detta mer konkret genom att titta på ett par scenarier.

### Realtidsanalys av sociala mediers sentiment
Vi börjar med ett scenario som ofta studeras av personer som börjar med maskininlärning: sentimentanalys av sociala medier i realtid.

Låt oss säga att du driver en nyhetswebbplats och vill utnyttja live-data för att förstå vilket innehåll dina läsare kan vara intresserade av. För att ta reda på mer om detta kan du bygga ett program som utför sentimentanalys i realtid av data från Twitter-publikationer, om ämnen som är relevanta för dina läsare.

De nyckelindikatorer du kommer att titta på är volymen av tweets om specifika ämnen (hashtags) och sentiment, som fastställs med hjälp av analysverktyg som utför sentimentanalys kring de angivna ämnena.

Stegen som krävs för att skapa detta projekt är följande:

* Skapa en event hub för att strömma indata, som kommer att samla in data från Twitter.
* Konfigurera och starta en Twitter-klientapplikation, som kommer att anropa Twitter Streaming APIs.
* Skapa ett Stream Analytics-jobb.
* Ange jobbets indata och fråga.
* Skapa en output-sink och ange jobbets output.
* Starta jobbet.

För att se hela processen, kolla in [dokumentationen](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Analys av vetenskapliga artiklar
Låt oss ta ett annat exempel på ett projekt skapat av [Dmitry Soshnikov](http://soshnikov.com), en av författarna till denna kursplan.

Dmitry skapade ett verktyg som analyserar COVID-artiklar. Genom att granska detta projekt kommer du att se hur du kan skapa ett verktyg som extraherar kunskap från vetenskapliga artiklar, får insikter och hjälper forskare att navigera genom stora samlingar av artiklar på ett effektivt sätt.

Låt oss se de olika stegen som används för detta:
* Extrahera och förbehandla information med [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Använda [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) för att parallellisera bearbetningen.
* Lagra och fråga information med [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Skapa en interaktiv dashboard för datautforskning och visualisering med Power BI.

För att se hela processen, besök [Dmitrys blogg](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Som du kan se kan vi utnyttja molntjänster på många sätt för att utföra Data Science.

## Fotnot

Källor:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Quiz efter föreläsningen

[Quiz efter föreläsningen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/33)

## Uppgift

[Marknadsundersökning](assignment.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.