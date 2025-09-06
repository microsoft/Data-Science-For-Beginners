<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-09-05T22:33:38+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "fi"
}
-->
# Johdanto pilvipohjaiseen data-analytiikkaan

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Data-analytiikka pilvessä: Johdanto - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Tässä oppitunnissa opit pilvipalveluiden perusperiaatteet, saat selville, miksi pilvipalveluiden käyttö voi olla hyödyllistä data-analytiikkaprojekteissasi, ja tarkastelemme esimerkkejä pilvessä toteutetuista data-analytiikkaprojekteista.

## [Esiluentavisa](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## Mikä on pilvi?

Pilvi, tai pilvipalvelut, tarkoittaa laajan valikoiman maksullisten tietotekniikkapalveluiden toimittamista internetin kautta ylläpidetyn infrastruktuurin avulla. Palveluihin kuuluu ratkaisuja, kuten tallennustilaa, tietokantoja, verkottumista, ohjelmistoja, analytiikkaa ja älykkäitä palveluita.

Yleensä pilvipalvelut jaetaan kolmeen kategoriaan: julkinen, yksityinen ja hybridi pilvi:

* Julkinen pilvi: julkinen pilvi on kolmannen osapuolen pilvipalveluntarjoajan omistama ja ylläpitämä, ja se toimittaa tietotekniikkapalveluita internetin kautta yleisölle.
* Yksityinen pilvi: viittaa pilvipalveluihin, joita käyttää yksinomaan yksi yritys tai organisaatio, ja palvelut sekä infrastruktuuri ylläpidetään yksityisessä verkossa.
* Hybridi pilvi: hybridi pilvi yhdistää julkisen ja yksityisen pilven. Käyttäjät voivat hyödyntää paikallista datakeskusta ja samalla ajaa dataa ja sovelluksia yhdessä tai useammassa julkisessa pilvessä.

Useimmat pilvipalvelut kuuluvat kolmeen pääkategoriaan: Infrastructure as a Service (IaaS), Platform as a Service (PaaS) ja Software as a Service (SaaS).

* Infrastructure as a Service (IaaS): käyttäjät vuokraavat IT-infrastruktuuria, kuten palvelimia ja virtuaalikoneita (VM), tallennustilaa, verkkoja ja käyttöjärjestelmiä.
* Platform as a Service (PaaS): käyttäjät vuokraavat ympäristön ohjelmistojen kehittämiseen, testaamiseen, toimittamiseen ja hallintaan. Käyttäjien ei tarvitse huolehtia palvelimien, tallennustilan, verkkojen tai tietokantojen infrastruktuurin hallinnasta.
* Software as a Service (SaaS): käyttäjät saavat pääsyn ohjelmistosovelluksiin internetin kautta tilauspohjaisesti. Käyttäjien ei tarvitse huolehtia ohjelmiston ylläpidosta, infrastruktuurista tai päivityksistä.

Suurimpia pilvipalveluntarjoajia ovat Amazon Web Services, Google Cloud Platform ja Microsoft Azure.

## Miksi valita pilvi data-analytiikkaan?

Kehittäjät ja IT-ammattilaiset valitsevat pilvipalvelut monista syistä, kuten:

* Innovaatio: voit tehostaa sovelluksiasi integroimalla pilvipalveluntarjoajien kehittämiä innovatiivisia palveluita suoraan sovelluksiisi.
* Joustavuus: maksat vain tarvitsemistasi palveluista ja voit valita laajasta palveluvalikoimasta. Maksat yleensä käytön mukaan ja voit mukauttaa palveluita tarpeidesi mukaan.
* Budjetti: sinun ei tarvitse tehdä alkuinvestointeja laitteistojen ja ohjelmistojen hankintaan tai datakeskusten perustamiseen ja ylläpitoon – maksat vain käytöstä.
* Skaalautuvuus: resurssit voivat skaalautua projektisi tarpeiden mukaan, mikä tarkoittaa, että sovelluksesi voivat käyttää enemmän tai vähemmän laskentatehoa, tallennustilaa ja kaistanleveyttä ulkoisten tekijöiden mukaan.
* Tuottavuus: voit keskittyä liiketoimintaasi sen sijaan, että käyttäisit aikaa tehtäviin, jotka joku muu voi hoitaa, kuten datakeskusten hallintaan.
* Luotettavuus: pilvipalvelut tarjoavat useita tapoja varmuuskopioida dataasi jatkuvasti, ja voit luoda katastrofipalautussuunnitelmia, jotta liiketoimintasi ja palvelusi pysyvät toiminnassa kriisitilanteissa.
* Turvallisuus: voit hyödyntää käytäntöjä, teknologioita ja valvontaa, jotka vahvistavat projektisi turvallisuutta.

Nämä ovat joitakin yleisimpiä syitä, miksi ihmiset valitsevat pilvipalvelut. Nyt kun ymmärrämme paremmin, mitä pilvi on ja mitkä ovat sen tärkeimmät hyödyt, tarkastellaan tarkemmin data-analyytikoiden ja datan parissa työskentelevien kehittäjien tehtäviä sekä sitä, miten pilvi voi auttaa heitä kohtaamaan erilaisia haasteita:

* Suurten datamäärien tallentaminen: sen sijaan, että ostaisit, hallinnoisit ja suojaisit suuria palvelimia, voit tallentaa datasi suoraan pilveen, esimerkiksi Azure Cosmos DB:n, Azure SQL Databasen ja Azure Data Lake Storagen avulla.
* Datan integrointi: datan integrointi on olennainen osa data-analytiikkaa, joka mahdollistaa siirtymisen datan keräämisestä toimenpiteisiin. Pilvipalveluiden tarjoamilla dataintegraatiopalveluilla voit kerätä, muuntaa ja yhdistää dataa eri lähteistä yhdeksi tietovarastoksi, esimerkiksi Data Factoryn avulla.
* Datan käsittely: suurten datamäärien käsittely vaatii paljon laskentatehoa, eikä kaikilla ole pääsyä tarpeeksi tehokkaisiin koneisiin. Siksi monet valitsevat suoraan pilven valtavan laskentatehon ratkaisujensa suorittamiseen ja käyttöönottoon.
* Data-analytiikkapalveluiden käyttö: pilvipalvelut, kuten Azure Synapse Analytics, Azure Stream Analytics ja Azure Databricks, auttavat muuttamaan datasi toimiviksi oivalluksiksi.
* Koneoppimisen ja älypalveluiden käyttö: sen sijaan, että aloittaisit alusta, voit käyttää pilvipalveluntarjoajan tarjoamia koneoppimisalgoritmeja, kuten AzureML. Voit myös hyödyntää kognitiivisia palveluita, kuten puheesta tekstiksi, tekstistä puheeksi, tietokonenäköä ja paljon muuta.

## Esimerkkejä data-analytiikasta pilvessä

Tarkastellaan muutamia käytännön esimerkkejä.

### Sosiaalisen median reaaliaikainen sentimenttianalyysi
Aloitetaan skenaariolla, jota monet koneoppimisen aloittelijat tutkivat: sosiaalisen median sentimenttianalyysi reaaliajassa.

Oletetaan, että ylläpidät uutismedia-sivustoa ja haluat hyödyntää reaaliaikaista dataa ymmärtääksesi, millainen sisältö kiinnostaa lukijoitasi. Tämän selvittämiseksi voit rakentaa ohjelman, joka suorittaa reaaliaikaista sentimenttianalyysiä Twitter-julkaisujen datasta aiheista, jotka ovat lukijoillesi merkityksellisiä.

Keskeisiä mittareita ovat tiettyihin aiheisiin liittyvien twiittien määrä (hashtagit) ja sentimentti, joka määritetään analytiikkatyökaluilla, jotka suorittavat sentimenttianalyysiä määriteltyjen aiheiden ympärillä.

Projektin luomiseen tarvittavat vaiheet ovat seuraavat:

* Luo tapahtumakeskus syötteen suoratoistoon, joka kerää dataa Twitteristä.
* Määritä ja käynnistä Twitter-asiakassovellus, joka kutsuu Twitterin suoratoisto-API:ta.
* Luo Stream Analytics -työ.
* Määritä työn syöte ja kysely.
* Luo ulostulosäilö ja määritä työn ulostulo.
* Käynnistä työ.

Katso koko prosessi [dokumentaatiosta](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Tieteellisten julkaisujen analyysi
Tarkastellaan toista esimerkkiä projektista, jonka on luonut [Dmitry Soshnikov](http://soshnikov.com), yksi tämän kurssin kirjoittajista.

Dmitry loi työkalun, joka analysoi COVID-tutkimusjulkaisuja. Tämän projektin avulla näet, kuinka voit luoda työkalun, joka poimii tietoa tieteellisistä julkaisuista, saa oivalluksia ja auttaa tutkijoita navigoimaan suurten julkaisukokoelmien läpi tehokkaasti.

Katsotaanpa projektin eri vaiheet:

* Tiedon poiminta ja esikäsittely [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) -työkalulla.
* [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) -palvelun käyttö prosessoinnin rinnakkaistamiseen.
* Tiedon tallentaminen ja kyselyt [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) -palvelulla.
* Interaktiivisen kojelaudan luominen tiedon tutkimiseen ja visualisointiin Power BI:n avulla.

Katso koko prosessi [Dmitryn blogista](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Kuten huomaat, pilvipalveluita voidaan hyödyntää monin tavoin data-analytiikassa.

## Loppuviite

Lähteet:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Jälkiluentavisa

## [Jälkiluentavisa](https://ff-quizzes.netlify.app/en/ds/quiz/33)

## Tehtävä

[Markkinatutkimus](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.