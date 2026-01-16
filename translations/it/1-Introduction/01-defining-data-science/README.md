<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43212cc1ac137b7bb1dcfb37ca06b0f4",
  "translation_date": "2025-10-25T18:50:24+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "it"
}
-->
# Definizione di Data Science

| ![ Sketchnote di [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------: |
|              Definizione di Data Science - _Sketchnote di [@nitya](https://twitter.com/nitya)_         |

---

[![Video sulla definizione di Data Science](../../../../translated_images/it/video-def-ds.6623ee2392ef1abf6d7faf3fad10a4163642811749da75f44e35a5bb121de15c.png)](https://youtu.be/beZ7Mb_oz9I)

## [Quiz pre-lezione](https://ff-quizzes.netlify.app/en/ds/quiz/0)

## Cos'è il dato?
Nella nostra vita quotidiana siamo costantemente circondati dai dati. Il testo che stai leggendo ora è un dato. L'elenco dei numeri di telefono dei tuoi amici sul tuo smartphone è un dato, così come l'ora attuale visualizzata sul tuo orologio. Come esseri umani, operiamo naturalmente con i dati contando i soldi che abbiamo o scrivendo lettere ai nostri amici.

Tuttavia, i dati sono diventati molto più importanti con la creazione dei computer. Il ruolo principale dei computer è eseguire calcoli, ma hanno bisogno di dati su cui operare. Pertanto, dobbiamo capire come i computer memorizzano e elaborano i dati.

Con l'emergere di Internet, il ruolo dei computer come dispositivi per la gestione dei dati è aumentato. Se ci pensi, ora usiamo i computer sempre di più per l'elaborazione e la comunicazione dei dati, piuttosto che per i calcoli veri e propri. Quando scriviamo un'e-mail a un amico o cerchiamo informazioni su Internet, stiamo essenzialmente creando, memorizzando, trasmettendo e manipolando dati.
> Riesci a ricordare l'ultima volta che hai usato un computer per fare effettivamente un calcolo?

## Cos'è la Data Science?

Su [Wikipedia](https://en.wikipedia.org/wiki/Data_science), la **Data Science** è definita come *un campo scientifico che utilizza metodi scientifici per estrarre conoscenza e intuizioni da dati strutturati e non strutturati, e applicare conoscenze e intuizioni pratiche derivanti dai dati in una vasta gamma di domini applicativi*.

Questa definizione evidenzia i seguenti aspetti importanti della Data Science:

* L'obiettivo principale della Data Science è **estrarre conoscenza** dai dati, in altre parole - **comprendere** i dati, trovare alcune relazioni nascoste e costruire un **modello**.
* La Data Science utilizza **metodi scientifici**, come probabilità e statistica. In effetti, quando il termine *Data Science* è stato introdotto per la prima volta, alcune persone sostenevano che fosse solo un nuovo nome alla moda per la statistica. Oggi è evidente che il campo è molto più ampio.
* La conoscenza ottenuta dovrebbe essere applicata per produrre **intuizioni pratiche**, ovvero intuizioni che si possono applicare a situazioni aziendali reali.
* Dovremmo essere in grado di operare su dati sia **strutturati** che **non strutturati**. Torneremo a discutere i diversi tipi di dati più avanti nel corso.
* Il **dominio applicativo** è un concetto importante, e i data scientist spesso necessitano almeno di un certo grado di competenza nel dominio del problema, ad esempio: finanza, medicina, marketing, ecc.

> Un altro aspetto importante della Data Science è che studia come i dati possono essere raccolti, memorizzati e gestiti utilizzando i computer. Mentre la statistica ci fornisce le basi matematiche, la Data Science applica i concetti matematici per trarre effettivamente intuizioni dai dati.

Uno dei modi (attribuito a [Jim Gray](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) per considerare la Data Science è vederla come un paradigma scientifico separato:
* **Empirico**, in cui ci si basa principalmente su osservazioni e risultati di esperimenti
* **Teorico**, dove emergono nuovi concetti dalla conoscenza scientifica esistente
* **Computazionale**, dove scopriamo nuovi principi basati su esperimenti computazionali
* **Guidato dai dati**, basato sulla scoperta di relazioni e schemi nei dati  

## Altri campi correlati

Poiché i dati sono onnipresenti, la Data Science stessa è anche un campo ampio, che tocca molte altre discipline.

<dl>
<dt>Database</dt>
<dd>
Una considerazione critica è <b>come memorizzare</b> i dati, ovvero come strutturarli in modo da consentire un'elaborazione più rapida. Esistono diversi tipi di database che memorizzano dati strutturati e non strutturati, che <a href="../../2-Working-With-Data/README.md">considereremo nel nostro corso</a>.
</dd>
<dt>Big Data</dt>
<dd>
Spesso dobbiamo memorizzare ed elaborare grandi quantità di dati con una struttura relativamente semplice. Esistono approcci e strumenti speciali per memorizzare quei dati in modo distribuito su un cluster di computer e elaborarli in modo efficiente.
</dd>
<dt>Machine Learning</dt>
<dd>
Un modo per comprendere i dati è <b>costruire un modello</b> che sia in grado di prevedere un risultato desiderato. Sviluppare modelli dai dati è chiamato <b>machine learning</b>. Potresti voler dare un'occhiata al nostro <a href="https://aka.ms/ml-beginners">Curriculum di Machine Learning per Principianti</a> per saperne di più.
</dd>
<dt>Intelligenza Artificiale</dt>
<dd>
Un'area del machine learning nota come intelligenza artificiale (IA) si basa anch'essa sui dati e implica la costruzione di modelli di alta complessità che imitano i processi di pensiero umano. I metodi di IA spesso ci permettono di trasformare dati non strutturati (ad esempio, il linguaggio naturale) in intuizioni strutturate. 
</dd>
<dt>Visualizzazione</dt>
<dd>
Grandi quantità di dati sono incomprensibili per un essere umano, ma una volta che creiamo visualizzazioni utili utilizzando quei dati, possiamo comprenderli meglio e trarre alcune conclusioni. Pertanto, è importante conoscere molti modi per visualizzare le informazioni - qualcosa che tratteremo nella <a href="../../3-Data-Visualization/README.md">Sezione 3</a> del nostro corso. Campi correlati includono anche <b>Infografiche</b> e <b>Interazione Uomo-Computer</b> in generale. 
</dd>
</dl>

## Tipi di dati

Come abbiamo già accennato, i dati sono ovunque. Dobbiamo solo catturarli nel modo giusto! È utile distinguere tra dati **strutturati** e **non strutturati**. I primi sono tipicamente rappresentati in una forma ben strutturata, spesso come una tabella o un numero di tabelle, mentre i secondi sono solo una raccolta di file. A volte possiamo anche parlare di dati **semi-strutturati**, che hanno una sorta di struttura che può variare notevolmente.

| Strutturati                                                                 | Semi-strutturati                                                                               | Non strutturati                          |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------- |
| Elenco di persone con i loro numeri di telefono                             | Pagine di Wikipedia con collegamenti                                                          | Testo dell'Enciclopedia Britannica      |
| Temperatura in tutte le stanze di un edificio ogni minuto negli ultimi 20 anni | Raccolta di articoli scientifici in formato JSON con autori, data di pubblicazione e abstract | Condivisione di file con documenti aziendali |
| Dati sull'età e il sesso di tutte le persone che entrano nell'edificio      | Pagine Internet                                                                                | Flusso video grezzo da una telecamera di sorveglianza |

## Dove ottenere i dati

Ci sono molte possibili fonti di dati, ed è impossibile elencarle tutte! Tuttavia, menzioniamo alcune delle tipiche fonti da cui è possibile ottenere dati:

* **Strutturati**
  - **Internet delle cose** (IoT), inclusi dati da diversi sensori, come sensori di temperatura o pressione, fornisce molti dati utili. Ad esempio, se un edificio per uffici è dotato di sensori IoT, possiamo controllare automaticamente il riscaldamento e l'illuminazione per minimizzare i costi.
  - **Sondaggi** che chiediamo agli utenti di completare dopo un acquisto o dopo aver visitato un sito web.
  - **Analisi del comportamento** può, ad esempio, aiutarci a capire quanto profondamente un utente esplora un sito e qual è il motivo tipico per cui lascia il sito.
* **Non strutturati**
  - **Testi** possono essere una ricca fonte di intuizioni, come un punteggio complessivo di **sentimento**, o l'estrazione di parole chiave e significati semantici.
  - **Immagini** o **Video**. Un video da una telecamera di sorveglianza può essere utilizzato per stimare il traffico sulla strada e informare le persone su potenziali ingorghi.
  - **Log** dei server web possono essere utilizzati per capire quali pagine del nostro sito sono più spesso visitate e per quanto tempo.
* Semi-strutturati
  - I grafi dei **Social Network** possono essere ottime fonti di dati sulle personalità degli utenti e sull'efficacia potenziale nella diffusione delle informazioni.
  - Quando abbiamo una serie di fotografie da una festa, possiamo provare a estrarre dati sulla **dinamica di gruppo** costruendo un grafo delle persone che si fotografano insieme.

Conoscendo le diverse possibili fonti di dati, puoi provare a pensare a diversi scenari in cui le tecniche di Data Science possono essere applicate per comprendere meglio la situazione e migliorare i processi aziendali.

## Cosa puoi fare con i dati

Nella Data Science, ci concentriamo sui seguenti passaggi del percorso dei dati:

<dl>
<dt>1) Acquisizione dei dati</dt>
<dd>
Il primo passo è raccogliere i dati. Sebbene in molti casi possa essere un processo semplice, come i dati che arrivano a un database da un'applicazione web, a volte dobbiamo utilizzare tecniche speciali. Ad esempio, i dati provenienti dai sensori IoT possono essere travolgenti, ed è una buona pratica utilizzare endpoint di buffering come IoT Hub per raccogliere tutti i dati prima di ulteriori elaborazioni.
</dd>
<dt>2) Archiviazione dei dati</dt>
<dd>
Archiviare i dati può essere impegnativo, soprattutto se parliamo di big data. Quando si decide come archiviare i dati, ha senso anticipare il modo in cui si desidera interrogarli in futuro. Ci sono diversi modi in cui i dati possono essere archiviati:
<ul>
<li>Un database relazionale memorizza una raccolta di tabelle e utilizza un linguaggio speciale chiamato SQL per interrogarle. Tipicamente, le tabelle sono organizzate in diversi gruppi chiamati schemi. In molti casi, dobbiamo convertire i dati dalla forma originale per adattarli allo schema.</li>
<li><a href="https://en.wikipedia.org/wiki/NoSQL">Un database NoSQL</a>, come <a href="https://azure.microsoft.com/services/cosmos-db/?WT.mc_id=academic-77958-bethanycheum">CosmosDB</a>, non impone schemi sui dati e consente di memorizzare dati più complessi, ad esempio documenti JSON gerarchici o grafi. Tuttavia, i database NoSQL non hanno le ricche capacità di interrogazione di SQL e non possono imporre l'integrità referenziale, ovvero le regole su come i dati sono strutturati nelle tabelle e governano le relazioni tra le tabelle.</li>
<li><a href="https://en.wikipedia.org/wiki/Data_lake">L'archiviazione in Data Lake</a> è utilizzata per grandi raccolte di dati in forma grezza e non strutturata. I Data Lake sono spesso utilizzati con i big data, dove tutti i dati non possono essere contenuti in una sola macchina e devono essere memorizzati ed elaborati da un cluster di server. <a href="https://en.wikipedia.org/wiki/Apache_Parquet">Parquet</a> è il formato dei dati spesso utilizzato in combinazione con i big data.</li> 
</ul>
</dd>
<dt>3) Elaborazione dei dati</dt>
<dd>
Questa è la parte più entusiasmante del percorso dei dati, che comporta la conversione dei dati dalla loro forma originale in una forma che può essere utilizzata per la visualizzazione o l'addestramento di modelli. Quando si tratta di dati non strutturati come testi o immagini, potremmo dover utilizzare alcune tecniche di IA per estrarre <b>caratteristiche</b> dai dati, convertendoli così in forma strutturata.
</dd>
<dt>4) Visualizzazione / Intuizioni umane</dt>
<dd>
Spesso, per comprendere i dati, dobbiamo visualizzarli. Avendo molte tecniche di visualizzazione diverse nel nostro arsenale, possiamo trovare la giusta rappresentazione per ottenere un'intuizione. Spesso, un data scientist deve "giocare con i dati", visualizzandoli molte volte e cercando alcune relazioni. Inoltre, possiamo utilizzare tecniche statistiche per testare ipotesi o dimostrare una correlazione tra diversi pezzi di dati.   
</dd>
<dt>5) Addestramento di un modello predittivo</dt>
<dd>
Poiché l'obiettivo finale della Data Science è essere in grado di prendere decisioni basate sui dati, potremmo voler utilizzare le tecniche di <a href="http://github.com/microsoft/ml-for-beginners">Machine Learning</a> per costruire un modello predittivo. Possiamo quindi utilizzarlo per fare previsioni utilizzando nuovi set di dati con strutture simili.
</dd>
</dl>

Ovviamente, a seconda dei dati effettivi, alcuni passaggi potrebbero mancare (ad esempio, quando abbiamo già i dati nel database o quando non è necessario l'addestramento del modello), o alcuni passaggi potrebbero essere ripetuti più volte (come l'elaborazione dei dati).

## Digitalizzazione e Trasformazione Digitale

Nell'ultimo decennio, molte aziende hanno iniziato a comprendere l'importanza dei dati nel prendere decisioni aziendali. Per applicare i principi della Data Science alla gestione di un'azienda, è necessario prima raccogliere alcuni dati, ovvero tradurre i processi aziendali in forma digitale. Questo è noto come **digitalizzazione**. Applicare tecniche di Data Science a questi dati per guidare le decisioni può portare a significativi aumenti di produttività (o persino a un cambiamento radicale dell'azienda), chiamato **trasformazione digitale**.

Consideriamo un esempio. Supponiamo di avere un corso di Data Science (come questo) che offriamo online agli studenti e vogliamo utilizzare la Data Science per migliorarlo. Come possiamo farlo?

Possiamo iniziare chiedendoci "Cosa può essere digitalizzato?" Il modo più semplice sarebbe misurare il tempo che ogni studente impiega per completare ogni modulo e misurare la conoscenza acquisita somministrando un test a scelta multipla alla fine di ogni modulo. Calcolando la media del tempo di completamento tra tutti gli studenti, possiamo scoprire quali moduli causano maggiori difficoltà agli studenti e lavorare per semplificarli.
> Potresti sostenere che questo approccio non sia ideale, perché i moduli possono avere lunghezze diverse. Probabilmente sarebbe più equo dividere il tempo per la lunghezza del modulo (in numero di caratteri) e confrontare quei valori.

Quando iniziamo ad analizzare i risultati dei test a scelta multipla, possiamo cercare di determinare quali concetti gli studenti trovano difficili da comprendere e utilizzare queste informazioni per migliorare i contenuti. Per farlo, dobbiamo progettare i test in modo che ogni domanda corrisponda a un determinato concetto o blocco di conoscenza.

Se vogliamo complicare ulteriormente le cose, possiamo tracciare il tempo impiegato per ogni modulo rispetto alla categoria di età degli studenti. Potremmo scoprire che per alcune categorie di età ci vuole un tempo eccessivamente lungo per completare il modulo, o che gli studenti abbandonano prima di completarlo. Questo può aiutarci a fornire raccomandazioni di età per il modulo e minimizzare l'insoddisfazione delle persone derivante da aspettative errate.

## 🚀 Sfida

In questa sfida, cercheremo di individuare concetti rilevanti per il campo della Data Science analizzando dei testi. Prenderemo un articolo di Wikipedia sulla Data Science, scaricheremo e processeremo il testo, e poi costruiremo una nuvola di parole come questa:

![Nuvola di parole per Data Science](../../../../translated_images/it/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.png)

Visita [`notebook.ipynb`](../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') per leggere il codice. Puoi anche eseguire il codice e vedere come effettua tutte le trasformazioni dei dati in tempo reale.

> Se non sai come eseguire il codice in un Jupyter Notebook, dai un'occhiata a [questo articolo](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Quiz post-lezione](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Compiti

* **Compito 1**: Modifica il codice sopra per scoprire concetti correlati ai campi di **Big Data** e **Machine Learning**  
* **Compito 2**: [Pensa a scenari di Data Science](assignment.md)

## Crediti

Questa lezione è stata scritta con ♥️ da [Dmitry Soshnikov](http://soshnikov.com)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.