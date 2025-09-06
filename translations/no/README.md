<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5443b88ba402d2ec7b000e4de6cecb8",
  "translation_date": "2025-08-29T10:02:52+00:00",
  "source_file": "README.md",
  "language_code": "no"
}
-->
# Data Science for Nybegynnere - En Læreplan

Azure Cloud Advocates hos Microsoft er glade for å tilby en 10-ukers, 20-leksjons læreplan om Data Science. Hver leksjon inkluderer quiz før og etter leksjonen, skriftlige instruksjoner for å fullføre leksjonen, en løsning og en oppgave. Vår prosjektbaserte pedagogikk lar deg lære mens du bygger, en velprøvd metode for å få nye ferdigheter til å "sitte fast".

**En stor takk til våre forfattere:** [Jasmine Greenaway](https://www.twitter.com/paladique), [Dmitry Soshnikov](http://soshnikov.com), [Nitya Narasimhan](https://twitter.com/nitya), [Jalen McGee](https://twitter.com/JalenMcG), [Jen Looper](https://twitter.com/jenlooper), [Maud Levy](https://twitter.com/maudstweets), [Tiffany Souterre](https://twitter.com/TiffanySouterre), [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏 Spesiell takk 🙏 til våre [Microsoft Student Ambassador](https://studentambassadors.microsoft.com/) forfattere, anmeldere og innholdsbidragsytere,** spesielt Aaryan Arora, [Aditya Garg](https://github.com/AdityaGarg00), [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/), [Ankita Singh](https://www.linkedin.com/in/ankitasingh007), [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/), [Arpita Das](https://www.linkedin.com/in/arpitadas01/), ChhailBihari Dubey, [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor), [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [Majd Safi](https://www.linkedin.com/in/majd-s/), [Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/), [Miguel Correa](https://www.linkedin.com/in/miguelmque/), [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119), [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum), [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/), [Rohit Yadav](https://www.linkedin.com/in/rty2423), Samridhi Sharma, [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200),
[Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/), [Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/), Yogendrasingh Pawar, [Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/), [Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![Sketchnote av @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.no.png)|
|:---:|
| Data Science for Nybegynnere - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

### 🌐 Flerspråklig støtte

#### Støttet via GitHub Action (Automatisk og alltid oppdatert)

[Fransk](../fr/README.md) | [Spansk](../es/README.md) | [Tysk](../de/README.md) | [Russisk](../ru/README.md) | [Arabisk](../ar/README.md) | [Persisk (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Kinesisk (Forenklet)](../zh/README.md) | [Kinesisk (Tradisjonell, Macau)](../mo/README.md) | [Kinesisk (Tradisjonell, Hong Kong)](../hk/README.md) | [Kinesisk (Tradisjonell, Taiwan)](../tw/README.md) | [Japansk](../ja/README.md) | [Koreansk](../ko/README.md) | [Hindi](../hi/README.md) | [Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portugisisk (Portugal)](../pt/README.md) | [Portugisisk (Brasil)](../br/README.md) | [Italiensk](../it/README.md) | [Polsk](../pl/README.md) | [Tyrkisk](../tr/README.md) | [Gresk](../el/README.md) | [Thai](../th/README.md) | [Svensk](../sv/README.md) | [Dansk](../da/README.md) | [Norsk](./README.md) | [Finsk](../fi/README.md) | [Nederlandsk](../nl/README.md) | [Hebraisk](../he/README.md) | [Vietnamesisk](../vi/README.md) | [Indonesisk](../id/README.md) | [Malayisk](../ms/README.md) | [Tagalog (Filippinsk)](../tl/README.md) | [Swahili](../sw/README.md) | [Ungarsk](../hu/README.md) | [Tsjekkisk](../cs/README.md) | [Slovakisk](../sk/README.md) | [Rumensk](../ro/README.md) | [Bulgarsk](../bg/README.md) | [Serbisk (Kyrillisk)](../sr/README.md) | [Kroatisk](../hr/README.md) | [Slovensk](../sl/README.md) | [Ukrainsk](../uk/README.md) | [Burmesisk (Myanmar)](../my/README.md)

**Hvis du ønsker å få støtte for flere oversettelser, finner du språkene som støttes [her](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

#### Bli med i vårt fellesskap 
[![Azure AI Discord](https://dcbadge.limes.pink/api/server/kzRShWzttr)](https://discord.gg/kzRShWzttr)

# Er du student?

Kom i gang med følgende ressurser:

- [Student Hub-side](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) På denne siden finner du ressurser for nybegynnere, studentpakker og til og med måter å få en gratis sertifikatkupong. Dette er en side du bør bokmerke og sjekke fra tid til annen, da vi bytter ut innhold minst månedlig.
- [Microsoft Learn Student Ambassadors](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) Bli med i et globalt fellesskap av studentambassadører, dette kan være din vei inn i Microsoft.

# Kom i gang

> **Lærere**: vi har [inkludert noen forslag](for-teachers.md) om hvordan du kan bruke denne læreplanen. Vi vil gjerne ha tilbakemeldingen din [i vårt diskusjonsforum](https://github.com/microsoft/Data-Science-For-Beginners/discussions)!

> **[Studenter](https://aka.ms/student-page)**: for å bruke denne læreplanen på egen hånd, fork hele repoet og fullfør oppgavene på egen hånd, start med en quiz før leksjonen. Les deretter leksjonen og fullfør resten av aktivitetene. Prøv å lage prosjektene ved å forstå leksjonene i stedet for å kopiere løsningskoden; denne koden er imidlertid tilgjengelig i /solutions-mappene i hver prosjektorienterte leksjon. Et annet forslag er å danne en studiegruppe med venner og gå gjennom innholdet sammen. For videre studier anbefaler vi [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum).

## Møt teamet

[![Promo-video](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "Promo-video")

**Gif av** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)

> 🎥 Klikk på bildet over for en video om prosjektet og menneskene som skapte det!

## Pedagogikk

Vi har valgt to pedagogiske prinsipper mens vi utviklet denne læreplanen: å sikre at den er prosjektbasert og at den inkluderer hyppige quizer. Ved slutten av denne serien vil studentene ha lært grunnleggende prinsipper for data science, inkludert etiske konsepter, datatilrettelegging, ulike måter å jobbe med data på, datavisualisering, dataanalyse, virkelige bruksområder for data science og mer.

I tillegg setter en lavterskelquiz før en klasse studentens intensjon mot å lære et emne, mens en andre quiz etter klassen sikrer ytterligere læring. Denne læreplanen er designet for å være fleksibel og morsom og kan tas i sin helhet eller delvis. Prosjektene starter små og blir stadig mer komplekse mot slutten av den 10-ukers syklusen.
> Finn våre retningslinjer for [Code of Conduct](CODE_OF_CONDUCT.md), [Contributing](CONTRIBUTING.md), [Translation](TRANSLATIONS.md). Vi setter pris på din konstruktive tilbakemelding!
## Hver leksjon inkluderer:

- Valgfri sketchnote
- Valgfri tilleggsvideo
- Oppvarmingsquiz før leksjonen
- Skriftlig leksjon
- For prosjektbaserte leksjoner, trinnvise guider for hvordan man bygger prosjektet
- Kunnskapssjekker
- En utfordring
- Tilleggslesing
- Oppgave
- [Quiz etter leksjonen](https://ff-quizzes.netlify.app/en/)

> **En merknad om quizer**: Alle quizer finnes i Quiz-App-mappen, totalt 40 quizer med tre spørsmål hver. De er lenket fra leksjonene, men quiz-appen kan kjøres lokalt eller distribueres til Azure; følg instruksjonene i `quiz-app`-mappen. De blir gradvis lokalisert.

## Leksjoner

|![ Sketchnote av @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Roadmap.4905d6567dff47532b9bfb8e0b8980fc6b0b1292eebb24181c1a9753b33bc0f5.no.png)|
|:---:|
| Data Science for Nybegynnere: Veikart - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

| Leksjonsnummer | Tema | Leksjonsgruppe | Læringsmål | Lenket leksjon | Forfatter |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | Definere Data Science | [Introduksjon](1-Introduction/README.md) | Lær de grunnleggende konseptene bak data science og hvordan det er relatert til kunstig intelligens, maskinlæring og big data. | [leksjon](1-Introduction/01-defining-data-science/README.md) [video](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | Data Science Etikk | [Introduksjon](1-Introduction/README.md) | Konsepter, utfordringer og rammeverk for dataetikk. | [leksjon](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | Definere Data | [Introduksjon](1-Introduction/README.md) | Hvordan data klassifiseres og vanlige kilder til data. | [leksjon](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | Introduksjon til Statistikk og Sannsynlighet | [Introduksjon](1-Introduction/README.md) | De matematiske teknikkene for sannsynlighet og statistikk for å forstå data. | [leksjon](1-Introduction/04-stats-and-probability/README.md) [video](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | Arbeide med Relasjonelle Data | [Arbeide med Data](2-Working-With-Data/README.md) | Introduksjon til relasjonelle data og grunnleggende utforsking og analyse av relasjonelle data med Structured Query Language, også kjent som SQL (uttales "see-quell"). | [leksjon](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | Arbeide med NoSQL Data | [Arbeide med Data](2-Working-With-Data/README.md) | Introduksjon til ikke-relasjonelle data, deres ulike typer og grunnleggende utforsking og analyse av dokumentdatabaser. | [leksjon](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | Arbeide med Python | [Arbeide med Data](2-Working-With-Data/README.md) | Grunnleggende bruk av Python for datautforsking med biblioteker som Pandas. Grunnleggende forståelse av Python-programmering anbefales. | [leksjon](2-Working-With-Data/07-python/README.md) [video](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | Datapreparering | [Arbeide med Data](2-Working-With-Data/README.md) | Temaer om teknikker for å rense og transformere data for å håndtere utfordringer med manglende, unøyaktige eller ufullstendige data. | [leksjon](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | Visualisere Mengder | [Datavisualisering](3-Data-Visualization/README.md) | Lær hvordan du bruker Matplotlib til å visualisere fugledata 🦆 | [leksjon](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | Visualisere Datafordelinger | [Datavisualisering](3-Data-Visualization/README.md) | Visualisere observasjoner og trender innenfor et intervall. | [leksjon](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | Visualisere Prosentandeler | [Datavisualisering](3-Data-Visualization/README.md) | Visualisere diskrete og grupperte prosentandeler. | [leksjon](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | Visualisere Relasjoner | [Datavisualisering](3-Data-Visualization/README.md) | Visualisere forbindelser og korrelasjoner mellom datasett og deres variabler. | [leksjon](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | Meningsfulle Visualiseringer | [Datavisualisering](3-Data-Visualization/README.md) | Teknikker og veiledning for å gjøre visualiseringene dine verdifulle for effektiv problemløsning og innsikt. | [leksjon](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | Introduksjon til Data Science Livssyklus | [Livssyklus](4-Data-Science-Lifecycle/README.md) | Introduksjon til data science-livssyklusen og dens første steg med å samle og trekke ut data. | [leksjon](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | Analyse | [Livssyklus](4-Data-Science-Lifecycle/README.md) | Denne fasen av data science-livssyklusen fokuserer på teknikker for å analysere data. | [leksjon](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | Kommunikasjon | [Livssyklus](4-Data-Science-Lifecycle/README.md) | Denne fasen av data science-livssyklusen fokuserer på å presentere innsiktene fra data på en måte som gjør det enklere for beslutningstakere å forstå. | [leksjon](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | Data Science i Skyen | [Skydata](5-Data-Science-In-Cloud/README.md) | Denne serien med leksjoner introduserer data science i skyen og fordelene med det. | [leksjon](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) og [Maud](https://twitter.com/maudstweets) |
| 18 | Data Science i Skyen | [Skydata](5-Data-Science-In-Cloud/README.md) | Trening av modeller ved bruk av Low Code-verktøy. |[leksjon](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) og [Maud](https://twitter.com/maudstweets) |
| 19 | Data Science i Skyen | [Skydata](5-Data-Science-In-Cloud/README.md) | Distribuering av modeller med Azure Machine Learning Studio. | [leksjon](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) og [Maud](https://twitter.com/maudstweets) |
| 20 | Data Science i Felten | [I Felten](6-Data-Science-In-Wild/README.md) | Prosjekter drevet av data science i den virkelige verden. | [leksjon](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

Følg disse trinnene for å åpne dette eksempelet i en Codespace:
1. Klikk på Code-rullegardinmenyen og velg alternativet Open with Codespaces.
2. Velg + New codespace nederst i panelet.
For mer informasjon, sjekk ut [GitHub-dokumentasjonen](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace).

## VSCode Remote - Containers
Følg disse trinnene for å åpne dette repoet i en container ved bruk av din lokale maskin og VSCode med VS Code Remote - Containers-utvidelsen:

1. Hvis dette er første gang du bruker en utviklingscontainer, sørg for at systemet ditt oppfyller kravene (f.eks. har Docker installert) i [komme i gang-dokumentasjonen](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started).

For å bruke dette repoet kan du enten åpne det i et isolert Docker-volum:

**Merk**: Under panseret vil dette bruke Remote-Containers: **Clone Repository in Container Volume...**-kommandoen for å klone kildekoden i et Docker-volum i stedet for det lokale filsystemet. [Volumer](https://docs.docker.com/storage/volumes/) er den foretrukne mekanismen for å vedvare containerdata.

Eller åpne en lokalt klonet eller nedlastet versjon av repoet:

- Klon dette repoet til ditt lokale filsystem.
- Trykk F1 og velg **Remote-Containers: Open Folder in Container...**-kommandoen.
- Velg den klonede kopien av denne mappen, vent til containeren starter, og prøv ting ut.

## Offline tilgang

Du kan kjøre denne dokumentasjonen offline ved å bruke [Docsify](https://docsify.js.org/#/). Fork dette repoet, [installer Docsify](https://docsify.js.org/#/quickstart) på din lokale maskin, og i rotmappen til dette repoet, skriv `docsify serve`. Nettstedet vil bli servert på port 3000 på din localhost: `localhost:3000`.

> Merk, notatbøker vil ikke bli gjengitt via Docsify, så når du trenger å kjøre en notatbok, gjør det separat i VS Code som kjører en Python-kjerne.

## Andre Læreplaner

Vårt team produserer andre læreplaner! Sjekk ut:

- [Generativ AI for Nybegynnere](https://aka.ms/genai-beginners)
- [Generativ AI for Nybegynnere .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generativ AI med JavaScript](https://github.com/microsoft/generative-ai-with-javascript)
- [Generativ AI med Java](https://aka.ms/genaijava)
- [AI for Nybegynnere](https://aka.ms/ai-beginners)
- [Data Science for Nybegynnere](https://aka.ms/datascience-beginners)
- [ML for Nybegynnere](https://aka.ms/ml-beginners)
- [Cybersikkerhet for Nybegynnere](https://github.com/microsoft/Security-101) 
- [Webutvikling for Nybegynnere](https://aka.ms/webdev-beginners)
- [IoT for Nybegynnere](https://aka.ms/iot-beginners)
- [XR-utvikling for Nybegynnere](https://github.com/microsoft/xr-development-for-beginners)
- [Mestring av GitHub Copilot for Parprogrammering](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)
- [Mestring av GitHub Copilot for C#/.NET Utviklere](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers)
- [Velg Ditt Eget Copilot-eventyr](https://github.com/microsoft/CopilotAdventures)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.