<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1341f6da63d434f5ba31b08ea951b02c",
  "translation_date": "2025-09-05T22:50:15+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "fi"
}
-->
# Johdanto datan etiikkaan

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Datan etiikka - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

---

Elämme kaikki datan kansalaisina datavetoisessa maailmassa.

Markkinatrendit osoittavat, että vuoteen 2022 mennessä yksi kolmesta suuresta organisaatiosta ostaa ja myy dataansa verkossa [markkinapaikkojen ja vaihtojen](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/) kautta. **Sovelluskehittäjinä** meidän on helpompaa ja edullisempaa integroida dataan perustuvia oivalluksia ja algoritmipohjaista automaatiota päivittäisiin käyttäjäkokemuksiin. Mutta kun tekoälystä tulee yhä yleisempää, meidän on myös ymmärrettävä, millaisia haittoja tällaisilla algoritmeilla voi olla, kun niitä käytetään [aseistettuna](https://www.youtube.com/watch?v=TQHs8SA1qpk) laajassa mittakaavassa.

Trendit osoittavat myös, että vuoteen 2025 mennessä luomme ja kulutamme yli [180 zettatavua](https://www.statista.com/statistics/871513/worldwide-data-created/) dataa. **Data-analyytikkoina** tämä antaa meille ennennäkemättömän pääsyn henkilökohtaisiin tietoihin. Tämä tarkoittaa, että voimme rakentaa käyttäjien käyttäytymisprofiileja ja vaikuttaa päätöksentekoon tavoilla, jotka luovat [illuusion vapaasta valinnasta](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice), samalla kun saatamme ohjata käyttäjiä kohti meille mieluisia lopputuloksia. Tämä herättää myös laajempia kysymyksiä tietosuojasta ja käyttäjien suojelusta.

Datan etiikka toimii nyt _välttämättöminä suojakaiteina_ data-analytiikassa ja -insinöörityössä, auttaen minimoimaan mahdollisia haittoja ja tahattomia seurauksia datavetoisista toimistamme. [Gartnerin Hype Cycle tekoälylle](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) tunnistaa digietiikan, vastuullisen tekoälyn ja tekoälyn hallinnan keskeisiksi trendeiksi, jotka ohjaavat suurempia megatrendejä, kuten tekoälyn _demokratisointia_ ja _teollistamista_.

![Gartnerin Hype Cycle tekoälylle - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

Tässä oppitunnissa tutkimme kiehtovaa datan etiikan aluetta - ydinkäsitteistä ja haasteista tapaustutkimuksiin ja soveltaviin tekoälykonsepteihin, kuten hallintoon, jotka auttavat luomaan eettisen kulttuurin tiimeissä ja organisaatioissa, jotka työskentelevät datan ja tekoälyn parissa.

## [Esiluentovisa](https://ff-quizzes.netlify.app/en/ds/quiz/2) 🎯

## Perusmääritelmät

Aloitetaan ymmärtämällä peruskäsitteitä.

Sana "etiikka" tulee [kreikan sanasta "ethikos"](https://en.wikipedia.org/wiki/Ethics) (ja sen juuresta "ethos"), joka tarkoittaa _luonnetta tai moraalista olemusta_.

**Etiikka** käsittelee yhteisiä arvoja ja moraalisia periaatteita, jotka ohjaavat käyttäytymistämme yhteiskunnassa. Etiikka ei perustu lakeihin, vaan yleisesti hyväksyttyihin normeihin siitä, mikä on "oikein vs. väärin". Kuitenkin eettiset näkökohdat voivat vaikuttaa yritysten hallintokäytäntöihin ja hallituksen säädöksiin, jotka luovat enemmän kannustimia noudattamiseen.

**Datan etiikka** on [uusi etiikan haara](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1), joka "tutkii ja arvioi moraalisia ongelmia, jotka liittyvät _dataan, algoritmeihin ja vastaaviin käytäntöihin_". Tässä **"data"** keskittyy toimiin, jotka liittyvät datan luomiseen, tallentamiseen, kuratointiin, käsittelyyn, levittämiseen, jakamiseen ja käyttöön, **"algoritmit"** keskittyvät tekoälyyn, agenteihin, koneoppimiseen ja robotteihin, ja **"käytännöt"** keskittyvät aiheisiin, kuten vastuulliseen innovointiin, ohjelmointiin, hakkerointiin ja eettisiin koodeihin.

**Soveltava etiikka** on [moraalisten näkökohtien käytännön soveltamista](https://en.wikipedia.org/wiki/Applied_ethics). Se on prosessi, jossa aktiivisesti tutkitaan eettisiä kysymyksiä _todellisen maailman toimien, tuotteiden ja prosessien_ yhteydessä ja toteutetaan korjaavia toimenpiteitä, jotta nämä pysyvät määriteltyjen eettisten arvojen mukaisina.

**Eettinen kulttuuri** tarkoittaa [_soveltavan etiikan operationalisointia_](https://hbr.org/2019/05/how-to-design-an-ethical-organization) varmistaakseen, että eettiset periaatteemme ja käytäntömme otetaan käyttöön johdonmukaisesti ja skaalautuvasti koko organisaatiossa. Onnistuneet eettiset kulttuurit määrittelevät organisaation laajuiset eettiset periaatteet, tarjoavat merkityksellisiä kannustimia noudattamiseen ja vahvistavat eettisiä normeja rohkaisemalla ja vahvistamalla toivottuja käyttäytymismalleja organisaation kaikilla tasoilla.

## Etiikan käsitteet

Tässä osiossa käsittelemme käsitteitä, kuten **yhteiset arvot** (periaatteet) ja **eettiset haasteet** (ongelmat) datan etiikassa - ja tutkimme **tapaustutkimuksia**, jotka auttavat ymmärtämään näitä käsitteitä todellisissa yhteyksissä.

### 1. Etiikan periaatteet

Jokainen datan etiikkastrategia alkaa määrittelemällä _eettiset periaatteet_ - "yhteiset arvot", jotka kuvaavat hyväksyttäviä käyttäytymismalleja ja ohjaavat sääntöjenmukaisia toimia data- ja tekoälyprojekteissamme. Voit määritellä nämä yksilö- tai tiimitasolla. Useimmat suuret organisaatiot kuitenkin määrittelevät nämä _eettisen tekoälyn_ missiolausekkeessa tai viitekehyksessä, joka on määritelty yritystasolla ja jota sovelletaan johdonmukaisesti kaikissa tiimeissä.

**Esimerkki:** Microsoftin [Vastuullisen tekoälyn](https://www.microsoft.com/en-us/ai/responsible-ai) missiolauseke kuuluu: _"Olemme sitoutuneet tekoälyn kehittämiseen eettisten periaatteiden pohjalta, jotka asettavat ihmiset etusijalle"_ - ja se tunnistaa kuusi eettistä periaatetta alla olevassa viitekehyksessä:

![Vastuullinen tekoäly Microsoftilla](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Tutkitaan lyhyesti näitä periaatteita. _Läpinäkyvyys_ ja _vastuullisuus_ ovat perustavanlaatuisia arvoja, joiden päälle muut periaatteet rakentuvat - aloitetaan siis niistä:

* [**Vastuullisuus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) tekee käytännön toteuttajista _vastuullisia_ data- ja tekoälytoiminnastaan sekä näiden eettisten periaatteiden noudattamisesta.
* [**Läpinäkyvyys**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) varmistaa, että data- ja tekoälytoimet ovat _ymmärrettäviä_ käyttäjille, selittäen päätösten taustalla olevat syyt ja perusteet.
* [**Reiluus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) keskittyy varmistamaan, että tekoäly kohtelee _kaikkia ihmisiä_ oikeudenmukaisesti, puuttuen mahdollisiin järjestelmällisiin tai piileviin sosio-teknisiin vinoumiin datassa ja järjestelmissä.
* [**Luotettavuus ja turvallisuus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) varmistavat, että tekoäly toimii _johdonmukaisesti_ määriteltyjen arvojen mukaisesti, minimoiden mahdolliset haitat tai tahattomat seuraukset.
* [**Yksityisyys ja turvallisuus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) liittyvät datan alkuperän ymmärtämiseen ja käyttäjille tarjottaviin _tietosuoja- ja turvallisuustoimiin_.
* [**Osallistavuus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) tarkoittaa tekoälyratkaisujen suunnittelua tarkoituksella, mukauttaen niitä vastaamaan _laajaa valikoimaa inhimillisiä tarpeita_ ja kykyjä.

> 🚨 Mieti, millainen datan etiikan missiolauseesi voisi olla. Tutki muiden organisaatioiden eettisiä tekoälyviitekehyksiä - tässä esimerkkejä [IBM:ltä](https://www.ibm.com/cloud/learn/ai-ethics), [Googlelta](https://ai.google/principles) ja [Facebookilta](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Mitä yhteisiä arvoja niillä on? Miten nämä periaatteet liittyvät tekoälytuotteeseen tai toimialaan, jolla ne toimivat?

### 2. Etiikan haasteet

Kun eettiset periaatteet on määritelty, seuraava askel on arvioida data- ja tekoälytoimiamme nähdäksemme, ovatko ne linjassa näiden yhteisten arvojen kanssa. Mieti toimiasi kahdessa kategoriassa: _datan kerääminen_ ja _algoritmien suunnittelu_.

Datan keräämisessä toimet liittyvät todennäköisesti **henkilökohtaisiin tietoihin** tai henkilön tunnistaviin tietoihin (PII), jotka koskevat tunnistettavissa olevia eläviä yksilöitä. Tämä sisältää [monenlaisia ei-henkilökohtaisia tietoja](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en), jotka _yhdessä_ voivat tunnistaa yksilön. Eettiset haasteet voivat liittyä _tietosuojaan_, _datan omistajuuteen_ ja aiheisiin, kuten _tietoiseen suostumukseen_ ja _henkisiin omaisuusoikeuksiin_.

Algoritmien suunnittelussa toimet liittyvät **datan keräämiseen ja kuratointiin**, ja niiden käyttämiseen **datamallien** kouluttamiseen ja käyttöönottoon, jotka ennustavat tuloksia tai automatisoivat päätöksiä todellisissa konteksteissa. Eettisiä haasteita voivat olla _datan vinoumat_, _datan laatuongelmat_, _epäreiluus_ ja _vääristely_ algoritmeissa - mukaan lukien joitakin järjestelmällisiä ongelmia.

Molemmissa tapauksissa eettiset haasteet korostavat alueita, joissa toimintamme saattaa olla ristiriidassa yhteisten arvojemme kanssa. Näiden huolenaiheiden havaitsemiseksi, lieventämiseksi, minimoimiseksi tai poistamiseksi meidän on esitettävä moraalisia "kyllä/ei"-kysymyksiä toimistamme ja toteutettava tarvittavat korjaavat toimenpiteet. Katsotaanpa joitakin eettisiä haasteita ja niihin liittyviä moraalisia kysymyksiä:

#### 2.1 Datan omistajuus

Datan kerääminen sisältää usein henkilökohtaisia tietoja, jotka voivat tunnistaa datan kohteet. [Datan omistajuus](https://permission.io/blog/data-ownership) koskee _kontrollia_ ja [_käyttäjän oikeuksia_](https://permission.io/blog/data-ownership), jotka liittyvät datan luomiseen, käsittelyyn ja levittämiseen.

Moraaliset kysymykset, joita meidän on esitettävä:
 * Kuka omistaa datan? (käyttäjä vai organisaatio)
 * Mitä oikeuksia datan kohteilla on? (esim. pääsy, poistaminen, siirrettävyys)
 * Mitä oikeuksia organisaatioilla on? (esim. haitallisten käyttäjäarvioiden oikaiseminen)

#### 2.2 Tietoinen suostumus

[Tietoinen suostumus](https://legaldictionary.net/informed-consent/) tarkoittaa käyttäjän suostumusta toimintaan (kuten datan keräämiseen) _täydellä ymmärryksellä_ asiaankuuluvista faktoista, mukaan lukien tarkoitus, mahdolliset riskit ja vaihtoehdot.

Kysymyksiä, joita on tutkittava:
 * Antoiko käyttäjä (datan kohde) luvan datan keräämiseen ja käyttöön?
 * Ymmärsikö käyttäjä, mihin tarkoitukseen data kerättiin?
 * Ymmärsikö käyttäjä osallistumisensa mahdolliset riskit?

#### 2.3 Henkinen omaisuus

[Henkinen omaisuus](https://en.wikipedia.org/wiki/Intellectual_property) viittaa aineettomiin luomuksiin, jotka ovat ihmisen aloitteellisuuden tulosta ja joilla voi olla _taloudellista arvoa_ yksilöille tai yrityksille.

Kysymyksiä, joita on tutkittava:
 * Sisältääkö kerätty data taloudellista arvoa käyttäjälle tai yritykselle?
 * Onko **käyttäjällä** henkistä omaisuutta tässä?
 * Onko **organisaatiolla** henkistä omaisuutta tässä?
 * Jos nämä oikeudet ovat olemassa, miten suojelemme niitä?

#### 2.4 Tietosuoja

[Tietosuoja](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) tai informaation yksityisyys viittaa käyttäjän yksityisyyden säilyttämiseen ja käyttäjän identiteetin suojaamiseen henkilön tunnistavien tietojen osalta.

Kysymyksiä, joita on tutkittava:
 * Onko käyttäjien (henkilökohtainen) data suojattu hakkereilta ja tietovuodoilta?
 * Onko käyttäjien data saatavilla vain valtuutetuille käyttäjille ja konteksteille?
 * Säilytetäänkö käyttäjien anonymiteetti, kun dataa jaetaan tai levitetään?
 * Voidaanko käyttäjä tunnistaa anonymisoiduista datasetistä?

#### 2.5 Oikeus tulla unohdetuksi

[Oikeus tulla unohdetuksi](https://en.wikipedia.org/wiki/Right_to_be_forgotten) tai [oikeus tietojen poistamiseen](https://www.gdpreu.org/right-to-be-forgotten/) tarjoaa käyttäjille lisäsuojaa henkilökohtaisille tiedoille. Se antaa käyttäjille oikeuden pyytää henkilökohtaisten tietojen poistamista Internet-hauista ja muista sijainneista _tietyissä olosuhteissa_, mahdollistaen uuden alun ilman, että menneitä toimia pidetään heitä vastaan.

Kysymyksiä, joita on tutkittava:
 * Salliko järjestelmä datan kohteiden pyytää tietojen poistamista?
 * Pitäisikö käyttäjän suostumuksen peruuttamisen laukaista automaattinen tietojen poisto?
 * Kerättiinkö data ilman suostumusta tai laittomin keinoin?
 * Olemmeko tietosuojalainsäädännön mukaisia?

#### 2.6 Datasetin vinouma

Datasetin tai [keräysvinouman](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) ongelma liittyy _epäedustavan_ datan alijoukon valintaan algoritmien kehittämiseen, mikä voi johtaa epäoikeudenmukaisiin tuloksiin eri ryhmille. Vinoumat voivat olla esimerkiksi valinta- tai otantavinoumia, vapaaehtoisuusvinoumia tai instrumenttivinoumia.

Kysymyksiä, joita on tutkittava:
 * Rekrytoimmeko edustavan joukon datan kohteita?
 * Testasimmeko kerättyä tai kuratoitua datasettiä eri vinoumien osalta?
 * Voimmeko lieventää tai poistaa havaittuja vinoumia?

#### 2.7 Datan laatu

[Datan laatu](https://lakefs.io/data-quality-testing/) tarkastelee kuratoidun datasetin pätevyy
[Algoritmien oikeudenmukaisuus](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) tarkastelee, syrjiikö algoritmin suunnittelu systemaattisesti tiettyjä tietoryhmien alaryhmiä, mikä voi johtaa [mahdollisiin haittoihin](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) _resurssien jakamisessa_ (kun resursseja evätään tai pidätetään kyseiseltä ryhmältä) ja _palvelun laadussa_ (kun tekoäly ei ole yhtä tarkka joillekin alaryhmille kuin toisille).

Tässä pohdittavia kysymyksiä:
 * Arvioimmeko mallin tarkkuutta eri alaryhmien ja olosuhteiden osalta?
 * Tarkastelimmeko järjestelmää mahdollisten haittojen (esim. stereotypioiden) varalta?
 * Voimmeko muokata dataa tai kouluttaa malleja uudelleen haittojen lieventämiseksi?

Tutustu resursseihin, kuten [tekoälyn oikeudenmukaisuuden tarkistuslistoihin](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA), saadaksesi lisätietoa.

#### 2.9 Vääristely

[Datavääristely](https://www.sciencedirect.com/topics/computer-science/misrepresentation) tarkoittaa sitä, että kysytään, viestimmekö rehellisesti raportoituja tietoja harhaanjohtavalla tavalla tukemaan haluttua narratiivia.

Tässä pohdittavia kysymyksiä:
 * Raportoimmeko puutteellisia tai epätarkkoja tietoja?
 * Visualisoimmeko dataa tavalla, joka johtaa harhaanjohtaviin johtopäätöksiin?
 * Käytämmekö valikoivia tilastollisia menetelmiä manipuloidaksemme tuloksia?
 * Onko olemassa vaihtoehtoisia selityksiä, jotka voivat tarjota erilaisen johtopäätöksen?

#### 2.10 Vapaa valinta
[Vapaan valinnan illuusio](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) syntyy, kun järjestelmän "valinta-arkkitehtuurit" käyttävät päätöksentekoalgoritmeja ohjaamaan ihmisiä kohti haluttua lopputulosta samalla, kun heille annetaan vaikutelma vaihtoehdoista ja hallinnasta. Nämä [pimeät mallit](https://www.darkpatterns.org/) voivat aiheuttaa sosiaalisia ja taloudellisia haittoja käyttäjille. Koska käyttäjien päätökset vaikuttavat käyttäytymisprofiileihin, nämä toimet voivat mahdollisesti ohjata tulevia valintoja ja laajentaa haittojen vaikutusta.

Tässä pohdittavia kysymyksiä:
 * Ymmärsikö käyttäjä valinnan tekemisen seuraukset?
 * Oliko käyttäjä tietoinen (vaihtoehtoisista) valinnoista ja niiden eduista ja haitoista?
 * Voiko käyttäjä peruuttaa automatisoidun tai vaikutetun valinnan myöhemmin?

### 3. Tapaustutkimukset

Jotta voimme asettaa nämä eettiset haasteet todellisiin konteksteihin, on hyödyllistä tarkastella tapaustutkimuksia, jotka korostavat mahdollisia haittoja ja seurauksia yksilöille ja yhteiskunnalle, kun tällaisia eettisiä rikkomuksia ei huomioida.

Tässä muutamia esimerkkejä:

| Eettinen haaste | Tapaustutkimus  | 
|--- |--- |
| **Tietoinen suostumus** | 1972 - [Tuskegeen kuppatutkimus](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Afrikkalaisamerikkalaisille miehille luvattiin ilmaista terveydenhoitoa, _mutta heitä huijattiin_ jättämällä kertomatta heidän diagnoosistaan tai hoidon saatavuudesta. Monet kuolivat, ja heidän kumppaninsa tai lapsensa kärsivät; tutkimus kesti 40 vuotta. | 
| **Tietosuoja** |  2007 - [Netflixin datakilpailu](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) tarjosi tutkijoille _10 miljoonaa anonymisoitua elokuva-arvostelua 50 000 asiakkaalta_ suositusalgoritmien parantamiseksi. Tutkijat pystyivät kuitenkin yhdistämään anonymisoidut tiedot henkilökohtaisesti tunnistettaviin tietoihin _ulkopuolisista tietokannoista_ (esim. IMDb-kommenteista) - käytännössä "de-anonymisoiden" joitakin Netflixin tilaajia.|
| **Keräysbias**  | 2013 - Bostonin kaupunki [kehitti Street Bump -sovelluksen](https://www.boston.gov/transportation/street-bump), joka antoi kansalaisille mahdollisuuden raportoida kuoppia, tarjoten kaupungille parempaa tietoa teiden kunnosta. Kuitenkin [alempituloisilla ryhmillä oli vähemmän pääsyä autoihin ja puhelimiin](https://hbr.org/2013/04/the-hidden-biases-in-big-data), mikä teki heidän tieongelmistaan näkymättömiä sovelluksessa. Kehittäjät työskentelivät akateemikkojen kanssa _tasapuolisen pääsyn ja digitaalisten erojen_ kysymysten ratkaisemiseksi. |
| **Algoritmien oikeudenmukaisuus**  | 2018 - MIT:n [Gender Shades -tutkimus](http://gendershades.org/overview.html) arvioi sukupuolen luokitteluun tarkoitettujen tekoälytuotteiden tarkkuutta, paljastaen tarkkuuspuutteita naisten ja värillisten henkilöiden kohdalla. [Vuoden 2019 Apple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) näytti tarjoavan vähemmän luottoa naisille kuin miehille. Molemmat osoittivat algoritmisen biasin aiheuttamia sosioekonomisia haittoja.|
| **Datavääristely** | 2020 - Georgian [terveysosasto julkaisi COVID-19-kaavioita](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening), jotka näyttivät harhaanjohtavan kansalaisia tapausten kehityksestä käyttämällä epäjärjestelmällistä x-akselin järjestystä. Tämä havainnollistaa vääristelyä visualisointikikkojen avulla. |
| **Vapaan valinnan illuusio** | 2020 - Oppimissovellus [ABCmouse maksoi 10 miljoonaa dollaria ratkaistakseen FTC:n valituksen](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/), jossa vanhemmat joutuivat maksamaan tilauksista, joita he eivät voineet peruuttaa. Tämä havainnollistaa pimeitä malleja valinta-arkkitehtuureissa, joissa käyttäjiä ohjattiin mahdollisesti haitallisiin valintoihin. |
| **Tietosuoja ja käyttäjien oikeudet** | 2021 - Facebookin [tietovuoto](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) paljasti 530 miljoonan käyttäjän tiedot, mikä johti 5 miljardin dollarin sovintoon FTC:n kanssa. Se kuitenkin kieltäytyi ilmoittamasta käyttäjille tietovuodosta, mikä rikkoi käyttäjien oikeuksia tiedon läpinäkyvyyteen ja saatavuuteen. |

Haluatko tutkia lisää tapaustutkimuksia? Tutustu näihin resursseihin:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - eettisiä dilemmoja eri toimialoilta. 
* [Data Science Ethics -kurssi](https://www.coursera.org/learn/data-science-ethics#syllabus) - merkittäviä tapaustutkimuksia.
* [Missä asiat ovat menneet pieleen](https://deon.drivendata.org/examples/) - Deon-tarkistuslista esimerkkien kera.

> 🚨 Mieti näkemäsi tapaustutkimuksia - oletko kokenut tai joutunut vastaavan eettisen haasteen vaikutuksen alaiseksi elämässäsi? Voitko keksiä ainakin yhden muun tapaustutkimuksen, joka havainnollistaa jotakin tässä osiossa käsitellyistä eettisistä haasteista?

## Soveltava etiikka

Olemme puhuneet etiikan käsitteistä, haasteista ja tapaustutkimuksista todellisissa konteksteissa. Mutta miten pääsemme alkuun _soveltamaan_ eettisiä periaatteita ja käytäntöjä projekteissamme? Ja miten _toiminnallistamme_ nämä käytännöt paremman hallinnan saavuttamiseksi? Tutkitaan joitakin todellisia ratkaisuja:

### 1. Ammatilliset säännöstöt

Ammatilliset säännöstöt tarjoavat yhden vaihtoehdon organisaatioille "kannustaa" jäseniään tukemaan eettisiä periaatteitaan ja missiotaan. Säännöstöt ovat _moraalisia ohjenuoria_ ammatilliselle käyttäytymiselle, jotka auttavat työntekijöitä tai jäseniä tekemään päätöksiä, jotka ovat linjassa organisaation periaatteiden kanssa. Niiden tehokkuus riippuu kuitenkin jäsenten vapaaehtoisesta noudattamisesta; monet organisaatiot tarjoavat lisäpalkkioita ja -rangaistuksia kannustaakseen noudattamista.

Esimerkkejä:
 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) - eettinen säännöstö
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) - käyttäytymissäännöt (luotu 2013)
 * [ACM:n eettiset säännöt ja ammatillinen käytös](https://www.acm.org/code-of-ethics) (vuodesta 1993)

> 🚨 Kuulutko ammatilliseen insinööri- tai datatiedeorganisaatioon? Tutki heidän verkkosivustoaan nähdäksesi, määrittelevätkö he ammatillisen eettisen säännöstön. Mitä tämä kertoo heidän eettisistä periaatteistaan? Miten he "kannustavat" jäseniä noudattamaan säännöstöä?

### 2. Etiikan tarkistuslistat

Vaikka ammatilliset säännöstöt määrittelevät vaaditun _eettisen käyttäytymisen_ ammattilaisilta, niillä [on tunnettuja rajoituksia](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) täytäntöönpanossa, erityisesti suurissa projekteissa. Sen sijaan monet datatieteen asiantuntijat [suosittelevat tarkistuslistoja](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), jotka voivat **yhdistää periaatteet käytäntöihin** määrätietoisemmilla ja toimivammilla tavoilla.

Tarkistuslistat muuttavat kysymykset "kyllä/ei"-tehtäviksi, joita voidaan toiminnallistaa ja seurata osana tavanomaisia tuotteen julkaisutyönkulkuja.

Esimerkkejä:
 * [Deon](https://deon.drivendata.org/) - yleiskäyttöinen dataetiikan tarkistuslista, joka on luotu [teollisuuden suosituksista](https://deon.drivendata.org/#checklist-citations) ja sisältää komentorivityökalun helppoon integrointiin.
 * [Tietosuojan auditointitarkistuslista](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - tarjoaa yleisiä ohjeita tietojen käsittelykäytännöistä oikeudellisista ja sosiaalisista näkökulmista.
 * [Tekoälyn oikeudenmukaisuuden tarkistuslista](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - tekoälyasiantuntijoiden luoma tukemaan oikeudenmukaisuustarkistusten käyttöönottoa ja integrointia tekoälyn kehityssykleihin.
 * [22 kysymystä datan ja tekoälyn etiikasta](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - avoimempi kehys, joka on suunniteltu eettisten kysymysten alustavaan tutkimiseen suunnittelussa, toteutuksessa ja organisaatiokonteksteissa.

### 3. Etiikan sääntely

Etiikka tarkoittaa yhteisten arvojen määrittelyä ja oikean tekemistä _vapaaehtoisesti_. **Sääntöjen noudattaminen** tarkoittaa _lain noudattamista_, jos ja kun sellainen on määritelty. **Hallinto** kattaa laajemmin kaikki tavat, joilla organisaatiot toimivat eettisten periaatteiden täytäntöönpanemiseksi ja voimassa olevien lakien noudattamiseksi.

Nykyään hallinto ilmenee organisaatioissa kahdella tavalla. Ensinnäkin se tarkoittaa **eettisen tekoälyn** periaatteiden määrittelyä ja käytäntöjen luomista niiden käyttöönoton toiminnallistamiseksi kaikissa organisaation tekoälyprojekteissa. Toiseksi se tarkoittaa kaikkien hallituksen määräämien **tietosuojasäädösten** noudattamista niillä alueilla, joilla organisaatio toimii.

Esimerkkejä tietosuoja- ja yksityisyydensuojalainsäädännöstä:

 * `1974`, [Yhdysvaltain Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - säätelee _liittovaltion hallituksen_ henkilötietojen keräämistä, käyttöä ja luovuttamista.
 * `1996`, [Yhdysvaltain Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - suojaa henkilökohtaisia terveystietoja.
 * `1998`, [Yhdysvaltain Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - suojaa alle 13-vuotiaiden lasten tietosuojaa.
 * `2018`, [Yleinen tietosuoja-asetus (GDPR)](https://gdpr-info.eu/) - tarjoaa käyttäjien oikeuksia, tietosuojaa ja yksityisyyttä.
 * `2018`, [Kalifornian kuluttajansuojalaki (CCPA)](https://www.oag.ca.gov/privacy/ccpa) antaa kuluttajille enemmän _oikeuksia_ heidän (henkilökohtaisiin) tietoihinsa.
 * `2021`, Kiinan [henkilötietojen suojaa koskeva laki](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) hyväksyttiin juuri, ja se luo yhden maailman vahvimmista verkkotietosuojasäädöksistä.

> 🚨 Euroopan unionin määrittelemä GDPR (yleinen tietosuoja-asetus) on edelleen yksi vaikutusvaltaisimmista tietosuojasäädöksistä. Tiesitkö, että se määrittelee myös [8 käyttäjäoikeutta](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) digitaalisen yksityisyyden ja henkilötietojen suojaamiseksi? Opi, mitä nämä ovat ja miksi ne ovat tärkeitä.

### 4. Etiikkakulttuuri

Huomaa, että _sääntöjen noudattamisen_ (lain kirjaimen täyttämisen) ja [systeemisten ongelmien](https://www.coursera.org/learn/data-science-ethics/home/week/4) (kuten jäykkyyden, tiedon epäsymmetrian ja jakautuvan epäoikeudenmukaisuuden) ratkaisemisen välillä on edelleen aineeton kuilu, joka voi nopeuttaa tekoälyn aseistamista.

Jälkimmäinen vaatii [yhteistyöhön perustuvia lähestymistapoja etiikkakulttuurien määrittelyyn](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f), jotka rakentavat emotionaalisia yhteyksiä ja johdonmukaisia yhteisiä arvoja _organisaatioiden välillä_ alalla. Tämä edellyttää enemmän [muodollistettuja dataetiikkakulttuureja](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) organisaatioissa - mahdollistaen _kenelle tahansa_ [vetää Andon-narusta](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (nostaa esiin eettisiä huolenaiheita prosessin alkuvaiheessa) ja tehdä _eettisiä arviointeja_ (esim. rekrytoinnissa) tekoälyprojektien tiimien muodostamisen keskeisenä kriteerinä.

---
## [Luentojälkeinen kysely](https://ff-quizzes.netlify.app/en/ds/quiz/3) 🎯
## Kertaus ja
* [Vastuullisen tekoälyn periaatteet](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - maksuton oppimispolku Microsoft Learnista.  
* [Etiikka ja datatiede](https://resources.oreilly.com/examples/0636920203964) - O'Reillyn e-kirja (M. Loukides, H. Mason ym.)  
* [Datatieteen etiikka](https://www.coursera.org/learn/data-science-ethics#syllabus) - verkkokurssi Michiganin yliopistosta.  
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - tapaustutkimuksia Texasin yliopistosta.  

# Tehtävä  

[Kirjoita tapaustutkimus datan etiikasta](assignment.md)  

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmisen tekemää käännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.