<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01d1b493e8b51a6ebb42524f6b1bcfff",
  "translation_date": "2025-08-26T15:42:57+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/assignment.md",
  "language_code": "ro"
}
-->
# Studiu Mic despre Diabet

În această temă, vom lucra cu un set de date mic despre pacienți cu diabet, preluat de [aici](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

|   | VÂRSTĂ | SEX | IMC | TA | S1 | S2 | S3 | S4 | S5 | S6 | Y  |
|---|--------|-----|-----|----|----|----|----|----|----|----|----|
| 0 | 59     | 2   | 32.1 | 101. | 157 | 93.2 | 38.0 | 4. | 4.8598 | 87 | 151 |
| 1 | 48     | 1   | 21.6 | 87.0 | 183 | 103.2 | 70. | 3. | 3.8918 | 69 | 75 |
| 2 | 72     | 2   | 30.5 | 93.0 | 156 | 93.6 | 41.0 | 4.0 | 4. | 85 | 141 |
| ... | ...  | ... | ...  | ...  | ... | ...  | ...  | ... | ... | ... | ... |

## Instrucțiuni

* Deschide [notebook-ul temei](assignment.ipynb) într-un mediu jupyter notebook
* Completează toate sarcinile listate în notebook, și anume:
   * [ ] Calculează valorile medii și varianța pentru toate valorile
   * [ ] Realizează boxplot-uri pentru IMC, TA și Y în funcție de gen
   * [ ] Care este distribuția variabilelor Vârstă, Sex, IMC și Y?
   * [ ] Testează corelația dintre diferite variabile și progresia bolii (Y)
   * [ ] Testează ipoteza conform căreia gradul de progresie a diabetului este diferit între bărbați și femei
   
## Criterii de Evaluare

Exemplar | Adecvat | Necesită Îmbunătățiri
--- | --- | -- |
Toate sarcinile cerute sunt complete, ilustrate grafic și explicate | Majoritatea sarcinilor sunt complete, dar lipsesc explicațiile sau concluziile din grafice și/sau valorile obținute | Doar sarcinile de bază, cum ar fi calculul mediei/varianței și graficele simple, sunt complete, fără concluzii din date

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.