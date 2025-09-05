<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "44de95649fcec43643cbe3962f904331",
  "translation_date": "2025-09-05T18:11:04+00:00",
  "source_file": "3-Data-Visualization/12-visualization-relationships/README.md",
  "language_code": "sk"
}
-->
# Vizualizácia vzťahov: Všetko o mede 🍯

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Vizualizácia vzťahov - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

Pokračujúc v našom výskume zameranom na prírodu, objavme zaujímavé vizualizácie, ktoré ukazujú vzťahy medzi rôznymi typmi medu podľa datasetu odvodeného od [Ministerstva poľnohospodárstva Spojených štátov](https://www.nass.usda.gov/About_NASS/index.php).

Tento dataset obsahuje približne 600 položiek a zobrazuje produkciu medu v mnohých štátoch USA. Napríklad môžete preskúmať počet kolónií, výnos na kolóniu, celkovú produkciu, zásoby, cenu za libru a hodnotu medu vyprodukovaného v danom štáte od roku 1998 do 2012, pričom každý riadok predstavuje jeden rok pre každý štát.

Bude zaujímavé vizualizovať vzťah medzi produkciou daného štátu za rok a napríklad cenou medu v tomto štáte. Alternatívne môžete vizualizovať vzťah medzi výnosom medu na kolóniu v jednotlivých štátoch. Toto časové obdobie zahŕňa ničivý fenomén 'CCD' alebo 'Colony Collapse Disorder', ktorý bol prvýkrát zaznamenaný v roku 2006 (http://npic.orst.edu/envir/ccd.html), takže ide o dojímavý dataset na štúdium. 🐝

## [Kvíz pred prednáškou](https://ff-quizzes.netlify.app/en/ds/quiz/22)

V tejto lekcii môžete použiť knižnicu Seaborn, ktorú ste už predtým používali, ako dobrý nástroj na vizualizáciu vzťahov medzi premennými. Obzvlášť zaujímavé je použitie funkcie `relplot` v Seaborne, ktorá umožňuje scatter ploty a line ploty na rýchlu vizualizáciu '[štatistických vzťahov](https://seaborn.pydata.org/tutorial/relational.html?highlight=relationships)', čo umožňuje dátovému analytikovi lepšie pochopiť, ako sa premenné navzájom ovplyvňujú.

## Scatterploty

Použite scatterplot na zobrazenie, ako sa cena medu vyvíjala rok po roku v jednotlivých štátoch. Seaborn, pomocou `relplot`, pohodlne zoskupuje údaje o štátoch a zobrazuje dátové body pre kategorizované aj numerické údaje.

Začnime importovaním dát a knižnice Seaborn:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
honey = pd.read_csv('../../data/honey.csv')
honey.head()
```
Všimnete si, že údaje o mede obsahujú niekoľko zaujímavých stĺpcov, vrátane roku a ceny za libru. Preskúmajme tieto údaje, zoskupené podľa štátov USA:

| štát | numcol | yieldpercol | totalprod | zásoby   | priceperlb | prodvalue | rok |
| ----- | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL    | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ    | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR    | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA    | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO    | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |

Vytvorte základný scatterplot na zobrazenie vzťahu medzi cenou za libru medu a jeho pôvodom v USA. Urobte os `y` dostatočne vysokú na zobrazenie všetkých štátov:

```python
sns.relplot(x="priceperlb", y="state", data=honey, height=15, aspect=.5);
```
![scatterplot 1](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter1.png)

Teraz zobrazte tie isté údaje s farebnou schémou medu, aby ste ukázali, ako sa cena vyvíja v priebehu rokov. Môžete to urobiť pridaním parametra 'hue', ktorý ukáže zmenu rok po roku:

> ✅ Viac sa dozviete o [farebných paletách, ktoré môžete použiť v Seaborne](https://seaborn.pydata.org/tutorial/color_palettes.html) - vyskúšajte krásnu dúhovú farebnú schému!

```python
sns.relplot(x="priceperlb", y="state", hue="year", palette="YlOrBr", data=honey, height=15, aspect=.5);
```
![scatterplot 2](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter2.png)

S touto zmenou farebnej schémy môžete vidieť, že existuje zjavný silný progres v priebehu rokov, pokiaľ ide o cenu medu za libru. Ak sa pozriete na vzorku údajov na overenie (vyberte si napríklad štát Arizona), môžete vidieť vzor zvyšovania cien rok po roku, s niekoľkými výnimkami:

| štát | numcol | yieldpercol | totalprod | zásoby  | priceperlb | prodvalue | rok |
| ----- | ------ | ----------- | --------- | ------- | ---------- | --------- | ---- |
| AZ    | 55000  | 60          | 3300000   | 1485000 | 0.64       | 2112000   | 1998 |
| AZ    | 52000  | 62          | 3224000   | 1548000 | 0.62       | 1999000   | 1999 |
| AZ    | 40000  | 59          | 2360000   | 1322000 | 0.73       | 1723000   | 2000 |
| AZ    | 43000  | 59          | 2537000   | 1142000 | 0.72       | 1827000   | 2001 |
| AZ    | 38000  | 63          | 2394000   | 1197000 | 1.08       | 2586000   | 2002 |
| AZ    | 35000  | 72          | 2520000   | 983000  | 1.34       | 3377000   | 2003 |
| AZ    | 32000  | 55          | 1760000   | 774000  | 1.11       | 1954000   | 2004 |
| AZ    | 36000  | 50          | 1800000   | 720000  | 1.04       | 1872000   | 2005 |
| AZ    | 30000  | 65          | 1950000   | 839000  | 0.91       | 1775000   | 2006 |
| AZ    | 30000  | 64          | 1920000   | 902000  | 1.26       | 2419000   | 2007 |
| AZ    | 25000  | 64          | 1600000   | 336000  | 1.26       | 2016000   | 2008 |
| AZ    | 20000  | 52          | 1040000   | 562000  | 1.45       | 1508000   | 2009 |
| AZ    | 24000  | 77          | 1848000   | 665000  | 1.52       | 2809000   | 2010 |
| AZ    | 23000  | 53          | 1219000   | 427000  | 1.55       | 1889000   | 2011 |
| AZ    | 22000  | 46          | 1012000   | 253000  | 1.79       | 1811000   | 2012 |

Ďalším spôsobom vizualizácie tohto progresu je použitie veľkosti namiesto farby. Pre používateľov s poruchou farebného vnímania to môže byť lepšia možnosť. Upraviť vizualizáciu tak, aby ukazovala nárast ceny zväčšením obvodu bodov:

```python
sns.relplot(x="priceperlb", y="state", size="year", data=honey, height=15, aspect=.5);
```
Vidíte, že veľkosť bodov sa postupne zväčšuje.

![scatterplot 3](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter3.png)

Je to jednoduchý prípad ponuky a dopytu? Kvôli faktorom, ako je klimatická zmena a kolaps kolónií, je rok po roku menej medu dostupného na kúpu, a preto cena stúpa?

Na objavenie korelácie medzi niektorými premennými v tomto datasete preskúmajme niektoré line charty.

## Line charty

Otázka: Je zjavný nárast ceny medu za libru rok po roku? Najjednoduchšie to zistíte vytvorením jedného line chartu:

```python
sns.relplot(x="year", y="priceperlb", kind="line", data=honey);
```
Odpoveď: Áno, s niektorými výnimkami okolo roku 2003:

![line chart 1](../../../../3-Data-Visualization/12-visualization-relationships/images/line1.png)

✅ Keďže Seaborn agreguje údaje okolo jednej línie, zobrazuje "viacero meraní pri každej hodnote x tým, že vykresľuje priemer a 95% interval spoľahlivosti okolo priemeru". [Zdroj](https://seaborn.pydata.org/tutorial/relational.html). Toto časovo náročné správanie môžete vypnúť pridaním `ci=None`.

Otázka: No, v roku 2003 môžeme tiež vidieť nárast zásob medu? Čo ak sa pozriete na celkovú produkciu rok po roku?

```python
sns.relplot(x="year", y="totalprod", kind="line", data=honey);
```

![line chart 2](../../../../3-Data-Visualization/12-visualization-relationships/images/line2.png)

Odpoveď: Nie úplne. Ak sa pozriete na celkovú produkciu, zdá sa, že v tomto konkrétnom roku skutočne vzrástla, aj keď všeobecne produkcia medu v týchto rokoch klesá.

Otázka: V tom prípade, čo mohlo spôsobiť nárast ceny medu okolo roku 2003?

Na objavenie tohto môžete preskúmať facet grid.

## Facet gridy

Facet gridy berú jednu vlastnosť vášho datasetu (v našom prípade môžete zvoliť 'rok', aby ste sa vyhli príliš veľkému počtu vytvorených gridov). Seaborn potom môže vytvoriť graf pre každý z týchto aspektov vašich zvolených x a y súradníc pre jednoduchšie vizuálne porovnanie. Vyniká rok 2003 v tomto type porovnania?

Vytvorte facet grid pokračovaním v používaní `relplot`, ako odporúča [dokumentácia Seaborn](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html?highlight=facetgrid#seaborn.FacetGrid).

```python
sns.relplot(
    data=honey, 
    x="yieldpercol", y="numcol",
    col="year", 
    col_wrap=3,
    kind="line"
```
V tejto vizualizácii môžete porovnať výnos na kolóniu a počet kolónií rok po roku, vedľa seba, s wrap nastaveným na 3 pre stĺpce:

![facet grid](../../../../3-Data-Visualization/12-visualization-relationships/images/facet.png)

Pre tento dataset nič zvláštne nevyniká, pokiaľ ide o počet kolónií a ich výnos, rok po roku a štát po štáte. Existuje iný spôsob, ako hľadať koreláciu medzi týmito dvoma premennými?

## Dvojité line ploty

Vyskúšajte multiline plot superponovaním dvoch lineplotov na seba, pomocou funkcie Seaborn 'despine' na odstránenie ich horných a pravých osí a použitia `ax.twinx` [odvodeného z Matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html). Twinx umožňuje grafu zdieľať os x a zobraziť dve osi y. Zobrazte výnos na kolóniu a počet kolónií, superponované:

```python
fig, ax = plt.subplots(figsize=(12,6))
lineplot = sns.lineplot(x=honey['year'], y=honey['numcol'], data=honey, 
                        label = 'Number of bee colonies', legend=False)
sns.despine()
plt.ylabel('# colonies')
plt.title('Honey Production Year over Year');

ax2 = ax.twinx()
lineplot2 = sns.lineplot(x=honey['year'], y=honey['yieldpercol'], ax=ax2, color="r", 
                         label ='Yield per colony', legend=False) 
sns.despine(right=False)
plt.ylabel('colony yield')
ax.figure.legend();
```
![superimposed plots](../../../../3-Data-Visualization/12-visualization-relationships/images/dual-line.png)

Aj keď nič výrazne nevyniká okolo roku 2003, umožňuje nám to ukončiť túto lekciu na trochu pozitívnejšiu poznámku: aj keď celkovo počet kolónií klesá, počet kolónií sa stabilizuje, aj keď ich výnos na kolóniu klesá.

Do toho, včely, do toho!

🐝❤️
## 🚀 Výzva

V tejto lekcii ste sa dozvedeli viac o iných využitiach scatterplotov a line gridov, vrátane facet gridov. Vyzvite sa na vytvorenie facet gridu pomocou iného datasetu, možno takého, ktorý ste použili pred týmito lekciami. Všimnite si, ako dlho trvá ich vytvorenie a ako musíte byť opatrní pri počte gridov, ktoré potrebujete vykresliť pomocou týchto techník.

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ds/quiz/23)

## Prehľad & Samoštúdium

Line ploty môžu byť jednoduché alebo pomerne zložité. Prečítajte si trochu viac v [dokumentácii Seaborn](https://seaborn.pydata.org/generated/seaborn.lineplot.html) o rôznych spôsoboch, akými ich môžete vytvoriť. Pokúste sa vylepšiť line charty, ktoré ste vytvorili v tejto lekcii, pomocou iných metód uvedených v dokumentácii.
## Zadanie

[Ponorte sa do úľa](assignment.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.