<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a167aa0bfb1c46ece1b3d21ae939cc0d",
  "translation_date": "2025-09-05T05:45:15+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "sk"
}
-->
# Životný cyklus dátovej vedy: Analýza

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Životný cyklus dátovej vedy: Analýza - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

## Kvíz pred prednáškou

## [Kvíz pred prednáškou](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

Analýza v životnom cykle dát potvrdzuje, že dáta dokážu odpovedať na položené otázky alebo vyriešiť konkrétny problém. Tento krok sa tiež zameriava na potvrdenie, že model správne rieši tieto otázky a problémy. Táto lekcia sa sústreďuje na prieskumnú analýzu dát (Exploratory Data Analysis, EDA), čo sú techniky na definovanie vlastností a vzťahov v rámci dát, ktoré môžu byť použité na prípravu dát na modelovanie.

Použijeme príkladový dataset z [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1), aby sme ukázali, ako sa to dá aplikovať pomocou Pythonu a knižnice Pandas. Tento dataset obsahuje počty niektorých bežných slov nachádzajúcich sa v e-mailoch, pričom zdroje týchto e-mailov sú anonymné. Použite [notebook](../../../../4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) v tomto adresári na sledovanie.

## Prieskumná analýza dát

Fáza zachytávania v životnom cykle je miestom, kde sa získavajú dáta, ako aj problémy a otázky, ktoré sú na stole. Ale ako vieme, že dáta môžu podporiť konečný výsledok? 
Pripomeňme si, že dátový vedec môže klásť nasledujúce otázky pri získavaní dát:
-   Mám dostatok dát na vyriešenie tohto problému?
-   Sú dáta dostatočne kvalitné pre tento problém?
-   Ak objavím ďalšie informácie prostredníctvom týchto dát, mali by sme zvážiť zmenu alebo predefinovanie cieľov?
Prieskumná analýza dát je proces spoznávania dát a môže byť použitá na zodpovedanie týchto otázok, ako aj na identifikáciu výziev pri práci s datasetom. Zamerajme sa na niektoré techniky používané na dosiahnutie tohto cieľa.

## Profilovanie dát, popisná štatistika a Pandas
Ako môžeme zhodnotiť, či máme dostatok dát na vyriešenie problému? Profilovanie dát môže zhrnúť a zhromaždiť niektoré všeobecné informácie o našom datasete prostredníctvom techník popisnej štatistiky. Profilovanie dát nám pomáha pochopiť, čo máme k dispozícii, a popisná štatistika nám pomáha pochopiť, koľko toho máme.

V niekoľkých predchádzajúcich lekciách sme použili Pandas na poskytovanie niektorých popisných štatistík pomocou funkcie [`describe()`]( https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Táto funkcia poskytuje počet, maximálne a minimálne hodnoty, priemer, štandardnú odchýlku a kvantily na číselných dátach. Používanie popisnej štatistiky, ako je funkcia `describe()`, vám môže pomôcť zhodnotiť, koľko dát máte a či potrebujete viac.

## Sampling a dotazovanie
Preskúmanie všetkého vo veľkom datasete môže byť veľmi časovo náročné a zvyčajne je to úloha ponechaná na počítač. Avšak sampling je užitočný nástroj na pochopenie dát a umožňuje nám lepšie pochopiť, čo je v datasete a čo reprezentuje. S vzorkou môžete aplikovať pravdepodobnosť a štatistiku na dosiahnutie všeobecných záverov o vašich dátach. Hoci neexistuje definované pravidlo o tom, koľko dát by ste mali vzorkovať, je dôležité si uvedomiť, že čím viac dát vzorkujete, tým presnejšiu generalizáciu môžete urobiť o dátach. 
Pandas má vo svojej knižnici funkciu [`sample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), kde môžete zadať argument o tom, koľko náhodných vzoriek chcete získať a použiť.

Všeobecné dotazovanie dát vám môže pomôcť odpovedať na niektoré všeobecné otázky a teórie, ktoré môžete mať. Na rozdiel od sampling-u vám dotazy umožňujú mať kontrolu a zamerať sa na konkrétne časti dát, na ktoré máte otázky. 
Funkcia [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) v knižnici Pandas vám umožňuje vybrať stĺpce a získať jednoduché odpovede o dátach prostredníctvom získaných riadkov.

## Preskúmanie pomocou vizualizácií
Nemusíte čakať, kým sú dáta dôkladne vyčistené a analyzované, aby ste začali vytvárať vizualizácie. V skutočnosti, mať vizuálne zastúpenie počas preskúmania môže pomôcť identifikovať vzory, vzťahy a problémy v dátach. Navyše, vizualizácie poskytujú prostriedok komunikácie s tými, ktorí nie sú zapojení do správy dát, a môžu byť príležitosťou na zdieľanie a objasnenie ďalších otázok, ktoré neboli riešené vo fáze zachytávania. Pozrite si [sekciu o vizualizáciách](../../../../../../../../../3-Data-Visualization), aby ste sa dozvedeli viac o niektorých populárnych spôsoboch preskúmania vizuálne.

## Preskúmanie na identifikáciu nekonzistencií
Všetky témy v tejto lekcii môžu pomôcť identifikovať chýbajúce alebo nekonzistentné hodnoty, ale Pandas poskytuje funkcie na kontrolu niektorých z nich. [isna() alebo isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) môžu kontrolovať chýbajúce hodnoty. Jedným z dôležitých aspektov preskúmania týchto hodnôt vo vašich dátach je preskúmanie, prečo sa tak stali. To vám môže pomôcť rozhodnúť sa, aké [kroky podniknúť na ich vyriešenie](../../../../../../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ds/)

## Zadanie

[Preskúmanie odpovedí](assignment.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.