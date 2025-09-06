<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2baeafe1db4d58ee5b8ec85db9de728a",
  "translation_date": "2025-09-06T08:44:00+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "it"
}
-->
# Il ciclo di vita della Data Science: Analisi

|![ Sketchnote di [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Ciclo di vita della Data Science: Analisi - _Sketchnote di [@nitya](https://twitter.com/nitya)_ |

## Quiz Pre-Lettura

## [Quiz Pre-Lettura](https://ff-quizzes.netlify.app/en/ds/quiz/28)

L'analisi nel ciclo di vita dei dati conferma che i dati possono rispondere alle domande proposte o risolvere un problema specifico. Questo passaggio può anche concentrarsi sul verificare che un modello stia affrontando correttamente queste domande e problemi. Questa lezione si focalizza sull'Analisi Esplorativa dei Dati (Exploratory Data Analysis o EDA), che comprende tecniche per definire caratteristiche e relazioni all'interno dei dati e può essere utilizzata per preparare i dati alla modellazione.

Utilizzeremo un dataset di esempio proveniente da [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) per mostrare come applicare queste tecniche con Python e la libreria Pandas. Questo dataset contiene un conteggio di alcune parole comuni trovate nelle email, le fonti di queste email sono anonime. Usa il [notebook](../../../../4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) in questa directory per seguire il contenuto.

## Analisi Esplorativa dei Dati

La fase di acquisizione del ciclo di vita è quella in cui i dati vengono raccolti insieme ai problemi e alle domande da affrontare, ma come possiamo sapere se i dati possono supportare il risultato finale? 
Ricorda che un data scientist potrebbe porsi le seguenti domande quando acquisisce i dati:
-   Ho abbastanza dati per risolvere questo problema?
-   I dati sono di qualità accettabile per questo problema?
-   Se scopro ulteriori informazioni attraverso questi dati, dovremmo considerare di cambiare o ridefinire gli obiettivi?

L'Analisi Esplorativa dei Dati è il processo di conoscenza dei dati e può essere utilizzata per rispondere a queste domande, oltre a identificare le sfide nel lavorare con il dataset. Concentriamoci su alcune delle tecniche utilizzate per raggiungere questi obiettivi.

## Profilazione dei Dati, Statistiche Descrittive e Pandas
Come possiamo valutare se abbiamo abbastanza dati per risolvere questo problema? La profilazione dei dati può riassumere e raccogliere alcune informazioni generali sul nostro dataset attraverso tecniche di statistiche descrittive. La profilazione dei dati ci aiuta a capire cosa abbiamo a disposizione, mentre le statistiche descrittive ci aiutano a comprendere quante cose sono disponibili.

In alcune delle lezioni precedenti, abbiamo utilizzato Pandas per fornire alcune statistiche descrittive con la funzione [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Questa funzione fornisce il conteggio, i valori massimi e minimi, la media, la deviazione standard e i quantili sui dati numerici. Utilizzare statistiche descrittive come la funzione `describe()` può aiutarti a valutare quanto hai a disposizione e se hai bisogno di più dati.

## Campionamento e Query
Esplorare tutto in un grande dataset può richiedere molto tempo ed è un compito che solitamente viene affidato a un computer. Tuttavia, il campionamento è uno strumento utile per comprendere i dati e permette di avere una migliore comprensione di ciò che è presente nel dataset e di cosa rappresenta. Con un campione, puoi applicare probabilità e statistiche per arrivare a conclusioni generali sui tuoi dati. Sebbene non ci sia una regola definita su quanto campionare, è importante notare che più dati campioni, più precisa sarà la generalizzazione che puoi fare sui dati.

Pandas ha la funzione [`sample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) nella sua libreria, dove puoi passare un argomento per indicare quanti campioni casuali desideri ricevere e utilizzare.

Le query generali sui dati possono aiutarti a rispondere a domande e teorie generali che potresti avere. A differenza del campionamento, le query ti permettono di avere controllo e concentrarti su parti specifiche dei dati su cui hai domande. La funzione [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) nella libreria Pandas ti consente di selezionare colonne e ottenere risposte semplici sui dati attraverso le righe recuperate.

## Esplorazione con Visualizzazioni
Non è necessario aspettare che i dati siano completamente puliti e analizzati per iniziare a creare visualizzazioni. Infatti, avere una rappresentazione visiva durante l'esplorazione può aiutare a identificare modelli, relazioni e problemi nei dati. Inoltre, le visualizzazioni offrono un mezzo di comunicazione con coloro che non sono coinvolti nella gestione dei dati e possono rappresentare un'opportunità per condividere e chiarire ulteriori domande che non sono state affrontate nella fase di acquisizione. Consulta la [sezione sulle Visualizzazioni](../../../../../../../../../3-Data-Visualization) per saperne di più su alcuni modi popolari di esplorare visivamente.

## Esplorazione per identificare incoerenze
Tutti gli argomenti trattati in questa lezione possono aiutare a identificare valori mancanti o incoerenti, ma Pandas fornisce funzioni per verificare alcuni di questi. [isna() o isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) possono controllare i valori mancanti. Un aspetto importante dell'esplorazione di questi valori nei tuoi dati è capire perché si sono verificati in primo luogo. Questo può aiutarti a decidere quali [azioni intraprendere per risolverli](../../../../../../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Quiz Post-Lettura](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Compito

[Esplorare per risposte](assignment.md)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.