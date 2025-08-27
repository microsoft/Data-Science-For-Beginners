<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-26T21:07:48+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "fi"
}
-->
# Tehtävä: Datan käsittely Pythonilla

Tässä tehtävässä pyydämme sinua jatkamaan koodin kehittämistä, jota olemme aloittaneet haasteissamme. Tehtävä koostuu kahdesta osasta:

## COVID-19:n leviämisen mallintaminen

 - [ ] Piirrä *R* -graafit 5-6 eri maalle joko yhdelle graafille vertailua varten tai useille graafeille rinnakkain.
 - [ ] Tutki, miten kuolemien ja parantumisten määrä korreloi tartuntojen määrän kanssa.
 - [ ] Selvitä, kuinka kauan tyypillinen tauti kestää visuaalisesti korreloimalla tartuntatahti ja kuolemantapausten tahti sekä etsimällä poikkeavuuksia. Saatat joutua tarkastelemaan eri maita saadaksesi selville tämän.
 - [ ] Laske kuolleisuusaste ja miten se muuttuu ajan myötä. *Saatat haluta ottaa huomioon taudin keston päivissä ja siirtää yhtä aikasarjaa ennen laskelmien tekemistä.*

## COVID-19-tutkimusten analyysi

- [ ] Rakenna yhteisesiintymismatriisi eri lääkkeistä ja tutki, mitkä lääkkeet esiintyvät usein yhdessä (eli mainitaan samassa tiivistelmässä). Voit muokata koodia lääkkeiden ja diagnoosien yhteisesiintymismatriisin rakentamiseksi.
- [ ] Visualisoi tämä matriisi lämpökartalla.
- [ ] Lisätehtävänä visualisoi lääkkeiden yhteisesiintyminen [chord diagram](https://en.wikipedia.org/wiki/Chord_diagram) -kaaviolla. [Tämä kirjasto](https://pypi.org/project/chord/) voi auttaa sinua piirtämään chord diagram -kaavion.
- [ ] Toinen lisätehtävä: Etsi eri lääkkeiden annostuksia (kuten **400mg** kohdassa *ota 400mg klorokiinia päivittäin*) käyttämällä säännöllisiä lausekkeita ja rakenna dataframe, joka näyttää eri lääkkeiden annostukset. **Huom**: ota huomioon numeeriset arvot, jotka ovat lähellä lääkkeen nimeä tekstissä.

## Arviointikriteerit

Erinomainen | Riittävä | Parannettavaa
--- | --- | -- |
Kaikki tehtävät on suoritettu, graafisesti havainnollistettu ja selitetty, mukaan lukien vähintään yksi kahdesta lisätehtävästä | Yli 5 tehtävää on suoritettu, lisätehtäviä ei ole yritetty tai tulokset eivät ole selkeitä | Vähemmän kuin 5 (mutta enemmän kuin 3) tehtävää on suoritettu, visualisoinnit eivät auta havainnollistamaan asiaa

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.