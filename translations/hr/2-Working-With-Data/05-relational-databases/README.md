<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T12:17:54+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "hr"
}
-->
# Rad s podacima: Relacijske baze podataka

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Rad s podacima: Relacijske baze podataka - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Vjerojatno ste u prošlosti koristili proračunsku tablicu za pohranu informacija. Imali ste skup redaka i stupaca, gdje su redci sadržavali informacije (ili podatke), a stupci su opisivali informacije (ponekad nazvane metapodacima). Relacijska baza podataka izgrađena je na ovom osnovnom principu stupaca i redaka u tablicama, što vam omogućuje da imate informacije raspoređene preko više tablica. To vam omogućuje rad s složenijim podacima, izbjegavanje dupliciranja i fleksibilnost u načinu na koji istražujete podatke. Istražimo koncepte relacijske baze podataka.

## [Kviz prije predavanja](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Sve počinje s tablicama

Relacijska baza podataka u svojoj je srži sastavljena od tablica. Baš kao i kod proračunske tablice, tablica je zbirka stupaca i redaka. Redak sadrži podatke ili informacije s kojima želimo raditi, poput imena grada ili količine oborina. Stupci opisuju podatke koje pohranjuju.

Započnimo naše istraživanje stvaranjem tablice za pohranu informacija o gradovima. Mogli bismo započeti s njihovim imenom i državom. To biste mogli pohraniti u tablicu na sljedeći način:

| Grad     | Država       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | Sjedinjene Države |
| Auckland | Novi Zeland   |

Primijetite da nazivi stupaca **grad**, **država** i **populacija** opisuju pohranjene podatke, a svaki redak sadrži informacije o jednom gradu.

## Nedostaci pristupa s jednom tablicom

Vjerojatno vam gornja tablica izgleda relativno poznato. Počnimo dodavati dodatne podatke u našu rastuću bazu podataka - godišnje oborine (u milimetrima). Usredotočit ćemo se na godine 2018., 2019. i 2020. Ako bismo to dodali za Tokyo, moglo bi izgledati ovako:

| Grad  | Država | Godina | Količina |
| ----- | ------- | ---- | ------ |
| Tokyo | Japan   | 2020 | 1690   |
| Tokyo | Japan   | 2019 | 1874   |
| Tokyo | Japan   | 2018 | 1445   |

Što primjećujete u našoj tablici? Možda primjećujete da dupliciramo ime i državu grada iznova i iznova. To bi moglo zauzeti dosta prostora za pohranu i uglavnom je nepotrebno imati više kopija. Uostalom, Tokyo ima samo jedno ime koje nas zanima.

OK, pokušajmo nešto drugo. Dodajmo nove stupce za svaku godinu:

| Grad     | Država       | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | Sjedinjene Države | 1779 | 1111 | 1683 |
| Auckland | Novi Zeland   | 1386 | 942  | 1176 |

Iako se ovime izbjegava dupliciranje redaka, pojavljuju se drugi izazovi. Morali bismo mijenjati strukturu naše tablice svaki put kad dođe nova godina. Osim toga, kako naši podaci rastu, imati godine kao stupce otežat će dohvaćanje i izračunavanje vrijednosti.

Zato nam trebaju više tablica i odnosi. Razdvajanjem podataka možemo izbjeći dupliciranje i imati veću fleksibilnost u radu s podacima.

## Koncepti odnosa

Vratimo se našim podacima i odlučimo kako ih želimo podijeliti. Znamo da želimo pohraniti ime i državu za naše gradove, pa će to vjerojatno najbolje funkcionirati u jednoj tablici.

| Grad     | Država       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | Sjedinjene Države |
| Auckland | Novi Zeland   |

No prije nego što stvorimo sljedeću tablicu, moramo shvatiti kako ćemo referencirati svaki grad. Trebamo neki oblik identifikatora, ID-a ili (u tehničkim terminima baza podataka) primarni ključ. Primarni ključ je vrijednost koja se koristi za identifikaciju jednog specifičnog retka u tablici. Iako bi to moglo biti temeljeno na samoj vrijednosti (na primjer, mogli bismo koristiti ime grada), gotovo uvijek bi to trebao biti broj ili neki drugi identifikator. Ne želimo da se ID ikada mijenja jer bi to prekinulo odnos. U većini slučajeva primarni ključ ili ID bit će automatski generirani broj.

> ✅ Primarni ključ se često skraćuje kao PK

### gradovi

| city_id | Grad     | Država       |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japan         |
| 2       | Atlanta  | Sjedinjene Države |
| 3       | Auckland | Novi Zeland   |

> ✅ Primijetit ćete da tijekom ovog lekcije koristimo pojmove "id" i "primarni ključ" naizmjenično. Koncepti ovdje vrijede i za DataFrameove, koje ćete istražiti kasnije. DataFrameovi ne koriste terminologiju "primarni ključ", no primijetit ćete da se ponašaju na sličan način.

Nakon što smo stvorili tablicu gradova, pohranimo podatke o oborinama. Umjesto da dupliciramo pune informacije o gradu, možemo koristiti ID. Također bismo trebali osigurati da nova tablica ima stupac *id*, jer sve tablice trebaju imati id ili primarni ključ.

### oborine

| rainfall_id | city_id | Godina | Količina |
| ----------- | ------- | ---- | ------ |
| 1           | 1       | 2018 | 1445   |
| 2           | 1       | 2019 | 1874   |
| 3           | 1       | 2020 | 1690   |
| 4           | 2       | 2018 | 1779   |
| 5           | 2       | 2019 | 1111   |
| 6           | 2       | 2020 | 1683   |
| 7           | 3       | 2018 | 1386   |
| 8           | 3       | 2019 | 942    |
| 9           | 3       | 2020 | 1176   |

Primijetite stupac **city_id** unutar novostvorene tablice **oborine**. Ovaj stupac sadrži vrijednosti koje referenciraju ID-eve u tablici **gradovi**. U tehničkim terminima relacijskih podataka, ovo se naziva **strani ključ**; to je primarni ključ iz druge tablice. Možete ga jednostavno smatrati referencom ili pokazivačem. **city_id** 1 referencira Tokyo.

> [!NOTE] 
> Strani ključ se često skraćuje kao FK

## Dohvaćanje podataka

S našim podacima razdvojenim u dvije tablice, možda se pitate kako ih dohvatiti. Ako koristimo relacijsku bazu podataka poput MySQL, SQL Server ili Oracle, možemo koristiti jezik nazvan Structured Query Language ili SQL. SQL (ponekad izgovaran kao "sequel") je standardni jezik za dohvaćanje i izmjenu podataka u relacijskoj bazi podataka.

Za dohvaćanje podataka koristite naredbu `SELECT`. U svojoj srži, vi **birate** stupce koje želite vidjeti **iz** tablice u kojoj se nalaze. Ako želite prikazati samo imena gradova, mogli biste koristiti sljedeće:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` je mjesto gdje navodite stupce, a `FROM` je mjesto gdje navodite tablice.

> [!NOTE] 
> SQL sintaksa nije osjetljiva na velika i mala slova, što znači da `select` i `SELECT` znače isto. Međutim, ovisno o vrsti baze podataka koju koristite, stupci i tablice mogu biti osjetljivi na velika i mala slova. Kao rezultat, najbolja praksa je uvijek tretirati sve u programiranju kao da je osjetljivo na velika i mala slova. Prilikom pisanja SQL upita uobičajena je konvencija da ključne riječi pišete velikim slovima.

Gornji upit prikazat će sve gradove. Zamislimo da želimo prikazati samo gradove u Novom Zelandu. Trebamo neki oblik filtra. SQL ključna riječ za to je `WHERE`, ili "gdje je nešto istinito".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Spajanje podataka

Do sada smo dohvaćali podatke iz jedne tablice. Sada želimo spojiti podatke iz obje tablice, **gradovi** i **oborine**. To se radi *spajanjem* tablica. Učinit ćete spoj između dvije tablice i uskladiti vrijednosti iz stupca svake tablice.

U našem primjeru, uskladit ćemo stupac **city_id** u tablici **oborine** sa stupcem **city_id** u tablici **gradovi**. Time ćemo povezati vrijednost oborina s pripadajućim gradom. Vrsta spajanja koju ćemo napraviti naziva se *inner* join, što znači da ako neki redci nemaju podudaranje u drugoj tablici, neće biti prikazani. U našem slučaju svaki grad ima podatke o oborinama, pa će sve biti prikazano.

Dohvatimo oborine za 2019. godinu za sve naše gradove.

Radit ćemo to u koracima. Prvi korak je spojiti podatke zajedno tako da naznačimo stupce za spoj - **city_id** kao što je ranije istaknuto.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Istaknuli smo dva stupca koja želimo i činjenicu da želimo spojiti tablice preko **city_id**. Sada možemo dodati `WHERE` naredbu da filtriramo samo godinu 2019.

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

## Sažetak

Relacijske baze podataka usredotočene su na dijeljenje informacija između više tablica koje se zatim ponovno spajaju za prikaz i analizu. To pruža visoku razinu fleksibilnosti za izvođenje izračuna i druge manipulacije podacima. Vidjeli ste osnovne koncepte relacijske baze podataka i kako napraviti spoj između dvije tablice.

## 🚀 Izazov

Postoji mnogo relacijskih baza podataka dostupnih na internetu. Možete istraživati podatke koristeći vještine koje ste naučili iznad.

## Kviz nakon predavanja

## [Kviz nakon predavanja](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Pregled i samostalno učenje

Na [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) dostupno je nekoliko resursa za nastavak istraživanja SQL-a i koncepata relacijskih baza podataka

- [Opisati koncepte relacijskih podataka](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Početak rada s upitima u Transact-SQL-u](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL je verzija SQL-a)
- [SQL sadržaj na Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Zadatak

[Prikaz podataka o zračnim lukama](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument preveden je pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->