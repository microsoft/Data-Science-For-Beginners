<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-31T05:41:18+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "lt"
}
-->
# Oro uostų duomenų rodymas

Jums buvo pateikta [duomenų bazė](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db), sukurta naudojant [SQLite](https://sqlite.org/index.html), kurioje yra informacija apie oro uostus. Žemiau pateikta schemos struktūra. Naudosite [SQLite plėtinį](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) programoje [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum), kad galėtumėte peržiūrėti informaciją apie įvairių miestų oro uostus.

## Instrukcijos

Norėdami pradėti užduotį, turėsite atlikti kelis veiksmus. Reikės įdiegti keletą įrankių ir atsisiųsti pavyzdinę duomenų bazę.

### Sistemos paruošimas

Galite naudoti Visual Studio Code ir SQLite plėtinį, kad galėtumėte dirbti su duomenų baze.

1. Eikite į [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) ir vykdykite instrukcijas, kad įdiegtumėte Visual Studio Code
1. Įdiekite [SQLite plėtinį](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum), kaip nurodyta Marketplace puslapyje

### Atsisiųskite ir atidarykite duomenų bazę

Toliau atsisiųskite ir atidarykite duomenų bazę.

1. Atsisiųskite [duomenų bazės failą iš GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) ir išsaugokite jį kataloge
1. Atidarykite Visual Studio Code
1. Atidarykite duomenų bazę SQLite plėtinyje, paspausdami **Ctl-Shift-P** (arba **Cmd-Shift-P** Mac kompiuteryje) ir įvesdami `SQLite: Open database`
1. Pasirinkite **Choose database from file** ir atidarykite **airports.db** failą, kurį atsisiuntėte anksčiau
1. Atidarę duomenų bazę (ekrane nebus matomas atnaujinimas), sukurkite naują užklausų langą, paspausdami **Ctl-Shift-P** (arba **Cmd-Shift-P** Mac kompiuteryje) ir įvesdami `SQLite: New query`

Kai langas atidarytas, jį galima naudoti SQL užklausoms vykdyti prieš duomenų bazę. Užklausas galite vykdyti naudodami komandą **Ctl-Shift-Q** (arba **Cmd-Shift-Q** Mac kompiuteryje).

> [!NOTE] Daugiau informacijos apie SQLite plėtinį galite rasti [dokumentacijoje](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Duomenų bazės schema

Duomenų bazės schema – tai jos lentelių dizainas ir struktūra. **airports** duomenų bazėje yra dvi lentelės: `cities`, kurioje pateikiamas Jungtinės Karalystės ir Airijos miestų sąrašas, ir `airports`, kurioje pateikiamas visų oro uostų sąrašas. Kadangi kai kuriuose miestuose gali būti keli oro uostai, buvo sukurtos dvi lentelės informacijai saugoti. Šioje užduotyje naudosite sujungimus (joins), kad galėtumėte peržiūrėti informaciją apie skirtingus miestus.

| Miestai           |
| ----------------- |
| id (PK, sveikasis skaičius) |
| city (tekstas)    |
| country (tekstas) |

| Oro uostai                        |
| --------------------------------- |
| id (PK, sveikasis skaičius)       |
| name (tekstas)                    |
| code (tekstas)                    |
| city_id (FK į id lentelėje **Cities**) |

## Užduotis

Sukurkite užklausas, kurios pateiktų šią informaciją:

1. visų miestų pavadinimus iš `Cities` lentelės
1. visus Airijos miestus iš `Cities` lentelės
1. visų oro uostų pavadinimus su jų miestu ir šalimi
1. visus oro uostus Londone, Jungtinėje Karalystėje

## Vertinimo kriterijai

| Puikiai | Pakankamai | Reikia tobulinti |
| -------- | ---------- | ---------------- |

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.