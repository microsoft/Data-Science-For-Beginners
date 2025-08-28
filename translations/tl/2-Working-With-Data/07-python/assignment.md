<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-28T02:28:40+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "tl"
}
-->
# Takdang-Aralin para sa Pagproseso ng Data sa Python

Sa takdang-araling ito, hihilingin namin sa iyo na palawakin ang code na sinimulan naming buuin sa aming mga hamon. Ang takdang-aralin ay binubuo ng dalawang bahagi:

## Pagmomodelo ng Pagkalat ng COVID-19

 - [ ] I-plot ang *R* graphs para sa 5-6 na iba't ibang bansa sa isang graph para sa paghahambing, o gumamit ng ilang graphs na magkatabi.
 - [ ] Tingnan kung paano nauugnay ang bilang ng mga namatay at gumaling sa bilang ng mga nahawaang kaso.
 - [ ] Tukuyin kung gaano katagal ang karaniwang sakit sa pamamagitan ng biswal na pag-uugnay ng rate ng impeksyon at rate ng pagkamatay at paghanap ng ilang anomalya. Maaaring kailanganin mong tingnan ang iba't ibang bansa upang matuklasan ito.
 - [ ] Kalkulahin ang fatality rate at kung paano ito nagbabago sa paglipas ng panahon. *Maaaring gusto mong isaalang-alang ang haba ng sakit sa mga araw upang ilipat ang isang time series bago gawin ang mga kalkulasyon.*

## Pagsusuri ng Mga Papel Tungkol sa COVID-19

- [ ] Bumuo ng co-occurrence matrix ng iba't ibang gamot, at tingnan kung aling mga gamot ang madalas na magkasama (hal., binanggit sa isang abstract). Maaari mong baguhin ang code para sa pagbuo ng co-occurrence matrix para sa mga gamot at diagnosis.
- [ ] I-visualize ang matrix na ito gamit ang heatmap.
- [ ] Bilang karagdagang hamon, i-visualize ang co-occurrence ng mga gamot gamit ang [chord diagram](https://en.wikipedia.org/wiki/Chord_diagram). [Ang library na ito](https://pypi.org/project/chord/) ay maaaring makatulong sa iyo na gumuhit ng chord diagram.
- [ ] Bilang isa pang karagdagang hamon, kunin ang mga dosage ng iba't ibang gamot (tulad ng **400mg** sa *uminom ng 400mg ng chloroquine araw-araw*) gamit ang regular expressions, at bumuo ng dataframe na nagpapakita ng iba't ibang dosage para sa iba't ibang gamot. **Tandaan**: isaalang-alang ang mga numerong halaga na malapit sa tekstuwal na lokasyon ng pangalan ng gamot.

## Rubric

Mahusay | Katamtaman | Kailangan ng Pagpapabuti
--- | --- | -- |
Lahat ng gawain ay tapos, may grapikal na ilustrasyon at paliwanag, kabilang ang hindi bababa sa isa sa dalawang karagdagang hamon | Mahigit sa 5 gawain ang tapos, walang sinubukang karagdagang hamon, o hindi malinaw ang mga resulta | Mas kaunti sa 5 (ngunit higit sa 3) gawain ang tapos, hindi nakakatulong ang mga visualizations upang ipakita ang punto

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.