<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "278a30661fe9f10afd81dea999adc63a",
  "translation_date": "2025-12-21T11:36:54+00:00",
  "source_file": "README.md",
  "language_code": "fi"
}
-->
# Data-analytiikka aloittelijoille - Opetussuunnitelma

[![Avaa GitHub Codespacesissa](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=344191198)

[![GitHub-lisenssi](https://img.shields.io/github/license/microsoft/Data-Science-For-Beginners.svg)](https://github.com/microsoft/Data-Science-For-Beginners/blob/master/LICENSE)
[![GitHubin tekijät](https://img.shields.io/github/contributors/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/graphs/contributors/)
[![GitHub-ongelmat](https://img.shields.io/github/issues/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/issues/)
[![GitHub pull-pyynnöt](https://img.shields.io/github/issues-pr/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/pulls/)
[![PR:t tervetulleita](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub-seuraajat](https://img.shields.io/github/watchers/microsoft/Data-Science-For-Beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/Data-Science-For-Beginners/watchers/)
[![GitHub-forkit](https://img.shields.io/github/forks/microsoft/Data-Science-For-Beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/Data-Science-For-Beginners/network/)
[![GitHub-tähdet](https://img.shields.io/github/stars/microsoft/Data-Science-For-Beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/Data-Science-For-Beginners/stargazers/)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Microsoft Foundryin kehittäjäfoorumi](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

Microsoftin Azure Cloud Advocates -tiimi iloitsee tarjotessaan 10-viikkoisen, 20-oppitunnin opetussuunnitelman, joka käsittelee data-analytiikkaa. Jokainen oppitunti sisältää ennakkokokeen ja jälkikokeen, kirjalliset ohjeet oppitunnin suorittamiseen, ratkaisun ja tehtävän. Projektipohjainen pedagogiikkamme antaa sinun oppia rakentamalla — todistettu tapa, jolla uudet taidot "juurtuvat".

**Sydämellinen kiitos kirjoittajillemme:** [Jasmine Greenaway](https://www.twitter.com/paladique), [Dmitry Soshnikov](http://soshnikov.com), [Nitya Narasimhan](https://twitter.com/nitya), [Jalen McGee](https://twitter.com/JalenMcG), [Jen Looper](https://twitter.com/jenlooper), [Maud Levy](https://twitter.com/maudstweets), [Tiffany Souterre](https://twitter.com/TiffanySouterre), [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏 Erityiskiitokset 🙏 [Microsoft Student Ambassador](https://studentambassadors.microsoft.com/) -kirjoittajille, tarkastajille ja sisällön tekijöille,** erityisesti Aaryan Arora, [Aditya Garg](https://github.com/AdityaGarg00), [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/), [Ankita Singh](https://www.linkedin.com/in/ankitasingh007), [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/), [Arpita Das](https://www.linkedin.com/in/arpitadas01/), ChhailBihari Dubey, [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor), [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [Majd Safi](https://www.linkedin.com/in/majd-s/), [Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/), [Miguel Correa](https://www.linkedin.com/in/miguelmque/), [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119), [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum), [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/), [Rohit Yadav](https://www.linkedin.com/in/rty2423), Samridhi Sharma, [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200),
[Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/), [Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/), Yogendrasingh Pawar , [Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/), [Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![Sketchnote: @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.fi.png)|
|:---:|
| Data-analytiikka aloittelijoille - _Sketchnote, tekijä [@nitya](https://twitter.com/nitya)_ |

### 🌐 Monikielinen tuki

#### Tuettu GitHub Actionin kautta (automaattinen ja aina ajan tasalla)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabia](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgaria](../bg/README.md) | [Burmalainen (Myanmar)](../my/README.md) | [Kiina (yksinkertaistettu)](../zh/README.md) | [Kiina (perinteinen, Hongkong)](../hk/README.md) | [Kiina (perinteinen, Makao)](../mo/README.md) | [Kiina (perinteinen, Taiwan)](../tw/README.md) | [Kroatia](../hr/README.md) | [Tšekki](../cs/README.md) | [Tanska](../da/README.md) | [Hollanti](../nl/README.md) | [Viro](../et/README.md) | [Suomi](./README.md) | [Ranska](../fr/README.md) | [Saksa](../de/README.md) | [Kreikka](../el/README.md) | [Heprea](../he/README.md) | [Hindi](../hi/README.md) | [Unkari](../hu/README.md) | [Indonesia](../id/README.md) | [Italia](../it/README.md) | [Japani](../ja/README.md) | [Kannada](../kn/README.md) | [Korea](../ko/README.md) | [Liettua](../lt/README.md) | [Malaiji](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerialainen pidgin](../pcm/README.md) | [Norja](../no/README.md) | [Persia (farsi)](../fa/README.md) | [Puola](../pl/README.md) | [Portugali (Brasilia)](../br/README.md) | [Portugali (Portugali)](../pt/README.md) | [Pandžabi (Gurmukhi)](../pa/README.md) | [Romania](../ro/README.md) | [Venäjä](../ru/README.md) | [Serbia (kyrillinen)](../sr/README.md) | [Slovakki](../sk/README.md) | [Sloveeni](../sl/README.md) | [Espanja](../es/README.md) | [Swahili](../sw/README.md) | [Ruotsi](../sv/README.md) | [Tagalog (filipino)](../tl/README.md) | [Tamili](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkki](../tr/README.md) | [Ukraina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnami](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Jos haluat lisätä tukemia käännöskieliä, tuetut kielet on lueteltu [tässä](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

#### Liity yhteisöömme 
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Meillä on käynnissä Discord-sarja Learn with AI, lue lisää ja liity [Learn with AI Series](https://aka.ms/learnwithai/discord) -tapahtumaan 18.–30. syyskuuta 2025. Saat vinkkejä ja niksejä GitHub Copilotin käyttämiseen data-analytiikassa.

![Learn with AI -sarja](../../translated_images/1.2b28cdc6205e26fef6a21817fe5d83ae8b50fbd0a33e9fed0df05845da5b30b6.fi.jpg)

# Oletko opiskelija?

Aloita seuraavista resursseista:

- [Student Hub -sivu](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) Tältä sivulta löydät aloittelijoille suunnattuja resursseja, opiskelijapakkauksia ja jopa tapoja saada ilmainen sertifikaattikuponki. Tämä on sivu, jonka haluat lisätä kirjanmerkkeihin ja tarkistaa aika ajoin, sillä päivitämme sisältöä vähintään kuukausittain.
- [Microsoft Learn Student Ambassadors](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) Liity maailmanlaajuiseen Student Ambassadors -yhteisöön; tämä voi olla sinun tiesi Microsoftiin.

# Aloittaminen

## 📚 Dokumentaatio

- **[Asennusopas](INSTALLATION.md)** - Vaiheittaiset asennusohjeet aloittelijoille
- **[Käyttöopas](USAGE.md)** - Esimerkkejä ja yleisiä työnkulkuja
- **[Vianmääritys](TROUBLESHOOTING.md)** - Ratkaisuja yleisiin ongelmiin
- **[Osallistumisopas](CONTRIBUTING.md)** - Ohjeet projektin kehittämiseen
- **[Opettajille](for-teachers.md)** - Opetusohjeet ja luokkahuoneresurssit

## 👨‍🎓 Opiskelijoille
> **Täysin aloittelijat**: Uusi data-analytiikassa? Aloita [aloittelijaystävällisistä esimerkeistämme](examples/README.md)! Nämä yksinkertaiset, hyvin kommentoidut esimerkit auttavat sinua ymmärtämään perusteet ennen kuin sukellat koko opetussuunnitelmaan.
> **[Opiskelijat](https://aka.ms/student-page)**: käyttääksesi tätä opetussuunnitelmaa itsenäisesti, tee fork koko repositoriosta ja tee harjoitukset itse aloittaen ennakkokokeella. Lue sitten luento ja suorita loput aktiviteeteista. Yritä luoda projektit ymmärtämällä oppitunnit sen sijaan, että kopioisit ratkaisukoodia; kyseinen koodi on kuitenkin saatavilla kunkin projektilähtöisen oppitunnin /solutions-kansioissa. Toinen idea on muodostaa opiskeluryhmä ystävien kanssa ja käydä sisältö yhdessä läpi. Jatko-opiskelua varten suosittelemme [Microsoft Learnia](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum).

**Pika-aloitus:**
1. Tarkista [Asennusopas](INSTALLATION.md) asettaaksesi ympäristösi
2. Tutustu [Käyttöoppaaseen](USAGE.md) oppiaksesi miten työskennellä opetussuunnitelman kanssa
3. Aloita Oppitunnista 1 ja etene peräkkäin
4. Liity [Discord-yhteisöömme](https://aka.ms/ds4beginners/discord) saadaksesi tukea

## 👩‍🏫 Opettajille

> **Opettajat**: olemme [sisällyttäneet joitakin ehdotuksia](for-teachers.md) siitä, miten käyttää tätä opetussuunnitelmaa. Haluaisimme kuulla palautteesi [keskustelufoorumillamme](https://github.com/microsoft/Data-Science-For-Beginners/discussions)!

## Tutustu tiimiin

[![Esittelyvideo](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "Esittelyvideo")

**Gif tekijä** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)
> 🎥 Klikkaa yllä olevaa kuvaa nähdäksesi videon projektista ja ihmisistä, jotka sen loivat!

## Pedagogiikka

Olemme valinneet kaksi opetuksellista periaatetta rakentaessamme tätä opetussuunnitelmaa: sen tulee olla projektipohjainen ja sen tulee sisältää usein toistuvia tietokilpailuja. Tämän sarjan loppuun mennessä opiskelijat ovat oppineet datatieteen perusperiaatteet, mukaan lukien eettiset käsitteet, datan valmistelun, erilaiset tavat työskennellä datan kanssa, datan visualisoinnin, data-analyysin, datatieteen käytännön käyttötapaukset ja muuta.

Lisäksi vähän panoksia vaativa ennakkotesti ennen tuntia suuntaa opiskelijan aikomusta oppia aihetta, ja toinen testi tunnin jälkeen varmistaa paremman muistamisen. Tämä opetussuunnitelma on suunniteltu joustavaksi ja hauskaksi, ja sen voi suorittaa kokonaan tai osittain. Projektit alkavat pienestä ja monimutkaistuvat vähitellen 10 viikon jakson loppuun mennessä.

> Löydät [käyttäytymisohjeemme](CODE_OF_CONDUCT.md), [ohjeet osallistumiseen](CONTRIBUTING.md), [käännösohjeet](TRANSLATIONS.md). Otamme mielellämme vastaan rakentavaa palautettasi!

## Jokainen oppitunti sisältää:

- Valinnainen sketchnote
- Valinnainen lisävideo
- Lämmittelykysely ennen oppituntia
- Kirjallinen oppitunti
- Projektipohjaisissa oppitunneissa vaiheittaiset ohjeet projektin rakentamiseen
- Tiedon tarkistuksia
- Haaste
- Lisälukemisto
- Tehtävä
- [Oppitunnin jälkeinen tietokilpailu](https://ff-quizzes.netlify.app/en/)

> **Huomio tietokilpailuista**: Kaikki tietokilpailut ovat Quiz-App-kansiossa, yhteensä 40 tietokilpailua, joissa jokaisessa on kolme kysymystä. Ne linkitetään oppitunneista, mutta tietokilpailusovellusta voi ajaa paikallisesti tai ottaa käyttöön Azureen; noudata ohjeita `quiz-app`-kansiossa. Niitä lokalisoidaan vähitellen.

## 🎓 Aloittelijaystävälliset esimerkit

**Uusi datatieteessä?** Olemme luoneet erityisen [esimerkkihakemiston](examples/README.md), jossa on yksinkertaista ja hyvin kommentoitua koodia auttamaan sinut alkuun:

- 🌟 **Hello World** - Ensimmäinen datatieteen ohjelmasi
- 📂 **Loading Data** - Opi lukemaan ja tutkimaan aineistoja
- 📊 **Simple Analysis** - Laske tilastot ja etsi kuvioita
- 📈 **Basic Visualization** - Luo kaavioita ja graafeja
- 🔬 **Real-World Project** - Kokonainen työnkulku alusta loppuun

Jokainen esimerkki sisältää yksityiskohtaiset kommentit, jotka selittävät jokaisen vaiheen, joten ne sopivat erinomaisesti täysin aloitteleville!

👉 **[Aloita esimerkeistä](examples/README.md)** 👈

## Oppitunnit


|![ Sketchnote tekijä @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Roadmap.4905d6567dff47532b9bfb8e0b8980fc6b0b1292eebb24181c1a9753b33bc0f5.fi.png)|
|:---:|
| Datatiede aloittelijoille: tiekartta - _Sketchnote tekijä [@nitya](https://twitter.com/nitya)_ |


| Oppitunnin numero | Aihe | Oppitunnin ryhmittely | Oppimistavoitteet | Liitetty oppitunti | Tekijä |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | Datatieteen määrittely | [Johdanto](1-Introduction/README.md) | Opit datatieteen peruskäsitteet ja miten se liittyy tekoälyyn, koneoppimiseen ja big dataan. | [oppitunti](1-Introduction/01-defining-data-science/README.md) [video](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | Datatieteen etiikka | [Johdanto](1-Introduction/README.md) | Datan eettiset käsitteet, haasteet ja viitekehykset. | [oppitunti](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | Datan määrittely | [Johdanto](1-Introduction/README.md) | Miten data luokitellaan ja sen yleisimmät lähteet. | [oppitunti](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | Johdatus tilastotieteeseen ja todennäköisyyslaskentaan | [Johdanto](1-Introduction/README.md) | Todennäköisyys- ja tilastolliset matemaattiset menetelmät datan ymmärtämiseen. | [oppitunti](1-Introduction/04-stats-and-probability/README.md) [video](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | Relaatiotietojen käsittely | [Tietojen käsittely](2-Working-With-Data/README.md) | Johdatus relaatiotietoihin ja perusteet relaatiotietojen tutkimisesta ja analysoinnista käyttäen Structured Query Languagea, joka tunnetaan myös nimellä SQL (lausutaan “see-quell”). | [oppitunti](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | NoSQL-datan käsittely | [Tietojen käsittely](2-Working-With-Data/README.md) | Johdatus ei-relaatiotyyppiseen dataan, sen eri tyyppeihin ja perusteet dokumenttitietokantojen tutkimisesta ja analysoinnista. | [oppitunti](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | Pythonin käyttö | [Tietojen käsittely](2-Working-With-Data/README.md) | Perusteet Pythonin käytöstä datan tutkimiseen kirjastoilla kuten Pandas. Suositellaan perustavaa ymmärrystä Python-ohjelmoinnista. | [oppitunti](2-Working-With-Data/07-python/README.md) [video](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | Datan valmistelu | [Tietojen käsittely](2-Working-With-Data/README.md) | Aiheita datan puhdistuksesta ja muokkaamisesta, jotta voidaan käsitellä puuttuvaa, virheellistä tai epätäydellistä dataa. | [oppitunti](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | Määrien visualisointi | [Datan visualisointi](3-Data-Visualization/README.md) | Opi käyttämään Matplotlibia lintudatan visualisointiin 🦆 | [oppitunti](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | Datan jakaumien visualisointi | [Datan visualisointi](3-Data-Visualization/README.md) | Havaintojen ja trendien visualisointi tietyllä välillä. | [oppitunti](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | Prosenttiosuuksien visualisointi | [Datan visualisointi](3-Data-Visualization/README.md) | Diskreettisten ja ryhmiteltyjen prosenttiosuuksien visualisointi. | [oppitunti](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | Suhteiden visualisointi | [Datan visualisointi](3-Data-Visualization/README.md) | Yhdistysten ja korrelaatioiden visualisointi datakokonaisuuksien ja niiden muuttujien välillä. | [oppitunti](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | Merkitykselliset visualisoinnit | [Datan visualisointi](3-Data-Visualization/README.md) | Tekniikoita ja ohjeita, joiden avulla visualisoinneistasi tulee arvokkaita ongelmanratkaisulle ja oivalluksille. | [oppitunti](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | Johdatus datatieteen elinkaareen | [Elinkaari](4-Data-Science-Lifecycle/README.md) | Johdatus datatieteen elinkaareen ja sen ensimmäiseen vaiheeseen, datan hankintaan ja poimintaan. | [oppitunti](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | Analysointi | [Elinkaari](4-Data-Science-Lifecycle/README.md) | Tämä vaihe datatieteen elinkaaressa keskittyy datan analysointimenetelmiin. | [oppitunti](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | Viestintä | [Elinkaari](4-Data-Science-Lifecycle/README.md) | Tämä vaihe keskittyy esittämään datasta saadut oivallukset siten, että päätöksentekijöiden on helpompi ymmärtää ne. | [oppitunti](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | Datatiede pilvessä | [Pilvidata](5-Data-Science-In-Cloud/README.md) | Tämä oppituntisarja esittelee datatiedettä pilvessä ja sen hyödyt. | [oppitunti](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 18 | Datatiede pilvessä | [Pilvidata](5-Data-Science-In-Cloud/README.md) | Mallien kouluttaminen matalakoodityökaluilla. |[oppitunti](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 19 | Datatiede pilvessä | [Pilvidata](5-Data-Science-In-Cloud/README.md) | Mallien käyttöönotto Azure Machine Learning Studion avulla. | [oppitunti](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 20 | Datatiede käytännössä | [Käytännön esimerkit](6-Data-Science-In-Wild/README.md) | Datatieteen ohjaamat projektit tosielämässä. | [oppitunti](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

Follow these steps to open this sample in a Codespace:
1. Klikkaa Code-pudotusvalikkoa ja valitse Open with Codespaces -vaihtoehto.
2. Valitse + New codespace paneelin alareunasta.
For more info, check out the [GitHub documentation](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace).

## VSCode Remote - Containers
Follow these steps to open this repo in a container using your local machine and VSCode using  the VS Code Remote - Containers extension:

1. If this is your first time using a development container, please ensure your system meets the pre-reqs (i.e. have Docker installed) in [aloitusohjeet](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started).

To use this repository, you can either open the repository in an isolated Docker volume:

**Huom**: Under the hood, this will use the Remote-Containers: **Clone Repository in Container Volume...** command to clone the source code in a Docker volume instead of the local filesystem. [Volumes](https://docs.docker.com/storage/volumes/) are the preferred mechanism for persisting container data.

Or open a locally cloned or downloaded version of the repository:

- Kloonaa tämä repositorio paikalliselle tiedostojärjestelmällesi.
- Paina F1 ja valitse **Remote-Containers: Open Folder in Container...** -komento.
- Valitse kloonattu kopio tästä kansiosta, odota että kontti käynnistyy, ja kokeile sitten.

## Offline access

Voit ajaa tämän dokumentaation offline-tilassa käyttämällä [Docsify](https://docsify.js.org/#/). Forkkaa tämä repositorio, asenna [Docsify](https://docsify.js.org/#/quickstart) paikalliselle koneellesi, sitten tämän repositorion juurikansiossa suorita `docsify serve`. Sivusto palvellaan portissa 3000 osoitteessa `localhost:3000`.

> Huomio: Notebookit eivät renderöidy Docsifyn kautta, joten kun sinun täytyy ajaa notebook, tee se erikseen VS Codessa Python-ytimen kanssa.

## Muut opetussuunnitelmat

Tiimimme tuottaa myös muita opetussuunnitelmia! Tutustu:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD aloittelijoille](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI aloittelijoille](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP aloittelijoille](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI-agentit aloittelijoille](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatiivinen tekoäly -sarja
[![Generatiivinen tekoäly aloittelijoille](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatiivinen tekoäly (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatiivinen tekoäly (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatiivinen tekoäly (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Perusopinnot
[![Koneoppiminen aloittelijoille](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Datatiede aloittelijoille](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![Tekoäly aloittelijoille](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kyberturvallisuus aloittelijoille](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Verkkokehitys aloittelijoille](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT aloittelijoille](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR-kehitys aloittelijoille](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot-sarja
[![Copilot tekoälypariohjelmointiin](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET -kehittäjille](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot-seikkailu](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Apua

**Koetko ongelmia?** Katso [Vianmääritysopas](TROUBLESHOOTING.md) yleisten ongelmien ratkaisuja varten.

Jos juutut tai sinulla on kysymyksiä tekoälysovellusten rakentamisesta, liity MCP:n keskusteluihin muiden oppijoiden ja kokeneiden kehittäjien kanssa. Se on kannustava yhteisö, jossa kysymyksiä saa esittää ja tietoa jaetaan vapaasti.

[![Microsoft Foundry -Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jos sinulla on tuotepalautetta tai kohtaat virheitä kehityksen aikana, vieraile:

[![Microsoft Foundry -kehittäjäfoorumi](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vastuuvapauslauseke:
Tämä asiakirja on käännetty tekoälykäännöspalvelulla Co-op Translator (https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää määräävänä lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->