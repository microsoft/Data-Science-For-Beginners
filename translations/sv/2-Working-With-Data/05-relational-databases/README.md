<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11b166fbcb7eaf82308cdc24b562f687",
  "translation_date": "2025-09-04T18:59:39+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "sv"
}
-->
# Arbeta med data: Relationsdatabaser

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Arbeta med data: Relationsdatabaser - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

Chansen är stor att du tidigare har använt ett kalkylblad för att lagra information. Du hade en uppsättning rader och kolumner, där raderna innehöll informationen (eller datan) och kolumnerna beskrev informationen (ibland kallad metadata). En relationsdatabas bygger på denna grundprincip med kolumner och rader i tabeller, vilket gör det möjligt att sprida information över flera tabeller. Detta gör att du kan arbeta med mer komplex data, undvika duplicering och ha flexibilitet i hur du utforskar datan. Låt oss utforska koncepten kring en relationsdatabas.

## [Quiz före föreläsningen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Allt börjar med tabeller

En relationsdatabas har tabeller som sin kärna. Precis som med kalkylbladet är en tabell en samling av kolumner och rader. Raden innehåller datan eller informationen vi vill arbeta med, såsom namnet på en stad eller mängden nederbörd. Kolumnerna beskriver datan de lagrar.

Låt oss börja vår utforskning genom att skapa en tabell för att lagra information om städer. Vi kan börja med deras namn och land. Du kan lagra detta i en tabell som följer:

| Stad     | Land          |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | USA           |
| Auckland | Nya Zeeland   |

Observera att kolumnnamnen **stad**, **land** och **befolkning** beskriver den data som lagras, och varje rad har information om en stad.

## Begränsningar med en enda tabell

Chansen är stor att tabellen ovan känns relativt bekant för dig. Låt oss börja lägga till ytterligare data till vår växande databas - årlig nederbörd (i millimeter). Vi fokuserar på åren 2018, 2019 och 2020. Om vi skulle lägga till det för Tokyo, kan det se ut så här:

| Stad  | Land   | År   | Mängd |
| ----- | ------ | ---- | ----- |
| Tokyo | Japan  | 2020 | 1690  |
| Tokyo | Japan  | 2019 | 1874  |
| Tokyo | Japan  | 2018 | 1445  |

Vad märker du med vår tabell? Du kanske märker att vi duplicerar stadens namn och land om och om igen. Det kan ta upp ganska mycket lagringsutrymme och är i stort sett onödigt att ha flera kopior av. Tokyo har ju bara ett namn som vi är intresserade av.

OK, låt oss prova något annat. Låt oss lägga till nya kolumner för varje år:

| Stad     | Land          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | USA           | 1779 | 1111 | 1683 |
| Auckland | Nya Zeeland   | 1386 | 942  | 1176 |

Även om detta undviker radduplicering, tillför det ett par andra utmaningar. Vi skulle behöva ändra strukturen på vår tabell varje gång det finns ett nytt år. Dessutom, när vår data växer, kommer det att bli svårare att hämta och beräkna värden med år som kolumner.

Det är därför vi behöver flera tabeller och relationer. Genom att dela upp vår data kan vi undvika duplicering och få mer flexibilitet i hur vi arbetar med datan.

## Konceptet med relationer

Låt oss återgå till vår data och bestämma hur vi vill dela upp den. Vi vet att vi vill lagra namn och land för våra städer, så detta fungerar förmodligen bäst i en tabell.

| Stad     | Land          |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | USA           |
| Auckland | Nya Zeeland   |

Men innan vi skapar nästa tabell, måste vi lista ut hur vi ska referera till varje stad. Vi behöver någon form av identifierare, ID eller (i tekniska databasvillkor) en primärnyckel. En primärnyckel är ett värde som används för att identifiera en specifik rad i en tabell. Även om detta kan baseras på ett värde i sig självt (vi skulle kunna använda stadens namn, till exempel), bör det nästan alltid vara ett nummer eller annan identifierare. Vi vill inte att ID:t någonsin ska ändras eftersom det skulle bryta relationen. I de flesta fall kommer primärnyckeln eller ID:t att vara ett automatiskt genererat nummer.

> ✅ Primärnyckel förkortas ofta som PK

### städer

| stad_id | Stad     | Land          |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japan         |
| 2       | Atlanta  | USA           |
| 3       | Auckland | Nya Zeeland   |

> ✅ Du kommer att märka att vi använder termerna "id" och "primärnyckel" omväxlande under denna lektion. Koncepten här gäller för DataFrames, som du kommer att utforska senare. DataFrames använder inte terminologin "primärnyckel", men du kommer att märka att de fungerar på samma sätt.

Med vår stadstabell skapad, låt oss lagra nederbörden. Istället för att duplicera den fullständiga informationen om staden kan vi använda ID:t. Vi bör också se till att den nyss skapade tabellen har en *id*-kolumn också, eftersom alla tabeller bör ha ett ID eller en primärnyckel.

### nederbörd

| nederbörd_id | stad_id | År   | Mängd |
| ------------ | ------- | ---- | ----- |
| 1            | 1       | 2018 | 1445  |
| 2            | 1       | 2019 | 1874  |
| 3            | 1       | 2020 | 1690  |
| 4            | 2       | 2018 | 1779  |
| 5            | 2       | 2019 | 1111  |
| 6            | 2       | 2020 | 1683  |
| 7            | 3       | 2018 | 1386  |
| 8            | 3       | 2019 | 942   |
| 9            | 3       | 2020 | 1176  |

Observera kolumnen **stad_id** i den nyss skapade tabellen **nederbörd**. Denna kolumn innehåller värden som refererar till ID:n i tabellen **städer**. I tekniska relationsdatatermer kallas detta en **främmande nyckel**; det är en primärnyckel från en annan tabell. Du kan tänka på det som en referens eller pekare. **stad_id** 1 refererar till Tokyo.

> [!NOTE] Främmande nyckel förkortas ofta som FK

## Hämta data

Med vår data separerad i två tabeller kanske du undrar hur vi hämtar den. Om vi använder en relationsdatabas som MySQL, SQL Server eller Oracle, kan vi använda ett språk som heter Structured Query Language eller SQL. SQL (ibland uttalat "sequel") är ett standardiserat språk som används för att hämta och ändra data i en relationsdatabas.

För att hämta data använder du kommandot `SELECT`. I grunden **väljer** du de kolumner du vill se **från** tabellen de finns i. Om du ville visa bara namnen på städerna, kan du använda följande:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` är där du listar kolumnerna, och `FROM` är där du listar tabellerna.

> [NOTE] SQL-syntax är inte skiftlägeskänslig, vilket betyder att `select` och `SELECT` betyder samma sak. Men beroende på vilken typ av databas du använder kan kolumner och tabeller vara skiftlägeskänsliga. Som en följd är det en god praxis att alltid behandla allt i programmering som om det vore skiftlägeskänsligt. När du skriver SQL-frågor är det vanligt att skriva nyckelord med stora bokstäver.

Frågan ovan kommer att visa alla städer. Låt oss föreställa oss att vi bara ville visa städer i Nya Zeeland. Vi behöver någon form av filter. SQL-nyckelordet för detta är `WHERE`, eller "där något är sant".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Kombinera data

Hittills har vi hämtat data från en enda tabell. Nu vill vi sammanföra data från både **städer** och **nederbörd**. Detta görs genom att *kombinera* dem. Du skapar i princip en koppling mellan de två tabellerna och matchar värdena från en kolumn i varje tabell.

I vårt exempel kommer vi att matcha kolumnen **stad_id** i **nederbörd** med kolumnen **stad_id** i **städer**. Detta kommer att matcha nederbördsdata med respektive stad. Den typ av kombination vi kommer att utföra kallas en *inner join*, vilket betyder att om några rader inte matchar med något från den andra tabellen kommer de inte att visas. I vårt fall har varje stad nederbörd, så allt kommer att visas.

Låt oss hämta nederbörden för 2019 för alla våra städer.

Vi kommer att göra detta i steg. Det första steget är att kombinera datan genom att ange kolumnerna för kopplingen - **stad_id** som vi nämnde tidigare.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Vi har markerat de två kolumner vi vill ha och att vi vill kombinera tabellerna genom **stad_id**. Nu kan vi lägga till `WHERE`-satsen för att filtrera ut endast år 2019.

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

## Sammanfattning

Relationsdatabaser är centrerade kring att dela upp information mellan flera tabeller som sedan sammanförs för visning och analys. Detta ger en hög grad av flexibilitet för att utföra beräkningar och manipulera data. Du har sett kärnkoncepten för en relationsdatabas och hur man utför en kombination mellan två tabeller.

## 🚀 Utmaning

Det finns många relationsdatabaser tillgängliga på internet. Du kan utforska datan genom att använda de färdigheter du har lärt dig ovan.

## Quiz efter föreläsningen

## [Quiz efter föreläsningen](https://ff-quizzes.netlify.app/en/ds/)

## Granskning & Självstudier

Det finns flera resurser tillgängliga på [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) för att fortsätta din utforskning av SQL och koncepten kring relationsdatabaser.

- [Beskriv koncepten kring relationsdata](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Kom igång med att göra frågor med Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL är en version av SQL)
- [SQL-innehåll på Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Uppgift

[Uppgiftstitel](assignment.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller inexaktheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.