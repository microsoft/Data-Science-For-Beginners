<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "06bac7959b46b6e8aedcae014278c476",
  "translation_date": "2025-09-05T22:31:30+00:00",
  "source_file": "6-Data-Science-In-Wild/20-Real-World-Examples/README.md",
  "language_code": "no"
}
-->
# Data Science i den Virkelige Verden

| ![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-RealWorld.png) |
| :--------------------------------------------------------------------------------------------------------------: |
|               Data Science i den Virkelige Verden - _Sketchnote av [@nitya](https://twitter.com/nitya)_           |

Vi nærmer oss slutten av denne læringsreisen!

Vi startet med definisjoner av data science og etikk, utforsket ulike verktøy og teknikker for dataanalyse og visualisering, gjennomgikk livssyklusen for data science, og så på hvordan man kan skalere og automatisere arbeidsflyter for data science med skytjenester. Så du lurer kanskje: _"Hvordan kan jeg egentlig koble alt dette til virkelige sammenhenger?"_

I denne leksjonen skal vi utforske virkelige anvendelser av data science på tvers av bransjer og dykke ned i spesifikke eksempler innen forskning, digitale humaniora og bærekraft. Vi skal også se på studentprosjektmuligheter og avslutte med nyttige ressurser som kan hjelpe deg med å fortsette læringsreisen din!

## Quiz før forelesning

## [Quiz før forelesning](https://ff-quizzes.netlify.app/en/ds/quiz/38)

## Data Science + Industri

Takket være demokratiseringen av AI, finner utviklere det nå enklere å designe og integrere AI-drevne beslutningsprosesser og datadrevne innsikter i brukeropplevelser og utviklingsarbeidsflyter. Her er noen eksempler på hvordan data science "brukes" i virkelige applikasjoner på tvers av bransjer:

 * [Google Flu Trends](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) brukte data science for å korrelere søketermer med influensatrender. Selv om tilnærmingen hadde svakheter, skapte den bevissthet om mulighetene (og utfordringene) ved datadrevne helseprediksjoner.

 * [UPS Routing Predictions](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - forklarer hvordan UPS bruker data science og maskinlæring for å forutsi optimale leveringsruter, med hensyn til værforhold, trafikkmønstre, leveringsfrister og mer.

 * [NYC Taxicab Route Visualization](http://chriswhong.github.io/nyctaxi/) - data samlet inn ved hjelp av [Freedom Of Information Laws](https://chriswhong.com/open-data/foil_nyc_taxi/) bidro til å visualisere en dag i livet til NYC-taxier, og hjalp oss med å forstå hvordan de navigerer i den travle byen, hvor mye de tjener, og varigheten av turer over en 24-timers periode.

 * [Uber Data Science Workbench](https://eng.uber.com/dsw/) - bruker data (om hente- og leveringssteder, turvarighet, foretrukne ruter osv.) samlet fra millioner av Uber-turer *daglig* for å bygge et dataanalytisk verktøy som hjelper med prissetting, sikkerhet, svindeldeteksjon og navigasjonsbeslutninger.

 * [Sports Analytics](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - fokuserer på _prediktiv analyse_ (lag- og spilleranalyse - tenk [Moneyball](https://datasciencedegree.wisconsin.edu/blog/moneyball-proves-importance-big-data-big-ideas/) - og fanhåndtering) og _datavisualisering_ (lag- og fandashboards, spill osv.) med applikasjoner som talentspeiding, sportsbetting og inventar-/arenaadministrasjon.

 * [Data Science i Banksektoren](https://data-flair.training/blogs/data-science-in-banking/) - fremhever verdien av data science i finansindustrien med applikasjoner som risikomodellering og svindeldeteksjon, kundesegmentering, sanntidsprediksjon og anbefalingssystemer. Prediktiv analyse driver også kritiske tiltak som [kredittscore](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit).

 * [Data Science i Helsevesenet](https://data-flair.training/blogs/data-science-in-healthcare/) - fremhever applikasjoner som medisinsk bildediagnostikk (f.eks. MR, røntgen, CT-skanning), genomikk (DNA-sekvensering), legemiddelutvikling (risikovurdering, suksessprediksjon), prediktiv analyse (pasientbehandling og logistikk), sykdomssporing og forebygging.

![Data Science Applications in The Real World](../../../../6-Data-Science-In-Wild/20-Real-World-Examples/images/data-science-applications.png) Bildekreditt: [Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

Figuren viser andre domener og eksempler på bruk av data science-teknikker. Vil du utforske andre applikasjoner? Sjekk ut [Gjennomgang og Selvstudium](../../../../6-Data-Science-In-Wild/20-Real-World-Examples)-seksjonen nedenfor.

## Data Science + Forskning

| ![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Research.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Data Science & Forskning - _Sketchnote av [@nitya](https://twitter.com/nitya)_              |

Mens virkelige applikasjoner ofte fokuserer på bruksområder i industrien i stor skala, kan _forskningsapplikasjoner_ og prosjekter være nyttige fra to perspektiver:

* _innovasjonsmuligheter_ - utforske rask prototyping av avanserte konsepter og testing av brukeropplevelser for neste generasjons applikasjoner.
* _utfordringer ved implementering_ - undersøke potensielle skader eller utilsiktede konsekvenser av data science-teknologier i virkelige sammenhenger.

For studenter kan disse forskningsprosjektene gi både lærings- og samarbeidsmuligheter som kan forbedre forståelsen av emnet og utvide bevisstheten og engasjementet med relevante personer eller team som jobber innen interesseområder. Hvordan ser forskningsprosjekter ut, og hvordan kan de ha en innvirkning?

La oss se på ett eksempel - [MIT Gender Shades Study](http://gendershades.org/overview.html) av Joy Buolamwini (MIT Media Labs) med en [signaturforskningsartikkel](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf) medforfattet av Timnit Gebru (den gang ved Microsoft Research) som fokuserte på:

 * **Hva:** Målet med forskningsprosjektet var å _evaluere skjevheter i automatiserte ansiktsanalysealgoritmer og datasett_ basert på kjønn og hudtype.
 * **Hvorfor:** Ansiktsanalyse brukes i områder som rettshåndhevelse, flyplassikkerhet, ansettelsessystemer og mer - sammenhenger der unøyaktige klassifiseringer (f.eks. på grunn av skjevheter) kan forårsake økonomiske og sosiale skader for berørte individer eller grupper. Å forstå (og eliminere eller redusere) skjevheter er nøkkelen til rettferdighet i bruk.
 * **Hvordan:** Forskerne oppdaget at eksisterende referansedata hovedsakelig brukte personer med lysere hud, og kuraterte et nytt datasett (1000+ bilder) som var _mer balansert_ med hensyn til kjønn og hudtype. Datasettet ble brukt til å evaluere nøyaktigheten til tre kjønnsklassifiseringsprodukter (fra Microsoft, IBM og Face++).

Resultatene viste at selv om den generelle klassifiseringsnøyaktigheten var god, var det en merkbar forskjell i feilrater mellom ulike undergrupper - med **feilkjønning** som var høyere for kvinner eller personer med mørkere hudtyper, noe som indikerte skjevheter.

**Viktige Resultater:** Økt bevissthet om at data science trenger mer _representative datasett_ (balanserte undergrupper) og mer _inkluderende team_ (mangfoldige bakgrunner) for å oppdage og eliminere eller redusere slike skjevheter tidligere i AI-løsninger. Forskningsinnsatser som dette er også avgjørende for at mange organisasjoner kan definere prinsipper og praksiser for _ansvarlig AI_ for å forbedre rettferdighet i deres AI-produkter og prosesser.

**Vil du lære om relevante forskningsinnsatser hos Microsoft?**

* Sjekk ut [Microsoft Research Projects](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project) innen kunstig intelligens.
* Utforsk studentprosjekter fra [Microsoft Research Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/).
* Sjekk ut [Fairlearn](https://fairlearn.org/)-prosjektet og [Ansvarlig AI](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6)-initiativene.

## Data Science + Humaniora

| ![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Data Science & Digitale Humaniora - _Sketchnote av [@nitya](https://twitter.com/nitya)_              |

Digitale Humaniora [er definert](https://digitalhumanities.stanford.edu/about-dh-stanford) som "en samling av praksiser og tilnærminger som kombinerer beregningsmetoder med humanistisk undersøkelse". [Stanford-prosjekter](https://digitalhumanities.stanford.edu/projects) som _"rebooting history"_ og _"poetic thinking"_ illustrerer koblingen mellom [Digitale Humaniora og Data Science](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science) - med vekt på teknikker som nettverksanalyse, informasjonsvisualisering, romlig og tekstanalyse som kan hjelpe oss med å gjenbesøke historiske og litterære datasett for å utlede nye innsikter og perspektiver.

*Vil du utforske og utvide et prosjekt innen dette området?*

Sjekk ut ["Emily Dickinson and the Meter of Mood"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671) - et flott eksempel fra [Jen Looper](https://twitter.com/jenlooper) som spør hvordan vi kan bruke data science til å gjenbesøke kjent poesi og revurdere dens betydning og bidragene fra forfatteren i nye sammenhenger. For eksempel, _kan vi forutsi hvilken årstid et dikt ble skrevet i ved å analysere tonen eller sentimentet_ - og hva forteller dette oss om forfatterens sinnstilstand i den aktuelle perioden?

For å svare på det spørsmålet følger vi trinnene i livssyklusen for data science:
 * [`Dataanskaffelse`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#acquiring-the-dataset) - for å samle inn et relevant datasett for analyse. Alternativer inkluderer bruk av en API (f.eks. [Poetry DB API](https://poetrydb.org/index.html)) eller skraping av nettsider (f.eks. [Project Gutenberg](https://www.gutenberg.org/files/12242/12242-h/12242-h.htm)) ved hjelp av verktøy som [Scrapy](https://scrapy.org/).
 * [`Datavask`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#clean-the-data) - forklarer hvordan tekst kan formateres, renses og forenkles ved hjelp av grunnleggende verktøy som Visual Studio Code og Microsoft Excel.
 * [`Dataanalyse`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#working-with-the-data-in-a-notebook) - forklarer hvordan vi nå kan importere datasettet til "Notebooks" for analyse ved hjelp av Python-pakker (som pandas, numpy og matplotlib) for å organisere og visualisere dataene.
 * [`Sentimentanalyse`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#sentiment-analysis-using-cognitive-services) - forklarer hvordan vi kan integrere skytjenester som Text Analytics, ved hjelp av lavkodeverktøy som [Power Automate](https://flow.microsoft.com/en-us/) for automatiserte databehandlingsarbeidsflyter.

Ved å bruke denne arbeidsflyten kan vi utforske sesongmessige påvirkninger på sentimentet i diktene og hjelpe oss med å forme våre egne perspektiver på forfatteren. Prøv det selv - og utvid deretter notatboken for å stille andre spørsmål eller visualisere dataene på nye måter!

> Du kan bruke noen av verktøyene i [Digital Humanities Toolkit](https://github.com/Digital-Humanities-Toolkit) for å forfølge disse undersøkelsene.

## Data Science + Bærekraft

| ![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Sustainability.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Data Science & Bærekraft - _Sketchnote av [@nitya](https://twitter.com/nitya)_              |

[2030 Agenda for Bærekraftig Utvikling](https://sdgs.un.org/2030agenda) - vedtatt av alle FN-medlemmer i 2015 - identifiserer 17 mål, inkludert mål som fokuserer på **å beskytte planeten** mot degradering og virkningen av klimaendringer. [Microsoft Sustainability](https://www.microsoft.com/en-us/sustainability)-initiativet støtter disse målene ved å utforske måter teknologiløsninger kan støtte og bygge mer bærekraftige fremtider med et [fokus på 4 mål](https://dev.to/azure/a-visual-guide-to-sustainable-software-engineering-53hh) - å være karbonnegative, vannpositive, null avfall og biologisk mangfoldige innen 2030.

Å takle disse utfordringene på en skalerbar og tidsriktig måte krever tenkning i skyskala - og store mengder data. [Planetary Computer](https://planetarycomputer.microsoft.com/)-initiativet gir 4 komponenter for å hjelpe dataforskere og utviklere i denne innsatsen:

 * [Data Catalog](https://planetarycomputer.microsoft.com/catalog) - med petabyte av data om jordens systemer (gratis og Azure-hostet).
 * [Planetary API](https://planetarycomputer.microsoft.com/docs/reference/stac/) - for å hjelpe brukere med å søke etter relevante data på tvers av rom og tid.
 * [Hub](https://planetarycomputer.microsoft.com/docs/overview/environment/) - et administrert miljø for forskere til å behandle massive geospatiale datasett.
 * [Applikasjoner](https://planetarycomputer.microsoft.com/applications) - viser bruksområder og verktøy for bærekraftige innsikter.
**Planetary Computer-prosjektet er for øyeblikket i forhåndsvisning (per september 2021)** – her er hvordan du kan komme i gang med å bidra til bærekraftige løsninger ved hjelp av dataanalyse.

* [Be om tilgang](https://planetarycomputer.microsoft.com/account/request) for å starte utforskningen og koble deg til andre.
* [Utforsk dokumentasjonen](https://planetarycomputer.microsoft.com/docs/overview/about) for å forstå hvilke datasett og API-er som støttes.
* Utforsk applikasjoner som [Ecosystem Monitoring](https://analytics-lab.org/ecosystemmonitoring/) for inspirasjon til applikasjonsideer.

Tenk på hvordan du kan bruke datavisualisering for å avdekke eller forsterke relevante innsikter innen områder som klimaendringer og avskoging. Eller vurder hvordan innsikter kan brukes til å skape nye brukeropplevelser som motiverer til atferdsendringer for et mer bærekraftig liv.

## Dataanalyse + Studenter

Vi har snakket om virkelige applikasjoner i industrien og forskningen, og utforsket eksempler på dataanalyseapplikasjoner innen digital humaniora og bærekraft. Så hvordan kan du bygge ferdighetene dine og dele ekspertisen din som nybegynner innen dataanalyse?

Her er noen eksempler på studentprosjekter innen dataanalyse for å inspirere deg.

* [MSR Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/#!projects) med GitHub [prosjekter](https://github.com/msr-ds3) som utforsker temaer som:
   - [Rasistisk skjevhet i politiets bruk av makt](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2019-replicating-an-empirical-analysis-of-racial-differences-in-police-use-of-force/) | [Github](https://github.com/msr-ds3/stop-question-frisk)
   - [Påliteligheten til New Yorks T-banesystem](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2018-exploring-the-reliability-of-the-nyc-subway-system/) | [Github](https://github.com/msr-ds3/nyctransit)
* [Digitalisering av materiell kultur: Utforsking av sosioøkonomiske fordelinger i Sirkap](https://claremont.maps.arcgis.com/apps/Cascade/index.html?appid=bdf2aef0f45a4674ba41cd373fa23afc) – fra [Ornella Altunyan](https://twitter.com/ornelladotcom) og teamet ved Claremont, ved bruk av [ArcGIS StoryMaps](https://storymaps.arcgis.com/).

## 🚀 Utfordring

Søk etter artikler som anbefaler nybegynnervennlige dataanalyseprosjekter – som [disse 50 temaområdene](https://www.upgrad.com/blog/data-science-project-ideas-topics-beginners/) eller [disse 21 prosjektideene](https://www.intellspot.com/data-science-project-ideas) eller [disse 16 prosjektene med kildekode](https://data-flair.training/blogs/data-science-project-ideas/) som du kan dekonstruere og remikse. Og ikke glem å blogge om læringsreisen din og dele innsiktene dine med oss alle.

## Quiz etter forelesning

## [Quiz etter forelesning](https://ff-quizzes.netlify.app/en/ds/quiz/39)

## Gjennomgang og selvstudium

Vil du utforske flere bruksområder? Her er noen relevante artikler:
* [17 Data Science Applications and Examples](https://builtin.com/data-science/data-science-applications-examples) – juli 2021
* [11 Breathtaking Data Science Applications in Real World](https://myblindbird.com/data-science-applications-real-world/) – mai 2021
* [Data Science In The Real World](https://towardsdatascience.com/data-science-in-the-real-world/home) – Artikkelsamling
* Dataanalyse innen: [Utdanning](https://data-flair.training/blogs/data-science-in-education/), [Landbruk](https://data-flair.training/blogs/data-science-in-agriculture/), [Finans](https://data-flair.training/blogs/data-science-in-finance/), [Film](https://data-flair.training/blogs/data-science-at-movies/) og mer.

## Oppgave

[Utforsk et Planetary Computer-datasett](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.