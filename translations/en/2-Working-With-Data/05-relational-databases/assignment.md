<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-31T10:59:00+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "en"
}
-->
# Displaying airport data

You have been provided a [database](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) built on [SQLite](https://sqlite.org/index.html) which contains information about airports. The schema is shown below. You will use the [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) in [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) to display information about airports in various cities.

## Instructions

To begin the assignment, you'll need to complete a few steps. This involves installing some tools and downloading the sample database.

### Set up your system

You can use Visual Studio Code and the SQLite extension to interact with the database.

1. Go to [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) and follow the instructions to install Visual Studio Code.
1. Install the [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) as described on the Marketplace page.

### Download and open the database

Next, download and open the database.

1. Download the [database file from GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) and save it to a folder.
1. Open Visual Studio Code.
1. Open the database in the SQLite extension by pressing **Ctrl-Shift-P** (or **Cmd-Shift-P** on a Mac) and typing `SQLite: Open database`.
1. Select **Choose database from file** and open the **airports.db** file you downloaded earlier.
1. After opening the database (you won't see any visible changes on the screen), create a new query window by pressing **Ctrl-Shift-P** (or **Cmd-Shift-P** on a Mac) and typing `SQLite: New query`.

Once the query window is open, you can use it to execute SQL statements against the database. Use the command **Ctrl-Shift-Q** (or **Cmd-Shift-Q** on a Mac) to run queries on the database.

> [!NOTE] For more details about the SQLite extension, refer to the [documentation](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum).

## Database schema

A database's schema defines its table design and structure. The **airports** database contains two tables: `cities`, which lists cities in the United Kingdom and Ireland, and `airports`, which lists all airports. Since some cities may have multiple airports, two separate tables were created to store this information. In this exercise, you will use joins to display data for various cities.

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

## Assignment

Write queries to retrieve the following information:

1. All city names in the `Cities` table.
1. All cities in Ireland from the `Cities` table.
1. All airport names along with their city and country.
1. All airports located in London, United Kingdom.

## Rubric

| Exemplary | Adequate | Needs Improvement |
| --------- | -------- | ----------------- |

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.