<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2baeafe1db4d58ee5b8ec85db9de728a",
  "translation_date": "2025-09-05T17:09:32+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "sw"
}
-->
# Mzunguko wa Sayansi ya Takwimu: Kuchambua

|![ Sketchnote na [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Mzunguko wa Sayansi ya Takwimu: Kuchambua - _Sketchnote na [@nitya](https://twitter.com/nitya)_ |

## Maswali ya Kabla ya Somo

## [Maswali ya Kabla ya Somo](https://ff-quizzes.netlify.app/en/ds/quiz/28)

Kuchambua katika mzunguko wa takwimu kunathibitisha kuwa data inaweza kujibu maswali yaliyopendekezwa au kutatua tatizo fulani. Hatua hii pia inaweza kuzingatia kuthibitisha kuwa modeli inashughulikia maswali na matatizo haya kwa usahihi. Somo hili linazingatia Uchambuzi wa Takwimu wa Kichunguzi au EDA, ambao ni mbinu za kufafanua vipengele na uhusiano ndani ya data na zinaweza kutumika kuandaa data kwa ajili ya modeli.

Tutatumia seti ya data ya mfano kutoka [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) kuonyesha jinsi hii inaweza kutekelezwa kwa kutumia Python na maktaba ya Pandas. Seti hii ya data ina hesabu ya maneno ya kawaida yanayopatikana kwenye barua pepe, vyanzo vya barua pepe hizi ni vya siri. Tumia [notebook](../../../../4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) katika jalada hili kufuatilia.

## Uchambuzi wa Takwimu wa Kichunguzi

Hatua ya kukusanya katika mzunguko ni pale data inapopatikana pamoja na matatizo na maswali yanayohusika, lakini tunajuaje kama data inaweza kusaidia kufanikisha matokeo ya mwisho? 
Kumbuka kuwa mwanasayansi wa takwimu anaweza kuuliza maswali yafuatayo anapopata data:
- Je, nina data ya kutosha kutatua tatizo hili?
- Je, data ina ubora unaokubalika kwa tatizo hili?
- Ikiwa nitagundua taarifa za ziada kupitia data hii, je, tunapaswa kuzingatia kubadilisha au kufafanua malengo?
Uchambuzi wa Takwimu wa Kichunguzi ni mchakato wa kufahamu data hiyo na unaweza kutumika kujibu maswali haya, pamoja na kutambua changamoto za kufanya kazi na seti ya data. Hebu tuzingatie baadhi ya mbinu zinazotumika kufanikisha hili.

## Uwasifu wa Data, Takwimu za Maelezo, na Pandas
Tunathibitishaje kama tuna data ya kutosha kutatua tatizo hili? Uwasifu wa data unaweza kufupisha na kukusanya taarifa za jumla kuhusu seti yetu ya data kupitia mbinu za takwimu za maelezo. Uwasifu wa data hutusaidia kuelewa kile kilichopo kwetu, na takwimu za maelezo hutusaidia kuelewa ni vitu vingapi vilivyopo kwetu.

Katika baadhi ya masomo ya awali, tumetumia Pandas kutoa takwimu za maelezo kwa kutumia [`describe()` function]( https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Inatoa hesabu, thamani za juu na za chini, wastani, upotofu wa kawaida na viwango vya asilimia kwenye data ya nambari. Kutumia takwimu za maelezo kama `describe()` function kunaweza kukusaidia kutathmini kiasi cha data ulichonacho na kama unahitaji zaidi.

## Sampuli na Uulizaji
Kuchunguza kila kitu katika seti kubwa ya data kunaweza kuchukua muda mwingi na ni kazi ambayo mara nyingi huachwa kwa kompyuta kufanya. Hata hivyo, sampuli ni zana muhimu katika kuelewa data na inatuwezesha kuwa na ufahamu bora wa kile kilichopo kwenye seti ya data na kile inachowakilisha. Kwa kutumia sampuli, unaweza kutumia uwezekano na takwimu kufikia hitimisho la jumla kuhusu data yako. Ingawa hakuna sheria iliyofafanuliwa kuhusu kiasi cha data unachopaswa kuchukua sampuli, ni muhimu kutambua kuwa kadri unavyotoa sampuli zaidi, ndivyo unavyoweza kufanya ujumla sahihi zaidi kuhusu data.

Pandas ina [`sample()` function katika maktaba yake](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) ambapo unaweza kupitisha hoja ya idadi ya sampuli za nasibu unazotaka kupokea na kutumia.

Uulizaji wa jumla wa data unaweza kukusaidia kujibu maswali na nadharia za jumla unazoweza kuwa nazo. Tofauti na sampuli, uulizaji unakuruhusu kuwa na udhibiti na kuzingatia sehemu maalum za data unazouliza maswali kuhusu. 
[`query()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) katika maktaba ya Pandas inakuruhusu kuchagua safu na kupokea majibu rahisi kuhusu data kupitia safu zilizopatikana.

## Kuchunguza kwa Kutumia Taswira
Huna haja ya kusubiri hadi data isafishwe kabisa na kuchambuliwa ili kuanza kuunda taswira. Kwa kweli, kuwa na uwakilishi wa taswira wakati wa kuchunguza kunaweza kusaidia kutambua mifumo, uhusiano, na matatizo katika data. Zaidi ya hayo, taswira hutoa njia ya mawasiliano na wale ambao hawahusiki moja kwa moja na usimamizi wa data na inaweza kuwa fursa ya kushiriki na kufafanua maswali ya ziada ambayo hayakushughulikiwa katika hatua ya kukusanya. Rejelea [sehemu ya Taswira](../../../../../../../../../3-Data-Visualization) kujifunza zaidi kuhusu njia maarufu za kuchunguza kwa taswira.

## Kuchunguza ili Kutambua Kutokuwepo kwa Muafaka
Mada zote katika somo hili zinaweza kusaidia kutambua thamani zilizokosekana au zisizo thabiti, lakini Pandas inatoa kazi za kuangalia baadhi ya hizi. [isna() au isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) zinaweza kuangalia thamani zilizokosekana. Kipengele muhimu cha kuchunguza thamani hizi ndani ya data yako ni kuchunguza kwa nini zilifikia hali hiyo hapo awali. Hii inaweza kukusaidia kuamua ni [hatua gani za kuchukua ili kuzitatua](../../../../../../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Maswali ya Baada ya Somo](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Kazi

[Kuchunguza kwa Majibu](assignment.md)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.