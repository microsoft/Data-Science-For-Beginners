<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01d1b493e8b51a6ebb42524f6b1bcfff",
  "translation_date": "2025-08-26T15:42:18+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/assignment.md",
  "language_code": "hu"
}
-->
# Kis Diabétesz Tanulmány

Ebben a feladatban egy kis diabéteszes betegek adatállományával fogunk dolgozni, amely innen származik: [here](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

|   | ÉLETKOR | NEM | BMI | VÉRNYOMÁS | S1 | S2 | S3 | S4 | S5 | S6 | Y  |
|---|---------|-----|-----|-----------|----|----|----|----|----|----|----|
| 0 | 59      | 2   | 32.1| 101.      | 157| 93.2| 38.0| 4. | 4.8598 | 87 | 151 |
| 1 | 48      | 1   | 21.6| 87.0      | 183| 103.2| 70. | 3. | 3.8918 | 69 | 75  |
| 2 | 72      | 2   | 30.5| 93.0      | 156| 93.6| 41.0| 4.0| 4. | 85 | 141 |
| ... | ...   | ... | ... | ...       | ...| ...| ...| ...| ...| ...| ... |

## Útmutató

* Nyisd meg a [feladat notebookot](assignment.ipynb) egy jupyter notebook környezetben
* Teljesítsd az összes feladatot, amelyek a notebookban szerepelnek, nevezetesen:
   * [ ] Számítsd ki az átlagértékeket és a szórást minden értékre
   * [ ] Készíts boxplotokat a BMI, vérnyomás és Y értékekről nemek szerint
   * [ ] Mi az Életkor, Nem, BMI és Y változók eloszlása?
   * [ ] Teszteld a korrelációt a különböző változók és a betegség előrehaladása (Y) között
   * [ ] Teszteld azt a hipotézist, hogy a diabétesz előrehaladásának mértéke eltér férfiak és nők között
   
## Értékelési szempontok

Kiemelkedő | Megfelelő | Fejlesztésre szorul
--- | --- | -- |
Minden szükséges feladat teljesítve, grafikusan illusztrálva és magyarázva | A legtöbb feladat teljesítve, magyarázatok vagy következtetések a grafikonokból és/vagy kapott értékekből hiányoznak | Csak alapfeladatok, mint az átlag/szórás számítása és alapvető grafikonok készítése teljesítve, nincs következtetés az adatokból

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.