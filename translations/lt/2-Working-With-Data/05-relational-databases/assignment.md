<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:59:27+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "lt"
}
-->
# Oro uostų duomenų rodymas

Jums buvo pateikta [duomenų bazė](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db), sukurta naudojant [SQLite](https://sqlite.org/index.html), kurioje yra informacija apie oro uostus. Schema pateikta žemiau. Naudosite [SQLite plėtinį](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) programoje [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum), kad galėtumėte rodyti informaciją apie įvairių miestų oro uostus.

## Instrukcijos

Norėdami pradėti užduotį, turėsite atlikti kelis veiksmus. Jums reikės įdiegti keletą įrankių ir atsisiųsti pavyzdinę duomenų bazę.

### Sistemos paruošimas

Galite naudoti Visual Studio Code ir SQLite plėtinį, kad galėtumėte sąveikauti su duomenų baze.

1. Eikite į [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) ir vadovaukitės instrukcijomis, kad įdiegtumėte Visual Studio Code
1. Įdiekite [SQLite plėtinį](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum), kaip nurodyta Marketplace puslapyje

### Atsisiųskite ir atidarykite duomenų bazę

Toliau atsisiųskite ir atidarykite duomenų bazę.

1. Atsisiųskite [duomenų bazės failą iš GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) ir išsaugokite jį kataloge
1. Atidarykite Visual Studio Code
1. Atidarykite duomenų bazę SQLite plėtinyje, pasirinkdami **Ctl-Shift-P** (arba **Cmd-Shift-P** Mac kompiuteryje) ir įvesdami `SQLite: Open database`
1. Pasirinkite **Choose database from file** ir atidarykite **airports.db** failą, kurį atsisiuntėte anksčiau
1. Atidarius duomenų bazę (ekrane nebus matomas atnaujinimas), sukurkite naują užklausos langą, pasirinkdami **Ctl-Shift-P** (arba **Cmd-Shift-P** Mac kompiuteryje) ir įvesdami `SQLite: New query`

Atidarius, naujas užklausos langas gali būti naudojamas SQL užklausoms vykdyti prieš duomenų bazę. Galite naudoti komandą **Ctl-Shift-Q** (arba **Cmd-Shift-Q** Mac kompiuteryje), kad vykdytumėte užklausas prieš duomenų bazę.

> [!NOTE] 
> Daugiau informacijos apie SQLite plėtinį galite rasti [dokumentacijoje](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum)

## Duomenų bazės schema

Duomenų bazės schema yra jos lentelių dizainas ir struktūra. **airports** duomenų bazė turi dvi lenteles: `cities`, kurioje yra Jungtinės Karalystės ir Airijos miestų sąrašas, ir `airports`, kurioje yra visų oro uostų sąrašas. Kadangi kai kuriuose miestuose gali būti keli oro uostai, buvo sukurtos dvi lentelės informacijai saugoti. Šioje užduotyje naudosite sujungimus, kad galėtumėte rodyti informaciją apie skirtingus miestus.

| Miestai           |
| ----------------- |
| id (PK, sveikasis skaičius) |
| city (tekstinis)  |
| country (tekstinis) |

| Oro uostai                        |
| --------------------------------- |
| id (PK, sveikasis skaičius)       |
| name (tekstinis)                  |
| code (tekstinis)                  |
| city_id (FK į id lentelėje **Cities**) |

## Užduotis

Sukurkite užklausas, kad gautumėte šią informaciją:

1. visų miestų pavadinimus iš `Cities` lentelės
1. visus Airijos miestus iš `Cities` lentelės
1. visų oro uostų pavadinimus su jų miestu ir šalimi
1. visus oro uostus Londone, Jungtinėje Karalystėje

## Vertinimo kriterijai

| Puikiai | Pakankamai | Reikia tobulinti |
| -------- | ---------- | ---------------- |

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.