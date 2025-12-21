<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T11:38:29+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "fi"
}
-->
# Työskentely datan kanssa: Relaatiotietokannat

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Työskentely datan kanssa: Relaatiotietokannat - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Todennäköisesti olet aiemmin käyttänyt taulukkolaskentaohjelmaa tietojen tallentamiseen. Sinulla oli joukko rivejä ja sarakkeita, joissa rivit sisälsivät tiedot (tai datan) ja sarakkeet kuvasivat tietoja (joskus kutsutaan metatiedoiksi). Relaatiotietokanta perustuu tähän perusperiaatteeseen sarakkeista ja riveistä tauluissa, jolloin voit jakaa tiedot useisiin tauluihin. Tämä mahdollistaa monimutkaisemman datan käsittelyn, päällekkäisyyden välttämisen ja joustavuuden datan tutkimisessa. Tutkitaanpa relaatiotietokannan käsitteitä.

## [Ennakkotentti](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Kaikki alkaa tauluista

Relaatiotietokannan ytimessä ovat taulut. Kuten taulukkolaskennassa, taulu on sarakkeiden ja rivien kokoelma. Rivi sisältää datan tai tiedon, jonka kanssa haluamme työskennellä, kuten kaupungin nimen tai sademäärän. Sarakkeet kuvaavat tallennettua dataa.

Aloitetaan tutkimus luomalla taulu kaupungeista. Voisimme aloittaa niiden nimellä ja maalla. Voisit tallentaa tämän tauluun seuraavasti:

| Kaupunki | Maa           |
| -------- | ------------- |
| Tokio    | Japani        |
| Atlanta  | Yhdysvallat   |
| Auckland | Uusi-Seelanti |

Huomaa sarakkeiden nimet **kaupunki**, **maa** ja **väestö** kuvaavat tallennettua dataa, ja jokaisella rivillä on tieto yhdestä kaupungista.

## Yhden taulun lähestymistavan puutteet

Todennäköisesti yllä oleva taulu näyttää sinulle melko tutulta. Lisätään tietokantaamme lisää dataa – vuotuinen sademäärä (millimetreinä). Keskitymme vuosiin 2018, 2019 ja 2020. Jos lisäisimme sen Tokion osalta, se voisi näyttää tältä:

| Kaupunki | Maa     | Vuosi | Määrä |
| -------- | ------- | ----- | ----- |
| Tokio    | Japani  | 2020  | 1690  |
| Tokio    | Japani  | 2019  | 1874  |
| Tokio    | Japani  | 2018  | 1445  |

Mitä huomaat taulustamme? Saatat huomata, että toistamme kaupungin nimen ja maan yhä uudelleen. Se voi viedä paljon tallennustilaa, ja on suurelta osin tarpeetonta pitää useita kopioita. Tokion nimi on kuitenkin vain yksi, joka kiinnostaa meitä.

Kokeillaanpa jotain muuta. Lisätään uudet sarakkeet jokaiselle vuodelle:

| Kaupunki | Maa           | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokio    | Japani        | 1445 | 1874 | 1690 |
| Atlanta  | Yhdysvallat   | 1779 | 1111 | 1683 |
| Auckland | Uusi-Seelanti | 1386 | 942  | 1176 |

Vaikka tämä välttää rivien toistamisen, se tuo mukanaan muutamia muita haasteita. Meidän pitäisi muuttaa taulun rakennetta aina, kun tulee uusi vuosi. Lisäksi, kun datamme kasvaa, vuosien pitäminen sarakkeina tekee arvojen hakemisesta ja laskemisesta hankalampaa.

Siksi tarvitsemme useita tauluja ja suhteita. Jakamalla datamme voimme välttää päällekkäisyyttä ja saada enemmän joustavuutta datan käsittelyyn.

## Suhteiden käsitteet

Palataan dataamme ja päätetään, miten haluamme jakaa asiat. Tiedämme, että haluamme tallentaa kaupunkien nimet ja maat, joten tämä toimii parhaiten yhdessä taulussa.

| Kaupunki | Maa           |
| -------- | ------------- |
| Tokio    | Japani        |
| Atlanta  | Yhdysvallat   |
| Auckland | Uusi-Seelanti |

Mutta ennen kuin luomme seuraavan taulun, meidän täytyy selvittää, miten viitata kuhunkin kaupunkiin. Tarvitsemme jonkinlaisen tunnisteen, ID:n tai (teknisissä tietokantatermeissä) ensisijaisen avaimen. Ensisijainen avain on arvo, jota käytetään tunnistamaan yksi tietty rivi taulussa. Vaikka se voisi perustua itse arvoon (voisimme käyttää esimerkiksi kaupungin nimeä), sen tulisi lähes aina olla numero tai muu tunniste. Emme halua, että id koskaan muuttuu, koska se rikkoisi suhteen. Useimmissa tapauksissa ensisijainen avain tai id on automaattisesti luotu numero.

> ✅ Ensisijainen avain lyhennetään usein PK:ksi

### cities

| city_id | Kaupunki | Maa           |
| ------- | -------- | ------------- |
| 1       | Tokio    | Japani        |
| 2       | Atlanta  | Yhdysvallat   |
| 3       | Auckland | Uusi-Seelanti |

> ✅ Huomaat, että käytämme tässä oppitunnissa termejä "id" ja "ensisijainen avain" vaihdellen. Nämä käsitteet pätevät myös DataFrameihin, joita tutkit myöhemmin. DataFramet eivät kuitenkaan käytä termiä "ensisijainen avain", mutta käyttäytyvät hyvin samankaltaisesti.

Kun kaupunkitaulu on luotu, tallennetaan sademäärät. Sen sijaan, että toistaisimme koko kaupungin tiedot, voimme käyttää id:tä. Meidän tulisi myös varmistaa, että uudessa taulussa on *id*-sarake, sillä kaikilla tauluilla tulisi olla id tai ensisijainen avain.

### rainfall

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

Huomaa **city_id**-sarake uudessa **rainfall**-taulussa. Tämä sarake sisältää arvoja, jotka viittaavat **cities**-taulun ID-arvoihin. Teknisten relaatiotietojen termein tätä kutsutaan **vierasavaimeksi**; se on ensisijainen avain toisesta taulusta. Voit ajatella sitä viittauksena tai osoittimena. **city_id** 1 viittaa Tokioon.

> [!NOTE] 
> Vierasavain lyhennetään usein FK:ksi

## Datan hakeminen

Kun data on jaettu kahteen tauluun, saatat miettiä, miten sitä haetaan. Jos käytämme relaatiotietokantaa kuten MySQL, SQL Server tai Oracle, voimme käyttää kieltä nimeltä Structured Query Language eli SQL. SQL (joskus lausutaan sequel) on standardikieli, jolla haetaan ja muokataan dataa relaatiotietokannassa.

Datan hakemiseen käytetään komentoa `SELECT`. Periaatteessa **valitset** sarakkeet, jotka haluat nähdä, **taulusta**, jossa ne sijaitsevat. Jos haluat näyttää vain kaupunkien nimet, voit käyttää seuraavaa:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` on kohta, jossa luetellaan sarakkeet, ja `FROM` on kohta, jossa luetellaan taulut.

> [!NOTE] 
> SQL-syntaksi ei ole kirjainkoon herkkä, eli `select` ja `SELECT` tarkoittavat samaa. Kuitenkin tietokannan tyypistä riippuen sarakkeet ja taulut voivat olla kirjainkoon herkkiä. Siksi on hyvä käytäntö käsitellä kaikkea ohjelmoinnissa kuin se olisi kirjainkoon herkkää. SQL-kyselyissä on yleinen käytäntö kirjoittaa avainsanat kokonaan isoilla kirjaimilla.

Yllä oleva kysely näyttää kaikki kaupungit. Kuvitellaan, että haluamme näyttää vain Uuden-Seelannin kaupungit. Tarvitsemme jonkinlaisen suodattimen. SQL:n avainsana tähän on `WHERE`, eli "missä jokin ehto on tosi".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Datan yhdistäminen

Tähän asti olemme hakeneet dataa yhdestä taulusta. Nyt haluamme yhdistää datan sekä **cities**- että **rainfall**-tauluista. Tämä tehdään *liittämällä* ne yhteen. Luot käytännössä saumakohdan kahden taulun välille ja yhdistät sarakkeiden arvot.

Esimerkissämme yhdistämme **city_id**-sarakkeen **rainfall**-taulussa **city_id**-sarakkeeseen **cities**-taulussa. Tämä yhdistää sademäärän vastaavaan kaupunkiin. Suorittamamme liitos on ns. *inner* join, eli jos riveillä ei ole vastaavuutta toisessa taulussa, niitä ei näytetä. Meidän tapauksessamme jokaisella kaupungilla on sademäärä, joten kaikki näytetään.

Haetaan sademäärä vuodelta 2019 kaikille kaupungeille.

Teemme tämän vaiheittain. Ensimmäinen vaihe on liittää data yhteen osoittamalla saumakohdan sarakkeet - **city_id** kuten aiemmin korostettu.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Olemme korostaneet kaksi haluamaamme saraketta ja sen, että haluamme liittää taulut **city_id**-sarakkeen perusteella. Nyt voimme lisätä `WHERE`-lauseen suodattamaan vain vuosi 2019.

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

Relaatiotietokannat perustuvat tiedon jakamiseen useisiin tauluihin, jotka sitten yhdistetään näyttöä ja analyysiä varten. Tämä tarjoaa suuren joustavuuden laskelmien tekemiseen ja datan muokkaamiseen. Olet nähnyt relaatiotietokannan ydinkäsitteet ja miten liitos kahden taulun välillä tehdään.

## 🚀 Haaste

Internetissä on lukuisia relaatiotietokantoja. Voit tutkia dataa käyttämällä yllä opittuja taitoja.

## Jälkitentti

## [Jälkitentti](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Kertaus & Itsenäinen opiskelu

Microsoft Learnissä on useita resursseja, joiden avulla voit jatkaa SQL:n ja relaatiotietokantojen käsitteiden tutkimista

- [Kuvaile relaatiodatan käsitteitä](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Aloita kyselyt Transact-SQL:llä](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL on SQL:n versio)
- [SQL-sisältö Microsoft Learnissä](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Tehtävä

[Lentokenttätietojen näyttäminen](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->