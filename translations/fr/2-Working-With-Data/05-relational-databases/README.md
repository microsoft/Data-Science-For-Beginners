<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80d80300002ef4e77cc7631d5904bd6e",
  "translation_date": "2025-10-25T18:32:46+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "fr"
}
-->
# Travailler avec les données : Bases de données relationnelles

|![ Sketchnote par [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Travailler avec les données : Bases de données relationnelles - _Sketchnote par [@nitya](https://twitter.com/nitya)_ |

Il y a de fortes chances que vous ayez déjà utilisé un tableur pour stocker des informations. Vous aviez un ensemble de lignes et de colonnes, où les lignes contenaient les informations (ou données), et les colonnes décrivaient ces informations (parfois appelées métadonnées). Une base de données relationnelle repose sur ce principe fondamental des colonnes et des lignes dans des tables, vous permettant de répartir les informations sur plusieurs tables. Cela vous permet de travailler avec des données plus complexes, d'éviter les doublons et d'avoir une flexibilité dans la manière dont vous explorez les données. Explorons les concepts d'une base de données relationnelle.

## [Quiz avant le cours](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Tout commence par des tables

Une base de données relationnelle repose sur des tables. Tout comme dans un tableur, une table est une collection de colonnes et de lignes. Les lignes contiennent les données ou informations avec lesquelles nous souhaitons travailler, comme le nom d'une ville ou la quantité de précipitations. Les colonnes décrivent les données qu'elles contiennent.

Commençons notre exploration en créant une table pour stocker des informations sur les villes. Nous pourrions commencer par leur nom et leur pays. Vous pourriez stocker cela dans une table comme suit :

| Ville    | Pays          |
| -------- | ------------- |
| Tokyo    | Japon         |
| Atlanta  | États-Unis    |
| Auckland | Nouvelle-Zélande |

Remarquez que les noms des colonnes **ville**, **pays** et **population** décrivent les données stockées, et chaque ligne contient des informations sur une ville.

## Les limites d'une approche avec une seule table

Il est probable que la table ci-dessus vous semble relativement familière. Commençons à ajouter des données supplémentaires à notre base de données en pleine croissance - les précipitations annuelles (en millimètres). Nous nous concentrerons sur les années 2018, 2019 et 2020. Si nous devions les ajouter pour Tokyo, cela pourrait ressembler à ceci :

| Ville | Pays   | Année | Quantité |
| ----- | ------ | ----- | -------- |
| Tokyo | Japon  | 2020  | 1690     |
| Tokyo | Japon  | 2019  | 1874     |
| Tokyo | Japon  | 2018  | 1445     |

Que remarquez-vous à propos de notre table ? Vous pourriez remarquer que nous dupliquons le nom et le pays de la ville encore et encore. Cela pourrait prendre beaucoup de stockage et il est largement inutile d'avoir plusieurs copies. Après tout, Tokyo n'a qu'un seul nom qui nous intéresse.

D'accord, essayons autre chose. Ajoutons de nouvelles colonnes pour chaque année :

| Ville    | Pays          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japon         | 1445 | 1874 | 1690 |
| Atlanta  | États-Unis    | 1779 | 1111 | 1683 |
| Auckland | Nouvelle-Zélande | 1386 | 942  | 1176 |

Bien que cela évite la duplication des lignes, cela ajoute quelques autres défis. Nous devrions modifier la structure de notre table chaque fois qu'une nouvelle année est ajoutée. De plus, à mesure que nos données augmentent, avoir nos années comme colonnes rendra plus difficile la récupération et le calcul des valeurs.

C'est pourquoi nous avons besoin de plusieurs tables et de relations. En divisant nos données, nous pouvons éviter les doublons et avoir plus de flexibilité dans la manière dont nous travaillons avec nos données.

## Les concepts de relations

Revenons à nos données et déterminons comment nous voulons les diviser. Nous savons que nous voulons stocker le nom et le pays de nos villes, donc cela fonctionnera probablement mieux dans une seule table.

| Ville    | Pays          |
| -------- | ------------- |
| Tokyo    | Japon         |
| Atlanta  | États-Unis    |
| Auckland | Nouvelle-Zélande |

Mais avant de créer la table suivante, nous devons déterminer comment référencer chaque ville. Nous avons besoin d'une forme d'identifiant, ID ou (en termes techniques de base de données) une clé primaire. Une clé primaire est une valeur utilisée pour identifier une ligne spécifique dans une table. Bien que cela puisse être basé sur une valeur elle-même (nous pourrions utiliser le nom de la ville, par exemple), cela devrait presque toujours être un numéro ou un autre identifiant. Nous ne voulons pas que l'identifiant change, car cela briserait la relation. Vous constaterez que dans la plupart des cas, la clé primaire ou l'identifiant sera un numéro généré automatiquement.

> ✅ La clé primaire est souvent abrégée en PK

### villes

| city_id | Ville    | Pays          |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japon         |
| 2       | Atlanta  | États-Unis    |
| 3       | Auckland | Nouvelle-Zélande |

> ✅ Vous remarquerez que nous utilisons les termes "id" et "clé primaire" de manière interchangeable pendant cette leçon. Les concepts ici s'appliquent aux DataFrames, que vous explorerez plus tard. Les DataFrames n'utilisent pas la terminologie de "clé primaire", cependant vous remarquerez qu'ils fonctionnent de manière similaire.

Avec notre table des villes créée, stockons les précipitations. Plutôt que de dupliquer les informations complètes sur la ville, nous pouvons utiliser l'identifiant. Nous devrions également nous assurer que la table nouvellement créée possède une colonne *id*, car toutes les tables devraient avoir un identifiant ou une clé primaire.

### précipitations

| rainfall_id | city_id | Année | Quantité |
| ----------- | ------- | ----- | -------- |
| 1           | 1       | 2018  | 1445     |
| 2           | 1       | 2019  | 1874     |
| 3           | 1       | 2020  | 1690     |
| 4           | 2       | 2018  | 1779     |
| 5           | 2       | 2019  | 1111     |
| 6           | 2       | 2020  | 1683     |
| 7           | 3       | 2018  | 1386     |
| 8           | 3       | 2019  | 942      |
| 9           | 3       | 2020  | 1176     |

Remarquez la colonne **city_id** dans la table nouvellement créée **précipitations**. Cette colonne contient des valeurs qui font référence aux identifiants dans la table **villes**. En termes techniques de données relationnelles, cela s'appelle une **clé étrangère** ; c'est une clé primaire d'une autre table. Vous pouvez simplement la considérer comme une référence ou un pointeur. **city_id** 1 fait référence à Tokyo.

> [!NOTE] 
> La clé étrangère est souvent abrégée en FK

## Récupérer les données

Avec nos données séparées en deux tables, vous vous demandez peut-être comment les récupérer. Si nous utilisons une base de données relationnelle comme MySQL, SQL Server ou Oracle, nous pouvons utiliser un langage appelé Structured Query Language ou SQL. SQL (parfois prononcé "sequel") est un langage standard utilisé pour récupérer et modifier des données dans une base de données relationnelle.

Pour récupérer des données, vous utilisez la commande `SELECT`. En gros, vous **sélectionnez** les colonnes que vous voulez voir **à partir de** la table dans laquelle elles se trouvent. Si vous voulez afficher uniquement les noms des villes, vous pouvez utiliser la commande suivante :

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` est l'endroit où vous listez les colonnes, et `FROM` est l'endroit où vous listez les tables.

> [!NOTE] 
> La syntaxe SQL n'est pas sensible à la casse, ce qui signifie que `select` et `SELECT` sont équivalents. Cependant, selon le type de base de données que vous utilisez, les colonnes et les tables peuvent être sensibles à la casse. Par conséquent, il est recommandé de toujours traiter tout en programmation comme étant sensible à la casse. Lors de l'écriture de requêtes SQL, la convention courante est de mettre les mots-clés en majuscules.

La requête ci-dessus affichera toutes les villes. Imaginons que nous voulions afficher uniquement les villes de Nouvelle-Zélande. Nous avons besoin d'une forme de filtre. Le mot-clé SQL pour cela est `WHERE`, ou "où quelque chose est vrai".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Joindre les données

Jusqu'à présent, nous avons récupéré des données à partir d'une seule table. Maintenant, nous voulons rassembler les données des tables **villes** et **précipitations**. Cela se fait en les *joignant* ensemble. Vous allez effectivement créer une liaison entre les deux tables et faire correspondre les valeurs d'une colonne de chaque table.

Dans notre exemple, nous allons faire correspondre la colonne **city_id** dans **précipitations** avec la colonne **city_id** dans **villes**. Cela associera la valeur des précipitations à sa ville respective. Le type de jointure que nous effectuerons est ce qu'on appelle une jointure *interne*, ce qui signifie que si des lignes ne correspondent pas à quelque chose de l'autre table, elles ne seront pas affichées. Dans notre cas, chaque ville a des précipitations, donc tout sera affiché.

Récupérons les précipitations de 2019 pour toutes nos villes.

Nous allons procéder par étapes. La première étape consiste à joindre les données en indiquant les colonnes pour la liaison - **city_id** comme mentionné précédemment.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Nous avons mis en évidence les deux colonnes que nous voulons, et le fait que nous voulons joindre les tables ensemble par **city_id**. Maintenant, nous pouvons ajouter l'instruction `WHERE` pour filtrer uniquement l'année 2019.

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

Les bases de données relationnelles sont centrées sur la division des informations entre plusieurs tables qui sont ensuite réunies pour l'affichage et l'analyse. Cela offre une grande flexibilité pour effectuer des calculs et manipuler les données. Vous avez vu les concepts fondamentaux d'une base de données relationnelle, et comment effectuer une jointure entre deux tables.

## 🚀 Défi

Il existe de nombreuses bases de données relationnelles disponibles sur Internet. Vous pouvez explorer les données en utilisant les compétences que vous avez apprises ci-dessus.

## Quiz après le cours

## [Quiz après le cours](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Révision et auto-apprentissage

Il existe plusieurs ressources disponibles sur [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) pour continuer votre exploration des concepts de SQL et des bases de données relationnelles.

- [Décrire les concepts des données relationnelles](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Commencer à interroger avec Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL est une version de SQL)
- [Contenu SQL sur Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Devoir

[Titre du devoir](assignment.md)

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.