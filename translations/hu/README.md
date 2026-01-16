<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7c31d1a22c746b1d0f0582d4f54702ba",
  "translation_date": "2025-12-25T00:09:12+00:00",
  "source_file": "README.md",
  "language_code": "hu"
}
-->
# Adattudomány kezdőknek - Tanterv

[![Megnyitás GitHub Codespaces-ben](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=344191198)

[![GitHub licenc](https://img.shields.io/github/license/microsoft/Data-Science-For-Beginners.svg)](https://github.com/microsoft/Data-Science-For-Beginners/blob/master/LICENSE)
[![GitHub közreműködők](https://img.shields.io/github/contributors/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/graphs/contributors/)
[![GitHub hibajegyek](https://img.shields.io/github/issues/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/issues/)
[![GitHub pull-kérelmek](https://img.shields.io/github/issues-pr/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/pulls/)
[![PR-eket szívesen látunk](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub figyelők](https://img.shields.io/github/watchers/microsoft/Data-Science-For-Beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/Data-Science-For-Beginners/watchers/)
[![GitHub forkok](https://img.shields.io/github/forks/microsoft/Data-Science-For-Beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/Data-Science-For-Beginners/network/)
[![GitHub csillagok](https://img.shields.io/github/stars/microsoft/Data-Science-For-Beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/Data-Science-For-Beginners/stargazers/)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

A Microsoft Azure Cloud Advocates csapata örömmel kínál egy 10 hetes, 20 leckéből álló tananyagot, amely teljes egészében az adattudománnyal foglalkozik. Minden lecke tartalmaz elő- és utóteszteket, írásos útmutatót a lecke elvégzéséhez, megoldást és egy feladatot. Projektalapú pedagógiánk lehetővé teszi, hogy építkezve tanulj, ami bevett módszer az új készségek elsajátítására és rögzítésére.

**Hálás köszönet szerzőinknek:** [Jasmine Greenaway](https://www.twitter.com/paladique), [Dmitry Soshnikov](http://soshnikov.com), [Nitya Narasimhan](https://twitter.com/nitya), [Jalen McGee](https://twitter.com/JalenMcG), [Jen Looper](https://twitter.com/jenlooper), [Maud Levy](https://twitter.com/maudstweets), [Tiffany Souterre](https://twitter.com/TiffanySouterre), [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏 Külön köszönet 🙏 a [Microsoft Student Ambassador](https://studentambassadors.microsoft.com/) szerzőknek, lektoroknak és tartalomközreműködőknek,** különösen Aaryan Arora, [Aditya Garg](https://github.com/AdityaGarg00), [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/), [Ankita Singh](https://www.linkedin.com/in/ankitasingh007), [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/), [Arpita Das](https://www.linkedin.com/in/arpitadas01/), ChhailBihari Dubey, [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor), [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [Majd Safi](https://www.linkedin.com/in/majd-s/), [Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/), [Miguel Correa](https://www.linkedin.com/in/miguelmque/), [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119), [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum), [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/), [Rohit Yadav](https://www.linkedin.com/in/rty2423), Samridhi Sharma, [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200),
[Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/), [Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/), Yogendrasingh Pawar , [Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/), [Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![Sketchnote by @sketchthedocs https://sketchthedocs.dev](../../translated_images/hu/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.png)|
|:---:|
| Adattudomány kezdőknek - _Sketchnote készítette [@nitya](https://twitter.com/nitya)_ |

### 🌐 Többnyelvű támogatás

#### Automatikusan GitHub Action által biztosítva (Automatizált és mindig naprakész)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arab](../ar/README.md) | [Bengáli](../bn/README.md) | [Bolgár](../bg/README.md) | [Burmai (Myanmar)](../my/README.md) | [Kínai (egyszerűsített)](../zh/README.md) | [Kínai (hagyományos, Hongkong)](../hk/README.md) | [Kínai (hagyományos, Macau)](../mo/README.md) | [Kínai (hagyományos, Taiwan)](../tw/README.md) | [Horvát](../hr/README.md) | [Cseh](../cs/README.md) | [Dán](../da/README.md) | [Holland](../nl/README.md) | [Észt](../et/README.md) | [Finn](../fi/README.md) | [Francia](../fr/README.md) | [Német](../de/README.md) | [Görög](../el/README.md) | [Héber](../he/README.md) | [Hindi](../hi/README.md) | [Magyar](./README.md) | [Indonéz](../id/README.md) | [Olasz](../it/README.md) | [Japán](../ja/README.md) | [Kannada](../kn/README.md) | [Koreai](../ko/README.md) | [Litván](../lt/README.md) | [Maláj](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepáli](../ne/README.md) | [Nigériai pidgin](../pcm/README.md) | [Norvég](../no/README.md) | [Perzsa (Farsi)](../fa/README.md) | [Lengyel](../pl/README.md) | [Portugál (Brazília)](../br/README.md) | [Portugál (Portugália)](../pt/README.md) | [Pandzsábi (Gurmukhi)](../pa/README.md) | [Román](../ro/README.md) | [Orosz](../ru/README.md) | [Szerb (cirill)](../sr/README.md) | [Szlovák](../sk/README.md) | [Szlovén](../sl/README.md) | [Spanyol](../es/README.md) | [Szuahéli](../sw/README.md) | [Svéd](../sv/README.md) | [Tagalog (filippínó)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Török](../tr/README.md) | [Ukrajnai](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnami](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Ha további fordítási nyelveket szeretnél támogatni, azok listája megtalálható [itt](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

#### Csatlakozz közösségünkhöz 
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Folyamatban van egy Discord-on futó Learn with AI sorozatunk, további információkért és csatlakozásért látogass el a [Learn with AI Series](https://aka.ms/learnwithai/discord) oldalra 2025. szeptember 18. és 30. között. Tippeket és trükköket kapsz a GitHub Copilot adattudományban való használatához.

![Learn with AI sorozat](../../translated_images/hu/1.2b28cdc6205e26fef6a21817fe5d83ae8b50fbd0a33e9fed0df05845da5b30b6.jpg)

# Diák vagy?

Kezdd a következő forrásokkal:

- [Diák Hub oldal](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) Ez az oldalon kezdő forrásokat, Diákcsomagokat és akár lehetőségeket is találsz ingyenes vizsga utalvány megszerzésére. Érdemes ezt az oldalt könyvjelzővel ellátni és időnként ellenőrizni, mivel legalább havonta frissítjük a tartalmakat.
- [Microsoft Learn Student Ambassadors](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) Csatlakozz a globális diákkövető közösséghez — ez lehet a bejáratod a Microsofthoz.

# Első lépések

## 📚 Dokumentáció

- **[Telepítési útmutató](INSTALLATION.md)** - Lépésről lépésre útmutató a környezet beállításához kezdőknek
- **[Használati útmutató](USAGE.md)** - Példák és gyakori munkafolyamatok
- **[Hibaelhárítás](TROUBLESHOOTING.md)** - Megoldások gyakori problémákra
- **[Közreműködési útmutató](CONTRIBUTING.md)** - Hogyan járulhatsz hozzá ehhez a projekthez
- **[Tanároknak](for-teachers.md)** - Oktatási útmutató és osztálytermi források

## 👨‍🎓 Diákoknak
> **Teljesen kezdők**: Új az adattudományban? Kezdd a [kezdőbarát példáinkkal](examples/README.md)! Ezek az egyszerű, jól kommentált példák segítenek megérteni az alapokat, mielőtt belevágsz a teljes tananyagba.
> **[Diákok](https://aka.ms/student-page)**: ha egyedül szeretnéd használni ezt a tananyagot, fork-old a teljes repót, és végezd el a gyakorlatokat egyedül, kezdve egy előadás előtti kvízzel. Ezután olvasd el az előadást és végezd el a többi feladatot. Próbáld meg a projekteket a leckék megértésével létrehozni ahelyett, hogy egyszerűen lemásolnád a megoldás kódját; ez a kód azonban elérhető a /solutions mappákban minden projektorientált leckénél. Másik ötlet, hogy alakíts tanulócsoportot barátokkal és közösen dolgozzátok végig a tartalmat. További tanuláshoz ajánljuk a [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum) anyagait.

**Gyors kezdés:**
1. Ellenőrizd a [Telepítési útmutatót](INSTALLATION.md) a környezeted beállításához
2. Tekintsd át a [Használati útmutatót](USAGE.md), hogy megtudd, hogyan dolgozz a tananyaggal
3. Kezdd az 1. leckével és haladj sorrendben
4. Csatlakozz a [Discord közösségünkhöz](https://aka.ms/ds4beginners/discord) a támogatásért

## 👩‍🏫 Tanároknak

> **Tanárok**: [tartalmaztunk néhány javaslatot](for-teachers.md) arra vonatkozóan, hogyan használjátok ezt a tananyagot. Szívesen fogadjuk visszajelzéseiteket [a beszélgetési fórumunkon](https://github.com/microsoft/Data-Science-For-Beginners/discussions)!

## Ismerkedj meg a csapattal

[![Bemutató videó](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "Bemutató videó")

**Gif készítője** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)
> 🎥 Kattints a fenti képre a projektről és az azt létrehozó emberekről szóló videóért!

## Pedagógia

Két pedagógiai elvet választottunk ennek a tananyagnak a kialakításakor: biztosítani, hogy projektalapú legyen, és hogy gyakori kvízeket tartalmazzon. A sorozat végére a tanulók megismerik az adattudomány alapelveit, beleértve az etikai fogalmakat, az adatelőkészítést, az adatokkal való különböző munkamódokat, az adatok vizualizálását, az adatelemzést, az adattudomány valós világban alkalmazott eseteit és még sok mást.

Ezen felül egy alacsony tétű kvíz egy óra előtt beállítja a tanuló szándékát egy téma megtanulására, míg egy második kvíz az óra után segíti a megtartást. Ezt a tananyagot rugalmasra és szórakoztatóra terveztük, és egészben vagy részben is elvégezhető. A projektek kis mérettel indulnak és a 10 hetes ciklus végére egyre összetettebbé válnak.

> Tekintsd meg a [Magatartási kódexünket](CODE_OF_CONDUCT.md), a [Hozzájárulási irányelveket](CONTRIBUTING.md) és a [Fordítási irányelveket](TRANSLATIONS.md). Várjuk építő jellegű visszajelzésedet!

## Minden lecke tartalmazza:

- Opcionális sketchnote
- Opcionális kiegészítő videó
- Lecke előtti bemelegítő kvíz
- Írott lecke
- Projektalapú leckékhez lépésről lépésre útmutatók a projekt elkészítéséhez
- Ismeretellenőrzések
- Egy kihívás
- Kiegészítő olvasmány
- Feladat
- [Lecke utáni kvíz](https://ff-quizzes.netlify.app/en/)

> **Egy megjegyzés a kvízekről**: Minden kvíz a Quiz-App mappában található, összesen 40 kvíz három-három kérdéssel. A leckékből vannak linkelve, de a kvízalkalmazás helyileg is futtatható vagy Azure-ra telepíthető; kövesd az utasításokat a `quiz-app` mappában. Fokozatosan lokalizálják őket.

## 🎓 Kezdőbarát példák

**Új az adattudományban?** Létrehoztunk egy külön [példakönyvtárat](examples/README.md) egyszerű, jól kommentált kóddal, hogy segítsünk elkezdeni:

- 🌟 **Hello World** - Az első adattudományi programod
- 📂 **Loading Data** - Tanulj meg adatkészleteket beolvasni és felfedezni
- 📊 **Simple Analysis** - Számíts statisztikákat és találj mintázatokat
- 📈 **Basic Visualization** - Készíts diagramokat és grafikonokat
- 🔬 **Real-World Project** - Teljes munkafolyamat a kezdetektől a befejezésig

Minden példa részletes kommentárokat tartalmaz, amelyek minden lépést elmagyaráznak, így tökéletes a teljesen kezdők számára!

👉 **[Kezdd a példákkal](examples/README.md)** 👈

## Leckék


|![ Sketchnote készítette @sketchthedocs https://sketchthedocs.dev](../../translated_images/hu/00-Roadmap.4905d6567dff47532b9bfb8e0b8980fc6b0b1292eebb24181c1a9753b33bc0f5.png)|
|:---:|
| Adattudomány kezdőknek: Útvonal - _Sketchnote készítette [@nitya](https://twitter.com/nitya)_ |


| Lecke száma | Téma | Lecke csoportja | Tanulási célok | Kapcsolódó lecke | Szerző |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | Az adattudomány meghatározása | [Bevezetés](1-Introduction/README.md) | Ismerd meg az adattudomány alapfogalmait és azt, hogy hogyan kapcsolódik a mesterséges intelligenciához, a gépi tanuláshoz és a big data-hoz. | [lecke](1-Introduction/01-defining-data-science/README.md) [videó](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | Adattudományi etika | [Bevezetés](1-Introduction/README.md) | Az adat-etika fogalmai, kihívásai és keretrendszerei. | [lecke](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | Az adatok meghatározása | [Bevezetés](1-Introduction/README.md) | Hogyan osztályozzák az adatokat és mik az általános forrásaik. | [lecke](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | Bevezetés a statisztikába és a valószínűségszámításba | [Bevezetés](1-Introduction/README.md) | A valószínűség és a statisztika matematikai módszerei az adatok megértéséhez. | [lecke](1-Introduction/04-stats-and-probability/README.md) [videó](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | Relációs adatok kezelése | [Adatok kezelése](2-Working-With-Data/README.md) | Bevezetés a relációs adatokhoz és az alapok a relációs adatok feltárásához és elemzéséhez a Structured Query Language, azaz SQL (kiejtve “see-quell”) segítségével. | [lecke](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | NoSQL adatok kezelése | [Adatok kezelése](2-Working-With-Data/README.md) | Bevezetés a nem relációs adatokhoz, azok különböző típusaihoz és a dokumentumalapú adatbázisok feltárásának és elemzésének alapjaihoz. | [lecke](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | Python használata | [Adatok kezelése](2-Working-With-Data/README.md) | Alapok a Python használatához adatok feltárásához olyan könyvtárakkal, mint a Pandas. Ajánlott az alapvető Python programozási ismeret. | [lecke](2-Working-With-Data/07-python/README.md) [videó](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | Adatelőkészítés | [Adatok kezelése](2-Working-With-Data/README.md) | Témakörök az adattisztításról és átalakításról, hogy kezeljük a hiányos, pontatlan vagy részleges adatokat. | [lecke](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | Mennyiségek vizualizálása | [Adatvizualizáció](3-Data-Visualization/README.md) | Tanuld meg, hogyan használhatod a Matplotlibet madáradatok vizualizálásához 🦆 | [lecke](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | Adateloszlások vizualizálása | [Adatvizualizáció](3-Data-Visualization/README.md) | Megfigyelések és trendek vizualizálása egy intervallumban. | [lecke](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | Arányok vizualizálása | [Adatvizualizáció](3-Data-Visualization/README.md) | Diszkrét és csoportosított százalékok vizualizálása. | [lecke](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | Kapcsolatok vizualizálása | [Adatvizualizáció](3-Data-Visualization/README.md) | Kapcsolatok és korrelációk vizualizálása adatkészletek és változóik között. | [lecke](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | Értelmes vizualizációk | [Adatvizualizáció](3-Data-Visualization/README.md) | Technikák és útmutatás, hogy vizualizációid értékesek legyenek a hatékony problémamegoldáshoz és betekintéshez. | [lecke](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | Bevezetés az adattudomány életciklusába | [Életciklus](4-Data-Science-Lifecycle/README.md) | Bevezetés az adattudomány életciklusába és annak első lépéseként az adatok megszerzésébe és kinyerésébe. | [lecke](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | Elemzés | [Életciklus](4-Data-Science-Lifecycle/README.md) | Az adattudomány életciklusának ez a szakasza az adatok elemzésére fókuszál. | [lecke](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | Kommunikáció | [Életciklus](4-Data-Science-Lifecycle/README.md) | Az adattudomány életciklusának ez a szakasza az adatokból származó eredmények bemutatására összpontosít úgy, hogy a döntéshozók számára könnyebb legyen megérteni azokat. | [lecke](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | Adattudomány a felhőben | [Felhőadatok](5-Data-Science-In-Cloud/README.md) | Ez a lecke sorozat bevezeti az adattudományt a felhőben és annak előnyeit. | [lecke](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 18 | Adattudomány a felhőben | [Felhőadatok](5-Data-Science-In-Cloud/README.md) | Modellek betanítása Low Code eszközökkel. |[lecke](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 19 | Adattudomány a felhőben | [Felhőadatok](5-Data-Science-In-Cloud/README.md) | Modellek telepítése Azure Machine Learning Studio-val. | [lecke](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 20 | Adattudomány a gyakorlatban | [A gyakorlatban](6-Data-Science-In-Wild/README.md) | Adattudomány által vezérelt projektek a való világban. | [lecke](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

Kövesd az alábbi lépéseket a minta Codespace-ben való megnyitásához:
1. Kattints a Code legördülő menüre, és válaszd az Open with Codespaces opciót.
2. A panel alján válaszd a + New codespace lehetőséget.
For more info, check out the [GitHub documentation](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace).

## VSCode Remote - Containers
Kövesd ezeket a lépéseket a repó konténerben való megnyitásához a helyi gépedet és VSCode-ot használva, a VS Code Remote - Containers bővítmény segítségével:

1. Ha ez az első alkalom, hogy fejlesztői konténert használsz, győződj meg róla, hogy a rendszered megfelel az előfeltételeknek (pl. Docker telepítve van) a [kezdő dokumentációban](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started).

To use this repository, you can either open the repository in an isolated Docker volume:

**Note**: Under the hood, this will use the Remote-Containers: **Clone Repository in Container Volume...** command to clone the source code in a Docker volume instead of the local filesystem. [Volumes](https://docs.docker.com/storage/volumes/) are the preferred mechanism for persisting container data.

Or open a locally cloned or downloaded version of the repository:

- Klónozd ezt a repót a helyi fájlrendszeredre.
- Nyomd meg az F1-et és válaszd a **Remote-Containers: Open Folder in Container...** parancsot.
- Válaszd ki a mappa klónozott példányát, várd meg, amíg elindul a konténer, és próbáld ki.

## Offline access

Ezt a dokumentációt offline is futtathatod a [Docsify](https://docsify.js.org/#/) használatával. Forkold ezt a repót, telepítsd a [Docsify-t](https://docsify.js.org/#/quickstart) a helyi gépedre, majd a repó gyökérmappájában írd be `docsify serve`. A weboldal a localhost 3000-es portján lesz elérhető: `localhost:3000`.

> Megjegyzés: a jegyzetfüzetek (notebookok) nem lesznek renderelve a Docsify-val, ezért ha futtatni kell egy notebookot, azt külön tedd meg VS Code-ban Python kernel használatával.

## Egyéb tananyagok

Csapatunk más tananyagokat is készít! Nézd meg:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD kezdőknek](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI kezdőknek](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP kezdőknek](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI ügynökök kezdőknek](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatív AI sorozat
[![Generatív AI kezdőknek](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Alapvető tananyagok
[![Gépi tanulás kezdőknek](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Adattudomány kezdőknek](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![Mesterséges intelligencia kezdőknek](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kiberbiztonság kezdőknek](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webfejlesztés kezdőknek](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT kezdőknek](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR fejlesztés kezdőknek](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot sorozat
[![Copilot AI páros programozáshoz](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET-hez](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot kaland](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Segítség

**Problémák merültek fel?** Nézze meg a [Hibaelhárítási útmutatót](TROUBLESHOOTING.md) a gyakori problémák megoldásaiért.

Ha elakad, vagy kérdése van az AI-alkalmazások fejlesztésével kapcsolatban. Csatlakozzon más tanulókhoz és tapasztalt fejlesztőkhöz az MCP-vel kapcsolatos beszélgetésekben. Ez egy támogató közösség, ahol a kérdések szívesen látottak és a tudás szabadon megosztott.

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ha termék-visszajelzése vagy hibák merülnek fel a fejlesztés közben, látogasson el ide:

[![Microsoft Foundry Fejlesztői Fórum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Felelősségkizárás:
Ez a dokumentum az AI fordítószolgáltatás (Co-op Translator: https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti, anyanyelvi dokumentum tekintendő irányadónak. Kritikus fontosságú információk esetén emberi, szakmai fordítást javaslunk. Nem vállalunk felelősséget az e fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->