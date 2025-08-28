<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "356d12cffc3125db133a2d27b827a745",
  "translation_date": "2025-08-28T11:25:06+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "it"
}
-->
# Definizione dei Dati

|![ Sketchnote di [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definizione dei Dati - _Sketchnote di [@nitya](https://twitter.com/nitya)_ |

I dati sono fatti, informazioni, osservazioni e misurazioni utilizzati per fare scoperte e supportare decisioni informate. Un punto dati è una singola unità di dati all'interno di un dataset, che è una raccolta di punti dati. I dataset possono avere formati e strutture diversi e di solito dipendono dalla loro origine, ovvero da dove provengono i dati. Ad esempio, i guadagni mensili di un'azienda potrebbero essere in un foglio di calcolo, mentre i dati sulla frequenza cardiaca oraria di uno smartwatch potrebbero essere in formato [JSON](https://stackoverflow.com/a/383699). È comune per i data scientist lavorare con diversi tipi di dati all'interno di un dataset.

Questa lezione si concentra sull'identificazione e la classificazione dei dati in base alle loro caratteristiche e alle loro fonti.

## [Quiz Pre-Lezione](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)

## Come vengono descritti i dati

### Dati grezzi
I dati grezzi sono dati che provengono dalla loro fonte nel loro stato iniziale e non sono stati analizzati o organizzati. Per comprendere cosa sta accadendo in un dataset, è necessario organizzarli in un formato comprensibile sia per gli esseri umani che per la tecnologia che potrebbe essere utilizzata per analizzarli ulteriormente. La struttura di un dataset descrive come è organizzato e può essere classificata come strutturata, non strutturata e semi-strutturata. Questi tipi di struttura variano a seconda della fonte, ma rientrano comunque in queste tre categorie.

### Dati quantitativi
I dati quantitativi sono osservazioni numeriche all'interno di un dataset e possono essere generalmente analizzati, misurati e utilizzati matematicamente. Alcuni esempi di dati quantitativi sono: la popolazione di un paese, l'altezza di una persona o i guadagni trimestrali di un'azienda. Con un'analisi aggiuntiva, i dati quantitativi potrebbero essere utilizzati per scoprire tendenze stagionali dell'Indice di Qualità dell'Aria (AQI) o stimare la probabilità di traffico nelle ore di punta in una tipica giornata lavorativa.

### Dati qualitativi
I dati qualitativi, noti anche come dati categoriali, sono dati che non possono essere misurati oggettivamente come le osservazioni dei dati quantitativi. Generalmente si tratta di vari formati di dati soggettivi che catturano la qualità di qualcosa, come un prodotto o un processo. A volte, i dati qualitativi sono numerici ma non vengono tipicamente utilizzati matematicamente, come numeri di telefono o timestamp. Alcuni esempi di dati qualitativi sono: commenti video, marca e modello di un'auto o il colore preferito dei tuoi amici più stretti. I dati qualitativi potrebbero essere utilizzati per comprendere quali prodotti piacciono di più ai consumatori o per identificare parole chiave popolari nei curriculum delle domande di lavoro.

### Dati strutturati
I dati strutturati sono dati organizzati in righe e colonne, dove ogni riga avrà lo stesso set di colonne. Le colonne rappresentano un valore di un particolare tipo e saranno identificate con un nome che descrive cosa rappresenta il valore, mentre le righe contengono i valori effettivi. Le colonne spesso hanno un insieme specifico di regole o restrizioni sui valori, per garantire che i valori rappresentino accuratamente la colonna. Ad esempio, immagina un foglio di calcolo di clienti in cui ogni riga deve avere un numero di telefono e i numeri di telefono non contengono caratteri alfabetici. Potrebbero esserci regole applicate alla colonna del numero di telefono per assicurarsi che non sia mai vuota e contenga solo numeri.

Un vantaggio dei dati strutturati è che possono essere organizzati in modo tale da essere correlati ad altri dati strutturati. Tuttavia, poiché i dati sono progettati per essere organizzati in un modo specifico, apportare modifiche alla loro struttura generale può richiedere molto sforzo. Ad esempio, aggiungere una colonna email al foglio di calcolo dei clienti che non può essere vuota significa che dovrai capire come aggiungere questi valori alle righe esistenti di clienti nel dataset.

Esempi di dati strutturati: fogli di calcolo, database relazionali, numeri di telefono, estratti conto bancari.

### Dati non strutturati
I dati non strutturati generalmente non possono essere categorizzati in righe o colonne e non contengono un formato o un insieme di regole da seguire. Poiché i dati non strutturati hanno meno restrizioni sulla loro struttura, è più facile aggiungere nuove informazioni rispetto a un dataset strutturato. Se un sensore che cattura dati sulla pressione barometrica ogni 2 minuti ha ricevuto un aggiornamento che ora gli consente di misurare e registrare la temperatura, non è necessario modificare i dati esistenti se sono non strutturati. Tuttavia, ciò potrebbe rendere più lungo l'analisi o l'indagine su questo tipo di dati. Ad esempio, uno scienziato che vuole trovare la temperatura media del mese precedente dai dati del sensore, ma scopre che il sensore ha registrato una "e" in alcuni dei suoi dati per indicare che era rotto invece di un numero tipico, il che significa che i dati sono incompleti.

Esempi di dati non strutturati: file di testo, messaggi di testo, file video.

### Dati semi-strutturati
I dati semi-strutturati hanno caratteristiche che li rendono una combinazione di dati strutturati e non strutturati. Generalmente non si conformano a un formato di righe e colonne, ma sono organizzati in un modo considerato strutturato e possono seguire un formato fisso o un insieme di regole. La struttura varia tra le fonti, da una gerarchia ben definita a qualcosa di più flessibile che consente una facile integrazione di nuove informazioni. I metadati sono indicatori che aiutano a decidere come i dati sono organizzati e archiviati e avranno vari nomi, in base al tipo di dati. Alcuni nomi comuni per i metadati sono tag, elementi, entità e attributi. Ad esempio, un tipico messaggio email avrà un oggetto, un corpo e un insieme di destinatari e può essere organizzato in base a chi o quando è stato inviato.

Esempi di dati semi-strutturati: HTML, file CSV, JavaScript Object Notation (JSON).

## Fonti di dati

Una fonte di dati è il luogo iniziale in cui i dati sono stati generati o dove "vivono" e varia in base a come e quando sono stati raccolti. I dati generati dai suoi utenti sono noti come dati primari, mentre i dati secondari provengono da una fonte che ha raccolto dati per uso generale. Ad esempio, un gruppo di scienziati che raccoglie osservazioni in una foresta pluviale sarebbe considerato primario e, se decidono di condividerlo con altri scienziati, sarebbe considerato secondario per coloro che lo utilizzano.

I database sono una fonte comune e si basano su un sistema di gestione dei database per ospitare e mantenere i dati, dove gli utenti utilizzano comandi chiamati query per esplorare i dati. I file come fonti di dati possono essere file audio, immagini e video, così come fogli di calcolo come Excel. Le fonti internet sono un luogo comune per ospitare dati, dove si possono trovare sia database che file. Le interfacce di programmazione delle applicazioni, note anche come API, consentono ai programmatori di creare modi per condividere dati con utenti esterni tramite internet, mentre il processo di web scraping estrae dati da una pagina web. Le [lezioni su Lavorare con i Dati](../../../../../../../../../2-Working-With-Data) si concentrano su come utilizzare varie fonti di dati.

## Conclusione

In questa lezione abbiamo imparato:

- Cosa sono i dati
- Come vengono descritti i dati
- Come i dati vengono classificati e categorizzati
- Dove si possono trovare i dati

## 🚀 Sfida

Kaggle è un'ottima fonte di dataset aperti. Usa lo [strumento di ricerca dei dataset](https://www.kaggle.com/datasets) per trovare alcuni dataset interessanti e classifica 3-5 dataset con questi criteri:

- I dati sono quantitativi o qualitativi?
- I dati sono strutturati, non strutturati o semi-strutturati?

## [Quiz Post-Lezione](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/5)

## Revisione e Studio Autonomo

- Questa unità di Microsoft Learn, intitolata [Classifica i tuoi Dati](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data) offre una spiegazione dettagliata dei dati strutturati, semi-strutturati e non strutturati.

## Compito

[Classificazione dei Dataset](assignment.md)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.