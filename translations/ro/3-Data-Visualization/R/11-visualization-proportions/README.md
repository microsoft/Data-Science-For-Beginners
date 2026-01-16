<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "47028abaaafa2bcb1079702d20569066",
  "translation_date": "2025-08-26T17:21:01+00:00",
  "source_file": "3-Data-Visualization/R/11-visualization-proportions/README.md",
  "language_code": "ro"
}
-->
# Vizualizarea Proporțiilor

|![ Sketchnote de [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Vizualizarea Proporțiilor - _Sketchnote de [@nitya](https://twitter.com/nitya)_ |

În această lecție, vei folosi un set de date axat pe natură pentru a vizualiza proporții, cum ar fi câte tipuri diferite de ciuperci sunt prezente într-un set de date despre ciuperci. Hai să explorăm aceste ciuperci fascinante folosind un set de date obținut de la Audubon, care listează detalii despre 23 de specii de ciuperci cu lamele din familiile Agaricus și Lepiota. Vei experimenta cu vizualizări interesante precum:

- Grafice de tip plăcintă 🥧  
- Grafice de tip gogoașă 🍩  
- Grafice de tip vafă 🧇  

> 💡 Un proiect foarte interesant numit [Charticulator](https://charticulator.com) de la Microsoft Research oferă o interfață gratuită de tip drag and drop pentru vizualizări de date. Într-unul dintre tutorialele lor, folosesc și acest set de date despre ciuperci! Așadar, poți explora datele și învăța biblioteca în același timp: [Tutorial Charticulator](https://charticulator.com/tutorials/tutorial4.html).

## [Chestionar înainte de lecție](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## Cunoaște-ți ciupercile 🍄

Ciupercile sunt foarte interesante. Hai să importăm un set de date pentru a le studia:

```r
mushrooms = read.csv('../../data/mushrooms.csv')
head(mushrooms)
```  
Se afișează un tabel cu date excelente pentru analiză:


| clasă      | formă-pălărie | suprafață-pălărie | culoare-pălărie | vânătăi | miros    | atașare-lamele | spațiere-lamele | dimensiune-lamele | culoare-lamele | formă-picior | rădăcină-picior | suprafață-picior-deasupra-inelului | suprafață-picior-dedesubt-inelului | culoare-picior-deasupra-inelului | culoare-picior-dedesubt-inelului | tip-voal | culoare-voal | număr-inele | tip-inel | culoare-spori | populație | habitat |
| --------- | ------------- | ----------------- | --------------- | ------- | -------- | -------------- | ---------------- | ---------------- | -------------- | ------------ | -------------- | ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- | --------- | ------------ | ----------- | -------- | ------------- | --------- | ------- |
| Otrăvitoare | Convexă      | Netedă            | Maro            | Vânătăi | Pungent  | Liber          | Apropiate        | Înguste          | Negru          | Lărgit       | Egal          | Netedă                          | Netedă                          | Albă                            | Albă                            | Parțial   | Albă         | Unu         | Pandantiv | Negru         | Răspândită | Urban   |
| Comestibilă | Convexă      | Netedă            | Galben          | Vânătăi | Migdale  | Liber          | Apropiate        | Late            | Negru          | Lărgit       | Club          | Netedă                          | Netedă                          | Albă                            | Albă                            | Parțial   | Albă         | Unu         | Pandantiv | Maro          | Numeroasă | Iarbă   |
| Comestibilă | Clopot       | Netedă            | Alb             | Vânătăi | Anason   | Liber          | Apropiate        | Late            | Maro           | Lărgit       | Club          | Netedă                          | Netedă                          | Albă                            | Albă                            | Parțial   | Albă         | Unu         | Pandantiv | Maro          | Numeroasă | Pajiști |
| Otrăvitoare | Convexă      | Solzoasă          | Alb             | Vânătăi | Pungent  | Liber          | Apropiate        | Înguste          | Maro           | Lărgit       | Egal          | Netedă                          | Netedă                          | Albă                            | Albă                            | Parțial   | Albă         | Unu         | Pandantiv | Negru         | Răspândită | Urban   |
| Comestibilă | Convexă      | Netedă            | Verde           | Fără vânătăi | Niciunul | Liber        | Înghesuite       | Late            | Negru          | Subțiat      | Egal          | Netedă                          | Netedă                          | Albă                            | Albă                            | Parțial   | Albă         | Unu         | Evanescent | Maro          | Abundentă | Iarbă   |
| Comestibilă | Convexă      | Solzoasă          | Galben          | Vânătăi | Migdale  | Liber          | Apropiate        | Late            | Maro           | Lărgit       | Club          | Netedă                          | Netedă                          | Albă                            | Albă                            | Parțial   | Albă         | Unu         | Pandantiv | Negru         | Numeroasă | Iarbă   |

Imediat observi că toate datele sunt textuale. Va trebui să convertești aceste date pentru a le putea folosi într-un grafic. Majoritatea datelor, de fapt, sunt reprezentate ca un obiect:

```r
names(mushrooms)
```  

Rezultatul este:

```output
[1] "class"                    "cap.shape"               
 [3] "cap.surface"              "cap.color"               
 [5] "bruises"                  "odor"                    
 [7] "gill.attachment"          "gill.spacing"            
 [9] "gill.size"                "gill.color"              
[11] "stalk.shape"              "stalk.root"              
[13] "stalk.surface.above.ring" "stalk.surface.below.ring"
[15] "stalk.color.above.ring"   "stalk.color.below.ring"  
[17] "veil.type"                "veil.color"              
[19] "ring.number"              "ring.type"               
[21] "spore.print.color"        "population"              
[23] "habitat"            
```  
Ia aceste date și convertește coloana 'clasă' într-o categorie:

```r
library(dplyr)
grouped=mushrooms %>%
  group_by(class) %>%
  summarise(count=n())
```  

Acum, dacă afișezi datele despre ciuperci, poți vedea că au fost grupate în categorii conform claselor comestibile/otrăvitoare:  
```r
View(grouped)
```  

| clasă      | număr |
| --------- | ----- |
| Comestibilă | 4208 |
| Otrăvitoare | 3916 |

Dacă urmezi ordinea prezentată în acest tabel pentru a crea etichetele categoriei clasă, poți construi un grafic de tip plăcintă.

## Plăcintă!

```r
pie(grouped$count,grouped$class, main="Edible?")
```  
Voila, un grafic de tip plăcintă care arată proporțiile acestor date conform celor două clase de ciuperci. Este foarte important să obții ordinea corectă a etichetelor, mai ales aici, așa că asigură-te că verifici ordinea în care este construită matricea de etichete!

![grafic plăcintă](../../../../../translated_images/ro/pie1-wb.685df063673751f4b0b82127f7a52c7f9a920192f22ae61ad28412ba9ace97bf.png)

## Gogoși!

Un grafic de tip gogoașă, care este o variantă mai interesantă vizual a graficului de tip plăcintă, are o gaură în mijloc. Hai să ne uităm la datele noastre folosind această metodă.

Aruncă o privire la diferitele habitate în care cresc ciupercile:

```r
library(dplyr)
habitat=mushrooms %>%
  group_by(habitat) %>%
  summarise(count=n())
View(habitat)
```  
Rezultatul este:  
| habitat | număr |
| ------- | ----- |
| Iarbă   | 2148  |
| Frunze  | 832   |
| Pajiști | 292   |
| Cărări  | 1144  |
| Urban   | 368   |
| Deșeuri | 192   |
| Lemn    | 3148  |

Aici, grupezi datele după habitat. Sunt 7 listate, așa că folosește-le ca etichete pentru graficul de tip gogoașă:

```r
library(ggplot2)
library(webr)
PieDonut(habitat, aes(habitat, count=count))
```  

![grafic gogoașă](../../../../../translated_images/ro/donut-wb.34e6fb275da9d834c2205145e39a3de9b6878191dcdba6f7a9e85f4b520449bc.png)

Acest cod folosește două biblioteci - ggplot2 și webr. Folosind funcția PieDonut din biblioteca webr, putem crea ușor un grafic de tip gogoașă!

Graficele de tip gogoașă în R pot fi realizate și folosind doar biblioteca ggplot2. Poți afla mai multe despre asta [aici](https://www.r-graph-gallery.com/128-ring-or-donut-plot.html) și să încerci singur.

Acum că știi cum să grupezi datele și să le afișezi ca plăcintă sau gogoașă, poți explora alte tipuri de grafice. Încearcă un grafic de tip vafă, care este doar o altă modalitate de a explora cantitățile.

## Vafe!

Un grafic de tip 'vafă' este o modalitate diferită de a vizualiza cantitățile ca o matrice 2D de pătrate. Încearcă să vizualizezi diferitele cantități de culori ale pălăriilor de ciuperci din acest set de date. Pentru a face asta, trebuie să instalezi o bibliotecă auxiliară numită [waffle](https://cran.r-project.org/web/packages/waffle/waffle.pdf) și să o folosești pentru a genera vizualizarea:

```r
install.packages("waffle", repos = "https://cinc.rud.is")
```  

Selectează un segment din datele tale pentru a le grupa:

```r
library(dplyr)
cap_color=mushrooms %>%
  group_by(cap.color) %>%
  summarise(count=n())
View(cap_color)
```  

Creează un grafic de tip vafă prin crearea etichetelor și apoi gruparea datelor:

```r
library(waffle)
names(cap_color$count) = paste0(cap_color$cap.color)
waffle((cap_color$count/10), rows = 7, title = "Waffle Chart")+scale_fill_manual(values=c("brown", "#F0DC82", "#D2691E", "green", 
                                                                                     "pink", "purple", "red", "grey", 
                                                                                     "yellow","white"))
```  

Folosind un grafic de tip vafă, poți vedea clar proporțiile culorilor pălăriilor din acest set de date despre ciuperci. Interesant, există multe ciuperci cu pălării verzi!

![grafic vafă](../../../../../translated_images/ro/waffle.aaa75c5337735a6ef32ace0ffb6506ef49e5aefe870ffd72b1bb080f4843c217.png)

În această lecție, ai învățat trei modalități de a vizualiza proporțiile. Mai întâi, trebuie să grupezi datele în categorii și apoi să decizi care este cea mai bună modalitate de a afișa datele - plăcintă, gogoașă sau vafă. Toate sunt delicioase și oferă utilizatorului o imagine instantanee a unui set de date.

## 🚀 Provocare

Încearcă să recreezi aceste grafice delicioase în [Charticulator](https://charticulator.com).  
## [Chestionar după lecție](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## Recapitulare & Studiu Individual

Uneori nu este evident când să folosești un grafic de tip plăcintă, gogoașă sau vafă. Iată câteva articole de citit pe acest subiect:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart  

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce  

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm  

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402  

Fă cercetări pentru a găsi mai multe informații despre această decizie dificilă.  

## Temă

[Încearcă în Excel](assignment.md)  

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.