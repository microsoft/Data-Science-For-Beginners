<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:58:01+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "sk"
}
-->
# Zobrazenie údajov o letiskách

Dostali ste [databázu](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) postavenú na [SQLite](https://sqlite.org/index.html), ktorá obsahuje informácie o letiskách. Schéma je zobrazená nižšie. Použijete [rozšírenie SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) v [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) na zobrazenie informácií o letiskách v rôznych mestách.

## Pokyny

Aby ste mohli začať s úlohou, budete musieť vykonať niekoľko krokov. Budete musieť nainštalovať niekoľko nástrojov a stiahnuť ukážkovú databázu.

### Nastavenie systému

Na interakciu s databázou môžete použiť Visual Studio Code a rozšírenie SQLite.

1. Prejdite na [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) a postupujte podľa pokynov na inštaláciu Visual Studio Code
1. Nainštalujte rozšírenie [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) podľa pokynov na stránke Marketplace

### Stiahnutie a otvorenie databázy

Ďalej si stiahnete a otvoríte databázu.

1. Stiahnite si [databázový súbor z GitHubu](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) a uložte ho do adresára
1. Otvorte Visual Studio Code
1. Otvorte databázu v rozšírení SQLite výberom **Ctl-Shift-P** (alebo **Cmd-Shift-P** na Macu) a zadaním `SQLite: Open database`
1. Vyberte **Choose database from file** a otvorte súbor **airports.db**, ktorý ste si predtým stiahli
1. Po otvorení databázy (na obrazovke neuvidíte žiadnu aktualizáciu), vytvorte nové okno pre dotazy výberom **Ctl-Shift-P** (alebo **Cmd-Shift-P** na Macu) a zadaním `SQLite: New query`

Po otvorení môžete nové okno pre dotazy použiť na spúšťanie SQL príkazov proti databáze. Na spustenie dotazov proti databáze môžete použiť príkaz **Ctl-Shift-Q** (alebo **Cmd-Shift-Q** na Macu).

> [!NOTE] 
> Viac informácií o rozšírení SQLite nájdete v [dokumentácii](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Schéma databázy

Schéma databázy je návrh a štruktúra jej tabuliek. Databáza **airports** obsahuje dve tabuľky, `cities`, ktorá obsahuje zoznam miest v Spojenom kráľovstve a Írsku, a `airports`, ktorá obsahuje zoznam všetkých letísk. Keďže niektoré mestá môžu mať viacero letísk, boli vytvorené dve tabuľky na uloženie informácií. V tomto cvičení použijete spojenia na zobrazenie informácií pre rôzne mestá.

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

## Úloha

Vytvorte dotazy na získanie nasledujúcich informácií:

1. všetky názvy miest v tabuľke `Cities`
1. všetky mestá v Írsku v tabuľke `Cities`
1. všetky názvy letísk spolu s ich mestom a krajinou
1. všetky letiská v Londýne, Spojené kráľovstvo

## Hodnotenie

| Vynikajúce | Dostatočné | Potrebuje zlepšenie |
| --------- | -------- | ----------------- |

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.