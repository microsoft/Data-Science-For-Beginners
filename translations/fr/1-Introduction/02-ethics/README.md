<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1341f6da63d434f5ba31b08ea951b02c",
  "translation_date": "2025-09-05T12:32:27+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "fr"
}
-->
# Introduction à l'éthique des données

|![ Sketchnote par [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Éthique des données - _Sketchnote par [@nitya](https://twitter.com/nitya)_ |

---

Nous sommes tous des citoyens des données vivant dans un monde axé sur les données.

Les tendances du marché indiquent qu'en 2022, une grande organisation sur trois achètera et vendra ses données via des [places de marché et des échanges](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/) en ligne. En tant que **développeurs d'applications**, il sera plus facile et moins coûteux d'intégrer des analyses basées sur les données et des automatisations pilotées par des algorithmes dans les expériences quotidiennes des utilisateurs. Mais à mesure que l'IA devient omniprésente, nous devrons également comprendre les dommages potentiels causés par la [militarisation](https://www.youtube.com/watch?v=TQHs8SA1qpk) de ces algorithmes à grande échelle.

Les tendances montrent également que nous créerons et consommerons plus de [180 zettaoctets](https://www.statista.com/statistics/871513/worldwide-data-created/) de données d'ici 2025. En tant que **scientifiques des données**, cela nous donne un accès sans précédent aux données personnelles. Cela signifie que nous pouvons construire des profils comportementaux des utilisateurs et influencer la prise de décision de manière à créer une [illusion de libre choix](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice), tout en orientant potentiellement les utilisateurs vers des résultats que nous préférons. Cela soulève également des questions plus larges sur la confidentialité des données et la protection des utilisateurs.

L'éthique des données est désormais une _barrière nécessaire_ pour la science et l'ingénierie des données, nous aidant à minimiser les dommages potentiels et les conséquences involontaires de nos actions basées sur les données. Le [cycle de vie des tendances de Gartner pour l'IA](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) identifie des tendances pertinentes en matière d'éthique numérique, d'IA responsable et de gouvernance de l'IA comme des moteurs clés des mégatendances plus larges autour de la _démocratisation_ et de l'_industrialisation_ de l'IA.

![Cycle de vie des tendances de Gartner pour l'IA - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

Dans cette leçon, nous explorerons le domaine fascinant de l'éthique des données - des concepts et défis fondamentaux aux études de cas et aux concepts appliqués de l'IA comme la gouvernance - qui aident à établir une culture éthique dans les équipes et les organisations travaillant avec les données et l'IA.

## [Quiz avant la leçon](https://ff-quizzes.netlify.app/en/ds/quiz/2) 🎯

## Définitions de base

Commençons par comprendre la terminologie de base.

Le mot "éthique" vient du [mot grec "ethikos"](https://en.wikipedia.org/wiki/Ethics) (et de sa racine "ethos") signifiant _caractère ou nature morale_. 

**L'éthique** concerne les valeurs partagées et les principes moraux qui régissent notre comportement en société. L'éthique ne repose pas sur des lois mais sur des normes largement acceptées de ce qui est "bien contre mal". Cependant, les considérations éthiques peuvent influencer les initiatives de gouvernance d'entreprise et les réglementations gouvernementales qui créent davantage d'incitations à la conformité.

**L'éthique des données** est une [nouvelle branche de l'éthique](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1) qui "étudie et évalue les problèmes moraux liés aux _données, algorithmes et pratiques correspondantes_". Ici, **"données"** se concentre sur les actions liées à la génération, l'enregistrement, la conservation, le traitement, la diffusion, le partage et l'utilisation, **"algorithmes"** se concentre sur l'IA, les agents, l'apprentissage automatique et les robots, et **"pratiques"** se concentre sur des sujets comme l'innovation responsable, la programmation, le piratage et les codes éthiques.

**L'éthique appliquée** est [l'application pratique des considérations morales](https://en.wikipedia.org/wiki/Applied_ethics). C'est le processus d'enquête active sur les questions éthiques dans le contexte des _actions, produits et processus du monde réel_, et de prise de mesures correctives pour s'assurer qu'ils restent alignés avec nos valeurs éthiques définies.

**La culture éthique** consiste à [_opérationnaliser_ l'éthique appliquée](https://hbr.org/2019/05/how-to-design-an-ethical-organization) pour s'assurer que nos principes et pratiques éthiques sont adoptés de manière cohérente et évolutive dans toute l'organisation. Les cultures éthiques réussies définissent des principes éthiques à l'échelle de l'organisation, offrent des incitations significatives à la conformité et renforcent les normes éthiques en encourageant et en amplifiant les comportements souhaités à tous les niveaux de l'organisation.

## Concepts d'éthique

Dans cette section, nous discuterons des concepts tels que les **valeurs partagées** (principes) et les **défis éthiques** (problèmes) pour l'éthique des données - et explorerons des **études de cas** qui vous aident à comprendre ces concepts dans des contextes réels.

### 1. Principes éthiques

Toute stratégie d'éthique des données commence par la définition des _principes éthiques_ - les "valeurs partagées" qui décrivent les comportements acceptables et guident les actions conformes dans nos projets de données et d'IA. Vous pouvez les définir au niveau individuel ou de l'équipe. Cependant, la plupart des grandes organisations les décrivent dans une déclaration de mission ou un cadre d'_IA éthique_ défini au niveau de l'entreprise et appliqué de manière cohérente à toutes les équipes.

**Exemple :** La déclaration de mission de [Microsoft sur l'IA responsable](https://www.microsoft.com/en-us/ai/responsible-ai) indique : _"Nous nous engageons à faire progresser l'IA guidée par des principes éthiques qui placent les personnes au premier plan"_ - en identifiant 6 principes éthiques dans le cadre ci-dessous :

![IA responsable chez Microsoft](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Explorons brièvement ces principes. _La transparence_ et _la responsabilité_ sont des valeurs fondamentales sur lesquelles les autres principes se construisent - commençons donc par là :

* [**Responsabilité**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) rend les praticiens _responsables_ de leurs opérations de données et d'IA, et de leur conformité à ces principes éthiques.
* [**Transparence**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) garantit que les actions liées aux données et à l'IA sont _compréhensibles_ (interprétables) pour les utilisateurs, en expliquant le quoi et le pourquoi derrière les décisions.
* [**Équité**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) - se concentre sur le fait de garantir que l'IA traite _toutes les personnes_ équitablement, en abordant les biais sociotechniques systémiques ou implicites dans les données et les systèmes.
* [**Fiabilité et sécurité**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - garantit que l'IA se comporte de manière _cohérente_ avec les valeurs définies, en minimisant les dommages potentiels ou les conséquences involontaires.
* [**Confidentialité et sécurité**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - concerne la compréhension de la provenance des données et la fourniture de _protection de la confidentialité des données_ aux utilisateurs.
* [**Inclusivité**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) - consiste à concevoir des solutions d'IA avec intention, en les adaptant pour répondre à un _large éventail de besoins et de capacités humaines_.

> 🚨 Réfléchissez à ce que pourrait être votre déclaration de mission sur l'éthique des données. Explorez les cadres d'IA éthique d'autres organisations - voici des exemples de [IBM](https://www.ibm.com/cloud/learn/ai-ethics), [Google](https://ai.google/principles), et [Facebook](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Quelles valeurs partagées ont-ils en commun ? Comment ces principes se rapportent-ils au produit ou à l'industrie de l'IA dans laquelle ils opèrent ?

### 2. Défis éthiques

Une fois que nous avons défini des principes éthiques, l'étape suivante consiste à évaluer nos actions liées aux données et à l'IA pour voir si elles s'alignent sur ces valeurs partagées. Réfléchissez à vos actions dans deux catégories : _collecte de données_ et _conception d'algorithmes_.

Avec la collecte de données, les actions impliqueront probablement des **données personnelles** ou des informations personnellement identifiables (PII) pour des individus identifiables. Cela inclut [divers éléments de données non personnelles](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en) qui _identifient collectivement_ un individu. Les défis éthiques peuvent concerner la _confidentialité des données_, la _propriété des données_, et des sujets connexes comme le _consentement éclairé_ et les _droits de propriété intellectuelle_ des utilisateurs.

Avec la conception d'algorithmes, les actions impliqueront la collecte et la conservation de **ensembles de données**, puis leur utilisation pour entraîner et déployer des **modèles de données** qui prédisent des résultats ou automatisent des décisions dans des contextes réels. Les défis éthiques peuvent découler de _biais dans les ensembles de données_, de problèmes de _qualité des données_, de _manque d'équité_, et de _mauvaise représentation_ dans les algorithmes - y compris certains problèmes qui sont systémiques.

Dans les deux cas, les défis éthiques mettent en évidence les domaines où nos actions peuvent entrer en conflit avec nos valeurs partagées. Pour détecter, atténuer, minimiser ou éliminer ces préoccupations, nous devons poser des questions morales "oui/non" liées à nos actions, puis prendre des mesures correctives si nécessaire. Examinons quelques défis éthiques et les questions morales qu'ils soulèvent :

#### 2.1 Propriété des données

La collecte de données implique souvent des données personnelles qui peuvent identifier les sujets des données. La [propriété des données](https://permission.io/blog/data-ownership) concerne le _contrôle_ et les [_droits des utilisateurs_](https://permission.io/blog/data-ownership) liés à la création, au traitement et à la diffusion des données.

Les questions morales à poser sont :  
* Qui possède les données ? (utilisateur ou organisation)  
* Quels droits les sujets des données ont-ils ? (ex : accès, effacement, portabilité)  
* Quels droits les organisations ont-elles ? (ex : rectifier des avis malveillants des utilisateurs)  

#### 2.2 Consentement éclairé

Le [consentement éclairé](https://legaldictionary.net/informed-consent/) définit l'acte des utilisateurs d'accepter une action (comme la collecte de données) avec une _compréhension complète_ des faits pertinents, y compris le but, les risques potentiels et les alternatives.

Questions à explorer ici :  
* L'utilisateur (sujet des données) a-t-il donné son autorisation pour la capture et l'utilisation des données ?  
* L'utilisateur a-t-il compris le but pour lequel ces données ont été capturées ?  
* L'utilisateur a-t-il compris les risques potentiels liés à sa participation ?  

#### 2.3 Propriété intellectuelle

La [propriété intellectuelle](https://en.wikipedia.org/wiki/Intellectual_property) fait référence aux créations intangibles résultant de l'initiative humaine, qui peuvent _avoir une valeur économique_ pour les individus ou les entreprises.

Questions à explorer ici :  
* Les données collectées avaient-elles une valeur économique pour un utilisateur ou une entreprise ?  
* L'**utilisateur** a-t-il une propriété intellectuelle ici ?  
* L'**organisation** a-t-elle une propriété intellectuelle ici ?  
* Si ces droits existent, comment les protégeons-nous ?  

#### 2.4 Confidentialité des données

La [confidentialité des données](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) ou confidentialité des informations fait référence à la préservation de la vie privée des utilisateurs et à la protection de leur identité en ce qui concerne les informations personnellement identifiables.

Questions à explorer ici :  
* Les données (personnelles) des utilisateurs sont-elles sécurisées contre les piratages et les fuites ?  
* Les données des utilisateurs sont-elles accessibles uniquement aux utilisateurs et contextes autorisés ?  
* L'anonymat des utilisateurs est-il préservé lorsque les données sont partagées ou diffusées ?  
* Un utilisateur peut-il être désidentifié à partir d'ensembles de données anonymisés ?  

#### 2.5 Droit à l'oubli

Le [droit à l'oubli](https://en.wikipedia.org/wiki/Right_to_be_forgotten) ou [droit à l'effacement](https://www.gdpreu.org/right-to-be-forgotten/) offre une protection supplémentaire des données personnelles aux utilisateurs. En particulier, il donne aux utilisateurs le droit de demander la suppression ou le retrait de données personnelles des recherches Internet et d'autres emplacements, _dans des circonstances spécifiques_ - leur permettant de repartir à zéro en ligne sans que leurs actions passées ne soient retenues contre eux.

Questions à explorer ici :  
* Le système permet-il aux sujets des données de demander l'effacement ?  
* Le retrait du consentement de l'utilisateur devrait-il déclencher un effacement automatisé ?  
* Les données ont-elles été collectées sans consentement ou par des moyens illégaux ?  
* Sommes-nous conformes aux réglementations gouvernementales sur la confidentialité des données ?  

#### 2.6 Biais dans les ensembles de données

Le biais dans les ensembles de données ou [biais de collecte](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) concerne la sélection d'un sous-ensemble _non représentatif_ de données pour le développement d'algorithmes, créant une potentielle injustice dans les résultats pour divers groupes. Les types de biais incluent le biais de sélection ou d'échantillonnage, le biais de volontariat et le biais d'instrument.

Questions à explorer ici :  
* Avons-nous recruté un ensemble représentatif de sujets des données ?  
* Avons-nous testé notre ensemble de données collecté ou conservé pour divers biais ?  
* Pouvons-nous atténuer ou supprimer les biais découverts ?  

#### 2.7 Qualité des données

La [qualité des données](https://lakefs.io/data-quality-testing/) examine la validité de l'ensemble de données conservé utilisé pour développer nos algorithmes, en vérifiant si les caractéristiques et les enregistrements répondent aux exigences du niveau de précision et de cohérence nécessaire à notre objectif d'IA.

Questions à explorer ici :  
* Avons-nous capturé des _caractéristiques_ valides pour notre cas d'utilisation ?  
* Les données ont-elles été capturées de manière _cohérente_ à travers diverses sources de données ?  
* L'ensemble de données est-il _complet_ pour diverses conditions ou scénarios ?  
* Les informations capturées sont-elles _précises_ et reflètent-elles la réalité ?  

#### 2.8 Équité des algorithmes
[Algorithm Fairness](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) vérifie si la conception de l'algorithme discrimine systématiquement certains sous-groupes de sujets de données, entraînant des [préjudices potentiels](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) dans l'_allocation_ (où des ressources sont refusées ou retenues pour ce groupe) et la _qualité du service_ (où l'IA est moins précise pour certains sous-groupes par rapport à d'autres).

Questions à explorer ici :
 * Avons-nous évalué la précision du modèle pour des sous-groupes et des conditions diversifiés ?
 * Avons-nous examiné le système pour identifier des préjudices potentiels (par exemple, des stéréotypes) ?
 * Pouvons-nous réviser les données ou réentraîner les modèles pour atténuer les préjudices identifiés ?

Explorez des ressources comme les [checklists sur l'équité de l'IA](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA) pour en savoir plus.

#### 2.9 Fausse représentation

La [fausse représentation des données](https://www.sciencedirect.com/topics/computer-science/misrepresentation) consiste à se demander si nous communiquons des informations issues de données honnêtement rapportées de manière trompeuse pour soutenir un récit souhaité.

Questions à explorer ici :
 * Rapportons-nous des données incomplètes ou inexactes ?
 * Visualisons-nous les données d'une manière qui conduit à des conclusions trompeuses ?
 * Utilisons-nous des techniques statistiques sélectives pour manipuler les résultats ?
 * Existe-t-il des explications alternatives qui pourraient offrir une conclusion différente ?

#### 2.10 Libre choix
L'[illusion du libre choix](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) se produit lorsque les "architectures de choix" des systèmes utilisent des algorithmes de prise de décision pour inciter les gens à adopter un résultat préféré tout en leur donnant l'impression d'avoir des options et du contrôle. Ces [dark patterns](https://www.darkpatterns.org/) peuvent causer des préjudices sociaux et économiques aux utilisateurs. Étant donné que les décisions des utilisateurs influencent les profils de comportement, ces actions peuvent potentiellement orienter les choix futurs, amplifiant ou prolongeant l'impact de ces préjudices.

Questions à explorer ici :
 * L'utilisateur a-t-il compris les implications de son choix ?
 * L'utilisateur était-il conscient des choix (alternatifs) et des avantages et inconvénients de chacun ?
 * L'utilisateur peut-il revenir sur un choix automatisé ou influencé ultérieurement ?

### 3. Études de cas

Pour mettre ces défis éthiques dans des contextes réels, il est utile d'examiner des études de cas qui mettent en lumière les préjudices et conséquences potentiels pour les individus et la société lorsque ces violations éthiques sont ignorées.

Voici quelques exemples :

| Défi éthique | Étude de cas  | 
|--- |--- |
| **Consentement éclairé** | 1972 - [Étude sur la syphilis de Tuskegee](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Les hommes afro-américains ayant participé à l'étude ont été promis des soins médicaux gratuits _mais trompés_ par des chercheurs qui n'ont pas informé les sujets de leur diagnostic ou de la disponibilité d'un traitement. De nombreux sujets sont morts et leurs partenaires ou enfants ont été affectés ; l'étude a duré 40 ans. | 
| **Confidentialité des données** |  2007 - Le [concours de données Netflix](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) a fourni aux chercheurs _10M de classements de films anonymisés de 50K clients_ pour améliorer les algorithmes de recommandation. Cependant, les chercheurs ont pu corréler les données anonymisées avec des données personnellement identifiables dans des _ensembles de données externes_ (par exemple, des commentaires IMDb), "désanonymisant" ainsi certains abonnés Netflix.|
| **Biais de collecte**  | 2013 - La ville de Boston a [développé Street Bump](https://www.boston.gov/transportation/street-bump), une application permettant aux citoyens de signaler les nids-de-poule, offrant à la ville de meilleures données sur les routes pour identifier et résoudre les problèmes. Cependant, [les personnes des groupes à faible revenu avaient moins accès aux voitures et aux téléphones](https://hbr.org/2013/04/the-hidden-biases-in-big-data), rendant leurs problèmes de routes invisibles dans cette application. Les développeurs ont travaillé avec des universitaires pour résoudre les problèmes d'_accès équitable et de fractures numériques_ pour plus d'équité. |
| **Équité algorithmique**  | 2018 - L'étude MIT [Gender Shades](http://gendershades.org/overview.html) a évalué la précision des produits d'IA de classification de genre, révélant des écarts de précision pour les femmes et les personnes de couleur. Une [carte Apple de 2019](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) semblait offrir moins de crédit aux femmes qu'aux hommes. Les deux cas ont illustré des problèmes de biais algorithmique entraînant des préjudices socio-économiques.|
| **Fausse représentation des données** | 2020 - Le [Département de la santé publique de Géorgie a publié des graphiques COVID-19](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening) qui semblaient induire les citoyens en erreur sur les tendances des cas confirmés avec un ordre non chronologique sur l'axe des x. Cela illustre la fausse représentation par des astuces de visualisation. |
| **Illusion du libre choix** | 2020 - L'application éducative [ABCmouse a payé 10M$ pour régler une plainte de la FTC](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/) où les parents étaient piégés dans des abonnements qu'ils ne pouvaient pas annuler. Cela illustre les dark patterns dans les architectures de choix, où les utilisateurs étaient incités à faire des choix potentiellement nuisibles. |
| **Confidentialité des données et droits des utilisateurs** | 2021 - La [violation de données Facebook](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) a exposé les données de 530M d'utilisateurs, entraînant un règlement de 5B$ avec la FTC. Cependant, Facebook a refusé de notifier les utilisateurs de la violation, violant les droits des utilisateurs en matière de transparence et d'accès aux données. |

Vous voulez explorer plus d'études de cas ? Consultez ces ressources :
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - dilemmes éthiques dans divers secteurs. 
* [Cours sur l'éthique en science des données](https://www.coursera.org/learn/data-science-ethics#syllabus) - études de cas emblématiques explorées.
* [Où les choses ont mal tourné](https://deon.drivendata.org/examples/) - checklist Deon avec des exemples.

> 🚨 Pensez aux études de cas que vous avez vues - avez-vous vécu ou été affecté par un défi éthique similaire dans votre vie ? Pouvez-vous penser à au moins une autre étude de cas qui illustre l'un des défis éthiques discutés dans cette section ?

## Éthique appliquée

Nous avons parlé des concepts éthiques, des défis et des études de cas dans des contextes réels. Mais comment commencer à _appliquer_ des principes et pratiques éthiques dans nos projets ? Et comment _opérationnaliser_ ces pratiques pour une meilleure gouvernance ? Explorons quelques solutions concrètes : 

### 1. Codes professionnels

Les codes professionnels offrent une option pour que les organisations "incitent" leurs membres à soutenir leurs principes éthiques et leur mission. Les codes sont des _lignes directrices morales_ pour le comportement professionnel, aidant les employés ou membres à prendre des décisions alignées sur les principes de leur organisation. Ils ne sont efficaces que si les membres les respectent volontairement ; cependant, de nombreuses organisations offrent des récompenses et des sanctions supplémentaires pour motiver la conformité.

Exemples :
 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Code d'éthique
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Code de conduite (créé en 2013)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (depuis 1993)

> 🚨 Faites-vous partie d'une organisation professionnelle en ingénierie ou en science des données ? Explorez leur site pour voir s'ils définissent un code d'éthique professionnel. Que dit-il sur leurs principes éthiques ? Comment incitent-ils leurs membres à suivre le code ?

### 2. Checklists éthiques

Alors que les codes professionnels définissent le comportement _éthique requis_ des praticiens, ils [ont des limites connues](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) en matière d'application, en particulier dans les projets à grande échelle. Au lieu de cela, de nombreux experts en science des données [préconisent des checklists](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), qui peuvent **connecter les principes aux pratiques** de manière plus déterministe et actionnable.

Les checklists transforment les questions en tâches "oui/non" qui peuvent être opérationnalisées, permettant leur suivi dans le cadre des workflows standard de lancement de produit.

Exemples :
 * [Deon](https://deon.drivendata.org/) - une checklist éthique générale créée à partir de [recommandations de l'industrie](https://deon.drivendata.org/#checklist-citations) avec un outil en ligne de commande pour une intégration facile.
 * [Checklist d'audit de confidentialité](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - fournit des conseils généraux sur les pratiques de gestion de l'information du point de vue juridique et social.
 * [Checklist sur l'équité de l'IA](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - créée par des praticiens de l'IA pour soutenir l'adoption et l'intégration des vérifications d'équité dans les cycles de développement de l'IA.
 * [22 questions pour l'éthique dans les données et l'IA](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - cadre plus ouvert, structuré pour une exploration initiale des problèmes éthiques dans la conception, la mise en œuvre et les contextes organisationnels.

### 3. Réglementations éthiques

L'éthique consiste à définir des valeurs partagées et à faire ce qui est juste _volontairement_. **La conformité** consiste à _respecter la loi_ là où elle est définie. **La gouvernance** couvre globalement toutes les façons dont les organisations opèrent pour appliquer des principes éthiques et se conformer aux lois établies.

Aujourd'hui, la gouvernance prend deux formes au sein des organisations. Premièrement, il s'agit de définir des principes d'**IA éthique** et d'établir des pratiques pour opérationnaliser leur adoption dans tous les projets liés à l'IA de l'organisation. Deuxièmement, il s'agit de se conformer à toutes les **réglementations sur la protection des données** imposées par les gouvernements des régions où elle opère.

Exemples de réglementations sur la protection des données et la confidentialité :
 * `1974`, [US Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - régule la collecte, l'utilisation et la divulgation des informations personnelles par le _gouvernement fédéral_.
 * `1996`, [US Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - protège les données personnelles de santé.
 * `1998`, [US Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - protège la confidentialité des données des enfants de moins de 13 ans.
 * `2018`, [Règlement général sur la protection des données (RGPD)](https://gdpr-info.eu/) - fournit des droits aux utilisateurs, protège les données et la vie privée.
 * `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) donne aux consommateurs plus de _droits_ sur leurs données personnelles.
 * `2021`, La [Loi sur la protection des informations personnelles de la Chine](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) vient d'être adoptée, créant l'une des réglementations les plus strictes sur la confidentialité des données en ligne dans le monde.

> 🚨 L'Union européenne a défini le RGPD (Règlement général sur la protection des données), qui reste l'une des réglementations les plus influentes sur la confidentialité des données aujourd'hui. Saviez-vous qu'il définit également [8 droits des utilisateurs](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) pour protéger la vie privée numérique et les données personnelles des citoyens ? Découvrez quels sont ces droits et pourquoi ils sont importants.

### 4. Culture éthique

Notez qu'il existe un écart intangible entre _la conformité_ (faire juste assez pour respecter "la lettre de la loi") et le traitement des [problèmes systémiques](https://www.coursera.org/learn/data-science-ethics/home/week/4) (comme l'ossification, l'asymétrie de l'information et l'injustice distributive) qui peuvent accélérer la militarisation de l'IA.

Ce dernier nécessite [des approches collaboratives pour définir des cultures éthiques](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f) qui construisent des connexions émotionnelles et des valeurs partagées cohérentes _entre les organisations_ de l'industrie. Cela appelle à des [cultures éthiques formalisées](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) dans les organisations - permettant à _n'importe qui_ de [tirer le cordon Andon](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (pour soulever des préoccupations éthiques tôt dans le processus) et faisant des _évaluations éthiques_ (par exemple, lors du recrutement) un critère central de la formation des équipes dans les projets d'IA.

---
## [Quiz post-conférence](https://ff-quizzes.netlify.app/en/ds/quiz/3) 🎯
## Révision et auto-apprentissage 

Les cours et les livres aident à comprendre les concepts et défis éthiques fondamentaux, tandis que les études de cas et les outils aident à appliquer les pratiques éthiques dans des contextes réels. Voici quelques ressources pour commencer.

* [Machine Learning For Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - leçon sur l'équité, de Microsoft.
* [Principes de l'IA Responsable](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - parcours d'apprentissage gratuit de Microsoft Learn.  
* [Éthique et Science des Données](https://resources.oreilly.com/examples/0636920203964) - EBook d'O'Reilly (M. Loukides, H. Mason et al.)  
* [Éthique en Science des Données](https://www.coursera.org/learn/data-science-ethics#syllabus) - cours en ligne de l'Université du Michigan.  
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - études de cas de l'Université du Texas.  

# Devoir  

[Écrire une Étude de Cas sur l'Éthique des Données](assignment.md)  

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.