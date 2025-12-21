<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T11:40:53+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "nl"
}
-->
# Werken met Data: Relationele Databases

|![ Sketchnote door [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Werken met Data: Relationele Databases - _Sketchnote door [@nitya](https://twitter.com/nitya)_ |

De kans is groot dat je in het verleden een spreadsheet hebt gebruikt om informatie op te slaan. Je had een set rijen en kolommen, waarbij de rijen de informatie (of data) bevatten, en de kolommen de informatie beschrijven (soms metadata genoemd). Een relationele database is gebouwd op dit kernprincipe van kolommen en rijen in tabellen, waardoor je informatie over meerdere tabellen kunt verspreiden. Dit stelt je in staat om met complexere data te werken, duplicatie te vermijden en flexibiliteit te hebben in de manier waarop je de data onderzoekt. Laten we de concepten van een relationele database verkennen.

## [Pre-college quiz](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Het begint allemaal met tabellen

Een relationele database heeft als kern tabellen. Net als bij de spreadsheet is een tabel een verzameling van kolommen en rijen. De rij bevat de data of informatie waarmee we willen werken, zoals de naam van een stad of de hoeveelheid neerslag. De kolommen beschrijven de data die ze opslaan.

Laten we onze verkenning beginnen door een tabel te starten om informatie over steden op te slaan. We kunnen beginnen met hun naam en land. Je zou dit in een tabel kunnen opslaan als volgt:

| Stad     | Land          |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | Verenigde Staten |
| Auckland | Nieuw-Zeeland |

Let op de kolomnamen **stad**, **land** en **bevolking** die de opgeslagen data beschrijven, en elke rij bevat informatie over één stad.

## De tekortkomingen van een enkele tabel aanpak

De kans is groot dat de bovenstaande tabel je redelijk bekend voorkomt. Laten we wat extra data toevoegen aan onze groeiende database - jaarlijkse neerslag (in millimeters). We richten ons op de jaren 2018, 2019 en 2020. Als we dit voor Tokyo zouden toevoegen, zou het er ongeveer zo uitzien:

| Stad  | Land    | Jaar | Hoeveelheid |
| ----- | ------- | ---- | ----------- |
| Tokyo | Japan   | 2020 | 1690        |
| Tokyo | Japan   | 2019 | 1874        |
| Tokyo | Japan   | 2018 | 1445        |

Wat valt je op aan onze tabel? Je zult merken dat we de naam en het land van de stad steeds opnieuw dupliceren. Dat kan behoorlijk wat opslagruimte innemen, en is grotendeels onnodig om meerdere kopieën van te hebben. Tokyo heeft immers maar één naam waarin we geïnteresseerd zijn.

Oké, laten we iets anders proberen. Laten we nieuwe kolommen toevoegen voor elk jaar:

| Stad     | Land          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | Verenigde Staten | 1779 | 1111 | 1683 |
| Auckland | Nieuw-Zeeland | 1386 | 942  | 1176 |

Hoewel dit de rijduplicatie voorkomt, voegt het een paar andere uitdagingen toe. We zouden de structuur van onze tabel elke keer moeten aanpassen als er een nieuw jaar bijkomt. Bovendien, naarmate onze data groeit, zal het hebben van jaren als kolommen het lastiger maken om waarden op te halen en te berekenen.

Daarom hebben we meerdere tabellen en relaties nodig. Door onze data op te splitsen kunnen we duplicatie vermijden en meer flexibiliteit hebben in hoe we met onze data werken.

## De concepten van relaties

Laten we terugkeren naar onze data en bepalen hoe we het willen opsplitsen. We weten dat we de naam en het land van onze steden willen opslaan, dus dit werkt waarschijnlijk het beste in één tabel.

| Stad     | Land          |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | Verenigde Staten |
| Auckland | Nieuw-Zeeland |

Maar voordat we de volgende tabel maken, moeten we uitzoeken hoe we naar elke stad verwijzen. We hebben een soort identificator, ID of (in technische databanktermen) een primaire sleutel nodig. Een primaire sleutel is een waarde die wordt gebruikt om één specifieke rij in een tabel te identificeren. Hoewel dit gebaseerd kan zijn op een waarde zelf (we zouden bijvoorbeeld de naam van de stad kunnen gebruiken), moet het bijna altijd een nummer of een andere identificator zijn. We willen niet dat de id ooit verandert, omdat dit de relatie zou verbreken. In de meeste gevallen zal de primaire sleutel of id een automatisch gegenereerd nummer zijn.

> ✅ Primaire sleutel wordt vaak afgekort als PK

### steden

| stad_id | Stad     | Land          |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japan         |
| 2       | Atlanta  | Verenigde Staten |
| 3       | Auckland | Nieuw-Zeeland |

> ✅ Je zult merken dat we de termen "id" en "primaire sleutel" door elkaar gebruiken tijdens deze les. De concepten hier zijn ook van toepassing op DataFrames, die je later zult verkennen. DataFrames gebruiken echter niet de terminologie van "primaire sleutel", maar je zult merken dat ze zich op dezelfde manier gedragen.

Met onze steden-tabel gemaakt, laten we de neerslag opslaan. In plaats van de volledige informatie over de stad te dupliceren, kunnen we de id gebruiken. We moeten er ook voor zorgen dat de nieuw gemaakte tabel een *id* kolom heeft, want alle tabellen moeten een id of primaire sleutel hebben.

### neerslag

| neerslag_id | stad_id | Jaar | Hoeveelheid |
| ----------- | ------- | ---- | ----------- |
| 1           | 1       | 2018 | 1445        |
| 2           | 1       | 2019 | 1874        |
| 3           | 1       | 2020 | 1690        |
| 4           | 2       | 2018 | 1779        |
| 5           | 2       | 2019 | 1111        |
| 6           | 2       | 2020 | 1683        |
| 7           | 3       | 2018 | 1386        |
| 8           | 3       | 2019 | 942         |
| 9           | 3       | 2020 | 1176        |

Let op de **stad_id** kolom in de nieuw gemaakte **neerslag** tabel. Deze kolom bevat waarden die verwijzen naar de ID's in de **steden** tabel. In technische relationele datatermen wordt dit een **foreign key** genoemd; het is een primaire sleutel uit een andere tabel. Je kunt het gewoon zien als een verwijzing of een pointer. **stad_id** 1 verwijst naar Tokyo.

> [!NOTE] 
> Foreign key wordt vaak afgekort als FK

## Data ophalen

Met onze data verdeeld over twee tabellen vraag je je misschien af hoe we die ophalen. Als we een relationele database gebruiken zoals MySQL, SQL Server of Oracle, kunnen we een taal gebruiken die Structured Query Language of SQL heet. SQL (soms uitgesproken als sequel) is een standaardtaal die wordt gebruikt om data op te halen en te wijzigen in een relationele database.

Om data op te halen gebruik je het commando `SELECT`. In de kern **selecteer** je de kolommen die je wilt zien **vanuit** de tabel waarin ze zich bevinden. Als je alleen de namen van de steden wilde weergeven, zou je het volgende kunnen gebruiken:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` is waar je de kolommen opsomt, en `FROM` is waar je de tabellen opsomt.

> [!NOTE] 
> SQL-syntaxis is niet hoofdlettergevoelig, wat betekent dat `select` en `SELECT` hetzelfde betekenen. Afhankelijk van het type database dat je gebruikt kunnen de kolommen en tabellen echter wel hoofdlettergevoelig zijn. Daarom is het een best practice om altijd alles in programmeren te behandelen alsof het hoofdlettergevoelig is. Bij het schrijven van SQL-query's is het gebruikelijk om de sleutelwoorden in hoofdletters te schrijven.

De bovenstaande query zal alle steden weergeven. Stel dat we alleen steden in Nieuw-Zeeland wilden weergeven. We hebben een soort filter nodig. Het SQL-sleutelwoord hiervoor is `WHERE`, of "waar iets waar is".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Data samenvoegen

Tot nu toe hebben we data opgehaald uit één tabel. Nu willen we de data samenbrengen van zowel **steden** als **neerslag**. Dit doen we door ze *te joinen*. Je maakt effectief een naad tussen de twee tabellen en koppelt de waarden van een kolom uit elke tabel aan elkaar.

In ons voorbeeld koppelen we de **stad_id** kolom in **neerslag** met de **stad_id** kolom in **steden**. Dit koppelt de neerslagwaarde aan de bijbehorende stad. Het type join dat we uitvoeren heet een *inner* join, wat betekent dat als er rijen zijn die niet overeenkomen met iets uit de andere tabel, ze niet worden weergegeven. In ons geval heeft elke stad neerslag, dus alles wordt weergegeven.

Laten we de neerslag voor 2019 ophalen voor al onze steden.

We doen dit in stappen. De eerste stap is om de data samen te voegen door de kolommen voor de naad aan te geven - **stad_id** zoals eerder gemarkeerd.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

We hebben de twee kolommen die we willen, gemarkeerd, en het feit dat we de tabellen willen joinen via de **stad_id**. Nu kunnen we de `WHERE`-verklaring toevoegen om alleen het jaar 2019 te filteren.

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

## Samenvatting

Relationele databases zijn gericht op het verdelen van informatie over meerdere tabellen die vervolgens weer worden samengebracht voor weergave en analyse. Dit biedt een hoge mate van flexibiliteit om berekeningen uit te voeren en anderszins data te manipuleren. Je hebt de kernconcepten van een relationele database gezien, en hoe je een join uitvoert tussen twee tabellen.

## 🚀 Uitdaging

Er zijn tal van relationele databases beschikbaar op het internet. Je kunt de data verkennen met de vaardigheden die je hierboven hebt geleerd.

## Post-college quiz

## [Post-college quiz](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Review & Zelfstudie

Er zijn verschillende bronnen beschikbaar op [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) om je verkenning van SQL en relationele databaseconcepten voort te zetten

- [Beschrijf concepten van relationele data](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Beginnen met query's schrijven met Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL is een versie van SQL)
- [SQL-inhoud op Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Opdracht

[Weergeven van luchthaven data](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->