<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b380bb6d34102bb061eb41de23d9834",
  "translation_date": "2025-09-05T06:02:53+00:00",
  "source_file": "3-Data-Visualization/13-meaningful-visualizations/README.md",
  "language_code": "sl"
}
-->
# Ustvarjanje smiselnih vizualizacij

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Smiselne vizualizacije - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

> "Če dovolj dolgo mučiš podatke, ti bodo priznali karkoli" -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

Ena od osnovnih veščin podatkovnega znanstvenika je sposobnost ustvarjanja smiselne vizualizacije podatkov, ki pomaga odgovoriti na vprašanja, ki jih imate. Preden vizualizirate svoje podatke, morate poskrbeti, da so očiščeni in pripravljeni, kot ste to storili v prejšnjih lekcijah. Nato lahko začnete razmišljati, kako najbolje predstaviti podatke.

V tej lekciji boste pregledali:

1. Kako izbrati pravi tip grafa
2. Kako se izogniti zavajajočim grafom
3. Kako delati z barvami
4. Kako oblikovati grafe za boljšo berljivost
5. Kako ustvariti animirane ali 3D rešitve za grafe
6. Kako ustvariti kreativno vizualizacijo

## [Predlekcijski kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/24)

## Izberite pravi tip grafa

V prejšnjih lekcijah ste eksperimentirali z ustvarjanjem različnih zanimivih vizualizacij podatkov z uporabo knjižnic Matplotlib in Seaborn. Na splošno lahko izberete [pravi tip grafa](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) glede na vprašanje, ki ga zastavljate, s pomočjo te tabele:

| Potrebujete:               | Uporabite:                     |
| -------------------------- | ------------------------------ |
| Prikazati trende skozi čas | Črta                           |
| Primerjati kategorije      | Stolpec, Krog                  |
| Primerjati skupne vrednosti| Krog, Zloženi stolpec          |
| Prikazati odnose           | Razpršen, Črta, Faset, Dvojna črta |
| Prikazati porazdelitve     | Razpršen, Histogram, Škatla    |
| Prikazati deleže           | Krog, Obroč, Vafelj            |

> ✅ Glede na sestavo vaših podatkov boste morda morali pretvoriti besedilo v številčne vrednosti, da bo graf podprt.

## Izogibajte se zavajanju

Tudi če podatkovni znanstvenik skrbno izbere pravi graf za prave podatke, obstaja veliko načinov, kako lahko podatki prikazujejo napačne zaključke, pogosto na račun resničnosti podatkov. Obstaja veliko primerov zavajajočih grafov in infografik!

[![Kako grafi lažejo, Alberto Cairo](../../../../3-Data-Visualization/13-meaningful-visualizations/images/tornado.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "Kako grafi lažejo")

> 🎥 Kliknite zgornjo sliko za konferenčno predavanje o zavajajočih grafih

Ta graf obrne X os, da prikaže nasprotje resnice, glede na datum:

![slab graf 1](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-1.png)

[Ta graf](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) je še bolj zavajajoč, saj oko pritegne desno stran, kar daje vtis, da so se primeri COVID-a v različnih okrožjih sčasoma zmanjšali. Če pa natančno pogledate datume, ugotovite, da so bili preurejeni, da ustvarijo zavajajoč trend upadanja.

![slab graf 2](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-2.jpg)

Ta zloglasni primer uporablja barvo IN obrnjeno Y os za zavajanje: namesto da bi sklepali, da so se smrti zaradi orožja povečale po sprejetju zakonodaje, ki podpira orožje, oko zavaja, da misli, da je resnica nasprotna:

![slab graf 3](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-3.jpg)

Ta nenavaden graf prikazuje, kako se lahko deleži manipulirajo, na smešen način:

![slab graf 4](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-4.jpg)

Primerjava neprimerljivega je še ena senčna taktika. Obstaja [odlično spletno mesto](https://tylervigen.com/spurious-correlations), ki prikazuje 'lažne korelacije', kot so povezave med stopnjo ločitev v Maineu in porabo margarine. Skupina na Redditu prav tako zbira [grde uporabe](https://www.reddit.com/r/dataisugly/top/?t=all) podatkov.

Pomembno je razumeti, kako lahko oko zlahka zavajajo zavajajoči grafi. Tudi če je namen podatkovnega znanstvenika dober, lahko izbira napačnega tipa grafa, kot je krožni graf z preveč kategorijami, povzroči zavajanje.

## Barva

V zgornjem grafu o 'nasilju z orožjem na Floridi' ste videli, kako lahko barva doda dodatno plast pomena grafom, še posebej tistim, ki niso zasnovani z knjižnicami, kot sta Matplotlib in Seaborn, ki vključujeta različne preverjene barvne palete. Če graf izdelujete ročno, si vzemite čas za študij [teorije barv](https://colormatters.com/color-and-design/basic-color-theory).

> ✅ Zavedajte se, da je pri oblikovanju grafov dostopnost pomemben vidik vizualizacije. Nekateri vaši uporabniki so morda barvno slepi - ali vaš graf dobro deluje za uporabnike z motnjami vida?

Bodite previdni pri izbiri barv za svoj graf, saj lahko barva prenese pomen, ki ga morda ne nameravate. 'Rožnate dame' v zgornjem grafu o 'višini' prenašajo izrazito 'ženski' pomen, ki prispeva k nenavadnosti samega grafa.

Medtem ko se [pomen barv](https://colormatters.com/color-symbolism/the-meanings-of-colors) lahko razlikuje v različnih delih sveta in se spreminja glede na odtenek, splošno gledano vključuje:

| Barva  | Pomen               |
| ------ | ------------------- |
| rdeča  | moč                 |
| modra  | zaupanje, zvestoba  |
| rumena | sreča, previdnost   |
| zelena | ekologija, sreča, zavist |
| vijolična | sreča             |
| oranžna | živahnost          |

Če morate ustvariti graf z lastnimi barvami, poskrbite, da bodo vaši grafi dostopni in da barva, ki jo izberete, ustreza pomenu, ki ga želite prenesti.

## Oblikovanje grafov za berljivost

Grafi niso smiselni, če niso berljivi! Vzemite si trenutek za razmislek o oblikovanju širine in višine grafa, da se dobro prilagodi vašim podatkom. Če je treba prikazati eno spremenljivko (na primer vseh 50 zveznih držav), jih prikažite navpično na Y osi, če je mogoče, da se izognete grafu, ki zahteva horizontalno drsenje.

Označite svoje osi, dodajte legendo, če je potrebno, in ponudite orodja za boljše razumevanje podatkov.

Če so vaši podatki besedilni in obsežni na X osi, lahko besedilo nagnite za boljšo berljivost. [Matplotlib](https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html) ponuja 3D grafiranje, če vaši podatki to podpirajo. S pomočjo `mpl_toolkits.mplot3d` lahko ustvarite napredne vizualizacije podatkov.

![3D grafi](../../../../3-Data-Visualization/13-meaningful-visualizations/images/3d.png)

## Animacija in prikaz 3D grafov

Nekatere najboljše vizualizacije podatkov danes so animirane. Shirley Wu je ustvarila neverjetne vizualizacije z D3, kot so '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', kjer je vsak cvet vizualizacija filma. Drug primer za Guardian je 'bussed out', interaktivna izkušnja, ki združuje vizualizacije z Greensock in D3 ter format članka za prikaz, kako NYC obravnava problem brezdomcev z njihovim prevozom iz mesta.

![prevoz](../../../../3-Data-Visualization/13-meaningful-visualizations/images/busing.png)

> "Bussed Out: Kako Amerika premika svoje brezdomce" iz [Guardiana](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Vizualizacije: Nadieh Bremer & Shirley Wu

Čeprav ta lekcija ni dovolj poglobljena, da bi vas naučila teh močnih knjižnic za vizualizacijo, poskusite D3 v aplikaciji Vue.js z uporabo knjižnice za prikaz vizualizacije knjige "Nevarne zveze" kot animirane socialne mreže.

> "Les Liaisons Dangereuses" je epistolarni roman, predstavljen kot serija pisem. Napisal ga je Choderlos de Laclos leta 1782 in pripoveduje zgodbo o zlobnih, moralno pokvarjenih družbenih manevrih dveh protagonistov francoske aristokracije v poznem 18. stoletju, vikonta de Valmonta in markize de Merteuil. Oba na koncu doživita propad, vendar ne brez povzročanja velike družbene škode. Roman se odvija kot serija pisem, napisanih različnim ljudem v njihovih krogih, bodisi za maščevanje bodisi za povzročanje težav. Ustvarite vizualizacijo teh pisem, da odkrijete glavne akterje zgodbe, vizualno.

Dokončali boste spletno aplikacijo, ki bo prikazala animiran pogled na to socialno mrežo. Uporablja knjižnico, ki je bila ustvarjena za [vizualizacijo mreže](https://github.com/emiliorizzo/vue-d3-network) z uporabo Vue.js in D3. Ko aplikacija deluje, lahko premikate vozlišča po zaslonu, da premešate podatke.

![zveze](../../../../3-Data-Visualization/13-meaningful-visualizations/images/liaisons.png)

## Projekt: Ustvarite graf za prikaz mreže z D3.js

> Ta mapa lekcije vključuje mapo `solution`, kjer lahko najdete dokončan projekt za referenco.

1. Sledite navodilom v datoteki README.md v korenski mapi začetnega projekta. Pred namestitvijo odvisnosti projekta poskrbite, da imate na računalniku nameščen NPM in Node.js.

2. Odprite mapo `starter/src`. V njej boste našli mapo `assets`, kjer je .json datoteka z vsemi pismi iz romana, oštevilčenimi, z oznako 'to' in 'from'.

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

Zaženite aplikacijo iz terminala (npm run serve) in uživajte v vizualizaciji!

## 🚀 Izziv

Raziskujte internet in odkrijte zavajajoče vizualizacije. Kako avtor zavaja uporabnika in ali je to namerno? Poskusite popraviti vizualizacije, da pokažete, kako bi morale izgledati.

## [Po-lekcijski kviz](https://ff-quizzes.netlify.app/en/ds/)

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
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.