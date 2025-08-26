<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "356d12cffc3125db133a2d27b827a745",
  "translation_date": "2025-08-26T15:27:22+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "sw"
}
-->
# Kufafanua Data

|![ Sketchnote na [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Kufafanua Data - _Sketchnote na [@nitya](https://twitter.com/nitya)_ |

Data ni ukweli, taarifa, uchunguzi na vipimo vinavyotumika kufanya ugunduzi na kusaidia maamuzi yenye ufahamu. Kipengele cha data ni kitengo kimoja cha data ndani ya seti ya data, ambayo ni mkusanyiko wa vipengele vya data. Seti za data zinaweza kuwa katika miundo na fomati tofauti, na mara nyingi zitategemea chanzo chake, au mahali data ilipotoka. Kwa mfano, mapato ya kila mwezi ya kampuni yanaweza kuwa kwenye lahajedwali lakini data ya kiwango cha moyo kwa saa kutoka kwa saa ya mkononi inaweza kuwa katika fomati ya [JSON](https://stackoverflow.com/a/383699). Ni kawaida kwa wanasayansi wa data kufanya kazi na aina tofauti za data ndani ya seti ya data.

Somo hili linazingatia kutambua na kuainisha data kulingana na sifa zake na vyanzo vyake.

## [Maswali ya Awali ya Somo](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)
## Jinsi Data Inavyoelezwa

### Data Ghafi
Data ghafi ni data ambayo imetoka kwenye chanzo chake katika hali yake ya awali na haijachambuliwa au kupangwa. Ili kuelewa kinachotokea na seti ya data, inahitaji kupangwa katika fomati inayoweza kueleweka na binadamu pamoja na teknolojia wanayoweza kutumia kuichambua zaidi. Muundo wa seti ya data unaelezea jinsi ilivyopangwa na inaweza kuainishwa kama iliyopangwa, isiyo na mpangilio, na nusu iliyopangwa. Aina hizi za muundo zitabadilika, kulingana na chanzo lakini hatimaye zitaingia katika mojawapo ya makundi haya matatu.

### Data ya Kiasi
Data ya kiasi ni uchunguzi wa nambari ndani ya seti ya data na mara nyingi inaweza kuchambuliwa, kupimwa, na kutumika kihisabati. Baadhi ya mifano ya data ya kiasi ni: idadi ya watu wa nchi, urefu wa mtu, au mapato ya kila robo ya kampuni. Kwa uchambuzi wa ziada, data ya kiasi inaweza kutumika kugundua mwenendo wa msimu wa Kielezo cha Ubora wa Hewa (AQI) au kukadiria uwezekano wa msongamano wa magari wakati wa saa za kazi za kawaida.

### Data ya Ubora
Data ya ubora, inayojulikana pia kama data ya kategoria, ni data ambayo haiwezi kupimwa kwa njia ya malengo kama uchunguzi wa data ya kiasi. Kwa ujumla ni fomati mbalimbali za data ya maoni inayorekodi ubora wa kitu, kama bidhaa au mchakato. Wakati mwingine, data ya ubora ni ya nambari lakini haitatumika kihisabati, kama namba za simu au mihuri ya muda. Baadhi ya mifano ya data ya ubora ni: maoni ya video, chapa na modeli ya gari, au rangi unayopenda ya rafiki yako wa karibu. Data ya ubora inaweza kutumika kuelewa ni bidhaa zipi wateja wanapenda zaidi au kutambua maneno maarufu katika wasifu wa maombi ya kazi.

### Data Iliyopangwa
Data iliyopangwa ni data ambayo imepangwa katika safu na nguzo, ambapo kila safu itakuwa na seti sawa ya nguzo. Nguzo zinawakilisha thamani ya aina fulani na zitatambuliwa kwa jina linaloelezea kile thamani inawakilisha, wakati safu zina thamani halisi. Nguzo mara nyingi zitakuwa na seti maalum ya sheria au vizuizi juu ya thamani, ili kuhakikisha kuwa thamani zinawakilisha nguzo kwa usahihi. Kwa mfano, fikiria lahajedwali la wateja ambapo kila safu lazima iwe na namba ya simu na namba za simu hazina herufi za alfabeti. Kunaweza kuwa na sheria zinazotumika kwenye nguzo ya namba ya simu ili kuhakikisha kuwa haijawahi kuwa tupu na ina namba pekee.

Faida ya data iliyopangwa ni kwamba inaweza kupangwa kwa njia ambayo inaweza kuhusishwa na data nyingine iliyopangwa. Hata hivyo, kwa sababu data imeundwa kupangwa kwa njia maalum, kufanya mabadiliko kwenye muundo wake wa jumla kunaweza kuchukua juhudi nyingi. Kwa mfano, kuongeza nguzo ya barua pepe kwenye lahajedwali la wateja ambayo haiwezi kuwa tupu inamaanisha utahitaji kujua jinsi ya kuongeza thamani hizi kwenye safu zilizopo za wateja katika seti ya data.

Mifano ya data iliyopangwa: lahajedwali, hifadhidata za uhusiano, namba za simu, taarifa za benki.

### Data Isiyo na Mpangilio
Data isiyo na mpangilio kwa kawaida haiwezi kuainishwa katika safu au nguzo na haina fomati au seti ya sheria za kufuata. Kwa sababu data isiyo na mpangilio ina vizuizi vichache juu ya muundo wake, ni rahisi kuongeza taarifa mpya ikilinganishwa na seti ya data iliyopangwa. Ikiwa sensor inayorekodi data ya shinikizo la anga kila dakika 2 imepokea sasisho linaloruhusu kupima na kurekodi joto, haitahitaji kubadilisha data iliyopo ikiwa ni isiyo na mpangilio. Hata hivyo, hii inaweza kufanya uchambuzi au uchunguzi wa aina hii ya data kuchukua muda mrefu. Kwa mfano, mwanasayansi anayetaka kupata wastani wa joto la mwezi uliopita kutoka kwa data ya sensor, lakini anakuta kuwa sensor ilirekodi "e" katika baadhi ya data yake ili kuonyesha kuwa ilikuwa imeharibika badala ya nambari ya kawaida, ambayo inamaanisha data haijakamilika.

Mifano ya data isiyo na mpangilio: faili za maandishi, ujumbe wa maandishi, faili za video.

### Data Nusu Iliyopangwa
Data nusu iliyopangwa ina sifa zinazofanya iwe mchanganyiko wa data iliyopangwa na isiyo na mpangilio. Kwa kawaida haifuati fomati ya safu na nguzo lakini imepangwa kwa njia inayochukuliwa kuwa imepangwa na inaweza kufuata fomati maalum au seti ya sheria. Muundo utatofautiana kati ya vyanzo, kama vile uongozi uliofafanuliwa vizuri hadi kitu kilicho rahisi zaidi kinachoruhusu ujumuishaji rahisi wa taarifa mpya. Metadata ni viashiria vinavyosaidia kuamua jinsi data imepangwa na kuhifadhiwa na itakuwa na majina mbalimbali, kulingana na aina ya data. Baadhi ya majina ya kawaida ya metadata ni lebo, vipengele, vyombo, na sifa. Kwa mfano, ujumbe wa barua pepe wa kawaida utakuwa na mada, mwili, na seti ya wapokeaji na unaweza kupangwa kulingana na nani au lini ulitumwa.

Mifano ya data nusu iliyopangwa: HTML, faili za CSV, JavaScript Object Notation (JSON).

## Vyanzo vya Data

Chanzo cha data ni eneo la awali ambapo data ilizalishwa, au mahali inapokaa, na itatofautiana kulingana na jinsi na wakati ilikusanywa. Data inayozalishwa na mtumiaji wake inajulikana kama data ya msingi, wakati data ya sekondari inatoka kwa chanzo ambacho kimekusanya data kwa matumizi ya jumla. Kwa mfano, kundi la wanasayansi wanaokusanya uchunguzi katika msitu wa mvua litachukuliwa kuwa data ya msingi, na ikiwa wataamua kushiriki na wanasayansi wengine itachukuliwa kuwa data ya sekondari kwa wale wanaoitumia.

Hifadhidata ni chanzo cha kawaida na hutegemea mfumo wa usimamizi wa hifadhidata kuhifadhi na kudumisha data ambapo watumiaji hutumia amri zinazoitwa maswali kuchunguza data. Faili kama vyanzo vya data vinaweza kuwa faili za sauti, picha, na video pamoja na lahajedwali kama Excel. Vyanzo vya mtandao ni eneo la kawaida la kuhifadhi data, ambapo hifadhidata pamoja na faili zinaweza kupatikana. Programu za kiolesura cha programu, zinazojulikana pia kama APIs, huruhusu waandaaji programu kuunda njia za kushiriki data na watumiaji wa nje kupitia mtandao, wakati mchakato wa kuchota data kutoka kwa ukurasa wa wavuti unajulikana kama web scraping. [Masomo katika Kufanya Kazi na Data](../../../../../../../../../2-Working-With-Data) yanazingatia jinsi ya kutumia vyanzo mbalimbali vya data.

## Hitimisho

Katika somo hili tumejifunza:

- Data ni nini
- Jinsi data inavyoelezwa
- Jinsi data inavyoainishwa na kuorodheshwa
- Mahali data inaweza kupatikana

## 🚀 Changamoto

Kaggle ni chanzo bora cha seti za data za wazi. Tumia [zana ya kutafuta seti za data](https://www.kaggle.com/datasets) kupata seti za data za kuvutia na uainishe seti 3-5 za data kwa vigezo hivi:

- Je, data ni ya kiasi au ya ubora?
- Je, data ni iliyopangwa, isiyo na mpangilio, au nusu iliyopangwa?

## [Maswali ya Baada ya Somo](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/5)

## Mapitio na Kujisomea

- Kitengo hiki cha Microsoft Learn, kinachoitwa [Ainisheni Data Yako](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data) kina maelezo ya kina kuhusu data iliyopangwa, nusu iliyopangwa, na isiyo na mpangilio.

## Kazi

[Ainisheni Seti za Data](assignment.md)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa maelewano mabaya au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.