<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-30T18:10:15+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "hr"
}
-->
# Zadatak za obradu podataka u Pythonu

U ovom zadatku tražimo od vas da razradite kod koji smo započeli razvijati u našim izazovima. Zadatak se sastoji od dva dijela:

## Modeliranje širenja COVID-19

 - [ ] Nacrtajte *R* grafove za 5-6 različitih zemalja na jednom grafu radi usporedbe, ili koristite nekoliko grafova jedan pored drugog.
 - [ ] Pogledajte kako broj smrtnih slučajeva i oporavaka korelira s brojem zaraženih slučajeva.
 - [ ] Utvrdite koliko dugo tipična bolest traje vizualno korelirajući stopu zaraze i stopu smrtnosti te tražeći neke anomalije. Možda ćete morati pogledati različite zemlje kako biste to otkrili.
 - [ ] Izračunajte stopu smrtnosti i kako se ona mijenja tijekom vremena. *Možda ćete htjeti uzeti u obzir trajanje bolesti u danima kako biste pomaknuli jednu vremensku seriju prije nego što napravite izračune.*

## Analiza radova o COVID-19

- [ ] Izgradite matricu ko-pojavljivanja različitih lijekova i pogledajte koji se lijekovi često pojavljuju zajedno (tj. spominju se u jednom sažetku). Možete modificirati kod za izgradnju matrice ko-pojavljivanja lijekova i dijagnoza.
- [ ] Vizualizirajte ovu matricu koristeći toplinsku kartu.
- [ ] Kao dodatni cilj, vizualizirajte ko-pojavljivanje lijekova koristeći [chord dijagram](https://en.wikipedia.org/wiki/Chord_diagram). [Ova biblioteka](https://pypi.org/project/chord/) može vam pomoći nacrtati chord dijagram.
- [ ] Kao još jedan dodatni cilj, izdvojite doze različitih lijekova (kao što je **400mg** u *uzimajte 400mg klorokina dnevno*) koristeći regularne izraze, i izgradite dataframe koji prikazuje različite doze za različite lijekove. **Napomena**: uzmite u obzir numeričke vrijednosti koje su u bliskom tekstualnom okruženju naziva lijeka.

## Rubrika

Izvrsno | Zadovoljavajuće | Potrebno poboljšanje
--- | --- | -- |
Svi zadaci su dovršeni, grafički ilustrirani i objašnjeni, uključujući barem jedan od dva dodatna cilja | Više od 5 zadataka je dovršeno, dodatni ciljevi nisu pokušani, ili rezultati nisu jasni | Manje od 5 (ali više od 3) zadataka je dovršeno, vizualizacije ne pomažu u demonstraciji poante

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.