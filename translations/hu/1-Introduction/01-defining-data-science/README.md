<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a76ab694b1534fa57981311975660bfe",
  "translation_date": "2025-09-06T12:29:32+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "hu"
}
-->
## Az adatok típusai

Ahogy már említettük, az adatok mindenhol jelen vannak. Csak meg kell találnunk a megfelelő módot, hogy rögzítsük őket! Hasznos megkülönböztetni a **strukturált** és **strukturálatlan** adatokat. Az előbbi általában jól strukturált formában jelenik meg, gyakran táblázatként vagy táblázatok sorozataként, míg az utóbbi csupán fájlok gyűjteménye. Néha beszélhetünk **félig strukturált** adatokról is, amelyek valamilyen szerkezettel rendelkeznek, de ez a szerkezet nagyban változhat.

| Strukturált                                                                 | Félig strukturált                                                                                  | Strukturálatlan                          |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Emberek listája a telefonszámaikkal                                         | Wikipédia oldalak hivatkozásokkal                                                                  | Az Encyclopedia Britannica szövege      |
| Egy épület összes szobájának hőmérséklete minden percben az elmúlt 20 évben | Tudományos cikkek gyűjteménye JSON formátumban szerzőkkel, publikáció dátumával és absztrakttal     | Vállalati dokumentumok fájlmegosztása    |
| Az épületbe belépő emberek életkora és neme                                 | Internetes oldalak                                                                                 | Nyers videófelvétel egy megfigyelő kamerából |

## Honnan szerezhetünk adatokat?

Számos lehetséges adatforrás létezik, és lehetetlen lenne mindet felsorolni! Azonban említsünk meg néhány tipikus helyet, ahonnan adatokat szerezhetünk:

* **Strukturált**
  - **Dolgok Internete** (IoT), beleértve különböző szenzorok, például hőmérséklet- vagy nyomásérzékelők adatait, amelyek sok hasznos információt nyújthatnak. Például, ha egy irodaház IoT szenzorokkal van felszerelve, automatikusan szabályozhatjuk a fűtést és a világítást a költségek minimalizálása érdekében.
  - **Kérdőívek**, amelyeket a felhasználókkal töltetünk ki egy vásárlás vagy egy weboldal meglátogatása után.
  - **Viselkedéselemzés**, amely például segíthet megérteni, hogy a felhasználó milyen mélyen merül el egy weboldalon, és miért hagyja el azt.
* **Strukturálatlan**
  - **Szövegek**, amelyek gazdag információforrást jelenthetnek, például általános **érzelmi pontszámot**, kulcsszavak és szemantikai jelentés kinyerését.
  - **Képek** vagy **videók**. Egy megfigyelő kamera videója például felhasználható az út forgalmának becslésére, és az emberek tájékoztatására a lehetséges dugókról.
  - Webszerver **naplók**, amelyek segítségével megérthetjük, hogy weboldalunk mely oldalait látogatják meg leggyakrabban, és mennyi ideig.
* **Félig strukturált**
  - **Közösségi hálózatok** gráfjai, amelyek nagyszerű adatforrások lehetnek a felhasználók személyiségéről és az információ terjesztésének hatékonyságáról.
  - Ha van egy csomó fényképünk egy partiról, megpróbálhatunk **csoportdinamikai** adatokat kinyerni azáltal, hogy gráfot építünk azokról az emberekről, akik közös képeket készítettek.

Ha ismerjük az adatok különböző lehetséges forrásait, gondolkodhatunk különböző forgatókönyveken, ahol az adattudományi technikák alkalmazhatók a helyzet jobb megértésére és az üzleti folyamatok javítására.

## Mit lehet kezdeni az adatokkal?

Az adattudományban az adatfeldolgozás következő lépéseire összpontosítunk:

Természetesen az adatok jellegétől függően néhány lépés kimaradhat (például, ha az adat már egy adatbázisban van, vagy ha nincs szükség modellképzésre), vagy néhány lépést többször is megismételhetünk (például az adatfeldolgozást).

## Digitalizáció és digitális transzformáció

Az elmúlt évtizedben sok vállalkozás kezdte felismerni az adatok fontosságát az üzleti döntések meghozatalában. Ahhoz, hogy az adattudomány elveit alkalmazzuk egy vállalkozás működtetésére, először adatokat kell gyűjtenünk, azaz az üzleti folyamatokat digitális formába kell önteni. Ezt nevezzük **digitalizációnak**. Az adattudományi technikák alkalmazása ezekre az adatokra, hogy irányítsuk a döntéseket, jelentős termelékenységnövekedéshez (vagy akár üzleti irányváltáshoz) vezethet, amit **digitális transzformációnak** nevezünk.

Vegyünk egy példát. Tegyük fel, hogy van egy adattudományi kurzusunk (mint ez itt), amelyet online tartunk a diákoknak, és szeretnénk adattudományi módszerekkel javítani rajta. Hogyan tehetjük ezt meg?

Kezdhetjük azzal a kérdéssel, hogy "Mit lehet digitalizálni?" A legegyszerűbb mód az lenne, ha mérnénk, mennyi időbe telik minden diáknak befejezni az egyes modulokat, és a megszerzett tudást egy feleletválasztós teszttel mérnénk a modul végén. Az összes diák átlagos modulbefejezési idejét elemezve kideríthetjük, mely modulok okozzák a legtöbb nehézséget, és dolgozhatunk azok egyszerűsítésén.
> Vitatható, hogy ez a megközelítés nem ideális, mivel a modulok hossza eltérő lehet. Valószínűleg igazságosabb lenne az időt a modul hosszával (karakterek száma alapján) elosztani, és az így kapott értékeket összehasonlítani.
Amikor elkezdjük elemezni a feleletválasztós tesztek eredményeit, megpróbálhatjuk meghatározni, hogy mely fogalmak megértése okoz nehézséget a diákoknak, és ezt az információt felhasználhatjuk a tartalom javítására. Ehhez úgy kell megterveznünk a teszteket, hogy minden kérdés egy adott fogalomhoz vagy tudáselemhez kapcsolódjon.

Ha még bonyolultabbá szeretnénk tenni az elemzést, ábrázolhatjuk az egyes modulok elvégzéséhez szükséges időt a diákok korcsoportjai szerint. Kiderülhet például, hogy bizonyos korcsoportok számára aránytalanul hosszú időbe telik a modul elvégzése, vagy hogy a diákok még a befejezés előtt lemorzsolódnak. Ez segíthet abban, hogy korosztály-specifikus ajánlásokat adjunk a modulhoz, és csökkentsük az emberek elégedetlenségét a helytelen elvárások miatt.

## 🚀 Kihívás

Ebben a kihívásban megpróbáljuk azonosítani azokat a fogalmakat, amelyek a Data Science területéhez kapcsolódnak, szövegek elemzésével. Egy Wikipedia-cikket fogunk használni a Data Science-ről, letöltjük és feldolgozzuk a szöveget, majd készítünk egy szófelhőt, például ilyet:

![Szófelhő a Data Science témában](../../../../translated_images/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.hu.png)

Látogass el a [`notebook.ipynb`](../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') fájlhoz, hogy átnézd a kódot. A kódot futtathatod is, és valós időben láthatod, hogyan hajtja végre az adattranszformációkat.

> Ha nem tudod, hogyan kell kódot futtatni egy Jupyter Notebookban, nézd meg [ezt a cikket](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Feladatok

* **1. feladat**: Módosítsd a fenti kódot, hogy megtaláld a **Big Data** és a **Machine Learning** területeihez kapcsolódó fogalmakat.
* **2. feladat**: [Gondolkodj el a Data Science forgatókönyveken](assignment.md)

## Köszönetnyilvánítás

Ezt a leckét ♥️-val készítette [Dmitry Soshnikov](http://soshnikov.com).

---

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.