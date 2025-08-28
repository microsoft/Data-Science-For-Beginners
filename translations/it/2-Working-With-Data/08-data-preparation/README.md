<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3ade580a06b5f04d57cc83a768a8fb77",
  "translation_date": "2025-08-28T10:53:12+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "it"
}
-->
# Lavorare con i Dati: Preparazione dei Dati

|![ Sketchnote di [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Preparazione dei Dati - _Sketchnote di [@nitya](https://twitter.com/nitya)_ |

## [Quiz Pre-Lezione](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

A seconda della sua origine, i dati grezzi possono contenere alcune incongruenze che creeranno difficoltà nell'analisi e nella modellazione. In altre parole, questi dati possono essere classificati come "sporchi" e necessitano di essere ripuliti. Questa lezione si concentra su tecniche per pulire e trasformare i dati per gestire problemi di dati mancanti, inaccurati o incompleti. Gli argomenti trattati in questa lezione utilizzeranno Python e la libreria Pandas e saranno [dimostrati nel notebook](notebook.ipynb) all'interno di questa directory.

## L'importanza di pulire i dati

- **Facilità d'uso e riutilizzo**: Quando i dati sono organizzati e normalizzati correttamente, è più facile cercarli, utilizzarli e condividerli con altri.

- **Coerenza**: La scienza dei dati spesso richiede di lavorare con più di un dataset, dove i dataset provenienti da fonti diverse devono essere uniti. Garantire che ogni singolo dataset abbia una standardizzazione comune assicurerà che i dati siano ancora utili quando vengono uniti in un unico dataset.

- **Accuratezza del modello**: I dati che sono stati puliti migliorano l'accuratezza dei modelli che ne dipendono.

## Obiettivi e strategie comuni di pulizia

- **Esplorare un dataset**: L'esplorazione dei dati, che viene trattata in una [lezione successiva](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), può aiutarti a scoprire dati che necessitano di essere ripuliti. Osservare visivamente i valori all'interno di un dataset può creare aspettative su come sarà il resto o fornire un'idea dei problemi che possono essere risolti. L'esplorazione può includere interrogazioni di base, visualizzazioni e campionamenti.

- **Formattazione**: A seconda della fonte, i dati possono presentare incongruenze nel modo in cui vengono presentati. Questo può causare problemi nella ricerca e nella rappresentazione dei valori, dove sono visibili nel dataset ma non sono rappresentati correttamente nelle visualizzazioni o nei risultati delle query. I problemi comuni di formattazione includono la gestione degli spazi bianchi, delle date e dei tipi di dati. Risolvere i problemi di formattazione è tipicamente compito di chi utilizza i dati. Ad esempio, gli standard su come vengono presentate le date e i numeri possono variare da paese a paese.

- **Duplicazioni**: I dati che si presentano più di una volta possono produrre risultati inaccurati e di solito dovrebbero essere rimossi. Questo può accadere frequentemente quando si uniscono due o più dataset. Tuttavia, ci sono casi in cui le duplicazioni nei dataset uniti contengono informazioni aggiuntive che potrebbero dover essere preservate.

- **Dati mancanti**: I dati mancanti possono causare risultati inaccurati, deboli o distorti. A volte possono essere risolti con un "ricaricamento" dei dati, riempiendo i valori mancanti con calcoli e codice come Python, o semplicemente rimuovendo il valore e i dati corrispondenti. Ci sono numerose ragioni per cui i dati possono mancare, e le azioni intraprese per risolvere questi valori mancanti possono dipendere da come e perché sono mancati.

## Esplorare le informazioni di un DataFrame
> **Obiettivo di apprendimento:** Alla fine di questa sottosezione, dovresti sentirti a tuo agio nel trovare informazioni generali sui dati memorizzati nei DataFrame di pandas.

Una volta caricati i dati in pandas, è probabile che siano in un DataFrame (consulta la [lezione precedente](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) per una panoramica dettagliata). Tuttavia, se il dataset nel tuo DataFrame ha 60.000 righe e 400 colonne, come inizi a farti un'idea di cosa stai lavorando? Fortunatamente, [pandas](https://pandas.pydata.org/) fornisce strumenti pratici per esaminare rapidamente le informazioni generali su un DataFrame, oltre alle prime e ultime righe.

Per esplorare questa funzionalità, importeremo la libreria Python scikit-learn e utilizzeremo un dataset iconico: il **dataset Iris**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |lunghezza sepalo (cm)|larghezza sepalo (cm)|lunghezza petalo (cm)|larghezza petalo (cm)|
|----------------------------------------|---------------------|---------------------|---------------------|---------------------|
|0                                       |5.1                  |3.5                  |1.4                  |0.2                  |
|1                                       |4.9                  |3.0                  |1.4                  |0.2                  |
|2                                       |4.7                  |3.2                  |1.3                  |0.2                  |
|3                                       |4.6                  |3.1                  |1.5                  |0.2                  |
|4                                       |5.0                  |3.6                  |1.4                  |0.2                  |

- **DataFrame.info**: Per iniziare, il metodo `info()` viene utilizzato per stampare un riepilogo del contenuto presente in un `DataFrame`. Diamo un'occhiata a questo dataset per vedere cosa abbiamo:
```python
iris_df.info()
```
```
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
dtypes: float64(4)
memory usage: 4.8 KB
```
Da questo, sappiamo che il dataset *Iris* ha 150 voci in quattro colonne senza valori nulli. Tutti i dati sono memorizzati come numeri in virgola mobile a 64 bit.

- **DataFrame.head()**: Successivamente, per controllare il contenuto effettivo del `DataFrame`, utilizziamo il metodo `head()`. Vediamo come appaiono le prime righe del nostro `iris_df`:
```python
iris_df.head()
```
```
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
```
- **DataFrame.tail()**: Al contrario, per controllare le ultime righe del `DataFrame`, utilizziamo il metodo `tail()`:
```python
iris_df.tail()
```
```
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
145                6.7               3.0                5.2               2.3
146                6.3               2.5                5.0               1.9
147                6.5               3.0                5.2               2.0
148                6.2               3.4                5.4               2.3
149                5.9               3.0                5.1               1.8
```
> **Conclusione:** Anche solo osservando i metadati sulle informazioni in un DataFrame o i primi e ultimi valori in esso, puoi ottenere un'idea immediata delle dimensioni, della forma e del contenuto dei dati con cui stai lavorando.

## Gestire i Dati Mancanti
> **Obiettivo di apprendimento:** Alla fine di questa sottosezione, dovresti sapere come sostituire o rimuovere valori nulli dai DataFrame.

La maggior parte delle volte, i dataset che vuoi utilizzare (o devi utilizzare) contengono valori mancanti. Il modo in cui i dati mancanti vengono gestiti comporta compromessi sottili che possono influenzare la tua analisi finale e i risultati nel mondo reale.

Pandas gestisce i valori mancanti in due modi. Il primo, che hai già visto in sezioni precedenti, è `NaN`, o Not a Number. Questo è in realtà un valore speciale che fa parte della specifica IEEE per i numeri in virgola mobile ed è utilizzato solo per indicare valori mancanti in virgola mobile.

Per i valori mancanti diversi dai numeri in virgola mobile, pandas utilizza l'oggetto Python `None`. Anche se può sembrare confuso incontrare due tipi diversi di valori che indicano essenzialmente la stessa cosa, ci sono valide ragioni programmatiche per questa scelta di design e, nella pratica, questa soluzione consente a pandas di offrire un buon compromesso per la stragrande maggioranza dei casi. Tuttavia, sia `None` che `NaN` presentano restrizioni di cui devi essere consapevole riguardo al loro utilizzo.

Scopri di più su `NaN` e `None` dal [notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Rilevare valori nulli**: In `pandas`, i metodi `isnull()` e `notnull()` sono i tuoi strumenti principali per rilevare dati nulli. Entrambi restituiscono maschere booleane sui tuoi dati. Utilizzeremo `numpy` per i valori `NaN`:
```python
import numpy as np

example1 = pd.Series([0, np.nan, '', None])
example1.isnull()
```
```
0    False
1     True
2    False
3     True
dtype: bool
```
Osserva attentamente l'output. Qualcosa ti sorprende? Anche se `0` è un valore nullo aritmetico, è comunque un intero valido e pandas lo tratta come tale. `''` è un po' più sottile. Anche se lo abbiamo usato nella Sezione 1 per rappresentare un valore stringa vuoto, è comunque un oggetto stringa e non una rappresentazione di nullo per pandas.

Ora, invertiamo la situazione e utilizziamo questi metodi in un modo più simile a come li userai nella pratica. Puoi utilizzare le maschere booleane direttamente come indice di una ``Series`` o di un ``DataFrame``, il che può essere utile quando cerchi di lavorare con valori nulli (o presenti) isolati.

> **Conclusione**: I metodi `isnull()` e `notnull()` producono risultati simili quando li utilizzi nei `DataFrame`: mostrano i risultati e l'indice di quei risultati, il che ti aiuterà enormemente mentre lavori con i tuoi dati.

- **Eliminare valori nulli**: Oltre a identificare i valori mancanti, pandas fornisce un mezzo pratico per rimuovere i valori nulli da `Series` e `DataFrame`. (Particolarmente nei dataset di grandi dimensioni, è spesso più consigliabile semplicemente rimuovere i valori mancanti [NA] dalla tua analisi piuttosto che gestirli in altri modi.) Per vedere questo in azione, torniamo a `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Nota che questo dovrebbe assomigliare al tuo output da `example3[example3.notnull()]`. La differenza qui è che, invece di indicizzare solo sui valori mascherati, `dropna` ha rimosso quei valori mancanti dalla `Series` `example1`.

Poiché i `DataFrame` hanno due dimensioni, offrono più opzioni per eliminare i dati.

```python
example2 = pd.DataFrame([[1,      np.nan, 7], 
                         [2,      5,      8], 
                         [np.nan, 6,      9]])
example2
```
|      | 0 | 1 | 2 |
|------|---|---|---|
|0     |1.0|NaN|7  |
|1     |2.0|5.0|8  |
|2     |NaN|6.0|9  |

(Hai notato che pandas ha convertito due delle colonne in float per accogliere i `NaN`?)

Non puoi eliminare un singolo valore da un `DataFrame`, quindi devi eliminare intere righe o colonne. A seconda di ciò che stai facendo, potresti voler fare una cosa o l'altra, e quindi pandas ti offre opzioni per entrambe. Poiché nella scienza dei dati le colonne generalmente rappresentano variabili e le righe rappresentano osservazioni, è più probabile che tu elimini righe di dati; l'impostazione predefinita per `dropna()` è eliminare tutte le righe che contengono valori nulli:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Se necessario, puoi eliminare i valori NA dalle colonne. Usa `axis=1` per farlo:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Nota che questo può eliminare molti dati che potresti voler mantenere, in particolare nei dataset più piccoli. E se volessi eliminare solo righe o colonne che contengono diversi o addirittura tutti i valori nulli? Puoi specificare queste impostazioni in `dropna` con i parametri `how` e `thresh`.

Per impostazione predefinita, `how='any'` (se vuoi verificare di persona o vedere quali altri parametri ha il metodo, esegui `example4.dropna?` in una cella di codice). Potresti specificare alternativamente `how='all'` per eliminare solo righe o colonne che contengono tutti i valori nulli. Espandiamo il nostro esempio di `DataFrame` per vedere questo in azione.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

Il parametro `thresh` ti offre un controllo più preciso: imposti il numero di valori *non nulli* che una riga o una colonna deve avere per essere mantenuta:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Qui, la prima e l'ultima riga sono state eliminate, perché contengono solo due valori non nulli.

- **Riempire valori nulli**: A seconda del tuo dataset, a volte può avere più senso riempire i valori nulli con valori validi piuttosto che eliminarli. Potresti usare `isnull` per farlo sul posto, ma questo può essere laborioso, in particolare se hai molti valori da riempire. Poiché questo è un compito così comune nella scienza dei dati, pandas fornisce `fillna`, che restituisce una copia della `Series` o del `DataFrame` con i valori mancanti sostituiti con uno a tua scelta. Creiamo un'altra `Series` di esempio per vedere come funziona nella pratica.
```python
example3 = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
example3
```
```
a    1.0
b    NaN
c    2.0
d    NaN
e    3.0
dtype: float64
```
Puoi riempire tutte le voci nulle con un singolo valore, come `0`:
```python
example3.fillna(0)
```
```
a    1.0
b    0.0
c    2.0
d    0.0
e    3.0
dtype: float64
```
Puoi **riempire in avanti** i valori nulli, utilizzando l'ultimo valore valido per riempire un nullo:
```python
example3.fillna(method='ffill')
```
```
a    1.0
b    1.0
c    2.0
d    2.0
e    3.0
dtype: float64
```
Puoi anche **riempire all'indietro** per propagare il prossimo valore valido all'indietro per riempire un nullo:
```python
example3.fillna(method='bfill')
```
```
a    1.0
b    2.0
c    2.0
d    3.0
e    3.0
dtype: float64
```
Come puoi immaginare, questo funziona allo stesso modo con i `DataFrame`, ma puoi anche specificare un `axis` lungo il quale riempire i valori nulli. Riprendendo l'`example2` utilizzato in precedenza:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Nota che quando un valore precedente non è disponibile per il riempimento in avanti, il valore nullo rimane.
> **Punto chiave:** Esistono diversi modi per gestire i valori mancanti nei tuoi dataset. La strategia specifica che utilizzi (rimuoverli, sostituirli o anche il modo in cui li sostituisci) dovrebbe essere dettata dalle caratteristiche di quei dati. Acquisirai una maggiore consapevolezza su come affrontare i valori mancanti man mano che gestisci e interagisci con i dataset.

## Rimozione di dati duplicati

> **Obiettivo di apprendimento:** Alla fine di questa sottosezione, dovresti sentirti a tuo agio nell'identificare e rimuovere valori duplicati dai DataFrame.

Oltre ai dati mancanti, spesso incontrerai dati duplicati nei dataset del mondo reale. Fortunatamente, `pandas` offre un modo semplice per rilevare e rimuovere le voci duplicate.

- **Identificazione dei duplicati: `duplicated`**: Puoi facilmente individuare i valori duplicati utilizzando il metodo `duplicated` di pandas, che restituisce una maschera booleana indicando se una voce in un `DataFrame` è un duplicato di una precedente. Creiamo un altro esempio di `DataFrame` per vedere questo in azione.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |letters|numbers|
|------|-------|-------|
|0     |A      |1      |
|1     |B      |2      |
|2     |A      |1      |
|3     |B      |3      |
|4     |B      |3      |

```python
example4.duplicated()
```
```
0    False
1    False
2     True
3    False
4     True
dtype: bool
```
- **Eliminazione dei duplicati: `drop_duplicates`:** restituisce semplicemente una copia dei dati per i quali tutti i valori `duplicated` sono `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Sia `duplicated` che `drop_duplicates` considerano di default tutte le colonne, ma puoi specificare che esaminino solo un sottoinsieme di colonne nel tuo `DataFrame`:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Punto chiave:** Rimuovere i dati duplicati è una parte essenziale di quasi ogni progetto di data science. I dati duplicati possono alterare i risultati delle tue analisi e fornire risultati inaccurati!


## 🚀 Sfida

Tutti i materiali discussi sono forniti come un [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Inoltre, ci sono esercizi presenti alla fine di ogni sezione, provali!

## [Quiz post-lezione](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/15)



## Revisione e studio autonomo

Esistono molti modi per scoprire e affrontare la preparazione dei tuoi dati per l'analisi e la modellazione, e la pulizia dei dati è un passaggio importante che richiede un'esperienza "pratica". Prova queste sfide su Kaggle per esplorare tecniche che questa lezione non ha trattato.

- [Data Cleaning Challenge: Parsing Dates](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Data Cleaning Challenge: Scale and Normalize Data](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Compito

[Valutazione dei dati da un modulo](assignment.md)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.