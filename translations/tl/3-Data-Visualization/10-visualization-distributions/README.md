<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "87faccac113d772551486a67a607153e",
  "translation_date": "2025-08-28T02:41:59+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "tl"
}
-->
# Pagpapakita ng Distribusyon

|![ Sketchnote ni [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Pagpapakita ng Distribusyon - _Sketchnote ni [@nitya](https://twitter.com/nitya)_ |

Sa nakaraang aralin, natutunan mo ang ilang kawili-wiling impormasyon tungkol sa isang dataset ng mga ibon sa Minnesota. Natuklasan mo ang ilang maling datos sa pamamagitan ng pagpapakita ng mga outlier at tiningnan ang mga pagkakaiba sa pagitan ng mga kategorya ng ibon batay sa kanilang pinakamahabang haba.

## [Pre-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/18)
## Tuklasin ang dataset ng mga ibon

Isa pang paraan upang masuri ang datos ay sa pamamagitan ng pagtingin sa distribusyon nito, o kung paano nakaayos ang datos sa isang axis. Halimbawa, maaaring gusto mong malaman ang pangkalahatang distribusyon ng maximum wingspan o maximum body mass ng mga ibon sa Minnesota mula sa dataset na ito.

Tuklasin natin ang ilang impormasyon tungkol sa distribusyon ng datos sa dataset na ito. Sa _notebook.ipynb_ file na nasa root ng folder ng araling ito, i-import ang Pandas, Matplotlib, at ang iyong datos:

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | Pangalan                     | Siyentipikong Pangalan | Kategorya             | Order        | Pamilya  | Genus       | Katayuan ng Konserbasyon | MinLength | MaxLength | MinBodyMass | MaxBodyMass | MinWingspan | MaxWingspan |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                       |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                       |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                       |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                       |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                       |        64 |        81 |        1930 |        3310 |         130 |         165 |

Sa pangkalahatan, mabilis mong makikita ang distribusyon ng datos sa pamamagitan ng paggamit ng scatter plot tulad ng ginawa natin sa nakaraang aralin:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![max length per order](../../../../translated_images/scatter-wb.9d98b0ed7f0388af979441853361a11df5f518f5307938a503ca7913e986111b.tl.png)

Ipinapakita nito ang pangkalahatang distribusyon ng haba ng katawan ayon sa Order ng ibon, ngunit hindi ito ang pinakamainam na paraan upang ipakita ang tunay na distribusyon. Ang gawaing ito ay karaniwang ginagawa sa pamamagitan ng paggawa ng Histogram.

## Paggamit ng histograms

Nag-aalok ang Matplotlib ng mahusay na paraan upang ipakita ang distribusyon ng datos gamit ang Histograms. Ang ganitong uri ng tsart ay parang bar chart kung saan makikita ang distribusyon sa pamamagitan ng pagtaas at pagbaba ng mga bar. Upang makabuo ng histogram, kailangan mo ng numerikal na datos. Upang makabuo ng Histogram, maaari kang mag-plot ng tsart na tinutukoy ang uri bilang 'hist' para sa Histogram. Ang tsart na ito ay nagpapakita ng distribusyon ng MaxBodyMass para sa buong saklaw ng numerikal na datos ng dataset. Sa pamamagitan ng paghahati ng array ng datos sa mas maliliit na bahagi, maipapakita nito ang distribusyon ng mga halaga ng datos:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![distribution over the entire dataset](../../../../translated_images/dist1-wb.0d0cac82e2974fbbec635826fefead401af795f82e2279e2e2678bf2c117d827.tl.png)

Tulad ng nakikita mo, karamihan sa 400+ na ibon sa dataset na ito ay nasa saklaw na mas mababa sa 2000 para sa kanilang Max Body Mass. Makakuha ng higit pang impormasyon sa datos sa pamamagitan ng pagbabago ng `bins` parameter sa mas mataas na numero, tulad ng 30:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![distribution over the entire dataset with larger bins param](../../../../translated_images/dist2-wb.2c0a7a3499b2fbf561e9f93b69f265dfc538dc78f6de15088ba84a88152e26ba.tl.png)

Ipinapakita ng tsart na ito ang distribusyon sa mas detalyadong paraan. Maaaring makabuo ng tsart na hindi masyadong skewed sa kaliwa sa pamamagitan ng pagtiyak na pipiliin mo lamang ang datos sa loob ng isang partikular na saklaw:

I-filter ang iyong datos upang makuha lamang ang mga ibon na ang body mass ay mas mababa sa 60, at ipakita ang 40 `bins`:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![filtered histogram](../../../../translated_images/dist3-wb.64b88db7f9780200bd486a2c2a3252548dd439672dbd3f778193db7f654b100c.tl.png)

✅ Subukan ang iba pang mga filter at puntos ng datos. Upang makita ang buong distribusyon ng datos, alisin ang `['MaxBodyMass']` filter upang ipakita ang mga labeled na distribusyon.

Nag-aalok ang histogram ng magagandang pagpapahusay sa kulay at labeling na maaari mo ring subukan:

Gumawa ng 2D histogram upang ihambing ang relasyon sa pagitan ng dalawang distribusyon. Ihambing natin ang `MaxBodyMass` vs. `MaxLength`. Nag-aalok ang Matplotlib ng built-in na paraan upang ipakita ang convergence gamit ang mas maliwanag na kulay:

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
Mukhang may inaasahang ugnayan sa pagitan ng dalawang elementong ito sa isang inaasahang axis, na may isang partikular na malakas na punto ng convergence:

![2D plot](../../../../translated_images/2D-wb.ae22fdd33936507a41e3af22e11e4903b04a9be973b23a4e05214efaccfd66c8.tl.png)

Ang mga histogram ay mahusay na gumagana bilang default para sa numerikal na datos. Paano kung kailangan mong makita ang distribusyon ayon sa text-based na datos? 
## Tuklasin ang dataset para sa distribusyon gamit ang text-based na datos 

Ang dataset na ito ay naglalaman din ng magandang impormasyon tungkol sa kategorya ng ibon at ang genus, species, at pamilya nito pati na rin ang katayuan ng konserbasyon nito. Tuklasin natin ang impormasyong ito tungkol sa konserbasyon. Ano ang distribusyon ng mga ibon ayon sa kanilang katayuan ng konserbasyon?

> ✅ Sa dataset, ilang mga acronym ang ginagamit upang ilarawan ang katayuan ng konserbasyon. Ang mga acronym na ito ay mula sa [IUCN Red List Categories](https://www.iucnredlist.org/), isang organisasyon na nagkakatalogo ng katayuan ng mga species.
> 
> - CR: Critically Endangered
> - EN: Endangered
> - EX: Extinct
> - LC: Least Concern
> - NT: Near Threatened
> - VU: Vulnerable

Ang mga ito ay text-based na halaga kaya kakailanganin mong gumawa ng transform upang makabuo ng histogram. Gamit ang filteredBirds dataframe, ipakita ang katayuan ng konserbasyon nito kasama ang Minimum Wingspan. Ano ang nakikita mo? 

```python
x1 = filteredBirds.loc[filteredBirds.ConservationStatus=='EX', 'MinWingspan']
x2 = filteredBirds.loc[filteredBirds.ConservationStatus=='CR', 'MinWingspan']
x3 = filteredBirds.loc[filteredBirds.ConservationStatus=='EN', 'MinWingspan']
x4 = filteredBirds.loc[filteredBirds.ConservationStatus=='NT', 'MinWingspan']
x5 = filteredBirds.loc[filteredBirds.ConservationStatus=='VU', 'MinWingspan']
x6 = filteredBirds.loc[filteredBirds.ConservationStatus=='LC', 'MinWingspan']

kwargs = dict(alpha=0.5, bins=20)

plt.hist(x1, **kwargs, color='red', label='Extinct')
plt.hist(x2, **kwargs, color='orange', label='Critically Endangered')
plt.hist(x3, **kwargs, color='yellow', label='Endangered')
plt.hist(x4, **kwargs, color='green', label='Near Threatened')
plt.hist(x5, **kwargs, color='blue', label='Vulnerable')
plt.hist(x6, **kwargs, color='gray', label='Least Concern')

plt.gca().set(title='Conservation Status', ylabel='Min Wingspan')
plt.legend();
```

![wingspan and conservation collation](../../../../translated_images/histogram-conservation-wb.3c40450eb072c14de7a1a3ec5c0fcba4995531024760741b392911b567fd8b70.tl.png)

Mukhang walang magandang ugnayan sa pagitan ng minimum wingspan at katayuan ng konserbasyon. Subukan ang iba pang mga elemento ng dataset gamit ang pamamaraang ito. Maaari ka ring mag-eksperimento sa iba't ibang filter. May nakikita ka bang ugnayan?

## Density plots

Maaaring napansin mo na ang mga histogram na tiningnan natin hanggang ngayon ay 'stepped' at hindi dumadaloy nang maayos sa isang arc. Upang ipakita ang mas maayos na density chart, maaari kang gumamit ng density plot.

Upang gumamit ng density plots, maging pamilyar sa isang bagong plotting library, [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html). 

I-load ang Seaborn at subukan ang isang basic density plot:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![Density plot](../../../../translated_images/density1.8801043bd4af2567b0f706332b5853c7614e5e4b81b457acc27eb4e092a65cbd.tl.png)

Makikita mo kung paano ginagaya ng plot ang naunang isa para sa Minimum Wingspan data; mas maayos lang ito. Ayon sa dokumentasyon ng Seaborn, "Kumpara sa isang histogram, ang KDE ay maaaring makabuo ng plot na mas malinis at mas madaling maunawaan, lalo na kapag nagpapakita ng maraming distribusyon. Ngunit maaari itong magpakilala ng mga distortion kung ang underlying distribution ay bounded o hindi maayos. Tulad ng histogram, ang kalidad ng representasyon ay nakasalalay din sa pagpili ng tamang smoothing parameters." [source](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) Sa madaling salita, ang mga outlier ay palaging magpapasama sa iyong mga tsart.

Kung nais mong balikan ang jagged MaxBodyMass line sa pangalawang tsart na ginawa mo, maaari mo itong gawing mas maayos sa pamamagitan ng muling paggawa nito gamit ang pamamaraang ito:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![smooth bodymass line](../../../../translated_images/density2.8e7647257060ff544a1aaded57e8dd1887586bfe340139e9b77ac1e5287f7977.tl.png)

Kung nais mo ng maayos, ngunit hindi masyadong maayos na linya, i-edit ang `bw_adjust` parameter: 

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![less smooth bodymass line](../../../../translated_images/density3.84ae27da82f31e6b83ad977646f029a1d21186574d7581facd70123b3eb257ee.tl.png)

✅ Basahin ang tungkol sa mga parameter na magagamit para sa ganitong uri ng plot at mag-eksperimento!

Ang ganitong uri ng tsart ay nag-aalok ng magagandang paliwanag na visualisasyon. Sa ilang linya ng code, halimbawa, maaari mong ipakita ang max body mass density ayon sa Order ng ibon:

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![bodymass per order](../../../../translated_images/density4.e9d6c033f15c500fd33df94cb592b9f5cf1ed2a3d213c448a3f9e97ba39573ce.tl.png)

Maaari mo ring i-map ang density ng ilang mga variable sa isang tsart. Subukan ang MaxLength at MinLength ng isang ibon kumpara sa kanilang katayuan ng konserbasyon:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![multiple densities, superimposed](../../../../translated_images/multi.56548caa9eae8d0fd9012a8586295538c7f4f426e2abc714ba070e2e4b1fc2c1.tl.png)

Marahil ay sulit na pag-aralan kung ang cluster ng 'Vulnerable' na mga ibon ayon sa kanilang haba ay may kahulugan o wala.

## 🚀 Hamon

Ang mga histogram ay mas sopistikadong uri ng tsart kaysa sa mga basic scatterplots, bar charts, o line charts. Maghanap sa internet ng magagandang halimbawa ng paggamit ng mga histogram. Paano sila ginagamit, ano ang kanilang ipinapakita, at sa anong mga larangan o lugar ng pag-aaral sila karaniwang ginagamit?

## [Post-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/19)

## Pagsusuri at Pag-aaral sa Sarili

Sa araling ito, ginamit mo ang Matplotlib at nagsimulang gumamit ng Seaborn upang makabuo ng mas sopistikadong mga tsart. Mag-research tungkol sa `kdeplot` sa Seaborn, isang "continuous probability density curve in one or more dimensions". Basahin ang [dokumentasyon](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) upang maunawaan kung paano ito gumagana.

## Gawain

[Ilapat ang iyong mga kasanayan](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.