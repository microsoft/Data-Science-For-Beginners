<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2baeafe1db4d58ee5b8ec85db9de728a",
  "translation_date": "2025-09-05T12:23:32+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "fr"
}
-->
# Le cycle de vie de la science des données : Analyse

|![ Sketchnote par [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Cycle de vie de la science des données : Analyse - _Sketchnote par [@nitya](https://twitter.com/nitya)_ |

## Quiz avant le cours

## [Quiz avant le cours](https://ff-quizzes.netlify.app/en/ds/quiz/28)

L'analyse dans le cycle de vie des données permet de confirmer que les données peuvent répondre aux questions posées ou résoudre un problème particulier. Cette étape peut également se concentrer sur la vérification qu'un modèle répond correctement à ces questions et problèmes. Cette leçon est axée sur l'analyse exploratoire des données (ou EDA), qui regroupe des techniques permettant de définir les caractéristiques et les relations au sein des données, et qui peuvent être utilisées pour préparer les données à la modélisation.

Nous utiliserons un jeu de données d'exemple provenant de [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) pour montrer comment cela peut être appliqué avec Python et la bibliothèque Pandas. Ce jeu de données contient un décompte de certains mots courants trouvés dans des e-mails, les sources de ces e-mails étant anonymes. Utilisez le [notebook](../../../../4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) dans ce répertoire pour suivre les étapes.

## Analyse exploratoire des données

La phase de collecte du cycle de vie est celle où les données sont acquises ainsi que les problèmes et questions à traiter, mais comment savoir si les données peuvent aider à atteindre le résultat final ? 
Rappelez-vous qu'un data scientist peut poser les questions suivantes lorsqu'il acquiert des données :
- Ai-je suffisamment de données pour résoudre ce problème ?
- Les données sont-elles de qualité acceptable pour ce problème ?
- Si je découvre des informations supplémentaires grâce à ces données, devrions-nous envisager de modifier ou redéfinir les objectifs ?
L'analyse exploratoire des données est le processus qui permet de mieux connaître ces données et peut être utilisée pour répondre à ces questions, ainsi que pour identifier les défis liés à l'utilisation du jeu de données. Concentrons-nous sur certaines des techniques utilisées pour y parvenir.

## Profilage des données, statistiques descriptives et Pandas
Comment évaluer si nous avons suffisamment de données pour résoudre ce problème ? Le profilage des données peut résumer et recueillir des informations générales sur notre jeu de données grâce à des techniques de statistiques descriptives. Le profilage des données nous aide à comprendre ce qui est disponible, et les statistiques descriptives nous aident à comprendre combien de choses sont disponibles.

Dans quelques leçons précédentes, nous avons utilisé Pandas pour fournir des statistiques descriptives avec la [`fonction describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Elle fournit le décompte, les valeurs maximales et minimales, la moyenne, l'écart type et les quantiles sur les données numériques. Utiliser des statistiques descriptives comme la fonction `describe()` peut vous aider à évaluer ce que vous avez et si vous avez besoin de plus.

## Échantillonnage et requêtes
Explorer l'intégralité d'un grand jeu de données peut être très chronophage et est généralement une tâche laissée à un ordinateur. Cependant, l'échantillonnage est un outil utile pour comprendre les données et permet d'avoir une meilleure idée de ce que contient le jeu de données et de ce qu'il représente. Avec un échantillon, vous pouvez appliquer des probabilités et des statistiques pour tirer des conclusions générales sur vos données. Bien qu'il n'existe pas de règle définie sur la quantité de données à échantillonner, il est important de noter que plus vous échantillonnez de données, plus vos généralisations seront précises. 
Pandas propose la [`fonction sample()` dans sa bibliothèque](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), où vous pouvez passer un argument indiquant combien d'échantillons aléatoires vous souhaitez recevoir et utiliser.

Les requêtes générales sur les données peuvent vous aider à répondre à certaines questions et théories générales que vous pourriez avoir. Contrairement à l'échantillonnage, les requêtes vous permettent de contrôler et de vous concentrer sur des parties spécifiques des données qui vous intéressent. 
La [`fonction query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) dans la bibliothèque Pandas vous permet de sélectionner des colonnes et d'obtenir des réponses simples sur les données via les lignes récupérées.

## Exploration avec des visualisations
Vous n'avez pas besoin d'attendre que les données soient complètement nettoyées et analysées pour commencer à créer des visualisations. En fait, avoir une représentation visuelle pendant l'exploration peut aider à identifier des motifs, des relations et des problèmes dans les données. De plus, les visualisations offrent un moyen de communication avec ceux qui ne sont pas impliqués dans la gestion des données et peuvent être une opportunité de partager et clarifier des questions supplémentaires qui n'ont pas été abordées lors de la phase de collecte. Consultez la [section sur les visualisations](../../../../../../../../../3-Data-Visualization) pour en savoir plus sur certaines méthodes populaires d'exploration visuelle.

## Exploration pour identifier les incohérences
Tous les sujets abordés dans cette leçon peuvent aider à identifier les valeurs manquantes ou incohérentes, mais Pandas propose des fonctions pour vérifier certaines d'entre elles. [isna() ou isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) peuvent vérifier les valeurs manquantes. Un aspect important de l'exploration de ces valeurs dans vos données est de comprendre pourquoi elles se sont retrouvées ainsi en premier lieu. Cela peut vous aider à décider quelles [actions entreprendre pour les résoudre](../../../../../../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Quiz après le cours](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Devoir

[Explorer pour trouver des réponses](assignment.md)

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.