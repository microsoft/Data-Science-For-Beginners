<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-30T18:10:25+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "sl"
}
-->
# Naloga za obdelavo podatkov v Pythonu

V tej nalogi vas bomo prosili, da razširite kodo, ki smo jo začeli razvijati v naših izzivih. Naloga je sestavljena iz dveh delov:

## Modeliranje širjenja COVID-19

 - [ ] Narišite grafe *R* za 5-6 različnih držav na enem grafu za primerjavo ali na več grafih, postavljenih drug ob drugem.
 - [ ] Preučite, kako število smrti in okrevanj korelira s številom okuženih primerov.
 - [ ] Ugotovite, kako dolgo običajno traja bolezen, tako da vizualno primerjate stopnjo okužb in stopnjo smrti ter iščete anomalije. Morda boste morali pogledati različne države, da to ugotovite.
 - [ ] Izračunajte stopnjo smrtnosti in kako se ta spreminja skozi čas. *Morda boste želeli upoštevati dolžino bolezni v dnevih, da premaknete eno časovno serijo, preden izvedete izračune.*

## Analiza člankov o COVID-19

- [ ] Zgradite matriko so-pojavitev različnih zdravil in preverite, katera zdravila se pogosto pojavljajo skupaj (tj. omenjena v enem povzetku). Kodo za gradnjo matrike so-pojavitev za zdravila in diagnoze lahko prilagodite.
- [ ] To matriko vizualizirajte s pomočjo toplotne karte.
- [ ] Kot dodatni cilj vizualizirajte so-pojavitev zdravil z uporabo [krožnega diagrama](https://en.wikipedia.org/wiki/Chord_diagram). [Ta knjižnica](https://pypi.org/project/chord/) vam lahko pomaga narisati krožni diagram.
- [ ] Kot še en dodatni cilj izluščite odmerke različnih zdravil (na primer **400mg** v *vzemite 400mg klorokina dnevno*) z uporabo regularnih izrazov in zgradite podatkovni okvir, ki prikazuje različne odmerke za različna zdravila. **Opomba**: upoštevajte številske vrednosti, ki so v bližini imena zdravila v besedilu.

## Merila ocenjevanja

Odlično | Zadostno | Potrebne izboljšave
--- | --- | -- |
Vse naloge so dokončane, grafično prikazane in razložene, vključno z vsaj enim od dveh dodatnih ciljev | Več kot 5 nalog je dokončanih, dodatni cilji niso poskušeni ali rezultati niso jasni | Manj kot 5 (vendar več kot 3) nalog je dokončanih, vizualizacije ne pomagajo pri prikazu točke

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.