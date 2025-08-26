<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-26T14:51:17+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "hu"
}
-->
# Feladat Pythonban történő adatfeldolgozáshoz

Ebben a feladatban arra kérünk, hogy dolgozd ki a kódot, amelyet a kihívásaink során elkezdtünk fejleszteni. A feladat két részből áll:

## COVID-19 terjedés modellezése

 - [ ] Készíts *R* grafikonokat 5-6 különböző ország számára egy grafikonon összehasonlítás céljából, vagy több grafikonon egymás mellett.
 - [ ] Vizsgáld meg, hogyan korrelálnak a halálesetek és a gyógyult esetek száma a fertőzött esetek számával.
 - [ ] Derítsd ki, hogy mennyi ideig tart egy tipikus betegség, vizuálisan korrelálva a fertőzési arányt és a halálozási arányt, és keresve néhány anomáliát. Ehhez lehet, hogy több országot is meg kell vizsgálnod.
 - [ ] Számítsd ki a halálozási arányt, és nézd meg, hogyan változik az idő múlásával. *Érdemes figyelembe venni a betegség hosszát napokban, hogy az egyik idősort eltolhasd a számítások előtt.*

## COVID-19 tanulmányok elemzése

- [ ] Készíts együtt-előfordulási mátrixot különböző gyógyszerekről, és nézd meg, mely gyógyszerek fordulnak elő gyakran együtt (azaz egy absztraktban említve). Módosíthatod a kódot a gyógyszerek és diagnózisok együtt-előfordulási mátrixának elkészítéséhez.
- [ ] Vizualizáld ezt a mátrixot hőtérképpel.
- [ ] Kihívásként vizualizáld a gyógyszerek együtt-előfordulását [chord diagram](https://en.wikipedia.org/wiki/Chord_diagram) segítségével. [Ez a könyvtár](https://pypi.org/project/chord/) segíthet chord diagramot rajzolni.
- [ ] Egy másik kihívásként, reguláris kifejezések segítségével nyerj ki különböző gyógyszerek adagolását (például **400mg** a *napi 400mg klorokin szedése* szövegben), és készíts adatkeretet, amely megmutatja a különböző gyógyszerek adagolását. **Megjegyzés**: vedd figyelembe a gyógyszer neve közelében található numerikus értékeket.

## Értékelési szempontok

Kiemelkedő | Megfelelő | Fejlesztésre szorul
--- | --- | -- |
Minden feladat teljesítve, grafikusan illusztrálva és magyarázva, beleértve legalább az egyik kihívást | Több mint 5 feladat teljesítve, kihívások nem kerültek megvalósításra, vagy az eredmények nem egyértelműek | Kevesebb mint 5 (de több mint 3) feladat teljesítve, a vizualizációk nem segítik a mondanivaló bemutatását

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.