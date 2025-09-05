<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "06bac7959b46b6e8aedcae014278c476",
  "translation_date": "2025-09-05T19:46:59+00:00",
  "source_file": "6-Data-Science-In-Wild/20-Real-World-Examples/README.md",
  "language_code": "sl"
}
-->
# Podatkovna znanost v resničnem svetu

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-RealWorld.png) |
| :--------------------------------------------------------------------------------------------------------------: |
|               Podatkovna znanost v resničnem svetu - _Sketchnote by [@nitya](https://twitter.com/nitya)_               |

Skoraj smo na koncu te učne poti!

Začeli smo z definicijami podatkovne znanosti in etike, raziskovali različna orodja in tehnike za analizo ter vizualizacijo podatkov, pregledali življenjski cikel podatkovne znanosti ter preučili možnosti za skaliranje in avtomatizacijo delovnih procesov podatkovne znanosti z uporabo storitev v oblaku. Verjetno se sprašujete: _"Kako lahko vse te nauke prenesem v resnične kontekste?"_

V tej lekciji bomo raziskali resnične aplikacije podatkovne znanosti v industriji ter se poglobili v konkretne primere v raziskovalnih, digitalno-humanističnih in trajnostnih kontekstih. Pogledali bomo priložnosti za študentske projekte ter zaključili z uporabnimi viri, ki vam bodo pomagali nadaljevati vašo učno pot!

## Predhodni kviz

## [Predhodni kviz](https://ff-quizzes.netlify.app/en/ds/quiz/38)

## Podatkovna znanost + Industrija

Zaradi demokratizacije umetne inteligence razvijalci zdaj lažje oblikujejo in vključujejo odločitve, ki temeljijo na umetni inteligenci, ter vpoglede, ki temeljijo na podatkih, v uporabniške izkušnje in razvojne delovne procese. Tukaj je nekaj primerov, kako se podatkovna znanost "uporablja" v resničnih aplikacijah v industriji:

 * [Google Flu Trends](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) je uporabil podatkovno znanost za povezovanje iskalnih izrazov s trendi gripe. Čeprav je imel pristop pomanjkljivosti, je opozoril na možnosti (in izzive) napovedovanja zdravja na podlagi podatkov.

 * [UPS Routing Predictions](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - pojasnjuje, kako UPS uporablja podatkovno znanost in strojno učenje za napovedovanje optimalnih poti za dostavo, pri čemer upošteva vremenske razmere, prometne vzorce, roke dostave in druge dejavnike.

 * [Vizualizacija poti taksijev v NYC](http://chriswhong.github.io/nyctaxi/) - podatki, zbrani z uporabo [zakonov o svobodi informacij](https://chriswhong.com/open-data/foil_nyc_taxi/), so pomagali vizualizirati dan v življenju taksijev v NYC, kar nam omogoča razumevanje, kako se premikajo po mestu, koliko zaslužijo in kako dolgo trajajo vožnje v 24-urnem obdobju.

 * [Uber Data Science Workbench](https://eng.uber.com/dsw/) - uporablja podatke (o lokacijah prevzemov in odložitev, trajanju voženj, prednostnih poteh itd.), zbrane iz milijonov Uber voženj *dnevno*, za izdelavo orodja za analizo podatkov, ki pomaga pri določanju cen, varnosti, odkrivanju goljufij in navigacijskih odločitvah.

 * [Športna analitika](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - osredotoča se na _napovedno analitiko_ (analiza ekip in igralcev - pomislite na [Moneyball](https://datasciencedegree.wisconsin.edu/blog/moneyball-proves-importance-big-data-big-ideas/) - ter upravljanje navijačev) in _vizualizacijo podatkov_ (nadzorne plošče ekip in navijačev, igre itd.) z aplikacijami, kot so iskanje talentov, športne stave in upravljanje zalog/objektov.

 * [Podatkovna znanost v bančništvu](https://data-flair.training/blogs/data-science-in-banking/) - poudarja vrednost podatkovne znanosti v finančni industriji z aplikacijami, ki segajo od modeliranja tveganj in odkrivanja goljufij do segmentacije strank, napovedovanja v realnem času in priporočilnih sistemov. Napovedna analitika prav tako poganja ključne ukrepe, kot so [kreditne ocene](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit).

 * [Podatkovna znanost v zdravstvu](https://data-flair.training/blogs/data-science-in-healthcare/) - poudarja aplikacije, kot so medicinsko slikanje (npr. MRI, rentgen, CT-skeniranje), genomika (sekvenciranje DNK), razvoj zdravil (ocena tveganja, napoved uspeha), napovedna analitika (oskrba pacientov in logistika oskrbe), sledenje boleznim in preprečevanje itd.

![Aplikacije podatkovne znanosti v resničnem svetu](../../../../6-Data-Science-In-Wild/20-Real-World-Examples/images/data-science-applications.png) Avtor slike: [Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

Slika prikazuje druge domene in primere uporabe tehnik podatkovne znanosti. Želite raziskati druge aplikacije? Oglejte si razdelek [Pregled in samostojno učenje](../../../../6-Data-Science-In-Wild/20-Real-World-Examples) spodaj.

## Podatkovna znanost + Raziskave

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Research.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Podatkovna znanost in raziskave - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

Medtem ko se resnične aplikacije pogosto osredotočajo na industrijske primere uporabe v velikem obsegu, so _raziskovalne_ aplikacije in projekti koristni z dveh vidikov:

* _priložnosti za inovacije_ - raziskovanje hitrega prototipiranja naprednih konceptov in testiranje uporabniških izkušenj za aplikacije naslednje generacije.
* _izzivi pri implementaciji_ - preučevanje potencialnih škod ali nenamernih posledic tehnologij podatkovne znanosti v resničnih kontekstih.

Za študente lahko ti raziskovalni projekti nudijo priložnosti za učenje in sodelovanje, ki izboljšajo vaše razumevanje teme ter razširijo vašo ozaveščenost in angažiranost z relevantnimi ljudmi ali ekipami, ki delajo na področjih vašega interesa. Kako torej izgledajo raziskovalni projekti in kako lahko vplivajo?

Poglejmo en primer - [MIT Gender Shades Study](http://gendershades.org/overview.html) Joy Buolamwini (MIT Media Labs) z [pomembnim raziskovalnim člankom](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf), ki ga je soavtorila s Timnit Gebru (takrat pri Microsoft Research), osredotočenim na:

 * **Kaj:** Cilj raziskovalnega projekta je bil _oceniti pristranskost v algoritmih in podatkovnih zbirkah za avtomatizirano analizo obrazov_ glede na spol in tip kože.
 * **Zakaj:** Analiza obrazov se uporablja na področjih, kot so kazenski pregon, varnost na letališčih, sistemi za zaposlovanje in več - konteksti, kjer lahko netočne klasifikacije (npr. zaradi pristranskosti) povzročijo potencialne ekonomske in socialne škode prizadetim posameznikom ali skupinam. Razumevanje (in odpravljanje ali zmanjševanje) pristranskosti je ključno za pravičnost pri uporabi.
 * **Kako:** Raziskovalci so ugotovili, da obstoječi referenčni podatki večinoma uporabljajo svetlopolte subjekte, in ustvarili novo podatkovno zbirko (1000+ slik), ki je bila _bolj uravnotežena_ glede na spol in tip kože. Podatkovna zbirka je bila uporabljena za oceno natančnosti treh produktov za klasifikacijo spola (Microsoft, IBM & Face++).

Rezultati so pokazali, da je bila skupna natančnost klasifikacije dobra, vendar je bila opazna razlika v stopnjah napak med različnimi podskupinami - z **napačno klasifikacijo spola** pogostejšo pri ženskah ali osebah s temnejšo poltjo, kar kaže na pristranskost.

**Ključni rezultati:** Povečana ozaveščenost, da podatkovna znanost potrebuje bolj _reprezentativne podatkovne zbirke_ (uravnotežene podskupine) in bolj _vključujoče ekipe_ (raznolika ozadja), da se pristranskosti v rešitvah umetne inteligence prepoznajo in odpravijo ali zmanjšajo že zgodaj. Takšni raziskovalni napori so ključni tudi za številne organizacije pri določanju načel in praks za _odgovorno umetno inteligenco_, da izboljšajo pravičnost svojih produktov in procesov umetne inteligence.

**Želite izvedeti več o relevantnih raziskovalnih prizadevanjih v Microsoftu?**

* Oglejte si [Microsoft Research Projects](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project) na področju umetne inteligence.
* Raziščite študentske projekte iz [Microsoft Research Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/).
* Oglejte si projekt [Fairlearn](https://fairlearn.org/) in pobude [Odgovorna umetna inteligenca](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6).

## Podatkovna znanost + Humanistika

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Podatkovna znanost in digitalna humanistika - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

Digitalna humanistika [je opredeljena](https://digitalhumanities.stanford.edu/about-dh-stanford) kot "zbirka praks in pristopov, ki združujejo računalniške metode s humanističnim raziskovanjem". [Stanfordovi projekti](https://digitalhumanities.stanford.edu/projects), kot sta _"rebooting history"_ in _"poetic thinking"_, ponazarjajo povezavo med [digitalno humanistiko in podatkovno znanostjo](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science) - poudarjajo tehnike, kot so analiza omrežij, vizualizacija informacij, prostorska in besedilna analiza, ki nam lahko pomagajo ponovno preučiti zgodovinske in literarne podatkovne zbirke ter pridobiti nove vpoglede in perspektive.

*Želite raziskati in razširiti projekt na tem področju?*

Oglejte si ["Emily Dickinson and the Meter of Mood"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671) - odličen primer [Jen Looper](https://twitter.com/jenlooper), ki sprašuje, kako lahko uporabimo podatkovno znanost za ponovno preučitev znane poezije in ponovno ovrednotenje njenega pomena ter prispevkov avtorice v novih kontekstih. Na primer, _ali lahko napovemo letni čas, v katerem je bila pesem napisana, z analizo njenega tona ali sentimenta_ - in kaj nam to pove o avtorjevem duševnem stanju v relevantnem obdobju?

Da bi odgovorili na to vprašanje, sledimo korakom življenjskega cikla podatkovne znanosti:
 * [`Pridobivanje podatkov`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#acquiring-the-dataset) - za zbiranje relevantne podatkovne zbirke za analizo. Možnosti vključujejo uporabo API-ja (npr. [Poetry DB API](https://poetrydb.org/index.html)) ali strganje spletnih strani (npr. [Project Gutenberg](https://www.gutenberg.org/files/12242/12242-h/12242-h.htm)) z orodji, kot je [Scrapy](https://scrapy.org/).
 * [`Čiščenje podatkov`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#clean-the-data) - pojasnjuje, kako je mogoče besedilo formatirati, očistiti in poenostaviti z osnovnimi orodji, kot sta Visual Studio Code in Microsoft Excel.
 * [`Analiza podatkov`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#working-with-the-data-in-a-notebook) - pojasnjuje, kako lahko zdaj uvozimo podatkovno zbirko v "zvezke" za analizo z uporabo Pythonovih paketov (kot so pandas, numpy in matplotlib) za organizacijo in vizualizacijo podatkov.
 * [`Analiza sentimenta`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#sentiment-analysis-using-cognitive-services) - pojasnjuje, kako lahko vključimo storitve v oblaku, kot je Text Analytics, z uporabo orodij z malo kode, kot je [Power Automate](https://flow.microsoft.com/en-us/) za avtomatizirane delovne procese obdelave podatkov.

Z uporabo tega delovnega procesa lahko raziskujemo sezonske vplive na sentiment pesmi in si oblikujemo lastne perspektive o avtorici. Preizkusite sami - nato razširite zvezek, da postavite druga vprašanja ali vizualizirate podatke na nove načine!

> Nekatera orodja iz [Digital Humanities toolkit](https://github.com/Digital-Humanities-Toolkit) lahko uporabite za raziskovanje teh vprašanj.

## Podatkovna znanost + Trajnost

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Sustainability.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Podatkovna znanost in trajnost - _Sketchnote by [@nitya](https://twitter.com/nitya)_              |

[Agenda 2030 za trajnostni razvoj](https://sdgs.un.org/2030agenda) - sprejeta s strani vseh članic Združenih narodov leta 2015 - opredeljuje 17 ciljev, vključno s tistimi, ki se osredotočajo na **zaščito planeta** pred degradacijo in vplivi podnebnih sprememb. Pobuda [Microsoft Sustainability](https://www.microsoft.com/en-us/sustainability) podpira te cilje z raziskovanjem načinov, kako lahko tehnološke rešitve podpirajo in gradijo bolj trajnostno prihodnost s [fokusom na 4 cilje](https://dev.to/azure/a-visual-guide-to-sustainable-software-engineering-53hh) - biti ogljično negativni, vodno pozitivni, brez odpadkov in biotsko raznoliki do leta 2030.

Reševanje teh izzivov na skalabilen in pravočasen način zahteva razmišljanje na ravni oblaka - in obsežne podatke. Pobuda [Planetary Computer](https://planetarycomputer.microsoft.com/) ponuja 4 komponente, ki pomagajo podatkovnim znanstvenikom in razvijalcem pri tem prizadevanju:

 * [Katalog podatkov](https://planetarycomputer.microsoft.com/catalog) - s petabajti podatkov o zemeljskih sistemih (brezplačno in gostovano na Azure).
 * [Planetary API](https://planetarycomputer.microsoft.com/docs/reference/stac/) - za pomoč uporabnikom pri iskanju relevantnih podatkov skozi prostor in čas.
 * [Hub](https://planetarycomputer.microsoft.com/docs/overview/environment/) - upravljano okolje za znanstvenike za obdelavo obsežnih geozemeljskih podatkovnih zbirk.
 * [Aplikacije](https://planetarycomputer.microsoft.com/applications) - prikazujejo primere uporabe in orodja za vpoglede v trajnost.
**Projekt Planetary Computer je trenutno v predogledu (od septembra 2021)** - tukaj je, kako lahko začnete prispevati k trajnostnim rešitvam z uporabo podatkovne znanosti.

* [Zahtevajte dostop](https://planetarycomputer.microsoft.com/account/request), da začnete raziskovati in se povezovati z vrstniki.
* [Raziskujte dokumentacijo](https://planetarycomputer.microsoft.com/docs/overview/about), da razumete podprte podatkovne zbirke in API-je.
* Raziskujte aplikacije, kot je [Ecosystem Monitoring](https://analytics-lab.org/ecosystemmonitoring/), za navdih pri idejah za aplikacije.

Razmislite, kako lahko uporabite vizualizacijo podatkov za razkrivanje ali poudarjanje pomembnih vpogledov na področjih, kot sta podnebne spremembe in krčenje gozdov. Ali pa razmislite, kako lahko vpogledi služijo za ustvarjanje novih uporabniških izkušenj, ki spodbujajo vedenjske spremembe za bolj trajnostno življenje.

## Podatkovna znanost + študenti

Govorili smo o aplikacijah v industriji in raziskavah ter raziskovali primere uporabe podatkovne znanosti v digitalni humanistiki in trajnosti. Kako pa lahko kot začetniki v podatkovni znanosti gradite svoje veščine in delite svoje znanje?

Tukaj je nekaj primerov študentskih projektov iz podatkovne znanosti, ki vas lahko navdihnejo.

* [Poletna šola podatkovne znanosti MSR](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/#!projects) z GitHub [projekti](https://github.com/msr-ds3), ki raziskujejo teme, kot so:
   - [Rasna pristranskost pri uporabi sile s strani policije](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2019-replicating-an-empirical-analysis-of-racial-differences-in-police-use-of-force/) | [Github](https://github.com/msr-ds3/stop-question-frisk)
   - [Zanesljivost sistema podzemne železnice v New Yorku](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2018-exploring-the-reliability-of-the-nyc-subway-system/) | [Github](https://github.com/msr-ds3/nyctransit)
* [Digitalizacija materialne kulture: Raziskovanje socio-ekonomskih razporeditev v Sirkapu](https://claremont.maps.arcgis.com/apps/Cascade/index.html?appid=bdf2aef0f45a4674ba41cd373fa23afc) - od [Ornella Altunyan](https://twitter.com/ornelladotcom) in ekipe na Claremontu, z uporabo [ArcGIS StoryMaps](https://storymaps.arcgis.com/).

## 🚀 Izziv

Poiščite članke, ki priporočajo projekte podatkovne znanosti, primerni za začetnike - kot [teh 50 tematskih področij](https://www.upgrad.com/blog/data-science-project-ideas-topics-beginners/) ali [teh 21 idej za projekte](https://www.intellspot.com/data-science-project-ideas) ali [teh 16 projektov z izvorno kodo](https://data-flair.training/blogs/data-science-project-ideas/), ki jih lahko razstavite in preoblikujete. Ne pozabite pisati blogov o svojih učnih poteh in deliti svoje vpoglede z nami.

## Kviz po predavanju

## [Kviz po predavanju](https://ff-quizzes.netlify.app/en/ds/quiz/39)

## Pregled in samostojno učenje

Želite raziskati več primerov uporabe? Tukaj je nekaj relevantnih člankov:
* [17 aplikacij in primerov uporabe podatkovne znanosti](https://builtin.com/data-science/data-science-applications-examples) - julij 2021
* [11 osupljivih aplikacij podatkovne znanosti v resničnem svetu](https://myblindbird.com/data-science-applications-real-world/) - maj 2021
* [Podatkovna znanost v resničnem svetu](https://towardsdatascience.com/data-science-in-the-real-world/home) - zbirka člankov
* Podatkovna znanost v: [izobraževanju](https://data-flair.training/blogs/data-science-in-education/), [kmetijstvu](https://data-flair.training/blogs/data-science-in-agriculture/), [financah](https://data-flair.training/blogs/data-science-in-finance/), [filmih](https://data-flair.training/blogs/data-science-at-movies/) in več.

## Naloga

[Raziskujte podatkovno zbirko Planetary Computer](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.