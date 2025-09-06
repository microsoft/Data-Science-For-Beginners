<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1cf49f029ba1f25a54f0d5bc2fa575fc",
  "translation_date": "2025-09-05T17:16:53+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/README.md",
  "language_code": "sw"
}
-->
# Utangulizi Mfupi wa Takwimu na Uwezekano

|![ Sketchnote na [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/04-Statistics-Probability.png)|
|:---:|
| Takwimu na Uwezekano - _Sketchnote na [@nitya](https://twitter.com/nitya)_ |

Nadharia ya Takwimu na Uwezekano ni maeneo mawili yanayohusiana sana ya Hisabati ambayo yana umuhimu mkubwa katika Sayansi ya Takwimu. Inawezekana kufanya kazi na data bila ujuzi wa kina wa hisabati, lakini ni bora kujua angalau dhana za msingi. Hapa tutatoa utangulizi mfupi ambao utakusaidia kuanza.

[![Video ya Utangulizi](../../../../1-Introduction/04-stats-and-probability/images/video-prob-and-stats.png)](https://youtu.be/Z5Zy85g4Yjw)

## [Jaribio la awali la somo](https://ff-quizzes.netlify.app/en/ds/quiz/6)

## Uwezekano na Vigezo vya Nasibu

**Uwezekano** ni namba kati ya 0 na 1 inayowakilisha jinsi tukio fulani lilivyo na uwezekano wa kutokea. Uwezekano hufafanuliwa kama idadi ya matokeo chanya (yanayopelekea tukio hilo), ikigawanywa na idadi ya jumla ya matokeo, kwa sharti kwamba matokeo yote yana uwezekano sawa. Kwa mfano, tunapopiga kete, uwezekano wa kupata namba shufwa ni 3/6 = 0.5.

Tunapozungumzia matukio, tunatumia **vigezo vya nasibu**. Kwa mfano, kigezo cha nasibu kinachowakilisha namba inayopatikana tunapopiga kete kitakuwa na thamani kati ya 1 hadi 6. Seti ya namba kutoka 1 hadi 6 inaitwa **nafasi ya sampuli**. Tunaweza kuzungumzia uwezekano wa kigezo cha nasibu kuchukua thamani fulani, kwa mfano P(X=3)=1/6.

Kigezo cha nasibu katika mfano uliopita kinaitwa **kigezo cha nasibu cha kidhahiri**, kwa sababu kina nafasi ya sampuli inayohesabika, yaani kuna thamani tofauti zinazoweza kuorodheshwa. Kuna hali ambapo nafasi ya sampuli ni safu ya namba halisi, au seti nzima ya namba halisi. Vigezo kama hivyo vinaitwa **vigezo vya nasibu vya kuendelea**. Mfano mzuri ni muda wa kuwasili kwa basi.

## Usambazaji wa Uwezekano

Kwa vigezo vya nasibu vya kidhahiri, ni rahisi kuelezea uwezekano wa kila tukio kwa kutumia kazi P(X). Kwa kila thamani *s* kutoka nafasi ya sampuli *S* itatoa namba kati ya 0 na 1, ambapo jumla ya thamani zote za P(X=s) kwa matukio yote itakuwa 1.

Usambazaji maarufu zaidi wa kidhahiri ni **usambazaji wa sare**, ambapo kuna nafasi ya sampuli ya vipengele N, na uwezekano sawa wa 1/N kwa kila moja.

Ni vigumu zaidi kuelezea usambazaji wa uwezekano wa kigezo cha kuendelea, chenye thamani zinazotolewa kutoka kwa safu fulani [a,b], au seti nzima ya namba halisi ℝ. Fikiria hali ya muda wa kuwasili kwa basi. Kwa kweli, kwa kila muda halisi wa kuwasili *t*, uwezekano wa basi kuwasili hasa wakati huo ni 0!

> Sasa unajua kwamba matukio yenye uwezekano wa 0 hutokea, na mara nyingi sana! Angalau kila wakati basi linapowasili!

Tunaweza tu kuzungumzia uwezekano wa kigezo kuangukia katika safu fulani ya thamani, kwa mfano P(t<sub>1</sub>≤X<t<sub>2</sub>). Katika hali hii, usambazaji wa uwezekano unafafanuliwa na **kazi ya msongamano wa uwezekano** p(x), ambapo

![P(t_1\le X<t_2)=\int_{t_1}^{t_2}p(x)dx](../../../../1-Introduction/04-stats-and-probability/images/probability-density.png)

Mfano wa kuendelea wa usambazaji wa sare unaitwa **sare ya kuendelea**, ambayo hufafanuliwa katika safu yenye kikomo. Uwezekano kwamba thamani X itaangukia katika safu ya urefu l ni sawia na l, na huongezeka hadi 1.

Usambazaji mwingine muhimu ni **usambazaji wa kawaida**, ambao tutazungumzia kwa undani zaidi hapa chini.

## Wastani, Tofauti na Mkengeuko wa Kawaida

Tuseme tunachukua mfululizo wa sampuli n za kigezo cha nasibu X: x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>. Tunaweza kufafanua thamani ya **wastani** (au **wastani wa hesabu**) wa mfululizo kwa njia ya jadi kama (x<sub>1</sub>+x<sub>2</sub>+x<sub>n</sub>)/n. Tunapoongeza ukubwa wa sampuli (yaani kuchukua kikomo na n→∞), tutapata wastani (pia huitwa **matarajio**) ya usambazaji. Tutataja matarajio kwa **E**(x).

> Inaweza kuonyeshwa kwamba kwa usambazaji wowote wa kidhahiri wenye thamani {x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>N</sub>} na uwezekano unaolingana p<sub>1</sub>, p<sub>2</sub>, ..., p<sub>N</sub>, matarajio yatakuwa E(X)=x<sub>1</sub>p<sub>1</sub>+x<sub>2</sub>p<sub>2</sub>+...+x<sub>N</sub>p<sub>N</sub>.

Ili kutambua jinsi thamani zilivyo mbali, tunaweza kuhesabu tofauti σ<sup>2</sup> = ∑(x<sub>i</sub> - μ)<sup>2</sup>/n, ambapo μ ni wastani wa mfululizo. Thamani σ inaitwa **mkengeuko wa kawaida**, na σ<sup>2</sup> inaitwa **tofauti**.

## Modi, Median na Robo

Wakati mwingine, wastani hauwakilishi vyema thamani "ya kawaida" ya data. Kwa mfano, wakati kuna thamani chache za kupindukia ambazo ziko nje kabisa ya safu, zinaweza kuathiri wastani. Kiashiria kingine kizuri ni **median**, thamani ambayo nusu ya alama za data ziko chini yake, na nusu nyingine - juu yake.

Ili kutusaidia kuelewa usambazaji wa data, ni muhimu kuzungumzia **robo**:

* Robo ya kwanza, au Q1, ni thamani ambayo 25% ya data iko chini yake
* Robo ya tatu, au Q3, ni thamani ambayo 75% ya data iko chini yake

Kigrafiki tunaweza kuwakilisha uhusiano kati ya median na robo katika mchoro unaoitwa **box plot**:

<img src="images/boxplot_explanation.png" width="50%"/>

Hapa pia tunahesabu **nafasi ya kati ya robo** IQR=Q3-Q1, na kinachoitwa **vipimo vya kupindukia** - thamani ambazo ziko nje ya mipaka [Q1-1.5*IQR,Q3+1.5*IQR].

Kwa usambazaji finyu unaojumuisha idadi ndogo ya thamani zinazowezekana, thamani nzuri "ya kawaida" ni ile inayojitokeza mara nyingi zaidi, ambayo inaitwa **modi**. Mara nyingi hutumika kwa data ya kategoria, kama vile rangi. Fikiria hali ambapo tuna vikundi viwili vya watu - baadhi wanapendelea sana nyekundu, na wengine wanapendelea bluu. Ikiwa tunapanga rangi kwa namba, thamani ya wastani kwa rangi inayopendwa itakuwa mahali fulani katika wigo wa machungwa-kijani, ambayo haionyeshi upendeleo halisi wa kundi lolote. Hata hivyo, modi itakuwa mojawapo ya rangi, au rangi zote mbili, ikiwa idadi ya watu wanaopendelea ni sawa (katika hali hii tunaita sampuli **multimodal**).

## Data ya Ulimwengu Halisi

Tunapochambua data kutoka maisha halisi, mara nyingi si vigezo vya nasibu kama hivyo, kwa maana kwamba hatufanyi majaribio yenye matokeo yasiyojulikana. Kwa mfano, fikiria timu ya wachezaji wa baseball, na data zao za mwili, kama vile urefu, uzito na umri. Namba hizo si nasibu hasa, lakini bado tunaweza kutumia dhana zile zile za hisabati. Kwa mfano, mfululizo wa uzito wa watu unaweza kuchukuliwa kuwa mfululizo wa thamani zinazotolewa kutoka kwa kigezo fulani cha nasibu. Hapa chini ni mfululizo wa uzito wa wachezaji halisi wa baseball kutoka [Major League Baseball](http://mlb.mlb.com/index.jsp), iliyochukuliwa kutoka [seti hii ya data](http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights) (kwa urahisi wako, thamani 20 za kwanza tu zimeonyeshwa):

```
[180.0, 215.0, 210.0, 210.0, 188.0, 176.0, 209.0, 200.0, 231.0, 180.0, 188.0, 180.0, 185.0, 160.0, 180.0, 185.0, 197.0, 189.0, 185.0, 219.0]
```

> **Note**: Ili kuona mfano wa kufanya kazi na seti hii ya data, angalia [notebook inayohusiana](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb). Pia kuna changamoto kadhaa katika somo hili, na unaweza kuzimaliza kwa kuongeza baadhi ya msimbo kwenye notebook hiyo. Ikiwa huna uhakika jinsi ya kufanya kazi na data, usijali - tutarudi kwenye kufanya kazi na data kwa kutumia Python baadaye. Ikiwa hujui jinsi ya kuendesha msimbo katika Jupyter Notebook, angalia [makala hii](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

Hapa kuna mchoro wa box plot unaoonyesha wastani, median na robo za data yetu:

![Weight Box Plot](../../../../1-Introduction/04-stats-and-probability/images/weight-boxplot.png)

Kwa kuwa data yetu ina taarifa kuhusu **majukumu** tofauti ya wachezaji, tunaweza pia kufanya box plot kwa majukumu - itaturuhusu kupata wazo la jinsi thamani za vigezo zinavyotofautiana kati ya majukumu. Wakati huu tutazingatia urefu:

![Box plot by role](../../../../1-Introduction/04-stats-and-probability/images/boxplot_byrole.png)

Mchoro huu unaonyesha kwamba, kwa wastani, urefu wa wachezaji wa nafasi ya kwanza ni mkubwa kuliko urefu wa wachezaji wa nafasi ya pili. Baadaye katika somo hili tutajifunza jinsi tunavyoweza kujaribu dhana hii kwa njia rasmi zaidi, na jinsi ya kuonyesha kwamba data yetu ina umuhimu wa takwimu kuonyesha hivyo.

> Tunapofanya kazi na data ya ulimwengu halisi, tunadhani kwamba alama zote za data ni sampuli zinazotolewa kutoka kwa usambazaji fulani wa uwezekano. Dhana hii inaturuhusu kutumia mbinu za kujifunza kwa mashine na kujenga mifano ya utabiri inayofanya kazi.

Ili kuona usambazaji wa data yetu, tunaweza kuchora grafu inayoitwa **histogramu**. X-axis itakuwa na idadi ya vipindi tofauti vya uzito (inayojulikana kama **bins**), na mhimili wima utaonyesha idadi ya mara ambazo sampuli ya kigezo cha nasibu ilikuwa ndani ya kipindi fulani.

![Histogram ya data ya ulimwengu halisi](../../../../1-Introduction/04-stats-and-probability/images/weight-histogram.png)

Kutoka kwa histogramu hii unaweza kuona kwamba thamani zote ziko katikati ya wastani fulani wa uzito, na kadri tunavyoenda mbali na uzito huo - namba za uzito wa thamani hiyo zinapungua. Yaani, ni nadra sana kwamba uzito wa mchezaji wa baseball utakuwa tofauti sana na wastani wa uzito. Tofauti ya uzito inaonyesha kiwango ambacho uzito unaweza kutofautiana kutoka kwa wastani.

> Ikiwa tunachukua uzito wa watu wengine, si kutoka ligi ya baseball, usambazaji unaweza kuwa tofauti. Hata hivyo, umbo la usambazaji litakuwa sawa, lakini wastani na tofauti zitabadilika. Kwa hivyo, ikiwa tunafundisha mfano wetu kwa wachezaji wa baseball, kuna uwezekano wa kutoa matokeo yasiyo sahihi unapowekwa kwa wanafunzi wa chuo kikuu, kwa sababu usambazaji wa msingi ni tofauti.

## Usambazaji wa Kawaida

Usambazaji wa uzito ambao tumeona hapo juu ni wa kawaida sana, na vipimo vingi kutoka ulimwengu halisi vinafuata aina hiyo ya usambazaji, lakini kwa wastani na tofauti tofauti. Usambazaji huu unaitwa **usambazaji wa kawaida**, na una jukumu muhimu sana katika takwimu.

Kutumia usambazaji wa kawaida ni njia sahihi ya kuzalisha uzito wa nasibu wa wachezaji wa baseball wa baadaye. Mara tu tunapojua wastani wa uzito `mean` na mkengeuko wa kawaida `std`, tunaweza kuzalisha sampuli 1000 za uzito kwa njia ifuatayo:
```python
samples = np.random.normal(mean,std,1000)
```

Ikiwa tunachora histogramu ya sampuli zilizozalishwa tutaona picha inayofanana sana na ile iliyoonyeshwa hapo juu. Na ikiwa tunaongeza idadi ya sampuli na idadi ya bins, tunaweza kuzalisha picha ya usambazaji wa kawaida ambayo inakaribia kuwa bora:

![Usambazaji wa Kawaida na wastani=0 na mkengeuko wa kawaida=1](../../../../1-Introduction/04-stats-and-probability/images/normal-histogram.png)

*Usambazaji wa Kawaida na wastani=0 na mkengeuko wa kawaida=1*

## Vipindi vya Uhakika

Tunapozungumzia uzito wa wachezaji wa baseball, tunadhani kwamba kuna **kigezo cha nasibu W** kinachowakilisha usambazaji bora wa uwezekano wa uzito wa wachezaji wote wa baseball (inayojulikana kama **idadi ya watu**). Mfululizo wetu wa uzito unahusiana na sehemu ndogo ya wachezaji wote wa baseball tunayoita **sampuli**. Swali la kuvutia ni, je, tunaweza kujua vigezo vya usambazaji wa W, yaani wastani na tofauti ya idadi ya watu?

Jibu rahisi litakuwa kuhesabu wastani na tofauti ya sampuli yetu. Hata hivyo, inaweza kutokea kwamba sampuli yetu ya nasibu haionyeshi kwa usahihi idadi kamili ya watu. Kwa hivyo inafaa kuzungumzia **kipindi cha uhakika**.

> **Kipindi cha uhakika** ni makadirio ya wastani halisi wa idadi ya watu kutokana na sampuli yetu, ambayo ni sahihi kwa uwezekano fulani (au **kiwango cha uhakika**).

Tuseme tuna sampuli X

1</sub>, ..., X<sub>n</sub> kutoka kwa usambazaji wetu. Kila mara tunapochukua sampuli kutoka kwa usambazaji wetu, tunapata thamani tofauti ya wastani μ. Kwa hivyo, μ inaweza kuchukuliwa kama kiashiria cha nasibu. **Kipindi cha kujiamini** chenye kujiamini p ni jozi ya thamani (L<sub>p</sub>,R<sub>p</sub>), ambapo **P**(L<sub>p</sub>≤μ≤R<sub>p</sub>) = p, yaani uwezekano wa thamani ya wastani kupatikana ndani ya kipindi ni sawa na p.

Inazidi utangulizi wetu mfupi kujadili kwa undani jinsi vipindi hivyo vya kujiamini vinavyohesabiwa. Maelezo zaidi yanaweza kupatikana [kwenye Wikipedia](https://en.wikipedia.org/wiki/Confidence_interval). Kwa ufupi, tunafafanua usambazaji wa wastani wa sampuli uliopatikana kulingana na wastani halisi wa idadi ya watu, unaoitwa **usambazaji wa mwanafunzi**.

> **Ukweli wa kuvutia**: Usambazaji wa mwanafunzi umepewa jina la mwanafizikia William Sealy Gosset, ambaye alichapisha karatasi yake kwa jina la bandia "Student". Alifanya kazi katika kiwanda cha bia cha Guinness, na, kulingana na mojawapo ya matoleo, mwajiri wake hakutaka umma kujua kwamba walikuwa wakitumia majaribio ya takwimu kuamua ubora wa malighafi.

Ikiwa tunataka kukadiria wastani μ wa idadi yetu ya watu kwa kujiamini p, tunahitaji kuchukua *(1-p)/2-th percentile* ya Usambazaji wa Mwanafunzi A, ambayo inaweza kuchukuliwa kutoka kwa jedwali, au kuhesabiwa kwa kutumia baadhi ya kazi za ndani za programu za takwimu (mfano Python, R, nk.). Kisha kipindi cha μ kitakuwa X±A*D/√n, ambapo X ni wastani uliopatikana wa sampuli, D ni mkengeuko wa kawaida.

> **Kumbuka**: Tunapuuza pia mjadala wa dhana muhimu ya [digrii za uhuru](https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics)), ambayo ni muhimu kuhusiana na Usambazaji wa Mwanafunzi. Unaweza kurejelea vitabu kamili zaidi vya takwimu ili kuelewa dhana hii kwa undani.

Mfano wa kuhesabu kipindi cha kujiamini kwa uzito na urefu umetolewa katika [majarida yanayoambatana](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb).

| p | Wastani wa Uzito |
|-----|-----------|
| 0.85 | 201.73±0.94 |
| 0.90 | 201.73±1.08 |
| 0.95 | 201.73±1.28 |

Angalia kwamba kadri uwezekano wa kujiamini unavyoongezeka, ndivyo kipindi cha kujiamini kinavyopanuka.

## Upimaji wa Dhana

Katika seti yetu ya data ya wachezaji wa baseball, kuna majukumu tofauti ya wachezaji, ambayo yanaweza kufupishwa hapa chini (angalia [majarida yanayoambatana](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb) ili kuona jinsi jedwali hili linavyoweza kuhesabiwa):

| Jukumu | Urefu | Uzito | Idadi |
|------|--------|--------|-------|
| Catcher | 72.723684 | 204.328947 | 76 |
| Designated_Hitter | 74.222222 | 220.888889 | 18 |
| First_Baseman | 74.000000 | 213.109091 | 55 |
| Outfielder | 73.010309 | 199.113402 | 194 |
| Relief_Pitcher | 74.374603 | 203.517460 | 315 |
| Second_Baseman | 71.362069 | 184.344828 | 58 |
| Shortstop | 71.903846 | 182.923077 | 52 |
| Starting_Pitcher | 74.719457 | 205.163636 | 221 |
| Third_Baseman | 73.044444 | 200.955556 | 45 |

Tunaweza kuona kwamba wastani wa urefu wa first basemen ni mkubwa kuliko wa second basemen. Kwa hivyo, tunaweza kushawishika kusema kwamba **first basemen ni warefu kuliko second basemen**.

> Kauli hii inaitwa **dhana**, kwa sababu hatujui kama ukweli huu ni sahihi au la.

Hata hivyo, si rahisi kila mara kusema kama tunaweza kufanya hitimisho hili. Kutoka kwa mjadala hapo juu tunajua kwamba kila wastani una kipindi cha kujiamini kinachohusiana, na kwa hivyo tofauti hii inaweza tu kuwa kosa la takwimu. Tunahitaji njia rasmi zaidi ya kupima dhana yetu.

Hebu tuhesabu vipindi vya kujiamini kando kwa urefu wa first na second basemen:

| Kujiamini | First Basemen | Second Basemen |
|------------|---------------|----------------|
| 0.85 | 73.62..74.38 | 71.04..71.69 |
| 0.90 | 73.56..74.44 | 70.99..71.73 |
| 0.95 | 73.47..74.53 | 70.92..71.81 |

Tunaweza kuona kwamba chini ya kujiamini yoyote vipindi havingiliani. Hii inathibitisha dhana yetu kwamba first basemen ni warefu kuliko second basemen.

Kwa njia rasmi zaidi, tatizo tunalotatua ni kuona kama **usambazaji mbili za uwezekano ni sawa**, au angalau zina vigezo sawa. Kutegemea usambazaji, tunahitaji kutumia majaribio tofauti kwa hilo. Ikiwa tunajua kwamba usambazaji wetu ni wa kawaida, tunaweza kutumia **[Student t-test](https://en.wikipedia.org/wiki/Student%27s_t-test)**.

Katika Student t-test, tunahesabu kinachoitwa **t-value**, ambacho kinaonyesha tofauti kati ya wastani, kwa kuzingatia mkengeuko. Imeonyeshwa kwamba t-value inafuata **usambazaji wa mwanafunzi**, ambao huturuhusu kupata thamani ya kizingiti kwa kiwango cha kujiamini **p** (hii inaweza kuhesabiwa, au kuangaliwa kwenye jedwali za nambari). Kisha tunalinganisha t-value na kizingiti hiki ili kuidhinisha au kukataa dhana.

Katika Python, tunaweza kutumia kifurushi cha **SciPy**, ambacho kinajumuisha kazi ya `ttest_ind` (pamoja na kazi nyingine nyingi za takwimu muhimu!). Inahesabu t-value kwa ajili yetu, na pia hufanya utafutaji wa kinyume wa p-value ya kujiamini, ili tuweze kuangalia tu kujiamini ili kufanya hitimisho.

Kwa mfano, kulinganisha kwetu kati ya urefu wa first na second basemen kunatupa matokeo yafuatayo:
```python
from scipy.stats import ttest_ind

tval, pval = ttest_ind(df.loc[df['Role']=='First_Baseman',['Height']], df.loc[df['Role']=='Designated_Hitter',['Height']],equal_var=False)
print(f"T-value = {tval[0]:.2f}\nP-value: {pval[0]}")
```
```
T-value = 7.65
P-value: 9.137321189738925e-12
```
Katika kesi yetu, p-value ni ndogo sana, ikimaanisha kwamba kuna ushahidi mkubwa unaounga mkono kwamba first basemen ni warefu.

Kuna aina nyingine tofauti za dhana ambazo tunaweza kutaka kupima, kwa mfano:
* Kuthibitisha kwamba sampuli fulani inafuata usambazaji fulani. Katika kesi yetu tumedhani kwamba urefu umegawanywa kawaida, lakini hiyo inahitaji uthibitisho rasmi wa takwimu.
* Kuthibitisha kwamba thamani ya wastani wa sampuli inalingana na thamani fulani iliyowekwa
* Kulinganisha wastani wa idadi ya sampuli (mfano, tofauti ya viwango vya furaha kati ya vikundi vya umri tofauti)

## Sheria ya Nambari Kubwa na Theoremu ya Kikomo cha Kati

Moja ya sababu kwa nini usambazaji wa kawaida ni muhimu ni kinachoitwa **theoremu ya kikomo cha kati**. Tuseme tuna sampuli kubwa ya N ya thamani huru X<sub>1</sub>, ..., X<sub>N</sub>, iliyochukuliwa kutoka kwa usambazaji wowote wenye wastani μ na mkengeuko σ<sup>2</sup>. Kisha, kwa N kubwa ya kutosha (kwa maneno mengine, wakati N→∞), wastani Σ<sub>i</sub>X<sub>i</sub> utakuwa umegawanywa kawaida, wenye wastani μ na mkengeuko σ<sup>2</sup>/N.

> Njia nyingine ya kufasiri theoremu ya kikomo cha kati ni kusema kwamba bila kujali usambazaji, unapohesabu wastani wa jumla ya thamani yoyote ya kiashiria cha nasibu unapata usambazaji wa kawaida.

Kutoka kwa theoremu ya kikomo cha kati pia inafuata kwamba, wakati N→∞, uwezekano wa wastani wa sampuli kuwa sawa na μ unakuwa 1. Hii inajulikana kama **sheria ya nambari kubwa**.

## Uhusiano wa Pamoja na Uwiano

Moja ya mambo ambayo Sayansi ya Takwimu hufanya ni kutafuta uhusiano kati ya data. Tunaposema kwamba mfululizo miwili **ina uhusiano wa pamoja** tunamaanisha kwamba inaonyesha tabia sawa kwa wakati mmoja, yaani inainuka/kushuka kwa pamoja, au mfululizo mmoja unainuka wakati mwingine unashuka na kinyume chake. Kwa maneno mengine, kunaonekana kuwa na uhusiano fulani kati ya mfululizo miwili.

> Uhusiano wa pamoja hauonyeshi lazima uhusiano wa kisababishi kati ya mfululizo miwili; wakati mwingine vigezo vyote vinaweza kutegemea sababu ya nje, au inaweza kuwa kwa bahati tu kwamba mfululizo miwili una uhusiano wa pamoja. Hata hivyo, uhusiano wa pamoja wa kihesabu wenye nguvu ni kiashiria kizuri kwamba vigezo viwili vina uhusiano fulani.

Kihesabu, dhana kuu inayonyesha uhusiano kati ya vigezo viwili vya nasibu ni **uhusiano wa pamoja**, ambao unahesabiwa kama hivi: Cov(X,Y) = **E**\[(X-**E**(X))(Y-**E**(Y))\]. Tunahesabu mkengeuko wa vigezo vyote kutoka kwa wastani wao, kisha tunazidisha mkengeuko huo. Ikiwa vigezo vyote vinatofautiana pamoja, kuzidisha kutakuwa na thamani chanya kila mara, ambayo itaongeza hadi uhusiano wa pamoja chanya. Ikiwa vigezo vyote vinatofautiana bila mpangilio (yaani moja linashuka chini ya wastani wakati lingine linapanda juu ya wastani), tutapata nambari hasi kila mara, ambayo itaongeza hadi uhusiano wa pamoja hasi. Ikiwa mkengeuko hauhusiani, utaongeza hadi takriban sifuri.

Thamani halisi ya uhusiano wa pamoja haituambii mengi kuhusu ukubwa wa uhusiano wa pamoja, kwa sababu inategemea ukubwa wa thamani halisi. Ili kuhalalisha, tunaweza kugawanya uhusiano wa pamoja kwa mkengeuko wa kawaida wa vigezo vyote, ili kupata **uwiano**. Jambo zuri ni kwamba uwiano huwa katika anuwai ya [-1,1], ambapo 1 inaonyesha uhusiano wa pamoja chanya wenye nguvu kati ya thamani, -1 - uhusiano wa pamoja hasi wenye nguvu, na 0 - hakuna uhusiano wa pamoja kabisa (vigezo ni huru).

**Mfano**: Tunaweza kuhesabu uwiano kati ya uzito na urefu wa wachezaji wa baseball kutoka kwa seti ya data iliyotajwa hapo juu:
```python
print(np.corrcoef(weights,heights))
```
Matokeo yake, tunapata **matriki ya uwiano** kama hii:
```
array([[1.        , 0.52959196],
       [0.52959196, 1.        ]])
```

> Matriki ya uwiano C inaweza kuhesabiwa kwa idadi yoyote ya mfululizo wa pembejeo S<sub>1</sub>, ..., S<sub>n</sub>. Thamani ya C<sub>ij</sub> ni uwiano kati ya S<sub>i</sub> na S<sub>j</sub>, na vipengele vya diagonal huwa 1 (ambayo pia ni uwiano wa pamoja wa S<sub>i</sub>).

Katika kesi yetu, thamani 0.53 inaonyesha kwamba kuna uhusiano fulani kati ya uzito na urefu wa mtu. Tunaweza pia kutengeneza mchoro wa kutawanyika wa thamani moja dhidi ya nyingine ili kuona uhusiano kwa macho:

![Uhusiano kati ya uzito na urefu](../../../../1-Introduction/04-stats-and-probability/images/weight-height-relationship.png)

> Mifano zaidi ya uwiano wa pamoja na uhusiano wa pamoja inaweza kupatikana katika [majarida yanayoambatana](../../../../1-Introduction/04-stats-and-probability/notebook.ipynb).

## Hitimisho

Katika sehemu hii, tumejifunza:

* mali za msingi za takwimu za data, kama vile wastani, mkengeuko, hali na robo
* usambazaji tofauti wa vigezo vya nasibu, ikiwa ni pamoja na usambazaji wa kawaida
* jinsi ya kupata uwiano kati ya mali tofauti
* jinsi ya kutumia vifaa vya sauti vya hesabu na takwimu ili kuthibitisha dhana fulani,
* jinsi ya kuhesabu vipindi vya kujiamini kwa kiashiria cha nasibu kwa kuzingatia sampuli ya data

Ingawa hii si orodha kamili ya mada zilizopo ndani ya uwezekano na takwimu, inapaswa kuwa ya kutosha kukupa mwanzo mzuri katika kozi hii.

## 🚀 Changamoto

Tumia msimbo wa sampuli katika jarida kujaribu dhana nyingine kwamba:
1. First basemen ni wazee kuliko second basemen
2. First basemen ni warefu kuliko third basemen
3. Shortstops ni warefu kuliko second basemen

## [Maswali ya baada ya somo](https://ff-quizzes.netlify.app/en/ds/quiz/7)

## Mapitio na Kujisomea

Uwezekano na takwimu ni mada pana sana inayostahili kozi yake yenyewe. Ikiwa una nia ya kwenda zaidi katika nadharia, unaweza kutaka kuendelea kusoma baadhi ya vitabu vifuatavyo:

1. [Carlos Fernandez-Granda](https://cims.nyu.edu/~cfgranda/) kutoka Chuo Kikuu cha New York ana maelezo mazuri ya mihadhara [Probability and Statistics for Data Science](https://cims.nyu.edu/~cfgranda/pages/stuff/probability_stats_for_DS.pdf) (inapatikana mtandaoni)
1. [Peter na Andrew Bruce. Practical Statistics for Data Scientists.](https://www.oreilly.com/library/view/practical-statistics-for/9781491952955/) [[msimbo wa sampuli katika R](https://github.com/andrewgbruce/statistics-for-data-scientists)]. 
1. [James D. Miller. Statistics for Data Science](https://www.packtpub.com/product/statistics-for-data-science/9781788290678) [[msimbo wa sampuli katika R](https://github.com/PacktPublishing/Statistics-for-Data-Science)]

## Kazi

[Utafiti Mdogo wa Kisukari](assignment.md)

## Credits

Somol hili limeandikwa kwa ♥️ na [Dmitry Soshnikov](http://soshnikov.com)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.