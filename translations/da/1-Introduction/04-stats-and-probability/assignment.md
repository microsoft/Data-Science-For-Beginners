<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01d1b493e8b51a6ebb42524f6b1bcfff",
  "translation_date": "2025-08-26T21:48:09+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/assignment.md",
  "language_code": "da"
}
-->
# Lille Diabetesundersøgelse

I denne opgave skal vi arbejde med et lille datasæt af diabetespatienter taget fra [her](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

|   | ALDER | KØN | BMI | BP | S1 | S2 | S3 | S4 | S5 | S6 | Y  |
|---|-------|-----|-----|----|----|----|----|----|----|----|----|
| 0 | 59 | 2 | 32.1 | 101. | 157 | 93.2 | 38.0 | 4. | 4.8598 | 87 | 151 |
| 1 | 48 | 1 | 21.6 | 87.0 | 183 | 103.2 | 70. | 3. | 3.8918 | 69 | 75 |
| 2 | 72 | 2 | 30.5 | 93.0 | 156 | 93.6 | 41.0 | 4.0 | 4. | 85 | 141 |
| ... | ... | ... | ... | ...| ...| ...| ...| ...| ...| ...| ... |

## Instruktioner

* Åbn [opgavenotebooken](assignment.ipynb) i et jupyter notebook-miljø
* Fuldfør alle opgaver, der er angivet i notebooken, nemlig:
   * [ ] Beregn gennemsnitsværdier og varians for alle værdier
   * [ ] Lav boksdiagrammer for BMI, BP og Y afhængigt af køn
   * [ ] Hvad er fordelingen af variablerne Alder, Køn, BMI og Y?
   * [ ] Test korrelationen mellem forskellige variabler og sygdomsprogression (Y)
   * [ ] Test hypotesen om, at graden af diabetesprogression er forskellig mellem mænd og kvinder
   
## Vurderingskriterier

Eksemplarisk | Tilstrækkelig | Kræver forbedring
--- | --- | -- |
Alle påkrævede opgaver er fuldført, grafisk illustreret og forklaret | De fleste opgaver er fuldført, forklaringer eller konklusioner fra grafer og/eller opnåede værdier mangler | Kun grundlæggende opgaver som beregning af gennemsnit/varians og grundlæggende diagrammer er fuldført, ingen konklusioner er lavet ud fra data

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.