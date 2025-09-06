<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1341f6da63d434f5ba31b08ea951b02c",
  "translation_date": "2025-09-05T21:53:38+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "sv"
}
-->
# Introduktion till Dataetik

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Dataetik inom Data Science - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

---

Vi är alla datamedborgare som lever i en datadriven värld.

Marknadstrender visar att år 2022 kommer 1 av 3 stora organisationer att köpa och sälja sin data via online [marknadsplatser och utbyten](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/). Som **apputvecklare** kommer vi att upptäcka att det blir enklare och billigare att integrera datadrivna insikter och algoritmstyrd automatisering i dagliga användarupplevelser. Men när AI blir alltmer utbrett måste vi också förstå de potentiella skador som kan orsakas av [vapenisering](https://www.youtube.com/watch?v=TQHs8SA1qpk) av sådana algoritmer i stor skala.

Trender visar också att vi kommer att skapa och konsumera över [180 zettabyte](https://www.statista.com/statistics/871513/worldwide-data-created/) data år 2025. Som **dataforskare** ger detta oss enastående tillgång till personlig data. Det innebär att vi kan bygga beteendeprofiler av användare och påverka beslutsfattande på sätt som skapar en [illusion av fri vilja](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) samtidigt som vi potentiellt styr användare mot resultat vi föredrar. Det väcker också bredare frågor om datasekretess och användarskydd.

Dataetik är nu _nödvändiga skyddsräcken_ för dataforskning och ingenjörskonst, som hjälper oss att minimera potentiella skador och oavsiktliga konsekvenser av våra datadrivna handlingar. [Gartners Hype Cycle för AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) identifierar relevanta trender inom digital etik, ansvarsfull AI och AI-styrning som nyckeldrivkrafter för större megatrender kring _demokratisering_ och _industrialisering_ av AI.

![Gartners Hype Cycle för AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

I denna lektion kommer vi att utforska det fascinerande området dataetik - från grundläggande begrepp och utmaningar till fallstudier och tillämpade AI-koncept som styrning - som hjälper till att etablera en etisk kultur i team och organisationer som arbetar med data och AI.

## [Quiz före föreläsningen](https://ff-quizzes.netlify.app/en/ds/quiz/2) 🎯

## Grundläggande Definitioner

Låt oss börja med att förstå den grundläggande terminologin.

Ordet "etik" kommer från det [grekiska ordet "ethikos"](https://en.wikipedia.org/wiki/Ethics) (och dess rot "ethos") som betyder _karaktär eller moralisk natur_. 

**Etik** handlar om de gemensamma värderingar och moraliska principer som styr vårt beteende i samhället. Etik baseras inte på lagar utan på allmänt accepterade normer för vad som är "rätt kontra fel". Etiska överväganden kan dock påverka företagsstyrningsinitiativ och regeringsregleringar som skapar fler incitament för efterlevnad.

**Dataetik** är en [ny gren av etiken](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1) som "studerar och utvärderar moraliska problem relaterade till _data, algoritmer och motsvarande praxis_". Här fokuserar **"data"** på handlingar relaterade till generering, registrering, kurering, bearbetning, spridning, delning och användning, **"algoritmer"** fokuserar på AI, agenter, maskininlärning och robotar, och **"praxis"** fokuserar på ämnen som ansvarsfull innovation, programmering, hacking och etiska koder.

**Tillämpad etik** är den [praktiska tillämpningen av moraliska överväganden](https://en.wikipedia.org/wiki/Applied_ethics). Det är processen att aktivt undersöka etiska frågor i samband med _verkliga handlingar, produkter och processer_, och vidta korrigerande åtgärder för att säkerställa att dessa förblir i linje med våra definierade etiska värderingar.

**Etisk kultur** handlar om [_operationalisering_ av tillämpad etik](https://hbr.org/2019/05/how-to-design-an-ethical-organization) för att säkerställa att våra etiska principer och praxis antas på ett konsekvent och skalbart sätt över hela organisationen. Framgångsrika etiska kulturer definierar organisationsövergripande etiska principer, tillhandahåller meningsfulla incitament för efterlevnad och förstärker etiska normer genom att uppmuntra och förstärka önskade beteenden på varje nivå i organisationen.

## Etiska Begrepp

I denna sektion kommer vi att diskutera begrepp som **gemensamma värderingar** (principer) och **etiska utmaningar** (problem) för dataetik - och utforska **fallstudier** som hjälper dig att förstå dessa begrepp i verkliga sammanhang.

### 1. Etiska Principer

Varje strategi för dataetik börjar med att definiera _etiska principer_ - de "gemensamma värderingar" som beskriver acceptabla beteenden och styr efterlevnad i våra data- och AI-projekt. Du kan definiera dessa på individuell eller teamnivå. Men de flesta stora organisationer beskriver dessa i ett _etiskt AI_-uppdrag eller ramverk som definieras på företagsnivå och tillämpas konsekvent över alla team.

**Exempel:** Microsofts [Ansvarsfull AI](https://www.microsoft.com/en-us/ai/responsible-ai) uppdrag lyder: _"Vi är engagerade i att främja AI som drivs av etiska principer som sätter människor först"_ - och identifierar 6 etiska principer i ramverket nedan:

![Ansvarsfull AI hos Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Låt oss kortfattat utforska dessa principer. _Transparens_ och _ansvar_ är grundläggande värderingar som andra principer bygger på - så låt oss börja där:

* [**Ansvar**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) gör utövare _ansvariga_ för sina data- och AI-operationer och efterlevnad av dessa etiska principer.
* [**Transparens**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) säkerställer att data och AI-åtgärder är _förståeliga_ (tolkbara) för användare, och förklarar vad och varför bakom beslut.
* [**Rättvisa**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - fokuserar på att säkerställa att AI behandlar _alla människor_ rättvist, och adresserar eventuella systemiska eller implicita socio-tekniska fördomar i data och system.
* [**Tillförlitlighet och Säkerhet**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - säkerställer att AI beter sig _konsekvent_ med definierade värderingar, och minimerar potentiella skador eller oavsiktliga konsekvenser.
* [**Sekretess och Säkerhet**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - handlar om att förstå dataursprung och tillhandahålla _datasekretess och relaterade skydd_ för användare.
* [**Inkludering**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - handlar om att designa AI-lösningar med avsikt, och anpassa dem för att möta ett _brett spektrum av mänskliga behov_ och förmågor.

> 🚨 Fundera på vad ditt dataetiska uppdrag skulle kunna vara. Utforska etiska AI-ramverk från andra organisationer - här är exempel från [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles), och [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Vilka gemensamma värderingar har de? Hur relaterar dessa principer till AI-produkten eller industrin de verkar inom?

### 2. Etiska Utmaningar

När vi har definierat etiska principer är nästa steg att utvärdera våra data- och AI-åtgärder för att se om de överensstämmer med dessa gemensamma värderingar. Tänk på dina åtgärder i två kategorier: _datainsamling_ och _algoritmdesign_. 

Vid datainsamling kommer åtgärder sannolikt att involvera **personlig data** eller personligt identifierbar information (PII) för identifierbara levande individer. Detta inkluderar [olika typer av icke-personlig data](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en) som _tillsammans_ kan identifiera en individ. Etiska utmaningar kan relatera till _datasekretess_, _dataägande_ och relaterade ämnen som _informerat samtycke_ och _immateriella rättigheter_ för användare.

Vid algoritmdesign kommer åtgärder att involvera insamling och kurering av **datamängder**, och sedan använda dem för att träna och implementera **datamodeller** som förutspår resultat eller automatiserar beslut i verkliga sammanhang. Etiska utmaningar kan uppstå från _datamängdsfördomar_, _datakvalitetsproblem_, _orättvisa_ och _missrepresentation_ i algoritmer - inklusive vissa problem som är systemiska till sin natur.

I båda fallen belyser etiska utmaningar områden där våra åtgärder kan komma i konflikt med våra gemensamma värderingar. För att upptäcka, mildra, minimera eller eliminera dessa bekymmer måste vi ställa moraliska "ja/nej"-frågor relaterade till våra åtgärder och vidta korrigerande åtgärder vid behov. Låt oss titta på några etiska utmaningar och de moraliska frågor de väcker:

#### 2.1 Dataägande

Datainsamling involverar ofta personlig data som kan identifiera datasubjekten. [Dataägande](https://permission.io/blog/data-ownership) handlar om _kontroll_ och [_användarrättigheter_](https://permission.io/blog/data-ownership) relaterade till skapande, bearbetning och spridning av data. 

De moraliska frågor vi behöver ställa är: 
 * Vem äger datan? (användare eller organisation)
 * Vilka rättigheter har datasubjekten? (ex: åtkomst, radering, portabilitet)
 * Vilka rättigheter har organisationer? (ex: rätta skadliga användarrecensioner)

#### 2.2 Informerat Samtycke

[Informerat samtycke](https://legaldictionary.net/informed-consent/) definierar handlingen där användare godkänner en åtgärd (som datainsamling) med en _full förståelse_ av relevanta fakta inklusive syfte, potentiella risker och alternativ. 

Frågor att utforska här är:
 * Gav användaren (datasubjektet) tillstånd för datainsamling och användning?
 * Förstod användaren syftet med att datan samlades in?
 * Förstod användaren de potentiella riskerna med sitt deltagande?

#### 2.3 Immateriella Rättigheter

[Immateriella rättigheter](https://en.wikipedia.org/wiki/Intellectual_property) avser immateriella skapelser som resultat av mänskligt initiativ, som kan _ha ekonomiskt värde_ för individer eller företag. 

Frågor att utforska här är:
 * Hade den insamlade datan ekonomiskt värde för en användare eller ett företag?
 * Har **användaren** immateriella rättigheter här?
 * Har **organisationen** immateriella rättigheter här?
 * Om dessa rättigheter finns, hur skyddar vi dem?

#### 2.4 Datasekretess

[Datasekretess](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) eller informationssekretess avser bevarandet av användarsekretess och skydd av användaridentitet med avseende på personligt identifierbar information. 

Frågor att utforska här är:
 * Är användarnas (personliga) data säkrad mot hack och läckor?
 * Är användarnas data endast tillgänglig för auktoriserade användare och sammanhang?
 * Bevaras användarnas anonymitet när data delas eller sprids?
 * Kan en användare avidentifieras från anonymiserade datamängder?

#### 2.5 Rätten att Bli Glömd

[Rätten att bli glömd](https://en.wikipedia.org/wiki/Right_to_be_forgotten) eller [Rätten till Radering](https://www.gdpreu.org/right-to-be-forgotten/) ger ytterligare skydd för personlig data till användare. Specifikt ger det användare rätt att begära radering eller borttagning av personlig data från internetsökningar och andra platser, _under specifika omständigheter_ - vilket ger dem en ny start online utan att tidigare handlingar hålls emot dem.

Frågor att utforska här är:
 * Tillåter systemet datasubjekt att begära radering?
 * Bör återkallande av användarsamtycke utlösa automatisk radering?
 * Samlades data in utan samtycke eller på olagliga sätt?
 * Är vi kompatibla med regeringsregler för datasekretess?

#### 2.6 Datamängdsfördomar

Datamängds- eller [insamlingfördomar](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) handlar om att välja en _icke-representativ_ delmängd av data för algoritmutveckling, vilket skapar potentiell orättvisa i resultat för olika grupper. Typer av fördomar inkluderar urvals- eller provtagningsfördomar, frivilligfördomar och instrumentfördomar. 

Frågor att utforska här är:
 * Rekryterade vi en representativ uppsättning datasubjekt?
 * Testade vi vår insamlade eller kuraterade datamängd för olika fördomar?
 * Kan vi mildra eller ta bort upptäckta fördomar?

#### 2.7 Datakvalitet

[Datakvalitet](https://lakefs.io/data-quality-testing/) handlar om att kontrollera validiteten hos den kuraterade datamängden som används för att utveckla våra algoritmer, och se om funktioner och poster uppfyller kraven för den nivå av noggrannhet och konsekvens som behövs för vårt AI-syfte.

Frågor att utforska här är:
 * Fångade vi giltiga _funktioner_ för vårt användningsfall?
 * Samlades data in _konsekvent_ över olika datakällor?
 * Är datamängden _komplett_ för olika förhållanden eller scenarier?
 * Är informationen som samlades in _korrekt_ i att återspegla verkligheten?

#### 2.8 Algoritmisk Rättvisa
[Algorithmisk rättvisa](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) handlar om att undersöka om algoritmdesignen systematiskt diskriminerar specifika undergrupper av datainsamlade individer, vilket kan leda till [potentiella skador](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) inom _resursfördelning_ (där resurser nekas eller undanhålls från den gruppen) och _servicekvalitet_ (där AI inte är lika exakt för vissa undergrupper som för andra).

Frågor att utforska här är:
 * Har vi utvärderat modellens noggrannhet för olika undergrupper och förhållanden?
 * Har vi granskat systemet för potentiella skador (t.ex. stereotyper)?
 * Kan vi revidera data eller träna om modeller för att minska identifierade skador?

Utforska resurser som [AI Fairness checklists](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) för att lära dig mer.

#### 2.9 Missrepresentation

[Datamissrepresentation](https://www.sciencedirect.com/topics/computer-science/misrepresentation) handlar om att fråga om vi kommunicerar insikter från ärligt rapporterad data på ett vilseledande sätt för att stödja en önskad berättelse.

Frågor att utforska här är:
 * Rapporterar vi ofullständig eller felaktig data?
 * Visualiserar vi data på ett sätt som leder till vilseledande slutsatser?
 * Använder vi selektiva statistiska tekniker för att manipulera resultat?
 * Finns det alternativa förklaringar som kan ge en annan slutsats?

#### 2.10 Fri vilja
[Illusionen av fri vilja](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) uppstår när systemets "valarkitekturer" använder beslutsalgoritmer för att påverka människor att ta ett föredraget resultat samtidigt som det verkar ge dem alternativ och kontroll. Dessa [mörka mönster](https://www.darkpatterns.org/) kan orsaka social och ekonomisk skada för användare. Eftersom användarens beslut påverkar beteendeprofiler kan dessa handlingar potentiellt driva framtida val som förstärker eller förlänger effekten av dessa skador.

Frågor att utforska här är:
 * Förstod användaren konsekvenserna av att göra det valet?
 * Var användaren medveten om (alternativa) val och för- och nackdelarna med varje?
 * Kan användaren senare ändra ett automatiserat eller påverkat val?

### 3. Fallstudier

För att sätta dessa etiska utmaningar i verkliga sammanhang kan det vara hjälpsamt att titta på fallstudier som belyser potentiella skador och konsekvenser för individer och samhället när sådana etiska överträdelser förbises.

Här är några exempel:

| Etisk utmaning | Fallstudie  | 
|--- |--- |
| **Informerat samtycke** | 1972 - [Tuskegee Syfilisstudien](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Afroamerikanska män som deltog i studien lovades gratis medicinsk vård _men blev lurade_ av forskare som inte informerade deltagarna om deras diagnos eller om tillgänglig behandling. Många deltagare dog och deras partners eller barn påverkades; studien pågick i 40 år. | 
| **Datasekretess** |  2007 - [Netflix dataprize](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) gav forskare _10M anonymiserade filmrankningar från 50K kunder_ för att förbättra rekommendationsalgoritmer. Dock kunde forskare korrelera anonymiserad data med personligt identifierbar data i _externa dataset_ (t.ex. IMDb-kommentarer) - vilket effektivt "de-anonymiserade" vissa Netflix-abonnenter.|
| **Insamlingsbias**  | 2013 - Staden Boston [utvecklade Street Bump](https://www.boston.gov/transportation/street-bump), en app som lät medborgare rapportera potthål, vilket gav staden bättre vägdata för att hitta och åtgärda problem. Dock hade [personer i låginkomstgrupper mindre tillgång till bilar och telefoner](https://hbr.org/2013/04/the-hidden-biases-in-big-data), vilket gjorde deras vägproblem osynliga i appen. Utvecklarna samarbetade med akademiker för att hantera _rättvis tillgång och digitala klyftor_. |
| **Algoritmisk rättvisa**  | 2018 - MIT:s [Gender Shades Study](http://gendershades.org/overview.html) utvärderade noggrannheten hos AI-produkter för könsklassificering och avslöjade brister i noggrannhet för kvinnor och personer med mörkare hudton. Ett [2019 Apple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) verkade erbjuda mindre kredit till kvinnor än män. Båda exemplen illustrerade problem med algoritmisk bias som leder till socioekonomiska skador.|
| **Datamissrepresentation** | 2020 - [Georgia Department of Public Health släppte COVID-19-diagram](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) som verkade vilseleda medborgare om trender i bekräftade fall med icke-kronologisk ordning på x-axeln. Detta illustrerar missrepresentation genom visualiseringstrick. |
| **Illusionen av fri vilja** | 2020 - Läroappen [ABCmouse betalade $10M för att lösa en FTC-klagan](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) där föräldrar fastnade i att betala för abonnemang de inte kunde avbryta. Detta illustrerar mörka mönster i valarkitekturer, där användare påverkades att göra potentiellt skadliga val. |
| **Datasekretess & användarrättigheter** | 2021 - Facebook [Data Breach](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) exponerade data från 530M användare, vilket resulterade i en $5B-uppgörelse med FTC. Dock vägrade företaget att informera användare om dataintrånget, vilket bröt mot användarrättigheter kring datatransparens och åtkomst. |

Vill du utforska fler fallstudier? Kolla in dessa resurser:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - etiska dilemman inom olika branscher. 
* [Data Science Ethics course](https://www.coursera.org/learn/data-science-ethics#syllabus) - fallstudier som utforskas.
* [Where things have gone wrong](https://deon.drivendata.org/examples/) - deon-checklista med exempel.

> 🚨 Tänk på de fallstudier du har sett - har du upplevt eller blivit påverkad av en liknande etisk utmaning i ditt liv? Kan du komma på minst en annan fallstudie som illustrerar en av de etiska utmaningarna vi har diskuterat i detta avsnitt?

## Tillämpad etik

Vi har pratat om etiska koncept, utmaningar och fallstudier i verkliga sammanhang. Men hur börjar vi _tillämpa_ etiska principer och praxis i våra projekt? Och hur _operationaliserar_ vi dessa praxis för bättre styrning? Låt oss utforska några verkliga lösningar:

### 1. Professionella koder

Professionella koder erbjuder ett alternativ för organisationer att "motivera" medlemmar att stödja deras etiska principer och mission. Koder är _moraliska riktlinjer_ för professionellt beteende och hjälper anställda eller medlemmar att fatta beslut som överensstämmer med organisationens principer. De är endast effektiva om medlemmarna frivilligt följer dem; dock erbjuder många organisationer ytterligare belöningar och straff för att motivera efterlevnad.

Exempel inkluderar:

 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Code of Ethics
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Code of Conduct (skapad 2013)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (sedan 1993)

> 🚨 Tillhör du en professionell ingenjörs- eller datavetenskapsorganisation? Utforska deras webbplats för att se om de definierar en professionell etisk kod. Vad säger detta om deras etiska principer? Hur motiverar de medlemmar att följa koden?

### 2. Etiska checklistor

Medan professionella koder definierar nödvändigt _etiskt beteende_ från praktiker, har de [kända begränsningar](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) i efterlevnad, särskilt i storskaliga projekt. Istället förespråkar många datavetenskapsexperter [checklistor](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) som kan **koppla principer till praxis** på mer deterministiska och handlingsbara sätt.

Checklistor omvandlar frågor till "ja/nej"-uppgifter som kan operationaliseras, vilket gör att de kan spåras som en del av standardarbetsflöden för produktlansering.

Exempel inkluderar:
 * [Deon](https://deon.drivendata.org/) - en allmän datavetenskaplig etisk checklista skapad från [branschrekommendationer](https://deon.drivendata.org/#checklist-citations) med ett kommandoradsverktyg för enkel integration.
 * [Privacy Audit Checklist](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - ger allmän vägledning för informationshantering ur juridiska och sociala perspektiv.
 * [AI Fairness Checklist](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - skapad av AI-praktiker för att stödja adoption och integration av rättvisekontroller i AI-utvecklingscykler.
 * [22 frågor för etik inom data och AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - en mer öppen ram, strukturerad för initial utforskning av etiska frågor i design, implementering och organisatoriska sammanhang.

### 3. Etiska regleringar

Etik handlar om att definiera gemensamma värderingar och göra det rätta _frivilligt_. **Efterlevnad** handlar om _att följa lagen_ där den är definierad. **Styrning** omfattar brett alla sätt som organisationer arbetar för att upprätthålla etiska principer och följa etablerade lagar.

Idag tar styrning två former inom organisationer. För det första handlar det om att definiera **etiska AI**-principer och etablera praxis för att operationalisera adoption över alla AI-relaterade projekt i organisationen. För det andra handlar det om att följa alla statligt föreskrivna **dataskyddsregleringar** för regioner där organisationen verkar.

Exempel på dataskydds- och sekretessregleringar:

 * `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - reglerar _federala myndigheters_ insamling, användning och spridning av personlig information.
 * `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - skyddar personlig hälsodata.
 * `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - skyddar datasekretess för barn under 13 år.
 * `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - ger användarrättigheter, dataskydd och sekretess.
 * `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) ger konsumenter fler _rättigheter_ över deras (personliga) data.
 * `2021`, Kinas [Personal Information Protection Law](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) antogs nyligen och skapar en av de starkaste regleringarna för datasekretess online i världen.

> 🚨 Europeiska unionens GDPR (General Data Protection Regulation) är fortfarande en av de mest inflytelserika regleringarna för datasekretess idag. Visste du att den också definierar [8 användarrättigheter](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) för att skydda medborgares digitala sekretess och personliga data? Lär dig vad dessa är och varför de är viktiga.

### 4. Etisk kultur

Observera att det fortfarande finns en immateriell klyfta mellan _efterlevnad_ (att göra tillräckligt för att uppfylla "lagens bokstav") och att adressera [systemiska problem](https://www.coursera.org/learn/data-science-ethics/home/week/4) (som stelhet, informationsasymmetri och orättvis fördelning) som kan påskynda AI:s vapenisering.

Det senare kräver [samarbetsmetoder för att definiera etiska kulturer](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f) som bygger känslomässiga kopplingar och konsekventa gemensamma värderingar _över organisationer_ inom branschen. Detta kräver mer [formaliserade datavetenskapliga etiska kulturer](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) i organisationer - vilket gör det möjligt för _vem som helst_ att [dra Andon-snöret](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (för att lyfta etiska problem tidigt i processen) och göra _etiska bedömningar_ (t.ex. vid rekrytering) till ett kärnkriterium för teambildning i AI-projekt.

---
## [Efterföreläsningsquiz](https://ff-quizzes.netlify.app/en/ds/quiz/3) 🎯
## Granskning & Självstudier 

Kurser och böcker hjälper till att förstå grundläggande etiska koncept och utmaningar, medan fallstudier och verktyg hjälper till med tillämpad etik i verkliga sammanhang. Här är några resurser att börja med.

* [Machine Learning For Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - lektion om rättvisa, från Microsoft.
* [Principer för ansvarsfull AI](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - gratis utbildningsväg från Microsoft Learn.
* [Etik och Data Science](https://resources.oreilly.com/examples/0636920203964) - O'Reilly EBook (M. Loukides, H. Mason m.fl.)
* [Data Science Etik](https://www.coursera.org/learn/data-science-ethics#syllabus) - onlinekurs från University of Michigan.
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - fallstudier från University of Texas.

# Uppgift 

[Skriv en fallstudie om dataetik](assignment.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.