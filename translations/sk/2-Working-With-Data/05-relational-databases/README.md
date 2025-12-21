<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T12:06:48+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "sk"
}
-->
# Práca s údajmi: Relačné databázy

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Práca s údajmi: Relačné databázy - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

Je pravdepodobné, že ste v minulosti používali tabuľkový procesor na ukladanie informácií. Mali ste súbor riadkov a stĺpcov, kde riadky obsahovali informácie (alebo údaje) a stĺpce popisovali informácie (niekedy nazývané metadáta). Relačná databáza je postavená na tomto základnom princípe stĺpcov a riadkov v tabuľkách, čo vám umožňuje mať informácie rozložené do viacerých tabuliek. To vám umožňuje pracovať s komplexnejšími údajmi, vyhnúť sa duplicite a mať flexibilitu v spôsobe, akým údaje skúmate. Poďme preskúmať koncepty relačnej databázy.

## [Prednáškový kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Všetko začína tabuľkami

Relačná databáza má vo svojom jadre tabuľky. Rovnako ako v tabuľkovom procesore, tabuľka je zbierka stĺpcov a riadkov. Riadok obsahuje údaje alebo informácie, s ktorými chceme pracovať, napríklad názov mesta alebo množstvo zrážok. Stĺpce popisujú údaje, ktoré ukladajú.

Začnime našu exploráciu vytvorením tabuľky na uloženie informácií o mestách. Môžeme začať ich názvom a krajinou. Môžete to uložiť do tabuľky nasledovne:

| Mesto    | Krajina       |
| -------- | ------------- |
| Tokio    | Japonsko      |
| Atlanta  | Spojené štáty |
| Auckland | Nový Zéland   |

Všimnite si názvy stĺpcov **mesto**, **krajina** a **populácia**, ktoré popisujú ukladané údaje, a každý riadok obsahuje informácie o jednom meste.

## Nedostatky prístupu s jednou tabuľkou

Je pravdepodobné, že vám vyššie uvedená tabuľka pripadá relatívne známa. Začnime pridávať ďalšie údaje do našej rastúcej databázy - ročné zrážky (v milimetroch). Zameriame sa na roky 2018, 2019 a 2020. Ak by sme ich pridali pre Tokio, mohlo by to vyzerať takto:

| Mesto | Krajina | Rok  | Množstvo |
| ----- | ------- | ---- | -------- |
| Tokio | Japonsko| 2020 | 1690     |
| Tokio | Japonsko| 2019 | 1874     |
| Tokio | Japonsko| 2018 | 1445     |

Čo si všimnete na našej tabuľke? Môžete si všimnúť, že opakovane duplikujeme názov a krajinu mesta. To by mohlo zaberať dosť miesta na ukladanie a je to väčšinou zbytočné mať viacero kópií. Napokon, Tokio má len jeden názov, o ktorý sa zaujímame.

Skúsme niečo iné. Pridajme nové stĺpce pre každý rok:

| Mesto    | Krajina       | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokio    | Japonsko      | 1445 | 1874 | 1690 |
| Atlanta  | Spojené štáty | 1779 | 1111 | 1683 |
| Auckland | Nový Zéland   | 1386 | 942  | 1176 |

Hoci sa tým vyhneme duplikácii riadkov, pridáva to niekoľko ďalších výziev. Museli by sme meniť štruktúru tabuľky vždy, keď príde nový rok. Navyše, keď naše údaje rastú, mať roky ako stĺpce sťaží získavanie a výpočty hodnôt.

Preto potrebujeme viacero tabuliek a vzťahov. Rozdelením údajov môžeme zabrániť duplicite a mať väčšiu flexibilitu v práci s údajmi.

## Koncepty vzťahov

Vráťme sa k našim údajom a rozhodnime sa, ako ich chceme rozdeliť. Vieme, že chceme uložiť názov a krajinu pre naše mestá, takže to pravdepodobne najlepšie funguje v jednej tabuľke.

| Mesto    | Krajina       |
| -------- | ------------- |
| Tokio    | Japonsko      |
| Atlanta  | Spojené štáty |
| Auckland | Nový Zéland   |

Pred vytvorením ďalšej tabuľky však musíme zistiť, ako budeme odkazovať na každé mesto. Potrebujeme nejaký identifikátor, ID alebo (v technických databázových termínoch) primárny kľúč. Primárny kľúč je hodnota používaná na identifikáciu jedného konkrétneho riadku v tabuľke. Hoci by to mohlo byť založené na hodnote samotnej (napríklad by sme mohli použiť názov mesta), malo by to byť takmer vždy číslo alebo iný identifikátor. Nechceme, aby sa ID niekedy zmenilo, pretože by to prerušilo vzťah. Vo väčšine prípadov bude primárny kľúč alebo ID automaticky generované číslo.

> ✅ Primárny kľúč sa často skracuje ako PK

### cities

| city_id | Mesto    | Krajina       |
| ------- | -------- | ------------- |
| 1       | Tokio    | Japonsko      |
| 2       | Atlanta  | Spojené štáty |
| 3       | Auckland | Nový Zéland   |

> ✅ V tejto lekcii budete vidieť, že pojmy "id" a "primárny kľúč" sa používajú zameniteľne. Tieto koncepty platia aj pre DataFrames, ktoré preskúmate neskôr. DataFrames nepoužívajú terminológiu "primárny kľúč", ale všimnete si, že sa správajú veľmi podobne.

Po vytvorení tabuľky miest uložme zrážky. Namiesto duplikovania úplných informácií o meste môžeme použiť ID. Mali by sme tiež zabezpečiť, aby novovytvorená tabuľka mala tiež stĺpec *id*, pretože všetky tabuľky by mali mať id alebo primárny kľúč.

### rainfall

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

Všimnite si stĺpec **city_id** v novo vytvorenej tabuľke **rainfall**. Tento stĺpec obsahuje hodnoty, ktoré odkazujú na ID v tabuľke **cities**. V technických relačných dátových termínoch sa to nazýva **cudzí kľúč**; je to primárny kľúč z inej tabuľky. Môžete si to jednoducho predstaviť ako odkaz alebo ukazovateľ. **city_id** 1 odkazuje na Tokio.

> [!NOTE]  
> Cudzí kľúč sa často skracuje ako FK

## Získavanie údajov

Keď máme údaje rozdelené do dvoch tabuliek, možno sa pýtate, ako ich získavame. Ak používame relačnú databázu ako MySQL, SQL Server alebo Oracle, môžeme použiť jazyk nazývaný Structured Query Language alebo SQL. SQL (niekedy vyslovované ako sequel) je štandardný jazyk používaný na získavanie a úpravu údajov v relačnej databáze.

Na získanie údajov používate príkaz `SELECT`. V jadre vyberiete stĺpce, ktoré chcete vidieť, **z** tabuľky, v ktorej sa nachádzajú. Ak by ste chceli zobraziť len názvy miest, mohli by ste použiť nasledovné:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` je miesto, kde vymenujete stĺpce, a `FROM` je miesto, kde vymenujete tabuľky.

> [!NOTE]  
> Syntax SQL nerozlišuje veľkosť písmen, takže `select` a `SELECT` znamenajú to isté. Avšak v závislosti od typu databázy môžu byť stĺpce a tabuľky citlivé na veľkosť písmen. Preto je najlepšou praxou vždy považovať všetko v programovaní za citlivé na veľkosť písmen. Pri písaní SQL dotazov je bežnou konvenciou písať kľúčové slová veľkými písmenami.

Vyššie uvedený dotaz zobrazí všetky mestá. Predstavme si, že chceme zobraziť len mestá na Novom Zélande. Potrebujeme nejaký filter. SQL kľúčové slovo pre to je `WHERE`, alebo "kde je niečo pravda".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Spájanie údajov

Doteraz sme získavali údaje z jednej tabuľky. Teraz chceme spojiť údaje z oboch tabuliek **cities** a **rainfall**. To sa robí ich *spojením*. V podstate vytvoríte spojenie medzi dvoma tabuľkami a zhodujete hodnoty zo stĺpca každej tabuľky.

V našom príklade zhodíme stĺpec **city_id** v tabuľke **rainfall** so stĺpcom **city_id** v tabuľke **cities**. Týmto priradíme hodnotu zrážok k príslušnému mestu. Typ spojenia, ktorý vykonáme, sa nazýva *inner* join, čo znamená, že ak sa nejaké riadky nezhodujú s ničím z druhej tabuľky, nebudú zobrazené. V našom prípade má každé mesto zrážky, takže všetko bude zobrazené.

Získajme zrážky za rok 2019 pre všetky naše mestá.

Urobíme to po krokoch. Prvým krokom je spojiť údaje tým, že určíme stĺpce pre spojenie - **city_id**, ako sme už zdôraznili.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Zvýraznili sme dva stĺpce, ktoré chceme, a fakt, že chceme spojiť tabuľky podľa **city_id**. Teraz môžeme pridať príkaz `WHERE` na filtrovanie len roku 2019.

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

Relačné databázy sú založené na rozdelení informácií medzi viaceré tabuľky, ktoré sa potom spájajú pre zobrazenie a analýzu. To poskytuje vysokú mieru flexibility na vykonávanie výpočtov a iné manipulácie s údajmi. Videli ste základné koncepty relačnej databázy a ako vykonať spojenie medzi dvoma tabuľkami.

## 🚀 Výzva

Na internete je k dispozícii množstvo relačných databáz. Môžete preskúmať údaje pomocou zručností, ktoré ste sa naučili vyššie.

## Post-prednáškový kvíz

## [Post-prednáškový kvíz](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Prehľad a samostatné štúdium

Na [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) je k dispozícii niekoľko zdrojov, ktoré vám umožnia pokračovať v skúmaní SQL a konceptov relačných databáz

- [Popísať koncepty relačných údajov](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Začať dotazovanie s Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL je verzia SQL)
- [Obsah SQL na Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Zadanie

[Zobrazenie údajov letiska](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->