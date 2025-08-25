<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01d1b493e8b51a6ebb42524f6b1bcfff",
  "translation_date": "2025-08-24T21:44:36+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/assignment.md",
  "language_code": "pl"
}
-->
# Małe badanie nad cukrzycą

W tym zadaniu będziemy pracować z małym zestawem danych pacjentów z cukrzycą, pobranym z [tutaj](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

|   | WIEK | PŁEĆ | BMI | BP | S1 | S2 | S3 | S4 | S5 | S6 | Y  |
|---|------|------|-----|----|----|----|----|----|----|----|----|
| 0 | 59   | 2    | 32.1 | 101. | 157 | 93.2 | 38.0 | 4. | 4.8598 | 87 | 151 |
| 1 | 48   | 1    | 21.6 | 87.0 | 183 | 103.2 | 70. | 3. | 3.8918 | 69 | 75 |
| 2 | 72   | 2    | 30.5 | 93.0 | 156 | 93.6 | 41.0 | 4.0 | 4. | 85 | 141 |
| ... | ... | ... | ... | ...| ...| ...| ...| ...| ...| ...| ... |

## Instrukcje

* Otwórz [notatnik zadania](../../../../1-Introduction/04-stats-and-probability/assignment.ipynb) w środowisku jupyter notebook
* Wykonaj wszystkie zadania wymienione w notatniku, mianowicie:
   * [ ] Oblicz średnie wartości i wariancję dla wszystkich zmiennych
   * [ ] Narysuj wykresy pudełkowe dla BMI, BP i Y w zależności od płci
   * [ ] Jaka jest dystrybucja zmiennych Wiek, Płeć, BMI i Y?
   * [ ] Przetestuj korelację między różnymi zmiennymi a postępem choroby (Y)
   * [ ] Przetestuj hipotezę, że stopień postępu cukrzycy różni się między mężczyznami a kobietami
   
## Kryteria oceny

Wzorowe | Zadowalające | Wymaga poprawy
--- | --- | --- |
Wszystkie wymagane zadania są wykonane, zilustrowane graficznie i wyjaśnione | Większość zadań jest wykonana, brakuje wyjaśnień lub wniosków z wykresów i/lub uzyskanych wartości | Wykonane są tylko podstawowe zadania, takie jak obliczenie średniej/wariancji i podstawowe wykresy, brak wniosków z danych

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.