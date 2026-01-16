<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0764fd4077f3f04a1d968ec371227744",
  "translation_date": "2025-09-06T11:43:58+00:00",
  "source_file": "3-Data-Visualization/12-visualization-relationships/README.md",
  "language_code": "tl"
}
-->
# Pagpapakita ng Relasyon: Lahat Tungkol sa Pulot 🍯

|![ Sketchnote ni [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Pagpapakita ng Relasyon - _Sketchnote ni [@nitya](https://twitter.com/nitya)_ |

Sa pagpapatuloy ng ating pananaliksik na nakatuon sa kalikasan, tuklasin natin ang mga kawili-wiling paraan ng pagpapakita ng relasyon sa pagitan ng iba't ibang uri ng pulot, batay sa dataset mula sa [United States Department of Agriculture](https://www.nass.usda.gov/About_NASS/index.php).

Ang dataset na ito, na may humigit-kumulang 600 item, ay nagpapakita ng produksyon ng pulot sa maraming estado sa U.S. Halimbawa, maaari mong tingnan ang bilang ng mga kolonya, ani bawat kolonya, kabuuang produksyon, imbentaryo, presyo bawat libra, at halaga ng pulot na ginawa sa isang partikular na estado mula 1998-2012, na may isang row bawat taon para sa bawat estado.

Magiging kawili-wiling ipakita ang relasyon sa pagitan ng produksyon ng isang estado bawat taon at, halimbawa, ang presyo ng pulot sa estado na iyon. Bilang alternatibo, maaari mong ipakita ang relasyon sa pagitan ng ani ng pulot bawat kolonya sa iba't ibang estado. Ang saklaw ng taon na ito ay sumasaklaw sa mapaminsalang 'CCD' o 'Colony Collapse Disorder' na unang nakita noong 2006 (http://npic.orst.edu/envir/ccd.html), kaya't ito ay isang makabuluhang dataset na pag-aralan. 🐝

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/22)

Sa araling ito, maaari mong gamitin ang Seaborn, na ginamit mo na dati, bilang isang mahusay na library para ipakita ang relasyon sa pagitan ng mga variable. Partikular na kawili-wili ang paggamit ng `relplot` function ng Seaborn na nagbibigay-daan sa scatter plots at line plots upang mabilis na ipakita ang '[statistical relationships](https://seaborn.pydata.org/tutorial/relational.html?highlight=relationships)', na tumutulong sa data scientist na mas maunawaan kung paano nauugnay ang mga variable sa isa't isa.

## Scatterplots

Gumamit ng scatterplot upang ipakita kung paano nagbago ang presyo ng pulot, taon-taon, sa bawat estado. Ang Seaborn, gamit ang `relplot`, ay maginhawang naggugrupo ng data ng estado at nagpapakita ng mga data point para sa parehong categorical at numeric na data.

Magsimula tayo sa pag-import ng data at Seaborn:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
honey = pd.read_csv('../../data/honey.csv')
honey.head()
```
Mapapansin mo na ang data ng pulot ay may ilang kawili-wiling mga column, kabilang ang taon at presyo bawat libra. Tuklasin natin ang data na ito, na naka-grupo ayon sa estado ng U.S.:

| estado | numcol | yieldpercol | totalprod | stocks   | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL    | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ    | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR    | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA    | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO    | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |

Gumawa ng basic scatterplot upang ipakita ang relasyon sa pagitan ng presyo bawat libra ng pulot at ng estado kung saan ito nagmula. Gawing sapat na mataas ang `y` axis upang maipakita ang lahat ng estado:

```python
sns.relplot(x="priceperlb", y="state", data=honey, height=15, aspect=.5);
```
![scatterplot 1](../../../../translated_images/tl/scatter1.5e1aa5fd6706c5d12b5e503ccb77f8a930f8620f539f524ddf56a16c039a5d2f.png)

Ngayon, ipakita ang parehong data gamit ang isang honey color scheme upang ipakita kung paano nagbabago ang presyo sa paglipas ng mga taon. Magagawa mo ito sa pamamagitan ng pagdaragdag ng 'hue' parameter upang ipakita ang pagbabago, taon-taon:

> ✅ Alamin ang higit pa tungkol sa [mga color palettes na maaari mong gamitin sa Seaborn](https://seaborn.pydata.org/tutorial/color_palettes.html) - subukan ang isang magandang rainbow color scheme!

```python
sns.relplot(x="priceperlb", y="state", hue="year", palette="YlOrBr", data=honey, height=15, aspect=.5);
```
![scatterplot 2](../../../../translated_images/tl/scatter2.c0041a58621ca702990b001aa0b20cd68c1e1814417139af8a7211a2bed51c5f.png)

Sa pagbabago ng color scheme na ito, makikita mo na malinaw na may malakas na pagtaas sa paglipas ng mga taon sa presyo ng pulot bawat libra. Sa katunayan, kung titingnan mo ang isang sample set sa data upang i-verify (pumili ng isang partikular na estado, Arizona halimbawa) makikita mo ang pattern ng pagtaas ng presyo taon-taon, na may ilang mga eksepsyon:

| estado | numcol | yieldpercol | totalprod | stocks  | priceperlb | prodvalue | year |
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

Isa pang paraan upang ipakita ang progresyon na ito ay ang paggamit ng laki, sa halip na kulay. Para sa mga gumagamit na may colorblindness, maaaring mas magandang opsyon ito. I-edit ang iyong visualization upang ipakita ang pagtaas ng presyo sa pamamagitan ng pagtaas ng circumference ng mga tuldok:

```python
sns.relplot(x="priceperlb", y="state", size="year", data=honey, height=15, aspect=.5);
```
Makikita mo ang unti-unting pagtaas ng laki ng mga tuldok.

![scatterplot 3](../../../../translated_images/tl/scatter3.3c160a3d1dcb36b37900ebb4cf97f34036f28ae2b7b8e6062766c7c1dfc00853.png)

Ito ba ay simpleng kaso ng supply at demand? Dahil sa mga salik tulad ng pagbabago ng klima at colony collapse, mas kaunti ba ang pulot na magagamit para bilhin taon-taon, kaya't tumataas ang presyo?

Upang matuklasan ang ugnayan sa pagitan ng ilang mga variable sa dataset na ito, tuklasin natin ang ilang line charts.

## Line charts

Tanong: May malinaw bang pagtaas sa presyo ng pulot bawat libra taon-taon? Pinakamadaling matuklasan ito sa pamamagitan ng paggawa ng isang simpleng line chart:

```python
sns.relplot(x="year", y="priceperlb", kind="line", data=honey);
```
Sagot: Oo, na may ilang mga eksepsyon sa paligid ng taong 2003:

![line chart 1](../../../../translated_images/tl/line1.f36eb465229a3b1fe385cdc93861aab3939de987d504b05de0b6cd567ef79f43.png)

✅ Dahil ang Seaborn ay nag-a-aggregate ng data sa isang linya, ipinapakita nito "ang maramihang sukat sa bawat x value sa pamamagitan ng pag-plot ng mean at ang 95% confidence interval sa paligid ng mean". [Source](https://seaborn.pydata.org/tutorial/relational.html). Ang time-consuming na behavior na ito ay maaaring i-disable sa pamamagitan ng pagdaragdag ng `ci=None`.

Tanong: Sa 2003, makikita rin ba natin ang pagtaas sa supply ng pulot? Paano kung tingnan mo ang kabuuang produksyon taon-taon?

```python
sns.relplot(x="year", y="totalprod", kind="line", data=honey);
```

![line chart 2](../../../../translated_images/tl/line2.a5b3493dc01058af6402e657aaa9ae1125fafb5e7d6630c777aa60f900a544e4.png)

Sagot: Hindi talaga. Kung titingnan mo ang kabuuang produksyon, tila ito ay tumaas sa partikular na taon, kahit na sa pangkalahatan ang dami ng pulot na ginagawa ay bumababa sa mga taong ito.

Tanong: Sa kasong iyon, ano kaya ang sanhi ng pagtaas ng presyo ng pulot sa paligid ng 2003?

Upang matuklasan ito, maaari kang mag-explore ng facet grid.

## Facet grids

Ang facet grids ay kumukuha ng isang aspeto ng iyong dataset (sa ating kaso, maaari mong piliin ang 'year' upang maiwasan ang sobrang dami ng facets). Ang Seaborn ay maaaring gumawa ng plot para sa bawat isa sa mga facets ng iyong napiling x at y coordinates para sa mas madaling visual na paghahambing. Kapansin-pansin ba ang 2003 sa ganitong uri ng paghahambing?

Gumawa ng facet grid sa pamamagitan ng patuloy na paggamit ng `relplot` tulad ng inirerekomenda ng [Seaborn's documentation](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html?highlight=facetgrid#seaborn.FacetGrid).

```python
sns.relplot(
    data=honey, 
    x="yieldpercol", y="numcol",
    col="year", 
    col_wrap=3,
    kind="line"
    )
```
Sa visualization na ito, maaari mong ihambing ang ani bawat kolonya at bilang ng mga kolonya taon-taon, magkatabi na may wrap na nakatakda sa 3 para sa mga column:

![facet grid](../../../../translated_images/tl/facet.6a34851dcd540050dcc0ead741be35075d776741668dd0e42f482c89b114c217.png)

Para sa dataset na ito, walang partikular na kapansin-pansin tungkol sa bilang ng mga kolonya at kanilang ani, taon-taon at estado sa estado. Mayroon bang ibang paraan upang tingnan ang paghahanap ng ugnayan sa pagitan ng dalawang variable na ito?

## Dual-line Plots

Subukan ang isang multiline plot sa pamamagitan ng pag-overlay ng dalawang lineplots sa ibabaw ng isa't isa, gamit ang `despine` ng Seaborn upang alisin ang kanilang top at right spines, at gamit ang `ax.twinx` [mula sa Matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html). Ang Twinx ay nagbibigay-daan sa isang chart na magbahagi ng x axis at magpakita ng dalawang y axes. Kaya, ipakita ang ani bawat kolonya at bilang ng mga kolonya, na naka-overlay:

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
![superimposed plots](../../../../translated_images/tl/dual-line.a4c28ce659603fab2c003f4df816733df2bf41d1facb7de27989ec9afbf01b33.png)

Habang walang kapansin-pansin sa mata sa paligid ng taong 2003, pinapayagan tayo nitong tapusin ang araling ito sa isang mas masayang tala: habang may pangkalahatang pagbaba sa bilang ng mga kolonya, ang bilang ng mga kolonya ay nagiging matatag kahit na ang kanilang ani bawat kolonya ay bumababa.

Go, bees, go!

🐝❤️
## 🚀 Hamon

Sa araling ito, natutunan mo ang higit pa tungkol sa iba pang gamit ng scatterplots at line grids, kabilang ang facet grids. Hamunin ang iyong sarili na gumawa ng facet grid gamit ang ibang dataset, marahil isa na ginamit mo bago ang mga araling ito. Pansinin kung gaano katagal ang paggawa nito at kung paano mo kailangang maging maingat sa dami ng grids na kailangang iguhit gamit ang mga teknik na ito.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/23)

## Review & Self Study

Ang mga line plots ay maaaring simple o medyo kumplikado. Magbasa nang kaunti sa [Seaborn documentation](https://seaborn.pydata.org/generated/seaborn.lineplot.html) tungkol sa iba't ibang paraan kung paano mo ito mabubuo. Subukang pagandahin ang mga line charts na ginawa mo sa araling ito gamit ang iba pang mga pamamaraan na nakalista sa docs.

## Assignment

[Dive into the beehive](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang orihinal na wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.