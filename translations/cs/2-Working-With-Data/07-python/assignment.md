<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-26T14:51:30+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "cs"
}
-->
# Zadání pro zpracování dat v Pythonu

V tomto zadání vás požádáme, abyste rozpracovali kód, který jsme začali vyvíjet v našich výzvách. Zadání se skládá ze dvou částí:

## Modelování šíření COVID-19

 - [ ] Vykreslete grafy *R* pro 5-6 různých zemí na jednom grafu pro porovnání, nebo použijte několik grafů vedle sebe.
 - [ ] Zjistěte, jak počet úmrtí a uzdravení koreluje s počtem nakažených případů.
 - [ ] Zjistěte, jak dlouho obvykle nemoc trvá, vizuálním porovnáním míry infekce a míry úmrtí a hledáním některých anomálií. Možná budete muset zkoumat různé země, abyste to zjistili.
 - [ ] Vypočítejte míru úmrtnosti a jak se mění v čase. *Možná budete chtít vzít v úvahu délku nemoci v dnech a posunout jednu časovou řadu před provedením výpočtů.*

## Analýza článků o COVID-19

- [ ] Vytvořte matici společného výskytu různých léků a zjistěte, které léky se často vyskytují společně (tj. jsou zmíněny v jednom abstraktu). Můžete upravit kód pro vytvoření matice společného výskytu léků a diagnóz.
- [ ] Vizualizujte tuto matici pomocí heatmapy.
- [ ] Jako rozšiřující úkol vizualizujte společný výskyt léků pomocí [chord diagramu](https://en.wikipedia.org/wiki/Chord_diagram). [Tato knihovna](https://pypi.org/project/chord/) vám může pomoci nakreslit chord diagram.
- [ ] Jako další rozšiřující úkol extrahujte dávkování různých léků (například **400mg** ve větě *užívejte 400mg chlorochinu denně*) pomocí regulárních výrazů a vytvořte dataframe, který ukazuje různá dávkování pro různé léky. **Poznámka**: zvažte číselné hodnoty, které se nacházejí v blízkém textovém okolí názvu léku.

## Hodnocení

Vynikající | Přiměřené | Potřebuje zlepšení
--- | --- | -- |
Všechny úkoly jsou splněny, graficky znázorněny a vysvětleny, včetně alespoň jednoho ze dvou rozšiřujících úkolů | Více než 5 úkolů je splněno, žádné rozšiřující úkoly nejsou pokuseny, nebo výsledky nejsou jasné | Méně než 5 (ale více než 3) úkolů je splněno, vizualizace nepomáhají demonstrovat pointu

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.