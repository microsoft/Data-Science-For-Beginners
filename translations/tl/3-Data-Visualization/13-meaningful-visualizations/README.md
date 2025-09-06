<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cfb068050337a36e348debaa502a24fa",
  "translation_date": "2025-09-06T00:26:07+00:00",
  "source_file": "3-Data-Visualization/13-meaningful-visualizations/README.md",
  "language_code": "tl"
}
-->
# Paggawa ng Makabuluhang Visualisasyon

|![ Sketchnote ni [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Makabuluhang Visualisasyon - _Sketchnote ni [@nitya](https://twitter.com/nitya)_ |

> "Kung pahihirapan mo ang datos nang matagal, aamin ito ng kahit ano" -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

Isa sa mga pangunahing kasanayan ng isang data scientist ay ang kakayahang lumikha ng makabuluhang visualisasyon ng datos na tumutulong sagutin ang mga tanong na maaaring mayroon ka. Bago mag-visualize ng iyong datos, kailangan mong tiyakin na ito ay nalinis at naihanda, tulad ng ginawa mo sa mga nakaraang aralin. Pagkatapos nito, maaari ka nang magsimulang magdesisyon kung paano pinakamahusay na ipakita ang datos.

Sa araling ito, iyong susuriin:

1. Paano pumili ng tamang uri ng tsart
2. Paano iwasan ang mapanlinlang na tsart
3. Paano gumamit ng kulay
4. Paano i-style ang iyong mga tsart para sa mas madaling mabasa
5. Paano gumawa ng animated o 3D na solusyon sa tsart
6. Paano gumawa ng malikhaing visualisasyon

## [Pre-Lecture Quiz](https://ff-quizzes.netlify.app/en/ds/quiz/24)

## Pumili ng tamang uri ng tsart

Sa mga nakaraang aralin, sinubukan mong gumawa ng iba't ibang uri ng visualisasyon ng datos gamit ang Matplotlib at Seaborn para sa pag-chart. Sa pangkalahatan, maaari mong piliin ang [tamang uri ng tsart](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) para sa tanong na iyong tinatanong gamit ang talahanayan na ito:

| Kailangan mong:            | Dapat mong gamitin:             |
| -------------------------- | ------------------------------- |
| Ipakita ang mga trend ng datos sa paglipas ng panahon | Line                            |
| Ihambing ang mga kategorya | Bar, Pie                        |
| Ihambing ang mga kabuuan   | Pie, Stacked Bar                |
| Ipakita ang mga relasyon   | Scatter, Line, Facet, Dual Line |
| Ipakita ang mga distribusyon | Scatter, Histogram, Box         |
| Ipakita ang mga proporsyon | Pie, Donut, Waffle              |

> ✅ Depende sa komposisyon ng iyong datos, maaaring kailanganin mong i-convert ito mula sa text patungong numeric upang suportahan ang isang partikular na tsart.

## Iwasan ang panlilinlang

Kahit na maingat ang isang data scientist sa pagpili ng tamang tsart para sa tamang datos, maraming paraan kung paano maipapakita ang datos upang patunayan ang isang punto, madalas sa kapinsalaan ng datos mismo. Maraming halimbawa ng mapanlinlang na tsart at infographics!

[![How Charts Lie ni Alberto Cairo](../../../../3-Data-Visualization/13-meaningful-visualizations/images/tornado.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "How charts lie")

> 🎥 I-click ang imahe sa itaas para sa isang talakayan tungkol sa mapanlinlang na tsart

Ang tsart na ito ay binabaliktad ang X axis upang ipakita ang kabaligtaran ng katotohanan, batay sa petsa:

![bad chart 1](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-1.png)

[Ang tsart na ito](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) ay mas mapanlinlang pa, dahil ang mata ay naaakit sa kanan upang isipin na, sa paglipas ng panahon, bumaba ang mga kaso ng COVID sa iba't ibang county. Sa katunayan, kung titingnan mo nang mabuti ang mga petsa, makikita mong inayos ang mga ito upang magmukhang pababa ang trend.

![bad chart 2](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-2.jpg)

Ang kilalang halimbawa na ito ay gumagamit ng kulay AT baliktad na Y axis upang manlinlang: sa halip na isipin na tumaas ang mga kaso ng pagkamatay dahil sa baril pagkatapos ng pagpasa ng batas na pabor sa baril, ang mata ay nalilinlang upang isipin ang kabaligtaran:

![bad chart 3](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-3.jpg)

Ang kakaibang tsart na ito ay nagpapakita kung paano maaaring manipulahin ang proporsyon, sa nakakatawang paraan:

![bad chart 4](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-4.jpg)

Ang paghahambing ng mga bagay na hindi maihahambing ay isa pang mapanlinlang na taktika. Mayroong [kahanga-hangang web site](https://tylervigen.com/spurious-correlations) tungkol sa 'spurious correlations' na nagpapakita ng 'mga katotohanan' na nag-uugnay sa mga bagay tulad ng rate ng diborsyo sa Maine at ang pagkonsumo ng margarina. Ang isang Reddit group ay nangongolekta rin ng [pangit na paggamit](https://www.reddit.com/r/dataisugly/top/?t=all) ng datos.

Mahalagang maunawaan kung gaano kadaling malinlang ang mata ng mapanlinlang na tsart. Kahit na mabuti ang intensyon ng data scientist, ang pagpili ng maling uri ng tsart, tulad ng pie chart na nagpapakita ng masyadong maraming kategorya, ay maaaring maging mapanlinlang.

## Kulay

Makikita mo sa 'Florida gun violence' chart sa itaas kung paano ang kulay ay maaaring magbigay ng karagdagang kahulugan sa mga tsart, lalo na ang mga hindi dinisenyo gamit ang mga library tulad ng Matplotlib at Seaborn na may iba't ibang na-vet na color libraries at palettes. Kung gumagawa ka ng tsart nang manu-mano, maglaan ng kaunting oras upang pag-aralan ang [teorya ng kulay](https://colormatters.com/color-and-design/basic-color-theory)

> ✅ Tandaan, kapag nagdidisenyo ng mga tsart, na ang accessibility ay mahalagang aspeto ng visualisasyon. Ang ilan sa iyong mga user ay maaaring color blind - maganda ba ang pagpapakita ng iyong tsart para sa mga user na may kapansanan sa paningin?

Mag-ingat sa pagpili ng mga kulay para sa iyong tsart, dahil ang kulay ay maaaring magbigay ng kahulugan na hindi mo sinasadya. Ang 'pink ladies' sa 'height' chart sa itaas ay nagbibigay ng isang malinaw na 'pambabae' na kahulugan na nagdaragdag sa kakaibang aspeto ng tsart mismo.

Habang [kahulugan ng kulay](https://colormatters.com/color-symbolism/the-meanings-of-colors) ay maaaring magkaiba sa iba't ibang bahagi ng mundo, at may tendensiyang magbago depende sa kanilang shade. Sa pangkalahatan, ang mga kahulugan ng kulay ay kinabibilangan ng:

| Kulay  | Kahulugan           |
| ------ | ------------------- |
| pula   | kapangyarihan       |
| asul   | tiwala, katapatan   |
| dilaw  | kasiyahan, babala   |
| berde  | ekolohiya, swerte, inggit |
| lila   | kasiyahan           |
| kahel  | sigla               |

Kung ikaw ay inatasang gumawa ng tsart na may custom na kulay, tiyakin na ang iyong mga tsart ay parehong accessible at ang kulay na iyong pinili ay tumutugma sa kahulugan na nais mong iparating.

## Pag-style ng iyong mga tsart para sa mas madaling mabasa

Ang mga tsart ay hindi makabuluhan kung hindi ito madaling mabasa! Maglaan ng sandali upang isaalang-alang ang pag-style ng lapad at taas ng iyong tsart upang mag-scale nang maayos sa iyong datos. Kung ang isang variable (tulad ng lahat ng 50 estado) ay kailangang ipakita, ipakita ang mga ito nang patayo sa Y axis kung maaari upang maiwasan ang tsart na kailangang i-scroll nang pahalang.

Lagyan ng label ang iyong mga axis, magbigay ng legend kung kinakailangan, at mag-alok ng tooltips para sa mas mahusay na pag-unawa sa datos.

Kung ang iyong datos ay tekstwal at mahaba sa X axis, maaari mong i-angle ang teksto para sa mas madaling mabasa. [Matplotlib](https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html) ay nag-aalok ng 3D plotting, kung ang iyong datos ay sumusuporta dito. Ang mga sopistikadong visualisasyon ng datos ay maaaring gawin gamit ang `mpl_toolkits.mplot3d`.

![3d plots](../../../../3-Data-Visualization/13-meaningful-visualizations/images/3d.png)

## Animation at 3D na pagpapakita ng tsart

Ang ilan sa mga pinakamahusay na visualisasyon ng datos ngayon ay animated. Si Shirley Wu ay may mga kamangha-manghang ginawa gamit ang D3, tulad ng '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', kung saan ang bawat bulaklak ay isang visualisasyon ng isang pelikula. Isa pang halimbawa para sa Guardian ay 'bussed out', isang interactive na karanasan na pinagsasama ang visualisasyon gamit ang Greensock at D3 kasama ang scrollytelling na format ng artikulo upang ipakita kung paano hinahandle ng NYC ang problema nito sa mga homeless sa pamamagitan ng pagbyahe sa mga tao palabas ng lungsod.

![busing](../../../../3-Data-Visualization/13-meaningful-visualizations/images/busing.png)

> "Bussed Out: Paano Inililipat ng Amerika ang mga Homeless" mula sa [the Guardian](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Visualisasyon ni Nadieh Bremer & Shirley Wu

Bagamat hindi sapat ang araling ito upang talakayin nang malalim ang mga makapangyarihang library ng visualisasyon, subukan ang iyong kakayahan sa D3 sa isang Vue.js app gamit ang isang library upang ipakita ang visualisasyon ng aklat na "Dangerous Liaisons" bilang isang animated na social network.

> "Les Liaisons Dangereuses" ay isang epistolaryong nobela, o isang nobela na ipinakita bilang serye ng mga liham. Isinulat noong 1782 ni Choderlos de Laclos, ito ay nagsasabi ng kuwento ng malupit, moral na bangkaroteng mga galaw ng dalawang nag-aaway na pangunahing tauhan ng French aristocracy noong huling bahagi ng ika-18 siglo, ang Vicomte de Valmont at ang Marquise de Merteuil. Pareho silang nagkaroon ng masamang wakas ngunit hindi bago magdulot ng malaking pinsala sa lipunan. Ang nobela ay nagbubukas bilang serye ng mga liham na isinulat sa iba't ibang tao sa kanilang mga bilog, nagbabalak ng paghihiganti o simpleng magdulot ng problema. Gumawa ng visualisasyon ng mga liham na ito upang matuklasan ang mga pangunahing tauhan ng kuwento, sa biswal na paraan.

Makukumpleto mo ang isang web app na magpapakita ng animated na view ng social network na ito. Gumagamit ito ng isang library na ginawa upang lumikha ng [visual ng isang network](https://github.com/emiliorizzo/vue-d3-network) gamit ang Vue.js at D3. Kapag tumatakbo na ang app, maaari mong hilahin ang mga nodes sa screen upang i-shuffle ang datos.

![liaisons](../../../../3-Data-Visualization/13-meaningful-visualizations/images/liaisons.png)

## Proyekto: Gumawa ng tsart upang ipakita ang isang network gamit ang D3.js

> Ang folder ng araling ito ay may kasamang `solution` folder kung saan maaari mong makita ang kumpletong proyekto, para sa iyong sanggunian.

1. Sundin ang mga tagubilin sa README.md file sa root ng starter folder. Tiyakin na mayroon kang NPM at Node.js na tumatakbo sa iyong makina bago i-install ang mga dependencies ng iyong proyekto.

2. Buksan ang `starter/src` folder. Makikita mo ang isang `assets` folder kung saan makakahanap ka ng .json file na naglalaman ng lahat ng mga liham mula sa nobela, na may bilang, at may 'to' at 'from' na anotasyon.

3. Kumpletuhin ang code sa `components/Nodes.vue` upang paganahin ang visualisasyon. Hanapin ang method na tinatawag na `createLinks()` at idagdag ang sumusunod na nested loop.

I-loop ang .json object upang makuha ang 'to' at 'from' na datos para sa mga liham at buuin ang `links` object upang magamit ito ng library ng visualisasyon:

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

Patakbuhin ang iyong app mula sa terminal (npm run serve) at tamasahin ang visualisasyon!

## 🚀 Hamon

Maglibot sa internet upang matuklasan ang mga mapanlinlang na visualisasyon. Paano nililinlang ng may-akda ang user, at ito ba ay sinadya? Subukang itama ang mga visualisasyon upang ipakita kung paano dapat ang hitsura nito.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/25)

## Review & Self Study

Narito ang ilang mga artikulo na maaaring basahin tungkol sa mapanlinlang na visualisasyon ng datos:

https://gizmodo.com/how-to-lie-with-data-visualization-1563576606

http://ixd.prattsi.org/2017/12/visual-lies-usability-in-deceptive-data-visualizations/

Tingnan ang mga interesanteng visualisasyon para sa mga makasaysayang assets at artifacts:

https://handbook.pubpub.org/

Basahin ang artikulong ito tungkol sa kung paano maaaring mapahusay ng animation ang iyong mga visualisasyon:

https://medium.com/@EvanSinar/use-animation-to-supercharge-data-visualization-cd905a882ad4

## Takdang Aralin

[Gumawa ng sarili mong custom na visualisasyon](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.