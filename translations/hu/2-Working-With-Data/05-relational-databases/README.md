<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T12:00:50+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "hu"
}
-->
# Adatkezelés: Relációs adatbázisok

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Adatkezelés: Relációs adatbázisok - _Sketchnote készítette [@nitya](https://twitter.com/nitya)_ |

Valószínűleg már használtál korábban táblázatkezelőt információk tárolására. Volt egy sorokból és oszlopokból álló készleted, ahol a sorok tartalmazták az információt (vagy adatot), az oszlopok pedig leírták az információt (néha metaadatnak is nevezik). A relációs adatbázis ezen az alapelven, az oszlopok és sorok táblákban való elrendezésén alapul, lehetővé téve, hogy az információ több táblában legyen elosztva. Ez lehetővé teszi, hogy összetettebb adatokkal dolgozz, elkerüld az ismétlődést, és rugalmasabb legyél az adatok felfedezésében. Vizsgáljuk meg a relációs adatbázis fogalmait.

## [Előadás előtti kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Minden táblákkal kezdődik

A relációs adatbázis alapját a táblák képezik. Ahogy a táblázatkezelőben, egy tábla oszlopok és sorok gyűjteménye. A sor tartalmazza az adatot vagy információt, amivel dolgozni szeretnénk, például egy város nevét vagy az éves csapadékmennyiséget. Az oszlopok leírják az általuk tárolt adatot.

Kezdjük azzal, hogy létrehozunk egy táblát a városok adatainak tárolására. Kezdhetjük a nevükkel és az országgal. Ezt egy táblában így tárolhatjuk:

| Város    | Ország       |
| -------- | ------------ |
| Tokió    | Japán        |
| Atlanta  | Egyesült Államok |
| Auckland | Új-Zéland    |

Figyeld meg, hogy a **város**, **ország** és **népesség** oszlopnevek leírják a tárolt adatot, és minden sor egy város adatait tartalmazza.

## Az egytáblás megközelítés hiányosságai

Valószínűleg a fenti tábla viszonylag ismerős számodra. Adjunk hozzá további adatot az egyre bővülő adatbázisunkhoz - az éves csapadékmennyiséget (milliméterben). A 2018, 2019 és 2020 évekre koncentrálunk. Ha Tokióra adnánk hozzá, valahogy így nézne ki:

| Város | Ország | Év   | Mennyiség |
| ----- | ------ | ---- | --------- |
| Tokió | Japán  | 2020 | 1690      |
| Tokió | Japán  | 2019 | 1874      |
| Tokió | Japán  | 2018 | 1445      |

Mit veszel észre a táblánkon? Észreveheted, hogy ismétlődően szerepel a város neve és országa. Ez sok tárhelyet foglalhat, és nagyrészt felesleges, hogy több példányban legyen. Hiszen Tokiónak csak egy neve van, ami minket érdekel.

Rendben, próbáljunk valami mást. Adjunk új oszlopokat minden évnek:

| Város    | Ország       | 2018 | 2019 | 2020 |
| -------- | ------------ | ---- | ---- | ---- |
| Tokió    | Japán        | 1445 | 1874 | 1690 |
| Atlanta  | Egyesült Államok | 1779 | 1111 | 1683 |
| Auckland | Új-Zéland    | 1386 | 942  | 1176 |

Bár ez elkerüli a sorok ismétlődését, más kihívásokat hoz. Minden új évnél módosítanunk kell a tábla szerkezetét. Emellett, ahogy nő az adatunk, az évek oszlopként való kezelése megnehezíti az értékek lekérését és számítását.

Ezért van szükségünk több táblára és kapcsolatokra. Az adatok szétbontásával elkerülhetjük az ismétlést, és rugalmasabban dolgozhatunk az adatokkal.

## A kapcsolatok fogalmai

Térjünk vissza az adatainkhoz, és határozzuk meg, hogyan osszuk fel őket. Tudjuk, hogy tárolni akarjuk a városok nevét és országát, így ez valószínűleg egy táblában lesz a legjobb.

| Város    | Ország       |
| -------- | ------------ |
| Tokió    | Japán        |
| Atlanta  | Egyesült Államok |
| Auckland | Új-Zéland    |

De mielőtt létrehoznánk a következő táblát, ki kell találnunk, hogyan hivatkozzunk minden egyes városra. Szükségünk van valamilyen azonosítóra, ID-re vagy (technikai adatbázis kifejezéssel) elsődleges kulcsra. Az elsődleges kulcs egy érték, amely egy adott sort azonosít egy táblában. Bár ez alapulhat egy értéken (például használhatnánk a város nevét), szinte mindig szám vagy más azonosító kell legyen. Nem akarjuk, hogy az id valaha is megváltozzon, mert az megszakítaná a kapcsolatot. A legtöbb esetben az elsődleges kulcs vagy id automatikusan generált szám lesz.

> ✅ Az elsődleges kulcs gyakran PK-ként rövidítve

### városok

| city_id | Város    | Ország       |
| ------- | -------- | ------------ |
| 1       | Tokió    | Japán        |
| 2       | Atlanta  | Egyesült Államok |
| 3       | Auckland | Új-Zéland    |

> ✅ Észre fogod venni, hogy a leckében az "id" és az "elsődleges kulcs" kifejezéseket felváltva használjuk. Ezek a fogalmak alkalmazhatók DataFrame-ekre is, amelyeket később fogsz tanulmányozni. A DataFrame-ek nem használják az "elsődleges kulcs" terminológiát, de viselkedésük hasonló.

Miután létrehoztuk a városok tábláját, tároljuk a csapadékmennyiséget. Ahelyett, hogy ismételnénk a város teljes adatait, használhatjuk az id-t. Biztosítanunk kell, hogy az újonnan létrehozott táblának is legyen *id* oszlopa, mivel minden táblának kell id vagy elsődleges kulcs.

### csapadék

| rainfall_id | city_id | Év   | Mennyiség |
| ----------- | ------- | ---- | --------- |
| 1           | 1       | 2018 | 1445      |
| 2           | 1       | 2019 | 1874      |
| 3           | 1       | 2020 | 1690      |
| 4           | 2       | 2018 | 1779      |
| 5           | 2       | 2019 | 1111      |
| 6           | 2       | 2020 | 1683      |
| 7           | 3       | 2018 | 1386      |
| 8           | 3       | 2019 | 942       |
| 9           | 3       | 2020 | 1176      |

Figyeld meg a **city_id** oszlopot az újonnan létrehozott **csapadék** táblában. Ez az oszlop olyan értékeket tartalmaz, amelyek a **városok** tábla ID-jaira hivatkoznak. Technikai relációs adatbázis kifejezéssel ez egy **külső kulcs**; egy másik tábla elsődleges kulcsa. Egyszerűen hivatkozásnak vagy mutatónak tekintheted. A **city_id** 1 Tokióra hivatkozik.

> [!NOTE] 
> A külső kulcs gyakran FK-ként rövidítve

## Az adatok lekérése

Miután az adataink két táblára vannak bontva, felmerülhet a kérdés, hogyan kérjük le őket. Ha relációs adatbázist használunk, mint például MySQL, SQL Server vagy Oracle, használhatunk egy Structured Query Language nevű nyelvet, azaz SQL-t. Az SQL (néha sequel-nek ejtik) egy szabványos nyelv, amelyet relációs adatbázisokban az adatok lekérésére és módosítására használnak.

Az adatok lekéréséhez a `SELECT` parancsot használjuk. Lényegében kiválasztod azokat az oszlopokat, amelyeket látni szeretnél, abból a táblából, amelyben azok vannak. Ha csak a városok neveit szeretnéd megjeleníteni, a következőt használhatod:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

A `SELECT` az oszlopok felsorolására szolgál, a `FROM` pedig a táblák megadására.

> [!NOTE] 
> Az SQL szintaxisa nem érzékeny a kis- és nagybetűkre, tehát a `select` és a `SELECT` ugyanazt jelenti. Azonban az adatbázis típusától függően az oszlopok és táblák lehetnek kis- és nagybetű érzékenyek. Ezért a legjobb gyakorlat, hogy a programozásban mindent kis- és nagybetű érzékenyként kezeljünk. Az SQL lekérdezések írásakor a kulcsszavakat általában nagybetűvel írjuk.

A fenti lekérdezés az összes várost megjeleníti. Tegyük fel, hogy csak az Új-Zélandi városokat szeretnénk megjeleníteni. Szükségünk van valamilyen szűrőre. Az SQL kulcsszó erre a `WHERE`, vagyis "ahol valami igaz".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Adatok összekapcsolása

Eddig egyetlen táblából kérdeztünk le adatokat. Most össze akarjuk hozni az adatokat a **városok** és a **csapadék** táblákból. Ezt úgy tesszük, hogy *összekapcsoljuk* őket. Lényegében egy varratot hozunk létre a két tábla között, és összeillesztjük az egyik tábla egy oszlopának értékeit a másik tábla megfelelő oszlopával.

Példánkban a **city_id** oszlopot a **csapadék** táblában összekapcsoljuk a **city_id** oszloppal a **városok** táblában. Ez összekapcsolja a csapadék értékét a megfelelő várossal. Az általunk végrehajtott összekapcsolás típusa egy úgynevezett *belső* összekapcsolás (inner join), ami azt jelenti, hogy ha bármelyik sor nem egyezik meg semmivel a másik táblából, azt nem jelenítjük meg. A mi esetünkben minden városhoz tartozik csapadék, így minden megjelenik.

Lekérdezzük a 2019-es csapadékmennyiséget minden városunkra.

Lépésenként fogjuk csinálni. Az első lépés az adatok összekapcsolása a varrat oszlopainak megadásával - a már kiemelt **city_id**.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Kiemeltük a két oszlopot, amelyeket szeretnénk, és azt, hogy a táblákat a **city_id** alapján kapcsoljuk össze. Most hozzáadhatjuk a `WHERE` feltételt, hogy csak a 2019-es évet szűrjük.

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

A relációs adatbázisok az információk több táblára való felosztására épülnek, amelyeket aztán visszahoznak megjelenítésre és elemzésre. Ez nagyfokú rugalmasságot biztosít a számítások elvégzéséhez és az adatok egyéb módon történő kezeléséhez. Megismerted a relációs adatbázis alapfogalmait, és azt, hogyan hajts végre összekapcsolást két tábla között.

## 🚀 Kihívás

Számos relációs adatbázis érhető el az interneten. Fedezd fel az adatokat a fent tanult készségek alkalmazásával.

## Előadás utáni kvíz

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Áttekintés és önálló tanulás

Több forrás is elérhető a [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) oldalán, hogy folytasd az SQL és a relációs adatbázis fogalmak felfedezését

- [Relációs adat fogalmainak leírása](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Kezdő lépések a Transact-SQL lekérdezésekhez](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (A Transact-SQL az SQL egy változata)
- [SQL tartalom a Microsoft Learn-en](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Feladat

[Repülőtéri adatok megjelenítése](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->