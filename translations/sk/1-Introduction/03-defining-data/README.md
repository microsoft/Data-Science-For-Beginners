<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "356d12cffc3125db133a2d27b827a745",
  "translation_date": "2025-08-26T15:29:18+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "sk"
}
-->
# Definovanie údajov

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definovanie údajov - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

Údaje sú fakty, informácie, pozorovania a merania, ktoré sa používajú na objavovanie a podporu informovaných rozhodnutí. Dátový bod je jedna jednotka údajov v rámci datasetu, čo je zbierka dátových bodov. Datasety môžu mať rôzne formáty a štruktúry, ktoré zvyčajne závisia od ich zdroja alebo miesta, odkiaľ údaje pochádzajú. Napríklad mesačné príjmy spoločnosti môžu byť v tabuľke, zatiaľ čo údaje o srdcovom tepe zo smart hodiniek môžu byť vo formáte [JSON](https://stackoverflow.com/a/383699). Je bežné, že dátoví vedci pracujú s rôznymi typmi údajov v rámci datasetu.

Táto lekcia sa zameriava na identifikáciu a klasifikáciu údajov podľa ich charakteristík a zdrojov.

## [Kvíz pred prednáškou](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)

## Ako sú údaje popísané

### Surové údaje
Surové údaje sú údaje, ktoré pochádzajú zo svojho zdroja v pôvodnom stave a neboli analyzované ani organizované. Aby sme pochopili, čo sa deje s datasetom, je potrebné ho usporiadať do formátu, ktorý je zrozumiteľný pre ľudí, ako aj pre technológie, ktoré môžu byť použité na jeho ďalšiu analýzu. Štruktúra datasetu popisuje, ako je organizovaný, a môže byť klasifikovaná ako štruktúrovaná, neštruktúrovaná a polostruktúrovaná. Tieto typy štruktúr sa líšia v závislosti od zdroja, ale nakoniec spadajú do týchto troch kategórií.

### Kvantitatívne údaje
Kvantitatívne údaje sú numerické pozorovania v rámci datasetu, ktoré je možné analyzovať, merať a používať matematicky. Niektoré príklady kvantitatívnych údajov sú: populácia krajiny, výška osoby alebo štvrťročné príjmy spoločnosti. S ďalšou analýzou by kvantitatívne údaje mohli byť použité na objavenie sezónnych trendov indexu kvality ovzdušia (AQI) alebo na odhad pravdepodobnosti dopravnej špičky počas bežného pracovného dňa.

### Kvalitatívne údaje
Kvalitatívne údaje, známe aj ako kategóriové údaje, sú údaje, ktoré nemožno objektívne merať ako kvantitatívne pozorovania. Vo všeobecnosti ide o rôzne formáty subjektívnych údajov, ktoré zachytávajú kvalitu niečoho, napríklad produktu alebo procesu. Niekedy sú kvalitatívne údaje numerické, ale zvyčajne sa nepoužívajú matematicky, ako napríklad telefónne čísla alebo časové pečiatky. Niektoré príklady kvalitatívnych údajov sú: komentáre k videám, značka a model auta alebo obľúbená farba vašich najbližších priateľov. Kvalitatívne údaje by mohli byť použité na pochopenie, ktoré produkty majú spotrebitelia najradšej, alebo na identifikáciu populárnych kľúčových slov v životopisoch uchádzačov o zamestnanie.

### Štruktúrované údaje
Štruktúrované údaje sú údaje, ktoré sú organizované do riadkov a stĺpcov, kde každý riadok má rovnakú sadu stĺpcov. Stĺpce predstavujú hodnotu určitého typu a sú identifikované názvom, ktorý popisuje, čo hodnota predstavuje, zatiaľ čo riadky obsahujú skutočné hodnoty. Stĺpce často majú konkrétnu sadu pravidiel alebo obmedzení na hodnoty, aby sa zabezpečilo, že hodnoty presne reprezentujú stĺpec. Napríklad si predstavte tabuľku zákazníkov, kde každý riadok musí obsahovať telefónne číslo a telefónne čísla nikdy neobsahujú abecedné znaky. Na stĺpec telefónneho čísla môžu byť aplikované pravidlá, aby nikdy nebol prázdny a obsahoval iba čísla.

Výhodou štruktúrovaných údajov je, že môžu byť organizované tak, aby mohli byť prepojené s inými štruktúrovanými údajmi. Avšak, pretože údaje sú navrhnuté tak, aby boli organizované konkrétnym spôsobom, zmeny v ich celkovej štruktúre môžu vyžadovať veľa úsilia. Napríklad pridanie stĺpca e-mailu do tabuľky zákazníkov, ktorý nemôže byť prázdny, znamená, že budete musieť zistiť, ako pridáte tieto hodnoty do existujúcich riadkov zákazníkov v datasetu.

Príklady štruktúrovaných údajov: tabuľky, relačné databázy, telefónne čísla, bankové výpisy.

### Neštruktúrované údaje
Neštruktúrované údaje zvyčajne nemožno kategorizovať do riadkov alebo stĺpcov a neobsahujú formát ani súbor pravidiel, ktoré by sa mali dodržiavať. Pretože neštruktúrované údaje majú menej obmedzení na svoju štruktúru, je jednoduchšie pridávať nové informácie v porovnaní so štruktúrovaným datasetom. Ak senzor, ktorý zachytáva údaje o barometrickom tlaku každé 2 minúty, dostane aktualizáciu, ktorá mu umožní merať a zaznamenávať teplotu, nevyžaduje to zmenu existujúcich údajov, ak sú neštruktúrované. Avšak to môže spôsobiť, že analýza alebo skúmanie takýchto údajov bude trvať dlhšie. Napríklad vedec, ktorý chce zistiť priemernú teplotu za predchádzajúci mesiac z údajov senzora, ale zistí, že senzor zaznamenal "e" v niektorých svojich údajoch, aby označil, že bol pokazený, namiesto typického čísla, čo znamená, že údaje sú neúplné.

Príklady neštruktúrovaných údajov: textové súbory, textové správy, video súbory.

### Polostruktúrované údaje
Polostruktúrované údaje majú vlastnosti, ktoré z nich robia kombináciu štruktúrovaných a neštruktúrovaných údajov. Zvyčajne nevyhovujú formátu riadkov a stĺpcov, ale sú organizované spôsobom, ktorý sa považuje za štruktúrovaný a môže dodržiavať pevný formát alebo súbor pravidiel. Štruktúra sa líši medzi zdrojmi, od dobre definovanej hierarchie až po niečo flexibilnejšie, čo umožňuje jednoduchú integráciu nových informácií. Metaúdaje sú indikátory, ktoré pomáhajú rozhodnúť, ako sú údaje organizované a uložené, a majú rôzne názvy v závislosti od typu údajov. Niektoré bežné názvy pre metaúdaje sú značky, prvky, entity a atribúty. Napríklad typická e-mailová správa bude mať predmet, telo a sadu príjemcov a môže byť organizovaná podľa toho, kto ju poslal alebo kedy bola odoslaná.

Príklady polostruktúrovaných údajov: HTML, CSV súbory, JavaScript Object Notation (JSON).

## Zdroje údajov

Zdroj údajov je počiatočné miesto, kde boli údaje generované alebo kde "žijú" a líši sa podľa toho, ako a kedy boli zhromaždené. Údaje generované ich používateľmi sú známe ako primárne údaje, zatiaľ čo sekundárne údaje pochádzajú zo zdroja, ktorý zhromaždil údaje na všeobecné použitie. Napríklad skupina vedcov, ktorá zhromažďuje pozorovania v dažďovom pralese, by bola považovaná za primárny zdroj, a ak sa rozhodnú zdieľať tieto údaje s inými vedcami, pre tých, ktorí ich používajú, by to bolo považované za sekundárny zdroj.

Databázy sú bežným zdrojom a spoliehajú sa na systém správy databáz na hosťovanie a údržbu údajov, kde používatelia používajú príkazy nazývané dotazy na skúmanie údajov. Súbory ako zdroje údajov môžu byť zvukové, obrazové a video súbory, ako aj tabuľky ako Excel. Internetové zdroje sú bežným miestom na hosťovanie údajov, kde sa dajú nájsť databázy aj súbory. Rozhrania aplikačného programovania, známe aj ako API, umožňujú programátorom vytvárať spôsoby zdieľania údajov s externými používateľmi prostredníctvom internetu, zatiaľ čo proces webového škrabania extrahuje údaje z webovej stránky. [Lekcie v práci s údajmi](../../../../../../../../../2-Working-With-Data) sa zameriavajú na to, ako používať rôzne zdroje údajov.

## Záver

V tejto lekcii sme sa naučili:

- Čo sú údaje
- Ako sú údaje popísané
- Ako sú údaje klasifikované a kategorizované
- Kde je možné údaje nájsť

## 🚀 Výzva

Kaggle je vynikajúcim zdrojom otvorených datasetov. Použite [nástroj na vyhľadávanie datasetov](https://www.kaggle.com/datasets) na nájdenie niekoľkých zaujímavých datasetov a klasifikujte 3-5 datasetov podľa týchto kritérií:

- Sú údaje kvantitatívne alebo kvalitatívne?
- Sú údaje štruktúrované, neštruktúrované alebo polostruktúrované?

## [Kvíz po prednáške](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/5)

## Prehľad a samostatné štúdium

- Táto jednotka Microsoft Learn s názvom [Klasifikujte svoje údaje](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data) obsahuje podrobný rozpis štruktúrovaných, polostruktúrovaných a neštruktúrovaných údajov.

## Zadanie

[Klasifikácia datasetov](assignment.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.