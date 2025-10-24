<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:56:33+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "nl"
}
-->
# Luchthavendata weergeven

Je hebt een [database](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) gekregen, gebouwd op [SQLite](https://sqlite.org/index.html), die informatie over luchthavens bevat. Het schema wordt hieronder weergegeven. Je zult de [SQLite-extensie](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) in [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) gebruiken om informatie over luchthavens in verschillende steden weer te geven.

## Instructies

Om aan de slag te gaan met de opdracht, moet je een paar stappen uitvoeren. Je moet wat tools installeren en de voorbeelddatabase downloaden.

### Stel je systeem in

Je kunt Visual Studio Code en de SQLite-extensie gebruiken om met de database te werken.

1. Ga naar [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) en volg de instructies om Visual Studio Code te installeren.
1. Installeer de [SQLite-extensie](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) zoals aangegeven op de Marketplace-pagina.

### Download en open de database

Vervolgens download en open je de database.

1. Download het [databasebestand van GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) en sla het op in een map.
1. Open Visual Studio Code.
1. Open de database in de SQLite-extensie door **Ctrl-Shift-P** (of **Cmd-Shift-P** op een Mac) te selecteren en `SQLite: Open database` te typen.
1. Selecteer **Choose database from file** en open het bestand **airports.db** dat je eerder hebt gedownload.
1. Nadat je de database hebt geopend (je zult geen update op het scherm zien), maak je een nieuw query-venster door **Ctrl-Shift-P** (of **Cmd-Shift-P** op een Mac) te selecteren en `SQLite: New query` te typen.

Eenmaal geopend, kan het nieuwe query-venster worden gebruikt om SQL-verklaringen tegen de database uit te voeren. Je kunt de opdracht **Ctrl-Shift-Q** (of **Cmd-Shift-Q** op een Mac) gebruiken om queries tegen de database uit te voeren.

> [!NOTE] 
> Voor meer informatie over de SQLite-extensie kun je de [documentatie](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) raadplegen.

## Databaseschema

Het schema van een database is het ontwerp en de structuur van de tabellen. De **airports**-database heeft twee tabellen, `cities`, die een lijst bevat van steden in het Verenigd Koninkrijk en Ierland, en `airports`, die de lijst van alle luchthavens bevat. Omdat sommige steden meerdere luchthavens kunnen hebben, zijn er twee tabellen gemaakt om de informatie op te slaan. In deze oefening gebruik je joins om informatie voor verschillende steden weer te geven.

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
| city_id (FK naar id in **Cities**) |

## Opdracht

Maak queries om de volgende informatie op te halen:

1. alle stadsnamen in de `Cities`-tabel
1. alle steden in Ierland in de `Cities`-tabel
1. alle luchthaven namen met hun stad en land
1. alle luchthavens in Londen, Verenigd Koninkrijk

## Beoordelingscriteria

| Uitmuntend | Voldoende | Verbetering nodig |
| --------- | -------- | ----------------- |

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.