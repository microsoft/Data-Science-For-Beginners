<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d92f57eb110dc7f765c05cbf0f837c77",
  "translation_date": "2025-08-26T16:28:45+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "sw"
}
-->
# Mzunguko wa Sayansi ya Takwimu: Kuchambua

|![ Sketchnote na [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Mzunguko wa Sayansi ya Takwimu: Kuchambua - _Sketchnote na [@nitya](https://twitter.com/nitya)_ |

## Maswali ya Awali ya Somo

## [Maswali ya Awali ya Somo](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

Kuchambua katika mzunguko wa takwimu kunathibitisha kuwa takwimu zinaweza kujibu maswali yaliyopendekezwa au kutatua tatizo fulani. Hatua hii pia inaweza kuzingatia kuthibitisha kuwa modeli inashughulikia maswali na matatizo haya kwa usahihi. Somo hili linazingatia Uchambuzi wa Takwimu wa Kichunguzi au EDA, ambao ni mbinu za kufafanua vipengele na uhusiano ndani ya takwimu na zinaweza kutumika kuandaa takwimu kwa ajili ya modeli.

Tutatumia seti ya takwimu kutoka [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) kuonyesha jinsi hili linaweza kutekelezwa kwa kutumia Python na maktaba ya Pandas. Seti hii ya takwimu ina hesabu ya maneno ya kawaida yanayopatikana kwenye barua pepe, vyanzo vya barua pepe hizi ni vya siri. Tumia [notebook](notebook.ipynb) katika jalada hili kufuatilia.

## Uchambuzi wa Takwimu wa Kichunguzi

Hatua ya kukusanya katika mzunguko ni pale takwimu zinapopatikana pamoja na matatizo na maswali yanayohusika, lakini tunajuaje kama takwimu zinaweza kusaidia kufanikisha matokeo ya mwisho? 
Kumbuka kuwa mtaalamu wa takwimu anaweza kuuliza maswali yafuatayo wanapopata takwimu:
- Je, nina takwimu za kutosha kutatua tatizo hili?
- Je, takwimu ni za ubora unaokubalika kwa tatizo hili?
- Ikiwa nitagundua taarifa za ziada kupitia takwimu hizi, je, tunapaswa kuzingatia kubadilisha au kufafanua malengo?
Uchambuzi wa Takwimu wa Kichunguzi ni mchakato wa kufahamu takwimu hizo na unaweza kutumika kujibu maswali haya, pamoja na kutambua changamoto za kufanya kazi na seti ya takwimu. Hebu tuzingatie baadhi ya mbinu zinazotumika kufanikisha hili.

## Uwasilishaji wa Takwimu, Takwimu za Maelezo, na Pandas
Tunathibitishaje kama tuna takwimu za kutosha kutatua tatizo hili? Uwasilishaji wa takwimu unaweza kufupisha na kukusanya taarifa za jumla kuhusu seti yetu ya takwimu kupitia mbinu za takwimu za maelezo. Uwasilishaji wa takwimu hutusaidia kuelewa kile kilichopo, na takwimu za maelezo hutusaidia kuelewa ni vitu vingapi vilivyopo.

Katika baadhi ya masomo ya awali, tumetumia Pandas kutoa takwimu za maelezo kwa kutumia [`describe()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Inatoa hesabu, thamani za juu na za chini, wastani, upotofu wa kawaida na viwango vya asilimia kwenye takwimu za namba. Kutumia takwimu za maelezo kama `describe()` function kunaweza kukusaidia kutathmini kiasi cha takwimu ulizonazo na kama unahitaji zaidi.

## Sampuli na Uulizaji
Kuchunguza kila kitu katika seti kubwa ya takwimu kunaweza kuchukua muda mwingi na ni kazi ambayo mara nyingi huachwa kwa kompyuta kufanya. Hata hivyo, sampuli ni zana muhimu katika kuelewa takwimu na inatuwezesha kuwa na ufahamu bora wa kile kilichopo kwenye seti ya takwimu na kile inachowakilisha. Kwa kutumia sampuli, unaweza kutumia uwezekano na takwimu kufikia hitimisho la jumla kuhusu takwimu zako. Ingawa hakuna sheria iliyofafanuliwa kuhusu kiasi cha takwimu unachopaswa kuchukua sampuli, ni muhimu kutambua kuwa kadri unavyotoa sampuli zaidi, ndivyo unavyoweza kufanya uelewa wa jumla wa takwimu kwa usahihi zaidi.
Pandas ina [`sample()` function katika maktaba yake](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) ambapo unaweza kupitisha hoja ya idadi ya sampuli za nasibu unazotaka kupokea na kutumia.

Uulizaji wa jumla wa takwimu unaweza kukusaidia kujibu maswali na nadharia za jumla ulizonazo. Tofauti na sampuli, uulizaji unakuruhusu kuwa na udhibiti na kuzingatia sehemu maalum za takwimu ambazo una maswali kuhusu. 
[`query()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) katika maktaba ya Pandas inakuruhusu kuchagua safu na kupokea majibu rahisi kuhusu takwimu kupitia safu zilizopatikana.

## Kuchunguza kwa Kutumia Taswira
Huna haja ya kusubiri hadi takwimu zimesafishwa kabisa na kuchambuliwa ili kuanza kuunda taswira. Kwa kweli, kuwa na uwakilishi wa kuona wakati wa kuchunguza kunaweza kusaidia kutambua mifumo, uhusiano, na matatizo katika takwimu. Zaidi ya hayo, taswira hutoa njia ya mawasiliano na wale ambao hawahusiki moja kwa moja na usimamizi wa takwimu na inaweza kuwa fursa ya kushiriki na kufafanua maswali ya ziada ambayo hayakushughulikiwa katika hatua ya kukusanya. Rejelea [sehemu ya Taswira](../../../../../../../../../3-Data-Visualization) kujifunza zaidi kuhusu njia maarufu za kuchunguza kwa kuona.

## Kuchunguza ili Kutambua Kutokuwepo kwa Muafaka
Mada zote katika somo hili zinaweza kusaidia kutambua thamani zilizokosekana au zisizo thabiti, lakini Pandas inatoa kazi za kuangalia baadhi ya hizi. [isna() au isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) zinaweza kuangalia thamani zilizokosekana. Kipengele muhimu cha kuchunguza thamani hizi ndani ya takwimu zako ni kuchunguza kwa nini zilifikia hali hiyo mwanzoni. Hii inaweza kukusaidia kuamua ni [hatua gani za kuchukua ili kuzitatua](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Maswali ya Awali ya Somo](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/27)

## Kazi

[Kuchunguza Majibu](assignment.md)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya tafsiri ya kibinadamu ya kitaalamu. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.