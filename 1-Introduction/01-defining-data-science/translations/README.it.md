# Definendo la  Data Science

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------: |
|              Definedo la  Data Science - _Sketchnote di [@nitya](https://twitter.com/nitya)_               |

---

[![Definendo la  Data Science Video](../images/video-def-ds.png)](https://youtu.be/beZ7Mb_oz9I)

## [Quiz pre-lezione](https://red-water-0103e7a0f.azurestaticapps.net/quiz/0)

## Cosa sono i Dati?
Nella vita di tutti i giorni, siamo costantemente circondati dai dati.Il testo che stai leggendo ora è parte dei dati. La lista dei numeri di telefono dei tuoi amici nel tuo smartphone fa parte dei dati, come anche l'ora mostrata dal tuo orologio in questo momento.Come abitudine umana, noi operiamo con i dati contando i soldi che abbamo, o scrivendo lettere ai nostri amici.

In ogni caso, i dati sono diventati più importanti con l'invenzione dei computers. Il ruolo principale dei computers è di fare calcoli, ma essi necessitano di dati per operare. Di conseguenza abbiamo bisogno di capire come i computers processano i dati.

Con l'emergere di Internet, il ruolo dei computers come manipolatori di dati è aumentato. Se pensi che, noi ora usiamo i computer sempre più per processare dati e per comunicare piuttosto che per calcoli effettivi. Quando scriviamo una e-mail ad un amico o cerchiamo delle informazioni online - noi stiamo essenzialmente creando, immagazinando, trasmettendo e manipolando dati. 
> Riesci a ricordate l'ultima volta che hai usato il computer per fare effettivamente dei calcoli?

## Cos'è la Data Science?

Su [Wikipedia](https://en.wikipedia.org/wiki/Data_science), **Data Science** è definita come  *un campo scientifico che fa uso di metodi scientifici al fine di estrarre informazioni e intuizioni da dati struttirati e non , e applica conoscenze e approfondimenti attuabili dai dati in un'ampia gamma di domini applicativi*

This definition highlights the following important aspects of data science:

* Lo scopo principale della data science è di **estrarre informazioni** dai dati, in altre parole - di **tradurre** i dati, trovare delle relazioni nascoste e costruire un **modello**
* La data science usa **metodi scientifici**, come la probabilità e la statistica, Infatti, quando il termine *data science* è stato inizialmente introdotto, alcune persone contestarono che data science era solamente un nominativo fantasioso per indicare la statistica, Oggigiorno è chiaro che si tratta di un campo molto più ampio. 
* Le informazioni ottenute dovrebbero essere applicate per produrre delle **intuizioni attuabili** o meglio intuizioni pratiche che si possono applicare alla reale situazione di un'azienda.
* Noi dovremmo essere in grado di operare su entrambi i tipi di dati, **strutturati** e **non strutturati**. Discuteremo i diversi tipi di dati più avanti nel corso.
* **Dominio applicativo**  è un concetto importante , e i data scientists spesso necessitano almeno di un certo grado di esperienza nel settore del problema, per esempio: finanza, medicina, marketing, etc.


> Un altro aspetto importante della Data Science è che studia come i dati possono essere raccolti, immagazzinati ed elaborati attraverso i computers. Mentre la statistica ci da un fondamento matematico, la data science applica i concetti matematici per creare delle reali intuizioni dai dati.

Uno dei modi  (attribuito a [Jim Gray](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) per vedere la data science è quello di considerarla come l'essere un paradigma separato della scienza:
* **Empirica**, nella quale noi ci affidiamo principalmente a osservazioni e risultati di esperimenti
* **Teorica**, dove nuovi concetti emergono dalla esistente conoscenza scientifica 
* **Computazionale**, dove noi scopriamo nuovi principi basandoci su esperimenti computazionali
* **Guidata dai dati**, basata sulla scoperta di realzioni tra i dati

## Altri campi correlati

Poiché i dati sono pervasivi, la scienza dei dati stessa è anche un campo ampio, che tocca molte altre discipline.

<dl>
<dt>Databases</dt>
<dd>
Una considerazione critica riguarda **come immagazzinare** i dati, o meglio, come struttirarli in modo da consentire una processazion più veloce . Ci sono vari tipi di database, che immagazzinano dati strutturati e non, che <a href="../../2-Working-With-Data/README.md">considereremo nel nostro corso</a>.
A critical consideration is **how to store** the data, i.e. how to structure it in a way that allows faster processing.  There are different types of databases that store structured and unstructured data, which <a href="../../2-Working-With-Data/README.md">we will consider in our course</a>.
</dd>
<dt>Big Data</dt>
<dd>
Spesso necessitiamo di immagazzinare e processare un quantità ingente di dati con strutture relativamente semplici. Esistono approcci e strumenti speciali per immagazzinare quei dati in modo distribuito in un sistema di computers e processarli in modo efficace.
</dd>
<dt>Machine Learning</dt>
<dd>
Un modo per trarre informazioni dai dati è quello di **costruire un modello** che predirrà un risultato desiderato. Lo sviluppo di modelli dai dati è chiamato **machine learning**. Penso vorrai dare uno sguardo al nostro corso <a href="https://aka.ms/ml-beginners">Machine Learning for Beginners</a>  per apprenderne di più.
</dd>
<dt>Intelligenza Artificiale</dt>
<dd>
Un area del machine learning conosciuta come ingelligenza artificiale (AI) anch essa si riferisce ai dati, e comprende la creazione di modelli di alta complessità che imitano gli umani attraverso i processi. I metodi di AI spesso ci consentono di rendere i dati non strutturati (es. linguaggio naturale) delle intuizioni strutturate.
</dd>
<dt>Visualizzazione</dt>
<dd>
Una grossa quantità di dati è incomprensibile agli umani, ma una volta creati dei modi utili di vedere questi dati, possiamo trarne un significato migliore, e trarre delle conclusioni. Così questo è importante per conoscere più modi per visualizzare informazioni - cosa che tratteremo nella <a href="../../3-Data-Visualization/README.md">Sezione 3</a> del nostro corso. Campi affini includono anche **Infografica**, e **Interazione Uomo-macchina** in generale.
</dd>
</dl>

## Tipi di Dati 

Come abbiamo già menzionato, i dati sono dappertutto. Abbiamo solo bisogno di capirli nel modo corretto! È utile distinguerli tra dati **strutturati** e **non strutturati**. Il primo è solitamente rappresentato in forma ben strutturata, spesso come una tabella o più tabelle, mentre il secondo è semplicemente un insieme di files. A volte possiamo anche parlare di dati **semi-strutturati**, che hanno una sorta di struttura che può variare in maniera significativa.

| Struttirati                                                                      | Semi-strutturati                                                                                       | Non strutturati                         |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------- |
| Lista di persone con il loro numero di telefono                                  | Pagina Wikipedia con dei links                                                                         | Testo dall'enciclopedia Britannica      |
| Temperature in tutte le stanze di un edificio a ogni minuto degli scorsi 20 anni | Collezione di documentazione scientifica in formato JSON con autore, data di pubblicazione e riassunto | File condiviso con documenti allegati   |
| Dati per anno e genere di tutte le persone che entrano in un edificio            | Pagine internet                                                                                        | Video delle telecamere di sorveglianza  |

## Dove reperire i dati 

Ci sono varie possibili fonti di dati, e sarebbe impossibile elencarle tutte! In ogni caso, menzioneremo alcuni dei più comuni:

* **Strutturati**
  - **Internet of Things** (IoT), includendo dati da sensori differenti, come sensori di temperatura o pressione, da cui ricaviamo dati utili. Per esempio, se un ufficio è dotato di sensori IoT, possiamo automaticamente controllare il riscaldamento e l'illuminazione in modo da minimizzare i costi.
  - **Sondaggi** che si fanno compilare agli utenti dopo aver comprato o aver visitato un sito web.
  - **Analisi del comportamento** che può, per esempio, aiutarci a capire quanto profondamente un utente va in un sito, e qual'è la motivazione per cui di solito abbandona il sito. 
* **Non strutturati**
  - **Testi** possono essere una grossa fonte di intuizioni, come un generale **punteggio sentimentale**, o l'estrazione di parole chiave e significati semantici.
  - **Immagini** o **Video**. Un video di una telecamera di video-sorveglianza può essere usato per stimare il traffico su una strada, e informare le persone riguardo a potenziali ingorghi stradali.
  - Web server **Logs** possono essere usati per capire che pagine di un sito web sono le più visitate e per quanto. 
* Semi-strutturati
  - grafici provenienti da **Social Networks** possono essere ottime risorse di dati riguardo a personalità e potenziale efficacia nella diffusione di informazioni.  
  - Quando abbiamo alcune forografie di una festa, possiamo provare ad estrarre le **Dinamiche di gruppo** dalla creazione di  un grafico delle persone che si fanno foto con altre persone.

Conoscendo diverse possibili fonti di dati, possiamo provare a pensare a scenari differenti dove le tecniche di data science possono essere applicate per conoscere meglio la situazione, e per migliorare i processi di un'azienda.

## Cosa si può fare con i dati 

Nella Data Science, noi ci concentriamo sui seguenti passaggi nel nostro cammino : 

<dl>
<dt>1) Acquisizione di dati</dt>
<dd>
Il primo step è quello di raccogliere dati. Mentre in molti casi potrebbe essere un processo diretto, come i dati provenienti da un database di una applicazione web, a volte necessitiamo di tecniche speciali. Per esempio, i dati di un sensore IoT possono essere fuorvianti, è una buona pratica utilizzare endpoint di buffering come IoT Hub per raccogliere tutti i dati prima di un'ulteriore elaborazione.
</dd>
<dt>2) Immagazzinamento dei dati</dt>
<dd>
Immagazzinare i dati può essere una sfida, specialmente se si tratta di big data. Quando decidiamo come immagazzinare i dati, ha senso anticipare il modo in cui andrai ad immagazzinare i dati in futuro. Ci sono vari dati che possono essere immagazzinati:
<ul>
<li>Un database relazionale contiene un insieme di tabelle, e usa un speciale linguaggio chiamato SQL per ricercare i dati. Di solito, le tabelle sono organizzate in gruppi differenti chiamati schemi. In vari casi abbiamo bisogno di convertire i dati dalla forma originale per adattarli allo schema.</li>
<li><a href="https://en.wikipedia.org/wiki/NoSQL">Un NonSQL</a> database, come per esempio <a href="https://azure.microsoft.com/services/cosmos-db/?WT.mc_id=academic-31812-dmitryso">CosmosDB</a>, non forza degli schemi sui dati , e permette di immagazzinare dati più complessi, per esempio una gerarchia di documenti JSON o grafici. Tuttavia, i NonSQL databases non hanno la capienza di quelli SQL, e non  possono far rispettare l'integrità referenziale, anche dette regole su come i dati sono strutturati in tabelle e come sono relazionati tra tabelle.</li>
<li><a href="https://en.wikipedia.org/wiki/Data_lake">Data Lake</a> uno spazio per contenere grosse quantità di dati, in forma non strutturata. I Data Lakes sono spesso usati con i big data, dove non possono essere inseriti in un unica macchina e devono essere immagazzinati e processati da un insieme di servers. <a href="https://en.wikipedia.org/wiki/Apache_Parquet">Parquet</a> è il formato per i dati spesso usato in congiunzione con big datas.</li> 
</ul>
</dd>
<dt>3) Processazione dei Dati</dt>
<dd>
Questa è la parte più divertende del percorso dei dati, che comprende la conversione di dati dalla forma originale in forme che possono essere usate per la visualizzazione / allenamento di modelli. Quando si ha a che fare con dati non strutturati come testi o immagini, abbiamo bisogno di tecniche di AI per estrarre **caratteristiche** dai dati, in modo da convertirti in strutturati.
</dd>
<dt>4) Visualizzazione / Intuizioni umane</dt>
<dd>
Spesso per fare in modo di capire i dati, necessitiamo di visualizzarli. Avere varie tecniche di visualizzazione nella nostra cassetta degli attressi ci consente di trovare il giusto punto di vista per trarre delle conclusioni dai nostri dati. Spesso i data scientist hanno necessità di "giocare con i dati", visualizzarli varie volte per trovare delle relazioni. Inoltre noi potremmo usare delle tecniche statistiche per testare un'ipotesi o provare una correlazione tra diversi pezzi di dati.
</dd>
<dt>5) Allenamento di un modello predittivo</dt>
<dd>
Siccome l'ultimo obbiettivo della data science è quello di essere in grado di prendere decisioni basate sui dati, potremmo voler usare tecniche di <a href="http://github.com/microsoft/ml-for-beginners">Machine Learning</a> per creare un modello predittivo. Possiamo usare questo poi per fare predizioni usando nuovi data sets con strutture simili.
</dd>
</dl>

Ovviamente in base ai dati attuali, alcuni steps potrebbero mancare (es. quando abbiamo già i dati nel database, o quando non necessitiamo di allenare un modello), o alcuni steps potrebbero essere ripetuti più volte (come la processazione dei dati).

## Digitalizzazione e Trasformazione Digitale 

Nell'ultimo decennio, varie aziende hanno iniziato a capire l'importanza dei dati quando si prendono decisioni. Per applicare i principi della data science ad un business già avviato, inizialmente bisogna raccogliere dei dati , o meglio tradurre il processo di business in una forma digitale . Questa è conosciuta come **digitalizzazione**. Applicare le tecniche di data sceince a questi dati per guidare decisioni può incidere significativamente nella produttività ( o anche il perno aziendale ), chiamato **digital transformation**.

Consideriamo un esempio. supponiamo di avere un corso di data science (come questo) che teniamo online per gli studenti, e vogliamo usare la data science per migliorarlo. Come possiamo fare?
 
Possiamo iniziare chiedendoci "cosa può essere digitalizzato?" Il modo più semplice sarebbe quello di misurare il tempo che ogni studente impiega a completare ogni modulo, e per misurare l'apprendimento si potrebbe utilizzare un test a risposta multipla alla fine di ogni modulo. Dalla media del tempo per il completamento del test da parte degli studenti possiamo capire quale modulo crea la maggiore difficoltà per gli studenti e lavorarci per semplificarlo.

>Potresti essere in disaccordo a questo approccio dicendo che non sia ottimale, perchè il modulo può essere di diversa lunghezza. È probabilmente più corretto dividere il tempo per la lunghezza del modulo (numero di caratteri), e confrontare quei valori piuttosto.

Quando iniziamo ad analizzare i risultati dei test a risposta multipla, possiamo provare a determinare quali concetti gli studenti hanno maggiore difficoltà ad apprendere, e usare quelle informazioni per migliorare il contenuto. Per farlo abbiamo bisogno di creare dei tests in modo che ogni domanda copra un certo concetto o porzione di materiale.

Se vogliamo complicare ancora la situazione, possiamo fare un grafico del tempo impiegato per ogni modulo a confronto con la categoria d' età degli studenti. Potremmo trovare che alcune categorie d'età impiegano un tempo inappropriatamente lungo per completare il modulo, o che alcuni studenti abbandonano prima di completarlo. Questo ci può aiutare fornandoci un'età di raccomandazione per il modulo in questione, e minimizzare la insoddisfazione delle persone per delle aspettative sbagliate.

## 🚀 Challenge

in questa challenge, proveremo a trovare concetti importanti per il campo della data science e cercare dei testi. Prenderemo degli articoli di Wikipedia di Data Science, li scaricheremo e processeremo il testo, e poi costruiremo un cloud di parole come questo:

![Word Cloud per la Data Science](../images/ds_wordcloud.png)

Visita [`notebook.ipynb`](/1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') per leggere il codice. Puoi anche eseguire il codice , e vedere com funzionano tutte le trasformazioni di dati in tempo reale. 

> Se non sai come eseguire il codice in un Notebook Jupyter guarda [questo articolo](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).



## [Quiz Scorsa lezione](https://red-water-0103e7a0f.azurestaticapps.net/quiz/1)

## Compiti

* **Compito 1**: Modifica il codice sopra per trovare i concetti legati ai campi di **Big Data** e **Machine Learning**
* **Compito 2**: [Pensa agli scenari da Data Science](assignment.md)

## Crediti

Questa lezione è stata creata con  ♥️ da [Dmitry Soshnikov](http://soshnikov.com)
