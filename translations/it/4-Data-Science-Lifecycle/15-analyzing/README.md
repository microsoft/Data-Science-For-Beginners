<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d92f57eb110dc7f765c05cbf0f837c77",
  "translation_date": "2025-08-28T10:56:04+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "it"
}
-->
# Il Ciclo di Vita della Data Science: Analisi

|![ Sketchnote di [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Ciclo di Vita della Data Science: Analisi - _Sketchnote di [@nitya](https://twitter.com/nitya)_ |

## Quiz Pre-Lezione

## [Quiz Pre-Lezione](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

L'analisi nel ciclo di vita dei dati conferma che i dati possono rispondere alle domande proposte o risolvere un problema specifico. Questo passaggio si concentra anche sul verificare che un modello stia affrontando correttamente queste domande e problemi. Questa lezione è focalizzata sull'Analisi Esplorativa dei Dati (Exploratory Data Analysis o EDA), che comprende tecniche per definire caratteristiche e relazioni all'interno dei dati e può essere utilizzata per preparare i dati alla modellazione.

Utilizzeremo un dataset di esempio da [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) per mostrare come applicare queste tecniche con Python e la libreria Pandas. Questo dataset contiene un conteggio di alcune parole comuni trovate nelle email, le cui fonti sono anonime. Usa il [notebook](notebook.ipynb) in questa directory per seguire il contenuto.

## Analisi Esplorativa dei Dati

La fase di acquisizione del ciclo di vita è dove i dati vengono raccolti insieme ai problemi e alle domande da affrontare, ma come possiamo sapere se i dati possono supportare il risultato finale? 
Ricorda che un data scientist potrebbe porsi le seguenti domande quando acquisisce i dati:
-   Ho abbastanza dati per risolvere questo problema?
-   I dati sono di qualità accettabile per questo problema?
-   Se scopro ulteriori informazioni attraverso questi dati, dovremmo considerare di cambiare o ridefinire gli obiettivi?

L'Analisi Esplorativa dei Dati è il processo di familiarizzazione con i dati e può essere utilizzata per rispondere a queste domande, oltre a identificare le sfide nel lavorare con il dataset. Concentriamoci su alcune delle tecniche utilizzate per raggiungere questi obiettivi.

## Profilazione dei Dati, Statistiche Descrittive e Pandas
Come possiamo valutare se abbiamo abbastanza dati per risolvere questo problema? La profilazione dei dati può riassumere e raccogliere alcune informazioni generali sul nostro dataset attraverso tecniche di statistiche descrittive. La profilazione dei dati ci aiuta a capire cosa è disponibile, mentre le statistiche descrittive ci aiutano a comprendere quante cose sono disponibili.

In alcune delle lezioni precedenti, abbiamo utilizzato Pandas per fornire alcune statistiche descrittive con la funzione [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Questa funzione fornisce il conteggio, i valori massimi e minimi, la media, la deviazione standard e i quantili sui dati numerici. Utilizzare statistiche descrittive come la funzione `describe()` può aiutarti a valutare quanto hai e se hai bisogno di più dati.

## Campionamento e Interrogazione
Esplorare tutto in un grande dataset può richiedere molto tempo ed è un compito che di solito viene lasciato a un computer. Tuttavia, il campionamento è uno strumento utile per comprendere i dati e permette di avere una migliore comprensione di ciò che è presente nel dataset e di cosa rappresenta. Con un campione, puoi applicare probabilità e statistiche per trarre alcune conclusioni generali sui tuoi dati. Sebbene non ci sia una regola definita su quanto campionare, è importante notare che più dati campioni, più precise saranno le generalizzazioni che puoi fare sui dati. 

Pandas ha la funzione [`sample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) nella sua libreria, dove puoi passare un argomento per specificare quanti campioni casuali desideri ricevere e utilizzare.

L'interrogazione generale dei dati può aiutarti a rispondere a domande e teorie generali che potresti avere. A differenza del campionamento, le interrogazioni ti permettono di avere controllo e concentrarti su parti specifiche dei dati su cui hai domande. La funzione [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) nella libreria Pandas ti consente di selezionare colonne e ottenere risposte semplici sui dati attraverso le righe recuperate.

## Esplorare con Visualizzazioni
Non è necessario aspettare che i dati siano completamente puliti e analizzati per iniziare a creare visualizzazioni. Infatti, avere una rappresentazione visiva durante l'esplorazione può aiutare a identificare schemi, relazioni e problemi nei dati. Inoltre, le visualizzazioni forniscono un mezzo di comunicazione con coloro che non sono coinvolti nella gestione dei dati e possono rappresentare un'opportunità per condividere e chiarire ulteriori domande che non sono state affrontate nella fase di acquisizione. Consulta la [sezione sulle Visualizzazioni](../../../../../../../../../3-Data-Visualization) per saperne di più su alcuni modi popolari per esplorare visivamente.

## Esplorare per identificare incoerenze
Tutti gli argomenti trattati in questa lezione possono aiutare a identificare valori mancanti o incoerenti, ma Pandas fornisce funzioni per controllare alcuni di questi. [isna() o isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) possono controllare i valori mancanti. Un aspetto importante dell'esplorazione di questi valori nei tuoi dati è capire perché si sono verificati in primo luogo. Questo può aiutarti a decidere quali [azioni intraprendere per risolverli](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Quiz Pre-Lezione](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/27)

## Compito

[Esplorare per risposte](assignment.md)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.