<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-26T14:51:44+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "sk"
}
-->
# Zadanie na spracovanie údajov v Pythone

V tomto zadaní vás požiadame, aby ste rozpracovali kód, ktorý sme začali vyvíjať v našich výzvach. Zadanie pozostáva z dvoch častí:

## Modelovanie šírenia COVID-19

 - [ ] Vykreslite grafy *R* pre 5-6 rôznych krajín na jednom grafe na porovnanie alebo použite niekoľko grafov vedľa seba.
 - [ ] Zistite, ako počet úmrtí a uzdravení koreluje s počtom nakazených prípadov.
 - [ ] Zistite, ako dlho typicky trvá choroba, vizuálnym porovnaním miery infekcie a miery úmrtí a hľadaním určitých anomálií. Možno budete musieť preskúmať rôzne krajiny, aby ste to zistili.
 - [ ] Vypočítajte mieru úmrtnosti a ako sa mení v čase. *Môžete chcieť zohľadniť dĺžku choroby v dňoch a posunúť jednu časovú sériu pred vykonaním výpočtov.*

## Analýza článkov o COVID-19

- [ ] Vytvorte maticu spoluvýskytu rôznych liekov a zistite, ktoré lieky sa často vyskytujú spolu (t. j. sú spomenuté v jednom abstrakte). Môžete upraviť kód na vytvorenie matice spoluvýskytu pre lieky a diagnózy.
- [ ] Vizualizujte túto maticu pomocou teplotnej mapy.
- [ ] Ako rozšírený cieľ vizualizujte spoluvýskyt liekov pomocou [chordového diagramu](https://en.wikipedia.org/wiki/Chord_diagram). [Táto knižnica](https://pypi.org/project/chord/) vám môže pomôcť nakresliť chordový diagram.
- [ ] Ako ďalší rozšírený cieľ extrahujte dávkovanie rôznych liekov (napríklad **400mg** v *užívajte 400mg chloroquinu denne*) pomocou regulárnych výrazov a vytvorte dataframe, ktorý ukazuje rôzne dávky pre rôzne lieky. **Poznámka**: zvážte číselné hodnoty, ktoré sa nachádzajú v blízkom textovom okolí názvu lieku.

## Hodnotiace kritériá

Vynikajúce | Dostatočné | Potrebuje zlepšenie
--- | --- | -- |
Všetky úlohy sú splnené, graficky znázornené a vysvetlené, vrátane aspoň jedného z dvoch rozšírených cieľov | Viac ako 5 úloh je splnených, žiadne rozšírené ciele nie sú pokusné, alebo výsledky nie sú jasné | Menej ako 5 (ale viac ako 3) úloh je splnených, vizualizácie nepomáhajú demonštrovať pointu

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.