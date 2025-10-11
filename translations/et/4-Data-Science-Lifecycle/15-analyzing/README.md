<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "661dad02c3ac239644d34c1eb51e76f8",
  "translation_date": "2025-10-11T15:49:11+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "et"
}
-->
# Andmeteaduse elutsükkel: Analüüsimine

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Andmeteaduse elutsükkel: Analüüsimine - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Eelloengu viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/28)

Analüüsimine andmete elutsüklis kinnitab, et andmed suudavad vastata esitatud küsimustele või lahendada konkreetse probleemi. See samm keskendub ka sellele, et mudel vastaks korrektselt nendele küsimustele ja probleemidele. See õppetund keskendub andmete uurivale analüüsile (Exploratory Data Analysis ehk EDA), mis hõlmab tehnikaid andmete omaduste ja seoste määratlemiseks ning nende ettevalmistamiseks modelleerimiseks.

Kasutame näidisandmestikku [Kaggle'ist](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1), et näidata, kuidas seda saab rakendada Pythonis ja Pandase teegis. See andmestik sisaldab loendit mõningatest tavalistest sõnadest, mis esinevad e-kirjades, kusjuures e-kirjade allikad on anonüümsed. Kasutage selle kataloogi [märkmikku](notebook.ipynb), et kaasa töötada.

## Uuriv andmeanalüüs

Elutsükli kogumise faasis omandatakse andmed ning määratletakse probleemid ja küsimused, kuid kuidas me teame, et andmed suudavad toetada lõpptulemust? 
Tuletage meelde, et andmeteadlane võib andmete hankimisel esitada järgmisi küsimusi:
- Kas mul on piisavalt andmeid selle probleemi lahendamiseks?
- Kas andmete kvaliteet on selle probleemi jaoks piisav?
- Kui ma avastan nende andmete kaudu lisainformatsiooni, kas peaksime kaaluma eesmärkide muutmist või ümberdefineerimist?

Uuriv andmeanalüüs on protsess, mille käigus tutvutakse andmetega ja vastatakse nendele küsimustele, samuti tuvastatakse andmestikuga töötamise väljakutsed. Vaatame mõningaid tehnikaid, mida selle saavutamiseks kasutatakse.

## Andmeprofiilimine, kirjeldav statistika ja Pandas
Kuidas hinnata, kas meil on piisavalt andmeid probleemi lahendamiseks? Andmeprofiilimine võimaldab kokku võtta ja koguda üldist teavet meie andmestiku kohta kirjeldava statistika tehnikate abil. Andmeprofiilimine aitab meil mõista, mis on meie käsutuses, ja kirjeldav statistika aitab meil mõista, kui palju asju on meie käsutuses.

Mõnes varasemas õppetunnis oleme kasutanud Pandast, et pakkuda kirjeldavat statistikat [`describe()` funktsiooni](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html) abil. See funktsioon annab numbriliste andmete kohta teavet, nagu loendus, maksimaalsed ja minimaalsed väärtused, keskmine, standardhälve ja kvantiilid. Kirjeldava statistika, näiteks `describe()` funktsiooni kasutamine, aitab teil hinnata, kui palju andmeid teil on ja kas vajate rohkem.

## Valimivõtmine ja päringud
Kõigi andmete uurimine suures andmestikus võib olla väga aeganõudev ja tavaliselt jäetakse see ülesanne arvuti hooleks. Kuid valimivõtmine on kasulik tööriist andmete mõistmiseks ja võimaldab meil paremini mõista, mis andmestikus sisaldub ja mida see esindab. Valimi abil saate rakendada tõenäosusteooriat ja statistikat, et teha andmete kohta üldisi järeldusi. Kuigi pole kindlat reeglit, kui palju andmeid tuleks valimisse võtta, on oluline märkida, et mida rohkem andmeid valimisse kaasate, seda täpsemaid üldistusi saate teha.

Pandas teegis on [`sample()` funktsioon](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), mille abil saate määrata, kui palju juhuslikke valimeid soovite saada ja kasutada.

Andmete üldine päring aitab teil vastata mõningatele üldistele küsimustele ja teooriatele, mis teil võivad olla. Erinevalt valimivõtmisest võimaldavad päringud teil keskenduda konkreetsetele andmete osadele, mille kohta teil on küsimusi. Pandase teegis olev [`query()` funktsioon](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) võimaldab teil valida veerge ja saada lihtsaid vastuseid andmete kohta ridade kaudu, mis päringuga tagastatakse.

## Uurimine visualiseerimiste abil
Te ei pea ootama, kuni andmed on täielikult puhastatud ja analüüsitud, et hakata looma visualiseeringuid. Tegelikult võib visuaalne esitus uurimise ajal aidata tuvastada mustreid, seoseid ja probleeme andmetes. Lisaks pakuvad visualiseeringud võimalust suhelda nendega, kes ei tegele andmete haldamisega, ning võivad olla võimalus jagada ja täpsustada täiendavaid küsimusi, mis kogumise etapis ei saanud vastust. Vaadake [visualiseerimiste sektsiooni](../../../../../../../../../3-Data-Visualization), et õppida rohkem populaarsete visuaalsete uurimisviiside kohta.

## Uurimine ebakõlade tuvastamiseks
Kõik selle õppetunni teemad aitavad tuvastada puuduvaid või ebajärjekindlaid väärtusi, kuid Pandas pakub funktsioone, mis aitavad mõningaid neist kontrollida. [isna() või isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) funktsioonid võimaldavad kontrollida puuduvaid väärtusi. Üks oluline osa nende väärtuste uurimisest teie andmetes on uurida, miks need üldse selliseks kujunesid. See aitab teil otsustada, milliseid [meetmeid nende lahendamiseks võtta](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Järelloengu viktoriin](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Ülesanne

[Uurimine vastuste leidmiseks](assignment.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.