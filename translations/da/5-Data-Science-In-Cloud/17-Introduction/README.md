<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-09-05T21:56:30+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "da"
}
-->
# Introduktion til Data Science i Skyen

|![ Sketchnote af [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Data Science i Skyen: Introduktion - _Sketchnote af [@nitya](https://twitter.com/nitya)_ |

I denne lektion vil du lære de grundlæggende principper for skyen, hvorfor det kan være interessant for dig at bruge skytjenester til at køre dine data science-projekter, og vi vil se på nogle eksempler på data science-projekter, der køres i skyen.

## [Quiz før lektionen](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## Hvad er Skyen?

Skyen, eller Cloud Computing, er levering af en bred vifte af betalingsbaserede computing-tjenester, der er hostet på en infrastruktur via internettet. Tjenesterne inkluderer løsninger som lagring, databaser, netværk, software, analyse og intelligente tjenester.

Vi skelner normalt mellem offentlig, privat og hybrid sky som følger:

* Offentlig sky: En offentlig sky ejes og drives af en tredjeparts skytjenesteudbyder, som leverer sine computing-ressourcer via internettet til offentligheden.
* Privat sky: Henviser til skytjenester, der udelukkende bruges af en enkelt virksomhed eller organisation, med tjenester og en infrastruktur, der vedligeholdes på et privat netværk.
* Hybrid sky: Hybrid skyen er et system, der kombinerer offentlige og private skyer. Brugere vælger et datacenter på stedet, mens de tillader data og applikationer at køre på en eller flere offentlige skyer.

De fleste skytjenester falder ind under tre kategorier: Infrastruktur som en tjeneste (IaaS), Platform som en tjeneste (PaaS) og Software som en tjeneste (SaaS).

* Infrastruktur som en tjeneste (IaaS): Brugere lejer en IT-infrastruktur såsom servere og virtuelle maskiner (VM'er), lagring, netværk, operativsystemer.
* Platform som en tjeneste (PaaS): Brugere lejer et miljø til udvikling, test, levering og styring af softwareapplikationer. Brugere behøver ikke bekymre sig om opsætning eller styring af den underliggende infrastruktur af servere, lagring, netværk og databaser, der er nødvendige for udvikling.
* Software som en tjeneste (SaaS): Brugere får adgang til softwareapplikationer via internettet, efter behov og typisk på abonnementsbasis. Brugere behøver ikke bekymre sig om hosting og styring af softwareapplikationen, den underliggende infrastruktur eller vedligeholdelse, som softwareopdateringer og sikkerhedspatching.

Nogle af de største skyudbydere er Amazon Web Services, Google Cloud Platform og Microsoft Azure.

## Hvorfor vælge Skyen til Data Science?

Udviklere og IT-professionelle vælger at arbejde med skyen af mange grunde, herunder følgende:

* Innovation: Du kan styrke dine applikationer ved at integrere innovative tjenester, der er skabt af skyudbydere, direkte i dine apps.
* Fleksibilitet: Du betaler kun for de tjenester, du har brug for, og kan vælge fra et bredt udvalg af tjenester. Du betaler typisk efter forbrug og tilpasser dine tjenester efter dine skiftende behov.
* Budget: Du behøver ikke foretage indledende investeringer i hardware og software, opsætning og drift af datacentre på stedet, og du kan blot betale for det, du bruger.
* Skalerbarhed: Dine ressourcer kan skaleres efter behovene i dit projekt, hvilket betyder, at dine apps kan bruge mere eller mindre computerkraft, lagring og båndbredde ved at tilpasse sig eksterne faktorer på ethvert tidspunkt.
* Produktivitet: Du kan fokusere på din virksomhed i stedet for at bruge tid på opgaver, der kan håndteres af andre, såsom styring af datacentre.
* Pålidelighed: Cloud Computing tilbyder flere måder at kontinuerligt sikkerhedskopiere dine data, og du kan oprette katastrofeberedskabsplaner for at holde din virksomhed og dine tjenester kørende, selv i krisetider.
* Sikkerhed: Du kan drage fordel af politikker, teknologier og kontroller, der styrker sikkerheden i dit projekt.

Dette er nogle af de mest almindelige grunde til, at folk vælger at bruge skytjenester. Nu hvor vi har en bedre forståelse af, hvad skyen er, og hvad dens vigtigste fordele er, lad os se mere specifikt på arbejdet for dataforskere og udviklere, der arbejder med data, og hvordan skyen kan hjælpe dem med flere udfordringer, de måtte stå overfor:

* Lagring af store mængder data: I stedet for at købe, administrere og beskytte store servere kan du lagre dine data direkte i skyen med løsninger som Azure Cosmos DB, Azure SQL Database og Azure Data Lake Storage.
* Udførelse af dataintegration: Dataintegration er en essentiel del af Data Science, der lader dig gå fra dataindsamling til handling. Med dataintegrationstjenester, der tilbydes i skyen, kan du indsamle, transformere og integrere data fra forskellige kilder i et enkelt datalager med Data Factory.
* Databehandling: Behandling af store mængder data kræver meget computerkraft, og ikke alle har adgang til maskiner, der er kraftige nok til det, hvilket er grunden til, at mange vælger at udnytte skyens enorme computerkraft direkte til at køre og implementere deres løsninger.
* Brug af dataanalyse-tjenester: Skytjenester som Azure Synapse Analytics, Azure Stream Analytics og Azure Databricks hjælper dig med at omdanne dine data til handlingsrettede indsigter.
* Brug af maskinlæring og dataintelligens-tjenester: I stedet for at starte fra bunden kan du bruge maskinlæringsalgoritmer, der tilbydes af skyudbyderen, med tjenester som AzureML. Du kan også bruge kognitive tjenester som tale-til-tekst, tekst-til-tale, computer vision og mere.

## Eksempler på Data Science i Skyen

Lad os gøre dette mere konkret ved at se på et par scenarier.

### Real-time sentimentanalyse af sociale medier
Vi starter med et scenarie, der ofte studeres af folk, der begynder med maskinlæring: sentimentanalyse af sociale medier i realtid.

Lad os sige, at du driver en nyhedsmedie-webside, og du vil udnytte live data til at forstå, hvilket indhold dine læsere kunne være interesserede i. For at finde ud af mere om det kan du bygge et program, der udfører real-time sentimentanalyse af data fra Twitter-publikationer om emner, der er relevante for dine læsere.

De nøgleindikatorer, du vil se på, er volumen af tweets om specifikke emner (hashtags) og sentiment, som fastlægges ved hjælp af analytiske værktøjer, der udfører sentimentanalyse omkring de specificerede emner.

De nødvendige trin for at oprette dette projekt er som følger:

* Opret en event hub til streaming input, som vil indsamle data fra Twitter.
* Konfigurer og start en Twitter-klientapplikation, som vil kalde Twitter Streaming APIs.
* Opret et Stream Analytics-job.
* Specificer jobinput og forespørgsel.
* Opret en output-sink og specificer joboutput.
* Start jobbet.

For at se hele processen, tjek [dokumentationen](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Analyse af videnskabelige artikler
Lad os tage et andet eksempel på et projekt skabt af [Dmitry Soshnikov](http://soshnikov.com), en af forfatterne til dette pensum.

Dmitry skabte et værktøj, der analyserer COVID-artikler. Ved at gennemgå dette projekt vil du se, hvordan du kan skabe et værktøj, der udtrækker viden fra videnskabelige artikler, opnår indsigter og hjælper forskere med at navigere gennem store samlinger af artikler på en effektiv måde.

Lad os se på de forskellige trin, der blev brugt til dette:
* Udtrækning og forbehandling af information med [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Brug af [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) til at parallelisere behandlingen.
* Lagring og forespørgsel af information med [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Opret en interaktiv dashboard til dataudforskning og visualisering ved hjælp af Power BI.

For at se hele processen, besøg [Dmitrys blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Som du kan se, kan vi udnytte skytjenester på mange måder til at udføre Data Science.

## Fodnote

Kilder:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Quiz efter lektionen

## [Quiz efter lektionen](https://ff-quizzes.netlify.app/en/ds/quiz/33)

## Opgave

[Markedsundersøgelse](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.