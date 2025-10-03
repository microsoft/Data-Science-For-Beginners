<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "53f99070cdd86f228ee65685e3104dec",
  "translation_date": "2025-10-03T10:45:40+00:00",
  "source_file": "README.md",
  "language_code": "sk"
}
-->
# Data Science pre začiatočníkov - Učebné osnovy

Azure Cloud Advocates v Microsoft s radosťou ponúkajú 10-týždňový, 20-lekciový kurz o Data Science. Každá lekcia obsahuje kvízy pred a po lekcii, písomné pokyny na dokončenie lekcie, riešenie a úlohu. Náš projektovo orientovaný prístup vám umožní učiť sa prostredníctvom tvorby, čo je osvedčený spôsob, ako si nové zručnosti lepšie zapamätať.

**Veľká vďaka našim autorom:** [Jasmine Greenaway](https://www.twitter.com/paladique), [Dmitry Soshnikov](http://soshnikov.com), [Nitya Narasimhan](https://twitter.com/nitya), [Jalen McGee](https://twitter.com/JalenMcG), [Jen Looper](https://twitter.com/jenlooper), [Maud Levy](https://twitter.com/maudstweets), [Tiffany Souterre](https://twitter.com/TiffanySouterre), [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏 Špeciálne poďakovanie 🙏 našim [Microsoft Student Ambassador](https://studentambassadors.microsoft.com/) autorom, recenzentom a prispievateľom obsahu,** najmä Aaryan Arora, [Aditya Garg](https://github.com/AdityaGarg00), [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/), [Ankita Singh](https://www.linkedin.com/in/ankitasingh007), [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/), [Arpita Das](https://www.linkedin.com/in/arpitadas01/), ChhailBihari Dubey, [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor), [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [Majd Safi](https://www.linkedin.com/in/majd-s/), [Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/), [Miguel Correa](https://www.linkedin.com/in/miguelmque/), [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119), [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum), [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/), [Rohit Yadav](https://www.linkedin.com/in/rty2423), Samridhi Sharma, [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200),
[Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/), [Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/), Yogendrasingh Pawar , [Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/), [Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![Sketchnote by @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.sk.png)|
|:---:|
| Data Science pre začiatočníkov - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

### 🌐 Podpora viacerých jazykov

#### Podporované prostredníctvom GitHub Action (Automatizované a vždy aktuálne)

[Francúzština](../fr/README.md) | [Španielčina](../es/README.md) | [Nemčina](../de/README.md) | [Ruština](../ru/README.md) | [Arabčina](../ar/README.md) | [Perzština (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Čínština (zjednodušená)](../zh/README.md) | [Čínština (tradičná, Macao)](../mo/README.md) | [Čínština (tradičná, Hongkong)](../hk/README.md) | [Čínština (tradičná, Taiwan)](../tw/README.md) | [Japončina](../ja/README.md) | [Kórejčina](../ko/README.md) | [Hindčina](../hi/README.md) | [Bengálčina](../bn/README.md) | [Maráthčina](../mr/README.md) | [Nepálčina](../ne/README.md) | [Pandžábčina (Gurmukhi)](../pa/README.md) | [Portugalčina (Portugalsko)](../pt/README.md) | [Portugalčina (Brazília)](../br/README.md) | [Taliančina](../it/README.md) | [Poľština](../pl/README.md) | [Turečtina](../tr/README.md) | [Gréčtina](../el/README.md) | [Thajčina](../th/README.md) | [Švédčina](../sv/README.md) | [Dánčina](../da/README.md) | [Nórčina](../no/README.md) | [Fínčina](../fi/README.md) | [Holandčina](../nl/README.md) | [Hebrejčina](../he/README.md) | [Vietnamčina](../vi/README.md) | [Indonézština](../id/README.md) | [Malajčina](../ms/README.md) | [Tagalog (Filipíny)](../tl/README.md) | [Swahilčina](../sw/README.md) | [Maďarčina](../hu/README.md) | [Čeština](../cs/README.md) | [Slovenčina](./README.md) | [Rumunčina](../ro/README.md) | [Bulharčina](../bg/README.md) | [Srbčina (cyrilika)](../sr/README.md) | [Chorvátčina](../hr/README.md) | [Slovinčina](../sl/README.md) | [Ukrajinčina](../uk/README.md) | [Barmčina (Mjanmarsko)](../my/README.md)

**Ak si želáte podporu ďalších jazykov, zoznam podporovaných jazykov nájdete [tu](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

#### Pripojte sa k našej komunite 
[![Azure AI Discord](https://dcbadge.limes.pink/api/server/kzRShWzttr)](https://aka.ms/ds4beginners/discord)

Máme prebiehajúcu sériu Learn with AI na Discorde, dozviete sa viac a pripojte sa k nám na [Learn with AI Series](https://aka.ms/learnwithai/discord) od 18. do 30. septembra 2025. Získate tipy a triky na používanie GitHub Copilot pre Data Science.

![Learn with AI series](../../translated_images/1.2b28cdc6205e26fef6a21817fe5d83ae8b50fbd0a33e9fed0df05845da5b30b6.sk.jpg)

# Ste študent?

Začnite s nasledujúcimi zdrojmi:

- [Stránka Student Hub](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) Na tejto stránke nájdete zdroje pre začiatočníkov, študentské balíčky a dokonca aj spôsoby, ako získať poukaz na certifikát zadarmo. Táto stránka je ideálna na uloženie do záložiek a pravidelné kontrolovanie, pretože obsah meníme minimálne raz mesačne.
- [Microsoft Learn Student Ambassadors](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) Pripojte sa k globálnej komunite študentských ambasádorov, toto môže byť vaša cesta do Microsoftu.

# Začíname

> **Učitelia**: [pridali sme niekoľko návrhov](for-teachers.md) na použitie týchto učebných osnov. Radi by sme získali vašu spätnú väzbu [v našom diskusnom fóre](https://github.com/microsoft/Data-Science-For-Beginners/discussions)!

> **[Študenti](https://aka.ms/student-page)**: ak chcete používať tieto učebné osnovy samostatne, vytvorte si vlastnú kópiu celého repozitára a dokončite cvičenia sami, začnite kvízom pred lekciou. Potom si prečítajte lekciu a dokončite zvyšok aktivít. Pokúste sa vytvoriť projekty pochopením lekcií namiesto kopírovania kódu riešenia; tento kód je však dostupný v priečinkoch /solutions v každej lekcii zameranej na projekt. Ďalším nápadom by bolo vytvoriť študijnú skupinu s priateľmi a prejsť obsah spolu. Pre ďalšie štúdium odporúčame [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum).

## Spoznajte tím

[![Promo video](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "Promo video")

**Gif od** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)

> 🎥 Kliknite na obrázok vyššie pre video o projekte a ľuďoch, ktorí ho vytvorili!

## Pedagogika

Pri tvorbe týchto učebných osnov sme si zvolili dva pedagogické princípy: zabezpečiť, aby boli projektovo orientované a aby obsahovali časté kvízy. Na konci tejto série sa študenti naučia základné princípy data science, vrátane etických konceptov, prípravy dát, rôznych spôsobov práce s dátami, vizualizácie dát, analýzy dát, reálnych prípadov použitia data science a ďalších.

Okrem toho, kvíz s nízkym rizikom pred hodinou nastaví úmysel študenta na učenie sa témy, zatiaľ čo druhý kvíz po hodine zabezpečí lepšie zapamätanie. Tieto učebné osnovy boli navrhnuté tak, aby boli flexibilné a zábavné, a môžu byť absolvované celé alebo čiastočne. Projekty začínajú malé a postupne sa stávajú zložitejšími na konci 10-týždňového cyklu.

> Nájdite náš [Kódex správania](CODE_OF_CONDUCT.md), [Prispievanie](CONTRIBUTING.md), [Preklad](TRANSLATIONS.md) pokyny. Uvítame vašu konštruktívnu spätnú väzbu!

## Každá lekcia obsahuje:

- Voliteľný sketchnote
- Voliteľné doplnkové video
- Kvíz na zahriatie pred lekciou
- Písomnú lekciu
- Pre lekcie zamerané na projekt, podrobné pokyny, ako projekt vytvoriť
- Kontroly vedomostí
- Výzvu
- Doplnkové čítanie
- Úlohu
- [Kvíz po lekcii](https://ff-quizzes.netlify.app/en/)

> **Poznámka o kvízoch**: Všetky kvízy sú obsiahnuté v priečinku Quiz-App, celkovo 40 kvízov po tri otázky. Sú prepojené v rámci lekcií, ale aplikáciu kvízov je možné spustiť lokálne alebo nasadiť na Azure; postupujte podľa pokynov v priečinku `quiz-app`. Postupne sa lokalizujú.

## Lekcie
|![ Sketchnote od @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Roadmap.4905d6567dff47532b9bfb8e0b8980fc6b0b1292eebb24181c1a9753b33bc0f5.sk.png)|
|:---:|
| Data Science pre začiatočníkov: Cestovná mapa - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

| Číslo lekcie | Téma | Skupina lekcií | Ciele učenia | Prepojená lekcia | Autor |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | Definovanie Data Science | [Úvod](1-Introduction/README.md) | Naučte sa základné koncepty Data Science a ako súvisí s umelou inteligenciou, strojovým učením a veľkými dátami. | [lekcia](1-Introduction/01-defining-data-science/README.md) [video](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | Etika v Data Science | [Úvod](1-Introduction/README.md) | Koncepty etiky dát, výzvy a rámce. | [lekcia](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | Definovanie dát | [Úvod](1-Introduction/README.md) | Ako sú dáta klasifikované a ich bežné zdroje. | [lekcia](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | Úvod do štatistiky a pravdepodobnosti | [Úvod](1-Introduction/README.md) | Matematické techniky pravdepodobnosti a štatistiky na pochopenie dát. | [lekcia](1-Introduction/04-stats-and-probability/README.md) [video](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | Práca s relačnými dátami | [Práca s dátami](2-Working-With-Data/README.md) | Úvod do relačných dát a základy skúmania a analýzy relačných dát pomocou Structured Query Language, známeho ako SQL (vyslovuje sa „si-kvel“). | [lekcia](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | Práca s NoSQL dátami | [Práca s dátami](2-Working-With-Data/README.md) | Úvod do nerelačných dát, ich rôznych typov a základy skúmania a analýzy dokumentových databáz. | [lekcia](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | Práca s Pythonom | [Práca s dátami](2-Working-With-Data/README.md) | Základy používania Pythonu na skúmanie dát s knižnicami ako Pandas. Odporúča sa základné pochopenie programovania v Pythone. | [lekcia](2-Working-With-Data/07-python/README.md) [video](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | Príprava dát | [Práca s dátami](2-Working-With-Data/README.md) | Témy o technikách čistenia a transformácie dát na riešenie problémov s chýbajúcimi, nepresnými alebo neúplnými dátami. | [lekcia](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | Vizualizácia množstiev | [Vizualizácia dát](3-Data-Visualization/README.md) | Naučte sa používať Matplotlib na vizualizáciu dát o vtákoch 🦆 | [lekcia](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | Vizualizácia rozdelení dát | [Vizualizácia dát](3-Data-Visualization/README.md) | Vizualizácia pozorovaní a trendov v intervale. | [lekcia](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | Vizualizácia proporcií | [Vizualizácia dát](3-Data-Visualization/README.md) | Vizualizácia diskrétnych a skupinových percentuálnych podielov. | [lekcia](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | Vizualizácia vzťahov | [Vizualizácia dát](3-Data-Visualization/README.md) | Vizualizácia spojení a korelácií medzi súbormi dát a ich premennými. | [lekcia](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | Zmysluplné vizualizácie | [Vizualizácia dát](3-Data-Visualization/README.md) | Techniky a odporúčania na vytváranie vizualizácií, ktoré sú hodnotné pre efektívne riešenie problémov a získavanie poznatkov. | [lekcia](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | Úvod do životného cyklu Data Science | [Životný cyklus](4-Data-Science-Lifecycle/README.md) | Úvod do životného cyklu Data Science a jeho prvého kroku získavania a extrakcie dát. | [lekcia](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | Analýza | [Životný cyklus](4-Data-Science-Lifecycle/README.md) | Táto fáza životného cyklu Data Science sa zameriava na techniky analýzy dát. | [lekcia](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | Komunikácia | [Životný cyklus](4-Data-Science-Lifecycle/README.md) | Táto fáza životného cyklu Data Science sa zameriava na prezentáciu poznatkov z dát spôsobom, ktorý uľahčuje ich pochopenie pre rozhodovateľov. | [lekcia](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | Data Science v cloude | [Cloudové dáta](5-Data-Science-In-Cloud/README.md) | Táto séria lekcií predstavuje Data Science v cloude a jeho výhody. | [lekcia](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) a [Maud](https://twitter.com/maudstweets) |
| 18 | Data Science v cloude | [Cloudové dáta](5-Data-Science-In-Cloud/README.md) | Trénovanie modelov pomocou nástrojov Low Code. |[lekcia](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) a [Maud](https://twitter.com/maudstweets) |
| 19 | Data Science v cloude | [Cloudové dáta](5-Data-Science-In-Cloud/README.md) | Nasadzovanie modelov pomocou Azure Machine Learning Studio. | [lekcia](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) a [Maud](https://twitter.com/maudstweets) |
| 20 | Data Science v praxi | [V praxi](6-Data-Science-In-Wild/README.md) | Projekty riadené Data Science v reálnom svete. | [lekcia](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

Postupujte podľa týchto krokov na otvorenie tejto ukážky v Codespace:
1. Kliknite na rozbaľovacie menu Code a vyberte možnosť Open with Codespaces.
2. Vyberte + New codespace v dolnej časti panela.
Viac informácií nájdete v [dokumentácii GitHub](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace).

## VSCode Remote - Containers
Postupujte podľa týchto krokov na otvorenie tohto repozitára v kontajneri pomocou vášho lokálneho počítača a VSCode s rozšírením VS Code Remote - Containers:

1. Ak je to prvýkrát, čo používate vývojový kontajner, uistite sa, že váš systém spĺňa predpoklady (napr. máte nainštalovaný Docker) v [dokumentácii pre začiatok](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started).

Na použitie tohto repozitára ho môžete otvoriť buď v izolovanom Docker objeme:

**Poznámka**: V zákulisí sa použije príkaz Remote-Containers: **Clone Repository in Container Volume...** na klonovanie zdrojového kódu do Docker objemu namiesto lokálneho súborového systému. [Objemy](https://docs.docker.com/storage/volumes/) sú preferovaným mechanizmom na uchovávanie dát kontajnera.

Alebo otvorte lokálne klonovanú alebo stiahnutú verziu repozitára:

- Klonujte tento repozitár do vášho lokálneho súborového systému.
- Stlačte F1 a vyberte príkaz **Remote-Containers: Open Folder in Container...**.
- Vyberte klonovanú kópiu tohto priečinka, počkajte, kým sa kontajner spustí, a vyskúšajte veci.

## Offline prístup

Túto dokumentáciu môžete spustiť offline pomocou [Docsify](https://docsify.js.org/#/). Forknite tento repozitár, [nainštalujte Docsify](https://docsify.js.org/#/quickstart) na váš lokálny počítač, potom v koreňovom priečinku tohto repozitára zadajte `docsify serve`. Webová stránka bude dostupná na porte 3000 na vašom localhost: `localhost:3000`.

> Poznámka, notebooky nebudú renderované cez Docsify, takže keď potrebujete spustiť notebook, urobte to samostatne vo VS Code s bežiacim Python kernelom.

## Ďalšie učebné osnovy

Náš tím vytvára ďalšie učebné osnovy! Pozrite si:

- [Edge AI pre začiatočníkov](https://aka.ms/edgeai-for-beginners)
- [AI agenti pre začiatočníkov](https://aka.ms/ai-agents-beginners)
- [Generatívna AI pre začiatočníkov](https://aka.ms/genai-beginners)
- [Generatívna AI pre začiatočníkov .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generatívna AI s JavaScriptom](https://github.com/microsoft/generative-ai-with-javascript)
- [Generatívna AI s Javou](https://aka.ms/genaijava)
- [AI pre začiatočníkov](https://aka.ms/ai-beginners)
- [Data Science pre začiatočníkov](https://aka.ms/datascience-beginners)
- [Bash pre začiatočníkov](https://github.com/microsoft/bash-for-beginners)
- [ML pre začiatočníkov](https://aka.ms/ml-beginners)
- [Kybernetická bezpečnosť pre začiatočníkov](https://github.com/microsoft/Security-101) 
- [Webový vývoj pre začiatočníkov](https://aka.ms/webdev-beginners)
- [IoT pre začiatočníkov](https://aka.ms/iot-beginners)
- [Strojové učenie pre začiatočníkov](https://aka.ms/ml-beginners)
- [XR vývoj pre začiatočníkov](https://aka.ms/xr-dev-for-beginners)
- [Ovládnutie GitHub Copilot pre AI párové programovanie](https://aka.ms/GitHubCopilotAI)
- [XR vývoj pre začiatočníkov](https://github.com/microsoft/xr-development-for-beginners)
- [Ovládnutie GitHub Copilot pre C#/.NET vývojárov](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers)
- [Vyberte si vlastné Copilot dobrodružstvo](https://github.com/microsoft/CopilotAdventures)

## Získanie pomoci

Ak sa zaseknete alebo máte akékoľvek otázky o budovaní AI aplikácií, pripojte sa:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Ak máte spätnú väzbu k produktu alebo chyby pri budovaní, navštívte:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.