<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "06bac7959b46b6e8aedcae014278c476",
  "translation_date": "2025-09-05T18:17:36+00:00",
  "source_file": "6-Data-Science-In-Wild/20-Real-World-Examples/README.md",
  "language_code": "sk"
}
-->
# Data Science v reálnom svete

| ![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-RealWorld.png) |
| :--------------------------------------------------------------------------------------------------------------: |
|               Data Science v reálnom svete - _Sketchnote od [@nitya](https://twitter.com/nitya)_               |

Sme takmer na konci tejto vzdelávacej cesty!

Začali sme definíciami dátovej vedy a etiky, preskúmali rôzne nástroje a techniky na analýzu a vizualizáciu dát, prešli životný cyklus dátovej vedy a pozreli sa na škálovanie a automatizáciu pracovných postupov dátovej vedy pomocou cloudových služieb. Pravdepodobne sa pýtate: _"Ako presne môžem všetky tieto poznatky aplikovať v reálnom svete?"_

V tejto lekcii preskúmame reálne aplikácie dátovej vedy v rôznych odvetviach a ponoríme sa do konkrétnych príkladov v oblasti výskumu, digitálnych humanitných vied a udržateľnosti. Pozrieme sa na príležitosti pre študentské projekty a zakončíme užitočnými zdrojmi, ktoré vám pomôžu pokračovať vo vašej vzdelávacej ceste!

## Kvíz pred prednáškou

## [Kvíz pred prednáškou](https://ff-quizzes.netlify.app/en/ds/quiz/38)

## Dátová veda + Priemysel

Vďaka demokratizácii AI je pre vývojárov teraz jednoduchšie navrhovať a integrovať rozhodovanie poháňané AI a poznatky založené na dátach do používateľských skúseností a vývojových pracovných postupov. Tu je niekoľko príkladov, ako sa dátová veda "aplikuje" v reálnych aplikáciách naprieč priemyslom:

 * [Google Flu Trends](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) využíval dátovú vedu na koreláciu vyhľadávacích termínov s trendmi chrípky. Hoci prístup mal nedostatky, zvýšil povedomie o možnostiach (a výzvach) predpovedí v zdravotníctve založených na dátach.

 * [Predikcie trás UPS](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - vysvetľuje, ako UPS využíva dátovú vedu a strojové učenie na predpovedanie optimálnych trás pre doručovanie, pričom zohľadňuje poveternostné podmienky, dopravné vzory, termíny doručenia a ďalšie faktory.

 * [Vizualizácia trás taxíkov v NYC](http://chriswhong.github.io/nyctaxi/) - dáta získané pomocou [zákonov o slobode informácií](https://chriswhong.com/open-data/foil_nyc_taxi/) pomohli vizualizovať deň v živote taxíkov v NYC, čo nám umožňuje pochopiť, ako sa pohybujú po rušnom meste, koľko zarábajú a aké sú trvania jázd počas každého 24-hodinového obdobia.

 * [Pracovná plocha dátovej vedy Uber](https://eng.uber.com/dsw/) - využíva dáta (o miestach vyzdvihnutia a vysadenia, trvaní jázd, preferovaných trasách atď.) získané z miliónov jázd Uber *denne* na vytvorenie nástroja na analýzu dát, ktorý pomáha s cenotvorbou, bezpečnosťou, detekciou podvodov a navigačnými rozhodnutiami.

 * [Analytika v športe](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - zameriava sa na _prediktívnu analytiku_ (analýza tímov a hráčov - napr. [Moneyball](https://datasciencedegree.wisconsin.edu/blog/moneyball-proves-importance-big-data-big-ideas/) - a manažment fanúšikov) a _vizualizáciu dát_ (dashboardy tímov a fanúšikov, hry atď.) s aplikáciami ako scouting talentov, športové stávkovanie a manažment inventára/miest.

 * [Dátová veda v bankovníctve](https://data-flair.training/blogs/data-science-in-banking/) - zdôrazňuje hodnotu dátovej vedy vo finančnom priemysle s aplikáciami od modelovania rizík a detekcie podvodov, cez segmentáciu zákazníkov, až po predikcie v reálnom čase a odporúčacie systémy. Prediktívna analytika tiež poháňa kritické opatrenia ako [kreditné skóre](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit).

 * [Dátová veda v zdravotníctve](https://data-flair.training/blogs/data-science-in-healthcare/) - zdôrazňuje aplikácie ako medicínske zobrazovanie (napr. MRI, röntgen, CT-sken), genomika (sekvenovanie DNA), vývoj liekov (hodnotenie rizík, predikcia úspechu), prediktívna analytika (starostlivosť o pacientov a logistika zásob), sledovanie a prevencia chorôb atď.

![Aplikácie dátovej vedy v reálnom svete](../../../../6-Data-Science-In-Wild/20-Real-World-Examples/images/data-science-applications.png) Zdroj obrázku: [Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

Obrázok ukazuje ďalšie oblasti a príklady aplikácie techník dátovej vedy. Chcete preskúmať ďalšie aplikácie? Pozrite si sekciu [Recenzia a samostatné štúdium](../../../../6-Data-Science-In-Wild/20-Real-World-Examples) nižšie.

## Dátová veda + Výskum

| ![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Research.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Dátová veda & Výskum - _Sketchnote od [@nitya](https://twitter.com/nitya)_              |

Zatiaľ čo aplikácie v reálnom svete sa často zameriavajú na priemyselné prípady použitia vo veľkom meradle, _výskumné_ aplikácie a projekty môžu byť užitočné z dvoch perspektív:

* _príležitosti na inovácie_ - skúmanie rýchleho prototypovania pokročilých konceptov a testovanie používateľských skúseností pre aplikácie budúcej generácie.
* _výzvy pri nasadení_ - skúmanie potenciálnych škôd alebo neúmyselných dôsledkov technológií dátovej vedy v reálnych kontextoch.

Pre študentov môžu tieto výskumné projekty poskytnúť príležitosti na učenie a spoluprácu, ktoré zlepšia vaše pochopenie témy a rozšíria vaše povedomie a zapojenie sa s relevantnými ľuďmi alebo tímami pracujúcimi v oblastiach záujmu. Ako teda vyzerajú výskumné projekty a aký môžu mať dopad?

Pozrime sa na jeden príklad - [MIT Gender Shades Study](http://gendershades.org/overview.html) od Joy Buolamwini (MIT Media Labs) s [významným výskumným článkom](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf) spoluautorky Timnit Gebru (vtedy v Microsoft Research), ktorý sa zameriaval na:

 * **Čo:** Cieľom výskumného projektu bolo _vyhodnotiť predsudky prítomné v algoritmoch a dátových súboroch automatizovanej analýzy tváre_ na základe pohlavia a typu pokožky.
 * **Prečo:** Analýza tváre sa používa v oblastiach ako presadzovanie práva, bezpečnosť na letiskách, systémy na prijímanie zamestnancov a ďalšie - kontexty, kde nepresné klasifikácie (napr. kvôli predsudkom) môžu spôsobiť potenciálne ekonomické a sociálne škody dotknutým jednotlivcom alebo skupinám. Pochopenie (a eliminácia alebo zmiernenie) predsudkov je kľúčom k spravodlivosti pri používaní.
 * **Ako:** Výskumníci si uvedomili, že existujúce benchmarky používali prevažne subjekty so svetlejšou pokožkou, a vytvorili nový dátový súbor (1000+ obrázkov), ktorý bol _vyváženejší_ podľa pohlavia a typu pokožky. Tento dátový súbor bol použitý na vyhodnotenie presnosti troch produktov na klasifikáciu pohlavia (od Microsoftu, IBM a Face++).

Výsledky ukázali, že hoci celková presnosť klasifikácie bola dobrá, existoval výrazný rozdiel v chybovosti medzi rôznymi podskupinami - s **nesprávnym určením pohlavia** častejším u žien alebo osôb s tmavšou pokožkou, čo naznačuje predsudky.

**Kľúčové výsledky:** Zvýšenie povedomia, že dátová veda potrebuje viac _reprezentatívnych dátových súborov_ (vyvážené podskupiny) a viac _inkluzívnych tímov_ (rôznorodé pozadie), aby sa takéto predsudky rozpoznali a eliminovali alebo zmiernili skôr v AI riešeniach. Výskumné úsilie ako toto je tiež zásadné pre mnohé organizácie pri definovaní princípov a postupov pre _zodpovednú AI_, aby sa zlepšila spravodlivosť ich AI produktov a procesov.

**Chcete sa dozvedieť o relevantných výskumných aktivitách v Microsoft?**

* Pozrite si [Microsoft Research Projects](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project) v oblasti umelej inteligencie.
* Preskúmajte študentské projekty z [Microsoft Research Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/).
* Pozrite si projekt [Fairlearn](https://fairlearn.org/) a iniciatívy [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6).

## Dátová veda + Humanitné vedy

| ![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Dátová veda & Digitálne humanitné vedy - _Sketchnote od [@nitya](https://twitter.com/nitya)_              |

Digitálne humanitné vedy [boli definované](https://digitalhumanities.stanford.edu/about-dh-stanford) ako "súbor praktík a prístupov kombinujúcich výpočtové metódy s humanistickým skúmaním". [Projekty Stanfordu](https://digitalhumanities.stanford.edu/projects) ako _"rebooting history"_ a _"poetic thinking"_ ilustrujú prepojenie medzi [digitálnymi humanitnými vedami a dátovou vedou](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science) - zdôrazňujúc techniky ako analýza sietí, vizualizácia informácií, priestorová a textová analýza, ktoré nám môžu pomôcť znovu preskúmať historické a literárne dátové súbory a odvodiť nové poznatky a perspektívy.

*Chcete preskúmať a rozšíriť projekt v tejto oblasti?*

Pozrite si ["Emily Dickinson and the Meter of Mood"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671) - skvelý príklad od [Jen Looper](https://twitter.com/jenlooper), ktorý sa pýta, ako môžeme pomocou dátovej vedy znovu preskúmať známe básne a prehodnotiť ich význam a prínos ich autora v nových kontextoch. Napríklad, _môžeme predpovedať ročné obdobie, v ktorom bola báseň napísaná, analýzou jej tónu alebo sentimentu_ - a čo nám to hovorí o stave mysle autora počas relevantného obdobia?

Na zodpovedanie tejto otázky postupujeme podľa krokov životného cyklu dátovej vedy:
 * [`Získavanie dát`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#acquiring-the-dataset) - na zhromaždenie relevantného dátového súboru na analýzu. Možnosti zahŕňajú použitie API (napr. [Poetry DB API](https://poetrydb.org/index.html)) alebo scraping webových stránok (napr. [Project Gutenberg](https://www.gutenberg.org/files/12242/12242-h/12242-h.htm)) pomocou nástrojov ako [Scrapy](https://scrapy.org/).
 * [`Čistenie dát`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#clean-the-data) - vysvetľuje, ako môže byť text formátovaný, sanitovaný a zjednodušený pomocou základných nástrojov ako Visual Studio Code a Microsoft Excel.
 * [`Analýza dát`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#working-with-the-data-in-a-notebook) - vysvetľuje, ako môžeme teraz importovať dátový súbor do "Notebooks" na analýzu pomocou Python balíkov (ako pandas, numpy a matplotlib) na organizáciu a vizualizáciu dát.
 * [`Analýza sentimentu`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#sentiment-analysis-using-cognitive-services) - vysvetľuje, ako môžeme integrovať cloudové služby ako Text Analytics, pomocou nástrojov s nízkym kódom ako [Power Automate](https://flow.microsoft.com/en-us/) na automatizované pracovné postupy spracovania dát.

Pomocou tohto pracovného postupu môžeme preskúmať sezónne vplyvy na sentiment básní a pomôcť nám vytvoriť vlastné perspektívy o autorovi. Vyskúšajte to sami - potom rozšírte notebook, aby ste položili ďalšie otázky alebo vizualizovali dáta novými spôsobmi!

> Môžete použiť niektoré nástroje z [Digital Humanities toolkit](https://github.com/Digital-Humanities-Toolkit) na preskúmanie týchto otázok.

## Dátová veda + Udržateľnosť

| ![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Sustainability.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Dátová veda & Udržateľnosť - _Sketchnote od [@nitya](https://twitter.com/nitya)_              |

[Agenda 2030 pre udržateľný rozvoj](https://sdgs.un.org/2030agenda) - prijatá všetkými členmi OSN v roku 2015 - identifikuje 17 cieľov vrátane tých, ktoré sa zameriavajú na **ochranu planéty** pred degradáciou a dopadmi klimatických zmien. Iniciatíva [Microsoft Sustainability](https://www.microsoft.com/en-us/sustainability) podporuje tieto ciele skúmaním spôsobov, ako technologické riešenia môžu podporovať a budovať udržateľnejšiu budúcnosť so [zameraním na 4 ciele](https://dev.to/azure/a-visual-guide-to-sustainable-software-engineering-53hh) - byť uhlíkovo negatívny, vodne pozitívny, bez odpadu a biodiverzný do roku 2030.

Riešenie týchto výziev v škálovateľnom a včasnom meradle si vyžaduje cloudové myslenie - a veľké množstvo dát. Iniciatíva [Planetary Computer](https://planetarycomputer.microsoft.com/) poskytuje 4 komponenty, ktoré pomáhajú dátovým vedcom a vývojárom v tomto úsilí:

 * [Katalóg dát](https://planetarycomputer.microsoft.com/catalog) - s petabajtmi dát o systémoch Zeme (bezplatné a hostované na Azure).
 * [Planetárne API](https://planetarycomputer.microsoft.com/docs/reference/stac/) - na pomoc používateľom pri hľadaní relevantných dát naprieč priestorom a časom.
 * [Hub](https://planetarycomputer.microsoft.com/docs/overview/environment/) - spr
**Projekt Planetary Computer je momentálne v náhľade (k septembru 2021)** - tu je návod, ako začať prispievať k riešeniam udržateľnosti pomocou dátovej vedy.

* [Požiadajte o prístup](https://planetarycomputer.microsoft.com/account/request) na začatie prieskumu a spojenie sa s kolegami.
* [Preskúmajte dokumentáciu](https://planetarycomputer.microsoft.com/docs/overview/about) na pochopenie podporovaných datasetov a API.
* Preskúmajte aplikácie ako [Monitorovanie ekosystémov](https://analytics-lab.org/ecosystemmonitoring/) pre inšpiráciu na nápady aplikácií.

Premýšľajte o tom, ako môžete použiť vizualizáciu dát na odhalenie alebo zvýraznenie relevantných poznatkov v oblastiach ako klimatické zmeny a odlesňovanie. Alebo premýšľajte o tom, ako môžu byť poznatky použité na vytvorenie nových užívateľských zážitkov, ktoré motivujú k zmenám správania pre udržateľnejší život.

## Dátová veda + Študenti

Hovorili sme o aplikáciách v reálnom svete v priemysle a výskume a preskúmali sme príklady aplikácií dátovej vedy v digitálnych humanitných vedách a udržateľnosti. Tak ako si môžete rozvíjať svoje zručnosti a zdieľať svoje odborné znalosti ako začiatočníci v dátovej vede?

Tu sú niektoré príklady študentských projektov z oblasti dátovej vedy, ktoré vás môžu inšpirovať.

* [Letná škola dátovej vedy MSR](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/#!projects) s GitHub [projektmi](https://github.com/msr-ds3), ktoré skúmajú témy ako:
   - [Rasová zaujatosť v používaní sily políciou](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2019-replicating-an-empirical-analysis-of-racial-differences-in-police-use-of-force/) | [Github](https://github.com/msr-ds3/stop-question-frisk)
   - [Spoľahlivosť systému metra v NYC](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2018-exploring-the-reliability-of-the-nyc-subway-system/) | [Github](https://github.com/msr-ds3/nyctransit)
* [Digitalizácia materiálnej kultúry: Skúmanie socio-ekonomických rozložení v Sirkape](https://claremont.maps.arcgis.com/apps/Cascade/index.html?appid=bdf2aef0f45a4674ba41cd373fa23afc) - od [Ornella Altunyan](https://twitter.com/ornelladotcom) a tímu z Claremont, pomocou [ArcGIS StoryMaps](https://storymaps.arcgis.com/).

## 🚀 Výzva

Vyhľadajte články, ktoré odporúčajú projekty dátovej vedy vhodné pre začiatočníkov - ako [týchto 50 tém](https://www.upgrad.com/blog/data-science-project-ideas-topics-beginners/) alebo [týchto 21 nápadov na projekty](https://www.intellspot.com/data-science-project-ideas) alebo [týchto 16 projektov so zdrojovým kódom](https://data-flair.training/blogs/data-science-project-ideas/), ktoré môžete rozobrať a upraviť. Nezabudnite blogovať o svojich učebných cestách a zdieľať svoje poznatky s nami všetkými.

## Kvíz po prednáške

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ds/quiz/39)

## Prehľad & Samoštúdium

Chcete preskúmať viac prípadov použitia? Tu je niekoľko relevantných článkov:
* [17 aplikácií a príkladov dátovej vedy](https://builtin.com/data-science/data-science-applications-examples) - júl 2021
* [11 úžasných aplikácií dátovej vedy v reálnom svete](https://myblindbird.com/data-science-applications-real-world/) - máj 2021
* [Dátová veda v reálnom svete](https://towardsdatascience.com/data-science-in-the-real-world/home) - kolekcia článkov
* Dátová veda v: [Vzdelávaní](https://data-flair.training/blogs/data-science-in-education/), [Poľnohospodárstve](https://data-flair.training/blogs/data-science-in-agriculture/), [Financiách](https://data-flair.training/blogs/data-science-in-finance/), [Filmoch](https://data-flair.training/blogs/data-science-at-movies/) a ďalších.

## Zadanie

[Preskúmajte dataset Planetary Computer](assignment.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.