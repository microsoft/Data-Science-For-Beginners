<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2baeafe1db4d58ee5b8ec85db9de728a",
  "translation_date": "2025-09-05T17:48:10+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "cs"
}
-->
# Životní cyklus datové vědy: Analýza

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Životní cyklus datové vědy: Analýza - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

## Kvíz před přednáškou

## [Kvíz před přednáškou](https://ff-quizzes.netlify.app/en/ds/quiz/28)

Analýza v životním cyklu dat potvrzuje, že data mohou odpovědět na položené otázky nebo vyřešit konkrétní problém. Tento krok se také zaměřuje na ověření, zda model správně řeší tyto otázky a problémy. Tato lekce se zaměřuje na průzkumnou analýzu dat (Exploratory Data Analysis, EDA), což jsou techniky pro definování vlastností a vztahů v datech, které mohou být použity k přípravě dat pro modelování.

Použijeme příklad datové sady z [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1), abychom ukázali, jak lze tyto techniky aplikovat pomocí Pythonu a knihovny Pandas. Tato datová sada obsahuje počty některých běžných slov nalezených v e-mailech, přičemž zdroje těchto e-mailů jsou anonymní. Použijte [notebook](../../../../4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) v tomto adresáři, abyste mohli postupovat podle příkladu.

## Průzkumná analýza dat

Fáze zachycení v životním cyklu je místem, kde jsou data získávána, stejně jako problémy a otázky, které je třeba řešit. Jak ale zjistíme, zda data mohou podpořit požadovaný výsledek? 
Připomeňme si, že datový vědec může při získávání dat klást následující otázky:
-   Mám dostatek dat k vyřešení tohoto problému?
-   Jsou data dostatečně kvalitní pro tento problém?
-   Pokud prostřednictvím těchto dat objevíme další informace, měli bychom zvážit změnu nebo redefinici cílů?
Průzkumná analýza dat je proces, jak se s daty seznámit, a může být použita k zodpovězení těchto otázek, stejně jako k identifikaci výzev při práci s datovou sadou. Zaměřme se na některé techniky, které se k tomu používají.

## Profilování dat, popisná statistika a Pandas
Jak můžeme zhodnotit, zda máme dostatek dat k vyřešení problému? Profilování dat může shrnout a shromáždit obecné informace o naší datové sadě prostřednictvím technik popisné statistiky. Profilování dat nám pomáhá pochopit, co máme k dispozici, a popisná statistika nám pomáhá pochopit, kolik toho máme.

V několika předchozích lekcích jsme použili Pandas k poskytování popisné statistiky pomocí funkce [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Tato funkce poskytuje počet, maximální a minimální hodnoty, průměr, standardní odchylku a kvantily na číselných datech. Použití popisné statistiky, jako je funkce `describe()`, vám může pomoci posoudit, kolik dat máte a zda potřebujete více.

## Vzorkování a dotazování
Prozkoumávání všeho v rozsáhlé datové sadě může být velmi časově náročné a obvykle je to úkol, který je ponechán na počítači. Vzorkování je však užitečný nástroj pro pochopení dat a umožňuje nám lépe porozumět tomu, co datová sada obsahuje a co reprezentuje. Pomocí vzorku můžete aplikovat pravděpodobnost a statistiku, abyste dospěli k obecným závěrům o svých datech. I když neexistuje žádné pevně stanovené pravidlo, kolik dat byste měli vzorkovat, je důležité si uvědomit, že čím více dat vzorkujete, tím přesnější generalizaci můžete o datech učinit. 
Pandas má funkci [`sample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), kde můžete zadat argument, kolik náhodných vzorků chcete získat a použít.

Obecné dotazování na data vám může pomoci odpovědět na některé obecné otázky a teorie, které můžete mít. Na rozdíl od vzorkování vám dotazy umožňují mít kontrolu a zaměřit se na konkrétní části dat, na které máte otázky. 
Funkce [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) v knihovně Pandas vám umožňuje vybrat sloupce a získat jednoduché odpovědi o datech prostřednictvím získaných řádků.

## Prozkoumávání pomocí vizualizací
Nemusíte čekat, až budou data důkladně vyčištěna a analyzována, abyste mohli začít vytvářet vizualizace. Ve skutečnosti může vizuální reprezentace při prozkoumávání pomoci identifikovat vzory, vztahy a problémy v datech. Navíc vizualizace poskytují prostředek komunikace s těmi, kteří nejsou zapojeni do správy dat, a mohou být příležitostí k sdílení a objasnění dalších otázek, které nebyly řešeny ve fázi zachycení. Odkazujte na [sekci o vizualizacích](../../../../../../../../../3-Data-Visualization), kde se dozvíte více o některých populárních způsobech vizuálního prozkoumávání.

## Prozkoumávání za účelem identifikace nesrovnalostí
Všechny témata v této lekci mohou pomoci identifikovat chybějící nebo nekonzistentní hodnoty, ale Pandas poskytuje funkce, které mohou některé z nich zkontrolovat. [isna() nebo isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) mohou zkontrolovat chybějící hodnoty. Důležitou součástí prozkoumávání těchto hodnot ve vašich datech je zjistit, proč se tak stalo. To vám může pomoci rozhodnout, jaké [kroky podniknout k jejich vyřešení](../../../../../../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Úkol

[Prozkoumávání odpovědí](assignment.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.