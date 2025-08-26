<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8796f41f566a0a8ebb72863a83d558ed",
  "translation_date": "2025-08-26T15:07:47+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "sk"
}
-->
# Úvod do dátovej etiky

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Etika dátovej vedy - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

---

Sme všetci dátoví občania žijúci v dátovom svete.

Trhové trendy naznačujú, že do roku 2022 bude 1 z 3 veľkých organizácií nakupovať a predávať svoje dáta prostredníctvom online [trhovísk a výmenných platforiem](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/). Ako **vývojári aplikácií** zistíme, že je jednoduchšie a lacnejšie integrovať poznatky založené na dátach a automatizáciu riadenú algoritmami do každodenných používateľských skúseností. Ale ako sa AI stáva všadeprítomnou, budeme musieť pochopiť aj potenciálne škody spôsobené [zbraňovaním](https://www.youtube.com/watch?v=TQHs8SA1qpk) takýchto algoritmov vo veľkom rozsahu.

Trendy tiež naznačujú, že do roku 2025 vytvoríme a spotrebujeme viac ako [180 zettabajtov](https://www.statista.com/statistics/871513/worldwide-data-created/) dát. Ako **dátoví vedci** získame bezprecedentný prístup k osobným údajom. To znamená, že môžeme vytvárať behaviorálne profily používateľov a ovplyvňovať rozhodovanie spôsobmi, ktoré vytvárajú [ilúziu slobodnej voľby](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice), pričom potenciálne posúvame používateľov k výsledkom, ktoré preferujeme. To tiež otvára širšie otázky o ochrane súkromia a právach používateľov.

Dátová etika je teraz _nevyhnutným ochranným mechanizmom_ pre dátovú vedu a inžinierstvo, pomáhajúc nám minimalizovať potenciálne škody a neúmyselné dôsledky našich rozhodnutí založených na dátach. [Gartnerov Hype Cycle pre AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) identifikuje relevantné trendy v digitálnej etike, zodpovednej AI a správe AI ako kľúčové faktory pre väčšie megatrendy okolo _demokratizácie_ a _industrializácie_ AI.

![Gartnerov Hype Cycle pre AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

V tejto lekcii preskúmame fascinujúcu oblasť dátovej etiky - od základných konceptov a výziev, cez prípadové štúdie až po aplikované koncepty AI, ako je správa - ktoré pomáhajú vytvárať kultúru etiky v tímoch a organizáciách pracujúcich s dátami a AI.

## [Kvíz pred prednáškou](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## Základné definície

Začnime pochopením základnej terminológie.

Slovo "etika" pochádza z [gréckeho slova "ethikos"](https://en.wikipedia.org/wiki/Ethics) (a jeho koreňa "ethos"), čo znamená _charakter alebo morálna povaha_. 

**Etika** sa týka spoločných hodnôt a morálnych princípov, ktoré riadia naše správanie v spoločnosti. Etika nie je založená na zákonoch, ale na všeobecne prijatých normách toho, čo je "správne vs. nesprávne". Etické úvahy však môžu ovplyvniť iniciatívy korporátneho riadenia a vládne regulácie, ktoré vytvárajú viac stimulov na dodržiavanie pravidiel.

**Dátová etika** je [nová vetva etiky](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1), ktorá "študuje a hodnotí morálne problémy súvisiace s _dátami, algoritmami a zodpovedajúcimi praktikami_". Tu sa **"dáta"** zameriavajú na akcie súvisiace s generovaním, zaznamenávaním, kuráciou, spracovaním, šírením, zdieľaním a používaním, **"algoritmy"** sa zameriavajú na AI, agentov, strojové učenie a roboty, a **"praktiky"** sa zameriavajú na témy ako zodpovedná inovácia, programovanie, hacking a etické kódy.

**Aplikovaná etika** je [praktická aplikácia morálnych úvah](https://en.wikipedia.org/wiki/Applied_ethics). Ide o proces aktívneho skúmania etických otázok v kontexte _skutočných akcií, produktov a procesov_ a prijímania nápravných opatrení, aby zostali v súlade s našimi definovanými etickými hodnotami.

**Kultúra etiky** je o [_operacionalizácii_ aplikovanej etiky](https://hbr.org/2019/05/how-to-design-an-ethical-organization), aby sme zabezpečili, že naše etické princípy a praktiky sú prijaté konzistentne a škálovateľne naprieč celou organizáciou. Úspešné kultúry etiky definujú celopodnikové etické princípy, poskytujú zmysluplné stimuly na dodržiavanie pravidiel a posilňujú normy etiky podporovaním a amplifikáciou požadovaného správania na každej úrovni organizácie.

## Koncepty etiky

V tejto sekcii sa budeme zaoberať konceptmi ako **spoločné hodnoty** (princípy) a **etické výzvy** (problémy) pre dátovú etiku - a preskúmame **prípadové štúdie**, ktoré vám pomôžu pochopiť tieto koncepty v reálnych kontextoch.

### 1. Princípy etiky

Každá stratégia dátovej etiky začína definovaním _etických princípov_ - "spoločných hodnôt", ktoré opisujú prijateľné správanie a usmerňujú súladné akcie v našich dátových a AI projektoch. Môžete ich definovať na individuálnej alebo tímovej úrovni. Väčšina veľkých organizácií však tieto princípy uvádza v _misijnom vyhlásení alebo rámci etickej AI_, ktorý je definovaný na korporátnej úrovni a dôsledne presadzovaný vo všetkých tímoch.

**Príklad:** Microsoftovo [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai) misijné vyhlásenie znie: _"Sme odhodlaní k pokroku AI riadenému etickými princípmi, ktoré kladú ľudí na prvé miesto"_ - identifikujúc 6 etických princípov v rámci nižšie:

![Responsible AI v Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Poďme si stručne preskúmať tieto princípy. _Transparentnosť_ a _zodpovednosť_ sú základné hodnoty, na ktorých sú postavené ostatné princípy - začnime teda nimi:

* [**Zodpovednosť**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) robí praktikov _zodpovednými_ za ich dátové a AI operácie a súlad s týmito etickými princípmi.
* [**Transparentnosť**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) zabezpečuje, že dátové a AI akcie sú _pochopiteľné_ (interpretovateľné) pre používateľov, vysvetľujúc čo a prečo za rozhodnutiami.
* [**Spravodlivosť**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - zameriava sa na zabezpečenie, že AI zaobchádza _so všetkými ľuďmi_ spravodlivo, riešiac akékoľvek systémové alebo implicitné sociálno-technické predsudky v dátach a systémoch.
* [**Spoľahlivosť a bezpečnosť**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - zabezpečuje, že AI sa správa _konzistentne_ s definovanými hodnotami, minimalizujúc potenciálne škody alebo neúmyselné dôsledky.
* [**Súkromie a bezpečnosť**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - ide o pochopenie pôvodu dát a poskytovanie _ochrany súkromia a súvisiacich práv_ používateľom.
* [**Inkluzívnosť**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - ide o navrhovanie AI riešení s úmyslom, prispôsobujúc ich na splnenie _širokého spektra ľudských potrieb_ a schopností.

> 🚨 Premýšľajte o tom, aké by mohlo byť vaše misijné vyhlásenie dátovej etiky. Preskúmajte rámce etickej AI od iných organizácií - tu sú príklady od [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles) a [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Aké spoločné hodnoty majú? Ako sa tieto princípy vzťahujú na AI produkt alebo odvetvie, v ktorom pôsobia?

### 2. Výzvy etiky

Keď máme definované etické princípy, ďalším krokom je hodnotenie našich dátových a AI akcií, aby sme zistili, či sú v súlade s týmito spoločnými hodnotami. Premýšľajte o svojich akciách v dvoch kategóriách: _zber dát_ a _návrh algoritmov_. 

Pri zbere dát budú akcie pravdepodobne zahŕňať **osobné údaje** alebo osobne identifikovateľné informácie (PII) pre identifikovateľné živé osoby. To zahŕňa [rôzne položky neosobných údajov](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en), ktoré _spoločne_ identifikujú jednotlivca. Etické výzvy sa môžu týkať _ochrany súkromia_, _vlastníctva dát_ a súvisiacich tém ako _informovaný súhlas_ a _práva duševného vlastníctva_ pre používateľov.

Pri návrhu algoritmov budú akcie zahŕňať zber a kuráciu **datasetov**, potom ich použitie na trénovanie a nasadenie **dátových modelov**, ktoré predpovedajú výsledky alebo automatizujú rozhodnutia v reálnych kontextoch. Etické výzvy môžu vzniknúť z _predsudkov v datasetoch_, _problémov kvality dát_, _nespravodlivosti_ a _skreslenia_ v algoritmoch - vrátane niektorých problémov, ktoré sú systémové.

V oboch prípadoch etické výzvy poukazujú na oblasti, kde naše akcie môžu naraziť na konflikt s našimi spoločnými hodnotami. Na ich detekciu, zmiernenie, minimalizáciu alebo odstránenie musíme klásť morálne "áno/nie" otázky súvisiace s našimi akciami a následne prijať nápravné opatrenia podľa potreby. Pozrime sa na niektoré etické výzvy a morálne otázky, ktoré vyvolávajú:

#### 2.1 Vlastníctvo dát

Zber dát často zahŕňa osobné údaje, ktoré môžu identifikovať subjekty dát. [Vlastníctvo dát](https://permission.io/blog/data-ownership) sa týka _kontroly_ a [_práv používateľov_](https://permission.io/blog/data-ownership) súvisiacich s vytváraním, spracovaním a šírením dát. 

Morálne otázky, ktoré musíme klásť, sú: 
 * Kto vlastní dáta? (používateľ alebo organizácia)
 * Aké práva majú subjekty dát? (napr. prístup, vymazanie, prenosnosť)
 * Aké práva majú organizácie? (napr. oprava škodlivých používateľských recenzií)

#### 2.2 Informovaný súhlas

[Informovaný súhlas](https://legaldictionary.net/informed-consent/) definuje akt používateľov, ktorí súhlasia s akciou (napr. zber dát) s _plným pochopením_ relevantných faktov vrátane účelu, potenciálnych rizík a alternatív. 

Otázky na preskúmanie sú:
 * Dal používateľ (subjekt dát) povolenie na zber a použitie dát?
 * Pochopil používateľ účel, na ktorý boli dáta zhromaždené?
 * Pochopil používateľ potenciálne riziká z ich účasti?

#### 2.3 Duševné vlastníctvo

[Duševné vlastníctvo](https://en.wikipedia.org/wiki/Intellectual_property) sa týka nehmotných výtvorov vyplývajúcich z ľudskej iniciatívy, ktoré môžu _mať ekonomickú hodnotu_ pre jednotlivcov alebo podniky. 

Otázky na preskúmanie sú:
 * Mali zhromaždené dáta ekonomickú hodnotu pre používateľa alebo podnik?
 * Má **používateľ** duševné vlastníctvo v tomto prípade?
 * Má **organizácia** duševné vlastníctvo v tomto prípade?
 * Ak tieto práva existujú, ako ich chránime?

#### 2.4 Ochrana súkromia dát

[Ochrana súkromia dát](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) alebo informačné súkromie sa týka zachovania súkromia používateľov a ochrany identity používateľov vo vzťahu k osobne identifikovateľným informáciám. 

Otázky na preskúmanie sú:
 * Sú dáta používateľov (osobné) zabezpečené proti hackom a únikom?
 * Sú dáta používateľov prístupné iba autorizovaným používateľom a kontextom?
 * Je anonymita používateľov zachovaná pri zdieľaní alebo šírení dát?
 * Môže byť používateľ de-identifikovaný z anonymizovaných datasetov?

#### 2.5 Právo byť zabudnutý

[Právo byť zabudnutý](https://en.wikipedia.org/wiki/Right_to_be_forgotten) alebo [Právo na vymazanie](https://www.gdpreu.org/right-to-be-forgotten/) poskytuje používateľom dodatočnú ochranu osobných údajov. Konkrétne dáva používateľom právo požiadať o vymazanie alebo odstránenie osobných údajov z internetových vyhľadávaní a iných lokalít, _za špecifických okolností_ - umožňujúc im nový začiatok online bez toho, aby ich minulé akcie boli proti nim použité.

Otázky na preskúmanie sú:
 * Umožňuje systém subjektom dát požiadať o vymazanie?
 * Mal by odvolanie súhlasu používateľa spustiť automatické vymazanie?
 * Boli dáta zhromaždené bez súhlasu alebo nezákonnými prostriedkami?
 * Sme v súlade s vládnymi reguláciami na ochranu súkromia dát?

#### 2.6 Predsudky v datasetoch

Predsudky v datasetoch alebo [Predsudky pri zbere](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) sa týkajú výberu _nereprezentatívnej_ podmnožiny dát na vývoj algoritmov, čo vytvára potenciálnu nespravodlivosť vo výsledkoch pre rôzne skupiny. Typy predsudkov zahŕňajú výberové alebo vzorkové predsudky, dobrovoľnícke predsudky a predsudky nástrojov. 

Otázky na preskúmanie sú:
 * Rekrutovali sme reprezentatívnu skupinu subjektov dát?
 * Testovali sme náš zhromaždený alebo kurátovaný dataset na rôzne predsudky?
 * Môžeme zmierniť alebo odstrániť objavené predsudky?


[Algorithmická spravodlivosť](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) skúma, či návrh algoritmu systematicky nediskriminuje konkrétne podskupiny dátových subjektov, čo môže viesť k [potenciálnym škodám](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) v oblasti _alokácie_ (kde sú zdroje odmietnuté alebo zadržané pre túto skupinu) a _kvality služieb_ (kde AI nie je pre niektoré podskupiny taká presná ako pre iné).

Otázky na preskúmanie:
 * Vyhodnotili sme presnosť modelu pre rôzne podskupiny a podmienky?
 * Preskúmali sme systém z hľadiska potenciálnych škôd (napr. stereotypizácie)?
 * Môžeme upraviť dáta alebo preškoliť modely na zmiernenie identifikovaných škôd?

Preskúmajte zdroje ako [kontrolné zoznamy pre spravodlivosť AI](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA), aby ste sa dozvedeli viac.

#### 2.9 Nesprávne prezentovanie údajov

[Nesprávne prezentovanie údajov](https://www.sciencedirect.com/topics/computer-science/misrepresentation) sa týka otázky, či komunikujeme poznatky z čestne získaných údajov zavádzajúcim spôsobom, aby sme podporili požadovaný naratív.

Otázky na preskúmanie:
 * Hlásime neúplné alebo nepresné údaje?
 * Vizualizujeme údaje spôsobom, ktorý vedie k zavádzajúcim záverom?
 * Používame selektívne štatistické techniky na manipuláciu s výsledkami?
 * Existujú alternatívne vysvetlenia, ktoré by mohli ponúknuť iný záver?

#### 2.10 Ilúzia voľby
[Ilúzia voľby](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) nastáva, keď „architektúry voľby“ systému používajú rozhodovacie algoritmy na ovplyvnenie ľudí, aby prijali preferovaný výsledok, pričom im dávajú zdanie možností a kontroly. Tieto [temné vzory](https://www.darkpatterns.org/) môžu spôsobiť sociálne a ekonomické škody používateľom. Keďže rozhodnutia používateľov ovplyvňujú profily správania, tieto akcie môžu potenciálne poháňať budúce voľby, ktoré môžu zosilniť alebo predĺžiť dopad týchto škôd.

Otázky na preskúmanie:
 * Rozumel používateľ dôsledkom prijatia tejto voľby?
 * Bol používateľ informovaný o (alternatívnych) možnostiach a výhodách a nevýhodách každej z nich?
 * Môže používateľ neskôr zvrátiť automatizovanú alebo ovplyvnenú voľbu?

### 3. Prípadové štúdie

Aby sme tieto etické výzvy zasadili do reálneho kontextu, je užitočné pozrieť sa na prípadové štúdie, ktoré zdôrazňujú potenciálne škody a dôsledky pre jednotlivcov a spoločnosť, keď sa tieto etické porušenia prehliadajú.

Tu je niekoľko príkladov:

| Etická výzva | Prípadová štúdia  | 
|--- |--- |
| **Informovaný súhlas** | 1972 - [Štúdia syfilisu v Tuskegee](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Afroamerickým mužom, ktorí sa zúčastnili štúdie, bola sľúbená bezplatná zdravotná starostlivosť, _ale boli oklamaní_ výskumníkmi, ktorí im neoznámili ich diagnózu ani dostupnosť liečby. Mnohí účastníci zomreli a ich partneri alebo deti boli ovplyvnení; štúdia trvala 40 rokov. | 
| **Ochrana údajov** |  2007 - [Netflix Data Prize](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) poskytla výskumníkom _10 miliónov anonymizovaných hodnotení filmov od 50 000 zákazníkov_, aby pomohla zlepšiť odporúčacie algoritmy. Výskumníci však dokázali prepojiť anonymizované údaje s osobne identifikovateľnými údajmi v _externých datasetoch_ (napr. komentáre na IMDb), čím efektívne „de-anonymizovali“ niektorých predplatiteľov Netflixu.|
| **Zber dát s predsudkami**  | 2013 - Mesto Boston [vyvinulo aplikáciu Street Bump](https://www.boston.gov/transportation/street-bump), ktorá umožnila občanom hlásiť výtlky, čím mestu poskytla lepšie údaje o cestách na identifikáciu a opravu problémov. Avšak [ľudia s nižšími príjmami mali menší prístup k autám a telefónom](https://hbr.org/2013/04/the-hidden-biases-in-big-data), čo spôsobilo, že ich problémy s cestami zostali v aplikácii neviditeľné. Vývojári spolupracovali s akademikmi na riešení problémov _rovnakého prístupu a digitálnych rozdielov_ pre spravodlivosť. |
| **Algoritmická spravodlivosť**  | 2018 - MIT [Gender Shades Study](http://gendershades.org/overview.html) hodnotila presnosť AI produktov na klasifikáciu pohlavia, pričom odhalila medzery v presnosti pre ženy a osoby inej farby pleti. [Apple Card z roku 2019](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) sa zdala ponúkať menej úveru ženám ako mužom. Obe štúdie ilustrovali problémy algoritmických predsudkov vedúcich k socio-ekonomickým škodám.|
| **Nesprávne prezentovanie údajov** | 2020 - [Ministerstvo zdravotníctva štátu Georgia zverejnilo grafy COVID-19](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening), ktoré sa zdali zavádzať občanov o trendoch potvrdených prípadov pomocou nechronologického usporiadania na osi x. To ilustruje nesprávne prezentovanie údajov prostredníctvom vizualizačných trikov. |
| **Ilúzia voľby** | 2020 - Vzdelávacia aplikácia [ABCmouse zaplatila 10 miliónov dolárov na urovnanie sťažnosti FTC](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/), kde boli rodičia nútení platiť za predplatné, ktoré nemohli zrušiť. To ilustruje temné vzory v architektúrach voľby, kde boli používatelia ovplyvnení k potenciálne škodlivým rozhodnutiam. |
| **Ochrana údajov a práva používateľov** | 2021 - [Únik údajov na Facebooku](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) odhalil údaje 530 miliónov používateľov, čo viedlo k urovnaniu vo výške 5 miliárd dolárov s FTC. Facebook však odmietol informovať používateľov o úniku, čím porušil práva používateľov na transparentnosť a prístup k údajom. |

Chcete preskúmať viac prípadových štúdií? Pozrite si tieto zdroje:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - etické dilemy v rôznych odvetviach.
* [Kurz etiky dátovej vedy](https://www.coursera.org/learn/data-science-ethics#syllabus) - preskúmanie významných prípadových štúdií.
* [Kde sa veci pokazili](https://deon.drivendata.org/examples/) - kontrolný zoznam Deon s príkladmi.

> 🚨 Zamyslite sa nad prípadovými štúdiami, ktoré ste videli – zažili ste alebo boli ste ovplyvnení podobnou etickou výzvou vo svojom živote? Dokážete si spomenúť na aspoň jednu ďalšiu prípadovú štúdiu, ktorá ilustruje jednu z etických výziev, o ktorých sme diskutovali v tejto sekcii?

## Aplikovaná etika

Hovorili sme o etických konceptoch, výzvach a prípadových štúdiách v reálnom kontexte. Ako však začať _uplatňovať_ etické princípy a praktiky vo svojich projektoch? A ako _zaviesť_ tieto praktiky pre lepšie riadenie? Poďme preskúmať niektoré reálne riešenia:

### 1. Profesionálne kódexy

Profesionálne kódexy ponúkajú jednu možnosť pre organizácie, ako „motivovať“ členov k podpore ich etických princípov a poslania. Kódexy sú _morálne usmernenia_ pre profesionálne správanie, ktoré pomáhajú zamestnancom alebo členom robiť rozhodnutia v súlade s princípmi ich organizácie. Ich účinnosť však závisí od dobrovoľného dodržiavania členmi; mnohé organizácie však ponúkajú dodatočné odmeny a sankcie na podporu dodržiavania.

Príklady zahŕňajú:

 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Kódex etiky
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Kódex správania (vytvorený v roku 2013)
 * [ACM Kódex etiky a profesionálneho správania](https://www.acm.org/code-of-ethics) (od roku 1993)

> 🚨 Patríte do profesionálnej inžinierskej alebo dátovej organizácie? Preskúmajte ich webovú stránku, aby ste zistili, či definujú profesionálny kódex etiky. Čo to hovorí o ich etických princípoch? Ako „motivujú“ členov k dodržiavaniu kódexu?

### 2. Etické kontrolné zoznamy

Zatiaľ čo profesionálne kódexy definujú požadované _etické správanie_ od odborníkov, [majú známe obmedzenia](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) pri presadzovaní, najmä pri veľkých projektoch. Mnohí odborníci na dátovú vedu preto [odporúčajú kontrolné zoznamy](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), ktoré môžu **prepojiť princípy s praxou** deterministickým a akčným spôsobom.

Kontrolné zoznamy premieňajú otázky na „áno/nie“ úlohy, ktoré je možné operacionalizovať, čo umožňuje ich sledovanie ako súčasť štandardných pracovných postupov pri vydávaní produktov.

Príklady zahŕňajú:
 * [Deon](https://deon.drivendata.org/) - všeobecný kontrolný zoznam etiky dát vytvorený na základe [odporúčaní z odvetvia](https://deon.drivendata.org/#checklist-citations) s nástrojom príkazového riadku pre jednoduchú integráciu.
 * [Kontrolný zoznam auditu ochrany súkromia](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - poskytuje všeobecné usmernenia pre praktiky manipulácie s informáciami z právneho a sociálneho hľadiska.
 * [Kontrolný zoznam spravodlivosti AI](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - vytvorený odborníkmi na AI na podporu prijatia a integrácie kontrol spravodlivosti do vývojových cyklov AI.
 * [22 otázok pre etiku v dátach a AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - otvorenejší rámec, štruktúrovaný na počiatočné preskúmanie etických otázok v dizajne, implementácii a organizačných kontextoch.

### 3. Etické regulácie

Etika je o definovaní spoločných hodnôt a dobrovoľnom konaní správnych vecí. **Súlad** je o _dodržiavaní zákona_, ak a kde je definovaný. **Riadenie** zahŕňa všetky spôsoby, akými organizácie presadzujú etické princípy a dodržiavajú stanovené zákony.

Dnes riadenie zahŕňa dve formy v rámci organizácií. Po prvé, ide o definovanie **etických princípov AI** a zavedenie praktík na podporu ich prijatia vo všetkých projektoch súvisiacich s AI v organizácii. Po druhé, ide o dodržiavanie všetkých vládou nariadených **regulácií ochrany údajov** pre regióny, v ktorých organizácia pôsobí.

Príklady regulácií ochrany údajov a súkromia:

 * `1974`, [Zákon o ochrane súkromia USA](https://www.justice.gov/opcl/privacy-act-1974) - reguluje _federálnu vládu_ pri zhromažďovaní, používaní a zverejňovaní osobných údajov.
 * `1996`, [Zákon o prenosnosti a zodpovednosti zdravotného poistenia USA (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - chráni osobné zdravotné údaje.
 * `1998`, [Zákon o ochrane súkromia detí online (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - chráni údaje detí mladších ako 13 rokov.
 * `2018`, [Všeobecné nariadenie o ochrane údajov (GDPR)](https://gdpr-info.eu/) - poskytuje práva používateľov, ochranu údajov a súkromie.
 * `2018`, [Kalifornský zákon o ochrane spotrebiteľov (CCPA)](https://www.oag.ca.gov/privacy/ccpa) - dáva spotrebiteľom viac _práv_ nad ich (osobnými) údajmi.
 * `2021`, Čína [Zákon o ochrane osobných údajov](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) - jeden z najsilnejších online zákonov o ochrane súkromia na svete.

> 🚨 Európska únia definovala GDPR (Všeobecné nariadenie o ochrane údajov), ktoré zostáva jedným z najvplyvnejších nariadení o ochrane údajov dnes. Vedeli ste, že GDPR tiež definuje [8 práv používateľov](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) na ochranu digitálneho súkromia a osobných údajov občanov? Zistite, aké sú tieto práva a prečo sú dôležité.

### 4. Kultúra etiky

Treba si uvedomiť, že medzi _dodržiavaním zákona_ (splnením „litery zákona“) a riešením [systémových problémov](https://www.coursera.org/learn/data-science-ethics/home/week/4) (ako je zakonzervovanie, informačná asymetria a distribučná nespravodlivosť), ktoré môžu urýchliť zneužitie AI, zostáva nehmotná priepasť.

Riešenie týchto problémov si vyžaduje [spoluprácu na definovaní kultúr etiky](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f), ktoré budujú emocionálne spojenia a konzistentné spoločné hodnoty _naprieč organizáciami_ v odvetví. To si vyžaduje viac [formalizovaných kultúr etiky dát](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) v organizáciách – umožňujúc _komukoľvek_ [zatiahnuť Andon šnúru](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (na včasné upozornenie na etické problémy) a robiť _etické hodnot
* [Zásady zodpovednej umelej inteligencie](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - bezplatná vzdelávacia cesta od Microsoft Learn.  
* [Etika a dátová veda](https://resources.oreilly.com/examples/0636920203964) - EBook od O'Reilly (M. Loukides, H. Mason a kol.)  
* [Etika v dátovej vede](https://www.coursera.org/learn/data-science-ethics#syllabus) - online kurz od University of Michigan.  
* [Etika v praxi](https://ethicsunwrapped.utexas.edu/case-studies) - prípadové štúdie od University of Texas.  

# Zadanie  

[Napíšte prípadovú štúdiu o etike dát](assignment.md)  

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.