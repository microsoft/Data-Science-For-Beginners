<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11b166fbcb7eaf82308cdc24b562f687",
  "translation_date": "2025-09-04T22:26:39+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "lt"
}
-->
# Darbas su duomenimis: Reliacinės duomenų bazės

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Darbas su duomenimis: Reliacinės duomenų bazės - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Tikėtina, kad anksčiau esate naudoję skaičiuoklę informacijai saugoti. Turėjote eilučių ir stulpelių rinkinį, kur eilutės turėjo informaciją (arba duomenis), o stulpeliai apibūdino tą informaciją (kartais vadinamą metaduomenimis). Reliacinė duomenų bazė yra sukurta remiantis šiuo pagrindiniu principu – lentelėmis su stulpeliais ir eilutėmis, leidžiančiomis informaciją paskirstyti per kelias lenteles. Tai suteikia galimybę dirbti su sudėtingesniais duomenimis, išvengti dubliavimo ir turėti lankstumo tyrinėjant duomenis. Pažvelkime į reliacinės duomenų bazės koncepcijas.

## [Prieš paskaitą: testas](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Viskas prasideda nuo lentelių

Reliacinės duomenų bazės pagrindas yra lentelės. Kaip ir skaičiuoklėje, lentelė yra stulpelių ir eilučių rinkinys. Eilutėse yra duomenys arba informacija, su kuria norime dirbti, pavyzdžiui, miesto pavadinimas ar kritulių kiekis. Stulpeliai apibūdina saugomus duomenis.

Pradėkime tyrinėjimą sukurdami lentelę, kurioje saugosime informaciją apie miestus. Galime pradėti nuo jų pavadinimo ir šalies. Tai galėtume saugoti lentelėje taip:

| Miestas  | Šalis          |
| -------- | -------------- |
| Tokijas  | Japonija       |
| Atlanta  | Jungtinės Valstijos |
| Oklendas | Naujoji Zelandija |

Atkreipkite dėmesį, kad stulpelių pavadinimai **miestas**, **šalis** ir **populiacija** apibūdina saugomus duomenis, o kiekviena eilutė pateikia informaciją apie vieną miestą.

## Vienos lentelės metodo trūkumai

Tikėtina, kad aukščiau pateikta lentelė jums atrodo gana pažįstama. Pradėkime pridėti papildomų duomenų į mūsų augančią duomenų bazę – metinį kritulių kiekį (milimetrais). Susitelkime į 2018, 2019 ir 2020 metus. Jei pridėtume duomenis apie Tokiją, tai galėtų atrodyti taip:

| Miestas | Šalis  | Metai | Kiekis |
| ------- | ------ | ----- | ------ |
| Tokijas | Japonija | 2020 | 1690   |
| Tokijas | Japonija | 2019 | 1874   |
| Tokijas | Japonija | 2018 | 1445   |

Ką pastebite apie mūsų lentelę? Galbūt pastebėjote, kad mes kartojame miesto pavadinimą ir šalį vėl ir vėl. Tai gali užimti nemažai vietos ir iš esmės yra nereikalinga. Juk Tokijas turi tik vieną pavadinimą, kuris mus domina.

Gerai, pabandykime ką nors kita. Pridėkime naujus stulpelius kiekvieniems metams:

| Miestas  | Šalis          | 2018 | 2019 | 2020 |
| -------- | -------------- | ---- | ---- | ---- |
| Tokijas  | Japonija       | 1445 | 1874 | 1690 |
| Atlanta  | Jungtinės Valstijos | 1779 | 1111 | 1683 |
| Oklendas | Naujoji Zelandija   | 1386 | 942  | 1176 |

Nors tai padeda išvengti eilučių dubliavimo, atsiranda keletas kitų iššūkių. Kiekvieną kartą atsiradus naujiems metams, reikėtų keisti lentelės struktūrą. Be to, augant duomenims, metų naudojimas kaip stulpelių apsunkins reikšmių gavimą ir skaičiavimą.

Štai kodėl mums reikia kelių lentelių ir ryšių. Padalindami duomenis galime išvengti dubliavimo ir turėti daugiau lankstumo dirbant su duomenimis.

## Ryšių koncepcijos

Grįžkime prie savo duomenų ir nuspręskime, kaip juos padalinti. Žinome, kad norime saugoti miestų pavadinimus ir šalis, todėl tai greičiausiai geriausiai veiks vienoje lentelėje.

| Miestas  | Šalis          |
| -------- | -------------- |
| Tokijas  | Japonija       |
| Atlanta  | Jungtinės Valstijos |
| Oklendas | Naujoji Zelandija   |

Tačiau prieš kurdami kitą lentelę, turime nuspręsti, kaip nurodyti kiekvieną miestą. Mums reikia kažkokio identifikatoriaus, ID arba (techniniais duomenų bazės terminais) pirminio rakto. Pirminis raktas yra reikšmė, naudojama konkrečiai eilutei lentelėje identifikuoti. Nors tai galėtų būti pagrįsta pačia reikšme (pavyzdžiui, galėtume naudoti miesto pavadinimą), tai beveik visada turėtų būti skaičius arba kitas identifikatorius. Nenorime, kad ID kada nors pasikeistų, nes tai sugadintų ryšį. Daugeliu atvejų pirminis raktas arba ID bus automatiškai sugeneruotas skaičius.

> ✅ Pirminis raktas dažnai trumpinamas kaip PK

### miestai

| miestas_id | Miestas  | Šalis          |
| ---------- | -------- | -------------- |
| 1          | Tokijas  | Japonija       |
| 2          | Atlanta  | Jungtinės Valstijos |
| 3          | Oklendas | Naujoji Zelandija   |

> ✅ Pastebėsite, kad šioje pamokoje terminus "id" ir "pirminis raktas" naudojame pakaitomis. Šios koncepcijos taikomos ir "DataFrames", kuriuos tyrinėsite vėliau. "DataFrames" nenaudoja termino "pirminis raktas", tačiau pastebėsite, kad jie veikia labai panašiai.

Sukūrę miestų lentelę, saugokime kritulių duomenis. Užuot dubliavę visą informaciją apie miestą, galime naudoti ID. Taip pat turėtume užtikrinti, kad naujai sukurtoje lentelėje būtų *id* stulpelis, nes visos lentelės turėtų turėti ID arba pirminį raktą.

### krituliai

| krituliai_id | miestas_id | Metai | Kiekis |
| ------------ | ---------- | ----- | ------ |
| 1            | 1          | 2018  | 1445   |
| 2            | 1          | 2019  | 1874   |
| 3            | 1          | 2020  | 1690   |
| 4            | 2          | 2018  | 1779   |
| 5            | 2          | 2019  | 1111   |
| 6            | 2          | 2020  | 1683   |
| 7            | 3          | 2018  | 1386   |
| 8            | 3          | 2019  | 942    |
| 9            | 3          | 2020  | 1176   |

Atkreipkite dėmesį į **miestas_id** stulpelį naujai sukurtoje **krituliai** lentelėje. Šis stulpelis turi reikšmes, kurios nurodo ID **miestai** lentelėje. Techniniais reliacinių duomenų terminais tai vadinama **užsienio raktu**; tai yra pirminis raktas iš kitos lentelės. Galite tiesiog galvoti apie tai kaip apie nuorodą arba rodyklę. **miestas_id** 1 nurodo Tokiją.

> [!NOTE] Užsienio raktas dažnai trumpinamas kaip FK

## Duomenų gavimas

Padalijus duomenis į dvi lenteles, galite susimąstyti, kaip juos gauti. Jei naudojame reliacinę duomenų bazę, tokią kaip MySQL, SQL Server ar Oracle, galime naudoti kalbą, vadinamą struktūrizuota užklausų kalba (SQL). SQL (kartais tariama "siquel") yra standartinė kalba, naudojama duomenims reliacinėje duomenų bazėje gauti ir keisti.

Norėdami gauti duomenis, naudojate komandą `SELECT`. Iš esmės jūs **pasirenkate** stulpelius, kuriuos norite matyti, **iš** lentelės, kurioje jie yra. Jei norėtumėte parodyti tik miestų pavadinimus, galėtumėte naudoti šią užklausą:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` nurodote stulpelius, o `FROM` nurodote lenteles.

> [NOTE] SQL sintaksė nėra jautri raidžių dydžiui, tai reiškia, kad `select` ir `SELECT` reiškia tą patį. Tačiau, priklausomai nuo naudojamos duomenų bazės tipo, stulpeliai ir lentelės gali būti jautrūs raidžių dydžiui. Todėl geriausia praktika yra visada elgtis taip, lyg viskas programavime būtų jautru raidžių dydžiui. Rašant SQL užklausas įprasta raktinius žodžius rašyti didžiosiomis raidėmis.

Aukščiau pateikta užklausa parodys visus miestus. Įsivaizduokime, kad norime parodyti tik Naujosios Zelandijos miestus. Mums reikia kažkokio filtro. SQL raktinis žodis tam yra `WHERE`, arba "kur kažkas yra tiesa".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Duomenų sujungimas

Iki šiol gavome duomenis iš vienos lentelės. Dabar norime sujungti duomenis iš **miestai** ir **krituliai**. Tai atliekama *sujungiant* juos. Iš esmės sukursite siūlę tarp dviejų lentelių ir suderinsite reikšmes iš stulpelio kiekvienoje lentelėje.

Mūsų pavyzdyje suderinsime **miestas_id** stulpelį **krituliai** su **miestas_id** stulpeliu **miestai**. Tai suderins kritulių reikšmę su atitinkamu miestu. Sujungimo tipas, kurį atliksime, vadinamas *vidiniu* sujungimu, tai reiškia, kad jei kokios nors eilutės nesutampa su kita lentele, jos nebus rodomos. Mūsų atveju kiekvienas miestas turi kritulių duomenis, todėl viskas bus parodyta.

Pažiūrėkime kritulių duomenis už 2019 metus visiems mūsų miestams.

Tai atliksime etapais. Pirmas žingsnis yra sujungti duomenis, nurodant stulpelius siūlei – **miestas_id**, kaip buvo pabrėžta anksčiau.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Pabrėžėme du stulpelius, kurių norime, ir tai, kad norime sujungti lenteles pagal **miestas_id**. Dabar galime pridėti `WHERE` sakinį, kad filtruotume tik 2019 metus.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
WHERE rainfall.year = 2019

-- Output

-- city     | amount
-- -------- | ------
-- Tokyo    | 1874
-- Atlanta  | 1111
-- Auckland |  942
```

## Santrauka

Reliacinės duomenų bazės yra orientuotos į informacijos padalijimą į kelias lenteles, kurios vėliau sujungiamos rodymui ir analizei. Tai suteikia didelį lankstumą atliekant skaičiavimus ir kitaip manipuliuojant duomenimis. Jūs susipažinote su pagrindinėmis reliacinės duomenų bazės koncepcijomis ir kaip atlikti sujungimą tarp dviejų lentelių.

## 🚀 Iššūkis

Internete yra daugybė reliacinių duomenų bazių. Galite tyrinėti duomenis naudodamiesi aukščiau išmoktais įgūdžiais.

## Po paskaitos: testas

## [Po paskaitos: testas](https://ff-quizzes.netlify.app/en/ds/)

## Peržiūra ir savarankiškas mokymasis

Yra keletas išteklių [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum), kurie padės jums toliau tyrinėti SQL ir reliacinių duomenų bazių koncepcijas:

- [Reliacinių duomenų koncepcijų aprašymas](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Pradėkite užklausų rašymą su Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL yra SQL versija)
- [SQL turinys Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Užduotis

[Užduoties pavadinimas](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.