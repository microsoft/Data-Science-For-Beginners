<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:57:49+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "cs"
}
-->
# Zobrazení dat o letištích

Byla vám poskytnuta [databáze](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) vytvořená na [SQLite](https://sqlite.org/index.html), která obsahuje informace o letištích. Schéma je zobrazeno níže. Budete používat [rozšíření SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) v [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) k zobrazení informací o letištích v různých městech.

## Pokyny

Abyste mohli začít s úkolem, budete muset provést několik kroků. Budete muset nainstalovat potřebné nástroje a stáhnout ukázkovou databázi.

### Nastavení systému

K interakci s databází můžete použít Visual Studio Code a rozšíření SQLite.

1. Přejděte na [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) a postupujte podle pokynů k instalaci Visual Studio Code
1. Nainstalujte rozšíření [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) podle pokynů na stránce Marketplace

### Stažení a otevření databáze

Dále stáhněte a otevřete databázi.

1. Stáhněte [soubor databáze z GitHubu](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) a uložte jej do adresáře
1. Otevřete Visual Studio Code
1. Otevřete databázi v rozšíření SQLite výběrem **Ctl-Shift-P** (nebo **Cmd-Shift-P** na Macu) a zadáním `SQLite: Open database`
1. Vyberte **Choose database from file** a otevřete soubor **airports.db**, který jste stáhli
1. Po otevření databáze (na obrazovce se nezobrazí žádná aktualizace) vytvořte nové okno dotazu výběrem **Ctl-Shift-P** (nebo **Cmd-Shift-P** na Macu) a zadáním `SQLite: New query`

Jakmile je okno dotazu otevřené, můžete jej použít k provádění SQL příkazů proti databázi. K provádění dotazů proti databázi můžete použít příkaz **Ctl-Shift-Q** (nebo **Cmd-Shift-Q** na Macu).

> [!NOTE] 
> Další informace o rozšíření SQLite naleznete v [dokumentaci](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Schéma databáze

Schéma databáze je návrh a struktura jejích tabulek. Databáze **airports** obsahuje dvě tabulky, `cities`, která obsahuje seznam měst ve Spojeném království a Irsku, a `airports`, která obsahuje seznam všech letišť. Protože některá města mohou mít více letišť, byly vytvořeny dvě tabulky pro uložení informací. V tomto cvičení budete používat spojení k zobrazení informací pro různá města.

| Města            |
| ---------------- |
| id (PK, integer) |
| city (text)      |
| country (text)   |

| Letiště                          |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK na id v **Cities**)  |

## Úkol

Vytvořte dotazy, které vrátí následující informace:

1. všechna jména měst v tabulce `Cities`
1. všechna města v Irsku v tabulce `Cities`
1. všechna jména letišť s jejich městem a zemí
1. všechna letiště v Londýně, Spojené království

## Hodnocení

| Vynikající | Přiměřené | Potřebuje zlepšení |
| ---------- | --------- | ----------------- |

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.