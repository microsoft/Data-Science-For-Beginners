<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a167aa0bfb1c46ece1b3d21ae939cc0d",
  "translation_date": "2025-09-04T19:40:07+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "fi"
}
-->
# Data Science -elinkaaren vaihe: Analysointi

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Data Science -elinkaaren vaihe: Analysointi - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## Ennen luentoa - Kysely

## [Ennen luentoa - Kysely](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

Analysointi datan elinkaaressa varmistaa, että data pystyy vastaamaan esitettyihin kysymyksiin tai ratkaisemaan tietyn ongelman. Tämä vaihe keskittyy myös mallin oikeellisuuden varmistamiseen näiden kysymysten ja ongelmien osalta. Tämä oppitunti keskittyy eksploratiiviseen data-analyysiin (EDA), joka sisältää tekniikoita datan ominaisuuksien ja suhteiden määrittämiseen sekä datan valmisteluun mallinnusta varten.

Käytämme esimerkkidataa [Kagglesta](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) havainnollistaaksemme, miten tämä voidaan toteuttaa Pythonilla ja Pandas-kirjastolla. Tämä datasetti sisältää yleisten sähköpostisanojen esiintymismääriä, ja sähköpostien lähteet ovat anonyymejä. Käytä tämän hakemiston [notebookia](notebook.ipynb) seurataksesi mukana.

## Eksploratiivinen data-analyysi

Elinkaaren keräysvaiheessa data hankitaan sekä määritellään ongelmat ja kysymykset, mutta miten voimme varmistaa, että data tukee lopputulosta? 
Muista, että data-analyytikko voi esittää seuraavia kysymyksiä datan hankinnan yhteydessä:
-   Onko minulla tarpeeksi dataa tämän ongelman ratkaisemiseksi?
-   Onko data riittävän laadukasta tähän ongelmaan?
-   Jos löydän lisätietoa datan kautta, pitäisikö meidän harkita tavoitteiden muuttamista tai uudelleenmäärittelyä?

Eksploratiivinen data-analyysi on prosessi, jossa tutustutaan dataan ja vastataan näihin kysymyksiin sekä tunnistetaan datasetin käsittelyn haasteet. Keskitytään joihinkin tekniikoihin, joita käytetään tämän saavuttamiseksi.

## Datan profilointi, kuvaileva tilastotiede ja Pandas
Miten voimme arvioida, onko meillä tarpeeksi dataa ongelman ratkaisemiseksi? Datan profilointi voi tiivistää ja kerätä yleistä tietoa datasetistä kuvailevan tilastotieteen tekniikoiden avulla. Datan profilointi auttaa ymmärtämään, mitä meillä on käytettävissä, ja kuvaileva tilastotiede auttaa ymmärtämään, kuinka paljon meillä on käytettävissä.

Joissakin aiemmissa oppitunneissa olemme käyttäneet Pandasia tarjoamaan kuvailevaa tilastotietoa [`describe()`-funktion](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html) avulla. Se tarjoaa lukumäärän, maksimi- ja minimiarvot, keskiarvon, keskihajonnan ja kvantiilit numeerisesta datasta. Kuvailevan tilastotieteen, kuten `describe()`-funktion, käyttö voi auttaa arvioimaan, kuinka paljon dataa on ja tarvitsemmeko lisää.

## Otanta ja kyselyt
Kaiken tutkiminen suuressa datasetissä voi olla erittäin aikaa vievää ja yleensä jätetään tietokoneen tehtäväksi. Otanta on kuitenkin hyödyllinen työkalu datan ymmärtämisessä ja antaa paremman käsityksen siitä, mitä datasetissä on ja mitä se edustaa. Otannan avulla voit soveltaa todennäköisyyslaskentaa ja tilastotiedettä tehdäksesi yleisiä johtopäätöksiä datasta. Vaikka ei ole olemassa tarkkaa sääntöä siitä, kuinka paljon dataa tulisi ottaa otantaan, on tärkeää huomata, että mitä enemmän dataa otat, sitä tarkempia yleistyksiä voit tehdä datasta.

Pandas-kirjastossa on [`sample()`-funktio](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), jossa voit määrittää argumentin, kuinka monta satunnaista otosta haluat saada ja käyttää.

Yleiset kyselyt datasta voivat auttaa vastaamaan joihinkin yleisiin kysymyksiin ja teorioihin, joita sinulla saattaa olla. Toisin kuin otanta, kyselyt antavat sinulle mahdollisuuden hallita ja keskittyä tiettyihin datan osiin, joista sinulla on kysymyksiä. Pandas-kirjaston [`query()`-funktio](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) mahdollistaa sarakkeiden valinnan ja yksinkertaisten vastausten saamisen datasta haettujen rivien kautta.

## Visualisointien käyttö tutkimisessa
Sinun ei tarvitse odottaa, että data on täysin puhdistettu ja analysoitu ennen visualisointien luomista. Itse asiassa visuaalinen esitys tutkimisen aikana voi auttaa tunnistamaan kuvioita, suhteita ja ongelmia datassa. Lisäksi visualisoinnit tarjoavat keinon kommunikoida niiden kanssa, jotka eivät ole mukana datan hallinnassa, ja voivat olla tilaisuus jakaa ja selventää lisäkysymyksiä, joita ei käsitelty keräysvaiheessa. Katso [Visualisointien osio](../../../../../../../../../3-Data-Visualization) oppiaksesi lisää suosituista tavoista tutkia visuaalisesti.

## Epäjohdonmukaisuuksien tunnistaminen tutkimisen avulla
Kaikki tämän oppitunnin aiheet voivat auttaa tunnistamaan puuttuvia tai epäjohdonmukaisia arvoja, mutta Pandas tarjoaa funktioita joidenkin näiden tarkistamiseen. [isna() tai isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) voi tarkistaa puuttuvat arvot. Yksi tärkeä osa näiden arvojen tutkimista datassa on selvittää, miksi ne päätyivät siihen tilaan alun perin. Tämä voi auttaa sinua päättämään, mitä [toimenpiteitä niiden ratkaisemiseksi](/2-Working-With-Data/08-data-preparation/notebook.ipynb) tulisi tehdä.

## [Luentojälkeinen kysely](https://ff-quizzes.netlify.app/en/ds/)

## Tehtävä

[Vastausten etsiminen](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.