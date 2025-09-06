<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "06bac7959b46b6e8aedcae014278c476",
  "translation_date": "2025-09-06T08:53:01+00:00",
  "source_file": "6-Data-Science-In-Wild/20-Real-World-Examples/README.md",
  "language_code": "it"
}
-->
# La Scienza dei Dati nel Mondo Reale

| ![ Sketchnote di [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-RealWorld.png) |
| :--------------------------------------------------------------------------------------------------------------: |
|               La Scienza dei Dati nel Mondo Reale - _Sketchnote di [@nitya](https://twitter.com/nitya)_           |

Siamo quasi alla fine di questo percorso di apprendimento!

Abbiamo iniziato con le definizioni di scienza dei dati ed etica, esplorato vari strumenti e tecniche per l'analisi e la visualizzazione dei dati, esaminato il ciclo di vita della scienza dei dati e analizzato come scalare e automatizzare i flussi di lavoro della scienza dei dati con i servizi di cloud computing. Quindi, probabilmente ti starai chiedendo: _"Come posso applicare tutto ciò che ho imparato ai contesti del mondo reale?"_

In questa lezione, esploreremo le applicazioni reali della scienza dei dati nei vari settori e approfondiremo esempi specifici nei contesti della ricerca, delle scienze umane digitali e della sostenibilità. Esamineremo opportunità di progetti per studenti e concluderemo con risorse utili per continuare il tuo percorso di apprendimento!

## Quiz Pre-Lezione

## [Quiz Pre-Lezione](https://ff-quizzes.netlify.app/en/ds/quiz/38)

## Scienza dei Dati + Industria

Grazie alla democratizzazione dell'IA, gli sviluppatori trovano sempre più facile progettare e integrare decisioni guidate dall'IA e intuizioni basate sui dati nelle esperienze utente e nei flussi di lavoro di sviluppo. Ecco alcuni esempi di come la scienza dei dati viene "applicata" a contesti reali nell'industria:

 * [Google Flu Trends](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) ha utilizzato la scienza dei dati per correlare i termini di ricerca con le tendenze dell'influenza. Sebbene l'approccio avesse delle lacune, ha sollevato consapevolezza sulle possibilità (e sfide) delle previsioni sanitarie basate sui dati.

 * [Previsioni di Routing di UPS](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - spiega come UPS utilizza la scienza dei dati e il machine learning per prevedere i percorsi ottimali per le consegne, tenendo conto delle condizioni meteorologiche, dei modelli di traffico, delle scadenze di consegna e altro ancora.

 * [Visualizzazione dei Percorsi dei Taxi di NYC](http://chriswhong.github.io/nyctaxi/) - i dati raccolti utilizzando le [Leggi sulla Libertà di Informazione](https://chriswhong.com/open-data/foil_nyc_taxi/) hanno aiutato a visualizzare una giornata nella vita dei taxi di NYC, permettendoci di capire come navigano nella città affollata, i guadagni e la durata dei viaggi in un periodo di 24 ore.

 * [Uber Data Science Workbench](https://eng.uber.com/dsw/) - utilizza i dati (su luoghi di prelievo e rilascio, durata dei viaggi, percorsi preferiti, ecc.) raccolti da milioni di viaggi Uber *quotidianamente* per costruire uno strumento di analisi dei dati utile per prezzi, sicurezza, rilevamento delle frodi e decisioni di navigazione.

 * [Analisi Sportiva](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - si concentra su _analisi predittiva_ (analisi di squadra e giocatori - pensa a [Moneyball](https://datasciencedegree.wisconsin.edu/blog/moneyball-proves-importance-big-data-big-ideas/) - e gestione dei fan) e _visualizzazione dei dati_ (dashboard per squadre e fan, giochi, ecc.) con applicazioni come scouting di talenti, scommesse sportive e gestione di inventari/luoghi.

 * [Scienza dei Dati nel Settore Bancario](https://data-flair.training/blogs/data-science-in-banking/) - evidenzia il valore della scienza dei dati nel settore finanziario con applicazioni che vanno dalla modellazione del rischio e rilevamento delle frodi, alla segmentazione dei clienti, previsioni in tempo reale e sistemi di raccomandazione. L'analisi predittiva guida anche misure critiche come i [credit scores](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit).

 * [Scienza dei Dati nella Sanità](https://data-flair.training/blogs/data-science-in-healthcare/) - evidenzia applicazioni come imaging medico (es. MRI, radiografie, TAC), genomica (sequenziamento del DNA), sviluppo di farmaci (valutazione del rischio, previsione del successo), analisi predittiva (cura dei pazienti e logistica delle forniture), monitoraggio e prevenzione delle malattie, ecc.

![Applicazioni della Scienza dei Dati nel Mondo Reale](../../../../6-Data-Science-In-Wild/20-Real-World-Examples/images/data-science-applications.png) Crediti Immagine: [Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

La figura mostra altri domini ed esempi di applicazione delle tecniche di scienza dei dati. Vuoi esplorare altre applicazioni? Dai un'occhiata alla sezione [Review & Self Study](../../../../6-Data-Science-In-Wild/20-Real-World-Examples) qui sotto.

## Scienza dei Dati + Ricerca

| ![ Sketchnote di [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Research.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Scienza dei Dati & Ricerca - _Sketchnote di [@nitya](https://twitter.com/nitya)_              |

Mentre le applicazioni reali spesso si concentrano su casi d'uso industriali su larga scala, le applicazioni e i progetti di _ricerca_ possono essere utili da due prospettive:

* _opportunità di innovazione_ - esplorare prototipi rapidi di concetti avanzati e testare esperienze utente per applicazioni di nuova generazione.
* _sfide di implementazione_ - indagare i potenziali danni o le conseguenze non intenzionali delle tecnologie di scienza dei dati nei contesti reali.

Per gli studenti, questi progetti di ricerca possono offrire opportunità di apprendimento e collaborazione che migliorano la comprensione dell'argomento e ampliano la consapevolezza e il coinvolgimento con persone o team rilevanti che lavorano in aree di interesse. Ma come sono i progetti di ricerca e quale impatto possono avere?

Esaminiamo un esempio: lo [Studio Gender Shades del MIT](http://gendershades.org/overview.html) di Joy Buolamwini (MIT Media Labs) con un [articolo di ricerca](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf) co-autore con Timnit Gebru (all'epoca presso Microsoft Research) che si è concentrato su:

 * **Cosa:** L'obiettivo del progetto di ricerca era _valutare i bias presenti negli algoritmi e nei dataset di analisi facciale automatizzata_ in base al genere e al tipo di pelle.
 * **Perché:** L'analisi facciale è utilizzata in contesti come forze dell'ordine, sicurezza aeroportuale, sistemi di assunzione e altro - contesti in cui classificazioni inaccurate (es. a causa di bias) possono causare potenziali danni economici e sociali agli individui o ai gruppi interessati. Comprendere (ed eliminare o mitigare) i bias è fondamentale per un uso equo.
 * **Come:** I ricercatori hanno riconosciuto che i benchmark esistenti utilizzavano prevalentemente soggetti con pelle chiara e hanno curato un nuovo dataset (oltre 1000 immagini) _più bilanciato_ per genere e tipo di pelle. Il dataset è stato utilizzato per valutare l'accuratezza di tre prodotti di classificazione di genere (di Microsoft, IBM e Face++).

I risultati hanno mostrato che, sebbene l'accuratezza complessiva della classificazione fosse buona, c'era una differenza evidente nei tassi di errore tra i vari sottogruppi - con un **misgendering** più elevato per le donne o le persone con pelle più scura, indicativo di bias.

**Risultati Chiave:** Ha sollevato consapevolezza sul fatto che la scienza dei dati necessita di _dataset più rappresentativi_ (sottogruppi bilanciati) e di _team più inclusivi_ (background diversificati) per riconoscere ed eliminare o mitigare tali bias nelle soluzioni di IA. Sforzi di ricerca come questo sono anche fondamentali per molte organizzazioni nella definizione di principi e pratiche per un'IA _responsabile_ per migliorare l'equità nei loro prodotti e processi di IA.

**Vuoi conoscere gli sforzi di ricerca rilevanti in Microsoft?**

* Dai un'occhiata ai [Progetti di Ricerca Microsoft](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project) sull'Intelligenza Artificiale.
* Esplora i progetti per studenti della [Microsoft Research Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/).
* Dai un'occhiata al progetto [Fairlearn](https://fairlearn.org/) e alle iniziative di [IA Responsabile](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6).

## Scienza dei Dati + Scienze Umane

| ![ Sketchnote di [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Scienza dei Dati & Scienze Umane Digitali - _Sketchnote di [@nitya](https://twitter.com/nitya)_              |

Le Scienze Umane Digitali [sono state definite](https://digitalhumanities.stanford.edu/about-dh-stanford) come "una raccolta di pratiche e approcci che combinano metodi computazionali con l'indagine umanistica". Progetti [Stanford](https://digitalhumanities.stanford.edu/projects) come _"rebooting history"_ e _"poetic thinking"_ illustrano il legame tra [Scienze Umane Digitali e Scienza dei Dati](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science) - enfatizzando tecniche come l'analisi delle reti, la visualizzazione delle informazioni, l'analisi spaziale e testuale che possono aiutarci a rivisitare dataset storici e letterari per trarre nuove intuizioni e prospettive.

*Vuoi esplorare ed estendere un progetto in questo ambito?*

Dai un'occhiata a ["Emily Dickinson and the Meter of Mood"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671) - un ottimo esempio di [Jen Looper](https://twitter.com/jenlooper) che si chiede come possiamo utilizzare la scienza dei dati per rivisitare poesie familiari e rivalutare il loro significato e il contributo dell'autore in nuovi contesti. Ad esempio, _possiamo prevedere la stagione in cui una poesia è stata scritta analizzandone il tono o il sentimento_ - e cosa ci dice questo sullo stato d'animo dell'autore nel periodo rilevante?

Per rispondere a questa domanda, seguiamo i passaggi del ciclo di vita della scienza dei dati:
 * [`Acquisizione dei Dati`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#acquiring-the-dataset) - per raccogliere un dataset rilevante per l'analisi. Le opzioni includono l'uso di un'API (es. [Poetry DB API](https://poetrydb.org/index.html)) o il web scraping (es. [Project Gutenberg](https://www.gutenberg.org/files/12242/12242-h/12242-h.htm)) utilizzando strumenti come [Scrapy](https://scrapy.org/).
 * [`Pulizia dei Dati`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#clean-the-data) - spiega come i testi possono essere formattati, sanitizzati e semplificati utilizzando strumenti di base come Visual Studio Code e Microsoft Excel.
 * [`Analisi dei Dati`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#working-with-the-data-in-a-notebook) - spiega come possiamo ora importare il dataset nei "Notebooks" per l'analisi utilizzando pacchetti Python (come pandas, numpy e matplotlib) per organizzare e visualizzare i dati.
 * [`Analisi del Sentimento`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#sentiment-analysis-using-cognitive-services) - spiega come possiamo integrare servizi cloud come Text Analytics, utilizzando strumenti low-code come [Power Automate](https://flow.microsoft.com/en-us/) per flussi di lavoro automatizzati di elaborazione dei dati.

Seguendo questo flusso di lavoro, possiamo esplorare gli impatti stagionali sul sentimento delle poesie e aiutarci a formare le nostre prospettive sull'autore. Provalo tu stesso - poi estendi il notebook per porre altre domande o visualizzare i dati in modi nuovi!

> Puoi utilizzare alcuni degli strumenti nel [Digital Humanities toolkit](https://github.com/Digital-Humanities-Toolkit) per perseguire queste linee di indagine.

## Scienza dei Dati + Sostenibilità

| ![ Sketchnote di [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Sustainability.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Scienza dei Dati & Sostenibilità - _Sketchnote di [@nitya](https://twitter.com/nitya)_              |

L'[Agenda 2030 per lo Sviluppo Sostenibile](https://sdgs.un.org/2030agenda) - adottata da tutti i membri delle Nazioni Unite nel 2015 - identifica 17 obiettivi, tra cui quelli che si concentrano su **Proteggere il Pianeta** dal degrado e dall'impatto dei cambiamenti climatici. L'iniziativa [Microsoft Sustainability](https://www.microsoft.com/en-us/sustainability) supporta questi obiettivi esplorando modi in cui le soluzioni tecnologiche possono sostenere e costruire futuri più sostenibili con un [focus su 4 obiettivi](https://dev.to/azure/a-visual-guide-to-sustainable-software-engineering-53hh) - essere carbon negative, water positive, zero waste e biodiversi entro il 2030.

Affrontare queste sfide in modo scalabile e tempestivo richiede un pensiero su scala cloud - e dati su larga scala. L'iniziativa [Planetary Computer](https://planetarycomputer.microsoft.com/) fornisce 4 componenti per aiutare i data scientist e gli sviluppatori in questo sforzo:

 * [Catalogo Dati](https://planetarycomputer.microsoft.com/catalog) - con petabyte di dati sui sistemi terrestri (gratuiti e ospitati su Azure).
 * [Planetary API](https://planetarycomputer.microsoft.com/docs/reference/stac/) - per aiutare gli utenti a cercare dati rilevanti nello spazio e nel tempo.
 * [Hub](https://planetarycomputer.microsoft.com/docs/overview/environment/) - ambiente gestito per gli scienziati per elaborare enormi dataset geospaziali.
 * [Applicazioni](https://planetarycomputer.microsoft.com/applications) - mostra casi d'uso e strumenti per intuizioni sulla sostenibilità.
**Il progetto Planetary Computer è attualmente in anteprima (a partire da settembre 2021)** - ecco come puoi iniziare a contribuire a soluzioni sostenibili utilizzando la data science.

* [Richiedi l'accesso](https://planetarycomputer.microsoft.com/account/request) per iniziare l'esplorazione e connetterti con altri utenti.
* [Esplora la documentazione](https://planetarycomputer.microsoft.com/docs/overview/about) per comprendere i dataset e le API supportate.
* Esplora applicazioni come [Ecosystem Monitoring](https://analytics-lab.org/ecosystemmonitoring/) per trovare ispirazione su idee applicative.

Pensa a come puoi utilizzare la visualizzazione dei dati per evidenziare o amplificare intuizioni rilevanti su temi come il cambiamento climatico e la deforestazione. Oppure considera come queste intuizioni possano essere utilizzate per creare nuove esperienze utente che motivino cambiamenti comportamentali verso uno stile di vita più sostenibile.

## Data Science + Studenti

Abbiamo parlato di applicazioni reali nell'industria e nella ricerca, ed esplorato esempi di applicazioni di data science nelle discipline umanistiche digitali e nella sostenibilità. Quindi, come puoi sviluppare le tue competenze e condividere la tua esperienza come principianti nella data science?

Ecco alcuni esempi di progetti di data science per studenti che possono ispirarti.

 * [MSR Data Science Summer School](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/#!projects) con [progetti](https://github.com/msr-ds3) su GitHub che esplorano argomenti come:
    - [Pregiudizi razziali nell'uso della forza da parte della polizia](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2019-replicating-an-empirical-analysis-of-racial-differences-in-police-use-of-force/) | [Github](https://github.com/msr-ds3/stop-question-frisk)
    - [Affidabilità del sistema della metropolitana di New York](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2018-exploring-the-reliability-of-the-nyc-subway-system/) | [Github](https://github.com/msr-ds3/nyctransit)
 * [Digitalizzazione della cultura materiale: esplorazione delle distribuzioni socio-economiche a Sirkap](https://claremont.maps.arcgis.com/apps/Cascade/index.html?appid=bdf2aef0f45a4674ba41cd373fa23afc) - da [Ornella Altunyan](https://twitter.com/ornelladotcom) e il suo team a Claremont, utilizzando [ArcGIS StoryMaps](https://storymaps.arcgis.com/).

## 🚀 Sfida

Cerca articoli che raccomandano progetti di data science adatti ai principianti - come [queste 50 aree tematiche](https://www.upgrad.com/blog/data-science-project-ideas-topics-beginners/) o [queste 21 idee di progetto](https://www.intellspot.com/data-science-project-ideas) o [questi 16 progetti con codice sorgente](https://data-flair.training/blogs/data-science-project-ideas/) che puoi analizzare e rielaborare. E non dimenticare di scrivere un blog sui tuoi percorsi di apprendimento e condividere le tue intuizioni con tutti noi.

## Quiz post-lezione

## [Quiz post-lezione](https://ff-quizzes.netlify.app/en/ds/quiz/39)

## Revisione e studio autonomo

Vuoi esplorare altri casi d'uso? Ecco alcuni articoli rilevanti:
 * [17 Applicazioni ed esempi di Data Science](https://builtin.com/data-science/data-science-applications-examples) - Luglio 2021
 * [11 Applicazioni straordinarie della Data Science nel mondo reale](https://myblindbird.com/data-science-applications-real-world/) - Maggio 2021
 * [Data Science nel mondo reale](https://towardsdatascience.com/data-science-in-the-real-world/home) - Raccolta di articoli
 * Data Science in: [Educazione](https://data-flair.training/blogs/data-science-in-education/), [Agricoltura](https://data-flair.training/blogs/data-science-in-agriculture/), [Finanza](https://data-flair.training/blogs/data-science-in-finance/), [Cinema](https://data-flair.training/blogs/data-science-at-movies/) e altro.

## Compito

[Esplora un dataset del Planetary Computer](assignment.md)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.