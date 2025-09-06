<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a76ab694b1534fa57981311975660bfe",
  "translation_date": "2025-09-06T12:23:26+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "fi"
}
-->
## Tietotyypit

Kuten jo mainittiin, dataa on kaikkialla. Meidän täytyy vain osata kerätä se oikealla tavalla! On hyödyllistä erottaa toisistaan **strukturoitu** ja **strukturoimaton** data. Strukturoitu data esitetään yleensä hyvin jäsennellyssä muodossa, usein taulukkona tai useina taulukoina, kun taas strukturoimaton data on vain kokoelma tiedostoja. Joskus voidaan myös puhua **puolistrukturoidusta** datasta, jolla on jonkinlainen rakenne, mutta joka voi vaihdella suuresti.

| Strukturoitu                                                                | Puolistrukturoitu                                                                             | Strukturoimaton                        |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------- |
| Lista ihmisistä ja heidän puhelinnumeroistaan                               | Wikipedian sivut linkkeineen                                                                  | Encyclopedia Britannican teksti        |
| Lämpötila kaikissa rakennuksen huoneissa joka minuutti viimeisen 20 vuoden ajalta | Tieteellisten artikkelien kokoelma JSON-muodossa, sisältäen kirjoittajat, julkaisupäivän ja tiivistelmän | Yrityksen dokumenttien tiedostojako    |
| Tiedot rakennukseen saapuvien ihmisten iästä ja sukupuolesta                 | Internet-sivut                                                                                | Valvontakameran raaka videokuva         |

## Mistä saada dataa

Datalla on lukemattomia mahdollisia lähteitä, eikä kaikkia voi mitenkään listata! Mainitaan kuitenkin joitakin tyypillisiä paikkoja, joista dataa voi saada:

* **Strukturoitu**
  - **Esineiden internet** (IoT), mukaan lukien erilaiset sensorit, kuten lämpötila- tai paineanturit, tuottavat paljon hyödyllistä dataa. Esimerkiksi, jos toimistorakennus on varustettu IoT-sensoreilla, voimme automaattisesti ohjata lämmitystä ja valaistusta kustannusten minimoimiseksi.
  - **Kyselyt**, joita pyydämme käyttäjiä täyttämään ostoksen jälkeen tai verkkosivustolla vierailun jälkeen.
  - **Käyttäytymisanalyysi** voi esimerkiksi auttaa ymmärtämään, kuinka syvälle käyttäjä menee sivustolla ja mikä on tyypillinen syy sivustolta poistumiseen.
* **Strukturoimaton**
  - **Tekstit** voivat olla rikas lähde oivalluksille, kuten yleinen **tunnelmapisteytys** tai avainsanojen ja semanttisen merkityksen poiminta.
  - **Kuvat** tai **videot**. Valvontakameran videoita voidaan käyttää liikenteen arvioimiseen tiellä ja tiedottamaan mahdollisista ruuhkista.
  - Verkkopalvelimen **lokitiedostot** voivat auttaa ymmärtämään, mitkä sivuston sivut ovat useimmin vierailtuja ja kuinka kauan niillä viivytään.
* **Puolistrukturoitu**
  - **Sosiaalisen verkoston** graafit voivat olla loistavia datalähteitä käyttäjien persoonallisuuksista ja potentiaalisesta tehokkuudesta tiedon levittämisessä.
  - Kun meillä on joukko valokuvia juhlista, voimme yrittää poimia **ryhmädynamiikkaa** rakentamalla graafin ihmisistä, jotka ottavat kuvia toistensa kanssa.

Kun tiedät erilaiset mahdolliset datalähteet, voit miettiä erilaisia skenaarioita, joissa datatieteen tekniikoita voidaan soveltaa tilanteen parempaan ymmärtämiseen ja liiketoimintaprosessien parantamiseen.

## Mitä datalla voi tehdä

Datatieteessä keskitymme seuraaviin datan käsittelyn vaiheisiin:

## Digitalisaatio ja digitaalinen transformaatio

Viimeisen vuosikymmenen aikana monet yritykset ovat alkaneet ymmärtää datan merkityksen liiketoimintapäätösten tekemisessä. Jotta datatieteen periaatteita voidaan soveltaa liiketoiminnan pyörittämiseen, täytyy ensin kerätä dataa, eli muuttaa liiketoimintaprosessit digitaaliseen muotoon. Tätä kutsutaan **digitalisaatioksi**. Datatieteen tekniikoiden soveltaminen tähän dataan päätöksenteon ohjaamiseksi voi johtaa merkittäviin tuottavuuden kasvuun (tai jopa liiketoiminnan suunnanmuutokseen), jota kutsutaan **digitaaliseksi transformaatioksi**.

Otetaan esimerkki. Oletetaan, että meillä on datatieteen kurssi (kuten tämä), jonka toimitamme verkossa opiskelijoille, ja haluamme käyttää datatiedettä sen parantamiseen. Miten voimme tehdä sen?

Voimme aloittaa kysymällä "Mitä voidaan digitalisoida?" Yksinkertaisin tapa olisi mitata, kuinka kauan kullakin opiskelijalla kestää suorittaa kukin moduuli, ja mitata saavutettu tieto antamalla monivalintatesti kunkin moduulin lopussa. Kun lasketaan keskimääräinen suorittamisaika kaikkien opiskelijoiden kesken, voimme selvittää, mitkä moduulit aiheuttavat eniten vaikeuksia opiskelijoille ja työskennellä niiden yksinkertaistamiseksi.
Voit väittää, että tämä lähestymistapa ei ole ihanteellinen, koska moduulit voivat olla eripituisia. On luultavasti oikeudenmukaisempaa jakaa aika moduulin pituuden mukaan (merkkien lukumäärässä) ja verrata näitä arvoja sen sijaan.
Kun alamme analysoida monivalintatestien tuloksia, voimme yrittää selvittää, mitkä käsitteet tuottavat opiskelijoille vaikeuksia ymmärtää, ja käyttää tätä tietoa sisällön parantamiseen. Tätä varten meidän täytyy suunnitella testit siten, että jokainen kysymys liittyy tiettyyn käsitteeseen tai tietokokonaisuuteen.

Jos haluamme mennä vielä pidemmälle, voimme verrata kunkin moduulin suorittamiseen käytettyä aikaa opiskelijoiden ikäryhmiin. Saatamme huomata, että joillekin ikäryhmille moduulin suorittaminen vie kohtuuttoman kauan, tai että opiskelijat keskeyttävät ennen moduulin loppuun suorittamista. Tämä voi auttaa meitä antamaan ikäsuosituksia moduulille ja vähentämään ihmisten tyytymättömyyttä vääristä odotuksista.

## 🚀 Haaste

Tässä haasteessa yritämme löytää Data Science -alaan liittyviä käsitteitä tarkastelemalla tekstejä. Otamme Wikipedia-artikkelin Data Sciencesta, lataamme ja käsittelemme tekstin, ja sitten rakennamme sanapilven, kuten tämän:

![Sanapilvi Data Sciencesta](../../../../translated_images/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.fi.png)

Vieraile [`notebook.ipynb`](../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') -tiedostossa lukeaksesi koodin läpi. Voit myös suorittaa koodin ja nähdä, miten se tekee kaikki datamuunnokset reaaliajassa.

> Jos et tiedä, miten suorittaa koodia Jupyter Notebookissa, tutustu [tähän artikkeliin](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Luennon jälkeinen kysely](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Tehtävät

* **Tehtävä 1**: Muokkaa yllä olevaa koodia löytääksesi liittyviä käsitteitä **Big Data**- ja **Machine Learning** -aloille.
* **Tehtävä 2**: [Pohdi Data Science -skenaarioita](assignment.md)

## Kiitokset

Tämän oppitunnin on kirjoittanut ♥️:lla [Dmitry Soshnikov](http://soshnikov.com)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskääntämistä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virhetulkinnoista.