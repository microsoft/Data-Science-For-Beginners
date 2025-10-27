<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80d80300002ef4e77cc7631d5904bd6e",
  "translation_date": "2025-10-25T18:56:47+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "fi"
}
-->
# Työskentely datan kanssa: Relaatiotietokannat

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Työskentely datan kanssa: Relaatiotietokannat - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Todennäköisesti olet aiemmin käyttänyt taulukkolaskentaohjelmaa tiedon tallentamiseen. Sinulla oli rivejä ja sarakkeita, joissa rivit sisälsivät tiedot ja sarakkeet kuvasivat tietoja (joskus kutsutaan metatiedoksi). Relaatiotietokanta perustuu tähän perusperiaatteeseen, jossa taulukot koostuvat sarakkeista ja riveistä, ja tiedot voivat olla hajautettuina useisiin taulukoihin. Tämä mahdollistaa monimutkaisemman datan käsittelyn, tietojen toiston välttämisen ja joustavuuden datan tutkimisessa. Tutustutaanpa relaatiotietokannan käsitteisiin.

## [Ennakkokysely](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Kaikki alkaa taulukoista

Relaatiotietokannan ydin on taulukot. Aivan kuten taulukkolaskennassa, taulukko on sarakkeiden ja rivien kokoelma. Rivi sisältää tiedot, joiden kanssa haluamme työskennellä, kuten kaupungin nimi tai sademäärä. Sarakkeet kuvaavat tallennettavia tietoja.

Aloitetaan tutkimalla taulukkoa, johon tallennamme tietoa kaupungeista. Voisimme aloittaa niiden nimellä ja maalla. Voisit tallentaa nämä tiedot taulukkoon seuraavasti:

| Kaupunki | Maa           |
| -------- | ------------- |
| Tokio    | Japani        |
| Atlanta  | Yhdysvallat   |
| Auckland | Uusi-Seelanti |

Huomaa, että sarakkeiden nimet **kaupunki**, **maa** ja **väkiluku** kuvaavat tallennettavia tietoja, ja jokainen rivi sisältää tiedot yhdestä kaupungista.

## Yhden taulukon lähestymistavan puutteet

Todennäköisesti yllä oleva taulukko vaikuttaa melko tutulta. Lisätään nyt lisää tietoa kasvavaan tietokantaamme - vuotuinen sademäärä (millimetreinä). Keskitymme vuosiin 2018, 2019 ja 2020. Jos lisäisimme tiedot Tokiolle, se voisi näyttää tältä:

| Kaupunki | Maa     | Vuosi | Määrä |
| -------- | ------- | ----- | ----- |
| Tokio    | Japani  | 2020  | 1690  |
| Tokio    | Japani  | 2019  | 1874  |
| Tokio    | Japani  | 2018  | 1445  |

Mitä huomaat taulukostamme? Saatat huomata, että toistamme kaupungin nimen ja maan uudelleen ja uudelleen. Tämä voi viedä melko paljon tallennustilaa, ja on suurelta osin tarpeetonta, koska olemme kiinnostuneita vain yhdestä Tokion nimestä.

Kokeillaan jotain muuta. Lisätään uusia sarakkeita jokaiselle vuodelle:

| Kaupunki  | Maa           | 2018 | 2019 | 2020 |
| --------- | ------------- | ---- | ---- | ---- |
| Tokio     | Japani        | 1445 | 1874 | 1690 |
| Atlanta   | Yhdysvallat   | 1779 | 1111 | 1683 |
| Auckland  | Uusi-Seelanti | 1386 | 942  | 1176 |

Vaikka tämä välttää rivien toistamisen, se tuo mukanaan muita haasteita. Meidän pitäisi muuttaa taulukon rakennetta joka kerta, kun tulee uusi vuosi. Lisäksi, kun datamäärä kasvaa, vuosien pitäminen sarakkeina tekee arvojen hakemisesta ja laskemisesta hankalampaa.

Tämän vuoksi tarvitsemme useita taulukoita ja niiden välisiä suhteita. Jakamalla tietomme osiin voimme välttää toistoa ja saada enemmän joustavuutta datan käsittelyyn.

## Suhteiden käsitteet

Palataan tietoihimme ja mietitään, miten haluamme jakaa ne. Tiedämme, että haluamme tallentaa kaupunkien nimet ja maat, joten tämä toimii todennäköisesti parhaiten yhdessä taulukossa.

| Kaupunki  | Maa           |
| --------- | ------------- |
| Tokio     | Japani        |
| Atlanta   | Yhdysvallat   |
| Auckland  | Uusi-Seelanti |

Mutta ennen kuin luomme seuraavan taulukon, meidän täytyy päättää, miten viittaamme jokaiseen kaupunkiin. Tarvitsemme jonkinlaisen tunnisteen, ID:n tai (teknisessä tietokantatermistössä) pääavaimen. Pääavain on arvo, jota käytetään yksittäisen rivin tunnistamiseen taulukossa. Vaikka tämä voisi perustua itse arvoon (voisimme käyttää esimerkiksi kaupungin nimeä), sen tulisi lähes aina olla numero tai muu tunniste. Emme halua, että ID muuttuu koskaan, koska se rikkoisi suhteen. Useimmissa tapauksissa pääavain tai ID on automaattisesti luotu numero.

> ✅ Pääavain lyhennetään usein PK

### kaupungit

| city_id | Kaupunki  | Maa           |
| ------- | --------- | ------------- |
| 1       | Tokio     | Japani        |
| 2       | Atlanta   | Yhdysvallat   |
| 3       | Auckland  | Uusi-Seelanti |

> ✅ Huomaat, että käytämme termejä "id" ja "pääavain" (primary key) vuorotellen tämän oppitunnin aikana. Nämä käsitteet pätevät myös DataFrameihin, joihin tutustut myöhemmin. DataFramet eivät käytä "pääavain"-terminologiaa, mutta huomaat, että ne toimivat hyvin samalla tavalla.

Kun kaupunkitaulukkomme on luotu, tallennetaan sademäärät. Sen sijaan, että toistaisimme kaupungin täydelliset tiedot, voimme käyttää ID:tä. Meidän tulisi myös varmistaa, että juuri luodulla taulukolla on *id*-sarake, sillä kaikilla taulukoilla tulisi olla ID tai pääavain.

### sademäärä

| rainfall_id | city_id | Vuosi | Määrä |
| ----------- | ------- | ----- | ----- |
| 1           | 1       | 2018  | 1445  |
| 2           | 1       | 2019  | 1874  |
| 3           | 1       | 2020  | 1690  |
| 4           | 2       | 2018  | 1779  |
| 5           | 2       | 2019  | 1111  |
| 6           | 2       | 2020  | 1683  |
| 7           | 3       | 2018  | 1386  |
| 8           | 3       | 2019  | 942   |
| 9           | 3       | 2020  | 1176  |

Huomaa **city_id**-sarake juuri luodussa **sademäärä**-taulukossa. Tämä sarake sisältää arvoja, jotka viittaavat **kaupungit**-taulukon ID:ihin. Teknisessä relaatiotietokantatermistössä tätä kutsutaan **vierasavaimeksi**; se on toisen taulukon pääavain. Voit ajatella sitä viittauksena tai osoittimena. **city_id** 1 viittaa Tokioon.

> [!NOTE] 
> Vierasavain lyhennetään usein FK

## Tietojen hakeminen

Kun tietomme on jaettu kahteen taulukkoon, saatat miettiä, miten ne haetaan. Jos käytämme relaatiotietokantaa, kuten MySQL, SQL Server tai Oracle, voimme käyttää kieltä nimeltä Structured Query Language eli SQL. SQL (joskus lausutaan "sequel") on standardikieli, jota käytetään tietojen hakemiseen ja muokkaamiseen relaatiotietokannassa.

Tietojen hakemiseen käytetään komentoa `SELECT`. Perusperiaatteena on, että **valitset** sarakkeet, jotka haluat nähdä, ja **mistä** taulukosta ne löytyvät. Jos haluaisit näyttää vain kaupunkien nimet, voisit käyttää seuraavaa:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT`-komennossa luetellaan sarakkeet, ja `FROM`-komennossa taulukot.

> [!NOTE] 
> SQL-syntaksi ei ole kirjainkoolle herkkä, eli `select` ja `SELECT` tarkoittavat samaa. Kuitenkin riippuen käyttämästäsi tietokantatyypistä sarakkeet ja taulukot voivat olla kirjainkoolle herkkiä. Tämän vuoksi on hyvä käytäntö aina käsitellä kaikkea ohjelmoinnissa kuin se olisi kirjainkoolle herkkää. SQL-kyselyitä kirjoitettaessa yleinen tapa on käyttää avainsanoja kokonaan isoilla kirjaimilla.

Yllä oleva kysely näyttää kaikki kaupungit. Kuvitellaan, että haluaisimme näyttää vain Uuden-Seelannin kaupungit. Tarvitsemme jonkinlaisen suodattimen. SQL-avainsana tähän on `WHERE`, eli "missä jokin ehto täyttyy".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Tietojen yhdistäminen

Tähän asti olemme hakeneet tietoja yhdestä taulukosta. Nyt haluamme yhdistää tiedot sekä **kaupungit**- että **sademäärä**-taulukoista. Tämä tehdään *liittämällä* ne yhteen. Käytännössä luot saumakohdan kahden taulukon välille ja yhdistät sarakkeiden arvot toisiinsa.

Esimerkissämme yhdistämme **city_id**-sarakkeen **sademäärä**-taulukosta **city_id**-sarakkeeseen **kaupungit**-taulukossa. Tämä yhdistää sademäärän sen vastaavaan kaupunkiin. Suoritamme niin sanotun *sisäisen* liitoksen, mikä tarkoittaa, että jos mikään rivi ei vastaa toisen taulukon tietoja, sitä ei näytetä. Meidän tapauksessamme jokaisella kaupungilla on sademäärätiedot, joten kaikki näytetään.

Haetaan vuoden 2019 sademäärät kaikille kaupungeille.

Teemme tämän vaiheittain. Ensimmäinen vaihe on yhdistää tiedot ilmoittamalla sarakkeet saumakohtaa varten - **city_id**, kuten aiemmin korostettiin.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Olemme korostaneet kaksi saraketta, jotka haluamme yhdistää, ja sen, että haluamme liittää taulukot yhteen **city_id**-sarakkeen avulla. Nyt voimme lisätä `WHERE`-lauseen suodattamaan vain vuoden 2019 tiedot.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
WHERE rainfall.year = 2019

-- Output

-- city     | amount
-- -------- | ------
-- Tokyo    | 1874
-- Atlanta  | 1111
-- Auckland |  942
```

## Yhteenveto

Relaatiotietokannat perustuvat tiedon jakamiseen useisiin taulukoihin, jotka tuodaan takaisin yhteen näyttämistä ja analysointia varten. Tämä tarjoaa suuren joustavuuden laskelmien tekemiseen ja datan muokkaamiseen. Olet nähnyt relaatiotietokannan keskeiset käsitteet ja miten suorittaa liitos kahden taulukon välillä.

## 🚀 Haaste

Internetissä on saatavilla lukuisia relaatiotietokantoja. Voit tutkia dataa käyttämällä yllä oppimiasi taitoja.

## Jälkikysely

## [Jälkikysely](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Kertaus ja itseopiskelu

Microsoft Learn -sivustolla on saatavilla useita resursseja, joiden avulla voit jatkaa SQL:n ja relaatiotietokannan käsitteiden tutkimista.

- [Relaatiodatan käsitteiden kuvaus](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Aloita kyselyiden tekeminen Transact-SQL:llä](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL on SQL:n versio)
- [SQL-sisältö Microsoft Learn -sivustolla](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Tehtävä

[Tehtävän nimi](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.