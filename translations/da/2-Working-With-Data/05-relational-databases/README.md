<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11b166fbcb7eaf82308cdc24b562f687",
  "translation_date": "2025-09-04T19:12:37+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "da"
}
-->
# Arbejde med data: Relationelle databaser

|![ Sketchnote af [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Arbejde med data: Relationelle databaser - _Sketchnote af [@nitya](https://twitter.com/nitya)_ |

Chancerne er, at du tidligere har brugt et regneark til at gemme information. Du havde et sæt rækker og kolonner, hvor rækkerne indeholdt informationen (eller data), og kolonnerne beskrev informationen (nogle gange kaldet metadata). En relationel database er bygget på dette grundprincip med kolonner og rækker i tabeller, hvilket giver dig mulighed for at sprede informationen over flere tabeller. Dette gør det muligt at arbejde med mere komplekse data, undgå duplikering og få fleksibilitet i måden, du udforsker dataene på. Lad os udforske begreberne i en relationel database.

## [Quiz før forelæsning](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Det hele starter med tabeller

En relationel database har tabeller som sin kerne. Ligesom med regnearket er en tabel en samling af kolonner og rækker. Rækkerne indeholder de data eller den information, vi ønsker at arbejde med, såsom navnet på en by eller mængden af nedbør. Kolonnerne beskriver de data, de gemmer.

Lad os begynde vores udforskning ved at oprette en tabel til at gemme information om byer. Vi kunne starte med deres navn og land. Du kunne gemme dette i en tabel som følgende:

| By       | Land          |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | USA           |
| Auckland | New Zealand   |

Bemærk, at kolonnenavnene **by**, **land** og **befolkning** beskriver de data, der gemmes, og hver række har information om én by.

## Begrænsninger ved en enkelt tabeltilgang

Chancerne er, at tabellen ovenfor virker relativt bekendt for dig. Lad os begynde at tilføje nogle yderligere data til vores spirende database - årlig nedbør (i millimeter). Vi fokuserer på årene 2018, 2019 og 2020. Hvis vi skulle tilføje det for Tokyo, kunne det se sådan ud:

| By    | Land    | År   | Mængde |
| ----- | ------- | ---- | ------ |
| Tokyo | Japan   | 2020 | 1690   |
| Tokyo | Japan   | 2019 | 1874   |
| Tokyo | Japan   | 2018 | 1445   |

Hvad bemærker du ved vores tabel? Du bemærker måske, at vi gentager navnet og landet for byen igen og igen. Det kunne tage en del lagerplads og er stort set unødvendigt at have flere kopier af. Tokyo har trods alt kun ét navn, vi er interesserede i.

OK, lad os prøve noget andet. Lad os tilføje nye kolonner for hvert år:

| By       | Land          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | USA           | 1779 | 1111 | 1683 |
| Auckland | New Zealand   | 1386 | 942  | 1176 |

Selvom dette undgår rækkeduplikering, tilføjer det et par andre udfordringer. Vi ville skulle ændre strukturen af vores tabel hver gang, der kommer et nyt år. Derudover vil det, efterhånden som vores data vokser, gøre det mere besværligt at hente og beregne værdier, hvis vores år er kolonner.

Dette er grunden til, at vi har brug for flere tabeller og relationer. Ved at opdele vores data kan vi undgå duplikering og få mere fleksibilitet i, hvordan vi arbejder med vores data.

## Begreberne bag relationer

Lad os vende tilbage til vores data og bestemme, hvordan vi vil opdele dem. Vi ved, at vi vil gemme navnet og landet for vores byer, så dette vil sandsynligvis fungere bedst i én tabel.

| By       | Land          |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | USA           |
| Auckland | New Zealand   |

Men før vi opretter den næste tabel, skal vi finde ud af, hvordan vi refererer til hver by. Vi har brug for en form for identifikator, ID eller (i tekniske database-termer) en primær nøgle. En primær nøgle er en værdi, der bruges til at identificere én specifik række i en tabel. Selvom dette kunne være baseret på en værdi i sig selv (vi kunne for eksempel bruge navnet på byen), bør det næsten altid være et nummer eller en anden identifikator. Vi ønsker ikke, at ID'et nogensinde ændrer sig, da det ville bryde relationen. Du vil finde, at i de fleste tilfælde vil den primære nøgle eller ID være et automatisk genereret nummer.

> ✅ Primær nøgle forkortes ofte som PK

### byer

| by_id | By       | Land          |
| ----- | -------- | ------------- |
| 1     | Tokyo    | Japan         |
| 2     | Atlanta  | USA           |
| 3     | Auckland | New Zealand   |

> ✅ Du vil bemærke, at vi bruger begreberne "id" og "primær nøgle" i flæng under denne lektion. Begreberne her gælder for DataFrames, som du vil udforske senere. DataFrames bruger ikke terminologien "primær nøgle", men du vil bemærke, at de opfører sig på samme måde.

Med vores byer-tabel oprettet, lad os gemme nedbøren. I stedet for at duplikere den fulde information om byen, kan vi bruge ID'et. Vi bør også sikre, at den nyoprettede tabel har en *id*-kolonne, da alle tabeller bør have et ID eller en primær nøgle.

### nedbør

| nedbør_id | by_id | År   | Mængde |
| --------- | ----- | ---- | ------ |
| 1         | 1     | 2018 | 1445   |
| 2         | 1     | 2019 | 1874   |
| 3         | 1     | 2020 | 1690   |
| 4         | 2     | 2018 | 1779   |
| 5         | 2     | 2019 | 1111   |
| 6         | 2     | 2020 | 1683   |
| 7         | 3     | 2018 | 1386   |
| 8         | 3     | 2019 | 942    |
| 9         | 3     | 2020 | 1176   |

Bemærk kolonnen **by_id** i den nyoprettede **nedbør**-tabel. Denne kolonne indeholder værdier, der refererer til ID'erne i **byer**-tabellen. I tekniske relationelle datatermer kaldes dette en **fremmed nøgle**; det er en primær nøgle fra en anden tabel. Du kan bare tænke på det som en reference eller en pegepind. **by_id** 1 refererer til Tokyo.

> [!NOTE] Fremmed nøgle forkortes ofte som FK

## Hente data

Med vores data opdelt i to tabeller, undrer du dig måske over, hvordan vi henter dem. Hvis vi bruger en relationel database som MySQL, SQL Server eller Oracle, kan vi bruge et sprog kaldet Structured Query Language eller SQL. SQL (nogle gange udtalt "sequel") er et standardiseret sprog, der bruges til at hente og ændre data i en relationel database.

For at hente data bruger du kommandoen `SELECT`. I sin kerne **vælger** du de kolonner, du vil se **fra** den tabel, de er indeholdt i. Hvis du ville vise kun navnene på byerne, kunne du bruge følgende:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` er hvor du lister kolonnerne, og `FROM` er hvor du lister tabellerne.

> [NOTE] SQL-syntaks er ikke case-sensitive, hvilket betyder, at `select` og `SELECT` betyder det samme. Dog kan kolonner og tabeller afhængigt af typen af database være case-sensitive. Derfor er det en god praksis altid at behandle alt i programmering som case-sensitive. Når du skriver SQL-forespørgsler, er det almindelig konvention at skrive nøgleordene med store bogstaver.

Forespørgslen ovenfor vil vise alle byer. Lad os forestille os, at vi kun ville vise byer i New Zealand. Vi har brug for en form for filter. SQL-nøgleordet for dette er `WHERE`, eller "hvor noget er sandt".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Sammenkædning af data

Indtil nu har vi hentet data fra en enkelt tabel. Nu vil vi samle dataene fra både **byer** og **nedbør**. Dette gøres ved at *sammenkæde* dem. Du vil effektivt skabe en forbindelse mellem de to tabeller og matche værdierne fra en kolonne fra hver tabel.

I vores eksempel vil vi matche kolonnen **by_id** i **nedbør** med kolonnen **by_id** i **byer**. Dette vil matche nedbørsværdien med dens respektive by. Den type sammenkædning, vi vil udføre, kaldes en *inner join*, hvilket betyder, at hvis nogen rækker ikke matcher med noget fra den anden tabel, vil de ikke blive vist. I vores tilfælde har hver by nedbør, så alt vil blive vist.

Lad os hente nedbøren for 2019 for alle vores byer.

Vi vil gøre dette i trin. Det første trin er at sammenkæde dataene ved at angive kolonnerne for forbindelsen - **by_id**, som fremhævet før.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Vi har fremhævet de to kolonner, vi ønsker, og det faktum, at vi vil sammenkæde tabellerne ved **by_id**. Nu kan vi tilføje `WHERE`-sætningen for kun at filtrere år 2019.

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

## Opsummering

Relationelle databaser er centreret omkring at opdele information mellem flere tabeller, som derefter samles igen til visning og analyse. Dette giver en høj grad af fleksibilitet til at udføre beregninger og på anden måde manipulere data. Du har set de grundlæggende begreber i en relationel database og hvordan man udfører en sammenkædning mellem to tabeller.

## 🚀 Udfordring

Der findes adskillige relationelle databaser på internettet. Du kan udforske dataene ved at bruge de færdigheder, du har lært ovenfor.

## Quiz efter forelæsning

## [Quiz efter forelæsning](https://ff-quizzes.netlify.app/en/ds/)

## Gennemgang & Selvstudie

Der er flere ressourcer tilgængelige på [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum), som du kan bruge til at fortsætte din udforskning af SQL og relationelle databasebegreber.

- [Beskriv begreberne bag relationelle data](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Kom i gang med forespørgsler i Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL er en version af SQL)
- [SQL-indhold på Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Opgave

[Opgavetitel](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.