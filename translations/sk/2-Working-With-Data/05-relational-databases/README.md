<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "870a0086adbc313a8eea5489bdcb2522",
  "translation_date": "2025-08-26T14:30:17+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "sk"
}
-->
# Práca s dátami: Relačné databázy

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Práca s dátami: Relačné databázy - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

Je pravdepodobné, že ste v minulosti používali tabuľkový procesor na ukladanie informácií. Mali ste sadu riadkov a stĺpcov, kde riadky obsahovali informácie (alebo dáta) a stĺpce opisovali tieto informácie (niekedy nazývané metadáta). Relačná databáza je postavená na tomto základnom princípe stĺpcov a riadkov v tabuľkách, čo vám umožňuje mať informácie rozdelené do viacerých tabuliek. To vám umožňuje pracovať so zložitejšími dátami, vyhnúť sa duplicite a mať flexibilitu pri skúmaní dát. Poďme preskúmať koncepty relačnej databázy.

## [Kvíz pred prednáškou](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Všetko začína tabuľkami

Relačná databáza má vo svojom jadre tabuľky. Rovnako ako v tabuľkovom procesore, tabuľka je zbierka stĺpcov a riadkov. Riadok obsahuje dáta alebo informácie, s ktorými chceme pracovať, ako napríklad názov mesta alebo množstvo zrážok. Stĺpce opisujú dáta, ktoré ukladajú.

Začnime našu analýzu vytvorením tabuľky na ukladanie informácií o mestách. Môžeme začať s ich názvom a krajinou. Mohli by ste to uložiť do tabuľky nasledovne:

| Mesto    | Krajina       |
| -------- | ------------- |
| Tokio    | Japonsko      |
| Atlanta  | Spojené štáty |
| Auckland | Nový Zéland   |

Všimnite si, že názvy stĺpcov **mesto**, **krajina** a **populácia** opisujú dáta, ktoré sa ukladajú, a každý riadok obsahuje informácie o jednom meste.

## Nedostatky prístupu s jednou tabuľkou

Je pravdepodobné, že vyššie uvedená tabuľka vám pripadá pomerne známa. Začnime pridávať ďalšie dáta do našej rozrastajúcej sa databázy - ročné zrážky (v milimetroch). Zameriame sa na roky 2018, 2019 a 2020. Ak by sme ich pridali pre Tokio, mohlo by to vyzerať takto:

| Mesto  | Krajina | Rok  | Množstvo |
| ------ | ------- | ---- | -------- |
| Tokio  | Japonsko| 2020 | 1690     |
| Tokio  | Japonsko| 2019 | 1874     |
| Tokio  | Japonsko| 2018 | 1445     |

Čo si všimnete na našej tabuľke? Možno si všimnete, že opakovane duplikujeme názov a krajinu mesta. To by mohlo zabrať dosť miesta na ukladanie a je to väčšinou zbytočné. Koniec koncov, Tokio má len jeden názov, ktorý nás zaujíma.

Dobre, skúsme niečo iné. Pridajme nové stĺpce pre každý rok:

| Mesto    | Krajina       | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokio    | Japonsko      | 1445 | 1874 | 1690 |
| Atlanta  | Spojené štáty | 1779 | 1111 | 1683 |
| Auckland | Nový Zéland   | 1386 | 942  | 1176 |

Aj keď sa týmto vyhneme duplikácii riadkov, pridáva to niekoľko ďalších výziev. Museli by sme upraviť štruktúru našej tabuľky zakaždým, keď pribudne nový rok. Navyše, ako naše dáta rastú, mať roky ako stĺpce by sťažilo získavanie a výpočty hodnôt.

Preto potrebujeme viacero tabuliek a vzťahy. Rozdelením našich dát sa môžeme vyhnúť duplicite a mať väčšiu flexibilitu pri práci s dátami.

## Koncepty vzťahov

Vráťme sa k našim dátam a určme, ako ich chceme rozdeliť. Vieme, že chceme ukladať názov a krajinu našich miest, takže to bude pravdepodobne najlepšie fungovať v jednej tabuľke.

| Mesto    | Krajina       |
| -------- | ------------- |
| Tokio    | Japonsko      |
| Atlanta  | Spojené štáty |
| Auckland | Nový Zéland   |

Ale predtým, než vytvoríme ďalšiu tabuľku, musíme zistiť, ako odkazovať na každé mesto. Potrebujeme nejakú formu identifikátora, ID alebo (v technických databázových termínoch) primárny kľúč. Primárny kľúč je hodnota používaná na identifikáciu jedného konkrétneho riadku v tabuľke. Aj keď by to mohlo byť založené na samotnej hodnote (mohli by sme napríklad použiť názov mesta), takmer vždy by to malo byť číslo alebo iný identifikátor. Nechceme, aby sa ID niekedy zmenilo, pretože by to narušilo vzťah. Vo väčšine prípadov je primárny kľúč alebo ID automaticky generované číslo.

> ✅ Primárny kľúč sa často skracuje ako PK

### mestá

| city_id | Mesto    | Krajina       |
| ------- | -------- | ------------- |
| 1       | Tokio    | Japonsko      |
| 2       | Atlanta  | Spojené štáty |
| 3       | Auckland | Nový Zéland   |

> ✅ Všimnite si, že počas tejto lekcie používame pojmy "id" a "primárny kľúč" zameniteľne. Tieto koncepty platia aj pre DataFrames, ktoré budete skúmať neskôr. DataFrames nepoužívajú terminológiu "primárny kľúč", avšak všimnete si, že sa správajú veľmi podobne.

S našou tabuľkou miest vytvorenou, uložme zrážky. Namiesto duplikovania úplných informácií o meste môžeme použiť ID. Mali by sme tiež zabezpečiť, aby novovytvorená tabuľka mala stĺpec *id*, pretože všetky tabuľky by mali mať ID alebo primárny kľúč.

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

Všimnite si stĺpec **city_id** v novovytvorenej tabuľke **zrážky**. Tento stĺpec obsahuje hodnoty, ktoré odkazujú na ID v tabuľke **mestá**. V technických termínoch relačných dát sa to nazýva **cudzí kľúč**; je to primárny kľúč z inej tabuľky. Môžete si to jednoducho predstaviť ako referenciu alebo ukazovateľ. **city_id** 1 odkazuje na Tokio.

> [!NOTE] Cudzí kľúč sa často skracuje ako FK

## Získavanie dát

S našimi dátami rozdelenými do dvoch tabuliek sa možno pýtate, ako ich získame. Ak používame relačnú databázu, ako je MySQL, SQL Server alebo Oracle, môžeme použiť jazyk nazývaný Structured Query Language alebo SQL. SQL (niekedy vyslovované ako "sequel") je štandardný jazyk používaný na získavanie a úpravu dát v relačnej databáze.

Na získanie dát použijete príkaz `SELECT`. V jeho jadre **vyberáte** stĺpce, ktoré chcete vidieť, **z** tabuľky, v ktorej sa nachádzajú. Ak by ste chceli zobraziť len názvy miest, mohli by ste použiť nasledujúce:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` je miesto, kde uvediete stĺpce, a `FROM` je miesto, kde uvediete tabuľky.

> [NOTE] Syntax SQL nie je citlivá na veľké a malé písmená, čo znamená, že `select` a `SELECT` znamenajú to isté. Avšak v závislosti od typu databázy, ktorú používate, môžu byť stĺpce a tabuľky citlivé na veľké a malé písmená. Preto je najlepšou praxou vždy zaobchádzať so všetkým v programovaní, akoby to bolo citlivé na veľké a malé písmená. Pri písaní SQL dotazov je bežnou konvenciou písať kľúčové slová veľkými písmenami.

Vyššie uvedený dotaz zobrazí všetky mestá. Predstavme si, že chceme zobraziť iba mestá na Novom Zélande. Potrebujeme nejakú formu filtra. Kľúčové slovo SQL pre toto je `WHERE`, alebo "kde niečo platí".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Spájanie dát

Doteraz sme získavali dáta z jednej tabuľky. Teraz chceme spojiť dáta z tabuliek **mestá** a **zrážky**. Toto sa robí pomocou *spájania* (join). V podstate vytvoríte spoj medzi dvoma tabuľkami a priradíte hodnoty zo stĺpca z každej tabuľky.

V našom príklade priradíme stĺpec **city_id** v tabuľke **zrážky** so stĺpcom **city_id** v tabuľke **mestá**. Týmto spôsobom priradíme hodnotu zrážok k príslušnému mestu. Typ spojenia, ktoré vykonáme, sa nazýva *vnútorné spojenie* (inner join), čo znamená, že akékoľvek riadky, ktoré sa nezhodujú s ničím z druhej tabuľky, nebudú zobrazené. V našom prípade má každé mesto zrážky, takže všetko bude zobrazené.

Získajme zrážky za rok 2019 pre všetky naše mestá.

Budeme to robiť v krokoch. Prvým krokom je spojiť dáta dohromady uvedením stĺpcov pre spojenie - **city_id**, ako sme už spomenuli.

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

Relačné databázy sú založené na rozdelení informácií medzi viaceré tabuľky, ktoré sa potom spájajú na zobrazenie a analýzu. To poskytuje vysokú mieru flexibility na vykonávanie výpočtov a iné manipulácie s dátami. Videli ste základné koncepty relačnej databázy a ako vykonať spojenie medzi dvoma tabuľkami.

## 🚀 Výzva

Na internete je k dispozícii množstvo relačných databáz. Môžete preskúmať dáta pomocou zručností, ktoré ste sa naučili vyššie.

## Kvíz po prednáške

## [Kvíz po prednáške](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/9)

## Prehľad a samoštúdium

Na [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) je k dispozícii niekoľko zdrojov, ktoré vám umožnia pokračovať v skúmaní SQL a konceptov relačných databáz.

- [Popis konceptov relačných dát](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Začnite s dotazovaním pomocou Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL je verzia SQL)
- [Obsah SQL na Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Zadanie

[Zadanie](assignment.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby na automatický preklad [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.