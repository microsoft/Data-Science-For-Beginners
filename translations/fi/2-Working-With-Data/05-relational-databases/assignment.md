<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-26T20:52:32+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "fi"
}
-->
# Lentokenttätietojen näyttäminen

Sinulle on annettu [tietokanta](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db), joka on rakennettu [SQLite](https://sqlite.org/index.html) -alustalle ja sisältää tietoa lentokentistä. Skeema on esitetty alla. Käytät [SQLite-laajennusta](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) -ohjelmassa näyttääksesi tietoa eri kaupunkien lentokentistä.

## Ohjeet

Tehtävän aloittamiseksi sinun tulee suorittaa muutama vaihe. Sinun tulee asentaa tarvittavat työkalut ja ladata esimerkkitietokanta.

### Järjestelmän valmistelu

Voit käyttää Visual Studio Codea ja SQLite-laajennusta vuorovaikutukseen tietokannan kanssa.

1. Siirry osoitteeseen [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) ja seuraa ohjeita Visual Studio Coden asentamiseksi
1. Asenna [SQLite-laajennus](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) Marketplace-sivun ohjeiden mukaisesti

### Lataa ja avaa tietokanta

Seuraavaksi lataa ja avaa tietokanta.

1. Lataa [tietokantatiedosto GitHubista](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) ja tallenna se hakemistoon
1. Avaa Visual Studio Code
1. Avaa tietokanta SQLite-laajennuksessa valitsemalla **Ctl-Shift-P** (tai **Cmd-Shift-P** Macilla) ja kirjoittamalla `SQLite: Open database`
1. Valitse **Choose database from file** ja avaa **airports.db** -tiedosto, jonka latasit aiemmin
1. Tietokannan avaamisen jälkeen (et näe päivitystä näytöllä), luo uusi kyselyikkuna valitsemalla **Ctl-Shift-P** (tai **Cmd-Shift-P** Macilla) ja kirjoittamalla `SQLite: New query`

Kun kyselyikkuna on avattu, sitä voidaan käyttää SQL-lauseiden suorittamiseen tietokantaa vastaan. Voit käyttää komentoa **Ctl-Shift-Q** (tai **Cmd-Shift-Q** Macilla) suorittaaksesi kyselyitä tietokantaa vastaan.

> [!NOTE] Lisätietoja SQLite-laajennuksesta löydät [dokumentaatiosta](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Tietokannan skeema

Tietokannan skeema tarkoittaa sen taulujen suunnittelua ja rakennetta. **airports**-tietokannassa on kaksi taulua: `cities`, joka sisältää luettelon kaupungeista Yhdistyneessä kuningaskunnassa ja Irlannissa, sekä `airports`, joka sisältää luettelon kaikista lentokentistä. Koska joillakin kaupungeilla voi olla useita lentokenttiä, tiedot on tallennettu kahteen tauluun. Tässä harjoituksessa käytät liitoksia näyttääksesi tietoa eri kaupungeista.

| Cities           |
| ---------------- |
| id (PK, integer) |
| city (text)      |
| country (text)   |

| Airports                         |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK to id in **Cities**) |

## Tehtävä

Luo kyselyitä, jotka palauttavat seuraavat tiedot:

1. kaikki kaupunkien nimet `Cities`-taulusta
1. kaikki Irlannin kaupungit `Cities`-taulusta
1. kaikkien lentokenttien nimet sekä niiden kaupunki ja maa
1. kaikki Lontoon, Yhdistyneen kuningaskunnan lentokentät

## Arviointikriteerit

| Erinomainen | Riittävä | Parannettavaa |
| ----------- | -------- | ------------- |

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.