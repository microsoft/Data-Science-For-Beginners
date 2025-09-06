<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7332da4946897c5885e9ca5bc24de96b",
  "translation_date": "2025-09-06T11:08:22+00:00",
  "source_file": "README.md",
  "language_code": "sk"
}
-->
# Úvod do dátovej vedy - Učebný plán

Azure Cloud Advocates v spoločnosti Microsoft s radosťou ponúkajú 10-týždňový, 20-lekciový učebný plán o dátovej vede. Každá lekcia obsahuje kvízy pred a po lekcii, písomné pokyny na dokončenie lekcie, riešenie a zadanie. Náš prístup založený na projektoch vám umožňuje učiť sa prostredníctvom tvorby, čo je osvedčený spôsob, ako si nové zručnosti lepšie osvojiť.

**Veľká vďaka našim autorom:** [Jasmine Greenaway](https://www.twitter.com/paladique), [Dmitry Soshnikov](http://soshnikov.com), [Nitya Narasimhan](https://twitter.com/nitya), [Jalen McGee](https://twitter.com/JalenMcG), [Jen Looper](https://twitter.com/jenlooper), [Maud Levy](https://twitter.com/maudstweets), [Tiffany Souterre](https://twitter.com/TiffanySouterre), [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏 Špeciálne poďakovanie 🙏 našim [Microsoft Student Ambassador](https://studentambassadors.microsoft.com/) autorom, recenzentom a prispievateľom obsahu,** najmä Aaryanovi Arorovi, [Adityovi Gargovi](https://github.com/AdityaGarg00), [Alondre Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/), [Ankite Singh](https://www.linkedin.com/in/ankitasingh007), [Anupamovi Mishrovi](https://www.linkedin.com/in/anupam--mishra/), [Arpite Das](https://www.linkedin.com/in/arpitadas01/), ChhailBiharimu Dubeymu, [Dibrimu Nsoforovi](https://www.linkedin.com/in/dibrinsofor), [Dishite Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [Majdovi Safimu](https://www.linkedin.com/in/majd-s/), [Maxovi Blumovi](https://www.linkedin.com/in/max-blum-6036a1186/), [Miguelovi Correaovi](https://www.linkedin.com/in/miguelmque/), [Mohammovi Iftekherovi (Iftu) Ebne Jalalovi](https://twitter.com/iftu119), [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum), [Raymondovi Wangsa Putrovi](https://www.linkedin.com/in/raymond-wp/), [Rohitovi Yadavovi](https://www.linkedin.com/in/rty2423), Samridhi Sharma, [Sanyi Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200), [Sheene Narula](https://www.linkedin.com/in/sheena-narua-n/), [Tauqeerovi Ahmadovi](https://www.linkedin.com/in/tauqeerahmad5201/), Yogendrasinghovi Pawarovi, [Vidushi Guptovi](https://www.linkedin.com/in/vidushi-gupta07/), [Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![Sketchnote od @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.sk.png)|
|:---:|
| Dátová veda pre začiatočníkov - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

### 🌐 Podpora viacerých jazykov

#### Podporované prostredníctvom GitHub Action (automatizované a vždy aktuálne)

[Francúzština](../fr/README.md) | [Španielčina](../es/README.md) | [Nemčina](../de/README.md) | [Ruština](../ru/README.md) | [Arabčina](../ar/README.md) | [Perzština (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Čínština (zjednodušená)](../zh/README.md) | [Čínština (tradičná, Macao)](../mo/README.md) | [Čínština (tradičná, Hongkong)](../hk/README.md) | [Čínština (tradičná, Taiwan)](../tw/README.md) | [Japončina](../ja/README.md) | [Kórejčina](../ko/README.md) | [Hindčina](../hi/README.md) | [Bengálčina](../bn/README.md) | [Maráthčina](../mr/README.md) | [Nepálčina](../ne/README.md) | [Pandžábčina (Gurmukhi)](../pa/README.md) | [Portugalčina (Portugalsko)](../pt/README.md) | [Portugalčina (Brazília)](../br/README.md) | [Taliančina](../it/README.md) | [Poľština](../pl/README.md) | [Turečtina](../tr/README.md) | [Gréčtina](../el/README.md) | [Thajčina](../th/README.md) | [Švédčina](../sv/README.md) | [Dánčina](../da/README.md) | [Nórčina](../no/README.md) | [Fínčina](../fi/README.md) | [Holandčina](../nl/README.md) | [Hebrejčina](../he/README.md) | [Vietnamčina](../vi/README.md) | [Indonézština](../id/README.md) | [Malajčina](../ms/README.md) | [Tagalčina (Filipíny)](../tl/README.md) | [Swahilčina](../sw/README.md) | [Maďarčina](../hu/README.md) | [Čeština](../cs/README.md) | [Slovenčina](./README.md) | [Rumunčina](../ro/README.md) | [Bulharčina](../bg/README.md) | [Srbčina (cyrilika)](../sr/README.md) | [Chorvátčina](../hr/README.md) | [Slovinčina](../sl/README.md) | [Ukrajinčina](../uk/README.md) | [Barmčina (Mjanmarsko)](../my/README.md)

**Ak chcete pridať ďalšie preklady, podporované jazyky sú uvedené [tu](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

#### Pridajte sa k našej komunite 
[![Azure AI Discord](https://dcbadge.limes.pink/api/server/kzRShWzttr)](https://discord.gg/kzRShWzttr)

# Ste študent?

Začnite s nasledujúcimi zdrojmi:

- [Stránka pre študentov](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) Na tejto stránke nájdete zdroje pre začiatočníkov, študentské balíčky a dokonca aj spôsoby, ako získať bezplatný certifikát. Túto stránku si určite uložte do záložiek a pravidelne kontrolujte, pretože obsah meníme aspoň raz mesačne.
- [Microsoft Learn Student Ambassadors](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) Pridajte sa k celosvetovej komunite študentských ambasádorov, čo môže byť vaša cesta do Microsoftu.

# Začíname

> **Učitelia**: [pridali sme niekoľko návrhov](for-teachers.md), ako tento učebný plán využiť. Radi by sme dostali vašu spätnú väzbu [v našom diskusnom fóre](https://github.com/microsoft/Data-Science-For-Beginners/discussions)!

> **[Študenti](https://aka.ms/student-page)**: ak chcete tento učebný plán používať samostatne, forknite si celý repozitár a dokončite cvičenia sami, začínajúc kvízom pred lekciou. Potom si prečítajte lekciu a dokončite zvyšné aktivity. Skúste vytvárať projekty pochopením lekcií namiesto kopírovania riešení; tieto riešenia sú však dostupné v priečinkoch /solutions v každej projektovo orientovanej lekcii. Ďalším nápadom by bolo vytvoriť študijnú skupinu s priateľmi a prejsť obsah spolu. Na ďalšie štúdium odporúčame [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum).

## Spoznajte tím

[![Promo video](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "Promo video")

**Gif od** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)

> 🎥 Kliknite na obrázok vyššie pre video o projekte a ľuďoch, ktorí ho vytvorili!

## Pedagogika

Pri tvorbe tohto učebného plánu sme sa riadili dvoma pedagogickými princípmi: zabezpečiť, aby bol založený na projektoch, a aby obsahoval časté kvízy. Na konci tejto série sa študenti naučia základné princípy dátovej vedy, vrátane etických konceptov, prípravy dát, rôznych spôsobov práce s dátami, vizualizácie dát, analýzy dát, reálnych prípadov použitia dátovej vedy a ďalších.

Okrem toho, kvíz s nízkym rizikom pred hodinou nastaví študentovi úmysel učiť sa danú tému, zatiaľ čo druhý kvíz po hodine zabezpečí lepšie zapamätanie. Tento učebný plán bol navrhnutý tak, aby bol flexibilný a zábavný a mohol byť absolvovaný celý alebo len jeho časti. Projekty začínajú jednoduchými úlohami a postupne sa stávajú zložitejšími na konci 10-týždňového cyklu.
> Nájdete náš [Kódex správania](CODE_OF_CONDUCT.md), [Pravidlá prispievania](CONTRIBUTING.md), [Pokyny pre preklad](TRANSLATIONS.md). Vaša konštruktívna spätná väzba je vítaná!
## Každá lekcia obsahuje:

- Voliteľný sketchnote
- Voliteľné doplnkové video
- Kvíz na rozohriatie pred lekciou
- Písomnú lekciu
- Pre lekcie založené na projektoch, podrobné návody na vytvorenie projektu
- Kontrolu vedomostí
- Výzvu
- Doplnkové čítanie
- Zadanie
- [Kvíz po lekcii](https://ff-quizzes.netlify.app/en/)

> **Poznámka ku kvízom**: Všetky kvízy sú uložené v priečinku Quiz-App, celkovo 40 kvízov, každý s tromi otázkami. Sú prepojené priamo z lekcií, ale aplikáciu kvízov je možné spustiť lokálne alebo nasadiť na Azure; postupujte podľa pokynov v priečinku `quiz-app`. Postupne sa lokalizujú.

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
| 05 | Práca s relačnými dátami | [Práca s dátami](2-Working-With-Data/README.md) | Úvod do relačných dát a základy ich skúmania a analýzy pomocou Structured Query Language, známeho ako SQL (vyslovuje sa „si-kvel“). | [lekcia](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | Práca s NoSQL dátami | [Práca s dátami](2-Working-With-Data/README.md) | Úvod do nerelačných dát, ich rôznych typov a základy skúmania a analýzy dokumentových databáz. | [lekcia](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | Práca s Pythonom | [Práca s dátami](2-Working-With-Data/README.md) | Základy používania Pythonu na skúmanie dát s knižnicami ako Pandas. Odporúča sa základné pochopenie programovania v Pythone. | [lekcia](2-Working-With-Data/07-python/README.md) [video](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | Príprava dát | [Práca s dátami](2-Working-With-Data/README.md) | Témy o technikách čistenia a transformácie dát na riešenie problémov s chýbajúcimi, nepresnými alebo neúplnými dátami. | [lekcia](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | Vizualizácia množstiev | [Vizualizácia dát](3-Data-Visualization/README.md) | Naučte sa používať Matplotlib na vizualizáciu dát o vtákoch 🦆 | [lekcia](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | Vizualizácia rozdelení dát | [Vizualizácia dát](3-Data-Visualization/README.md) | Vizualizácia pozorovaní a trendov v rámci intervalu. | [lekcia](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
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
- Vyberte klonovanú kópiu tohto priečinka, počkajte na spustenie kontajnera a vyskúšajte si veci.

## Offline prístup

Túto dokumentáciu môžete spustiť offline pomocou [Docsify](https://docsify.js.org/#/). Forknite tento repozitár, [nainštalujte Docsify](https://docsify.js.org/#/quickstart) na váš lokálny počítač, potom v koreňovom priečinku tohto repozitára zadajte `docsify serve`. Webová stránka bude dostupná na porte 3000 na vašom localhost: `localhost:3000`.

> Poznámka, notebooky nebudú renderované cez Docsify, takže keď potrebujete spustiť notebook, urobte to samostatne vo VS Code s bežiacim Python kernelom.

## Ďalšie učebné osnovy

Náš tím vytvára aj ďalšie učebné osnovy! Pozrite si:

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
- [Vyberte si vlastné dobrodružstvo s Copilotom](https://github.com/microsoft/CopilotAdventures)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby na automatický preklad [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.