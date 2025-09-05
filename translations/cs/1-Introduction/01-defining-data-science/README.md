<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a0516588d172f82f35f7a0d4a001e5d0",
  "translation_date": "2025-09-05T17:56:47+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "cs"
}
-->
## Typy dat

Jak jsme již zmínili, data jsou všude kolem nás. Stačí je jen správně zachytit! Je užitečné rozlišovat mezi **strukturovanými** a **nestrukturovanými** daty. Strukturovaná data jsou obvykle reprezentována v dobře organizované formě, často jako tabulka nebo množina tabulek, zatímco nestrukturovaná data jsou jen sbírkou souborů. Někdy můžeme také mluvit o **polostrukturovaných** datech, která mají určitý druh struktury, jež se může značně lišit.

| Strukturovaná                                                               | Polostrukturovaná                                                                             | Nestrukturovaná                        |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------- |
| Seznam lidí s jejich telefonními čísly                                      | Stránky Wikipedie s odkazy                                                                    | Text Encyklopedie Britannica           |
| Teplota ve všech místnostech budovy každou minutu za posledních 20 let       | Sbírka vědeckých článků ve formátu JSON s autory, datem publikace a abstraktem                | Sdílené soubory s firemními dokumenty  |
| Data o věku a pohlaví všech lidí vstupujících do budovy                      | Internetové stránky                                                                           | Surový videozáznam z bezpečnostní kamery |

## Kde získat data

Existuje mnoho možných zdrojů dat, a je nemožné je všechny vyjmenovat! Nicméně zmíníme některé typické místa, kde můžete data získat:

* **Strukturovaná**
  - **Internet věcí** (IoT), včetně dat z různých senzorů, jako jsou senzory teploty nebo tlaku, poskytuje mnoho užitečných dat. Například pokud je kancelářská budova vybavena IoT senzory, můžeme automaticky řídit vytápění a osvětlení, abychom minimalizovali náklady.
  - **Dotazníky**, které žádáme uživatele vyplnit po nákupu nebo po návštěvě webové stránky.
  - **Analýza chování** nám může například pomoci pochopit, jak hluboko uživatel proniká na web, a jaký je typický důvod jeho odchodu.
* **Nestrukturovaná**
  - **Texty** mohou být bohatým zdrojem poznatků, jako je celkový **skóre sentimentu** nebo extrakce klíčových slov a sémantického významu.
  - **Obrázky** nebo **video**. Video z bezpečnostní kamery může být použito k odhadu provozu na silnici a informování lidí o možných dopravních zácpách.
  - **Logy** webových serverů mohou být použity k pochopení, které stránky našeho webu jsou nejčastěji navštěvovány a jak dlouho.
* **Polostrukturovaná**
  - **Grafy sociálních sítí** mohou být skvělým zdrojem dat o osobnostech uživatelů a potenciální efektivitě šíření informací.
  - Když máme sbírku fotografií z večírku, můžeme se pokusit extrahovat data o **skupinové dynamice** vytvořením grafu lidí, kteří se fotili spolu.

Pokud znáte různé možné zdroje dat, můžete přemýšlet o různých scénářích, kde lze aplikovat techniky datové vědy k lepšímu pochopení situace a zlepšení obchodních procesů.

## Co můžete dělat s daty

V datové vědě se zaměřujeme na následující kroky práce s daty:

Samozřejmě, v závislosti na konkrétních datech mohou některé kroky chybět (např. když už máme data v databázi nebo když nepotřebujeme trénovat model), nebo mohou být některé kroky opakovány několikrát (například zpracování dat).

## Digitalizace a digitální transformace

V posledním desetiletí mnoho podniků začalo chápat důležitost dat při rozhodování. Aby bylo možné aplikovat principy datové vědy na řízení podniku, je nejprve nutné shromáždit nějaká data, tj. převést obchodní procesy do digitální podoby. To se nazývá **digitalizace**. Použití technik datové vědy na tato data k usměrnění rozhodování může vést k významnému zvýšení produktivity (nebo dokonce k zásadní změně podnikání), což se nazývá **digitální transformace**.

Podívejme se na příklad. Představme si, že máme kurz datové vědy (jako je tento), který poskytujeme online studentům, a chceme jej pomocí datové vědy zlepšit. Jak to můžeme udělat?

Můžeme začít otázkou „Co lze digitalizovat?“ Nejjednodušší způsob by byl měřit čas, který každý student potřebuje k dokončení každého modulu, a měřit získané znalosti pomocí testu s výběrem odpovědí na konci každého modulu. Průměrováním času potřebného k dokončení mezi všemi studenty můžeme zjistit, které moduly studentům způsobují největší potíže, a pracovat na jejich zjednodušení.
Můžete namítnout, že tento přístup není ideální, protože moduly mohou mít různou délku. Pravděpodobně by bylo spravedlivější rozdělit čas podle délky modulu (v počtu znaků) a porovnat tyto hodnoty místo toho.
Když začneme analyzovat výsledky testů s výběrem odpovědí, můžeme se pokusit zjistit, které koncepty dělají studentům problémy, a využít tyto informace k vylepšení obsahu. Abychom toho dosáhli, musíme navrhnout testy tak, aby každá otázka odpovídala určitému konceptu nebo části znalostí.

Pokud chceme být ještě složitější, můžeme vykreslit čas potřebný na dokončení každého modulu proti věkové kategorii studentů. Můžeme zjistit, že pro některé věkové kategorie trvá nepřiměřeně dlouho dokončit modul, nebo že studenti modul opouštějí před jeho dokončením. To nám může pomoci poskytnout věková doporučení pro modul a minimalizovat nespokojenost lidí z nesprávných očekávání.

## 🚀 Výzva

V této výzvě se pokusíme najít koncepty relevantní pro oblast Data Science tím, že se podíváme na texty. Vezmeme článek z Wikipedie o Data Science, stáhneme a zpracujeme text a poté vytvoříme slovní mrak, jako je tento:

![Slovní mrak pro Data Science](../../../../1-Introduction/01-defining-data-science/images/ds_wordcloud.png)

Navštivte [`notebook.ipynb`](../../../../../../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') a projděte si kód. Můžete také spustit kód a sledovat, jak provádí všechny transformace dat v reálném čase.

> Pokud nevíte, jak spustit kód v Jupyter Notebooku, podívejte se na [tento článek](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Úkoly

* **Úkol 1**: Upravte výše uvedený kód, abyste zjistili související koncepty pro oblasti **Big Data** a **Machine Learning**
* **Úkol 2**: [Přemýšlejte o scénářích Data Science](assignment.md)

## Poděkování

Tuto lekci vytvořil s ♥️ [Dmitry Soshnikov](http://soshnikov.com)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.