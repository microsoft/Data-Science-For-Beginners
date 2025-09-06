<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "12339119c0165da569a93ddba05f9339",
  "translation_date": "2025-09-05T17:37:52+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "hu"
}
-->
# Adatok meghatározása

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Adatok meghatározása - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Az adatok tények, információk, megfigyelések és mérések, amelyeket felfedezésekhez és megalapozott döntések támogatásához használnak. Egy adatpont egyetlen adategység egy adathalmazon belül, amely adatpontok gyűjteménye. Az adathalmazok különböző formátumokban és struktúrákban jelenhetnek meg, és általában az adat forrásától függnek, vagyis attól, hogy honnan származnak. Például egy vállalat havi bevételei lehetnek egy táblázatban, míg egy okosóra óránkénti pulzusadatai [JSON](https://stackoverflow.com/a/383699) formátumban lehetnek. Gyakori, hogy adatkutatók különböző típusú adatokkal dolgoznak egy adathalmazon belül.

Ez a lecke az adatok jellemzői és forrásai alapján történő azonosítására és osztályozására összpontosít.

## [Előadás előtti kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Hogyan írjuk le az adatokat

### Nyers adatok
A nyers adatok azok az adatok, amelyek a forrásukból származnak eredeti állapotukban, és amelyeket még nem elemeztek vagy szerveztek meg. Ahhoz, hogy megértsük, mi történik egy adathalmazzal, azt olyan formátumba kell szervezni, amelyet az emberek és az általuk használt technológia is képes értelmezni. Az adathalmaz szerkezete leírja, hogyan van megszervezve, és osztályozható strukturált, strukturálatlan és félig strukturált kategóriákba. Ezek a struktúratípusok a forrástól függően változhatnak, de végül ebbe a három kategóriába sorolhatók.

### Kvantitatív adatok
A kvantitatív adatok numerikus megfigyelések egy adathalmazon belül, amelyeket általában elemezni, mérni és matematikailag használni lehet. Néhány példa a kvantitatív adatokra: egy ország népessége, egy személy magassága vagy egy vállalat negyedéves bevételei. További elemzéssel a kvantitatív adatok felhasználhatók például az Air Quality Index (AQI) szezonális trendjeinek felfedezésére vagy a csúcsforgalom valószínűségének becslésére egy tipikus munkanapon.

### Kvalitatív adatok
A kvalitatív adatok, más néven kategóriális adatok, olyan adatok, amelyeket nem lehet objektíven mérni, mint a kvantitatív adatok megfigyeléseit. Általában különböző formátumú szubjektív adatok, amelyek valaminek a minőségét rögzítik, például egy termék vagy folyamat esetében. Néha a kvalitatív adatok numerikusak, de nem használhatók matematikailag, mint például telefonszámok vagy időbélyegek. Néhány példa a kvalitatív adatokra: videókommentek, egy autó márkája és modellje, vagy a legközelebbi barátok kedvenc színe. A kvalitatív adatok felhasználhatók például annak megértésére, hogy mely termékeket kedvelik leginkább a fogyasztók, vagy népszerű kulcsszavak azonosítására álláspályázatokban.

### Strukturált adatok
A strukturált adatok olyan adatok, amelyek sorokba és oszlopokba vannak szervezve, ahol minden sor ugyanazt az oszlopkészletet tartalmazza. Az oszlopok egy adott típusú értéket képviselnek, és egy névvel vannak azonosítva, amely leírja, mit képvisel az érték, míg a sorok tartalmazzák a tényleges értékeket. Az oszlopok gyakran meghatározott szabályokat vagy korlátozásokat tartalmaznak az értékekre vonatkozóan, hogy biztosítsák, hogy az értékek pontosan képviseljék az oszlopot. Például képzeljünk el egy ügyfelekről szóló táblázatot, ahol minden sornak tartalmaznia kell egy telefonszámot, és a telefonszámok soha nem tartalmazhatnak betűket. Lehetnek szabályok a telefonszám oszlopra vonatkozóan, hogy az soha ne legyen üres, és csak számokat tartalmazzon.

A strukturált adatok előnye, hogy olyan módon szervezhetők, hogy más strukturált adatokkal kapcsolatba hozhatók legyenek. Azonban mivel az adatokat egy adott módon kell megszervezni, az általános struktúra megváltoztatása sok erőfeszítést igényelhet. Például, ha egy e-mail oszlopot szeretnénk hozzáadni az ügyfelek táblázatához, amely nem lehet üres, akkor ki kell találnunk, hogyan adjuk hozzá ezeket az értékeket az adathalmaz meglévő ügyfél soraihoz.

Példák strukturált adatokra: táblázatok, relációs adatbázisok, telefonszámok, bankszámlakivonatok

### Strukturálatlan adatok
A strukturálatlan adatok általában nem sorokba vagy oszlopokba kategorizálhatók, és nem tartalmaznak formátumot vagy szabályrendszert, amelyet követni kell. Mivel a strukturálatlan adatoknak kevesebb korlátozása van a struktúrájukra vonatkozóan, könnyebb új információkat hozzáadni, mint egy strukturált adathalmaz esetében. Ha például egy szenzor, amely 2 percenként rögzíti a légnyomás adatokat, frissítést kap, amely lehetővé teszi számára a hőmérséklet mérését és rögzítését, nem szükséges módosítani a meglévő adatokat, ha azok strukturálatlanok. Azonban ez megnehezítheti az ilyen típusú adatok elemzését vagy vizsgálatát. Például egy tudós, aki az előző hónap átlagos hőmérsékletét szeretné megtalálni a szenzor adataiból, felfedezheti, hogy a szenzor néhány adatában "e"-t rögzített, hogy jelezze, hogy meghibásodott, ahelyett, hogy tipikus számot rögzített volna, ami azt jelenti, hogy az adatok hiányosak.

Példák strukturálatlan adatokra: szövegfájlok, szöveges üzenetek, videófájlok

### Félig strukturált adatok
A félig strukturált adatok olyan jellemzőkkel rendelkeznek, amelyek a strukturált és strukturálatlan adatok kombinációjává teszik őket. Általában nem felelnek meg a sorok és oszlopok formátumának, de olyan módon vannak szervezve, amely strukturáltnak tekinthető, és követhetnek egy meghatározott formátumot vagy szabályrendszert. A struktúra a források között változhat, például egy jól definiált hierarchiától valami rugalmasabbig, amely lehetővé teszi az új információk könnyű integrálását. A metaadatok olyan jelzők, amelyek segítenek eldönteni, hogyan van az adat szervezve és tárolva, és különböző nevekkel rendelkeznek az adat típusától függően. Néhány gyakori név a metaadatokra: címkék, elemek, entitások és attribútumok. Például egy tipikus e-mail üzenetnek van tárgya, szövege és címzettjei, és szervezhető az alapján, hogy ki vagy mikor küldte.

Példák félig strukturált adatokra: HTML, CSV fájlok, JavaScript Object Notation (JSON)

## Az adatok forrásai

Az adatforrás az a kezdeti hely, ahol az adat létrejött, vagy ahol "él", és változhat attól függően, hogyan és mikor gyűjtötték. A felhasználók által generált adatok elsődleges adatoknak számítanak, míg a másodlagos adatok olyan forrásból származnak, amely általános használatra gyűjtött adatokat. Például egy esőerdőben megfigyeléseket gyűjtő tudósok csoportja elsődleges adatnak számít, és ha úgy döntenek, hogy megosztják azt más tudósokkal, akkor azok számára másodlagos adatnak minősül.

Az adatbázisok gyakori források, és egy adatbázis-kezelő rendszerre támaszkodnak az adatok tárolására és karbantartására, ahol a felhasználók lekérdezéseknek nevezett parancsokkal fedezik fel az adatokat. A fájlok adatforrásként lehetnek hang-, kép- és videófájlok, valamint táblázatok, mint például az Excel. Az internetes források gyakori helyek az adatok tárolására, ahol adatbázisok és fájlok is megtalálhatók. Az alkalmazásprogramozási interfészek, más néven API-k lehetővé teszik a programozók számára, hogy adatokat osszanak meg külső felhasználókkal az interneten keresztül, míg a webes adatgyűjtés egy weboldalról nyeri ki az adatokat. A [Working with Data leckék](../../../../../../../../../2-Working-With-Data) arra összpontosítanak, hogyan használjuk a különböző adatforrásokat.

## Összegzés

Ebben a leckében megtanultuk:

- Mi az adat
- Hogyan írjuk le az adatokat
- Hogyan osztályozzuk és kategorizáljuk az adatokat
- Hol találhatók az adatok

## 🚀 Kihívás

A Kaggle kiváló forrása a nyílt adathalmazoknak. Használja a [dataset kereső eszközt](https://www.kaggle.com/datasets), hogy találjon néhány érdekes adathalmazt, és osztályozzon 3-5 adathalmazt az alábbi kritériumok szerint:

- Az adatok kvantitatívak vagy kvalitatívak?
- Az adatok strukturáltak, strukturálatlanok vagy félig strukturáltak?

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/5)

## Áttekintés és önálló tanulás

- Ez a Microsoft Learn egység, amelynek címe [Classify your Data](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data), részletesen bemutatja a strukturált, félig strukturált és strukturálatlan adatokat.

## Feladat

[Adathalmazok osztályozása](assignment.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.