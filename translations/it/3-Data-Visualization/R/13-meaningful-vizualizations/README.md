<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4039f1c76548d144a0aee0bf28304ec",
  "translation_date": "2025-08-28T11:09:16+00:00",
  "source_file": "3-Data-Visualization/R/13-meaningful-vizualizations/README.md",
  "language_code": "it"
}
-->
# Creare Visualizzazioni Significative

|![ Sketchnote di [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Visualizzazioni Significative - _Sketchnote di [@nitya](https://twitter.com/nitya)_ |

> "Se torturi i dati abbastanza a lungo, confesseranno qualsiasi cosa" -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

Una delle competenze fondamentali di un data scientist è la capacità di creare una visualizzazione dei dati significativa che aiuti a rispondere alle domande che si potrebbero avere. Prima di visualizzare i dati, è necessario assicurarsi che siano stati puliti e preparati, come fatto nelle lezioni precedenti. Dopo di ciò, si può iniziare a decidere come presentare al meglio i dati.

In questa lezione, esaminerai:

1. Come scegliere il tipo di grafico giusto
2. Come evitare grafici ingannevoli
3. Come lavorare con i colori
4. Come stilizzare i grafici per migliorarne la leggibilità
5. Come creare soluzioni di grafici animati o in 3D
6. Come costruire una visualizzazione creativa

## [Quiz Pre-Lezione](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/24)

## Scegliere il tipo di grafico giusto

Nelle lezioni precedenti, hai sperimentato la creazione di vari tipi di visualizzazioni dei dati utilizzando Matplotlib e Seaborn. In generale, puoi selezionare il [tipo di grafico giusto](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) per la domanda che stai ponendo utilizzando questa tabella:

| Necessità:                 | Dovresti usare:                 |
| -------------------------- | ------------------------------- |
| Mostrare tendenze nel tempo | Linea                          |
| Confrontare categorie       | Barre, Torta                   |
| Confrontare totali          | Torta, Barre impilate          |
| Mostrare relazioni          | Dispersione, Linea, Facet, Linea doppia |
| Mostrare distribuzioni      | Dispersione, Istogramma, Box   |
| Mostrare proporzioni        | Torta, Donut, Waffle           |

> ✅ A seconda della composizione dei tuoi dati, potrebbe essere necessario convertirli da testo a numerico per supportare un determinato tipo di grafico.

## Evitare inganni

Anche se un data scientist sceglie con attenzione il grafico giusto per i dati, ci sono molti modi in cui i dati possono essere visualizzati per dimostrare un punto, spesso a scapito della veridicità dei dati stessi. Esistono molti esempi di grafici e infografiche ingannevoli!

[![How Charts Lie di Alberto Cairo](../../../../../translated_images/it/tornado.2880ffc7f135f82b5e5328624799010abefd1080ae4b7ecacbdc7d792f1d8849.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "How charts lie")

> 🎥 Clicca sull'immagine sopra per una conferenza sui grafici ingannevoli

Questo grafico inverte l'asse X per mostrare l'opposto della verità, basandosi sulla data:

![grafico errato 1](../../../../../translated_images/it/bad-chart-1.596bc93425a8ac301a28b8361f59a970276e7b961658ce849886aa1fed427341.png)

[Questo grafico](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) è ancora più ingannevole, poiché l'occhio è attirato verso destra per concludere che, nel tempo, i casi di COVID siano diminuiti nelle varie contee. In realtà, se si osservano attentamente le date, si scopre che sono state riorganizzate per creare questa falsa tendenza al ribasso.

![grafico errato 2](../../../../../translated_images/it/bad-chart-2.62edf4d2f30f4e519f5ef50c07ce686e27b0196a364febf9a4d98eecd21f9f60.jpg)

Questo esempio noto utilizza il colore E un asse Y invertito per ingannare: invece di concludere che le morti per armi da fuoco siano aumentate dopo l'approvazione di una legislazione favorevole alle armi, l'occhio è ingannato a pensare che sia vero il contrario:

![grafico errato 3](../../../../../translated_images/it/bad-chart-3.e201e2e915a230bc2cde289110604ec9abeb89be510bd82665bebc1228258972.jpg)

Questo grafico strano mostra come le proporzioni possano essere manipolate, con effetti esilaranti:

![grafico errato 4](../../../../../translated_images/it/bad-chart-4.8872b2b881ffa96c3e0db10eb6aed7793efae2cac382c53932794260f7bfff07.jpg)

Confrontare l'incomparabile è un altro trucco discutibile. Esiste un [sito web meraviglioso](https://tylervigen.com/spurious-correlations) dedicato alle 'correlazioni spurie' che mostra 'fatti' correlando cose come il tasso di divorzi nel Maine e il consumo di margarina. Un gruppo su Reddit raccoglie anche [usi discutibili](https://www.reddit.com/r/dataisugly/top/?t=all) dei dati.

È importante capire quanto facilmente l'occhio possa essere ingannato da grafici ingannevoli. Anche se l'intenzione del data scientist è buona, la scelta di un tipo di grafico sbagliato, come un grafico a torta con troppe categorie, può risultare ingannevole.

## Colore

Come visto nel grafico sulla 'violenza con armi da fuoco in Florida', il colore può aggiungere un ulteriore livello di significato ai grafici, specialmente quelli non progettati utilizzando librerie come ggplot2 e RColorBrewer, che offrono palette di colori validate. Se stai creando un grafico manualmente, studia un po' la [teoria del colore](https://colormatters.com/color-and-design/basic-color-theory).

> ✅ Quando progetti grafici, tieni presente che l'accessibilità è un aspetto importante della visualizzazione. Alcuni utenti potrebbero essere daltonici - il tuo grafico è leggibile per utenti con disabilità visive?

Fai attenzione quando scegli i colori per il tuo grafico, poiché il colore può trasmettere significati che potresti non intendere. Le 'signore rosa' nel grafico sull'altezza sopra trasmettono un significato distintamente 'femminile' che aggiunge alla stranezza del grafico stesso.

Sebbene il [significato del colore](https://colormatters.com/color-symbolism/the-meanings-of-colors) possa variare in diverse parti del mondo e tendere a cambiare in base alla tonalità, generalmente i significati dei colori includono:

| Colore | Significato         |
| ------ | ------------------- |
| rosso  | potere              |
| blu    | fiducia, lealtà     |
| giallo | felicità, cautela   |
| verde  | ecologia, fortuna, invidia |
| viola  | felicità            |
| arancione | vivacità          |

Se ti viene chiesto di creare un grafico con colori personalizzati, assicurati che i tuoi grafici siano accessibili e che il colore scelto coincida con il significato che vuoi trasmettere.

## Stilizzare i grafici per la leggibilità

I grafici non sono significativi se non sono leggibili! Prenditi un momento per considerare lo stile della larghezza e altezza del grafico per adattarlo bene ai tuoi dati. Se una variabile (come tutti i 50 stati) deve essere visualizzata, mostrala verticalmente sull'asse Y se possibile, per evitare un grafico con scorrimento orizzontale.

Etichetta gli assi, fornisci una legenda se necessario e offri tooltip per una migliore comprensione dei dati.

Se i tuoi dati sono testuali e verbosi sull'asse X, puoi angolare il testo per migliorarne la leggibilità. [plot3D](https://cran.r-project.org/web/packages/plot3D/index.html) offre la possibilità di creare grafici in 3D, se i tuoi dati lo supportano. Con esso è possibile produrre visualizzazioni sofisticate.

![grafici 3D](../../../../../translated_images/it/3d.db1734c151eee87d924989306a00e23f8cddac6a0aab122852ece220e9448def.png)

## Animazione e visualizzazione di grafici in 3D

Alcune delle migliori visualizzazioni dei dati oggi sono animate. Shirley Wu ha creato visualizzazioni straordinarie con D3, come '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', dove ogni fiore rappresenta una visualizzazione di un film. Un altro esempio per il Guardian è 'bussed out', un'esperienza interattiva che combina visualizzazioni con Greensock e D3, oltre a un formato di articolo scrollytelling per mostrare come NYC gestisce il problema dei senzatetto bussando le persone fuori dalla città.

![busing](../../../../../translated_images/it/busing.8157cf1bc89a3f65052d362a78c72f964982ceb9dcacbe44480e35909c3dce62.png)

> "Bussed Out: How America Moves its Homeless" dal [Guardian](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Visualizzazioni di Nadieh Bremer & Shirley Wu

Sebbene questa lezione non sia sufficiente per approfondire l'insegnamento di queste potenti librerie di visualizzazione, prova a utilizzare D3 in un'app Vue.js per visualizzare il libro "Le relazioni pericolose" come una rete sociale animata.

> "Les Liaisons Dangereuses" è un romanzo epistolare, ovvero un romanzo presentato come una serie di lettere. Scritto nel 1782 da Choderlos de Laclos, racconta le manovre sociali spietate e moralmente corrotte di due protagonisti in duello dell'aristocrazia francese del tardo XVIII secolo, il Visconte di Valmont e la Marchesa di Merteuil. Entrambi incontrano la loro fine, ma non senza infliggere un grande danno sociale. Il romanzo si sviluppa come una serie di lettere scritte a varie persone nei loro circoli, tramando vendette o semplicemente per creare problemi. Crea una visualizzazione di queste lettere per scoprire i principali protagonisti della narrazione, visivamente.

Completerai un'app web che visualizzerà una vista animata di questa rete sociale. Utilizza una libreria progettata per creare una [visualizzazione di una rete](https://github.com/emiliorizzo/vue-d3-network) utilizzando Vue.js e D3. Quando l'app è in esecuzione, puoi spostare i nodi sullo schermo per riorganizzare i dati.

![liaisons](../../../../../translated_images/it/liaisons.90ce7360bcf8476558f700bbbaf198ad697d5b5cb2829ba141a89c0add7c6ecd.png)

## Progetto: Creare un grafico per mostrare una rete usando D3.js

> Questa cartella della lezione include una cartella `solution` dove puoi trovare il progetto completato, per riferimento.

1. Segui le istruzioni nel file README.md nella cartella radice dello starter. Assicurati di avere NPM e Node.js in esecuzione sulla tua macchina prima di installare le dipendenze del progetto.

2. Apri la cartella `starter/src`. Troverai una cartella `assets` dove è presente un file .json con tutte le lettere del romanzo, numerate, con annotazioni 'to' e 'from'.

3. Completa il codice in `components/Nodes.vue` per abilitare la visualizzazione. Cerca il metodo chiamato `createLinks()` e aggiungi il seguente ciclo nidificato.

Cicla attraverso l'oggetto .json per catturare i dati 'to' e 'from' delle lettere e costruire l'oggetto `links` affinché la libreria di visualizzazione possa utilizzarlo:

```javascript
//loop through letters
      let f = 0;
      let t = 0;
      for (var i = 0; i < letters.length; i++) {
          for (var j = 0; j < characters.length; j++) {
              
            if (characters[j] == letters[i].from) {
              f = j;
            }
            if (characters[j] == letters[i].to) {
              t = j;
            }
        }
        this.links.push({ sid: f, tid: t });
      }
  ```

Esegui la tua app dal terminale (npm run serve) e goditi la visualizzazione!

## 🚀 Sfida

Fai un giro su internet per scoprire visualizzazioni ingannevoli. Come l'autore inganna l'utente, e ciò è intenzionale? Prova a correggere le visualizzazioni per mostrare come dovrebbero apparire.

## [Quiz Post-Lezione](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/25)

## Revisione & Studio Autonomo

Ecco alcuni articoli da leggere sulle visualizzazioni dei dati ingannevoli:

https://gizmodo.com/how-to-lie-with-data-visualization-1563576606

http://ixd.prattsi.org/2017/12/visual-lies-usability-in-deceptive-data-visualizations/

Dai un'occhiata a queste interessanti visualizzazioni di beni e artefatti storici:

https://handbook.pubpub.org/

Leggi questo articolo su come l'animazione può migliorare le visualizzazioni:

https://medium.com/@EvanSinar/use-animation-to-supercharge-data-visualization-cd905a882ad4

## Compito

[Costruisci la tua visualizzazione personalizzata](assignment.md)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.