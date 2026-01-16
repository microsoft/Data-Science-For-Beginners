<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4039f1c76548d144a0aee0bf28304ec",
  "translation_date": "2025-08-30T18:55:30+00:00",
  "source_file": "3-Data-Visualization/R/13-meaningful-vizualizations/README.md",
  "language_code": "sl"
}
-->
# Ustvarjanje smiselnih vizualizacij

|![ Sketchnote avtorja [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Smiselne vizualizacije - _Sketchnote avtorja [@nitya](https://twitter.com/nitya)_ |

> "Če dovolj dolgo mučiš podatke, bodo priznali karkoli." -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

Ena osnovnih veščin podatkovnega znanstvenika je sposobnost ustvarjanja smiselnih vizualizacij podatkov, ki pomagajo odgovoriti na zastavljena vprašanja. Preden vizualizirate svoje podatke, morate zagotoviti, da so očiščeni in pripravljeni, kot ste to storili v prejšnjih lekcijah. Nato lahko začnete razmišljati, kako najbolje predstaviti podatke.

V tej lekciji boste pregledali:

1. Kako izbrati pravi tip grafa
2. Kako se izogniti zavajajočim grafom
3. Kako delati z barvami
4. Kako oblikovati grafe za boljšo berljivost
5. Kako ustvariti animirane ali 3D grafe
6. Kako ustvariti kreativno vizualizacijo

## [Predlekcijski kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/24)

## Izberite pravi tip grafa

V prejšnjih lekcijah ste eksperimentirali z ustvarjanjem različnih zanimivih vizualizacij podatkov z uporabo knjižnic Matplotlib in Seaborn. Na splošno lahko izberete [pravi tip grafa](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) za vprašanje, ki ga zastavljate, s pomočjo te tabele:

| Potrebujete:               | Uporabite:                     |
| -------------------------- | ----------------------------- |
| Prikazati trende skozi čas | Črta                          |
| Primerjati kategorije      | Stolpec, Krog                 |
| Primerjati skupne vrednosti| Krog, Zloženi stolpec         |
| Prikazati odnose           | Raztresen, Črta, Facet, Dvojna črta |
| Prikazati porazdelitve     | Raztresen, Histogram, Škatla  |
| Prikazati deleže           | Krog, Obroč, Vafelj          |

> ✅ Glede na sestavo vaših podatkov boste morda morali pretvoriti besedilo v številčne vrednosti, da bo določen graf deloval.

## Izogibajte se zavajanju

Tudi če podatkovni znanstvenik skrbno izbere pravi graf za prave podatke, obstaja veliko načinov, kako lahko podatke prikažemo tako, da podpirajo določeno točko, pogosto na račun resničnosti podatkov. Obstaja veliko primerov zavajajočih grafov in infografik!

[![Kako grafi lažejo avtorja Alberta Caira](../../../../../translated_images/sl/tornado.2880ffc7f135f82b5e5328624799010abefd1080ae4b7ecacbdc7d792f1d8849.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "Kako grafi lažejo")

> 🎥 Kliknite zgornjo sliko za konferenčno predavanje o zavajajočih grafih

Ta graf obrne os X, da prikaže nasprotje resnice, glede na datum:

![slab graf 1](../../../../../translated_images/sl/bad-chart-1.596bc93425a8ac301a28b8361f59a970276e7b961658ce849886aa1fed427341.png)

[Ta graf](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) je še bolj zavajajoč, saj pogled pritegne desno stran, kar daje vtis, da so se primeri COVID-a skozi čas zmanjšali v različnih okrožjih. Če pa natančno pogledate datume, ugotovite, da so bili preurejeni, da bi ustvarili zavajajoč trend navzdol.

![slab graf 2](../../../../../translated_images/sl/bad-chart-2.62edf4d2f30f4e519f5ef50c07ce686e27b0196a364febf9a4d98eecd21f9f60.jpg)

Ta zloglasni primer uporablja barvo IN obrnjeno os Y za zavajanje: namesto da bi sklepali, da so se smrti zaradi orožja povečale po sprejetju zakonodaje, prijazne do orožja, je pogled zaveden, da misli, da je resnica nasprotna:

![slab graf 3](../../../../../translated_images/sl/bad-chart-3.e201e2e915a230bc2cde289110604ec9abeb89be510bd82665bebc1228258972.jpg)

Ta nenavaden graf prikazuje, kako je mogoče manipulirati s proporci, kar vodi do smešnih rezultatov:

![slab graf 4](../../../../../translated_images/sl/bad-chart-4.8872b2b881ffa96c3e0db10eb6aed7793efae2cac382c53932794260f7bfff07.jpg)

Primerjanje neprimerljivega je še en dvomljiv trik. Obstaja [odlična spletna stran](https://tylervigen.com/spurious-correlations), ki prikazuje 'lažne korelacije', kot so 'dejstva', ki povezujejo stopnjo ločitev v Mainu in porabo margarine. Skupina na Redditu prav tako zbira [grde primere](https://www.reddit.com/r/dataisugly/top/?t=all) uporabe podatkov.

Pomembno je razumeti, kako zlahka lahko pogled zavedejo zavajajoči grafi. Tudi če so nameni podatkovnega znanstvenika dobri, lahko izbira napačnega tipa grafa, kot je krožni graf z preveč kategorijami, zavede.

## Barve

Kot ste videli v zgornjem grafu o 'nasilju z orožjem na Floridi', lahko barva doda dodatno plast pomena grafom, še posebej tistim, ki niso zasnovani z uporabo knjižnic, kot sta ggplot2 in RColorBrewer, ki vključujejo različne preverjene barvne knjižnice in palete. Če graf ustvarjate ročno, si vzemite čas za študij [teorije barv](https://colormatters.com/color-and-design/basic-color-theory).

> ✅ Zavedajte se, da je pri oblikovanju grafov dostopnost pomemben vidik vizualizacije. Nekateri vaši uporabniki so lahko barvno slepi - ali je vaš graf berljiv za uporabnike z okvarami vida?

Bodite previdni pri izbiri barv za svoj graf, saj lahko barva prenaša pomen, ki ga morda niste nameravali. 'Rožnate dame' v zgornjem grafu o 'višini' prenašajo izrazito 'ženski' pomen, ki še povečuje nenavadnost grafa.

Čeprav se [pomen barv](https://colormatters.com/color-symbolism/the-meanings-of-colors) lahko razlikuje v različnih delih sveta in se spreminja glede na odtenek, splošno velja:

| Barva  | Pomen               |
| ------ | ------------------- |
| rdeča  | moč                |
| modra  | zaupanje, lojalnost |
| rumena | sreča, previdnost  |
| zelena | ekologija, sreča, zavist |
| vijolična | sreča            |
| oranžna | živahnost         |

Če morate ustvariti graf z lastnimi barvami, poskrbite, da bodo vaši grafi dostopni in da barva, ki jo izberete, ustreza pomenu, ki ga želite prenesti.

## Oblikovanje grafov za boljšo berljivost

Grafi niso smiselni, če niso berljivi! Vzemite si trenutek za razmislek o oblikovanju širine in višine grafa, da se dobro prilega vašim podatkom. Če je treba prikazati eno spremenljivko (na primer vseh 50 držav), jih prikažite navpično na osi Y, če je mogoče, da se izognete grafu, ki zahteva vodoravno pomikanje.

Označite svoje osi, zagotovite legendo, če je potrebno, in ponudite orodja za boljše razumevanje podatkov.

Če so vaši podatki besedilni in obsežni na osi X, lahko besedilo nagnite za boljšo berljivost. [plot3D](https://cran.r-project.org/web/packages/plot3D/index.html) omogoča 3D risanje, če vaši podatki to podpirajo. Z njim je mogoče ustvariti napredne vizualizacije podatkov.

![3d grafi](../../../../../translated_images/sl/3d.db1734c151eee87d924989306a00e23f8cddac6a0aab122852ece220e9448def.png)

## Animacija in prikaz 3D grafov

Nekatere najboljše vizualizacije podatkov danes so animirane. Shirley Wu je ustvarila neverjetne vizualizacije z D3, kot je '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', kjer vsak cvet predstavlja vizualizacijo filma. Drug primer za Guardian je 'bussed out', interaktivna izkušnja, ki združuje vizualizacije z Greensock in D3 ter format članka za prikaz, kako NYC rešuje problem brezdomcev z njihovim prevozom iz mesta.

![bussing](../../../../../translated_images/sl/busing.8157cf1bc89a3f65052d362a78c72f964982ceb9dcacbe44480e35909c3dce62.png)

> "Bussed Out: How America Moves its Homeless" iz [Guardiana](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Vizualizacije avtorjev Nadieh Bremer & Shirley Wu

Čeprav ta lekcija ni dovolj poglobljena za učenje teh zmogljivih knjižnic za vizualizacijo, poskusite uporabiti D3 v aplikaciji Vue.js z uporabo knjižnice za prikaz vizualizacije knjige "Nevarna razmerja" kot animirano socialno omrežje.

> "Les Liaisons Dangereuses" je epistolarni roman, predstavljen kot serija pisem. Napisal ga je Choderlos de Laclos leta 1782 in pripoveduje zgodbo o zlobnih, moralno pokvarjenih družbenih manevrih dveh protagonistov francoskega plemstva v poznem 18. stoletju, vikonta de Valmonta in markize de Merteuil. Oba na koncu propadeta, vendar ne brez povzročanja velike družbene škode. Roman se odvija kot serija pisem, napisanih različnim ljudem v njunem krogu, z namenom maščevanja ali povzročanja težav. Ustvarite vizualizacijo teh pisem, da odkrijete glavne akterje zgodbe, vizualno.

Dokončali boste spletno aplikacijo, ki bo prikazala animiran pogled tega socialnega omrežja. Uporablja knjižnico, zasnovano za ustvarjanje [vizualizacije omrežja](https://github.com/emiliorizzo/vue-d3-network) z uporabo Vue.js in D3. Ko aplikacija deluje, lahko premikate vozlišča po zaslonu in premešate podatke.

![liaisons](../../../../../translated_images/sl/liaisons.90ce7360bcf8476558f700bbbaf198ad697d5b5cb2829ba141a89c0add7c6ecd.png)

## Projekt: Ustvarite graf za prikaz omrežja z uporabo D3.js

> Ta mapa lekcije vključuje mapo `solution`, kjer lahko najdete dokončan projekt za referenco.

1. Sledite navodilom v datoteki README.md v korenski mapi začetnega projekta. Pred namestitvijo odvisnosti projekta poskrbite, da imate na računalniku nameščena NPM in Node.js.

2. Odprite mapo `starter/src`. V mapi `assets` boste našli datoteko .json z vsemi pismi iz romana, oštevilčenimi, z oznakama 'to' in 'from'.

3. Dokončajte kodo v datoteki `components/Nodes.vue`, da omogočite vizualizacijo. Poiščite metodo `createLinks()` in dodajte naslednjo zanko.

Prebrskajte objekt .json, da zajamete podatke 'to' in 'from' za pisma ter zgradite objekt `links`, ki ga lahko knjižnica za vizualizacijo uporabi:

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

Zaženite svojo aplikacijo iz terminala (npm run serve) in uživajte v vizualizaciji!

## 🚀 Izziv

Raziščite internet in odkrijte zavajajoče vizualizacije. Kako avtor zavede uporabnika in ali je to namerno? Poskusite popraviti vizualizacije, da prikažete, kako bi morale izgledati.

## [Po-lekcijski kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/25)

## Pregled in samostojno učenje

Tukaj je nekaj člankov o zavajajočih vizualizacijah podatkov:

https://gizmodo.com/how-to-lie-with-data-visualization-1563576606

http://ixd.prattsi.org/2017/12/visual-lies-usability-in-deceptive-data-visualizations/

Oglejte si te zanimive vizualizacije zgodovinskih virov in artefaktov:

https://handbook.pubpub.org/

Preberite ta članek o tem, kako animacija lahko izboljša vaše vizualizacije:

https://medium.com/@EvanSinar/use-animation-to-supercharge-data-visualization-cd905a882ad4

## Naloga

[Ustvarite svojo lastno vizualizacijo](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.