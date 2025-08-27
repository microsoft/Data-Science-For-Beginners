<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-26T20:52:16+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "no"
}
-->
# Vise flyplassdata

Du har fått tilgang til en [database](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) bygget på [SQLite](https://sqlite.org/index.html) som inneholder informasjon om flyplasser. Skjemaet vises nedenfor. Du skal bruke [SQLite-utvidelsen](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) i [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) for å vise informasjon om flyplasser i ulike byer.

## Instruksjoner

For å komme i gang med oppgaven må du utføre noen få trinn. Du må installere noen verktøy og laste ned eksempelbasen.

### Sett opp systemet ditt

Du kan bruke Visual Studio Code og SQLite-utvidelsen for å samhandle med databasen.

1. Gå til [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) og følg instruksjonene for å installere Visual Studio Code
1. Installer [SQLite-utvidelsen](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) som beskrevet på Marketplace-siden

### Last ned og åpne databasen

Deretter laster du ned og åpner databasen.

1. Last ned [databasefilen fra GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) og lagre den i en mappe
1. Åpne Visual Studio Code
1. Åpne databasen i SQLite-utvidelsen ved å velge **Ctrl-Shift-P** (eller **Cmd-Shift-P** på en Mac) og skrive `SQLite: Open database`
1. Velg **Choose database from file** og åpne **airports.db**-filen du lastet ned tidligere
1. Etter at databasen er åpnet (du vil ikke se en oppdatering på skjermen), opprett et nytt spørringsvindu ved å velge **Ctrl-Shift-P** (eller **Cmd-Shift-P** på en Mac) og skrive `SQLite: New query`

Når det nye spørringsvinduet er åpent, kan det brukes til å kjøre SQL-setninger mot databasen. Du kan bruke kommandoen **Ctrl-Shift-Q** (eller **Cmd-Shift-Q** på en Mac) for å kjøre spørringer mot databasen.

> [!NOTE] For mer informasjon om SQLite-utvidelsen kan du konsultere [dokumentasjonen](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Databaseskjema

Et databaseskjema er designet og strukturen til tabellene. **airports**-databasen har to tabeller, `cities`, som inneholder en liste over byer i Storbritannia og Irland, og `airports`, som inneholder en liste over alle flyplasser. Siden noen byer kan ha flere flyplasser, ble det opprettet to tabeller for å lagre informasjonen. I denne oppgaven vil du bruke joins for å vise informasjon for ulike byer.

| Cities           |
| ---------------- |
| id (PK, integer) |
| city (tekst)     |
| country (tekst)  |

| Airports                         |
| -------------------------------- |
| id (PK, integer)                 |
| name (tekst)                     |
| code (tekst)                     |
| city_id (FK til id i **Cities**) |

## Oppgave

Lag spørringer for å hente følgende informasjon:

1. alle bynavn i `Cities`-tabellen
1. alle byer i Irland i `Cities`-tabellen
1. alle flyplassnavn med deres by og land
1. alle flyplasser i London, Storbritannia

## Vurderingskriterier

| Fremragende | Tilfredsstillende | Trenger forbedring |
| ----------- | ----------------- | ------------------ |

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.