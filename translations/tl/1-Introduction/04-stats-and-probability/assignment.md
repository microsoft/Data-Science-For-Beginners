<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01d1b493e8b51a6ebb42524f6b1bcfff",
  "translation_date": "2025-08-28T02:44:16+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/assignment.md",
  "language_code": "tl"
}
-->
# Maliit na Pag-aaral Tungkol sa Diabetes

Sa gawaing ito, gagamit tayo ng maliit na dataset ng mga pasyenteng may diabetes na kinuha mula [dito](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

|   | EDAD | KASARIAN | BMI | BP | S1 | S2 | S3 | S4 | S5 | S6 | Y  |
|---|------|----------|-----|----|----|----|----|----|----|----|----|
| 0 | 59   | 2        | 32.1| 101.| 157| 93.2| 38.0| 4. | 4.8598 | 87 | 151 |
| 1 | 48   | 1        | 21.6| 87.0| 183| 103.2| 70. | 3. | 3.8918 | 69 | 75  |
| 2 | 72   | 2        | 30.5| 93.0| 156| 93.6| 41.0| 4.0| 4. | 85 | 141 |
| ... | ... | ...      | ... | ...| ...| ...| ...| ...| ...| ...| ... |

## Mga Panuto

* Buksan ang [assignment notebook](assignment.ipynb) sa isang jupyter notebook na kapaligiran
* Kumpletuhin ang lahat ng mga gawain na nakalista sa notebook, kabilang ang:
   * [ ] Kalkulahin ang mga mean na halaga at variance para sa lahat ng mga halaga
   * [ ] Gumawa ng mga boxplot para sa BMI, BP, at Y batay sa kasarian
   * [ ] Ano ang distribusyon ng mga variable na Edad, Kasarian, BMI, at Y?
   * [ ] Subukan ang ugnayan sa pagitan ng iba't ibang mga variable at ng pag-usad ng sakit (Y)
   * [ ] Subukan ang hypothesis na ang antas ng pag-usad ng diabetes ay magkaiba sa pagitan ng mga lalaki at babae
   
## Rubric

Natatangi | Katanggap-tanggap | Kailangan ng Pagpapabuti
--- | --- | --- |
Lahat ng kinakailangang gawain ay kumpleto, may grapikong presentasyon at paliwanag | Karamihan sa mga gawain ay kumpleto, ngunit kulang ang mga paliwanag o takeaway mula sa mga graph at/o nakuhang mga halaga | Tanging mga pangunahing gawain tulad ng pagkalkula ng mean/variance at mga pangunahing plot ang kumpleto, walang konklusyon na ginawa mula sa datos

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.