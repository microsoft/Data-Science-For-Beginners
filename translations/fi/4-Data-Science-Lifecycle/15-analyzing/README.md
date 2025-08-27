<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d92f57eb110dc7f765c05cbf0f837c77",
  "translation_date": "2025-08-26T22:30:13+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "fi"
}
-->
# Tietojenkäsittelyn elinkaari: Analysointi

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Tietojenkäsittelyn elinkaari: Analysointi - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## Ennen luentoa - Kysely

## [Ennen luentoa - Kysely](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

Analysointi tietojenkäsittelyn elinkaaressa varmistaa, että data pystyy vastaamaan esitettyihin kysymyksiin tai ratkaisemaan tietyn ongelman. Tämä vaihe voi myös keskittyä varmistamaan, että malli käsittelee näitä kysymyksiä ja ongelmia oikein. Tämä oppitunti keskittyy eksploratiiviseen data-analyysiin (EDA), joka sisältää tekniikoita datan ominaisuuksien ja suhteiden määrittämiseksi ja joita voidaan käyttää datan valmisteluun mallinnusta varten.

Käytämme esimerkkidatasettiä [Kagglesta](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) havainnollistamaan, miten tätä voidaan soveltaa Pythonin ja Pandas-kirjaston avulla. Tämä datasetti sisältää yleisten sähköpostisanojen esiintymismääriä, ja sähköpostien lähteet ovat anonyymejä. Käytä tämän hakemiston [muistikirjaa](notebook.ipynb) seurataksesi mukana.

## Eksploratiivinen data-analyysi

Elinkaaren keräysvaiheessa data hankitaan, ja ongelmat ja kysymykset määritellään, mutta miten voimme tietää, että data tukee lopputulosta?  
Muista, että datatieteilijä voi kysyä seuraavia kysymyksiä hankkiessaan dataa:
-   Onko minulla tarpeeksi dataa tämän ongelman ratkaisemiseksi?
-   Onko data riittävän laadukasta tähän ongelmaan?
-   Jos löydän lisätietoa tämän datan kautta, pitäisikö meidän harkita tavoitteiden muuttamista tai uudelleenmäärittelyä?

Eksploratiivinen data-analyysi on prosessi, jossa tutustutaan dataan, ja sitä voidaan käyttää vastaamaan näihin kysymyksiin sekä tunnistamaan datasetin kanssa työskentelyn haasteet. Keskitytään joihinkin tekniikoihin, joita käytetään tämän saavuttamiseksi.

## Datan profilointi, kuvaileva tilastotiede ja Pandas
Miten arvioimme, onko meillä tarpeeksi dataa ongelman ratkaisemiseksi? Datan profilointi voi tiivistää ja kerätä yleistä tietoa datasetistämme kuvailevan tilastotieteen tekniikoiden avulla. Datan profilointi auttaa ymmärtämään, mitä meillä on käytettävissä, ja kuvaileva tilastotiede auttaa ymmärtämään, kuinka paljon meillä on käytettävissä.

Joissakin aiemmissa oppitunneissa olemme käyttäneet Pandasia tarjoamaan kuvailevaa tilastotietoa [`describe()`-funktion](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html) avulla. Se tarjoaa lukumäärän, maksimi- ja minimiarvot, keskiarvon, keskihajonnan ja kvantiilit numeerisesta datasta. Kuvailevan tilastotieteen, kuten `describe()`-funktion, käyttö voi auttaa arvioimaan, kuinka paljon dataa on, ja tarvitsemmeko lisää.

## Otanta ja kyselyt
Kaiken tutkiminen suuressa datasetissä voi olla erittäin aikaa vievää ja tehtävä, joka yleensä jätetään tietokoneen tehtäväksi. Otanta on kuitenkin hyödyllinen työkalu datan ymmärtämisessä ja antaa paremman käsityksen siitä, mitä datasetti sisältää ja mitä se edustaa. Otannan avulla voit soveltaa todennäköisyyslaskentaa ja tilastotiedettä tehdäksesi yleisiä johtopäätöksiä datastasi. Vaikka ei ole olemassa tarkkaa sääntöä siitä, kuinka paljon dataa tulisi ottaa otantaan, on tärkeää huomata, että mitä enemmän dataa otat, sitä tarkempia yleistyksiä voit tehdä datasta.  
Pandas-kirjastossa on [`sample()`-funktio](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), jossa voit määrittää argumentin, kuinka monta satunnaista otosta haluat saada ja käyttää.

Yleiset kyselyt datasta voivat auttaa vastaamaan joihinkin yleisiin kysymyksiin ja teorioihin, joita sinulla saattaa olla. Toisin kuin otanta, kyselyt antavat sinulle hallinnan ja mahdollisuuden keskittyä tiettyihin osiin datasta, joista sinulla on kysymyksiä.  
Pandas-kirjaston [`query()`-funktio](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) mahdollistaa sarakkeiden valinnan ja yksinkertaisten vastausten saamisen datasta haettujen rivien kautta.

## Visualisointien käyttö tutkimisessa
Sinun ei tarvitse odottaa, että data on täysin puhdistettu ja analysoitu, ennen kuin alat luoda visualisointeja. Itse asiassa visuaalinen esitys tutkimisen aikana voi auttaa tunnistamaan kuvioita, suhteita ja ongelmia datassa. Lisäksi visualisoinnit tarjoavat tavan kommunikoida niiden kanssa, jotka eivät ole mukana datan hallinnassa, ja voivat olla tilaisuus jakaa ja selventää lisäkysymyksiä, joita ei käsitelty keräysvaiheessa. Katso [Visualisointien osio](../../../../../../../../../3-Data-Visualization) oppiaksesi lisää suosituista tavoista tutkia visuaalisesti.

## Inkonsekvenssien tunnistaminen tutkimalla
Kaikki tämän oppitunnin aiheet voivat auttaa tunnistamaan puuttuvia tai epäjohdonmukaisia arvoja, mutta Pandas tarjoaa funktioita joidenkin näiden tarkistamiseen. [isna() tai isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) voivat tarkistaa puuttuvat arvot. Yksi tärkeä osa näiden arvojen tutkimista datassasi on selvittää, miksi ne päätyivät sellaisiksi alun perin. Tämä voi auttaa sinua päättämään, mitä [toimenpiteitä niiden ratkaisemiseksi tulisi tehdä](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Ennen luentoa - Kysely](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/27)

## Tehtävä

[Tutkiminen vastauksia varten](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskääntämistä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.