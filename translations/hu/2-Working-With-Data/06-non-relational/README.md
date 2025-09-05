<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c182e87f9f80be7e7cdffc7b40bbfccf",
  "translation_date": "2025-09-05T17:26:09+00:00",
  "source_file": "2-Working-With-Data/06-non-relational/README.md",
  "language_code": "hu"
}
-->
# Adatok kezelése: Nem-relációs adatok

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/06-NoSQL.png)|
|:---:|
|NoSQL adatok kezelése - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Előadás előtti kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/10)

Az adatok nem korlátozódnak relációs adatbázisokra. Ez a lecke a nem-relációs adatokra összpontosít, és bemutatja az alapokat a táblázatok és a NoSQL kapcsán.

## Táblázatok

A táblázatok népszerű módjai az adatok tárolásának és vizsgálatának, mivel kevesebb előkészületet igényelnek a használatuk. Ebben a leckében megismerheted a táblázatok alapvető elemeit, valamint a képleteket és függvényeket. Az példák Microsoft Excel segítségével lesznek bemutatva, de a legtöbb rész és téma hasonló elnevezésekkel és lépésekkel rendelkezik más táblázatkezelő szoftverek esetében is.

![Egy üres Microsoft Excel munkafüzet két munkalappal](../../../../2-Working-With-Data/06-non-relational/images/parts-of-spreadsheet.png)

A táblázat egy fájl, amely elérhető a számítógép, eszköz vagy felhő alapú fájlrendszerben. Maga a szoftver lehet böngésző alapú vagy telepíthető alkalmazás, illetve letölthető applikáció. Az Excelben ezek a fájlok **munkafüzetként** vannak definiálva, és ezt a terminológiát fogjuk használni a lecke további részében.

Egy munkafüzet egy vagy több **munkalapot** tartalmaz, ahol minden munkalap fülekkel van megjelölve. Egy munkalapon belül találhatók a téglalap alakú **cellák**, amelyek az adatokat tartalmazzák. Egy cella egy sor és oszlop metszéspontjában helyezkedik el, ahol az oszlopokat betűkkel, a sorokat pedig számokkal jelölik. Néhány táblázat az első néhány sorban fejlécet tartalmaz, amely leírja az adott cellában található adatokat.

Az Excel munkafüzet alapvető elemeivel egy példát fogunk használni a [Microsoft Templates](https://templates.office.com/) oldalról, amely egy készletkezelésre fókuszál, hogy bemutassuk a táblázatok további részeit.

### Készletkezelés

A "InventoryExample" nevű táblázatfájl egy formázott táblázat, amely egy készlet elemeit tartalmazza, és három munkalapot foglal magában, ahol a fülek nevei: "Inventory List", "Inventory Pick List" és "Bin Lookup". Az Inventory List munkalap 4. sora a fejléc, amely leírja az egyes cellák értékét az oszlopokban.

![Egy kiemelt képlet egy példakészlet listájából a Microsoft Excelben](../../../../2-Working-With-Data/06-non-relational/images/formula-excel.png)

Vannak olyan esetek, amikor egy cella értéke más cellák értékeitől függ, hogy meghatározza saját értékét. Az Inventory List táblázat nyomon követi az egyes elemek költségét a készletben, de mi van akkor, ha tudni szeretnénk a teljes készlet értékét? [**Képletek**](https://support.microsoft.com/en-us/office/overview-of-formulas-34519a4e-1e8d-4f4b-84d4-d642c4f63263) hajtanak végre műveleteket a cellaadatokon, és ebben a példában a készlet költségének kiszámítására használják. Ez a táblázat egy képletet használ az Inventory Value oszlopban, hogy kiszámítsa az egyes elemek értékét a QTY fejléc alatti mennyiség és a COST fejléc alatti költség szorzásával. Egy cellára duplán kattintva vagy kiemelve látható a képlet. Észre fogod venni, hogy a képletek egy egyenlőségjellel kezdődnek, amelyet a számítás vagy művelet követ.

![Egy kiemelt függvény egy példakészlet listájából a Microsoft Excelben](../../../../2-Working-With-Data/06-non-relational/images/function-excel.png)

Egy másik képletet is használhatunk, hogy összeadjuk az Inventory Value értékeit, és megkapjuk a teljes értéket. Ez kiszámítható lenne az egyes cellák összeadásával, de ez fárasztó feladat lehet. Az Excel rendelkezik [**függvényekkel**](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89), vagyis előre definiált képletekkel, amelyek cellaértékeken végeznek számításokat. A függvények argumentumokat igényelnek, amelyek a számításokhoz szükséges értékek. Ha egy függvény több argumentumot igényel, akkor azokat meghatározott sorrendben kell megadni, különben a függvény nem számítja ki helyesen az értéket. Ebben a példában a SUM függvényt használjuk, amely az Inventory Value értékeit használja argumentumként, hogy összeadja azokat, és az eredményt a 3. sor, B oszlop (B3) alatt jeleníti meg.

## NoSQL

A NoSQL egy gyűjtőfogalom a nem-relációs adatok tárolásának különböző módjaira, és értelmezhető "nem-SQL", "nem-relációs" vagy "nem csak SQL" kifejezésként. Ezeket az adatbázis-rendszereket négy típusba lehet sorolni.

![Egy kulcs-érték adatbázis grafikus ábrázolása, amely négy egyedi numerikus kulcsot mutat, amelyek négy különböző értékhez kapcsolódnak](../../../../2-Working-With-Data/06-non-relational/images/kv-db.png)
> Forrás: [Michał Białecki Blog](https://www.michalbialecki.com/2018/03/18/azure-cosmos-db-key-value-database-cloud/)

A [Kulcs-érték](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#keyvalue-data-stores) adatbázisok egyedi kulcsokat párosítanak, amelyek egyedi azonosítók, és egy értékhez kapcsolódnak. Ezeket a párokat egy [hash táblában](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/) tárolják egy megfelelő hash függvény segítségével.

![Egy gráf adatbázis grafikus ábrázolása, amely emberek, érdeklődési körök és helyek közötti kapcsolatokat mutat](../../../../2-Working-With-Data/06-non-relational/images/graph-db.png)
> Forrás: [Microsoft](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/graph-introduction#graph-database-by-example)

A [Gráf](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#graph-data-stores) adatbázisok az adatok közötti kapcsolatokat írják le, és csomópontok és élek gyűjteményeként vannak ábrázolva. Egy csomópont egy entitást képvisel, például egy diákot vagy bankszámlakivonatot. Az élek két entitás közötti kapcsolatot jelentenek. Minden csomópontnak és élnek vannak tulajdonságai, amelyek további információkat nyújtanak róluk.

![Egy oszlopos adatbázis grafikus ábrázolása, amely egy ügyféladatbázist mutat két oszlopcsaláddal: Identity és Contact Info](../../../../2-Working-With-Data/06-non-relational/images/columnar-db.png)

Az [Oszlopos](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#columnar-data-stores) adatbázisok az adatokat oszlopokba és sorokba szervezik, hasonlóan a relációs adatstruktúrához, de minden oszlop csoportokba van osztva, amelyeket oszlopcsaládnak neveznek, ahol az egy oszlop alatti összes adat kapcsolódik egymáshoz, és egy egységként lekérhető vagy módosítható.

### Dokumentum Adattárolók az Azure Cosmos DB-vel

A [Dokumentum](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#document-data-stores) adattárolók a kulcs-érték adattároló koncepciójára épülnek, és mezők és objektumok sorozatából állnak. Ebben a részben a dokumentum adatbázisokat fogjuk felfedezni a Cosmos DB emulátor segítségével.

Az Azure Cosmos DB adatbázis megfelel a "Nem Csak SQL" definíciónak, ahol a Cosmos DB dokumentum adatbázisa SQL-t használ az adatok lekérdezésére. Az [előző lecke](../05-relational-databases/README.md) az SQL alapjait tárgyalja, és itt néhány ugyanazt a lekérdezést alkalmazhatjuk egy dokumentum adatbázisra. A Cosmos DB Emulátort fogjuk használni, amely lehetővé teszi, hogy helyileg, a számítógépen hozzunk létre és fedezzünk fel egy dokumentum adatbázist. További információ az Emulátorról [itt](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21).

Egy dokumentum mezők és objektumértékek gyűjteménye, ahol a mezők leírják, hogy mit képvisel az objektumérték. Az alábbiakban egy dokumentum példája látható.

```json
{
    "firstname": "Eva",
    "age": 44,
    "id": "8c74a315-aebf-4a16-bb38-2430a9896ce5",
    "_rid": "bHwDAPQz8s0BAAAAAAAAAA==",
    "_self": "dbs/bHwDAA==/colls/bHwDAPQz8s0=/docs/bHwDAPQz8s0BAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f95-010a691e01d7\"",
    "_attachments": "attachments/",
    "_ts": 1630544034
}
```

A dokumentum érdekes mezői: `firstname`, `id` és `age`. A többi mezőt a Cosmos DB generálta.

#### Adatok felfedezése a Cosmos DB Emulátorral

Az emulátort letöltheted és telepítheted [Windowsra itt](https://aka.ms/cosmosdb-emulator). További információ a macOS és Linux rendszeren való futtatásról [itt található](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos).

Az emulátor egy böngészőablakot indít el, ahol az Explorer nézet lehetővé teszi a dokumentumok felfedezését.

![A Cosmos DB Emulátor Explorer nézete](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-explorer.png)

Ha követed az útmutatót, kattints a "Start with Sample" gombra, hogy létrehozz egy mintaadatbázist, amelynek neve SampleDB. Ha kibontod a SampleDB-t az nyílra kattintva, találsz egy `Persons` nevű tárolót. Egy tároló egy gyűjteményt tartalmaz, amely a tárolóban lévő dokumentumokat jelenti. Felfedezheted a négy egyedi dokumentumot az `Items` alatt.

![Mintaadatok felfedezése a Cosmos DB Emulátorban](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons.png)

#### Dokumentumadatok lekérdezése a Cosmos DB Emulátorral

A mintaadatokat SQL-lekérdezéssel is lekérdezhetjük, ha a második bal oldali gombra kattintasz ("New SQL Query").

`SELECT * FROM c` visszaadja az összes dokumentumot a tárolóban. Adjunk hozzá egy where záradékot, hogy megtaláljuk azokat, akik fiatalabbak 40 évnél.

`SELECT * FROM c where c.age < 40`

![Egy SELECT lekérdezés futtatása a mintaadatokon a Cosmos DB Emulátorban, hogy megtaláljuk azokat a dokumentumokat, amelyek age mezője kisebb mint 40](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons-query.png)

A lekérdezés két dokumentumot ad vissza, észreveheted, hogy az age mező értéke mindkét dokumentumban kisebb mint 40.

#### JSON és Dokumentumok

Ha ismered a JavaScript Object Notation (JSON) formátumot, észre fogod venni, hogy a dokumentumok hasonlítanak a JSON-ra. Ebben a könyvtárban található egy `PersonsData.json` fájl, amely további adatokat tartalmaz, és feltölthető a Persons tárolóba az Emulátorban az `Upload Item` gomb segítségével.

A legtöbb esetben az API-k által visszaadott JSON-adatok közvetlenül áthelyezhetők és tárolhatók dokumentum adatbázisokban. Az alábbiakban egy másik dokumentum látható, amely a Microsoft Twitter-fiókjának tweetjeit képviseli, amelyeket a Twitter API segítségével nyertek ki, majd beillesztettek a Cosmos DB-be.

```json
{
    "created_at": "2021-08-31T19:03:01.000Z",
    "id": "1432780985872142341",
    "text": "Blank slate. Like this tweet if you’ve ever painted in Microsoft Paint before. https://t.co/cFeEs8eOPK",
    "_rid": "dhAmAIUsA4oHAAAAAAAAAA==",
    "_self": "dbs/dhAmAA==/colls/dhAmAIUsA4o=/docs/dhAmAIUsA4oHAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f84-a0958ad901d7\"",
    "_attachments": "attachments/",
    "_ts": 1630537000
```

A dokumentum érdekes mezői: `created_at`, `id` és `text`.

## 🚀 Kihívás

Van egy `TwitterData.json` fájl, amelyet feltölthetsz a SampleDB adatbázisba. Javasolt, hogy egy külön tárolóba add hozzá. Ez az alábbi módon történhet:

1. Kattints az új tároló gombra a jobb felső sarokban
1. Válaszd ki a meglévő adatbázist (SampleDB), és hozz létre egy tároló azonosítót
1. Állítsd be a partíciókulcsot `/id`-re
1. Kattints az OK gombra (a nézet többi információját figyelmen kívül hagyhatod, mivel ez egy kis adatállomány, amely helyileg fut a gépeden)
1. Nyisd meg az új tárolódat, és töltsd fel a Twitter Data fájlt az `Upload Item` gombbal

Próbálj ki néhány SELECT lekérdezést, hogy megtaláld azokat a dokumentumokat, amelyek szövegmezőjében szerepel a Microsoft. Tipp: próbáld ki a [LIKE kulcsszót](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character).

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/11)

## Áttekintés és önálló tanulás

- Vannak további formázási és funkciók a táblázatban, amelyeket ez a lecke nem tárgyal. A Microsoftnak van egy [nagy dokumentációs és videókönyvtára](https://support.microsoft.com/excel) az Excelről, ha többet szeretnél megtudni.

- Ez az architekturális dokumentáció részletezi a nem-relációs adatok különböző típusainak jellemzőit: [Nem-relációs adatok és NoSQL](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data)

- A Cosmos DB egy felhőalapú nem-relációs adatbázis, amely képes tárolni a lecke során említett különböző NoSQL típusokat. Tudj meg többet ezekről a típusokról ebben a [Cosmos DB Microsoft Learn modulban](https://docs.microsoft.com/en-us/learn/paths/work-with-nosql-data-in-azure-cosmos-db/).

## Feladat

[Soda Profits](assignment.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.