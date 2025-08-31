<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "356d12cffc3125db133a2d27b827a745",
  "translation_date": "2025-08-31T05:58:00+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "lt"
}
-->
# Duomenų Apibrėžimas

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Duomenų apibrėžimas - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Duomenys – tai faktai, informacija, stebėjimai ir matavimai, naudojami atradimams daryti ir pagrįstiems sprendimams priimti. Duomenų taškas yra vienas duomenų vienetas duomenų rinkinyje, kuris yra duomenų taškų kolekcija. Duomenų rinkiniai gali būti įvairių formatų ir struktūrų, dažniausiai priklausomai nuo jų šaltinio arba vietos, iš kur jie gauti. Pavyzdžiui, įmonės mėnesinės pajamos gali būti pateiktos skaičiuoklėje, o išmaniojo laikrodžio valandinis širdies ritmo duomenys gali būti [JSON](https://stackoverflow.com/a/383699) formatu. Duomenų mokslininkai dažnai dirba su skirtingų tipų duomenimis viename duomenų rinkinyje.

Ši pamoka skirta duomenų identifikavimui ir klasifikavimui pagal jų savybes ir šaltinius.

## [Prieš paskaitą: Klausimynas](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)
## Kaip apibūdinami duomenys

### Pirminiai duomenys
Pirminiai duomenys yra duomenys, kurie gaunami iš šaltinio pradinėje būsenoje ir dar nėra analizuoti ar organizuoti. Kad būtų galima suprasti, kas vyksta su duomenų rinkiniu, jis turi būti organizuotas į formatą, kurį suprastų tiek žmonės, tiek technologijos, naudojamos tolesnei analizei. Duomenų rinkinio struktūra apibūdina, kaip jis organizuotas, ir gali būti klasifikuojama kaip struktūrizuota, nestruktūrizuota arba pusiau struktūrizuota. Šios struktūros tipai skirsis priklausomai nuo šaltinio, tačiau galiausiai atitiks vieną iš šių trijų kategorijų.

### Kiekybiniai duomenys
Kiekybiniai duomenys yra skaitiniai stebėjimai duomenų rinkinyje, kuriuos paprastai galima analizuoti, matuoti ir naudoti matematiškai. Kai kurie kiekybinių duomenų pavyzdžiai: šalies gyventojų skaičius, žmogaus ūgis ar įmonės ketvirčio pajamos. Atlikus papildomą analizę, kiekybiniai duomenys galėtų būti naudojami sezoninėms oro kokybės indekso (AQI) tendencijoms nustatyti arba spūsties tikimybei darbo dienos piko metu įvertinti.

### Kokybiniai duomenys
Kokybiniai duomenys, dar vadinami kategoriniais duomenimis, yra duomenys, kurių negalima objektyviai išmatuoti, kaip kiekybinių duomenų stebėjimų. Tai dažniausiai įvairių formatų subjektyvūs duomenys, kurie atspindi kažko kokybę, pavyzdžiui, produkto ar proceso. Kartais kokybiniai duomenys yra skaitiniai, tačiau paprastai nenaudojami matematiškai, pavyzdžiui, telefono numeriai ar laiko žymos. Kai kurie kokybinių duomenų pavyzdžiai: vaizdo įrašų komentarai, automobilio markė ir modelis arba artimiausių draugų mėgstamiausia spalva. Kokybiniai duomenys galėtų būti naudojami norint suprasti, kurie produktai vartotojams patinka labiausiai, arba populiariems raktažodžiams darbo paraiškų gyvenimo aprašymuose nustatyti.

### Struktūrizuoti duomenys
Struktūrizuoti duomenys yra duomenys, organizuoti eilutėmis ir stulpeliais, kur kiekviena eilutė turi tą patį stulpelių rinkinį. Stulpeliai atspindi tam tikro tipo reikšmę ir bus identifikuojami pavadinimu, apibūdinančiu, ką ta reikšmė reiškia, o eilutėse pateikiamos faktinės reikšmės. Stulpeliai dažnai turi specifinį taisyklių ar apribojimų rinkinį, kad užtikrintų, jog reikšmės tiksliai atspindi stulpelį. Pavyzdžiui, įsivaizduokite klientų skaičiuoklę, kur kiekviena eilutė privalo turėti telefono numerį, o telefono numeriai niekada neturi turėti raidžių. Gali būti taikomos taisyklės, kad telefono numerio stulpelis niekada nebūtų tuščias ir turėtų tik skaičius.

Struktūrizuotų duomenų privalumas yra tas, kad jie gali būti organizuoti taip, kad būtų susiję su kitais struktūrizuotais duomenimis. Tačiau dėl to, kad duomenys sukurti būti organizuoti konkrečiu būdu, jų bendros struktūros keitimas gali pareikalauti daug pastangų. Pavyzdžiui, pridėjus el. pašto stulpelį klientų skaičiuoklėje, kuris negali būti tuščias, reikės nuspręsti, kaip pridėti šias reikšmes prie esamų klientų eilučių duomenų rinkinyje.

Struktūrizuotų duomenų pavyzdžiai: skaičiuoklės, reliacinės duomenų bazės, telefono numeriai, banko išrašai.

### Nestruktūrizuoti duomenys
Nestruktūrizuoti duomenys paprastai negali būti suskirstyti į eilutes ar stulpelius ir neturi formato ar taisyklių rinkinio, kurio reikėtų laikytis. Kadangi nestruktūrizuoti duomenys turi mažiau apribojimų savo struktūrai, juos lengviau papildyti nauja informacija, palyginti su struktūrizuotu duomenų rinkiniu. Jei jutiklis, fiksuojantis barometrinį slėgį kas 2 minutes, gauna atnaujinimą, leidžiantį jam matuoti ir registruoti temperatūrą, nereikia keisti esamų duomenų, jei jie yra nestruktūrizuoti. Tačiau tai gali apsunkinti šių duomenų analizę ar tyrimą. Pavyzdžiui, mokslininkas, norintis rasti vidutinę praėjusio mėnesio temperatūrą iš jutiklio duomenų, gali pastebėti, kad jutiklis kai kuriuose įrašuose užfiksavo „e“, nurodydamas, kad jis buvo sugedęs, o tai reiškia, kad duomenys yra neišsamūs.

Nestruktūrizuotų duomenų pavyzdžiai: tekstiniai failai, tekstinės žinutės, vaizdo failai.

### Pusiau struktūrizuoti
Pusiau struktūrizuoti duomenys turi savybių, dėl kurių jie yra struktūrizuotų ir nestruktūrizuotų duomenų derinys. Jie paprastai neatitinka eilučių ir stulpelių formato, tačiau yra organizuoti taip, kad laikomi struktūrizuotais ir gali laikytis fiksuoto formato ar taisyklių rinkinio. Struktūra skirsis priklausomai nuo šaltinio, pavyzdžiui, nuo gerai apibrėžtos hierarchijos iki lankstesnės, leidžiančios lengvai integruoti naują informaciją. Metaduomenys yra indikatoriai, padedantys nuspręsti, kaip duomenys organizuojami ir saugomi, ir turės įvairius pavadinimus, priklausomai nuo duomenų tipo. Kai kurie įprasti metaduomenų pavadinimai yra žymos, elementai, subjektai ir atributai. Pavyzdžiui, tipinis el. laiškas turės temą, turinį ir gavėjų rinkinį ir gali būti organizuotas pagal tai, kas ar kada jį išsiuntė.

Pusiau struktūrizuotų duomenų pavyzdžiai: HTML, CSV failai, JavaScript Object Notation (JSON).

## Duomenų šaltiniai

Duomenų šaltinis yra pradinė vieta, kurioje duomenys buvo sugeneruoti arba „gyvena“, ir skirsis priklausomai nuo to, kaip ir kada jie buvo surinkti. Duomenys, sugeneruoti jų naudotojų, vadinami pirminiais duomenimis, o antriniai duomenys gaunami iš šaltinio, kuris surinko duomenis bendram naudojimui. Pavyzdžiui, mokslininkų grupė, renkantys stebėjimus atogrąžų miške, būtų laikomi pirminiais, o jei jie nuspręstų pasidalinti jais su kitais mokslininkais, tai būtų laikoma antriniais tiems, kurie juos naudoja.

Duomenų bazės yra dažnas šaltinis ir remiasi duomenų bazių valdymo sistema, kuri talpina ir prižiūri duomenis, kur naudotojai naudoja užklausas duomenims tyrinėti. Failai kaip duomenų šaltiniai gali būti garso, vaizdo ir vaizdo failai, taip pat skaičiuoklės, tokios kaip Excel. Interneto šaltiniai yra dažna vieta duomenims talpinti, kur galima rasti tiek duomenų bazių, tiek failų. Programų programavimo sąsajos, dar vadinamos API, leidžia programuotojams kurti būdus dalintis duomenimis su išoriniais naudotojais per internetą, o interneto duomenų nuskaitymas išgauna duomenis iš tinklalapio. [Pamokos apie darbą su duomenimis](../../../../../../../../../2-Working-With-Data) yra skirtos įvairių duomenų šaltinių naudojimui.

## Išvada

Šioje pamokoje sužinojome:

- Kas yra duomenys
- Kaip apibūdinami duomenys
- Kaip duomenys klasifikuojami ir kategorizuojami
- Kur galima rasti duomenis

## 🚀 Iššūkis

Kaggle yra puikus atvirų duomenų rinkinių šaltinis. Naudokite [duomenų rinkinių paieškos įrankį](https://www.kaggle.com/datasets), kad rastumėte įdomių duomenų rinkinių ir klasifikuotumėte 3–5 rinkinius pagal šiuos kriterijus:

- Ar duomenys yra kiekybiniai ar kokybiniai?
- Ar duomenys yra struktūrizuoti, nestruktūrizuoti ar pusiau struktūrizuoti?

## [Po paskaitos: Klausimynas](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/5)

## Peržiūra ir savarankiškas mokymasis

- Šis Microsoft Learn modulis, pavadintas [Klasifikuokite savo duomenis](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data), pateikia išsamų struktūrizuotų, pusiau struktūrizuotų ir nestruktūrizuotų duomenų suskirstymą.

## Užduotis

[Klasifikuoti duomenų rinkinius](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipiame dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, kylančius dėl šio vertimo naudojimo.