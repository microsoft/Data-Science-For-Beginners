<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0f67a4139454816631526779a456b734",
  "translation_date": "2025-09-06T18:41:52+00:00",
  "source_file": "6-Data-Science-In-Wild/20-Real-World-Examples/README.md",
  "language_code": "cs"
}
-->
# Data Science v reálném světě

| ![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-RealWorld.png) |
| :--------------------------------------------------------------------------------------------------------------: |
|               Data Science v reálném světě - _Sketchnote od [@nitya](https://twitter.com/nitya)_               |

Jsme téměř na konci této vzdělávací cesty!

Začali jsme definicemi datové vědy a etiky, prozkoumali různé nástroje a techniky pro analýzu a vizualizaci dat, přezkoumali životní cyklus datové vědy a podívali se na škálování a automatizaci pracovních postupů datové vědy pomocí cloudových služeb. Možná si teď říkáte: _"Jak přesně mohu všechny tyto znalosti aplikovat v reálném světě?"_

V této lekci prozkoumáme reálné aplikace datové vědy napříč průmyslem a ponoříme se do konkrétních příkladů v oblasti výzkumu, digitálních humanitních věd a udržitelnosti. Podíváme se na příležitosti studentských projektů a zakončíme užitečnými zdroji, které vám pomohou pokračovat ve vaší vzdělávací cestě!

## Kvíz před přednáškou

## [Kvíz před přednáškou](https://ff-quizzes.netlify.app/en/ds/quiz/38)

## Data Science + Průmysl

Díky demokratizaci AI je pro vývojáře nyní snazší navrhovat a integrovat rozhodování řízené AI a poznatky založené na datech do uživatelských zkušeností a vývojových pracovních postupů. Zde je několik příkladů, jak je datová věda "aplikována" na reálné aplikace napříč průmyslem:

 * [Google Flu Trends](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) využíval datovou vědu k propojení vyhledávacích termínů s trendy chřipky. Přestože přístup měl své nedostatky, zvýšil povědomí o možnostech (a výzvách) predikcí zdravotní péče založených na datech.

 * [Predikce tras UPS](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - vysvětluje, jak UPS využívá datovou vědu a strojové učení k predikci optimálních tras pro doručování, přičemž bere v úvahu povětrnostní podmínky, dopravní situaci, termíny doručení a další faktory.

 * [Vizualizace tras taxíků v NYC](http://chriswhong.github.io/nyctaxi/) - data získaná pomocí [zákonů o svobodném přístupu k informacím](https://chriswhong.com/open-data/foil_nyc_taxi/) pomohla vizualizovat jeden den v životě taxíků v NYC, což nám umožňuje pochopit, jak se pohybují po rušném městě, kolik vydělávají a jak dlouho trvají jejich cesty během každého 24hodinového období.

 * [Uber Data Science Workbench](https://eng.uber.com/dsw/) - využívá data (o místech vyzvednutí a vysazení, délce cesty, preferovaných trasách atd.) získaná z milionů denních jízd Uberu k vytvoření analytického nástroje, který pomáhá s cenotvorbou, bezpečností, detekcí podvodů a navigačními rozhodnutími.

 * [Analytika ve sportu](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - zaměřuje se na _prediktivní analytiku_ (analýza týmů a hráčů - například [Moneyball](https://datasciencedegree.wisconsin.edu/blog/moneyball-proves-importance-big-data-big-ideas/) - a řízení fanoušků) a _vizualizaci dat_ (dashboardy týmů a fanoušků, hry atd.) s aplikacemi jako skauting talentů, sportovní sázení a řízení inventáře/areálu.

 * [Datová věda v bankovnictví](https://data-flair.training/blogs/data-science-in-banking/) - zdůrazňuje hodnotu datové vědy ve finančním průmyslu s aplikacemi od modelování rizik a detekce podvodů po segmentaci zákazníků, predikce v reálném čase a doporučovací systémy. Prediktivní analytika také pohání klíčová opatření jako [kreditní skóre](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit).

 * [Datová věda ve zdravotnictví](https://data-flair.training/blogs/data-science-in-healthcare/) - zdůrazňuje aplikace jako lékařské zobrazování (např. MRI, rentgen, CT-sken), genomiku (sekvenování DNA), vývoj léků (hodnocení rizik, predikce úspěchu), prediktivní analytiku (péče o pacienty a logistika zásob), sledování a prevence nemocí atd.

![Aplikace datové vědy v reálném světě](../../../../translated_images/cs/data-science-applications.4e5019cd8790ebac2277ff5f08af386f8727cac5d30f77727c7090677e6adb9c.png) Zdroj obrázku: [Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

Obrázek ukazuje další oblasti a příklady aplikace technik datové vědy. Chcete prozkoumat další aplikace? Podívejte se na sekci [Review & Self Study](../../../../6-Data-Science-In-Wild/20-Real-World-Examples) níže.

## Data Science + Výzkum

| ![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Research.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Data Science & Výzkum - _Sketchnote od [@nitya](https://twitter.com/nitya)_              |

Zatímco aplikace v reálném světě se často zaměřují na průmyslové případy použití ve velkém měřítku, _výzkumné_ aplikace a projekty mohou být užitečné ze dvou perspektiv:

* _příležitosti k inovacím_ - zkoumání rychlého prototypování pokročilých konceptů a testování uživatelských zkušeností pro aplikace nové generace.
* _výzvy při nasazení_ - zkoumání potenciálních škod nebo nechtěných důsledků technologií datové vědy v reálných kontextech.

Pro studenty mohou tyto výzkumné projekty poskytnout jak příležitosti k učení, tak ke spolupráci, což může zlepšit jejich porozumění tématu a rozšířit jejich povědomí a zapojení s relevantními lidmi nebo týmy pracujícími v oblastech zájmu. Jak tedy výzkumné projekty vypadají a jak mohou mít dopad?

Podívejme se na jeden příklad - [MIT Gender Shades Study](http://gendershades.org/overview.html) od Joy Buolamwini (MIT Media Labs) s [významným výzkumným článkem](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf) spoluautorky Timnit Gebru (tehdy v Microsoft Research), který se zaměřil na:

 * **Co:** Cílem výzkumného projektu bylo _vyhodnotit přítomnost zaujatosti v algoritmech a datových sadách pro automatizovanou analýzu obličeje_ na základě pohlaví a typu pokožky.
 * **Proč:** Analýza obličeje se používá v oblastech jako vymáhání práva, bezpečnost na letištích, systémy náboru a další - kontexty, kde nepřesné klasifikace (např. kvůli zaujatosti) mohou způsobit potenciální ekonomické a sociální škody postiženým jednotlivcům nebo skupinám. Porozumění (a eliminace nebo zmírnění) zaujatosti je klíčem k férovosti při používání.
 * **Jak:** Výzkumníci zjistili, že stávající benchmarky používaly převážně subjekty se světlejší pokožkou, a vytvořili novou datovou sadu (1000+ obrázků), která byla _vyváženější_ podle pohlaví a typu pokožky. Datová sada byla použita k vyhodnocení přesnosti tří produktů pro klasifikaci pohlaví (od Microsoftu, IBM a Face++).

Výsledky ukázaly, že přestože celková přesnost klasifikace byla dobrá, existoval znatelný rozdíl v míře chyb mezi různými podskupinami - s **nesprávným určením pohlaví** častějším u žen nebo osob s tmavší pokožkou, což naznačuje zaujatost.

**Klíčové výsledky:** Zvýšení povědomí o tom, že datová věda potřebuje více _reprezentativních datových sad_ (vyvážené podskupiny) a více _inkluzivních týmů_ (různorodé zázemí), aby bylo možné rozpoznat a eliminovat nebo zmírnit takové zaujatosti dříve v AI řešeních. Výzkumné úsilí jako toto je také klíčové pro mnoho organizací při definování principů a postupů pro _odpovědnou AI_, aby se zlepšila férovost napříč jejich AI produkty a procesy.

**Chcete se dozvědět o relevantních výzkumných snahách v Microsoftu?**

* Podívejte se na [Microsoft Research Projects](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project) v oblasti umělé inteligence.
* Prozkoumejte studentské projekty z [Microsoft Research Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/).
* Podívejte se na projekt [Fairlearn](https://fairlearn.org/) a iniciativy [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6).

## Data Science + Humanitní vědy

| ![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Data Science & Digitální humanitní vědy - _Sketchnote od [@nitya](https://twitter.com/nitya)_              |

Digitální humanitní vědy [byly definovány](https://digitalhumanities.stanford.edu/about-dh-stanford) jako "soubor praktik a přístupů kombinujících výpočetní metody s humanistickým zkoumáním". [Projekty Stanfordu](https://digitalhumanities.stanford.edu/projects) jako _"rebooting history"_ a _"poetic thinking"_ ilustrují propojení mezi [digitálními humanitními vědami a datovou vědou](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science) - zdůrazňují techniky jako analýza sítí, vizualizace informací, prostorová a textová analýza, které nám mohou pomoci znovu prozkoumat historické a literární datové sady a získat nové poznatky a perspektivy.

*Chcete prozkoumat a rozšířit projekt v této oblasti?*

Podívejte se na ["Emily Dickinson and the Meter of Mood"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671) - skvělý příklad od [Jen Looper](https://twitter.com/jenlooper), který se ptá, jak můžeme využít datovou vědu k opětovnému prozkoumání známé poezie a přehodnocení jejího významu a přínosů jejího autora v nových kontextech. Například, _můžeme předpovědět roční období, ve kterém byla báseň napsána, analýzou jejího tónu nebo sentimentu_ - a co nám to říká o stavu mysli autora během daného období?

K zodpovězení této otázky následujeme kroky životního cyklu datové vědy:
 * [`Získávání dat`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#acquiring-the-dataset) - sběr relevantní datové sady pro analýzu. Možnosti zahrnují použití API (např. [Poetry DB API](https://poetrydb.org/index.html)) nebo scraping webových stránek (např. [Project Gutenberg](https://www.gutenberg.org/files/12242/12242-h/12242-h.htm)) pomocí nástrojů jako [Scrapy](https://scrapy.org/).
 * [`Čištění dat`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#clean-the-data) - vysvětluje, jak může být text formátován, očištěn a zjednodušen pomocí základních nástrojů jako Visual Studio Code a Microsoft Excel.
 * [`Analýza dat`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#working-with-the-data-in-a-notebook) - vysvětluje, jak můžeme nyní importovat datovou sadu do "Notebooks" pro analýzu pomocí Python balíčků (jako pandas, numpy a matplotlib) k organizaci a vizualizaci dat.
 * [`Analýza sentimentu`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#sentiment-analysis-using-cognitive-services) - vysvětluje, jak můžeme integrovat cloudové služby jako Text Analytics, pomocí nástrojů s nízkým kódem jako [Power Automate](https://flow.microsoft.com/en-us/) pro automatizované pracovní postupy zpracování dat.

Pomocí tohoto pracovního postupu můžeme prozkoumat sezónní vlivy na sentiment básní a pomoci nám vytvořit vlastní perspektivy na autora. Vyzkoušejte to sami - poté rozšiřte notebook, abyste položili další otázky nebo vizualizovali data novými způsoby!

> Můžete použít některé nástroje z [Digital Humanities toolkit](https://github.com/Digital-Humanities-Toolkit) k prozkoumání těchto možností.

## Data Science + Udržitelnost

| ![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Sustainability.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Data Science & Udržitelnost - _Sketchnote od [@nitya](https://twitter.com/nitya)_              |

[Agenda 2030 pro udržitelný rozvoj](https://sdgs.un.org/2030agenda) - přijatá všemi členy OSN v roce 2015 - identifikuje 17 cílů, včetně těch, které se zaměřují na **ochranu planety** před degradací a dopady změny klimatu. Iniciativa [Microsoft Sustainability](https://www.microsoft.com/en-us/sustainability) podporuje tyto cíle zkoumáním způsobů, jak technologická řešení mohou podporovat a budovat udržitelnější budoucnost se [zaměřením na 4 cíle](https://dev.to/azure/a-visual-guide-to-sustainable-software-engineering-53hh) - být uhlíkově negativní, vodně pozitivní, bez odpadu a biodiverzní do roku 2030.

Řešení těchto výzev ve škálovatelném a včasném měřítku vyžaduje cloudové myšlení - a velké množství dat. Iniciativa [Planetary Computer](https://planetarycomputer.microsoft.com/) poskytuje 4 komponenty, které pomáhají datovým vědcům a vývojářům v tomto úsilí:

 * [Katalog dat](https://planetarycomputer.microsoft.com/catalog) - s petabajty dat o systémech Země (zdarma a hostováno na Azure).
 * [Planetary API](https://planetarycomputer.microsoft.com/docs/reference/stac/) - pomáhá uživatelům hledat relevantní data napříč prostorem a časem.
 * [Hub](https://planetarycomputer.microsoft.com/docs/overview/environment/) - spravované prostředí pro vědce k zpracování masivních geodatových sad.
 * [Aplikace](https://planetarycomputer.microsoft.com/applications) - ukazují případy použití a nástroje pro udržitelné poznatky.
**Projekt Planetary Computer je aktuálně v náhledu (k září 2021)** - zde je návod, jak začít přispívat k řešením udržitelnosti pomocí datové vědy.

* [Požádejte o přístup](https://planetarycomputer.microsoft.com/account/request) a začněte s průzkumem a propojením s kolegy.
* [Prozkoumejte dokumentaci](https://planetarycomputer.microsoft.com/docs/overview/about), abyste porozuměli podporovaným datovým sadám a API.
* Prozkoumejte aplikace jako [Monitoring ekosystémů](https://analytics-lab.org/ecosystemmonitoring/) pro inspiraci na nápady aplikací.

Přemýšlejte o tom, jak můžete využít vizualizaci dat k odhalení nebo zesílení relevantních poznatků v oblastech, jako je změna klimatu a odlesňování. Nebo přemýšlejte o tom, jak lze poznatky využít k vytvoření nových uživatelských zkušeností, které motivují ke změně chování pro udržitelnější život.

## Datová věda + studenti

Hovořili jsme o aplikacích v reálném světě v průmyslu a výzkumu a prozkoumali příklady aplikací datové vědy v digitálních humanitních vědách a udržitelnosti. Jak si tedy můžete rozvíjet své dovednosti a sdílet své znalosti jako začátečníci v datové vědě?

Zde jsou některé příklady studentských projektů v oblasti datové vědy, které vás mohou inspirovat.

 * [Letní škola datové vědy MSR](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/#!projects) s GitHub [projekty](https://github.com/msr-ds3), které zkoumají témata jako:
    - [Rasová zaujatost při použití síly policií](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2019-replicating-an-empirical-analysis-of-racial-differences-in-police-use-of-force/) | [Github](https://github.com/msr-ds3/stop-question-frisk)
    - [Spolehlivost systému metra v NYC](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2018-exploring-the-reliability-of-the-nyc-subway-system/) | [Github](https://github.com/msr-ds3/nyctransit)
 * [Digitalizace materiální kultury: Zkoumání socio-ekonomických rozložení v Sirkapu](https://claremont.maps.arcgis.com/apps/Cascade/index.html?appid=bdf2aef0f45a4674ba41cd373fa23afc) - od [Ornella Altunyan](https://twitter.com/ornelladotcom) a týmu z Claremontu, využívající [ArcGIS StoryMaps](https://storymaps.arcgis.com/).

## 🚀 Výzva

Vyhledejte články, které doporučují projekty datové vědy vhodné pro začátečníky - například [těchto 50 témat](https://www.upgrad.com/blog/data-science-project-ideas-topics-beginners/) nebo [těchto 21 nápadů na projekty](https://www.intellspot.com/data-science-project-ideas) nebo [těchto 16 projektů se zdrojovým kódem](https://data-flair.training/blogs/data-science-project-ideas/), které můžete rozebrat a upravit. Nezapomeňte také blogovat o svých učebních cestách a sdílet své poznatky s námi všemi.

## Kvíz po přednášce

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ds/quiz/39)

## Přehled & samostudium

Chcete prozkoumat více případů použití? Zde je několik relevantních článků:
 * [17 aplikací a příkladů datové vědy](https://builtin.com/data-science/data-science-applications-examples) - červenec 2021
 * [11 úžasných aplikací datové vědy v reálném světě](https://myblindbird.com/data-science-applications-real-world/) - květen 2021
 * [Datová věda v reálném světě](https://towardsdatascience.com/data-science-in-the-real-world/home) - sbírka článků
 * [12 aplikací datové vědy v reálném světě s příklady](https://www.scaler.com/blog/data-science-applications/) - květen 2024
 * Datová věda v: [vzdělávání](https://data-flair.training/blogs/data-science-in-education/), [zemědělství](https://data-flair.training/blogs/data-science-in-agriculture/), [financích](https://data-flair.training/blogs/data-science-in-finance/), [filmech](https://data-flair.training/blogs/data-science-at-movies/), [zdravotní péči](https://onlinedegrees.sandiego.edu/data-science-health-care/) a dalších.

## Zadání

[Prozkoumejte datovou sadu Planetary Computer](assignment.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o co největší přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj by měl být považován původní dokument v jeho původním jazyce. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.