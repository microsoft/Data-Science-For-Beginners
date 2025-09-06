<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "661dad02c3ac239644d34c1eb51e76f8",
  "translation_date": "2025-09-06T21:28:18+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "hu"
}
-->
# Az adattudomány életciklusa: Elemzés

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Az adattudomány életciklusa: Elemzés - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Előadás előtti kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/28)

Az adatelemzés az adatok életciklusában megerősíti, hogy az adatok képesek megválaszolni a feltett kérdéseket vagy megoldani egy adott problémát. Ez a lépés arra is összpontosíthat, hogy megerősítse, hogy egy modell helyesen foglalkozik-e ezekkel a kérdésekkel és problémákkal. Ez a lecke az Exploratory Data Analysis (EDA) technikáira összpontosít, amelyek segítenek meghatározni az adatok jellemzőit és kapcsolatait, valamint előkészíteni az adatokat a modellezéshez.

Egy példaként szolgáló adatállományt fogunk használni a [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) oldalról, hogy bemutassuk, hogyan alkalmazható ez Python és a Pandas könyvtár segítségével. Ez az adatállomány néhány gyakori szó előfordulását tartalmazza e-mailekben, az e-mailek forrásai anonimak. Használja a [notebookot](notebook.ipynb) ebben a könyvtárban, hogy kövesse a példát.

## Feltáró adatelemzés

Az életciklus gyűjtési fázisában történik az adatok megszerzése, valamint a problémák és kérdések meghatározása, de honnan tudhatjuk, hogy az adatok támogatják-e a kívánt eredményt? 
Emlékezzünk, hogy egy adatelemző a következő kérdéseket teheti fel, amikor adatokat szerez:
-   Van elég adat a probléma megoldásához?
-   Az adatok megfelelő minőségűek ehhez a problémához?
-   Ha további információkat fedezek fel az adatokon keresztül, érdemes-e megfontolni a célok módosítását vagy újradefiniálását?
A feltáró adatelemzés az adatok megismerésének folyamata, amely segíthet megválaszolni ezeket a kérdéseket, valamint azonosítani az adatállománnyal való munka kihívásait. Nézzük meg néhány technikát, amelyeket ennek elérésére használhatunk.

## Adatprofilozás, leíró statisztikák és Pandas
Hogyan értékelhetjük, hogy van-e elegendő adat a probléma megoldásához? Az adatprofilozás összefoglalhatja és általános információkat gyűjthet az adatállományunkról a leíró statisztikák technikáin keresztül. Az adatprofilozás segít megérteni, hogy mi áll rendelkezésünkre, míg a leíró statisztikák segítenek megérteni, hogy mennyi áll rendelkezésünkre.

Néhány korábbi leckében használtuk a Pandas [`describe()` függvényét](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html), amely megadja a darabszámot, maximum és minimum értékeket, átlagot, szórást és kvantiliseket a numerikus adatokon. Az ilyen leíró statisztikák, mint a `describe()` függvény, segíthetnek felmérni, hogy mennyi adatunk van, és szükségünk van-e többre.

## Mintavétel és lekérdezés
Egy nagy adatállomány teljes körű feltárása nagyon időigényes lehet, és általában számítógépre bízzák. Azonban a mintavétel hasznos eszköz az adatok megértéséhez, és lehetővé teszi, hogy jobban megértsük, mi van az adatállományban és mit képvisel. Egy mintával valószínűségi és statisztikai módszereket alkalmazhatunk, hogy általános következtetéseket vonjunk le az adatainkról. Bár nincs meghatározott szabály arra, hogy mennyi adatot kell mintavételezni, fontos megjegyezni, hogy minél több adatot mintavételezünk, annál pontosabb általánosítást tehetünk az adatokkal kapcsolatban. 
A Pandas [`sample()` függvénye](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) lehetővé teszi, hogy megadjuk, hány véletlenszerű mintát szeretnénk kapni és használni.

Az adatok általános lekérdezése segíthet megválaszolni néhány általános kérdést és elméletet, amelyek felmerülhetnek. A mintavétellel ellentétben a lekérdezések lehetővé teszik, hogy irányítást gyakoroljunk és konkrét részekre összpontosítsunk az adatokban, amelyekkel kapcsolatban kérdéseink vannak. 
A Pandas [`query()` függvénye](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) lehetővé teszi, hogy oszlopokat válasszunk ki, és egyszerű válaszokat kapjunk az adatokból a lekért sorokon keresztül.

## Feltárás vizualizációkkal
Nem kell megvárni, amíg az adatok teljesen megtisztítottak és elemzettek, hogy elkezdjük a vizualizációk készítését. Valójában a vizuális ábrázolás már a feltárás során segíthet azonosítani mintákat, kapcsolatokat és problémákat az adatokban. Továbbá, a vizualizációk lehetőséget nyújtanak arra, hogy kommunikáljunk azokkal, akik nem vesznek részt az adatok kezelésében, és alkalmat adhatnak további kérdések megosztására és tisztázására, amelyeket a gyűjtési szakaszban nem tárgyaltak. Tekintse meg a [Vizualizációk szekciót](../../../../../../../../../3-Data-Visualization), hogy többet megtudjon néhány népszerű vizuális feltárási módszerről.

## Feltárás az inkonzisztenciák azonosítására
A lecke összes témája segíthet azonosítani hiányzó vagy inkonzisztens értékeket, de a Pandas biztosít funkciókat ezek ellenőrzésére. Az [isna() vagy isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) ellenőrizheti a hiányzó értékeket. Az adatokban található hiányzó értékek feltárásának egyik fontos része az, hogy megvizsgáljuk, miért kerültek ilyen állapotba. Ez segíthet eldönteni, hogy milyen [lépéseket tegyünk ezek megoldására](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Feladat

[Válaszok keresése](assignment.md)

---

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.