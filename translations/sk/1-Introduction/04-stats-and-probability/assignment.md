<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01d1b493e8b51a6ebb42524f6b1bcfff",
  "translation_date": "2025-08-26T15:42:44+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/assignment.md",
  "language_code": "sk"
}
-->
# Malá štúdia o cukrovke

V tejto úlohe budeme pracovať s malým datasetom pacientov s cukrovkou, ktorý je prevzatý z [tohto odkazu](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

|   | VEK | POHLAVIE | BMI | TK | S1 | S2 | S3 | S4 | S5 | S6 | Y  |
|---|-----|----------|-----|----|----|----|----|----|----|----|----|
| 0 | 59 | 2 | 32.1 | 101. | 157 | 93.2 | 38.0 | 4. | 4.8598 | 87 | 151 |
| 1 | 48 | 1 | 21.6 | 87.0 | 183 | 103.2 | 70. | 3. | 3.8918 | 69 | 75 |
| 2 | 72 | 2 | 30.5 | 93.0 | 156 | 93.6 | 41.0 | 4.0 | 4. | 85 | 141 |
| ... | ... | ... | ... | ...| ...| ...| ...| ...| ...| ...| ... |

## Pokyny

* Otvorte [notebook k úlohe](assignment.ipynb) v prostredí jupyter notebook
* Dokončite všetky úlohy uvedené v notebooku, konkrétne:
   * [ ] Vypočítajte priemerné hodnoty a rozptyl pre všetky hodnoty
   * [ ] Vytvorte boxploty pre BMI, TK a Y v závislosti od pohlavia
   * [ ] Aké je rozdelenie premenných Vek, Pohlavie, BMI a Y?
   * [ ] Otestujte koreláciu medzi rôznymi premennými a progresiou ochorenia (Y)
   * [ ] Otestujte hypotézu, že miera progresie cukrovky sa líši medzi mužmi a ženami
   
## Hodnotiace kritériá

Vynikajúce | Dostatočné | Potrebuje zlepšenie
--- | --- | -- |
Všetky požadované úlohy sú dokončené, graficky znázornené a vysvetlené | Väčšina úloh je dokončená, chýbajú vysvetlenia alebo závery z grafov a/alebo získaných hodnôt | Dokončené sú iba základné úlohy, ako výpočet priemeru/rozptylu a základné grafy, z dát nie sú vyvodené žiadne závery

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.