<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "870a0086adbc313a8eea5489bdcb2522",
  "translation_date": "2025-08-28T15:17:39+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "nl"
}
-->
# Werken met Data: Relationele Databases

|![ Sketchnote door [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Werken met Data: Relationele Databases - _Sketchnote door [@nitya](https://twitter.com/nitya)_ |

De kans is groot dat je in het verleden een spreadsheet hebt gebruikt om informatie op te slaan. Je had een set van rijen en kolommen, waarbij de rijen de informatie (of data) bevatten en de kolommen de informatie beschreven (soms metadata genoemd). Een relationele database is gebaseerd op dit kernprincipe van kolommen en rijen in tabellen, waardoor je informatie over meerdere tabellen kunt verspreiden. Dit stelt je in staat om met complexere data te werken, duplicatie te vermijden en flexibiliteit te hebben in de manier waarop je de data onderzoekt. Laten we de concepten van een relationele database verkennen.

## [Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Het begint allemaal met tabellen

Een relationele database heeft tabellen als kern. Net zoals bij een spreadsheet is een tabel een verzameling van kolommen en rijen. De rij bevat de data of informatie waarmee we willen werken, zoals de naam van een stad of de hoeveelheid neerslag. De kolommen beschrijven de data die ze opslaan.

Laten we onze verkenning beginnen door een tabel te maken om informatie over steden op te slaan. We kunnen beginnen met hun naam en land. Je zou dit in een tabel kunnen opslaan zoals hieronder:

| Stad      | Land          |
| --------- | ------------- |
| Tokio     | Japan         |
| Atlanta   | Verenigde Staten |
| Auckland  | Nieuw-Zeeland |

Let op dat de kolomnamen **stad**, **land** en **bevolking** de opgeslagen data beschrijven, en elke rij informatie bevat over één stad.

## De tekortkomingen van een enkele tabelbenadering

De kans is groot dat de bovenstaande tabel je relatief bekend voorkomt. Laten we wat extra data toevoegen aan onze groeiende database - jaarlijkse neerslag (in millimeters). We richten ons op de jaren 2018, 2019 en 2020. Als we dit voor Tokio zouden toevoegen, zou het er ongeveer zo uitzien:

| Stad   | Land    | Jaar | Hoeveelheid |
| ------ | ------- | ---- | ----------- |
| Tokio  | Japan   | 2020 | 1690        |
| Tokio  | Japan   | 2019 | 1874        |
| Tokio  | Japan   | 2018 | 1445        |

Wat valt je op aan onze tabel? Je merkt misschien dat we de naam en het land van de stad steeds opnieuw dupliceren. Dat kan behoorlijk wat opslagruimte innemen en is grotendeels onnodig om meerdere kopieën te hebben. Tokio heeft immers maar één naam die ons interesseert.

OK, laten we iets anders proberen. Laten we nieuwe kolommen toevoegen voor elk jaar:

| Stad      | Land          | 2018 | 2019 | 2020 |
| --------- | ------------- | ---- | ---- | ---- |
| Tokio     | Japan         | 1445 | 1874 | 1690 |
| Atlanta   | Verenigde Staten | 1779 | 1111 | 1683 |
| Auckland  | Nieuw-Zeeland | 1386 | 942  | 1176 |

Hoewel dit de duplicatie van rijen vermijdt, brengt het een paar andere uitdagingen met zich mee. We zouden de structuur van onze tabel moeten aanpassen telkens wanneer er een nieuw jaar is. Bovendien, naarmate onze data groeit, zal het hebben van jaren als kolommen het moeilijker maken om waarden op te halen en berekeningen uit te voeren.

Dit is waarom we meerdere tabellen en relaties nodig hebben. Door onze data op te splitsen kunnen we duplicatie vermijden en meer flexibiliteit hebben in hoe we met onze data werken.

## De concepten van relaties

Laten we terugkeren naar onze data en bepalen hoe we deze willen opsplitsen. We weten dat we de naam en het land van onze steden willen opslaan, dus dit werkt waarschijnlijk het beste in één tabel.

| Stad      | Land          |
| --------- | ------------- |
| Tokio     | Japan         |
| Atlanta   | Verenigde Staten |
| Auckland  | Nieuw-Zeeland |

Maar voordat we de volgende tabel maken, moeten we bedenken hoe we elke stad willen refereren. We hebben een soort identificator, ID of (in technische database termen) een primaire sleutel nodig. Een primaire sleutel is een waarde die wordt gebruikt om één specifieke rij in een tabel te identificeren. Hoewel dit gebaseerd kan zijn op een waarde zelf (we zouden bijvoorbeeld de naam van de stad kunnen gebruiken), moet het bijna altijd een nummer of andere identificator zijn. We willen niet dat de id ooit verandert, omdat dit de relatie zou verbreken. In de meeste gevallen zal de primaire sleutel of id een automatisch gegenereerd nummer zijn.

> ✅ Primaire sleutel wordt vaak afgekort als PK

### steden

| stad_id | Stad      | Land          |
| ------- | --------- | ------------- |
| 1       | Tokio     | Japan         |
| 2       | Atlanta   | Verenigde Staten |
| 3       | Auckland  | Nieuw-Zeeland |

> ✅ Je zult merken dat we de termen "id" en "primaire sleutel" door elkaar gebruiken tijdens deze les. De concepten hier zijn van toepassing op DataFrames, die je later zult verkennen. DataFrames gebruiken niet de terminologie van "primaire sleutel", maar je zult merken dat ze zich grotendeels hetzelfde gedragen.

Met onze steden-tabel gemaakt, laten we de neerslag opslaan. In plaats van de volledige informatie over de stad te dupliceren, kunnen we de id gebruiken. We moeten er ook voor zorgen dat de nieuw gemaakte tabel een *id*-kolom heeft, aangezien alle tabellen een id of primaire sleutel moeten hebben.

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

Let op de **stad_id**-kolom in de nieuw gemaakte **neerslag**-tabel. Deze kolom bevat waarden die verwijzen naar de IDs in de **steden**-tabel. In technische relationele datatermen wordt dit een **vreemde sleutel** genoemd; het is een primaire sleutel uit een andere tabel. Je kunt het gewoon zien als een referentie of een pointer. **stad_id** 1 verwijst naar Tokio.

> [!NOTE] Vreemde sleutel wordt vaak afgekort als FK

## Data ophalen

Met onze data verdeeld over twee tabellen, vraag je je misschien af hoe we deze ophalen. Als we een relationele database zoals MySQL, SQL Server of Oracle gebruiken, kunnen we een taal genaamd Structured Query Language of SQL gebruiken. SQL (soms uitgesproken als sequel) is een standaardtaal die wordt gebruikt om data in een relationele database op te halen en te wijzigen.

Om data op te halen gebruik je het commando `SELECT`. In de kern **selecteer** je de kolommen die je wilt zien **uit** de tabel waarin ze staan. Als je alleen de namen van de steden wilt weergeven, kun je het volgende gebruiken:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` is waar je de kolommen opsomt, en `FROM` is waar je de tabellen opsomt.

> [NOTE] SQL-syntaxis is niet hoofdlettergevoelig, wat betekent dat `select` en `SELECT` hetzelfde betekenen. Afhankelijk van het type database dat je gebruikt, kunnen de kolommen en tabellen echter wel hoofdlettergevoelig zijn. Daarom is het een goede gewoonte om alles in programmeren te behandelen alsof het hoofdlettergevoelig is. Bij het schrijven van SQL-query's is het gebruikelijk om de sleutelwoorden in hoofdletters te zetten.

De bovenstaande query zal alle steden weergeven. Stel dat we alleen steden in Nieuw-Zeeland willen weergeven. We hebben een soort filter nodig. Het SQL-sleutelwoord hiervoor is `WHERE`, of "waar iets waar is".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Data samenvoegen

Tot nu toe hebben we data opgehaald uit één tabel. Nu willen we de data uit zowel **steden** als **neerslag** samenvoegen. Dit wordt gedaan door ze *te koppelen*. Je creëert in feite een verbinding tussen de twee tabellen en koppelt de waarden van een kolom uit elke tabel.

In ons voorbeeld zullen we de **stad_id**-kolom in **neerslag** koppelen aan de **stad_id**-kolom in **steden**. Dit zal de neerslagwaarde koppelen aan de bijbehorende stad. Het type koppeling dat we zullen uitvoeren is een *inner* join, wat betekent dat als er rijen zijn die niet overeenkomen met iets uit de andere tabel, ze niet worden weergegeven. In ons geval heeft elke stad neerslag, dus alles zal worden weergegeven.

Laten we de neerslag voor 2019 ophalen voor al onze steden.

We gaan dit in stappen doen. De eerste stap is om de data samen te voegen door de kolommen voor de verbinding aan te geven - **stad_id** zoals eerder benadrukt.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

We hebben de twee kolommen die we willen koppelen gemarkeerd, en het feit dat we de tabellen willen samenvoegen via de **stad_id**. Nu kunnen we de `WHERE`-verklaring toevoegen om alleen jaar 2019 te filteren.

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

Relationele databases draaien om het verdelen van informatie over meerdere tabellen, die vervolgens worden samengevoegd voor weergave en analyse. Dit biedt een hoge mate van flexibiliteit om berekeningen uit te voeren en anderszins data te manipuleren. Je hebt de kernconcepten van een relationele database gezien en hoe je een koppeling tussen twee tabellen uitvoert.

## 🚀 Uitdaging

Er zijn tal van relationele databases beschikbaar op het internet. Je kunt de data verkennen door gebruik te maken van de vaardigheden die je hierboven hebt geleerd.

## Post-Lecture Quiz

## [Post-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/9)

## Review & Zelfstudie

Er zijn verschillende bronnen beschikbaar op [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) om je verkenning van SQL en relationele databaseconcepten voort te zetten.

- [Concepten van relationele data beschrijven](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Beginnen met Queryen met Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL is een versie van SQL)
- [SQL-content op Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Opdracht

[Opdracht Titel](assignment.md)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, willen we u erop wijzen dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.