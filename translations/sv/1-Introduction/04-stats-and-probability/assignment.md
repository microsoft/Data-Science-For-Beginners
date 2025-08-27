<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01d1b493e8b51a6ebb42524f6b1bcfff",
  "translation_date": "2025-08-26T21:47:59+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/assignment.md",
  "language_code": "sv"
}
-->
# Liten Diabetesstudie

I denna uppgift kommer vi att arbeta med en liten dataset av diabetespatienter hämtad från [här](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

|   | ÅLDER | KÖN | BMI | BP | S1 | S2 | S3 | S4 | S5 | S6 | Y  |
|---|-------|-----|-----|----|----|----|----|----|----|----|----|
| 0 | 59    | 2   | 32.1 | 101. | 157 | 93.2 | 38.0 | 4. | 4.8598 | 87 | 151 |
| 1 | 48    | 1   | 21.6 | 87.0 | 183 | 103.2 | 70. | 3. | 3.8918 | 69 | 75 |
| 2 | 72    | 2   | 30.5 | 93.0 | 156 | 93.6 | 41.0 | 4.0 | 4. | 85 | 141 |
| ... | ... | ... | ... | ...| ...| ...| ...| ...| ...| ...| ... |

## Instruktioner

* Öppna [uppgiftsnotebooken](assignment.ipynb) i en jupyter notebook-miljö
* Slutför alla uppgifter som anges i notebooken, nämligen:
   * [ ] Beräkna medelvärden och varians för alla värden
   * [ ] Rita boxplots för BMI, BP och Y beroende på kön
   * [ ] Hur ser fördelningen ut för variablerna Ålder, Kön, BMI och Y?
   * [ ] Testa korrelationen mellan olika variabler och sjukdomsprogression (Y)
   * [ ] Testa hypotesen att graden av diabetesprogression skiljer sig mellan män och kvinnor
   
## Bedömningskriterier

Utmärkt | Tillräckligt | Behöver förbättras
--- | --- | -- |
Alla uppgifter är slutförda, grafiskt illustrerade och förklarade | De flesta uppgifter är slutförda, förklaringar eller slutsatser från grafer och/eller erhållna värden saknas | Endast grundläggande uppgifter som beräkning av medelvärde/varians och grundläggande grafer är slutförda, inga slutsatser dras från datan

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.