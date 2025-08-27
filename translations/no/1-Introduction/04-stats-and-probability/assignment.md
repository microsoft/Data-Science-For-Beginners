<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01d1b493e8b51a6ebb42524f6b1bcfff",
  "translation_date": "2025-08-26T21:48:19+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/assignment.md",
  "language_code": "no"
}
-->
# Liten Diabetesstudie

I denne oppgaven skal vi jobbe med et lite datasett av diabetespasienter hentet fra [her](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

|   | ALDER | KJØNN | BMI | BP | S1 | S2 | S3 | S4 | S5 | S6 | Y  |
|---|-------|-------|-----|----|----|----|----|----|----|----|----|
| 0 | 59    | 2     | 32.1 | 101. | 157 | 93.2 | 38.0 | 4. | 4.8598 | 87 | 151 |
| 1 | 48    | 1     | 21.6 | 87.0 | 183 | 103.2 | 70. | 3. | 3.8918 | 69 | 75 |
| 2 | 72    | 2     | 30.5 | 93.0 | 156 | 93.6 | 41.0 | 4.0 | 4. | 85 | 141 |
| ... | ... | ...   | ...  | ...  | ... | ... | ... | ... | ... | ... | ... |

## Instruksjoner

* Åpne [oppgavenotatboken](assignment.ipynb) i et jupyter-notatbokmiljø
* Fullfør alle oppgaver som er listet opp i notatboken, nemlig:
   * [ ] Beregn gjennomsnittsverdier og varians for alle verdier
   * [ ] Lag boksplott for BMI, BP og Y avhengig av kjønn
   * [ ] Hva er fordelingen av variablene Alder, Kjønn, BMI og Y?
   * [ ] Test korrelasjonen mellom ulike variabler og sykdomsprogresjon (Y)
   * [ ] Test hypotesen om at graden av diabetesprogresjon er forskjellig mellom menn og kvinner
   
## Vurderingskriterier

Eksemplarisk | Tilfredsstillende | Trenger forbedring
--- | --- | -- |
Alle påkrevde oppgaver er fullført, grafisk illustrert og forklart | De fleste oppgavene er fullført, forklaringer eller konklusjoner fra grafer og/eller oppnådde verdier mangler | Kun grunnleggende oppgaver som beregning av gjennomsnitt/varians og enkle grafer er fullført, ingen konklusjoner er gjort fra dataene

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.