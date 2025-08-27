<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "870a0086adbc313a8eea5489bdcb2522",
  "translation_date": "2025-08-26T20:50:07+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "no"
}
-->
# Arbeide med data: Relasjonsdatabaser

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Arbeide med data: Relasjonsdatabaser - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

Sjansen er stor for at du tidligere har brukt et regneark for å lagre informasjon. Du hadde et sett med rader og kolonner, der radene inneholdt informasjonen (eller dataene), og kolonnene beskrev informasjonen (noen ganger kalt metadata). En relasjonsdatabase er bygget på dette grunnprinsippet med kolonner og rader i tabeller, som lar deg ha informasjon fordelt på flere tabeller. Dette gjør det mulig å jobbe med mer komplekse data, unngå duplisering og ha fleksibilitet i måten du utforsker dataene på. La oss utforske konseptene bak en relasjonsdatabase.

## [Quiz før forelesning](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Det starter med tabeller

En relasjonsdatabase har tabeller som kjerne. Akkurat som med et regneark, er en tabell en samling av kolonner og rader. Radene inneholder dataene eller informasjonen vi ønsker å jobbe med, som navnet på en by eller mengden nedbør. Kolonnene beskriver dataene de lagrer.

La oss begynne vår utforskning ved å lage en tabell for å lagre informasjon om byer. Vi kan starte med deres navn og land. Du kan lagre dette i en tabell som følger:

| By       | Land           |
| -------- | -------------- |
| Tokyo    | Japan          |
| Atlanta  | USA            |
| Auckland | New Zealand    |

Legg merke til at kolonnenavnene **by**, **land** og **befolkning** beskriver dataene som lagres, og hver rad har informasjon om én by.

## Begrensningene ved en enkelt tabell

Sjansen er stor for at tabellen ovenfor virker relativt kjent for deg. La oss begynne å legge til noen ekstra data i vår voksende database – årlig nedbør (i millimeter). Vi fokuserer på årene 2018, 2019 og 2020. Hvis vi skulle legge det til for Tokyo, kan det se slik ut:

| By    | Land   | År  | Mengde |
| ----- | ------ | --- | ------ |
| Tokyo | Japan  | 2020| 1690   |
| Tokyo | Japan  | 2019| 1874   |
| Tokyo | Japan  | 2018| 1445   |

Hva legger du merke til med tabellen vår? Du ser kanskje at vi dupliserer navnet og landet til byen om og om igjen. Dette kan ta opp ganske mye lagringsplass og er stort sett unødvendig. Tross alt har Tokyo bare ett navn vi er interessert i.

OK, la oss prøve noe annet. La oss legge til nye kolonner for hvert år:

| By       | Land           | 2018 | 2019 | 2020 |
| -------- | -------------- | ---- | ---- | ---- |
| Tokyo    | Japan          | 1445 | 1874 | 1690 |
| Atlanta  | USA            | 1779 | 1111 | 1683 |
| Auckland | New Zealand    | 1386 | 942  | 1176 |

Selv om dette unngår duplisering av rader, introduserer det noen andre utfordringer. Vi må endre strukturen på tabellen hver gang det kommer et nytt år. I tillegg, etter hvert som dataene vokser, vil det å ha år som kolonner gjøre det vanskeligere å hente ut og beregne verdier.

Dette er grunnen til at vi trenger flere tabeller og relasjoner. Ved å dele opp dataene kan vi unngå duplisering og ha mer fleksibilitet i hvordan vi jobber med dataene.

## Konseptet med relasjoner

La oss gå tilbake til dataene våre og bestemme hvordan vi vil dele dem opp. Vi vet at vi vil lagre navn og land for byene våre, så dette vil sannsynligvis fungere best i én tabell.

| By       | Land           |
| -------- | -------------- |
| Tokyo    | Japan          |
| Atlanta  | USA            |
| Auckland | New Zealand    |

Men før vi oppretter neste tabell, må vi finne ut hvordan vi skal referere til hver by. Vi trenger en form for identifikator, ID eller (i tekniske databasetermer) en primærnøkkel. En primærnøkkel er en verdi som brukes til å identifisere én spesifikk rad i en tabell. Selv om dette kan være basert på en verdi i seg selv (vi kunne for eksempel bruke navnet på byen), bør det nesten alltid være et nummer eller en annen identifikator. Vi vil ikke at ID-en skal endres, da det vil bryte relasjonen. I de fleste tilfeller vil primærnøkkelen eller ID-en være et automatisk generert nummer.

> ✅ Primærnøkkel forkortes ofte som PK

### byer

| by_id | By       | Land           |
| ----- | -------- | -------------- |
| 1     | Tokyo    | Japan          |
| 2     | Atlanta  | USA            |
| 3     | Auckland | New Zealand    |

> ✅ Du vil legge merke til at vi bruker begrepene "id" og "primærnøkkel" om hverandre i løpet av denne leksjonen. Konseptene her gjelder også for DataFrames, som du vil utforske senere. DataFrames bruker ikke terminologien "primærnøkkel", men du vil legge merke til at de oppfører seg på samme måte.

Med vår **byer**-tabell opprettet, la oss lagre nedbøren. I stedet for å duplisere full informasjon om byen, kan vi bruke ID-en. Vi bør også sørge for at den nyopprettede tabellen har en *id*-kolonne, siden alle tabeller bør ha en ID eller primærnøkkel.

### nedbør

| nedbør_id | by_id | År  | Mengde |
| --------- | ----- | --- | ------ |
| 1         | 1     | 2018| 1445   |
| 2         | 1     | 2019| 1874   |
| 3         | 1     | 2020| 1690   |
| 4         | 2     | 2018| 1779   |
| 5         | 2     | 2019| 1111   |
| 6         | 2     | 2020| 1683   |
| 7         | 3     | 2018| 1386   |
| 8         | 3     | 2019| 942    |
| 9         | 3     | 2020| 1176   |

Legg merke til **by_id**-kolonnen i den nyopprettede **nedbør**-tabellen. Denne kolonnen inneholder verdier som refererer til ID-ene i **byer**-tabellen. I tekniske relasjonsdatatermer kalles dette en **fremmednøkkel**; det er en primærnøkkel fra en annen tabell. Du kan bare tenke på det som en referanse eller en peker. **by_id** 1 refererer til Tokyo.

> [!NOTE] Fremmednøkkel forkortes ofte som FK

## Hente ut data

Med dataene våre delt opp i to tabeller, lurer du kanskje på hvordan vi henter dem ut. Hvis vi bruker en relasjonsdatabase som MySQL, SQL Server eller Oracle, kan vi bruke et språk som heter Structured Query Language eller SQL. SQL (noen ganger uttalt "sequel") er et standard språk som brukes til å hente og endre data i en relasjonsdatabase.

For å hente data bruker du kommandoen `SELECT`. I sin kjerne **velger** du kolonnene du vil se **fra** tabellen de er inneholdt i. Hvis du for eksempel bare vil vise navnene på byene, kan du bruke følgende:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` er der du lister opp kolonnene, og `FROM` er der du lister opp tabellene.

> [NOTE] SQL-syntaks er ikke store- og småbokstavfølsom, noe som betyr at `select` og `SELECT` betyr det samme. Men avhengig av hvilken type database du bruker, kan kolonner og tabeller være store- og småbokstavfølsomme. Som et resultat er det en god praksis alltid å behandle alt i programmering som om det er store- og småbokstavfølsomt. Når du skriver SQL-spørringer, er det vanlig konvensjon å skrive nøkkelordene med store bokstaver.

Spørringen ovenfor vil vise alle byene. La oss forestille oss at vi bare vil vise byer i New Zealand. Vi trenger en form for filter. SQL-nøkkelordet for dette er `WHERE`, eller "hvor noe er sant".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Slå sammen data

Til nå har vi hentet data fra én enkelt tabell. Nå vil vi kombinere dataene fra både **byer** og **nedbør**. Dette gjøres ved å *slå dem sammen*. Du vil i praksis lage en kobling mellom de to tabellene og matche verdiene fra en kolonne i hver tabell.

I vårt eksempel vil vi matche **by_id**-kolonnen i **nedbør** med **by_id**-kolonnen i **byer**. Dette vil matche nedbørverdien med sin respektive by. Typen sammenslåing vi vil utføre kalles en *inner join*, noe som betyr at hvis noen rader ikke matcher med noe fra den andre tabellen, vil de ikke bli vist. I vårt tilfelle har hver by nedbør, så alt vil bli vist.

La oss hente nedbøren for 2019 for alle byene våre.

Vi skal gjøre dette i trinn. Det første trinnet er å slå sammen dataene ved å indikere kolonnene for koblingen - **by_id** som fremhevet tidligere.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Vi har fremhevet de to kolonnene vi ønsker, og det faktum at vi vil slå sammen tabellene ved hjelp av **by_id**. Nå kan vi legge til `WHERE`-setningen for å filtrere ut kun år 2019.

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

Relasjonsdatabaser er sentrert rundt å dele informasjon mellom flere tabeller som deretter bringes sammen for visning og analyse. Dette gir en høy grad av fleksibilitet til å utføre beregninger og ellers manipulere data. Du har sett kjernekonseptene i en relasjonsdatabase, og hvordan du utfører en sammenslåing mellom to tabeller.

## 🚀 Utfordring

Det finnes mange relasjonsdatabaser tilgjengelig på internett. Du kan utforske dataene ved å bruke ferdighetene du har lært ovenfor.

## Quiz etter forelesning

## [Quiz etter forelesning](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/9)

## Gjennomgang og selvstudium

Det finnes flere ressurser tilgjengelig på [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) for å fortsette din utforskning av SQL og relasjonsdatabasekonsepter:

- [Beskriv konsepter for relasjonsdata](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Kom i gang med spørringer i Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL er en versjon av SQL)
- [SQL-innhold på Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Oppgave

[Oppgavetittel](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.