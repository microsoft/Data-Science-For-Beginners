<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a0556b17de4c8d1a9470b02247b01d4",
  "translation_date": "2025-09-04T22:07:08+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "hu"
}
-->
# Bevezetés az adatkutatásba a felhőben

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Adatkutatás a felhőben: Bevezetés - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Ebben a leckében megismerheted a felhő alapvető elveit, majd megtudhatod, miért lehet érdekes számodra a felhőszolgáltatások használata adatkutatási projektjeid futtatásához. Végül néhány példát nézünk meg az adatkutatási projektekről, amelyeket a felhőben futtatnak.

## [Előadás előtti kvíz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## Mi az a felhő?

A felhő, vagy felhőalapú számítástechnika, az interneten keresztül elérhető, fizetés-alapú számítástechnikai szolgáltatások széles skálájának biztosítása egy infrastruktúrán keresztül. A szolgáltatások közé tartoznak például a tárolás, adatbázisok, hálózatok, szoftverek, analitika és intelligens szolgáltatások.

Általában megkülönböztetjük a nyilvános, privát és hibrid felhőket az alábbiak szerint:

* Nyilvános felhő: egy harmadik fél által üzemeltetett felhőszolgáltató tulajdonában van, amely számítástechnikai erőforrásait az interneten keresztül a nyilvánosság számára biztosítja.
* Privát felhő: kizárólag egyetlen vállalkozás vagy szervezet által használt felhőszámítástechnikai erőforrásokat jelenti, amelyeket egy privát hálózaton tartanak fenn.
* Hibrid felhő: a hibrid felhő egy olyan rendszer, amely kombinálja a nyilvános és privát felhőket. A felhasználók helyszíni adatközpontot választanak, miközben lehetővé teszik az adatok és alkalmazások futtatását egy vagy több nyilvános felhőben.

A legtöbb felhőszámítástechnikai szolgáltatás három kategóriába sorolható: infrastruktúra mint szolgáltatás (IaaS), platform mint szolgáltatás (PaaS) és szoftver mint szolgáltatás (SaaS).

* Infrastruktúra mint szolgáltatás (IaaS): a felhasználók IT-infrastruktúrát bérelnek, például szervereket és virtuális gépeket (VM-eket), tárolást, hálózatokat, operációs rendszereket.
* Platform mint szolgáltatás (PaaS): a felhasználók környezetet bérelnek szoftveralkalmazások fejlesztéséhez, teszteléséhez, szállításához és kezeléséhez. Nem kell aggódniuk a szerverek, tárolás, hálózat és adatbázisok alapinfrastruktúrájának beállítása vagy kezelése miatt.
* Szoftver mint szolgáltatás (SaaS): a felhasználók interneten keresztül, igény szerint és általában előfizetéses alapon férnek hozzá szoftveralkalmazásokhoz. Nem kell aggódniuk a szoftveralkalmazás üzemeltetése és kezelése, az alapinfrastruktúra vagy a karbantartás, például a szoftverfrissítések és biztonsági javítások miatt.

A legnagyobb felhőszolgáltatók közé tartozik az Amazon Web Services, a Google Cloud Platform és a Microsoft Azure.

## Miért válasszuk a felhőt az adatkutatáshoz?

A fejlesztők és IT-szakemberek számos okból döntenek a felhő használata mellett, többek között az alábbiak miatt:

* Innováció: az alkalmazásaidat közvetlenül a felhőszolgáltatók által létrehozott innovatív szolgáltatások integrálásával támogathatod.
* Rugalmasság: csak azokért a szolgáltatásokért fizetsz, amelyekre szükséged van, és széles szolgáltatási skálából választhatsz. Általában fizetsz, ahogy használod, és a szolgáltatásaidat az igényeidhez igazíthatod.
* Költségvetés: nem kell kezdeti beruházásokat tenni hardverek és szoftverek vásárlására, helyszíni adatközpontok beállítására és működtetésére, csak azért fizetsz, amit használsz.
* Skálázhatóság: az erőforrásaid a projekted igényei szerint skálázhatók, ami azt jelenti, hogy az alkalmazásaid több vagy kevesebb számítástechnikai kapacitást, tárolást és sávszélességet használhatnak, külső tényezőkhöz igazodva bármikor.
* Produktivitás: az üzletedre koncentrálhatsz, ahelyett hogy olyan feladatokra pazarolnád az időt, amelyeket mások is kezelhetnek, például adatközpontok kezelésére.
* Megbízhatóság: a felhőszámítástechnika számos módot kínál az adataid folyamatos biztonsági mentésére, és katasztrófa-helyreállítási terveket állíthatsz fel, hogy az üzleted és szolgáltatásaid válság idején is működjenek.
* Biztonság: olyan szabályzatokat, technológiákat és ellenőrzéseket vehetsz igénybe, amelyek erősítik a projekted biztonságát.

Ezek a leggyakoribb okok, amiért az emberek a felhőszolgáltatások használata mellett döntenek. Most, hogy jobban megértettük, mi a felhő és mik az előnyei, nézzük meg konkrétabban az adatkutatással foglalkozó tudósok és fejlesztők munkáját, és azt, hogyan segíthet nekik a felhő az általuk tapasztalt kihívások kezelésében:

* Nagy mennyiségű adat tárolása: ahelyett, hogy nagy szervereket vásárolnál, kezelnél és védenél, az adataidat közvetlenül a felhőben tárolhatod, olyan megoldásokkal, mint az Azure Cosmos DB, Azure SQL Database és Azure Data Lake Storage.
* Adatintegráció végrehajtása: az adatintegráció az adatkutatás alapvető része, amely lehetővé teszi az adatgyűjtésből a cselekvésre való áttérést. A felhőben kínált adatintegrációs szolgáltatásokkal különböző forrásokból származó adatokat gyűjthetsz, alakíthatsz át és integrálhatsz egyetlen adattárházba, például a Data Factory segítségével.
* Adatok feldolgozása: nagy mennyiségű adat feldolgozása sok számítástechnikai kapacitást igényel, és nem mindenki fér hozzá elég erős gépekhez ehhez. Ezért sokan közvetlenül a felhő hatalmas számítástechnikai kapacitását használják megoldásaik futtatására és telepítésére.
* Adatanalitika szolgáltatások használata: olyan felhőszolgáltatások, mint az Azure Synapse Analytics, Azure Stream Analytics és Azure Databricks segítenek abban, hogy az adataidból cselekvésre alkalmas betekintéseket nyerj.
* Gépi tanulás és adatintelligencia szolgáltatások használata: ahelyett, hogy nulláról kezdenéd, használhatod a felhőszolgáltató által kínált gépi tanulási algoritmusokat, például az AzureML szolgáltatást. Emellett használhatsz kognitív szolgáltatásokat, mint például beszéd szöveggé alakítása, szöveg beszéddé alakítása, számítógépes látás és még sok más.

## Példák adatkutatásra a felhőben

Tegyük ezt kézzelfoghatóbbá néhány forgatókönyv bemutatásával.

### Valós idejű közösségi média érzelem-elemzés
Kezdjünk egy olyan forgatókönyvvel, amelyet gyakran tanulmányoznak azok, akik gépi tanulással foglalkoznak: valós idejű közösségi média érzelem-elemzés.

Tegyük fel, hogy egy hírmédia weboldalt üzemeltetsz, és szeretnéd kihasználni az élő adatokat, hogy megértsd, milyen tartalom érdekelheti az olvasóidat. Ehhez létrehozhatsz egy programot, amely valós idejű érzelem-elemzést végez a Twitter publikációk adataiból, az olvasóid számára releváns témákban.

A kulcsfontosságú mutatók, amelyeket figyelni fogsz, a konkrét témákhoz (hashtagekhez) kapcsolódó tweetek mennyisége és az érzelem, amelyet analitikai eszközök határoznak meg az adott témák körül.

A projekt létrehozásához szükséges lépések a következők:

* Hozz létre egy eseményközpontot a bemeneti adatfolyamhoz, amely a Twitter adatait gyűjti.
* Konfiguráld és indítsd el a Twitter kliens alkalmazást, amely hívja a Twitter Streaming API-kat.
* Hozz létre egy Stream Analytics munkát.
* Add meg a munka bemenetét és lekérdezését.
* Hozz létre egy kimeneti tárolót, és add meg a munka kimenetét.
* Indítsd el a munkát.

A teljes folyamat megtekintéséhez nézd meg a [dokumentációt](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Tudományos cikkek elemzése
Vegyünk egy másik példát egy projektre, amelyet [Dmitry Soshnikov](http://soshnikov.com), a tananyag egyik szerzője készített.

Dmitry létrehozott egy eszközt, amely COVID-cikkeket elemez. E projekt áttekintésével láthatod, hogyan hozhatsz létre egy eszközt, amely tudományos cikkekből nyer ki tudást, betekintést nyújt, és segíti a kutatókat a nagy cikkgyűjtemények hatékony navigálásában.

Nézzük meg a különböző lépéseket, amelyeket ehhez használtak:

* Információk kinyerése és előfeldolgozása a [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) segítségével.
* [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) használata a feldolgozás párhuzamosításához.
* Információk tárolása és lekérdezése a [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) segítségével.
* Interaktív irányítópult létrehozása az adatok feltárásához és vizualizációjához a Power BI segítségével.

A teljes folyamat megtekintéséhez látogasd meg [Dmitry blogját](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Amint láthatod, számos módon használhatjuk a felhőszolgáltatásokat adatkutatás végrehajtására.

## Lábjegyzet

Források:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Előadás utáni kvíz

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ds/)

## Feladat

[Piackutatás](assignment.md)

---

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.