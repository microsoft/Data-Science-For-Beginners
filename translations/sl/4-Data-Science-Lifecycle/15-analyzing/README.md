<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d92f57eb110dc7f765c05cbf0f837c77",
  "translation_date": "2025-08-30T18:23:41+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "sl"
}
-->
# Življenjski cikel podatkovne znanosti: Analiza

|![ Sketchnote avtorja [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Življenjski cikel podatkovne znanosti: Analiza - _Sketchnote avtorja [@nitya](https://twitter.com/nitya)_ |

## Predavanje - kviz

## [Predavanje - kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

Analiza v življenjskem ciklu podatkov potrjuje, da lahko podatki odgovorijo na zastavljena vprašanja ali rešijo določen problem. Ta korak se osredotoča tudi na preverjanje, ali model pravilno naslavlja ta vprašanja in probleme. Ta lekcija je osredotočena na raziskovalno analizo podatkov (Exploratory Data Analysis ali EDA), ki vključuje tehnike za določanje značilnosti in odnosov znotraj podatkov ter pripravo podatkov za modeliranje.

Uporabili bomo primer podatkovnega nabora s [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1), da pokažemo, kako to uporabiti s Pythonom in knjižnico Pandas. Ta podatkovni nabor vsebuje število nekaterih pogostih besed, ki se pojavljajo v e-poštnih sporočilih, pri čemer so viri teh sporočil anonimni. Uporabite [zvezek](notebook.ipynb) v tej mapi za sledenje.

## Raziskovalna analiza podatkov

Faza zajema v življenjskem ciklu je tista, kjer se pridobijo podatki ter določijo problemi in vprašanja, vendar kako vemo, ali lahko podatki podprejo končni rezultat? 
Spomnimo se, da si podatkovni znanstvenik lahko zastavi naslednja vprašanja, ko pridobi podatke:
- Ali imam dovolj podatkov za rešitev tega problema?
- Ali so podatki ustrezne kakovosti za ta problem?
- Če skozi te podatke odkrijem dodatne informacije, ali bi morali razmisliti o spremembi ali ponovni opredelitvi ciljev?

Raziskovalna analiza podatkov je proces spoznavanja podatkov in se lahko uporabi za odgovore na ta vprašanja ter za prepoznavanje izzivov pri delu s podatkovnim naborom. Osredotočimo se na nekatere tehnike, ki se uporabljajo za dosego tega.

## Profiliranje podatkov, opisna statistika in Pandas
Kako oceniti, ali imamo dovolj podatkov za rešitev problema? Profiliranje podatkov lahko povzame in zbere splošne informacije o našem podatkovnem naboru s tehnikami opisne statistike. Profiliranje podatkov nam pomaga razumeti, kaj imamo na voljo, opisna statistika pa nam pomaga razumeti, koliko stvari imamo na voljo.

V nekaj prejšnjih lekcijah smo uporabili Pandas za zagotavljanje opisne statistike z uporabo funkcije [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Ta funkcija zagotavlja število, največje in najmanjše vrednosti, povprečje, standardni odklon in kvantile za numerične podatke. Uporaba opisne statistike, kot je funkcija `describe()`, vam lahko pomaga oceniti, koliko podatkov imate in ali jih potrebujete več.

## Vzorčenje in poizvedovanje
Raziskovanje vsega v velikem podatkovnem naboru je lahko zelo zamudno in naloga, ki jo običajno prepustimo računalniku. Vendar pa je vzorčenje koristno orodje za razumevanje podatkov in nam omogoča boljše razumevanje, kaj je v podatkovnem naboru in kaj predstavlja. Z vzorcem lahko uporabite verjetnost in statistiko za oblikovanje splošnih zaključkov o svojih podatkih. Čeprav ni določenega pravila o tem, koliko podatkov bi morali vzorčiti, je pomembno opozoriti, da več kot vzorčite, natančnejše posplošitve lahko naredite o podatkih.

Pandas ima funkcijo [`sample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), kjer lahko podate argument, koliko naključnih vzorcev želite prejeti in uporabiti.

Splošno poizvedovanje podatkov vam lahko pomaga odgovoriti na splošna vprašanja in teorije, ki jih imate. V nasprotju z vzorčenjem vam poizvedbe omogočajo nadzor in osredotočanje na specifične dele podatkov, o katerih imate vprašanja. Funkcija [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) v knjižnici Pandas vam omogoča izbiro stolpcev in pridobivanje preprostih odgovorov o podatkih prek pridobljenih vrstic.

## Raziskovanje z vizualizacijami
Ni vam treba čakati, da so podatki temeljito očiščeni in analizirani, da začnete ustvarjati vizualizacije. Pravzaprav lahko vizualna predstavitev med raziskovanjem pomaga prepoznati vzorce, odnose in težave v podatkih. Poleg tega vizualizacije omogočajo komunikacijo s tistimi, ki niso vključeni v upravljanje podatkov, in so lahko priložnost za deljenje in pojasnjevanje dodatnih vprašanj, ki niso bila obravnavana v fazi zajema. Oglejte si [oddelek o vizualizacijah](../../../../../../../../../3-Data-Visualization), da izveste več o nekaterih priljubljenih načinih vizualnega raziskovanja.

## Raziskovanje za prepoznavanje nedoslednosti
Vse teme v tej lekciji lahko pomagajo prepoznati manjkajoče ali nedosledne vrednosti, vendar Pandas ponuja funkcije za preverjanje nekaterih od teh. Funkciji [isna() ali isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) lahko preverita manjkajoče vrednosti. Pomemben del raziskovanja teh vrednosti v vaših podatkih je raziskovanje, zakaj so se sploh pojavile. To vam lahko pomaga odločiti, katere [ukrepe sprejeti za njihovo rešitev](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Predavanje - kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/27)

## Naloga

[Raziskovanje za odgovore](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.