<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a34157cc63516eba97c89a0b2f8c3e6",
  "translation_date": "2025-09-03T21:53:36+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "hr"
}
-->
# Uvod u etiku podataka

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Etika u znanosti o podacima - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

---

Svi smo mi građani podataka koji živimo u svijetu prepunom podataka.

Tržišni trendovi pokazuju da će do 2022. godine jedna od tri velike organizacije kupovati i prodavati svoje podatke putem online [tržnica i burzi](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/). Kao **razvijatelji aplikacija**, bit će nam lakše i jeftinije integrirati uvide temeljene na podacima i automatizaciju vođenu algoritmima u svakodnevna korisnička iskustva. No, kako umjetna inteligencija postaje sveprisutna, morat ćemo razumjeti i potencijalne štete koje može prouzročiti [oružavanje](https://www.youtube.com/watch?v=TQHs8SA1qpk) takvih algoritama u velikim razmjerima.

Trendovi također pokazuju da ćemo do 2025. godine stvoriti i konzumirati preko [180 zettabajta](https://www.statista.com/statistics/871513/worldwide-data-created/) podataka. Kao **znanstvenici podataka**, to nam daje neviđenu razinu pristupa osobnim podacima. To znači da možemo izgraditi profile ponašanja korisnika i utjecati na donošenje odluka na načine koji stvaraju [iluziju slobodnog izbora](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice), dok potencijalno usmjeravamo korisnike prema ishodima koji nama odgovaraju. Također se postavljaju šira pitanja o privatnosti podataka i zaštiti korisnika.

Etika podataka sada su _nužne zaštitne mjere_ za znanost o podacima i inženjering, pomažući nam da minimiziramo potencijalne štete i nenamjerne posljedice naših radnji vođenih podacima. [Gartnerov Hype Cycle za AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) identificira relevantne trendove u digitalnoj etici, odgovornoj AI i upravljanju AI-jem kao ključne pokretače većih megatrendova oko _demokratizacije_ i _industrijalizacije_ AI-ja.

![Gartnerov Hype Cycle za AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

U ovoj lekciji istražit ćemo fascinantno područje etike podataka - od osnovnih pojmova i izazova, do studija slučaja i primijenjenih AI koncepata poput upravljanja - koji pomažu uspostaviti kulturu etike u timovima i organizacijama koje rade s podacima i AI-jem.

## [Kviz prije predavanja](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## Osnovne definicije

Počnimo s razumijevanjem osnovne terminologije.

Riječ "etika" dolazi od [grčke riječi "ethikos"](https://en.wikipedia.org/wiki/Ethics) (i njenog korijena "ethos") što znači _karakter ili moralna priroda_.

**Etika** se odnosi na zajedničke vrijednosti i moralna načela koja upravljaju našim ponašanjem u društvu. Etika se ne temelji na zakonima, već na široko prihvaćenim normama o tome što je "ispravno naspram pogrešnog". Međutim, etička razmatranja mogu utjecati na inicijative korporativnog upravljanja i vladine regulative koje stvaraju više poticaja za usklađenost.

**Etika podataka** je [nova grana etike](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1) koja "proučava i procjenjuje moralne probleme povezane s _podacima, algoritmima i odgovarajućim praksama_". Ovdje se **"podaci"** fokusiraju na radnje povezane s generiranjem, snimanjem, kuriranjem, obradom, širenjem, dijeljenjem i korištenjem, **"algoritmi"** se fokusiraju na AI, agente, strojno učenje i robote, a **"prakse"** se fokusiraju na teme poput odgovorne inovacije, programiranja, hakiranja i etičkih kodeksa.

**Primijenjena etika** je [praktična primjena moralnih razmatranja](https://en.wikipedia.org/wiki/Applied_ethics). To je proces aktivnog istraživanja etičkih pitanja u kontekstu _stvarnih radnji, proizvoda i procesa_, te poduzimanja korektivnih mjera kako bi se osiguralo da ostanu usklađeni s našim definiranim etičkim vrijednostima.

**Kultura etike** odnosi se na [_operacionalizaciju_ primijenjene etike](https://hbr.org/2019/05/how-to-design-an-ethical-organization) kako bi se osiguralo da se naši etički principi i prakse dosljedno i skalabilno usvajaju u cijeloj organizaciji. Uspješne kulture etike definiraju etičke principe na razini organizacije, pružaju značajne poticaje za usklađenost i jačaju norme etike poticanjem i amplifikacijom željenih ponašanja na svakoj razini organizacije.

## Koncepti etike

U ovom dijelu raspravljat ćemo o konceptima poput **zajedničkih vrijednosti** (principa) i **etičkih izazova** (problema) za etiku podataka - te istražiti **studije slučaja** koje vam pomažu razumjeti ove koncepte u stvarnim kontekstima.

### 1. Principi etike

Svaka strategija etike podataka počinje definiranjem _etičkih principa_ - "zajedničkih vrijednosti" koje opisuju prihvatljiva ponašanja i vode usklađene radnje u našim projektima vezanim uz podatke i AI. Možete ih definirati na individualnoj ili timskoj razini. Međutim, većina velikih organizacija ih navodi u _misiji etičkog AI-ja_ ili okviru koji je definiran na korporativnoj razini i dosljedno proveden u svim timovima.

**Primjer:** Microsoftova [Odgovorna AI](https://www.microsoft.com/en-us/ai/responsible-ai) misija glasi: _"Posvećeni smo razvoju AI-ja vođenog etičkim principima koji stavljaju ljude na prvo mjesto"_ - identificirajući 6 etičkih principa u okviru ispod:

![Odgovorna AI u Microsoftu](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Kratko ćemo istražiti ove principe. _Transparentnost_ i _odgovornost_ su temeljne vrijednosti na kojima se grade ostali principi - pa krenimo od njih:

* [**Odgovornost**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) čini praktičare _odgovornima_ za njihove operacije s podacima i AI-jem, te usklađenost s ovim etičkim principima.
* [**Transparentnost**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) osigurava da su radnje vezane uz podatke i AI _razumljive_ korisnicima, objašnjavajući što i zašto iza odluka.
* [**Pravednost**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - fokusira se na osiguranje da AI _sve ljude_ tretira pravedno, rješavajući bilo kakve sustavne ili implicitne socio-tehničke pristranosti u podacima i sustavima.
* [**Pouzdanost i sigurnost**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - osigurava da AI djeluje _dosljedno_ s definiranim vrijednostima, minimizirajući potencijalne štete ili nenamjerne posljedice.
* [**Privatnost i sigurnost**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - odnosi se na razumijevanje podrijetla podataka i pružanje _privatnosti podataka i povezanih zaštita_ korisnicima.
* [**Uključivost**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - odnosi se na dizajniranje AI rješenja s namjerom, prilagođavajući ih kako bi zadovoljila _širok raspon ljudskih potreba_ i sposobnosti.

> 🚨 Razmislite o tome što bi mogla biti vaša misija etike podataka. Istražite okvire etičkog AI-ja drugih organizacija - ovdje su primjeri iz [IBM-a](https://www.ibm.com/cloud/learn/ai-ethics), [Googlea](https://ai.google/principles) i [Facebooka](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Koje zajedničke vrijednosti imaju? Kako se ti principi odnose na AI proizvod ili industriju u kojoj djeluju?

### 2. Etički izazovi

Nakon što definiramo etičke principe, sljedeći korak je procijeniti naše radnje vezane uz podatke i AI kako bismo vidjeli jesu li usklađene s tim zajedničkim vrijednostima. Razmislite o svojim radnjama u dvije kategorije: _prikupljanje podataka_ i _dizajn algoritama_.

Kod prikupljanja podataka, radnje će vjerojatno uključivati **osobne podatke** ili osobno prepoznatljive informacije (PII) za identificirane žive pojedince. To uključuje [različite stavke neosobnih podataka](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en) koje _zajedno_ identificiraju pojedinca. Etički izazovi mogu se odnositi na _privatnost podataka_, _vlasništvo podataka_ i povezane teme poput _informiranog pristanka_ i _prava intelektualnog vlasništva_ za korisnike.

Kod dizajna algoritama, radnje će uključivati prikupljanje i kuriranje **skupova podataka**, a zatim njihovo korištenje za treniranje i implementaciju **modela podataka** koji predviđaju ishode ili automatiziraju odluke u stvarnim kontekstima. Etički izazovi mogu proizaći iz _pristranosti skupa podataka_, problema _kvalitete podataka_, _nepravednosti_ i _pogrešnog predstavljanja_ u algoritmima - uključujući neke probleme koji su sustavne prirode.

U oba slučaja, etički izazovi ističu područja gdje naše radnje mogu biti u sukobu s našim zajedničkim vrijednostima. Kako bismo otkrili, ublažili, minimizirali ili eliminirali ove zabrinutosti - trebamo postavljati moralna "da/ne" pitanja vezana uz naše radnje, a zatim poduzeti korektivne mjere prema potrebi. Pogledajmo neke etičke izazove i moralna pitanja koja postavljaju:

#### 2.1 Vlasništvo podataka

Prikupljanje podataka često uključuje osobne podatke koji mogu identificirati subjekte podataka. [Vlasništvo podataka](https://permission.io/blog/data-ownership) odnosi se na _kontrolu_ i [_prava korisnika_](https://permission.io/blog/data-ownership) vezana uz stvaranje, obradu i širenje podataka.

Moralna pitanja koja trebamo postaviti su:
* Tko posjeduje podatke? (korisnik ili organizacija)
* Koja prava imaju subjekti podataka? (npr. pristup, brisanje, prenosivost)
* Koja prava imaju organizacije? (npr. ispravljanje zlonamjernih korisničkih recenzija)

#### 2.2 Informirani pristanak

[Informirani pristanak](https://legaldictionary.net/informed-consent/) definira čin korisnika koji pristaju na radnju (poput prikupljanja podataka) uz _potpuno razumijevanje_ relevantnih činjenica, uključujući svrhu, potencijalne rizike i alternative.

Pitanja za istraživanje ovdje su:
* Je li korisnik (subjekt podataka) dao dopuštenje za prikupljanje i korištenje podataka?
* Je li korisnik razumio svrhu za koju su ti podaci prikupljeni?
* Je li korisnik razumio potencijalne rizike od sudjelovanja?

#### 2.3 Intelektualno vlasništvo

[Intelektualno vlasništvo](https://en.wikipedia.org/wiki/Intellectual_property) odnosi se na nematerijalne kreacije koje proizlaze iz ljudske inicijative, a koje mogu _imati ekonomsku vrijednost_ za pojedince ili tvrtke.

Pitanja za istraživanje ovdje su:
* Jesu li prikupljeni podaci imali ekonomsku vrijednost za korisnika ili tvrtku?
* Ima li **korisnik** intelektualno vlasništvo ovdje?
* Ima li **organizacija** intelektualno vlasništvo ovdje?
* Ako ta prava postoje, kako ih štitimo?

#### 2.4 Privatnost podataka

[Privatnost podataka](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) ili informacijska privatnost odnosi se na očuvanje privatnosti korisnika i zaštitu identiteta korisnika u vezi s osobno prepoznatljivim informacijama.

Pitanja za istraživanje ovdje su:
* Jesu li korisnički (osobni) podaci zaštićeni od hakiranja i curenja?
* Jesu li korisnički podaci dostupni samo ovlaštenim korisnicima i kontekstima?
* Je li anonimnost korisnika očuvana kada se podaci dijele ili šire?
* Može li se korisnik de-identificirati iz anonimiziranih skupova podataka?

#### 2.5 Pravo na zaborav

[Pravo na zaborav](https://en.wikipedia.org/wiki/Right_to_be_forgotten) ili [Pravo na brisanje](https://www.gdpreu.org/right-to-be-forgotten/) pruža dodatnu zaštitu osobnih podataka korisnicima. Konkretno, daje korisnicima pravo da zatraže brisanje ili uklanjanje osobnih podataka iz internetskih pretraživanja i drugih lokacija, _pod određenim okolnostima_ - omogućujući im novi početak online bez da se prošle radnje drže protiv njih.

Pitanja za istraživanje ovdje su:
* Omogućava li sustav subjektima podataka da zatraže brisanje?
* Treba li povlačenje korisničkog pristanka automatski pokrenuti brisanje?
* Jesu li podaci prikupljeni bez pristanka ili nezakonitim sredstvima?
* Jesmo li usklađeni s vladinim regulativama za privatnost podataka?

#### 2.6 Pristranost skupa podataka

Pristranost skupa podataka ili [pristranost prikupljanja](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) odnosi se na odabir _nereprezentativnog_ podskupa podataka za razvoj algoritama, stvarajući potencijalnu nepravednost u ishodima za različite skupine. Vrste pristranosti uključuju pristranost odabira ili uzorkovanja, pristranost volontera i pristranost instrumenata.

Pitanja za istraživanje ovdje su:
* Jesmo li regrutirali reprezentativni skup subjekata podataka?
* Jesmo li testirali naš prikupljeni ili kurirani skup podataka na razne pristranosti?
* Možemo li ublažiti ili ukloniti otkrivene pristranosti?

#### 2.7 Kvaliteta podataka

[Kvaliteta podataka](https://lakefs.io/data-quality-testing/) ispituje valjanost kuriranog skupa podataka korištenog za razvoj naših algoritama, provjeravajući jesu li značajke i zapisi u skladu s zahtjevima za razinu točnosti i dosljednosti potrebnu za naš AI cilj.

Pitanja za istraživanje ovdje su:
* Jesmo li uhvatili valjane _značajke_ za našu svrhu?
* Jesu li podaci dosljedno prikupljeni iz različitih izvora podataka?
* Je li skup podataka _potpun_ za različite uvjete ili scenarije?
* Jesu li informacije točno uhvaćene u odražavanju stvarnosti?
[Algorithm Fairness](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) provjerava dizajn algoritma kako bi se utvrdilo diskriminira li sustavno određene podskupine subjekata podataka, što može dovesti do [potencijalnih šteta](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) u _dodjeli_ (gdje se resursi uskraćuju ili odbijaju toj skupini) i _kvaliteti usluge_ (gdje AI nije jednako precizan za neke podskupine kao za druge).

Pitanja za istraživanje:
 * Jesmo li procijenili točnost modela za različite podskupine i uvjete?
 * Jesmo li detaljno analizirali sustav zbog potencijalnih šteta (npr. stereotipiziranja)?
 * Možemo li revidirati podatke ili ponovno trenirati modele kako bismo ublažili identificirane štete?

Istražite resurse poput [AI Fairness checklists](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) za više informacija.

#### 2.9 Pogrešno predstavljanje

[Pogrešno predstavljanje podataka](https://www.sciencedirect.com/topics/computer-science/misrepresentation) odnosi se na pitanje jesmo li komunikaciju utemeljenu na iskreno prijavljenim podacima koristili na obmanjujući način kako bismo podržali željeni narativ.

Pitanja za istraživanje:
 * Prijavljujemo li nepotpune ili netočne podatke?
 * Vizualiziramo li podatke na način koji vodi do pogrešnih zaključaka?
 * Koristimo li selektivne statističke tehnike za manipulaciju rezultatima?
 * Postoje li alternativna objašnjenja koja mogu ponuditi drugačiji zaključak?

#### 2.10 Slobodan izbor
[Iluzija slobodnog izbora](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) događa se kada sustavi "arhitekture izbora" koriste algoritme za donošenje odluka kako bi potaknuli ljude na odabir preferiranog ishoda, dok im se istovremeno čini da imaju opcije i kontrolu. Ovi [tamni obrasci](https://www.darkpatterns.org/) mogu uzrokovati društvene i ekonomske štete korisnicima. Budući da odluke korisnika utječu na profile ponašanja, te radnje potencijalno oblikuju buduće izbore koji mogu pojačati ili proširiti utjecaj tih šteta.

Pitanja za istraživanje:
 * Je li korisnik razumio implikacije donošenja tog izbora?
 * Je li korisnik bio svjestan (alternativnih) izbora i prednosti i nedostataka svakog?
 * Može li korisnik kasnije poništiti automatizirani ili utjecani izbor?

### 3. Studije slučaja

Kako bismo ove etičke izazove stavili u kontekst stvarnog svijeta, korisno je pogledati studije slučaja koje ističu potencijalne štete i posljedice za pojedince i društvo kada se zanemaruju etička kršenja.

Evo nekoliko primjera:

| Etički izazov | Studija slučaja  | 
|--- |--- |
| **Informirani pristanak** | 1972 - [Tuskegee Syphilis Study](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Afroameričkim muškarcima koji su sudjelovali u studiji obećana je besplatna medicinska skrb _ali su ih istraživači obmanuli_ ne informirajući ih o dijagnozi ili dostupnosti liječenja. Mnogi su umrli, a partneri i djeca su bili pogođeni; studija je trajala 40 godina. | 
| **Privatnost podataka** |  2007 - [Netflix data prize](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) pružio je istraživačima _10M anonimiziranih ocjena filmova od 50K korisnika_ kako bi se poboljšali algoritmi preporuka. Međutim, istraživači su uspjeli povezati anonimizirane podatke s osobno identificiranim podacima u _vanjskim skupovima podataka_ (npr. IMDb komentari) - učinkovito "deanonimizirajući" neke Netflix pretplatnike.|
| **Pristranost u prikupljanju podataka**  | 2013 - Grad Boston [razvio Street Bump](https://www.boston.gov/transportation/street-bump), aplikaciju koja je omogućila građanima da prijave rupe na cestama, dajući gradu bolje podatke o cestama za pronalaženje i popravak problema. Međutim, [ljudi s nižim prihodima imali su manje pristupa automobilima i telefonima](https://hbr.org/2013/04/the-hidden-biases-in-big-data), čineći njihove probleme s cestama nevidljivima u ovoj aplikaciji. Programeri su surađivali s akademicima na _pristupu i digitalnim podjelama_ radi pravednosti. |
| **Pravednost algoritma**  | 2018 - MIT [Gender Shades Study](http://gendershades.org/overview.html) procijenila je točnost AI proizvoda za klasifikaciju spola, otkrivajući nedostatke u točnosti za žene i osobe tamnije boje kože. [Apple Card iz 2019.](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) činilo se da nudi manje kredita ženama nego muškarcima. Oba primjera ilustriraju probleme pristranosti algoritma koji dovode do socio-ekonomskih šteta.|
| **Pogrešno predstavljanje podataka** | 2020 - [Georgia Department of Public Health objavio COVID-19 grafikone](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) koji su izgledali kao da obmanjuju građane o trendovima potvrđenih slučajeva s ne-kronološkim redoslijedom na x-osi. Ovo ilustrira pogrešno predstavljanje kroz trikove vizualizacije. |
| **Iluzija slobodnog izbora** | 2020 - Edukativna aplikacija [ABCmouse platila $10M za nagodbu s FTC-om](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) gdje su roditelji bili zarobljeni u plaćanju pretplata koje nisu mogli otkazati. Ovo ilustrira tamne obrasce u arhitekturama izbora, gdje su korisnici bili potaknuti na potencijalno štetne odluke. |
| **Privatnost podataka i prava korisnika** | 2021 - Facebook [Data Breach](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) otkrio podatke 530M korisnika, što je rezultiralo nagodbom od $5B s FTC-om. Međutim, odbio je obavijestiti korisnike o povredi, kršeći prava korisnika na transparentnost i pristup podacima. |

Želite istražiti više studija slučaja? Pogledajte ove resurse:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - etičke dileme u raznim industrijama. 
* [Data Science Ethics course](https://www.coursera.org/learn/data-science-ethics#syllabus) - studije slučaja u fokusu.
* [Where things have gone wrong](https://deon.drivendata.org/examples/) - Deon popis s primjerima.


> 🚨 Razmislite o studijama slučaja koje ste vidjeli - jeste li doživjeli ili bili pogođeni sličnim etičkim izazovom u svom životu? Možete li se sjetiti barem jedne druge studije slučaja koja ilustrira jedan od etičkih izazova koje smo raspravili u ovom odjeljku?

## Primijenjena etika

Razgovarali smo o konceptima etike, izazovima i studijama slučaja u kontekstu stvarnog svijeta. No, kako započeti _primjenu_ etičkih načela i praksi u našim projektima? I kako _operacionalizirati_ ove prakse za bolju upravu? Istražimo neka rješenja iz stvarnog svijeta:

### 1. Profesionalni kodeksi

Profesionalni kodeksi nude jednu opciju za organizacije da "potaknu" članove na podršku njihovim etičkim načelima i misiji. Kodeksi su _moralne smjernice_ za profesionalno ponašanje, pomažući zaposlenicima ili članovima da donose odluke koje su u skladu s načelima njihove organizacije. Oni su učinkoviti koliko i dobrovoljna usklađenost članova; međutim, mnoge organizacije nude dodatne nagrade i kazne kako bi motivirale usklađenost.

Primjeri uključuju:

 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Kodeks etike
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Kodeks ponašanja (kreiran 2013.)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (od 1993.)

> 🚨 Pripadate li profesionalnoj inženjerskoj ili organizaciji za podatkovnu znanost? Istražite njihovu stranicu kako biste vidjeli definiraju li profesionalni kodeks etike. Što to govori o njihovim etičkim načelima? Kako "potiču" članove da slijede kodeks?

### 2. Etičke kontrolne liste

Dok profesionalni kodeksi definiraju potrebna _etička ponašanja_ od praktičara, oni [imaju poznata ograničenja](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) u provedbi, posebno u projektima velikih razmjera. Umjesto toga, mnogi stručnjaci za podatkovnu znanost [zagovaraju kontrolne liste](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), koje mogu **povezati načela s praksama** na deterministički i provediv način.

Kontrolne liste pretvaraju pitanja u zadatke "da/ne" koji se mogu operacionalizirati, omogućujući njihovo praćenje kao dio standardnih tijekova rada za izdavanje proizvoda.

Primjeri uključuju:
 * [Deon](https://deon.drivendata.org/) - opća kontrolna lista za etiku podataka kreirana iz [preporuka industrije](https://deon.drivendata.org/#checklist-citations) s alatom naredbenog retka za jednostavnu integraciju.
 * [Privacy Audit Checklist](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - pruža opće smjernice za praksu rukovanja informacijama iz pravne i društvene perspektive.
 * [AI Fairness Checklist](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - kreirana od strane AI praktičara za podršku usvajanju i integraciji provjera pravednosti u AI razvojne cikluse.
 * [22 pitanja za etiku u podacima i AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - otvoreniji okvir, strukturiran za početno istraživanje etičkih pitanja u dizajnu, implementaciji i organizacijskim kontekstima.

### 3. Etičke regulative

Etika se odnosi na definiranje zajedničkih vrijednosti i činjenje ispravnih stvari _dobrovoljno_. **Usklađenost** se odnosi na _poštivanje zakona_ ako i gdje je definiran. **Upravljanje** općenito pokriva sve načine na koje organizacije djeluju kako bi provele etička načela i uskladile se s utvrđenim zakonima.

Danas upravljanje ima dva oblika unutar organizacija. Prvo, radi se o definiranju **etičkih AI** načela i uspostavljanju praksi za operacionalizaciju usvajanja u svim AI projektima organizacije. Drugo, radi se o usklađivanju sa svim vladinim propisima o zaštiti podataka za regije u kojima djeluje.

Primjeri propisa o zaštiti podataka i privatnosti:

 * `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - regulira _saveznu vladu_ u prikupljanju, korištenju i otkrivanju osobnih podataka.
 * `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - štiti osobne zdravstvene podatke.
 * `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - štiti privatnost podataka djece mlađe od 13 godina.
 * `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - pruža prava korisnika, zaštitu podataka i privatnost.
 * `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) daje potrošačima više _prava_ nad njihovim (osobnim) podacima.
 * `2021`, Kineski [Zakon o zaštiti osobnih podataka](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) upravo je donesen, stvarajući jedan od najjačih propisa o privatnosti podataka na internetu u svijetu.

> 🚨 Europska unija definirala je GDPR (Opća uredba o zaštiti podataka) koji ostaje jedan od najutjecajnijih propisa o privatnosti podataka danas. Jeste li znali da također definira [8 prava korisnika](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) za zaštitu digitalne privatnosti i osobnih podataka građana? Saznajte koja su to prava i zašto su važna.

### 4. Kultura etike

Napominjemo da i dalje postoji nematerijalni jaz između _usklađenosti_ (činjenja dovoljno da se zadovolji "slovo zakona") i rješavanja [sustavnih problema](https://www.coursera.org/learn/data-science-ethics/home/week/4) (poput osifikacije, asimetrije informacija i distribucijske nepravednosti) koji mogu ubrzati "oružavanje" AI-a.

Ovo drugo zahtijeva [suradničke pristupe za definiranje kultura etike](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f) koje grade emocionalne veze i dosljedne zajedničke vrijednosti _među organizacijama_ u industriji. To poziva na više [formaliziranih kultura etike podataka](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) u organizacijama - omogućujući _svima_ da [povuku Andon konopac](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (kako bi rano ukazali na etičke probleme) i čineći _etičke procjene_ (npr. pri zapošljavanju) ključnim kriterijem za formiranje timova u AI projektima.

---
## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/) 🎯
## Pregled i samostalno učenje 

Tečajevi i knjige pomažu u razumijevanju osnovnih etičkih koncepata i izazova, dok studije slučaja i alati pomažu u primjeni etičkih praksi u stvarnim kontekstima. Evo nekoliko resursa za početak.

* [Machine Learning For Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - lekcija o pravednosti, od Microsofta.
* [Principi odgovorne umjetne inteligencije](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - besplatni obrazovni program od Microsoft Learn.
* [Etika i znanost o podacima](https://resources.oreilly.com/examples/0636920203964) - O'Reilly EBook (M. Loukides, H. Mason i dr.)
* [Etika u znanosti o podacima](https://www.coursera.org/learn/data-science-ethics#syllabus) - online tečaj Sveučilišta Michigan.
* [Etika razotkrivena](https://ethicsunwrapped.utexas.edu/case-studies) - studije slučaja Sveučilišta Texas.

# Zadatak

[Napišite studiju slučaja o etici podataka](assignment.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešne interpretacije koje mogu proizaći iz korištenja ovog prijevoda.