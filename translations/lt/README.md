<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7c31d1a22c746b1d0f0582d4f54702ba",
  "translation_date": "2025-12-25T00:39:12+00:00",
  "source_file": "README.md",
  "language_code": "lt"
}
-->
# Duomenų mokslas pradedantiesiems - Mokymo programa

[![Atidaryti GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=344191198)

[![GitHub licencija](https://img.shields.io/github/license/microsoft/Data-Science-For-Beginners.svg)](https://github.com/microsoft/Data-Science-For-Beginners/blob/master/LICENSE)
[![GitHub bendradarbiai](https://img.shields.io/github/contributors/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/graphs/contributors/)
[![GitHub problemos](https://img.shields.io/github/issues/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/issues/)
[![GitHub pull-užklausos](https://img.shields.io/github/issues-pr/microsoft/Data-Science-For-Beginners.svg)](https://GitHub.com/microsoft/Data-Science-For-Beginners/pulls/)
[![PRs laukiami](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub stebėtojai](https://img.shields.io/github/watchers/microsoft/Data-Science-For-Beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/Data-Science-For-Beginners/watchers/)
[![GitHub fork'ai](https://img.shields.io/github/forks/microsoft/Data-Science-For-Beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/Data-Science-For-Beginners/network/)
[![GitHub žvaigždės](https://img.shields.io/github/stars/microsoft/Data-Science-For-Beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/Data-Science-For-Beginners/stargazers/)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Microsoft Foundry kūrėjų forumas](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

Azure Cloud Advocates komanda Microsoft įmonėje džiaugiasi galėdama pasiūlyti 10 savaičių, 20 pamokų mokymo programą apie duomenų mokslą. Kiekvienoje pamokoje yra priešpamokinis ir po-pamokinis testai, rašytinės instrukcijos pamokos atlikimui, sprendimas ir užduotis. Mūsų projektinis pedagoginis požiūris leidžia mokytis kuriant — tai įrodytas būdas, kad nauji įgūdžiai „įsimestų“.

**Nuoširdus ačiū mūsų autoriams:** [Jasmine Greenaway](https://www.twitter.com/paladique), [Dmitry Soshnikov](http://soshnikov.com), [Nitya Narasimhan](https://twitter.com/nitya), [Jalen McGee](https://twitter.com/JalenMcG), [Jen Looper](https://twitter.com/jenlooper), [Maud Levy](https://twitter.com/maudstweets), [Tiffany Souterre](https://twitter.com/TiffanySouterre), [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏 Ypatingas ačiū 🙏 mūsų [Microsoft Student Ambassador](https://studentambassadors.microsoft.com/) autoriams, peržiūrėtojams ir turinio bendradarbiams,** išskirtinai Aaryan Arora, [Aditya Garg](https://github.com/AdityaGarg00), [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/), [Ankita Singh](https://www.linkedin.com/in/ankitasingh007), [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/), [Arpita Das](https://www.linkedin.com/in/arpitadas01/), ChhailBihari Dubey, [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor), [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [Majd Safi](https://www.linkedin.com/in/majd-s/), [Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/), [Miguel Correa](https://www.linkedin.com/in/miguelmque/), [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119), [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum), [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/), [Rohit Yadav](https://www.linkedin.com/in/rty2423), Samridhi Sharma, [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200),
[Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/), [Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/), Yogendrasingh Pawar , [Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/), [Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![Sketchnote autorius @sketchthedocs https://sketchthedocs.dev](../../translated_images/lt/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.png)|
|:---:|
| Duomenų mokslas pradedantiesiems - _Sketchnote autorius [@nitya](https://twitter.com/nitya)_ |

### 🌐 Daugiakalbė parama

#### Remiama per GitHub Action (automatizuota ir visada atnaujinama)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](./README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Jei norite, kad būtų palaikomos papildomos kalbos, palaikomos kalbos išvardytos [čia](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

#### Prisijunkite prie mūsų bendruomenės 
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Mes rengiame Discord „Mokymasis su DI“ seriją — sužinokite daugiau ir prisijunkite prie mūsų [Mokymasis su DI serijos](https://aka.ms/learnwithai/discord) renginio nuo 2025 m. rugsėjo 18 d. iki 30 d. Gavę patarimų ir gudrybių, kaip naudoti GitHub Copilot Duomenų mokslui.

![Mokymasis su DI serija](../../translated_images/lt/1.2b28cdc6205e26fef6a21817fe5d83ae8b50fbd0a33e9fed0df05845da5b30b6.jpg)

# Ar esi studentas?

Pradėkite nuo šių išteklių:

- [Student Hub page](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) Šiame puslapyje rasite pradedantiesiems skirtus išteklius, studentų paketus ir net būdus gauti nemokamą sertifikato kuponą. Tai puslapis, kurį verta pažymėti ir tikrinti laikas nuo laiko, nes mes atnaujiname turinį bent kartą per mėnesį.
- [Microsoft Learn Student Ambassadors](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) Prisijunkite prie pasaulinės studentų ambasadorių bendruomenės — tai gali būti jūsų kelias į Microsoft.

# Kaip pradėti

## 📚 Dokumentacija

- **[Įdiegimo vadovas](INSTALLATION.md)** - Žingsnis po žingsnio nustatymo instrukcijos pradedantiesiems
- **[Naudojimo vadovas](USAGE.md)** - Pavyzdžiai ir įprasti darbo srautai
- **[Trikčių šalinimas](TROUBLESHOOTING.md)** - Sprendimai dažnoms problemoms
- **[Kaip prisidėti](CONTRIBUTING.md)** - Kaip prisidėti prie šio projekto
- **[Mokytojams](for-teachers.md)** - Mokymo gairės ir klasės ištekliai

## 👨‍🎓 Studentams
> **Visiškai pradedantiesiems**: Naujas duomenų moksle? Pradėkite nuo mūsų [pradedantiesiems draugiškų pavyzdžių](examples/README.md)! Šie paprasti, gerai paaiškinti pavyzdžiai padės suprasti pagrindus prieš imantis visos mokymo programos.
> **[Studentai](https://aka.ms/student-page)**: kad naudotumėte šią mokymo programą savarankiškai, fork'inkite visą repozitoriją ir atlikite užduotis savarankiškai, pradėdami nuo priešpaskaitinio testo. Tuomet perskaitykite paskaitą ir atlikite likusias veiklas. Stenkitės kurti projektus suprasdami pamokas, o ne kopijuodami sprendimo kodą; vis dėlto tas kodas yra prieinamas kiekvienos projekto orientuotos pamokos /solutions aplankuose. Kita idėja — suformuoti studijų grupę su draugais ir kartu peržiūrėti turinį. Tolimesniam mokymuisi rekomenduojame [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum).

**Greitas pradėjimas:**
1. Peržiūrėkite [Įdiegimo vadovą](INSTALLATION.md) norėdami paruošti savo aplinką
2. Peržiūrėkite [Naudojimo vadovą](USAGE.md), kad sužinotumėte, kaip dirbti su mokymo programa
3. Pradėkite nuo 1 pamokos ir dirbkite paeiliui
4. Prisijunkite prie mūsų [Discord bendruomenės](https://aka.ms/ds4beginners/discord) dėl pagalbos

## 👩‍🏫 Mokytojams

> **Mokytojams**: mes [įtraukėme keletą pasiūlymų](for-teachers.md), kaip naudoti šią mokymo programą. Laukiame jūsų atsiliepimų [mūsų diskusijų forume](https://github.com/microsoft/Data-Science-For-Beginners/discussions)!

## Susipažinkite su komanda

[![Reklaminis vaizdo įrašas](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "Reklaminis vaizdo įrašas")

**Gif autorius** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)
> 🎥 Spustelėkite aukščiau esantį vaizdą, kad peržiūrėtumėte vaizdo įrašą apie projektą ir žmones, kurie jį sukūrė!

## Pedagogika

Mes pasirinkome dvi pedagogines nuostatas kurdami šią mokymo programą: užtikrinti, kad ji būtų projektu grįsta, ir kad joje būtų dažnos viktorinos. Iki šios serijos pabaigos studentai išmoks pagrindinius duomenų mokslo principus, įskaitant etikos sąvokas, duomenų paruošimą, skirtingus būdus dirbti su duomenimis, duomenų vizualizavimą, duomenų analizę, realaus pasaulio duomenų mokslo taikymus ir dar daugiau.

Be to, mažos rizikos viktorina prieš pamoką nukreipia studentą į temos mokymąsi, o antra viktorina po pamokos užtikrina geresnį įsisavinimą. Ši mokymo programa sukurta taip, kad būtų lanksčią ir linksmą, ją galima atlikti visą arba dalimis. Projektai prasideda nuo mažų užduočių ir pamažu tampa sudėtingesni per 10 savaičių ciklą.

> Raskite mūsų [Elgesio taisykles](CODE_OF_CONDUCT.md), [Prisidėjimo](CONTRIBUTING.md),  [Vertimo](TRANSLATIONS.md) gaires. Laukiame jūsų konstruktyvaus atsiliepimo!

## Kiekviena pamoka apima:

- Pasirenkama sketchnote
- Pasirinktinė papildoma vaizdo medžiaga
- Įžanginė viktorina prieš pamoką
- Rašytinė pamoka
- Projektinėms pamokoms — žingsnis po žingsnio vadovai, kaip sukurti projektą
- Žinių tikrinimai
- Iššūkis
- Papildomas skaitymas
- Užduotis
- [Viktorina po pamokos](https://ff-quizzes.netlify.app/en/)

> **Pastaba apie viktorinas**: Visos viktorinos yra Quiz-App kataloge; iš viso yra 40 viktorinų po tris klausimus kiekvienoje. Jos yra susietos pamokose, tačiau viktorinų programėlę galima paleisti vietoje arba diegti į Azure; vadovaukitės nurodymais `quiz-app` kataloge. Jos palaipsniui lokalizuojamos.

## 🎓 Pradedantiesiems draugiški pavyzdžiai

**Naujokas duomenų mokslui?** Mes sukūrėme specialų [pavyzdžių katalogą](examples/README.md) su paprastu, gerai komentuotu kodu, kad padėtume jums pradėti:

- 🌟 **Hello World** - Jūsų pirmoji duomenų mokslo programa
- 📂 **Loading Data** - Išmokite skaityti ir tyrinėti duomenų rinkinius
- 📊 **Simple Analysis** - Apskaičiuokite statistiką ir raskite dėsningumus
- 📈 **Basic Visualization** - Kurkite diagramas ir grafikus
- 🔬 **Real-World Project** - Pilnas darbo eiga nuo pradžios iki pabaigos

Kiekvienas pavyzdys turi išsamius komentarus, paaiškinančius kiekvieną žingsnį, todėl jis puikiai tinka visiškiems pradedantiesiems!

👉 **[Pradėkite nuo pavyzdžių](examples/README.md)** 👈

## Pamokos


|![ Sketchnote sukūrė @sketchthedocs https://sketchthedocs.dev](../../translated_images/lt/00-Roadmap.4905d6567dff47532b9bfb8e0b8980fc6b0b1292eebb24181c1a9753b33bc0f5.png)|
|:---:|
| Duomenų mokslas pradedantiesiems: kelio žemėlapis - _Sketchnote sukūrė [@nitya](https://twitter.com/nitya)_ |


| Lesson Number | Topic | Lesson Grouping | Learning Objectives | Linked Lesson | Author |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | Duomenų mokslo apibrėžimas | [Įvadas](1-Introduction/README.md) | Išmokti pagrindines duomenų mokslo sąvokas ir suprasti, kaip jis susijęs su dirbtiniu intelektu, mašininio mokymosi ir didžiųjų duomenų sritimis. | [pamoka](1-Introduction/01-defining-data-science/README.md) [vaizdo įrašas](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | Duomenų mokslo etika | [Įvadas](1-Introduction/README.md) | Duomenų etikos sąvokos, iššūkiai ir gairės. | [pamoka](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | Duomenų apibrėžimas | [Įvadas](1-Introduction/README.md) | Kaip klasifikuojami duomenys ir jų įprasti šaltiniai. | [pamoka](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | Įvadas į statistiką ir tikimybių teoriją | [Įvadas](1-Introduction/README.md) | Matematinės tikimybių ir statistikos technikos duomenų supratimui. | [pamoka](1-Introduction/04-stats-and-probability/README.md) [vaizdo įrašas](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | Darbas su reliaciniais duomenimis | [Darbas su duomenimis](2-Working-With-Data/README.md) | Įvadas į reliacinius duomenis ir pagrindai, kaip tirti ir analizuoti reliacinius duomenis naudojant struktūrizuotą užklausų kalbą, dar žinomą kaip SQL (ištariama „see-quell“). | [pamoka](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | Darbas su NoSQL duomenimis | [Darbas su duomenimis](2-Working-With-Data/README.md) | Įvadas į nereliacinius duomenis, jų įvairius tipus ir pagrindus, kaip tirti ir analizuoti dokumentų duomenų bazes. | [pamoka](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | Darbas su Python | [Darbas su duomenimis](2-Working-With-Data/README.md) | Python naudojimo duomenų tyrimui pagrindai su tokiomis bibliotekomis kaip Pandas. Rekomenduojama turėti pagrindines Python programavimo žinias. | [pamoka](2-Working-With-Data/07-python/README.md) [vaizdo įrašas](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | Duomenų paruošimas | [Darbas su duomenimis](2-Working-With-Data/README.md) | Temos apie duomenų valymo ir transformavimo technikas, skirtas spręsti trūkstamų, netikslių ar nepilnų duomenų problemas. | [pamoka](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | Kiekių vizualizavimas | [Duomenų vizualizacija](3-Data-Visualization/README.md) | Išmokite naudoti Matplotlib paukščių duomenų vizualizavimui 🦆 | [pamoka](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | Duomenų pasiskirstymo vizualizavimas | [Duomenų vizualizacija](3-Data-Visualization/README.md) | Observacijų ir tendencijų vizualizavimas intervale. | [pamoka](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | Proporcijų vizualizavimas | [Duomenų vizualizacija](3-Data-Visualization/README.md) | Diskrečių ir sugrupuotų procentų vizualizavimas. | [pamoka](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | Ryšių vizualizavimas | [Duomenų vizualizacija](3-Data-Visualization/README.md) | Ryšių ir koreliacijų tarp duomenų rinkinių ir jų kintamųjų vizualizavimas. | [pamoka](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | Reikšmingos vizualizacijos | [Duomenų vizualizacija](3-Data-Visualization/README.md) | Technikos ir gairės, kaip padaryti vizualizacijas naudingas efektyviam problemų sprendimui ir įžvalgų gavimui. | [pamoka](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | Įvadas į duomenų mokslo gyvavimo ciklą | [Gyvavimo ciklas](4-Data-Science-Lifecycle/README.md) | Įvadas į duomenų mokslo gyvavimo ciklą ir pirmąjį jo žingsnį — duomenų įsigijimą ir išgavimą. | [pamoka](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | Analizė | [Gyvavimo ciklas](4-Data-Science-Lifecycle/README.md) | Ši duomenų mokslo gyvavimo ciklo fazė orientuota į duomenų analizavimo technikas. | [pamoka](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | Komunikavimas | [Gyvavimo ciklas](4-Data-Science-Lifecycle/README.md) | Ši duomenų mokslo gyvavimo ciklo fazė orientuota į įžvalgų iš duomenų pateikimą taip, kad sprendimus priimantys asmenys lengviau juos suprastų. | [pamoka](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | Duomenų mokslas debesyje | [Duomenys debesyje](5-Data-Science-In-Cloud/README.md) | Ši pamokų serija supažindina su duomenų mokslu debesyje ir jo privalumais. | [pamoka](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 18 | Duomenų mokslas debesyje | [Duomenys debesyje](5-Data-Science-In-Cloud/README.md) | Modelių mokymas naudojant Low Code įrankius. |[pamoka](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 19 | Duomenų mokslas debesyje | [Duomenys debesyje](5-Data-Science-In-Cloud/README.md) | Modelių diegimas naudojant Azure Machine Learning Studio. | [pamoka](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 20 | Duomenų mokslas realiame pasaulyje | [Realiame pasaulyje](6-Data-Science-In-Wild/README.md) | Duomenų mokslo varomos realaus pasaulio projektai. | [pamoka](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

Atlikite šiuos veiksmus, kad atidarytumėte šį pavyzdį Codespace aplinkoje:
1. Spustelėkite išskleidžiamąjį meniu Code ir pasirinkite parinktį Open with Codespaces.
2. Pasirinkite + New codespace apačioje esančiame skydelyje.
Daugiau informacijos rasite [GitHub dokumentacijoje](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace).

## VSCode Remote - Containers
Atlikite šiuos veiksmus, kad atidarytumėte šią saugyklą konteineryje naudodami savo vietinį kompiuterį ir VSCode su VS Code Remote - Containers plėtiniu:

1. Jei pirmą kartą naudojate kūrimo konteinerį, įsitikinkite, kad jūsų sistema atitinka reikalavimus (pvz., yra įdiegtas Docker) žr. [pradžios dokumentaciją](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started).

Norėdami naudoti šią saugyklą, galite atidaryti ją izoliuotame Docker volume:

**Pastaba**: po gaubtu tai naudos komandą Remote-Containers: **Clone Repository in Container Volume...** kad nukopijuotų šaltinio kodą į Docker volume vietoje vietinio failų sistemos. [Volumes](https://docs.docker.com/storage/volumes/) yra pageidaujamas mechanizmas konteinerio duomenims išsaugoti.

Arba atidarykite vietoje nuklonuotą arba atsisiųstą saugyklos kopiją:

- Nuklonuokite šią saugyklą į savo vietinį failų sistemą.
- Paspauskite F1 ir pasirinkite komandą **Remote-Containers: Open Folder in Container...**.
- Pasirinkite nuklonuotą šio aplanko kopiją, palaukite kol konteineris paleis ir išbandykite.

## Offline access

Šią dokumentaciją galite paleisti neprisijungę naudodami [Docsify](https://docsify.js.org/#/). Fork'inkite šią saugyklą, [įdiekite Docsify](https://docsify.js.org/#/quickstart) savo vietiniame kompiuteryje, tada šios saugyklos šakninėje direktorijoje įveskite `docsify serve`. Svetainė bus talpinama 3000 prievade jūsų localhost: `localhost:3000`.

> Pastaba: užrašų knygelės (notebooks) nebus atvaizduojamos per Docsify, todėl kai reikia paleisti užrašų knygelę, darykite tai atskirai VS Code, naudojant Python kernelį.

## Kitos mokymo programos

Mūsų komanda rengia ir kitas mokymo programas! Peržiūrėkite:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD pradedantiesiems](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI pradedantiesiems](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP pradedantiesiems](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI agentai pradedantiesiems](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatyvinio AI serija
[![Generatyvinis AI pradedantiesiems](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatyvinis AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatyvinis AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatyvinis AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Pagrindiniai mokymai
[![Mašininis mokymasis pradedantiesiems](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Duomenų mokslas pradedantiesiems](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI pradedantiesiems](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kibernetinis saugumas pradedantiesiems](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Žiniatinklio kūrimas pradedantiesiems](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![Daiktų internetas pradedantiesiems](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR kūrimas pradedantiesiems](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot serija
[![Copilot AI poriniam programavimui](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot skirtas C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot nuotykiai](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Pagalba

**Susiduriate su problemomis?** Peržiūrėkite mūsų [Trikčių šalinimo vadovą](TROUBLESHOOTING.md), kad rastumėte sprendimus dažniausiai pasitaikančioms problemoms.

Jei įstringate arba turite klausimų apie AI programėlių kūrimą. Prisijunkite prie kitų besimokančiųjų ir patyrusių kūrėjų diskusijose apie MCP. Tai palaikanti bendruomenė, kurioje klausimai yra laukiami, o žinios dalijamos laisvai.

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jei turite atsiliepimų apie produktą arba pastebėjote klaidų kūrimo metu, apsilankykite:

[![Microsoft Foundry kūrėjų forumas](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų arba būti netikslūs. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Esant svarbiai informacijai, rekomenduojamas profesionalaus vertėjo atliktas vertimas. Mes neatsakome už jokius nesusipratimus ar klaidingas interpretacijas, kylančias dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->