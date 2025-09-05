<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a0516588d172f82f35f7a0d4a001e5d0",
  "translation_date": "2025-09-05T19:44:45+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "sl"
}
-->
## Vrste podatkov

Kot smo že omenili, podatki so povsod okoli nas. Le pravilno jih moramo zajeti! Koristno je razlikovati med **strukturiranimi** in **nestrukturiranimi** podatki. Prvi so običajno predstavljeni v dobro strukturirani obliki, pogosto kot tabela ali več tabel, medtem ko so drugi le zbirka datotek. Včasih lahko govorimo tudi o **polstrukturiranih** podatkih, ki imajo neko obliko strukture, ki se lahko močno razlikuje.

| Strukturirani                                                               | Polstrukturirani                                                                                 | Nestrukturirani                          |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | --------------------------------------- |
| Seznam ljudi z njihovimi telefonskimi številkami                            | Wikipedijine strani s povezavami                                                                 | Besedilo Enciklopedije Britannica       |
| Temperatura v vseh sobah stavbe vsako minuto v zadnjih 20 letih             | Zbirka znanstvenih člankov v JSON formatu z avtorji, datumom objave in povzetkom                  | Datoteke z dokumenti podjetja           |
| Podatki o starosti in spolu vseh ljudi, ki vstopajo v stavbo                | Spletne strani                                                                                   | Surov video posnetek iz nadzorne kamere |

## Kje pridobiti podatke

Obstaja veliko možnih virov podatkov, zato jih je nemogoče vse našteti! Vendar pa omenimo nekaj tipičnih mest, kjer lahko pridobimo podatke:

* **Strukturirani**
  - **Internet stvari** (IoT), vključno s podatki iz različnih senzorjev, kot so senzorji temperature ali tlaka, zagotavlja veliko uporabnih podatkov. Na primer, če je poslovna stavba opremljena z IoT senzorji, lahko samodejno nadzorujemo ogrevanje in razsvetljavo, da zmanjšamo stroške.
  - **Ankete**, ki jih prosimo uporabnike, da izpolnijo po nakupu ali po obisku spletne strani.
  - **Analiza vedenja** nam lahko na primer pomaga razumeti, kako globoko uporabnik raziskuje spletno stran in kaj je tipičen razlog za njen zapustitev.
* **Nestrukturirani**
  - **Besedila** so lahko bogat vir vpogledov, kot je skupna **ocena sentimenta** ali pridobivanje ključnih besed in semantičnega pomena.
  - **Slike** ali **video posnetki**. Video posnetek iz nadzorne kamere lahko uporabimo za oceno prometa na cesti in obveščanje ljudi o morebitnih zastojih.
  - **Dnevniki spletnih strežnikov** nam lahko pomagajo razumeti, katere strani naše spletne strani so najpogosteje obiskane in kako dolgo.
* **Polstrukturirani**
  - **Grafi družbenih omrežij** so lahko odličen vir podatkov o osebnostih uporabnikov in potencialni učinkovitosti pri širjenju informacij.
  - Ko imamo kup fotografij s zabave, lahko poskusimo pridobiti podatke o **dinamiki skupine** z izdelavo grafa ljudi, ki se fotografirajo skupaj.

Z poznavanjem različnih možnih virov podatkov lahko razmišljate o različnih scenarijih, kjer je mogoče uporabiti tehnike podatkovne znanosti za boljše razumevanje situacije in izboljšanje poslovnih procesov.

## Kaj lahko storite s podatki

V podatkovni znanosti se osredotočamo na naslednje korake pri delu s podatki:

Seveda, odvisno od dejanskih podatkov, lahko nekateri koraki manjkajo (npr. ko že imamo podatke v podatkovni bazi ali ko ne potrebujemo usposabljanja modela), ali pa se nekateri koraki večkrat ponovijo (kot je obdelava podatkov).

## Digitalizacija in digitalna transformacija

V zadnjem desetletju so številna podjetja začela razumeti pomen podatkov pri sprejemanju poslovnih odločitev. Da bi uporabili načela podatkovne znanosti pri vodenju podjetja, moramo najprej zbrati nekaj podatkov, torej poslovne procese prevesti v digitalno obliko. To imenujemo **digitalizacija**. Uporaba tehnik podatkovne znanosti na teh podatkih za usmerjanje odločitev lahko vodi do znatnih povečanj produktivnosti (ali celo preoblikovanja poslovanja), kar imenujemo **digitalna transformacija**.

Poglejmo primer. Recimo, da imamo tečaj podatkovne znanosti (kot je ta), ki ga izvajamo na spletu za študente, in želimo uporabiti podatkovno znanost za njegovo izboljšanje. Kako lahko to storimo?

Začnemo lahko z vprašanjem "Kaj lahko digitaliziramo?" Najpreprostejši način bi bil merjenje časa, ki ga vsak študent porabi za dokončanje posameznega modula, ter merjenje pridobljenega znanja z večkratno izbiro testa na koncu vsakega modula. Z izračunom povprečnega časa dokončanja med vsemi študenti lahko ugotovimo, kateri moduli povzročajo največ težav študentom, in se osredotočimo na njihovo poenostavitev.
> Lahko bi trdili, da ta pristop ni najboljši, saj so moduli lahko različno dolgi. Verjetno bi bilo bolj pravično čas razdeliti glede na dolžino modula (v številu znakov) in nato primerjati te vrednosti.
Ko začnemo analizirati rezultate testov z več izbirami, lahko poskusimo ugotoviti, katere koncepte imajo študenti težave razumeti, in uporabimo te informacije za izboljšanje vsebine. Da bi to dosegli, moramo teste oblikovati tako, da vsako vprašanje ustreza določenemu konceptu ali delu znanja.

Če želimo stvari še bolj zaplesti, lahko primerjamo čas, potreben za dokončanje posameznega modula, glede na starostno kategorijo študentov. Morda ugotovimo, da za nekatere starostne kategorije traja neprimerno dolgo, da dokončajo modul, ali pa da študenti odnehajo, preden ga zaključijo. To nam lahko pomaga podati starostna priporočila za modul in zmanjšati nezadovoljstvo ljudi zaradi napačnih pričakovanj.

## 🚀 Izziv

V tem izzivu bomo poskušali najti koncepte, ki so relevantni za področje podatkovne znanosti, tako da pregledamo besedila. Vzeli bomo Wikipedijin članek o podatkovni znanosti, prenesli in obdelali besedilo ter nato ustvarili oblak besed, kot je ta:

![Oblak besed za podatkovno znanost](../../../../1-Introduction/01-defining-data-science/images/ds_wordcloud.png)

Obiščite [`notebook.ipynb`](../../../../../../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore'), da preberete kodo. Lahko tudi zaženete kodo in vidite, kako v realnem času izvaja vse transformacije podatkov.

> Če ne veste, kako zagnati kodo v Jupyter Notebooku, si oglejte [ta članek](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Kvizi po predavanju](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Naloge

* **Naloga 1**: Spremenite zgornjo kodo, da ugotovite povezane koncepte za področji **Big Data** in **strojno učenje**.
* **Naloga 2**: [Razmislite o scenarijih podatkovne znanosti](assignment.md)

## Zasluge

To lekcijo je z ♥️ pripravil [Dmitry Soshnikov](http://soshnikov.com)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.