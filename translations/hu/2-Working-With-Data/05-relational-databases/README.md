<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9399d7b4767e75068f95ce5c660b285c",
  "translation_date": "2025-09-05T17:28:01+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "hu"
}
-->
# Adatok kezelése: Relációs adatbázisok

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Adatok kezelése: Relációs adatbázisok - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Valószínűleg már használtál korábban táblázatkezelőt információk tárolására. Volt egy sorokból és oszlopokból álló készleted, ahol a sorok tartalmazták az információkat (vagy adatokat), az oszlopok pedig leírták az információkat (néha metaadatoknak nevezik). A relációs adatbázis ezen alapelvre épül: táblázatokban oszlopok és sorok segítségével tárolja az adatokat, lehetővé téve, hogy az információ több táblázatban legyen elosztva. Ez lehetővé teszi, hogy összetettebb adatokkal dolgozz, elkerüld az ismétléseket, és rugalmasan fedezd fel az adatokat. Nézzük meg a relációs adatbázis fogalmait.

## [Előadás előtti kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Minden a táblázatokkal kezdődik

A relációs adatbázis alapja a táblázatok. Akárcsak a táblázatkezelőben, egy táblázat oszlopok és sorok gyűjteménye. A sorok tartalmazzák azokat az adatokat vagy információkat, amelyekkel dolgozni szeretnénk, például egy város nevét vagy a csapadékmennyiséget. Az oszlopok leírják, hogy milyen adatokat tárolnak.

Kezdjük azzal, hogy létrehozunk egy táblázatot a városokkal kapcsolatos információk tárolására. Például elkezdhetjük a nevükkel és az országukkal. Ezt így tárolhatnánk egy táblázatban:

| Város    | Ország         |
| -------- | -------------- |
| Tokió    | Japán          |
| Atlanta  | Egyesült Államok |
| Auckland | Új-Zéland      |

Figyeld meg, hogy a **város**, **ország** és **népesség** oszlopok leírják a tárolt adatokat, és minden sor egy városról tartalmaz információt.

## Az egyetlen táblázatos megközelítés hiányosságai

Valószínűleg a fenti táblázat ismerősnek tűnik számodra. Most adjunk hozzá néhány további adatot az alakuló adatbázisunkhoz - éves csapadékmennyiséget (milliméterben). Az évekre 2018, 2019 és 2020 fogunk koncentrálni. Ha Tokióra szeretnénk hozzáadni, valahogy így nézne ki:

| Város  | Ország | Év   | Mennyiség |
| ------ | ------ | ---- | --------- |
| Tokió  | Japán  | 2020 | 1690      |
| Tokió  | Japán  | 2019 | 1874      |
| Tokió  | Japán  | 2018 | 1445      |

Mit veszel észre a táblázatunkon? Valószínűleg észreveszed, hogy újra és újra ismételjük a város nevét és országát. Ez elég sok tárhelyet foglalhat, és nagyrészt szükségtelen, hogy több példányban legyen. Végül is Tokiónak csak egy neve van, ami minket érdekel.

Rendben, próbáljunk ki valami mást. Adjunk hozzá új oszlopokat minden évhez:

| Város    | Ország         | 2018 | 2019 | 2020 |
| -------- | -------------- | ---- | ---- | ---- |
| Tokió    | Japán          | 1445 | 1874 | 1690 |
| Atlanta  | Egyesült Államok | 1779 | 1111 | 1683 |
| Auckland | Új-Zéland      | 1386 | 942  | 1176 |

Bár ez elkerüli a sorok ismétlését, néhány más kihívást is hoz. Módosítanunk kellene a táblázat szerkezetét minden alkalommal, amikor új év van. Ezenkívül, ahogy az adataink növekednek, az évek oszlopként való tárolása megnehezíti az értékek lekérését és kiszámítását.

Ezért van szükségünk több táblázatra és kapcsolatokra. Az adatok szétválasztásával elkerülhetjük az ismétléseket, és nagyobb rugalmasságot érhetünk el az adatok kezelésében.

## A kapcsolatok fogalma

Térjünk vissza az adatainkhoz, és határozzuk meg, hogyan szeretnénk szétválasztani őket. Tudjuk, hogy a városok neveit és országait szeretnénk tárolni, így ez valószínűleg egy táblázatban működik a legjobban.

| Város    | Ország         |
| -------- | -------------- |
| Tokió    | Japán          |
| Atlanta  | Egyesült Államok |
| Auckland | Új-Zéland      |

De mielőtt létrehoznánk a következő táblázatot, ki kell találnunk, hogyan hivatkozzunk minden városra. Szükségünk van valamilyen azonosítóra, ID-re vagy (technikai adatbázis kifejezéssel élve) elsődleges kulcsra. Az elsődleges kulcs egy érték, amely egy adott sort azonosít egy táblázatban. Bár ez alapulhat egy értéken (például használhatnánk a város nevét), szinte mindig számnak vagy más azonosítónak kell lennie. Nem akarjuk, hogy az azonosító valaha megváltozzon, mert az megszakítaná a kapcsolatot. A legtöbb esetben az elsődleges kulcs vagy azonosító automatikusan generált szám lesz.

> ✅ Az elsődleges kulcsot gyakran PK-ként rövidítik

### városok

| város_id | Város    | Ország         |
| -------- | -------- | -------------- |
| 1        | Tokió    | Japán          |
| 2        | Atlanta  | Egyesült Államok |
| 3        | Auckland | Új-Zéland      |

> ✅ Észre fogod venni, hogy az "id" és "elsődleges kulcs" kifejezéseket felváltva használjuk ebben a leckében. Ezek a fogalmak vonatkoznak a DataFrame-ekre is, amelyeket később fogsz felfedezni. A DataFrame-ek nem használják az "elsődleges kulcs" terminológiát, azonban észre fogod venni, hogy hasonlóan viselkednek.

Miután létrehoztuk a városok táblázatát, tároljuk a csapadékmennyiséget. Ahelyett, hogy megismételnénk a város teljes információját, használhatjuk az azonosítót. Biztosítanunk kell azt is, hogy az újonnan létrehozott táblázatnak legyen egy *id* oszlopa, mivel minden táblázatnak kell, hogy legyen egy azonosítója vagy elsődleges kulcsa.

### csapadék

| csapadék_id | város_id | Év   | Mennyiség |
| ----------- | -------- | ---- | --------- |
| 1           | 1        | 2018 | 1445      |
| 2           | 1        | 2019 | 1874      |
| 3           | 1        | 2020 | 1690      |
| 4           | 2        | 2018 | 1779      |
| 5           | 2        | 2019 | 1111      |
| 6           | 2        | 2020 | 1683      |
| 7           | 3        | 2018 | 1386      |
| 8           | 3        | 2019 | 942       |
| 9           | 3        | 2020 | 1176      |

Figyeld meg a **város_id** oszlopot az újonnan létrehozott **csapadék** táblázatban. Ez az oszlop olyan értékeket tartalmaz, amelyek a **városok** táblázat azonosítójára hivatkoznak. Technikai relációs adatbázis kifejezéssel élve ezt **idegen kulcsnak** nevezzük; ez egy másik táblázat elsődleges kulcsa. Egyszerűen gondolj rá úgy, mint egy hivatkozásra vagy mutatóra. A **város_id** 1 Tokióra hivatkozik.

> [!NOTE] Az idegen kulcsot gyakran FK-ként rövidítik

## Az adatok lekérése

Miután az adatainkat két táblázatra osztottuk, felmerülhet benned a kérdés, hogyan kérjük le őket. Ha relációs adatbázist használunk, például MySQL-t, SQL Servert vagy Oracle-t, egy Structured Query Language (SQL) nevű nyelvet használhatunk. Az SQL (néha "szíkvöl"-nek ejtik) egy szabványos nyelv, amelyet az adatok lekérésére és módosítására használnak egy relációs adatbázisban.

Az adatok lekéréséhez a `SELECT` parancsot használjuk. Alapvetően **kiválasztod** azokat az oszlopokat, amelyeket látni szeretnél, **abból** a táblázatból, amelyben találhatók. Ha csak a városok neveit szeretnéd megjeleníteni, a következőt használhatod:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

A `SELECT` az, ahol felsorolod az oszlopokat, és a `FROM` az, ahol felsorolod a táblázatokat.

> [NOTE] Az SQL szintaxis nem érzékeny a kis- és nagybetűkre, tehát a `select` és a `SELECT` ugyanazt jelenti. Azonban attól függően, hogy milyen típusú adatbázist használsz, az oszlopok és táblázatok érzékenyek lehetnek a kis- és nagybetűkre. Ezért a legjobb gyakorlat mindig úgy kezelni mindent a programozásban, mintha érzékeny lenne a kis- és nagybetűkre. Az SQL lekérdezések írásakor általános szokás, hogy a kulcsszavakat nagybetűvel írjuk.

A fenti lekérdezés megjeleníti az összes várost. Képzeljük el, hogy csak az Új-Zélandon található városokat szeretnénk megjeleníteni. Szükségünk van valamilyen szűrőre. Az SQL kulcsszava erre a `WHERE`, vagyis "ahol valami igaz".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Adatok összekapcsolása

Eddig adatokat csak egyetlen táblázatból kértünk le. Most szeretnénk összehozni az adatokat a **városok** és **csapadék** táblázatokból. Ezt úgy tesszük, hogy *összekapcsoljuk* őket. Lényegében létrehozunk egy varratot a két táblázat között, és összepárosítjuk az értékeket egy-egy oszlopból mindkét táblázatban.

Példánkban a **város_id** oszlopot fogjuk összepárosítani a **csapadék** táblázatban a **város_id** oszloppal a **városok** táblázatban. Ez összekapcsolja a csapadékmennyiséget a megfelelő várossal. Az általunk végrehajtott kapcsolás típusa úgynevezett *belső* kapcsolás, ami azt jelenti, hogy ha bármelyik sor nem egyezik meg semmivel a másik táblázatból, akkor nem jelenik meg. Esetünkben minden városnak van csapadékmennyisége, így minden megjelenik.

Kérjük le a 2019-es csapadékmennyiséget minden városunkra.

Lépésekben fogjuk ezt megtenni. Az első lépés az adatok összekapcsolása azáltal, hogy megadjuk az oszlopokat a varrat számára - **város_id**, ahogy korábban kiemeltük.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Kiemeltük a két oszlopot, amelyeket szeretnénk, és azt, hogy össze akarjuk kapcsolni a táblázatokat a **város_id** alapján. Most hozzáadhatjuk a `WHERE` utasítást, hogy csak a 2019-es évet szűrjük ki.

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

A relációs adatbázisok középpontjában az információk több táblázatra való felosztása áll, amelyeket aztán megjelenítésre és elemzésre hozunk össze. Ez nagyfokú rugalmasságot biztosít a számítások elvégzéséhez és az adatok egyéb módon történő manipulálásához. Láttad a relációs adatbázis alapfogalmait, és azt, hogyan lehet összekapcsolni két táblázatot.

## 🚀 Kihívás

Számos relációs adatbázis érhető el az interneten. Fedezd fel az adatokat az itt tanult készségek segítségével.

## Előadás utáni kvíz

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Áttekintés és önálló tanulás

Számos forrás érhető el a [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) oldalon, hogy folytathasd az SQL és a relációs adatbázis fogalmainak felfedezését.

- [Relációs adatok fogalmainak leírása](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Kezdd el az SQL-lekérdezéseket Transact-SQL-lel](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (A Transact-SQL az SQL egy verziója)
- [SQL tartalom a Microsoft Learn oldalon](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Feladat

[Feladat címe](assignment.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.