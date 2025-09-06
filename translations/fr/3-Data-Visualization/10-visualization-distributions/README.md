<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a20467e046d312809d008395051fc7",
  "translation_date": "2025-09-05T12:27:54+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "fr"
}
-->
# Visualiser les distributions

|![ Sketchnote par [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Visualiser les distributions - _Sketchnote par [@nitya](https://twitter.com/nitya)_ |

Dans la leçon précédente, vous avez appris des faits intéressants sur un ensemble de données concernant les oiseaux du Minnesota. Vous avez identifié des données erronées en visualisant les valeurs aberrantes et examiné les différences entre les catégories d'oiseaux en fonction de leur longueur maximale.

## [Quiz avant le cours](https://ff-quizzes.netlify.app/en/ds/quiz/18)
## Explorer l'ensemble de données sur les oiseaux

Une autre façon d'explorer les données est d'examiner leur distribution, c'est-à-dire comment elles sont organisées le long d'un axe. Par exemple, vous pourriez vouloir connaître la distribution générale, dans cet ensemble de données, de l'envergure maximale ou de la masse corporelle maximale des oiseaux du Minnesota.

Découvrons quelques faits sur les distributions des données dans cet ensemble. Dans le fichier _notebook.ipynb_ à la racine de ce dossier de leçon, importez Pandas, Matplotlib et vos données :

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | Nom                          | NomScientifique        | Catégorie             | Ordre        | Famille  | Genre       | StatutConservation | LongueurMin | LongueurMax | MasseCorporelleMin | MasseCorporelleMax | EnvergureMin | EnvergureMax |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | -----------:| -----------:| ------------------:| ------------------:| ------------:| ------------:|
|    0 | Dendrocygne à ventre noir    | Dendrocygna autumnalis | Canards/Oies/Oiseaux aquatiques | Anseriformes | Anatidae | Dendrocygna | LC                 |        47   |        56   |         652        |        1020        |          76  |          94  |
|    1 | Dendrocygne fauve            | Dendrocygna bicolor    | Canards/Oies/Oiseaux aquatiques | Anseriformes | Anatidae | Dendrocygna | LC                 |        45   |        53   |         712        |        1050        |          85  |          93  |
|    2 | Oie des neiges               | Anser caerulescens     | Canards/Oies/Oiseaux aquatiques | Anseriformes | Anatidae | Anser       | LC                 |        64   |        79   |        2050        |        4050        |         135  |         165  |
|    3 | Oie de Ross                  | Anser rossii           | Canards/Oies/Oiseaux aquatiques | Anseriformes | Anatidae | Anser       | LC                 |      57.3   |        64   |        1066        |        1567        |         113  |         116  |
|    4 | Oie rieuse                   | Anser albifrons        | Canards/Oies/Oiseaux aquatiques | Anseriformes | Anatidae | Anser       | LC                 |        64   |        81   |        1930        |        3310        |         130  |         165  |

En général, vous pouvez rapidement examiner la manière dont les données sont distribuées en utilisant un nuage de points, comme nous l'avons fait dans la leçon précédente :

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![longueur max par ordre](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

Cela donne un aperçu de la distribution générale de la longueur corporelle par ordre d'oiseaux, mais ce n'est pas la méthode optimale pour afficher de véritables distributions. Cette tâche est généralement mieux réalisée en créant un histogramme.

## Travailler avec des histogrammes

Matplotlib offre d'excellents moyens de visualiser la distribution des données à l'aide d'histogrammes. Ce type de graphique ressemble à un diagramme en barres où la distribution peut être observée à travers la montée et la descente des barres. Pour construire un histogramme, vous avez besoin de données numériques. Pour créer un histogramme, vous pouvez tracer un graphique en définissant le type comme 'hist' pour Histogramme. Ce graphique montre la distribution de la MasseCorporelleMax pour l'ensemble de données numériques. En divisant le tableau de données en plus petits intervalles (bins), il peut afficher la distribution des valeurs des données :

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![distribution sur l'ensemble du dataset](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

Comme vous pouvez le voir, la plupart des 400+ oiseaux de cet ensemble de données ont une MasseCorporelleMax inférieure à 2000. Obtenez plus d'informations sur les données en modifiant le paramètre `bins` à une valeur plus élevée, comme 30 :

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![distribution avec bins plus grands](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

Ce graphique montre la distribution de manière un peu plus détaillée. Un graphique moins biaisé vers la gauche pourrait être créé en s'assurant que vous ne sélectionnez que des données dans une plage donnée :

Filtrez vos données pour ne conserver que les oiseaux dont la masse corporelle est inférieure à 60, et affichez 40 `bins` :

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![histogramme filtré](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ Essayez d'autres filtres et points de données. Pour voir la distribution complète des données, supprimez le filtre `['MaxBodyMass']` pour afficher les distributions étiquetées.

L'histogramme offre également des améliorations intéressantes en termes de couleurs et d'étiquetage :

Créez un histogramme 2D pour comparer la relation entre deux distributions. Comparons `MaxBodyMass` et `MaxLength`. Matplotlib propose une méthode intégrée pour montrer la convergence à l'aide de couleurs plus vives :

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
Il semble y avoir une corrélation attendue entre ces deux éléments le long d'un axe attendu, avec un point de convergence particulièrement fort :

![graphique 2D](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

Les histogrammes fonctionnent bien par défaut pour les données numériques. Que faire si vous devez examiner les distributions selon des données textuelles ?
## Explorer l'ensemble de données pour les distributions basées sur des données textuelles 

Cet ensemble de données contient également des informations intéressantes sur la catégorie des oiseaux, leur genre, leur espèce, leur famille ainsi que leur statut de conservation. Explorons ces informations de conservation. Quelle est la distribution des oiseaux selon leur statut de conservation ?

> ✅ Dans l'ensemble de données, plusieurs acronymes sont utilisés pour décrire le statut de conservation. Ces acronymes proviennent des [Catégories de la Liste Rouge de l'UICN](https://www.iucnredlist.org/), une organisation qui catalogue le statut des espèces.
> 
> - CR : En danger critique d'extinction
> - EN : En danger
> - EX : Éteint
> - LC : Préoccupation mineure
> - NT : Quasi menacé
> - VU : Vulnérable

Ces valeurs sont basées sur du texte, vous devrez donc effectuer une transformation pour créer un histogramme. En utilisant le dataframe filteredBirds, affichez son statut de conservation avec son EnvergureMin. Que remarquez-vous ?

```python
x1 = filteredBirds.loc[filteredBirds.ConservationStatus=='EX', 'MinWingspan']
x2 = filteredBirds.loc[filteredBirds.ConservationStatus=='CR', 'MinWingspan']
x3 = filteredBirds.loc[filteredBirds.ConservationStatus=='EN', 'MinWingspan']
x4 = filteredBirds.loc[filteredBirds.ConservationStatus=='NT', 'MinWingspan']
x5 = filteredBirds.loc[filteredBirds.ConservationStatus=='VU', 'MinWingspan']
x6 = filteredBirds.loc[filteredBirds.ConservationStatus=='LC', 'MinWingspan']

kwargs = dict(alpha=0.5, bins=20)

plt.hist(x1, **kwargs, color='red', label='Extinct')
plt.hist(x2, **kwargs, color='orange', label='Critically Endangered')
plt.hist(x3, **kwargs, color='yellow', label='Endangered')
plt.hist(x4, **kwargs, color='green', label='Near Threatened')
plt.hist(x5, **kwargs, color='blue', label='Vulnerable')
plt.hist(x6, **kwargs, color='gray', label='Least Concern')

plt.gca().set(title='Conservation Status', ylabel='Min Wingspan')
plt.legend();
```

![collation envergure et conservation](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

Il ne semble pas y avoir de bonne corrélation entre l'envergure minimale et le statut de conservation. Testez d'autres éléments de l'ensemble de données en utilisant cette méthode. Vous pouvez également essayer différents filtres. Trouvez-vous une corrélation ?

## Graphiques de densité

Vous avez peut-être remarqué que les histogrammes que nous avons examinés jusqu'à présent sont "en escalier" et ne s'écoulent pas de manière fluide en arc. Pour afficher un graphique de densité plus fluide, vous pouvez essayer un graphique de densité.

Pour travailler avec des graphiques de densité, familiarisez-vous avec une nouvelle bibliothèque de visualisation, [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html). 

En chargeant Seaborn, essayez un graphique de densité de base :

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![Graphique de densité](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

Vous pouvez voir que le graphique reflète le précédent pour les données d'EnvergureMin ; il est simplement un peu plus fluide. Selon la documentation de Seaborn, "Par rapport à un histogramme, le KDE peut produire un graphique moins encombré et plus interprétable, surtout lorsqu'on trace plusieurs distributions. Mais il peut introduire des distorsions si la distribution sous-jacente est limitée ou non fluide. Comme un histogramme, la qualité de la représentation dépend également de la sélection de bons paramètres de lissage." [source](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) En d'autres termes, comme toujours, les valeurs aberrantes peuvent perturber vos graphiques.

Si vous vouliez revisiter cette ligne irrégulière de MasseCorporelleMax dans le deuxième graphique que vous avez construit, vous pourriez la lisser très bien en la recréant avec cette méthode :

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![ligne lissée de masse corporelle](../../../../3-Data-Visualization/10-visualization-distributions/images/density2.png)

Si vous vouliez une ligne lisse, mais pas trop lisse, modifiez le paramètre `bw_adjust` : 

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![ligne moins lissée de masse corporelle](../../../../3-Data-Visualization/10-visualization-distributions/images/density3.png)

✅ Lisez à propos des paramètres disponibles pour ce type de graphique et expérimentez !

Ce type de graphique offre des visualisations magnifiquement explicatives. Avec quelques lignes de code, par exemple, vous pouvez montrer la densité de masse corporelle maximale par ordre d'oiseaux :

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![masse corporelle par ordre](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

Vous pouvez également cartographier la densité de plusieurs variables dans un seul graphique. Testez la LongueurMax et la LongueurMin d'un oiseau par rapport à son statut de conservation :

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![densités multiples, superposées](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

Peut-être vaut-il la peine de rechercher si le regroupement des oiseaux "Vulnérables" selon leurs longueurs est significatif ou non.

## 🚀 Défi

Les histogrammes sont un type de graphique plus sophistiqué que les nuages de points, les diagrammes en barres ou les graphiques linéaires de base. Faites une recherche sur Internet pour trouver de bons exemples d'utilisation des histogrammes. Comment sont-ils utilisés, que démontrent-ils, et dans quels domaines ou champs d'étude ont-ils tendance à être utilisés ?

## [Quiz après le cours](https://ff-quizzes.netlify.app/en/ds/quiz/19)

## Révision et auto-apprentissage

Dans cette leçon, vous avez utilisé Matplotlib et commencé à travailler avec Seaborn pour afficher des graphiques plus sophistiqués. Faites des recherches sur `kdeplot` dans Seaborn, une "courbe de densité de probabilité continue dans une ou plusieurs dimensions". Lisez la [documentation](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) pour comprendre son fonctionnement.

## Devoir

[Appliquez vos compétences](assignment.md)

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.