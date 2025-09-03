<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a34157cc63516eba97c89a0b2f8c3e6",
  "translation_date": "2025-09-03T21:30:27+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "no"
}
-->
# Introduksjon til Dataetikk

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Data Science Ethics - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

---

Vi er alle databorgere som lever i en verden preget av data.

Markedsanalyser viser at innen 2022 vil 1 av 3 store organisasjoner kjøpe og selge data gjennom online [markedsplasser og utvekslinger](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/). Som **apputviklere** vil vi oppleve at det blir enklere og billigere å integrere datadrevne innsikter og algoritmestyrt automatisering i daglige brukeropplevelser. Men etter hvert som AI blir mer utbredt, må vi også forstå de potensielle skadene som kan oppstå ved [våpenisering](https://www.youtube.com/watch?v=TQHs8SA1qpk) av slike algoritmer i stor skala.

Trender viser også at vi vil skape og konsumere over [180 zettabyte](https://www.statista.com/statistics/871513/worldwide-data-created/) med data innen 2025. Som **dataforskere** gir dette oss enestående tilgang til personlig data. Dette betyr at vi kan bygge atferdsprofiler av brukere og påvirke beslutningstaking på måter som skaper en [illusjon av fri vilje](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice), samtidig som vi potensielt dytter brukere mot utfall vi foretrekker. Det reiser også bredere spørsmål om databeskyttelse og brukerrettigheter.

Dataetikk er nå _nødvendige retningslinjer_ for dataforskning og ingeniørarbeid, som hjelper oss med å minimere potensielle skader og utilsiktede konsekvenser av våre datadrevne handlinger. [Gartner Hype Cycle for AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) identifiserer relevante trender innen digital etikk, ansvarlig AI og AI-styring som nøkkeldrivere for større megatrender rundt _demokratisering_ og _industrialisering_ av AI.

![Gartner's Hype Cycle for AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

I denne leksjonen skal vi utforske det fascinerende området dataetikk - fra grunnleggende konsepter og utfordringer til casestudier og anvendte AI-konsepter som styring - som hjelper med å etablere en etikkultur i team og organisasjoner som jobber med data og AI.

## [Quiz før forelesning](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## Grunnleggende definisjoner

La oss starte med å forstå grunnleggende terminologi.

Ordet "etikk" kommer fra det [greske ordet "ethikos"](https://en.wikipedia.org/wiki/Ethics) (og roten "ethos") som betyr _karakter eller moralsk natur_. 

**Etikk** handler om de delte verdiene og moralske prinsippene som styrer vår oppførsel i samfunnet. Etikk er ikke basert på lover, men på bredt aksepterte normer for hva som er "riktig vs. galt". Etiske hensyn kan imidlertid påvirke initiativer for selskapsstyring og myndighetsreguleringer som skaper flere insentiver for samsvar.

**Dataetikk** er en [ny gren av etikk](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1) som "studerer og evaluerer moralske problemer knyttet til _data, algoritmer og tilhørende praksis_". Her fokuserer **"data"** på handlinger relatert til generering, registrering, kuratering, behandling, spredning, deling og bruk, **"algoritmer"** fokuserer på AI, agenter, maskinlæring og roboter, og **"praksis"** fokuserer på temaer som ansvarlig innovasjon, programmering, hacking og etiske retningslinjer.

**Anvendt etikk** er den [praktiske anvendelsen av moralske hensyn](https://en.wikipedia.org/wiki/Applied_ethics). Det er prosessen med aktivt å undersøke etiske spørsmål i konteksten av _virkelige handlinger, produkter og prosesser_, og ta korrigerende tiltak for å sikre at disse forblir i tråd med våre definerte etiske verdier.

**Etikkultur** handler om [_operasjonalisering_ av anvendt etikk](https://hbr.org/2019/05/how-to-design-an-ethical-organization) for å sikre at våre etiske prinsipper og praksiser blir vedtatt på en konsekvent og skalerbar måte i hele organisasjonen. Vellykkede etikkulturer definerer organisasjonsomfattende etiske prinsipper, gir meningsfulle insentiver for samsvar, og forsterker etiske normer ved å oppmuntre og forsterke ønsket atferd på alle nivåer i organisasjonen.

## Etiske konsepter

I denne delen skal vi diskutere konsepter som **delte verdier** (prinsipper) og **etiske utfordringer** (problemer) for dataetikk - og utforske **casestudier** som hjelper deg med å forstå disse konseptene i virkelige kontekster.

### 1. Etiske prinsipper

Hver dataetikkstrategi begynner med å definere _etiske prinsipper_ - de "delte verdiene" som beskriver akseptabel oppførsel og veileder samsvarende handlinger i våre data- og AI-prosjekter. Du kan definere disse på individ- eller teamnivå. Imidlertid skisserer de fleste store organisasjoner disse i en _etisk AI_-misjonserklæring eller rammeverk som er definert på selskapsnivå og håndhevet konsekvent på tvers av alle team.

**Eksempel:** Microsofts [Ansvarlig AI](https://www.microsoft.com/en-us/ai/responsible-ai)-misjonserklæring lyder: _"Vi er forpliktet til å fremme AI drevet av etiske prinsipper som setter mennesker først"_ - og identifiserer 6 etiske prinsipper i rammeverket nedenfor:

![Ansvarlig AI hos Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

La oss kort utforske disse prinsippene. _Åpenhet_ og _ansvarlighet_ er grunnleggende verdier som andre prinsipper bygger på - så la oss begynne der:

* [**Ansvarlighet**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) gjør utøvere _ansvarlige_ for sine data- og AI-operasjoner, og samsvar med disse etiske prinsippene.
* [**Åpenhet**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) sikrer at data- og AI-handlinger er _forståelige_ (tolkbare) for brukere, og forklarer hva og hvorfor bak beslutninger.
* [**Rettferdighet**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - fokuserer på å sikre at AI behandler _alle mennesker_ rettferdig, og adresserer eventuelle systemiske eller implisitte sosio-tekniske skjevheter i data og systemer.
* [**Pålitelighet og sikkerhet**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - sikrer at AI oppfører seg _konsekvent_ med definerte verdier, og minimerer potensielle skader eller utilsiktede konsekvenser.
* [**Personvern og sikkerhet**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - handler om å forstå dataopprinnelse og gi _databeskyttelse og relaterte rettigheter_ til brukere.
* [**Inkludering**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - handler om å designe AI-løsninger med intensjon, og tilpasse dem for å møte et _bredt spekter av menneskelige behov_ og evner.

> 🚨 Tenk på hva din dataetikk-misjonserklæring kunne vært. Utforsk etiske AI-rammeverk fra andre organisasjoner - her er eksempler fra [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles), og [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Hvilke delte verdier har de til felles? Hvordan relaterer disse prinsippene seg til AI-produktet eller industrien de opererer i?

### 2. Etiske utfordringer

Når vi har definert etiske prinsipper, er neste steg å evaluere våre data- og AI-handlinger for å se om de samsvarer med disse delte verdiene. Tenk på handlingene dine i to kategorier: _datainnsamling_ og _algoritmedesign_. 

Ved datainnsamling vil handlingene sannsynligvis involvere **personlig data** eller personlig identifiserbar informasjon (PII) for identifiserbare levende individer. Dette inkluderer [mangfoldige elementer av ikke-personlig data](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en) som _samlet sett_ identifiserer en person. Etiske utfordringer kan relatere seg til _databeskyttelse_, _dataeierskap_, og relaterte temaer som _informert samtykke_ og _immaterielle rettigheter_ for brukere.

Ved algoritmedesign vil handlingene involvere innsamling og kuratering av **datasett**, og deretter bruke dem til å trene og distribuere **datamodeller** som forutsier utfall eller automatiserer beslutninger i virkelige kontekster. Etiske utfordringer kan oppstå fra _datasettbias_, _datakvalitetsproblemer_, _urettferdighet_, og _feilrepresentasjon_ i algoritmer - inkludert noen problemer som er systemiske i natur.

I begge tilfeller fremhever etiske utfordringer områder der våre handlinger kan komme i konflikt med våre delte verdier. For å oppdage, redusere, minimere eller eliminere disse bekymringene - må vi stille moralske "ja/nei"-spørsmål relatert til våre handlinger, og deretter ta korrigerende tiltak etter behov. La oss se på noen etiske utfordringer og de moralske spørsmålene de reiser:

#### 2.1 Dataeierskap

Datainnsamling involverer ofte personlig data som kan identifisere datasubjektene. [Dataeierskap](https://permission.io/blog/data-ownership) handler om _kontroll_ og [_brukerrettigheter_](https://permission.io/blog/data-ownership) relatert til opprettelse, behandling og spredning av data. 

De moralske spørsmålene vi må stille er: 
 * Hvem eier dataene? (bruker eller organisasjon)
 * Hvilke rettigheter har datasubjektene? (eks: tilgang, sletting, portabilitet)
 * Hvilke rettigheter har organisasjoner? (eks: rette opp skadelige brukeranmeldelser)

#### 2.2 Informert samtykke

[Informert samtykke](https://legaldictionary.net/informed-consent/) definerer handlingen der brukere samtykker til en handling (som datainnsamling) med en _full forståelse_ av relevante fakta, inkludert formål, potensielle risikoer og alternativer. 

Spørsmål å utforske her er:
 * Ga brukeren (datasubjektet) tillatelse til datainnsamling og bruk?
 * Forsto brukeren formålet med datainnsamlingen?
 * Forsto brukeren de potensielle risikoene ved deltakelsen?

#### 2.3 Immaterielle rettigheter

[Immaterielle rettigheter](https://en.wikipedia.org/wiki/Intellectual_property) refererer til immaterielle skapelser som resultat av menneskelig initiativ, som kan _ha økonomisk verdi_ for individer eller bedrifter. 

Spørsmål å utforske her er:
 * Hadde de innsamlede dataene økonomisk verdi for en bruker eller bedrift?
 * Har **brukeren** immaterielle rettigheter her?
 * Har **organisasjonen** immaterielle rettigheter her?
 * Hvis disse rettighetene eksisterer, hvordan beskytter vi dem?

#### 2.4 Databeskyttelse

[Databeskyttelse](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) eller informasjonsbeskyttelse refererer til bevaring av brukerens personvern og beskyttelse av brukerens identitet med hensyn til personlig identifiserbar informasjon. 

Spørsmål å utforske her er:
 * Er brukernes (personlige) data sikret mot hacking og lekkasjer?
 * Er brukernes data kun tilgjengelig for autoriserte brukere og kontekster?
 * Er brukernes anonymitet bevart når data deles eller spres?
 * Kan en bruker bli avidentifisert fra anonymiserte datasett?

#### 2.5 Rett til å bli glemt

[Rett til å bli glemt](https://en.wikipedia.org/wiki/Right_to_be_forgotten) eller [rett til sletting](https://www.gdpreu.org/right-to-be-forgotten/) gir ekstra beskyttelse av personlig data til brukere. Spesielt gir det brukere rett til å be om sletting eller fjerning av personlig data fra Internett-søk og andre steder, _under spesifikke omstendigheter_ - slik at de kan få en ny start online uten at tidligere handlinger holdes mot dem.

Spørsmål å utforske her er:
 * Tillater systemet datasubjekter å be om sletting?
 * Bør tilbaketrekking av brukersamtykke utløse automatisk sletting?
 * Ble data samlet inn uten samtykke eller på ulovlig vis?
 * Er vi i samsvar med myndighetsreguleringer for databeskyttelse?

#### 2.6 Datasettbias

Datasett eller [innsamlingsbias](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) handler om å velge et _ikke-representativt_ datasett for algoritmeutvikling, noe som kan skape potensielle urettferdigheter i resultatene for ulike grupper. Typer bias inkluderer utvalgsbias, frivillighetsbias og instrumentbias. 

Spørsmål å utforske her er:
 * Rekrutterte vi et representativt sett med datasubjekter?
 * Testet vi vårt innsamlede eller kuraterte datasett for ulike typer bias?
 * Kan vi redusere eller fjerne oppdagede bias?

#### 2.7 Datakvalitet

[Datakvalitet](https://lakefs.io/data-quality-testing/) ser på gyldigheten av det kuraterte datasettet som brukes til å utvikle våre algoritmer, og sjekker om funksjoner og poster oppfyller kravene til nivået av nøyaktighet og konsistens som trengs for vårt AI-formål.

Spørsmål å utforske her er:
 * Fanget vi gyldige _funksjoner_ for vår brukssak?
 * Ble data fanget _konsistent_ på tvers av ulike datakilder?
 * Er datasettet _komplett_ for ulike forhold eller scenarier?
 * Er informasjonen fanget _nøyaktig_ i å reflektere virkeligheten?

#### 2.8 Algoritme-rettferdighet
[Algorithmisk rettferdighet](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) undersøker om algoritmedesign systematisk diskriminerer spesifikke undergrupper av datasubjekter, noe som kan føre til [potensielle skader](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) innen _fordeling_ (der ressurser nektes eller holdes tilbake fra den gruppen) og _tjenestekvalitet_ (der AI ikke er like nøyaktig for noen undergrupper som for andre).

Spørsmål å utforske her er:
 * Evaluerte vi modellens nøyaktighet for ulike undergrupper og forhold?
 * Undersøkte vi systemet for potensielle skader (f.eks. stereotypier)?
 * Kan vi revidere data eller trene opp modeller på nytt for å redusere identifiserte skader?

Utforsk ressurser som [AI Fairness-sjekklister](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) for å lære mer.

#### 2.9 Feilrepresentasjon

[Feilrepresentasjon av data](https://www.sciencedirect.com/topics/computer-science/misrepresentation) handler om å spørre om vi kommuniserer innsikter fra ærlig rapporterte data på en villedende måte for å støtte en ønsket fortelling.

Spørsmål å utforske her er:
 * Rapporterer vi ufullstendige eller unøyaktige data?
 * Visualiserer vi data på en måte som fører til misvisende konklusjoner?
 * Bruker vi selektive statistiske teknikker for å manipulere resultater?
 * Finnes det alternative forklaringer som kan gi en annen konklusjon?

#### 2.10 Fri vilje
[Illusjonen av fri vilje](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) oppstår når systemets "valgarkitekturer" bruker beslutningsalgoritmer for å påvirke folk til å ta et foretrukket utfall, samtidig som det ser ut som de har alternativer og kontroll. Disse [mørke mønstrene](https://www.darkpatterns.org/) kan forårsake sosial og økonomisk skade for brukere. Fordi brukerbeslutninger påvirker atferdsprofiler, kan disse handlingene potensielt drive fremtidige valg som forsterker eller utvider virkningen av disse skadene.

Spørsmål å utforske her er:
 * Forsto brukeren konsekvensene av å ta det valget?
 * Var brukeren klar over (alternative) valg og fordeler og ulemper ved hvert?
 * Kan brukeren reversere et automatisert eller påvirket valg senere?

### 3. Casestudier

For å sette disse etiske utfordringene i virkelige kontekster, hjelper det å se på casestudier som fremhever potensielle skader og konsekvenser for enkeltpersoner og samfunn når slike etikkbrudd blir oversett.

Her er noen eksempler:

| Etisk utfordring | Casestudie  | 
|--- |--- |
| **Informert samtykke** | 1972 - [Tuskegee Syphilis Study](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Afroamerikanske menn som deltok i studien ble lovet gratis medisinsk behandling _men ble lurt_ av forskere som unnlot å informere deltakerne om diagnosen eller tilgjengelig behandling. Mange døde, og partnere eller barn ble påvirket; studien varte i 40 år. | 
| **Datapersonvern** |  2007 - [Netflix data prize](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) ga forskere _10M anonymiserte filmrangeringer fra 50K kunder_ for å forbedre anbefalingsalgoritmer. Imidlertid klarte forskere å korrelere anonymiserte data med personlig identifiserbare data i _eksterne datasett_ (f.eks. IMDb-kommentarer) - effektivt "de-anonymiserte" noen Netflix-abonnenter.|
| **Innsamlingsskjevhet**  | 2013 - Boston by [utviklet Street Bump](https://www.boston.gov/transportation/street-bump), en app som lot innbyggere rapportere hull i veien, og ga byen bedre data for å finne og fikse problemer. Imidlertid hadde [folk i lavinntektsgrupper mindre tilgang til biler og telefoner](https://hbr.org/2013/04/the-hidden-biases-in-big-data), noe som gjorde deres veiproblemer usynlige i denne appen. Utviklere samarbeidet med akademikere for å adressere _rettferdig tilgang og digitale skiller_. |
| **Algoritmisk rettferdighet**  | 2018 - MIT [Gender Shades Study](http://gendershades.org/overview.html) evaluerte nøyaktigheten til AI-produkter for kjønnsidentifikasjon, og avdekket mangler i nøyaktighet for kvinner og personer med mørk hud. Et [2019 Apple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) syntes å tilby mindre kreditt til kvinner enn menn. Begge illustrerte problemer med algoritmisk skjevhet som førte til sosioøkonomiske skader.|
| **Feilrepresentasjon av data** | 2020 - [Georgia Department of Public Health publiserte COVID-19-diagrammer](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) som syntes å villede innbyggere om trender i bekreftede tilfeller med ikke-kronologisk rekkefølge på x-aksen. Dette illustrerer feilrepresentasjon gjennom visualiseringstriks. |
| **Illusjonen av fri vilje** | 2020 - Læringsappen [ABCmouse betalte $10M for å løse en FTC-klage](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) der foreldre ble fanget i abonnementer de ikke kunne kansellere. Dette illustrerer mørke mønstre i valgarkitekturer, der brukere ble påvirket til potensielt skadelige valg. |
| **Datapersonvern og brukerrettigheter** | 2021 - Facebook [Data Breach](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) eksponerte data fra 530M brukere, noe som resulterte i et forlik på $5B med FTC. Det nektet imidlertid å varsle brukere om bruddet, og brøt brukerrettigheter rundt datatransparens og tilgang. |

Vil du utforske flere casestudier? Sjekk ut disse ressursene:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - etiske dilemmaer på tvers av ulike bransjer. 
* [Data Science Ethics course](https://www.coursera.org/learn/data-science-ethics#syllabus) - casestudier utforsket.
* [Where things have gone wrong](https://deon.drivendata.org/examples/) - deon-sjekkliste med eksempler.


> 🚨 Tenk på casestudiene du har sett - har du opplevd, eller blitt påvirket av, en lignende etisk utfordring i ditt liv? Kan du komme på minst én annen casestudie som illustrerer en av de etiske utfordringene vi har diskutert i denne seksjonen?

## Anvendt etikk

Vi har snakket om etiske konsepter, utfordringer og casestudier i virkelige kontekster. Men hvordan kommer vi i gang med å _anvende_ etiske prinsipper og praksiser i våre prosjekter? Og hvordan _operasjonaliserer_ vi disse praksisene for bedre styring? La oss utforske noen løsninger fra virkeligheten: 

### 1. Profesjonelle koder

Profesjonelle koder tilbyr en mulighet for organisasjoner til å "incentivere" medlemmer til å støtte deres etiske prinsipper og misjonserklæring. Koder er _moralske retningslinjer_ for profesjonell oppførsel, som hjelper ansatte eller medlemmer med å ta beslutninger som samsvarer med organisasjonens prinsipper. De er kun så gode som den frivillige etterlevelsen fra medlemmene; imidlertid tilbyr mange organisasjoner belønninger og straffer for å motivere etterlevelse.

Eksempler inkluderer:

 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Code of Ethics
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Code of Conduct (opprettet 2013)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (siden 1993)

> 🚨 Tilhører du en profesjonell ingeniør- eller dataorganisasjon? Utforsk deres nettsted for å se om de definerer en profesjonell etisk kode. Hva sier dette om deres etiske prinsipper? Hvordan "incentiverer" de medlemmene til å følge koden?

### 2. Etiske sjekklister

Mens profesjonelle koder definerer nødvendig _etisk oppførsel_ fra utøvere, har de [kjente begrensninger](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) i håndheving, spesielt i storskala prosjekter. I stedet anbefaler mange dataeksperter [sjekklister](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), som kan **koble prinsipper til praksis** på mer deterministiske og handlingsrettede måter.

Sjekklister konverterer spørsmål til "ja/nei"-oppgaver som kan operasjonaliseres, slik at de kan spores som en del av standard produktutgivelsesarbeidsflyter.

Eksempler inkluderer:
 * [Deon](https://deon.drivendata.org/) - en generell sjekkliste for dataetikk opprettet fra [industrianbefalinger](https://deon.drivendata.org/#checklist-citations) med et kommandolinjeverktøy for enkel integrering.
 * [Privacy Audit Checklist](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - gir generell veiledning for informasjonsbehandlingspraksis fra juridiske og sosiale eksponeringsperspektiver.
 * [AI Fairness Checklist](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - opprettet av AI-utøvere for å støtte adopsjon og integrering av rettferdighetssjekker i AI-utviklingssykluser.
 * [22 spørsmål for etikk i data og AI](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - en mer åpen rammeverk, strukturert for innledende utforskning av etiske spørsmål i design, implementering og organisatoriske kontekster.

### 3. Etiske reguleringer

Etikk handler om å definere felles verdier og gjøre det rette _frivillig_. **Etterlevelse** handler om _å følge loven_ der den er definert. **Styring** dekker bredt alle måter organisasjoner opererer for å håndheve etiske prinsipper og overholde etablerte lover.

I dag tar styring to former innen organisasjoner. For det første handler det om å definere **etiske AI**-prinsipper og etablere praksiser for å operasjonalisere adopsjon på tvers av alle AI-relaterte prosjekter i organisasjonen. For det andre handler det om å overholde alle myndighetsmandaterte **databeskyttelsesreguleringer** for regionene de opererer i.

Eksempler på databeskyttelse og personvernreguleringer:

 * `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - regulerer _føderal regjering_ sin innsamling, bruk og offentliggjøring av personlig informasjon.
 * `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - beskytter personlig helsedata.
 * `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - beskytter dataprivacy for barn under 13 år.
 * `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - gir brukerrettigheter, databeskyttelse og personvern.
 * `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) gir forbrukere flere _rettigheter_ over deres (personlige) data.
 * `2021`, Kinas [Personal Information Protection Law](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) ble nettopp vedtatt, og skaper en av de sterkeste online dataprivacy-reguleringene i verden.

> 🚨 Den europeiske unionens GDPR (General Data Protection Regulation) forblir en av de mest innflytelsesrike dataprivacy-reguleringene i dag. Visste du at den også definerer [8 brukerrettigheter](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) for å beskytte borgernes digitale personvern og personlige data? Lær om hva disse er, og hvorfor de er viktige.


### 4. Etisk kultur

Merk at det fortsatt er et immaterielt gap mellom _etterlevelse_ (å gjøre nok for å møte "lovens bokstav") og å adressere [systemiske problemer](https://www.coursera.org/learn/data-science-ethics/home/week/4) (som ossifikasjon, informasjonsasymmetri og distribusjonsurettferdighet) som kan akselerere våpeniseringen av AI.

Det sistnevnte krever [samarbeidende tilnærminger for å definere etiske kulturer](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f) som bygger emosjonelle forbindelser og konsistente felles verdier _på tvers av organisasjoner_ i bransjen. Dette krever mer [formaliserte dataetiske kulturer](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) i organisasjoner - som lar _hvem som helst_ [trekke Andon-snoren](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (for å reise etiske bekymringer tidlig i prosessen) og gjøre _etiske vurderinger_ (f.eks. ved ansettelser) til et kjernekrav for teamdannelse i AI-prosjekter.

---
## [Quiz etter forelesning](https://ff-quizzes.netlify.app/en/ds/) 🎯
## Gjennomgang og selvstudium 

Kurs og bøker hjelper med å forstå kjernebegreper og utfordringer innen etikk, mens casestudier og verktøy hjelper med anvendt etikk i virkelige kontekster. Her er noen ressurser for å komme i gang.

* [Machine Learning For Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - leksjon om rettferdighet, fra Microsoft.
* [Prinsipper for ansvarlig AI](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - gratis læringssti fra Microsoft Learn.
* [Etikk og datavitenskap](https://resources.oreilly.com/examples/0636920203964) - O'Reilly EBook (M. Loukides, H. Mason m.fl.)
* [Etikk innen datavitenskap](https://www.coursera.org/learn/data-science-ethics#syllabus) - nettkurs fra University of Michigan.
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - casestudier fra University of Texas.

# Oppgave

[Skriv en casestudie om dataetikk](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.