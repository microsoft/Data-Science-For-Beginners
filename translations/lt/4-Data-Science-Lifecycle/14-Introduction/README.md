<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "07478c2092203a69087b9c76b1f4dd56",
  "translation_date": "2025-09-05T16:07:13+00:00",
  "source_file": "4-Data-Science-Lifecycle/14-Introduction/README.md",
  "language_code": "lt"
}
-->
# Duomenų mokslo gyvavimo ciklo įvadas

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/14-DataScience-Lifecycle.png)|
|:---:|
| Duomenų mokslo gyvavimo ciklo įvadas - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Prieš paskaitos testą](https://ff-quizzes.netlify.app/en/ds/quiz/26)

Šiuo metu turbūt jau supratote, kad duomenų mokslas yra procesas. Šį procesą galima suskirstyti į 5 etapus:

- Duomenų rinkimas
- Apdorojimas
- Analizė
- Komunikacija
- Priežiūra

Ši pamoka orientuota į 3 gyvavimo ciklo dalis: duomenų rinkimą, apdorojimą ir priežiūrą.

![Duomenų mokslo gyvavimo ciklo diagrama](../../../../4-Data-Science-Lifecycle/14-Introduction/images/data-science-lifecycle.jpg)  
> Nuotrauka iš [Berkeley School of Information](https://ischoolonline.berkeley.edu/data-science/what-is-data-science/)

## Duomenų rinkimas

Pirmasis gyvavimo ciklo etapas yra labai svarbus, nes nuo jo priklauso visi kiti etapai. Iš esmės tai yra du etapai, sujungti į vieną: duomenų gavimas ir projekto tikslų bei spręstinų problemų apibrėžimas.  
Projekto tikslų apibrėžimas reikalauja gilesnio problemos ar klausimo konteksto. Pirmiausia reikia identifikuoti ir surinkti tuos, kuriems reikia išspręsti problemą. Tai gali būti verslo suinteresuotosios šalys arba projekto rėmėjai, kurie padės nustatyti, kas ar kas pasinaudos šiuo projektu, taip pat kodėl ir kam to reikia. Aiškiai apibrėžtas tikslas turėtų būti išmatuojamas ir kiekybiškai įvertinamas, kad būtų galima nustatyti priimtiną rezultatą.

Klausimai, kuriuos gali užduoti duomenų mokslininkas:
- Ar ši problema jau buvo spręsta anksčiau? Ką pavyko atrasti?
- Ar visi dalyviai supranta tikslą ir paskirtį?
- Ar yra neaiškumų, ir kaip juos sumažinti?
- Kokie yra apribojimai?
- Kaip galėtų atrodyti galutinis rezultatas?
- Kiek turime resursų (laiko, žmonių, skaičiavimo galimybių)?

Toliau reikia identifikuoti, surinkti ir galiausiai ištirti duomenis, reikalingus šiems tikslams pasiekti. Šiame duomenų gavimo etape duomenų mokslininkai taip pat turi įvertinti duomenų kiekį ir kokybę. Tam reikia atlikti tam tikrą duomenų tyrimą, kad būtų patvirtinta, jog surinkti duomenys padės pasiekti norimą rezultatą.

Klausimai, kuriuos gali užduoti duomenų mokslininkas apie duomenis:
- Kokie duomenys jau yra prieinami?
- Kas yra šių duomenų savininkas?
- Kokie yra privatumo klausimai?
- Ar turiu pakankamai duomenų šiai problemai išspręsti?
- Ar duomenų kokybė yra tinkama šiai problemai?
- Jei per šiuos duomenis atrasiu papildomos informacijos, ar turėtume apsvarstyti tikslų pakeitimą ar perapibrėžimą?

## Apdorojimas

Gyvavimo ciklo apdorojimo etapas orientuotas į duomenų šablonų atradimą ir modeliavimą. Kai kurie metodai, naudojami apdorojimo etape, reikalauja statistinių metodų, kad būtų atskleisti šablonai. Paprastai tai būtų varginanti užduotis žmogui, dirbančiam su dideliu duomenų rinkiniu, todėl procesui paspartinti pasitelkiami kompiuteriai. Šiame etape duomenų mokslas ir mašininis mokymasis susikerta. Kaip sužinojote pirmoje pamokoje, mašininis mokymasis yra modelių kūrimo procesas, siekiant suprasti duomenis. Modeliai yra duomenų kintamųjų tarpusavio ryšių reprezentacija, padedanti prognozuoti rezultatus.

Dažniausiai naudojami metodai šiame etape aptariami „ML for Beginners“ mokymo programoje. Sekite nuorodas, kad sužinotumėte daugiau apie juos:

- [Klasifikacija](https://github.com/microsoft/ML-For-Beginners/tree/main/4-Classification): Duomenų organizavimas į kategorijas efektyvesniam naudojimui.
- [Grupavimas](https://github.com/microsoft/ML-For-Beginners/tree/main/5-Clustering): Duomenų suskirstymas į panašias grupes.
- [Regresija](https://github.com/microsoft/ML-For-Beginners/tree/main/2-Regression): Kintamųjų tarpusavio ryšių nustatymas, siekiant prognozuoti ar numatyti vertes.

## Priežiūra

Gyvavimo ciklo diagramoje galite pastebėti, kad priežiūra yra tarp duomenų rinkimo ir apdorojimo. Priežiūra yra nuolatinis duomenų valdymo, saugojimo ir apsaugos procesas viso projekto metu ir turėtų būti svarstoma viso projekto eigoje.

### Duomenų saugojimas

Sprendimai, kaip ir kur saugoti duomenis, gali turėti įtakos saugojimo kaštams, taip pat duomenų prieigos greičiui. Tokius sprendimus greičiausiai priima ne vien duomenų mokslininkas, tačiau jis gali būti atsakingas už pasirinkimus, kaip dirbti su duomenimis, atsižvelgiant į jų saugojimo būdą.

Štai keletas šiuolaikinių duomenų saugojimo sistemų aspektų, galinčių turėti įtakos šiems pasirinkimams:

**Vietinis saugojimas vs nuotolinis saugojimas vs viešas ar privatus debesų saugojimas**

Vietinis saugojimas reiškia duomenų talpinimą ir valdymą savo įrangoje, pavyzdžiui, serveryje su kietaisiais diskais, kuriuose saugomi duomenys, o nuotolinis saugojimas remiasi įranga, kurios jūs nevaldote, pavyzdžiui, duomenų centru. Viešas debesų saugojimas yra populiarus pasirinkimas, kai nereikia žinoti, kaip ar kur tiksliai saugomi duomenys, o viešas reiškia bendrą infrastruktūrą, kuria naudojasi visi debesų paslaugų vartotojai. Kai kurios organizacijos turi griežtas saugumo politikos taisykles, kurios reikalauja visiškos prieigos prie įrangos, kurioje saugomi duomenys, ir pasirenka privatų debesų saugojimą, kuris teikia savo debesų paslaugas. Apie duomenis debesyse sužinosite daugiau [vėlesnėse pamokose](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/5-Data-Science-In-Cloud).

**Šalti vs karšti duomenys**

Mokant modelius, jums gali prireikti daugiau mokymo duomenų. Jei esate patenkinti savo modeliu, daugiau duomenų bus naudojama modeliui atlikti savo funkciją. Bet kuriuo atveju saugojimo ir prieigos kaštai didės, kai kaupsite daugiau duomenų. Retai naudojamų duomenų, vadinamų šaltais duomenimis, atskyrimas nuo dažnai pasiekiamų karštų duomenų gali būti pigesnis saugojimo sprendimas, naudojant techninę ar programinę įrangą. Jei reikia pasiekti šaltus duomenis, jų gavimas gali užtrukti šiek tiek ilgiau nei karštų duomenų.

### Duomenų valdymas

Dirbdami su duomenimis galite pastebėti, kad kai kuriuos duomenis reikia išvalyti, naudojant pamokoje apie [duomenų paruošimą](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/08-data-preparation) aptartus metodus, kad būtų galima sukurti tikslius modelius. Kai atvyksta nauji duomenys, jiems reikės taikyti tuos pačius metodus, kad būtų išlaikyta kokybės nuoseklumas. Kai kurie projektai apima automatizuoto įrankio naudojimą duomenų valymui, agregavimui ir suspaudimui prieš duomenų perkėlimą į galutinę vietą. „Azure Data Factory“ yra vienas iš tokių įrankių pavyzdžių.

### Duomenų apsauga

Viena pagrindinių duomenų apsaugos tikslų yra užtikrinti, kad tie, kurie dirba su duomenimis, kontroliuotų, kas yra renkama ir kokiame kontekste tai naudojama. Duomenų apsauga apima prieigos apribojimą tik tiems, kuriems jos reikia, vietinių įstatymų ir reglamentų laikymąsi, taip pat etikos standartų laikymąsi, aptartų [etikos pamokoje](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/02-ethics).

Štai keletas dalykų, kuriuos komanda gali atlikti, atsižvelgdama į saugumą:
- Užtikrinti, kad visi duomenys būtų užšifruoti
- Suteikti klientams informaciją apie tai, kaip jų duomenys naudojami
- Pašalinti duomenų prieigą tiems, kurie paliko projektą
- Leisti tik tam tikriems projekto nariams keisti duomenis

## 🚀 Iššūkis

Yra daug duomenų mokslo gyvavimo ciklo versijų, kuriose kiekvienas etapas gali turėti skirtingus pavadinimus ir etapų skaičių, tačiau jose bus tie patys procesai, aptarti šioje pamokoje.

Išnagrinėkite [Komandos duomenų mokslo proceso gyvavimo ciklą](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/lifecycle) ir [Kryžminės pramonės standartinį duomenų gavybos procesą](https://www.datascience-pm.com/crisp-dm-2/). Įvardykite 3 panašumus ir skirtumus tarp jų.

|Komandos duomenų mokslo procesas (TDSP)|Kryžminės pramonės standartinis duomenų gavybos procesas (CRISP-DM)|
|--|--|
|![Komandos duomenų mokslo gyvavimo ciklas](../../../../4-Data-Science-Lifecycle/14-Introduction/images/tdsp-lifecycle2.png) | ![Duomenų mokslo proceso aljanso vaizdas](../../../../4-Data-Science-Lifecycle/14-Introduction/images/CRISP-DM.png) |
| Vaizdas iš [Microsoft](https://docs.microsoft.comazure/architecture/data-science-process/lifecycle) | Vaizdas iš [Duomenų mokslo proceso aljanso](https://www.datascience-pm.com/crisp-dm-2/) |

## [Po paskaitos testą](https://ff-quizzes.netlify.app/en/ds/quiz/27)

## Apžvalga ir savarankiškas mokymasis

Duomenų mokslo gyvavimo ciklo taikymas apima įvairius vaidmenis ir užduotis, kur kai kurie gali būti orientuoti į konkrečias kiekvieno etapo dalis. Komandos duomenų mokslo procesas pateikia keletą išteklių, kurie paaiškina vaidmenų ir užduočių tipus, kuriuos kažkas gali turėti projekte.

* [Komandos duomenų mokslo proceso vaidmenys ir užduotys](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/roles-tasks)
* [Duomenų mokslo užduočių vykdymas: tyrimas, modeliavimas ir diegimas](https://docs.microsoft.com/en-us/azure/architecture/data-science-process/execute-data-science-tasks)

## Užduotis

[Duomenų rinkinio vertinimas](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.