# Opredelitev podatkov

|![ Sketchnote avtorja [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Opredelitev podatkov - _Sketchnote avtorja [@nitya](https://twitter.com/nitya)_ |

Podatki so dejstva, informacije, opazovanja in meritve, ki se uporabljajo za odkritja in podporo informiranim odločitvam. Podatkovna točka je ena enota podatkov v podatkovnem naboru, ki je zbirka podatkovnih točk. Podatkovni nabori so lahko v različnih formatih in strukturah, običajno pa so odvisni od vira oziroma od kje podatki prihajajo. Na primer, mesečni prihodki podjetja so lahko v preglednici, medtem ko so podatki o srčnem utripu po urah iz pametne ure morda v formatu [JSON](https://stackoverflow.com/a/383699). Pogosto delajo podatkovni znanstveniki z različnimi vrstami podatkov znotraj podatkovnega nabora.

Ta lekcija se osredotoča na prepoznavanje in razvrščanje podatkov glede na njihove značilnosti in vire.

## [Predpredavalni kviz](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Kako so podatki opisani

### Surovi podatki
Surovi podatki so podatki, ki so prišli iz vira v svoji začetni obliki in niso bili analizirani ali organizirani. Da bi razumeli, kaj se dogaja s podatkovnim naborom, jih je treba organizirati v obliko, ki je razumljiva ljudem in tehnologiji, ki jo lahko uporabi za nadaljnjo analizo. Struktura podatkovnega nabora opisuje, kako je organiziran in se lahko uvrsti na strukturiran, nestrukturiran in polstrukturiran. Te vrste struktur se razlikujejo glede na vir, a na koncu se uvrščajo v te tri kategorije.

### Kvantitativni podatki
Kvantitativni podatki so številčna opazovanja znotraj podatkovnega nabora, ki jih je običajno mogoče analizirati, meriti in uporabljati matematično. Nekaj primerov kvantitativnih podatkov so: prebivalstvo države, višina osebe ali četrtletni dobiček podjetja. Z dodatno analizo bi lahko kvantitativne podatke uporabili za odkrivanje sezonskih trendov indeksa kakovosti zraka (AQI) ali ocenjevanje verjetnosti prometnih konic na običajni delovni dan.

### Kvalitativni podatki
Kvalitativni podatki, znani tudi kot kategorijalni podatki, so podatki, ki jih ni mogoče objektivno meriti, kot so opazovanja kvantitativnih podatkov. Običajno gre za različne oblike subjektivnih podatkov, ki zajemajo kakovost nečesa, na primer izdelka ali procesa. Včasih so kvalitativni podatki številčni, vendar jih običajno ne uporabljamo matematično, kot so telefonske številke ali časovne oznake. Nekaj primerov kvalitativnih podatkov so: komentarji pod videom, znamka in model avtomobila ali najljubša barva vaših najbližjih prijateljev. Kvalitativne podatke bi lahko uporabili za razumevanje, kateri izdelki so potrošnikom najbolj všeč ali za prepoznavanje priljubljenih ključnih besed v življenjepisih.

### Strukturirani podatki
Strukturirani podatki so podatki organizirani v vrsticah in stolpcih, pri čemer ima vsaka vrstica enako množico stolpcev. Stolpci predstavljajo vrednost določenega tipa in so označeni z imenom, ki opisuje, kaj vrednost predstavlja, medtem ko vrstice vsebujejo dejanske vrednosti. Stolpci imajo pogosto določena pravila ali omejitve glede vrednosti, da se zagotovi, da vrednosti natančno predstavljajo stolpec. Na primer, predstavite si preglednico strank, kjer mora imeti vsaka vrstica telefonsko številko, pri čemer telefonske številke nikoli ne vsebujejo črk. Na stolpec s telefonskimi številkami so lahko uporabljena pravila, da nikoli ni prazen in vsebuje samo številke.

Prednost strukturiranih podatkov je v tem, da jih je mogoče organizirati tako, da so povezani z drugimi strukturiranimi podatki. Vendar pa zaradi zasnove strukture podatkov spremembe v njeni celotni strukturi lahko zahtevajo veliko truda. Na primer, dodajanje stolpca z elektronsko pošto v preglednico strank, ki ne sme biti prazna, pomeni, da boste morali ugotoviti, kako dodati te vrednosti v obstoječe vrstice strank v podatkovnem naboru.

Primeri strukturiranih podatkov: preglednice, relacijske baze podatkov, telefonske številke, bančni izpiski

### Nestrukturirani podatki
Nestrukturirani podatki običajno niso razporejeni v vrstice ali stolpce in nimajo formata ali niza pravil, ki jih je treba upoštevati. Ker imajo nestrukturirani podatki manj omejitev glede strukture, je dodajanje novih informacij lažje v primerjavi z strukturiranim podatkovnim naborom. Če senzor, ki beleži podatke o barometričnem tlaku vsaki 2 minuti, prejme posodobitev, ki mu zdaj omogoča merjenje in zapis temperature, ni treba spreminjati obstoječih podatkov, če so nestrukturirani. Vendar pa lahko analiza ali preiskava take vrste podatkov traja dlje. Na primer, znanstvenik, ki želi najti povprečno temperaturo iz prejšnjega meseca s podatki senzorjev, odkrije, da je senzor v nekaterih svojih zabeleženih podatkih zapisal "e" za označitev, da je bil pokvarjen, namesto običajne številke, kar pomeni, da so podatki nepopolni.

Primeri nestrukturiranih podatkov: besedilne datoteke, besedilna sporočila, video datoteke

### Polstrukturirani podatki
Polstrukturirani podatki imajo značilnosti, ki jih naredijo kombinacijo strukturiranih in nestrukturiranih podatkov. Običajno niso oblikovani po vrsticah in stolpcih, so pa organizirani na način, ki velja za strukturiran in lahko sledijo določenemu formatu ali sklopu pravil. Struktura se razlikuje med viri, od dobro definirane hierarhije do nečesa bolj prilagodljivega, kar omogoča enostavno integracijo novih informacij. Metapodatki so kazalci, ki pomagajo ugotoviti, kako so podatki organizirani in shranjeni, ter imajo različna imena, glede na vrsto podatkov. Nekaj pogostih imen za metapodatke so označbe (tags), elementi, entitete in atributi. Na primer, tipično elektronsko sporočilo ima zadevo, telo in nabor prejemnikov ter je lahko organizirano po tem, kdo ali kdaj je bilo poslano.

Primeri polstrukturiranih podatkov: HTML, CSV datoteke, JavaScript Object Notation (JSON)

## Viri podatkov

Vir podatkov je začetna lokacija, kjer so bili podatki ustvarjeni ali kjer "bivajo" in se razlikuje glede na to, kako in kdaj so bili zbrani. Podatki, ki jih ustvarijo njihovi uporabniki, so znani kot primarni podatki, medtem ko sekundarni podatki prihajajo iz vira, ki je zbral podatke za splošno uporabo. Na primer, skupina znanstvenikov, ki zbira opazovanja v deževnem gozdu, bi veljala za primarno, če pa se odločijo te podatke deliti z drugimi znanstveniki, bi ti bili za uporabnike sekundarni.

Baze podatkov so pogost vir in se zanašajo na sistem za upravljanje baz podatkov, ki gosti in vzdržuje podatke, pri čemer uporabniki uporabljajo ukaze, imenovane poizvedbe, za raziskovanje podatkov. Datoteke kot viri podatkov so lahko avdio, slikovne in video datoteke, kot tudi preglednice, npr. Excel. Internetni viri so pogosta lokacija za gostovanje podatkov, kjer lahko najdemo baze podatkov in datoteke. Application programming interfaces, znani tudi kot API-ji, omogočajo programerjem ustvarjanje načinov za deljenje podatkov z zunanjimi uporabniki preko interneta, medtem ko postopek spletnega strganja (web scraping) izvleče podatke s spletne strani. [Lekcije v delu z podatki](../../../../../../../../../2-Working-With-Data) se osredotočajo na uporabo različnih virov podatkov.

## Zaključek

V tej lekciji smo se naučili:

- Kaj so podatki
- Kako so podatki opisani
- Kako so podatki razvrščeni in kategorizirani
- Kje lahko podatke najdemo

## 🚀 Izziv

Kaggle je odličen vir odprtih podatkovnih nizov. Uporabite [orodje za iskanje podatkovnih nizov](https://www.kaggle.com/datasets), da poiščete nekaj zanimivih datasettov in razvrstite 3-5 podatkovnih nizov glede na naslednja merila:

- Ali so podatki kvantitativni ali kvalitativni?
- Ali so podatki strukturirani, nestrukturirani ali polstrukturirani?

## [Popredavalni kviz](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Pregled in samostojno učenje

- Ta Microsoft Learn enota z naslovom [Prepoznajte formate podatkov](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text) ima podrobno razčlenitev strukturiranih, polstrukturiranih in nestrukturiranih podatkov.

## Domača naloga

[Razvrščanje podatkovnih nizov](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->