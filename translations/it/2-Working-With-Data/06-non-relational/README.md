<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c182e87f9f80be7e7cdffc7b40bbfccf",
  "translation_date": "2025-09-06T08:41:23+00:00",
  "source_file": "2-Working-With-Data/06-non-relational/README.md",
  "language_code": "it"
}
-->
# Lavorare con i dati: Dati non relazionali

|![ Sketchnote di [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/06-NoSQL.png)|
|:---:|
|Lavorare con i dati NoSQL - _Sketchnote di [@nitya](https://twitter.com/nitya)_ |

## [Quiz Pre-Lezione](https://ff-quizzes.netlify.app/en/ds/quiz/10)

I dati non sono limitati ai database relazionali. Questa lezione si concentra sui dati non relazionali e coprirà le basi dei fogli di calcolo e del NoSQL.

## Fogli di calcolo

I fogli di calcolo sono un modo popolare per archiviare ed esplorare i dati perché richiedono meno lavoro per essere configurati e utilizzati. In questa lezione imparerai i componenti di base di un foglio di calcolo, oltre a formule e funzioni. Gli esempi saranno illustrati con Microsoft Excel, ma la maggior parte delle parti e degli argomenti avrà nomi e passaggi simili rispetto ad altri software di fogli di calcolo.

![Un foglio di lavoro vuoto di Microsoft Excel con due schede](../../../../2-Working-With-Data/06-non-relational/images/parts-of-spreadsheet.png)

Un foglio di calcolo è un file e sarà accessibile nel file system di un computer, dispositivo o sistema di file basato su cloud. Il software stesso può essere basato su browser o un'applicazione che deve essere installata su un computer o scaricata come app. In Excel questi file sono definiti anche come **workbook** e questa terminologia sarà utilizzata per il resto della lezione.

Un workbook contiene una o più **worksheets**, dove ogni worksheet è etichettata con delle schede. All'interno di una worksheet ci sono rettangoli chiamati **celle**, che contengono i dati effettivi. Una cella è l'intersezione di una riga e una colonna, dove le colonne sono etichettate con caratteri alfabetici e le righe con numeri. Alcuni fogli di calcolo contengono intestazioni nelle prime righe per descrivere i dati in una cella.

Con questi elementi di base di un workbook Excel, utilizzeremo un esempio da [Microsoft Templates](https://templates.office.com/) focalizzato su un inventario per esaminare alcune parti aggiuntive di un foglio di calcolo.

### Gestione di un inventario

Il file del foglio di calcolo chiamato "InventoryExample" è un foglio di calcolo formattato di articoli all'interno di un inventario che contiene tre worksheets, dove le schede sono etichettate "Inventory List", "Inventory Pick List" e "Bin Lookup". La riga 4 della worksheet Inventory List è l'intestazione, che descrive il valore di ogni cella nella colonna dell'intestazione.

![Una formula evidenziata da un esempio di lista inventario in Microsoft Excel](../../../../2-Working-With-Data/06-non-relational/images/formula-excel.png)

Ci sono casi in cui una cella dipende dai valori di altre celle per generare il proprio valore. Il foglio di calcolo Inventory List tiene traccia del costo di ogni articolo nel suo inventario, ma cosa succede se abbiamo bisogno di sapere il valore di tutto l'inventario? [**Le formule**](https://support.microsoft.com/en-us/office/overview-of-formulas-34519a4e-1e8d-4f4b-84d4-d642c4f63263) eseguono azioni sui dati delle celle e vengono utilizzate per calcolare il costo dell'inventario in questo esempio. Questo foglio di calcolo utilizza una formula nella colonna Inventory Value per calcolare il valore di ogni articolo moltiplicando la quantità sotto l'intestazione QTY e i suoi costi dalle celle sotto l'intestazione COST. Facendo doppio clic o evidenziando una cella verrà mostrata la formula. Noterai che le formule iniziano con un segno di uguale, seguito dal calcolo o dall'operazione.

![Una funzione evidenziata da un esempio di lista inventario in Microsoft Excel](../../../../2-Working-With-Data/06-non-relational/images/function-excel.png)

Possiamo utilizzare un'altra formula per sommare tutti i valori di Inventory Value e ottenere il valore totale. Questo potrebbe essere calcolato sommando ogni cella per generare la somma, ma può essere un compito tedioso. Excel ha [**funzioni**](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89), ovvero formule predefinite per eseguire calcoli sui valori delle celle. Le funzioni richiedono argomenti, che sono i valori necessari per eseguire questi calcoli. Quando le funzioni richiedono più di un argomento, devono essere elencate in un ordine specifico o la funzione potrebbe non calcolare il valore corretto. Questo esempio utilizza la funzione SUM e utilizza i valori di Inventory Value come argomento per generare il totale elencato sotto la riga 3, colonna B (anche indicata come B3).

## NoSQL

NoSQL è un termine generico per i diversi modi di archiviare dati non relazionali e può essere interpretato come "non-SQL", "non-relazionale" o "non solo SQL". Questi tipi di sistemi di database possono essere classificati in 4 tipi.

![Rappresentazione grafica di un archivio dati chiave-valore che mostra 4 chiavi numeriche uniche associate a 4 valori diversi](../../../../2-Working-With-Data/06-non-relational/images/kv-db.png)
> Fonte da [Blog di Michał Białecki](https://www.michalbialecki.com/2018/03/18/azure-cosmos-db-key-value-database-cloud/)

I database [Key-value](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#keyvalue-data-stores) associano chiavi uniche, che sono identificatori unici associati a un valore. Queste coppie sono archiviate utilizzando una [tabella hash](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/) con una funzione di hashing appropriata.

![Rappresentazione grafica di un archivio dati a grafo che mostra le relazioni tra persone, i loro interessi e le loro posizioni](../../../../2-Working-With-Data/06-non-relational/images/graph-db.png)
> Fonte da [Microsoft](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/graph-introduction#graph-database-by-example)

I database [Graph](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#graph-data-stores) descrivono le relazioni nei dati e sono rappresentati come una raccolta di nodi e archi. Un nodo rappresenta un'entità, qualcosa che esiste nel mondo reale come uno studente o un estratto conto bancario. Gli archi rappresentano la relazione tra due entità. Ogni nodo e arco ha proprietà che forniscono informazioni aggiuntive su ciascun nodo e arco.

![Rappresentazione grafica di un archivio dati colonnare che mostra un database clienti con due famiglie di colonne chiamate Identità e Informazioni di Contatto](../../../../2-Working-With-Data/06-non-relational/images/columnar-db.png)

Gli archivi dati [Columnar](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#columnar-data-stores) organizzano i dati in colonne e righe come una struttura dati relazionale, ma ogni colonna è divisa in gruppi chiamati famiglie di colonne, dove tutti i dati sotto una colonna sono correlati e possono essere recuperati e modificati in un'unica unità.

### Archivi dati documentali con Azure Cosmos DB

Gli archivi dati [Document](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#document-data-stores) si basano sul concetto di archivio dati chiave-valore e sono costituiti da una serie di campi e oggetti. Questa sezione esplorerà i database documentali con l'emulatore Cosmos DB.

Un database Cosmos DB si adatta alla definizione di "Non Solo SQL", dove il database documentale di Cosmos DB si basa su SQL per interrogare i dati. La [lezione precedente](../05-relational-databases/README.md) su SQL copre le basi del linguaggio e saremo in grado di applicare alcune delle stesse query a un database documentale qui. Utilizzeremo l'emulatore Cosmos DB, che ci consente di creare ed esplorare un database documentale localmente su un computer. Leggi di più sull'emulatore [qui](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21).

Un documento è una raccolta di campi e valori di oggetti, dove i campi descrivono cosa rappresenta il valore dell'oggetto. Di seguito è riportato un esempio di documento.

```json
{
    "firstname": "Eva",
    "age": 44,
    "id": "8c74a315-aebf-4a16-bb38-2430a9896ce5",
    "_rid": "bHwDAPQz8s0BAAAAAAAAAA==",
    "_self": "dbs/bHwDAA==/colls/bHwDAPQz8s0=/docs/bHwDAPQz8s0BAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f95-010a691e01d7\"",
    "_attachments": "attachments/",
    "_ts": 1630544034
}
```

I campi di interesse in questo documento sono: `firstname`, `id` e `age`. Gli altri campi con gli underscore sono stati generati da Cosmos DB.

#### Esplorare i dati con l'emulatore Cosmos DB

Puoi scaricare e installare l'emulatore [per Windows qui](https://aka.ms/cosmosdb-emulator). Consulta questa [documentazione](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos) per le opzioni su come eseguire l'emulatore su macOS e Linux.

L'emulatore avvia una finestra del browser, dove la vista Explorer consente di esplorare i documenti.

![La vista Explorer dell'emulatore Cosmos DB](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-explorer.png)

Se stai seguendo, clicca su "Start with Sample" per generare un database di esempio chiamato SampleDB. Se espandi SampleDB cliccando sulla freccia troverai un contenitore chiamato `Persons`, un contenitore contiene una raccolta di elementi, che sono i documenti all'interno del contenitore. Puoi esplorare i quattro documenti individuali sotto `Items`.

![Esplorare dati di esempio nell'emulatore Cosmos DB](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons.png)

#### Interrogare i dati documentali con l'emulatore Cosmos DB

Possiamo anche interrogare i dati di esempio cliccando sul pulsante nuova query SQL (secondo pulsante da sinistra).

`SELECT * FROM c` restituisce tutti i documenti nel contenitore. Aggiungiamo una clausola where e troviamo tutti quelli con meno di 40 anni.

`SELECT * FROM c where c.age < 40`

![Eseguire una query SELECT sui dati di esempio nell'emulatore Cosmos DB per trovare documenti che hanno un valore del campo age inferiore a 40](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons-query.png)

La query restituisce due documenti, nota che il valore age per ciascun documento è inferiore a 40.

#### JSON e documenti

Se hai familiarità con JavaScript Object Notation (JSON) noterai che i documenti sembrano simili a JSON. C'è un file `PersonsData.json` in questa directory con più dati che puoi caricare nel contenitore Persons nell'emulatore tramite il pulsante `Upload Item`.

Nella maggior parte dei casi, le API che restituiscono dati JSON possono essere trasferite direttamente e archiviate nei database documentali. Di seguito è riportato un altro documento, rappresenta tweet dall'account Twitter di Microsoft che sono stati recuperati utilizzando l'API di Twitter, quindi inseriti in Cosmos DB.

```json
{
    "created_at": "2021-08-31T19:03:01.000Z",
    "id": "1432780985872142341",
    "text": "Blank slate. Like this tweet if you’ve ever painted in Microsoft Paint before. https://t.co/cFeEs8eOPK",
    "_rid": "dhAmAIUsA4oHAAAAAAAAAA==",
    "_self": "dbs/dhAmAA==/colls/dhAmAIUsA4o=/docs/dhAmAIUsA4oHAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f84-a0958ad901d7\"",
    "_attachments": "attachments/",
    "_ts": 1630537000
```

I campi di interesse in questo documento sono: `created_at`, `id` e `text`.

## 🚀 Sfida

C'è un file `TwitterData.json` che puoi caricare nel database SampleDB. Si consiglia di aggiungerlo a un contenitore separato. Questo può essere fatto:

1. Cliccando sul pulsante nuovo contenitore in alto a destra
1. Selezionando il database esistente (SampleDB) e creando un id per il contenitore
1. Impostando la chiave di partizione su `/id`
1. Cliccando su OK (puoi ignorare il resto delle informazioni in questa vista poiché si tratta di un piccolo dataset che gira localmente sulla tua macchina)
1. Apri il tuo nuovo contenitore e carica il file Twitter Data con il pulsante `Upload Item`

Prova a eseguire alcune query SELECT per trovare i documenti che contengono Microsoft nel campo text. Suggerimento: prova a utilizzare la [parola chiave LIKE](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character).

## [Quiz Post-Lezione](https://ff-quizzes.netlify.app/en/ds/quiz/11)

## Revisione e studio autonomo

- Ci sono alcune formattazioni e funzionalità aggiuntive in questo foglio di calcolo che questa lezione non copre. Microsoft ha una [grande libreria di documentazione e video](https://support.microsoft.com/excel) su Excel se sei interessato a imparare di più.

- Questa documentazione architettonica dettaglia le caratteristiche dei diversi tipi di dati non relazionali: [Dati non relazionali e NoSQL](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data)

- Cosmos DB è un database non relazionale basato su cloud che può anche archiviare i diversi tipi di NoSQL menzionati in questa lezione. Scopri di più su questi tipi in questo [Modulo Microsoft Learn su Cosmos DB](https://docs.microsoft.com/en-us/learn/paths/work-with-nosql-data-in-azure-cosmos-db/)

## Compito

[Soda Profits](assignment.md)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.