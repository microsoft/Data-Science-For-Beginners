<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a167aa0bfb1c46ece1b3d21ae939cc0d",
  "translation_date": "2025-09-05T05:59:31+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "sl"
}
-->
# Življenjski cikel podatkovne znanosti: Analiza

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Življenjski cikel podatkovne znanosti: Analiza - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## Predhodni kviz

## [Predhodni kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

Analiza v življenjskem ciklu podatkov potrjuje, da podatki lahko odgovorijo na zastavljena vprašanja ali rešijo določen problem. Ta korak se osredotoča tudi na preverjanje, ali model pravilno obravnava ta vprašanja in probleme. Ta lekcija je osredotočena na raziskovalno analizo podatkov (Exploratory Data Analysis ali EDA), ki vključuje tehnike za opredelitev značilnosti in odnosov znotraj podatkov ter pripravo podatkov za modeliranje.

Uporabili bomo primer podatkovne zbirke iz [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1), da pokažemo, kako to uporabiti s Pythonom in knjižnico Pandas. Ta podatkovna zbirka vsebuje število nekaterih pogostih besed, ki se pojavljajo v e-poštnih sporočilih, pri čemer so viri teh sporočil anonimni. Uporabite [notebook](../../../../4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) v tej mapi za spremljanje.

## Raziskovalna analiza podatkov

Faza zajema v življenjskem ciklu vključuje pridobivanje podatkov ter opredelitev problemov in vprašanj, vendar kako vemo, da podatki lahko podpirajo končni rezultat? 
Spomnite se, da si podatkovni znanstvenik lahko zastavi naslednja vprašanja, ko pridobi podatke:
-   Ali imam dovolj podatkov za rešitev tega problema?
-   Ali so podatki ustrezne kakovosti za ta problem?
-   Če skozi podatke odkrijem dodatne informacije, ali bi morali razmisliti o spremembi ali ponovni opredelitvi ciljev?

Raziskovalna analiza podatkov je proces spoznavanja podatkov in se lahko uporablja za odgovore na ta vprašanja ter za prepoznavanje izzivov pri delu s podatkovno zbirko. Osredotočimo se na nekatere tehnike, ki se uporabljajo za dosego tega.

## Profiliranje podatkov, opisna statistika in Pandas
Kako oceniti, ali imamo dovolj podatkov za rešitev problema? Profiliranje podatkov lahko povzame in zbere splošne informacije o naši podatkovni zbirki z uporabo tehnik opisne statistike. Profiliranje podatkov nam pomaga razumeti, kaj imamo na voljo, opisna statistika pa nam pomaga razumeti, koliko stvari imamo na voljo.

V nekaj prejšnjih lekcijah smo uporabili Pandas za pridobitev opisne statistike z uporabo funkcije [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Ta funkcija zagotavlja število, največje in najmanjše vrednosti, povprečje, standardni odklon in kvantile za numerične podatke. Uporaba opisne statistike, kot je funkcija `describe()`, vam lahko pomaga oceniti, koliko podatkov imate in ali jih potrebujete več.

## Vzorčenje in poizvedovanje
Raziskovanje celotne velike podatkovne zbirke je lahko zelo zamudno in naloga, ki jo običajno opravi računalnik. Vzorčenje pa je koristno orodje za razumevanje podatkov in omogoča boljše razumevanje, kaj je v podatkovni zbirki in kaj predstavlja. Z vzorcem lahko uporabite verjetnost in statistiko za oblikovanje splošnih zaključkov o vaših podatkih. Čeprav ni določenega pravila, koliko podatkov bi morali vzorčiti, je pomembno vedeti, da več podatkov kot vzorčite, bolj natančno lahko oblikujete splošne zaključke o podatkih.

Pandas ima funkcijo [`sample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), kjer lahko podate argument, koliko naključnih vzorcev želite prejeti in uporabiti.

Splošno poizvedovanje podatkov vam lahko pomaga odgovoriti na splošna vprašanja in teorije, ki jih imate. V nasprotju z vzorčenjem vam poizvedbe omogočajo nadzor in osredotočenje na specifične dele podatkov, o katerih imate vprašanja. Funkcija [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) v knjižnici Pandas vam omogoča izbiro stolpcev in pridobitev preprostih odgovorov o podatkih prek pridobljenih vrstic.

## Raziskovanje z vizualizacijami
Ni vam treba čakati, da so podatki temeljito očiščeni in analizirani, da začnete ustvarjati vizualizacije. Pravzaprav lahko vizualna predstavitev med raziskovanjem pomaga prepoznati vzorce, odnose in težave v podatkih. Poleg tega vizualizacije omogočajo komunikacijo z osebami, ki niso vključene v upravljanje podatkov, in so lahko priložnost za deljenje ter pojasnjevanje dodatnih vprašanj, ki niso bila obravnavana v fazi zajema. Oglejte si [oddelek o vizualizacijah](../../../../../../../../../3-Data-Visualization), da se naučite več o nekaterih priljubljenih načinih vizualnega raziskovanja.

## Raziskovanje za prepoznavanje nedoslednosti
Vse teme v tej lekciji lahko pomagajo prepoznati manjkajoče ali nedosledne vrednosti, vendar Pandas ponuja funkcije za preverjanje nekaterih od teh. [isna() ali isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) lahko preverita manjkajoče vrednosti. Pomemben del raziskovanja teh vrednosti v vaših podatkih je raziskovanje, zakaj so se tako pojavile. To vam lahko pomaga pri odločitvi, katere [ukrepe sprejeti za njihovo rešitev](../../../../../../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Kviz po predavanju](https://ff-quizzes.netlify.app/en/ds/)

## Naloga

[Raziskovanje za odgovore](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.