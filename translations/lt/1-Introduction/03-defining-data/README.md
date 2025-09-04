<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1228edf3572afca7d7cdcd938b6b4984",
  "translation_date": "2025-09-04T22:34:57+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "lt"
}
-->
# Apibrėžiant duomenis

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Duomenų apibrėžimas - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Duomenys yra faktai, informacija, stebėjimai ir matavimai, kurie naudojami atradimams daryti ir pagrįstiems sprendimams priimti. Duomenų taškas yra vienetas duomenų rinkinyje, kuris yra duomenų taškų kolekcija. Duomenų rinkiniai gali būti įvairių formatų ir struktūrų, dažniausiai priklausomai nuo jų šaltinio arba vietos, iš kur duomenys buvo gauti. Pavyzdžiui, įmonės mėnesio pajamos gali būti pateiktos skaičiuoklėje, o išmaniojo laikrodžio valandiniai širdies ritmo duomenys gali būti [JSON](https://stackoverflow.com/a/383699) formatu. Duomenų mokslininkai dažnai dirba su skirtingais duomenų tipais viename duomenų rinkinyje.

Ši pamoka skirta duomenų identifikavimui ir klasifikavimui pagal jų savybes ir šaltinius.

## [Prieš paskaitą: testas](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)
## Kaip apibūdinami duomenys

### Pirminiai duomenys
Pirminiai duomenys yra duomenys, kurie gauti iš šaltinio pradinėje būsenoje ir dar nebuvo analizuoti ar organizuoti. Kad būtų galima suprasti, kas vyksta su duomenų rinkiniu, jis turi būti organizuotas į formatą, kurį suprastų žmonės ir technologijos, naudojamos tolimesnei analizei. Duomenų rinkinio struktūra apibūdina, kaip jis organizuotas, ir gali būti klasifikuojama kaip struktūrizuota, nestruktūrizuota ir pusiau struktūrizuota. Šios struktūros tipai skiriasi priklausomai nuo šaltinio, tačiau galiausiai telpa į šias tris kategorijas.

### Kiekybiniai duomenys
Kiekybiniai duomenys yra skaitiniai stebėjimai duomenų rinkinyje, kuriuos paprastai galima analizuoti, matuoti ir naudoti matematiškai. Kai kurie kiekybinių duomenų pavyzdžiai: šalies gyventojų skaičius, žmogaus ūgis ar įmonės ketvirčio pajamos. Su papildoma analize kiekybiniai duomenys galėtų būti naudojami sezoninėms oro kokybės indekso (AQI) tendencijoms atrasti arba numatyti tikimybę, kad darbo dienos piko metu bus eismas.

### Kokybiniai duomenys
Kokybiniai duomenys, dar vadinami kategoriniais duomenimis, yra duomenys, kurių negalima objektyviai išmatuoti, kaip kiekybinių duomenų stebėjimų. Tai paprastai yra įvairūs subjektyvūs duomenys, kurie fiksuoja kažko kokybę, pavyzdžiui, produkto ar proceso. Kartais kokybiniai duomenys yra skaitiniai, tačiau paprastai nenaudojami matematiškai, kaip telefono numeriai ar laiko žymos. Kai kurie kokybinių duomenų pavyzdžiai: vaizdo įrašų komentarai, automobilio markė ir modelis arba artimiausių draugų mėgstamiausia spalva. Kokybiniai duomenys galėtų būti naudojami suprasti, kurie produktai vartotojams patinka labiausiai, arba identifikuoti populiarius raktažodžius darbo paraiškų gyvenimo aprašymuose.

### Struktūrizuoti duomenys
Struktūrizuoti duomenys yra duomenys, kurie organizuoti į eilutes ir stulpelius, kur kiekviena eilutė turi tą patį stulpelių rinkinį. Stulpeliai atspindi tam tikro tipo vertę ir yra identifikuojami pavadinimu, apibūdinančiu, ką vertė reiškia, o eilutės turi faktines vertes. Stulpeliai dažnai turi specifines taisykles ar apribojimus vertėms, kad būtų užtikrinta, jog vertės tiksliai atspindi stulpelį. Pavyzdžiui, įsivaizduokite klientų skaičiuoklę, kur kiekviena eilutė turi turėti telefono numerį, o telefono numeriai niekada neturi turėti abėcėlinių simbolių. Gali būti taikomos taisyklės, kad telefono numerio stulpelis niekada nebūtų tuščias ir turėtų tik skaičius.

Struktūrizuotų duomenų privalumas yra tas, kad jie gali būti organizuoti taip, kad būtų susiję su kitais struktūrizuotais duomenimis. Tačiau, kadangi duomenys sukurti būti organizuoti specifiniu būdu, jų bendros struktūros keitimas gali pareikalauti daug pastangų. Pavyzdžiui, pridėti el. pašto stulpelį klientų skaičiuoklėje, kuris negali būti tuščias, reiškia, kad reikės sugalvoti, kaip pridėti šias vertes esamoms klientų eilutėms duomenų rinkinyje.

Struktūrizuotų duomenų pavyzdžiai: skaičiuoklės, reliacinės duomenų bazės, telefono numeriai, banko išrašai.

### Nestruktūrizuoti duomenys
Nestruktūrizuoti duomenys paprastai negali būti suskirstyti į eilutes ar stulpelius ir neturi formato ar taisyklių rinkinio, kurio reikia laikytis. Kadangi nestruktūrizuoti duomenys turi mažiau apribojimų savo struktūrai, lengviau pridėti naują informaciją, palyginti su struktūrizuotu duomenų rinkiniu. Jei jutiklis, fiksuojantis duomenis apie barometrinį slėgį kas 2 minutes, gauna atnaujinimą, leidžiantį matuoti ir registruoti temperatūrą, nereikia keisti esamų duomenų, jei jie yra nestruktūrizuoti. Tačiau tai gali užtrukti ilgiau analizuojant ar tiriant tokius duomenis. Pavyzdžiui, mokslininkas, norintis rasti vidutinę temperatūrą praėjusį mėnesį iš jutiklio duomenų, gali pastebėti, kad jutiklis kai kuriuose duomenyse įrašė "e", kad pažymėtų, jog jis buvo sugedęs, o ne įprastą skaičių, todėl duomenys yra neišsamūs.

Nestruktūrizuotų duomenų pavyzdžiai: tekstiniai failai, tekstinės žinutės, vaizdo failai.

### Pusiau struktūrizuoti duomenys
Pusiau struktūrizuoti duomenys turi savybių, kurios daro juos struktūrizuotų ir nestruktūrizuotų duomenų deriniu. Jie paprastai neatitinka eilutėms ir stulpeliams būdingo formato, tačiau yra organizuoti taip, kad laikomi struktūrizuotais ir gali laikytis fiksuoto formato ar taisyklių rinkinio. Struktūra skiriasi priklausomai nuo šaltinio, pavyzdžiui, nuo gerai apibrėžtos hierarchijos iki lankstesnės, leidžiančios lengvai integruoti naują informaciją. Metaduomenys yra indikatoriai, padedantys nuspręsti, kaip duomenys organizuojami ir saugomi, ir turi įvairius pavadinimus, priklausomai nuo duomenų tipo. Kai kurie dažni metaduomenų pavadinimai yra žymos, elementai, subjektai ir atributai. Pavyzdžiui, tipinis el. laiškas turės temą, turinį ir gavėjų rinkinį, ir gali būti organizuotas pagal tai, kas ar kada jis buvo išsiųstas.

Pusiau struktūrizuotų duomenų pavyzdžiai: HTML, CSV failai, JavaScript Object Notation (JSON).

## Duomenų šaltiniai

Duomenų šaltinis yra pradinė vieta, kurioje duomenys buvo sugeneruoti arba kur jie "gyvena", ir skiriasi priklausomai nuo to, kaip ir kada jie buvo surinkti. Duomenys, sugeneruoti jų vartotojų, vadinami pirminiais duomenimis, o antriniai duomenys gaunami iš šaltinio, kuris surinko duomenis bendram naudojimui. Pavyzdžiui, mokslininkų grupė, renkantys stebėjimus atogrąžų miške, būtų laikomi pirminiais, o jei jie nuspręstų pasidalinti jais su kitais mokslininkais, tai būtų laikoma antriniais tiems, kurie juos naudoja.

Duomenų bazės yra dažnas šaltinis ir remiasi duomenų bazių valdymo sistema, kad talpintų ir prižiūrėtų duomenis, kur vartotojai naudoja komandas, vadinamas užklausomis, duomenims tyrinėti. Failai kaip duomenų šaltiniai gali būti garso, vaizdo ir vaizdo failai, taip pat skaičiuoklės, tokios kaip Excel. Interneto šaltiniai yra dažna vieta duomenims talpinti, kur galima rasti tiek duomenų bazių, tiek failų. Programų programavimo sąsajos, dar vadinamos API, leidžia programuotojams kurti būdus dalintis duomenimis su išoriniais vartotojais per internetą, o procesas, vadinamas interneto duomenų išgavimo, ištraukia duomenis iš tinklalapio. [Pamokos apie darbą su duomenimis](../../../../../../../../../2-Working-With-Data) yra skirtos tam, kaip naudoti įvairius duomenų šaltinius.

## Išvada

Šioje pamokoje sužinojome:

- Kas yra duomenys
- Kaip apibūdinami duomenys
- Kaip duomenys klasifikuojami ir kategorizuojami
- Kur galima rasti duomenis

## 🚀 Iššūkis

Kaggle yra puikus atvirų duomenų rinkinių šaltinis. Naudokite [duomenų rinkinių paieškos įrankį](https://www.kaggle.com/datasets), kad surastumėte įdomių duomenų rinkinių ir klasifikuokite 3–5 rinkinius pagal šiuos kriterijus:

- Ar duomenys yra kiekybiniai ar kokybiniai?
- Ar duomenys yra struktūrizuoti, nestruktūrizuoti ar pusiau struktūrizuoti?

## [Po paskaitos: testas](https://ff-quizzes.netlify.app/en/ds/)

## Apžvalga ir savarankiškas mokymasis

- Šis Microsoft Learn modulis, pavadintas [Klasifikuokite savo duomenis](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data), turi išsamų struktūrizuotų, pusiau struktūrizuotų ir nestruktūrizuotų duomenų aprašymą.

## Užduotis

[Klasifikuoti duomenų rinkinius](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.