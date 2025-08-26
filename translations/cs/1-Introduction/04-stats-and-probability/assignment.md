<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01d1b493e8b51a6ebb42524f6b1bcfff",
  "translation_date": "2025-08-26T15:42:33+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/assignment.md",
  "language_code": "cs"
}
-->
# Malá studie o cukrovce

V tomto úkolu budeme pracovat s malým datovým souborem pacientů s cukrovkou, který je dostupný [zde](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

|   | VĚK | POHLAVÍ | BMI | TK | S1 | S2 | S3 | S4 | S5 | S6 | Y  |
|---|-----|---------|-----|----|----|----|----|----|----|----|----|
| 0 | 59 | 2 | 32.1 | 101. | 157 | 93.2 | 38.0 | 4. | 4.8598 | 87 | 151 |
| 1 | 48 | 1 | 21.6 | 87.0 | 183 | 103.2 | 70. | 3. | 3.8918 | 69 | 75 |
| 2 | 72 | 2 | 30.5 | 93.0 | 156 | 93.6 | 41.0 | 4.0 | 4. | 85 | 141 |
| ... | ... | ... | ... | ...| ...| ...| ...| ...| ...| ...| ... |

## Pokyny

* Otevřete [notebook s úkolem](assignment.ipynb) v prostředí jupyter notebooku
* Dokončete všechny úkoly uvedené v notebooku, konkrétně:
   * [ ] Vypočítejte průměrné hodnoty a rozptyl pro všechny hodnoty
   * [ ] Vytvořte boxploty pro BMI, TK a Y v závislosti na pohlaví
   * [ ] Jaké je rozložení proměnných Věk, Pohlaví, BMI a Y?
   * [ ] Otestujte korelaci mezi různými proměnnými a progresí onemocnění (Y)
   * [ ] Otestujte hypotézu, že míra progrese cukrovky se liší mezi muži a ženami
   
## Hodnocení

Vynikající | Přiměřené | Vyžaduje zlepšení
--- | --- | -- |
Všechny požadované úkoly jsou dokončeny, graficky znázorněny a vysvětleny | Většina úkolů je dokončena, chybí vysvětlení nebo závěry z grafů a/nebo získaných hodnot | Dokončeny jsou pouze základní úkoly, jako výpočet průměru/rozptylu a základní grafy, nejsou vyvozeny žádné závěry z dat

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.