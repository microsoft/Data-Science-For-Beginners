<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-26T21:07:25+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "da"
}
-->
# Opgave i Databehandling med Python

I denne opgave vil vi bede dig om at uddybe den kode, vi er begyndt at udvikle i vores udfordringer. Opgaven består af to dele:

## COVID-19 Spredningsmodellering

 - [ ] Plot *R* grafer for 5-6 forskellige lande på én graf til sammenligning, eller brug flere grafer side om side.
 - [ ] Undersøg, hvordan antallet af dødsfald og helbredelser korrelerer med antallet af smittede tilfælde.
 - [ ] Find ud af, hvor længe en typisk sygdom varer ved visuelt at korrelere smittehastighed og dødsrate og lede efter nogle afvigelser. Du kan være nødt til at kigge på forskellige lande for at finde ud af det.
 - [ ] Beregn dødelighedsraten, og hvordan den ændrer sig over tid. *Du kan overveje at tage sygdommens varighed i dage med i betragtning for at forskyde én tidsserie, før du udfører beregningerne.*

## Analyse af COVID-19 Artikler

- [ ] Byg en co-occurrence matrix for forskellige medicinpræparater, og se hvilke medicinpræparater der ofte nævnes sammen (dvs. nævnt i samme abstrakt). Du kan tilpasse koden til at bygge en co-occurrence matrix for medicin og diagnoser.
- [ ] Visualisér denne matrix ved hjælp af et heatmap.
- [ ] Som en ekstra udfordring, visualisér co-occurrence af medicin ved hjælp af [chord diagram](https://en.wikipedia.org/wiki/Chord_diagram). [Dette bibliotek](https://pypi.org/project/chord/) kan hjælpe dig med at tegne et chord diagram.
- [ ] Som en anden ekstra udfordring, udtræk doseringer af forskellige medicinpræparater (såsom **400mg** i *tag 400mg chloroquine dagligt*) ved hjælp af regulære udtryk, og byg en dataframe, der viser forskellige doseringer for forskellige medicinpræparater. **Bemærk**: Overvej numeriske værdier, der er i tæt tekstnærhed til medicinnavnet.

## Bedømmelseskriterier

Eksemplarisk | Tilstrækkelig | Kræver Forbedring
--- | --- | -- |
Alle opgaver er fuldført, grafisk illustreret og forklaret, inklusive mindst ét af de to ekstra mål | Mere end 5 opgaver er fuldført, ingen ekstra mål er forsøgt, eller resultaterne er ikke klare | Færre end 5 (men mere end 3) opgaver er fuldført, visualiseringer hjælper ikke med at demonstrere pointen

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.