<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80d80300002ef4e77cc7631d5904bd6e",
  "translation_date": "2025-10-25T18:50:05+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "it"
}
-->
# Lavorare con i dati: Database relazionali

|![ Sketchnote di [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Lavorare con i dati: Database relazionali - _Sketchnote di [@nitya](https://twitter.com/nitya)_ |

Probabilmente hai già utilizzato un foglio di calcolo in passato per memorizzare informazioni. Avevi un insieme di righe e colonne, dove le righe contenevano le informazioni (o dati) e le colonne descrivevano le informazioni (a volte chiamate metadati). Un database relazionale si basa su questo principio fondamentale di colonne e righe in tabelle, permettendoti di avere informazioni distribuite su più tabelle. Questo ti consente di lavorare con dati più complessi, evitare duplicazioni e avere flessibilità nel modo in cui esplori i dati. Esploriamo i concetti di un database relazionale.

## [Quiz pre-lezione](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Tutto inizia con le tabelle

Un database relazionale ha come nucleo centrale le tabelle. Proprio come con il foglio di calcolo, una tabella è una raccolta di colonne e righe. La riga contiene i dati o le informazioni con cui vogliamo lavorare, come il nome di una città o la quantità di pioggia. Le colonne descrivono i dati che contengono.

Iniziamo la nostra esplorazione creando una tabella per memorizzare informazioni sulle città. Potremmo iniziare con il loro nome e il paese. Potresti memorizzare queste informazioni in una tabella come segue:

| Città    | Paese         |
| -------- | ------------- |
| Tokyo    | Giappone      |
| Atlanta  | Stati Uniti   |
| Auckland | Nuova Zelanda |

Nota che i nomi delle colonne **città**, **paese** e **popolazione** descrivono i dati memorizzati, e ogni riga contiene informazioni su una città.

## I limiti di un approccio con una sola tabella

Probabilmente la tabella sopra ti sembra abbastanza familiare. Iniziamo ad aggiungere alcuni dati aggiuntivi al nostro nascente database: la pioggia annuale (in millimetri). Ci concentreremo sugli anni 2018, 2019 e 2020. Se dovessimo aggiungerla per Tokyo, potrebbe apparire così:

| Città  | Paese   | Anno | Quantità |
| ------ | ------- | ---- | -------- |
| Tokyo  | Giappone| 2020 | 1690     |
| Tokyo  | Giappone| 2019 | 1874     |
| Tokyo  | Giappone| 2018 | 1445     |

Cosa noti nella nostra tabella? Potresti notare che stiamo duplicando il nome e il paese della città più e più volte. Questo potrebbe occupare molto spazio di archiviazione ed è in gran parte inutile avere più copie. Dopotutto, Tokyo ha solo un nome che ci interessa.

OK, proviamo qualcos'altro. Aggiungiamo nuove colonne per ogni anno:

| Città    | Paese         | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Giappone      | 1445 | 1874 | 1690 |
| Atlanta  | Stati Uniti   | 1779 | 1111 | 1683 |
| Auckland | Nuova Zelanda | 1386 | 942  | 1176 |

Anche se questo evita la duplicazione delle righe, introduce un paio di altre sfide. Dovremmo modificare la struttura della nostra tabella ogni volta che c'è un nuovo anno. Inoltre, man mano che i nostri dati crescono, avere gli anni come colonne renderà più complicato recuperare e calcolare i valori.

Ecco perché abbiamo bisogno di più tabelle e relazioni. Dividendo i nostri dati possiamo evitare duplicazioni e avere maggiore flessibilità nel modo in cui lavoriamo con i dati.

## I concetti di relazioni

Torniamo ai nostri dati e determiniamo come vogliamo suddividerli. Sappiamo di voler memorizzare il nome e il paese delle nostre città, quindi probabilmente questo funzionerà meglio in una tabella.

| Città    | Paese         |
| -------- | ------------- |
| Tokyo    | Giappone      |
| Atlanta  | Stati Uniti   |
| Auckland | Nuova Zelanda |

Ma prima di creare la prossima tabella, dobbiamo capire come fare riferimento a ciascuna città. Abbiamo bisogno di una forma di identificatore, ID o (in termini tecnici di database) una chiave primaria. Una chiave primaria è un valore utilizzato per identificare una riga specifica in una tabella. Anche se potrebbe essere basata su un valore stesso (potremmo usare il nome della città, ad esempio), dovrebbe quasi sempre essere un numero o un altro identificatore. Non vogliamo che l'ID cambi mai, poiché romperebbe la relazione. Nella maggior parte dei casi, la chiave primaria o l'ID sarà un numero generato automaticamente.

> ✅ La chiave primaria è spesso abbreviata come PK

### città

| city_id | Città    | Paese         |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Giappone      |
| 2       | Atlanta  | Stati Uniti   |
| 3       | Auckland | Nuova Zelanda |

> ✅ Noterai che usiamo i termini "id" e "chiave primaria" in modo intercambiabile durante questa lezione. I concetti qui si applicano ai DataFrame, che esplorerai più avanti. I DataFrame non usano la terminologia di "chiave primaria", tuttavia noterai che si comportano in modo molto simile.

Con la nostra tabella delle città creata, memorizziamo la pioggia. Piuttosto che duplicare tutte le informazioni sulla città, possiamo usare l'ID. Dovremmo anche assicurarci che la tabella appena creata abbia una colonna *id*, poiché tutte le tabelle dovrebbero avere un ID o una chiave primaria.

### pioggia

| rainfall_id | city_id | Anno | Quantità |
| ----------- | ------- | ---- | -------- |
| 1           | 1       | 2018 | 1445     |
| 2           | 1       | 2019 | 1874     |
| 3           | 1       | 2020 | 1690     |
| 4           | 2       | 2018 | 1779     |
| 5           | 2       | 2019 | 1111     |
| 6           | 2       | 2020 | 1683     |
| 7           | 3       | 2018 | 1386     |
| 8           | 3       | 2019 | 942      |
| 9           | 3       | 2020 | 1176     |

Nota la colonna **city_id** all'interno della nuova tabella **pioggia**. Questa colonna contiene valori che fanno riferimento agli ID nella tabella **città**. In termini tecnici di dati relazionali, questo è chiamato **chiave esterna**; è una chiave primaria di un'altra tabella. Puoi semplicemente pensarlo come un riferimento o un puntatore. **city_id** 1 fa riferimento a Tokyo.

> [!NOTE] 
> La chiave esterna è spesso abbreviata come FK

## Recuperare i dati

Con i nostri dati separati in due tabelle, potresti chiederti come recuperarli. Se stiamo usando un database relazionale come MySQL, SQL Server o Oracle, possiamo usare un linguaggio chiamato Structured Query Language o SQL. SQL (a volte pronunciato sequel) è un linguaggio standard utilizzato per recuperare e modificare i dati in un database relazionale.

Per recuperare i dati si usa il comando `SELECT`. Alla base, **selezioni** le colonne che vuoi vedere **da** la tabella in cui sono contenute. Se volessi visualizzare solo i nomi delle città, potresti usare il seguente:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` è dove elenchi le colonne, e `FROM` è dove elenchi le tabelle.

> [!NOTE] 
> La sintassi SQL non distingue tra maiuscole e minuscole, il che significa che `select` e `SELECT` sono la stessa cosa. Tuttavia, a seconda del tipo di database che stai utilizzando, le colonne e le tabelle potrebbero essere sensibili alle maiuscole. Di conseguenza, è una buona pratica trattare sempre tutto nella programmazione come se fosse sensibile alle maiuscole. Quando scrivi query SQL, la convenzione comune è di mettere le parole chiave in lettere maiuscole.

La query sopra visualizzerà tutte le città. Immaginiamo di voler visualizzare solo le città in Nuova Zelanda. Abbiamo bisogno di una sorta di filtro. La parola chiave SQL per questo è `WHERE`, o "dove qualcosa è vero".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Unire i dati

Finora abbiamo recuperato dati da una singola tabella. Ora vogliamo unire i dati provenienti sia da **città** che da **pioggia**. Questo viene fatto *unendo* le due tabelle. Creerai effettivamente un collegamento tra le due tabelle, abbinando i valori di una colonna di ciascuna tabella.

Nel nostro esempio, abbineremo la colonna **city_id** in **pioggia** con la colonna **city_id** in **città**. Questo abbinerà il valore della pioggia alla sua rispettiva città. Il tipo di unione che eseguiremo è ciò che viene chiamato un'unione *interna*, il che significa che se alcune righe non corrispondono a nulla dall'altra tabella, non verranno visualizzate. Nel nostro caso ogni città ha dati sulla pioggia, quindi tutto verrà visualizzato.

Recuperiamo la pioggia del 2019 per tutte le nostre città.

Lo faremo in passaggi. Il primo passo è unire i dati indicando le colonne per il collegamento - **city_id** come evidenziato prima.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Abbiamo evidenziato le due colonne che vogliamo, e il fatto che vogliamo unire le tabelle insieme tramite **city_id**. Ora possiamo aggiungere l'istruzione `WHERE` per filtrare solo l'anno 2019.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
WHERE rainfall.year = 2019

-- Output

-- city     | amount
-- -------- | ------
-- Tokyo    | 1874
-- Atlanta  | 1111
-- Auckland |  942
```

## Riepilogo

I database relazionali si basano sulla divisione delle informazioni tra più tabelle che vengono poi riunite per la visualizzazione e l'analisi. Questo fornisce un alto grado di flessibilità per eseguire calcoli e manipolare i dati. Hai visto i concetti fondamentali di un database relazionale e come eseguire un'unione tra due tabelle.

## 🚀 Sfida

Esistono numerosi database relazionali disponibili su Internet. Puoi esplorare i dati utilizzando le competenze che hai appreso sopra.

## Quiz post-lezione

## [Quiz post-lezione](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Revisione e studio autonomo

Ci sono diverse risorse disponibili su [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) per continuare la tua esplorazione dei concetti di SQL e database relazionali.

- [Descrivere i concetti di dati relazionali](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Introduzione alle query con Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL è una versione di SQL)
- [Contenuti SQL su Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Compito

[Titolo del compito](assignment.md)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.