<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8796f41f566a0a8ebb72863a83d558ed",
  "translation_date": "2025-08-26T21:22:22+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "da"
}
-->
# Introduktion til Dataetik

|![ Sketchnote af [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Data Science Ethics - _Sketchnote af [@nitya](https://twitter.com/nitya)_ |

---

Vi er alle databorger i en verden præget af data.

Markedsanalyser viser, at i 2022 vil 1 ud af 3 store organisationer købe og sælge deres data via online [markedspladser og børser](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/). Som **appudviklere** vil vi opleve, at det bliver lettere og billigere at integrere datadrevne indsigter og algoritmestyret automatisering i daglige brugeroplevelser. Men efterhånden som AI bliver allestedsnærværende, skal vi også forstå de potentielle skader, der kan opstå ved [våbenisering](https://www.youtube.com/watch?v=TQHs8SA1qpk) af sådanne algoritmer i stor skala.

Tendenser viser også, at vi vil skabe og forbruge over [180 zettabytes](https://www.statista.com/statistics/871513/worldwide-data-created/) data inden 2025. Som **dataspecialister** giver dette os en hidtil uset adgang til personlige data. Det betyder, at vi kan opbygge adfærdsprofiler af brugere og påvirke beslutningstagning på måder, der skaber en [illusion af frit valg](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice), mens vi potentielt skubber brugere mod resultater, vi foretrækker. Det rejser også bredere spørgsmål om databeskyttelse og brugerrettigheder.

Dataetik er nu _nødvendige retningslinjer_ for datavidenskab og -teknik, der hjælper os med at minimere potentielle skader og utilsigtede konsekvenser af vores datadrevne handlinger. [Gartner Hype Cycle for AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) identificerer relevante tendenser inden for digital etik, ansvarlig AI og AI-styring som nøglefaktorer for større megatrends omkring _demokratisering_ og _industrialisering_ af AI.

![Gartner's Hype Cycle for AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

I denne lektion vil vi udforske det fascinerende område dataetik - fra kernekoncepter og udfordringer til casestudier og anvendte AI-koncepter som styring - der hjælper med at etablere en etik-kultur i teams og organisationer, der arbejder med data og AI.

## [Quiz før lektionen](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## Grundlæggende Definitioner

Lad os starte med at forstå den grundlæggende terminologi.

Ordet "etik" stammer fra det [græske ord "ethikos"](https://en.wikipedia.org/wiki/Ethics) (og dets rod "ethos"), der betyder _karakter eller moralsk natur_. 

**Etik** handler om de fælles værdier og moralske principper, der styrer vores adfærd i samfundet. Etik er ikke baseret på love, men på bredt accepterede normer for, hvad der er "rigtigt vs. forkert". Dog kan etiske overvejelser påvirke virksomhedsledelse og regeringsreguleringer, der skaber flere incitamenter til overholdelse.

**Dataetik** er en [ny gren af etik](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1), der "undersøger og evaluerer moralske problemer relateret til _data, algoritmer og tilsvarende praksis_". Her fokuserer **"data"** på handlinger relateret til generering, registrering, kuratering, behandling, formidling, deling og brug, **"algoritmer"** på AI, agenter, maskinlæring og robotter, og **"praksis"** på emner som ansvarlig innovation, programmering, hacking og etiske kodekser.

**Anvendt etik** er den [praktiske anvendelse af moralske overvejelser](https://en.wikipedia.org/wiki/Applied_ethics). Det er processen med aktivt at undersøge etiske spørgsmål i konteksten af _virkelige handlinger, produkter og processer_ og tage korrigerende foranstaltninger for at sikre, at disse forbliver i overensstemmelse med vores definerede etiske værdier.

**Etik-kultur** handler om [_at operationalisere_ anvendt etik](https://hbr.org/2019/05/how-to-design-an-ethical-organization) for at sikre, at vores etiske principper og praksisser bliver vedtaget på en konsekvent og skalerbar måde i hele organisationen. Succesfulde etik-kulturer definerer organisationens etiske principper, giver meningsfulde incitamenter til overholdelse og forstærker etiske normer ved at opmuntre og fremhæve ønsket adfærd på alle niveauer i organisationen.

## Etiske Koncepter

I denne sektion vil vi diskutere koncepter som **fælles værdier** (principper) og **etiske udfordringer** (problemer) for dataetik - og udforske **casestudier**, der hjælper dig med at forstå disse koncepter i virkelige kontekster.

### 1. Etiske Principper

Enhver dataetikstrategi begynder med at definere _etiske principper_ - de "fælles værdier", der beskriver acceptabel adfærd og guider overholdelse i vores data- og AI-projekter. Du kan definere disse på individuelt eller teamniveau. Dog skitserer de fleste store organisationer disse i en _etisk AI_-missionserklæring eller ramme, der er defineret på virksomhedsniveau og konsekvent håndhævet på tværs af alle teams.

**Eksempel:** Microsofts [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai)-missionserklæring lyder: _"Vi er forpligtet til at fremme AI drevet af etiske principper, der sætter mennesker først"_ - og identificerer 6 etiske principper i nedenstående ramme:

![Responsible AI hos Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Lad os kort udforske disse principper. _Gennemsigtighed_ og _ansvarlighed_ er grundlæggende værdier, som de andre principper bygger på - så lad os starte der:

* [**Ansvarlighed**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) gør praktikere _ansvarlige_ for deres data- og AI-operationer og overholdelse af disse etiske principper.
* [**Gennemsigtighed**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) sikrer, at data- og AI-handlinger er _forståelige_ (fortolkelige) for brugere og forklarer hvad og hvorfor bag beslutninger.
* [**Retfærdighed**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) fokuserer på at sikre, at AI behandler _alle mennesker_ retfærdigt og adresserer eventuelle systemiske eller implicitte socio-tekniske skævheder i data og systemer.
* [**Pålidelighed & Sikkerhed**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) sikrer, at AI opfører sig _konsekvent_ med definerede værdier og minimerer potentielle skader eller utilsigtede konsekvenser.
* [**Privatliv & Sikkerhed**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) handler om at forstå dataens oprindelse og give _databeskyttelse og relaterede rettigheder_ til brugere.
* [**Inklusion**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) handler om at designe AI-løsninger med intention og tilpasse dem til at imødekomme et _bredt spektrum af menneskelige behov_ og evner.

> 🚨 Overvej, hvad din dataetik-missionserklæring kunne være. Udforsk etiske AI-rammer fra andre organisationer - her er eksempler fra [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles) og [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Hvilke fælles værdier har de? Hvordan relaterer disse principper sig til de AI-produkter eller industrier, de opererer i?

### 2. Etiske Udfordringer

Når vi har defineret etiske principper, er næste skridt at evaluere vores data- og AI-handlinger for at se, om de stemmer overens med disse fælles værdier. Tænk på dine handlinger i to kategorier: _datainnsamling_ og _algoritmedesign_. 

Ved datainnsamling vil handlinger sandsynligvis involvere **personlige data** eller personligt identificerbare oplysninger (PII) for identificerbare levende individer. Dette inkluderer [forskellige typer ikke-personlige data](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en), der _samlet set_ kan identificere en person. Etiske udfordringer kan relateres til _databeskyttelse_, _dataejerskab_ og relaterede emner som _informeret samtykke_ og _intellektuelle ejendomsrettigheder_ for brugere.

Ved algoritmedesign vil handlinger involvere indsamling og kuratering af **datasæt**, som derefter bruges til at træne og implementere **datamodeller**, der forudsiger resultater eller automatiserer beslutninger i virkelige kontekster. Etiske udfordringer kan opstå fra _datasæt-skævhed_, _datakvalitetsproblemer_, _uretfærdighed_ og _fejlrepræsentation_ i algoritmer - inklusive nogle problemer, der er systemiske af natur.

I begge tilfælde fremhæver etiske udfordringer områder, hvor vores handlinger kan komme i konflikt med vores fælles værdier. For at opdage, afbøde, minimere eller eliminere disse bekymringer skal vi stille moralske "ja/nej"-spørgsmål relateret til vores handlinger og derefter tage korrigerende handlinger efter behov. Lad os se på nogle etiske udfordringer og de moralske spørgsmål, de rejser:

#### 2.1 Dataejerskab

Datainnsamling involverer ofte personlige data, der kan identificere datasubjekterne. [Dataejerskab](https://permission.io/blog/data-ownership) handler om _kontrol_ og [_brugernes rettigheder_](https://permission.io/blog/data-ownership) i forhold til oprettelse, behandling og formidling af data. 

De moralske spørgsmål, vi skal stille, er: 
 * Hvem ejer dataene? (brugeren eller organisationen)
 * Hvilke rettigheder har datasubjekterne? (fx adgang, sletning, portabilitet)
 * Hvilke rettigheder har organisationer? (fx rette ondsindede brugeranmeldelser)

#### 2.2 Informeret Samtykke

[Informeret samtykke](https://legaldictionary.net/informed-consent/) definerer handlingen, hvor brugere accepterer en handling (som datainnsamling) med en _fuld forståelse_ af relevante fakta, herunder formål, potentielle risici og alternativer. 

Spørgsmål at udforske her er:
 * Gav brugeren (datasubjektet) tilladelse til dataindsamling og brug?
 * Forstod brugeren formålet med, at dataene blev indsamlet?
 * Forstod brugeren de potentielle risici ved deres deltagelse?

#### 2.3 Intellektuel Ejendomsret

[Intellektuel ejendomsret](https://en.wikipedia.org/wiki/Intellectual_property) refererer til immaterielle skabelser, der kan _have økonomisk værdi_ for individer eller virksomheder. 

Spørgsmål at udforske her er:
 * Havde de indsamlede data økonomisk værdi for en bruger eller virksomhed?
 * Har **brugeren** intellektuel ejendomsret her?
 * Har **organisationen** intellektuel ejendomsret her?
 * Hvis disse rettigheder eksisterer, hvordan beskytter vi dem?

#### 2.4 Databeskyttelse

[Databeskyttelse](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) eller informationsbeskyttelse refererer til bevarelse af brugerens privatliv og beskyttelse af brugerens identitet i forhold til personligt identificerbare oplysninger. 

Spørgsmål at udforske her er:
 * Er brugernes (personlige) data sikret mod hacking og lækager?
 * Er brugernes data kun tilgængelige for autoriserede brugere og kontekster?
 * Bevares brugernes anonymitet, når data deles eller formidles?
 * Kan en bruger blive de-identificeret fra anonymiserede datasæt?

#### 2.5 Retten til at Blive Glemt

[Retten til at blive glemt](https://en.wikipedia.org/wiki/Right_to_be_forgotten) eller [retten til sletning](https://www.gdpreu.org/right-to-be-forgotten/) giver yderligere beskyttelse af personlige data til brugere. Specifikt giver det brugere ret til at anmode om sletning eller fjernelse af personlige data fra internetsøgninger og andre steder, _under specifikke omstændigheder_ - hvilket giver dem en ny start online uden tidligere handlinger, der holdes imod dem.

Spørgsmål at udforske her er:
 * Tillader systemet datasubjekter at anmode om sletning?
 * Skal tilbagetrækning af brugerens samtykke udløse automatisk sletning?
 * Blev data indsamlet uden samtykke eller på ulovlig vis?
 * Overholder vi regeringsregler for databeskyttelse?

#### 2.6 Datasæt-skævhed

Datasæt- eller [indsamlingsskævhed](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) handler om at vælge et _ikke-repræsentativt_ datasæt til algoritmeudvikling, hvilket skaber potentiel uretfærdighed i resultatet for forskellige grupper. Typer af skævhed inkluderer udvælgelses- eller stikprøveskævhed, frivillighedsskævhed og instrumentel skævhed. 

Spørgsmål at udforske her er:
 * Rekrutterede vi et repræsentativt sæt datasubjekter?
 * Testede vi vores indsamlede eller kuraterede datasæt for forskellige skævheder?
 * Kan vi afbøde eller fjerne eventuelle opdagede skævheder?

#### 2.7 Datakvalitet

[Datakvalitet](https://lakefs.io/data-quality-testing/) ser på gyldigheden af det kuraterede datasæt, der bruges til at udvikle vores algoritmer, og kontrollerer, om funktioner og poster opfylder kravene til det niveau af nøjagtighed og konsistens, der er nødvendigt for vores AI-formål.

Spørgsmål at udforske her er:
 * Indfangede vi gyldige _funktioner_ til vores brugssag?
 * Blev data indsamlet _konsekvent_ på tværs af forskellige datakilder?
 * Er datasættet _komplet_ for forskellige forhold eller scenarier?
 * Er information indfanget _nøjagtigt_ i forhold til virkeligheden?

#### 2.8 Algoritme-retfærdighed
[Algorithmisk retfærdighed](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) undersøger, om algoritmedesign systematisk diskriminerer specifikke undergrupper af datasubjekter, hvilket kan føre til [potentielle skader](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) inden for _fordeling_ (hvor ressourcer nægtes eller tilbageholdes fra den gruppe) og _kvaliteten af service_ (hvor AI ikke er lige så præcis for nogle undergrupper som for andre).

Spørgsmål, der kan udforskes her, er:
 * Evaluerede vi modelpræcision for forskellige undergrupper og forhold?
 * Undersøgte vi systemet for potentielle skader (f.eks. stereotyper)?
 * Kan vi revidere data eller genoptræne modeller for at afhjælpe identificerede skader?

Udforsk ressourcer som [AI Fairness-tjeklister](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) for at lære mere.

#### 2.9 Fejlrepræsentation

[Datafejlrepræsentation](https://www.sciencedirect.com/topics/computer-science/misrepresentation) handler om at spørge, om vi kommunikerer indsigt fra ærligt rapporterede data på en vildledende måde for at understøtte en ønsket fortælling.

Spørgsmål, der kan udforskes her, er:
 * Rapporterer vi ufuldstændige eller unøjagtige data?
 * Visualiserer vi data på en måde, der fører til vildledende konklusioner?
 * Bruger vi selektive statistiske teknikker til at manipulere resultater?
 * Er der alternative forklaringer, der kan give en anden konklusion?

#### 2.10 Fri vilje
[Illusionen af fri vilje](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) opstår, når systemets "valgarkitekturer" bruger beslutningsalgoritmer til at skubbe folk mod at tage et foretrukket resultat, mens det ser ud som om, de har valgmuligheder og kontrol. Disse [mørke mønstre](https://www.darkpatterns.org/) kan forårsage sociale og økonomiske skader for brugere. Fordi brugerbeslutninger påvirker adfærdsprofiler, kan disse handlinger potentielt drive fremtidige valg, der kan forstærke eller udvide virkningen af disse skader.

Spørgsmål, der kan udforskes her, er:
 * Forstod brugeren konsekvenserne af at træffe det valg?
 * Var brugeren opmærksom på (alternative) valg og fordele & ulemper ved hver?
 * Kan brugeren senere fortryde et automatiseret eller påvirket valg?

### 3. Case-studier

For at sætte disse etiske udfordringer i virkelige kontekster hjælper det at se på case-studier, der fremhæver de potentielle skader og konsekvenser for individer og samfund, når sådanne etiske overtrædelser overses.

Her er nogle eksempler:

| Etisk udfordring | Case-studie  | 
|--- |--- |
| **Informeret samtykke** | 1972 - [Tuskegee Syphilis Study](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Afroamerikanske mænd, der deltog i undersøgelsen, blev lovet gratis lægehjælp _men blev bedraget_ af forskere, der undlod at informere dem om deres diagnose eller om tilgængelig behandling. Mange døde, og partnere eller børn blev påvirket; undersøgelsen varede i 40 år. | 
| **Databeskyttelse** |  2007 - [Netflix data prize](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) gav forskere _10M anonymiserede filmvurderinger fra 50K kunder_ for at hjælpe med at forbedre anbefalingsalgoritmer. Forskere kunne dog korrelere anonymiserede data med personligt identificerbare data i _eksterne datasæt_ (f.eks. IMDb-kommentarer) - effektivt "de-anonymiserende" nogle Netflix-abonnenter.|
| **Indsamlingsbias**  | 2013 - Boston City [udviklede Street Bump](https://www.boston.gov/transportation/street-bump), en app, der lod borgere rapportere huller i vejen, hvilket gav byen bedre data til at finde og løse problemer. Dog havde [folk i lavindkomstgrupper mindre adgang til biler og telefoner](https://hbr.org/2013/04/the-hidden-biases-in-big-data), hvilket gjorde deres vejproblemer usynlige i denne app. Udviklere arbejdede med akademikere for at løse _lighed i adgang og digitale skel_ for retfærdighed. |
| **Algoritmisk retfærdighed**  | 2018 - MIT [Gender Shades Study](http://gendershades.org/overview.html) evaluerede nøjagtigheden af AI-produkter til kønsidentifikation og afslørede mangler i nøjagtighed for kvinder og farvede personer. Et [2019 Apple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) syntes at tilbyde mindre kredit til kvinder end mænd. Begge illustrerede problemer med algoritmisk bias, der førte til socioøkonomiske skader.|
| **Datafejlrepræsentation** | 2020 - [Georgia Department of Public Health udgav COVID-19-diagrammer](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening), der syntes at vildlede borgere om tendenser i bekræftede tilfælde med ikke-kronologisk rækkefølge på x-aksen. Dette illustrerer fejlrepræsentation gennem visualiseringstricks. |
| **Illusionen af fri vilje** | 2020 - Læringsappen [ABCmouse betalte $10M for at løse en FTC-klage](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/), hvor forældre blev fanget i at betale for abonnementer, de ikke kunne annullere. Dette illustrerer mørke mønstre i valgarkitekturer, hvor brugere blev skubbet mod potentielt skadelige valg. |
| **Databeskyttelse & brugerrettigheder** | 2021 - Facebook [Data Breach](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) afslørede data fra 530M brugere, hvilket resulterede i en $5B forlig med FTC. Det nægtede dog at informere brugere om bruddet og overtrådte brugerrettigheder omkring datatransparens og adgang. |

Vil du udforske flere case-studier? Tjek disse ressourcer:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - etiske dilemmaer på tværs af forskellige industrier. 
* [Data Science Ethics course](https://www.coursera.org/learn/data-science-ethics#syllabus) - landmark case-studier udforsket.
* [Where things have gone wrong](https://deon.drivendata.org/examples/) - deon-tjekliste med eksempler.

> 🚨 Tænk over de case-studier, du har set - har du oplevet eller været påvirket af en lignende etisk udfordring i dit liv? Kan du tænke på mindst én anden case-studie, der illustrerer en af de etiske udfordringer, vi har diskuteret i dette afsnit?

## Anvendt etik

Vi har talt om etiske begreber, udfordringer og case-studier i virkelige kontekster. Men hvordan kommer vi i gang med at _anvende_ etiske principper og praksisser i vores projekter? Og hvordan _operationaliserer_ vi disse praksisser for bedre styring? Lad os udforske nogle løsninger fra den virkelige verden:

### 1. Professionelle kodekser

Professionelle kodekser tilbyder en mulighed for organisationer til at "incitamentere" medlemmer til at støtte deres etiske principper og mission. Kodekser er _moralske retningslinjer_ for professionel adfærd, der hjælper medarbejdere eller medlemmer med at træffe beslutninger, der stemmer overens med organisationens principper. De er kun så gode som den frivillige overholdelse fra medlemmer; dog tilbyder mange organisationer yderligere belønninger og sanktioner for at motivere overholdelse.

Eksempler inkluderer:

 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Code of Ethics
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Code of Conduct (oprettet 2013)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (siden 1993)

> 🚨 Tilhører du en professionel ingeniør- eller data science-organisation? Udforsk deres hjemmeside for at se, om de definerer en professionel etisk kodeks. Hvad siger dette om deres etiske principper? Hvordan "incitamenterer" de medlemmer til at følge kodeksen?

### 2. Etiske tjeklister

Mens professionelle kodekser definerer krævet _etisk adfærd_ fra praktikere, har de [kendte begrænsninger](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) i håndhævelse, især i storskala projekter. I stedet anbefaler mange data science-eksperter [tjeklister](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), der kan **forbinde principper med praksis** på mere deterministiske og handlingsorienterede måder.

Tjeklister konverterer spørgsmål til "ja/nej"-opgaver, der kan operationaliseres, hvilket gør det muligt at spore dem som en del af standard produktudgivelsesarbejdsgange.

Eksempler inkluderer:
 * [Deon](https://deon.drivendata.org/) - en generel dataetisk tjekliste oprettet fra [brancheanbefalinger](https://deon.drivendata.org/#checklist-citations) med et kommandolinjeværktøj for nem integration.
 * [Privacy Audit Checklist](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - giver generel vejledning til informationshåndteringspraksis fra juridiske og sociale eksponeringsperspektiver.
 * [AI Fairness Checklist](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - oprettet af AI-praktikere for at støtte adoption og integration af fairness-tjek i AI-udviklingscyklusser.
 * [22 spørgsmål om etik i data og AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - en mere åben ramme, struktureret til indledende udforskning af etiske spørgsmål i design, implementering og organisatoriske kontekster.

### 3. Etiske reguleringer

Etik handler om at definere fælles værdier og gøre det rigtige _frivilligt_. **Overholdelse** handler om _at følge loven_, hvis og hvor den er defineret. **Styring** dækker bredt alle de måder, hvorpå organisationer opererer for at håndhæve etiske principper og overholde etablerede love.

I dag tager styring to former inden for organisationer. For det første handler det om at definere **etiske AI**-principper og etablere praksisser for at operationalisere adoption på tværs af alle AI-relaterede projekter i organisationen. For det andet handler det om at overholde alle regeringsmandaterede **databeskyttelsesreguleringer** for de regioner, den opererer i.

Eksempler på databeskyttelses- og privatlivsreguleringer:

 * `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - regulerer _føderal regeringens_ indsamling, brug og offentliggørelse af personlige oplysninger.
 * `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - beskytter personlige sundhedsdata.
 * `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - beskytter dataprivacy for børn under 13.
 * `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - giver brugerrettigheder, databeskyttelse og privatliv.
 * `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) giver forbrugere flere _rettigheder_ over deres (personlige) data.
 * `2021`, Kinas [Personal Information Protection Law](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) blev netop vedtaget og skaber en af de stærkeste online databeskyttelsesreguleringer i verden.

> 🚨 Den Europæiske Union definerede GDPR (General Data Protection Regulation) forbliver en af de mest indflydelsesrige databeskyttelsesreguleringer i dag. Vidste du, at den også definerer [8 brugerrettigheder](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) for at beskytte borgernes digitale privatliv og personlige data? Lær om, hvad disse er, og hvorfor de betyder noget.

### 4. Etisk kultur

Bemærk, at der stadig er en uhåndgribelig kløft mellem _overholdelse_ (at gøre nok for at opfylde "lovens bogstav") og adressering af [systemiske problemer](https://www.coursera.org/learn/data-science-ethics/home/week/4) (som stivhed, informationsasymmetri og fordelingsmæssig uretfærdighed), der kan fremskynde våbeniseringen af AI.

Sidstnævnte kræver [samarbejdsmetoder til at definere etiske kulturer](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f), der bygger følelsesmæssige forbindelser og konsistente fælles værdier _på tværs af organisationer_ i branchen. Dette kalder på mere [formaliserede dataetiske kulturer](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) i organisationer - hvilket giver _enhver_ mulighed for at [trække Andon-snoren](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (for at rejse etiske bekymringer tidligt i processen) og gøre _etiske vurderinger_ (f.eks. ved ansættelse) til et kernekriterium for teamdannelse i AI-projekter.

---
## [Quiz efter forelæsning](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/3) 🎯
## Gennemgang & Selvstudie 

Kurser og bøger hjælper med at forstå kerneetikbegreber og udfordringer, mens case-studier og værktøjer hjælper med anvendte etiske praksisser i virkelige kontekster. Her er nogle ressourcer at starte med.

* [Machine Learning For Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - lektion om retfærdighed, fra Microsoft.
* [Principper for ansvarlig AI](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - gratis læringsforløb fra Microsoft Learn.
* [Etik og Data Science](https://resources.oreilly.com/examples/0636920203964) - O'Reilly EBook (M. Loukides, H. Mason m.fl.)
* [Data Science Etik](https://www.coursera.org/learn/data-science-ethics#syllabus) - online kursus fra University of Michigan.
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - casestudier fra University of Texas.

# Opgave 

[Skriv en case study om dataetik](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.