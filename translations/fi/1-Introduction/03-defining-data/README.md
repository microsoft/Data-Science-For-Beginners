<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "12339119c0165da569a93ddba05f9339",
  "translation_date": "2025-09-05T22:49:52+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "fi"
}
-->
# Määritellään dataa

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Datan määrittely - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Data on faktoja, tietoa, havaintoja ja mittauksia, joita käytetään löytöjen tekemiseen ja perusteltujen päätösten tukemiseen. Datapiste on yksittäinen datayksikkö datasetissä, joka on kokoelma datapisteitä. Datasetit voivat olla eri muodoissa ja rakenteissa, ja ne perustuvat yleensä lähteeseensä eli siihen, mistä data on peräisin. Esimerkiksi yrityksen kuukausittaiset tulot voivat olla taulukkolaskennassa, mutta älykellon tuntikohtaiset syketiedot voivat olla [JSON](https://stackoverflow.com/a/383699)-muodossa. On yleistä, että data-analyytikot työskentelevät erilaisten datatyyppien kanssa samassa datasetissä.

Tämä oppitunti keskittyy datan tunnistamiseen ja luokitteluun sen ominaisuuksien ja lähteiden perusteella.

## [Esiluennon kysely](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Miten dataa kuvataan

### Raakadata
Raakadata on dataa, joka on peräisin lähteestään alkuperäisessä muodossaan eikä sitä ole analysoitu tai järjestetty. Jotta datasetistä saataisiin selkoa, se täytyy järjestää muotoon, joka on ymmärrettävä ihmisille sekä teknologialle, jota he voivat käyttää sen jatkoanalysointiin. Datasetin rakenne kuvaa, miten se on järjestetty, ja se voidaan luokitella rakenteelliseksi, rakenteettomaksi ja puolirakenteelliseksi. Nämä rakenteet vaihtelevat lähteen mukaan, mutta ne kuuluvat lopulta näihin kolmeen kategoriaan.

### Kvantitatiivinen data
Kvantitatiivinen data on datasetin numeerisia havaintoja, joita voidaan yleensä analysoida, mitata ja käyttää matemaattisesti. Esimerkkejä kvantitatiivisesta datasta ovat: maan väkiluku, henkilön pituus tai yrityksen neljännesvuosittaiset tulot. Lisäanalyysin avulla kvantitatiivista dataa voitaisiin käyttää esimerkiksi ilmanlaatuindeksin (AQI) kausitrendien löytämiseen tai arvioimaan ruuhka-ajan liikenteen todennäköisyyttä tyypillisenä työpäivänä.

### Kvalitatiivinen data
Kvalitatiivinen data, joka tunnetaan myös kategorisena datana, on dataa, jota ei voida mitata objektiivisesti kuten kvantitatiivista dataa. Se on yleensä subjektiivista dataa, joka kuvaa jonkin asian laatua, kuten tuotetta tai prosessia. Joskus kvalitatiivinen data on numeerista, mutta sitä ei yleensä käytetä matemaattisesti, kuten puhelinnumerot tai aikaleimat. Esimerkkejä kvalitatiivisesta datasta ovat: videokommentit, auton merkki ja malli tai lähimpien ystäviesi suosikkiväri. Kvalitatiivista dataa voitaisiin käyttää esimerkiksi ymmärtämään, mitkä tuotteet kuluttajat pitävät parhaimpina tai tunnistamaan suosittuja avainsanoja työhakemusten ansioluetteloista.

### Rakenteellinen data
Rakenteellinen data on dataa, joka on järjestetty riveihin ja sarakkeisiin, joissa jokaisella rivillä on sama sarakejoukko. Sarakkeet edustavat tietyn tyyppistä arvoa ja ne tunnistetaan nimellä, joka kuvaa, mitä arvo edustaa, kun taas rivit sisältävät varsinaiset arvot. Sarakkeilla on usein erityiset säännöt tai rajoitukset arvoille, jotta arvot edustavat saraketta tarkasti. Esimerkiksi kuvittele asiakastaulukko, jossa jokaisella rivillä täytyy olla puhelinnumero, eikä puhelinnumerot koskaan sisällä aakkosmerkkejä. Puhelinnumerosarakkeeseen voidaan soveltaa sääntöjä, jotka varmistavat, että se ei ole koskaan tyhjä ja sisältää vain numeroita.

Rakenteellisen datan etuna on, että se voidaan järjestää tavalla, joka mahdollistaa sen yhdistämisen toiseen rakenteelliseen dataan. Koska data on suunniteltu järjestettäväksi tietyllä tavalla, sen rakenteen muuttaminen voi kuitenkin vaatia paljon vaivaa. Esimerkiksi jos asiakastaulukkoon lisätään sähköpostisarakke, joka ei voi olla tyhjä, täytyy miettiä, miten nämä arvot lisätään olemassa oleviin asiakasriveihin datasetissä.

Esimerkkejä rakenteellisesta datasta: taulukkolaskennat, relaatiotietokannat, puhelinnumerot, tiliotteet

### Rakenteeton data
Rakenteeton data ei yleensä sovi riveihin tai sarakkeisiin eikä sisällä muotoa tai sääntöjä, joita noudattaa. Koska rakenteettomalla datalla on vähemmän rajoituksia rakenteelleen, uuden tiedon lisääminen on helpompaa verrattuna rakenteelliseen datasettiin. Jos sensori, joka tallentaa ilmanpaineen dataa kahden minuutin välein, saa päivityksen, joka mahdollistaa lämpötilan mittaamisen ja tallentamisen, se ei vaadi olemassa olevan datan muuttamista, jos se on rakenteetonta. Tämä voi kuitenkin tehdä tällaisen datan analysoinnista tai tutkimisesta aikaa vievää. Esimerkiksi tutkija, joka haluaa löytää keskimääräisen lämpötilan edelliseltä kuukaudelta sensorin datasta, mutta huomaa, että sensori on tallentanut "e"-kirjaimen joihinkin tietoihinsa merkiksi siitä, että se oli rikki, mikä tarkoittaa, että data on puutteellista.

Esimerkkejä rakenteettomasta datasta: tekstiedostot, tekstiviestit, videotiedostot

### Puolirakenteellinen data
Puolirakenteellisellä datalla on ominaisuuksia, jotka tekevät siitä rakenteellisen ja rakenteettoman datan yhdistelmän. Se ei yleensä noudata rivien ja sarakkeiden muotoa, mutta se on järjestetty tavalla, joka katsotaan rakenteelliseksi ja voi noudattaa kiinteää muotoa tai sääntöjä. Rakenne vaihtelee lähteiden välillä, kuten hyvin määritellystä hierarkiasta joustavampaan muotoon, joka mahdollistaa uuden tiedon helpon integroinnin. Metadata ovat indikaattoreita, jotka auttavat päättämään, miten data on järjestetty ja tallennettu, ja niillä on erilaisia nimiä datatyypistä riippuen. Joitakin yleisiä metadatan nimiä ovat tagit, elementit, entiteetit ja attribuutit. Esimerkiksi tyypillinen sähköpostiviesti sisältää aiheen, tekstin ja vastaanottajien joukon, ja se voidaan järjestää lähettäjän tai lähetysajan mukaan.

Esimerkkejä puolirakenteellisestä datasta: HTML, CSV-tiedostot, JavaScript Object Notation (JSON)

## Datan lähteet 

Datalähde on alkuperäinen sijainti, jossa data on luotu tai missä se "elää", ja se vaihtelee sen mukaan, miten ja milloin se on kerätty. Käyttäjien tuottama data tunnetaan primääridatana, kun taas sekundääridata tulee lähteestä, joka on kerännyt dataa yleiseen käyttöön. Esimerkiksi ryhmä tutkijoita, jotka keräävät havaintoja sademetsässä, katsottaisiin primääridataksi, ja jos he päättävät jakaa sen muiden tutkijoiden kanssa, se katsottaisiin sekundääridataksi niille, jotka käyttävät sitä.

Tietokannat ovat yleinen lähde ja ne käyttävät tietokannan hallintajärjestelmää datan isännöintiin ja ylläpitoon, jossa käyttäjät käyttävät komentoja, joita kutsutaan kyselyiksi, datan tutkimiseen. Tiedostot datalähteinä voivat olla ääni-, kuva- ja videotiedostoja sekä taulukkolaskentoja, kuten Excel. Internetlähteet ovat yleinen sijainti datan isännöintiin, jossa tietokantoja ja tiedostoja voidaan löytää. Sovellusohjelmointirajapinnat, jotka tunnetaan myös nimellä API:t, mahdollistavat ohjelmoijien luoda tapoja jakaa dataa ulkoisille käyttäjille internetin kautta, kun taas verkkosivujen kaavinta (web scraping) poimii dataa verkkosivulta. [Oppitunnit datan kanssa työskentelystä](../../../../../../../../../2-Working-With-Data) keskittyvät siihen, miten käyttää erilaisia datalähteitä.

## Yhteenveto

Tässä oppitunnissa opimme:

- Mitä data on
- Miten dataa kuvataan
- Miten dataa luokitellaan ja kategorisoidaan
- Mistä dataa voi löytää

## 🚀 Haaste

Kaggle on erinomainen lähde avoimille dataseteille. Käytä [dataset-hakutyökalua](https://www.kaggle.com/datasets) löytääksesi mielenkiintoisia datasettejä ja luokittele 3-5 datasettiä seuraavien kriteerien mukaan:

- Onko data kvantitatiivista vai kvalitatiivista?
- Onko data rakenteellista, rakenteetonta vai puolirakenteellista?

## [Luennon jälkeinen kysely](https://ff-quizzes.netlify.app/en/ds/quiz/5)

## Kertaus ja itseopiskelu

- Tämä Microsoft Learn -yksikkö, nimeltään [Classify your Data](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data), sisältää yksityiskohtaisen erittelyn rakenteellisesta, puolirakenteellisesta ja rakenteettomasta datasta.

## Tehtävä

[Datasettien luokittelu](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskääntämistä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virhetulkinnoista.