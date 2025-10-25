<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80d80300002ef4e77cc7631d5904bd6e",
  "translation_date": "2025-10-25T19:05:29+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "sk"
}
-->
# Práca s dátami: Relačné databázy

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Práca s dátami: Relačné databázy - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

Je pravdepodobné, že ste už niekedy používali tabuľkový procesor na ukladanie informácií. Mali ste sadu riadkov a stĺpcov, kde riadky obsahovali informácie (alebo dáta) a stĺpce opisovali tieto informácie (niekedy nazývané metadáta). Relačná databáza je postavená na tomto základnom princípe stĺpcov a riadkov v tabuľkách, čo vám umožňuje mať informácie rozložené do viacerých tabuliek. To vám umožňuje pracovať s komplexnejšími dátami, vyhnúť sa duplicite a mať flexibilitu pri skúmaní dát. Poďme preskúmať koncepty relačnej databázy.

## [Kvíz pred prednáškou](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Všetko začína tabuľkami

Relačná databáza má vo svojom jadre tabuľky. Rovnako ako v tabuľkovom procesore, tabuľka je zbierka stĺpcov a riadkov. Riadok obsahuje dáta alebo informácie, s ktorými chceme pracovať, ako napríklad názov mesta alebo množstvo zrážok. Stĺpce opisujú dáta, ktoré uchovávajú.

Začnime našu analýzu vytvorením tabuľky na ukladanie informácií o mestách. Môžeme začať s ich názvom a krajinou. Mohli by ste to uložiť do tabuľky nasledovne:

| Mesto    | Krajina       |
| -------- | ------------- |
| Tokio    | Japonsko      |
| Atlanta  | Spojené štáty |
| Auckland | Nový Zéland   |

Všimnite si, že názvy stĺpcov **mesto**, **krajina** a **populácia** opisujú uchovávané dáta a každý riadok obsahuje informácie o jednom meste.

## Nedostatky prístupu s jednou tabuľkou

Je pravdepodobné, že vyššie uvedená tabuľka vám pripadá pomerne známa. Začnime pridávať ďalšie údaje do našej rozvíjajúcej sa databázy - ročné zrážky (v milimetroch). Zameriame sa na roky 2018, 2019 a 2020. Ak by sme ich pridali pre Tokio, mohlo by to vyzerať takto:

| Mesto | Krajina | Rok  | Množstvo |
| ----- | ------- | ---- | -------- |
| Tokio | Japonsko| 2020 | 1690     |
| Tokio | Japonsko| 2019 | 1874     |
| Tokio | Japonsko| 2018 | 1445     |

Čo si všimnete na našej tabuľke? Možno si všimnete, že opakovane duplikujeme názov a krajinu mesta. To by mohlo zabrať dosť veľa úložného priestoru a je to vo veľkej miere zbytočné, pretože Tokio má len jeden názov, ktorý nás zaujíma.

Dobre, skúsme niečo iné. Pridajme nové stĺpce pre každý rok:

| Mesto    | Krajina       | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokio    | Japonsko      | 1445 | 1874 | 1690 |
| Atlanta  | Spojené štáty | 1779 | 1111 | 1683 |
| Auckland | Nový Zéland   | 1386 | 942  | 1176 |

Aj keď sa tým vyhneme duplicite riadkov, prináša to niekoľko ďalších výziev. Museli by sme upraviť štruktúru našej tabuľky vždy, keď pribudne nový rok. Navyše, ako naše dáta rastú, mať roky ako stĺpce by mohlo sťažiť ich vyhľadávanie a výpočty.

Preto potrebujeme viacero tabuliek a vzťahy medzi nimi. Rozdelením našich dát sa môžeme vyhnúť duplicite a získať väčšiu flexibilitu pri práci s dátami.

## Koncepty vzťahov

Vráťme sa k našim dátam a určme, ako ich chceme rozdeliť. Vieme, že chceme uchovávať názov a krajinu našich miest, takže to bude pravdepodobne najlepšie fungovať v jednej tabuľke.

| Mesto    | Krajina       |
| -------- | ------------- |
| Tokio    | Japonsko      |
| Atlanta  | Spojené štáty |
| Auckland | Nový Zéland   |

Ale predtým, než vytvoríme ďalšiu tabuľku, musíme zistiť, ako odkazovať na každé mesto. Potrebujeme nejakú formu identifikátora, ID alebo (v technických databázových termínoch) primárny kľúč. Primárny kľúč je hodnota používaná na identifikáciu jedného konkrétneho riadku v tabuľke. Aj keď by to mohlo byť založené na samotnej hodnote (napríklad by sme mohli použiť názov mesta), takmer vždy by to malo byť číslo alebo iný identifikátor. Nechceme, aby sa ID niekedy zmenilo, pretože by to narušilo vzťah. Vo väčšine prípadov je primárny kľúč alebo ID automaticky generované číslo.

> ✅ Primárny kľúč sa často skracuje ako PK

### mestá

| city_id | Mesto    | Krajina       |
| ------- | -------- | ------------- |
| 1       | Tokio    | Japonsko      |
| 2       | Atlanta  | Spojené štáty |
| 3       | Auckland | Nový Zéland   |

> ✅ Všimnite si, že počas tejto lekcie používame pojmy "id" a "primárny kľúč" zameniteľne. Tieto koncepty sa vzťahujú aj na DataFrames, ktoré budete skúmať neskôr. DataFrames nepoužívajú terminológiu "primárny kľúč", avšak všimnete si, že sa správajú veľmi podobne.

Keď sme vytvorili tabuľku miest, uložme zrážky. Namiesto duplikovania úplných informácií o meste môžeme použiť ID. Mali by sme tiež zabezpečiť, aby novovytvorená tabuľka mala stĺpec *id*, pretože všetky tabuľky by mali mať ID alebo primárny kľúč.

### zrážky

| rainfall_id | city_id | Rok  | Množstvo |
| ----------- | ------- | ---- | -------- |
| 1           | 1       | 2018 | 1445     |
| 2           | 1       | 2019 | 1874     |
| 3           | 1       | 2020 | 1690     |
| 4           | 2       | 2018 | 1779     |
| 5           | 2       | 2019 | 1111     |
| 6           | 2       | 2020 | 1683     |
| 7           | 3       | 2018 | 1386     |
| 8           | 3       | 2019 | 942      |
| 9           | 3       | 2020 | 1176     |

Všimnite si stĺpec **city_id** v novo vytvorenej tabuľke **zrážky**. Tento stĺpec obsahuje hodnoty, ktoré odkazujú na ID v tabuľke **mestá**. V technických termínoch relačných dát sa to nazýva **cudzí kľúč**; je to primárny kľúč z inej tabuľky. Môžete si to jednoducho predstaviť ako odkaz alebo ukazovateľ. **city_id** 1 odkazuje na Tokio.

> [!NOTE] 
> Cudzí kľúč sa často skracuje ako FK

## Získavanie dát

S našimi dátami rozdelenými do dvoch tabuliek sa možno pýtate, ako ich získať. Ak používame relačnú databázu, ako je MySQL, SQL Server alebo Oracle, môžeme použiť jazyk nazývaný Structured Query Language alebo SQL. SQL (niekedy vyslovované ako "sequel") je štandardný jazyk používaný na získavanie a úpravu dát v relačnej databáze.

Na získanie dát používate príkaz `SELECT`. V podstate **vyberáte** stĺpce, ktoré chcete vidieť **z** tabuľky, v ktorej sa nachádzajú. Ak by ste chceli zobraziť iba názvy miest, mohli by ste použiť nasledujúci príkaz:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` je miesto, kde uvádzate stĺpce, a `FROM` je miesto, kde uvádzate tabuľky.

> [!NOTE] 
> Syntax SQL nie je citlivá na veľkosť písmen, čo znamená, že `select` a `SELECT` znamenajú to isté. Avšak v závislosti od typu databázy, ktorú používate, môžu byť stĺpce a tabuľky citlivé na veľkosť písmen. Preto je najlepšou praxou vždy zaobchádzať so všetkým v programovaní, akoby to bolo citlivé na veľkosť písmen. Pri písaní SQL dotazov je bežné používať kľúčové slová veľkými písmenami.

Vyššie uvedený dotaz zobrazí všetky mestá. Predstavme si, že chceme zobraziť iba mestá na Novom Zélande. Potrebujeme nejakú formu filtra. Kľúčové slovo SQL pre toto je `WHERE`, alebo "kde niečo platí".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Spájanie dát

Doteraz sme získavali dáta z jednej tabuľky. Teraz chceme spojiť dáta z oboch tabuliek **mestá** a **zrážky**. To sa robí *spojením* týchto tabuliek. V podstate vytvoríte spojenie medzi dvoma tabuľkami a priradíte hodnoty zo stĺpca z každej tabuľky.

V našom príklade priradíme stĺpec **city_id** v **zrážkach** so stĺpcom **city_id** v **mestách**. Týmto spôsobom priradíme hodnotu zrážok k príslušnému mestu. Typ spojenia, ktoré vykonáme, sa nazýva *vnútorné* spojenie, čo znamená, že akékoľvek riadky, ktoré sa nezhodujú s ničím z druhej tabuľky, nebudú zobrazené. V našom prípade má každé mesto zrážky, takže všetko bude zobrazené.

Získajme zrážky za rok 2019 pre všetky naše mestá.

Urobíme to v krokoch. Prvým krokom je spojenie dát tým, že označíme stĺpce pre spojenie - **city_id**, ako sme už spomenuli.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Zvýraznili sme dva stĺpce, ktoré chceme, a fakt, že chceme spojiť tabuľky pomocou **city_id**. Teraz môžeme pridať príkaz `WHERE`, aby sme filtrovali iba rok 2019.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
WHERE rainfall.year = 2019

-- Output

-- city     | amount
-- -------- | ------
-- Tokyo    | 1874
-- Atlanta  | 1111
-- Auckland |  942
```

## Zhrnutie

Relačné databázy sú založené na rozdelení informácií medzi viaceré tabuľky, ktoré sa potom spájajú späť na zobrazenie a analýzu. To poskytuje vysoký stupeň flexibility na vykonávanie výpočtov a iné manipulácie s dátami. Videli ste základné koncepty relačnej databázy a ako vykonať spojenie medzi dvoma tabuľkami.

## 🚀 Výzva

Na internete je dostupných množstvo relačných databáz. Môžete preskúmať dáta pomocou zručností, ktoré ste sa naučili vyššie.

## Kvíz po prednáške

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Prehľad a samostatné štúdium

Na [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) je k dispozícii niekoľko zdrojov, ktoré vám umožnia pokračovať v skúmaní konceptov SQL a relačných databáz.

- [Popis konceptov relačných dát](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Začnite s dotazovaním pomocou Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL je verzia SQL)
- [Obsah SQL na Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Zadanie

[Zadanie](assignment.md)

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.