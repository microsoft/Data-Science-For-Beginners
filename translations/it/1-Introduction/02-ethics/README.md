<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a34157cc63516eba97c89a0b2f8c3e6",
  "translation_date": "2025-09-03T21:18:02+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "it"
}
-->
# Introduzione all'etica dei dati

|![ Sketchnote di [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Etica della scienza dei dati - _Sketchnote di [@nitya](https://twitter.com/nitya)_ |

---

Siamo tutti cittadini dei dati che vivono in un mondo dataficato.

Le tendenze di mercato ci dicono che entro il 2022, 1 organizzazione su 3 di grandi dimensioni comprerà e venderà i propri dati attraverso [Marketplace e Exchange](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/) online. Come **sviluppatori di app**, sarà più facile ed economico integrare intuizioni basate sui dati e automazione guidata da algoritmi nelle esperienze quotidiane degli utenti. Ma con l'AI che diventa sempre più pervasiva, sarà anche necessario comprendere i potenziali danni causati dalla [strumentalizzazione](https://www.youtube.com/watch?v=TQHs8SA1qpk) di tali algoritmi su larga scala.

Le tendenze indicano inoltre che entro il 2025 creeremo e consumeremo oltre [180 zettabyte](https://www.statista.com/statistics/871513/worldwide-data-created/) di dati. Come **data scientist**, questo ci offre livelli senza precedenti di accesso ai dati personali. Ciò significa che possiamo costruire profili comportamentali degli utenti e influenzare il processo decisionale in modi che creano un'[illusione di scelta libera](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice), spingendo potenzialmente gli utenti verso risultati che preferiamo. Questo solleva anche questioni più ampie sulla privacy dei dati e sulla protezione degli utenti.

L'etica dei dati è ora _un binario necessario_ per la scienza e l'ingegneria dei dati, aiutandoci a minimizzare i potenziali danni e le conseguenze indesiderate delle nostre azioni guidate dai dati. Il [Gartner Hype Cycle per l'AI](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) identifica tendenze rilevanti in etica digitale, AI responsabile e governance dell'AI come fattori chiave per megatrend più ampi legati alla _democratizzazione_ e _industrializzazione_ dell'AI.

![Gartner's Hype Cycle per l'AI - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

In questa lezione, esploreremo l'affascinante area dell'etica dei dati - dai concetti fondamentali e sfide, agli studi di caso e ai concetti applicati di AI come la governance - che aiutano a stabilire una cultura etica nei team e nelle organizzazioni che lavorano con dati e AI.

## [Quiz pre-lezione](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## Definizioni di base

Iniziamo comprendendo la terminologia di base.

La parola "etica" deriva dalla [parola greca "ethikos"](https://en.wikipedia.org/wiki/Ethics) (e dalla sua radice "ethos") che significa _carattere o natura morale_. 

**Etica** riguarda i valori condivisi e i principi morali che governano il nostro comportamento nella società. L'etica non si basa su leggi, ma su norme ampiamente accettate di ciò che è "giusto vs. sbagliato". Tuttavia, le considerazioni etiche possono influenzare le iniziative di governance aziendale e le regolamentazioni governative che creano maggiori incentivi per la conformità.

**Etica dei dati** è un [nuovo ramo dell'etica](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1) che "studia e valuta i problemi morali legati a _dati, algoritmi e pratiche corrispondenti_". Qui, **"dati"** si concentra sulle azioni relative alla generazione, registrazione, cura, elaborazione, diffusione, condivisione e utilizzo, **"algoritmi"** si concentra su AI, agenti, machine learning e robot, e **"pratiche"** si concentra su argomenti come innovazione responsabile, programmazione, hacking e codici etici.

**Etica applicata** è l'[applicazione pratica delle considerazioni morali](https://en.wikipedia.org/wiki/Applied_ethics). È il processo di indagare attivamente le questioni etiche nel contesto di _azioni, prodotti e processi reali_, e di adottare misure correttive per garantire che rimangano allineati ai nostri valori etici definiti.

**Cultura etica** riguarda [_operazionalizzare_ l'etica applicata](https://hbr.org/2019/05/how-to-design-an-ethical-organization) per garantire che i nostri principi e pratiche etiche siano adottati in modo coerente e scalabile in tutta l'organizzazione. Le culture etiche di successo definiscono principi etici a livello organizzativo, forniscono incentivi significativi per la conformità e rafforzano le norme etiche incoraggiando e amplificando i comportamenti desiderati a ogni livello dell'organizzazione.

## Concetti di etica

In questa sezione, discuteremo concetti come **valori condivisi** (principi) e **sfide etiche** (problemi) per l'etica dei dati - ed esploreremo **studi di caso** che ti aiutano a comprendere questi concetti in contesti reali.

### 1. Principi etici

Ogni strategia di etica dei dati inizia definendo _principi etici_ - i "valori condivisi" che descrivono comportamenti accettabili e guidano azioni conformi nei nostri progetti di dati e AI. Puoi definirli a livello individuale o di team. Tuttavia, la maggior parte delle grandi organizzazioni li delinea in una dichiarazione di missione o quadro di _AI etica_ definita a livello aziendale e applicata in modo coerente in tutti i team.

**Esempio:** La dichiarazione di missione di [AI responsabile](https://www.microsoft.com/en-us/ai/responsible-ai) di Microsoft recita: _"Siamo impegnati nell'avanzamento dell'AI guidata da principi etici che mettono le persone al primo posto"_ - identificando 6 principi etici nel quadro seguente:

![AI responsabile in Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Esploriamo brevemente questi principi. _Trasparenza_ e _responsabilità_ sono valori fondamentali su cui si basano gli altri principi - quindi iniziamo da lì:

* [**Responsabilità**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) rende i professionisti _responsabili_ delle loro operazioni di dati e AI e della conformità a questi principi etici.
* [**Trasparenza**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) garantisce che le azioni di dati e AI siano _comprensibili_ (interpretabili) per gli utenti, spiegando il cosa e il perché delle decisioni.
* [**Equità**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - si concentra sull'assicurare che l'AI tratti _tutte le persone_ in modo equo, affrontando eventuali pregiudizi socio-tecnici sistemici o impliciti nei dati e nei sistemi.
* [**Affidabilità e sicurezza**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - garantisce che l'AI si comporti _coerentemente_ con i valori definiti, minimizzando i potenziali danni o conseguenze indesiderate.
* [**Privacy e sicurezza**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - riguarda la comprensione della provenienza dei dati e la fornitura di _privacy dei dati e protezioni correlate_ agli utenti.
* [**Inclusività**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - riguarda la progettazione di soluzioni AI con intenzione, adattandole per soddisfare una _ampia gamma di esigenze e capacità umane_.

> 🚨 Pensa a quale potrebbe essere la tua dichiarazione di missione per l'etica dei dati. Esplora i quadri di AI etica di altre organizzazioni - ecco esempi da [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles) e [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Quali valori condivisi hanno in comune? Come si relazionano questi principi al prodotto AI o al settore in cui operano?

### 2. Sfide etiche

Una volta definiti i principi etici, il passo successivo è valutare le nostre azioni di dati e AI per vedere se sono allineate a quei valori condivisi. Pensa alle tue azioni in due categorie: _raccolta dati_ e _progettazione algoritmica_. 

Con la raccolta dati, le azioni probabilmente coinvolgeranno **dati personali** o informazioni personali identificabili (PII) per individui identificabili. Questo include [diversi elementi di dati non personali](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en) che _collettivamente_ identificano un individuo. Le sfide etiche possono riguardare _privacy dei dati_, _proprietà dei dati_ e argomenti correlati come _consenso informato_ e _diritti di proprietà intellettuale_ per gli utenti.

Con la progettazione algoritmica, le azioni coinvolgeranno la raccolta e la cura di **dataset**, quindi il loro utilizzo per addestrare e distribuire **modelli di dati** che prevedono risultati o automatizzano decisioni in contesti reali. Le sfide etiche possono derivare da _pregiudizi nei dataset_, problemi di _qualità dei dati_, _iniquità_ e _rappresentazione errata_ negli algoritmi - inclusi alcuni problemi che sono sistemici.

In entrambi i casi, le sfide etiche evidenziano aree in cui le nostre azioni possono entrare in conflitto con i nostri valori condivisi. Per rilevare, mitigare, minimizzare o eliminare queste preoccupazioni, dobbiamo porci domande morali "sì/no" relative alle nostre azioni, quindi adottare misure correttive secondo necessità. Esaminiamo alcune sfide etiche e le domande morali che sollevano:

#### 2.1 Proprietà dei dati

La raccolta dati spesso coinvolge dati personali che possono identificare i soggetti dei dati. La [proprietà dei dati](https://permission.io/blog/data-ownership) riguarda il _controllo_ e i [_diritti degli utenti_](https://permission.io/blog/data-ownership) relativi alla creazione, elaborazione e diffusione dei dati. 

Le domande morali da porsi sono: 
 * Chi possiede i dati? (utente o organizzazione)
 * Quali diritti hanno i soggetti dei dati? (es: accesso, cancellazione, portabilità)
 * Quali diritti hanno le organizzazioni? (es: rettificare recensioni utente dannose)

#### 2.2 Consenso informato

Il [consenso informato](https://legaldictionary.net/informed-consent/) definisce l'atto degli utenti di accettare un'azione (come la raccolta dati) con una _piena comprensione_ dei fatti rilevanti, inclusi lo scopo, i rischi potenziali e le alternative. 

Domande da esplorare qui sono:
 * L'utente (soggetto dei dati) ha dato il permesso per la cattura e l'uso dei dati?
 * L'utente ha compreso lo scopo per cui quei dati sono stati catturati?
 * L'utente ha compreso i rischi potenziali derivanti dalla sua partecipazione?

#### 2.3 Proprietà intellettuale

La [proprietà intellettuale](https://en.wikipedia.org/wiki/Intellectual_property) si riferisce a creazioni intangibili derivanti dall'iniziativa umana, che possono _avere valore economico_ per individui o aziende. 

Domande da esplorare qui sono:
 * I dati raccolti avevano valore economico per un utente o un'azienda?
 * L'**utente** ha proprietà intellettuale qui?
 * L'**organizzazione** ha proprietà intellettuale qui?
 * Se esistono questi diritti, come li stiamo proteggendo?

#### 2.4 Privacy dei dati

La [privacy dei dati](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) o privacy delle informazioni si riferisce alla preservazione della privacy degli utenti e alla protezione dell'identità degli utenti rispetto alle informazioni personali identificabili. 

Domande da esplorare qui sono:
 * I dati (personali) degli utenti sono protetti contro hack e fughe di dati?
 * I dati degli utenti sono accessibili solo a utenti e contesti autorizzati?
 * L'anonimato degli utenti è preservato quando i dati vengono condivisi o diffusi?
 * È possibile de-identificare un utente da dataset anonimizzati?

#### 2.5 Diritto all'oblio

Il [Diritto all'oblio](https://en.wikipedia.org/wiki/Right_to_be_forgotten) o [Diritto alla cancellazione](https://www.gdpreu.org/right-to-be-forgotten/) offre ulteriore protezione dei dati personali agli utenti. In particolare, dà agli utenti il diritto di richiedere la cancellazione o la rimozione dei dati personali da ricerche su Internet e altre posizioni, _in circostanze specifiche_ - permettendo loro un nuovo inizio online senza che le azioni passate vengano usate contro di loro.

Domande da esplorare qui sono:
 * Il sistema consente ai soggetti dei dati di richiedere la cancellazione?
 * Il ritiro del consenso dell'utente dovrebbe innescare una cancellazione automatica?
 * I dati sono stati raccolti senza consenso o con mezzi illeciti?
 * Siamo conformi alle normative governative sulla privacy dei dati?

#### 2.6 Pregiudizi nei dataset

Il pregiudizio nei dataset o [pregiudizio nella raccolta](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) riguarda la selezione di un sottoinsieme _non rappresentativo_ di dati per lo sviluppo di algoritmi, creando potenziale iniquità nei risultati per gruppi diversi. Tipi di pregiudizio includono pregiudizio di selezione o campionamento, pregiudizio volontario e pregiudizio strumentale. 

Domande da esplorare qui sono:
 * Abbiamo reclutato un set rappresentativo di soggetti dei dati?
 * Abbiamo testato il nostro dataset raccolto o curato per vari pregiudizi?
 * Possiamo mitigare o rimuovere eventuali pregiudizi scoperti?

#### 2.7 Qualità dei dati

La [qualità dei dati](https://lakefs.io/data-quality-testing/) esamina la validità del dataset curato utilizzato per sviluppare i nostri algoritmi, verificando se le caratteristiche e i record soddisfano i requisiti per il livello di accuratezza e coerenza necessario per il nostro scopo AI.

Domande da esplorare qui sono:
 * Abbiamo catturato caratteristiche valide per il nostro caso d'uso?
 * I dati sono stati catturati in modo coerente tra diverse fonti di dati?
 * Il dataset è completo per condizioni o scenari diversi?
 * Le informazioni catturate riflettono accuratamente la realtà?

#### 2.8 Equità degli algoritmi
[Algorithm Fairness](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) verifica se il design dell'algoritmo discrimina sistematicamente contro specifici sottogruppi di soggetti, portando a [potenziali danni](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) nella _distribuzione_ (dove le risorse vengono negate o trattenute per quel gruppo) e nella _qualità del servizio_ (dove l'IA non è altrettanto accurata per alcuni sottogruppi rispetto ad altri).

Domande da esplorare qui sono:
 * Abbiamo valutato l'accuratezza del modello per sottogruppi e condizioni diverse?
 * Abbiamo esaminato il sistema per potenziali danni (ad esempio, stereotipi)?
 * Possiamo rivedere i dati o riaddestrare i modelli per mitigare i danni identificati?

Esplora risorse come [AI Fairness checklists](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) per saperne di più.

#### 2.9 Falsificazione

[Data Misrepresentation](https://www.sciencedirect.com/topics/computer-science/misrepresentation) riguarda il chiedersi se stiamo comunicando intuizioni da dati riportati onestamente in modo ingannevole per supportare una narrativa desiderata.

Domande da esplorare qui sono:
 * Stiamo riportando dati incompleti o inaccurati?
 * Stiamo visualizzando i dati in modo da indurre conclusioni fuorvianti?
 * Stiamo usando tecniche statistiche selettive per manipolare i risultati?
 * Ci sono spiegazioni alternative che potrebbero offrire una conclusione diversa?

#### 2.10 Libera Scelta
L'[Illusione della Libera Scelta](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) si verifica quando le "architetture di scelta" del sistema utilizzano algoritmi decisionali per spingere le persone verso un risultato preferito, pur dando l'impressione di offrire opzioni e controllo. Questi [dark patterns](https://www.darkpatterns.org/) possono causare danni sociali ed economici agli utenti. Poiché le decisioni degli utenti influenzano i profili comportamentali, queste azioni possono potenzialmente guidare scelte future che amplificano o estendono l'impatto di questi danni.

Domande da esplorare qui sono:
 * L'utente ha compreso le implicazioni di quella scelta?
 * L'utente era consapevole delle (alternative) opzioni e dei pro e contro di ciascuna?
 * L'utente può annullare una scelta automatizzata o influenzata in seguito?

### 3. Studi di Caso

Per mettere queste sfide etiche in contesti reali, è utile esaminare studi di caso che evidenziano i potenziali danni e le conseguenze per individui e società, quando tali violazioni etiche vengono trascurate.

Ecco alcuni esempi:

| Sfida Etica | Studio di Caso  | 
|--- |--- |
| **Consenso Informato** | 1972 - [Tuskegee Syphilis Study](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Gli uomini afroamericani che parteciparono allo studio furono promessi cure mediche gratuite _ma ingannati_ dai ricercatori che non informarono i soggetti della loro diagnosi o della disponibilità di trattamenti. Molti soggetti morirono e partner o figli furono colpiti; lo studio durò 40 anni. | 
| **Privacy dei Dati** |  2007 - Il [Netflix data prize](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) fornì ai ricercatori _10M di valutazioni di film anonimizzate da 50K clienti_ per migliorare gli algoritmi di raccomandazione. Tuttavia, i ricercatori riuscirono a correlare i dati anonimizzati con dati identificabili personalmente in _dataset esterni_ (ad esempio, commenti su IMDb), "de-anonimizzando" di fatto alcuni abbonati Netflix.|
| **Bias nella Raccolta**  | 2013 - La città di Boston [sviluppò Street Bump](https://www.boston.gov/transportation/street-bump), un'app che permetteva ai cittadini di segnalare buche, fornendo alla città dati migliori sulle strade per individuare e risolvere i problemi. Tuttavia, [le persone con redditi più bassi avevano meno accesso a auto e telefoni](https://hbr.org/2013/04/the-hidden-biases-in-big-data), rendendo invisibili i loro problemi stradali in questa app. Gli sviluppatori collaborarono con accademici per affrontare _problemi di accesso equo e divari digitali_ per garantire equità. |
| **Equità Algoritmica**  | 2018 - Lo studio MIT [Gender Shades Study](http://gendershades.org/overview.html) valutò l'accuratezza dei prodotti di classificazione di genere basati su IA, evidenziando lacune nell'accuratezza per donne e persone di colore. Una [Apple Card del 2019](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) sembrava offrire meno credito alle donne rispetto agli uomini. Entrambi illustrarono problemi di bias algoritmico che portano a danni socio-economici.|
| **Falsificazione dei Dati** | 2020 - Il [Dipartimento della Salute della Georgia pubblicò grafici COVID-19](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) che sembravano fuorviare i cittadini sulle tendenze dei casi confermati con un ordinamento non cronologico sull'asse x. Questo illustra la falsificazione attraverso trucchi di visualizzazione. |
| **Illusione della libera scelta** | 2020 - L'app educativa [ABCmouse pagò $10M per risolvere una denuncia FTC](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) in cui i genitori erano intrappolati nel pagamento di abbonamenti che non potevano cancellare. Questo illustra i dark patterns nelle architetture di scelta, dove gli utenti erano spinti verso scelte potenzialmente dannose. |
| **Privacy dei Dati e Diritti degli Utenti** | 2021 - La [violazione dei dati di Facebook](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) espose dati di 530M di utenti, portando a un accordo da $5B con la FTC. Tuttavia, si rifiutò di notificare agli utenti la violazione, violando i diritti degli utenti sulla trasparenza e l'accesso ai dati. |

Vuoi esplorare più studi di caso? Dai un'occhiata a queste risorse:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - dilemmi etici in diversi settori. 
* [Corso di Etica della Data Science](https://www.coursera.org/learn/data-science-ethics#syllabus) - studi di caso fondamentali esplorati.
* [Dove le cose sono andate male](https://deon.drivendata.org/examples/) - checklist Deon con esempi.

> 🚨 Pensa agli studi di caso che hai visto: hai vissuto o sei stato colpito da una sfida etica simile nella tua vita? Riesci a pensare ad almeno un altro studio di caso che illustri una delle sfide etiche discusse in questa sezione?

## Etica Applicata

Abbiamo parlato di concetti etici, sfide e studi di caso in contesti reali. Ma come iniziamo ad _applicare_ principi e pratiche etiche nei nostri progetti? E come _operazionalizziamo_ queste pratiche per una migliore governance? Esploriamo alcune soluzioni reali:

### 1. Codici Professionali

I Codici Professionali offrono un'opzione per le organizzazioni per "incentivare" i membri a supportare i loro principi etici e la dichiarazione di missione. I codici sono _linee guida morali_ per il comportamento professionale, aiutando i dipendenti o i membri a prendere decisioni che si allineano ai principi dell'organizzazione. Sono efficaci solo quanto la conformità volontaria dei membri; tuttavia, molte organizzazioni offrono ricompense e penalità aggiuntive per motivare la conformità.

Esempi includono:

 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Codice Etico
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Codice di Condotta (creato nel 2013)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (dal 1993)

> 🚨 Appartieni a un'organizzazione professionale di ingegneria o data science? Esplora il loro sito per vedere se definiscono un codice etico professionale. Cosa dice sui loro principi etici? Come stanno "incentivando" i membri a seguire il codice?

### 2. Checklist Etiche

Mentre i codici professionali definiscono il comportamento _etico richiesto_ dai professionisti, [hanno limiti noti](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) nell'applicazione, in particolare nei progetti su larga scala. Invece, molti esperti di data science [sostengono le checklist](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), che possono **collegare i principi alle pratiche** in modi più deterministici e attuabili.

Le checklist convertono le domande in compiti "sì/no" che possono essere operazionalizzati, permettendo loro di essere tracciati come parte dei flussi di lavoro standard di rilascio del prodotto.

Esempi includono:
 * [Deon](https://deon.drivendata.org/) - una checklist etica generica per i dati creata da [raccomandazioni del settore](https://deon.drivendata.org/#checklist-citations) con uno strumento da riga di comando per una facile integrazione.
 * [Privacy Audit Checklist](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - fornisce indicazioni generali per le pratiche di gestione delle informazioni da prospettive legali e sociali.
 * [AI Fairness Checklist](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - creata da professionisti dell'IA per supportare l'adozione e l'integrazione di controlli di equità nei cicli di sviluppo dell'IA.
 * [22 domande per l'etica nei dati e nell'IA](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - framework più aperto, strutturato per l'esplorazione iniziale delle questioni etiche nel design, implementazione e contesti organizzativi.

### 3. Regolamenti Etici

L'etica riguarda la definizione di valori condivisi e il fare la cosa giusta _volontariamente_. **Conformità** riguarda il _rispetto della legge_ se e dove definita. **Governance** copre in generale tutti i modi in cui le organizzazioni operano per applicare principi etici e rispettare le leggi stabilite.

Oggi, la governance assume due forme all'interno delle organizzazioni. Innanzitutto, riguarda la definizione di principi di **IA etica** e l'istituzione di pratiche per operazionalizzare l'adozione in tutti i progetti legati all'IA nell'organizzazione. In secondo luogo, riguarda il rispetto di tutti i regolamenti governativi di **protezione dei dati** per le regioni in cui opera.

Esempi di regolamenti sulla protezione dei dati e sulla privacy:

 * `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - regola la raccolta, l'uso e la divulgazione di informazioni personali da parte del _governo federale_.
 * `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - protegge i dati sanitari personali.
 * `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - protegge la privacy dei dati dei bambini sotto i 13 anni.
 * `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - fornisce diritti agli utenti, protezione dei dati e privacy.
 * `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) - offre ai consumatori più _diritti_ sui loro dati personali.
 * `2021`, La [Legge sulla Protezione delle Informazioni Personali della Cina](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) appena approvata, crea una delle normative sulla privacy online più forti al mondo.

> 🚨 L'Unione Europea ha definito il GDPR (Regolamento Generale sulla Protezione dei Dati), che rimane una delle normative sulla privacy dei dati più influenti oggi. Sapevi che definisce anche [8 diritti degli utenti](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) per proteggere la privacy digitale e i dati personali dei cittadini? Scopri quali sono e perché sono importanti.

### 4. Cultura Etica

Nota che rimane un divario intangibile tra _conformità_ (fare abbastanza per soddisfare "la lettera della legge") e affrontare [problemi sistemici](https://www.coursera.org/learn/data-science-ethics/home/week/4) (come ossificazione, asimmetria informativa e ingiustizia distributiva) che possono accelerare la strumentalizzazione dell'IA.

Quest'ultimo richiede [approcci collaborativi per definire culture etiche](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f) che costruiscano connessioni emotive e valori condivisi coerenti _tra organizzazioni_ nel settore. Questo richiede più [culture etiche formalizzate](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) nelle organizzazioni - permettendo a _chiunque_ di [tirare la corda Andon](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (per sollevare preoccupazioni etiche presto nel processo) e rendendo _le valutazioni etiche_ (ad esempio, nell'assunzione) un criterio centrale per la formazione dei team nei progetti di IA.

---
## [Quiz post-lezione](https://ff-quizzes.netlify.app/en/ds/) 🎯
## Revisione e Studio Autonomo 

Corsi e libri aiutano a comprendere i concetti etici fondamentali e le sfide, mentre studi di caso e strumenti aiutano con le pratiche etiche applicate in contesti reali. Ecco alcune risorse per iniziare.

* [Machine Learning For Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - lezione sulla Equità, da Microsoft.
* [Principi di AI Responsabile](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - percorso di apprendimento gratuito di Microsoft Learn.
* [Etica e Data Science](https://resources.oreilly.com/examples/0636920203964) - EBook di O'Reilly (M. Loukides, H. Mason et. al)
* [Etica della Data Science](https://www.coursera.org/learn/data-science-ethics#syllabus) - corso online dell'Università del Michigan.
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - studi di caso dell'Università del Texas.

# Compito

[Scrivi uno studio di caso sull'etica dei dati](assignment.md)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.