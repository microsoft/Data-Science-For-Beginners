<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:57:37+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "hu"
}
-->
# Repülőtéri adatok megjelenítése

Egy [adatbázist](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) kaptál, amelyet [SQLite](https://sqlite.org/index.html) alapokra építettek, és repülőterekről tartalmaz információkat. Az adatbázis sémája az alábbiakban látható. A [SQLite kiterjesztést](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) fogod használni a [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) programban, hogy különböző városok repülőtereiről jeleníts meg információkat.

## Útmutató

Az feladat elkezdéséhez néhány lépést kell végrehajtanod. Telepítened kell néhány eszközt, és le kell töltened a mintaadatbázist.

### Rendszer beállítása

A Visual Studio Code és a SQLite kiterjesztés segítségével tudsz interakcióba lépni az adatbázissal.

1. Lépj a [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) oldalra, és kövesd az utasításokat a Visual Studio Code telepítéséhez
1. Telepítsd a [SQLite kiterjesztést](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) az utasítások szerint a Marketplace oldalán

### Az adatbázis letöltése és megnyitása

Ezután töltsd le és nyisd meg az adatbázist.

1. Töltsd le a [GitHubról származó adatbázis fájlt](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db), és mentsd el egy könyvtárba
1. Nyisd meg a Visual Studio Code-ot
1. Nyisd meg az adatbázist a SQLite kiterjesztésben úgy, hogy kiválasztod a **Ctl-Shift-P** (vagy **Cmd-Shift-P** Mac-en) parancsot, és begépeled a `SQLite: Open database` parancsot
1. Válaszd a **Choose database from file** opciót, és nyisd meg a korábban letöltött **airports.db** fájlt
1. Miután megnyitottad az adatbázist (nem fogsz látni frissítést a képernyőn), hozz létre egy új lekérdezési ablakot úgy, hogy kiválasztod a **Ctl-Shift-P** (vagy **Cmd-Shift-P** Mac-en) parancsot, és begépeled a `SQLite: New query` parancsot

Miután megnyitottad, az új lekérdezési ablakot SQL utasítások futtatására használhatod az adatbázis ellen. Az **Ctl-Shift-Q** (vagy **Cmd-Shift-Q** Mac-en) parancs segítségével futtathatsz lekérdezéseket az adatbázis ellen.

> [!NOTE] 
> További információért a SQLite kiterjesztésről, tekintsd meg a [dokumentációt](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Adatbázis séma

Egy adatbázis sémája az adatbázis tábláinak tervezése és struktúrája. Az **airports** adatbázis két táblát tartalmaz: `cities`, amely az Egyesült Királyság és Írország városainak listáját tartalmazza, és `airports`, amely az összes repülőtér listáját tartalmazza. Mivel egyes városoknak több repülőtere is lehet, két táblát hoztak létre az információk tárolására. Ebben a gyakorlatban csatlakozásokat fogsz használni, hogy különböző városok információit jelenítsd meg.

| Városok          |
| ---------------- |
| id (PK, integer) |
| city (text)      |
| country (text)   |

| Repülőterek                      |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK to id in **Cities**) |

## Feladat

Hozz létre lekérdezéseket, amelyek a következő információkat adják vissza:

1. az összes város neve a `Cities` táblában
1. az összes város Írországban a `Cities` táblában
1. az összes repülőtér neve a városukkal és országukkal együtt
1. az összes repülőtér Londonban, Egyesült Királyságban

## Értékelési szempontok

| Kiváló       | Megfelelő    | Fejlesztésre szorul |
| ------------ | ------------ | ------------------- |

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.