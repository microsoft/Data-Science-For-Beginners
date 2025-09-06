<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-26T14:33:42+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "ro"
}
-->
# Afișarea datelor despre aeroporturi

Vi s-a pus la dispoziție o [bază de date](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) construită pe [SQLite](https://sqlite.org/index.html), care conține informații despre aeroporturi. Schema este afișată mai jos. Veți utiliza [extensia SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) în [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) pentru a afișa informații despre aeroporturile din diferite orașe.

## Instrucțiuni

Pentru a începe această sarcină, va trebui să urmați câțiva pași. Va trebui să instalați câteva instrumente și să descărcați baza de date de exemplu.

### Configurați sistemul

Puteți utiliza Visual Studio Code și extensia SQLite pentru a interacționa cu baza de date.

1. Accesați [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) și urmați instrucțiunile pentru a instala Visual Studio Code
1. Instalați [extensia SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) conform instrucțiunilor de pe pagina Marketplace

### Descărcați și deschideți baza de date

În continuare, veți descărca și deschide baza de date.

1. Descărcați [fișierul bazei de date de pe GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) și salvați-l într-un director
1. Deschideți Visual Studio Code
1. Deschideți baza de date în extensia SQLite selectând **Ctl-Shift-P** (sau **Cmd-Shift-P** pe Mac) și tastând `SQLite: Open database`
1. Selectați **Choose database from file** și deschideți fișierul **airports.db** pe care l-ați descărcat anterior
1. După ce ați deschis baza de date (nu veți vedea o actualizare pe ecran), creați o fereastră nouă de interogare selectând **Ctl-Shift-P** (sau **Cmd-Shift-P** pe Mac) și tastând `SQLite: New query`

Odată deschisă, fereastra nouă de interogare poate fi utilizată pentru a rula instrucțiuni SQL împotriva bazei de date. Puteți utiliza comanda **Ctl-Shift-Q** (sau **Cmd-Shift-Q** pe Mac) pentru a rula interogări împotriva bazei de date.

> [!NOTE] Pentru mai multe informații despre extensia SQLite, puteți consulta [documentația](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Schema bazei de date

Schema unei baze de date reprezintă designul și structura tabelelor sale. Baza de date **airports** are două tabele, `cities`, care conține o listă de orașe din Regatul Unit și Irlanda, și `airports`, care conține lista tuturor aeroporturilor. Deoarece unele orașe pot avea mai multe aeroporturi, au fost create două tabele pentru a stoca informațiile. În acest exercițiu veți utiliza operațiuni de tip join pentru a afișa informații despre diferite orașe.

| Orașe            |
| ---------------- |
| id (PK, integer) |
| city (text)      |
| country (text)   |

| Aeroporturi                      |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK către id în **Orașe**) |

## Sarcină

Creați interogări pentru a returna următoarele informații:

1. toate numele orașelor din tabelul `Cities`
1. toate orașele din Irlanda din tabelul `Cities`
1. toate numele aeroporturilor împreună cu orașul și țara lor
1. toate aeroporturile din Londra, Regatul Unit

## Criterii de evaluare

| Exemplu | Adecvat | Necesită îmbunătățiri |
| ------- | ------- | --------------------- |

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.