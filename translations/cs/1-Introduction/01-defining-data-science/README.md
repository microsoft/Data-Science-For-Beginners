<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43212cc1ac137b7bb1dcfb37ca06b0f4",
  "translation_date": "2025-10-25T19:04:57+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "cs"
}
-->
# Definice datové vědy

| ![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------: |
|              Definice datové vědy - _Sketchnote od [@nitya](https://twitter.com/nitya)_               |

---

[![Video o definici datové vědy](../../../../translated_images/cs/video-def-ds.6623ee2392ef1abf6d7faf3fad10a4163642811749da75f44e35a5bb121de15c.png)](https://youtu.be/beZ7Mb_oz9I)

## [Kvíz před přednáškou](https://ff-quizzes.netlify.app/en/ds/quiz/0)

## Co jsou data?
V našem každodenním životě jsme neustále obklopeni daty. Text, který právě čtete, jsou data. Seznam telefonních čísel vašich přátel ve vašem chytrém telefonu jsou data, stejně jako aktuální čas zobrazený na vašich hodinkách. Jako lidé přirozeně pracujeme s daty, například když počítáme peníze nebo píšeme dopisy přátelům.

S příchodem počítačů však data získala mnohem větší význam. Hlavním úkolem počítačů je provádět výpočty, ale k tomu potřebují data. Proto je důležité pochopit, jak počítače data ukládají a zpracovávají.

S rozvojem internetu se role počítačů jako zařízení pro práci s daty ještě zvýšila. Když se nad tím zamyslíte, používáme počítače stále více pro zpracování a komunikaci dat než pro samotné výpočty. Když píšeme e-mail příteli nebo hledáme informace na internetu, v podstatě vytváříme, ukládáme, přenášíme a manipulujeme s daty.
> Pamatujete si, kdy jste naposledy použili počítač k provedení skutečného výpočtu?

## Co je datová věda?

Na [Wikipedii](https://en.wikipedia.org/wiki/Data_science) je **datová věda** definována jako *vědecký obor, který využívá vědecké metody k získávání znalostí a poznatků ze strukturovaných a nestrukturovaných dat a aplikuje tyto znalosti a praktické poznatky z dat v široké škále aplikačních oblastí*.

Tato definice zdůrazňuje následující důležité aspekty datové vědy:

* Hlavním cílem datové vědy je **získávání znalostí** z dat, jinými slovy - **porozumění** datům, hledání skrytých vztahů a vytváření **modelů**.
* Datová věda využívá **vědecké metody**, jako je pravděpodobnost a statistika. Když byl termín *datová věda* poprvé představen, někteří lidé tvrdili, že datová věda je jen nový módní název pro statistiku. Dnes je však zřejmé, že tento obor je mnohem širší.
* Získané znalosti by měly být aplikovány k vytvoření **praktických poznatků**, tedy praktických závěrů, které lze použít v reálných obchodních situacích.
* Měli bychom být schopni pracovat jak s **strukturovanými**, tak s **nestrukturovanými** daty. O různých typech dat budeme hovořit později v kurzu.
* **Aplikační oblast** je důležitý koncept, a datoví vědci často potřebují alespoň určitou míru odbornosti v dané problematice, například: finance, medicína, marketing atd.

> Dalším důležitým aspektem datové vědy je studium toho, jak lze data shromažďovat, ukládat a zpracovávat pomocí počítačů. Zatímco statistika nám poskytuje matematické základy, datová věda aplikuje matematické koncepty k získávání poznatků z dat.

Jedním ze způsobů (přisuzováno [Jimovi Grayovi](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) jak nahlížet na datovou vědu, je považovat ji za samostatný vědecký paradigmat:
* **Empirický**, kde se spoléháme především na pozorování a výsledky experimentů
* **Teoretický**, kde nové koncepty vycházejí z existujících vědeckých poznatků
* **Výpočetní**, kde objevujeme nové principy na základě výpočetních experimentů
* **Data-řízený**, založený na objevování vztahů a vzorců v datech  

## Další související obory

Protože data jsou všudypřítomná, datová věda je také široký obor, který se dotýká mnoha dalších disciplín.

<dl>
<dt>Databáze</dt>
<dd>
Klíčovým aspektem je <b>jak ukládat</b> data, tedy jak je strukturovat tak, aby bylo možné je rychleji zpracovávat. Existují různé typy databází, které ukládají strukturovaná a nestrukturovaná data, což <a href="../../2-Working-With-Data/README.md">probereme v našem kurzu</a>.
</dd>
<dt>Velká data</dt>
<dd>
Často potřebujeme ukládat a zpracovávat velmi velké množství dat s relativně jednoduchou strukturou. Existují speciální přístupy a nástroje, které umožňují ukládat tato data distribuovaným způsobem na clusteru počítačů a efektivně je zpracovávat.
</dd>
<dt>Strojové učení</dt>
<dd>
Jedním ze způsobů, jak porozumět datům, je <b>vytvořit model</b>, který bude schopen předpovídat požadovaný výsledek. Vývoj modelů z dat se nazývá <b>strojové učení</b>. Můžete se podívat na náš <a href="https://aka.ms/ml-beginners">kurz Strojové učení pro začátečníky</a>, abyste se o tom dozvěděli více.
</dd>
<dt>Umělá inteligence</dt>
<dd>
Oblast strojového učení známá jako umělá inteligence (AI) také spoléhá na data a zahrnuje vytváření vysoce komplexních modelů, které napodobují lidské myšlenkové procesy. Metody AI nám často umožňují převádět nestrukturovaná data (např. přirozený jazyk) na strukturované poznatky. 
</dd>
<dt>Vizualizace</dt>
<dd>
Obrovské množství dat je pro člověka nepochopitelné, ale jakmile vytvoříme užitečné vizualizace pomocí těchto dat, můžeme lépe porozumět datům a vyvodit závěry. Proto je důležité znát mnoho způsobů vizualizace informací - něco, co probereme v <a href="../../3-Data-Visualization/README.md">sekci 3</a> našeho kurzu. Související obory zahrnují také <b>infografiku</b> a obecně <b>interakci člověka s počítačem</b>. 
</dd>
</dl>

## Typy dat

Jak jsme již zmínili, data jsou všude. Stačí je jen správně zachytit! Je užitečné rozlišovat mezi **strukturovanými** a **nestrukturovanými** daty. Strukturovaná data jsou obvykle reprezentována v nějaké dobře strukturované formě, často jako tabulka nebo množství tabulek, zatímco nestrukturovaná data jsou pouze sbírkou souborů. Někdy můžeme také hovořit o **polo-strukturovaných** datech, která mají nějaký druh struktury, která se může značně lišit.

| Strukturovaná                                                               | Polo-strukturovaná                                                                           | Nestrukturovaná                        |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------- |
| Seznam lidí s jejich telefonními čísly                                      | Stránky Wikipedie s odkazy                                                                  | Text Encyklopedie Britannica           |
| Teplota ve všech místnostech budovy každou minutu za posledních 20 let      | Sbírka vědeckých článků ve formátu JSON s autory, datem publikace a abstraktem              | Sdílené soubory s firemními dokumenty  |
| Data o věku a pohlaví všech lidí vstupujících do budovy                     | Internetové stránky                                                                         | Surový videozáznam z bezpečnostní kamery |

## Kde získat data

Existuje mnoho možných zdrojů dat, a bylo by nemožné je všechny vyjmenovat! Nicméně zmíníme některá typická místa, kde můžete data získat:

* **Strukturovaná**
  - **Internet věcí** (IoT), včetně dat z různých senzorů, jako jsou teplotní nebo tlakové senzory, poskytuje mnoho užitečných dat. Například pokud je kancelářská budova vybavena IoT senzory, můžeme automaticky řídit vytápění a osvětlení, abychom minimalizovali náklady. 
  - **Průzkumy**, které žádáme uživatele vyplnit po nákupu nebo po návštěvě webové stránky.
  - **Analýza chování** nám může například pomoci pochopit, jak hluboko uživatel proniká na webovou stránku a jaký je typický důvod jejího opuštění.
* **Nestrukturovaná**
  - **Texty** mohou být bohatým zdrojem poznatků, jako je celkový **skóre sentimentu** nebo extrakce klíčových slov a sémantického významu.
  - **Obrázky** nebo **videa**. Video z bezpečnostní kamery může být použito k odhadu dopravní situace na silnici a informování lidí o možných dopravních zácpách.
  - **Logy** webových serverů mohou být použity k pochopení, které stránky našeho webu jsou nejčastěji navštěvovány a jak dlouho.
* Polo-strukturovaná
  - **Grafy sociálních sítí** mohou být skvělým zdrojem dat o osobnostech uživatelů a potenciální účinnosti šíření informací.
  - Když máme hromadu fotografií z večírku, můžeme se pokusit extrahovat data o **skupinové dynamice** vytvořením grafu lidí, kteří se fotili společně.

Pokud znáte různé možné zdroje dat, můžete přemýšlet o různých scénářích, kde lze aplikovat techniky datové vědy k lepšímu pochopení situace a zlepšení obchodních procesů. 

## Co můžete dělat s daty

V datové vědě se zaměřujeme na následující kroky datové cesty:

<dl>
<dt>1) Získávání dat</dt>
<dd>
Prvním krokem je sběr dat. Zatímco v mnoha případech to může být jednoduchý proces, například data přicházející do databáze z webové aplikace, někdy musíme použít speciální techniky. Například data ze senzorů IoT mohou být ohromující, a je dobré použít mezibufery, jako je IoT Hub, k jejich shromažďování před dalším zpracováním.
</dd>
<dt>2) Ukládání dat</dt>
<dd>
Ukládání dat může být náročné, zejména pokud mluvíme o velkých datech. Při rozhodování o způsobu ukládání dat má smysl předvídat, jak budete chtít data v budoucnu dotazovat. Existuje několik způsobů, jak lze data ukládat:
<ul>
<li>Relační databáze ukládá sbírku tabulek a používá speciální jazyk nazývaný SQL k jejich dotazování. Tabulky jsou obvykle organizovány do různých skupin nazývaných schémata. V mnoha případech musíme data převést z původní formy, aby odpovídala schématu.</li>
<li><a href="https://en.wikipedia.org/wiki/NoSQL">NoSQL</a> databáze, jako je <a href="https://azure.microsoft.com/services/cosmos-db/?WT.mc_id=academic-77958-bethanycheum">CosmosDB</a>, nevyžaduje schémata pro data a umožňuje ukládání složitějších dat, například hierarchických JSON dokumentů nebo grafů. Nicméně NoSQL databáze nemají tak bohaté možnosti dotazování jako SQL a nemohou vynucovat referenční integritu, tj. pravidla o tom, jak jsou data strukturována v tabulkách a jaké jsou vztahy mezi tabulkami.</li>
<li><a href="https://en.wikipedia.org/wiki/Data_lake">Úložiště datových jezer</a> se používá pro velké sbírky dat v surové, nestrukturované formě. Datová jezera se často používají s velkými daty, kde všechna data nemohou být uložena na jednom stroji a musí být uložena a zpracována clusterem serverů. <a href="https://en.wikipedia.org/wiki/Apache_Parquet">Parquet</a> je datový formát, který se často používá ve spojení s velkými daty.</li> 
</ul>
</dd>
<dt>3) Zpracování dat</dt>
<dd>
Toto je nejzajímavější část datové cesty, která zahrnuje převod dat z jejich původní formy do formy, která může být použita pro vizualizaci nebo trénink modelů. Při práci s nestrukturovanými daty, jako jsou texty nebo obrázky, můžeme potřebovat použít některé techniky AI k extrakci <b>vlastností</b> z dat, čímž je převedeme do strukturované formy.
</dd>
<dt>4) Vizualizace / Lidské poznatky</dt>
<dd>
Často, abychom porozuměli datům, je musíme vizualizovat. Díky mnoha různým technikám vizualizace můžeme najít správný pohled na data, který nám umožní získat poznatky. Často musí datový vědec "hrát si s daty", opakovaně je vizualizovat a hledat vztahy. Také můžeme použít statistické techniky k testování hypotéz nebo prokázání korelace mezi různými částmi dat.   
</dd>
<dt>5) Trénink prediktivního modelu</dt>
<dd>
Protože konečným cílem datové vědy je být schopen činit rozhodnutí na základě dat, můžeme chtít použít techniky <a href="http://github.com/microsoft/ml-for-beginners">strojového učení</a> k vytvoření prediktivního modelu. Ten pak můžeme použít k předpovědím na základě nových datových sad s podobnou strukturou.
</dd>
</dl>

Samozřejmě, v závislosti na skutečných datech mohou některé kroky chybět (např. když už máme data v databázi nebo když nepotřebujeme trénink modelu), nebo mohou být některé kroky opakovány několikrát (například zpracování dat).

## Digitalizace a digitální transformace

V posledním desetiletí mnoho podniků začalo chápat důležitost dat při rozhodování o podnikání. Aby bylo možné aplikovat principy datové vědy na řízení podniku, je nejprve nutné shromáždit nějaká data, tj. převést obchodní procesy do digitální podoby. To je známé jako **digitalizace**. Použití technik datové vědy na tato data k usměrnění rozhodování může vést k významnému zvýšení produktivity (nebo dokonce k zásadní změně podnikání), což se nazývá **digitální transformace**.

Uvažujme příklad. Představme si, že máme kurz datové vědy (jako je tento), který poskytujeme online studentům, a chceme použít datovou vědu k jeho zlepšení. Jak to můžeme udělat?

Můžeme začít otázkou "Co lze digitalizovat?" Nejjednodušší způsob by byl měřit čas, který každý student potřebuje k dokončení každého modulu, a měřit získané znalosti pomocí testu s výběrem odpovědí na konci každého modulu. Průměrováním času potřebného k dokončení mezi všemi studenty můžeme zjistit, které moduly způsobují studentům největší obtíže, a pracovat na jejich zjednodušení.
> Můžete namítnout, že tento přístup není ideální, protože moduly mohou mít různou délku. Pravděpodobně by bylo spravedlivější rozdělit čas podle délky modulu (v počtu znaků) a porovnat tyto hodnoty.

Když začneme analyzovat výsledky testů s výběrem odpovědí, můžeme se pokusit zjistit, které koncepty studentům dělají problémy, a využít tyto informace k vylepšení obsahu. Abychom toho dosáhli, musíme navrhnout testy tak, aby každá otázka odpovídala určitému konceptu nebo části znalostí.

Pokud se chceme pustit do ještě složitější analýzy, můžeme vykreslit čas potřebný k dokončení každého modulu v závislosti na věkové kategorii studentů. Můžeme zjistit, že některým věkovým kategoriím trvá nepřiměřeně dlouho dokončit modul, nebo že studenti odpadnou před jeho dokončením. To nám může pomoci doporučit vhodné věkové kategorie pro daný modul a minimalizovat nespokojenost lidí způsobenou nesprávnými očekáváními.

## 🚀 Výzva

V této výzvě se pokusíme najít koncepty relevantní pro oblast Data Science tím, že se podíváme na texty. Vezmeme článek z Wikipedie o Data Science, stáhneme a zpracujeme text, a poté vytvoříme slovní mrak, který bude vypadat takto:

![Slovní mrak pro Data Science](../../../../translated_images/cs/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.png)

Navštivte [`notebook.ipynb`](../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') a projděte si kód. Můžete také spustit kód a sledovat, jak provádí všechny transformace dat v reálném čase.

> Pokud nevíte, jak spustit kód v Jupyter Notebooku, podívejte se na [tento článek](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Úkoly

* **Úkol 1**: Upravte výše uvedený kód, abyste zjistili související koncepty pro oblasti **Big Data** a **Machine Learning**.
* **Úkol 2**: [Přemýšlejte o scénářích Data Science](assignment.md)

## Poděkování

Tuto lekci vytvořil s ♥️ [Dmitry Soshnikov](http://soshnikov.com)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.