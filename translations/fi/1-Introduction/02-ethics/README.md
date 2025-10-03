<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58860ce9a4b8a564003d2752f7c72851",
  "translation_date": "2025-10-03T16:40:59+00:00",
  "source_file": "1-Introduction/02-ethics/README.md",
  "language_code": "fi"
}
-->
# Johdanto datan etiikkaan

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/02-Ethics.png)|
|:---:|
| Datan etiikka - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

---

Me kaikki olemme datan kansalaisia, jotka elävät datan kyllästämässä maailmassa.

Markkinatrendit kertovat, että vuoteen 2022 mennessä yksi kolmesta suuresta organisaatiosta ostaa ja myy dataansa verkossa [markkinapaikkojen ja pörssien](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/) kautta. **Sovelluskehittäjinä** meidän on entistä helpompaa ja edullisempaa integroida dataan perustuvia oivalluksia ja algoritmeihin perustuvaa automaatiota päivittäisiin käyttäjäkokemuksiin. Mutta kun tekoälystä tulee yhä yleisempää, meidän on myös ymmärrettävä mahdolliset haitat, joita aiheutuu tällaisten algoritmien [aseistamisesta](https://www.youtube.com/watch?v=TQHs8SA1qpk) suuressa mittakaavassa.

Trendit viittaavat siihen, että vuoteen 2025 mennessä tuotamme ja kulutamme yli [180 zettatavua](https://www.statista.com/statistics/871513/worldwide-data-created/) dataa. **Data-analyytikoille** tämä tietomäärän räjähdys tarjoaa ennennäkemättömän pääsyn henkilökohtaisiin ja käyttäytymiseen liittyviin tietoihin. Tämän avulla voidaan rakentaa yksityiskohtaisia käyttäjäprofiileja ja hienovaraisesti vaikuttaa päätöksentekoon—usein tavoilla, jotka luovat [illuusion vapaasta valinnasta](https://www.datasciencecentral.com/the-pareto-set-and-the-paradox-of-choice/). Vaikka tätä voidaan käyttää ohjaamaan käyttäjiä kohti toivottuja lopputuloksia, se herättää myös kriittisiä kysymyksiä datan yksityisyydestä, autonomiasta ja algoritmisen vaikutuksen eettisistä rajoista.

Datan etiikka toimii nyt _välttämättöminä suojakaiteina_ data-analytiikassa ja -insinöörityössä, auttaen minimoimaan mahdolliset haitat ja tahattomat seuraukset datan ohjaamista toimista. [Gartnerin Hype Cycle tekoälylle](https://www.gartner.com/smarterwithgartner/2-megatrends-dominate-the-gartner-hype-cycle-for-artificial-intelligence-2020/) tunnistaa digitaaliset eettiset trendit, vastuullisen tekoälyn ja tekoälyn hallinnan keskeisiksi tekijöiksi suuremmille megatrendeille, kuten tekoälyn _demokratisointi_ ja _teollistaminen_.

![Gartnerin Hype Cycle tekoälylle - 2020](https://images-cdn.newscred.com/Zz1mOWJhNzlkNDA2ZTMxMWViYjRiOGFiM2IyMjQ1YmMwZQ==)

Tässä oppitunnissa tutustumme kiehtovaan datan etiikan alueeseen—peruskäsitteistä ja haasteista tapaustutkimuksiin ja sovellettuihin tekoälykonsepteihin, kuten hallintaan—jotka auttavat luomaan eettisen kulttuurin tiimeissä ja organisaatioissa, jotka työskentelevät datan ja tekoälyn parissa.




## [Esiluennon kysely](https://ff-quizzes.netlify.app/en/ds/quiz/2) 🎯

## Perusmääritelmät

Aloitetaan ymmärtämällä peruskäsitteet.

Sana "etiikka" tulee [kreikan sanasta "ethikos"](https://en.wikipedia.org/wiki/Ethics) (ja sen juuresta "ethos"), joka tarkoittaa _luonnetta tai moraalista olemusta_. 

**Etiikka** käsittelee yhteisiä arvoja ja moraalisia periaatteita, jotka ohjaavat käyttäytymistämme yhteiskunnassa. Etiikka ei perustu lakeihin, vaan yleisesti hyväksyttyihin normeihin siitä, mikä on "oikein vs. väärin". Kuitenkin eettiset näkökohdat voivat vaikuttaa yritysten hallintokäytäntöihin ja hallituksen säädöksiin, jotka luovat enemmän kannustimia noudattamiselle.

**Datan etiikka** on [uusi etiikan haara](https://royalsocietypublishing.org/doi/full/10.1098/rsta.2016.0360#sec-1), joka "tutkii ja arvioi moraalisia ongelmia, jotka liittyvät _dataan, algoritmeihin ja vastaaviin käytäntöihin_". Tässä **"data"** keskittyy toimiin, jotka liittyvät datan tuottamiseen, tallentamiseen, kuratointiin, käsittelyyn, levittämiseen, jakamiseen ja käyttöön, **"algoritmit"** keskittyvät tekoälyyn, agentteihin, koneoppimiseen ja robotteihin, ja **"käytännöt"** keskittyvät aiheisiin, kuten vastuullinen innovaatio, ohjelmointi, hakkerointi ja eettiset koodit.

**Sovellettu etiikka** on [moraalisten näkökohtien käytännön soveltamista](https://en.wikipedia.org/wiki/Applied_ethics). Se on prosessi, jossa aktiivisesti tutkitaan eettisiä kysymyksiä _todellisten toimien, tuotteiden ja prosessien_ yhteydessä ja toteutetaan korjaavia toimenpiteitä, jotta nämä pysyvät määriteltyjen eettisten arvojen mukaisina.

**Eettinen kulttuuri** tarkoittaa [_sovellettujen eettisten periaatteiden operationalisointia_](https://hbr.org/2019/05/how-to-design-an-ethical-organization), jotta varmistetaan, että eettiset periaatteemme ja käytäntömme otetaan käyttöön johdonmukaisesti ja skaalautuvasti koko organisaatiossa. Menestyvät eettiset kulttuurit määrittelevät organisaation laajuiset eettiset periaatteet, tarjoavat merkityksellisiä kannustimia noudattamiselle ja vahvistavat eettisiä normeja rohkaisemalla ja vahvistamalla toivottuja käyttäytymismalleja organisaation kaikilla tasoilla.


## Etiikan käsitteet

Tässä osiossa käsittelemme käsitteitä, kuten **yhteiset arvot** (periaatteet) ja **eettiset haasteet** (ongelmat) datan etiikassa—sekä tutkimme **tapaustutkimuksia**, jotka auttavat ymmärtämään näitä käsitteitä todellisissa yhteyksissä.

### 1. Etiikan periaatteet

Jokainen datan etiikkastrategia alkaa määrittelemällä _eettiset periaatteet_—"yhteiset arvot", jotka kuvaavat hyväksyttäviä käyttäytymismalleja ja ohjaavat noudattavia toimia data- ja tekoälyprojekteissamme. Voit määritellä nämä yksilö- tai tiimitasolla. Kuitenkin useimmat suuret organisaatiot hahmottelevat nämä _eettisen tekoälyn_ missiolausekkeessa tai kehyksessä, joka määritellään yritystasolla ja pannaan johdonmukaisesti täytäntöön kaikissa tiimeissä.

**Esimerkki:** Microsoftin [Vastuullisen tekoälyn](https://www.microsoft.com/en-us/ai/responsible-ai) missiolauseke kuuluu: _"Olemme sitoutuneet tekoälyn kehittämiseen eettisten periaatteiden pohjalta, jotka asettavat ihmiset etusijalle"_—määritellen kuusi eettistä periaatetta alla olevassa kehyksessä:

![Vastuullinen tekoäly Microsoftilla](https://docs.microsoft.com/en-gb/azure/cognitive-services/personalizer/media/ethics-and-responsible-use/ai-values-future-computed.png)

Tutustutaan lyhyesti näihin periaatteisiin. _Läpinäkyvyys_ ja _vastuullisuus_ ovat perustavanlaatuisia arvoja, joiden päälle muut periaatteet rakentuvat—aloitetaan niistä:

* [**Vastuullisuus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) tekee käytännön harjoittajista _vastuullisia_ data- ja tekoälytoiminnastaan sekä näiden eettisten periaatteiden noudattamisesta.
* [**Läpinäkyvyys**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) varmistaa, että data- ja tekoälytoimet ovat _ymmärrettäviä_ käyttäjille, selittäen päätösten taustalla olevat syyt ja tarkoitukset.
* [**Reiluus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6) keskittyy varmistamaan, että tekoäly kohtelee _kaikkia ihmisiä_ reilusti, käsitellen mahdollisia järjestelmällisiä tai implisiittisiä sosio-teknisiä vinoumia datassa ja järjestelmissä.
* [**Luotettavuus ja turvallisuus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) varmistaa, että tekoäly toimii _johdonmukaisesti_ määriteltyjen arvojen mukaisesti, minimoiden mahdolliset haitat tai tahattomat seuraukset.
* [**Yksityisyys ja turvallisuus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) liittyy datan alkuperän ymmärtämiseen ja käyttäjille tarjottaviin _datan yksityisyyden ja siihen liittyvien suojausten_ varmistamiseen.
* [**Osallisuus**](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1:primaryr6) tarkoittaa tekoälyratkaisujen suunnittelua tarkoituksella, mukauttaen niitä vastaamaan _laajaa joukkoa ihmisten tarpeita_ ja kykyjä.

> 🚨 Mieti, mikä voisi olla datan etiikan missiolausekkeesi. Tutki muiden organisaatioiden eettisiä tekoälykehyksiä—tässä esimerkkejä [IBM:ltä](https://www.ibm.com/cloud/learn/ai-ethics), [Googlelta](https://ai.google/principles) ja [Facebookilta](https://ai.facebook.com/blog/facebooks-five-pillars-of-responsible-ai/). Mitä yhteisiä arvoja niillä on? Miten nämä periaatteet liittyvät tekoälytuotteeseen tai toimialaan, jolla ne toimivat?

### 2. Etiikan haasteet

Kun eettiset periaatteet on määritelty, seuraava askel on arvioida data- ja tekoälytoimiamme nähdäksemme, ovatko ne linjassa näiden yhteisten arvojen kanssa. Mieti toimiasi kahdessa kategoriassa: _datan kerääminen_ ja _algoritmien suunnittelu_. 

Datan keräämisessä toimet liittyvät todennäköisesti **henkilökohtaisiin tietoihin** tai henkilökohtaisesti tunnistettaviin tietoihin (PII), jotka koskevat tunnistettavia eläviä yksilöitä. Tämä sisältää [monenlaisia ei-henkilökohtaisia tietoja](https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_en), jotka _yhdessä_ tunnistavat yksilön. Eettiset haasteet voivat liittyä _datan yksityisyyteen_, _datan omistajuuteen_ ja aiheisiin, kuten _tietoinen suostumus_ ja _käyttäjien immateriaalioikeudet_.

Algoritmien suunnittelussa toimet liittyvät **datan keräämiseen ja kuratointiin**, ja niiden käyttämiseen **datamallien** kouluttamiseen ja käyttöönottoon, jotka ennustavat tuloksia tai automatisoivat päätöksiä todellisissa yhteyksissä. Eettiset haasteet voivat liittyä _datan vinoumiin_, _datan laatuun_, _epäreiluuteen_ ja _vääristelyyn_ algoritmeissa—mukaan lukien jotkut järjestelmälliset ongelmat.

Molemmissa tapauksissa eettiset haasteet korostavat alueita, joissa toimemme voivat olla ristiriidassa yhteisten arvojemme kanssa. Näiden huolenaiheiden havaitsemiseksi, lieventämiseksi, minimoimiseksi tai poistamiseksi meidän on esitettävä moraalisia "kyllä/ei"-kysymyksiä toimistamme ja toteutettava tarvittavat korjaavat toimenpiteet. Katsotaanpa joitakin eettisiä haasteita ja moraalisia kysymyksiä, joita ne herättävät:


#### 2.1 Datan omistajuus

Datan kerääminen liittyy usein henkilökohtaisiin tietoihin, jotka voivat tunnistaa datan kohteet. [Datan omistajuus](https://permission.io/blog/data-ownership) koskee _kontrollia_ ja [_käyttäjän oikeuksia_](https://permission.io/blog/data-ownership) datan luomiseen, käsittelyyn ja levittämiseen liittyen. 

Moraaliset kysymykset, joita meidän on esitettävä:
 * Kuka omistaa datan? (käyttäjä vai organisaatio)
 * Mitä oikeuksia datan kohteilla on? (esim. pääsy, poisto, siirrettävyys)
 * Mitä oikeuksia organisaatioilla on? (esim. haitallisten käyttäjäarvostelujen korjaaminen)

#### 2.2 Tietoinen suostumus

[Tietoinen suostumus](https://legaldictionary.net/informed-consent/) määrittelee käyttäjien suostumuksen toimintaan (kuten datan keräämiseen) _täydellä ymmärryksellä_ asiaankuuluvista faktoista, mukaan lukien tarkoitus, mahdolliset riskit ja vaihtoehdot. 

Kysymyksiä, joita tässä kannattaa pohtia:
 * Antoiko käyttäjä (datan kohde) luvan datan keräämiseen ja käyttöön?
 * Ymmärsikö käyttäjä datan keräämisen tarkoituksen?
 * Ymmärsikö käyttäjä osallistumisensa mahdolliset riskit?

#### 2.3 Immateriaalioikeudet

[Immateriaalioikeudet](https://en.wikipedia.org/wiki/Intellectual_property) viittaavat aineettomiin luomuksiin, jotka syntyvät ihmisen aloitteesta ja joilla voi _olla taloudellista arvoa_ yksilöille tai yrityksille. 

Kysymyksiä, joita tässä kannattaa pohtia:
 * Sisältääkö kerätty data taloudellista arvoa käyttäjälle tai yritykselle?
 * Onko **käyttäjällä** immateriaalioikeuksia tässä?
 * Onko **organisaatiolla** immateriaalioikeuksia tässä?
 * Jos nämä oikeudet ovat olemassa, miten suojelemme niitä?

#### 2.4 Datan yksityisyys

[Datan yksityisyys](https://www.northeastern.edu/graduate/blog/what-is-data-privacy/) tai informaation yksityisyys viittaa käyttäjän yksityisyyden säilyttämiseen ja käyttäjän identiteetin suojaamiseen henkilökohtaisesti tunnistettavien tietojen osalta. 

Kysymyksiä, joita tässä kannattaa pohtia:
 * Onko käyttäjien (henkilökohtainen) data suojattu hakkereilta ja vuodoilta?
 * Onko käyttäjien data saatavilla vain valtuutetuille käyttäjille ja konteksteille?
 * Säilytetäänkö käyttäjien anonymiteetti, kun dataa jaetaan tai levitetään?
 * Voidaanko käyttäjä tunnistaa anonymisoiduista datakokonaisuuksista?

#### 2.5 Oikeus tulla unohdetuksi

[Oikeus tulla unohdetuksi](https://en.wikipedia.org/wiki/Right_to_be_forgotten) tai [oikeus poistamiseen](https://www.gdpreu.org/right-to-be-forgotten/) tarjoaa käyttäjille lisäsuojaa henkilökohtaisille tiedoille. Erityisesti se antaa käyttäjille oikeuden pyytää henkilökohtaisten tietojen poistamista Internet-hauista ja muista sijainneista, _tietyissä olosuhteissa_—mahdollistaen uuden alun verkossa ilman, että menneitä toimia pidetään heitä vastaan.

Kysymyksiä, joita tässä kannattaa pohtia:
 * Salliko järjestelmä datan kohteiden pyytää tietojen poistamista?
 * Pitäisikö käyttäjän suostumuksen peruuttamisen laukaista automaattinen poisto?
 * Kerättiinkö data ilman suostumusta tai laittomin keinoin?
 * Olemmeko noudattaneet hallituksen säädöksiä datan yksityisyydestä?

#### 2.6 Datakokonaisuuden vinoumat

Datakokonaisuuden tai [keräysvinouman](http://researcharticles.com/index.php/bias-in-data-collection-in-research/) osalta kyse on _epäedustavan_ datan alijoukon valinnasta algoritmien kehittämiseen, mikä voi aiheuttaa mahdollista epäreiluutta tuloksissa eri ryhmille. Vinoumat voivat olla esimerkiksi valinta- tai otantavinoumia, vapaaehtoisuusvinoumia ja instrumenttivinoumia. 

Kysymyksiä, joita tässä kannattaa pohtia:
 * Rekrytoimmeko edustavan joukon dat
* Taltioidaanko tiedot _tarkasti_ todellisuutta heijastaen?

#### 2.8 Algoritmien oikeudenmukaisuus

[Algoritmien oikeudenmukaisuus](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) tarkastelee, syrjiikö algoritmin suunnittelu systemaattisesti tiettyjä datan kohderyhmiä, mikä voi johtaa [mahdollisiin haittoihin](https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml) _resurssien jakamisessa_ (kun resursseja evätään tai pidätetään kyseiseltä ryhmältä) ja _palvelun laadussa_ (kun tekoäly ei ole yhtä tarkka joillekin alaryhmille kuin toisille).

Kysymyksiä, joita tässä kannattaa pohtia:
* Arvioimmeko mallin tarkkuutta eri alaryhmille ja olosuhteille?
* Tutkimmeko järjestelmää mahdollisten haittojen (esim. stereotypioiden) varalta?
* Voimmeko muokata dataa tai kouluttaa malleja uudelleen haittojen vähentämiseksi?

Tutustu resursseihin, kuten [AI Fairness -tarkistuslistoihin](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4t6dA), saadaksesi lisätietoa.

#### 2.9 Vääristely

[Datavääristely](https://www.sciencedirect.com/topics/computer-science/misrepresentation) tarkoittaa sitä, että kysytään, raportoimmeko rehellisesti kerättyjä tietoja harhaanjohtavasti tukemaan haluttua narratiivia.

Kysymyksiä, joita tässä kannattaa pohtia:
* Raportoimmeko puutteellisia tai epätarkkoja tietoja?
* Visualisoimmeko dataa tavalla, joka johtaa harhaanjohtaviin johtopäätöksiin?
* Käytämmekö valikoivia tilastollisia menetelmiä manipuloidaksemme tuloksia?
* Onko olemassa vaihtoehtoisia selityksiä, jotka voivat tarjota erilaisen johtopäätöksen?

#### 2.10 Vapaa valinta
[Vapaan valinnan illuusio](https://www.datasciencecentral.com/profiles/blogs/the-illusion-of-choice) syntyy, kun järjestelmän "valinta-arkkitehtuurit" käyttävät päätöksentekoalgoritmeja ohjaamaan ihmisiä kohti haluttua lopputulosta samalla kun heille annetaan näennäisesti vaihtoehtoja ja kontrollia. Nämä [dark patterns](https://www.darkpatterns.org/) voivat aiheuttaa sosiaalisia ja taloudellisia haittoja käyttäjille. Koska käyttäjien päätökset vaikuttavat käyttäytymisprofiileihin, nämä toimet voivat mahdollisesti ohjata tulevia valintoja ja vahvistaa tai laajentaa näiden haittojen vaikutuksia.

Kysymyksiä, joita tässä kannattaa pohtia:
* Ymmärsikö käyttäjä valinnan tekemisen seuraukset?
* Oliko käyttäjä tietoinen (vaihtoehtoisista) valinnoista ja niiden eduista ja haitoista?
* Voiko käyttäjä myöhemmin peruuttaa automatisoidun tai ohjatun valinnan?

### 3. Tapaustutkimukset

Eettisten haasteiden asettaminen todellisiin konteksteihin auttaa ymmärtämään mahdollisia haittoja ja seurauksia yksilöille ja yhteiskunnalle, kun eettisiä rikkomuksia ei huomioida.

Tässä muutamia esimerkkejä:

| Eettinen haaste | Tapaustutkimus | 
|--- |--- |
| **Tietoinen suostumus** | 1972 - [Tuskegeen kuppatutkimus](https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study) - Afrikkalaisamerikkalaisille miehille, jotka osallistuivat tutkimukseen, luvattiin ilmainen lääkärinhoito, _mutta heitä petettiin_ tutkijoiden toimesta, jotka eivät kertoneet heille diagnoosista tai hoidon saatavuudesta. Monet kuolivat, ja heidän kumppaninsa tai lapsensa kärsivät; tutkimus kesti 40 vuotta. | 
| **Tietosuoja** | 2007 - [Netflixin datakilpailu](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) tarjosi tutkijoille _10 miljoonaa anonymisoitua elokuva-arvostelua 50 000 asiakkaalta_ suositusalgoritmien parantamiseksi. Tutkijat pystyivät kuitenkin yhdistämään anonymisoidut tiedot henkilökohtaisesti tunnistettaviin tietoihin _ulkopuolisista tietokannoista_ (esim. IMDb-kommentit), käytännössä "de-anonymisoiden" joitakin Netflixin tilaajia.|
| **Keräysbias** | 2013 - Bostonin kaupunki [kehitti Street Bump -sovelluksen](https://www.boston.gov/transportation/street-bump), joka antoi kansalaisille mahdollisuuden raportoida kuoppia, tarjoten kaupungille parempaa tietoa teiden ongelmista. Kuitenkin [alhaisemman tulotason ryhmillä oli vähemmän pääsyä autoihin ja puhelimiin](https://hbr.org/2013/04/the-hidden-biases-in-big-data), mikä teki heidän tieongelmansa näkymättömiksi sovelluksessa. Kehittäjät tekivät yhteistyötä akateemikkojen kanssa _tasapuolisen pääsyn ja digitaalisten erojen_ ratkaisemiseksi oikeudenmukaisuuden nimissä. |
| **Algoritmien oikeudenmukaisuus** | 2018 - MIT:n [Gender Shades -tutkimus](http://gendershades.org/overview.html) arvioi sukupuolen luokitteluun tarkoitettujen tekoälytuotteiden tarkkuutta, paljastaen tarkkuuspuutteita naisille ja värillisille henkilöille. [Vuoden 2019 Apple Card](https://www.wired.com/story/the-apple-card-didnt-see-genderand-thats-the-problem/) näytti tarjoavan vähemmän luottoa naisille kuin miehille. Molemmat osoittivat algoritmisen biasin aiheuttamia sosioekonomisia haittoja.|
| **Datavääristely** | 2020 - Georgian terveysosasto [julkaisi COVID-19-kaavioita](https://www.vox.com/covid-19-coronavirus-us-response-trump/2020/5/18/21262265/georgia-covid-19-cases-declining-reopening), jotka näyttivät harhaanjohtavan kansalaisia vahvistettujen tapausten trendeistä käyttämällä ei-kronologista järjestystä x-akselilla. Tämä havainnollistaa vääristelyä visualisointikikkojen avulla. |
| **Vapaan valinnan illuusio** | 2020 - Oppimissovellus [ABCmouse maksoi 10 miljoonaa dollaria FTC:n valituksen sovittelusta](https://www.washingtonpost.com/business/2020/09/04/abcmouse-10-million-ftc-settlement/), jossa vanhemmat joutuivat maksamaan tilauksista, joita he eivät voineet peruuttaa. Tämä havainnollistaa valinta-arkkitehtuurien dark patterns -ilmiötä, jossa käyttäjiä ohjattiin mahdollisesti haitallisiin valintoihin. |
| **Tietosuoja ja käyttäjän oikeudet** | 2021 - Facebookin [tietovuoto](https://www.npr.org/2021/04/09/986005820/after-data-breach-exposes-530-million-facebook-says-it-will-not-notify-users) paljasti 530 miljoonan käyttäjän tiedot, mikä johti 5 miljardin dollarin sovitteluun FTC:n kanssa. Se kuitenkin kieltäytyi ilmoittamasta käyttäjille tietovuodosta, mikä rikkoi käyttäjien oikeuksia datan läpinäkyvyyden ja saatavuuden osalta. |

Haluatko tutkia lisää tapaustutkimuksia? Katso nämä resurssit:
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - eettisiä dilemmoja eri toimialoilla.
* [Data Science Ethics -kurssi](https://www.coursera.org/learn/data-science-ethics#syllabus) - merkittäviä tapaustutkimuksia.
* [Missä asiat ovat menneet pieleen](https://deon.drivendata.org/examples/) - Deon-tarkistuslista esimerkkien kanssa.

> 🚨 Mieti tapaustutkimuksia, joita olet nähnyt – oletko kokenut tai ollut osallisena vastaavassa eettisessä haasteessa elämässäsi? Voitko keksiä ainakin yhden muun tapaustutkimuksen, joka havainnollistaa jotakin tässä osiossa käsitellyistä eettisistä haasteista?

## Soveltava etiikka

Olemme käsitelleet etiikan käsitteitä, haasteita ja tapaustutkimuksia todellisissa konteksteissa. Mutta miten voimme aloittaa eettisten periaatteiden ja käytäntöjen _soveltamisen_ projekteissamme? Ja miten voimme _operationalisoida_ nämä käytännöt paremman hallinnan saavuttamiseksi? Tutkitaan joitakin käytännön ratkaisuja:

### 1. Ammattikoodit

Ammattikoodit tarjoavat yhden vaihtoehdon organisaatioille "kannustaa" jäseniä tukemaan eettisiä periaatteitaan ja missiolauseitaan. Koodit ovat _moraalisia ohjeita_ ammatilliselle käyttäytymiselle, jotka auttavat työntekijöitä tai jäseniä tekemään päätöksiä, jotka ovat linjassa organisaation periaatteiden kanssa. Ne ovat vain niin hyviä kuin jäsenten vapaaehtoinen noudattaminen; monet organisaatiot tarjoavat kuitenkin lisäpalkintoja ja -rangaistuksia motivoidakseen jäseniä noudattamaan koodia.

Esimerkkejä:
* [Oxford Munich](http://www.code-of-ethics.org/code-of-conduct/) Code of Ethics
* [Data Science Association](http://datascienceassn.org/code-of-conduct.html) Code of Conduct (luotu 2013)
* [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (vuodesta 1993)

> 🚨 Kuulutko ammatilliseen insinööri- tai data science -organisaatioon? Tutki heidän sivustoaan nähdäksesi, määrittelevätkö he ammatillisen eettisen koodin. Mitä tämä kertoo heidän eettisistä periaatteistaan? Miten he "kannustavat" jäseniä noudattamaan koodia?

### 2. Etiikan tarkistuslistat

Vaikka ammattikoodit määrittelevät vaaditun _eettisen käyttäytymisen_ ammattilaisilta, niillä [on tunnettuja rajoituksia](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md) valvonnassa, erityisesti laajamittaisissa projekteissa. Sen sijaan monet data science -asiantuntijat [suosittelevat tarkistuslistoja](https://resources.oreilly.com/examples/0636920203964/blob/master/of_oaths_and_checklists.md), jotka voivat **yhdistää periaatteet käytäntöihin** määrätietoisemmilla ja toiminnallisemmilla tavoilla.

Tarkistuslistat muuttavat kysymykset "kyllä/ei"-tehtäviksi, jotka voidaan operationalisoida, jolloin niitä voidaan seurata osana standardeja tuotteen julkaisutyönkulkuja.

Esimerkkejä:
* [Deon](https://deon.drivendata.org/) - yleiskäyttöinen dataetiikan tarkistuslista, joka on luotu [teollisuuden suosituksista](https://deon.drivendata.org/#checklist-citations) ja sisältää komentorivityökalun helppoa integrointia varten.
* [Tietosuojan auditointitarkistuslista](https://cyber.harvard.edu/ecommerce/privacyaudit.html) - tarjoaa yleistä ohjeistusta tietojen käsittelykäytännöistä oikeudellisista ja sosiaalisista näkökulmista.
* [AI Fairness -tarkistuslista](https://www.microsoft.com/en-us/research/project/ai-fairness-checklist/) - luotu tekoälyasiantuntijoiden toimesta tukemaan oikeudenmukaisuustarkistusten käyttöönottoa ja integrointia tekoälyn kehityssykleihin.
* [22 kysymystä datan ja tekoälyn etiikasta](https://medium.com/the-organization/22-questions-for-ethics-in-data-and-ai-efb68fd19429) - avoimempi kehys, joka on suunniteltu eettisten kysymysten alkuperäiseen tutkimiseen suunnittelu-, toteutus- ja organisaatiokonteksteissa.

### 3. Etiikan sääntely

Etiikka tarkoittaa yhteisten arvojen määrittämistä ja oikean tekemistä _vapaaehtoisesti_. **Noudattaminen** tarkoittaa _lain noudattamista_ silloin ja siellä, missä se on määritelty. **Hallinto** kattaa laajemmin kaikki tavat, joilla organisaatiot toimivat eettisten periaatteiden täytäntöönpanemiseksi ja määriteltyjen lakien noudattamiseksi.

Nykyään hallinto ilmenee organisaatioissa kahdella tavalla. Ensinnäkin se tarkoittaa **eettisten tekoälyperiaatteiden** määrittämistä ja käytäntöjen luomista niiden käyttöönoton operationalisoimiseksi kaikissa organisaation tekoälyyn liittyvissä projekteissa. Toiseksi se tarkoittaa kaikkien hallituksen määräämien **tietosuojamääräysten** noudattamista niillä alueilla, joilla organisaatio toimii.

Esimerkkejä tietosuoja- ja yksityisyysmääräyksistä:

* `1974`, [Yhdysvaltain Privacy Act](https://www.justice.gov/opcl/privacy-act-1974) - säätelee _liittovaltion hallituksen_ henkilötietojen keräämistä, käyttöä ja luovutusta.
* `1996`, [Yhdysvaltain Health Insurance Portability & Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) - suojaa henkilökohtaisia terveystietoja.
* `1998`, [Yhdysvaltain Children's Online Privacy Protection Act (COPPA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) - suojaa alle 13-vuotiaiden lasten tietosuojaa.
* `2018`, [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) - tarjoaa käyttäjän oikeuksia, tietosuojaa ja yksityisyyttä.
* `2018`, [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa) antaa kuluttajille enemmän _oikeuksia_ heidän (henkilökohtaisiin) tietoihinsa.
* `2021`, Kiinan [Personal Information Protection Law](https://www.reuters.com/world/china/china-passes-new-personal-data-privacy-law-take-effect-nov-1-2021-08-20/) juuri hyväksytty, luoden yhden maailman vahvimmista verkkotietosuojamääräyksistä.

> 🚨 Euroopan unionin määrittelemä GDPR (General Data Protection Regulation) on edelleen yksi vaikutusvaltaisimmista tietosuojamääräyksistä tänään. Tiesitkö, että se myös määrittelee [8 käyttäjän oikeutta](https://www.freeprivacypolicy.com/blog/8-user-rights-gdpr) kansalaisten digitaalisen yksityisyyden ja henkilötietojen suojaamiseksi? Opi, mitä nämä ovat ja miksi ne ovat tärkeitä.

### 4. Etiikan kulttuuri

Huomaa, että _noudattamisen_ (tehdä tarpeeksi täyttääkseen "lain kirjaimen") ja [systeemisten ongelmien](https://www.coursera.org/learn/data-science-ethics/home/week/4) (kuten jäykistyminen, tiedon epäsymmetria ja jakelun epäoikeudenmukaisuus) ratkaisemisen välillä on edelleen aineeton kuilu, joka voi nopeuttaa tekoälyn aseistamista.

Jälkimmäinen vaatii [yhteistyöhön perustuvia lähestymistapoja etiikan kulttuurien määrittämiseksi](https://towardsdatascience.com/why-ai-ethics-requires-a-culture-driven-approach-26f451afa29f), jotka rakentavat emotionaalisia yhteyksiä ja johdonmukaisia yhteisiä arvoja _organisaatioiden_ välillä teollisuudessa. Tämä vaatii enemmän [formalisoituja dataetiikan kulttuureja](https://www.codeforamerica.org/news/formalizing-an-ethical-data-culture/) organisaatioissa – mahdollistaen _kenelle tahansa_ [vetää Andon-köyttä](https://en.wikipedia.org/wiki/Andon_(manufacturing)) (nostaa eettisiä huolenaiheita prosessin alkuvaiheessa) ja tehdä _eettisiä arviointeja_ (esim. rekrytoinnissa) tekoälyprojektien tiimien muodostamisen keskeisenä kriteerinä.

---
## [Luennon jälkeinen kysely](https://ff-quizzes.netlify.app/en/ds/quiz/3) 🎯
## Kertaus ja itseopiskelu

Kurssit ja kirjat auttavat ymmärtämään keskeisiä etiikan käsitteitä ja haasteita,
* [Machine Learning For Beginners](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/3-fairness/README.md) - oppitunti oikeudenmukaisuudesta, Microsoftilta.
* [Vastuullisen tekoälyn periaatteet](https://docs.microsoft.com/en-us/learn/modules/responsible-ai-principles/) - ilmainen oppimispolku Microsoft Learnilta.
* [Etiikka ja data-analytiikka](https://resources.oreilly.com/examples/0636920203964) - O'Reilly EBook (M. Loukides, H. Mason ym.)
* [Data-analytiikan etiikka](https://www.coursera.org/learn/data-science-ethics#syllabus) - verkkokurssi Michiganin yliopistolta.
* [Ethics Unwrapped](https://ethicsunwrapped.utexas.edu/case-studies) - tapaustutkimuksia Texasin yliopistolta.

# Tehtävä

[Kirjoita tapaustutkimus dataetiikasta](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.