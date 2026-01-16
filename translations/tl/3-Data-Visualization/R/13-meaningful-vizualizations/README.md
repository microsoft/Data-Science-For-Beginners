<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4039f1c76548d144a0aee0bf28304ec",
  "translation_date": "2025-08-28T02:37:46+00:00",
  "source_file": "3-Data-Visualization/R/13-meaningful-vizualizations/README.md",
  "language_code": "tl"
}
-->
# Paggawa ng Makahulugang Visualisasyon

|![ Sketchnote ni [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Makahulugang Visualisasyon - _Sketchnote ni [@nitya](https://twitter.com/nitya)_ |

> "Kung pipilitin mo ang datos nang matagal, aamin ito ng kahit ano" -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

Isa sa mga pangunahing kasanayan ng isang data scientist ay ang kakayahang lumikha ng makahulugang visualisasyon ng datos na tumutulong sagutin ang mga tanong na maaaring mayroon ka. Bago mag-visualize ng datos, kailangang tiyakin na ito ay nalinis at naihanda, tulad ng ginawa mo sa mga nakaraang aralin. Pagkatapos nito, maaari ka nang magdesisyon kung paano pinakamahusay na ipapakita ang datos.

Sa araling ito, tatalakayin mo ang:

1. Paano pumili ng tamang uri ng tsart  
2. Paano iwasan ang mapanlinlang na tsart  
3. Paano gumamit ng kulay  
4. Paano istilohan ang iyong mga tsart para sa mas madaling basahin  
5. Paano gumawa ng animated o 3D na solusyon sa tsart  
6. Paano gumawa ng malikhaing visualisasyon  

## [Pre-Lecture Quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/24)

## Pumili ng tamang uri ng tsart

Sa mga nakaraang aralin, sinubukan mong gumawa ng iba't ibang uri ng visualisasyon ng datos gamit ang Matplotlib at Seaborn para sa paggawa ng tsart. Sa pangkalahatan, maaari mong piliin ang [tamang uri ng tsart](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) para sa tanong na nais mong sagutin gamit ang talahanayang ito:

| Kailangan mong:            | Dapat mong gamitin:             |
| -------------------------- | ------------------------------- |
| Ipakita ang mga trend ng datos sa paglipas ng panahon | Line                            |
| Ihambing ang mga kategorya | Bar, Pie                        |
| Ihambing ang kabuuan       | Pie, Stacked Bar                |
| Ipakita ang mga relasyon   | Scatter, Line, Facet, Dual Line |
| Ipakita ang distribusyon   | Scatter, Histogram, Box         |
| Ipakita ang proporsyon     | Pie, Donut, Waffle              |

> ✅ Depende sa anyo ng iyong datos, maaaring kailanganin mong i-convert ito mula text patungong numeric upang suportahan ang isang partikular na tsart.

## Iwasan ang panlilinlang

Kahit na maingat ang isang data scientist sa pagpili ng tamang tsart para sa tamang datos, maraming paraan upang maipakita ang datos sa paraang nagpapakita ng isang punto, madalas sa kapinsalaan ng datos mismo. Maraming halimbawa ng mapanlinlang na tsart at infographics!

[![Paano Nagsisinungaling ang mga Tsart ni Alberto Cairo](../../../../../translated_images/tl/tornado.2880ffc7f135f82b5e5328624799010abefd1080ae4b7ecacbdc7d792f1d8849.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "Paano Nagsisinungaling ang mga Tsart")

> 🎥 I-click ang larawan sa itaas para sa isang talakayan tungkol sa mapanlinlang na mga tsart

Ang tsart na ito ay binabaliktad ang X axis upang ipakita ang kabaligtaran ng katotohanan, batay sa petsa:

![masamang tsart 1](../../../../../translated_images/tl/bad-chart-1.596bc93425a8ac301a28b8361f59a970276e7b961658ce849886aa1fed427341.png)

[Ang tsart na ito](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) ay mas mapanlinlang pa, dahil ang mata ay naaakit sa kanan upang isipin na, sa paglipas ng panahon, ang mga kaso ng COVID ay bumaba sa iba't ibang mga county. Sa katunayan, kung titingnan mong mabuti ang mga petsa, makikita mong inayos ang mga ito upang magmukhang pababa ang trend.

![masamang tsart 2](../../../../../translated_images/tl/bad-chart-2.62edf4d2f30f4e519f5ef50c07ce686e27b0196a364febf9a4d98eecd21f9f60.jpg)

Ang kilalang halimbawa na ito ay gumagamit ng kulay AT baliktad na Y axis upang manlinlang: sa halip na isipin na tumaas ang mga pagkamatay dahil sa baril pagkatapos ng pagpasa ng batas na pabor sa baril, ang mata ay nalilinlang upang isipin ang kabaligtaran:

![masamang tsart 3](../../../../../translated_images/tl/bad-chart-3.e201e2e915a230bc2cde289110604ec9abeb89be510bd82665bebc1228258972.jpg)

Ang kakaibang tsart na ito ay nagpapakita kung paano maaaring manipulahin ang proporsyon, na nagdudulot ng nakakatawang epekto:

![masamang tsart 4](../../../../../translated_images/tl/bad-chart-4.8872b2b881ffa96c3e0db10eb6aed7793efae2cac382c53932794260f7bfff07.jpg)

Ang paghahambing ng mga bagay na hindi maihahambing ay isa pang mapanlinlang na taktika. Mayroong [kahanga-hangang website](https://tylervigen.com/spurious-correlations) na nagpapakita ng 'spurious correlations' na nagtatampok ng 'mga katotohanan' na nag-uugnay sa mga bagay tulad ng rate ng diborsyo sa Maine at ang pagkonsumo ng margarina. Ang isang Reddit group ay nangongolekta rin ng [pangit na paggamit](https://www.reddit.com/r/dataisugly/top/?t=all) ng datos.

Mahalagang maunawaan kung gaano kadaling malinlang ang mata ng mga mapanlinlang na tsart. Kahit na mabuti ang intensyon ng data scientist, ang pagpili ng maling uri ng tsart, tulad ng pie chart na nagpapakita ng masyadong maraming kategorya, ay maaaring mapanlinlang.

## Kulay

Nakita mo sa 'Florida gun violence' chart sa itaas kung paano maaaring magbigay ng karagdagang kahulugan ang kulay sa mga tsart, lalo na ang mga hindi dinisenyo gamit ang mga library tulad ng ggplot2 at RColorBrewer na may iba't ibang na-vet na color libraries at palettes. Kung gumagawa ka ng tsart nang mano-mano, maglaan ng oras upang mag-aral ng [teorya ng kulay](https://colormatters.com/color-and-design/basic-color-theory).

> ✅ Tandaan, kapag nagdidisenyo ng mga tsart, na ang accessibility ay mahalagang aspeto ng visualisasyon. Ang ilan sa iyong mga gumagamit ay maaaring may color blindness - nagpapakita ba nang maayos ang iyong tsart para sa mga may kapansanan sa paningin?

Mag-ingat sa pagpili ng mga kulay para sa iyong tsart, dahil ang kulay ay maaaring maghatid ng kahulugan na hindi mo sinasadya. Ang 'pink ladies' sa 'height' chart sa itaas ay nagdadala ng isang malinaw na 'pambabae' na kahulugan na nagdaragdag sa kakaibang anyo ng tsart mismo.

Habang ang [kahulugan ng kulay](https://colormatters.com/color-symbolism/the-meanings-of-colors) ay maaaring magkaiba sa iba't ibang bahagi ng mundo, at may posibilidad na magbago depende sa lilim nito. Sa pangkalahatan, ang mga kahulugan ng kulay ay kinabibilangan ng:

| Kulay  | Kahulugan           |
| ------ | ------------------- |
| pula   | kapangyarihan       |
| asul   | tiwala, katapatan   |
| dilaw  | kasiyahan, babala   |
| berde  | ekolohiya, swerte, inggit |
| lila   | kasiyahan           |
| kahel  | sigla               |

Kung ikaw ay inatasang gumawa ng tsart na may custom na mga kulay, tiyakin na ang iyong mga tsart ay parehong accessible at ang kulay na iyong pinili ay tumutugma sa kahulugan na nais mong iparating.

## Istilohan ang iyong mga tsart para sa mas madaling basahin

Ang mga tsart ay hindi makahulugan kung hindi ito madaling basahin! Maglaan ng oras upang isaalang-alang ang pag-istilo ng lapad at taas ng iyong tsart upang magkasya nang maayos sa iyong datos. Kung ang isang variable (tulad ng lahat ng 50 estado) ay kailangang ipakita, ipakita ang mga ito nang patayo sa Y axis kung maaari upang maiwasan ang isang tsart na kailangang i-scroll nang pahalang.

Lagyan ng label ang iyong mga axis, magbigay ng legend kung kinakailangan, at mag-alok ng tooltips para sa mas mahusay na pag-unawa sa datos.

Kung ang iyong datos ay tekstwal at mahaba sa X axis, maaari mong i-anggulo ang teksto para sa mas madaling basahin. Ang [plot3D](https://cran.r-project.org/web/packages/plot3D/index.html) ay nag-aalok ng 3D plotting, kung sinusuportahan ito ng iyong datos. Ang mga sopistikadong visualisasyon ng datos ay maaaring gawin gamit ito.

![3d plots](../../../../../translated_images/tl/3d.db1734c151eee87d924989306a00e23f8cddac6a0aab122852ece220e9448def.png)

## Animation at 3D na pagpapakita ng tsart

Ang ilan sa mga pinakamahusay na visualisasyon ng datos ngayon ay animated. Si Shirley Wu ay may mga kamangha-manghang gawa gamit ang D3, tulad ng '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', kung saan ang bawat bulaklak ay isang visualisasyon ng isang pelikula. Isa pang halimbawa para sa Guardian ay 'bussed out', isang interactive na karanasan na pinagsasama ang mga visualisasyon gamit ang Greensock at D3 kasama ang isang scrollytelling na format ng artikulo upang ipakita kung paano hinahawakan ng NYC ang problema nito sa mga walang tirahan sa pamamagitan ng pagdadala ng mga tao palabas ng lungsod.

![busing](../../../../../translated_images/tl/busing.8157cf1bc89a3f65052d362a78c72f964982ceb9dcacbe44480e35909c3dce62.png)

> "Bussed Out: Paano Inililipat ng Amerika ang mga Walang Tirahan" mula sa [the Guardian](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Mga visualisasyon nina Nadieh Bremer & Shirley Wu

Bagama't hindi sapat ang araling ito upang talakayin nang malalim ang mga makapangyarihang library ng visualisasyon, subukan ang iyong kakayahan sa D3 sa isang Vue.js app gamit ang isang library upang ipakita ang isang visualisasyon ng aklat na "Dangerous Liaisons" bilang isang animated na social network.

> "Les Liaisons Dangereuses" ay isang epistolaryong nobela, o isang nobela na iniharap bilang isang serye ng mga liham. Isinulat noong 1782 ni Choderlos de Laclos, ito ay nagsasalaysay ng kuwento ng masama at moral na bangkaroteng mga galaw panlipunan ng dalawang naglalabanang pangunahing tauhan ng aristokrasya ng Pransya noong huling bahagi ng ika-18 siglo, ang Vicomte de Valmont at ang Marquise de Merteuil. Pareho silang nagwawakas sa trahedya ngunit hindi bago magdulot ng malaking pinsala sa lipunan. Ang nobela ay nagbubukas bilang isang serye ng mga liham na isinulat sa iba't ibang tao sa kanilang mga bilog, nagbabalak ng paghihiganti o simpleng magdulot ng kaguluhan. Gumawa ng isang visualisasyon ng mga liham na ito upang matuklasan ang mga pangunahing tauhan ng kuwento, sa biswal na paraan.

Kukumpletuhin mo ang isang web app na magpapakita ng isang animated na view ng social network na ito. Gumagamit ito ng isang library na ginawa upang lumikha ng isang [visual ng isang network](https://github.com/emiliorizzo/vue-d3-network) gamit ang Vue.js at D3. Kapag tumatakbo na ang app, maaari mong hilahin ang mga node sa screen upang i-shuffle ang datos.

![liaisons](../../../../../translated_images/tl/liaisons.90ce7360bcf8476558f700bbbaf198ad697d5b5cb2829ba141a89c0add7c6ecd.png)

## Proyekto: Gumawa ng tsart upang ipakita ang isang network gamit ang D3.js

> Ang folder ng araling ito ay may kasamang `solution` folder kung saan makikita mo ang kumpletong proyekto, para sa iyong sanggunian.

1. Sundin ang mga tagubilin sa README.md file sa root ng starter folder. Tiyaking mayroon kang NPM at Node.js na tumatakbo sa iyong makina bago i-install ang mga dependency ng iyong proyekto.

2. Buksan ang `starter/src` folder. Makikita mo ang isang `assets` folder kung saan mayroong .json file na naglalaman ng lahat ng mga liham mula sa nobela, na may bilang, at may anotasyon na 'to' at 'from'.

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

Maglibot sa internet upang matuklasan ang mga mapanlinlang na visualisasyon. Paano nililinlang ng may-akda ang gumagamit, at ito ba ay sinasadya? Subukang itama ang mga visualisasyon upang ipakita kung paano dapat ang mga ito.

## [Post-lecture quiz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/25)

## Pagsusuri at Pag-aaral sa Sarili

Narito ang ilang mga artikulo na maaaring basahin tungkol sa mapanlinlang na visualisasyon ng datos:

https://gizmodo.com/how-to-lie-with-data-visualization-1563576606

http://ixd.prattsi.org/2017/12/visual-lies-usability-in-deceptive-data-visualizations/

Tingnan ang mga interesanteng visualisasyon para sa mga makasaysayang assets at artifacts:

https://handbook.pubpub.org/

Basahin ang artikulong ito tungkol sa kung paano maaaring mapahusay ng animation ang iyong mga visualisasyon:

https://medium.com/@EvanSinar/use-animation-to-supercharge-data-visualization-cd905a882ad4

## Takdang-Aralin

[Gumawa ng sarili mong custom na visualisasyon](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.