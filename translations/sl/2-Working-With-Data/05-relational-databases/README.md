<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11b166fbcb7eaf82308cdc24b562f687",
  "translation_date": "2025-09-05T05:58:08+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "sl"
}
-->
# Delo z podatki: Relacijske baze podatkov

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Delo z podatki: Relacijske baze podatkov - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

Verjetno ste že kdaj uporabili preglednico za shranjevanje informacij. Imeli ste niz vrstic in stolpcev, kjer so vrstice vsebovale informacije (ali podatke), stolpci pa so opisovali te informacije (včasih imenovane metapodatki). Relacijska baza podatkov temelji na tem osnovnem principu stolpcev in vrstic v tabelah, kar omogoča razporeditev informacij med več tabelami. To vam omogoča delo z bolj zapletenimi podatki, izogibanje podvajanju in večjo prilagodljivost pri raziskovanju podatkov. Raziskali bomo koncepte relacijske baze podatkov.

## [Predhodni kviz](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Vse se začne s tabelami

Jedro relacijske baze podatkov so tabele. Tako kot pri preglednici je tabela zbirka stolpcev in vrstic. Vrstica vsebuje podatke ali informacije, s katerimi želimo delati, kot so ime mesta ali količina padavin. Stolpci opisujejo podatke, ki jih hranijo.

Začnimo z raziskovanjem tako, da ustvarimo tabelo za shranjevanje informacij o mestih. Morda začnemo z njihovim imenom in državo. To bi lahko shranili v tabelo, kot je prikazano spodaj:

| Mesto    | Država        |
| -------- | ------------- |
| Tokio    | Japonska      |
| Atlanta  | Združene države |
| Auckland | Nova Zelandija |

Opazite, da imena stolpcev **mesto**, **država** in **prebivalstvo** opisujejo podatke, ki se hranijo, vsaka vrstica pa vsebuje informacije o enem mestu.

## Pomanjkljivosti pristopa z eno tabelo

Verjetno se vam zgornja tabela zdi precej znana. Dodajmo nekaj dodatnih podatkov v našo nastajajočo bazo podatkov - letne padavine (v milimetrih). Osredotočili se bomo na leta 2018, 2019 in 2020. Če bi jih dodali za Tokio, bi to izgledalo nekako takole:

| Mesto | Država | Leto | Količina |
| ----- | ------- | ---- | ------ |
| Tokio | Japonska | 2020 | 1690   |
| Tokio | Japonska | 2019 | 1874   |
| Tokio | Japonska | 2018 | 1445   |

Kaj opazite pri naši tabeli? Morda opazite, da podvajamo ime in državo mesta znova in znova. To bi lahko zavzelo precej prostora za shranjevanje, kar je večinoma nepotrebno. Navsezadnje ima Tokio samo eno ime, ki nas zanima.

OK, poskusimo nekaj drugega. Dodajmo nove stolpce za vsako leto:

| Mesto    | Država        | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokio    | Japonska      | 1445 | 1874 | 1690 |
| Atlanta  | Združene države | 1779 | 1111 | 1683 |
| Auckland | Nova Zelandija | 1386 | 942  | 1176 |

Čeprav se s tem izognemo podvajanju vrstic, to prinaša nekaj drugih izzivov. Strukturo tabele bi morali spreminjati vsakič, ko se pojavi novo leto. Poleg tega bo z rastjo naših podatkov uporaba let kot stolpcev otežila pridobivanje in izračunavanje vrednosti.

Zato potrebujemo več tabel in relacije. Z razdelitvijo podatkov se lahko izognemo podvajanju in pridobimo večjo prilagodljivost pri delu s podatki.

## Koncepti relacij

Vrnimo se k našim podatkom in določimo, kako jih želimo razdeliti. Vemo, da želimo shraniti ime in državo za naša mesta, zato bo to verjetno najbolje delovalo v eni tabeli.

| Mesto    | Država        |
| -------- | ------------- |
| Tokio    | Japonska      |
| Atlanta  | Združene države |
| Auckland | Nova Zelandija |

Preden ustvarimo naslednjo tabelo, moramo ugotoviti, kako bomo sklicevali na vsako mesto. Potrebujemo neko obliko identifikatorja, ID ali (v tehničnih izrazih baze podatkov) primarni ključ. Primarni ključ je vrednost, ki se uporablja za identifikacijo ene specifične vrstice v tabeli. Čeprav bi to lahko temeljilo na sami vrednosti (na primer lahko uporabimo ime mesta), bi moral biti skoraj vedno številka ali drug identifikator. Ne želimo, da se ID kdaj spremeni, saj bi to prekinilo relacijo. V večini primerov bo primarni ključ ali ID samodejno generirana številka.

> ✅ Primarni ključ je pogosto okrajšan kot PK

### mesta

| mesto_id | Mesto    | Država        |
| -------- | -------- | ------------- |
| 1        | Tokio    | Japonska      |
| 2        | Atlanta  | Združene države |
| 3        | Auckland | Nova Zelandija |

> ✅ Opazili boste, da izraze "id" in "primarni ključ" uporabljamo izmenično med to lekcijo. Koncepti tukaj veljajo za DataFrames, ki jih boste raziskovali kasneje. DataFrames ne uporabljajo terminologije "primarni ključ", vendar boste opazili, da se obnašajo zelo podobno.

Ko smo ustvarili tabelo mest, shranimo padavine. Namesto da podvajamo celotne informacije o mestu, lahko uporabimo ID. Prav tako moramo zagotoviti, da ima na novo ustvarjena tabela stolpec *id*, saj bi morale vse tabele imeti ID ali primarni ključ.

### padavine

| padavine_id | mesto_id | Leto | Količina |
| ----------- | -------- | ---- | ------ |
| 1           | 1        | 2018 | 1445   |
| 2           | 1        | 2019 | 1874   |
| 3           | 1        | 2020 | 1690   |
| 4           | 2        | 2018 | 1779   |
| 5           | 2        | 2019 | 1111   |
| 6           | 2        | 2020 | 1683   |
| 7           | 3        | 2018 | 1386   |
| 8           | 3        | 2019 | 942    |
| 9           | 3        | 2020 | 1176   |

Opazite stolpec **mesto_id** znotraj na novo ustvarjene tabele **padavine**. Ta stolpec vsebuje vrednosti, ki se sklicujejo na ID-je v tabeli **mesta**. V tehničnih relacijskih podatkovnih izrazih se to imenuje **tuji ključ**; to je primarni ključ iz druge tabele. Lahko si ga preprosto predstavljate kot referenco ali kazalec. **mesto_id** 1 se sklicuje na Tokio.

> [!NOTE] Tuji ključ je pogosto okrajšan kot FK

## Pridobivanje podatkov

Ko so naši podatki razdeljeni v dve tabeli, se morda sprašujete, kako jih pridobiti. Če uporabljamo relacijsko bazo podatkov, kot so MySQL, SQL Server ali Oracle, lahko uporabimo jezik, imenovan Structured Query Language ali SQL. SQL (včasih izgovorjen kot "sequel") je standardni jezik, ki se uporablja za pridobivanje in spreminjanje podatkov v relacijski bazi podatkov.

Za pridobivanje podatkov uporabite ukaz `SELECT`. V osnovi **izberete** stolpce, ki jih želite videti **iz** tabele, v kateri so vsebovani. Če želite prikazati samo imena mest, lahko uporabite naslednje:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` je mesto, kjer navedete stolpce, `FROM` pa mesto, kjer navedete tabele.

> [NOTE] Sintaksa SQL ni občutljiva na velike in male črke, kar pomeni, da `select` in `SELECT` pomenita isto. Vendar pa so lahko stolpci in tabele, odvisno od vrste baze podatkov, občutljivi na velike in male črke. Zato je dobra praksa, da vse v programiranju obravnavate, kot da je občutljivo na velike in male črke. Pri pisanju SQL poizvedb je običajna konvencija, da ključne besede pišete z velikimi črkami.

Zgornja poizvedba bo prikazala vsa mesta. Predstavljajte si, da želimo prikazati samo mesta v Novi Zelandiji. Potrebujemo neko obliko filtra. Ključna beseda SQL za to je `WHERE`, ali "kjer nekaj drži".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Združevanje podatkov

Do zdaj smo pridobivali podatke iz ene same tabele. Zdaj želimo združiti podatke iz obeh tabel **mesta** in **padavine**. To se naredi z *združevanjem* tabel. Ustvarili boste povezavo med obema tabelama in uskladili vrednosti iz stolpca vsake tabele.

V našem primeru bomo uskladili stolpec **mesto_id** v tabeli **padavine** s stolpcem **mesto_id** v tabeli **mesta**. To bo uskladilo vrednost padavin z ustreznim mestom. Vrsta združitve, ki jo bomo izvedli, se imenuje *notranja* združitev, kar pomeni, da vrstice, ki se ne ujemajo z ničemer iz druge tabele, ne bodo prikazane. V našem primeru ima vsako mesto padavine, zato bo vse prikazano.

Pridobimo podatke o padavinah za leto 2019 za vsa naša mesta.

To bomo naredili v korakih. Prvi korak je združitev podatkov z navedbo stolpcev za povezavo - **mesto_id**, kot je bilo poudarjeno prej.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Poudarili smo dva stolpca, ki ju želimo, in dejstvo, da želimo združiti tabele z **mesto_id**. Zdaj lahko dodamo stavek `WHERE`, da filtriramo samo leto 2019.

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

Relacijske baze podatkov temeljijo na razdelitvi informacij med več tabel, ki se nato združijo za prikaz in analizo. To zagotavlja visoko stopnjo prilagodljivosti za izvajanje izračunov in drugačno manipulacijo podatkov. Spoznali ste osnovne koncepte relacijske baze podatkov in kako izvesti združitev med dvema tabelama.

## 🚀 Izziv

Na internetu je na voljo veliko relacijskih baz podatkov. Raziskujte podatke z uporabo veščin, ki ste se jih naučili zgoraj.

## Kviz po predavanju

## [Kviz po predavanju](https://ff-quizzes.netlify.app/en/ds/)

## Pregled in samostojno učenje

Na voljo je več virov na [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum), ki vam omogočajo nadaljnje raziskovanje konceptov SQL in relacijskih baz podatkov.

- [Opis konceptov relacijskih podatkov](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Začnite z poizvedbami v Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL je različica SQL)
- [SQL vsebine na Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Naloga

[Naslov naloge](assignment.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.