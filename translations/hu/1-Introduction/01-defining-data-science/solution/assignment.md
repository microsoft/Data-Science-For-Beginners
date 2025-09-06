<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8f79b9c0484c35b4f26e8aec7fc4d56",
  "translation_date": "2025-08-26T15:26:04+00:00",
  "source_file": "1-Introduction/01-defining-data-science/solution/assignment.md",
  "language_code": "hu"
}
-->
# Feladat: Adattudományi Szenáriók

Ebben az első feladatban arra kérünk, hogy gondolj egy valós életbeli folyamatra vagy problémára különböző problématerületeken, és hogyan tudnád javítani azt az adattudományi folyamat segítségével. Gondolj az alábbiakra:

1. Milyen adatokat tudsz gyűjteni?
1. Hogyan gyűjtenéd az adatokat?
1. Hogyan tárolnád az adatokat? Mekkora valószínűleg az adatok mérete?
1. Milyen betekintéseket tudnánk nyerni ezekből az adatokból? Milyen döntéseket tudnánk hozni az adatok alapján?

Próbálj meg három különböző problémát/folyamatot átgondolni, és írd le az egyes pontokat minden problématerületre vonatkozóan.

Íme néhány problématerület és probléma, amelyek segíthetnek az ötletelésben:

1. Hogyan tudnád az adatokat felhasználni a gyermekek iskolai oktatási folyamatának javítására?
1. Hogyan tudnád az adatokat felhasználni a pandémia alatti oltások ellenőrzésére?
1. Hogyan tudnád az adatokat felhasználni annak biztosítására, hogy produktív vagy a munkában?

## Útmutató

Töltsd ki az alábbi táblázatot (ha szükséges, cseréld ki a javasolt problématerületeket saját ötleteidre):

| Problématerület | Probléma | Milyen adatokat gyűjteni | Hogyan tárolni az adatokat | Milyen betekintések/döntések hozhatók | 
|------------------|----------|--------------------------|----------------------------|---------------------------------------|
| Oktatás | Az egyetemen általában alacsony a részvétel az előadásokon, és azt feltételezzük, hogy azok a diákok, akik rendszeresen részt vesznek az előadásokon, általában jobban teljesítenek a vizsgákon. Szeretnénk ösztönözni a részvételt és tesztelni a hipotézist. | A részvételt nyomon követhetjük az osztályban lévő biztonsági kamera által készített képek segítségével, vagy a diákok mobiltelefonjainak bluetooth/wifi címének követésével. A vizsgaadatok már elérhetők az egyetemi adatbázisban. | Ha biztonsági kamera képeit követjük, néhány (5-10) fényképet kell tárolnunk az osztály alatt (strukturálatlan adat), majd mesterséges intelligenciát használunk a diákok arcának azonosítására (az adatokat strukturált formára alakítjuk). | Számíthatjuk az egyes diákok átlagos részvételi adatait, és megnézhetjük, van-e bármilyen korreláció a vizsgaeredményekkel. A korrelációról többet fogunk beszélni a [valószínűség és statisztika](../../04-stats-and-probability/README.md) részben. A diákok részvételének ösztönzése érdekében közzétehetjük a heti részvételi rangsort az iskolai portálon, és díjakat sorsolhatunk ki a legmagasabb részvételi arányúak között. |
| Oltás | | | | |
| Produktivitás | | | | |

> *Csak egy választ adunk példaként, hogy megértsd, mi várható el ebben a feladatban.*

## Értékelési szempontok

Kiemelkedő | Megfelelő | Fejlesztésre szorul
--- | --- | -- |
Az illető képes volt ésszerű adatforrásokat, adat-tárolási módokat és lehetséges döntéseket/betekintéseket azonosítani minden problématerületre | A megoldás egyes aspektusai nem részletesek, az adat-tárolás nem került megvitatásra, legalább 2 problématerület leírásra került | Csak az adatmegoldás egyes részei kerültek leírásra, csak egy problématerületet vettek figyelembe.

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.