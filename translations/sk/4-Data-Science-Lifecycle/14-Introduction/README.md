<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "07e12a25d20b8f191e3cb651c27fdb2b",
  "translation_date": "2025-09-06T21:33:41+00:00",
  "source_file": "4-Data-Science-Lifecycle/14-Introduction/README.md",
  "language_code": "sk"
}
-->
# Úvod do životného cyklu dátovej vedy

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/14-DataScience-Lifecycle.png)|
|:---:|
| Úvod do životného cyklu dátovej vedy - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

## [Kvíz pred prednáškou](https://ff-quizzes.netlify.app/en/ds/quiz/26)

V tomto bode ste si pravdepodobne uvedomili, že dátová veda je proces. Tento proces je možné rozdeliť do 5 fáz:

- Získavanie
- Spracovanie
- Analýza
- Komunikácia
- Údržba

Táto lekcia sa zameriava na 3 časti životného cyklu: získavanie, spracovanie a údržbu.

![Diagram životného cyklu dátovej vedy](../../../../translated_images/sk/data-science-lifecycle.a1e362637503c4fb0cd5e859d7552edcdb4aa629a279727008baa121f2d33f32.jpg)  
> Foto od [Berkeley School of Information](https://ischoolonline.berkeley.edu/data-science/what-is-data-science/)

## Získavanie

Prvá fáza životného cyklu je veľmi dôležitá, pretože na nej závisia ďalšie fázy. Prakticky ide o dve fázy spojené do jednej: získavanie dát a definovanie účelu a problémov, ktoré je potrebné riešiť.  
Definovanie cieľov projektu si vyžaduje hlbší kontext problému alebo otázky. Najprv musíme identifikovať a získať tých, ktorí potrebujú vyriešiť svoj problém. Môžu to byť zainteresované strany v podniku alebo sponzori projektu, ktorí môžu pomôcť identifikovať, kto alebo čo bude mať z projektu úžitok, ako aj čo a prečo to potrebujú. Dobre definovaný cieľ by mal byť merateľný a kvantifikovateľný, aby bolo možné definovať prijateľný výsledok.

Otázky, ktoré si dátový vedec môže položiť:
- Bol tento problém už niekedy riešený? Čo sa zistilo?
- Je účel a cieľ jasný všetkým zúčastneným?
- Existuje nejasnosť a ako ju znížiť?
- Aké sú obmedzenia?
- Ako bude potenciálne vyzerať konečný výsledok?
- Koľko zdrojov (čas, ľudia, výpočtová kapacita) je k dispozícii?

Ďalším krokom je identifikácia, zhromaždenie a nakoniec preskúmanie dát potrebných na dosiahnutie týchto definovaných cieľov. V tomto kroku získavania musia dátoví vedci tiež vyhodnotiť množstvo a kvalitu dát. To si vyžaduje určitý prieskum dát, aby sa potvrdilo, že získané dáta podporia dosiahnutie požadovaného výsledku.

Otázky, ktoré si dátový vedec môže položiť o dátach:
- Aké dáta už mám k dispozícii?
- Kto vlastní tieto dáta?
- Aké sú obavy týkajúce sa ochrany súkromia?
- Mám dostatok dát na vyriešenie problému?
- Sú dáta dostatočne kvalitné pre tento problém?
- Ak objavím ďalšie informácie prostredníctvom týchto dát, mali by sme zvážiť zmenu alebo predefinovanie cieľov?

## Spracovanie

Fáza spracovania v životnom cykle sa zameriava na objavovanie vzorcov v dátach, ako aj na modelovanie. Niektoré techniky používané vo fáze spracovania vyžadujú štatistické metódy na odhalenie vzorcov. Typicky by to bola únavná úloha pre človeka pri práci s veľkým dátovým súborom, preto sa spoliehame na počítače, ktoré urýchlia proces. Táto fáza je tiež miestom, kde sa dátová veda a strojové učenie prelínajú. Ako ste sa naučili v prvej lekcii, strojové učenie je proces budovania modelov na pochopenie dát. Modely predstavujú vzťah medzi premennými v dátach, ktorý pomáha predpovedať výsledky.

Bežné techniky používané v tejto fáze sú pokryté v učebných materiáloch ML for Beginners. Nasledujte odkazy, aby ste sa o nich dozvedeli viac:

- [Klasifikácia](https://github.com/microsoft/ML-For-Beginners/tree/main/4-Classification): Organizovanie dát do kategórií pre efektívnejšie využitie.
- [Zhlukovanie](https://github.com/microsoft/ML-For-Beginners/tree/main/5-Clustering): Zoskupovanie dát do podobných skupín.
- [Regresia](https://github.com/microsoft/ML-For-Beginners/tree/main/2-Regression): Určenie vzťahov medzi premennými na predpovedanie alebo prognózovanie hodnôt.

## Údržba

Na diagrame životného cyklu ste si mohli všimnúť, že údržba sa nachádza medzi získavaním a spracovaním. Údržba je nepretržitý proces správy, ukladania a zabezpečenia dát počas celého procesu projektu a mala by byť zohľadnená počas celej jeho realizácie.

### Ukladanie dát

Úvahy o tom, ako a kde sú dáta uložené, môžu ovplyvniť náklady na ich ukladanie, ako aj výkon pri ich prístupe. Takéto rozhodnutia pravdepodobne nebudú robiť dátoví vedci sami, ale môžu sa ocitnúť v situácii, keď musia rozhodovať o tom, ako pracovať s dátami na základe spôsobu ich uloženia.

Tu sú niektoré aspekty moderných systémov ukladania dát, ktoré môžu ovplyvniť tieto rozhodnutia:

**On-premise vs off-premise vs verejný alebo súkromný cloud**

On-premise označuje hosting a správu dát na vlastnom vybavení, napríklad vlastnenie servera s pevnými diskami, ktoré ukladajú dáta, zatiaľ čo off-premise sa spolieha na vybavenie, ktoré nevlastníte, ako je dátové centrum. Verejný cloud je populárnou voľbou na ukladanie dát, ktorá nevyžaduje znalosti o tom, ako alebo kde presne sú dáta uložené, pričom verejný označuje jednotnú základnú infraštruktúru, ktorú zdieľajú všetci používatelia cloudu. Niektoré organizácie majú prísne bezpečnostné politiky, ktoré vyžadujú úplný prístup k vybaveniu, kde sú dáta hostované, a spoliehajú sa na súkromný cloud, ktorý poskytuje vlastné cloudové služby. Viac o dátach v cloude sa dozviete v [neskorších lekciách](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/5-Data-Science-In-Cloud).

**Studené vs horúce dáta**

Pri trénovaní modelov môžete potrebovať viac tréningových dát. Ak ste spokojní so svojím modelom, prídu ďalšie dáta, aby model slúžil svojmu účelu. V každom prípade náklady na ukladanie a prístup k dátam budú rásť, ako ich budete hromadiť. Oddelenie zriedka používaných dát, známych ako studené dáta, od často používaných horúcich dát môže byť lacnejšou možnosťou ukladania dát prostredníctvom hardvérových alebo softvérových služieb. Ak je potrebné pristupovať k studeným dátam, ich získanie môže trvať o niečo dlhšie v porovnaní s horúcimi dátami.

### Správa dát

Pri práci s dátami môžete zistiť, že niektoré z nich je potrebné vyčistiť pomocou techník pokrytých v lekcii zameranej na [prípravu dát](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/08-data-preparation), aby ste mohli vytvárať presné modely. Keď prídu nové dáta, budú potrebovať rovnaké aplikácie na udržanie konzistencie kvality. Niektoré projekty budú zahŕňať použitie automatizovaného nástroja na čistenie, agregáciu a kompresiu predtým, ako sa dáta presunú na svoje konečné miesto. Azure Data Factory je príkladom jedného z týchto nástrojov.

### Zabezpečenie dát

Jedným z hlavných cieľov zabezpečenia dát je zabezpečiť, aby tí, ktorí s nimi pracujú, mali kontrolu nad tým, čo sa zhromažďuje a v akom kontexte sa používa. Udržiavanie dát v bezpečí zahŕňa obmedzenie prístupu len na tých, ktorí ho potrebujú, dodržiavanie miestnych zákonov a predpisov, ako aj dodržiavanie etických štandardov, ktoré sú pokryté v [lekcii o etike](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/02-ethics).

Tu sú niektoré kroky, ktoré môže tím podniknúť s ohľadom na bezpečnosť:
- Potvrdiť, že všetky dáta sú šifrované
- Poskytnúť zákazníkom informácie o tom, ako sa ich dáta používajú
- Odobrať prístup k dátam tým, ktorí opustili projekt
- Umožniť len určitým členom projektu meniť dáta

## 🚀 Výzva

Existuje mnoho verzií životného cyklu dátovej vedy, kde každý krok môže mať rôzne názvy a počet fáz, ale bude obsahovať rovnaké procesy uvedené v tejto lekcii.

Preskúmajte [životný cyklus procesu tímovej dátovej vedy](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/lifecycle) a [štandardný proces pre dolovanie dát naprieč odvetviami](https://www.datascience-pm.com/crisp-dm-2/). Pomenujte 3 podobnosti a rozdiely medzi nimi.

|Proces tímovej dátovej vedy (TDSP)|Štandardný proces pre dolovanie dát naprieč odvetviami (CRISP-DM)|
|--|--|
|![Životný cyklus tímovej dátovej vedy](../../../../translated_images/sk/tdsp-lifecycle2.e19029d598e2e73d5ef8a4b98837d688ec6044fe332c905d4dbb69eb6d5c1d96.png) | ![Obrázok od Data Science Process Alliance](../../../../translated_images/sk/CRISP-DM.8bad2b4c66e62aa75278009e38e3e99902c73b0a6f63fd605a67c687a536698c.png) |
| Obrázok od [Microsoft](https://docs.microsoft.comazure/architecture/data-science-process/lifecycle) | Obrázok od [Data Science Process Alliance](https://www.datascience-pm.com/crisp-dm-2/) |

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ds/quiz/27)

## Prehľad a samostatné štúdium

Aplikovanie životného cyklu dátovej vedy zahŕňa rôzne úlohy a role, kde sa niektorí môžu zamerať na konkrétne časti každej fázy. Proces tímovej dátovej vedy poskytuje niekoľko zdrojov, ktoré vysvetľujú typy rolí a úloh, ktoré môže mať niekto v projekte.

* [Role a úlohy procesu tímovej dátovej vedy](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/roles-tasks)  
* [Vykonávanie úloh dátovej vedy: prieskum, modelovanie a nasadenie](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/execute-data-science-tasks)

## Zadanie

[Hodnotenie dátového súboru](assignment.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby na automatický preklad [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie odporúčame profesionálny ľudský preklad. Nezodpovedáme za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.