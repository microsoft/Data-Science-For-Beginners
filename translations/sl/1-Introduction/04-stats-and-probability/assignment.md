<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01d1b493e8b51a6ebb42524f6b1bcfff",
  "translation_date": "2025-08-30T19:26:25+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/assignment.md",
  "language_code": "sl"
}
-->
# Majhna študija o diabetesu

V tej nalogi bomo delali z majhnim naborom podatkov o bolnikih z diabetesom, ki je vzet iz [tukaj](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

|   | STAROST | SPOL | ITM | KR | S1 | S2 | S3 | S4 | S5 | S6 | Y  |
|---|---------|------|-----|----|----|----|----|----|----|----|----|
| 0 | 59 | 2 | 32.1 | 101. | 157 | 93.2 | 38.0 | 4. | 4.8598 | 87 | 151 |
| 1 | 48 | 1 | 21.6 | 87.0 | 183 | 103.2 | 70. | 3. | 3.8918 | 69 | 75 |
| 2 | 72 | 2 | 30.5 | 93.0 | 156 | 93.6 | 41.0 | 4.0 | 4. | 85 | 141 |
| ... | ... | ... | ... | ...| ...| ...| ...| ...| ...| ...| ... |

## Navodila

* Odprite [zvezek z nalogo](assignment.ipynb) v okolju jupyter notebook
* Izpolnite vse naloge, navedene v zvezku, in sicer:
   * [ ] Izračunajte povprečne vrednosti in varianco za vse vrednosti
   * [ ] Narišite boxplote za ITM, KR in Y glede na spol
   * [ ] Kakšna je porazdelitev spremenljivk Starost, Spol, ITM in Y?
   * [ ] Preverite korelacijo med različnimi spremenljivkami in napredovanjem bolezni (Y)
   * [ ] Preverite hipotezo, da je stopnja napredovanja diabetesa različna med moškimi in ženskami
   
## Merila ocenjevanja

Odlično | Zadostno | Potrebno izboljšanje
--- | --- | -- |
Vse zahtevane naloge so izpolnjene, grafično prikazane in razložene | Večina nalog je izpolnjenih, manjkajo razlage ali sklepi iz grafov in/ali pridobljenih vrednosti | Izpolnjene so le osnovne naloge, kot so izračun povprečja/variance in osnovni grafi, brez sklepov iz podatkov

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.