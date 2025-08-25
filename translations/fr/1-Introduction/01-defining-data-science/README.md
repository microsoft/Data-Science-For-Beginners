<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2583a9894af7123b2fcae3376b14c035",
  "translation_date": "2025-08-25T16:53:33+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "fr"
}
-->
## Types de données

Comme nous l'avons déjà mentionné, les données sont partout. Il suffit de les capturer de la bonne manière ! Il est utile de distinguer entre les données **structurées** et **non structurées**. Les premières sont généralement représentées sous une forme bien organisée, souvent sous forme de tableau ou de plusieurs tableaux, tandis que les secondes ne sont qu'une collection de fichiers. Parfois, on peut également parler de données **semi-structurées**, qui possèdent une certaine structure pouvant varier considérablement.

| Structurées                                                                  | Semi-structurées                                                                               | Non structurées                         |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------- |
| Liste de personnes avec leurs numéros de téléphone                          | Pages Wikipédia avec des liens                                                                | Texte de l'Encyclopédie Britannica      |
| Température dans toutes les pièces d'un bâtiment chaque minute pendant 20 ans | Collection d'articles scientifiques au format JSON avec auteurs, date de publication et résumé | Partage de fichiers avec des documents d'entreprise |
| Données sur l'âge et le sexe de toutes les personnes entrant dans le bâtiment | Pages Internet                                                                                | Flux vidéo brut d'une caméra de surveillance |

## Où trouver des données

Il existe de nombreuses sources possibles de données, et il serait impossible de toutes les énumérer ! Cependant, mentionnons quelques endroits typiques où vous pouvez obtenir des données :

* **Structurées**
  - **Internet des objets** (IoT), y compris les données provenant de différents capteurs, tels que les capteurs de température ou de pression, fournit de nombreuses données utiles. Par exemple, si un bâtiment de bureaux est équipé de capteurs IoT, nous pouvons contrôler automatiquement le chauffage et l'éclairage afin de minimiser les coûts.
  - **Enquêtes** que nous demandons aux utilisateurs de remplir après un achat ou après avoir visité un site web.
  - **Analyse du comportement** peut, par exemple, nous aider à comprendre jusqu'où un utilisateur explore un site et quelle est la raison typique de son départ.
* **Non structurées**
  - **Textes** peuvent être une source riche d'informations, comme un score global de **sentiment**, ou l'extraction de mots-clés et de significations sémantiques.
  - **Images** ou **vidéos**. Une vidéo d'une caméra de surveillance peut être utilisée pour estimer le trafic sur la route et informer les gens des éventuels embouteillages.
  - Les **journaux** des serveurs web peuvent être utilisés pour comprendre quelles pages de notre site sont les plus souvent visitées et pendant combien de temps.
* **Semi-structurées**
  - Les graphes des **réseaux sociaux** peuvent être d'excellentes sources de données sur les personnalités des utilisateurs et leur potentiel à diffuser des informations.
  - Lorsque nous avons une série de photographies d'une fête, nous pouvons essayer d'extraire des données sur la **dynamique de groupe** en construisant un graphe des personnes prenant des photos ensemble.

En connaissant les différentes sources possibles de données, vous pouvez réfléchir à divers scénarios où les techniques de science des données peuvent être appliquées pour mieux comprendre la situation et améliorer les processus commerciaux.

## Ce que vous pouvez faire avec les données

En science des données, nous nous concentrons sur les étapes suivantes du parcours des données :

Bien sûr, selon les données réelles, certaines étapes peuvent être absentes (par exemple, lorsque nous avons déjà les données dans une base de données ou lorsque nous n'avons pas besoin d'entraîner un modèle), ou certaines étapes peuvent être répétées plusieurs fois (comme le traitement des données).

## Numérisation et transformation numérique

Au cours de la dernière décennie, de nombreuses entreprises ont commencé à comprendre l'importance des données dans la prise de décisions commerciales. Pour appliquer les principes de la science des données à la gestion d'une entreprise, il faut d'abord collecter des données, c'est-à-dire traduire les processus commerciaux en forme numérique. Cela s'appelle la **numérisation**. L'application des techniques de science des données à ces données pour orienter les décisions peut entraîner des augmentations significatives de la productivité (ou même un pivot commercial), appelée **transformation numérique**.

Prenons un exemple. Supposons que nous avons un cours de science des données (comme celui-ci) que nous proposons en ligne aux étudiants, et que nous souhaitons utiliser la science des données pour l'améliorer. Comment pouvons-nous le faire ?

Nous pouvons commencer par nous demander "Que peut-on numériser ?" La manière la plus simple serait de mesurer le temps qu'il faut à chaque étudiant pour terminer chaque module, et d'évaluer les connaissances acquises en proposant un test à choix multiples à la fin de chaque module. En calculant la moyenne du temps nécessaire pour terminer chaque module parmi tous les étudiants, nous pouvons identifier les modules qui posent le plus de difficultés et travailler à les simplifier.
> Vous pourriez soutenir que cette approche n'est pas idéale, car les modules peuvent avoir des longueurs différentes. Il serait probablement plus juste de diviser le temps par la longueur du module (en nombre de caractères) et de comparer ces valeurs à la place.
Lorsque nous commençons à analyser les résultats des tests à choix multiples, nous pouvons essayer de déterminer quels concepts posent des difficultés de compréhension aux étudiants, et utiliser ces informations pour améliorer le contenu. Pour ce faire, il est nécessaire de concevoir les tests de manière à ce que chaque question corresponde à un concept ou une portion de connaissances spécifique.

Si nous souhaitons aller encore plus loin, nous pouvons tracer le temps nécessaire pour chaque module en fonction de la catégorie d'âge des étudiants. Nous pourrions découvrir que, pour certaines catégories d'âge, il faut un temps excessivement long pour terminer le module, ou que les étudiants abandonnent avant de le terminer. Cela peut nous aider à fournir des recommandations d'âge pour le module et à minimiser l'insatisfaction liée à des attentes erronées.

## 🚀 Défi

Dans ce défi, nous allons essayer de trouver des concepts pertinents dans le domaine de la science des données en analysant des textes. Nous prendrons un article Wikipédia sur la science des données, téléchargerons et traiterons le texte, puis créerons un nuage de mots comme celui-ci :

![Nuage de mots pour la science des données](../../../../translated_images/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.fr.png)

Visitez [`notebook.ipynb`](../../../../../../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') pour parcourir le code. Vous pouvez également exécuter le code et voir comment il effectue toutes les transformations de données en temps réel.

> Si vous ne savez pas comment exécuter du code dans un Jupyter Notebook, consultez [cet article](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Quiz post-conférence](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/1)

## Exercices

* **Tâche 1** : Modifiez le code ci-dessus pour découvrir des concepts liés aux domaines du **Big Data** et de l'**apprentissage automatique**.
* **Tâche 2** : [Réfléchissez à des scénarios de science des données](assignment.md)

## Crédits

Cette leçon a été rédigée avec ♥️ par [Dmitry Soshnikov](http://soshnikov.com)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction professionnelle humaine. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.