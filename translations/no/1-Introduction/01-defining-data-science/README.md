<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43212cc1ac137b7bb1dcfb37ca06b0f4",
  "translation_date": "2025-10-25T18:56:20+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "no"
}
-->
# Definere Data Science

| ![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------: |
|              Definere Data Science - _Sketchnote av [@nitya](https://twitter.com/nitya)_               |

---

[![Definere Data Science Video](../../../../translated_images/no/video-def-ds.6623ee2392ef1abf6d7faf3fad10a4163642811749da75f44e35a5bb121de15c.png)](https://youtu.be/beZ7Mb_oz9I)

## [Quiz før forelesning](https://ff-quizzes.netlify.app/en/ds/quiz/0)

## Hva er Data?
I hverdagen er vi konstant omgitt av data. Teksten du leser nå er data. Listen over telefonnumre til vennene dine på smarttelefonen din er data, det samme er tiden som vises på klokken din. Som mennesker opererer vi naturlig med data ved å telle penger vi har eller ved å skrive brev til vennene våre.

Data ble imidlertid mye viktigere med oppfinnelsen av datamaskiner. Den primære rollen til datamaskiner er å utføre beregninger, men de trenger data for å fungere. Derfor må vi forstå hvordan datamaskiner lagrer og behandler data.

Med fremveksten av Internett har datamaskiners rolle som datahåndteringsenheter økt. Hvis du tenker over det, bruker vi nå datamaskiner mer og mer til databehandling og kommunikasjon, snarere enn til faktiske beregninger. Når vi skriver en e-post til en venn eller søker etter informasjon på Internett, skaper, lagrer, overfører og manipulerer vi i hovedsak data.
> Kan du huske sist gang du brukte en datamaskin til faktisk å beregne noe?

## Hva er Data Science?

I [Wikipedia](https://en.wikipedia.org/wiki/Data_science) er **Data Science** definert som *et vitenskapelig felt som bruker vitenskapelige metoder for å utvinne kunnskap og innsikt fra strukturerte og ustrukturerte data, og anvender kunnskap og handlingsrettet innsikt fra data på tvers av et bredt spekter av applikasjonsområder*.

Denne definisjonen fremhever følgende viktige aspekter ved data science:

* Hovedmålet med data science er å **utvinne kunnskap** fra data, med andre ord - å **forstå** data, finne skjulte sammenhenger og bygge en **modell**.
* Data science bruker **vitenskapelige metoder**, som sannsynlighet og statistikk. Faktisk, da begrepet *data science* først ble introdusert, mente noen at det bare var et nytt fancy navn for statistikk. I dag er det tydelig at feltet er mye bredere.
* Oppnådd kunnskap bør brukes til å produsere **handlingsrettet innsikt**, det vil si praktiske innsikter som kan brukes i virkelige forretningssituasjoner.
* Vi bør kunne operere med både **strukturerte** og **ustrukturerte** data. Vi kommer tilbake til å diskutere ulike typer data senere i kurset.
* **Applikasjonsområde** er et viktig konsept, og dataforskere trenger ofte en viss grad av ekspertise innen problemområdet, for eksempel: finans, medisin, markedsføring, osv.

> Et annet viktig aspekt ved Data Science er at det studerer hvordan data kan samles inn, lagres og bearbeides ved hjelp av datamaskiner. Mens statistikk gir oss matematiske grunnlag, bruker data science matematiske konsepter for faktisk å trekke innsikt fra data.

En av måtene (tilskrevet [Jim Gray](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) å se på data science er å betrakte det som et eget vitenskapsparadigme:
* **Empirisk**, der vi hovedsakelig baserer oss på observasjoner og resultater fra eksperimenter
* **Teoretisk**, der nye konsepter oppstår fra eksisterende vitenskapelig kunnskap
* **Computational**, der vi oppdager nye prinsipper basert på noen beregningsmessige eksperimenter
* **Datadrevet**, basert på å oppdage sammenhenger og mønstre i data  

## Andre Relaterte Felt

Siden data er allestedsnærværende, er data science i seg selv også et bredt felt som berører mange andre disipliner.

<dl>
<dt>Databaser</dt>
<dd>
En kritisk vurdering er <b>hvordan man lagrer</b> data, altså hvordan man strukturerer det på en måte som tillater raskere behandling. Det finnes ulike typer databaser som lagrer strukturerte og ustrukturerte data, som <a href="../../2-Working-With-Data/README.md">vi vil se nærmere på i vårt kurs</a>.
</dd>
<dt>Big Data</dt>
<dd>
Ofte må vi lagre og behandle svært store mengder data med en relativt enkel struktur. Det finnes spesielle tilnærminger og verktøy for å lagre data på en distribuert måte på en datamaskinklynge, og behandle det effektivt.
</dd>
<dt>Maskinlæring</dt>
<dd>
En måte å forstå data på er å <b>bygge en modell</b> som kan forutsi ønsket resultat. Å utvikle modeller fra data kalles <b>maskinlæring</b>. Du kan ta en titt på vårt <a href="https://aka.ms/ml-beginners">Maskinlæring for Nybegynnere</a>-kurs for å lære mer om det.
</dd>
<dt>Kunstig intelligens</dt>
<dd>
Et område innen maskinlæring kjent som kunstig intelligens (AI) er også avhengig av data, og det innebærer å bygge svært komplekse modeller som etterligner menneskelige tankeprosesser. AI-metoder lar oss ofte omdanne ustrukturerte data (f.eks. naturlig språk) til strukturerte innsikter. 
</dd>
<dt>Visualisering</dt>
<dd>
Store mengder data er uforståelige for et menneske, men når vi lager nyttige visualiseringer ved hjelp av data, kan vi få mer mening ut av det og trekke noen konklusjoner. Derfor er det viktig å kjenne til mange måter å visualisere informasjon på - noe vi vil dekke i <a href="../../3-Data-Visualization/README.md">Seksjon 3</a> av vårt kurs. Relaterte felt inkluderer også <b>Infografikk</b> og <b>Menneske-datamaskin-interaksjon</b> generelt. 
</dd>
</dl>

## Typer av Data

Som vi allerede har nevnt, er data overalt. Vi trenger bare å fange det på riktig måte! Det er nyttig å skille mellom **strukturerte** og **ustrukturerte** data. Førstnevnte er vanligvis representert i en godt strukturert form, ofte som en tabell eller flere tabeller, mens sistnevnte bare er en samling av filer. Noen ganger kan vi også snakke om **semi-strukturerte** data, som har en slags struktur som kan variere mye.

| Strukturert                                                                  | Semi-strukturert                                                                               | Ustrukturert                            |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------- |
| Liste over personer med telefonnumrene deres                                 | Wikipedia-sider med lenker                                                                    | Tekst fra Encyclopedia Britannica       |
| Temperatur i alle rom i en bygning hvert minutt de siste 20 årene            | Samling av vitenskapelige artikler i JSON-format med forfattere, publiseringsdato og sammendrag | Filarkiv med bedriftsdokumenter         |
| Data om alder og kjønn til alle som går inn i bygningen                      | Internetsider                                                                                  | Rå videostrøm fra overvåkningskamera    |

## Hvor man kan få tak i Data

Det finnes mange mulige kilder til data, og det vil være umulig å liste opp alle! La oss imidlertid nevne noen typiske steder hvor du kan få tak i data:

* **Strukturert**
  - **Internet of Things** (IoT), inkludert data fra ulike sensorer, som temperatur- eller trykksensorer, gir mye nyttig data. For eksempel, hvis en kontorbygning er utstyrt med IoT-sensorer, kan vi automatisk kontrollere oppvarming og belysning for å minimere kostnader. 
  - **Undersøkelser** som vi ber brukere om å fylle ut etter et kjøp, eller etter å ha besøkt en nettside.
  - **Analyse av atferd** kan for eksempel hjelpe oss med å forstå hvor dypt en bruker går inn på en nettside, og hva som er den typiske årsaken til at de forlater siden.
* **Ustrukturert**
  - **Tekster** kan være en rik kilde til innsikt, som en overordnet **sentimentscore**, eller ved å trekke ut nøkkelord og semantisk mening.
  - **Bilder** eller **Video**. En video fra et overvåkningskamera kan brukes til å estimere trafikken på veien og informere folk om potensielle trafikkorker.
  - Webserver **logger** kan brukes til å forstå hvilke sider på nettstedet vårt som oftest blir besøkt, og hvor lenge.
* Semi-strukturert
  - **Sosiale nettverk**-grafer kan være gode kilder til data om brukeres personligheter og potensiell effektivitet i å spre informasjon.
  - Når vi har en haug med fotografier fra en fest, kan vi prøve å trekke ut **gruppe-dynamikk**-data ved å bygge en graf over personer som tar bilder sammen.

Ved å kjenne til ulike mulige kilder til data, kan du prøve å tenke på ulike scenarier der data science-teknikker kan brukes til å forstå situasjonen bedre og forbedre forretningsprosesser. 

## Hva du kan gjøre med Data

I Data Science fokuserer vi på følgende steg i datareisen:

<dl>
<dt>1) Datainnsamling</dt>
<dd>
Det første steget er å samle inn data. Selv om det i mange tilfeller kan være en enkel prosess, som data som kommer inn i en database fra en webapplikasjon, må vi noen ganger bruke spesielle teknikker. For eksempel kan data fra IoT-sensorer være overveldende, og det er en god praksis å bruke bufferingsendepunkter som IoT Hub for å samle all data før videre behandling.
</dd>
<dt>2) Datalagring</dt>
<dd>
Å lagre data kan være utfordrende, spesielt hvis vi snakker om store datamengder. Når man bestemmer seg for hvordan man skal lagre data, er det fornuftig å forutse hvordan man ønsker å hente ut dataen i fremtiden. Det finnes flere måter data kan lagres:
<ul>
<li>En relasjonsdatabase lagrer en samling av tabeller og bruker et spesielt språk kalt SQL for å hente dem. Vanligvis er tabeller organisert i ulike grupper kalt skjemaer. I mange tilfeller må vi konvertere data fra sin opprinnelige form for å passe inn i skjemaet.</li>
<li><a href="https://en.wikipedia.org/wiki/NoSQL">En NoSQL</a>-database, som <a href="https://azure.microsoft.com/services/cosmos-db/?WT.mc_id=academic-77958-bethanycheum">CosmosDB</a>, påtvinger ikke skjemaer på data og tillater lagring av mer kompleks data, for eksempel hierarkiske JSON-dokumenter eller grafer. Imidlertid har ikke NoSQL-databaser de rike spørringsmulighetene til SQL og kan ikke påtvinge referanseintegritet, dvs. regler for hvordan data er strukturert i tabeller og styrer forholdet mellom tabeller.</li>
<li><a href="https://en.wikipedia.org/wiki/Data_lake">Data Lake</a>-lagring brukes til store samlinger av data i rå, ustrukturert form. Data Lakes brukes ofte med big data, der all data ikke kan passe på én maskin og må lagres og behandles av en serverklynge. <a href="https://en.wikipedia.org/wiki/Apache_Parquet">Parquet</a> er dataformatet som ofte brukes i forbindelse med big data.</li> 
</ul>
</dd>
<dt>3) Databehandling</dt>
<dd>
Dette er den mest spennende delen av datareisen, som innebærer å konvertere data fra sin opprinnelige form til en form som kan brukes til visualisering/modelltrening. Når vi arbeider med ustrukturerte data som tekst eller bilder, kan vi trenge å bruke noen AI-teknikker for å trekke ut <b>funksjoner</b> fra dataen, og dermed konvertere den til en strukturert form.
</dd>
<dt>4) Visualisering / Menneskelig innsikt</dt>
<dd>
Ofte, for å forstå data, må vi visualisere den. Ved å ha mange forskjellige visualiseringsteknikker i verktøykassen vår, kan vi finne den rette måten å få innsikt på. Ofte trenger en dataforsker å "leke med data", visualisere den mange ganger og lete etter sammenhenger. Vi kan også bruke statistiske teknikker for å teste hypoteser eller bevise en korrelasjon mellom ulike deler av data.   
</dd>
<dt>5) Trening av en prediktiv modell</dt>
<dd>
Fordi det ultimate målet med data science er å kunne ta beslutninger basert på data, kan vi bruke teknikker fra <a href="http://github.com/microsoft/ml-for-beginners">Maskinlæring</a> for å bygge en prediktiv modell. Vi kan deretter bruke denne til å gjøre forutsigelser ved hjelp av nye datasett med lignende strukturer.
</dd>
</dl>

Selvfølgelig, avhengig av den faktiske dataen, kan noen steg mangle (f.eks. når vi allerede har dataen i databasen, eller når vi ikke trenger modelltrening), eller noen steg kan gjentas flere ganger (som databehandling).

## Digitalisering og Digital Transformasjon

I løpet av det siste tiåret har mange bedrifter begynt å forstå viktigheten av data når de tar forretningsbeslutninger. For å anvende prinsippene for data science på bedriftsdrift, må man først samle inn noe data, dvs. oversette forretningsprosesser til digital form. Dette kalles **digitalisering**. Å bruke data science-teknikker på denne dataen for å veilede beslutninger kan føre til betydelige produktivitetsøkninger (eller til og med en omstilling av virksomheten), kalt **digital transformasjon**.

La oss vurdere et eksempel. Anta at vi har et data science-kurs (som dette) som vi leverer online til studenter, og vi ønsker å bruke data science for å forbedre det. Hvordan kan vi gjøre det?

Vi kan starte med å spørre "Hva kan digitaliseres?" Den enkleste måten ville være å måle tiden det tar for hver student å fullføre hver modul, og å måle den oppnådde kunnskapen ved å gi en flervalgstest på slutten av hver modul. Ved å beregne gjennomsnittlig tid til fullføring på tvers av alle studenter, kan vi finne ut hvilke moduler som skaper mest utfordringer for studentene, og jobbe med å forenkle dem.
> Du kan argumentere for at denne tilnærmingen ikke er ideell, fordi moduler kan ha ulik lengde. Det er sannsynligvis mer rettferdig å dele tiden på lengden av modulen (i antall tegn) og sammenligne disse verdiene i stedet.

Når vi begynner å analysere resultatene fra flervalgstester, kan vi prøve å finne ut hvilke konsepter studentene har vanskeligheter med å forstå, og bruke den informasjonen til å forbedre innholdet. For å gjøre det, må vi designe tester på en slik måte at hvert spørsmål knyttes til et bestemt konsept eller en kunnskapsdel.

Hvis vi vil gjøre det enda mer komplisert, kan vi plotte tiden brukt på hver modul mot alderskategorien til studentene. Vi kan finne ut at det for noen alderskategorier tar uforholdsmessig lang tid å fullføre modulen, eller at studentene slutter før de fullfører den. Dette kan hjelpe oss med å gi aldersanbefalinger for modulen og minimere misnøye på grunn av feil forventninger.

## 🚀 Utfordring

I denne utfordringen skal vi prøve å finne konsepter som er relevante for feltet Data Science ved å se på tekster. Vi skal ta en Wikipedia-artikkel om Data Science, laste ned og behandle teksten, og deretter lage en ordsky som denne:

![Ordsky for Data Science](../../../../translated_images/no/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.png)

Besøk [`notebook.ipynb`](../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') for å lese gjennom koden. Du kan også kjøre koden og se hvordan den utfører alle datatransformasjonene i sanntid.

> Hvis du ikke vet hvordan du kjører kode i en Jupyter Notebook, kan du ta en titt på [denne artikkelen](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Quiz etter forelesning](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Oppgaver

* **Oppgave 1**: Endre koden ovenfor for å finne relaterte konsepter for feltene **Big Data** og **Maskinlæring**  
* **Oppgave 2**: [Tenk på scenarier innen Data Science](assignment.md)

## Kreditering

Denne leksjonen er laget med ♥️ av [Dmitry Soshnikov](http://soshnikov.com)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.