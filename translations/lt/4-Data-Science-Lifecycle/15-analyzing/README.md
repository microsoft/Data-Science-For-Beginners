<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d92f57eb110dc7f765c05cbf0f837c77",
  "translation_date": "2025-08-31T05:42:58+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "lt"
}
-->
# Duomenų mokslo gyvavimo ciklas: Analizavimas

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Duomenų mokslo gyvavimo ciklas: Analizavimas - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## Prieš paskaitą: testas

## [Prieš paskaitą: testas](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/28)

Analizavimas duomenų gyvavimo cikle patvirtina, kad duomenys gali atsakyti į pateiktus klausimus arba išspręsti tam tikrą problemą. Šis etapas taip pat gali būti skirtas patvirtinti, kad modelis tinkamai sprendžia šiuos klausimus ir problemas. Ši pamoka orientuota į duomenų tyrimo analizę (EDA), kuri apima metodus, skirtus apibrėžti duomenų savybes ir ryšius, bei gali būti naudojama duomenų paruošimui modeliavimui.

Naudosime pavyzdinį duomenų rinkinį iš [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1), kad parodytume, kaip tai galima pritaikyti naudojant Python ir Pandas biblioteką. Šis duomenų rinkinys apima dažniausiai pasitaikančių žodžių skaičių el. laiškuose, o šių laiškų šaltiniai yra anonimiški. Naudokite [užrašų knygelę](notebook.ipynb) šiame kataloge, kad galėtumėte sekti pamoką.

## Duomenų tyrimo analizė

Duomenų surinkimo etapas gyvavimo cikle yra tas, kuriame duomenys yra įgyjami, taip pat apibrėžiamos problemos ir klausimai. Bet kaip žinoti, ar duomenys gali padėti pasiekti galutinį rezultatą? 
Priminkime, kad duomenų mokslininkas gali užduoti šiuos klausimus, kai gauna duomenis:
- Ar turiu pakankamai duomenų šiai problemai išspręsti?
- Ar duomenų kokybė yra tinkama šiai problemai?
- Jei per šiuos duomenis atrandu papildomos informacijos, ar turėtume apsvarstyti tikslų pakeitimą ar perdefinavimą?

Duomenų tyrimo analizė yra procesas, leidžiantis geriau pažinti duomenis ir gali būti naudojamas atsakyti į šiuos klausimus, taip pat nustatyti iššūkius, susijusius su duomenų rinkiniu. Pažvelkime į kai kuriuos metodus, naudojamus šiam tikslui pasiekti.

## Duomenų profiliavimas, aprašomoji statistika ir Pandas
Kaip įvertinti, ar turime pakankamai duomenų problemai išspręsti? Duomenų profiliavimas gali apibendrinti ir surinkti bendrą informaciją apie mūsų duomenų rinkinį naudojant aprašomosios statistikos metodus. Duomenų profiliavimas padeda suprasti, kas mums yra prieinama, o aprašomoji statistika padeda suprasti, kiek dalykų yra prieinama.

Keletą ankstesnių pamokų metu naudojome Pandas, kad pateiktume aprašomąją statistiką su [`describe()` funkcija](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Ji pateikia skaičių, maksimalias ir minimalias reikšmes, vidurkį, standartinį nuokrypį ir kvantiles skaitmeniniams duomenims. Naudojant aprašomąją statistiką, tokią kaip `describe()` funkcija, galima įvertinti, kiek turime duomenų ir ar jų reikia daugiau.

## Imčių ėmimas ir užklausos
Didelio duomenų rinkinio tyrimas gali būti labai daug laiko reikalaujantis procesas, kurį dažniausiai atlieka kompiuteris. Tačiau imčių ėmimas yra naudingas įrankis, leidžiantis geriau suprasti duomenis ir tai, ką jie reprezentuoja. Naudodami imtį, galite taikyti tikimybių ir statistikos metodus, kad padarytumėte bendras išvadas apie savo duomenis. Nors nėra nustatytos taisyklės, kiek duomenų reikėtų imti, svarbu pažymėti, kad kuo daugiau duomenų imsite, tuo tikslesnę bendrą išvadą galėsite padaryti apie duomenis.

Pandas bibliotekoje yra [`sample()` funkcija](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), kurioje galite nurodyti, kiek atsitiktinių imčių norite gauti ir naudoti.

Bendros duomenų užklausos gali padėti atsakyti į kai kuriuos bendrus klausimus ir teorijas, kurias galite turėti. Skirtingai nuo imčių ėmimo, užklausos leidžia jums kontroliuoti ir susitelkti į konkrečias duomenų dalis, apie kurias turite klausimų. 
[`query()` funkcija](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) Pandas bibliotekoje leidžia pasirinkti stulpelius ir gauti paprastus atsakymus apie duomenis per gautas eilutes.

## Tyrimas naudojant vizualizacijas
Jums nereikia laukti, kol duomenys bus visiškai išvalyti ir išanalizuoti, kad pradėtumėte kurti vizualizacijas. Iš tiesų, vizualinis atvaizdavimas tyrimo metu gali padėti identifikuoti duomenų modelius, ryšius ir problemas. Be to, vizualizacijos suteikia galimybę bendrauti su tais, kurie nėra tiesiogiai susiję su duomenų valdymu, ir gali būti galimybė pasidalinti bei patikslinti papildomus klausimus, kurie nebuvo sprendžiami surinkimo etape. Žr. [Vizualizacijų skyrių](../../../../../../../../../3-Data-Visualization), kad sužinotumėte daugiau apie populiarius būdus tyrinėti vizualiai.

## Tyrimas siekiant nustatyti neatitikimus
Visos šios pamokos temos gali padėti identifikuoti trūkstamas ar nesuderinamas reikšmes, tačiau Pandas suteikia funkcijas, leidžiančias patikrinti kai kurias iš jų. [isna() arba isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) gali patikrinti trūkstamas reikšmes. Vienas svarbus aspektas, tyrinėjant šias reikšmes jūsų duomenyse, yra suprasti, kodėl jos atsirado. Tai gali padėti nuspręsti, kokius [veiksmus reikėtų atlikti, kad jas išspręstumėte](/2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Prieš paskaitą: testas](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/27)

## Užduotis

[Tyrimas atsakymams rasti](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, kylančius dėl šio vertimo naudojimo.