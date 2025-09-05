<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cfb068050337a36e348debaa502a24fa",
  "translation_date": "2025-09-05T19:40:22+00:00",
  "source_file": "3-Data-Visualization/13-meaningful-visualizations/README.md",
  "language_code": "sl"
}
-->
# Ustvarjanje smiselnih vizualizacij

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Smiselne vizualizacije - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

> "Če dovolj dolgo mučiš podatke, ti bodo priznali karkoli" -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

Ena osnovnih veščin podatkovnega znanstvenika je sposobnost ustvarjanja smiselne vizualizacije podatkov, ki pomaga odgovoriti na vprašanja, ki jih imate. Preden vizualizirate svoje podatke, morate poskrbeti, da so očiščeni in pripravljeni, kot ste to storili v prejšnjih lekcijah. Nato lahko začnete razmišljati, kako najbolje predstaviti podatke.

V tej lekciji boste pregledali:

1. Kako izbrati pravi tip grafikona
2. Kako se izogniti zavajajočim grafom
3. Kako delati z barvami
4. Kako oblikovati grafe za boljšo berljivost
5. Kako ustvariti animirane ali 3D rešitve za grafe
6. Kako ustvariti kreativno vizualizacijo

## [Predlekcijski kviz](https://ff-quizzes.netlify.app/en/ds/quiz/24)

## Izberite pravi tip grafikona

V prejšnjih lekcijah ste eksperimentirali z ustvarjanjem različnih zanimivih vizualizacij podatkov z uporabo knjižnic Matplotlib in Seaborn. Na splošno lahko izberete [pravi tip grafikona](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) glede na vprašanje, ki ga zastavljate, s pomočjo te tabele:

| Potrebujete:               | Uporabite:                     |
| -------------------------- | ------------------------------ |
| Prikazati trende skozi čas | Črta                           |
| Primerjati kategorije      | Stolpec, Krog                  |
| Primerjati skupne vrednosti| Krog, Zloženi stolpec          |
| Prikazati odnose           | Razpršenost, Črta, Faset, Dvojna črta |
| Prikazati porazdelitve     | Razpršenost, Histogram, Škatla |
| Prikazati deleže           | Krog, Obroč, Vafelj            |

> ✅ Glede na sestavo vaših podatkov boste morda morali pretvoriti besedilo v številčne vrednosti, da bo določen grafikon deloval.

## Izogibajte se zavajanju

Tudi če podatkovni znanstvenik skrbno izbere pravi grafikon za prave podatke, obstaja veliko načinov, kako lahko podatki prikazujejo napačno sliko, pogosto na račun resničnosti podatkov. Obstaja veliko primerov zavajajočih grafov in infografik!

[![Kako grafi lažejo, Alberto Cairo](../../../../3-Data-Visualization/13-meaningful-visualizations/images/tornado.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "Kako grafi lažejo")

> 🎥 Kliknite zgornjo sliko za konferenčno predavanje o zavajajočih grafih

Ta grafikon obrne os X, da prikaže nasprotno od resnice, glede na datum:

![slab grafikon 1](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-1.png)

[Ta grafikon](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) je še bolj zavajajoč, saj oko pritegne desno stran, kar daje vtis, da so se primeri COVID-a skozi čas zmanjšali v različnih okrožjih. Če pa natančno pogledate datume, ugotovite, da so bili preurejeni, da ustvarijo zavajajoč trend upadanja.

![slab grafikon 2](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-2.jpg)

Ta zloglasni primer uporablja barvo IN obrnjeno os Y za zavajanje: namesto da bi sklepali, da so se smrti zaradi orožja povečale po sprejetju zakonodaje, ki podpira orožje, je oko zavedeno, da misli, da je resnica ravno obratna:

![slab grafikon 3](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-3.jpg)

Ta nenavaden grafikon prikazuje, kako se lahko deleži manipulirajo, kar vodi do smešnih rezultatov:

![slab grafikon 4](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-4.jpg)

Primerjava neprimerljivega je še ena senčna taktika. Obstaja [čudovita spletna stran](https://tylervigen.com/spurious-correlations), ki prikazuje 'lažne korelacije', kot so 'dejstva', ki povezujejo stopnjo ločitev v Maineu in porabo margarine. Skupina na Redditu prav tako zbira [grde primere](https://www.reddit.com/r/dataisugly/top/?t=all) uporabe podatkov.

Pomembno je razumeti, kako zlahka lahko oko zavedemo z zavajajočimi grafi. Tudi če je namen podatkovnega znanstvenika dober, lahko izbira napačnega tipa grafikona, kot je krožni grafikon s preveč kategorijami, vodi v zavajanje.

## Barve

V zgornjem grafu o 'nasilju s strelnim orožjem na Floridi' ste videli, kako lahko barva doda dodatno plast pomena grafom, še posebej tistim, ki niso zasnovani z uporabo knjižnic, kot sta Matplotlib in Seaborn, ki vključujeta različne preverjene barvne knjižnice in palete. Če grafikon izdelujete ročno, si vzemite čas za študij [teorije barv](https://colormatters.com/color-and-design/basic-color-theory).

> ✅ Zavedajte se, da je pri oblikovanju grafov dostopnost pomemben vidik vizualizacije. Nekateri vaši uporabniki so lahko barvno slepi - ali vaš grafikon dobro deluje za uporabnike z motnjami vida?

Bodite previdni pri izbiri barv za svoj grafikon, saj lahko barva prenese pomen, ki ga morda ne nameravate. 'Rožnate dame' v zgornjem grafu o 'višini' prenašajo izrazito 'ženski' pomen, ki prispeva k nenavadnosti samega grafikona.

Medtem ko se [pomen barv](https://colormatters.com/color-symbolism/the-meanings-of-colors) lahko razlikuje v različnih delih sveta in se spreminja glede na odtenek, splošno gledano vključuje:

| Barva  | Pomen               |
| ------ | ------------------- |
| rdeča  | moč                 |
| modra  | zaupanje, zvestoba  |
| rumena | sreča, previdnost   |
| zelena | ekologija, sreča, zavist |
| vijolična | sreča             |
| oranžna | živahnost          |

Če morate ustvariti grafikon z lastnimi barvami, poskrbite, da bodo vaši grafi dostopni in da barva, ki jo izberete, ustreza pomenu, ki ga želite prenesti.

## Oblikovanje grafov za berljivost

Grafi niso smiselni, če niso berljivi! Vzemite si trenutek za razmislek o prilagoditvi širine in višine grafikona, da se dobro prilega vašim podatkom. Če je treba prikazati eno spremenljivko (na primer vseh 50 zveznih držav), jih prikažite navpično na osi Y, če je mogoče, da se izognete grafu, ki zahteva horizontalno drsenje.

Označite osi, zagotovite legendo, če je potrebno, in ponudite orodne nasvete za boljše razumevanje podatkov.

Če so vaši podatki besedilni in obsežni na osi X, lahko besedilo nagnite za boljšo berljivost. [Matplotlib](https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html) omogoča 3D grafiko, če vaši podatki to podpirajo. S pomočjo `mpl_toolkits.mplot3d` lahko ustvarite sofisticirane vizualizacije podatkov.

![3D grafi](../../../../3-Data-Visualization/13-meaningful-visualizations/images/3d.png)

## Animacija in prikaz 3D grafov

Nekatere najboljše vizualizacije podatkov danes so animirane. Shirley Wu je ustvarila izjemne vizualizacije z D3, kot so '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', kjer vsak cvet predstavlja vizualizacijo filma. Drug primer za Guardian je 'bussed out', interaktivna izkušnja, ki združuje vizualizacije z Greensock in D3 ter format članka za prikaz, kako NYC obravnava problem brezdomcev z njihovim prevozom iz mesta.

![prevoz](../../../../3-Data-Visualization/13-meaningful-visualizations/images/busing.png)

> "Bussed Out: Kako Amerika premika svoje brezdomce" iz [Guardiana](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Vizualizacije: Nadieh Bremer & Shirley Wu

Čeprav ta lekcija ni dovolj poglobljena, da bi vas naučila teh močnih knjižnic za vizualizacijo, poskusite uporabiti D3 v aplikaciji Vue.js z uporabo knjižnice za prikaz vizualizacije knjige "Nevarne zveze" kot animirano socialno omrežje.

> "Les Liaisons Dangereuses" je epistolarni roman, predstavljen kot serija pisem. Napisal ga je Choderlos de Laclos leta 1782 in pripoveduje zgodbo o zlobnih, moralno pokvarjenih družbenih manevrih dveh protagonistov francoske aristokracije v poznem 18. stoletju, vikonta de Valmonta in markize de Merteuil. Oba na koncu propadeta, vendar ne brez povzročanja velike družbene škode. Roman se odvija kot serija pisem, napisanih različnim ljudem v njihovih krogih, z namenom maščevanja ali zgolj povzročanja težav. Ustvarite vizualizacijo teh pisem, da odkrijete glavne akterje zgodbe, vizualno.

Dokončali boste spletno aplikacijo, ki bo prikazala animiran pogled na to socialno omrežje. Uporablja knjižnico, ki je bila ustvarjena za [vizualizacijo omrežja](https://github.com/emiliorizzo/vue-d3-network) z uporabo Vue.js in D3. Ko aplikacija deluje, lahko premikate vozlišča po zaslonu, da premešate podatke.

![zveze](../../../../3-Data-Visualization/13-meaningful-visualizations/images/liaisons.png)

## Projekt: Ustvarite grafikon za prikaz omrežja z D3.js

> Ta mapa lekcije vključuje mapo `solution`, kjer lahko najdete dokončan projekt za referenco.

1. Sledite navodilom v datoteki README.md v korenski mapi začetnega projekta. Pred namestitvijo odvisnosti projekta poskrbite, da imate na računalniku nameščen NPM in Node.js.

2. Odprite mapo `starter/src`. V njej boste našli mapo `assets`, kjer je .json datoteka z vsemi pismi iz romana, oštevilčenimi, z oznakami 'to' in 'from'.

3. Dokončajte kodo v `components/Nodes.vue`, da omogočite vizualizacijo. Poiščite metodo `createLinks()` in dodajte naslednjo zanko.

Prebrskajte .json objekt, da zajamete podatke 'to' in 'from' za pisma ter zgradite objekt `links`, da ga lahko knjižnica za vizualizacijo uporabi:

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

Raziskujte internet in odkrijte zavajajoče vizualizacije. Kako avtor zavaja uporabnika in ali je to namerno? Poskusite popraviti vizualizacije, da pokažete, kako bi morale izgledati.

## [Po-lekcijski kviz](https://ff-quizzes.netlify.app/en/ds/quiz/25)

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
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.