<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01d1b493e8b51a6ebb42524f6b1bcfff",
  "translation_date": "2025-08-31T05:56:25+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/assignment.md",
  "language_code": "lt"
}
-->
# Mažas diabeto tyrimas

Šioje užduotyje dirbsime su mažu diabeto pacientų duomenų rinkiniu, paimtu iš [čia](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

|   | AMŽIUS | LYTIS | KMI | KRAUJOSPŪDIS | S1 | S2 | S3 | S4 | S5 | S6 | Y  |
|---|--------|-------|-----|-------------|----|----|----|----|----|----|----|
| 0 | 59     | 2     | 32.1| 101.        | 157| 93.2| 38.0| 4. | 4.8598 | 87 | 151 |
| 1 | 48     | 1     | 21.6| 87.0        | 183| 103.2| 70. | 3. | 3.8918 | 69 | 75  |
| 2 | 72     | 2     | 30.5| 93.0        | 156| 93.6| 41.0| 4.0| 4.     | 85 | 141 |
| ... | ...  | ...   | ... | ...         | ...| ... | ... | ...| ...    | ...| ... |

## Instrukcijos

* Atidarykite [užduoties užrašų knygelę](assignment.ipynb) jupyter užrašų knygelės aplinkoje
* Atlikite visas užrašų knygelėje nurodytas užduotis, būtent:
   * [ ] Apskaičiuokite visų reikšmių vidurkius ir dispersijas
   * [ ] Nubraižykite dėžutinius grafikus (boxplots) KMI, kraujospūdžiui ir Y, atsižvelgiant į lytį
   * [ ] Kokia yra amžiaus, lyties, KMI ir Y kintamųjų pasiskirstymo forma?
   * [ ] Patikrinkite koreliaciją tarp skirtingų kintamųjų ir ligos progresavimo (Y)
   * [ ] Patikrinkite hipotezę, kad diabeto progresavimo laipsnis skiriasi tarp vyrų ir moterų

## Vertinimo kriterijai

Pavyzdingai | Pakankamai | Reikia patobulinimų
--- | --- | --- |
Visos reikalaujamos užduotys yra atliktos, grafiškai iliustruotos ir paaiškintos | Dauguma užduočių yra atliktos, tačiau trūksta paaiškinimų arba išvadų iš grafikų ir/arba gautų reikšmių | Atliktos tik pagrindinės užduotys, tokios kaip vidurkių/dispersijų skaičiavimas ir pagrindiniai grafikai, tačiau iš duomenų nėra padaryta jokių išvadų

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipiame dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudotis profesionalių vertėjų paslaugomis. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, kylančius dėl šio vertimo naudojimo.