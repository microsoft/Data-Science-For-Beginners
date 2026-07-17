# Définir les Données

|![ Sketchnote par [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Définir les Données - _Sketchnote par [@nitya](https://twitter.com/nitya)_ |

Les données sont des faits, informations, observations et mesures utilisées pour faire des découvertes et soutenir des décisions éclairées. Un point de données est une seule unité de données dans un ensemble de données, qui est une collection de points de données. Les ensembles de données peuvent venir sous différents formats et structures, et seront généralement basés sur leur source, ou d'où proviennent les données. Par exemple, les gains mensuels d'une entreprise pourraient être dans une feuille de calcul mais les données de fréquence cardiaque horaire d'une montre connectée peuvent être en format [JSON](https://stackoverflow.com/a/383699). Il est courant que les data scientists travaillent avec différents types de données au sein d'un ensemble de données.

Cette leçon se concentre sur l'identification et la classification des données selon leurs caractéristiques et leurs sources.

## [Quiz avant la conférence](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Comment les données sont décrites

### Données Brutes
Les données brutes sont des données qui proviennent de leur source dans leur état initial et n'ont pas été analysées ou organisées. Pour comprendre ce qui se passe avec un ensemble de données, il doit être organisé dans un format compréhensible par les humains ainsi que par la technologie utilisée pour l'analyser plus avant. La structure d'un ensemble de données décrit comment il est organisé et peut être classée en structuré, non structuré et semi-structuré. Ces types de structure varient selon la source mais entrent finalement dans ces trois catégories.

### Données Quantitatives
Les données quantitatives sont des observations numériques dans un ensemble de données qui peuvent généralement être analysées, mesurées et utilisées mathématiquement. Quelques exemples de données quantitatives sont : la population d'un pays, la taille d'une personne ou les revenus trimestriels d'une entreprise. Avec une analyse supplémentaire, les données quantitatives pourraient être utilisées pour découvrir des tendances saisonnières de l'Indice de Qualité de l'Air (IQA) ou estimer la probabilité d'embouteillages aux heures de pointe un jour de travail typique.

### Données Qualitatives
Les données qualitatives, également appelées données catégorielles, sont des données qui ne peuvent pas être mesurées objectivement comme des observations de données quantitatives. Ce sont généralement divers formats de données subjectives qui capturent la qualité de quelque chose, comme un produit ou un processus. Parfois, les données qualitatives sont numériques et ne seraient pas typiquement utilisées mathématiquement, comme les numéros de téléphone ou les horodatages. Quelques exemples de données qualitatives sont : les commentaires vidéo, la marque et le modèle d'une voiture ou la couleur préférée de vos amis proches. Les données qualitatives pourraient être utilisées pour comprendre quels produits les consommateurs préfèrent ou identifier des mots-clés populaires dans des CV de candidatures.

### Données Structurées
Les données structurées sont des données organisées en lignes et colonnes, où chaque ligne a le même ensemble de colonnes. Les colonnes représentent une valeur d'un type particulier et sont identifiées par un nom décrivant ce que la valeur représente, tandis que les lignes contiennent les valeurs réelles. Les colonnes auront souvent un ensemble spécifique de règles ou de restrictions sur les valeurs, pour assurer que celles-ci représentent précisément la colonne. Par exemple, imaginez une feuille de calcul de clients où chaque ligne doit avoir un numéro de téléphone et les numéros de téléphone ne contiennent jamais de caractères alphabétiques. Il peut y avoir des règles appliquées à la colonne numéro de téléphone pour s'assurer qu'elle n'est jamais vide et ne contient que des nombres.

Un avantage des données structurées est qu'elles peuvent être organisées de manière à pouvoir être reliées à d'autres données structurées. Cependant, parce que les données sont conçues pour être organisées d'une certaine manière, modifier leur structure globale peut demander beaucoup d'efforts. Par exemple, ajouter une colonne d'emails à la feuille de calcul client qui ne peut pas être vide signifie que vous devrez trouver comment ajouter ces valeurs aux lignes déjà existantes dans l'ensemble de données.

Exemples de données structurées : feuilles de calcul, bases de données relationnelles, numéros de téléphone, relevés bancaires

### Données Non Structurées
Les données non structurées ne peuvent généralement pas être catégorisées en lignes ou colonnes et ne contiennent pas de format ou d'ensemble de règles à suivre. Parce que les données non structurées ont moins de restrictions sur leur structure, il est plus facile d'y ajouter de nouvelles informations par comparaison à un ensemble de données structuré. Si un capteur mesurant la pression barométrique toutes les 2 minutes reçoit une mise à jour qui lui permet maintenant de mesurer et enregistrer la température, il n'est pas nécessaire d'altérer les données existantes si elles sont non structurées. Cependant, cela peut rendre l'analyse ou l'investigation de ce type de données plus longue. Par exemple, un scientifique qui veut trouver la température moyenne du mois précédent à partir des données du capteur, mais découvre que le capteur a enregistré un "e" dans certaines de ses données notant qu'il était cassé au lieu d'un nombre typique, ce qui signifie que les données sont incomplètes.

Exemples de données non structurées : fichiers texte, messages texte, fichiers vidéo

### Semi-structurées
Les données semi-structurées ont des caractéristiques qui en font une combinaison de données structurées et non structurées. Elles ne se conforment généralement pas à un format de lignes et colonnes mais sont organisées d'une manière considérée comme structurée et peuvent suivre un format fixe ou un ensemble de règles. La structure variera selon les sources, comme une hiérarchie bien définie à quelque chose de plus flexible permettant une intégration facile de nouvelles informations. Les métadonnées sont des indicateurs qui aident à décider comment les données sont organisées et stockées et auront différents noms selon le type de données. Quelques noms communs pour les métadonnées sont tags, éléments, entités et attributs. Par exemple, un message email typique aura un sujet, un corps et un ensemble de destinataires et peut être organisé par qui ou quand il a été envoyé.

Exemples de données semi-structurées : HTML, fichiers CSV, JavaScript Object Notation (JSON)

## Sources de Données

Une source de données est l'emplacement initial où les données ont été générées, ou où elles "vivent", et variera selon comment et quand elles ont été collectées. Les données générées par leur(s) utilisateur(s) sont appelées données primaires tandis que les données secondaires proviennent d'une source ayant collecté des données pour un usage général. Par exemple, un groupe de scientifiques collectant des observations dans une forêt tropicale serait considéré comme primaire, et s'ils décident de les partager avec d'autres scientifiques, elles seraient alors considérées comme secondaires pour ceux qui les utilisent.

Les bases de données sont une source commune et reposent sur un système de gestion de bases de données pour héberger et maintenir les données où les utilisateurs utilisent des commandes appelées requêtes pour explorer les données. Les fichiers comme sources de données peuvent être des fichiers audio, image, et vidéo ainsi que des feuilles de calcul comme Excel. Les sources Internet sont un lieu commun pour héberger des données, où bases de données ainsi que fichiers peuvent être trouvés. Les interfaces de programmation d'applications, aussi appelées APIs, permettent aux programmeurs de créer des moyens de partager des données avec des utilisateurs externes via Internet, tandis que le processus de récupération web extrait des données d'une page web. Les [leçons sur Travailler avec les Données](../../../../../../../../../2-Working-With-Data) se concentrent sur comment utiliser diverses sources de données.

## Conclusion

Dans cette leçon, nous avons appris :

- Ce que sont les données
- Comment les données sont décrites
- Comment les données sont classifiées et catégorisées
- Où les données peuvent être trouvées

## 🚀 Défi

Kaggle est une excellente source d'ensembles de données ouverts. Utilisez l'[outil de recherche de jeux de données](https://www.kaggle.com/datasets) pour trouver des ensembles de données intéressants et classifiez 3-5 ensembles avec ces critères :

- Les données sont-elles quantitatives ou qualitatives ?
- Les données sont-elles structurées, non structurées ou semi-structurées ?

## [Quiz post-conférence](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Revue & Auto-apprentissage

- Cette unité Microsoft Learn, intitulée [Identifier les formats de données](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text) offre une analyse détaillée des données structurées, semi-structurées et non structurées.

## Devoir

[Classifying Datasets](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->