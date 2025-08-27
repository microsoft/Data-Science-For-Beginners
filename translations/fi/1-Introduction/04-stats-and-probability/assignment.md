<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01d1b493e8b51a6ebb42524f6b1bcfff",
  "translation_date": "2025-08-26T21:48:30+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/assignment.md",
  "language_code": "fi"
}
-->
# Pieni diabetes-tutkimus

Tässä tehtävässä työskentelemme pienen diabetespotilaiden datasetin kanssa, joka on otettu [täältä](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

|   | IKÄ | SUKUPUOLI | BMI | BP | S1 | S2 | S3 | S4 | S5 | S6 | Y  |
|---|-----|-----------|-----|----|----|----|----|----|----|----|----|
| 0 | 59 | 2 | 32.1 | 101. | 157 | 93.2 | 38.0 | 4. | 4.8598 | 87 | 151 |
| 1 | 48 | 1 | 21.6 | 87.0 | 183 | 103.2 | 70. | 3. | 3.8918 | 69 | 75 |
| 2 | 72 | 2 | 30.5 | 93.0 | 156 | 93.6 | 41.0 | 4.0 | 4. | 85 | 141 |
| ... | ... | ... | ... | ...| ...| ...| ...| ...| ...| ...| ... |

## Ohjeet

* Avaa [tehtävänotebook](assignment.ipynb) jupyter-notebook-ympäristössä
* Suorita kaikki notebookissa listatut tehtävät, nimittäin:
   * [ ] Laske kaikkien arvojen keskiarvot ja varianssit
   * [ ] Piirrä laatikkokaaviot BMI-, BP- ja Y-arvoille sukupuolen mukaan
   * [ ] Mikä on ikä-, sukupuoli-, BMI- ja Y-muuttujien jakauma?
   * [ ] Testaa eri muuttujien ja sairauden etenemisen (Y) välinen korrelaatio
   * [ ] Testaa hypoteesi, että diabeteksen etenemisen aste eroaa miesten ja naisten välillä
   
## Arviointikriteerit

Erinomainen | Riittävä | Parannettavaa
--- | --- | -- |
Kaikki vaaditut tehtävät on suoritettu, graafisesti havainnollistettu ja selitetty | Suurin osa tehtävistä on suoritettu, mutta selitykset tai johtopäätökset graafeista ja/tai saaduista arvoista puuttuvat | Vain perusasiat, kuten keskiarvon/varianssin laskeminen ja peruskaaviot, on suoritettu, eikä datasta ole tehty johtopäätöksiä

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.