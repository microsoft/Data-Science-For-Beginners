# Definizione dei Dati

|![ Sketchnote di [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definizione dei Dati - _Sketchnote di [@nitya](https://twitter.com/nitya)_ |

I dati sono fatti, informazioni, osservazioni e misurazioni utilizzati per fare scoperte e supportare decisioni informate. Un punto dati è un'unità singola di dati all'interno di un dataset, che è una raccolta di punti dati. I dataset possono avere diversi formati e strutture, e solitamente dipenderanno dalla loro fonte, ovvero da dove provengono i dati. Per esempio, i guadagni mensili di un'azienda potrebbero essere in un foglio di calcolo mentre i dati sul battito cardiaco orario di uno smartwatch potrebbero essere in formato [JSON](https://stackoverflow.com/a/383699). È comune per i data scientist lavorare con diversi tipi di dati all'interno di un dataset. 

Questa lezione si concentra sull'identificare e classificare i dati in base alle loro caratteristiche e alle loro fonti.

## [Quiz Pre-Lezione](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Come vengono Descritti i Dati

### Dati Grezzi
I dati grezzi sono dati che provengono dalla loro fonte nel loro stato iniziale e non sono stati analizzati o organizzati. Per dare senso a quello che accade in un dataset, è necessario organizzarli in un formato comprensibile sia dagli esseri umani che dalla tecnologia che potrebbe essere usata per analizzarli ulteriormente. La struttura di un dataset descrive come è organizzato e può essere classificata come strutturata, non strutturata e semi-strutturata. Questi tipi di struttura variano a seconda della fonte ma alla fine rientrano in queste tre categorie. 

### Dati Quantitativi
I dati quantitativi sono osservazioni numeriche all'interno di un dataset e generalmente possono essere analizzati, misurati e usati matematicamente. Alcuni esempi di dati quantitativi sono: la popolazione di un paese, l'altezza di una persona o i guadagni trimestrali di un'azienda. Con un'analisi aggiuntiva, i dati quantitativi potrebbero essere usati per scoprire tendenze stagionali dell'Indice di Qualità dell'Aria (AQI) o stimare la probabilità del traffico nelle ore di punta in un normale giorno lavorativo.

### Dati Qualitativi
I dati qualitativi, noti anche come dati categorici, sono dati che non possono essere misurati oggettivamente come le osservazioni dei dati quantitativi. Sono generalmente varie forme di dati soggettivi che catturano la qualità di qualcosa, come un prodotto o un processo. A volte i dati qualitativi sono numerici e tipicamente non usati matematicamente, come numeri di telefono o timestamp. Alcuni esempi di dati qualitativi sono: commenti video, marca e modello di un’auto o il colore preferito dei tuoi amici più stretti. I dati qualitativi potrebbero essere utilizzati per capire quali prodotti piacciono di più ai consumatori o per identificare parole chiave popolari nei curriculum per l'applicazione a un lavoro.

### Dati Strutturati
I dati strutturati sono dati organizzati in righe e colonne, dove ogni riga ha lo stesso set di colonne. Le colonne rappresentano un valore di un tipo particolare e sono identificate da un nome che descrive cosa rappresenta il valore, mentre le righe contengono i valori effettivi. Le colonne spesso hanno un insieme specifico di regole o restrizioni sui valori, per assicurare che rappresentino accuratamente la colonna. Per esempio, immagina un foglio di calcolo dei clienti in cui ogni riga deve avere un numero di telefono e i numeri di telefono non contengono mai caratteri alfabetici. Potrebbero esserci regole applicate alla colonna del numero di telefono per garantire che non sia mai vuota e che contenga solo numeri. 

Un vantaggio dei dati strutturati è che possono essere organizzati in modo tale da poter essere correlati ad altri dati strutturati. Tuttavia, poiché i dati sono progettati per essere organizzati in un modo specifico, modificare la loro struttura complessiva può richiedere molto sforzo. Per esempio, aggiungere una colonna di email al foglio clienti che non può essere vuota significa che devi capire come aggiungere questi valori alle righe esistenti dei clienti nel dataset. 

Esempi di dati strutturati: fogli di calcolo, database relazionali, numeri di telefono, estratti conto bancari

### Dati Non Strutturati
I dati non strutturati tipicamente non possono essere categorizzati in righe o colonne e non hanno un formato o un insieme di regole da seguire. Poiché i dati non strutturati hanno meno restrizioni sulla loro struttura, è più facile aggiungere nuove informazioni rispetto a un dataset strutturato. Se un sensore che cattura dati sulla pressione barometrica ogni 2 minuti viene aggiornato per misurare e registrare anche la temperatura, non è necessario modificare i dati esistenti se sono non strutturati. Tuttavia, ciò può rendere più lunga l'analisi o l'indagine su questo tipo di dati. Per esempio, uno scienziato che vuole trovare la temperatura media del mese precedente dai dati del sensore ma scopre che il sensore ha registrato una "e" in alcuni valori per indicare che era rotto invece di un numero tipico, il che significa che i dati sono incompleti.

Esempi di dati non strutturati: file di testo, messaggi di testo, file video

### Semi-strutturati
I dati semi-strutturati hanno caratteristiche che li rendono una combinazione di dati strutturati e non strutturati. Tipicamente non seguono un formato di righe e colonne ma sono organizzati in modo considerato strutturato e possono seguire un formato fisso o un insieme di regole. La struttura varia tra le fonti, da una gerarchia ben definita a qualcosa di più flessibile che permette un’integrazione facile di nuove informazioni. I metadati sono indicatori che aiutano a decidere come i dati sono organizzati e memorizzati e possono avere vari nomi, basati sul tipo di dati. Alcuni nomi comuni per i metadati sono tag, elementi, entità e attributi. Per esempio, un tipico messaggio email ha un soggetto, un corpo e un set di destinatari e può essere organizzato in base a chi o quando è stato inviato. 

Esempi di dati semi-strutturati: HTML, file CSV, JavaScript Object Notation (JSON)

## Fonti di Dati 

Una fonte di dati è la posizione iniziale in cui i dati sono stati generati o dove "risiedono" e varia in base a come e quando sono stati raccolti. I dati generati dagli utenti sono noti come dati primari, mentre i dati secondari provengono da una fonte che ha raccolto dati per uso generale. Per esempio, un gruppo di scienziati che raccoglie osservazioni in una foresta pluviale sarebbe considerato primaria e se decidono di condividerlo con altri scienziati sarebbe considerata secondaria per chi la usa. 

I database sono una fonte comune e si basano su un sistema di gestione del database per ospitare e mantenere i dati, dove gli utenti usano comandi chiamati query per esplorare i dati. I file come fonti di dati possono essere file audio, immagine e video così come fogli di calcolo come Excel. Le fonti internet sono un luogo comune per ospitare dati, dove possono essere trovati database e file. Le Application Programming Interfaces, note anche come API, permettono ai programmatori di creare modi per condividere dati con utenti esterni attraverso internet, mentre il processo di web scraping estrae dati da una pagina web. Le [lezioni in Working with Data](../../../../../../../../../2-Working-With-Data) si concentrano su come usare varie fonti di dati. 

## Conclusione

In questa lezione abbiamo imparato:

- Che cosa sono i dati
- Come vengono descritti i dati
- Come i dati sono classificati e categorizzati
- Dove si possono trovare i dati

## 🚀 Sfida

Kaggle è un'ottima fonte di dataset aperti. Usa il [dataset search tool](https://www.kaggle.com/datasets) per trovare alcuni dataset interessanti e classifica 3-5 dataset con questi criteri:

- I dati sono quantitativi o qualitativi?
- I dati sono strutturati, non strutturati o semi-strutturati?

## [Quiz Post-Lezione](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Revisione & Studio Autonomo

- Questa unità Microsoft Learn, intitolata [Identificare i formati di dati](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text) offre una dettagliata suddivisione di dati strutturati, semi-strutturati e non strutturati.

## Compito

[Classificare i Dataset](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->