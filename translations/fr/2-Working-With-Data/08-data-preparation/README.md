<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1b560955ff39a2bcf2a049fce474a951",
  "translation_date": "2025-09-05T12:22:36+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "fr"
}
-->
# Travailler avec les données : Préparation des données

|![ Sketchnote par [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Préparation des données - _Sketchnote par [@nitya](https://twitter.com/nitya)_ |

## [Quiz avant le cours](https://ff-quizzes.netlify.app/en/ds/quiz/14)

Selon sa source, les données brutes peuvent contenir des incohérences qui posent des défis pour l'analyse et la modélisation. En d'autres termes, ces données peuvent être qualifiées de "sales" et nécessiter un nettoyage. Cette leçon se concentre sur les techniques de nettoyage et de transformation des données pour gérer les problèmes de données manquantes, inexactes ou incomplètes. Les sujets abordés dans cette leçon utiliseront Python et la bibliothèque Pandas et seront [illustrés dans le notebook](../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb) de ce répertoire.

## L'importance de nettoyer les données

- **Facilité d'utilisation et de réutilisation** : Lorsque les données sont correctement organisées et normalisées, il est plus facile de les rechercher, les utiliser et les partager avec d'autres.

- **Cohérence** : La science des données nécessite souvent de travailler avec plusieurs ensembles de données, où des ensembles provenant de différentes sources doivent être fusionnés. S'assurer que chaque ensemble de données individuel respecte une standardisation commune garantit que les données restent utiles une fois fusionnées.

- **Précision des modèles** : Des données nettoyées améliorent la précision des modèles qui en dépendent.

## Objectifs et stratégies courants de nettoyage

- **Explorer un ensemble de données** : L'exploration des données, qui est abordée dans une [leçon ultérieure](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), peut vous aider à identifier les données nécessitant un nettoyage. Observer visuellement les valeurs dans un ensemble de données peut donner une idée de ce à quoi s'attendre pour le reste ou fournir une idée des problèmes à résoudre. L'exploration peut inclure des requêtes basiques, des visualisations et des échantillonnages.

- **Formatage** : Selon la source, les données peuvent présenter des incohérences dans leur présentation. Cela peut poser des problèmes pour la recherche et la représentation des valeurs, où elles sont visibles dans l'ensemble de données mais mal représentées dans les visualisations ou les résultats de requêtes. Les problèmes courants de formatage incluent la gestion des espaces blancs, des dates et des types de données. La résolution de ces problèmes dépend souvent des utilisateurs des données. Par exemple, les normes sur la présentation des dates et des nombres peuvent varier selon les pays.

- **Doublons** : Les données ayant plusieurs occurrences peuvent produire des résultats inexacts et doivent généralement être supprimées. Cela peut se produire fréquemment lors de la fusion de plusieurs ensembles de données. Cependant, il existe des cas où les doublons contiennent des informations supplémentaires et doivent être conservés.

- **Données manquantes** : Les données manquantes peuvent entraîner des résultats biaisés ou faibles. Parfois, elles peuvent être résolues par un "rechargement" des données, en remplissant les valeurs manquantes par des calculs et du code comme Python, ou simplement en supprimant la valeur et les données correspondantes. Les raisons des données manquantes et les actions prises pour les résoudre dépendent souvent de leur origine.

## Explorer les informations des DataFrames
> **Objectif d'apprentissage** : À la fin de cette sous-section, vous devriez être à l'aise pour trouver des informations générales sur les données stockées dans les DataFrames de pandas.

Une fois vos données chargées dans pandas, elles seront probablement dans un DataFrame (voir la [leçon précédente](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) pour un aperçu détaillé). Cependant, si votre DataFrame contient 60 000 lignes et 400 colonnes, comment commencer à comprendre ce que vous avez ? Heureusement, [pandas](https://pandas.pydata.org/) offre des outils pratiques pour examiner rapidement les informations générales sur un DataFrame, ainsi que les premières et dernières lignes.

Pour explorer cette fonctionnalité, nous allons importer la bibliothèque Python scikit-learn et utiliser un ensemble de données emblématique : l'ensemble de données **Iris**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |longueur du sépale (cm)|largeur du sépale (cm)|longueur du pétale (cm)|largeur du pétale (cm)|
|----------------------------------------|-----------------------|----------------------|-----------------------|----------------------|
|0                                       |5.1                    |3.5                   |1.4                    |0.2                   |
|1                                       |4.9                    |3.0                   |1.4                    |0.2                   |
|2                                       |4.7                    |3.2                   |1.3                    |0.2                   |
|3                                       |4.6                    |3.1                   |1.5                    |0.2                   |
|4                                       |5.0                    |3.6                   |1.4                    |0.2                   |

- **DataFrame.info** : Pour commencer, la méthode `info()` est utilisée pour afficher un résumé du contenu présent dans un `DataFrame`. Jetons un coup d'œil à cet ensemble de données pour voir ce que nous avons :
```python
iris_df.info()
```
```
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
dtypes: float64(4)
memory usage: 4.8 KB
```
D'après cela, nous savons que l'ensemble de données *Iris* contient 150 entrées réparties sur quatre colonnes sans valeurs nulles. Toutes les données sont stockées sous forme de nombres à virgule flottante 64 bits.

- **DataFrame.head()** : Ensuite, pour vérifier le contenu réel du `DataFrame`, nous utilisons la méthode `head()`. Voyons à quoi ressemblent les premières lignes de notre `iris_df` :
```python
iris_df.head()
```
```
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
```
- **DataFrame.tail()** : À l'inverse, pour vérifier les dernières lignes du `DataFrame`, nous utilisons la méthode `tail()` :
```python
iris_df.tail()
```
```
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
145                6.7               3.0                5.2               2.3
146                6.3               2.5                5.0               1.9
147                6.5               3.0                5.2               2.0
148                6.2               3.4                5.4               2.3
149                5.9               3.0                5.1               1.8
```
> **À retenir** : En examinant simplement les métadonnées sur les informations d'un DataFrame ou les premières et dernières valeurs, vous pouvez obtenir une idée immédiate de la taille, de la forme et du contenu des données avec lesquelles vous travaillez.

## Gérer les données manquantes
> **Objectif d'apprentissage** : À la fin de cette sous-section, vous devriez savoir comment remplacer ou supprimer les valeurs nulles des DataFrames.

La plupart du temps, les ensembles de données que vous souhaitez utiliser (ou devez utiliser) contiennent des valeurs manquantes. La manière dont les données manquantes sont gérées implique des compromis subtils qui peuvent affecter votre analyse finale et les résultats réels.

Pandas gère les valeurs manquantes de deux manières. La première, que vous avez déjà vue dans les sections précédentes, est `NaN`, ou Not a Number. Il s'agit d'une valeur spéciale faisant partie de la spécification IEEE pour les nombres à virgule flottante et utilisée uniquement pour indiquer des valeurs manquantes de type flottant.

Pour les valeurs manquantes autres que les flottants, pandas utilise l'objet Python `None`. Bien que cela puisse sembler déroutant d'avoir deux types de valeurs indiquant essentiellement la même chose, il existe des raisons programmatiques solides pour ce choix de conception. En pratique, cela permet à pandas de proposer un compromis efficace dans la grande majorité des cas. Cependant, `None` et `NaN` ont des restrictions qu'il est important de connaître concernant leur utilisation.

Découvrez-en davantage sur `NaN` et `None` dans le [notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) !

- **Détecter les valeurs nulles** : Dans `pandas`, les méthodes `isnull()` et `notnull()` sont vos principales méthodes pour détecter les données nulles. Les deux renvoient des masques booléens sur vos données. Nous utiliserons `numpy` pour les valeurs `NaN` :
```python
import numpy as np

example1 = pd.Series([0, np.nan, '', None])
example1.isnull()
```
```
0    False
1     True
2    False
3     True
dtype: bool
```
Regardez attentivement la sortie. Y a-t-il quelque chose qui vous surprend ? Bien que `0` soit un nul arithmétique, il reste néanmoins un entier valide et pandas le traite comme tel. `''` est un peu plus subtil. Bien que nous l'ayons utilisé dans la Section 1 pour représenter une chaîne vide, il reste un objet chaîne et non une représentation de null pour pandas.

Maintenant, retournons cela et utilisons ces méthodes de manière plus proche de leur utilisation pratique. Vous pouvez utiliser des masques booléens directement comme index de ``Series`` ou ``DataFrame``, ce qui peut être utile pour travailler avec des valeurs manquantes (ou présentes) isolées.

> **À retenir** : Les méthodes `isnull()` et `notnull()` produisent des résultats similaires lorsqu'elles sont utilisées dans des `DataFrame`s : elles montrent les résultats et l'index de ces résultats, ce qui vous aidera énormément à gérer vos données.

- **Supprimer les valeurs nulles** : Au-delà de l'identification des valeurs manquantes, pandas offre un moyen pratique de supprimer les valeurs nulles des `Series` et `DataFrame`s. (En particulier pour les grands ensembles de données, il est souvent plus conseillé de simplement supprimer les valeurs manquantes [NA] de votre analyse plutôt que de les traiter autrement.) Pour voir cela en action, revenons à `example1` :
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Notez que cela devrait ressembler à votre sortie de `example3[example3.notnull()]`. La différence ici est que, plutôt que de simplement indexer les valeurs masquées, `dropna` a supprimé ces valeurs manquantes de la `Series` `example1`.

Étant donné que les `DataFrame`s ont deux dimensions, ils offrent plus d'options pour supprimer des données.

```python
example2 = pd.DataFrame([[1,      np.nan, 7], 
                         [2,      5,      8], 
                         [np.nan, 6,      9]])
example2
```
|      | 0 | 1 | 2 |
|------|---|---|---|
|0     |1.0|NaN|7  |
|1     |2.0|5.0|8  |
|2     |NaN|6.0|9  |

(Avez-vous remarqué que pandas a converti deux des colonnes en flottants pour accueillir les `NaN` ?)

Vous ne pouvez pas supprimer une seule valeur d'un `DataFrame`, vous devez donc supprimer des lignes ou des colonnes entières. Selon ce que vous faites, vous pourriez vouloir faire l'un ou l'autre, et pandas vous offre des options pour les deux. En science des données, les colonnes représentent généralement des variables et les lignes des observations, vous êtes donc plus susceptible de supprimer des lignes de données ; le paramètre par défaut de `dropna()` est de supprimer toutes les lignes contenant des valeurs nulles :

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Si nécessaire, vous pouvez supprimer les valeurs NA des colonnes. Utilisez `axis=1` pour le faire :
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Notez que cela peut supprimer beaucoup de données que vous pourriez vouloir conserver, en particulier dans les petits ensembles de données. Que faire si vous souhaitez uniquement supprimer les lignes ou colonnes contenant plusieurs ou même toutes les valeurs nulles ? Vous spécifiez ces paramètres dans `dropna` avec les paramètres `how` et `thresh`.

Par défaut, `how='any'` (si vous souhaitez vérifier par vous-même ou voir quels autres paramètres la méthode possède, exécutez `example4.dropna?` dans une cellule de code). Vous pourriez alternativement spécifier `how='all'` pour ne supprimer que les lignes ou colonnes contenant toutes des valeurs nulles. Étendons notre exemple de `DataFrame` pour voir cela en action.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

Le paramètre `thresh` vous donne un contrôle plus précis : vous définissez le nombre de valeurs *non nulles* qu'une ligne ou colonne doit avoir pour être conservée :
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Ici, la première et la dernière ligne ont été supprimées, car elles contiennent seulement deux valeurs non nulles.

- **Remplir les valeurs nulles** : Selon votre ensemble de données, il peut parfois être plus logique de remplir les valeurs nulles avec des valeurs valides plutôt que de les supprimer. Vous pourriez utiliser `isnull` pour le faire directement, mais cela peut être laborieux, en particulier si vous avez beaucoup de valeurs à remplir. Étant donné que cette tâche est courante en science des données, pandas propose `fillna`, qui renvoie une copie de la `Series` ou du `DataFrame` avec les valeurs manquantes remplacées par celles de votre choix. Créons une autre `Series` pour voir comment cela fonctionne en pratique.
```python
example3 = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
example3
```
```
a    1.0
b    NaN
c    2.0
d    NaN
e    3.0
dtype: float64
```
Vous pouvez remplir toutes les entrées nulles avec une seule valeur, comme `0` :
```python
example3.fillna(0)
```
```
a    1.0
b    0.0
c    2.0
d    0.0
e    3.0
dtype: float64
```
Vous pouvez **propager vers l'avant** les valeurs nulles, c'est-à-dire utiliser la dernière valeur valide pour remplir une valeur nulle :
```python
example3.fillna(method='ffill')
```
```
a    1.0
b    1.0
c    2.0
d    2.0
e    3.0
dtype: float64
```
Vous pouvez également **propager vers l'arrière** pour utiliser la prochaine valeur valide pour remplir une valeur nulle :
```python
example3.fillna(method='bfill')
```
```
a    1.0
b    2.0
c    2.0
d    3.0
e    3.0
dtype: float64
```
Comme vous pouvez le deviner, cela fonctionne de la même manière avec les `DataFrame`s, mais vous pouvez également spécifier un `axis` le long duquel remplir les valeurs nulles. En reprenant `example2` utilisé précédemment :
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Notez que lorsqu'une valeur précédente n'est pas disponible pour la propagation vers l'avant, la valeur nulle reste.
> **À retenir :** Il existe plusieurs façons de gérer les valeurs manquantes dans vos ensembles de données. La stratégie spécifique que vous choisissez (les supprimer, les remplacer, ou même la manière dont vous les remplacez) doit être dictée par les particularités de ces données. Vous développerez une meilleure intuition pour traiter les valeurs manquantes à mesure que vous manipulerez et interagirez avec des ensembles de données.
## Suppression des données dupliquées

> **Objectif d'apprentissage :** À la fin de cette sous-section, vous devriez être à l'aise pour identifier et supprimer les valeurs dupliquées dans les DataFrames.

En plus des données manquantes, vous rencontrerez souvent des données dupliquées dans les ensembles de données du monde réel. Heureusement, `pandas` offre un moyen simple de détecter et de supprimer les entrées en double.

- **Identifier les doublons : `duplicated`** : Vous pouvez facilement repérer les valeurs dupliquées en utilisant la méthode `duplicated` de pandas, qui renvoie un masque booléen indiquant si une entrée dans un `DataFrame` est un doublon d'une entrée précédente. Créons un autre exemple de `DataFrame` pour voir cela en action.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |lettres|nombres|
|------|-------|-------|
|0     |A      |1      |
|1     |B      |2      |
|2     |A      |1      |
|3     |B      |3      |
|4     |B      |3      |

```python
example4.duplicated()
```
```
0    False
1    False
2     True
3    False
4     True
dtype: bool
```
- **Supprimer les doublons : `drop_duplicates` :** renvoie simplement une copie des données pour lesquelles toutes les valeurs `duplicated` sont `False` :
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Les méthodes `duplicated` et `drop_duplicates` considèrent par défaut toutes les colonnes, mais vous pouvez spécifier qu'elles examinent uniquement un sous-ensemble de colonnes dans votre `DataFrame` :
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **À retenir :** Supprimer les données dupliquées est une étape essentielle dans presque tous les projets de science des données. Les données dupliquées peuvent fausser les résultats de vos analyses et produire des résultats inexacts !


## 🚀 Défi

Tous les matériaux abordés sont disponibles sous forme de [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). De plus, des exercices sont proposés après chaque section, essayez-les !

## [Quiz post-cours](https://ff-quizzes.netlify.app/en/ds/quiz/15)



## Révision et auto-apprentissage

Il existe de nombreuses façons de découvrir et d'aborder la préparation de vos données pour l'analyse et la modélisation, et le nettoyage des données est une étape importante qui nécessite une expérience pratique. Essayez ces défis sur Kaggle pour explorer des techniques qui n'ont pas été couvertes dans cette leçon.

- [Défi de nettoyage des données : Analyse des dates](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Défi de nettoyage des données : Mise à l'échelle et normalisation des données](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Devoir

[Évaluation des données d'un formulaire](assignment.md)

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.