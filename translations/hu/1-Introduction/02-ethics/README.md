<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58860ce9a4b8a564003d2752f7c72851",
  "translation_date": "2025-10-03T16:53:07+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "hu"
}
-->
# Bevezetés az adatetikába

|![ Sketchnote készítette: [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Adattudományi etika - _Sketchnote készítette: [@nitya](https://twitter.com/nitya)_ |

---

Mindannyian adatpolgárok vagyunk egy adatvezérelt világban.

A piaci trendek azt mutatják, hogy 2022-re minden harmadik nagy szervezet online [piactereken és tőzsdéken](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/) keresztül fog adatokat vásárolni és eladni. **Alkalmazásfejlesztőként** könnyebb és olcsóbb lesz adatvezérelt betekintéseket és algoritmusvezérelt automatizálást integrálni a mindennapi felhasználói élményekbe. Azonban ahogy az AI egyre elterjedtebbé válik, meg kell értenünk az olyan algoritmusok [fegyveresítéséből](https://www.youtube.com/watch?v=TQHs8SA1qpk) származó potenciális károkat is, amelyek nagy léptékben működnek.

A trendek azt sugallják, hogy 2025-re több mint [180 zettabájtnyi](https://www.statista.com/statistics/871513/worldwide-data-created/) adatot fogunk generálni és fogyasztani. **Adattudósokként** ez az információrobbanás példátlan hozzáférést biztosít személyes és viselkedési adatokhoz. Ez lehetőséget ad részletes felhasználói profilok létrehozására és a döntéshozatal finom befolyásolására—gyakran olyan módon, amely egy [szabad választás illúzióját](https://www.datasciencecentral.com/the-pareto-set-and-the-paradox-of-choice/) kelti. Bár ez felhasználható arra, hogy a felhasználókat preferált eredmények felé tereljük, komoly kérdéseket vet fel az adatvédelemről, autonómiáról és az algoritmikus befolyás etikai határairól.

Az adatetika mostanra _szükséges korlátokat_ jelent az adattudomány és mérnöki munka számára, segítve a potenciális károk és nem szándékos következmények minimalizálását az adatvezérelt cselekvéseinkből. A [Gartner AI Hype Cycle](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) azonosítja a digitális etika, a felelős AI és az AI irányítás releváns trendjeit, mint kulcsfontosságú hajtóerőket az AI _demokratizálása_ és _iparosítása_ körüli nagyobb megatrendekhez.

![Gartner AI Hype Cycle - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

Ebben a leckében az adatetika lenyűgöző területét fogjuk felfedezni—az alapfogalmaktól és kihívásoktól kezdve az esettanulmányokon és alkalmazott AI fogalmakon át, mint az irányítás—amelyek segítenek az etikai kultúra kialakításában az adatokat és AI-t használó csapatokban és szervezetekben.

## [Előadás előtti kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/2) 🎯

## Alapvető meghatározások

Kezdjük az alapvető terminológia megértésével.

Az "etika" szó a [görög "ethikos"](https://en.wikipedia.org/wiki/Ethics) (és annak "ethos" gyökere) szóból származik, amely _jellemet vagy erkölcsi természetet_ jelent.

**Etika** azokról a közös értékekről és erkölcsi elvekről szól, amelyek irányítják viselkedésünket a társadalomban. Az etika nem törvényeken alapul, hanem széles körben elfogadott normákon arról, hogy mi a "helyes és helytelen". Az etikai megfontolások azonban befolyásolhatják a vállalatirányítási kezdeményezéseket és a kormányzati szabályozásokat, amelyek több ösztönzőt teremtenek a megfelelésre.

**Adatetika** egy [új etikai ág](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1), amely "tanulmányozza és értékeli az _adatokkal, algoritmusokkal és kapcsolódó gyakorlatokkal_ kapcsolatos erkölcsi problémákat". Itt az **"adatok"** az adatok létrehozásával, rögzítésével, gondozásával, feldolgozásával, terjesztésével, megosztásával és felhasználásával kapcsolatos cselekvésekre összpontosítanak, az **"algoritmusok"** az AI-ra, ügynökökre, gépi tanulásra és robotokra, míg a **"gyakorlatok"** olyan témákra, mint a felelős innováció, programozás, hackelés és etikai kódexek.

**Alkalmazott etika** az [erkölcsi megfontolások gyakorlati alkalmazása](https://en.wikipedia.org/wiki/Applied_ethics). Ez az etikai kérdések aktív vizsgálatának folyamata a _valós cselekvések, termékek és folyamatok_ kontextusában, és korrekciós intézkedések megtétele annak érdekében, hogy ezek összhangban maradjanak a meghatározott etikai értékeinkkel.

**Etikai kultúra** az [_alkalmazott etika működtetése_](https://hbr.org/2019/05/how-to-design-an-ethical-organization), hogy biztosítsuk, hogy etikai elveink és gyakorlataink következetesen és skálázható módon kerüljenek alkalmazásra az egész szervezetben. A sikeres etikai kultúrák szervezet-szintű etikai elveket határoznak meg, jelentős ösztönzőket biztosítanak a megfeleléshez, és megerősítik az etikai normákat azáltal, hogy ösztönzik és felerősítik a kívánt viselkedéseket a szervezet minden szintjén.

## Etikai fogalmak

Ebben a részben olyan fogalmakat tárgyalunk, mint a **közös értékek** (elvek) és **etikai kihívások** (problémák) az adatetikában—valamint **esettanulmányokat** vizsgálunk, amelyek segítenek megérteni ezeket a fogalmakat a valós helyzetekben.

### 1. Etikai elvek

Minden adatetikai stratégia az _etikai elvek_ meghatározásával kezdődik—azokkal a "közös értékekkel", amelyek leírják az elfogadható viselkedéseket, és irányítják a megfelelési cselekvéseket adat- és AI-projektjeinkben. Ezeket egyéni vagy csapatszinten is meghatározhatjuk. Azonban a legtöbb nagy szervezet ezeket egy _etikus AI_ küldetésnyilatkozatban vagy keretrendszerben határozza meg, amelyet vállalati szinten definiálnak és következetesen érvényesítenek minden csapatnál.

**Példa:** A Microsoft [Felelős AI](https://www.microsoft.com/en-us/ai/responsible-ai) küldetésnyilatkozata így szól: _"Elkötelezettek vagyunk az AI fejlődése mellett, amelyet etikai elvek vezérelnek, és az embereket helyezik előtérbe"_—6 etikai elvet azonosítva az alábbi keretrendszerben:

![Felelős AI a Microsoftnál](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Nézzük meg röviden ezeket az elveket. A _transzparencia_ és _elszámoltathatóság_ alapvető értékek, amelyekre a többi elv épül—kezdjük ezekkel:

* [**Elszámoltathatóság**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) arra kötelezi a szakembereket, hogy _felelősséget vállaljanak_ adat- és AI-műveleteikért, valamint az etikai elvek betartásáért.
* [**Transzparencia**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) biztosítja, hogy az adat- és AI-cselekvések _érthetőek_ legyenek a felhasználók számára, megmagyarázva a döntések mögötti mit és miért.
* [**Méltányosság**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) arra összpontosít, hogy az AI _minden embert_ méltányosan kezeljen, foglalkozva az adatokban és rendszerekben lévő szisztematikus vagy implicit szociotechnikai torzításokkal.
* [**Megbízhatóság és biztonság**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) biztosítja, hogy az AI _következetesen_ viselkedjen a meghatározott értékekkel, minimalizálva a potenciális károkat vagy nem szándékos következményeket.
* [**Adatvédelem és biztonság**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) az adatok eredetének megértéséről szól, és _adatvédelemhez kapcsolódó védelmet_ nyújt a felhasználóknak.
* [**Befogadás**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) az AI-megoldások szándékos tervezéséről szól, alkalmazkodva a _széles körű emberi igényekhez_ és képességekhez.

> 🚨 Gondolkodj el azon, hogy mi lehetne az adatetikai küldetésnyilatkozatod. Fedezd fel más szervezetek etikus AI keretrendszereit—példák: [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles), és [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Milyen közös értékekkel rendelkeznek? Hogyan kapcsolódnak ezek az elvek az AI-termékhez vagy iparághoz, amelyben működnek?

### 2. Etikai kihívások

Miután meghatároztuk az etikai elveket, a következő lépés az adat- és AI-cselekvéseink értékelése, hogy megfelelnek-e ezeknek a közös értékeknek. Gondolj a cselekvésekre két kategóriában: _adatgyűjtés_ és _algoritmus tervezés_.

Az adatgyűjtés során a cselekvések valószínűleg **személyes adatokkal** vagy személyesen azonosítható információkkal (PII) kapcsolatosak, amelyek azonosítható élő személyekre vonatkoznak. Ez magában foglalja a [különféle nem személyes adatokat](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en), amelyek _együttesen_ azonosítanak egy személyt. Az etikai kihívások kapcsolódhatnak _adatvédelemhez_, _adat tulajdonjoghoz_, és kapcsolódó témákhoz, mint _tájékozott beleegyezés_ és _szellemi tulajdonjogok_ a felhasználók számára.

Az algoritmus tervezés során a cselekvések magukban foglalják **adatkészletek** gyűjtését és gondozását, majd ezek felhasználását **adatmodellek** képzésére és telepítésére, amelyek valós helyzetekben előrejelzéseket készítenek vagy automatizált döntéseket hoznak. Etikai kihívások merülhetnek fel _adatkészlet torzítás_, _adatminőség_ problémák, _méltánytalanság_, és _félrevezetés_ miatt az algoritmusokban—beleértve néhány szisztematikus jellegű problémát.

Mindkét esetben az etikai kihívások olyan területeket emelnek ki, ahol cselekvéseink konfliktusba kerülhetnek közös értékeinkkel. Ezek észleléséhez, enyhítéséhez, minimalizálásához vagy megszüntetéséhez erkölcsi "igen/nem" kérdéseket kell feltennünk cselekvéseinkkel kapcsolatban, majd szükség esetén korrekciós intézkedéseket kell tennünk. Nézzünk meg néhány etikai kihívást és az általuk felvetett erkölcsi kérdéseket:

#### 2.1 Adattulajdonjog

Az adatgyűjtés gyakran személyes adatokat foglal magában, amelyek azonosíthatják az adat alanyait. Az [adattulajdonjog](https://permission.io/blog/data-ownership) az adatok létrehozásával, feldolgozásával és terjesztésével kapcsolatos _ellenőrzésről_ és [_felhasználói jogokról_](https://permission.io/blog/data-ownership) szól.

Az erkölcsi kérdések, amelyeket fel kell tennünk:
 * Ki birtokolja az adatokat? (felhasználó vagy szervezet)
 * Milyen jogokkal rendelkeznek az adat alanyai? (pl. hozzáférés, törlés, hordozhatóság)
 * Milyen jogokkal rendelkeznek a szervezetek? (pl. rosszindulatú felhasználói vélemények helyesbítése)

#### 2.2 Tájékozott beleegyezés

A [tájékozott beleegyezés](https://legaldictionary.net/informed-consent/) azt jelenti, hogy a felhasználók beleegyeznek egy cselekvésbe (például adatgyűjtésbe) a releváns tények teljes megértésével, beleértve a célt, a potenciális kockázatokat és az alternatívákat.

Itt felmerülő kérdések:
 * A felhasználó (adat alany) engedélyt adott az adatok rögzítésére és felhasználására?
 * A felhasználó megértette, hogy miért gyűjtötték az adatokat?
 * A felhasználó megértette a részvételéből származó potenciális kockázatokat?

#### 2.3 Szellemi tulajdon

A [szellemi tulajdon](https://en.wikipedia.org/wiki/Intellectual_property) az emberi kezdeményezésből származó immateriális alkotásokra utal, amelyek _gazdasági értékkel_ bírhatnak egyének vagy vállalkozások számára.

Itt felmerülő kérdések:
 * A gyűjtött adatok gazdasági értékkel bírnak-e egy felhasználó vagy vállalkozás számára?
 * Van-e a **felhasználónak** szellemi tulajdona itt?
 * Van-e a **szervezetnek** szellemi tulajdona itt?
 * Ha ezek a jogok léteznek, hogyan védjük őket?

#### 2.4 Adatvédelem

Az [adatvédelem](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) vagy információs magánélet a felhasználói magánélet megőrzésére és a felhasználói identitás védelmére vonatkozik a személyesen azonosítható információk tekintetében.

Itt felmerülő kérdések:
 * A felhasználók (személyes) adatai védettek-e a hackelésekkel és szivárgásokkal szemben?
 * A felhasználók adatai csak jogosult felhasználók és kontextusok számára hozzáférhetők?
 * A felhasználók anonimitása megmarad-e, amikor az adatokat megosztják vagy terjesztik?
 * Lehet-e egy felhasználót azonosítani anonimizált adatkészletekből?

#### 2.5 Az elfeledtetés joga

Az [elfeledtetés joga](https://en
* Tükrözi az információ _pontosan_ a valóságot?

#### 2.8 Algoritmusok méltányossága

[Algoritmusok méltányossága](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) azt vizsgálja, hogy az algoritmus tervezése szisztematikusan diszkriminálja-e az adatközlők bizonyos alcsoportjait, ami [potenciális károkat](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) okozhat az _elosztásban_ (ahol erőforrásokat tagadnak meg vagy tartanak vissza az adott csoporttól) és a _szolgáltatás minőségében_ (ahol az AI nem olyan pontos bizonyos alcsoportok esetében, mint másoknál).

A következő kérdéseket érdemes megvizsgálni:
* Értékeltük-e a modell pontosságát különböző alcsoportok és feltételek esetében?
* Vizsgáltuk-e a rendszert potenciális károk (pl. sztereotipizálás) szempontjából?
* Tudjuk-e módosítani az adatokat vagy újratanítani a modelleket az azonosított károk enyhítése érdekében?

Fedezze fel az olyan forrásokat, mint az [AI méltányossági ellenőrzőlisták](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA), hogy többet megtudjon.

#### 2.9 Félrevezetés

[Adatok félrevezetése](https://www.sciencedirect.com/topics/computer-science/misrepresentation) arról szól, hogy vajon őszintén közölt adatokból származó betekintéseket használunk-e fel megtévesztő módon egy kívánt narratíva támogatására.

A következő kérdéseket érdemes megvizsgálni:
* Jelentünk-e be hiányos vagy pontatlan adatokat?
* Úgy vizualizáljuk-e az adatokat, hogy félrevezető következtetéseket vonjanak le belőlük?
* Használunk-e szelektív statisztikai technikákat az eredmények manipulálására?
* Vannak-e alternatív magyarázatok, amelyek más következtetést kínálhatnak?

#### 2.10 Szabad választás
A [szabad választás illúziója](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) akkor fordul elő, amikor a rendszer „választási architektúrái” döntéshozó algoritmusokat használnak arra, hogy az embereket egy preferált eredmény felé tereljék, miközben látszólag lehetőségeket és kontrollt kínálnak nekik. Ezek a [sötét minták](https://www.darkpatterns.org/) társadalmi és gazdasági károkat okozhatnak a felhasználóknak. Mivel a felhasználói döntések befolyásolják a viselkedési profilokat, ezek a cselekvések potenciálisan meghatározhatják a jövőbeli választásokat, amelyek felerősíthetik vagy kiterjeszthetik ezen károk hatását.

A következő kérdéseket érdemes megvizsgálni:
* Megértette-e a felhasználó annak a választásnak a következményeit?
* Tudott-e a felhasználó (alternatív) választási lehetőségekről és azok előnyeiről és hátrányairól?
* Visszavonhatja-e a felhasználó egy automatizált vagy befolyásolt döntést később?

### 3. Esettanulmányok

Ahhoz, hogy ezeket az etikai kihívásokat valós környezetben megértsük, érdemes olyan esettanulmányokat megvizsgálni, amelyek rávilágítanak az egyénekre és a társadalomra gyakorolt potenciális károkra és következményekre, amikor az ilyen etikai vétségeket figyelmen kívül hagyják.

Íme néhány példa:

| Etikai kihívás | Esettanulmány | 
|--- |--- |
| **Tájékozott beleegyezés** | 1972 - [Tuskegee szifilisz tanulmány](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Az afrikai-amerikai férfiak, akik részt vettek a tanulmányban, ingyenes orvosi ellátást ígértek, _de megtévesztették_ őket a kutatók, akik nem tájékoztatták őket a diagnózisukról vagy a kezelés elérhetőségéről. Sok alany meghalt, és partnereik vagy gyermekeik is érintettek voltak; a tanulmány 40 évig tartott. | 
| **Adatvédelem** | 2007 - A [Netflix adatdíj](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) kutatóknak _10M anonimizált filmértékelést_ biztosított 50K ügyféltől, hogy javítsák az ajánlási algoritmusokat. Azonban a kutatók képesek voltak az anonimizált adatokat személyazonosító adatokkal összekapcsolni _külső adatbázisokban_ (pl. IMDb kommentek), hatékonyan „deanonimizálva” néhány Netflix előfizetőt.|
| **Gyűjtési torzítás** | 2013 - Boston városa [kifejlesztette a Street Bump alkalmazást](https://www.boston.gov/transportation/street-bump), amely lehetővé tette a polgárok számára, hogy kátyúkat jelentsenek, jobb úthálózati adatokat biztosítva a városnak a problémák megtalálásához és javításához. Azonban [az alacsonyabb jövedelmű csoportoknak kevesebb hozzáférésük volt autókhoz és telefonokhoz](https://hbr.org/2013/04/the-hidden-biases-in-big-data), így az ő úthálózati problémáik láthatatlanok maradtak az alkalmazásban. A fejlesztők akadémikusokkal dolgoztak együtt az _egyenlő hozzáférés és digitális szakadék_ kérdéseinek megoldása érdekében. |
| **Algoritmusok méltányossága** | 2018 - Az MIT [Gender Shades tanulmány](http://gendershades.org/overview.html) értékelte a nemek osztályozására szolgáló AI termékek pontosságát, feltárva a pontossági hiányosságokat a nők és színes bőrűek esetében. Egy [2019-es Apple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) úgy tűnt, hogy kevesebb hitelt kínál a nőknek, mint a férfiaknak. Mindkettő az algoritmikus torzítás problémáit illusztrálta, amelyek társadalmi-gazdasági károkat okoztak.|
| **Adatok félrevezetése** | 2020 - A [Georgia Egészségügyi Minisztérium COVID-19 grafikonokat tett közzé](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening), amelyek félrevezetően mutatták a megerősített esetek trendjeit, nem kronológiai sorrendben az x-tengelyen. Ez a vizualizációs trükkök általi félrevezetést illusztrálja. |
| **Szabad választás illúziója** | 2020 - Az ABCmouse tanulási alkalmazás [10M dollárt fizetett az FTC panasz rendezésére](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/), ahol a szülők olyan előfizetésekért fizettek, amelyeket nem tudtak lemondani. Ez a választási architektúrák sötét mintáit illusztrálja, ahol a felhasználókat potenciálisan káros döntések felé terelték. |
| **Adatvédelem és felhasználói jogok** | 2021 - A Facebook [adatvédelmi incidens](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) 530M felhasználó adatait tette ki, ami 5B dolláros egyezséget eredményezett az FTC-vel. Azonban megtagadta a felhasználók értesítését az incidensről, megsértve a felhasználói jogokat az adatátláthatóság és hozzáférés terén. |

Szeretne további esettanulmányokat felfedezni? Nézze meg ezeket a forrásokat:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - etikai dilemmák különböző iparágakban.
* [Data Science Ethics kurzus](https://www.coursera.org/learn/data-science-ethics#syllabus) - mérföldkőnek számító esettanulmányok.
* [Hol mentek félre a dolgok](https://deon.drivendata.org/examples/) - Deon ellenőrzőlista példákkal.

> 🚨 Gondoljon azokra az esettanulmányokra, amelyeket látott – tapasztalt-e, vagy érintették-e hasonló etikai kihívások az életében? Tud-e legalább egy másik esettanulmányt, amely illusztrálja az ebben a szakaszban tárgyalt etikai kihívások egyikét?

## Alkalmazott etika

Beszéltünk az etikai fogalmakról, kihívásokról és esettanulmányokról valós környezetben. De hogyan kezdhetjük el az etikai elvek és gyakorlatok _alkalmazását_ a projektjeinkben? És hogyan _valósíthatjuk meg_ ezeket a gyakorlatokat a jobb irányítás érdekében? Nézzünk meg néhány valós megoldást:

### 1. Szakmai kódexek

A szakmai kódexek egy lehetőséget kínálnak a szervezetek számára, hogy „ösztönözzék” tagjaikat az etikai elveik és küldetésük támogatására. A kódexek _erkölcsi iránymutatások_ a szakmai viselkedéshez, segítve az alkalmazottakat vagy tagokat olyan döntések meghozatalában, amelyek összhangban vannak a szervezetük elveivel. Csak annyira hatékonyak, amennyire a tagok önkéntes megfelelése; azonban sok szervezet további jutalmakat és büntetéseket kínál, hogy motiválja a tagok megfelelését.

Példák:
* [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Etikai Kódex
* [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Magatartási Kódex (2013-ban készült)
* [ACM Etikai Kódex és Szakmai Magatartás](https://www.acm.org/code-of-ethics) (1993 óta)

> 🚨 Tagja-e valamilyen szakmai mérnöki vagy adatkutatási szervezetnek? Nézze meg a weboldalukat, hogy meghatároznak-e szakmai etikai kódexet. Mit mond ez az etikai elveikről? Hogyan „ösztönzik” a tagokat a kódex követésére?

### 2. Etikai ellenőrzőlisták

Míg a szakmai kódexek meghatározzák a gyakorlók által megkövetelt _etikai viselkedést_, [ismert korlátokkal](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) rendelkeznek a végrehajtásban, különösen nagyszabású projektek esetében. Ehelyett sok adatkutatási szakértő [ellenőrzőlistákat javasol](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), amelyek **összekapcsolják az elveket a gyakorlatokkal** determinisztikusabb és cselekvőképesebb módon.

Az ellenőrzőlisták a kérdéseket „igen/nem” feladatokká alakítják, amelyek operacionalizálhatók, lehetővé téve, hogy nyomon kövessék őket a szokásos termékkiadási munkafolyamatok részeként.

Példák:
* [Deon](https://deon.drivendata.org/) - általános célú adatetikai ellenőrzőlista, amelyet [iparági ajánlásokból](https://deon.drivendata.org/#checklist-citations) hoztak létre, parancssori eszközzel a könnyű integráció érdekében.
* [Adatvédelmi audit ellenőrzőlista](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - általános iránymutatást nyújt az információkezelési gyakorlatokhoz jogi és társadalmi kitettség szempontjából.
* [AI méltányossági ellenőrzőlista](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - AI szakemberek által létrehozva, hogy támogassák a méltányossági ellenőrzések bevezetését és integrációját az AI fejlesztési ciklusokba.
* [22 kérdés az adatok és AI etikájáról](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - nyitottabb keretrendszer, amelyet az etikai kérdések kezdeti feltárására terveztek a tervezés, megvalósítás és szervezeti kontextusokban.

### 3. Etikai szabályozások

Az etika közös értékek meghatározásáról és a helyes cselekvésről szól _önkéntesen_. **Megfelelés** arról szól, hogy _követjük a törvényt_, ha és ahol meghatározták. **Irányítás** széles körben lefedi az összes módot, ahogyan a szervezetek működnek az etikai elvek érvényesítése és a meghatározott törvények betartása érdekében.

Ma az irányítás két formát ölt a szervezeteken belül. Először is, az **etikus AI** elvek meghatározásáról és a gyakorlatok létrehozásáról szól, hogy operacionalizálják az elfogadást az összes AI-val kapcsolatos projektben a szervezeten belül. Másodszor, a kormány által előírt **adatvédelmi szabályozások** betartásáról szól azokban a régiókban, ahol működik.

Adatvédelmi és adatkezelési szabályozások példái:

* `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - szabályozza a _szövetségi kormány_ személyes adatok gyűjtését, használatát és közzétételét.
* `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - védi a személyes egészségügyi adatokat.
* `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - védi a 13 év alatti gyermekek adatvédelmét.
* `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - felhasználói jogokat, adatvédelmet és adatbiztonságot biztosít.
* `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) több _jogot_ biztosít a fogyasztóknak a (személyes) adataik felett.
* `2021`, Kína [Személyes Adatvédelmi Törvénye](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) éppen elfogadva, létrehozva az egyik legerősebb online adatvédelmi szabályozást világszerte.

> 🚨 Az Európai Unió által meghatározott GDPR (General Data Protection Regulation) ma az egyik legbefolyásosabb adatvédelmi szabályozás. Tudta, hogy ez [8 felhasználói jogot](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) is meghatároz az állampolgárok digitális adatvédelmének és személyes adat
* [Machine Learning For Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - lecke az igazságosságról, a Microsofttól.
* [A Felelős MI Alapelvei](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - ingyenes tanulási útvonal a Microsoft Learn-től.
* [Etika és Adattudomány](https://resources.oreilly.com/examples/0636920203964) - O'Reilly e-könyv (M. Loukides, H. Mason és mások)
* [Adattudományi Etika](https://www.coursera.org/learn/data-science-ethics#syllabus) - online kurzus a Michigani Egyetemtől.
* [Etika Kibontva](https://ethicsunwrapped.utexas.edu/case-studies) - esettanulmányok a Texasi Egyetemtől.

# Feladat

[Írj egy esettanulmányt az adatetikáról](assignment.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.