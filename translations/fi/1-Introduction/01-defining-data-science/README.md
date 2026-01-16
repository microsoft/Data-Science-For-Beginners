<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43212cc1ac137b7bb1dcfb37ca06b0f4",
  "translation_date": "2025-10-25T18:57:10+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "fi"
}
-->
# Määritelmä: Tietojenkäsittelytiede

| ![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------: |
|              Tietojenkäsittelytieteen määritelmä - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

---

[![Tietojenkäsittelytieteen määritelmä - Video](../../../../translated_images/fi/video-def-ds.6623ee2392ef1abf6d7faf3fad10a4163642811749da75f44e35a5bb121de15c.png)](https://youtu.be/beZ7Mb_oz9I)

## [Esiluennon kysely](https://ff-quizzes.netlify.app/en/ds/quiz/0)

## Mitä data on?
Jokapäiväisessä elämässämme olemme jatkuvasti datan ympäröimänä. Teksti, jota luet juuri nyt, on dataa. Ystäviesi puhelinnumerolista älypuhelimessasi on dataa, samoin kuin kellosi näyttämä nykyinen aika. Ihmisinä käsittelemme luonnostaan dataa laskemalla rahaa tai kirjoittamalla kirjeitä ystävillemme.

Tietokoneiden keksimisen myötä datasta tuli kuitenkin paljon tärkeämpää. Tietokoneiden päätehtävä on suorittaa laskutoimituksia, mutta ne tarvitsevat dataa toimiakseen. Siksi meidän on ymmärrettävä, miten tietokoneet tallentavat ja käsittelevät dataa.

Internetin syntyminen on lisännyt tietokoneiden roolia datan käsittelylaitteina. Jos mietit asiaa, käytämme nykyään tietokoneita yhä enemmän datan käsittelyyn ja viestintään kuin varsinaisiin laskutoimituksiin. Kun kirjoitamme sähköpostia ystävälle tai etsimme tietoa internetistä, luomme, tallennamme, siirrämme ja käsittelemme dataa.
> Muistatko, milloin viimeksi käytit tietokonetta varsinaiseen laskemiseen?

## Mitä on tietojenkäsittelytiede?

[Wikipedian](https://en.wikipedia.org/wiki/Data_science) mukaan **tietojenkäsittelytiede** määritellään *tieteelliseksi alaksi, joka käyttää tieteellisiä menetelmiä tiedon ja oivallusten hankkimiseksi sekä rakenteellisesta että rakenteettomasta datasta ja soveltaa tietoa ja käytännön oivalluksia dataan laajalla sovellusalueella*.

Tämä määritelmä korostaa seuraavia tietojenkäsittelytieteen keskeisiä näkökohtia:

* Tietojenkäsittelytieteen päätavoite on **hankkia tietoa** datasta, toisin sanoen **ymmärtää** dataa, löytää piilotettuja yhteyksiä ja rakentaa **malli**.
* Tietojenkäsittelytiede käyttää **tieteellisiä menetelmiä**, kuten todennäköisyyslaskentaa ja tilastotiedettä. Kun termi *tietojenkäsittelytiede* alun perin esiteltiin, jotkut väittivät sen olevan vain uusi hieno nimi tilastotieteelle. Nykyään on selvää, että ala on paljon laajempi.
* Hankittu tieto tulisi soveltaa tuottamaan **käytännön oivalluksia**, eli käytännöllisiä näkemyksiä, joita voidaan soveltaa todellisiin liiketoimintatilanteisiin.
* Meidän tulisi pystyä käsittelemään sekä **rakenteellista** että **rakenteetonta** dataa. Palaamme myöhemmin kurssilla keskustelemaan datan eri tyypeistä.
* **Sovellusalue** on tärkeä käsite, ja tietojenkäsittelytieteilijöiden on usein oltava ainakin jossain määrin asiantuntijoita ongelma-alueella, esimerkiksi: rahoitus, lääketiede, markkinointi jne.

> Toinen tärkeä näkökohta tietojenkäsittelytieteessä on se, että se tutkii, miten dataa voidaan kerätä, tallentaa ja käsitellä tietokoneiden avulla. Vaikka tilastotiede antaa meille matemaattiset perusteet, tietojenkäsittelytiede soveltaa matemaattisia käsitteitä oivallusten saamiseksi datasta.

Yksi tapa (liitetty [Jim Grayhin](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) tarkastella tietojenkäsittelytiedettä on pitää sitä erillisenä tieteen paradigmana:
* **Empiirinen**, jossa luotamme pääasiassa havaintoihin ja kokeiden tuloksiin
* **Teoreettinen**, jossa uudet käsitteet syntyvät olemassa olevasta tieteellisestä tiedosta
* **Laskennallinen**, jossa löydämme uusia periaatteita laskennallisten kokeiden avulla
* **Dataohjautuva**, perustuu datan suhteiden ja mallien löytämiseen  

## Muita liittyviä aloja

Koska data on kaikkialla, tietojenkäsittelytiede on myös laaja ala, joka koskettaa monia muita tieteenaloja.

<dl>
<dt>Tietokannat</dt>
<dd>
Keskeinen kysymys on <b>miten dataa tallennetaan</b>, eli miten se jäsennetään niin, että käsittely on nopeampaa. On olemassa erilaisia tietokantoja, jotka tallentavat rakenteellista ja rakenteetonta dataa, joita <a href="../../2-Working-With-Data/README.md">käsittelemme kurssillamme</a>.
</dd>
<dt>Big Data</dt>
<dd>
Usein meidän täytyy tallentaa ja käsitellä erittäin suuria määriä dataa, jolla on suhteellisen yksinkertainen rakenne. On olemassa erityisiä lähestymistapoja ja työkaluja, jotka mahdollistavat datan tallentamisen hajautetusti tietokoneklusterissa ja sen tehokkaan käsittelyn.
</dd>
<dt>Koneoppiminen</dt>
<dd>
Yksi tapa ymmärtää dataa on <b>rakentaa malli</b>, joka pystyy ennustamaan halutun lopputuloksen. Mallien kehittäminen datasta tunnetaan nimellä <b>koneoppiminen</b>. Voit tutustua <a href="https://aka.ms/ml-beginners">Koneoppiminen aloittelijoille</a> -opetusohjelmaamme saadaksesi lisätietoa.
</dd>
<dt>Keinoäly</dt>
<dd>
Koneoppimisen alue, joka tunnetaan nimellä keinoäly (AI), perustuu myös dataan ja sisältää monimutkaisten mallien rakentamisen, jotka jäljittelevät ihmisen ajatteluprosesseja. AI-menetelmät mahdollistavat usein rakenteettoman datan (esim. luonnollinen kieli) muuttamisen rakenteellisiksi oivalluksiksi.
</dd>
<dt>Visualisointi</dt>
<dd>
Valtavat määrät dataa ovat ihmiselle vaikeasti ymmärrettäviä, mutta kun luomme hyödyllisiä visualisointeja datasta, voimme ymmärtää sitä paremmin ja tehdä johtopäätöksiä. Siksi on tärkeää tuntea monia tapoja visualisoida tietoa - asia, jota käsittelemme <a href="../../3-Data-Visualization/README.md">kurssimme osassa 3</a>. Liittyviä aloja ovat myös <b>infografiikka</b> ja yleisesti <b>ihmisen ja tietokoneen vuorovaikutus</b>.
</dd>
</dl>

## Datan tyypit

Kuten jo mainitsimme, dataa on kaikkialla. Meidän täytyy vain tallentaa se oikealla tavalla! On hyödyllistä erottaa toisistaan **rakenteellinen** ja **rakenteeton** data. Ensimmäinen esitetään tyypillisesti hyvin jäsennellyssä muodossa, usein taulukkona tai useina taulukoina, kun taas jälkimmäinen on vain kokoelma tiedostoja. Joskus voidaan puhua myös **puolirakenteisesta** datasta, jolla on jonkinlainen rakenne, joka voi vaihdella suuresti.

| Rakenteellinen                                                              | Puolirakenteinen                                                                            | Rakenteeton                            |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------- |
| Lista ihmisistä ja heidän puhelinnumeroistaan                               | Wikipedian sivut linkkeineen                                                               | Encyclopedia Britannican teksti        |
| Lämpötila kaikissa rakennuksen huoneissa joka minuutti viimeisen 20 vuoden ajan | Tieteellisten artikkelien kokoelma JSON-muodossa, jossa on kirjoittajat, julkaisupäivä ja tiivistelmä | Yritysdokumenttien tiedostokansio      |
| Tiedot rakennukseen tulevien ihmisten iästä ja sukupuolesta                  | Internet-sivut                                                                             | Valvontakameran raaka videokuva         |

## Mistä dataa saa?

Datalla on monia mahdollisia lähteitä, eikä niitä kaikkia ole mahdollista luetella! Mainitaan kuitenkin joitakin tyypillisiä paikkoja, joista dataa voi saada:

* **Rakenteellinen**
  - **Esineiden internet** (IoT), mukaan lukien erilaisista sensoreista, kuten lämpötila- tai paineantureista, saatu data tarjoaa paljon hyödyllistä tietoa. Esimerkiksi, jos toimistorakennus on varustettu IoT-sensoreilla, voimme automaattisesti ohjata lämmitystä ja valaistusta kustannusten minimoimiseksi.
  - **Kyselyt**, joita pyydämme käyttäjiä täyttämään ostoksen jälkeen tai verkkosivustolla vierailun jälkeen.
  - **Käyttäytymisanalyysi** voi esimerkiksi auttaa meitä ymmärtämään, kuinka syvälle käyttäjä menee sivustolla ja mikä on tyypillinen syy sivustolta poistumiseen.
* **Rakenteeton**
  - **Tekstit** voivat olla rikas oivallusten lähde, kuten yleinen **tunnelmapisteytys** tai avainsanojen ja semanttisen merkityksen poiminta.
  - **Kuvat** tai **videot**. Valvontakameran videoita voidaan käyttää liikenteen arvioimiseen tiellä ja ihmisten informoimiseen mahdollisista ruuhkista.
  - Verkkopalvelimen **lokitiedostot** voivat auttaa ymmärtämään, mitkä sivuston sivut ovat useimmin vierailtuja ja kuinka kauan niillä viivytään.
* Puolirakenteinen
  - **Sosiaalisen verkoston** graafit voivat olla erinomaisia tietolähteitä käyttäjien persoonallisuuksista ja mahdollisesta tehokkuudesta tiedon levittämisessä.
  - Kun meillä on joukko valokuvia juhlista, voimme yrittää poimia **ryhmädynamiikkaa** rakentamalla graafin ihmisistä, jotka ottavat kuvia yhdessä.

Kun tiedät erilaiset mahdolliset datan lähteet, voit miettiä erilaisia skenaarioita, joissa tietojenkäsittelytieteen tekniikoita voidaan soveltaa tilanteen ymmärtämiseksi paremmin ja liiketoimintaprosessien parantamiseksi.

## Mitä datalla voi tehdä?

Tietojenkäsittelytieteessä keskitymme seuraaviin datan käsittelyn vaiheisiin:

<dl>
<dt>1) Datan hankinta</dt>
<dd>
Ensimmäinen askel on datan kerääminen. Vaikka monissa tapauksissa se voi olla yksinkertainen prosessi, kuten datan siirtyminen tietokantaan verkkosovelluksesta, joskus meidän täytyy käyttää erityisiä tekniikoita. Esimerkiksi IoT-sensoreista tuleva data voi olla ylivoimaista, ja on hyvä käytäntö käyttää välimuistipäätteitä, kuten IoT Hubia, keräämään kaikki data ennen sen jatkokäsittelyä.
</dd>
<dt>2) Datan tallennus</dt>
<dd>
Datan tallentaminen voi olla haastavaa, erityisesti jos puhumme big datasta. Kun päätämme, miten dataa tallennetaan, on järkevää ennakoida, miten haluamme kysellä dataa tulevaisuudessa. Datan tallentamiseen on useita tapoja:
<ul>
<li>Relaatiotietokanta tallentaa taulukoiden kokoelman ja käyttää erityistä kieltä nimeltä SQL niiden kyselyyn. Tyypillisesti taulukot järjestetään eri ryhmiin, joita kutsutaan skeemoiksi. Monissa tapauksissa meidän täytyy muuntaa data alkuperäisestä muodosta sopimaan skeemaan.</li>
<li><a href="https://en.wikipedia.org/wiki/NoSQL">NoSQL</a>-tietokanta, kuten <a href="https://azure.microsoft.com/services/cosmos-db/?WT.mc_id=academic-77958-bethanycheum">CosmosDB</a>, ei pakota skeemoja dataan ja mahdollistaa monimutkaisemman datan, kuten hierarkkisten JSON-dokumenttien tai graafien, tallentamisen. Kuitenkin NoSQL-tietokannoilla ei ole yhtä rikkaita kyselyominaisuuksia kuin SQL:llä, eikä ne voi varmistaa viite-eheyttä, eli sääntöjä siitä, miten data on jäsennelty taulukoihin ja miten taulukoiden väliset suhteet toimivat.</li>
<li><a href="https://en.wikipedia.org/wiki/Data_lake">Data Lake</a> -tallennusta käytetään suurten datakokoelmien tallentamiseen raakana, rakenteettomassa muodossa. Datajärviä käytetään usein big datan kanssa, jossa kaikki data ei mahdu yhdelle koneelle ja se täytyy tallentaa ja käsitellä palvelinklustereilla. <a href="https://en.wikipedia.org/wiki/Apache_Parquet">Parquet</a> on datamuoto, jota käytetään usein yhdessä big datan kanssa.</li> 
</ul>
</dd>
<dt>3) Datan käsittely</dt>
<dd>
Tämä on datan käsittelyn jännittävin osa, joka sisältää datan muuntamisen alkuperäisestä muodosta muotoon, jota voidaan käyttää visualisointiin tai mallin kouluttamiseen. Kun käsittelemme rakenteetonta dataa, kuten tekstiä tai kuvia, saatamme tarvita joitakin AI-tekniikoita datan <b>ominaisuuksien</b> poimimiseen, jolloin se voidaan muuntaa rakenteelliseksi muodoksi.
</dd>
<dt>4) Visualisointi / Ihmisen oivallukset</dt>
<dd>
Usein datan ymmärtämiseksi meidän täytyy visualisoida se. Kun meillä on monia erilaisia visualisointitekniikoita työkalupakissamme, voimme löytää oikean näkökulman oivallusten tekemiseksi. Usein tietojenkäsittelytieteilijän täytyy "leikkiä datalla", visualisoida sitä useita kertoja ja etsiä yhteyksiä. Lisäksi voimme käyttää tilastollisia tekniikoita hypoteesien testaamiseen tai korrelaation todistamiseen eri datan osien välillä.
</dd>
<dt>5) Ennustavan mallin kouluttaminen</dt>
<dd>
Koska tietojenkäsittelytieteen lopullinen tavoite on pystyä tekemään päätöksiä datan perusteella, saatamme haluta käyttää <a href="http://github.com/microsoft/ml-for-beginners">koneoppimisen</a> tekniikoita ennustavan mallin rakentamiseen. Voimme sitten käyttää tätä mallia ennustamaan uusia datakokonaisuuksia, joilla on samanlainen rakenne.
</dd>
</dl>

Tietenkin, riippuen datasta, jotkut vaiheet voivat puuttua (esim. kun data on jo tietokannassa tai kun emme tarvitse mallin koulutusta), tai jotkut vaiheet voivat toistua useita kertoja (kuten datan käsittely).

## Digitalisaatio ja digitaalinen transformaatio

Viime vuosikymmenen aikana monet yritykset ovat alkaneet ymmärtää datan merkityksen liiketoimintapäätösten tekemisessä. Jotta tietojenkäsittelytieteen periaatteita voidaan soveltaa liiketoiminnan johtamiseen, on ensin kerättävä dataa, eli muutettava liiketoimintaprosessit digitaaliseen muotoon. Tätä kutsutaan **digitalisaatioksi**. Tietojenkäsittelytieteen tekniikoiden soveltaminen tähän dataan päätösten ohjaamiseksi voi johtaa merkittäviin tuottavuuden parannuksiin (tai jopa liiketoiminnan uudistamiseen), mikä tunnetaan nimellä **digitaalinen transformaatio**.

Otetaan esimerkki. Oletetaan, että meillä on tietojenkäsittelytieteen kurssi (kuten tämä), jonka toimitamme verkossa opiskelijoille, ja haluamme käyttää tietojenkäsittelytieteen menetelmiä sen parantamiseksi. Kuinka voimme tehdä sen?

Voimme aloittaa kysymällä "Mitä voidaan digitalisoida?" Yksinkertaisin tapa olisi mitata, kuinka kauan kunkin opiskelijan kestää suorittaa kukin moduuli, ja mitata hankittu tieto antamalla monivalintatesti kunkin moduulin lopussa. Kun lasketaan keskimääräinen suorittamisaika kaikkien opiskelijoiden kesken, voimme selvittää, mitkä moduulit aiheuttavat eniten vaikeuksia opiskelijoille ja työskennellä niiden yksinkertaistamiseksi.
> Voit väittää, että tämä lähestymistapa ei ole ihanteellinen, koska moduulit voivat olla eri pituisia. On todennäköisesti oikeudenmukaisempaa jakaa aika moduulin pituudella (merkkien lukumäärällä) ja verrata näitä arvoja keskenään.

Kun alamme analysoida monivalintatestien tuloksia, voimme yrittää selvittää, mitkä käsitteet ovat opiskelijoille vaikeita ymmärtää, ja käyttää tätä tietoa sisällön parantamiseen. Tämän tekemiseksi meidän on suunniteltava testit siten, että jokainen kysymys liittyy tiettyyn käsitteeseen tai tietokokonaisuuteen.

Jos haluamme mennä vielä pidemmälle, voimme piirtää kaavion, jossa esitetään kunkin moduulin suorittamiseen käytetty aika suhteessa opiskelijoiden ikäryhmiin. Voimme huomata, että joillekin ikäryhmille moduulin suorittaminen vie suhteettoman kauan tai että opiskelijat keskeyttävät ennen sen suorittamista. Tämä voi auttaa meitä antamaan ikäsuosituksia moduulille ja vähentämään ihmisten tyytymättömyyttä väärien odotusten vuoksi.

## 🚀 Haaste

Tässä haasteessa yritämme löytää Data Science -alaan liittyviä käsitteitä tarkastelemalla tekstejä. Otamme Wikipedia-artikkelin Data Sciencesta, lataamme ja käsittelemme tekstin ja luomme sitten sanapilven, joka näyttää tältä:

![Sanapilvi Data Sciencesta](../../../../translated_images/fi/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.png)

Vieraile tiedostossa [`notebook.ipynb`](../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') lukeaksesi koodin läpi. Voit myös suorittaa koodin ja nähdä, kuinka se suorittaa kaikki datan muunnokset reaaliajassa.

> Jos et tiedä, miten koodia suoritetaan Jupyter Notebookissa, tutustu [tähän artikkeliin](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Luentojälkeinen kysely](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Tehtävät

* **Tehtävä 1**: Muokkaa yllä olevaa koodia löytääksesi **Big Data**- ja **Machine Learning** -aloihin liittyviä käsitteitä.
* **Tehtävä 2**: [Pohdi Data Science -skenaarioita](assignment.md)

## Kiitokset

Tämän oppitunnin on laatinut ♥️:lla [Dmitry Soshnikov](http://soshnikov.com)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.