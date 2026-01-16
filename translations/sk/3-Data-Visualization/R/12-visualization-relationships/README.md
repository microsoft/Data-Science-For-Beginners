<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a33c5d4b4156a2b41788d8720b6f724c",
  "translation_date": "2025-08-26T17:04:34+00:00",
  "source_file": "3-Data-Visualization/R/12-visualization-relationships/README.md",
  "language_code": "sk"
}
-->
# Vizualizácia vzťahov: Všetko o mede 🍯

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Vizualizácia vzťahov - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

Pokračujúc v prírodnom zameraní nášho výskumu, poďme objaviť zaujímavé vizualizácie, ktoré ukazujú vzťahy medzi rôznymi druhmi medu, podľa datasetu odvodeného od [Ministerstva poľnohospodárstva Spojených štátov](https://www.nass.usda.gov/About_NASS/index.php). 

Tento dataset obsahuje približne 600 položiek a zobrazuje produkciu medu v mnohých štátoch USA. Napríklad môžete preskúmať počet kolónií, výnos na kolóniu, celkovú produkciu, zásoby, cenu za libru a hodnotu vyprodukovaného medu v danom štáte od roku 1998 do 2012, pričom každý riadok predstavuje jeden rok pre každý štát. 

Bude zaujímavé vizualizovať vzťah medzi produkciou v danom štáte za rok a napríklad cenou medu v tom istom štáte. Alternatívne môžete vizualizovať vzťah medzi výnosom medu na kolóniu v jednotlivých štátoch. Toto obdobie zahŕňa ničivý fenomén 'CCD' alebo 'Colony Collapse Disorder', ktorý bol prvýkrát zaznamenaný v roku 2006 (http://npic.orst.edu/envir/ccd.html), takže ide o dojímavý dataset na štúdium. 🐝

## [Kvíz pred prednáškou](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

V tejto lekcii môžete použiť ggplot2, ktorý ste už predtým používali, ako výbornú knižnicu na vizualizáciu vzťahov medzi premennými. Obzvlášť zaujímavé je použitie funkcií `geom_point` a `qplot` z ggplot2, ktoré umožňujú rýchlo vytvárať bodové a čiarové grafy na vizualizáciu '[štatistických vzťahov](https://ggplot2.tidyverse.org/)', čo umožňuje dátovým vedcom lepšie pochopiť, ako sa premenné navzájom ovplyvňujú.

## Bodové grafy

Použite bodový graf na zobrazenie, ako sa cena medu vyvíjala rok po roku v jednotlivých štátoch. ggplot2, pomocou `ggplot` a `geom_point`, pohodlne zoskupuje údaje podľa štátov a zobrazuje dátové body pre kategorizované aj číselné údaje. 

Začnime importovaním dát a knižnice Seaborn:

```r
honey=read.csv('../../data/honey.csv')
head(honey)
```
Všimnete si, že údaje o mede obsahujú niekoľko zaujímavých stĺpcov, vrátane roku a ceny za libru. Preskúmajme tieto údaje, zoskupené podľa štátov USA:

| štát | početkolónií | výnosnakolóniu | celkováprodukcia | zásoby   | cenazalibru | hodnotaprodukcie | rok |
| ----- | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL    | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ    | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR    | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA    | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO    | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |
| FL    | 230000 | 98          |22540000   | 4508000  | 0.64       | 14426000  | 1998 |

Vytvorte základný bodový graf na zobrazenie vzťahu medzi cenou za libru medu a štátom jeho pôvodu. Nastavte os `y` dostatočne vysokú, aby zobrazila všetky štáty:

```r
library(ggplot2)
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(colour = "blue")
```
![bodový graf 1](../../../../../translated_images/sk/scatter1.86b8900674d88b26dd3353a83fe604e9ab3722c4680cc40ee9beb452ff02cdea.png)

Teraz zobrazte tie isté údaje s farebnou schémou medu, aby ste ukázali, ako sa cena vyvíja v priebehu rokov. Môžete to urobiť pridaním parametra 'scale_color_gradientn', ktorý ukazuje zmenu rok po roku:

> ✅ Viac sa dozviete o [scale_color_gradientn](https://www.rdocumentation.org/packages/ggplot2/versions/0.9.1/topics/scale_colour_gradientn) - vyskúšajte krásnu dúhovú farebnú schému!

```r
ggplot(honey, aes(x = priceperlb, y = state, color=year)) +
  geom_point()+scale_color_gradientn(colours = colorspace::heat_hcl(7))
```
![bodový graf 2](../../../../../translated_images/sk/scatter2.4d1cbc693bad20e2b563888747eb6bdf65b73ce449d903f7cd4068a78502dcff.png)

S touto zmenou farebnej schémy môžete vidieť, že v priebehu rokov existuje zjavný silný nárast ceny za libru medu. Ak si overíte vzorku údajov (napríklad pre štát Arizona), môžete vidieť vzor zvyšovania cien rok po roku, s niekoľkými výnimkami:

| štát | početkolónií | výnosnakolóniu | celkováprodukcia | zásoby  | cenazalibru | hodnotaprodukcie | rok |
| ----- | ------ | ----------- | --------- | ------- | ---------- | --------- | ---- |
| AZ    | 55000  | 60          | 3300000   | 1485000 | 0.64       | 2112000   | 1998 |
| AZ    | 52000  | 62          | 3224000   | 1548000 | 0.62       | 1999000   | 1999 |
| AZ    | 40000  | 59          | 2360000   | 1322000 | 0.73       | 1723000   | 2000 |
| AZ    | 43000  | 59          | 2537000   | 1142000 | 0.72       | 1827000   | 2001 |
| AZ    | 38000  | 63          | 2394000   | 1197000 | 1.08       | 2586000   | 2002 |
| AZ    | 35000  | 72          | 2520000   | 983000  | 1.34       | 3377000   | 2003 |
| AZ    | 32000  | 55          | 1760000   | 774000  | 1.11       | 1954000   | 2004 |
| AZ    | 36000  | 50          | 1800000   | 720000  | 1.04       | 1872000   | 2005 |
| AZ    | 30000  | 65          | 1950000   | 839000  | 0.91       | 1775000   | 2006 |
| AZ    | 30000  | 64          | 1920000   | 902000  | 1.26       | 2419000   | 2007 |
| AZ    | 25000  | 64          | 1600000   | 336000  | 1.26       | 2016000   | 2008 |
| AZ    | 20000  | 52          | 1040000   | 562000  | 1.45       | 1508000   | 2009 |
| AZ    | 24000  | 77          | 1848000   | 665000  | 1.52       | 2809000   | 2010 |
| AZ    | 23000  | 53          | 1219000   | 427000  | 1.55       | 1889000   | 2011 |
| AZ    | 22000  | 46          | 1012000   | 253000  | 1.79       | 1811000   | 2012 |

Ďalším spôsobom, ako vizualizovať tento vývoj, je použiť veľkosť namiesto farby. Pre používateľov s poruchami farebného videnia by to mohla byť lepšia možnosť. Upravte svoju vizualizáciu tak, aby nárast ceny bol zobrazený zväčšením obvodu bodov:

```r
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(aes(size = year),colour = "blue") +
  scale_size_continuous(range = c(0.25, 3))
```
Vidíte, že veľkosť bodov sa postupne zväčšuje.

![bodový graf 3](../../../../../translated_images/sk/scatter3.722d21e6f20b3ea2e18339bb9b10d75906126715eb7d5fdc88fe74dcb6d7066a.png)

Je to jednoduchý prípad ponuky a dopytu? Kvôli faktorom, ako je zmena klímy a kolaps kolónií, je k dispozícii menej medu na predaj rok po roku, a preto cena stúpa?

Aby sme objavili koreláciu medzi niektorými premennými v tomto datasete, poďme preskúmať niektoré čiarové grafy.

## Čiarové grafy

Otázka: Existuje jasný nárast ceny medu za libru rok po roku? Najjednoduchšie to zistíte vytvorením jedného čiarového grafu:

```r
qplot(honey$year,honey$priceperlb, geom='smooth', span =0.5, xlab = "year",ylab = "priceperlb")
```
Odpoveď: Áno, s niektorými výnimkami okolo roku 2003:

![čiarový graf 1](../../../../../translated_images/sk/line1.299b576fbb2a59e60a59e7130030f59836891f90302be084e4e8d14da0562e2a.png)

Otázka: No, v roku 2003 môžeme tiež vidieť nárast v zásobách medu? Čo ak sa pozriete na celkovú produkciu rok po roku?

```python
qplot(honey$year,honey$totalprod, geom='smooth', span =0.5, xlab = "year",ylab = "totalprod")
```

![čiarový graf 2](../../../../../translated_images/sk/line2.3b18fcda7176ceba5b6689eaaabb817d49c965e986f11cac1ae3f424030c34d8.png)

Odpoveď: Nie celkom. Ak sa pozriete na celkovú produkciu, zdá sa, že v tomto konkrétnom roku skutočne vzrástla, aj keď všeobecne produkcia medu v týchto rokoch klesá.

Otázka: V tom prípade, čo mohlo spôsobiť ten nárast ceny medu okolo roku 2003? 

Aby sme to zistili, môžeme preskúmať mriežku s viacerými grafmi.

## Mriežky s viacerými grafmi

Mriežky s viacerými grafmi (facet grids) zoberú jednu vlastnosť vášho datasetu (v našom prípade môžete zvoliť 'rok', aby sa nevytvorilo príliš veľa grafov). Seaborn potom vytvorí graf pre každý z týchto aspektov na zvolených osiach x a y, čo umožňuje jednoduchšie vizuálne porovnanie. Vyniká rok 2003 v tomto type porovnania?

Vytvorte mriežku s viacerými grafmi pomocou `facet_wrap`, ako odporúča [dokumentácia ggplot2](https://ggplot2.tidyverse.org/reference/facet_wrap.html). 

```r
ggplot(honey, aes(x=yieldpercol, y = numcol,group = 1)) + 
  geom_line() + facet_wrap(vars(year))
```
V tejto vizualizácii môžete porovnať výnos na kolóniu a počet kolónií rok po roku, vedľa seba, s nastavením wrap na 3 pre stĺpce:

![mriežka s viacerými grafmi](../../../../../translated_images/sk/facet.491ad90d61c2a7cc69b50c929f80786c749e38217ccedbf1e22ed8909b65987c.png)

Pre tento dataset nič konkrétne nevyniká, pokiaľ ide o počet kolónií a ich výnos rok po roku a štát po štáte. Existuje iný spôsob, ako nájsť koreláciu medzi týmito dvoma premennými?

## Dvojité čiarové grafy

Vyskúšajte viacnásobný čiarový graf prekrytím dvoch čiarových grafov na seba, pomocou funkcií `par` a `plot` v R. Budeme zobrazovať rok na osi x a dve osi y. Zobrazte výnos na kolóniu a počet kolónií, prekryté:

```r
par(mar = c(5, 4, 4, 4) + 0.3)              
plot(honey$year, honey$numcol, pch = 16, col = 2,type="l")              
par(new = TRUE)                             
plot(honey$year, honey$yieldpercol, pch = 17, col = 3,              
     axes = FALSE, xlab = "", ylab = "",type="l")
axis(side = 4, at = pretty(range(y2)))      
mtext("colony yield", side = 4, line = 3)   
```
![prekryté grafy](../../../../../translated_images/sk/dual-line.fc4665f360a54018d7df9bc6abcc26460112e17dcbda18d3b9ae6109b32b36c3.png)

Aj keď nič výrazné nevyniká okolo roku 2003, umožňuje nám to ukončiť túto lekciu na trochu pozitívnejšiu nôtu: aj keď celkový počet kolónií klesá, počet kolónií sa stabilizuje, aj keď ich výnos na kolóniu klesá.

Do toho, včely, do toho!

🐝❤️
## 🚀 Výzva

V tejto lekcii ste sa dozvedeli viac o ďalších využitiach bodových grafov a mriežok s viacerými grafmi. Skúste si vytvoriť mriežku s viacerými grafmi pomocou iného datasetu, možno takého, ktorý ste použili v predchádzajúcich lekciách. Všimnite si, ako dlho trvá ich vytvorenie a ako musíte byť opatrní pri počte grafov, ktoré potrebujete nakresliť pomocou týchto techník.
## [Kvíz po prednáške](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## Prehľad a samoštúdium

Čiarové grafy môžu byť jednoduché alebo pomerne zložité. Prečítajte si niečo o rôznych spôsoboch, ako ich môžete vytvoriť, v [dokumentácii ggplot2](https://ggplot2.tidyverse.org/reference/geom_path.html#:~:text=geom_line()%20connects%20them%20in,which%20cases%20are%20connected%20together). Skúste vylepšiť čiarové grafy, ktoré ste vytvorili v tejto lekcii, pomocou iných metód uvedených v dokumentácii.
## Zadanie

[Ponorte sa do úľa](assignment.md)

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.