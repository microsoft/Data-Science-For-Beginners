<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a0556b17de4c8d1a9470b02247b01d4",
  "translation_date": "2025-09-04T12:54:48+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "fr"
}
-->
# Introduction à la Science des Données dans le Cloud

|![ Sketchnote par [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Science des Données dans le Cloud : Introduction - _Sketchnote par [@nitya](https://twitter.com/nitya)_ |


Dans cette leçon, vous apprendrez les principes fondamentaux du Cloud, puis vous découvrirez pourquoi il peut être intéressant d'utiliser les services Cloud pour exécuter vos projets de science des données. Nous examinerons également quelques exemples de projets de science des données réalisés dans le Cloud. 

## [Quiz avant la leçon](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## Qu'est-ce que le Cloud ?

Le Cloud, ou l'informatique en nuage, désigne la fourniture d'une large gamme de services informatiques à la demande, hébergés sur une infrastructure accessible via Internet. Ces services incluent des solutions telles que le stockage, les bases de données, les réseaux, les logiciels, l'analyse et les services intelligents.

On distingue généralement les Clouds Publics, Privés et Hybrides comme suit :

* Cloud public : un cloud public est détenu et exploité par un fournisseur de services cloud tiers qui met ses ressources informatiques à disposition du public via Internet.
* Cloud privé : fait référence aux ressources informatiques en nuage utilisées exclusivement par une entreprise ou organisation unique, avec des services et une infrastructure maintenus sur un réseau privé.
* Cloud hybride : le cloud hybride est un système qui combine les clouds publics et privés. Les utilisateurs optent pour un centre de données sur site tout en permettant aux données et applications de fonctionner sur un ou plusieurs clouds publics.

La plupart des services d'informatique en nuage se répartissent en trois catégories : Infrastructure en tant que Service (IaaS), Plateforme en tant que Service (PaaS) et Logiciel en tant que Service (SaaS).

* Infrastructure en tant que Service (IaaS) : les utilisateurs louent une infrastructure informatique telle que des serveurs, des machines virtuelles (VM), du stockage, des réseaux, des systèmes d'exploitation.
* Plateforme en tant que Service (PaaS) : les utilisateurs louent un environnement pour développer, tester, livrer et gérer des applications logicielles. Les utilisateurs n'ont pas besoin de se soucier de la configuration ou de la gestion de l'infrastructure sous-jacente des serveurs, du stockage, du réseau et des bases de données nécessaires au développement.
* Logiciel en tant que Service (SaaS) : les utilisateurs accèdent à des applications logicielles via Internet, à la demande et généralement sur une base d'abonnement. Les utilisateurs n'ont pas besoin de se soucier de l'hébergement et de la gestion de l'application logicielle, de l'infrastructure sous-jacente ou de la maintenance, comme les mises à jour logicielles et les correctifs de sécurité.

Parmi les principaux fournisseurs de Cloud figurent Amazon Web Services, Google Cloud Platform et Microsoft Azure.

## Pourquoi choisir le Cloud pour la science des données ?

Les développeurs et les professionnels de l'informatique choisissent de travailler avec le Cloud pour de nombreuses raisons, notamment :

* Innovation : vous pouvez alimenter vos applications en intégrant directement des services innovants créés par les fournisseurs de Cloud dans vos applications.
* Flexibilité : vous ne payez que pour les services dont vous avez besoin et pouvez choisir parmi une large gamme de services. Vous payez généralement à l'utilisation et adaptez vos services en fonction de vos besoins évolutifs.
* Budget : vous n'avez pas besoin de faire des investissements initiaux pour acheter du matériel et des logiciels, configurer et gérer des centres de données sur site, et vous pouvez simplement payer pour ce que vous utilisez.
* Scalabilité : vos ressources peuvent évoluer en fonction des besoins de votre projet, ce qui signifie que vos applications peuvent utiliser plus ou moins de puissance de calcul, de stockage et de bande passante, en s'adaptant à des facteurs externes à tout moment.
* Productivité : vous pouvez vous concentrer sur votre activité plutôt que de passer du temps sur des tâches qui peuvent être gérées par quelqu'un d'autre, comme la gestion des centres de données.
* Fiabilité : l'informatique en nuage offre plusieurs moyens de sauvegarder en continu vos données et vous pouvez mettre en place des plans de reprise après sinistre pour maintenir votre activité et vos services, même en période de crise.
* Sécurité : vous pouvez bénéficier de politiques, de technologies et de contrôles qui renforcent la sécurité de votre projet.

Ce sont quelques-unes des raisons les plus courantes pour lesquelles les gens choisissent d'utiliser les services Cloud. Maintenant que nous avons une meilleure compréhension de ce qu'est le Cloud et de ses principaux avantages, examinons plus spécifiquement les métiers des data scientists et des développeurs travaillant avec les données, et comment le Cloud peut les aider à relever plusieurs défis auxquels ils pourraient être confrontés :

* Stocker de grandes quantités de données : au lieu d'acheter, de gérer et de protéger de grands serveurs, vous pouvez stocker vos données directement dans le Cloud, avec des solutions telles qu'Azure Cosmos DB, Azure SQL Database et Azure Data Lake Storage.
* Réaliser l'intégration des données : l'intégration des données est une partie essentielle de la science des données, qui vous permet de passer de la collecte de données à la prise de décisions. Avec les services d'intégration de données proposés dans le Cloud, vous pouvez collecter, transformer et intégrer des données provenant de diverses sources dans un entrepôt de données unique, avec Data Factory.
* Traiter les données : le traitement de vastes quantités de données nécessite beaucoup de puissance de calcul, et tout le monde n'a pas accès à des machines suffisamment puissantes pour cela, c'est pourquoi beaucoup choisissent de tirer parti de la puissance de calcul massive du Cloud pour exécuter et déployer leurs solutions.
* Utiliser des services d'analyse de données : des services Cloud comme Azure Synapse Analytics, Azure Stream Analytics et Azure Databricks vous aident à transformer vos données en informations exploitables.
* Utiliser des services d'intelligence artificielle et d'apprentissage automatique : au lieu de partir de zéro, vous pouvez utiliser des algorithmes d'apprentissage automatique proposés par le fournisseur de Cloud, avec des services tels qu'AzureML. Vous pouvez également utiliser des services cognitifs tels que la conversion de la parole en texte, le texte en parole, la vision par ordinateur et bien plus encore.

## Exemples de science des données dans le Cloud

Rendons cela plus concret en examinant quelques scénarios.

### Analyse en temps réel des sentiments sur les réseaux sociaux
Commençons par un scénario couramment étudié par les débutants en apprentissage automatique : l'analyse des sentiments sur les réseaux sociaux en temps réel.

Disons que vous gérez un site web d'actualités et que vous souhaitez exploiter des données en direct pour comprendre quels contenus pourraient intéresser vos lecteurs. Pour en savoir plus, vous pouvez créer un programme qui effectue une analyse des sentiments en temps réel des données provenant des publications Twitter, sur des sujets pertinents pour vos lecteurs.

Les indicateurs clés que vous examinerez sont le volume de tweets sur des sujets spécifiques (hashtags) et les sentiments, établis à l'aide d'outils d'analyse qui réalisent une analyse des sentiments autour des sujets spécifiés.

Les étapes nécessaires pour créer ce projet sont les suivantes :

* Créer un hub d'événements pour la collecte des données en streaming, qui collectera les données de Twitter.
* Configurer et démarrer une application cliente Twitter, qui appellera les API de streaming Twitter.
* Créer un travail d'analyse de flux.
* Spécifier les entrées et les requêtes du travail.
* Créer un réceptacle de sortie et spécifier les sorties du travail.
* Démarrer le travail.

Pour voir le processus complet, consultez la [documentation](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Analyse des articles scientifiques
Prenons un autre exemple de projet créé par [Dmitry Soshnikov](http://soshnikov.com), l'un des auteurs de ce programme.

Dmitry a créé un outil qui analyse les articles sur le COVID. En examinant ce projet, vous verrez comment créer un outil qui extrait des connaissances des articles scientifiques, obtient des informations et aide les chercheurs à naviguer efficacement dans de grandes collections d'articles.

Voyons les différentes étapes utilisées pour cela :
* Extraction et prétraitement des informations avec [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Utilisation de [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) pour paralléliser le traitement.
* Stockage et interrogation des informations avec [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Création d'un tableau de bord interactif pour l'exploration et la visualisation des données avec Power BI.

Pour voir le processus complet, visitez le [blog de Dmitry](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Comme vous pouvez le constater, nous pouvons tirer parti des services Cloud de nombreuses façons pour réaliser de la science des données.

## Note de bas de page

Sources :
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Quiz après la leçon

## [Quiz après la leçon](https://ff-quizzes.netlify.app/en/ds/)

## Devoir

[Étude de marché](assignment.md)

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.