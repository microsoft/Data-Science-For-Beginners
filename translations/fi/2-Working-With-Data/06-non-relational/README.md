<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c182e87f9f80be7e7cdffc7b40bbfccf",
  "translation_date": "2025-09-05T22:36:11+00:00",
  "source_file": "2-Working-With-Data/06-non-relational/README.md",
  "language_code": "fi"
}
-->
# Työskentely datan kanssa: Ei-relationaalinen data

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/06-NoSQL.png)|
|:---:|
|Työskentely NoSQL-datan kanssa - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Esiluentavisa](https://ff-quizzes.netlify.app/en/ds/quiz/10)

Data ei rajoitu vain relationaalisiin tietokantoihin. Tämä oppitunti keskittyy ei-relationaaliseen dataan ja kattaa taulukkolaskentaohjelmien ja NoSQL:n perusteet.

## Taulukkolaskentaohjelmat

Taulukkolaskentaohjelmat ovat suosittu tapa tallentaa ja tutkia dataa, koska niiden käyttöönotto ja aloitus vaativat vähemmän työtä. Tässä oppitunnissa opit taulukkolaskennan perusosat sekä kaavat ja funktiot. Esimerkit havainnollistetaan Microsoft Excelillä, mutta suurimmalla osalla osista ja aiheista on samankaltaiset nimet ja vaiheet muihin taulukkolaskentaohjelmiin verrattuna.

![Tyhjä Microsoft Excel -työkirja, jossa on kaksi laskentataulukkoa](../../../../2-Working-With-Data/06-non-relational/images/parts-of-spreadsheet.png)

Taulukkolaskenta on tiedosto, joka on käytettävissä tietokoneen, laitteen tai pilvipohjaisen tiedostojärjestelmän tiedostojärjestelmässä. Itse ohjelmisto voi olla selainpohjainen tai sovellus, joka on asennettava tietokoneelle tai ladattava sovelluksena. Excelissä näitä tiedostoja kutsutaan myös **työkirjoiksi**, ja tätä terminologiaa käytetään loppuosassa tätä oppituntia.

Työkirja sisältää yhden tai useamman **laskentataulukon**, joista jokainen on merkitty välilehdillä. Laskentataulukossa on suorakulmioita, joita kutsutaan **soluiksi**, ja ne sisältävät varsinaisen datan. Solu on rivin ja sarakkeen leikkauspiste, jossa sarakkeet on merkitty aakkosilla ja rivit numeroilla. Joissakin taulukkolaskentaohjelmissa ensimmäiset rivit sisältävät otsikoita, jotka kuvaavat solun dataa.

Näiden Excel-työkirjan peruselementtien avulla käytämme esimerkkiä [Microsoft Templates](https://templates.office.com/) -sivustolta, joka keskittyy varastoon, ja käymme läpi joitakin taulukkolaskennan lisäosia.

### Varaston hallinta

Taulukkolaskentatiedosto nimeltä "InventoryExample" on muotoiltu taulukkolaskenta, joka sisältää varaston kohteita ja kolme laskentataulukkoa, joiden välilehdet on nimetty "Inventory List", "Inventory Pick List" ja "Bin Lookup". Inventory List -laskentataulukon rivi 4 on otsikko, joka kuvaa kunkin solun arvon otsikkosarakkeessa.

![Korostettu kaava esimerkkinä varastoluettelosta Microsoft Excelissä](../../../../2-Working-With-Data/06-non-relational/images/formula-excel.png)

On tilanteita, joissa solun arvo riippuu muiden solujen arvoista. Inventory List -taulukkolaskenta seuraa jokaisen varastossa olevan kohteen kustannuksia, mutta entä jos haluamme tietää koko varaston arvon? [**Kaavat**](https://support.microsoft.com/en-us/office/overview-of-formulas-34519a4e-1e8d-4f4b-84d4-d642c4f63263) suorittavat toimintoja soludatalla ja niitä käytetään tässä esimerkissä laskemaan varaston arvo. Tämä taulukkolaskenta käyttää kaavaa Inventory Value -sarakkeessa laskemaan kunkin kohteen arvon kertomalla QTY-otsikon alla oleva määrä ja COST-otsikon alla olevat kustannukset. Kaksoisnapsauttamalla tai korostamalla solua näet kaavan. Huomaat, että kaavat alkavat yhtäläisyysmerkillä, jota seuraa laskenta tai operaatio.

![Korostettu funktio esimerkkinä varastoluettelosta Microsoft Excelissä](../../../../2-Working-With-Data/06-non-relational/images/function-excel.png)

Voimme käyttää toista kaavaa lisätäksemme kaikki Inventory Value -arvot yhteen saadaksemme niiden kokonaisarvon. Tämä voitaisiin laskea lisäämällä jokainen solu yhteen, mutta se voi olla työlästä. Excelissä on [**funktioita**](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89), eli ennalta määritettyjä kaavoja, jotka suorittavat laskelmia soluarvoilla. Funktiot vaativat argumentteja, jotka ovat laskelmissa tarvittavia arvoja. Kun funktiot vaativat useamman kuin yhden argumentin, ne on listattava tietyssä järjestyksessä, muuten funktio ei ehkä laske oikeaa arvoa. Tässä esimerkissä käytetään SUM-funktiota, ja argumenttina käytetään Inventory Value -arvoja, jotta saadaan kokonaisarvo, joka on listattu rivillä 3, sarakkeessa B (tunnetaan myös nimellä B3).

## NoSQL

NoSQL on kattotermi erilaisille tavoille tallentaa ei-relationaalista dataa, ja se voidaan tulkita "non-SQL", "ei-relationaalinen" tai "ei vain SQL". Tämän tyyppiset tietokantajärjestelmät voidaan luokitella neljään tyyppiin.

![Graafinen esitys avain-arvo-tietokannasta, jossa on 4 uniikkia numeerista avainta, jotka liittyvät 4 erilaiseen arvoon](../../../../2-Working-With-Data/06-non-relational/images/kv-db.png)
> Lähde: [Michał Białecki Blog](https://www.michalbialecki.com/2018/03/18/azure-cosmos-db-key-value-database-cloud/)

[Avain-arvo](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#keyvalue-data-stores) -tietokannat yhdistävät uniikit avaimet, jotka ovat yksilöllisiä tunnisteita, arvoihin. Nämä parit tallennetaan [hajautustauluun](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/) sopivan hajautusfunktion avulla.

![Graafinen esitys graafitietokannasta, joka näyttää ihmisten, heidän kiinnostuksen kohteidensa ja sijaintien väliset suhteet](../../../../2-Working-With-Data/06-non-relational/images/graph-db.png)
> Lähde: [Microsoft](https://docs.microsoft.com/en-us/azure/cosmos-db/graph/graph-introduction#graph-database-by-example)

[Graafi](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#graph-data-stores) -tietokannat kuvaavat datan välisiä suhteita ja esitetään solmujen ja kaarien kokoelmana. Solmu edustaa entiteettiä, jotain, joka on olemassa reaalimaailmassa, kuten opiskelija tai pankkitiliote. Kaarilla kuvataan kahden entiteetin välistä suhdetta. Jokaisella solmulla ja kaarella on ominaisuuksia, jotka antavat lisätietoa niistä.

![Graafinen esitys saraketietokannasta, joka näyttää asiakastietokannan kahdella sarakeperheellä nimeltä Identity ja Contact Info](../../../../2-Working-With-Data/06-non-relational/images/columnar-db.png)

[Sarakepohjaiset](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#columnar-data-stores) tietokannat järjestävät datan sarakkeisiin ja riveihin kuten relationaalisessa tietorakenteessa, mutta jokainen sarake on jaettu ryhmiin, joita kutsutaan sarakeperheiksi. Kaikki yhden sarakkeen data on toisiinsa liittyvää ja voidaan hakea ja muuttaa yhtenä yksikkönä.

### Dokumenttitietokannat Azure Cosmos DB:llä

[Dokumentti](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data#document-data-stores) -tietokannat perustuvat avain-arvo-tietokannan käsitteeseen ja koostuvat kentistä ja objekteista. Tässä osiossa tutkitaan dokumenttitietokantoja Cosmos DB -emulaattorin avulla.

Cosmos DB -tietokanta täyttää "Not Only SQL" -määritelmän, jossa Cosmos DB:n dokumenttitietokanta käyttää SQL:ää datan kyselyyn. [Edellinen oppitunti](../05-relational-databases/README.md) SQL:stä kattaa kielen perusteet, ja voimme soveltaa joitakin samoja kyselyitä dokumenttitietokantaan täällä. Käytämme Cosmos DB -emulaattoria, jonka avulla voimme luoda ja tutkia dokumenttitietokantaa paikallisesti tietokoneella. Lue lisää emulaattorista [täältä](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21).

Dokumentti on kenttien ja objektien kokoelma, jossa kentät kuvaavat, mitä objektin arvo edustaa. Alla on esimerkki dokumentista.

```json
{
    "firstname": "Eva",
    "age": 44,
    "id": "8c74a315-aebf-4a16-bb38-2430a9896ce5",
    "_rid": "bHwDAPQz8s0BAAAAAAAAAA==",
    "_self": "dbs/bHwDAA==/colls/bHwDAPQz8s0=/docs/bHwDAPQz8s0BAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f95-010a691e01d7\"",
    "_attachments": "attachments/",
    "_ts": 1630544034
}
```

Tämän dokumentin kiinnostavia kenttiä ovat: `firstname`, `id` ja `age`. Loput kentistä, joissa on alaviivoja, on luotu Cosmos DB:n toimesta.

#### Datan tutkiminen Cosmos DB -emulaattorilla

Voit ladata ja asentaa emulaattorin [Windowsille täältä](https://aka.ms/cosmosdb-emulator). Katso tämä [dokumentaatio](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos) saadaksesi ohjeita emulaattorin suorittamiseen macOS:llä ja Linuxilla.

Emulaattori avaa selainikkunan, jossa Explorer-näkymä mahdollistaa dokumenttien tutkimisen.

![Cosmos DB -emulaattorin Explorer-näkymä](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-explorer.png)

Jos seuraat mukana, napsauta "Start with Sample" luodaksesi esimerkkitietokannan nimeltä SampleDB. Jos laajennat SampleDB:n napsauttamalla nuolta, löydät säilön nimeltä `Persons`. Säilö sisältää kokoelman kohteita, jotka ovat säilön sisällä olevia dokumentteja. Voit tutkia neljää yksittäistä dokumenttia `Items`-kohdassa.

![Esimerkkidatan tutkiminen Cosmos DB -emulaattorissa](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons.png)

#### Dokumenttidatan kysely Cosmos DB -emulaattorilla

Voimme myös tehdä kyselyitä esimerkkidatalle napsauttamalla uutta SQL Query -painiketta (toinen painike vasemmalta).

`SELECT * FROM c` palauttaa kaikki säilön dokumentit. Lisätään where-lauseke ja etsitään kaikki, jotka ovat alle 40-vuotiaita.

`SELECT * FROM c where c.age < 40`

![SELECT-kyselyn suorittaminen esimerkkidatalle Cosmos DB -emulaattorissa, jotta löydetään dokumentit, joiden age-kentän arvo on alle 40](../../../../2-Working-With-Data/06-non-relational/images/cosmosdb-emulator-persons-query.png)

Kysely palauttaa kaksi dokumenttia, huomaa, että kunkin dokumentin age-arvo on alle 40.

#### JSON ja dokumentit

Jos tunnet JavaScript Object Notationin (JSON), huomaat, että dokumentit näyttävät samankaltaisilta kuin JSON. Tässä hakemistossa on `PersonsData.json`-tiedosto, jossa on lisää dataa, jonka voit ladata Persons-säilöön emulaattorissa `Upload Item` -painikkeen avulla.

Useimmissa tapauksissa API:t, jotka palauttavat JSON-dataa, voidaan siirtää suoraan ja tallentaa dokumenttitietokantoihin. Alla on toinen dokumentti, joka edustaa Microsoftin Twitter-tilin twiittejä, jotka on haettu Twitter-rajapinnan avulla ja lisätty Cosmos DB:hen.

```json
{
    "created_at": "2021-08-31T19:03:01.000Z",
    "id": "1432780985872142341",
    "text": "Blank slate. Like this tweet if you’ve ever painted in Microsoft Paint before. https://t.co/cFeEs8eOPK",
    "_rid": "dhAmAIUsA4oHAAAAAAAAAA==",
    "_self": "dbs/dhAmAA==/colls/dhAmAIUsA4o=/docs/dhAmAIUsA4oHAAAAAAAAAA==/",
    "_etag": "\"00000000-0000-0000-9f84-a0958ad901d7\"",
    "_attachments": "attachments/",
    "_ts": 1630537000
```

Tämän dokumentin kiinnostavia kenttiä ovat: `created_at`, `id` ja `text`.

## 🚀 Haaste

Hakemistossa on `TwitterData.json`-tiedosto, jonka voit ladata SampleDB-tietokantaan. On suositeltavaa, että lisäät sen erilliseen säilöön. Tämä voidaan tehdä seuraavasti:

1. Napsauta oikeassa yläkulmassa olevaa uutta säilöä -painiketta
2. Valitse olemassa oleva tietokanta (SampleDB) ja luo säilön tunnus
3. Aseta osioavaimeksi `/id`
4. Napsauta OK (voit ohittaa muut tiedot tässä näkymässä, koska tämä on pieni datasetti, joka toimii paikallisesti koneellasi)
5. Avaa uusi säilösi ja lataa Twitter Data -tiedosto `Upload Item` -painikkeella

Yritä suorittaa muutamia SELECT-kyselyitä löytääksesi dokumentit, joissa tekstikentässä on sana "Microsoft". Vihje: kokeile käyttää [LIKE-avainsanaa](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-query-keywords#using-like-with-the--wildcard-character).

## [Jälkiluentavisa](https://ff-quizzes.netlify.app/en/ds/quiz/11)

## Kertaus ja itseopiskelu

- Tässä taulukkolaskennassa on joitakin lisämuotoiluja ja ominaisuuksia, joita tämä oppitunti ei kata. Microsoftilla on [laaja kirjasto dokumentaatiota ja videoita](https://support.microsoft.com/excel) Excelistä, jos haluat oppia lisää.

- Tämä arkkitehtuuridokumentaatio kuvaa ei-relationaalisen datan eri tyyppien ominaisuuksia: [Ei-relationaalinen data ja NoSQL](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/non-relational-data)

- Cosmos DB on pilvipohjainen ei-relationaalinen tietokanta, joka voi myös tallentaa tässä oppitunnissa mainittuja eri NoSQL-tyyppejä. Lue lisää näistä tyypeistä tässä [Cosmos DB Microsoft Learn -moduulissa](https://docs.microsoft.com/en-us/learn/paths/work-with-nosql-data-in-azure-cosmos-db/).

## Tehtävä

[Sooda-tuotot](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskääntämistä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virhetulkinnoista.