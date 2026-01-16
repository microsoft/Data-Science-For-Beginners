<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "47028abaaafa2bcb1079702d20569066",
  "translation_date": "2025-08-26T23:13:21+00:00",
  "source_file": "3-Data-Visualization/R/11-visualization-proportions/README.md",
  "language_code": "el"
}
-->
# Οπτικοποίηση Αναλογιών

|![ Σκίτσο από [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Οπτικοποίηση Αναλογιών - _Σκίτσο από [@nitya](https://twitter.com/nitya)_ |

Σε αυτό το μάθημα, θα χρησιμοποιήσετε ένα διαφορετικό σύνολο δεδομένων με επίκεντρο τη φύση για να οπτικοποιήσετε αναλογίες, όπως πόσα διαφορετικά είδη μανιταριών υπάρχουν σε ένα δεδομένο σύνολο δεδομένων για μανιτάρια. Ας εξερευνήσουμε αυτά τα συναρπαστικά μανιτάρια χρησιμοποιώντας ένα σύνολο δεδομένων από το Audubon που περιλαμβάνει λεπτομέρειες για 23 είδη μανιταριών με βράγχια στις οικογένειες Agaricus και Lepiota. Θα πειραματιστείτε με νόστιμες οπτικοποιήσεις όπως:

- Γραφήματα πίτας 🥧
- Γραφήματα ντόνατ 🍩
- Γραφήματα βάφλας 🧇

> 💡 Ένα πολύ ενδιαφέρον έργο που ονομάζεται [Charticulator](https://charticulator.com) από τη Microsoft Research προσφέρει μια δωρεάν διεπαφή drag and drop για οπτικοποιήσεις δεδομένων. Σε ένα από τα μαθήματά τους χρησιμοποιούν επίσης αυτό το σύνολο δεδομένων για μανιτάρια! Έτσι, μπορείτε να εξερευνήσετε τα δεδομένα και να μάθετε τη βιβλιοθήκη ταυτόχρονα: [Charticulator tutorial](https://charticulator.com/tutorials/tutorial4.html).

## [Προ-μάθημα κουίζ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## Γνωρίστε τα μανιτάρια σας 🍄

Τα μανιτάρια είναι πολύ ενδιαφέροντα. Ας εισάγουμε ένα σύνολο δεδομένων για να τα μελετήσουμε:

```r
mushrooms = read.csv('../../data/mushrooms.csv')
head(mushrooms)
```
Ένας πίνακας εμφανίζεται με εξαιρετικά δεδομένα για ανάλυση:

| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Poisonous | Convex    | Smooth      | Brown     | Bruises | Pungent | Free            | Close        | Narrow    | Black      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |
| Edible    | Convex    | Smooth      | Yellow    | Bruises | Almond  | Free            | Close        | Broad     | Black      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Grasses |
| Edible    | Bell      | Smooth      | White     | Bruises | Anise   | Free            | Close        | Broad     | Brown      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Meadows |
| Poisonous | Convex    | Scaly       | White     | Bruises | Pungent | Free            | Close        | Narrow    | Brown      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban 
| Edible | Convex       |Smooth       | Green     | No Bruises| None   |Free            | Crowded       | Broad     | Black      | Tapering   | Equal      |  Smooth | Smooth                    | White                 | White                  | Partial    | White     | One         | Evanescent | Brown             | Abundant | Grasses
|Edible  |  Convex      | Scaly   | Yellow         | Bruises  | Almond  | Free | Close  |   Broad   |   Brown  | Enlarging   |   Club                      | Smooth                  | Smooth    | White                 |  White                | Partial      | White    |  One  |  Pendant | Black   | Numerous | Grasses
      
Αμέσως παρατηρείτε ότι όλα τα δεδομένα είναι κειμενικά. Θα πρέπει να μετατρέψετε αυτά τα δεδομένα για να μπορέσετε να τα χρησιμοποιήσετε σε ένα γράφημα. Στην πραγματικότητα, τα περισσότερα δεδομένα αναπαρίστανται ως αντικείμενο:

```r
names(mushrooms)
```

Η έξοδος είναι:

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
Πάρτε αυτά τα δεδομένα και μετατρέψτε τη στήλη 'class' σε κατηγορία:

```r
library(dplyr)
grouped=mushrooms %>%
  group_by(class) %>%
  summarise(count=n())
```

Τώρα, αν εκτυπώσετε τα δεδομένα των μανιταριών, μπορείτε να δείτε ότι έχουν ομαδοποιηθεί σε κατηγορίες σύμφωνα με την κατηγορία δηλητηριώδη/βρώσιμα:
```r
View(grouped)
```

| class | count |
| --------- | --------- |
| Edible | 4208 |
| Poisonous| 3916 |

Αν ακολουθήσετε τη σειρά που παρουσιάζεται σε αυτόν τον πίνακα για να δημιουργήσετε τις ετικέτες κατηγορίας, μπορείτε να δημιουργήσετε ένα γράφημα πίτας.

## Πίτα!

```r
pie(grouped$count,grouped$class, main="Edible?")
```
Ορίστε, ένα γράφημα πίτας που δείχνει τις αναλογίες αυτών των δεδομένων σύμφωνα με αυτές τις δύο κατηγορίες μανιταριών. Είναι αρκετά σημαντικό να έχετε τη σωστή σειρά των ετικετών, ειδικά εδώ, οπότε βεβαιωθείτε ότι έχετε επαληθεύσει τη σειρά με την οποία δημιουργείται ο πίνακας ετικετών!

![pie chart](../../../../../translated_images/el/pie1-wb.685df063673751f4b0b82127f7a52c7f9a920192f22ae61ad28412ba9ace97bf.png)

## Ντόνατ!

Ένα κάπως πιο οπτικά ενδιαφέρον γράφημα πίτας είναι το γράφημα ντόνατ, το οποίο είναι ένα γράφημα πίτας με μια τρύπα στη μέση. Ας δούμε τα δεδομένα μας χρησιμοποιώντας αυτή τη μέθοδο.

Δείτε τους διάφορους βιότοπους όπου μεγαλώνουν τα μανιτάρια:

```r
library(dplyr)
habitat=mushrooms %>%
  group_by(habitat) %>%
  summarise(count=n())
View(habitat)
```
Η έξοδος είναι:
| habitat| count |
| --------- | --------- |
| Grasses    | 2148 |
| Leaves| 832 |
| Meadows    | 292 |
| Paths| 1144 |
| Urban    | 368 |
| Waste| 192 |
| Wood| 3148 |

Εδώ, ομαδοποιείτε τα δεδομένα σας ανά βιότοπο. Υπάρχουν 7 καταγεγραμμένοι, οπότε χρησιμοποιήστε αυτούς ως ετικέτες για το γράφημα ντόνατ:

```r
library(ggplot2)
library(webr)
PieDonut(habitat, aes(habitat, count=count))
```

![donut chart](../../../../../translated_images/el/donut-wb.34e6fb275da9d834c2205145e39a3de9b6878191dcdba6f7a9e85f4b520449bc.png)

Αυτός ο κώδικας χρησιμοποιεί τις δύο βιβλιοθήκες - ggplot2 και webr. Χρησιμοποιώντας τη συνάρτηση PieDonut της βιβλιοθήκης webr, μπορούμε να δημιουργήσουμε εύκολα ένα γράφημα ντόνατ!

Τα γραφήματα ντόνατ στο R μπορούν να δημιουργηθούν χρησιμοποιώντας μόνο τη βιβλιοθήκη ggplot2. Μπορείτε να μάθετε περισσότερα για αυτό [εδώ](https://www.r-graph-gallery.com/128-ring-or-donut-plot.html) και να το δοκιμάσετε μόνοι σας.

Τώρα που ξέρετε πώς να ομαδοποιείτε τα δεδομένα σας και να τα εμφανίζετε ως πίτα ή ντόνατ, μπορείτε να εξερευνήσετε άλλους τύπους γραφημάτων. Δοκιμάστε ένα γράφημα βάφλας, το οποίο είναι απλώς ένας διαφορετικός τρόπος εξερεύνησης ποσοτήτων.

## Βάφλες!

Ένα γράφημα τύπου 'βάφλας' είναι ένας διαφορετικός τρόπος οπτικοποίησης ποσοτήτων ως δισδιάστατος πίνακας τετραγώνων. Δοκιμάστε να οπτικοποιήσετε τις διαφορετικές ποσότητες χρωμάτων καπέλων μανιταριών σε αυτό το σύνολο δεδομένων. Για να το κάνετε αυτό, πρέπει να εγκαταστήσετε μια βοηθητική βιβλιοθήκη που ονομάζεται [waffle](https://cran.r-project.org/web/packages/waffle/waffle.pdf) και να τη χρησιμοποιήσετε για να δημιουργήσετε την οπτικοποίησή σας:

```r
install.packages("waffle", repos = "https://cinc.rud.is")
```

Επιλέξτε ένα τμήμα των δεδομένων σας για ομαδοποίηση:

```r
library(dplyr)
cap_color=mushrooms %>%
  group_by(cap.color) %>%
  summarise(count=n())
View(cap_color)
```

Δημιουργήστε ένα γράφημα βάφλας δημιουργώντας ετικέτες και στη συνέχεια ομαδοποιώντας τα δεδομένα σας:

```r
library(waffle)
names(cap_color$count) = paste0(cap_color$cap.color)
waffle((cap_color$count/10), rows = 7, title = "Waffle Chart")+scale_fill_manual(values=c("brown", "#F0DC82", "#D2691E", "green", 
                                                                                     "pink", "purple", "red", "grey", 
                                                                                     "yellow","white"))
```

Χρησιμοποιώντας ένα γράφημα βάφλας, μπορείτε να δείτε ξεκάθαρα τις αναλογίες χρωμάτων καπέλων σε αυτό το σύνολο δεδομένων μανιταριών. Ενδιαφέρον είναι ότι υπάρχουν πολλά μανιτάρια με πράσινα καπέλα!

![waffle chart](../../../../../translated_images/el/waffle.aaa75c5337735a6ef32ace0ffb6506ef49e5aefe870ffd72b1bb080f4843c217.png)

Σε αυτό το μάθημα, μάθατε τρεις τρόπους για να οπτικοποιήσετε αναλογίες. Πρώτα, πρέπει να ομαδοποιήσετε τα δεδομένα σας σε κατηγορίες και στη συνέχεια να αποφασίσετε ποιος είναι ο καλύτερος τρόπος για να εμφανίσετε τα δεδομένα - πίτα, ντόνατ ή βάφλα. Όλα είναι νόστιμα και προσφέρουν στον χρήστη μια άμεση εικόνα ενός συνόλου δεδομένων.

## 🚀 Πρόκληση

Δοκιμάστε να αναδημιουργήσετε αυτά τα νόστιμα γραφήματα στο [Charticulator](https://charticulator.com).

## [Μετά το μάθημα κουίζ](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## Ανασκόπηση & Αυτομελέτη

Μερικές φορές δεν είναι προφανές πότε να χρησιμοποιήσετε ένα γράφημα πίτας, ντόνατ ή βάφλας. Ακολουθούν μερικά άρθρα για να διαβάσετε σχετικά με αυτό το θέμα:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Κάντε έρευνα για να βρείτε περισσότερες πληροφορίες σχετικά με αυτή τη δύσκολη απόφαση.

## Εργασία

[Δοκιμάστε το στο Excel](assignment.md)

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.