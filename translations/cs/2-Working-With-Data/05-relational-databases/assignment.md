<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-26T14:33:05+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "cs"
}
-->
# Zobrazení údajů o letištích

Byla vám poskytnuta [databáze](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) vytvořená na základě [SQLite](https://sqlite.org/index.html), která obsahuje informace o letištích. Schéma databáze je uvedeno níže. Budete používat [rozšíření SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) v [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) pro zobrazení informací o letištích v různých městech.

## Instrukce

Abyste mohli začít s tímto úkolem, budete muset provést několik kroků. Budete potřebovat nainstalovat potřebné nástroje a stáhnout ukázkovou databázi.

### Nastavení systému

K interakci s databází můžete použít Visual Studio Code a rozšíření SQLite.

1. Přejděte na [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) a postupujte podle pokynů pro instalaci Visual Studio Code
1. Nainstalujte rozšíření [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) podle pokynů na stránce Marketplace

### Stažení a otevření databáze

Dále stáhněte a otevřete databázi.

1. Stáhněte si [soubor databáze z GitHubu](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) a uložte jej do nějaké složky
1. Otevřete Visual Studio Code
1. Otevřete databázi v rozšíření SQLite výběrem **Ctl-Shift-P** (nebo **Cmd-Shift-P** na Macu) a zadáním `SQLite: Open database`
1. Vyberte **Choose database from file** a otevřete soubor **airports.db**, který jste si stáhli
1. Po otevření databáze (na obrazovce se nezobrazí žádná aktualizace) vytvořte nové okno pro dotazy výběrem **Ctl-Shift-P** (nebo **Cmd-Shift-P** na Macu) a zadáním `SQLite: New query`

Jakmile je nové okno pro dotazy otevřené, můžete jej použít k provádění SQL příkazů proti databázi. K provádění dotazů můžete použít příkaz **Ctl-Shift-Q** (nebo **Cmd-Shift-Q** na Macu).

> [!NOTE] Další informace o rozšíření SQLite naleznete v [dokumentaci](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Schéma databáze

Schéma databáze představuje návrh a strukturu jejích tabulek. Databáze **airports** obsahuje dvě tabulky: `cities`, která obsahuje seznam měst ve Spojeném království a Irsku, a `airports`, která obsahuje seznam všech letišť. Protože některá města mohou mít více letišť, byly vytvořeny dvě tabulky pro uložení těchto informací. V tomto cvičení budete používat spojení (joins) k zobrazení informací o různých městech.

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

## Zadání

Vytvořte dotazy, které vrátí následující informace:

1. všechna jména měst v tabulce `Cities`
1. všechna města v Irsku v tabulce `Cities`
1. všechna jména letišť spolu s jejich městem a zemí
1. všechna letiště v Londýně, Spojené království

## Hodnocení

| Vynikající | Dostatečné | Potřebuje zlepšení |
| ---------- | ---------- | ------------------ |

---

**Upozornění**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.