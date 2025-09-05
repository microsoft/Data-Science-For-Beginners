<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1228edf3572afca7d7cdcd938b6b4984",
  "translation_date": "2025-09-05T06:05:51+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "sl"
}
-->
# Definiranje podatkov

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Definiranje podatkov - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Podatki so dejstva, informacije, opazovanja in meritve, ki se uporabljajo za odkrivanje novih spoznanj in podporo pri sprejemanju informiranih odločitev. Podatkovna točka je posamezna enota podatkov znotraj podatkovnega nabora, ki je zbirka podatkovnih točk. Podatkovni nabori so lahko v različnih formatih in strukturah, običajno pa temeljijo na svojem viru oziroma na tem, od kod podatki izvirajo. Na primer, mesečni zaslužek podjetja je lahko v preglednici, medtem ko so podatki o srčnem utripu iz pametne ure lahko v formatu [JSON](https://stackoverflow.com/a/383699). Pogosto se podatkovni znanstveniki ukvarjajo z različnimi vrstami podatkov znotraj podatkovnega nabora.

Ta lekcija se osredotoča na prepoznavanje in razvrščanje podatkov glede na njihove značilnosti in vire.

## [Pred-predavanje kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)

## Kako so podatki opisani

### Surovi podatki
Surovi podatki so podatki, ki prihajajo iz svojega vira v prvotnem stanju in niso bili analizirani ali organizirani. Da bi razumeli, kaj se dogaja s podatkovnim naborom, ga je treba organizirati v format, ki ga lahko razumejo ljudje, pa tudi tehnologija, ki jo lahko uporabijo za nadaljnjo analizo. Struktura podatkovnega nabora opisuje, kako je organiziran, in ga je mogoče razvrstiti kot strukturiran, nestrukturiran ali polstrukturiran. Te vrste struktur se razlikujejo glede na vir, vendar se na koncu uvrščajo v te tri kategorije.

### Kvantitativni podatki
Kvantitativni podatki so numerična opazovanja znotraj podatkovnega nabora, ki jih je mogoče običajno analizirati, meriti in matematično obdelovati. Nekateri primeri kvantitativnih podatkov so: populacija države, višina osebe ali četrtletni zaslužek podjetja. Z dodatno analizo bi lahko kvantitativne podatke uporabili za odkrivanje sezonskih trendov indeksa kakovosti zraka (AQI) ali za oceno verjetnosti prometne konice na običajen delovni dan.

### Kvalitativni podatki
Kvalitativni podatki, znani tudi kot kategorijski podatki, so podatki, ki jih ni mogoče objektivno meriti, kot so opazovanja kvantitativnih podatkov. Na splošno gre za različne oblike subjektivnih podatkov, ki zajemajo kakovost nečesa, kot je izdelek ali proces. Včasih so kvalitativni podatki numerični, vendar jih običajno ne uporabljamo matematično, kot so telefonske številke ali časovni žigi. Nekateri primeri kvalitativnih podatkov so: komentarji na videoposnetke, znamka in model avtomobila ali najljubša barva vaših najbližjih prijateljev. Kvalitativni podatki bi lahko bili uporabljeni za razumevanje, kateri izdelki so najbolj priljubljeni med potrošniki ali za prepoznavanje priljubljenih ključnih besed v življenjepisih za prijave na delovna mesta.

### Strukturirani podatki
Strukturirani podatki so podatki, ki so organizirani v vrstice in stolpce, kjer ima vsaka vrstica enak nabor stolpcev. Stolpci predstavljajo vrednost določenega tipa in so identificirani z imenom, ki opisuje, kaj vrednost predstavlja, medtem ko vrstice vsebujejo dejanske vrednosti. Stolpci pogosto vsebujejo specifičen nabor pravil ali omejitev glede vrednosti, da zagotovijo, da vrednosti natančno predstavljajo stolpec. Na primer, si predstavljajte preglednico strank, kjer mora vsaka vrstica imeti telefonsko številko, telefonske številke pa ne smejo vsebovati abecednih znakov. Na stolpec s telefonskimi številkami so lahko uporabljena pravila, da nikoli ni prazen in vsebuje le številke.

Prednost strukturiranih podatkov je, da jih je mogoče organizirati na način, ki omogoča povezovanje z drugimi strukturiranimi podatki. Vendar pa lahko zaradi tega, ker so podatki zasnovani tako, da so organizirani na določen način, spremembe celotne strukture zahtevajo veliko truda. Na primer, dodajanje stolpca z e-poštnimi naslovi v preglednico strank, ki ne sme biti prazen, pomeni, da boste morali ugotoviti, kako dodati te vrednosti obstoječim vrsticam strank v podatkovnem naboru.

Primeri strukturiranih podatkov: preglednice, relacijske baze podatkov, telefonske številke, bančni izpiski.

### Nestrukturirani podatki
Nestrukturirani podatki običajno ne morejo biti kategorizirani v vrstice ali stolpce in ne vsebujejo formata ali niza pravil, ki bi jih morali upoštevati. Ker imajo nestrukturirani podatki manj omejitev glede svoje strukture, je lažje dodajati nove informacije v primerjavi s strukturiranim podatkovnim naborom. Če senzor, ki zajema podatke o barometričnem tlaku vsakih 2 minuti, prejme posodobitev, ki mu omogoča merjenje in beleženje temperature, ni treba spreminjati obstoječih podatkov, če so nestrukturirani. Vendar pa lahko to podaljša čas analize ali preiskovanja takšnih podatkov. Na primer, znanstvenik, ki želi ugotoviti povprečno temperaturo prejšnjega meseca iz podatkov senzorja, odkrije, da je senzor v nekaterih svojih zapisih zabeležil "e", da bi označil, da je bil pokvarjen, namesto običajne številke, kar pomeni, da so podatki nepopolni.

Primeri nestrukturiranih podatkov: besedilne datoteke, besedilna sporočila, video datoteke.

### Polstrukturirani podatki
Polstrukturirani podatki imajo značilnosti, zaradi katerih so kombinacija strukturiranih in nestrukturiranih podatkov. Običajno ne ustrezajo formatu vrstic in stolpcev, vendar so organizirani na način, ki se šteje za strukturiran, in lahko sledijo določenemu formatu ali nizu pravil. Struktura se razlikuje med viri, od dobro definirane hierarhije do nečesa bolj prilagodljivega, kar omogoča enostavno vključevanje novih informacij. Metapodatki so kazalniki, ki pomagajo določiti, kako so podatki organizirani in shranjeni, ter imajo različna imena glede na vrsto podatkov. Nekatera pogosta imena za metapodatke so oznake, elementi, entitete in atributi. Na primer, tipično e-poštno sporočilo bo imelo zadevo, telo in nabor prejemnikov ter ga je mogoče organizirati glede na to, kdo ali kdaj je bilo poslano.

Primeri polstrukturiranih podatkov: HTML, datoteke CSV, JavaScript Object Notation (JSON).

## Viri podatkov

Vir podatkov je začetna lokacija, kjer so bili podatki ustvarjeni ali kjer "živijo", in se razlikuje glede na to, kako in kdaj so bili zbrani. Podatki, ki jih ustvarijo uporabniki, so znani kot primarni podatki, medtem ko sekundarni podatki prihajajo iz vira, ki je zbral podatke za splošno uporabo. Na primer, skupina znanstvenikov, ki zbira opazovanja v deževnem gozdu, bi se štela za primarni vir, če pa se odločijo, da jih delijo z drugimi znanstveniki, bi se za tiste, ki jih uporabljajo, štelo za sekundarni vir.

Baze podatkov so pogost vir in se zanašajo na sistem za upravljanje baz podatkov, da gostijo in vzdržujejo podatke, kjer uporabniki uporabljajo ukaze, imenovane poizvedbe, za raziskovanje podatkov. Datoteke kot viri podatkov so lahko zvočne, slikovne in video datoteke ter preglednice, kot je Excel. Internetni viri so pogosta lokacija za gostovanje podatkov, kjer je mogoče najti baze podatkov in datoteke. Programski vmesniki aplikacij, znani tudi kot API-ji, omogočajo programerjem ustvarjanje načinov za deljenje podatkov z zunanjimi uporabniki prek interneta, medtem ko proces spletnega strganja pridobiva podatke s spletne strani. [Lekcije o delu s podatki](../../../../../../../../../2-Working-With-Data) se osredotočajo na to, kako uporabljati različne vire podatkov.

## Zaključek

V tej lekciji smo se naučili:

- Kaj so podatki
- Kako so podatki opisani
- Kako so podatki razvrščeni in kategorizirani
- Kje je mogoče najti podatke

## 🚀 Izziv

Kaggle je odličen vir odprtih podatkovnih naborov. Uporabite [orodje za iskanje podatkovnih naborov](https://www.kaggle.com/datasets), da najdete nekaj zanimivih podatkovnih naborov in razvrstite 3-5 podatkovnih naborov po teh kriterijih:

- Ali so podatki kvantitativni ali kvalitativni?
- Ali so podatki strukturirani, nestrukturirani ali polstrukturirani?

## [Kviz po predavanju](https://ff-quizzes.netlify.app/en/ds/)

## Pregled in samostojno učenje

- Enota Microsoft Learn z naslovom [Razvrščanje vaših podatkov](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data) vsebuje podroben pregled strukturiranih, polstrukturiranih in nestrukturiranih podatkov.

## Naloga

[Razvrščanje podatkovnih naborov](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni prevod s strani človeka. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.