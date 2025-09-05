<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cfb068050337a36e348debaa502a24fa",
  "translation_date": "2025-09-05T17:13:37+00:00",
  "source_file": "3-Data-Visualization/13-meaningful-visualizations/README.md",
  "language_code": "sw"
}
-->
# Kutengeneza Uwasilishaji wa Takwimu wa Maana

|![ Sketchnote na [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Uwasilishaji wa Takwimu wa Maana - _Sketchnote na [@nitya](https://twitter.com/nitya)_ |

> "Ukitesa takwimu vya kutosha, zitakiri chochote" -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

Moja ya ujuzi wa msingi wa mwanasayansi wa takwimu ni uwezo wa kuunda uwasilishaji wa takwimu wa maana ambao husaidia kujibu maswali unayoweza kuwa nayo. Kabla ya kuwasilisha takwimu zako, unahitaji kuhakikisha kuwa zimefanyiwa usafi na maandalizi, kama ulivyofanya katika masomo ya awali. Baada ya hapo, unaweza kuanza kuamua jinsi bora ya kuwasilisha takwimu hizo.

Katika somo hili, utapitia:

1. Jinsi ya kuchagua aina sahihi ya chati
2. Jinsi ya kuepuka chati za udanganyifu
3. Jinsi ya kutumia rangi
4. Jinsi ya kuunda chati zako ili ziwe rahisi kusomeka
5. Jinsi ya kuunda suluhisho za chati za kuhamasisha au za 3D
6. Jinsi ya kuunda uwasilishaji wa ubunifu

## [Maswali ya Kabla ya Somo](https://ff-quizzes.netlify.app/en/ds/quiz/24)

## Chagua aina sahihi ya chati

Katika masomo ya awali, ulijaribu kuunda aina mbalimbali za uwasilishaji wa takwimu kwa kutumia Matplotlib na Seaborn. Kwa ujumla, unaweza kuchagua [aina sahihi ya chati](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) kwa swali unalouliza kwa kutumia jedwali hili:

| Unahitaji:                 | Unapaswa kutumia:               |
| -------------------------- | ------------------------------- |
| Kuonyesha mwenendo wa takwimu kwa muda | Line                            |
| Kulinganisha makundi       | Bar, Pie                        |
| Kulinganisha jumla         | Pie, Stacked Bar                |
| Kuonyesha uhusiano         | Scatter, Line, Facet, Dual Line |
| Kuonyesha usambazaji       | Scatter, Histogram, Box         |
| Kuonyesha uwiano           | Pie, Donut, Waffle              |

> ✅ Kulingana na muundo wa takwimu zako, unaweza kuhitaji kuzibadilisha kutoka maandishi hadi nambari ili kupata chati inayounga mkono.

## Epuka udanganyifu

Hata kama mwanasayansi wa takwimu anachagua chati sahihi kwa takwimu sahihi, kuna njia nyingi ambazo takwimu zinaweza kuwasilishwa ili kuthibitisha hoja, mara nyingi kwa gharama ya kudhoofisha takwimu zenyewe. Kuna mifano mingi ya chati na infografia za udanganyifu!

[![Jinsi Chati Zinavyodanganya na Alberto Cairo](../../../../3-Data-Visualization/13-meaningful-visualizations/images/tornado.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "Jinsi chati zinavyodanganya")

> 🎥 Bonyeza picha hapo juu kwa mazungumzo ya mkutano kuhusu chati za udanganyifu

Chati hii inageuza mhimili wa X ili kuonyesha kinyume cha ukweli, kulingana na tarehe:

![chati mbaya 1](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-1.png)

[Chati hii](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) ni ya udanganyifu zaidi, kwani jicho linavutwa upande wa kulia kuhitimisha kuwa, kwa muda, kesi za COVID zimepungua katika kaunti mbalimbali. Kwa kweli, ukitazama kwa makini tarehe, utagundua kuwa zimepangwa upya ili kuonyesha mwenendo wa kupungua kwa udanganyifu.

![chati mbaya 2](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-2.jpg)

Mfano huu maarufu unatumia rangi NA mhimili wa Y uliogeuzwa kudanganya: badala ya kuhitimisha kuwa vifo vya bunduki viliongezeka baada ya kupitishwa kwa sheria zinazopendelea bunduki, kwa kweli jicho linadanganywa kufikiria kinyume chake:

![chati mbaya 3](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-3.jpg)

Chati hii ya ajabu inaonyesha jinsi uwiano unavyoweza kudanganywa, kwa athari za kuchekesha:

![chati mbaya 4](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-4.jpg)

Kulinganisha vitu visivyolinganishwa ni mbinu nyingine ya hila. Kuna [tovuti nzuri](https://tylervigen.com/spurious-correlations) kuhusu 'uhusiano wa uwongo' inayoonyesha 'mambo' yanayohusisha vitu kama kiwango cha talaka huko Maine na matumizi ya siagi ya margarine. Kikundi cha Reddit pia hukusanya [matumizi mabaya](https://www.reddit.com/r/dataisugly/top/?t=all) ya takwimu.

Ni muhimu kuelewa jinsi jicho linaweza kudanganywa kwa urahisi na chati za udanganyifu. Hata kama nia ya mwanasayansi wa takwimu ni nzuri, chaguo la aina mbaya ya chati, kama chati ya pie inayoonyesha makundi mengi sana, linaweza kuwa la udanganyifu.

## Rangi

Umeona katika chati ya 'vurugu za bunduki Florida' hapo juu jinsi rangi inaweza kutoa maana ya ziada kwa chati, hasa zile ambazo hazijatengenezwa kwa kutumia maktaba kama Matplotlib na Seaborn ambazo zinakuja na maktaba mbalimbali za rangi zilizothibitishwa. Ikiwa unaunda chati kwa mkono, fanya utafiti kidogo kuhusu [nadharia ya rangi](https://colormatters.com/color-and-design/basic-color-theory)

> ✅ Kuwa makini, unapounda chati, kwamba upatikanaji ni kipengele muhimu cha uwasilishaji. Baadhi ya watumiaji wako wanaweza kuwa na upofu wa rangi - je, chati yako inaonekana vizuri kwa watumiaji wenye ulemavu wa kuona?

Kuwa mwangalifu unapochagua rangi kwa chati yako, kwani rangi inaweza kuonyesha maana ambayo huenda hukusudia. 'Wanawake wa pinki' katika chati ya 'urefu' hapo juu wanaonyesha maana ya 'kike' ambayo inaongeza uzito wa ajabu wa chati yenyewe.

Ingawa [maana ya rangi](https://colormatters.com/color-symbolism/the-meanings-of-colors) inaweza kuwa tofauti katika sehemu mbalimbali za dunia, na huwa zinabadilika kulingana na kivuli chake. Kwa ujumla, maana za rangi ni pamoja na:

| Rangi  | Maana               |
| ------ | ------------------- |
| nyekundu | nguvu               |
| bluu   | uaminifu, uaminifu  |
| njano  | furaha, tahadhari   |
| kijani | ekolojia, bahati, wivu |
| zambarau | furaha              |
| chungwa | nguvu               |

Ikiwa umepewa jukumu la kuunda chati yenye rangi maalum, hakikisha kuwa chati zako zinapatikana na rangi unayochagua inalingana na maana unayojaribu kuonyesha.

## Kuunda chati zako ili ziwe rahisi kusomeka

Chati hazina maana ikiwa hazisomeki! Chukua muda kuzingatia kuunda upana na urefu wa chati yako ili iweze kuendana vizuri na takwimu zako. Ikiwa kipengele kimoja (kama majimbo yote 50) kinahitaji kuonyeshwa, yaonyeshe wima kwenye mhimili wa Y ikiwa inawezekana ili kuepuka chati inayosogezwa kwa usawa.

Weka lebo kwenye mihimili yako, toa ufafanuzi ikiwa ni lazima, na toa vidokezo vya kuelewa takwimu vizuri.

Ikiwa takwimu zako ni za maandishi na zina maneno mengi kwenye mhimili wa X, unaweza kugeuza maandishi kwa pembe ili yasomeke vizuri. [Matplotlib](https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html) inatoa uwezekano wa kuchora kwa 3D, ikiwa takwimu zako zinaunga mkono. Uwasilishaji wa takwimu wa kisasa unaweza kuzalishwa kwa kutumia `mpl_toolkits.mplot3d`.

![chati za 3D](../../../../3-Data-Visualization/13-meaningful-visualizations/images/3d.png)

## Uhuishaji na maonyesho ya chati za 3D

Baadhi ya uwasilishaji bora wa takwimu leo ni wa kuhamasisha. Shirley Wu ana mifano ya kushangaza iliyofanywa na D3, kama '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', ambapo kila ua ni uwasilishaji wa filamu. Mfano mwingine kwa Guardian ni 'bussed out', uzoefu wa maingiliano unaochanganya uwasilishaji na Greensock na D3 pamoja na makala ya scrollytelling ili kuonyesha jinsi NYC inavyoshughulikia tatizo la watu wasio na makazi kwa kuwapeleka nje ya jiji.

![busing](../../../../3-Data-Visualization/13-meaningful-visualizations/images/busing.png)

> "Bussed Out: Jinsi Amerika Inavyohamisha Watu Wasio na Makazi" kutoka [Guardian](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Uwasilishaji na Nadieh Bremer & Shirley Wu

Ingawa somo hili halitoshi kuingia kwa kina kufundisha maktaba hizi zenye nguvu za uwasilishaji, jaribu kutumia D3 katika programu ya Vue.js kwa kutumia maktaba kuonyesha uwasilishaji wa kitabu "Dangerous Liaisons" kama mtandao wa kijamii wa kuhamasisha.

> "Les Liaisons Dangereuses" ni riwaya ya barua, au riwaya iliyowasilishwa kama mfululizo wa barua. Iliandikwa mwaka 1782 na Choderlos de Laclos, inasimulia hadithi ya maneva ya kijamii ya kikatili na isiyo na maadili ya wahusika wawili wa kike wa aristokrasia ya Ufaransa mwishoni mwa karne ya 18, Vicomte de Valmont na Marquise de Merteuil. Wote wanakutana na mwisho wao lakini si bila kusababisha uharibifu mkubwa wa kijamii. Riwaya inafunguka kama mfululizo wa barua zilizoandikwa kwa watu mbalimbali katika duru zao, wakipanga kulipiza kisasi au tu kuleta matatizo. Unda uwasilishaji wa barua hizi ili kugundua wahusika wakuu wa hadithi, kwa njia ya kuona.

Utakamilisha programu ya wavuti ambayo itaonyesha mtazamo wa kuhamasisha wa mtandao huu wa kijamii. Inatumia maktaba iliyojengwa kuunda [mtazamo wa mtandao](https://github.com/emiliorizzo/vue-d3-network) kwa kutumia Vue.js na D3. Wakati programu inafanya kazi, unaweza kuvuta nodi kwenye skrini ili kupanga upya takwimu.

![liaisons](../../../../3-Data-Visualization/13-meaningful-visualizations/images/liaisons.png)

## Mradi: Unda chati ya kuonyesha mtandao kwa kutumia D3.js

> Folda ya somo hili inajumuisha folda ya `solution` ambapo unaweza kupata mradi uliokamilika, kwa marejeleo yako.

1. Fuata maelekezo katika faili la README.md kwenye mzizi wa folda ya mwanzo. Hakikisha una NPM na Node.js inayoendesha kwenye mashine yako kabla ya kusakinisha utegemezi wa mradi wako.

2. Fungua folda ya `starter/src`. Utakuta folda ya `assets` ambapo unaweza kupata faili ya .json yenye barua zote kutoka kwa riwaya, zikiwa na namba, na maelezo ya 'to' na 'from'.

3. Kamilisha msimbo katika `components/Nodes.vue` ili kuwezesha uwasilishaji. Tafuta njia inayoitwa `createLinks()` na ongeza kitanzi kilichopachikwa hapa chini.

Pitia kitu cha .json ili kukamata data ya 'to' na 'from' kwa barua na kujenga kitu cha `links` ili maktaba ya uwasilishaji iweze kuitumia:

```javascript
//loop through letters
      let f = 0;
      let t = 0;
      for (var i = 0; i < letters.length; i++) {
          for (var j = 0; j < characters.length; j++) {
              
            if (characters[j] == letters[i].from) {
              f = j;
            }
            if (characters[j] == letters[i].to) {
              t = j;
            }
        }
        this.links.push({ sid: f, tid: t });
      }
  ```

Endesha programu yako kutoka kwa terminal (npm run serve) na furahia uwasilishaji!

## 🚀 Changamoto

Tembelea mtandao ili kugundua uwasilishaji wa takwimu wa udanganyifu. Je, mwandishi anamdanganya mtumiaji, na je, ni kwa makusudi? Jaribu kurekebisha uwasilishaji ili kuonyesha jinsi unavyopaswa kuonekana.

## [Maswali ya Baada ya Somo](https://ff-quizzes.netlify.app/en/ds/quiz/25)

## Mapitio na Kujisomea

Hapa kuna makala za kusoma kuhusu uwasilishaji wa takwimu wa udanganyifu:

https://gizmodo.com/how-to-lie-with-data-visualization-1563576606

http://ixd.prattsi.org/2017/12/visual-lies-usability-in-deceptive-data-visualizations/

Tazama uwasilishaji huu wa kuvutia wa mali za kihistoria na vitu vya kale:

https://handbook.pubpub.org/

Pitia makala hii kuhusu jinsi uhuishaji unavyoweza kuboresha uwasilishaji wako:

https://medium.com/@EvanSinar/use-animation-to-supercharge-data-visualization-cd905a882ad4

## Kazi

[Unda uwasilishaji wako wa kipekee](assignment.md)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.