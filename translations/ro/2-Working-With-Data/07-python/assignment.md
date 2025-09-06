<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-26T14:51:58+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "ro"
}
-->
# Temă pentru Procesarea Datelor în Python

În această temă, vă vom cere să dezvoltați codul pe care l-am început în provocările noastre. Tema constă din două părți:

## Modelarea Răspândirii COVID-19

 - [ ] Desenați grafice *R* pentru 5-6 țări diferite pe un singur grafic pentru comparație sau folosind mai multe grafice alăturate.
 - [ ] Analizați cum numărul de decese și recuperări se corelează cu numărul de cazuri infectate.
 - [ ] Determinați cât durează, în medie, o boală, corelând vizual rata de infectare cu rata de decese și căutând anomalii. Este posibil să fie nevoie să analizați mai multe țări pentru a descoperi acest lucru.
 - [ ] Calculați rata de fatalitate și cum se schimbă aceasta în timp. *Este posibil să doriți să luați în considerare durata bolii în zile pentru a deplasa o serie temporală înainte de a face calculele.*

## Analiza Articolelor despre COVID-19

- [ ] Construiți o matrice de co-apariție pentru diferite medicamente și analizați care medicamente apar frecvent împreună (adică menționate într-un singur rezumat). Puteți modifica codul pentru construirea matricei de co-apariție pentru medicamente și diagnostice.
- [ ] Vizualizați această matrice folosind o hartă termică.
- [ ] Ca obiectiv suplimentar, vizualizați co-apariția medicamentelor folosind [diagrama chord](https://en.wikipedia.org/wiki/Chord_diagram). [Această bibliotecă](https://pypi.org/project/chord/) vă poate ajuta să desenați o diagramă chord.
- [ ] Ca un alt obiectiv suplimentar, extrageți dozele diferitelor medicamente (cum ar fi **400mg** în *luați 400mg de clorochină zilnic*) folosind expresii regulate și construiți un dataframe care arată diferite doze pentru diferite medicamente. **Notă**: luați în considerare valorile numerice care sunt în apropierea textuală a numelui medicamentului.

## Rubrică

Exemplar | Adecvat | Necesită Îmbunătățiri
--- | --- | -- |
Toate sarcinile sunt complete, ilustrate grafic și explicate, incluzând cel puțin unul dintre cele două obiective suplimentare | Mai mult de 5 sarcini sunt complete, niciun obiectiv suplimentar nu este încercat sau rezultatele nu sunt clare | Mai puțin de 5 (dar mai mult de 3) sarcini sunt complete, vizualizările nu ajută la demonstrarea punctului

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți de faptul că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.