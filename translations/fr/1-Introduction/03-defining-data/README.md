<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "12339119c0165da569a93ddba05f9339",
  "translation_date": "2025-09-05T12:32:04+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "fr"
}
-->
# Définir les données

|![ Sketchnote par [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Définir les données - _Sketchnote par [@nitya](https://twitter.com/nitya)_ |

Les données sont des faits, des informations, des observations et des mesures utilisées pour faire des découvertes et soutenir des décisions éclairées. Un point de données est une unité unique de données au sein d'un ensemble de données, qui est une collection de points de données. Les ensembles de données peuvent se présenter sous différents formats et structures, et sont généralement basés sur leur source ou leur origine. Par exemple, les revenus mensuels d'une entreprise pourraient être dans une feuille de calcul, tandis que les données de fréquence cardiaque horaire d'une montre connectée pourraient être au format [JSON](https://stackoverflow.com/a/383699). Il est courant que les data scientists travaillent avec différents types de données au sein d'un ensemble de données.

Cette leçon se concentre sur l'identification et la classification des données en fonction de leurs caractéristiques et de leurs sources.

## [Quiz avant la leçon](https://ff-quizzes.netlify.app/en/ds/quiz/4)

## Comment les données sont décrites

### Données brutes
Les données brutes sont des données provenant de leur source dans leur état initial et qui n'ont pas été analysées ou organisées. Pour comprendre ce qui se passe avec un ensemble de données, il doit être organisé dans un format compréhensible par les humains ainsi que par la technologie utilisée pour l'analyser davantage. La structure d'un ensemble de données décrit comment il est organisé et peut être classée comme structuré, non structuré ou semi-structuré. Ces types de structures varient en fonction de la source, mais s'inscrivent finalement dans ces trois catégories.

### Données quantitatives
Les données quantitatives sont des observations numériques au sein d'un ensemble de données et peuvent généralement être analysées, mesurées et utilisées mathématiquement. Quelques exemples de données quantitatives sont : la population d'un pays, la taille d'une personne ou les revenus trimestriels d'une entreprise. Avec une analyse supplémentaire, les données quantitatives pourraient être utilisées pour découvrir des tendances saisonnières de l'indice de qualité de l'air (AQI) ou estimer la probabilité de trafic aux heures de pointe lors d'une journée de travail typique.

### Données qualitatives
Les données qualitatives, également appelées données catégorielles, sont des données qui ne peuvent pas être mesurées objectivement comme les observations des données quantitatives. Ce sont généralement divers formats de données subjectives qui capturent la qualité de quelque chose, comme un produit ou un processus. Parfois, les données qualitatives sont numériques mais ne seraient pas utilisées mathématiquement, comme les numéros de téléphone ou les horodatages. Quelques exemples de données qualitatives sont : les commentaires vidéo, la marque et le modèle d'une voiture ou la couleur préférée de vos amis proches. Les données qualitatives pourraient être utilisées pour comprendre quels produits les consommateurs préfèrent ou pour identifier des mots-clés populaires dans les CV de candidatures.

### Données structurées
Les données structurées sont des données organisées en lignes et colonnes, où chaque ligne aura le même ensemble de colonnes. Les colonnes représentent une valeur d'un type particulier et seront identifiées par un nom décrivant ce que représente la valeur, tandis que les lignes contiennent les valeurs réelles. Les colonnes auront souvent un ensemble spécifique de règles ou de restrictions sur les valeurs, afin de garantir que les valeurs représentent correctement la colonne. Par exemple, imaginez une feuille de calcul de clients où chaque ligne doit avoir un numéro de téléphone et les numéros de téléphone ne contiennent jamais de caractères alphabétiques. Il peut y avoir des règles appliquées à la colonne des numéros de téléphone pour s'assurer qu'elle n'est jamais vide et ne contient que des chiffres.

Un avantage des données structurées est qu'elles peuvent être organisées de manière à être liées à d'autres données structurées. Cependant, comme les données sont conçues pour être organisées d'une manière spécifique, apporter des modifications à leur structure globale peut demander beaucoup d'efforts. Par exemple, ajouter une colonne d'e-mail à la feuille de calcul des clients qui ne peut pas être vide signifie que vous devrez trouver comment ajouter ces valeurs aux lignes existantes de clients dans l'ensemble de données.

Exemples de données structurées : feuilles de calcul, bases de données relationnelles, numéros de téléphone, relevés bancaires.

### Données non structurées
Les données non structurées ne peuvent généralement pas être catégorisées en lignes ou colonnes et ne contiennent pas de format ou de règles à suivre. Comme les données non structurées ont moins de restrictions sur leur structure, il est plus facile d'ajouter de nouvelles informations par rapport à un ensemble de données structuré. Si un capteur capturant des données sur la pression barométrique toutes les 2 minutes reçoit une mise à jour lui permettant désormais de mesurer et d'enregistrer la température, cela ne nécessite pas de modification des données existantes si elles sont non structurées. Cependant, cela peut rendre l'analyse ou l'examen de ce type de données plus long. Par exemple, un scientifique qui souhaite trouver la température moyenne du mois précédent à partir des données du capteur découvre que le capteur a enregistré un "e" dans certaines de ses données pour indiquer qu'il était en panne au lieu d'un nombre typique, ce qui signifie que les données sont incomplètes.

Exemples de données non structurées : fichiers texte, messages texte, fichiers vidéo.

### Données semi-structurées
Les données semi-structurées ont des caractéristiques qui en font une combinaison de données structurées et non structurées. Elles ne se conforment généralement pas à un format de lignes et colonnes, mais sont organisées d'une manière considérée comme structurée et peuvent suivre un format fixe ou un ensemble de règles. La structure varie selon les sources, allant d'une hiérarchie bien définie à quelque chose de plus flexible permettant une intégration facile de nouvelles informations. Les métadonnées sont des indicateurs qui aident à décider comment les données sont organisées et stockées et auront divers noms, en fonction du type de données. Quelques noms courants pour les métadonnées sont balises, éléments, entités et attributs. Par exemple, un message e-mail typique aura un sujet, un corps et un ensemble de destinataires et peut être organisé par qui ou quand il a été envoyé.

Exemples de données semi-structurées : HTML, fichiers CSV, JavaScript Object Notation (JSON).

## Sources de données

Une source de données est l'emplacement initial où les données ont été générées ou où elles "résident" et varie en fonction de la manière et du moment où elles ont été collectées. Les données générées par leurs utilisateurs sont appelées données primaires, tandis que les données secondaires proviennent d'une source ayant collecté des données pour un usage général. Par exemple, un groupe de scientifiques collectant des observations dans une forêt tropicale serait considéré comme primaire, et s'ils décident de les partager avec d'autres scientifiques, cela serait considéré comme secondaire pour ceux qui les utilisent.

Les bases de données sont une source courante et reposent sur un système de gestion de bases de données pour héberger et maintenir les données, où les utilisateurs utilisent des commandes appelées requêtes pour explorer les données. Les fichiers en tant que sources de données peuvent être des fichiers audio, image et vidéo ainsi que des feuilles de calcul comme Excel. Les sources Internet sont un emplacement courant pour héberger des données, où des bases de données ainsi que des fichiers peuvent être trouvés. Les interfaces de programmation d'applications, également appelées API, permettent aux programmeurs de créer des moyens de partager des données avec des utilisateurs externes via Internet, tandis que le processus de web scraping extrait des données d'une page web. Les [leçons sur le travail avec les données](../../../../../../../../../2-Working-With-Data) se concentrent sur la manière d'utiliser diverses sources de données.

## Conclusion

Dans cette leçon, nous avons appris :

- Ce que sont les données
- Comment les données sont décrites
- Comment les données sont classées et catégorisées
- Où les données peuvent être trouvées

## 🚀 Défi

Kaggle est une excellente source d'ensembles de données ouverts. Utilisez l'[outil de recherche d'ensembles de données](https://www.kaggle.com/datasets) pour trouver des ensembles de données intéressants et classifiez 3 à 5 ensembles de données selon ces critères :

- Les données sont-elles quantitatives ou qualitatives ?
- Les données sont-elles structurées, non structurées ou semi-structurées ?

## [Quiz après la leçon](https://ff-quizzes.netlify.app/en/ds/quiz/5)

## Révision et étude personnelle

- Cette unité Microsoft Learn, intitulée [Classifiez vos données](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data), propose une analyse détaillée des données structurées, semi-structurées et non structurées.

## Devoir

[Classifiez les ensembles de données](assignment.md)

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.