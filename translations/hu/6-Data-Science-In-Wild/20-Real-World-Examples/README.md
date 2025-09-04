<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f95679140c7cb39c30ccba535cd8f03f",
  "translation_date": "2025-09-04T22:20:05+00:00",
  "source_file": "6-Data-Science-In-Wild/20-Real-World-Examples/README.md",
  "language_code": "hu"
}
-->
# Adattudomány a való világban

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-RealWorld.png) |
| :--------------------------------------------------------------------------------------------------------------: |
|               Adattudomány a való világban - _Sketchnote by [@nitya](https://twitter.com/nitya)_               |

Már majdnem a tanulási utazás végére értünk!

Az adattudomány és az etika definícióival kezdtük, felfedeztük az adatelemzés és vizualizáció különböző eszközeit és technikáit, áttekintettük az adattudomány életciklusát, valamint megvizsgáltuk, hogyan lehet az adattudományi munkafolyamatokat méretezni és automatizálni felhőalapú szolgáltatásokkal. Most valószínűleg azon gondolkodsz: _"Hogyan tudom mindezt a tanultakat a való világ kontextusába helyezni?"_

Ebben a leckében az adattudomány iparági alkalmazásait vizsgáljuk meg, és konkrét példákat nézünk meg a kutatás, a digitális humán tudományok és a fenntarthatóság területén. Megvizsgáljuk a diákprojektek lehetőségeit, és hasznos forrásokkal zárjuk, amelyek segítenek folytatni a tanulási utadat!

## Előadás előtti kvíz

[Előadás előtti kvíz](https://ff-quizzes.netlify.app/en/ds/)

## Adattudomány + Ipar

Az AI demokratizálásának köszönhetően a fejlesztők számára egyre könnyebb AI-alapú döntéshozatali és adatvezérelt betekintéseket tervezni és integrálni a felhasználói élményekbe és fejlesztési munkafolyamatokba. Íme néhány példa arra, hogyan alkalmazzák az adattudományt a való világ iparági alkalmazásaiban:

 * [Google Flu Trends](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) az adattudományt használta arra, hogy a keresési kifejezéseket összekapcsolja az influenzatrendekkel. Bár a megközelítésnek voltak hibái, felhívta a figyelmet az adatvezérelt egészségügyi előrejelzések lehetőségeire (és kihívásaira).

 * [UPS Routing Predictions](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - bemutatja, hogyan használja a UPS az adattudományt és a gépi tanulást az optimális szállítási útvonalak előrejelzésére, figyelembe véve az időjárási viszonyokat, a forgalmi mintákat, a szállítási határidőket és egyebeket.

 * [NYC Taxicab Route Visualization](http://chriswhong.github.io/nyctaxi/) - az [Információszabadság törvények](https://chriswhong.com/open-data/foil_nyc_taxi/) alapján gyűjtött adatok segítségével vizualizálták egy napot a New York-i taxik életéből, megértve, hogyan navigálnak a forgalmas városban, mennyi pénzt keresnek, és mennyi ideig tartanak az utazások egy 24 órás időszak alatt.

 * [Uber Data Science Workbench](https://eng.uber.com/dsw/) - napi szinten több millió Uber-utazásból gyűjtött adatokat (felvételi és leadási helyek, utazási időtartam, preferált útvonalak stb.) használnak egy adat-elemző eszköz létrehozására, amely segít az árképzésben, a biztonságban, a csalásfelderítésben és a navigációs döntésekben.

 * [Sports Analytics](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - a _prediktív analitikára_ (csapat- és játékoselemzés - gondoljunk csak a [Moneyball](https://datasciencedegree.wisconsin.edu/blog/moneyball-proves-importance-big-data-big-ideas/) példájára - és rajongói menedzsmentre) és az _adatvizualizációra_ (csapat- és rajongói irányítópultok, játékok stb.) összpontosít, olyan alkalmazásokkal, mint a tehetségkutatás, sportfogadás és készlet-/helyszíngazdálkodás.

 * [Adattudomány a banki szektorban](https://data-flair.training/blogs/data-science-in-banking/) - kiemeli az adattudomány értékét a pénzügyi iparban, olyan alkalmazásokkal, mint a kockázatmodellezés és csalásfelderítés, ügyfélszegmentáció, valós idejű előrejelzés és ajánlórendszerek. A prediktív analitika olyan kritikus intézkedéseket is támogat, mint például a [hitelpontszámok](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit).

 * [Adattudomány az egészségügyben](https://data-flair.training/blogs/data-science-in-healthcare/) - kiemeli az olyan alkalmazásokat, mint az orvosi képalkotás (pl. MRI, röntgen, CT-vizsgálat), genomika (DNS-szekvenálás), gyógyszerfejlesztés (kockázatértékelés, siker előrejelzés), prediktív analitika (betegellátás és ellátási logisztika), betegségkövetés és megelőzés stb.

![Adattudomány alkalmazásai a való világban](../../../../6-Data-Science-In-Wild/20-Real-World-Examples/images/data-science-applications.png) Kép forrása: [Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

A fenti ábra más területeket és példákat is bemutat az adattudományi technikák alkalmazására. Szeretnél további alkalmazásokat felfedezni? Nézd meg az alábbi [Áttekintés és önálló tanulás](../../../../6-Data-Science-In-Wild/20-Real-World-Examples) részt.

## Adattudomány + Kutatás

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Research.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Adattudomány és Kutatás - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

Míg a való világ alkalmazásai gyakran az ipari felhasználási esetekre összpontosítanak, a _kutatási_ alkalmazások és projektek két szempontból is hasznosak lehetnek:

* _innovációs lehetőségek_ - fejlett koncepciók gyors prototípusának kidolgozása és a következő generációs alkalmazások felhasználói élményének tesztelése.
* _telepítési kihívások_ - az adattudományi technológiák potenciális káros hatásainak vagy nem szándékos következményeinek vizsgálata a való világ kontextusában.

A diákok számára ezek a kutatási projektek tanulási és együttműködési lehetőségeket kínálhatnak, amelyek javíthatják a téma megértését, és szélesíthetik a releváns emberekkel vagy csapatokkal való kapcsolatteremtést az érdeklődési területeken. De hogyan néznek ki ezek a kutatási projektek, és milyen hatást gyakorolhatnak?

Nézzünk meg egy példát - az [MIT Gender Shades Study](http://gendershades.org/overview.html) projektet Joy Buolamwini (MIT Media Labs) vezetésével, amelyhez egy [jelentős kutatási tanulmány](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf) is kapcsolódik, Timnit Gebru (akkoriban a Microsoft Research-nél) társszerzőként. A kutatás célja:

 * **Mi:** A kutatási projekt célja az volt, hogy _értékelje az automatizált arcelemző algoritmusok és adathalmazok elfogultságát_ nem és bőrtípus alapján.
 * **Miért:** Az arcelemzést olyan területeken használják, mint a bűnüldözés, repülőtéri biztonság, toborzási rendszerek stb. - olyan kontextusokban, ahol a pontatlan osztályozások (pl. elfogultság miatt) gazdasági és társadalmi károkat okozhatnak az érintett egyéneknek vagy csoportoknak. Az elfogultság megértése (és megszüntetése vagy enyhítése) kulcsfontosságú a használat méltányosságának biztosításához.
 * **Hogyan:** A kutatók felismerték, hogy a meglévő referenciaértékek túlnyomórészt világosabb bőrű alanyokat használtak, és egy új adathalmazt (1000+ kép) állítottak össze, amely _kiegyensúlyozottabb_ volt nem és bőrtípus szerint. Az adathalmazt három nemi osztályozási termék (Microsoft, IBM és Face++) pontosságának értékelésére használták.

Az eredmények azt mutatták, hogy bár az általános osztályozási pontosság jó volt, észrevehető különbség volt a hibaarányok között a különböző alcsoportok esetében - a **téves nemi besorolás** magasabb volt a nők vagy sötétebb bőrtípusú személyek esetében, ami elfogultságra utalt.

**Fő eredmények:** Felhívta a figyelmet arra, hogy az adattudománynak _reprezentatívabb adathalmazokra_ (kiegyensúlyozott alcsoportok) és _inkluzívabb csapatokra_ (sokszínű háttérrel) van szüksége, hogy az ilyen elfogultságokat korábban felismerjék és megszüntessék vagy enyhítsék az AI megoldásokban. Az ilyen kutatási erőfeszítések számos szervezet számára alapvetőek az _etikus AI_ elveinek és gyakorlatainak meghatározásában, hogy javítsák a méltányosságot AI termékeik és folyamataik során.

**Szeretnél többet megtudni a Microsoft releváns kutatási erőfeszítéseiről?**

* Nézd meg a [Microsoft Research Projects](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project) mesterséges intelligenciával kapcsolatos projektjeit.
* Fedezd fel a [Microsoft Research Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/) diákprojektjeit.
* Nézd meg a [Fairlearn](https://fairlearn.org/) projektet és a [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) kezdeményezéseket.

## Adattudomány + Humán tudományok

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Adattudomány és Digitális Humán Tudományok - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

A Digitális Humán Tudományokat [úgy definiálták](https://digitalhumanities.stanford.edu/about-dh-stanford), mint "egy gyakorlatok és megközelítések gyűjteményét, amely a számítógépes módszereket ötvözi a humán tudományos kutatással". A [Stanford projektek](https://digitalhumanities.stanford.edu/projects), mint például a _"történelem újraindítása"_ és a _"költői gondolkodás"_ bemutatják a kapcsolatot a [Digitális Humán Tudományok és az Adattudomány](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science) között - hangsúlyozva az olyan technikákat, mint a hálózatelemzés, információvizualizáció, térbeli és szövegelemzés, amelyek segíthetnek új betekintéseket és perspektívákat nyerni történelmi és irodalmi adathalmazokból.

*Szeretnél egy projektet felfedezni és továbbfejleszteni ezen a területen?*

Nézd meg az ["Emily Dickinson és a hangulat metrumának elemzése"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671) projektet - egy nagyszerű példát [Jen Looper](https://twitter.com/jenlooper) munkájából, amely azt vizsgálja, hogyan használhatjuk az adattudományt ismert költészet újraértelmezésére és az író hozzájárulásainak új kontextusban való értékelésére. Például, _meg tudjuk-e jósolni, hogy egy vers melyik évszakban íródott a hangulatának vagy érzelmi tónusának elemzése alapján_ - és mit árul el ez az író lelkiállapotáról az adott időszakban?

A kérdés megválaszolásához kövessük az adattudományi életciklus lépéseit:
 * [`Adatgyűjtés`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#acquiring-the-dataset) - releváns adathalmaz gyűjtése elemzéshez. Lehetőségek közé tartozik egy API használata (pl. [Poetry DB API](https://poetrydb.org/index.html)) vagy weboldalak adatainak lekaparása (pl. [Project Gutenberg](https://www.gutenberg.org/files/12242/12242-h/12242-h.htm)) olyan eszközökkel, mint a [Scrapy](https://scrapy.org/).
 * [`Adattisztítás`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#clean-the-data) - magyarázat arra, hogyan lehet a szöveget formázni, tisztítani és egyszerűsíteni alapvető eszközökkel, mint a Visual Studio Code és a Microsoft Excel.
 * [`Adatelemzés`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#working-with-the-data-in-a-notebook) - magyarázat arra, hogyan importálhatjuk az adathalmazt "Notebookokba" elemzés céljából Python csomagok (mint a pandas, numpy és matplotlib) használatával az adatok rendszerezésére és vizualizálására.
 * [`Érzelemelemzés`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#sentiment-analysis-using-cognitive-services) - magyarázat arra, hogyan integrálhatunk felhőszolgáltatásokat, mint például a Text Analytics, alacsony kódú eszközökkel, mint a [Power Automate](https://flow.microsoft.com/en-us/) az automatizált adatfeldolgozási munkafolyamatokhoz.

Ezzel a munkafolyamattal felfedezhetjük az évszakok hatását a versek érzelmi tónusára, és segíthetünk saját perspektívánk kialakításában az íróról. Próbáld ki magad - majd bővítsd a notebookot, hogy más kérdéseket tegyél fel, vagy új módokon vizualizáld az adatokat!

> Használhatod a [Digitális Humán Tudományok eszközkészletének](https://github.com/Digital-Humanities-Toolkit) néhány eszközét, hogy folytasd ezeket a kutatásokat.

## Adattudomány + Fenntarthatóság

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Sustainability.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Adattudomány és Fenntarthatóság - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

A [2030-as Fenntartható Fejlődési Agenda](https://sdgs.un.org/2030agenda) - amelyet az Egyesült Nemzetek minden tagja elfogadott 2015-ben - 17 célt azonosít, köztük olyanokat, amelyek a **bolygó védelmére** összpontosítanak a degradációtól és az éghajlatváltozás hatásaitól. A [Microsoft Fenntarthatósági](https://www.microsoft.com/en-us/sustainability)
**A Planetary Computer Project jelenleg előzetes fázisban van (2021 szeptemberétől)** - íme, hogyan kezdheted el hozzájárulásodat a fenntarthatósági megoldásokhoz adattudomány segítségével.

* [Kérj hozzáférést](https://planetarycomputer.microsoft.com/account/request), hogy elkezdhesd a felfedezést és kapcsolatba léphess másokkal.
* [Fedezd fel a dokumentációt](https://planetarycomputer.microsoft.com/docs/overview/about), hogy megértsd a támogatott adatállományokat és API-kat.
* Fedezz fel alkalmazásokat, mint például az [Ecosystem Monitoring](https://analytics-lab.org/ecosystemmonitoring/), hogy inspirációt nyerj alkalmazási ötletekhez.

Gondolkodj azon, hogyan használhatod az adatvizualizációt arra, hogy releváns betekintéseket tárj fel vagy erősíts meg olyan területeken, mint a klímaváltozás és az erdőirtás. Vagy gondolkodj azon, hogyan lehet ezeket a betekintéseket új felhasználói élmények létrehozására használni, amelyek viselkedésbeli változásokat motiválnak a fenntarthatóbb élet érdekében.

## Adattudomány + Diákok

Beszéltünk az iparban és kutatásban alkalmazott valós példákról, valamint felfedeztük az adattudomány alkalmazási példáit a digitális humán tudományokban és a fenntarthatóságban. Hogyan fejlesztheted készségeidet és oszthatod meg szakértelmedet adattudomány kezdőként?

Íme néhány példa adattudományi diákprojektekre, amelyek inspirálhatnak.

 * [MSR Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/#!projects) GitHub [projektek](https://github.com/msr-ds3) témákkal, mint például:
    - [Faji elfogultság a rendőri erőszak alkalmazásában](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2019-replicating-an-empirical-analysis-of-racial-differences-in-police-use-of-force/) | [Github](https://github.com/msr-ds3/stop-question-frisk)
    - [A New York-i metró rendszer megbízhatósága](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2018-exploring-the-reliability-of-the-nyc-subway-system/) | [Github](https://github.com/msr-ds3/nyctransit)
 * [Anyagi kultúra digitalizálása: társadalmi-gazdasági eloszlások vizsgálata Sirkapban](https://claremont.maps.arcgis.com/apps/Cascade/index.html?appid=bdf2aef0f45a4674ba41cd373fa23afc) - [Ornella Altunyan](https://twitter.com/ornelladotcom) és csapata Claremontból, [ArcGIS StoryMaps](https://storymaps.arcgis.com/) használatával.

## 🚀 Kihívás

Keress cikkeket, amelyek kezdőbarát adattudományi projekteket ajánlanak - például [ezeket az 50 témakört](https://www.upgrad.com/blog/data-science-project-ideas-topics-beginners/) vagy [ezeket a 21 projektötletet](https://www.intellspot.com/data-science-project-ideas) vagy [ezeket a 16 projektet forráskóddal](https://data-flair.training/blogs/data-science-project-ideas/), amelyeket elemezhetsz és újraalkothatsz. Ne felejtsd el blogolni a tanulási utazásaidról, és oszd meg betekintéseidet velünk.

## Előadás utáni kvíz

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ds/)

## Áttekintés és önálló tanulás

Szeretnél további felhasználási eseteket felfedezni? Íme néhány releváns cikk:
 * [17 adattudományi alkalmazás és példa](https://builtin.com/data-science/data-science-applications-examples) - 2021. július
 * [11 lenyűgöző adattudományi alkalmazás a való világban](https://myblindbird.com/data-science-applications-real-world/) - 2021. május
 * [Adattudomány a való világban](https://towardsdatascience.com/data-science-in-the-real-world/home) - cikkgyűjtemény
 * Adattudomány az alábbi területeken: [Oktatás](https://data-flair.training/blogs/data-science-in-education/), [Mezőgazdaság](https://data-flair.training/blogs/data-science-in-agriculture/), [Pénzügy](https://data-flair.training/blogs/data-science-in-finance/), [Filmek](https://data-flair.training/blogs/data-science-at-movies/) és még sok más.

## Feladat

[Fedezz fel egy Planetary Computer adatállományt](assignment.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.