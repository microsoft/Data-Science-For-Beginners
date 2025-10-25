<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80d80300002ef4e77cc7631d5904bd6e",
  "translation_date": "2025-10-25T19:03:35+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "hu"
}
-->
# Adatok kezelése: Relációs adatbázisok

|![ Sketchnote készítette: [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Adatok kezelése: Relációs adatbázisok - _Sketchnote készítette: [@nitya](https://twitter.com/nitya)_ |

Valószínűleg már használtál korábban táblázatot információk tárolására. Volt egy sorokból és oszlopokból álló táblázatod, ahol a sorok tartalmazták az információkat (vagy adatokat), az oszlopok pedig leírták az információkat (ezeket néha metaadatoknak is nevezik). A relációs adatbázis ezen alapelvre épül, amely táblázatokban oszlopokat és sorokat használ, lehetővé téve az információk több táblázatban való elosztását. Ez lehetővé teszi, hogy összetettebb adatokkal dolgozz, elkerüld az ismétléseket, és rugalmasan vizsgálhasd az adatokat. Nézzük meg a relációs adatbázis fogalmait.

## [Előadás előtti kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Minden a táblázatokkal kezdődik

A relációs adatbázis alapja a táblázatok. Akárcsak a táblázatok esetében, egy táblázat oszlopok és sorok gyűjteménye. A sorok tartalmazzák azokat az adatokat vagy információkat, amelyekkel dolgozni szeretnénk, például egy város nevét vagy a csapadékmennyiséget. Az oszlopok leírják az általuk tárolt adatokat.

Kezdjük azzal, hogy létrehozunk egy táblázatot a városokkal kapcsolatos információk tárolására. Kezdhetjük a nevükkel és az országukkal. Ezt például így tárolhatnánk egy táblázatban:

| Város    | Ország        |
| -------- | ------------- |
| Tokió    | Japán         |
| Atlanta  | Egyesült Államok |
| Auckland | Új-Zéland     |

Figyeld meg, hogy a **város**, **ország** és **népesség** oszlopok leírják a tárolt adatokat, és minden sor egy városról tartalmaz információt.

## Az egyetlen táblázatos megközelítés hiányosságai

Valószínűleg a fenti táblázat ismerősnek tűnik számodra. Kezdjünk el további adatokat hozzáadni a növekvő adatbázisunkhoz - éves csapadékmennyiség (milliméterben). Az évekre koncentrálunk: 2018, 2019 és 2020. Ha Tokióra vonatkozóan adnánk hozzá adatokat, az valahogy így nézne ki:

| Város | Ország | Év   | Mennyiség |
| ----- | ------ | ---- | -------- |
| Tokió | Japán  | 2020 | 1690     |
| Tokió | Japán  | 2019 | 1874     |
| Tokió | Japán  | 2018 | 1445     |

Mit veszel észre a táblázatunkon? Valószínűleg észreveszed, hogy a város nevét és országát újra és újra megismételjük. Ez elég sok tárhelyet foglalhat, és nagyrészt felesleges, hogy több példányban szerepeljen. Végül is Tokiónak csak egy neve van, ami minket érdekel.

Rendben, próbáljunk ki valami mást. Adjunk hozzá új oszlopokat minden évhez:

| Város    | Ország        | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokió    | Japán         | 1445 | 1874 | 1690 |
| Atlanta  | Egyesült Államok | 1779 | 1111 | 1683 |
| Auckland | Új-Zéland     | 1386 | 942  | 1176 |

Bár ez elkerüli a sorok ismétlését, néhány más kihívást is felvet. Módosítanunk kellene a táblázat szerkezetét minden alkalommal, amikor új év kerül hozzáadásra. Ezenkívül, ahogy az adataink növekednek, az évek oszlopként való tárolása megnehezíti az értékek lekérését és kiszámítását.

Ezért van szükségünk több táblázatra és kapcsolatokra. Az adatok szétválasztásával elkerülhetjük az ismétlést, és nagyobb rugalmasságot érhetünk el az adatok kezelésében.

## A kapcsolatok fogalma

Térjünk vissza az adatainkhoz, és határozzuk meg, hogyan szeretnénk szétosztani őket. Tudjuk, hogy a városok nevét és országát szeretnénk tárolni, így ez valószínűleg egy táblázatban működik a legjobban.

| Város    | Ország        |
| -------- | ------------- |
| Tokió    | Japán         |
| Atlanta  | Egyesült Államok |
| Auckland | Új-Zéland     |

De mielőtt létrehoznánk a következő táblázatot, ki kell találnunk, hogyan hivatkozzunk minden egyes városra. Szükségünk van valamilyen azonosítóra, ID-re vagy (technikai adatbázis kifejezéssel élve) elsődleges kulcsra. Az elsődleges kulcs egy érték, amely egy adott sort azonosít a táblázatban. Bár ez alapulhat egy értéken (például használhatnánk a város nevét), szinte mindig egy szám vagy más azonosító kell, hogy legyen. Nem szeretnénk, hogy az azonosító valaha is megváltozzon, mivel ez megszakítaná a kapcsolatot. A legtöbb esetben az elsődleges kulcs vagy azonosító automatikusan generált szám lesz.

> ✅ Az elsődleges kulcsot gyakran PK-ként rövidítik.

### városok

| város_id | Város    | Ország        |
| -------- | -------- | ------------- |
| 1        | Tokió    | Japán         |
| 2        | Atlanta  | Egyesült Államok |
| 3        | Auckland | Új-Zéland     |

> ✅ Észre fogod venni, hogy az "id" és az "elsődleges kulcs" kifejezéseket felváltva használjuk ebben a leckében. Ezek a fogalmak vonatkoznak a DataFrame-ekre is, amelyeket később fogsz felfedezni. A DataFrame-ek nem használják az "elsődleges kulcs" terminológiát, azonban észre fogod venni, hogy nagyon hasonlóan viselkednek.

Miután létrehoztuk a városok táblázatát, tároljuk a csapadékmennyiséget. Ahelyett, hogy megismételnénk a város teljes információját, használhatjuk az azonosítót. Biztosítanunk kell azt is, hogy az újonnan létrehozott táblázatnak legyen egy *id* oszlopa, mivel minden táblázatnak kell, hogy legyen egy azonosítója vagy elsődleges kulcsa.

### csapadék

| csapadék_id | város_id | Év   | Mennyiség |
| ----------- | -------- | ---- | -------- |
| 1           | 1        | 2018 | 1445     |
| 2           | 1        | 2019 | 1874     |
| 3           | 1        | 2020 | 1690     |
| 4           | 2        | 2018 | 1779     |
| 5           | 2        | 2019 | 1111     |
| 6           | 2        | 2020 | 1683     |
| 7           | 3        | 2018 | 1386     |
| 8           | 3        | 2019 | 942      |
| 9           | 3        | 2020 | 1176     |

Figyeld meg a **város_id** oszlopot az újonnan létrehozott **csapadék** táblázatban. Ez az oszlop olyan értékeket tartalmaz, amelyek a **városok** táblázat azonosítóihoz kapcsolódnak. Technikai relációs adatbázis kifejezéssel élve ezt **idegen kulcsnak** nevezzük; ez egy másik táblázat elsődleges kulcsa. Egyszerűen gondolj rá úgy, mint egy hivatkozásra vagy mutatóra. Az **város_id** 1 Tokióra utal.

> [!NOTE] 
> Az idegen kulcsot gyakran FK-ként rövidítik.

## Az adatok lekérése

Miután az adatainkat két táblázatra osztottuk, felmerülhet a kérdés, hogyan kérhetjük le őket. Ha relációs adatbázist használunk, például MySQL-t, SQL Server-t vagy Oracle-t, akkor egy Structured Query Language (SQL) nevű nyelvet használhatunk. Az SQL (néha "szíkvöl"-nek ejtik) egy szabványos nyelv, amelyet az adatok lekérésére és módosítására használnak egy relációs adatbázisban.

Az adatok lekéréséhez a `SELECT` parancsot használjuk. Alapvetően **kiválasztod** azokat az oszlopokat, amelyeket látni szeretnél, **abból** a táblázatból, amelyben találhatók. Ha csak a városok neveit szeretnéd megjeleníteni, akkor a következőt használhatod:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

A `SELECT` az, ahol felsorolod az oszlopokat, a `FROM` pedig az, ahol felsorolod a táblázatokat.

> [!NOTE] 
> Az SQL szintaxis nem érzékeny a kis- és nagybetűkre, tehát a `select` és a `SELECT` ugyanazt jelenti. Azonban az adatbázis típusától függően az oszlopok és táblázatok neve érzékeny lehet a kis- és nagybetűkre. Ezért jó gyakorlat, ha mindig úgy kezeljük a programozásban mindent, mintha érzékeny lenne a kis- és nagybetűkre. Az SQL lekérdezések írásakor általános szokás, hogy a kulcsszavakat nagybetűvel írjuk.

A fenti lekérdezés megjeleníti az összes várost. Képzeljük el, hogy csak az Új-Zélandon található városokat szeretnénk megjeleníteni. Szükségünk van valamilyen szűrőre. Az SQL kulcsszava erre a `WHERE`, vagyis "ahol valami igaz".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Adatok összekapcsolása

Eddig csak egyetlen táblázatból kértünk le adatokat. Most szeretnénk összehozni az adatokat a **városok** és **csapadék** táblázatokból. Ezt úgy tehetjük meg, hogy *összekapcsoljuk* őket. Lényegében létrehozunk egy kapcsolatot a két táblázat között, és összepárosítjuk az egyes táblázatok egy-egy oszlopának értékeit.

Példánkban a **város_id** oszlopot fogjuk összekapcsolni a **csapadék** táblázat **város_id** oszlopával. Ez összekapcsolja a csapadékmennyiséget a megfelelő várossal. Az általunk végrehajtott kapcsolat típusa úgynevezett *belső* kapcsolat lesz, ami azt jelenti, hogy ha bármelyik sor nem egyezik meg a másik táblázat valamelyik sorával, akkor nem jelenik meg. A mi esetünkben minden városnak van csapadékmennyisége, így minden megjelenik.

Kérjük le a 2019-es év csapadékmennyiségét minden városra vonatkozóan.

Ezt lépésenként fogjuk megtenni. Az első lépés az adatok összekapcsolása azáltal, hogy megadjuk az oszlopokat a kapcsolat létrehozásához - **város_id**, ahogy korábban kiemeltük.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Kiemeltük a két oszlopot, amelyeket szeretnénk, és azt, hogy a táblázatokat a **város_id** alapján szeretnénk összekapcsolni. Most hozzáadhatjuk a `WHERE` utasítást, hogy csak a 2019-es évet szűrjük ki.

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

## Összefoglalás

A relációs adatbázisok középpontjában az információk több táblázatra való felosztása áll, amelyeket aztán megjelenítésre és elemzésre újra össze lehet kapcsolni. Ez nagy fokú rugalmasságot biztosít a számítások elvégzéséhez és az adatok egyéb módon történő manipulálásához. Láttad a relációs adatbázis alapfogalmait, és azt, hogyan lehet kapcsolatot létrehozni két táblázat között.

## 🚀 Kihívás

Számos relációs adatbázis érhető el az interneten. Fedezd fel az adatokat az itt tanult készségek segítségével.

## Előadás utáni kvíz

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Áttekintés és önálló tanulás

Számos erőforrás érhető el a [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) oldalon, hogy folytathasd az SQL és a relációs adatbázis fogalmainak felfedezését.

- [Relációs adatok fogalmainak ismertetése](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Kezdd el az ismerkedést a Transact-SQL-lel](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (A Transact-SQL az SQL egy változata)
- [SQL tartalom a Microsoft Learn oldalon](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Feladat

[Feladat címe](assignment.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.