<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58860ce9a4b8a564003d2752f7c72851",
  "translation_date": "2025-10-03T16:38:15+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "da"
}
-->
# Introduktion til Dataetik

|![ Sketchnote af [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Data Science Ethics - _Sketchnote af [@nitya](https://twitter.com/nitya)_ |

---

Vi er alle databorgere, der lever i en verden præget af data.

Markedstendenser viser, at inden 2022 vil 1 ud af 3 store organisationer købe og sælge deres data via online [markedspladser og børser](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/). Som **appudviklere** vil vi finde det nemmere og billigere at integrere datadrevne indsigter og algoritmebaseret automatisering i daglige brugeroplevelser. Men efterhånden som AI bliver mere udbredt, skal vi også forstå de potentielle skader forårsaget af [våbenisering](https://www.youtube.com/watch?v=TQHs8SA1qpk) af sådanne algoritmer i stor skala.

Tendenser antyder, at vi inden 2025 vil generere og forbruge over [180 zettabytes](https://www.statista.com/statistics/871513/worldwide-data-created/) data. For **dataspecialister** giver denne eksplosion af information en enestående adgang til personlige og adfærdsmæssige data. Med denne adgang følger muligheden for at opbygge detaljerede brugerprofiler og subtilt påvirke beslutningstagning—ofte på måder, der skaber en [illusion af fri vilje](https://www.datasciencecentral.com/the-pareto-set-and-the-paradox-of-choice/). Selvom dette kan bruges til at skubbe brugere mod ønskede resultater, rejser det også kritiske spørgsmål om databeskyttelse, autonomi og de etiske grænser for algoritmisk indflydelse.

Dataetik er nu _nødvendige retningslinjer_ for datavidenskab og ingeniørarbejde, der hjælper os med at minimere potentielle skader og utilsigtede konsekvenser af vores datadrevne handlinger. [Gartner Hype Cycle for AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) identificerer relevante tendenser inden for digital etik, ansvarlig AI og AI-styring som nøglefaktorer for større megatrends omkring _demokratisering_ og _industrialisering_ af AI.

![Gartner's Hype Cycle for AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

I denne lektion vil vi udforske det fascinerende område inden for dataetik - fra kernekoncepter og udfordringer til casestudier og anvendte AI-koncepter som styring - der hjælper med at etablere en etik-kultur i teams og organisationer, der arbejder med data og AI.

## [Quiz før lektionen](https://ff-quizzes.netlify.app/en/ds/quiz/2) 🎯

## Grundlæggende Definitioner

Lad os starte med at forstå den grundlæggende terminologi.

Ordet "etik" stammer fra det [græske ord "ethikos"](https://en.wikipedia.org/wiki/Ethics) (og dets rod "ethos"), som betyder _karakter eller moralsk natur_. 

**Etik** handler om de fælles værdier og moralske principper, der styrer vores adfærd i samfundet. Etik er ikke baseret på love, men på bredt accepterede normer for, hvad der er "rigtigt vs. forkert". Dog kan etiske overvejelser påvirke initiativer inden for virksomhedsledelse og regeringsreguleringer, der skaber flere incitamenter til overholdelse.

**Dataetik** er en [ny gren af etik](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1), der "undersøger og evaluerer moralske problemer relateret til _data, algoritmer og tilsvarende praksis_". Her fokuserer **"data"** på handlinger relateret til generering, registrering, kuratering, behandling, formidling, deling og brug, **"algoritmer"** fokuserer på AI, agenter, maskinlæring og robotter, og **"praksis"** fokuserer på emner som ansvarlig innovation, programmering, hacking og etiske kodeks.

**Anvendt etik** er den [praktiske anvendelse af moralske overvejelser](https://en.wikipedia.org/wiki/Applied_ethics). Det er processen med aktivt at undersøge etiske spørgsmål i konteksten af _virkelige handlinger, produkter og processer_ og tage korrigerende foranstaltninger for at sikre, at disse forbliver i overensstemmelse med vores definerede etiske værdier.

**Etik-kultur** handler om [_operationelt at anvende_ anvendt etik](https://hbr.org/2019/05/how-to-design-an-ethical-organization) for at sikre, at vores etiske principper og praksis bliver vedtaget på en konsekvent og skalerbar måde i hele organisationen. Succesfulde etik-kulturer definerer organisationens etiske principper, giver meningsfulde incitamenter til overholdelse og forstærker etiske normer ved at opmuntre og fremhæve ønsket adfærd på alle niveauer i organisationen.

## Etiske Koncepter

I denne sektion vil vi diskutere koncepter som **fælles værdier** (principper) og **etiske udfordringer** (problemer) inden for dataetik - og udforske **casestudier**, der hjælper dig med at forstå disse koncepter i virkelige kontekster.

### 1. Etiske Principper

Enhver dataetik-strategi begynder med at definere _etiske principper_ - de "fælles værdier", der beskriver acceptable adfærd og guider overholdelse i vores data- og AI-projekter. Du kan definere disse på individuelt eller teamniveau. Dog beskriver de fleste store organisationer disse i en _etisk AI_-missionserklæring eller rammeværk, der er defineret på virksomhedsniveau og konsekvent håndhævet på tværs af alle teams.

**Eksempel:** Microsofts [Ansvarlig AI](https://www.microsoft.com/en-us/ai/responsible-ai)-missionserklæring lyder: _"Vi er forpligtet til at fremme AI drevet af etiske principper, der sætter mennesker først"_ - og identificerer 6 etiske principper i rammeværket nedenfor:

![Ansvarlig AI hos Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Lad os kort udforske disse principper. _Transparens_ og _ansvarlighed_ er grundlæggende værdier, som de andre principper bygger på - så lad os starte der:

* [**Ansvarlighed**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) gør praktikere _ansvarlige_ for deres data- og AI-operationer og overholdelse af disse etiske principper.
* [**Transparens**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) sikrer, at data- og AI-handlinger er _forståelige_ (fortolkelige) for brugere, og forklarer hvad og hvorfor bag beslutninger.
* [**Fairness**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - fokuserer på at sikre, at AI behandler _alle mennesker_ retfærdigt og adresserer eventuelle systemiske eller implicitte socio-tekniske bias i data og systemer.
* [**Pålidelighed & Sikkerhed**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - sikrer, at AI opfører sig _konsekvent_ med definerede værdier og minimerer potentielle skader eller utilsigtede konsekvenser.
* [**Privatliv & Sikkerhed**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - handler om at forstå dataens oprindelse og give _databeskyttelse og relaterede sikkerhedsforanstaltninger_ til brugere.
* [**Inklusion**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - handler om at designe AI-løsninger med intention og tilpasse dem til at imødekomme et _bredt spektrum af menneskelige behov_ og kapaciteter.

> 🚨 Tænk over, hvad din dataetik-missionserklæring kunne være. Udforsk etiske AI-rammeværk fra andre organisationer - her er eksempler fra [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles) og [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Hvilke fælles værdier har de? Hvordan relaterer disse principper sig til AI-produktet eller industrien, de opererer i?

### 2. Etiske Udfordringer

Når vi har defineret etiske principper, er næste skridt at evaluere vores data- og AI-handlinger for at se, om de stemmer overens med disse fælles værdier. Tænk på dine handlinger i to kategorier: _datainnsamling_ og _algoritmedesign_. 

Ved datainnsamling vil handlinger sandsynligvis involvere **personlige data** eller personligt identificerbare oplysninger (PII) for identificerbare levende individer. Dette inkluderer [forskellige typer af ikke-personlige data](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en), der _samlet set_ identificerer en person. Etiske udfordringer kan relateres til _databeskyttelse_, _dataejerskab_ og relaterede emner som _informeret samtykke_ og _intellektuelle ejendomsrettigheder_ for brugere.

Ved algoritmedesign vil handlinger involvere indsamling og kuratering af **datasæt**, som derefter bruges til at træne og implementere **datamodeller**, der forudsiger resultater eller automatiserer beslutninger i virkelige kontekster. Etiske udfordringer kan opstå fra _datasætbias_, _datakvalitetsproblemer_, _uretfærdighed_ og _fejlrepræsentation_ i algoritmer - inklusive nogle problemer, der er systemiske af natur.

I begge tilfælde fremhæver etiske udfordringer områder, hvor vores handlinger kan komme i konflikt med vores fælles værdier. For at opdage, afbøde, minimere eller eliminere disse bekymringer skal vi stille moralske "ja/nej"-spørgsmål relateret til vores handlinger og derefter tage korrigerende handlinger efter behov. Lad os se på nogle etiske udfordringer og de moralske spørgsmål, de rejser:

#### 2.1 Dataejerskab

Datainnsamling involverer ofte personlige data, der kan identificere datasubjekterne. [Dataejerskab](https://permission.io/blog/data-ownership) handler om _kontrol_ og [_brugernes rettigheder_](https://permission.io/blog/data-ownership) relateret til oprettelse, behandling og formidling af data. 

De moralske spørgsmål, vi skal stille, er: 
 * Hvem ejer dataene? (bruger eller organisation)
 * Hvilke rettigheder har datasubjekterne? (fx adgang, sletning, portabilitet)
 * Hvilke rettigheder har organisationer? (fx rette skadelige brugeranmeldelser)

#### 2.2 Informeret Samtykke

[Informeret samtykke](https://legaldictionary.net/informed-consent/) definerer handlingen, hvor brugere accepterer en handling (som datainnsamling) med en _fuld forståelse_ af relevante fakta, herunder formål, potentielle risici og alternativer. 

Spørgsmål at udforske her er:
 * Gav brugeren (datasubjektet) tilladelse til datainnsamling og brug?
 * Forstod brugeren formålet med, hvorfor dataene blev indsamlet?
 * Forstod brugeren de potentielle risici ved deres deltagelse?

#### 2.3 Intellektuel Ejendom

[Intellektuel ejendom](https://en.wikipedia.org/wiki/Intellectual_property) refererer til immaterielle skabelser, der er resultatet af menneskelig initiativ, og som kan _have økonomisk værdi_ for individer eller virksomheder. 

Spørgsmål at udforske her er:
 * Havde de indsamlede data økonomisk værdi for en bruger eller virksomhed?
 * Har **brugeren** intellektuel ejendom her?
 * Har **organisationen** intellektuel ejendom her?
 * Hvis disse rettigheder eksisterer, hvordan beskytter vi dem?

#### 2.4 Databeskyttelse

[Databeskyttelse](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) eller informationsbeskyttelse refererer til bevarelse af brugerens privatliv og beskyttelse af brugerens identitet med hensyn til personligt identificerbare oplysninger. 

Spørgsmål at udforske her er:
 * Er brugernes (personlige) data sikret mod hacking og lækager?
 * Er brugernes data kun tilgængelige for autoriserede brugere og kontekster?
 * Bevares brugernes anonymitet, når data deles eller formidles?
 * Kan en bruger blive de-identificeret fra anonymiserede datasæt?

#### 2.5 Retten til at Blive Glemt

[Retten til at blive glemt](https://en.wikipedia.org/wiki/Right_to_be_forgotten) eller [Retten til Sletning](https://www.gdpreu.org/right-to-be-forgotten/) giver yderligere beskyttelse af personlige data til brugere. Specifikt giver det brugere ret til at anmode om sletning eller fjernelse af personlige data fra internetsøgninger og andre steder, _under specifikke omstændigheder_ - hvilket giver dem en ny start online uden tidligere handlinger, der holdes imod dem.

Spørgsmål at udforske her er:
 * Tillader systemet datasubjekter at anmode om sletning?
 * Skal tilbagetrækning af brugerens samtykke udløse automatisk sletning?
 * Blev data indsamlet uden samtykke eller på ulovlig vis?
 * Er vi i overensstemmelse med regeringsreguleringer for databeskyttelse?

#### 2.6 Datasætbias

Datasæt eller [indsamlingsbias](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) handler om at vælge et _ikke-repræsentativt_ datasæt til algoritmeudvikling, hvilket skaber potentiel uretfærdighed i resultatet for forskellige grupper. Typer af bias inkluderer udvælgelses- eller prøvebias, frivillig bias og instrumentbias. 

Spørgsmål at udforske her er:
 * Rekrutterede vi et repræsentativt datasæt af datasubjekter?
 * Testede vi vores indsamlede eller kuraterede datasæt for forskellige bias?
 * Kan vi afbøde eller fjerne eventuelle opdagede bias?

#### 2.7 Datakvalitet

[Datakvalitet](https://lakefs.io/data-quality-testing/) ser på gyldigheden af det kuraterede datasæt, der bruges til at udvikle vores algoritmer, og kontrollerer, om funktioner og poster opfylder kravene til det niveau af nøjagtighed og konsistens, der er nødvendigt for vores AI-formål.

Spørgsmål at udforske her er:
 * Indsamlede vi gyldige _funktioner_ til vores brugssag?
 * Blev data indsamlet _konsekvent_ på tværs af forskellige datakilder?
 * Er datasættet _komplet_ for forskellige forhold eller scenarier?
* Bliver information indfanget _præcist_ og afspejler virkeligheden?

#### 2.8 Algoritmisk Retfærdighed

[Algoritmisk Retfærdighed](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) undersøger, om algoritmens design systematisk diskriminerer specifikke undergrupper af datasubjekter, hvilket kan føre til [potentielle skader](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) i _ressourcefordeling_ (hvor ressourcer nægtes eller tilbageholdes fra den gruppe) og _servicekvalitet_ (hvor AI ikke er lige så præcis for nogle undergrupper som for andre).

Spørgsmål, der kan udforskes her, er:
* Evaluerede vi modelpræcision for forskellige undergrupper og forhold?
* Undersøgte vi systemet for potentielle skader (f.eks. stereotyper)?
* Kan vi revidere data eller genoptræne modeller for at afhjælpe identificerede skader?

Udforsk ressourcer som [AI Fairness-tjeklister](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) for at lære mere.

#### 2.9 Fejlrepræsentation

[Data Fejlrepræsentation](https://www.sciencedirect.com/topics/computer-science/misrepresentation) handler om at spørge, om vi kommunikerer indsigt fra ærligt rapporterede data på en vildledende måde for at understøtte en ønsket fortælling.

Spørgsmål, der kan udforskes her, er:
* Rapporterer vi ufuldstændige eller unøjagtige data?
* Visualiserer vi data på en måde, der fører til vildledende konklusioner?
* Bruger vi selektive statistiske teknikker til at manipulere resultater?
* Er der alternative forklaringer, der kan give en anden konklusion?

#### 2.10 Fri Valg
[Illusionen af Fri Valg](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) opstår, når systemets "valgarkitekturer" bruger beslutningsalgoritmer til at skubbe folk mod at tage et foretrukket resultat, mens det ser ud som om, de har muligheder og kontrol. Disse [mørke mønstre](https://www.darkpatterns.org/) kan forårsage sociale og økonomiske skader for brugere. Fordi brugerbeslutninger påvirker adfærdsprofiler, kan disse handlinger potentielt drive fremtidige valg, der kan forstærke eller udvide virkningen af disse skader.

Spørgsmål, der kan udforskes her, er:
* Forstod brugeren konsekvenserne af at træffe det valg?
* Var brugeren opmærksom på (alternative) valg og fordele & ulemper ved hver?
* Kan brugeren senere fortryde et automatiseret eller påvirket valg?

### 3. Case Studier

For at sætte disse etiske udfordringer i en virkelighedsnær kontekst hjælper det at se på case studier, der fremhæver de potentielle skader og konsekvenser for individer og samfund, når sådanne etiske overtrædelser overses.

Her er nogle eksempler:

| Etisk Udfordring | Case Studie | 
|--- |--- |
| **Informeret Samtykke** | 1972 - [Tuskegee Syfilis Studie](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Afroamerikanske mænd, der deltog i studiet, blev lovet gratis medicinsk behandling _men blev bedraget_ af forskere, der undlod at informere deltagerne om deres diagnose eller om tilgængelig behandling. Mange deltagere døde, og partnere eller børn blev påvirket; studiet varede i 40 år. | 
| **Databeskyttelse** | 2007 - [Netflix data-pris](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) gav forskere _10M anonymiserede filmvurderinger fra 50K kunder_ for at hjælpe med at forbedre anbefalingsalgoritmer. Forskere var dog i stand til at korrelere anonymiserede data med personligt identificerbare data i _eksterne datasæt_ (f.eks. IMDb-kommentarer) - effektivt "de-anonymiserende" nogle Netflix-abonnenter. |
| **Indsamlingsbias** | 2013 - Boston City [udviklede Street Bump](https://www.boston.gov/transportation/street-bump), en app, der lod borgere rapportere huller i vejen, hvilket gav byen bedre data til at finde og løse problemer. Dog havde [folk i lavindkomstgrupper mindre adgang til biler og telefoner](https://hbr.org/2013/04/the-hidden-biases-in-big-data), hvilket gjorde deres vejproblemer usynlige i denne app. Udviklere arbejdede med akademikere for at løse _lighed i adgang og digitale skel_ for retfærdighed. |
| **Algoritmisk Retfærdighed** | 2018 - MIT [Gender Shades Studie](http://gendershades.org/overview.html) evaluerede præcisionen af AI-produkter til kønsidentifikation og afslørede mangler i præcision for kvinder og farvede personer. Et [2019 Apple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) syntes at tilbyde mindre kredit til kvinder end mænd. Begge illustrerede problemer med algoritmisk bias, der førte til socioøkonomiske skader. |
| **Data Fejlrepræsentation** | 2020 - [Georgia Department of Public Health udgav COVID-19 diagrammer](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening), der syntes at vildlede borgere om tendenser i bekræftede tilfælde med ikke-kronologisk rækkefølge på x-aksen. Dette illustrerer fejlrepræsentation gennem visualiseringstricks. |
| **Illusionen af fri valg** | 2020 - Læringsappen [ABCmouse betalte $10M for at afvikle en FTC-klage](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/), hvor forældre blev fanget i at betale for abonnementer, de ikke kunne annullere. Dette illustrerer mørke mønstre i valgarkitekturer, hvor brugere blev skubbet mod potentielt skadelige valg. |
| **Databeskyttelse & Brugerrettigheder** | 2021 - Facebook [Data Brud](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) afslørede data fra 530M brugere, hvilket resulterede i en $5B afvikling til FTC. Det nægtede dog at informere brugere om bruddet, hvilket overtrådte brugerrettigheder omkring datatransparens og adgang. |

Vil du udforske flere case studier? Tjek disse ressourcer:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - etiske dilemmaer på tværs af forskellige industrier. 
* [Data Science Ethics kursus](https://www.coursera.org/learn/data-science-ethics#syllabus) - landmark case studier udforsket.
* [Hvor tingene er gået galt](https://deon.drivendata.org/examples/) - deon-tjekliste med eksempler.

> 🚨 Tænk over de case studier, du har set - har du oplevet eller været påvirket af en lignende etisk udfordring i dit liv? Kan du tænke på mindst én anden case studie, der illustrerer en af de etiske udfordringer, vi har diskuteret i dette afsnit?

## Anvendt Etik

Vi har talt om etiske begreber, udfordringer og case studier i virkelighedsnære kontekster. Men hvordan kommer vi i gang med at _anvende_ etiske principper og praksisser i vores projekter? Og hvordan _operationaliserer_ vi disse praksisser for bedre styring? Lad os udforske nogle virkelighedsnære løsninger:

### 1. Professionelle Koder

Professionelle koder tilbyder en mulighed for organisationer til at "incitamentere" medlemmer til at støtte deres etiske principper og mission. Koder er _moralske retningslinjer_ for professionel adfærd, der hjælper medarbejdere eller medlemmer med at træffe beslutninger, der stemmer overens med organisationens principper. De er kun så gode som den frivillige overholdelse fra medlemmer; dog tilbyder mange organisationer yderligere belønninger og sanktioner for at motivere overholdelse.

Eksempler inkluderer:

* [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Etisk kodeks
* [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Adfærdskodeks (oprettet 2013)
* [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (siden 1993)

> 🚨 Tilhører du en professionel ingeniør- eller data science-organisation? Udforsk deres hjemmeside for at se, om de definerer en professionel etisk kodeks. Hvad siger dette om deres etiske principper? Hvordan "incitamenterer" de medlemmer til at følge koden?

### 2. Etiske Tjeklister

Mens professionelle koder definerer krævet _etisk adfærd_ fra praktikere, har de [kendte begrænsninger](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) i håndhævelse, især i storskala projekter. I stedet anbefaler mange data science-eksperter [tjeklister](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), der kan **forbinde principper med praksis** på mere deterministiske og handlingsorienterede måder.

Tjeklister konverterer spørgsmål til "ja/nej"-opgaver, der kan operationaliseres, hvilket gør det muligt at spore dem som en del af standard produktudgivelsesarbejdsgange.

Eksempler inkluderer:
* [Deon](https://deon.drivendata.org/) - en generel dataetik-tjekliste oprettet fra [industriens anbefalinger](https://deon.drivendata.org/#checklist-citations) med et kommandolinjeværktøj for nem integration.
* [Privacy Audit Checklist](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - giver generel vejledning til informationshåndteringspraksis fra juridiske og sociale eksponeringsperspektiver.
* [AI Fairness Checklist](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - oprettet af AI-praktikere for at støtte adoption og integration af fairness-tjek i AI-udviklingscyklusser.
* [22 spørgsmål om etik i data og AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - en mere åben ramme, struktureret til indledende udforskning af etiske spørgsmål i design, implementering og organisatoriske kontekster.

### 3. Etiske Reguleringer

Etik handler om at definere fælles værdier og gøre det rigtige _frivilligt_. **Overholdelse** handler om _at følge loven_, hvis og hvor den er defineret. **Styring** dækker bredt alle de måder, hvorpå organisationer opererer for at håndhæve etiske principper og overholde etablerede love.

I dag tager styring to former inden for organisationer. For det første handler det om at definere **etiske AI**-principper og etablere praksisser for at operationalisere adoption på tværs af alle AI-relaterede projekter i organisationen. For det andet handler det om at overholde alle regeringsmandaterede **databeskyttelsesreguleringer** for de regioner, den opererer i.

Eksempler på databeskyttelses- og privatlivsreguleringer:

* `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - regulerer _føderal regeringens_ indsamling, brug og offentliggørelse af personlige oplysninger.
* `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - beskytter personlige sundhedsdata.
* `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - beskytter databeskyttelse for børn under 13.
* `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - giver brugerrettigheder, databeskyttelse og privatliv.
* `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) giver forbrugere flere _rettigheder_ over deres (personlige) data.
* `2021`, Kinas [Personal Information Protection Law](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) blev netop vedtaget og skaber en af de stærkeste online databeskyttelsesreguleringer i verden.

> 🚨 Den Europæiske Union definerede GDPR (General Data Protection Regulation) forbliver en af de mest indflydelsesrige databeskyttelsesreguleringer i dag. Vidste du, at den også definerer [8 brugerrettigheder](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) for at beskytte borgernes digitale privatliv og personlige data? Lær om, hvad disse er, og hvorfor de betyder noget.

### 4. Etisk Kultur

Bemærk, at der stadig er en immateriel kløft mellem _overholdelse_ (at gøre nok for at opfylde "lovens bogstav") og adressering af [systemiske problemer](https://www.coursera.org/learn/data-science-ethics/home/week/4) (som stivhed, informationsasymmetri og fordelingsmæssig uretfærdighed), der kan fremskynde våbeniseringen af AI.

Sidstnævnte kræver [samarbejdsmetoder til at definere etiske kulturer](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f), der bygger følelsesmæssige forbindelser og konsistente fælles værdier _på tværs af organisationer_ i branchen. Dette kræver mere [formaliserede dataetiske kulturer](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) i organisationer - hvilket giver _enhver_ mulighed for at [trække Andon-snoren](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (for at rejse etiske bekymringer tidligt i processen) og gøre _etiske vurderinger_ (f.eks. ved ansættelse) til et kernekriterium for teamdannelse i AI-projekter.

---
## [Quiz efter forelæsning](https://ff-quizzes.netlify.app/en/ds/quiz/3) 🎯
## Gennemgang & Selvstudie

Kurser og bøger hjælper med at forstå kerneetikbegreber og udfordringer, mens case studier og værktøjer hjælper med anvendte etiske praksisser i virkelighedsnære kontekster. Her er nogle ressourcer at starte med.
* [Maskinlæring for begyndere](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - lektion om retfærdighed fra Microsoft.
* [Principper for ansvarlig AI](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - gratis læringsforløb fra Microsoft Learn.
* [Etik og datavidenskab](https://resources.oreilly.com/examples/0636920203964) - O'Reilly EBook (M. Loukides, H. Mason m.fl.)
* [Data Science Ethics](https://www.coursera.org/learn/data-science-ethics#syllabus) - online kursus fra University of Michigan.
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - casestudier fra University of Texas.

# Opgave

[Skriv en case study om dataetik](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.