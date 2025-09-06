<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9399d7b4767e75068f95ce5c660b285c",
  "translation_date": "2025-09-05T19:19:23+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "hr"
}
-->
# Rad s podacima: Relacijske baze podataka

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Rad s podacima: Relacijske baze podataka - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Velike su šanse da ste u prošlosti koristili proračunsku tablicu za pohranu informacija. Imali ste skup redaka i stupaca, gdje su redci sadržavali informacije (ili podatke), a stupci opisivali te informacije (ponekad nazvane metapodaci). Relacijska baza podataka temelji se na ovom osnovnom principu stupaca i redaka u tablicama, omogućujući vam da informacije rasporedite u više tablica. To vam omogućuje rad s kompleksnijim podacima, izbjegavanje dupliciranja i fleksibilnost u istraživanju podataka. Pogledajmo koncepte relacijske baze podataka.

## [Kviz prije predavanja](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Sve počinje s tablicama

Relacijska baza podataka u svojoj osnovi ima tablice. Kao i kod proračunske tablice, tablica je zbirka stupaca i redaka. Redak sadrži podatke ili informacije s kojima želimo raditi, poput imena grada ili količine oborina. Stupci opisuju podatke koje pohranjuju.

Započnimo istraživanje stvaranjem tablice za pohranu informacija o gradovima. Možemo početi s njihovim imenom i državom. To biste mogli pohraniti u tablicu na sljedeći način:

| Grad     | Država        |
| -------- | ------------- |
| Tokio    | Japan         |
| Atlanta  | Sjedinjene Države |
| Auckland | Novi Zeland   |

Primijetite da nazivi stupaca **grad**, **država** i **populacija** opisuju podatke koji se pohranjuju, a svaki redak sadrži informacije o jednom gradu.

## Nedostaci pristupa jednoj tablici

Velike su šanse da vam gornja tablica izgleda relativno poznato. Dodajmo dodatne podatke u našu rastuću bazu podataka - godišnje oborine (u milimetrima). Usredotočit ćemo se na godine 2018., 2019. i 2020. Ako bismo ih dodali za Tokio, to bi izgledalo ovako:

| Grad  | Država | Godina | Količina |
| ----- | ------- | ---- | ------ |
| Tokio | Japan   | 2020 | 1690   |
| Tokio | Japan   | 2019 | 1874   |
| Tokio | Japan   | 2018 | 1445   |

Što primjećujete kod naše tablice? Možda primjećujete da ponavljamo ime i državu grada iznova i iznova. To bi moglo zauzeti dosta prostora za pohranu, a uglavnom je nepotrebno imati više kopija. Uostalom, Tokio ima samo jedno ime koje nas zanima.

OK, pokušajmo nešto drugo. Dodajmo nove stupce za svaku godinu:

| Grad     | Država        | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokio    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | Sjedinjene Države | 1779 | 1111 | 1683 |
| Auckland | Novi Zeland   | 1386 | 942  | 1176 |

Iako ovo izbjegava dupliciranje redaka, dodaje nekoliko drugih izazova. Morali bismo mijenjati strukturu naše tablice svaki put kad se pojavi nova godina. Osim toga, kako naši podaci rastu, imati godine kao stupce otežat će dohvaćanje i izračunavanje vrijednosti.

Zbog toga trebamo više tablica i odnose. Razdvajanjem podataka možemo izbjeći dupliciranje i imati veću fleksibilnost u radu s podacima.

## Koncepti odnosa

Vratimo se našim podacima i odredimo kako ih želimo podijeliti. Znamo da želimo pohraniti ime i državu za naše gradove, pa će to vjerojatno najbolje funkcionirati u jednoj tablici.

| Grad     | Država        |
| -------- | ------------- |
| Tokio    | Japan         |
| Atlanta  | Sjedinjene Države |
| Auckland | Novi Zeland   |

No prije nego što stvorimo sljedeću tablicu, moramo smisliti kako referencirati svaki grad. Trebamo neki oblik identifikatora, ID ili (u tehničkim terminima baze podataka) primarni ključ. Primarni ključ je vrijednost koja se koristi za identifikaciju jednog specifičnog retka u tablici. Iako bi se to moglo temeljiti na samoj vrijednosti (mogli bismo koristiti ime grada, na primjer), gotovo uvijek bi to trebao biti broj ili drugi identifikator. Ne želimo da se ID ikada promijeni jer bi to prekinulo odnos. U većini slučajeva primarni ključ ili ID bit će automatski generirani broj.

> ✅ Primarni ključ često se skraćuje kao PK

### gradovi

| grad_id | Grad     | Država        |
| ------- | -------- | ------------- |
| 1       | Tokio    | Japan         |
| 2       | Atlanta  | Sjedinjene Države |
| 3       | Auckland | Novi Zeland   |

> ✅ Primijetit ćete da tijekom ove lekcije koristimo izraze "id" i "primarni ključ" naizmjenično. Koncepti ovdje vrijede za DataFrameove, koje ćete kasnije istražiti. DataFrameovi ne koriste terminologiju "primarni ključ", no primijetit ćete da se ponašaju na vrlo sličan način.

S našom tablicom gradova stvorenom, pohranimo oborine. Umjesto dupliciranja punih informacija o gradu, možemo koristiti ID. Također bismo trebali osigurati da novostvorena tablica ima *id* stupac, jer sve tablice trebaju imati ID ili primarni ključ.

### oborine

| oborine_id | grad_id | Godina | Količina |
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

Primijetite stupac **grad_id** unutar novostvorene tablice **oborine**. Ovaj stupac sadrži vrijednosti koje referenciraju ID-ove u tablici **gradovi**. U tehničkim terminima relacijskih podataka, ovo se naziva **strani ključ**; to je primarni ključ iz druge tablice. Možete ga jednostavno zamisliti kao referencu ili pokazivač. **grad_id** 1 referencira Tokio.

> [!NOTE] Strani ključ često se skraćuje kao FK

## Dohvaćanje podataka

S našim podacima podijeljenim u dvije tablice, možda se pitate kako ih dohvatiti. Ako koristimo relacijsku bazu podataka poput MySQL-a, SQL Servera ili Oraclea, možemo koristiti jezik nazvan Structured Query Language ili SQL. SQL (ponekad se izgovara "sequel") je standardni jezik koji se koristi za dohvaćanje i izmjenu podataka u relacijskoj bazi podataka.

Za dohvaćanje podataka koristite naredbu `SELECT`. U svojoj osnovi, **odabirete** stupce koje želite vidjeti **iz** tablice u kojoj se nalaze. Ako želite prikazati samo imena gradova, možete koristiti sljedeće:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` je mjesto gdje navodite stupce, a `FROM` je mjesto gdje navodite tablice.

> [NOTE] SQL sintaksa nije osjetljiva na velika i mala slova, što znači da `select` i `SELECT` znače isto. Međutim, ovisno o vrsti baze podataka koju koristite, stupci i tablice mogu biti osjetljivi na velika i mala slova. Kao rezultat toga, najbolje je uvijek tretirati sve u programiranju kao da je osjetljivo na velika i mala slova. Kada pišete SQL upite, uobičajena konvencija je da ključne riječi pišete velikim slovima.

Gornji upit prikazat će sve gradove. Zamislimo da želimo prikazati samo gradove u Novom Zelandu. Trebamo neki oblik filtra. SQL ključna riječ za to je `WHERE`, ili "gdje nešto vrijedi".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Spajanje podataka

Do sada smo dohvaćali podatke iz jedne tablice. Sada želimo spojiti podatke iz **gradovi** i **oborine**. To se radi *spajanjem* tablica. Učinkovito ćete stvoriti vezu između dvije tablice i uskladiti vrijednosti iz stupca iz svake tablice.

U našem primjeru, uskladit ćemo stupac **grad_id** u **oborine** sa stupcem **grad_id** u **gradovi**. Ovo će povezati vrijednost oborina s odgovarajućim gradom. Vrsta spajanja koju ćemo izvesti naziva se *unutarnje* spajanje, što znači da se redci koji se ne podudaraju s ničim iz druge tablice neće prikazati. U našem slučaju svaki grad ima oborine, pa će se sve prikazati.

Dohvatimo oborine za 2019. za sve naše gradove.

To ćemo učiniti u koracima. Prvi korak je spajanje podataka označavanjem stupaca za vezu - **grad_id** kao što je prethodno istaknuto.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Istaknuli smo dva stupca koja želimo, i činjenicu da želimo spojiti tablice pomoću **grad_id**. Sada možemo dodati `WHERE` izjavu kako bismo filtrirali samo godinu 2019.

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

Relacijske baze podataka temelje se na podjeli informacija između više tablica koje se zatim ponovno spajaju za prikaz i analizu. To pruža visok stupanj fleksibilnosti za izvođenje izračuna i manipulaciju podacima. Vidjeli ste osnovne koncepte relacijske baze podataka i kako izvesti spajanje između dvije tablice.

## 🚀 Izazov

Na internetu postoji mnogo relacijskih baza podataka. Možete istraživati podatke koristeći vještine koje ste naučili.

## Kviz nakon predavanja

## [Kviz nakon predavanja](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Pregled i samostalno učenje

Postoji nekoliko resursa dostupnih na [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) za nastavak vašeg istraživanja SQL-a i koncepata relacijskih baza podataka.

- [Opis koncepata relacijskih podataka](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Početak rada s upitima u Transact-SQL-u](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL je verzija SQL-a)
- [SQL sadržaj na Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Zadatak

[Naslov zadatka](assignment.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.