<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-28T10:50:40+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "it"
}
-->
# Compito per l'elaborazione dei dati in Python

In questo compito, ti chiederemo di approfondire il codice che abbiamo iniziato a sviluppare nelle nostre sfide. Il compito è suddiviso in due parti:

## Modellazione della diffusione del COVID-19

 - [ ] Tracciare i grafici di *R* per 5-6 paesi diversi su un unico grafico per confronto, oppure utilizzando più grafici affiancati.
 - [ ] Analizzare come il numero di decessi e guarigioni si correla con il numero di casi infetti.
 - [ ] Scoprire quanto dura tipicamente una malattia correlando visivamente il tasso di infezione e il tasso di decessi, cercando eventuali anomalie. Potrebbe essere necessario osservare diversi paesi per scoprirlo.
 - [ ] Calcolare il tasso di mortalità e come cambia nel tempo. *Potresti voler considerare la durata della malattia in giorni per spostare una serie temporale prima di effettuare i calcoli.*

## Analisi degli articoli sul COVID-19

- [ ] Costruire una matrice di co-occorrenza di diversi farmaci e vedere quali farmaci vengono spesso menzionati insieme (ad esempio, citati in un unico abstract). Puoi modificare il codice per costruire la matrice di co-occorrenza per farmaci e diagnosi.
- [ ] Visualizzare questa matrice utilizzando una heatmap.
- [ ] Come obiettivo aggiuntivo, visualizzare la co-occorrenza dei farmaci utilizzando un [diagramma a corde](https://en.wikipedia.org/wiki/Chord_diagram). [Questa libreria](https://pypi.org/project/chord/) potrebbe aiutarti a disegnare un diagramma a corde.
- [ ] Come un altro obiettivo aggiuntivo, estrarre i dosaggi di diversi farmaci (come **400mg** in *assumere 400mg di clorochina al giorno*) utilizzando espressioni regolari, e costruire un dataframe che mostri i diversi dosaggi per i vari farmaci. **Nota**: considera i valori numerici che si trovano in prossimità testuale del nome del farmaco.

## Griglia di valutazione

Esemplare | Adeguato | Da migliorare
--- | --- | -- |
Tutti i compiti sono completati, illustrati graficamente e spiegati, inclusi almeno uno dei due obiettivi aggiuntivi | Più di 5 compiti sono completati, nessun obiettivo aggiuntivo è stato tentato, oppure i risultati non sono chiari | Meno di 5 (ma più di 3) compiti sono completati, le visualizzazioni non aiutano a dimostrare il punto

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.