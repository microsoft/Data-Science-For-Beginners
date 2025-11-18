<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-11-18T18:24:14+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "pcm"
}
-->
# How to show airport data

Dem don give you one [database](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) wey dey use [SQLite](https://sqlite.org/index.html) wey get info about airports. The schema dey show for down. You go use the [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) for [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) to show info about airports for different cities.

## Wetin you go do

To start this assignment, you go need do some steps. You go need install some tools and download the sample database.

### Set up your system

You fit use Visual Studio Code and the SQLite extension to work with the database.

1. Go [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) and follow the instructions to install Visual Studio Code
1. Install the [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) extension as dem talk for the Marketplace page

### Download and open the database

Next, you go download and open the database.

1. Download the [database file from GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) and save am for one folder
1. Open Visual Studio Code
1. Open the database for the SQLite extension by pressing **Ctl-Shift-P** (or **Cmd-Shift-P** if na Mac) and type `SQLite: Open database`
1. Choose **Choose database from file** and open the **airports.db** file wey you download before
1. After you don open the database (you no go see any update for the screen), create new query window by pressing **Ctl-Shift-P** (or **Cmd-Shift-P** if na Mac) and type `SQLite: New query`

Once you don open am, the new query window fit dey use to run SQL statements for the database. You fit use the command **Ctl-Shift-Q** (or **Cmd-Shift-Q** if na Mac) to run queries for the database.

> [!NOTE] 
> If you want know more about the SQLite extension, you fit check the [documentation](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Database schema

Database schema na how dem design and structure the table. The **airports** database get two tables, `cities`, wey get list of cities for United Kingdom and Ireland, and `airports`, wey get list of all airports. Because some cities fit get plenty airports, dem create two tables to store the info. For this exercise, you go use joins to show info for different cities.

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
| city_id (FK to id in **Cities**) |

## Wetin you go do

Create queries wey go show this info:

1. all city names for the `Cities` table
1. all cities for Ireland for the `Cities` table
1. all airport names with their city and country
1. all airports for London, United Kingdom

## How dem go mark am

| Exemplary | Adequate | Needs Improvement |
| --------- | -------- | ----------------- |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go trust. For important mata, na beta make you use professional human translation. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->