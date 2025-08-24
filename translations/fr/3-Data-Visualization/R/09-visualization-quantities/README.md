<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22acf28f518a4769ea14fa42f4734b9f",
  "translation_date": "2025-08-24T13:53:41+00:00",
  "source_file": "3-Data-Visualization/R/09-visualization-quantities/README.md",
  "language_code": "fr"
}
-->
# Visualiser des quantités
|![ Sketchnote par [(@sketchthedocs)](https://sketchthedocs.dev) ](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Visualiser des quantités - _Sketchnote par [@nitya](https://twitter.com/nitya)_ |

Dans cette leçon, vous allez explorer comment utiliser certaines des nombreuses bibliothèques de packages R disponibles pour apprendre à créer des visualisations intéressantes autour du concept de quantité. En utilisant un ensemble de données nettoyé sur les oiseaux du Minnesota, vous pouvez découvrir de nombreux faits intéressants sur la faune locale.  
## [Quiz avant la leçon](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## Observer l'envergure des ailes avec ggplot2
Une bibliothèque excellente pour créer des graphiques et des diagrammes simples ou sophistiqués de divers types est [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html). En termes généraux, le processus de création de graphiques à l'aide de ces bibliothèques inclut l'identification des parties de votre dataframe que vous souhaitez cibler, la réalisation des transformations nécessaires sur ces données, l'attribution des valeurs des axes x et y, le choix du type de graphique à afficher, puis l'affichage du graphique.

`ggplot2` est un système pour créer des graphiques de manière déclarative, basé sur la grammaire des graphiques. La [grammaire des graphiques](https://en.wikipedia.org/wiki/Ggplot2) est un schéma général pour la visualisation des données qui divise les graphiques en composants sémantiques tels que les échelles et les couches. En d'autres termes, la facilité de création de graphiques pour des données univariées ou multivariées avec peu de code fait de `ggplot2` le package le plus populaire utilisé pour les visualisations en R. L'utilisateur indique à `ggplot2` comment mapper les variables aux esthétiques, les primitives graphiques à utiliser, et `ggplot2` s'occupe du reste.

> ✅ Graphique = Données + Esthétiques + Géométrie  
> - Les données font référence à l'ensemble de données  
> - Les esthétiques indiquent les variables à étudier (variables x et y)  
> - La géométrie fait référence au type de graphique (graphique linéaire, diagramme en barres, etc.)  

Choisissez la meilleure géométrie (type de graphique) en fonction de vos données et de l'histoire que vous souhaitez raconter à travers le graphique.  

> - Pour analyser les tendances : ligne, colonne  
> - Pour comparer des valeurs : barre, colonne, camembert, nuage de points  
> - Pour montrer comment les parties se rapportent à un tout : camembert  
> - Pour montrer la distribution des données : nuage de points, barre  
> - Pour montrer les relations entre les valeurs : ligne, nuage de points, bulle  

✅ Vous pouvez également consulter cette [cheatsheet descriptive](https://nyu-cdsc.github.io/learningr/assets/data-visualization-2.1.pdf) pour ggplot2.

## Construire un graphique linéaire sur les valeurs d'envergure des ailes des oiseaux

Ouvrez la console R et importez l'ensemble de données.  
> Note : L'ensemble de données est stocké à la racine de ce dépôt dans le dossier `/data`.

Importons l'ensemble de données et observons les premières lignes (les 5 premières lignes) des données.

```r
birds <- read.csv("../../data/birds.csv",fileEncoding="UTF-8-BOM")
head(birds)
```  
Les premières lignes des données contiennent un mélange de texte et de chiffres :

|      | Nom                          | NomScientifique        | Catégorie             | Ordre        | Famille  | Genre       | StatutConservation | LongueurMin | LongueurMax | MasseMinCorps | MasseMaxCorps | EnvergureMin | EnvergureMax |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | -----------:| -----------:| -------------:| -------------:| ------------:| ------------:|
|    0 | Dendrocygne à ventre noir    | Dendrocygna autumnalis | Canards/Oies/Oiseaux aquatiques | Anseriformes | Anatidae | Dendrocygna | LC                 |        47    |        56    |         652    |        1020    |          76   |          94   |
|    1 | Dendrocygne fauve            | Dendrocygna bicolor    | Canards/Oies/Oiseaux aquatiques | Anseriformes | Anatidae | Dendrocygna | LC                 |        45    |        53    |         712    |        1050    |          85   |          93   |
|    2 | Oie des neiges               | Anser caerulescens     | Canards/Oies/Oiseaux aquatiques | Anseriformes | Anatidae | Anser       | LC                 |        64    |        79    |        2050    |        4050    |         135   |         165   |
|    3 | Oie de Ross                  | Anser rossii           | Canards/Oies/Oiseaux aquatiques | Anseriformes | Anatidae | Anser       | LC                 |      57.3    |        64    |        1066    |        1567    |         113   |         116   |
|    4 | Oie rieuse                   | Anser albifrons        | Canards/Oies/Oiseaux aquatiques | Anseriformes | Anatidae | Anser       | LC                 |        64    |        81    |        1930    |        3310    |         130   |         165   |

Commençons par tracer certaines des données numériques à l'aide d'un graphique linéaire de base. Supposons que vous souhaitiez une vue de l'envergure maximale pour ces oiseaux intéressants.

```r
install.packages("ggplot2")
library("ggplot2")
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() 
```  
Ici, vous installez le package `ggplot2` puis l'importez dans l'espace de travail à l'aide de la commande `library("ggplot2")`. Pour tracer un graphique dans ggplot, la fonction `ggplot()` est utilisée et vous spécifiez l'ensemble de données, les variables x et y comme attributs. Dans ce cas, nous utilisons la fonction `geom_line()` car nous visons à tracer un graphique linéaire.

![MaxWingspan-lineplot](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/MaxWingspan-lineplot.png)

Que remarquez-vous immédiatement ? Il semble y avoir au moins un point aberrant - quelle envergure impressionnante ! Une envergure de plus de 2000 centimètres équivaut à plus de 20 mètres - y aurait-il des ptérodactyles qui rôdent dans le Minnesota ? Enquêtons.

Bien que vous puissiez effectuer un tri rapide dans Excel pour trouver ces points aberrants, qui sont probablement des erreurs de saisie, continuez le processus de visualisation en travaillant directement depuis le graphique.

Ajoutez des étiquettes à l'axe x pour montrer de quels types d'oiseaux il s'agit :

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_line() +
  theme(axis.text.x = element_text(angle = 45, hjust=1))+
  xlab("Birds") +
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters")
```  
Nous spécifions l'angle dans le `theme` et spécifions les étiquettes des axes x et y dans `xlab()` et `ylab()` respectivement. Le `ggtitle()` donne un nom au graphique.

![MaxWingspan-lineplot-improved](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/MaxWingspan-lineplot-improved.png)

Même avec la rotation des étiquettes réglée à 45 degrés, il y en a trop pour être lisibles. Essayons une stratégie différente : étiqueter uniquement les points aberrants et placer les étiquettes directement dans le graphique. Vous pouvez utiliser un graphique en nuage de points pour faire plus de place aux étiquettes :

```r
ggplot(data=birds, aes(x=Name, y=MaxWingspan,group=1)) +
  geom_point() +
  geom_text(aes(label=ifelse(MaxWingspan>500,as.character(Name),'')),hjust=0,vjust=0) + 
  theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank())
  ylab("Wingspan (CM)") +
  ggtitle("Max Wingspan in Centimeters") + 
```  
Que se passe-t-il ici ? Vous avez utilisé la fonction `geom_point()` pour tracer des points de dispersion. Avec cela, vous avez ajouté des étiquettes pour les oiseaux ayant une `MaxWingspan > 500` et également masqué les étiquettes sur l'axe x pour désencombrer le graphique.  

Que découvrez-vous ?

![MaxWingspan-scatterplot](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/MaxWingspan-scatterplot.png)

## Filtrer vos données

Le pygargue à tête blanche et le faucon des prairies, bien qu'étant probablement de très grands oiseaux, semblent être mal étiquetés, avec un zéro supplémentaire ajouté à leur envergure maximale. Il est peu probable que vous rencontriez un pygargue à tête blanche avec une envergure de 25 mètres, mais si c'est le cas, faites-le nous savoir ! Créons un nouveau dataframe sans ces deux points aberrants :

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
Nous avons créé un nouveau dataframe `birds_filtered` puis tracé un graphique en nuage de points. En filtrant les points aberrants, vos données sont maintenant plus cohérentes et compréhensibles.

![MaxWingspan-scatterplot-improved](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/MaxWingspan-scatterplot-improved.png)

Maintenant que nous avons un ensemble de données plus propre, du moins en termes d'envergure, découvrons-en davantage sur ces oiseaux.

Bien que les graphiques linéaires et en nuage de points puissent afficher des informations sur les valeurs des données et leur distribution, nous voulons réfléchir aux valeurs inhérentes à cet ensemble de données. Vous pourriez créer des visualisations pour répondre aux questions suivantes sur les quantités :

> Combien de catégories d'oiseaux existe-t-il, et quels sont leurs nombres ?  
> Combien d'oiseaux sont éteints, en danger, rares ou communs ?  
> Combien y a-t-il de genres et d'ordres différents selon la terminologie de Linné ?  

## Explorer les diagrammes en barres

Les diagrammes en barres sont pratiques lorsque vous devez montrer des regroupements de données. Explorons les catégories d'oiseaux présentes dans cet ensemble de données pour voir laquelle est la plus courante en nombre.  
Créons un diagramme en barres sur les données filtrées.

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
Dans l'extrait suivant, nous installons les packages [dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8) et [lubridate](https://www.rdocumentation.org/packages/lubridate/versions/1.8.0) pour aider à manipuler et regrouper les données afin de tracer un diagramme en barres empilées. Tout d'abord, vous regroupez les données par la `Category` des oiseaux, puis vous résumez les colonnes `MinLength`, `MaxLength`, `MinBodyMass`, `MaxBodyMass`, `MinWingspan`, `MaxWingspan`. Ensuite, vous tracez le diagramme en barres à l'aide du package `ggplot2` et spécifiez les couleurs pour les différentes catégories et les étiquettes.

![Stacked bar chart](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/stacked-bar-chart.png)

Ce diagramme en barres, cependant, est illisible car il y a trop de données non regroupées. Vous devez sélectionner uniquement les données que vous souhaitez tracer, alors regardons la longueur des oiseaux en fonction de leur catégorie.

Filtrez vos données pour inclure uniquement la catégorie des oiseaux.

Étant donné qu'il y a de nombreuses catégories, vous pouvez afficher ce graphique verticalement et ajuster sa hauteur pour tenir compte de toutes les données :

```r
birds_count<-dplyr::count(birds_filtered, Category, sort = TRUE)
birds_count$Category <- factor(birds_count$Category, levels = birds_count$Category)
ggplot(birds_count,aes(Category,n))+geom_bar(stat="identity")+coord_flip()
```  
Vous comptez d'abord les valeurs uniques dans la colonne `Category` puis les triez dans un nouveau dataframe `birds_count`. Ces données triées sont ensuite facturées au même niveau afin qu'elles soient tracées de manière triée. En utilisant `ggplot2`, vous tracez ensuite les données dans un diagramme en barres. Le `coord_flip()` trace des barres horizontales.

![category-length](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/category-length.png)

Ce diagramme en barres montre une bonne vue du nombre d'oiseaux dans chaque catégorie. En un clin d'œil, vous voyez que le plus grand nombre d'oiseaux dans cette région appartient à la catégorie Canards/Oies/Oiseaux aquatiques. Le Minnesota est le "pays des 10 000 lacs", donc ce n'est pas surprenant !

✅ Essayez d'autres comptages sur cet ensemble de données. Y a-t-il quelque chose qui vous surprend ?

## Comparer les données

Vous pouvez essayer différentes comparaisons de données regroupées en créant de nouveaux axes. Essayez une comparaison de la longueur maximale d'un oiseau, en fonction de sa catégorie :

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
Nous regroupons les données `birds_filtered` par `Category` puis traçons un graphique en barres.

![comparing data](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/comparingdata.png)

Rien de surprenant ici : les colibris ont la longueur maximale la plus faible par rapport aux pélicans ou aux oies. C'est bien lorsque les données ont du sens logiquement !

Vous pouvez créer des visualisations plus intéressantes de diagrammes en barres en superposant des données. Superposons la longueur minimale et maximale pour une catégorie d'oiseaux donnée :

```r
ggplot(data=birds_grouped, aes(x=Category)) +
  geom_bar(aes(y=MaxLength), stat="identity", position ="identity",  fill='blue') +
  geom_bar(aes(y=MinLength), stat="identity", position="identity", fill='orange')+
  coord_flip()
```  
![super-imposed values](../../../../../3-Data-Visualization/R/09-visualization-quantities/images/superimposed-values.png)

## 🚀 Défi

Cet ensemble de données sur les oiseaux offre une mine d'informations sur différents types d'oiseaux au sein d'un écosystème particulier. Cherchez sur Internet et voyez si vous pouvez trouver d'autres ensembles de données orientés vers les oiseaux. Entraînez-vous à créer des graphiques et des diagrammes autour de ces oiseaux pour découvrir des faits que vous ne connaissiez pas.

## [Quiz après la leçon](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## Révision et auto-apprentissage

Cette première leçon vous a donné des informations sur la façon d'utiliser `ggplot2` pour visualiser des quantités. Faites des recherches sur d'autres façons de travailler avec des ensembles de données pour la visualisation. Recherchez et explorez des ensembles de données que vous pourriez visualiser en utilisant d'autres packages comme [Lattice](https://stat.ethz.ch/R-manual/R-devel/library/lattice/html/Lattice.html) et [Plotly](https://github.com/plotly/plotly.R#readme).

## Devoir
[Graphiques linéaires, nuages de points et barres](assignment.md)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.