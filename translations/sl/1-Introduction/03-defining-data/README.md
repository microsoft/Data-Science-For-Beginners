<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "12339119c0165da569a93ddba05f9339",
  "translation_date": "2025-09-05T19:45:08+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "sl"
}
-->
# Definiranje podatkov

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definiranje podatkov - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Podatki so dejstva, informacije, opazovanja in meritve, ki se uporabljajo za odkrivanje novih spoznanj in podporo pri sprejemanju informiranih odločitev. Podatek je posamezna enota podatkov znotraj nabora podatkov, ki je zbirka podatkovnih točk. Nabori podatkov so lahko v različnih formatih in strukturah, običajno pa temeljijo na svojem viru oziroma na tem, od kod podatki izvirajo. Na primer, mesečni zaslužek podjetja je lahko v preglednici, medtem ko so podatki o srčnem utripu iz pametne ure lahko v formatu [JSON](https://stackoverflow.com/a/383699). Pogosto se podatkovni znanstveniki ukvarjajo z različnimi vrstami podatkov znotraj nabora podatkov.

Ta lekcija se osredotoča na prepoznavanje in razvrščanje podatkov glede na njihove značilnosti in vire.

## [Pred-predavanjem kviz](https://ff-quizzes.netlify.app/en/ds/quiz/4)

## Kako so podatki opisani

### Surovi podatki
Surovi podatki so podatki, ki prihajajo iz svojega vira v začetnem stanju in niso bili analizirani ali organizirani. Da bi razumeli, kaj se dogaja z naborom podatkov, jih je treba organizirati v format, ki ga lahko razumejo ljudje, pa tudi tehnologija, ki jo lahko uporabijo za nadaljnjo analizo. Struktura nabora podatkov opisuje, kako je organiziran, in jo je mogoče razvrstiti kot strukturirano, nestrukturirano ali polstrukturirano. Te vrste struktur se razlikujejo glede na vir, vendar se na koncu uvrščajo v te tri kategorije.

### Kvantitativni podatki
Kvantitativni podatki so numerična opazovanja znotraj nabora podatkov, ki jih je mogoče običajno analizirati, meriti in matematično obdelovati. Nekateri primeri kvantitativnih podatkov so: populacija države, višina osebe ali četrtletni zaslužek podjetja. Z dodatno analizo bi lahko kvantitativni podatki razkrili sezonske trende indeksa kakovosti zraka (AQI) ali ocenili verjetnost prometne konice na običajen delovni dan.

### Kvalitativni podatki
Kvalitativni podatki, znani tudi kot kategorijski podatki, so podatki, ki jih ni mogoče objektivno meriti, kot so opazovanja kvantitativnih podatkov. Na splošno gre za različne oblike subjektivnih podatkov, ki zajemajo kakovost nečesa, na primer izdelka ali procesa. Včasih so kvalitativni podatki numerični, vendar jih običajno ne uporabljamo matematično, kot so telefonske številke ali časovni žigi. Nekateri primeri kvalitativnih podatkov so: komentarji na videoposnetke, znamka in model avtomobila ali najljubša barva vaših najbližjih prijateljev. Kvalitativni podatki bi lahko pomagali razumeti, kateri izdelki so najbolj priljubljeni med potrošniki ali prepoznati priljubljene ključne besede v življenjepisih za prijave na delovna mesta.

### Strukturirani podatki
Strukturirani podatki so podatki, ki so organizirani v vrstice in stolpce, kjer ima vsaka vrstica enak nabor stolpcev. Stolpci predstavljajo vrednost določenega tipa in so označeni z imenom, ki opisuje, kaj vrednost predstavlja, medtem ko vrstice vsebujejo dejanske vrednosti. Stolpci pogosto vsebujejo specifičen nabor pravil ali omejitev za vrednosti, da zagotovijo, da vrednosti natančno predstavljajo stolpec. Na primer, predstavljajte si preglednico strank, kjer mora vsaka vrstica imeti telefonsko številko, telefonske številke pa ne smejo vsebovati abecednih znakov. Na stolpec s telefonskimi številkami bi lahko bila uporabljena pravila, da nikoli ni prazen in vsebuje samo številke.

Prednost strukturiranih podatkov je, da jih je mogoče organizirati na način, ki omogoča povezovanje z drugimi strukturiranimi podatki. Vendar pa lahko zaradi tega, ker so podatki zasnovani tako, da so organizirani na določen način, spremembe celotne strukture zahtevajo veliko truda. Na primer, dodajanje stolpca za e-pošto v preglednico strank, ki ne sme biti prazen, pomeni, da morate ugotoviti, kako boste dodali te vrednosti obstoječim vrsticam strank v naboru podatkov.

Primeri strukturiranih podatkov: preglednice, relacijske baze podatkov, telefonske številke, bančni izpiski.

### Nestrukturirani podatki
Nestrukturirani podatki običajno ne morejo biti kategorizirani v vrstice ali stolpce in ne vsebujejo formata ali niza pravil, ki bi jih morali upoštevati. Ker imajo nestrukturirani podatki manj omejitev glede svoje strukture, je lažje dodajati nove informacije v primerjavi s strukturiranim naborom podatkov. Če senzor, ki zajema podatke o barometričnem tlaku vsakih 2 minuti, prejme posodobitev, ki mu omogoča merjenje in beleženje temperature, ni treba spreminjati obstoječih podatkov, če so nestrukturirani. Vendar pa lahko to oteži analizo ali preiskovanje takšnih podatkov. Na primer, znanstvenik, ki želi ugotoviti povprečno temperaturo prejšnjega meseca iz podatkov senzorja, odkrije, da je senzor v nekaterih svojih zapisih zabeležil "e", da označi, da je bil pokvarjen, namesto običajne številke, kar pomeni, da so podatki nepopolni.

Primeri nestrukturiranih podatkov: besedilne datoteke, besedilna sporočila, video datoteke.

### Polstrukturirani podatki
Polstrukturirani podatki imajo značilnosti, zaradi katerih so kombinacija strukturiranih in nestrukturiranih podatkov. Običajno ne ustrezajo formatu vrstic in stolpcev, vendar so organizirani na način, ki velja za strukturiranega, in lahko sledijo določenemu formatu ali nizu pravil. Struktura se razlikuje glede na vire, od dobro definirane hierarhije do nečesa bolj prilagodljivega, kar omogoča enostavno vključevanje novih informacij. Metapodatki so kazalniki, ki pomagajo določiti, kako so podatki organizirani in shranjeni, ter imajo različna imena glede na vrsto podatkov. Nekatera pogosta imena za metapodatke so oznake, elementi, entitete in atributi. Na primer, tipično e-poštno sporočilo bo imelo zadevo, telo in nabor prejemnikov ter ga je mogoče organizirati glede na to, kdo ali kdaj je bilo poslano.

Primeri polstrukturiranih podatkov: HTML, datoteke CSV, JavaScript Object Notation (JSON).

## Viri podatkov

Vir podatkov je začetna lokacija, kjer so bili podatki ustvarjeni ali kjer "živijo", in se razlikuje glede na to, kako in kdaj so bili zbrani. Podatki, ki jih ustvarijo uporabniki, so znani kot primarni podatki, medtem ko sekundarni podatki prihajajo iz vira, ki je zbral podatke za splošno uporabo. Na primer, skupina znanstvenikov, ki zbira opazovanja v deževnem gozdu, bi veljala za primarne podatke, če pa jih delijo z drugimi znanstveniki, bi ti podatki veljali za sekundarne za tiste, ki jih uporabljajo.

Baze podatkov so pogost vir in se zanašajo na sistem za upravljanje baz podatkov, ki gosti in vzdržuje podatke, kjer uporabniki uporabljajo ukaze, imenovane poizvedbe, za raziskovanje podatkov. Datoteke kot viri podatkov so lahko zvočne, slikovne in video datoteke ter preglednice, kot je Excel. Internetni viri so pogosta lokacija za gostovanje podatkov, kjer je mogoče najti baze podatkov in datoteke. Programski vmesniki aplikacij, znani tudi kot API-ji, omogočajo programerjem ustvarjanje načinov za deljenje podatkov z zunanjimi uporabniki prek interneta, medtem ko proces spletnega strganja pridobiva podatke s spletne strani. [Lekcije o delu s podatki](../../../../../../../../../2-Working-With-Data) se osredotočajo na to, kako uporabljati različne vire podatkov.

## Zaključek

V tej lekciji smo se naučili:

- Kaj so podatki
- Kako so podatki opisani
- Kako so podatki razvrščeni in kategorizirani
- Kje je mogoče najti podatke

## 🚀 Izziv

Kaggle je odličen vir odprtih naborov podatkov. Uporabite [orodje za iskanje naborov podatkov](https://www.kaggle.com/datasets), da najdete nekaj zanimivih naborov podatkov in razvrstite 3-5 naborov podatkov po teh kriterijih:

- Ali so podatki kvantitativni ali kvalitativni?
- Ali so podatki strukturirani, nestrukturirani ali polstrukturirani?

## [Kviz po predavanju](https://ff-quizzes.netlify.app/en/ds/quiz/5)

## Pregled in samostojno učenje

- Enota Microsoft Learn, naslovljena [Razvrščanje vaših podatkov](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data), vsebuje podroben pregled strukturiranih, polstrukturiranih in nestrukturiranih podatkov.

## Naloga

[Razvrščanje naborov podatkov](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.