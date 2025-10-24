<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:58:42+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "hr"
}
-->
# Prikaz podataka o zračnim lukama

Dobili ste [bazu podataka](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) izgrađenu na [SQLite](https://sqlite.org/index.html) koja sadrži informacije o zračnim lukama. Shema baze podataka prikazana je dolje. Koristit ćete [SQLite ekstenziju](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) u [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) za prikaz informacija o zračnim lukama u različitim gradovima.

## Upute

Za početak zadatka, potrebno je izvršiti nekoliko koraka. Trebat ćete instalirati potrebne alate i preuzeti primjer baze podataka.

### Postavljanje sustava

Možete koristiti Visual Studio Code i SQLite ekstenziju za interakciju s bazom podataka.

1. Posjetite [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) i slijedite upute za instalaciju Visual Studio Code-a
1. Instalirajte [SQLite ekstenziju](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) prema uputama na stranici Marketplace-a

### Preuzimanje i otvaranje baze podataka

Sljedeći korak je preuzimanje i otvaranje baze podataka.

1. Preuzmite [datoteku baze podataka s GitHuba](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) i spremite je u direktorij
1. Otvorite Visual Studio Code
1. Otvorite bazu podataka u SQLite ekstenziji odabirom **Ctl-Shift-P** (ili **Cmd-Shift-P** na Macu) i upisivanjem `SQLite: Open database`
1. Odaberite **Choose database from file** i otvorite datoteku **airports.db** koju ste prethodno preuzeli
1. Nakon otvaranja baze podataka (nećete vidjeti promjenu na ekranu), kreirajte novi prozor za upite odabirom **Ctl-Shift-P** (ili **Cmd-Shift-P** na Macu) i upisivanjem `SQLite: New query`

Jednom otvoren, novi prozor za upite može se koristiti za pokretanje SQL naredbi protiv baze podataka. Možete koristiti naredbu **Ctl-Shift-Q** (ili **Cmd-Shift-Q** na Macu) za izvršavanje upita protiv baze podataka.

> [!NOTE] 
> Za više informacija o SQLite ekstenziji, možete konzultirati [dokumentaciju](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Shema baze podataka

Shema baze podataka predstavlja dizajn i strukturu tablica. Baza podataka **airports** ima dvije tablice, `cities`, koja sadrži popis gradova u Ujedinjenom Kraljevstvu i Irskoj, i `airports`, koja sadrži popis svih zračnih luka. Budući da neki gradovi mogu imati više zračnih luka, kreirane su dvije tablice za pohranu informacija. U ovom zadatku koristit ćete spajanja (joins) za prikaz informacija o različitim gradovima.

| Gradovi           |
| ----------------- |
| id (PK, integer)  |
| city (text)       |
| country (text)    |

| Zračne luke                     |
| ------------------------------- |
| id (PK, integer)                |
| name (text)                     |
| code (text)                     |
| city_id (FK prema id u **Gradovi**) |

## Zadatak

Kreirajte upite za prikaz sljedećih informacija:

1. svih imena gradova u tablici `Cities`
1. svih gradova u Irskoj u tablici `Cities`
1. svih imena zračnih luka s njihovim gradom i državom
1. svih zračnih luka u Londonu, Ujedinjeno Kraljevstvo

## Rubrika

| Izvrsno     | Zadovoljavajuće | Potrebno poboljšanje |
| ----------- | --------------- | -------------------- |

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.