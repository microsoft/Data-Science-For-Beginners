<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a0556b17de4c8d1a9470b02247b01d4",
  "translation_date": "2025-09-04T19:23:08+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "no"
}
-->
# Introduksjon til Data Science i Skyen

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Data Science i Skyen: Introduksjon - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |


I denne leksjonen vil du lære de grunnleggende prinsippene for skyen, deretter vil du se hvorfor det kan være interessant for deg å bruke skytjenester til å kjøre dine data science-prosjekter, og vi skal se på noen eksempler på data science-prosjekter som kjøres i skyen. 

## [Quiz før forelesning](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## Hva er skyen?

Skyen, eller skybasert databehandling, er levering av et bredt spekter av betaling-etter-bruk datatjenester som er vert på en infrastruktur over internett. Tjenestene inkluderer løsninger som lagring, databaser, nettverk, programvare, analyse og intelligente tjenester. 

Vi skiller vanligvis mellom offentlig, privat og hybrid sky som følger: 

* Offentlig sky: en offentlig sky eies og drives av en tredjeparts skytjenesteleverandør som leverer sine databehandlingsressurser over internett til offentligheten. 
* Privat sky: refererer til databehandlingsressurser som brukes eksklusivt av en enkelt bedrift eller organisasjon, med tjenester og infrastruktur som opprettholdes på et privat nettverk. 
* Hybrid sky: hybrid sky er et system som kombinerer offentlig og privat sky. Brukere velger et lokalt datasenter, samtidig som de tillater data og applikasjoner å kjøre på en eller flere offentlige skyer. 

De fleste skytjenester faller inn i tre kategorier: Infrastruktur som en tjeneste (IaaS), Plattform som en tjeneste (PaaS) og Programvare som en tjeneste (SaaS).

* Infrastruktur som en tjeneste (IaaS): brukere leier en IT-infrastruktur som servere og virtuelle maskiner (VMs), lagring, nettverk, operativsystemer. 
* Plattform som en tjeneste (PaaS): brukere leier et miljø for utvikling, testing, levering og administrasjon av programvareapplikasjoner. Brukere trenger ikke å bekymre seg for å sette opp eller administrere den underliggende infrastrukturen av servere, lagring, nettverk og databaser som trengs for utvikling. 
* Programvare som en tjeneste (SaaS): brukere får tilgang til programvareapplikasjoner over internett, på forespørsel og vanligvis på abonnementsbasis. Brukere trenger ikke å bekymre seg for hosting og administrasjon av programvareapplikasjonen, den underliggende infrastrukturen eller vedlikehold, som programvareoppgraderinger og sikkerhetsoppdateringer. 

Noen av de største skyleverandørene er Amazon Web Services, Google Cloud Platform og Microsoft Azure.

## Hvorfor velge skyen for Data Science?

Utviklere og IT-profesjonelle velger å jobbe med skyen av mange grunner, inkludert følgende: 

* Innovasjon: du kan styrke applikasjonene dine ved å integrere innovative tjenester laget av skyleverandører direkte inn i appene dine.
* Fleksibilitet: du betaler kun for tjenestene du trenger og kan velge fra et bredt spekter av tjenester. Du betaler typisk etter bruk og tilpasser tjenestene dine etter dine utviklende behov. 
* Budsjett: du trenger ikke å gjøre innledende investeringer for å kjøpe maskinvare og programvare, sette opp og drive lokale datasentre, og du kan bare betale for det du bruker. 
* Skalerbarhet: ressursene dine kan skaleres i henhold til behovene til prosjektet ditt, noe som betyr at appene dine kan bruke mer eller mindre datakraft, lagring og båndbredde, ved å tilpasse seg eksterne faktorer når som helst. 
* Produktivitet: du kan fokusere på virksomheten din i stedet for å bruke tid på oppgaver som kan administreres av andre, som å administrere datasentre. 
* Pålitelighet: skybasert databehandling tilbyr flere måter å kontinuerlig sikkerhetskopiere dataene dine, og du kan sette opp katastrofegjenopprettingsplaner for å holde virksomheten og tjenestene i gang, selv i krisetider.
* Sikkerhet: du kan dra nytte av policyer, teknologier og kontroller som styrker sikkerheten til prosjektet ditt. 

Dette er noen av de vanligste grunnene til at folk velger å bruke skytjenester. Nå som vi har en bedre forståelse av hva skyen er og hva dens viktigste fordeler er, la oss se mer spesifikt på jobbene til dataforskere og utviklere som jobber med data, og hvordan skyen kan hjelpe dem med flere utfordringer de kan møte: 

* Lagring av store mengder data: i stedet for å kjøpe, administrere og beskytte store servere, kan du lagre dataene dine direkte i skyen, med løsninger som Azure Cosmos DB, Azure SQL Database og Azure Data Lake Storage.
* Utføre dataintegrasjon: dataintegrasjon er en essensiell del av Data Science, som lar deg gjøre en overgang fra datainnsamling til å ta handlinger. Med dataintegrasjonstjenester som tilbys i skyen, kan du samle inn, transformere og integrere data fra ulike kilder til et enkelt datalager, med Data Factory. 
* Behandle data: behandling av store mengder data krever mye datakraft, og ikke alle har tilgang til maskiner som er kraftige nok til det, noe som er grunnen til at mange velger å direkte utnytte skyens enorme datakraft for å kjøre og distribuere løsningene sine. 
* Bruke dataanalyse-tjenester: skytjenester som Azure Synapse Analytics, Azure Stream Analytics og Azure Databricks hjelper deg med å gjøre dataene dine om til handlingsbare innsikter. 
* Bruke maskinlæring og dataintelligens-tjenester: i stedet for å starte fra bunnen av, kan du bruke maskinlæringsalgoritmer som tilbys av skyleverandøren, med tjenester som AzureML. Du kan også bruke kognitive tjenester som tale-til-tekst, tekst-til-tale, datamaskinsyn og mer.

## Eksempler på Data Science i Skyen

La oss gjøre dette mer konkret ved å se på et par scenarier. 

### Sanntidsanalyse av sosiale medier-sentiment
Vi starter med et scenario som ofte studeres av folk som begynner med maskinlæring: sanntidsanalyse av sentiment på sosiale medier. 

La oss si at du driver et nyhetsmedie-nettsted og ønsker å utnytte live data for å forstå hvilket innhold leserne dine kan være interessert i. For å finne ut mer om dette, kan du bygge et program som utfører sanntidsanalyse av sentiment fra Twitter-publikasjoner, om emner som er relevante for leserne dine. 

De viktigste indikatorene du vil se på er volumet av tweets om spesifikke emner (hashtags) og sentiment, som etableres ved hjelp av analysetjenester som utfører sentimentanalyse rundt de spesifiserte emnene. 

Stegene som er nødvendige for å lage dette prosjektet er som følger: 

* Opprett en event hub for streaming input, som vil samle inn data fra Twitter 
* Konfigurer og start en Twitter-klientapplikasjon, som vil kalle Twitter Streaming APIs 
* Opprett en Stream Analytics-jobb 
* Spesifiser jobbinput og spørring 
* Opprett en output sink og spesifiser jobboutput 
* Start jobben 

For å se hele prosessen, sjekk ut [dokumentasjonen](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Analyse av vitenskapelige artikler
La oss ta et annet eksempel på et prosjekt laget av [Dmitry Soshnikov](http://soshnikov.com), en av forfatterne av dette pensumet. 

Dmitry laget et verktøy som analyserer COVID-artikler. Ved å gjennomgå dette prosjektet, vil du se hvordan du kan lage et verktøy som trekker ut kunnskap fra vitenskapelige artikler, får innsikter og hjelper forskere med å navigere gjennom store samlinger av artikler på en effektiv måte.

La oss se på de forskjellige stegene som ble brukt for dette: 
* Ekstrahere og forhåndsbehandle informasjon med [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)
* Bruke [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) for å parallellisere prosesseringen
* Lagring og spørring av informasjon med [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109)
* Opprett en interaktiv dashboard for datautforskning og visualisering ved hjelp av Power BI

For å se hele prosessen, besøk [Dmitrys blogg](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). 

Som du kan se, kan vi utnytte skytjenester på mange måter for å utføre Data Science.

## Fotnote

Kilder:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Quiz etter forelesning

## [Quiz etter forelesning](https://ff-quizzes.netlify.app/en/ds/)

## Oppgave

[Markedsundersøkelse](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.