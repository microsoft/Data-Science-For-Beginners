<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:56:05+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "da"
}
-->
# Vise lufthavnsdata

Du har fået en [database](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) bygget på [SQLite](https://sqlite.org/index.html), som indeholder information om lufthavne. Skemaet vises nedenfor. Du vil bruge [SQLite-udvidelsen](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) i [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) til at vise information om forskellige byers lufthavne.

## Instruktioner

For at komme i gang med opgaven skal du udføre et par trin. Du skal installere nogle værktøjer og downloade den eksempeldatabase.

### Opsætning af dit system

Du kan bruge Visual Studio Code og SQLite-udvidelsen til at interagere med databasen.

1. Gå til [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) og følg instruktionerne for at installere Visual Studio Code
1. Installer [SQLite-udvidelsen](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) som beskrevet på Marketplace-siden

### Download og åbn databasen

Dernæst skal du downloade og åbne databasen.

1. Download [databasefilen fra GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) og gem den i en mappe
1. Åbn Visual Studio Code
1. Åbn databasen i SQLite-udvidelsen ved at vælge **Ctrl-Shift-P** (eller **Cmd-Shift-P** på en Mac) og skrive `SQLite: Open database`
1. Vælg **Choose database from file** og åbn **airports.db**-filen, du downloadede tidligere
1. Efter åbning af databasen (du vil ikke se en opdatering på skærmen), opret et nyt forespørgselsvindue ved at vælge **Ctrl-Shift-P** (eller **Cmd-Shift-P** på en Mac) og skrive `SQLite: New query`

Når det nye forespørgselsvindue er åbent, kan det bruges til at køre SQL-udsagn mod databasen. Du kan bruge kommandoen **Ctrl-Shift-Q** (eller **Cmd-Shift-Q** på en Mac) til at køre forespørgsler mod databasen.

> [!NOTE] 
> For mere information om SQLite-udvidelsen kan du konsultere [dokumentationen](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Databaseskema

Et databaseskema er dets tabeldesign og struktur. **airports**-databasen har to tabeller, `cities`, som indeholder en liste over byer i Storbritannien og Irland, og `airports`, som indeholder listen over alle lufthavne. Fordi nogle byer kan have flere lufthavne, blev der oprettet to tabeller til at gemme informationen. I denne øvelse vil du bruge joins til at vise information for forskellige byer.

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
| city_id (FK til id i **Cities**) |

## Opgave

Opret forespørgsler for at returnere følgende information:

1. alle bynavne i `Cities`-tabellen
1. alle byer i Irland i `Cities`-tabellen
1. alle lufthavnsnavne med deres by og land
1. alle lufthavne i London, Storbritannien

## Bedømmelseskriterier

| Fremragende | Tilstrækkelig | Kræver forbedring |
| ----------- | ------------- | ----------------- |

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.