<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-09-06T08:40:19+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "it"
}
-->
# Introduzione alla Data Science nel Cloud

|![ Sketchnote di [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Data Science nel Cloud: Introduzione - _Sketchnote di [@nitya](https://twitter.com/nitya)_ |

In questa lezione, imparerai i principi fondamentali del Cloud, scoprirai perché può essere interessante utilizzare i servizi Cloud per eseguire i tuoi progetti di data science e vedremo alcuni esempi di progetti di data science eseguiti nel Cloud.

## [Quiz Pre-Lezione](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## Cos'è il Cloud?

Il Cloud, o Cloud Computing, è la fornitura di una vasta gamma di servizi informatici a consumo ospitati su un'infrastruttura tramite Internet. I servizi includono soluzioni come archiviazione, database, networking, software, analisi e servizi intelligenti.

Di solito distinguiamo tra Cloud Pubblico, Privato e Ibrido come segue:

* Cloud pubblico: un cloud pubblico è di proprietà e gestito da un fornitore di servizi cloud di terze parti che fornisce le sue risorse informatiche su Internet al pubblico.
* Cloud privato: si riferisce a risorse di cloud computing utilizzate esclusivamente da un'unica azienda o organizzazione, con servizi e un'infrastruttura mantenuti su una rete privata.
* Cloud ibrido: il cloud ibrido è un sistema che combina cloud pubblici e privati. Gli utenti optano per un datacenter locale, consentendo al contempo l'esecuzione di dati e applicazioni su uno o più cloud pubblici.

La maggior parte dei servizi di cloud computing rientra in tre categorie: Infrastructure as a Service (IaaS), Platform as a Service (PaaS) e Software as a Service (SaaS).

* Infrastructure as a Service (IaaS): gli utenti noleggiano un'infrastruttura IT come server e macchine virtuali (VM), archiviazione, reti, sistemi operativi.
* Platform as a Service (PaaS): gli utenti noleggiano un ambiente per sviluppare, testare, distribuire e gestire applicazioni software. Gli utenti non devono preoccuparsi di configurare o gestire l'infrastruttura sottostante di server, archiviazione, rete e database necessari per lo sviluppo.
* Software as a Service (SaaS): gli utenti accedono a applicazioni software tramite Internet, su richiesta e tipicamente in abbonamento. Gli utenti non devono preoccuparsi di ospitare e gestire l'applicazione software, l'infrastruttura sottostante o la manutenzione, come aggiornamenti software e patch di sicurezza.

Alcuni dei maggiori fornitori di Cloud sono Amazon Web Services, Google Cloud Platform e Microsoft Azure.

## Perché scegliere il Cloud per la Data Science?

Gli sviluppatori e i professionisti IT scelgono di lavorare con il Cloud per molte ragioni, tra cui:

* Innovazione: puoi potenziare le tue applicazioni integrando servizi innovativi creati dai fornitori di Cloud direttamente nelle tue app.
* Flessibilità: paghi solo per i servizi di cui hai bisogno e puoi scegliere tra una vasta gamma di servizi. Di solito paghi a consumo e adatti i tuoi servizi in base alle tue esigenze in evoluzione.
* Budget: non è necessario fare investimenti iniziali per acquistare hardware e software, configurare e gestire datacenter in loco, e puoi semplicemente pagare per ciò che utilizzi.
* Scalabilità: le tue risorse possono scalare in base alle esigenze del tuo progetto, il che significa che le tue app possono utilizzare più o meno potenza di calcolo, archiviazione e larghezza di banda, adattandosi ai fattori esterni in qualsiasi momento.
* Produttività: puoi concentrarti sul tuo business piuttosto che perdere tempo in attività che possono essere gestite da qualcun altro, come la gestione dei datacenter.
* Affidabilità: il Cloud Computing offre diversi modi per eseguire backup continui dei tuoi dati e puoi impostare piani di recupero in caso di disastri per mantenere il tuo business e i tuoi servizi operativi, anche in tempi di crisi.
* Sicurezza: puoi beneficiare di politiche, tecnologie e controlli che rafforzano la sicurezza del tuo progetto.

Queste sono alcune delle ragioni più comuni per cui le persone scelgono di utilizzare i servizi Cloud. Ora che abbiamo una migliore comprensione di cosa sia il Cloud e dei suoi principali vantaggi, vediamo più specificamente i lavori dei Data Scientist e degli sviluppatori che lavorano con i dati, e come il Cloud può aiutarli a superare diverse sfide che potrebbero affrontare:

* Archiviazione di grandi quantità di dati: invece di acquistare, gestire e proteggere grandi server, puoi archiviare i tuoi dati direttamente nel cloud, con soluzioni come Azure Cosmos DB, Azure SQL Database e Azure Data Lake Storage.
* Integrazione dei dati: l'integrazione dei dati è una parte essenziale della Data Science, che ti consente di passare dalla raccolta dei dati all'azione. Con i servizi di integrazione dei dati offerti nel cloud, puoi raccogliere, trasformare e integrare dati da varie fonti in un unico data warehouse, con Data Factory.
* Elaborazione dei dati: elaborare grandi quantità di dati richiede molta potenza di calcolo, e non tutti hanno accesso a macchine abbastanza potenti per farlo, motivo per cui molte persone scelgono di sfruttare direttamente la grande potenza di calcolo del cloud per eseguire e distribuire le loro soluzioni.
* Utilizzo di servizi di analisi dei dati: servizi cloud come Azure Synapse Analytics, Azure Stream Analytics e Azure Databricks ti aiutano a trasformare i tuoi dati in informazioni utili.
* Utilizzo di servizi di Machine Learning e intelligenza artificiale: invece di partire da zero, puoi utilizzare algoritmi di machine learning offerti dal fornitore di cloud, con servizi come AzureML. Puoi anche utilizzare servizi cognitivi come speech-to-text, text-to-speech, computer vision e altro.

## Esempi di Data Science nel Cloud

Rendiamo tutto più concreto esaminando un paio di scenari.

### Analisi in tempo reale del sentiment sui social media
Iniziamo con uno scenario comunemente studiato da chi inizia con il machine learning: l'analisi del sentiment sui social media in tempo reale.

Supponiamo che tu gestisca un sito di notizie e voglia sfruttare i dati in tempo reale per capire quali contenuti potrebbero interessare i tuoi lettori. Per saperne di più, puoi creare un programma che esegue un'analisi del sentiment in tempo reale dei dati provenienti da pubblicazioni su Twitter, su argomenti rilevanti per i tuoi lettori.

Gli indicatori chiave che analizzerai sono il volume di tweet su argomenti specifici (hashtag) e il sentiment, che viene stabilito utilizzando strumenti di analisi che eseguono l'analisi del sentiment sugli argomenti specificati.

I passaggi necessari per creare questo progetto sono i seguenti:

* Creare un event hub per lo streaming degli input, che raccoglierà dati da Twitter.
* Configurare e avviare un'applicazione client Twitter, che chiamerà le API di Streaming di Twitter.
* Creare un lavoro di Stream Analytics.
* Specificare l'input e la query del lavoro.
* Creare un output sink e specificare l'output del lavoro.
* Avviare il lavoro.

Per visualizzare l'intero processo, consulta la [documentazione](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Analisi di articoli scientifici
Prendiamo un altro esempio di un progetto creato da [Dmitry Soshnikov](http://soshnikov.com), uno degli autori di questo curriculum.

Dmitry ha creato uno strumento che analizza articoli sul COVID. Esaminando questo progetto, vedrai come puoi creare uno strumento che estrae conoscenze da articoli scientifici, ottiene informazioni utili e aiuta i ricercatori a navigare attraverso grandi collezioni di articoli in modo efficiente.

Vediamo i diversi passaggi utilizzati per questo:

* Estrazione e pre-elaborazione delle informazioni con [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Utilizzo di [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) per parallelizzare l'elaborazione.
* Archiviazione e interrogazione delle informazioni con [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Creazione di un dashboard interattivo per l'esplorazione e la visualizzazione dei dati utilizzando Power BI.

Per vedere l'intero processo, visita il [blog di Dmitry](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Come puoi vedere, possiamo sfruttare i servizi Cloud in molti modi per eseguire la Data Science.

## Nota a piè di pagina

Fonti:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Quiz Post-Lezione

## [Quiz Post-Lezione](https://ff-quizzes.netlify.app/en/ds/quiz/33)

## Compito

[Analisi di Mercato](assignment.md)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.