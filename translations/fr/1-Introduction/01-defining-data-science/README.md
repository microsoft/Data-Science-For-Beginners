<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a0516588d172f82f35f7a0d4a001e5d0",
  "translation_date": "2025-09-05T12:31:30+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "fr"
}
-->
# Définir la Science des Données

| ![ Sketchnote par [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------: |
|              Définir la Science des Données - _Sketchnote par [@nitya](https://twitter.com/nitya)_     |

---

[![Vidéo : Définir la Science des Données](../../../../1-Introduction/01-defining-data-science/images/video-def-ds.png)](https://youtu.be/beZ7Mb_oz9I)

## [Quiz avant le cours](https://ff-quizzes.netlify.app/en/ds/quiz/0)

## Qu'est-ce que les Données ?
Dans notre vie quotidienne, nous sommes constamment entourés de données. Le texte que vous lisez actuellement est une donnée. La liste des numéros de téléphone de vos amis dans votre smartphone est une donnée, tout comme l'heure actuelle affichée sur votre montre. En tant qu'êtres humains, nous manipulons naturellement des données en comptant l'argent que nous avons ou en écrivant des lettres à nos amis.

Cependant, les données sont devenues beaucoup plus cruciales avec l'avènement des ordinateurs. Le rôle principal des ordinateurs est d'effectuer des calculs, mais ils ont besoin de données pour fonctionner. Ainsi, nous devons comprendre comment les ordinateurs stockent et traitent les données.

Avec l'émergence d'Internet, le rôle des ordinateurs en tant qu'outils de gestion des données s'est accru. Si vous y réfléchissez, nous utilisons désormais les ordinateurs de plus en plus pour traiter et communiquer des données, plutôt que pour effectuer de réels calculs. Lorsque nous écrivons un e-mail à un ami ou recherchons des informations sur Internet, nous créons, stockons, transmettons et manipulons essentiellement des données.
> Vous souvenez-vous de la dernière fois où vous avez utilisé un ordinateur pour réellement effectuer un calcul ?

## Qu'est-ce que la Science des Données ?

Selon [Wikipedia](https://en.wikipedia.org/wiki/Data_science), la **Science des Données** est définie comme *un domaine scientifique qui utilise des méthodes scientifiques pour extraire des connaissances et des informations à partir de données structurées et non structurées, et appliquer ces connaissances et informations exploitables dans divers domaines d'application*.

Cette définition met en lumière les aspects importants suivants de la science des données :

* L'objectif principal de la science des données est d'**extraire des connaissances** à partir des données, c'est-à-dire **comprendre** les données, découvrir des relations cachées et construire un **modèle**.
* La science des données utilise des **méthodes scientifiques**, telles que la probabilité et les statistiques. En fait, lorsque le terme *science des données* a été introduit pour la première fois, certains ont soutenu qu'il ne s'agissait que d'un nouveau nom à la mode pour les statistiques. Aujourd'hui, il est évident que le domaine est beaucoup plus vaste.
* Les connaissances obtenues doivent être appliquées pour produire des **informations exploitables**, c'est-à-dire des informations pratiques que l'on peut appliquer à des situations commerciales réelles.
* Nous devons être capables de travailler avec des données à la fois **structurées** et **non structurées**. Nous reviendrons sur les différents types de données plus tard dans le cours.
* Le **domaine d'application** est un concept important, et les scientifiques des données ont souvent besoin d'un certain degré d'expertise dans le domaine du problème, par exemple : finance, médecine, marketing, etc.

> Un autre aspect important de la Science des Données est qu'elle étudie comment les données peuvent être collectées, stockées et manipulées à l'aide d'ordinateurs. Alors que les statistiques nous fournissent des bases mathématiques, la science des données applique des concepts mathématiques pour réellement tirer des informations des données.

Une des façons (attribuée à [Jim Gray](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) de considérer la science des données est de la voir comme un paradigme scientifique distinct :
* **Empirique**, où l'on se base principalement sur les observations et les résultats d'expériences
* **Théorique**, où de nouveaux concepts émergent à partir des connaissances scientifiques existantes
* **Computationnel**, où l'on découvre de nouveaux principes à partir d'expériences computationnelles
* **Basé sur les Données**, en découvrant des relations et des motifs dans les données  

## Autres Domaines Connexes

Étant donné que les données sont omniprésentes, la science des données est également un domaine vaste, touchant à de nombreuses autres disciplines.

## Types de Données

Comme nous l'avons déjà mentionné, les données sont partout. Il suffit de les capturer de la bonne manière ! Il est utile de distinguer entre les données **structurées** et **non structurées**. Les premières sont généralement représentées sous une forme bien structurée, souvent sous forme de tableau ou de plusieurs tableaux, tandis que les secondes ne sont qu'une collection de fichiers. Parfois, on peut également parler de données **semi-structurées**, qui possèdent une certaine structure pouvant varier considérablement.

| Structurées                                                                | Semi-structurées                                                                               | Non structurées                        |
| -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | -------------------------------------- |
| Liste de personnes avec leurs numéros de téléphone                         | Pages Wikipédia avec des liens                                                                | Texte de l'Encyclopédie Britannica     |
| Température dans toutes les pièces d'un bâtiment chaque minute pendant 20 ans | Collection d'articles scientifiques au format JSON avec auteurs, date de publication et résumé | Partage de fichiers avec des documents d'entreprise |
| Données sur l'âge et le genre de toutes les personnes entrant dans un bâtiment | Pages Internet                                                                                | Flux vidéo brut d'une caméra de surveillance |

## Où Trouver des Données

Il existe de nombreuses sources possibles de données, et il serait impossible de toutes les énumérer ! Cependant, mentionnons quelques endroits typiques où vous pouvez trouver des données :

* **Structurées**
  - **Internet des Objets** (IoT), y compris les données provenant de différents capteurs, tels que les capteurs de température ou de pression, qui fournissent de nombreuses données utiles. Par exemple, si un bâtiment de bureaux est équipé de capteurs IoT, nous pouvons contrôler automatiquement le chauffage et l'éclairage pour minimiser les coûts.
  - **Enquêtes** que nous demandons aux utilisateurs de remplir après un achat ou après avoir visité un site web.
  - **Analyse du comportement** peut, par exemple, nous aider à comprendre jusqu'où un utilisateur explore un site et quelle est la raison typique de son départ.
* **Non structurées**
  - **Textes** qui peuvent être une riche source d'informations, comme un **score de sentiment global**, ou l'extraction de mots-clés et de significations sémantiques.
  - **Images** ou **Vidéos**. Une vidéo d'une caméra de surveillance peut être utilisée pour estimer le trafic sur la route et informer les gens des embouteillages potentiels.
  - Les **Journaux** des serveurs web peuvent être utilisés pour comprendre quelles pages de notre site sont les plus souvent visitées et pendant combien de temps.
* **Semi-structurées**
  - Les graphes des **Réseaux Sociaux** peuvent être d'excellentes sources de données sur les personnalités des utilisateurs et leur potentiel à diffuser des informations.
  - Lorsque nous avons un ensemble de photographies d'une fête, nous pouvons essayer d'extraire des données sur la **dynamique de groupe** en construisant un graphe des personnes prenant des photos ensemble.

En connaissant les différentes sources possibles de données, vous pouvez réfléchir à différents scénarios où les techniques de science des données peuvent être appliquées pour mieux comprendre une situation et améliorer les processus commerciaux.

## Ce que Vous Pouvez Faire avec les Données

En Science des Données, nous nous concentrons sur les étapes suivantes du parcours des données :

Bien sûr, selon les données réelles, certaines étapes peuvent être absentes (par exemple, lorsque nous avons déjà les données dans la base de données, ou lorsque nous n'avons pas besoin d'entraîner un modèle), ou certaines étapes peuvent être répétées plusieurs fois (comme le traitement des données).

## Numérisation et Transformation Numérique

Au cours de la dernière décennie, de nombreuses entreprises ont commencé à comprendre l'importance des données dans la prise de décisions commerciales. Pour appliquer les principes de la science des données à la gestion d'une entreprise, il faut d'abord collecter des données, c'est-à-dire traduire les processus commerciaux en forme numérique. Cela s'appelle la **numérisation**. Appliquer des techniques de science des données à ces données pour orienter les décisions peut conduire à des augmentations significatives de la productivité (ou même à un pivot commercial), appelé **transformation numérique**.

Prenons un exemple. Supposons que nous ayons un cours de science des données (comme celui-ci) que nous dispensons en ligne aux étudiants, et que nous souhaitons utiliser la science des données pour l'améliorer. Comment pouvons-nous le faire ?

Nous pouvons commencer par nous demander "Qu'est-ce qui peut être numérisé ?" La manière la plus simple serait de mesurer le temps qu'il faut à chaque étudiant pour terminer chaque module, et d'évaluer les connaissances acquises en donnant un test à choix multiples à la fin de chaque module. En calculant la moyenne du temps nécessaire pour terminer chaque module parmi tous les étudiants, nous pouvons identifier les modules qui posent le plus de difficultés et travailler à les simplifier.
> Vous pourriez soutenir que cette approche n'est pas idéale, car les modules peuvent avoir des longueurs différentes. Il serait probablement plus juste de diviser le temps par la longueur du module (en nombre de caractères) et de comparer ces valeurs à la place.
Lorsque nous commençons à analyser les résultats de tests à choix multiples, nous pouvons essayer de déterminer quels concepts les étudiants ont du mal à comprendre, et utiliser ces informations pour améliorer le contenu. Pour ce faire, nous devons concevoir les tests de manière à ce que chaque question corresponde à un concept ou une notion spécifique.

Si nous voulons aller encore plus loin, nous pouvons tracer le temps pris pour chaque module en fonction de la catégorie d'âge des étudiants. Nous pourrions découvrir que, pour certaines catégories d'âge, il faut un temps excessivement long pour terminer le module, ou que les étudiants abandonnent avant de le terminer. Cela peut nous aider à fournir des recommandations d'âge pour le module et à minimiser l'insatisfaction liée à des attentes erronées.

## 🚀 Défi

Dans ce défi, nous allons essayer de trouver des concepts pertinents dans le domaine de la science des données en examinant des textes. Nous prendrons un article Wikipédia sur la science des données, téléchargerons et traiterons le texte, puis construirons un nuage de mots comme celui-ci :

![Nuage de mots pour la science des données](../../../../1-Introduction/01-defining-data-science/images/ds_wordcloud.png)

Visitez [`notebook.ipynb`](../../../../../../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') pour parcourir le code. Vous pouvez également exécuter le code et voir comment il effectue toutes les transformations de données en temps réel.

> Si vous ne savez pas comment exécuter du code dans un Jupyter Notebook, consultez [cet article](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Quiz post-cours](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Devoirs

* **Tâche 1** : Modifiez le code ci-dessus pour découvrir des concepts liés aux domaines du **Big Data** et de l'**apprentissage automatique**.
* **Tâche 2** : [Réfléchissez à des scénarios en science des données](assignment.md)

## Crédits

Cette leçon a été rédigée avec ♥️ par [Dmitry Soshnikov](http://soshnikov.com)

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.