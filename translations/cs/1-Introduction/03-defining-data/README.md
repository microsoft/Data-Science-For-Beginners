# Definování dat

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definování dat - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

Data jsou fakta, informace, pozorování a měření, které se používají k objevům a k podpoře informovaných rozhodnutí. Datový bod je jednotlivá jednotka dat v sadě dat, což je kolekce datových bodů. Sady dat mohou mít různé formáty a struktury a obvykle budou založeny na svém zdroji, tedy odkud data pocházejí. Například měsíční výdělky společnosti mohou být v tabulce, ale hodinová data o srdečním tepu ze smartphonu mohou být ve formátu [JSON](https://stackoverflow.com/a/383699). Je běžné, že datoví vědci pracují s různými typy dat v rámci jedné sady dat.

Tato lekce se zaměřuje na identifikaci a klasifikaci dat podle jejich vlastností a zdrojů.

## [Přednáškový kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Jak jsou data popsána

### Surová data
Surová data jsou data, která pocházejí ze svého zdroje ve svém počátečním stavu a nebyla analyzována ani uspořádána. Abychom pochopili, co se se sadou dat děje, musí být uspořádána do formátu, který může být chápán jak lidmi, tak technologiemi, jež je mohou dál analyzovat. Struktura sady dat popisuje, jak je uspořádána, a může být klasifikována jako strukturovaná, nestrukturovaná a polostrukturovaná. Tyto typy struktur se budou lišit v závislosti na zdroji, ale nakonec spadají do těchto tří kategorií.

### Kvantitativní data
Kvantitativní data jsou číselná pozorování ve skupině dat a obvykle je lze analyzovat, měřit a používat matematicky. Některé příklady kvantitativních dat jsou: populace země, výška osoby nebo čtvrtletní výdělky společnosti. S další analýzou by kvantitativní data mohla být použita k objevení sezónních trendů indexu kvality ovzduší (AQI) nebo k odhadu pravděpodobnosti dopravní špičky v typický pracovní den.

### Kvalitativní data
Kvalitativní data, také známá jako kategoriální data, jsou data, která nelze objektivně měřit jako pozorování kvantitativních dat. Obvykle jde o různé formáty subjektivních dat, která zachycují kvalitu něčeho, například produktu nebo procesu. Někdy jsou kvalitativní data číselná a obvykle by nebyla používána matematicky, jako jsou telefonní čísla nebo časová razítka. Některé příklady kvalitativních dat jsou: komentáře k videím, značka a model auta nebo oblíbená barva vašich nejbližších přátel. Kvalitativní data lze použít k pochopení, které produkty mají spotřebitelé nejraději, nebo k identifikaci populárních klíčových slov v životopisech pracovních uchazečů.

### Strukturovaná data
Strukturovaná data jsou data uspořádaná do řádků a sloupců, kde každý řádek má stejnou sadu sloupců. Sloupce představují hodnotu určitého typu a jsou identifikovány názvem, který popisuje, co hodnota představuje, zatímco řádky obsahují skutečné hodnoty. Sloupce často mají specifické sady pravidel nebo omezení na hodnoty, aby bylo zajištěno, že hodnoty správně reprezentují sloupec. Například si představte tabulku zákazníků, kde každý řádek musí mít telefonní číslo a telefonní čísla nikdy neobsahují abecední znaky. Mohou být na sloupec s telefonním číslem aplikována pravidla, aby nikdy nebyl prázdný a obsahoval pouze čísla.

Výhodou strukturovaných dat je, že mohou být uspořádána tak, aby bylo možné je vztáhnout k jiným strukturovaným datům. Nicméně, protože data jsou navržena k uspořádání určitým způsobem, může být změna jejich celkové struktury náročná. Například přidání sloupce s e-mailem do tabulky zákazníků, který nesmí být prázdný, znamená, že budete muset zjistit, jak tyto hodnoty přidat k existujícím řádkům zákazníků v sadě dat.

Příklady strukturovaných dat: tabulky, relační databáze, telefonní čísla, bankovní výpisy

### Nestrukturovaná data
Nestrukturovaná data obvykle nelze kategorizovat do řádků nebo sloupců a neobsahují formát ani sadu pravidel, která by bylo třeba dodržovat. Protože nestrukturovaná data mají méně omezení na svou strukturu, je snazší přidávat nové informace ve srovnání se strukturovanou sadou dat. Pokud senzor, který snímá data o barometrickém tlaku každé 2 minuty, dostane aktualizaci, která mu umožní měřit a zaznamenávat teplotu, nebude nutné měnit stávající data, pokud jsou nestrukturovaná. Toto však může znamenat, že analýza nebo zkoumání takových dat potrvá déle. Například vědec, který chce zjistit průměrnou teplotu za předchozí měsíc z dat senzoru, ale zjistí, že senzor zaznamenal v některých datech písmeno „e“ pro označení, že byl senzor rozbitý místo typického čísla, což znamená, že data nejsou kompletní.

Příklady nestrukturovaných dat: textové soubory, textové zprávy, video soubory

### Polostrukturovaná data
Polostrukturovaná data mají vlastnosti, které z nich činí kombinaci strukturovaných a nestrukturovaných dat. Obvykle neodpovídají formátu řádků a sloupců, ale jsou uspořádána způsobem, který je považován za strukturovaný a může dodržovat pevný formát nebo sadu pravidel. Struktura se bude lišit podle zdrojů, například od dobře definované hierarchie až po něco flexibilnějšího, co umožňuje snadnou integraci nových informací. Metadata jsou indikátory, které pomáhají rozhodnout, jak jsou data uspořádána a uložena, a mají různá jména podle typu dat. Některá běžná jména pro metadata jsou tagy, elementy, entity a atributy. Například běžný e-mail bude mít předmět, tělo a sadu příjemců a může být uspořádán podle toho, kdo nebo kdy byl odeslán.

Příklady polostrukturovaných dat: HTML, CSV soubory, JavaScript Object Notation (JSON)

## Zdroje dat

Zdroj dat je počáteční místo, kde byla data vytvořena nebo kde „žijí“ a bude se lišit podle toho, jak a kdy byla data shromážděna. Data generovaná svými uživateli jsou známá jako primární data, zatímco sekundární data pocházejí ze zdroje, který data shromažďoval pro obecné použití. Například skupina vědců sbírajících pozorování v deštném pralese by byla považována za primární zdroj a pokud je rozhodnou sdílet s jinými vědci, budou pro ty, kdo je používají, považována za sekundární.

Databáze jsou běžným zdrojem a spoléhají na systém pro správu databází k hostování a udržování dat, kde uživatelé používají příkazy zvané dotazy k průzkumu dat. Soubory jako zdroje dat mohou být audio, obrazové a video soubory, stejně jako tabulky typu Excel. Internetové zdroje jsou běžným místem pro hostování dat, kde lze najít databáze i soubory. Rozhraní aplikačního programování, známá také jako API, umožňují programátorům vytvářet způsoby sdílení dat s externími uživateli přes internet, zatímco proces web scrapingu extrahuje data z webové stránky. [Lekce v sekci Práce s daty](../../../../../../../../../2-Working-With-Data) se zaměřují na to, jak využívat různé zdroje dat.

## Závěr

V této lekci jsme se naučili:

- Co jsou data
- Jak jsou data popsána
- Jak jsou data klasifikována a kategorizována
- Kde lze data najít

## 🚀 Výzva

Kaggle je vynikajícím zdrojem otevřených sad dat. Použijte [nástroj pro hledání sad dat](https://www.kaggle.com/datasets), abyste našli zajímavé sady dat a klasifikovali 3-5 sad pomocí těchto kritérií:

- Jsou data kvantitativní nebo kvalitativní?
- Jsou data strukturovaná, nestrukturovaná, nebo polostrukturovaná?

## [Popřednáškový kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Revize & Samostudium

- Tato jednotka Microsoft Learn, nazvaná [Identifikace formátů dat](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text), má podrobný rozbor strukturovaných, polostrukturovaných a nestrukturovaných dat.

## Úkol

[Klasifikace sad dat](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->