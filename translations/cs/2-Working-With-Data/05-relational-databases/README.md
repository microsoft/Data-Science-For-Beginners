<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80d80300002ef4e77cc7631d5904bd6e",
  "translation_date": "2025-10-25T19:04:37+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "cs"
}
-->
# Práce s daty: Relační databáze

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Práce s daty: Relační databáze - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

Je pravděpodobné, že jste v minulosti použili tabulkový procesor k ukládání informací. Měli jste sadu řádků a sloupců, kde řádky obsahovaly informace (nebo data) a sloupce popisovaly tyto informace (někdy nazývané metadata). Relační databáze je postavena na tomto základním principu sloupců a řádků v tabulkách, což vám umožňuje mít informace rozložené do více tabulek. To vám umožňuje pracovat s komplexnějšími daty, vyhnout se duplicitám a mít flexibilitu při zkoumání dat. Pojďme prozkoumat koncepty relační databáze.

## [Kvíz před přednáškou](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Vše začíná tabulkami

Relační databáze má jako svůj základ tabulky. Stejně jako u tabulkového procesoru je tabulka kolekcí sloupců a řádků. Řádek obsahuje data nebo informace, se kterými chceme pracovat, například název města nebo množství srážek. Sloupce popisují data, která ukládají.

Začněme naše zkoumání vytvořením tabulky pro ukládání informací o městech. Můžeme začít jejich názvem a zemí. Mohli byste to uložit do tabulky takto:

| Město    | Země          |
| -------- | ------------- |
| Tokio    | Japonsko      |
| Atlanta  | Spojené státy |
| Auckland | Nový Zéland   |

Všimněte si, že názvy sloupců **město**, **země** a **populace** popisují ukládaná data a každý řádek obsahuje informace o jednom městě.

## Nedostatky přístupu s jednou tabulkou

Je pravděpodobné, že výše uvedená tabulka vám připadá poměrně známá. Začněme přidávat další data do naší rozrůstající se databáze - roční srážky (v milimetrech). Zaměříme se na roky 2018, 2019 a 2020. Pokud bychom je přidali pro Tokio, mohlo by to vypadat nějak takto:

| Město | Země     | Rok  | Množství |
| ----- | -------- | ---- | -------- |
| Tokio | Japonsko | 2020 | 1690     |
| Tokio | Japonsko | 2019 | 1874     |
| Tokio | Japonsko | 2018 | 1445     |

Co si všimnete na naší tabulce? Možná si všimnete, že opakovaně duplikujeme název a zemi města. To by mohlo zabrat poměrně dost úložného prostoru a je to většinou zbytečné, protože Tokio má jen jedno jméno, které nás zajímá.

Dobře, zkusme něco jiného. Přidáme nové sloupce pro každý rok:

| Město    | Země          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokio    | Japonsko      | 1445 | 1874 | 1690 |
| Atlanta  | Spojené státy | 1779 | 1111 | 1683 |
| Auckland | Nový Zéland   | 1386 | 942  | 1176 |

I když se tím vyhneme duplikaci řádků, přináší to několik dalších problémů. Museli bychom upravit strukturu naší tabulky pokaždé, když přibude nový rok. Navíc, jak naše data rostou, mít roky jako sloupce by ztížilo jejich získávání a výpočty.

Proto potřebujeme více tabulek a vztahy mezi nimi. Rozdělením našich dat se můžeme vyhnout duplicitám a získat větší flexibilitu při práci s daty.

## Koncepty vztahů

Vraťme se k našim datům a určme, jak je chceme rozdělit. Víme, že chceme uložit název a zemi našich měst, takže to bude pravděpodobně nejlépe fungovat v jedné tabulce.

| Město    | Země          |
| -------- | ------------- |
| Tokio    | Japonsko      |
| Atlanta  | Spojené státy |
| Auckland | Nový Zéland   |

Ale než vytvoříme další tabulku, musíme zjistit, jak odkazovat na každé město. Potřebujeme nějakou formu identifikátoru, ID nebo (v technických termínech databáze) primární klíč. Primární klíč je hodnota používaná k identifikaci jednoho konkrétního řádku v tabulce. I když by to mohlo být založeno na samotné hodnotě (například bychom mohli použít název města), mělo by to být téměř vždy číslo nebo jiný identifikátor. Nechceme, aby se ID někdy změnilo, protože by to narušilo vztah. Ve většině případů je primární klíč nebo ID automaticky generované číslo.

> ✅ Primární klíč se často zkracuje jako PK

### města

| city_id | Město    | Země          |
| ------- | -------- | ------------- |
| 1       | Tokio    | Japonsko      |
| 2       | Atlanta  | Spojené státy |
| 3       | Auckland | Nový Zéland   |

> ✅ Všimněte si, že během této lekce používáme termíny "id" a "primární klíč" zaměnitelně. Tyto koncepty se vztahují i na DataFrames, které budete zkoumat později. DataFrames nepoužívají terminologii "primární klíč", nicméně si všimnete, že se chovají velmi podobně.

Po vytvoření naší tabulky měst uložíme srážky. Místo duplikování úplných informací o městě můžeme použít ID. Měli bychom také zajistit, aby nově vytvořená tabulka měla sloupec *id*, protože všechny tabulky by měly mít ID nebo primární klíč.

### srážky

| rainfall_id | city_id | Rok  | Množství |
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

Všimněte si sloupce **city_id** v nově vytvořené tabulce **srážky**. Tento sloupec obsahuje hodnoty, které odkazují na ID v tabulce **města**. V technických termínech relačních dat se tomu říká **cizí klíč**; je to primární klíč z jiné tabulky. Můžete si to jednoduše představit jako odkaz nebo ukazatel. **city_id** 1 odkazuje na Tokio.

> [!NOTE] 
> Cizí klíč se často zkracuje jako FK

## Získávání dat

S našimi daty rozdělenými do dvou tabulek se možná ptáte, jak je získat. Pokud používáme relační databázi, jako je MySQL, SQL Server nebo Oracle, můžeme použít jazyk nazvaný Structured Query Language nebo SQL. SQL (někdy vyslovováno jako "sequel") je standardní jazyk používaný k získávání a úpravě dat v relační databázi.

K získání dat používáte příkaz `SELECT`. V podstatě **vyberete** sloupce, které chcete zobrazit, **z** tabulky, ve které se nacházejí. Pokud byste chtěli zobrazit pouze názvy měst, mohli byste použít následující:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` je místo, kde uvádíte sloupce, a `FROM` je místo, kde uvádíte tabulky.

> [!NOTE] 
> Syntaxe SQL není citlivá na velikost písmen, což znamená, že `select` a `SELECT` znamenají totéž. Nicméně, v závislosti na typu databáze, kterou používáte, mohou být sloupce a tabulky citlivé na velikost písmen. Proto je nejlepší praxí vždy zacházet se vším v programování, jako by to bylo citlivé na velikost písmen. Při psaní SQL dotazů je běžnou konvencí psát klíčová slova velkými písmeny.

Výše uvedený dotaz zobrazí všechna města. Představme si, že bychom chtěli zobrazit pouze města na Novém Zélandu. Potřebujeme nějakou formu filtru. Klíčové slovo SQL pro toto je `WHERE`, neboli "kde něco platí".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Spojování dat

Doposud jsme získávali data z jedné tabulky. Nyní chceme spojit data z obou tabulek **města** a **srážky**. To se provádí *spojením* těchto tabulek. Efektivně vytvoříte spojení mezi dvěma tabulkami a přiřadíte hodnoty ze sloupce z každé tabulky.

V našem příkladu spojíme sloupec **city_id** v tabulce **srážky** se sloupcem **city_id** v tabulce **města**. Tím přiřadíme hodnoty srážek k jejich příslušnému městu. Typ spojení, který provedeme, se nazývá *vnitřní* spojení, což znamená, že pokud nějaké řádky neodpovídají žádnému z druhé tabulky, nebudou zobrazeny. V našem případě má každé město srážky, takže vše bude zobrazeno.

Pojďme získat údaje o srážkách za rok 2019 pro všechna naše města.

Uděláme to v krocích. Prvním krokem je spojení dat dohromady tím, že označíme sloupce pro spojení - **city_id**, jak bylo uvedeno výše.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Zvýraznili jsme dva sloupce, které chceme, a fakt, že chceme spojit tabulky dohromady podle **city_id**. Nyní můžeme přidat příkaz `WHERE`, abychom filtrovali pouze rok 2019.

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

## Shrnutí

Relační databáze jsou založeny na rozdělení informací mezi více tabulek, které se poté spojují zpět pro zobrazení a analýzu. To poskytuje vysokou míru flexibility při provádění výpočtů a jiných manipulacích s daty. Viděli jste základní koncepty relační databáze a jak provést spojení mezi dvěma tabulkami.

## 🚀 Výzva

Na internetu je k dispozici mnoho relačních databází. Můžete prozkoumat data pomocí dovedností, které jste se naučili výše.

## Kvíz po přednášce

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Opakování a samostudium

Na [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) je k dispozici několik zdrojů, které vám umožní pokračovat v objevování SQL a konceptů relačních databází.

- [Popis konceptů relačních dat](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Začínáme s dotazováním pomocí Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL je verze SQL)
- [Obsah SQL na Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Úkol

[Úkol - Název](assignment.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.