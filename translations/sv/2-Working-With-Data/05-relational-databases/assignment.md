<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:55:56+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "sv"
}
-->
# Visa flygplatsdata

Du har fått en [databas](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) byggd på [SQLite](https://sqlite.org/index.html) som innehåller information om flygplatser. Schemat visas nedan. Du kommer att använda [SQLite-tillägget](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) i [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) för att visa information om olika städers flygplatser.

## Instruktioner

För att komma igång med uppgiften behöver du utföra några steg. Du måste installera några verktyg och ladda ner exempeldatabasen.

### Ställ in ditt system

Du kan använda Visual Studio Code och SQLite-tillägget för att interagera med databasen.

1. Gå till [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) och följ instruktionerna för att installera Visual Studio Code
1. Installera [SQLite-tillägget](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) enligt instruktionerna på Marketplace-sidan

### Ladda ner och öppna databasen

Nästa steg är att ladda ner och öppna databasen.

1. Ladda ner [databasfilen från GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) och spara den i en katalog
1. Öppna Visual Studio Code
1. Öppna databasen i SQLite-tillägget genom att välja **Ctrl-Shift-P** (eller **Cmd-Shift-P** på en Mac) och skriva `SQLite: Open database`
1. Välj **Choose database from file** och öppna filen **airports.db** som du laddade ner tidigare
1. Efter att ha öppnat databasen (du kommer inte att se någon uppdatering på skärmen), skapa ett nytt frågefönster genom att välja **Ctrl-Shift-P** (eller **Cmd-Shift-P** på en Mac) och skriva `SQLite: New query`

När det nya frågefönstret är öppet kan det användas för att köra SQL-satser mot databasen. Du kan använda kommandot **Ctrl-Shift-Q** (eller **Cmd-Shift-Q** på en Mac) för att köra frågor mot databasen.

> [!NOTE] 
> För mer information om SQLite-tillägget kan du konsultera [dokumentationen](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Databasschema

En databas schema är dess tabelldesign och struktur. **airports**-databasen har två tabeller, `cities`, som innehåller en lista över städer i Storbritannien och Irland, och `airports`, som innehåller en lista över alla flygplatser. Eftersom vissa städer kan ha flera flygplatser skapades två tabeller för att lagra informationen. I denna övning kommer du att använda joins för att visa information för olika städer.

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
| city_id (FK till id i **Cities**) |

## Uppgift

Skapa frågor för att returnera följande information:

1. alla stadsnamn i tabellen `Cities`
1. alla städer i Irland i tabellen `Cities`
1. alla flygplatsnamn med deras stad och land
1. alla flygplatser i London, Storbritannien

## Bedömningskriterier

| Exemplariskt | Tillräckligt | Behöver förbättras |
| ------------ | ------------ | ------------------ |

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.