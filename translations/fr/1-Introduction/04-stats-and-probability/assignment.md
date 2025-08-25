<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01d1b493e8b51a6ebb42524f6b1bcfff",
  "translation_date": "2025-08-25T17:10:49+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/assignment.md",
  "language_code": "fr"
}
-->
# Petite étude sur le diabète

Dans cet exercice, nous travaillerons avec un petit ensemble de données de patients atteints de diabète, disponible [ici](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

|   | ÂGE | SEXE | IMC | TA | S1 | S2 | S3 | S4 | S5 | S6 | Y  |
|---|-----|------|-----|----|----|----|----|----|----|----|----|
| 0 | 59 | 2 | 32.1 | 101. | 157 | 93.2 | 38.0 | 4. | 4.8598 | 87 | 151 |
| 1 | 48 | 1 | 21.6 | 87.0 | 183 | 103.2 | 70. | 3. | 3.8918 | 69 | 75 |
| 2 | 72 | 2 | 30.5 | 93.0 | 156 | 93.6 | 41.0 | 4.0 | 4. | 85 | 141 |
| ... | ... | ... | ... | ...| ...| ...| ...| ...| ...| ...| ... |

## Instructions

* Ouvrez le [notebook de l'exercice](../../../../1-Introduction/04-stats-and-probability/assignment.ipynb) dans un environnement jupyter notebook
* Complétez toutes les tâches listées dans le notebook, à savoir :
   * [ ] Calculer les valeurs moyennes et la variance pour toutes les variables
   * [ ] Tracer des boxplots pour IMC, TA et Y en fonction du sexe
   * [ ] Quelle est la distribution des variables Âge, Sexe, IMC et Y ?
   * [ ] Tester la corrélation entre les différentes variables et la progression de la maladie (Y)
   * [ ] Tester l'hypothèse selon laquelle le degré de progression du diabète est différent entre les hommes et les femmes
   
## Barème

Exemplaire | Adéquat | À améliorer
--- | --- | -- |
Toutes les tâches requises sont complètes, illustrées graphiquement et expliquées | La plupart des tâches sont complètes, mais les explications ou les conclusions des graphiques et/ou des valeurs obtenues manquent | Seules les tâches de base, comme le calcul des moyennes/variances et les graphiques simples, sont complètes, aucune conclusion n'est tirée des données

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.