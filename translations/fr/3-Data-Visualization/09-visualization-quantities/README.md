<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43c402d9d90ae6da55d004519ada5033",
  "translation_date": "2025-08-25T18:36:37+00:00",
  "source_file": "3-Data-Visualization/09-visualization-quantities/README.md",
  "language_code": "fr"
}
-->
# Visualiser les quantités

|![ Sketchnote par [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Visualiser les quantités - _Sketchnote par [@nitya](https://twitter.com/nitya)_ |

Dans cette leçon, vous allez explorer comment utiliser l'une des nombreuses bibliothèques Python disponibles pour apprendre à créer des visualisations intéressantes autour du concept de quantité. En utilisant un jeu de données nettoyé sur les oiseaux du Minnesota, vous pouvez découvrir de nombreux faits intéressants sur la faune locale.  
## [Quiz pré-lecture](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/16)

## Observer l'envergure des ailes avec Matplotlib

Une excellente bibliothèque pour créer des graphiques simples ou sophistiqués de divers types est [Matplotlib](https://matplotlib.org/stable/index.html). En termes généraux, le processus de création de graphiques à l'aide de ces bibliothèques comprend l'identification des parties de votre dataframe que vous souhaitez cibler, la réalisation des transformations nécessaires sur ces données, l'attribution des valeurs des axes x et y, le choix du type de graphique à afficher, puis l'affichage du graphique. Matplotlib offre une grande variété de visualisations, mais pour cette leçon, concentrons-nous sur celles les plus appropriées pour visualiser des quantités : les graphiques linéaires, les nuages de points et les diagrammes en barres.

> ✅ Utilisez le meilleur graphique en fonction de la structure de vos données et de l'histoire que vous voulez raconter.  
> - Pour analyser les tendances au fil du temps : linéaire  
> - Pour comparer des valeurs : barres, colonnes, camembert, nuage de points  
> - Pour montrer comment les parties se rapportent à un tout : camembert  
> - Pour montrer la distribution des données : nuage de points, barres  
> - Pour montrer les tendances : linéaire, colonnes  
> - Pour montrer les relations entre les valeurs : linéaire, nuage de points, bulles  

Si vous avez un jeu de données et que vous devez découvrir combien d'un certain élément est inclus, l'une des premières tâches consistera à inspecter ses valeurs.  

✅ Il existe d'excellents 'cheat sheets' pour Matplotlib [ici](https://matplotlib.org/cheatsheets/cheatsheets.pdf).

## Construire un graphique linéaire sur les valeurs d'envergure des ailes des oiseaux

Ouvrez le fichier `notebook.ipynb` à la racine de ce dossier de leçon et ajoutez une cellule.

> Note : les données sont stockées à la racine de ce dépôt dans le dossier `/data`.

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```  
Ces données sont un mélange de texte et de chiffres :  

|      | Nom                          | NomScientifique        | Catégorie             | Ordre        | Famille  | Genre       | StatutConservation | LongueurMin | LongueurMax | MasseMin | MasseMax | EnvergureMin | EnvergureMax |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | -----------:| -----------:| --------:| --------:| ------------:| ------------:|
|    0 | Dendrocygne à ventre noir    | Dendrocygna autumnalis | Canards/Oies/Oiseaux d'eau | Anseriformes | Anatidae | Dendrocygna | LC                 |        47    |        56    |       652 |      1020 |           76 |           94 |
|    1 | Dendrocygne fauve            | Dendrocygna bicolor    | Canards/Oies/Oiseaux d'eau | Anseriformes | Anatidae | Dendrocygna | LC                 |        45    |        53    |       712 |      1050 |           85 |           93 |
|    2 | Oie des neiges               | Anser caerulescens     | Canards/Oies/Oiseaux d'eau | Anseriformes | Anatidae | Anser       | LC                 |        64    |        79    |      2050 |      4050 |          135 |          165 |
|    3 | Oie de Ross                  | Anser rossii           | Canards/Oies/Oiseaux d'eau | Anseriformes | Anatidae | Anser       | LC                 |      57.3    |        64    |      1066 |      1567 |          113 |          116 |
|    4 | Oie rieuse                   | Anser albifrons        | Canards/Oies/Oiseaux d'eau | Anseriformes | Anatidae | Anser       | LC                 |        64    |        81    |      1930 |      3310 |          130 |          165 |

Commençons par tracer certaines des données numériques à l'aide d'un graphique linéaire de base. Supposons que vous vouliez une vue de l'envergure maximale de ces oiseaux intéressants.

```python
wingspan = birds['MaxWingspan'] 
wingspan.plot()
```  
![Envergure Max](../../../../translated_images/max-wingspan-02.e79fd847b2640b89e21e340a3a9f4c5d4b224c4fcd65f54385e84f1c9ed26d52.fr.png)

Que remarquez-vous immédiatement ? Il semble y avoir au moins une valeur aberrante - quelle envergure impressionnante ! Une envergure de 2300 centimètres équivaut à 23 mètres - y a-t-il des ptérodactyles qui rôdent dans le Minnesota ? Enquêtons.

Bien que vous puissiez effectuer un tri rapide dans Excel pour trouver ces valeurs aberrantes, qui sont probablement des erreurs de saisie, continuez le processus de visualisation en travaillant directement à partir du graphique.

Ajoutez des étiquettes à l'axe des x pour montrer de quels oiseaux il s'agit :

```
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.xticks(rotation=45)
x = birds['Name'] 
y = birds['MaxWingspan']

plt.plot(x, y)

plt.show()
```  
![envergure avec étiquettes](../../../../translated_images/max-wingspan-labels-02.aa90e826ca49a9d1dde78075e9755c1849ef56a4e9ec60f7e9f3806daf9283e2.fr.png)

Même avec une rotation des étiquettes réglée à 45 degrés, il y en a trop pour être lisibles. Essayons une autre stratégie : étiqueter uniquement les valeurs aberrantes et placer les étiquettes dans le graphique. Vous pouvez utiliser un nuage de points pour faire plus de place aux étiquettes :

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)

for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    plt.plot(x, y, 'bo')
    if birds['MaxWingspan'][i] > 500:
        plt.text(x, y * (1 - 0.05), birds['Name'][i], fontsize=12)
    
plt.show()
```  
Que se passe-t-il ici ? Vous avez utilisé `tick_params` pour masquer les étiquettes du bas, puis créé une boucle sur votre jeu de données d'oiseaux. En traçant le graphique avec de petits points bleus ronds en utilisant `bo`, vous avez vérifié si un oiseau avait une envergure maximale supérieure à 500 et affiché son étiquette à côté du point si c'était le cas. Vous avez décalé légèrement les étiquettes sur l'axe y (`y * (1 - 0.05)`) et utilisé le nom de l'oiseau comme étiquette.

Qu'avez-vous découvert ?

![valeurs aberrantes](../../../../translated_images/labeled-wingspan-02.6110e2d2401cd5238ccc24dfb6d04a6c19436101f6cec151e3992e719f9f1e1f.fr.png)  
## Filtrer vos données

L'Aigle chauve et le Faucon des prairies, bien que probablement très grands, semblent être mal étiquetés, avec un `0` supplémentaire ajouté à leur envergure maximale. Il est peu probable que vous rencontriez un Aigle chauve avec une envergure de 25 mètres, mais si c'est le cas, faites-le nous savoir ! Créons un nouveau dataframe sans ces deux valeurs aberrantes :

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)
for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    if birds['Name'][i] not in ['Bald eagle', 'Prairie falcon']:
        plt.plot(x, y, 'bo')
plt.show()
```  

En filtrant les valeurs aberrantes, vos données sont maintenant plus cohérentes et compréhensibles.

![nuage de points des envergures](../../../../translated_images/scatterplot-wingspan-02.1c33790094ce36a75f5fb45b25ed2cf27f0356ea609e43c11e97a2cedd7011a4.fr.png)

Maintenant que nous avons un jeu de données plus propre, du moins en termes d'envergure, découvrons-en davantage sur ces oiseaux.

Bien que les graphiques linéaires et les nuages de points puissent afficher des informations sur les valeurs des données et leur distribution, nous voulons réfléchir aux valeurs inhérentes à ce jeu de données. Vous pourriez créer des visualisations pour répondre aux questions suivantes sur les quantités :

> Combien de catégories d'oiseaux y a-t-il, et quels sont leurs effectifs ?  
> Combien d'oiseaux sont éteints, en danger, rares ou communs ?  
> Combien y a-t-il de genres et d'ordres différents selon la terminologie de Linné ?  
## Explorer les diagrammes en barres

Les diagrammes en barres sont pratiques lorsque vous devez montrer des regroupements de données. Explorons les catégories d'oiseaux présentes dans ce jeu de données pour voir laquelle est la plus courante en nombre.

Dans le fichier notebook, créez un diagramme en barres de base.

✅ Notez que vous pouvez soit filtrer les deux oiseaux aberrants identifiés dans la section précédente, soit corriger l'erreur dans leur envergure, soit les laisser pour ces exercices qui ne dépendent pas des valeurs d'envergure.

Si vous voulez créer un diagramme en barres, vous pouvez sélectionner les données sur lesquelles vous voulez vous concentrer. Les diagrammes en barres peuvent être créés à partir de données brutes :

```python
birds.plot(x='Category',
        kind='bar',
        stacked=True,
        title='Birds of Minnesota')

```  
![données complètes en diagramme en barres](../../../../translated_images/full-data-bar-02.aaa3fda71c63ed564b917841a1886c177dd9a26424142e510c0c0498fd6ca160.fr.png)

Ce diagramme en barres, cependant, est illisible car il y a trop de données non regroupées. Vous devez sélectionner uniquement les données que vous souhaitez tracer, alors regardons la longueur des oiseaux en fonction de leur catégorie.  

Filtrez vos données pour inclure uniquement la catégorie des oiseaux.  

✅ Remarquez que vous utilisez Pandas pour gérer les données, puis laissez Matplotlib faire le tracé.

Comme il y a de nombreuses catégories, vous pouvez afficher ce graphique verticalement et ajuster sa hauteur pour tenir compte de toutes les données :

```python
category_count = birds.value_counts(birds['Category'].values, sort=True)
plt.rcParams['figure.figsize'] = [6, 12]
category_count.plot.barh()
```  
![catégorie et longueur](../../../../translated_images/category-counts-02.0b9a0a4de42275ae5096d0f8da590d8bf520d9e7e40aad5cc4fc8d276480cc32.fr.png)

Ce diagramme en barres montre une bonne vue du nombre d'oiseaux dans chaque catégorie. En un clin d'œil, vous voyez que le plus grand nombre d'oiseaux dans cette région appartient à la catégorie Canards/Oies/Oiseaux d'eau. Le Minnesota est le "pays des 10 000 lacs", donc cela n'est pas surprenant !

✅ Essayez d'autres décomptes sur ce jeu de données. Quelque chose vous surprend-il ?

## Comparer les données

Vous pouvez essayer différentes comparaisons de données regroupées en créant de nouveaux axes. Essayez une comparaison de la LongueurMax d'un oiseau, en fonction de sa catégorie :

```python
maxlength = birds['MaxLength']
plt.barh(y=birds['Category'], width=maxlength)
plt.rcParams['figure.figsize'] = [6, 12]
plt.show()
```  
![comparer les données](../../../../translated_images/category-length-02.7304bf519375c9807d8165cc7ec60dd2a60f7b365b23098538e287d89adb7d76.fr.png)

Rien de surprenant ici : les colibris ont la LongueurMax la plus faible comparée aux pélicans ou aux oies. C'est bien lorsque les données ont du sens logiquement !

Vous pouvez créer des visualisations plus intéressantes de diagrammes en barres en superposant des données. Superposons la LongueurMin et la LongueurMax pour une catégorie d'oiseaux donnée :

```python
minLength = birds['MinLength']
maxLength = birds['MaxLength']
category = birds['Category']

plt.barh(category, maxLength)
plt.barh(category, minLength)

plt.show()
```  
Dans ce graphique, vous pouvez voir l'étendue par catégorie d'oiseaux de la LongueurMin et de la LongueurMax. Vous pouvez affirmer sans risque que, selon ces données, plus l'oiseau est grand, plus son étendue de longueur est importante. Fascinant !

![valeurs superposées](../../../../translated_images/superimposed-02.f03058536baeb2ed7864f01102538464d4c2fd7ade881ddd7d5ba74dc5d2fdae.fr.png)

## 🚀 Défi

Ce jeu de données sur les oiseaux offre une mine d'informations sur différents types d'oiseaux dans un écosystème particulier. Cherchez sur Internet pour voir si vous pouvez trouver d'autres jeux de données orientés sur les oiseaux. Entraînez-vous à créer des graphiques et des diagrammes autour de ces oiseaux pour découvrir des faits que vous ne soupçonniez pas.  
## [Quiz post-lecture](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/17)

## Révision & Auto-apprentissage

Cette première leçon vous a donné des informations sur l'utilisation de Matplotlib pour visualiser des quantités. Faites des recherches sur d'autres façons de travailler avec des jeux de données pour la visualisation. [Plotly](https://github.com/plotly/plotly.py) est une bibliothèque que nous ne couvrirons pas dans ces leçons, alors jetez un œil à ce qu'elle peut offrir.  
## Devoir

[Graphiques linéaires, nuages de points et barres](assignment.md)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.