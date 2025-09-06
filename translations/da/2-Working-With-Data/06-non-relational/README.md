<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c182e87f9f80be7e7cdffc7b40bbfccf",
  "translation_date": "2025-09-05T21:57:30+00:00",
  "source_file": "2-Working-With-Data/06-non-relational/README.md",
  "language_code": "da"
}
-->
# Arbejde med data: Ikke-relationelle data

|![ Sketchnote af [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/06-NoSQL.png)|
|:---:|
|Arbejde med NoSQL-data - _Sketchnote af [@nitya](https://twitter.com/nitya)_ |

## [Quiz før lektionen](https://ff-quizzes.netlify.app/en/ds/quiz/10)

Data er ikke begrænset til relationelle databaser. Denne lektion fokuserer på ikke-relationelle data og vil dække grundlæggende om regneark og NoSQL.

## Regneark

Regneark er en populær måde at gemme og udforske data på, fordi det kræver mindre arbejde at opsætte og komme i gang. I denne lektion vil du lære de grundlæggende komponenter i et regneark, samt formler og funktioner. Eksemplerne vil blive illustreret med Microsoft Excel, men de fleste dele og emner vil have lignende navne og trin i forhold til andre regnearksprogrammer.

![Et tomt Microsoft Excel-arbejdsark med to regneark](../../../../2-Working-With-Data/06-non-relational/images/parts-of-spreadsheet.png)

Et regneark er en fil og vil være tilgængelig i filsystemet på en computer, enhed eller skybaseret filsystem. Selve softwaren kan være browserbaseret eller en applikation, der skal installeres på en computer eller downloades som en app. I Excel defineres disse filer også som **arbejdsbøger**, og denne terminologi vil blive brugt resten af lektionen.

En arbejdsbog indeholder et eller flere **regneark**, hvor hvert regneark er mærket med faner. Inden for et regneark er der rektangler kaldet **celler**, som indeholder de faktiske data. En celle er skæringspunktet mellem en række og en kolonne, hvor kolonnerne er mærket med alfabetiske tegn og rækkerne numerisk. Nogle regneark vil indeholde overskrifter i de første par rækker for at beskrive dataene i en celle.

Med disse grundlæggende elementer i en Excel-arbejdsbog vil vi bruge et eksempel fra [Microsoft Templates](https://templates.office.com/) med fokus på et lager for at gennemgå nogle yderligere dele af et regneark.

### Håndtering af et lager

Regnearksfilen kaldet "InventoryExample" er et formateret regneark med varer i et lager, der indeholder tre regneark, hvor fanerne er mærket "Inventory List", "Inventory Pick List" og "Bin Lookup". Række 4 i regnearket Inventory List er overskriften, som beskriver værdien af hver celle i overskriftskolonnen.

![En fremhævet formel fra et eksempel på lagerliste i Microsoft Excel](../../../../2-Working-With-Data/06-non-relational/images/formula-excel.png)

Der er tilfælde, hvor en celle er afhængig af værdierne i andre celler for at generere sin værdi. Lagerlisten holder styr på omkostningerne for hver vare i lageret, men hvad hvis vi skal kende værdien af alt i lageret? [**Formler**](https://support.microsoft.com/en-us/office/overview-of-formulas-34519a4e-1e8d-4f4b-84d4-d642c4f63263) udfører handlinger på celldata og bruges til at beregne lagerets værdi i dette eksempel. Dette regneark brugte en formel i kolonnen Inventory Value til at beregne værdien af hver vare ved at multiplicere mængden under overskriften QTY og dens omkostninger under overskriften COST. Dobbeltklik eller fremhæv en celle for at se formlen. Du vil bemærke, at formler starter med et lighedstegn, efterfulgt af beregningen eller operationen.

![En fremhævet funktion fra et eksempel på lagerliste i Microsoft Excel](../../../../2-Working-With-Data/06-non-relational/images/function-excel.png)

Vi kan bruge en anden formel til at lægge alle værdierne i Inventory Value sammen for at få den samlede værdi. Dette kunne beregnes ved at tilføje hver celle for at generere summen, men det kan være en tidskrævende opgave. Excel har [**funktioner**](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89), eller foruddefinerede formler til at udføre beregninger på celldata. Funktioner kræver argumenter, som er de nødvendige værdier, der bruges til at udføre disse beregninger. Når funktioner kræver mere end ét argument, skal de angives i en bestemt rækkefølge, ellers beregner funktionen muligvis ikke den korrekte værdi. Dette eksempel bruger SUM-funktionen og bruger værdierne i Inventory Value som argumentet for at generere summen, der er angivet under række 3, kolonne B (også kaldet B3).

## NoSQL

NoSQL er en paraplybetegnelse for de forskellige måder at gemme ikke-relationelle data på og kan tolkes som "non-SQL", "non-relational" eller "not only SQL". Disse typer databasesystemer kan kategoriseres i 4 typer.

![Grafisk repræsentation af en nøgle-værdi-datastore, der viser 4 unikke numeriske nøgler, der er knyttet til 4 forskellige værdier](../../../../2-Working-With-Data/06-non-relational/images/kv-db.png)
> Kilde fra [Michał Białecki Blog](https://www.michalbialecki.com/2018/03/18/azure-cosmos-db-key-value-database-cloud/)

[Nøgle-værdi](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#keyvalue-data-stores) databaser parrer unikke nøgler, som er en unik identifikator knyttet til en værdi. Disse par gemmes ved hjælp af en [hash-tabel](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/) med en passende hash-funktion.

![Grafisk repræsentation af en graf-datastore, der viser relationerne mellem personer, deres interesser og lokationer](../../../../2-Working-With-Data/06-non-relational/images/graph-db.png)
> Kilde fra [Microsoft](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/graph-introduction#graph-database-by-example)

[Graf](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#graph-data-stores) databaser beskriver relationer i data og er repræsenteret som en samling af noder og kanter. En node repræsenterer en enhed, noget der eksisterer i den virkelige verden, såsom en studerende eller en bankudskrift. Kanter repræsenterer relationen mellem to enheder. Hver node og kant har egenskaber, der giver yderligere information om hver node og kant.

![Grafisk repræsentation af en kolonnær-datastore, der viser en kundedatabase med to kolonnefamilier kaldet Identity og Contact Info](../../../../2-Working-With-Data/06-non-relational/images/columnar-db.png)

[Kolonnær](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#columnar-data-stores) datastores organiserer data i kolonner og rækker som en relationel datastruktur, men hver kolonne er opdelt i grupper kaldet en kolonnefamilie, hvor alle data under én kolonne er relaterede og kan hentes og ændres som en enhed.

### Dokumentdatastores med Azure Cosmos DB

[Dokument](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#document-data-stores) datastores bygger på konceptet med en nøgle-værdi-datastore og består af en række felter og objekter. Denne sektion vil udforske dokumentdatabaser med Cosmos DB-emulatoren.

En Cosmos DB-database passer til definitionen af "Not Only SQL", hvor Cosmos DB's dokumentdatabase bruger SQL til at forespørge data. [Den tidligere lektion](../05-relational-databases/README.md) om SQL dækker grundlæggende om sproget, og vi vil kunne anvende nogle af de samme forespørgsler på en dokumentdatabase her. Vi vil bruge Cosmos DB Emulator, som giver os mulighed for at oprette og udforske en dokumentdatabase lokalt på en computer. Læs mere om Emulatoren [her](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21).

Et dokument er en samling af felter og objektværdier, hvor felterne beskriver, hvad objektværdien repræsenterer. Nedenfor er et eksempel på et dokument.

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

De interessante felter i dette dokument er: `firstname`, `id` og `age`. Resten af felterne med understregninger blev genereret af Cosmos DB.

#### Udforskning af data med Cosmos DB Emulator

Du kan downloade og installere emulatoren [til Windows her](https://aka.ms/cosmosdb-emulator). Se denne [dokumentation](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos) for muligheder for at køre Emulatoren på macOS og Linux.

Emulatoren åbner et browservindue, hvor Explorer-visningen giver dig mulighed for at udforske dokumenter.

![Explorer-visningen af Cosmos DB Emulator](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-explorer.png)

Hvis du følger med, skal du klikke på "Start with Sample" for at generere en prøvedatabase kaldet SampleDB. Hvis du udvider SampleDB ved at klikke på pilen, finder du en container kaldet `Persons`. En container indeholder en samling af elementer, som er dokumenterne inden for containeren. Du kan udforske de fire individuelle dokumenter under `Items`.

![Udforskning af prøvedata i Cosmos DB Emulator](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons.png)

#### Forespørgsel på dokumentdata med Cosmos DB Emulator

Vi kan også forespørge prøvedataene ved at klikke på knappen "New SQL Query" (anden knap fra venstre).

`SELECT * FROM c` returnerer alle dokumenterne i containeren. Lad os tilføje en where-klausul og finde alle, der er yngre end 40.

`SELECT * FROM c where c.age < 40`

![Kørsel af en SELECT-forespørgsel på prøvedata i Cosmos DB Emulator for at finde dokumenter, der har en age-feltværdi mindre end 40](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons-query.png)

Forespørgslen returnerer to dokumenter, bemærk aldersværdien for hvert dokument er mindre end 40.

#### JSON og dokumenter

Hvis du er bekendt med JavaScript Object Notation (JSON), vil du bemærke, at dokumenter ligner JSON. Der er en `PersonsData.json`-fil i denne mappe med flere data, som du kan uploade til Persons-containeren i Emulatoren via knappen `Upload Item`.

I de fleste tilfælde kan API'er, der returnerer JSON-data, direkte overføres og gemmes i dokumentdatabaser. Nedenfor er et andet dokument, det repræsenterer tweets fra Microsofts Twitter-konto, der blev hentet ved hjælp af Twitter API og derefter indsat i Cosmos DB.

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

De interessante felter i dette dokument er: `created_at`, `id` og `text`.

## 🚀 Udfordring

Der er en `TwitterData.json`-fil, som du kan uploade til SampleDB-databasen. Det anbefales, at du tilføjer den til en separat container. Dette kan gøres ved:

1. Klikke på knappen "New Container" øverst til højre
1. Vælge den eksisterende database (SampleDB) og oprette et container-id for containeren
1. Indstille partitionsnøglen til `/id`
1. Klikke på OK (du kan ignorere resten af informationen i denne visning, da dette er et lille datasæt, der kører lokalt på din maskine)
1. Åbne din nye container og uploade Twitter Data-filen med knappen `Upload Item`

Prøv at køre nogle SELECT-forespørgsler for at finde dokumenterne, der har Microsoft i tekstfeltet. Tip: prøv at bruge [LIKE nøgleordet](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character)

## [Quiz efter lektionen](https://ff-quizzes.netlify.app/en/ds/quiz/11)

## Gennemgang & Selvstudie

- Der er nogle yderligere formateringsmuligheder og funktioner tilføjet til dette regneark, som denne lektion ikke dækker. Microsoft har et [stort bibliotek af dokumentation og videoer](https://support.microsoft.com/excel) om Excel, hvis du er interesseret i at lære mere.

- Denne arkitekturdokumentation beskriver egenskaberne ved de forskellige typer ikke-relationelle data: [Ikke-relationelle data og NoSQL](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data)

- Cosmos DB er en skybaseret ikke-relationel database, der også kan gemme de forskellige NoSQL-typer nævnt i denne lektion. Lær mere om disse typer i dette [Cosmos DB Microsoft Learn Module](https://docs.microsoft.com/en-us/learn/paths/work-with-nosql-data-in-azure-cosmos-db/)

## Opgave

[Soda Profits](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.