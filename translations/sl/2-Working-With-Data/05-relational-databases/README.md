<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T12:20:51+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "sl"
}
-->
# Delo s podatki: Relacijske baze podatkov

|![ Sketchnote avtorja [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Delo s podatki: Relacijske baze podatkov - _Sketchnote avtorja [@nitya](https://twitter.com/nitya)_ |

Verjetno ste v preteklosti uporabljali preglednico za shranjevanje informacij. Imeli ste niz vrstic in stolpcev, kjer so vrstice vsebovale informacije (ali podatke), stolpci pa so opisovali informacije (včasih imenovane metapodatki). Relacijska baza podatkov temelji na tem osnovnem principu stolpcev in vrstic v tabelah, kar vam omogoča, da imate informacije razporejene po več tabelah. To vam omogoča delo z bolj zapletenimi podatki, preprečuje podvajanje in nudi prilagodljivost pri raziskovanju podatkov. Raziščimo koncepte relacijske baze podatkov.

## [Predpredavanje kviz](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Vse se začne s tabelami

Relacijska baza podatkov ima v svojem jedru tabele. Tako kot pri preglednici je tabela zbirka stolpcev in vrstic. Vrstica vsebuje podatke ali informacije, s katerimi želimo delati, na primer ime mesta ali količino padavin. Stolpci opisujejo podatke, ki jih hranijo.

Začnimo z raziskovanjem tako, da ustvarimo tabelo za shranjevanje informacij o mestih. Začeli bi z njihovim imenom in državo. To lahko shranite v tabelo, kot sledi:

| Mesto    | Država        |
| -------- | ------------- |
| Tokio    | Japonska      |
| Atlanta  | Združene države Amerike |
| Auckland | Nova Zelandija|

Opazite, da imena stolpcev **mesto**, **država** in **prebivalstvo** opisujejo shranjene podatke, vsaka vrstica pa vsebuje informacije o enem mestu.

## Pomanjkljivosti pristopa z eno samo tabelo

Verjetno vam je zgornja tabela dokaj znana. Dodajmo nekaj dodatnih podatkov v našo rastočo bazo podatkov - letne padavine (v milimetrih). Osredotočili se bomo na leta 2018, 2019 in 2020. Če bi jih dodali za Tokio, bi to izgledalo nekako takole:

| Mesto | Država | Leto | Količina |
| ----- | ------ | ---- | -------- |
| Tokio | Japonska | 2020 | 1690     |
| Tokio | Japonska | 2019 | 1874     |
| Tokio | Japonska | 2018 | 1445     |

Kaj opazite pri naši tabeli? Morda opazite, da podvajamo ime in državo mesta znova in znova. To lahko zavzame precej prostora za shranjevanje in je večinoma nepotrebno imeti več kopij. Navsezadnje ima Tokio samo eno ime, ki nas zanima.

Poskusimo nekaj drugega. Dodajmo nove stolpce za vsako leto:

| Mesto    | Država        | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokio    | Japonska      | 1445 | 1874 | 1690 |
| Atlanta  | Združene države Amerike | 1779 | 1111 | 1683 |
| Auckland | Nova Zelandija| 1386 | 942  | 1176 |

Čeprav se s tem izognemo podvajanju vrstic, se pojavijo še nekateri drugi izzivi. Vsakič, ko pride novo leto, bi morali spremeniti strukturo naše tabele. Poleg tega bo z rastjo podatkov imeti leta kot stolpce otežilo pridobivanje in izračun vrednosti.

Zato potrebujemo več tabel in relacij. Z razdelitvijo podatkov se lahko izognemo podvajanju in imamo večjo prilagodljivost pri delu s podatki.

## Koncepti relacij

Vrnimo se k našim podatkom in določimo, kako jih želimo razdeliti. Vemo, da želimo shraniti ime in državo za naša mesta, zato bo to verjetno najbolje v eni tabeli.

| Mesto    | Država        |
| -------- | ------------- |
| Tokio    | Japonska      |
| Atlanta  | Združene države Amerike |
| Auckland | Nova Zelandija|

Preden ustvarimo naslednjo tabelo, moramo ugotoviti, kako bomo sklicevali na vsako mesto. Potrebujemo nekakšen identifikator, ID ali (v tehničnih izrazih baz podatkov) primarni ključ. Primarni ključ je vrednost, ki se uporablja za identifikacijo ene specifične vrstice v tabeli. Čeprav bi lahko temeljil na sami vrednosti (na primer lahko uporabimo ime mesta), bi moral skoraj vedno biti številka ali drug identifikator. Ne želimo, da se ID kdaj spremeni, saj bi to prekinilo relacijo. V večini primerov bo primarni ključ ali ID samodejno generirana številka.

> ✅ Primarni ključ je pogosto okrajšan kot PK

### mesta

| mesto_id | Mesto    | Država        |
| -------- | -------- | ------------- |
| 1        | Tokio    | Japonska      |
| 2        | Atlanta  | Združene države Amerike |
| 3        | Auckland | Nova Zelandija|

> ✅ Opazili boste, da v tej lekciji uporabljamo izraza "id" in "primarni ključ" izmenično. Koncepti tukaj veljajo tudi za DataFrame-e, ki jih boste raziskali kasneje. DataFrame-i ne uporabljajo terminologije "primarni ključ", vendar boste opazili, da se obnašajo na podoben način.

Ko imamo tabelo mest, shranimo podatke o padavinah. Namesto da podvajamo celotne informacije o mestu, lahko uporabimo ID. Prav tako moramo zagotoviti, da ima nova tabela stolpec *id*, saj bi morale vse tabele imeti id ali primarni ključ.

### padavine

| padavine_id | mesto_id | Leto | Količina |
| ----------- | -------- | ---- | -------- |
| 1           | 1        | 2018 | 1445     |
| 2           | 1        | 2019 | 1874     |
| 3           | 1        | 2020 | 1690     |
| 4           | 2        | 2018 | 1779     |
| 5           | 2        | 2019 | 1111     |
| 6           | 2        | 2020 | 1683     |
| 7           | 3        | 2018 | 1386     |
| 8           | 3        | 2019 | 942      |
| 9           | 3        | 2020 | 1176     |

Opazite stolpec **mesto_id** v novi tabeli **padavine**. Ta stolpec vsebuje vrednosti, ki se sklicujejo na ID-je v tabeli **mesta**. V tehničnih izrazih relacijskih podatkov je to imenovano **tuji ključ**; to je primarni ključ iz druge tabele. Lahko si ga predstavljate kot referenco ali kazalec. **mesto_id** 1 se nanaša na Tokio.

> [!NOTE] 
> Tuji ključ je pogosto okrajšan kot FK

## Pridobivanje podatkov

Ker imamo podatke razdeljene v dve tabeli, se morda sprašujete, kako jih pridobimo. Če uporabljamo relacijsko bazo podatkov, kot so MySQL, SQL Server ali Oracle, lahko uporabimo jezik, imenovan Structured Query Language ali SQL. SQL (včasih izgovorjen kot "sequel") je standardni jezik za pridobivanje in spreminjanje podatkov v relacijski bazi podatkov.

Za pridobivanje podatkov uporabite ukaz `SELECT`. V osnovi **izberete** stolpce, ki jih želite videti, **iz** tabele, v kateri so shranjeni. Če želite prikazati samo imena mest, lahko uporabite naslednje:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` je mesto, kjer navedete stolpce, `FROM` pa je mesto, kjer navedete tabele.

> [!NOTE] 
> Sintaksa SQL ni občutljiva na velike in male črke, kar pomeni, da `select` in `SELECT` pomenita isto. Vendar pa so stolpci in tabele lahko občutljivi na velike in male črke, odvisno od vrste baze podatkov, ki jo uporabljate. Zato je najboljša praksa, da v programiranju vedno obravnavate vse kot občutljivo na velike in male črke. Pri pisanju SQL poizvedb je običajna konvencija, da ključne besede pišemo z velikimi črkami.

Zgornja poizvedba bo prikazala vsa mesta. Predstavljajmo si, da želimo prikazati samo mesta na Novi Zelandiji. Potrebujemo nekakšen filter. SQL ključna beseda za to je `WHERE`, ali "kjer je nekaj resnično".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Združevanje podatkov

Do zdaj smo pridobivali podatke iz ene same tabele. Zdaj želimo združiti podatke iz obeh tabel **mesta** in **padavine**. To naredimo z *združevanjem* (join). Ustvarili boste povezavo med obema tabelama in ujemali vrednosti iz stolpca vsake tabele.

V našem primeru bomo ujemali stolpec **mesto_id** v tabeli **padavine** s stolpcem **mesto_id** v tabeli **mesta**. Tako bomo povezali vrednost padavin z ustreznim mestom. Tip združitve, ki ga bomo izvedli, se imenuje *notranja* združitev (inner join), kar pomeni, da se neujemajoče vrstice ne bodo prikazale. V našem primeru ima vsako mesto podatke o padavinah, zato bo vse prikazano.

Pridobimo podatke o padavinah za leto 2019 za vsa naša mesta.

To bomo naredili v korakih. Prvi korak je združiti podatke tako, da določimo stolpce za povezavo - **mesto_id**, kot smo že poudarili.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Poudarili smo dva stolpca, ki ju želimo, in dejstvo, da želimo združiti tabele po **mesto_id**. Zdaj lahko dodamo stavek `WHERE`, da filtriramo samo leto 2019.

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

## Povzetek

Relacijske baze podatkov temeljijo na razdelitvi informacij med več tabel, ki se nato združijo za prikaz in analizo. To omogoča visoko stopnjo prilagodljivosti za izvajanje izračunov in drugačno manipulacijo podatkov. Spoznali ste osnovne koncepte relacijske baze podatkov in kako izvesti združitev med dvema tabelama.

## 🚀 Izziv

Na internetu je na voljo veliko relacijskih baz podatkov. Podatke lahko raziskujete z uporabo veščin, ki ste jih pridobili zgoraj.

## Kviz po predavanju

## [Kviz po predavanju](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Pregled in samostojno učenje

Na voljo je več virov na [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum), kjer lahko nadaljujete z raziskovanjem SQL in konceptov relacijskih baz podatkov

- [Opis konceptov relacijskih podatkov](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Začetek poizvedovanja s Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL je različica SQL)
- [Vsebina SQL na Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Naloga

[Prikaz podatkov letališča](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->