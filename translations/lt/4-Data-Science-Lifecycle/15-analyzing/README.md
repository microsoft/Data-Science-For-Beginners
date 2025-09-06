<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2baeafe1db4d58ee5b8ec85db9de728a",
  "translation_date": "2025-09-05T16:06:19+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "lt"
}
-->
# Duomenų mokslo gyvavimo ciklas: Analizavimas

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Duomenų mokslo gyvavimo ciklas: Analizavimas - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## Prieš paskaitą: testas

## [Prieš paskaitą: testas](https://ff-quizzes.netlify.app/en/ds/quiz/28)

Analizavimas duomenų gyvavimo cikle patvirtina, kad duomenys gali atsakyti į pateiktus klausimus arba išspręsti konkrečią problemą. Šis etapas taip pat gali būti skirtas patvirtinti, kad modelis tinkamai sprendžia šiuos klausimus ir problemas. Ši pamoka orientuota į duomenų tyrimo analizę (EDA), kuri apima technikas, padedančias apibrėžti duomenų savybes ir ryšius bei paruošti duomenis modeliavimui.

Naudosime pavyzdinį duomenų rinkinį iš [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1), kad parodytume, kaip tai galima pritaikyti naudojant Python ir Pandas biblioteką. Šis duomenų rinkinys apima dažniausiai pasitaikančių žodžių skaičių el. laiškuose, o šių laiškų šaltiniai yra anonimiški. Naudokite [užrašų knygelę](../../../../4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) šiame kataloge, kad galėtumėte sekti pamoką.

## Duomenų tyrimo analizė

Duomenų surinkimo etapas gyvavimo cikle yra tas, kuriame duomenys įgyjami, taip pat apibrėžiamos problemos ir klausimai. Bet kaip žinoti, ar duomenys gali padėti pasiekti galutinį rezultatą? 
Priminkime, kad duomenų mokslininkas gali užduoti šiuos klausimus, kai gauna duomenis:
- Ar turiu pakankamai duomenų šiai problemai išspręsti?
- Ar duomenų kokybė yra tinkama šiai problemai?
- Jei per šiuos duomenis atrandu papildomos informacijos, ar turėtume apsvarstyti tikslų pakeitimą ar perdefinavimą?

Duomenų tyrimo analizė yra procesas, padedantis geriau pažinti duomenis ir atsakyti į šiuos klausimus, taip pat identifikuoti iššūkius, susijusius su duomenų rinkiniu. Pažvelkime į kai kurias technikas, naudojamas šiam tikslui pasiekti.

## Duomenų profilavimas, aprašomoji statistika ir Pandas
Kaip įvertinti, ar turime pakankamai duomenų problemai išspręsti? Duomenų profilavimas gali apibendrinti ir surinkti bendrą informaciją apie mūsų duomenų rinkinį, naudojant aprašomosios statistikos technikas. Duomenų profilavimas padeda suprasti, kas mums prieinama, o aprašomoji statistika padeda suprasti, kiek turime.

Keletą ankstesnių pamokų metu naudojome Pandas, kad gautume aprašomąją statistiką su [`describe()` funkcija](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Ji pateikia skaičių, maksimalias ir minimalias reikšmes, vidurkį, standartinį nuokrypį ir kvantiles skaitiniuose duomenyse. Naudojant aprašomąją statistiką, kaip `describe()` funkciją, galima įvertinti, kiek turime duomenų ir ar jų reikia daugiau.

## Imčių ėmimas ir užklausos
Didelio duomenų rinkinio tyrimas gali būti labai laiko reikalaujantis ir dažnai paliekamas kompiuteriui. Tačiau imčių ėmimas yra naudinga priemonė, padedanti geriau suprasti duomenis ir tai, ką jie reprezentuoja. Naudojant imtį, galima taikyti tikimybių teoriją ir statistiką, kad būtų galima padaryti bendras išvadas apie duomenis. Nors nėra nustatytos taisyklės, kiek duomenų reikėtų imti, svarbu pažymėti, kad kuo daugiau duomenų imsite, tuo tikslesnės bus jūsų bendros išvados apie duomenis.

Pandas biblioteka turi [`sample()` funkciją](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), kurioje galite nurodyti, kiek atsitiktinių imčių norite gauti ir naudoti.

Bendros duomenų užklausos gali padėti atsakyti į kai kuriuos bendrus klausimus ir teorijas, kurias turite. Skirtingai nuo imčių, užklausos leidžia jums kontroliuoti ir susitelkti į konkrečias duomenų dalis, kurios jus domina. 
[`query()` funkcija](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) Pandas bibliotekoje leidžia pasirinkti stulpelius ir gauti paprastus atsakymus apie duomenis per gautas eilutes.

## Tyrimas naudojant vizualizacijas
Jums nereikia laukti, kol duomenys bus visiškai išvalyti ir išanalizuoti, kad pradėtumėte kurti vizualizacijas. Iš tiesų, vizualinis atvaizdavimas tyrimo metu gali padėti identifikuoti duomenų šablonus, ryšius ir problemas. Be to, vizualizacijos suteikia galimybę bendrauti su tais, kurie nėra tiesiogiai susiję su duomenų valdymu, ir gali būti proga pasidalinti bei patikslinti papildomus klausimus, kurie nebuvo sprendžiami surinkimo etape. Žr. [Vizualizacijų skyrių](../../../../../../../../../3-Data-Visualization), kad sužinotumėte daugiau apie populiarius vizualinio tyrimo būdus.

## Tyrimas siekiant identifikuoti neatitikimus
Visos šios pamokos temos gali padėti identifikuoti trūkstamas ar nesuderinamas reikšmes, tačiau Pandas suteikia funkcijas, skirtas kai kuriems iš jų patikrinti. [isna() arba isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) gali patikrinti trūkstamas reikšmes. Vienas svarbus aspektas, tyrinėjant šias reikšmes duomenyse, yra suprasti, kodėl jos atsirado. Tai gali padėti nuspręsti, kokius [veiksmus reikėtų atlikti, kad jas išspręstumėte](../../../../../../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Po paskaitos: testas](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Užduotis

[Tyrimas atsakymams rasti](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.