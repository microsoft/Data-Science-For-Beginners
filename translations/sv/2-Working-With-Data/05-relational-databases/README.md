<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T11:30:36+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "sv"
}
-->
# Arbeta med data: Relationsdatabaser

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Arbeta med data: Relationsdatabaser - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

Chansen är stor att du tidigare har använt ett kalkylblad för att lagra information. Du hade en uppsättning rader och kolumner, där raderna innehöll informationen (eller data) och kolumnerna beskrev informationen (ibland kallad metadata). En relationsdatabas bygger på denna grundprincip med kolumner och rader i tabeller, vilket gör att du kan ha information spridd över flera tabeller. Detta gör att du kan arbeta med mer komplex data, undvika duplicering och ha flexibilitet i hur du utforskar datan. Låt oss utforska begreppen i en relationsdatabas.

## [Förföreläsningsquiz](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Allt börjar med tabeller

En relationsdatabas har i sin kärna tabeller. Precis som med kalkylbladet är en tabell en samling av kolumner och rader. Raden innehåller data eller information som vi vill arbeta med, såsom namnet på en stad eller mängden nederbörd. Kolumnerna beskriver den data de lagrar.

Låt oss börja vår utforskning genom att starta en tabell för att lagra information om städer. Vi kan börja med deras namn och land. Du kan lagra detta i en tabell enligt följande:

| Stad     | Land          |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | USA           |
| Auckland | Nya Zeeland   |

Notera kolumnnamnen **stad**, **land** och **befolkning** som beskriver den data som lagras, och varje rad har information om en stad.

## Bristerna med en enda tabell

Chansen är att tabellen ovan känns relativt bekant för dig. Låt oss börja lägga till ytterligare data till vår växande databas – årlig nederbörd (i millimeter). Vi fokuserar på åren 2018, 2019 och 2020. Om vi skulle lägga till det för Tokyo kan det se ut så här:

| Stad  | Land   | År   | Mängd  |
| ----- | ------ | ---- | ------ |
| Tokyo | Japan  | 2020 | 1690   |
| Tokyo | Japan  | 2019 | 1874   |
| Tokyo | Japan  | 2018 | 1445   |

Vad lägger du märke till i vår tabell? Du kanske märker att vi duplicerar namnet och landet för staden om och om igen. Det kan ta upp ganska mycket lagringsutrymme och är i stort sett onödigt att ha flera kopior av. Tokyo har ju bara ett namn som vi är intresserade av.

Okej, låt oss prova något annat. Låt oss lägga till nya kolumner för varje år:

| Stad     | Land          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | USA           | 1779 | 1111 | 1683 |
| Auckland | Nya Zeeland   | 1386 | 942  | 1176 |

Medan detta undviker rad-duplicering, tillför det några andra utmaningar. Vi skulle behöva ändra strukturen på vår tabell varje gång det kommer ett nytt år. Dessutom, när vår data växer, gör det att ha åren som kolumner svårare att hämta och beräkna värden.

Det är därför vi behöver flera tabeller och relationer. Genom att dela upp vår data kan vi undvika duplicering och ha mer flexibilitet i hur vi arbetar med vår data.

## Begreppen relationer

Låt oss återgå till vår data och bestämma hur vi vill dela upp saker. Vi vet att vi vill lagra namn och land för våra städer, så detta fungerar troligen bäst i en tabell.

| Stad     | Land          |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | USA           |
| Auckland | Nya Zeeland   |

Men innan vi skapar nästa tabell måste vi lista ut hur vi ska referera till varje stad. Vi behöver någon form av identifierare, ID eller (i tekniska databastermer) en primärnyckel. En primärnyckel är ett värde som används för att identifiera en specifik rad i en tabell. Även om detta kan baseras på ett värde i sig (vi skulle till exempel kunna använda stadens namn), bör det nästan alltid vara ett nummer eller annan identifierare. Vi vill inte att id någonsin ska ändras eftersom det skulle bryta relationen. Du kommer i de flesta fall att hitta att primärnyckeln eller id är ett autogenererat nummer.

> ✅ Primärnyckel förkortas ofta som PK

### städer

| stad_id | Stad     | Land          |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japan         |
| 2       | Atlanta  | USA           |
| 3       | Auckland | Nya Zeeland   |

> ✅ Du kommer att märka att vi använder termerna "id" och "primärnyckel" omväxlande under denna lektion. Begreppen här gäller även för DataFrames, som du kommer att utforska senare. DataFrames använder inte terminologin "primärnyckel", men du kommer att märka att de beter sig på ungefär samma sätt.

Med vår tabell för städer skapad, låt oss lagra nederbörden. Istället för att duplicera fullständig information om staden kan vi använda id. Vi bör också säkerställa att den nyss skapade tabellen har en *id*-kolumn också, eftersom alla tabeller bör ha ett id eller primärnyckel.

### nederbörd

| nederbörd_id | stad_id | År   | Mängd  |
| ------------ | ------- | ---- | ------ |
| 1            | 1       | 2018 | 1445   |
| 2            | 1       | 2019 | 1874   |
| 3            | 1       | 2020 | 1690   |
| 4            | 2       | 2018 | 1779   |
| 5            | 2       | 2019 | 1111   |
| 6            | 2       | 2020 | 1683   |
| 7            | 3       | 2018 | 1386   |
| 8            | 3       | 2019 | 942    |
| 9            | 3       | 2020 | 1176   |

Notera kolumnen **stad_id** i den nyss skapade tabellen **nederbörd**. Denna kolumn innehåller värden som refererar till ID:n i tabellen **städer**. I tekniska relationsdatatermer kallas detta en **främmande nyckel**; det är en primärnyckel från en annan tabell. Du kan bara tänka på det som en referens eller en pekare. **stad_id** 1 refererar till Tokyo.

> [!NOTE] 
> Främmande nyckel förkortas ofta som FK

## Hämta data

Med vår data uppdelad i två tabeller kanske du undrar hur vi hämtar den. Om vi använder en relationsdatabas som MySQL, SQL Server eller Oracle kan vi använda ett språk som kallas Structured Query Language eller SQL. SQL (ibland uttalat "sequel") är ett standardiserat språk som används för att hämta och modifiera data i en relationsdatabas.

För att hämta data använder du kommandot `SELECT`. I sin kärna **väljer** du de kolumner du vill se **från** tabellen de finns i. Om du bara ville visa namnen på städerna kunde du använda följande:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` är där du listar kolumnerna, och `FROM` är där du listar tabellerna.

> [!NOTE] 
> SQL-syntax är skiftlägesokänslig, vilket betyder att `select` och `SELECT` betyder samma sak. Men beroende på vilken typ av databas du använder kan kolumner och tabeller vara skiftlägeskänsliga. Därför är det bästa praxis att alltid behandla allt i programmering som skiftlägeskänsligt. När du skriver SQL-frågor är det vanligt att skriva nyckelorden med versaler.

Frågan ovan visar alla städer. Låt oss föreställa oss att vi bara vill visa städer i Nya Zeeland. Vi behöver någon form av filter. SQL-nyckelordet för detta är `WHERE`, eller "där något är sant".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Sammanfoga data

Hittills har vi hämtat data från en enda tabell. Nu vill vi sammanföra data från både **städer** och **nederbörd**. Detta görs genom att *sammanfoga* dem. Du skapar i praktiken en söm mellan de två tabellerna och matchar värden från en kolumn i varje tabell.

I vårt exempel kommer vi att matcha kolumnen **stad_id** i **nederbörd** med kolumnen **stad_id** i **städer**. Detta matchar nederbörden med dess respektive stad. Typen av sammanfogning vi kommer att göra kallas en *inner* join, vilket betyder att om några rader inte matchar något från den andra tabellen visas de inte. I vårt fall har varje stad nederbörd, så allt kommer att visas.

Låt oss hämta nederbörden för 2019 för alla våra städer.

Vi gör detta i steg. Det första steget är att sammanfoga datan genom att ange kolumnerna för sömmen - **stad_id** som markerats tidigare.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Vi har markerat de två kolumner vi vill ha, och att vi vill sammanfoga tabellerna via **stad_id**. Nu kan vi lägga till `WHERE`-satsen för att filtrera ut endast år 2019.

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

Relationsdatabaser är centrerade kring att dela upp information mellan flera tabeller som sedan sammanförs för visning och analys. Detta ger en hög grad av flexibilitet för att utföra beräkningar och på andra sätt manipulera data. Du har sett kärnbegreppen i en relationsdatabas och hur man gör en sammanfogning mellan två tabeller.

## 🚀 Utmaning

Det finns många relationsdatabaser tillgängliga på internet. Du kan utforska data genom att använda de färdigheter du lärt dig ovan.

## Efterföreläsningsquiz

## [Efterföreläsningsquiz](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Granskning & Självstudier

Det finns flera resurser tillgängliga på [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) för att du ska kunna fortsätta din utforskning av SQL och relationsdatabaskoncept

- [Beskriv begrepp för relationsdata](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Kom igång med frågor med Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL är en version av SQL)
- [SQL-innehåll på Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Uppgift

[Visa flygplatsdata](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->