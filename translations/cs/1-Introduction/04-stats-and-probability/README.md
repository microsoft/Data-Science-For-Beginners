<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8bbb3fa0d4ad61384a3b4b5f7560226f",
  "translation_date": "2025-09-04T21:48:00+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/README.md",
  "language_code": "cs"
}
-->
# Stručný úvod do statistiky a pravděpodobnosti

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/04-Statistics-Probability.png)|
|:---:|
| Statistika a pravděpodobnost - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

Teorie statistiky a pravděpodobnosti jsou dvě úzce propojené oblasti matematiky, které mají velký význam pro datovou vědu. S daty lze pracovat i bez hlubokých znalostí matematiky, ale je lepší znát alespoň základní koncepty. Zde vám představíme krátký úvod, který vám pomůže začít.

[![Úvodní video](../../../../1-Introduction/04-stats-and-probability/images/video-prob-and-stats.png)](https://youtu.be/Z5Zy85g4Yjw)

## [Kvíz před přednáškou](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/6)

## Pravděpodobnost a náhodné proměnné

**Pravděpodobnost** je číslo mezi 0 a 1, které vyjadřuje, jak pravděpodobný je určitý **jev**. Definuje se jako počet pozitivních výsledků (které vedou k danému jevu) dělený celkovým počtem výsledků, za předpokladu, že všechny výsledky jsou stejně pravděpodobné. Například při hodu kostkou je pravděpodobnost, že padne sudé číslo, 3/6 = 0,5.

Když mluvíme o jevech, používáme **náhodné proměnné**. Například náhodná proměnná, která představuje číslo získané při hodu kostkou, nabývá hodnot od 1 do 6. Množina čísel od 1 do 6 se nazývá **prostor výsledků**. Můžeme hovořit o pravděpodobnosti, že náhodná proměnná nabude určité hodnoty, například P(X=3)=1/6.

Náhodná proměnná v předchozím příkladu se nazývá **diskrétní**, protože má spočetný prostor výsledků, tj. existují oddělené hodnoty, které lze vyjmenovat. Existují však případy, kdy je prostor výsledků interval reálných čísel nebo celá množina reálných čísel. Takové proměnné se nazývají **spojité**. Dobrým příkladem je čas příjezdu autobusu.

## Pravděpodobnostní rozdělení

V případě diskrétních náhodných proměnných je snadné popsat pravděpodobnost každého jevu pomocí funkce P(X). Pro každou hodnotu *s* z prostoru výsledků *S* poskytne číslo mezi 0 a 1 tak, že součet všech hodnot P(X=s) pro všechny jevy bude 1.

Nejznámější diskrétní rozdělení je **rovnoměrné rozdělení**, kde prostor výsledků obsahuje N prvků, přičemž pravděpodobnost každého z nich je 1/N.

Popis pravděpodobnostního rozdělení spojité proměnné, jejíž hodnoty pocházejí z nějakého intervalu [a,b] nebo celé množiny reálných čísel ℝ, je složitější. Uvažujme například čas příjezdu autobusu. Ve skutečnosti je pravděpodobnost, že autobus přijede přesně v určitém čase *t*, rovna 0!

> Teď už víte, že jevy s nulovou pravděpodobností se stávají, a to velmi často! Například pokaždé, když autobus přijede!

Můžeme hovořit pouze o pravděpodobnosti, že proměnná spadne do určitého intervalu hodnot, např. P(t<sub>1</sub>≤X<t<sub>2</sub>). V tomto případě je pravděpodobnostní rozdělení popsáno pomocí **hustotní funkce pravděpodobnosti** p(x), takové že

![P(t_1\le X<t_2)=\int_{t_1}^{t_2}p(x)dx](../../../../1-Introduction/04-stats-and-probability/images/probability-density.png)

Spojitým analogem rovnoměrného rozdělení je **spojité rovnoměrné rozdělení**, které je definováno na konečném intervalu. Pravděpodobnost, že hodnota X spadne do intervalu délky l, je úměrná l a dosahuje až 1.

Dalším důležitým rozdělením je **normální rozdělení**, o kterém si povíme podrobněji níže.

## Průměr, rozptyl a směrodatná odchylka

Předpokládejme, že máme sekvenci n vzorků náhodné proměnné X: x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>. **Průměr** (nebo **aritmetický průměr**) této sekvence můžeme definovat tradičním způsobem jako (x<sub>1</sub>+x<sub>2</sub>+...+x<sub>n</sub>)/n. Pokud zvětšíme velikost vzorku (tj. vezmeme limit s n→∞), získáme průměr (také nazývaný **střední hodnota**) rozdělení. Střední hodnotu budeme označovat jako **E**(x).

> Lze ukázat, že pro jakékoli diskrétní rozdělení s hodnotami {x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>N</sub>} a odpovídajícími pravděpodobnostmi p<sub>1</sub>, p<sub>2</sub>, ..., p<sub>N</sub> platí, že střední hodnota je E(X)=x<sub>1</sub>p<sub>1</sub>+x<sub>2</sub>p<sub>2</sub>+...+x<sub>N</sub>p<sub>N</sub>.

Pro určení, jak moc jsou hodnoty rozptýlené, můžeme vypočítat rozptyl σ<sup>2</sup> = ∑(x<sub>i</sub> - μ)<sup>2</sup>/n, kde μ je průměr sekvence. Hodnota σ se nazývá **směrodatná odchylka** a σ<sup>2</sup> se nazývá **rozptyl**.

## Mód, medián a kvartily

Někdy průměr nedostatečně reprezentuje „typickou“ hodnotu dat. Například pokud existuje několik extrémních hodnot, které jsou zcela mimo rozsah, mohou ovlivnit průměr. Dalším dobrým ukazatelem je **medián**, což je hodnota, pro kterou platí, že polovina datových bodů je nižší a druhá polovina vyšší.

Pro lepší pochopení rozdělení dat je užitečné hovořit o **kvartilech**:

* První kvartil, nebo Q1, je hodnota, pod kterou spadá 25 % dat
* Třetí kvartil, nebo Q3, je hodnota, pod kterou spadá 75 % dat

Graficky můžeme vztah mezi mediánem a kvartily znázornit v diagramu nazývaném **box plot**:

<img src="images/boxplot_explanation.png" width="50%"/>

Zde také vypočítáme **mezikvartilové rozpětí** IQR=Q3-Q1 a tzv. **odlehlé hodnoty** – hodnoty, které leží mimo hranice [Q1-1.5*IQR,Q3+1.5*IQR].

Pro konečné rozdělení obsahující malý počet možných hodnot je dobrá „typická“ hodnota ta, která se vyskytuje nejčastěji, a nazývá se **mód**. Často se používá pro kategorická data, jako jsou barvy. Uvažujme situaci, kdy máme dvě skupiny lidí – jedni silně preferují červenou a druzí modrou. Pokud barvy zakódujeme čísly, průměrná hodnota oblíbené barvy by byla někde ve spektru oranžové až zelené, což neodráží skutečné preference žádné skupiny. Mód by však byl buď jedna z barev, nebo obě barvy, pokud by počet lidí hlasujících pro ně byl stejný (v tomto případě nazýváme vzorek **multimodální**).

## Reálná data

Když analyzujeme data z reálného světa, často nejsou náhodnými proměnnými v tom smyslu, že neprovádíme experimenty s neznámým výsledkem. Například vezměme tým baseballových hráčů a jejich tělesné údaje, jako je výška, váha a věk. Tyto hodnoty nejsou přesně náhodné, ale stále můžeme použít stejné matematické koncepty. Například sekvenci hmotností lidí můžeme považovat za sekvenci hodnot pocházejících z nějaké náhodné proměnné. Níže je sekvence hmotností skutečných baseballových hráčů z [Major League Baseball](http://mlb.mlb.com/index.jsp), převzatá z [tohoto datasetu](http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights) (pro vaše pohodlí je uvedeno pouze prvních 20 hodnot):

```
[180.0, 215.0, 210.0, 210.0, 188.0, 176.0, 209.0, 200.0, 231.0, 180.0, 188.0, 180.0, 185.0, 160.0, 180.0, 185.0, 197.0, 189.0, 185.0, 219.0]
```

> **Poznámka**: Pro příklad práce s tímto datasetem se podívejte na [doprovodný notebook](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb). V této lekci je také několik výzev, které můžete splnit přidáním kódu do tohoto notebooku. Pokud si nejste jisti, jak s daty pracovat, nebojte se – k práci s daty pomocí Pythonu se vrátíme později. Pokud nevíte, jak spustit kód v Jupyter Notebooku, podívejte se na [tento článek](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

Zde je box plot zobrazující průměr, medián a kvartily pro naše data:

![Box plot hmotností](../../../../1-Introduction/04-stats-and-probability/images/weight-boxplot.png)

Protože naše data obsahují informace o různých **rolích hráčů**, můžeme také vytvořit box plot podle role – to nám umožní získat představu o tom, jak se hodnoty parametrů liší mezi rolemi. Tentokrát budeme uvažovat výšku:

![Box plot podle role](../../../../1-Introduction/04-stats-and-probability/images/boxplot_byrole.png)

Tento diagram naznačuje, že průměrná výška hráčů na první metě je vyšší než výška hráčů na druhé metě. Později v této lekci se naučíme, jak tuto hypotézu formálněji otestovat a jak ukázat, že naše data jsou statisticky významná.

> Při práci s reálnými daty předpokládáme, že všechny datové body jsou vzorky pocházející z nějakého pravděpodobnostního rozdělení. Tento předpoklad nám umožňuje aplikovat techniky strojového učení a vytvářet funkční prediktivní modely.

Pro zjištění, jaké je rozdělení našich dat, můžeme vytvořit graf nazývaný **histogram**. Osa X bude obsahovat různé intervaly hmotností (tzv. **bin**), a svislá osa ukáže počet výskytů naší náhodné proměnné v daném intervalu.

![Histogram reálných dat](../../../../1-Introduction/04-stats-and-probability/images/weight-histogram.png)

Z tohoto histogramu vidíme, že všechny hodnoty jsou soustředěny kolem určité průměrné hmotnosti a čím dále od této hmotnosti jdeme, tím méně často se dané hodnoty vyskytují. Jinými slovy, je velmi nepravděpodobné, že by hmotnost baseballového hráče byla výrazně odlišná od průměrné hmotnosti. Rozptyl hmotností ukazuje, do jaké míry se hmotnosti pravděpodobně liší od průměru.

> Pokud bychom vzali hmotnosti jiných lidí, kteří nejsou z baseballové ligy, rozdělení by pravděpodobně bylo jiné. Tvar rozdělení by však zůstal stejný, ale průměr a rozptyl by se změnily. Pokud tedy náš model trénujeme na baseballových hráčích, pravděpodobně poskytne špatné výsledky, pokud jej aplikujeme na studenty univerzity, protože základní rozdělení je odlišné.

## Normální rozdělení

Rozdělení hmotností, které jsme viděli výše, je velmi typické a mnoho měření z reálného světa sleduje stejný typ rozdělení, ale s různým průměrem a rozptylem. Toto rozdělení se nazývá **normální rozdělení** a hraje velmi důležitou roli ve statistice.

Použití normálního rozdělení je správný způsob, jak generovat náhodné hmotnosti potenciálních baseballových hráčů. Jakmile známe průměrnou hmotnost `mean` a směrodatnou odchylku `std`, můžeme vygenerovat 1000 vzorků hmotností následujícím způsobem:
```python
samples = np.random.normal(mean,std,1000)
```

Pokud vykreslíme histogram vygenerovaných vzorků, uvidíme obrázek velmi podobný tomu, který je uveden výše. A pokud zvýšíme počet vzorků a počet binů, můžeme vytvořit obrázek normálního rozdělení, který je blíže ideálu:

![Normální rozdělení s průměrem=0 a směrodatnou odchylkou=1](../../../../1-Introduction/04-stats-and-probability/images/normal-histogram.png)

*Normální rozdělení s průměrem=0 a směrodatnou odchylkou=1*

## Intervaly spolehlivosti

Když mluvíme o hmotnostech baseballových hráčů, předpokládáme, že existuje určitá **náhodná proměnná W**, která odpovídá ideálnímu pravděpodobnostnímu rozdělení hmotností všech baseballových hráčů (tzv. **populace**). Naše sekvence hmotností odpovídá podmnožině všech baseballových hráčů, kterou nazýváme **vzorek**. Zajímavou otázkou je, zda můžeme znát parametry rozdělení W, tj. průměr a rozptyl populace.

Nejjednodušší odpovědí by bylo vypočítat průměr a rozptyl našeho vzorku. Nicméně se může stát, že náš náhodný vzorek přesně neodráží celou populaci. Proto má smysl hovořit o **intervalech spolehlivosti**.
> **Interval spolehlivosti** je odhad skutečného průměru populace na základě našeho vzorku, který je přesný s určitou pravděpodobností (nebo **úrovní spolehlivosti**).
Předpokládejme, že máme vzorek X<sub>1</sub>, ..., X<sub>n</sub> z naší distribuce. Pokaždé, když odebereme vzorek z naší distribuce, dostaneme jinou střední hodnotu μ. Proto lze μ považovat za náhodnou veličinu. **Interval spolehlivosti** s pravděpodobností p je dvojice hodnot (L<sub>p</sub>,R<sub>p</sub>), taková, že **P**(L<sub>p</sub>≤μ≤R<sub>p</sub>) = p, tj. pravděpodobnost, že naměřená střední hodnota spadne do tohoto intervalu, je rovna p.

Podrobné vysvětlení výpočtu těchto intervalů spolehlivosti přesahuje rámec našeho krátkého úvodu. Další podrobnosti lze nalézt [na Wikipedii](https://en.wikipedia.org/wiki/Confidence_interval). Stručně řečeno, definujeme distribuci vypočítané střední hodnoty vzorku vzhledem ke skutečné střední hodnotě populace, což se nazývá **Studentova distribuce**.

> **Zajímavý fakt**: Studentova distribuce je pojmenována po matematikovi Williamu Sealy Gossetovi, který publikoval svůj článek pod pseudonymem "Student". Pracoval v pivovaru Guinness a podle jedné z verzí jeho zaměstnavatel nechtěl, aby veřejnost věděla, že používají statistické testy k určení kvality surovin.

Pokud chceme odhadnout střední hodnotu μ naší populace s pravděpodobností p, musíme vzít *(1-p)/2-tý percentil* Studentovy distribuce A, který lze buď najít v tabulkách, nebo vypočítat pomocí vestavěných funkcí statistického softwaru (např. Python, R atd.). Poté bude interval pro μ dán jako X±A*D/√n, kde X je získaná střední hodnota vzorku a D je směrodatná odchylka.

> **Poznámka**: Vynecháváme také diskusi o důležitém konceptu [stupňů volnosti](https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics)), který je důležitý ve vztahu ke Studentově distribuci. Pro hlubší pochopení tohoto konceptu se můžete obrátit na podrobnější knihy o statistice.

Příklad výpočtu intervalu spolehlivosti pro hmotnosti a výšky je uveden v [přiložených poznámkových blocích](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb).

| p | Průměr hmotnosti |
|-----|----------------|
| 0.85 | 201.73±0.94 |
| 0.90 | 201.73±1.08 |
| 0.95 | 201.73±1.28 |

Všimněte si, že čím vyšší je pravděpodobnost spolehlivosti, tím širší je interval spolehlivosti.

## Testování hypotéz

V naší datové sadě baseballových hráčů existují různé role hráčů, které lze shrnout níže (podívejte se na [přiložený poznámkový blok](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb), kde je ukázáno, jak tuto tabulku vypočítat):

| Role | Výška | Hmotnost | Počet |
|------|-------|----------|-------|
| Catcher | 72.723684 | 204.328947 | 76 |
| Designated_Hitter | 74.222222 | 220.888889 | 18 |
| First_Baseman | 74.000000 | 213.109091 | 55 |
| Outfielder | 73.010309 | 199.113402 | 194 |
| Relief_Pitcher | 74.374603 | 203.517460 | 315 |
| Second_Baseman | 71.362069 | 184.344828 | 58 |
| Shortstop | 71.903846 | 182.923077 | 52 |
| Starting_Pitcher | 74.719457 | 205.163636 | 221 |
| Third_Baseman | 73.044444 | 200.955556 | 45 |

Můžeme si všimnout, že průměrná výška hráčů na první metě je vyšší než u hráčů na druhé metě. Mohli bychom tedy dojít k závěru, že **hráči na první metě jsou vyšší než hráči na druhé metě**.

> Toto tvrzení se nazývá **hypotéza**, protože nevíme, zda je tento fakt skutečně pravdivý.

Není však vždy zřejmé, zda můžeme tento závěr učinit. Z výše uvedené diskuse víme, že každá střední hodnota má svůj interval spolehlivosti, a proto může být tento rozdíl pouze statistickou chybou. Potřebujeme formálnější způsob, jak naši hypotézu otestovat.

Spočítejme intervaly spolehlivosti zvlášť pro výšky hráčů na první a druhé metě:

| Spolehlivost | První meta | Druhá meta |
|--------------|------------|------------|
| 0.85 | 73.62..74.38 | 71.04..71.69 |
| 0.90 | 73.56..74.44 | 70.99..71.73 |
| 0.95 | 73.47..74.53 | 70.92..71.81 |

Vidíme, že za žádné spolehlivosti se intervaly nepřekrývají. To potvrzuje naši hypotézu, že hráči na první metě jsou vyšší než hráči na druhé metě.

Formálněji řečeno, problém, který řešíme, je zjistit, zda **dvě pravděpodobnostní distribuce jsou stejné**, nebo alespoň mají stejné parametry. V závislosti na distribuci musíme použít různé testy. Pokud víme, že naše distribuce jsou normální, můžeme použít **[Studentův t-test](https://en.wikipedia.org/wiki/Student%27s_t-test)**.

V Studentově t-testu počítáme tzv. **t-hodnotu**, která ukazuje rozdíl mezi středními hodnotami s ohledem na rozptyl. Bylo prokázáno, že t-hodnota následuje **Studentovu distribuci**, což nám umožňuje získat prahovou hodnotu pro danou úroveň spolehlivosti **p** (to lze vypočítat nebo najít v numerických tabulkách). Poté porovnáme t-hodnotu s touto prahovou hodnotou, abychom hypotézu potvrdili nebo zamítli.

V Pythonu můžeme použít balíček **SciPy**, který obsahuje funkci `ttest_ind` (kromě mnoha dalších užitečných statistických funkcí!). Tato funkce za nás vypočítá t-hodnotu a také provede zpětné vyhledání p-hodnoty spolehlivosti, takže se můžeme jednoduše podívat na spolehlivost a učinit závěr.

Například naše srovnání výšek hráčů na první a druhé metě nám dává následující výsledky: 
```python
from scipy.stats import ttest_ind

tval, pval = ttest_ind(df.loc[df['Role']=='First_Baseman',['Height']], df.loc[df['Role']=='Designated_Hitter',['Height']],equal_var=False)
print(f"T-value = {tval[0]:.2f}\nP-value: {pval[0]}")
```
```
T-value = 7.65
P-value: 9.137321189738925e-12
```
V našem případě je p-hodnota velmi nízká, což znamená, že existuje silný důkaz podporující tvrzení, že hráči na první metě jsou vyšší.

Existují také různé další typy hypotéz, které bychom mohli chtít testovat, například:
* Prokázat, že daný vzorek odpovídá nějaké distribuci. V našem případě jsme předpokládali, že výšky mají normální distribuci, ale to vyžaduje formální statistické ověření.
* Prokázat, že střední hodnota vzorku odpovídá nějaké předem definované hodnotě.
* Porovnat střední hodnoty několika vzorků (např. jaký je rozdíl v úrovních štěstí mezi různými věkovými skupinami).

## Zákon velkých čísel a centrální limitní věta

Jedním z důvodů, proč je normální distribuce tak důležitá, je tzv. **centrální limitní věta**. Předpokládejme, že máme velký vzorek nezávislých hodnot N, X<sub>1</sub>, ..., X<sub>N</sub>, odebraných z libovolné distribuce se střední hodnotou μ a rozptylem σ<sup>2</sup>. Poté, pro dostatečně velké N (jinými slovy, když N→∞), bude střední hodnota Σ<sub>i</sub>X<sub>i</sub> normálně distribuována se střední hodnotou μ a rozptylem σ<sup>2</sup>/N.

> Jiný způsob, jak interpretovat centrální limitní větu, je říci, že bez ohledu na distribuci, když vypočítáte průměr součtu libovolných hodnot náhodné veličiny, skončíte s normální distribucí.

Z centrální limitní věty také vyplývá, že když N→∞, pravděpodobnost, že střední hodnota vzorku bude rovna μ, se blíží 1. To je známé jako **zákon velkých čísel**.

## Kovariance a korelace

Jednou z věcí, které datová věda dělá, je hledání vztahů mezi daty. Říkáme, že dvě sekvence **korelují**, když vykazují podobné chování ve stejnou dobu, tj. buď společně rostou/klesají, nebo jedna sekvence roste, když druhá klesá, a naopak. Jinými slovy, zdá se, že mezi dvěma sekvencemi existuje nějaký vztah.

> Korelace nemusí nutně znamenat příčinný vztah mezi dvěma sekvencemi; někdy mohou obě proměnné záviset na nějaké vnější příčině, nebo může být korelace čistě náhodná. Silná matematická korelace je však dobrým indikátorem, že dvě proměnné jsou nějak propojeny.

Matematicky je hlavním konceptem, který ukazuje vztah mezi dvěma náhodnými veličinami, **kovariance**, která se počítá takto: Cov(X,Y) = **E**\[(X-**E**(X))(Y-**E**(Y))\]. Počítáme odchylku obou proměnných od jejich středních hodnot a poté součin těchto odchylek. Pokud se obě proměnné odchylují společně, součin bude vždy kladný, což povede k kladné kovarianci. Pokud se obě proměnné odchylují nesynchronně (tj. jedna klesá pod průměr, když druhá stoupá nad průměr), vždy dostaneme záporné hodnoty, což povede k záporné kovarianci. Pokud odchylky nejsou závislé, budou se přibližně rovnat nule.

Absolutní hodnota kovariance nám toho o velikosti korelace příliš neřekne, protože závisí na velikosti skutečných hodnot. Abychom ji normalizovali, můžeme kovarianci vydělit směrodatnou odchylkou obou proměnných a získat **korelaci**. Dobrá věc je, že korelace je vždy v rozmezí [-1,1], kde 1 označuje silnou kladnou korelaci mezi hodnotami, -1 silnou zápornou korelaci a 0 žádnou korelaci (proměnné jsou nezávislé).

**Příklad**: Můžeme spočítat korelaci mezi hmotnostmi a výškami baseballových hráčů z výše uvedené datové sady:
```python
print(np.corrcoef(weights,heights))
```
Výsledkem získáme **korelační matici** podobnou této:
```
array([[1.        , 0.52959196],
       [0.52959196, 1.        ]])
```

> Korelační matice C může být vypočítána pro libovolný počet vstupních sekvencí S<sub>1</sub>, ..., S<sub>n</sub>. Hodnota C<sub>ij</sub> je korelace mezi S<sub>i</sub> a S<sub>j</sub>, a diagonální prvky jsou vždy 1 (což je také vlastní korelace S<sub>i</sub>).

V našem případě hodnota 0.53 naznačuje, že mezi hmotností a výškou osoby existuje určitá korelace. Můžeme také vytvořit bodový graf jedné hodnoty proti druhé, abychom vizuálně viděli vztah:

![Vztah mezi hmotností a výškou](../../../../1-Introduction/04-stats-and-probability/images/weight-height-relationship.png)

> Další příklady korelace a kovariance naleznete v [přiloženém poznámkovém bloku](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb).

## Závěr

V této sekci jsme se naučili:

* základní statistické vlastnosti dat, jako je průměr, rozptyl, modus a kvartily
* různé distribuce náhodných veličin, včetně normální distribuce
* jak najít korelaci mezi různými vlastnostmi
* jak použít matematický a statistický aparát k ověření hypotéz
* jak vypočítat intervaly spolehlivosti pro náhodnou veličinu na základě vzorku dat

I když to rozhodně není vyčerpávající seznam témat, která existují v oblasti pravděpodobnosti a statistiky, mělo by to být dostatečné pro dobrý začátek tohoto kurzu.

## 🚀 Výzva

Použijte ukázkový kód v poznámkovém bloku k otestování dalších hypotéz:
1. Hráči na první metě jsou starší než hráči na druhé metě.
2. Hráči na první metě jsou vyšší než hráči na třetí metě.
3. Shortstopi jsou vyšší než hráči na druhé metě.

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ds/)

## Přehled a samostudium

Pravděpodobnost a statistika je tak široké téma, že si zaslouží vlastní kurz. Pokud se chcete ponořit hlouběji do teorie, můžete pokračovat ve čtení některých z následujících knih:

1. [Carlos Fernandez-Granda](https://cims.nyu.edu/~cfgranda/) z New York University má skvělé přednáškové poznámky [Probability and Statistics for Data Science](https://cims.nyu.edu/~cfgranda/pages/stuff/probability_stats_for_DS.pdf) (dostupné online).
1. [Peter a Andrew Bruce. Practical Statistics for Data Scientists.](https://www.oreilly.com/library/view/practical-statistics-for/9781491952955/) [[ukázkový kód v R](https://github.com/andrewgbruce/statistics-for-data-scientists)].
1. [James D. Miller. Statistics for Data Science](https://www.packtpub.com/product/statistics-for-data-science/9781788290678) [[ukázkový kód v R](https://github.com/PacktPublishing/Statistics-for-Data-Science)].

## Zadání

[Malá studie o diabetu](assignment.md)

## Poděkování

Tuto lekci vytvořil s ♥️ [Dmitry Soshnikov](http://soshnikov.com).

---

**Upozornění**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o co největší přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.