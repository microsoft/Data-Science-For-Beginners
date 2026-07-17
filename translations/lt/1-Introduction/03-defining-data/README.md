# Duomenų apibrėžimas

|![ Sketchnote autorius [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Duomenų apibrėžimas - _Sketchnote autorius [@nitya](https://twitter.com/nitya)_ |

Duomenys yra faktai, informacija, stebėjimai ir matavimai, kurie naudojami atradimams padaryti ir pagrįstiems sprendimams priimti. Duomenų taškas – tai vienetas duomenų rinkinyje, kuris yra duomenų taškų rinkinys. Duomenų rinkiniai gali būti įvairių formatų ir struktūrų, paprastai priklausant nuo jų šaltinio arba nuo to, iš kur atėjo duomenys. Pavyzdžiui, įmonės mėnesinės pajamos gali būti skaičiuoklėje, o laikrodžio širdies ritmo duomenys per valandą gali būti [JSON](https://stackoverflow.com/a/383699) formatu. Duomenų mokslininkams dažnai tenka dirbti su skirtingų tipų duomenimis viename duomenų rinkinyje.

Ši pamoka orientuota į duomenų identifikavimą ir klasifikavimą pagal jų savybes ir šaltinius.

## [Priešpaskaitos testas](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Kaip aprašomi duomenys

### Žali duomenys
Žali duomenys yra duomenys, gauti tiesiai iš jų šaltinio pradinėje būsenoje, kurie nėra analizėti ar organizuoti. Norint suprasti, kas vyksta su duomenų rinkiniu, jį reikia suorganizuoti į tokį formatą, kurį suprastų žmonės ir technologijos, kurias jie gali naudoti tolesnei analizei. Duomenų rinkinio struktūra apibūdina, kaip jis yra organizuotas, ir gali būti klasifikuojama kaip struktūrizuota, nestruktūrizuota ir pusiau struktūrizuota. Šie struktūros tipai priklausys nuo šaltinio, bet galutiniame rezultate telpa į šias tris kategorijas.

### Kiekybiniai duomenys
Kiekybiniai duomenys yra skaitinės stebėsenos duomenų rinkinyje ir paprastai gali būti analizuojami, matuojami ir naudojami matematiškai. Pavyzdžiai: šalies gyventojų skaičius, asmens ūgis arba įmonės ketvirčio pajamos. Papildoma analize kiekybiniai duomenys gali būti naudojami sezoniniams Oro kokybės indekso (AQI) tendencijoms atrasti arba įvertinti eismo srauto piko valandas įprastą darbo dieną.

### Kokybiniai duomenys
Kokybiniai duomenys, dar vadinami kategoriniais, yra duomenys, kurių negalima objektyviai išmatuoti, kaip kiekybinius duomenis. Tai paprastai yra įvairios subjektyvios informacijos formos, kurios aprašo kažką kokybiškai, pavyzdžiui, produktą ar procesą. Kartais kokybiniai duomenys yra skaitiniai, bet paprastai nėra naudojami matematiškai, kaip telefono numeriai ar laiko žymos. Pavyzdžiai: vaizdo komentarai, automobilio markė ir modelis arba artimiausių draugų mėgstamiausia spalva. Kokybiniai duomenys gali padėti suprasti, kurie produktai vartotojams patinka labiausiai, arba identifikuoti populiariausius raktinius žodžius darbo paraiškų gyvenimo aprašymuose.

### Struktūrizuoti duomenys
Struktūrizuoti duomenys yra organizuoti į eilutes ir stulpelius, kur kiekviena eilutė turi tą patį stulpelių rinkinį. Stulpeliai rodo tam tikro tipo reikšmę ir būna pavadinti, apibūdinant ką ta reikšmė reiškia, o eilutės talpina faktines reikšmes. Stulpelių reikšmėms dažnai taikomos specifinės taisyklės ar apribojimai, kad užtikrintų reikšmių tikslumą. Pavyzdžiui, klientų skaičiuoklėje kiekviena eilutė turi turėti telefono numerį, kuriame nėra raidžių. Gali būti taisyklės telefone, kad jis niekada nebūtų tuščias ir turėtų tik skaitmenis.

Vienas struktūrizuotų duomenų privalumų yra tas, kad jie gali būti susieti su kitais struktūrizuotais duomenimis. Tačiau, kadangi duomenys sukurti taip, kad būtų organizuoti pagal tam tikrą tvarką, bendri jos struktūros pakeitimai gali būti sudėtingi. Pavyzdžiui, pridėti el. pašto stulpelį, kuris negali būti tuščias klientų skaičiuoklėje reiškia, kad reikės spręsti, kaip šias reikšmes pridėti prie esamų duomenų eilučių.

Struktūrizuotų duomenų pavyzdžiai: skaičiuoklės, reliacinės duomenų bazės, telefono numeriai, banko išrašai

### Nestruktūrizuoti duomenys
Nestruktūrizuoti duomenys paprastai nėra suskirstyti į eilutes ar stulpelius ir neturi nustatyto formato ar taisyklių. Kadangi nestruktūrizuoti duomenys turi mažiau apribojimų, juos lengviau papildyti nauja informacija, palyginus su struktūrizuotu duomenų rinkiniu. Pavyzdžiui, jei jutiklis matuoja barometrinį slėgį kas 2 minutes ir gauna atnaujinimą, leidžiantį jame matuoti ir temperatūrą, tai nėra būtina keisti esamus duomenis, jei jie nestruktūrizuoti. Tačiau tai gali pailginti tokio duomenų analizės ar tyrimo laiką. Pavyzdžiui, mokslininkas, norintis apskaičiuoti vidutinę ankstesnio mėnesio temperatūrą pagal jutiklio duomenis, atranda, kad jutiklis kai kur įrašė „e“ žymėdamas, kad jis buvo sugadintas, o ne skaitinę reikšmę, tad duomenys yra neišsamūs.

Nestruktūrizuotų duomenų pavyzdžiai: teksto failai, žinutės, vaizdo įrašai

### Pusiau struktūrizuoti duomenys
Pusiau struktūrizuoti duomenys turi savybių, kurios sudaro struktūrizuotų ir nestruktūrizuotų duomenų derinį. Jie paprastai nesilaiko eilučių ir stulpelių formato, bet yra organizuoti taip, kad laikomi struktūrizuotais ir gali turėti nustatytą formatą ar taisyklių rinkinį. Struktūra skiriasi priklausomai nuo šaltinių nuo aiškiai apibrėžtos hierarchijos iki lankstesnės, leidžiančios lengvai integruoti naują informaciją. Metaduomenys yra indikatoriai, padedantys nuspręsti, kaip duomenys organizuojami ir saugomi, jų pavadinimai skiriasi priklausomai nuo duomenų tipo. Dažniausi metaduomenų pavadinimai yra žymos, elementai, objektai ir atributai. Pavyzdžiui, tipinė el. laiško žinutė turi temą, turinį ir gavėjų sąrašą, kurį galima suorganizuoti pagal siuntėją ar laiką.

Pusiau struktūrizuotų duomenų pavyzdžiai: HTML, CSV failai, JavaScript objektų žymėjimas (JSON)

## Duomenų šaltiniai

Duomenų šaltinis yra pradinė vieta, kur duomenis sugeneravo arba kur jie „gyvena“, ir priklauso nuo to, kaip ir kada jie surinkti. Duomenys, sugeneruoti paties naudotojo (naudotojų), vadinami pirminiais, o antriniai duomenys yra iš šaltinio, kuris rinko duomenis bendram naudojimui. Pavyzdžiui, grupė mokslininkų, stebinčių lietaus miško duomenis, būtų laikomi pirminiais, o jei jie pasidalins su kitais mokslininkais, tai bus antriniai naujiems naudotojams.

Duomenų bazės yra įprastas šaltinis ir remiasi duomenų bazių valdymo sistema, kurioje naudotojai naudoja užklausas duomenų tyrimui. Failai kaip duomenų šaltiniai gali būti garso, vaizdo ir vaizdo įrašų failai, taip pat skaičiuoklės, tokios kaip Excel. Interneto šaltiniai yra dažna vieta duomenų talpinimui, kur galima rasti duomenų bazes ir failus. Programavimo sąsajos (APIs) leidžia programuotojams kurti būdus dalintis duomenimis su išoriniais naudotojais per internetą, o interneto duomenų nuskaitymas (web scraping) ištraukia duomenis iš tinklalapio. [Pamokos Darbas su Duomenimis](../../../../../../../../../2-Working-With-Data) orientuotos į įvairių duomenų šaltinių naudojimą.

## Išvada

Šioje pamokoje sužinojome:

- Kas yra duomenys
- Kaip aprašomi duomenys
- Kaip klasifikuojami ir kategorizuojami duomenys
- Kur galima rasti duomenų

## 🚀 Iššūkis

Kaggle yra puikus atvirų duomenų šaltinis. Naudokite [duomenų rinkinių paieškos įrankį](https://www.kaggle.com/datasets), kad surastumėte įdomių duomenų rinkinių ir klasifikuokite 3–5 duomenų rinkinius pagal šiuos kriterijus:

- Ar duomenys yra kiekybiniai ar kokybiniai?
- Ar duomenys yra struktūrizuoti, nestruktūrizuoti ar pusiau struktūrizuoti?

## [Po paskaitos testas](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Peržiūra ir savarankiškas mokymasis

- Ši Microsoft Learn dalis, pavadinta [Duomenų formatų identifikacija](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text), aprašo struktūrizuotus, pusiau struktūrizuotus ir nestruktūrizuotus duomenis.

## Užduotis

[Duomenų rinkinių klasifikavimas](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->