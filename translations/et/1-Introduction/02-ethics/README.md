<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58860ce9a4b8a564003d2752f7c72851",
  "translation_date": "2025-10-11T15:39:35+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "et"
}
-->
# Sissejuhatus andme-eetikasse

|![ Sketchnote autorilt [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Andmeteaduse eetika - _Sketchnote autorilt [@nitya](https://twitter.com/nitya)_ |

---

Me kõik oleme andmekodanikud, kes elavad andmestunud maailmas.

Turutrendid näitavad, et aastaks 2022 hakkab iga kolmas suurorganisatsioon ostma ja müüma oma andmeid veebipõhiste [turgude ja vahetusplatvormide](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/) kaudu. **Rakenduste arendajatena** muutub andmepõhiste teadmiste ja algoritmipõhise automatiseerimise integreerimine igapäevastesse kasutajakogemustesse lihtsamaks ja odavamaks. Kuid kuna tehisintellekt muutub kõikjalolevaks, peame mõistma ka võimalikke kahjusid, mida põhjustab selliste algoritmide [relvastamine](https://www.youtube.com/watch?v=TQHs8SA1qpk) suurel skaalal.

Trendid viitavad sellele, et aastaks 2025 loome ja tarbime üle [180 zettabaidi](https://www.statista.com/statistics/871513/worldwide-data-created/) andmeid. **Andmeteadlastele** pakub see andmeplahvatus enneolematut juurdepääsu isiku- ja käitumisandmetele. Sellega kaasneb võime luua üksikasjalikke kasutajaprofiile ja mõjutada otsuste tegemist peenelt—tihti viisil, mis tekitab [vaba valiku illusiooni](https://www.datasciencecentral.com/the-pareto-set-and-the-paradox-of-choice/). Kuigi seda saab kasutada kasutajate suunamiseks eelistatud tulemusteni, tõstatab see ka olulisi küsimusi andmete privaatsuse, autonoomia ja algoritmilise mõju eetiliste piiride kohta.

Andme-eetika on nüüd _vajalikud kaitsepiirded_ andmeteaduse ja inseneeria jaoks, aidates meil minimeerida võimalikke kahjusid ja soovimatuid tagajärgi, mis tulenevad meie andmepõhistest tegevustest. [Gartneri tehisintellekti hype-tsükkel](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) toob esile digitaalse eetika, vastutustundliku AI ja AI juhtimise kui olulised suundumused, mis juhivad suuremaid megatrende, nagu tehisintellekti _demokratiseerimine_ ja _industrialiseerimine_.

![Gartneri tehisintellekti hype-tsükkel - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

Selles õppetükis uurime põnevat andme-eetika valdkonda—alates põhikontseptsioonidest ja väljakutsetest kuni juhtumiuuringute ja rakendatud AI kontseptsioonideni, nagu juhtimine—mis aitavad luua eetika kultuuri meeskondades ja organisatsioonides, mis töötavad andmete ja tehisintellektiga.




## [Loengu-eelne viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/2) 🎯

## Põhimõisted

Alustame põhiterminoloogia mõistmisest.

Sõna "eetika" pärineb [kreeka sõnast "ethikos"](https://en.wikipedia.org/wiki/Ethics) (ja selle juurest "ethos"), mis tähendab _iseloomu või moraalset olemust_.

**Eetika** käsitleb jagatud väärtusi ja moraalseid põhimõtteid, mis juhivad meie käitumist ühiskonnas. Eetika ei põhine seadustel, vaid laialdaselt aktsepteeritud normidel selle kohta, mis on "õige vs. vale". Siiski võivad eetilised kaalutlused mõjutada ettevõtte juhtimisalgatusi ja valitsuse regulatsioone, mis loovad rohkem stiimuleid vastavuse tagamiseks.

**Andme-eetika** on [uus eetika haru](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1), mis "uurib ja hindab moraalseid probleeme, mis on seotud _andmete, algoritmide ja vastavate praktikatega_". Siin keskendub **"andmed"** tegevustele, mis on seotud andmete loomise, salvestamise, kureerimise, töötlemise, levitamise, jagamise ja kasutamisega, **"algoritmid"** keskenduvad tehisintellektile, agentidele, masinõppele ja robotitele ning **"praktikad"** keskenduvad teemadele nagu vastutustundlik innovatsioon, programmeerimine, häkkimine ja eetika koodid.

**Rakenduseetika** on [moraalsete kaalutluste praktiline rakendamine](https://en.wikipedia.org/wiki/Applied_ethics). See on protsess, kus aktiivselt uuritakse eetilisi küsimusi _reaalse maailma tegevuste, toodete ja protsesside_ kontekstis ning võetakse parandusmeetmeid, et need jääksid kooskõlla meie määratletud eetiliste väärtustega.

**Eetika kultuur** käsitleb [_rakenduseetika operationaliseerimist_](https://hbr.org/2019/05/how-to-design-an-ethical-organization), et tagada, et meie eetilised põhimõtted ja praktikad võetakse kasutusele järjepidevalt ja skaleeritavalt kogu organisatsioonis. Edukad eetika kultuurid määratlevad organisatsiooniülesed eetilised põhimõtted, pakuvad tähendusrikkaid stiimuleid vastavuse tagamiseks ning tugevdavad eetikanorme, julgustades ja võimendades soovitud käitumist igal organisatsiooni tasandil.


## Eetika kontseptsioonid

Selles jaotises arutame selliseid kontseptsioone nagu **jagatud väärtused** (põhimõtted) ja **eetilised väljakutsed** (probleemid) andme-eetika jaoks—ning uurime **juhtumiuuringuid**, mis aitavad teil mõista neid kontseptsioone reaalse maailma kontekstis.

### 1. Eetika põhimõtted

Iga andme-eetika strateegia algab _eetiliste põhimõtete_ määratlemisest—"jagatud väärtustest", mis kirjeldavad vastuvõetavat käitumist ja juhivad vastavuses olevaid tegevusi meie andme- ja AI-projektides. Neid saab määratleda individuaalsel või meeskonna tasandil. Kuid enamik suuri organisatsioone määratleb need _eetilise AI_ missioonilause või raamistikuna, mis on määratletud korporatiivsel tasandil ja rakendatud järjepidevalt kõigis meeskondades.

**Näide:** Microsofti [Vastutustundliku AI](https://www.microsoft.com/en-us/ai/responsible-ai) missioonilause kõlab: _"Me oleme pühendunud AI edendamisele eetiliste põhimõtete alusel, mis asetavad inimesed esikohale"_—tuvastades 6 eetilist põhimõtet allolevas raamistikus:

![Vastutustundlik AI Microsoftis](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Vaatame lühidalt neid põhimõtteid. _Läbipaistvus_ ja _vastutus_ on põhiväärtused, millele teised põhimõtted tuginevad—alustame neist:

* [**Vastutus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) teeb praktikud _vastutavaks_ nende andme- ja AI-tegevuste eest ning vastavuse eest nendele eetilistele põhimõtetele.
* [**Läbipaistvus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) tagab, et andme- ja AI-tegevused on _arusaadavad_ (tõlgendatavad) kasutajatele, selgitades otsuste taga olevat "mida" ja "miks".
* [**Õiglus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) keskendub sellele, et AI kohtleks _kõiki inimesi_ õiglaselt, lahendades süsteemseid või varjatud sotsiaal-tehnilisi eelarvamusi andmetes ja süsteemides.
* [**Usaldusväärsus ja ohutus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) tagab, et AI käitub _järjekindlalt_ määratletud väärtustega, minimeerides võimalikke kahjusid või soovimatuid tagajärgi.
* [**Privaatsus ja turvalisus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) käsitleb andmete päritolu mõistmist ja kasutajatele _andmeprivaatsuse ja sellega seotud kaitsete_ pakkumist.
* [**Kaasatus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) keskendub AI lahenduste kavandamisele eesmärgiga kohandada neid _laiade inimvajaduste ja -võimaluste_ rahuldamiseks.

> 🚨 Mõelge, milline võiks olla teie andme-eetika missioonilause. Uurige teiste organisatsioonide eetilise AI raamistikke—siin on näited [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles) ja [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Millised jagatud väärtused neil on ühiselt? Kuidas need põhimõtted seostuvad AI toodete või tööstusharuga, milles nad tegutsevad?

### 2. Eetilised väljakutsed

Kui eetilised põhimõtted on määratletud, on järgmine samm hinnata meie andme- ja AI-tegevusi, et näha, kas need vastavad neile jagatud väärtustele. Mõelge oma tegevustele kahes kategoorias: _andmete kogumine_ ja _algoritmide kujundamine_.

Andmete kogumisega seotud tegevused hõlmavad tõenäoliselt **isikuandmeid** või isikut tuvastavat teavet (PII) tuvastatavate elavate isikute kohta. See hõlmab [mitmekesiseid mitteisiklikke andmeid](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en), mis _koos_ tuvastavad isiku. Eetilised väljakutsed võivad olla seotud _andmete privaatsuse_, _andmete omandiõiguse_ ja seotud teemadega, nagu _teadlik nõusolek_ ja _intellektuaalomandi õigused_ kasutajatele.

Algoritmide kujundamisega seotud tegevused hõlmavad **andmekogumite** kogumist ja kureerimist ning nende kasutamist **andmemudelite** treenimiseks ja juurutamiseks, mis ennustavad tulemusi või automatiseerivad otsuseid reaalses maailmas. Eetilised väljakutsed võivad tekkida _andmekogumi eelarvamustest_, _andmete kvaliteedi_ probleemidest, _ebaõiglusest_ ja _valest esitusest_ algoritmides—sealhulgas mõned probleemid, mis on süsteemsed.

Mõlemal juhul toovad eetilised väljakutsed esile valdkonnad, kus meie tegevused võivad olla vastuolus meie jagatud väärtustega. Nende probleemide tuvastamiseks, leevendamiseks, minimeerimiseks või kõrvaldamiseks peame esitama moraalseid "jah/ei" küsimusi, mis on seotud meie tegevustega, ja võtma vajadusel parandusmeetmeid. Vaatame mõningaid eetilisi väljakutseid ja moraalseid küsimusi, mida need tõstatavad:


#### 2.1 Andmete omandiõigus

Andmete kogumine hõlmab sageli isikuandmeid, mis võivad tuvastada andmesubjekte. [Andmete omandiõigus](https://permission.io/blog/data-ownership) käsitleb _kontrolli_ ja [_kasutaja õigusi_](https://permission.io/blog/data-ownership), mis on seotud andmete loomise, töötlemise ja levitamisega.

Moraalsed küsimused, mida peame esitama, on:
 * Kes omab andmeid? (kasutaja või organisatsioon)
 * Millised õigused on andmesubjektidel? (nt juurdepääs, kustutamine, teisaldatavus)
 * Millised õigused on organisatsioonidel? (nt pahatahtlike kasutajaülevaadete parandamine)

#### 2.2 Teadlik nõusolek

[Teadlik nõusolek](https://legaldictionary.net/informed-consent/) määratleb kasutajate tegevuse (nt andmete kogumine) nõustumise _täieliku arusaamisega_ asjakohastest faktidest, sealhulgas eesmärgist, võimalikest riskidest ja alternatiividest.

Küsimused, mida siin uurida:
 * Kas kasutaja (andmesubjekt) andis loa andmete kogumiseks ja kasutamiseks?
 * Kas kasutaja mõistis, mis eesmärgil need andmed koguti?
 * Kas kasutaja mõistis osalemisega kaasnevaid võimalikke riske?

#### 2.3 Intellektuaalomand

[Intellektuaalomand](https://en.wikipedia.org/wiki/Intellectual_property) viitab immateriaalsetele loomingutele, mis tulenevad inimlikust algatusest ja võivad _omada majanduslikku väärtust_ üksikisikutele või ettevõtetele.

Küsimused, mida siin uurida:
 * Kas kogutud andmetel oli majanduslik väärtus kasutajale või ettevõttele?
 * Kas **kasutajal** on siin intellektuaalomand?
 * Kas **organisatsioonil** on siin intellektuaalomand?
 * Kui need õigused eksisteerivad, kuidas me neid kaitseme?

#### 2.4 Andmete privaatsus

[Andmete privaatsus](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) või teabe privaatsus viitab kasutaja privaatsuse säilitamisele ja kasutaja identiteedi kaitsmisele isikut tuvastava teabe osas.

Küsimused, mida siin uurida:
 * Kas kasutajate (isiklikud) andmed on kaitstud häkkimiste ja lekkimiste eest?
 * Kas kasutajate andmed on juurdepääsetavad ainult volitatud kasutajatele ja kontekstidele?
 * Kas kasutajate anonüümsus säilib, kui andmeid jagatakse või levitatakse?
 * Kas kasutaja saab anonüümsetest andmekogumitest tuvastamatuks muuta?

#### 2.5 Õigus olla unustatud

[Õigus olla unustatud](https://en.wikipedia.org/wiki/Right_to_be_forgotten) või [Õigus kustutamisele](https://www.gdpreu.org/right-to-be-forgotten/) pakub kasutajatele täiendavat isikuandmete kaitset. Eelkõige annab see kasutajatele õiguse taotleda isikuandmete kustutamist või eemaldamist Interneti otsingutest ja muudest kohtadest, _teatud tingimustel_—võimaldades neile veebis uut algust, ilma et mineviku tegevusi nende vastu kasutataks.

Küsimused, mida siin uurida:
 * Kas süsteem võimaldab andmesubjektidel taotleda kustutamist?
 * Kas kasutaja nõusoleku tagasivõtmine peaks käivitama automaatse kustutamise?
 * Kas andmeid koguti ilma nõusolekuta või ebaseaduslikult?
 * Kas me järgime valitsuse regulatsioone andmete privaatsuse osas?

#### 2.6 Andmekogumi eelarvamused

Andmekogumi või [kogumise eelarvamused](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) käsitlevad _mitteesindusliku_ andmealamkogumi valimist algoritmi arendamiseks, mis võib luua potentsiaalset ebaõiglust tulemuste osas erinevatele gruppidele. Eelarvamuste tüübid hõlmavad valiku- või proovivõtueelarvamusi, vabatahtlike eelarvamusi ja instrumentaalset eelarvamust.

Küsimused, mida siin uurida:
 * Kas me kaasasime esindusliku andmesubjektide kogumi?
 * Kas me testisime kogutud või kureeritud andmekogumit erinevate eelarvamuste osas?
 * Kas me saame avastatud eelarvamusi leevendada või eemaldada?

#### 2.7 Andmete kvaliteet

[Andmete kvaliteet](https://lakefs.io/data-quality-testing/) uurib kureeritud andmekogumi kehtivust, mida kasutatakse meie algoritmide arendamiseks, kontrollides, kas tunnused ja kirjed vastavad meie AI
* Kas teave kajastab _täpselt_ tegelikkust?

#### 2.8 Algoritmiline õiglus

[Algoritmiline õiglus](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) uurib, kas algoritmi disain diskrimineerib süstemaatiliselt teatud andmesubjektide alarühmi, põhjustades [potentsiaalseid kahjusid](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) _ressursside jaotamisel_ (kus ressursid jäetakse grupile kättesaamatuks) ja _teenuse kvaliteedis_ (kus AI ei ole teatud alarühmade jaoks nii täpne kui teiste jaoks).

Küsimused, mida siin uurida:
* Kas me hindasime mudeli täpsust erinevate alarühmade ja tingimuste jaoks?
* Kas me analüüsisime süsteemi võimalike kahjude (nt stereotüübid) osas?
* Kas me saame andmeid muuta või mudeleid uuesti treenida, et tuvastatud kahjusid vähendada?

Tutvu ressurssidega nagu [AI õiglus kontrollnimekirjad](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA), et rohkem teada saada.

#### 2.9 Valeandmete esitamine

[Andmete vale esitamine](https://www.sciencedirect.com/topics/computer-science/misrepresentation) tähendab küsimust, kas me edastame ausalt esitatud andmetest saadud teadmisi eksitaval viisil, et toetada soovitud narratiivi.

Küsimused, mida siin uurida:
* Kas me esitame puudulikke või ebatäpseid andmeid?
* Kas me visualiseerime andmeid viisil, mis viib eksitavate järeldusteni?
* Kas me kasutame valikulisi statistilisi meetodeid tulemuste manipuleerimiseks?
* Kas on olemas alternatiivseid selgitusi, mis võivad pakkuda teistsugust järeldust?

#### 2.10 Vaba valiku illusioon

[Vaba valiku illusioon](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) tekib siis, kui süsteemi "valikuarhitektuurid" kasutavad otsustusalgoritme, et suunata inimesi eelistatud tulemuse poole, samal ajal näidates, et neil on valikud ja kontroll. Need [tumedad mustrid](https://www.darkpatterns.org/) võivad põhjustada kasutajatele sotsiaalset ja majanduslikku kahju. Kuna kasutajate otsused mõjutavad käitumisprofiile, võivad need tegevused potentsiaalselt võimendada või pikendada nende kahjude mõju.

Küsimused, mida siin uurida:
* Kas kasutaja mõistis selle valiku tegemise tagajärgi?
* Kas kasutaja oli teadlik (alternatiivsetest) valikutest ja nende plussidest ja miinustest?
* Kas kasutaja saab hiljem automatiseeritud või mõjutatud valiku tagasi pöörata?

### 3. Juhtumiuuringud

Et panna need eetilised väljakutsed reaalsesse konteksti, on kasulik vaadata juhtumiuuringuid, mis toovad esile potentsiaalsed kahjud ja tagajärjed üksikisikutele ja ühiskonnale, kui selliseid eetikarikkumisi eiratakse.

Siin on mõned näited:

| Eetiline väljakutse | Juhtumiuuring | 
|--- |--- |
| **Teadlik nõusolek** | 1972 - [Tuskegee süüfilise uuring](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Aafrika-Ameerika mehed, kes osalesid uuringus, lubati tasuta arstiabi, _kuid peteti_, kuna teadlased ei teavitanud osalejaid nende diagnoosist ega ravi kättesaadavusest. Paljud osalejad surid ja nende partnerid või lapsed olid mõjutatud; uuring kestis 40 aastat. | 
| **Andmete privaatsus** | 2007 - [Netflixi andmeauhind](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) pakkus teadlastele _10M anonüümset filmihinnangut 50K kliendilt_, et parandada soovitusalgoritme. Kuid teadlased suutsid anonüümseid andmeid korreleerida isikutuvastatavate andmetega _välises andmebaasis_ (nt IMDb kommentaarid), mis sisuliselt "deanonüümis" mõned Netflixi tellijad.|
| **Kogumise kallutatus** | 2013 - Bostoni linn [arendas Street Bumpi](https://www.boston.gov/transportation/street-bump), rakenduse, mis võimaldas kodanikel teatada teekatteaukudest, andes linnale paremaid andmeid probleemide leidmiseks ja parandamiseks. Kuid [madalama sissetulekuga inimesed omasid vähem autosid ja telefone](https://hbr.org/2013/04/the-hidden-biases-in-big-data), muutes nende teekatteprobleemid rakenduses nähtamatuks. Arendajad tegid koostööd akadeemikutega, et lahendada _võrdse juurdepääsu ja digitaalse lõhe_ küsimusi õiglasuse tagamiseks. |
| **Algoritmiline õiglus** | 2018 - MIT [Gender Shades Study](http://gendershades.org/overview.html) hindas soo klassifitseerimise AI toodete täpsust, paljastades täpsuse puudujääke naiste ja värviliste inimeste jaoks. [2019 Apple'i krediitkaart](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) näis pakkuvat naistele vähem krediiti kui meestele. Mõlemad näitasid algoritmilise kallutatuse probleeme, mis põhjustasid sotsiaal-majanduslikku kahju.|
| **Andmete vale esitamine** | 2020 - [Georgia rahvatervise osakond avaldas COVID-19 graafikud](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening), mis näisid eksitavat kodanikke kinnitatud juhtumite trendide osas, kasutades mitte-kronoloogilist järjestust x-teljel. See illustreerib valeandmete esitamist visualiseerimise trikkide kaudu. |
| **Vaba valiku illusioon** | 2020 - Õppeäpp [ABCmouse maksis $10M, et lahendada FTC kaebus](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/), kus vanemad olid sunnitud maksma tellimuste eest, mida nad ei saanud tühistada. See illustreerib tumedaid mustreid valikuarhitektuurides, kus kasutajad suunati potentsiaalselt kahjulike valikute poole. |
| **Andmete privaatsus ja kasutajaõigused** | 2021 - Facebooki [andmeleke](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) paljastas 530M kasutaja andmed, mille tulemusel määrati FTC-le $5B trahv. Kuid Facebook keeldus kasutajaid lekke kohta teavitamast, rikkudes kasutajaõigusi andmete läbipaistvuse ja juurdepääsu osas. |

Kas soovid uurida rohkem juhtumiuuringuid? Vaata neid ressursse:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - eetilised dilemmad erinevates tööstusharudes.
* [Andmeteaduse eetika kursus](https://www.coursera.org/learn/data-science-ethics#syllabus) - olulised juhtumiuuringud.
* [Kus asjad on valesti läinud](https://deon.drivendata.org/examples/) - Deoni kontrollnimekiri koos näidetega.

> 🚨 Mõtle juhtumiuuringutele, mida oled näinud - kas oled kogenud või olnud mõjutatud sarnasest eetilisest väljakutsest oma elus? Kas suudad mõelda vähemalt ühele teisele juhtumiuuringule, mis illustreerib ühte eetilist väljakutset, mida oleme selles osas arutanud?

## Rakendatud eetika

Oleme rääkinud eetika kontseptsioonidest, väljakutsetest ja juhtumiuuringutest reaalses kontekstis. Aga kuidas alustada eetiliste põhimõtete ja praktikate _rakendamist_ oma projektides? Ja kuidas _operationaliseerida_ neid praktikaid parema juhtimise jaoks? Uurime mõningaid reaalse maailma lahendusi:

### 1. Professionaalsed eetikakoodeksid

Professionaalsed eetikakoodeksid pakuvad ühte võimalust organisatsioonidele "motiveerida" liikmeid toetama nende eetilisi põhimõtteid ja missioonilauseid. Koodeksid on _moraalsed juhised_ professionaalseks käitumiseks, aidates töötajatel või liikmetel teha otsuseid, mis vastavad nende organisatsiooni põhimõtetele. Need on ainult nii head, kui liikmete vabatahtlik järgimine; siiski pakuvad paljud organisatsioonid täiendavaid preemiaid ja karistusi, et motiveerida liikmeid järgima koodeksit.

Näited:
* [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) eetikakoodeks
* [Andmeteaduse Assotsiatsioon](http://datascienceassn.org/code-of-conduct.html) käitumiskoodeks (loodud 2013)
* [ACM eetikakoodeks ja professionaalse käitumise juhend](https://www.acm.org/code-of-ethics) (alates 1993)

> 🚨 Kas kuulud professionaalsesse inseneri- või andmeteaduse organisatsiooni? Uuri nende veebisaiti, et näha, kas nad määratlevad professionaalse eetikakoodeksi. Mida see ütleb nende eetiliste põhimõtete kohta? Kuidas nad "motiveerivad" liikmeid koodeksit järgima?

### 2. Eetika kontrollnimekirjad

Kuigi professionaalsed koodeksid määratlevad praktikutelt nõutava _eetilise käitumise_, on neil [teadaolevad piirangud](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) jõustamisel, eriti suurtes projektides. Selle asemel soovitavad paljud andmeteaduse eksperdid [kontrollnimekirju](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), mis võivad **ühendada põhimõtted praktikatega** deterministlikumal ja rakendatavamal viisil.

Kontrollnimekirjad muudavad küsimused "jah/ei" ülesanneteks, mida saab operationaliseerida, võimaldades neid jälgida osana standardsetest toote väljalaske töövoogudest.

Näited:
* [Deon](https://deon.drivendata.org/) - üldotstarbeline andmete eetika kontrollnimekiri, loodud [tööstuse soovituste](https://deon.drivendata.org/#checklist-citations) põhjal koos käsurea tööriistaga lihtsaks integreerimiseks.
* [Privaatsuse auditi kontrollnimekiri](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - pakub üldist juhendit teabe käsitlemise praktikate kohta juriidilisest ja sotsiaalsest vaatenurgast.
* [AI õiglus kontrollnimekiri](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - loodud AI praktikute poolt, et toetada õigluskontrollide kasutuselevõttu ja integreerimist AI arendustsüklitesse.
* [22 küsimust eetika kohta andmetes ja AI-s](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - avatum raamistik, struktureeritud eetiliste probleemide esialgseks uurimiseks disaini, rakendamise ja organisatsioonilises kontekstis.

### 3. Eetika regulatsioonid

Eetika seisneb jagatud väärtuste määratlemises ja õige asja tegemises _vabatahtlikult_. **Vastavus** seisneb _seaduse järgimises_, kui ja kus see on määratletud. **Juhtimine** hõlmab laiemalt kõiki viise, kuidas organisatsioonid rakendavad eetilisi põhimõtteid ja järgivad kehtestatud seadusi.

Tänapäeval toimub juhtimine organisatsioonides kahel viisil. Esiteks seisneb see **eetiliste AI** põhimõtete määratlemises ja praktikate kehtestamises, et operationaliseerida nende kasutuselevõttu kõigis organisatsiooni AI-ga seotud projektides. Teiseks seisneb see kõigi valitsuse määratud **andmekaitse regulatsioonide** järgimises piirkondades, kus organisatsioon tegutseb.

Näited andmekaitse ja privaatsuse regulatsioonidest:
* `1974`, [USA privaatsusseadus](https://www.justice.gov/opcl/privacy-act-1974) - reguleerib _föderaalvalitsuse_ isikuandmete kogumist, kasutamist ja avalikustamist.
* `1996`, [USA tervisekindlustuse kaasaskantavuse ja vastutuse seadus (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - kaitseb isiklikke terviseandmeid.
* `1998`, [USA laste veebipõhise privaatsuse kaitse seadus (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - kaitseb alla 13-aastaste laste andmete privaatsust.
* `2018`, [Üldine andmekaitse määrus (GDPR)](https://gdpr-info.eu/) - pakub kasutajaõigusi, andmekaitset ja privaatsust.
* `2018`, [California tarbijate privaatsusseadus (CCPA)](https://www.oag.ca.gov/privacy/ccpa) annab tarbijatele rohkem _õigusi_ nende (isiku)andmete üle.
* `2021`, Hiina [isikuandmete kaitse seadus](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) just vastu võetud, luues ühe maailma tugevaima veebipõhise andmete privaatsuse regulatsiooni.

> 🚨 Euroopa Liidu määratletud GDPR (Üldine andmekaitse määrus) jääb tänapäeval üheks mõjukamaks andmete privaatsuse regulatsiooniks. Kas teadsite, et see määratleb ka [8 kasutajaõigust](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr), et kaitsta kodanike digitaalset privaatsust ja isikuandmeid? Uurige, mis need on ja miks need on olulised.

### 4. Eetika kultuur

Pange tähele, et jääb puudu _vastavuse_ (tehes piisavalt, et täita "seaduse kirja") ja [süsteemsete probleemide](https://www.coursera.org/learn/data-science-ethics/home/week/4) (nagu ossifikatsioon, teabe asümmeetria ja jaotuse ebaõiglus) lahendamise vahel, mis võivad kiirendada AI relvastamist.

Viimane nõuab [koostööl põhinevaid lähenemisviise eetika kultuuride määratlemiseks](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f), mis loovad emotsionaalseid sidemeid ja järjepidevaid jagatud väärtusi _organisatsioonide vahel_ tööstuses. See nõuab rohkem [formaliseeritud andmete eetika kultuure](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) organisatsioonides - võimaldades _kõigil_ [tõmmata Andoni nööri](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (et tõstatada eetilisi probleeme varakult protsessis) ja muutes _eetilised hinnangud_ (nt värbamisel) AI projektide meeskonna moodustamise põhikriteeriumiks.

---
## [Loengu järgne viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/3) 🎯
## Ülevaade ja iseseisev õpe

Kursused ja raamatud aitavad mõista eetika põhikontseptsioone ja väljakutseid, samas kui juhtumiuuringud ja tööriistad aitavad rakendada eetika praktikaid reaalses kontekstis. Siin on mõned ressursid alustamiseks.
* [Masinõpe algajatele](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - Microsofti õppetund õiglusest.
* [Vastutustundliku tehisintellekti põhimõtted](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - tasuta õppeprogramm Microsoft Learnist.
* [Eetika ja andmeteadus](https://resources.oreilly.com/examples/0636920203964) - O'Reilly e-raamat (M. Loukides, H. Mason jt.)
* [Andmeteaduse eetika](https://www.coursera.org/learn/data-science-ethics#syllabus) - veebikursus Michigani Ülikoolist.
* [Eetika lahtiseletatult](https://ethicsunwrapped.utexas.edu/case-studies) - juhtumiuuringud Texase Ülikoolist.

# Ülesanne

[Kirjuta andmeeetika juhtumiuuring](assignment.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.