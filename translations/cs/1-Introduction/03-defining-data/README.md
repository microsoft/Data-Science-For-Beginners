<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1228edf3572afca7d7cdcd938b6b4984",
  "translation_date": "2025-09-04T21:49:22+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "cs"
}
-->
# Definování dat

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definování dat - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

Data jsou fakta, informace, pozorování a měření, která se používají k objevování a podpoře informovaného rozhodování. Datový bod je jedna jednotka dat v rámci datové sady, což je sbírka datových bodů. Datové sady mohou mít různé formáty a struktury a obvykle závisí na svém zdroji, tedy na tom, odkud data pocházejí. Například měsíční výdělky společnosti mohou být ve formátu tabulky, zatímco hodinová data o srdečním tepu ze smartwatch mohou být ve formátu [JSON](https://stackoverflow.com/a/383699). Je běžné, že datoví vědci pracují s různými typy dat v rámci jedné datové sady.

Tato lekce se zaměřuje na identifikaci a klasifikaci dat podle jejich charakteristik a zdrojů.

## [Kvíz před lekcí](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)
## Jak jsou data popisována

### Surová data
Surová data jsou data, která pocházejí ze svého zdroje ve svém původním stavu a nebyla analyzována ani organizována. Abychom pochopili, co se děje s datovou sadou, je třeba ji uspořádat do formátu, kterému rozumí lidé i technologie, kterou mohou použít k další analýze. Struktura datové sady popisuje, jak je organizována, a může být klasifikována jako strukturovaná, nestrukturovaná a polostrukturovaná. Tyto typy struktur se liší v závislosti na zdroji, ale nakonec spadají do těchto tří kategorií.

### Kvantitativní data
Kvantitativní data jsou číselná pozorování v rámci datové sady, která lze obvykle analyzovat, měřit a matematicky zpracovávat. Některé příklady kvantitativních dat jsou: počet obyvatel země, výška osoby nebo čtvrtletní výdělky společnosti. S další analýzou by kvantitativní data mohla být použita k odhalení sezónních trendů indexu kvality ovzduší (AQI) nebo k odhadu pravděpodobnosti dopravní špičky během běžného pracovního dne.

### Kvalitativní data
Kvalitativní data, známá také jako kategorická data, jsou data, která nelze objektivně měřit, jako je tomu u kvantitativních dat. Obvykle se jedná o různé formáty subjektivních dat, která zachycují kvalitu něčeho, například produktu nebo procesu. Někdy jsou kvalitativní data číselná, ale obvykle se matematicky nevyužívají, například telefonní čísla nebo časová razítka. Některé příklady kvalitativních dat jsou: komentáře k videím, značka a model auta nebo oblíbená barva vašich nejbližších přátel. Kvalitativní data by mohla být použita k pochopení, které produkty mají spotřebitelé nejraději, nebo k identifikaci populárních klíčových slov v životopisech uchazečů o zaměstnání.

### Strukturovaná data
Strukturovaná data jsou data organizovaná do řádků a sloupců, kde každý řádek má stejnou sadu sloupců. Sloupce představují hodnotu určitého typu a jsou identifikovány názvem, který popisuje, co hodnota představuje, zatímco řádky obsahují skutečné hodnoty. Sloupce často mají specifickou sadu pravidel nebo omezení pro hodnoty, aby bylo zajištěno, že hodnoty přesně reprezentují sloupec. Například si představte tabulku zákazníků, kde každý řádek musí obsahovat telefonní číslo a telefonní čísla nikdy neobsahují abecední znaky. Mohou být aplikována pravidla na sloupec telefonního čísla, aby bylo zajištěno, že nikdy nebude prázdný a bude obsahovat pouze čísla.

Výhodou strukturovaných dat je, že mohou být organizována tak, aby byla propojitelná s jinými strukturovanými daty. Nicméně, protože data jsou navržena tak, aby byla organizována specifickým způsobem, může být změna jejich celkové struktury velmi náročná. Například přidání sloupce e-mailu do tabulky zákazníků, který nesmí být prázdný, znamená, že budete muset zjistit, jak přidat tyto hodnoty do stávajících řádků zákazníků v datové sadě.

Příklady strukturovaných dat: tabulky, relační databáze, telefonní čísla, bankovní výpisy

### Nestrukturovaná data
Nestrukturovaná data obvykle nelze kategorizovat do řádků nebo sloupců a neobsahují formát ani sadu pravidel, která by se měla dodržovat. Protože nestrukturovaná data mají méně omezení na svou strukturu, je snazší přidávat nové informace ve srovnání se strukturovanou datovou sadou. Pokud senzor zaznamenávající data o barometrickém tlaku každé 2 minuty obdrží aktualizaci, která mu nyní umožňuje měřit a zaznamenávat teplotu, není nutné měnit stávající data, pokud jsou nestrukturovaná. Nicméně to může znamenat, že analýza nebo zkoumání tohoto typu dat bude trvat déle. Například vědec, který chce zjistit průměrnou teplotu za předchozí měsíc z dat senzoru, ale zjistí, že senzor zaznamenal "e" v některých svých datech, aby označil, že byl rozbitý, což znamená, že data jsou neúplná.

Příklady nestrukturovaných dat: textové soubory, textové zprávy, video soubory

### Polostrukturovaná data
Polostrukturovaná data mají vlastnosti, díky nimž jsou kombinací strukturovaných a nestrukturovaných dat. Obvykle neodpovídají formátu řádků a sloupců, ale jsou organizována způsobem, který je považován za strukturovaný, a mohou dodržovat pevný formát nebo sadu pravidel. Struktura se liší mezi zdroji, od dobře definované hierarchie po něco flexibilnějšího, co umožňuje snadnou integraci nových informací. Metadata jsou ukazatele, které pomáhají rozhodnout, jak jsou data organizována a ukládána, a mají různé názvy podle typu dat. Některé běžné názvy pro metadata jsou značky, prvky, entity a atributy. Například typická e-mailová zpráva bude mít předmět, tělo a sadu příjemců a může být organizována podle toho, kdo nebo kdy ji odeslal.

Příklady polostrukturovaných dat: HTML, soubory CSV, JavaScript Object Notation (JSON)

## Zdroje dat

Zdroj dat je počáteční místo, kde byla data vytvořena, nebo kde "žijí", a liší se podle toho, jak a kdy byla shromážděna. Data generovaná uživatelem (uživateli) jsou známá jako primární data, zatímco sekundární data pocházejí ze zdroje, který shromáždil data pro obecné použití. Například skupina vědců shromažďující pozorování v deštném pralese by byla považována za primární zdroj, a pokud by se rozhodli sdílet je s jinými vědci, byla by tato data považována za sekundární pro ty, kteří je používají.

Databáze jsou běžným zdrojem a spoléhají na systém správy databází, který hostí a udržuje data, kde uživatelé používají příkazy nazývané dotazy k prozkoumání dat. Soubory jako zdroje dat mohou být zvukové, obrazové a video soubory, stejně jako tabulky, například Excel. Internetové zdroje jsou běžným místem pro hostování dat, kde lze nalézt databáze i soubory. Rozhraní pro programování aplikací, známá také jako API, umožňují programátorům vytvářet způsoby sdílení dat s externími uživateli prostřednictvím internetu, zatímco proces webového scrapingu extrahuje data z webové stránky. [Lekce v části Práce s daty](../../../../../../../../../2-Working-With-Data) se zaměřují na to, jak používat různé zdroje dat.

## Závěr

V této lekci jsme se naučili:

- Co jsou data
- Jak jsou data popisována
- Jak jsou data klasifikována a kategorizována
- Kde lze data nalézt

## 🚀 Výzva

Kaggle je vynikajícím zdrojem otevřených datových sad. Použijte [nástroj pro vyhledávání datových sad](https://www.kaggle.com/datasets) k nalezení několika zajímavých datových sad a klasifikujte 3-5 datových sad podle těchto kritérií:

- Jsou data kvantitativní nebo kvalitativní?
- Jsou data strukturovaná, nestrukturovaná nebo polostrukturovaná?

## [Kvíz po lekci](https://ff-quizzes.netlify.app/en/ds/)

## Přehled a samostudium

- Tato jednotka Microsoft Learn s názvem [Klasifikace vašich dat](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data) obsahuje podrobný rozbor strukturovaných, polostrukturovaných a nestrukturovaných dat.

## Zadání

[Klasifikace datových sad](assignment.md)

---

**Upozornění**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o co největší přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Za závazný zdroj by měl být považován původní dokument v jeho původním jazyce. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.