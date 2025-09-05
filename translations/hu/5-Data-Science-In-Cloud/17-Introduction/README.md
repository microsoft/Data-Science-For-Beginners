<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-09-05T17:23:29+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "hu"
}
-->
# Bevezetés az adatkutatásba a felhőben

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Adatkutatás a felhőben: Bevezetés - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Ebben a leckében megismerheted a felhő alapelveit, majd megtudhatod, miért lehet érdekes számodra a felhőszolgáltatások használata adatkutatási projektjeid futtatásához. Végül néhány példát is megnézünk, amelyek a felhőben futtatott adatkutatási projekteket mutatnak be.

## [Előadás előtti kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## Mi az a felhő?

A felhő, vagy felhőalapú számítástechnika, az interneten keresztül elérhető, széles körű, igény szerinti számítástechnikai szolgáltatások biztosítása, amelyeket egy infrastruktúra üzemeltet. A szolgáltatások közé tartoznak például a tárhelyek, adatbázisok, hálózatok, szoftverek, analitikai és intelligens szolgáltatások.

Általában megkülönböztetjük a nyilvános, privát és hibrid felhőket az alábbiak szerint:

* Nyilvános felhő: egy harmadik fél által üzemeltetett felhőszolgáltató tulajdonában van, amely számítástechnikai erőforrásait az interneten keresztül a nyilvánosság számára biztosítja.
* Privát felhő: kizárólag egyetlen vállalkozás vagy szervezet által használt felhőalapú számítástechnikai erőforrásokat jelenti, amelyeket egy privát hálózaton üzemeltetnek.
* Hibrid felhő: a hibrid felhő egy olyan rendszer, amely a nyilvános és privát felhőket kombinálja. A felhasználók helyszíni adatközpontot választanak, miközben lehetővé teszik az adatok és alkalmazások futtatását egy vagy több nyilvános felhőben.

A legtöbb felhőalapú számítástechnikai szolgáltatás három kategóriába sorolható: infrastruktúra mint szolgáltatás (IaaS), platform mint szolgáltatás (PaaS) és szoftver mint szolgáltatás (SaaS).

* Infrastruktúra mint szolgáltatás (IaaS): a felhasználók IT-infrastruktúrát bérelnek, például szervereket és virtuális gépeket (VM-eket), tárhelyet, hálózatokat, operációs rendszereket.
* Platform mint szolgáltatás (PaaS): a felhasználók egy környezetet bérelnek szoftveralkalmazások fejlesztéséhez, teszteléséhez, szállításához és kezeléséhez. Nem kell aggódniuk a szerverek, tárhelyek, hálózatok és adatbázisok alapinfrastruktúrájának beállítása vagy kezelése miatt.
* Szoftver mint szolgáltatás (SaaS): a felhasználók igény szerint, általában előfizetéses alapon férnek hozzá szoftveralkalmazásokhoz az interneten keresztül. Nem kell aggódniuk a szoftveralkalmazás üzemeltetése és kezelése, az alapinfrastruktúra vagy a karbantartás, például a szoftverfrissítések és biztonsági javítások miatt.

A legnagyobb felhőszolgáltatók közé tartozik az Amazon Web Services, a Google Cloud Platform és a Microsoft Azure.

## Miért válasszuk a felhőt az adatkutatáshoz?

A fejlesztők és IT-szakemberek számos okból döntenek a felhő használata mellett, többek között az alábbiak miatt:

* Innováció: alkalmazásaidat felhőszolgáltatók által létrehozott innovatív szolgáltatások integrálásával teheted hatékonyabbá.
* Rugalmasság: csak azokat a szolgáltatásokat fizeted, amelyekre szükséged van, és széles körű szolgáltatások közül választhatsz. Általában igény szerint fizetsz, és a szolgáltatásokat az igényeidhez igazíthatod.
* Költségvetés: nem kell kezdeti beruházásokat végezned hardverek és szoftverek vásárlására, helyszíni adatközpontok beállítására és üzemeltetésére, csak azt fizeted, amit használsz.
* Skálázhatóság: az erőforrásaid a projekt igényei szerint skálázhatók, ami azt jelenti, hogy alkalmazásaid több vagy kevesebb számítási kapacitást, tárhelyet és sávszélességet használhatnak, külső tényezőkhöz igazodva bármikor.
* Produktivitás: az üzletedre koncentrálhatsz, ahelyett hogy olyan feladatokkal töltenéd az időt, amelyeket mások is kezelhetnek, például adatközpontok kezelésével.
* Megbízhatóság: a felhőalapú számítástechnika számos módot kínál az adatok folyamatos biztonsági mentésére, és katasztrófa-helyreállítási terveket állíthatsz fel, hogy vállalkozásod és szolgáltatásaid válság idején is működjenek.
* Biztonság: olyan irányelvek, technológiák és ellenőrzések előnyeit élvezheted, amelyek erősítik projekted biztonságát.

Ezek a leggyakoribb okok, amiért sokan a felhőszolgáltatások használata mellett döntenek. Most, hogy jobban megértettük, mi a felhő és mik az előnyei, nézzük meg konkrétabban, hogyan segíthet a felhő az adatkutatók és adatfejlesztők munkájában, valamint az általuk szembesülő kihívások kezelésében:

* Nagy mennyiségű adat tárolása: ahelyett, hogy nagy szervereket vásárolnál, kezelnél és védenél, az adatokat közvetlenül a felhőben tárolhatod, például az Azure Cosmos DB, Azure SQL Database és Azure Data Lake Storage megoldásokkal.
* Adatintegráció végrehajtása: az adatintegráció az adatkutatás alapvető része, amely lehetővé teszi az adatgyűjtésből a cselekvésre való áttérést. A felhőben kínált adatintegrációs szolgáltatásokkal különböző forrásokból származó adatokat gyűjthetsz, alakíthatsz át és integrálhatsz egyetlen adattárházba, például a Data Factory segítségével.
* Adatok feldolgozása: nagy mennyiségű adat feldolgozása jelentős számítási kapacitást igényel, és nem mindenki fér hozzá elég erős gépekhez. Ezért sokan közvetlenül a felhő hatalmas számítási kapacitását használják megoldásaik futtatásához és telepítéséhez.
* Adat-analitikai szolgáltatások használata: felhőszolgáltatások, mint például az Azure Synapse Analytics, Azure Stream Analytics és Azure Databricks segítenek az adatokból cselekvési lehetőségeket nyerni.
* Gépi tanulás és adatintelligencia szolgáltatások használata: ahelyett, hogy mindent a nulláról kezdenél, használhatod a felhőszolgáltató által kínált gépi tanulási algoritmusokat, például az AzureML szolgáltatást. Emellett kognitív szolgáltatásokat is használhatsz, mint például beszéd szöveggé alakítása, szöveg beszéddé alakítása, számítógépes látás és még sok más.

## Példák adatkutatásra a felhőben

Tegyük ezt kézzelfoghatóbbá néhány forgatókönyv bemutatásával.

### Valós idejű közösségi média érzelem-elemzés
Kezdjük egy olyan forgatókönyvvel, amelyet gyakran tanulmányoznak azok, akik gépi tanulással foglalkoznak: valós idejű közösségi média érzelem-elemzés.

Tegyük fel, hogy egy híroldalt üzemeltetsz, és szeretnéd kihasználni az élő adatokat, hogy megértsd, milyen tartalom érdekelheti olvasóidat. Ehhez létrehozhatsz egy programot, amely valós idejű érzelem-elemzést végez a Twitter bejegyzésein, az olvasóid számára releváns témákban.

A kulcsfontosságú mutatók, amelyeket figyelni fogsz, a meghatározott témákhoz (hashtagekhez) kapcsolódó tweetek mennyisége és az érzelem, amelyet analitikai eszközök segítségével állapítanak meg.

A projekt létrehozásához szükséges lépések:

* Hozz létre egy eseményközpontot a bemeneti adatfolyamhoz, amely a Twitter adatait gyűjti.
* Konfiguráld és indítsd el a Twitter kliens alkalmazást, amely a Twitter Streaming API-kat hívja.
* Hozz létre egy Stream Analytics munkát.
* Add meg a munka bemenetét és lekérdezését.
* Hozz létre egy kimeneti tárolót, és add meg a munka kimenetét.
* Indítsd el a munkát.

A teljes folyamat megtekintéséhez nézd meg a [dokumentációt](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Tudományos cikkek elemzése
Vegyünk egy másik példát egy projektre, amelyet [Dmitry Soshnikov](http://soshnikov.com), a tananyag egyik szerzője készített.

Dmitry létrehozott egy eszközt, amely COVID-témájú cikkeket elemez. E projekt áttekintésével láthatod, hogyan hozhatsz létre egy eszközt, amely tudományos cikkekből nyer információkat, betekintést nyújt, és segíti a kutatókat a nagy mennyiségű cikk hatékony kezelésében.

Nézzük meg a projekt különböző lépéseit:
* Információk kinyerése és előfeldolgozása a [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) segítségével.
* Az adatok párhuzamos feldolgozása az [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) használatával.
* Információk tárolása és lekérdezése a [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) segítségével.
* Interaktív irányítópult létrehozása az adatok felfedezéséhez és vizualizációjához a Power BI segítségével.

A teljes folyamat megtekintéséhez látogass el [Dmitry blogjára](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Amint látható, számos módon használhatjuk a felhőszolgáltatásokat az adatkutatás elvégzéséhez.

## Lábjegyzet

Források:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Előadás utáni kvíz

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/33)

## Feladat

[Piackutatás](assignment.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.