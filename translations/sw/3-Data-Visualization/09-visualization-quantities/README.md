<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a49d78e32e280c410f04e5f2a2068e77",
  "translation_date": "2025-09-05T17:13:05+00:00",
  "source_file": "3-Data-Visualization/09-visualization-quantities/README.md",
  "language_code": "sw"
}
-->
# Kuonyesha Kiasi

|![ Sketchnote na [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/09-Visualizing-Quantities.png)|
|:---:|
| Kuonyesha Kiasi - _Sketchnote na [@nitya](https://twitter.com/nitya)_ |

Katika somo hili, utachunguza jinsi ya kutumia moja ya maktaba nyingi za Python ili kujifunza jinsi ya kuunda taswira za kuvutia zinazohusiana na dhana ya kiasi. Kwa kutumia seti ya data iliyosafishwa kuhusu ndege wa Minnesota, unaweza kujifunza mambo mengi ya kuvutia kuhusu wanyama wa porini wa eneo hilo.  
## [Jaribio la kabla ya somo](https://ff-quizzes.netlify.app/en/ds/quiz/16)

## Angalia upana wa mabawa kwa kutumia Matplotlib

Maktaba bora ya kuunda michoro rahisi na ngumu za aina mbalimbali ni [Matplotlib](https://matplotlib.org/stable/index.html). Kwa ujumla, mchakato wa kuchora data kwa kutumia maktaba hizi unajumuisha kutambua sehemu za dataframe yako unayotaka kulenga, kufanya mabadiliko yoyote yanayohitajika kwenye data hiyo, kupeana thamani za mhimili wa x na y, kuamua aina ya mchoro wa kuonyesha, na kisha kuonyesha mchoro huo. Matplotlib inatoa aina nyingi za taswira, lakini kwa somo hili, hebu tuzingatie zile zinazofaa zaidi kwa kuonyesha kiasi: chati za mstari, scatterplots, na bar plots.

> ✅ Tumia chati bora inayofaa muundo wa data yako na hadithi unayotaka kusimulia.  
> - Kuchambua mwenendo kwa muda: mstari  
> - Kulinganisha thamani: bar, column, pie, scatterplot  
> - Kuonyesha jinsi sehemu zinavyohusiana na jumla: pie  
> - Kuonyesha usambazaji wa data: scatterplot, bar  
> - Kuonyesha mwenendo: mstari, column  
> - Kuonyesha uhusiano kati ya thamani: mstari, scatterplot, bubble  

Ikiwa una seti ya data na unahitaji kugundua kiasi cha kipengee fulani kilichojumuishwa, moja ya kazi za kwanza ulizonazo ni kuchunguza thamani zake.  

✅ Kuna 'cheat sheets' nzuri sana zinazopatikana kwa Matplotlib [hapa](https://matplotlib.org/cheatsheets/cheatsheets.pdf).

## Unda mchoro wa mstari kuhusu thamani za upana wa mabawa ya ndege

Fungua faili `notebook.ipynb` kwenye mzizi wa folda ya somo hili na ongeza seli.  

> Kumbuka: data imehifadhiwa kwenye mzizi wa repo hii katika folda ya `/data`.

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```  
Data hii ni mchanganyiko wa maandishi na namba:

|      | Jina                          | Jina la Kisayansi      | Kategoria             | Order        | Family   | Genus       | Hali ya Uhifadhi   | MinLength | MaxLength | MinBodyMass | MaxBodyMass | MinWingspan | MaxWingspan |
| ---: | :---------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | --------: | --------: | ----------: | ----------: | ----------: | ----------: |
|    0 | Black-bellied whistling-duck | Dendrocygna autumnalis | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        47 |        56 |         652 |        1020 |          76 |          94 |
|    1 | Fulvous whistling-duck       | Dendrocygna bicolor    | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Dendrocygna | LC                 |        45 |        53 |         712 |        1050 |          85 |          93 |
|    2 | Snow goose                   | Anser caerulescens     | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        79 |        2050 |        4050 |         135 |         165 |
|    3 | Ross's goose                 | Anser rossii           | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |      57.3 |        64 |        1066 |        1567 |         113 |         116 |
|    4 | Greater white-fronted goose  | Anser albifrons        | Ducks/Geese/Waterfowl | Anseriformes | Anatidae | Anser       | LC                 |        64 |        81 |        1930 |        3310 |         130 |         165 |

Hebu tuanze kwa kuchora baadhi ya data ya namba kwa kutumia mchoro wa mstari wa msingi. Tuseme unataka kuona upana wa mabawa wa juu zaidi kwa ndege hawa wa kuvutia.

```python
wingspan = birds['MaxWingspan'] 
wingspan.plot()
```  
![Max Wingspan](../../../../3-Data-Visualization/09-visualization-quantities/images/max-wingspan-02.png)

Unagundua nini mara moja? Inaonekana kuna angalau kipengee kimoja cha kipekee - huo ni upana mkubwa wa mabawa! Upana wa mabawa wa sentimita 2300 ni sawa na mita 23 - kuna Pterodactyls wanaozunguka Minnesota? Hebu tuchunguze.  

Ingawa unaweza kufanya mpangilio wa haraka katika Excel ili kupata vipengee vya kipekee, ambavyo pengine ni makosa ya uandishi, endelea na mchakato wa taswira kwa kufanya kazi kutoka ndani ya mchoro.  

Ongeza lebo kwenye mhimili wa x ili kuonyesha aina gani ya ndege inahusika:

```
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.xticks(rotation=45)
x = birds['Name'] 
y = birds['MaxWingspan']

plt.plot(x, y)

plt.show()
```  
![wingspan with labels](../../../../3-Data-Visualization/09-visualization-quantities/images/max-wingspan-labels-02.png)

Hata ukiweka mzunguko wa lebo kwa digrii 45, kuna nyingi sana kusoma. Hebu jaribu mkakati tofauti: lebo tu vipengee vya kipekee na weka lebo ndani ya mchoro. Unaweza kutumia mchoro wa scatter ili kutoa nafasi zaidi kwa kuweka lebo:

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)

for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    plt.plot(x, y, 'bo')
    if birds['MaxWingspan'][i] > 500:
        plt.text(x, y * (1 - 0.05), birds['Name'][i], fontsize=12)
    
plt.show()
```  
Nini kinaendelea hapa? Ulitumia `tick_params` kuficha lebo za chini na kisha ukaunda mzunguko juu ya seti yako ya data ya ndege. Ukichora mchoro kwa kutumia nukta ndogo za bluu kwa `bo`, ulitafuta ndege yoyote yenye upana wa mabawa wa juu zaidi ya 500 na ukaonyesha lebo yao karibu na nukta ikiwa ni hivyo. Uliongeza kidogo lebo kwenye mhimili wa y (`y * (1 - 0.05)`) na ukatumia jina la ndege kama lebo.  

Umegundua nini?  

![outliers](../../../../3-Data-Visualization/09-visualization-quantities/images/labeled-wingspan-02.png)  
## Chuja data yako  

Bald Eagle na Prairie Falcon, ingawa pengine ni ndege wakubwa sana, inaonekana wameandikwa vibaya, na `0` ya ziada imeongezwa kwenye upana wao wa mabawa wa juu zaidi. Haiwezekani kukutana na Bald Eagle yenye upana wa mabawa wa mita 25, lakini ikiwa ni hivyo, tafadhali tujulishe! Hebu tuunde dataframe mpya bila vipengee hivyo vya kipekee:  

```python
plt.title('Max Wingspan in Centimeters')
plt.ylabel('Wingspan (CM)')
plt.xlabel('Birds')
plt.tick_params(axis='both',which='both',labelbottom=False,bottom=False)
for i in range(len(birds)):
    x = birds['Name'][i]
    y = birds['MaxWingspan'][i]
    if birds['Name'][i] not in ['Bald eagle', 'Prairie falcon']:
        plt.plot(x, y, 'bo')
plt.show()
```  

Kwa kuchuja vipengee vya kipekee, data yako sasa ni ya mshikamano na inayoeleweka.  

![scatterplot of wingspans](../../../../3-Data-Visualization/09-visualization-quantities/images/scatterplot-wingspan-02.png)  

Sasa kwa kuwa tuna seti ya data safi angalau kwa suala la upana wa mabawa, hebu tujifunze zaidi kuhusu ndege hawa.  

Ingawa michoro ya mstari na scatter inaweza kuonyesha taarifa kuhusu thamani za data na usambazaji wake, tunataka kufikiria kuhusu thamani zilizomo katika seti hii ya data. Unaweza kuunda taswira ili kujibu maswali yafuatayo kuhusu kiasi:  

> Kuna kategoria ngapi za ndege, na idadi yao ni ngapi?  
> Kuna ndege wangapi waliopotea, walio hatarini, nadra, au wa kawaida?  
> Kuna idadi gani ya genus na order mbalimbali kulingana na terminolojia ya Linnaeus?  
## Chunguza chati za bar  

Chati za bar ni za vitendo unapohitaji kuonyesha makundi ya data. Hebu tuchunguze kategoria za ndege zilizopo katika seti hii ya data ili kuona ni ipi iliyo ya kawaida zaidi kwa idadi.  

Katika faili ya notebook, unda chati ya bar ya msingi  

✅ Kumbuka, unaweza kuchuja ndege wawili wa kipekee tulioainisha katika sehemu iliyopita, kuhariri makosa ya uandishi katika upana wao wa mabawa, au kuwaacha kwa mazoezi haya ambayo hayategemei thamani za upana wa mabawa.  

Ikiwa unataka kuunda chati ya bar, unaweza kuchagua data unayotaka kuzingatia. Chati za bar zinaweza kuundwa kutoka kwa data ghafi:  

```python
birds.plot(x='Category',
        kind='bar',
        stacked=True,
        title='Birds of Minnesota')

```  
![full data as a bar chart](../../../../3-Data-Visualization/09-visualization-quantities/images/full-data-bar-02.png)  

Hata hivyo, chati hii ya bar haiwezi kusomeka kwa sababu kuna data nyingi zisizo na makundi. Unahitaji kuchagua tu data unayotaka kuchora, kwa hivyo hebu tuangalie urefu wa ndege kulingana na kategoria yao.  

Chuja data yako ili kujumuisha tu kategoria ya ndege.  

✅ Kumbuka kwamba unatumia Pandas kusimamia data, na kisha unaruhusu Matplotlib kufanya uchoraji.  

Kwa kuwa kuna kategoria nyingi, unaweza kuonyesha chati hii kwa wima na kurekebisha urefu wake ili kuzingatia data yote:  

```python
category_count = birds.value_counts(birds['Category'].values, sort=True)
plt.rcParams['figure.figsize'] = [6, 12]
category_count.plot.barh()
```  
![category and length](../../../../3-Data-Visualization/09-visualization-quantities/images/category-counts-02.png)  

Chati hii ya bar inaonyesha mtazamo mzuri wa idadi ya ndege katika kila kategoria. Kwa haraka, unaona kwamba idadi kubwa ya ndege katika eneo hili wako katika kategoria ya Ducks/Geese/Waterfowl. Minnesota ni 'ardhi ya maziwa 10,000' kwa hivyo hili halishangazi!  

✅ Jaribu hesabu nyingine kwenye seti hii ya data. Kuna kitu chochote kinachokushangaza?  

## Kulinganisha data  

Unaweza kujaribu kulinganisha data ya makundi tofauti kwa kuunda axes mpya. Jaribu kulinganisha MaxLength ya ndege, kulingana na kategoria yake:  

```python
maxlength = birds['MaxLength']
plt.barh(y=birds['Category'], width=maxlength)
plt.rcParams['figure.figsize'] = [6, 12]
plt.show()
```  
![comparing data](../../../../3-Data-Visualization/09-visualization-quantities/images/category-length-02.png)  

Hakuna kinachoshangaza hapa: hummingbirds wana MaxLength ndogo zaidi ikilinganishwa na Pelicans au Geese. Ni vizuri data inapofanya mantiki!  

Unaweza kuunda taswira za kuvutia zaidi za chati za bar kwa kuweka data juu ya nyingine. Hebu tuweke Minimum na Maximum Length kwenye kategoria ya ndege fulani:  

```python
minLength = birds['MinLength']
maxLength = birds['MaxLength']
category = birds['Category']

plt.barh(category, maxLength)
plt.barh(category, minLength)

plt.show()
```  
Katika mchoro huu, unaweza kuona anuwai kwa kategoria ya ndege ya Minimum Length na Maximum Length. Unaweza kusema kwa usalama kwamba, kulingana na data hii, ndege mkubwa zaidi ana anuwai kubwa zaidi ya urefu. Inavutia!  

![superimposed values](../../../../3-Data-Visualization/09-visualization-quantities/images/superimposed-02.png)  

## 🚀 Changamoto  

Seti hii ya data ya ndege inatoa utajiri wa taarifa kuhusu aina tofauti za ndege ndani ya mfumo fulani wa ikolojia. Tafuta mtandaoni na uone ikiwa unaweza kupata seti nyingine za data zinazohusiana na ndege. Fanya mazoezi ya kujenga chati na grafu kuhusu ndege hawa ili kugundua ukweli ambao hukujua.  

## [Jaribio la baada ya somo](https://ff-quizzes.netlify.app/en/ds/quiz/17)

## Mapitio & Kujisomea  

Somo hili la kwanza limekupa taarifa kuhusu jinsi ya kutumia Matplotlib kuonyesha kiasi. Fanya utafiti kuhusu njia nyingine za kufanya kazi na seti za data kwa taswira. [Plotly](https://github.com/plotly/plotly.py) ni moja ambayo hatutashughulikia katika masomo haya, kwa hivyo angalia kile inachoweza kutoa.  
## Kazi  

[Lines, Scatters, and Bars](assignment.md)  

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.