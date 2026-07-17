# Adatok meghatározása

|![ Sketchnote készítette: [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Adatok meghatározása - _Sketchnote készítette: [@nitya](https://twitter.com/nitya)_ |

Az adat tények, információk, megfigyelések és mérések, amelyeket felfedezésekhez és megalapozott döntések támogatásához használnak. Egy adatpont egyetlen adat egység egy adatkészleten belül, amely adatpontok gyűjteménye. Az adatkészletek különböző formátumokban és struktúrákban fordulhatnak elő, és általában az alapján alakulnak, hogy honnan származnak vagy honnan származik az adat. Például egy vállalat havi bevételei egy táblázatban lehetnek, míg egy okosóra által mért óránkénti pulzusadat [JSON](https://stackoverflow.com/a/383699) formátumban lehet. Az adatkutatók gyakran dolgoznak különböző típusú adatokkal egy adatkészleten belül.

Ez a lecke az adatok jellemzői és forrásai szerinti azonosítására és osztályozására fókuszál.

## [Előadás előtti kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Hogyan írjuk le az adatokat

### Nyers adatok
A nyers adat az, amely a forrásból annak kezdeti állapotában érkezett, és még nem lett elemezve vagy rendezve. Ahhoz, hogy megértsük, mi történik egy adatkészlettel, azt olyanná kell szervezni, amit az emberek és a technológia is érteni tud, amellyel tovább elemezhető. Az adatkészlet szerkezete meghatározza, hogyan van szervezve, és osztályozható strukturált, strukturálatlan és félig strukturált kategóriákba. Ezek a struktúratípusok forrásonként eltérőek lehetnek, de végső soron ezekbe a három kategóriába sorolhatók.

### Mennyiségi (kvantitatív) adatok
A mennyiségi adat egy adatkészleten belüli numerikus megfigyelés, amely általában elemezhető, mérhető és matematikailag használható. Például egy ország népessége, egy személy magassága vagy egy vállalat negyedéves bevétele. További elemzéssel a mennyiségi adatok segítségével felfedezhetőek az éves légminőségi index (AQI) szezonális trendjei vagy becsülhető a csúcsforgalmi forgalom valószínűsége egy átlagos munkanapon.

### Minőségi (kvalitatív) adatok
A minőségi adat, más néven kategóriális adat olyan adat, amely nem mérhető objektíven, mint a mennyiségi adat. Általában különböző szubjektív formátumok, amelyek valami minőségét ragadják meg, például egy termék vagy folyamat minőségét. Néha a minőségi adat numerikus, de nem hagyományosan matematikailag használatos, például telefonszámok vagy időbélyegek. Példák a minőségi adatra: videókommentárok, egy autó márkája és modellje vagy a legjobb barátaid kedvenc színe. A minőségi adatokat felhasználhatjuk annak megértésére, hogy mely termékeket kedvelik leginkább a fogyasztók vagy azonosítani a népszerű kulcsszavakat álláspályázati önéletrajzokban.

### Strukturált adatok
A strukturált adat sorokba és oszlopokba rendezett adat, ahol minden sor ugyanazt az oszlopkészletet tartalmazza. Az oszlopok egy adott típus értékét képviselik, és egy névvel vannak azonosítva, amely leírja az érték jelentését, míg a sorok az aktuális értékeket tartalmazzák. Az oszlopok általában speciális szabályokkal vagy korlátozásokkal rendelkeznek az értékekre vonatkozóan, hogy biztosítsák, hogy az értékek pontosan tükrözik az oszlopot. Például képzelj el egy ügyfelekről szóló táblázatot, ahol minden sornak rendelkeznie kell telefonszámmal, és a telefonszámok soha nem tartalmaznak betűket. Lehetnek szabályok az adott telefonszám oszlopban, hogy az ne legyen üres és csak számokat tartalmazzon.

A strukturált adat előnye, hogy olyan módon szervezhető, hogy más strukturált adatokkal összekapcsolható legyen. Ugyanakkor, mivel az adat egy adott módon van szervezve, a struktúrájának megváltoztatása sok munkát igényelhet. Például, ha hozzáadunk egy e-mail oszlopot az ügyféltáblázathoz, aminek nem lehet üresnek lennie, akkor ki kell találni, hogyan adjuk hozzá ezen értékeket a meglévő ügyfélsorokhoz az adatkészletben.

Strukturált adatok példái: táblázatok, relációs adatbázisok, telefonszámok, bankszámlakivonatok

### Strukturálatlan adatok
A strukturálatlan adat tipikusan nem sorokba vagy oszlopokba rendezhető, és nem követ formátumot vagy előírt szabályokat. Mivel kevesebb korlátozás van a szerkezetében, könnyebb új információt hozzáadni, mint egy strukturált adatkészlethez képest. Ha például egy szenzor, amely 2 percenként gyűjt adatot a légnyomásról, frissítésként kap egy lehetőséget a hőmérséklet mérésére és rögzítésére is, akkor nem kell módosítani a meglévő adatokat, ha azok strukturálatlanok. Ugyanakkor ez megnehezítheti az adatok elemzését vagy vizsgálatát. Például egy tudós szeretné megtalálni egy hónap átlaghőmérsékletét a szenzoradatokból, de azt találja, hogy a szenzor időnként egy "e" karaktert rögzített a helyett, hogy számadatot jegyezne fel, jelezve, hogy a szenzor meghibásodott, így az adat hiányos.

Strukturálatlan adatok példái: szövegfájlok, szöveges üzenetek, videófájlok

### Félig strukturált adatok
A félig strukturált adat olyan jellemzőkkel rendelkezik, amelyek a strukturált és strukturálatlan adat kombinációját alkotják. Nem jellemző rá, hogy sorokból és oszlopokból áll, de olyan módon szervezett, amely strukturáltnak tekinthető, és követhet állandó formát vagy szabálykészletet. A szerkezet forrásonként változó lehet, például egy jól definiált hierarchia vagy egy rugalmasabb, amely lehetővé teszi új információk egyszerű integrálását. A metaadatok olyan mutatók, amelyek segítenek eldönteni, hogyan van az adat szervezve és tárolva, és különböző neveken ismerhetők az adatok típusától függően. Gyakori metaadat elnevezések: címkék (tags), elemek (elements), entitások (entities) és attribútumok (attributes). Például egy tipikus e-mail üzenetnek van tárgya, törzse és címzettjei, és szervezhető azok szerint, hogy ki vagy mikor küldte.

Félig strukturált adatok példái: HTML, CSV fájlok, JavaScript Object Notation (JSON)

## Az adatok forrásai

Az adatforrás az a kezdeti hely, ahol az adat keletkezett vagy ahol "lakik", és az alapján változhat, hogy hogyan és mikor gyűjtötték. A felhasználó(k) által generált adatokat elsődleges adatnak nevezzük, míg a másodlagos adat olyan forrásból származik, amely általános használatra gyűjtött adatokat. Például egy esőerdőben megfigyeléseket gyűjtő tudósok csoportja elsődleges adatnak számít, és ha úgy döntenek, hogy megosztják más tudósokkal, az másodlagos adatnak minősül azon tudósok számára.

A adatbázisok egy gyakori adatforrás, amelyek adatbázis-kezelő rendszeren keresztül tárolják és kezelik az adatokat, ahol a felhasználók lekérdezéseknek nevezett parancsokkal böngésznek az adatokban. Az adatforrásként szolgáló fájlok lehetnek hang-, kép- és videófájlok, valamint táblázatok, például Excel. Az internetes források is gyakoriak az adatok tárolására, ahol adatbázisokat és fájlokat egyaránt találhatunk. Az alkalmazásprogramozási felületek (API-k) lehetővé teszik a programozók számára, hogy módot teremtsenek az adatok interneten keresztüli külső felhasználóknak történő megosztására, míg a webes adatkinyerés (web scraping) weboldalakról von ki adatokat. A [Working with Data](../../../../../../../../../2-Working-With-Data) leckék arra fókuszálnak, hogyan lehet különböző adatforrásokat használni.

## Összefoglaló

Ebben a leckében megtanultuk:

- Mi az adat
- Hogyan írjuk le az adatokat
- Hogyan osztályozzuk és kategorizáljuk az adatokat
- Hol találhatók meg az adatok

## 🚀 Feladat

A Kaggle egy kiváló forrás nyílt adatkészletekre. Használd a [dataset search tool](https://www.kaggle.com/datasets) eszközt, hogy találj néhány érdekes adatkészletet, és osztályozz 3-5 adatkészletet a következő szempontok szerint:

- Az adatok mennyiségi vagy minőségi jellegűek?
- Az adatok strukturáltak, strukturálatlanok vagy félig strukturáltak?

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Áttekintés és önálló tanulás

- Ez a Microsoft Learn egység, [Identify data formats](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text) részletesen bemutatja a strukturált, félig strukturált és strukturálatlan adatokat.

## Feladat

[Datasets osztályozása](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->