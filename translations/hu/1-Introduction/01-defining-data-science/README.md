<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2583a9894af7123b2fcae3376b14c035",
  "translation_date": "2025-08-26T15:19:18+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "hu"
}
-->
## Adatelemzés és digitális átalakulás

Az elmúlt évtizedben sok vállalkozás kezdte felismerni az adatok fontosságát az üzleti döntések meghozatalában. Ahhoz, hogy az adatelemzés elveit alkalmazni lehessen egy vállalkozás működtetésében, először adatokat kell gyűjteni, azaz az üzleti folyamatokat digitális formába kell átültetni. Ezt nevezzük **digitalizációnak**. Az adatelemzési technikák alkalmazása ezekre az adatokra jelentős termelékenységnövekedést eredményezhet (vagy akár az üzleti modell átalakítását), amit **digitális átalakulásnak** nevezünk.

Vegyünk egy példát. Tegyük fel, hogy van egy adatelemzési kurzusunk (mint ez), amelyet online módon kínálunk a diákoknak, és szeretnénk adatelemzést alkalmazni annak fejlesztésére. Hogyan tehetjük ezt meg?

Először is feltehetjük a kérdést: "Mit lehet digitalizálni?" A legegyszerűbb mód az lenne, ha mérnénk, mennyi időt vesz igénybe minden diáknak egy-egy modul elvégzése, és a megszerzett tudást egy feleletválasztós teszttel értékelnénk minden modul végén. Az összes diák átlagos modul-elvégzési idejének kiszámításával megtudhatjuk, mely modulok okozzák a legtöbb nehézséget a diákoknak, és dolgozhatunk azok egyszerűsítésén.
> Vitatható, hogy ez a megközelítés nem ideális, mivel a modulok hossza eltérő lehet. Valószínűleg igazságosabb lenne az időt a modul hosszával (karakterek száma alapján) elosztani, és az így kapott értékeket összehasonlítani.
Amikor elkezdjük elemezni a feleletválasztós tesztek eredményeit, megpróbálhatjuk meghatározni, hogy mely fogalmak megértése okoz nehézséget a diákoknak, és ezt az információt felhasználhatjuk a tartalom fejlesztésére. Ehhez úgy kell megterveznünk a teszteket, hogy minden kérdés egy adott fogalomhoz vagy tudáselemhez kapcsolódjon.

Ha még bonyolultabb elemzést szeretnénk végezni, összevethetjük az egyes modulok elvégzéséhez szükséges időt a diákok korcsoportjaival. Lehet, hogy kiderül, hogy bizonyos korcsoportok számára túl hosszú időt vesz igénybe a modul befejezése, vagy hogy a diákok még a modul befejezése előtt abbahagyják. Ez segíthet abban, hogy korosztályi ajánlásokat adjunk a modulhoz, és csökkentsük az emberek elégedetlenségét a téves elvárások miatt.

## 🚀 Kihívás

Ebben a kihívásban megpróbálunk a Data Science területéhez kapcsolódó fogalmakat azonosítani szövegek elemzésével. Egy Wikipedia cikket fogunk használni a Data Science témájában, letöltjük és feldolgozzuk a szöveget, majd készítünk egy szófelhőt, amely így néz ki:

![Szófelhő a Data Science témájában](../../../../translated_images/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.hu.png)

Látogass el a [`notebook.ipynb`](../../../../../../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') fájlhoz, hogy átnézd a kódot. A kódot futtathatod is, és valós időben láthatod, hogyan hajtja végre az adattranszformációkat.

> Ha nem tudod, hogyan kell kódot futtatni egy Jupyter Notebookban, nézd meg [ezt a cikket](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Előadás utáni kvíz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/1)

## Feladatok

* **Feladat 1**: Módosítsd a fenti kódot, hogy az **Big Data** és **Machine Learning** területekhez kapcsolódó fogalmakat azonosítsd.
* **Feladat 2**: [Gondolkodj Data Science forgatókönyveken](assignment.md)

## Köszönetnyilvánítás

Ezt a leckét ♥️-vel készítette [Dmitry Soshnikov](http://soshnikov.com).

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.