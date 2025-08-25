<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "870a0086adbc313a8eea5489bdcb2522",
  "translation_date": "2025-08-25T16:14:59+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "fr"
}
-->
# Travailler avec les données : Bases de données relationnelles

|![ Sketchnote par [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Travailler avec les données : Bases de données relationnelles - _Sketchnote par [@nitya](https://twitter.com/nitya)_ |

Il y a de fortes chances que vous ayez déjà utilisé un tableur pour stocker des informations. Vous aviez un ensemble de lignes et de colonnes, où les lignes contenaient les informations (ou données), et les colonnes décrivaient ces informations (parfois appelées métadonnées). Une base de données relationnelle repose sur ce principe fondamental de colonnes et de lignes dans des tables, vous permettant de répartir les informations sur plusieurs tables. Cela vous permet de travailler avec des données plus complexes, d'éviter les duplications et d'avoir une flexibilité dans la manière d'explorer les données. Explorons les concepts d'une base de données relationnelle.

## [Quiz avant le cours](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Tout commence par des tables

Une base de données relationnelle repose sur des tables. Tout comme dans un tableur, une table est une collection de colonnes et de lignes. Les lignes contiennent les données ou informations avec lesquelles nous souhaitons travailler, comme le nom d'une ville ou la quantité de précipitations. Les colonnes décrivent les données qu'elles stockent.

Commençons notre exploration en créant une table pour stocker des informations sur les villes. Nous pourrions commencer par leur nom et leur pays. Vous pourriez stocker cela dans une table comme suit :

| Ville     | Pays           |
| --------- | -------------- |
| Tokyo     | Japon          |
| Atlanta   | États-Unis     |
| Auckland  | Nouvelle-Zélande |

Remarquez que les noms des colonnes **Ville**, **Pays** et **Population** décrivent les données stockées, et chaque ligne contient des informations sur une ville.

## Les limites d'une approche avec une seule table

Il y a de fortes chances que la table ci-dessus vous semble relativement familière. Ajoutons maintenant des données supplémentaires à notre base de données naissante : les précipitations annuelles (en millimètres). Nous nous concentrerons sur les années 2018, 2019 et 2020. Si nous devions les ajouter pour Tokyo, cela pourrait ressembler à ceci :

| Ville  | Pays   | Année | Quantité |
| ------ | ------ | ----- | -------- |
| Tokyo  | Japon  | 2020  | 1690     |
| Tokyo  | Japon  | 2019  | 1874     |
| Tokyo  | Japon  | 2018  | 1445     |

Que remarquez-vous dans notre table ? Vous pourriez remarquer que nous dupliquons le nom et le pays de la ville encore et encore. Cela pourrait occuper beaucoup d'espace de stockage, et il est largement inutile d'avoir plusieurs copies. Après tout, Tokyo n'a qu'un seul nom qui nous intéresse.

OK, essayons autre chose. Ajoutons de nouvelles colonnes pour chaque année :

| Ville     | Pays           | 2018  | 2019  | 2020  |
| --------- | -------------- | ----- | ----- | ----- |
| Tokyo     | Japon          | 1445  | 1874  | 1690  |
| Atlanta   | États-Unis     | 1779  | 1111  | 1683  |
| Auckland  | Nouvelle-Zélande | 1386  | 942   | 1176  |

Bien que cela évite la duplication des lignes, cela ajoute d'autres défis. Nous devrions modifier la structure de notre table chaque fois qu'une nouvelle année est ajoutée. De plus, à mesure que nos données augmentent, avoir les années comme colonnes rendra plus difficile la récupération et le calcul des valeurs.

C'est pourquoi nous avons besoin de plusieurs tables et de relations. En divisant nos données, nous pouvons éviter les duplications et avoir plus de flexibilité dans la manière dont nous travaillons avec nos données.

## Les concepts de relations

Revenons à nos données et déterminons comment nous voulons les diviser. Nous savons que nous voulons stocker le nom et le pays de nos villes, donc cela fonctionnera probablement mieux dans une table.

| Ville     | Pays           |
| --------- | -------------- |
| Tokyo     | Japon          |
| Atlanta   | États-Unis     |
| Auckland  | Nouvelle-Zélande |

Mais avant de créer la table suivante, nous devons déterminer comment référencer chaque ville. Nous avons besoin d'une forme d'identifiant, ID ou (en termes techniques de base de données) une clé primaire. Une clé primaire est une valeur utilisée pour identifier une ligne spécifique dans une table. Bien que cela puisse être basé sur une valeur elle-même (nous pourrions utiliser le nom de la ville, par exemple), cela devrait presque toujours être un numéro ou un autre identifiant. Nous ne voulons pas que l'ID change, car cela casserait la relation. Dans la plupart des cas, la clé primaire ou ID sera un numéro généré automatiquement.

> ✅ La clé primaire est fréquemment abrégée en PK

### villes

| ville_id | Ville     | Pays           |
| -------- | --------- | -------------- |
| 1        | Tokyo     | Japon          |
| 2        | Atlanta   | États-Unis     |
| 3        | Auckland  | Nouvelle-Zélande |

> ✅ Vous remarquerez que nous utilisons les termes "id" et "clé primaire" de manière interchangeable pendant cette leçon. Les concepts ici s'appliquent également aux DataFrames, que vous explorerez plus tard. Les DataFrames n'utilisent pas la terminologie de "clé primaire", mais vous remarquerez qu'ils se comportent de manière similaire.

Avec notre table **villes** créée, stockons les précipitations. Plutôt que de dupliquer les informations complètes sur la ville, nous pouvons utiliser l'ID. Nous devrions également nous assurer que la table nouvellement créée a une colonne *id*, car toutes les tables devraient avoir un ID ou une clé primaire.

### précipitations

| precipitation_id | ville_id | Année | Quantité |
| ---------------- | -------- | ----- | -------- |
| 1                | 1        | 2018  | 1445     |
| 2                | 1        | 2019  | 1874     |
| 3                | 1        | 2020  | 1690     |
| 4                | 2        | 2018  | 1779     |
| 5                | 2        | 2019  | 1111     |
| 6                | 2        | 2020  | 1683     |
| 7                | 3        | 2018  | 1386     |
| 8                | 3        | 2019  | 942      |
| 9                | 3        | 2020  | 1176     |

Remarquez la colonne **ville_id** dans la table nouvellement créée **précipitations**. Cette colonne contient des valeurs qui font référence aux IDs dans la table **villes**. En termes techniques de données relationnelles, cela s'appelle une **clé étrangère** ; c'est une clé primaire provenant d'une autre table. Vous pouvez simplement la considérer comme une référence ou un pointeur. **ville_id** 1 fait référence à Tokyo.

> [!NOTE] La clé étrangère est fréquemment abrégée en FK

## Récupérer les données

Avec nos données séparées en deux tables, vous vous demandez peut-être comment les récupérer. Si nous utilisons une base de données relationnelle comme MySQL, SQL Server ou Oracle, nous pouvons utiliser un langage appelé Structured Query Language ou SQL. SQL (parfois prononcé "sequel") est un langage standard utilisé pour récupérer et modifier des données dans une base de données relationnelle.

Pour récupérer des données, vous utilisez la commande `SELECT`. En son cœur, vous **sélectionnez** les colonnes que vous voulez voir **à partir de** la table où elles se trouvent. Si vous vouliez afficher uniquement les noms des villes, vous pourriez utiliser la commande suivante :

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` est l'endroit où vous listez les colonnes, et `FROM` est l'endroit où vous listez les tables.

> [NOTE] La syntaxe SQL n'est pas sensible à la casse, ce qui signifie que `select` et `SELECT` signifient la même chose. Cependant, selon le type de base de données que vous utilisez, les colonnes et les tables pourraient être sensibles à la casse. Par conséquent, il est préférable de toujours traiter tout en programmation comme si c'était sensible à la casse. Lors de l'écriture de requêtes SQL, la convention courante est de mettre les mots-clés en majuscules.

La requête ci-dessus affichera toutes les villes. Imaginons que nous voulions afficher uniquement les villes en Nouvelle-Zélande. Nous avons besoin d'une forme de filtre. Le mot-clé SQL pour cela est `WHERE`, ou "où quelque chose est vrai".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Joindre des données

Jusqu'à présent, nous avons récupéré des données à partir d'une seule table. Maintenant, nous voulons rassembler les données des tables **villes** et **précipitations**. Cela se fait en les *joignant*. Vous allez effectivement créer une liaison entre les deux tables et faire correspondre les valeurs d'une colonne de chaque table.

Dans notre exemple, nous allons faire correspondre la colonne **ville_id** dans **précipitations** avec la colonne **ville_id** dans **villes**. Cela associera la valeur des précipitations à sa ville respective. Le type de jointure que nous effectuerons est ce qu'on appelle une jointure *interne*, ce qui signifie que si des lignes ne correspondent pas à quelque chose dans l'autre table, elles ne seront pas affichées. Dans notre cas, chaque ville a des précipitations, donc tout sera affiché.

Récupérons les précipitations pour 2019 pour toutes nos villes.

Nous allons le faire en étapes. La première étape consiste à joindre les données en indiquant les colonnes pour la liaison - **ville_id** comme mentionné précédemment.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Nous avons mis en évidence les deux colonnes que nous voulons, et le fait que nous voulons joindre les tables ensemble par la colonne **ville_id**. Maintenant, nous pouvons ajouter l'instruction `WHERE` pour filtrer uniquement l'année 2019.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
WHERE rainfall.year = 2019

-- Output

-- city     | amount
-- -------- | ------
-- Tokyo    | 1874
-- Atlanta  | 1111
-- Auckland |  942
```

## Résumé

Les bases de données relationnelles sont centrées sur la division des informations entre plusieurs tables, qui sont ensuite rassemblées pour l'affichage et l'analyse. Cela offre une grande flexibilité pour effectuer des calculs et manipuler les données. Vous avez vu les concepts fondamentaux d'une base de données relationnelle et comment effectuer une jointure entre deux tables.

## 🚀 Défi

Il existe de nombreuses bases de données relationnelles disponibles sur Internet. Vous pouvez explorer les données en utilisant les compétences que vous avez apprises ci-dessus.

## Quiz après le cours

## [Quiz après le cours](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/9)

## Révision et auto-apprentissage

Il existe plusieurs ressources disponibles sur [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) pour continuer votre exploration des concepts SQL et des bases de données relationnelles :

- [Décrire les concepts des données relationnelles](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Commencer à interroger avec Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL est une version de SQL)
- [Contenu SQL sur Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Devoir

[Titre du devoir](assignment.md)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.