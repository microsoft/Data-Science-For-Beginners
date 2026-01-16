<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a33c5d4b4156a2b41788d8720b6f724c",
  "translation_date": "2025-08-30T18:48:10+00:00",
  "source_file": "3-Data-Visualization/R/12-visualization-relationships/README.md",
  "language_code": "sl"
}
-->
# Vizualizacija odnosov: Vse o medu 🍯

|![ Sketchnote avtorja [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Vizualizacija odnosov - _Sketchnote avtorja [@nitya](https://twitter.com/nitya)_ |

Nadaljujmo z naravoslovnim fokusom naše raziskave in odkrijmo zanimive vizualizacije, ki prikazujejo odnose med različnimi vrstami medu, na podlagi podatkov, pridobljenih iz [Ministrstva za kmetijstvo Združenih držav Amerike](https://www.nass.usda.gov/About_NASS/index.php).

Ta podatkovna zbirka, ki vsebuje približno 600 elementov, prikazuje proizvodnjo medu v številnih zveznih državah ZDA. Na primer, lahko si ogledate število kolonij, donos na kolonijo, skupno proizvodnjo, zaloge, ceno na funt in vrednost proizvedenega medu v določeni državi od leta 1998 do 2012, pri čemer je ena vrstica na leto za vsako državo.

Zanimivo bo vizualizirati odnos med letno proizvodnjo določene države in, na primer, ceno medu v tej državi. Alternativno bi lahko vizualizirali odnos med donosom medu na kolonijo v različnih državah. To časovno obdobje zajema uničujočo 'CCD' ali 'Colony Collapse Disorder', ki je bila prvič opažena leta 2006 (http://npic.orst.edu/envir/ccd.html), zato je to ganljiva podatkovna zbirka za preučevanje. 🐝

## [Predhodni kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

V tej lekciji lahko uporabite ggplot2, ki ste ga že uporabljali, kot odlično knjižnico za vizualizacijo odnosov med spremenljivkami. Še posebej zanimiva je uporaba funkcij ggplot2 `geom_point` in `qplot`, ki omogočata razpršene grafe in črtne grafe za hitro vizualizacijo '[statističnih odnosov](https://ggplot2.tidyverse.org/)', kar podatkovnemu znanstveniku omogoča boljše razumevanje, kako se spremenljivke med seboj povezujejo.

## Razpršeni grafi

Uporabite razpršeni graf za prikaz, kako se je cena medu razvijala iz leta v leto po posameznih državah. ggplot2, z uporabo `ggplot` in `geom_point`, priročno združi podatke držav in prikaže točke za tako kategorijske kot numerične podatke.

Začnimo z uvozom podatkov in knjižnice Seaborn:

```r
honey=read.csv('../../data/honey.csv')
head(honey)
```
Opazite, da ima podatkovna zbirka medu več zanimivih stolpcev, vključno z letom in ceno na funt. Raziščimo te podatke, razvrščene po zveznih državah ZDA:

| država | št_kolonij | donos_na_kolonijo | skupna_proizvodnja | zaloge   | cena_na_funt | vrednost_proizvodnje | leto |
| ------ | ---------- | ----------------- | ------------------ | -------- | ------------ | -------------------- | ---- |
| AL     | 16000      | 71               | 1136000            | 159000   | 0.72         | 818000               | 1998 |
| AZ     | 55000      | 60               | 3300000            | 1485000  | 0.64         | 2112000              | 1998 |
| AR     | 53000      | 65               | 3445000            | 1688000  | 0.59         | 2033000              | 1998 |
| CA     | 450000     | 83               | 37350000           | 12326000 | 0.62         | 23157000             | 1998 |
| CO     | 27000      | 72               | 1944000            | 1594000  | 0.7          | 1361000              | 1998 |
| FL     | 230000     | 98               | 22540000           | 4508000  | 0.64         | 14426000             | 1998 |

Ustvarite osnovni razpršeni graf za prikaz odnosa med ceno na funt medu in zvezno državo, iz katere med izvira. Os y naj bo dovolj visok, da prikaže vse države:

```r
library(ggplot2)
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(colour = "blue")
```
![razpršeni graf 1](../../../../../translated_images/sl/scatter1.86b8900674d88b26dd3353a83fe604e9ab3722c4680cc40ee9beb452ff02cdea.png)

Zdaj prikažite iste podatke z barvno shemo medu, da pokažete, kako se cena spreminja skozi leta. To lahko storite z dodajanjem parametra 'scale_color_gradientn', ki prikazuje spremembe iz leta v leto:

> ✅ Več o [scale_color_gradientn](https://www.rdocumentation.org/packages/ggplot2/versions/0.9.1/topics/scale_colour_gradientn) - preizkusite čudovito mavrično barvno shemo!

```r
ggplot(honey, aes(x = priceperlb, y = state, color=year)) +
  geom_point()+scale_color_gradientn(colours = colorspace::heat_hcl(7))
```
![razpršeni graf 2](../../../../../translated_images/sl/scatter2.4d1cbc693bad20e2b563888747eb6bdf65b73ce449d903f7cd4068a78502dcff.png)

S to spremembo barvne sheme lahko vidite, da je očitno močan napredek skozi leta glede cene medu na funt. Če pogledate vzorec podatkov za preverjanje (izberite določeno državo, na primer Arizono), lahko opazite vzorec naraščanja cen iz leta v leto, z nekaj izjemami:

| država | št_kolonij | donos_na_kolonijo | skupna_proizvodnja | zaloge  | cena_na_funt | vrednost_proizvodnje | leto |
| ------ | ---------- | ----------------- | ------------------ | ------- | ------------ | -------------------- | ---- |
| AZ     | 55000      | 60               | 3300000            | 1485000 | 0.64         | 2112000              | 1998 |
| AZ     | 52000      | 62               | 3224000            | 1548000 | 0.62         | 1999000              | 1999 |
| AZ     | 40000      | 59               | 2360000            | 1322000 | 0.73         | 1723000              | 2000 |
| AZ     | 43000      | 59               | 2537000            | 1142000 | 0.72         | 1827000              | 2001 |
| AZ     | 38000      | 63               | 2394000            | 1197000 | 1.08         | 2586000              | 2002 |
| AZ     | 35000      | 72               | 2520000            | 983000  | 1.34         | 3377000              | 2003 |
| AZ     | 32000      | 55               | 1760000            | 774000  | 1.11         | 1954000              | 2004 |
| AZ     | 36000      | 50               | 1800000            | 720000  | 1.04         | 1872000              | 2005 |
| AZ     | 30000      | 65               | 1950000            | 839000  | 0.91         | 1775000              | 2006 |
| AZ     | 30000      | 64               | 1920000            | 902000  | 1.26         | 2419000              | 2007 |
| AZ     | 25000      | 64               | 1600000            | 336000  | 1.26         | 2016000              | 2008 |
| AZ     | 20000      | 52               | 1040000            | 562000  | 1.45         | 1508000              | 2009 |
| AZ     | 24000      | 77               | 1848000            | 665000  | 1.52         | 2809000              | 2010 |
| AZ     | 23000      | 53               | 1219000            | 427000  | 1.55         | 1889000              | 2011 |
| AZ     | 22000      | 46               | 1012000            | 253000  | 1.79         | 1811000              | 2012 |

Drug način za vizualizacijo tega napredka je uporaba velikosti namesto barve. Za uporabnike, ki imajo težave z barvnim vidom, je to morda boljša možnost. Uredite svojo vizualizacijo tako, da pokažete povečanje cene z večanjem obsega točk:

```r
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(aes(size = year),colour = "blue") +
  scale_size_continuous(range = c(0.25, 3))
```
Vidite lahko, da se velikost točk postopoma povečuje.

![razpršeni graf 3](../../../../../translated_images/sl/scatter3.722d21e6f20b3ea2e18339bb9b10d75906126715eb7d5fdc88fe74dcb6d7066a.png)

Je to preprost primer ponudbe in povpraševanja? Zaradi dejavnikov, kot so podnebne spremembe in propad kolonij, je na voljo manj medu za nakup iz leta v leto, zato se cena povečuje?

Da bi odkrili korelacijo med nekaterimi spremenljivkami v tej podatkovni zbirki, raziščimo nekaj črtnih grafov.

## Črtni grafi

Vprašanje: Ali je jasno vidno naraščanje cene medu na funt iz leta v leto? To lahko najlažje odkrijete z ustvarjanjem enega samega črtnega grafa:

```r
qplot(honey$year,honey$priceperlb, geom='smooth', span =0.5, xlab = "year",ylab = "priceperlb")
```
Odgovor: Da, z nekaj izjemami okoli leta 2003:

![črtni graf 1](../../../../../translated_images/sl/line1.299b576fbb2a59e60a59e7130030f59836891f90302be084e4e8d14da0562e2a.png)

Vprašanje: No, ali lahko leta 2003 opazimo tudi porast zaloge medu? Kaj pa, če pogledate skupno proizvodnjo iz leta v leto?

```python
qplot(honey$year,honey$totalprod, geom='smooth', span =0.5, xlab = "year",ylab = "totalprod")
```

![črtni graf 2](../../../../../translated_images/sl/line2.3b18fcda7176ceba5b6689eaaabb817d49c965e986f11cac1ae3f424030c34d8.png)

Odgovor: Ne ravno. Če pogledate skupno proizvodnjo, se zdi, da se je v tem letu dejansko povečala, čeprav na splošno količina proizvedenega medu v teh letih upada.

Vprašanje: V tem primeru, kaj bi lahko povzročilo porast cene medu okoli leta 2003?

Da bi to odkrili, lahko raziščete mrežo faset.

## Mreže faset

Mreže faset vzamejo en vidik vaše podatkovne zbirke (v našem primeru lahko izberete 'leto', da se izognete prevelikemu številu faset). Seaborn nato ustvari graf za vsako od teh faset izbranih x in y koordinat za lažjo vizualno primerjavo. Ali leto 2003 izstopa v tej vrsti primerjave?

Ustvarite mrežo faset z uporabo `facet_wrap`, kot je priporočeno v [dokumentaciji ggplot2](https://ggplot2.tidyverse.org/reference/facet_wrap.html).

```r
ggplot(honey, aes(x=yieldpercol, y = numcol,group = 1)) + 
  geom_line() + facet_wrap(vars(year))
```
V tej vizualizaciji lahko primerjate donos na kolonijo in število kolonij iz leta v leto, drug ob drugem, z nastavitvijo wrap na 3 za stolpce:

![mreža faset](../../../../../translated_images/sl/facet.491ad90d61c2a7cc69b50c929f80786c749e38217ccedbf1e22ed8909b65987c.png)

Za to podatkovno zbirko nič posebej ne izstopa glede števila kolonij in njihovega donosa iz leta v leto ter med državami. Ali obstaja drugačen način za iskanje korelacije med tema dvema spremenljivkama?

## Dvovrstni grafi

Poskusite večvrstni graf z nadgrajevanjem dveh črtnih grafov enega na drugega, z uporabo funkcij `par` in `plot` v R. Grafirali bomo leto na osi x in prikazali dve osi y. Prikazali bomo donos na kolonijo in število kolonij, nadgrajeno:

```r
par(mar = c(5, 4, 4, 4) + 0.3)              
plot(honey$year, honey$numcol, pch = 16, col = 2,type="l")              
par(new = TRUE)                             
plot(honey$year, honey$yieldpercol, pch = 17, col = 3,              
     axes = FALSE, xlab = "", ylab = "",type="l")
axis(side = 4, at = pretty(range(y2)))      
mtext("colony yield", side = 4, line = 3)   
```
![nadgrajeni grafi](../../../../../translated_images/sl/dual-line.fc4665f360a54018d7df9bc6abcc26460112e17dcbda18d3b9ae6109b32b36c3.png)

Čeprav nič ne izstopa okoli leta 2003, nam to omogoča, da zaključimo to lekcijo na nekoliko bolj veseli noti: čeprav je skupno število kolonij v upadu, se število kolonij stabilizira, tudi če njihov donos na kolonijo upada.

Naprej, čebele, naprej!

🐝❤️
## 🚀 Izziv

V tej lekciji ste se naučili nekaj več o drugih uporabah razpršenih grafov in mrež faset, vključno z mrežami faset. Izzovite se in ustvarite mrežo faset z uporabo druge podatkovne zbirke, morda tiste, ki ste jo uporabili pred temi lekcijami. Opazujte, kako dolgo traja njihova izdelava in kako morate biti previdni glede števila faset, ki jih želite narisati s temi tehnikami.
## [Naknadni kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## Pregled in samostojno učenje

Črtni grafi so lahko preprosti ali precej kompleksni. Malo preberite v [dokumentaciji ggplot2](https://ggplot2.tidyverse.org/reference/geom_path.html#:~:text=geom_line()%20connects%20them%20in,which%20cases%20are%20connected%20together) o različnih načinih, kako jih lahko zgradite. Poskusite izboljšati črtne grafe, ki ste jih zgradili v tej lekciji, z drugimi metodami, navedenimi v dokumentaciji.
## Naloga

[Potopite se v čebelnjak](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.