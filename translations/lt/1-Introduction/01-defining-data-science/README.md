<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a0516588d172f82f35f7a0d4a001e5d0",
  "translation_date": "2025-09-05T16:15:07+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "lt"
}
-->
## Duomenų tipai

Kaip jau minėjome, duomenys yra visur. Tereikia juos tinkamai užfiksuoti! Naudinga atskirti **struktūrizuotus** ir **nestruktūrizuotus** duomenis. Struktūrizuoti duomenys paprastai pateikiami gerai organizuota forma, dažniausiai lentelėje ar kelių lentelių pavidalu, o nestruktūrizuoti duomenys yra tiesiog failų rinkinys. Kartais galime kalbėti ir apie **pusiau struktūrizuotus** duomenis, kurie turi tam tikrą struktūrą, tačiau ji gali labai skirtis.

| Struktūrizuoti                                                              | Pusiau struktūrizuoti                                                                         | Nestruktūrizuoti                        |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------- |
| Žmonių sąrašas su jų telefono numeriais                                      | Vikipedijos puslapiai su nuorodomis                                                          | Enciklopedijos Britannica tekstas       |
| Temperatūra visose pastato patalpose kas minutę per pastaruosius 20 metų     | Mokslinių straipsnių rinkinys JSON formatu su autoriais, publikavimo data ir santrauka        | Failų saugykla su įmonės dokumentais    |
| Duomenys apie amžių ir lytį visų žmonių, įeinančių į pastatą                 | Interneto puslapiai                                                                          | Neapdorotas vaizdo įrašas iš stebėjimo kameros |

## Kur gauti duomenų

Yra daugybė galimų duomenų šaltinių, ir būtų neįmanoma išvardyti visų! Tačiau paminėkime keletą tipinių vietų, kur galima gauti duomenų:

* **Struktūrizuoti**
  - **Daiktų internetas** (IoT), įskaitant duomenis iš įvairių jutiklių, tokių kaip temperatūros ar slėgio jutikliai, teikia daug naudingų duomenų. Pavyzdžiui, jei biurų pastatas yra aprūpintas IoT jutikliais, galime automatiškai valdyti šildymą ir apšvietimą, kad sumažintume išlaidas.
  - **Apklausos**, kurias prašome vartotojų užpildyti po pirkimo ar apsilankymo svetainėje.
  - **Elgsenos analizė** gali padėti suprasti, kaip giliai vartotojas naršo svetainėje ir kokios yra tipinės priežastys, kodėl jis ją palieka.
* **Nestruktūrizuoti**
  - **Tekstai** gali būti turtingas įžvalgų šaltinis, pavyzdžiui, bendras **nuotaikos balas** arba raktažodžių ir semantinės prasmės išgavimas.
  - **Vaizdai** ar **vaizdo įrašai**. Vaizdo įrašas iš stebėjimo kameros gali būti naudojamas eismo intensyvumui kelyje įvertinti ir informuoti žmones apie galimus kamščius.
  - Interneto serverio **žurnalai** gali padėti suprasti, kurie mūsų svetainės puslapiai yra dažniausiai lankomi ir kiek laiko.
* **Pusiau struktūrizuoti**
  - **Socialinių tinklų** grafai gali būti puikūs duomenų šaltiniai apie vartotojų asmenybes ir potencialų efektyvumą skleidžiant informaciją.
  - Kai turime daugybę nuotraukų iš vakarėlio, galime pabandyti išgauti **grupės dinamikos** duomenis, sudarydami žmonių, fotografuojančių vieni kitus, grafą.

Žinodami įvairius galimus duomenų šaltinius, galite pabandyti pagalvoti apie skirtingus scenarijus, kur duomenų mokslo metodai gali būti taikomi situacijai geriau suprasti ir verslo procesams tobulinti.

## Ką galima daryti su duomenimis

Duomenų moksle mes sutelkiame dėmesį į šiuos duomenų kelionės etapus:

Žinoma, priklausomai nuo konkrečių duomenų, kai kurie etapai gali būti praleisti (pvz., kai duomenys jau yra duomenų bazėje arba kai nereikia modelio mokymo), o kai kurie etapai gali būti kartojami kelis kartus (pvz., duomenų apdorojimas).

## Skaitmenizacija ir skaitmeninė transformacija

Pastarąjį dešimtmetį daugelis verslų pradėjo suprasti duomenų svarbą priimant verslo sprendimus. Norint taikyti duomenų mokslo principus verslo valdymui, pirmiausia reikia surinkti tam tikrus duomenis, t. y. verslo procesus paversti skaitmenine forma. Tai vadinama **skaitmenizacija**. Duomenų mokslo metodų taikymas šiems duomenims sprendimams priimti gali lemti reikšmingą produktyvumo padidėjimą (ar net verslo krypties pakeitimą), vadinamą **skaitmenine transformacija**.

Pažvelkime į pavyzdį. Tarkime, turime duomenų mokslo kursą (kaip šis), kurį pristatome internetu studentams, ir norime jį patobulinti pasitelkdami duomenų mokslą. Kaip tai galime padaryti?

Galime pradėti klausdami: „Ką galima skaitmenizuoti?“ Paprasčiausias būdas būtų matuoti laiką, kurio kiekvienam studentui reikia kiekvienam modulio užbaigimui, ir įvertinti įgytas žinias, pateikiant daugiapakopį testą modulio pabaigoje. Vidutiniškai apskaičiavę laiką, reikalingą modulio užbaigimui visiems studentams, galime nustatyti, kurie moduliai studentams kelia daugiausia sunkumų, ir dirbti ties jų supaprastinimu.
Galite teigti, kad toks požiūris nėra idealus, nes moduliai gali būti skirtingo ilgio. Tikriausiai būtų teisingiau laiką padalyti iš modulio ilgio (simbolių skaičiumi) ir palyginti šias reikšmes vietoj to.
Kai pradedame analizuoti daugybinio pasirinkimo testų rezultatus, galime pabandyti nustatyti, su kokiomis sąvokomis studentams sunkiausia susidoroti, ir naudoti šią informaciją turiniui tobulinti. Tam reikia sukurti testus taip, kad kiekvienas klausimas būtų susietas su tam tikra sąvoka ar žinių dalimi.

Jei norime eiti dar sudėtingesniu keliu, galime sudaryti grafiką, kuriame pavaizduotas laikas, praleistas kiekviename modulyje, palyginti su studentų amžiaus kategorijomis. Galime pastebėti, kad kai kurioms amžiaus grupėms užtrunka neproporcingai ilgai užbaigti modulį arba kad studentai meta mokymąsi jo nebaigę. Tai gali padėti pateikti amžiaus rekomendacijas moduliui ir sumažinti žmonių nusivylimą dėl neteisingų lūkesčių.

## 🚀 Iššūkis

Šiame iššūkyje bandysime rasti sąvokas, susijusias su duomenų mokslo sritimi, analizuodami tekstus. Paimsime Vikipedijos straipsnį apie duomenų mokslą, atsisiųsime ir apdorosime tekstą, o tada sukursime žodžių debesį, panašų į šį:

![Žodžių debesis apie duomenų mokslą](../../../../1-Introduction/01-defining-data-science/images/ds_wordcloud.png)

Apsilankykite [`notebook.ipynb`](../../../../../../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore'), kad peržiūrėtumėte kodą. Taip pat galite paleisti kodą ir pamatyti, kaip jis realiuoju laiku atlieka visus duomenų transformavimus.

> Jei nežinote, kaip paleisti kodą Jupyter Notebook aplinkoje, peržiūrėkite [šį straipsnį](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Po paskaitos testas](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Užduotys

* **Užduotis 1**: Pakeiskite aukščiau pateiktą kodą, kad rastumėte susijusias sąvokas **Didžiųjų duomenų** ir **Mašininio mokymosi** srityse.
* **Užduotis 2**: [Pagalvokite apie duomenų mokslo scenarijus](assignment.md)

## Autorystė

Šią pamoką su ♥️ parengė [Dmitry Soshnikov](http://soshnikov.com)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.