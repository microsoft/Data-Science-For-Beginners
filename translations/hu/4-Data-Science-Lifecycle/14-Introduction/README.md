<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "07e12a25d20b8f191e3cb651c27fdb2b",
  "translation_date": "2025-09-06T21:29:06+00:00",
  "source_file": "4-Data-Science-Lifecycle/14-Introduction/README.md",
  "language_code": "hu"
}
-->
# Bevezetés az adattudomány életciklusába

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/14-DataScience-Lifecycle.png)|
|:---:|
| Bevezetés az adattudomány életciklusába - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Előadás előtti kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/26)

Ezen a ponton valószínűleg már rájöttél, hogy az adattudomány egy folyamat. Ez a folyamat öt szakaszra bontható:

- Adatgyűjtés
- Feldolgozás
- Elemzés
- Kommunikáció
- Karbantartás

Ez a lecke az életciklus három részére összpontosít: adatgyűjtés, feldolgozás és karbantartás.

![Az adattudomány életciklusának diagramja](../../../../translated_images/hu/data-science-lifecycle.a1e362637503c4fb0cd5e859d7552edcdb4aa629a279727008baa121f2d33f32.jpg)
> Fotó: [Berkeley School of Information](https://ischoolonline.berkeley.edu/data-science/what-is-data-science/)

## Adatgyűjtés

Az életciklus első szakasza rendkívül fontos, mivel a következő szakaszok erre épülnek. Ez gyakorlatilag két szakasz egyesítése: az adatok megszerzése és a célok, valamint a megoldandó problémák meghatározása.  
A projekt céljainak meghatározása mélyebb kontextust igényel a problémával vagy kérdéssel kapcsolatban. Először meg kell határoznunk és meg kell szereznünk azokat, akiknek a problémáját meg kell oldani. Ezek lehetnek üzleti érdekelt felek vagy a projekt szponzorai, akik segíthetnek azonosítani, hogy ki vagy mi fog profitálni a projektből, valamint hogy mire és miért van szükségük. Egy jól meghatározott cél mérhető és számszerűsíthető kell legyen, hogy elfogadható eredményt lehessen meghatározni.

Kérdések, amelyeket egy adattudós feltehet:
- Megközelítették már korábban ezt a problémát? Mit fedeztek fel?
- Minden érintett érti a célt és a szándékot?
- Van-e bizonytalanság, és hogyan lehet csökkenteni?
- Milyen korlátok vannak?
- Hogyan fog kinézni a végeredmény?
- Mennyi erőforrás (idő, emberi, számítástechnikai) áll rendelkezésre?

Ezután az adatok azonosítása, összegyűjtése, majd végül feltárása következik, amelyek szükségesek a meghatározott célok eléréséhez. Ebben az adatgyűjtési lépésben az adattudósoknak értékelniük kell az adatok mennyiségét és minőségét is. Ez némi adatfeltárást igényel annak megerősítésére, hogy az összegyűjtött adatok támogatják-e a kívánt eredmény elérését.

Kérdések, amelyeket egy adattudós feltehet az adatokkal kapcsolatban:
- Milyen adatok állnak már rendelkezésemre?
- Ki birtokolja ezeket az adatokat?
- Milyen adatvédelmi aggályok vannak?
- Elég adat áll rendelkezésre a probléma megoldásához?
- Az adatok megfelelő minőségűek ehhez a problémához?
- Ha további információkat fedezek fel az adatokon keresztül, érdemes-e megváltoztatni vagy újradefiniálni a célokat?

## Feldolgozás

Az életciklus feldolgozási szakasza az adatokban rejlő minták felfedezésére és modellezésére összpontosít. A feldolgozási szakaszban alkalmazott technikák közül néhány statisztikai módszereket igényel a minták feltárásához. Ez általában fárasztó feladat lenne egy ember számára nagy adathalmaz esetén, ezért számítógépekre támaszkodnak, hogy felgyorsítsák a folyamatot. Ebben a szakaszban az adattudomány és a gépi tanulás is találkozik. Ahogy az első leckében tanultad, a gépi tanulás a modellek építésének folyamata az adatok megértéséhez. A modellek az adatokban lévő változók közötti kapcsolatot reprezentálják, amelyek segítenek az eredmények előrejelzésében.

A szakaszban alkalmazott gyakori technikák az ML kezdőknek szóló tananyagban találhatók. Kövesd a linkeket, hogy többet megtudj róluk:

- [Osztályozás](https://github.com/microsoft/ML-For-Beginners/tree/main/4-Classification): Az adatok kategóriákba rendezése a hatékonyabb felhasználás érdekében.
- [Csoportosítás](https://github.com/microsoft/ML-For-Beginners/tree/main/5-Clustering): Az adatok hasonló csoportokba rendezése.
- [Regresszió](https://github.com/microsoft/ML-For-Beginners/tree/main/2-Regression): A változók közötti kapcsolatok meghatározása az értékek előrejelzéséhez vagy becsléséhez.

## Karbantartás

Az életciklus diagramján látható, hogy a karbantartás az adatgyűjtés és feldolgozás között helyezkedik el. A karbantartás egy folyamatos folyamat, amely az adatok kezelését, tárolását és védelmét foglalja magában a projekt teljes folyamata során, és ezt a projekt egészében figyelembe kell venni.

### Adatok tárolása

Az adatok tárolásának módja és helye befolyásolhatja a tárolás költségeit, valamint az adatok elérésének sebességét. Az ilyen döntéseket valószínűleg nem egy adattudós hozza meg egyedül, de előfordulhat, hogy választásokat kell tennie az adatokkal való munka módjáról a tárolásuk alapján.

Íme néhány modern adat-tárolási rendszer szempontja, amelyek befolyásolhatják ezeket a döntéseket:

**Helyszíni vs távoli vs nyilvános vagy privát felhő**

A helyszíni tárolás azt jelenti, hogy az adatokat saját eszközökön tároljuk, például saját szerveren, amely merevlemezeken tárolja az adatokat, míg a távoli tárolás olyan eszközökre támaszkodik, amelyeket nem birtoklunk, például adatközpontokra. A nyilvános felhő népszerű választás az adatok tárolására, amely nem igényel ismereteket arról, hogy pontosan hol és hogyan tárolják az adatokat, ahol a nyilvános felhő egy egységes alapinfrastruktúrát jelent, amelyet minden felhasználó megoszt. Néhány szervezet szigorú biztonsági szabályzatot követ, amely megköveteli, hogy teljes hozzáféréssel rendelkezzenek az adatok tárolására használt eszközökhöz, és privát felhőt használnak, amely saját felhőszolgáltatásokat biztosít. A felhőben történő adattárolásról többet megtudhatsz a [későbbi leckékben](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/5-Data-Science-In-Cloud).

**Hideg vs forró adatok**

Amikor modelleket tanítasz, előfordulhat, hogy több tanító adatra van szükséged. Ha elégedett vagy a modelleddel, további adatok érkezhetnek, hogy a modell betöltse a célját. Mindenesetre az adatok tárolásának és elérésének költsége növekedni fog, ahogy egyre több adatot halmozol fel. A ritkán használt adatok, az úgynevezett hideg adatok elkülönítése a gyakran elért forró adatoktól olcsóbb adattárolási lehetőséget kínálhat hardveres vagy szoftveres szolgáltatások révén. Ha hideg adatokat kell elérni, az valamivel hosszabb időt vehet igénybe, mint a forró adatok elérése.

### Adatok kezelése

Ahogy az adatokkal dolgozol, előfordulhat, hogy néhány adatot tisztítani kell a [adatelőkészítésről szóló lecke](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/08-data-preparation) során tárgyalt technikák alkalmazásával, hogy pontos modelleket építs. Amikor új adatok érkeznek, ugyanezeket az alkalmazásokat kell használni a minőség következetességének fenntartása érdekében. Néhány projekt automatizált eszközt használ az adatok tisztítására, aggregálására és tömörítésére, mielőtt azokat végleges helyükre helyeznék. Az Azure Data Factory egy példa ezekre az eszközökre.

### Adatok védelme

Az adatok védelmének egyik fő célja annak biztosítása, hogy azok, akik az adatokkal dolgoznak, ellenőrzésük alatt tartsák, hogy mit gyűjtenek, és milyen kontextusban használják fel azokat. Az adatok biztonságban tartása magában foglalja az adatokhoz való hozzáférés korlátozását csak azok számára, akiknek szükségük van rá, a helyi törvények és szabályozások betartását, valamint az etikai normák fenntartását, ahogy azt az [etikai leckében](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/02-ethics) tárgyaltuk.

Íme néhány dolog, amit egy csapat tehet a biztonság érdekében:
- Biztosítsák, hogy minden adat titkosítva legyen
- Tájékoztassák az ügyfeleket arról, hogyan használják fel az adataikat
- Távolítsák el az adatokhoz való hozzáférést azoktól, akik elhagyták a projektet
- Csak bizonyos projekt tagoknak engedélyezzék az adatok módosítását

## 🚀 Kihívás

Az adattudomány életciklusának számos változata létezik, ahol az egyes lépések eltérő neveket és szakaszok számát kaphatják, de ugyanazokat a folyamatokat tartalmazzák, amelyeket ebben a leckében említettünk.

Fedezd fel a [Team Data Science Process életciklust](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/lifecycle) és a [Cross-industry standard process for data mining](https://www.datascience-pm.com/crisp-dm-2/) folyamatot. Nevezz meg 3 hasonlóságot és különbséget a kettő között.

|Team Data Science Process (TDSP)|Cross-industry standard process for data mining (CRISP-DM)|
|--|--|
|![Team Data Science Lifecycle](../../../../translated_images/hu/tdsp-lifecycle2.e19029d598e2e73d5ef8a4b98837d688ec6044fe332c905d4dbb69eb6d5c1d96.png) | ![Data Science Process Alliance Image](../../../../translated_images/hu/CRISP-DM.8bad2b4c66e62aa75278009e38e3e99902c73b0a6f63fd605a67c687a536698c.png) |
| Kép: [Microsoft](https://docs.microsoft.comazure/architecture/data-science-process/lifecycle) | Kép: [Data Science Process Alliance](https://www.datascience-pm.com/crisp-dm-2/) |

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/27)

## Áttekintés és önálló tanulás

Az adattudomány életciklusának alkalmazása több szerepet és feladatot foglal magában, ahol egyesek az egyes szakaszok bizonyos részeire összpontosíthatnak. A Team Data Science Process néhány erőforrást biztosít, amelyek elmagyarázzák, hogy valaki milyen szerepeket és feladatokat láthat el egy projektben.

* [Team Data Science Process szerepek és feladatok](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/roles-tasks)
* [Adattudományi feladatok végrehajtása: feltárás, modellezés és telepítés](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/execute-data-science-tasks)

## Feladat

[Adatkészlet értékelése](assignment.md)

---

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.