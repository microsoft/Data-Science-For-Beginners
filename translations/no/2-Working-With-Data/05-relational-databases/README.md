<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T11:35:58+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "no"
}
-->
# Arbeide med data: Relasjonsdatabaser

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Arbeide med data: Relasjonsdatabaser - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

Sannsynligvis har du brukt et regneark tidligere for å lagre informasjon. Du hadde et sett med rader og kolonner, hvor radene inneholdt informasjonen (eller data), og kolonnene beskrev informasjonen (noen ganger kalt metadata). En relasjonsdatabase er bygget på dette kjerneprinsippet med kolonner og rader i tabeller, som lar deg ha informasjon spredt over flere tabeller. Dette gjør at du kan arbeide med mer kompleks data, unngå duplisering, og ha fleksibilitet i måten du utforsker dataene på. La oss utforske konseptene i en relasjonsdatabase.

## [For-forelesningsquiz](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Alt starter med tabeller

En relasjonsdatabase har i kjernen tabeller. Akkurat som med regnearket, er en tabell en samling av kolonner og rader. Raden inneholder dataene eller informasjonen vi ønsker å arbeide med, som for eksempel navnet på en by eller mengden nedbør. Kolonnene beskriver dataene de lagrer.

La oss begynne vår utforskning ved å starte en tabell for å lagre informasjon om byer. Vi kan begynne med navn og land. Du kan lagre dette i en tabell som følger:

| By       | Land          |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | USA           |
| Auckland | New Zealand   |

Legg merke til kolonnenavnene **By**, **Land** og **befolkning** som beskriver dataene som lagres, og hver rad har informasjon om én by.

## Begrensningene ved en enkelt tabell-tilnærming

Sannsynligvis virker tabellen over relativt kjent for deg. La oss begynne å legge til noen ekstra data til vår voksende database - årlig nedbør (i millimeter). Vi fokuserer på årene 2018, 2019 og 2020. Hvis vi skulle legge det til for Tokyo, kan det se slik ut:

| By    | Land  | År   | Mengde |
| ----- | ----- | ---- | ------ |
| Tokyo | Japan | 2020 | 1690   |
| Tokyo | Japan | 2019 | 1874   |
| Tokyo | Japan | 2018 | 1445   |

Hva legger du merke til med tabellen vår? Du vil kanskje legge merke til at vi dupliserer navnet og landet til byen om og om igjen. Det kan ta opp ganske mye lagringsplass, og det er stort sett unødvendig å ha flere kopier av det. Tross alt har Tokyo bare ett navn vi er interessert i.

OK, la oss prøve noe annet. La oss legge til nye kolonner for hvert år:

| By       | Land          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | USA           | 1779 | 1111 | 1683 |
| Auckland | New Zealand   | 1386 | 942  | 1176 |

Selv om dette unngår duplisering av rader, legger det til noen andre utfordringer. Vi må endre strukturen på tabellen hver gang det kommer et nytt år. I tillegg, når dataene våre vokser, vil det å ha årene som kolonner gjøre det vanskeligere å hente ut og beregne verdier.

Derfor trenger vi flere tabeller og relasjoner. Ved å dele opp dataene kan vi unngå duplisering og ha mer fleksibilitet i hvordan vi arbeider med dataene.

## Konseptene bak relasjoner

La oss gå tilbake til dataene våre og bestemme hvordan vi vil dele opp ting. Vi vet at vi vil lagre navn og land for byene våre, så dette vil sannsynligvis fungere best i én tabell.

| By       | Land          |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | USA           |
| Auckland | New Zealand   |

Men før vi lager neste tabell, må vi finne ut hvordan vi skal referere til hver by. Vi trenger en form for identifikator, ID eller (i tekniske databasertermer) en primærnøkkel. En primærnøkkel er en verdi som brukes til å identifisere én spesifikk rad i en tabell. Selv om dette kan baseres på en verdi i seg selv (vi kunne for eksempel bruke navnet på byen), bør det nesten alltid være et tall eller en annen identifikator. Vi ønsker ikke at ID-en skal endres, da det vil bryte relasjonen. Du vil i de fleste tilfeller finne at primærnøkkelen eller ID-en er et automatisk generert nummer.

> ✅ Primærnøkkel forkortes ofte som PK

### byer

| by_id | By       | Land          |
| ----- | -------- | ------------- |
| 1     | Tokyo    | Japan         |
| 2     | Atlanta  | USA           |
| 3     | Auckland | New Zealand   |

> ✅ Du vil legge merke til at vi bruker begrepene "id" og "primærnøkkel" om hverandre i denne leksjonen. Konseptene her gjelder også for DataFrames, som du vil utforske senere. DataFrames bruker ikke terminologien "primærnøkkel", men du vil merke at de oppfører seg på omtrent samme måte.

Med vår byer-tabell opprettet, la oss lagre nedbøren. I stedet for å duplisere all informasjon om byen, kan vi bruke ID-en. Vi bør også sørge for at den nylig opprettede tabellen har en *id*-kolonne også, siden alle tabeller bør ha en id eller primærnøkkel.

### nedbør

| nedbør_id | by_id | År   | Mengde |
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

Legg merke til kolonnen **by_id** inne i den nylig opprettede **nedbør**-tabellen. Denne kolonnen inneholder verdier som refererer til ID-ene i **byer**-tabellen. I tekniske relasjonsdatatermer kalles dette en **fremmednøkkel**; det er en primærnøkkel fra en annen tabell. Du kan bare tenke på det som en referanse eller en peker. **by_id** 1 refererer til Tokyo.

> [!NOTE] 
> Fremmednøkkel forkortes ofte som FK

## Hente ut data

Med dataene våre delt opp i to tabeller, lurer du kanskje på hvordan vi henter dem ut. Hvis vi bruker en relasjonsdatabase som MySQL, SQL Server eller Oracle, kan vi bruke et språk kalt Structured Query Language eller SQL. SQL (noen ganger uttalt "sequel") er et standard språk som brukes for å hente ut og endre data i en relasjonsdatabase.

For å hente ut data bruker du kommandoen `SELECT`. I kjernen velger du kolonnene du vil se **fra** tabellen de ligger i. Hvis du bare vil vise navnene på byene, kan du bruke følgende:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` er der du lister opp kolonnene, og `FROM` er der du lister opp tabellene.

> [!NOTE] 
> SQL-syntaks er ikke sensitiv for store og små bokstaver, så `select` og `SELECT` betyr det samme. Men avhengig av hvilken type database du bruker, kan kolonner og tabeller være case-sensitive. Derfor er det beste praksis å alltid behandle alt i programmering som case-sensitive. Når du skriver SQL-spørringer, er det vanlig konvensjon å skrive nøkkelordene med store bokstaver.

Spørringen over vil vise alle byer. La oss si vi bare vil vise byer i New Zealand. Vi trenger en form for filter. SQL-nøkkelordet for dette er `WHERE`, eller "hvor noe er sant".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Slå sammen data

Til nå har vi hentet data fra én enkelt tabell. Nå vil vi samle dataene fra både **byer** og **nedbør**. Dette gjøres ved å *slå sammen* dem. Du lager effektivt en søm mellom de to tabellene, og matcher verdiene fra en kolonne i hver tabell.

I vårt eksempel vil vi matche kolonnen **by_id** i **nedbør** med kolonnen **by_id** i **byer**. Dette vil matche nedbørsmengden med sin respektive by. Typen sammenslåing vi utfører kalles en *indre* join, som betyr at hvis noen rader ikke matcher noe fra den andre tabellen, vil de ikke vises. I vårt tilfelle har hver by nedbør, så alt vil vises.

La oss hente nedbøren for 2019 for alle byene våre.

Vi gjør dette i trinn. Det første trinnet er å slå sammen dataene ved å indikere kolonnene for sømmen - **by_id** som fremhevet tidligere.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Vi har fremhevet de to kolonnene vi vil ha, og at vi vil slå sammen tabellene ved **by_id**. Nå kan vi legge til `WHERE`-setningen for å filtrere ut bare året 2019.

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

## Oppsummering

Relasjonsdatabaser er sentrert rundt å dele informasjon mellom flere tabeller som deretter bringes sammen igjen for visning og analyse. Dette gir stor fleksibilitet til å utføre beregninger og ellers manipulere data. Du har sett kjernebegrepene i en relasjonsdatabase, og hvordan du utfører en join mellom to tabeller.

## 🚀 Utfordring

Det finnes mange relasjonsdatabaser tilgjengelig på internett. Du kan utforske dataene ved å bruke ferdighetene du har lært ovenfor.

## Etter-forelesningsquiz

## [Etter-forelesningsquiz](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Gjennomgang og selvstudium

Det finnes flere ressurser tilgjengelig på [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) for at du kan fortsette utforskningen av SQL og relasjonsdatabasekonsepter

- [Beskriv konsepter for relasjonsdata](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Kom i gang med spørringer med Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL er en versjon av SQL)
- [SQL-innhold på Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Oppgave

[Visning av flyplassdata](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->