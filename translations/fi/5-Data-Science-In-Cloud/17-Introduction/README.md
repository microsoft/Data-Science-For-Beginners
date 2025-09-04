<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a0556b17de4c8d1a9470b02247b01d4",
  "translation_date": "2025-09-04T19:35:51+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "fi"
}
-->
# Johdatus pilvipohjaiseen data-analytiikkaan

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Data-analytiikka pilvessä: Johdanto - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Tässä oppitunnissa opit pilvipalveluiden perusperiaatteet, näet miksi pilvipalveluiden käyttö voi olla hyödyllistä data-analytiikkaprojekteissa, ja tarkastelemme esimerkkejä pilvessä toteutetuista data-analytiikkaprojekteista.

## [Esiluennon kysely](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## Mikä on pilvi?

Pilvi, tai pilvilaskenta, tarkoittaa laajan valikoiman maksullisten laskentapalveluiden tarjoamista internetin kautta. Palveluihin kuuluu ratkaisuja, kuten tallennus, tietokannat, verkot, ohjelmistot, analytiikka ja älykkäät palvelut.

Pilvipalvelut jaetaan yleensä julkisiin, yksityisiin ja hybridipilviin seuraavasti:

* Julkinen pilvi: julkinen pilvi on kolmannen osapuolen pilvipalveluntarjoajan omistama ja ylläpitämä, ja se tarjoaa laskentaresursseja internetin kautta yleisölle.
* Yksityinen pilvi: viittaa pilvilaskentaresursseihin, joita käyttää yksinomaan yksi yritys tai organisaatio, ja palvelut sekä infrastruktuuri ylläpidetään yksityisessä verkossa.
* Hybridipilvi: hybridipilvi yhdistää julkisen ja yksityisen pilven. Käyttäjät voivat valita paikallisen datakeskuksen, mutta sallia datan ja sovellusten käytön yhdellä tai useammalla julkisella pilvellä.

Suurin osa pilvilaskentapalveluista kuuluu kolmeen kategoriaan: Infrastructure as a Service (IaaS), Platform as a Service (PaaS) ja Software as a Service (SaaS).

* Infrastructure as a Service (IaaS): käyttäjät vuokraavat IT-infrastruktuurin, kuten palvelimia, virtuaalikoneita (VM), tallennustilaa, verkkoja ja käyttöjärjestelmiä.
* Platform as a Service (PaaS): käyttäjät vuokraavat ympäristön ohjelmistosovellusten kehittämiseen, testaamiseen, toimittamiseen ja hallintaan. Käyttäjien ei tarvitse huolehtia palvelimien, tallennustilan, verkon ja tietokantojen infrastruktuurin hallinnasta.
* Software as a Service (SaaS): käyttäjät saavat pääsyn ohjelmistosovelluksiin internetin kautta, yleensä tilauspohjaisesti. Käyttäjien ei tarvitse huolehtia ohjelmiston isännöinnistä, hallinnasta tai ylläpidosta, kuten päivityksistä ja tietoturvasta.

Suurimpia pilvipalveluntarjoajia ovat Amazon Web Services, Google Cloud Platform ja Microsoft Azure.

## Miksi valita pilvi data-analytiikkaan?

Kehittäjät ja IT-ammattilaiset valitsevat pilvipalvelut monista syistä, kuten:

* Innovaatio: voit tehostaa sovelluksiasi integroimalla pilvipalveluntarjoajien innovatiivisia palveluita suoraan sovelluksiisi.
* Joustavuus: maksat vain tarvitsemistasi palveluista ja voit valita laajasta palveluvalikoimasta. Maksat yleensä käytön mukaan ja mukautat palvelut tarpeidesi mukaan.
* Budjetti: sinun ei tarvitse tehdä alkuinvestointeja laitteistojen ja ohjelmistojen ostamiseen, datakeskusten perustamiseen ja ylläpitoon, vaan maksat vain käytöstä.
* Skaalautuvuus: resurssit voivat skaalautua projektin tarpeiden mukaan, mikä tarkoittaa, että sovelluksesi voivat käyttää enemmän tai vähemmän laskentatehoa, tallennustilaa ja kaistanleveyttä ulkoisten tekijöiden mukaan.
* Tuottavuus: voit keskittyä liiketoimintaasi sen sijaan, että käyttäisit aikaa tehtäviin, jotka joku muu voi hoitaa, kuten datakeskusten hallintaan.
* Luotettavuus: pilvilaskenta tarjoaa useita tapoja varmuuskopioida dataa jatkuvasti, ja voit luoda katastrofipalautussuunnitelmia, jotka pitävät liiketoimintasi ja palvelusi käynnissä kriisitilanteissa.
* Tietoturva: voit hyödyntää politiikkoja, teknologioita ja kontrollimekanismeja, jotka vahvistavat projektisi tietoturvaa.

Nämä ovat joitakin yleisimpiä syitä, miksi ihmiset valitsevat pilvipalvelut. Nyt kun ymmärrämme paremmin, mitä pilvi on ja mitkä sen tärkeimmät edut ovat, tarkastellaan tarkemmin data-analytiikan ammattilaisten ja kehittäjien työtä sekä sitä, miten pilvi voi auttaa heitä kohtaamaan erilaisia haasteita:

* Suurten datamäärien tallentaminen: sen sijaan, että ostaisit, hallitsisit ja suojaisit suuria palvelimia, voit tallentaa datasi suoraan pilveen, esimerkiksi Azure Cosmos DB:n, Azure SQL Databasen ja Azure Data Lake Storagen avulla.
* Datan integrointi: datan integrointi on olennainen osa data-analytiikkaa, joka mahdollistaa siirtymisen datan keräämisestä toimintaan. Pilvipalveluiden tarjoamat datan integrointipalvelut, kuten Data Factory, auttavat keräämään, muuntamaan ja integroimaan dataa eri lähteistä yhteen datavarastoon.
* Datan käsittely: suurten datamäärien käsittely vaatii paljon laskentatehoa, eikä kaikilla ole pääsyä tarpeeksi tehokkaisiin koneisiin. Siksi monet valitsevat pilven valtavan laskentatehon ratkaisujensa suorittamiseen ja käyttöönottoon.
* Data-analytiikkapalveluiden käyttö: pilvipalvelut, kuten Azure Synapse Analytics, Azure Stream Analytics ja Azure Databricks, auttavat muuttamaan datan toiminnallisiksi oivalluksiksi.
* Koneoppimisen ja dataälyn palveluiden käyttö: sen sijaan, että aloittaisit alusta, voit käyttää pilvipalveluntarjoajan tarjoamia koneoppimisalgoritmeja, kuten AzureML. Voit myös hyödyntää kognitiivisia palveluita, kuten puheesta tekstiksi, tekstistä puheeksi, tietokonenäköä ja paljon muuta.

## Esimerkkejä data-analytiikasta pilvessä

Tarkastellaan muutamia konkreettisia esimerkkejä.

### Sosiaalisen median reaaliaikainen sentimenttianalyysi
Aloitetaan skenaariolla, joka on yleinen koneoppimisen aloittelijoille: sosiaalisen median sentimenttianalyysi reaaliajassa.

Oletetaan, että ylläpidät uutismedia-sivustoa ja haluat hyödyntää reaaliaikaista dataa ymmärtääksesi, millainen sisältö kiinnostaisi lukijoitasi. Tätä varten voit rakentaa ohjelman, joka suorittaa reaaliaikaista sentimenttianalyysiä Twitter-julkaisujen datasta aiheista, jotka ovat lukijoillesi merkityksellisiä.

Keskeiset indikaattorit, joita tarkastelet, ovat tiettyjen aiheiden (hashtagien) twiittien määrä ja sentimentti, joka määritetään analytiikkatyökaluilla, jotka suorittavat sentimenttianalyysiä määritettyjen aiheiden ympärillä.

Projektin luomiseen tarvittavat vaiheet ovat seuraavat:

* Luo tapahtumakeskus syötteen suoratoistolle, joka kerää dataa Twitteristä
* Määritä ja käynnistä Twitter-asiakassovellus, joka kutsuu Twitter Streaming API:ta
* Luo Stream Analytics -työ
* Määritä työn syöte ja kysely
* Luo ulostulosäiliö ja määritä työn ulostulo
* Käynnistä työ

Katso koko prosessi [dokumentaatiosta](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Tieteellisten artikkeleiden analyysi
Tarkastellaan toista esimerkkiä projektista, jonka on luonut [Dmitry Soshnikov](http://soshnikov.com), yksi tämän kurssin kirjoittajista.

Dmitry loi työkalun, joka analysoi COVID-artikkeleita. Tarkastelemalla tätä projektia näet, miten voit luoda työkalun, joka poimii tietoa tieteellisistä artikkeleista, saa oivalluksia ja auttaa tutkijoita navigoimaan suurten artikkelikokoelmien läpi tehokkaasti.

Katsotaan projektin eri vaiheet:

* Tiedon poiminta ja esikäsittely [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) avulla
* [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) -palvelun käyttö prosessoinnin rinnakkaistamiseen
* Tiedon tallennus ja kyselyt [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) avulla
* Interaktiivisen dashboardin luominen tiedon tutkimiseen ja visualisointiin Power BI:n avulla

Katso koko prosessi Dmitryn blogista [täältä](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Kuten näet, pilvipalveluita voidaan hyödyntää monin tavoin data-analytiikan toteuttamisessa.

## Loppuviite

Lähteet:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Jälkiluennon kysely

## [Jälkiluennon kysely](https://ff-quizzes.netlify.app/en/ds/)

## Tehtävä

[Markkinatutkimus](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.