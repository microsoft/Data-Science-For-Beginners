<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "12339119c0165da569a93ddba05f9339",
  "translation_date": "2025-09-05T16:15:34+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "lt"
}
-->
# Duomenų Apibrėžimas

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Duomenų apibrėžimas - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Duomenys – tai faktai, informacija, stebėjimai ir matavimai, naudojami atradimams daryti ir pagrįstiems sprendimams priimti. Duomenų taškas yra vienas duomenų vienetas duomenų rinkinyje, kuris yra duomenų taškų kolekcija. Duomenų rinkiniai gali būti įvairių formatų ir struktūrų, dažniausiai priklausomai nuo jų šaltinio arba vietos, iš kur jie buvo gauti. Pavyzdžiui, įmonės mėnesinės pajamos gali būti pateiktos skaičiuoklėje, o išmaniojo laikrodžio valandinis širdies ritmo duomenys gali būti [JSON](https://stackoverflow.com/a/383699) formatu. Duomenų mokslininkai dažnai dirba su skirtingų tipų duomenimis viename duomenų rinkinyje.

Ši pamoka skirta duomenų identifikavimui ir klasifikavimui pagal jų savybes ir šaltinius.

## [Prieš paskaitą: testas](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Kaip apibūdinami duomenys

### Pirminiai duomenys
Pirminiai duomenys yra duomenys, kurie gaunami tiesiai iš šaltinio savo pradinėje būsenoje ir dar nėra analizuoti ar organizuoti. Kad būtų galima suprasti, kas vyksta su duomenų rinkiniu, jis turi būti organizuotas į formatą, kurį suprastų tiek žmonės, tiek technologijos, naudojamos tolesnei analizei. Duomenų rinkinio struktūra apibūdina, kaip jis yra organizuotas, ir gali būti klasifikuojama kaip struktūrizuota, nestruktūrizuota arba pusiau struktūrizuota. Šios struktūros tipai skirsis priklausomai nuo šaltinio, tačiau galiausiai atitiks vieną iš šių trijų kategorijų.

### Kiekybiniai duomenys
Kiekybiniai duomenys yra skaitiniai stebėjimai duomenų rinkinyje, kuriuos paprastai galima analizuoti, matuoti ir naudoti matematiškai. Kai kurie kiekybinių duomenų pavyzdžiai: šalies gyventojų skaičius, žmogaus ūgis ar įmonės ketvirčio pajamos. Atlikus papildomą analizę, kiekybiniai duomenys galėtų būti naudojami sezoninėms oro kokybės indekso (AQI) tendencijoms nustatyti arba spėti, kokia tikimybė, kad darbo dienos piko metu bus eismas.

### Kokybiniai duomenys
Kokybiniai duomenys, dar vadinami kategoriniais duomenimis, yra duomenys, kurių negalima objektyviai išmatuoti, kaip kiekybinių duomenų stebėjimų. Tai dažniausiai įvairių formatų subjektyvūs duomenys, kurie atspindi kažko kokybę, pavyzdžiui, produkto ar proceso. Kartais kokybiniai duomenys yra skaitiniai, tačiau paprastai nenaudojami matematiškai, pavyzdžiui, telefono numeriai ar laiko žymos. Kai kurie kokybinių duomenų pavyzdžiai: vaizdo įrašų komentarai, automobilio markė ir modelis arba artimiausių draugų mėgstamiausia spalva. Kokybiniai duomenys galėtų būti naudojami norint suprasti, kurie produktai vartotojams patinka labiausiai, arba nustatyti populiarius raktinius žodžius darbo paraiškų gyvenimo aprašymuose.

### Struktūrizuoti duomenys
Struktūrizuoti duomenys yra organizuoti į eilutes ir stulpelius, kur kiekviena eilutė turi tą patį stulpelių rinkinį. Stulpeliai atspindi tam tikro tipo reikšmę ir bus identifikuojami pavadinimu, apibūdinančiu, ką ta reikšmė reiškia, o eilutės turės faktines reikšmes. Stulpeliai dažnai turi specifines taisykles ar apribojimus reikšmėms, kad būtų užtikrinta, jog reikšmės tiksliai atspindi stulpelį. Pavyzdžiui, įsivaizduokite klientų skaičiuoklę, kur kiekviena eilutė privalo turėti telefono numerį, o telefono numeriai niekada neturi raidžių. Gali būti taikomos taisyklės, užtikrinančios, kad telefono numerio stulpelis niekada nebūtų tuščias ir jame būtų tik skaičiai.

Struktūrizuotų duomenų privalumas yra tas, kad jie gali būti organizuoti taip, kad būtų susiję su kitais struktūrizuotais duomenimis. Tačiau dėl to, kad duomenys yra sukurti būti organizuoti konkrečiu būdu, jų bendros struktūros keitimas gali pareikalauti daug pastangų. Pavyzdžiui, pridėjus el. pašto stulpelį klientų skaičiuoklėje, kuris negali būti tuščias, reikės nuspręsti, kaip pridėti šias reikšmes prie esamų klientų eilučių duomenų rinkinyje.

Struktūrizuotų duomenų pavyzdžiai: skaičiuoklės, reliacinės duomenų bazės, telefono numeriai, banko išrašai.

### Nestruktūrizuoti duomenys
Nestruktūrizuoti duomenys paprastai negali būti suskirstyti į eilutes ar stulpelius ir neturi formato ar taisyklių rinkinio, kurio reikėtų laikytis. Kadangi nestruktūrizuoti duomenys turi mažiau apribojimų savo struktūrai, juos lengviau papildyti nauja informacija, palyginti su struktūrizuotu duomenų rinkiniu. Jei jutiklis, fiksuojantis barometrinį slėgį kas 2 minutes, gauna atnaujinimą, leidžiantį matuoti ir registruoti temperatūrą, nereikia keisti esamų duomenų, jei jie yra nestruktūrizuoti. Tačiau tai gali apsunkinti šių duomenų analizę ar tyrimą. Pavyzdžiui, mokslininkas, norintis rasti vidutinę praėjusio mėnesio temperatūrą pagal jutiklio duomenis, gali pastebėti, kad jutiklis kai kuriuose įrašuose užfiksavo „e“, nurodydamas, kad jis buvo sugedęs, o tai reiškia, kad duomenys yra neišsamūs.

Nestruktūrizuotų duomenų pavyzdžiai: tekstiniai failai, tekstinės žinutės, vaizdo failai.

### Pusiau struktūrizuoti duomenys
Pusiau struktūrizuoti duomenys turi savybių, dėl kurių jie yra struktūrizuotų ir nestruktūrizuotų duomenų derinys. Jie paprastai neatitinka eilučių ir stulpelių formato, tačiau yra organizuoti taip, kad būtų laikomi struktūrizuotais ir gali laikytis nustatyto formato ar taisyklių rinkinio. Struktūra skirsis priklausomai nuo šaltinio, pavyzdžiui, nuo gerai apibrėžtos hierarchijos iki lankstesnės, leidžiančios lengvai integruoti naują informaciją. Metaduomenys yra indikatoriai, padedantys nuspręsti, kaip duomenys yra organizuoti ir saugomi, ir turės įvairius pavadinimus, priklausomai nuo duomenų tipo. Kai kurie įprasti metaduomenų pavadinimai yra žymos, elementai, subjektai ir atributai. Pavyzdžiui, tipinė el. laiško žinutė turės temą, turinį ir gavėjų rinkinį ir gali būti organizuota pagal tai, kas ar kada ją išsiuntė.

Pusiau struktūrizuotų duomenų pavyzdžiai: HTML, CSV failai, JavaScript Object Notation (JSON).

## Duomenų šaltiniai

Duomenų šaltinis yra pradinė vieta, kurioje duomenys buvo sugeneruoti arba „gyvena“, ir skirsis priklausomai nuo to, kaip ir kada jie buvo surinkti. Duomenys, sugeneruoti jų naudotojų, vadinami pirminiais duomenimis, o antriniai duomenys gaunami iš šaltinio, kuris surinko duomenis bendram naudojimui. Pavyzdžiui, mokslininkų grupė, renkantys stebėjimus atogrąžų miške, būtų laikomi pirminiais, o jei jie nuspręstų pasidalinti šiais duomenimis su kitais mokslininkais, jie būtų laikomi antriniais tiems, kurie juos naudoja.

Duomenų bazės yra dažnas šaltinis ir remiasi duomenų bazių valdymo sistema, kuri talpina ir prižiūri duomenis, kur naudotojai naudoja užklausas duomenims tyrinėti. Failai kaip duomenų šaltiniai gali būti garso, vaizdo ir vaizdo failai, taip pat skaičiuoklės, tokios kaip Excel. Interneto šaltiniai yra dažna vieta duomenims talpinti, kur galima rasti tiek duomenų bazių, tiek failų. Programų programavimo sąsajos, dar žinomos kaip API, leidžia programuotojams kurti būdus dalintis duomenimis su išoriniais naudotojais per internetą, o interneto duomenų nuskaitymas išgauna duomenis iš tinklalapio. [Pamokos apie darbą su duomenimis](../../../../../../../../../2-Working-With-Data) yra skirtos įvairių duomenų šaltinių naudojimui.

## Išvada

Šioje pamokoje sužinojome:

- Kas yra duomenys
- Kaip apibūdinami duomenys
- Kaip duomenys klasifikuojami ir kategorizuojami
- Kur galima rasti duomenis

## 🚀 Iššūkis

Kaggle yra puikus atvirų duomenų rinkinių šaltinis. Naudokite [duomenų rinkinių paieškos įrankį](https://www.kaggle.com/datasets), kad rastumėte įdomių duomenų rinkinių ir klasifikuokite 3–5 rinkinius pagal šiuos kriterijus:

- Ar duomenys yra kiekybiniai ar kokybiniai?
- Ar duomenys yra struktūrizuoti, nestruktūrizuoti ar pusiau struktūrizuoti?

## [Po paskaitos: testas](https://ff-quizzes.netlify.app/en/ds/quiz/5)

## Peržiūra ir savarankiškas mokymasis

- Šis „Microsoft Learn“ modulis, pavadintas [Klasifikuokite savo duomenis](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data), išsamiai aprašo struktūrizuotus, pusiau struktūrizuotus ir nestruktūrizuotus duomenis.

## Užduotis

[Klasifikuoti duomenų rinkinius](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.