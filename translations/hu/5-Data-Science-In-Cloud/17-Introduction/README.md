<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "408c55cab2880daa4e78616308bd5db7",
  "translation_date": "2025-08-26T16:05:33+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "hu"
}
-->
# Bevezetés az adattudományba a felhőben

|![ Sketchnote készítette: [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Adattudomány a felhőben: Bevezetés - _Sketchnote készítette: [@nitya](https://twitter.com/nitya)_ |


Ebben a leckében megismered a felhő alapelveit, megtudod, miért lehet érdekes számodra a felhőszolgáltatások használata az adattudományi projektjeid futtatásához, és néhány példát is megnézünk a felhőben futtatott adattudományi projektekről. 

## [Előadás előtti kvíz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## Mi az a felhő?

A felhő, vagy felhőalapú számítástechnika, az interneten keresztül elérhető, széles körű, igény szerinti számítástechnikai szolgáltatások biztosítását jelenti. Ezek a szolgáltatások magukban foglalják például a tárhelyet, adatbázisokat, hálózatokat, szoftvereket, analitikát és intelligens szolgáltatásokat.

Általában megkülönböztetjük a nyilvános, privát és hibrid felhőket az alábbiak szerint:

* Nyilvános felhő: egy harmadik fél által üzemeltetett és birtokolt felhőszolgáltatás, amely az interneten keresztül nyújt számítástechnikai erőforrásokat a nyilvánosság számára.
* Privát felhő: kizárólag egyetlen vállalkozás vagy szervezet által használt felhőszolgáltatások és infrastruktúra, amely egy privát hálózaton van fenntartva.
* Hibrid felhő: a hibrid felhő egy olyan rendszer, amely ötvözi a nyilvános és privát felhőket. A felhasználók helyszíni adatközpontot használnak, miközben lehetővé teszik az adatok és alkalmazások futtatását egy vagy több nyilvános felhőben.

A legtöbb felhőalapú számítástechnikai szolgáltatás három kategóriába sorolható: infrastruktúra mint szolgáltatás (IaaS), platform mint szolgáltatás (PaaS) és szoftver mint szolgáltatás (SaaS).

* Infrastruktúra mint szolgáltatás (IaaS): a felhasználók IT-infrastruktúrát bérelnek, például szervereket, virtuális gépeket (VM-eket), tárhelyet, hálózatokat, operációs rendszereket.
* Platform mint szolgáltatás (PaaS): a felhasználók egy környezetet bérelnek szoftveralkalmazások fejlesztéséhez, teszteléséhez, szállításához és kezeléséhez. Nem kell aggódniuk a szerverek, tárhely, hálózat és adatbázisok alapinfrastruktúrájának beállítása vagy kezelése miatt.
* Szoftver mint szolgáltatás (SaaS): a felhasználók igény szerint, általában előfizetéses alapon férhetnek hozzá szoftveralkalmazásokhoz az interneten keresztül. Nem kell foglalkozniuk a szoftveralkalmazás üzemeltetésével és kezelésével, az alapinfrastruktúrával vagy a karbantartással, például a szoftverfrissítésekkel és biztonsági javításokkal.

A legnagyobb felhőszolgáltatók közé tartozik az Amazon Web Services, a Google Cloud Platform és a Microsoft Azure.

## Miért válaszd a felhőt az adattudományhoz?

A fejlesztők és IT-szakemberek számos okból döntenek a felhő használata mellett, többek között az alábbiak miatt:

* Innováció: alkalmazásaidat közvetlenül a felhőszolgáltatók által kínált innovatív szolgáltatások integrálásával teheted erősebbé.
* Rugalmasság: csak azokért a szolgáltatásokért fizetsz, amelyekre szükséged van, és széles körű szolgáltatások közül választhatsz. Általában használat alapján fizetsz, és a szolgáltatásaidat az igényeidhez igazíthatod.
* Költségvetés: nincs szükség kezdeti beruházásokra hardverek és szoftverek vásárlásához, helyszíni adatközpontok beállításához és üzemeltetéséhez, csak azért fizetsz, amit használsz.
* Skálázhatóság: az erőforrásaid a projekted igényeihez igazodva skálázhatók, ami azt jelenti, hogy az alkalmazásaid több vagy kevesebb számítási teljesítményt, tárhelyet és sávszélességet használhatnak, az aktuális külső tényezőkhöz igazodva.
* Produktivitás: az üzletedre koncentrálhatsz, ahelyett, hogy olyan feladatokra pazarolnád az idődet, amelyeket mások is kezelhetnek, például adatközpontok kezelésére.
* Megbízhatóság: a felhőalapú számítástechnika számos módot kínál az adataid folyamatos biztonsági mentésére, és katasztrófa-helyreállítási terveket állíthatsz fel, hogy vállalkozásod és szolgáltatásaid válság idején is működjenek.
* Biztonság: olyan szabályzatokat, technológiákat és ellenőrzéseket vehetsz igénybe, amelyek erősítik a projekted biztonságát.

Ezek a leggyakoribb okok, amiért az emberek a felhőszolgáltatások mellett döntenek. Most, hogy jobban megértettük, mi a felhő és mik az előnyei, nézzük meg konkrétabban, hogyan segítheti a felhő az adattudósok és az adatokkal dolgozó fejlesztők munkáját, és hogyan oldhatja meg az általuk tapasztalt kihívásokat:

* Nagy mennyiségű adat tárolása: ahelyett, hogy nagy szervereket vásárolnál, kezelnél és védenél, közvetlenül a felhőben tárolhatod az adataidat, például az Azure Cosmos DB, Azure SQL Database és Azure Data Lake Storage megoldásokkal.
* Adatintegráció végrehajtása: az adatintegráció az adattudomány alapvető része, amely lehetővé teszi az adatok gyűjtésétől a cselekvésig való átmenetet. A felhőben kínált adatintegrációs szolgáltatásokkal különböző forrásokból származó adatokat gyűjthetsz, alakíthatsz át és integrálhatsz egyetlen adattárházba, például a Data Factory segítségével.
* Adatok feldolgozása: hatalmas mennyiségű adat feldolgozása rengeteg számítási teljesítményt igényel, és nem mindenkinek van hozzáférése elég erős gépekhez, ezért sokan közvetlenül a felhő hatalmas számítási teljesítményét használják megoldásaik futtatásához és telepítéséhez.
* Adat-analitikai szolgáltatások használata: olyan felhőszolgáltatások, mint az Azure Synapse Analytics, Azure Stream Analytics és Azure Databricks segítenek az adataidat cselekvésre alkalmas betekintésekké alakítani.
* Gépi tanulás és adatintelligencia szolgáltatások használata: ahelyett, hogy mindent a nulláról kezdenél, használhatod a felhőszolgáltatók által kínált gépi tanulási algoritmusokat, például az AzureML szolgáltatást. Emellett használhatsz kognitív szolgáltatásokat is, például beszéd-szöveg átalakítást, szöveg-beszéd átalakítást, számítógépes látást és még sok mást.

## Példák az adattudományra a felhőben

Tegyük ezt kézzelfoghatóbbá néhány forgatókönyv megvizsgálásával.

### Valós idejű közösségi média hangulatelemzés
Kezdjünk egy olyan forgatókönyvvel, amelyet gyakran tanulmányoznak a gépi tanulással ismerkedők: valós idejű közösségi média hangulatelemzés.

Tegyük fel, hogy egy híroldalt üzemeltetsz, és szeretnéd kihasználni az élő adatokat, hogy megértsd, milyen tartalmak érdekelhetik az olvasóidat. Ehhez készíthetsz egy programot, amely valós idejű hangulatelemzést végez a Twitter-bejegyzések adatai alapján, az olvasóid számára releváns témákban.

A kulcsfontosságú mutatók, amelyeket figyelni fogsz, a meghatározott témákhoz (hashtagekhez) kapcsolódó tweetek mennyisége és a hangulat, amelyet az elemző eszközök állapítanak meg a megadott témák körül.

A projekt létrehozásához szükséges lépések a következők:

* Hozz létre egy eseményközpontot a bemeneti adatfolyamhoz, amely a Twitter adatait gyűjti.
* Konfigurálj és indíts el egy Twitter kliensalkalmazást, amely hívja a Twitter Streaming API-kat.
* Hozz létre egy Stream Analytics feladatot.
* Add meg a feladat bemenetét és lekérdezését.
* Hozz létre egy kimeneti tárolót, és add meg a feladat kimenetét.
* Indítsd el a feladatot.

A teljes folyamat megtekintéséhez nézd meg a [dokumentációt](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Tudományos cikkek elemzése
Vegyünk egy másik példát egy projektre, amelyet [Dmitry Soshnikov](http://soshnikov.com), ennek a tananyagnak az egyik szerzője készített.

Dmitry egy olyan eszközt hozott létre, amely COVID-cikkeket elemez. E projekt áttekintésével láthatod, hogyan hozhatsz létre egy olyan eszközt, amely tudást nyer ki tudományos cikkekből, betekintéseket szerez, és segíti a kutatókat a nagy mennyiségű cikk hatékony kezelésében.

Nézzük meg a különböző lépéseket, amelyeket ehhez használtak:
* Információk kinyerése és előfeldolgozása a [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) segítségével.
* Az [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) használata a feldolgozás párhuzamosításához.
* Információk tárolása és lekérdezése a [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) segítségével.
* Interaktív irányítópult létrehozása az adatok felfedezéséhez és vizualizációjához a Power BI segítségével.

A teljes folyamat megtekintéséhez látogasd meg [Dmitry blogját](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Amint láthatod, a felhőszolgáltatások számos módon segíthetnek az adattudományi feladatok elvégzésében.

## Lábjegyzet

Források:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Előadás utáni kvíz

[Előadás utáni kvíz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/33)

## Feladat

[Piackutatás](assignment.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.