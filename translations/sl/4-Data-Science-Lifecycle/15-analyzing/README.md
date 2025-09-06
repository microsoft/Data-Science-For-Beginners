<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "661dad02c3ac239644d34c1eb51e76f8",
  "translation_date": "2025-09-06T21:45:04+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "sl"
}
-->
# Življenjski cikel podatkovne znanosti: Analiza

|![ Sketchnote avtorja [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Življenjski cikel podatkovne znanosti: Analiza - _Sketchnote avtorja [@nitya](https://twitter.com/nitya)_ |

## [Predavanje: Kviz](https://ff-quizzes.netlify.app/en/ds/quiz/28)

Analiza v življenjskem ciklu podatkov potrjuje, da lahko podatki odgovorijo na zastavljena vprašanja ali rešijo določen problem. Ta korak se osredotoča tudi na preverjanje, ali model pravilno naslavlja ta vprašanja in probleme. Lekcija je osredotočena na raziskovalno analizo podatkov (Exploratory Data Analysis ali EDA), ki vključuje tehnike za določanje značilnosti in odnosov znotraj podatkov ter pripravo podatkov za modeliranje.

Uporabili bomo primer podatkovnega nabora s [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1), da pokažemo, kako to uporabiti s Pythonom in knjižnico Pandas. Ta podatkovni nabor vsebuje število nekaterih pogostih besed, ki se pojavljajo v e-poštnih sporočilih, pri čemer so viri teh sporočil anonimni. Uporabite [zvezek](notebook.ipynb) v tej mapi za sledenje.

## Raziskovalna analiza podatkov

Faza zajema v življenjskem ciklu vključuje pridobivanje podatkov ter določanje problemov in vprašanj, vendar kako vemo, ali podatki lahko podprejo končni rezultat? 
Spomnimo se, da si podatkovni znanstvenik lahko zastavi naslednja vprašanja, ko pridobi podatke:
- Ali imam dovolj podatkov za rešitev tega problema?
- Ali so podatki ustrezne kakovosti za ta problem?
- Če skozi te podatke odkrijem dodatne informacije, ali bi morali razmisliti o spremembi ali ponovni opredelitvi ciljev?
Raziskovalna analiza podatkov je proces spoznavanja podatkov in se lahko uporablja za odgovore na ta vprašanja ter za prepoznavanje izzivov pri delu s podatkovnim naborom. Osredotočimo se na nekatere tehnike, ki se uporabljajo za dosego tega.

## Profiliranje podatkov, opisna statistika in Pandas
Kako oceniti, ali imamo dovolj podatkov za rešitev problema? Profiliranje podatkov lahko povzame in zbere splošne informacije o našem podatkovnem naboru s tehnikami opisne statistike. Profiliranje podatkov nam pomaga razumeti, kaj imamo na voljo, opisna statistika pa, koliko tega imamo.

V nekaj prejšnjih lekcijah smo uporabili Pandas za pridobivanje opisne statistike z uporabo funkcije [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Ta funkcija zagotavlja število, največje in najmanjše vrednosti, povprečje, standardni odklon in kvantile za numerične podatke. Uporaba opisne statistike, kot je funkcija `describe()`, vam lahko pomaga oceniti, koliko podatkov imate in ali jih potrebujete več.

## Vzorčenje in poizvedovanje
Raziskovanje celotnega velikega podatkovnega nabora je lahko zelo zamudno in je običajno naloga, ki jo prepustimo računalniku. Vzorčenje pa je uporabno orodje za razumevanje podatkov in omogoča boljši vpogled v to, kaj podatkovni nabor predstavlja. Z vzorcem lahko uporabite verjetnost in statistiko za oblikovanje splošnih zaključkov o svojih podatkih. Čeprav ni določenega pravila o tem, koliko podatkov bi morali vzorčiti, je pomembno vedeti, da več podatkov kot vzorčite, bolj natančne posplošitve lahko naredite. 
Pandas ima funkcijo [`sample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), kjer lahko določite, koliko naključnih vzorcev želite prejeti in uporabiti.

Splošno poizvedovanje podatkov vam lahko pomaga odgovoriti na splošna vprašanja in teorije, ki jih imate. V nasprotju z vzorčenjem vam poizvedbe omogočajo nadzor in osredotočenost na specifične dele podatkov, o katerih imate vprašanja. 
Funkcija [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) v knjižnici Pandas vam omogoča izbiro stolpcev in pridobivanje preprostih odgovorov o podatkih prek pridobljenih vrstic.

## Raziskovanje z vizualizacijami
Ni vam treba čakati, da so podatki popolnoma očiščeni in analizirani, preden začnete ustvarjati vizualizacije. Pravzaprav lahko vizualna predstavitev med raziskovanjem pomaga prepoznati vzorce, odnose in težave v podatkih. Poleg tega vizualizacije omogočajo komunikacijo s tistimi, ki niso vključeni v upravljanje podatkov, in so lahko priložnost za deljenje in pojasnjevanje dodatnih vprašanj, ki niso bila obravnavana v fazi zajema. Oglejte si [oddelek o vizualizacijah](../../../../../../../../../3-Data-Visualization), da izveste več o nekaterih priljubljenih načinih vizualnega raziskovanja.

## Raziskovanje za prepoznavanje nedoslednosti
Vse teme v tej lekciji lahko pomagajo prepoznati manjkajoče ali nedosledne vrednosti, vendar Pandas ponuja funkcije za preverjanje nekaterih od teh. [isna() ali isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) lahko preverita manjkajoče vrednosti. Pomemben del raziskovanja teh vrednosti v vaših podatkih je raziskati, zakaj so se sploh pojavile. To vam lahko pomaga odločiti, katere [ukrepe sprejeti za njihovo rešitev](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Kviz po predavanju](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Naloga

[Raziskovanje za odgovore](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.