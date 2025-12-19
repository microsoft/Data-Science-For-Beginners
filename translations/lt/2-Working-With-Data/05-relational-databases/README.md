<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T12:30:34+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "lt"
}
-->
# Darbas su duomenimis: reliacinės duomenų bazės

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Darbas su duomenimis: reliacinės duomenų bazės - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Tikėtina, kad anksčiau esate naudoję skaičiuoklę informacijos saugojimui. Turėjote eilučių ir stulpelių rinkinį, kur eilutėse buvo informacija (arba duomenys), o stulpeliai aprašė informaciją (kartais vadinamą metaduomenimis). Reliacinė duomenų bazė yra sukurta remiantis šiuo pagrindiniu stulpelių ir eilučių lentelėse principu, leidžiančiu turėti informaciją paskirstytą keliuose lentelėse. Tai leidžia dirbti su sudėtingesniais duomenimis, išvengti dubliavimo ir turėti lankstumą tyrinėjant duomenis. Pažvelkime į reliacinės duomenų bazės sąvokas.

## [Priešpaskaitos testas](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Viskas prasideda nuo lentelių

Reliacinės duomenų bazės pagrindą sudaro lentelės. Kaip ir skaičiuoklėje, lentelė yra stulpelių ir eilučių rinkinys. Eilutėse yra duomenys arba informacija, su kuria norime dirbti, pavyzdžiui, miesto pavadinimas ar kritulių kiekis. Stulpeliai aprašo saugomus duomenis.

Pradėkime tyrinėjimą sukurdami lentelę, kurioje saugosime informaciją apie miestus. Galime pradėti nuo jų pavadinimo ir šalies. Tai galėtumėte saugoti lentelėje taip:

| Miestas  | Šalis         |
| -------- | ------------- |
| Tokijas  | Japonija      |
| Atlanta  | Jungtinės Valstijos |
| Oklendas | Naujoji Zelandija |

Atkreipkite dėmesį, kad stulpelių pavadinimai **miestas**, **šalis** ir **populiacija** aprašo saugomus duomenis, o kiekviena eilutė turi informaciją apie vieną miestą.

## Vienos lentelės metodo trūkumai

Tikėtina, kad aukščiau pateikta lentelė jums atrodo gana pažįstama. Pridėkime papildomų duomenų į mūsų augančią duomenų bazę – metinius kritulių kiekius (milimetrais). Susitelksime į 2018, 2019 ir 2020 metus. Jei pridėtume duomenis Tokijui, tai atrodytų maždaug taip:

| Miestas | Šalis   | Metai | Kiekis |
| ------- | ------- | ----- | ------ |
| Tokijas | Japonija| 2020  | 1690   |
| Tokijas | Japonija| 2019  | 1874   |
| Tokijas | Japonija| 2018  | 1445   |

Ką pastebite apie mūsų lentelę? Galite pastebėti, kad mes dubliuojame miesto pavadinimą ir šalį vėl ir vėl. Tai gali užimti nemažai vietos saugykloje ir dažniausiai nereikia turėti kelių kopijų. Juk Tokijas turi tik vieną pavadinimą, kuris mus domina.

Gerai, pabandykime ką nors kita. Pridėkime naujus stulpelius kiekvieniems metams:

| Miestas  | Šalis         | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokijas  | Japonija      | 1445 | 1874 | 1690 |
| Atlanta  | Jungtinės Valstijos | 1779 | 1111 | 1683 |
| Oklendas | Naujoji Zelandija | 1386 | 942  | 1176 |

Nors tai išvengia eilučių dubliavimo, atsiranda keletas kitų iššūkių. Kiekvieną kartą atsiradus naujiems metams, reikėtų keisti lentelės struktūrą. Be to, kai duomenys auga, metai kaip stulpeliai apsunkins reikšmių gavimą ir skaičiavimą.

Todėl mums reikia kelių lentelių ir ryšių. Padalindami duomenis galime išvengti dubliavimo ir turėti daugiau lankstumo dirbant su duomenimis.

## Ryšių sąvokos

Grįžkime prie mūsų duomenų ir nuspręskime, kaip juos padalinti. Žinome, kad norime saugoti miestų pavadinimus ir šalis, todėl tai geriausiai tiks vienoje lentelėje.

| Miestas  | Šalis         |
| -------- | ------------- |
| Tokijas  | Japonija      |
| Atlanta  | Jungtinės Valstijos |
| Oklendas | Naujoji Zelandija |

Tačiau prieš kuriant kitą lentelę, turime nuspręsti, kaip nurodyti kiekvieną miestą. Reikia tam tikro identifikatoriaus, ID arba (techniniais duomenų bazės terminais) pirminio rakto. Pirminis raktas yra reikšmė, naudojama identifikuoti vieną konkretų eilutę lentelėje. Nors tai galėtų būti pagrįsta pačia reikšme (pavyzdžiui, galėtume naudoti miesto pavadinimą), beveik visada tai turėtų būti skaičius arba kitas identifikatorius. Nenorime, kad ID keistųsi, nes tai sulaužytų ryšį. Daugeliu atvejų pirminis raktas arba ID bus automatiškai sugeneruotas skaičius.

> ✅ Pirminis raktas dažnai sutrumpinamas kaip PK

### cities

| city_id | Miestas  | Šalis         |
| ------- | -------- | ------------- |
| 1       | Tokijas  | Japonija      |
| 2       | Atlanta  | Jungtinės Valstijos |
| 3       | Oklendas | Naujoji Zelandija |

> ✅ Pastebėsite, kad šioje pamokoje terminus „id“ ir „pirminis raktas“ vartojame pakaitomis. Šios sąvokos taikomos ir DataFrames, kuriuos tyrinėsite vėliau. DataFrames nenaudoja termino „pirminis raktas“, tačiau elgiasi panašiai.

Sukūrę miestų lentelę, saugosime kritulių duomenis. Vietoj to, kad dubliuotume visą informaciją apie miestą, galime naudoti ID. Taip pat turėtume užtikrinti, kad naujai sukurtoje lentelėje būtų *id* stulpelis, nes visos lentelės turėtų turėti ID arba pirminį raktą.

### rainfall

| rainfall_id | city_id | Metai | Kiekis |
| ----------- | ------- | ----- | ------ |
| 1           | 1       | 2018  | 1445   |
| 2           | 1       | 2019  | 1874   |
| 3           | 1       | 2020  | 1690   |
| 4           | 2       | 2018  | 1779   |
| 5           | 2       | 2019  | 1111   |
| 6           | 2       | 2020  | 1683   |
| 7           | 3       | 2018  | 1386   |
| 8           | 3       | 2019  | 942    |
| 9           | 3       | 2020  | 1176   |

Atkreipkite dėmesį į **city_id** stulpelį naujai sukurtos **rainfall** lentelės viduje. Šis stulpelis turi reikšmes, kurios nurodo ID reikšmes **cities** lentelėje. Techniniais reliacinių duomenų terminais tai vadinama **svetimu raktu**; tai yra pirminis raktas iš kitos lentelės. Galite tiesiog galvoti apie tai kaip nuorodą arba rodyklę. **city_id** 1 nurodo Tokiją.

> [!NOTE] 
> Svetimas raktas dažnai sutrumpinamas kaip FK

## Duomenų gavimas

Padaliję duomenis į dvi lenteles, galbūt svarstote, kaip juos gauti. Jei naudojame reliacinę duomenų bazę, tokią kaip MySQL, SQL Server ar Oracle, galime naudoti kalbą, vadinamą struktūruotąja užklausų kalba arba SQL. SQL (kartais tariama „sequel“) yra standartinė kalba, naudojama duomenims gauti ir keisti reliacinėje duomenų bazėje.

Duomenims gauti naudojama komanda `SELECT`. Iš esmės jūs **pasirenkate** stulpelius, kuriuos norite matyti, **iš** lentelės, kurioje jie yra. Jei norėtumėte parodyti tik miestų pavadinimus, galėtumėte naudoti šią užklausą:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` nurodo stulpelius, o `FROM` – lenteles.

> [!NOTE] 
> SQL sintaksė nėra jautri raidžių dydžiui, tai reiškia, kad `select` ir `SELECT` reiškia tą patį. Tačiau, priklausomai nuo duomenų bazės tipo, stulpeliai ir lentelės gali būti jautrūs raidžių dydžiui. Todėl geriausia praktika yra viską programavime laikyti jautriu raidžių dydžiui. Rašant SQL užklausas įprasta raktinius žodžius rašyti didžiosiomis raidėmis.

Aukščiau pateikta užklausa parodys visus miestus. Įsivaizduokime, kad norime parodyti tik Naujosios Zelandijos miestus. Reikia tam tikro filtro. SQL raktinis žodis tam yra `WHERE`, arba „kur kažkas yra tiesa“.

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Duomenų sujungimas

Iki šiol gavome duomenis iš vienos lentelės. Dabar norime sujungti duomenis iš **cities** ir **rainfall**. Tai atliekama *sujungiant* jas kartu. Iš esmės sukuriate jungtį tarp dviejų lentelių ir suderinate reikšmes iš stulpelio kiekvienoje lentelėje.

Mūsų pavyzdyje suderinsime **city_id** stulpelį **rainfall** su **city_id** stulpeliu **cities**. Tai suderins kritulių reikšmę su atitinkamu miestu. Atliksime tai, kas vadinama *vidiniu* sujungimu, reiškiančiu, kad jei kokios nors eilutės nesutampa su kita lentelės reikšme, jos nebus rodomos. Mūsų atveju kiekvienas miestas turi kritulių duomenis, todėl viskas bus parodyta.

Gaukime kritulių duomenis už 2019 metus visiems mūsų miestams.

Darysime tai etapais. Pirmas žingsnis – sujungti duomenis nurodant jungties stulpelius – **city_id**, kaip minėta anksčiau.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Pažymėjome du stulpelius, kuriuos norime, ir faktą, kad norime sujungti lenteles pagal **city_id**. Dabar galime pridėti `WHERE` sakinį, kad filtruotume tik 2019 metus.

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

Reliacinės duomenų bazės yra sutelktos į informacijos padalijimą tarp kelių lentelių, kurios vėliau sujungiamos rodymui ir analizei. Tai suteikia didelį lankstumą atlikti skaičiavimus ir kitaip manipuliuoti duomenimis. Jūs susipažinote su reliacinės duomenų bazės pagrindinėmis sąvokomis ir kaip atlikti sujungimą tarp dviejų lentelių.

## 🚀 Iššūkis

Internete yra daug reliacinių duomenų bazių. Galite tyrinėti duomenis naudodami aukščiau įgytas žinias.

## Po paskaitos testas

## [Po paskaitos testas](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Peržiūra ir savarankiškas mokymasis

Yra keletas išteklių [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum), kurie padės toliau tyrinėti SQL ir reliacinių duomenų bazių sąvokas

- [Aprašykite reliacinių duomenų sąvokas](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Pradėkite užklausas su Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL yra SQL versija)
- [SQL turinys Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Užduotis

[Oro uostų duomenų rodymas](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->