<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-10-11T15:24:58+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "et"
}
-->
# Lennujaamade andmete kuvamine

Teile on antud [andmebaas](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db), mis on ehitatud [SQLite](https://sqlite.org/index.html) peale ja sisaldab teavet lennujaamade kohta. Skeem on allpool välja toodud. Kasutate [SQLite laiendust](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) [Visual Studio Code'is](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum), et kuvada teavet erinevate linnade lennujaamade kohta.

## Juhised

Ülesande alustamiseks peate tegema mõned sammud. Teil tuleb paigaldada vajalikud tööriistad ja alla laadida näidisandmebaas.

### Süsteemi seadistamine

Visual Studio Code'i ja SQLite laienduse abil saate andmebaasiga suhelda.

1. Minge lehele [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) ja järgige juhiseid Visual Studio Code'i paigaldamiseks
1. Paigaldage [SQLite laiendus](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) vastavalt Marketplace'i lehel toodud juhistele

### Andmebaasi allalaadimine ja avamine

Järgmisena laadige alla ja avage andmebaas.

1. Laadige [andmebaasi fail GitHubist](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) alla ja salvestage see kausta
1. Avage Visual Studio Code
1. Avage andmebaas SQLite laienduses, valides **Ctl-Shift-P** (või **Cmd-Shift-P** Macis) ja sisestades `SQLite: Open database`
1. Valige **Choose database from file** ja avage varem alla laaditud **airports.db** fail
1. Pärast andmebaasi avamist (ekraanil ei pruugi midagi muutuda) looge uus päringuaken, valides **Ctl-Shift-P** (või **Cmd-Shift-P** Macis) ja sisestades `SQLite: New query`

Kui päringuaken on avatud, saate SQL-lauseid andmebaasi vastu käivitada. Kasutage käsku **Ctl-Shift-Q** (või **Cmd-Shift-Q** Macis), et päringuid käivitada.

> [!NOTE] Lisateabe saamiseks SQLite laienduse kohta vaadake [dokumentatsiooni](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Andmebaasi skeem

Andmebaasi skeem on selle tabelite disain ja struktuur. **airports** andmebaasis on kaks tabelit: `cities`, mis sisaldab Ühendkuningriigi ja Iirimaa linnade loetelu, ja `airports`, mis sisaldab kõigi lennujaamade loetelu. Kuna mõnes linnas võib olla mitu lennujaama, loodi teabe salvestamiseks kaks tabelit. Selles ülesandes kasutate liitumisi, et kuvada teavet erinevate linnade kohta.

| Linnad            |
| ----------------- |
| id (PK, integer)  |
| city (text)       |
| country (text)    |

| Lennujaamad                      |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK to id in **Cities**) |

## Ülesanne

Looge päringud, et tagastada järgmine teave:

1. kõik linnanimed `Cities` tabelis
1. kõik Iirimaa linnad `Cities` tabelis
1. kõik lennujaamade nimed koos nende linna ja riigiga
1. kõik Londoni, Ühendkuningriigi lennujaamad

## Hindamiskriteeriumid

| Näidislik | Piisav | Vajab parandamist |
| --------- | ------ | ----------------- |

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsuse, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.