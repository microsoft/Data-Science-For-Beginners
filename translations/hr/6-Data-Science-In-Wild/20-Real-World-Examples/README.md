<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f95679140c7cb39c30ccba535cd8f03f",
  "translation_date": "2025-09-04T22:04:55+00:00",
  "source_file": "6-Data-Science-In-Wild/20-Real-World-Examples/README.md",
  "language_code": "hr"
}
-->
# Data Science u stvarnom svijetu

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-RealWorld.png) |
| :--------------------------------------------------------------------------------------------------------------: |
|               Data Science u stvarnom svijetu - _Sketchnote by [@nitya](https://twitter.com/nitya)_               |

Skoro smo na kraju ovog edukativnog putovanja!

Počeli smo s definicijama data sciencea i etike, istražili razne alate i tehnike za analizu i vizualizaciju podataka, pregledali životni ciklus data sciencea te razmotrili skaliranje i automatizaciju radnih procesa uz usluge računalstva u oblaku. Dakle, vjerojatno se pitate: _"Kako točno primijeniti sve ove spoznaje u stvarnim kontekstima?"_

U ovoj lekciji istražit ćemo primjene data sciencea u industriji i detaljno razmotriti specifične primjere u istraživanju, digitalnim humanističkim znanostima i održivosti. Pogledat ćemo prilike za studentske projekte i zaključiti s korisnim resursima koji će vam pomoći da nastavite svoje edukativno putovanje!

## Kviz prije predavanja

[Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ds/)

## Data Science + Industrija

Zahvaljujući demokratizaciji AI-a, programerima je sada lakše dizajnirati i integrirati odluke vođene umjetnom inteligencijom i uvide temeljene na podacima u korisničke iskustve i razvojne procese. Evo nekoliko primjera kako se data science "primjenjuje" u stvarnim industrijskim aplikacijama:

 * [Google Flu Trends](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) koristio je data science za povezivanje pojmova pretraživanja s trendovima gripe. Iako je pristup imao nedostatke, podigao je svijest o mogućnostima (i izazovima) predviđanja u zdravstvu temeljenog na podacima.

 * [UPS Routing Predictions](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - objašnjava kako UPS koristi data science i strojno učenje za predviđanje optimalnih ruta dostave, uzimajući u obzir vremenske uvjete, prometne obrasce, rokove dostave i druge faktore.

 * [NYC Taxicab Route Visualization](http://chriswhong.github.io/nyctaxi/) - podaci prikupljeni pomoću [Zakona o slobodi informacija](https://chriswhong.com/open-data/foil_nyc_taxi/) pomogli su vizualizirati jedan dan u životu taksija u New Yorku, omogućujući nam da razumijemo kako se kreću po gradu, koliko zarađuju i koliko traju vožnje tijekom 24-satnog razdoblja.

 * [Uber Data Science Workbench](https://eng.uber.com/dsw/) - koristi podatke (o lokacijama preuzimanja i odredišta, trajanju vožnje, preferiranim rutama itd.) prikupljene iz milijuna Uber vožnji *dnevno* za izradu alata za analizu podataka koji pomaže u određivanju cijena, sigurnosti, otkrivanju prijevara i navigacijskim odlukama.

 * [Sports Analytics](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - fokusira se na _prediktivnu analitiku_ (analiza timova i igrača - poput [Moneyball](https://datasciencedegree.wisconsin.edu/blog/moneyball-proves-importance-big-data-big-ideas/) - i upravljanje navijačima) i _vizualizaciju podataka_ (nadzorne ploče za timove i navijače, igre itd.) s primjenama poput skautinga talenata, sportskog klađenja i upravljanja inventarom/objektima.

 * [Data Science u bankarstvu](https://data-flair.training/blogs/data-science-in-banking/) - ističe vrijednost data sciencea u financijskoj industriji s primjenama koje se kreću od modeliranja rizika i otkrivanja prijevara do segmentacije klijenata, predviđanja u stvarnom vremenu i sustava preporuka. Prediktivna analitika također pokreće ključne mjere poput [kreditnih bodova](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit).

 * [Data Science u zdravstvu](https://data-flair.training/blogs/data-science-in-healthcare/) - ističe primjene poput medicinskog snimanja (npr. MRI, X-Ray, CT-Scan), genomike (sekvenciranje DNA), razvoja lijekova (procjena rizika, predviđanje uspjeha), prediktivne analitike (skrb za pacijente i logistika opskrbe), praćenja i prevencije bolesti itd.

![Primjene Data Sciencea u stvarnom svijetu](../../../../6-Data-Science-In-Wild/20-Real-World-Examples/images/data-science-applications.png) Izvor slike: [Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

Slika prikazuje druge domene i primjere primjene tehnika data sciencea. Želite istražiti druge primjene? Pogledajte odjeljak [Pregled i samostalno učenje](../../../../6-Data-Science-In-Wild/20-Real-World-Examples) u nastavku.

## Data Science + Istraživanje

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Research.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Data Science & Istraživanje - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

Dok se primjene u stvarnom svijetu često fokusiraju na industrijske slučajeve korištenja u velikim razmjerima, _istraživačke_ primjene i projekti mogu biti korisni iz dvije perspektive:

* _prilike za inovaciju_ - istraživanje brzog prototipiranja naprednih koncepata i testiranje korisničkih iskustava za aplikacije sljedeće generacije.
* _izazovi implementacije_ - istraživanje potencijalnih šteta ili nenamjernih posljedica tehnologija data sciencea u stvarnim kontekstima.

Za studente, ovi istraživački projekti mogu pružiti prilike za učenje i suradnju koje poboljšavaju razumijevanje teme te proširuju svijest i angažman s relevantnim ljudima ili timovima koji rade u područjima interesa. Kako izgledaju istraživački projekti i kako mogu imati utjecaj?

Pogledajmo jedan primjer - [MIT Gender Shades Study](http://gendershades.org/overview.html) od Joy Buolamwini (MIT Media Labs) s [prepoznatljivim istraživačkim radom](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf) koji je koautorirala s Timnit Gebru (tada u Microsoft Researchu) i koji se fokusirao na:

 * **Što:** Cilj istraživačkog projekta bio je _procijeniti pristranost prisutnu u algoritmima i skupovima podataka za automatsku analizu lica_ na temelju spola i tipa kože. 
 * **Zašto:** Analiza lica koristi se u područjima poput provedbe zakona, sigurnosti u zračnim lukama, sustava zapošljavanja i drugih - konteksti u kojima netočne klasifikacije (npr. zbog pristranosti) mogu uzrokovati potencijalne ekonomske i društvene štete za pogođene pojedince ili skupine. Razumijevanje (i uklanjanje ili ublažavanje) pristranosti ključno je za pravednost u korištenju.
 * **Kako:** Istraživači su prepoznali da se postojeći referentni skupovi podataka uglavnom koriste za subjekte svjetlije kože te su kreirali novi skup podataka (1000+ slika) koji je _uravnoteženiji_ prema spolu i tipu kože. Skup podataka korišten je za procjenu točnosti tri proizvoda za klasifikaciju spola (od Microsofta, IBM-a i Face++). 

Rezultati su pokazali da, iako je ukupna točnost klasifikacije bila dobra, postojala je primjetna razlika u stopama pogrešaka između različitih podskupina - s **pogrešnim određivanjem spola** češćim kod žena ili osoba tamnije kože, što ukazuje na pristranost.

**Ključni rezultati:** Podignuta je svijest da data science treba više _reprezentativnih skupova podataka_ (uravnotežene podskupine) i više _inkluzivnih timova_ (raznolike pozadine) kako bi se pristranosti prepoznale i uklonile ili ublažile ranije u AI rješenjima. Istraživački napori poput ovog također su ključni za mnoge organizacije u definiranju principa i praksi za _odgovorni AI_ kako bi se poboljšala pravednost u njihovim AI proizvodima i procesima.

**Želite saznati više o relevantnim istraživačkim naporima u Microsoftu?**

* Pogledajte [Microsoft Research Projects](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project) o umjetnoj inteligenciji.
* Istražite studentske projekte iz [Microsoft Research Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/).
* Pogledajte projekt [Fairlearn](https://fairlearn.org/) i inicijative [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6).

## Data Science + Humanističke znanosti

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Data Science & Digitalne humanističke znanosti - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

Digitalne humanističke znanosti [definirane su](https://digitalhumanities.stanford.edu/about-dh-stanford) kao "zbirka praksi i pristupa koji kombiniraju računalne metode s humanističkim istraživanjem". [Stanford projekti](https://digitalhumanities.stanford.edu/projects) poput _"rebooting history"_ i _"poetic thinking"_ ilustriraju povezanost između [Digitalnih humanističkih znanosti i Data Sciencea](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science) - naglašavajući tehnike poput analize mreža, vizualizacije informacija, prostorne i tekstualne analize koje nam mogu pomoći da ponovno razmotrimo povijesne i književne skupove podataka kako bismo dobili nove uvide i perspektive.

*Želite istražiti i proširiti projekt u ovom području?*

Pogledajte ["Emily Dickinson and the Meter of Mood"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671) - izvrstan primjer od [Jen Looper](https://twitter.com/jenlooper) koji postavlja pitanje kako možemo koristiti data science za ponovno razmatranje poznate poezije i preispitivanje njezina značenja te doprinosa autora u novim kontekstima. Na primjer, _možemo li predvidjeti godišnje doba u kojem je pjesma napisana analizom tona ili sentimenta_ - i što nam to govori o autorovom stanju uma tijekom relevantnog razdoblja?

Da bismo odgovorili na to pitanje, slijedimo korake životnog ciklusa data sciencea:
 * [`Prikupljanje podataka`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#acquiring-the-dataset) - za prikupljanje relevantnog skupa podataka za analizu. Opcije uključuju korištenje API-ja (npr. [Poetry DB API](https://poetrydb.org/index.html)) ili struganje web stranica (npr. [Project Gutenberg](https://www.gutenberg.org/files/12242/12242-h/12242-h.htm)) pomoću alata poput [Scrapy](https://scrapy.org/).
 * [`Čišćenje podataka`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#clean-the-data) - objašnjava kako se tekst može formatirati, sanitizirati i pojednostaviti pomoću osnovnih alata poput Visual Studio Codea i Microsoft Excela.
 * [`Analiza podataka`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#working-with-the-data-in-a-notebook) - objašnjava kako sada možemo uvesti skup podataka u "Notebooks" za analizu pomoću Python paketa (poput pandas, numpy i matplotlib) za organizaciju i vizualizaciju podataka.
 * [`Analiza sentimenta`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#sentiment-analysis-using-cognitive-services) - objašnjava kako možemo integrirati usluge u oblaku poput Text Analyticsa, koristeći alate s malo koda poput [Power Automate](https://flow.microsoft.com/en-us/) za automatizirane radne procese obrade podataka.

Koristeći ovaj radni proces, možemo istražiti sezonske utjecaje na sentiment pjesama i pomoći nam oblikovati vlastite perspektive o autoru. Isprobajte sami - zatim proširite bilježnicu kako biste postavili druga pitanja ili vizualizirali podatke na nove načine!

> Možete koristiti neke od alata iz [Digital Humanities toolkit](https://github.com/Digital-Humanities-Toolkit) za istraživanje ovih područja.

## Data Science + Održivost

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Sustainability.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Data Science & Održivost - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

[Agenda za održivi razvoj 2030](https://sdgs.un.org/2030agenda) - koju su usvojile sve članice Ujedinjenih naroda 2015. godine - identificira 17 ciljeva, uključujući one koji se fokusiraju na **zaštitu planeta** od degradacije i utjecaja klimatskih promjena. [Microsoft Sustainability](https://www.microsoft.com/en-us/sustainability) inicijativa podržava ove ciljeve istražujući načine na koje tehnološka rješenja mogu podržati i izgraditi održiviju budućnost s [fokusom na 4 cilja](https://dev.to/azure/a-visual-guide-to-sustainable-software-engineering-53hh) - biti ugljično negativan, vodno pozitivan, bez otpada i biodiverzan do 2030.

Rješavanje ovih izazova na skalabilan i pravovremen način zahtijeva razmišljanje u oblaku - i velike količine podataka. [Planetary Computer](https://planetarycomputer.microsoft.com/) inicijativa pruža 4 komponente koje pomažu data znanstvenicima i programerima u ovom naporu:

 * [Katalog podataka](https://planetarycomputer.microsoft.com/catalog) - s petabajtima podataka o Zemljinim sustavima (besplatno i hostirano na Azureu).
 * [Planetary API](https://planetarycomputer.microsoft.com/docs/reference/stac/) - za pomoć korisnicima u pretraživanju relevantnih podataka kroz prostor i vrijeme.
 * [Hub](https://planetarycomputer.microsoft.com/docs/overview/environment/) - upravljano okruženje za znanstvenike za obradu masivnih geoprostornih skupova podataka.
 * [Aplikacije](https://planetarycomputer.microsoft.com/applications) - prikazuju slučajeve korištenja i alate za uvide u održivost.
**Projekt Planetary Computer trenutno je u fazi pregleda (od rujna 2021.)** - evo kako možete započeti s doprinosom rješenjima za održivost koristeći podatkovnu znanost.

* [Zatražite pristup](https://planetarycomputer.microsoft.com/account/request) kako biste započeli istraživanje i povezali se s kolegama.
* [Istražite dokumentaciju](https://planetarycomputer.microsoft.com/docs/overview/about) kako biste razumjeli podržane skupove podataka i API-je.
* Istražite aplikacije poput [Praćenje ekosustava](https://analytics-lab.org/ecosystemmonitoring/) za inspiraciju za ideje o primjeni.

Razmislite o tome kako možete koristiti vizualizaciju podataka za otkrivanje ili naglašavanje relevantnih uvida u područjima poput klimatskih promjena i krčenja šuma. Ili razmislite o tome kako se uvidi mogu koristiti za stvaranje novih korisničkih iskustava koja motiviraju promjene ponašanja za održiviji način života.

## Podatkovna znanost + studenti

Razgovarali smo o stvarnim primjenama u industriji i istraživanju te istražili primjere primjene podatkovne znanosti u digitalnim humanističkim znanostima i održivosti. Pa kako možete izgraditi svoje vještine i podijeliti svoje znanje kao početnici u podatkovnoj znanosti?

Evo nekoliko primjera studentskih projekata iz podatkovne znanosti koji vas mogu inspirirati.

* [MSR Ljetna škola podatkovne znanosti](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/#!projects) s GitHub [projektima](https://github.com/msr-ds3) koji istražuju teme poput:
   - [Rasna pristranost u policijskoj upotrebi sile](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2019-replicating-an-empirical-analysis-of-racial-differences-in-police-use-of-force/) | [Github](https://github.com/msr-ds3/stop-question-frisk)
   - [Pouzdanost sustava podzemne željeznice u New Yorku](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2018-exploring-the-reliability-of-the-nyc-subway-system/) | [Github](https://github.com/msr-ds3/nyctransit)
* [Digitalizacija materijalne kulture: Istraživanje socio-ekonomskih distribucija u Sirkapu](https://claremont.maps.arcgis.com/apps/Cascade/index.html?appid=bdf2aef0f45a4674ba41cd373fa23afc) - od [Ornella Altunyan](https://twitter.com/ornelladotcom) i tima iz Claremonta, koristeći [ArcGIS StoryMaps](https://storymaps.arcgis.com/).

## 🚀 Izazov

Potražite članke koji preporučuju projekte iz podatkovne znanosti prilagođene početnicima - poput [ovih 50 područja](https://www.upgrad.com/blog/data-science-project-ideas-topics-beginners/) ili [ovih 21 ideja za projekte](https://www.intellspot.com/data-science-project-ideas) ili [ovih 16 projekata s izvornim kodom](https://data-flair.training/blogs/data-science-project-ideas/) koje možete rastaviti i ponovno sastaviti. I ne zaboravite pisati blog o svojim iskustvima učenja i podijeliti svoje uvide s nama.

## Kviz nakon predavanja

## [Kviz nakon predavanja](https://ff-quizzes.netlify.app/en/ds/)

## Pregled i samostalno učenje

Želite istražiti više primjera primjene? Evo nekoliko relevantnih članaka:
* [17 primjena i primjera podatkovne znanosti](https://builtin.com/data-science/data-science-applications-examples) - srpanj 2021.
* [11 zadivljujućih primjena podatkovne znanosti u stvarnom svijetu](https://myblindbird.com/data-science-applications-real-world/) - svibanj 2021.
* [Podatkovna znanost u stvarnom svijetu](https://towardsdatascience.com/data-science-in-the-real-world/home) - zbirka članaka
* Podatkovna znanost u: [Obrazovanju](https://data-flair.training/blogs/data-science-in-education/), [Poljoprivredi](https://data-flair.training/blogs/data-science-in-agriculture/), [Financijama](https://data-flair.training/blogs/data-science-in-finance/), [Filmovima](https://data-flair.training/blogs/data-science-at-movies/) i više.

## Zadatak

[Istražite skup podataka Planetary Computer](assignment.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.