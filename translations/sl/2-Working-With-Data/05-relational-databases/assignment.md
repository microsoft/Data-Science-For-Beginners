<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:58:53+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "sl"
}
-->
# Prikaz podatkov o letališčih

Na voljo imate [bazo podatkov](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db), zgrajeno na [SQLite](https://sqlite.org/index.html), ki vsebuje informacije o letališčih. Shema je prikazana spodaj. Uporabili boste [razširitev SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) v [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) za prikaz informacij o letališčih v različnih mestih.

## Navodila

Za začetek naloge boste morali opraviti nekaj korakov. Namestiti boste morali nekaj orodij in prenesti vzorčno bazo podatkov.

### Priprava sistema

Za interakcijo z bazo podatkov lahko uporabite Visual Studio Code in razširitev SQLite.

1. Obiščite [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) in sledite navodilom za namestitev Visual Studio Code
1. Namestite razširitev [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum), kot je opisano na strani Marketplace

### Prenos in odpiranje baze podatkov

Nato prenesite in odprite bazo podatkov.

1. Prenesite [datoteko baze podatkov z GitHuba](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) in jo shranite v mapo
1. Odprite Visual Studio Code
1. Odprite bazo podatkov v razširitvi SQLite tako, da izberete **Ctl-Shift-P** (ali **Cmd-Shift-P** na Macu) in vnesete `SQLite: Open database`
1. Izberite **Choose database from file** in odprite datoteko **airports.db**, ki ste jo prej prenesli
1. Po odprtju baze podatkov (na zaslonu ne bo vidne posodobitve) ustvarite novo okno za poizvedbe tako, da izberete **Ctl-Shift-P** (ali **Cmd-Shift-P** na Macu) in vnesete `SQLite: New query`

Ko je okno odprto, ga lahko uporabite za izvajanje SQL stavkov proti bazi podatkov. Za izvajanje poizvedb proti bazi podatkov lahko uporabite ukaz **Ctl-Shift-Q** (ali **Cmd-Shift-Q** na Macu).

> [!NOTE] 
> Za več informacij o razširitvi SQLite si lahko ogledate [dokumentacijo](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Shema baze podatkov

Shema baze podatkov je zasnova in struktura njenih tabel. Baza podatkov **airports** ima dve tabeli, `cities`, ki vsebuje seznam mest v Združenem kraljestvu in na Irskem, ter `airports`, ki vsebuje seznam vseh letališč. Ker imajo nekatera mesta lahko več letališč, sta bili ustvarjeni dve tabeli za shranjevanje informacij. V tej nalogi boste uporabili združevanje za prikaz informacij za različna mesta.

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

## Naloga

Ustvarite poizvedbe za prikaz naslednjih informacij:

1. vseh imen mest v tabeli `Cities`
1. vseh mest na Irskem v tabeli `Cities`
1. vseh imen letališč z njihovim mestom in državo
1. vseh letališč v Londonu, Združenem kraljestvu

## Merila ocenjevanja

| Odlično | Zadostno | Potrebno izboljšanje |
| --------- | -------- | ----------------- |

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.