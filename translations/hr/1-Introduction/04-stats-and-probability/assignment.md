<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01d1b493e8b51a6ebb42524f6b1bcfff",
  "translation_date": "2025-08-30T19:26:15+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/assignment.md",
  "language_code": "hr"
}
-->
# Mala studija o dijabetesu

U ovom zadatku radit ćemo s malim skupom podataka o pacijentima s dijabetesom preuzetim s [ovdje](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

|   | DOB | SPOL | BMI | KR | S1 | S2 | S3 | S4 | S5 | S6 | Y  |
|---|-----|------|-----|----|----|----|----|----|----|----|----|
| 0 | 59  | 2    | 32.1| 101.| 157| 93.2| 38.0| 4. | 4.8598| 87 | 151 |
| 1 | 48  | 1    | 21.6| 87.0| 183| 103.2| 70. | 3. | 3.8918| 69 | 75  |
| 2 | 72  | 2    | 30.5| 93.0| 156| 93.6| 41.0| 4.0| 4.     | 85 | 141 |
| ... | ... | ...  | ... | ... | ...| ... | ... | ...| ...   | ...| ... |

## Upute

* Otvorite [bilježnicu zadatka](assignment.ipynb) u jupyter notebook okruženju
* Dovršite sve zadatke navedene u bilježnici, i to:
   * [ ] Izračunajte srednje vrijednosti i varijancu za sve vrijednosti
   * [ ] Nacrtajte boxplotove za BMI, KR i Y ovisno o spolu
   * [ ] Koja je distribucija varijabli Dob, Spol, BMI i Y?
   * [ ] Testirajte korelaciju između različitih varijabli i progresije bolesti (Y)
   * [ ] Testirajte hipotezu da se stupanj progresije dijabetesa razlikuje između muškaraca i žena

## Rubrika

Izvrsno | Zadovoljavajuće | Potrebna poboljšanja
--- | --- | -- |
Svi zadaci su dovršeni, grafički prikazani i objašnjeni | Većina zadataka je dovršena, ali nedostaju objašnjenja ili zaključci iz grafova i/ili dobivenih vrijednosti | Dovršeni su samo osnovni zadaci poput izračuna srednje vrijednosti/varijance i osnovnih grafova, bez zaključaka iz podataka

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.