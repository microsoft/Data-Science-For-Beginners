<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d92f57eb110dc7f765c05cbf0f837c77",
  "translation_date": "2025-08-26T16:29:50+00:00",
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

Analýza v životnom cykle dát potvrdzuje, že dáta dokážu odpovedať na položené otázky alebo vyriešiť konkrétny problém. Tento krok sa môže tiež zamerať na potvrdenie, že model správne rieši tieto otázky a problémy. Táto lekcia sa sústreďuje na prieskumnú analýzu dát (Exploratory Data Analysis, EDA), čo sú techniky na definovanie vlastností a vzťahov v rámci dát a ich prípravu na modelovanie.

Použijeme príkladovú dátovú sadu z [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1), aby sme ukázali, ako to možno aplikovať pomocou Pythonu a knižnice Pandas. Táto dátová sada obsahuje počty niektorých bežných slov nachádzajúcich sa v e-mailoch, pričom zdroje týchto e-mailov sú anonymné. Použite [notebook](notebook.ipynb) v tomto adresári na sledovanie postupu.

## Prieskumná analýza dát

Fáza zachytávania v životnom cykle je miestom, kde sa získavajú dáta, ako aj problémy a otázky, ktoré treba riešiť. Ale ako zistíme, či dáta môžu podporiť konečný výsledok? 
Pripomeňme si, že dátový vedec môže klásť nasledujúce otázky pri získavaní dát:
-   Mám dostatok dát na vyriešenie tohto problému?
-   Sú dáta dostatočne kvalitné pre tento problém?
-   Ak objavím ďalšie informácie prostredníctvom týchto dát, mali by sme zvážiť zmenu alebo predefinovanie cieľov?
Prieskumná analýza dát je proces spoznávania dát a môže byť použitá na zodpovedanie týchto otázok, ako aj na identifikáciu výziev pri práci s dátovou sadou. Poďme sa zamerať na niektoré techniky používané na dosiahnutie tohto cieľa.

## Profilovanie dát, popisná štatistika a Pandas
Ako zhodnotíme, či máme dostatok dát na vyriešenie problému? Profilovanie dát môže zhrnúť a zhromaždiť niektoré všeobecné informácie o našej dátovej sade prostredníctvom techník popisnej štatistiky. Profilovanie dát nám pomáha pochopiť, čo máme k dispozícii, a popisná štatistika nám pomáha pochopiť, koľko toho máme.

V niektorých predchádzajúcich lekciách sme použili Pandas na poskytnutie popisnej štatistiky pomocou funkcie [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Táto funkcia poskytuje počet, maximálne a minimálne hodnoty, priemer, štandardnú odchýlku a kvantily pre numerické dáta. Použitie popisnej štatistiky, ako je funkcia `describe()`, vám môže pomôcť posúdiť, koľko dát máte a či potrebujete viac.

## Vzorkovanie a dotazovanie
Preskúmanie všetkého v rozsiahlej dátovej sade môže byť veľmi časovo náročné a zvyčajne je to úloha, ktorú vykonáva počítač. Vzorkovanie je však užitočný nástroj na pochopenie dát a umožňuje nám lepšie pochopiť, čo sa v dátovej sade nachádza a čo reprezentuje. Pomocou vzorky môžete aplikovať pravdepodobnosť a štatistiku na dosiahnutie všeobecných záverov o vašich dátach. Hoci neexistuje presne definované pravidlo, koľko dát by ste mali vzorkovať, je dôležité si uvedomiť, že čím viac dát vzorkujete, tým presnejšiu generalizáciu môžete o dátach urobiť. 
Pandas má vo svojej knižnici funkciu [`sample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), kde môžete zadať argument o tom, koľko náhodných vzoriek chcete získať a použiť.

Všeobecné dotazovanie dát vám môže pomôcť odpovedať na niektoré všeobecné otázky a teórie, ktoré môžete mať. Na rozdiel od vzorkovania vám dotazy umožňujú mať kontrolu a zamerať sa na konkrétne časti dát, na ktoré máte otázky. 
Funkcia [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) v knižnici Pandas vám umožňuje vybrať stĺpce a získať jednoduché odpovede o dátach prostredníctvom získaných riadkov.

## Preskúmanie pomocou vizualizácií
Nemusíte čakať, kým budú dáta dôkladne vyčistené a analyzované, aby ste mohli začať vytvárať vizualizácie. V skutočnosti môže mať vizuálne znázornenie počas preskúmavania dát pomôcť identifikovať vzory, vzťahy a problémy v dátach. Navyše, vizualizácie poskytujú spôsob komunikácie s tými, ktorí nie sú zapojení do správy dát, a môžu byť príležitosťou na zdieľanie a objasnenie ďalších otázok, ktoré neboli riešené vo fáze zachytávania. Pozrite si [sekciu o vizualizáciách](../../../../../../../../../3-Data-Visualization), aby ste sa dozvedeli viac o niektorých populárnych spôsoboch vizuálneho preskúmavania.

## Preskúmanie na identifikáciu nekonzistencií
Všetky témy v tejto lekcii môžu pomôcť identifikovať chýbajúce alebo nekonzistentné hodnoty, ale Pandas poskytuje funkcie na kontrolu niektorých z nich. [isna() alebo isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) môžu skontrolovať chýbajúce hodnoty. Jedným z dôležitých aspektov preskúmavania týchto hodnôt vo vašich dátach je preskúmať, prečo sa tam vôbec dostali. To vám môže pomôcť rozhodnúť sa, aké [kroky podniknúť na ich vyriešenie](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Kvíz pred prednáškou](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/27)

## Zadanie

[Preskúmanie pre odpovede](assignment.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.