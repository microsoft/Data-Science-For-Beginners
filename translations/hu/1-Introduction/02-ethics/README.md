<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a34157cc63516eba97c89a0b2f8c3e6",
  "translation_date": "2025-09-03T21:43:48+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "hu"
}
-->
# Bevezetés az adatetikai kérdésekbe

|![ Sketchnote készítette: [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Adatelemzési etika - _Sketchnote készítette: [@nitya](https://twitter.com/nitya)_ |

---

Mindannyian adatpolgárok vagyunk egy adatközpontú világban.

A piaci trendek azt mutatják, hogy 2022-re minden harmadik nagy szervezet online [piactereken és csereplatformokon](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/) keresztül fog adatokat vásárolni és eladni. **Alkalmazásfejlesztőként** könnyebb és olcsóbb lesz adatvezérelt betekintéseket és algoritmusvezérelt automatizációt integrálni a mindennapi felhasználói élményekbe. Azonban ahogy az AI egyre elterjedtebbé válik, meg kell értenünk azokat a potenciális károkat is, amelyeket az ilyen algoritmusok [fegyveres alkalmazása](https://www.youtube.com/watch?v=TQHs8SA1qpk) okozhat nagy léptékben.

A trendek azt is mutatják, hogy 2025-re több mint [180 zettabájtnyi](https://www.statista.com/statistics/871513/worldwide-data-created/) adatot fogunk létrehozni és fogyasztani. **Adattudósként** ez példátlan szintű hozzáférést biztosít számunkra személyes adatokhoz. Ez lehetővé teszi, hogy viselkedési profilokat építsünk fel a felhasználókról, és befolyásoljuk döntéseiket olyan módon, amely [a szabad választás illúzióját](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) kelti, miközben esetlegesen a számunkra kedvező eredmények felé tereljük őket. Ez szélesebb körű kérdéseket vet fel az adatvédelemről és a felhasználói jogok védelméről.

Az adatetika mostanra _szükséges védőkorlát_ az adatelemzés és mérnöki munka számára, segítve a potenciális károk és nem szándékos következmények minimalizálását az adatvezérelt cselekvéseinkből. A [Gartner AI Hype Cycle](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) az adatetika, a felelős AI és az AI irányítás releváns trendjeit az AI _demokratizációja_ és _iparosítása_ körüli nagyobb megatrendek kulcsfontosságú hajtóerejeként azonosítja.

![Gartner AI Hype Cycle - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

Ebben a leckében az adatetika lenyűgöző területét fogjuk felfedezni - az alapfogalmaktól és kihívásoktól kezdve az esettanulmányokon és alkalmazott AI koncepciókon át, mint például az irányítás -, amelyek segítenek az etikai kultúra kialakításában az adatokat és AI-t használó csapatokban és szervezetekben.

## [Előadás előtti kvíz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## Alapvető definíciók

Kezdjük az alapvető terminológia megértésével.

Az "etika" szó a [görög "ethikos"](https://en.wikipedia.org/wiki/Ethics) (és annak "ethos" gyökere) szóból származik, amely _jellemet vagy erkölcsi természetet_ jelent.

**Etika** azokról a közös értékekről és erkölcsi elvekről szól, amelyek irányítják viselkedésünket a társadalomban. Az etika nem törvényeken alapul, hanem széles körben elfogadott normákon arról, hogy mi a "helyes és helytelen". Az etikai megfontolások azonban befolyásolhatják a vállalati irányítási kezdeményezéseket és a kormányzati szabályozásokat, amelyek több ösztönzőt teremtenek a megfelelésre.

**Adatetika** egy [új etikai ág](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1), amely "tanulmányozza és értékeli az _adatokkal, algoritmusokkal és kapcsolódó gyakorlatokkal_ kapcsolatos erkölcsi problémákat". Itt az **"adatok"** az adatok létrehozásával, rögzítésével, gondozásával, feldolgozásával, terjesztésével, megosztásával és felhasználásával kapcsolatos cselekvésekre összpontosítanak, az **"algoritmusok"** az AI-ra, ügynökökre, gépi tanulásra és robotokra, míg a **"gyakorlatok"** olyan témákra, mint a felelős innováció, programozás, hackelés és etikai kódexek.

**Alkalmazott etika** az [erkölcsi megfontolások gyakorlati alkalmazása](https://en.wikipedia.org/wiki/Applied_ethics). Ez az etikai kérdések aktív vizsgálatának folyamata a _valós cselekvések, termékek és folyamatok_ kontextusában, és korrekciós intézkedések megtétele annak érdekében, hogy ezek összhangban maradjanak a meghatározott etikai értékeinkkel.

**Etikai kultúra** az [_alkalmazott etika működőképessé tétele_](https://hbr.org/2019/05/how-to-design-an-ethical-organization), hogy biztosítsuk, hogy etikai elveink és gyakorlataink következetesen és skálázható módon kerüljenek alkalmazásra az egész szervezetben. A sikeres etikai kultúrák szervezet-szintű etikai elveket határoznak meg, jelentős ösztönzőket biztosítanak a megfeleléshez, és megerősítik az etikai normákat azáltal, hogy minden szinten ösztönzik és erősítik a kívánt viselkedéseket.

## Etikai fogalmak

Ebben a szakaszban olyan fogalmakat fogunk megvitatni, mint a **közös értékek** (elvek) és **etikai kihívások** (problémák) az adatetika területén - valamint **esettanulmányokat** fogunk vizsgálni, amelyek segítenek megérteni ezeket a fogalmakat valós kontextusban.

### 1. Etikai elvek

Minden adatetikai stratégia az _etikai elvek_ meghatározásával kezdődik - azokkal a "közös értékekkel", amelyek leírják az elfogadható viselkedéseket, és irányítják a megfelelési cselekvéseket adat- és AI-projektjeinkben. Ezeket egyéni vagy csapatszinten is meghatározhatjuk. Azonban a legtöbb nagy szervezet ezeket egy _etikus AI_ küldetésnyilatkozatban vagy keretrendszerben határozza meg, amelyet vállalati szinten definiálnak és következetesen érvényesítenek minden csapatban.

**Példa:** A Microsoft [Felelős AI](https://www.microsoft.com/en-us/ai/responsible-ai) küldetésnyilatkozata így szól: _"Elkötelezettek vagyunk az AI fejlődése iránt, amelyet etikai elvek vezérelnek, amelyek az embereket helyezik előtérbe"_ - az alábbi keretrendszerben 6 etikai elvet azonosítva:

![Felelős AI a Microsoftnál](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Nézzük meg röviden ezeket az elveket. A _transzparencia_ és _felelősségvállalás_ alapvető értékek, amelyekre a többi elv épül - kezdjük ezekkel:

* [**Felelősségvállalás**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) arra ösztönzi a szakembereket, hogy _felelősséget vállaljanak_ adat- és AI-műveleteikért, valamint az etikai elvek betartásáért.
* [**Transzparencia**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) biztosítja, hogy az adat- és AI-cselekvések _érthetőek_ legyenek a felhasználók számára, megmagyarázva a döntések mögötti mit és miért.
* [**Méltányosság**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - arra összpontosít, hogy az AI _minden embert_ méltányosan kezeljen, foglalkozva az adatokban és rendszerekben lévő szisztematikus vagy implicit szociotechnikai torzításokkal.
* [**Megbízhatóság és biztonság**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - biztosítja, hogy az AI _következetesen_ viselkedjen a meghatározott értékekkel összhangban, minimalizálva a potenciális károkat vagy nem szándékos következményeket.
* [**Adatvédelem és biztonság**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - az adatvonal megértéséről és a felhasználók számára _adatvédelem és kapcsolódó védelem_ biztosításáról szól.
* [**Befogadás**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - az AI-megoldások szándékos tervezéséről szól, hogy azok _széles körű emberi igényekhez_ és képességekhez alkalmazkodjanak.

> 🚨 Gondolkodj el azon, hogy mi lehetne az adatetikai küldetésnyilatkozatod. Fedezd fel más szervezetek etikus AI keretrendszereit - itt van néhány példa: [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles), és [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Milyen közös értékekkel rendelkeznek? Hogyan kapcsolódnak ezek az elvek az általuk működtetett AI-termékhez vagy iparághoz?

### 2. Etikai kihívások

Miután meghatároztuk az etikai elveket, a következő lépés az adat- és AI-cselekvéseink értékelése annak érdekében, hogy azok összhangban állnak-e ezekkel a közös értékekkel. Gondolj a cselekvéseidre két kategóriában: _adatgyűjtés_ és _algoritmus tervezés_.

Az adatgyűjtés során a cselekvések valószínűleg **személyes adatokat** vagy személyesen azonosítható információkat (PII) érintenek az azonosítható élő egyének számára. Ez magában foglalja a [különféle nem személyes adatokat](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en), amelyek _együttesen_ azonosítanak egy egyént. Az etikai kihívások az _adatvédelem_, _adatbirtoklás_ és kapcsolódó témák, mint például _tájékozott beleegyezés_ és _szellemi tulajdonjogok_ köré összpontosulhatnak.

Az algoritmus tervezés során a cselekvések magukban foglalják **adatkészletek** gyűjtését és gondozását, majd ezek felhasználását **adatmodellek** képzésére és telepítésére, amelyek valós kontextusban előrejelzéseket készítenek vagy automatizált döntéseket hoznak. Az etikai kihívások a _adatkészlet torzítás_, _adatminőség_ problémák, _méltánytalanság_ és _félrevezetés_ köré összpontosulhatnak az algoritmusokban - beleértve néhány szisztematikus jellegű problémát.

Mindkét esetben az etikai kihívások olyan területeket emelnek ki, ahol cselekvéseink konfliktusba kerülhetnek közös értékeinkkel. Az ilyen aggályok észleléséhez, enyhítéséhez, minimalizálásához vagy megszüntetéséhez erkölcsi "igen/nem" kérdéseket kell feltennünk cselekvéseinkkel kapcsolatban, majd szükség esetén korrekciós intézkedéseket kell tennünk. Nézzünk meg néhány etikai kihívást és az általuk felvetett erkölcsi kérdéseket:

#### 2.1 Adatbirtoklás

Az adatgyűjtés gyakran személyes adatokat érint, amelyek az adat alanyait azonosíthatják. Az [adatbirtoklás](https://permission.io/blog/data-ownership) az adatok létrehozásával, feldolgozásával és terjesztésével kapcsolatos _ellenőrzésről_ és [_felhasználói jogokról_](https://permission.io/blog/data-ownership) szól.

Az erkölcsi kérdések, amelyeket fel kell tennünk:
 * Ki birtokolja az adatokat? (felhasználó vagy szervezet)
 * Milyen jogai vannak az adat alanyainak? (pl. hozzáférés, törlés, hordozhatóság)
 * Milyen jogai vannak a szervezeteknek? (pl. rosszindulatú felhasználói vélemények helyreállítása)

#### 2.2 Tájékozott beleegyezés

A [tájékozott beleegyezés](https://legaldictionary.net/informed-consent/) azt jelenti, hogy a felhasználók egy cselekvéshez (például adatgyűjtéshez) _teljes körű megértéssel_ járulnak hozzá, beleértve a célt, a potenciális kockázatokat és az alternatívákat.

Itt felmerülő kérdések:
 * A felhasználó (adat alanya) engedélyt adott az adatok rögzítésére és felhasználására?
 * A felhasználó megértette, hogy miért gyűjtötték az adatokat?
 * A felhasználó megértette a részvételéből eredő potenciális kockázatokat?

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
 * A felhasználók (személyes) adatai védettek-e a hackelés és szivárgás ellen?
 * A felhasználók adatai csak jogosult felhasználók és kontextusok számára hozzáférhetők-e?
 * A felhasználók anonimitása megőrzött-e, amikor az adatokat megosztják vagy terjesztik?
 * Lehet-e egy felhasználót azonosítani anonimizált adatállományokból?

#### 2.5 Az elfeledtetés joga

Az [elfeledtet
[Algorithmusok méltányossága](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) azt vizsgálja, hogy az algoritmus tervezése szisztematikusan diszkriminál-e bizonyos adatcsoportok ellen, ami [potenciális károkat](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) okozhat az _elosztásban_ (ahol erőforrásokat tagadnak meg vagy vonnak vissza az adott csoporttól) és a _szolgáltatás minőségében_ (ahol az AI nem olyan pontos bizonyos csoportok esetében, mint másoknál).

Kérdések, amelyeket érdemes megvizsgálni:
 * Értékeltük-e a modell pontosságát különböző csoportok és feltételek esetében?
 * Vizsgáltuk-e a rendszert potenciális károk (pl. sztereotipizálás) szempontjából?
 * Tudjuk-e módosítani az adatokat vagy újratanítani a modelleket az azonosított károk enyhítése érdekében?

Fedezz fel olyan forrásokat, mint az [AI méltányossági ellenőrzőlisták](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA), hogy többet megtudj.

#### 2.9 Félrevezetés

[Adataz félrevezetése](https://www.sciencedirect.com/topics/computer-science/misrepresentation) arról szól, hogy vajon őszintén közölt adatokból származó betekintéseket megtévesztő módon kommunikálunk-e egy kívánt narratíva támogatása érdekében.

Kérdések, amelyeket érdemes megvizsgálni:
 * Jelentünk-e hiányos vagy pontatlan adatokat?
 * Úgy vizualizáljuk-e az adatokat, hogy az félrevezető következtetéseket eredményezzen?
 * Használunk-e szelektív statisztikai technikákat az eredmények manipulálására?
 * Vannak-e alternatív magyarázatok, amelyek más következtetést kínálhatnak?

#### 2.10 Szabad választás
A [szabad választás illúziója](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) akkor fordul elő, amikor a rendszer „választási architektúrái” döntéshozó algoritmusokat használnak arra, hogy az embereket egy preferált eredmény felé tereljék, miközben látszólag lehetőségeket és kontrollt kínálnak nekik. Ezek a [sötét minták](https://www.darkpatterns.org/) társadalmi és gazdasági károkat okozhatnak a felhasználóknak. Mivel a felhasználói döntések hatással vannak a viselkedési profilokra, ezek a cselekvések potenciálisan befolyásolják a jövőbeli választásokat, amelyek felerősíthetik vagy kiterjeszthetik ezen károk hatását.

Kérdések, amelyeket érdemes megvizsgálni:
 * Értette-e a felhasználó annak a választásnak a következményeit?
 * Tudott-e a felhasználó (alternatív) választási lehetőségekről és azok előnyeiről és hátrányairól?
 * Visszafordíthatja-e a felhasználó egy automatizált vagy befolyásolt döntést később?

### 3. Esettanulmányok

Ahhoz, hogy ezeket az etikai kihívásokat valós kontextusba helyezzük, érdemes olyan esettanulmányokat megvizsgálni, amelyek rávilágítanak az egyénekre és a társadalomra gyakorolt potenciális károkra és következményekre, amikor az ilyen etikai vétségeket figyelmen kívül hagyják.

Íme néhány példa:

| Etikai kihívás | Esettanulmány  | 
|--- |--- |
| **Tájékozott beleegyezés** | 1972 - [Tuskegee szifilisz tanulmány](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Az afrikai-amerikai férfiak, akik részt vettek a tanulmányban, ingyenes orvosi ellátást ígértek, _de megtévesztették őket_ a kutatók, akik nem tájékoztatták őket a diagnózisukról vagy a kezelés elérhetőségéről. Sok alany meghalt, és partnereik vagy gyermekeik is érintettek voltak; a tanulmány 40 évig tartott. | 
| **Adatvédelem** |  2007 - A [Netflix adatdíj](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) kutatóknak _10M anonimizált filmértékelést_ biztosított 50K ügyféltől az ajánlási algoritmusok javítása érdekében. Azonban a kutatók képesek voltak az anonimizált adatokat személyazonosító adatokkal összekapcsolni _külső adatbázisokban_ (pl. IMDb kommentek), hatékonyan „deanonimizálva” néhány Netflix előfizetőt.|
| **Gyűjtési torzítás**  | 2013 - Boston városa [kifejlesztette a Street Bump](https://www.boston.gov/transportation/street-bump) nevű alkalmazást, amely lehetővé tette a polgárok számára, hogy kátyúkat jelentsenek, jobb úthálózati adatokat biztosítva a városnak a problémák megtalálásához és javításához. Azonban [az alacsonyabb jövedelmű csoportoknak kevesebb hozzáférésük volt autókhoz és telefonokhoz](https://hbr.org/2013/04/the-hidden-biases-in-big-data), így az ő úthálózati problémáik láthatatlanok maradtak az alkalmazásban. A fejlesztők akadémikusokkal dolgoztak együtt az _egyenlő hozzáférés és digitális szakadék_ kérdéseinek megoldása érdekében. |
| **Algoritmusok méltányossága**  | 2018 - Az MIT [Gender Shades Study](http://gendershades.org/overview.html) értékelte a nemek osztályozására szolgáló AI termékek pontosságát, feltárva a pontossági hiányosságokat a nők és színes bőrűek esetében. Egy [2019-es Apple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) látszólag kevesebb hitelt kínált a nőknek, mint a férfiaknak. Mindkettő rávilágított az algoritmikus torzítás problémáira, amelyek társadalmi-gazdasági károkat okoztak.|
| **Adatok félrevezetése** | 2020 - A [Georgia Egészségügyi Minisztérium COVID-19 grafikonokat](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) tett közzé, amelyek látszólag félrevezették a polgárokat az igazolt esetek trendjeiről a nem kronológiai sorrendben elhelyezett x-tengely miatt. Ez a vizualizációs trükkök általi félrevezetést illusztrálja. |
| **Szabad választás illúziója** | 2020 - A tanulási alkalmazás [ABCmouse 10M dollárt fizetett az FTC panasz rendezésére](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/), ahol a szülők nem tudták lemondani az előfizetéseket, amelyekbe „csapdába estek”. Ez a választási architektúrák sötét mintáit illusztrálja, ahol a felhasználókat potenciálisan káros döntések felé terelték. |
| **Adatvédelem és felhasználói jogok** | 2021 - A Facebook [adatvédelmi incidens](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) 530M felhasználó adatait tette ki, ami 5B dolláros egyezséget eredményezett az FTC-vel. Azonban megtagadta a felhasználók értesítését az incidensről, megsértve a felhasználói jogokat az adatok átláthatóságával és hozzáférésével kapcsolatban. |

Szeretnél további esettanulmányokat felfedezni? Nézd meg ezeket a forrásokat:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - etikai dilemmák különböző iparágakban. 
* [Data Science Ethics course](https://www.coursera.org/learn/data-science-ethics#syllabus) - mérföldkőnek számító esettanulmányok.
* [Where things have gone wrong](https://deon.drivendata.org/examples/) - deon ellenőrzőlista példákkal.


> 🚨 Gondolj az általad látott esettanulmányokra - tapasztaltál vagy érintett voltál hasonló etikai kihívásban az életedben? Tudsz legalább egy másik esettanulmányt, amely illusztrálja az ebben a szakaszban tárgyalt etikai kihívások egyikét?

## Alkalmazott etika

Beszéltünk az etikai fogalmakról, kihívásokról és esettanulmányokról valós kontextusban. De hogyan kezdhetjük el _alkalmazni_ az etikai elveket és gyakorlatokat a projektjeinkben? És hogyan _operacionalizálhatjuk_ ezeket a gyakorlatokat a jobb irányítás érdekében? Nézzünk meg néhány valós megoldást:

### 1. Szakmai kódexek

A szakmai kódexek egy lehetőséget kínálnak a szervezetek számára, hogy „ösztönözzék” tagjaikat az etikai elvek és küldetésnyilatkozat támogatására. A kódexek _erkölcsi iránymutatások_ a szakmai viselkedéshez, segítve az alkalmazottakat vagy tagokat olyan döntések meghozatalában, amelyek összhangban vannak a szervezet elveivel. Csak annyira hatékonyak, amennyire a tagok önkéntes megfelelése; azonban sok szervezet további jutalmakat és büntetéseket kínál a megfelelés ösztönzésére.

Példák:
 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Etikai Kódex
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Magatartási Kódex (2013-ban létrehozva)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (1993 óta)

> 🚨 Tagja vagy valamilyen szakmai mérnöki vagy adatkutatási szervezetnek? Nézd meg a weboldalukat, hogy meghatároznak-e szakmai etikai kódexet. Mit mond ez az etikai elveikről? Hogyan „ösztönzik” a tagokat a kódex követésére?

### 2. Etikai ellenőrzőlisták

Míg a szakmai kódexek meghatározzák a szakemberek _etikai viselkedését_, [ismert korlátokkal](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) rendelkeznek a végrehajtásban, különösen nagyszabású projektek esetében. Ehelyett sok adatkutatási szakértő [ellenőrzőlistákat javasol](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), amelyek **összekapcsolják az elveket a gyakorlatokkal** determinisztikusabb és cselekvőképesebb módon.

Az ellenőrzőlisták a kérdéseket „igen/nem” feladatokká alakítják, amelyek operacionalizálhatók, lehetővé téve, hogy nyomon kövessék őket a szokásos termékkiadási munkafolyamatok részeként.

Példák:
 * [Deon](https://deon.drivendata.org/) - általános célú adatetikai ellenőrzőlista, amelyet [iparági ajánlások](https://deon.drivendata.org/#checklist-citations) alapján hoztak létre, parancssori eszközzel a könnyű integráció érdekében.
 * [Adatvédelmi audit ellenőrzőlista](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - általános iránymutatást nyújt az információkezelési gyakorlatokhoz jogi és társadalmi kitettség szempontjából.
 * [AI méltányossági ellenőrzőlista](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - AI szakemberek által létrehozva, hogy támogassa a méltányossági ellenőrzések bevezetését és integrációját az AI fejlesztési ciklusokba.
 * [22 kérdés az adatok és AI etikájáról](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - nyitottabb keretrendszer, amelyet az etikai kérdések kezdeti feltárására terveztek a tervezés, megvalósítás és szervezeti kontextusokban.

### 3. Etikai szabályozások

Az etika közös értékek meghatározásáról és a helyes cselekvésről szól _önkéntesen_. **Megfelelés** a _törvények betartásáról_ szól, ha és ahol meghatározták. **Irányítás** szélesebb értelemben magában foglalja az összes olyan módot, ahogyan a szervezetek működnek az etikai elvek érvényesítése és a meghatározott törvények betartása érdekében.

Ma az irányítás két formát ölt a szervezeteken belül. Először is, az **etikus AI** elvek meghatározásáról és a gyakorlatok létrehozásáról szól, amelyek operacionalizálják az elfogadást az összes AI-val kapcsolatos projektben a szervezeten belül. Másodszor, az összes kormány által előírt **adatvédelmi szabályozásnak** való megfelelésről szól azokban a régiókban, ahol működik.

Adatvédelmi és adatvédelmi szabályozások példái:

 * `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - szabályozza a _szövetségi kormány_ személyes adatok gyűjtését, használatát és közzétételét.
 * `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - védi a személyes egészségügyi adatokat.
 * `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - védi a 13 év alatti gyermekek adatvédelmét.
 * `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - felhasználói jogokat, adatvédelmet és adatbiztonságot biztosít.
 * `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) több _jogot_ biztosít a fogyasztóknak a személyes adataik felett.
 * `2021`, Kína [Személyes Adatvédelmi Törvénye](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) éppen elfogadva, létrehozva az egyik legerősebb online adatvédelmi szabályozást világszerte.

> 🚨 Az Európai Unió által meghatározott GDPR (General Data Protection Regulation) ma az egyik legbefolyásosabb adatvédelmi szabályozás. Tudtad, hogy [8 felhasználói jogot](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) is meghatároz a polgárok digitális adatvédelmének és személyes adatainak védelmére? Ismerd meg, mik ezek, és miért fontosak.

### 4. Etikai kultúra

Fontos meg
* [A felelős mesterséges intelligencia alapelvei](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - ingyenes tanulási útvonal a Microsoft Learn-től.
* [Etika és adat tudomány](https://resources.oreilly.com/examples/0636920203964) - O'Reilly EBook (M. Loukides, H. Mason és mások)
* [Adattudományi etika](https://www.coursera.org/learn/data-science-ethics#syllabus) - online kurzus a Michigani Egyetemtől.
* [Etika kibontva](https://ethicsunwrapped.utexas.edu/case-studies) - esettanulmányok a Texasi Egyetemtől.

# Feladat 

[Írj egy adatetikai esettanulmányt](assignment.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.