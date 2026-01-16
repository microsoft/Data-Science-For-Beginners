<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43212cc1ac137b7bb1dcfb37ca06b0f4",
  "translation_date": "2025-10-25T19:10:19+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "sl"
}
-->
# Definiranje podatkovne znanosti

| ![ Sketchnote avtorja [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/01-Definitions.png) |
| :-------------------------------------------------------------------------------------------------------: |
|              Definiranje podatkovne znanosti - _Sketchnote avtorja [@nitya](https://twitter.com/nitya)_               |

---

[![Video o definiranju podatkovne znanosti](../../../../translated_images/sl/video-def-ds.6623ee2392ef1abf6d7faf3fad10a4163642811749da75f44e35a5bb121de15c.png)](https://youtu.be/beZ7Mb_oz9I)

## [Predavanje - kviz](https://ff-quizzes.netlify.app/en/ds/quiz/0)

## Kaj so podatki?
V vsakdanjem življenju smo nenehno obdani s podatki. Besedilo, ki ga trenutno berete, so podatki. Seznam telefonskih številk vaših prijateljev v pametnem telefonu so podatki, prav tako kot trenutni čas, prikazan na vaši uri. Kot ljudje naravno delujemo s podatki, ko štejemo denar ali pišemo pisma prijateljem.

Vendar pa so podatki postali veliko bolj pomembni z nastankom računalnikov. Primarna vloga računalnikov je izvajanje izračunov, vendar za svoje delovanje potrebujejo podatke. Zato moramo razumeti, kako računalniki shranjujejo in obdelujejo podatke.

S pojavom interneta se je vloga računalnikov kot naprav za obdelavo podatkov povečala. Če pomislite, danes računalnike vse bolj uporabljamo za obdelavo in komunikacijo podatkov, namesto za dejanske izračune. Ko pišemo e-pošto prijatelju ali iščemo informacije na internetu, v bistvu ustvarjamo, shranjujemo, prenašamo in obdelujemo podatke.
> Se spomnite, kdaj ste nazadnje uporabili računalnik za dejanski izračun nečesa?

## Kaj je podatkovna znanost?

Na [Wikipediji](https://en.wikipedia.org/wiki/Data_science) je **podatkovna znanost** opredeljena kot *znanstveno področje, ki uporablja znanstvene metode za pridobivanje znanja in vpogledov iz strukturiranih in nestrukturiranih podatkov ter uporablja znanje in uporabne vpoglede iz podatkov na širokem spektru aplikacijskih področij*.

Ta definicija poudarja naslednje pomembne vidike podatkovne znanosti:

* Glavni cilj podatkovne znanosti je **pridobivanje znanja** iz podatkov, z drugimi besedami - **razumevanje** podatkov, iskanje skritih povezav in gradnja **modela**.
* Podatkovna znanost uporablja **znanstvene metode**, kot so verjetnost in statistika. Pravzaprav so nekateri ob uvedbi izraza *podatkovna znanost* trdili, da je to le nov moderen izraz za statistiko. Danes je jasno, da je to področje veliko širše.
* Pridobljeno znanje je treba uporabiti za ustvarjanje **uporabnih vpogledov**, tj. praktičnih vpogledov, ki jih lahko uporabimo v resničnih poslovnih situacijah.
* Moramo biti sposobni delati tako s **strukturiranimi** kot z **nestrukturiranimi** podatki. O različnih vrstah podatkov bomo govorili kasneje v tečaju.
* **Aplikacijsko področje** je pomemben koncept, podatkovni znanstveniki pa pogosto potrebujejo vsaj nekaj stopnje strokovnega znanja na področju problema, na primer: finance, medicina, marketing itd.

> Drug pomemben vidik podatkovne znanosti je, da preučuje, kako je mogoče podatke zbirati, shranjevati in obdelovati z uporabo računalnikov. Medtem ko nam statistika daje matematične temelje, podatkovna znanost uporablja matematične koncepte za dejansko pridobivanje vpogledov iz podatkov.

Eden od načinov (pripisan [Jim Grayu](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) za razumevanje podatkovne znanosti je, da jo obravnavamo kot ločen znanstveni pristop:
* **Empirični**, kjer se zanašamo predvsem na opazovanja in rezultate eksperimentov
* **Teoretični**, kjer novi koncepti izhajajo iz obstoječega znanstvenega znanja
* **Računalniški**, kjer odkrivamo nova načela na podlagi računalniških eksperimentov
* **Na podatkih temelječ**, kjer odkrivamo povezave in vzorce v podatkih  

## Druga sorodna področja

Ker so podatki vseprisotni, je tudi podatkovna znanost široko področje, ki se dotika številnih drugih disciplin.

<dl>
<dt>Baze podatkov</dt>
<dd>
Ključno vprašanje je <b>kako shraniti</b> podatke, tj. kako jih strukturirati na način, ki omogoča hitrejšo obdelavo. Obstajajo različne vrste baz podatkov, ki shranjujejo strukturirane in nestrukturirane podatke, kar <a href="../../2-Working-With-Data/README.md">bomo obravnavali v našem tečaju</a>.
</dd>
<dt>Veliki podatki</dt>
<dd>
Pogosto moramo shranjevati in obdelovati zelo velike količine podatkov z relativno preprosto strukturo. Obstajajo posebni pristopi in orodja za shranjevanje teh podatkov na porazdeljen način na računalniškem grozdu in njihovo učinkovito obdelavo.
</dd>
<dt>Strojno učenje</dt>
<dd>
Eden od načinov za razumevanje podatkov je <b>gradnja modela</b>, ki bo lahko napovedal želeni izid. Razvoj modelov iz podatkov se imenuje <b>strojno učenje</b>. Morda si želite ogledati naš <a href="https://aka.ms/ml-beginners">tečaj Strojno učenje za začetnike</a>, da izveste več o tem.
</dd>
<dt>Umetna inteligenca</dt>
<dd>
Področje strojnega učenja, znano kot umetna inteligenca (UI), se prav tako opira na podatke in vključuje gradnjo zelo kompleksnih modelov, ki posnemajo človeške miselne procese. Metode UI pogosto omogočajo pretvorbo nestrukturiranih podatkov (npr. naravnega jezika) v strukturirane vpoglede. 
</dd>
<dt>Vizualizacija</dt>
<dd>
Ogromne količine podatkov so za človeka nerazumljive, vendar lahko z ustvarjanjem uporabnih vizualizacij teh podatkov bolje razumemo podatke in iz njih izpeljemo zaključke. Zato je pomembno poznati številne načine vizualizacije informacij - nekaj, kar bomo obravnavali v <a href="../../3-Data-Visualization/README.md">3. poglavju</a> našega tečaja. Sorodna področja vključujejo tudi <b>infografiko</b> in splošno <b>interakcijo človek-računalnik</b>. 
</dd>
</dl>

## Vrste podatkov

Kot smo že omenili, so podatki povsod. Samo na pravi način jih moramo zajeti! Koristno je razlikovati med **strukturiranimi** in **nestrukturiranimi** podatki. Prvi so običajno predstavljeni v neki dobro strukturirani obliki, pogosto kot tabela ali več tabel, medtem ko so drugi le zbirka datotek. Včasih lahko govorimo tudi o **polstrukturiranih** podatkih, ki imajo neko vrsto strukture, ki se lahko močno razlikuje.

| Strukturirani                                                              | Polstrukturirani                                                                                 | Nestrukturirani                        |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------- |
| Seznam ljudi z njihovimi telefonskimi številkami                           | Strani Wikipedije s povezavami                                                                   | Besedilo Enciklopedije Britannica      |
| Temperatura v vseh sobah stavbe vsako minuto v zadnjih 20 letih            | Zbirka znanstvenih člankov v formatu JSON z avtorji, datumom objave in povzetkom                 | Datotečni strežnik s korporativnimi dokumenti |
| Podatki o starosti in spolu vseh ljudi, ki vstopajo v stavbo               | Internetne strani                                                                                | Surovi video posnetki iz nadzornih kamer |

## Kje dobiti podatke

Obstaja veliko možnih virov podatkov, zato jih je nemogoče vse našteti! Vendar pa omenimo nekaj tipičnih mest, kjer lahko pridobite podatke:

* **Strukturirani**
  - **Internet stvari** (IoT), vključno s podatki iz različnih senzorjev, kot so temperaturni ali tlačni senzorji, zagotavlja veliko uporabnih podatkov. Na primer, če je poslovna stavba opremljena s senzorji IoT, lahko samodejno nadzorujemo ogrevanje in razsvetljavo, da zmanjšamo stroške.
  - **Ankete**, ki jih prosimo uporabnike, da jih izpolnijo po nakupu ali po obisku spletne strani.
  - **Analiza vedenja** nam lahko na primer pomaga razumeti, kako globoko uporabnik raziskuje spletno stran in kaj je tipičen razlog za njen zapustitev.
* **Nestrukturirani**
  - **Besedila** so lahko bogat vir vpogledov, kot je splošna **ocena sentimenta** ali izločanje ključnih besed in semantičnega pomena.
  - **Slike** ali **video posnetki**. Video posnetek iz nadzorne kamere se lahko uporabi za oceno prometa na cesti in obveščanje ljudi o morebitnih zastojih.
  - **Dnevniki spletnih strežnikov** se lahko uporabijo za razumevanje, katere strani naše spletne strani so najpogosteje obiskane in kako dolgo.
* Polstrukturirani
  - **Grafi družbenih omrežij** so lahko odličen vir podatkov o osebnostih uporabnikov in potencialni učinkovitosti pri širjenju informacij.
  - Ko imamo kup fotografij s zabave, lahko poskusimo izločiti podatke o **skupinski dinamiki** z gradnjo grafa ljudi, ki se fotografirajo skupaj.

Z poznavanjem različnih možnih virov podatkov lahko razmišljate o različnih scenarijih, kjer je mogoče uporabiti tehnike podatkovne znanosti za boljše razumevanje situacije in izboljšanje poslovnih procesov.

## Kaj lahko naredite s podatki

V podatkovni znanosti se osredotočamo na naslednje korake v podatkovni poti:

<dl>
<dt>1) Pridobivanje podatkov</dt>
<dd>
Prvi korak je zbiranje podatkov. Čeprav je v mnogih primerih to lahko preprost postopek, kot je prenos podatkov v bazo podatkov iz spletne aplikacije, včasih potrebujemo posebne tehnike. Na primer, podatki iz IoT senzorjev so lahko preobsežni, zato je dobra praksa uporaba vmesnih točk za medpomnjenje, kot je IoT Hub, za zbiranje vseh podatkov pred nadaljnjo obdelavo.
</dd>
<dt>2) Shranjevanje podatkov</dt>
<dd>
Shranjevanje podatkov je lahko zahtevno, še posebej, če govorimo o velikih podatkih. Pri odločanju, kako shraniti podatke, je smiselno predvideti način, kako jih boste želeli v prihodnosti poizvedovati. Obstaja več načinov za shranjevanje podatkov:
<ul>
<li>Relacijska baza podatkov shranjuje zbirko tabel in uporablja poseben jezik, imenovan SQL, za poizvedovanje po njih. Tabele so običajno organizirane v različne skupine, imenovane sheme. V mnogih primerih moramo podatke pretvoriti iz izvirne oblike, da ustrezajo shemi.</li>
<li><a href="https://en.wikipedia.org/wiki/NoSQL">NoSQL</a> baza podatkov, kot je <a href="https://azure.microsoft.com/services/cosmos-db/?WT.mc_id=academic-77958-bethanycheum">CosmosDB</a>, ne zahteva shem za podatke in omogoča shranjevanje bolj zapletenih podatkov, na primer hierarhičnih JSON dokumentov ali grafov. Vendar pa NoSQL baze podatkov nimajo bogatih možnosti poizvedovanja, kot jih ima SQL, in ne morejo zagotavljati referenčne integritete, tj. pravil o tem, kako so podatki strukturirani v tabelah in urejajo odnose med tabelami.</li>
<li><a href="https://en.wikipedia.org/wiki/Data_lake">Shranjevanje podatkov v jezeru</a> se uporablja za velike zbirke podatkov v surovi, nestrukturirani obliki. Jezera podatkov se pogosto uporabljajo pri velikih podatkih, kjer vsi podatki ne morejo biti shranjeni na enem računalniku in jih je treba shraniti in obdelati z grozdom strežnikov. <a href="https://en.wikipedia.org/wiki/Apache_Parquet">Parquet</a> je podatkovni format, ki se pogosto uporablja v povezavi z velikimi podatki.</li> 
</ul>
</dd>
<dt>3) Obdelava podatkov</dt>
<dd>
To je najbolj razburljiv del podatkovne poti, ki vključuje pretvorbo podatkov iz njihove izvirne oblike v obliko, ki jo je mogoče uporabiti za vizualizacijo ali usposabljanje modela. Pri delu z nestrukturiranimi podatki, kot so besedila ali slike, bomo morda morali uporabiti nekatere tehnike umetne inteligence za izločanje <b>značilnosti</b> iz podatkov, s čimer jih pretvorimo v strukturirano obliko.
</dd>
<dt>4) Vizualizacija / Človeški vpogledi</dt>
<dd>
Pogosto, da bi razumeli podatke, jih moramo vizualizirati. Z različnimi tehnikami vizualizacije lahko najdemo pravi pogled, da pridemo do vpogleda. Pogosto mora podatkovni znanstvenik "eksperimentirati s podatki", jih večkrat vizualizirati in iskati določene povezave. Prav tako lahko uporabimo statistične tehnike za testiranje hipotez ali dokazovanje korelacije med različnimi podatki.   
</dd>
<dt>5) Usposabljanje napovednega modela</dt>
<dd>
Ker je končni cilj podatkovne znanosti sprejemanje odločitev na podlagi podatkov, bomo morda želeli uporabiti tehnike <a href="http://github.com/microsoft/ml-for-beginners">strojnega učenja</a> za gradnjo napovednega modela. Ta model lahko nato uporabimo za napovedovanje z uporabo novih podatkovnih nizov s podobnimi strukturami.
</dd>
</dl>

Seveda, odvisno od dejanskih podatkov, lahko nekateri koraki manjkajo (npr. ko so podatki že v bazi podatkov ali ko ne potrebujemo usposabljanja modela), ali pa se nekateri koraki ponovijo večkrat (na primer obdelava podatkov).

## Digitalizacija in digitalna transformacija

V zadnjem desetletju so številna podjetja začela razumeti pomen podatkov pri sprejemanju poslovnih odločitev. Za uporabo načel podatkovne znanosti pri vodenju podjetja je najprej treba zbrati nekaj podatkov, tj. prevesti poslovne procese v digitalno obliko. To je znano kot **digitalizacija**. Uporaba tehnik podatkovne znanosti na teh podatkih za usmerjanje odločitev lahko vodi do znatnega povečanja produktivnosti (ali celo preoblikovanja poslovanja), kar imenujemo **digitalna transformacija**.

Razmislimo o primeru. Predpostavimo, da imamo tečaj podatkovne znanosti (kot je ta), ki ga izvajamo na spletu za študente, in želimo uporabiti podatkovno znanost za njegovo izboljšanje. Kako lahko to storimo?

Začnemo lahko z vprašanjem "Kaj lahko digitaliziramo?" Najenostavnejši način bi bil merjenje časa, ki ga vsak študent potrebuje za dokončanje vsakega modula, in merjenje pridobljenega znanja z izvedbo testa z več izbirami na koncu vsakega modula. Z izračunom povprečnega časa za dokončanje med vsemi študenti lahko ugotovimo, kateri moduli povzročajo največ težav študentom, in delamo na njihovi poenostavitvi.
> Morda boste trdili, da ta pristop ni idealen, ker so moduli lahko različno dolgi. Verjetno bi bilo bolj pošteno čas deliti z dolžino modula (v številu znakov) in primerjati te vrednosti.

Ko začnemo analizirati rezultate testov z več izbirami, lahko poskusimo ugotoviti, katere koncepte imajo študenti težave razumeti, in uporabimo te informacije za izboljšanje vsebine. Da bi to dosegli, moramo teste oblikovati tako, da vsako vprašanje ustreza določenemu konceptu ali delu znanja.

Če želimo stvari še bolj zaplesti, lahko čas, porabljen za vsak modul, primerjamo s starostno kategorijo študentov. Morda bomo ugotovili, da za nekatere starostne kategorije traja neprimerno dolgo, da dokončajo modul, ali pa da študenti odnehajo, preden ga dokončajo. To nam lahko pomaga podati starostna priporočila za modul in zmanjšati nezadovoljstvo ljudi zaradi napačnih pričakovanj.

## 🚀 Izziv

V tem izzivu bomo poskušali najti koncepte, povezane s področjem podatkovne znanosti, tako da bomo analizirali besedila. Vzeli bomo članek iz Wikipedije o podatkovni znanosti, prenesli in obdelali besedilo ter nato ustvarili oblak besed, kot je ta:

![Oblak besed za podatkovno znanost](../../../../translated_images/sl/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.png)

Obiščite [`notebook.ipynb`](../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore'), da si ogledate kodo. Prav tako lahko zaženete kodo in vidite, kako v realnem času izvaja vse transformacije podatkov.

> Če ne veste, kako zagnati kodo v Jupyter Notebooku, si oglejte [ta članek](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Kvizi po predavanju](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Naloge

* **Naloga 1**: Spremenite zgornjo kodo, da ugotovite povezane koncepte za področji **Big Data** in **strojno učenje**
* **Naloga 2**: [Razmislite o scenarijih podatkovne znanosti](assignment.md)

## Zasluge

To lekcijo je z ljubeznijo pripravil [Dmitry Soshnikov](http://soshnikov.com)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.