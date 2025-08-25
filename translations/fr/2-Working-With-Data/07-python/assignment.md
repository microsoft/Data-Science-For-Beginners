<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-25T16:31:32+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "fr"
}
-->
# Devoir sur le traitement des données en Python

Dans ce devoir, nous vous demandons d'approfondir le code que nous avons commencé à développer dans nos défis. Le devoir se compose de deux parties :

## Modélisation de la propagation du COVID-19

 - [ ] Tracez des graphiques *R* pour 5-6 pays différents sur un seul graphique pour comparaison, ou utilisez plusieurs graphiques côte à côte.
 - [ ] Analysez comment le nombre de décès et de guérisons est corrélé au nombre de cas infectés.
 - [ ] Déterminez combien de temps dure typiquement une maladie en corrélant visuellement le taux d'infection et le taux de décès, et en recherchant des anomalies. Vous devrez peut-être examiner différents pays pour le découvrir.
 - [ ] Calculez le taux de mortalité et comment il évolue au fil du temps. *Vous pourriez vouloir prendre en compte la durée de la maladie en jours pour décaler une série temporelle avant de faire les calculs.*

## Analyse des articles sur le COVID-19

- [ ] Construisez une matrice de co-occurrence des différents médicaments et identifiez quels médicaments apparaissent souvent ensemble (c'est-à-dire mentionnés dans un même résumé). Vous pouvez modifier le code pour construire une matrice de co-occurrence pour les médicaments et les diagnostics.
- [ ] Visualisez cette matrice à l'aide d'une carte thermique.
- [ ] En guise de défi supplémentaire, visualisez la co-occurrence des médicaments à l'aide d'un [diagramme en cordes](https://en.wikipedia.org/wiki/Chord_diagram). [Cette bibliothèque](https://pypi.org/project/chord/) pourrait vous aider à dessiner un diagramme en cordes.
- [ ] En guise d'autre défi supplémentaire, extrayez les dosages des différents médicaments (comme **400mg** dans *prendre 400mg de chloroquine quotidiennement*) en utilisant des expressions régulières, et construisez un dataframe qui montre les différents dosages pour différents médicaments. **Note** : prenez en compte les valeurs numériques qui se trouvent à proximité textuelle du nom du médicament.

## Barème

Exemplaire | Adéquat | À améliorer
--- | --- | -- |
Toutes les tâches sont complètes, illustrées graphiquement et expliquées, incluant au moins un des deux défis supplémentaires | Plus de 5 tâches sont complètes, aucun défi supplémentaire n'est tenté, ou les résultats ne sont pas clairs | Moins de 5 (mais plus de 3) tâches sont complètes, les visualisations n'aident pas à démontrer le point

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.