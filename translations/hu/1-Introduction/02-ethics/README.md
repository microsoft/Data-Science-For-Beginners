<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8796f41f566a0a8ebb72863a83d558ed",
  "translation_date": "2025-08-26T15:04:07+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "hu"
}
-->
# Bevezetés az adatetika világába

|![ Sketchnote készítette: [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Adattudományi etika - _Sketchnote készítette: [@nitya](https://twitter.com/nitya)_ |

---

Mindannyian adatpolgárok vagyunk egy adatokkal átszőtt világban.

A piaci trendek azt mutatják, hogy 2022-re minden harmadik nagy szervezet online [piactereken és tőzsdéken](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/) keresztül fog adatokat vásárolni és eladni. **Alkalmazásfejlesztőként** egyre könnyebb és olcsóbb lesz adatvezérelt betekintéseket és algoritmusvezérelt automatizációt integrálni a mindennapi felhasználói élményekbe. Azonban, ahogy a mesterséges intelligencia (MI) mindent áthatóvá válik, meg kell értenünk azokat a potenciális károkat is, amelyeket az ilyen algoritmusok [fegyverként való alkalmazása](https://www.youtube.com/watch?v=TQHs8SA1qpk) okozhat nagy léptékben.

A trendek azt is jelzik, hogy 2025-re több mint [180 zettabájtnyi](https://www.statista.com/statistics/871513/worldwide-data-created/) adatot fogunk létrehozni és fogyasztani. **Adattudósként** ez példátlan szintű hozzáférést biztosít számunkra a személyes adatokhoz. Ez lehetővé teszi, hogy felhasználói viselkedési profilokat építsünk, és olyan döntéshozatalt befolyásoljunk, amely [a szabad választás illúzióját](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) kelti, miközben esetleg a számunkra kedvező eredmények felé tereljük a felhasználókat. Ez szélesebb körű kérdéseket is felvet az adatvédelemről és a felhasználói jogok védelméről.

Az adatetika ma már _elengedhetetlen irányelv_ az adattudomány és a mérnöki munka számára, amely segít minimalizálni az adatvezérelt cselekedeteinkből eredő potenciális károkat és nem szándékos következményeket. A [Gartner MI Hype Cycle](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) azonosítja a digitális etika, a felelős MI és az MI irányítás releváns trendjeit, mint kulcsfontosságú hajtóerőket az MI _demokratizálása_ és _iparosítása_ körüli nagyobb megatrendekhez.

![Gartner MI Hype Cycle - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

Ebben a leckében az adatetika lenyűgöző területét fogjuk felfedezni - az alapfogalmaktól és kihívásoktól kezdve az esettanulmányokon át az alkalmazott MI fogalmakig, mint például az irányítás -, amelyek segítenek az etikai kultúra kialakításában az adatokkal és MI-vel dolgozó csapatokban és szervezetekben.

## [Előadás előtti kvíz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## Alapvető meghatározások

Kezdjük az alapvető terminológia megértésével.

Az "etika" szó a [görög "ethikos"](https://en.wikipedia.org/wiki/Ethics) (és annak gyökere, az "ethos") szóból származik, amely _jellemet vagy erkölcsi természetet_ jelent.

**Etika** azokról a közös értékekről és erkölcsi elvekről szól, amelyek irányítják viselkedésünket a társadalomban. Az etika nem törvényeken alapul, hanem azon a széles körben elfogadott normán, hogy mi a "helyes és helytelen". Azonban az etikai megfontolások befolyásolhatják a vállalatirányítási kezdeményezéseket és a kormányzati szabályozásokat, amelyek több ösztönzőt teremtenek a megfelelésre.

**Adatetika** egy [új etikai ág](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1), amely "az _adatokkal, algoritmusokkal és a hozzájuk kapcsolódó gyakorlatokkal_ kapcsolatos erkölcsi problémákat tanulmányozza és értékeli". Itt az **"adatok"** az adatok generálásával, rögzítésével, kurálásával, feldolgozásával, terjesztésével, megosztásával és felhasználásával kapcsolatos cselekvésekre összpontosítanak, az **"algoritmusok"** az MI-re, ügynökökre, gépi tanulásra és robotokra, míg a **"gyakorlatok"** olyan témákra, mint a felelős innováció, programozás, hackelés és etikai kódexek.

**Alkalmazott etika** az [erkölcsi megfontolások gyakorlati alkalmazása](https://en.wikipedia.org/wiki/Applied_ethics). Ez az a folyamat, amely során aktívan vizsgáljuk az etikai kérdéseket a _valós cselekvések, termékek és folyamatok_ kontextusában, és korrekciós intézkedéseket teszünk annak érdekében, hogy ezek összhangban maradjanak a meghatározott etikai értékeinkkel.

**Etikai kultúra** az [_alkalmazott etika operacionalizálásáról_](https://hbr.org/2019/05/how-to-design-an-ethical-organization) szól, hogy biztosítsuk, hogy etikai elveinket és gyakorlatainkat következetesen és skálázható módon alkalmazzák a szervezet egészében. A sikeres etikai kultúrák szervezet-szintű etikai elveket határoznak meg, jelentős ösztönzőket biztosítanak a megfeleléshez, és megerősítik az etikai normákat azáltal, hogy minden szinten ösztönzik és erősítik a kívánt viselkedéseket.

## Etikai fogalmak

Ebben a részben olyan fogalmakat tárgyalunk, mint a **közös értékek** (elvek) és az **etikai kihívások** (problémák) az adatetika területén - valamint **esettanulmányokat** vizsgálunk, amelyek segítenek megérteni ezeket a fogalmakat a valós kontextusokban.

### 1. Etikai elvek

Minden adatetikai stratégia az _etikai elvek_ meghatározásával kezdődik - azokkal a "közös értékekkel", amelyek leírják az elfogadható viselkedéseket, és irányítják a megfelelőségi cselekvéseket az adat- és MI-projektjeinkben. Ezeket egyéni vagy csapatszinten is meghatározhatjuk. Azonban a legtöbb nagy szervezet ezeket egy _etikus MI_ küldetésnyilatkozatban vagy keretrendszerben foglalja össze, amelyet vállalati szinten határoznak meg, és következetesen érvényesítenek minden csapatban.

**Példa:** A Microsoft [Felelős MI](https://www.microsoft.com/en-us/ai/responsible-ai) küldetésnyilatkozata így szól: _"Elkötelezettek vagyunk az MI fejlődése iránt, amelyet olyan etikai elvek vezérelnek, amelyek az embereket helyezik előtérbe"_ - az alábbi keretrendszerben 6 etikai elvet azonosítva:

![Felelős MI a Microsoftnál](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Vizsgáljuk meg röviden ezeket az elveket. A _transzparencia_ és az _elszámoltathatóság_ alapvető értékek, amelyekre a többi elv épül - kezdjük ezekkel:

* [**Elszámoltathatóság**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) biztosítja, hogy a szakemberek _felelősséget vállaljanak_ adat- és MI-műveleteikért, valamint az etikai elvek betartásáért.
* [**Transzparencia**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) biztosítja, hogy az adat- és MI-műveletek _érthetőek_ legyenek a felhasználók számára, megmagyarázva a döntések mögötti mit és miért.
* [**Méltányosság**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - biztosítja, hogy az MI _minden embert_ méltányosan kezeljen, kezelve az adat- és rendszerszintű implicit társadalmi-technikai torzításokat.
* [**Megbízhatóság és biztonság**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - biztosítja, hogy az MI _következetesen_ viselkedjen a meghatározott értékekkel összhangban, minimalizálva a potenciális károkat vagy nem szándékos következményeket.
* [**Adatvédelem és biztonság**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - az adatok eredetének megértéséről és a felhasználók számára _adatvédelem és kapcsolódó védelem_ biztosításáról szól.
* [**Befogadás**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - az MI-megoldások szándékos tervezéséről szól, hogy azok _széles körű emberi igényekhez_ és képességekhez alkalmazkodjanak.

> 🚨 Gondolkodj el azon, hogy mi lehetne a te adatetikai küldetésnyilatkozatod. Fedezd fel más szervezetek etikus MI-keretrendszereit - itt van néhány példa: [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles), és [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Milyen közös értékeket találsz bennük? Hogyan kapcsolódnak ezek az elvek az általuk működtetett MI-termékekhez vagy iparágakhoz?

### 2. Etikai kihívások

Miután meghatároztuk az etikai elveket, a következő lépés az adat- és MI-műveleteink értékelése annak érdekében, hogy azok összhangban állnak-e ezekkel a közös értékekkel. Gondolj a cselekedeteidre két kategóriában: _adatgyűjtés_ és _algoritmus tervezés_.

Az adatok gyűjtése során a műveletek valószínűleg **személyes adatokat** vagy személyesen azonosítható információkat (PII) érintenek, amelyek azonosítható élő személyekre vonatkoznak. Ez magában foglalja a [különféle nem személyes adatokat](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en), amelyek _együttesen_ azonosítanak egy személyt. Az etikai kihívások kapcsolódhatnak az _adatvédelemhez_, _adatbirtokláshoz_ és kapcsolódó témákhoz, mint például a _tájékozott beleegyezés_ és a _felhasználói szellemi tulajdonjogok_.

Az algoritmus tervezése során a műveletek magukban foglalják a **adatkészletek** gyűjtését és kurálását, majd ezek felhasználását **adatmodellek** betanítására és telepítésére, amelyek valós környezetben jósolnak eredményeket vagy automatizálnak döntéseket. Az etikai kihívások felmerülhetnek az _adatkészlet torzításából_, _adatminőségi_ problémákból, _méltánytalanságból_ és _félrevezetésből_ az algoritmusokban - beleértve néhány rendszerszintű problémát is.

Mindkét esetben az etikai kihívások olyan területeket emelnek ki, ahol cselekedeteink konfliktusba kerülhetnek közös értékeinkkel. Az ilyen aggályok észleléséhez, enyhítéséhez, minimalizálásához vagy megszüntetéséhez erkölcsi "igen/nem" kérdéseket kell feltennünk a cselekedeteinkkel kapcsolatban, majd szükség esetén korrekciós intézkedéseket kell tennünk. Nézzünk meg néhány etikai kihívást és az általuk felvetett erkölcsi kérdéseket:

#### 2.1 Adatbirtoklás

Az adatok gyűjtése gyakran személyes adatokat érint, amelyek az adat alanyait azonosíthatják. Az [adatbirtoklás](https://permission.io/blog/data-ownership) az adatok létrehozásával, feldolgozásával és terjesztésével kapcsolatos _ellenőrzésről_ és [_felhasználói jogokról_](https://permission.io/blog/data-ownership) szól.

Az erkölcsi kérdések, amelyeket fel kell tennünk:
 * Ki birtokolja az adatokat? (felhasználó vagy szervezet)
 * Milyen jogai vannak az adat alanyainak? (pl. hozzáférés, törlés, hordozhatóság)
 * Milyen jogai vannak a szervezeteknek? (pl. rosszindulatú felhasználói vélemények helyesbítése)

#### 2.2 Tájékozott beleegyezés

A [tájékozott beleegyezés](https://legaldictionary.net/informed-consent/) azt jelenti, hogy a felhasználók egy cselekvéshez (például adatgyűjtéshez) _teljes körű megértéssel_ járulnak hozzá, beleértve a célokat, a lehetséges kockázatokat és az alternatívákat.

Itt feltett kérdések:
 * A felhasználó (adat alanya) engedélyt adott az adatok rögzítésére és felhasználására?
 * A felhasználó megértette, hogy mi célból gyűjtötték az adatokat?
 * A felhasználó megértette a részvételéből eredő lehetséges kockázatokat?

#### 2.3 Szellemi tulajdon

A [szellemi tulajdon](https://en.wikipedia.org/wiki/Intellectual_property) az emberi kezdeményezésből származó immateriális alkotásokra utal, amelyek _gazdasági értékkel_ bírhatnak egyének vagy vállalkozások számára.

Itt feltett kérdések:
 * Az összegyűjtött adatok gazdasági értékkel bírnak-e egy felhasználó vagy vállalkozás számára?
 * Van-e a **felhasználónak** szellemi tulajdona itt?
 * Van-e a **szervezetnek** szellemi tulajdona itt?
 * Ha ezek a jogok léteznek, hogyan védjük őket?

#### 2.4 Adatvédelem

Az [adatvédelem](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) vagy információs magánélet a felhasználói magánélet megőrzésére és a felhasználói identitás védelmére vonatkozik a személyesen azonosítható információk tekintetében.

Itt feltett kérdések:
 * A felhasználók (személyes) adatai védettek-e a hackelésekkel és szivárgásokkal szemben?
 * A felhasználók adatai csak jogosult felhasználók és kontextusok számára érhetők el?
 * A felhasználók anonimitása megmarad-e, amikor az adatokat megosztják vagy terjesztik?
 * Egy felhasználó
[Algorithmusok méltányossága](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) azt vizsgálja, hogy az algoritmus tervezése szisztematikusan diszkriminálja-e az adatközösségek bizonyos alcsoportjait, ami [potenciális károkat](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) okozhat az _erőforrások elosztásában_ (amikor az erőforrásokat megtagadják vagy visszatartják az adott csoporttól) és a _szolgáltatás minőségében_ (amikor az AI nem olyan pontos bizonyos alcsoportok esetében, mint másoknál).

Kérdések, amelyeket érdemes megvizsgálni:
 * Értékeltük-e a modell pontosságát különböző alcsoportok és körülmények között?
 * Vizsgáltuk-e a rendszert potenciális károk (pl. sztereotípiák) szempontjából?
 * Tudjuk-e módosítani az adatokat vagy újratanítani a modelleket az azonosított károk enyhítése érdekében?

Fedezz fel olyan forrásokat, mint az [AI méltányossági ellenőrzőlisták](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA), hogy többet megtudj.

#### 2.9 Félrevezetés

[Adataz félrevezetése](https://www.sciencedirect.com/topics/computer-science/misrepresentation) arra vonatkozik, hogy vajon őszintén jelentett adatokból származó betekintéseket megtévesztő módon kommunikálunk-e, hogy támogassunk egy kívánt narratívát.

Kérdések, amelyeket érdemes megvizsgálni:
 * Jelentünk-e hiányos vagy pontatlan adatokat?
 * Úgy vizualizáljuk-e az adatokat, hogy félrevezető következtetéseket vonjanak le belőlük?
 * Használunk-e szelektív statisztikai technikákat az eredmények manipulálására?
 * Vannak-e alternatív magyarázatok, amelyek más következtetést kínálhatnak?

#### 2.10 Szabad választás
A [szabad választás illúziója](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) akkor fordul elő, amikor a rendszer "választási architektúrái" döntéshozó algoritmusokat használnak arra, hogy az embereket egy preferált eredmény felé tereljék, miközben úgy tűnik, hogy lehetőségeket és kontrollt adnak nekik. Ezek a [sötét minták](https://www.darkpatterns.org/) társadalmi és gazdasági károkat okozhatnak a felhasználóknak. Mivel a felhasználói döntések befolyásolják a viselkedési profilokat, ezek a cselekvések potenciálisan meghatározhatják a jövőbeli választásokat, amelyek felerősíthetik vagy kiterjeszthetik a károk hatását.

Kérdések, amelyeket érdemes megvizsgálni:
 * Értette-e a felhasználó annak a választásnak a következményeit?
 * Tudott-e a felhasználó az (alternatív) választási lehetőségekről és azok előnyeiről és hátrányairól?
 * Visszafordíthatja-e a felhasználó egy automatizált vagy befolyásolt döntést később?

### 3. Esettanulmányok

Ahhoz, hogy ezeket az etikai kihívásokat valós kontextusba helyezzük, érdemes olyan esettanulmányokat megvizsgálni, amelyek kiemelik az egyénekre és a társadalomra gyakorolt potenciális károkat és következményeket, amikor az ilyen etikai vétségeket figyelmen kívül hagyják.

Íme néhány példa:

| Etikai kihívás | Esettanulmány  | 
|--- |--- |
| **Tájékozott beleegyezés** | 1972 - [Tuskegee szifilisz tanulmány](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Az afrikai-amerikai férfiak, akik részt vettek a tanulmányban, ingyenes orvosi ellátást ígértek, _de megtévesztették_ őket a kutatók, akik nem tájékoztatták őket a diagnózisukról vagy a kezelés elérhetőségéről. Sok alany meghalt, és partnereik vagy gyermekeik is érintettek voltak; a tanulmány 40 évig tartott. | 
| **Adatvédelem** |  2007 - A [Netflix adatdíj](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) kutatóknak _10M anonimizált filmértékelést 50K ügyféltől_ biztosított, hogy javítsák az ajánlási algoritmusokat. Azonban a kutatók képesek voltak az anonimizált adatokat személyazonosító adatokkal összekapcsolni _külső adatbázisokban_ (pl. IMDb kommentek), hatékonyan "deanonimizálva" néhány Netflix előfizetőt.|
| **Gyűjtési torzítás**  | 2013 - Boston városa [kifejlesztette a Street Bump](https://www.boston.gov/transportation/street-bump) alkalmazást, amely lehetővé tette a polgárok számára, hogy kátyúkat jelentsenek, jobb úthálózati adatokat biztosítva a városnak a problémák megtalálásához és javításához. Azonban [az alacsonyabb jövedelmű csoportoknak kevesebb hozzáférésük volt autókhoz és telefonokhoz](https://hbr.org/2013/04/the-hidden-biases-in-big-data), így az ő úthálózati problémáik láthatatlanok maradtak az alkalmazásban. A fejlesztők akadémikusokkal dolgoztak együtt, hogy _méltányos hozzáférést és digitális szakadékokat_ kezeljenek a méltányosság érdekében. |
| **Algoritmusok méltányossága**  | 2018 - Az MIT [Gender Shades Study](http://gendershades.org/overview.html) értékelte a nemek osztályozására szolgáló AI termékek pontosságát, feltárva a pontossági hiányosságokat a nők és színes bőrűek esetében. Egy [2019-es Apple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) látszólag kevesebb hitelt kínált a nőknek, mint a férfiaknak. Mindkettő az algoritmikus torzítás problémáit illusztrálta, amelyek társadalmi-gazdasági károkat okoztak.|
| **Adatok félrevezetése** | 2020 - A [Georgia Egészségügyi Minisztérium COVID-19 grafikonokat](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) tett közzé, amelyek látszólag félrevezették a polgárokat az igazolt esetek trendjeiről, nem kronológiai sorrendben az x-tengelyen. Ez a vizualizációs trükkök általi félrevezetést illusztrálja. |
| **Szabad választás illúziója** | 2020 - A tanulási alkalmazás [ABCmouse 10M dollárt fizetett az FTC panasz rendezésére](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/), ahol a szülők nem tudták lemondani az előfizetéseket, amelyekbe belecsúsztak. Ez a választási architektúrák sötét mintáit illusztrálja, ahol a felhasználókat potenciálisan káros döntések felé terelték. |
| **Adatvédelem és felhasználói jogok** | 2021 - A Facebook [adatvédelmi incidens](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) 530M felhasználó adatait tette ki, ami 5B dolláros egyezséget eredményezett az FTC-vel. Azonban megtagadta a felhasználók értesítését az incidensről, megsértve a felhasználói jogokat az adatátláthatóság és hozzáférés terén. |

Szeretnél további esettanulmányokat felfedezni? Nézd meg ezeket a forrásokat:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - etikai dilemmák különböző iparágakban. 
* [Data Science Ethics course](https://www.coursera.org/learn/data-science-ethics#syllabus) - mérföldkőnek számító esettanulmányok.
* [Where things have gone wrong](https://deon.drivendata.org/examples/) - deon ellenőrzőlista példákkal.

> 🚨 Gondolj azokra az esettanulmányokra, amelyeket láttál - tapasztaltál vagy érintett-e hasonló etikai kihívást az életedben? Tudsz legalább egy másik esettanulmányt, amely illusztrálja az ebben a szakaszban tárgyalt etikai kihívások egyikét?

## Alkalmazott etika

Beszéltünk az etikai fogalmakról, kihívásokról és esettanulmányokról valós kontextusban. De hogyan kezdhetjük el _alkalmazni_ az etikai elveket és gyakorlatokat a projektjeinkben? És hogyan _operacionalizálhatjuk_ ezeket a gyakorlatokat a jobb irányítás érdekében? Nézzünk meg néhány valós megoldást:

### 1. Szakmai kódexek

A szakmai kódexek egy lehetőséget kínálnak a szervezetek számára, hogy "ösztönözzék" tagjaikat az etikai elveik és küldetésük támogatására. A kódexek _erkölcsi iránymutatások_ a szakmai viselkedéshez, segítve az alkalmazottakat vagy tagokat olyan döntések meghozatalában, amelyek összhangban vannak a szervezet elveivel. Csak annyira hatékonyak, amennyire a tagok önkéntes megfelelése; azonban sok szervezet további jutalmakat és büntetéseket kínál, hogy motiválja a tagokat a megfelelésre.

Példák:
 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Etikai Kódex
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Magatartási Kódex (2013-ban létrehozva)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (1993 óta)

> 🚨 Tagja vagy valamilyen szakmai mérnöki vagy adatkutatási szervezetnek? Nézd meg a weboldalukat, hogy meghatároznak-e szakmai etikai kódexet. Mit mond ez az etikai elveikről? Hogyan "ösztönzik" a tagokat a kódex követésére?

### 2. Etikai ellenőrzőlisták

Míg a szakmai kódexek meghatározzák a szakemberek _etikai viselkedését_, [ismert korlátokkal](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) rendelkeznek a végrehajtásban, különösen nagyszabású projektek esetében. Ehelyett sok adatkutatási szakértő [ellenőrzőlistákat javasol](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), amelyek **összekapcsolják az elveket a gyakorlatokkal** determinisztikusabb és cselekvőképesebb módon.

Az ellenőrzőlisták a kérdéseket "igen/nem" feladatokká alakítják, amelyek operacionalizálhatók, lehetővé téve, hogy nyomon kövessék őket a szokásos termékkiadási munkafolyamatok részeként.

Példák:
 * [Deon](https://deon.drivendata.org/) - általános célú adatetikai ellenőrzőlista, amelyet [iparági ajánlások](https://deon.drivendata.org/#checklist-citations) alapján hoztak létre, parancssori eszközzel a könnyű integráció érdekében.
 * [Adatvédelmi audit ellenőrzőlista](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - általános iránymutatást nyújt az információkezelési gyakorlatokhoz jogi és társadalmi kitettség szempontjából.
 * [AI méltányossági ellenőrzőlista](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - AI szakemberek által létrehozva, hogy támogassák a méltányossági ellenőrzések bevezetését és integrációját az AI fejlesztési ciklusokba.
 * [22 kérdés az adatok és AI etikájáról](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - nyitottabb keretrendszer, amelyet az etikai kérdések kezdeti feltárására strukturáltak a tervezés, megvalósítás és szervezeti kontextusokban.

### 3. Etikai szabályozások

Az etika közös értékek meghatározásáról és a helyes cselekvésről szól _önkéntesen_. **Megfelelés** arról szól, hogy _követjük a törvényt_, ha és ahol meghatározták. **Irányítás** szélesebb értelemben magában foglalja az összes módot, ahogyan a szervezetek működnek az etikai elvek érvényesítése és a meghatározott törvények betartása érdekében.

Ma az irányítás két formát ölt a szervezeteken belül. Először is, az **etikus AI** elvek meghatározásáról és a gyakorlatok létrehozásáról szól, hogy operacionalizálják az elfogadást az összes AI-val kapcsolatos projektben a szervezeten belül. Másodszor, arról szól, hogy megfeleljenek az összes kormány által előírt **adatvédelmi szabályozásnak** azokban a régiókban, ahol működnek.

Adatvédelmi és adatvédelmi szabályozások példái:

 * `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - szabályozza a _szövetségi kormány_ személyes információk gyűjtését, használatát és közzétételét.
 * `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - védi a személyes egészségügyi adatokat.
 * `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - védi a 13 év alatti gyermekek adatvédelmét.
 * `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - felhasználói jogokat, adatvédelmet és adatbiztonságot biztosít.
 * `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) több _jogot_ biztosít a fogyasztóknak a (személyes) adataik felett.
 * `2021`, Kína [Személyes Információk Védelmi Törvénye](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) éppen elfogadva, létrehozva az egyik legerősebb online adatvédelmi szabályozást világszerte.

> 🚨 Az Európai Unió által meghatározott GDPR (Általános Adatvédelmi Rendelet) ma az egyik legbefolyásosabb adatvédelmi szabályozás. Tudtad, hogy [8 felhasználói jogot](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) is meghatároz a digitális adatvédelem és személyes adatok védelme érdek
* [A felelős mesterséges intelligencia alapelvei](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - ingyenes tanulási útvonal a Microsoft Learn-től.
* [Etika és adattudomány](https://resources.oreilly.com/examples/0636920203964) - O'Reilly EBook (M. Loukides, H. Mason és mások)
* [Adattudományi etika](https://www.coursera.org/learn/data-science-ethics#syllabus) - online kurzus a Michigani Egyetemtől.
* [Etika kibontva](https://ethicsunwrapped.utexas.edu/case-studies) - esettanulmányok a Texasi Egyetemtől.

# Feladat 

[Írj egy esettanulmányt az adatetikáról](assignment.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.