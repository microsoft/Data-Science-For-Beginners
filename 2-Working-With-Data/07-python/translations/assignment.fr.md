# Tâche: Traitement Des Données en Python

Dans cette tâche, développez le code que nous avons commencé dans nos défis. La tâche a deux sections:

## Modélisation de la Propagation de COVID-19 

 - [ ] Placez les graphiques $R_t$ de 5-6 pays sur une graphe à comparer, ou mettez plusieurs graphiques côte à côte
 - [ ] Voiez comment les nombres des morts et guérisons sont liés aux nombres des infectés
 - [ ] Trouvez combien de temps une maladie typique dure en mettre en corrélation le taux de l'infection avex le taux du décès et cherchez les anomalies. Peut-être vous avez besoin de regarder les pays différents à le trouver. 
 - [ ] Calculez le taux du décès et comment il change au fil du temps. *Il se peut que vous voulez prendre en compte la durée de la maladie en jours alors que vous pouvez déplacer une série chronologique avant de faire les calculs*

## Analyse des Articles COVID-19 

- [ ] Build co-occurrence matrix of different medications, and see which medications often occur together (i.e. mentioned in one abstract). You can modify the code for building co-occurrence matrix for medications and diagnoses.
- [ ] Visualize this matrix using heatmap.
- [ ] As a stretch goal, visualize the co-occurrence of medications using [chord diagram](https://en.wikipedia.org/wiki/Chord_diagram). [This library](https://pypi.org/project/chord/) may help you draw a chord diagram.
- [ ] As another stretch goal, extract dosages of different medications (such as **400mg** in *take 400mg of chloroquine daily*) using regular expressions, and build dataframe that shows different dosages for different medications. **Note**: consider numeric values that are in close textual vicinity of the medicine name.

## Rubric

Exemplaire | Acceptable | A Besoin D’amélioration
--- | --- | -- |
Chaque tâche est complet, illustré, et expliqué, y compris au moins un des deux objectifs | Plus que 5 tâches sont complets, aucun des objectifs sont essayés, ou les résultats ne sont pas évidents | Moins que 5 (mais plus que 3) tâches sont complets, les illustrations n'expliquent pas l'objectif
