<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a33c5d4b4156a2b41788d8720b6f724c",
  "translation_date": "2025-08-28T02:36:06+00:00",
  "source_file": "3-Data-Visualization/R/12-visualization-relationships/README.md",
  "language_code": "tl"
}
-->
# Pagpapakita ng Relasyon: Lahat Tungkol sa Pulot 🍯

|![ Sketchnote ni [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Pagpapakita ng Relasyon - _Sketchnote ni [@nitya](https://twitter.com/nitya)_ |

Sa pagpapatuloy ng ating pananaliksik na nakatuon sa kalikasan, tuklasin natin ang mga kawili-wiling paraan ng pagpapakita ng relasyon sa pagitan ng iba't ibang uri ng pulot, batay sa dataset mula sa [United States Department of Agriculture](https://www.nass.usda.gov/About_NASS/index.php).

Ang dataset na ito, na may humigit-kumulang 600 item, ay nagpapakita ng produksyon ng pulot sa maraming estado sa U.S. Halimbawa, maaari mong tingnan ang bilang ng mga kolonya, ani bawat kolonya, kabuuang produksyon, imbentaryo, presyo bawat libra, at halaga ng pulot na ginawa sa isang partikular na estado mula 1998-2012, na may isang hilera bawat taon para sa bawat estado.

Magiging kawili-wiling ipakita ang relasyon sa pagitan ng produksyon ng isang estado bawat taon at, halimbawa, ang presyo ng pulot sa estado na iyon. Bilang alternatibo, maaari mong ipakita ang relasyon sa pagitan ng ani ng pulot bawat kolonya sa iba't ibang estado. Ang saklaw ng taon na ito ay sumasaklaw sa mapaminsalang 'CCD' o 'Colony Collapse Disorder' na unang nakita noong 2006 (http://npic.orst.edu/envir/ccd.html), kaya't ito ay isang makabuluhang dataset na pag-aralan. 🐝

## [Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

Sa araling ito, maaari mong gamitin ang ggplot2, na ginamit mo na dati, bilang isang mahusay na library para ipakita ang relasyon sa pagitan ng mga variable. Partikular na kawili-wili ang paggamit ng `geom_point` at `qplot` function ng ggplot2 na nagbibigay-daan sa scatter plots at line plots upang mabilis na ipakita ang '[statistical relationships](https://ggplot2.tidyverse.org/)', na tumutulong sa data scientist na mas maunawaan kung paano nauugnay ang mga variable sa isa't isa.

## Scatterplots

Gumamit ng scatterplot upang ipakita kung paano nagbago ang presyo ng pulot, taon-taon, sa bawat estado. Ang ggplot2, gamit ang `ggplot` at `geom_point`, ay maginhawang naggugrupo ng data ng estado at nagpapakita ng mga data point para sa parehong kategorya at numerong data.

Magsimula tayo sa pag-import ng data at Seaborn:

```r
honey=read.csv('../../data/honey.csv')
head(honey)
```
Mapapansin mo na ang data ng pulot ay may ilang kawili-wiling mga column, kabilang ang taon at presyo bawat libra. Tuklasin natin ang data na ito, na naka-grupo ayon sa estado ng U.S.:

| estado | numcol | yieldpercol | totalprod | stocks   | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL    | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ    | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR    | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA    | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO    | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |
| FL    | 230000 | 98          |22540000   | 4508000  | 0.64       | 14426000  | 1998 |

Gumawa ng simpleng scatterplot upang ipakita ang relasyon sa pagitan ng presyo bawat libra ng pulot at ng estado kung saan ito nagmula. Gawing sapat na mataas ang `y` axis upang maipakita ang lahat ng estado:

```r
library(ggplot2)
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(colour = "blue")
```
![scatterplot 1](../../../../../translated_images/tl/scatter1.86b8900674d88b26dd3353a83fe604e9ab3722c4680cc40ee9beb452ff02cdea.png)

Ngayon, ipakita ang parehong data gamit ang isang kulay ng pulot upang ipakita kung paano nagbago ang presyo sa paglipas ng mga taon. Magagawa mo ito sa pamamagitan ng pagdaragdag ng parameter na 'scale_color_gradientn' upang ipakita ang pagbabago, taon-taon:

> ✅ Alamin ang higit pa tungkol sa [scale_color_gradientn](https://www.rdocumentation.org/packages/ggplot2/versions/0.9.1/topics/scale_colour_gradientn) - subukan ang isang magandang rainbow color scheme!

```r
ggplot(honey, aes(x = priceperlb, y = state, color=year)) +
  geom_point()+scale_color_gradientn(colours = colorspace::heat_hcl(7))
```
![scatterplot 2](../../../../../translated_images/tl/scatter2.4d1cbc693bad20e2b563888747eb6bdf65b73ce449d903f7cd4068a78502dcff.png)

Sa pagbabago ng color scheme na ito, makikita mo na malinaw na may malakas na pagtaas sa paglipas ng mga taon sa presyo ng pulot bawat libra. Sa katunayan, kung titingnan mo ang isang sample set sa data upang i-verify (pumili ng isang partikular na estado, Arizona halimbawa) makikita mo ang pattern ng pagtaas ng presyo taon-taon, na may ilang mga pagbubukod:

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

Isa pang paraan upang ipakita ang progresyon na ito ay ang paggamit ng laki, sa halip na kulay. Para sa mga gumagamit na may colorblindness, maaaring mas mabuting opsyon ito. I-edit ang iyong visualization upang ipakita ang pagtaas ng presyo sa pamamagitan ng pagtaas ng circumference ng mga tuldok:

```r
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(aes(size = year),colour = "blue") +
  scale_size_continuous(range = c(0.25, 3))
```
Makikita mo ang unti-unting pagtaas ng laki ng mga tuldok.

![scatterplot 3](../../../../../translated_images/tl/scatter3.722d21e6f20b3ea2e18339bb9b10d75906126715eb7d5fdc88fe74dcb6d7066a.png)

Ito ba ay simpleng kaso ng supply at demand? Dahil sa mga salik tulad ng pagbabago ng klima at colony collapse, mas kaunti ba ang pulot na magagamit para bilhin taon-taon, kaya't tumataas ang presyo?

Upang matuklasan ang ugnayan sa pagitan ng ilang mga variable sa dataset na ito, tuklasin natin ang ilang line charts.

## Line charts

Tanong: May malinaw bang pagtaas sa presyo ng pulot bawat libra taon-taon? Pinakamadaling matuklasan ito sa pamamagitan ng paggawa ng isang simpleng line chart:

```r
qplot(honey$year,honey$priceperlb, geom='smooth', span =0.5, xlab = "year",ylab = "priceperlb")
```
Sagot: Oo, na may ilang mga pagbubukod sa paligid ng taong 2003:

![line chart 1](../../../../../translated_images/tl/line1.299b576fbb2a59e60a59e7130030f59836891f90302be084e4e8d14da0562e2a.png)

Tanong: Sa 2003, makikita rin ba natin ang pagtaas sa supply ng pulot? Paano kung tingnan mo ang kabuuang produksyon taon-taon?

```python
qplot(honey$year,honey$totalprod, geom='smooth', span =0.5, xlab = "year",ylab = "totalprod")
```

![line chart 2](../../../../../translated_images/tl/line2.3b18fcda7176ceba5b6689eaaabb817d49c965e986f11cac1ae3f424030c34d8.png)

Sagot: Hindi talaga. Kung titingnan mo ang kabuuang produksyon, tila ito ay tumaas sa partikular na taon na iyon, kahit na sa pangkalahatan ang dami ng pulot na ginagawa ay bumababa sa mga taong ito.

Tanong: Sa kasong iyon, ano kaya ang sanhi ng pagtaas ng presyo ng pulot sa paligid ng 2003?

Upang matuklasan ito, maaari kang mag-explore ng facet grid.

## Facet grids

Ang facet grids ay kumukuha ng isang aspeto ng iyong dataset (sa ating kaso, maaari mong piliin ang 'year' upang maiwasan ang sobrang dami ng facets na ginawa). Ang Seaborn ay maaaring gumawa ng plot para sa bawat isa sa mga aspeto ng iyong napiling x at y coordinates para sa mas madaling visual na paghahambing. Kapansin-pansin ba ang 2003 sa ganitong uri ng paghahambing?

Gumawa ng facet grid gamit ang `facet_wrap` tulad ng inirerekomenda ng [ggplot2's documentation](https://ggplot2.tidyverse.org/reference/facet_wrap.html).

```r
ggplot(honey, aes(x=yieldpercol, y = numcol,group = 1)) + 
  geom_line() + facet_wrap(vars(year))
```
Sa visualization na ito, maaari mong ihambing ang ani bawat kolonya at bilang ng mga kolonya taon-taon, magkatabi na may wrap na nakatakda sa 3 para sa mga column:

![facet grid](../../../../../translated_images/tl/facet.491ad90d61c2a7cc69b50c929f80786c749e38217ccedbf1e22ed8909b65987c.png)

Para sa dataset na ito, walang partikular na kapansin-pansin tungkol sa bilang ng mga kolonya at kanilang ani, taon-taon at estado sa estado. Mayroon bang ibang paraan upang tingnan ang paghahanap ng ugnayan sa pagitan ng dalawang variable na ito?

## Dual-line Plots

Subukan ang multiline plot sa pamamagitan ng pag-overlay ng dalawang lineplots sa ibabaw ng isa't isa, gamit ang `par` at `plot` function ng R. Mag-plot tayo ng taon sa x axis at ipakita ang dalawang y axes. Kaya, ipakita ang ani bawat kolonya at bilang ng mga kolonya, na naka-overlay:

```r
par(mar = c(5, 4, 4, 4) + 0.3)              
plot(honey$year, honey$numcol, pch = 16, col = 2,type="l")              
par(new = TRUE)                             
plot(honey$year, honey$yieldpercol, pch = 17, col = 3,              
     axes = FALSE, xlab = "", ylab = "",type="l")
axis(side = 4, at = pretty(range(y2)))      
mtext("colony yield", side = 4, line = 3)   
```
![superimposed plots](../../../../../translated_images/tl/dual-line.fc4665f360a54018d7df9bc6abcc26460112e17dcbda18d3b9ae6109b32b36c3.png)

Habang walang kapansin-pansin sa mata sa paligid ng taong 2003, pinapayagan tayo nitong tapusin ang araling ito sa mas masayang tala: habang may pangkalahatang pagbaba sa bilang ng mga kolonya, ang bilang ng mga kolonya ay nagiging matatag kahit na ang kanilang ani bawat kolonya ay bumababa.

Go, bees, go!

🐝❤️
## 🚀 Hamon

Sa araling ito, natutunan mo ang kaunti pa tungkol sa iba pang gamit ng scatterplots at line grids, kabilang ang facet grids. Hamunin ang iyong sarili na gumawa ng facet grid gamit ang ibang dataset, marahil isa na ginamit mo bago ang mga araling ito. Pansinin kung gaano katagal ang paggawa nito at kung paano mo kailangang maging maingat sa dami ng grids na kailangang iguhit gamit ang mga teknik na ito.
## [Post-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## Review & Self Study

Ang mga line plots ay maaaring simple o medyo kumplikado. Magbasa nang kaunti sa [ggplot2 documentation](https://ggplot2.tidyverse.org/reference/geom_path.html#:~:text=geom_line()%20connects%20them%20in,which%20cases%20are%20connected%20together) tungkol sa iba't ibang paraan kung paano mo ito mabubuo. Subukang pagandahin ang mga line charts na ginawa mo sa araling ito gamit ang iba pang mga pamamaraan na nakalista sa docs.
## Assignment

[Dive into the beehive](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.