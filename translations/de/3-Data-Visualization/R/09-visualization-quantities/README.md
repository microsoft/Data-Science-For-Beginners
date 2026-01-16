<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-24T22:50:01+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "de"
}
-->
# Visualisierung von Mengen
|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Visualisierung von Mengen - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

In dieser Lektion wirst du erkunden, wie du einige der vielen verfügbaren R-Paketbibliotheken nutzen kannst, um interessante Visualisierungen rund um das Konzept der Menge zu erstellen. Mithilfe eines bereinigten Datensatzes über die Vögel von Minnesota kannst du viele interessante Fakten über die lokale Tierwelt erfahren.  
## [Quiz vor der Vorlesung](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## Beobachte die Flügelspannweite mit ggplot2
Eine ausgezeichnete Bibliothek, um sowohl einfache als auch anspruchsvolle Diagramme und Grafiken verschiedener Art zu erstellen, ist [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html). Im Allgemeinen umfasst der Prozess des Plotten von Daten mit diesen Bibliotheken die Identifizierung der Teile deines Dataframes, die du anvisieren möchtest, die Durchführung notwendiger Transformationen der Daten, die Zuweisung von x- und y-Achsenwerten, die Entscheidung über die Art des Diagramms und schließlich die Darstellung des Diagramms.

`ggplot2` ist ein System zur deklarativen Erstellung von Grafiken, basierend auf der Grammatik der Grafiken. Die [Grammatik der Grafiken](https://en.wikipedia.org/wiki/Ggplot2) ist ein allgemeines Schema für die Datenvisualisierung, das Diagramme in semantische Komponenten wie Skalen und Ebenen unterteilt. Mit anderen Worten: Die einfache Erstellung von Diagrammen und Grafiken für univariate oder multivariate Daten mit wenig Code macht `ggplot2` zum beliebtesten Paket für Visualisierungen in R. Der Benutzer gibt `ggplot2` an, wie die Variablen auf die Ästhetik abgebildet werden sollen, welche grafischen Primitive verwendet werden sollen, und `ggplot2` kümmert sich um den Rest.

> ✅ Diagramm = Daten + Ästhetik + Geometrie  
> - Daten beziehen sich auf den Datensatz  
> - Ästhetik gibt die zu untersuchenden Variablen an (x- und y-Variablen)  
> - Geometrie bezieht sich auf die Art des Diagramms (Liniendiagramm, Balkendiagramm usw.)  

Wähle die beste Geometrie (Art des Diagramms) entsprechend deinen Daten und der Geschichte, die du durch das Diagramm erzählen möchtest.

> - Um Trends zu analysieren: Linie, Säule  
> - Um Werte zu vergleichen: Balken, Säule, Kreisdiagramm, Streudiagramm  
> - Um zu zeigen, wie Teile zu einem Ganzen gehören: Kreisdiagramm  
> - Um die Verteilung von Daten zu zeigen: Streudiagramm, Balken  
> - Um Beziehungen zwischen Werten zu zeigen: Linie, Streudiagramm, Blase  

✅ Du kannst auch dieses hilfreiche [Cheatsheet](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf) für ggplot2 ansehen.

## Erstelle ein Liniendiagramm über die Flügelspannweite von Vögeln

Öffne die R-Konsole und importiere den Datensatz.  
> Hinweis: Der Datensatz befindet sich im Root dieses Repos im `/data`-Ordner.

Importiere den Datensatz und betrachte die Kopfzeile (die obersten 5 Zeilen) der Daten.

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```  
Die Kopfzeile der Daten enthält eine Mischung aus Text und Zahlen:

|      | Name                         | Wissenschaftlicher Name | Kategorie              | Ordnung      | Familie  | Gattung     | Erhaltungsstatus     | MinLänge | MaxLänge | MinKörpermasse | MaxKörpermasse | MinFlügelspannweite | MaxFlügelspannweite |
| ---: | :--------------------------- | :---------------------- | :--------------------- | :----------- | :------- | :---------- | :------------------- | --------: | --------: | -------------: | -------------: | ------------------: | ------------------: |
|    0 | Schwarzbauch-Pfeifente       | Dendrocygna autumnalis | Enten/Gänse/Wasservögel | Anseriformes | Anatidae | Dendrocygna | LC                   |        47 |        56 |           652  |          1020  |                76   |                94   |
|    1 | Fahlpfeifente                | Dendrocygna bicolor    | Enten/Gänse/Wasservögel | Anseriformes | Anatidae | Dendrocygna | LC                   |        45 |        53 |           712  |          1050  |                85   |                93   |
|    2 | Schneegans                   | Anser caerulescens     | Enten/Gänse/Wasservögel | Anseriformes | Anatidae | Anser       | LC                   |        64 |        79 |          2050  |          4050  |               135   |               165   |
|    3 | Zwerggans                    | Anser rossii           | Enten/Gänse/Wasservögel | Anseriformes | Anatidae | Anser       | LC                   |      57.3 |        64 |          1066  |          1567  |               113   |               116   |
|    4 | Blässgans                    | Anser albifrons        | Enten/Gänse/Wasservögel | Anseriformes | Anatidae | Anser       | LC                   |        64 |        81 |          1930  |          3310  |               130   |               165   |

Beginnen wir damit, einige der numerischen Daten mit einem einfachen Liniendiagramm zu plotten. Angenommen, du möchtest die maximale Flügelspannweite dieser interessanten Vögel betrachten.

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```  
Hier installierst du das `ggplot2`-Paket und importierst es dann in den Arbeitsbereich mit dem Befehl `library("ggplot2")`. Um ein Diagramm in ggplot zu erstellen, wird die Funktion `ggplot()` verwendet, und du gibst den Datensatz sowie die x- und y-Variablen als Attribute an. In diesem Fall verwenden wir die Funktion `geom_line()`, da wir ein Liniendiagramm erstellen möchten.

![MaxWingspan-lineplot](../../../../../translated_images/de/MaxWingspan-lineplot.b12169f99d26fdd263f291008dfd73c18a4ba8f3d32b1fda3d74af51a0a28616.png)

Was fällt dir sofort auf? Es scheint mindestens einen Ausreißer zu geben – das ist eine beeindruckende Flügelspannweite! Eine Flügelspannweite von über 2000 Zentimetern entspricht mehr als 20 Metern – gibt es Pterodaktylen in Minnesota? Lass uns das untersuchen.

Während du in Excel schnell sortieren könntest, um diese Ausreißer zu finden, die wahrscheinlich Tippfehler sind, setze den Visualisierungsprozess fort, indem du direkt im Diagramm arbeitest.

Füge der x-Achse Beschriftungen hinzu, um zu zeigen, um welche Vogelarten es sich handelt:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```  
Wir geben den Winkel im `theme` an und spezifizieren die x- und y-Achsenbeschriftungen in `xlab()` und `ylab()`. Der `ggtitle()` gibt dem Diagramm/Plot einen Namen.

![MaxWingspan-lineplot-improved](../../../../../translated_images/de/MaxWingspan-lineplot-improved.04b73b4d5a59552a6bc7590678899718e1f065abe9eada9ebb4148939b622fd4.png)

Selbst mit der Drehung der Beschriftungen auf 45 Grad sind es zu viele, um sie zu lesen. Versuchen wir eine andere Strategie: Beschrifte nur die Ausreißer und setze die Beschriftungen direkt ins Diagramm. Du kannst ein Streudiagramm verwenden, um mehr Platz für die Beschriftungen zu schaffen:

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```  
Was passiert hier? Du hast die Funktion `geom_point()` verwendet, um Streupunkte zu plotten. Damit hast du Beschriftungen für Vögel hinzugefügt, deren `MaxWingspan > 500` ist, und die Beschriftungen auf der x-Achse ausgeblendet, um das Diagramm zu entschlacken.

Was entdeckst du?

![MaxWingspan-scatterplot](../../../../../translated_images/de/MaxWingspan-scatterplot.60dc9e0e19d32700283558f253841fdab5104abb62bc96f7d97f9c0ee857fa8b.png)

## Filtere deine Daten

Sowohl der Weißkopfseeadler als auch der Präriefalke, obwohl wahrscheinlich sehr große Vögel, scheinen falsch beschriftet zu sein, mit einer zusätzlichen 0 in ihrer maximalen Flügelspannweite. Es ist unwahrscheinlich, dass du einem Weißkopfseeadler mit einer Flügelspannweite von 25 Metern begegnest, aber falls doch, lass es uns wissen! Lass uns einen neuen Dataframe ohne diese beiden Ausreißer erstellen:

```r
birds_filtered <- subset(birds, MaxWingspan < 500)

ggplot(data=birds_filtered, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  ylab("Wingspan (CM)") +
  xlab("Birds") +
  ggtitle("Max Wingspan in Centimeters") + 
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) +
  theme(axis.text.x=element_blank(), axis.ticks.x=element_blank())
```  
Wir haben einen neuen Dataframe `birds_filtered` erstellt und dann ein Streudiagramm geplottet. Durch das Herausfiltern von Ausreißern sind deine Daten jetzt kohärenter und verständlicher.

![MaxWingspan-scatterplot-improved](../../../../../translated_images/de/MaxWingspan-scatterplot-improved.7d0af81658c65f3e75b8fedeb2335399e31108257e48db15d875ece608272051.png)

Jetzt, da wir einen bereinigten Datensatz zumindest in Bezug auf die Flügelspannweite haben, lass uns mehr über diese Vögel herausfinden.

Während Linien- und Streudiagramme Informationen über Datenwerte und deren Verteilungen anzeigen können, möchten wir über die Werte in diesem Datensatz nachdenken. Du könntest Visualisierungen erstellen, um die folgenden Fragen zur Menge zu beantworten:

> Wie viele Kategorien von Vögeln gibt es und wie viele gibt es in jeder Kategorie?  
> Wie viele Vögel sind ausgestorben, gefährdet, selten oder häufig?  
> Wie viele gibt es von den verschiedenen Gattungen und Ordnungen in der Terminologie von Linnaeus?  
## Erkunde Balkendiagramme

Balkendiagramme sind praktisch, wenn du Gruppierungen von Daten anzeigen möchtest. Lass uns die Kategorien von Vögeln in diesem Datensatz erkunden, um zu sehen, welche am häufigsten vorkommen.  
Lass uns ein Balkendiagramm mit gefilterten Daten erstellen.

```r
install.packages("dplyr")
install.packages("tidyverse")

library(lubridate)
library(scales)
library(dplyr)
library(ggplot2)
library(tidyverse)

birds_filtered %>% group_by(Category) %>%
  summarise(n=n(),
  MinLength = mean(MinLength),
  MaxLength = mean(MaxLength),
  MinBodyMass = mean(MinBodyMass),
  MaxBodyMass = mean(MaxBodyMass),
  MinWingspan=mean(MinWingspan),
  MaxWingspan=mean(MaxWingspan)) %>% 
  gather("key", "value", - c(Category, n)) %>%
  ggplot(aes(x = Category, y = value, group = key, fill = key)) +
  geom_bar(stat = "identity") +
  scale_fill_manual(values = c("#D62728", "#FF7F0E", "#8C564B","#2CA02C", "#1F77B4", "#9467BD")) +                   
  xlab("Category")+ggtitle("Birds of Minnesota")

```  
Im folgenden Code-Snippet installieren wir die Pakete [dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8) und [lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0), um Daten zu manipulieren und zu gruppieren, um ein gestapeltes Balkendiagramm zu erstellen. Zuerst gruppierst du die Daten nach der `Category` der Vögel und fasst die Spalten `MinLength`, `MaxLength`, `MinBodyMass`, `MaxBodyMass`, `MinWingspan`, `MaxWingspan` zusammen. Anschließend erstellst du das Balkendiagramm mit dem `ggplot2`-Paket und spezifizierst die Farben für die verschiedenen Kategorien und die Beschriftungen.

![Stacked bar chart](../../../../../translated_images/de/stacked-bar-chart.0c92264e89da7b391a7490224d1e7059a020e8b74dcd354414aeac78871c02f1.png)

Dieses Balkendiagramm ist jedoch unleserlich, da es zu viele nicht gruppierte Daten gibt. Du musst nur die Daten auswählen, die du plotten möchtest. Lass uns die Länge der Vögel basierend auf ihrer Kategorie betrachten.

Filtere deine Daten, um nur die Kategorie der Vögel einzubeziehen.

Da es viele Kategorien gibt, kannst du dieses Diagramm vertikal anzeigen und seine Höhe anpassen, um alle Daten zu berücksichtigen:

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```  
Du zählst zuerst die eindeutigen Werte in der Spalte `Category` und sortierst sie in einen neuen Dataframe `birds_count`. Diese sortierten Daten werden dann auf derselben Ebene fakturiert, sodass sie in der sortierten Weise geplottet werden. Mit `ggplot2` plottest du die Daten dann in einem Balkendiagramm. Die Funktion `coord_flip()` erstellt horizontale Balken.

![category-length](../../../../../translated_images/de/category-length.7e34c296690e85d64f7e4d25a56077442683eca96c4f5b4eae120a64c0755636.png)

Dieses Balkendiagramm zeigt eine gute Ansicht der Anzahl der Vögel in jeder Kategorie. Auf einen Blick siehst du, dass die größte Anzahl von Vögeln in dieser Region in der Kategorie Enten/Gänse/Wasservögel liegt. Minnesota ist das 'Land der 10.000 Seen', daher ist das nicht überraschend!

✅ Probiere einige andere Zählungen in diesem Datensatz aus. Gibt es etwas, das dich überrascht?

## Vergleich von Daten

Du kannst verschiedene Vergleiche von gruppierten Daten erstellen, indem du neue Achsen erstellst. Probiere einen Vergleich der MaxLänge eines Vogels basierend auf seiner Kategorie:

```r
birds_grouped <- birds_filtered %>%
  group_by(Category) %>%
  summarise(
  MaxLength = max(MaxLength, na.rm = T),
  MinLength = max(MinLength, na.rm = T)
           ) %>%
  arrange(Category)
  
ggplot(birds_grouped,aes(Category,MaxLength))+geom_bar(stat="identity")+coord_flip()
```  
Wir gruppieren die `birds_filtered`-Daten nach `Category` und erstellen ein Balkendiagramm.

![comparing data](../../../../../translated_images/de/comparingdata.f486a450d61c7ca5416f27f3f55a6a4465d00df3be5e6d33936e9b07b95e2fdd.png)

Hier gibt es nichts Überraschendes: Kolibris haben die geringste MaxLänge im Vergleich zu Pelikanen oder Gänsen. Es ist gut, wenn Daten logisch Sinn ergeben!

Du kannst interessantere Visualisierungen von Balkendiagrammen erstellen, indem du Daten überlagerst. Lass uns die minimale und maximale Länge einer bestimmten Vogelkategorie überlagern:

```r
ggplot(data=birds_grouped, aes(x=Category)) +
  geom_bar(aes(y=MaxLength), stat="identity", position ="identity",  fill='blue') +
  geom_bar(aes(y=MinLength), stat="identity", position="identity", fill='orange')+
  coord_flip()
```  
![super-imposed values](../../../../../translated_images/de/superimposed-values.5363f0705a1da4167625a373a1064331ea3cb7a06a297297d0734fcc9b3819a0.png)

## 🚀 Herausforderung

Dieser Vogeldatensatz bietet eine Fülle von Informationen über verschiedene Vogelarten innerhalb eines bestimmten Ökosystems. Suche im Internet nach anderen vogelorientierten Datensätzen. Übe das Erstellen von Diagrammen und Grafiken zu diesen Vögeln, um Fakten zu entdecken, die dir vorher nicht bewusst waren.  
## [Quiz nach der Vorlesung](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## Rückblick & Selbststudium

Diese erste Lektion hat dir einige Informationen darüber gegeben, wie du `ggplot2` verwenden kannst, um Mengen zu visualisieren. Recherchiere andere Möglichkeiten, mit Datensätzen für Visualisierungen zu arbeiten. Suche nach Datensätzen, die du mit anderen Paketen wie [Lattice](https://stat.ethz.ch/R-manual/R-devel/library/lattice/html/Lattice.html) und [Plotly](https://github.com/plotly/plotly.R#readme) visualisieren könntest.

## Aufgabe  
[Linien, Streudiagramme und Balken](assignment.md)  

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.