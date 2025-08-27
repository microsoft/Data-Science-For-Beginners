<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "408c55cab2880daa4e78616308bd5db7",
  "translation_date": "2025-08-26T22:10:18+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "fi"
}
-->
# Johdanto pilvipohjaiseen data-analytiikkaan

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Data-analytiikka pilvessä: Johdanto - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Tässä oppitunnissa opit pilvipalveluiden perusperiaatteet, näet, miksi pilvipalveluiden käyttö voi olla hyödyllistä data-analytiikkaprojekteissasi, ja tarkastelemme esimerkkejä pilvessä toteutetuista data-analytiikkaprojekteista.

## [Esiluentakysely](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/32)

## Mikä on pilvi?

Pilvi, tai pilvipalvelut, tarkoittaa laajan valikoiman maksullisten tietotekniikkapalveluiden toimittamista internetin kautta. Näihin palveluihin kuuluvat esimerkiksi tallennusratkaisut, tietokannat, verkot, ohjelmistot, analytiikka ja älykkäät palvelut.

Pilvipalvelut jaetaan yleensä kolmeen kategoriaan: julkinen pilvi, yksityinen pilvi ja hybridi pilvi:

* **Julkinen pilvi**: Julkinen pilvi on kolmannen osapuolen pilvipalveluntarjoajan omistama ja hallinnoima, ja se tarjoaa tietotekniikkapalveluita internetin kautta yleisölle.
* **Yksityinen pilvi**: Yksityinen pilvi tarkoittaa pilvipalveluita, joita käyttää vain yksi yritys tai organisaatio, ja palvelut sekä infrastruktuuri ylläpidetään yksityisessä verkossa.
* **Hybridi pilvi**: Hybridi pilvi yhdistää julkisen ja yksityisen pilven. Käyttäjät voivat hyödyntää paikallista datakeskusta ja samalla ajaa dataa ja sovelluksia yhdellä tai useammalla julkisella pilvellä.

Useimmat pilvipalvelut kuuluvat kolmeen pääkategoriaan: Infrastructure as a Service (IaaS), Platform as a Service (PaaS) ja Software as a Service (SaaS).

* **Infrastructure as a Service (IaaS)**: Käyttäjät vuokraavat IT-infrastruktuuria, kuten palvelimia, virtuaalikoneita (VM), tallennustilaa, verkkoja ja käyttöjärjestelmiä.
* **Platform as a Service (PaaS)**: Käyttäjät vuokraavat ympäristön ohjelmistosovellusten kehittämiseen, testaamiseen, toimittamiseen ja hallintaan ilman, että heidän tarvitsee huolehtia palvelimien, tallennustilan, verkkojen ja tietokantojen infrastruktuurista.
* **Software as a Service (SaaS)**: Käyttäjät saavat pääsyn ohjelmistosovelluksiin internetin kautta tilauspohjaisesti ilman, että heidän tarvitsee huolehtia sovelluksen ylläpidosta, infrastruktuurista tai päivityksistä.

Suurimpia pilvipalveluntarjoajia ovat Amazon Web Services, Google Cloud Platform ja Microsoft Azure.

## Miksi valita pilvi data-analytiikkaan?

Kehittäjät ja IT-ammattilaiset valitsevat pilvipalvelut monista syistä, kuten:

* **Innovaatio**: Voit hyödyntää pilvipalveluntarjoajien innovatiivisia palveluita suoraan sovelluksissasi.
* **Joustavuus**: Maksat vain tarvitsemistasi palveluista ja voit valita laajasta palveluvalikoimasta. Maksat käytön mukaan ja voit mukauttaa palveluita tarpeidesi mukaan.
* **Budjetti**: Sinun ei tarvitse tehdä alkuinvestointeja laitteistojen ja ohjelmistojen hankintaan tai datakeskusten perustamiseen ja ylläpitoon – maksat vain käytöstä.
* **Skaalautuvuus**: Resurssit skaalautuvat projektisi tarpeiden mukaan, mikä tarkoittaa, että sovelluksesi voivat käyttää enemmän tai vähemmän laskentatehoa, tallennustilaa ja kaistanleveyttä ulkoisten tekijöiden mukaan.
* **Tuottavuus**: Voit keskittyä liiketoimintaasi sen sijaan, että käyttäisit aikaa tehtäviin, jotka joku muu voi hoitaa, kuten datakeskusten hallintaan.
* **Luotettavuus**: Pilvipalvelut tarjoavat useita tapoja varmuuskopioida dataa jatkuvasti ja voit luoda katastrofipalautussuunnitelmia, jotta liiketoimintasi ja palvelusi pysyvät toiminnassa myös kriisitilanteissa.
* **Turvallisuus**: Hyödyt käytännöistä, teknologioista ja valvontamekanismeista, jotka vahvistavat projektisi turvallisuutta.

Nämä ovat joitakin yleisimmistä syistä, miksi ihmiset valitsevat pilvipalvelut. Nyt kun ymmärrämme paremmin, mitä pilvi on ja mitkä sen tärkeimmät hyödyt ovat, tarkastellaan tarkemmin data-analytiikan ja datan parissa työskentelevien kehittäjien haasteita ja sitä, miten pilvi voi auttaa heitä:

* **Suurten datamäärien tallentaminen**: Sen sijaan, että ostaisit, hallinnoisit ja suojaisit suuria palvelimia, voit tallentaa datasi suoraan pilveen, esimerkiksi Azure Cosmos DB:n, Azure SQL Databasen ja Azure Data Lake Storagen avulla.
* **Datan integrointi**: Datan integrointi on olennainen osa data-analytiikkaa, joka mahdollistaa siirtymisen datan keräämisestä toimenpiteisiin. Pilvipalveluiden tarjoamien dataintegraatiopalveluiden avulla voit kerätä, muuntaa ja integroida dataa eri lähteistä yhteen datavarastoon, esimerkiksi Data Factoryn avulla.
* **Datan käsittely**: Suurten datamäärien käsittely vaatii paljon laskentatehoa, eikä kaikilla ole pääsyä riittävän tehokkaisiin koneisiin. Siksi monet valitsevat pilven valtavan laskentatehon ratkaisujensa ajamiseen ja käyttöönottoon.
* **Data-analytiikkapalveluiden käyttö**: Pilvipalvelut, kuten Azure Synapse Analytics, Azure Stream Analytics ja Azure Databricks, auttavat muuttamaan datan toiminnallisiksi oivalluksiksi.
* **Koneoppimisen ja älykkäiden palveluiden käyttö**: Sen sijaan, että aloittaisit alusta, voit käyttää pilvipalveluntarjoajan tarjoamia koneoppimisalgoritmeja, kuten AzureML:n avulla. Voit myös hyödyntää kognitiivisia palveluita, kuten puheesta tekstiksi, tekstistä puheeksi, tietokonenäköä ja paljon muuta.

## Esimerkkejä data-analytiikasta pilvessä

Tarkastellaan muutamaa konkreettista esimerkkiä.

### Sosiaalisen median reaaliaikainen sentimenttianalyysi
Aloitetaan skenaariolla, joka on yleinen koneoppimisen aloittelijoille: sosiaalisen median sentimenttianalyysi reaaliajassa.

Oletetaan, että ylläpidät uutismedia-sivustoa ja haluat hyödyntää reaaliaikaista dataa ymmärtääksesi, millainen sisältö kiinnostaa lukijoitasi. Tätä varten voit rakentaa ohjelman, joka suorittaa reaaliaikaista sentimenttianalyysiä Twitter-julkaisujen datasta aiheista, jotka ovat lukijoillesi merkityksellisiä.

Keskeisiä mittareita ovat tiettyihin aiheisiin (hashtageihin) liittyvien twiittien määrä ja sentimentti, joka määritetään analytiikkatyökaluilla.

Projektin vaiheet ovat seuraavat:

* Luo tapahtumakeskus (event hub) syötteen suoratoistoon, joka kerää dataa Twitteristä.
* Määritä ja käynnistä Twitter-asiakassovellus, joka kutsuu Twitterin suoratoisto-API:ta.
* Luo Stream Analytics -työ.
* Määritä työn syöte ja kysely.
* Luo ulostulosäilö ja määritä työn ulostulo.
* Käynnistä työ.

Katso koko prosessi [dokumentaatiosta](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Tieteellisten julkaisujen analyysi
Tarkastellaan toista esimerkkiä projektista, jonka on luonut [Dmitry Soshnikov](http://soshnikov.com), yksi tämän oppimateriaalin kirjoittajista.

Dmitry loi työkalun, joka analysoi COVID-tutkimusjulkaisuja. Tämän projektin avulla näet, miten voit luoda työkalun, joka poimii tietoa tieteellisistä julkaisuista, tuottaa oivalluksia ja auttaa tutkijoita navigoimaan suurten julkaisukokoelmien läpi tehokkaasti.

Projektin vaiheet:

* Tiedon poiminta ja esikäsittely [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) -työkalulla.
* [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109):n käyttö prosessoinnin rinnakkaistamiseen.
* Tiedon tallentaminen ja kyselyt [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109):n avulla.
* Interaktiivisen kojelaudan luominen datan tutkimiseen ja visualisointiin Power BI:llä.

Katso koko prosessi [Dmitryn blogista](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Kuten näet, pilvipalveluita voidaan hyödyntää monin tavoin data-analytiikassa.

## Loppuviite

Lähteet:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Jälkiluentakysely

[Jälkiluentakysely](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/33)

## Tehtävä

[Markkinatutkimus](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.