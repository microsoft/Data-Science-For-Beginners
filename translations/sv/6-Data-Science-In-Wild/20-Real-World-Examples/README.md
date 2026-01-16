<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0f67a4139454816631526779a456b734",
  "translation_date": "2025-09-06T18:32:07+00:00",
  "source_file": "6-Data-Science-In-Wild/20-Real-World-Examples/README.md",
  "language_code": "sv"
}
-->
# Data Science i Verkligheten

| ![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-RealWorld.png) |
| :--------------------------------------------------------------------------------------------------------------: |
|               Data Science i Verkligheten - _Sketchnote av [@nitya](https://twitter.com/nitya)_               |

Vi är nästan i mål med denna läranderesa!

Vi började med att definiera data science och etik, utforskade olika verktyg och tekniker för dataanalys och visualisering, gick igenom data science-livscykeln och tittade på hur man kan skala och automatisera data science-arbetsflöden med molntjänster. Så du kanske undrar: _"Hur kan jag koppla allt detta till verkliga sammanhang?"_

I denna lektion kommer vi att utforska verkliga tillämpningar av data science inom olika branscher och dyka ner i specifika exempel inom forskning, digital humaniora och hållbarhet. Vi kommer att titta på studentprojektmöjligheter och avsluta med användbara resurser för att hjälpa dig fortsätta din läranderesa!

## Förhandsquiz

## [Förhandsquiz](https://ff-quizzes.netlify.app/en/ds/quiz/38)

## Data Science + Industri

Tack vare AI:s demokratisering är det nu enklare för utvecklare att designa och integrera AI-drivna beslutsprocesser och datadrivna insikter i användarupplevelser och utvecklingsarbetsflöden. Här är några exempel på hur data science används i verkliga tillämpningar inom industrin:

 * [Google Flu Trends](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) använde data science för att korrelera söktermer med influensatrender. Även om metoden hade brister, väckte den medvetenhet om möjligheterna (och utmaningarna) med datadrivna hälsoprediktioner.

 * [UPS Routing Predictions](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - förklarar hur UPS använder data science och maskininlärning för att förutsäga optimala leveransrutter, med hänsyn till väderförhållanden, trafikmönster, leveransdeadlines och mer.

 * [NYC Taxicab Route Visualization](http://chriswhong.github.io/nyctaxi/) - data insamlad med hjälp av [Freedom Of Information Laws](https://chriswhong.com/open-data/foil_nyc_taxi/) hjälpte till att visualisera en dag i livet för NYC-taxibilar, vilket gav insikter om hur de navigerar i den hektiska staden, hur mycket pengar de tjänar och hur lång tid resorna tar under en 24-timmarsperiod.

 * [Uber Data Science Workbench](https://eng.uber.com/dsw/) - använder data (om upphämtnings- och avlämningsplatser, reslängd, föredragna rutter etc.) insamlad från miljontals Uber-resor *dagligen* för att bygga ett dataanalysverktyg som hjälper med prissättning, säkerhet, bedrägeridetektion och navigeringsbeslut.

 * [Sports Analytics](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - fokuserar på _prediktiv analys_ (lag- och spelaranalys - tänk [Moneyball](https://datasciencedegree.wisconsin.edu/blog/moneyball-proves-importance-big-data-big-ideas/) - och hantering av fans) och _datavisualisering_ (lag- och fandashboards, spel etc.) med tillämpningar som talangscouting, sportspel och hantering av inventarier/arenor.

 * [Data Science i Banksektorn](https://data-flair.training/blogs/data-science-in-banking/) - lyfter fram värdet av data science inom finansindustrin med tillämpningar som riskmodellering och bedrägeridetektion, kundsegmentering, realtidsprognoser och rekommendationssystem. Prediktiv analys driver också viktiga mått som [kreditvärderingar](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit).

 * [Data Science inom Hälsovård](https://data-flair.training/blogs/data-science-in-healthcare/) - lyfter fram tillämpningar som medicinsk bildbehandling (t.ex. MRI, röntgen, CT-skanning), genomik (DNA-sekvensering), läkemedelsutveckling (riskbedömning, framgångsprognoser), prediktiv analys (patientvård och logistik), sjukdomsspårning och förebyggande åtgärder.

![Data Science-tillämpningar i Verkligheten](../../../../translated_images/sv/data-science-applications.4e5019cd8790ebac2277ff5f08af386f8727cac5d30f77727c7090677e6adb9c.png) Bildkälla: [Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

Figuren visar andra områden och exempel på hur data science-tekniker kan tillämpas. Vill du utforska fler tillämpningar? Kolla in [Review & Self Study](../../../../6-Data-Science-In-Wild/20-Real-World-Examples)-avsnittet nedan.

## Data Science + Forskning

| ![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Research.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Data Science & Forskning - _Sketchnote av [@nitya](https://twitter.com/nitya)_              |

Medan verkliga tillämpningar ofta fokuserar på industriella användningsfall i stor skala, kan _forskningsprojekt_ vara användbara ur två perspektiv:

* _innovationsmöjligheter_ - utforska snabb prototypframtagning av avancerade koncept och testning av användarupplevelser för nästa generations applikationer.
* _implementeringsutmaningar_ - undersök potentiella skador eller oavsiktliga konsekvenser av data science-teknologier i verkliga sammanhang.

För studenter kan dessa forskningsprojekt ge både lärande och samarbetsmöjligheter som förbättrar din förståelse för ämnet och breddar din medvetenhet och engagemang med relevanta personer eller team som arbetar inom intressanta områden. Så hur ser forskningsprojekt ut och hur kan de göra skillnad?

Låt oss titta på ett exempel - [MIT Gender Shades Study](http://gendershades.org/overview.html) av Joy Buolamwini (MIT Media Labs) med en [signaturforskningsartikel](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf) medförfattad av Timnit Gebru (då vid Microsoft Research) som fokuserade på:

 * **Vad:** Syftet med forskningsprojektet var att _utvärdera bias i automatiserade algoritmer och dataset för ansiktsanalys_ baserat på kön och hudtyp. 
 * **Varför:** Ansiktsanalys används inom områden som brottsbekämpning, flygplatssäkerhet, rekryteringssystem och mer - sammanhang där felaktiga klassificeringar (t.ex. på grund av bias) kan orsaka ekonomiska och sociala skador för drabbade individer eller grupper. Att förstå (och eliminera eller mildra) bias är avgörande för rättvisa i användningen.
 * **Hur:** Forskarna insåg att befintliga benchmarks huvudsakligen använde ljushyade personer och skapade ett nytt dataset (1000+ bilder) som var _mer balanserat_ vad gäller kön och hudtyp. Datasetet användes för att utvärdera noggrannheten hos tre könsklassificeringsprodukter (från Microsoft, IBM & Face++). 

Resultaten visade att även om den totala klassificeringsnoggrannheten var bra, fanns det en märkbar skillnad i felprocent mellan olika undergrupper - med **felkönande** som var högre för kvinnor eller personer med mörkare hudtyper, vilket indikerar bias.

**Viktiga Resultat:** Ökad medvetenhet om att data science behöver mer _representativa dataset_ (balanserade undergrupper) och mer _inkluderande team_ (mångsidiga bakgrunder) för att identifiera och eliminera eller mildra sådana bias tidigt i AI-lösningar. Forskningsinsatser som denna är också avgörande för att många organisationer ska kunna definiera principer och praxis för _ansvarsfull AI_ för att förbättra rättvisa i sina AI-produkter och processer.

**Vill du lära dig om relevanta forskningsinsatser på Microsoft?** 

* Kolla in [Microsoft Research Projects](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project) inom artificiell intelligens.
* Utforska studentprojekt från [Microsoft Research Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/).
* Kolla in projektet [Fairlearn](https://fairlearn.org/) och initiativen för [Ansvarsfull AI](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6).

## Data Science + Humaniora

| ![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Data Science & Digital Humaniora - _Sketchnote av [@nitya](https://twitter.com/nitya)_              |

Digital Humaniora [har definierats](https://digitalhumanities.stanford.edu/about-dh-stanford) som "en samling av metoder och tillvägagångssätt som kombinerar beräkningsmetoder med humanistisk forskning". [Stanford-projekt](https://digitalhumanities.stanford.edu/projects) som _"rebooting history"_ och _"poetic thinking"_ illustrerar kopplingen mellan [Digital Humaniora och Data Science](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science) - med fokus på tekniker som nätverksanalys, informationsvisualisering, rumslig och textanalys som kan hjälpa oss att återbesöka historiska och litterära dataset för att få nya insikter och perspektiv.

*Vill du utforska och utveckla ett projekt inom detta område?*

Kolla in ["Emily Dickinson and the Meter of Mood"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671) - ett utmärkt exempel från [Jen Looper](https://twitter.com/jenlooper) som frågar hur vi kan använda data science för att återbesöka välkänd poesi och omvärdera dess betydelse och författarens bidrag i nya sammanhang. Till exempel, _kan vi förutsäga vilken årstid en dikt skrevs genom att analysera dess ton eller känsla_ - och vad säger detta om författarens sinnestillstånd under den relevanta perioden?

För att besvara den frågan följer vi stegen i vår data science-livscykel:
 * [`Data Acquisition`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#acquiring-the-dataset) - för att samla in ett relevant dataset för analys. Alternativ inkluderar att använda ett API (t.ex. [Poetry DB API](https://poetrydb.org/index.html)) eller att skrapa webbsidor (t.ex. [Project Gutenberg](https://www.gutenberg.org/files/12242/12242-h/12242-h.htm)) med verktyg som [Scrapy](https://scrapy.org/).
 * [`Data Cleaning`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#clean-the-data) - förklarar hur text kan formateras, saneras och förenklas med grundläggande verktyg som Visual Studio Code och Microsoft Excel.
 * [`Data Analysis`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#working-with-the-data-in-a-notebook) - förklarar hur vi kan importera datasetet till "Notebooks" för analys med Python-paket (som pandas, numpy och matplotlib) för att organisera och visualisera data.
 * [`Sentiment Analysis`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#sentiment-analysis-using-cognitive-services) - förklarar hur vi kan integrera molntjänster som Text Analytics, med hjälp av lågkodverktyg som [Power Automate](https://flow.microsoft.com/en-us/) för automatiserade databehandlingsarbetsflöden.

Med denna arbetsflöde kan vi utforska årstidernas påverkan på dikternas känslor och hjälpa oss att skapa våra egna perspektiv på författaren. Testa det själv - och utveckla sedan notebooken för att ställa andra frågor eller visualisera data på nya sätt!

> Du kan använda några av verktygen i [Digital Humanities toolkit](https://github.com/Digital-Humanities-Toolkit) för att utforska dessa forskningsvägar.

## Data Science + Hållbarhet

| ![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Sustainability.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Data Science & Hållbarhet - _Sketchnote av [@nitya](https://twitter.com/nitya)_              |

[Agenda 2030 för Hållbar Utveckling](https://sdgs.un.org/2030agenda) - antagen av alla FN-medlemmar 2015 - identifierar 17 mål, inklusive de som fokuserar på att **Skydda Planeten** från nedbrytning och klimatförändringarnas påverkan. [Microsoft Sustainability](https://www.microsoft.com/en-us/sustainability)-initiativet stödjer dessa mål genom att utforska hur teknologilösningar kan bidra till att bygga mer hållbara framtider med ett [fokus på 4 mål](https://dev.to/azure/a-visual-guide-to-sustainable-software-engineering-53hh) - att vara koldioxidnegativa, vattenpositiva, noll avfall och biologiskt mångfaldiga till 2030.

Att hantera dessa utmaningar på ett skalbart och tidsenligt sätt kräver tänkande i molnskala - och stora mängder data. [Planetary Computer](https://planetarycomputer.microsoft.com/)-initiativet erbjuder 4 komponenter för att hjälpa dataforskare och utvecklare i detta arbete:

 * [Data Catalog](https://planetarycomputer.microsoft.com/catalog) - med petabyte av data om jordens system (gratis och Azure-hostad).
 * [Planetary API](https://planetarycomputer.microsoft.com/docs/reference/stac/) - för att hjälpa användare att söka efter relevant data över tid och rum.
 * [Hub](https://planetarycomputer.microsoft.com/docs/overview/environment/) - en hanterad miljö för forskare att bearbeta massiva geospatiala dataset.
 * [Applications](https://planetarycomputer.microsoft.com/applications) - visar användningsfall och verktyg för insikter om hållbarhet.
**Planetary Computer-projektet är för närvarande i förhandsvisning (från och med september 2021)** - här är hur du kan börja bidra till hållbara lösningar med hjälp av data science.

* [Begär åtkomst](https://planetarycomputer.microsoft.com/account/request) för att börja utforska och koppla samman med andra.
* [Utforska dokumentation](https://planetarycomputer.microsoft.com/docs/overview/about) för att förstå vilka dataset och API:er som stöds.
* Utforska applikationer som [Ecosystem Monitoring](https://analytics-lab.org/ecosystemmonitoring/) för inspiration till applikationsidéer.

Fundera på hur du kan använda datavisualisering för att avslöja eller förstärka relevanta insikter inom områden som klimatförändringar och avskogning. Eller fundera på hur insikter kan användas för att skapa nya användarupplevelser som motiverar beteendeförändringar för ett mer hållbart liv.

## Data Science + Studenter

Vi har pratat om verkliga tillämpningar inom industrin och forskningen och utforskat exempel på data science-applikationer inom digital humaniora och hållbarhet. Så hur kan du bygga dina färdigheter och dela din expertis som nybörjare inom data science?

Här är några exempel på studentprojekt inom data science för att inspirera dig.

* [MSR Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/#!projects) med GitHub [projekt](https://github.com/msr-ds3) som utforskar ämnen som:
   - [Rasistisk partiskhet i polisens användning av våld](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2019-replicating-an-empirical-analysis-of-racial-differences-in-police-use-of-force/) | [Github](https://github.com/msr-ds3/stop-question-frisk)
   - [Tillförlitligheten hos New Yorks tunnelbanesystem](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2018-exploring-the-reliability-of-the-nyc-subway-system/) | [Github](https://github.com/msr-ds3/nyctransit)
* [Digitalisering av materiell kultur: Utforska socio-ekonomiska fördelningar i Sirkap](https://claremont.maps.arcgis.com/apps/Cascade/index.html?appid=bdf2aef0f45a4674ba41cd373fa23afc) - från [Ornella Altunyan](https://twitter.com/ornelladotcom) och teamet vid Claremont, med hjälp av [ArcGIS StoryMaps](https://storymaps.arcgis.com/).

## 🚀 Utmaning

Sök efter artiklar som rekommenderar data science-projekt som är nybörjarvänliga - som [dessa 50 ämnesområden](https://www.upgrad.com/blog/data-science-project-ideas-topics-beginners/) eller [dessa 21 projektidéer](https://www.intellspot.com/data-science-project-ideas) eller [dessa 16 projekt med källkod](https://data-flair.training/blogs/data-science-project-ideas/) som du kan analysera och remix. Och glöm inte att blogga om dina läranderesor och dela dina insikter med oss alla.

## Efterföreläsningsquiz

## [Efterföreläsningsquiz](https://ff-quizzes.netlify.app/en/ds/quiz/39)

## Granskning & Självstudier

Vill du utforska fler användningsområden? Här är några relevanta artiklar:
* [17 Data Science-applikationer och exempel](https://builtin.com/data-science/data-science-applications-examples) - juli 2021
* [11 Fantastiska Data Science-applikationer i verkliga världen](https://myblindbird.com/data-science-applications-real-world/) - maj 2021
* [Data Science i den verkliga världen](https://towardsdatascience.com/data-science-in-the-real-world/home) - Artikelkollektion
* [12 Verkliga Data Science-applikationer med exempel](https://www.scaler.com/blog/data-science-applications/) - maj 2024
* Data Science inom: [Utbildning](https://data-flair.training/blogs/data-science-in-education/), [Jordbruk](https://data-flair.training/blogs/data-science-in-agriculture/), [Finans](https://data-flair.training/blogs/data-science-in-finance/), [Film](https://data-flair.training/blogs/data-science-at-movies/), [Hälsovård](https://onlinedegrees.sandiego.edu/data-science-health-care/) och mer.

## Uppgift

[Utforska ett Planetary Computer-dataset](assignment.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.