# Datan Määrittely

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Datan määrittely - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Data on faktoja, tietoa, havaintoja ja mittauksia, joita käytetään löytöjen tekemiseen ja perusteltujen päätösten tukemiseen. Datan piste on yksittäinen datapiste tietoaineistossa, joka on datapisteiden kokoelma. Tietoaineistot voivat olla eri muodoissa ja rakenteissa, ja ne perustuvat yleensä lähteeseensä eli mistä data on peräisin. Esimerkiksi yrityksen kuukausitulo saattaa olla taulukkolaskentaohjelmassa, mutta älykellon tuntikohtainen syketieto voi olla [JSON](https://stackoverflow.com/a/383699) -muodossa. On yleistä, että datatieteilijät työskentelevät erilaisten datatyyppien kanssa samassa tietoaineistossa.

Tämä oppitunti keskittyy datan tunnistamiseen ja luokitteluun sen ominaisuuksien ja lähteiden mukaan.

## [Ennakkotehtävä](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Kuinka dataa kuvataan

### Raakadatan
Raadata on dataa, joka on tullut lähteestään alkuperäisessä muodossaan eikä sitä ole analysoitu tai järjestetty. Jotta tiedostoista voisi saada merkityksen, se on järjestettävä ihmisten ja teknologian ymmärtämään muotoon, jota voidaan analysoida edelleen. Tietoaineiston rakenne kuvaa, miten se on järjestetty, ja se voidaan luokitella rakenteelliseksi, rakenteettomaksi tai puolistrukturoiduksi. Näiden rakennetyyppien muoto vaihtelee lähteen mukaan, mutta ne sopivat yleensä näihin kolmeen luokkaan.

### Kvantitatiivinen Data
Kvantitatiivinen data koostuu numeerisista havainnoista tietoaineistossa, joita voidaan tyypillisesti analysoida, mitata ja käyttää matemaattisesti. Esimerkkejä kvantitatiivisesta datasta ovat: maan väestö, henkilön pituus tai yrityksen neljännesvuositulokset. Jatkoanalyysin avulla kvantitatiivista dataa voidaan käyttää esimerkiksi ilmanlaatuindeksin (AQI) kausivaihteluiden tutkimiseen tai ruuhka-aikojen todennäköisyyden arvioimiseen tyypillisenä arkipäivänä.

### Kvalitatiivinen Data
Kvalitatiivinen data, joka tunnetaan myös kategorisena datana, on dataa, jota ei voida mitata objektiivisesti kuten kvantitatiivista dataa. Se koostuu yleensä erilaisista subjektiivisista tiedoista, jotka kuvaavat jonkin asian laatua, kuten tuotetta tai prosessia. Joissakin tapauksissa kvalitatiivinen data on numeerista, mutta sitä ei normaalisti käytetä matemaattisesti, kuten puhelinnumerot tai aikaleimat. Esimerkkejä kvalitatiivisesta datasta ovat: videokommentit, auton merkki ja malli tai lähimpien ystäviesi lempiväri. Kvalitatiivista dataa voidaan käyttää esimerkiksi selvittämään, mitkä tuotteet kuluttajat pitävät parhaimpina tai tunnistamaan suosittuja hakusanoja työhakemuksissa.

### Rakenteellinen Data
Rakenteellinen data on dataa, joka on järjestetty riveihin ja sarakkeisiin siten, että jokaisella rivillä on sama sarjallinen sarakkeita. Sarakkeet edustavat tietyn tyyppistä arvoa ja niillä on nimi, joka kuvaa, mitä arvo tarkoittaa, kun taas rivit sisältävät varsinaiset arvot. Sarakkeilla on usein tiettyjen arvojen säännöt tai rajoitukset, jotka varmistavat, että arvot kuvaavat saraketta tarkasti. Kuvittele esimerkiksi asiakastietojen taulukko, jossa jokaisella rivillä on oltava puhelinnumero, eikä puhelinnumerot saa sisältää kirjaimia. Puhelinnumerosarakkeeseen voi olla sovellettuna sääntöjä, jotka varmistavat, että se ei ole koskaan tyhjä ja sisältää vain numeroita.

Rakenteellisen datan etuna on, että sitä voidaan järjestää siten, että sitä voidaan yhdistää muuhun rakenteelliseen dataan. Koska data on suunniteltu tiettyyn rakenteeseen, rakenteen muuttaminen voi kuitenkin vaatia paljon työtä. Esimerkiksi sähköpostisarakkeen lisääminen asiakastietojen taulukkoon, joka ei saa olla tyhjä, tarkoittaa, että sinun on päätettävä, miten lisäät nämä arvot olemassa oleviin asiakasriveihin datassa.

Esimerkkejä rakenteellisesta datasta: taulukkolaskelmat, relaatiotietokannat, puhelinnumerot, pankkitilitiedot

### Rakenteeton Data
Rakenteetonta dataa ei tyypillisesti voi luokitella riveihin tai sarakkeisiin, eikä sillä ole selkeää muotoa tai sääntöjä. Koska rakenteettomalla datalla on vähemmän rakenteellisia rajoitteita, uuden tiedon lisääminen on helpompaa verrattuna rakenteelliseen aineistoon. Jos anturi, joka mittaa barometripainetta kahden minuutin välein, saa päivityksen, joka antaa sen mitata ja tallentaa myös lämpötilaa, tämä ei vaadi olemassa olevan datan muuttamista, jos se on rakenteetonta. Tämä voi kuitenkin pidentää tämän tyyppisen datan analysointi- tai tutkimusaikaa. Esimerkiksi tutkija, joka haluaa löytää anturidatan perusteella keskimääräisen lämpötilan edelliseltä kuukaudelta, voi huomata, että anturi on merkinnyt osaan tallennettua dataa kirjain "e" osoittamaan, että se oli rikki, ei normaalia lukua, jolloin data on epätäydellistä.

Esimerkkejä rakenteettomasta datasta: tekstitiedostot, tekstiviestit, videotiedostot

### Puolistrukturoitu Data
Puolistrukturoitu data sisältää piirteitä, jotka yhdistävät rakenteellisen ja rakenteettoman datan ominaisuuksia. Se ei tyypillisesti noudata sarakkeiden ja rivien muotoa, mutta on järjestetty rakenteellisesti ja saattaa noudattaa kiinteää muotoa tai sääntöjä. Rakenne vaihtelee lähteittäin, kuten tarkkaan määritelty hierarkia tai joustavampi rakenne, joka mahdollistaa uuden tiedon helpon integroinnin. Metadata ovat indikaattoreita, jotka auttavat päättämään, miten data on järjestetty ja tallennettu, ja niitä kutsutaan eri nimillä datan tyypistä riippuen. Yleisiä metadatan nimiä ovat tagit, elementit, entiteetit ja attribuutit. Esimerkiksi tyypillisellä sähköpostiviestillä on otsikko, runko ja vastaanottajalista, ja sitä voidaan järjestää lähettäjän tai lähetysajan mukaan.

Esimerkkejä puolistrukturoidusta datasta: HTML, CSV-tiedostot, JavaScript Object Notation (JSON)

## Datan Lähteet

Datalähde on paikka, jossa data on alun perin generoitu tai jossa se "asuu", ja se vaihtelee sen mukaan, miten ja milloin data on kerätty. Käyttäjän tai käyttäjien generoima data tunnetaan ensisijaisena datana, kun taas toissijainen data tulee lähteestä, joka on kerännyt dataa yleistä käyttöä varten. Esimerkiksi ryhmä tutkijoita, jotka keräävät havaintoja sademetsästä, edustaa ensisijaista dataa, ja jos he päättävät jakaa sen muiden tutkijoiden kanssa, se on toissijaista niille, jotka käyttävät sitä.

Tietokannat ovat yleinen lähde, ja ne käyttävät tietokannan hallintajärjestelmää datan ylläpitoon, jossa käyttäjät käyttävät kyselyjä tutkiakseen dataa. Tiedostojen datalähteet voivat olla ääni-, kuva- ja videotiedostoja sekä taulukkolaskentatiedostoja, kuten Excel. Internet-lähteet ovat yleinen paikka datan ylläpitoon, jossa sekä tietokannat että tiedostot löytyvät. Sovellusrajapinnat eli API:t antavat kehittäjille keinon jakaa dataa ulkoisille käyttäjille internetin kautta, kun taas verkkosivujen tietojen poiminta eli web scraping kerää dataa verkkosivulta. [Työskentely datan kanssa](../../../../../../../../../2-Working-With-Data) -oppitunnit keskittyvät eri datalähteiden käyttöön.

## Yhteenveto

Tässä oppitunnissa olemme oppineet:

- Mitä data on
- Miten data kuvataan
- Miten data luokitellaan ja luokitellaan
- Mistä dataa löytyy

## 🚀 Haaste

Kaggle on erinomainen avoimen datan lähde. Käytä [dataset search tool](https://www.kaggle.com/datasets) -työkalua löytääksesi mielenkiintoisia datakokoelmia ja luokittele 3-5 dataset:iä seuraavien kriteerien mukaan:

- Onko data kvantitatiivista vai kvalitatiivista?
- Onko data rakenteellista, rakenteetonta vai puolistrukturoitua?

## [Luentotehtävä](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Kertausta ja Itseopiskelua

- Tämä Microsoft Learn -yksikkö, nimeltään [Identify data formats](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text), tarjoaa yksityiskohtaisen erittelyn rakenteellisesta, puolistrukturoidusta ja rakenteettomasta datasta.

## Tehtävä

[Datasetien luokittelu](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->