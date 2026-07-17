# Definovanie údajov

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definovanie údajov - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

Údaje sú fakty, informácie, pozorovania a merania, ktoré sa používajú na objavovanie a podporu informovaných rozhodnutí. Dátový bod je jediná jednotka údajov v rámci dátovej sady, čo je zbierka dátových bodov. Dátové súbory môžu mať rôzne formáty a štruktúry a zvyčajne sú založené na ich zdroji alebo odkiaľ údaje pochádzajú. Napríklad mesačný zárobok firmy môže byť v tabuľke, ale hodinové údaje o srdcovom tepe z chytrých hodiniek môžu byť vo formáte [JSON](https://stackoverflow.com/a/383699). Je bežné, že dátoví vedci pracujú s rôznymi typmi údajov v rámci dátovej sady.

Táto lekcia sa zameriava na identifikáciu a klasifikáciu údajov podľa ich charakteristík a zdrojov.

## [Kvíz pred prednáškou](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Ako sa údaje opisujú

### Neupravené údaje
Neupravené údaje sú údaje, ktoré pochádzajú zo svojho zdroja v pôvodnom stave a neboli analyzované ani organizované. Aby bolo možné pochopiť, čo sa s dátovou sadou deje, je potrebné ich usporiadať do formátu, ktorý môžu pochopiť nielen ľudia, ale aj technológie, ktoré ich budú ďalej analyzovať. Štruktúra dátovej sady popisuje, ako je organizovaná a môže byť klasifikovaná ako štruktúrovaná, neštruktúrovaná alebo pološtruktúrovaná. Tieto typy štruktúr sa líšia v závislosti od zdroja, ale nakoniec zapadajú do týchto troch kategórií.

### Kvantitatívne údaje
Kvantitatívne údaje sú numerické pozorovania v rámci dátovej sady, ktoré sa typicky dajú analyzovať, merať a používať matematicky. Niektoré príklady kvantitatívnych údajov sú: populácia krajiny, výška osoby alebo štvrťročné zárobky firmy. S dodatočnou analýzou by sa kvantitatívne údaje mohli použiť na objavenie sezónnych trendov indexu kvality ovzdušia (AQI) alebo na odhad pravdepodobnosti dopravnej špičky v typický pracovný deň.

### Kvalitatívne údaje
Kvalitatívne údaje, známe tiež ako kategorizované údaje, sú údaje, ktoré sa nedajú objektívne merať ako pozorovania kvantitatívnych údajov. Väčšinou ide o rôzne formáty subjektívnych údajov, ktoré zachytávajú kvalitu niečoho, napríklad produktu alebo procesu. Niekedy sú kvalitatívne údaje číselné, ale obvykle sa matematicky nepoužívajú, napríklad telefónne čísla alebo časové značky. Niektoré príklady kvalitatívnych údajov sú: komentáre k videám, značka a model auta alebo obľúbená farba vašich najbližších priateľov. Kvalitatívne údaje by sa mohli použiť na pochopenie toho, ktoré produkty majú spotrebitelia najradšej, alebo na identifikáciu populárnych kľúčových slov v životopisoch pri žiadostiach o zamestnanie.

### Štruktúrované údaje
Štruktúrované údaje sú údaje organizované do riadkov a stĺpcov, kde každý riadok má rovnaký súbor stĺpcov. Stĺpce predstavujú hodnoty určitého typu a sú identifikované menom, ktoré popisuje, čo hodnota predstavuje, zatiaľ čo riadky obsahujú skutočné hodnoty. Stĺpce často majú špecifické pravidlá alebo obmedzenia pre hodnoty, aby sa zabezpečilo, že hodnoty presne reprezentujú stĺpec. Napríklad si predstavte tabuľku zákazníkov, kde každý riadok musí mať telefónne číslo a tieto telefónne čísla nesmú obsahovať abecedné znaky. Môžu tam byť pravidlá pre stĺpec telefónneho čísla, aby nikdy nebol prázdny a obsahoval len čísla.

Výhodou štruktúrovaných údajov je, že môžu byť organizované tak, aby boli prepojené s inými štruktúrovanými údajmi. Avšak pretože sú navrhnuté byť organizované špecifickým spôsobom, zmeny ich celkovej štruktúry môžu byť náročné na realizáciu. Napríklad pridať stĺpec emailovú adresu do tabuľky zákazníkov, kde tento stĺpec nesmie byť prázdny, znamená, že budete musieť vymyslieť spôsob, ako tieto hodnoty pridať k existujúcim riadkom zákazníkov v dátovej sade.

Príklady štruktúrovaných údajov: tabuľky, relačné databázy, telefónne čísla, bankové výpisy

### Neštruktúrované údaje
Neštruktúrované údaje sa zvyčajne nedajú kategorizovať do riadkov alebo stĺpcov a neobsahujú formát ani súbor pravidiel, ktorým by sa mali riadiť. Pretože neštruktúrované údaje majú menej obmedzení vo svojej štruktúre, je jednoduchšie pridávať nové informácie v porovnaní so štruktúrovanou dátovou sadou. Ak senzor zaznamenávajúci údaje o barometrickom tlaku každé 2 minúty dostane aktualizáciu, ktorá mu umožní merať a zaznamenať teplotu, nemusí meniť existujúce údaje, ak sú neštruktúrované. Avšak to môže spôsobiť, že analýza alebo skúmanie takýchto údajov bude trvať dlhšie. Napríklad vedec, ktorý chce získať priemernú teplotu za predchádzajúci mesiac zo senzorových údajov, objaví, že senzor zaznamenal v niektorých údajoch "e" na označenie, že bol poškodený, namiesto typického čísla, čo znamená, že údaje sú neúplné.

Príklady neštruktúrovaných údajov: textové súbory, textové správy, video súbory

### Pološtruktúrované údaje
Pološtruktúrované údaje majú charakteristiky, ktoré ich robia kombináciou štruktúrovaných a neštruktúrovaných údajov. Zvyčajne nezodpovedajú formátu riadkov a stĺpcov, ale sú organizované spôsobom, ktorý sa považuje za štruktúrovaný a môžu nasledovať pevný formát alebo súbor pravidiel. Štruktúra sa líši medzi zdrojmi, od dobre definovanej hierarchie až po niečo flexibilnejšie, čo umožňuje ľahkú integráciu nových informácií. Metadáta sú indikátory, ktoré pomáhajú rozhodnúť, ako sú údaje organizované a uložené, a majú rôzne názvy podľa typu údajov. Niektoré bežné názvy metadát sú značky, prvky, entity a atribúty. Napríklad typická emailová správa má predmet, telo a súbor príjemcov a môže byť organizovaná podľa toho, kto ju poslal alebo kedy bola odoslaná.

Príklady pološtruktúrovaných údajov: HTML, CSV súbory, JavaScript Object Notation (JSON)

## Zdroje údajov

Zdroj údajov je počiatočné miesto, kde boli údaje vytvorené alebo kde „žijú“, a líši sa v závislosti od toho, ako a kedy boli zozbierané. Údaje generované používateľmi sa nazývajú primárne údaje, zatiaľ čo sekundárne údaje pochádzajú zo zdroja, ktorý údaje zhromaždil na všeobecné použitie. Napríklad skupina vedcov zhromažďujúcich pozorovania v dažďovom pralese sa považuje za primárny zdroj, a ak sa rozhodnú zdieľať tieto údaje s inými vedcami, budú pre týchto používateľov sekundárne.

Databázy sú bežným zdrojom a spoľahnú sa na systém správy databáz na hosťovanie a údržbu údajov, kde používatelia používajú príkazy nazývané dotazy na prieskum údajov. Súbory ako zdroje údajov môžu byť audio, obrazové a video súbory, ako aj tabuľky ako Excel. Internetové zdroje sú bežným miestom na ukladanie údajov, kde sa nachádzajú databázy aj súbory. Aplikačné programovacie rozhrania, známe ako API, umožňujú programátorom vytvárať spôsoby zdieľania údajov s externými používateľmi cez internet, zatiaľ čo proces webového škrabania získava údaje z webovej stránky. [Lekcie v sekcii Práca s údajmi](../../../../../../../../../2-Working-With-Data) sa zameriavajú na používanie rôznych zdrojov údajov.

## Záver

V tejto lekcii sme sa naučili:

- Čo sú údaje
- Ako sa údaje opisujú
- Ako sa údaje klasifikujú a kategorizujú
- Kde sa údaje dajú nájsť

## 🚀 Výzva

Kaggle je vynikajúci zdroj otvorených dátových súborov. Použite [nástroj na vyhľadávanie datasetov](https://www.kaggle.com/datasets) na nájdenie niekoľkých zaujímavých datasetov a klasifikujte 3-5 datasetov podľa týchto kritérií:

- Sú údaje kvantitatívne alebo kvalitatívne?
- Sú údaje štruktúrované, neštruktúrované alebo pološtruktúrované?

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Prehľad a samostatné štúdium

- Táto jednotka Microsoft Learn, s názvom [Identifikácia formátov údajov](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text) má detailné rozdelenie štruktúrovaných, pološtruktúrovaných a neštruktúrovaných údajov.

## Úloha

[Klasifikácia datasetov](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->