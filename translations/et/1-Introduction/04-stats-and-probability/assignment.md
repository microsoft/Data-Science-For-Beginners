<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01d1b493e8b51a6ebb42524f6b1bcfff",
  "translation_date": "2025-10-11T15:44:40+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/assignment.md",
  "language_code": "et"
}
-->
# Väike Diabeediuuring

Selles ülesandes töötame väikese diabeedipatsientide andmestikuga, mis on võetud [siit](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

|   | VANUS | SUGU | KMI | VP | S1 | S2 | S3 | S4 | S5 | S6 | Y  |
|---|-------|------|-----|----|----|----|----|----|----|----|----|
| 0 | 59    | 2    | 32.1| 101.| 157| 93.2| 38.0| 4. | 4.8598 | 87 | 151 |
| 1 | 48    | 1    | 21.6| 87.0| 183| 103.2| 70. | 3. | 3.8918 | 69 | 75  |
| 2 | 72    | 2    | 30.5| 93.0| 156| 93.6| 41.0| 4.0| 4. | 85 | 141 |
| ... | ... | ...  | ... | ... | ...| ... | ... | ...| ... | ... | ... |

## Juhised

* Ava [ülesande märkmik](assignment.ipynb) Jupyter Notebooki keskkonnas
* Täida kõik märkmikus loetletud ülesanded, sealhulgas:
   * [ ] Arvuta kõigi väärtuste keskmised ja variatsioonid
   * [ ] Joonista kastdiagrammid KMI, VP ja Y jaoks sõltuvalt soost
   * [ ] Milline on vanuse, soo, KMI ja Y muutujate jaotus?
   * [ ] Testi erinevate muutujate ja haiguse progresseerumise (Y) vahelisi korrelatsioone
   * [ ] Testi hüpoteesi, et diabeedi progresseerumise aste on meestel ja naistel erinev

## Hindamiskriteeriumid

Eeskujulik | Piisav | Vajab Parandamist
--- | --- | --- |
Kõik nõutud ülesanded on täidetud, graafiliselt illustreeritud ja selgitatud | Enamik ülesandeid on täidetud, kuid graafikute ja/või saadud väärtuste selgitused või järeldused puuduvad | Täidetud on ainult põhiülesanded, nagu keskmise/variatsiooni arvutamine ja lihtsad graafikud, kuid andmetest järeldusi ei ole tehtud

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.