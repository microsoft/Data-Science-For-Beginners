<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a34157cc63516eba97c89a0b2f8c3e6",
  "translation_date": "2025-09-03T21:54:57+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "sl"
}
-->
# Uvod v podatkovno etiko

|![ Sketchnote avtorja [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Etika podatkovne znanosti - _Sketchnote avtorja [@nitya](https://twitter.com/nitya)_ |

---

Vsi smo podatkovni državljani, ki živimo v svetu, prežetem s podatki.

Tržni trendi kažejo, da bo do leta 2022 1 od 3 velikih organizacij kupovala in prodajala svoje podatke prek spletnih [tržnic in izmenjav](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/). Kot **razvijalci aplikacij** bomo lažje in ceneje vključili vpoglede, ki temeljijo na podatkih, ter avtomatizacijo, ki jo poganjajo algoritmi, v vsakodnevne uporabniške izkušnje. Toda z razširjenostjo umetne inteligence bomo morali razumeti tudi potencialne škodljive učinke [uporabe algoritmov kot orožja](https://www.youtube.com/watch?v=TQHs8SA1qpk) v velikem obsegu.

Trend kaže tudi, da bomo do leta 2025 ustvarili in porabili več kot [180 zettabajtov](https://www.statista.com/statistics/871513/worldwide-data-created/) podatkov. Kot **podatkovni znanstveniki** bomo imeli neprimerljivo raven dostopa do osebnih podatkov. To nam omogoča gradnjo vedenjskih profilov uporabnikov in vplivanje na sprejemanje odločitev na načine, ki ustvarjajo [iluzijo svobodne izbire](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice), hkrati pa potencialno usmerjajo uporabnike k izidom, ki jih sami preferiramo. To pa odpira širša vprašanja o zasebnosti podatkov in zaščiti uporabnikov.

Podatkovna etika je zdaj _nujna varovalka_ za podatkovno znanost in inženiring, ki nam pomaga zmanjšati potencialne škodljive učinke in nenamerne posledice naših dejanj, ki temeljijo na podatkih. [Gartnerjev Hype Cycle za AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) identificira relevantne trende v digitalni etiki, odgovorni AI in upravljanju AI kot ključne dejavnike večjih megatrendov okoli _demokratizacije_ in _industrializacije_ umetne inteligence.

![Gartnerjev Hype Cycle za AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

V tej lekciji bomo raziskali fascinantno področje podatkovne etike - od osnovnih konceptov in izzivov do študij primerov in uporabljenih konceptov AI, kot je upravljanje, ki pomagajo vzpostaviti kulturo etike v ekipah in organizacijah, ki delajo s podatki in umetno inteligenco.

## [Predhodni kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## Osnovne definicije

Začnimo z razumevanjem osnovne terminologije.

Beseda "etika" izhaja iz [grške besede "ethikos"](https://en.wikipedia.org/wiki/Ethics) (in njenega korena "ethos"), ki pomeni _značaj ali moralna narava_.

**Etika** se nanaša na skupne vrednote in moralna načela, ki usmerjajo naše vedenje v družbi. Etika temelji ne na zakonih, temveč na splošno sprejetih normah, kaj je "prav vs. narobe". Vendar pa lahko etične premisleke vplivajo na pobude korporativnega upravljanja in vladne regulacije, ki ustvarjajo več spodbud za skladnost.

**Podatkovna etika** je [nova veja etike](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1), ki "preučuje in ocenjuje moralne probleme, povezane s _podatki, algoritmi in ustreznimi praksami_". Tukaj se **"podatki"** osredotočajo na dejanja, povezana z generiranjem, beleženjem, kuriranjem, obdelavo, razširjanjem, deljenjem in uporabo, **"algoritmi"** se osredotočajo na AI, agente, strojno učenje in robote, medtem ko se **"prakse"** osredotočajo na teme, kot so odgovorne inovacije, programiranje, hekanje in kodeks etike.

**Uporabljena etika** je [praktična uporaba moralnih premislekov](https://en.wikipedia.org/wiki/Applied_ethics). Gre za proces aktivnega raziskovanja etičnih vprašanj v kontekstu _dejanskih dejanj, izdelkov in procesov_ ter sprejemanja korektivnih ukrepov, da ostanejo skladni z našimi opredeljenimi etičnimi vrednotami.

**Kultura etike** se nanaša na [_operacionalizacijo_ uporabljene etike](https://hbr.org/2019/05/how-to-design-an-ethical-organization), da zagotovimo, da so naša etična načela in prakse sprejeta na dosleden in razširljiv način po celotni organizaciji. Uspešne kulture etike opredelijo organizacijsko široka etična načela, zagotavljajo smiselne spodbude za skladnost in krepijo etične norme z vzpodbujanjem in amplifikacijo želenih vedenj na vseh ravneh organizacije.

## Koncepti etike

V tem razdelku bomo razpravljali o konceptih, kot so **skupne vrednote** (načela) in **etični izzivi** (problemi) za podatkovno etiko - ter raziskali **študije primerov**, ki vam pomagajo razumeti te koncepte v realnih kontekstih.

### 1. Načela etike

Vsaka strategija podatkovne etike se začne z opredelitvijo _etičnih načel_ - "skupnih vrednot", ki opisujejo sprejemljiva vedenja in usmerjajo skladna dejanja v naših projektih, povezanih s podatki in AI. Ta načela lahko opredelite na individualni ali skupinski ravni. Vendar pa večina velikih organizacij opredeli ta načela v _etičnem AI_ misijskem izjavi ali okviru, ki je opredeljen na korporativni ravni in dosledno uveljavljen v vseh ekipah.

**Primer:** Microsoftova [Odgovorna AI](https://www.microsoft.com/en-us/ai/responsible-ai) misijska izjava se glasi: _"Zavezani smo k napredku AI, ki ga vodijo etična načela, ki postavljajo ljudi na prvo mesto"_ - opredeljuje 6 etičnih načel v spodnjem okviru:

![Odgovorna AI pri Microsoftu](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Na kratko raziščimo ta načela. _Transparentnost_ in _odgovornost_ sta temeljni vrednoti, na katerih temeljijo druga načela - zato začnimo tam:

* [**Odgovornost**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) zahteva, da so praktiki _odgovorni_ za svoje podatkovne in AI operacije ter skladnost s temi etičnimi načeli.
* [**Transparentnost**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) zagotavlja, da so dejanja, povezana s podatki in AI, _razumljiva_ (interpretabilna) za uporabnike, pojasnjujoč kaj in zakaj za odločitvami.
* [**Pravičnost**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - se osredotoča na zagotavljanje, da AI _vse ljudi_ obravnava pravično, obravnavajoč sistemske ali implicitne socio-tehnične pristranskosti v podatkih in sistemih.
* [**Zanesljivost in varnost**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - zagotavlja, da AI deluje _dosledno_ z opredeljenimi vrednotami, zmanjšuje potencialne škodljive učinke ali nenamerne posledice.
* [**Zasebnost in varnost**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - se nanaša na razumevanje izvora podatkov ter zagotavljanje _zasebnosti podatkov in povezanih zaščit_ za uporabnike.
* [**Vključenost**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - se nanaša na oblikovanje AI rešitev z namenom, prilagajanje za izpolnjevanje _širokega spektra človeških potreb_ in sposobnosti.

> 🚨 Razmislite, kakšna bi lahko bila vaša misijska izjava o podatkovni etiki. Raziščite etične AI okvire drugih organizacij - tukaj so primeri od [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles) in [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Katere skupne vrednote imajo? Kako se ta načela nanašajo na AI izdelke ali industrijo, v kateri delujejo?

### 2. Etični izzivi

Ko imamo opredeljena etična načela, je naslednji korak oceniti naša dejanja, povezana s podatki in AI, da vidimo, ali so skladna s temi skupnimi vrednotami. Razmislite o svojih dejanjih v dveh kategorijah: _zbiranje podatkov_ in _oblikovanje algoritmov_.

Pri zbiranju podatkov bodo dejanja verjetno vključevala **osebne podatke** ali osebno prepoznavne informacije (PII) za prepoznavne žive posameznike. To vključuje [raznolike elemente neosebnih podatkov](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en), ki _skupno_ identificirajo posameznika. Etični izzivi se lahko nanašajo na _zasebnost podatkov_, _lastništvo podatkov_ in povezana vprašanja, kot so _informirano soglasje_ ter _pravice intelektualne lastnine_ za uporabnike.

Pri oblikovanju algoritmov bodo dejanja vključevala zbiranje in kuriranje **naborov podatkov**, nato pa njihovo uporabo za treniranje in uvajanje **podatkovnih modelov**, ki napovedujejo izide ali avtomatizirajo odločitve v realnih kontekstih. Etični izzivi se lahko pojavijo zaradi _pristranskosti nabora podatkov_, _težav s kakovostjo podatkov_, _nepravičnosti_ in _napačne predstavitve_ v algoritmih - vključno z nekaterimi vprašanji, ki so sistemske narave.

V obeh primerih etični izzivi izpostavljajo področja, kjer lahko naša dejanja naletijo na konflikt z našimi skupnimi vrednotami. Da bi zaznali, ublažili, zmanjšali ali odpravili te skrbi, moramo zastaviti moralna "da/ne" vprašanja, povezana z našimi dejanji, nato pa po potrebi sprejeti korektivne ukrepe. Poglejmo si nekaj etičnih izzivov in moralnih vprašanj, ki jih sprožajo:

#### 2.1 Lastništvo podatkov

Zbiranje podatkov pogosto vključuje osebne podatke, ki lahko identificirajo podatkovne subjekte. [Lastništvo podatkov](https://permission.io/blog/data-ownership) se nanaša na _nadzor_ in [_pravice uporabnikov_](https://permission.io/blog/data-ownership), povezane z ustvarjanjem, obdelavo in razširjanjem podatkov.

Moralna vprašanja, ki jih moramo zastaviti, so:
 * Kdo je lastnik podatkov? (uporabnik ali organizacija)
 * Katere pravice imajo podatkovni subjekti? (npr. dostop, izbris, prenosljivost)
 * Katere pravice imajo organizacije? (npr. popravljanje zlonamernih uporabniških ocen)

#### 2.2 Informirano soglasje

[Informirano soglasje](https://legaldictionary.net/informed-consent/) opredeljuje dejanje, ko uporabniki privolijo v dejanje (npr. zbiranje podatkov) z _polnim razumevanjem_ relevantnih dejstev, vključno z namenom, potencialnimi tveganji in alternativami.

Vprašanja za raziskovanje tukaj so:
 * Ali je uporabnik (podatkovni subjekt) dal dovoljenje za zajemanje in uporabo podatkov?
 * Ali je uporabnik razumel namen, za katerega so bili podatki zajeti?
 * Ali je uporabnik razumel potencialna tveganja zaradi svoje udeležbe?

#### 2.3 Intelektualna lastnina

[Intelektualna lastnina](https://en.wikipedia.org/wiki/Intellectual_property) se nanaša na nematerialne stvaritve, ki izhajajo iz človeške pobude in lahko _imajo ekonomsko vrednost_ za posameznike ali podjetja.

Vprašanja za raziskovanje tukaj so:
 * Ali imajo zbrani podatki ekonomsko vrednost za uporabnika ali podjetje?
 * Ali ima **uporabnik** tukaj intelektualno lastnino?
 * Ali ima **organizacija** tukaj intelektualno lastnino?
 * Če te pravice obstajajo, kako jih ščitimo?

#### 2.4 Zasebnost podatkov

[Zasebnost podatkov](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) ali informacijska zasebnost se nanaša na ohranjanje zasebnosti uporabnikov in zaščito identitete uporabnikov glede osebno prepoznavnih informacij.

Vprašanja za raziskovanje tukaj so:
 * Ali so uporabnikovi (osebni) podatki zaščiteni pred vdori in uhajanjem?
 * Ali so uporabnikovi podatki dostopni le pooblaščenim uporabnikom in kontekstom?
 * Ali je uporabnikova anonimnost ohranjena, ko so podatki deljeni ali razširjeni?
 * Ali je mogoče uporabnika de-identificirati iz anonimiziranih naborov podatkov?

#### 2.5 Pravica do pozabe

[Pravica do pozabe](https://en.wikipedia.org/wiki/Right_to_be_forgotten) ali [pravica do izbrisa](https://www.gdpreu.org/right-to-be-forgotten/) zagotavlja dodatno zaščito osebnih podatkov uporabnikom. Konkretno, daje uporabnikom pravico zahtevati izbris ali odstranitev osebnih podatkov iz internetnih iskanj in drugih lokacij, _pod določenimi pogoji_ - kar jim omogoča nov začetek na spletu brez preteklih dejanj, ki bi jih bremenila.

Vprašanja za raziskovanje tukaj so:
 * Ali sistem omogoča podatkovnim subjektom zahtevo za izbris?
 * Ali bi morala umaknitev uporabniškega soglasja sprožiti avtomatiziran izbris?
 * Ali so bili podatki zbrani brez soglasja ali na nezakonit način?
 * Ali smo skladni z vladnimi regulacijami za zasebnost podatkov?

#### 2.6 Pristranskost nabora podatkov

Pristranskost nabora podatkov ali [pristranskost zbiranja](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) se nanaša na izbiro _nereprezentativnega_ podnabora podatkov za razvoj algoritmov, kar lahko povzroči potencialno nepravičnost v rezultatih za raznolike skupine. Vrste pristranskosti vključujejo pristranskost izbire ali vzorčenja, pristranskost prostovoljcev in pristranskost instrumentov.

Vprašanja za raziskovanje tukaj so:
 * Ali smo pridobili reprezentativen nabor podatkovnih subjektov?
 * Ali smo testirali naš zbrani ali kurirani nabor podatkov za različne pristranskosti?
 * Ali lahko ublažimo ali odstranimo odkrite pristranskosti?

#### 2.7 Kakovost podatkov

[Kakovost podatkov](https://lakefs.io/data-quality-testing/) preverja veljavnost kuriranega nabora podatkov, uporabljenega za razvoj naših algoritmov, preverja, ali značilnosti in zapisi izpolnjujejo zahteve za raven natančnosti in doslednosti, ki je potrebna za naš AI namen.

Vprašanja za raziskovanje tukaj so:
 * Ali smo zajeli veljavne _značilnosti_ za naš primer uporabe?
 * Ali so bili podatki zajeti _dosledno_ iz raznolikih virov podatkov?
 * Ali je nabor podatkov _popoln_ za raznolike pogoje ali scenarije?
 * Ali so informacije zajete _natančno_
[Algorithm Fairness](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) preverja, ali zasnova algoritma sistematično diskriminira določene podskupine podatkovnih subjektov, kar lahko vodi do [potencialnih škod](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) pri _dodeljevanju_ (kjer so sredstva zavrnjena ali zadržana za to skupino) in _kakovosti storitev_ (kjer AI ni tako natančen za nekatere podskupine kot za druge).

Vprašanja, ki jih je treba raziskati:
 * Ali smo ocenili natančnost modela za različne podskupine in pogoje?
 * Ali smo sistem preverili glede potencialnih škod (npr. stereotipiziranje)?
 * Ali lahko spremenimo podatke ali ponovno usposobimo modele za zmanjšanje ugotovljenih škod?

Raziskujte vire, kot so [AI Fairness checklists](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA), da izveste več.

#### 2.9 Napačna predstavitev

[Napačna predstavitev podatkov](https://www.sciencedirect.com/topics/computer-science/misrepresentation) se nanaša na vprašanje, ali sporočamo vpoglede iz pošteno poročanih podatkov na zavajajoč način, da podpiramo želeno pripoved.

Vprašanja, ki jih je treba raziskati:
 * Ali poročamo o nepopolnih ali netočnih podatkih?
 * Ali vizualiziramo podatke na način, ki vodi do zavajajočih zaključkov?
 * Ali uporabljamo selektivne statistične tehnike za manipulacijo rezultatov?
 * Ali obstajajo alternativne razlage, ki bi lahko ponudile drugačen zaključek?

#### 2.10 Svobodna izbira
[Iluzija svobodne izbire](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) se pojavi, ko "arhitekture izbire" sistema uporabljajo algoritme za sprejemanje odločitev, da ljudi usmerijo k želenemu izidu, medtem ko jim dajejo občutek možnosti in nadzora. Ti [temni vzorci](https://www.darkpatterns.org/) lahko povzročijo socialno in ekonomsko škodo uporabnikom. Ker odločitve uporabnikov vplivajo na vedenjske profile, lahko te akcije potencialno poganjajo prihodnje izbire, ki lahko okrepijo ali podaljšajo vpliv teh škod.

Vprašanja, ki jih je treba raziskati:
 * Ali je uporabnik razumel posledice sprejemanja te izbire?
 * Ali je bil uporabnik seznanjen z (alternativnimi) izbirami in prednostmi ter slabostmi vsake?
 * Ali lahko uporabnik kasneje razveljavi avtomatizirano ali vplivano izbiro?

### 3. Študije primerov

Da bi te etične izzive postavili v kontekst resničnega sveta, je koristno pogledati študije primerov, ki poudarjajo potencialne škode in posledice za posameznike in družbo, kadar se takšne kršitve etike prezrejo.

Tukaj je nekaj primerov:

| Etični izziv | Študija primera | 
|--- |--- |
| **Informirano soglasje** | 1972 - [Študija sifilisa Tuskegee](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Afroameriškim moškim, ki so sodelovali v študiji, so obljubili brezplačno zdravstveno oskrbo, _vendar so jih raziskovalci zavajali_, saj jim niso povedali za diagnozo ali razpoložljivost zdravljenja. Veliko udeležencev je umrlo, prizadeti pa so bili tudi partnerji in otroci; študija je trajala 40 let. | 
| **Zasebnost podatkov** | 2007 - [Netflixova nagrada za podatke](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) je raziskovalcem zagotovila _10M anonimiziranih ocen filmov od 50K strank_, da bi izboljšali algoritme priporočanja. Vendar so raziskovalci uspeli povezati anonimizirane podatke z osebnimi podatki v _zunanjih zbirkah podatkov_ (npr. komentarji na IMDb) - učinkovito "deanonimizirali" nekatere naročnike Netflixa.|
| **Pristranskost pri zbiranju podatkov** | 2013 - Mesto Boston je [razvilo Street Bump](https://www.boston.gov/transportation/street-bump), aplikacijo, ki je državljanom omogočila prijavo lukenj na cestah, kar je mestu zagotovilo boljše podatke o cestah za odpravljanje težav. Vendar pa [ljudje z nižjimi dohodki niso imeli enakega dostopa do avtomobilov in telefonov](https://hbr.org/2013/04/the-hidden-biases-in-big-data), zaradi česar so bile njihove težave na cestah nevidne v tej aplikaciji. Razvijalci so sodelovali z akademiki pri reševanju vprašanj _enakopravnega dostopa in digitalnih vrzeli_ za pravičnost. |
| **Pravičnost algoritmov** | 2018 - MIT [Gender Shades Study](http://gendershades.org/overview.html) je ocenila natančnost AI produktov za klasifikacijo spola, razkrivajoč vrzeli v natančnosti za ženske in osebe barve. [Apple Card iz leta 2019](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) je očitno ponujala manj kreditov ženskam kot moškim. Obe študiji sta pokazali težave pristranskosti algoritmov, ki vodijo do socio-ekonomskih škod.|
| **Napačna predstavitev podatkov** | 2020 - [Oddelek za javno zdravje Georgie je objavil COVID-19 grafe](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening), ki so zavajali državljane glede trendov potrjenih primerov z ne-kronološkim razvrščanjem na x-osi. To ponazarja napačno predstavitev s triki vizualizacije. |
| **Iluzija svobodne izbire** | 2020 - Učna aplikacija [ABCmouse je plačala 10M za poravnavo pritožbe FTC](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/), kjer so bili starši ujeti v plačevanje naročnin, ki jih niso mogli preklicati. To ponazarja temne vzorce v arhitekturah izbire, kjer so bili uporabniki usmerjeni k potencialno škodljivim odločitvam. |
| **Zasebnost podatkov in pravice uporabnikov** | 2021 - Facebook [kršitev podatkov](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) je razkrila podatke 530M uporabnikov, kar je privedlo do poravnave v višini 5B z FTC. Vendar pa ni obvestil uporabnikov o kršitvi, kar je kršilo pravice uporabnikov glede transparentnosti podatkov in dostopa. |

Želite raziskati več študij primerov? Oglejte si te vire:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - etične dileme v različnih industrijah. 
* [Tečaj o etiki podatkovne znanosti](https://www.coursera.org/learn/data-science-ethics#syllabus) - raziskane ključne študije primerov.
* [Kje so stvari šle narobe](https://deon.drivendata.org/examples/) - kontrolni seznam Deon z primeri.

> 🚨 Razmislite o študijah primerov, ki ste jih videli - ali ste doživeli ali bili prizadeti zaradi podobnega etičnega izziva v svojem življenju? Ali lahko pomislite na vsaj eno drugo študijo primera, ki ponazarja enega od etičnih izzivov, o katerih smo razpravljali v tem razdelku?

## Uporabna etika

Pogovarjali smo se o konceptih etike, izzivih in študijah primerov v kontekstih resničnega sveta. Toda kako začeti _uporabljati_ etična načela in prakse v svojih projektih? In kako _operacionalizirati_ te prakse za boljše upravljanje? Raziskujmo nekaj rešitev iz resničnega sveta:

### 1. Profesionalni kodeksi

Profesionalni kodeksi ponujajo eno možnost za organizacije, da "spodbujajo" člane k podpori njihovih etičnih načel in poslanstva. Kodeksi so _moralne smernice_ za profesionalno vedenje, ki pomagajo zaposlenim ali članom sprejemati odločitve, ki so skladne z načeli njihove organizacije. Njihova učinkovitost je odvisna od prostovoljne skladnosti članov; vendar pa mnoge organizacije ponujajo dodatne nagrade in kazni za motivacijo skladnosti članov.

Primeri vključujejo:

 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Kodeks etike
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Kodeks ravnanja (ustvarjen leta 2013)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (od leta 1993)

> 🚨 Ali pripadate profesionalni inženirski ali podatkovno-znanstveni organizaciji? Raziskujte njihovo spletno stran, da vidite, ali definirajo profesionalni kodeks etike. Kaj to pove o njihovih etičnih načelih? Kako "spodbujajo" člane k upoštevanju kodeksa?

### 2. Etični kontrolni seznami

Medtem ko profesionalni kodeksi definirajo zahtevano _etično vedenje_ od praktikov, imajo [znane omejitve](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) pri izvajanju, zlasti pri velikih projektih. Namesto tega mnogi strokovnjaki za podatkovno znanost [zagovarjajo kontrolne sezname](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), ki lahko **povežejo načela s praksami** na bolj determinističen in izvedljiv način.

Kontrolni seznami pretvorijo vprašanja v "da/ne" naloge, ki jih je mogoče operacionalizirati, kar omogoča njihovo sledenje kot del standardnih delovnih tokov za izdajo izdelkov.

Primeri vključujejo:
 * [Deon](https://deon.drivendata.org/) - splošni kontrolni seznam etike podatkov, ustvarjen iz [priporočil industrije](https://deon.drivendata.org/#checklist-citations) z orodjem ukazne vrstice za enostavno integracijo.
 * [Kontrolni seznam za revizijo zasebnosti](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - zagotavlja splošne smernice za ravnanje z informacijami z vidika pravne in socialne izpostavljenosti.
 * [Kontrolni seznam pravičnosti AI](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - ustvarjen s strani AI praktikov za podporo sprejemanju in integraciji preverjanj pravičnosti v razvojne cikle AI.
 * [22 vprašanj za etiko v podatkih in AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - bolj odprt okvir, strukturiran za začetno raziskovanje etičnih vprašanj v oblikovanju, izvajanju in organizacijskih kontekstih.

### 3. Etika in regulacije

Etika je o definiranju skupnih vrednot in prostovoljnem ravnanju _pravilno_. **Skladnost** je o _upoštevanju zakonov_, če in kjer so opredeljeni. **Upravljanje** na splošno zajema vse načine, kako organizacije delujejo za uveljavljanje etičnih načel in skladnost z uveljavljenimi zakoni.

Danes upravljanje poteka v dveh oblikah znotraj organizacij. Prvič, gre za definiranje **etičnih AI** načel in vzpostavitev praks za operacionalizacijo sprejemanja v vseh projektih, povezanih z AI, v organizaciji. Drugič, gre za skladnost z vsemi vladno določenimi **regulacijami zaščite podatkov** za regije, v katerih deluje.

Primeri regulacij zaščite podatkov in zasebnosti:

 * `1974`, [Zakon o zasebnosti ZDA](https://www.justice.gov/opcl/privacy-act-1974) - ureja _zbiranje, uporabo in razkritje osebnih podatkov_ s strani zvezne vlade.
 * `1996`, [Zakon o prenosljivosti in odgovornosti zdravstvenega zavarovanja ZDA (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - ščiti osebne zdravstvene podatke.
 * `1998`, [Zakon o zasebnosti otrok na spletu ZDA (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - ščiti zasebnost podatkov otrok, mlajših od 13 let.
 * `2018`, [Splošna uredba o varstvu podatkov (GDPR)](https://gdpr-info.eu/) - zagotavlja pravice uporabnikov, zaščito podatkov in zasebnost.
 * `2018`, [Kalifornijski zakon o zasebnosti potrošnikov (CCPA)](https://www.oag.ca.gov/privacy/ccpa) daje potrošnikom več _pravic_ nad njihovimi (osebnimi) podatki.
 * `2021`, Kitajska [Zakon o zaščiti osebnih podatkov](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) je pravkar sprejet, kar ustvarja eno najmočnejših regulacij zasebnosti podatkov na spletu na svetu.

> 🚨 Evropska unija je definirala GDPR (Splošna uredba o varstvu podatkov), ki ostaja ena najvplivnejših regulacij zasebnosti podatkov danes. Ali ste vedeli, da definira tudi [8 pravic uporabnikov](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) za zaščito digitalne zasebnosti in osebnih podatkov državljanov? Naučite se, kaj so te pravice in zakaj so pomembne.

### 4. Kultura etike

Upoštevajte, da ostaja neoprijemljiva vrzel med _skladnostjo_ (narediti dovolj, da izpolnimo "črko zakona") in obravnavanjem [sistemskih vprašanj](https://www.coursera.org/learn/data-science-ethics/home/week/4) (kot so okostenelost, asimetrija informacij in distribucijska nepravičnost), ki lahko pospešijo orožitev AI.

Za slednje so potrebni [sodelovalni pristopi k definiranju kultur etike](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f), ki gradijo čustvene povezave in dosledne skupne vrednote _med organizacijami_ v industriji. To zahteva bolj [formalizirane kulture etike podatkov](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) v organizacijah - omogočanje _komurkoli_, da [potegne Andon vrv](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (za zgodnje opozarjanje na etične pomisleke) in postavljanje _etičnih ocen_ (npr. pri zaposlovanju) kot ključnega kriterija za oblikovanje ekip v AI projektih.

---
## [Kvizi po predavanju](https://ff-quizzes.netlify.app/en/ds/) 🎯
## Pregled in samostojno učenje

Tečaji in knjige pomagajo pri razumevanju osnovnih konceptov etike in izzivov, medtem ko študije primerov in orodja pomagajo pri uporabi etičnih praks v kontekstih resničnega sveta. Tukaj je nekaj virov za začetek.

* [Strojno učenje za začetnike](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - lekcija o pravičnosti, Microsoft.
* [Načela odgovorne umetne inteligence](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - brezplačna učna pot na Microsoft Learn.
* [Etika in podatkovna znanost](https://resources.oreilly.com/examples/0636920203964) - O'Reilly EBook (M. Loukides, H. Mason in drugi)
* [Etika podatkovne znanosti](https://www.coursera.org/learn/data-science-ethics#syllabus) - spletni tečaj Univerze v Michiganu.
* [Etika razkrita](https://ethicsunwrapped.utexas.edu/case-studies) - študije primerov Univerze v Teksasu.

# Naloga

[Napišite študijo primera o etiki podatkov](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.