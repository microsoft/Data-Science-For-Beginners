<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T11:33:15+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "da"
}
-->
# Arbejde med data: Relationelle databaser

|![ Sketchnote af [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Arbejde med data: Relationelle databaser - _Sketchnote af [@nitya](https://twitter.com/nitya)_ |

Chancerne er, at du tidligere har brugt et regneark til at gemme information. Du havde et sæt rækker og kolonner, hvor rækkerne indeholdt informationen (eller data), og kolonnerne beskrev informationen (nogle gange kaldet metadata). En relationel database er bygget på dette kerneprincip om kolonner og rækker i tabeller, hvilket giver dig mulighed for at have information spredt over flere tabeller. Dette giver dig mulighed for at arbejde med mere komplekse data, undgå duplikering og have fleksibilitet i den måde, du udforsker dataene på. Lad os udforske begreberne i en relationel database.

## [For-forelæsning quiz](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Det hele starter med tabeller

En relationel database har tabeller som sin kerne. Ligesom med regnearket er en tabel en samling af kolonner og rækker. Rækken indeholder de data eller oplysninger, vi ønsker at arbejde med, såsom navnet på en by eller mængden af nedbør. Kolonnerne beskriver de data, de gemmer.

Lad os begynde vores udforskning ved at starte en tabel til at gemme information om byer. Vi kunne starte med deres navn og land. Du kunne gemme dette i en tabel som følger:

| By       | Land          |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | USA           |
| Auckland | New Zealand   |

Bemærk kolonnenavnene **By**, **Land** og **Befolkning** beskriver de data, der gemmes, og hver række har information om én by.

## Ulemperne ved en enkelt tabel tilgang

Chancerne er, at tabellen ovenfor virker relativt velkendt for dig. Lad os begynde at tilføje nogle yderligere data til vores voksende database - årlig nedbør (i millimeter). Vi vil fokusere på årene 2018, 2019 og 2020. Hvis vi skulle tilføje det for Tokyo, kunne det se sådan ud:

| By    | Land  | År   | Mængde |
| ----- | ----- | ---- | ------ |
| Tokyo | Japan | 2020 | 1690   |
| Tokyo | Japan | 2019 | 1874   |
| Tokyo | Japan | 2018 | 1445   |

Hvad bemærker du ved vores tabel? Du vil måske bemærke, at vi gentager navnet og landet på byen igen og igen. Det kan optage en del lagerplads og er stort set unødvendigt at have flere kopier af. Tokyo har trods alt kun ét navn, vi er interesserede i.

OK, lad os prøve noget andet. Lad os tilføje nye kolonner for hvert år:

| By       | Land          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | USA           | 1779 | 1111 | 1683 |
| Auckland | New Zealand   | 1386 | 942  | 1176 |

Selvom dette undgår gentagelse af rækker, tilføjer det et par andre udfordringer. Vi ville skulle ændre strukturen af vores tabel hver gang, der kommer et nyt år. Derudover, efterhånden som vores data vokser, vil det gøre det sværere at hente og beregne værdier, når vores år er kolonner.

Derfor har vi brug for flere tabeller og relationer. Ved at opdele vores data kan vi undgå duplikering og have mere fleksibilitet i, hvordan vi arbejder med vores data.

## Begreberne om relationer

Lad os vende tilbage til vores data og afgøre, hvordan vi vil opdele tingene. Vi ved, at vi vil gemme navn og land for vores byer, så det vil sandsynligvis fungere bedst i én tabel.

| By       | Land          |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | USA           |
| Auckland | New Zealand   |

Men før vi opretter den næste tabel, skal vi finde ud af, hvordan vi refererer til hver by. Vi har brug for en form for identifikator, ID eller (i tekniske databaser termer) en primær nøgle. En primær nøgle er en værdi, der bruges til at identificere en specifik række i en tabel. Selvom dette kunne baseres på en værdi i sig selv (vi kunne for eksempel bruge byens navn), bør det næsten altid være et nummer eller en anden identifikator. Vi ønsker ikke, at id nogensinde ændres, da det ville bryde relationen. Du vil i de fleste tilfælde finde, at den primære nøgle eller id er et automatisk genereret nummer.

> ✅ Primær nøgle forkortes ofte som PK

### byer

| city_id | By       | Land          |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japan         |
| 2       | Atlanta  | USA           |
| 3       | Auckland | New Zealand   |

> ✅ Du vil bemærke, at vi bruger termerne "id" og "primær nøgle" om hinanden i denne lektion. Begreberne her gælder også for DataFrames, som du vil udforske senere. DataFrames bruger ikke terminologien "primær nøgle", men du vil bemærke, at de opfører sig på samme måde.

Med vores byer-tabel oprettet, lad os gemme nedbøren. I stedet for at duplikere den fulde information om byen, kan vi bruge id'et. Vi bør også sikre, at den nyligt oprettede tabel også har en *id*-kolonne, da alle tabeller bør have en id eller primær nøgle.

### nedbør

| rainfall_id | city_id | År   | Mængde |
| ----------- | ------- | ---- | ------ |
| 1           | 1       | 2018 | 1445   |
| 2           | 1       | 2019 | 1874   |
| 3           | 1       | 2020 | 1690   |
| 4           | 2       | 2018 | 1779   |
| 5           | 2       | 2019 | 1111   |
| 6           | 2       | 2020 | 1683   |
| 7           | 3       | 2018 | 1386   |
| 8           | 3       | 2019 | 942    |
| 9           | 3       | 2020 | 1176   |

Bemærk kolonnen **city_id** i den nyligt oprettede **nedbør**-tabel. Denne kolonne indeholder værdier, som refererer til ID'erne i **byer**-tabellen. I tekniske relationelle datatermer kaldes dette en **fremmed nøgle**; det er en primær nøgle fra en anden tabel. Du kan bare tænke på det som en reference eller en pegepind. **city_id** 1 refererer til Tokyo.

> [!NOTE] 
> Fremmed nøgle forkortes ofte som FK

## Hentning af data

Med vores data opdelt i to tabeller, spekulerer du måske på, hvordan vi henter det. Hvis vi bruger en relationel database som MySQL, SQL Server eller Oracle, kan vi bruge et sprog kaldet Structured Query Language eller SQL. SQL (nogle gange udtalt sequel) er et standardsprog, der bruges til at hente og ændre data i en relationel database.

For at hente data bruger du kommandoen `SELECT`. Grundlæggende **vælger** du de kolonner, du vil se, **fra** den tabel, de er indeholdt i. Hvis du kun ville vise navnene på byerne, kunne du bruge følgende:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` er hvor du lister kolonnerne, og `FROM` er hvor du lister tabellerne.

> [!NOTE] 
> SQL-syntaks er ikke-følsom over for store og små bogstaver, hvilket betyder, at `select` og `SELECT` betyder det samme. Afhængigt af hvilken type database du bruger, kan kolonner og tabeller dog være store- og småbogstavsfølsomme. Derfor er det en god praksis altid at behandle alt i programmering som om det er store- og småbogstavsfølsomt. Når du skriver SQL-forespørgsler, er det almindelig konvention at skrive nøgleordene med store bogstaver.

Forespørgslen ovenfor vil vise alle byer. Lad os forestille os, at vi kun ville vise byer i New Zealand. Vi har brug for en form for filter. SQL-nøgleordet for dette er `WHERE`, eller "hvor noget er sandt".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Sammenkædning af data

Indtil nu har vi hentet data fra en enkelt tabel. Nu vil vi samle dataene fra både **byer** og **nedbør**. Dette gøres ved at *sammenkæde* dem. Du vil effektivt skabe en søm mellem de to tabeller og matche værdierne fra en kolonne i hver tabel.

I vores eksempel vil vi matche kolonnen **city_id** i **nedbør** med kolonnen **city_id** i **byer**. Dette vil matche nedbørsværdien med dens respektive by. Den type sammenkædning, vi vil udføre, kaldes en *inner* join, hvilket betyder, at hvis nogen rækker ikke matcher noget fra den anden tabel, vil de ikke blive vist. I vores tilfælde har hver by nedbør, så alt vil blive vist.

Lad os hente nedbøren for 2019 for alle vores byer.

Vi vil gøre dette i trin. Det første trin er at sammenkæde dataene ved at angive kolonnerne for sømmen - **city_id** som fremhævet før.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Vi har fremhævet de to kolonner, vi ønsker, og det faktum, at vi vil sammenkæde tabellerne ved **city_id**. Nu kan vi tilføje `WHERE`-sætningen for kun at filtrere på år 2019.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
WHERE rainfall.year = 2019

-- Output

-- city     | amount
-- -------- | ------
-- Tokyo    | 1874
-- Atlanta  | 1111
-- Auckland |  942
```

## Resumé

Relationelle databaser er centreret omkring at opdele information mellem flere tabeller, som derefter bringes sammen igen til visning og analyse. Dette giver en høj grad af fleksibilitet til at udføre beregninger og på anden måde manipulere data. Du har set kernebegreberne i en relationel database, og hvordan man udfører en sammenkædning mellem to tabeller.

## 🚀 Udfordring

Der findes mange relationelle databaser tilgængelige på internettet. Du kan udforske dataene ved at bruge de færdigheder, du har lært ovenfor.

## Post-forelæsning quiz

## [Post-forelæsning quiz](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Gennemgang & Selvstudie

Der findes flere ressourcer på [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum), hvor du kan fortsætte din udforskning af SQL og relationelle databasebegreber

- [Beskriv begreber om relationelle data](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Kom godt i gang med forespørgsler med Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL er en version af SQL)
- [SQL-indhold på Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Opgave

[Visning af lufthavnsdata](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->