<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:55:08+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "it"
}
-->
# Visualizzazione dei dati sugli aeroporti

Ti è stato fornito un [database](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) basato su [SQLite](https://sqlite.org/index.html) che contiene informazioni sugli aeroporti. Lo schema è mostrato di seguito. Utilizzerai l'[estensione SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) in [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) per visualizzare informazioni sugli aeroporti di diverse città.

## Istruzioni

Per iniziare con l'esercizio, dovrai eseguire alcuni passaggi. Sarà necessario installare alcuni strumenti e scaricare il database di esempio.

### Configura il tuo sistema

Puoi utilizzare Visual Studio Code e l'estensione SQLite per interagire con il database.

1. Vai su [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) e segui le istruzioni per installare Visual Studio Code
1. Installa l'[estensione SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) come indicato nella pagina del Marketplace

### Scarica e apri il database

Successivamente, scarica e apri il database.

1. Scarica il [file del database da GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) e salvalo in una directory
1. Apri Visual Studio Code
1. Apri il database nell'estensione SQLite selezionando **Ctl-Shift-P** (o **Cmd-Shift-P** su Mac) e digitando `SQLite: Open database`
1. Seleziona **Choose database from file** e apri il file **airports.db** che hai scaricato in precedenza
1. Dopo aver aperto il database (non vedrai un aggiornamento sullo schermo), crea una nuova finestra di query selezionando **Ctl-Shift-P** (o **Cmd-Shift-P** su Mac) e digitando `SQLite: New query`

Una volta aperta, la nuova finestra di query può essere utilizzata per eseguire istruzioni SQL sul database. Puoi utilizzare il comando **Ctl-Shift-Q** (o **Cmd-Shift-Q** su Mac) per eseguire query sul database.

> [!NOTE] 
> Per ulteriori informazioni sull'estensione SQLite, puoi consultare la [documentazione](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Schema del database

Lo schema di un database è il design e la struttura delle sue tabelle. Il database **airports** ha due tabelle, `cities`, che contiene un elenco di città nel Regno Unito e in Irlanda, e `airports`, che contiene l'elenco di tutti gli aeroporti. Poiché alcune città possono avere più aeroporti, sono state create due tabelle per memorizzare le informazioni. In questo esercizio utilizzerai le join per visualizzare informazioni relative a diverse città.

| Città            |
| ----------------- |
| id (PK, integer)  |
| city (text)       |
| country (text)    |

| Aeroporti                        |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK a id in **Cities**)  |

## Compito

Crea query per restituire le seguenti informazioni:

1. tutti i nomi delle città nella tabella `Cities`
1. tutte le città in Irlanda nella tabella `Cities`
1. tutti i nomi degli aeroporti con la loro città e paese
1. tutti gli aeroporti a Londra, Regno Unito

## Valutazione

| Esemplare | Adeguato | Da migliorare |
| --------- | -------- | ------------- |

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.