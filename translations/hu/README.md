<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d24976d371de57bb657d3127f4195542",
  "translation_date": "2025-10-03T14:29:14+00:00",
  "source_file": "README.md",
  "language_code": "hu"
}
-->
# Adattudomány kezdőknek - Tanterv

Azure Cloud Advocates a Microsoftnál örömmel kínál egy 10 hetes, 20 leckéből álló tantervet az adattudományról. Minden lecke tartalmaz előzetes és utólagos kvízeket, írásos útmutatót a lecke elvégzéséhez, megoldást és feladatot. Projektalapú pedagógiánk lehetővé teszi, hogy tanulás közben építs, ami bizonyítottan segíti az új készségek elsajátítását.

**Szívből köszönjük szerzőinknek:** [Jasmine Greenaway](https://www.twitter.com/paladique), [Dmitry Soshnikov](http://soshnikov.com), [Nitya Narasimhan](https://twitter.com/nitya), [Jalen McGee](https://twitter.com/JalenMcG), [Jen Looper](https://twitter.com/jenlooper), [Maud Levy](https://twitter.com/maudstweets), [Tiffany Souterre](https://twitter.com/TiffanySouterre), [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏 Külön köszönet 🙏 a [Microsoft Student Ambassador](https://studentambassadors.microsoft.com/) szerzőknek, lektoroknak és tartalomhozzájárulóknak,** különösen Aaryan Arora, [Aditya Garg](https://github.com/AdityaGarg00), [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/), [Ankita Singh](https://www.linkedin.com/in/ankitasingh007), [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/), [Arpita Das](https://www.linkedin.com/in/arpitadas01/), ChhailBihari Dubey, [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor), [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [Majd Safi](https://www.linkedin.com/in/majd-s/), [Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/), [Miguel Correa](https://www.linkedin.com/in/miguelmque/), [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119), [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum), [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/), [Rohit Yadav](https://www.linkedin.com/in/rty2423), Samridhi Sharma, [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200),
[Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/), [Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/), Yogendrasingh Pawar , [Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/), [Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![Sketchnote by @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.hu.png)|
|:---:|
| Adattudomány kezdőknek - _Sketchnote készítette: [@nitya](https://twitter.com/nitya)_ |

### 🌐 Többnyelvű támogatás

#### Támogatott GitHub Action segítségével (Automatikus és mindig naprakész)

[Francia](../fr/README.md) | [Spanyol](../es/README.md) | [Német](../de/README.md) | [Orosz](../ru/README.md) | [Arab](../ar/README.md) | [Perzsa (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Kínai (Egyszerűsített)](../zh/README.md) | [Kínai (Hagyományos, Makaó)](../mo/README.md) | [Kínai (Hagyományos, Hongkong)](../hk/README.md) | [Kínai (Hagyományos, Tajvan)](../tw/README.md) | [Japán](../ja/README.md) | [Koreai](../ko/README.md) | [Hindi](../hi/README.md) | [Bengáli](../bn/README.md) | [Marathi](../mr/README.md) | [Nepáli](../ne/README.md) | [Pandzsábi (Gurmukhi)](../pa/README.md) | [Portugál (Portugália)](../pt/README.md) | [Portugál (Brazília)](../br/README.md) | [Olasz](../it/README.md) | [Lengyel](../pl/README.md) | [Török](../tr/README.md) | [Görög](../el/README.md) | [Thai](../th/README.md) | [Svéd](../sv/README.md) | [Dán](../da/README.md) | [Norvég](../no/README.md) | [Finn](../fi/README.md) | [Holland](../nl/README.md) | [Héber](../he/README.md) | [Vietnámi](../vi/README.md) | [Indonéz](../id/README.md) | [Maláj](../ms/README.md) | [Tagalog (Filippínó)](../tl/README.md) | [Szuahéli](../sw/README.md) | [Magyar](./README.md) | [Cseh](../cs/README.md) | [Szlovák](../sk/README.md) | [Román](../ro/README.md) | [Bolgár](../bg/README.md) | [Szerb (Cirill)](../sr/README.md) | [Horvát](../hr/README.md) | [Szlovén](../sl/README.md) | [Ukrán](../uk/README.md) | [Burmai (Mianmar)](../my/README.md)

**Ha további fordításokat szeretnél, a támogatott nyelvek listája [itt található](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

#### Csatlakozz közösségünkhöz 
[![Azure AI Discord](https://dcbadge.limes.pink/api/server/kzRShWzttr)](https://aka.ms/ds4beginners/discord)

Van egy folyamatban lévő Discord tanulási sorozatunk AI-val, tudj meg többet és csatlakozz hozzánk a [Learn with AI Series](https://aka.ms/learnwithai/discord) eseményen 2025. szeptember 18-30. között. Tippeket és trükköket kapsz a GitHub Copilot használatához az adattudományban.

![Learn with AI sorozat](../../translated_images/1.2b28cdc6205e26fef6a21817fe5d83ae8b50fbd0a33e9fed0df05845da5b30b6.hu.jpg)

# Diák vagy?

Kezdd az alábbi forrásokkal:

- [Student Hub oldal](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) Ezen az oldalon kezdő forrásokat, diákcsomagokat és akár ingyenes tanúsítvány-vouchert is találhatsz. Ez egy olyan oldal, amit érdemes könyvjelzőzni és időnként ellenőrizni, mivel havonta legalább egyszer frissítjük a tartalmat.
- [Microsoft Learn Student Ambassadors](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) Csatlakozz egy globális diák nagyköveti közösséghez, ez lehet az utad a Microsofthoz.

# Kezdés

## 📚 Dokumentáció

- **[Telepítési útmutató](INSTALLATION.md)** - Lépésről lépésre bemutatott beállítási útmutató kezdőknek
- **[Használati útmutató](USAGE.md)** - Példák és gyakori munkafolyamatok
- **[Hibaelhárítás](TROUBLESHOOTING.md)** - Megoldások gyakori problémákra
- **[Hozzájárulási útmutató](CONTRIBUTING.md)** - Hogyan járulhatsz hozzá ehhez a projekthez
- **[Tanároknak](for-teachers.md)** - Oktatási útmutató és osztálytermi források

## 👨‍🎓 Diákoknak
> **Teljesen kezdőknek**: Új vagy az adattudományban? Kezdd a [kezdőbarát példákkal](examples/README.md)! Ezek az egyszerű, jól kommentált példák segítenek megérteni az alapokat, mielőtt belevágnál a teljes tantervbe.
> **[Diákok](https://aka.ms/student-page)**: ha önállóan szeretnéd használni ezt a tantervet, forkolj le az egész repót, és végezd el a gyakorlatokat önállóan, kezdve egy előadás előtti kvízzel. Ezután olvasd el az előadást, és végezd el a többi tevékenységet. Próbáld meg a projekteket úgy létrehozni, hogy megérted a leckéket, ahelyett hogy lemásolnád a megoldási kódot; azonban ez a kód elérhető a /solutions mappákban minden projektorientált leckében. Egy másik ötlet lehet, hogy tanulócsoportot alakítasz barátaiddal, és együtt haladtok a tartalommal. További tanulmányokhoz ajánljuk a [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum) platformot.

**Gyors kezdés:**
1. Nézd meg a [Telepítési útmutatót](INSTALLATION.md) a környezet beállításához
2. Tekintsd át a [Használati útmutatót](USAGE.md), hogy megtanuld, hogyan dolgozz a tantervvel
3. Kezdd az 1. leckével, és haladj sorban
4. Csatlakozz a [Discord közösségünkhöz](https://aka.ms/ds4beginners/discord) támogatásért

## 👩‍🏫 Tanároknak

> **Tanárok**: [néhány javaslatot is mellékeltünk](for-teachers.md) arra vonatkozóan, hogyan használhatjátok ezt a tantervet. Szívesen fogadjuk visszajelzéseiteket [a vitafórumunkon](https://github.com/microsoft/Data-Science-For-Beginners/discussions)!

## Ismerd meg a csapatot

[![Promo videó](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "Promo videó")

**Gif készítette:** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)

> 🎥 Kattints a fenti képre, hogy megnézd a projektet és azokat, akik létrehozták!

## Pedagógia

Két pedagógiai alapelvet választottunk a tanterv kidolgozása során: biztosítani, hogy projektalapú legyen, és hogy gyakori kvízeket tartalmazzon. A sorozat végére a diákok megtanulják az adattudomány alapelveit, beleértve az etikai fogalmakat, az adatok előkészítését, az adatokkal való munka különböző módjait, az adatvizualizációt, az adatelemzést, az adattudomány valós alkalmazásait és még sok mást.
Ezenkívül egy alacsony tétű kvíz az óra előtt segíti a diákokat abban, hogy a tananyag elsajátítására összpontosítsanak, míg egy második kvíz az óra után biztosítja a tanultak jobb megőrzését. Ez a tanterv rugalmas és szórakoztató módon lett kialakítva, és teljes egészében vagy részleteiben is elvégezhető. A projektek kicsiben kezdődnek, és a 10 hetes ciklus végére egyre összetettebbé válnak.

> Találd meg [Magatartási Kódexünket](CODE_OF_CONDUCT.md), [Hozzájárulási](CONTRIBUTING.md), [Fordítási](TRANSLATIONS.md) irányelveinket. Szívesen fogadjuk az építő jellegű visszajelzéseidet!

## Minden lecke tartalmazza:

- Opcionális sketchnote
- Opcionális kiegészítő videó
- Óra előtti bemelegítő kvíz
- Írott lecke
- Projektalapú leckék esetén lépésről lépésre útmutatók a projekt elkészítéséhez
- Tudásellenőrzések
- Egy kihívás
- Kiegészítő olvasmány
- Feladat
- [Óra utáni kvíz](https://ff-quizzes.netlify.app/en/)

> **Megjegyzés a kvízekről**: Az összes kvíz a Quiz-App mappában található, összesen 40 darab, mindegyik három kérdéssel. Ezek a leckékből érhetők el, de a kvízalkalmazás helyileg is futtatható vagy Azure-ra telepíthető; kövesd az `quiz-app` mappában található utasításokat. A kvízeket fokozatosan lokalizáljuk.

## 🎓 Kezdőbarát példák

**Új vagy az adatelemzés világában?** Készítettünk egy különleges [példák könyvtárat](examples/README.md) egyszerű, jól kommentált kódokkal, hogy segítsünk az indulásban:

- 🌟 **Hello World** - Az első adatelemző programod
- 📂 **Adatok betöltése** - Tanuld meg, hogyan olvass és fedezz fel adatállományokat
- 📊 **Egyszerű elemzés** - Számolj statisztikákat és találj mintázatokat
- 📈 **Alapvető vizualizáció** - Készíts diagramokat és grafikonokat
- 🔬 **Valós projekt** - Teljes munkafolyamat az elejétől a végéig

Minden példa részletes kommentárokat tartalmaz, amelyek minden lépést elmagyaráznak, így tökéletesek abszolút kezdők számára!

👉 **[Kezdd a példákkal](examples/README.md)** 👈

## Leckék

|![ Sketchnote by @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Roadmap.4905d6567dff47532b9bfb8e0b8980fc6b0b1292eebb24181c1a9753b33bc0f5.hu.png)|
|:---:|
| Adatelemzés kezdőknek: Útmutató - _Sketchnote készítette: [@nitya](https://twitter.com/nitya)_ |

| Lecke száma | Téma | Leckecsoportosítás | Tanulási célok | Kapcsolódó lecke | Szerző |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | Az adatelemzés meghatározása | [Bevezetés](1-Introduction/README.md) | Ismerd meg az adatelemzés alapfogalmait, és hogy hogyan kapcsolódik a mesterséges intelligenciához, gépi tanuláshoz és a big data-hoz. | [lecke](1-Introduction/01-defining-data-science/README.md) [videó](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | Az adatelemzés etikája | [Bevezetés](1-Introduction/README.md) | Az adatetika fogalmai, kihívásai és keretrendszerei. | [lecke](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | Az adatok meghatározása | [Bevezetés](1-Introduction/README.md) | Hogyan osztályozzuk az adatokat és mik a leggyakoribb forrásaik. | [lecke](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | Bevezetés a statisztikába és valószínűségszámításba | [Bevezetés](1-Introduction/README.md) | A statisztika és valószínűségszámítás matematikai technikái az adatok megértéséhez. | [lecke](1-Introduction/04-stats-and-probability/README.md) [videó](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | Relációs adatok kezelése | [Adatok kezelése](2-Working-With-Data/README.md) | Bevezetés a relációs adatokba, valamint az SQL (Structured Query Language) alapjainak megismerése. | [lecke](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | NoSQL adatok kezelése | [Adatok kezelése](2-Working-With-Data/README.md) | Bevezetés a nem relációs adatokba, azok különböző típusaiba, valamint a dokumentumadatbázisok felfedezésének és elemzésének alapjaiba. | [lecke](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | Python használata | [Adatok kezelése](2-Working-With-Data/README.md) | A Python alapjai az adatok felfedezéséhez, például a Pandas könyvtár használatával. Alapvető Python programozási ismeretek ajánlottak. | [lecke](2-Working-With-Data/07-python/README.md) [videó](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | Adatok előkészítése | [Adatok kezelése](2-Working-With-Data/README.md) | Az adatok tisztításának és átalakításának technikái a hiányos, pontatlan vagy nem teljes adatok kezelésére. | [lecke](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | Mennyiségek vizualizálása | [Adatok vizualizálása](3-Data-Visualization/README.md) | Tanuld meg, hogyan használhatod a Matplotlib-et madáradatok vizualizálására 🦆 | [lecke](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | Adatok eloszlásának vizualizálása | [Adatok vizualizálása](3-Data-Visualization/README.md) | Megfigyelések és trendek vizualizálása egy intervallumon belül. | [lecke](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | Arányok vizualizálása | [Adatok vizualizálása](3-Data-Visualization/README.md) | Diszkrét és csoportosított százalékok vizualizálása. | [lecke](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | Kapcsolatok vizualizálása | [Adatok vizualizálása](3-Data-Visualization/README.md) | Kapcsolatok és korrelációk vizualizálása adathalmazok és azok változói között. | [lecke](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | Jelentőségteljes vizualizációk | [Adatok vizualizálása](3-Data-Visualization/README.md) | Technikák és útmutatók, amelyek segítenek értékes vizualizációkat készíteni a hatékony problémamegoldás és betekintés érdekében. | [lecke](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | Bevezetés az adatelemzési életciklusba | [Életciklus](4-Data-Science-Lifecycle/README.md) | Bevezetés az adatelemzési életciklusba és annak első lépésébe, az adatok megszerzésébe és kinyerésébe. | [lecke](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | Elemzés | [Életciklus](4-Data-Science-Lifecycle/README.md) | Az adatelemzési életciklus ezen fázisa az adatok elemzésének technikáira összpontosít. | [lecke](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | Kommunikáció | [Életciklus](4-Data-Science-Lifecycle/README.md) | Az adatelemzési életciklus ezen fázisa az adatokból származó betekintések bemutatására összpontosít, hogy a döntéshozók számára könnyebben érthetővé váljanak. | [lecke](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | Adatelemzés a felhőben | [Felhő adatok](5-Data-Science-In-Cloud/README.md) | Ez a leckesorozat bevezeti az adatelemzést a felhőben és annak előnyeit. | [lecke](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) és [Maud](https://twitter.com/maudstweets) |
| 18 | Adatelemzés a felhőben | [Felhő adatok](5-Data-Science-In-Cloud/README.md) | Modellek betanítása alacsony kódú eszközökkel. |[lecke](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) és [Maud](https://twitter.com/maudstweets) |
| 19 | Adatelemzés a felhőben | [Felhő adatok](5-Data-Science-In-Cloud/README.md) | Modellek telepítése az Azure Machine Learning Studio segítségével. | [lecke](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) és [Maud](https://twitter.com/maudstweets) |
| 20 | Adatelemzés a valóságban | [A valóságban](6-Data-Science-In-Wild/README.md) | Adatelemzés által vezérelt projektek a való világban. | [lecke](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

Kövesd az alábbi lépéseket, hogy megnyisd ezt a mintát egy Codespace-ben:
1. Kattints a Code legördülő menüre, és válaszd az Open with Codespaces opciót.
2. Válaszd a + New codespace lehetőséget az ablak alján.
További információért nézd meg a [GitHub dokumentációt](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace).

## VSCode Remote - Containers
Kövesd az alábbi lépéseket, hogy megnyisd ezt a repót egy konténerben a helyi gépeden és a VSCode-on keresztül a VS Code Remote - Containers bővítmény segítségével:

1. Ha először használsz fejlesztői konténert, győződj meg róla, hogy a rendszered megfelel az előfeltételeknek (pl. Docker telepítve van) a [kezdő dokumentációban](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started) leírtak szerint.

A repó használatához megnyithatod azt egy izolált Docker kötetben:

**Megjegyzés**: A háttérben ez a Remote-Containers: **Clone Repository in Container Volume...** parancsot használja, hogy a forráskódot egy Docker kötetben klónozza a helyi fájlrendszer helyett. A [kötetek](https://docs.docker.com/storage/volumes/) az adatok tárolásának preferált mechanizmusa a konténerekben.

Vagy megnyithatod a repó helyileg klónozott vagy letöltött verzióját:

- Klónozd ezt a repót a helyi fájlrendszeredre.
- Nyomd meg az F1-et, és válaszd a **Remote-Containers: Open Folder in Container...** parancsot.
- Válaszd ki ennek a mappának a klónozott másolatát, várj, amíg a konténer elindul, és próbáld ki a dolgokat.

## Offline hozzáférés

Ezt a dokumentációt offline is futtathatod a [Docsify](https://docsify.js.org/#/) segítségével. Forkold ezt a repót, [telepítsd a Docsify-t](https://docsify.js.org/#/quickstart) a helyi gépedre, majd a repó gyökérmappájában írd be: `docsify serve`. A weboldal a 3000-es porton lesz elérhető a localhostodon: `localhost:3000`.

> Megjegyzés: a notebookok nem lesznek megjelenítve a Docsify-on keresztül, ezért ha notebookot kell futtatnod, azt külön tedd meg a VS Code-ban, Python kernel használatával.

## Egyéb tantervek

Csapatunk más tanterveket is készít! Nézd meg:

- [Edge AI kezdőknek](https://aka.ms/edgeai-for-beginners)
- [AI ügynökök kezdőknek](https://aka.ms/ai-agents-beginners)
- [Generatív AI kezdőknek](https://aka.ms/genai-beginners)
- [Generatív AI kezdőknek .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generatív AI JavaScript-tel](https://github.com/microsoft/generative-ai-with-javascript)
- [Generatív AI Java-val](https://aka.ms/genaijava)
- [AI kezdőknek](https://aka.ms/ai-beginners)
- [Adatelemzés kezdőknek](https://aka.ms/datascience-beginners)
- [Bash kezdőknek](https://github.com/microsoft/bash-for-beginners)
- [Gépi tanulás kezdőknek](https://aka.ms/ml-beginners)
- [Kiberbiztonság kezdőknek](https://github.com/microsoft/Security-101) 
- [Webfejlesztés kezdőknek](https://aka.ms/webdev-beginners)
- [IoT kezdőknek](https://aka.ms/iot-beginners)
- [Gépi tanulás kezdőknek](https://aka.ms/ml-beginners)
- [XR fejlesztés kezdőknek](https://aka.ms/xr-dev-for-beginners)
- [GitHub Copilot mesteri használata AI páros programozáshoz](https://aka.ms/GitHubCopilotAI)
- [XR fejlesztés kezdőknek](https://github.com/microsoft/xr-development-for-beginners)
- [GitHub Copilot mesteri használata C#/.NET fejlesztők számára](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers)
- [Válaszd ki a saját Copilot kalandodat](https://github.com/microsoft/CopilotAdventures)

## Segítség kérése

**Problémákba ütköztél?** Nézd meg a [Hibaelhárítási útmutatót](TROUBLESHOOTING.md) a gyakori problémák megoldásához.

Ha elakadnál, vagy kérdéseid lennének az AI alkalmazások építésével kapcsolatban, csatlakozz:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Ha termék-visszajelzést szeretnél adni, vagy hibákba ütközöl az építés során, látogass el ide:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.