<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8796f41f566a0a8ebb72863a83d558ed",
  "translation_date": "2025-08-26T21:25:18+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "fi"
}
-->
# Johdanto datan etiikkaan

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Datan etiikka - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

---

Me kaikki olemme datan kansalaisia, jotka elävät dataistuneessa maailmassa.

Markkinatrendit kertovat, että vuoteen 2022 mennessä yksi kolmesta suuresta organisaatiosta ostaa ja myy dataansa verkossa [markkinapaikkojen ja pörssien](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/) kautta. **Sovelluskehittäjinä** meidän on helpompaa ja edullisempaa integroida dataan perustuvia oivalluksia ja algoritmeihin perustuvaa automaatiota päivittäisiin käyttäjäkokemuksiin. Mutta kun tekoälystä tulee yhä yleisempää, meidän on myös ymmärrettävä mahdolliset haitat, joita syntyy tällaisten algoritmien [aseistamisesta](https://www.youtube.com/watch?v=TQHs8SA1qpk) suuressa mittakaavassa.

Trendit osoittavat myös, että vuoteen 2025 mennessä tuotamme ja kulutamme yli [180 zettatavua](https://www.statista.com/statistics/871513/worldwide-data-created/) dataa. **Data-analyytikkoina** tämä antaa meille ennennäkemättömän pääsyn henkilökohtaisiin tietoihin. Tämä tarkoittaa, että voimme rakentaa käyttäjien käyttäytymisprofiileja ja vaikuttaa päätöksentekoon tavoilla, jotka luovat [illuusion vapaasta valinnasta](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice), samalla kun saatamme ohjata käyttäjiä kohti meille suotuisia lopputuloksia. Tämä herättää myös laajempia kysymyksiä datan yksityisyydestä ja käyttäjien suojelusta.

Datan etiikka on nyt _välttämätön suojakaide_ data-analytiikassa ja -insinöörityössä, auttaen meitä minimoimaan mahdolliset haitat ja tahattomat seuraukset datalähtöisistä toimistamme. [Gartnerin tekoälyn hypekäyrä](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) tunnistaa digietiikan, vastuullisen tekoälyn ja tekoälyn hallinnan keskeisiksi trendeiksi, jotka ohjaavat suurempia megatrendejä, kuten tekoälyn _demokratisointia_ ja _teollistamista_.

![Gartnerin tekoälyn hypekäyrä - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

Tässä oppitunnissa tutkimme kiehtovaa datan etiikan aluetta - peruskäsitteistä ja haasteista tapaustutkimuksiin ja soveltaviin tekoälykonsepteihin, kuten hallintoon, jotka auttavat luomaan eettisen kulttuurin dataa ja tekoälyä käsittelevissä tiimeissä ja organisaatioissa.

## [Esiluentavisa](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/2) 🎯

## Perusmääritelmät

Aloitetaan ymmärtämällä peruskäsitteet.

Sana "etiikka" tulee [kreikan sanasta "ethikos"](https://en.wikipedia.org/wiki/Ethics) (ja sen juuresta "ethos"), joka tarkoittaa _luonnetta tai moraalista olemusta_.

**Etiikka** käsittelee yhteisiä arvoja ja moraalisia periaatteita, jotka ohjaavat käyttäytymistämme yhteiskunnassa. Etiikka ei perustu lakeihin, vaan yleisesti hyväksyttyihin normeihin siitä, mikä on "oikein vs. väärin". Kuitenkin eettiset näkökohdat voivat vaikuttaa yritysten hallintokäytäntöihin ja hallituksen säädöksiin, jotka luovat enemmän kannustimia noudattamiselle.

**Datan etiikka** on [uusi etiikan haara](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1), joka "tutkii ja arvioi moraalisia ongelmia, jotka liittyvät _dataan, algoritmeihin ja vastaaviin käytäntöihin_". Tässä **"data"** keskittyy toimiin, jotka liittyvät datan luomiseen, tallentamiseen, kuratointiin, käsittelyyn, levittämiseen, jakamiseen ja käyttöön, **"algoritmit"** keskittyvät tekoälyyn, agenteihin, koneoppimiseen ja robotteihin, ja **"käytännöt"** keskittyvät aiheisiin, kuten vastuulliseen innovointiin, ohjelmointiin, hakkerointiin ja eettisiin koodeihin.

**Soveltava etiikka** on [moraalisten näkökohtien käytännön soveltamista](https://en.wikipedia.org/wiki/Applied_ethics). Se on prosessi, jossa aktiivisesti tutkitaan eettisiä kysymyksiä _todellisen maailman toimien, tuotteiden ja prosessien_ yhteydessä ja toteutetaan korjaavia toimenpiteitä, jotta nämä pysyvät linjassa määriteltyjen eettisten arvojemme kanssa.

**Eettinen kulttuuri** tarkoittaa [_soveltavan etiikan operationalisointia_](https://hbr.org/2019/05/how-to-design-an-ethical-organization) varmistaakseen, että eettiset periaatteemme ja käytäntömme otetaan käyttöön johdonmukaisesti ja skaalautuvasti koko organisaatiossa. Onnistuneet eettiset kulttuurit määrittelevät organisaation laajuiset eettiset periaatteet, tarjoavat merkityksellisiä kannustimia noudattamiselle ja vahvistavat eettisiä normeja rohkaisemalla ja korostamalla toivottuja käyttäytymismalleja organisaation kaikilla tasoilla.

## Etiikan käsitteet

Tässä osiossa käsittelemme käsitteitä, kuten **yhteiset arvot** (periaatteet) ja **eettiset haasteet** (ongelmat) datan etiikassa - ja tutkimme **tapaustutkimuksia**, jotka auttavat ymmärtämään näitä käsitteitä todellisissa konteksteissa.

### 1. Etiikan periaatteet

Jokainen datan etiikkastrategia alkaa määrittelemällä _eettiset periaatteet_ - "yhteiset arvot", jotka kuvaavat hyväksyttäviä käyttäytymismalleja ja ohjaavat noudattavia toimia data- ja tekoälyprojekteissamme. Voit määritellä nämä yksilö- tai tiimitasolla. Useimmat suuret organisaatiot kuitenkin laativat nämä _eettisen tekoälyn_ missiolausekkeessa tai viitekehyksessä, joka määritellään yritystasolla ja jota sovelletaan johdonmukaisesti kaikissa tiimeissä.

**Esimerkki:** Microsoftin [Vastuullisen tekoälyn](https://www.microsoft.com/en-us/ai/responsible-ai) missiolauseke kuuluu: _"Olemme sitoutuneet edistämään tekoälyä eettisten periaatteiden pohjalta, jotka asettavat ihmiset etusijalle"_ - tunnistaen kuusi eettistä periaatetta alla olevassa viitekehyksessä:

![Vastuullinen tekoäly Microsoftilla](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Tutkitaan lyhyesti näitä periaatteita. _Läpinäkyvyys_ ja _vastuullisuus_ ovat perustavanlaatuisia arvoja, joiden päälle muut periaatteet rakentuvat - aloitetaan siis niistä:

* [**Vastuullisuus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) tekee käytännön toteuttajista _vastuullisia_ data- ja tekoälytoiminnoistaan sekä näiden eettisten periaatteiden noudattamisesta.
* [**Läpinäkyvyys**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) varmistaa, että data- ja tekoälytoimet ovat _ymmärrettäviä_ (tulkittavia) käyttäjille, selittäen päätösten taustalla olevat syyt ja tarkoitukset.
* [**Reiluus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) keskittyy varmistamaan, että tekoäly kohtelee _kaikkia ihmisiä_ oikeudenmukaisesti, käsitellen mahdollisia järjestelmällisiä tai piileviä sosio-teknisiä vinoumia datassa ja järjestelmissä.
* [**Luotettavuus ja turvallisuus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) varmistaa, että tekoäly toimii _johdonmukaisesti_ määriteltyjen arvojen mukaisesti, minimoiden mahdolliset haitat tai tahattomat seuraukset.
* [**Yksityisyys ja turvallisuus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) liittyy datan alkuperän ymmärtämiseen ja _datan yksityisyyden ja siihen liittyvien suojatoimien_ tarjoamiseen käyttäjille.
* [**Osallistavuus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) tarkoittaa tekoälyratkaisujen suunnittelua tarkoituksella, mukauttamalla ne vastaamaan _laajaa joukkoa ihmisten tarpeita_ ja kykyjä.

> 🚨 Mieti, mikä voisi olla sinun datan etiikan missiolausekkeesi. Tutki muiden organisaatioiden eettisiä tekoälyviitekehyksiä - tässä esimerkkejä [IBM:ltä](https://www.ibm.com/cloud/learn/ai-ethics), [Googlelta](https://ai.google/principles) ja [Facebookilta](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Mitä yhteisiä arvoja niillä on? Miten nämä periaatteet liittyvät tekoälytuotteeseen tai -alaan, jolla ne toimivat?

### 2. Etiikan haasteet

Kun eettiset periaatteet on määritelty, seuraava askel on arvioida data- ja tekoälytoimiamme nähdäksemme, ovatko ne linjassa näiden yhteisten arvojen kanssa. Mieti toimiasi kahdessa kategoriassa: _datan kerääminen_ ja _algoritmien suunnittelu_.

Datan keräämisessä toimet liittyvät todennäköisesti **henkilökohtaisiin tietoihin** tai henkilön tunnistettaviin tietoihin (PII), jotka koskevat tunnistettavissa olevia eläviä yksilöitä. Tämä sisältää [monenlaisia ei-henkilökohtaisia tietoja](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en), jotka _yhdessä_ voivat tunnistaa yksilön. Eettiset haasteet voivat liittyä _datan yksityisyyteen_, _datan omistajuuteen_ ja aiheisiin, kuten _tietoinen suostumus_ ja _käyttäjien immateriaalioikeudet_.

Algoritmien suunnittelussa toimet liittyvät **datan keräämiseen ja kuratointiin**, ja niiden käyttämiseen **datamallien** kouluttamiseen ja käyttöönottoon, jotka ennustavat tuloksia tai automatisoivat päätöksiä todellisissa konteksteissa. Eettisiä haasteita voi syntyä _datan vinoumista_, _datan laadun_ ongelmista, _epäreiluudesta_ ja _vääristymistä_ algoritmeissa - mukaan lukien joitakin järjestelmällisiä ongelmia.

Molemmissa tapauksissa eettiset haasteet korostavat alueita, joissa toimintamme saattaa olla ristiriidassa yhteisten arvojemme kanssa. Näiden huolenaiheiden havaitsemiseksi, lieventämiseksi, minimoimiseksi tai poistamiseksi meidän on esitettävä moraalisia "kyllä/ei"-kysymyksiä toimistamme ja toteutettava tarvittavat korjaavat toimenpiteet. Katsotaanpa joitakin eettisiä haasteita ja niihin liittyviä moraalisia kysymyksiä:

#### 2.1 Datan omistajuus

Datan kerääminen sisältää usein henkilökohtaisia tietoja, jotka voivat tunnistaa datan kohteet. [Datan omistajuus](https://permission.io/blog/data-ownership) koskee _kontrollia_ ja [_käyttäjien oikeuksia_](https://permission.io/blog/data-ownership) liittyen datan luomiseen, käsittelyyn ja levittämiseen.

Moraalisia kysymyksiä, joita meidän on esitettävä:
 * Kuka omistaa datan? (käyttäjä vai organisaatio)
 * Mitä oikeuksia datan kohteilla on? (esim. pääsy, poistaminen, siirrettävyys)
 * Mitä oikeuksia organisaatioilla on? (esim. korjata haitallisia käyttäjäarvioita)

#### 2.2 Tietoinen suostumus

[Tietoinen suostumus](https://legaldictionary.net/informed-consent/) määrittelee käyttäjien toiminnan (kuten datan keräämisen) hyväksymisen _täydellä ymmärryksellä_ asiaankuuluvista faktoista, mukaan lukien tarkoitus, mahdolliset riskit ja vaihtoehdot.

Kysymyksiä, joita on tutkittava:
 * Antoiko käyttäjä (datan kohde) luvan datan keräämiseen ja käyttöön?
 * Ymmärsikö käyttäjä, mihin tarkoitukseen data kerättiin?
 * Ymmärsikö käyttäjä osallistumisensa mahdolliset riskit?

#### 2.3 Immateriaalioikeudet

[Immateriaalioikeudet](https://en.wikipedia.org/wiki/Intellectual_property) viittaavat aineettomiin luomuksiin, jotka ovat ihmisen aloitteellisuuden tulosta ja joilla voi olla _taloudellista arvoa_ yksilöille tai yrityksille.

Kysymyksiä, joita on tutkittava:
 * Sisältääkö kerätty data taloudellista arvoa käyttäjälle tai yritykselle?
 * Onko **käyttäjällä** immateriaalioikeuksia tässä?
 * Onko **organisaatiolla** immateriaalioikeuksia tässä?
 * Jos nämä oikeudet ovat olemassa, miten suojelemme niitä?

#### 2.4 Datan yksityisyys

[Datan yksityisyys](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) tai tietosuoja viittaa käyttäjän yksityisyyden säilyttämiseen ja käyttäjän identiteetin suojaamiseen henkilön tunnistettavien tietojen osalta.

Kysymyksiä, joita on tutkittava:
 * Onko käyttäjien (henkilökohtainen) data suojattu hakkereilta ja vuodoilta?
 * Onko käyttäjien data vain valtuutettujen käyttäjien ja kontekstien saatavilla?
 * Säilytetäänkö käyttäjien anonymiteetti, kun dataa jaetaan tai levitetään?
 * Voidaanko käyttäjä tunnistaa uudelleen anonymisoiduista datasetistä?

#### 2.5 Oikeus tulla unohdetuksi

[Oikeus tulla unohdetuksi](https://en.wikipedia.org/wiki/Right_to_be_forgotten) tai [oikeus tietojen poistamiseen](https://www.gdpreu.org/right-to-be-forgotten/) tarjoaa käyttäjille lisäsuojaa henkilökohtaisille tiedoille. Se antaa käyttäjille oikeuden pyytää henkilökohtaisten tietojen poistamista Internet-hauista ja muista sijainneista _tietyissä olosuhteissa_ - mahdollistaen uuden alun verkossa ilman, että menneitä toimia pidetään heitä vastaan.

Kysymyksiä, joita on tutkittava:
 * Salliko järjestelmä datan kohteiden pyytää tietojen poistamista?
 * Pitäisikö käyttäjän suostumuksen peruuttamisen laukaista automaattinen poistaminen?
 * Kerättiinkö data ilman suostumusta tai laittomin keinoin?
 * Olemmeko noudattaneet hallituksen säädöksiä datan yksityisyydestä?

#### 2.6 Datasetin vinoumat

Datasetin tai [keräysvinouman](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) ongelma liittyy _epäedustavan_ datan alijoukon valintaan algoritmien kehittämiseen, mikä voi johtaa mahdolliseen epäoikeudenmukaisuuteen tuloksissa eri ryhmille. Vinoumat voivat olla esimerkiksi valinta- tai otantavinoumia, vapaaehtoisuusvinoumia ja instrumenttivinoumia.

Kysymyksiä, joita on tutkittava:
 * Rekrytoimmeko edustavan joukon datan kohteita?
 * Testasimmeko kerättyä tai kuratoitua datasettiä eri vinoumien varalta?
 * Voimmeko lieventää tai poistaa havaittuja vinoumia?

#### 2.7 Datan laatu


[Algorithminen oikeudenmukaisuus](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) tarkastelee, syrjiikö algoritmin suunnittelu systemaattisesti tiettyjä datan kohderyhmiä, mikä voi johtaa [mahdollisiin haittoihin](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) _resurssien jakamisessa_ (kun resursseja evätään tai pidätetään kyseiseltä ryhmältä) ja _palvelun laadussa_ (kun tekoäly ei ole yhtä tarkka joillekin alaryhmille kuin muille).

Kysymyksiä, joita tässä kannattaa pohtia:
 * Arvioimmeko mallin tarkkuutta eri alaryhmien ja olosuhteiden osalta?
 * Tutkimmeko järjestelmää mahdollisten haittojen (esim. stereotypioiden) osalta?
 * Voimmeko muokata dataa tai kouluttaa malleja uudelleen haittojen vähentämiseksi?

Tutustu resursseihin, kuten [AI Fairness -tarkistuslistoihin](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA), oppiaksesi lisää.

#### 2.9 Vääristely

[Datavääristely](https://www.sciencedirect.com/topics/computer-science/misrepresentation) tarkoittaa sitä, että kysytään, viestimmekö rehellisesti raportoidusta datasta saadut oivallukset harhaanjohtavalla tavalla tukemaan haluttua narratiivia.

Kysymyksiä, joita tässä kannattaa pohtia:
 * Raportoimmeko puutteellista tai epätarkkaa dataa?
 * Visualisoimmeko dataa tavalla, joka johtaa harhaanjohtaviin johtopäätöksiin?
 * Käytämmekö valikoivia tilastollisia tekniikoita manipuloidaksemme tuloksia?
 * Onko olemassa vaihtoehtoisia selityksiä, jotka voivat tarjota erilaisen johtopäätöksen?

#### 2.10 Vapaa valinta
[Vapaan valinnan illuusio](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) syntyy, kun järjestelmän "valinta-arkkitehtuurit" käyttävät päätöksentekoalgoritmeja ohjaamaan ihmisiä kohti haluttua lopputulosta samalla, kun heille näennäisesti annetaan vaihtoehtoja ja kontrollia. Nämä [pimeät kuviot](https://www.darkpatterns.org/) voivat aiheuttaa sosiaalisia ja taloudellisia haittoja käyttäjille. Koska käyttäjien päätökset vaikuttavat käyttäytymisprofiileihin, nämä toimet voivat mahdollisesti ohjata tulevia valintoja ja vahvistaa tai laajentaa haittojen vaikutusta.

Kysymyksiä, joita tässä kannattaa pohtia:
 * Ymmärsikö käyttäjä valinnan tekemisen seuraukset?
 * Oliko käyttäjä tietoinen (vaihtoehtoisista) valinnoista ja niiden eduista ja haitoista?
 * Voiko käyttäjä myöhemmin peruuttaa automatisoidun tai ohjatun valinnan?

### 3. Tapaustutkimukset

Eettisten haasteiden asettaminen todellisiin konteksteihin auttaa ymmärtämään mahdollisia haittoja ja seurauksia yksilöille ja yhteiskunnalle, kun eettisiä rikkomuksia ei huomioida.

Tässä muutamia esimerkkejä:

| Eettinen haaste | Tapaustutkimus | 
|--- |--- |
| **Tietoinen suostumus** | 1972 - [Tuskegeen kuppatutkimus](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Afrikkalaisamerikkalaisille miehille luvattiin ilmainen lääkärinhoito, _mutta heitä petettiin_ tutkijoiden toimesta, jotka eivät kertoneet diagnoosista tai hoidon saatavuudesta. Monet kuolivat, ja heidän kumppaninsa tai lapsensa kärsivät; tutkimus kesti 40 vuotta. | 
| **Dataprivaatisuus** | 2007 - [Netflixin datapalkinto](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) tarjosi tutkijoille _10 miljoonaa anonymisoitua elokuva-arvostelua 50 000 asiakkaalta_ parantaakseen suositusalgoritmeja. Tutkijat pystyivät kuitenkin yhdistämään anonymisoidun datan henkilökohtaisesti tunnistettavaan dataan _ulkoisista tietokannoista_ (esim. IMDb-kommentit), mikä käytännössä "de-anonymisoi" joitakin Netflixin tilaajia.|
| **Keräysbias**  | 2013 - Bostonin kaupunki [kehitti Street Bump -sovelluksen](https://www.boston.gov/transportation/street-bump), joka antoi kansalaisille mahdollisuuden raportoida kuoppia, tarjoten kaupungille parempaa tietoa teiden korjaamiseksi. Kuitenkin [alemman tulotason ryhmillä oli vähemmän pääsyä autoihin ja puhelimiin](https://hbr.org/2013/04/the-hidden-biases-in-big-data), mikä teki heidän tieongelmansa näkymättömiksi sovelluksessa. Kehittäjät tekivät yhteistyötä akateemikkojen kanssa _tasapuolisen pääsyn ja digitaalisten kuilujen_ ratkaisemiseksi oikeudenmukaisuuden nimissä. |
| **Algoritminen oikeudenmukaisuus**  | 2018 - MIT:n [Gender Shades -tutkimus](http://gendershades.org/overview.html) arvioi sukupuolen luokitteluun tarkoitettujen tekoälytuotteiden tarkkuutta, paljastaen puutteita naisten ja värillisten henkilöiden osalta. [2019 Apple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) näytti tarjoavan vähemmän luottoa naisille kuin miehille. Molemmat osoittivat algoritmisen biasin aiheuttamia sosioekonomisia haittoja.|
| **Datavääristely** | 2020 - Georgian [terveysosasto julkaisi COVID-19-kaavioita](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening), jotka näyttivät harhaanjohtavan kansalaisia vahvistettujen tapausten trendeistä käyttämällä ei-kronologista järjestystä x-akselilla. Tämä havainnollistaa vääristelyä visualisointikikkojen avulla. |
| **Vapaan valinnan illuusio** | 2020 - Oppimissovellus [ABCmouse maksoi 10 miljoonaa dollaria FTC:n valituksen sovittelusta](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/), jossa vanhemmat joutuivat maksamaan tilauksista, joita he eivät voineet peruuttaa. Tämä havainnollistaa pimeitä kuvioita valinta-arkkitehtuureissa, joissa käyttäjiä ohjattiin mahdollisesti haitallisiin valintoihin. |
| **Dataprivaatisuus ja käyttäjän oikeudet** | 2021 - Facebookin [datavuoto](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) paljasti 530 miljoonan käyttäjän tiedot, mikä johti 5 miljardin dollarin sovitteluun FTC:n kanssa. Se kuitenkin kieltäytyi ilmoittamasta käyttäjille vuodosta, mikä rikkoi käyttäjän oikeuksia datan läpinäkyvyyden ja saatavuuden osalta. |

Haluatko tutkia lisää tapaustutkimuksia? Tutustu näihin resursseihin:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - eettisiä dilemmoja eri toimialoilla. 
* [Data Science Ethics -kurssi](https://www.coursera.org/learn/data-science-ethics#syllabus) - merkittäviä tapaustutkimuksia. 
* [Missä asiat ovat menneet pieleen](https://deon.drivendata.org/examples/) - Deon-tarkistuslista esimerkkien kanssa.

> 🚨 Mieti tapaustutkimuksia, joita olet nähnyt – oletko kokenut tai ollut osallisena vastaavassa eettisessä haasteessa elämässäsi? Voitko keksiä ainakin yhden muun tapaustutkimuksen, joka havainnollistaa jotakin tässä osiossa käsitellyistä eettisistä haasteista?

## Soveltava etiikka

Olemme puhuneet etiikan käsitteistä, haasteista ja tapaustutkimuksista todellisissa konteksteissa. Mutta miten pääsemme alkuun eettisten periaatteiden ja käytäntöjen _soveltamisessa_ projekteissamme? Ja miten _operationalisoimme_ nämä käytännöt paremman hallinnan saavuttamiseksi? Tutkitaan joitakin käytännön ratkaisuja:

### 1. Ammattikoodit

Ammattikoodit tarjoavat yhden vaihtoehdon organisaatioille "kannustaa" jäseniä tukemaan eettisiä periaatteitaan ja missiotaan. Koodit ovat _moraalisia ohjeita_ ammatilliselle käyttäytymiselle, jotka auttavat työntekijöitä tai jäseniä tekemään päätöksiä, jotka ovat linjassa organisaation periaatteiden kanssa. Ne ovat vain niin hyviä kuin jäsenten vapaaehtoinen noudattaminen; monet organisaatiot tarjoavat kuitenkin lisäpalkintoja ja -rangaistuksia motivoidakseen jäseniä noudattamaan koodia.

Esimerkkejä:
 * [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Code of Ethics
 * [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Code of Conduct (luotu 2013)
 * [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (vuodesta 1993)

> 🚨 Kuulutko ammatilliseen insinööri- tai data science -organisaatioon? Tutki heidän sivustoaan nähdäksesi, määrittelevätkö he ammattikoodin. Mitä tämä kertoo heidän eettisistä periaatteistaan? Miten he "kannustavat" jäseniä noudattamaan koodia?

### 2. Etiikan tarkistuslistat

Vaikka ammattikoodit määrittelevät vaaditun _eettisen käyttäytymisen_ ammattilaisilta, niillä [on tunnettuja rajoituksia](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) täytäntöönpanossa, erityisesti suurissa projekteissa. Sen sijaan monet data science -asiantuntijat [suosittelevat tarkistuslistoja](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), jotka voivat **yhdistää periaatteet käytäntöihin** määrätietoisemmilla ja toiminnallisemmilla tavoilla.

Tarkistuslistat muuttavat kysymykset "kyllä/ei"-tehtäviksi, jotka voidaan operationalisoida, jolloin niitä voidaan seurata osana standardeja tuotteen julkaisutyönkulkuja.

Esimerkkejä:
 * [Deon](https://deon.drivendata.org/) - yleiskäyttöinen dataetiikan tarkistuslista, joka on luotu [teollisuuden suosituksista](https://deon.drivendata.org/#checklist-citations) ja sisältää komentorivityökalun helppoa integrointia varten.
 * [Privacy Audit Checklist](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - tarjoaa yleistä ohjeistusta tietojen käsittelykäytännöistä oikeudellisista ja sosiaalisista näkökulmista.
 * [AI Fairness Checklist](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - tekoälyasiantuntijoiden luoma tukemaan oikeudenmukaisuustarkistusten käyttöönottoa ja integrointia tekoälyn kehityssykleihin.
 * [22 kysymystä datan ja tekoälyn etiikasta](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - avoimempi kehys, joka on suunniteltu eettisten kysymysten alustavaan tutkimiseen suunnittelussa, toteutuksessa ja organisaatiokonteksteissa.

### 3. Etiikan sääntely

Etiikka tarkoittaa yhteisten arvojen määrittämistä ja oikean tekemistä _vapaaehtoisesti_. **Noudattaminen** tarkoittaa _lain seuraamista_ silloin ja siellä, missä se on määritelty. **Hallinto** kattaa laajemmin kaikki tavat, joilla organisaatiot toimivat eettisten periaatteiden täytäntöönpanemiseksi ja määriteltyjen lakien noudattamiseksi.

Nykyään hallinto ilmenee organisaatioissa kahdella tavalla. Ensinnäkin kyse on **eettisten tekoälyperiaatteiden** määrittämisestä ja käytäntöjen luomisesta niiden käyttöönoton operationalisoimiseksi kaikissa organisaation tekoälyyn liittyvissä projekteissa. Toiseksi kyse on kaikkien hallituksen määrittelemien **datansuojelusäädösten** noudattamisesta niillä alueilla, joilla organisaatio toimii.

Esimerkkejä datansuojelusta ja yksityisyyden sääntelystä:

 * `1974`, [Yhdysvaltain Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - säätelee _liittovaltion hallituksen_ henkilökohtaisen tiedon keräämistä, käyttöä ja julkistamista.
 * `1996`, [Yhdysvaltain Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - suojaa henkilökohtaisia terveystietoja.
 * `1998`, [Yhdysvaltain Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - suojaa alle 13-vuotiaiden lasten tietosuojaa.
 * `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - tarjoaa käyttäjän oikeuksia, datansuojaa ja yksityisyyttä.
 * `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) antaa kuluttajille enemmän _oikeuksia_ heidän (henkilökohtaisiin) tietoihinsa.
 * `2021`, Kiinan [Personal Information Protection Law](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) juuri hyväksytty, luoden yhden maailman vahvimmista verkkotietosuojelusäädöksistä.

> 🚨 Euroopan unionin määrittelemä GDPR (General Data Protection Regulation) on edelleen yksi vaikutusvaltaisimmista datan yksityisyyden sääntelyistä. Tiesitkö, että se myös määrittelee [8 käyttäjän oikeutta](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) suojaamaan kansalaisten digitaalista yksityisyyttä ja henkilökohtaisia tietoja? Opi, mitä nämä ovat ja miksi ne ovat tärkeitä.

### 4. Etiikan kulttuuri

Huomaa, että _lain noudattamisen_ (tehdä tarpeeksi täyttääkseen "lain kirjaimen") ja [systeemisten ongelmien](https://www.coursera.org/learn/data-science-ethics/home/week/4) (kuten jäykistyminen, tiedon epäsymmetria ja jakautumisen epäoikeudenmukaisuus) käsittelyn välillä on edelleen aineeton kuilu, joka voi nopeuttaa tekoälyn aseistamista.

Jälkimmäinen vaatii [yhteistyöhön perustuvia lähestymistapoja etiikan kulttuurien määrittämiseen](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f), jotka rakentavat emotionaalisia yhteyksiä ja johdonmukaisia yhteisiä arvoja _organisaatioiden välillä_ teollisuudessa. Tämä vaatii enemmän [formalisoituja dataetiikan kulttuureja](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) organisaatioissa – mahdollistaen _kenelle tahansa_ [vetää Andon-köyttä](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (nostaa eettisiä huolenaiheita prosessin alkuvaiheessa) ja tehden _eettisistä arvioinneista_ (esim. rekrytoinnissa) keskeisen kriteerin tiimien muodostamisessa tekoälyprojekteissa.

---
## [Luennon jälkeinen kysely](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/3) 🎯
## Kertaus ja itseopiskelu 

Kurssit ja kirjat auttavat ymmärtämään keskeisiä etiikan käsitteitä ja haasteita, kun taas tapaustutkimukset ja työkalut auttavat soveltamaan eettisiä käytäntöjä todellisissa konteksteissa. Tässä muutamia resursseja, joista voit aloittaa.

* [Machine Learning For
* [Vastuullisen tekoälyn periaatteet](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - ilmainen oppimispolku Microsoft Learnista.  
* [Etiikka ja datatiede](https://resources.oreilly.com/examples/0636920203964) - O'Reillyn e-kirja (M. Loukides, H. Mason ym.)  
* [Datatieteen etiikka](https://www.coursera.org/learn/data-science-ethics#syllabus) - verkkokurssi Michiganin yliopistosta.  
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - tapaustutkimuksia Texasin yliopistosta.  

# Tehtävä  

[Kirjoita tapaustutkimus datan etiikasta](assignment.md)  

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.