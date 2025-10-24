<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:59:49+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "et"
}
-->
# Lennujaamade andmete kuvamine

Teile on antud [andmebaas](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db), mis on loodud [SQLite](https://sqlite.org/index.html) abil ja sisaldab teavet lennujaamade kohta. Skeem on allpool kuvatud. Kasutate [SQLite laiendust](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) [Visual Studio Code'is](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum), et kuvada teavet erinevate linnade lennujaamade kohta.

## Juhised

Ülesande alustamiseks peate tegema mõned sammud. Teil tuleb paigaldada vajalikud tööriistad ja alla laadida näidisandmebaas.

### Süsteemi seadistamine

Andmebaasiga suhtlemiseks saate kasutada Visual Studio Code'i ja SQLite laiendust.

1. Minge lehele [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) ja järgige juhiseid Visual Studio Code'i paigaldamiseks
1. Paigaldage [SQLite laiendus](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) vastavalt juhistele Marketplace'i lehel

### Andmebaasi allalaadimine ja avamine

Järgmisena laadige alla ja avage andmebaas.

1. Laadige [GitHubist andmebaasifail](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) alla ja salvestage see kausta
1. Avage Visual Studio Code
1. Avage andmebaas SQLite laienduses, valides **Ctl-Shift-P** (või **Cmd-Shift-P** Macis) ja sisestades `SQLite: Open database`
1. Valige **Choose database from file** ja avage **airports.db** fail, mille te varem alla laadisite
1. Pärast andmebaasi avamist (ekraanil ei pruugi näha olla muudatusi), looge uus päringuaken, valides **Ctl-Shift-P** (või **Cmd-Shift-P** Macis) ja sisestades `SQLite: New query`

Kui päringuaken on avatud, saab seda kasutada SQL-i käskude täitmiseks andmebaasi vastu. Käskude täitmiseks andmebaasis saate kasutada käsku **Ctl-Shift-Q** (või **Cmd-Shift-Q** Macis).

> [!NOTE] 
> Lisateabe saamiseks SQLite laienduse kohta võite tutvuda [dokumentatsiooniga](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Andmebaasi skeem

Andmebaasi skeem on selle tabelite kujundus ja struktuur. **airports** andmebaasis on kaks tabelit: `cities`, mis sisaldab Ühendkuningriigi ja Iirimaa linnade loetelu, ja `airports`, mis sisaldab kõigi lennujaamade loetelu. Kuna mõnes linnas võib olla mitu lennujaama, loodi teabe salvestamiseks kaks tabelit. Selles harjutuses kasutate liitumisi, et kuvada teavet erinevate linnade kohta.

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
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.