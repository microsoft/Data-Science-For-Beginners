<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a0516588d172f82f35f7a0d4a001e5d0",
  "translation_date": "2025-09-05T17:37:24+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "hu"
}
-->
## Adatelemzés típusai

Ahogy már említettük, az adatok mindenhol jelen vannak. Csak megfelelő módon kell őket rögzíteni! Hasznos megkülönböztetni a **strukturált** és **nem strukturált** adatokat. Az előbbi általában jól strukturált formában jelenik meg, gyakran táblázatként vagy táblázatok sorozataként, míg az utóbbi csak fájlok gyűjteménye. Néha beszélhetünk **félig strukturált** adatokról is, amelyeknek van valamilyen szerkezete, de az nagyban változhat.

| Strukturált                                                                 | Félig strukturált                                                                                  | Nem strukturált                        |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Emberek listája telefonszámaikkal                                           | Wikipédia oldalak hivatkozásokkal                                                                  | Az Encyclopedia Britannica szövege     |
| Egy épület összes szobájának hőmérséklete minden percben az elmúlt 20 évben | Tudományos cikkek gyűjteménye JSON formátumban szerzőkkel, publikáció dátumával és absztrakttal     | Vállalati dokumentumok fájlmegosztása  |
| Az épületbe belépő emberek életkora és neme                                 | Internetes oldalak                                                                                 | Nyers videófelvétel megfigyelő kamerából |

## Hol találhatók adatok?

Számos lehetséges adatforrás létezik, és lehetetlen lenne mindet felsorolni! Azonban említsünk meg néhány tipikus helyet, ahol adatokat találhatunk:

* **Strukturált**
  - **Internet of Things** (IoT), beleértve különböző szenzorok, például hőmérséklet- vagy nyomásszenzorok adatait, amelyek sok hasznos információt nyújtanak. Például, ha egy irodaház IoT szenzorokkal van felszerelve, automatikusan szabályozhatjuk a fűtést és világítást a költségek minimalizálása érdekében.
  - **Kérdőívek**, amelyeket a felhasználóktól kérünk kitölteni vásárlás után vagy egy weboldal meglátogatása után.
  - **Viselkedéselemzés**, amely például segíthet megérteni, hogy egy felhasználó milyen mélyen merül el egy weboldalon, és miért hagyja el azt.
* **Nem strukturált**
  - **Szövegek**, amelyek gazdag információforrást jelenthetnek, például általános **hangulatpontszámot**, kulcsszavak és szemantikai jelentés kinyerését.
  - **Képek** vagy **videók**. Egy megfigyelő kamera videója felhasználható az útforgalom becslésére, és az emberek tájékoztatására a lehetséges torlódásokról.
  - Webszerver **naplók**, amelyek segítségével megérthetjük, hogy weboldalunk mely oldalait látogatják meg leggyakrabban, és mennyi ideig.
* Félig strukturált
  - **Közösségi hálózatok** gráfjai kiváló adatforrások lehetnek a felhasználók személyiségéről és az információ terjesztésének hatékonyságáról.
  - Ha van egy csomó fényképünk egy buliról, megpróbálhatunk **csoportdinamikai** adatokat kinyerni azáltal, hogy gráfot építünk azokról az emberekről, akik egymással fényképezkedtek.

Ha ismerjük az adatok lehetséges forrásait, gondolkodhatunk különböző forgatókönyveken, ahol az adatelemzési technikák alkalmazhatók a helyzet jobb megértésére és az üzleti folyamatok javítására.

## Mit lehet kezdeni az adatokkal?

Az adatelemzés során az alábbi lépéseket követjük az adatok feldolgozása során:

## Digitalizáció és digitális átalakulás

Az elmúlt évtizedben sok vállalkozás kezdte felismerni az adatok fontosságát az üzleti döntések meghozatalában. Ahhoz, hogy az adatelemzés elveit alkalmazzuk egy vállalkozás működtetésére, először adatokat kell gyűjteni, azaz az üzleti folyamatokat digitális formába kell átültetni. Ezt nevezzük **digitalizációnak**. Az adatelemzési technikák alkalmazása ezekre az adatokra jelentős termelékenységnövekedést (vagy akár üzleti irányváltást) eredményezhet, amit **digitális átalakulásnak** nevezünk.

Vegyünk egy példát. Tegyük fel, hogy van egy adatelemzési kurzusunk (mint ez), amelyet online kínálunk a diákoknak, és szeretnénk adatelemzést alkalmazni annak fejlesztésére. Hogyan tehetjük ezt meg?

Először is feltehetjük a kérdést: "Mit lehet digitalizálni?" A legegyszerűbb mód az lenne, ha mérnénk, mennyi időbe telik minden diáknak egy-egy modul elvégzése, és a megszerzett tudást egy feleletválasztós teszttel mérnénk a modul végén. Az összes diák átlagos modul-elvégzési idejének kiszámításával megtudhatjuk, mely modulok okozzák a legtöbb nehézséget, és dolgozhatunk azok egyszerűsítésén.
> Vitatható, hogy ez a megközelítés nem ideális, mivel a modulok hossza eltérő lehet. Valószínűleg igazságosabb lenne az időt a modul hosszával (karakterek száma alapján) elosztani, és az így kapott értékeket összehasonlítani.
Amikor elkezdjük elemezni a feleletválasztós tesztek eredményeit, megpróbálhatjuk meghatározni, hogy mely fogalmak megértése okoz nehézséget a diákoknak, és ezt az információt felhasználhatjuk a tartalom fejlesztésére. Ehhez úgy kell megterveznünk a teszteket, hogy minden kérdés egy adott fogalomhoz vagy tudáselemhez kapcsolódjon.

Ha még bonyolultabb elemzést szeretnénk végezni, összevethetjük az egyes modulok elvégzéséhez szükséges időt a diákok korcsoportjaival. Lehet, hogy kiderül, hogy bizonyos korcsoportok számára túl hosszú időt vesz igénybe a modul befejezése, vagy hogy a diákok még a modul befejezése előtt lemorzsolódnak. Ez segíthet abban, hogy korosztály-specifikus ajánlásokat adjunk a modulhoz, és csökkentsük az emberek elégedetlenségét a téves elvárások miatt.

## 🚀 Kihívás

Ebben a kihívásban megpróbálunk a Data Science területéhez kapcsolódó fogalmakat azonosítani szövegek elemzésével. Egy Wikipedia-cikket fogunk használni a Data Science témájában, letöltjük és feldolgozzuk a szöveget, majd készítünk egy szófelhőt, amely így néz ki:

![Szófelhő a Data Science-ről](../../../../1-Introduction/01-defining-data-science/images/ds_wordcloud.png)

Látogass el a [`notebook.ipynb`](../../../../../../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') fájlhoz, hogy átnézd a kódot. A kódot futtathatod is, és valós időben láthatod, hogyan hajtja végre az adattranszformációkat.

> Ha nem tudod, hogyan kell kódot futtatni egy Jupyter Notebookban, nézd meg [ezt a cikket](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Feladatok

* **1. feladat**: Módosítsd a fenti kódot, hogy azonosítsd a **Big Data** és **Machine Learning** területeihez kapcsolódó fogalmakat.
* **2. feladat**: [Gondolkodj Data Science forgatókönyveken](assignment.md)

## Köszönetnyilvánítás

Ezt a leckét ♥️-val készítette [Dmitry Soshnikov](http://soshnikov.com).

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.