<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a33c5d4b4156a2b41788d8720b6f724c",
  "translation_date": "2025-08-28T11:06:39+00:00",
  "source_file": "3-Data-Visualization/R/12-visualization-relationships/README.md",
  "language_code": "it"
}
-->
# Visualizzare le Relazioni: Tutto sul Miele 🍯

|![ Sketchnote di [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Visualizzare le Relazioni - _Sketchnote di [@nitya](https://twitter.com/nitya)_ |

Continuando con il focus sulla natura della nostra ricerca, scopriamo visualizzazioni interessanti per mostrare le relazioni tra i vari tipi di miele, secondo un dataset derivato dal [Dipartimento dell'Agricoltura degli Stati Uniti](https://www.nass.usda.gov/About_NASS/index.php).

Questo dataset di circa 600 elementi mostra la produzione di miele in molti stati americani. Ad esempio, è possibile osservare il numero di colonie, la resa per colonia, la produzione totale, le scorte, il prezzo per libbra e il valore del miele prodotto in un determinato stato dal 1998 al 2012, con una riga per anno per ogni stato.

Sarà interessante visualizzare la relazione tra la produzione annuale di un determinato stato e, ad esempio, il prezzo del miele in quello stato. In alternativa, si potrebbe visualizzare la relazione tra la resa per colonia nei vari stati. Questo intervallo di anni copre il devastante 'CCD' o 'Colony Collapse Disorder', osservato per la prima volta nel 2006 (http://npic.orst.edu/envir/ccd.html), rendendo questo dataset particolarmente significativo da studiare. 🐝

## [Quiz pre-lezione](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

In questa lezione, puoi utilizzare ggplot2, che hai già usato in precedenza, come una buona libreria per visualizzare le relazioni tra variabili. Particolarmente interessante è l'uso delle funzioni `geom_point` e `qplot` di ggplot2, che permettono di creare grafici a dispersione e grafici a linee per visualizzare rapidamente le '[relazioni statistiche](https://ggplot2.tidyverse.org/)', consentendo al data scientist di comprendere meglio come le variabili si relazionano tra loro.

## Grafici a dispersione

Utilizza un grafico a dispersione per mostrare come il prezzo del miele si è evoluto anno dopo anno, per stato. ggplot2, utilizzando `ggplot` e `geom_point`, raggruppa comodamente i dati per stato e visualizza i punti dati sia per dati categorici che numerici.

Iniziamo importando i dati e Seaborn:

```r
honey=read.csv('../../data/honey.csv')
head(honey)
```
Noterai che i dati sul miele contengono diverse colonne interessanti, tra cui anno e prezzo per libbra. Esploriamo questi dati, raggruppati per stato americano:

| stato | numcol | yieldpercol | totalprod | stocks   | priceperlb | prodvalue | anno |
| ----- | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL    | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ    | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR    | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA    | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO    | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |
| FL    | 230000 | 98          |22540000   | 4508000  | 0.64       | 14426000  | 1998 |

Crea un grafico a dispersione di base per mostrare la relazione tra il prezzo per libbra del miele e il suo stato di origine negli Stati Uniti. Fai in modo che l'asse `y` sia abbastanza alto da visualizzare tutti gli stati:

```r
library(ggplot2)
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(colour = "blue")
```
![scatterplot 1](../../../../../translated_images/scatter1.86b8900674d88b26dd3353a83fe604e9ab3722c4680cc40ee9beb452ff02cdea.it.png)

Ora, mostra gli stessi dati con una scala di colori che richiami il miele per evidenziare come il prezzo si evolve nel corso degli anni. Puoi farlo aggiungendo un parametro 'scale_color_gradientn' per mostrare il cambiamento anno dopo anno:

> ✅ Scopri di più su [scale_color_gradientn](https://www.rdocumentation.org/packages/ggplot2/versions/0.9.1/topics/scale_colour_gradientn) - prova uno schema di colori arcobaleno!

```r
ggplot(honey, aes(x = priceperlb, y = state, color=year)) +
  geom_point()+scale_color_gradientn(colours = colorspace::heat_hcl(7))
```
![scatterplot 2](../../../../../translated_images/scatter2.4d1cbc693bad20e2b563888747eb6bdf65b73ce449d903f7cd4068a78502dcff.it.png)

Con questo cambiamento di schema di colori, puoi vedere chiaramente una forte progressione nel corso degli anni in termini di prezzo del miele per libbra. Infatti, se guardi un sottoinsieme di dati per verificare (scegli uno stato, ad esempio l'Arizona), puoi osservare un pattern di aumento dei prezzi anno dopo anno, con poche eccezioni:

| stato | numcol | yieldpercol | totalprod | stocks  | priceperlb | prodvalue | anno |
| ----- | ------ | ----------- | --------- | ------- | ---------- | --------- | ---- |
| AZ    | 55000  | 60          | 3300000   | 1485000 | 0.64       | 2112000   | 1998 |
| AZ    | 52000  | 62          | 3224000   | 1548000 | 0.62       | 1999000   | 1999 |
| AZ    | 40000  | 59          | 2360000   | 1322000 | 0.73       | 1723000   | 2000 |
| AZ    | 43000  | 59          | 2537000   | 1142000 | 0.72       | 1827000   | 2001 |
| AZ    | 38000  | 63          | 2394000   | 1197000 | 1.08       | 2586000   | 2002 |
| AZ    | 35000  | 72          | 2520000   | 983000  | 1.34       | 3377000   | 2003 |
| AZ    | 32000  | 55          | 1760000   | 774000  | 1.11       | 1954000   | 2004 |
| AZ    | 36000  | 50          | 1800000   | 720000  | 1.04       | 1872000   | 2005 |
| AZ    | 30000  | 65          | 1950000   | 839000  | 0.91       | 1775000   | 2006 |
| AZ    | 30000  | 64          | 1920000   | 902000  | 1.26       | 2419000   | 2007 |
| AZ    | 25000  | 64          | 1600000   | 336000  | 1.26       | 2016000   | 2008 |
| AZ    | 20000  | 52          | 1040000   | 562000  | 1.45       | 1508000   | 2009 |
| AZ    | 24000  | 77          | 1848000   | 665000  | 1.52       | 2809000   | 2010 |
| AZ    | 23000  | 53          | 1219000   | 427000  | 1.55       | 1889000   | 2011 |
| AZ    | 22000  | 46          | 1012000   | 253000  | 1.79       | 1811000   | 2012 |

Un altro modo per visualizzare questa progressione è utilizzare la dimensione, anziché il colore. Per gli utenti daltonici, questa potrebbe essere un'opzione migliore. Modifica la tua visualizzazione per mostrare un aumento del prezzo attraverso un aumento della circonferenza dei punti:

```r
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(aes(size = year),colour = "blue") +
  scale_size_continuous(range = c(0.25, 3))
```
Puoi vedere la dimensione dei punti aumentare gradualmente.

![scatterplot 3](../../../../../translated_images/scatter3.722d21e6f20b3ea2e18339bb9b10d75906126715eb7d5fdc88fe74dcb6d7066a.it.png)

È un semplice caso di domanda e offerta? A causa di fattori come il cambiamento climatico e il collasso delle colonie, c'è meno miele disponibile per l'acquisto anno dopo anno, e quindi il prezzo aumenta?

Per scoprire una correlazione tra alcune delle variabili in questo dataset, esploriamo alcuni grafici a linee.

## Grafici a linee

Domanda: C'è un chiaro aumento del prezzo del miele per libbra anno dopo anno? Puoi scoprirlo facilmente creando un singolo grafico a linee:

```r
qplot(honey$year,honey$priceperlb, geom='smooth', span =0.5, xlab = "year",ylab = "priceperlb")
```
Risposta: Sì, con alcune eccezioni intorno all'anno 2003:

![line chart 1](../../../../../translated_images/line1.299b576fbb2a59e60a59e7130030f59836891f90302be084e4e8d14da0562e2a.it.png)

Domanda: Bene, nel 2003 possiamo anche vedere un picco nella fornitura di miele? E se guardassimo la produzione totale anno dopo anno?

```python
qplot(honey$year,honey$totalprod, geom='smooth', span =0.5, xlab = "year",ylab = "totalprod")
```

![line chart 2](../../../../../translated_images/line2.3b18fcda7176ceba5b6689eaaabb817d49c965e986f11cac1ae3f424030c34d8.it.png)

Risposta: Non proprio. Se guardi la produzione totale, sembra effettivamente essere aumentata in quell'anno particolare, anche se generalmente la quantità di miele prodotta è in calo durante questi anni.

Domanda: In tal caso, cosa potrebbe aver causato quel picco nel prezzo del miele intorno al 2003?

Per scoprirlo, puoi esplorare una griglia di faccette.

## Griglie di faccette

Le griglie di faccette prendono una faccetta del tuo dataset (nel nostro caso, puoi scegliere 'anno' per evitare di produrre troppe faccette). Seaborn può quindi creare un grafico per ciascuna di queste faccette delle coordinate x e y scelte per un confronto visivo più semplice. Il 2003 si distingue in questo tipo di confronto?

Crea una griglia di faccette utilizzando `facet_wrap` come raccomandato dalla [documentazione di ggplot2](https://ggplot2.tidyverse.org/reference/facet_wrap.html).

```r
ggplot(honey, aes(x=yieldpercol, y = numcol,group = 1)) + 
  geom_line() + facet_wrap(vars(year))
```
In questa visualizzazione, puoi confrontare la resa per colonia e il numero di colonie anno dopo anno, fianco a fianco con un wrap impostato a 3 per le colonne:

![facet grid](../../../../../translated_images/facet.491ad90d61c2a7cc69b50c929f80786c749e38217ccedbf1e22ed8909b65987c.it.png)

Per questo dataset, nulla di particolarmente evidente emerge riguardo al numero di colonie e alla loro resa, anno dopo anno e stato per stato. C'è un modo diverso per cercare una correlazione tra queste due variabili?

## Grafici a linee doppie

Prova un grafico multilinea sovrapponendo due grafici a linee uno sopra l'altro, utilizzando le funzioni `par` e `plot` di R. Tracceremo l'anno sull'asse x e visualizzeremo due assi y. Quindi, visualizza la resa per colonia e il numero di colonie, sovrapposti:

```r
par(mar = c(5, 4, 4, 4) + 0.3)              
plot(honey$year, honey$numcol, pch = 16, col = 2,type="l")              
par(new = TRUE)                             
plot(honey$year, honey$yieldpercol, pch = 17, col = 3,              
     axes = FALSE, xlab = "", ylab = "",type="l")
axis(side = 4, at = pretty(range(y2)))      
mtext("colony yield", side = 4, line = 3)   
```
![superimposed plots](../../../../../translated_images/dual-line.fc4665f360a54018d7df9bc6abcc26460112e17dcbda18d3b9ae6109b32b36c3.it.png)

Sebbene nulla salti all'occhio intorno all'anno 2003, questo ci permette di concludere la lezione con una nota un po' più positiva: mentre il numero di colonie è generalmente in calo, sembra stabilizzarsi anche se la loro resa per colonia diminuisce.

Forza, api, forza!

🐝❤️
## 🚀 Sfida

In questa lezione, hai imparato un po' di più su altri usi dei grafici a dispersione e delle griglie a linee, incluse le griglie di faccette. Sfida te stesso a creare una griglia di faccette utilizzando un dataset diverso, magari uno che hai usato prima di queste lezioni. Nota quanto tempo impiegano a essere create e quanto devi essere attento al numero di griglie che devi disegnare utilizzando queste tecniche.
## [Quiz post-lezione](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## Revisione & Studio Autonomo

I grafici a linee possono essere semplici o piuttosto complessi. Fai un po' di lettura nella [documentazione di ggplot2](https://ggplot2.tidyverse.org/reference/geom_path.html#:~:text=geom_line()%20connects%20them%20in,which%20cases%20are%20connected%20together) sui vari modi in cui puoi costruirli. Prova a migliorare i grafici a linee che hai costruito in questa lezione con altri metodi elencati nei documenti.
## Compito

[Immergiti nell'alveare](assignment.md)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.