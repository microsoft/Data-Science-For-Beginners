<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "12339119c0165da569a93ddba05f9339",
  "translation_date": "2025-09-05T17:57:18+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "cs"
}
-->
# Definování dat

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definování dat - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

Data jsou fakta, informace, pozorování a měření, která se používají k objevování nových poznatků a k podpoře informovaného rozhodování. Datový bod je jednotka dat v rámci datové sady, což je sbírka datových bodů. Datové sady mohou mít různé formáty a struktury, obvykle podle svého zdroje, tedy odkud data pocházejí. Například měsíční příjmy společnosti mohou být ve formátu tabulky, zatímco hodinová data o srdečním tepu ze smartwatch mohou být ve formátu [JSON](https://stackoverflow.com/a/383699). Je běžné, že datoví vědci pracují s různými typy dat v rámci jedné datové sady.

Tato lekce se zaměřuje na identifikaci a klasifikaci dat podle jejich charakteristik a zdrojů.

## [Kvíz před přednáškou](https://ff-quizzes.netlify.app/en/ds/quiz/4)

## Jak jsou data popisována

### Surová data
Surová data jsou data, která pocházejí ze svého zdroje ve svém původním stavu a nebyla analyzována ani organizována. Aby bylo možné pochopit, co se děje s datovou sadou, je třeba ji uspořádat do formátu, který je srozumitelný jak pro lidi, tak pro technologie, které mohou být použity k její další analýze. Struktura datové sady popisuje, jak je organizována, a může být klasifikována jako strukturovaná, nestrukturovaná nebo polostrukturovaná. Tyto typy struktur se liší podle zdroje, ale nakonec spadají do těchto tří kategorií.

### Kvantitativní data
Kvantitativní data jsou číselná pozorování v rámci datové sady, která lze obvykle analyzovat, měřit a používat matematicky. Některé příklady kvantitativních dat jsou: počet obyvatel země, výška osoby nebo čtvrtletní příjmy společnosti. S další analýzou by kvantitativní data mohla být použita k objevení sezónních trendů indexu kvality ovzduší (AQI) nebo k odhadu pravděpodobnosti dopravní špičky během běžného pracovního dne.

### Kvalitativní data
Kvalitativní data, známá také jako kategorická data, jsou data, která nelze měřit objektivně jako kvantitativní pozorování. Obvykle se jedná o různé formáty subjektivních dat, která zachycují kvalitu něčeho, například produktu nebo procesu. Někdy jsou kvalitativní data číselná, ale obvykle se nepoužívají matematicky, například telefonní čísla nebo časové značky. Některé příklady kvalitativních dat jsou: komentáře k videím, značka a model auta nebo oblíbená barva vašich nejbližších přátel. Kvalitativní data by mohla být použita k pochopení, které produkty mají spotřebitelé nejraději, nebo k identifikaci populárních klíčových slov v životopisech uchazečů o zaměstnání.

### Strukturovaná data
Strukturovaná data jsou data, která jsou organizována do řádků a sloupců, kde každý řádek má stejnou sadu sloupců. Sloupce představují hodnotu určitého typu a jsou identifikovány názvem, který popisuje, co hodnota představuje, zatímco řádky obsahují skutečné hodnoty. Sloupce často mají specifickou sadu pravidel nebo omezení pro hodnoty, aby bylo zajištěno, že hodnoty přesně reprezentují sloupec. Například si představte tabulku zákazníků, kde každý řádek musí obsahovat telefonní číslo a telefonní čísla nikdy neobsahují abecední znaky. Mohou být aplikována pravidla na sloupec telefonního čísla, aby bylo zajištěno, že nikdy nebude prázdný a bude obsahovat pouze čísla.

Výhodou strukturovaných dat je, že mohou být organizována tak, aby byla propojena s jinými strukturovanými daty. Nicméně, protože data jsou navržena tak, aby byla organizována specifickým způsobem, změny v jejich celkové struktuře mohou být náročné. Například přidání sloupce e-mailu do tabulky zákazníků, který nemůže být prázdný, znamená, že budete muset zjistit, jak přidat tyto hodnoty do existujících řádků zákazníků v datové sadě.

Příklady strukturovaných dat: tabulky, relační databáze, telefonní čísla, bankovní výpisy

### Nestrukturovaná data
Nestrukturovaná data obvykle nelze kategorizovat do řádků nebo sloupců a neobsahují formát ani sadu pravidel, která by se měla dodržovat. Protože nestrukturovaná data mají méně omezení na svou strukturu, je snazší přidávat nové informace ve srovnání se strukturovanou datovou sadou. Pokud senzor, který zachycuje data o barometrickém tlaku každé 2 minuty, obdrží aktualizaci, která mu nyní umožňuje měřit a zaznamenávat teplotu, nevyžaduje to změnu existujících dat, pokud jsou nestrukturovaná. Nicméně to může prodloužit dobu analýzy nebo zkoumání tohoto typu dat. Například vědec, který chce zjistit průměrnou teplotu za předchozí měsíc z dat senzoru, ale zjistí, že senzor zaznamenal "e" v některých svých datech, aby označil, že byl rozbitý, místo typického čísla, což znamená, že data jsou neúplná.

Příklady nestrukturovaných dat: textové soubory, textové zprávy, video soubory

### Polostrukturovaná data
Polostrukturovaná data mají vlastnosti, které je činí kombinací strukturovaných a nestrukturovaných dat. Obvykle neodpovídají formátu řádků a sloupců, ale jsou organizována způsobem, který je považován za strukturovaný, a mohou dodržovat pevný formát nebo sadu pravidel. Struktura se liší podle zdrojů, od dobře definované hierarchie až po něco flexibilnějšího, co umožňuje snadnou integraci nových informací. Metadata jsou indikátory, které pomáhají rozhodnout, jak jsou data organizována a ukládána, a mají různé názvy podle typu dat. Některé běžné názvy pro metadata jsou značky, prvky, entity a atributy. Například typická e-mailová zpráva bude mít předmět, tělo a sadu příjemců a může být organizována podle toho, kdo ji poslal nebo kdy byla odeslána.

Příklady polostrukturovaných dat: HTML, soubory CSV, JavaScript Object Notation (JSON)

## Zdroje dat

Zdroj dat je počáteční místo, kde byla data vytvořena, nebo kde "žijí", a liší se podle toho, jak a kdy byla shromážděna. Data generovaná uživateli jsou známá jako primární data, zatímco sekundární data pocházejí ze zdroje, který shromáždil data pro obecné použití. Například skupina vědců, která sbírá pozorování v deštném pralese, by byla považována za primární zdroj, a pokud se rozhodnou sdílet tato data s jinými vědci, byla by považována za sekundární pro ty, kteří je používají.

Databáze jsou běžným zdrojem a spoléhají na systém správy databází, který hostuje a udržuje data, kde uživatelé používají příkazy nazývané dotazy k prozkoumání dat. Soubory jako zdroje dat mohou být zvukové, obrazové a video soubory, stejně jako tabulky, například Excel. Internetové zdroje jsou běžným místem pro hostování dat, kde lze najít databáze i soubory. Rozhraní pro programování aplikací, známá také jako API, umožňují programátorům vytvářet způsoby sdílení dat s externími uživateli prostřednictvím internetu, zatímco proces webového scrappingu extrahuje data z webové stránky. [Lekce v Práce s daty](../../../../../../../../../2-Working-With-Data) se zaměřují na to, jak používat různé zdroje dat.

## Závěr

V této lekci jsme se naučili:

- Co jsou data
- Jak jsou data popisována
- Jak jsou data klasifikována a kategorizována
- Kde lze data najít

## 🚀 Výzva

Kaggle je vynikajícím zdrojem otevřených datových sad. Použijte [nástroj pro vyhledávání datových sad](https://www.kaggle.com/datasets) k nalezení zajímavých datových sad a klasifikujte 3-5 datových sad podle těchto kritérií:

- Jsou data kvantitativní nebo kvalitativní?
- Jsou data strukturovaná, nestrukturovaná nebo polostrukturovaná?

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ds/quiz/5)

## Přehled a samostudium

- Tato jednotka Microsoft Learn s názvem [Klasifikace vašich dat](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data) obsahuje podrobný rozbor strukturovaných, polostrukturovaných a nestrukturovaných dat.

## Úkol

[Klasifikace datových sad](assignment.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.