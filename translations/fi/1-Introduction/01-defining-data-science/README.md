<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8141e7195841682914be03ef930fe43d",
  "translation_date": "2025-09-03T20:20:38+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "fi"
}
-->
## Tietotyypit

Kuten jo mainittiin, dataa on kaikkialla. Meidän täytyy vain osata tallentaa se oikealla tavalla! On hyödyllistä erottaa toisistaan **strukturoitu** ja **strukturoimaton** data. Strukturoitu data esitetään yleensä hyvin jäsennellyssä muodossa, usein taulukkona tai useampana taulukkona, kun taas strukturoimaton data on vain joukko tiedostoja. Joskus voidaan puhua myös **puolistrukturoidusta** datasta, jolla on jonkinlainen rakenne, mutta se voi vaihdella suuresti.

| Strukturoitu                                                                | Puolistrukturoitu                                                                             | Strukturoimaton                        |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------- |
| Lista ihmisistä ja heidän puhelinnumeroistaan                               | Wikipedia-sivut linkkeineen                                                                   | Encyclopedia Britannican teksti        |
| Lämpötila kaikissa rakennuksen huoneissa joka minuutti viimeisen 20 vuoden ajalta | Tieteellisten artikkelien kokoelma JSON-muodossa, sisältäen kirjoittajat, julkaisupäivän ja tiivistelmän | Yrityksen asiakirjojen tiedostojako     |
| Tiedot kaikkien rakennukseen tulevien ihmisten iästä ja sukupuolesta         | Internet-sivut                                                                               | Valvontakameran raaka videokuva         |

## Mistä dataa saa

Datalla on lukemattomia mahdollisia lähteitä, eikä kaikkia voi mitenkään listata! Mainitaan kuitenkin joitakin tyypillisiä paikkoja, joista dataa voi saada:

* **Strukturoitu**
  - **Esineiden internet** (IoT), mukaan lukien erilaiset sensorit, kuten lämpötila- tai paineanturit, tuottavat paljon hyödyllistä dataa. Esimerkiksi, jos toimistorakennus on varustettu IoT-sensoreilla, voimme automaattisesti ohjata lämmitystä ja valaistusta kustannusten minimoimiseksi.
  - **Kyselyt**, joita pyydämme käyttäjiä täyttämään ostoksen jälkeen tai verkkosivustolla vierailun jälkeen.
  - **Käyttäytymisanalyysi** voi esimerkiksi auttaa ymmärtämään, kuinka syvälle käyttäjä menee sivustolla ja mikä on tyypillinen syy sivustolta poistumiseen.
* **Strukturoimaton**
  - **Tekstit** voivat olla rikas lähde oivalluksille, kuten yleinen **tunnelmapisteytys** tai avainsanojen ja semanttisen merkityksen poiminta.
  - **Kuvat** tai **videot**. Valvontakameran videoita voidaan käyttää liikenteen arvioimiseen tiellä ja tiedottamaan mahdollisista ruuhkista.
  - Verkkopalvelimen **lokit** voivat auttaa ymmärtämään, mitkä sivuston sivut ovat useimmin vierailtuja ja kuinka kauan.
* **Puolistrukturoitu**
  - **Sosiaalisen verkoston** graafit voivat olla erinomaisia datalähteitä käyttäjien persoonallisuuksista ja tiedon levittämisen potentiaalisesta tehokkuudesta.
  - Kun meillä on joukko valokuvia juhlista, voimme yrittää poimia **ryhmädynamiikkaa** rakentamalla graafin ihmisistä, jotka ottavat kuvia toistensa kanssa.

Kun tiedät erilaiset mahdolliset datalähteet, voit miettiä erilaisia skenaarioita, joissa datatieteen tekniikoita voidaan soveltaa tilanteen parempaan ymmärtämiseen ja liiketoimintaprosessien parantamiseen.

## Mitä datalla voi tehdä

Datatieteessä keskitytään seuraaviin datan käsittelyn vaiheisiin:

## Digitalisaatio ja digitaalinen transformaatio

Viimeisen vuosikymmenen aikana monet yritykset ovat alkaneet ymmärtää datan merkityksen liiketoimintapäätösten tekemisessä. Jotta datatieteen periaatteita voidaan soveltaa liiketoiminnan pyörittämiseen, täytyy ensin kerätä dataa, eli muuttaa liiketoimintaprosessit digitaaliseen muotoon. Tätä kutsutaan **digitalisaatioksi**. Datatieteen tekniikoiden soveltaminen tähän dataan päätöksenteon ohjaamiseksi voi johtaa merkittäviin tuottavuuden parannuksiin (tai jopa liiketoiminnan suunnanmuutokseen), jota kutsutaan **digitaaliseksi transformaatioksi**.

Otetaan esimerkki. Oletetaan, että meillä on datatieteen kurssi (kuten tämä), jonka toimitamme verkossa opiskelijoille, ja haluamme käyttää datatiedettä sen parantamiseen. Miten voimme tehdä sen?

Voimme aloittaa kysymällä "Mitä voidaan digitalisoida?" Yksinkertaisin tapa olisi mitata, kuinka kauan jokaisella opiskelijalla kestää suorittaa jokainen moduuli, ja mitata saavutettu tieto antamalla monivalintatesti jokaisen moduulin lopussa. Kun keskiarvoistamme suoritusajat kaikkien opiskelijoiden kesken, voimme selvittää, mitkä moduulit aiheuttavat eniten vaikeuksia opiskelijoille ja työskennellä niiden yksinkertaistamiseksi.
Voit väittää, että tämä lähestymistapa ei ole ihanteellinen, koska moduulit voivat olla eripituisia. On luultavasti oikeudenmukaisempaa jakaa aika moduulin pituudella (merkkien lukumäärällä) ja verrata näitä arvoja sen sijaan.
Kun alamme analysoida monivalintakokeiden tuloksia, voimme yrittää selvittää, mitkä käsitteet ovat opiskelijoille vaikeita ymmärtää, ja käyttää tätä tietoa sisällön parantamiseen. Tämän saavuttamiseksi meidän on suunniteltava kokeet siten, että jokainen kysymys liittyy tiettyyn käsitteeseen tai tietokokonaisuuteen.

Jos haluamme mennä vielä pidemmälle, voimme piirtää kaavion, jossa kunkin moduulin suorittamiseen käytetty aika asetetaan vastakkain opiskelijoiden ikäryhmien kanssa. Saatamme huomata, että joissakin ikäryhmissä moduulin suorittaminen vie suhteettoman kauan tai että opiskelijat keskeyttävät ennen sen suorittamista. Tämä voi auttaa meitä antamaan ikäsuosituksia moduulille ja vähentämään ihmisten tyytymättömyyttä väärien odotusten vuoksi.

## 🚀 Haaste

Tässä haasteessa yritämme löytää Data Science -alaan liittyviä käsitteitä tarkastelemalla tekstejä. Otamme Wikipedia-artikkelin Data Sciencesta, lataamme ja käsittelemme tekstin, ja rakennamme sitten sanapilven, joka näyttää tältä:

![Sanapilvi Data Sciencesta](../../../../translated_images/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.fi.png)

Vieraile tiedostossa [`notebook.ipynb`](../../../../../../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') lukeaksesi koodin läpi. Voit myös suorittaa koodin ja nähdä, kuinka se tekee kaikki datamuunnokset reaaliajassa.

> Jos et tiedä, miten suorittaa koodia Jupyter Notebookissa, tutustu [tähän artikkeliin](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Luennon jälkeinen kysely](https://ff-quizzes.netlify.app/en/ds/)

## Tehtävät

* **Tehtävä 1**: Muokkaa yllä olevaa koodia löytääksesi liittyviä käsitteitä **Big Data**- ja **Machine Learning** -aloille.
* **Tehtävä 2**: [Pohdi Data Science -skenaarioita](assignment.md)

## Kiitokset

Tämän oppitunnin on laatinut ♥️:lla [Dmitry Soshnikov](http://soshnikov.com).

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.