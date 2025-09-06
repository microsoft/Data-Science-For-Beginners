<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a0516588d172f82f35f7a0d4a001e5d0",
  "translation_date": "2025-09-05T22:29:00+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "no"
}
-->
# Definere Data Science

| ![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------: |
|              Definere Data Science - _Sketchnote av [@nitya](https://twitter.com/nitya)_               |

---

[![Definere Data Science Video](../../../../1-Introduction/01-defining-data-science/images/video-def-ds.png)](https://youtu.be/beZ7Mb_oz9I)

## [Quiz før forelesning](https://ff-quizzes.netlify.app/en/ds/quiz/0)

## Hva er Data?
I hverdagen er vi konstant omgitt av data. Teksten du leser nå er data. Listen over telefonnumre til vennene dine på smarttelefonen din er data, og det samme er tiden som vises på klokken din. Som mennesker opererer vi naturlig med data, enten det er å telle penger eller skrive brev til venner.

Men data ble langt viktigere med fremveksten av datamaskiner. Datamaskiners hovedoppgave er å utføre beregninger, men de trenger data for å fungere. Derfor må vi forstå hvordan datamaskiner lagrer og behandler data.

Med Internettets fremvekst økte datamaskiners rolle som datahåndteringsenheter. Hvis du tenker over det, bruker vi nå datamaskiner mer og mer til databehandling og kommunikasjon, snarere enn til rene beregninger. Når vi skriver en e-post til en venn eller søker etter informasjon på Internett, skaper, lagrer, overfører og manipulerer vi i bunn og grunn data.
> Kan du huske sist gang du brukte en datamaskin til faktisk å beregne noe?

## Hva er Data Science?

I [Wikipedia](https://en.wikipedia.org/wiki/Data_science) defineres **Data Science** som *et vitenskapelig felt som bruker vitenskapelige metoder for å hente kunnskap og innsikt fra strukturerte og ustrukturerte data, og anvender kunnskap og handlingsrettede innsikter fra data på tvers av et bredt spekter av bruksområder*.

Denne definisjonen fremhever følgende viktige aspekter ved data science:

* Hovedmålet med data science er å **hente kunnskap** fra data, med andre ord - å **forstå** data, finne skjulte sammenhenger og bygge en **modell**.
* Data science bruker **vitenskapelige metoder**, som sannsynlighet og statistikk. Da begrepet *data science* først ble introdusert, mente noen at det bare var et nytt og fancy navn for statistikk. I dag er det tydelig at feltet er langt bredere.
* Den oppnådde kunnskapen bør brukes til å produsere **handlingsrettede innsikter**, altså praktiske innsikter som kan anvendes i reelle forretningssituasjoner.
* Vi må kunne operere på både **strukturerte** og **ustrukturerte** data. Vi kommer tilbake til ulike typer data senere i kurset.
* **Bruksområde** er et viktig konsept, og dataforskere trenger ofte en viss grad av ekspertise innen problemområdet, for eksempel: finans, medisin, markedsføring osv.

> Et annet viktig aspekt ved Data Science er at det studerer hvordan data kan samles inn, lagres og bearbeides ved hjelp av datamaskiner. Mens statistikk gir oss matematiske grunnlag, bruker data science matematiske konsepter for faktisk å trekke innsikter fra data.

En måte (tilskrevet [Jim Gray](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) å se på data science på, er å betrakte det som et eget vitenskapsparadigme:
* **Empirisk**, hvor vi hovedsakelig baserer oss på observasjoner og eksperimentresultater
* **Teoretisk**, hvor nye konsepter oppstår fra eksisterende vitenskapelig kunnskap
* **Beregningsteknisk**, hvor vi oppdager nye prinsipper basert på beregningseksperimenter
* **Datadrevet**, basert på å oppdage sammenhenger og mønstre i data

## Andre Relaterte Felt

Siden data er allestedsnærværende, er data science også et bredt felt som berører mange andre disipliner.

## Typer av Data

Som vi allerede har nevnt, er data overalt. Vi må bare fange det på riktig måte! Det er nyttig å skille mellom **strukturerte** og **ustrukturerte** data. Førstnevnte er vanligvis representert i en velstrukturert form, ofte som en tabell eller flere tabeller, mens sistnevnte bare er en samling filer. Noen ganger kan vi også snakke om **semi-strukturerte** data, som har en viss struktur som kan variere mye.

| Strukturert                                                                  | Semi-strukturert                                                                               | Ustrukturert                           |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | -------------------------------------- |
| Liste over personer med telefonnumrene deres                                 | Wikipedia-sider med lenker                                                                    | Teksten i Encyclopedia Britannica     |
| Temperatur i alle rom i en bygning hvert minutt de siste 20 årene            | Samling av vitenskapelige artikler i JSON-format med forfattere, publikasjonsdato og sammendrag | Fildeling med bedriftsdokumenter      |
| Data om alder og kjønn til alle som går inn i bygningen                      | Internett-sider                                                                               | Rå videostrøm fra overvåkningskamera  |

## Hvor man kan få Data

Det finnes mange mulige kilder til data, og det er umulig å liste opp alle! Men la oss nevne noen typiske steder hvor du kan få data:

* **Strukturert**
  - **Internet of Things** (IoT), inkludert data fra ulike sensorer som temperatur- eller trykksensorer, gir mye nyttig data. For eksempel, hvis et kontorbygg er utstyrt med IoT-sensorer, kan vi automatisk kontrollere oppvarming og belysning for å minimere kostnader.
  - **Undersøkelser** som vi ber brukere fylle ut etter et kjøp eller etter å ha besøkt et nettsted.
  - **Analyse av atferd** kan for eksempel hjelpe oss med å forstå hvor dypt en bruker går inn på et nettsted, og hva som er den typiske årsaken til at de forlater det.
* **Ustrukturert**
  - **Tekster** kan være en rik kilde til innsikt, som en overordnet **stemningsscore**, eller ved å trekke ut nøkkelord og semantisk mening.
  - **Bilder** eller **Video**. En video fra et overvåkningskamera kan brukes til å estimere trafikken på veien og informere folk om potensielle trafikkorker.
  - Webserver-**logger** kan brukes til å forstå hvilke sider på nettstedet vårt som oftest besøkes, og hvor lenge.
* **Semi-strukturert**
  - **Sosiale nettverk**-grafer kan være gode kilder til data om brukeres personligheter og potensielle effektivitet i å spre informasjon.
  - Når vi har en haug med fotografier fra en fest, kan vi prøve å trekke ut **gruppe-dynamikk**-data ved å bygge en graf over folk som tar bilder sammen.

Ved å kjenne til ulike mulige datakilder, kan du prøve å tenke på ulike scenarier der data science-teknikker kan brukes for å forstå situasjonen bedre og forbedre forretningsprosesser.

## Hva du kan gjøre med Data

I Data Science fokuserer vi på følgende trinn i datareisen:

Selvfølgelig, avhengig av de faktiske dataene, kan noen trinn mangle (f.eks. når vi allerede har dataene i databasen, eller når vi ikke trenger modelltrening), eller noen trinn kan gjentas flere ganger (som databehandling).

## Digitalisering og Digital Transformasjon

I løpet av det siste tiåret har mange bedrifter begynt å forstå viktigheten av data når de tar forretningsbeslutninger. For å anvende prinsippene for data science i en bedrift, må man først samle inn data, altså oversette forretningsprosesser til digital form. Dette kalles **digitalisering**. Å bruke data science-teknikker på disse dataene for å veilede beslutninger kan føre til betydelige produktivitetsøkninger (eller til og med en forretningspivot), kjent som **digital transformasjon**.

La oss se på et eksempel. Anta at vi har et data science-kurs (som dette) som vi leverer online til studenter, og vi ønsker å bruke data science for å forbedre det. Hvordan kan vi gjøre det?

Vi kan starte med å spørre: "Hva kan digitaliseres?" Den enkleste måten ville være å måle tiden det tar for hver student å fullføre hver modul, og å måle den oppnådde kunnskapen ved å gi en flervalgsprøve på slutten av hver modul. Ved å gjennomsnittliggjøre tiden det tar å fullføre på tvers av alle studenter, kan vi finne ut hvilke moduler som skaper mest vanskeligheter for studentene, og jobbe med å forenkle dem.
> Du kan argumentere for at denne tilnærmingen ikke er optimal, fordi moduler kan ha ulik lengde. Det er sannsynligvis mer rettferdig å dele tiden på lengden av modulen (i antall tegn) og sammenligne disse verdiene i stedet.
Når vi begynner å analysere resultatene fra flervalgstester, kan vi prøve å finne ut hvilke konsepter studentene har vanskeligheter med å forstå, og bruke den informasjonen til å forbedre innholdet. For å gjøre dette må vi designe tester slik at hvert spørsmål knyttes til et bestemt konsept eller kunnskapsområde.

Hvis vi ønsker å gjøre det enda mer komplisert, kan vi plotte tiden brukt på hvert modul mot alderskategorien til studentene. Vi kan oppdage at det for enkelte alderskategorier tar uforholdsmessig lang tid å fullføre modulen, eller at studentene slutter før de fullfører. Dette kan hjelpe oss med å gi aldersanbefalinger for modulen og minimere misnøye fra feil forventninger.

## 🚀 Utfordring

I denne utfordringen skal vi prøve å finne konsepter som er relevante for feltet Data Science ved å se på tekster. Vi skal ta en Wikipedia-artikkel om Data Science, laste ned og prosessere teksten, og deretter lage en ordsky som denne:

![Ordsky for Data Science](../../../../1-Introduction/01-defining-data-science/images/ds_wordcloud.png)

Besøk [`notebook.ipynb`](../../../../../../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') for å lese gjennom koden. Du kan også kjøre koden og se hvordan den utfører alle datatransformasjoner i sanntid.

> Hvis du ikke vet hvordan du kjører kode i en Jupyter Notebook, ta en titt på [denne artikkelen](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Quiz etter forelesning](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Oppgaver

* **Oppgave 1**: Endre koden ovenfor for å finne relaterte konsepter for feltene **Big Data** og **Maskinlæring**
* **Oppgave 2**: [Tenk på Data Science-scenarier](assignment.md)

## Kreditering

Denne leksjonen er laget med ♥️ av [Dmitry Soshnikov](http://soshnikov.com)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.