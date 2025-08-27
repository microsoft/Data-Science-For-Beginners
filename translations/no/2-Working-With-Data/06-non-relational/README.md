<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "32ddfef8121650f2ca2f3416fd283c37",
  "translation_date": "2025-08-26T21:10:37+00:00",
  "source_file": "2-Working-With-Data/06-non-relational/README.md",
  "language_code": "no"
}
-->
# Arbeide med data: Ikke-relasjonelle data

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/06-NoSQL.png)|
|:---:|
|Arbeide med NoSQL-data - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

## [Quiz før forelesning](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/10)

Data er ikke begrenset til relasjonsdatabaser. Denne leksjonen fokuserer på ikke-relasjonelle data og vil dekke det grunnleggende om regneark og NoSQL.

## Regneark

Regneark er en populær måte å lagre og utforske data på fordi det krever mindre arbeid for å sette opp og komme i gang. I denne leksjonen vil du lære de grunnleggende komponentene i et regneark, samt formler og funksjoner. Eksemplene vil bli illustrert med Microsoft Excel, men de fleste delene og temaene vil ha lignende navn og trinn sammenlignet med andre regnearkprogrammer.

![En tom Microsoft Excel-arbeidsbok med to regneark](../../../../translated_images/parts-of-spreadsheet.120711c82aa18a45c3e62a491a15bba0a31ab0e9db407ec022702fed8ffd89bf.no.png)

Et regneark er en fil og vil være tilgjengelig i filsystemet på en datamaskin, enhet eller skybasert filsystem. Selve programvaren kan være nettleserbasert eller en applikasjon som må installeres på en datamaskin eller lastes ned som en app. I Excel defineres disse filene også som **arbeidsbøker**, og denne terminologien vil bli brukt resten av denne leksjonen.

En arbeidsbok inneholder ett eller flere **regneark**, der hvert regneark er merket med faner. Innenfor et regneark er det rektangler kalt **celler**, som inneholder selve dataene. En celle er skjæringspunktet mellom en rad og en kolonne, der kolonnene er merket med alfabetiske tegn og radene er merket numerisk. Noen regneark vil inneholde overskrifter i de første radene for å beskrive dataene i en celle.

Med disse grunnleggende elementene i en Excel-arbeidsbok vil vi bruke et eksempel fra [Microsoft Templates](https://templates.office.com/) fokusert på et lager for å gå gjennom noen flere deler av et regneark.

### Administrere et lager

Regnearkfilen kalt "InventoryExample" er et formatert regneark med elementer i et lager som inneholder tre regneark, der fanene er merket "Inventory List", "Inventory Pick List" og "Bin Lookup". Rad 4 i regnearket Inventory List er overskriften, som beskriver verdien av hver celle i overskriftskolonnen.

![En uthevet formel fra et eksempel på en lagerliste i Microsoft Excel](../../../../translated_images/formula-excel.ad1068c220892f5ead570d12f2394897961d31a5043a1dd4e6fc5d7690c7a14e.no.png)

Det finnes tilfeller der en celle er avhengig av verdiene i andre celler for å generere sin verdi. Lagerlisten holder oversikt over kostnaden for hver vare i lageret, men hva om vi trenger å vite verdien av alt i lageret? [**Formler**](https://support.microsoft.com/en-us/office/overview-of-formulas-34519a4e-1e8d-4f4b-84d4-d642c4f63263) utfører handlinger på celldata og brukes til å beregne lagerverdien i dette eksemplet. Dette regnearket brukte en formel i kolonnen Inventory Value for å beregne verdien av hver vare ved å multiplisere mengden under overskriften QTY og kostnadene under overskriften COST. Ved å dobbeltklikke eller markere en celle vil du se formelen. Du vil legge merke til at formler starter med et likhetstegn, etterfulgt av beregningen eller operasjonen.

![En uthevet funksjon fra et eksempel på en lagerliste i Microsoft Excel](../../../../translated_images/function-excel.be2ae4feddc10ca089f3d4363040d93b7fd046c8d4f83ba975ec46483ee99895.no.png)

Vi kan bruke en annen formel for å legge sammen alle verdiene i Inventory Value for å få totalverdien. Dette kan beregnes ved å legge til hver celle for å generere summen, men det kan være en tidkrevende oppgave. Excel har [**funksjoner**](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89), eller forhåndsdefinerte formler for å utføre beregninger på celldata. Funksjoner krever argumenter, som er de nødvendige verdiene som brukes til å utføre disse beregningene. Når funksjoner krever mer enn ett argument, må de listes opp i en bestemt rekkefølge, ellers kan funksjonen beregne feil verdi. Dette eksemplet bruker SUM-funksjonen og bruker verdiene i Inventory Value som argument for å generere totalen oppført under rad 3, kolonne B (også referert til som B3).

## NoSQL

NoSQL er en samlebetegnelse for de forskjellige måtene å lagre ikke-relasjonelle data på og kan tolkes som "ikke-SQL", "ikke-relasjonell" eller "ikke bare SQL". Disse typene databasesystemer kan kategoriseres i fire typer.

![Grafisk fremstilling av en nøkkel-verdi-database som viser 4 unike numeriske nøkler som er knyttet til 4 ulike verdier](../../../../translated_images/kv-db.e8f2b75686bbdfcba0c827b9272c10ae0821611ea0fe98429b9d13194383afa6.no.png)
> Kilde fra [Michał Białecki Blog](https://www.michalbialecki.com/2018/03/18/azure-cosmos-db-key-value-database-cloud/)

[Nøkkel-verdi](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#keyvalue-data-stores)-databaser parer unike nøkler, som er en unik identifikator knyttet til en verdi. Disse parene lagres ved hjelp av en [hashtabell](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/) med en passende hashfunksjon.

![Grafisk fremstilling av en grafdatabase som viser forholdet mellom personer, deres interesser og steder](../../../../translated_images/graph-db.d13629152f79a9dac895b20fa7d841d4d4d6f6008b1382227c3bbd200fd4cfa1.no.png)
> Kilde fra [Microsoft](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/graph-introduction#graph-database-by-example)

[Graf](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#graph-data-stores)-databaser beskriver forhold i data og er representert som en samling av noder og kanter. En node representerer en enhet, noe som eksisterer i den virkelige verden, som en student eller en bankutskrift. Kanter representerer forholdet mellom to enheter. Hver node og kant har egenskaper som gir tilleggsinformasjon om hver node og kant.

![Grafisk fremstilling av en kolonnedatabase som viser en kundedatabase med to kolonnefamilier kalt Identity og Contact Info](../../../../translated_images/columnar-db.ffcfe73c3e9063a8c8f93f8ace85e1200863584b1e324eb5159d8ca10f62ec04.no.png)

[Kolonnebaserte](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#columnar-data-stores) databaser organiserer data i kolonner og rader som en relasjonell datastruktur, men hver kolonne er delt inn i grupper kalt kolonnefamilier, der alle dataene under én kolonne er relatert og kan hentes og endres som en enhet.

### Dokumentdatabaser med Azure Cosmos DB

[Dokument](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#document-data-stores)-databaser bygger på konseptet med en nøkkel-verdi-database og består av en serie felt og objekter. Denne delen vil utforske dokumentdatabaser med Cosmos DB-emulatoren.

En Cosmos DB-database passer til definisjonen av "ikke bare SQL", der Cosmos DBs dokumentdatabase er avhengig av SQL for å hente data. [Forrige leksjon](../05-relational-databases/README.md) om SQL dekker det grunnleggende om språket, og vi vil kunne bruke noen av de samme spørringene på en dokumentdatabase her. Vi vil bruke Cosmos DB Emulator, som lar oss opprette og utforske en dokumentdatabase lokalt på en datamaskin. Les mer om emulatoren [her](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21).

Et dokument er en samling av felt og objektverdier, der feltene beskriver hva objektverdien representerer. Nedenfor er et eksempel på et dokument.

```json
{
    "firstname": "Eva",
    "age": 44,
    "id": "8c74a315-aebf-4a16-bb38-2430a9896ce5",
    "_rid": "bHwDAPQz8s0BAAAAAAAAAA==",
    "_self": "dbs/bHwDAA==/colls/bHwDAPQz8s0=/docs/bHwDAPQz8s0BAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f95-010a691e01d7\"",
    "_attachments": "attachments/",
    "_ts": 1630544034
}
```

Feltene av interesse i dette dokumentet er: `firstname`, `id` og `age`. Resten av feltene med understreker ble generert av Cosmos DB.

#### Utforske data med Cosmos DB Emulator

Du kan laste ned og installere emulatoren [for Windows her](https://aka.ms/cosmosdb-emulator). Se denne [dokumentasjonen](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos) for alternativer for hvordan du kjører emulatoren for macOS og Linux.

Emulatoren åpner et nettleservindu, der Explorer-visningen lar deg utforske dokumenter.

![Explorer-visningen i Cosmos DB Emulator](../../../../translated_images/cosmosdb-emulator-explorer.a1c80b1347206fe2f30f88fc123821636587d04fc5a56a9eb350c7da6b31f361.no.png)

Hvis du følger med, klikk på "Start with Sample" for å generere en eksempel-database kalt SampleDB. Hvis du utvider SampleDB ved å klikke på pilen, finner du en beholder kalt `Persons`. En beholder holder en samling av elementer, som er dokumentene i beholderen. Du kan utforske de fire individuelle dokumentene under `Items`.

![Utforske eksempeldata i Cosmos DB Emulator](../../../../translated_images/cosmosdb-emulator-persons.bf640586a7077c8985dfd3071946465c8e074c722c7c202d6d714de99a93b90a.no.png)

#### Spørring av dokumentdata med Cosmos DB Emulator

Vi kan også spørring på eksempeldataene ved å klikke på knappen for ny SQL-spørring (andre knapp fra venstre).

`SELECT * FROM c` returnerer alle dokumentene i beholderen. La oss legge til en where-setning og finne alle som er yngre enn 40.

`SELECT * FROM c where c.age < 40`

![Kjøre en SELECT-spørring på eksempeldata i Cosmos DB Emulator for å finne dokumenter som har en alder-verdi mindre enn 40](../../../../translated_images/cosmosdb-emulator-persons-query.6905ebb497e3cd047cd96e55a0a03f69ce1b91b2b3d8c147e617b746b22b7e33.no.png)

Spørringen returnerer to dokumenter. Legg merke til at alder-verdien for hvert dokument er mindre enn 40.

#### JSON og dokumenter

Hvis du er kjent med JavaScript Object Notation (JSON), vil du legge merke til at dokumenter ligner på JSON. Det finnes en `PersonsData.json`-fil i denne katalogen med flere data som du kan laste opp til Persons-beholderen i emulatoren via `Upload Item`-knappen.

I de fleste tilfeller kan API-er som returnerer JSON-data direkte overføres og lagres i dokumentdatabaser. Nedenfor er et annet dokument som representerer tweets fra Microsofts Twitter-konto, hentet ved hjelp av Twitter API og deretter satt inn i Cosmos DB.

```json
{
    "created_at": "2021-08-31T19:03:01.000Z",
    "id": "1432780985872142341",
    "text": "Blank slate. Like this tweet if you’ve ever painted in Microsoft Paint before. https://t.co/cFeEs8eOPK",
    "_rid": "dhAmAIUsA4oHAAAAAAAAAA==",
    "_self": "dbs/dhAmAA==/colls/dhAmAIUsA4o=/docs/dhAmAIUsA4oHAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f84-a0958ad901d7\"",
    "_attachments": "attachments/",
    "_ts": 1630537000
```

Feltene av interesse i dette dokumentet er: `created_at`, `id` og `text`.

## 🚀 Utfordring

Det finnes en `TwitterData.json`-fil som du kan laste opp til SampleDB-databasen. Det anbefales at du legger den til i en separat beholder. Dette kan gjøres ved å:

1. Klikke på knappen for ny beholder øverst til høyre
1. Velge den eksisterende databasen (SampleDB) og opprette en beholder-ID for beholderen
1. Sette partisjonsnøkkelen til `/id`
1. Klikke OK (du kan ignorere resten av informasjonen i denne visningen siden dette er et lite datasett som kjører lokalt på maskinen din)
1. Åpne den nye beholderen din og laste opp TwitterData-filen med `Upload Item`-knappen

Prøv å kjøre noen SELECT-spørringer for å finne dokumentene som har Microsoft i tekstfeltet. Tips: prøv å bruke [LIKE-nøkkelordet](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character).

## [Quiz etter forelesning](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/11)

## Gjennomgang og selvstudium

- Det er noen ekstra formateringer og funksjoner lagt til i dette regnearket som ikke dekkes i denne leksjonen. Microsoft har et [stort bibliotek med dokumentasjon og videoer](https://support.microsoft.com/excel) om Excel hvis du er interessert i å lære mer.

- Denne arkitekturdokumentasjonen beskriver egenskapene til de forskjellige typene ikke-relasjonelle data: [Ikke-relasjonelle data og NoSQL](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data).

- Cosmos DB er en skybasert ikke-relasjonell database som også kan lagre de forskjellige NoSQL-typene nevnt i denne leksjonen. Lær mer om disse typene i dette [Cosmos DB Microsoft Learn-modulet](https://docs.microsoft.com/en-us/learn/paths/work-with-nosql-data-in-azure-cosmos-db/).

## Oppgave

[Soda Profits](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.