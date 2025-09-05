<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11b166fbcb7eaf82308cdc24b562f687",
  "translation_date": "2025-09-04T21:56:27+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "hr"
}
-->
# Rad s podacima: Relacijske baze podataka

|![ Sketchnote autora [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Rad s podacima: Relacijske baze podataka - _Sketchnote autora [@nitya](https://twitter.com/nitya)_ |

Velika je vjerojatnost da ste u prošlosti koristili proračunsku tablicu za pohranu informacija. Imali ste skup redaka i stupaca, gdje su redci sadržavali informacije (ili podatke), a stupci opisivali te informacije (ponekad se nazivaju metapodacima). Relacijska baza podataka temelji se na ovom osnovnom principu stupaca i redaka u tablicama, omogućujući vam da informacije rasporedite u više tablica. To vam omogućuje rad s kompleksnijim podacima, izbjegavanje dupliciranja i veću fleksibilnost u istraživanju podataka. Istražimo koncepte relacijske baze podataka.

## [Kviz prije predavanja](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Sve počinje s tablicama

U središtu relacijske baze podataka nalaze se tablice. Kao i kod proračunske tablice, tablica je zbirka stupaca i redaka. Redak sadrži podatke ili informacije s kojima želimo raditi, poput imena grada ili količine padalina. Stupci opisuju podatke koje pohranjuju.

Započnimo istraživanje stvaranjem tablice za pohranu informacija o gradovima. Možda bismo započeli s njihovim imenom i državom. To biste mogli pohraniti u tablicu na sljedeći način:

| Grad      | Država         |
| --------- | -------------- |
| Tokio     | Japan          |
| Atlanta   | Sjedinjene Države |
| Auckland  | Novi Zeland    |

Primijetite da nazivi stupaca **grad**, **država** i **populacija** opisuju podatke koji se pohranjuju, a svaki redak sadrži informacije o jednom gradu.

## Nedostaci pristupa s jednom tablicom

Velika je vjerojatnost da vam gornja tablica izgleda prilično poznato. Počnimo dodavati dodatne podatke u našu rastuću bazu podataka - godišnje padaline (u milimetrima). Usredotočit ćemo se na godine 2018., 2019. i 2020. Ako bismo to dodali za Tokio, moglo bi izgledati ovako:

| Grad  | Država | Godina | Količina |
| ----- | -------| ------ | -------- |
| Tokio | Japan  | 2020   | 1690     |
| Tokio | Japan  | 2019   | 1874     |
| Tokio | Japan  | 2018   | 1445     |

Što primjećujete kod naše tablice? Možda primjećujete da ponavljamo ime i državu grada iznova i iznova. To bi moglo zauzeti prilično puno prostora za pohranu, a uglavnom je nepotrebno imati više kopija. Uostalom, Tokio ima samo jedno ime koje nas zanima.

OK, pokušajmo nešto drugo. Dodajmo nove stupce za svaku godinu:

| Grad      | Država         | 2018  | 2019  | 2020  |
| --------- | -------------- | ----- | ----- | ----- |
| Tokio     | Japan          | 1445  | 1874  | 1690  |
| Atlanta   | Sjedinjene Države | 1779  | 1111  | 1683  |
| Auckland  | Novi Zeland    | 1386  | 942   | 1176  |

Iako ovo izbjegava dupliciranje redaka, dodaje nekoliko drugih izazova. Morali bismo mijenjati strukturu naše tablice svaki put kada se pojavi nova godina. Osim toga, kako naši podaci rastu, imati godine kao stupce otežat će dohvaćanje i izračunavanje vrijednosti.

Zbog toga su nam potrebne višestruke tablice i odnosi. Razdvajanjem podataka možemo izbjeći dupliciranje i imati veću fleksibilnost u radu s podacima.

## Koncepti odnosa

Vratimo se našim podacima i odredimo kako ih želimo podijeliti. Znamo da želimo pohraniti ime i državu za naše gradove, pa će to vjerojatno najbolje funkcionirati u jednoj tablici.

| Grad      | Država         |
| --------- | -------------- |
| Tokio     | Japan          |
| Atlanta   | Sjedinjene Države |
| Auckland  | Novi Zeland    |

No prije nego što stvorimo sljedeću tablicu, moramo odrediti kako ćemo referencirati svaki grad. Trebamo neki oblik identifikatora, ID-a ili (u tehničkim terminima baze podataka) primarnog ključa. Primarni ključ je vrijednost koja se koristi za identifikaciju jednog specifičnog retka u tablici. Iako bi to moglo biti temeljeno na samoj vrijednosti (mogli bismo koristiti ime grada, na primjer), gotovo uvijek bi to trebao biti broj ili neki drugi identifikator. Ne želimo da se ID ikada promijeni jer bi to prekinulo odnos. U većini slučajeva primarni ključ ili ID bit će automatski generirani broj.

> ✅ Primarni ključ često se skraćuje kao PK

### gradovi

| grad_id | Grad      | Država         |
| ------- | --------- | -------------- |
| 1       | Tokio     | Japan          |
| 2       | Atlanta   | Sjedinjene Države |
| 3       | Auckland  | Novi Zeland    |

> ✅ Primijetit ćete da tijekom ove lekcije koristimo izraze "id" i "primarni ključ" naizmjenično. Ovi koncepti primjenjuju se na DataFrame-ove, koje ćete kasnije istražiti. DataFrame-ovi ne koriste terminologiju "primarni ključ", no primijetit ćete da se ponašaju na sličan način.

S našom tablicom gradova stvorenom, pohranimo podatke o padalinama. Umjesto dupliciranja svih informacija o gradu, možemo koristiti ID. Također bismo trebali osigurati da novo stvorena tablica ima stupac *id*, jer sve tablice trebaju imati ID ili primarni ključ.

### padaline

| padaline_id | grad_id | Godina | Količina |
| ----------- | ------- | ------ | -------- |
| 1           | 1       | 2018   | 1445     |
| 2           | 1       | 2019   | 1874     |
| 3           | 1       | 2020   | 1690     |
| 4           | 2       | 2018   | 1779     |
| 5           | 2       | 2019   | 1111     |
| 6           | 2       | 2020   | 1683     |
| 7           | 3       | 2018   | 1386     |
| 8           | 3       | 2019   | 942      |
| 9           | 3       | 2020   | 1176     |

Primijetite stupac **grad_id** unutar novo stvorene tablice **padaline**. Ovaj stupac sadrži vrijednosti koje referenciraju ID-ove u tablici **gradovi**. U tehničkim terminima relacijskih podataka, ovo se naziva **strani ključ**; to je primarni ključ iz druge tablice. Možete ga jednostavno smatrati referencom ili pokazivačem. **grad_id** 1 referencira Tokio.

> [!NOTE] Strani ključ često se skraćuje kao FK

## Dohvaćanje podataka

S našim podacima podijeljenim u dvije tablice, možda se pitate kako ih dohvatiti. Ako koristimo relacijsku bazu podataka poput MySQL-a, SQL Servera ili Oraclea, možemo koristiti jezik nazvan Structured Query Language ili SQL. SQL (ponekad izgovaran kao "sikvel") je standardni jezik koji se koristi za dohvaćanje i izmjenu podataka u relacijskoj bazi podataka.

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

> [NOTE] SQL sintaksa nije osjetljiva na velika i mala slova, što znači da `select` i `SELECT` znače isto. Međutim, ovisno o vrsti baze podataka koju koristite, stupci i tablice mogu biti osjetljivi na velika i mala slova. Kao rezultat toga, najbolje je uvijek tretirati sve u programiranju kao da je osjetljivo na velika i mala slova. Kada pišete SQL upite, uobičajena konvencija je pisanje ključnih riječi velikim slovima.

Gornji upit prikazat će sve gradove. Zamislimo da želimo prikazati samo gradove u Novom Zelandu. Trebamo neki oblik filtra. SQL ključna riječ za to je `WHERE`, ili "gdje nešto vrijedi".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Spajanje podataka

Do sada smo dohvaćali podatke iz jedne tablice. Sada želimo spojiti podatke iz tablica **gradovi** i **padaline**. Ovo se postiže *spajanjem* tablica. Učinkovito ćete stvoriti vezu između dviju tablica i uskladiti vrijednosti iz stupca iz svake tablice.

U našem primjeru, uskladit ćemo stupac **grad_id** u tablici **padaline** sa stupcem **grad_id** u tablici **gradovi**. Ovo će povezati vrijednosti padalina s odgovarajućim gradom. Tip spajanja koji ćemo koristiti naziva se *unutarnje* spajanje, što znači da se redci koji nemaju podudaranje u drugoj tablici neće prikazati. U našem slučaju svaki grad ima podatke o padalinama, pa će se sve prikazati.

Dohvatimo podatke o padalinama za 2019. za sve naše gradove.

Ovo ćemo učiniti u koracima. Prvi korak je spajanje podataka navođenjem stupaca za vezu - **grad_id**, kako je prethodno istaknuto.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Istaknuli smo dva stupca koja želimo, kao i činjenicu da želimo spojiti tablice pomoću **grad_id**. Sada možemo dodati `WHERE` izjavu kako bismo filtrirali samo godinu 2019.

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

Relacijske baze podataka temelje se na podjeli informacija između više tablica koje se zatim ponovno spajaju za prikaz i analizu. Ovo pruža visoku razinu fleksibilnosti za izvođenje izračuna i manipulaciju podacima. Vidjeli ste osnovne koncepte relacijske baze podataka i kako izvršiti spajanje između dviju tablica.

## 🚀 Izazov

Na internetu postoji mnogo relacijskih baza podataka. Možete istražiti podatke koristeći vještine koje ste naučili iznad.

## Kviz nakon predavanja

## [Kviz nakon predavanja](https://ff-quizzes.netlify.app/en/ds/)

## Pregled i samostalno učenje

Na raspolaganju vam je nekoliko resursa na [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) za nastavak istraživanja SQL-a i koncepata relacijskih baza podataka:

- [Opis koncepata relacijskih podataka](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Početak rada s Transact-SQL-om](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL je verzija SQL-a)
- [SQL sadržaj na Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Zadatak

[Naslov zadatka](assignment.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.