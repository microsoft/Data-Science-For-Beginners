<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-25T16:17:34+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "fr"
}
-->
# Affichage des données des aéroports

On vous a fourni une [base de données](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) construite sur [SQLite](https://sqlite.org/index.html) qui contient des informations sur les aéroports. Le schéma est affiché ci-dessous. Vous utiliserez l'[extension SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) dans [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) pour afficher des informations sur les aéroports de différentes villes.

## Instructions

Pour commencer cet exercice, vous devrez effectuer quelques étapes. Vous devrez installer certains outils et télécharger la base de données d'exemple.

### Configurez votre système

Vous pouvez utiliser Visual Studio Code et l'extension SQLite pour interagir avec la base de données.

1. Rendez-vous sur [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) et suivez les instructions pour installer Visual Studio Code  
1. Installez l'[extension SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) comme indiqué sur la page du Marketplace  

### Téléchargez et ouvrez la base de données

Ensuite, vous téléchargerez et ouvrirez la base de données.

1. Téléchargez le [fichier de base de données depuis GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) et enregistrez-le dans un répertoire  
1. Ouvrez Visual Studio Code  
1. Ouvrez la base de données dans l'extension SQLite en sélectionnant **Ctrl-Shift-P** (ou **Cmd-Shift-P** sur un Mac) et en tapant `SQLite: Open database`  
1. Sélectionnez **Choose database from file** et ouvrez le fichier **airports.db** que vous avez téléchargé précédemment  
1. Après avoir ouvert la base de données (vous ne verrez pas de mise à jour à l'écran), créez une nouvelle fenêtre de requête en sélectionnant **Ctrl-Shift-P** (ou **Cmd-Shift-P** sur un Mac) et en tapant `SQLite: New query`  

Une fois ouverte, la nouvelle fenêtre de requête peut être utilisée pour exécuter des instructions SQL sur la base de données. Vous pouvez utiliser la commande **Ctrl-Shift-Q** (ou **Cmd-Shift-Q** sur un Mac) pour exécuter des requêtes sur la base de données.

> [!NOTE] Pour plus d'informations sur l'extension SQLite, vous pouvez consulter la [documentation](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Schéma de la base de données

Le schéma d'une base de données correspond à la conception et à la structure de ses tables. La base de données **airports** contient deux tables : `cities`, qui contient une liste de villes au Royaume-Uni et en Irlande, et `airports`, qui contient la liste de tous les aéroports. Comme certaines villes peuvent avoir plusieurs aéroports, deux tables ont été créées pour stocker les informations. Dans cet exercice, vous utiliserez des jointures pour afficher des informations sur différentes villes.

| Cities           |
| ---------------- |
| id (PK, integer) |
| city (text)      |
| country (text)   |

| Airports                         |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK vers id dans **Cities**) |

## Exercice

Créez des requêtes pour retourner les informations suivantes :

1. tous les noms de villes dans la table `Cities`  
1. toutes les villes en Irlande dans la table `Cities`  
1. tous les noms d'aéroports avec leur ville et leur pays  
1. tous les aéroports à Londres, Royaume-Uni  

## Grille d'évaluation

| Exemplaire | Adéquat  | À améliorer       |
| ---------- | -------- | ----------------- |

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.