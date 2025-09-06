<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "661dad02c3ac239644d34c1eb51e76f8",
  "translation_date": "2025-09-06T21:12:07+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "fi"
}
-->
# Data Science -elinkaari: Analysointi

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Data Science -elinkaari: Analysointi - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Ennakkokysely](https://ff-quizzes.netlify.app/en/ds/quiz/28)

Analysointi datan elinkaaren vaiheessa varmistaa, että data pystyy vastaamaan esitettyihin kysymyksiin tai ratkaisemaan tietyn ongelman. Tämä vaihe keskittyy myös mallin oikeellisuuden varmistamiseen näiden kysymysten ja ongelmien osalta. Tämä oppitunti keskittyy eksploratiiviseen data-analyysiin (EDA), joka sisältää tekniikoita datan ominaisuuksien ja suhteiden määrittämiseen sekä datan valmisteluun mallinnusta varten.

Käytämme esimerkkidataa [Kagglesta](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) havainnollistaaksemme, miten tätä voidaan soveltaa Pythonin ja Pandas-kirjaston avulla. Tämä datasetti sisältää yleisten sähköpostisanojen lukumäärän, ja sähköpostien lähteet ovat anonyymejä. Käytä tämän hakemiston [notebookia](notebook.ipynb) seurataksesi mukana.

## Eksploratiivinen data-analyysi

Elinkaaren keräysvaiheessa data hankitaan sekä määritellään ongelmat ja kysymykset, mutta miten voimme varmistaa, että data tukee lopputulosta?  
Muista, että data-analyytikko saattaa kysyä seuraavia kysymyksiä datan hankinnan yhteydessä:
-   Onko minulla tarpeeksi dataa tämän ongelman ratkaisemiseksi?
-   Onko data riittävän laadukasta tähän ongelmaan?
-   Jos löydän lisätietoa datan kautta, pitäisikö meidän harkita tavoitteiden muuttamista tai uudelleenmäärittelyä?

Eksploratiivinen data-analyysi on prosessi, jossa tutustutaan dataan ja vastataan näihin kysymyksiin sekä tunnistetaan datasetin käsittelyn haasteet. Keskitytään joihinkin tekniikoihin, joita käytetään tämän saavuttamiseksi.

## Datan profilointi, kuvaileva tilastotiede ja Pandas
Miten arvioimme, onko meillä tarpeeksi dataa ongelman ratkaisemiseksi? Datan profilointi voi tiivistää ja kerätä yleistä tietoa datasetistä kuvailevan tilastotieteen tekniikoiden avulla. Datan profilointi auttaa ymmärtämään, mitä meillä on käytettävissä, ja kuvaileva tilastotiede auttaa ymmärtämään, kuinka paljon meillä on käytettävissä.

Joissakin aiemmissa oppitunneissa olemme käyttäneet Pandasia tarjoamaan kuvailevaa tilastotietoa [`describe()`-funktion](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html) avulla. Se tarjoaa lukumäärän, maksimi- ja minimiarvot, keskiarvon, keskihajonnan ja kvantiilit numeerisesta datasta. Kuvailevan tilastotieteen, kuten `describe()`-funktion, käyttö voi auttaa arvioimaan, kuinka paljon dataa on ja tarvitsemmeko lisää.

## Otanta ja kyselyt
Kaiken tutkiminen suuressa datasetissä voi olla erittäin aikaa vievää ja yleensä jätetään tietokoneen tehtäväksi. Otanta on kuitenkin hyödyllinen työkalu datan ymmärtämisessä ja antaa paremman käsityksen siitä, mitä datasetissä on ja mitä se edustaa. Otannan avulla voit soveltaa todennäköisyyttä ja tilastotiedettä tehdäksesi yleisiä johtopäätöksiä datasta. Vaikka ei ole olemassa tarkkaa sääntöä siitä, kuinka paljon dataa tulisi ottaa otantaan, on tärkeää huomata, että mitä enemmän dataa otat, sitä tarkempia yleistyksiä voit tehdä datasta.  
Pandas-kirjastossa on [`sample()`-funktio](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), jossa voit määrittää argumentin, kuinka monta satunnaista otosta haluat saada ja käyttää.

Yleiset kyselyt datasta voivat auttaa vastaamaan joihinkin yleisiin kysymyksiin ja teorioihin, joita sinulla saattaa olla. Toisin kuin otanta, kyselyt antavat sinulle mahdollisuuden hallita ja keskittyä tiettyihin osiin datasta, joista haluat vastauksia.  
Pandas-kirjaston [`query()`-funktio](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) mahdollistaa sarakkeiden valinnan ja yksinkertaisten vastausten saamisen datasta haettujen rivien kautta.

## Visualisointien käyttö tutkimisessa
Sinun ei tarvitse odottaa, että data on täysin puhdistettu ja analysoitu ennen visualisointien luomista. Itse asiassa visuaalinen esitys tutkimisen aikana voi auttaa tunnistamaan kuvioita, suhteita ja ongelmia datassa. Lisäksi visualisoinnit tarjoavat viestintäkeinon niille, jotka eivät ole mukana datan hallinnassa, ja voivat olla tilaisuus jakaa ja selventää lisäkysymyksiä, joita ei käsitelty keräysvaiheessa. Katso [Visualisointien osio](../../../../../../../../../3-Data-Visualization) oppiaksesi lisää suosituista tavoista tutkia visuaalisesti.

## Epäjohdonmukaisuuksien tunnistaminen tutkimalla
Kaikki tämän oppitunnin aiheet voivat auttaa tunnistamaan puuttuvia tai epäjohdonmukaisia arvoja, mutta Pandas tarjoaa funktioita joiden avulla näitä voi tarkistaa. [isna() tai isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) voi tarkistaa puuttuvia arvoja. Yksi tärkeä osa näiden arvojen tutkimista datassa on selvittää, miksi ne päätyivät siihen tilaan alun perin. Tämä voi auttaa päättämään, mitä [toimenpiteitä niiden ratkaisemiseksi tulisi tehdä](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Jälkikysely](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Tehtävä

[Tutkiminen vastauksia varten](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.